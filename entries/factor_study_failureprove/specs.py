# -*- coding: utf-8 -*-
"""
本档案的 11 个失败条目：定义、回测、邻近变体、压力测试、判定。
规则和通过标准来自《事先登记.md》（14 个候选，其中 11 个失败，归档在这里）。
"""
import math
import os

import numpy as np
import pandas as pd

import study as S

P = S.load()
SG = S.signals(P)
BTC = P.ret["BTCUSDT"]
DATA_END = P.close.index[-1]
XS_START, LO_START, BTC_START = "2020-07-01", "2019-07-01", "2018-01-01"

# 美国 13 周国债收益率（年化，%），资金费篮子的收益要减掉它
_tb = pd.read_csv(os.path.join(S.DATA, "tbill_13w.csv.gz"), index_col=0, parse_dates=True)["yield_pct"]
RF_D = (_tb / 100.0 / 365.0).reindex(P.close.index, method="ffill")

# 永续合约自己的日线：有的用它，没有的（很早下架的合约）用现货。只用于"换成合约价格重算"这一项核对
_pc = pd.read_csv(os.path.join(S.DATA, "perp_close.csv.gz"), index_col=0, parse_dates=True).reindex(index=P.close.index, columns=P.close.columns)
_rp = _pc / _pc.shift(1) - 1
RET_PERP = _rp.where(_rp.notna(), P.ret)

# 跨资产趋势要用 Yahoo 的 ETF 日线，这份数据不随仓库分发，需要先运行  py download_data.py --yahoo
try:
    import macro
    MC = macro.load(end=DATA_END) if os.path.exists(os.path.join(S.DATA, "yahoo_adjclose.csv.gz")) else None
except Exception as e:                      # 数据文件损坏等情况：当作没有，跳过 T5
    print("跨资产数据读取失败：%s" % e)
    MC = None

SPECS = [
    dict(no=14, id="X1", name="横截面动量 7 天", kind="xs", sig="mom7", sign=1, rebal="weekly"),
    dict(no=15, id="X2", name="横截面动量 28 天", kind="xs", sig="mom28", sign=1, rebal="weekly"),
    dict(no=16, id="X3", name="横截面动量 90 天", kind="xs", sig="mom90", sign=1, rebal="weekly"),
    dict(no=17, id="X5", name="资金费 30 天多空（多低空高）", kind="xs", sig="fund30", sign=-1, rebal="weekly"),
    dict(no=18, id="X8", name="横截面一日反转（每天调仓）", kind="xs", sig="ret1", sign=-1, rebal="daily"),
    dict(no=19, id="T1", name="30 币分散趋势·现货只做多", kind="trend", perp=False, ls=False, bench="BTC"),
    dict(no=20, id="T2", name="30 币分散趋势·永续多空", kind="trend", perp=True, ls=True),
    dict(no=21, id="T3", name="波动率管理的 BTC 持有", kind="btcvol", bench="BTC"),
    dict(no=22, id="T5", name="跨资产趋势·多空", kind="macro"),
    dict(no=23, id="C1", name="资金费篮子（现货多 + 永续空）", kind="carry"),
    dict(no=24, id="S1", name="做多 BTC、做空山寨篮子", kind="btcalts"),
]
BY_ID = {s["id"]: s for s in SPECS}


def biweekly():
    w = np.where(P.weekly)[0]
    m = np.zeros(len(P.weekly), dtype=bool)
    m[w[::2]] = True
    return m


def run(spec, cost_mult=1.0, delay=0, pen=0.0, perp_price=False, **o):
    """返回 (每天净收益, 每次调仓的换手, 年化系数)。o 里是邻近变体要改的参数。"""
    k = spec["kind"]
    N = o.get("N", 30)
    cost = S.COST * cost_mult
    R = RET_PERP if perp_price else P.ret
    if k == "xs":
        sig = SG[o.get("sig", spec["sig"])] * spec["sign"]
        W = S.xs_weights(P, sig, N=N, n_leg=o.get("n_leg"), weighting=o.get("weighting", "equal"))
        rb = {"daily": P.daily, "weekly": P.weekly, "biweekly": biweekly()}[o.get("rebal", spec["rebal"])]
        r, tr = S.simulate(W, R, F=P.fund, cost=cost, rebal=rb, delay=delay, pen=P.pen, pen_size=pen, start=XS_START)
        return r, tr, 365
    if k == "trend":
        W = S.trend_weights(P, N=N, need_perp=spec["perp"], longshort=spec["ls"], looks=o.get("looks", (30, 90, 180, 365)), vt=o.get("vt", 0.60))
        r, tr = S.simulate(W, R if spec["perp"] else P.ret, F=P.fund if spec["perp"] else None, cost=cost, rebal=P.weekly, delay=delay,
                           pen=P.pen, pen_size=pen, start=XS_START if spec["perp"] else LO_START)
        return r, tr, 365
    if k == "btcvol":
        win = o.get("win", 30)
        sig = P.ret["BTCUSDT"].rolling(win, min_periods=int(win * 2 / 3)).std() * math.sqrt(365)
        W = pd.DataFrame(0.0, index=P.close.index, columns=P.close.columns)
        W["BTCUSDT"] = np.minimum(1.0, o.get("vt", 0.40) / sig).fillna(0.0)
        r, tr = S.simulate(W, P.ret, cost=cost, rebal=P.weekly, delay=delay, start=BTC_START)
        return r, tr, 365
    if k == "btcalts":
        U = S.universe(P, N, True).copy()
        U["BTCUSDT"] = False
        n = U.sum(axis=1).replace(0, np.nan)
        W = (U.astype(float).div(n, axis=0) * -0.5).fillna(0.0)
        W["BTCUSDT"] = np.where(n.notna(), 0.5, 0.0)
        rb = {"weekly": P.weekly, "biweekly": biweekly(), "daily": P.daily}[o.get("rebal", "weekly")]
        r, tr = S.simulate(W, R, F=P.fund, cost=cost, rebal=rb, delay=delay, pen=P.pen, pen_size=pen, start=XS_START)
        return r, tr, 365
    if k == "carry":
        kk, look, thr, notional = o.get("k", 5), o.get("look", 7), o.get("thr", 0.10), 0.70
        U = S.universe(P, N, True).values
        f = SG["fund%d" % look].values
        W = np.zeros(f.shape)
        for i in range(len(f)):
            cols = np.where(U[i] & np.isfinite(f[i]) & (f[i] * 365.0 > thr))[0]
            if len(cols):
                top = cols[np.argsort(f[i, cols], kind="mergesort")][-kk:]
                W[i, top] = -notional / kk          # 永续空单；现货多单对冲掉价格，所以价格收益记 0
        W = pd.DataFrame(W, index=P.close.index, columns=P.close.columns)
        Z = P.ret * 0.0
        r, tr = S.simulate(W, Z, F=P.fund, cost=2.0 * cost, rebal=P.weekly, delay=delay, start=XS_START)   # 两条腿，成本加倍
        return r - RF_D.reindex(r.index).fillna(0.0), tr, 365                                                # 超过国债利率的部分
    if k == "macro":
        if MC is None:
            raise FileNotFoundError("缺少 data/yahoo_adjclose.csv.gz，请先运行： py download_data.py --yahoo")
        kw = {a: o[a] for a in ("looks", "markets", "longonly", "trend") if a in o}
        r, tr, _ = macro.run(MC, cost=cost, delay=delay, **kw)
        return r, tr, 252
    raise ValueError(k)


def variants(spec):
    k = spec["kind"]
    if k == "xs":
        v = [("池子 20 个", dict(N=20)), ("池子 50 个", dict(N=50)), ("每边 6 个", dict(n_leg=6)), ("按波动率倒数加权", dict(weighting="invvol"))]
        v.append(("每周调仓", dict(rebal="weekly")) if spec["rebal"] == "daily" else ("每天调仓", dict(rebal="daily")))
        return v
    if k == "trend":
        return [("只用 30 天", dict(looks=(30,))), ("只用 90 天", dict(looks=(90,))), ("只用 180 天", dict(looks=(180,))), ("只用 365 天", dict(looks=(365,))),
                ("波动率目标减半", dict(vt=0.30)), ("波动率目标加倍", dict(vt=1.20)), ("池子 20 个", dict(N=20)), ("池子 50 个", dict(N=50))]
    if k == "btcvol":
        return [("目标 30%", dict(vt=0.30)), ("目标 50%", dict(vt=0.50)), ("窗口 14 天", dict(win=14)), ("窗口 60 天", dict(win=60))]
    if k == "btcalts":
        return [("池子 20 个", dict(N=20)), ("池子 50 个", dict(N=50)), ("两周调仓", dict(rebal="biweekly"))]
    if k == "carry":
        return [("选 3 个", dict(k=3)), ("选 10 个", dict(k=10)), ("看 3 天", dict(look=3)), ("看 14 天", dict(look=14)),
                ("门槛 0%", dict(thr=0.0)), ("门槛 20%", dict(thr=0.20)), ("池子 50 个", dict(N=50))]
    if k == "macro":
        return [("只用 21 天", dict(looks=(21,))), ("只用 63 天", dict(looks=(63,))), ("只用 126 天", dict(looks=(126,))), ("只用 252 天", dict(looks=(252,))),
                ("去掉加密", dict(markets=[m for m in macro.MARKETS if "USD" not in m]))]
    raise ValueError(k)


def stat(r, ann):
    """全样本 / 训练段 / 验证段的指标，以及对市场基准回归的超额（加密的对 BTC，跨资产的对标普 500）。"""
    out = {}
    for key, rr in (("all", r), ("train", r[r.index < S.SPLIT]), ("test", r[r.index >= S.SPLIT])):
        p = S.perf(rr, ann)
        b = (MC.ex["SPY"] if ann == 252 else BTC).reindex(rr.index)
        if len(rr) >= 60 and b.notna().sum() >= 60:
            a, beta, ta = S.ols_alpha(rr, b)
            p.update(alpha=a * ann, beta=beta, t_alpha=ta)
        out[key] = p
    return out


def key_t(spec, st, part="all"):
    """对门槛用哪个 t：有市场敞口的（T1、T3）看相对 BTC 的超额的 t，其余看净收益的 t。"""
    return st[part].get("t_alpha") if spec.get("bench") else st[part].get("t")


def key_ret(spec, st, part="all"):
    return st[part].get("alpha") if spec.get("bench") else st[part].get("ret")


def extras(r, tr, ann):
    """模板里要填的其他数字：累计收益、调仓次数、换手、按周的胜率和盈亏比。"""
    wk = (1.0 + r).resample("W-SUN").prod() - 1.0
    win, loss = wk[wk > 0], wk[wk < 0]
    te = r[r.index >= S.SPLIT]
    eq_te = (1.0 + te).cumprod()
    return dict(total=float((1.0 + r).prod() - 1.0), total_test=float(eq_te.iloc[-1] - 1.0), mdd_test=float((eq_te / eq_te.cummax() - 1.0).min()),
                rebalances=int((tr > 0).sum()), turnover=float(tr.sum() / (len(r) / ann)),
                week_win=float((wk > 0).mean()), payoff=float(win.mean() / -loss.mean()) if len(loss) and len(win) else float("nan"))


def evaluate(spec):
    k = spec["kind"]
    r, tr, ann = run(spec)
    st = stat(r, ann)
    res = dict(no=spec["no"], id=spec["id"], name=spec["name"], kind=k, ann=ann, start=str(r.index[0].date()), end=str(r.index[-1].date()),
               stats=st, extras=extras(r, tr, ann), uses_alpha=bool(spec.get("bench")))
    stress = {}
    for label, kw in (("成本翻倍", dict(cost_mult=2.0)), ("晚一天执行", dict(delay=1)), ("下架惩罚 30%", dict(pen=0.30)), ("零成本", dict(cost_mult=0.0))):
        if label.startswith("下架") and k in ("btcvol", "carry", "macro"):
            continue
        rr, _, _ = run(spec, **kw)
        s2 = stat(rr, ann)
        stress[label] = dict(ret=key_ret(spec, s2), t=key_t(spec, s2), sharpe=s2["all"].get("sharpe"), raw_ret=s2["all"].get("ret"))
    res["stress"] = stress
    var = {}
    for label, kw in variants(spec):
        rr, _, _ = run(spec, **kw)
        s2 = stat(rr, ann)
        var[label] = dict(ret=key_ret(spec, s2), t=key_t(spec, s2), sharpe=s2["all"].get("sharpe"))
    res["variants"] = var
    if k in ("xs", "btcalts") or (k == "trend" and spec["perp"]):
        rr, _, _ = run(spec, perp_price=True)
        s2 = stat(rr, ann)
        res["perp_price"] = dict(ret=s2["all"]["ret"], sharpe=s2["all"]["sharpe"], t=s2["all"]["t"], mdd=s2["all"]["mdd"])
    # 判定（和《事先登记.md》第 5 节一致）
    t_all, t_tr, t_te = key_t(spec, st, "all"), key_t(spec, st, "train"), key_t(spec, st, "test")
    r_tr, r_te = key_ret(spec, st, "train"), key_ret(spec, st, "test")
    ta = st["all"].get("t_alpha", float("nan"))
    vt = [v["t"] for v in var.values()]
    vr = [v["ret"] for v in var.values()]
    same_sign = all(x > 0 for x in vr)
    two_thirds = sum(1 for x in vt if x >= 1.5) >= math.ceil(len(vt) * 2 / 3)
    stress_ok = all(stress[x]["ret"] > 0 for x in stress if x != "零成本")
    c = {"全样本 t ≥ 3": t_all >= 3.0, "训练段和验证段都为正且 t ≥ 2": (r_tr > 0 and r_te > 0 and t_tr >= 2.0 and t_te >= 2.0),
         "对市场回归后的超额 t ≥ 2": ta >= 2.0, "邻近变体全部为正且三分之二 t ≥ 1.5": same_sign and two_thirds,
         "成本翻倍、晚一天、下架惩罚后仍为正": stress_ok}
    if all(c.values()):
        verdict = "通过"
    elif t_all >= 2.0 and r_tr > 0 and r_te > 0 and ta >= 2.0 and stress_ok and same_sign:
        verdict = "待观察"
    else:
        verdict = "失败"
    res.update(checks=c, verdict=verdict, key=dict(t_all=t_all, t_train=t_tr, t_test=t_te, ret_train=r_tr, ret_test=r_te))
    yr = {}
    for y in sorted(set(r.index.year)):
        x = r[r.index.year == y]
        if len(x) > 20:
            eq = (1 + x).cumprod()
            yr[int(y)] = dict(ret=float(eq.iloc[-1] - 1), mdd=float((eq / eq.cummax() - 1).min()))
    res["yearly"] = yr
    return res, r


def benchmarks():
    """对照组：一直持有、等权持有、BTC 100 日均线。"""
    out = {}
    W = pd.DataFrame(0.0, index=P.close.index, columns=P.close.columns)
    W["BTCUSDT"] = 1.0
    for label, start in (("BTC 一直持有（2018 起）", BTC_START), ("BTC 一直持有（2019-07 起）", LO_START), ("BTC 一直持有（2020-07 起）", XS_START)):
        once = np.zeros(len(W), dtype=bool)
        once[W.index.searchsorted(pd.Timestamp(start))] = True
        r, _ = S.simulate(W, P.ret, cost=S.COST, rebal=once, start=start)
        out[label] = (r, 365)
    U = S.universe(P, 30, False)
    We = U.astype(float).div(U.sum(axis=1).replace(0, np.nan), axis=0).fillna(0.0)
    r, _ = S.simulate(We, P.ret, cost=S.COST, rebal=P.weekly, start=LO_START)
    out["池子 30 个币等权持有（2019-07 起）"] = (r, 365)
    c = P.close["BTCUSDT"]
    Wm = pd.DataFrame(0.0, index=P.close.index, columns=P.close.columns)
    Wm["BTCUSDT"] = (c > c.rolling(100).mean()).astype(float)
    chg = np.asarray(Wm["BTCUSDT"].diff().fillna(0.0) != 0) | (np.arange(len(Wm)) == Wm.index.searchsorted(pd.Timestamp(BTC_START)))
    r, _ = S.simulate(Wm, P.ret, cost=S.COST, rebal=chg, start=BTC_START)
    out["BTC 100 日均线择时（2018 起）"] = (r, 365)
    if MC is not None:
        r, _, _ = macro.run(MC, trend=False)
        out["跨资产只做多·按风险均摊（2007 起）"] = (r, 252)
        W1 = pd.DataFrame(1.0, index=MC.cal, columns=["SPY"])
        once = np.zeros(len(MC.cal), dtype=bool)
        once[MC.cal.searchsorted(pd.Timestamp("2007-01-01"))] = True
        r, _ = S.simulate(W1, MC.ex[["SPY"]], cost=S.COST, rebal=once, start="2007-01-01")
        out["标普 500 超额收益（2007 起）"] = (r, 252)
    return out


def clean(o):
    """把 numpy 数值和 NaN 变成 JSON 能存的样子。"""
    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (bool, np.bool_)):
        return bool(o)
    if isinstance(o, (int, np.integer)):
        return int(o)
    if isinstance(o, (float, np.floating)):
        return float(o) if math.isfinite(o) else None
    return o
