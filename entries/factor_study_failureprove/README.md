# factor_study_failureprove

**事先登记的 14 个因子候选里失败的 11 个**的档案，属于 [量化失败合集 quant-failure-archive](https://github.com/runningshark/quant-failure-archive) 的第 14 到 24 条。

这 11 条来自同一次研究，共用一套代码和数据，所以放在一起。拆开会丢掉“同时测了 14 个、门槛因此是 t ≥ 3”这个前提。

| # | 编号 | 策略 | 结论 | 年化净收益 | 夏普 | t | 样本外 t | 最大回撤 | 档案 |
|---|---|---|---|---|---|---|---|---|---|
| 14 | X1 | 横截面动量 7 天 | 确认失败（零成本勉强，扣成本后不显著） | +17.8% | 0.69 | 1.75 | 1.52 | −37.8% | [详情](reports/14_X1_xs_momentum_7d.md) |
| 15 | X2 | 横截面动量 28 天 | 确认失败（没有信号） | +9.0% | 0.34 | 0.85 | 0.28 | −35.6% | [详情](reports/15_X2_xs_momentum_28d.md) |
| 16 | X3 | 横截面动量 90 天 | 确认失败（方向相反） | −14.0% | −0.52 | −1.25 | −2.19 | −76.9% | [详情](reports/16_X3_xs_momentum_90d.md) |
| 17 | X5 | 资金费 30 天多空（多低空高） | 确认失败（信号被平均掉） | +4.0% | 0.18 | 0.44 | 0.06 | −44.5% | [详情](reports/17_X5_funding_30d.md) |
| 18 | X8 | 横截面一日反转（每天调仓） | 确认失败（零成本也亏） | −54.5% | −2.16 | −6.17 | −3.48 | −97.8% | [详情](reports/18_X8_xs_reversal_1d.md) |
| 19 | T1 | 30 币分散趋势·现货只做多 | 确认失败（对 BTC 没有超额） | +13.8% | 0.53 | 0.20 | −1.04 | −38.6% | [详情](reports/19_T1_trend_spot.md) |
| 20 | T2 | 30 币分散趋势·永续多空 | 确认失败（样本外转负） | +12.3% | 0.50 | 1.33 | −0.32 | −35.7% | [详情](reports/20_T2_trend_perp.md) |
| 21 | T3 | 波动率管理的 BTC 持有 | 指标无效（没有超额） | +24.9% | 0.57 | 0.20 | −0.29 | −64.9% | [详情](reports/21_T3_btc_vol_managed.md) |
| 22 | T5 | 跨资产趋势·多空 | 确认失败（成本吃掉一半，仍不显著） | +0.9% | 0.25 | 1.21 | −0.30 | −10.1% | [详情](reports/22_T5_cross_asset_trend.md) |
| 23 | C1 | 资金费篮子（现货多 + 永续空） | 收益衰减 | +3.1% | 1.84 | 2.01 | −3.73 | −17.1% | [详情](reports/23_C1_funding_basket.md) |
| 24 | S1 | 做多 BTC、做空山寨篮子 | 确认失败（不显著，山寨季巨亏） | +7.5% | 0.29 | 0.76 | 1.51 | −56.1% | [详情](reports/24_S1_btc_vs_alts.md) |

- 总览和共同的方法：[FAILURE_REPORT.md](FAILURE_REPORT.md)
- 每一条的档案（按合集模板）：[reports/](reports/)
- 测之前写下的规则和通过标准：[事先登记.md](事先登记.md)
- 复现：`py verify.py`（需要 pandas、numpy），结果写到 `results/output.txt`；单条用 `py verify.py X1`
- 代码：`study.py`（读数据、选币池、信号、回测引擎、统计）、`macro.py`（跨资产趋势）、`specs.py`（11 个条目的定义和判定）、`selftest.py`（引擎自检）、`tools/make_reports.py`（把归档数字填进各份档案）
- 数据：`data/`，币安现货日线（含已下架的币）、永续合约资金费率和日线的快照，截至 2026-11-25。跨资产趋势要用的 ETF 日线不随仓库分发，运行 `py download_data.py --yahoo` 下载
- 归档时的原始输出：`results/`

```bash
git clone https://github.com/runningshark/quant-failure-archive
cd quant-failure-archive/entries/factor_study_failureprove
pip install pandas numpy
py download_data.py --yahoo   # 只有第 22 条需要
py verify.py
```

不构成任何投资建议。
