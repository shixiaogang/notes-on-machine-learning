# 真实a9目标与引用核对

目标提交a9cebd3ad6820d90e3f033822cdecd5a3002f547。50个目标文件的blob/SHA存00-input-identity.json，实际读取范围如下；保存50文件不意味着全读50文件。源为根真实33a06c NN10快照，最终r2 SHA在08 JSON。每个非V6目标都在a9文本只找到一次，标签位置和实际标题载于07 JSON（该地址表只定位，不生成接受语义）。

本轮实际目标读取：V2 deep-learning-theory L1–1485全章；convex-learning-and-stability L178–300、355–470、1612–1975；binary-classification L395–500；statistical-learning-framework L1–80、660–800；robustness L1–145。V1 analysis L475–525、829–948；functional-analysis L2460–2528；optimization L375–460、582–855、2410–2508；information-theory/statistical-geometry L2020–2180；action/state L245–355、715–786、1295–1390；graph-structure L40–175、1925–2015；signal-representation L850–920、1255–1730。均从本次git show a9快照实际读取，fbb稿仅作起点，不替真实查证。

37处V2引用逐一核对（X是此前稳定发现/引用身份，CNN源行已迁移，按新07 JSON定位）：

| 引用 | 实际支持及本地范围 |
|---|---|
| X01 | 深度学习章：架构候选与算法选解不同，不能仅凭名称保证泛化；F01a后置引用。 |
| X02 | 鲁棒性章：允许扰动/变化及任务风险规定评价，随机噪声/自然shift/主动搜索分开；F01b后置。 |
| X03 | 深度学习章：复杂度与稳定性连接样本风险，章首只是问题边界不预称定理。 |
| X07 | 两层范数风险定理L177：无bias ReLU、Σ|a|≤A、||w||≤B、iid预固定ABrγ；4ABr/(γ√n)+3sqrt与本地式逐项同。 |
| X08 | 固定有限ReLU的参数/总层/计算单元容量口径，与允许任意宽权重子族分开；F01c补条件。 |
| X09 | 参数大小节L144：spectral乘积是敏感度，泛化另要rowgroup等范数、radius、margin；F02明确V2总层包含线性输出。 |
| X10 | 梯度更新节L713：init/update隐式选解的例子按各自线性/矩阵条件，不泛化每种网络。 |
| X11 | 初始梯度节L410：初始特征是输出对参数的导数φ0及K0，不是隐表示或loss梯度；正文“初始梯度特征”与该对象相容。 |
| X12 | 深度学习章：CNN结构约束与样本风险接口，独立描述后参考。 |
| X15 | 二分类章风险定理L444实际支持一般Z的有界可测损失族；CNN球类固定、单侧Rad对称、Lip收缩、iid按原图n，常数2/3与式同。 |
| X16 | 参数大小节：整层C不是局部Wloc，谱/覆盖及margin才是risk；F01d括号后置，不改变局部norm计算。 |
| X23 | 固定NTK定理L484是半平方PD固定核连续流、残差指数率λmin/n；不是finitewidth theorem，F03拆出init/width/drift额外条件。 |
| X24 | Rademacher风险定理：Transformer采用loss族[0,1]/iid/可测/固定长度及norm条件，无界CE另处理，不借输入敏感度替risk。 |
| X25 | 均匀稳定性与期望风险L410及随后随机扩展L449：loss stability控|E_Sgap|；随机算法再平均独立U，F04a/b改同名同口径，不换E|gap|或high probability。 |
| X26 | framework研究内容L671：任务/目标分布/预测过程须重定，长序列可算位置不自动外推低risk。 |
| X27 | 深度学习章三种参数/梯度/分布分析接口，只作训练条件概述。 |
| X28 | 非凸学习L1802：stationarity与全局objective不同；本地可微内部点，ReLU另非光滑。 |
| X29 | 分解梯度流式L948：U/V改变W动力学，即使预测loss凸；本地二次目标本身是教学例，并未冒充该矩阵式。 |
| X30 | SGD稳定L1615：有放回独立均匀、小步凸Lipschitz smooth固定T；小批量正文随后说有放回的无偏/1b协方差，F12索引多重集保重复。 |
| X37 | 初始参数梯度节：φ0输出parameter derivative，finitewidth移动改变kernel；正文限定起点与轨迹。 |
| X38 | 参数大小节：管理传播尺度后转norm/margin/data风险，未声称初始化方差就是risk。 |
| X39 | 理论比较真实L1428“理论的比较与使用”，F05补精确章/节名称，不沿旧泛称。 |
| X40 | framework：iid样本单位来源，相关窗口不等独立n，本地主体例支持。 |
| X41 | 神经网络学习问题L11：函数族/参数/目标及抽样，不以参数数单独给PAC保证。 |
| X42 | 参数大小节：input/loss/margin/norm同列条件，约束过强与过弱分别指拟合/自由度。 |
| X43 | 梯度更新：同低loss多解、init/order/optimizer选择；“训练敏感性”与固定输入扰动分开。 |
| X44 | 算法稳定L182：替一个样本后的loss变化，种子实验不是形式界，本地说清采样算法条件。 |
| X45 | 参数大小节：绑定是候选限制，norm penalty评价候选；没有把两条路线混成代数等价。 |
| X46 | 参数大小节：norm+input+margin风险，惩罚目标在本地独立写min，λ≥0和L1/L2形式俱全。 |
| X47 | stability：停止/平均/optimizer/noise改变学习算法，验证评价实际候选；不直接保证验证选择。 |
| X48 | gradient update：同一训练行为另有选解偏好，和X47不同理论对象；并列参考不重复定义。 |
| X49 | SGD凸smooth Lipschitz、独立uniform replacement及所需step范围；F06a/d列条件，earlystop本身仍由验证选择。 |
| X50 | 同SGD上界2L²Ση/n先固定T，F06b/c补验证选时刻另入分析；不是直接由Ση推出整个验证程序stability。 |
| X51 | 更新隐式偏差与无偏梯度期望分别定义，线性/矩阵例有各自条件。 |
| X52 | logistic implicitbias：无bias、±1、严格过原点线性可分、mean logistic、固定0<η<n/||X||²足够条件；F07本地精确对象且||w||→∞不是逐步单调，direction→Euclidean margin。 |
| X53 | 参数分布L1109：ρ积分成deterministic neuronmean模型，Q抽整个参数向量产生random predictor；F08明确完整网络Q的期望，不把activationnoise都等同该Q或PACBayes。 |
| X54 | stability：Bagging是bootstrap训练并组合，平均prob和score不同；仅引用替样本损失敏感接口，不声称bagging总更稳。 |

21处V1（原16+CNN真实上游3+新增精确2）逐一核对：

| 引用 | 实际对应及关键约定 |
|---|---|
| X04、X22 | 两处softmax公式指同analysis L907 diag(p)−ppᵀ；FFN K互斥输出与TF有效集合上的Softmax均符合，mask禁止梯度零不把∞作浮点求导。 |
| X05 | chain rule L844行输出列输入、列梯度Jᵀ；Ffn本地解释后括号，不保纯卷名依赖。 |
| X06 | functional L2477真名“单隐藏层的通用逼近”；compact/continuous/nonpoly/bias本地全具备。 |
| X13 | signal L862真名LTI卷积映射；当前根此前已经修真名，此patch不重复原hunk。数学卷积按核线性且边界下平移交换，有限裁剪和互相关下一段分别约定。 |
| 新fast-transforms | signal L1263，数学代数主讲已上移；当前CNN本地同预激活精确算术和采样条件先给，别把截断/浮点误差写成exact。 |
| 新fast-winograd | signal L1514，Bᵀ4×4/G4×3/Aᵀ2×4、4输入→2输出、stride1无dilation实数互相关；CNN通道求和恢复式维数相同，F(2×2,3×3)次数16来自空间变换位置。 |
| 新fast-separable | signal L1647，全非零秩项精确恢复、截断近似；CNN参数通道结构depthwise另对象，且输入边界决定实际成本。 |
| X17 | action/state L257历史输入累计，V1输出Cx[t]+Du[t]先读旧state，CNN之后RNN用已更新h^t读；本地NM014明确保持区间末状态。 |
| X18 | action/state L1300真名“离散化条件下的轨迹求解”，不误称扫描节；ZOH只在区间常值输入精确，A不可逆用积分。 |
| 新affine composition | action/state式L731在并行扫描小节；AQAP后片段在左、有序非交换，固定大小composition工作/深度条件与RNN一致。 |
| X19 | graph L43对象表示，GNN属性/边消息接收下标已本地解释。 |
| 新matrix representations | graph L132邻接行起点列终点；GNN A=Agraphᵀ用于接收sum，零weight边用结构mask，参考后置。 |
| X20 | graph L1930顶点函数谱变换，用组合L主讲；GNN当前是normalized L且d>0、零模sqrt(d)，NM019不把U当V1同一个基。 |
| X21 | analysis L490真名Banach压缩映射，闭非空有限维域完备、selfmap、uniform c<1本地已具备；只保证状态迭代。 |
| X31 | optimization L379梯度下降真名，fullGD线段smooth；网络非smooth另条件。 |
| X32 | optimization L2417近似更新是节而非小节，stoch条件不对每步确定下降；本地full/noisy梯度分开。 |
| X33 | optimization L585动量与加速真名，缓冲未归一化、初零，与NN式相同；不由二次谱速率直接得网络加速。 |
| X34 | optimization L692Newton/Gauss–Newton真名，local quadratic需近点PD LipHessian、unit undamped；NM026补全，不套所有λ/line-search。 |
| X35 | optimization L766拟牛顿真名，逆近似C y=s，PD要yᵀs>0，同NN割线口径。 |
| X36 | information geometry L2123是“基于分布几何的参数更新”小节中的自然梯度段落；固定PX model y期望、共同支持/可积/交换、奇异冗余/λ代价与a9相容。 |

原X14是V6系统的边界说明，目标标签不在本次V1/V2五十文件，未冒称最新版V6协调通过；正文只是说存储/调度/fusion后续展开，未借该引用承担当前算法定义。原纯卷名五句已就地补对象：FFN自动微分行列、RNN状态J行列、RNNscan结合律、GNN接收矩阵、GNN normalized U。无“卷一已经/卷二已经”式讲解。

全部37V2和21V1位置/必要条件已按实际a9读取核对；这不是两卷整体质量验收，也不替代此次最终书页和构建。
