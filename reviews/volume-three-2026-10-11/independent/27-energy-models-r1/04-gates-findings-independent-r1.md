# IND27-r1 七门槛、E1–E12与发现

固定正文SHA f41d0d120284718d27e22447226ea32cf6ece4a7fe9d8b566fe0caa440b2645a，完整606行C→P→W顺序已分别记录。P122、W377全部行政地址具对应手写语义依据；36显示数学、2表所有格、1算法全部步骤、全部图/表注在03-W记录。行政地址扫描只查漏号，不生成语义通过理由。

## 七门槛实际执行

|门槛|位置、动作与结论|
|---|---|
|G1可检验命题|U010有限离散/连续尾部、U023有限内点MLE、U026Q正定、U044finiteθ不可约非周期、U052神经尾部、U077固定特征完整标签凹性、U101有限候选精确性分别展开成对象+条件+性质。限定不是“模型好/算法稳定”等无判据说法。U044明确长期分布而非smallk样本保证，U031明确R^d排除PSD替代支持。|
|G2压缩表达拆解|外场/耦合/精度/自由能/softmax得分、模板共享/grounding成本、同图/新图评价均有解释。U117同集平均每序列NLL越小越好，point/wholeerror不互换，未给无基准“接近/更好”；U090两decoding准则逐点0/1loss vs jointprob明确。|
|G3新对象转换|U007joint→givenx标签，U020±1→Kclasses，U025离散→continuous，U032observed→latent0/1，U041complete→partialobs，U093point→span，U102span→point higherorder，U105chain→generalrelation，U111samegraph→newgraph。各处为何变、fixedinput/unknowns、所继承Z与不继承算法条件在本地恢复。|
|G4解释时序|U003权重任务→势→−log→Z，U037hidden sum→freeenergy而非最佳hidden；U085明确重三点是新增input改变prob，U100新一类三点是boundaryuncertainty，非迟到重复铺垫。U034删组内边解决hiddenpost缺口，U058导数/边界条件先于scoreobjective。|
|G5局部入口|C/P的逐入口记录已列L11、66、120、169、269、313、357、362、395、490、540、563，均有整排状态、二值/连续检测、未测共同源、函数形状、组规则、输入标签、相邻标签、区间形状或非链关系。NCE先给免modelchain+knownnoise，Langevin先给无解析块+continuousinputgradient，未只抛抽象评价句。|
|G6公式双门槛|36式逐一核用途、符号、候选、sum/max/expectation缘由。唯一未满足项IND27-F01在U063.S03：countdefinedallC，但message只countothernodes后用g(k)，缺target状态导致wrongmessage。O(r²)claim仍是卷积cost，不需要改展示式或复杂度。其它α/β/Viterbi/span/likelihood运算集合及方向可从邻正文还原。|
|G7回指与范围|U002/U010先述separator/positivity再外引；U023先述梯度再引参数学习；U084sum分配律和U108width先本地述后引用，U121dynamicstates/observation先本地解释后章引。jointpairwise→marginalhigherorder有sumz机制；fixedfinitehistory不能任意distantY scope；conditionalinputmissing和newedgegeneration未继承未定义density。无用“卷二已说明”代当地任务。|

## 人工反馈校准E1–E12

|校准项|触发检查对象与实际判断|
|---|---|
|E1比较口径|U117.S02明确sameholdout、meanpersequenceNLL、lowerbetter；U111.S01–02明确singlegraphtransductive与newindependentgraphs。核训练/调参未使用数据条件和point/wholemetric，不存在未给数据单位的“留出接近”。|
|E2关系两端|U050形状/作用域与独立性质、U063localfactor vs globalcycles、U064parametercount vs groundedsize、U110wrongedgeprefer vs collectivebias都展开两端及作用机制。U110同label奖励而实际异类的例可判断后果，非只“相关子类型”。|
|E3要求承载对象|U008 everyusedx正有限Z是概率存在要求，U052r下界及positivesupport、U071hardrulesZ0、U111testY不可入trainfeature都明确承载prob/energy/support/dataflow；未出现无对象的“要求可落在频率含义”。|
|E4多重否定|检查U056.S02、U059.S04、U120.S01等否定表述：均单层“不保证/不表示/不意味着”，能直接复述“短链gradient可偏、训练未算Z不会给其值、fixedx的Y仍可相关”。无“不一定仍不可减少”等嵌套反转；必要限制与已有计算任务相连。|
|E5候选集合|U003Efamily、U050local/global、U094partitioncandidate、U102history states、U105generalgraph、新query候选均说明旧对象缺口与新的允许集。有限数据multi-model分歧是本章未讨论对象，不凭外部知识要求新风险模型族。|
|E6重复例子|U016三点joint说明unconnectedmarginalcorrelation；U028三continuous说明Q vs Σ和补全；U085明确input影响labeltask；U100三positiononeclass说明boundaryuncertainty。不同新增问题明示，无只迟到铺垫的泛泛再对照。|
|E7抽象回指|U002无向separator、U022半因子、U084sum分配律、U090latentMAP、U120三个analysis、U121dynamic生成均恢复所需命题而后ref。读者无需找前章“几个问题”自行拼出要求。|
|E8抽象节首|P逐新节核localentry；“共同异常未测”在BM、“更复杂非线性”在neural、“恰一激活/规则”在higherorder、“区间长度/形状”在semiMarkov、“二维/设备”在generalgraph先于name。U053不是新节首，softmax同shift反例当地承接已定义条件归一化。|
|E9最不利允许集|本章未定义鲁棒扰动/最坏环境，无“最不利变化”无集合触发。相关max为Viterbi/最佳分段，候选label1:K、合法partitions及最大score方向都已给，不把它们冒称worstcase risk。|
|E10范围扩大|fullx→missingx需p(x)；pairwisejoint→visiblehigherorder用hiddenelim；finitewindow→generallabelgraph需width；finiteD→newD需groundcounts/边缘一致性重查。各处说明旧结论能/不能继承什么。F01是count输出状态漏项，非宏观范围转换失败。|
|E11新符号与目标|θ/μ/C、Q/Σ、x/z/u、r/α/C、pN/ν/c、p*/Δ、nr/I、α/β、spanA/B均先给任务或紧邻解释；单个M020C1条件只定义update不构成精确抽样保证。F01的新countmessage需要target状态值才能定义正确可计算量，列G6必须修。|
|E12指标方向/基线|U040covdiff1/169明确5/13 vs(8/13)^2，U088ηgrad empirical2−modelexpected1.56，U090pointloss vs wholeprob，U117NLLlower/不同errorunit均有方向/基准。无未说明“下降幅度”的实际实证claim；trainlossdrop不保证holdout明确不作泛化证明。|

## 稳定发现IND27-F01

- 原版：f41d0d120284718d27e22447226ea32cf6ece4a7fe9d8b566fe0caa440b2645a，L322，U063.S03。
- 短引：“汇总其余节点恰有k个激活的权重，再乘e^{-g(k)}求和”。
- 根因：k是target以外count，g在U060定义为全C的countenergy。targetxi=+1还需+1；漏偏移可让两个输出消息错误使用同一势值。
- 代数证据：设c_k为others恰k激活的incomingproductweight，则m_(C→i)(xi)=Σ_(k=0)^(r−1)c_k exp[−g(k+1{xi=+1})]。xi=−1乘e^{-g(k)}，xi=+1乘e^{-g(k+1)}。三节点恰一active势、其余incoming全1时，target−1 message=2+2e^{-λ}，target+1 message=1+3e^{-λ}，λ>0一般不同；原句无法说明差别。
- 级别：必须修正的计算条件/阅读障碍，非可选文风。
- 最小动作：仅将“再乘e^{-g(k)}求和”改为按target未激活/激活分别乘e^{-g(k)}或e^{-g(k+1)}再求和。卷积O(r²)、其它公式和模型结构保持。
- r1状态：待修改/独立复读。父代理已认可并另行修主源；本记录只绑定旧冻结f41，不倒算其已通过。

## 本版结论与记录范围

独立C/P/W语义记录完整，无脚本自动生成统一接受；正文f41本版结论为待修改（仅IND27-F01），不是通过。尚未核对作者原r1/r3/r4审查记录，下一步在独立正文判断完成后核对版本与闭环，并对新稿该处连续复读。外部引用、图资产及PDF版面不在本轮认证范围。
