# 第4章共享修复请求

CH04-REPAIR，2026-10-13。仅供主代理串行处理，不是已执行的共享修改。
本代理只改本章正文及本目录，不改索引、图源、文献或入口。

## 首现词典

本章新增的 `\term` 调用如下。本worktree现有词典对以下显示词条均无精确登记。
主代理须在最终集成稿确认全书首次出现归属、已有别名与冲突，再登记。
英文扩写核验的实际材料及限制见 `source-checks.md`，不得以本表代替一手核验。
英文专名已经是显示词条时，不把中文机制描述另造为方法译名。

| 显示词条 | 建议英文映射 | 正文首次定位锚 | 处理要点 |
| --- | --- | --- | --- |
| 卡尔曼滤波 | Kalman filter | `eq:rl-information-kalman` 前 | 全书已有Kalman相关讲解，核最早归属及拼写别名；不要重复冲突登记。 |
| 深度循环Q网络 | Deep Recurrent Q-Network | `rl4-hausknecht2015-drqn` 前 | DRQN；不要以论文标题Q-Learning替代网络全称。 |
| R2D2 | Recurrent Replay Distributed DQN | `rl4-kapturowski2019-r2d2` 前 | 中文说明循环网络、序列重放、分布式训练，非另造译名。 |
| GTrXL | Gated Transformer-XL | `sec:rl-information-filtering` 后半 | 不猜XL的扩写。 |
| 线性二次高斯控制 | linear-quadratic-Gaussian control | `sec:rl-information-belief-control` 后半 | LQG；核数学准备卷既有讲解是否使用别名。 |
| DICE | DIstribution Correction Estimation | `eq:rl-information-dice` 前 | 分布校正估计是描述，不作为新中文专名。 |
| DualDICE | Dual stationary DIstribution Correction Estimation | 同上 | 保留作者有意的大写取字，不以论文副标题替展开。 |
| BEAR | Bootstrapping Error Accumulation Reduction | `rl4-kumar2019-bear` 前 | 包含Accumulation；中文描述减少自举误差累积。 |
| BRAC | Behavior Regularized Actor Critic | `rl4-wu2019-brac` 前 | 中文描述行为正则化的行动者与评论家。 |
| ReBRAC | Revisited BRAC | `rl4-tarasov2023-rebrac` 前 | 不编造另一个完整扩写。 |
| Decision Transformer | Decision Transformer | `rl4-chen2021-dt` 前 | 中文描述回报条件序列模型，保留专名。 |
| Diffusion-QL | Diffusion Q-learning | `rl4-wang2023-diffusionql` 前 | 中文描述扩散动作建模与Q学习结合，不声明某直译已通行。 |
| IDQL | Implicit Diffusion Q-learning | `rl4-hansenestruch2023-idql` 前 | 不能把整篇论文标题当缩写全称。 |
| DEAS | DEtached value learning with Action Sequence | `rl4-kim2026-deas` 前 | 中文描述动作序列上的分离价值学习；方法展开不含论文标题后缀。 |
| MOPO | Model-based Offline Policy Optimization | `rl4-yu2020-mopo` 前 | 中文说明学习模型上的离线策略优化。 |
| MOReL | Model-Based Offline Reinforcement Learning | `rl4-kidambi2020-morel` 前 | 中文说明基于模型的离线强化学习。 |
| COMBO | Conservative Offline Model-Based Policy Optimization | `rl4-yu2021-combo` 前 | 中文说明学习模型上的保守离线策略优化。 |
| Trajectory Transformer | Trajectory Transformer | `rl4-janner2021-trajectory` 前 | 中文描述轨迹序列预测模型。 |
| Diffuser | Diffuser | `rl4-janner2022-diffuser` 前 | 中文描述扩散模型轨迹规划；不是缩写，无全称另展开。 |
| SPIBB | Safe Policy Improvement with Baseline Bootstrapping | `rl4-laroche2019-spibb` 前 | 中文说明基线自举约束；safe不扩成业务安全保证。 |
| AWAC | Advantage Weighted Actor Critic | `rl4-nair2021-awac` 前 | 中文描述优势加权的行动者与评论家。 |
| Cal-QL | Calibrated Q-Learning | `rl4-nakamoto2023-calql` 前 | 中文说明Q价值校准，不是概率校准。 |

## 版面与来源

- SH05冻结稿L738-739与L1161-1164已用拆句、拆数学列表及缩短公式引导处理；数学值与展示公式未改，未使用负间距。是否消除10.01886pt及6.5826pt溢出须由主代理最终构建和书页检查确认。
- 新术语带来的英文长串可能新增版面问题，当前禁止构建，不能声称未有新溢出。主代理需连同Kalman增补段、DICE增补段核最终书页。
- 本次没有新增、删除或更换正文引文目标，无文献入口修改请求。`source-checks.md`只记录实际打开的命名与机制材料，不代表全部外部证明或实验已经复现。
- 本worktree为冻结旧出版基线；主代理集成到十二卷结构时，按最终词典归属和实际依赖更新，不能复用本目录的旧卷号作为新出版配置。
