# 第3章R2特殊单元：表格2

CH03-R2-ST2，2026-10-12，修订1；独立R2；hash `927887345166301fb9aaa47eb6a53ec8389f7abfe6353bc87e5b27b5049f353e`。规则同ST1；按源逐表头、逐行所有列及表注重新核。T15-T27覆盖L1187-2361。

| ID、位置短引 | 白话及具体依据 |
|---|---|
| T15-H L1192「critic位置/估计/偏方差」 | 固定同π梯度，比较减statebaseline与替future；前文已有基线零均及GAE误差推导。 |
| T15-R1194「状态基线」 | 完整G−V，动作前固定保gradientE，V误差仅影响Var、不保下降；不需V精确。 |
| T15-R1195「future替代」 | r+γVnext−Vnow，尾误差随a变化通常bias，不能借前行baseline不偏。 |
| T15-R1196「多步混合」 | 指向已释GAE式，λ及L共同决定预测尾依赖/真实奖跨度，不只λ决定无偏性。 |
| T15-R1197「同批拟合」 | 该a回报训练b后扣b可能携a信息，需condindep、oldratio/repeatedoptimization检查。 |
| T15-C L1200 | subtract与replace两个运算区别准确。 |
| T16-H L1377「接口/数据时机/条件」 | 同AC接口，sync/async/advantage长度可组合，非互斥算法层次。 |
| T16-R1379「一步AC」 | 每真实transfer改V/π，TDerror/steps/weights需核，discounttime保目标已给。 |
| T16-R1380「A2C」 | 多环境shortseq同参数同步batch，π版本/true终一致，parallel改组织不凭空info。 |
| T16-R1381「A3C」 | workerlocalπ采、asyncgrad滞后冲突；global当前π非严格onpolicy，不称无需校正。 |
| T16-R1382「GAE AC」 | criticfreeze生成A后改actor，λ/tail/estimatorfixed及重复batch的distribution条件明。 |
| T16-C L1385 | sync/async与优势长是不同维可组合。 |
| T17-H L1557「校正位置/数据边界」 | 比behavior/learner差的处理，不把distributed采本身当guarantee。 |
| T17-R1559「ACER」 | IS截+补bias、Retrace评价、π变化约束；少补偿即不同估计器，三职责不替support。 |
| T17-R1560「IMPALA」 | Vtrace修mu/learner滞后，采学解耦、rho截改有效target；前文有explicitπ_barρ。 |
| T17-R1561「MPO」 | KL限定非param动作E步/paramfit M步，replaystate/Q来源明，动作改进不解决statecoverage。 |
| T17-R1562「APPO」 | asyncVtrace+proxratio代理，行为/target/learner可能三个π，sync/ratio需version具体；实现族不统一定理。 |
| T17-C L1565 | 同缩写不代表同估计目标。 |
| T18-H L1689「表示实例/fit/接口局限」 | 非格点mean反例后改output/representation，显式与latent、randomlatent与paramposterior不同层。 |
| T18-R1691「显式」 | 已定义position/velocity后继distribution、R已知或学；送value合法state，coorderror与单位/决策后果合读。 |
| T18-R1692「World Models」 | VAEcompress+mixturedensityrecurrent latent、controller读memory/representation；可ES训练，非每stepMPC。 |
| T18-R1693「PlaNet」 | detmemory+randomlatent RSSM fitobs/R/multistep，latentactionsequenceeval/firstaction执行；rollquality/stateinference仍需。 |
| T18-C L1696 | latent随机、参数posterior、ensemble三不确定层不混。 |
| T19-H L1762「来源/可重用生成/风险」 | Dyna同record与replay算同.43之后问extraquery能力，非仅次数比新信息。 |
| T19-R1764「replay」 | 复用已有wholetransfer，coverage不足/oldpolicyweights/correlation依旧，不能查询newactiontrueoutcome。 |
| T19-R1765「经验表model」 | 已见pair经验分布E或sample，finitecount误差，重复modeldraw不增trueinfo。 |
| T19-R1766「parammodel」 | newpairs泛化并roll，OOD/terminationwrong/fictionalreachable风险，比表model更强假设。 |
| T19-C L1769 | 更灵活接口需要更强预测正确条件。 |
| T20-H L1814「优化器/候选更新/预算」 | sameestimatedF下三solve接口，PETS/PlaNet组合不能与CEM互斥列。 |
| T20-R1816「shooting」 | fixedproposal序列highestscore、no导、一次N，无eliteadapt区别CEM清。 |
| T20-R1817「CEM」 | iteratesamples截高scoreelite/MLdistributionfit，no导但I/Eratio/floor/constraints配置必要。 |
| T20-R1818「MPPI」 | nominalseqnoise/exponentialreturn或negativecostweightsmeanperturb，standarddyn/noise匹配，general需IS/controlcost；不从指数alone保optimal。 |
| T20-C L1821 | 优化器与modelplanning系统不同层。 |
| T21-H L1900「model要求/检查/不推出」 | 不以视觉细排统一好坏，前MuZerovalue/search目标明确。 |
| T21-R1902「观测重建」 | obs当前futureerror/likelihood只观测，对关键a排序、unseen反事实、安全无automaticguarantee。 |
| T21-R1903「reward/value/π预测」 | 指定a-seq下R/strategyvalue/searchdist，不能任π/任depth/全规则预测。 |
| T21-R1904「control充分」 | 所需π/intervention集上保decisioninfo，不继续声称其他π/task/干预有效。 |
| T21-C L1907 | 要求按实际下游task而非视觉精细度。 |
| T22-H L1960「planning/modules/a/budget」 | 同query预算仍需countmodulecalls、branch/particle/depth不同，valueguide可配optimizer。 |
| T22-R1962「latenttree」 | encoder/dyn/R/prior/leaf，finitebranch直接、continuous需候选机制，reusebranchstats分expand。 |
| T22-R1963「trajectory」 | dyn/R optionaltail，vectorconstraint可jointsample；N/M/L/I相互预算竞争，不只一N称相同算力。 |
| T22-R1964「shortvalueguide」 | latentdyn/R/tailQ/πprior，commoncontinuous，critic替longtail、query短优化；notpureparamπ执行。 |
| T22-C L1967 | tailvalue是评分组成不另互斥optimizer。 |
| T23-H L2051「检验层/回答/所需」 | 模型值界和selection以后回看证据层次，非全modelquality一数。 |
| T23-R2053「重建」 | 已观测encode/restore，still decision量/history充分缺证，不能derivefuturecorrect。 |
| T23-R2054「predict一致」 | 已covera-seq吻合，longerroll/newπ/calibration条件另需。 |
| T23-R2055「反事实」 | changea仍modelvalid，所需干预truecoverage或identifiable结构；observationalfit不替。 |
| T23-R2056「control」 | representation/model保所需πdecisionquality，task/πclass/depth/err→performance明才可判断。 |
| T23-C L2059 | 前行通过不automatically后行，不含“重建必充分”的逆推。 |
| T24-H L2134「接口/modelinfo/算误」 | modelgradientchain/矩传播/blackbox各依不同model信息；localtoy后固定比较。 |
| T24-R2136「path backprop」 | 可微P/R/π、噪声可重param或另梯度，存/重算L、导连乘消/爆、sampleVar/modelderivbias。 |
| T24-R2137「analyticapprox」 | 可算矩/expectedcost/derivatives，mu/cov传播依distribution/kernel/cost形式，momentapprox bias不trueexact。 |
| T24-R2138「blackbox」 | 参数modelreturn样本，多candidate/noise重复，无Jacobian但wrongranking可利用，no微分非noerror。 |
| T24-C L2141 | 降部分searchcost却增derivativequality要求，不无条件更省总budget。 |
| T25-H L2252「阶段/calls/cost检查」 | Dreamer部署无search仍modelinference，训练/想象/执行/再学四phase费用明。 |
| T25-R2254「真实seq」 | encode/posterior/reconstructpredictheads/φupdate，realN/seqL/backprop memory必须计。 |
| T25-R2255「想象」 | 多trueposteriorroots priorroll、actor/R/c/value每step，modeltransfers/Qπupdates计，高hatreturn需trueeval。 |
| T25-R2256「部署」 | newobs recurrentmemory/posterior/currentπ，still per-stepstateinferencecost；stochastic/deteval预先固定。 |
| T25-R2257「online再学」 | newrecord入D交替φ/Q/π，allowedinteraction/updatewhen/afterupdatestate重新算配置；离线不假免费边。 |
| T25-C L2260 | compute位置改变不消除，非statelessnetworkalone执行。 |
| T26-H L2317「design/直接/未保」 | Bk誤差界后列限制，均设计需验而非全局安全性能证明。 |
| T26-R2319「realroot」 | 避免长modelhistoryroot，可能oldπroot/futureoutofsupport，true根不把tail变true。 |
| T26-R2320「短k日程」 | 连用wrongP次数少，不保tailvalueaccurate/koptimal；γkεV trade-off已式说明。 |
| T26-R2321「real比例高」 | 合成batchweight低但不填real未见a，质量非仅比例。 |
| T26-R2322「ensemble筛」 | 排显成员disagree，共同错仍在，disagreement非calibratedTV，旧model假设未忽略。 |
| T26-R2323「dataage」 | 旧φ合成经验占比低，但currentφ可systematicwrong，not无bias保证。 |
| T26-C L2326 | 所有限制非globalperformance/safetytheorem。 |
| T27-H L2351「处置/环节/代价」 | 一步model优化从old0到new.4真实性能降低后，分别score/depth/info/policyshift。 |
| T27-R2353「uncertainty罚」 | hatR−λu降不确信regionsscore，u须敏感/可能overconservative阻必要explore，not自动errorbound。 |
| T27-R2354「shortimagination」 | modelerror传播深度少，tailcritic更多/可能漏delay，notshort一直最佳。 |
| T27-R2355「truecalibration」 | newπregions真验证更新φ需extraenvironmentdata，不逆不可逆loss，不假offline也可。 |
| T27-R2356「restrictπshift」 | 单次不快离support，小局部多次可累大变化，oldcoverage非永久。 |
| T27-C L2359 | 罚score/短传播/trueinfo不同作用不相互代替。 |

共13表头、47表行、13表注；每行接受以本地已有定义/机制为限，不冒称外部文献实验或程序已复现。其余T28-T40另续。
