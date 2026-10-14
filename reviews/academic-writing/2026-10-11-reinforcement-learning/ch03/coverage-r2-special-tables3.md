# 第3章R2特殊单元：表格3

CH03-R2-ST3，2026-10-12，修订1；独立R2；hash `927887345166301fb9aaa47eb6a53ec8389f7abfe6353bc87e5b27b5049f353e`。按原源T28-T40表头、全部列和表注亲自读取并判断。原行ID稳定，表注W中有逐句记录。

| ID、位置短引 | 白话及具体依据 |
|---|---|
| T28-H L2402「职责/输入输出/学习」 | 当前房间行为调用需高层/内部/终止三职责，非highlevelname即可备份。 |
| T28-R2404「高层」 | state/task→ω或subgoal，ζ/行为Q/启动条件要指定或学，不能任state无条件启动。 |
| T28-R2405「内部」 | state/ω或goal→atomic a，lowπ与optionalauxreward，不混原始全局目标。 |
| T28-R2406「终止」 | state/ω→交还控制，β/timeout/reach条件，Option超时不自动environmentterminal。 |
| T28-C L2409 | handcode/discovery是取得三对象方式非额外职责。 |
| T29-H L2571「方法/先验/学习数据难」 | fixed内部Option备份转如何取得内部/β，比较先验而非单algorithm无结构叠。 |
| T29-R2573「Feudal」 | givenhierarchy/stateabstract/instruction，各层select/execution，localR可限制globalbehavior。 |
| T29-R2574「MAXQ」 | subtaskgraph/termination/pseudoreward，childV+completionC，保证依分解/stateabstract；recursiveopt不global。 |
| T29-R2575「Option-Critic」 | Ω数/parameterization/启动约定先给，learninternal/β/highQ，可能short/redundant，未保证自动有usefulskills。 |
| T29-R2576「HIRO」 | goalcoords/window/distanceR，highlowoffpolicy，currentlowa likelihood校旧goal意义，notfabricatetruepath。 |
| T29-R2577「HAC」 | goalspaces/executionbudgets/test机制，hindsighta/hindsightgoal/subgoaltest分别作用，onlysuccessrelabel会overestimate不可达goal。 |
| T29-C L2580 | 每层必须state/goal/a/R接口，not复制singlelearner堆叠。 |
| T30-H L2648「方法/区分对象/信号条件」 | noR先学differentcontrolledoutcomes，condition/outcome不同改变MI含义。 |
| T30-R2650「VIC」 | givenstart skill/end，conditionaldiscriminatorlowerbound、termination/reach定义outcome，not任终点distribution。 |
| T30-R2651「DIAYN」 | skill vsvisitedstate、classifierR+actionentropy，distinctstate不保证taskrelevant。 |
| T30-R2652「DADS」 | givenstate skill/next，skilldynlikelihoodratio/predictable+diverse，finiteM近似非exactMI。 |
| T30-R2653「CIC」 | continuousskill/transitionembedding、contrastfit+representationentropyreward，distance/negatives决定，notDIAYNclassifier替名。 |
| T30-C L2656 | 没有一个通用MI损失，条件与后果选择要声明。 |
| T31-H L2703「保证/数学量/输出条件」 | finitebudget需明确输出vsprocess，概率训练随机性/环境E分开。 |
| T31-R2705「PAC」 | loss≤eps prob≥1−δ，budget/stop/参照class/singlemix输出全须声明，notasymptoticconvergence。 |
| T31-R2706「regret」 | 全K回合累sum价值diff hprobB(Kδ)或Ebound不能交换，与最后strategy不同。 |
| T31-R2707「simple regret」 | outputlossΔ_N=J*−Jhat，expected或hprob明确，不将meanε称PAC1−δ。 |
| T31-R2708「识别」 | Pπhat∈optimalclass≥1−δ，exact需gap、optimalmultiple可能，not默认唯一。 |
| T31-R2709「最后」 | π^(K)本身loss，averageregret小不能保last，randomhistoricpolicy输出不同接口。 |
| T31-C L2712 | 渐近/PAC/process/last不同问题。 |
| T32-H L2725「访问/查询/困难」 | 生成模型trueoracle不同learnedmodel，online到达vs任query，lowadapt附约束可叠加。 |
| T32-R2727「oracle」 | anylegalpair真实independentsample，仍需微小gap辨识但无actualreachcost，不是hatPdraw。 |
| T32-R2728「onlineepisode」 | agreeddistribution/adversarialroot，within必须a取得cover，不能任跳state。 |
| T32-R2729「continuous」 | norestart/prevaction接state，reach/return/traps/averagecommunication条件，不能用episodeH替。 |
| T32-R2730「少适应」 | 同batch规则提前固定、轮间反馈才改，同N可能costmore，约束反馈节奏非新互斥environment类。 |
| T32-C L2733 | sampleN放协议才可比，附加lowadapt可叠。 |
| T33-H L2767「method/目标访问/乐观条件」 | tablefinite按counts、PAC与regret及average/episodic不同；不能单N排优劣。 |
| T33-R2769「E³」 | finitePAC/effectivehorizon/mixing，knownregionexploit vsunknownreachplan两职责。 |
| T33-R2770「R-MAX」 | finite近优/average适当mix时间，不足count给maxrewardoptimisticmodel，不anytask即PAC。 |
| T33-R2771「UCRL2」 | no-resetcontinuousregret、finiteD communication，R/Pconfidenceplan，D不是H。 |
| T33-R2772「UCBVI」 | fixedHonlineepisode/regret、empiricalP+valuebonus，此后theoremunknown时齐P/knownR，不任Pt。 |
| T33-C L2775 | PAC/regret不是同计数目标，持续/episode访问不同。 |
| T34-H L3016「复杂度/对象/区别」 | 低Bellmanrank的有限残差方向后compare邻概念，不替各条件。 |
| T34-R3018「Bellman rank」 | rollin分布与candidatemeanresidual因子，ζnorm与πclass，notweightmatrixrank。 |
| T34-R3019「Witness」 | candidateP通过testfunctions被data区分的modelmismatch证据，依model/testclass不是Qloss。 |
| T34-R3020「Eluder」 | successiveinputs上未被priorobservations约束函数difference，pointwiseindependence，不自带dynamic/Bellmanbackup。 |
| T34-R3021「Bellman-Eluder」 | residualclass/alloweddistribution的序贯独立，point→residual/distribution明确转换，分布族须给。 |
| T34-C L3024 | 不能交换维度代另一算法bound，名称近非定理同。 |
| T35-H L3092「障碍/证据/能推什么」 | 两instance信息lowerbound与样本可行/computeefficiency三对象分。 |
| T35-R3094「信息」 | fixedprotocol难区分environment/testinglowerbound，对anycompute不够N不能targetguarantee。 |
| T35-R3095「样本有效compute贵」 | algo枚举largeF/difficultsolve仅currentconstructioninefficient，全算法计算难要reduction/assumption。 |
| T35-R3096「compute有效强结构」 | knownφ合法linearP/executablemax，族内两预算兼顾不任NN满足。 |
| T35-C L3099 | costlysubstep不证明计算lowerbound，oraclevsrealrunningcost明确。 |
| T36-H L3122「budget/计数/误读」 | 同trainstep混info/computation故七实际单位，真/datareuse/model/planning分别。 |
| T36-R3124「trueenv」 | totalactualtransition/并行相加，vectorcall非1、actionrepeatframes另计。 |
| T36-R3125「gradient」 | optimizerupdates分别actor/critic/model，两个Q更新不与singleQ含混一步。 |
| T36-R3126「replayratio」 | U/Nenv更新比vsUB/Nenv抽条比差B，B/U变按actualbatchsum，计对象齐。 |
| T36-R3127「modelsamples」 | synthetictransfers/roots/L分别，1million不1milliontrueinfos。 |
| T36-R3128「walltime」 | samehardware/parallel、采/训/测/总耗时，不只nettrain漏plan/simulation/wait。 |
| T36-R3129「param/memory」 | trainable、target/ensemble数/peakmem含buffer，sameparams不samecompute。 |
| T36-R3130「deployment」 | perdecisionmodelqueries/candidates/latencyquantiles/hardware，train省samples可executionsearch贵。 |
| T36-C L3133 | 动态U/B按各批实际大小，不用finalconfig代整个过程。 |
| T37-H L3175「抽样unit/随机与量/不能替」 | fixedpolicytestvsindependenttrainlayers，CI覆盖对象要明。 |
| T37-R3177「one测试」 | root/noise/πsampling，G/length/succ事件单样本，luckyone不是policyE。 |
| T37-R3178「fixed产物」 | 多tests mean/CI是sameπ性能，不retrain失败率。 |
| T37-R3179「independenttrain」 | seeddistribution/mean/robustsummary+CI，更多sameseedtest不能消训练Var。 |
| T37-R3180「multitask」 | pertaskscore/明确normalize汇总/performance分布，sameproducttask相关不独samples。 |
| T37-C L3183 | trainingseed/testRNG/task抽样分别，95%需coverage谁不是裸percent。 |
| T38-H L3229「基准/info/randomsplit/terminateversion」 | sameenvname未保协议，columns可判定samea/info/P/R目标。 |
| T38-R3231「ALE」 | pixels/internal/stack/actions/repeat、sticky/randomstart/testseed、trueover/lifewrapper/timecap/ALEversion/ROMhash，不写流行default唯一。 |
| T38-R3232「Procgen」 | pixels/actionmap/wrapper/input、Ntrainlevels/seedrange/unseen/difficultydist，end/trunc/pkg/game/generatorseed记录；重合train不是同generalization。 |
| T38-R3233「continuous」 | state/pixels/physicala/controlfreq/repeat、dynnoise/initial/taskperturbs，failure/timecap/simulator/model/taskversion，不同bodyname不直接比。 |
| T38-C L3236 | actualconfig读prob/repeat，不固定唯一default。 |
| T39-H L3259「复现/最少保存」 | code/data/semantics/selection/failure/resource六并列真实条件，not形式追加清单。 |
| T39-R3261「代码配置」 | commit/deplock/env/wrapperversion/actualexpandedhyperparams，cfg要可恢复不只algo名字。 |
| T39-R3262「data/RNG」 | real/modelsource/N/trainingevalRNG/initial/split，支持协议可比较。 |
| T39-R3263「updates」 | samplingπversion/targetπfreq/terminalmask/replayratio/dataage，改变实际target与分布。 |
| T39-R3264「selection」 | candidates/tune/validation/stop/checkpointrule/independentfinaltest，防choosebest再报unbiased。 |
| T39-R3265「failure」 | definition/rawresult/infrastructure重跑规则/count，不删低种子而篡总体。 |
| T39-R3266「resources/artifacts」 | hardware/precision/parallel/wall/deploymentbudget/checkpoint/perrunlogs/plotscripts，程序本轮未运行。 |
| T39-C L3269 | systems细节可后卷但影响samplingtarget接口必须本experiment说明，crossref不替必要解释。 |
| T40-H L3286「interface/update/actionsource」 | 章首实际四组合回答的汇总，sharedexplore/representation/temporal条件，非各系统只学一种对象。 |
| T40-R3288「modelfreevalue」 | MC/TD目标Q表示，greedy/exploreaction，SARSA/Qlearn/DQN差异此前已展开。 |
| T40-R3289「modelfreeπ」 | θ通常另critic，PPO/SACπ执行，offpolicycalibration/cover需查，不能以directπ去掉value误差。 |
| T40-R3290「modelvalue/planning」 | learnedP/R和所需value/prior，DynaQ或MPC/MuZero/TD-MPC currentplan，不强称全部训练independentV。 |
| T40-R3291「modelπ」 | P与modelgradient/syntheticactorcritic，PILCO/Dreamer/MBPO训练后π，latent推断仍modelcall。 |
| T40-C L3294 | 混合按真实data/actionflow说明，不为了四格分类宣称互斥独立。 |

本文件13表头、56表行、13表注。ST1-ST3完整覆盖40表、40表头及159数据行；表注W有自然句记录，表中重要行内公式已在对应行核对。源表结构与正文比较关系已核，未检查PDF排版或外部表格来源。
