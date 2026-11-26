# -*- coding: utf-8 -*-
"""
生成 reports/ 下 11 份条目档案、FAILURE_REPORT.md 和 README.md。
数字全部来自 results/expected.json（verify.py --update 写出的归档数字）和当场算的对照组，不手抄。
用法：  py tools/make_reports.py
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import study as S          # noqa: E402
import specs               # noqa: E402

REPO = "factor_study_failureprove"
ARCHIVE = "https://github.com/runningshark/quant-failure-archive"
# 这份档案可以放在总仓库的 entries/ 文件夹里（默认），也可以单独一个仓库（环境变量 LAYOUT=standalone）
STANDALONE = os.environ.get("LAYOUT", "inrepo") == "standalone"
URL = "https://github.com/runningshark/" + REPO if STANDALONE else ARCHIVE + "/tree/master/entries/" + REPO
CLONE = ["git clone https://github.com/runningshark/" + REPO, "cd " + REPO] if STANDALONE else ["git clone " + ARCHIVE, "cd quant-failure-archive/entries/" + REPO]
E = json.load(open(os.path.join(S.RES, "expected.json"), encoding="utf-8"))
BENCH = {k: specs.stat(r, ann) for k, (r, ann) in specs.benchmarks().items()}
BENCH_TOTAL = {k: float((1 + r[r.index >= S.SPLIT]).prod() - 1) for k, (r, ann) in specs.benchmarks().items()}
json.dump(specs.clean(BENCH), open(os.path.join(S.RES, "benchmarks.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

pc = lambda x, d=1: "—" if x is None else ("%+.*f%%" % (d, 100 * x)).replace("-", "−")
pu = lambda x, d=1: "—" if x is None else ("%.*f%%" % (d, 100 * x)).replace("-", "−")
nm = lambda x, d=2: "—" if x is None else ("%.*f" % (d, x)).replace("-", "−")
up1 = lambda x: "%.1f" % (math.ceil(x * 10) / 10.0)          # 向上取到一位小数，用在“都在 x 以下”这种说法里
bold = lambda s: "**" + s.replace("（", "**（", 1) if "（" in s else "**" + s + "**"

SLUG = {"X1": "xs_momentum_7d", "X2": "xs_momentum_28d", "X3": "xs_momentum_90d", "X5": "funding_30d", "X8": "xs_reversal_1d",
        "T1": "trend_spot", "T2": "trend_perp", "T3": "btc_vol_managed", "T5": "cross_asset_trend", "C1": "funding_basket", "S1": "btc_vs_alts"}
FILE = {i: "reports/%d_%s_%s.md" % (E[i]["no"], i, s) for i, s in SLUG.items()}

XS_RULE = "每周日收盘（周一 00:00 UTC），在成交额最高的 30 个有永续合约的币里，%s，等权，多空各占资金的 50%%，持有一周。"
RULE = {
    "X1": XS_RULE % "按过去 7 天涨幅排序，做多最高的 10 个、做空最低的 10 个",
    "X2": XS_RULE % "按过去 28 天涨幅排序，做多最高的 10 个、做空最低的 10 个",
    "X3": XS_RULE % "按过去 90 天涨幅排序，做多最高的 10 个、做空最低的 10 个",
    "X5": XS_RULE % "按过去 30 天的平均资金费率排序，做多费率最低的 10 个、做空费率最高的 10 个",
    "X8": "每天收盘，在成交额最高的 30 个有永续合约的币里，按当天的涨跌排序，做多跌得最多的 10 个、做空涨得最多的 10 个，等权，多空各占资金的 50%，持有一天。",
    "T1": "每周日收盘，对成交额最高的 30 个币（现货）：趋势分 = 现价高于 30 / 90 / 180 / 365 天前价格的比例（0 到 1）；仓位 = 趋势分 × min(1, 60% ÷ 该币年化波动率) ÷ 30。只做多，总仓位不超过 100%。",
    "T2": "每周日收盘，对成交额最高的 30 个有永续合约的币：趋势分 = 30 / 90 / 180 / 365 天四个回看期涨跌方向的平均（−1 到 1）；仓位 = 趋势分 × min(1, 60% ÷ 该币年化波动率) ÷ 30。可以做空，计入资金费。",
    "T3": "BTC 现货仓位 = min(1, 40% ÷ 过去 30 天的年化波动率)，每周日收盘调一次，不加杠杆。",
    "T5": "25 个市场（美股、纳指、日本、韩国、巴西、台湾、印度股指；黄金、白银、铂、钯、原油、布油、天然气、铜、玉米、小麦、铀、能源股；欧元、日元、英镑、美元指数；BTC、ETH），用 ETF 的复权日线作代理。每周最后一个交易日：趋势分 = 21 / 63 / 126 / 252 个交易日四个回看期涨跌方向的平均；仓位 = 趋势分 × (10% ÷ 年化波动率) ÷ 当时可交易的市场数。收益扣掉无风险利率（相当于持有永续合约的成本），BTC 和 ETH 在有资金费数据之后扣真实资金费。",
    "C1": "每周日收盘，在成交额最高的 30 个有永续合约的币里，选过去 7 天平均资金费率最高的 5 个，只持有年化超过 10% 的；每个币买现货、做空等量永续，名义仓位合计占资金的 70%（其余作保证金）。收益 = 收到的资金费 − 换仓成本（两条腿各单边 0.10%）− 美国短期国债利率。不计基差变动。",
    "S1": "每周日收盘，BTC 永续多单占资金的 50%，成交额最高的 30 个有永续合约的币里其余 29 个等权做空，合计占 50%。计入资金费。",
}

LTW = "Liu、Tsyvinski、Wu《Common Risk Factors in Cryptocurrency》（Journal of Finance，2022；NBER w25882）"
CLAIM = {
    "X1": dict(src=LTW + "。论文把过去 1 到 4 周的涨幅列为能预测横截面收益的动量因子。",
               ret="论文报告动量多空组合的收益显著为正；这里没有复算它的样本，原文的具体数字见论文。后来的综述《Cryptocurrency as an Investable Asset Class: Coming of Age》（2025）复核后仍报告动量多空收益显著为正。",
               data="原文用的是全市场的币（含大量流动性很差的小币），周频，主要结果不扣交易成本。"),
    "X2": dict(src=LTW + "。四周动量是论文里动量因子的回看期之一。",
               ret="论文报告过去 1 到 4 周涨幅排序的多空组合收益显著为正；原文的具体数字见论文。",
               data="原文用的是全市场的币（含大量流动性很差的小币），周频，主要结果不扣交易成本。"),
    "X3": dict(src="股票里经典的 3 到 12 个月动量（Jegadeesh、Titman，1993）直接搬到币上，是很多“强者恒强”轮动策略的依据。加密文献对这么长的周期本来就没有一致结论。",
               ret="没有一篇可以直接对照的原文。本条检验的是“过去三个月涨得多的币，之后继续跑赢”这个说法。",
               data="—"),
    "X5": dict(src="Fan、Jiao、Lu、Tong《The Risk and Return of Cryptocurrency Carry Trade》（SSRN 4666425）。",
               ret="论文报告横截面套息多空组合年化 43.4%，夏普 0.74。本条检验的是把排序信号换成“过去 30 天平均资金费率”的版本，回看天数是这次研究自己定的，不是原文的设定。",
               data="原文的样本、交易所和成本设定没有在这里复核。"),
    "X8": dict(src="“短期反转”的常见说法。例如公开项目 prams2104/crypto-momentum-backtest 报告：2025–2026 样本外，横截面反转扣成本前的年化超额 73%（t = 4.64），但每天换手 138%，扣成本后为负。本档案第 05 条（小时反转）也是零成本为正、扣成本后全亏。",
               ret="零成本下显著为正；扣成本后是否还有，是要检验的问题。",
               data="上述项目按 0.20% 的交易成本计算；它的币池和这里不同。"),
    "T1": dict(src="时间序列动量：Moskowitz、Ooi、Pedersen《Time Series Momentum》（Journal of Financial Economics，2012），做法是很多品种各自看趋势、按波动率定仓位。加密上的例子：arXiv 2602.11708 报告一套趋势系统 2022–2024 年在 150 多个交易对上夏普 2.41、最大回撤 −12.7%。本档案第 01 条的复核里，16 个币的日线趋势等权组合年化 +17.0%、t = 1.63。",
               ret="分散到很多币上的趋势跟随，风险调整后明显好于持有。",
               data="各篇不同；上面那篇 arXiv 论文用 6 小时线。"),
    "T2": dict(src="同第 19 条（时间序列动量），这里是可以做空的永续合约版本。",
               ret="分散到很多币上的多空趋势跟随，不依赖大盘方向也能赚钱。",
               data="各篇不同。"),
    "T3": dict(src="Moreira、Muir《Volatility-Managed Portfolios》（Journal of Finance，2017）：波动率高的时候减仓、低的时候加仓，在股票因子上能提高夏普并产生显著的超额。",
               ret="按波动率管理仓位，相对一直持有有超额收益。",
               data="原文是美股因子的月频数据，可以加杠杆。这里搬到 BTC 上，不加杠杆。"),
    "T5": dict(src="趋势跟随是管理期货基金最经典的策略：Hurst、Ooi、Pedersen《A Century of Evidence on Trend-Following Investing》；AQR《Trends Everywhere》。",
               ret="《Trends Everywhere》报告 1985–2017 年传统资产上 12 个月时间序列动量的毛夏普为 1.17（未扣成本）。",
               data="原文用几十到上百个期货和远期品种，报告的是扣成本前的夏普。这里用 25 个现在在 Hyperliquid 的 xyz 市场或币安 TradFi 永续上有对应合约的品种，成本按零售水平算。"),
    "C1": dict(src="“资金费套利”的流行说法：买现货、空永续，价格风险对冲掉，只收资金费。综述《Cryptocurrency as an Investable Asset Class: Coming of Age》（2025）报告这类套息策略全样本平均收益约 8%、波动约 0.8%。本档案第 10 条已经测过 BTC、ETH 等 6 个币各自做的版本，结论是收益衰减。",
               ret="接近无风险的稳定收益。本条检验的是“每周挑资金费最高的几个币来做”能不能把衰减的收益找回来。",
               data="综述的成本和样本设定没有在这里复核。"),
    "S1": dict(src="“山寨币长期跑输比特币”的流行说法（做多 BTC 市占率）。没有找到可以直接对照的正式论文，这是本次研究自己登记的假设。",
               ret="山寨币相对 BTC 持续走弱，多 BTC、空山寨可以稳定赚钱。",
               data="—"),
}

b = lambda k, part="all": BENCH[k][part]
hold18, hold19, ew19, ma18 = "BTC 一直持有（2018 起）", "BTC 一直持有（2019-07 起）", "池子 30 个币等权持有（2019-07 起）", "BTC 100 日均线择时（2018 起）"


def reasons(i):
    r = E[i]
    a, tr, te, ex, st, va, yr = r["stats"]["all"], r["stats"]["train"], r["stats"]["test"], r["extras"], r["stress"], r["variants"], r["yearly"]
    y = lambda k: pc(yr[str(k)]["ret"])
    if i == "X1":
        return ["**成本。** 零成本年化 %s（t = %s）；年换手 %.0f 倍，单边 0.10%% 一年吃掉约 %s，净 t 只剩 %s；成本翻倍后 t = %s。见 `verify.py` 输出的“压力测试”一行。" % (
                    pc(st["零成本"]["ret"]), nm(st["零成本"]["t"]), ex["turnover"], pu(st["零成本"]["ret"] - a["ret"]), nm(a["t"]), nm(st["成本翻倍"]["t"])),
                "**信号衰减得快。** 晚一天执行，年化从 %s 掉到 %s。" % (pc(a["ret"]), pc(st["晚一天执行"]["ret"])),
                "**邻近变体不稳。** 池子 20 个 t = %s、按波动率倒数加权 t = %s、每天调仓 t = %s，只有“每边 6 个”接近 2（%s）。见“邻近变体”一行。" % (
                    nm(va["池子 20 个"]["t"]), nm(va["按波动率倒数加权"]["t"]), nm(va["每天调仓"]["t"]), nm(va["每边 6 个"]["t"])),
                "**两段都不显著，分年很不均匀。** 训练段 t = %s，验证段 t = %s；2020 下半年 %s，2021–2023 三年分别是 %s、%s、%s。" % (
                    nm(r["key"]["t_train"]), nm(r["key"]["t_test"]), y(2020), y(2021), y(2022), y(2023))]
    if i == "X2":
        return ["**没有信号。** 全区间 t = %s，零成本也只有 %s。" % (nm(a["t"]), nm(st["零成本"]["t"])),
                "**验证段几乎为零。** 年化 %s（t = %s），累计 %s，期间最大回撤 %s。" % (pc(te["ret"]), nm(r["key"]["t_test"]), pc(ex["total_test"]), pu(ex["mdd_test"])),
                "**变体里没有一个 t 到 2。** 从 %s 到 %s。2021、2022、2024、2026 四年为负（%s、%s、%s、%s）。" % (
                    nm(min(v["t"] for v in va.values())), nm(max(v["t"] for v in va.values())), y(2021), y(2022), y(2024), y(2026))]
    if i == "X3":
        return ["**方向和声称相反。** 做多过去 90 天涨得多的、做空涨得少的：年化 %s，累计 %s，最大回撤 %s。" % (pc(a["ret"]), pc(ex["total"]), pu(a["mdd"])),
                "**怎么改都是负的。** 5 个邻近变体、3 项压力测试全部为负，零成本也是 %s。" % pc(st["零成本"]["ret"]),
                "**越近越差。** 训练段年化 %s（t = %s），验证段 %s（t = %s）；2021 年以后只有 2023 年勉强为正（%s）。" % (
                    pc(tr["ret"]), nm(r["key"]["t_train"]), pc(te["ret"]), nm(r["key"]["t_test"]), y(2023)),
                "**不是成本问题。** 年换手只有 %.0f 倍。" % ex["turnover"]]
    if i == "X5":
        return ["**没有信号。** 年化 %s，t = %s；零成本 t = %s。" % (pc(a["ret"]), nm(a["t"]), nm(st["零成本"]["t"])),
                "**晚一天执行就转负。** 年化 %s。" % pc(st["晚一天执行"]["ret"]),
                "**验证段没有收益。** 年化 %s（t = %s），累计 %s，期间最大回撤 %s；2022、2023、2025、2026 四年为负。" % (
                    pc(te["ret"]), nm(r["key"]["t_test"]), pc(ex["total_test"]), pu(ex["mdd_test"])),
                "**变体也不显著。** 最好的是池子 50 个（t = %s），其余都在 %s 以下。" % (
                    nm(va["池子 50 个"]["t"]), up1(sorted(v["t"] for v in va.values())[-2]))]
    if i == "X8":
        return ["**信号本身就是负的。** 零成本年化 %s（t = %s）。在流动性最高的 30 个币上，当天跌得多的第二天并不反弹。" % (pc(st["零成本"]["ret"]), nm(st["零成本"]["t"])),
                "**每天调仓的成本压垮一切。** 年换手 %.0f 倍，单边 0.10%% 一年约 %s；净年化 %s，累计 %s。" % (
                    ex["turnover"], pu(ex["turnover"] * S.COST, 0), pc(a["ret"]), pc(ex["total"])),
                "**降低换手也没用。** 改成每周调仓，年化 %s（t = %s）。" % (pc(va["每周调仓"]["ret"]), nm(va["每周调仓"]["t"])),
                "**每一年都亏。** 从 %s 到 %s。" % (pc(max(v["ret"] for v in yr.values())), pc(min(v["ret"] for v in yr.values())))]
    if i == "T1":
        return ["**没有超过 BTC 的部分。** 对 BTC 回归：贝塔 %s，超额年化 %s，t = %s。收益来自对大盘的敞口，不是趋势信号。" % (nm(a["beta"]), pc(a["alpha"]), nm(a["t_alpha"])),
                "**验证段亏损。** 年化 %s，累计 %s；同期一直持有 BTC 年化 %s。相对 BTC 的超额是每年 %s（t = %s）。" % (
                    pc(te["ret"]), pc(ex["total_test"]), pc(b(hold19, "test")["ret"]), pc(te["alpha"]), nm(te["t_alpha"])),
                "**对回看期敏感。** 只用 30 天时超额 t = %s，只用 90 天、180 天时超额为负（%s、%s）。" % (
                    nm(va["只用 30 天"]["t"]), pc(va["只用 90 天"]["ret"]), pc(va["只用 180 天"]["ret"])),
                "**夏普不如持有 BTC。** 这里 %s，同期一直持有 BTC 是 %s，BTC 100 日均线择时（2018 起）是 %s。" % (
                    nm(a["sharpe"]), nm(b(hold19)["sharpe"]), nm(b(ma18)["sharpe"]))]
    if i == "T2":
        return ["**样本外没有了。** 训练段年化 %s（t = %s），验证段 %s（t = %s）；2024、2025、2026 年分别是 %s、%s、%s。" % (
                    pc(tr["ret"]), nm(r["key"]["t_train"]), pc(te["ret"]), nm(r["key"]["t_test"]), y(2024), y(2025), y(2026)),
                "**对回看期敏感。** 只用 30 天 t = %s，只用 180 天为负（%s）。四个回看期平均以后，全区间 t = %s。" % (
                    nm(va["只用 30 天"]["t"]), pc(va["只用 180 天"]["ret"]), nm(a["t"])),
                "**对 BTC 回归后的超额不显著。** 超额年化 %s，t = %s。" % (pc(a["alpha"]), nm(a["t_alpha"]))]
    if i == "T3":
        return ["**没有超额。** 对 BTC 回归：贝塔 %s，超额年化 %s，t = %s。夏普 %s，一直持有是 %s。" % (
                    nm(a["beta"]), pc(a["alpha"]), nm(a["t_alpha"]), nm(a["sharpe"]), nm(b(hold18)["sharpe"])),
                "**只是把仓位缩小了。** 最大回撤从 %s 降到 %s，年化收益也从 %s 降到 %s，风险和收益同比例下降。" % (
                    pu(b(hold18)["mdd"]), pu(a["mdd"]), pc(b(hold18)["ret"]), pc(a["ret"])),
                "**怎么调都一样。** 目标波动率 30%% / 50%%、窗口 14 天 / 60 天，超额的 t 都在 %s 以下。" % up1(max(v["t"] for v in va.values()))]
    if i == "T5":
        return ["**成本吃掉一半。** 零成本年化 %s（夏普 %s，t = %s）；组合波动只有 %s，年换手 %.1f 倍，单边 0.10%% 一年约 %s，净夏普 %s；成本翻倍后夏普 %s。" % (
                    pc(st["零成本"]["ret"]), nm(st["零成本"]["sharpe"]), nm(st["零成本"]["t"]), pu(a["vol"]), ex["turnover"], pu(ex["turnover"] * S.COST, 2),
                    nm(a["sharpe"]), nm(st["成本翻倍"]["sharpe"])),
                "**快的回看期是负的。** 只用 21 天年化 %s；只用 126 天、252 天 t = %s、%s，也没到 2。" % (
                    pc(va["只用 21 天"]["ret"]), nm(va["只用 126 天"]["t"]), nm(va["只用 252 天"]["t"])),
                "**近年是亏的。** 验证段年化 %s；2023、2024、2025 年分别是 %s、%s、%s。" % (pc(te["ret"]), y(2023), y(2024), y(2025)),
                "**%.1f 年的 t 只有 %s。** 加上 BTC 和 ETH 并没有改变结论：去掉加密后 t = %s。" % (a["years"], nm(a["t"]), nm(va["去掉加密"]["t"]))]
    if i == "C1":
        return ["**收益衰减。** 超过国债利率的部分：2020 下半年 %s、2021 年 %s，2022 年起每年都是负的（%s、%s、%s、%s、%s）。" % (
                    y(2020), y(2021), y(2022), y(2023), y(2024), y(2025), y(2026)),
                "**成本。** 零成本年化 %s，两条腿的换仓成本一年约 %s；成本翻倍后全区间为负（%s）。" % (
                    pc(st["零成本"]["ret"]), pu(st["零成本"]["ret"] - a["ret"]), pc(st["成本翻倍"]["ret"])),
                "**挑币救不回来。** 选 3 个、5 个、10 个差别不大（%s、%s、%s）；门槛从 10%% 提到 20%% 是 %s，降到 0%% 是 %s。训练段每年 %s，验证段每年 %s。" % (
                    pc(va["选 3 个"]["ret"]), pc(a["ret"]), pc(va["选 10 个"]["ret"]), pc(va["门槛 20%"]["ret"]), pc(va["门槛 0%"]["ret"]), pc(tr["ret"]), pc(te["ret"])),
                "**回测还偏乐观。** 没有算基差变动、空头一侧被强平、交易所本身的风险。"]
    if i == "S1":
        return ["**不显著。** 全区间 t = %s，训练段年化 %s（t = %s）。" % (nm(a["t"]), pc(tr["ret"]), nm(r["key"]["t_train"])),
                "**山寨季的尾部风险。** 2021 年一年 %s，最大回撤 %s。" % (y(2021), pu(a["mdd"])),
                "**收益都来自 2024 年以后。** 训练段（到 2023 年底）合计是亏的，全区间的收益都来自 2024 年以后（年化 %s，t = %s）；3 个变体的 t 都在 %s 以下。" % (
                    pc(te["ret"]), nm(r["key"]["t_test"]), up1(max(v["t"] for v in va.values())))]
    raise KeyError(i)


def one_liner(i):
    r = E[i]
    a, tr, te, st = r["stats"]["all"], r["stats"]["train"], r["stats"]["test"], r["stress"]
    return {
        "X1": "零成本 t %s，扣单边 0.10%% 成本后只剩 %s，不显著。" % (nm(st["零成本"]["t"]), nm(a["t"])),
        "X2": "年化 %s，t %s；验证段 t %s，没有信号。" % (pc(a["ret"]), nm(a["t"]), nm(r["key"]["t_test"])),
        "X3": "方向相反：年化 %s，验证段 %s（t %s）。" % (pc(a["ret"]), pc(te["ret"]), nm(r["key"]["t_test"])),
        "X5": "年化 %s，t %s；晚一天执行就转负。" % (pc(a["ret"]), nm(a["t"])),
        "X8": "零成本年化 %s，加成本后 %s，回撤 %s。" % (pc(st["零成本"]["ret"]), pc(a["ret"]), pu(a["mdd"])),
        "T1": "夏普 %s，但相对 BTC 的超额 t 只有 %s，验证段亏损。" % (nm(a["sharpe"]), nm(a["t_alpha"])),
        "T2": "训练段 t %s，验证段 t %s；全区间 t %s。" % (nm(r["key"]["t_train"]), nm(r["key"]["t_test"]), nm(a["t"])),
        "T3": "回撤 %s 降到 %s，夏普 %s 对 %s，没有超额。" % (pu(b(hold18)["mdd"]), pu(a["mdd"]), nm(a["sharpe"]), nm(b(hold18)["sharpe"])),
        "T5": "零成本夏普 %s，扣成本后 %s；%.1f 年 t 只有 %s。" % (nm(st["零成本"]["sharpe"]), nm(a["sharpe"]), a["years"], nm(a["t"])),
        "C1": "超过国债利率的部分：训练段每年 %s，验证段 %s。" % (pc(tr["ret"]), pc(te["ret"])),
        "S1": "全区间 t %s；2021 年一年亏 %s，回撤 %s。" % (nm(a["t"]), pu(-r["yearly"]["2021"]["ret"]), pu(a["mdd"])),
    }[i]


LEFT = {
    "X1": "一周动量在零成本下是有的（t = {zc_t}），方向和文献一致。要让它在扣成本后接近显著，单边成本大约要压到这里假设的一半以下；能不能做到没有验证。",
    "X2": "没有。",
    "X3": "在 90 天这个周期上，大币更像反转而不是延续（验证段 t = {t_test}）。但这是事后看到的方向，反过来用需要新数据确认，不能当成结论。",
    "X5": "资金费率的信息集中在最近几天，30 天的平均把它抹平了。同一研究里更短回看期的版本没有被判为失败，仍在纸面观察，不属于本档案。",
    "X8": "没有。第 05 条里小时级的反转在零成本下是正的；到了日线、换成大币的横截面，连零成本都不成立。",
    "T1": "作为风控是有用的：最大回撤 {mdd}，等权持有同一批币是 {ew_mdd}。但同样的事，只对 BTC 一个币做均线择时（第 12 条）就能做到，分散到 30 个币没有多出东西。",
    "T2": "2020 到 2023 年是赚钱的（训练段夏普 {sr_train}）。只用 30 天回看的变体 t = {v30}，但这是事后挑出来的。",
    "T3": "可以当成降低回撤的旋钮，不能当成收益来源。",
    "T5": "慢的趋势（半年、一年）在零成本下是一个真实但很弱的溢价，而且危机年份为正（2008 年 {y2008}、2020 年 {y2020}、2022 年 {y2022}）。对交易成本只有这里十分之一的机构，它仍然成立；对按零售成本交易的个人，不成立。",
    "C1": "和第 10 条一样，可以当成“市场热度”的指标：资金费重新回到高位时才值得看。",
    "S1": "山寨币相对 BTC 的弱势在 2022 年以后确实存在（2022 到 2025 年每年为正），但一次山寨季就能亏掉几年的积累，而且统计上不显著。",
}

COMMON_DEFECTS = [
    "只用了币安一家的数据。",
    "这是把原文的思路搬到“流动性最高的 30 个大币”上的重写，不是对原文的逐位复现。原文在小币上、在更早年份里的结果，这里没有复核，也没有否定。",
    "没有模拟强平、保证金占用、极端行情下无法成交的情况。",
    "被下架的币按最后一个交易日的收盘价平仓；另做了“最后一天对多头再亏 30%”的压力测试。",
    "同一次研究一共事先登记了 14 个候选，t 的门槛因此定在 3.0。只看这一条时，不要用 2.0 的门槛去读它。",
]
EXTRA_DEFECTS = {
    "X1": ["盈亏用现货收盘价计算，没有用永续合约自己的价格；`verify.py` 里有换成合约价格的重算，结论不变。"],
    "T1": ["只做现货，没有考虑小币的买卖价差比 0.10% 更大的情况。"],
    "T3": [],
    "T5": ["用 ETF 作各个市场的代理。这些品种现在是否都能以单边 0.10% 的成本在永续合约上交易，没有逐一核实。",
           "ETF 日线来自 Yahoo，不随仓库分发，复现时要先下载；重新下载的数据可能有细微差别，所以这一条核对时容差放宽。",
           "数据源里有两处明显的错价（铜 ETF，2014-12-04 和 2015-02-02）做了手工修正，见 `macro.py` 里的 `BAD_TICKS`。",
           "BTC、ETH 在 2019 年 9 月以前没有资金费数据，持仓成本用无风险利率代替。"],
    "C1": ["不计基差变动的盈亏，也没有模拟空头一侧在暴涨时被强平。", "无风险利率用美国 13 周国债收益率。"],
}
for k in ("X2", "X3", "X5", "X8", "T2", "S1"):
    EXTRA_DEFECTS[k] = EXTRA_DEFECTS["X1"]
# 有两条的情况不一样（一条只有 BTC，一条不是币安的数据），通用的几句不适用
COMMON_BY = {
    "T3": ["只用了币安一家的数据。",
           "这是把原文的思路搬到 BTC 上的重写（不加杠杆），不是对原文的逐位复现。原文在股票因子上的结果，这里没有复核，也没有否定。",
           COMMON_DEFECTS[4]],
    "T5": ["这是按原文思路的重写，不是逐位复现：品种、年份和成本假设都和原文不同。原文在更多品种、更长年份、机构成本下的结果，这里没有复核，也没有否定。",
           "没有模拟强平、保证金占用、极端行情下无法成交的情况。",
           COMMON_DEFECTS[4]],
}


def numbers_table(i):
    r = E[i]
    a, te, ex = r["stats"]["all"], r["stats"]["test"], r["extras"]
    claim = {"X5": ("年化 43.4%", "—", "—", "0.74"), "T5": ("—", "—", "—", "1.17（毛，1985–2017）"), "C1": ("年化约 8%", "—", "—", "—")}.get(i, ("显著为正" if i in ("X1", "X2") else "—", "—", "—", "—"))
    rows = [("全区间收益", claim[0], "累计 %s，年化 %s（%s 到 %s）" % (pc(ex["total"]), pc(a["ret"]), r["start"], r["end"])),
            ("样本外收益", claim[1], "2024-01-01 以后：累计 %s，年化 %s，t = %s" % (pc(ex["total_test"]), pc(te["ret"]), nm(te["t"]))),
            ("最大回撤", claim[2], "%s（样本外 %s）" % (pu(a["mdd"]), pu(ex["mdd_test"]))),
            ("夏普", claim[3], "%s（t = %s）" % (nm(a["sharpe"]), nm(a["t"]))),
            ("交易次数", "—", "调仓 %d 次，年换手 %.1f 倍" % (ex["rebalances"], ex["turnover"])),
            ("胜率 / 盈亏比", "—", "按周：赚钱的周占 %s，平均赚 ÷ 平均亏 = %s" % (pu(ex["week_win"], 0), nm(ex["payoff"])))]
    if r["uses_alpha"]:
        rows.append(("相对 BTC 的超额", "显著为正" if i == "T3" else "—", "年化 %s，贝塔 %s，t = %s" % (pc(a["alpha"]), nm(a["beta"]), nm(a["t_alpha"]))))
    if i == "C1":
        rows[0] = (rows[0][0], rows[0][1], rows[0][2] + "；都是超过国债利率的部分")
    return "| 项目 | 原声称 | 复核结果 |\n|------|--------|----------|\n" + "\n".join("| %s | %s | %s |" % x for x in rows)


def left(i):
    r = E[i]
    a, yr = r["stats"]["all"], r["yearly"]
    g = lambda k: pc(yr[str(k)]["ret"]) if str(k) in yr else "—"
    return LEFT[i].format(zc_t=nm(r["stress"]["零成本"]["t"]), t_test=nm(r["key"]["t_test"]), mdd=pu(a["mdd"]), ew_mdd=pu(b(ew19)["mdd"]),
                          sr_train=nm(r["stats"]["train"]["sharpe"]), v30=nm(r["variants"].get("只用 30 天", {}).get("t")),
                          y2008=g(2008), y2020=g(2020), y2022=g(2022))


def entry_report(i):
    r = E[i]
    c = CLAIM[i]
    cmd = "py verify.py %s" % i
    pre = "py download_data.py --yahoo   # 这一条要用的 ETF 日线不随仓库分发，先下载一次\n" if i == "T5" else ""
    L = ["# %d · %s（%s）" % (r["no"], r["name"], i), "",
         "属于 [量化失败合集](https://github.com/runningshark/quant-failure-archive)。这一条来自同一次事先登记的研究，共用代码和数据，总览见 [FAILURE_REPORT.md](../FAILURE_REPORT.md)。", "",
         "## 一句话结论", "", one_liner(i), "",
         "## 原始声称", "",
         "- 作者 / 出处：" + c["src"],
         "- 声称的收益、回撤、样本外区间：" + c["ret"],
         "- 声称使用的数据与成本假设：" + c["data"], "",
         "## 复核方法", "",
         "- 被检验的规则：" + RULE[i],
         "- 数据来源与区间：" + ("ETF 复权日线（Yahoo），2005 年起，回测区间 %s 到 %s；BTC、ETH 的资金费率来自币安。" % (r["start"], r["end"]) if i == "T5" else
                          "币安 BTCUSDT 现货日线。回测区间 %s 到 %s。" % (r["start"], r["end"]) if i == "T3" else
                          "币安现货全部 USDT 交易对的日线，**包含已下架的币**（588 个可用品种里 194 个已下架）。回测区间 %s 到 %s。" % (r["start"], r["end"]) if i == "T1" else
                          "币安现货全部 USDT 交易对的日线，**包含已下架的币**（588 个可用品种里 194 个已下架）；币安 U 本位永续合约的资金费率（官方归档）。回测区间 %s 到 %s。" % (r["start"], r["end"])),
         "- 复现方式（逐位复现 / 重写 / 只做统计检验）：重写。规则、参数、通过标准在看到任何结果之前写进了[《事先登记.md》](../事先登记.md)，之后没有改过，也没有调参。",
         "- 成本假设（手续费、滑点、资金费、借贷利息）：单边 0.10%（手续费加滑点）" + ("；永续合约持仓计入每天的资金费（多头付、空头收）。" if r["kind"] in ("xs", "btcalts", "carry") or i == "T2" else
                                                         "；收益已扣无风险利率，BTC、ETH 扣资金费。" if i == "T5" else "；现货，不涉及资金费。") + "另做成本翻倍、晚一天执行" + ("" if i in ("T3", "T5", "C1") else "、下架惩罚") + "的压力测试。",
         "- 是否样本外：是。训练段到 2023-12-31，验证段从 2024-01-01 起；通过标准要求两段各自 t ≥ 2、全区间 t ≥ 3。", "",
         "## 实际数字", "", numbers_table(i), "",
         "## 失败原因", ""]
    L += ["%d. %s" % (k + 1, s) for k, s in enumerate(reasons(i))]
    miss = [k for k, v in r["checks"].items() if not v]
    L += ["", "按《事先登记.md》第 5 节，没有满足的标准：" + "；".join(miss) + "。", "",
          "## 剩下的东西", "", left(i), "",
          "## 复现命令", "", "```bash"] + CLONE + ["pip install pandas numpy", pre + cmd, "```", "",
          "输出里的“核对”一行会把这次算出来的数字和归档时的数字逐项比较。归档时的完整输出在 [results/%s.txt](../results/%s.txt)。" % (i, i), "",
          "## 已知缺陷 / 未验证部分", ""]
    L += ["- " + s for s in EXTRA_DEFECTS.get(i, []) + COMMON_BY.get(i, COMMON_DEFECTS)]
    L += ["", "不构成任何投资建议。", ""]
    return "\n".join(L)


CONCL = {"X1": "确认失败（零成本勉强，扣成本后不显著）", "X2": "确认失败（没有信号）", "X3": "确认失败（方向相反）", "X5": "确认失败（信号被平均掉）",
         "X8": "确认失败（零成本也亏）", "T1": "确认失败（对 BTC 没有超额）", "T2": "确认失败（样本外转负）", "T3": "指标无效（没有超额）",
         "T5": "确认失败（成本吃掉一半，仍不显著）", "C1": "收益衰减", "S1": "确认失败（不显著，山寨季巨亏）"}


def key_numbers(i):
    r = E[i]
    a, tr, te, ex, st, va, yr = r["stats"]["all"], r["stats"]["train"], r["stats"]["test"], r["extras"], r["stress"], r["variants"], r["yearly"]
    B = lambda s: "**" + s + "**"
    return {
        "X1": "零成本 t %s，扣成本后 t %s；年换手 %.0f 倍；成本翻倍 t %s" % (nm(st["零成本"]["t"]), B(nm(a["t"])), ex["turnover"], nm(st["成本翻倍"]["t"])),
        "X2": "年化 %s，t %s；样本外年化 %s（t %s）" % (pc(a["ret"]), B(nm(a["t"])), pc(te["ret"]), nm(te["t"])),
        "X3": "年化 %s，回撤 %s；样本外年化 %s（t %s）；5 个变体全负" % (B(pc(a["ret"])), B(pu(a["mdd"])), pc(te["ret"]), nm(te["t"])),
        "X5": "年化 %s，t %s；晚一天执行 %s；样本外累计 %s" % (pc(a["ret"]), B(nm(a["t"])), pc(st["晚一天执行"]["ret"]), pc(ex["total_test"])),
        "X8": "零成本年化 %s；年换手 %.0f 倍，净年化 %s，回撤 %s" % (B(pc(st["零成本"]["ret"])), ex["turnover"], B(pc(a["ret"])), pu(a["mdd"])),
        "T1": "夏普 %s，对 BTC 超额 t %s（贝塔 %s）；样本外累计 %s" % (nm(a["sharpe"]), B(nm(a["t_alpha"])), nm(a["beta"]), B(pc(ex["total_test"]))),
        "T2": "训练段 t %s → 样本外 t %s；2024–2026 年 %s / %s / %s" % (nm(r["key"]["t_train"]), B(nm(r["key"]["t_test"])), pc(yr["2024"]["ret"]), pc(yr["2025"]["ret"]), pc(yr["2026"]["ret"])),
        "T3": "夏普 %s vs 持有 %s；对 BTC 超额 t %s；回撤 %s vs %s" % (nm(a["sharpe"]), nm(b(hold18)["sharpe"]), B(nm(a["t_alpha"])), pu(a["mdd"]), pu(b(hold18)["mdd"])),
        "T5": "%.1f 年：零成本夏普 %s → 扣成本 %s（t %s）；成本翻倍 %s；2023–2025 连亏" % (a["years"], nm(st["零成本"]["sharpe"]), B(nm(a["sharpe"])), nm(a["t"]), nm(st["成本翻倍"]["sharpe"])),
        "C1": "超过国债利率：训练段每年 %s → 样本外每年 %s；2022 年起年年为负" % (pc(tr["ret"]), B(pc(te["ret"]))),
        "S1": "t %s；2021 年 %s，回撤 %s；训练段年化 %s" % (B(nm(a["t"])), B(pc(yr["2021"]["ret"])), pu(a["mdd"]), pc(tr["ret"])),
    }[i]


def overview_table(link_prefix=""):
    rows = ["| # | 编号 | 策略 | 结论 | 年化净收益 | 夏普 | t | 样本外 t | 最大回撤 | 档案 |", "|---|---|---|---|---|---|---|---|---|---|"]
    for s in specs.SPECS:
        i = s["id"]
        r = E[i]
        a = r["stats"]["all"]
        rows.append("| %d | %s | %s | %s | %s | %s | %s | %s | %s | [详情](%s%s) |" % (
            r["no"], i, r["name"], CONCL[i], pc(a["ret"]), nm(a["sharpe"]), nm(r["key"]["t_all"]), nm(r["key"]["t_test"]), pu(a["mdd"]), link_prefix, FILE[i]))
    return "\n".join(rows)


def failure_report():
    n = len(specs.SPECS)
    L = ["# 事先登记的 14 个因子候选：失败的 %d 个" % n, "",
         "属于 [量化失败合集](https://github.com/runningshark/quant-failure-archive) 的第 %d 到 %d 条。每一条单独的档案在 [reports/](reports/)，这份是总览。" % (specs.SPECS[0]["no"], specs.SPECS[-1]["no"]), "",
         "## 一句话结论", "",
         "事先登记 14 个候选、门槛 t ≥ 3：没有一个通过，%d 个失败（本档案）。" % n, "",
         "## 原始声称", "",
         "- 作者 / 出处：这不是某一个人的策略。它是把量化机构和学术界公开的几类做法（横截面动量、套息、趋势跟随、波动率管理、多空配对）搬到币安上的一次集中检验。每一条各自的出处见 reports/ 里对应的档案。",
         "- 声称的收益、回撤、样本外区间：各条不同。共同点是原文都报告了显著的正收益，多数不扣或少扣交易成本。",
         "- 声称使用的数据与成本假设：各条不同，多数用全市场的币（含大量小币）或机构水平的成本。", "",
         "## 复核方法", "",
         "- 数据来源与区间：币安现货全部 USDT 交易对的日线，2017-08 到 %s，**包含已下架的币**（788 个交易对，去掉稳定币、杠杆代币、包装资产、代币化股票后 588 个可用，其中 194 个已下架）；币安 U 本位永续合约的资金费率（官方归档，含已下架合约）；跨资产那一条用 ETF 的复权日线。" % specs.DATA_END.date(),
         "- 复现方式（逐位复现 / 重写 / 只做统计检验）：重写。测之前把 14 个候选的规则、参数和通过标准写进[《事先登记.md》](事先登记.md)，之后不改、不调参。",
         "- 选币池：每个调仓日，在当天有价格、已有至少 90 天历史的币里，按**此前** 30 天的日成交额中位数取前 30。需要做空的策略还要求当天有永续合约。这样避免只用今天还活着的币，也避免用事后才知道的成交量选币。",
         "- 成本假设（手续费、滑点、资金费、借贷利息）：单边 0.10%；永续合约持仓计入每天的资金费。压力测试：成本翻倍、晚一天执行、被下架的币最后一天对多头再亏 30%。",
         "- 是否样本外：是。训练段到 2023-12-31，验证段从 2024-01-01 起。",
         "- 门槛：同时测 14 个，碰巧有一个 t 超过 2 的概率接近一半，所以要求全区间 t ≥ 3.0（Bonferroni 校正后是 2.91），并且训练段、验证段各自 t ≥ 2.0，对市场回归后的超额 t ≥ 2.0，邻近变体全部为正，压力测试后仍为正。",
         "- 自检（`selftest.py`）：回测引擎和手算对得上；把数据截短后重算，截止日之前的仓位完全不变；300 个随机信号在零成本下 t 值平均 0.06、标准差 1.05。", "",
         "## 实际数字", "",
         "t 一栏：T1、T3 有市场敞口，用的是相对 BTC 的超额的 t；其余是净收益的 t。C1 的收益是超过美国短期国债利率的部分。", "",
         overview_table(), "",
         "对照组（同一套引擎，同样的成本）：", "",
         "| 对照 | 年化 | 夏普 | 最大回撤 | 2024 年以后的夏普 |", "|---|---|---|---|---|"]
    for k in BENCH:
        L.append("| %s | %s | %s | %s | %s |" % (k, pc(b(k)["ret"]), nm(b(k)["sharpe"]), pu(b(k)["mdd"]), nm(b(k, "test")["sharpe"])))
    x1, t5, c1 = E["X1"], E.get("T5"), E["C1"]
    L += ["",
          "## 失败原因", "",
          "按重要性排序的三个共同原因。每一条各自的原因见它的档案。", "",
          "1. **成本。** 好几个信号在零成本下是成立的，扣掉零售水平的成本就没了一半：动量 7 天的 t 从 %s 掉到 %s；跨资产趋势的夏普从 %s 掉到 %s；资金费篮子的年化从 %s 掉到 %s。见 `verify.py` 输出里每条的“压力测试”一行。" % (
              nm(x1["stress"]["零成本"]["t"]), nm(x1["stats"]["all"]["t"]), nm(t5["stress"]["零成本"]["sharpe"]), nm(t5["stats"]["all"]["sharpe"]),
              pc(c1["stress"]["零成本"]["ret"]), pc(c1["stats"]["all"]["ret"])),
          "2. **样本外衰减。** 趋势类训练段还可以，2024 年以后转负（T1 验证段累计 %s，T2 验证段 t = %s）；资金费篮子 2022 年起每年都跑不赢国债。" % (
              pc(E["T1"]["extras"]["total_test"]), nm(E["T2"]["key"]["t_test"])),
          "3. **收益来自大盘或一段行情，不是信号。** T1 相对 BTC 的超额 t 只有 %s；T3 的超额 t 也是 %s；S1 的收益全部来自 2024 年以后，2021 年一年亏 %s。" % (
              nm(E["T1"]["stats"]["all"]["t_alpha"]), nm(E["T3"]["stats"]["all"]["t_alpha"]), pu(-E["S1"]["yearly"]["2021"]["ret"])), "",
          "## 剩下的东西", "",
          "- 对照组里最简单的 BTC 100 日均线择时（本合集第 12 条）仍然是方向性规则里最好的：夏普 %s，最大回撤 %s，一直持有是 %s 和 %s。把趋势分散到 30 个币没有多出东西。" % (
              nm(b(ma18)["sharpe"]), pu(b(ma18)["mdd"]), nm(b(hold18)["sharpe"]), pu(b(hold18)["mdd"])),
          "- 一周动量和慢的跨资产趋势在零成本下是真实但很弱的信号，对成本足够低的人可能还成立。",
          "- 14 个候选里另外 3 个没有被判为失败，属于“待观察”（值得纸面跟踪，但没有被证明），不在失败档案里，这里不放它们的结果。", "",
          "## 复现命令", "",
          "```bash"] + CLONE + ["pip install pandas numpy",
          "py download_data.py --yahoo   # 只有第 22 条（跨资产趋势）需要：ETF 日线不随仓库分发",
          "py verify.py                  # 11 条全部，约 1 分钟；末尾一行是 “11 / 11 条和归档数字一致”",
          "py verify.py X1               # 只跑一条",
          "py selftest.py                # 引擎自检，约 2 分钟", "```", "",
          "## 已知缺陷 / 未验证部分", ""]
    L += ["- " + s for s in COMMON_DEFECTS[:4]]
    L += ["- 盈亏用现货收盘价计算；`verify.py` 对每个用永续合约的条目都另用合约自己的价格重算了一遍，结论不变（合约日线覆盖约 95% 的“币·天”）。",
          "- 很多币的资金费率同时停在默认值时，排序会出现并列，这时按代码字母顺序取，是任意的。",
          "- 跨资产那一条用 ETF 作代理，数据来自 Yahoo，不随仓库分发；有两处明显错价做了手工修正。",
          "- 设计候选时已经读过相关文献，知道哪些方向别人报告过有效，这本身也是一种偏差。", "", "不构成任何投资建议。", ""]
    return "\n".join(L)


def readme():
    L = ["# " + REPO, "",
         "**事先登记的 14 个因子候选里失败的 %d 个**的档案，属于 [量化失败合集 quant-failure-archive](https://github.com/runningshark/quant-failure-archive) 的第 %d 到 %d 条。" % (
             len(specs.SPECS), specs.SPECS[0]["no"], specs.SPECS[-1]["no"]), "",
         "这 %d 条来自同一次研究，共用一套代码和数据，所以放在一起。拆开会丢掉“同时测了 14 个、门槛因此是 t ≥ 3”这个前提。" % len(specs.SPECS), "",
         overview_table(), "",
         "- 总览和共同的方法：[FAILURE_REPORT.md](FAILURE_REPORT.md)",
         "- 每一条的档案（按合集模板）：[reports/](reports/)",
         "- 测之前写下的规则和通过标准：[事先登记.md](事先登记.md)",
         "- 复现：`py verify.py`（需要 pandas、numpy），结果写到 `results/output.txt`；单条用 `py verify.py X1`",
         "- 代码：`study.py`（读数据、选币池、信号、回测引擎、统计）、`macro.py`（跨资产趋势）、`specs.py`（11 个条目的定义和判定）、`selftest.py`（引擎自检）、`tools/make_reports.py`（把归档数字填进各份档案）",
         "- 数据：`data/`，币安现货日线（含已下架的币）、永续合约资金费率和日线的快照，截至 %s。跨资产趋势要用的 ETF 日线不随仓库分发，运行 `py download_data.py --yahoo` 下载" % specs.DATA_END.date(),
         "- 归档时的原始输出：`results/`", "",
         "```bash"] + CLONE + ["pip install pandas numpy", "py download_data.py --yahoo   # 只有第 22 条需要", "py verify.py", "```", "",
         "不构成任何投资建议。", ""]
    return "\n".join(L)


TITLE = {"X1": "周线 · 横截面动量（7 天）", "X2": "周线 · 横截面动量（28 天）", "X3": "周线 · 横截面动量（90 天）", "X5": "周线 · 资金费 30 天多空",
         "X8": "日线 · 横截面一日反转", "T1": "周线 · 30 币分散趋势（现货）", "T2": "周线 · 30 币分散趋势（永续多空）", "T3": "周线 · 波动率管理的 BTC",
         "T5": "周线 · 跨资产趋势（25 个市场）", "C1": "周线 · 资金费篮子（挑费率最高的币）", "S1": "周线 · 多 BTC 空山寨"}


def main_section(base):
    """总仓库 README 里 14–24 这一节。"""
    x1, t1, t2, t3, t5, c1 = E["X1"], E["T1"], E["T2"], E["T3"], E["T5"], E["C1"]
    first, last = specs.SPECS[0]["no"], specs.SPECS[-1]["no"]
    L = ["### %d–%d · 事先登记的 14 个因子候选（%d 个失败）" % (first, last, len(specs.SPECS)), "",
         "把量化机构和学术界公开的几类做法（横截面动量、套息、趋势跟随、波动率管理、多空配对）搬到币安上集中测了一遍。和前面的条目不同的地方：", "",
         "- **事先登记。** 测之前把 14 个候选的规则、参数和通过标准写死（[事先登记.md](%s事先登记.md)），之后不改、不调参。" % base,
         "- **不用幸存者。** 数据包含已下架的币（588 个品种里 194 个已下架）；每个调仓日只用当时的成交额取前 30。",
         "- **门槛是 t ≥ 3。** 同时测 14 个，碰巧有一个 t 超过 2 的概率接近一半。",
         "- 成本单边 0.10%，永续合约持仓计入资金费；训练段到 2023 年底，验证段从 2024 年起。", "",
         "结果：**没有一个通过，%d 个失败。** 这 %d 条共用一套代码和数据，所以放在同一个文件夹里，没有各建一个仓库；拆开会丢掉“同时测了 14 个”这个前提。总览见 [FAILURE_REPORT.md](%sFAILURE_REPORT.md)。" % (
             len(specs.SPECS), len(specs.SPECS), base), "",
         "三个共同的死法：", "",
         "- **成本。** 动量 7 天零成本 t **%s**，扣成本后 **%s**；跨资产趋势夏普 **%s → %s**；资金费篮子年化 **%s → %s**。" % (
             nm(x1["stress"]["零成本"]["t"]), nm(x1["stats"]["all"]["t"]), nm(t5["stress"]["零成本"]["sharpe"]), nm(t5["stats"]["all"]["sharpe"]),
             pc(c1["stress"]["零成本"]["ret"]), pc(c1["stats"]["all"]["ret"])),
         "- **样本外衰减。** 30 币多空趋势训练段 t %s，2024 年以后 **%s**；资金费篮子 2022 年起每年都跑不赢国债。" % (nm(t2["key"]["t_train"]), nm(t2["key"]["t_test"])),
         "- **收益来自大盘，不是信号。** 30 币趋势（现货）和波动率管理的 BTC，相对 BTC 的超额 t 都只有 **%s**。" % nm(t1["stats"]["all"]["t_alpha"]), "",
         "各条一句话：", ""]
    for s_ in specs.SPECS:
        i = s_["id"]
        L.append("- **%d · %s**：%s [档案](%s%s)" % (E[i]["no"], E[i]["name"], one_liner(i), base, FILE[i]))
    L += ["",
          "剩下的线索：对照组里最简单的 BTC 100 日均线择时（第 12 条）夏普 **%s**、回撤 %s，仍然是方向性规则里最好的，把趋势分散到 30 个币没有多出东西；一周动量和慢的跨资产趋势在零成本下是真实但很弱的信号。14 个候选里另外 3 个没有被判为失败，属于“待观察”，不在这里。" % (
              nm(b(ma18)["sharpe"]), pu(b(ma18)["mdd"])), "",
          "```bash"] + CLONE + ["pip install pandas numpy", "py download_data.py --yahoo   # 只有第 22 条需要：ETF 日线不随仓库分发",
                                "py verify.py                  # 末尾一行：11 / 11 条和归档数字一致", "py verify.py X1               # 只跑一条", "```", ""]
    return "\n".join(L)


def main():
    root = S.HERE
    os.makedirs(os.path.join(root, "reports"), exist_ok=True)
    for i in SLUG:
        open(os.path.join(root, FILE[i]), "w", encoding="utf-8").write(entry_report(i))
    open(os.path.join(root, "FAILURE_REPORT.md"), "w", encoding="utf-8").write(failure_report())
    open(os.path.join(root, "README.md"), "w", encoding="utf-8").write(readme())
    entry = dict(study="事先登记的 14 个因子候选", data_end=str(specs.DATA_END.date()), cost_per_side=S.COST, split=str(S.SPLIT.date()), threshold_t=3.0,
                 registered=14, failed=len(specs.SPECS),
                 entries=[dict(no=s["no"], id=s["id"], name=s["name"], verdict=E[s["id"]]["verdict"], conclusion=CONCL[s["id"]], report=FILE[s["id"]],
                               spec={k: v for k, v in s.items() if k not in ("no", "id", "name")}) for s in specs.SPECS])
    json.dump(entry, open(os.path.join(root, "entry.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # 给总仓库 README 用的表格行和小节（只在指定 MAIN_ROWS / MAIN_SECTION 时写出）
    base = "" if STANDALONE else "entries/%s/" % REPO
    link = (lambda i: "[%s](https://github.com/runningshark/%s/blob/master/%s)" % (REPO, REPO, FILE[i])) if STANDALONE else (lambda i: "[entries/%s](%s%s)" % (REPO, base, FILE[i]))
    rows = ["| %d | %s | %s | %s | %s |" % (E[s["id"]]["no"], TITLE[s["id"]], bold(CONCL[s["id"]]), key_numbers(s["id"]), link(s["id"])) for s in specs.SPECS]
    if os.environ.get("MAIN_ROWS"):
        open(os.environ["MAIN_ROWS"], "w", encoding="utf-8").write("\n".join(rows) + "\n")
    if os.environ.get("MAIN_SECTION"):
        open(os.environ["MAIN_SECTION"], "w", encoding="utf-8").write(main_section(base))
    print("写好了 11 份 reports、FAILURE_REPORT.md、README.md、entry.json")


if __name__ == "__main__":
    main()
