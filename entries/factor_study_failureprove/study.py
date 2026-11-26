# -*- coding: utf-8 -*-
"""
因子研究的公共部分：读数据、选币池、信号、回测引擎、统计。只用 numpy / pandas。
规则见同目录的《事先登记.md》。入口是 verify.py。
"""
import math
import os

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
RES = os.path.join(HERE, "results")
SPLIT = pd.Timestamp("2024-01-01")      # 这一天之前是训练段，之后是验证段
COST = 0.0010                           # 单边成本：手续费 + 滑点
ANN = 365


class Panel(object):
    pass


def runlen(valid):
    """每个品种到当天为止，连续有价格的天数。"""
    v = valid.values.astype(np.int32)
    out = np.zeros(v.shape, dtype=np.int32)
    out[0] = v[0]
    for i in range(1, len(v)):
        out[i] = (out[i - 1] + 1) * v[i]
    return pd.DataFrame(out, index=valid.index, columns=valid.columns)


def _rd(name):
    return pd.read_csv(os.path.join(DATA, name + ".csv.gz"), index_col=0, parse_dates=True)


def load(end=None):
    """end：只用到这一天为止的数据（自检未来函数时用）。"""
    P = Panel()
    meta = pd.read_csv(os.path.join(DATA, "spot_meta.csv"), index_col=0, encoding="utf-8")
    meta["excluded"] = meta["excluded"].fillna("")
    ok = list(meta.index[meta.excluded == ""])
    close, qvol = _rd("close")[ok], _rd("qvol")[ok]
    fund = _rd("funding_daily")
    if end is not None:
        close, qvol, fund = close.loc[:end], qvol.loc[:end], fund.loc[:end]
    # 短暂停牌（3 天以内）沿用停牌前的价格；更长的断档当作两段，断档前后不连着算收益
    ff = close.ffill(limit=3)
    ff = ff.where(close.bfill().notna())
    P.close = ff
    P.qvol = qvol
    P.meta = meta.loc[ok]
    P.ret = ff / ff.shift(1) - 1
    P.valid = ff.notna()
    P.run = runlen(P.valid)
    P.liq = qvol.rolling(30, min_periods=20).median().shift(1)      # 只用到前一天为止的成交额
    P.fund = fund.reindex(index=ff.index, columns=ff.columns)
    # 下架惩罚用：已下架的币最后一个有价格的日子
    pen = np.zeros(ff.shape)
    endd = ff.index[-1]
    for j, s in enumerate(ff.columns):
        d = close[s].last_valid_index()
        if d is not None and P.meta.loc[s, "status"] != "TRADING" and d < endd - pd.Timedelta(days=5):
            pen[ff.index.get_loc(d), j] = 1.0
    P.pen = pd.DataFrame(pen, index=ff.index, columns=ff.columns)
    P.weekly = np.asarray(ff.index.dayofweek == 6)                  # 周日收盘 = 周一 00:00 UTC
    P.daily = np.ones(len(ff.index), dtype=bool)
    return P


def universe(P, N=30, need_perp=True, min_hist=90, skip=0):
    """当天的币池：有价格、连续历史够长、（需要时）有永续合约；按此前 30 天成交额中位数取前 N。
    skip：跳过排名最靠前的几个（skip=30、N=50 就是第 31 到 80 名）。"""
    elig = P.valid & (P.run >= min_hist) & P.liq.notna()
    if need_perp:
        elig = elig & P.fund.notna()
    rk = P.liq.where(elig).rank(axis=1, ascending=False, method="first")
    return (rk > skip) & (rk <= skip + N)


def signals(P):
    c = P.close
    S = {}
    for k in (7, 14, 28, 56, 90, 180):
        S["mom%d" % k] = (c / c.shift(k) - 1).where(P.run >= k + 1)
    for k, m in ((3, 2), (7, 5), (14, 10), (30, 21), (60, 42)):
        S["fund%d" % k] = P.fund.rolling(k, min_periods=m).mean()
    for k, m in ((14, 10), (30, 20), (60, 40)):
        S["vol%d" % k] = P.ret.rolling(k, min_periods=m).std()
        S["max%d" % k] = P.ret.rolling(k, min_periods=m).max()
    S["ret1"] = P.ret
    S["ret3"] = (c / c.shift(3) - 1).where(P.run >= 4)
    return S


def xs_weights(P, sig, N=30, n_leg=None, weighting="equal", need_perp=True, skip=0, side="both"):
    """横截面多空：信号最高的 n_leg 个做多、最低的 n_leg 个做空，多空各 50%。side 可以只要一侧（拆开看用）。"""
    U = universe(P, N, need_perp, skip=skip).values
    S = sig.values
    n_leg = n_leg or N // 3
    iv = None
    if weighting == "invvol":
        iv = 1.0 / P.ret.rolling(30, min_periods=20).std().values
    W = np.zeros(S.shape)
    for i in range(len(S)):
        cols = np.where(U[i] & np.isfinite(S[i]))[0]
        if len(cols) < 2 * n_leg:
            continue
        order = cols[np.argsort(S[i, cols], kind="mergesort")]
        lo, hi = order[:n_leg], order[-n_leg:]
        if iv is None:
            W[i, hi] = 0.5 / n_leg
            W[i, lo] = -0.5 / n_leg
        else:
            for leg, sgn in ((hi, 1.0), (lo, -1.0)):
                a = iv[i, leg]
                med = np.nanmedian(a) if np.isfinite(a).any() else 1.0
                a = np.where(np.isfinite(a), a, med)
                W[i, leg] = sgn * 0.5 * a / a.sum()
    if side == "long":
        W = np.maximum(W, 0.0)
    elif side == "short":
        W = np.minimum(W, 0.0)
    return pd.DataFrame(W, index=sig.index, columns=sig.columns)


def trend_weights(P, N=30, need_perp=False, longshort=False, looks=(30, 90, 180, 365), vt=0.60, vol_win=60):
    """分散化趋势：趋势分 × min(1, 目标波动率 ÷ 该币波动率) ÷ N。"""
    U = universe(P, N, need_perp).values
    c = P.close.values
    run = P.run.values
    ssum = np.zeros(c.shape)
    scnt = np.zeros(c.shape)
    for L in looks:
        past = np.full(c.shape, np.nan)
        past[L:] = c[:-L]
        ok = np.isfinite(c) & np.isfinite(past) & (run >= L + 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            up = c > past
            s = np.where(up, 1.0, -1.0) if longshort else up.astype(float)
        ssum += np.where(ok, s, 0.0)
        scnt += ok
    with np.errstate(invalid="ignore", divide="ignore"):
        score = ssum / scnt
        sigma = P.ret.rolling(vol_win, min_periods=int(vol_win * 2 / 3)).std().values * math.sqrt(ANN)
        w = score * np.minimum(1.0, vt / sigma) / N
    w = np.where(U & np.isfinite(w), w, 0.0)
    return pd.DataFrame(w, index=P.close.index, columns=P.close.columns)


def simulate(W, R, F=None, cost=COST, rebal=None, delay=0, pen=None, pen_size=0.0, start=None, end=None):
    """
    W：每天收盘时定的目标仓位（占净值的比例），只有 rebal 为真的那些天会真的调仓。
    仓位在收盘时建立，从下一天开始吃收益；两次调仓之间仓位随价格漂移。
    F：每天的资金费率（多头付、空头收）。delay：晚几天执行。pen：下架惩罚的位置。
    返回每天的净收益（Series）和每次调仓的换手（占净值比例）。
    """
    idx = W.index
    Wv = np.nan_to_num(W.values)
    Rv = np.nan_to_num(R.values)
    Fv = np.nan_to_num(F.values) if F is not None else None
    Pv = pen.values if (pen is not None and pen_size) else None
    n = len(idx)
    if rebal is None:
        rebal = np.ones(n, dtype=bool)
    i0 = idx.searchsorted(pd.Timestamp(start)) if start is not None else 0
    i1 = idx.searchsorted(pd.Timestamp(end), side="right") if end is not None else n
    h = np.zeros(Wv.shape[1])
    E = 1.0
    out = np.zeros(n)
    turn = np.zeros(n)
    for i in range(i0, i1):
        E0 = E
        r = Rv[i]
        pnl = h @ r
        if Fv is not None:
            pnl -= h @ Fv[i]
        h = h * (1.0 + r)
        if Pv is not None:
            loss = np.maximum(h, 0.0) * Pv[i] * pen_size
            pnl -= loss.sum()
            h = h - loss
        E += pnl
        j = i - delay
        if j >= i0 and rebal[j]:
            tgt = Wv[j] * E
            tr = np.abs(tgt - h).sum()
            E -= cost * tr
            h = tgt
            turn[i] = tr / E0
        out[i] = E / E0 - 1.0
        if E <= 0:
            out[i + 1:i1] = 0.0
            break
    return pd.Series(out[i0:i1], index=idx[i0:i1]), pd.Series(turn[i0:i1], index=idx[i0:i1])


# ---------------- 统计 ----------------

def nw_t(x, lags=10):
    """均值的 t 值，标准误用 Newey-West 修正自相关。"""
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    n = len(x)
    if n < 30 or x.std() == 0:
        return float("nan")
    m = x.mean()
    e = x - m
    s = (e @ e) / n
    for k in range(1, lags + 1):
        s += 2.0 * (1.0 - k / (lags + 1.0)) * (e[k:] @ e[:-k]) / n
    return m / math.sqrt(s / n) if s > 0 else float("nan")


def ols_alpha(y, x, lags=10):
    """y = alpha + beta·x，返回 (alpha 日均, beta, alpha 的 t 值)，标准误同样用 Newey-West。"""
    d = pd.concat([pd.Series(y), pd.Series(x)], axis=1).dropna()
    yv, xv = d.iloc[:, 0].values, d.iloc[:, 1].values
    if len(yv) < 30:
        return float("nan"), float("nan"), float("nan")
    X = np.column_stack([np.ones(len(xv)), xv])
    b = np.linalg.lstsq(X, yv, rcond=None)[0]
    u = yv - X @ b
    Xu = X * u[:, None]
    S = Xu.T @ Xu
    for k in range(1, lags + 1):
        G = Xu[k:].T @ Xu[:-k]
        S += (1.0 - k / (lags + 1.0)) * (G + G.T)
    Xi = np.linalg.inv(X.T @ X)
    V = Xi @ S @ Xi
    return b[0], b[1], b[0] / math.sqrt(V[0, 0])


def perf(r, ann=ANN):
    r = pd.Series(r).dropna()
    if len(r) < 30:
        return dict(n=len(r))
    eq = (1.0 + r).cumprod()
    sd = r.std() * math.sqrt(ann)
    mu = r.mean() * ann
    return dict(n=int(len(r)), years=round(len(r) / ann, 2), ret=mu, vol=sd, sharpe=mu / sd if sd > 0 else float("nan"),
                t=nw_t(r.values), mdd=float((eq / eq.cummax() - 1.0).min()),
                cagr=float(eq.iloc[-1] ** (ann / len(r)) - 1.0) if eq.iloc[-1] > 0 else -1.0,
                total=float(eq.iloc[-1] - 1.0))


def split_perf(r, ann=ANN, split=SPLIT):
    a, b = perf(r[r.index < split], ann), perf(r[r.index >= split], ann)
    return a, b


def norm_cdf(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))
