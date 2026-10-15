# 第3章R2门槛、入口与依赖记录

CH03-R2-G，2026-10-12，修订1；独立R2；hash `927887345166301fb9aaa47eb6a53ec8389f7abfe6353bc87e5b27b5049f353e`。在C全文、P001-P528和W全文1658句后执行专项复核；以下覆盖当前正文L1-3304，特殊单元另在SF、M1-M3、ST1-ST3、SG。本文没有修改，唯一成立发现CH03-R2-01。接受项限当前位置之前的正文，后章只作后续入口不补本章推理。

## 七门槛

| 项 | 全文触发位置与实际检查、具体依据 |
|---|---|
| G1 可检验命题 | L88固定随机臂/范围与UCB次数界、L350表格TD访问步长、L377固定参数等价、L458支持/可积IS、L957全pairq误差、L1233同起点两π性能差、L1447有限熵变分、L1993全pair模型误差、L2464固定Option压缩、L2803/2908/2988原算法保证、L3053任算法辨识、L3137-3274实验协议全部还原对象/条件/量。不是“样本高效/稳定”裸标签；L2737把示例协议写明并声明不是运行事实。L907精确分位能力受F901反例否定，CH03-R2-01。 |
| G2 压缩拆解 | L9四接口以查询/动作来源判定；L49认知与偶然用重走能否消随机区分；L634三误差按真实值/平均备份/投影；L852组件改target/表示/sampling/noise；L909distributionvsconfidence与risk；L1699一步误差/multistep/calibration有对象；L1895/2046三预测及四质量层；L2698五保证、L3011四复杂度、L3117预算与L3170抽样。每个“更好/更稳”核对到回报/导数/计数/运行Var；L907平滑误差与精确分位混同登记发现。 |
| G3 新对象转换 | L82去MDP转移→bandit；L141userfeature→context且a不改nextcontext；L181固定均值→对手奖前定；L204过程→deploymentonearm；L247回MDPreach；L632表→sharedparam；L879mean→Z分布另奖；L911statequotient；L1417replayν非dpi；L1652explicitcoord→conditionaldistribution；L1788feedbacktree→openloopseq；L2073rewardmax→costmin r=−c；L2159historyposterior/latentprior；L2384新8x5room；L2434原子→randomK；L2689discount→finiteH；L2737→average/diameter；L2850valuefeature→linearP/R/mixture；L2965实现→完备；L3049visible→hidden；L3160test→trainingpop；L3243rawgame→referenceunit均有改变条件及继承边界。 |
| G4 解释时序 | 下节入口表逐项保存缺口/命名/初释。概念比较和重复例另列；L112prior/后验样本、L229时间一致区间、L375前后迹、L695双采、L900分位Huber、L1210Fisher、L1420Jν、L2159RSSM/版本、L2593技能/MI、L2950实现/完备均在当前首次使用前或紧接给必要对象，未借后章。L900-907有限Huber错误不是后释可修，发现待修改。 |
| G5 局部入口 | 全9section、41subsection、4paragraph按下面54个入口逐个核。入口从真实对象/反例/当前数学缺口进入，章首4x3网格回接时明确，另设例重新给规则。表中的方法例预告不要求先掌握其全部名称，但正式使用均查本地解释。 |
| G6 公式双门槛 | 147展示式与所有关键行内式M1-M3，159表行公式ST已记录。UCBmax/椭球max/合法KL替代inf、PPO内min与外max、MPCcandidate/particleE、MuZeroPUCT、OptionlegalΩmax、赋能允许controlclassmax、PACtrainingP、BFmin/variance、LSVIΛdirection、sup值/模型误差/TV/Option紧因子全部核候选域和指标方向。L954关键岔路例解释平均不足，L1277rarepolicyshift需全stateTV，L2483全合法Optionsup，L1993全pairモデル误差支持selection。F901代数正确但精确分位话语错误登记。 |
| G7 回指范围 | L5规划章Bellman所需真条件E就地复述；L179前线性结构、L508IS/retrace/trace、L1333AC前baseline/GAE、L1582熵/KL、L1773MVE先前value、L1788前章feedbackplanning、L2073chain、L2270Dyna/MVE/SAC来源差、L2306mu→π误差、L2336fixedπ→selectedπ、L2431原子K1/记忆扩state、L2584restrictedhierarchy→atomic保留、L2619技能后果差、L2716historicmix→PAC、L2910线性MDP测度、L2999总奖归一、L3047/3049反馈族、L3210最好checkpoint原协议、L3240终止就地数例都恢复必要结论。后POMDP/offline/reward/transfer/multi/safe不充本章前提。 |

## E1-E12校准

全部存在同根触发对象，不用“未发现”冒充执行；未出现示例原句不等于不适用。

| 项 | 触发位置、检查动作与结论 |
|---|---|
| E1 比较表现接近 | L867Rainbow消融/预算，L1699model平均误差vs门边误差，L1979.008testerror/loss.5，L2334model.16/true−.16，L3139样本fixedvswallfixed，L3195跨taskstats，L3245归一；逐项核任务/data/指标/baseline，非“表现接近”无量。外部实证来源未核。 |
| E2 类型与后果关系 | L49两uncertainty对应采样收益，L911quotient保reward/下一决策机会，L1699door两侧碰撞，L1895重建/值相关/充分表示、L2593后果Y选择；关系两端和改变决策的后果在具体例说明，非标签分类本身。 |
| E3 要求承载对象 | L350step/visitTDconvergence、L1136score baseline variance、L1277全statepolicyTV、L1993R/Prowbounds、L2466OptionK条件、L2737protocol、L2913μ测试范数；要求约束采样/模型核/π/更新/输出谁均可指出，不泛称落概率含义。 |
| E4 多重否定 | L49增加样本可能缩小无知但不消随机、L542截断currentρ改target、L909control切换不继承compression、L1419ν起点也需futureoccupancy、L2483永不终需另定义、L2965实现不保complete、L3095枚举贵不证明所有compute难、L3240截断非任务终止。逐句展开正向命题与反例，否定范围清；不把专业补出的条件算正文解释。 |
| E5 候选模型/分歧来由 | L128合法另一奖励分布信息下界、L161估计椭球未排除params、L255modelconfidence/回合sampledyn、L1654Bayes/ensemble生成途径、L1701shareddata/misrepresentation导致共同错、L2322ensemble筛不是TV；有限数据如何留多候选与不同层uncertainty在正文有桥。 |
| E6 重复例的新增职责 | 同4x3grid的MC/TD L308、control L578、DQN L838、AC L1348、Dyna L1742分别同record/目标/共享输出/两个params/模型传播；房间L2384、K折L2485、forceddoorL2584、skillL2660依次时间单位/持续时间/表达能力/多样但不可达，明确新增而非迟到定义。详细比较见下面复用表。 |
| E7 抽象回指 | L5Bellman条件E、L1773MVE旧多步、L1788前planning闭环、L2306policycoverage、L2336统一simulationbound、L2716mix输出、L2910definitionlinearMDP、L3240terminal/trunc、L3298-3304结论，均核当前所需命题实在本地恢复；没有让读者猜“前章三个问题”。 |
| E8 节首抽象判断 | 本表下全部入口核本地state/数学目标/反例先行；L1208坐标sigmoid、L1652非法mean、L1975rarepath、L2334单步model利用、L2950任候选backup、L3038组合锁、L3159train/test区别都先有可复算对象。 |
| E9 最不利集合/方向 | L129奖励族KLinf(难辨正改)、L163参数confidence集合maxreward、L954所有legalpairq sup、L1267maxallstateTV、L1996allpairP/Rerr、L2483sup合法s/ωEγK、L2759diametermaxallpairs minπhitcost、L2841worstproblemfamily遗憾；每个集合来源/指标高低/为何max或inf具体。 |
| E10 局部到一般变化 | L911sameimage→controlquotient、L1417replayfixedweights→νstart后currentoccupancy、L2145functionvalueerror→derivativeerror、L2306行为data→targetpolicy、L2336fixedpolicy→modelselectedregion、L2965oneQ*→allnextf、L3049visiblechain→hiddenfeedback、L3197fixedtasks→newtaskpop、L2364videoopenloop→closedloopcontrol，转向理由与不可继承条件均明。 |
| E11 突然一般对象/风险式 | L144linearregression先userrewardsharedsamples、L634误差目标先sharedstate、L685MSBE梯度先two-objectloss例、L1025J先动作梯度目的、L1418Jν先replay不occupancy、L1662NLL先非法mean、L1798MPC先boundedsequence、L2285eP/eR先k步取舍、L2682PAC先输出质量、L3163均值先两抽样单位、L3245HN先gameunits不同，式没有脱离当前缺口。 |
| E12 绝对量/变化幅度 | L1979safe.6/chance.1及loss.5、L2334old0/new−.16 vsmodel+.16、L2584五步.51854/九步.20265、L3203true.6/chosenreport.65偏.05、L3240target.68/−.04漏.72、L3245raw30 vsrefs10/50/.5，检查方向和参照；完整数例不是仅“下降幅度要看”的抽象提醒。 |

## 全部局部入口

ID以标题源行定位，冒号后分别为本地对象/缺口、引入对象和首次解释/边界；不要求改冻结标题。

| ID | 本地立足点、方法及顺序判断 |
|---|---|
| EN40/46 | L43避开岔路无经验→策略/数据反馈；L49未走岔路vs已知滑移→两uncertainty白话及样本收益，在名词前给场景。 |
| EN79 | L82去转移只chosenreward→噪声锁贪心，L103εuniform试/105UCB分数/113TS抽posterior，均直接回应纠错。 |
| EN138 | L141同推荐不同user→featurebeforea/linearsharedreward，L181非固定reward→history前对手EXP3，条件切换明。 |
| EN201 | L204online服务vs只部署→simple regret/errors，L227randomstop需alltimeconfidence→L237elimination/LUCB，命名后的作用即时给。 |
| EN244 | L247门只有到达才试→MDP乐观备份/完整dyn回合sample；L257内奖/278noisyTV/288GoExplore更多reset能力，非纯bandit照搬。 |
| EN290/296 | L293已记录需longterm估计→先fixedπ评价；L299完整trajectory→MC、L324等待困难→TD/bootstrap；不是直接定义Bellmanerror。 |
| EN355 | L358完整vs一步→n真reward+尾，L366λ混、L375立即误差credit→trace/前后向，L421fixedθ到online变化限定。 |
| EN453 | L456旧trajectory评价mu非pi→actionratio+support，L508longweights波动→Retrace，各weight位置/有效fixedpoint已就地述。 |
| EN548 | L551fixed走法评价→据Q控制/cover；L584maxnoise→Double选评拆；L600持续每步产出→averagegain/Poisson，目标变更明。 |
| EN629 | L632图像/continuous难表→sharedφθ，L634误差量区分；L652随机后继→sample²≠mean²、L685梯度/695双采、L731Baird/768GTD。 |
| EN794 | L797共享target+相关experience+大δ→DQN三mechanisms；L799record与sgy目的先给，L845各component分target/表示/sampling/explore。 |
| EN877 | L879sameE/differentoutcomes→Z，L898C51/QR/IQN不同表示；L900分位loss目的有桥但L907精确含义错误CH03-R2-01；L911state合并转表示充分。 |
| EN952 | L954q要决定return/rarebranch平均遮→supQ*与greedy损失，定理/数例支持worstcase目的。 |
| EN1015/1021 | L1018连续枚举/动作突切→直接π；L1024π变化改trajectory概率→J_H/scoregradient，不环境导。 |
| EN1108 | L1111高G状态随机抽a大更新→actionbeforebaseline；L1136scoreweightedVar选b、L1144未来未得奖→bootstrap/GAE，减基线与换未来区分。 |
| EN1205 | L1208samecoordinate不同Bernoulli概率→KL/Fisher/naturalstep；L1231localdistance无returnguarantee→newoccupancy性能差，L1285TRPOcompute→PPOproxy。 |
| EN1330 | L1333π改变需重新critic→两个过程耦合，L1335onpolicyrecord→两params各目标，L1369sync/async新增sampleversion职责。 |
| EN1392 | L1395continuousQa导→DPG，L1410DDPGreplay/cost，L1417ν非dpi，L1423三error→TD3，L1436外noise→entropy目标/SACsamplingdensity。 |
| EN1580 | L1583已知entropy/KLfixedstate→regularizedprobupdate；L1602不可微policy→parameterCEM，L1622ES平滑方向，空间转换明。 |
| EN1643/1649 | L1646replay无newcounterfactual→learnmodel供backup/currentplan；L1652gridmean非法→predictdistribution/不同heads，L1654形式、L1660NLLfit/use、L1671joint依赖。 |
| EN1709 | L1712新终点R但上游无returnvisit→Dyna真实/model同Q，L1755replay同.43→额外modelqueries；L1773多一步转continuousMVE。 |
| EN1785 | L1788currentmodelcompareplans→只first执行/newobs重plan；限制openloopseq先于F1798，L1807三个solve接口/明确预算。 |
| EN1841 | L1844left/right搜索需R/V不backgroundpixels→MuZero表示/g/f/prior/leaf，再search/真实targets/边界；没有“视觉越逼真越好”。 |
| EN1912 | L1915tree finitebranch不适continuous→shortlatentseq+末Q+prior，L1923五module/score/trueloss，valueguide可组合optimizer。 |
| EN1972 | L1975modelaccurate是否搜越多越好→rarepath教学反例→L1991需uniformerror界，先selectionfailed例再bound对象。 |
| EN2064/2070 | L2067本轮sequenceplanning→训练跨state共享π免部署search；L2073state feedback链→modelJacobian和costgradient，固定模型vsfit区别。 |
| EN2149 | L2152trueinteraction贵→latentmodel供actorcritic训练；L2154trueposteriorroot/prior无newobs，L2159RSSM最小计算在此给不借ch04充分性。 |
| EN2265 | L2268longmodelerror→真实root短branch/独Dmodel训练SAC；L2270与Dyna/MVE具体接口差，L2283fixedπk-score量取舍。 |
| EN2331 | L2334一步a∈[-1,1]olddata0/newπ.4真下降→selectedregionerror；L2364actionvideo扩大obs但控制还需干预/true测试。 |
| EN2374/2380 | L2377“到门口”多step→时间间隔正交四组合；L2384完整8x5room/五原子两高calls，收益/low训练cost先于Option。 |
| EN2416 | L2419到门随机K→end/R/K三后果和Option三职责，L2421正式、L2433原子G分组/高层合法E与max。 |
| EN2498 | L2501fixed内部/β后需获得→handgoal/OptionCritic外R；L2511扩stateω每step续/切、L2524/2537梯度先有评价对象。 |
| EN2590 | L2593没taskR→distinctcontrolledoutcomes/skillZ/posteriorq，L2595MI/empower、L2608不可算posterior→bound、各方法改变Y/conditions明。 |
| EN2672/2678 | L2675finite真实budget不同asymptotic→访问/问题/F；L2681部署hatπloss→PACtrainingP，L2689H过程→regret与输出接口。 |
| EN2742 | L2745finiteSA counts→optimisticbackup传播；L2759continuous无reset→Ddiameter/UCRL，L2779定时齐在线/knownR再BF保证。 |
| EN2820 | 需真正上界才explore→全round/time/pair置信reverse归纳，限制固定trueV集中不足，非只写“乐观性”。 |
| EN2825 | 乐观value覆盖真实regret→沿trajectorybackup得到零condmean鞅差，访问项累加为后计数求和留对象。 |
| EN2828 | 同pairradius按本地n缩→三计数/Cauchy界，真正新data决定半宽非gradient次数。 |
| EN2837 | 若每step范围H粗界多付H→BFtrajectoryconditionVar及Freedman，数据依赖V第三bonus必要。 |
| EN2843 | L2846每图像state新无法count→可检验linearMDPR/Pclosure，L2848knownφ/mixture区别、L2867backup、L2877LSVI regressiondirection。 |
| EN2944 | L2947最终correctcandidate不能表示某中间target→实现/complete，L2965toy、L2967manyerrors→rank因子/OLIVEelimination，不以容量替样本结构。 |
| EN3035 | L3038lower需fixedfeedback→visible/hiddenchain区别，L3051仍fullstate微差reward→two-instance检验下界；样本/compute另表。 |
| EN3106/3112 | L3109测G高可能budget→先可复核比较；L3115同trueexperience重复train/model生成→单位分开，两budget固定回答不同问题。 |
| EN3156 | L3159samepolicytests vsretraining区别→两层means/Var/CI，L3200bestcheckpointnoise→validation/finaltest分离。 |
| EN3214 | L3217sameenvname可能info/P/R不同→ALE/Procgen/continuous具体conditions；L3240terminal数例、L3243rawunits→refsnormalize。 |
| EN3276 | L3279回一次动作只有reward/落点→四接口与数据-估计-访问反馈答案，终L3304访问/F/budget限定非新理论。 |

## 方法依赖链

每行按任务/缺口→预测评价→残差或指标→总体/经验目标→求解和条件核；概览方法不强加无需要的监督loss。

| 链ID、方法位置 | 实际链及不适用环节 |
|---|---|
| ML1 ε/UCB/TS/EXP3/LUCB L103-241 | 未知chosenreward纠错→均值/后验/权/interval→gap与uncertainty→在线regret或deploymentloss不同→sample/update/最大评分或淘汰。ε无拟合loss，UCB/TS不冒称同posteriorguarantee，EXP3fixedmean不适用，LUCBtimeuniformstop。 |
| ML2 optimism/PSRL/intrinsic/GoExplore L247-288 | 需达到farreward→value/modelconfidentroute或novelty→counts/预测error→optimisticplanning/训练r+βb→回合一致sample/计数/返回savedpath。新内奖不等originalJ、simulatorreset增协议能力；概览无mandatoryparamloss。 |
| ML3 MC/TD/n-step/trace/IS/Retrace L299-546 | fixedπ真实价值→G或r+γV/多步→target−value→meanreturn/Bellmanfixedpoint，ISsupport校E→empiricalavg/sampleupdate/trace、π比与c未来传播。不能samplesquare直接MSBE、截currentρ改变Vtrace目标。 |
| ML4 SARSA/Qlearning/Double/average L551-627 | 改走法→Qπ/targetmax或平均gain→y−Q/δ差分→controlfixedpoint/长期g→合法a/ratio条件/本地steps/infinitevisit，Double选评不同估计。平均目标无折compression，Rlearninggain条件不同。 |
| ML5 linear/halfTD/LSTD/LSPI/FQI/GTD L632-790 | sharedparams更新互相牵连→value/realT/ΠT三量→meanδ或projectresidual→MSBE/MSPBE与sample²差→双采或固定点/矩阵/重复freeze回归/双scale。Baird能表达true0仍unstable；onlyfixedlinear/evaluable/coverconditions，不任NN保。 |
| ML6 DQN/Double/Dueling/PER/Noisy/Rainbow L797-874 | target同参/相关样本/大δ→onlineQ与delayQ→sgy−Q→replayHuber empirical→批gradient/periodcopy/真实buffer，components分别不同接口，budget消融条件和priorities校正明。 |
| ML7 Distribution/representation L879-950 | mean丢后果/合并state丢动作机会→Z或控制充分表示→projection/distribution/auxiliaryerror→C51/QR/IQN与contrast/predict/value目标→parameterfit、固定pi压缩/控制切换边界。有限Huberproxy不精确quantile，CH03-R2-01；辅助loss不全controlcertificate。 |
| ML8 score/baseline/GAE/natural/TRPO/PPO L1024-1327 | continuous枚举/策略切换→J及A→gradient/advantage/πdistance→truepolicygradient或旧data代理→scoreMC、baseline、Fisher局部球、真实performance差、ratio/Clip minibatch。bootstrapbias/oldstate不校/currentbatch再用必须区别。 |
| ML9 AC/DPG/DDPG/TD3/SAC/ACER/MPO/APPO L1333-1577 | critic随π变/continuousQa导/滞后data→V/Q/softQ→TD或softtarget、density→各loss/代理→两个params/梯度路径、重param/tanhJac/温度/SG目标、sync和oldπ条件。不能softtable定理证明NNbuffer收敛。 |
| ML10 KL动作/CEM/ES/CMA L1583-1640 | local改π而不离ref/不可微program→fixedq或parameterreturn→KLcost/selectionnoise→simplexregularizedmax、Gaussian平滑J→指数归一/eliteMLE/perturbedreturndirection；blackbox无supervisedresidual必要，参数search成本真实trajectory。 |
| ML11 learnedmodel/WorldModels/PlaNet/PETS L1652-1701/1788-1839 | record不能newa/非法mean→conditionalP/R/c或latent→NLL/datafit/决策error→真seqprediction→φfit后sample/plan，joint依赖和history充分性有边界；TS1/∞不同joint、pixel重建非controlguarantee。 |
| ML12 Dyna/MVE/MPC/MZ/TD-MPC L1712-1970 | reward上游未返/每currenta选→Qbackup或modeltrajectoryscore/searchR/prior/leaf→targetresidual或counterfactualscore→model+value/policytargets→simulateQ/continuouslambda/particleCEM/PUCT/latentshortplan。来源/执行器和querybudget逐项明，不把同simdata=同learninggoal。 |
| ML13 modelgradient/PILCO/Dreamer/MBPO L2073-2328 | directcostderiv不可得/trueexperience贵/longrollwrong→path/moment/model想象G/短transfer→costJac或value/advantage→fixedφpolicyC、V3代理/softSAC经验→chain/近似moment/REINFORCE/混合D，真model监督与policymodel内学习分开。 |
| ML14 SMDP/OptionCritic/Feudal/MAXQ/HIRO/HAC L2384-2588 | highdecisiondepth→end/R/K/QU/U→highreturn/continue-vs-switchA/oldgoalmeaning→原子discountJ或auxgoalR→legalΩbackup/内部及βgrad/任务图/当前lowlikelihoodrelabel/test。辅助reward与globaltarget/recursiveopt区别明。 |
| ML15 VIC/DIAYN/DADS/CIC L2593-2670 | 无任务奖励先学可控distinct行为→skill/outcome posterior或dyn/embedding→MI/KL/contrast与entropy→各指定conditions下internalR→判别器MLE+RL、finiteM近似/negatives；MIlog3taskfail反例保下游条件。 |
| ML16 UCBVI/LSVI/OLIVE L2675-3033 | finiteN目标不是asymptotic→PAC/regret/actualfamily→confidenceresidual/directionaluncertainty/eliminationerror→uniformconcentration/PAC而非经验lossalone→反向optimism/BF、knownφregression、finiteF候选检验；sample vscompute以及奖励归一化保条件。 |
| ML17 evaluation L3109-3274 | performance升可能预算/selectionnoise→J/algorithmmean/taskscore→train/testVar与reference幅度→协议测量目标→independenttests/seeds、validation与finaltest、复现artifacts。无需要虚构训练loss；source/程序/PDF未实际执行。 |

## 范围转换、定义与重复解释

| ID、位置 | 原对象到新对象、可继承部分与须改变的条件 |
|---|---|
| RC1 L82/141/181/204/247 | MDP去转移→bandit、添feature→context、固定均值→对手、online→bestarm、恢复transition→reach。chosenfeedback共同，meanIID/时序/比较类/stopcriterion/reachcost逐次不同，探索表非互斥。 |
| RC2 L632/652/705/731/797 | 表格→sharedlinear→loss对象→halfgradient→offpolicyBaird→network。samplebackup外形可继承，projection/动作和stateweights/目标停导/矩条件/收敛不能继承；Baird非仅randomvariance。 |
| RC3 L879/909/911/919 | mean→distribution→risk/parameterconfidence不同；statequotient→特定价值测试class。保完整Z不等riskaverse、smalltestsetvalueequivalence不保全干预/搜索；奖励同/类概率同才closure。 |
| RC4 L1231/1258/1277/1296/1417 | 真newoccupancyperformance→oldstate代理→sampleKL/Clip→replayν代理。动作ratio可继承同state校正、不能校stateweights；maxstateTV理由rarechange，平均KL不是同保证，νstart依后续currentoccupancy。 |
| RC5 L1652/1673/1788/1991/2032/2145 | explicitmean→random/latentmodel、feedbacktree→openloopplan、fixedπerror→选择π、valueerror→gradienterror。reward/backup形式可复用，状态合法/联合预测/representation/horizon/classuniform/derivativequality条件新增。 |
| RC6 L2159-2245/2268/2306/2336/2364 | obs后验root→无obsprior想象；Dreamer版本目标不相同，V3score非路径；MBPOsynthetic→mixedSAC、behaviorerror→targeterror、oldπ→selectedregion、openloopvideo→trueclosedloop。所需监督/可用interaction/action接口/coverage改变，不后章补充分性。 |
| RC7 L2384/2431/2433/2511/2584/2660 | baseline4x3→独8x5room、原子K1→randomK、fixedΩ→learninginternal/β、restrictedhierarchy→保atomicexpressiveness、diverse技能→task调用。保originalγ^atomic时间，activeΩ/domain/fixedkernel/auxR/startcompatibility/训练成本条件新增。 |
| RC8 L2689/2737/2759/2779/2848/2999/3049 | discount→finiteH→averagegain，各奖励bounds/stop和protocol不同；tabular→knownφlinearR/P→finiteFrank；perstepR1→wholeepisodeR1；visiblechain→hiddenonlyterminal。结构/访问/归一化/degreeinfo不同，不能拼各界作NNguarantee。 |
| RC9 L3160/3197/3209/3217/3243 | 单轨迹→fixed产物→trainingpop→多task/新task，bestcheckpoint→独test、同envname→versionprotocol、rawscore→refsnormalize。期望可计算但独立层/coverageobject/selection/baseline量和units全需重定。 |
| DC1 L71/84/205/2681/2691 | 累积/简单遗憾、覆盖、最终loss、PAC、识别、lastiter分别时间/输出/随机层，正式块与表ST绑定，不用一个“表现”概括。 |
| DC2 L634/658/685/770 | valueerror真实V监督、MSBEmeanBellman、MSPBElinearprojection、sampleTD²=mean²+Var，conditions/目标/solve区分；double-sampling同条件two独立非buffer任二条。 |
| DC3 L1113/1136/1145/1187/1210/1278 | action前baseline保E不需准确、bestvariance基线score加权、bootstrapfuturebias、Fisherlocalgeometry/compatiblefeaturegradient分别条件，非减V均不偏。 |
| DC4 L1654/1671/1699/1895/2046 | deterministicnext/randomP、posterior参数/ensemble拟合分歧、R/cjoint、一步/multistep/calibration、reconstruction/反事实/充分控制不同量；同错误可多个成员共同犯。 |
| DC5 L2421/2512/2595/2848/2949/2970 | SMDP后果三量/Option实现三元、QU/QΩ/U/V切换位置、MI/赋能允许controlclass、linearMDP/mixture未知对象、实现一个Q* vscomplete任backup、rank因子依环境/F/roll-in分别明确。 |
| EXR1 L98/112/111/237 | bandit各小例新增greedy纠错/Beta posterior/乐观score/区间淘汰的任务，不拿同三臂重新定义噪声，数值角色提前给。 |
| EXR2 L308/578/838/1348/1742 | grid不同使用新增MCfirsteveryvsTD、三控制target、DQNoutputgradient、actorcritic两个params、modelreward上游传播；共享state/R条件但冻结初值/record明确新，非迟到铺垫。 |
| EXR3 L674/767/1003/1979/2334 | loss最优点不等、averageupdate发散、rarebranchMSE错、modelplan错、policygradient利用错不同error环节；每例新机制可指出，非同“训练好部署坏”换词。 |
| EXR4 L2384/2485/2584/2660 | 房间五step两calls→同终不同K→层级排除五step路线→技能distinct却不穿门，原子单位/折扣/expressiveness/可组合性分别新增。 |
| EXR5 L1163/2206/2790/2906/3203/3240/3250 | 同一δ或modelpred手算各为GAE贡献/想象continue/统计confidence/方向coverage/selectionnoise/terminationmask/归一尺度；无实验结果冒充，外部数据句仍核源受限。 |

## 记录结论

适用G1-G7与E1-E12均执行。局部入口、方法链、范围变化、定义比较、重复例和核心公式记录完整；CH03-R2-01在G1/G2/G4/G6仍待修改，不能写成全部门槛通过。后章内容未用于解除该问题。本文核源、完整外部证明、执行程序和最终版面未核。
