# 量化失败合集 / Quant Failure Archive

做过、跑过、最后没赚到钱的策略，在这里留一份可复现的档案。

不写"经验总结"，只写能重跑的数字：原始声称是什么、用什么数据复核、扣完成本和样本外之后还剩多少。每一条都是**独立仓库**，代码、数据、验证脚本齐全，clone 下来就能自己跑一遍看我有没有骗人。（14–24、25–29、31–34、35–37、38–40、41–45、46–48、49–53、54–59、60–65、66–71、72–77、78–83、84–95、96–98、99–103、104–109、110–113、114–117、118–119 各来自一次事先登记的研究，每次研究共用一个仓库。）

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
| 54 | 1 小时 · 扫前低（前高）后收回 | **确认失败**（比随手进场还差） | 每笔净 R **−0.315**（其中成本 0.253R），t −18.53；比随手进场差 0.054R（t −3.58） | [h1_price_action_failureprove · P1](https://github.com/runningshark/h1_price_action_failureprove/blob/master/reports/54_P1_liquidity_sweep.md) |
| 55 | 1 小时 · 前低下方挂单接针 | **确认失败**（比随手进场还差） | 每笔净 R **−0.174**，t −12.38；比随手进场差 0.065R（t −4.65）；“K 线里先算止盈”时随手挂单也赚钱 | [h1_price_action_failureprove · P2](https://github.com/runningshark/h1_price_action_failureprove/blob/master/reports/55_P2_limit_below_swing_low.md) |
| 56 | 1 小时 · FVG（失衡缺口）回踩 | **确认失败**（和随手进场一样） | 每笔净 R **−0.068**，t −4.11；和随手进场比 +0.004R（t 0.26） | [h1_price_action_failureprove · P3](https://github.com/runningshark/h1_price_action_failureprove/blob/master/reports/56_P3_fair_value_gap.md) |
| 57 | 1 小时 · 订单块回踩 | **确认失败**（比随手进场还差） | 每笔净 R **−0.162**，t −10.40；比随手进场差 0.042R（t −2.70）；“K 线里先算止盈”时随手挂单也赚钱 | [h1_price_action_failureprove · P4](https://github.com/runningshark/h1_price_action_failureprove/blob/master/reports/57_P4_order_block.md) |
| 58 | 1 小时 · 锤子线、射击之星 | **确认失败**（比随手进场还差） | 每笔净 R **−0.217**，t −10.51；比随手进场差 0.070R（t −3.49） | [h1_price_action_failureprove · P5](https://github.com/runningshark/h1_price_action_failureprove/blob/master/reports/58_P5_pin_bar.md) |
| 59 | 1 小时 · 吞没形态 | **确认失败**（和随手进场一样） | 每笔净 R **−0.100**，t −4.99；和随手进场比 +0.021R（t 1.08） | [h1_price_action_failureprove · P6](https://github.com/runningshark/h1_price_action_failureprove/blob/master/reports/59_P6_engulfing.md) |
| 60 | 1 小时 · 斐波那契 0.618 回撤挂单 | **确认失败**（和随手进场一样） | 每笔净 R **−0.143**，t −7.76；和随手挂单比 +0.002R（t 0.11）；“K 线里先算止盈”时随手挂单也赚钱 | [h1_levels_divergence_failureprove · F1](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/reports/60_F1_fibonacci_618.md) |
| 61 | 1 小时 · 整数关口挂单 | **确认失败**（比随手进场还差） | 每笔净 R **−0.111**，t −16.67；比随手挂单差 0.024R（t −3.89），每一年都差 | [h1_levels_divergence_failureprove · F2](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/reports/61_F2_round_numbers.md) |
| 62 | 1 小时 · 枢轴点 S1、R1 挂单 | **确认失败**（和随手进场一样） | 每笔净 R **−0.127**，t −9.16；和随手挂单比 +0.002R（t 0.17）；“K 线里先算止盈”时 t 12.14，但随手挂单赚得更多 | [h1_levels_divergence_failureprove · F3](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/reports/62_F3_pivot_points.md) |
| 63 | 1 小时 · VWAP 回踩 | **确认失败**（2024 年起不比随手进场好） | 每笔净 R **−0.078**，t −6.07；比随手挂单好 +0.025R（t 2.08），2024 年起没有了 | [h1_levels_divergence_failureprove · F4](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/reports/63_F4_vwap_pullback.md) |
| 64 | 1 小时 · RSI 背离 | **确认失败**（好一点但不显著，付不起成本） | 每笔净 R **−0.102**，t −5.06；比随手进场好 +0.033R（t 1.70），成本是它的 4 倍 | [h1_levels_divergence_failureprove · F5](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/reports/64_F5_rsi_divergence.md) |
| 65 | 1 小时 · MACD 背离 | **确认失败**（好一点但不显著，付不起成本） | 每笔净 R **−0.121**，t −5.14；比随手进场好 +0.029R（t 1.26），成本是它的 5 倍 | [h1_levels_divergence_failureprove · F6](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/reports/65_F6_macd_divergence.md) |
| 66 | 1 小时 · 双底、双顶 | **确认失败**（和随手进场一样） | 每笔净 R **−0.097**，t −3.38；和随手进场比 −0.021R（t −0.73） | [h1_patterns_chan_failureprove · G1](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/reports/66_G1_double_top_bottom.md) |
| 67 | 1 小时 · 头肩底、头肩顶 | **确认失败**（好一点但不显著，样本少） | 每笔净 R **−0.058**，t −1.18；比随手进场好 +0.058R（t 1.16），只有 981 笔 | [h1_patterns_chan_failureprove · G2](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/reports/67_G2_head_and_shoulders.md) |
| 68 | 1 小时 · 收敛三角形突破 | **确认失败**（和随手进场一样） | 每笔净 R **−0.081**，t −3.54；和随手进场比 +0.021R（t 0.94） | [h1_patterns_chan_failureprove · G3](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/reports/68_G3_triangle_breakout.md) |
| 69 | 1 小时 · 缠论一买、一卖（笔的背驰） | **确认失败**（和随手进场一样） | 每笔净 R **−0.150**，t −7.08；和随手进场比 −0.004R（t −0.17）；每笔成本 0.151R | [h1_patterns_chan_failureprove · C1](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/reports/69_C1_chan_buy1.md) |
| 70 | 1 小时 · 缠论二买、二卖 | **确认失败**（和随手进场一样） | 每笔净 R **−0.193**，t −7.59；和随手进场比 +0.022R（t 0.90）；每笔成本 0.203R | [h1_patterns_chan_failureprove · C2](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/reports/70_C2_chan_buy2.md) |
| 71 | 1 小时 · 缠论三买、三卖 | **确认失败**（和随手进场一样） | 每笔净 R **−0.190**，t −8.06；和随手进场比 +0.001R（t 0.06）；每笔成本 0.193R | [h1_patterns_chan_failureprove · C3](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/reports/71_C3_chan_buy3.md) |
| 72 | 1 小时 · 网格（合约中性网格） | **确认失败**（单边行情里大亏） | 年化 **−74.7%**，t −2.60；打乱顺序也亏（−58.1%）；涨超过 50% 的季度平均 −103% | [h1_position_mgmt_failureprove · E1](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/reports/72_E1_grid_neutral.md) |
| 73 | 1 小时 · 马丁格尔（摊平加仓） | **确认失败**（赚的是上涨，不是摊平） | 年化 **+15.0%**，t 1.09；打乱以后 +18.9%（更高）；每轮止盈 99.3%，但 84% 的机器人季度末亏着平仓 | [h1_position_mgmt_failureprove · E2](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/reports/73_E2_martingale_dca.md) |
| 74 | 1 小时 · 随机进场加移动止损（Van Tharp） | **确认失败**（有一点趋势，付不起成本） | 每笔净 R **−0.042**，t −2.93；比打乱多 +0.048R（t 3.42），付不起每笔 0.070R 的成本 | [h1_position_mgmt_failureprove · E3](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/reports/74_E3_random_entry_trailing_stop.md) |
| 75 | 1 小时 · 保本止损 | **确认失败**（没有改进） | 改进 **−0.004**R，t −1.20；胜率 34% → 30% | [h1_position_mgmt_failureprove · E4](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/reports/75_E4_breakeven_stop.md) |
| 76 | 1 小时 · 分批止盈 | **确认失败**（胜率变高，赚的一样） | 改进 **−0.001**R，t −0.13；胜率 34% → 50%，赚的一样 | [h1_position_mgmt_failureprove · E5](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/reports/76_E5_partial_take_profit.md) |
| 77 | 1 小时 · 浮盈加仓 | **确认失败**（多赚的被成本吃光） | 改进 **−0.001**R，t −0.02；不扣成本多 +0.147R（t 3.18），被成本吃光 | [h1_position_mgmt_failureprove · E6](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/reports/77_E6_pyramiding.md) |
| 78 | 日线 · 负资金费做多 | **确认失败**（2024 年起没有了） | 每笔净 **+0.79%**，t 1.70；超出随手进场 +1.12%（t 2.45），验证段只有 +0.20% | [d1_funding_rotation_factors_failureprove · H1](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/reports/78_H1_negative_funding_long.md) |
| 79 | 日线 · 升水过高做空 | **确认失败**（牛市里做空，还是亏） | 每笔净 **−0.87%**，t −0.73；随手做空更亏（−1.75%）；拿掉 LUNA 那一笔是 −1.13% | [d1_funding_rotation_factors_failureprove · H2](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/reports/79_H2_high_basis_short.md) |
| 80 | 1 小时 · BTC 领涨、山寨补涨 | **确认失败**（落后的不补涨） | 每笔净 **−0.31%**，t −1.58；超出随手进场 −0.27%（t −1.35），落后的没有补涨 | [d1_funding_rotation_factors_failureprove · H3](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/reports/80_H3_btc_lead_alt_catchup.md) |
| 81 | 日线 · BTC 强势之后换山寨 | **确认失败**（没有规律） | 每笔净 **+0.05%**，t 0.07；做多篮子 +1.60%，反过来 −1.36% | [d1_funding_rotation_factors_failureprove · H4](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/reports/81_H4_btc_alt_rotation.md) |
| 82 | 周度 · 低贝塔（Betting Against Beta） | **确认失败**（主要是拿着 BTC） | 年化 **+20.8%**，t 1.74；平均净多头 40%，对市场和 BTC 回归后截距 +8.4%（t 0.82） | [d1_funding_rotation_factors_failureprove · H5](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/reports/82_H5_low_beta_bab.md) |
| 83 | 周度 · 偏度（彩票效应） | **确认失败**（做空彩票币亏钱） | 年化 **−15.2%**，t −1.20；超出随手选币 −6.8%（t −0.55） | [d1_funding_rotation_factors_failureprove · H6](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/reports/83_H6_skewness_lottery.md) |
| 84 | 周度 · 主动买入占比（订单流） | **确认失败**（2024 年起变弱） | 年化 **+21.8%**，t 1.88；验证段 +6.8%（t 0.43） | [orderflow_ml_macro_failureprove · OF1](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/84_OF1_taker_share_weekly.md) |
| 85 | 日线 · 主动买入占比的极端日 | **确认失败**（扣成本后是 0） | 每笔净 **+0.01%**，t 0.05；超出随手进场 +0.67% 是因为随手进场亏（−0.45%） | [orderflow_ml_macro_failureprove · OF2](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/85_OF2_taker_share_extreme.md) |
| 86 | 日线 · 大单日跟随 | **确认失败**（和随手进场差不多） | 每笔净 **+0.48%**，t 1.05；超出随手进场 +0.13%（t 0.31） | [orderflow_ml_macro_failureprove · OF3](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/86_OF3_big_trade_days.md) |
| 87 | 周度 · 岭回归选币（机器学习） | **确认失败**（排名有用，组合不显著） | 年化 **+17.0%**，t 1.32；排名相关 0.132（t 5.27），多空 3 个币被几周大亏拖住 | [orderflow_ml_macro_failureprove · ML1](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/87_ML1_ridge_weekly.md) |
| 88 | 周度 · 梯度提升树选币（机器学习） | **确认失败**（扣成本后接近 0） | 年化 **+2.3%**，t 0.18；排名相关 0.126（t 5.33） | [orderflow_ml_macro_failureprove · ML2](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/88_ML2_gbm_weekly.md) |
| 89 | 日线 · BTC 隐含波动率飙升后做多 | **确认失败**（样本太小，验证段为负） | 32 笔每笔 **+1.05%**，t 0.97；验证段 −0.97% | [orderflow_ml_macro_failureprove · V1](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/89_V1_bvol_spike_long.md) |
| 90 | 择时 · 波动率风险溢价为正时持有 BTC | **确认失败**（没有择时超额） | 择时超额 **+1.4%**，t 0.18；平移检验 p 0.39 | [orderflow_ml_macro_failureprove · V2](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/90_V2_vrp_timing.md) |
| 91 | 择时 · 实际利率下降时持有 BTC | **确认失败**（没有择时超额） | 择时超额 **+1.3%**，t 0.12；1 → 4.25（持有 16.42） | [orderflow_ml_macro_failureprove · M1](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/91_M1_real_yield_timing.md) |
| 92 | 择时 · 美元走弱时持有 BTC | **确认失败**（没有择时超额） | 择时超额 **+5.2%**，t 0.46；1 → 6.41（持有 16.42） | [orderflow_ml_macro_failureprove · M2](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/92_M2_dollar_timing.md) |
| 93 | 1 小时 · FOMC 公布前 24 小时做多 BTC | **确认失败**（只来自 2020 年） | 每笔净 **+0.49%**，t 1.31；去掉 2020 年 +0.06%；和第 39 条是同一个说法 | [orderflow_ml_macro_failureprove · M3](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/93_M3_pre_fomc_drift.md) |
| 94 | 择时 · 恐惧贪婪指数 | **确认失败**（卖早了，跑输持有） | 择时超额 **−17.1%**，t −1.84；1 → 0.94（持有 7.54） | [orderflow_ml_macro_failureprove · S1](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/94_S1_fear_greed_timing.md) |
| 95 | 日线 · BTC 市占率趋势 | **确认失败**（顺着市占率做是亏的） | 每笔净 **−0.50%**，t −0.81；做多 BTC 那边 −1.30% | [orderflow_ml_macro_failureprove · D1](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/95_D1_btc_dominance_trend.md) |
| 96 | 择时 · 梅耶倍数（BTC） | **确认失败**（卖早了、买贵了） | 择时超额 **+13.4%**，t 1.19；验证段 +0.8%；1 → 863（持有 5,656） | [d1_btc_cycle_seasonality_failureprove · P1](https://github.com/runningshark/d1_btc_cycle_seasonality_failureprove/blob/master/reports/96_P1_mayer_multiple.md) |
| 97 | 择时 · 两年均线乘数（BTC） | **确认失败**（2021 年没碰到线） | 择时超额 **+12.8%**，t 1.12；2018 年以后一直满仓 | [d1_btc_cycle_seasonality_failureprove · P3](https://github.com/runningshark/d1_btc_cycle_seasonality_failureprove/blob/master/reports/97_P3_two_year_ma_multiplier.md) |
| 98 | 择时 · 五月卖出（Sell in May，BTC） | **确认失败**（没有择时超额） | 择时超额 **−0.2%**，t −0.02；平移检验 p 0.37 | [d1_btc_cycle_seasonality_failureprove · S1](https://github.com/runningshark/d1_btc_cycle_seasonality_failureprove/blob/master/reports/98_S1_sell_in_may.md) |
| 99 | 周度 · 52 周高点 | **确认失败**（这一轮最接近，但 t 不到 2） | 年化 **+22.4%**，t 1.86；超出随手选币 +30.8%（t 2.47），训练段 t 0.74 | [resid_mom_usdt_failureprove · X1](https://github.com/runningshark/resid_mom_usdt_failureprove/blob/master/reports/99_X1_52w_high_weekly.md) |
| 100 | 周度 · 残差动量（去掉大盘） | **确认失败**（扣成本后接近 0） | 年化 **+1.5%**，t 0.12；验证段 −3.4% | [resid_mom_usdt_failureprove · X2](https://github.com/runningshark/resid_mom_usdt_failureprove/blob/master/reports/100_X2_residual_momentum_weekly.md) |
| 101 | 周度 · 残差短期反转（去掉大盘） | **确认失败**（方向反了，反过来也付不起成本） | 年化 **−15.6%**，t −1.26；反过来也付不起成本 | [resid_mom_usdt_failureprove · X3](https://github.com/runningshark/resid_mom_usdt_failureprove/blob/master/reports/101_X3_residual_reversal_weekly.md) |
| 102 | 日线 · USDT 增发后做多 BTC | **确认失败**（只是赶上了牛市） | 每笔净 **+1.79%**，t 2.39；超出随手进场 +0.62%（t 0.87） | [resid_mom_usdt_failureprove · E1](https://github.com/runningshark/resid_mom_usdt_failureprove/blob/master/reports/102_E1_usdt_mint_long_btc.md) |
| 103 | 日线 · 现货带动还是合约带动的大涨 | **确认失败**（两种大涨之后没有区别） | 每笔净 **+0.03%**，t 0.11；现货带动做多 +0.66%，合约带动做空 −0.68% | [resid_mom_usdt_failureprove · E2](https://github.com/runningshark/resid_mom_usdt_failureprove/blob/master/reports/103_E2_spot_vs_perp_led_pumps.md) |
| 104 | 日线 · 广度推力后做多 BTC | **确认失败**（不如随手挑一天买） | 每笔净 **+2.04%**，t 0.63；随手进场 +3.08% | [m2_orderbook_cny_failureprove · B1](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/reports/104_B1_breadth_thrust_long_btc.md) |
| 105 | 择时 · 美国 M2 增长时持有 BTC（滞后 70 天） | **确认失败**（错过了 2023 年的上涨） | 择时超额 **−2.9%**，t −0.64；1 → 2,559（持有 5,656） | [m2_orderbook_cny_failureprove · M4](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/reports/105_M4_us_m2_lag_timing.md) |
| 106 | 择时 · 订单簿买盘厚时持有 BTC | **确认失败**（没有预测力，换仓太多） | 择时超额 **−12.5%**，t −1.13；不扣成本 +2.8% | [m2_orderbook_cny_failureprove · OB1](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/reports/106_OB1_orderbook_bid_heavy_timing.md) |
| 107 | 日线 · 订单簿极端失衡跟着做 | **确认失败**（扣成本后接近 0） | 每笔净 **+0.15%**，t 0.38；超出随手进场 +0.23% | [m2_orderbook_cny_failureprove · OB2](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/reports/107_OB2_orderbook_extreme_imbalance.md) |
| 108 | 1 小时 · 资金费高时结算前做空 | **确认失败**（结算前后价格反而在涨） | 每笔净 **−0.30%**，t −3.17；结算后 1 小时反而涨 0.159% | [m2_orderbook_cny_failureprove · FS1](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/reports/108_FS1_short_before_funding.md) |
| 109 | 择时 · 春节前两周空仓（BTC） | **确认失败**（春节前多数年份在涨） | 择时超额 **−5.4%**，t −1.31；春节前 14 天 14 年里涨了 9 年 | [m2_orderbook_cny_failureprove · CNY](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/reports/109_CNY_flat_before_chinese_new_year.md) |
| 110 | 择时 · 美联储净流动性增加时持有 BTC | **确认失败**（不显著，换个算法就变负） | 择时超额 **+12.7%**，t 1.21；1 → 1,462（持有 5,656） | [fed_fees_stables_failureprove · NL1](https://github.com/runningshark/fed_fees_stables_failureprove/blob/master/reports/110_NL1_fed_net_liquidity_timing.md) |
| 111 | 日线 · 链上手续费创一年新高就做空 | **确认失败**（做空亏钱，笔数太少） | 每笔净 **−2.30%**，t −0.55；17 笔 | [fed_fees_stables_failureprove · FE](https://github.com/runningshark/fed_fees_stables_failureprove/blob/master/reports/111_FE_fee_spike_short.md) |
| 112 | 择时 · USDT 市占率低于 50 天平均时持有 BTC | **确认失败**（其实是 BTC 的均线，验证段变弱） | 择时超额 **+19.1%**，t 1.66；验证段 +4.2%，和 BTC 50 天均线 86% 相同 | [fed_fees_stables_failureprove · UD1](https://github.com/runningshark/fed_fees_stables_failureprove/blob/master/reports/112_UD1_usdt_dominance_timing.md) |
| 113 | 择时 · 稳定币供给比率低时持有 BTC | **确认失败**（低的时候买反而跑输） | 择时超额 **−12.7%**，t −1.13；1 → 1.51（持有 7.27） | [fed_fees_stables_failureprove · SSR1](https://github.com/runningshark/fed_fees_stables_failureprove/blob/master/reports/113_SSR1_stablecoin_supply_ratio_timing.md) |
| 114 | 日线 · 持仓量骤降后做多 BTC、ETH | **确认失败**（和随手进场差不多） | 每笔净 **+1.18%**，t 1.08；超出随手进场 +0.37%（t 0.34） | [oi_moon_calendar_failureprove · OI1](https://github.com/runningshark/oi_moon_calendar_failureprove/blob/master/reports/114_OI1_oi_flush_long.md) |
| 115 | 日历 · 新月前后持有 BTC | **确认失败**（新月满月没有差别） | 择时超额 **−1.1%**，t −0.10；随机相位 p = 0.43 | [oi_moon_calendar_failureprove · MOON1](https://github.com/runningshark/oi_moon_calendar_failureprove/blob/master/reports/115_MOON1_lunar_new_moon_timing.md) |
| 116 | 日历 · 只在周一持有 BTC | **确认失败**（不扣成本还在，付不起成本） | 择时超额 **+6.2%**，t 0.89；不扣成本 +16.6%（t 2.39） | [oi_moon_calendar_failureprove · DOW1](https://github.com/runningshark/oi_moon_calendar_failureprove/blob/master/reports/116_DOW1_monday_effect_timing.md) |
| 117 | 日历 · 月末到月初持有 BTC | **确认失败**（2020 年以后没有了） | 择时超额 **+7.0%**，t 1.04；验证段 −2.3% | [oi_moon_calendar_failureprove · TOM1](https://github.com/runningshark/oi_moon_calendar_failureprove/blob/master/reports/117_TOM1_turn_of_month_timing.md) |
| 118 | 日线 · 技术指标规则大全第二批（145 条，BTC） | **确认失败**（最好的一条和运气分不出来） | 最大 t 2.93，校正“试了 145 条”后 p **0.087**；训练段最好的规则验证段 t **−0.09** | [d1_indicator_zoo2_failureprove · A](https://github.com/runningshark/d1_indicator_zoo2_failureprove/blob/master/reports/118_A_btc_indicator_zoo2.md) |
| 119 | 日线 · 技术指标规则大全第二批（145 条，每季度 10 个币） | **确认失败**（145 条里只有 1 条 t > 2） | 最大 t 2.58，校正后 p **0.166**；145 条里 t > 2 的只有 1 条 | [d1_indicator_zoo2_failureprove · B](https://github.com/runningshark/d1_indicator_zoo2_failureprove/blob/master/reports/119_B_alt10_indicator_zoo2.md) |

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

### 54–59 · 第十轮事先登记的研究：价格行为——SMC 和 K 线形态（共用一个仓库）

测“在哪里开单”的几种说法：SMC 的扫流动性、FVG、订单块，挂单接针，锤子线和吞没。规则和通过标准同样是事先登记的（[事先登记_第十轮.md](https://github.com/runningshark/h1_price_action_failureprove/blob/master/事先登记_第十轮.md)）。**登记 6 个，6 个失败**。

- 累计 51 个候选，门槛是 t ≥ 3.3。币安 U 本位永续的 1 小时 K 线，每个季度按成交额选 10 个币（共 48 个合约，含后来下架的），2020-04 到 2026-10，训练段到 2023 年底。止盈 2R，最长持有 48 根；市价单每边 0.10%、限价单每边 0.02%。
- 每笔用 R 计（亏到止损是 −1R）。除了扣成本后的收益，还拿**随手进场**做对照：同一个合约、同一个方向、同样的止损止盈，在前后 30 天里随机进场。两边之差只剩进场位置本身的作用。
- 6 条扣成本后每一年都亏；没有一条比随手进场好，4 条显著更差。顺着 4 小时方向做也没有帮助。
- 这 6 条共用一个仓库 [h1_price_action_failureprove](https://github.com/runningshark/h1_price_action_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/h1_price_action_failureprove/blob/master/FAILURE_REPORT.md)。数据来自 Binance Vision（CC BY-NC-SA 4.0）。

### 54 · 扫前低（前高）后收回

“价格刺破前低、扫掉止损之后收回，就是反转”（SMC 的流动性扫荡，更早的版本是 Turtle Soup）。规则：4 小时方向看多时，前低被刺破、那根 K 线又收回前低之上，下一根开盘做多，止损在刺破的最低点外面；做空对称。（[档案](https://github.com/runningshark/h1_price_action_failureprove/blob/master/reports/54_P1_liquidity_sweep.md)）

- **扣成本后每笔亏 0.315R。** 12,667 笔（每年约 1,922 笔），胜率 32%，扣成本后平均赚 1.79R、平均亏 1.29R。不扣成本每笔 −0.060R，手续费加滑点每笔 0.253R，资金费每笔付出 0.002R。组合 t = −18.53，每年合计 −606R，最大回撤 4,000R。
- **比随手进场还差。** 同样的方向、同样的止损止盈，在前后 30 天里随手进场，每笔毛 R 是 −0.006；按规则进场是 −0.060，差 0.054R（t = −3.58）。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.290R（t = −12.54），验证段（2024 年起）每笔 −0.348R（t = −14.12）；超出随手进场的部分，训练段 −0.045R，验证段 −0.065R。
- **邻近变体、压力测试全是负的。** 摆动点左右各 2 根 −0.299R，摆动点左右各 6 根 −0.298R，不看 4 小时方向 −0.282R，止盈 3R −0.308R；成本翻倍 −0.568R，晚一根 K 线 −0.269R。不扣成本也是亏的：每笔 −0.062R（t = −4.21）。
- **止损太紧，成本吃掉一大块。** 止损放在刺破那根 K 线的最低点外面，中位数只有价格的 0.86%（0.71 个 ATR）；BTC 上只有 0.57%，每笔光成本就是 0.373R。同样 0.1% 的手续费，止损越紧，在 R 里占得越多。
- **顺着 4 小时方向做没有帮助。** 去掉 4 小时方向的变体每笔 −0.282R，比主规则（−0.315R）亏得少；对照只从 4 小时方向相同的时刻里抽，按规则进场仍然差 0.043R（t = −2.81）。

```bash
git clone https://github.com/runningshark/h1_price_action_failureprove
cd h1_price_action_failureprove
py verify.py P1
```

### 55 · 前低下方挂单接针

“在前低下方挂单，等插针成交”。规则：4 小时方向看多时，在还没被扫过的前低下方 0.2 个 ATR 挂买单，止损 1 个 ATR、止盈 2 个 ATR；做空对称。（[档案](https://github.com/runningshark/h1_price_action_failureprove/blob/master/reports/55_P2_limit_below_swing_low.md)）

- **扣成本后每笔亏 0.174R。** 16,798 笔（每年约 2,549 笔），胜率 31%，扣成本后平均赚 1.95R、平均亏 1.13R。不扣成本每笔 −0.069R，手续费加滑点每笔 0.104R，资金费每笔付出 0.001R。组合 t = −12.38，每年合计 −444R，最大回撤 2,925R。
- **比随手进场还差。** 同样的方向、同样的止损止盈，在前后 30 天里随手进场，每笔毛 R 是 −0.003；按规则进场是 −0.069，差 0.065R（t = −4.65）。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.176R（t = −9.83），验证段（2024 年起）每笔 −0.171R（t = −7.62）；超出随手进场的部分，训练段 −0.080R，验证段 −0.045R。
- **邻近变体、压力测试全是负的。** 挂在前低下方 0.1 个 ATR −0.196R，挂在前低下方 0.5 个 ATR −0.147R，不看 4 小时方向 −0.152R，止损 1.5 个 ATR −0.118R；成本翻倍 −0.278R，晚一根 K 线 −0.175R。不扣成本也是亏的：每笔 −0.070R（t = −5.18）。
- **“先成交、再到止盈”的算法会把随手挂的单也算成赚钱（登记之外的诊断）。** 如果同一根 K 线里先算止盈，这一条扣成本后每笔变成 +0.039R；但随手挂的单在同样的算法下每笔毛 R 是 +0.187，比按规则挂单（+0.136）还高。成交的那一根里有 5.5% 的开盘价已经越过止盈：价格先到了止盈、后来才跌到挂单价，这样算出来的“赚钱”在现实里不可能。1 小时 K 线分不出 K 线里的先后，所以登记时选了保守的算法。
- **顺着 4 小时方向做没有帮助。** 去掉 4 小时方向的变体每笔 −0.152R，比主规则（−0.174R）亏得少；对照只从 4 小时方向相同的时刻里抽，按规则进场仍然差 0.048R（t = −3.31）。

```bash
git clone https://github.com/runningshark/h1_price_action_failureprove
cd h1_price_action_failureprove
py verify.py P2
```

### 56 · FVG（失衡缺口）回踩

“价格会回来补 FVG（失衡缺口）”（ICT）。规则：4 小时方向看多时，出现看多的 FVG 就在缺口中点挂买单，止损在第一根 K 线的最低点外面；做空对称。（[档案](https://github.com/runningshark/h1_price_action_failureprove/blob/master/reports/56_P3_fair_value_gap.md)）

- **扣成本后每笔亏 0.068R。** 14,967 笔（每年约 2,271 笔），胜率 35%，扣成本后平均赚 1.85R、平均亏 1.09R。不扣成本每笔 +0.013R，手续费加滑点每笔 0.078R，资金费每笔付出 0.003R。组合 t = −4.11，每年合计 −155R，最大回撤 1,054R。
- **和随手进场没有分别。** 同样的方向、同样的止损止盈，在前后 30 天里随手进场，每笔毛 R 是 +0.009；按规则进场是 +0.013，超出 +0.004R（t = 0.26）。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.066R（t = −3.11），验证段（2024 年起）每笔 −0.072R（t = −2.70）；超出随手进场的部分，训练段 −0.004R，验证段 +0.015R。
- **邻近变体、压力测试全是负的。** 挂在缺口边缘 −0.050R，缺口至少 0.5 个 ATR −0.062R，不看 4 小时方向 −0.054R，止盈 3R −0.062R；成本翻倍 −0.146R，晚一根 K 线 −0.072R。不扣成本每笔 +0.010R（t = 0.61），也不显著。
- **4 小时方向拖了后腿。** 对照只从 4 小时方向相同的时刻里抽，超出变成 +0.033R（t = 1.99，没到门槛）：顺着 4 小时方向随手进场（每笔毛 R −0.020）本身就比不看方向随手进场（+0.009）差，FVG 只是把这一点差距补了回来。去掉 4 小时方向的变体也比主规则亏得少（−0.054R 对 −0.068R）。

```bash
git clone https://github.com/runningshark/h1_price_action_failureprove
cd h1_price_action_failureprove
py verify.py P3
```

### 57 · 订单块回踩

“价格回到订单块会再次被推开”（ICT、SMC）。规则：4 小时方向看多时，收盘突破前高后，在突破前最后一根收跌的 K 线的最高价挂买单，止损在它的最低点外面；做空对称。（[档案](https://github.com/runningshark/h1_price_action_failureprove/blob/master/reports/57_P4_order_block.md)）

- **扣成本后每笔亏 0.162R。** 13,350 笔（每年约 2,026 笔），胜率 32%，扣成本后平均赚 1.94R、平均亏 1.14R。不扣成本每笔 −0.044R，手续费加滑点每笔 0.115R，资金费每笔付出 0.003R。组合 t = −10.40，每年合计 −327R，最大回撤 2,163R。
- **比随手进场还差。** 同样的方向、同样的止损止盈，在前后 30 天里随手进场，每笔毛 R 是 −0.002；按规则进场是 −0.044，差 0.042R（t = −2.70）。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.168R（t = −7.92），验证段（2024 年起）每笔 −0.153R（t = −6.76）；超出随手进场的部分，训练段 −0.064R，验证段 −0.012R。
- **邻近变体、压力测试全是负的。** 挂在订单块中点 −0.238R，只在前 10 根里找 −0.162R，不看 4 小时方向 −0.140R，止盈 3R −0.167R；成本翻倍 −0.277R，晚一根 K 线 −0.162R。不扣成本也是亏的：每笔 −0.047R（t = −3.13）。
- **“先成交、再到止盈”的算法会把随手挂的单也算成赚钱（登记之外的诊断）。** 如果同一根 K 线里先算止盈，这一条扣成本后每笔变成 +0.117R；但随手挂的单在同样的算法下每笔毛 R 是 +0.246，比按规则挂单（+0.222）还高。成交的那一根里有 7.1% 的开盘价已经越过止盈：价格先到了止盈、后来才跌到挂单价，这样算出来的“赚钱”在现实里不可能。1 小时 K 线分不出 K 线里的先后，所以登记时选了保守的算法。
- **顺着 4 小时方向做没有帮助。** 去掉 4 小时方向的变体每笔 −0.140R，比主规则（−0.162R）亏得少；对照只从 4 小时方向相同的时刻里抽，按规则进场仍然差 0.024R（t = −1.58）。

```bash
git clone https://github.com/runningshark/h1_price_action_failureprove
cd h1_price_action_failureprove
py verify.py P4
```

### 58 · 锤子线、射击之星

“低点出现锤子线是反转信号”。规则：最近 20 根的最低处出现锤子线（下影线至少 60%、实体最多 30%）就做多，止损在锤子线最低点外面；射击之星对称做空。（[档案](https://github.com/runningshark/h1_price_action_failureprove/blob/master/reports/58_P5_pin_bar.md)）

- **扣成本后每笔亏 0.217R。** 10,281 笔（每年约 1,560 笔），胜率 32%，扣成本后平均赚 1.77R、平均亏 1.15R。不扣成本每笔 −0.072R，手续费加滑点每笔 0.145R，资金费每笔付出 0.001R。组合 t = −10.51，每年合计 −339R，最大回撤 2,279R。
- **比随手进场还差。** 同样的方向、同样的止损止盈，在前后 30 天里随手进场，每笔毛 R 是 −0.002；按规则进场是 −0.072，差 0.070R（t = −3.49）。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.199R（t = −7.55），验证段（2024 年起）每笔 −0.241R（t = −7.36）；超出随手进场的部分，训练段 −0.064R，验证段 −0.078R。
- **邻近变体、压力测试全是负的。** 最近 10 根 −0.229R，最近 50 根 −0.198R，只做 4 小时方向那一边 −0.248R，止盈 3R −0.222R；成本翻倍 −0.362R，晚一根 K 线 −0.236R。不扣成本也是亏的：每笔 −0.072R（t = −3.66）。
- **多空都亏，加上 4 小时方向更差。** 做多 5,702 笔，每笔 −0.256R；做空 4,579 笔，每笔 −0.169R。只做 4 小时方向那一边：每笔 −0.248R，比主规则（−0.217R）还差。

```bash
git clone https://github.com/runningshark/h1_price_action_failureprove
cd h1_price_action_failureprove
py verify.py P5
```

### 59 · 吞没形态

“低点出现看多吞没是反转信号”。规则：最近 20 根的最低处出现看多吞没（实体至少 0.5 个 ATR）就做多，止损在两根的最低点外面；看空吞没对称。（[档案](https://github.com/runningshark/h1_price_action_failureprove/blob/master/reports/59_P6_engulfing.md)）

- **扣成本后每笔亏 0.100R。** 7,187 笔（每年约 1,091 笔），胜率 36%，扣成本后平均赚 1.72R、平均亏 1.11R。不扣成本每笔 +0.020R，手续费加滑点每笔 0.123R，资金费每笔收到 0.003R。组合 t = −4.99，每年合计 −109R，最大回撤 726R。
- **和随手进场没有分别。** 同样的方向、同样的止损止盈，在前后 30 天里随手进场，每笔毛 R 是 −0.001；按规则进场是 +0.020，超出 +0.021R（t = 1.08）。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.091R（t = −3.59），验证段（2024 年起）每笔 −0.109R（t = −3.51）；超出随手进场的部分，训练段 +0.012R，验证段 +0.031R。
- **邻近变体、压力测试全是负的。** 最近 10 根 −0.102R，最近 50 根 −0.099R，只做 4 小时方向那一边 −0.108R，止盈 3R −0.101R；成本翻倍 −0.223R，晚一根 K 线 −0.116R。不扣成本每笔 +0.023R（t = 1.20），也不显著。
- **多空都亏，加上 4 小时方向更差。** 做多 3,274 笔，每笔 −0.124R；做空 3,913 笔，每笔 −0.080R。只做 4 小时方向那一边：每笔 −0.108R，比主规则（−0.100R）还差。

```bash
git clone https://github.com/runningshark/h1_price_action_failureprove
cd h1_price_action_failureprove
py verify.py P6
```

### 60–65 · 第十一轮事先登记的研究：支撑阻力和背离（共用一个仓库）

接着第十轮，测另一类“在哪里开单”的说法：斐波那契 0.618、整数关口、枢轴点、VWAP 回踩、RSI 背离、MACD 背离。数据和方法与第十轮相同，规则和通过标准同样是事先登记的（[事先登记_第十一轮.md](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/事先登记_第十一轮.md)）。**登记 6 个，6 个失败**。

- 累计 57 个候选，门槛是 t ≥ 3.4。币安 U 本位永续的 1 小时 K 线，每个季度按成交额选 10 个币（共 48 个合约，含后来下架的），2020-04 到 2026-10，训练段到 2023 年底。止盈 2R，最长持有 48 根；市价单每边 0.10%、限价单每边 0.02%。
- 每笔用 R 计，同时和**随手进场**比（同一个合约、同一个方向、同样的止损止盈，在前后 30 天里随机进场）。
- 6 条扣成本后每一年都亏。整数关口每一年都比随手挂单差；斐波那契、枢轴点和随手挂单一样；VWAP 回踩在 2023 年以前好一点，2024 年起没有了；两种背离好一点但不显著，付不起成本。顺着 4 小时方向做都更差。
- 这 6 条共用一个仓库 [h1_levels_divergence_failureprove](https://github.com/runningshark/h1_levels_divergence_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/FAILURE_REPORT.md)。数据来自 Binance Vision（CC BY-NC-SA 4.0）。

### 60 · 斐波那契 0.618 回撤挂单

“回调到 0.618 是买点”。规则：最近一段上涨至少 3 个 ATR、价格第一次回落到 0.618 回撤位时挂买单，止损在 0.786 外面；下跌对称。（[档案](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/reports/60_F1_fibonacci_618.md)）

- **扣成本后每笔亏 0.143R。** 9,125 笔（每年约 1,385 笔），胜率 33%，扣成本后平均赚 1.96R、平均亏 1.16R。不扣成本每笔 −0.015R，手续费加滑点每笔 0.129R，资金费每笔收到 0.001R。组合 t = −7.76，每年合计 −199R，最大回撤 1,316R。
- **和随手挂单没有分别。** 同样的方向、同样的止损止盈，在前后 30 天里随手挂单，每笔毛 R 是 −0.017；按规则挂单是 −0.015，超出 +0.002R（t = 0.11）。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.130R（t = −5.42），验证段（2024 年起）每笔 −0.163R（t = −5.63）。
- **邻近变体、压力测试全是负的。** 止损放在摆动点外面 −0.090R，挂在 0.5 回撤位 −0.072R，这一段至少 5 个 ATR −0.101R，止盈 3R −0.188R；成本翻倍 −0.272R，晚一根 K 线 −0.158R。手续费、滑点都记 0（资金费照算）也是亏的：每笔 −0.014R（t = −0.84）。
- **乐观的算法会把随手挂的单也算成赚钱。** 如果限价单成交的那一根 K 线里也算止盈，这一条扣成本后每笔变成 +0.060R（t = 3.25）；但随手挂的单在同样的算法下每笔毛 R 是 +0.213，比按规则挂单（+0.180）还高。成交的那一根里，有 3.8% 一开盘就已经越过止盈价：价格先经过止盈、再回落到挂单价成交，乐观的算法照样把它算成止盈。

```bash
git clone https://github.com/runningshark/h1_levels_divergence_failureprove
cd h1_levels_divergence_failureprove
py verify.py F1
```

### 61 · 整数关口挂单

“整数关口有支撑和阻力”。规则：在离收盘价 2 个 ATR 以内的两位有效数字整数（BTC 63,000、64,000 这种）前面 0.1 个 ATR 挂单，止损 1 个 ATR、止盈 2 个 ATR。（[档案](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/reports/61_F2_round_numbers.md)）

- **扣成本后每笔亏 0.111R。** 56,959 笔（每年约 8,645 笔），胜率 32%，扣成本后平均赚 1.97R、平均亏 1.10R。不扣成本每笔 −0.029R，手续费加滑点每笔 0.082R，资金费每笔不到 0.001R。组合 t = −16.67，每年合计 −958R，最大回撤 6,337R。
- **比随手挂单还差，而且每一年都差。** 同样的方向、同样的止损止盈，在前后 30 天里随手挂单，每笔毛 R 是 −0.006；挂在整数关口是 −0.029，差 0.024R（t = −3.89）。分年度看，每一年都差（−0.041R 到 −0.010R）。整数关口更像是价格会穿过去的地方，不是停下来的地方。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.092R（t = −10.73），验证段（2024 年起）每笔 −0.136R（t = −13.58）。
- **邻近变体、压力测试全是负的。** 只用一位有效数字的整数 −0.100R，挂在关口上 −0.113R，挂在关口外 0.3 个 ATR −0.087R，止损 1.5 个 ATR −0.079R；成本翻倍 −0.193R，晚一根 K 线 −0.109R。手续费、滑点都记 0（资金费照算）也是亏的：每笔 −0.029R（t = −4.74）。

```bash
git clone https://github.com/runningshark/h1_levels_divergence_failureprove
cd h1_levels_divergence_failureprove
py verify.py F2
```

### 62 · 枢轴点 S1、R1 挂单

“枢轴点 S1 是支撑、R1 是阻力”。规则：用前一天的高低收算经典枢轴点，在 S1 挂买单、在 R1 挂卖单（挂离价格近的那一边），每个价位一天做一次，止损 1 个 ATR、止盈 2 个 ATR。（[档案](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/reports/62_F3_pivot_points.md)）

- **扣成本后每笔亏 0.127R。** 19,161 笔（每年约 2,908 笔），胜率 32%，扣成本后平均赚 1.97R、平均亏 1.13R。不扣成本每笔 −0.023R，手续费加滑点每笔 0.104R，资金费每笔收到 0.001R。组合 t = −9.16，每年合计 −369R，最大回撤 2,473R。
- **和随手挂单没有分别。** 同样的方向、同样的止损止盈，在前后 30 天里随手挂单，每笔毛 R 是 −0.025；按规则挂单是 −0.023，超出 +0.002R（t = 0.17）。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.132R（t = −7.45），验证段（2024 年起）每笔 −0.121R（t = −5.48）。
- **邻近变体、压力测试全是负的。** 用 S2、R2 −0.131R，用枢轴点 P −0.095R，只做 4 小时方向那一边 −0.161R，止损 1.5 个 ATR −0.085R；成本翻倍 −0.231R，晚一根 K 线 −0.138R。手续费、滑点都记 0（资金费照算）也是亏的：每笔 −0.022R（t = −1.67）。
- **乐观的算法会把随手挂的单也算成赚钱。** 如果限价单成交的那一根 K 线里也算止盈，这一条扣成本后每笔变成 +0.183R（t = 12.14）；但随手挂的单在同样的算法下每笔毛 R 是 +0.298，比按规则挂单（+0.275）还高。成交的那一根里，有 9.7% 一开盘就已经越过止盈价：价格先经过止盈、再回落到挂单价成交，乐观的算法照样把它算成止盈。
- **顺着 4 小时方向做更差。** 只做 4 小时方向那一边：每笔 −0.161R，比主规则（−0.127R）亏得更多。

```bash
git clone https://github.com/runningshark/h1_levels_divergence_failureprove
cd h1_levels_divergence_failureprove
py verify.py F3
```

### 63 · VWAP 回踩

“价格在 VWAP 上方时回踩 VWAP 做多”。规则：当天最近 4 根都收在 VWAP 上方，就在 VWAP 挂买单；都在下方就挂卖单；止损 1 个 ATR、止盈 2 个 ATR。（[档案](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/reports/63_F4_vwap_pullback.md)）

- **扣成本后每笔亏 0.078R。** 33,193 笔（每年约 5,038 笔），胜率 34%，扣成本后平均赚 1.95R、平均亏 1.12R。不扣成本每笔 +0.017R，手续费加滑点每笔 0.095R，资金费每笔不到 0.001R。组合 t = −6.07，每年合计 −395R，最大回撤 2,666R。
- **比随手挂单好的那一点集中在 2023 年以前。** 全部算在一起超出 +0.025R（t = 2.08），没到门槛；训练段超出 +0.047R，验证段 −0.004R。分年度：2020 到 2023 年 +0.033R 到 +0.065R，2024 年 +0.010R，2025 年、2026 年 −0.013R、−0.010R。
- **两段都亏，后一段亏得更多。** 训练段每笔 −0.041R（t = −2.42），验证段每笔 −0.128R（t = −6.76）。
- **邻近变体、压力测试全是负的。** 最近 8 根在同一侧 −0.066R，最近 2 根在同一侧 −0.074R，只做 4 小时方向那一边 −0.088R，止损 1.5 个 ATR −0.054R；成本翻倍 −0.174R，晚一根 K 线 −0.088R。手续费、滑点都记 0（资金费照算），每笔 +0.017R（t = 1.39），也不显著。
- **顺着 4 小时方向做更差。** 只做 4 小时方向那一边：每笔 −0.088R，比主规则（−0.078R）亏得更多。

```bash
git clone https://github.com/runningshark/h1_levels_divergence_failureprove
cd h1_levels_divergence_failureprove
py verify.py F4
```

### 64 · RSI 背离

“价格创新低、RSI 不创新低是反转信号”。规则：相邻两个摆动低点，后一个更低、RSI 更高，就做多，止损在新低外面；高点对称。（[档案](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/reports/64_F5_rsi_divergence.md)）

- **扣成本后每笔亏 0.102R。** 9,064 笔（每年约 1,376 笔），胜率 37%，扣成本后平均赚 1.63R、平均亏 1.11R。不扣成本每笔 +0.028R，手续费加滑点每笔 0.132R，资金费每笔收到 0.002R。组合 t = −5.06，每年合计 −141R，最大回撤 1,009R。
- **比随手进场好一点，但不显著。** 同样的方向、同样的止损止盈，随手进场每笔毛 R 是 −0.005，按背离进场是 +0.028，超出 +0.033R（t = 1.70）；训练段 +0.034R，验证段 +0.033R。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.090R（t = −3.29），验证段（2024 年起）每笔 −0.117R（t = −3.92）。
- **邻近变体、压力测试全是负的。** 前一个低点的 RSI 低于 30 −0.128R，摆动点左右各 5 根 −0.073R，最多相隔 120 根 −0.102R，只做 4 小时方向那一边 −0.163R；成本翻倍 −0.235R，晚一根 K 线 −0.122R。手续费、滑点都记 0（资金费照算），每笔 +0.030R（t = 1.58），也不显著。
- **顺着 4 小时方向做更差。** 只做 4 小时方向那一边：每笔 −0.163R，比主规则（−0.102R）亏得更多。
- **这一点信息付不起成本。** 每笔成本 0.132R，是超出随手进场那部分的 4 倍。

```bash
git clone https://github.com/runningshark/h1_levels_divergence_failureprove
cd h1_levels_divergence_failureprove
py verify.py F5
```

### 65 · MACD 背离

“MACD 背离是反转信号”。规则：相邻两个摆动低点，后一个更低、MACD 线更高（且前一个在 0 下方），就做多，止损在新低外面；高点对称。（[档案](https://github.com/runningshark/h1_levels_divergence_failureprove/blob/master/reports/65_F6_macd_divergence.md)）

- **扣成本后每笔亏 0.121R。** 7,318 笔（每年约 1,111 笔），胜率 36%，扣成本后平均赚 1.64R、平均亏 1.13R。不扣成本每笔 +0.020R，手续费加滑点每笔 0.143R，资金费每笔收到 0.002R。组合 t = −5.14，每年合计 −134R，最大回撤 944R。
- **比随手进场好一点，但不显著。** 同样的方向、同样的止损止盈，随手进场每笔毛 R 是 −0.008，按背离进场是 +0.020，超出 +0.029R（t = 1.26）；训练段 +0.020R，验证段 +0.039R。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.123R（t = −3.90），验证段（2024 年起）每笔 −0.118R（t = −3.35）。
- **邻近变体、压力测试全是负的。** 用 MACD 柱 −0.088R，摆动点左右各 5 根 −0.092R，最多相隔 120 根 −0.121R，只做 4 小时方向那一边 −0.186R；成本翻倍 −0.264R，晚一根 K 线 −0.159R。手续费、滑点都记 0（资金费照算），每笔 +0.022R（t = 0.99），也不显著。
- **顺着 4 小时方向做更差。** 只做 4 小时方向那一边：每笔 −0.186R，比主规则（−0.121R）亏得更多。
- **这一点信息付不起成本。** 每笔成本 0.143R，是超出随手进场那部分的 5 倍。

```bash
git clone https://github.com/runningshark/h1_levels_divergence_failureprove
cd h1_levels_divergence_failureprove
py verify.py F6
```

### 66–71 · 第十二轮事先登记的研究：图形和缠论（共用一个仓库）

“看图开单”这一类的最后一轮：双底双顶、头肩、收敛三角形三种经典图形，和缠论的一买、二买、三买。数据和方法与第十轮、第十一轮相同，规则和通过标准同样是事先登记的（[事先登记_第十二轮.md](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/事先登记_第十二轮.md)）。**登记 6 个，6 个失败**。

- 累计 63 个候选，门槛是 t ≥ 3.4。币安 U 本位永续的 1 小时 K 线，每个季度按成交额选 10 个币（共 48 个合约，含后来下架的），2020-04 到 2026-10，训练段到 2023 年底。信号后下一根开盘市价进场，止盈 2R，最长持有 48 根；市价每边 0.10%、止盈每边 0.02%。
- 每笔用 R 计，同时和**随手进场**比（同一个合约、同一个方向、同样的止损止盈，在前后 30 天里随机进场）。
- 6 条扣成本后全部亏损，按信号进场都和随手进场没有可靠的分别；头肩好一点，但样本少、2024 年起基本没了。缠论三个买卖点的止损紧，每笔成本 0.15 到 0.20R，亏得最多。
- 这 6 条共用一个仓库 [h1_patterns_chan_failureprove](https://github.com/runningshark/h1_patterns_chan_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/FAILURE_REPORT.md)。数据来自 Binance Vision（CC BY-NC-SA 4.0）。

### 66 · 双底、双顶

“双底（W 底）突破颈线做多，双顶（M 头）跌破颈线做空”。规则：两个差不多一样低的摆动低点（相差不超过 0.5 个 ATR），收盘突破两者之间的最高价时做多，止损在底部外面；双顶对称。（[档案](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/reports/66_G1_double_top_bottom.md)）

- **扣成本后每笔亏 0.097R。** 2,527 笔（每年约 384 笔），胜率 37%，扣成本后平均赚 1.49R、平均亏 1.01R。不扣成本每笔 −0.018R，手续费加滑点每笔 0.079R，资金费每笔不到 0.001R。组合 t = −3.38，每年合计 −37R，最大回撤 267R。
- **和随手进场没有分别，验证段还更差。** 同样的方向、同样的止损止盈，在前后 30 天里随手进场，每笔毛 R 是 +0.003；按形态进场是 −0.018，差 0.021R（t = −0.73）。训练段超出 +0.022R，验证段 −0.078R。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.056R（t = −1.50），验证段（2024 年起）每笔 −0.150R（t = −3.43）。
- **7 年里 6 年亏。** 赚的是 2021 年（+0.009R）。2022 年起每年都亏。
- **邻近变体、压力测试全是负的。** 两个低点相差不超过 0.25 个 ATR −0.053R，形态高度至少 1 个 ATR −0.095R，止盈按形态高度 −0.083R，摆动点左右各 5 根 −0.071R；成本翻倍 −0.176R，晚一根 K 线 −0.138R。手续费、滑点都记 0（资金费照算）也是亏的：每笔 −0.018R（t = −0.65）。

```bash
git clone https://github.com/runningshark/h1_patterns_chan_failureprove
cd h1_patterns_chan_failureprove
py verify.py G1
```

### 67 · 头肩底、头肩顶

“头肩底突破颈线做多，头肩顶跌破颈线做空”。规则：三个摆动低点，中间的头最低、两肩差不多高，收盘突破两个反弹高点连成的颈线时做多，止损在右肩外面；头肩顶对称。（[档案](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/reports/67_G2_head_and_shoulders.md)）

- **扣成本后每笔亏 0.058R。** 981 笔（每年约 149 笔），胜率 37%，扣成本后平均赚 1.61R、平均亏 1.05R。不扣成本每笔 +0.047R，手续费加滑点每笔 0.102R，资金费每笔付出 0.002R。组合 t = −1.18，每年合计 −9R，最大回撤 119R。
- **比随手进场好一点，但不显著，样本也少。** 同样的方向、同样的止损止盈，在前后 30 天里随手进场，每笔毛 R 是 −0.011；按形态进场是 +0.047，超出 +0.058R（t = 1.16）。训练段超出 +0.093R，验证段只有 +0.007R。一共只有 981 笔。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.011R（t = −0.18），验证段（2024 年起）每笔 −0.125R（t = −1.63）。
- **7 年里 5 年亏。** 赚的是 2020 年（+0.254R）、2021 年（+0.026R）。2022 年起每年都亏。
- **邻近变体、压力测试全是负的。** 两肩相差不超过 0.5 个 ATR −0.071R，水平颈线 −0.087R，止损在头的外面 −0.007R，摆动点左右各 5 根 −0.234R；成本翻倍 −0.160R，晚一根 K 线 −0.063R。手续费、滑点都记 0（资金费照算），每笔 +0.045R（t = 0.94），也不显著。

```bash
git clone https://github.com/runningshark/h1_patterns_chan_failureprove
cd h1_patterns_chan_failureprove
py verify.py G2
```

### 68 · 收敛三角形突破

“收敛三角形突破跟进”。规则：高点一个比一个低、低点一个比一个高，收盘突破上边线做多、跌破下边线做空，止损在三角形另一边最后一个低点（高点）外面。（[档案](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/reports/68_G3_triangle_breakout.md)）

- **扣成本后每笔亏 0.081R。** 4,585 笔（每年约 696 笔），胜率 37%，扣成本后平均赚 1.63R、平均亏 1.07R。不扣成本每笔 +0.025R，手续费加滑点每笔 0.104R，资金费每笔付出 0.002R。组合 t = −3.54，每年合计 −56R，最大回撤 395R。
- **和随手进场没有分别。** 同样的方向、同样的止损止盈，在前后 30 天里随手进场，每笔毛 R 是 +0.004；按规则进场是 +0.025，超出 +0.021R（t = 0.94）；训练段 +0.024R，验证段 +0.017R。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.078R（t = −2.72），验证段（2024 年起）每笔 −0.084R（t = −2.27）。
- **每一年都亏。** 2020 到 2026 年，每年的每笔净 R 在 −0.155R 到 −0.009R 之间。
- **邻近变体、压力测试全是负的。** 四个点在最近 240 根以内 −0.081R，止损在另一条边线外面 −0.084R，起点宽度至少 3 个 ATR −0.073R，摆动点左右各 5 根 −0.064R；成本翻倍 −0.185R，晚一根 K 线 −0.106R。手续费、滑点都记 0（资金费照算），每笔 +0.023R（t = 1.07），也不显著。

```bash
git clone https://github.com/runningshark/h1_patterns_chan_failureprove
cd h1_patterns_chan_failureprove
py verify.py G3
```

### 69 · 缠论一买、一卖（笔的背驰）

“背驰是第一类买点”。规则：K 线做包含处理后画笔，新的下跌笔创了新低、MACD 柱面积却比前一个下跌笔小，就做多，止损在这一笔的低点外面；一卖对称。（[档案](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/reports/69_C1_chan_buy1.md)）

- **扣成本后每笔亏 0.150R。** 7,894 笔（每年约 1,198 笔），胜率 35%，扣成本后平均赚 1.73R、平均亏 1.15R。不扣成本每笔 −0.001R，手续费加滑点每笔 0.151R，资金费每笔收到 0.002R。组合 t = −7.08，每年合计 −179R，最大回撤 1,217R。
- **和随手进场没有分别。** 同样的方向、同样的止损止盈，在前后 30 天里随手进场，每笔毛 R 是 +0.002；按规则进场是 −0.001，超出 −0.004R（t = −0.17）；训练段 −0.006R，验证段 −0.001R。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.125R（t = −4.48），验证段（2024 年起）每笔 −0.179R（t = −5.63）。
- **每一年都亏。** 2020 到 2026 年，每年的每笔净 R 在 −0.233R 到 −0.068R 之间。
- **邻近变体、压力测试全是负的。** 力度用 MACD 柱的最大值 −0.123R，还要求 DIF 在零轴下方（一卖在上方） −0.150R，笔放宽为至少 3 根 −0.128R，止盈 3R −0.172R；成本翻倍 −0.300R，晚一根 K 线 −0.200R。手续费、滑点都记 0（资金费照算），每笔 +0.001R（t = 0.05），也不显著。
- **止损紧，成本吃掉一大块。** 止损放在笔的端点外面 0.1 个 ATR，中位数只有价格的 1.54%（1.31 个 ATR），一进一出的手续费和滑点就是每笔 0.151R；不扣成本时，它和随手进场一样接近 0。

```bash
git clone https://github.com/runningshark/h1_patterns_chan_failureprove
cd h1_patterns_chan_failureprove
py verify.py C1
```

### 70 · 缠论二买、二卖

“一买之后回调不创新低是第二类买点”。规则：前一个下跌笔是一买，之后再下跌的一笔低点高于一买，就做多，止损在这一笔的低点外面；二卖对称。（[档案](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/reports/70_C2_chan_buy2.md)）

- **扣成本后每笔亏 0.193R。** 4,733 笔（每年约 718 笔），胜率 34%，扣成本后平均赚 1.79R、平均亏 1.22R。不扣成本每笔 +0.010R，手续费加滑点每笔 0.203R，资金费每笔不到 0.001R。组合 t = −7.59，每年合计 −139R，最大回撤 977R。
- **和随手进场没有分别。** 同样的方向、同样的止损止盈，在前后 30 天里随手进场，每笔毛 R 是 −0.012；按规则进场是 +0.010，超出 +0.022R（t = 0.90）；训练段 +0.043R，验证段 −0.005R。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.157R（t = −4.45），验证段（2024 年起）每笔 −0.238R（t = −6.70）。
- **每一年都亏。** 2020 到 2026 年，每年的每笔净 R 在 −0.323R 到 −0.071R 之间。
- **邻近变体、压力测试全是负的。** 不要求前一个低点是一买 −0.197R，止损在一买的外面 −0.104R，笔放宽为至少 3 根 −0.162R，止盈 3R −0.199R；成本翻倍 −0.396R，晚一根 K 线 −0.213R。手续费、滑点都记 0（资金费照算），每笔 +0.010R（t = 0.42），也不显著。
- **止损紧，成本吃掉一大块。** 止损放在笔的端点外面 0.1 个 ATR，中位数只有价格的 1.11%（0.99 个 ATR），一进一出的手续费和滑点就是每笔 0.203R；不扣成本时，它和随手进场一样接近 0。

```bash
git clone https://github.com/runningshark/h1_patterns_chan_failureprove
cd h1_patterns_chan_failureprove
py verify.py C2
```

### 71 · 缠论三买、三卖

“离开中枢后回抽不进中枢是第三类买点”。规则：三笔重叠构成中枢，向上离开以后，回抽的低点仍然高于中枢上沿，就做多，止损在回抽的低点外面；三卖对称。（[档案](https://github.com/runningshark/h1_patterns_chan_failureprove/blob/master/reports/71_C3_chan_buy3.md)）

- **扣成本后每笔亏 0.190R。** 7,838 笔（每年约 1,190 笔），胜率 34%，扣成本后平均赚 1.81R、平均亏 1.22R。不扣成本每笔 +0.005R，手续费加滑点每笔 0.193R，资金费每笔付出 0.003R。组合 t = −8.06，每年合计 −227R，最大回撤 1,520R。
- **和随手进场没有分别。** 同样的方向、同样的止损止盈，在前后 30 天里随手进场，每笔毛 R 是 +0.004；按规则进场是 +0.005，超出 +0.001R（t = 0.06）；训练段 −0.046R，验证段 +0.062R。
- **两段都亏。** 训练段（2020-04 到 2023 年底）每笔 −0.225R（t = −7.19），验证段（2024 年起）每笔 −0.146R（t = −4.13）。
- **每一年都亏。** 2020 到 2026 年，每年的每笔净 R 在 −0.305R 到 −0.049R 之间。
- **邻近变体、压力测试全是负的。** 回抽离中枢至少 0.25 个 ATR −0.186R，止损在中枢边上 −0.148R，笔放宽为至少 3 根 −0.166R，止盈 3R −0.202R；成本翻倍 −0.383R，晚一根 K 线 −0.221R。手续费、滑点都记 0（资金费照算），每笔 +0.002R（t = 0.10），也不显著。
- **止损紧，成本吃掉一大块。** 止损放在笔的端点外面 0.1 个 ATR，中位数只有价格的 1.15%（0.95 个 ATR），一进一出的手续费和滑点就是每笔 0.193R；不扣成本时，它和随手进场一样接近 0。

```bash
git clone https://github.com/runningshark/h1_patterns_chan_failureprove
cd h1_patterns_chan_failureprove
py verify.py C3
```

### 72–77 · 第十三轮事先登记的研究：仓位和执行（共用一个仓库）

前几轮测的是“在哪里开单”，这一轮测“开了单以后怎么管”：网格、马丁格尔、随机进场加移动止损（Van Tharp），以及保本止损、分批止盈、浮盈加仓。数据和第十轮到第十二轮相同，规则和通过标准同样是事先登记的（[事先登记_第十三轮.md](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/事先登记_第十三轮.md)）。**登记 6 个，6 个失败**。

- 累计 69 个候选，门槛是 t ≥ 3.4。币安 U 本位永续的 1 小时 K 线，每个季度按成交额选 10 个币（共 48 个合约，含后来下架的），2020-04 到 2026-10，训练段到 2023 年底。市价每边 0.10%、限价每边 0.02%，资金费照算。
- A 组（网格、马丁格尔、移动止损）和**同一批 K 线打乱顺序**的结果比：每个季度的总涨跌、每根 K 线的形状不变，只去掉先后关系。B 组（保本止损、分批止盈、浮盈加仓）用同一批随机进场，比加和不加的差别。
- 网格在单边行情里大亏；马丁格尔赚的是上涨，打乱顺序以后赚得更多；移动止损和浮盈加仓抓到一点顺势延续，但付不起成本；保本止损、分批止盈只改变胜率。
- 这 6 条共用一个仓库 [h1_position_mgmt_failureprove](https://github.com/runningshark/h1_position_mgmt_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/FAILURE_REPORT.md)。数据来自 Binance Vision（CC BY-NC-SA 4.0）。

### 72 · 网格（合约中性网格）

“网格在震荡里来回赚钱，不用判断方向”。规则：每个季度开始时，以开盘价为中心开一个中性网格，上下各 10 格、每格 1%，跌一格买一份、涨一格卖一份，出了区间不再挂单，季度末全部平仓。（[档案](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/reports/72_E1_grid_neutral.md)）

- **扣成本后大亏。** 每天的组合收益年化 −74.7%（t −2.60），夏普 −0.93；每个季度重新放 1 份资金、不复利，6 年半里累计的最大回撤是 −497%（亏掉将近 5 份资金）。成本不是主要原因：零成本也是年化 −70.9%。
- **震荡时赚，单边时亏得更多。** 273 个网格（币 × 季度）里，季度末价格还在 ±10% 以内的只有 18%，它们的中位数是 +26.3%；走出区间的 82% 中位数是 −14.2%。涨超过 50% 的 50 个季度平均 −103%：中性网格一路卖、一路做空，价格不回头。网格的盈亏和币的季度涨跌的相关是 −0.81。价格有 67% 的时间在区间外，每个季度成交约 400 次。
- **打乱 K 线顺序也亏，真实的更差。** 同一批 K 线打乱顺序以后年化 −58.1%：亏损主要来自每个季度的总涨跌，不是来自 K 线的先后。真实的比打乱的还差 −16.6%（日度 t −0.59；按季度加总的 t −3.04，登记之外）。
- **两段都亏。** 训练段（到 2023 年底）年化 −94.5%（t −2.08），验证段（2024 年起）−48.4%（t −1.66）。
- **邻近变体、压力测试全是负的。** 每格 0.5% −96.1%（t −3.35），每格 2% −60.8%（t −2.10），区间 ±20% −64.8%（t −2.36），出了区间就平仓重开 −140.7%（t −4.25）；成本翻倍 −78.5%（t −2.73），价格越过格子 0.05% 才成交 −80.1%（t −2.79）。
- **这里没有算爆仓。** 15 个网格一个季度亏掉超过本金（最多 −614%，BNB 2021Q1 涨了 709%）。如果亏到本金就爆仓，平均每个季度 −10.7%，仍然是大亏。

```bash
git clone https://github.com/runningshark/h1_position_mgmt_failureprove
cd h1_position_mgmt_failureprove
py verify.py E1
```

### 73 · 马丁格尔（摊平加仓）

“马丁格尔胜率接近 100%”。规则：每个季度开一个只做多的机器人，每跌 2% 补一次仓、金额翻倍（最多 5 次），涨到均价上面 1.5% 全部卖出再开始新的一轮，没有止损，季度末全部平仓。（[档案](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/reports/73_E2_martingale_dca.md)）

- **扣成本后年化 +15.0%，不显著（t 1.09）。** 夏普 0.37，累计最大回撤 −79%。
- **赚的是上涨的行情，不是摊平。** 同一批 K 线打乱顺序以后年化 +18.9%，比真实的还高；超出打乱 −3.8%（t −0.29）。机器人一直拿着多单，盈亏和币的季度涨跌的相关是 0.63：涨超过 50% 的季度平均 +31%，跌超过 30% 的平均 −32%。
- **“胜率 99%”是每一轮的胜率。** 35,454 轮里 99.3% 止盈；但 97% 的机器人到季度末还有没止盈的仓位，84% 的机器人最后一轮是亏着平掉的。97% 的机器人在季度里至少有一次把补仓单用完。
- **2024 年起基本不赚。** 训练段年化 +23.8%（t 1.21），验证段 +3.4%（t 0.18）。
- **邻近变体、压力测试都没有过门槛。** 每跌 3% 补一次 +19.3%（t 2.04），补仓金额每次 1.5 倍 +14.5%（t 0.90），止盈 1% +12.9%（t 1.15），加满后再跌 5% 止损 −7.7%（t −0.92）；成本翻倍 +12.0%（t 0.87），补仓改成下一根开盘市价 +4.4%（t 0.45）。不算资金费是年化 +16.6%。

```bash
git clone https://github.com/runningshark/h1_position_mgmt_failureprove
cd h1_position_mgmt_failureprove
py verify.py E2
```

### 74 · 随机进场加移动止损（Van Tharp）

“随机进场加 3 倍 ATR 的移动止损也能赚钱”（Van Tharp）。规则：随机时刻、随机方向进场，止损 3 个 ATR，每根收盘按“收盘价减 3 个 ATR”往有利方向移，没有止盈。（[档案](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/reports/74_E3_random_entry_trailing_stop.md)）

- **扣成本后每笔亏 0.042R（t −2.93）。** 23,789 笔（每年约 3,610 笔），胜率 33%，平均赚 1.22R、平均亏 0.67R，持有中位数 24 根。不扣成本每笔 +0.027R，成本每笔 0.070R（3 个 ATR 的止损中位数是价格的 3.55%）。
- **真实的 K 线比打乱的多一点趋势，但不够付成本。** 同一批进场，真实的毛 R +0.027，打乱顺序以后 −0.020，超出 +0.048R（t 3.42，刚过 3.4 的门槛；训练段 +0.048R，验证段 +0.046R）。
- **一部分来自打乱本身。** 打乱以后毛 R 是负的，说明打乱会让顺势的出场吃亏。只翻转每根 K 线的方向、不动位置（保留波动的聚集，登记之外）时，对照是 −0.001R，真实的超出 +0.029R（t 2.12）。
- **两段都亏。** 训练段每笔 −0.041R（t −2.32），验证段 −0.044R（t −1.83）。不扣成本每笔 +0.026R（t 1.81），也不显著。
- **邻近变体、压力测试全是负的。** 2 个 ATR −0.082（t −6.40），4 个 ATR −0.022（t −1.07），从最高价（最低价）算 −0.053（t −5.80），最长持有 120 根 −0.040（t −2.79）；成本翻倍 −0.111（t −7.47），移动止损晚一根更新 −0.042（t −2.94）。做多每笔 −0.069R，做空 −0.015R。

```bash
git clone https://github.com/runningshark/h1_position_mgmt_failureprove
cd h1_position_mgmt_failureprove
py verify.py E3
```

### 75 · 保本止损

“赚到 1R 就把止损移到保本”。规则：同一批随机进场，比较“止损 1 个 ATR、止盈 2R”和“收盘到了 1R 以后止损移到进场价”。（[档案](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/reports/75_E4_breakeven_stop.md)）

- **没有改进。** 24,081 笔随机进场，加上保本止损每笔 −0.172R，不加 −0.168R，改进 −0.004R（t −1.20）。不扣成本的改进 −0.001R（t −0.32）。
- **胜率反而低了。** 保本出场扣了成本也是小亏，胜率从 34% 变成 30%；少亏的和少赚的差不多抵消。
- **越早移越差。** 到 0.5R 就移 −0.012（t −2.56），到 1.5R 才移 0.000（t −0.03），移到进场价外面 0.2% −0.007（t −2.06），止盈改成 3R −0.002（t −0.40）。
- **两段都没有改进。** 训练段 −0.004R（t −1.07），验证段 −0.003R（t −0.62）。
- **压力测试也是负的。** 成本翻倍 −0.006（t −2.07），止损晚一根移到进场价 −0.003（t −0.97）。

```bash
git clone https://github.com/runningshark/h1_position_mgmt_failureprove
cd h1_position_mgmt_failureprove
py verify.py E4
```

### 76 · 分批止盈

“先平一半、剩下的让利润奔跑”。规则：同一批随机进场，比较“全部在 2R 止盈”和“一半在 1R、一半在 2R，第一半成交后止损移到进场价”。（[档案](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/reports/76_E5_partial_take_profit.md)）

- **没有改进。** 24,204 笔随机进场，分批止盈每笔 −0.165R，全部在 2R 止盈 −0.165R，改进 −0.001R（t −0.13）。
- **胜率从 34% 提高到 50%，每笔赚的一样。** 先平的一半更容易到，但剩下一半少赚了；分批只是改变了盈亏的分布。
- **变体也都在 0 附近。** 第一半成交后止损不移 +0.001（t 0.34），第一半在 1.5R +0.002（t 0.66），第二部分在 3R +0.003（t 0.37），先平三分之一 −0.002（t −0.35）。
- **两段一正一负。** 训练段 +0.002R（t 0.30），验证段 −0.004R（t −0.54）。不扣成本的改进 −0.004R（t −0.82）。
- **压力测试：** 成本翻倍 +0.003（t 0.51），第一半改成下一根开盘市价平 −0.001（t −0.19）。

```bash
git clone https://github.com/runningshark/h1_position_mgmt_failureprove
cd h1_position_mgmt_failureprove
py verify.py E5
```

### 77 · 浮盈加仓

“大钱靠浮盈加仓”。规则：同一批随机进场，比较“1 份、止损 2 个 ATR、持有 96 根”和“每赚 1 个 ATR 加 1 份（最多 4 份），止损跟着移到最近一次加仓价减 2 个 ATR”。（[档案](https://github.com/runningshark/h1_position_mgmt_failureprove/blob/master/reports/77_E6_pyramiding.md)）

- **扣成本后没有改进。** 24,033 笔随机进场，浮盈加仓每笔 −0.057R，不加 −0.056R，改进 −0.001R（t −0.02）。
- **不扣成本时多赚，被成本吃光。** 不扣成本的改进是 +0.147R（t 3.18）：加仓确实抓到了一点趋势（只翻转每根 K 线的方向时，这个数是 +0.005R，登记之外）。但每多加一份就多付一进一出的成本，扣完正好没了；成本翻倍时改进是 −0.143R。
- **胜率从 24% 降到 8%。** 加仓以后止损跟着上移，大部分单最后打在止损上，靠少数大赚的单撑着。
- **做多赚、做空亏。** 做多的改进 +0.097R，做空 −0.101R：主要是上涨行情里加多单赚钱。训练段 +0.008R（t 0.14），验证段 −0.013R（t −0.18）。
- **邻近变体、压力测试：** 每 0.5A 加一次 −0.059（t −1.05），最多 2 份 −0.014（t −0.64），止损 1A −0.080（t −1.96），加仓后止损不移 +0.003（t 0.04）；成本翻倍 −0.143（t −3.17），加仓改成下一根开盘市价 −0.014（t −0.33）。

```bash
git clone https://github.com/runningshark/h1_position_mgmt_failureprove
cd h1_position_mgmt_failureprove
py verify.py E6
```

### 78–83 · 第十四轮事先登记的研究：资金费和基差的极端值、BTC 和山寨的轮动、低贝塔和偏度（共用一个仓库）

清单上还没测的三个方向：资金费和基差的极端值（负资金费做多、升水过高做空），BTC 和山寨的轮动（领涨补涨、相对强势之后换山寨），以及两个没测过的横截面因子（低贝塔、偏度）。规则和通过标准同样是事先登记的（[事先登记_第十四轮.md](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/事先登记_第十四轮.md)）。**登记 6 个，6 个失败**。

- 累计 75 个候选，门槛是 t ≥ 3.5。币安现货和 U 本位永续的日线、日资金费，H3 用 1 小时 K 线；每个季度按成交额选 10 个币（共 48 个合约，含后来下架的），2020-04 到 2026-10，训练段到 2023 年底。每边成本 0.10%，资金费照算。
- 前四个是事件，和**随手进场**比（同一个币、同一个方向、同样拿多久，进场时刻在前后 30 天里随机抽）；后两个是周度多空组合，和**随手选币**比。
- 负资金费做多在 2024 年以前比随手进场好，之后没有了；升水高时做空只是比随手做空亏得少；落后于 BTC 的山寨不补涨；轮动没有规律；低贝塔的收益主要来自拿着 BTC；做空“彩票”币亏钱。
- 这 6 条共用一个仓库 [d1_funding_rotation_factors_failureprove](https://github.com/runningshark/d1_funding_rotation_factors_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/FAILURE_REPORT.md)。数据来自 Binance Vision（CC BY-NC-SA 4.0）。

### 78 · 负资金费做多

“资金费很负说明空头太拥挤，会被挤空”。规则：某个币当天的资金费合计 ≤ −0.03%，当天收盘做多永续合约，拿 3 天。（[档案](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/reports/78_H1_negative_funding_long.md)）

- **扣成本后每笔 +0.79%，不显著（t 1.70）。** 801 笔（每年约 122 笔），胜率 52%，平均赚 7.09%、亏 5.98%。不扣成本每笔 +0.99%（其中平均收到 0.23% 的资金费），成本 0.20%。
- **比随手进场好，但只在 2024 年以前。** 同一个币、同样做多 3 天，随手进场平均 −0.13%，真实的 +0.99%，超出 +1.12%（t 2.45）。训练段超出 +1.62%（t 2.56），验证段只有 +0.20%（t 0.37）。
- **验证段不赚钱。** 训练段每笔 +1.32%（t 2.02），验证段 −0.17%（t −0.32）。2022 年笔数最多（294 笔，熊市里资金费常常是负的），每笔 −0.23%，其中 LUNA 的 22 笔平均 −5.27%；2025 年每笔 −0.83%。拿掉 2022 年，每笔 +1.39%（t 2.57，登记之外）。
- **邻近变体都为正，但只有两个 t 过 1.5。** 门槛 −0.1% 246 笔 +1.89%（t 2.16），只要是负的 1,944 笔 +0.18%（t 0.52），拿 1 天 1,163 笔 +0.24%（t 0.71），拿 7 天 547 笔 +2.35%（t 2.34）；压力测试 成本翻倍 +0.59%（t 1.27），晚一天进场 +0.72%（t 1.35）。
- **集中在少数几个币。** BNB 一个币就有 177 笔（22%），每笔 +1.36%。

```bash
git clone https://github.com/runningshark/d1_funding_rotation_factors_failureprove
cd d1_funding_rotation_factors_failureprove
py verify.py H1
```

### 79 · 升水过高做空

“永续合约升水过高说明市场过热”。规则：永续收盘价比现货高 0.15% 以上（不到 5%），当天收盘做空，拿 3 天。（[档案](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/reports/79_H2_high_basis_short.md)）

- **扣成本后每笔亏 0.87%（t −0.73）。** 376 笔，胜率 54%，平均赚 7.53%、亏 10.83%；不扣成本每笔 −0.67%（其中平均收到 0.59% 的资金费），收到的资金费抵不过价格继续涨。
- **亏得比随手做空少，差别不显著。** 347 笔在 2020–2021 年（基差 ≥ +0.15% 几乎只在那时的牛市里出现），这时随手做空 3 天平均 −1.75%，升水信号做空 −0.67%，超出 +1.08%（t 0.92）。
- **唯一的一大笔是 LUNA。** 2022-05-10 收盘做空，合约 2022-05-12 之后停止交易，在最后一个收盘价平仓，+95.7%；拿掉这一笔，每笔 −1.13%（t −0.97，登记之外）。
- **两段都亏。** 训练段每笔 −0.93%（t −0.74），验证段 −0.02%（t −0.01，只有 22 笔）。
- **邻近变体、压力测试全是负的。** 门槛 +0.1% 873 笔 −1.11%（t −1.67），门槛 +0.3% 52 笔 −0.12%（t −0.04），拿 1 天 519 笔 −0.15%（t −0.33），拿 7 天 257 笔 −2.48%（t −0.96）；成本翻倍 −1.07%（t −0.89），晚一天进场 −1.28%（t −0.97）。

```bash
git clone https://github.com/runningshark/d1_funding_rotation_factors_failureprove
cd d1_funding_rotation_factors_failureprove
py verify.py H2
```

### 80 · BTC 领涨、山寨补涨

“BTC 先涨，山寨跟着补涨”。规则（1 小时）：BTC 24 小时涨了 3% 以上、某个山寨落后 3 个百分点以上，下一根做多这个山寨，拿 24 根；领跌时反过来做空。（[档案](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/reports/80_H3_btc_lead_alt_catchup.md)）

- **扣成本后每笔亏 0.31%（t −1.58）。** 2,655 笔（每年约 403 笔），胜率 46%，平均赚 4.55%、亏 4.44%；不扣成本每笔 −0.11%，成本 0.20%。
- **比随手进场还差，落后的不补涨。** 同一个币、同一个方向、同样拿 24 根，随手进场平均 +0.16%，真实的 −0.11%，超出 −0.27%（t −1.35）。做多（补涨）1,712 笔扣成本后每笔 +0.01%，做空（补跌）943 笔 −0.88%。
- **门槛放宽以后显著地亏。** 5% 和 5 个百分点 816 笔 −0.10%（t −0.27），2% 和 2 个百分点 5,139 笔 −0.42%（t −3.04），拿 12 根 3,689 笔 −0.22%（t −2.01），拿 48 根 2,108 笔 +0.21%（t 0.67）。
- **两段都亏，压力测试也是负的。** 训练段每笔 −0.30%（t −1.19），验证段 −0.34%（t −1.22）；成本翻倍 −0.51%（t −2.62），晚一根进场 −0.33%（t −1.70）。

```bash
git clone https://github.com/runningshark/d1_funding_rotation_factors_failureprove
cd d1_funding_rotation_factors_failureprove
py verify.py H3
```

### 81 · BTC 强势之后换山寨

“BTC 涨得多了以后，资金轮动到山寨”。规则：山寨篮子 30 天的平均涨幅比 BTC 少 15 个百分点以上，做多篮子、做空 BTC，拿 7 天；多 15 个百分点以上时反过来。（[档案](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/reports/81_H4_btc_alt_rotation.md)）

- **每笔接近 0。** 111 笔（每年约 17 笔），扣成本后每笔 +0.05%（t 0.07）；两条腿的成本每笔 0.40%，不扣成本 +0.45%。
- **和随手进场比，差别不显著。** 同一种组合、同一个方向、同样拿 7 天，随手进场平均 −0.26%，真实的 +0.45%，超出 +0.71%（t 0.91）。
- **两个方向一正一负，两段也一正一负。** 做多篮子（BTC 多涨了 15 个百分点以后）53 笔每笔 +1.60%，反过来 58 笔 −1.36%；训练段 −0.68%（t −0.67），验证段 +1.64%（t 1.55）。
- **邻近变体大多为负。** 门槛 10% 169 笔 −0.52%（t −0.93），门槛 25% 42 笔 −1.93%（t −1.51），用 60 天的涨幅 158 笔 −0.75%（t −1.16），拿 14 天 70 笔 +0.39%（t 0.26）；压力测试 成本翻倍 −0.35%（t −0.45），晚一天进场 +0.04%（t 0.05）。

```bash
git clone https://github.com/runningshark/d1_funding_rotation_factors_failureprove
cd d1_funding_rotation_factors_failureprove
py verify.py H4
```

### 82 · 低贝塔（Betting Against Beta）

“低贝塔的资产风险调整后更好”（Frazzini 和 Pedersen，2014）。规则：每周按 60 天的贝塔，做多最低的 3 个币、做空最高的 3 个，按贝塔加权让组合的事前贝塔为 0。（[档案](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/reports/82_H5_low_beta_bab.md)）

- **扣成本后年化 +20.8%，不显著（t 1.74）。** 夏普 0.71，累计最大回撤 −46%（按天相加）；平均每次调仓换手 0.29。训练段年化 +23.7%（t 1.36），验证段 +17.0%（t 1.11）。
- **主要是拿着 BTC。** 按贝塔加权以后，组合平均净多头 40%（多头仓位减空头仓位），BTC 在 93% 的周里在多头那边。把每天的收益对市场（当季 10 个币的平均）和 BTC 回归，截距只剩年化 +8.4%（t 0.82，登记之外）；同样的选币改成多空等额，年化 +0.9%（t 0.07）。
- **和随手选币比，不过门槛。** 20 个随机组合（同样按贝塔加权）年化 −7.8%，超出 +28.7%（t 2.43）。随机组合每周全换，手续费每年约 7.7%；不扣手续费，超出 +22.5%（t 1.92）。
- **邻近变体：** 用过去 120 天 +27.1%（t 2.41），对 BTC 算贝塔 +28.4%（t 2.05），多空各 2 个 +29.2%（t 1.96），多空等额 +0.9%（t 0.07）；压力测试 成本翻倍 +19.3%（t 1.62），晚一天调仓 +24.2%（t 2.02）。

```bash
git clone https://github.com/runningshark/d1_funding_rotation_factors_failureprove
cd d1_funding_rotation_factors_failureprove
py verify.py H5
```

### 83 · 偏度（彩票效应）

“像彩票的资产被买贵了”（偏度、MAX 效应）。规则：每周按 30 天日收益的偏度，做多最低的 3 个币、做空最高的 3 个，等额。（[档案](https://github.com/runningshark/d1_funding_rotation_factors_failureprove/blob/master/reports/83_H6_skewness_lottery.md)）

- **扣成本后年化 −15.2%（t −1.20）。** 夏普 −0.48，累计最大回撤 −104%（按天相加，不复利）；平均每次调仓换手 0.78。
- **做空“彩票”币亏钱。** 偏度最高的币（暴涨过的）之后没有变差。和随手选币比，超出 −6.8%（t −0.55）；只有 2022、2025 年为正。
- **两段都亏。** 训练段年化 −15.7%（t −0.83），验证段 −14.4%（t −0.96）。
- **邻近变体、压力测试全是负的。** 用 MAX 代替偏度 −12.4%（t −0.90），用过去 60 天 −6.4%（t −0.53），多空各 2 个 −12.0%（t −0.76），每两周调一次仓 −1.9%（t −0.15）；成本翻倍 −19.2%（t −1.52），晚一天调仓 −16.1%（t −1.35）。

```bash
git clone https://github.com/runningshark/d1_funding_rotation_factors_failureprove
cd d1_funding_rotation_factors_failureprove
py verify.py H6
```

### 84–95 · 第十五轮事先登记的研究：订单流、机器学习、期权隐含波动率、宏观、情绪指数、BTC 市占率（共用一个仓库）

订单流（主动买入占比、主动买入的极端日、大单日）、机器学习选币（岭回归、梯度提升树，模型和参数事先固定，只算一次）、BTC 期权隐含波动率（飙升后做多、波动率风险溢价）、宏观（实际利率、美元、FOMC 公布前）、恐惧贪婪指数、BTC 市占率。规则和通过标准同样是事先登记的（[事先登记_第十五轮.md](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/事先登记_第十五轮.md)）。**登记 12 个，12 个失败**。

- 累计 87 个候选，门槛是 t ≥ 3.5。币安 U 本位永续合约和现货的日线、BTC 现货的 1 小时 K 线、BVOL（Binance Vision）；美国财政部、美联储理事会的公开数据；Coin Metrics 社区数据；alternative.me 的恐惧贪婪指数（不随仓库公开）。每个季度按成交额选 10 个币，2020-04 到 2026-10（择时规则从 2017-09 或 2018-02 起），训练段到 2023 年底。每边成本 0.10%，资金费照算。
- 事件类和**随手进场**比；周度组合和**随手选币**比；BTC 的满仓 / 空仓择时看**择时超额**和**平移检验**（和第九轮相同）。
- 机器学习的排名有预测力（排名相关约 0.13，验证段也在），但等额多空 3 个币被少数几周的大亏拖住；主动买入占比 2024 年起变弱；宏观和情绪择时没有择时超额；FOMC 公布前的漂移只来自 2020 年；顺着市占率做是亏的。
- 这 12 条共用一个仓库 [orderflow_ml_macro_failureprove](https://github.com/runningshark/orderflow_ml_macro_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/FAILURE_REPORT.md)。数据许可见仓库的 data/README.md。

### 84 · 主动买入占比（订单流）

“主动买盘强，后面要涨”（订单流失衡）。规则：每周按过去 7 天的主动买入成交额占比，做多最高的 3 个币、做空最低的 3 个。（[档案](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/84_OF1_taker_share_weekly.md)）

- **扣成本后年化 +21.8%（t 1.88）。** 夏普 0.75，累计最大回撤 −56%（按天相加）；343 周，平均每次调仓换手 0.91，资金费每年 −3.4%。
- **不只是动量，但也不稳。** 分数和下一周涨跌的排名相关 0.084（t 4.39），验证段 0.067（t 2.18）；每周选中的币和按 7 天涨幅选的只有 48% 相同，两个组合每天收益的相关 0.29，对动量组合回归后剩下 +21.1%（t 1.89，登记之外）。
- **和随手选币比：** 20 个随机组合年化 −5.2%，超出 +26.9%（t 2.28）；不扣手续费，超出 +24.1%（t 2.05）。
- **训练段年化 +33.1%（t 2.02），验证段 +6.8%（t 0.43）。**
- **邻近变体：** 只看过去 1 天 +14.1%（t 1.31），看过去 30 天 +19.4%（t 1.68），减去自己过去 90 天的平均占比 +8.9%（t 0.71），多空各 2 个 +15.4%（t 1.10）；压力测试 成本翻倍 +17.0%（t 1.47），晚一天调仓 +20.8%（t 1.84）。

```bash
git clone https://github.com/runningshark/orderflow_ml_macro_failureprove
cd orderflow_ml_macro_failureprove
py verify.py OF1
```

### 85 · 主动买入占比的极端日

“主动买入突然大增，跟着做”。规则：某个币当天的主动买入占比比前 30 天的平均高（低）2 个标准差以上，当天收盘做多（做空），拿 3 天。（[档案](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/85_OF2_taker_share_extreme.md)）

- **扣成本后每笔 +0.01%（t 0.05）。** 1,305 笔（每年约 198 笔），胜率 50%，平均赚 5.76%、亏 5.76%；不扣成本每笔 +0.21%，成本 0.20%。
- **“超出随手进场”来自随手进场是亏的。** 同一个币、同一个方向随机进场平均 −0.45%（做空那边亏得多）；真实交易扣成本后接近 0。门槛提高到 3 个标准差的 226 笔每笔 +1.34%（t 2.26），7 年每年都为正，是事后线索，不是结论。
- **和随手进场比：** 随手进场平均 −0.45%，真实的 +0.21%，超出 +0.67%（t 2.35）；训练段超出 +0.84%，验证段 +0.45%。
- **训练段每笔 +0.06%（t 0.14，726 笔），验证段 −0.04%（t −0.12，579 笔）。**
- **邻近变体：** 门槛 1.5 个标准差 2,526 笔 −0.25%（t −1.08），门槛 3 个标准差 226 笔 +1.34%（t 2.26），拿 1 天 1,498 笔 −0.01%（t −0.06），拿 7 天 1,082 笔 +0.59%（t 1.15）；压力测试 成本翻倍 −0.19%（t −0.66），晚一天进场 +0.03%（t 0.11）。

```bash
git clone https://github.com/runningshark/orderflow_ml_macro_failureprove
cd orderflow_ml_macro_failureprove
py verify.py OF2
```

### 86 · 大单日跟随

“大单进场，跟着主力走”。规则：平均每笔成交额比前 30 天的平均高 2 个标准差以上，跟着当天的涨跌方向，拿 3 天。（[档案](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/86_OF3_big_trade_days.md)）

- **扣成本后每笔 +0.48%（t 1.05）。** 837 笔（每年约 127 笔），胜率 50%，平均赚 7.52%、亏 6.48%；不扣成本每笔 +0.68%，成本 0.20%。
- **做多赚、做空亏，和随手进场差不多。** 做多 604 笔每笔 +1.26%（超出随手进场 +0.47%），做空 233 笔 −1.56%（超出 −0.73%）。
- **和随手进场比：** 随手进场平均 +0.55%，真实的 +0.68%，超出 +0.13%（t 0.31）；训练段超出 +0.47%，验证段 −0.29%。
- **训练段每笔 +1.09%（t 1.60，467 笔），验证段 −0.29%（t −0.52，370 笔）。**
- **邻近变体：** 门槛 1.5 个标准差 1,354 笔 +0.62%（t 1.75），门槛 3 个标准差 288 笔 +0.50%（t 0.68），拿 1 天 1,083 笔 +0.14%（t 0.62），拿 7 天 657 笔 +1.70%（t 2.18）；压力测试 成本翻倍 +0.28%（t 0.62），晚一天进场 +0.73%（t 1.61）。

```bash
git clone https://github.com/runningshark/orderflow_ml_macro_failureprove
cd orderflow_ml_macro_failureprove
py verify.py OF3
```

### 87 · 岭回归选币（机器学习）

“用机器学习组合多个因子选币”。规则：12 个特征按周排名，滚动训练岭回归预测下一周的排名，做多最高的 3 个、做空最低的 3 个。（[档案](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/87_ML1_ridge_weekly.md)）

- **扣成本后年化 +17.0%（t 1.32）。** 夏普 0.58，累计最大回撤 −55%（按天相加）；291 周，平均每次调仓换手 0.70，资金费每年 −3.3%。
- **排名有预测力，组合却不显著（登记之外）。** 分数和下一周涨跌的排名相关 0.132（t 5.27，290 周），验证段 0.140（t 3.68）；但多减空 3 个币每周平均 +0.78%（t 1.51，不扣成本），中位数 +1.64%，63% 的周为正，最差一周 −33%。排名相关最强的单个特征都是“低风险”一类：30 天波动率低（0.126，t 4.47）、60 天贝塔低（0.128，t 4.53）、流动性好（0.107，t 5.10）、30 天最大单日涨幅小（0.108，t 4.35）——低波动、大市值的币多数周排名靠前，但被做空的高波动小币偶尔一周暴涨，把平均收益吃掉。
- **和随手选币比：** 20 个随机组合年化 −10.0%，超出 +27.0%（t 1.97）；不扣手续费，超出 +23.1%（t 1.69）。
- **训练段年化 +30.0%（t 1.70），验证段 +4.3%（t 0.23）。**
- **邻近变体：** λ = 0.1 × 样本数 +22.9%（t 1.76），只用最近 104 周训练 +3.1%（t 0.23），多空各 2 个 +15.7%（t 1.08），每 4 周重新训练 +18.3%（t 1.41）；压力测试 成本翻倍 +13.3%（t 1.03），晚一天调仓 +13.7%（t 1.07）。

```bash
git clone https://github.com/runningshark/orderflow_ml_macro_failureprove
cd orderflow_ml_macro_failureprove
py verify.py ML1
```

### 88 · 梯度提升树选币（机器学习）

同上，模型换成梯度提升树（100 棵、深度 2、学习率 0.05，事先固定）。（[档案](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/88_ML2_gbm_weekly.md)）

- **扣成本后年化 +2.3%（t 0.18）。** 夏普 0.08，累计最大回撤 −58%（按天相加）；291 周，平均每次调仓换手 0.79，资金费每年 −3.2%。
- **排名有预测力，组合不赚钱（登记之外）。** 排名相关 0.126（t 5.33），验证段 0.147（t 4.09）；多减空 3 个币每周平均 +0.23%（t 0.45），中位数 +1.31%，最差一周 −41%。
- **和随手选币比：** 20 个随机组合年化 −7.9%，超出 +10.2%（t 0.78）；不扣手续费，超出 +6.9%（t 0.53）。
- **训练段年化 −3.5%（t −0.19），验证段 +8.0%（t 0.44）。**
- **邻近变体：** 200 棵树 +2.5%（t 0.19），深度 3 −0.4%（t −0.03），只用最近 104 周训练 −11.4%（t −0.90），多空各 2 个 +12.3%（t 0.79）；压力测试 成本翻倍 −1.8%（t −0.14），晚一天调仓 +2.8%（t 0.22）。

```bash
git clone https://github.com/runningshark/orderflow_ml_macro_failureprove
cd orderflow_ml_macro_failureprove
py verify.py ML2
```

### 89 · BTC 隐含波动率飙升后做多

“恐慌指数飙升是买点”。规则：BTC 隐含波动率指数 BVOL 高于前 90 天的第 90 百分位，做多 BTC，拿 7 天。（[档案](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/89_V1_bvol_spike_long.md)）

- **扣成本后每笔 +1.05%（t 0.97）。** 32 笔（每年约 9 笔），胜率 59%，平均赚 5.46%、亏 5.38%；不扣成本每笔 +1.25%，成本 0.20%。
- **样本太小。** 拿 7 天不重叠，2023-06 到 2026-10 只有 32 笔。
- **和随手进场比：** 随手进场平均 +0.23%，真实的 +1.25%，超出 +1.02%（t 0.90）；训练段超出 +1.05%，验证段 +0.99%。
- **训练段每笔 +2.63%（t 1.84，18 笔），验证段 −0.97%（t −0.60，14 笔）。**
- **邻近变体：** 第 80 百分位 54 笔 +1.21%（t 1.34），第 95 百分位 25 笔 +2.75%（t 2.29），拿 3 天 53 笔 +0.33%（t 0.58），拿 14 天 23 笔 +2.40%（t 1.29）；压力测试 成本翻倍 +0.85%（t 0.79），晚一天进场 +1.30%（t 1.21）。

```bash
git clone https://github.com/runningshark/orderflow_ml_macro_failureprove
cd orderflow_ml_macro_failureprove
py verify.py V1
```

### 90 · 波动率风险溢价为正时持有 BTC

“波动率风险溢价为正时风险资产更好”。规则：BVOL 高于 BTC 30 天的已实现波动率就持有 BTC，否则空仓。（[档案](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/90_V2_vrp_timing.md)）

- **择时超额 +1.4%（年化，t 0.18）。** 满仓 80% 的时间，进出 51 次；一块钱变成 2.40，一直持有是 2.74；夏普 0.83 对 0.88，最大回撤 −50% 对 −53%。
- **持有的时间太多，和一直持有差不多。** 溢价为正的日子约占 80%；已实现波动率换成 14 天、60 天，择时超额变成 −12.4%、−16.8%。
- **训练段 +11.2%（t 0.89），验证段 −9.7%（t −0.87）；平移检验 p = 0.39（870 种平移）。** 持有的日子 BTC 年化 +44.9%（波动 46%），空仓的日子 +21.7%（波动 43%）。
- **邻近变体：** 已实现波动率用 14 天 −12.4%（t −1.38），用 60 天 −16.8%（t −1.84），溢价 > 5 才持有 −3.6%（t −0.34），溢价高于前 90 天的中位数 +10.9%（t 0.89）；压力测试 成本翻倍 −0.1%（t −0.01），指标再晚一天 −6.6%（t −0.79）。

```bash
git clone https://github.com/runningshark/orderflow_ml_macro_failureprove
cd orderflow_ml_macro_failureprove
py verify.py V2
```

### 91 · 实际利率下降时持有 BTC

“实际利率下降利好 BTC”。规则：美国 10 年期实际收益率比 20 个观测前低就持有 BTC，否则空仓。（[档案](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/91_M1_real_yield_timing.md)）

- **择时超额 +1.3%（年化，t 0.12）。** 满仓 48% 的时间，进出 225 次；一块钱变成 4.25，一直持有是 16.42；夏普 0.58 对 0.80，最大回撤 −55% 对 −83%。
- **大约一半时间空仓，错过了大部分涨幅。** 按承担的波动算没有超额，邻近变体有正有负。
- **训练段 +6.6%（t 0.45），验证段 −10.2%（t −0.81）；平移检验 p = 0.35（2,989 种平移）。** 持有的日子 BTC 年化 +61.3%（波动 67%），空仓的日子 +45.4%（波动 66%）。
- **邻近变体：** 和第 10 个观测前比 +9.4%（t 0.83），和第 60 个观测前比 +21.5%（t 1.90），用 5 年期 −1.5%（t −0.14），低于最近 50 个观测的平均 +9.1%（t 0.79）；压力测试 成本翻倍 −1.2%（t −0.11），指标再晚一天 −6.6%（t −0.59）。

```bash
git clone https://github.com/runningshark/orderflow_ml_macro_failureprove
cd orderflow_ml_macro_failureprove
py verify.py M1
```

### 92 · 美元走弱时持有 BTC

“美元走弱利好 BTC”。规则：名义广义美元指数（只用 10 天以前的数据）低于 50 日均线就持有 BTC，否则空仓。（[档案](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/92_M2_dollar_timing.md)）

- **择时超额 +5.2%（年化，t 0.46）。** 满仓 47% 的时间，进出 152 次；一块钱变成 6.41，一直持有是 16.42；夏普 0.67 对 0.80，最大回撤 −60% 对 −83%。
- **大约一半时间空仓，错过了大部分涨幅。** 邻近变体有正有负（用 100 个观测的平均 +19.6%，和第 20 个观测前比 −17.2%）。
- **训练段 +8.6%（t 0.56），验证段 −2.4%（t −0.18）；平移检验 p = 0.25（2,989 种平移）。** 持有的日子 BTC 年化 +69.7%（波动 68%），空仓的日子 +38.2%（波动 66%）。
- **邻近变体：** 20 个观测的平均 −8.3%（t −0.69），100 个观测的平均 +19.6%（t 1.76），和第 20 个观测前比 −17.2%（t −1.55），只用 t−14 天及以前的值 +6.7%（t 0.59）；压力测试 成本翻倍 +3.6%（t 0.31），指标再晚一天 +6.3%（t 0.54）。

```bash
git clone https://github.com/runningshark/orderflow_ml_macro_failureprove
cd orderflow_ml_macro_failureprove
py verify.py M2
```

### 93 · FOMC 公布前 24 小时做多 BTC

“议息前漂移”（Lucca 和 Moench，2015）。规则：FOMC 声明公布前 24 小时做多 BTC 现货，公布那一刻平仓。第七轮（第 39 条）用永续合约测过同一个说法，这一轮登记时没有注意到重复。（[档案](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/93_M3_pre_fomc_drift.md)）

- **扣成本后每笔 +0.49%（t 1.31）。** 73 笔（每年约 8 笔），胜率 58%，平均赚 2.43%、亏 2.13%；不扣成本每笔 +0.69%，成本 0.20%。
- **只来自 2020 年。** 2020 年的 7 次每笔 +4.58%；去掉 2020 年剩下 66 次每笔 +0.06%，胜率 53%（登记之外）。第七轮（合集第 39 条）已经用 BTC 永续测过同一个说法（2020–2026 年，结论一样）；这一轮登记时没有注意到重复，这次用现货、往前加了 2017–2019 年的 19 次，那几次每笔平均 +0.07%，也没有漂移。
- **和随手进场比：** 随手进场平均 +0.06%，真实的 +0.69%，超出 +0.63%（t 1.66）；训练段超出 +0.96%，验证段 −0.08%。
- **训练段每笔 +0.87%（t 1.70，50 笔），验证段 −0.32%（t −0.71，23 笔）。**
- **邻近变体：** 公布前 12 小时进场 73 笔 +0.35%（t 1.21），公布前 48 小时进场 73 笔 +0.29%（t 0.55），公布后 2 小时才平仓 73 笔 +0.50%（t 1.21），拿到公布那天的 UTC 收盘 73 笔 +0.88%（t 1.96）；压力测试 成本翻倍 +0.29%（t 0.78），晚一根进场 +0.65%（t 1.75）。

```bash
git clone https://github.com/runningshark/orderflow_ml_macro_failureprove
cd orderflow_ml_macro_failureprove
py verify.py M3
```

### 94 · 恐惧贪婪指数

“别人恐惧时贪婪”。规则：恐惧贪婪指数 ≤ 25（极度恐惧）买入 BTC，≥ 76（极度贪婪）卖出。（[档案](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/94_S1_fear_greed_timing.md)）

- **择时超额 −17.1%（年化，t −1.84）。** 满仓 71% 的时间，进出 16 次；一块钱变成 0.94，一直持有是 7.54；夏普 0.26 对 0.69，最大回撤 −78% 对 −77%。
- **卖在“极度贪婪”会错过大段牛市。** 空仓的日子 BTC 年化涨 +99.9%，持有的日子只有 +19.9%；最长的一段空仓是 2020-07-28 到 2021-05-15（BTC 从 10,906 涨到 46,763）。4 个变体全部为负。
- **训练段 −22.2%（t −1.85），验证段 −4.9%（t −0.37）；平移检验 p = 0.96（2,836 种平移）。** 持有的日子 BTC 年化 +19.9%（波动 63%），空仓的日子 +99.9%（波动 62%）。
- **邻近变体：** 20 / 80 −6.7%（t −0.77），30 / 70 −22.0%（t −2.24），用 7 天平均 −6.9%（t −0.68），到“贪婪”（≥ 55）就卖 −19.6%（t −1.93）；压力测试 成本翻倍 −17.2%（t −1.86），指标再晚一天 −15.9%（t −1.66）。

```bash
git clone https://github.com/runningshark/orderflow_ml_macro_failureprove
cd orderflow_ml_macro_failureprove
py download_data.py fng && py build_data.py fng
py verify.py S1
```

### 95 · BTC 市占率趋势

“BTC 市占率下降就是山寨季”。规则：市占率 30 天降了 2 个百分点以上，做多山寨篮子、做空 BTC，拿 7 天；升了 2 个百分点以上反过来。（[档案](https://github.com/runningshark/orderflow_ml_macro_failureprove/blob/master/reports/95_D1_btc_dominance_trend.md)）

- **扣成本后每笔 −0.50%（t −0.81）。** 136 笔（每年约 22 笔），胜率 47%，平均赚 5.43%、亏 5.78%；不扣成本每笔 −0.10%，成本 0.40%。
- **顺着市占率做是亏的。** 市占率下降时做多山寨 61 笔每笔 +0.48%，上升时做多 BTC 75 笔每笔 −1.30%；82% 的信号日和“山寨篮子 30 天比 BTC 涨得多（少）”同时出现，和第十四轮 H4（用价格、方向相反）是同一个信息，两个都不行。
- **和随手进场比：** 随手进场平均 +0.07%，真实的 −0.10%，超出 −0.17%（t −0.27）；训练段超出 +0.24%，验证段 −1.11%。
- **训练段每笔 −0.02%（t −0.02，94 笔），验证段 −1.59%（t −1.49，42 笔）。**
- **邻近变体：** 门槛 1 个百分点 229 笔 −0.62%（t −1.42），门槛 3 个百分点 83 笔 −0.32%（t −0.44），用 60 天的变化 183 笔 −0.54%（t −1.11），拿 14 天 83 笔 −0.71%（t −0.64）；压力测试 成本翻倍 −0.90%（t −1.46），晚一天进场 −0.86%（t −1.47）。

```bash
git clone https://github.com/runningshark/orderflow_ml_macro_failureprove
cd orderflow_ml_macro_failureprove
py verify.py D1
```

### 96–98 · 第十六轮事先登记的研究：BTC 周期指标和月份季节性（共用一个仓库）

只用价格算的“周期顶底”指标（梅耶倍数、Pi 周期、两年均线乘数、减半周期）和月份季节性（五月卖出、十月必涨），都是 BTC 满仓 / 空仓的择时规则。规则和通过标准同样是事先登记的（[事先登记_第十六轮.md](https://github.com/runningshark/d1_btc_cycle_seasonality_failureprove/blob/master/事先登记_第十六轮.md)）。**登记 6 个，3 个失败**；另外 3 个（Pi 周期、减半周期、十月必涨）没有被判为失败，不在合集里。

- 累计 93 个候选，门槛是 t ≥ 3.5。Coin Metrics 社区数据的 BTC 每日价格，2013-01 到 2026-05，训练段到 2019 年底。每次进出 0.10%。统计量和第 49–53 条相同：择时超额和平移检验。
- 梅耶倍数两次卖早了、买贵了；两年均线乘数的 5 倍线 2021 年没碰到，之后一直满仓；冬半年和夏半年差不多。
- 这 3 条共用一个仓库 [d1_btc_cycle_seasonality_failureprove](https://github.com/runningshark/d1_btc_cycle_seasonality_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/d1_btc_cycle_seasonality_failureprove/blob/master/FAILURE_REPORT.md)。数据来自 Coin Metrics（CC BY-NC 4.0）。

### 96 · 梅耶倍数（BTC）

“梅耶倍数（价格 ÷ 200 日均线）高于 2.4 是过热”。规则：高于 2.4 卖出，回到 1.0 以下买回。（[档案](https://github.com/runningshark/d1_btc_cycle_seasonality_failureprove/blob/master/reports/96_P1_mayer_multiple.md)）

- **择时超额 +13.4%（年化，t 1.19）。** 满仓 85% 的时间，2013 年到 2026-05 进出 10 次；一块钱变成 863，一直持有是 5,656；夏普 1.17 对 1.23，最大回撤 −77% 对 −85%。
- **卖早了、买贵了。** 进出：2013-03-05 卖（41 美元）；2013-07-06 买（66 美元）；2013-11-08 卖（334 美元）；2014-03-28 买（499 美元）；2017-06-07 卖（2,707 美元）；2018-02-06 买（7,739 美元）；2019-06-27 卖（11,110 美元）；2019-09-27 买（8,187 美元）；2021-01-04 卖（31,802 美元）；2021-05-20 买（40,799 美元）。2017 年和 2021 年两次都是卖出以后价格继续涨，买回来比卖出的价格高。
- **验证段（2020 年起）没有超额：** +0.8%（t 0.09）；训练段 +26.2%（t 1.43）；平移检验 p = 0.11（4,532 种平移）。
- **邻近变体：** 2.0 / 1.0 +7.4%（t 0.65），2.8 / 1.0 +21.9%（t 2.00），2.4 / 0.8 +8.7%（t 0.77），2.4 / 1.2 +6.8%（t 0.62）；压力测试 成本翻倍 +13.3%（t 1.19），晚一天 +15.6%（t 1.38）。
- **换起点、拿掉一段时期都不显著（登记之外）：** 2014 年 t 0.58、2015 年 t 0.39、2016 年 t 0.43、2017 年 t 0.26、2018 年 t 1.54；拿掉 2013–2015 t 0.44、拿掉 2016–2019 t 1.05、拿掉 2020–2022 t 1.57、拿掉 2023–2026 t 1.02。

```bash
git clone https://github.com/runningshark/d1_btc_cycle_seasonality_failureprove
cd d1_btc_cycle_seasonality_failureprove
py verify.py P1
```

### 97 · 两年均线乘数（BTC）

“价格高于两年均线的 5 倍是顶，低于两年均线是底”（Philip Swift）。规则：5 倍卖出，回到两年均线以下买回。（[档案](https://github.com/runningshark/d1_btc_cycle_seasonality_failureprove/blob/master/reports/97_P3_two_year_ma_multiplier.md)）

- **择时超额 +12.8%（年化，t 1.12）。** 满仓 79% 的时间，2013 年到 2026-05 进出 4 次；一块钱变成 679，一直持有是 5,656；夏普 1.14 对 1.23，最大回撤 −77% 对 −85%。
- **2021 年价格没有碰到两年均线的 5 倍，2018-11 以后一直满仓。** 进出：2013-03-10 卖（46 美元）；2014-11-02 买（324 美元）；2017-09-02 卖（4,595 美元）；2018-11-16 买（5,496 美元）。验证段（2020 年起）和一直持有完全一样（所以没有 t）；训练段 +26.3%（t 1.53）；平移检验 p = 0.11（4,532 种平移）。
- **邻近变体：** 4 倍 / 1 倍 +16.9%（t 1.52），6 倍 / 1 倍 +18.9%（t 1.69），5 倍 / 0.8 倍 +16.7%（t 1.47），5 倍 / 1.2 倍 +10.1%（t 0.89）；压力测试 成本翻倍 +12.8%（t 1.12），晚一天 +13.1%（t 1.15）。
- **换起点、拿掉一段时期都不显著（登记之外）：** 2014 年 t 1.69、2015 年 t 0.91、2016 年 t 0.93、2017 年 t 0.80、2018 年 t 1.68；拿掉 2013–2015 t 0.95、拿掉 2016–2019 t 0.56、拿掉 2020–2022 t 1.66、拿掉 2023–2026 t 0.95。

```bash
git clone https://github.com/runningshark/d1_btc_cycle_seasonality_failureprove
cd d1_btc_cycle_seasonality_failureprove
py verify.py P3
```

### 98 · 五月卖出（Sell in May，BTC）

“五月卖出，十一月回来”（Sell in May）。规则：只在 11 月到 4 月持有 BTC。（[档案](https://github.com/runningshark/d1_btc_cycle_seasonality_failureprove/blob/master/reports/98_S1_sell_in_may.md)）

- **择时超额 −0.2%（年化，t −0.02）。** 满仓 51% 的时间，2013 年到 2026-05 进出 28 次；一块钱变成 303，一直持有是 5,656；夏普 1.00 对 1.23，最大回撤 −79% 对 −85%。
- **冬半年和夏半年差不多。** 持有的日子 BTC 年化 +123.7%，空仓的日子 +63.5%，但按承担的波动算没有超额；训练段 −8.0%（t −0.49），验证段 +8.1%（t 0.67）；平移检验（去掉月份又对齐的平移）p = 0.37（3,066 种）。
- **邻近变体：** 10 月到 4 月 +13.0%（t 1.32），11 月到 5 月 +1.0%（t 0.10），12 月到 4 月 −9.2%（t −0.81），11 月到 3 月 −0.3%（t −0.02）；压力测试 成本翻倍 −0.4%（t −0.04），晚一天 −2.2%（t −0.21）。
- **换起点、拿掉一段时期都不显著（登记之外）：** 2014 年 t −0.61、2015 年 t −0.50、2016 年 t −0.29、2017 年 t −0.27、2018 年 t 0.16；拿掉 2013–2015 t −0.28、拿掉 2016–2019 t 0.73、拿掉 2020–2022 t −0.44、拿掉 2023–2026 t −0.04。

```bash
git clone https://github.com/runningshark/d1_btc_cycle_seasonality_failureprove
cd d1_btc_cycle_seasonality_failureprove
py verify.py S1
```

### 99–103 · 第十七轮事先登记的研究：52 周高点、残差动量和残差反转、USDT 增发、现货带动的大涨（共用一个仓库）

离 52 周高点越近越做多、去掉大盘以后的动量和一周反转（每周多空组合），USDT 增发后做多 BTC、一天大涨以后看现货还是合约带动（事件类）。规则和通过标准同样是事先登记的（[事先登记_第十七轮.md](https://github.com/runningshark/resid_mom_usdt_failureprove/blob/master/事先登记_第十七轮.md)）。**登记 5 个，5 个失败**。

- 累计 98 个候选，门槛是 t ≥ 3.5。币安 U 本位永续合约的日线、对应现货的日成交额（Binance Vision）；Coin Metrics 社区数据的 USDT 流通量。每个季度按成交额选 10 个币，2020-04 到 2026-10，训练段到 2023 年底。每边成本 0.10%，资金费照算。
- 周度组合和**随手选币**比；事件类和**随手进场**比。
- 52 周高点最接近（超出随手选币 t 2.47），但训练段不显著、和普通动量有不少重合；去掉大盘以后的动量、反转都没有；USDT 增发多发生在牛市，增发后的涨幅和随手进场差不多；现货带动和合约带动的大涨之后没有区别。
- 这 5 条共用一个仓库 [resid_mom_usdt_failureprove](https://github.com/runningshark/resid_mom_usdt_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/resid_mom_usdt_failureprove/blob/master/FAILURE_REPORT.md)。数据许可见仓库的 data/README.md。

### 99 · 52 周高点

“离 52 周高点越近越强”（George 和 Hwang，2004）。规则：每周按收盘价 ÷ 365 天最高价，做多最高的 3 个币、做空最低的 3 个。（[档案](https://github.com/runningshark/resid_mom_usdt_failureprove/blob/master/reports/99_X1_52w_high_weekly.md)）

- **扣成本后年化 +22.4%（t 1.86）。** 夏普 0.69，累计最大回撤 −54%（按天相加）；343 周（有 6 个以上分数的 329 周），平均每次调仓换手 0.39，资金费每年 −3.2%（负数是收到）。
- **主要来自做空那边，和普通动量有不少重合（登记之外）。** 多头一边（相对当周 10 个币的等权平均，不扣成本）年化 +10.1%（t 0.66），空头一边 +18.5%（t 1.43）；分数和过去 28 天涨幅的排名相关 0.43、和 90 天的 0.49（合集第 14–16 条的横截面动量都失败了）。每周超出随手选币的平均 +0.59%、中位数 +0.59%，不是靠少数几周；组合每年还收到 3.2% 的资金费（做空的 3 个币资金费平均年化 10.7%，做多的 5.5%）。2022 年 −17.8%。
- **和随手选币比：** 20 个随机组合年化 −8.3%（不扣手续费 −1.2%），超出 +30.8%（t 2.47）；不扣手续费，超出 +25.5%（t 2.05）。
- **训练段年化 +11.9%（t 0.74），验证段 +36.3%（t 2.04）；超出随手选币 训练段 +19.9%，验证段 +45.0%。**
- **邻近变体：** 用过去 180 天的最高价 +23.7%（t 1.85），用上线以来的最高价 +16.7%（t 1.42），多空各 2 个 +19.4%（t 1.33），每两周调一次仓 +20.5%（t 1.83）；压力测试 成本翻倍 +20.5%（t 1.70），晚一天调仓 +25.5%（t 2.19）。

```bash
git clone https://github.com/runningshark/resid_mom_usdt_failureprove
cd resid_mom_usdt_failureprove
py verify.py X1
```

### 100 · 残差动量（去掉大盘）

“去掉大盘以后的动量更稳”（Blitz、Huij 和 Martens，2011）。规则：每周按最近 28 天的残差之和 ÷ 残差的标准差（对币池等权平均回归，90 天），做多最高的 3 个、做空最低的 3 个。（[档案](https://github.com/runningshark/resid_mom_usdt_failureprove/blob/master/reports/100_X2_residual_momentum_weekly.md)）

- **扣成本后年化 +1.5%（t 0.12）。** 夏普 0.05，累计最大回撤 −78%（按天相加）；343 周（有 6 个以上分数的 343 周），平均每次调仓换手 0.82，资金费每年 −0.8%（负数是收到）。
- **多头、空头两边都不显著（登记之外）。** 多头一边（相对当周 10 个币的等权平均，不扣成本）年化 +11.4%（t 0.80），空头一边 +8.0%（t 0.52）。
- **和随手选币比：** 20 个随机组合年化 −6.5%（不扣手续费 +1.0%），超出 +8.0%（t 0.66）；不扣手续费，超出 +4.8%（t 0.39）。
- **训练段年化 +5.2%（t 0.28），验证段 −3.4%（t −0.22）；超出随手选币 训练段 +13.5%，验证段 +0.8%。**
- **邻近变体：** 残差之和用最近 56 天 +8.0%（t 0.68），用最近 14 天 +7.9%（t 0.63），回归用过去 180 天 +10.9%（t 0.88），多空各 2 个 −15.4%（t −0.99）；压力测试 成本翻倍 −2.8%（t −0.23），晚一天调仓 +7.0%（t 0.58）。

```bash
git clone https://github.com/runningshark/resid_mom_usdt_failureprove
cd resid_mom_usdt_failureprove
py verify.py X2
```

### 101 · 残差短期反转（去掉大盘）

“去掉大盘以后，上一周跌得最多的反弹”。规则：残差同 X2，按最近 7 天的残差之和（取负号）排名，做多上一周相对大盘跌得最多的 3 个、做空涨得最多的 3 个。（[档案](https://github.com/runningshark/resid_mom_usdt_failureprove/blob/master/reports/101_X3_residual_reversal_weekly.md)）

- **扣成本后年化 −15.6%（t −1.26）。** 夏普 −0.49，累计最大回撤 −127%（按天相加）；343 周（有 6 个以上分数的 343 周），平均每次调仓换手 1.42，资金费每年 −0.4%（负数是收到）。
- **方向反了：上一周相对大盘跌得多的，下一周继续偏弱；但反过来做也付不起成本。** 扣成本前年化 −8.2%，每次调仓换手 1.42，一年的手续费大约 7.4%。
- **和随手选币比：** 20 个随机组合年化 −4.2%（不扣手续费 +3.3%），超出 −11.3%（t −0.91）；不扣手续费，超出 −11.5%（t −0.92）。
- **训练段年化 −30.6%（t −1.81），验证段 +4.3%（t 0.24）；超出随手选币 训练段 −28.8%，验证段 +11.7%。**
- **邻近变体：** 残差之和用最近 3 天 −8.2%（t −0.69），用最近 14 天 −18.5%（t −1.48），回归用过去 180 天 −19.3%（t −1.62），多空各 2 个 −25.1%（t −1.64）；压力测试 成本翻倍 −23.0%（t −1.86），晚一天调仓 −24.3%（t −2.06）。

```bash
git clone https://github.com/runningshark/resid_mom_usdt_failureprove
cd resid_mom_usdt_failureprove
py verify.py X3
```

### 102 · USDT 增发后做多 BTC

“Tether 一印钱，BTC 就涨”。规则：USDT 的流通量前一天比再前一天多 0.5% 以上，当天收盘做多 BTC 永续合约，拿 7 天。（[档案](https://github.com/runningshark/resid_mom_usdt_failureprove/blob/master/reports/102_E1_usdt_mint_long_btc.md)）

- **扣成本后每笔 +1.79%（t 2.39）。** 122 笔（每年约 20 笔），胜率 59%，平均赚 6.63%、亏 5.16%；不扣成本每笔 +1.99%，成本 0.20%。
- **增发多发生在牛市，只是赶上了 BTC 在涨。** 2020-04 到 2026-05 之间任意一天买 BTC 拿 7 天平均 +1.07%；增发后的 7 天（扣成本前）+1.99%，前后 30 天随手进场 +1.37%。122 笔里 2020、2021 年有 49 笔。按增发幅度分（登记之外）：0.5%–1% 的 46 笔超出 +1.08%，1%–2% 的 57 笔超出 +0.23%，2% 以上的 19 笔超出 +0.69%，增发越多不是涨得越多。
- **和随手进场比：** 随手进场平均 +1.37%，真实的 +1.99%，超出 +0.62%（t 0.87）；训练段超出 +0.53%，验证段 +0.76%。
- **训练段每笔 +2.28%（t 2.07，73 笔），验证段 +1.07%（t 1.22，49 笔）。**
- **邻近变体：** 门槛 0.2% 126 笔 +1.72%（t 2.36），门槛 1% 84 笔 +1.43%（t 1.54），拿 3 天 175 笔 +0.88%（t 2.22），拿 14 天 87 笔 +2.61%（t 2.10）；压力测试 成本翻倍 +1.59%（t 2.13），晚一天进场 +1.67%（t 2.24）。

```bash
git clone https://github.com/runningshark/resid_mom_usdt_failureprove
cd resid_mom_usdt_failureprove
py verify.py E1
```

### 103 · 现货带动还是合约带动的大涨

“现货带动的上涨更持久，合约拉的盘会跌回去”。规则：一天涨 5% 以上，现货成交额占比高于前 30 天的平均就做多、低于平均就做空，拿 3 天。（[档案](https://github.com/runningshark/resid_mom_usdt_failureprove/blob/master/reports/103_E2_spot_vs_perp_led_pumps.md)）

- **扣成本后每笔 +0.03%（t 0.11）。** 1,811 笔（每年约 275 笔），胜率 50%，平均赚 7.49%、亏 7.51%；不扣成本每笔 +0.23%，成本 0.20%。
- **两种大涨之后价格都还在小幅上涨，合约拉的盘没有跌回去。** 现货带动的做多 966 笔每笔 +0.66%（超出随手进场 +0.21%），合约带动的做空 845 笔 −0.68%（超出 −0.20%）。（登记之外）不分现货、合约一律做多拿 3 天，1,811 笔每笔 +0.48%（t 1.07），超出随手进场 +0.23%（t 0.53）；按“当天现货占比 − 前 30 天平均”分 5 组，做多拿 3 天（扣成本前）分别是 −0.05%、+0.91%、+0.87%、+1.07%、+0.60%，没有单调的关系。
- **和随手进场比：** 随手进场平均 +0.21%，真实的 +0.23%，超出 +0.02%（t 0.07）；训练段超出 −0.07%，验证段 +0.16%。
- **训练段每笔 −0.01%（t −0.02，1,112 笔），验证段 +0.10%（t 0.22，699 笔）。**
- **邻近变体：** 门槛 8% 938 笔 −0.26%（t −0.53），门槛 10% 630 笔 −0.56%（t −0.91），拿 1 天 2,267 笔 −0.32%（t −2.02），拿 7 天 1,328 笔 +0.12%（t 0.23）；压力测试 成本翻倍 −0.17%（t −0.57），晚一天进场 +0.12%（t 0.45）。

```bash
git clone https://github.com/runningshark/resid_mom_usdt_failureprove
cd resid_mom_usdt_failureprove
py verify.py E2
```

### 104–109 · 第十八轮事先登记的研究：广度推力、美国 M2、订单簿买卖盘、资金费结算前、春节前（共用一个仓库）

广度推力后做多 BTC、订单簿极端失衡跟着做、资金费高时结算前做空（事件类），美国 M2、订单簿买盘厚、春节前空仓（BTC 择时）。规则和通过标准同样是事先登记的（[事先登记_第十八轮.md](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/事先登记_第十八轮.md)）。**登记 6 个，6 个失败**。

- 累计 104 个候选，门槛是 t ≥ 3.5。币安的合约日线、1 小时 K 线、资金费、BTC 现货日线、BTCUSDT 和 ETHUSDT 的订单簿深度（Binance Vision）；美联储理事会 H.6 的 M2；Coin Metrics 社区数据的 BTC 价格。每边成本 0.10%，资金费照算。
- 事件类和**随手进场**比；BTC 的满仓 / 空仓择时看**择时超额**和**平移检验**（和第九、十六轮相同）。
- 订单簿的买卖失衡对第二天的涨跌没有预测力；资金费高时结算前没有抛压，结算开始的那 1 小时反而在涨；美国 M2 的规则错过了 2023 年的上涨；春节前 14 天 BTC 14 年里涨了 9 年。
- 这 6 条共用一个仓库 [m2_orderbook_cny_failureprove](https://github.com/runningshark/m2_orderbook_cny_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/FAILURE_REPORT.md)。数据许可见仓库的 data/README.md。

### 104 · 广度推力后做多 BTC

“广度推力之后有一段上涨”（Zweig）。规则：币池 10 个币的上涨家数比例，10 天指数平均在 10 天之内从 40% 以下升到 61.5% 以上，做多 BTC 30 天。（[档案](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/reports/104_B1_breadth_thrust_long_btc.md)）

- **扣成本后每笔 +2.04%（t 0.63）。** 36 笔（每年约 5 笔），胜率 53%，平均赚 16.18%、亏 13.75%；不扣成本每笔 +2.24%，成本 0.20%。
- **信号之后 30 天平均是涨的，但随手挑一天买涨得更多。** 每笔中位数 +1.28%；广度的比例只能是 0、0.1、…、1（币池只有 10 个币），指数平均在 40% 和 61.5% 之间来回很常见，6 年半有 36 次“推力”，不像股票里那样罕见。
- **和随手进场比：** 随手进场平均 +3.08%，真实的 +2.24%，超出 −0.84%（t −0.32）；训练段超出 +0.46%，验证段 −2.88%。
- **训练段每笔 +4.26%（t 0.85，22 笔），验证段 −1.45%（t −0.53，14 笔）。**
- **邻近变体：** 拿 10 天 45 笔 +1.18%（t 0.90），拿 60 天 25 笔 +8.44%（t 1.40），门槛 0.45 / 0.60 54 笔 +3.36%（t 1.24），15 天之内 42 笔 +2.71%（t 0.87）；压力测试 成本翻倍 +1.84%（t 0.57），晚一天进场 +1.20%（t 0.40）。

```bash
git clone https://github.com/runningshark/m2_orderbook_cny_failureprove
cd m2_orderbook_cny_failureprove
py verify.py B1
```

### 105 · 美国 M2 增长时持有 BTC（滞后 70 天）

“BTC 跟着 M2 走，滞后 10 周”。规则：美国 M2（滞后 70 天）比 3 个月前高就持有 BTC，否则空仓。（[档案](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/reports/105_M4_us_m2_lag_timing.md)）

- **择时超额 −2.9%（年化，t −0.64）。** 满仓 89% 的时间，进出 5 次；一块钱变成 2,559，一直持有是 5,656；夏普 1.16 对 1.23，最大回撤 −85% 对 −85%。
- **规则只空过两段仓，正好错过 2023 年的上涨（登记之外）。** 进出：2022-08-09 卖（23,186 美元）；2023-10-09 买（27,591 美元）；2023-11-09 卖（36,675 美元）；2024-03-10 买（68,882 美元）。2023 年规则 +33%、一直持有 +155%；2024 年 +35%、+121%。M2 的 3 个月增长 2012 年以后只有 2022-05 到 2023-11（2023-07 除外）是负的。
- **训练段 +0.2%（t 1.00），验证段 −6.9%（t −0.76）；平移检验 p = 0.60（4,532 种平移）。** 持有的日子 BTC 年化 +97.7%（波动 79%），空仓的日子 +64.4%（波动 49%）。
- **邻近变体：** 滞后 30 天 −2.9%（t −0.64），滞后 100 天 −4.8%（t −1.04），和 6 个月前比 −8.4%（t −2.00），和 1 个月前比 −6.6%（t −1.53）；压力测试 成本翻倍 −3.0%（t −0.65），数据再晚一天 −2.9%（t −0.62）。

```bash
git clone https://github.com/runningshark/m2_orderbook_cny_failureprove
cd m2_orderbook_cny_failureprove
py verify.py M4
```

### 106 · 订单簿买盘厚时持有 BTC

“买盘墙在下面，价格要涨”。规则：BTCUSDT 永续订单簿 1% 以内的买单金额多于卖单，第二天持有 BTC，否则空仓。（[档案](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/reports/106_OB1_orderbook_bid_heavy_timing.md)）

- **择时超额 −12.5%（年化，t −1.13）。** 满仓 61% 的时间，进出 590 次；一块钱变成 1.65，一直持有是 4.69；夏普 0.54 对 1.10，最大回撤 −46% 对 −53%。
- **失衡对第二天的涨跌没有预测力，换仓又太多（登记之外）。** 当天 1% 以内的失衡和第二天 BTC 涨跌的排名相关 0.012（t 0.43），2% 以内 -0.001，5% 以内 0.029（t 1.09）；不扣成本的择时超额 +2.8%（t 0.25），进出 590 次，一年的成本大约 15%。
- **训练段 −21.0%（t −1.25），验证段 −1.8%（t −0.13）；平移检验 p = 0.40（1,041 种平移）。** 持有的日子 BTC 年化 +57.7%（波动 47%），空仓的日子 +40.3%（波动 45%）。
- **邻近变体：** 用 2% 以内 −16.1%（t −1.39），用 5% 以内 +6.7%（t 0.67），高于前 30 天的中位数 −11.4%（t −0.94），最近 3 天的平均 +0.2%（t 0.02）；压力测试 成本翻倍 −27.8%（t −2.55），数据再晚一天 −6.3%（t −0.63）。

```bash
git clone https://github.com/runningshark/m2_orderbook_cny_failureprove
cd m2_orderbook_cny_failureprove
py verify.py OB1
```

### 107 · 订单簿极端失衡跟着做

“订单簿极端失衡跟着做”。规则：BTC、ETH 的买卖失衡偏离前 30 天 ±2 个标准差，跟着失衡的方向做 3 天。（[档案](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/reports/107_OB2_orderbook_extreme_imbalance.md)）

- **扣成本后每笔 +0.15%（t 0.38）。** 154 笔（每年约 40 笔），胜率 53%，平均赚 3.29%、亏 3.34%；不扣成本每笔 +0.35%，成本 0.20%。
- **做多、做空都只比随手进场好一点点。** 做多 69 笔每笔 +0.81%（超出随手进场 +0.25%），做空 85 笔 −0.39%（超出 +0.21%）。
- **和随手进场比：** 随手进场平均 +0.12%，真实的 +0.35%，超出 +0.23%（t 0.54）；训练段超出 −0.10%，验证段 +0.62%。
- **训练段每笔 −0.20%（t −0.36，83 笔），验证段 +0.55%（t 0.98，71 笔）。**
- **邻近变体：** 门槛 1.5 个标准差 264 笔 +0.06%（t 0.20），门槛 3 个标准差 33 笔 −0.80%（t −0.70），拿 1 天 192 笔 −0.19%（t −0.91），拿 7 天 119 笔 +0.77%（t 1.04）；压力测试 成本翻倍 −0.05%（t −0.14），晚一天进场 +0.02%（t 0.04）。

```bash
git clone https://github.com/runningshark/m2_orderbook_cny_failureprove
cd m2_orderbook_cny_failureprove
py verify.py OB2
```

### 108 · 资金费高时结算前做空

“资金费高时，结算前多头平仓、价格下跌”。规则：上一次费率 ≥ 0.05%，结算前 1 小时做空、结算后 1 小时平仓。（[档案](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/reports/108_FS1_short_before_funding.md)）

- **扣成本后每笔 −0.30%（t −3.17）。** 4,170 笔（每年约 633 笔），胜率 45%，平均赚 1.39%、亏 1.69%；不扣成本每笔 −0.10%，成本 0.20%。
- **结算前没有抛压，结算开始的那 1 小时反而在涨（登记之外）。** 上一次费率 ≥ 0.05% 的结算，前后每一根 1 小时 K 线的平均涨跌：结算前 3 小时那根 +0.079%（t 3.21），前 1 小时 +0.035%（t 1.43），结算开始的那 1 小时 +0.159%（t 5.83；但同一时刻常有好几个币一起结算，按结算时刻先平均（872 个时刻）只剩 +0.098%、t 1.90），之后 +0.030%、−0.057%；同样的币、同样的日子里所有小时平均 +0.026%。做空 2 小时每笔价格上亏 0.197%，收到的资金费平均只有 0.092%。
- **和随手进场比：** 随手进场平均 −0.06%，真实的 −0.20%，超出 −0.13%（t −1.70）；训练段超出 −0.12%，验证段 −0.21%。（只比价格的涨跌）
- **训练段每笔 −0.29%（t −2.87，3,743 笔），验证段 −0.40%（t −1.56，427 笔）。**
- **邻近变体：** 门槛 0.03% 6,778 笔 −0.28%（t −3.86），门槛 0.1% 1,479 笔 −0.30%（t −1.69），只拿 1 根（结算那一刻平仓） 4,170 笔 −0.24%（t −3.74），提前 2 小时进场 4,170 笔 −0.30%（t −2.69）；压力测试 成本翻倍 −0.50%（t −4.06），晚一根进场 −0.39%（t −3.96）。

```bash
git clone https://github.com/runningshark/m2_orderbook_cny_failureprove
cd m2_orderbook_cny_failureprove
py verify.py FS1
```

### 109 · 春节前两周空仓（BTC）

“春节前砸盘”。规则：每年春节前 14 天空仓，其余时间持有 BTC。（[档案](https://github.com/runningshark/m2_orderbook_cny_failureprove/blob/master/reports/109_CNY_flat_before_chinese_new_year.md)）

- **择时超额 −5.4%（年化，t −1.31）。** 满仓 96% 的时间，进出 29 次；一块钱变成 1,937，一直持有是 5,656；夏普 1.14 对 1.23，最大回撤 −86% 对 −85%。
- **春节前多数年份在涨（登记之外）。** 14 年里春节前 14 天 BTC 涨了 9 年、跌了 5 年，平均 +9.1%，中位数 +4.4%：2013 年 +35.2%、2014 年 −2.0%、2015 年 +4.1%、2016 年 −7.0%、2017 年 +11.3%、2018 年 +11.8%、2019 年 −3.5%、2020 年 +3.6%、2021 年 +42.9%、2022 年 −8.9%、2023 年 +34.6%、2024 年 +12.7%、2025 年 +4.7%、2026 年 −12.7%。
- **训练段 −3.2%（t −0.64），验证段 −7.8%（t −1.20）；平移检验 p = 0.88（3,066 种平移）。** 持有的日子 BTC 年化 +88.6%（波动 76%），空仓的日子 +222.6%（波动 76%）。
- **邻近变体：** 春节前 7 天 −5.2%（t −2.06），春节前 21 天 −3.4%（t −0.65），春节前 28 天 +2.2%（t 0.36），一直空仓到正月初七 −9.4%（t −1.97）；压力测试 成本翻倍 −5.6%（t −1.37），区间晚一天 −6.4%（t −1.63）。

```bash
git clone https://github.com/runningshark/m2_orderbook_cny_failureprove
cd m2_orderbook_cny_failureprove
py verify.py CNY
```

### 110–113 · 第十九轮事先登记的研究：美联储净流动性、链上手续费、USDT 市占率、稳定币供给比率（共用一个仓库）

美联储净流动性、USDT 市占率、稳定币供给比率（BTC 择时），链上手续费创一年新高就做空（事件类）。规则和通过标准同样是事先登记的（[事先登记_第十九轮.md](https://github.com/runningshark/fed_fees_stables_failureprove/blob/master/事先登记_第十九轮.md)）。**登记 4 个，4 个失败**。

- 累计 108 个候选，Bonferroni 校正 3.501，门槛从这一轮起是 t ≥ 3.6。美联储理事会 H.4.1；Coin Metrics 社区数据（手续费、市值、BTC 价格，到 2026-05-23）；币安 BTCUSDT、ETHUSDT 永续合约（Binance Vision）。每次进出 0.10%。
- BTC 的满仓 / 空仓择时看**择时超额**和**平移检验**；事件类和**随手进场**比。
- 净流动性的规则不显著、换个算法就变负；USDT 市占率其实是 BTC 的均线；稳定币供给比率低的时候买反而跑输；手续费创新高之后做空只有 17 笔，还是亏的。
- 这 4 条共用一个仓库 [fed_fees_stables_failureprove](https://github.com/runningshark/fed_fees_stables_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/fed_fees_stables_failureprove/blob/master/FAILURE_REPORT.md)。数据许可见仓库的 data/README.md。

### 110 · 美联储净流动性增加时持有 BTC

“BTC 跟着美联储净流动性走”。规则：净流动性（总资产 − 财政部一般账户 − 逆回购）比 4 周前多就持有 BTC，否则空仓。（[档案](https://github.com/runningshark/fed_fees_stables_failureprove/blob/master/reports/110_NL1_fed_net_liquidity_timing.md)）

- **择时超额 +12.7%（年化，t 1.21）。** 满仓 56% 的时间，进出 173 次；一块钱变成 1,462，一直持有是 5,656；夏普 1.20 对 1.23，最大回撤 −82% 对 −85%。
- **不显著，换个算法就变负。** 变体“和 1 周前比”−12.0%、“只看总资产”−0.7%。分年度看，BTC 下跌的年份（2014、2018、2022、2025、2026）规则都少亏，BTC 翻倍以上的年份（2013、2016、2017、2020、2023、2024）规则都少赚很多。
- **训练段 +10.5%（t 0.65），验证段 +14.8%（t 1.19）；平移检验 p = 0.12（4,532 种平移）。** 持有的日子 BTC 年化 +134.4%（波动 82%），空仓的日子 +43.0%（波动 68%）。
- **邻近变体：** 和 1 周前比 −12.0%（t −1.16），和 13 周前比 +10.8%（t 1.02），高于最近 13 周的平均 +12.3%（t 1.17），只看总资产 −0.7%（t −0.07）；压力测试 成本翻倍 +11.4%（t 1.09），数据再晚一天 +12.3%（t 1.17）。

```bash
git clone https://github.com/runningshark/fed_fees_stables_failureprove
cd fed_fees_stables_failureprove
py verify.py NL1
```

### 111 · 链上手续费创一年新高就做空

“链上手续费暴涨就是见顶”。规则：BTC 或 ETH 的手续费（7 天平均，美元）创一年新高，做空这个币 30 天。（[档案](https://github.com/runningshark/fed_fees_stables_failureprove/blob/master/reports/111_FE_fee_spike_short.md)）

- **扣成本后每笔 −2.30%（t −0.55）。** 17 笔（每年约 3 笔），胜率 53%，平均赚 11.19%、亏 17.47%；不扣成本每笔 −2.10%，成本 0.20%。
- **分币种看（登记之外）：比在前后的日子里随便哪天做空亏得少，但还是亏。** BTC 9 笔每笔 −3.12%（随手进场 −11.48%），ETH 8 笔每笔 −1.38%（随手进场 −17.09%）：手续费创新高之后的 30 天，价格平均还在涨，只是比前后的日子涨得少。只有 17 笔，验证段 2 笔。
- **和随手进场比：** 随手进场平均 −14.12%，真实的 −2.10%，超出 +12.02%（t 2.16）；训练段超出 +11.77%，验证段 +13.91%。
- **训练段每笔 −3.42%（t −0.74，15 笔），验证段 +6.08%（t 0.77，2 笔）。**
- **邻近变体：** 拿 10 天 24 笔 −0.81%（t −0.28），拿 60 天 13 笔 −9.00%（t −0.86），30 天的平均手续费 20 笔 −7.74%（t −1.42），创 90 天新高 40 笔 −4.19%（t −1.24）；压力测试 成本翻倍 −2.50%（t −0.60），晚一天进场 −4.52%（t −0.97）。

```bash
git clone https://github.com/runningshark/fed_fees_stables_failureprove
cd fed_fees_stables_failureprove
py verify.py FE
```

### 112 · USDT 市占率低于 50 天平均时持有 BTC

“USDT 市占率上升是避险”。规则：USDT 市占率低于 50 天平均就持有 BTC，否则空仓。（[档案](https://github.com/runningshark/fed_fees_stables_failureprove/blob/master/reports/112_UD1_usdt_dominance_timing.md)）

- **择时超额 +19.1%（年化，t 1.66）。** 满仓 46% 的时间，进出 172 次；一块钱变成 14.76，一直持有是 19.67；夏普 1.11 对 0.98，最大回撤 −60% 对 −77%。
- **其实是 BTC 的均线（登记之外）。** 和“BTC 高于 50 天均线就持有”在 86% 的日子里仓位相同；同样的日子、同样的成本，BTC 50 天均线规则的择时超额是 +28.9%（t 2.46）。USDT 的市值变化慢，市占率的涨跌主要来自分母（全部资产的市值），也就是行情本身。
- **训练段 +31.4%（t 1.71），验证段 +4.2%（t 0.34）；平移检验 p = 0.03（2,291 种平移）。** 持有的日子 BTC 年化 +104.2%（波动 60%），空仓的日子 +23.5%（波动 63%）。
- **邻近变体：** 20 天平均 +9.3%（t 0.84），100 天平均 +7.9%（t 0.73），200 天平均 −5.8%（t −0.54），USDT 加 USDC +19.1%（t 1.67）；压力测试 成本翻倍 +16.7%（t 1.44），数据再晚一天 +12.4%（t 1.07）。

```bash
git clone https://github.com/runningshark/fed_fees_stables_failureprove
cd fed_fees_stables_failureprove
py verify.py UD1
```

### 113 · 稳定币供给比率低时持有 BTC

“稳定币供给比率低就是弹药多”。规则：BTC 市值 ÷（USDT + USDC 市值）低于 200 天平均就持有 BTC，否则空仓。（[档案](https://github.com/runningshark/fed_fees_stables_failureprove/blob/master/reports/113_SSR1_stablecoin_supply_ratio_timing.md)）

- **择时超额 −12.7%（年化，t −1.13）。** 满仓 58% 的时间，进出 45 次；一块钱变成 1.51，一直持有是 7.27；夏普 0.37 对 0.79，最大回撤 −69% 对 −77%。
- **比率低的时候买，反而跑输。** 2022 年熊市全程满仓（规则 −64%）；2023、2024 年的上涨里大部分时间空仓（满仓 17%、25% 的时间），一直持有 +155%、+121%，规则只有 +53%、+21%。
- **训练段 −11.9%（t −0.67），验证段 −4.0%（t −0.34）；平移检验 p = 0.85（2,141 种平移）。** 持有的日子 BTC 年化 +32.4%（波动 64%），空仓的日子 +68.1%（波动 55%）。
- **邻近变体：** 50 天平均 −16.4%（t −1.44），100 天平均 −18.6%（t −1.69），365 天平均 −11.2%（t −1.02），只用 USDT −13.0%（t −1.18）；压力测试 成本翻倍 −13.4%（t −1.19），数据再晚一天 −11.2%（t −0.98）。

```bash
git clone https://github.com/runningshark/fed_fees_stables_failureprove
cd fed_fees_stables_failureprove
py verify.py SSR1
```

### 114–117 · 第二十轮事先登记的研究：持仓量骤降、月相、周一效应、月初效应（共用一个仓库）

持仓量骤降后做多（事件类），新月前后、只在周一、月末到月初持有 BTC（日历规则）。规则和通过标准同样是事先登记的（[事先登记_第二十轮.md](https://github.com/runningshark/oi_moon_calendar_failureprove/blob/master/事先登记_第二十轮.md)）。**登记 4 个，4 个失败**。

- 累计 112 个候选，Bonferroni 校正 3.511，门槛 t ≥ 3.6。币安 BTCUSDT、ETHUSDT 永续合约的持仓量和日线（Binance Vision）；Coin Metrics 社区数据的 BTC、ETH 每日价格（到 2026-05-23）；新月、满月自己算。每边 0.10%。
- 日历规则看**择时超额**和**周期内的随机相位检验**（以前的平移检验对按周期重复的规则不适用）；事件类和**随手进场**比。
- 持仓量骤降之后的一周和随手挑的一周差不多；新月前后和满月前后没有差别；周一不扣成本还涨得多，但一周进出两次付不起成本；月初效应 2020 年以后没有了。
- 这 4 条共用一个仓库 [oi_moon_calendar_failureprove](https://github.com/runningshark/oi_moon_calendar_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/oi_moon_calendar_failureprove/blob/master/FAILURE_REPORT.md)。数据许可见仓库的 data/README.md。
- 说明（登记之后才发现）：116（DOW1）、117（TOM1）和第三轮（第 30 条）登记的日历类规则部分重复。第三轮的 467 条里已经有“只在星期一持有”和“只在月末 2 天和月初 3 天持有”，在 30 个币、ETH、BTC 上都测过，结论也是没有择时能力。这一轮的登记里说周内、月初效应“都还没有测过”是错的；判定不变。详见仓库 [FAILURE_REPORT.md](https://github.com/runningshark/oi_moon_calendar_failureprove/blob/master/FAILURE_REPORT.md) 的“已知缺陷”。

### 114 · 持仓量骤降后做多 BTC、ETH

“持仓量骤降之后是买点”。规则：BTC 或 ETH 的持仓量一天跌 8% 以上、价格也跌，收盘做多 7 天。（[档案](https://github.com/runningshark/oi_moon_calendar_failureprove/blob/master/reports/114_OI1_oi_flush_long.md)）

- **扣成本后每笔 +1.18%（t 1.08）。** 64 笔（每年约 10 笔），胜率 62%，平均赚 5.65%、亏 6.26%；不扣成本每笔 +1.38%，成本 0.20%。
- **分币种看（登记之外）：BTC 和随手进场一样。** BTC 38 笔每笔扣成本后 +1.35%，不扣成本只比随手进场多 +0.15%；ETH 26 笔每笔 +0.95%，多 +0.70%。2025、2026 年（5、6 笔）每笔平均 −3.97%、−4.75%。
- **和随手进场比：** 随手进场平均 +1.01%，真实的 +1.38%，超出 +0.37%（t 0.34）；训练段超出 +0.46%，验证段 +0.21%。
- **训练段每笔 +1.58%（t 1.21，43 笔），验证段 +0.37%（t 0.19，21 笔）。**
- **邻近变体：** 门槛 5% 139 笔 +1.09%（t 1.38），门槛 12% 26 笔 +1.64%（t 0.92），拿 3 天 70 笔 +2.31%（t 2.72），拿 14 天 55 笔 +1.16%（t 0.76）；压力测试 成本翻倍 +0.98%（t 0.90），晚一天进场 +0.21%（t 0.24）。

```bash
git clone https://github.com/runningshark/oi_moon_calendar_failureprove
cd oi_moon_calendar_failureprove
py verify.py OI1
```

### 115 · 新月前后持有 BTC

“新月前后涨得多”（Yuan、Zheng、Zhu 2006 的月相效应）。规则：新月前后 15 天持有 BTC，其余的日子空仓。（[档案](https://github.com/runningshark/oi_moon_calendar_failureprove/blob/master/reports/115_MOON1_lunar_new_moon_timing.md)）

- **择时超额 −1.1%（年化，t −0.10）。** 满仓 51% 的时间，进出 332 次；一块钱变成 84，一直持有是 5,656；夏普 0.88 对 1.23，最大回撤 −74% 对 −85%。
- **新月前后和满月前后没有差别。** 14 年里新月那一半涨得多的正好 7 年；不扣成本的择时超额也只有 +1.4%（t 0.13）。
- **训练段 −8.6%（t −0.48），验证段 +6.7%（t 0.56）；随机相位检验 p = 0.43（1,999 次）。** 持有的日子 BTC 年化 +100.7%（波动 78%），空仓的日子 +87.0%（波动 75%）。
- **邻近变体：** 新月前后 3 天 −11.1%（t −1.12），只在满月前后 3 天空仓 +1.0%（t 0.11），新月到之后 14 天 −3.7%（t −0.30），ETH +2.7%（t 0.18）；压力测试 成本翻倍 −3.6%（t −0.32），换成币安 BTCUSDT 永续合约的价格 +8.2%（t 0.73）。

```bash
git clone https://github.com/runningshark/oi_moon_calendar_failureprove
cd oi_moon_calendar_failureprove
py verify.py MOON1
```

### 116 · 只在周一持有 BTC

“BTC 周一涨得多”（Caporale、Plastun 2019）。规则：只在周一持有 BTC。（[档案](https://github.com/runningshark/oi_moon_calendar_failureprove/blob/master/reports/116_DOW1_monday_effect_timing.md)）

- **择时超额 +6.2%（年化，t 0.89）。** 满仓 14% 的时间，进出 1,396 次；一块钱变成 9.68，一直持有是 5,656；夏普 0.70 对 1.23，最大回撤 −49% 对 −85%。
- **不扣成本还在，但付不起一周两次进出（分段是登记之外的）。** 不扣成本的择时超额 +16.6%（t 2.39），训练段 +21.2%（t 2.09），验证段 +11.7%（t 1.25）；13 年多进出 1,396 次，成本一年约 10%。一周七天里不扣成本最差的是周四 −19.6%（t −2.12），是七天里挑出来的，不算线索。
- **训练段 +10.8%（t 1.07），验证段 +1.3%（t 0.14）；随机相位检验 p = 0.01（1,999 次）。** 持有的日子 BTC 年化 +224.3%（波动 81%），空仓的日子 +72.3%（波动 75%）。
- **邻近变体：** 周日和周一 +4.8%（t 0.56），周一和周二 +7.6%（t 0.80），周一到周五 −12.2%（t −1.74），ETH 的周一 −7.2%（t −0.68）；压力测试 成本翻倍 −4.2%（t −0.61），换成币安 BTCUSDT 永续合约的价格 +1.2%（t 0.14）。

```bash
git clone https://github.com/runningshark/oi_moon_calendar_failureprove
cd oi_moon_calendar_failureprove
py verify.py DOW1
```

### 117 · 月末到月初持有 BTC

月初效应（Lakonishok、Smidt 1988）。规则：月末最后一天到月初第 3 天持有 BTC。（[档案](https://github.com/runningshark/oi_moon_calendar_failureprove/blob/master/reports/117_TOM1_turn_of_month_timing.md)）

- **择时超额 +7.0%（年化，t 1.04）。** 满仓 13% 的时间，进出 322 次；一块钱变成 6.54，一直持有是 5,656；夏普 0.68 对 1.23，最大回撤 −53% 对 −85%。
- **2020 年以前有一点，之后没有了。** 不扣成本 +9.4%（t 1.39）：训练段 +17.9%，验证段 +0.1%；换成币安的价格（2020 年起）−3.5%。
- **训练段 +15.5%（t 1.38），验证段 −2.3%（t −0.34）；随机相位检验 p = 0.10（1,999 次）。** 持有的日子 BTC 年化 +149.1%（波动 69%），空仓的日子 +85.6%（波动 77%）。
- **邻近变体：** 月末最后一天到月初第 2 天 +4.7%（t 0.79），月末最后两天到月初第 3 天 +9.4%（t 1.35），月初第 1 到第 5 天 +5.0%（t 0.62），ETH +13.6%（t 1.56）；压力测试 成本翻倍 +4.6%（t 0.68），换成币安 BTCUSDT 永续合约的价格 −3.5%（t −0.51）。

```bash
git clone https://github.com/runningshark/oi_moon_calendar_failureprove
cd oi_moon_calendar_failureprove
py verify.py TOM1
```

### 118–119 · 第二十一轮事先登记的研究：技术指标规则大全第二批（共用一个仓库）

第三轮（第 30 条）测过 21 类、467 条指标规则；这一轮把它没有的 40 种常见指标（均线的变种（Hull、DEMA、TEMA、ZLEMA、VWMA、ALMA、McGinley、KAMA）；趋势状态（抛物线 SAR、Aroon、Vortex、TRIX、线性回归、吊灯止损、平均 K 线、鳄鱼线、Elder 脉冲、UT Bot、SSL 通道、分形）；摆动类（威廉 %R、Stoch RSI、终极振荡器、AO、Fisher 变换、Schaff、Coppock、KST、DPO、RSI(2)、Connors RSI、WaveTrend）；成交量类（MFI、CMF、A/D 线、蔡金振荡器、强力指数、EMV、Klinger）；波动和突破（Larry Williams 波动突破、Choppiness））展开成 145 条只做多的日线规则，在 BTC 和每季度 10 个币上各测一遍。规则清单和通过标准同样是事先登记的（[事先登记_第二十一轮.md](https://github.com/runningshark/d1_indicator_zoo2_failureprove/blob/master/事先登记_第二十一轮.md)）。**登记 2 组，2 组失败**。

- 累计 114 个事先登记的检验，Reality Check 的门槛 p < 0.00022。Binance Vision 的 BTCUSDT 现货日线和 48 个永续合约的日线、资金费；单边 0.10%。
- 和第三轮一样：BTC 上趋势类作为一类是正的，超卖买入的规则是负的（BTC 组 −0.81，10 个币那一组 −1.02），单独哪一条都和运气分不出来。
- 这 2 条共用一个仓库 [d1_indicator_zoo2_failureprove](https://github.com/runningshark/d1_indicator_zoo2_failureprove)（需要 pandas、numpy）。总览见 [FAILURE_REPORT.md](https://github.com/runningshark/d1_indicator_zoo2_failureprove/blob/master/FAILURE_REPORT.md)。数据许可见仓库的 data/README.md。

### 118 · 技术指标规则大全第二批（145 条，BTC）

这一组只用 BTC：持有时满仓 BTCUSDT 现货，空仓时拿现金。（[档案](https://github.com/runningshark/d1_indicator_zoo2_failureprove/blob/master/reports/118_A_btc_indicator_zoo2.md)）

- **最好的一条经不起“试了 145 条”的校正。** 超额 t 最高的是“MFI(28) > 50 持有”，t = 2.93。如果 145 条全都没有择时能力，光靠运气，最大 t 的 95% 分位就有 3.14。Reality Check 的 p = 0.087，离登记的门槛 0.00022 很远。
- **到验证段就没了。** 只看训练段（到 2023-12-31），最好的规则也是“MFI(28) > 50 持有”（训练段 t 3.36），它在验证段的超额是 −1.2%/年，t −0.09。训练段前 10% 的 14 条规则合在一起，验证段超额 +4.6%/年，t 0.43。
- **成本。** 零成本时 p = 0.040（最大 t 3.22）；扣单边 0.10% 后 p = 0.087；成本翻倍后 p = 0.164（最大 t 2.68）。
- **超卖买入的规则是负的（登记之外的分组）。** “指标在低位时买”的 17 条规则（%R < −80、RSI(2) < 10、MFI < 20、Connors RSI < 10 等）t 的中位数 −0.81，超额为正的只占 18%；其余 128 条 t 的中位数 1.37。
- 剩下的线索：趋势类作为一类是正的：均线的变种 7 种、趋势状态 12 种，19 种里 18 种 t 的中位数在 0.5 以上，例外是平均 K 线（两条一正一负，中位数约为 0）；两大类的中位数 1.07、1.39。145 条里 t > 2 的有 29 条（20%）。规则之间高度相关，这个比例不能当成 29 个独立的证据。这和第三轮 BTC 那一组（“待观察”，不在失败档案里）的读法一样：作为一类有一点择时能力，单独哪一条都和运气分不出来。

```bash
git clone https://github.com/runningshark/d1_indicator_zoo2_failureprove
cd d1_indicator_zoo2_failureprove
py verify.py
```

### 119 · 技术指标规则大全第二批（145 条，每季度 10 个币）

每个季度第一天按现货成交额选 10 个币（和第十到二十轮相同，一共 48 个合约，含后来下架的），每条规则在每个币上各自给信号；币在币池里、并且规则说持有时，占资金的 1/10（U 本位永续合约），其余拿现金。（[档案](https://github.com/runningshark/d1_indicator_zoo2_failureprove/blob/master/reports/119_B_alt10_indicator_zoo2.md)）

- **最好的一条经不起“试了 145 条”的校正。** 超额 t 最高的是“CHOP(14) < 38.2 且收盘 > 20 日均线”，t = 2.58。全靠运气时最大 t 的 95% 分位是 3.07；Reality Check 的 p = 0.166，离门槛 0.00022 很远。
- **单独像样的规则几乎没有。** 145 条里 t > 2 的只有 1 条，t 的中位数 0.50，超额为正的占 71%。
- **样本外不够。** 训练段最好的规则就是这条（训练段 t 2.02），验证段超额 +9.5%/年，t 1.61，没到登记的 2。训练段前 10% 的 14 条合在一起，验证段 t 0.41。
- **成本和执行。** 零成本 p = 0.112；成本翻倍 p = 0.242（最大 t 2.40）；晚一天执行 p = 0.451（最大 t 2.09）。
- 剩下的线索：降回撤：一直持有这 10 个币（等权，按价格算）：夏普 0.65、最大回撤 −90%；夏普最高的一条（CHOP(14) < 38.2 且收盘 > 20 日均线）：夏普 1.17、最大回撤 −11%，平均只有 5.5% 的资金在场；145 条里夏普超过持有的占 43%。

```bash
git clone https://github.com/runningshark/d1_indicator_zoo2_failureprove
cd d1_indicator_zoo2_failureprove
py verify.py
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
