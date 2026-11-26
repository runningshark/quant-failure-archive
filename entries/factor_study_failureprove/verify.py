# -*- coding: utf-8 -*-
"""
复现本档案的 11 个失败条目。

  py verify.py            全部
  py verify.py X1 T5      只跑指定的条目（用编号 X1 … S1，或档案号 14 … 24）

每条会打印：全区间 / 训练段 / 验证段的数字、对市场回归后的超额、压力测试、邻近变体、分年度、判定，
然后和 results/expected.json 里归档时的数字逐项核对。
结果同时写到 results/output.txt（全部）或 results/<编号>.txt（单条）。

需要 pandas 和 numpy：  pip install pandas numpy
跨资产趋势（T5）要用的 ETF 日线不随仓库分发，先运行一次：  py download_data.py --yahoo
"""
import json
import math
import os
import sys
import time

T0 = time.time()
import study as S          # noqa: E402
import specs               # noqa: E402

LINES = []


def out(s=""):
    print(s)
    LINES.append(s)


def pc(x, d=1):
    return "—" if x is None or (isinstance(x, float) and not math.isfinite(x)) else "%+.*f%%" % (d, 100 * x)


def nm(x, d=2):
    return "—" if x is None or (isinstance(x, float) and not math.isfinite(x)) else "%.*f" % (d, x)


def show(res):
    a, tr, te, ex = res["stats"]["all"], res["stats"]["train"], res["stats"]["test"], res["extras"]
    out("=" * 78)
    out("%d · %s  %s" % (res["no"], res["id"], res["name"]))
    out("区间 %s → %s（%.1f 年），成本单边 %.2f%%，分界 %s" % (res["start"], res["end"], a["years"], 100 * S.COST, S.SPLIT.date()))
    for lab, p in (("全区间", a), ("训练段", tr), ("验证段", te)):
        out("  %s  年化 %7s  波动 %6s  夏普 %5s  t %5s  最大回撤 %7s  | 对市场回归：超额 %7s  贝塔 %5s  超额 t %5s" % (
            lab, pc(p.get("ret")), pc(p.get("vol")).lstrip("+"), nm(p.get("sharpe")), nm(p.get("t")), pc(p.get("mdd")),
            pc(p.get("alpha")), nm(p.get("beta")), nm(p.get("t_alpha"))))
    out("  累计：全区间 %s，验证段 %s（验证段最大回撤 %s）" % (pc(ex["total"]), pc(ex["total_test"]), pc(ex["mdd_test"])))
    out("  调仓 %d 次，年换手 %.1f 倍；按周算赚钱的周占 %.0f%%，平均赚 ÷ 平均亏 = %s" % (ex["rebalances"], ex["turnover"], 100 * ex["week_win"], nm(ex["payoff"])))
    key = "相对 BTC 的超额" if res["uses_alpha"] else "年化净收益"
    out("  压力测试（%s / t）：" % key + "；".join("%s %s / %s" % (k, pc(v["ret"]), nm(v["t"])) for k, v in res["stress"].items()))
    out("  邻近变体（%s / t）：" % key + "；".join("%s %s / %s" % (k, pc(v["ret"]), nm(v["t"])) for k, v in res["variants"].items()))
    if "perp_price" in res:
        q = res["perp_price"]
        out("  换成永续合约自己的价格重算：年化 %s，夏普 %s，t %s，最大回撤 %s" % (pc(q["ret"]), nm(q["sharpe"]), nm(q["t"]), pc(q["mdd"])))
    out("  分年度：" + "  ".join("%s %s" % (y, pc(v["ret"])) for y, v in res["yearly"].items()))
    miss = [k for k, v in res["checks"].items() if not v]
    out("  判定：%s。没有满足的标准：%s" % (res["verdict"], "；".join(miss) if miss else "无"))


def compare(res, exp):
    """和归档时的数字核对。跨资产那条的数据是复现时重新下载的，容差放宽。"""
    tol = 0.03 if res["kind"] == "macro" else 0.002
    a, b = res["stats"]["all"], exp["stats"]["all"]
    items = [("年化", a["ret"], b["ret"]), ("夏普", a["sharpe"], b["sharpe"]), ("t", a["t"], b["t"]), ("最大回撤", a["mdd"], b["mdd"]),
             ("训练段 t", res["key"]["t_train"], exp["key"]["t_train"]), ("验证段 t", res["key"]["t_test"], exp["key"]["t_test"])]
    bad = [n for n, x, y in items if abs(x - y) > tol * max(1.0, abs(y))]
    if res["verdict"] != exp["verdict"]:
        bad.append("判定")
    return bad


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    update = "--update" in sys.argv
    want = []
    for a in args:
        hit = [s for s in specs.SPECS if a.upper() == s["id"] or a == str(s["no"])]
        if not hit:
            print("不认识的条目：%s。可用的：%s" % (a, "、".join("%s(%d)" % (s["id"], s["no"]) for s in specs.SPECS)))
            sys.exit(2)
        want += hit
    want = want or specs.SPECS
    efn = os.path.join(S.RES, "expected.json")
    expected = json.load(open(efn, encoding="utf-8")) if os.path.exists(efn) else {}
    out("数据：币安现货日线 %s 到 %s，%d 个品种（其中已下架 %d 个）；资金费率 %d 个币" % (
        specs.P.close.index[0].date(), specs.DATA_END.date(), specs.P.close.shape[1], int((specs.P.meta.status != "TRADING").sum()),
        int(specs.P.fund.notna().any().sum())))
    ok = skipped = 0
    results, series = {}, {}
    for spec in want:
        if spec["kind"] == "macro" and specs.MC is None:
            out("=" * 78)
            out("%d · %s  %s：跳过。缺少 data/yahoo_adjclose.csv.gz，请先运行  py download_data.py --yahoo" % (spec["no"], spec["id"], spec["name"]))
            skipped += 1
            continue
        res, ret = specs.evaluate(spec)
        results[spec["id"]] = res
        series[spec["id"]] = ret
        show(res)
        if update or spec["id"] not in expected:
            out("  核对：没有归档数字可比（这次的结果已记为归档数字）" if update else "  核对：results/expected.json 里没有这一条")
            expected[spec["id"]] = specs.clean(res)
            ok += 1 if update else 0
            continue
        bad = compare(res, expected[spec["id"]])
        if bad:
            out("  核对：和归档数字不一致 → %s" % "、".join(bad))
        else:
            out("  核对：和归档数字一致")
            ok += 1
    out("=" * 78)
    n = len(want) - skipped
    out("结果：%d / %d 条和归档数字一致%s；判定为失败的 %d 条。用时 %.0f 秒" % (
        ok, n, "（另有 %d 条因缺数据跳过）" % skipped if skipped else "", sum(1 for r in results.values() if r["verdict"] == "失败"), time.time() - T0))
    os.makedirs(S.RES, exist_ok=True)
    if update:
        import pandas as pd
        json.dump(expected, open(efn, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        cr = {k: v for k, v in series.items() if specs.BY_ID[k]["kind"] != "macro"}
        if cr:
            pd.DataFrame(cr).to_csv(os.path.join(S.RES, "daily_returns_crypto.csv"), float_format="%.8f")
        if "T5" in series:
            pd.DataFrame({"T5": series["T5"]}).to_csv(os.path.join(S.RES, "daily_returns_T5.csv"), float_format="%.8f")
    name = "output.txt" if len(want) == len(specs.SPECS) else "_".join(s["id"] for s in want) + ".txt"
    with open(os.path.join(S.RES, name), "w", encoding="utf-8") as f:
        f.write("\n".join(LINES) + "\n")
    sys.exit(0 if ok == n else 1)


if __name__ == "__main__":
    main()
