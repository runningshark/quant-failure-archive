# -*- coding: utf-8 -*-
"""自检：回测引擎有没有算错、有没有用到未来的数据、随机信号会不会凭空赚钱。"""
import sys, time
import numpy as np, pandas as pd
import study as S

t0 = time.time()
P = S.load()
print("数据：%s 到 %s，%d 个品种（其中已下架 %d 个）" % (P.close.index[0].date(), P.close.index[-1].date(), P.close.shape[1], (P.meta.status != "TRADING").sum()))
ok = True

# 1. 引擎：满仓 BTC、零成本，应该正好等于 BTC 的涨幅
W = pd.DataFrame(0.0, index=P.close.index, columns=P.close.columns); W["BTCUSDT"] = 1.0
once = np.zeros(len(W), bool); i0 = W.index.searchsorted(pd.Timestamp("2020-01-01")); once[i0] = True
r, _ = S.simulate(W, P.ret, cost=0.0, rebal=once, start="2020-01-01")
a = (1 + r).prod(); b = P.close["BTCUSDT"].iloc[-1] / P.close["BTCUSDT"].loc["2020-01-01"]
print("[1] 引擎对账：回测净值 %.6f，BTC 实际涨幅倍数 %.6f" % (a, b)); ok &= abs(a / b - 1) < 1e-9

# 2. 成本：每周从 0 到满仓再到 0，零收益时每次调仓应正好扣 cost × 换手
Z = P.ret * 0.0
W2 = W.copy(); wk = np.where(P.weekly)[0]; W2.iloc[wk[1::2]] = 0.0
r2, tr = S.simulate(W2, Z, cost=0.001, rebal=P.weekly, start="2022-01-01", end="2022-12-31")
nreb = int((tr > 0).sum()); exp = (1 - 0.002) ** (nreb // 2)      # 一买一卖合计扣 0.2%（成本从净值里扣，按调仓前的净值下单）
print("[2] 成本对账：调仓 %d 次，净值 %.6f，应为 %.6f" % (nreb, (1 + r2).prod(), exp)); ok &= abs((1 + r2).prod() / exp - 1) < 1e-6

# 3. 资金费：持有 BTC 永续空单一年，价格收益设为 0，净值应等于资金费累加
Ws = -W
r3, _ = S.simulate(Ws, Z, F=P.fund, cost=0.0, rebal=once, start="2020-01-01", end="2020-12-31")
f = P.fund["BTCUSDT"].loc["2020-01-02":"2020-12-31"].sum()
g = (1 + r3).prod() - 1
print("[3] 资金费对账：空单一年净值增加 %.6f，资金费率合计 %.6f" % (g, f)); ok &= abs(g - f) < 1e-9

# 4. 未来函数：把数据截到 2023-06-30 再算，截止日及之前的目标仓位必须完全一样
cut = pd.Timestamp("2023-06-30")
Pc = S.load(end=cut)
Sg, Sc = S.signals(P), S.signals(Pc)
bad = 0
for name, kw in (("mom28", {}), ("fund7", {}), ("vol30", {}), ("max30", {}), ("ret1", {})):
    A = S.xs_weights(P, Sg[name]).loc[:cut]; B = S.xs_weights(Pc, Sc[name])
    d = float((A - B).abs().values.max()); bad += d > 1e-12
    print("    横截面 %-6s 最大差异 %.2e" % (name, d))
for ls in (False, True):
    A = S.trend_weights(P, need_perp=ls, longshort=ls).loc[:cut]; B = S.trend_weights(Pc, need_perp=ls, longshort=ls)
    d = float((A - B).abs().values.max()); bad += d > 1e-12
    print("    趋势 %s 最大差异 %.2e" % ("多空" if ls else "只做多", d))
print("[4] 未来函数检查：%s" % ("通过" if not bad else "没通过")); ok &= not bad

# 5. 安慰剂：每周随机排序做多空 300 次。零成本时 t 值应以 0 为中心、标准差约 1；加成本后应整体为负
rng = np.random.default_rng(20261126)
U = S.universe(P, 30, True)
ts0, ts1 = [], []
NPL = int(sys.argv[1]) if len(sys.argv) > 1 else 300
for k in range(NPL):
    sig = pd.DataFrame(rng.random(P.close.shape), index=P.close.index, columns=P.close.columns)
    Wr = S.xs_weights(P, sig)
    r0, _ = S.simulate(Wr, P.ret, F=P.fund, cost=0.0, rebal=P.weekly, start="2020-07-01")
    r1, _ = S.simulate(Wr, P.ret, F=P.fund, cost=S.COST, rebal=P.weekly, start="2020-07-01")
    ts0.append(S.nw_t(r0.values)); ts1.append(S.nw_t(r1.values))
ts0, ts1 = np.array(ts0), np.array(ts1)
print("[5] 随机信号 %d 次：" % NPL + "零成本 t 均值 %.2f、标准差 %.2f、|t|>2 的占 %.1f%%、|t|>3 的占 %.1f%%；加成本后 t 均值 %.2f、最大 %.2f"
      % (ts0.mean(), ts0.std(), 100 * (np.abs(ts0) > 2).mean(), 100 * (np.abs(ts0) > 3).mean(), ts1.mean(), ts1.max()))
ok &= abs(ts0.mean()) < 0.35 and 0.7 < ts0.std() < 1.4

# 6. 币池情况
for need in (False, True):
    m = S.universe(P, 30, need)
    cnt = m.sum(axis=1)
    print("[6] 币池（%s）每年平均个数：" % ("要求有永续" if need else "现货"), {y: round(float(cnt[cnt.index.year == y].mean()), 1) for y in range(2018, 2027)})
m = S.universe(P, 30, True)
dead = (P.meta.status != "TRADING").reindex(m.columns).values
print("    币池里后来被下架的币占比（按年）：", {y: "%.0f%%" % (100 * m[m.index.year == y].values[:, dead].sum() / max(1, m[m.index.year == y].values.sum())) for y in range(2020, 2027)})
print("\n结论：%s（用时 %.0f 秒）" % ("全部通过" if ok else "有项目没通过", time.time() - t0))
sys.exit(0 if ok else 1)
