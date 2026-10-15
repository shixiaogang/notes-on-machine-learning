# CH03-R1 接管者W遍：L1708--1838

人工W1--W6接续，G/E证据随条目，正文输入同冻结值。Dyna/MPC源图全部亲读，预算手算复核而未运行生成程序/模型实验。后MuZero从L1840另块完整审查。

|ID、位置短引|白话意思；专项依据或发现|
|---|---|
|RW-L1712-S01，“不上游也传奖”|已见近终转移后旧上游可借model传播信息不用当前再访；本地具体延迟问题先给，G5接受。|
|RW-L1712-S02，“真实/model同Q接口”|Dyna真实sample先更新，model再采后果重复Bellman样本更新；输入/用途/改变的计算机制及时，G4接受。|
|RW-L1712-S03，“来源无论”|给sa/r/s'/c，两源都同r+gamma c maxQ-Q递推，样本来源影响统计正确而非算术外形；G6接受。|
|RW-L1718-S01，“真实或model”|同更新的输入可能真sample或learnedmodel预测，明确证据类型；G1/G2接受。|
|RW-L1718-S02，“图线型/随机版本”|图虚真实区分，算法empiricaljoint可存stochastic，给scope非全部Dyna实现，G2接受。|
|RW-L1718-S03，“末次后果vs分布”|det环境只存lastoutcome可，randomgrid需empiricaldist或可多后果模型；条件变化需model表示改，G3/G7/E10接受，历史原始归因未核。|
|RW-L1744-S01，1744--1745，“先前记录Q0”|基准3,2右→4,2 r-.04 c1，此前Q0记录用于当前model后备份；旧记录具体且合法，G5/G6接受。|
|RW-L1746-S01，“4,2上到终Q1”|当前上成功入4,3真终奖1，alpha1 Q当前=1；实际事件非成功概率1，G1接受。|
|RW-L1747-S01，1747--1748首句，“upstream目标.86”|model重放已记录过渡到当前有Qmax1的4,2，上游target-.04+.9=.86；只一后果sample而非核期望，G6接受。|
|RW-L1748-S02，“Q .43不返”|上游当前Q0/alpha_plan.5修到.43，无需真实返3,2；scalar/table前提完整，G1/G6接受。|
|RW-L1750-S01，“非精Bellman”|一条model记录更新不能当stochasticgrid真备份；证据强度及时限定，G1接受。|
|RW-L1751-S01，1751--1752首句，“真核目标.68”|其他后继maxQ0，则真.8到有Q1处的平均target-.04+.9*.8=.68，和model.86区别；sample统计与核期望比较固定Q，G2/G6/E12接受。|
|RW-L1752-S02，“没记滑移不消”|重复simulate不能增加未记真实kernel后果证据，支撑.86/.68差；G1/G4接受。|
|RW-L1755-S01，“回放同.43”|该已记录transitionreplay也能同算，model额外能力非这重复算术；与1750独立更新例目的对应不抢算法保证，G2接受。|
|RW-L1755-S02，“概率组合/泛化/新态”|model可组合后果、预测可泛化未记录sa、递归新态；条件“可泛化”不保所有OOD准确，风险表1766明，G1/G2接受。|
|RW-L1755-S03，“表区分复用泛化”|数据reuse与modelpredict能力不同轴，不把全部生成经验都视新真sample，G2接受。|
|RW-L1755-S04，“优先扫描前驱”|按value变化沿modelpredecessors调计划次数，可快奖传播但不能修未得真实转移；方法操作/作用与limit一同，G4/G7接受。|
|RW-L1773-S01，“一步多次/连续合目标”|Dyna独立模拟多一步update，另一可把连续modelrollout合一次returntarget；新机制相对已知Dyna不同时间合成，G5接受。|
|RW-L1773-S02，“MVE短model后critic”|model-basedvalueexpansion用短预测奖再critic剩未来，名字伴白话；数据flow/用途及时，G4接受。|
|RW-L1773-S03，“real起点/策略modelL步”|起点realbuffer s，futurea待评pi/modelrollL，c_j继续标累积w从1乘c屏终后贡献；候选/长度/终止权符号先给，G3/G6接受。|
|RW-L1780-S01，“三来源”|r/s'/c是model、s0真实、末Vtargetcritic，证据类型和部件角色明确；G2接受。|
|RW-L1780-S02，“联合期望非边缘乘”|r/c/next相关时jointrolloutexpectation不能随意productmarginalmeans；原1669/1671相关性此处新累积权用途，G6/G7/E10接受。|
|RW-L1780-S03，“Q首a固定”|动作值目标条件(sa)，首步固定待更a、之后pi抽a；V→Q条件变化操作明确，G3/G7接受。|
|RW-L1780-S04，“criticstop目标”|critic将MVEtarget停导拟值，不在这步穿modelgrad改policy；本接口modelvaluevsmodelpolicy区别，G2/G6接受。|
|RW-L1782-S01，“model真末误差gammaL”|若modelcorrect且无终，末criticuniformepsilonV被gamma^L缩，当前段奖无modelerror；条件/被控误差量明，G1/G6接受。|
|RW-L1782-S02，“L大加预测要求”|L长少critic尾误差但更多r/s要model正确；取舍不是单向better，G2接受。|
|RW-L1782-S03，“L2 .685/误终损.405”|人工r .1/.2，Vtail.5/gamma.9，无终G .685；第二transition误终去tail.9²*.5=.405，奖仍保第二步；全部输入/作用明，G6接受。|
|RW-L1782-S04，“多模拟非独立真证据”|rolllong不自动好/百万生成trajectory非百万独立env观测；引用统计信息来源为前缺覆盖实际，G1/G4接受。|
|RW-L1788-S01，“当前plan不写Q”|model可在当前s比较候选计划，无需先train长期Q；本地具体执行问题先给，G5接受。|
|RW-L1788-S02，“前章闭环恢复”|优化plan只firsta、新obs再plan，准确恢复前MPC动作步骤而非只section号，G7接受。|
|RW-L1788-S03，“learned核/开环限制”|新model来自数据，computebudget候选每轮限openloopseq，和前feedbacktree不同；原/新对象/理由明，G3/G7/E10接受。|
|RW-L1788-S04，“不同后继需不同a”|固定sequence不能根据randomnext变futurea，即使modeltrue也表达受限；具体反例类型/失去feedback能力明，G1/G2接受。|
|RW-L1788-S05，“树保证不移用”|前feedbacksearch前瞻界不能直接拿openloopcandidate的learnedkernel来用；改条件/不可继承部分明，G1/G7接受。|
|RW-L1788-S06，“只真first反馈”|图realcorrection只执行firsta得到obs，不验证所有candidate预测path；访问协议明确，G2/E3接受。|
|RW-L1797-S01，“boundedseq候选”|continuousu每维有界，allowset是长度L合法actionsequence；候选集从actionconstraint构造，G3/G6接受。|
|RW-L1797-S02，“M粒子平均选高”|model每sequence抽Mtrajectory，以平均predr+tailV估expectedreturn，选择score高；metric/direction/average原因都先给，G6/E9接受。|
|RW-L1797-S03，“评分为”|式1798把particleaverage标hatF而非trueJ，计算对象动机已给，G6接受。|
|RW-L1805-S01，“same起点/终止处理”|eachparticle同currentstate或inferredstate law，model传播，真/预测终止后stopr去tail；起点随机和terminalmask语义明确，G6接受。|
|RW-L1805-S02，“PETS概率ensemble”|model噪是randomnext，members差是fitdisagreement，两个不确定对象不能混置信；1656形成多个fit前置、本地两端恢复，G2/E5接受。|
|RW-L1805-S03，“TS1与TS∞”|eachstep换member vswholeparticle固定member，后保持同解释跨时相关，因此jointlaw不同；抽样方法具体/时间单位明，G2/G4接受。|
|RW-L1807-S01，“三优化器表”|同模型score不同搜索方法/预算，一层接口非PETS模型组名，G2接受。|
|RW-L1807-S02，“CEM现在序列”|旧CEM搜跨s policytheta，当前搜一次openloopa序列；新范围/对象本地明不因同名混概率，G3/G7/E10接受。|
|RW-L1807-S03，“教学配置L5N200M20E20I5”|explicitplanningbudgetcandidate/particle/elite/iterationcount，notassertPETSdefault；数据单位各定义，G1/G6接受。|
|RW-L1807-S04，“warmstart/方差”|各维Gaussianmean上轮bestseq左移lastzero，stdhalfactionrange，firstmeanszero；init和timecontinuation规则明，G6接受。|
|RW-L1825-S01，“采clip/tie编号”|每轮从currentGaussian抽seq逐坐标clip合法interval、score、topE，tie按id；候选、合法/排序方向、平局全指定，G6接受。|
|RW-L1825-S02，“elite均方差更新”|E成员coordinate均m_E/v_E用于平滑nextproposal，不宣称原Gaussian截断MLE精解；G6接受。|
|RW-L1832-S01，“std floor1%”|v_min来源是每coordstd最小range*.01的平方，范围单位stdvsvariance明确；G6接受。|
|RW-L1832-S02，“裁剪非截断MLE”|clip生成有boundarymass不是truncatedconditionalGaussian精确MLE，明确实现选择不冒数学同解；G1/G4接受。|
|RW-L1832-S03，“5轮best已评分first”|fixedIstop，allscoredcandidates里bestexecuteonlyfirst，不用未evalmean默认best；输出/停止/评口径完整，G6接受。|
|RW-L1832-S04，“INML100000”|I5*N200*M20*L5=100000particletransitioncalls，tailINM=20000另加；每truea规划预算清晰非envsamplecount，G1/G6接受。|
|RW-L1832-S05，“并行不改querycount”|batchparallel可改walltime不改totalcalls计数；资源评价对象/单位明确，G2接受。|
|RW-L1832-S06，“非统一默认”|配置仅教材budget算例非PETS所有运行同数；证据类型限定，G1接受。|
|RW-L1834-S01，“MPPI指数扰动”|weights∝exp((score_i-maxscore)/tau)加权noise更新nominalseq；metric回报高weights大，减max共同factor只numeric，G4/G6接受。|
|RW-L1834-S02，“改采样需补权”|proposal/refdistribution或controlnoise结构变需IS correction，指数形式不单独保pathintegralopt；allowedassumption与loss不能继承范围明，G1/G7/E10接受。|
|RW-L1836-S01，“PlaNet latentscore”|candidatea入latentdynamics以predr评sequence、CEM选，无需decode所有pixel；trainoutput与execute接口具体，G2接受。|
|RW-L1836-S02，“PETS坐标”|PETS常用给statecoords的dynamics，比较inputrep不同不是更高model质量；G2接受。|
|RW-L1836-S03，“同闭环不同成本”|两个可replan但pred对象/infer/callcost不同；比较两端都有表/机制，不泛性能，G2/E1接受。|
|RW-L1838-S01，“墙边边界”|局部网格滑移具体准备限制replan，非抽象“闭环不安全”先抛；G5接受。|
|RW-L1838-S02，“4,2上概率”|.8到终4,3，.1left到3,2，.1right撞墙stay；基准核与合法intent/slide一致，G1/G6接受。|
|RW-L1838-S03，“错.98/短长代价”|wrongsuccess.98高估终，太短无tail低估绕路，long仍用wrongkernel；各误差不同条件/机制明确，G2接受。|
|RW-L1838-S04，“obs只事后”|nextobs知道这次slide但执行前不能补遗漏risk，反馈不能重写已采取动作；因果/时间限定明，G1接受。|
|RW-L1838-S05，“不可逆改墙”|若wall改不可逆lossregion，replan不能undo落入，需安全条件另章；原可stay网格→新irreversibletask理由与不能继承安全clear，G3/G7/E10接受。|

## 特殊单元

|ID、位置|白话与依据|
|---|---|
|RX-L1713，1713--1717|缺model奖传播统一更新，sample可real/model，max只合法b沿本章约定，ccontinue屏tail，target-current差乘alpha；来源不保证model正确1718/1750明，接受。|
|RA-L1730，“探索真执行”|Q探索在currentstate取合法a真实sample r/s'/c，c真终label1661，接受。|
|RA-L1731，“trueQupdate”|真实访问sa用统一式先更value，不把先model生成伪r当真实，接受。|
|RA-L1732，“jointcounts模型”|update后继/r/c联合计数形成stochasticmodel，可保相关而非lastdetoutcome，接受。|
|RA-L1733，“n_plan循环”|planningnumber是model调用预算不trueinteraction，接受。|
|RA-L1734，“已见sa规划分布”|按指定proposal从knownsa挑查询起点，不自动OODtablemodel有预测，接受。|
|RA-L1735，“modeljointsample”|给选sa当前model抽r/s'/c，保经验jointoutput，接受。|
|RA-L1736，“sameQupdate”|simulate也targetdifference更对应Q，role只源不同，接受。|
|RA-L1738，“reset/截断c1”|真终或envlimitreset，timecut标continue1且留reset前s'；terminaltask语义不随收集边界变，接受。|
|RX-L1748，1748，target .86/update.43|model采已seen3,2→4,2，currentnextQmax1/gamma.9/r-.04给.86；currentupstream0/alpha.5给.43，real不再访，接受。|
|RX-L1752，1752，true target.68|其他两nextQmax0，true.8prob to4,2给.68而非.86；对samefrozenQ核期望vs样本target区别，接受。|
|RT-L1762，“source/能力/risk”|并列datareuse、empiricalsampling、paramgeneralization的访问能力与误差，不将sim count当truecount，接受。|
|RT-L1764，“replay”|只有完整旧transition重用，支持/oldpolicy/相关需检查；不是不允许共享networkpredictunseenstate，限定数据接口，接受。|
|RT-L1765，“empiricaltable”|knownsa经验law求mean或sample，finitecountuncertainty不因sim多消；1752具体例支持，接受。|
|RT-L1766，“parammodel”|newsa prediction/recursive roll引OOD、termin、虚可达state错误；更queryflexible需更correctness，接受。|
|RC-L1769-S01，“real与generated”|区别source及availablequery，不是统计独立皆同，接受。|
|RC-L1769-S02，“flexquery更强要求”|OOD/generalization query需model正确范围，1766风险承载对象明确，G1/E3接受。|
|RX-L1774，1774--1779|缺multistepmodelvalue目标，real起点fixed、pi/model连续L，w0=1累乘c遮终后奖/末V，sumgamma^j w_j rpred+gamma^L w_L Vtarget；symbols1773、三源/相关/stopgrad1780解释，接受G6。|
|RX-L1782，1782，tail/例|modeltrue/noendtailerrorgamma^L epsilonV，L2r .1/.2/V.5 target.685，错第二terminal去.405而保r2；tradeoffmodel vscritic明确，接受。|
|RX-L1798，1798--1804|缺当前合法sequence评分，allowu∈bounds lengthL，Mmodelparticle平均rewarddiscount+tailV估expectedreturn；samecurrentstate/inferlaw及terminalstop1805明，候选/metric/high方向先1797，接受G6。|
|RT-L1814，“optimizer/候选/预算”|同score1799不同search接口，不把modelpackage和optimizer同class，接受。|
|RT-L1816，“shooting”|fixedproposal抽Nsequence选highestscore无grad/eliteadapt；候选domain1797合法sequence，接受。|
|RT-L1817，“CEM”|repetsampletopeliteMLEsequenceproposal，budget/elite/floor/constraints需报；从paramCEM转actionsequence1807明，接受。|
|RT-L1818，“MPPI”|nominalseq+noise用expscore/negcostweightedperturbation，standardderive需dynamics-noise匹配，generalsamplerIS/controlcost需说明；概览边界不冒完整保证，接受。|
|RC-L1821-S01，“同目标异接口”|三optimizer同model expectedscore，不说同优化精度，接受。|
|RC-L1821-S02，“组合非互斥optimizer”|PETS/PlaNet是model+planner，CEM是planneroptimizer，不同层角色；G2接受。|
|RX-L1826，1826--1831|缺CEMupdate防早collapse，m/v halfold halfelite且v逐coordmaxfloor，合法区clipsample/floorstd1%范围明确；max用于variance≥floor不选worstmodel，接受G6。|
|RX-L1832，1832，budget|INML=100000transitioncalls，INM=20000tailcalls，每真实a额外modelcompute；规定Istop/topscored而非fittedmeanexecute，全部输入1807/1825，接受。|
|RX-L1834，1834，weights|exp((F_i-maxF)/tau)normalize权给highF更大noisecontrib，subtractsame max不改ratio只防exp溢出；proposalchange需IS而非exponential自带optimalcontrol，接受G6。|
|RC-L1723-S01，“Dyna flow”|图数据来源区分而非losscurve，接受。|
|RC-L1723-S02，“真实线/模拟虚线同Q”|两个来源进sameupdate，分线型避免冒sim=real，接受。|
|RC-L1723-S03，“planning非realquantity”|modelcalls为计算预算、非新真实step，接受G1。|
|RC-L1793-S01，“learned滚动plan”|modelcandidateprediction与real纠正区别，接受。|
|RC-L1793-S02，“realobs起点/model较低频fit”|每轮obsreinfercurrentstate、model更新可schedule较慢，未说每动作必须refit，接受。|
|RC-L1793-S03，“onlyfirst真实/其余不记录”|optimizedseq只first执行，futureprediction不writeasrealdata，真实证据scope明确，接受。|
|RF-dyna-L06，“realenv一步”|realstep获取新record而非多modelcall，接受。|
|RF-dyna-L07，“real五元c”|recordsa/r/s'/continueflag，与1712/1730一致，接受。|
|RF-dyna-L08，“统一Q target”|r+gamma c maxQ作为target示意，fullcurrenterrorupdate1715给；合法动作沿规范，接受。|
|RF-dyna-L09，“empiricalmodelcounts”|jointcountsincludescontinue1732，图简题后继奖励不表示丢终止，record/virtualc节点显式，接受。|
|RF-dyna-L10，“simtilde五元”|modelgeneratechoice/后果与realrecord相区分，接受。|
|RF-dyna-L11--13，“real→data→Q/model”|trueexperience直接updateQ并fitmodel，不从Q幻觉写real，接受。|
|RF-dyna-L14，“sample n_plan”|model→virtualsample虚线规划次数，接受。|
|RF-dyna-L15，“virtual→Q”|同update但statisticalsource不同，接受。|
|RF-dyna-L16--17，“更新Q后探索下一真a”|Qpolicy确定下一环境动作/数据，体现采样feedback，接受。|
|RF-dyna-L19-S01，“reuse同部分update”|旧recordreplay也可same.43，model区别非这算式，接受。|
|RF-dyna-L19-S02，“new后果/modelerror”|extraquery能来自model且需modelcorrect不是新增realdata，接受。|
|RF-mpc-L05，“realobs新起点”|eachreplanstartreset至实际观测，而非重置真实任务初始s，标题“重置规划起点”明确，接受。|
|RF-mpc-L06，“infer/scheduledfit”|currentstateinference及model按日程更新职责分开，接受。|
|RF-mpc-L07，“sequence采评分更”|候选sampling/score/proposalupdate在model内进行，接受。|
|RF-mpc-L08，“firsta真实转移”|onlyfirst执行，部署动作源plannercomparison，接受。|
|RF-mpc-L09--11，“obs→infer→opt→act”|从实测新起点到planexecuteflow，不把全部candidate验证，接受。|
|RF-mpc-L14-S01，“Nsequence/Mparticles”|modelquery候选数/随机trajectory数，单位分明1807，接受。|
|RF-mpc-L14-S02，“L步/末V”|Lrolloutscore optionaltailV，长域missingtail风险1838，接受。|
|RF-mpc-L14-S03，“I轮CEM”|maxiterbudget并非I新trueinteraction，接受。|
|RF-mpc-L15--16，“opt/particle双边”|proposalcandidate→modelrollscore→optimizer按score改proposal，不是environmentloop，接受。|
|RF-mpc-L17--18，“真feedback纠正”|execute→newobs只有实firststep产生predictioncorrection证据，接受。|
|RF-mpc-L20-S01，“futurepred非realrecord”|其余计划结果未真实发生不写bufferreal，接受。|
|RF-mpc-L20-S02，“不可逆已执行”|newobs/replan不能撤回已action，1838改lossregion条件说明，接受G7。|

## 关键链与边界

- RI/RM-Dyna：近终value变而upstream难重访→真样本与modelplanning同Q target→jointempiricalcountmodel→knownsa抽起点/model联合后果→n_plan计算额外更新→.43传播例→truekernel目标.68与sample.86区分→replay也同.43、parammodel才泛化new后果。缺model预测不因规划多得到真实证据。
- RI/RM-MVE：多次一步update→连续L预测合一次目标→real起点/待评pi/modelr,s,c/targetcriticV→累积继续权避免终后贡献→joint expectation相关性→criticstop目标→正确model条件下gamma^L尾误差，长L需更多modelcorrectness。此处是value估计非穿modelgrad优化policy。
- RI/RM-MPC：当前state直接比plan→恢复前章onlyfirst/newobs闭环→learnedkernel+openloopseq计算限制→bounded合法L序列/M随机particle平均score→CEM N/E/I/warmstart/floor/clip/tie/stop最高已评候选→querycount与trueactions分开→真实replan只事后纠正。不开新标题或移动材料。
- RS-1788：feedbacktree→openloopsequence，不可按不同randomnext选不同futurea，前章feedback保证不继承。RS-1807：CEM policyparams→每动作序列，保持筛elite机制但candidateprob对象变。RS-1838：可staywall→irreversiblelossregion，闭环不是安全证明。
- 全适用min/max/期望/阈值：合法b最大Q、继续mask、联合rollout期望、合法seq高score、topE、variancefloor、指数score权都有候选来源与运算目的；未以平均/最坏统计词代模型保证。无本块新必改发现。
