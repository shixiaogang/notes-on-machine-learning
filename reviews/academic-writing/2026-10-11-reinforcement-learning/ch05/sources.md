# CH05 汇总修复一手证据

- 日期：2026-10-13；身份：修订者核源，不是独立复核。只核本轮算法目标、命名和所需边界，不声称核完全部引文全文。
- 既有引用目标保持。网页/PDF由只读网络取得；PDF选页在内存中解析，未写图源、文献库或其他共享文件。

## IQ-Learn

- 原作者论文：[arXiv 2106.12142v4](https://arxiv.org/pdf/2106.12142v4)，正文第6页第4.3节式(9)，第7页第5.1、5.3节式(12)。核到 `max_Q E_rhoE[phi(Q-gamma E V)]-(1-gamma)E_rho0[V]`；所选 `phi(x)=x-x²/(4alpha)`。本文将尺度参数改记 `kappa`，奖励平方系数记 `c=1/(4kappa)`，熵温度仍为1。
- 第5.1节：初态项可由占用上的 `E[V(s)-gamma V(s')]` 估计；离线只用专家转移，在线可混合专家和策略转移。第5.3节离线式(12)为 `min E_expert[V-Q]+c E_expert[(Q-gamma E V(next))²]`，不是普通环境奖励的TD回归，也不是策略分布上的平方奖励正则。
- v4的归一化占用与本章一致；早期会议版的占用口径不同，不直接搬其比例。本文保留初态系数 `(1-gamma)`，未只缩放奖励项。
- 作者代码：[Div99/IQ-Learn iq.py](https://raw.githubusercontent.com/Div99/IQ-Learn/main/iq_learn/iq.py)，核读 `expert` 上平方残差正则、`value_expert` 和混合 `value` 分支。代码仅辅助确认经验训练对象，不替代论文目标；未运行训练，也未声称本文梯度就是所有目标网络/停止梯度配置的精确复制。
- 新增单后继经验平方项与总体式的差异由条件二阶矩恒等式亲算：`E(delta²|s,a)=R_Q²+gamma² Var(V(next)|s,a)`。所以随机转移时明确称经验代理；确定性转移时才与总体残差相同。吸收尾项仍按本章占用延拓计入，不能用 `done` 掩码悄然删除。
- `chi²(policy occupancy || expert occupancy)` 的方向核自论文第4.1-4.2节及附录统计距离表。受限Q类对应受限对偶目标，不能声称等于完整散度；超出专家支持时完整散度可无穷大。

## AIRL

- 原作者论文：[arXiv 1710.11248v2](https://arxiv.org/pdf/1710.11248v2)，第5页第6节式(4)、算法1，第11页附录A.1，第13页附录B定义B.1。核到 `D=exp f/(exp f+pi)`、`f=g+gamma h(next)-h(s)`；专家标签1、策略标签0，最大化专家 `log D` 加策略 `log(1-D)`。
- 算法1第6-7行明确 `r=log D-log(1-D)` 后策略优化。代入可得 `r=f-log pi`；附录A.1式(6)为温度1的奖励减对数动作概率，不能用GAIL的 `-log(1-D)` 原样替代，也不能重复加同一熵。
- 作者代码：[justinjfu/inverse_rl airl_state.py](https://raw.githubusercontent.com/justinjfu/inverse_rl/master/inverse_rl/models/airl_state.py)，核读来源标签、策略概率分母及 `score_discrim` 对数几率分支。专家记录也使用当前策略概率，不是专家概率。未执行模型训练。
- 本章明确所示策略梯度是本轮冻结奖励/优势的一次更新，下一轮刷新分母；多次复用旧样本为代理更新，不冒充任意新策略下的精确熵目标。折扣/吸收口径是本章采用的教学协议，不把论文有限未折扣附录自动当作该协议下的完整恢复证明。
- 第6节及附录B/C的恢复条件有 `g(s)`、真实状态奖励、确定性动态、理想最大因果熵专家/优化等限制。定义B.1不是普通路径可达：共同前驱的一步后继相连，并取传递闭包后要求全体状态相连。迁移取 `g`，不取含旧价值/策略信息的 `f` 或判别奖励。

## 名称与首现

|对象|一手位置|核实结果及本章动作|
|---|---|---|
|SEARN|[Daumé等作者PDF](https://users.umiacs.umd.edu/~hal3/docs/daume09searn.pdf)，标题及方法介绍|`Search-Based Structured Prediction`，方法名Searn/SEARN；不编造逐字母全称。本章采用“基于搜索的结构化预测”，明确方法专名。|
|AggreVaTe|[Ross与Bagnell论文](https://arxiv.org/pdf/1406.5979)，引言|`Aggregate Values to Imitate`，聚合专家cost-to-go；本章“聚合价值模仿”。|
|TAMER|[Knox与Stone作者PDF](https://www.cs.utexas.edu/~bradknox/papers/kcap09-knox.pdf)，引言|`Training an Agent Manually via Evaluative Reinforcement`；本章“通过评价强化手动训练智能体”，保人工评价拟合/反应延迟的原机制。|
|CVaR|[Rockafellar与Uryasev作者PDF](https://sites.math.washington.edu/~rtr/papers/rtr179-CVaR1.pdf)，标题及定义|`conditional value-at-risk`；保全书“条件风险价值”译名，并以损失 `-G_0` 上尾说明回报下尾，不改变后章的符号约定。|
|HER|[作者论文](https://arxiv.org/pdf/1707.01495)，标题|`Hindsight Experience Replay`；保“事后经验回放”，仅补英文，不在本章扩写后章算法。|
|DAPO|[作者arXiv报告v2](https://arxiv.org/pdf/2503.14476v2)，摘要及算法节；[NeurIPS官方会议页](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a4277440d50f1f15d2cb4c14f7e0c0d2-Abstract-Conference.html)|`Decoupled Clip and Dynamic sAmpling Policy Optimization`；本章“解耦剪裁与动态采样策略优化”，展开移至表前。官方页确认为NeurIPS 2025主会，DOI `10.52202/085713-3775`；没有混同另一个同缩写的Direct Advantage-Based Policy Optimization。|

## 限制

- 未对其他既有文献的全部历史归因、实验结果或完整原证明重新核源。
- 未重新读取9图全部源语义，不借R1/R3图源检查作为本人检查；本次亲读图注与正文数据/公式，图源和成品交独立复核者与主代理。
- 未运行算法、绘图程序、构建或PDF版面检查；这些限制不能由来源网页或静态公式验证抵消。
