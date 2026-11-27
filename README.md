# 量化失败合集 / Quant Failure Archive

做过、跑过、最后没赚到钱的策略，在这里留一份可复现的档案。

不写"经验总结"，只写能重跑的数字：原始声称是什么、用什么数据复核、扣完成本和样本外之后还剩多少。每一条都是**独立仓库**，代码、数据、验证脚本齐全，clone 下来就能自己跑一遍看我有没有骗人。（14–24、25–29、31–34、35–37、38–40、41–45、46–48、49–53 各来自一次事先登记的研究，每次研究共用一个仓库。）

---

## 条目

| # | 策略 | 结论 | 关键数字 | 仓库 |
|---|------|------|----------|------|
| 01 | ETH 择时 · 遗传规划（GP） | **确认失败**（外部复核，不是原作者自评） | 样本外 **−5.3%**，最大回撤 **−58.4%** | [gp_eth_failureprove](https://github.com/runningshark/gp_eth_failureprove) |
| 02 | ETH 择时 · 1 小时（趋势 + 动量） | **确认失败**（且「参数寻优」是假的） | 全区间 **−85.5%**，回撤 **−90.5%**，612 笔；零成本仍 **−50.7%** | [eth_1h_failureprove](https://github.com/runningshark/eth_1h_failureprove) |
| 03 | 1 小时 · 超卖接多（带止损） | **确认失败**（零成本也亏） | 样本外 BTC **−51%** / ETH **−83%**；零成本 BTC 全期 **−64%** | [h1_dip_stop_failureprove](https://github.com/runningshark/h1_dip_stop_failureprove) |
| 04 | 1 小时 · 超卖接多（不止损） | **确认失败**（高胜率陷阱） | 胜率 89%–94%，样本外 BTC **−31%** / ETH **−56%**，单笔扛单 **−12.7%** | [h1_dip_nostop_failureprove](https://github.com/runningshark/h1_dip_nostop_failureprove) |
| 05 | 1 小时 · 反转（跌了就买） | **确认失败**（被手续费吃光） | 样本外 BTC **−65%** / ETH **−62%**；零成本 **+213%**，约 3,500 笔换手 | [h1_reversal_failureprove](https://github.com/runningshark/h1_reversal_failureprove) |
| 06 | 日线 · 均值回归（连跌接多） | **不值得交易**（没亏，但赚得太少） | 7 年 BTC **+1.8%** / ETH **+5.5%**；样本外六币 −1.9%～+2.4%，同期持有 BTC +39%；81 组参数夏普全部 < 0.5 | [d1_meanrev_failureprove](https://github.com/runningshark/d1_meanrev_failureprove) |
| 07 | 1 小时 · 突破（48 小时，海龟式） | **确认失败**（样本外衰减，做空版亏损） | 只做多样本外夏普中位 **0.27**（训练段约 1.0），BTC +11% vs 持有 +42%；允许做空后全期 BTC **−27%**、XRP **−86%** | [h1_breakout_failureprove](https://github.com/runningshark/h1_breakout_failureprove) |
| 08 | 1 小时 · 动量（168 小时） | **确认失败**（手续费吃掉全部优势） | 只做多样本外 BTC **−4%**（持有 +48%），六币三亏；最近一年六币全亏；零成本样本外全正，扣成本后一半变负；允许做空 BNB **−65%** | [h1_momentum_failureprove](https://github.com/runningshark/h1_momentum_failureprove) |
| 09 | 日线 · 突破 + 订单流过滤 | **指标无效**（加上后没有变好） | 订单流和未来 1/7/30 日收益相关系数 ≈ 0；6 币合计样本外 **+84R → +72R**（不加过滤 → 加过滤）；10 组参数训练段无一组超过不加过滤 | [d1_flow_filter_failureprove](https://github.com/runningshark/d1_flow_filter_failureprove) |
| 10 | 日线 · 资金费套息（现货多 + 永续空） | **收益衰减**（不亏钱，但已不值得占用资金） | 6 币全期都为正（+20%～+54%），但年化 2024 年前 5.6% → 2024 年后 2.1% → 2025 年后 **0.4%**；105 组参数最好一组 2025 年后也只有 1.1% | [d1_funding_carry_failureprove](https://github.com/runningshark/d1_funding_carry_failureprove) |
| 11 | 日线 · 布林带收缩突破（squeeze） | **指标无效**（收缩条件越严越差） | 收缩分位 10% → 25% → 60% → 不要求收缩：样本外 +23R → +76R → +105R → +101R；默认版两段都输给普通 20 日突破（+159R vs +223R / +76R vs +84R），BTC 样本外亏损 | [d1_squeeze_failureprove](https://github.com/runningshark/d1_squeeze_failureprove) |
| 12 | 日线 · 均线择时（100 日，满仓） | **基准·待改进**（不是失败） | 2024 年后 6 币 5 个跑赢持有（ETH +43% vs −27%），夏普 0.56，和突破策略相当；但满仓无止损，平均最大回撤 **−51%**（最深 −69%） | [d1_ma_baseline_failureprove](https://github.com/runningshark/d1_ma_baseline_failureprove) |
| 13 | 4H · 维纳斯通道引擎（Vegas 隧道 + 主区 + MACD + 斐位） | **确认失败**（前视偏差 + 参数过拟合） | 看板原声称 **+87.4%**；前视 **+19.0%** vs 实时 **−1.0%**；参数样本内最优 **+76.3% → 样本外 −4.1%**，样本外 36 组全负 | [vegas_channel_failureprove](https://github.com/runningshark/vegas_channel_failureprove) |
| 14 | 周线 · 横截面动量（7 天） | **确认失败**（零成本勉强，扣成本后不显著） | 零成本 t 2.48，扣成本后 t **1.75**；年换手 73 倍；成本翻倍 t 1.03 | [factor_study_failureprove · X1](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/14_X1_xs_momentum_7d.md) |
| 15 | 周线 · 横截面动量（28 天） | **确认失败**（没有信号） | 年化 +9.0%，t **0.85**；样本外年化 +3.6%（t 0.28） | [factor_study_failureprove · X2](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/15_X2_xs_momentum_28d.md) |
| 16 | 周线 · 横截面动量（90 天） | **确认失败**（方向相反） | 年化 **−14.0%**，回撤 **−76.9%**；样本外年化 −28.2%（t −2.19）；5 个变体全负 | [factor_study_failureprove · X3](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/16_X3_xs_momentum_90d.md) |
| 17 | 周线 · 资金费 30 天多空 | **确认失败**（信号被平均掉） | 年化 +4.0%，t **0.44**；晚一天执行 −0.6%；样本外累计 −3.7% | [factor_study_failureprove · X5](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/17_X5_funding_30d.md) |
| 18 | 日线 · 横截面一日反转 | **确认失败**（零成本也亏） | 零成本年化 **−5.0%**；年换手 495 倍，净年化 **−54.5%**，回撤 −97.8% | [factor_study_failureprove · X8](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/18_X8_xs_reversal_1d.md) |
| 19 | 周线 · 30 币分散趋势（现货） | **确认失败**（对 BTC 没有超额） | 夏普 0.53，对 BTC 超额 t **0.20**（贝塔 0.30）；样本外累计 **−13.5%** | [factor_study_failureprove · T1](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/19_T1_trend_spot.md) |
| 20 | 周线 · 30 币分散趋势（永续多空） | **确认失败**（样本外转负） | 训练段 t 2.01 → 样本外 t **−0.32**；2024–2026 年 +0.0% / −3.7% / −15.1% | [factor_study_failureprove · T2](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/20_T2_trend_perp.md) |
| 21 | 周线 · 波动率管理的 BTC | **指标无效**（没有超额） | 夏普 0.57 vs 持有 0.59；对 BTC 超额 t **0.20**；回撤 −64.9% vs −81.2% | [factor_study_failureprove · T3](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/21_T3_btc_vol_managed.md) |
| 22 | 周线 · 跨资产趋势（25 个市场） | **确认失败**（成本吃掉一半，仍不显著） | 19.9 年：零成本夏普 0.47 → 扣成本 **0.25**（t 1.21）；成本翻倍 0.04；2023–2025 连亏 | [factor_study_failureprove · T5](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/22_T5_cross_asset_trend.md) |
| 23 | 周线 · 资金费篮子（挑费率最高的币） | **收益衰减** | 超过国债利率：训练段每年 +8.7% → 样本外每年 **−3.5%**；2022 年起年年为负 | [factor_study_failureprove · C1](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/23_C1_funding_basket.md) |
| 24 | 周线 · 多 BTC 空山寨 | **确认失败**（不显著，山寨季巨亏） | t **0.76**；2021 年 **−51.4%**，回撤 −56.1%；训练段年化 −2.7% | [factor_study_failureprove · S1](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/24_S1_btc_vs_alts.md) |
| 25 | 周线 · 做空新上线的币（第 7–90 天） | **确认失败**（新币会跌，但做空不赚钱） | 新币第 7–90 天 76% 下跌（中位数 −39.0%），做空却年化 **−8.5%**、回撤 **−81.3%**；做空一年要付约 11.6% 资金费 | [factor_study2_failureprove · N1](https://github.com/runningshark/factor_study2_failureprove/blob/master/reports/25_N1_new_listing_short_7_90.md) |
| 26 | 周线 · 做空新上线的币（第 91–365 天） | **确认失败**（牛市里被逼空） | 年化 **−8.1%**，t −0.82；2021 年 **−44.1%**；5 个变体全负 | [factor_study2_failureprove · N2](https://github.com/runningshark/factor_study2_failureprove/blob/master/reports/26_N2_new_listing_short_91_365.md) |
| 27 | 周线 · 散户多空比（反向） | **确认失败**（样本外反转） | 训练段 t 2.10 → 验证段 **−12.0%**（t −1.18）；全区间 t **0.62**；收益主要是资金费 | [factor_study2_failureprove · P1](https://github.com/runningshark/factor_study2_failureprove/blob/master/reports/27_P1_retail_ls_ratio.md) |
| 28 | 周线 · 大户持仓多空比（跟随） | **确认失败**（跟着大户反而亏） | 年化 **−8.5%**，t **−1.49**；两段都亏，4 个变体全负 | [factor_study2_failureprove · P2](https://github.com/runningshark/factor_study2_failureprove/blob/master/reports/28_P2_top_trader_ratio.md) |
| 29 | 周线 · 持仓量增速（反向） | **确认失败**（方向相反） | 年化 **−20.5%**，t **−3.12**（方向相反）；反过来扣成本后 t 1.23，验证段 +0.3% | [factor_study2_failureprove · P3](https://github.com/runningshark/factor_study2_failureprove/blob/master/reports/29_P3_oi_growth.md) |
| 30 | 日线 · 技术指标规则大全（467 条，30 币等权） | **确认失败**（最好的一条和运气分不出来） | 最大 t 2.85，校正“试了 467 条”后 p **0.16**；成本翻倍 p 0.34；训练段最好的规则验证段 t **0.48**；KD 12 条全负 | [d1_indicator_zoo_failureprove](https://github.com/runningshark/d1_indicator_zoo_failureprove) |
| 31 | 周 · 每周卖出 BTC 平值跨式（不对冲） | **确认失败**（权利金刚好抵掉赔付） | 年化 **+1.9%**，t 0.12，回撤 **−77.3%**；每周收权利金 5.94%、赔 5.83%；最差一周亏 38.8% | [w1_short_straddle_failureprove · V1](https://github.com/runningshark/w1_short_straddle_failureprove/blob/master/reports/31_V1_btc_short_straddle.md) |
| 32 | 周 · 每周卖出 ETH 平值跨式（不对冲） | **确认失败**（权利金抵不掉赔付） | 年化 **−3.8%**，t −0.24，回撤 **−86.9%**；每周收 7.26%、赔 7.27% | [w1_short_straddle_failureprove · V2](https://github.com/runningshark/w1_short_straddle_failureprove/blob/master/reports/32_V2_eth_short_straddle.md) |
| 33 | 周 · 每周卖出 BTC 平值跨式（每天对冲） | **确认失败**（对冲后仍不显著） | 年化 +6.8%，t **0.98**；对冲成本每年 5.5%；权利金打 95 折 → **−8.5%** | [w1_short_straddle_failureprove · V3](https://github.com/runningshark/w1_short_straddle_failureprove/blob/master/reports/33_V3_btc_short_straddle_hedged.md) |
| 34 | 周 · 每周卖出 ETH 平值跨式（每天对冲） | **确认失败**（对冲后仍为负） | 年化 **−5.0%**，t −0.59；训练段、验证段都为负 | [w1_short_straddle_failureprove · V4](https://github.com/runningshark/w1_short_straddle_failureprove/blob/master/reports/34_V4_eth_short_straddle_hedged.md) |
| 35 | 日线 · 距离法配对交易 | **确认失败**（零成本也不赚） | 年化 **−2.7%**，t −0.78；零成本也是 −1.0%；4 个变体全负 | [pairs_trading_failureprove · S1](https://github.com/runningshark/pairs_trading_failureprove/blob/master/reports/35_S1_distance_pairs.md) |
| 36 | 日线 · 协整配对交易 | **确认失败**（方向相反） | 年化 **−16.7%**，t **−3.24**（方向相反），每年都亏；反过来扣成本后 t 2.44，没到门槛 | [pairs_trading_failureprove · S2](https://github.com/runningshark/pairs_trading_failureprove/blob/master/reports/36_S2_cointegration_pairs.md) |
| 37 | 日线 · ETH/BTC 比值回归 | **确认失败**（没有信号） | 年化 +0.7%，t **0.09**；验证段 −1.4%；六年多只开仓 36 次 | [pairs_trading_failureprove · S3](https://github.com/runningshark/pairs_trading_failureprove/blob/master/reports/37_S3_ethbtc_ratio.md) |
| 38 | 1 小时 · CME 缺口回补 | **确认失败**（高胜率陷阱） | 赚钱的占 72%，年化 **−19.5%**，回撤 −88.0%；回补的平均赚 2.4%，没回补的平均亏 7.9%；零成本也是 −14.0% | [h1_calendar_failureprove · G1](https://github.com/runningshark/h1_calendar_failureprove/blob/master/reports/38_G1_cme_gap.md) |
| 39 | 1 小时 · 议息前 24 小时做多 | **确认失败**（只有 2020 年有效） | 年化 +4.8%，t **1.41**；验证段 −2.6%；去掉 2020 年只剩 +0.3% | [h1_calendar_failureprove · F1](https://github.com/runningshark/h1_calendar_failureprove/blob/master/reports/39_F1_pre_fomc.md) |
| 40 | 1 小时 · 每天 21–23 点（UTC）做多 | **确认失败**（被手续费吃光） | 年化 **−47.4%**（成本一年 73%）；零成本 +25.6%（t 4.35），但每笔只有 +0.07% | [h1_calendar_failureprove · T1](https://github.com/runningshark/h1_calendar_failureprove/blob/master/reports/40_T1_hours_21_23.md) |
| 41 | 日线 · 解锁前 14 天做空 | **确认失败**（不显著，挑日子没有用） | 年化 +4.3%，t **1.15**；解锁前下跌的占 63%（不是 90%），相对大盘平均只跑输 1.5%；随机日期的 t 平均 0.96 | [token_events_failureprove · U1](https://github.com/runningshark/token_events_failureprove/blob/master/reports/41_U1_short_before_unlock.md) |
| 42 | 日线 · 解锁后 14 天做空 | **确认失败**（前段是亏的） | 年化 +3.4%，t **0.95**；前段 −3.3%；随机日期的 t 平均 1.29，比真实日期高 | [token_events_failureprove · U2](https://github.com/runningshark/token_events_failureprove/blob/master/reports/42_U2_short_after_unlock.md) |
| 43 | 周线 · 稀释多空（空临近解锁的，多已经放完的） | **确认失败**（不显著） | 年化 +9.3%，t **1.20**，回撤 −29.2%；多头换成普通篮子变成 −2.2% | [token_events_failureprove · U3](https://github.com/runningshark/token_events_failureprove/blob/master/reports/43_U3_dilution_long_short.md) |
| 44 | 日线 · 下架公告后做空 | **确认失败**（样本不足，放宽后亏损） | 合格事件只有 **17** 个；公告当天中位数 −21.3%（吃不到），之后平均 +21.1%（逼空）；门槛放宽后年化 −10.2% | [token_events_failureprove · D1](https://github.com/runningshark/token_events_failureprove/blob/master/reports/44_D1_short_after_delist_notice.md) |
| 45 | 日线 · 观察标签后做空 | **确认失败**（消息当天就消化完了） | 年化 +3.1%，t **1.02**；公告当天中位数 −12.0%（吃不到），之后相对大盘平均 +0.4% | [token_events_failureprove · M1](https://github.com/runningshark/token_events_failureprove/blob/master/reports/45_M1_short_after_monitoring_tag.md) |
| 46 | 周线 · 非流动性溢价 | **确认失败**（方向相反） | 年化 **−18.6%**，t −1.84（方向相反）；验证段 t −2.83；4 个变体全负 | [volume_liquidity_failureprove · L1](https://github.com/runningshark/volume_liquidity_failureprove/blob/master/reports/46_L1_illiquidity_premium.md) |
| 47 | 周线 · 成交量冲击 | **确认失败**（没有信号） | 年化 +6.1%，t **0.64**；零成本 t 1.15；变体有正有负 | [volume_liquidity_failureprove · L2](https://github.com/runningshark/volume_liquidity_failureprove/blob/master/reports/47_L2_volume_shock.md) |
| 48 | 周线 · 量价配合 | **指标无效**（加了成交量条件反而更差） | 年化 +10.7%，t **0.74**；不加成交量条件是 +27.3%（t 1.91），缩量的那一半是 +20.1%（t 1.70） | [volume_liquidity_failureprove · L3](https://github.com/runningshark/volume_liquidity_failureprove/blob/master/reports/48_L3_volume_confirmed_momentum.md) |
| 49 | 日线 · MVRV 估值择时 | **确认失败**（不显著，14 年只离场 3 次） | 择时超额 +23.5%，t **2.19**，平移检验 p 0.064；14 年只离场 3 次，钱比一直持有少（2,568 倍对 16,253 倍）；原文的 3.7 事后重算 t 3.14，也没过 3.3 | [onchain_timing_failureprove · O1](https://github.com/runningshark/onchain_timing_failureprove/blob/master/reports/49_O1_mvrv_valuation.md) |
| 50 | 日线 · 交易所余额下降就持有 | **确认失败**（没有信号） | 择时超额 +5.7%，t **0.61**；验证段 −0.7%；余额上升的日子 BTC 反而涨得多（+109.5% 对 +77.3%） | [onchain_timing_failureprove · O2](https://github.com/runningshark/onchain_timing_failureprove/blob/master/reports/50_O2_exchange_balance.md) |
| 51 | 日线 · 活跃地址上升就持有 | **确认失败**（2020 年以后失效） | 择时超额 +10.6%，t **1.24**；训练段 t 1.72，验证段 **0.0%**；2024 年 BTC 涨 121%，它只有 15% 的时间在场 | [onchain_timing_failureprove · O3](https://github.com/runningshark/onchain_timing_failureprove/blob/master/reports/51_O3_active_addresses.md) |
| 52 | 日线 · 哈希率带 | **确认失败**（没有信号） | 择时超额 +2.4%，t **0.37**；验证段 −1.3%；变体有正有负 | [onchain_timing_failureprove · O4](https://github.com/runningshark/onchain_timing_failureprove/blob/master/reports/52_O4_hash_ribbons.md) |
| 53 | 日线 · Puell 倍数择时 | **确认失败**（顶部线再也没碰到，2020 年以后没有交易） | 择时超额 +20.2%，t **1.88**；顶部线 4 在 2018-01-06 之后再没碰到，2020 年以后 **0 次交易** | [onchain_timing_failureprove · O5](https://github.com/runningshark/onchain_timing_failureprove/blob/master/reports/53_O5_puell_multiple.md) |

### 01 · ETH 择时（遗传规划）

原策略声称样本外能稳定盈利。逐位复现后确认失败：**样本外 −5.3%**，最大回撤 −58.4%，同期买入持有并不是这个数量级。

复核里顺带量化了三件事，比"策略挂了"更有用：

- **趋势跟踪是真的，但很弱。** 16 个币种的日线面板，等权组合年化 **+17.0%**，最大回撤 **30.1%**，t 值 **1.63** —— 统计上站不住"显著"，只能算一个弱的正期望。
- **4h + 杠杆的分支是杠杆 beta，不是 alpha。** 收益好看的回撤全在 **73%–86%**，本质是放大方向暴露。
- **横盘突破从没工作过。** 默认参数跑出来 **0 笔交易**（报告里没提）；参数修好之后是 +10.3% / 夏普 0.45 / 回撤 68.1%，仍然不值得上线。

复现：

```bash
git clone https://github.com/runningshark/gp_eth_failureprove
cd gp_eth_failureprove
py main.py tests          # 27/27
py verify/01_gp_holdout.py
```

### 02 · ETH 择时（1 小时）

报告写着「1h 参数寻优后 −85.4%」。复核发现这句话本身是空的：

- **训练区间 64 组参数，0 组是正的**（中位 −79.6%，最好 −41.5%）。优化器只保留正收益 + 正夏普，返回空列表后代码静默回退 `DEFAULT_PARAMS`，报告把这个默认值写成了「最佳参数」。
- **不是手续费的问题。** 零成本仍然 **−50.7%**，平均每笔 −0.050%；多头腿 −33.9%、空头腿 −25.3%，两个方向都在亏。10 bps 只是把 −51% 放大成 −85%。
- **训练区间就已经 −72.7%**，报告只披露了「样本外 −46.4%」。

同一份信号在 1 天上是 +2331%（买入持有 +1858%），样本外 +283% vs 买入持有 −32.9%，216 组参数样本外全正——但那段样本外是 ETH 单边下跌，趋势策略顺风，单品种单区间，只能算「值得再验」，不能算 edge。

```bash
git clone https://github.com/runningshark/eth_1h_failureprove
cd eth_1h_failureprove
py verify/01_reproduce.py        # 8/8：−85.5% / −90.5% / 612 笔
py verify/02_grid_and_costs.py   # 1h 参数面 0/64、成本阶梯
```

### 03 · 1 小时超卖接多（带止损）

急跌到 24 小时低点、RSI < 35 就接多，+1% 止盈、−2% 止损。

- **胜率 62%–65%，但盈亏比 1:2 要 66.7% 以上才打平**，所以零成本也是亏的。
- 六个币 × 九组参数，扣成本后**全部为负**。
- 2026-11-21 暴跌时连续三个小时接刀、连续止损，纸面账户一周 **−12.9%**。

```bash
git clone https://github.com/runningshark/h1_dip_stop_failureprove
cd h1_dip_stop_failureprove
py verify.py
```

### 04 · 1 小时超卖接多（不止损）

和 03 一样，只是不止损、亏了就扛。

- **胜率接近 90%**，带单页面一片绿，但少数大亏吃掉全部小赚：2026-11-13 买入的 BTC 扛到 11-20，这一笔 **−12.7%**。
- 六个币四个亏。BNB 样本外 +30%，但同一套规则在其他五个币都亏——对品种和参数敏感，判为过拟合。

```bash
git clone https://github.com/runningshark/h1_dip_nostop_failureprove
cd h1_dip_nostop_failureprove
py verify.py
```

### 05 · 1 小时反转

收盘价低于 24 小时前就持多，否则空仓。

- **零成本 BTC 全期 +213%、ETH +182%**——小时级短期反转确实有一点统计倾向。
- 但七年多换手约 **3,500 次**，单边 0.05% 成本后六个币**全部亏损**（BTC −91%）。
- 回看窗口 6 到 336 小时**全部为负**，不是参数没调好。

```bash
git clone https://github.com/runningshark/h1_reversal_failureprove
cd h1_reversal_failureprove
py verify.py
```

### 06 · 日线均值回归（连跌接多）

上升趋势（收盘在 200 日均线上方）里，连跌 3 天后次日开盘买入；回到 5 日均线上方或持满 5 天卖出；3 倍 ATR 止损，每笔风险 1%。

- **胜率 64%–76%，回撤只有 1%–4%，但几乎不赚钱**：平均每笔约 +0.25R，7 年合计约 +5R；BTC 全期 +1.8%，同期一直持有 +470%。
- 一年只出手 8～10 次、持仓时间占 6%–9%，仓位只有账户的几个百分点，钱大部分时间闲着。
- **唯一有用的是趋势过滤**：81 组参数里，去掉 200 / 100 日均线过滤的 27 组**全部为负**；连跌天数、出场均线、持有天数怎么调都差不多，最好的夏普只有 0.27。
- 不算"亏损失败"，算"性价比失败"：在系统里占一个位置，却几乎不产生收益。

```bash
git clone https://github.com/runningshark/d1_meanrev_failureprove
cd d1_meanrev_failureprove
py verify.py
```

### 07 · 1 小时突破（48 小时）

小时收盘创 48 小时新高、且在 200 小时均线上方就买，跌破 24 小时新低就卖；可选对称做空。

- **训练段夏普约 1.0，2024 年后中位数只剩 0.27**：BTC +11%（同期持有 +42%），SOL −23%、BNB −9%。全期的大收益主要来自 2019–2021 年牛市。
- **做空部分六个币全部亏损**：200 小时均线只有 8 天，牛市回调也被当成下跌；创新低时跌势往往已近尾声，随后的轧空打掉离场线；交易次数和手续费翻倍。打开做空后 BTC 全期 −27%、XRP −86%，回撤 −84% 到 −99%。
- 手续费吃掉约一半：零成本 BTC 样本外 +29%，扣成本后 +11%。
- 剩下的线索：窗口拉长到 7～14 天明显更好（但那已是日线突破）；做空只在日线下跌趋势里做，空单从全亏变成接近不亏——这一条是事后挑出来的，需要新数据再确认。

```bash
git clone https://github.com/runningshark/h1_breakout_failureprove
cd h1_breakout_failureprove
py verify.py
```

### 08 · 1 小时动量（168 小时）

当前小时收盘高于 168 小时（7 天）前就持有，低于就平仓；可选做空。每小时判断一次。

- **"手续费决定生死"的标准案例**：样本外每年约 150 次换仓，不扣成本六个币全是正的（BTC +47%、ETH +84%），扣单边 0.05% 后 BTC −4%、BNB −9%、DOGE −8%。平均夏普从训练段约 1.05 掉到 0.26。
- 最近一年六个币全亏（−10% 到 −51%），只是比买入持有亏得少。
- 做空版样本外六个币五个亏（BTC −49%、BNB −65%）：小时级下跌常被很快拉回，交易次数和手续费翻倍。
- 回看越短越差（24 小时 BTC −65%、ETH −84%）。336 小时样本外很好，但是孤立尖峰：312 小时做空版六币全亏，属于幸运参数。360～720 小时较稳，但那已经等于日线动量。

```bash
git clone https://github.com/runningshark/h1_momentum_failureprove
cd h1_momentum_failureprove
py verify.py
```

### 09 · 日线突破 + 订单流过滤

在日线趋势突破（200 日均线上方、创 20 日新高买入）上加一个条件：最近 7 天主动买入多于主动卖出才做多。这一条**不是亏钱**，而是"加了一个听起来有道理的指标，结果没有用"。

- 指标本身没有预测力：订单流 z 值和未来 1 / 7 / 30 日收益的相关系数几乎都在 ±0.05 以内，训练段和样本外常常符号相反；BNB 2024 年后甚至反向。
- 对照不加过滤的同一策略：6 币合计 2024 年前 +223R → +218R，2024 年后 +84R → +72R。SOL、BNB 变差，ETH、DOGE 略好，合计略差。
- 过滤器主要是在"推迟进场"：被拦下的突破日占 11%–35%，但交易笔数几乎不变，真趋势里订单流过一两天也会转正，只是进场价更差。
- 10 组参数里没有一组在训练段超过不加过滤的版本；累计天数越长越差（30 天版本样本外只剩 +27R～+36R）。
- 教训：给现成策略加指标，要和"不加"的版本逐笔对照，而不是只看加了以后赚不赚钱。

```bash
git clone https://github.com/runningshark/d1_flow_filter_failureprove
cd d1_flow_filter_failureprove
py verify.py
```

### 10 · 资金费套息（现货多 + 永续空）

买入现货、做空等量永续合约，价格风险对冲掉，只收多头付给空头的资金费；近 7 天平均资金费年化 > 10% 建仓，< 0% 平仓。这一条**没有亏钱**，收进来是因为它的收益已经没了。

- 回测里 6 个币全期都是正的、从未亏损——门槛机制让它在资金费低时自动停下（2022 年 SOL 资金费 −38%，它没进场）。
- 但收益几乎全来自 2020–2021 年：资金费本身 2021 年 30%–50%，2024 年 12%–14%，2025–2026 年只剩 0–5%，BNB、SOL 多年为负。按账户算（一半现货、一半保证金）只吃到一半：2025 年以来 6 币平均年化 0.4%，2026 年 BTC 只有 5% 的时间在持仓。
- 调参上限很低：最稳的改进是"早进晚出"（建仓 5%、平仓 −5%），前十几组结果挤在一起、不是过拟合，但 2025 年后也只有 1.1%。平仓门槛高于建仓门槛的组合会反复开平仓，每年被手续费吃掉 15%–24%。
- 回测没算强平、基差和交易所风险，真实结果只会更差。可以当"市场狂热度"指标用：资金费年化重新上到 10% 以上时才值得开。

```bash
git clone https://github.com/runningshark/d1_funding_carry_failureprove
cd d1_funding_carry_failureprove
py verify.py
```

### 11 · 布林带收缩突破（squeeze）

布林带宽度处在过去 120 天最窄的 25% 时，收盘站上上轨就做多，跌回中轨离场，止损 2 倍 ATR。卖点是"先蓄力再突破，假信号更少"。

- **关键检验**：只改"收缩分位"一个参数。条件越严越差：最窄 10% 时 6 币合计 2024 年后只有 +23R，默认 25% 是 +76R，放宽到 60% 是 +105R，**完全不要求收缩**是 +101R——起作用的是"站上上轨"这个突破，不是收缩。
- 和普通 20 日突破相比，默认版本两段都更差：2024 年前 +159R vs +223R，2024 年后 +76R vs +84R；BTC 2024 年后 16 笔胜率 25%、−1.1R。样本外合计的一半多来自 XRP 一两段行情。
- 原因：低波动之后确实更可能出现大波动，但向上、向下差不多；方向已经由"站上上轨"给出了，收缩条件只是在减少交易次数，错过趋势启动。
- 教训和 09 一样：给突破加一个"听起来有道理"的过滤条件，要和不加的版本对照，并且把这个条件从严到松扫一遍。

```bash
git clone https://github.com/runningshark/d1_squeeze_failureprove
cd d1_squeeze_failureprove
py verify.py
```

### 12 · 均线择时（基准·待改进）

收盘在 100 日均线之上满仓持有，之下空仓。这是"及格线"：任何更复杂的策略都应该先赢过它。**它不是失败**，收进来是因为它还不能直接拿真钱用，需要改进。

- 信号不差：2024 年后 6 个币里 5 个跑赢一直持有（BTC +67% vs +39%，ETH +43% vs −27%，DOGE +70% vs −40%），平均夏普 0.56，和精心设计的 20 日突破（约 0.50）相当；平均最大回撤从持有的 −70% 降到 −51%。
- 问题在仓位：满仓、无止损，跌破均线时往往已经回撤 20%–40%；SOL 2024 年后 −69%。震荡市贴着均线来回打脸（XRP 2024 年前 54 笔、−79%）。牛市跑输持有是这类规则的固有代价。
- 改进探测：均线 20–150 日差别不大（50 日两段都最好）；打开做空回撤更深（−63%）；加 200 日方向过滤几乎没变化；改成 2 倍 ATR 止损 + 每笔 1% 风险，回撤降到 −11% 但收益也几乎没了。**方向是按波动率定仓位、多条均线投票**，介于满仓和 1% 风险之间。

```bash
git clone https://github.com/runningshark/d1_ma_baseline_failureprove
cd d1_ma_baseline_failureprove
py verify.py
```

### 13 · 维纳斯通道引擎

Vegas 隧道 EMA144/169 + EMA12 过滤 + 主区 EMA576/676 + MACD + 斐波那契打分定仓位，执行层后改用 S1 日线 EMA20/60 主区作开关。

- **+87.4% 是前视偏差**：用「当天日线最终收盘」判断主区，08:00 的 4H bar 偷看到 23:59 的收盘。同一窗口前视 **+19.0%**，当天进行中（看板口径）**−1.0%**，昨日已收盘 −2.5%。
- **参数调不出 edge**：36 组网格样本内最优 **+76.3%** 到样本外 **−4.1%**；样本外 36 组全负，最好也只有 −0.9%，样本内/外收益相关系数 0.507。
- **不是某个指标没用**：消融里去掉主区 / 隧道 / 过滤 / MACD / 斐位任一项都更差（去龙虾 −15.4% → −18.1%～−22.8%），失败来自整套信号在该窗口没有 edge；旧 4H 主区作开关（−15.7%）明显差于 S1 日线开关（−1.0%）。
- **5% 龙虾撑场**：去龙虾短窗口 −1.0%，含龙虾 +3.8%；项目看板同口径 +1.2% → +8.8%。去掉个别币就基本不赚钱。
- 剩下的线索：S1 日线 EMA20/60 作为「该不该空仓」的风控开关确实有效（回撤 −9.3% vs 旧主区 −22.7%、买入持有 −38.1%），可以拆出来单独当风控条件用，但不能当收益引擎。

```bash
git clone https://github.com/runningshark/vegas_channel_failureprove
cd vegas_channel_failureprove
py verify.py
```

### 14–24 · 同一次事先登记的研究（共用一个仓库）

14 到 24 这 11 条来自同一次研究：把量化机构和学术界公开的几类做法（横截面动量、套息、趋势跟随、波动率管理、多空配对）搬到币安上，测之前把 14 个候选的规则、参数和通过标准写死（[事先登记.md](https://github.com/runningshark/factor_study_failureprove/blob/master/事先登记.md)），之后不改、不调参。14 个里**没有一个通过，11 个失败**，下面逐条列出；另外 3 个没有被判为失败，属于“待观察”，不在这里。

- **不用幸存者。** 数据包含已下架的币（588 个品种里 194 个已下架）；每个调仓日只用当时的成交额取前 30。成本单边 0.10%，永续合约持仓计入资金费；训练段到 2023 年底，验证段从 2024 年起。
- **门槛是 t ≥ 3，不是 2。** 同时测 14 个，碰巧有一个 t 超过 2 的概率接近一半。下面每一条的 t 都按这个门槛读。
- **共用一个仓库。** 这 11 条共用一套代码和数据，拆开会丢掉“同时测了 14 个”这个前提，所以放在 [factor_study_failureprove](https://github.com/runningshark/factor_study_failureprove) 一个仓库里，每条用自己的编号单独复现（需要 pandas、numpy）。总览和三个共同的死法（成本、样本外衰减、收益来自大盘而不是信号）见 [FAILURE_REPORT.md](https://github.com/runningshark/factor_study_failureprove/blob/master/FAILURE_REPORT.md)。

### 14 · 横截面动量（7 天）

每周日收盘，在成交额最高的 30 个有永续合约的币里，做多过去 7 天涨得最多的 10 个、做空涨得最少的 10 个，等权，持有一周。（[档案](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/14_X1_xs_momentum_7d.md)）

- **成本。** 零成本年化 +25.1%（t = 2.48）；年换手 73 倍，单边 0.10% 一年吃掉约 7.3%，净 t 只剩 1.75；成本翻倍后 t = 1.03。
- **信号衰减得快。** 晚一天执行，年化从 +17.8% 掉到 +11.8%。
- **邻近变体不稳。** 池子 20 个 t = 0.89、按波动率倒数加权 t = 0.90、每天调仓 t = 1.18，只有“每边 6 个”接近 2（1.95）。
- **两段都不显著，分年很不均匀。** 训练段 t = 1.11，验证段 t = 1.52；2020 下半年 +58.5%，2021–2023 三年分别是 +5.5%、−8.2%、+4.1%。
- 剩下的线索：一周动量在零成本下是有的（t = 2.48），方向和文献一致。要让它在扣成本后接近显著，单边成本大约要压到这里假设的一半以下；能不能做到没有验证。

```bash
git clone https://github.com/runningshark/factor_study_failureprove
cd factor_study_failureprove
py verify.py X1
```

### 15 · 横截面动量（28 天）

和 14 一样，排序换成过去 28 天的涨幅。（[档案](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/15_X2_xs_momentum_28d.md)）

- **没有信号。** 全区间 t = 0.85，零成本也只有 1.25。
- **验证段几乎为零。** 年化 +3.6%（t = 0.28），累计 +1.7%，期间最大回撤 −32.7%。
- **变体里没有一个 t 到 2。** 从 0.50 到 1.58。2021、2022、2024、2026 四年为负（−13.4%、−5.2%、−3.0%、−22.0%）。

```bash
git clone https://github.com/runningshark/factor_study_failureprove
cd factor_study_failureprove
py verify.py X2
```

### 16 · 横截面动量（90 天）

和 14 一样，排序换成过去 90 天的涨幅，也就是“强者恒强”轮动的依据。（[档案](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/16_X3_xs_momentum_90d.md)）

- **方向和声称相反。** 做多过去 90 天涨得多的、做空涨得少的：年化 −14.0%，累计 −67.8%，最大回撤 −76.9%。
- **怎么改都是负的。** 5 个邻近变体、3 项压力测试全部为负，零成本也是 −11.1%。
- **越近越差。** 训练段年化 −2.2%（t = −0.13），验证段 −28.2%（t = −2.19）；2021 年以后只有 2023 年勉强为正（+1.0%）。
- **不是成本问题。** 年换手只有 29 倍。
- 剩下的线索：在 90 天这个周期上，大币更像反转而不是延续（验证段 t = −2.19）。但这是事后看到的方向，反过来用需要新数据确认，不能当成结论。

```bash
git clone https://github.com/runningshark/factor_study_failureprove
cd factor_study_failureprove
py verify.py X3
```

### 17 · 资金费 30 天多空

每周日收盘，在成交额最高的 30 个有永续合约的币里，做多过去 30 天平均资金费率最低的 10 个、做空最高的 10 个，等权，持有一周。（[档案](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/17_X5_funding_30d.md)）

- **没有信号。** 年化 +4.0%，t = 0.44；零成本 t = 0.75。
- **晚一天执行就转负。** 年化 −0.6%。
- **验证段没有收益。** 年化 +0.8%（t = 0.06），累计 −3.7%，期间最大回撤 −41.7%；2022、2023、2025、2026 四年为负。
- **变体也不显著。** 最好的是池子 50 个（t = 1.80），其余都在 1.4 以下。
- 剩下的线索：资金费率的信息集中在最近几天，30 天的平均把它抹平了。同一研究里更短回看期的版本没有被判为失败，仍在纸面观察，不属于本档案。

```bash
git clone https://github.com/runningshark/factor_study_failureprove
cd factor_study_failureprove
py verify.py X5
```

### 18 · 横截面一日反转

每天收盘，在成交额最高的 30 个有永续合约的币里，做多当天跌得最多的 10 个、做空涨得最多的 10 个，等权，持有一天。（[档案](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/18_X8_xs_reversal_1d.md)）

- **信号本身就是负的。** 零成本年化 −5.0%（t = −0.56）。在流动性最高的 30 个币上，当天跌得多的第二天并不反弹。
- **每天调仓的成本压垮一切。** 年换手 495 倍，单边 0.10% 一年约 49%；净年化 −54.5%，累计 −97.5%。
- **降低换手也没用。** 改成每周调仓，年化 −4.9%（t = −0.49）。
- **每一年都亏。** 从 −30.7% 到 −64.8%。
- 和第 05 条对照：小时级的反转在零成本下是正的；到了日线、换成大币的横截面，连零成本都不成立。

```bash
git clone https://github.com/runningshark/factor_study_failureprove
cd factor_study_failureprove
py verify.py X8
```

### 19 · 30 币分散趋势（现货）

每周日收盘，对成交额最高的 30 个币（现货）各看 30 / 90 / 180 / 365 天四个回看期：现价高于其中几个回看期之前的价格，趋势分就是几分之几；仓位按趋势分和波动率定，只做多，不加杠杆。（[档案](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/19_T1_trend_spot.md)）

- **没有超过 BTC 的部分。** 对 BTC 回归：贝塔 0.30，超额年化 +1.4%，t = 0.20。收益来自对大盘的敞口，不是趋势信号。
- **验证段亏损。** 年化 −1.9%，累计 −13.5%；同期一直持有 BTC 年化 +23.3%。相对 BTC 的超额是每年 −10.5%（t = −1.04）。
- **对回看期敏感。** 只用 30 天时超额 t = 1.63，只用 90 天、180 天时超额为负（−2.5%、−7.2%）。
- **夏普不如持有 BTC。** 这里 0.53，同期一直持有 BTC 是 0.70，BTC 100 日均线择时（2018 起）是 0.92。
- 剩下的线索：作为风控是有用的，最大回撤 −38.6%，而等权持有同一批币是 −96.3%。但同样的事，只对 BTC 一个币做均线择时（第 12 条）就能做到，分散到 30 个币没有多出东西。

```bash
git clone https://github.com/runningshark/factor_study_failureprove
cd factor_study_failureprove
py verify.py T1
```

### 20 · 30 币分散趋势（永续多空）

和 19 一样，换成永续合约：四个回看期按涨跌方向投票，趋势向下就做空，计入资金费。（[档案](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/20_T2_trend_perp.md)）

- **样本外没有了。** 训练段年化 +26.0%（t = 2.01），验证段 −4.1%（t = −0.32）；2024、2025、2026 年分别是 +0.0%、−3.7%、−15.1%。
- **对回看期敏感。** 只用 30 天 t = 2.52，只用 180 天为负（−3.5%）。四个回看期平均以后，全区间 t = 1.33。
- **对 BTC 回归后的超额不显著。** 超额年化 +10.5%，t = 1.09。
- 剩下的线索：2020 到 2023 年是赚钱的（训练段夏普 1.02）。只用 30 天回看的变体 t = 2.52，但这是事后挑出来的。

```bash
git clone https://github.com/runningshark/factor_study_failureprove
cd factor_study_failureprove
py verify.py T2
```

### 21 · 波动率管理的 BTC

BTC 现货仓位 = min(1, 40% ÷ 过去 30 天的年化波动率)，每周日收盘调一次，不加杠杆。检验的是“按波动率管理仓位，相对一直持有有超额”。（[档案](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/21_T3_btc_vol_managed.md)）

- **没有超额。** 对 BTC 回归：贝塔 0.64，超额年化 +1.1%，t = 0.20。夏普 0.57，一直持有是 0.59。
- **只是把仓位缩小了。** 最大回撤从 −81.2% 降到 −64.9%，年化收益也从 +37.7% 降到 +24.9%，风险和收益同比例下降。
- **怎么调都一样。** 目标波动率 30% / 50%、窗口 14 天 / 60 天，超额的 t 都在 0.3 以下。
- 剩下的线索：可以当成降低回撤的旋钮，不能当成收益来源。

```bash
git clone https://github.com/runningshark/factor_study_failureprove
cd factor_study_failureprove
py verify.py T3
```

### 22 · 跨资产趋势（25 个市场）

25 个市场（股指、贵金属、能源、农产品、外汇，加上 BTC、ETH，用 ETF 日线作代理），每周按 21 / 63 / 126 / 252 个交易日四个回看期的涨跌方向定多空、按波动率定仓位，也就是管理期货基金最经典的做法。（[档案](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/22_T5_cross_asset_trend.md)）

- **成本吃掉一半。** 零成本年化 +1.7%（夏普 0.47，t = 2.26）；组合波动只有 3.6%，年换手 7.8 倍，单边 0.10% 一年约 0.78%，净夏普 0.25；成本翻倍后夏普 0.04。
- **快的回看期是负的。** 只用 21 天年化 −0.4%；只用 126 天、252 天 t = 1.45、1.73，也没到 2。
- **近年是亏的。** 验证段年化 −0.4%；2023、2024、2025 年分别是 −1.7%、−2.1%、−0.8%。
- **19.9 年的 t 只有 1.21。** 加上 BTC 和 ETH 并没有改变结论：去掉加密后 t = 0.87。
- 剩下的线索：慢的趋势（半年、一年）在零成本下是一个真实但很弱的溢价，而且危机年份为正（2008 年 +7.2%、2020 年 +3.7%、2022 年 +2.6%）。对交易成本只有这里十分之一的机构，它仍然成立；对按零售成本交易的个人，不成立。

```bash
git clone https://github.com/runningshark/factor_study_failureprove
cd factor_study_failureprove
py download_data.py --yahoo   # ETF 日线不随仓库分发，先下载一次
py verify.py T5
```

### 23 · 资金费篮子（挑费率最高的币）

每周日收盘，在成交额最高的 30 个有永续合约的币里，挑过去 7 天平均资金费率最高的 5 个（年化超过 10% 才持有），买现货、做空等量永续，只收资金费。检验的是“每周挑费率最高的币”能不能把第 10 条里衰减掉的收益找回来。（[档案](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/23_C1_funding_basket.md)）

- **收益衰减。** 超过国债利率的部分：2020 下半年 +10.6%、2021 年 +32.9%，2022 年起每年都是负的（−4.5%、−3.6%、−0.7%、−4.3%、−5.1%）。
- **成本。** 零成本年化 +8.4%，两条腿的换仓成本一年约 5.3%；成本翻倍后全区间为负（−2.1%）。
- **挑币救不回来。** 选 3 个、5 个、10 个差别不大（+3.0%、+3.1%、+3.6%）；门槛从 10% 提到 20% 是 +4.0%，降到 0% 是 +0.6%。训练段每年 +8.7%，验证段每年 −3.5%。
- **回测还偏乐观。** 没有算基差变动、空头一侧被强平、交易所本身的风险。
- 剩下的线索：和第 10 条一样，可以当成“市场热度”的指标，资金费重新回到高位时才值得看。

```bash
git clone https://github.com/runningshark/factor_study_failureprove
cd factor_study_failureprove
py verify.py C1
```

### 24 · 多 BTC 空山寨

每周日收盘，BTC 永续多单占资金的 50%，成交额前 30 里其余 29 个币等权做空，合计也占 50%。检验的是“山寨币长期跑输比特币”。（[档案](https://github.com/runningshark/factor_study_failureprove/blob/master/reports/24_S1_btc_vs_alts.md)）

- **不显著。** 全区间 t = 0.76，训练段年化 −2.7%（t = −0.19）。
- **山寨季的尾部风险。** 2021 年一年 −51.4%，最大回撤 −56.1%。
- **收益都来自 2024 年以后。** 训练段（到 2023 年底）合计是亏的，全区间的收益都来自 2024 年以后（年化 +19.9%，t = 1.51）；3 个变体的 t 都在 0.8 以下。
- 剩下的线索：山寨币相对 BTC 的弱势在 2022 年以后确实存在（2022 到 2025 年每年为正），但一次山寨季就能亏掉几年的积累，而且统计上不显著。

```bash
git clone https://github.com/runningshark/factor_study_failureprove
cd factor_study_failureprove
py verify.py S1
```

### 25–29 · 第二轮事先登记的研究（共用一个仓库）

14–24 的失败集中在成本、样本外衰减、收益来自大盘三种，所以第二轮只挑换手低、说得出是谁在付钱、多空对冲的做法：做空新上线的币，以及三个持仓拥挤度指标。测之前同样把规则、参数和通过标准写死（[事先登记_第二轮.md](https://github.com/runningshark/factor_study2_failureprove/blob/master/事先登记_第二轮.md)，并记下文件的 SHA-256）。**5 个全部失败**，没有一个进入“待观察”。

- **门槛随累计个数提高到 t ≥ 3.1。** 两轮累计 19 个候选。下面每一条的 t 都按这个门槛读。
- 数据是币安全部 U 本位永续（含已下架的）的日线、成交额、资金费，加上官方归档的持仓量和多空比；成本单边 0.10%，计入资金费；训练段到 2023 年底，验证段从 2024 年起。
- 这 5 条共用一个仓库 [factor_study2_failureprove](https://github.com/runningshark/factor_study2_failureprove)（需要 pandas、numpy），每条用自己的编号单独复现。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/factor_study2_failureprove/blob/master/FAILURE_REPORT.md)。

### 25 · 做空新上线的币（第 7–90 天）

每周日收盘，做空上线第 7 到 90 天、日成交额不低于 1000 万美元的新币永续（每个最多占资金的 5%，合计最多 50%），同时等额做多 20 个最活跃的老币对冲。检验的是“新币上线后都会跌，所以做空它”。（[档案](https://github.com/runningshark/factor_study2_failureprove/blob/master/reports/25_N1_new_listing_short_7_90.md)）

- **新币确实跌，但做空吃不到这个跌幅。** 不经过回测直接统计：442 个新币从上线第 7 天持有到第 90 天，76% 下跌，中位数 −39.0%，平均却是 +12.3%，因为少数暴涨的币把平均数拉成了正的。做空吃的是平均数，不是中位数：空头一侧的价格盈亏是每年 −9.1%。
- **牛市里被逼空。** 2021 年和 2024 年，空头一侧在价格上分别亏掉 56.9% 和 34.5%（按日盈亏相加，占资金的比例）；最差的一周组合亏 37.9%，最大回撤 −81.3%。
- **新币下跌的年份，资金费把利润吃掉。** 2025、2026 年空头一侧在价格上赚了 5.7%、34.7%，但付出的资金费是 41.2%、23.3%（同样按日相加）。窗口内做空平均每年要付约 11.6% 的资金费，说明做空新币的人已经很多了。
- **对冲和变体都救不了。** 全区间年化 −8.5%（t = −0.59），训练段 +3.8%，验证段 −23.3%；只用 BTC 对冲是 −2.2%；5 个邻近变体全部为负。
- 剩下的线索：新币会跌这件事是真的：上线第 7 天买入、持有到第 90 天，76% 的币是亏的，中位数 −39.0%。能用的结论是“别在上线头几个月买新币”，而不是“做空它”。负的资金费说明做空这个方向已经很拥挤。

```bash
git clone https://github.com/runningshark/factor_study2_failureprove
cd factor_study2_failureprove
py verify.py N1
```

### 26 · 做空新上线的币（第 91–365 天）

和 25 一样，换成上线第 91 到 365 天的币，避开刚上线时的炒作。（[档案](https://github.com/runningshark/factor_study2_failureprove/blob/master/reports/26_N2_new_listing_short_91_365.md)）

- **同样是少数暴涨拉高平均。** 380 个新币从上线第 91 天持有到第 365 天，74% 下跌，中位数 −51.2%，平均却是 +58.7%。空头一侧的价格盈亏是每年 −17.7%。
- **2021 年一年亏掉近一半。** 组合 2021 年 −44.1%：上线不到一年的币在牛市里涨得比老币多得多，空头一侧的亏损远大于多头一侧的盈利。
- **两段都是负的。** 训练段年化 −9.3%（t = −0.72），验证段 −6.6%（t = −0.43）；5 个邻近变体、3 项压力测试全部为负。
- **这个窗口里资金费不是问题**（空头一侧每年 +0.3%），亏在价格上。
- 剩下的线索：和第 25 条一样：上线第 91 天买入、持有到第 365 天，74% 下跌，中位数 −51.2%。结论同样是不要买，而不是做空。

```bash
git clone https://github.com/runningshark/factor_study2_failureprove
cd factor_study2_failureprove
py verify.py N2
```

### 27 · 散户多空比（反向）

每周日收盘，在成交额最高的 30 个有永续合约的币里，做多“全部账户多空人数比”最低的 10 个、做空最高的 10 个，等权，持有一周。检验的是“多空比是反向指标”。（[档案](https://github.com/runningshark/factor_study2_failureprove/blob/master/reports/27_P1_retail_ls_ratio.md)）

- **样本外反过来了。** 训练段（到 2023 年底）年化 +18.8%（t = 2.10），验证段 −12.0%（t = −1.18）；2023 年一年 +71.2%，之后三年是 −8.7%、−9.5%、−19.2%。
- **赚的主要是资金费，不是指标。** 拆开看：两侧的资金费合计约每年 +4.7%，价格盈亏合计约 +2.6%，成本 2.8%。散户扎堆做多的币正好是资金费高的币，这个指标大体上是资金费的另一种读法。
- **换一种算法就变号。** 信号改成一周的变化，年化 −12.6%（t = −1.96）；每边 6 个时 t = 0.57。
- **全区间不显著。** t = 0.62，零成本也只有 1.04。

```bash
git clone https://github.com/runningshark/factor_study2_failureprove
cd factor_study2_failureprove
py verify.py P1
```

### 28 · 大户持仓多空比（跟随）

和 27 一样，信号换成“大户持仓多空比”，方向是跟随：做多大户最偏多的 10 个、做空最偏空的 10 个。（[档案](https://github.com/runningshark/factor_study2_failureprove/blob/master/reports/28_P2_top_trader_ratio.md)）

- **方向是负的。** 年化 −8.5%（t = −1.49），训练段 −7.0%、验证段 −10.2% 都亏；4 个邻近变体全部为负（t 从 −2.43 到 −1.25）。
- **跟着大户还要倒贴资金费。** 两侧资金费合计每年约 −4.4%：大户持仓偏多的币资金费更高，做多它们要付钱。
- **可用的数据很短。** 归档里这个字段 2022 年几乎是空的，321 周里实际有仓位的只有 216 周，主要在 2023 年以后，训练段只有一年左右。

```bash
git clone https://github.com/runningshark/factor_study2_failureprove
cd factor_study2_failureprove
py verify.py P2
```

### 29 · 持仓量增速（反向）

和 27 一样，信号换成持仓量一周的增速：做多增长最慢的 10 个、做空增长最快的 10 个。检验的是“持仓量暴增说明杠杆过热”。（[档案](https://github.com/runningshark/factor_study2_failureprove/blob/master/reports/29_P3_oi_growth.md)）

- **方向和流行说法相反。** 做空持仓量增长最快的、做多最慢的：年化 −20.5%（t = −3.12），零成本也是 −14.2%（t = −2.18）；有仓位以来每一年都亏。
- **亏在多头一侧。** 持仓量增长最慢（常常是在减少）的币之后继续走弱：多头一侧的价格盈亏每年 −16.9%，空头一侧 +2.6%。
- **换手高。** 年换手 63 倍，成本每年 6.3%。
- **反过来做也不够。** 把方向反过来（不是登记的候选，只作说明）：零成本年化 +14.1%（t = 2.20），扣成本后 +7.9%（t = 1.23），验证段 +0.3%（t = 0.03）。
- 剩下的线索：持仓量增长快的币之后表现更好，方向和商品期货上的文献（Hong、Yogo）一致。但扣成本后不显著，验证段接近零，而且这是事后看到的方向，不能当成结论。

```bash
git clone https://github.com/runningshark/factor_study2_failureprove
cd factor_study2_failureprove
py verify.py P3
```

### 30 · 技术指标规则大全（467 条，30 币等权）

把常见技术指标（均线、MACD、RSI、布林带、KD、通道突破、一目均衡表、SuperTrend 等 21 类）展开成 467 条只做多的日线规则，每周日选成交额最高的 30 个币，每条规则在每个币上各自给信号。规则清单和通过标准同样是事先登记的。问的不是“哪一条好”，而是“最好的那一条，扣掉试了 467 条的运气之后还剩不剩”。

- **最好的一条经不起“试了 467 条”的校正。** 超额 t 最高的是“距 50 日低点涨 5% 买 距高点跌 5% 卖”，t = 2.85。如果 467 条全都没有择时能力，光靠运气，最大 t 的 95% 分位就有 3.28。Reality Check 的 p = 0.16，离登记的门槛 0.0024 很远。
- **成本。** 零成本时 p = 0.065（最大 t 3.20）；扣单边 0.10% 后 p = 0.16；成本翻倍后 p = 0.34（最大 t 2.50）。
- **样本外。** 只看训练段，最好的规则是“30 日涨幅 >5% 持有”（训练段 t 2.63），它在验证段的超额 t 只有 0.48。训练段前 10% 的 46 条规则合在一起，验证段 t 也只有 0.90。均线两类在验证段的 t 中位数是 0.00 和 −0.19。
- **逆势、摆动类没有择时能力。** 随机指标 KD 的 12 条规则超额全部为负（t 中位数 −2.05）。布林带回归、RSI 超卖买入、连跌接多、日历这几类，在类内部做同样的检验，p 都在 0.33 以上。
- 剩下的线索：趋势类规则（均线、MACD、布林带突破、SuperTrend、一目均衡表等）超额为正的占 89% 到 100%，方向一致，但没有一条单独显著。它们实在的作用是降回撤：一直持有这 30 个币，夏普 0.43、最大回撤 −94.9%；467 条里夏普超过持有的占 58%，夏普最高的一条（距 50 日低点涨 5% 买 距高点跌 5% 卖）夏普 1.18、最大回撤 −21.1%。可以当风控，不能当成稳定的超额来源。

```bash
git clone https://github.com/runningshark/d1_indicator_zoo_failureprove
cd d1_indicator_zoo_failureprove
py verify.py
```

### 31–34 · 第四轮事先登记的研究：卖波动率（共用一个仓库）

前三轮没有一个通过，这一轮测机构里最经典的“有人付钱给你”的收益：期权的波动率溢价。数据是 Deribit 期权的历史逐笔成交，成交价用“主动卖出”的成交（卖给买一价）。规则和通过标准同样是事先登记的（[事先登记_第四轮.md](https://github.com/runningshark/w1_short_straddle_failureprove/blob/master/事先登记_第四轮.md)）。**4 个全部失败。**

- 累计 25 个候选，门槛是 t ≥ 3.1。
- 这 4 条共用一个仓库 [w1_short_straddle_failureprove](https://github.com/runningshark/w1_short_straddle_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/w1_short_straddle_failureprove/blob/master/FAILURE_REPORT.md)。

### 31 · 每周卖出 BTC 平值跨式（不对冲）

每个周五在 Deribit 上卖出下周五到期的 BTC 平值看涨和看跌各一张（按买一侧的真实成交价），持有到期，每周的名义金额等于全部资金。检验的是“卖期权收波动率溢价”。（[档案](https://github.com/runningshark/w1_short_straddle_failureprove/blob/master/reports/31_V1_btc_short_straddle.md)）

- **收到的权利金和赔出去的几乎一样多。** 平均每周收权利金 5.94%，到期平均赔付 5.83%（都按进场时的现货价计）。按买一价卖出时，成交的隐含波动率平均 55%，而之后一周实际走出来的波动率是 60%：在周度平值期权上，“隐含高于实现”这个前提在这段样本里不成立。
- **亏损集中在少数几周。** 385 周里赚钱的周占 63%，但全部加起来只有 +14%，其中最差的 5 周合计 −134%。最差的一周（2020-03-13 到期）亏 38.8%，最大回撤 −77.3%。
- **对成交价极其敏感。** 权利金打 95 折（成交价再差 5%），年化变成 −13.4%；打 90 折是 −28.7%；费用翻倍是 −2.0%。
- **全区间 t = 0.12。** 训练段年化 +0.7%（t = 0.03），验证段 +3.7%（t = 0.21）；2020、2021、2023、2024 年为负。
- 剩下的线索：卖方的优势如果存在，也薄到被买卖价差吃掉：用全部成交的均价（接近中间价）再打 97 折是 −6.4%，按买一价是 +1.9%，差别就在这几个点的成交价上。对做市商（挂单、赚价差）和对散户（吃单、付价差）来说，这是两个不同的策略。

```bash
git clone https://github.com/runningshark/w1_short_straddle_failureprove
cd w1_short_straddle_failureprove
py verify.py V1
```

### 32 · 每周卖出 ETH 平值跨式（不对冲）

和 31 一样，换成 ETH。（[档案](https://github.com/runningshark/w1_short_straddle_failureprove/blob/master/reports/32_V2_eth_short_straddle.md)）

- **权利金抵不掉赔付。** 平均每周收权利金 7.26%，到期平均赔付 7.27%。成交的隐含波动率平均 67%，之后一周实际的波动率是 71%。
- **两段都是负的。** 全区间年化 −3.8%（t = −0.24），训练段 −3.2%，验证段 −4.8%；2020、2021、2022、2023、2024、2025 年为负，最大回撤 −86.9%。
- **变体全部为负。** 下午进场 −5.0%，全部成交均价打 97 折 −23.5%，宽跨式 −14.1%。
- **成交稀疏。** 382 周里只有 332 周找得到两条腿都有主动卖出成交的行权价，每周用到的成交笔数中位数只有 18 笔。

```bash
git clone https://github.com/runningshark/w1_short_straddle_failureprove
cd w1_short_straddle_failureprove
py verify.py V2
```

### 33 · 每周卖出 BTC 平值跨式（每天对冲）

和 31 一样，另外每天用永续合约把 delta 对冲掉，只留下波动率的敞口。（[档案](https://github.com/runningshark/w1_short_straddle_failureprove/blob/master/reports/33_V3_btc_short_straddle_hedged.md)）

- **对冲把风险降下来了，收益仍然不显著。** 每天对冲之后，最差的一周从 38.8% 降到 17.8%，最大回撤从 −77.3% 降到 −38.5%，年化 +6.8%，但 t 只有 0.98（训练段 0.65，验证段 0.97）。
- **对冲本身要花钱。** 每天调一次，对冲成本每年约 5.5%。
- **对成交价同样敏感。** 权利金打 95 折，年化变成 −8.5%；打 90 折 −23.8%；费用翻倍 −2.5%。
- **变体不稳。** 下午进场 +14.4%（t = 2.21），全部成交均价打 97 折 +0.8%，宽跨式 +3.8%（t = 0.88）：同一个策略换个进场时间差一倍，说明结果很依赖成交价的细节。
- 剩下的线索：每天对冲的 BTC 版本是四个里唯一为正的（年化 +6.8%，下午进场的变体 t = 2.21），但没有过任何一条门槛，而且下午进场是事后看到的。要判断它需要更细的数据（挂单价、盘口深度），日线级别的回测判断不了。

```bash
git clone https://github.com/runningshark/w1_short_straddle_failureprove
cd w1_short_straddle_failureprove
py verify.py V3
```

### 34 · 每周卖出 ETH 平值跨式（每天对冲）

和 33 一样，换成 ETH。（[档案](https://github.com/runningshark/w1_short_straddle_failureprove/blob/master/reports/34_V4_eth_short_straddle_hedged.md)）

- **对冲之后还是负的。** 年化 −5.0%（t = −0.59），训练段 −1.9%，验证段 −9.9%；最大回撤 −62.0%。
- **权利金本来就不够。** 平均每周收 7.26%，赔 7.27%；对冲成本每年还要约 5.7%。
- **压力测试和多数变体为负。** 权利金打 95 折 −21.4%，费用翻倍 −13.4%；全部成交均价打 97 折 −13.0%，宽跨式 −10.5%。

```bash
git clone https://github.com/runningshark/w1_short_straddle_failureprove
cd w1_short_straddle_failureprove
py verify.py V4
```

### 35–37 · 第五轮事先登记的研究：配对交易（共用一个仓库）

前面测的都是单个币的择时、按指标排队的多空，或者卖期权。这一轮测“两个币之间的价差会收回来”这一类。规则和通过标准同样是事先登记的（[事先登记_第五轮.md](https://github.com/runningshark/pairs_trading_failureprove/blob/master/事先登记_第五轮.md)）。**3 个全部失败。**

- 累计 28 个候选，门槛是 t ≥ 3.2。成本单边 0.10%，多空都用永续合约并计入资金费。
- 这 3 条共用一个仓库 [pairs_trading_failureprove](https://github.com/runningshark/pairs_trading_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/pairs_trading_failureprove/blob/master/FAILURE_REPORT.md)。

### 35 · 距离法配对交易

每 4 周在成交额最高的 30 个币里，挑过去 180 天走势最贴近的 10 对；之后 4 周里，一对的价差超过 2 倍标准差就做空高的、做多低的，价差收回来平仓。配对交易最经典的做法。（[档案](https://github.com/runningshark/pairs_trading_failureprove/blob/master/reports/35_S1_distance_pairs.md)）

- **零成本也不赚。** 全区间年化 −2.7%（t = −0.78），不扣成本也是 −1.0%（t = −0.30）：价差拉开之后并没有收回来的倾向。
- **两段都为负。** 训练段年化 −3.3%，验证段 −2.0%；7 年里 2021、2022、2023、2024、2025、2026 年为负。
- **4 个邻近变体全部为负。** 依次是 −3.4%、−2.6%、−3.7%、−8.4%（阈值 1.5σ、阈值 2.5σ、形成期 90 天、取 20 对）。
- **拆开看。** 做空的一侧（涨得多的那个币）每年在价格上亏 6.0%，做多的一侧赚 +5.3%，合起来接近零，再扣成本每年 1.7%。

```bash
git clone https://github.com/runningshark/pairs_trading_failureprove
cd pairs_trading_failureprove
py verify.py S1
```

### 36 · 协整配对交易

和 35 一样，选对的方法换成协整检验：用对数价格回归，挑残差最像“会回到均值”的 10 对。（[档案](https://github.com/runningshark/pairs_trading_failureprove/blob/master/reports/36_S2_cointegration_pairs.md)）

- **方向是反的，而且显著。** 全区间年化 −16.7%（t = −3.24），零成本也是 −14.6%（t = −2.84），7 年里每一年都亏，最大回撤 −71.3%。
- **形成期里看起来协整，到了交易期继续拉开。** 做空的一侧每年在价格上亏 24.0%，做多的一侧只赚 +9.5%：被判成“偏高”的币之后继续跑赢。
- **变体。** 开仓阈值 1.5σ 是 −21.8%，2.5σ 是 −12.6%，取 20 对是 −18.2%，形成期 90 天是 −1.0%。
- **反过来做是事后的方向，也没到门槛。** 把方向反过来（赌价差继续拉开；不是登记的候选，只作说明）：零成本年化 +14.6%（t = 2.84），扣成本后 +12.5%（t = 2.44），训练段 t 1.58，验证段 t 2.07。
- 剩下的线索：在成交额最高的这批币里，价差拉开之后更常见的是继续拉开，而不是收回来。这和合集第 14 条（一周动量在零成本下为正）、第 18 条（一日反转零成本也亏）是同一件事的不同侧面。反过来做扣成本后 t = 2.44，没到门槛，而且是事后看到的方向，需要新数据确认，不能当成结论。

```bash
git clone https://github.com/runningshark/pairs_trading_failureprove
cd pairs_trading_failureprove
py verify.py S2
```

### 37 · ETH/BTC 比值回归

ETH/BTC 的比值相对过去 90 天偏离超过 2 倍标准差，就赌它回来：偏高做空 ETH、做多 BTC，偏低反过来。（[档案](https://github.com/runningshark/pairs_trading_failureprove/blob/master/reports/37_S3_ethbtc_ratio.md)）

- **没有信号。** 全区间年化 +0.7%（t = 0.09），零成本 +2.0%（t = 0.29）。
- **样本外为负。** 训练段年化 +2.4%，验证段 −1.4%；2025 年一年 −19.3%。
- **变体有正有负。** 窗口 60 天、180 天，阈值 1.5、2.5，依次是 −5.4%、−0.7%、−1.6%、+3.1%。
- **次数太少。** 六年多只开仓 36 次，就算有效果，统计上也说明不了。

```bash
git clone https://github.com/runningshark/pairs_trading_failureprove
cd pairs_trading_failureprove
py verify.py S3
```

### 38–40 · 第七轮事先登记的研究：日历和时段（共用一个仓库）

这一轮测要用小时线才能检验的三种说法，都是“到了某个时刻就该做什么”。规则和通过标准同样是事先登记的（[事先登记_第七轮.md](https://github.com/runningshark/h1_calendar_failureprove/blob/master/事先登记_第七轮.md)）。**3 个全部失败。**

- 累计 36 个候选（其中第六轮的 5 个是下面的第 41–45 条，公开得晚），门槛是 t ≥ 3.2。用 BTC 永续的 1 小时线，每次开仓、平仓各付 0.10%，计入资金费。
- 这 3 条共用一个仓库 [h1_calendar_failureprove](https://github.com/runningshark/h1_calendar_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/h1_calendar_failureprove/blob/master/FAILURE_REPORT.md)。

### 38 · CME 缺口回补

CME 的比特币期货周五收盘、周日开盘，中间价格跳开的那一段叫缺口。缺口不小于 1% 时，周日开盘就往回补的方向做（向上的缺口做空，向下的做多），碰到周五收盘价就平，一周没碰到也平。（[档案](https://github.com/runningshark/h1_calendar_failureprove/blob/master/reports/38_G1_cme_gap.md)）

- **回补比例没有流传的那么高，而且不回补的时候亏得多。** 360 个周末里缺口不小于 1% 的有 186 个，一周内回补的占 69%（24 小时内 42%）。回补的平均赚 2.4%，没回补的 57 笔平均亏 7.9%。合起来赚钱的占 72%，平均每笔却是 −0.74%。
- **不是成本问题。** 全区间年化 −19.5%（t = −1.60），最大回撤 −88.0%；不扣成本也是 −14.0%。7 年里 6 年为负。
- **亏的那几笔都在大行情里。** 2020-03-08 那个周末向下跳了 9.5%，往回做之后一周亏 35.2%；2023-03-12 向上跳了 5.9%，亏 25.9%。周末跳得大，往往是有事发生，行情接着走。
- **和 CME 关系不大。** 把“周五收盘”换成一周里别的日子，同样隔两天、同样的规则，回补比例是 46% 到 63%，年化 −36.6% 到 +0.5%。价格本来就来回波动，两天前的价位之后被碰到是常事。
- **变体。** 门槛 0.5%、门槛 2%、最多拿 48 小时、加止损，依次是 −23.2%、−18.5%、−17.8%、−23.3%；换成 ETH 是 +11.6%（t = 0.60），不显著，也和 BTC 的结果相反。

```bash
git clone https://github.com/runningshark/h1_calendar_failureprove
cd h1_calendar_failureprove
py verify.py G1
```

### 39 · 议息前 24 小时做多

美联储每次例行议息声明前 24 小时做多 BTC，声明发布时平仓。股票上有名的“议息前漂移”搬到 BTC 上。（[档案](https://github.com/runningshark/h1_calendar_failureprove/blob/master/reports/39_F1_pre_fomc.md)）

- **全靠 2020 年。** 54 次里上涨的占 63%，不扣成本平均每次 +0.81%。分年看 2020 年 +35.6%，之后是 2021 −6.0%、2022 +11.9%、2023 +3.1%、2024 −3.4%、2025 −0.7%、2026 −4.0%；去掉 2020 年，年化只剩 +0.3%（t = 0.10）。
- **样本外为负。** 训练段年化 +10.3%（t = 1.95），验证段 −2.6%（t = −0.74）。
- **不是议息带来的。** 把同样的 24 小时挪到前一周、后一周、前两周、后两周（都不是议息的日子），不扣成本平均每次是 +0.72%、+0.22%、+0.28%、+0.58%。这几年 BTC 本来就是涨的，随便哪个 24 小时平均都是正的。
- **统计上不显著。** 全区间年化 +4.8%，t = 1.41，对 BTC 回归后的超额 t = 1.13；4 个变体依次是 +4.1%、+5.2%、+4.4%、+0.3%。

```bash
git clone https://github.com/runningshark/h1_calendar_failureprove
cd h1_calendar_failureprove
py verify.py F1
```

### 40 · 每天 21–23 点（UTC）做多

每天 UTC 21 点买入 BTC、23 点卖出。出处是 Quantpedia 收录的一篇论文，称这两个小时的收益明显更高。（[档案](https://github.com/runningshark/h1_calendar_failureprove/blob/master/reports/40_T1_hours_21_23.md)）

- **手续费。** 每天一进一出，单边 0.10% 一年就是 73%。全区间年化 −47.4%（t = −8.05），每一年都亏，累计 −96.5%。
- **这个时段效应本身是真的。** 不扣成本年化 +25.6%（t = 4.35），训练段 t = 3.24，验证段 t = 2.99；在 23 个两小时时段里排第 1，紧挨着的 20–22 点是 +22.9%；ETH 上也有（+31.4%，t = 4.01）。原文是 2022 年发表的，在它之后的年份里这个现象还在（不扣成本时 2022 年 −13.7%、2026 年 −3.9%，其余年份为正）。
- **但每笔只有 +0.07%。** 来回的成本超过这个数就是亏的：单边 0.05% 是 −10.9%；按挂单费率单边 0.02% 算是 +11.0%（t = 1.87），而且挂单不保证成交。
- **变体全部为负。** 20–22 点、22–24 点、只做周一到周五、换成 ETH，依次是 −50.1%、−71.3%、−33.2%、−41.6%。
- 剩下的线索：UTC 21 点到 23 点这两个小时，BTC 平均是涨的：不扣成本 t = 4.35，训练段和验证段各自都接近 3，ETH 上也成立，窗口是原文事先给定的，不是这里挑出来的。它不够付吃单的手续费，不能当成一个策略。能想到的用处是“反正要成交的时候挑时间”：同一笔买入放在 21 点比放在 23 点平均便宜约 0.07%。这个用法没有单独检验过。

```bash
git clone https://github.com/runningshark/h1_calendar_failureprove
cd h1_calendar_failureprove
py verify.py T1
```

### 41–45 · 第六轮事先登记的研究：代币事件（共用一个仓库）

测“某件事发生前后做空”这一类：代币解锁、币安下架公告、币安观察标签。规则和通过标准同样是事先登记的（[事先登记_第六轮.md](https://github.com/runningshark/token_events_failureprove/blob/master/事先登记_第六轮.md)）。**5 个全部失败。**

- 这一轮做在第七轮（38–40）之前，公开得晚，所以编号排在后面。登记时累计 33 个候选，门槛是 t ≥ 3.2。做空事件里的币，等额做多 20 个最活跃的老币对冲；成本单边 0.10%，计入资金费。
- **第 41–43 条不能只靠仓库复现**：解锁时间表来自 DefiLlama，它的使用条款不允许转载，数据和下载脚本都没有放进仓库（需要的文件格式见 [data/README.md](https://github.com/runningshark/token_events_failureprove/blob/master/data/README.md)）。第 44、45 条可以直接复现。
- 这 5 条共用一个仓库 [token_events_failureprove](https://github.com/runningshark/token_events_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/token_events_failureprove/blob/master/FAILURE_REPORT.md)。

### 41 · 解锁前 14 天做空

团队、顾问、投资人的筹码一次解锁不少于流通量的 1% 时，提前 15 天做空这个币，解锁前一天平仓，同时等额做多 20 个最活跃的老币对冲。检验的是“解锁前会砸盘”。（[档案](https://github.com/runningshark/token_events_failureprove/blob/master/reports/41_U1_short_before_unlock.md)）

- **多数会跌，但幅度很小。** 792 个事件里，解锁前 14 天下跌的占 63%（流传的说法是 90%），中位数 −5.5%；减去同期 30 币等权篮子之后，跑输的占 65%，平均只有 −1.5%。按解锁量占流通量分：1–5%：623 个，相对大盘平均 −0.9%；5–10%：98 个，相对大盘平均 −4.2%；10% 以上：71 个，相对大盘平均 −3.1%。
- **挑日子没有用。** 同样的币、同样多的事件，把日期换成随机的，重复 40 次，t 平均 0.96；真实日期的 t 是 1.15，40 次里有 12 次不比它差。那点正收益来自“这批还在解锁期的币整体跑输老币”，和解锁那一天无关。
- **不显著，也不稳定。** 全区间年化 +4.3%（t = 1.15），前段 t = 1.25，后段 t = 0.84；2024 年 +20.3%、2025 年 +22.2%、2026 年 −19.5%。
- **做空一侧赚的被吃掉大半。** 空头一侧在价格上每年赚 10.5%，付资金费 1.1%；对冲篮子每年亏 2.6%，另付资金费 0.5%；成本每年 2.0%。成本三倍后只剩 +0.4%。
- **变体。** 窗口 7 天、窗口 30 天、门槛 0.5%、门槛 5%、只用 BTC 对冲，依次是 +1.2%、+7.3%、+5.0%、+0.8%、+8.5%，t 最高 1.64。
- 剩下的线索：还在解锁期的币整体跑输老币，这在真实日期和随机日期的结果里都看得到（t 在 1 上下），但没有到显著的程度，也和解锁的日子无关。“解锁前会跌”作为描述大体成立（63% 下跌），作为交易依据不成立。

```bash
git clone https://github.com/runningshark/token_events_failureprove
cd token_events_failureprove
py verify.py U1      # 没有 DefiLlama 数据时只显示归档数字
```

### 42 · 解锁后 14 天做空

和 41 一样，换成解锁前一天做空、拿到解锁后第 13 天。检验的是“解锁之后还会跌”。（[档案](https://github.com/runningshark/token_events_failureprove/blob/master/reports/42_U2_short_after_unlock.md)）

- **解锁之后并没有明显多跌。** 781 个事件里，解锁后 14 天下跌的占 59%，中位数 −3.9%；减去同期 30 币等权篮子之后，平均只有 −0.8%。按解锁量占流通量分：1–5%：613 个，相对大盘平均 −0.6%；5–10%：98 个，相对大盘平均 −2.9%；10% 以上：70 个，相对大盘平均 +0.1%。
- **前段是亏的。** 2023 年底以前年化 −3.3%（t = −1.43），2024 年以后 +11.4%（t = 1.56）；全区间 t = 0.95。
- **随机日期更好。** 同样的币、同样多的事件，日期换成随机的，重复 40 次，t 平均 1.29，其中 30 次不比真实日期差。
- **经不起成本。** 成本翻倍 +1.4%，成本三倍 −0.6%，晚一天执行 +2.0%。
- **变体。** 窗口 7 天、窗口 30 天、门槛 0.5%、门槛 5%、只用 BTC 对冲，依次是 +3.8%、+2.0%、+5.1%、+0.2%、+4.5%，t 最高 1.73。
- 剩下的线索：和第 41 条相同：跑输是这批币的常态，不是解锁那一天带来的。

```bash
git clone https://github.com/runningshark/token_events_failureprove
cd token_events_failureprove
py verify.py U2      # 没有 DefiLlama 数据时只显示归档数字
```

### 43 · 稀释多空（空临近解锁的，多已经放完的）

每周做空未来 30 天有大额解锁的币，做多筹码已经放完的币。检验的是“解锁压力大的币跑输”。（[档案](https://github.com/runningshark/token_events_failureprove/blob/master/reports/43_U3_dilution_long_short.md)）

- **方向和说法一致，但太吵。** 全区间年化 +9.3%，t 只有 1.20，最大回撤 −29.2%；2021 年一年 −15.4%。前段 t = 0.53，后段 t = 1.30。
- **收益来自多头那一组，不是来自做空解锁币。** 多头（筹码已经放完的币，平均 22 个）每年在价格上赚 +19.4%；空头（临近大额解锁的币，平均 13 个）每年在价格上是 −5.8%，做空它们本身是亏的。
- **把多头换成普通的对冲篮子就没有了。** 这个变体年化 −2.2%（t = −0.24）。
- **其余变体。** 空头门槛 0.5%、空头门槛 3%、改看未来 90 天，依次是 +11.1%、+3.3%、+8.7%；对市场回归后的超额 t = 0.87。
- 剩下的线索：方向和流传的说法一致（临近大额解锁的币跑输筹码已经放完的币），多空年化 +9.3%，但 t 只有 1.20，而且主要来自多头那一组。需要更长的样本才能下结论。

```bash
git clone https://github.com/runningshark/token_events_failureprove
cd token_events_failureprove
py verify.py U3      # 没有 DefiLlama 数据时只显示归档数字
```

### 44 · 下架公告后做空

币安公告要下架某个币，当天收盘做空它的合约，拿到合约下架。检验的是“被下架的币会暴跌”。（[档案](https://github.com/runningshark/token_events_failureprove/blob/master/reports/44_D1_short_after_delist_notice.md)）

- **跌在公告当天，这一段吃不到。** 62 个当时有合约的下架事件，公告当天下跌的占 87%，中位数 −21.3%。规则是公告当天收盘才进场，检验的是看到公告再动手的人。
- **之后多数继续跌，平均却是涨的。** 从公告当天收盘拿到合约下架（中位数 6 天），下跌的占 76%，中位数 −15.5%，平均是 +21.1%：少数被逼空暴涨的把平均数拉成了正的（ALPACA +1709%、AERGO +320%、HFT +154%、A2Z +139%）。
- **合格的事件太少。** 满足成交额条件、实际开仓的只有 17 个，按登记的规则直接记为失败（样本不足）。这 17 个的结果是年化 +0.5%（t = 0.32）。
- **放宽门槛就亏。** 成交额门槛降到 200 万美元有 44 个事件，年化 −10.2%（t = −0.93），最差的一天亏 25.3%，最差的一周亏 31.1%。
- 剩下的线索：能用的结论是反过来的：别在下架公告之后去做空流动性差的币。多数时候小赚，偶尔一次被逼空亏掉很多，和合集第 25 条（做空新上线的币）是同一种死法。

```bash
git clone https://github.com/runningshark/token_events_failureprove
cd token_events_failureprove
py verify.py D1
```

### 45 · 观察标签后做空

币安给某个币打上观察标签，当天收盘做空它的合约，拿 30 天。检验的是“观察标签是下架预备队”。（[档案](https://github.com/runningshark/token_events_failureprove/blob/master/reports/45_M1_short_after_monitoring_tag.md)）

- **消息当天就反映完了。** 93 个事件，公告当天下跌的占 92%，中位数 −12.0%，这一段吃不到。之后 30 天下跌的占 67%，但减去同期 30 币等权篮子之后平均是 +0.4%，什么都不剩。
- **同样有逼空。** 打标签之后涨得最多的：SYN +282%、VOXEL +177%、BSW +125%、FLM +106%。
- **不显著。** 实际开仓 34 个事件，全区间年化 +3.1%（t = 1.02），前段 t = 0.97，后段 t = 0.31。
- **变体。** 拿 14 天、拿 60 天、成交额门槛 200 万美元、只用 BTC 对冲，依次是 +2.8%、+7.2%、−2.8%、+5.4%；门槛放宽后有 73 个事件，最差的一周亏 25.5%。

```bash
git clone https://github.com/runningshark/token_events_failureprove
cd token_events_failureprove
py verify.py M1
```

### 46–48 · 第八轮事先登记的研究：成交量和流动性（共用一个仓库）

前面几轮里成交量只当过筛选条件，这一轮把它当信号来测。规则和通过标准同样是事先登记的（[事先登记_第八轮.md](https://github.com/runningshark/volume_liquidity_failureprove/blob/master/事先登记_第八轮.md)）。**3 个全部失败。**

- 累计 39 个候选，门槛是 t ≥ 3.3。数据和币池同第 14–18 条：成交额最高的 30 个币，多空都用永续合约，每周调仓，成本单边 0.10%，计入资金费。
- 这 3 条共用一个仓库 [volume_liquidity_failureprove](https://github.com/runningshark/volume_liquidity_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/volume_liquidity_failureprove/blob/master/FAILURE_REPORT.md)。

### 46 · 非流动性溢价

教科书里的“非流动性溢价”：同样的成交额把价格推得越远，这个币越不流动。每周做多最不流动的 10 个币，做空最流动的 10 个。（[档案](https://github.com/runningshark/volume_liquidity_failureprove/blob/master/reports/46_L1_illiquidity_premium.md)）

- **方向是反的。** 全区间年化 −18.6%（t = −1.84），验证段 −34.0%（t = −2.83），对 BTC 回归后的超额 t = −2.19，最大回撤 −78.9%。
- **亏在做空的那一边。** 被做空的是币池里流动性最好的 10 个币，也就是 BTC、ETH 这一类大币；它们每年在价格上让空头亏 24.3%，做多的那 10 个流动性差的币每年只赚 +4.1%。这个组合实际上是“空大币、多小币”，和合集第 24 条（多 BTC 空山寨）正好反着。
- **变体全部为负。** 池子 50 个、每边 6 个、按波动率倒数加权、窗口 60 天，依次是 −13.3%、−24.3%、−13.9%、−22.6%。换成最简单的成交额水平（做多成交额最低的 10 个）也是 −14.1%（t = −1.64）。
- **越近越差。** 2024 年 −42.6%、2025 年 −30.0%、2026 年 −14.6%；7 年里 5 年为负。
- 剩下的线索：在成交额最高的这批币里，流动性越好的币表现越好，持有冷门币没有得到补偿，和原文在股票上的方向相反。反过来做（多流动性好的、空流动性差的）是事后的方向，t 的绝对值也只有 1.84，不能当成结论。

```bash
git clone https://github.com/runningshark/volume_liquidity_failureprove
cd volume_liquidity_failureprove
py verify.py L1
```

### 47 · 成交量冲击

“放量的币要涨”：每周做多成交额相对自己过去 8 周放大最多的 10 个币，做空萎缩最多的 10 个。（[档案](https://github.com/runningshark/volume_liquidity_failureprove/blob/master/reports/47_L2_volume_shock.md)）

- **没有信号。** 全区间年化 +6.1%（t = 0.64），不扣成本也只有 +10.9%（t = 1.15）；训练段 t = 0.38，验证段 t = 0.59。
- **变体有正有负。** 池子 50 个 −2.5%、每边 6 个 +10.5%、按波动率倒数加权 +7.2%、改看 14 天 −4.5%。
- **换手高。** 放量倍数每周都在变，年换手 48 倍，成本每年 4.8%；成本翻倍后只剩 +1.3%。
- **分年不稳定。** 2021、2022、2026 年为负，其中 2022 年 −24.4%、2026 年 −22.4%。

```bash
git clone https://github.com/runningshark/volume_liquidity_failureprove
cd volume_liquidity_failureprove
py verify.py L2
```

### 48 · 量价配合

“量价配合”：只在放量的那一半币里做一周动量，做多涨得最多的 5 个，做空跌得最多的 5 个。（[档案](https://github.com/runningshark/volume_liquidity_failureprove/blob/master/reports/48_L3_volume_confirmed_momentum.md)）

- **加了成交量条件，比不加更差。** 只在放量的币里做 7 天动量：年化 +10.7%（t = 0.74）。不看成交量、直接做涨幅最高和最低各 5 个：+27.3%（t = 1.91）。在缩量的那一半里做同样的事：+20.1%（t = 1.70）。“放量上涨才是真涨”在这里不成立，放量的那一半里动量反而更弱。
- **训练段是负的。** 训练段 t = −0.11，验证段 t = 1.60；2022 年 −20.1%、2023 年 −27.6%，最大回撤 −66.3%。
- **经不起成本和延迟。** 年换手 83 倍，成本每年 8.3%；成本翻倍 +2.4%，晚一天执行 +1.9%。
- **变体。** 池子 50 个、每边 3 个、按波动率倒数加权、都改看 14 天，依次是 +12.9%、+33.2%、+0.8%、+16.8%，t 最高 1.81。
- 剩下的线索：不加成交量条件的 7 天动量，不扣成本 t = 2.51，扣成本后 1.91，和合集第 14 条的结果一致：一周动量是有的，但不够显著，也经不起成本。成交量条件没有帮上忙。动量在缩量的那一半里更强一些（t = 1.70），这是事后看到的，需要新数据确认。

```bash
git clone https://github.com/runningshark/volume_liquidity_failureprove
cd volume_liquidity_failureprove
py verify.py L3
```

### 49–53 · 第九轮事先登记的研究：链上指标择时（共用一个仓库）

前面八轮用的都是交易所里的数据。这一轮测“看链上数据决定该不该持有比特币”的几个流传最广的说法。规则和通过标准同样是事先登记的（[事先登记_第九轮.md](https://github.com/runningshark/onchain_timing_failureprove/blob/master/事先登记_第九轮.md)）。**登记 6 个，5 个失败**；另外 1 个没有被判为失败，不在这里。

- 累计 45 个候选，门槛是 t ≥ 3.3。只做 BTC 现货的满仓 / 空仓，指标晚一天使用，每次进出成本 0.10%，2012-01-01 到 2026-05-23，训练段到 2019 年底。
- 看的是**择时超额**：规则每天的净收益对 BTC 当天涨跌回归后的截距。只做多的规则光看收益没有意义，这段时间比特币自己涨了一万多倍。另外做了平移检验（把仓位整体前后挪动，看真实的那一种排在哪里），因为这类规则几年才换一次仓。
- 5 条规则最后的钱都比一直持有少。
- 这 5 条共用一个仓库 [onchain_timing_failureprove](https://github.com/runningshark/onchain_timing_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/onchain_timing_failureprove/blob/master/FAILURE_REPORT.md)。数据是 Coin Metrics 的社区数据（CC BY-NC 4.0）。

### 49 · MVRV 估值择时

“MVRV 太高是顶，低于 1 是底”。MVRV 是市值除以已实现市值（每个币按最后一次转账时的价格算）。登记的规则：高于 3.5 清仓，跌回 1 以下再买回来；原文的顶部线是 3.7。（[档案](https://github.com/runningshark/onchain_timing_failureprove/blob/master/reports/49_O1_mvrv_valuation.md)）

- **没过门槛，离“待观察”只差一条。** 择时超额年化 +23.5%（t = 2.19），门槛是 3.3；训练段 t = 1.61，验证段 t = 1.87。平移检验 p = 0.064：把仓位整体前后挪动，有 6.4% 的挪法不比真实的差，“待观察”要求不超过 5%。
- **14 年只离场 3 次，其中 2 次回场价比离场价高。** 2013-03 离场（46 美元）→ 2014-10 回场（323 美元）；2017-06 离场（2,707 美元）→ 2018-11 回场（4,318 美元）；2021-01 离场（39,216 美元）→ 2022-06 回场（22,073 美元）。规则把 1 变成 2,568，一直持有是 16,253。
- **超额来自少承担了波动，不是躲开了下跌。** 空仓的日子（占 31%）BTC 平均每天的涨幅折成一年是 +92.6%，和持有的日子（+98.9%）差不多；不同的是波动，空仓期间年化 100.7%，持有期间 62.4%。回归里贝塔只有 0.46，所以算出来是正的超额，钱却比一直持有少。最大回撤是 −61.4%，一直持有是 −84.5%。
- **结论取决于顶部线差 0.2（登记之外的重算）。** 原文的顶部线是 3.7，登记时写的是 3.5。换成 3.7：择时超额 +34.0%，t = 3.14，平移检验 p = 0.0002，仍然不到 3.3。差别只来自一次交易：2017 年的离场从 6 月（2,707 美元）变成了 12 月（17,032 美元）。顶部线从 3.0 到 4.2 每隔 0.1 算一遍，3.0–3.6 的 t 在 1.77 到 2.37 之间，3.7–3.9 在 3.14 到 3.31 之间，4.0 以上又回到 2.20 左右（2021 年不再离场）。
- **顶部线一轮比一轮够不着。** 每轮牛市 MVRV 的最高值：2013 年 5.88，2017 年 4.72，2021 年 3.96，2024 年 2.78，2025 年 2.52。3.5 最后一次被碰到是 2021-03-19。2023 年以后规则一直满仓，2025 年的高点和之后的下跌它都没有任何动作。
- 剩下的线索：择时超额一直是正的，顶部线从 3.0 到 4.2 都是（+19% 到 +36%），训练段和验证段也都为正。原文的 3.7 事后重算 t = 3.14、平移检验 p = 0.0002，但那是看了结果之后才用的线，样本只有 3 次离场，而且 2024–2025 这一轮 MVRV 最高只到 2.78，按哪条线都没有信号。要把它当成候选，需要一条不依赖固定数值的规则，另外登记，等新的周期来验证。

```bash
git clone https://github.com/runningshark/onchain_timing_failureprove
cd onchain_timing_failureprove
py verify.py O1
```

### 50 · 交易所余额下降就持有

“币从交易所流出是看涨”。规则：交易所里的 BTC 比 30 天前少就持有，否则空仓。（[档案](https://github.com/runningshark/onchain_timing_failureprove/blob/master/reports/50_O2_exchange_balance.md)）

- **没有信号。** 择时超额年化 +5.7%（t = 0.61）；训练段 +12.0%（t = 1.00），验证段 −0.7%（t = −0.06）；平移检验 p = 0.247。
- **涨得多的反而是余额上升的日子。** 余额下降、规则持有的日子占 39%，这些日子 BTC 平均每天的涨幅折成一年是 +77.3%；余额上升、规则空仓的日子占 61%，折成一年是 +109.5%。只看 2020 年以后也一样：+50.3% 对 +61.5%。差别不显著，但方向和说法相反。
- **错过了大部分涨幅。** 规则把 1 变成 21.2，一直持有是 16,253。2013 年它只有 1% 的时间在场（那一年 BTC 涨 5,286%），2017 年 39%（BTC 涨 1,337%），2020 年 58%（BTC 涨 305%）。
- **变体里有两个好看一些，主规则撑不起来。** 和 7 天前比 +14.3%（t = 1.48），和 90 天前比 +20.0%（t = 2.42），改用净流量 +5.3%（t = 0.57），改用余额占流通量的比例 +6.1%（t = 0.65）。四个都没有到门槛，主规则的 t 只有 0.61。
- **换手多。** 进出 297 次；成本翻倍后择时超额剩 +3.6%。

```bash
git clone https://github.com/runningshark/onchain_timing_failureprove
cd onchain_timing_failureprove
py verify.py O2
```

### 51 · 活跃地址上升就持有

“链上活跃度上升是看涨”。规则：活跃地址数的 30 日均值高于 365 日均值就持有，否则空仓。（[档案](https://github.com/runningshark/onchain_timing_failureprove/blob/master/reports/51_O3_active_addresses.md)）

- **全区间不显著。** 择时超额年化 +10.6%（t = 1.24），平移检验 p = 0.171。
- **2020 年以后没有了。** 训练段 +17.6%（t = 1.72），验证段 0.0%（t = 0.00）。
- **最近一轮牛市它基本不在场。** 2024 年 BTC 涨 121%，规则只有 15% 的时间持有，赚 9%；2023 年 BTC 涨 155%，规则赚 61%。2023 年以后合计：规则 +88%，一直持有 +364%，持仓时间 34%。这种读法是 2022 年提出的，这一段才是它真正的样本外。
- **变体全部为正，但都不显著。** 30 日对 180 日、90 日对 365 日、14 日对 365 日、换成交易笔数，依次是 +7.2%、+16.0%、+9.7%、+4.6%，t 最高 1.80。
- **钱比一直持有少，回撤一样大。** 规则把 1 变成 8,993，一直持有是 16,253；最大回撤 −84.5% 对 −84.5%。

```bash
git clone https://github.com/runningshark/onchain_timing_failureprove
cd onchain_timing_failureprove
py verify.py O3
```

### 52 · 哈希率带

“矿工投降”。规则：哈希率的 30 日均线在 60 日均线之下的时候空仓，其余时间持有。（[档案](https://github.com/runningshark/onchain_timing_failureprove/blob/master/reports/52_O4_hash_ribbons.md)）

- **没有信号。** 择时超额年化 +2.4%（t = 0.37）；训练段 +4.7%（t = 0.63），验证段 −1.3%（t = −0.12）；平移检验 p = 0.359。
- **“投降期”涨得少一些，但不值得躲。** 哈希率 30 日线在 60 日线之下的日子占 16%，这些日子 BTC 平均每天的涨幅折成一年是 +42.1%，其余日子 +107.0%。差别不显著；规则把 1 变成 8,870，一直持有是 16,253，最大回撤一样大（−84.4% 对 −84.5%）。
- **变体有正有负。** 30 日对 90 日 −2.6%，60 日对 120 日 −6.5%，20 日对 60 日 +4.2%，加上原文的价格确认 +8.3%（t = 1.11）。
- **当成买点看（原文的本意；登记之外，只是描述）。** 2012 年以来 30 日线收复 60 日线一共 38 次，之后 90 天涨幅的中位数是 +5%、上涨的占 60%，和任意一天买入（+10%、60%）没有差别。再加上价格确认后是 26 次，之后 90 天的中位数 +22%、上涨的占 79%（能算的 24 次），比任意一天高，也比只看价格均线金叉（+10%、59%）高。拉长到 180 天和 365 天差别就小了（+43% 对 +36%，+106% 对 +92%）。这些数字没有做显著性检验，窗口之间互相重叠，不能当成结论。
- 剩下的线索：“收复并且价格确认”之后 90 天的涨幅比平时高（中位数 +22% 对 +10%），这是事后看到的描述，能算的只有 24 次。要当成候选，需要另外登记成一条完整的规则（买入后持有多久、什么时候卖）。

```bash
git clone https://github.com/runningshark/onchain_timing_failureprove
cd onchain_timing_failureprove
py verify.py O4
```

### 53 · Puell 倍数择时

“Puell 倍数高于 4 是顶，低于 0.5 是底”。Puell 倍数是每天新发行的币的美元价值除以它过去一年的均值。规则：高于 4 清仓，跌回 0.5 以下再买回来。（[档案](https://github.com/runningshark/onchain_timing_failureprove/blob/master/reports/53_O5_puell_multiple.md)）

- **没过门槛。** 择时超额年化 +20.2%（t = 1.88）；训练段 +38.5%（t = 2.35）。
- **2020 年以后一次都没动。** Puell 倍数最后一次高于 4 是 2018-01-06。每轮牛市的最高值：2013 年 10.49，2017 年 6.62，2021 年 3.46，2024 年 2.43，2025 年 1.59，一轮比一轮低，固定的 4 够不着了。验证段规则全程满仓，和一直持有完全一样，择时超额是 0。
- **全部结论来自 2 次离场。** 2013-03 离场（71 美元）→ 2014-10 回场（354 美元）；2017-11 离场（9,932 美元）→ 2018-11 回场（4,318 美元）。一次回场价比离场价高，一次低。平移检验 p = 0.002，但两次交易撑不起任何结论。
- **钱比一直持有少。** 规则把 1 变成 7,452，一直持有是 16,253；最大回撤 −76.7% 对 −84.5%。和 MVRV 那一条一样，超额来自空仓的那段时间波动特别大（112.7%，持有期间 66.1%），不是那段时间跌了（空仓期间 BTC 平均每天的涨幅折成一年是 +95.5%）。
- **变体。** 顶部线 3、顶部线 5、底部线 0.6、底部线 0.4，依次是 +16.3%、+23.1%、+16.1%、+26.6%，t 最高 2.42。

```bash
git clone https://github.com/runningshark/onchain_timing_failureprove
cd onchain_timing_failureprove
py verify.py O5
```

---

## 入库规则

1. **必须有代码和数据。** 只贴结论的文章不收。
2. **必须做样本外 / 扣成本。** 全区间最优参数的回测不叫证据。
3. **必须给复现命令。** 别人 clone 下来跑不通的，视为没做过。
4. **不删原始档案。** 失败也要保留原始参数和输出，方便日后确认"不是当时手滑"。
5. **不美化。** 亏就是亏，回撤 86% 就写 86%。

## 判定标准

一条策略被记成"失败"，满足任一即可：

- 样本外收益为负，或扣掉手续费/滑点/资金费后不显著；
- 收益来自单边 beta / 杠杆暴露，而不是信号本身；
- 参数稍一扰动就翻负（过拟合）；
- 默认参数下根本没有交易（逻辑写死或阈值不可达）；
- 加到现成策略上的指标或过滤条件，和"不加"的同一策略对照后没有改善（记为"指标无效"，例如 09、11）；
- 没有亏损，但收益已衰减到不值得占用资金和承担尾部风险（记为"收益衰减"，例如 10）；
- 作为基准有参考价值、但风险控制还不能直接实盘的规则（记为"基准·待改进"，例如 12）。

## 为什么公开

因为失败样本比成功样本稀有。成功案例永远有幸存者偏差，而"这条路我走过，是死的"至少能省掉别人的三个月。

## 相关

- [crypto-quant-dashboard](https://github.com/runningshark/crypto-quant-dashboard) —— 在跑的数据看板（只读，不下单）
- 条目模板：[_template.md](_template.md)
