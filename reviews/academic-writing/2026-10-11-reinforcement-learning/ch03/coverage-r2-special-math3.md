# 第3章R2特殊单元：公式3

CH03-R2-M3，2026-10-12，修订1；独立R2；hash `927887345166301fb9aaa47eb6a53ec8389f7abfe6353bc87e5b27b5049f353e`。规则同M1；展示式所有内部行和重要行内式逐项人工核，未执行数值程序或外部完整证明。

| ID、位置短引 | 当前缺口、符号集合、运算方向理由、判断 |
|---|---|
| F-L2434「Rω+gamma^K G」 | 高层随机决策间隔不能当原一步，K实际有限长度、原子r索引分组，前K奖按γj累加/未来从t+K再γK；保持原始目标非高层计数目标。 |
| F-L2443「Option Bellman」 | fixed内部/β后(s,ω)决定joint K/end/R，高层ζ在合法启动集平均futureQ，E conditional起点/ω；终环境tail0、主动Option结束非0，record需K与Rω。 |
| F-L2455「高层控制max」 | fixedζ评价转control，下一允许Ω(state)中max更高estimatedreturn，实际γK不γ。sample残差lr上调/下调；非重新定义高层时间。 |
| F-L2473「E gamma^K sup」 | fixed规则rewardcancel，有界V/W、K≥1 a.s.finite、γ<1，EγK≤γ、概率平均/max不扩、supstate覆盖全部合法调用。不是学习内部π时同算子固定。 |
| F-L2488「yA .572」 | 房间独立task同起终/全部step−.04，K2/tail.8，−.076+.648=.572，实际stepcost/discount顺序齐。 |
| F-L2491「yB .38732」 | K4四stepcost−.13756+tail.52488=.38732，wrongγ一次.58244，randomK不能γEK EV，不因sameendpoint忽略duration。 |
| F-L2512「U/QU/QΩ」 | 每原子step可续/切换，allΩ可启动前提、βnextmix currentωQ与ζreselectV；QU=R+γP U、QΩ=πωavgQU。三评价位置不同，trueenvironmentterminalU0。 |
| F-L2527「内部gradient」 | fixed高层ζ/β，扩state(s,ω) currentπa，归一原子discountdΩ含dummy吸收延拓，1/(1−γ) scoreQU；baselineQΩ与a无关可减，非high-leveldecision occupancy。 |
| F-L2539「终止负A」 | νparamβ抵达后∂U=V−Q=−A，futureγ^{t+1}因先step再终止，sumarrival E，归一对应−γ/(1−γ)。A>0续更好降低β、A<0升β，高层θ偏导另计。 |
| F-L2598「MI」 | no taskreward先学differentcontrolledoutcomes，fixeds0/K、Z技能/后果Y，posterior/priorlog E=H(Y)−H(Y|Z)。选择行为影响后果可辨非不可控noise，开闭loop控制类区别明。 |
| F-L2609「判别MI下界」 | trueposterior不可计算，用带Z标签fitq，加减logq得posteriorKLgap≥0，下界signal logq−logprior，max策略分辨、qMLE，uniformprior常数不保taskcoverage。 |
| F-L2627「DADS近似比」 | target I(Z;S'|S)，conditionalskillmodelq denominatorM priorz均近似marginal，比预测性/多样性，r_int训练；finiteM/log非精确MI、不宣称无偏下界。 |
| F-L2682「PAC P」 | finite预算输出hatπ，参照声明策略类maxJ，loss≤eps的训练/alg概率≥1−δ，J已部署E。输出single/mix/stop协议先定义，不将expectedloss改highprob。 |
| F-L2690「episode regret」 | H/K/T=KH、各k给定起点与π的expectedvaluediff求sum、向小，过程代价非最终output/真实rewardnoise差。无γ有限H目标新范围明。 |
| F-L2782「UCBVI三min」 | 已知detR[0,1]/unknown时齐P/nooracle，remainingvalue reverse、legalmaxa动作，min历史上界/H/empiricalbackup+bonus保optimism。zeroN维持H，notHoeffding同BF保证。 |
| F-L2790「BF三bonus」 | N>0、empiricalP/nextV variance、Llog、next时刻count n∨1，sqrtVar/N+range14HL/(3N)+数据依赖误差sqrt weightedmin(countbound,H²)。内min两有效界更紧，经验E后继；不省第三项冒用定理。 |
| F-L2807「BF regret三项」 | T=KH/Llog5HSATδ、同原算法/hprob1−δ，30L√HSAT +2500H²S²AL²+4H√TL，首/尾K→T转换正确；主导尺度仅largeT区。 |
| F-L2830「计数三和界」 | sum1/√n≤2√m、sum1/n≤1+logm、allSA sqrtN≤sqrtSAT由Cauchy/总N=T。半径作用真实visit不是gradient/model次数；前两m≥1零访另处理。 |
| F-L2852「linear R/P测度」 | largeState需可检验sharedstructure，knownφ d/unknownθ_t与vectorμ_t对所有可测B，合法非负全空间1。仅Q*linear不保P/R此结构。 |
| F-L2858「mixture kernel」 | knownbaseP_i、unknownη∈simplex，区别unknown后继测度；每核合法/凸组合合法，generalcoef需另probconstraint。 |
| F-L2869「线性backup」 | anyboundednextV，积分μ系数+θ而已知φ不变，说明任意中间backupclosure。mixture特征P_iV随V变，不能互换保证。 |
| F-L2879「LSVI四式」 | reverseH−1..0/currentk旧samples重算nexttargets，Λ positiveλ+outerproducts、wregressioninverse、bonusβ directionalnorm、minH optimisticQ。argmaxfinitea真执行nextrecords；非固定labels仅最新update。 |
| F-L2913「全测试范数」 | 所有boundedmeasurablev vectorμ积分norm≤√d supv，保障真实backup参数界；不以有符号测度totalmass替totalvariation、state/feature单位正确定义。 |
| F-L2920「d³H³T regret」 | knownφ≤1/θ≤√d/detR[0,1]/onlineH/λ1/βcdHsqrtlog、universalC、hprob1−δ，无显S但feature与maxa可执行。不是任NN拟合Q*同样bound。 |
| F-L2934「det lemma」 | adaptive新direction误差预算，Λpositive更新rank1，det ratio1+φ'Λ^-1φ，logdet控制direction累和，再Cauchy/H汇成regret；此证明支点非原proof全常数。 |
| F-L2955「complete backup」 | F_t类/终F_H0，可实现只Q*成员，complete任nextf的realR+Pmaxf属本F_t；换regressionG应T F⊂G，量词/候选域全。 |
| F-L2973「Bellman平均残差」 | 候选groll-in到t再f于t/t+1、f值−r−fnext，E访问由g决定且动作由f；用于模型排除不是随意trainMSE。 |
| F-L2979「因子/norm bound」 | eacht统一M维ν(g)/ξ(f)内积+prod norms≤ζ，约束environment/F/访问共同，非某weightsmatrixrank；alg无需知道maps但proof依赖。 |
| F-L2992「OLIVE回合bound」 | onlinefixedreset/H/A/episode总奖≤1/finiteF N values[0,1]/实现Q*/Mrankζ≥1、原阈值batch，回合~M²H³A ε^-2logNζδ；原子反馈乘H、notperstepR1归一。 |
| F-L3003「f预测−J=残差和」 | 停终fH0、sameπftrajectory telescopes，initialprediction−actualexpectedG=sumE(f,f)，大差至少某t大；evidence选时刻随机a覆盖检测otherf。 |
| F-L3057「两环境n下界」 | H1/a2、Δ≤.25/epsΔ4/δ<.25、任何adaptiven条件reward/输出randomπ；n≥log1/(4δ)/(16Δ²)=/(256eps²)。限制信息需求非全部SAHfactor。 |
| F-L3068「KL链」 | samedecisionalg两环境仅arm1rewarddiff，wholehistorylawKL=E+N1 kl(.5±Δ)≤16nΔ²；KL约logratio inequalityΔ bound，two-lawtestingerror≥.5exp−KL给n，外部检验不等式未重证明。 |
| F-L3163「两层均值」 | fixed产物test轨迹G_mn平均Ntest估产物J_m，再M独立training平均估algmean，sampleunit先定义；不拿1000tests替1000trains，数值均高回报向好。 |
| F-L3188「total Var两项」 | J_m varianceτ²、conditionaltrajVar平均σ²，训练independent/testsconditionalIID，Varavg=τ²/M+σ²/(MNtest)。Ntest只降低第二项，pointwisecurveCI非simultaneousband。 |
| F-L3203「chosencheckpoint .65」 | trueboth.6/independent±.1，max测值.5 prob1/4/.7 prob3/4，E.65；chosenactualmean仍.6，+.05selectionnoise而非policyimprovement。 |
| F-L3245「human normalize」 | 多gameunits需fixedrandom/humanreferences、S_HN(agent−random)/(human−random)，largerbetter仅正分母；small/0/反常分母排替规则、30/10/50得.5不是raw50%。 |

## 重要行内式

| ID、位置短引 | 人工核对 |
|---|---|
| I-L2384/2386/2395「独立房间/5原子2高层」 | 8x5/wallx4|5门y2,4/start2,2/goal7,2、γ.9/- .04/入目标1与baseline4x3不混；continuousforce仍atomic、discreteω可持续random。 |
| I-L2423-2429/2431「Option三元」 | I启动、πinternal、β到达terminateprob，先≥1step再检测、Markovonlys/ω；memory/duration需expandstate，K1atomic可保。 |
| I-L2468/2483/2494「compression/紧因子」 | fixedrules theorem ∥TΩV−TΩW∥sup≤γ∥V−W∥，tight sup_{s,ω} EγK覆盖all合法非avg；永不终需另定义，不能推longoptionlessdata。 |
| I-L2511/2521/2524/2535「VΩ/y/dΩ/baseline」 | allΩ可启动取ζ重新选择V，y=r+γU true终0；dΩ原子γ占用延拓dummy mass1，QΩ baseline动作前，notoption切换计时。 |
| I-L2537/2547/2550「termination方向/toy」 | ∂U/∂β=V−Q=−A，归一arrival−γ/(1−γ)，Q.6/V.9/β.25→U.675/y.5675、−β(1−β)A=.05625，续比切更差终止不是absolute低值。 |
| I-L2556/2560/2584「MAXQ/HIRO/层级反例」 | Q_i=V_child+C父remaining含Kdiscount，recursiveoptimal弱global；HIRO当前lowπloglikelihood旧a重目标不是newtrajectory，forcedupperdoor9stepreturn.20265vs5step.51854且原子保留可表示但不保证学会。 |
| I-L2593/2603/2619/2623/2638「技能posterior/empower/CIC」 | priorbeforecall、Y指定outcome、empowermaxopenloopsequence distribution允许域明；uniformprior不保task，DIAYNstate平均与VIC条件终点不同，CICcontrastbatch match不等innerentropyreward。 |
| I-L2660「log3反例」 | 三det技能终点distinct、Zuniform posterior确定→MIlog3，却allpoliciesstayleft任组合不穿门，说明可分不任务可达/启动相容。 |
| I-L2681/2687/2716「类内参照/混合输出」 | π*只声明classmax，J部署E vsPAC训练P；uniform选择历史policy meanε不hprobε，averageparameters非πmix。 |
| I-L2737/2739「可检验协议/奖励尺度」 | finiteS/A/r[0,1]/γ.9/oracle/δ.05/eps.1仅example，H20/VH0 online目标bound20非discount10，averageg/diameter需别protocol；K/H/totalr归一改变Hfactor。 |
| I-L2759「直径/UCRL2」 | D=maxall(s,s') minallowedπ Efirsthitτ，min求最快可达/max确保最难pair，通信finiteD排trap；~DS√AT continuousregret条件不换H。 |
| I-L2788/2801/2818/2841「UCBVI条件」 | V=maxlegalQ、zeroN H、threeBFbonus归纳上界；K→T首30HL√SAK/尾4H^1.5√KL核；expectedlower c√HSAT适当largeT非samehprobstatement。 |
| I-L2865/2875/2896/2906/2918/2938「LSVI限制」 | mixturefeaturesP_iV随V变/linearφ固定，Q*实现弱anybackup；Λdiag101,2由100e1+1e2、半径.0995/.7071；βcdH√log、detbound(1+K/d)^d/Cauchy，文献误设扩展未并定理。 |
| I-L2961/2965「两类/反例」 | T F_next⊂G另class，H2/R0/F1{0,1}/F0{0,2} containsQ*0 but T1=1notF0；fixedzeroterm/identicalcompletebackups才能reverse推实现。 |
| I-L2985/2991/2997/3000/3007「rank/OLIVE」 | 表格νstateprobs/ξerrors维≤S直观；finiteN/ζ≥1上调不改condition、~hide只对数/回合乘H；Q*不删与volume shrinking支点非complete原proof。 |
| I-L3028/3030/3032「相邻复杂度」 | Eluderpointwise、witnessmodeltest、BellmanEluderresidual/访问族，具体算法实现/complete不同不把维交换samplebound。 |
| I-L3047/3049「锁链反馈」 | observedprogress deterministic记prefix至多A层次×H走前缀→O(AH²)步；randomsuccess A^-H只strategy；隐藏时间only失败仅排one串→Ω(A^H)attempts，非fullyobservableMDP通用。 |
| I-L3065/3074-3078「下界证明」 | p+≥.75/p−≤.25使testp>.5两error≤2δ，kl=2Δlog((1+2Δ)/(1−2Δ))≤16Δ²、testinginequality联立；teacher常数直接derive不借论文全部factor。 |
| I-L3126/3137-3144/3145/3153「预算」 | replayU/Nenv vsUB/Nenv差B、变化batch需actualsum；samegridQ/Dyna不能oracle真实P，samehyperbudget，samplefixed vswallfixed是两个target；20seeds100testprotocol非已运行。 |
| I-L3195/3197/3209/3211「报告/选择」 | IQMmiddle50%与mean/median不同target、thresholdnormalizedscore>τ方向好，τ此threshold非方差；taskfixedbootstraptrain vsnewtaskouter抽/task相关整组；validation选择+independenttest非同test挑再无偏报。 |
| I-L3240/3242/3250-3252「终止与score」 | true终tail0/trunc继续target.68误当终−.04漏.72，timefinite任务零尾需remainingtime；auto-reset finalobs别newroot；HNrefs/scale/clipping改变汇总而非rawpercent。 |

M1-M3完成全部147展示单元，独立ID以原式首行绑定；表行内公式另在ST各行检查。记录完整不消除CH03-R2-01；真实程序、外部原证明和版面仍未执行。
