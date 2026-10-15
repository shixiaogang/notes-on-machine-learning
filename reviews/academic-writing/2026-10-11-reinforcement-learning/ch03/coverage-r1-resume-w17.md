# CH03-R1 接管者W遍：L2501--2669

人工W1--W6与所有特殊单元；hierarchy及skill-regions图源亲读。Option-Critic原完整梯度证明未外核，仅核正文局部推导、归一与数例；其他方法原文归因未核。不存在的option-critic/complexity图路径读取失败不作覆盖，实际本块只有上述两图。

|ID、位置短引|白话；具体依据或发现|
|---|---|
|RW-L2501-S01，“fixed内部如何获得”|Option备份已固定inner/stop，转学习二者，具体缺口与局部入口明，G5/G7接受。|
|RW-L2501-S02，“手工door高低IO”|low格点/door→方向可auxreward；high房间/task→subgoal按originalreturn；两不同训练目标明，G2/E3接受。|
|RW-L2501-S03，“OptionCritic外回报”|可不预设door、用externalreturn训internalpi/stop，改变先验对象具体，不称自动discover最优门技能，G1/G3接受。|
|RW-L2501-S04，“图奖励分层”|图分high/low IO及reward，避免auxglobal混，接受。|
|RW-L2510-S01，“每步继续或重选”|Option执行时每步nexts可keep或terminate，评价需omega状态，不等普通singleQ(s,a)，G5接受。|
|RW-L2510-S02，“两后续分别估”|critics分别估继续omega与high重选后值，预测对象先公式建立，G6接受。|
|RW-L2510-S03，2510--2511，“全nonterminal可启动/Q/V”|本小节allOptions所有nonterminal可用，Q为继续omega值/V=zeta平均重选值，较之前I限定扩大明，G3/G6接受。|
|RW-L2511-S04，“未stop选择U”|到nexts'未终止判定，U需混keepQ和stopV，为什么新量此刻需要明确，G6/E11接受。|
|RW-L2521-S01，“原子更新不等结束”|U恢复nextvalue让one-stepcriticupdate，不需waitK，仅fixedparams Bellman一致，G2/G6接受。|
|RW-L2521-S02，2521--2522，“y/终止0”|r+gammaU(nexts,currentomega)，envterminalU0，Optionstop则beta混highV，区别明确，G6接受。|
|RW-L2522-S03，“inner提Q_U大概率”|internalpi向highreturn a变，优化方向相对于sameomega/actionvalue可判，G1/G6接受。|
|RW-L2524-S01，“fixedhigh/stop训inner”|theta参数化inner，zeta/termination固定，偏导对象/条件明确，G6接受。|
|RW-L2524-S02，2524--2526，“dOmega归一”|d=(1-gamma)sum gamma^t prob(s_t,omega_t)，atomicclock折扣，stateomega联合occupancy新对象明，G6/E11接受。|
|RW-L2526-S03，“吸收延拓质量1”|terminal后zeroR固定dummyOption，保normalizedmass1且dummy无paramsgrad，不截质量假称概率，G1/G6接受。|
|RW-L2526-S04，“扩展普通梯度”|扩state=(s,omega)，theta只internalpi ordinaryscoregradient给式，非high/stop也变，G6/G7接受，完整证明未核。|
|RW-L2535-S01，“QOmega动作无关baseline”|same(s,omega) Q平均a，扣baseline使adv不改scoreexpectation，前普通PG机制准确复用，G6/G7接受。|
|RW-L2535-S02，“按atomic非switch折扣”|occupancy仍每stepgamma，与highgammaK一致，时间单位明确，G6接受。|
|RW-L2537-S01，“U给终止方向”|U=(1-beta)Q+betaV，dU/dbeta=V-Q，本地由可微线性mix求，G5/G6接受。|
|RW-L2537-S02，2537--2538，“nu/beta与-A”|nu参数化beta，local差V-Q=-A为继续相对重选优势，A语义由等式本地给，G6接受。|
|RW-L2538-S03，“未来到达影响”|累各t到达s_t+1,currentomega的局部终止effect乘gamma^t+1，不一帧导数假装wholeJ，G6接受。|
|RW-L2547-S01，“多gamma先走步”|call先action后stop，arrivalimpact要多1折扣，条件实际解释系数，G6接受。|
|RW-L2547-S02，2547--2548，“归一arrival系数”|arrivald=(1-gamma)sumgamma^t joint，总导数系数-gamma/(1-gamma)，norm对象非sourceoccupancy偷换，G6接受。|
|RW-L2548-S03，“A正降stop/负升”|继续比重新选好，maxJ降低beta；badcurrent提高beta，按relativevalue非absolute，G1/G6/E12接受。|
|RW-L2548-S04，“high另计”|zeta若求grad要按其choice时刻新贡献，fixedzeta偏导不包含，范围改变不能继承，G7/E10接受。|
|RW-L2548-S05，“原完整关系”|来源指完整PG/termination关系，本地只解释公式和局部推导，不宣称已读原证明。|
|RW-L2550-S01，2550--2552，“Q.6/V.9/beta.25”|人工U=.75*.6+.25*.9=.675，给samearrival比较输入，G6接受。|
|RW-L2552-S02，“y.5675”|-.04+.9*.675=.5675，criticone-step真样本设r/discount清楚，G6/E12接受。|
|RW-L2552-S03，2552--2553，“logit局部.05625”|A=-.3，dbeta/dnu=.25*.75，-productA=.05625正，乘arrivaldiscount后提高stop；sigmoid先前NN常见但前已policylogit说明，等式数解释充足，G6接受。|
|RW-L2553-S04，“相对而非低值”|continue.6低于reselect.9才stop，不以valueabsolute低判断；例补区别非重复U定义，G4/E6接受。|
|RW-L2555-S01，“other任务分解/复用”|其它hierarchy变prior与旧data处理，不取消high/low/stop功能，比较轴明确，G2接受。|
|RW-L2555-S02，“Feudal指令/局部奖”|manager下指令、low为其局部reward学，statepartition/interface强prior限制behaviorclass；机制与代价具体，G1/G3接受，未核源。|
|RW-L2557-S01，“MAXQ两value”|subtaskgraph把子任务自身价值与完成后parentremaining拆，为什么两对象清楚，G2/G5接受。|
|RW-L2557-S02，2557--2558，“Qi=Va+Ci”|parenti挑subtaska，Va childvalue+Ci remaining且durationdiscount在completion，符号/角色即时给，G6接受。|
|RW-L2558-S03，“递归最优弱全局”|固定子层eachsubtaskopt不等originalMDPglobalopt，保证相对给定分解限定，G1/G7接受，未核完整MAXQ条件。|
|RW-L2560-S01，“HIRO相对goal”|highg训练low，目标坐标明确不是Optionid，G3接受。|
|RW-L2560-S02，“window/距离/平移”|fixedwindow low读s/g目标s_t+g_t，state变需维持sameabsolutegoal而调relativeg；动作/goal机制白话明，G6接受。|
|RW-L2560-S03，“low变旧high原意”|low更新后同g产生别a串，highreplay转移模型不stationary；specificdatareuse缺口先，G5接受。|
|RW-L2560-S04，“向东两格”|same高goal因lowpolicy变而对应不同actionseq，类比对象对应唯一，G2接受。|
|RW-L2560-S05，2560--2562，“候选goal最大似然”|用currentlow对recordactions算loglikelihoodsum再relabelling，方向/目的明确；候选新目标由什么集合/提议规则、tildeg_i怎样逐步生成未明确，候选CH03-R1-07（G6/E9）。不以原HIRO常识替正文补。|
|RW-L2562-S06，“校low非补真轨迹”|重标highg但realobservedactions/states不改，不能创造未发生realtrajectory，G1/G7接受。|
|RW-L2564-S01，“HAC后验动作+测试”|achievedstate当hindsighthigha、各层goal重标以接口近似ideal lowcompletion，另外testpenalty区分realreachability，机制明，G6接受。|
|RW-L2564-S02，“忽略test高估”|若只有achievedsuccessfulrelabel不test原提议可达，会overvalue实际低层未能达目标，具体selectionbias/代价，G1/G7接受。|
|RW-L2584-S01，“prior可排好policy”|hierarchyprior降搜索同时限制candidatebehaviorclass，不能一概帮助，G1/G2接受。|
|RW-L2584-S02，“forced4,4五变九”|same房间任务全high强制upperleftgoal，route至少9而自由5，前几何可复算，G6/E9接受。|
|RW-L2584-S03，2584--2586，“two return”|5步四nonterm-.04加gamma4goal1得.51854；9步八nonterm加gamma8得.20265，方向high好，G6/E12接受。|
|RW-L2587-S01，“完美子task仍排route”|candidatefamily不含下门直达，即局部各opt不能恢复被prior排的globalroute，例支持反向限制，G1/G7接受。|
|RW-L2587-S02，“atomic保留表达不保找到”|allatomic+high任意选可expressoriginaloptimal，但sample/searchtime仍可能不找到；存在与求解效率分开，G1/G7接受。|
|RW-L2593-S01，“门含任务prior”|手工door位置用了下游知识，切到无externalreward发现技能的local缺口，G5接受。|
|RW-L2593-S02，“先行为后任务检”|无外奖先不同controllableoutcomes，再testdownstream可call，能力目标非自动tasksolvable，G1接受。|
|RW-L2593-S03，“Z/pi与Y”|Z为call前behaviorid，pi(a|s,z)，Y终点/访问/摘要可选，不同后果变量的作用先给，G3/G6接受。|
|RW-L2593-S04，“q从后果猜技能”|discriminator反推z给可辨识信号，输入y/s0输出conditionalprob，G6接受。|
|RW-L2593-S05，“同终点不可分”|skills同outcome无法从Y辨z，I小，关系两端明，G2接受。|
|RW-L2593-S06，“噪声差不可控”|只noise不同非selection稳定产生，想学可控不是random多样，G2/E2接受。|
|RW-L2593-S07，“行为改变后果”|目标skills choice→controlledY区分，明确因果控制而非obsvariation，G1/E3接受。|
|RW-L2603-S01，“MI可辨识”|I fixeds0时域说明Y含多少z辨识信息，与前discriminator对象相同，G2/G6接受。|
|RW-L2603-S02，2603--2604，“赋能capacity”|openloop原子a_seq distribution任意合法概率law maximizeI(Aseq;S_K|s0)，控制选择可辨识程度而非rawstateentropy；候选/方向/用途明，G6/E9接受。|
|RW-L2605-S01，“闭环替开环改类”|learnedclosedloopskill可反馈新s，而seq不反馈，allowedcontrolclass变化须版本明，G3/G7/E10接受。|
|RW-L2608-S01，“真实posterior难算”|I需joint技能后果、p(z|y,s0)未知不能直接compute，缺口先loss，G5/G6接受。|
|RW-L2608-S02，“label经验拟q→下界”|knownz rolloutY监督discriminator概率近真实posterior，使policy有可计算reward，数据→预测→目标链明，G6接受。|
|RW-L2608-S03，“加减logq”|将MI拆可算项和posteriorKL，目的与变形依据先给，G6接受。|
|RW-L2619-S01，“MLEq/内部reward”|q用knownzlabel最大似然，policymaximize bracketinternalr，两个参数优化目标分工完整，G6接受。|
|RW-L2619-S02，“KL非负非学好保证”|下界成立仅KL非负，tightness和技能质量还需Y/qcapacity/coverage/opt，数学保证与学习表现不同，G1/G7接受。|
|RW-L2619-S03，“uniformprior常数不覆盖”|-logp(z) constant不意味可到有用区，uniformz分配不等taskstatecoverage，G2/G7接受。|
|RW-L2621-S01，“VIC终点条件起点”|fixeds0用terminalY辨Option，接前conditionalMI准确，不新框架无桥，G4/G7接受。|
|RW-L2621-S02，“terminalreward分PG/stop含义”|整段终点判别r用PG分配internalactions，termination也决定Y，数据到update机制明，G6接受，未核源。|
|RW-L2623-S01，“DIAYN访问态与entropy”|改变Y为visitedstate、addactionentropy，各skill可随机，区别终点控制，G3接受。|
|RW-L2623-S02，2623--2624，“logq-logp内奖”|classifierq(z|s)/prior给r，maxentropyRL优化，前SAC机制已建无需复述，G6/G7接受。|
|RW-L2624-S03，“不是同条件终点”|s0是否给、哪些t state平均会改MI对象，固定/改变项明，G3/G7/E10接受。|
|RW-L2626-S01，“DADS预测与差异”|给s辨z与nexts目标I(Z;S'|S)，Y/condition都改有原因“动力后果可预测而不同”，G3/G5接受。|
|RW-L2626-S02，2626--2634，“model似然比近似”|q(s'|s,z)给selectedskill预测密度，分母Mprior技能平均近q(s'|s)，score比值大表示selectedpredictable与others不同；分布/用途即时给，G6接受。|
|RW-L2634-S03，“finiteM非精确MI”|M MonteCarlo、learnedq及datadependentzlaw误差使finite logratio不自动精确I，限制具体，G1/G7接受。|
|RW-L2634-S04，“skill模型下游plan”|q学nextstateunderz可供skillspaceplanner，输出与用途明非仅命名效果，G1/E3接受。|
|RW-L2637-S01，“CIC表示/熵奖”|transition与continuousz对比训representation，entropy inrepresentation作explorereward，区别classifier直接内奖明，G3/G6接受，未核源。|
|RW-L2638-S02，2638--2641，“匹配loss”|v_i transitionembedding/u_i skillmatching、批内j negatives，-logsoftmax偏向matchingpositive；sim未给定义或选择、tau未给含义/正值；候选CH03-R1-06（W3/G6）。精搜前置01/02及此章此前未定义sim，旧tau为trajectory/targetEMA/MPPI另情境不能替本地temperature定义。|
|RW-L2641-S03，“particleentropyreward”|actualr来自embedding近邻distanceentropy估计，contrastloss不是DIAYNclassificationr，更新representation与policyreward分开，G2/G6接受。|
|RW-L2641-S04，“两实现分别核”|比较需分别看reprtraining与reward产生，要求对象可观察不是泛泛实现好，G1/E3接受。|
|RW-L2660-S01，“多样性非可解”|四种diversitymetrics不保taskreturn，下一反例给具体原因，G5接受。|
|RW-L2660-S02，“三左终点log3不能到右”|uniform3/不同deterministicterminal可完全识别z得I=Hz=log3，allskill不穿door，高任意组合仍不出left；条件相容给全，G6/E9接受。|
|RW-L2660-S03，“确定且每call左/人工”|说明maxI所需确定且每次call左closedinvariant，regions非measuredheatmap，G1/G6接受。|
|RW-L2669-S01，“穿门仍需组合”|已onecrossskill仍startup兼容、terminaldist落下skillstart/stop可靠，各constraint具体，G1/G7接受。|
|RW-L2669-S02，“复用另预算”|MI/area仅pretrain指标，downstreamselection/finetune/newinteractioncost要计，不把多样高当reuse便宜，G2/E12接受。|
|RW-L2669-S03，“改单位非取消三条件”|tasktransfer留后章、这里temporalunitchange仍需coverage/estimation/optimization；综合边界与核心question连接，G7接受。|

## 特殊单元

|ID、位置|对象、计算目的、允许集合、方向、依据|
|---|---|
|RC-L2506-S01，“分层接口”|房间下door/Option对low持续direction，接受。|
|RC-L2506-S02，“high→low→stop返”|编号/subgoal后每步atomica，stop后reselect，高层间隔随机，接受。|
|RC-L2506-S03，“原/辅助与OptionCritic”|auxlow可选，OC用originalreturn不需人设auxr；图rewardbox并列不意味着high吃aux，正文2501/图注区分，接受。|
|RF-hierarchy-L06，“state/task”|到右G外任务输入high，接受。|
|RF-hierarchy-L07，“highzeta”|输出下doorgoal或omega，接受。|
|RF-hierarchy-L08，“lowpi”|内部每步directionpolicy，接受。|
|RF-hierarchy-L09，“envatomica”|env交互单位仍一步，接受。|
|RF-hierarchy-L10，“stopbeta”|到door后交control，不等envdone，接受。|
|RF-hierarchy-L11，“两reward”|originalr高评价，可选goalr训练low，正文/图注负责区别，接受。|
|RF-hierarchy-L12--17，“task/high/low/env/reward及更新边”|high指令给low、atomica交互r回训练，非同reward统一优化全部，正文明确，接受。|
|RF-hierarchy-L18--20，“newstate到low/stop”|low与beta每原子步可读state，观察时刻不同highcall，接受。|
|RF-hierarchy-L21，“stop回high”|终止后再highselect，接受。|
|RF-hierarchy-L22--24-S01，“high随机/low每步”|decisiontiming区分，接受。|
|RF-hierarchy-L22--24-S02，“low更新改high含义”|highgoal下state/actionkernel由low变，oldreplay需校正/测试，HIRO/HAC给后机制，接受G7。|
|RX-L2513，2512--2520|缺到达nexts未判stopvalue，U=(1-beta)currentQ+beta highV，QU=R+gamma E_PU，QOmega=E_innerpi QU，allnonterminalOptions可启动前提明；与每原子更新目的对应，接受G6。|
|RX-L2522，2521--2522|sampley=r+gammaU,currentomega、envdoneU0，internala向大QU，scope与OptioncallgammaK一致，接受G6。|
|RX-L2525，2524--2526|stateomegaoccupancy normalized(1-gamma) atomicdiscount，absorbeddummy保mass1/no gradient，接受G6。|
|RX-L2528，2527--2534|缺innerpi ascentgradient，fixedhigh/stop，ordinaryPG扩state得1/(1-gamma) E_dOmega,a scoreQU，baselineQOmega不改mean；不是未归一sum假E，接受G6。|
|RX-L2538，2537--2538|缺beta增减方向，dU/dbeta=V-Q=-A，各继续/切换值本地定义，接受G6。|
|RX-L2540，2539--2546|wholeterminationgradient=-sum_t gamma^{t+1} E[gradnu beta currentomega(nexts)*A]，先action后stop多gamma；arrivalnorm后-gamma/(1-gamma)，接受G6。|
|RX-L2552，2550--2553|Q.6/V.9/beta.25→U.675→y.5675；A-.3 beta' .1875→localgrad.05625，relativecontinueworse因此stop增，接受G6/E12。|
|RX-L2558，2557--2558|MAXQ parentvalue childVa+completionCi，childdurationdiscount在completion，givenparent/childgraph目标不是globaloptimal，无完整递归证明核验，接受本地角色解释。|
|RX-L2561，2560--2562|currentlow最大recordactions loglikelihood选tildeg relabelhigh，但允许goal候选构成/逐steptildeg_i构造未说明；候选CH03-R1-07待最终连续核定，不凭外部paper填集合，G6/E9。|
|RT-L2571，“方法/prior/数据”|同三learningfunctions下对比分解先验/复用条件，接受。|
|RT-L2573，“Feudal”|固定manager/stateabstract/interface，learnselect与execute、localr可限制globalbehavior，接受。|
|RT-L2574，“MAXQ”|graph/stop/possiblepseudor预设，subtaskvalue+completion需abstractconditions，接受。|
|RT-L2575，“OC”|Option数/param/start预设，learninner/stop/highvalue可能短/重复collapse，具体失效对象，接受G1。|
|RT-L2576，“HIRO”|coords/window/distr固定，offpolicyhighlow用currentlowrecorda likelihoodcorrectoldg，集合疑点同07不重复发现。|
|RT-L2577，“HAC”|goalspace/budget/test固定，hindsightaction/hindsightgoal/test各功能分开，接受。|
|RC-L2580-S01，“prior与边界”|不是五保证互比优劣，accept指定结构/学对象对比，接受。|
|RC-L2580-S02，“notrepeatstack”|各层state/goal/action/r明，单层算法复制不能定interface，具体缺口而非空评价，接受G1。|
|RX-L2585，2584--2587|缺hierarchyprior如何损真return，samegridfree5step J=.51854/forcedupper9step .20265，四/八nonterminalr和gamma4/8goal计数正确，接受G6/E12。|
|RD-L2597，2595--2606|固定s0时域MI、两formalidentity、controlcapacity与closedloop类改变句全纳入下列RX/RW2603/2605，接受。|
|RX-L2599，2598--2602|缺技能辨识量，E logposterior/prior=H(Y|s0)-H(Y|Z,s0)共同jointlaw，比较从skillchoice信息能去掉outcomenoise；条件固定s0/H给，接受G6。|
|RX-L2604，2603--2604|empowerment maximizeallowedactionseq distribution I(Aseq;terminalS|s0)为capacity，候选prob laws动作合法/时域固定，whymax是最多可区分控制，接受G6/E9。|
|RX-L2610，2609--2618|缺trueposterior不可算→q拟替代：addsublogq分ELq/prior+E_YKL(trueposterior||q)，KL>=0得lowerbound；knownz/Ysample训练q/policymaximize下界，接受G6。|
|RX-L2624，2623--2624|DIAYN访问s分类内rewardlogq(z|s)-logp(z)，加actionentropy与VICterminalcondition不同，条件变量改变有明确桥，接受G6/G7。|
|RX-L2628，2627--2633|DADS selectedz conditionalnextdensity比Mpriorz平均，logratio近MItrainr；M/source/qmodel误差2634声明，非精确信息保证，接受G6。|
|RX-L2639，2638--2641|transitionv/skillu批i matched分类logsoftmax，缺sim函数定义与tau温度/positive；候选CH03-R1-06，W3/G6。不能将先前trajectorytau/EMA tau/MPPI tau自动当此loss参数。|
|RT-L2648，“区分对象/信号条件”|same unsupervisedskills以Y/conditioning区别loss，接受。|
|RT-L2650，“VIC”|s0后z/terminal辨识条件下界，stop/reachability决定Y，接受。|
|RT-L2651，“DIAYN”|z/visiteds+entropy，visiteddiversity不一定taskstates，接受。|
|RT-L2652，“DADS”|givenS,z/nextS likelihoodratio，predictable/diverse两objectives与MI式相合，接受。|
|RT-L2653，“CIC”|transitionrepr与continuousz，contrasttraining+reprentropyreward，distance/negativedesign需配置；符号缺口同06，非此table可回补。|
|RC-L2656-S01，“非通用MIloss”|四方法后果/条件/representationreward差异具体，接受G2。|
|RC-L2656-S02，“变变量变不同含义”|terminal、visited、conditionalnext、representation四不同observable对象，接受G3/G7。|
|RX-L2660，2660|uniformdeterministicthreeleftterminalperfectrecoverz givesI=log3，但所有callleftclosed无法到right，候选技能不能组合crossdomain，反例条件明，接受G6/E9。|
|RC-L2665-S01，“多样非跨房task”|图测试downstreamgoalreachability不测losslearningcurve，接受。|
|RC-L2665-S02，“threefill/leftonly”|three人工不同终点区域含文字z1/2/3，alllow不得过墙，接受。|
|RC-L2665-S03，“无door/兼容启动”|识别技能不自动生成crossdoor或nextstartupcompatible，任务missingbehavior明确，G1/E3接受。|
|RF-regions-L02--04，“三人工区域”|leftx1..2 y1/3/5三个不同区，无实测mass刻度声明，接受。|
|RF-regions-L05--08，“grid/two doors”|same8x5/y2/4wall洞，右goal可达原任务但技能不使用洞，接受。|
|RF-regions-L09--11，“z1/z2/z3”|区域标签可明确辨技能，非仅颜色，接受。|
|RF-regions-L12--13，“S3,2/G7,2”|该反例起点变3,2图内明确，2660声明独立skillregiontask而不继承2,2手算，不影响closedleft结论，接受G3。|
|RF-regions-L14--17，“三路径留左”|routesendpoint2,1/2,3/2,5都x<4.5，dashed第三示意非原子完整走格，人工regionroute不暗示每弯曲坐标为真实state，接受。|
|RF-regions-L18--19-S01，“完全区分”|三terminal区disjoint确定→recoverz，不必要trajectorydisjoint，接受G6。|
|RF-regions-L18--19-S02，“无人穿门”|allskill invariantleft，eachcall仅left使组合也不穿，正文2660给闭合条件，接受G1。|

## 链与候选

- RM-2510--2553：原子步保持omega/stop混U→QU/critic目标→扩state dOmega归一PG训inner→dU/dbeta=-A→arrivaldiscount累terminationgrad→.6/.9/.25人工例解释relative而非absolute。
- RS-2555--2587：三函数同但先验/数据reuse不同→Feudal/MAXQ固定graph限制candidate→HIROcurrentlow likelihoodrelabel/HACachievement/test→forcedupper5→9、return降→expressoriginalatomic≠能及时学到。
- RM-2593--2669：无外奖技能选择能改变Y→MI/empowerment固定起点域→posterior未知由q监督lowerbound→VIC/DIAYN/DADS/CIC分别改变Y/condition与reward路径→I最大仍不crossdoor反例→复用另需startup/terminal/stop相容及downstreamcost。
- 新候选06为CIC sim/tau即时定义缺口；07为HIRO允许候选与逐step相对goal对应缺口。保留待最终核定，不能按所有业内常用缩写自动接受。其他未新增必改项。
