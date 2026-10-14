# 第4章汇总修复的一手来源核验

身份：CH04-REPAIR，2026-10-13，汇总修复代理自查，不是独立复核。
受审输入：rewrite-v1.tex，SHA-256
`b93de38ccbd71003d1a8e88b44cb46a8dcb11912a4a2a57c58ef63aa4901e503`。
本表只记录实际打开的一手命名材料与相关机制，不把摘要核验说成全部证明或实验复现。

| 对象 | 实际一手材料及位置 | 核验结果与正文命名动作 |
| --- | --- | --- |
| DRQN | https://arxiv.org/abs/1507.06527 ，v4摘要 | Deep Recurrent Q-Network，不是论文标题中的Q-Learning；用深度循环Q网络。 |
| R2D2 | https://openreview.net/forum?id=r1lyTjAqYX ，作者摘要及作者回复 | Recurrent Replay Distributed DQN；中文描述循环网络、序列重放和分布式训练，保留专名。DQN沿用前章定义。 |
| GTrXL | https://proceedings.mlr.press/v119/parisotto20a.html ，作者摘要 | Gated Transformer-XL；中文描述带门控的Transformer-XL，保留专名，不把XL猜成新全称。 |
| Kalman | https://doi.org/10.1115/1.3662552 ，ASME作者页与摘要 | 原1960论文确为最优线性滤波及误差协方差递推来源；当前网页未取得全文。现代独立高斯递推及正规关系另按本worktree卷一正文推导核验，不冒称原论文全文已审。 |
| LQG | 本worktree卷一 `03-policy-value-and-optimization.tex` L1811-1878；https://underactuated.mit.edu/output_feedback.html 作者教材 | 既有中文为线性二次高斯控制；英文linear-quadratic-Gaussian。沿用正文已有独立噪声、无约束、动作无关协方差条件，不新增普遍分离结论。网络返回正文截断，教材后半未算已读。 |
| DICE / DualDICE | https://arxiv.org/html/1906.04733v2 ，Introduction、2.2式(3)、2.3 Assumption 1及3.1 | Dual stationary DIstribution Correction Estimation；DICE取DIstribution Correction Estimation，不误展开为密度比标题。有限全流约束和目标支持是总体关系；本次正文已明确测试类，完整误差定理仍需另核。 |
| BEAR | https://arxiv.org/html/1906.00949v1 ，摘要、Introduction及第5节标题 | Bootstrapping Error Accumulation Reduction，不能省Accumulation。中文描述减少自举误差累积，保留专名。 |
| BRAC | https://arxiv.org/html/1911.11361v1 ，摘要、Introduction及第3节 | Behavior Regularized Actor Critic；用行为正则化的行动者与评论家这一描述。 |
| ReBRAC | https://proceedings.neurips.cc/paper_files/paper/2023/hash/26cce1e512793f2072fd27c391e04652-Abstract-Conference.html 及 https://arxiv.org/html/2305.09836v2 第3节 | 原文明说Revisited BRAC；不另造完整扩写，中文说明重新考察BRAC并结合TD3+BC设计。 |
| Decision Transformer | https://arxiv.org/abs/2106.01345 ，v2摘要 | 原专名成立；中文描述回报条件序列模型，不硬造Transformer译名。 |
| Diffusion-QL | https://arxiv.org/abs/2208.06193 ，v3摘要 | Diffusion Q-learning；补英文专名首现标记，中文描述扩散动作建模与Q学习结合，不把未核通行性的直译当公认译名。 |
| IDQL | https://arxiv.org/html/2304.10573v2 ，摘要及Introduction | Implicit Diffusion Q-learning；不是把标题Implicit Q-Learning as an Actor-Critic Method with Diffusion Policies当缩写全称。保留专名，中文描述隐式Q学习与扩散动作模型结合。 |
| DEAS | https://openreview.net/forum?id=bVTaAXeBmE ，作者摘要、标题及官方Decision | DEtached value learning with Action Sequence；ICLR 2026 Poster正式状态已核。标题含for Scalable Offline RL，但作者摘要中的方法展开止于Action Sequence。中文描述动作序列上的分离价值学习，不把固定动作块当Option。 |
| MOPO | https://arxiv.org/abs/2005.13239 ，v6标题与摘要 | Model-based Offline Policy Optimization；中文描述学习模型上的离线策略优化。 |
| MOReL | https://arxiv.org/abs/2005.05951 ，v3标题与摘要 | Model-Based Offline Reinforcement Learning；中文描述基于模型的离线强化学习，具体低回报吸收态机制保留。 |
| COMBO | https://arxiv.org/abs/2102.08363 ，v2标题与摘要 | Conservative Offline Model-Based Policy Optimization；中文描述学习模型上的保守离线策略优化。 |
| Trajectory Transformer | https://arxiv.org/html/2106.02039v4 ，Introduction及3.1 | 原专名成立，中文描述轨迹序列预测模型；保留束搜索及首动作执行机制。 |
| Diffuser | https://proceedings.mlr.press/v162/janner22a.html ，作者摘要 | 扩散轨迹规划机制有依据；保留原专名，无缩写全称可展开。 |
| SPIBB | https://proceedings.mlr.press/v97/laroche19a.html ，作者摘要 | Safe Policy Improvement with Baseline Bootstrapping；用基线自举的安全策略改进，并保留safe只约束相对回报、不是业务安全的限定。 |
| AWAC | https://arxiv.org/html/2006.09359v3 ，Introduction末及第4节标题 | Advantage Weighted Actor Critic；用优势加权的行动者与评论家这一描述。 |
| Cal-QL | https://arxiv.org/html/2303.05479v4 ，摘要、Introduction及第5节标题 | Calibrated Q-Learning，不以论文副标题充当方法展开；中文价值校准Q学习，明确不是概率校准。 |

失败检索不作证据：BEAR v3 HTML、ReBRAC v3 HTML无该文档；已改用实际存在的v1/v2原文。UNC Kalman PDF链接404，已核ASME DOI页面但未取得原论文全文。

前置反证已亲读：本worktree回归章 `02-regression.tex` L154明写
`$(a)_+=\max(a,0)$`；卷一Kalman正文 L2694-2758给联合高斯、
创新协方差、增益及误差与创新正交关系；LQG正文 L1811-1878给有限时域分离推导。
这些是已有正文依据，不是本次拟增加文字；CH04-R1-03的撤销仍须在repair.md绑定冻结上下文。

正文首现方案已写回，22项新增调用已逐项列入 `shared-repair-requests.md`。
本代理未修改索引、文献或共享入口；本文的来源核验不替代主代理最终词典审计。
