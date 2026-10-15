# CH03-R1 接管者W遍：L3187--3304

接管者W遍最后一块，人工W1--W6及全部特殊单元。方差分解、选择偏差与截断数例本地独立核对，所有外部基准/统计论文未核原文；未运行实验或查看PDF。主报告形成前仍要核全覆盖/门槛与候选，不能仅本块完成判正文通过。

|ID、位置短引|白话；具体依据|
|---|---|
|RW-L3187-S01，“两层量化”|前fixedproduct测试与retrain区别可用variance拆解，不泛泛“统计稳”，G5/G6接受。|
|RW-L3187-S02，“tau/sigma/独立”|tau²是真产物J跨trainvar、sigma²是conditionaltrajectoryvar平均，train独立/conditionaltestIID，计算meanG总体var条件先给，G6/E11接受。|
|RW-L3193-S01，“Ntest只减第二”|Var mean=ta²/M+sig²/(MNtest)，moretest不能消trainvar，指标/方向明，G2/E12接受。|
|RW-L3193-S02，“相邻点相关/点CI非整带”|same训练检查点相关，即各point95%不allcurve同时95%，量词/覆盖对象区别具体，G1/G7接受。|
|RW-L3195-S01，“curve/final/all分数”|预定最后点和allrunfinal与curve共同保以防onlyluckyselection，评价对象具体，G1/E3接受。|
|RW-L3195-S02，“normalize/mean/median/IQM”|cross-task需scale，mean outliers敏感、median可藏tails，IQM排序中50%平均，另robustmetric非唯一排名；比较对象/聚合定义即时给，G2/E1接受。|
|RW-L3195-S03，3195--3196，“performanceprofile”|P(normalizedscore>tau)按thresholdcurve显示哪些score域胜，不同tau此处明确threshold而非trainvar，G3/G6接受。|
|RW-L3198-S01，“重采匹配目标”|CI抽样scheme需coverageobject与hierarchy一致，后具体两情况提供可检验动作，G1/E3接受。|
|RW-L3198-S02，“固定task vs新总体”|tasksetfixedwithin-taskresampletrainruns；newtaskpopulation需taskdistribution及outerresample，固定/扩大对象理由与condition明，G3/G7/E10接受。|
|RW-L3198-S03，“sameproduct组保相关”|multitaskfrozenproduct scores联合cluster重抽，不当independenttaskscore，samplingunit明，G1/G6接受。|
|RW-L3198-S04，“少seed区间不稳/raw”|lowindependentM可能高CI估计var，公开rawscore避免narrowband虚精确，不统一固定M保证充分，G1/E3接受。|
|RW-L3198-S05，“原研究范围”|Agarwal工作讨论fewruns/CI/IQM/profile，来源关系具体但未外核。|
|RW-L3202-S01，“两checkpoint均.6误差±.1”|teachingtwofixedtrueJ.6 eachmeasurement独立等prob±.1，非实际曲线各point通常相关假装独立，G3/G6接受。|
|RW-L3202-S02，“预定最后mean.6”|fixedone errorzero mean unbiased .6，baseline固定rule明确，G6接受。|
|RW-L3202-S03，“测试后挑max期望”|onlybothlow prob.25→.5，其余.75→.7，expectedreported .65，selectionnoise偏差可复算，G6/E9/E12接受。|
|RW-L3206-S01，“selectedtrue仍.6”|selection不能改变two真实policyJ，本身measurementhigher非truegain，G1接受。|
|RW-L3206-S02，“.05无策略改”|.65-.6 bias来自maxnoise，不将negativefinding删，比较基准与direction明，G6/E12接受。|
|RW-L3209-S01，“bestpoint可协议非同test无偏”|modelselect合法但samevalidation选再report有winnerbias，具体twooutput对象区别明，G1/G7接受。|
|RW-L3209-S02，“候选/预算/独立test”|fixedsearchcount/validationbudget/rule，afterselection unusedtest再eval；若反复看test调param则test变validation须另final，权限/信息flow清楚，G1/E3接受。|
|RW-L3209-S03，“Rainbow快照协议不同”|前Rainbowbestpolicy原protocol不可与fixedlast偷偷同口径，回指恢复当前重要区别，G7/E1接受，原protocol未外核。|
|RW-L3211-S01，“ablation同预算”|组件删后释放compute会changequestion，需要配置budget定义，G5接受。|
|RW-L3211-S02，“keepupdates vsreallocate”|固定其它updates探组件作用；fixedresourcesreallocate探系统，改变哪个因素/比较goal明，G3/G7接受。|
|RW-L3211-S03，“failure纳入/infra重跑”|algorithmfailure按prespecified分布纳入，infra故障重跑次数另记，不onlydeletebadseeds，G1/E3接受。|
|RW-L3217-S01，“同名非同协议”|sameenvironmentname仍可不同info/action/goal，下ALE具体因素建立入口，G5接受。|
|RW-L3217-S02，“pixels/state/repeat/sticky/life”|ALE visibleinput与wrapper改变transition/episodeboundary各对象明，G2/G3接受。|
|RW-L3217-S03，“sticky再前a”|概率reuseprevexecuteda使fixedrequeststring不必sameactualtrajectory，术语机制即时给，G4接受。|
|RW-L3217-S04，“version/ROM/wrapper/prob”|需实际字段辨sameprotocol而非同gamename，要求可验证，G1/E3接受，外源未核。|
|RW-L3219-S01，“Procgen16/heldoutlevels”|16generatedgames、restrictedtrainseeds与unseenlevelseval核心protocol，样本对象/划分明，原事实未核。|
|RW-L3219-S02，“重合测另泛化”|overlaptrain/test不是heldoutnewlevelgeneralization，difficulty/num/range/version需留，范围变化和metrics不同明，G3/G7/E10接受。|
|RW-L3219-S03，“infinite/finitelevels不混”|原sampleefficiency/generalization不同trainprotocol，不能onefinalscore跨levels预算compare，G2/E1接受，未核source。|
|RW-L3222-S01，“control多参数”|state/pixel info、controlperiod/physicsdelta、repeat、rewardscale/done各改变access/dynamics/goal，具体要求明，G1/E3接受。|
|RW-L3222-S02，“body类似非task同”|DMC/Gym同body可不同reward/frequency/terminal，不用名称当equalprotocol，G2/E1接受。|
|RW-L3222-S03，“按version定义”|实际task/包版本记录须matchcompareobject，不声称流行默认唯一，G1接受，原definitions未核。|
|RW-L3240-S01，“timecap改目标”|同timeoutflag可对应recordstop或taskend，需要明确bootstrap语义，G5接受。|
|RW-L3240-S02，“真终止/采样截断”|恢复前章zeroaftertaskterminal vsrecord仅停，回指不给读者猜，G7接受。|
|RW-L3240-S03，“-.04/.8/.9→.68 vs-.04”|nonterminalcap需要r+.9V=.68，错mask零漏.72；inputs/条件/两个target同trans明确，G6/E12接受。|
|RW-L3240-S04，“若task时限zero/时间state”|taskdefinedend则zero才对，remainingtime影响决策通常须state；改变goalcondition不原timeout结论无条件，G1/G7/E10接受。|
|RW-L3242-S01，“两flag含义/mask”|保存terminated/truncated而mask按taskgoal，不机械按anydone遮值，G1/E3接受。|
|RW-L3242-S02，“auto-reset最终obs”|vectorenvresetnextobs不是当前transitionnexts，需截断前finalobs避免targetcross-episode，索引/数据来源明，G6接受。|
|RW-L3242-S03，“专原分析”|source覆盖timecaps对state/bootstrap影响，未核原文但关联明。|
|RW-L3244-S01，“跨game原分单位不同”|rawscore不能rank统一performance，需要pergame参照scale，G5/G6接受。|
|RW-L3244-S02，“固定参照和测量”|human/random同protocol才能normalize，补可比缺口而非任意一比例，G1/E3接受。|
|RW-L3244-S03，“人类归一式”|S_agent/random/human构成scaledgap，用处先于newS_HN，G6/E11接受。|
|RW-L3250-S01，“每game参照记录”|ratio两baseline值及评测protocol要给，明确metric允许对象与comparisonbase，G1/E1接受。|
|RW-L3250-S02，“small/zero/反常denom”|分母小放大score差，zero/反顺须exclude/alternate而不直接平均，条件和失效类型具体，G1/G6接受。|
|RW-L3250-S03，3250--3252，“30/10/50→.5”|teaching(30-10)/(50-10)=.5非raw30的50%，不同百分比含义及时解，G6/E12接受。|
|RW-L3252-S04，“random到human差一半”|scale.5仅基准gap的位置，不successprob或原分百分比，G2接受。|
|RW-L3252-S05，“clip影响aggregate”|cliprange changevalues/outliers hencecross-tasksummary，需配置而非默认clip无影响，G1/G7接受。|
|RW-L3273-S01，“记录改变结论非形式”|reprofields影响data/update/metric而不是形式合规，后examples给对象，G1/E3接受。|
|RW-L3273-S02，“async/replay/model频率”|async延迟增behavior-targetdiff、replaylifetime改visitD、modelfrequency改syntheticmisfit；eachconfig→specificconsequence明确，G2/E2接受。|
|RW-L3273-S03，“system工程留后但影响先记”|具体storage/collector实现后续systemvolume，不借后补algo当前数据与目标变化，G7接受。|
|RW-L3279-S01，“一条记录两任务”|回章首onea→oneR/nexts，用其估长期+decidewheregetdata，核心twoquestion实际回收，C4/G7接受。|
|RW-L3279-S02，“四信息接口”|directvalue/directpolicy或model预测辅助update，而非systemnetname分类，G2接受。|
|RW-L3279-S03，“主要对象/动作flow”|table聚inputupdates和deployactions混系统按flow，不求exclusiveobject，criteria可观察，G1/E2接受。|
|RW-L3298-S01，“同反馈”|所有fourinterfaces由policy→data→estimate→newpi循环，G7接受。|
|RW-L3298-S02，“keycoverage/err/visit纠错”|keya不足使R/P/Q估错，greedy/update改a、newD决定哪error可纠，不声称samplecount自动性能好，G1/G2接受。|
|RW-L3298-S03，“MC/TD/IS取舍”|fullreturn/estimatedbootstrap/ratio-supportolddata是不同evidencerequirements与variancebias，机制前已展开非只names，G7接受。|
|RW-L3298-S04，“loss校对/trace不补信息”|double-samplingexample提醒objectivefit，traces/adv传播creditlength不创造r，具体新综合限制，G1/G7接受。|
|RW-L3300-S01，“error要转decisionD”|可靠policy需所用decisiondistribution下误差，不trainloss自身small，承载目标J明确前句long后果，G1/E3接受。|
|RW-L3300-S02，“三界与范围”|uniformQ→greedygap不fromavgMSE；performanceidentitynewoccupancy需controloldproxyD；modeluniformerr需chosenpolicy域而optimizers选高估，三个具体条件前正文证，G7/E1/E10接受。|
|RW-L3300-S03，“gammaK/highcall非env/risk同比”|Option原atomictarget保留、少highchoice不代表env5变2也不免lowlearning或risk，原例与条件支持，G1/G7/E12接受。|
|RW-L3302-S01，“finite分析protocol/structure”|从局部可算到finiteN需family/access，problem层依赖回收，C4/G7接受。|
|RW-L3302-S02，“三theorem不同族”|UCBVIcount/LSVIknownlinearR/P/OLIVEerrorfactor各结构，不拼generalNNguarantee，G1/G7接受。|
|RW-L3302-S03，“budget和独立train”|experiment分别real/update/model/selection/deploy，independenttrainvar不用fixedtest替，原量化formula支持，G1/E3接受。|
|RW-L3304-S01，“可算不足finite近优”|unknownmodel可经验评价改policy，onestep computable不fixedNnearopt，核心答案有边界，C4/G1接受。|
|RW-L3304-S02，“形式/访问/函数/预算四职责”|algohowuse/accesswhichdata/Fsharedinfo/budgetlimitidentify&solve，互补条件实际明确，不目录复述，C4/G2接受。|
|RW-L3304-S03，“后章改变条件须重核”|信息/反馈/task/players/behaviorrequirement变，reuse组件需重核source/target/conditions，不无条件套本章，G7/E10接受。|

## 特殊单元

|ID、位置|接受依据|
|---|---|
|RX-L3189，3188--3192|缺algorithmmeanvar如何随M/Ntest变，totalvariance Var(mean_m)=Var(J_m)+Econditionalvar/Ntest=tau²+sigma²/Ntest，M独立mean除M；条件3187明，接受G6。|
|RX-L3196，3195--3196|缺performance在哪normalizedscore域优，P(score>thresholdtau)高好；distribution含哪些tasks/seeds需前normalize/samplingprotocol，作为optionalprofile而非结果已报告，接受G6。|
|RX-L3204，3203--3205|twoindependent±.1 noise max onlyalllow.25/otherwise.75 givesreported.65 vsfixed.6，selectedtrueJ remains.6，why independenttest needed concrete，接受G6/E9/E12。|
|RX-L3240，3240|samplecapnonterminalr-.04/gamma.9/nextv.8 target.68，wrongdone-.04 leaks.72；ifactualtaskend usezero needsremainingtimestate，正/反条件明，接受G6。|
|RX-L3246，3245--3249|缺rawcross-gamecomparison需human-randomgapscale：(agent-random)/(human-random)，允许参照sameprotocol/positiveusabledenom，越界/反常另rule，highergood whenpositive；示例.5表distancefromrandom不是rawpercent，接受G6/E12。|
|RT-L3229，“benchmark/info/random/version”|task同名仍不同data/action/R/done，具体表四columns，接受。|
|RT-L3231，“ALE”|pixels/internal/frame/actionrepeat、sticky/starts/train-testseed、gameend/life/timecap、versionROMhash，实际概率配置不统一默认，接受。|
|RT-L3232，“Procgen”|pixel/actionmap/inputwrapper、levelsnum/seed/unseen/difficulty、end/cap/version/configgeneratorseed，单位/划分清楚，接受。|
|RT-L3233，“control”|input/actionrange/frequency、noise/initial/taskperturbation、failure/cap/sim/model/taskversion，samebody非sameexperiment，接受。|
|RC-L3236-S01，“info/dynamics/目标”|字段都明确改变其中对象，不只形式metadata，接受。|
|RC-L3236-S02，“actualconfig非默认唯一”|prob/repeat从实际run读，不无据宣称onlystandard，G1接受。|
|RT-L3259，“复现/最少内容”|allfields实际机制影响与metadata，接受。|
|RT-L3261，“code/config”|commit/depslock/envwrapper/version/expandedparam，不给templatefinal值冒实际配置，接受。|
|RT-L3262，“data/random”|real/modelsource规模/train/evalseed/rho/train-test split，接受。|
|RT-L3263，“update”|behaviorversion/target/pifrequency/donemask/replayratio/lifetime，影响targets与D，接受。|
|RT-L3264，“selection”|candidate/tuningbudget/validation/stopping/checkpointrule/finalunusedtest，防selectionbias，接受。|
|RT-L3265，“failure”|definition/rawscore/infra重跑规则与真实count，负面保留，接受。|
|RT-L3266，“resource/artifacts”|hardware/precision/parallel/wall/deploy/checkpoint/log/plotscript，实际计算和追溯记录，不把param数当全部cost，接受。|
|RC-L3269-S01，“最小复现”|table不是实验已复现证据，只要求字段，接受G1。|
|RC-L3269-S02，“system可后/接口当前说明”|改变dataD/target的system接口本算法实验不可推给后卷，声明scope分清，G7接受。|
|RT-L3286，“interface/update/actionsource”|fourcombination同两轴，混system不互斥，接受。|
|RT-L3288，“model-freevalue”|MC/TDreturn/Q/repr真samples改value，a贪心/探索各protocol，SARSA/Q/DQN已本章讲，接受。|
|RT-L3289，“model-freepolicy”|theta常critic配合，policydeployPPO/SAC，offpolicy/coverage另check，不critic存在转类，接受。|
|RT-L3290，“modelvalue/plan”|R/P/value/priortrain用currentplanning动作，DynaQupdate/MPC/MuZero/TD-MPC计划结果，旧分类脚注本地chapterintro已解释，接受。|
|RT-L3291，“modelpolicy”|modelgrad/synthetic训练actorcritic，deployupdatedpolicy，latentstateinference可能仍model，PILCO/Dreamer/MBPOdataflow分别成立，接受。|
|RC-L3294-S01，“共享三条件”|explore/repr/timeabstraction不是additionalexclusivealgotype，接受G2。|
|RC-L3294-S02，“混系统按flow不onlyoneobject”|system可多个learnedparts，用actualdata/decisioninterface判断，不由netname硬标，G1/E2接受。|

## 综合证据

- RI/RX-3187--3211：fixedproduct测试与retrain不同variance→totalvariance tau²/M+sigma²/(MNtest)→同curvepoints相关，pointCI非simultaneousband→prespecifiedfinal/allrun/profile与合理resampling→bestcheckpointmaxnoise.65反例→validationselection与finalunusedtest分开→ablationbudget/failure规则防偏。
- RI/RS-3217--3252：同名基准不同info/action/transition/goal→具体ALE/Procgen/controlversionfields→recordcap vsactualterminal两target.68/-.04→terminated/truncated/auto-resetobs索引→rawscore不可cross-game直接平均→fixedhuman/randomscale与denom边界。
- C4/RW-3279--3304：一记录估计与采证→四接口同数据反馈→decisiondistribution下误差才可保策略→timeK与highcall/envunit分开→finitefamily/access/structure相配→实验独立train/预算→可算与finite近优区别回答章首。
- W遍本接管者现已连续复读到L3304；31张实际引用图均有对应图内记录。本块不作为全章覆盖自我验收，下一执行枚举/版本/编号核对与候选定案。
