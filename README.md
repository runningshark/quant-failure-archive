# 量化失败合集 / Quant Failure Archive

做过、跑过、最后没赚到钱的策略，在这里留一份可复现的档案。

不写"经验总结"，只写能重跑的数字：原始声称是什么、用什么数据复核、扣完成本和样本外之后还剩多少。每一条都是**独立仓库**，代码、数据、验证脚本齐全，clone 下来就能自己跑一遍看我有没有骗人。

---

## 条目

| # | 策略 | 结论 | 关键数字 | 仓库 |
|---|------|------|----------|------|
| 01 | ETH 择时 · 遗传规划（GP） | **确认失败**（外部复核，不是原作者自评） | 样本外 **−5.3%**，最大回撤 **−58.4%** | [gp_eth_failureprove](https://github.com/runningshark/gp_eth_failureprove) |
| 02 | ETH 择时 · 1 小时（趋势 + 动量） | **确认失败**（且「参数寻优」是假的） | 全区间 **−85.5%**，回撤 **−90.5%**，612 笔；零成本仍 **−50.7%** | [eth_1h_failureprove](https://github.com/runningshark/eth_1h_failureprove) |
| 03 | 1 小时 · 超卖接多（带止损） | **确认失败**（零成本也亏） | 样本外 BTC **−51%** / ETH **−83%**；零成本 BTC 全期 **−64%** | [h1_dip_stop_failureprove](https://github.com/runningshark/h1_dip_stop_failureprove) |
| 04 | 1 小时 · 超卖接多（不止损） | **确认失败**（高胜率陷阱） | 胜率 89%–94%，样本外 BTC **−31%** / ETH **−56%**，单笔扛单 **−12.7%** | [h1_dip_nostop_failureprove](https://github.com/runningshark/h1_dip_nostop_failureprove) |
| 05 | 1 小时 · 反转（跌了就买） | **确认失败**（被手续费吃光） | 样本外 BTC **−65%** / ETH **−62%**；零成本 **+213%**，约 3,500 笔换手 | [h1_reversal_failureprove](https://github.com/runningshark/h1_reversal_failureprove) |

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
- 默认参数下根本没有交易（逻辑写死或阈值不可达）。

## 为什么公开

因为失败样本比成功样本稀有。成功案例永远有幸存者偏差，而"这条路我走过，是死的"至少能省掉别人的三个月。

## 相关

- [crypto-quant-dashboard](https://github.com/runningshark/crypto-quant-dashboard) —— 在跑的数据看板（只读，不下单）
- 条目模板：[_template.md](_template.md)
