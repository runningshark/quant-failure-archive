# -*- coding: utf-8 -*-
"""T5：跨资产趋势。用 ETF 的复权日线作代理，收益扣掉无风险利率（相当于持有永续合约的成本）。"""
import math
import os

import numpy as np
import pandas as pd

import study as S

MARKETS = ["SPY", "QQQ", "EWJ", "EWY", "EWZ", "EWT", "INDA",                    # 股指
           "GLD", "SLV", "PPLT", "PALL", "USO", "BNO", "UNG", "CPER", "CORN", "WEAT", "URA", "XLE",   # 商品和能源
           "FXE", "FXY", "FXB", "UUP",                                           # 外汇
           "BTC-USD", "ETH-USD"]                                                 # 加密
NAMES = {"SPY": "标普500", "QQQ": "纳指100", "EWJ": "日本", "EWY": "韩国", "EWZ": "巴西", "EWT": "台湾", "INDA": "印度",
         "GLD": "黄金", "SLV": "白银", "PPLT": "铂", "PALL": "钯", "USO": "原油", "BNO": "布伦特原油", "UNG": "天然气",
         "CPER": "铜", "CORN": "玉米", "WEAT": "小麦", "URA": "铀", "XLE": "能源股",
         "FXE": "欧元", "FXY": "日元", "FXB": "英镑", "UUP": "美元指数", "BTC-USD": "比特币", "ETH-USD": "以太坊"}
GROUP = {"股指": MARKETS[:7], "商品": MARKETS[7:19], "外汇": MARKETS[19:23], "加密": MARKETS[23:]}
ANN = 252
BAD_TICKS = [("CPER", "2014-12-04"), ("CPER", "2015-02-02")]


class M(object):
    pass


def load(end=None):
    Y = pd.read_csv(os.path.join(S.DATA, "yahoo_adjclose.csv.gz"), index_col=0, parse_dates=True)
    if end is not None:
        Y = Y.loc[:end]
    cal = Y["SPY"].dropna().index
    cal = cal[cal >= pd.Timestamp("2005-01-03")]
    px = Y[MARKETS].ffill(limit=5).reindex(cal)
    # 数据源里两处明显的错价（铜 ETF 单日 −33% / −29% 后第二天原样弹回，相邻几天价格没动），用前一天的价格代替
    for c, d in BAD_TICKS:
        d = pd.Timestamp(d)
        if d in px.index:
            px.loc[d, c] = px[c].shift(1).loc[d]
    irx = (Y["_IRX"].ffill() / 100.0).reindex(cal).ffill()
    days = pd.Series(cal, index=cal).diff().dt.days.fillna(1.0)
    rf = irx.shift(1).fillna(irx.iloc[0]) * days / 360.0
    ret = px / px.shift(1) - 1.0
    ex = ret.sub(rf, axis=0)
    # BTC / ETH：有币安资金费数据之后，持仓成本用真实资金费
    f = pd.read_csv(os.path.join(S.DATA, "funding_daily.csv.gz"), index_col=0, parse_dates=True)
    for col, y in (("BTCUSDT", "BTC-USD"), ("ETHUSDT", "ETH-USD")):
        fd = f[col]
        cum = fd.fillna(0.0).cumsum().reindex(cal, method="ffill")
        fint = cum.diff()
        have = fd.notna().reindex(cal, method="ffill").fillna(False).astype(bool) & fint.notna()
        ex[y] = np.where(have, ret[y] - fint, ex[y])
    m = M()
    m.px, m.ret, m.ex, m.rf, m.cal = px, ret, ex, rf, cal
    wk = np.asarray(cal.to_period("W-SUN").astype(str))
    m.weekly = np.append(wk[1:] != wk[:-1], True)                                  # 每周最后一个交易日
    return m


def weights(m, looks=(21, 63, 126, 252), vt=0.10, vol_win=60, markets=None, longonly=False, trend=True):
    """趋势分（各回看期方向的平均）× (目标波动率 ÷ 年化波动率) ÷ 当时可交易的市场数。trend=False 时是只做多的风险平价对照。"""
    cols = list(markets or MARKETS)
    ex = m.ex[cols]
    idx = (1.0 + ex.fillna(0.0)).cumprod().where(ex.notna())
    cnt = ex.notna().cumsum()
    ssum = pd.DataFrame(0.0, index=ex.index, columns=cols)
    scnt = pd.DataFrame(0.0, index=ex.index, columns=cols)
    for L in looks:
        ok = (cnt >= L + 1) & idx.notna() & idx.shift(L).notna()
        sgn = np.sign(idx / idx.shift(L) - 1.0)
        if longonly:
            sgn = sgn.clip(lower=0.0)
        ssum = ssum + sgn.where(ok, 0.0)
        scnt = scnt + ok.astype(float)
    score = (ssum / scnt).where(scnt > 0)
    if not trend:
        score = score.notna().astype(float).where(score.notna())
    sigma = ex.rolling(vol_win, min_periods=int(vol_win * 2 / 3)).std() * math.sqrt(ANN)
    raw = score * (vt / sigma)
    n = raw.notna().sum(axis=1).replace(0, np.nan)
    W = raw.div(n, axis=0).fillna(0.0)
    return W


def run(m, cost=S.COST, delay=0, start="2007-01-01", **kw):
    W = weights(m, **kw)
    R = m.ex[W.columns]
    r, tr = S.simulate(W, R, cost=cost, rebal=m.weekly, delay=delay, start=start)
    return r, tr, W
