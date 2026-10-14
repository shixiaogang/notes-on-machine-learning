# 第3章R2特殊单元：公式2

CH03-R2-M2，2026-10-12，修订1；独立R2；hash `927887345166301fb9aaa47eb6a53ec8389f7abfe6353bc87e5b27b5049f353e`。与M1同规则，连续上下文及每组内全部式亲自复核，F首行ID不按编译号。用途/符号/集合/方向/理由保留在每条，不由枚举生成语义。

| ID、位置短引 | 计算缺口、符号与集合、运算方向及理由、判断 |
|---|---|
| F-L1116「score b零」 | 本状态高G未说明动作优，动作前h可测b、乘积可积，score乘b E0，允许G−b保gradient均值；不保证Var一定降。 |
| F-L1124「条件b∇1」 | 固h可把b出期望，所有legal动作pi归一导0，塔性质再时间加；不能同批action拟合baseline后假其固定。 |
| F-L1137「b*加权比」 | 零均保许多基线需选最小Var，固定s二阶矩、score norm² mean>0，在b∈R min二阶矩得导零；分母0任有限b同效，Vpi仅特殊等条件。 |
| F-L1145「n优势delta」 | 完整G不及时需bootstrap，固定片段L及critic、sum真n delta telescopes=G[n]−Vnow。目标估本a相对state水平；截断末V只进末δ。 |
| F-L1151「GAE两式」 | 混长度λ∈[0,1]含末剩余质量，汇各delta权=(γλ)^l。所有L项已读，逆递推linearcompute，非λ任意都近似critic无偏。 |
| F-L1163「三delta/.3872」 | γ.9 λ.8指定，.2−.072+.2592=.3872，人工例非curve；作用比较衰减贡献。 |
| F-L1178「e偏差」 | exactcritic条件已给，换approx e bounded/infinite discount，差=-e_now+γ(1−λ)future weightedE e；statebaselinescore均0，动作相关tail会bias，λ1完整回报去tail，截断另留尾。 |
| F-L1211「KL二阶/F」 | 同坐标步不同动作概率，要固定旧dpi比较分布；Δ参数位移、F=oldstate/oldaction score外积，可微支撑一阶导归一0。局部quadratic非finite回报保证。 |
| F-L1222「约束上升步」 | 候选有效子空间KL近似球 Δ'FΔ/2≤δ，g非零/Fpositive，max g'Δ，拉格朗日或柯西给归一F^-1g。零g取零/奇异限制或伪逆/阻尼本地述。 |
| F-L1236「性能差」 | 分布步长不保证回报，需要新π实际访问旧A均，有限折扣两stationary/sameρ0/rewardbound，外1/(1−γ)为归一占用。动作/state必须new，旧data仅later代理。 |
| F-L1248「A望远镜」 | same新trajectory对oldV残差，γt sum奖−initialoldV+tail；boundedtail0/initialE oldV=oldJ给真差，不借模型预测。 |
| F-L1259「旧dpi动作比代理」 | 更新前没newtrajectory，替stateweight成old、动作ratio支持π'≪π，L=oldJ+oldE ratio A/(1−γ)。ratio只修same-state a不能state distribution，名称代理明确。 |
| F-L1272「TV平方下界」 | η=max_s TV及epsilonA maxpairabsA，从occupancyL1≤2γη/(1−γ)和newE A≤2epsAη相乘，减4γepsAη²/(1−γ)²。全部s是为罕见可达区不被平均漏，理由先给。 |
| F-L1288「PPO Clip内min」 | 约束TRPO算贵，oldπ fixedA/ratio/currentparam外max，经验批权须匹配discount代理；内min是两contribution较小保守取值而非对a最坏。正A上端/负A下端flat，反向罚，非hardratio约束。 |
| F-L1336「AC三式」 | actor改变数据critic需跟踪；真实同πrecord/z终，δcritic/actor共享但不同params方向，critic半梯度β、actorγt α scoreδ且停导。占用抽样可另常系数，不混timeweight。 |
| F-L1396「DPG链」 | continuous不可逐a，Q对a导×f对θ导，stateE当前dpi并归一；可微/可积，value小error不保导，环境无需可微。 |
| F-L1418「Jnu」 | replaystateν不是dpi，重新以ν为起点J仍需当前π后续occupancy；表达定义清不把fixedν链代理说精确gradient。 |
| F-L1424「TD3平滑/min」 | 评论家highpeak/overestimation，人工高斯ε clip ±c再project合法A，tail取双Qbar较小；min loweringbias可低估，noise宽会抹窄最优，另延迟actor不是这个式自动条件。 |
| F-L1437「最大熵J」 | 确定动作需外noise，改目标r−αlogπ，α>0奖励分散，真πdiscountE；continuousdensity尺度/negativeentropy解释，不称仅gradientvariance减少。 |
| F-L1450「simplex变分」 | fixedstatefinitelegalq，候选全部概率Δ(A)，max均q+αH，logsumexp平滑max；q finite使p*positive，目的软改进非hardchoose。 |
| F-L1460「logZ−αKL」 | q/α−logZ代归一sum，KL≥0且唯一0→softmaxunique，完整有限支撑，无需用连续无界积分换式。 |
| F-L1470「softQ/V」 | 保熵位置一致：Q当前reward不含当前entropy但tailV有；VactionE[Q−αlogπ]包含当stateentropy，定义约定为后SACtarget依据。 |
| F-L1486「tanh density」 | Gaussian noise可重param变有界a，logdensity=logGaussian−sumlogJac1−tanh²，取物理scale需额logdet；不得漏此改熵和gradient。 |
| F-L1497「SAC y/LQ/Lpi」 | criticreplayrecorda vs actornewa，barmin+tailentropy/truez；LQ halfbatchsquare sg(y)降，Lpi alpha logπ−minQ降等softvalue升，Qparams固但a导通。三式均核，非NN arbitrarybuffer convergence。 |
| F-L1584「q−αKL max」 | 从entropy/KL统一local动作选择，legalprob候选、refpositive支撑，avgq升离ref罚；refzero给infiniteKL支持障碍非温度可解。 |
| F-L1591「指数归一」 | 概率constraint乘子一阶给ref exp(q/α)，sum所有refsupport正常数；uniformref回entropy，oldref镜像一步，动作概率非参数sampling。 |
| F-L1603「精英mean/cov」 | nonmicroprogramblackbox需多参数trial，Gaussianθ候选，higherestimatedJ精英E先非空；MLE mean/fullcov除|E|非unbiasedn−1，smooth/mincov可后。 |
| F-L1626「ES平滑梯度」 | 从CEM选择拟合转扰动score估方向，Fσ=GaussianE J(θ+σε)，σ>0/可積，1/σ回报乘ε由densityderivative，目标平滑非J精确；pairestimate符号相反正确。 |
| F-L1662「三NLL」 | 平均格点不合法故预测fullconditionalP/R/c，真实D E NLL最小，候选φ，likelihood三结果监督非maxcontrolJ；joint乘隐condindependent(r,c|s,a,s')已就地解释，相关可joint或condr。 |
| F-L1713「Dyna同Q式」 | 上游暂不能真返，用model重复valuebackup，sample真实/模拟来源异但r+γclegalmax−Q同外形。c继续非z终，合成次数不算真info。 |
| F-L1774「MVE权重sum/tail」 | 多singlebackup改一continuousL目标，realroot、π后续modelroll、w_{j+1}=w_j c_j屏terminal后，预测r/lastcritic停导。不能依赖的边缘均乘代jointE，firsta给定若Qtarget。 |
| F-L1798「粒子MPC平均」 | 本轮boundedactionsequence候选，不训练Q；M粒子同root/model E以mean估expectedreturn，γreward+tailV；trueobs只executefirst后修，不验证所有候选/openloop非feedbacktree。 |
| F-L1826「CEM平滑/下限」 | 高分E候选先编号破平、mean/coordvar，.5smooth保持history、max逐coord下variancefloor防collapse；合法clip的高斯不是truncatedMLE，final选已评分best非均值。 |
| F-L1847「MuZero g/f」 | search需r/value/prior不pixels，g latent,a→predreward/nextlatent，f→prior/value；hroot在相邻文本定义。非任动作完整environment reconstruction。 |
| F-L1858「PUCT最大」 | legalchildren b分数Qbar+cprior sqrt totalN/(1+N_b)，高value/lowvisit prior鼓励search，cscale/numeratornorm本地述；有限模拟分配非新真实sample。 |
| F-L1877「MZ三loss」 | truefuture r+n-stepsearchtail value target，unroll k0..K value/πcrossentropy及reward k<K，searchπ是visits归一、nottruepolicy labels；支撑encode/no directpixelrequire，停止target/terminal已说明。 |
| F-L1925「短model末Q」 | TD-MPC shortenrolltailcritic，fixedcandidatea、latentdyn/r+γLQ(latentL,policyproposal)，maximizeestimatedreturn not训练proposal即deployment无plan；source为机制式非completeimplementation。 |
| F-L1933「TD-MPC三loss」 | sameTrue record、slowtargetlatent/sg、rewardMSE、Qtarget withc，positiveλ weights，jointrepresentation/dynamics/critic fit。三项目的不同，notalllatentmatch automaticallycontrolcomplete。 |
| F-L1996「全pair R/L1」 | testsmallavg仍假modelmax选择，需要所有legal(s,a)rewardabsdiff/transitionL1；same finite/γ/两Rbound，TV=halfL1因此常数不能换错。 |
| F-L2002「模拟界」 | fixedπ评价模型，rewardterm/(1−γ)+γRmaxεP/(1−γ)²，supvalue for allstate prevents raregap；bound uniformlymodel supports laterselection，testMAE≠these eps。 |
| F-L2016「三误差分解」 | subtracttrue/hatBellman，加减P hatV得rewarddiff+γPvaluediff+γ(P−hatP)hatV，sameπ合法kernel；每项含义可跟踪。 |
| F-L2024「L1×sup tail」 | hatVboundRmax/(1−γ)、L1逐row误差乘sup；随机P不扩sup后移γ得到bound，全式常数手核非TV双计。 |
| F-L2035「选择三差」 | uniformmodelbound适用π*及hatπ、middleε_plan modelnearoptimal，两side各B→2B+εplan；候选策略范围明，fixedold validation不能套。 |
| F-L2077「模型D递推」 | continuousroll参数每step复用，φfixed/ξ独θ，D0=0fixedstart，(f_x+f_uπ_x)D+f_uπθ。stateindirect+currentdirect两条防漏secondpolicy读取。 |
| F-L2086「成本gradient」 | 有限Cstage+terminal要算参数下降，所有t成本state导及action总导、lastD_L terminal；r=−c说明direction转换，需可微可积分不套collision/hardterminate。 |
| F-L2107「矩参数敏感度」 | PILCO不直接sampletrajectory，m=(mu,vecSigma)近似Gaussian moment递推F，chain partialF/partialm×Dm+partialF/θ；可行但multimodal损失不真积分。 |
| F-L2118「两步手算导」 | detscalar q=a+bθ、x1=q/x2=q²，Dx1=b/Dx2=qb+bx1=2bq/Cθ2bq³，a=b1θ−.5→.25、lr.1→−.525。漏statefeedback半导仅该toy。 |
| F-L2160「RSSM三行」 | 真观测后验root/无未来obsprior要区分，detmemory m与randomz状态(x=m,z)、dynadvance thenq(z_next|m_next,o_next) vs p(z_next|m_next)。reward读nextstate时r_t/训练r_{t−1}索引明确。 |
| F-L2171「V3模型loss」 | 真seqsupervisedNLL(o,rprev,cprev)与prior对posterior的KL不足1natfloor，sg侧分两职责、rep权.1，均真实seqE minφ。首无transition项省/1%uniform有说，不能将floor当KL保证。 |
| F-L2198「想象lambda逆序」 | realposteriorroot、π/modelfuture/rhat/chat有效γ=γc，G_L=currentv，G_j=r+γhat[(1−λ)vnext+λGnext]。samefiniteλ尾，预测continue控制贡献，不偷未来trueobservations。 |
| F-L2222「twohot crossentropy」 | V3值尺度使用fixed原始supportprob，T(sgG)软标签与pcritic交叉entropymin，不symlogmean反transform；criticcurrentbootstrap/EMA另regularizer非统一target替。 |
| F-L2231「V3 actor」 | 每j权W=prodprev effectiveγ、sg normalized(G−v)/max(1,S)、SEMA95−5 percentile、entropy正η，maxREINFORCE代理。sample状态/weights/优势固，not直接动力学导或精确trueJ；V2/V3版本不同已述。 |
| F-L2285「TV/eR」 | 长roll折中需量k-step误差，sameπ/rootν，eP逐pairTV/eRabs，指标向小，与前L1不同明定义。 |
| F-L2294「Bk分三项」 | 每深度trueqjπ下Eerrors≤εm/r、两rewardbound/sharedtailVbound，TVstate≤jεm。奖localerr+2Rmax jεm sumdiscount、tail2γkVmax kεm；trueinfinite另γkεV，短k非永好。 |

## 重要行内式

| ID、位置短引 | 人工含义与核对依据 |
|---|---|
| I-L1133/1136「sgbaseline/二阶矩」 | baseline停止导，不让logπ loss导入bθ；优化variance等minrealb二阶矩仅因mean不变，score加权Vpi非总最优。 |
| I-L1167/1168/1185「逆GAE/边界」 | A_T=0、末V只进δ末，非terminal保尾/真实terminalV0、不跨reset；λ1仅completeG无tailbias。 |
| I-L1208/1229「sigmoid坐标/退化F」 | θ+.1prob.525 vsφ+.1θ+.01prob.5025，samecoordinate不等samebehavior；g0/Fsingular分支说明，不用不定归一公式。 |
| I-L1267-1270/1278「η/epsA/occupancy/compatible」 | fullstateTV与pairAmax明确，L1 occupancy及newEA bounds乘η²；compatiblecritic z'w同dpiπ精确regression正规方程给F w/(1−γ)，任network不inherit。 |
| I-L1285/1296/1305「ratio/weights/PPO-KL」 | current/old同a概率、A固定，olddata支撑，batchweights声明；PPOclipflat不hardlimit，KL penalty−βKL方向不同附monitor。 |
| I-L1346/1350-1356/1389「AC数值/steps」 | delta.21，critic.221，actorθ.021→.50525，time0γ0=1；two-timescale sums∞ squaresfinite α/β0仅有遍历/平滑/稳定跟踪时分析。 |
| I-L1411/1413/1420/1432「DDPG代理/TD3noise」 | barQ/barf truey sg，对replayνstatechain只proxy，Jν精确仍后续occupancy；targetnoise不是actual探索，min可能underestimate。 |
| I-L1442/1455/1479/1483「熵/softmax/积分」 | finiteH−sumplogp、continuousmeasure/scale，positivefiniteqsoftmaxsupport；constantq无界空间partition∞反例，不任意换sumintegral。 |
| I-L1520/1538/1544-1549「温度/软targettoy」 | α=eξ Lα=Eα(−logπ−H0)降，entropy低梯度负ξ升；targetτ同步不tauquantile；.82 critic.622、actor−.81仅loss值需导不定parameterstep。 |
| I-L1588/1597/1599「乘子/参考support/最优性」 | KL正support求驻点与归一，ref0不可rediscover；controlas inference需真实kernel变分族固定，只优化policy，不能控制luckytransition。 |
| I-L1602/1612/1630「CEMtoy/ESpair」 | candidates−1,0,1,2得−4,−1,0,−1 tie小θ，elite0,1 newmean.5/MLvar.25；pairES1/(2Nσ)差J±ε，goalGaussian smoothing非原J。 |
| I-L1652/1658/1671「非法mean/joint」 | (.8 right/.1 up/.1down)coordsmean(3.8,2)非法，统计最优不control；c继续/true截断1，jointR/c条件indep或加rewardcondition。 |
| I-L1745-1753/1773/1781「Dyna/MVEtoy」 | modelrecordupstream .86 lr.5 .43 vs trueP .68，replay同record也.43；MVEwprod c保terminal、L2 .685/tail .405丢，非加roll必好。 |
| I-L1805/1807/1831/1833「TS/预算/MPPI」 | TS1每step换member vsTS∞wholeparticlefixed改变joint；L5 N200 M20 E20 I5 countsINML100000/末valueINM20000，不PETS默认。MPPI减max稳定指数权但需参考samplingratio/controlcost。 |
| I-L1845/1854/1865/1873/1887-1891「MuZero」 | h真实historyroot、g/f职责；PUCTvalue统一scale/root0初访问规则/realterminal尾0、value/πsearch targets可reanalysis，latentconsistencysg不保无塌缩，均本地说明。 |
| I-L1923/1930/1945/1951「TD-MPC」 | zencoder/dyna/r/Q/proposalpi五模块，shortcandidate scoretailQ；loss权/target与模型latentunit明确，TD-MPC2额design非初版同loss。 |
| I-L1979/2010/2032「利用toy/TV/selection」 | rarepath真.1模型.9 vs安全.6/testing99%safe MAE.008却loss.5；L1定义不TV，统一bound两策略三差给选择，fixedpi不能只平均就选。 |
| I-L2083/2095/2104/2145「Jacobian/导数误差」 | f_x/f_u/π_x/πθ currenteval、costmin rneg，m分布矩区别xsample；hatf=u+εsinωu supε而导εωcos可大，函数值界不控制policymodelgradient。 |
| I-L2159/2168/2185「时间索引/KLfloor」 | memory/random合x，预测进入x_t对应r_{t−1}/cprev；floor1nat/rep.1与1%uniform独不同，no重建即control充分。 |
| I-L2206-2209/2218/2227/2230「V3值/优势」 | toyγ.9 λ.5 r.2,.3/v.4,.6→G1.84 G0.758，c1=0→.3/.515；symexp rawsupporttwohot原值域weight sum1、EMAregularizer/.3replay非bootstrap替换；Wdiscount和SquantileEMA代理条件齐。 |
| I-L2269/2279/2291/2301/2306-2310「MBPO」 | real/modelbuffers/version分，F/B/k/realratio/dataage固定；modelrecord .41target即使true可发生也非观察；qπ≤Cqmu给非negativeerrorE放C，oldMSE不TV/coverage，wholecandidateuniform才selection支持。 |
| I-L2334/2336/2353「一步model利用/罚」 | a∈[−1,1],R−a²/hatR−a²+.8a，data0误0但grad.8→.4/hat.16/true−.16，对old准确不对new；λu惩罚需u敏感不能凭ensemble一致有TV校准。 |
| I-L2366/2369「视频协议数值」 | 2541h360p20fps/23binarykeys121mouse及1000world60min/.7%按原预印本声明，notV3同budgetcomparison；数据/版本是外部事实本轮仅核表达未一手查证。 |

记录结论：展示式和关键行内式的本文机制/代数与边界已核；没有在本范围新增成立发现。所有外部算法版本、论文实验数字及常数仍保留一手来源未核限制。
