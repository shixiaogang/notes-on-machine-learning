# CH03-R1 接管者W遍：L1840--1970

同一接管者人工W1--W6及特殊单元；MuZero/TD-MPC源图亲读全部标签和关系。版本/身份/禁读边界同resume，未核一手论文实验、完整证明、程序或PDF。下一块从1971继续，模型误差界证明尚未在W判结论。

|ID、位置短引|白话意思；具体依据或发现|
|---|---|
|RW-L1844-S01，“搜索要分支奖值”|左右选择直接需分支r/长期V，不需恢复所有背景像素；局部可计算任务先于模型名，G5接受。|
|RW-L1844-S02，“所用深度保预测/提议”|latentmodel保该展开深度决策量、给值得查动作才能可能支持planner；能力条件/范围有限不假定全环境保真，G1/E3接受。|
|RW-L1844-S03，“MuZero无需重建”|search-oriented e/g/f，不强求完整observationreconstruction，但仍需decisionprediction准确；输出要求减不等准确性免，G2/G4/E4接受。|
|RW-L1846-S01，“e避h历史混淆”|e_phi命名表示函数与h_t环境历史区别，局部符号角色明确，G4接受。|
|RW-L1846-S02，“history编码/动力预测头”|真实h编码z0，g预测r/nextz，f给p/v，数据到接口连续具体；G6接受。|
|RW-L1853-S01，“prior非访问/v非根return”|p是searchinput动作prior，不等searchoutputN分布；v是leaf未来，不含path奖；两重要比较对象明，G2接受。|
|RW-L1853-S02，1853--1854，“边奖折扣备份”|沿edgeG_k=rhat_k+gammaG_next，必须奖励加后值，非copyv；目的/索引/操作都有，G6接受。|
|RW-L1855-S01，“-.04/.8→.68”|新edge奖-.04/gamma.9/leaf.8给.68不是.8，手算映射作用明确；不称是真网格精确搜索值，G1/G6接受。|
|RW-L1857-S01，“有限展开分配”|searchbudget要兼当前高return与prior高未访a，给PUCT动机；具体actioncandidate/数值信号先，G5接受。|
|RW-L1857-S02，“N/Qbar”|节点存accesscounts和meanreturn，各变量类型/时点明确，G4/G6接受。|
|RW-L1857-S03，“合法return加explore”|在合法branch取Qbar+prior*countbonus高者，constantc PUCT只是说明形式；候选/方向/bonus样本少目的给全，G6/E9接受。|
|RW-L1865-S01，“实际配置细节”|actualMuZero会变c、normalizevalues、rootnoise需taskconfig，式为constantc接口非统一实现；模型版本/证据范围明确，G1接受，历史原文未核。|
|RW-L1865-S02，“树选叶扩备份”|score沿现tree到leaf，g调用生nextlatent/f预测，再path增加N更meanQ；完整一次simulation操作/模块顺序可复述，G4/G6接受。|
|RW-L1865-S03，“search与supervision分”|图将modelplanning内部统计和真实data目标分开，不把simulation当real观测，G2接受。|
|RW-L1874-S01，“根快照均值.7933”|人工右N2 Qbar.85、上N1 .6，新rightreturn.68后N3 mean(1.7+.68)/3=.7933；明确统计数据人工，计数/平均单位相同，G6接受。|
|RW-L1874-S02，“温1访问目标/温0”|totalN4 right3/up1给searchpi(.75,.25)，温降至0选最大N；target来自searchvisits而非当前p原值，G6接受。|
|RW-L1874-S03，“非环境四步”|N为模拟次数不是同s四次trueactions，资源/证据对象明确，G1/E3接受。|
|RW-L1876-S01，“统计用于train”|searchN形成policytarget，连接planningoutput与network下一轮prior；新监督用途非重讲同counts，G4/E6接受。|
|RW-L1876-S02，“真实actions展K/三目标”|realbuffer起点后actions rolloutlatentK，rhead拟真r，vhead真n奖+末searchV，phead拟searchN分布；每训练模块输入target/生成路径明，G6接受。|
|RW-L1876-S03，“searchpi/zV/sumloss”|searchpi保存或recompute，zV为nstep目标，在各kposition累三loss最小phi；候选modelparams/标签版本来源/方向明确，G6/E11接受。|
|RW-L1887-S01，“终止/棋类/Atari目标”|真实terminaltruncate奖与自举；chessfinaloutcome可target，Ataritransformeddistvalue另版本；环境/目标切换声明不当同scalar数字，G3/G7/E10接受。|
|RW-L1887-S02，“r索引不移位”|r_t+k为执行记录a_t+k后奖，latentfirstedge奖与real第0转移对齐；具体错误风险和正确索引明，G1/G6接受。|
|RW-L1887-S03，“三模块/下批重搜索”|opt三loss改e/g/f，下一realinteraction新modulessearch，改policytarget再fit循环；状态变化/训练使用关系完整，G2接受。|
|RW-L1889-S01，“EfficientZero补强”|finite真实data下监督latent与realnextencoding一致、valueprefix降逐reward误差、oldtargetoffpolicy修正/reanalysis；核心新增作用具体，不是重建头名词，G4接受。|
|RW-L1889-S02，1889--1890，“q一致性”|predictorq用负cos(predlatent,targetencoderrealobs)且targetsg，目标对象非Q动作价值此q“预测器”本地明设；G6接受。|
|RW-L1891-S01，“stopgrad非防塌缩”|sg仅让targetbranch当前loss不同步更新，常量representation仍可一致，完整design才稳；具体机制与不能推性质明，G1/G2接受。|
|RW-L1891-S02，“非加重建自动效率”|EfficientZero是MuZero数据/target改进组合，不等任意额外reconstructhead同sampleefficiency；保证对象/比较scope限定，G1/G7接受，来源未核。|
|RW-L1893-S01，“两类要求表”|重建与decisionprediction分对应不同检查对象，表第三control充分是条件层，不硬当互斥第三model类，G2接受。|
|RW-L1893-S02，“行为轨迹准反事实可错”|在behavior路径value预测准不保rareactioncombo/deeper展开，no-rebuild仅免输出非免反事实检查；新范围不可继承部分具体，G1/G7/E10接受。|
|RW-L1893-S03，“执行search统计非prior最大”|deploy主要searchvisits选a，若单独argmaxp是另protocol；训练prior预测存在不改变执行接口分类，G2接受。|
|RW-L1915-S01，“MuZero树离散”|已tree分配finitebranchsimulation，恢复前对象以转continuousseq，G7接受。|
|RW-L1915-S02，“continuous∞candidate”|continuous节点无限a，因此另一方式直接sampleopt shortseq；旧树枚举缺口/新接口本地，G3/G5接受。|
|RW-L1915-S03，“TD-MPC组件”|latentdynamics预测短r/z，Q估tail，policyprior提部分candidates减search；模型/预测对象/数据flow及时解释，G4/G6接受。|
|RW-L1915-S04，“提议不等执行”|图分priorproposal与最终plannedscorechoice，即使trainprior最终a仍planner；关系两端/角色具体，G2/E2接受。|
|RW-L1924-S01，“真实s编码/latentnext”|realcurrent s→e z0，candidatea→d nextz，控制预测链清楚不冒realobs，G6接受。|
|RW-L1924-S02，“L奖加末先验Q”|为比合法seq，短predr sum，tail调用priora和Q补future；为何需tail/集合/评分方向1915明，G6/E11接受。|
|RW-L1930-S01，“先无终/有终继续mask”|score示例片段先不终，若终用cumcontinue遮后r/tail，MVE式本地恢复要用的mask性质；G1/G7接受。|
|RW-L1930-S02，“尾Q不重复L动作奖”|prefixr只0..L-1，tailQ at zL包含aL奖，所以无重复；索引与对象解释完整，G6接受。|
|RW-L1930-S03，“Gaussian和prior候选/first”|candidateproposal可mix Gaussianperturbseq/priorrollout，高scoreweight或elite优化后仅firstexecute；方法机制前CEM/MPPI已讲，回指用途明确，G7接受。|
|RW-L1930-S04，“prior提高不必firstprior”|planner不同候选score maychoose非prior(z0)，prior训练不等唯一executor；图/候选机制支持，G1/G2接受。|
|RW-L1932-S01，“真实序列三loss”|真实短序列作latent一致/r预测/Q-TD监督，明predictiontarget来源；G6接受。|
|RW-L1932-S02，“sg单步形式”|sg停target导，给scalarone-step核心关系非TD-MPC2全实现；scope与符号就地，G4接受。|
|RW-L1946-S01，“target编码/多步深度权”|barznext来自targetencoder真s'，predbranch沿recordeda递归、多k加权loss；真实目标/latentprediction不混，G6接受。|
|RW-L1947-S01，“prior升Q/recordedmodel”|prioropt Q(z,pi(z))时freezecriticparams，model/valuefitrecordactions；不同训练动作对象具体，G2接受。|
|RW-L1947-S02，“版本核心非全实现”|targetnet/norm/regularizer/Qensemble随版本，式只originalcore接口不等TD-MPC2，原历史归因/全代码未核但范围准确。|
|RW-L1949-S01，“TD-MPC2设计”|shortplan/tailV保，加SimNorm、distreward/value/Qensemble/maxentprior；每组件后明作用，不等简单samplebudget统一，G4接受。|
|RW-L1949-S02，“组softmax限制scale”|vector分组softmax各非负和1限制潜表示尺度，不产生dynamicsconfidence；性质可由softmax定义算，G1/G2接受。|
|RW-L1949-S03，“不同scale/overestimate/coverage”|distributional目标用于rewardscale优化、Qensemble抑部分过估，仍不能替真实sa访问；每组件作用及limit具体，G1/G7接受。|
|RW-L1951-S01，“104域/317M80非统一预算”|论文在线104task四domains另multitask，317M/80tasks setting不能当全部baselines同预算；数据范围/单位明确，外源未核不判实证正确。|
|RW-L1951-S02，“协议内经验非排序”|结果只相应data/model/task协议证据，不证latentplanning一定胜treesearch；比较scope清楚，G1/G7接受。|
|RW-L1953-S01，“按query非name”|table比较实际modelcall结构，避免方法名称混同计算资源；指标对象明确，G2/E1接受。|
|RW-L1953-S02，“NLM与tree拓展”|fixedtotalB下N长度L每Mparticles需NLM transitions；tree每sim常一newnode仍走旧path/维护stats；不同调用/遍历单位清楚，G6接受。|
|RW-L1953-S03，“query不等walltime”|batching/actiondim/leafeval成本不同，samecount不等sameelapsed；可比较量/单位/条件明确，G2/E1接受。|

## 特殊单元

|ID、位置|白话与依据|
|---|---|
|RX-L1847，1847--1852|缺search所需latent/r/p/v输出，historye编码z0，g(z,a)给r/nextz，f(z)给prior/leafV；模块类型/输入output明确，1844先需branchdecisionobjects，接受G6。|
|RX-L1854，1854|edgebackupG^k=rhat^k+gammaGnext，leafvalue未来与路径奖分角色，示例-.04+.9*.8=.68，notcopyv；接受。|
|RX-L1858，1858--1864|缺finiteexpand分配，legalb max Qbar+cp_b sqrt(sumN)/(1+N_b)，Ncounts/pprior/Qmean各1853/1857定义，少visited高priorbonus与highreturn兼顾；cconstantillustration实际配置1865，acceptG6/E9。|
|RX-L1874，1874，N/mean/searchpi|rightoldsum=2*.85，new.68，总N3/Qbar.7933，上N1，温1 searchpi3/4 1/4，温0maxcount；searchsim不是trueactions，接受。|
|RX-L1877，1877--1886|缺把searchlearning三targets写可trainphi loss，zV_n=realnreward+gamma^nsearchV，v/p lossesk0..K，r lossesedgek0..K-1；crossentropysearchprob与priorlogp匹配，realsamples/actions1876，termstop1887，接受G6。|
|RX-L1890，1890|缺finite-data latentconsistency目标，负cos(q(predz^k),sg(e(realobs_t+k)))，targetnotupdate此loss；停止grad不保无collapse1891，scope为illustrativecore非完整algorithm，接受。|
|RT-L1900，“requirement/check/不能推”|比较reconstruct、value/policy预测及control充分条件，非按imageprecision统一quality，接受。|
|RT-L1902，“reconstruct观测”|current/futureobs error/likelihood不自动保关键a排序/OOD/safety；模型prediction对象和control要求不同，接受。|
|RT-L1903，“r/v/p预测”|specifiedactionseq奖励、policyrelatedV/searchpi训练，不能保allpolicy/all-depth/fullrules；allowedtestscope明确，G3接受。|
|RT-L1904，“control充分”|所需policy/interventions保decisioninformation，不超声明task/controlset任意有效；candidate范围从实际任务需来而非无限族，接受。|
|RC-L1907-S01，“rebuild/valuepred”|这两不同outputrequirement不是统一model排行榜，接受。|
|RC-L1907-S02，“任务定要求”|要求按model所承担decisions/outputs/testset确定，不以视觉fine粗代排序；table具体承载对象/指标明，G1/E3接受。|
|RX-L1925，1925--1929|缺shortcandidateexpectedscore，sumj0..L-1 gamma^j learnedr加gamma^L Q(zL,prior(zL))，legalfiniteLseq来源1924、prefix/tail范围1930解释；noend先限定，有endmask非后猜，接受G6。|
|RX-L1933，1933--1944|缺latent/r/Q三监督从realshortseq，targety=r+gamma c targetQ(targetznext,currentprior)，latentdpred匹配sg(targetencoding)、rfitrealr、Qfitstopy，lambda_z/r/Q为lossweights；sg/真s'来源/多步动作本地1932/1946清楚，接受。|
|RX-L1949，1949，SimNorm|latent分组softmax各组非负和1，限制scale不是statisticalconfidence；候选boundedrep语义不同modeluncertainty，接受。|
|RX-L1953，1953，NLM|每candidateLtransitions、Mparticles、Ncandidate product，在fixedB争预算，tree扩newnode另旧pathcost不能同claimwalltime；units全部定义，接受。|
|RT-L1960，“接口/模块/动作/预算”|按call部件和searchstructure比较，query计数不等实际运行时，接受。|
|RT-L1962，“latenttree”|e/dynamics/r/prior/leafV，finitebranchesdirect、continuous需候选，budget在branch复用N/Q统计，接受。|
|RT-L1963，“trajectorysampling”|dynamics/r/optiontailV，vector合法约束可jointsample，N/M/L/I争预算；不保复杂动作采样全局最优，接受。|
|RT-L1964，“value短规划”|latentdynamics/r/tailQ/prior，用Q代longrolltail、queries短候选优化，commoncontinuous但非独立互斥optimizerclass；接受。|
|RC-L1967-S01，“同budget异计算”|samequery需别whichmodule/sequence/treepath，不混walltime，接受。|
|RC-L1967-S02，“valueguide可组合”|tail评估构成方式可与CEM/MPPI等采样optimizer组合，层级关系明确，G2接受。|
|RC-L1870-S01，“MuZero搜索学习”|图twoflow不是realonlyreplay，接受。|
|RC-L1870-S02，“边r折扣v/三supervision”|toplatent展开/r+futureleaf回根，bottomrealr/value并searchcounts监督prior；targets不同input来源明确，接受。|
|RC-L1870-S03，“潜在非obs/count非真频次”|latentnext未真实发生，searchN分布非记录a频率simplecopy；模型规划证据与经验输入区别，接受。|
|RC-L1920-S01，“valueguide latentplan”|图以短predr/tailcritic评序列而非直接policy输出，接受。|
|RC-L1920-S02，“realroot/尾Q/prior部分”|多轨迹共同realcurrentroot、tailcritic、prior只部分候选，score选择执行；source/role明确，接受。|
|RC-L1920-S03，“training不等deployprior”|bottomrealtrainmodel/r/TD，与执行planner查modeldifferentdataflow；不因prior训练改分类，接受。|
|RF-muzero-L07，“realhistory/e”|rootlatentfromh_t真实obs历史，不是全kernelknown，接受。|
|RF-muzero-L08，“z0”|e输出当前rootlatent，接受。|
|RF-muzero-L09，“z1_u”|上a分支modelnextlatent，notrealobs，接受。|
|RF-muzero-L10，“z1_r”|右a分支modelnextlatent，两potential后继非同sample确定，接受。|
|RF-muzero-L11，“leaf f/prior/value”|head给inputpriorp/leafv，不是searchreturn/winningrealobservedvalue，接受。|
|RF-muzero-L12--15，“history→root/上右/leaf”|rootencodedthenlatentg按action展开、f叶预测，实际模型调用16label说明，接受。|
|RF-muzero-L16，“edgeg给r/z'”|steptransitionlearnedg分别预测reward与latentnext，输入actorlabel两branch明，接受。|
|RF-muzero-L17--18，“r+gamma v返/NQ”|leaf未来乘discount加edgepredr，path统计N/Qmean更新，notcopyv，接受。|
|RF-muzero-L19，“real后actions/r”|realtrainsequence数据源，与topvirtual展开区别，接受。|
|RF-muzero-L20，“r/vloss real+bstrap”|rheadfitrealr/vheadrealnreward+searchtail，latent展开按recorda，接受。|
|RF-muzero-L21，“policyfitsearchcounts”|targetpolicy来自N而不是realactionfrequency，接受。|
|RF-muzero-L22，“real→r/vtarget”|真实路径监督reward与valueestimate，not潜预测自证true，接受。|
|RF-muzero-L23--24，“rootsearchpi∝N^(1/tau)”|searchvisitcounts温度变为policytarget，tau为searchtemperature而非分位概率，1874本地有温值作用，接受。|
|RF-muzero-L26-S01，“record动作展开三target”|trainlatent按realactions展开fit三supervision，samephi modulesoptimization，接受。|
|RF-muzero-L26-S02，“每步重search/prior输入”|执行planneraction而prior只是searchguidance，不当directpi共类，接受。|
|RF-tdmpc-L07，“realroot z0=e(s)”|各candidate共同实测state编码，不从模型虚构start，接受。|
|RF-tdmpc-L08--13，“三路潜点”|三candidate各两点示意shortlatentroL不表示固定L2所有任务；root→各predpoints→tail评分关系全核，接受。|
|RF-tdmpc-L14，“累计r+tailQ”|prefixpredr discount+tailQ补future，1927/1930定义无doublecount，接受。|
|RF-tdmpc-L15，“highestseq/firsta”|score max candidate输出firstonly，prior不唯一executor，接受。|
|RF-tdmpc-L16--20，“三trajectory汇尾”|各predseq共享root独立候选评到tailQ汇score，而非中间混路径转移，接受。|
|RF-tdmpc-L21，“评分→act”|plannercomparison选executedaction，接受。|
|RF-tdmpc-L22，“prior提部分”|policyproposal参与candidate构造但非直接decider，接受。|
|RF-tdmpc-L23，“prior进一部分路线”|arrow示onlycandidatebranchproposal，不等将所有路线绑prior，接受。|
|RF-tdmpc-L24，“其余trajectorynoise”|othercandidates来自perturbedseq，和1930混提议一致，接受。|
|RF-tdmpc-L25，“realshort五元c”|model/value监督使用trueaction/r/next/c，接受。|
|RF-tdmpc-L28-S01，“一致/r/TD”|latentnexttargetencoding、rreal、Q-TD三损失明确1938--42，接受。|
|RF-tdmpc-L28-S02，“prior升Q”|prioractor独立提高critic评价，不把recordaction直接作为label，接受。|
|RF-tdmpc-L29--30，“realtrain→model”|虚线trainingfromtrue_sequence更新模型/值，区别实线planner调用，接受。|
|RF-tdmpc-L32-S01，“实plan虚train”|明确关系类型，notdash代表低信度或可达性，接受。|
|RF-tdmpc-L32-S02，“prior非唯一执行”|prior减search负担，但最高score可选otherproposal，1930具体机制支持，接受G2。|

## 关键单元

- RI/RM-MuZero：左右分支决策需r/value非pixels→realhistorye→g latenttransition/reward+fprior/leafv→PUCT有限展开次数→edge奖励加future值pathbackupsN/Q→searchNtargetpi→realrecord动作latentunrollK→realr/nreward+searchV/searchcounts三supervision→newmodules下轮search。目标和候选范围均来自本地数据流，不以模型生成后继当新真实观测。
- RS-1887/1893：训练各任务value目标/表示有差→term截断/chessfinal/Ataritransform；behaviortrajectory预测好不能继承rare反事实/deeper任意展开，no-rebuild不是免controlpredictioncorrectness。执行独取priorargmax为另一协议。
- RI/RM-TD-MPC：离散treefinitebranch→continuous∞candidates→shortsequenceproposal→realencodedroot/modelshortpredr/z→tailpriora+Q→合法seqscore比较firstexecute→realshortdata三loss/targetencoder/stopTD→prior单独升Q。原始核心loss不是TD-MPC2完整代码。
- RS-1949/1951：SimNorm尺度约束/分布目标/Qensemble是训练机制，不是动力学confidence或coverage证书；104task与317M80task是不同实验setting，不能全baseline同预算。RD-1953：transquerycount、旧tree路径遍历、leafcalls与walltime不同。
- 本块无新必改发现。模型利用偏差反例L1975--1981与模型误差界L1991以后已取到工具输出，但尚未写本人的W完整覆盖，不称W已完成至那些位置。
