# 量化失败合集 / Quant Failure Archive

做过、跑过、最后没赚到钱的策略，在这里留一份可复现的档案。

不写"经验总结"，只写能重跑的数字：原始声称是什么、用什么数据复核、扣完成本和样本外之后还剩多少。每一条都是**独立仓库**，代码、数据、验证脚本齐全，clone 下来就能自己跑一遍看我有没有骗人。（14–24 是同一次研究里的 11 条，共用代码和数据，放在本仓库的 [entries/factor_study_failureprove](entries/factor_study_failureprove/)。）

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
| 14 | 周线 · 横截面动量（7 天） | **确认失败**（零成本勉强，扣成本后不显著） | 零成本 t 2.48，扣成本后 t **1.75**；年换手 73 倍；成本翻倍 t 1.03 | [entries/factor_study_failureprove](entries/factor_study_failureprove/reports/14_X1_xs_momentum_7d.md) |
| 15 | 周线 · 横截面动量（28 天） | **确认失败**（没有信号） | 年化 +9.0%，t **0.85**；样本外年化 +3.6%（t 0.28） | [entries/factor_study_failureprove](entries/factor_study_failureprove/reports/15_X2_xs_momentum_28d.md) |
| 16 | 周线 · 横截面动量（90 天） | **确认失败**（方向相反） | 年化 **−14.0%**，回撤 **−76.9%**；样本外年化 −28.2%（t −2.19）；5 个变体全负 | [entries/factor_study_failureprove](entries/factor_study_failureprove/reports/16_X3_xs_momentum_90d.md) |
| 17 | 周线 · 资金费 30 天多空 | **确认失败**（信号被平均掉） | 年化 +4.0%，t **0.44**；晚一天执行 −0.6%；样本外累计 −3.7% | [entries/factor_study_failureprove](entries/factor_study_failureprove/reports/17_X5_funding_30d.md) |
| 18 | 日线 · 横截面一日反转 | **确认失败**（零成本也亏） | 零成本年化 **−5.0%**；年换手 495 倍，净年化 **−54.5%**，回撤 −97.8% | [entries/factor_study_failureprove](entries/factor_study_failureprove/reports/18_X8_xs_reversal_1d.md) |
| 19 | 周线 · 30 币分散趋势（现货） | **确认失败**（对 BTC 没有超额） | 夏普 0.53，对 BTC 超额 t **0.20**（贝塔 0.30）；样本外累计 **−13.5%** | [entries/factor_study_failureprove](entries/factor_study_failureprove/reports/19_T1_trend_spot.md) |
| 20 | 周线 · 30 币分散趋势（永续多空） | **确认失败**（样本外转负） | 训练段 t 2.01 → 样本外 t **−0.32**；2024–2026 年 +0.0% / −3.7% / −15.1% | [entries/factor_study_failureprove](entries/factor_study_failureprove/reports/20_T2_trend_perp.md) |
| 21 | 周线 · 波动率管理的 BTC | **指标无效**（没有超额） | 夏普 0.57 vs 持有 0.59；对 BTC 超额 t **0.20**；回撤 −64.9% vs −81.2% | [entries/factor_study_failureprove](entries/factor_study_failureprove/reports/21_T3_btc_vol_managed.md) |
| 22 | 周线 · 跨资产趋势（25 个市场） | **确认失败**（成本吃掉一半，仍不显著） | 19.9 年：零成本夏普 0.47 → 扣成本 **0.25**（t 1.21）；成本翻倍 0.04；2023–2025 连亏 | [entries/factor_study_failureprove](entries/factor_study_failureprove/reports/22_T5_cross_asset_trend.md) |
| 23 | 周线 · 资金费篮子（挑费率最高的币） | **收益衰减** | 超过国债利率：训练段每年 +8.7% → 样本外每年 **−3.5%**；2022 年起年年为负 | [entries/factor_study_failureprove](entries/factor_study_failureprove/reports/23_C1_funding_basket.md) |
| 24 | 周线 · 多 BTC 空山寨 | **确认失败**（不显著，山寨季巨亏） | t **0.76**；2021 年 **−51.4%**，回撤 −56.1%；训练段年化 −2.7% | [entries/factor_study_failureprove](entries/factor_study_failureprove/reports/24_S1_btc_vs_alts.md) |

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

### 14–24 · 事先登记的 14 个因子候选（11 个失败）

把量化机构和学术界公开的几类做法（横截面动量、套息、趋势跟随、波动率管理、多空配对）搬到币安上集中测了一遍。和前面的条目不同的地方：

- **事先登记。** 测之前把 14 个候选的规则、参数和通过标准写死（[事先登记.md](entries/factor_study_failureprove/事先登记.md)），之后不改、不调参。
- **不用幸存者。** 数据包含已下架的币（588 个品种里 194 个已下架）；每个调仓日只用当时的成交额取前 30。
- **门槛是 t ≥ 3。** 同时测 14 个，碰巧有一个 t 超过 2 的概率接近一半。
- 成本单边 0.10%，永续合约持仓计入资金费；训练段到 2023 年底，验证段从 2024 年起。

结果：**没有一个通过，11 个失败。** 这 11 条共用一套代码和数据，所以放在同一个文件夹里，没有各建一个仓库；拆开会丢掉“同时测了 14 个”这个前提。总览见 [FAILURE_REPORT.md](entries/factor_study_failureprove/FAILURE_REPORT.md)。

三个共同的死法：

- **成本。** 动量 7 天零成本 t **2.48**，扣成本后 **1.75**；跨资产趋势夏普 **0.47 → 0.25**；资金费篮子年化 **+8.4% → +3.1%**。
- **样本外衰减。** 30 币多空趋势训练段 t 2.01，2024 年以后 **−0.32**；资金费篮子 2022 年起每年都跑不赢国债。
- **收益来自大盘，不是信号。** 30 币趋势（现货）和波动率管理的 BTC，相对 BTC 的超额 t 都只有 **0.20**。

各条一句话：

- **14 · 横截面动量 7 天**：零成本 t 2.48，扣单边 0.10% 成本后只剩 1.75，不显著。 [档案](entries/factor_study_failureprove/reports/14_X1_xs_momentum_7d.md)
- **15 · 横截面动量 28 天**：年化 +9.0%，t 0.85；验证段 t 0.28，没有信号。 [档案](entries/factor_study_failureprove/reports/15_X2_xs_momentum_28d.md)
- **16 · 横截面动量 90 天**：方向相反：年化 −14.0%，验证段 −28.2%（t −2.19）。 [档案](entries/factor_study_failureprove/reports/16_X3_xs_momentum_90d.md)
- **17 · 资金费 30 天多空（多低空高）**：年化 +4.0%，t 0.44；晚一天执行就转负。 [档案](entries/factor_study_failureprove/reports/17_X5_funding_30d.md)
- **18 · 横截面一日反转（每天调仓）**：零成本年化 −5.0%，加成本后 −54.5%，回撤 −97.8%。 [档案](entries/factor_study_failureprove/reports/18_X8_xs_reversal_1d.md)
- **19 · 30 币分散趋势·现货只做多**：夏普 0.53，但相对 BTC 的超额 t 只有 0.20，验证段亏损。 [档案](entries/factor_study_failureprove/reports/19_T1_trend_spot.md)
- **20 · 30 币分散趋势·永续多空**：训练段 t 2.01，验证段 t −0.32；全区间 t 1.33。 [档案](entries/factor_study_failureprove/reports/20_T2_trend_perp.md)
- **21 · 波动率管理的 BTC 持有**：回撤 −81.2% 降到 −64.9%，夏普 0.57 对 0.59，没有超额。 [档案](entries/factor_study_failureprove/reports/21_T3_btc_vol_managed.md)
- **22 · 跨资产趋势·多空**：零成本夏普 0.47，扣成本后 0.25；19.9 年 t 只有 1.21。 [档案](entries/factor_study_failureprove/reports/22_T5_cross_asset_trend.md)
- **23 · 资金费篮子（现货多 + 永续空）**：超过国债利率的部分：训练段每年 +8.7%，验证段 −3.5%。 [档案](entries/factor_study_failureprove/reports/23_C1_funding_basket.md)
- **24 · 做多 BTC、做空山寨篮子**：全区间 t 0.76；2021 年一年亏 51.4%，回撤 −56.1%。 [档案](entries/factor_study_failureprove/reports/24_S1_btc_vs_alts.md)

剩下的线索：对照组里最简单的 BTC 100 日均线择时（第 12 条）夏普 **0.92**、回撤 −59.8%，仍然是方向性规则里最好的，把趋势分散到 30 个币没有多出东西；一周动量和慢的跨资产趋势在零成本下是真实但很弱的信号。14 个候选里另外 3 个没有被判为失败，属于“待观察”，不在这里。

```bash
git clone https://github.com/runningshark/quant-failure-archive
cd quant-failure-archive/entries/factor_study_failureprove
pip install pandas numpy
py download_data.py --yahoo   # 只有第 22 条需要：ETF 日线不随仓库分发
py verify.py                  # 末尾一行：11 / 11 条和归档数字一致
py verify.py X1               # 只跑一条
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
