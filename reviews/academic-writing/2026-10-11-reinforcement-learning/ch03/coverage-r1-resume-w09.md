# CH03-R1 接管者W遍：L1391--1577

人工逐句W1--W6，G1--G7及E专项随条目；跨行句范围列明。SAC源图31行全部亲读。各损失/梯度/表体/伪代码单列，不借后文或作者材料；未核原来源、运行程序、完整收敛证明和PDF版面。

|ID、位置短引|白话意思；具体依据或发现|
|---|---|
|RW-L1395-S01，“动作附近价值变化”|连续a无法逐个比，但Q局部动作导可指如何改actor输出；局部具体任务/旧缺口先给，G5接受。|
|RW-L1395-S02，“确定性f诱导pi”|actor a=f_theta(s)，诱导点质量策略pi_theta；新参数化对象与其符号就地，G3/G4接受。|
|RW-L1395-S03，“DPG链式”|先Q对a导再f对theta链式乘，函数可微导可积才有精确目标梯度；名称+机制+条件一起给，G4/G6接受。|
|RW-L1407-S01，“Q认为上升”|actor沿Q动作增值方向，通过f导传参数；与已给1395计算关系一致，G2接受。|
|RW-L1407-S02，“环境不微/Q导意义”|env不需可微，但Q函数值误差小不保动作梯度准确；价值评价和动作导数两个量明，G1/G7/E1接受，来源未核。|
|RW-L1409-S01，“DDPG组合”|把确定f/Q/回放/慢目标组合，概览是数据参数接口非收敛保证；前网络回放和actor机制已建，G4接受。|
|RW-L1410-S01，1410--1414首句，“回放目标与actor导”|critic以r+gamma目标Q(s',目标f)自举，actor以回放s的f导乘Q动作导；两预测对象/数据/导路径分清，G6接受。|
|RW-L1414-S02，“横线慢目标”|bar theta/barw为缓慢跟随online参数，非独立估计器；首次目标角色就地，G4接受。|
|RW-L1414-S03，“执行噪声投影”|det输出另加探索noise后投合法动作，噪声为采数据而非actor的det目标；合法约束和训练/执行区别明确，G2接受。|
|RW-L1417-S01，“固定回放nu”|nu定义为回放状态分布，非d自动同物；新对象先说明来源，G3/G6接受。|
|RW-L1417-S02，“历史行为混合”|buffer可能多旧pi混合，不是某单pi折扣占用、通常不同current d；两分布关系/不可继承精确PG条件明，G2/G7/E10接受。|
|RW-L1417-S03，“nu作新起点目标”|若把nu当新初始分布再定义Jnu，明确改变哪种目标；不是专业知识猜replay目标，G3/E11接受。|
|RW-L1421-S01，“精确权是未来占用”|Jnu精确grad要nu起沿currentpi全未来占用，不仅初始nu；随机访问来源和梯度权为何变说明，G6/G7接受。|
|RW-L1421-S02，“代理非复用证明”|只replay s链乘是固定权actor proxy/近似，忽略未来访问依参数不能凭复用称精确；明确缺失依赖而非泛称bias，G1/G4接受。|
|RW-L1423-S01，“TD3三误差”|在DDPG接口加部件，分类轴是改哪种估计/更新问题，G2接受。|
|RW-L1423-S02，“较小Q/平滑/延迟”|两Q取小降过估、目标a噪平滑防利用尖峰、actor慢让critic多批评价；各具体作用对象/收益代价后1434限定，G2/G4接受。|
|RW-L1423-S03，“目标可写”|给合法投影和两Q最小目标，服务上述三个改动中的目标/动作两项；不是下界保证，G6接受。|
|RW-L1433-S01，“人为epsilon”|targetnoise指定零均Gaussian常见，不是env随机滑移/actor探索噪；新随机源作用/分布就地，G3/G4接受。|
|RW-L1433-S02，“三部件定位”|调整target值、actor更新时点、目标a局部平均，区分位置与旧DDPG；G2接受，原论文未核。|
|RW-L1434-S01，“低估/平滑过大”|min两Q可负偏，过大噪平滑可抹真窄最优；取舍机制明非万能更稳，G1/G2接受。|
|RW-L1434-S02，“不消所有误差”|这些改动只特定噪声/更新时间，不保所有Q预测导误差0；正向性质前句具体，G1/G4接受。|
|RW-L1436-S01，“det另噪探索”|之前噪为采集，承接可把随机性入目标的新选择；重复新增奖励熵而非仅重讲噪，G4/E6接受。|
|RW-L1436-S02，“随机性入目标”|奖励动作分布分散，使高奖附近保多选择；新优化目的/改变项先解释，G5接受。|
|RW-L1436-S03，“最大熵/温度”|原回报加策略熵，alpha>0权衡愿用回报换分散；新术语、白话、参数作用明确，G4/G6接受。|
|RW-L1436-S04，“目标为”|式展示原r和负logpi熵奖励折扣和期望，先目标改变再数学量，G6/E11接受。|
|RW-L1442-S01，“改变目标非方差”|maxent给Jalpha不同于原J，不只是梯度估量改造；优化对象区别清楚，G1/G7接受。|
|RW-L1442-S02，1442--1443，“离散/微分熵”|finite熵sum -p logp，continuous需reference density且依scale可负；从动作概率到密度新增条件/数值意义明，G3/G7/E10接受。|
|RW-L1445-S01，“固定状态评分”|为求软改进先固定s q_a仅优化动作概率，分离值评价与局部选分布；对象转换理由明确，G3/G5接受。|
|RW-L1445-S02，“全部合法分布”|候选simplex来自有限合法动作，最大平均q+熵而非max单q；集合/方向/运算理由全给，G6/E9接受。|
|RW-L1445-S03，“确切局部解”|下面变分恒等式只该finite局部问题精解，不承诺整个训练全局解；G1接受。|
|RW-L1449-S01，“任意有限q/alpha正”|finite动作、实评分、alpha>0给entropy问题，合法域1445限定；条件保normalizer有限，G1/G6接受。|
|RW-L1455-S01，“唯一p*”|softmax指数q/alpha正规化得唯一最优分布，正q升其概率；KL证支持唯一，G1/G6接受。|
|RW-L1458-S01，1458--1459首句，“Z/logp*”|定义分区和Z，由p*=exp q/alpha除Z得logp式；记号转换目的供KL化，G6接受。|
|RW-L1459-S02，“任意p”|在全合法simplex内写目标为常数-alpha KL，候选域仍同，不转任意实向量p；G6接受。|
|RW-L1466-S01，“KL非负仅相等0”|最大目标时KL最小0且p=p*，故值alpha logZ/唯一性；运算选择明确，G6接受。|
|RW-L1466-S02，“q有限支撑正”|所有exp正/finiteZ保证p*>0，p0时p logp比按0极限，未漏零支持除；条件实际用，G1接受。|
|RW-L1469-S01，“熵位置约定”|固定pi Q不含当前熵、V含当前熵，设一致软备份；当前约定目的避免重复加entropy，G4/G6接受。|
|RW-L1479-S01，“Q不含/V含”|精确规定熵从当前动作pi中只记V、Q记future V；后SACtarget位置一致，G6接受。|
|RW-L1479-S02，“软改进来自变分”|固定q softmax最大q+entropy产生softpolicy improvement，具体已1453/1455，G7接受。|
|RW-L1479-S03，“连续积分需有限”|finite sum→continuous integral须Z/entropy/return可积，unbounded动作常数q exp不可归一；正反例和失去条件本地，G3/G7/E10接受。|
|RW-L1481-S01，“Boltzmann难抽”|continuous指数q分布难归一/抽样，SAC用参数pi近似软改进；旧解缺口与新接口先给，G5接受。|
|RW-L1481-S02，“重参数化”|先抽独立theta noise，再可微变换a，让Q动作导传actor；术语/可计算机制同句，G4接受。|
|RW-L1481-S03，1481--1484，“有界例”|Gaussian u均值尺度由pi网络出，epsilon标准正态，a=tanh u有界；均值/尺度/随机源/变换完整，G6接受。|
|RW-L1485-S01，“密度Jacobian”|动作(-1,1)密度要减log tanh导行列式，换变量而非仅Gaussian u密度；局部可算目的先给，G6接受。|
|RW-L1492-S01，“物理缩放”|再线性scale动作区间需另Jacobian logdet，不能把归一坐标熵当physical熵；范围转换改变密度/尺度明，G7/E10接受。|
|RW-L1492-S02，“漏影响三项”|遗漏变换项改变熵、pi梯度及温度调节，因这些都用logpi；可追计算对象非泛影响效果，G2/E2接受。|
|RW-L1494-S01，“critic记录/actor新抽”|critic评真实buffer sa，actor在buffer s抽currenta升softvalue；两数据接口对象明确不监督动作模仿，G2/G5接受。|
|RW-L1494-S02，1494--1496首句，“无独立V版本”|指定常见SAC无Vnetwork，nexta'由currentpi，currenta_theta重参数化；版本/随机源/时点就地，G3/G6接受。|
|RW-L1496-S03，“目标双损失”|batch中target软Q自举、Q回归记录动作、pi用新动作，先数据角色后式；G6接受。|
|RW-L1511-S01，“固定w保a导/stop y”|actor不更新critic params但Q对a导仍过pi，criticstop整个y；路径分开而非去Q所有梯度，G2/G6接受。|
|RW-L1511-S02，“两路径图”|图视觉分离记录动作eval和reparameterized动作提高softQ，接受。|
|RW-L1511-S03，“精表迭代非任意深网”|exacttab softpolicyiter条件不能证twoapproxnetworkloss任意buffer稳；明确对象/范围变化条件失效，G1/G7/E10接受。|
|RW-L1520-S01，“目标熵调温”|H0目标熵决定alpha自适应，而非固定alpha任选不变；新control对象/目的明确，G4接受。|
|RW-L1520-S02，1520--1523首句，“exp xi loss固定pi”|alpha=exp xi保正，下降Ealpha(currententropy-H0)，该步pi samples/logprobstop；参数/方向/数据时点说明，G6接受。|
|RW-L1523-S02，“低熵升xi”|H-H0负则gradxi负，下降让xi增alpha增熵奖励；高熵反向，符号/评价方向可检，G1/G6/E12接受。|
|RW-L1523-S03，“continuousH0可负”|微分熵依scale可负，非离散动作数log；1443有背景本地恢复需要的区别，G7接受。|
|RW-L1523-S04，“顺序与版本”|无V/autoalpha为后续版本须别于最初SAC，算法声明版本targetcurrenta'；历史归因外源未核，正文范围限定接受。|
|RW-L1544-S01，1544--1546，“人工目标.82”|r.1/gamma.9/z0，minQ.7与logpi-.5 alpha.2给future.8、y.82；教学人工非实测，G6接受。|
|RW-L1547-S01，“tableQ .622”|currentQ.6 loss halfsquare grad-.22步.1加.022，更新.622；scalar/table假设而非任意network输出，G1/G6接受。|
|RW-L1548-S01，“pi loss -.81不是步长”|current新a minQ.65 logpi-.8贡献-.81，但必须密度及Q_a导定paramupdate，loss数不独定grad；值/梯度对象明确，G2接受。|
|RW-L1548-S02，“不是记录a监督”|actor用currentpi重采a最大softq，不将buffer动作当标签拟合；原/新数据接口明确，G1/G4接受。|
|RW-L1550-S01，“离策略近端可组合”|数据复用/策略变化约束可另组合，非互斥四class；G2接受。|
|RW-L1550-S02，“比率位置/旧参数”|表对照ratio校哪里和oldpi谁，不把分布式采样自身保学习；承载对象/判定标准具体，G2/E3接受。|
|RW-L1570-S01，“ACER补偿”|截rho需保被截部分期望补项，否则另有偏梯度；不是所有截断均不变目标，前530/533呼应具体权位置，G1/G7接受，外证未核。|
|RW-L1571-S01，“三个职责”|Retrace是critic目标、trustconstraint限幅、支持是数据覆盖，互不替代；关系两端/性质一一给，G2接受。|
|RW-L1573-S01，“MPO两步”|nonparam动作分布改进+parampolicy拟合分开控制改进/投影；表已给E/M各操作非裸缩写，G4接受。|
|RW-L1573-S02，“state覆盖未解决”|buffer s仍behavior，动作KL不造没见s信息；原动作域约束扩大到状态访问不继承覆盖，G7/E10接受。|
|RW-L1576-S01，“IMPALA已出现”|该名回指之前Vtrace评行为/learner差，表1560本地给需要的机制；不是单靠读者找全章，G7接受。|
|RW-L1576-S02，“APPO看实现”|APPO版本族需具体文档确定target/ratio同步，而非每同名同目标；当前表1562明确不同角色可存在，不作为已核来源结论。|
|RW-L1577-S01，“版本配置旧pi”|训练报告需保version/config不能缩写省oldpolicy定义；可检验要求约束报告内容、对象分布角色明确，G1/E3接受。|

## 特殊单元

|ID、位置|白话与具体依据|
|---|---|
|RX-L1396，1396--1406|缺连续a可算pi参数回报导，det f与pi诱导currentd，Qpi动作导乘f参数Jacobian再平均d/1-gamma；可微可积条件1395、critic derivative误差限制1407，接受G6。|
|RX-L1411，1411|缺DDPGcritic目标，r+gamma(1-z)targetQ(s',targetf)使用慢参数/truez；同targetcritic/actor区分1414，接受。|
|RX-L1413，1413|actorreplays上f导链Q_a用于proxy，1417--1421明不无条件等currentd精梯度，不能用公式单独盖精确PG，接受。|
|RX-L1418，1418--1420|缺另replay目标明确，nu为固定buffer初始，Jnu=E_nu Vcurrent，精grad未来占用不只nu；动机1417、运算/平均对象明，接受。|
|RX-L1424，1424--1431|缺TD3目标平滑与保守估，人为noiseclip[-c,c]后proj合法A，twoQtarget取min加r；候选是两估量非真实环境worstmodel，min针对过估，投影维护合法动作，低估/过平滑1434，接受G6。|
|RX-L1437，1437--1441|缺将随机性入优化目的，alpha正权entropy(-logpi)与r同折扣和，期望策略轨迹；continuousreference与可积边界1443/1479，本目标非原J方差工具，接受。|
|RX-L1443，1443，H(p)|finite合法a分布熵-sum p logp，均奖散程度、p0按极限；continuousdensityscale不同明，接受。|
|RX-L1450，1450--1454|缺fixeds soft选a分布精解，allowp合法finite simplex，metric平均q+alphaH求大，变为alpha logpartition；候选集/为何不hardmax1445，KLproof保障，接受G6/E9。|
|RX-L1455，1455，p*|p*softmaxfiniteqa/alpha positive normalized，unique由KL非负等号onlysame；允许域与归一条件明，接受。|
|RX-L1458，1458--1459|Zsumexp给logp*变换，为target转KL；不混随机回报Zpi同符号此Z局部明确声明，接受。|
|RX-L1460，1460--1465|任意p目标=alpha logZ-alphaKL(p||p*)，求大=求KL小，positivep*支持保证定义，finiteZ已qa条件；接受。|
|RX-L1470，1470--1478|缺soft回报一致备份，Q当前奖不含当前entropy但后futureV含，V当前pi平均Q-alpha logpi；避免多次加entropy而Jalpha回报位置一致，1479明，接受。|
|RX-L1482，1482--1484|缺paramsoftpi可抽/可导，epsilonindependentGaussian,u=m+sigma*noise,a=tanh u归一bounded；positivevariance作为Gaussian密度模型条件语义，未要求完整网络clamp实现，接受。|
|RX-L1486，1486--1491|缺a实际密度entropy，logGaussian u减sumlog(1-tanh²u_i)为变换Jacobian，dimensioni各动作轴；后physicalscale另det，漏项后果1492明，接受G6。|
|RX-L1497，1497--1510|缺SAC当前pi近soft改进：nexta'currentpi/targetQmin生成stopy，critic记录a halfsqbatchloss；actor在buffers重采aθ以alpha logpi-minonlineQ求小，Q_a留/paramswfreeze，1511解释；batch经验代理非原J精梯度，接受G6。|
|RX-L1521，1521--1522|缺alpha适配目标H0，alphaexp xi使正，fixedlogpi样本下下降alpha(H-H0)，低熵gradientnegative升alpha；不是独立把pi同时导进去，1523方向明，接受G6/E12。|
|RA-L1528，“初始化”|pi/twoQ/targetQ/alpha/真实buffer初始，输出角色完整，接受。|
|RA-L1529，“每真实步”|交互计数循环不是每gradient必新data，接受。|
|RA-L1530，“currentpi执行”|采currenta真实执行记录sa/r/s'/z，预热可指定randompi；初始无需用空buffertrain，接受。|
|RA-L1531，“写buffer/重置”|真终或环境时间限reset，其他续s'，真实数据流明，接受。|
|RA-L1532，“timecutz0保末s'”|截断不是终止，记录末后继不能换新起点观测作目标，接受。|
|RA-L1533，“规定U梯度”|数据复用U预选，不把同一记录U次视环境独立U次，接受。|
|RA-L1534，“nextcurrenta'/stopy”|currentpi在s'抽target动作，targetQ慢params，wholey停止grad；接受。|
|RA-L1535，“twoQ分别拟合”|onlyonlineQ降half平方，不通过targetnet/targeta反传；接受。|
|RA-L1536，“当前重采/固定w”|actorbufferstate新a重参数化，固定Qparams但留Q_a导，区别记录动作；接受。|
|RA-L1537，“autoalpha固定输出”|auto温loss单独更alpha，policylogdensitystop，接受。|
|RA-L1538，“targetslow跟”|barw←(1-tau)barw+tauw慢跟，tau此处作混合系数非分位tau；“缓慢移动/跟踪”约束小混合，完整实现需取0<tau<=1，非已实验配置，接受。|
|RT-L1557，“校正位置接口边界”|比较数据reuse/滞后/更新约束各位置，不等分布式体系保证，接受。|
|RT-L1559，“ACER”|truncatedrho加biascomp、Retracecritic、strategy约束，回放/当前组合；截后删comp不是同estimator，接受。|
|RT-L1560，“IMPALA”|Vtrace修behavior/learner差，阈值影响targetpolicy；前533/544本地指具体目标改变，不借名称盖同policy，接受。|
|RT-L1561，“MPO”|E改动作分布受KL，M约束下拟parampolicy；动作改进与statecoverage分问题，接受。|
|RT-L1562，“APPO”|asynVtrace+proxyratio，可有behavior/target/learner三版本需sync/ratio明；这是实现族概览非唯一原公式，接受。|
|RC-L1565-S01，“三维组合”|数据reuse、policy滞后、更新constraint可组合非互斥四class，接受。|
|RC-L1565-S02，“版本不同目标”|APPO各实现target定义不同须记录版本不共保一个estimator；受限陈述未外核实现docs，接受范围说明。|
|RC-L1516-S01，“SAC梯度职责”|diagram关注记录/新动作两梯度非soft理论curve，接受。|
|RC-L1516-S02，“上下/next当前/target慢”|upperrecordeda critic，下currentactor抽aθ，nexta'currentpi配慢targetQ；正文/伪码一致，接受。|
|RF-sac-L06，“真实buffer五元”|真实sa/r/s'/truez为critic样本，接受。|
|RF-sac-L07，“twoQ(s,a)”|top组件评记录a，对actor另以aθ求Q_a，图箭头25标固定w保Q_a并结合actor到loss18表模型重用，不误用记录标量导，接受。|
|RF-sac-L08，“critic halfsquare”|预测Q-record与stopy残差half平方，仅updatew，接受。|
|RF-sac-L09，“stopy后softvalue”|targetminQ与entropyfuture停止grad，接受。|
|RF-sac-L10，“actor aθ=f(s,epsilon)”|当前s独立noise可导抽currenta，不使用recordeda标签，接受。|
|RF-sac-L11，“alpha logpi-minQ”|actorloss下降提高softscore，动作相关Q导留；符号方向与1508一致，接受。|
|RF-sac-L12，“targetQ/currenta'”|target慢Q，但a'currentpolicy，无旧targetpi误用，接受。|
|RF-sac-L13，“记录动作”|buffer→onlineQ评真实a，接受。|
|RF-sac-L14--15，“Q/y送LQ”|recordprediction和fixedfuturetarget构criticresidual，接受。|
|RF-sac-L16--17，“s送actor”|buffer仅state送currentpi，与动作另重抽区分，接受。|
|RF-sac-L18，“重采样到Lpi”|pi新动作logpi/Q评价参与actorloss，接受。|
|RF-sac-L19，“target到y”|targetQnexta'构softfuture，接受。|
|RF-sac-L20--21，“r/z不求梯度”|recordr/z给target计算不为actorpathbackprop，接受。|
|RF-sac-L22--23，“s'到target”|buffer后继currentpi抽a'配targetQ，与1500含currentlogpi一致，接受。|
|RF-sac-L24--25，“固定w留Q_a”|用同Qcomponent给actor动作评价但paramswfixed、Q对新a可导，不把recordedQscalar复用为a导；body1494/1511明确对象，接受。|
|RF-sac-L26--27，“reparamgrad”|actorloss经aθ参数导更新theta，不updateQparams，接受。|
|RF-sac-L28--29，“仅updatew”|criticloss反向仅onlineQ，不targety，接受。|
|RF-sac-L30-S01，“target慢跟w”|barQ缓慢跟onlineQ，1538给混合更新而非independent fit，接受。|
|RF-sac-L30-S02，“温度另调”|alpha与policy/Q不同步目标熵loss，1523/1537明stopoutput，接受。|

## 关键链与范围

- RI/RM-DPG：连续a无法枚举→Q_a局部升值→detf链theta导→currentd精梯度→DDPGreplaystatesproxy，nu非currentd→定义Jnu仍需nu起后占用→TD3minQ/targeta平滑/actor延时分别改误差。真实动作噪声不等目标noise或maxentropy目标。
- RI-maxentropy/SAC：随机det执行noise只采样→分散本身入Jalpha→fixeds合法simplex平均q+entropy→KL变分softmax→连续Z有限/可抽困难→parampi可重参数化Gaussian-tanh和Jacobian→criticrecorded动作/actor新抽a、stopy、Q_a导→alpha按H0单独更新。
- 公式方向：entropy目标增大Jalpha，局部p最大q+alphaH；SACactor最小alpha logpi-minQ，critic最小half平方；温度最小alpha(H-H0)低熵使alpha升。min两Q为过估计抑制，不是允许模型集合的worstcase，不与risk目标混。
- RS-1417/1421：currentd→fixedbuffernu，数据复用不保起点J精grad；RS-1443/1479：finiteprob→continuousreference density，需finiteZ/可积且entropy依scale可负；RS-1492：归一a→physicalinterval加Jacobian；RS-1511：exacttabsoftiter→approxnetworkloss任意replay不继承收敛。
- RS-1550--1577：三policy角色/实现族替单oldpolicy时，ratio/target同步需明，不能据同缩写推同estimator。此块无新必改发现，已核数据/梯度与教学数值一致。
