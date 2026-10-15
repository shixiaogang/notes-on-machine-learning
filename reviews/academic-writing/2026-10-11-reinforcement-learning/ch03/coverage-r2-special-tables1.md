# 第3章R2特殊单元：表格1

CH03-R2-ST1，2026-10-12，修订1；独立R2；hash `927887345166301fb9aaa47eb6a53ec8389f7abfe6353bc87e5b27b5049f353e`。重新顺读源表头及所有行。H是表头，R源行是稳定行ID；每行的全部列共同完成一次比较，列内断句已逐项读，不用表名摘要代所有行。表注见W按caption源行逐句记录，并在本文件绑定。此文件T01-T14，其余续ST2。

| ID、位置短引 | 白话、比较口径及全部列的具体依据 |
|---|---|
| T01-H L18「改进接口/模型/价值/动作」 | 两维实际数据流，价值职责与动作例分列；不以预测网络出现就认modelbased，L9-11先解释在线规划无需独立V。 |
| T01-R20「无模型价值」 | 不查P，由Q比较长期回报、贪心/探索执行；DQN例是预告，非未释前提。 |
| T01-R21「无模型策略」 | 不查P，V/Q给基线/优势/目标，参数π执行；PPO/SAC可有critic而不成为第五互斥类。 |
| T01-R22「模型价值」 | 模型做模拟/前瞻/search，值可备份/叶值/轨迹score，动作来自更新Q或当前规划；Dyna/MuZero职责准确。 |
| T01-R23「模型策略」 | 模型导/训练样本供参数策略改进、回报自举，训练后π执行；PILCO/Dreamer仅例非所有model都有真state预测。 |
| T01-C L26 | caption明确分类数据流，技术名字不直接提供额外保证。 |
| T02-H L58「变化条件/可见/样本/输出」 | 五种单维变化非互斥类别，先L51说明信息/任务差及恢复MDP可达性。 |
| T02-R60「回报未知」 | history+a集合，只有chosenarm reward，输出在线序列；不错误假未选臂反馈。 |
| T02-R61「上下文」 | 本轮已见feature、同feature所选reward，输出feature→a；与动作改变nextcontext不同。 |
| T02-R62「对手」 | history可有context，只chosen本轮reward，比指定类的regret序列；不默认固定均值/全知每轮参照。 |
| T02-R63「部署动作」 | 随机bandit同信息、按识别分配样本，输出一a+置信；非在线regret和固定T自动置信。 |
| T02-R64「影响状态」 | currentstate/history及reward/nextstate，输出可到达利用highvalue策略，增可达性不只是feature加列。 |
| T02-C L67 | 非互斥及可组合条件在caption明。 |
| T03-H L218「协议/固定量/输出分析」 | 比停止依据而非两算法，L211先指出错误率和差幅不同。 |
| T03-R220「固定预算」 | 先固定T拉臂数再hat a_T，分析simple regret或Pwrong；不能先选T称δ达标。 |
| T03-R221「固定置信」 | 先δ/必要eps，随机τ和hat a_τ、Perror≤δ及Eτ成本；随机停止需timeuniform interval，下一段补在用前。 |
| T03-C L224 | 固T与δ不同承诺明确，未编造指定算法复杂度。 |
| T04-H L265「方法/信号/行为边界」 | novelty测量对象与行为分工，先L257定义r+βb/原奖eval；训练奖不称confidence。 |
| T04-R267「计数」 | b=1/sqrt(N+1)偏低访问，离散划分需有意义；99/3数例.1/.5核。 |
| T04-R268「伪计数」 | 密度更新概率变作替代，大state范围需density假设；不是实visitcount，此关键区别明。 |
| T04-R269「ICM」 | learnedfeature动作conditional前向error/逆dyn表示，偏可控features但不保全噪剔除，后noisyTV解释该限制。 |
| T04-R270「RND」 | trainedpredictor对fixedrandomnet output差，拟合困难代理novelty，generalization/forget/noise影响score；不声称P不确定性。 |
| T04-R271「回合内」 | currentembedding到本回合memory距离或near density；memoryreset改变何为新，不混跨回合经验计数。 |
| T04-C L274 | caption信号训练工具而非转移置信，本地界限清。 |
| T05-H L337「比较对象/MC/TD」 | 同fixedpi评价比较target来源、时机、条件均值；不互比不同训练budget实验。 |
| T05-R339「何时更新」 | MC等真return，TD一step后可算；不是MC永远慢的计算定理。 |
| T05-R340「随机性」 | MC余下state/reward，TD当step后继及估值，target条件当前value；不是固定V自身必随机。 |
| T05-R341「初值」 | initial不进入trueG，却进入TD尾，MC currentV仍影响update residual；列指target依赖有上下文。 |
| T05-R342「均值」 | fixedpi Gmean=Vpi，TDmean=TpiV通常≠Vpi，说明一步bootstrap bias不等最终bias。 |
| T05-R343「注意」 | MC终止或处理infinite尾，TD控制bootstrap/sample条件；后给finite访问步长noise，未无条件convergence。 |
| T05-C L346 | target/finalbias分开，满足条件表格收敛而不是任network。 |
| T06-H L434「方法/改动/边界」 | 改trace/在线参数/奖励位置不同对象，L421定理固定参数后改变条件。 |
| T06-R436「积累」 | feature每visit加、旧traceγλ衰减，重复累加，等价fixedθ条件不漏。 |
| T06-R437「替换」 | tabular/binary当前component1，改变repeatweight；dense特征不能原样套activation1。 |
| T06-R438「真实在线」 | correctedtrace/update匹配timechanging前向，精确经典linear，不扩大任network恒等。 |
| T06-R439「重奖励」 | pastkeyevent分配delayR，逐trajectory折总奖相等或明确等价条件保目标；折与不折后有等式。 |
| T06-C L442 | trueonline修变参、RUDDER学奖励归属，不合并一机制。 |
| T07-H L527「权放哪/targetfixedpoint」 | 同pi/mu环境看currenterror与futuretrace差，表fixedpoint非有限NN guarantee。 |
| T07-R529「IS」 | wholeG或每r prefix积恢复piE需support，方差可能指数非必指数。 |
| T07-R530「总权截断」 | min(c,W)一般变E、无补偿不精确pi；没有用降Var忽略bias。 |
| T07-R531「Tree Backup」 | traceλpi、pi期望backup用未选估值，保Qpi零点；“未选”不是已获得真reward。 |
| T07-R532「Retrace」 | futuretraceλmin(1,rho)，tabular/coverage fixedpointQpi，非直接截G权；F514起始动作给定不乘rho_t。 |
| T07-R533「V-trace」 | currentrho截/futurec另截，barρ有限effectiveπ∝min(barρmu,pi)，c影响传播/速；不说两种截均不改target。 |
| T07-C L536 | 表格零点不替finite样本和非线性优化。 |
| T08-H L566「方法/y/谁决定a'」 | 同Q残差update，只target/动作source异，caption真terminaltail0/合法max。 |
| T08-R568「MC」 | G整trajectorybehavior，估回报之后才改π，目标不是先在targetQ选nexta。 |
| T08-R569「SARSA」 | r+γQ下一实a，由当前mu采，同policy版本含探索；不能称Q*最优target。 |
| T08-R570「Expected」 | r+γ∑πQ指定target，π=mu才同策略；减少nexta抽样随机性非消转移noise。 |
| T08-R571「Q-learning」 | r+γmax合法nexta，targetgreedy/behavior探索可异；同数据三target数例已支持。 |
| T08-C L574 | 终止遮与动作域均明确。 |
| T09-H L641「误差/式/未知对象」 | d>0指定权/真Tpi/linear投影在L634先定义，避免MSBE与sample平方混淆。 |
| T09-R643「valueerror」 | norm_d Vθ−Vpi平方，通常缺真value监督；对象真实V而非Bellmanresidual。 |
| T09-R644「MSBE」 | norm_d TpiVθ−Vθ，先条件平均后平方；后双采反例说明为何不同。 |
| T09-R645「MSPBE」 | 先linearΠ_d backup再与Vθ，取决feature和weight；非任NNprojection唯一。 |
| T09-C L648 | 单sampleTD²不自动MSBE，技术缺口准确。 |
| T10-H L717「方法/问题/表示数据边界」 | 同评价/控制接口下列计算求解，邻文halfgrad固定点路线明。 |
| T10-R719「halfTD」 | sample固定点不fulltarget导，linearonpolicy专门保证、NN不等MSBE下降。 |
| T10-R720「LSTD」 | meanA=Eφ(φ−γφ')'/b=Erφ，solveAθ=b，fixedpi/linear，offpolicy需ratio与invertibility；可写方程不代表总稳定逆。 |
| T10-R721「LSPI」 | actionvalueLSTD与greedy交替，fixedbatch对newπ复用需coveredpairs，不一次solve得最优。 |
| T10-R722「FQI」 | freezeoldQ、监督回归r+γlegalmax，nonlinear可用；regressionerror/closure/distributionchange都影响控制。 |
| T10-C L725 | batch降逐step噪不是填缺数据/错target，未定量比较胜负。 |
| T11-H L850「component/机制/不能推出」 | 四component改不同接口，不总以稳定作指标；正文已建DQN的data/target问题。 |
| T11-R852「Double」 | online选argmax、bar评同a，二网训练history相关非完全无偏，合法域继承本地DQN。 |
| T11-R853「Dueling」 | Q=V+A−meanlegalA去常数ambiguity，共statevalue，notindependently真advantage；均值分母为|A(s)|。 |
| T11-R854「priority」 | P∝(|δ|+eps)^p、w∝(NP)^−β，samplingloss改权，β<1 partial，β1并保正确factor才uniform校正；norm过期要另说。 |
| T11-R855「NoisyNet」 | W=M+Σ⊙E learnedscale，paramnoise共作用多个a不同每stepε，notdeepcoverageguarantee。 |
| T11-C L858 | target/representation/sampling/exploration四对象明。 |
| T12-H L929「表示/监督/性质边界」 | 保动作后果非仅易predict，先有控制充分性合并反例与测试类缩限。 |
| T12-R931「DeepMDP」 | latentP/Rloss，须error/distance/smooth条件才能value联系，finite训练loss不全局条件。 |
| T12-R932「CURL」 | sameobsaugmentcontrast，表示consistent需增强不删动作信息，非任augment都好。 |
| T12-R933「SPR」 | actionconditionalmultisteplatent/targetmatch保temporalaction关系；prediction出现不自动执行modelplanning。 |
| T12-R934「DrQ」 | enhancedobsvalue目标正则，合理augmentation约束一致性非环境model。 |
| T12-C L937 | idealstructure/trainloss/testperformance三个证据不混。 |
| T13-H L991「已知error/选a/结论」 | 各行改变被近似的参照和接口，prior定理supQ*已证明，不按相同“error小”混算。 |
| T13-R993「q对Q*」 | legalmaxq，sup≤eps→loss≤2eps/(1−γ)，两误差和geometric演算完整。 |
| T13-R994「v对V*」 | accurateP/R前瞻max，extraγ接v尾误差→2γeps/(1−γ)，缺model不能直接v比较a。 |
| T13-R995「q对Qpi」 | 相对当前π作approx改善，非相对optimal同界；参照π名称明确。 |
| T13-R996「trainMSE」 | dataweightedaverage小不控制部署稀见gap，需coverage/densityratio/transfer，下一.001 vs1例具体。 |
| T13-C L999 | value接口差异/未知P缺动作比较对象本地解释。 |
| T14-H L1096「路径/可计算/不需与代价」 | actor入口动作不能枚举，三梯度路径比较所需可导信息，名字是问题预告后各局部展开。 |
| T14-R1098「REINFORCE」 | πprob/density loggradient+sampleG，不env导，longepisode可能highVar，finitegradient前已derive。 |
| T14-R1099「DPG」 | π参数导+Q动作导不枚举continuous，critic动作导质量代价不是免评价；不能从REINFORCE推env需导。 |
| T14-R1100「黑盒」 | 参数给定可evalreturn、不需π或env微分，但多参数trajectory成本；notzerocostnor精确J。 |
| T14-C L1103 | 概率、动作、参数空间三个微分/搜索对象区别，caption与先后方法一致。 |

本文件覆盖T01-T14共14表头、56表行、14表注（表注自然句另在W）。不涉及来源原论文核对或PDF渲染；没有由表数量推正文通过。
