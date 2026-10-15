# CH03-R1 接管者W遍：L2063--2213

同一接管者，人工逐句W1--W6复读及全部特殊单元。模型梯度、Dreamer图源全部文字和关系亲读。本块不借P遍作为W覆盖，不称核验PILCO/Dreamer一手来源或完整算法收敛证明。身份、版本、前置和冻结约束见resume。

|ID、位置短引|白话意思；专项依据或发现|
|---|---|
|RW-L2067-S01，“下次重新搜索”|前节MPC输出当次动作序列，下一状态重规划，不是一份跨状态固定策略；接口对象本地恢复，G7接受。|
|RW-L2067-S02，“序列改共享参数”|要可重复调用的状态到动作规则，搜索变量由当前序列变策略参数；固定模型使用、改变优化对象，理由在前句，G3/E10接受。|
|RW-L2067-S03，“导数或生成经验”|模型可提供路径求导或虚拟训练转移，两种改变策略的机制不同；不是仅列模型名称，G2接受。|
|RW-L2067-S04，“训练与推断成本”|动作来自策略不等于状态无需模型，新观测可能需推断；范围限定“主要/可能”有实际部件，G1/E3接受。|
|RW-L2073-S01，“真实不给导数”|要从动作参数求长期成本变化，学习模型可给真实黑盒环境不能直接查询的导数；后句连续控制对象建立本地入口，G5接受。|
|RW-L2073-S02，“后继再改策略”|theta改当前u、u改nextx、nextx改后续u，必须保留全链；数学关系两端/类型明确，G2接受。|
|RW-L2073-S03，2073--2075，“重参数化动力学”|xnext=fphi(x,u,xi)、u=pitheta(x)，xi分布不随theta，模型固定使路径导数成立；模型/策略/随机输入即时给，G6接受。|
|RW-L2075-S04，2075--2076，“D为敏感度”|D是状态对共享策略参数Jacobian，同采样轨迹求导；类型/计算对象清楚，不把模型参数一起更新，G6接受。|
|RW-L2076-S05，“链式法则”|将直接动作参数影响和旧状态影响分开供下一式；依据为复合函数求导，G6接受。|
|RW-L2083-S01，“四Jacobian”|f_x/f_u与pi_x/pi_theta分别是哪一导数及求值位置都明确；不把pi_theta误当全导数，G2/G6接受。|
|RW-L2083-S02，“直接/历史两项”|f_u pi_theta是当前参数直接影响；(f_x+f_u pi_x)D保留旧动作影响，解释公式为何两项，G6接受。|
|RW-L2083-S03，“成本下降方向”|敏感度链乘成本梯度得到模型内而非真实环境梯度，下文成本方向和交换条件限定，G1/G6接受。|
|RW-L2083-S04，2083--2085，“有限时域成本”|定义L步期望成本加终端成本，要计算其theta导数；指标对象、时域和末端项明，G6/E11接受。|
|RW-L2095-S01，“r=-c”|成本低好与奖励高好相反，通过符号取负对应；不悄换优化方向，G6/E12接受。|
|RW-L2095-S02，“交换期望的条件”|可微和可积控制才可导数进入期望，硬碰撞/离散/终止可能失败；充分条件非所有控制自动成立，G1/G7接受。|
|RW-L2095-S03，“训练两路径”|图用于区分真实数据拟合模型与固定模型求策略导数，职责可辨，接受。|
|RW-L2104-S01，“轨迹变分布参数”|路径采样导数处理随机性，替代是传播近似分布矩；原随机轨迹→近似参数对象及理由明，G3/E10接受。|
|RW-L2104-S02，“GP增量/不确定性”|PILCO预测动力学增量并带给定数据下不确定性，不是只点预测；模型作用具体，G2接受，未核源。|
|RW-L2104-S03，“矩匹配再导成本”|由近似Gaussian状态和策略算next矩，再拟Gaussian均值协方差、递推并求成本导数；机制输入输出顺序清楚，G4/G6接受。|
|RW-L2104-S04，2104--2106，“m合矩与F”|m=(mu,vecSigma)是分布矩参数不是环境状态，把next矩写F(m,theta)以求导；符号用途/类型即时给，G6接受。|
|RW-L2113-S01，“成本乘敏感度”|期望成本对矩导数乘矩对theta导数，接回长期目标；未将Gaussian参数当真实状态精确值，G6接受。|
|RW-L2113-S02，“多峰/核噪声”|Gaussian近似丢形状，GP不确定性依核和噪声假设；代价约束具体，G1/G7接受。|
|RW-L2113-S03，“非精确积分”|近似矩传播不等真实非线性全分布精确积分，正向边界清楚无多重否定，G4/E4接受。|
|RW-L2117-S01，“标量两步末成本”|无噪声、x0固定1、线性系统和共享theta、末成本x2²/2都给；最小例检验跨时刻导数，G3/G6接受。|
|RW-L2117-S02，“q/x1/x2”|q=a+btheta给x1=q/x2=q²，简化复合求导而非新未连接动作值q；局部定义明确，G6接受。|
|RW-L2124-S01，“.25→-.525”|a=b1 theta-.5得q.5及2bq³=.25，成本梯度下降theta-.1*.25=-.525；人工数/方向/步长可复算，G6/E12接受。|
|RW-L2124-S02，“漏一半”|x2=q*x1的两条theta影响各bq，漏pi_x D项剩一半；一般两步系统解析式支持，不泛称任何任务均一半，G1/G6接受。|
|RW-L2127-S01，“黑盒评分器”|模型还可仅输出候选策略回报不供导数，本节同目标下另一接口，G3接受。|
|RW-L2127-S02，“固定候选搜索”|每候选theta模型rollout采样回报，回接前述搜索，免可微但需多次评估；新参数域而非当前动作序列明确，G6/G7接受。|
|RW-L2127-S03，“三信息需求”|表比較同模型策略搜索所需信息，不将三者算法保证混同，G2接受。|
|RW-L2145-S01，“误差小非导数准”|函数值误差与局部敏感度不同，承接表中导数质量要求，G2/G5接受。|
|RW-L2145-S02，2145--2146，“epsilon sin反例”|f=u/fhat=u+epsilon sinomega u全域值差<=epsilon，但导数误差幅度epsilon omega无统一上界；可直接微分验证，G1/G6接受。|
|RW-L2146-S03，“u0输出相同”|u0 sin0=0而cos0=1，输出同仍梯度可差；新反例任务是值→导数非重复两步链，G4/E6接受。|
|RW-L2146-S04，“价值界不控导数”|前节模拟引理传值而非导数，需额外敏感度或真实更新检验；旧结论可继承/不可继承对象明确，G7/E10接受。|
|RW-L2152-S01，“模型反复给轨迹”|真实交互昂贵时在模型生成策略训练序列，承接两模型接口而非空泛性能说，G5接受。|
|RW-L2152-S02，“World Models”|观测编码latent、循环预测next、搜索controller参数，主要接口具体；历史来源未外核，G2接受。|
|RW-L2152-S03，“Dreamer三分工”|模型内策略行动→critic评价预测return→actor改进，既有AC接预测环境；每部件输入用途清楚，G4接受。|
|RW-L2152-S04，“规律非新证据”|虚拟轨迹依旧模型信息，不增加独立真实环境证据，G1/E3接受。|
|RW-L2156-S01，“想象定义”|真实history潜状态起点，之后policy a/modelnext/reward与continue头，构成imaginedseq；定义各输出源完整，G2/G4接受。|
|RW-L2156-S02，“后验起点先验后继”|无新观测时不能编码未来真obs，先验滚动；条件/信息可用性明确，G1/G7接受。|
|RW-L2159-S01，“有无obs如何更”|前定义后验/先验需展开更新区别，当前明确新问题不是重复定义，G4/E6接受。|
|RW-L2159-S02，“RSSM记忆与随机”|deterministicmemory递推历史、随机latent含当前条件不确定性，两状态角色区别明，G2接受。|
|RW-L2159-S03，“m/z避免h混”|命名m/z合x与真实历史h分开；局部x复用为latent明确不再标量例真物理x，G3/G6接受。|
|RW-L2159-S04，“真实后验/想象先验”|观测存在可纠状态，无新obs只能预测，不暗示先验等真实已观察，G1接受。|
|RW-L2159-S05，“动作时刻奖索引”|统一r_t为执行a_t后奖，使后式的state-entering监督可追溯，G6接受。|
|RW-L2168-S01，“后继头读奖/继续”|r_t/c_t是该转移后继x上的头输出，明确转移对齐，G6接受。|
|RW-L2168-S02，“改索引必须整体”|实现若用r_t+1表示enteringstate奖要全目标一致，不把preaction奖当postaction，具体风险/动作明，G1/G6接受。|
|RW-L2170-S01，“三监督仍缺先验”|obs/r/c拟合真实后验状态不直接约束无obs先验，需prior接posterior；损失缺口先于KL项，G5/G6接受。|
|RW-L2170-S02，“V3离散q/p”|V3对象限定，q_t/p_t同刻posterior/prior，不混旧章节状态值q；名称角色即时给，G3/G6接受。|
|RW-L2170-S03，“三NLL/双KL最小”|真实seq期望预测损失加分别stopgrad一侧KL，优化模型phi向低loss；总体对象/方向/梯度分工明，G6/E11接受。|
|RW-L2185-S01，“首项缺转移省”|seq首state无配套prevtransition时不用r/c监督，处理边界索引，G1/G6接受。|
|RW-L2185-S02，“rprev进入x”|r_t-1是前步行为后入x_t奖，和本章r_t postaction定义相容，G6接受。|
|RW-L2185-S03，“KL低1停/均匀”|dyn训prior、rep训posterior，max1使<1不额外压KL，离散混1%防zero/extreme；机制/尺度明，G1/G6接受，版本配置未核源。|
|RW-L2185-S04，“重建非全干预充分”|重建仅约束obs拟合不能保新动作所有控制结果，承接前节层次检验具体对象，G1/G7/E3接受。|
|RW-L2194-S01，“固定model目标”|无未来真reward可用，actorcritic需modelpredreturn目标；评价量需要先建立，G5/G6接受。|
|RW-L2194-S02，2194--2196，“起点到三输出”|后验起点、策略抽a、model出nextx/r/c，训练数据来源顺序明确，G6接受。|
|RW-L2196-S03，2196--2197，“有效折扣逆递推”|gammac为终止折扣，用lambda组合one-stepvalue和laterreturn，既有lambda回报接imagined数据；运算用途/参数/末端边界明确，G6/G7接受。|
|RW-L2206-S01，2206--2207，“两步教学数据”|gamma.9 lambda.5 L2 c全1/r.2,.3/nextv.4,.6全指定，非实测轨迹，G1/G6接受。|
|RW-L2207-S02，2207--2209，“.84/.758”|G2=.6，G1=.3+.9*.6=.84，G0=.2+.9(.2+.42)=.758，可复算，G6/E12接受。|
|RW-L2209-S03，“c1变0”|G1=.3、G0=.2+.9(.2+.15)=.515，改变终止会改变bootstrapping，G3/G6接受。|
|RW-L2209-S04，“回报与权重污染”|c影响递推也决定有效生存权，不只r预测误差；权重机制前节cumcontinue已建立、后式会落实，G2接受。|
|RW-L2211-S01，“分工同损失不同”|各Dreamer同model/actor/critic职责不等同估计器，比较对象限定，G2接受。|
|RW-L2211-S02，“V1路径导数”|连续latent/control通过model和critic求imaginedreturn导数，明确版本/动作条件，G3接受，来源未核。|
|RW-L2211-S03，“V2离散/配置不同”|离散latent直通、路径/似然比组合随动作配置，未称纯统一一种梯度，G1/G7接受。|
|RW-L2213-S01，“V2不推出V3梯度”|离散视觉控制用途差异不允许把V3纯似然比同路径梯度，版本范围明确，G3/G7接受；“更实用”实验来源未独立核验。|
|RW-L2213-S02，“按独立协议”|V2网络/目标/eval必须独立来源解释，不能拿V3配置套V2，G1接受。|

## 特殊单元

|ID、位置|白话与具体依据|
|---|---|
|RX-L2074，2074--2075|缺模型轨迹对theta导数，fphi可重参数化/xi law独立/policy可导让pathwisechain成立；不含phi同时训练，接受G6。|
|RX-L2078，2077--2082|Dnext=(fx+fu pix)D+fu pitheta由totaldx/du链，D0=0按章前置固定初始分布对theta无依赖；直接项和历史项2083各解释，接受。|
|RX-L2087，2086--2094|缺finiteLcost梯度，state项Dᵀcx/action项(pixD+pithet)ᵀcu/terminalDLᵀcL相加再期望；低cost目标、交换积分条件2095即给，接受G6。|
|RX-L2105，2105--2106|为降低随机trajectory计算改追踪Gaussian矩mu/Sigma，vec合参数用于F递推；不是保持完整分布，2113边界明，接受。|
|RX-L2108，2107--2112|F(m,theta)全导数分旧m敏感度与直接theta项，成本再乘之；矩估计模型条件2104，接受G6。|
|RX-L2119，2118--2123|x1=q/x2=q²/末cost=.5q4，导数b、2bq、2bq³，相同theta两次调用两项相等，接受G6。|
|RT-L2134，2134|接口/信息/计算误差三列同策略搜索任务，接受。|
|RT-L2136，2136|可微或适当随机估计路径，长度L memory/derivative连乘、采样与导数误差；功能与代价对应，接受。|
|RT-L2137，2137|矩/期望cost/导数可算，Gaussian形状与核cost假设带近似偏差，非所有分布可精确传播，接受。|
|RT-L2138，2138|候选theta只需samplemodelreturn，多个候选噪声重复、modelwrong排序仍风险，接受。|
|RC-L2141-S01，2141，“三方式”|表按获取梯度/评分信息分，不按有无net名称分，接受。|
|RC-L2141-S02，2141，“导数质量”|可微可能省部分无梯度搜索，但额外需局部导数准确；后反例直接测试新增条件，接受G1。|
|RX-L2146，2145--2146|f/u值差<=epsilon而导数epsilonomega cos任大，在u0值同导数差最大；全u允许集合、比较量低absdiff好、反例数学可证，接受G6/E9。|
|RD-L2156，2154--2157|definition两句各RW2156S01/S02，覆盖真root/无真obs后继/outputs来源/信息条件，不省特殊环境，接受。|
|RX-L2161，2160--2167|RSSM nextmemory依prev m/z/a，posterior附nextobs、prior只memory，缺少obs时两conditional不同；符号/角色/索引2168解，接受G6。|
|RX-L2172，2171--2184|缺真实预测兼无obs滚动训练，三NLL拟obs/prev r/c，sgq||p只训prior、q||sgp只训rep，max1 lowerfloor免低KL压力、.1rep weight明确；phi最小true-seqexpectation，接受G6。|
|RX-L2199，2198--2205|缺imaginedlambda目标，末v bootstrap、r+gammac[(1-lambda)nextv+lambda nextG]逆序，terminalc0免后项；数例验证，接受G6。|
|RC-L2100-S01，“模型展开”|图画共享策略产生控制的多时刻状态链，接受。|
|RC-L2100-S02，“实虚线”|前向依赖与成本反导不同，policy参数共享、状态回输policy，接受。|
|RC-L2100-S03，“phi固定”|realdata拟phi与fixedphi模型内求theta分开，梯度穿过非模型loss更新；G2/E2接受。|
|RF-gradient-L07，“x0/x1/x2三态”|foreach三态皆进入同theta策略，跨时刻共享非独立theta_t，接受。|
|RF-gradient-L08，“三策略”|policy(x_i)输出，x2策略画出但无后继用于末cost，此为可重复调用接口非额外计入两步，接受。|
|RF-gradient-L09，“s→pi”|state-input影响当步action，全导数包含pi_x，接受。|
|RF-gradient-L11--12，“两个fphi”|共享固定dynamics两次调用，不需真实可微环境，接受。|
|RF-gradient-L13--16，“x→f→next”|状态两步前向链保历史作用，接受。|
|RF-gradient-L17--18，“u0/u1”|policy输出动作输入各步动力学，接受。|
|RF-gradient-L19--20，“末cost与x2”|cL读最后状态与两步例相合，接受。|
|RF-gradient-L21--24，“cost反导路径”|虚线自cost经f1/f0达各policy，省绘所有Jacobian分支但正文给全链，不暗示阻断state到laterpolicy，接受。|
|RF-gradient-L25--26，“theta共享phi固定”|明确当前theta求导时phi不优化，接受G2。|
|RF-gradient-L27--29-S01，“实线前向虚线导数”|关系类型图内自明，接受。|
|RF-gradient-L27--29-S02，“真实数据另拟合”|不拿cost导数充环境model监督，接受G1。|
|RC-L2190-S01，“真实与想象”|图是两训练来源不是两真实dataset，接受。|
|RC-L2190-S02，“后验起点先验/末值”|真实序列拟model并形成root，无obs先验roll/r/c进return、critic末bootstrap；机制完整，接受。|
|RC-L2190-S03，“部署仍model”|no-stepsearch不免memory/posterior推断，动作策略与状态模型不同对象，G2/G7接受。|
|RF-dreamer-L06，“真实o/a/r/c”|用于model监督来源为实际sequence非imagined奖励，接受。|
|RF-dreamer-L07，“RSSM后验root”|obs-conditioned状态起imagined，接受。|
|RF-dreamer-L08，“预测loss/KL”|三head监督和prior/rep对齐，正文2172训练对象明，接受。|
|RF-dreamer-L09--10，“data/post→fit”|real推断state再loss更phi，与另一imaginedtraining支不同，接受。|
|RF-dreamer-L11，“actor抽a”|imaginedstate条件action来自policy，接受。|
|RF-dreamer-L12，“priornext”|无futureobs先验nextlatent，接受。|
|RF-dreamer-L13，“r/c头”|modelpred奖励/存活非真环境测量，接受。|
|RF-dreamer-L14，“G递推”|predr/c和criticvalue共同算lambda target，接受。|
|RF-dreamer-L15，“criticv”|value输入bootstrap亦从returntarget训练，非未来真v标签，接受。|
|RF-dreamer-L16--20，“root/a→prior→head→return/v→return”|forward数据链完整；post→prior画起点接滚动不表示新obs持续可用，图末注明，接受。|
|RF-dreamer-L21--22，“新state回actor”|后继state用于下一policy调用，非一次动作不复用状态，接受。|
|RF-dreamer-L23--25，“return虚线更critic/actor”|loss更新关系，不宣称所有版本同pathgradient；V3具体likelihoodratio正文后续界定，接受。|
|RF-dreamer-L26--28-S01，“实线与虚线”|推断/想象/return和loss更新两类关系解释明确，接受。|
|RF-dreamer-L26--28-S02，“起点后无真obs”|imaginedroll不新增realinteraction，边界清楚，G1/E3接受。|

## 关键链与范围

- RI-2067/2073：当次规划输出→跨状态共享theta→动作/后继/下次策略的复合依赖→可重参数化且固定phi→D递推与cost梯度→两步数例→硬接触/终止的可微交换限制。
- RM-2104/2127：随机路径成本优化→Gaussian矩近似/可计算后继矩→矩敏感度×期望成本导数；黑盒备选只供候选theta回报，免导数但评估与模型排序误差仍有。模型拟合此前已给，非此处新监督目标。
- RI/RM-2152/2170/2194：真实交互昂贵→模型重复生训练seq→posterior真实root/prior无obsnext→真实三NLL不足约束prior→双stopgrad KL训练model→固定model imagined r/c/critic→lambda return→接下来critic/actor更新。各步骤输入/预测/损失方向明确。
- 范围：动作序列→跨状态theta有变量与用途桥；物理x→latentx有显式合状态定义；pathdistribution→Gaussian矩承认可丢多峰；reward转移索引→enteringstate监督逐式对齐；DreamerV1→V2→V3不能承袭同损失/gradient。
- 本块未新增必改发现；V3后续、MBPO等尚未完成W覆盖。
