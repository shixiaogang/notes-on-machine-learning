# 第8章概念审读清单（独立读者B，第一轮）

## 版本与覆盖

- 源文件：`tex/01-mathematical-preliminaries/03-random-variables-distributions-and-causality/01-random-variables.tex`。
- 冻结 SHA-256：`6f509824dd918d56cf5319cc9404b26e5d1d992deed3a80a9e2d938a39dd9c17`，开始审读、读至1440、3350行及全章读完后的实际校验均一致；3350行和全章完成检查点也重核了第7、9–11章，均未变。
- 全章5715行、187511源字符已逐段完整顺读。读取块为1–240、241–480、481–715、716–960、961–1200、1201–1440、1431–1670（重叠接续定义）、1671–1910、1911–2150、2151–2390、2391–2630、2631–2870、2871–3110、3111–3350、3328–3570（重叠接续算例）、3571–3810、3811–4050、4051–4290、4291–4530、4531–4770、4771–5010、5011–5250、5251–5490、5491–5715。包含全部证明、算例、图注、表及独立本章小结，无未读行。概念表共747项；第7–11章整组首轮状态见`reader-b.md`。
- 各表节标签和上述源路径共同适用于每一行；位置是实际源行号，短引文供后续定位。基础概率概念仍逐项记为已回顾，纯预告不当作已建立。
- 读者背景与审读边界同`reader-b.md`；图只按当前说明核对支撑，不宣称完成PDF视觉检查。

## 已核对的边界依赖

以下范围均已实际展开；路径以`tex/01-mathematical-preliminaries/`为前缀。

| 前章文件 | 实读范围 | 用途与核对结果 |
| --- | --- | --- |
| `01-mathematical-language-combinatorics-analysis-optimization/03-mathematical-analysis.tex` | 130–240、1418–1585、1590–1730、1730–1855、2470–2511 | σ代数、Borel、测度连续性、可测函数、简单逼近、单调收敛完整证明、积分线性及有符号可积性、σ有限、乘积测度、Tonelli/Fubini的准确声明与证明边界、换元条件及极坐标、积分下求导条件与证明。支持本章前部测度证明，不凭章节名补条件。 |
| `01-mathematical-language-combinatorics-analysis-optimization/05-functional-analysis-and-approximation.tex` | 251–301、486–607、1253–1340、1684–1699、1736–1744 | 稠密、完备化及可分定义；Hilbert闭凸投影完整证明及闭性的必要性、有界线性泛函、Riesz表示完整主要论证与范数等式、σ有限的再次定义；支持RN和条件期望投影。 |
| `01-mathematical-language-combinatorics-analysis-optimization/04-optimization.tex` | 199–250 | 凸函数一二阶判据证明、有限Jensen归纳证明；没有一般条件Jensen，见B-013。 |
| `02-linear-algebra-and-geometry/01-linear-algebra-and-matrix-analysis.tex` | 1116–1199 | Schur补、块消元、逆与正定判据；条件高斯回指可用。后段Woodbury是同块读取，不作为本章当前依赖。 |
| `01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex` | 19–134、371–531 | 前一范围为节标签定位并实读；后一范围完整核对限制类、打散、VC维、生长函数、阈值／区间例、Sauer–Shelah证明及“计数不直接给概率”的边界。 |
| `01-mathematical-language-combinatorics-analysis-optimization/05-functional-analysis-and-approximation.tex` | 973–1118 | 覆盖数、度量熵、伪距离、全有界与稠密量词、样本覆盖及九格心图。与本章随机Lipschitz误差传递对接。1118为后续和／复合证明跨块行，本次不以该未读完的证明作依据。 |
| `01-mathematical-language-combinatorics-analysis-optimization/03-mathematical-analysis.tex` | 682–756、2350–2463 | Lipschitz／一致连续与平方根例、度量紧致及闭有界的有限维边界；Fatou、支配收敛及完整证明、尖峰反例、交换条件表。前文未定义Hölder连续或Arzelà–Ascoli。 |
| `01-mathematical-language-combinatorics-analysis-optimization/04-optimization.tex` | 139–178 | 下半连续的序列定义、下水平集判据及其极限用途。该定义可直接用度量收敛推广，本章Portmanteau回用可理解。 |
| `01-mathematical-language-combinatorics-analysis-optimization/03-mathematical-analysis.tex` | 885–949 | 复合梯度例及softmax的动机、定义、Jacobian完整核对；温度缩放可复用此处实值评分转概率。949行后的矩阵微分未作为本次补读依据。 |
| `01-mathematical-language-combinatorics-analysis-optimization/04-optimization.tex` | 979–1016 | 凸次梯度／次微分、绝对值例及零在次微分中等价最优的证明；支持分位损失最优条件。 |
| `02-linear-algebra-and-geometry/01-linear-algebra-and-matrix-analysis.tex` | 892–954 | 正规方程、满列秩唯一解、加权版本及半正定权重边界均已展开；支持局部线性拟合与Gauss–Markov。948–954的后续算例只读开头，不据此声称例子完整核对。 |
| `01-mathematical-language-combinatorics-analysis-optimization/03-mathematical-analysis.tex` | 1116–1205 | 一元Taylor、二阶多元展开及Peano余项、局部Hessian正定推出二次下界，包含中间算例与图注；支持密度平滑和Laplace局部控制。 |
| `02-linear-algebra-and-geometry/01-linear-algebra-and-matrix-analysis.tex` | 1640–1668 | 1647起的正半定平方根定义、唯一性证明及正定实幂／逆平方根完整核对，支持Laplace白化换元；1640–1645只是前段级数论证的接续，不据此声称前段完整证明已补读。 |

另实际展开第3章283–327行及第6章2310–2364行作定位核查；这些范围不是本章新增论证的依据，不以其标题冒充相关证明。前1–7章未检索到概率特征函数唯一性、对数正态、协方差白化的定义。

## 概率空间与读数

节标签：`sec:probability-spaces-random-variables`，上层`sec:rv-definition`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-001 随机变量／取值／分布的层次 | 9预告，“可测映射…一次取值…概率”；`chap:random-variables` | 开篇区分规则、实现与规律。 | 78–93四状态表与`fig:rv-objects` | 纯预告后逐项建立；不把观测等同变量。 | 已清楚；无。 |
| B08-002 样本空间Ω与基础结果ω | 19、26–27，“所有可能结果”；`sec:probability-spaces-random-variables` | 给概率及读数一个共同底层。 | 有限权重表、a/b/c/d设备状态 | 已回顾；ω不是数值读数。 | 已清楚；无。 |
| B08-003 事件与事件族F | 20、27，“事件组成的σ代数”；`sec:probability-spaces-random-variables` | 指明可询问的集合，改变F会改变问题。 | 事件{X=9}={a,b} | 已回顾；不是所有任意子集自动可测。 | 已清楚；无。 |
| B08-004 概率空间 | 24–31，“三元组”；`sec:probability-spaces-random-variables` | 把有限概率推广到一般空间；总测度1。 | `def:probability-space` | 第3章测度已核对；空间不是单独的P。 | 已清楚；无。 |
| B08-005 可数可加性 | 28–30，“两两不交”；`sec:probability-spaces-random-variables` | 保证拆分概率相容。 | 可数并公式、后续递增证明 | 已回顾测度性质；与非互斥联合界不同。 | 已清楚；无。 |
| B08-006 补事件概率 | 34–36，“1-P(A)”；`sec:probability-spaces-random-variables` | 从全集质量计算余下概率。 | 显式等式 | 已回顾；来自不交分割。 | 已清楚；无。 |
| B08-007 概率单调性 | 34–36，“A⊆B”；`sec:probability-spaces-random-variables` | 事件扩大不能降低质量。 | 显式蕴含 | 已回顾；不是数列单调性。 | 已清楚；无。 |
| B08-008 概率递增连续性 | 37–44，“A_n↑A”；`sec:probability-spaces-random-variables` | 允许事件极限换到概率极限。 | 不交B_n分解完整论证 | 第3章同结论已核对。 | 已清楚；无。 |
| B08-009 概率递减连续性 | 45–47，“起始集合具有有限测度”；`sec:probability-spaces-random-variables` | 处理缩小事件，强调一般测度边界。 | 补事件证明 | 概率自动有限，一般测度并非如此。 | 已清楚；无。 |
| B08-010 联合界 | 49–55，“即使事件不互斥”；`sec:probability-spaces-random-variables` | 同时控制多个坏事件。 | `eq:probability-union-bound` | 与可加等式区别明确；后用途为预告。 | 已回顾且清楚；无。 |
| B08-011 随机变量的可测映射定义 | 58–69，“X⁻¹(B)∈F”；`sec:probability-spaces-random-variables` | 保证值域条件确实有概率。 | `def:probability-random-variable`、四状态表 | 第3章可测函数已核对；不是随意变化的符号。 | 已清楚；无。 |
| B08-012 实随机变量的阈值判据 | 65–68，“X(ω)≤x”；`sec:probability-spaces-random-variables` | 把全部Borel集合检查缩成半直线。 | 前章1439–1467生成族解释 | 已回顾；原像不要求逆函数。 | 已清楚；无。 |
| B08-013 随机向量 | 71–76，“等价于各坐标可测”；`sec:probability-spaces-random-variables` | 同时描述多个读数。 | `def:rv-random-vector`、(X,Y)表 | 已回顾；可测不含独立。 | 已清楚；无。 |
| B08-014 一般随机对象 | 75，“换成指定的可测空间”；`sec:probability-spaces-random-variables` | 为非数值对象保留接口。 | 取值空间替换的明确规则；无专例 | 对前一定义的直接扩展，非新概率公理。 | 已清楚；无。 |
| B08-015 重复实验的联合规则 | 87，“不自动意味着独立抽样”；`sec:probability-spaces-random-variables` | 防止同规则被误认同结果或独立。 | 四状态规则的文字比较 | 联合与独立的正式建立在后文；此处边界提醒。 | 预告清楚；无。 |

## 分布与参考测度

节标签：`sec:rv-distribution`／`sec:probability-radon-nikodym-change-measure`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-016 分布／推送概率P_X | 100–102，“诱导的概率测度”；`sec:rv-distribution` | 不保留底层状态，只记录值域概率。 | P_X(B)=P(X∈B)、`fig:rv-objects` | 映射与测度不同；后续期望公式给推送证明。 | 已清楚；无。 |
| B08-017 分布函数F_X | 103–105，“P(X≤x)”；`sec:rv-distribution` | 用阈值概率编码实分布。 | 单调、右连续、两端极限；密度CDF图 | 已回顾；逆向存在结论仅声明，基础背景可接。 | 已清楚；无。 |
| B08-018 概率质量函数 | 107，“集中在可数点集”；`sec:rv-distribution` | 离散规律可列单点权重。 | p_X(x)=P(X=x)、四状态变权重 | 不是密度高度；计数测度参照。 | 已回顾且清楚；无。 |
| B08-019 概率密度 | 107–114，“相对于Lebesgue测度”；`sec:rv-distribution` | 连续情形通过积分求概率。 | 高度4、宽0.05、概率0.2 | 已回顾；单点概率为0不表示密度为0。 | 已清楚；无。 |
| B08-020 密度的几乎处处确定性 | 110–111，“不能在任意指定点”；`sec:rv-distribution` | 限制密度局部极限解释。 | 连续点的小区间比值说明 | 第3章a.e.已核对；分布不依赖零集修改。 | 已清楚；无。 |
| B08-021 均匀分布 | 112–121，“[0,1/4]上均匀”；`sec:rv-distribution` | 给面积与CDF增量的可算实例。 | `fig:probability-density-cdf` | 已回顾；密度大于1合法。 | 已清楚；无。 |
| B08-022 下q分位数／广义逆 | 125–129，“inf{y:F(y)≥q}”；`sec:rv-distribution` | 从概率水平反求阈值，0<q<1。 | 显式定义 | 不是必须可逆的普通逆函数。 | 已清楚；可选用离散例代入。 |
| B08-023 分位数集合Q_q | 129–134，“F(a⁻)≤q≤F(a)”；`sec:rv-distribution` | 区分广义逆选代表与可能多个最优阈值。 | 平坦区间解释 | 下分位数是集合下端；不同于所有q都唯一。 | 已清楚；无。 |
| B08-024 参考测度 | 138–144，“密度的数值不能脱离”；`sec:rv-distribution` | 统一质量函数与连续密度。 | 计数／Lebesgue对照 | 同映射改底层概率会改分布；两种变化不可混淆。 | 已清楚；无。 |
| B08-025 测度绝对连续ν≪μ | 146–160，“零集也是…零集”；`sec:rv-distribution` | 排除参考样本永远看不到的目标质量。 | 有限q_j/p_j失效例、`def:probability-absolute-continuity` | 与ν≤μ、比值有界、函数连续明确不同。 | 已清楚；无。 |
| B08-026 密度比／分块权重r | 163–169，“ν(A_j)/μ(A_j)”；`sec:rv-distribution` | 在有限分割上构造新测度的积分权重。 | 逐块相加，零质量块取0 | 只保证分块生成事件，不夸大全F。 | 已清楚；无。 |
| B08-027 有限换测度公式 | 170–176，“∫g dν=∫gr dμ”；`sec:rv-distribution` | 同函数改权重，不必重新抽目标分布。 | `eq:probability-finite-change-measure` | 当地g分块常数且测度有限；一般化待后。 | 已清楚；无。 |
| B08-028 σ有限 | 182，“σ有限测度”；`sec:rv-distribution` | 为全空间拼接有限构造设条件。 | 第3章1702–1713及本章242 | 已回顾可数有限测度覆盖；不是每点质量有限。 | 已清楚；无。 |
| B08-029 Radon–Nikodym导数 | 180–190，“非负可测函数r”；`sec:rv-distribution` | 在无预给分割时仍表示ν。 | `thm:probability-radon-nikodym`完整证明 | 只在μ-a.e.唯一；并非通常微分的逐点导数。 | 已清楚；无。 |
| B08-030 共同支配测度λ=μ+ν | 193–205，“ν≤λ”；`sec:rv-distribution` | RN证明先把两测度放在同一L²中。 | Cauchy–Schwarz有界估计 | 已核对第5章有界泛函条件；不是假定r已存在。 | 已清楚；无。 |
| B08-031 Riesz表示的测度应用 | 206–216，“存在g∈L²(λ)”；`sec:rv-distribution` | 把积分泛函变成函数后辨认非负权重。 | 测试指示函数推出0≤g≤1 | 第5章1253–1340实读；与有限矩阵表示不同。 | 已清楚；无。 |
| B08-032 排除g=1及r=g/(1-g) | 218–231，“绝对连续性…排除”；`sec:rv-distribution` | 防止除零承载正质量。 | μ(C)=ν(C)=λ(C)=0，积分代换 | 绝对连续用处明确，不声称逐点界。 | 已清楚；无。 |
| B08-033 密度a.e.唯一的测试集证明 | 234–240，“A_k={r₁≥r₂+1/k}”；`sec:rv-distribution` | 将两密度不同变成正质量矛盾。 | 完整积分不等式及交换 | 可数并零集；有限情形先证明再分块。 | 已清楚；无。 |
| B08-034 σ有限拼接 | 242–247，“覆盖并求交…互不相交”；`sec:rv-distribution` | 从有限测度扩展到一般σ有限。 | 分块构造、单调收敛 | 前章MCT实际核对；并非无限量直接相减。 | 已清楚；无。 |

## 整体摘要与变换函数

节标签：`sec:rv-features`／`sec:probability-expectation-conditional-expectation`／`sec:probability-moment-transforms`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-035 期望 | 255–260，“∫X dP”；`sec:rv-features` | 概率加权整体平均。 | 正负部分定义、带噪信号例 | 已回顾；非负允许∞，可积实值不允许∞-∞。 | 已清楚；无。 |
| B08-036 随机变量可积性 | 258–260，“E\|X\|<∞”；`sec:rv-features` | 使有符号平均有限。 | 第3章1643–1669 | 已回顾；可测不保证可积。 | 已清楚；无。 |
| B08-037 无须先求变换分布的期望公式 | 262–273，“E[g(X)]”；`sec:rv-features` | 直接由X分布计算函数平均；非负或可积。 | `eq:probability-lotus`及简单函数/MCT证明 | 推送测度已建；不要求密度。 | 已清楚；无。 |
| B08-038 零均值加性观测模型 | 275–282，“Y=θ+ε”；`sec:rv-features` | 将未知信号设为平均目标。 | `ex:probability-noisy-observation` | 一次接近、平均收敛、独立性均不随之保证。 | 已清楚；无。 |
| B08-039 均值μ_X | 284，“E[X]”；`sec:rv-features` | 为中心化固定位置。 | 带噪信号平均 | 已回顾；非单次读数。 | 已清楚；无。 |
| B08-040 方差 | 284–286，“E[(X-μ_X)²]”；`sec:rv-features` | 测量平均周围波动，要求二阶矩有限。 | 二阶矩减均值平方 | 已回顾；不同于平均误差的概率界。 | 已清楚；无。 |
| B08-041 原点矩 | 291，“E[X^k]”；`sec:rv-features` | 以更高阶摘要保留额外信息。 | 绝对k阶可积条件 | 与中心矩区别由平移位置给出。 | 已回顾且清楚；无。 |
| B08-042 中心矩 | 291–292，“E[(X-EX)^k]”；`sec:rv-features` | 观察围绕均值的高阶波动。 | 三阶不对称、四阶尾部解释 | 有限低阶矩不能唯一确定分布。 | 已清楚；无。 |
| B08-043 偏斜、峰度 | 289–292，“不对称性…尾部与峰度”；`sec:rv-features` | 提示三四阶摘要用途。 | 无标准化公式；此处仅定性说明 | 已回顾定性直觉；未声称三四阶矩就是标准化系数。 | 可理解；可选补标准化以防尺度混淆，不列实质问题。 |
| B08-044 矩母函数M_X | 294–302，“E[e^{tX}]”；`sec:rv-features` | 把一列矩组织成函数；需零点双侧邻域有限。 | `def:probability-moment-generating-functions`、导数式 | 矩存在不推出MGF存在。 | 已清楚；反例入口见B-011。 |
| B08-045 累积量生成函数K_X | 298–323，“log M_X”；`sec:rv-features` | 用对数组织摘要，后为独立和服务。 | K′(0)=EX、K″(0)=Var X完整计算 | 不是未取log的MGF导数；可加性是预告。 | 已清楚；无。 |
| B08-046 对数正态反例 | 301–302，“拥有所有…矩…却…”；`sec:rv-features` | 证明矩存在比MGF存在弱。 | 无构造、密度或尾部算式 | 前1–7章及此前未定义该分布。 | 局部费力；B-011，给X=e^Z及两种积分比较。 |
| B08-047 联合累积量 | 303–306，“混合偏导数”；`sec:rv-features` | 推广到随机向量的共同波动摘要。 | K_X(t)=log E exp(tᵀX) | 一元导数的多元推广；未规定阶数组合，可由混合阶数读出。 | 已清楚；可选显式κ_α=∂^αK(0)。 |
| B08-048 积分下求导的指数支配 | 309–315，“更小邻域…端点…控制”；`sec:rv-features` | 使形式求导合法。 | 第3章2470–2511条件与证明 | 邻域有限性强于单点有限；非任意交换。 | 已清楚；可选给多项式乘指数的常数界。 |
| B08-049 特征函数 | 324–330，“E e^{itX}”；`sec:rv-features` | MGF可发散时仍有全实参数变换。 | `def:probability-characteristic-function`、模恒1 | 复期望按实虚部；不同于指数放大。 | 已清楚；独立和及极限仅预告。 |

## 常见分布

节标签：`sec:probability-common-distributions`／`sec:probability-families-transformations`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-050 取值空间与建模假设 | 335，“相容仍不代表模型正确”；`sec:probability-common-distributions` | 将数值类型与概率形状分开。 | 成功标记、次数、时间、比例对照 | 不把非负整数自动当Poisson。 | 已清楚；无。 |
| B08-051 Bernoulli分布 | 339–342，“一次二元结果”；`sec:probability-common-distributions` | 建模0/1，p∈[0,1]。 | 质量式、均值方差 | 已回顾；独热类别的二元特例。 | 已清楚；无。 |
| B08-052 二项分布 | 342–346，“n个独立同分布…之和”；`sec:probability-common-distributions` | 固定次数中的成功数。 | 组合数质量式及矩 | 已回顾；独立同分布条件明确，不等同任意计数。 | 已清楚；无。 |
| B08-053 独立同分布 | 342首次使用，“n个独立同分布”；`sec:probability-common-distributions` | 保证和的指定分布。 | 基础概率背景；正式定义在后节 | 已回顾而非新研究生概念；记录其提前使用。 | 可跟上；无。 |
| B08-054 多项分布 | 348–351，“整组计数”；`sec:probability-common-distributions` | 推广到K类固定次数抽取。 | 质量式、均值、协方差 | 已回顾；总计数固定导致负相关，非独立坐标。 | 已清楚；无。 |
| B08-055 协方差（首次回用） | 351，“Cov(N_j,N_k)”；`sec:probability-common-distributions` | 摘要共同计数变化。 | 多项显式公式，正式定义591行 | 本科背景已学，仍登记提前回用。 | 已回顾；定义与直觉后节补全。 |
| B08-056 Poisson分布 | 353–356，“固定窗口中的稀疏计数”；`sec:probability-common-distributions` | 无固定最大次数的计数模型。 | 质量式，均值=方差=λ | 已回顾；与二项上界不同，过程假设以后建立。 | 已清楚；无。 |
| B08-057 类别分布 | 358–360，“编号只是标记”；`sec:probability-common-distributions` | 一次K类选择，避免赋予编号均值意义。 | P(C=k)=p_k | 与多项整组计数不同。 | 已清楚；无。 |
| B08-058 独热向量e_C | 359–360，“均值就是概率向量”；`sec:probability-common-distributions` | 将类别标记变为可平均的坐标指示。 | E e_C=p | 本科线代标准基已知；当地未显式展开但含义明确。 | 已回顾；可选说明仅第C项为1。 |
| B08-059 指数分布 | 365–369，“速率λ…等待时间”；`sec:probability-common-distributions` | 建模非负等待。 | 密度、均值、方差 | 已回顾；速率是时间倒数。 | 已清楚；无。 |
| B08-060 无记忆性 | 369–372，“已经等待…不改变剩余”；`sec:probability-common-distributions` | 表达特定等待规律。 | 条件尾概率恒等式 | 已回顾条件概率；不意味着不同等待自动独立。 | 已清楚；无。 |
| B08-061 一维高斯分布 | 374–378，“也称正态”；`sec:probability-common-distributions` | 无约束实读数模型。 | 密度、矩、仿射变换式 | 已回顾；σ²>0。 | 已清楚；无。 |
| B08-062 退化高斯／点质量 | 378，“集中于b”；`sec:probability-common-distributions` | 处理仿射缩放a=0边界。 | 常量结果与无密度说明 | 不得使用正方差密度。 | 已清楚；无。 |
| B08-063 Gamma函数 | 380–393，“归一化…积分常数”；`sec:probability-common-distributions` | 为正变量幂乘指数形状归一化。 | `eq:probability-gamma-function`、分部积分、换元 | 阶乘向正实参数延拓；不是Gamma分布本身。 | 已清楚；无。 |
| B08-064 Gamma分布 | 395–399，“形状…速率”；`sec:probability-common-distributions` | 建模不同形状非负量。 | 密度、矩、指数特例 | 速率b与尺度1/b区别明确。 | 已清楚；无。 |
| B08-065 比例与总量变换(R,S) | 401–412，“U=RS、V=(1-R)S”；`sec:probability-common-distributions` | 从正量构造随机比例。 | Jacobian=s、联合密度计算 | 前章换元已核对；Gamma共同速率与独立不可省。 | 已清楚；无。 |
| B08-066 Beta分布 | 401–426，“[0,1]上的随机比例”；`sec:probability-common-distributions` | 为概率／占比指定连续分布。 | 密度、矩、Gamma比值推导 | 非任意比值都是Beta，速率不同不直接成立。 | 已清楚；无。 |
| B08-067 归一化Gamma向量 | 428–433，“G_k/ΣG_j”；`sec:probability-common-distributions` | 从两个比例推广至K类组成。 | 自由K-1坐标、Jacobian=s^(K-1) | 与直接独立比例不同；总和约束。 | 已清楚；无。 |
| B08-068 概率单纯形 | 436–447，“p_k>0、Σp_k=1”；`sec:probability-common-distributions` | 描述组成向量的实际自由度。 | 支持域及自由坐标说明 | 第7章单纯形已读；非K维满维区域。 | 已回顾且清楚；无。 |
| B08-069 Dirichlet分布 | 434–458，“相对于dp₁…dp_(K-1)”；`sec:probability-common-distributions` | 多类比例模型，α_k>0。 | `def:probability-dirichlet-distribution`、矩 | 不存在K维Lebesgue密度；K=1点质量另约定。 | 已清楚；无。 |
| B08-070 Dirichlet总参数α₀与集中程度 | 431、458–461，“参数总量增大…更集中”；`sec:probability-common-distributions` | 区分均值位置和波动强度。 | Beta(8,2)与(80,20)数值比较 | 不是实际样本频数；统计更新后讲。 | 已清楚；无。 |
| B08-071 单纯形上的负协方差 | 448–458，“各坐标之和固定”；`sec:probability-common-distributions` | 说明比例不能独立涨落。 | Var、Cov显式式 | 已回顾协方差；约束并不等于各坐标都负相关的一般定理，此处限定Dirichlet。 | 已清楚；无。 |
| B08-072 多元高斯密度 | 463–476，“协方差…正定”；`sec:probability-common-distributions` | 无约束向量分布的模型表达。 | 二次型与det归一化 | 基础线代正定已知；正式联合高斯判据后给。 | 已回顾且清楚；无。 |
| B08-073 奇异高斯的支持子空间 | 477–479，“集中在低维仿射子空间”；`sec:probability-common-distributions` | 区分分布存在与满维密度存在。 | (Z,Z)位于直线 | 与单个边缘有密度并不矛盾。 | 已清楚；无。 |
| B08-074 卡方分布 | 481–491，“独立标准高斯平方…和”；`sec:probability-common-distributions` | 为平方误差与后续统计量提供分布。 | `def:probability-chi-square-distribution` | 已回顾；Gamma(k/2,1/2)用速率。 | 已清楚；无。 |
| B08-075 卡方自由度 | 487–491，“k为正整数”；`sec:probability-common-distributions` | 计数独立平方方向。 | k项平方及均值k、方差2k | 不是任意高斯协方差秩的默认替代。 | 已回顾；无。 |

## 指数族表示

节标签：仍为`sec:probability-common-distributions`，子标题“参数化分布的指数族表示”。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-076 指数族 | 495–515，“参数依赖…少量摘要”；`sec:probability-common-distributions` | 复用均值、协方差、似然计算；固定σ有限μ、h、T。 | `eq:probability-exponential-family`、Poisson/Bernoulli/高斯例 | 不等同指数分布；参考测度可以离散或连续。 | 已清楚；无。 |
| B08-077 自然参数η | 508、513，“索引的分布”；`sec:probability-common-distributions` | 把参数与摘要的作用写成线性内积。 | log λ、logit p、μ/σ² | 不一定等同原参数；端点不一定有有限η。 | 基本清楚；Bernoulli例应加0<p<1，局部边界提醒。 |
| B08-078 充分统计量T(x) | 508–510，“与参数…有关的部分只通过摘要”；`sec:probability-common-distributions` | 暂以因子形式解释参数信息压缩。 | T(x)=x、样本ΣT(x_i) | 正式统计充分性明确后置，不冒充完整定义。 | 预告带白话，清楚；无。 |
| B08-079 基准项h(x) | 498、508，“非负可测基准项”；`sec:probability-common-distributions` | 收纳不随参数变化的密度因素。 | Poisson 1/x!、高斯指数项 | 固定μ和h决定可用表达，不能随η改变。 | 已清楚；无。 |
| B08-080 对数配分函数A(η) | 510–513，“负责归一化”；`sec:probability-common-distributions` | 总质量须为1。 | log积分及三种显式A | 与MGF、未取log归一化常数分别处理。 | 已清楚；无。 |
| B08-081 自然参数空间 | 513，“严格为正且有限”；`sec:probability-common-distributions` | 排除不可归一化参数。 | 明示可用集合可以是其子集 | 内部点为后续求导条件，不自动遍及边界。 | 已清楚；无。 |
| B08-082 A梯度给摘要均值 | 517–528，“E_η[T(X)]”；`sec:probability-common-distributions` | 用一次求导统一计算。 | 分子分母完整式、Poisson/Bernoulli核对 | 积分下求导需可积控制，前章已核对。 | 已清楚；无。 |
| B08-083 A Hessian给摘要协方差 | 529–558，“Cov_η(T(X))”；`sec:probability-common-distributions` | 二阶导同时给波动及凸性。 | `eq:probability-log-partition-hessian`及标量核对 | 协方差基础回用；严谨向量定义后节。 | 已清楚；无。 |
| B08-084 A凸但未必严格凸 | 536，“Hessian…可能奇异”；`sec:probability-common-distributions` | 防止把可归一化当可识别／强凸。 | 统计量方向冗余说明 | 二阶凸判据基础已知；后文统计可识别性非此处已建。 | 已清楚；无。 |

## 联合关系

节标签：`sec:rv-joint`／`sec:probability-joint-marginal-conditional`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-085 联合分布 | 568，“乘积空间上诱导”；`sec:rv-joint` | 两台设备平均需知道共同变化。 | `fig:rv-dependence`、三张质量表 | 不是边缘分布的简单罗列。 | 已回顾且清楚；无。 |
| B08-086 联合质量／联合密度 | 569–573，“完整表格”；`sec:rv-joint` | 给联合测度具体计算表示。 | 二元求和与积分 | 已回顾；无密度时仍有联合测度。 | 已清楚；无。 |
| B08-087 边缘分布与边缘化 | 569–588，“投影的推送”；`sec:rv-joint` | 消去不关心的坐标。 | π_X及Tonelli推出密度公式 | 前章Tonelli实际核对；边缘丢依赖信息。 | 已清楚；无。 |
| B08-088 协方差正式定义 | 591–599，“中心化…乘积”；`sec:rv-joint` | 量化一起涨落及和的方差。 | Cov定义、和方差式、三种二元例 | 基础回顾；二阶可积使乘积可积。 | 已清楚；无。 |
| B08-089 方差缩放与和的交叉项 | 595–599，“2Cov(X,Y)”；`sec:rv-joint` | 说明平均并不自动减小误差。 | 线性缩放与和的显式式 | 独立充分但非必要，后反例区分。 | 已回顾且清楚；无。 |
| B08-090 随机向量均值 | 601–604，“E X”；`sec:rv-joint` | 将各坐标平均组织成向量。 | 显式记号 | 逐坐标可积；不是共同变化摘要。 | 已回顾；无。 |
| B08-091 协方差矩阵 | 601–612，“E[(X-μ)(X-μ)ᵀ]”；`sec:rv-joint` | 收集全部二阶共同波动。 | uᵀΣu=E[(uᵀ(X-μ))²] | 矩阵基础已回顾；对称半正定不必正定。 | 已清楚；无。 |
| B08-092 联合高斯的线性组合判据 | 614–618，“每个u”；`sec:rv-joint` | 给出含退化情形的正式定义。 | `def:probability-multivariate-gaussian` | 不是只检查单个坐标高斯。 | 已清楚；无。 |
| B08-093 高斯向量特征函数 | 620–624，“exp{iuᵀμ-…}”；`sec:rv-joint` | 统一一二阶矩与分布。 | 显式式但未展示一维积分 | 来自每个投影的一维高斯；非普通MGF。 | 局部费力；B-012，补一维计算入口。 |
| B08-094 特征函数唯一确定分布 | 625，“唯一确定分布”；`sec:rv-joint` | 从函数因子化推出测度因子化。 | 当地只有调用，没有命题或来源 | 不由特征函数存在推出；非有限矩唯一性。 | 局部费力；B-012，明确命题及引用边界。 |
| B08-095 联合高斯零交叉协方差推出独立 | 625，“分解成…乘积”；`sec:rv-joint` | 为条件高斯残差证明服务。 | 特征函数分解 | 要求联合高斯；依赖B08-094。 | 结论清楚，补B-012后支撑完整。 |
| B08-096 边缘高斯不等于联合高斯 | 626–627，“(SZ)²=Z²”；`sec:rv-joint` | 排除只看边缘的错误推断。 | Z与独立符号S构造 | 不相关仍可非线性依赖。 | 已清楚；无。 |
| B08-097 同边缘不同和的分布 | 629–648，“三种不同…效果”；`sec:rv-joint` | 具体展示联合结构不可省。 | V=U、独立、V=1-U表及图注 | 边缘相同、协方差和累计波动不同。 | 已清楚；无。 |

## 条件期望

节标签：`sec:rv-conditional-expectation`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-098 子σ代数作为信息 | 657，“当前可用信息”；`sec:rv-conditional-expectation` | 预测不能使用无法辨认的细节。 | 有限分组A/B表 | 与全部事件F不同；不是给条件点除概率。 | 已清楚；无。 |
| B08-099 观测生成的信息σ(X) | 658–663，“最小σ代数”；`sec:rv-conditional-expectation` | 精确表达仅观察X可区分什么。 | `def:probability-generated-information` | 可测原像族已构成σ代数；多观测需共同生成。 | 已清楚；无。 |
| B08-100 条件期望 | 664–672，“可积随机变量Z”；`sec:rv-conditional-expectation` | 只用G信息且每个可识别组内保平均。 | `def:probability-conditional-expectation`、分组例 | 是随机变量，不是单一常数或完整条件分布。 | 已清楚；无。 |
| B08-101 条件期望存在的RN构造 | 674–684，“ν(A)=∫_A X dP”；`sec:rv-conditional-expectation` | 定义必须确有满足对象，先非负后取差。 | `thm:probability-conditional-expectation-existence`证明 | 使用限制到G的测度；本章RN已读。 | 已清楚；无。 |
| B08-102 条件期望a.e.唯一 | 686–691，“D=Z₁-Z₂”；`sec:rv-conditional-expectation` | 说明不同版本仅零概率处不同。 | A_k正质量矛盾 | 同样的测试集工具已见于RN。 | 已清楚；无。 |
| B08-103 已知变量的条件期望 | 693，“本来就…可测”；`sec:rv-conditional-expectation` | 已有信息无需重新平均。 | E[X\|G]=X | 与独立未知变量相反。 | 已清楚；无。 |
| B08-104 独立于信息时条件均值不变 | 693–694，“等于常数E[X]”；`sec:rv-conditional-expectation` | 说明无关信息不能改变平均。 | 显式结论；基础独立可理解 | 随机变量与σ代数独立未正式展开，但基础事件定义可延用。 | 已回顾；可选说明对G中每个事件独立。 |
| B08-105 提出已知因子 | 694–701，“U有界且G-可测”；`sec:rv-conditional-expectation` | 后续正交性和换测度的运算工具。 | `eq:probability-taking-out-known-factor` | 非有界须查乘积可积，非无条件移出。 | 已清楚；无。 |
| B08-106 有限分组条件平均 | 703–716，“逐组平均”；`sec:rv-conditional-expectation` | 将抽象条件具象化。 | `eq:probability-finite-partition-conditional-expectation` | 正概率组可除；零概率组任意指定。 | 已清楚；无。 |
| B08-107 平方预测风险 | 718–747，“E[(X-U)²]”；`sec:rv-conditional-expectation` | 比较不看分组、随意分组、正确均值。 | `tab:probability-finite-partition-predictions`，5.64/2.80/0.80 | 使用信息不等于使用得最优。 | 已清楚；数值可核对。 |
| B08-108 塔式性质 | 749–769，“H⊆G”；`sec:rv-conditional-expectation` | 细信息再粗化等于直接粗化。 | `thm:probability-tower-property`完整证明 | 要求嵌套，非任意交换条件顺序。 | 已清楚；无。 |
| B08-109 全期望公式 | 771–778，“再平均…总体均值”；`sec:rv-conditional-expectation` | 将组内平均与总体目标接合。 | `eq:probability-total-expectation` | 塔式取平凡σ代数，不增加新抽样假设。 | 已清楚；无。 |
| B08-110 条件Jensen不等式 | 783–789，“使用条件Jensen”；`sec:rv-conditional-expectation` | 先证明条件均值有二阶矩。 | 只列平方特例，未建一般条件版 | 第4章仅有限Jensen实际核对。 | 局部费力；B-013，补条件版或有理仿射下界证明。 |
| B08-111 条件期望L²收缩 | 790–793，“E[m²]≤E[X²]”；`sec:rv-conditional-expectation` | 使后面平方展开与投影合法。 | 全期望接条件Jensen | 不依赖尚待证明的最优投影。 | 衔接目的明确；依据须补B-013。 |
| B08-112 条件方差 | 807–809，“E[(X-m)²\|G]”；`sec:rv-conditional-expectation` | 描述获知信息后剩余波动。 | 全方差式 | 它本身随信息变，是随机变量。 | 已清楚；无。 |
| B08-113 全方差分解 | 780–810，“无法解释…可解释”；`sec:rv-conditional-expectation` | 分开组内与组间波动。 | `eq:probability-total-variance`、交叉项消失 | 二阶可积已专门核查；不是方差任意相加。 | 已清楚；依B-013。 |
| B08-114 条件均值的平方损失最优性 | 812–818，“全部G-可测…中”；`sec:rv-conditional-expectation` | 解释为什么选条件均值作预测。 | `thm:probability-conditional-mean-l2-projection` | 只对平方损失和L²成立。 | 已清楚；无。 |
| B08-115 L²(G)闭子空间与信息投影 | 821–826，“正交投影”；`sec:rv-conditional-expectation` | 把概率预测接到Hilbert几何。 | 第5章486–592投影完整证明；当地残差正交 | 闭性只声明，直接勾股证明也足够最优性。 | 可跟上；可选补L²极限可选G-可测代表。 |
| B08-116 预测残差正交 | 823–825，“与整个L²(G)正交”；`sec:rv-conditional-expectation` | 消去风险展开交叉项。 | 提因子+塔式+Cauchy–Schwarz | 非逐点残差零，也非一般独立。 | 已清楚；无。 |
| B08-117 预测勾股分解 | 827–835，“第二项非负”；`sec:rv-conditional-expectation` | 显式证明最优及a.e.唯一。 | `eq:probability-pythagorean-prediction` | 平均平方误差，不是每样本误差都改善。 | 已清楚；无。 |
| B08-118 L¹存在与L²几何的边界 | 838–839，“仍可能存在…不能使用Hilbert”；`sec:rv-conditional-expectation` | 避免把条件期望一概当有限风险投影。 | 对比RN与平方可积条件 | 属概念比较，不是两个不同条件期望。 | 已清楚；无。 |

## 条件分布

节标签：`sec:rv-conditional-distribution`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-119 概率核 | 845–853，“每个条件值对应一个分布”；`sec:rv-conditional-distribution` | 零概率条件点不能简单相除，但还需再积分。 | `def:probability-kernel`两条要求 | 每个x的测度与每个B的可测函数是不同槽。 | 已清楚；无。 |
| B08-120 概率核可测不等于连续 | 855，“在x=0处跳变”；`sec:rv-conditional-distribution` | 防止把连续条件变量当连续条件规律。 | Y=I{X≥0} | 前章可测与连续差别已核对。 | 已清楚；无。 |
| B08-121 正则条件分布 | 857–867，“满足联合分解”；`sec:rv-conditional-distribution` | 将一般核与指定联合分布对应。 | `eq:probability-regular-conditional-kernel` | 任意核未必是当前(X,Y)的条件分布。 | 已清楚；无。 |
| B08-122 条件分布版本与共同零集 | 868，“固定B…共同零测集”；`sec:rv-conditional-distribution` | 解释点处条件规律的非唯一性。 | 逐事件和标准Borel两种范围明确 | 不能任意零点值推出实际机制改变。 | 已清楚；无。 |
| B08-123 Polish空间 | 872–876，“诱导该拓扑”；`sec:rv-conditional-distribution` | 为核存在给可控空间条件。 | 欧氏空间例 | 完备可分已解释，抽象拓扑／兼容度量未交代。 | 局部费力；B-014，改用保持同样开集的距离解释。 |
| B08-124 可分性 | 874、881，“可数稠密子集”；`sec:rv-conditional-distribution` | 让不可数状态仍可用可数结构逼近。 | 欧氏空间例；第5章251–301、1736–1744已核对 | 已回顾；与完备性不同，两条件不能互相替代。 | 已清楚；可选用Q^d。 |
| B08-125 兼容完备度量 | 874，“存在一个…完备…度量”；`sec:rv-conditional-distribution` | 极限能留在空间，同时保持原连续结构。 | Cauchy含义已复述 | 不是当前任一度量都必须完备。 | 局部费力；并B-014补“相同开集”。 |
| B08-126 标准Borel空间／可测同构 | 877–881，“双射及其逆…可测”；`sec:rv-conditional-distribution` | 只保留适合核拼接的可测结构。 | 实数、欧氏、可数集合列举 | 与同胚不同，不需保持距离；Borel子集未必继承完备。 | 已清楚；B-014补比较后更稳。 |
| B08-127 正则条件分布存在条件 | 881–886，“都是标准Borel”；`sec:rv-conditional-distribution` | 排除一般可测空间无核的风险。 | 条件与不能无条件写p(y\|x)的提醒 | 条件期望存在不推出所有点有条件密度。 | 已清楚；无。 |
| B08-128 可数生成族与测度扩张思路 | 889–891，“同一个概率核”；`sec:rv-conditional-distribution` | 说明逐事件版本如何整理。 | 仅构造路线，无完整证明 | 不能把可数生成自动当所有连续性均已核验。 | 路线可读；可选注明完整扩张论证来源，不要求当场证明。 |
| B08-129 离散条件质量与乘法公式 | 893–897，“p_X(x)>0”；`sec:rv-conditional-distribution` | 在正概率点恢复熟悉的比值。 | p_X,Y/p_X | 已回顾；不是连续零概率事件相除。 | 已清楚；无。 |
| B08-130 Bayes公式 | 898–906，“按另一顺序分解”；`sec:rv-conditional-distribution` | 由观测反向更新候选权重。 | `eq:probability-discrete-bayes`、±1信号例 | 分母边缘概率须正，不把候选变成确定点。 | 已回顾且清楚；无。 |
| B08-131 条件密度 | 908–916，“0<f_X(x)<∞”；`sec:rv-conditional-distribution` | 在共同参考测度下用密度比表示核。 | 联合密度积分版本与零集处理 | 密度版本只能a.e.保证；核不一定有密度。 | 已清楚；无。 |
| B08-132 条件高斯均值与协方差 | 927–951，“Σ₂₂可逆”；`sec:rv-conditional-distribution` | 给连续带噪更新的可算闭式。 | `eq:probability-conditional-gaussian`、S~N(0,4)例 | 与非联合高斯不相关情形分开；协方差与观测值无关。 | 已清楚；无。 |
| B08-133 Schur补 | 938、945–947，“Schur补运算”；`sec:rv-conditional-distribution` | 解释扣除观测解释掉的二阶波动。 | 第6章1116–1166已核对 | 不是Schur分解；奇异块需支持子空间及广义逆。 | 已回顾且清楚；无。 |
| B08-134 独立高斯残差 | 953–968，“R的分布不变”；`sec:rv-conditional-distribution` | 直接推导条件公式而不只背块逆。 | R定义、零交叉协方差、移项 | 依赖联合高斯零相关独立；B-012需补入口。 | 已清楚（补B-012后）；无其他修改。 |
| B08-135 条件分位数 | 982–987，“按输入报告分位数”；`sec:rv-conditional-distribution` | 输入不同可有不同尾部与位置。 | `def:statistics-conditional-quantile` | 是已知条件分布特征，非数据估计方法；a.e.版本明确。 | 已清楚；无。 |

## 独立与可交换

节标签：`sec:probability-moments-independence`，1093行起为`sec:rv-exchangeability`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-136 独立的事件乘积判据 | 994–997，“所有Borel集合”；`sec:probability-moments-independence` | 正式限制完整联合依赖。 | 显式定义、前二元表 | 基础回顾；不等于只检查协方差。 | 已清楚；无。 |
| B08-137 独立的可分函数期望乘积 | 997–1000，“从指示函数开始”；`sec:probability-moments-independence` | 后续变换函数和误差界的证明工具。 | 简单函数、MCT、正负部分的路线 | 需相关积分有定义，不能形式乘发散期望。 | 已清楚；无。 |
| B08-138 不相关与非线性依赖 | 1002–1005，“Y=X²”；`sec:probability-moments-independence` | 给独立逆命题反例。 | 对称性使Cov=0但Y确定 | 二阶摘要只排线性关联。 | 已清楚；无。 |
| B08-139 条件独立 | 1008–1016，“Z已知以后…不再提供”；`sec:probability-moments-independence` | 表达信息给定后的分布分离。 | `def:probability-conditional-independence` | 不保证去掉Z后独立；a.e.条件明确。 | 已清楚；无。 |
| B08-140 条件独立对称性 | 1021–1023，“Y⊥X\|Z”；`sec:probability-moments-independence` | 可互换两个被比较对象。 | 乘积交换即可验证 | 不与变换条件集混同。 | 已清楚；无。 |
| B08-141 分解规则 | 1024–1026，“X⊥(Y,W)…X⊥Y”；`sec:probability-moments-independence` | 删除不关心的独立对象。 | 1068–1075把C取全集 | 边缘化不新增信息。 | 已清楚；无。 |
| B08-142 弱并规则 | 1027–1029，“X⊥Y\|Z,W”；`sec:probability-moments-independence` | 将原本联合无关的W移入条件。 | 只列公式；可从条件乘积分解跟上 | 不允许对任意独立关系随意加条件。 | 已清楚；可选补一句联合前提为何关键。 |
| B08-143 收缩规则 | 1030–1032，“X⊥(Y,W)\|Z”；`sec:probability-moments-independence` | 合并分步条件独立。 | 1076–1088核因子推导 | 不是交性质，前提条件集不同。 | 已清楚；无。 |
| B08-144 交性质 | 1035–1039，“并非无条件成立”；`sec:probability-moments-independence` | 在足够支持条件下去掉交叉条件。 | `lem:probability-positive-intersection` | 与收缩不同；严格正性是附加假设。 | 已清楚；无。 |
| B08-145 严格正离散分布 | 1041–1065，“所有配置p(x)>0”；`sec:probability-moments-independence` | 使条件值能独立改变，保证消元。 | 固定b°得到q(a,c)完整证明 | 不是只要求已观察配置为正。 | 已清楚；无。 |
| B08-146 支持退化导致交性质失效 | 1066，“X=Y=W=B”；`sec:probability-moments-independence` | 验证严格正性并非装饰。 | 给定一项其他均确定，但无条件依赖 | 零配置使自由改变b,d失效。 | 已清楚；无。 |
| B08-147 图分离语义 | 1088，“图上没有边…不是…证明”；`sec:probability-moments-independence` | 限制将概率规则直接图形化。 | 无图，此处仅预告 | 概率独立与后续图模型假设分开。 | 纯预告清楚；无。 |
| B08-148 条件高斯零协方差与条件独立 | 1090–1091，“特殊情形”；`sec:probability-moments-independence` | 将高斯性质应用于条件分布。 | 前条件高斯公式 | 不能推广一般分布；退化时应说分布而非密度。 | 清楚；可选将“密度”改“分布”涵盖退化。 |
| B08-149 可交换性 | 1096–1102，“每个排列…同分布”；`sec:rv-exchangeability` | 表达观测标签无偏好。 | `def:probability-exchangeability` | 独立同分布充分，反向不成立。 | 已清楚；无。 |
| B08-150 同分布符号=ᵈ | 1100，“overset{d}{=}”；`sec:rv-exchangeability` | 说明排列仅保联合规律。 | 可交换定义的两向量 | 不是同一实现逐坐标相等。 | 已清楚；可选直说等号上d含义。 |
| B08-151 共享潜参数导致可交换依赖 | 1104、1107–1115，“共享Θ而相关”；`sec:rv-exchangeability` | 给非独立可交换的具体构造。 | Beta(2,2)，Cov=1/20，联合成功0.3 | 条件独立与边缘依赖并存；有限可交换不必混合可表。 | 已清楚；无。 |
| B08-152 可交换分数的秩对称 | 1106，“任一秩…相同机会”；`sec:rv-exchangeability` | 预备有限样本共形覆盖。 | 无并列处理，只有一句结论 | 需要无并列或对称随机破并列。 | 技术疑点；B-015，补规则及条件。 |
| B08-153 Hoeffding与共形预测 | 1106，“不能直接代入…利用…对称性”；`sec:rv-exchangeability` | 预告两类后续保证不同前提。 | 后面详细建立，此处不要求公式 | 可交换不是独立乘积结构。 | 纯预告清楚；秩措辞修B-015。 |

## 确定变换与组合

节标签：`sec:rv-pushforward`、1154行起`sec:rv-combinations`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-154 确定变换的推送g_#P | 1123–1133，“规则确定…输出不随机”；`sec:rv-transformations` | 改变取值规则并计算新分布。 | 逆像概率与h∘g平均式 | 不需要密度或逆映射；和换测度分开。 | 已清楚；无。 |
| B08-155 可逆密度换元 | 1135–1145，“补偿局部体积变化”；`sec:rv-pushforward` | 从推送得到可计算密度。 | `eq:probability-density-change-variables` | 前第3章1811–1852已读；本处默认同维欧氏可微域。 | 已清楚；可选补开集及C¹以同前章条件一致。 |
| B08-156 多分支密度变换 | 1147–1149，“对所有逆像分支求和”；`sec:rv-pushforward` | 不可逆时避免丢质量。 | Y=X²的±√y两项 | 临界y=0不直接代式；密度a.e.足够。 | 已清楚；无。 |
| B08-157 降维投影与升维嵌入的密度区别 | 1150–1152，“输出支持与输出空间”；`sec:rv-pushforward` | 纠正非方阵Jacobian误用。 | 正方形投影密度1、对角线嵌入无二维密度 | 不把降维自动等于无密度。 | 已清楚；无。 |
| B08-158 和的期望线性 | 1156，“不需要独立”；`sec:rv-combinations` | 区别平均运算和依赖假设。 | E(X+Y)=EX+EY | 已回顾，须可积。 | 已清楚；无。 |
| B08-159 线性组合方差 | 1157–1163，“2abCov”；`sec:rv-combinations` | 定量比较前面三种平均。 | 三个和方差1、1/2、0 | 与相同边缘无关，需联合二阶信息。 | 已清楚；无。 |
| B08-160 乘积与比值的可积条件 | 1163，“另查比值的矩”；`sec:rv-combinations` | 防止对变量做运算后沿用原矩条件。 | Cauchy–Schwarz与后Cauchy比值例 | 两个L¹不足乘积L¹，分母非零仍不足有限均值。 | 已清楚；无。 |
| B08-161 和的密度 | 1165–1168，“f_(X+Y)(s)”；`sec:rv-combinations` | 把二元变换与边缘化合用。 | ∫f_X,Y(x,s-x)dx | 不要求独立。 | 已清楚；无。 |
| B08-162 乘积密度 | 1169–1174，“1/\|x\|”；`sec:rv-combinations` | 追踪乘法的体积因子。 | ∫f_X,Y(x,z/x)/\|x\| | x=0排除，联合密度下零集不承质量。 | 已清楚；无。 |
| B08-163 比值密度 | 1171–1181，“\|y\|”；`sec:rv-combinations` | 计算除法后分布与重尾。 | R=X/Y积分 | 与乘积因子互反；零分母概率在联合密度下为0。 | 已清楚；无。 |
| B08-164 独立和的卷积 | 1174–1175，“f_X*f_Y”；`sec:rv-combinations` | 独立使联合密度因子化。 | 连续卷积及离散和式 | 第7章连续卷积已读；此处概率用途。 | 已清楚；无。 |
| B08-165 Cauchy分布 | 1176–1182，“1/[π(1+r²)]”；`sec:rv-combinations` | 高斯之比证明矩不能沿除法传递。 | 完整积分、E\|R\|=∞ | 两个高斯所有矩有限不改变该反例。 | 已清楚；无。 |
| B08-166 独立和特征函数乘积 | 1184–1188，“φ_(X+Y)=φ_Xφ_Y”；`sec:rv-combinations` | 将卷积转成简单乘法。 | 期望乘積一行推导 | 由独立性，不由均值相加。 | 已清楚；无。 |
| B08-167 MGF乘积与累积量可加 | 1189–1190，“K_(X+Y)=K_X+K_Y”；`sec:rv-combinations` | 组织独立累计的各阶量。 | 共同有限邻域条件明确 | 与始终存在的特征函数分开。 | 已清楚；无。 |
| B08-168 跨坐标累积量为零与逆判据 | 1190，“原点邻域解析”；`sec:rv-combinations` | 高阶摘要检测非高斯依赖。 | 正向相加，反向调用唯一性 | 并非只要某个三四阶为零就独立。 | 概念可读；变换唯一性补B-012。 |
| B08-169 高斯高阶累积量为零 | 1190–1191，“三阶及以上…为零”；`sec:rv-combinations` | 说明高斯只留二阶方向信息。 | K为二次式可对照前高斯例 | 不意味着变量必常数。 | 已清楚；无。 |
| B08-170 独立成分分析 | 1191，“辨认…隐藏的依赖”；`sec:rv-combinations` | 给高阶统计应用，但未说要从什么恢复什么。 | 无混合模型或来源 | 非基础概率概念；与PCA不同。 | 局部费力；B-017，补线性混合到独立源的任务定义或标纯预告。 |
| B08-171 协方差白化 | 1191，“白化后”；`sec:rv-combinations` | 说明二阶信息不足以确定独立方向。 | 当地无定义、无Cov=I式 | 前1–7章未定义；不能靠“白化”一词理解。 | 局部费力；B-017，补线性变换使协方差为I及旋转不变。 |
| B08-172 Poisson与Gamma的独立相加规律 | 1192–1193，“相乘后参数相加”；`sec:rv-combinations` | 回答前面计数／平方和组合的预告。 | Poisson MGF明确；Gamma MGF未列 | 由密度积分可跟算；共同速率关键。 | 已清楚；可选列Gamma MGF=(b/(b-t))^a。 |
| B08-173 向量仿射变换的矩 | 1195–1200，“AΣAᵀ”；`sec:rv-combinations` | 统一线性特征变换后的均值与波动。 | 均值、方差、两映射交叉协方差三式 | 不需高斯，相关矩须存在。 | 已回顾且清楚；无。 |
| B08-174 高斯在线性变换下封闭 | 1201–1202，“即使A不满秩”；`sec:rv-combinations` | 从线性投影定义得到变换分布。 | N(Aμ+b,AΣAᵀ) | 可能退化，无非退化密度保证。 | 已清楚；无。 |
| B08-175 最大值与最小值分布 | 1204–1208，“F(x)^n”；`sec:rv-combinations` | 排序也是确定变换。 | 交事件与iid概率乘积 | n个样本需独立同分布。 | 已回顾且清楚；无。 |
| B08-176 次序统计量X_(k) | 1210–1215，“第k小”；`sec:rv-combinations` | 用二项计数计算秩位置阈值。 | 至少k个输入≤x的和式 | 索引(k)不是样本编号k。 | 已清楚；无。 |
| B08-177 经验分位数 | 1215，“相应秩位置”；`sec:rv-combinations` | 将分位数落实到有限样本。 | 排序向量 | 此处未定精确取整，正式经验分布后补；作为预告足够。 | 预告清楚；无。 |
| B08-178 连续样本分位秩的Beta分布 | 1216–1219，“F(Y_(k))”；`sec:rv-combinations` | 不依赖高斯近似计算分位数覆盖。 | Beta(k,n+1-k)结论；二项式可推 | 连续CDF足够，离散跳跃须另保不等式。 | 可跟上；可选补概率积分变换的一句说明。 |

## 随机生成

节标签：`sec:rv-random-generation`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-179 混合模型 | 1224–1226，“先抽指标…再…分量”；`sec:rv-random-generation` | 条件生成后边缘化得到多形状分布。 | 混合密度和式、双高斯例 | 不是分布参数的简单平均。 | 已清楚；无。 |
| B08-180 潜变量 | 1226，“组织联合分布和计算”；`sec:rv-random-generation` | 为生成过程加入未观测的中间变量。 | 分量指标Z | 不必对应真实可观测类别。 | 已清楚；无。 |
| B08-181 分量责任概率 | 1226，“条件化X”；`sec:rv-random-generation` | 根据结果推回可能分量。 | 由已建Bayes可写P(Z=k\|X=x)，当地未列 | 与混合权重先验不同。 | 基本可懂；可选显式列权重比，非实质问题。 |
| B08-182 混合分布总方差 | 1228–1241，“分量内和分量间”；`sec:rv-random-generation` | 防止只平均分量方差。 | 两高斯均值1/2、方差7/4 | 全方差已读，漏项3/4明确。 | 已清楚；无。 |
| B08-183 层次模型 | 1243–1247，“参数本身也…随机”；`sec:rv-random-generation` | 组织共享不确定性。 | Θ~π，X_i\|Θ条件独立 | 与固定参数iid不同；边缘通常相关。 | 已清楚；无。 |
| B08-184 随机概率测度 | 1249–1261，“整个概率分布随机”；`sec:rv-random-generation` | 从随机有限参数扩到随机规律。 | `def:probability-random-probability-measure` | 每次实现必须是测度；不是维数写∞。 | 已清楚；无。 |
| B08-185 评价σ代数 | 1256–1259，“μ↦μ(A)”；`sec:rv-random-generation` | 使测度值域具备明确可测结构。 | 对每个A，G(A)可测的等价解释 | 与状态空间A的σ代数分处不同层。 | 已清楚；无。 |
| B08-186 Dirichlet过程 | 1252预告、1262–1270定义，“任意有限可测分割”；`sec:rv-random-generation` | 任意有限概率分组遵循一致Dirichlet规律。 | `def:probability-dirichlet-process` | 不只一个有限Dirichlet向量；零参数坐标单列。 | 已清楚；可选二分区Beta例帮助定位随机对象层次。 |
| B08-187 基概率测度G₀与总质量参数α | 1264–1269，“参数(α,G₀)”；`sec:rv-random-generation` | 分开质量位置与集中程度。 | Dirichlet参数αG₀(A_k) | 与一次实现G不同；可回用Beta矩。 | 已清楚；可选写E G(A)=G₀(A)。 |
| B08-188 分割相容性 | 1271–1272，“合并…质量相加…参数…相加”；`sec:rv-random-generation` | 同一随机测度不能给冲突有限规律。 | 明确合并规则 | 不能只因有限维相容就忽略路径可数可加。 | 已清楚；一般存在为引用结论，可选补来源。 |

## 概率加权与条件换测度

节标签：`sec:rv-change-measure`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-189 一般换测度积分公式 | 1277–1288，“每个非负可测g”；`sec:rv-change-measure` | 将有限分块公式推广到一般积分。 | `thm:probability-change-measure-integral`完整证明 | RN导数已存在；非负后可积实值。 | 已清楚；无。 |
| B08-190 权重均值为1 | 1290，“E_Q[w]=1”；`sec:rv-change-measure` | 验证目标是概率而非任意有限测度。 | 取g=1及有限三点表 | 不保证权重有界或方差有限。 | 已清楚；无。 |
| B08-191 权重存在／有界／二阶矩有限的区别 | 1290–1293，“三项不同条件”；`sec:rv-change-measure` | 为数值重加权误差设边界。 | w=1/(2√x)，积分1、平方发散 | 绝对连续只看零集兼容。 | 已清楚；无。 |
| B08-192 权重方向与贡献 | 1295–1316，“dP/dQ”；`sec:rv-change-measure` | 防止参考和目标写反。 | (0.4,0.75,5)表、`fig:probability-importance-weights` | 观测值g不是概率；P无法到达质量不可补救。 | 已清楚；无。 |
| B08-193 a.e.结论随绝对连续转移 | 1319–1322，“反向…需要Q≪P”；`sec:rv-change-measure` | 明确换测度后上界何时保留。 | 坏集合零测说明 | 与L²大小控制不同。 | 已清楚；无。 |
| B08-194 重加权有限方差充分条件 | 1322–1326，“E_Q[w²g²]≤B²E_Q[w²]”；`sec:rv-change-measure` | 连接有界函数与权重尾部。 | 显式不等式 | 权重二阶矩有限是充分而非必要。 | 已清楚；无。 |
| B08-195 权重截断与偏差 | 1326–1329，“w_c=min{w,c}”；`sec:rv-change-measure` | 限制波动需付目标偏移代价。 | 偏差=-E_Q[(w-c)_+g] | 不再是精确换测度；非归一化自归一估计。 | 已清楚；无。 |
| B08-196 条件换测度公式 | 1332–1339，“条件期望的比值”；`sec:rv-change-measure` | 条件分组内重新归一化。 | `eq:probability-conditional-change-measure` | 与无条件乘权不同；X需Q可积。 | 公式与证明清楚；示例问题见B-016。 |
| B08-197 分母零集在目标下可忽略 | 1340–1354，“Q(D=0)=0”；`sec:rv-change-measure` | 合法定义候选Z，不在零分母硬除。 | D、N与指标式 | P下可有正质量，Q下却零；方向重要。 | 已清楚；无。 |
| B08-198 条件期望保序与三角不等式 | 1355–1371，“\|N\|≤E_P[L\|X\|\|G]”；`sec:rv-change-measure` | 保证零集上N也为0、后续可积。 | 非负零期望推出a.e.零 | 保序可由RN非负构造推出，正文未明接；B-013已覆盖入口。 | 可跟上；随B-013补一句。 |
| B08-199 非负已知因子的有界截断 | 1372–1387，“由有界截断和单调收敛”；`sec:rv-change-measure` | 在未先知可积时合法提出\|Z\|。 | E_Q\|Z\|≤E_Q\|X\|完整估计 | 不能先把未证可积当既有条件。 | 已清楚；无。 |
| B08-200 条件换测度的定义验证 | 1388–1405，“对A∈G…计算”；`sec:rv-change-measure` | 证明候选保所有可识别事件积分。 | 六步积分等式 | 先有可积，再用条件定义，顺序合理。 | 已清楚；无。 |
| B08-201 有限分组重新归一化示例 | 1407–1420，“分母为何不可省略”；`sec:rv-change-measure` | 想显示漏分母会错。 | 四点P/Q/L算式 | 实际P(A)=Q(A)=1/2，两组分母都1。 | 局部费力；B-016，改Q使组总质量不同。 |
| B08-202 有限联合观测的链式密度比 | 1421–1429，“逐步…乘积”；`sec:rv-change-measure` | 将一次权重扩展到历史依赖观测。 | ∏q_i(x_i\|x_<i)/p_i(x_i\|x_<i) | 各步可测且归一，绝对连续；不预设Markov。 | 已清楚；无。 |

## 随机序列与单个累计量

节标签：`sec:rv-sequences`、`sec:rv-aggregation`／`sec:probability-basic-tail-bounds`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-203 随机序列 | 1438–1441，“同一概率空间上的可测映射族”；`sec:rv-sequences` | 扩展单变量到重复观测。 | `def:rv-random-sequence` | 索引未必是物理时间。 | 已清楚；无。 |
| B08-204 实现序列 | 1440–1441，“固定ω”；`sec:rv-sequences` | 区分固定编号的随机变量与固定结果的一串数。 | 显式(X_n(ω)) | 非随机变量族本身。 | 已清楚；无。 |
| B08-205 累计和序列 | 1444–1445，“共享此前的全部增量”；`sec:rv-sequences` | 说明独立输入不意味着独立累计量。 | S_n=Σ ε_i与共享Θ读数比较 | 边缘相同不确定联合。 | 已清楚；无。 |
| B08-206 有限样本误差 | 1449，“现有n次观测是否足够”；`sec:rv-aggregation` | 将概率常数与极限区别。 | 后面各界可代n计算 | 不由收敛声明自动给出。 | 已清楚；无。 |
| B08-207 Markov不等式 | 1456–1467，“X≥0”；`sec:probability-basic-tail-bounds` | 用一阶矩控制大值概率。 | `eq:probability-markov-inequality`及指标证明 | 已回顾；非负条件必要。 | 已清楚；无。 |
| B08-208 Chebyshev不等式 | 1467–1475，“用于(X-μ)²”；`sec:probability-basic-tail-bounds` | 方差转双侧偏差概率。 | `eq:probability-chebyshev-inequality` | 已回顾；仅二阶信息，不利用范围。 | 已清楚；无。 |
| B08-209 Chernoff方法 | 1477–1487，“随后对λ优化”；`sec:probability-basic-tail-bounds` | 指数放大尾部后优化界。 | `eq:probability-chernoff-step` | MGF有限才有用，不同于直接Markov常数。 | 已清楚；无。 |
| B08-210 次高斯变量 | 1489–1499，“描述…上界”；`sec:probability-basic-tail-bounds` | 用统一指数矩形式组织高斯型尾界。 | `def:probability-subgaussian`及λ=t/σ² | 不必是高斯；σ²是上界参数而非必等于方差。 | 已清楚；可选显说参数非唯一。 |
| B08-211 Hoeffding引理 | 1502–1507，“X∈[a,b]”；`sec:probability-basic-tail-bounds` | 有界中心化变量自动有指数矩上界。 | `lem:probability-hoeffding-lemma` | 与和的Hoeffding定理不同。 | 结论清楚；证明变量见B-018。 |
| B08-212 指数函数的端点弦控制 | 1510–1514，“二点分布矩母函数”；`sec:probability-basic-tail-bounds` | 将任意有界规律变成端点最坏界。 | 两端凸组合公式 | 用已知凸性，不是假设X本来二点。 | 已清楚；无。 |
| B08-213 对数MGF的二阶导数界 | 1514–1517，“至多为1/4”；`sec:probability-basic-tail-bounds` | 两次积分产生区间平方常数。 | 当地未列函数及求导变量 | λ与λ(b-a)尺度不同。 | 局部费力；B-018，写s及ψ(s)。 |
| B08-214 Hoeffding不等式 | 1521–1560，“相互独立”；`sec:probability-basic-tail-bounds` | 控制有界独立但未必同分布的和。 | `thm:probability-hoeffding-inequality`完整乘積及优化 | 有界用于单项，独立用于分解，双侧再联合界。 | 已清楚；无。 |
| B08-215 [0,1]样本平均集中 | 1562–1565，“2e^(-2nε²)”；`sec:probability-basic-tail-bounds` | 把累计偏差换成平均误差。 | 显式双侧式 | 只要求独立，中心为E平均。 | 已清楚；无。 |
| B08-216 Bernstein不等式 | 1567–1575，“v=ΣE X_i²”；`sec:probability-basic-tail-bounds` | 利用实际方差改善区间最坏界。 | `eq:probability-bernstein-inequality` | 中心化、独立、有界M；不同于仅区间长度。 | 已清楚；无。 |
| B08-217 Bernstein高阶矩控制 | 1577–1593，“\|X_i\|^k≤M^(k-2)X_i²”；`sec:probability-basic-tail-bounds` | 解释指数矩中的几何级数。 | 级数、1+u≤e^u | k!≥2·3^(k-2)未列但可初等归纳。 | 可跟算；可选补该阶乘界。 |
| B08-218 高斯型与指数型双尺度 | 1603，“小偏差…大偏差”；`sec:probability-basic-tail-bounds` | 解释v与Mt哪项控制分母。 | Bernoulli(0.01)的两界数值 | Bernstein不处处优于Hoeffding。 | 已清楚；无。 |
| B08-219 重尾及集中工具失效 | 1617–1618，“方差可能不存在”；`sec:probability-basic-tail-bounds` | 明确矩／范围条件失效不能照搬。 | 前Cauchy例可回用 | 截断与稳健均值只预告，不能当已建立算法。 | 已清楚；无。 |

## 共同误差与随机复杂度

节标签：`sec:probability-uniform-errors-symmetry`／`sec:probability-random-functions-uniform-error`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-220 损失函数 | 1627，“ℓ(h,Z)∈[0,1]”；`sec:probability-uniform-errors-symmetry` | 将候选表现转成可平均读数。 | 风险两式 | 本处有界，非所有损失自动满足。 | 已清楚；可选以错误指示解释“损失”。 |
| B08-221 真实风险 | 1627–1629，“E[ℓ(h,Z)]”；`sec:probability-uniform-errors-symmetry` | 表示总体而非这批样本表现。 | R(h)定义 | 期望已建立，P是未知但固定规律。 | 已清楚；无。 |
| B08-222 经验风险 | 1629，“1/n Σℓ”；`sec:probability-uniform-errors-symmetry` | 由已有样本估算总体平均。 | R̂_n(h)定义 | 与真实风险差是随机量。 | 已清楚；无。 |
| B08-223 经验风险最小化 | 1633–1634，“argmin…由同一批数据选出”；`sec:probability-uniform-errors-symmetry` | 让最优候选随观测改变。 | 后三步风险比较 | 不是预先固定候选。 | 已清楚；无。 |
| B08-224 选择偏差 | 1634，“恰好因噪声看起来最好”；`sec:probability-uniform-errors-symmetry` | 解释为何需全类共同事件。 | 候选事后选择与固定h对比 | 此处不是抽样代表性偏差。 | 已清楚；无。 |
| B08-225 随机上确界可测性 | 1636，“可数子类…逐点极限”；`sec:probability-uniform-errors-symmetry` | 保证共同误差事件有概率。 | 可数稠密充分条件 | 点态极限配有界收敛使总体平均一致；非任意不可数并。 | 已清楚；可选接一句支配收敛用途。 |
| B08-226 分布无关一致收敛 | 1637–1648，“同一个n₀”；`sec:probability-uniform-errors-symmetry` | 同时量化候选、分布与样本量。 | `def:uniform-convergence`及量词解释 | 不同于逐函数或逐分布收敛，也不同于确定函数列一致收敛。 | 已清楚；无。 |
| B08-227 有限函数类共同界 | 1650–1670，“同时对所有h”；`sec:probability-uniform-errors-symmetry` | 联合界把单项Hoeffding转为可选择保证。 | `eq:probability-finite-class-bound`完整证明 | 预先固定M个候选，log M成本。 | 已清楚；无。 |
| B08-228 超额风险的2ε传递 | 1672–1684，“第二步…经验最优性”；`sec:probability-uniform-errors-symmetry` | 从估计误差转选择结果质量。 | 三行不等式 | 最佳候选h*是类内总体最优。 | 已清楚；无。 |
| B08-229 事先固定类与数据生成类 | 1684–1689，“最终数量…未必合法”；`sec:probability-uniform-errors-symmetry` | 防止事后缩小计数偷去复杂度。 | M=100、n=1000得0.0644 | 单项95%不等于共同95%。 | 已清楚；无。 |
| B08-230 χ²尾界 | 1692–1707，“2√kx+2x”；`sec:probability-uniform-errors-symmetry` | 为随机投影的平方长度建立专用界。 | `lem:probability-chi-square-tail` | χ²分布此前已定义；这里不是正态近似。 | 已清楚；无。 |
| B08-231 χ²指数矩推导 | 1711–1724，“高斯积分给出”；`sec:probability-uniform-errors-symmetry` | 精确MGF经Chernoff转两侧阈值。 | 对数级数、两组λ和相对界 | 上下尾不同，最后保守统一常数。 | 已清楚；无。 |
| B08-232 高斯随机投影 | 1726–1732，“元素独立N(0,1/k)”；`sec:probability-uniform-errors-symmetry` | 随机线性映射近似保留有限点距离。 | `thm:probability-johnson-lindenstrauss` | 与PCA数据自适应方向不同。 | 已清楚；无。 |
| B08-233 Johnson–Lindenstrauss距离保持 | 1733–1748，“全部i,j同时”；`sec:probability-uniform-errors-symmetry` | 点对计数把固定方向集中推广全点集。 | `eq:probability-jl-distance-preservation`完整证明 | 平方距离与距离因子分开；零差与核方向边界明确。 | 已清楚；无。 |
| B08-234 有限取值模式化 | 1752–1755，“只需对这些模式联合控制”；`sec:probability-uniform-errors-symmetry` | 借前章组合容量处理无限类。 | 第2章371–531已实读 | 样本限制只留样本内值，不保真实风险。 | 局部费力；B-019，需先对称化再条件于合并样本。 |
| B08-235 ε网／覆盖数回顾 | 1753–1761，“有限ε-网”；`sec:probability-uniform-errors-symmetry` | 用有限代表逼近连续候选。 | 第5章973–1118和九格心图 | 本章参数顺序N(F,d,ε)与前章N(ε,F,d)不同。 | 已回顾；可选统一记号次序。 |
| B08-236 候选索引随机过程 | 1761–1766，“{Z_f:f∈F}”；`sec:probability-uniform-errors-symmetry` | 把每个候选误差当共同概率空间的变量。 | 随机Lipschitz条件 | “过程”尚未正式定义，但族写法已明确；非必时间。 | 可理解；可选写“随机变量族”避免提前术语。 |
| B08-237 有限网控制引理 | 1757–1787，“t+Lε”；`sec:probability-uniform-errors-symmetry` | 同时保留离散误差与尾概率代价。 | `eq:probability-covering-finite-net`逐点选代表证明 | 要a.s.同时Lipschitz，非各对分开a.s.。 | 已清楚；无。 |
| B08-238 经验与真实风险的Lipschitz传递 | 1789–1792，“过程常数是2L₀”；`sec:probability-uniform-errors-symmetry` | 防止把样本近似直接当风险近似。 | 两项常数相加 | 两种风险均需控制，不只报告覆盖大小。 | 已清楚；无。 |
| B08-239 有界差条件 | 1795–1797，“替换第i个输入”；`sec:probability-uniform-errors-symmetry` | 控制整个数据函数对单观测敏感度。 | c_i上确界式 | 不是要求F自身取值区间固定为c_i。 | 已清楚；无。 |
| B08-240 McDiarmid不等式 | 1798–1810，“独立输入下”；`sec:probability-uniform-errors-symmetry` | 将和的集中推广到数据函数。 | `eq:probability-mcdiarmid` | Doob鞅是明确后文证明预告，不当现有定义。 | 陈述清楚；无。 |
| B08-241 Rademacher随机符号 | 1815，“独立且等概率取-1,1”；`sec:probability-uniform-errors-symmetry` | 构造无信号的可拟合扰动。 | 定义内给出分布 | 与观测样本的随机性分层。 | 已清楚；无。 |
| B08-242 经验Rademacher复杂度 | 1812–1822，“尽量对齐…随机正负号”；`sec:probability-uniform-errors-symmetry` | 衡量固定观测上的随机拟合能力。 | `eq:empirical-rademacher`、常数类例 | 先sup后平均不能换序。 | 已清楚；无。 |
| B08-243 期望Rademacher复杂度 | 1823–1830，“还平均了抽样结果”；`sec:probability-uniform-errors-symmetry` | 把样本条件复杂度转整体量。 | `def:expected-rademacher-complexity` | 依赖P，经验版只依赖样本值。 | 已清楚；无。 |
| B08-244 函数类凸包 | 1831–1845，“全部有限凸组合”；`sec:probability-uniform-errors-symmetry` | 检查增加混合候选是否增加随机线性拟合。 | 显式conv B集合 | 凸组合非任意线性组合；前4章凸包已读。 | 已回顾且清楚；无。 |
| B08-245 凸包复杂度不变 | 1835–1869，“两个上确界都相等”；`sec:probability-uniform-errors-symmetry` | 利用线性泛函在凸包上不增最大值。 | `thm:ensemble-convex-hull`完整双向证明 | 需样本统一有界和后样本可测性，不要求达到sup。 | 已清楚；无。 |
| B08-246 常数基类的复杂度算例 | 1871–1876，“两类…都为1/2”；`sec:probability-uniform-errors-symmetry` | 给无限候选不必更复杂的可算例。 | n=1、0和1及[0,1]常值类 | 阈值化等非线性变换不保恒等式。 | 已清楚；无。 |
| B08-247 经验高斯复杂度 | 1878–1884，“符号与幅度都变化”；`sec:probability-uniform-errors-symmetry` | 用高斯随机线性和衡量类。 | `def:gaussian-complexity` | 不能按单次系数直接比较。 | 已清楚；无。 |
| B08-248 期望高斯复杂度 | 1885，“E_S”；`sec:probability-uniform-errors-symmetry` | 对固定样本复杂度再平均。 | 显式G_n式 | 与经验版相同层次差异。 | 已清楚；无。 |
| B08-249 带绝对值复杂度 | 1889–1895，“G∪(-G)”；`sec:probability-uniform-errors-symmetry` | 双侧误差需同时考虑正负方向。 | 单常数1的0与正值对比 | 对称类可等同，不一般混用。 | 已清楚；无。 |
| B08-250 独立同分布副本 | 1901，“Z₁′,…,Z_n′”；`sec:probability-uniform-errors-symmetry` | 用第二批经验平均代替未知总体均值。 | Jensen显示E sup差的上界 | 副本独立于原样本是要点。 | 已清楚；Jensen入口归B-013。 |
| B08-251 对称化 | 1897–1924，“交换后联合分布不变”；`sec:probability-uniform-errors-symmetry` | 从总体误差转成符号随机和。 | 对换不变及2倍R_abs界 | 2来自三角不等式拆原样本／副本，不是凭空常数。 | 可跟上；可选列中间拆和一行。 |
| B08-252 收缩不等式 | 1926–1942，“L-Lipschitz且φ_i(0)=0”；`sec:probability-uniform-errors-symmetry` | 把预测类复杂度传到损失类。 | 带绝对值2L界 | 一般类与关于取负封闭类常数有别。 | 已清楚；无。 |
| B08-253 逐坐标替换证明 | 1944–1958，“近似最大元”；`sec:probability-uniform-errors-symmetry` | 将非线性φ坐标逐一换成L倍线性坐标。 | 正负各半sup、按a_n-b_n选方向 | 不需最大值实际达到。 | 已清楚；无。 |
| B08-254 加入零向量 | 1959–1989，“两个单侧上确界非负”；`sec:probability-uniform-errors-symmetry` | 合法把绝对值最大值控制为两项和。 | A₀及逐行2L界 | 加零不改变原绝对值sup，非原类含零的隐藏假设。 | 已清楚；无。 |
| B08-255 线性范数球复杂度 | 1991–2011，“BR/√n”；`sec:probability-uniform-errors-symmetry` | 将抽象sup化成对偶范数和样本尺度。 | 展开范数、符号交叉项为零 | 第6章278–310对偶范数已于第7章依赖核对；不直接是高概率界。 | 已清楚；无。 |
| B08-256 高斯符号与幅度分解 | 2026，“g_i=σ_i\|g_i\|”；`sec:probability-uniform-errors-symmetry` | 为复杂度单向比较建立共同随机性。 | 独立、E\|g\|=√(2/π) | 高斯对称性使幅度与符号分离，非任意分布都有。 | 已清楚；Jensen仍见B-013。 |
| B08-257 Rademacher至高斯单向比较 | 2019–2026，“≤√(π/2)”；`sec:probability-uniform-errors-symmetry` | 允许保方向地更换复杂度工具。 | 凸函数幅度平均说明 | 不是两者普适常数等价。 | 已清楚；无。 |
| B08-258 反向比较的√log n代价 | 2028–2030，“坐标向量及其相反数”；`sec:probability-uniform-errors-symmetry` | 说明为何不能对称替换。 | 只给Θ结论，未列最大高斯绝对值 | 需要此前未建的独立高斯最大值尺度。 | 局部费力；B-020，展开两个sup并注明最大值估计来源。 |

## 采样积分与方差缩减

节标签：`sec:probability-monte-carlo-variance-reduction`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-259 直接蒙特卡洛估计 | 2035–2039，“独立采样”；`sec:probability-monte-carlo-variance-reduction` | 用随机样本平均近似积分。 | Î_n公式、∫x²=1/3教学积分 | 需可执行采样，非将所有积分直接离散网格化。 | 已清楚；无。 |
| B08-260 估计无偏性 | 2040，“线性性给出无偏性”；`sec:probability-monte-carlo-variance-reduction` | 比较估计量平均与目标是否相等。 | E Î_n=I可直接取期望 | 本科背景已回顾，正式统计定义在后；非单次精确。 | 已清楚；无。 |
| B08-261 蒙特卡洛方差及根号样本量尺度 | 2040–2051，“σ_f²/n”；`sec:probability-monte-carlo-variance-reduction` | 给采样预算与波动的量化关系。 | 单样本方差4/45 | 维数未显式出现不等于方差不随维数增长；一致性后讲。 | 已清楚；无。 |
| B08-262 重要性采样 | 2053–2064，“从Q采样得到无偏估计”；`sec:probability-monte-carlo-variance-reduction` | 改采样分布并用密度比补偿。 | `eq:probability-importance-sampling` | P≪Q、乘积可积；权重存在非有限方差。 | 已清楚；无。 |
| B08-263 提议分布的方差效果 | 2066–2070，“q(x)=2x”；`sec:probability-monte-carlo-variance-reduction` | 可算地比较改变采样分布的收益。 | 方差1/72与4/45 | 过轻尾部会增大方差，不普遍降低。 | 已清楚；无。 |
| B08-264 固定被积函数的支持条件 | 2072–2089，“支配…f dP”；`sec:probability-monte-carlo-variance-reduction` | 松开不必要的全P绝对连续条件。 | q>0在\|f\|p>0处、h_Q=fp/q | 与可重用到其他f的密度比不同。 | 已清楚；无。 |
| B08-265 最优提议密度 | 2080–2086，“q*∝\|f\|p”；`sec:probability-monte-carlo-variance-reduction` | 给采样质量分配的理想基准。 | 显式归一式；未展示最优性证明 | Cauchy–Schwarz可直接推出：E_Q h²≥(E_P\|f\|)²。 | 可跟上；可选补这行不等式。 |
| B08-266 零方差理想采样 | 2090–2093，“h_Q*(X)=I”；`sec:probability-monte-carlo-variance-reduction` | 区分理论最优与可执行算法。 | 非负f时归一化正好未知I | 非负是关键；有符号f不保证零方差。 | 已清楚；无。 |
| B08-267 混入目标分布保支持 | 2094–2097，“q_η=(1-η)q*+ηp”；`sec:probability-monte-carlo-variance-reduction` | 需要复用权重时避免目标正质量区消失。 | η∈(0,1)显式混合 | 仍须能归一化和采样；不是已给可实施算法。 | 已清楚；无。 |
| B08-268 控制变量 | 2099–2105，“减去β(h-μ_h)”；`sec:probability-monte-carlo-variance-reduction` | 通过已知零均值修正消波动。 | 方差二次式 | 改读数而非改采样分布，μ_h须已知。 | 已清楚；无。 |
| B08-269 最优控制系数 | 2106–2112，“Cov(f,h)/Var(h)”；`sec:probability-monte-carlo-variance-reduction` | 对方差二次函数求最小。 | h=X、β*=1、方差1/180 | Var h>0；估计β不能沿用固定系数无偏论证。 | 已清楚；无。 |
| B08-270 Rao–Blackwell化 | 2114–2128，“消去条件内噪声”；`sec:probability-monte-carlo-variance-reduction` | 用条件平均保持均值且降低方差。 | `eq:probability-rao-blackwell-variance` | 本处任意统计量的方差分解版本；统计充分性条件后再论。 | 已清楚；无。 |
| B08-271 命中型积分估计 | 2130–2133，“I{U≤X²}”；`sec:probability-monte-carlo-variance-reduction` | 将二维命中随机性与条件平滑作可算比较。 | 均值1/3、方差2/9到4/45 | X²是给定X的条件成功概率；依赖独立U。 | 已清楚；无。 |

## 自归一化与重采样

节标签：`sec:probability-monte-carlo-variance-reduction`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-272 自归一化重要性估计 | 2135–2153，“未知公共常数倍”；`sec:probability-monte-carlo-variance-reduction` | 用比值消掉归一化常数。 | `eq:probability-self-normalized-importance-sampling` | 分母正，权重须为目标比的共同倍数；不是任意权重平均。 | 已清楚；无。 |
| B08-273 有限样本比值偏差 | 2151–2152，“E[A/B]≠EA/EB”；`sec:probability-monte-carlo-variance-reduction` | 区分原始IS无偏与自归一比值。 | 明确反等式，长期条件后讲 | 强一致仍可有限样本有偏。 | 已清楚；无。 |
| B08-274 截断偏差与方差算例 | 2155–2175，“权重截断在2”；`sec:probability-monte-carlo-variance-reduction` | 定量核对缩波动的代价。 | 三点表，2.04到0.64、偏差-0.2 | 截断原贡献与截断后归一化不是同目标。 | 已清楚；无。 |
| B08-275 粒子加权经验分布 | 2177–2178，“二十粒子样本”；`sec:probability-monte-carlo-variance-reduction` | 给重采样提供有限离散概率。 | 16a、3b、1c及加权三点质量 | “粒子”在此就是一个样本点，未显说但例明确。 | 可理解；可选补这一同义说明。 |
| B08-276 多项重采样 | 2179–2185，“后代数的条件期望”；`sec:probability-monte-carlo-variance-reduction` | 将不均权重转为随机复制次数。 | (8,6,6)、额外条件方差0.012 | 保当前经验目标的条件均值，不修复原目标偏差。 | 已清楚；可选显说按归一权重独立抽20次。 |
| B08-277 经验有效样本量 | 2185–2192，“权重退化的诊断量”；`sec:probability-monte-carlo-variance-reduction` | 摘要权重是否集中在少数点。 | (Σw)²/Σw²、7.69与12.8 | 非所有估计目标共享的精确iid样本数。 | 已清楚；无。 |
| B08-278 自归一化集中 | 2192，“随机设计矩阵度量累计噪声”；`sec:probability-monte-carlo-variance-reduction` | 避免与比值估计同名混用。 | 明确后节引用 | 纯预告，不当现有已建工具。 | 预告清楚；无。 |

## 收敛方式与变换

节标签：`sec:rv-numerical-convergence`，上层`sec:probability-random-convergence-asymptotics`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-279 事件上极限 | 2201–2207，“发生无穷多次”；`sec:rv-numerical-convergence` | 从逐时刻概率改问路径反复出错。 | ∩尾部∪定义 | 非数列数值limsup，但集合量词清楚。 | 已清楚；无。 |
| B08-280 Borel–Cantelli可求和方向 | 2208–2213、2223–2228，“不要求独立”；`sec:rv-numerical-convergence` | 可求和坏概率排除无限次发生。 | `thm:probability-borel-cantelli`联合界证明 | 不从单项概率趋零直接推出。 | 已清楚；无。 |
| B08-281 Borel–Cantelli独立发散方向 | 2214–2218、2228–2239，“相互独立”；`sec:rv-numerical-convergence` | 证明少见事件仍可无穷次发生。 | 补事件概率乘积及指数界 | 发散本身不够，独立进入乘積。 | 已清楚；无。 |
| B08-282 依概率收敛 | 2245–2247，“固定容差外的概率趋于零”；`sec:rv-numerical-convergence` | 量化多数结果上的接近。 | `def:probability-random-convergence` | 需同一基础空间；坏事件可随n变。 | 已回顾且清楚；无。 |
| B08-283 几乎必然收敛 | 2249–2253，“固定零测集外”；`sec:rv-numerical-convergence` | 要求几乎每条实现最终收敛。 | P(lim X_n=X)=1 | 比逐时刻小概率强。 | 已清楚；无。 |
| B08-284 L^p收敛 | 2255–2258，“E\|X_n-X\|^p→0”；`sec:rv-numerical-convergence` | 控制误差幅度的整体p阶量。 | Markov蕴含依概率 | 第5章范数收敛回顾；所有对象需L^p。 | 已清楚；无。 |
| B08-285 均方收敛 | 2255，“p=2”；`sec:rv-numerical-convergence` | 特别关心平方误差。 | 后尖峰二阶矩反例 | 非a.s.自动可得。 | 已回顾且清楚；无。 |
| B08-286 依分布收敛 | 2260–2262，“分布函数连续点”；`sec:rv-numerical-convergence` | 比较规律而非同次实现。 | CDF定义、对称变量例 | 不需同一基础空间，不能任意点逐项要求。 | 已回顾且清楚；无。 |
| B08-287 收敛蕴含链 | 2265–2283，“a.s.⇒P⇒d”；`sec:rv-numerical-convergence` | 明确各保证能推出什么。 | 指示变量DCT及CDF夹逼完整证明 | DCT已补读第3章2350–2463。 | 已清楚；无。 |
| B08-288 Lévy连续性定理 | 2285–2296，“极限在零点连续”；`sec:rv-numerical-convergence` | 特征函数极限转概率分布极限。 | `thm:probability-levy-continuity` | 此处作为外部定理陈述，不伪装已证；零点连续防质量逃逸。 | 陈述可懂；可选补明确文献引用。 |
| B08-289 a.s.不推出均方的尖峰 | 2298–2301，“√n I{U≤1/n}”；`sec:rv-numerical-convergence` | 证明路径接近不能控制高幅值矩。 | E X_n²=1 | 同一U提供逐路径趋零。 | 已清楚；无。 |
| B08-290 依概率不推出a.s.的独立稀有事件 | 2301–2304，“P(A_n)=1/n”；`sec:rv-numerical-convergence` | 区分频繁更换坏事件与固定例外集。 | BC第二条 | 与前例嵌套事件不同。 | 已清楚；无。 |
| B08-291 常数极限的特殊性 | 2306，“依分布收敛到常数”；`sec:rv-numerical-convergence` | 后面Slutsky替换常数的基础。 | X_n=-X对照 | 非退化相同分布不保证两者接近。 | 已清楚；可选CDF两侧夹住常数证明。 |
| B08-292 一致可积 | 2308–2319，“尾部贡献”；`sec:rv-numerical-convergence` | 排除小概率巨值阻止期望交换。 | `def:probability-uniform-integrability` | 与逐个可积、概率有界、共同可积支配不同。 | 已清楚；无。 |
| B08-293 有界截断T_K | 2321–2323，“max{-K,min{x,K}}”；`sec:rv-numerical-convergence` | 将无限尾部和有界主体分开证明。 | 显式连续裁剪函数 | 比权重截断多了负端，目标是极限控制。 | 已清楚；无。 |
| B08-294 依概率收敛的子列判据 | 2323首次，2356再次，“抽出几乎必然收敛的子列”；`sec:rv-numerical-convergence` | 把依概率转换成可用DCT的路径收敛。 | 未陈述／证明；BC已可支持 | 不是从任一依概率列自身a.s.收敛。 | 局部费力；B-021，补可求和阈值抽取。 |
| B08-295 依概率加一致可积推出L¹ | 2321–2326，“每条子列都有进一步子列”；`sec:rv-numerical-convergence` | 给期望交换准确充分条件。 | 截断、Fatou、子列反证路线 | Fatou已补读；子列工具未建。 | 结论清楚；证明补B-021及两端尾误差式。 |
| B08-296 平均质量不消失的尖峰 | 2325–2334，“面积仍是1”；`sec:rv-numerical-convergence` | 可视解释sup_n尾控制失败。 | `fig:probability-vanishing-spikes` | a.s.路径收敛不等于均值收敛；非模拟数据。 | 已清楚；无。 |
| B08-297 概率有界O_P(1) | 2336–2344，“同一常数压小”；`sec:rv-numerical-convergence` | 为渐近随机余项固定量词。 | `def:statistics-probability-order` | 每次实现有限不等于整个序列概率有界。 | 已清楚；无。 |
| B08-298 o_P(1) | 2344–2345，“依概率趋零”；`sec:rv-numerical-convergence` | 简记渐近可忽略余项。 | 明确定义 | 比O_P(1)强，不等于a.s.小o。 | 已清楚；无。 |
| B08-299 带确定尺度的概率阶 | 2345，“X_n/a_n”；`sec:rv-numerical-convergence` | 区分样本量尺度与随机波动。 | O_P(a_n)、o_P(a_n)规则 | a_n正且确定，与第2章确定数列阶不同。 | 已清楚；无。 |
| B08-300 连续映射定理 | 2350–2360，“在X的取值处几乎必然连续”；`sec:rv-numerical-convergence` | 把随机极限传给后续确定变换。 | `thm:rv-continuous-mapping`、倒数例 | a.s./P/d版本各有条件；L²不自动传递。 | 可理解；子列补B-021，弱版明确前指Portmanteau。 |
| B08-301 Slutsky定理 | 2362–2377，“其中c为常数”；`sec:rv-numerical-convergence` | 允许一致估计归一因子和小余项替换。 | `thm:statistics-slutsky` | 两个一般随机极限仍需联合规律。 | 已清楚；可选补联合(X_n,Y_n)⇒(X,c)的说明。 |
| B08-302 标准误 | 2376，“标准误、归一化因子”；`sec:rv-numerical-convergence` | 说明Slutsky的后续统计用途。 | 仅列用途，正式定义在后 | 本科统计常见，但本读者只将此处作为预告。 | 纯预告可懂；无。 |
| B08-303 Delta方法 | 2379–2388，“g在θ处可微”；`sec:rv-numerical-convergence` | 线性化统计变换的缩放误差。 | `thm:statistics-delta-method`及log例 | 当前仅一维标量版本。 | 已清楚；无。 |
| B08-304 依分布收敛推出概率有界 | 2347声明、2398–2405证明，“闭集上界”；`sec:rv-numerical-convergence` | 为Taylor余项乘积控制提供有界尺度。 | 闭集概率估计 | Portmanteau在后明确给出，不把其当已证。 | 可跟上；可选把通用闭集定理前置。 |
| B08-305 o_P乘O_P规则 | 2406–2417，“联合界”；`sec:rv-numerical-convergence` | 证明随机小余项乘有界量仍消失。 | η/M与M两事件 | 不要求两变量独立。 | 已清楚；无。 |
| B08-306 随机Taylor余项 | 2420–2429，“r_n=o_P(1)”；`sec:rv-numerical-convergence` | 将确定点可微性用于一致估计点。 | 显式展开、Slutsky | 应在差为0处任定余项；不影响结论。 | 已清楚；无。 |
| B08-307 退化一阶Delta极限 | 2432–2436，“g′(θ)=0”；`sec:rv-numerical-convergence` | 防止把零导数误判为定理失效。 | log方差与零导数两种情况 | 要非退化新尺度才需高阶，不是原结论错误。 | 已清楚；无。 |

## 弱收敛与聚合极限

节标签：`sec:rv-weak-convergence`，2485行起`sec:rv-aggregate-limits`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-308 概率测度弱收敛 | 2442–2447，“每个有界连续实函数”；`sec:rv-weak-convergence` | 统一向量、路径及耦合分布比较。 | `def:information-weak-measure-convergence` | 不同于固定测度下函数弱收敛；实数上与CDF等价。 | 已清楚；可选直提与第5章弱收敛对象不同。 |
| B08-309 有界连续测试函数 | 2444–2447，“比较分布的探针”；`sec:rv-weak-convergence` | 同时排除位置不连续与远尾过度放大。 | 逐项解释连续、有界的职责 | 不允许任意事件指标代入。 | 已清楚；无。 |
| B08-310 弱收敛不保所有事件概率 | 2447，“δ_(1/n)⇒δ₀”；`sec:rv-weak-convergence` | 显示测试函数限制实际必要。 | 集合{0}概率0与1 | 极限质量在边界时会变。 | 已清楚；无。 |
| B08-311 Portmanteau闭集上界 | 2449–2452、2461，“limsup P_n(C)≤P(C)”；`sec:rv-weak-convergence` | 让弱收敛转可用事件界。 | `thm:rv-portmanteau`、h_k距离函数逼近 | 不是闭集概率必收敛。 | 已清楚；无。 |
| B08-312 Portmanteau开集下界 | 2453、2461，“liminf P_n(G)≥P(G)”；`sec:rv-weak-convergence` | 配合闭集夹逼事件概率。 | 取补集推导 | 方向与闭集相反。 | 已清楚；无。 |
| B08-313 连续集／零边界质量 | 2454，“P(∂A)=0”；`sec:rv-weak-convergence` | 给事件概率真正收敛的条件。 | 内部与闭包夹逼 | 边界条件针对极限P，不是每个P_n。 | 已清楚；无。 |
| B08-314 下半连续成本 | 2455，“非负下半连续c”；`sec:rv-weak-convergence` | 无界成本仍保极限单向下界。 | 前第4章139–178已读 | 概念已回顾，度量空间序列定义同样成立。 | 已清楚；无。 |
| B08-315 弱极限积分下界 | 2455–2461，“递增…有界连续函数逼近”；`sec:rv-weak-convergence` | 为后最优耦合存在提供代价下界。 | 先固定逼近取弱极限再MCT | 不等于任意无界函数积分交换。 | 陈述可懂；可选给下确界卷积逼近或引文。 |
| B08-316 紧概率测度 | 2464–2467，“紧集外小于ε”；`sec:rv-weak-convergence` | 将几乎全部质量留在紧区域。 | `def:information-tightness` | 与某个取值空间本身紧不同。 | 已清楚；无。 |
| B08-317 一致紧族 | 2468–2475，“同一个紧集”；`sec:rv-weak-convergence` | 防止一族分布逐次逃向远处。 | δ_n各自紧却不一致紧 | 统一量词关键，非逐测度分别选集。 | 已清楚；无。 |
| B08-318 Prokhorov定理／相对弱序列紧 | 2471–2475，“每个序列…子列”；`sec:rv-weak-convergence` | 提供概率分布极限存在机制。 | `thm:rv-prokhorov` | 可抽取不等于已识别唯一极限，Polish条件。 | 陈述可懂；可选补引用来源。 |
| B08-319 矩界给有限维紧性 | 2477–2483，“闭球紧”；`sec:rv-weak-convergence` | 将概率尾界接回几何紧性。 | Markov C/R^p | 无限维闭有界不紧，前章682–756已核对。 | 已清楚；无。 |
| B08-320 强大数定律 | 2488–2497，“E\|X₁\|<∞”；`sec:rv-aggregate-limits` | 回答iid重复平均是否稳定。 | `thm:probability-strong-law-large-numbers`、带噪θ例 | 只需L¹；依赖／自适应数据不可直接套；证明明确引用。 | 已回顾且清楚；无。 |
| B08-321 有限方差弱大数定律 | 2499–2513，“σ²/(nε²)”；`sec:rv-aggregate-limits` | 在当前工具内完整证明较弱结论。 | 方差加和及Chebyshev | 1/n概率不可求和，不能由此宣称a.s.。 | 已清楚；无。 |
| B08-322 iid中心极限定理 | 2520–2529，“√n剩余波动”；`sec:rv-aggregate-limits` | 解释稳定平均周围误差的形状。 | `thm:probability-iid-central-limit` | 0<方差<∞，不同于LLN及有限n精确正态。 | 已回顾且清楚；无。 |
| B08-323 Lindeberg条件 | 2529，“相应Lindeberg条件”；`sec:rv-aggregate-limits` | 提醒非iid数组需要额外条件。 | 尚无定义，作为推广预告出现 | 不用作当前iid定理前提。 | 纯预告；可选写“后续推广另需尾部条件”避免悬置名词。 |
| B08-324 特征函数二阶展开与CLT证明 | 2531–2550，“1-u²/2+o(u²)”；`sec:rv-aggregate-limits` | 独立和乘積趋高斯特征函数。 | n次幂极限、Lévy调用 | 只需二阶矩，可由DCT求两阶导；不需三阶矩。 | 可跟算；可选说明二阶DCT不假设三阶矩。 |
| B08-325 积分估计的逐项极限核验 | 2551–2557，“换成w(X)f(X)”；`sec:rv-aggregate-limits` | 将前面方差算法接到一致性与CLT。 | 一阶／二阶矩分开核对 | 控制系数随机时不直接套固定式；条件Jensen入口见B-013。 | 已清楚；无。 |
| B08-326 自归一化强一致性 | 2559–2570，“分母最终远离零”；`sec:rv-aggregate-limits` | 证明比值虽有偏仍可趋目标。 | 两个SLLN与连续映射 | Z正有限，乘积绝对可积；权重方向正确。 | 已清楚；无。 |
| B08-327 自归一化渐近方差 | 2571–2575，“联合中心极限定理…比值Delta”；`sec:rv-aggregate-limits` | 给随机分母下误差尺度。 | E_Q[w̃²(f-I)²]/Z² | 当地只建立一维CLT和Delta，没有多元版。 | 局部费力；B-022，用中心化标量分子及Slutsky改证。 |

## 随机过程与路径空间

节标签：`sec:rv-paths`、`sec:rv-finite-dimensional-laws`、`sec:rv-path-convergence`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-328 随机过程 | 2585–2588，“索引集T…一族随机变量”；`sec:rv-paths` | 将序列扩展到任意尤其连续时间索引。 | `def:stoch-process` | 每时刻可测不等于联合(t,ω)可测。 | 已清楚；无。 |
| B08-329 连续时间与连续状态 | 2589–2593，“不规定取值连续”；`sec:rv-paths` | 区分索引、状态与路径性质。 | 整数阶梯与实值粗糙路径比较 | 三种“连续”不同。 | 已清楚；无。 |
| B08-330 样本路径及时间截面 | 2590–2598，“固定基础结果”；`sec:rv-paths` | 解释横看实现、纵看同一时刻变量。 | `fig:rv-paths`人工路径图注 | 三条路径不是估计密度，图意明确。 | 已清楚；无。 |
| B08-331 有限维分布 | 2603–2604，“任意有限时刻集合”；`sec:rv-finite-dimensional-laws` | 保存时刻之间依赖而非仅边缘。 | L(X_t₁,…,X_t_m) | “维”是选的坐标数，不是状态维数。 | 已清楚；无。 |
| B08-332 Kolmogorov扩张 | 2606–2612，“存在唯一的概率测度”；`sec:rv-finite-dimensional-laws` | 从相容有限规律得到共同过程。 | `thm:rv-kolmogorov-extension` | 标准Borel已建；不承诺连续路径或联合可测。 | 陈述清楚；无穷乘积对象补B-025。 |
| B08-333 无穷乘积σ代数 | 2608，“E^T的乘积σ代数”；`sec:rv-finite-dimensional-laws` | 指定扩张唯一性究竟在哪些事件上成立。 | 当地无生成族定义 | 第3章只给两个空间的矩形生成，未给任意索引乘积。 | 局部费力；B-025，补有限坐标柱集生成定义。 |
| B08-334 投影相容与重排相容 | 2608–2611，“删掉一个坐标”；`sec:rv-finite-dimensional-laws` | 防止指定的不同维联合规律相互冲突。 | 两时刻直接指定与三时刻边缘比较 | 有序元组额外需重排，不是时刻可交换。 | 已清楚；无。 |
| B08-335 过程版本 | 2614–2617，“每个固定t…概率1”；`sec:rv-finite-dimensional-laws` | 允许各时刻零集修改。 | U随机尖点与零过程 | 不能将不可数个概率1事件直接取交。 | 已清楚；无。 |
| B08-336 不可区分 | 2615–2618，“∀t…概率1”；`sec:rv-finite-dimensional-laws` | 要求一组共同零集外整条路径相同。 | 右连续与可数稠密时刻升级说明 | 强于互为版本；若端点T须一并列入稠密集。 | 已清楚；无。 |
| B08-337 Kolmogorov连续性准则 | 2620–2625，“增量p阶矩”；`sec:rv-finite-dimensional-laws` | 从联合增量控制取得连续版本。 | C\|t-s\|^(1+β)、Brownian四阶矩预告 | 与扩张定理不同；边缘有连续密度不够。 | 陈述可懂；可选补引用，不要求完整证明。 |
| B08-338 Hölder指数 | 2625，“任意小于β/p的正Hölder指数”；`sec:rv-finite-dimensional-laws` | 量化所得路径的粗糙程度。 | 未给\|x(t)-x(s)\|≤C\|t-s\|^α | 前1–7章无定义，只有Hölder不等式及Lipschitz。 | 局部费力；B-023，给路径条件与随机常数。 |
| B08-339 连续路径空间C([0,T]) | 2629–2631，“一致距离”；`sec:rv-path-convergence` | 把整条连续函数作随机取值对象。 | sup距离显式式 | 第5章连续函数范数空间背景可回用；本处Polish另声明。 | 已清楚；无。 |
| B08-340 右连续有左极限路径D([0,T]) | 2632，“右连续且有左极限”；`sec:rv-path-convergence` | 容纳跳跃轨迹。 | 与C及后Poisson预告比较 | 路径可跳，但非任意不规则函数。 | 已清楚；无。 |
| B08-341 Skorokhod J₁收敛 | 2632–2638，“跳跃时刻略微错开”；`sec:rv-path-convergence` | 允许时间微调后比较跳跃轨迹。 | 两个sup趋零、递增连续双射λ_n | 连续极限时同一致收敛；不任意重排时间。 | 已清楚；无。 |
| B08-342 有限维收敛不足路径收敛 | 2640–2646，“越来越窄的尖峰”；`sec:rv-path-convergence` | 解释为何还需路径紧性。 | 峰位1/n、宽1/n²、sup=1 | 固定有限截面最终看不到峰。 | 已清楚；无。 |
| B08-343 连续模量w(x,δ) | 2650–2657，“短时振荡”；`sec:rv-path-convergence` | 定量统一控制路径局部起伏。 | 显式sup定义 | 不是单一固定时刻方差。 | 已清楚；无。 |
| B08-344 连续路径紧性与极限识别 | 2648–2665，“初值一致紧…模连续性”；`sec:rv-path-convergence` | 用概率紧集和有限维规律确定整条路径极限。 | `thm:rv-continuous-path-tightness` | 还需候选连续，非FDD单独足够。 | 陈述清楚；证明缺Ascoli桥接见B-024。 |
| B08-345 Arzelà–Ascoli工具 | 2662，“得到高概率紧集”；`sec:rv-path-convergence` | 将统一幅度／振荡限制转函数集紧致。 | 未陈述或定义等度连续 | 前1–7章未建立，不能只由闭有界推出。 | 局部费力；B-024，给确定性版本及可求和事件构造。 |
| B08-346 跳跃路径紧包含与停时增量 | 2667–2668，“须另证J₁紧性”；`sec:rv-path-convergence` | 限制将连续模量准则误套跳跃。 | 无完整准则，作为替代方法预告 | 停时正式定义紧随下一节；不能当当前可用定理。 | 纯预告可懂；可选明确标延伸工具。 |
| B08-347 缩放随机游走与插值 | 2670–2671，“S_k/√n…线性插值”；`sec:rv-path-convergence` | 把离散累计量变成连续路径对象。 | iid零均值单位方差、网格k/n | 线性与阶梯插值落在不同路径空间。 | 已清楚；无。 |
| B08-348 Donsker定理 | 2672–2673，“弱收敛到标准Brownian运动”；`sec:rv-path-convergence` | 预告CLT的路径版需要额外紧性。 | 明确Brownian定义后文，非只改t | 作为引用结果可读；不能据单时刻CLT自证。 | 预告可懂；可选补来源。 |

## 历史信息与条件依赖

节标签：`sec:stoch-martingales-stopping-sequential-concentration`、`sec:rv-markov`、`sec:rv-martingales`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-349 滤过 | 2679–2687，“随时间增长的信息”；`sec:stoch-martingales-stopping-sequential-concentration` | 把可用历史写成可测事件族。 | `def:stoch-filtration-adaptation-predictability` | 子σ代数嵌套，不是状态取值增大。 | 已清楚；无。 |
| B08-350 适应过程 | 2688–2689，“时刻t已经可知”；`sec:stoch-martingales-stopping-sequential-concentration` | 保证当前变量不需要未来信息。 | X_t对F_t可测 | 不等于可提前一步决定。 | 已清楚；无。 |
| B08-351 可预测过程 | 2689–2692，“第t次新噪声到来之前”；`sec:stoch-martingales-stopping-sequential-concentration` | 为历史选择的系数排除偷看新噪声。 | H_t对F_(t-1)可测 | 可随机，与适应相差一个时间步；当前为离散定义。 | 已清楚；无。 |
| B08-352 停时 | 2694–2699，“足以判断是否已经停止”；`sec:stoch-martingales-stopping-sequential-concentration` | 允许依历史停止且不看未来。 | `def:stoch-stopping-time`、最后达最大值非例 | 允许∞；不是任何随机时刻。 | 已清楚；无。 |
| B08-353 Markov性质／Markov链 | 2705–2717，“保存了预测下一步所需…信息”；`sec:rv-markov` | 限定完整条件分布只需当前状态。 | `def:stoch-markov-chain` | 不代表过去毫无影响，也不只是条件均值相同。 | 已清楚；无。 |
| B08-354 时间齐次 | 2718–2725，“所有t…同一个概率核”；`sec:rv-markov` | 区分机制不变与分布不变。 | `def:stoch-time-homogeneous-chain` | 非平稳边缘保证。 | 已清楚；无。 |
| B08-355 核对函数的作用Pf | 2727–2730，“∫f(z′)P(z,dz′)”；`sec:rv-markov` | 把下一步分布换成下一步平均。 | 显式定义 | 概率核两条件已于本章前部建立。 | 已清楚；无。 |
| B08-356 概率核复合 | 2731–2737，“先按P…再按Q”；`sec:rv-markov` | 表达多步演化。 | (PQ)(z,B)积分式 | 复合顺序与转移步骤明确，非逐点相乘。 | 已清楚；无。 |
| B08-357 核幂P^m | 2737–2744，“P⁰…指示函数”；`sec:rv-markov` | 将齐次一步规则推进多步。 | 归纳定义 | P⁰是保持当前位置的恒等核。 | 已清楚；无。 |
| B08-358 Chapman–Kolmogorov关系 | 2739–2750，“塔式性质”；`sec:rv-markov` | 验证多步拆分相容。 | `eq:stoch-chapman-kolmogorov`及中间状态积分 | Markov与齐次条件都已列。 | 已清楚；无。 |
| B08-359 平稳分布 | 2752–2766，“保持…分布”；`sec:rv-markov` | 找一步演化后不变的规律。 | `eq:stoch-stationary-distribution`、恒等核反例 | 保持目标不等于从任意初态到达目标。 | 已清楚；无。 |
| B08-360 细致平衡 | 2769–2781，“概率流量正反相等”；`sec:rv-markov` | 给平稳分布可核验证书。 | `eq:stoch-detailed-balance`、三态单向环反例 | 足以平稳但非必要，不等于遍历。 | 已清楚；无。 |
| B08-361 状态行动轨迹模型 | 2783–2789，“行动只按当前状态”；`sec:rv-markov` | 将历史密度比应用到受行动影响的过程。 | τ=(s₀,a₀,…,s_T)、链式分解 | π此处是行动核，和上一段平稳分布同字母但作用明确。 | 已清楚；可选提醒符号角色切换。 |
| B08-362 轨迹密度比 | 2790–2799，“公共因子相消”；`sec:rv-markov` | 比较目标与采样策略的路径规律。 | `eq:probability-trajectory-likelihood-ratio` | 同初始、同环境且绝对连续；连乘有限不保低方差。 | 已清楚；连续状态可选重申共同参考密度。 |
| B08-363 鞅 | 2804–2811，“条件平均等于当前”；`sec:rv-martingales` | 描述给定历史无法预期增益的累计量。 | `eq:stoch-martingale-definition` | 可积、适应；不同于Markov完整分布约束。 | 已清楚；无。 |
| B08-364 鞅差 | 2811–2824，“排除…可利用的条件平均”；`sec:rv-martingales` | 为累计误差分离新噪声。 | `eq:stoch-martingale-difference` | 无条件零均值不够，也不要求独立。 | 已清楚；无。 |
| B08-365 超鞅 | 2816，“≤M_(t-1)”；`sec:rv-martingales` | 允许有向下条件漂移。 | 定义内方向明确 | 仍可积适应，不是每条路径单调下降。 | 已清楚；可选直说非逐路径单调。 |
| B08-366 次鞅 | 2816，“≥”；`sec:rv-martingales` | 对应向上条件漂移。 | 定义内显式不等号 | 与超鞅不等号相反。 | 已清楚；无。 |
| B08-367 连续时间鞅版本 | 2818–2821，“任意0≤s≤t”；`sec:rv-martingales` | 为后计数、Brownian过程准备。 | E[M_t\|F_s]=M_s | 不可只检查相邻整数；仍需可积适应。 | 已清楚；无。 |
| B08-368 自然滤过 | 2828–2830，“σ(ε₁,…,ε_t)”；`sec:rv-martingales` | 具体化逐步观测产生的信息。 | 公平游走例，后3134称自然滤过 | 不包含未来或外部额外信号。 | 已清楚；可选在2829行就命名。 |
| B08-369 可预测下注／鞅变换 | 2832–2846，“H_t ε_t可积”；`sec:rv-martingales` | 展示历史自适应仍不改变条件零均值。 | `ex:stoch-predictable-betting`完整条件计算 | 可预测不自动可积；偷看新噪声破坏等式。 | 已清楚；无。 |
| B08-370 上穿次数及上穿不等式 | 2850–2868，“从不高于a到不低于b”；`sec:rv-martingales` | 通过反复盈利策略排除永久振荡。 | U_n[a,b]、交易收益与未完成负部 | 非负超鞅收益期望≤0；有限时刻有界持仓可积。 | 已清楚；无。 |
| B08-371 非负超鞅收敛 | 2869–2874，“有限随机变量”；`sec:rv-martingales` | 由有限上穿与Fatou得到路径极限。 | 有理区间可数、E L_t≤E L₀ | 不保证均值保留；UI另需。 | 已清楚；无。 |
| B08-372 L²有界鞅收敛 | 2876–2882，“a.s.且在L²中”；`sec:rv-martingales` | 为有符号噪声提供另一收敛入口。 | `thm:rv-l2-martingale-convergence` | 统一二阶矩界，非逐项有限就够。 | 已清楚；无。 |
| B08-373 鞅增量L²正交 | 2884–2889，“E[M_n(M_m-M_n)]=0”；`sec:rv-martingales` | 使二阶矩差就是均方距离。 | 显式勾股式 | 用条件均值，不是增量独立。 | 已清楚；无。 |
| B08-374 Doob L²最大不等式 | 2890–2900，“E(Y*)²≤4E Y_N²”；`sec:rv-martingales` | 从终点矩控制整段最大波动。 | 首越水平分解、积分、Cauchy–Schwarz | 尾积分可由前Tonelli推出；非只控固定时刻。 | 可跟上；可选补积分权重2 da与尾积分等式。 |
| B08-375 可求和子列提升整列a.s.收敛 | 2901–2907，“sup_(m≥n)”；`sec:rv-martingales` | 防止只证明选中子列收敛。 | 2^(-4k)与阈值2^(-k)、BC | 最大尾波动保证整列Cauchy，非单点子列结论。 | 已清楚；无。 |
| B08-376 终值的条件期望表示 | 2881、2908–2909，“M_n=E[M_∞\|F_n]”；`sec:rv-martingales` | 表示每步是终值在现有信息下的平均。 | 事件积分取m极限 | L²⇒L¹保证取极限，非任意a.s.鞅都有此表示。 | 已清楚；无。 |

## 固定时刻与任意时刻

节标签：`sec:rv-martingales`下累计误差、`sec:rv-fixed-time`、`sec:rv-anytime`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-377 可预测二次变差 | 2915–2923，“新增量到来之前…条件方差”；`sec:stoch-martingales-stopping-sequential-concentration` | 序贯累计实际噪声尺度。 | `eq:stoch-predictable-quadratic-variation` | 需平方可积鞅差，零条件均值使二阶矩=条件方差。 | 已清楚；无。 |
| B08-378 实现二次变差 | 2924–2925，“Σ X_s²”；`sec:stoch-martingales-stopping-sequential-concentration` | 区分事前条件规模与事后观察平方和。 | 两个和的直接比较 | Freedman不能不说明地换成此量。 | 已清楚；无。 |
| B08-379 Azuma–Hoeffding界 | 2932–2943，“确定常数a_t,b_t”；`sec:rv-fixed-time` | 把有界独立和推广鞅差。 | `eq:stoch-azuma-hoeffding` | 不需独立，条件均值与范围足够。 | 已清楚；无。 |
| B08-380 条件Hoeffding与塔式迭代 | 2945–2981，“反复使用塔式性质”；`sec:rv-fixed-time` | 不靠独立乘積仍控制指数矩。 | 单步条件界、累计MGF、优化 | 原Hoeffding证明可条件化；尺度仍最坏范围。 | 已清楚；原引理缩放补B-018。 |
| B08-381 Doob揭示鞅 | 2982–2989，“逐步揭示输入”；`sec:rv-fixed-time` | 为一般数据函数构造鞅差。 | Z_i=E[f\|X₁,…,X_i] | 和函数特殊结构不必；塔式给鞅。 | 已清楚；无。 |
| B08-382 McDiarmid条件范围证明 | 2990–3007，“同一未来分布”；`sec:rv-fixed-time` | 回答前面有界差如何生成指数界。 | 积分未来、区间长度c_i、完整优化 | 独立在未来积分处使用，历史变端点但长度固定。 | 已清楚；无。 |
| B08-383 有界停时可选停止 | 3013–3020，“τ≤n”；`sec:rv-anytime` | 说明观察历史后有界停止仍保鞅均值。 | `thm:stoch-bounded-optional-stopping` | 随机停止不等于任意停止无偏。 | 已清楚；无。 |
| B08-384 停止和的可预测指示表示 | 3022–3044，“I{τ≥t}”；`sec:rv-anytime` | 把随机长度改固定有限和合法取期望。 | {τ≥t}∈F_(t-1)及塔式 | 停时条件在此发挥作用。 | 已清楚；无。 |
| B08-385 无界停时的附加条件 | 3046–3048，“一致可积…Eτ<∞”；`sec:rv-anytime` | 明确有界停时结论扩展边界。 | 列三类充分条件 | 本处只声明，不假装前有限和证明涵盖无界。 | 可理解；可选给停止族的UI确切对象。 |
| B08-386 首达1的随机游走反例 | 3048–3050，“a.s.有限…Eτ=∞”；`sec:rv-anytime` | 说明a.s.有限停时不足保均值。 | S_τ=1但缺首达性质推导 | 还未建游走返回／首达概率。 | 局部费力；B-026，给两吸收端点计算或准确来源。 |
| B08-387 Ville不等式 | 3052–3060，“sup_t L_t≥1/δ”；`sec:rv-anytime` | 提供任意时刻同时越界概率控制。 | `eq:stoch-ville`、首越停时证明略述 | 上确界未必在某时刻达到；超鞅只保≤。 | 局部费力；B-027，补a′↑a的极限及≤版停止。 |
| B08-388 反演检验得到置信集合 | 3060，“随时间更新”；`sec:rv-anytime` | 预告序贯统计用途。 | 后统计推断建立，不在此代替定义 | 纯预告，固定n区间不可直接重复窥视。 | 预告清楚；无。 |
| B08-389 标量Freedman界 | 3062–3079，“存在t…V_t≤v”；`sec:rv-anytime` | 用条件方差改善范围型鞅界。 | `eq:stoch-freedman` | 是时刻同时但附固定方差阈v，不等于随手代随机v。 | 已清楚；无。 |
| B08-390 条件Bernstein指数超鞅 | 3081–3111，“exp{λS_t-ψ(λ)V_t}”；`sec:rv-anytime` | 构造可停止的非负证据过程。 | 指数级数标量界、条件均值消一阶 | 可预测V使每步条件抵消；λ固定在(0,3/b)。 | 已清楚；无。 |
| B08-391 首次联合越界的停时论证 | 3113–3131，“S_t≥x,V_t≤v”；`sec:rv-anytime` | 完成Freedman同时界。 | E L_(τ∧n)≤1、越界下界及λ优化 | 不用把固定时刻n机械换τ。 | 已清楚；无。 |
| B08-392 Freedman恢复Bernstein | 3133–3144，“自然滤过…V_n确定”；`sec:rv-anytime` | 核对一般序贯界含独立特例。 | 同常数指数式 | 独立方差和不随机；条件方差可随机。 | 已清楚；无。 |
| B08-393 方差几何分段 | 3146–3149，“分配失败概率”；`sec:rv-anytime` | 从固定方差阈值构造自适应边界。 | 操作步骤有白话，未给完整边界 | 作为方法预告，非直接宣称V_t代v合法。 | 预告清楚；无。 |
| B08-394 混合不同指数参数 | 3148，“混合不同λ”；`sec:rv-anytime` | 提示另一任意时刻边界构造。 | 后向量高斯混合是具体实例 | 混合要保非负超鞅，不是任意择优参数。 | 预告清楚；无。 |

## 自适应设计与自归一化

节标签：`sec:stoch-self-normalized-adaptive-design`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-395 自适应线性观测 | 3151–3158，“查询带有特征x_t”；`sec:rv-anytime` | 把标量累计扩展为历史选择方向上的读数。 | `eq:stoch-adaptive-linear-observation` | 特征可预测，非当前噪声揭晓后选择。 | 已清楚；无。 |
| B08-396 条件次高斯噪声 | 3159–3172，“对每个γ…几乎必然”；`sec:rv-anytime` | 为历史依赖噪声给统一指数矩控制。 | `eq:stoch-conditional-subgaussian` | 比无条件次高斯强，蕴含条件中心化。 | 陈述清楚；随机参数使用补B-028。 |
| B08-397 向量累计噪声 | 3174–3176，“Σx_s η_s”；`sec:rv-anytime` | 保存不同特征方向的噪声贡献。 | `eq:stoch-vector-sum-design` | 标量噪声乘向量，不需向量本身独立。 | 已清楚；无。 |
| B08-398 正则化设计矩阵 | 3178–3193，“从未…方向只剩初始正则化”；`sec:rv-anytime` | 度量各方向观测信息。 | V_t=V₀+Σx_sx_sᵀ | V₀≻0保证初始可逆；可选显说V₀固定。 | 已清楚；无。 |
| B08-399 向量鞅的可积条件 | 3182–3191，“E‖x_tη_t‖<∞”；`sec:rv-anytime` | 防止可预测被误当成可积。 | 条件均值逐坐标为0 | 自归一集中本身只需指数过程可积，不必先将S叫鞅。 | 已清楚；无。 |
| B08-400 设计逆矩阵范数 | 3193–3201，“信息越多…权重越小”；`sec:rv-anytime` | 按各方向实际观测量归一化噪声。 | ‖S_t‖_(V_t⁻¹)显式二次式 | 与权重比值自归一化对象不同。 | 已清楚；无。 |
| B08-401 向量自归一化集中界 | 3204–3220，“所有t同时”；`sec:rv-anytime` | 统一控制自适应多方向累计误差。 | `eq:stoch-vector-self-normalized-bound` | 不是固定特征或独立特征结论；行列式与R、δ各有角色。 | 已清楚；证明参数补B-028。 |
| B08-402 可预测随机指数参数 | 3223–3236，“取γ=⟨u,x_t⟩”；`sec:rv-anytime` | 为每个方向构造一阶指数补偿。 | 显式条件指数式 | 原假设逐确定γ a.s.，须由简单逼近合法推广。 | 局部费力；B-028，补条件Fatou的一句桥接。 |
| B08-403 固定方向指数过程 | 3237–3247，“L_t(u)”；`sec:rv-anytime` | 将各步条件界累积为非负超鞅。 | 展开二次型补偿 | V_t−V₀可半正定，仅作为半范数记号；无求逆。 | 已清楚；无。 |
| B08-404 高斯混合指数超鞅 | 3249–3253，“对L_t(U)积分”；`sec:rv-anytime` | 避免只控制预先固定的一个方向。 | U~N(0,R⁻²V₀⁻¹)、非负条件Tonelli | U独立于数据；混合不是数据后选择u。 | 已清楚；无。 |
| B08-405 高斯配方及行列式比 | 3253–3276，“归一化常数…中心移动”；`sec:rv-anytime` | 将混合过程转成可解释矩阵半径。 | 显式L̄_t、Ville取对数 | 行列式不是访问次数之和，重复／新方向贡献不同。 | 已清楚；可选二维重复与正交方向数值例。 |

## 平稳性与随机游走

节标签：`sec:rv-stationarity`、`sec:rv-random-walk`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-406 严格平稳过程 | 3282–3287，“有限维分布…平移”；`sec:rv-stationarity` | 将核保持分布扩展到完整过程规律。 | `def:stoch-stationary-process` | 同一边缘不等于联合平移不变。 | 已清楚；无。 |
| B08-407 平稳初始的齐次链 | 3288–3299，“πP=π”；`sec:rv-stationarity` | 证明平稳分布何时生成平稳过程。 | 联合链式式、积分掉起点证明 | 需从π启动且核齐次，不只某时刻等于π。 | 已清楚；无。 |
| B08-408 二阶平稳／弱平稳 | 3300–3305，“协方差只依赖时间差”；`sec:rv-stationarity` | 只用二阶摘要描述时间不变性。 | `def:rv-second-order-stationary` | 需二阶矩；严格平稳反推须有该矩。 | 已清楚；无。 |
| B08-409 弱平稳不推出严格平稳 | 3305，“偶数高斯…奇数±1”；`sec:rv-stationarity` | 用边缘交替显示二阶摘要漏信息。 | 均值0、方差1、跨时刻协方差0 | 联合高斯例外，均值协方差决定全部规律。 | 已清楚；无。 |
| B08-410 平稳增量 | 3306、3309，“增量却可平稳”；`sec:rv-stationarity` | 区分累计过程不平稳与噪声规律不变。 | 随机游走／Brownian预告 | 后Poisson与Brownian定义细化，当前可由游走增量理解。 | 可理解；可选显式说等长时间段增量同分布。 |
| B08-411 一般随机游走 | 3313–3322，“iid增量…累计和”；`sec:rv-random-walk` | 逐项核对Markov、鞅和非平稳可并存。 | 均值、方差、min(m,n)协方差 | 位置共享增量非独立，减漂移后才中心化鞅。 | 已清楚；无。 |
| B08-412 ±1游走漂移与方差 | 3323–3326，“p=0.6”；`sec:rv-random-walk` | 将抽象过程落到可算路径尺度。 | 十步均值2、方差9.6 | LLN控制S_n/n，CLT控制中心缩放，路径定理另需紧性。 | 已清楚；无。 |

## Markov链的长期行为

节标签：`sec:stoch-markov-long-run-average`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-413 两状态链的平稳流与非平稳启动 | 3334–3353，“经过一段时间才接近平稳”；`sec:stoch-markov-long-run-average` | 用同一矩阵区分机制、初态、极限。 | `ex:stoch-two-state-chain`、跨状态流1/15、q_t递推 | 平稳分布及细致平衡已回顾；不推出独立。 | 已清楚；无。 |
| B08-414 有限链不可约性 | 3356–3362，“任意状态i,j”；`sec:stoch-markov-long-run-average` | 排除被初始区域永久限制。 | `def:stoch-finite-irreducibility-period`、两状态例 | P的幂已建；m依赖状态对。 | 已清楚；无。 |
| B08-415 状态周期 | 3358–3359，“返回步数…gcd”；`sec:stoch-markov-long-run-average` | 判断返回是否被固定节律限制。 | 确定交替链周期2 | gcd是本科整数背景；不是最短返回时间。 | 已清楚；无。 |
| B08-416 非周期性 | 3360，“共同周期为1”；`sec:stoch-markov-long-run-average` | 排除分布持续轮转。 | 非周期两状态与交替链对照 | 不可约性和非周期性不同，前者不排除交替。 | 已清楚；无。 |
| B08-417 封闭常返类 | 3362、3377，“至少一个封闭常返类”；`sec:stoch-markov-long-run-average` | 为有限链返回结论提供结构理由。 | 未定义类和封闭；只有不可约直觉 | 后图论不能倒补此处；与整个链不可约不同。 | 局部费力；B-029，补互达等价类及无流出定义。 |
| B08-418 状态可达 | 3373，“存在m≥0”；`sec:stoch-markov-long-run-average` | 将不可约的成对条件单独命名。 | 与3358相同的核幂条件 | 已回顾；可达通常有方向，不等于互达。 | 已清楚；可选直说方向。 |
| B08-419 首次返回时间T_i⁺ | 3374，“inf{t≥1:Z_t=i}”；`sec:stoch-markov-long-run-average` | 对访问间隔作随机长度切分。 | 起点i、排除t=0 | 与首达时间及已建停时相接；允许∞。 | 已清楚；无。 |
| B08-420 常返状态 | 3376，“返回概率1”；`sec:stoch-markov-long-run-average` | 区分可到达与必然回来。 | 定义式、后一般状态对照 | 不等于返回均值有限。 | 已清楚；有限均值证明桥接见B-029。 |
| B08-421 游程 | 3378，“一次访问…下一次返回前”；`sec:stoch-markov-long-run-average` | 将相关路径切成可用iid大数定律的单位。 | L_k长度、R_k访问次数 | 不包含终点以免两次计数；非固定长度批次。 | 已清楚；无。 |
| B08-422 强Markov性 | 3378，“随机时刻之后仍成立”；`sec:stoch-markov-long-run-average` | 使返回后可重新启动同样的条件规律。 | 对停时取值分事件验证的离散说明 | 强于只写确定t条件，非连续时间无条件推广。 | 解释足够；可选列{T=m}上的一次条件式。 |
| B08-423 游程奖励比极限 | 3379–3387，“累计比值…不是单次随机比值”；`sec:stoch-markov-long-run-average` | 识别长期访问比例。 | ΣR_k/ΣL_k→ER/EL | iid LLN已建；等于π以及任意时间截断待接。 | 局部费力；B-029，证明归一化访问向量不变并控制末段。 |
| B08-424 平稳概率与平均返回时间 | 3388–3389，“π_i=1/E_iT_i⁺”；`sec:stoch-markov-long-run-average` | 将稳态质量解释成返回频率。 | 每游程访问i一次 | 需先证有限平均返回与奖励比识别。 | 局部费力；同B-029，不能仅凭常返推出。 |
| B08-425 特征模态与周期振荡 | 3390–3394，“单位圆上持续振荡”；`sec:stoch-markov-long-run-average` | 给矩阵侧直觉说明分布与平均差异。 | 第二特征值0.7及交替链 | 第6章检索无Perron理论；当地是证明路线说明而非完整证明。 | 可读；可选注明有限链谱结论引用来源。 |
| B08-426 总变差距离 | 3402–3408，“比较所有事件概率”；`sec:stoch-markov-long-run-average` | 明确逐时刻分布收敛口径。 | sup_B绝对概率差 | 新定义已就地给出，后章前指不承担当前定义。 | 已清楚；无。 |
| B08-427 有限链分布收敛 | 3396–3401，“对每个初始状态”；`sec:stoch-markov-long-run-average` | 指明不可约加非周期的作用。 | `eq:stoch-finite-chain-distribution-convergence`、q_t解析式 | 不是只要求π存在；一般速率未给。 | 已清楚；无。 |
| B08-428 遍历时间平均 | 3409–3416，“即使有周期”；`sec:stoch-markov-long-run-average` | 相关样本仍可识别均值。 | `eq:stoch-markov-ergodic-average` | 有限不可约且任意实函数，独立LLN不能直接套逐时刻样本。 | 陈述清楚；证明入口补B-029。 |
| B08-429 周期链平均与边缘分离反例 | 3417–3419，“平均仍趋向1”；`sec:stoch-markov-long-run-average` | 反驳两种收敛等同。 | 0,2确定交替 | 每步边缘点质量，时间占比各半。 | 已清楚；无。 |
| B08-430 中心化特征函数关系 | 3421–3428，“0.7 Ỹ_t”；`sec:stoch-markov-long-run-average` | 从核作用计算多步相关。 | `eq:stoch-two-state-eigenfunction`与塔式迭代 | 此处是核的特征函数，不是概率Fourier特征函数。 | 已清楚；可选提醒同名对象不同。 |
| B08-431 两状态自相关几何衰减 | 3429–3435，“Corr=0.7^k”；`sec:stoch-markov-long-run-average` | 显示边缘已平稳仍非独立。 | `eq:stoch-two-state-autocorrelation` | 需要平稳启动；方差正可约消。 | 已清楚；无。 |
| B08-432 φ不可约性 | 3437–3445，“正测度集合…正概率”；`sec:stoch-markov-long-run-average` | 一般空间单点零概率，改用集合可达。 | `def:stoch-harris-recurrence` | 参考测度非零；不要求精确击中每个点。 | 有白话、无具体连续链例；可理解，可选加独立核例。 |
| B08-433 Harris常返性 | 3446–3447，“概率1…无穷多个t”；`sec:stoch-markov-long-run-average` | 将有机会访问加强为反复必然访问。 | 3452–3454量词再解释 | 比φ不可约强；事件对每个B分别a.s.。 | 已清楚；无。 |
| B08-434 正Harris常返性 | 3447，“再要求存在不变概率”；`sec:stoch-markov-long-run-average` | 给可归一化长期目标。 | 定义及可积性边界 | 与常返本身、仅有不变概率不同。 | 条件清楚；无具体算例，可选补同一核例。 |
| B08-435 一般状态遍历大数定律 | 3449–3456，“函数必须π可积”；`sec:stoch-markov-long-run-average` | 把时间均值识别推广到连续状态。 | 明确引用有限式及Kallenberg来源 | 局部可积不够；这里只声明不假装有限矩阵已证明。 | 已清楚；无。 |
| B08-436 一般状态周期分割 | 3458–3461，“A_i轮流进入下一集”；`sec:stoch-markov-long-run-average` | 把返回步数节律改为正概率区域轮转。 | 可测分割、全π概率、mod d | 正Harris框架中的等价表述，不任意状态空间泛化。 | 已清楚；无。 |
| B08-437 一般状态TV收敛 | 3462–3465，“任意初态”；`sec:stoch-markov-long-run-average` | 明确比时间平均多需什么。 | 标准Borel、正Harris、非周期、来源 | 不承诺统一速率。 | 已清楚；无。 |
| B08-438 几何遍历性 | 3467–3477，“C(z)r^t”；`sec:stoch-markov-long-run-average` | 将存在极限加强为几何速度控制。 | `def:stoch-geometric-ergodicity` | 共同r而C依初态；不等于统一遍历，也不自动CLT。 | 已清楚；无。 |
| B08-439 混合速度 | 3485–3486，“忘记初态的快慢”；`sec:stoch-markov-long-run-average` | 从长期是否成立转到预算。 | 后混合时间定义 | 不等于特定f的自相关速度。 | 已清楚；无。 |
| B08-440 最坏初态混合时间 | 3487–3499，“d(t)…sup_z”；`sec:stoch-markov-long-run-average` | 定量达到TV容差所需步数。 | `def:stoch-finite-mixing-time`、空集∞ | 当前只定义有限链；未收敛可为∞。 | 已清楚；无。 |
| B08-441 平稳观测方差与自相关函数 | 3501–3508，“0<σ_f²<∞”；`sec:stoch-markov-long-run-average` | 为均值精度固定归一化尺度。 | ρ_f(k)=Corr(f(Z₀),f(Z_k)) | 已回顾相关系数；依赖所选f，常量例另排除。 | 已清楚；无。 |
| B08-442 相关样本均值方差 | 3509–3522，“1-k/n”；`sec:stoch-markov-long-run-average` | 精确累计各时间差的协方差。 | `eq:stoch-markov-average-variance` | 平稳性使同间隔相同，独立只是ρ=0特例。 | 已清楚；可选写每个间隔有n-k对。 |
| B08-443 积分自相关时间 | 3523–3529，“1+2Σρ”；`sec:stoch-markov-long-run-average` | 把渐近方差放大归成一个数。 | 绝对可和条件、17/3算例 | 为非负方差比，不是事件真实等待时间。 | 已清楚；无。 |
| B08-444 自相关有效样本量 | 3529–3531，“n/τ_f”；`sec:stoch-markov-long-run-average` | 与独立样本均值精度换算。 | `fig:stochastic-mixing-variance`与3n/17 | 不同于重要性权重ESS；τ=0不套比值。 | 已清楚；无。 |
| B08-445 负自相关与ESS大于n | 3539–3541，“不是…样本条数”；`sec:stoch-markov-long-run-average` | 防止把精度口径实体化。 | τ_f可小于1的式 | 不表示制造独立观测；初态偏差不属于平稳方差式。 | 已清楚；无。 |

## 计数、跳跃与补偿

节标签：`sec:rv-poisson`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-446 齐次Poisson过程 | 3552–3567，“规定不同窗口间的联合关系”；`sec:rv-poisson` | 从单窗口分布扩展到整个到达过程。 | `def:rv-poisson-process` | 适应、单位跳、右连续、增量独立于给定历史均明确。 | 已清楚；无。 |
| B08-447 独立平稳增量与计数不平稳 | 3568–3570，“平稳性属于增量”；`sec:rv-poisson` | 防止N_t随时间增长与齐次矛盾。 | Poisson(λ(t-s))、扩大滤过警告 | 自然滤过与额外未来信息不可混同。 | 已回顾且清楚；无。 |
| B08-448 短时跳跃概率尺度 | 3572–3580，“概率一阶…幅度始终为一”；`sec:rv-poisson` | 为连续时间跳跃模型建立直觉。 | 0、1、≥2三种概率展开 | O(h²)是概率余量，不是跳幅O(h)。 | 已清楚；无。 |
| B08-449 到达时刻T_k | 3581，“inf{t:N_t≥k}”；`sec:rv-poisson` | 将计数读数转换为等待读数。 | T₁尾概率计算 | 停时背景已建；不是均匀固定网格。 | 已清楚；无。 |
| B08-450 有限活动过程 | 3581–3582，“有限次跳跃”；`sec:rv-poisson` | 保证有限时间的跳跃和逐路径可算。 | N_t有限a.s. | 不意味着全时间只发生有限跳跃。 | 已清楚；无。 |
| B08-451 左极限与跳跃量 | 3583–3584，“ΔN_t=N_t-N_(t-)”；`sec:rv-poisson` | 区分到达前与到达后的值。 | 单位跳路径图 | 右连续仍可有左侧跳差；有限活动使取和明确。 | 已清楚；无。 |
| B08-452 指数等待间隔 | 3586–3603，“同一…机制两个侧面”；`sec:rv-poisson` | 把计数与等待分布接起来。 | T₁尾概率、λ^k exp(-λt_k)联合密度及Jacobian1 | 不只从边缘指数推独立；无记忆性支持反向构造。 | 已清楚；无。 |
| B08-453 Gamma累计等待 | 3604–3608，“等待k次…总时长”；`sec:rv-poisson` | 给Gamma形状参数事件数解释。 | iid指数求和、P(T_k≤t<T_(k+1)) | 速率λ非尺度；Gamma此前已定义。 | 已回顾且清楚；无。 |
| B08-454 复合Poisson过程 | 3610–3614，“Σ_(k≤N_t)J_k”；`sec:rv-poisson` | 每个事件可携带不同量。 | J_k iid且独立于计数 | 跳量可负，与单调单位计数不同。 | 已清楚；无。 |
| B08-455 随机事件数的全方差 | 3615–3620，“λt E J₁²”；`sec:rv-poisson` | 说明标记方差以外还有计数方差。 | 条件均值、全方差及矩条件 | 不是λt Var J₁；本科概率工具已回顾。 | 已清楚；可选列两项相加一行。 |
| B08-456 Poisson过程与Poisson方程 | 3621，“不是同一个对象”；`sec:rv-poisson` | 为同名后续工具划边界。 | 过程到达／核均值校正一句比较 | 方程仅预告，不作为本节前提。 | 纯预告清楚；无。 |
| B08-457 补偿Poisson过程 | 3623–3627，“减去…平均趋势”；`sec:rv-poisson` | 把计数变成条件零均值噪声。 | Ñ_t=N_t-λt、`fig:rv-poisson-compensation` | 补偿不是删掉跳跃。 | 已清楚；无。 |
| B08-458 补偿计数的平方可积鞅 | 3628–3645，“Ñ_t²-λt也是鞅”；`sec:rv-poisson` | 将增量均值及方差联系到鞅工具。 | `thm:rv-compensated-poisson`完整条件展开 | 需相同滤过独立增量；不是任意零均值过程。 | 已清楚；无。 |
| B08-459 跳跃平方和／实现二次变差 | 3653–3659，“[Ñ]_t=N_t”；`sec:rv-poisson` | 记录观察到的实际平方波动。 | 有限跳跃加线性漂移的细分解释 | 与单时刻方差或可预测累计不同。 | 已清楚；无。 |
| B08-460 连续时间可预测补偿括号 | 3657–3660，“⟨Ñ⟩_t=λt”；`sec:rv-poisson` | 用补偿使平方过程成为鞅。 | 条件平方增量定理 | 此处确定连续函数必可预测，未需一般可预测σ代数。 | 已清楚；无。 |
| B08-461 标记补偿的矩与滤过 | 3662–3666，“只揭示已到达标记”；`sec:rv-poisson` | 推广到复合跳量而不偷看未来。 | J≡2时一阶2λ、二阶4λ | 一阶可积给鞅、二阶有限给二次累计。 | 已清楚；无。 |
| B08-462 补偿增量有限和等距 | 3667–3676，“λΣEH_i² Δt_i”；`sec:rv-poisson` | 为随机积分预告可复用的L²结构。 | 确定分割、H_i∈L²(F_(t_i))、正交性 | 当地只证有限和，一般闭包定义准确前指。 | 已清楚；可选补一项交叉项条件期望为零。 |

## 连续波动与高斯函数

节标签：`sec:dynamical-brownian-motion`；高斯过程无独立节标签，用`def:stoch-gaussian-process`定位。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-463 平方根时间缩放 | 3685–3696，“有限非零波动”；`sec:dynamical-brownian-motion` | 选择连续时间极限中非退化增量。 | nΔt=t，与Δt及不缩放比较 | 是方差尺度论证，不单独证明路径极限。 | 已清楚；无。 |
| B08-464 函数型CLT与Brownian极限 | 3698–3699，“不重证…一般弱收敛”；`sec:dynamical-brownian-motion` | 接回前Donsker预告。 | 明确有限方差与插值条件 | 全路径收敛还需紧性，未假称由标量CLT推出。 | 预告清楚；无。 |
| B08-465 标准Brownian运动 | 3701–3713，“路径几乎必然连续”；`sec:dynamical-brownian-motion` | 定义连续而粗糙的基本噪声。 | 四项定义、协方差推导 | 零起点、高斯独立平稳增量及连续版本各独立列出。 | 已清楚；无。 |
| B08-466 相对于滤过的Brownian运动 | 3715–3718，“过去信息不能预见”；`sec:dynamical-brownian-motion` | 为后续历史依赖积分选择合法信息流。 | 适应及增量独立F_s | 比只声明自身增量独立多一项约束。 | 已清楚；无。 |
| B08-467 Brownian协方差核 | 3720–3725，“min(s,t)”；`sec:dynamical-brownian-motion` | 解释位置共享历史而相关。 | `eq:dynamical-brownian-covariance`推导 | 与独立增量不矛盾。 | 已清楚；无。 |
| B08-468 Brownian尺度规律 | 3727–3737，“c^(-1/2)W_ct”；`sec:dynamical-brownian-motion` | 表达不同观察尺度下同一过程律。 | 逐项核对定义 | 同有限维分布，不是同一路径逐点相等。 | 已清楚；无。 |
| B08-469 多维标准Brownian运动 | 3739–3744，“相互独立的实值…组成”；`sec:dynamical-brownian-motion` | 为向量噪声固定协方差基准。 | N(0,(t-s)I_m)、共同滤过 | 各边缘标准不够，分量要联合独立。 | 已清楚；无。 |
| B08-470 矩阵混合与退化扩散 | 3745–3746，“AAᵀ”；`sec:dynamical-brownian-motion` | 连接各向异性及低秩随机增量。 | 协方差显式式 | 扩散此处指混合噪声，完整SDE尚是后文。 | 可理解；可选将“退化扩散”标为预告术语。 |
| B08-471 Brownian不可微性 | 3748–3756，“差商标准差发散”；`sec:dynamical-brownian-motion` | 解释普通微分积分失效的原因。 | 1/√h尺度；3801明确非完整证明 | 固定时刻方差不证明所有时刻不可微；严格结论另声明。 | 已清楚；可选给路径定理准确来源。 |
| B08-472 确定分割二次变差 | 3758–3769，“同一条路径…求和再取极限”；`sec:dynamical-brownian-motion` | 保留细分后仍有的累计平方波动。 | `def:dynamical-quadratic-variation` | 每列确定分割的依概率极限，不是所有分割共同逐路径极限。 | 已清楚；无。 |
| B08-473 Brownian二次变差L²证明 | 3770–3781，“Var Q_n≤2t网格”；`sec:dynamical-brownian-motion` | 使[X]_t=t不只是图上直觉。 | 独立高斯四阶矩、均值t及方差界 | 各增量平方独立，网格不要求等长。 | 已清楚；无。 |
| B08-474 光滑路径与Brownian平方增量 | 3783–3785，“普通…趋零”；`sec:dynamical-brownian-motion` | 对照为何Itô链式公式需二阶项。 | O(Δt)与O_P(√Δt) | 概率阶已于2337–2345定义；非统一确定性路径界。 | 已清楚；无。 |
| B08-475 有限教学折线的证据边界 | 3787–3797，“不…作为…收敛证明”；`sec:dynamical-brownian-motion` | 限制模拟图的解释强度。 | `fig:reader-brownian-quadratic-variation`明确网格及种子 | 路径高低、平方累计及分割尺度不同。 | 已清楚；无。 |
| B08-476 Itô公式预告 | 3785、3800，“保留二阶导数项”；`sec:dynamical-brownian-motion` | 指出本节波动结构的后续用途。 | 非零二次变差 | 当前不介绍公式，后章承担完整定义。 | 纯预告清楚；无。 |
| B08-477 交叉二次变差 | 3804–3812，“增量乘积而非平方”；`sec:dynamical-brownian-motion` | 记录多维噪声共同波动。 | [W^i,W^j]_t=δ_ij t及方差计算 | 不同于固定时刻协方差；独立分量给零极限。 | 已清楚；无。 |
| B08-478 二进分割的a.s.提升 | 3813，“方差界可求和”；`sec:dynamical-brownian-motion` | 区分特定网格的强结论与一般结论。 | Chebyshev加已建BC | 固定终点，不声称所有路径所有分割。 | 已清楚；无。 |
| B08-479 高斯过程 | 3817–3826，“任意…有限联合分布”；`sec:rv-sequences-processes` | 把高斯向量扩展到随机函数。 | `def:stoch-gaussian-process`、F(x)=A+Bx | 索引非必时间，协方差可奇异。 | 已清楚；无。 |
| B08-480 均值函数与协方差函数 | 3820–3825，“m(x)、k(x,x′)”；`sec:rv-sequences-processes` | 用两个确定函数编码全部高斯有限维规律。 | 显式定义、1+xx′算例 | 普通过程的两摘要不决定分布，高斯类才足够。 | 已清楚；无。 |
| B08-481 协方差核正半定 | 3827–3831，“任意有限输入…≥0”；`sec:rv-sequences-processes` | 检验候选函数能否作高斯协方差。 | 有限二次型式、min(s,t)积分平方 | 矩阵PSD已建；不是逐点k非负。 | 已清楚；无。 |
| B08-482 低秩随机线性函数 | 3833–3834，“同两个随机系数”；`sec:rv-sequences-processes` | 解释多点协方差奇异仍合法。 | A+Bx，三点以上矩阵秩≤2 | 与正定密度公式不同；分布可退化。 | 已清楚；无。 |
| B08-483 高斯边缘不保证联合高斯 | 3834，“X,SX…平方相同”；`sec:rv-sequences-processes` | 强调定义的联合量词。 | 独立符号反例、不相关但依赖 | 联合高斯不相关⇒独立已建，不能用边缘代替联合。 | 已清楚；无。 |
| B08-484 由核构造过程及版本条件 | 3835–3840，“有限维分布相容”；`sec:rv-sequences-processes` | 回答合法核如何产生完整随机对象。 | Brownian核平方积分、扩张定理回指 | 路径连续仍需增量矩，不由GP名称保证。 | 已清楚；扩张可测空间补B-025。 |

## 推断目标与观测机制

节标签：`sec:rv-inference`、`sec:statistics-model-target`、`sec:statistics-sampling-population`／`sec:statistics-missingness-observation`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-485 数理统计 | 3842–3847，“只有有限数据…规律未知”；`sec:rv-inference` | 从正向概率计算转向反推规律。 | 参数、分布、未来结果三种目标 | 不企图唯一重建底层随机映射。 | 已清楚；无。 |
| B08-486 行动与损失 | 3849，“报告的结论…偏离目标的代价”；`sec:rv-inference` | 为误差指定可比较口径。 | ℓ(a,τ(θ))、后平方与绝对例 | 损失不是概率，行动可为点或函数。 | 已清楚；无。 |
| B08-487 统计风险 | 3851–3860，“重复抽样取期望”；`sec:rv-inference` | 评价整个程序而非某次读数。 | `def:statistics-estimator-risk` | 非负可测，允许∞；与本章前预测函数风险对象不同。 | 已清楚；无。 |
| B08-488 统计模型 | 3869–3877，“一族候选分布”；`sec:statistics-model-target` | 明确数据可能由哪些规律生成。 | `def:statistics-model-statistic` | 共同可测观测空间，参数可无限维。 | 已清楚；无。 |
| B08-489 参数作为未知索引 | 3875–3877，“未必是物理常数”；`sec:statistics-model-target` | 防止把所有拟合系数实体化。 | 系数、比例、CDF例 | 模型参数与被随机观测的数据不同。 | 已清楚；无。 |
| B08-490 统计量 | 3879–3880，“只依赖样本的可测函数”；`sec:statistics-model-target` | 定义允许计算的数据摘要。 | T(Y)及样本均值 | 不得含未知真实参数。 | 已回顾且清楚；无。 |
| B08-491 估计量 | 3880–3885，“设计来逼近…未知目标”；`sec:statistics-model-target` | 区分任意摘要与承担估计职责的规则。 | τ̂(Y) | 重复抽样下随机，不是参数自身。 | 已清楚；无。 |
| B08-492 估计值 | 3882–3885，“观测…具体数值”；`sec:statistics-model-target` | 区分随机程序与本次输出。 | τ̂(y)与τ̂(Y)对照 | 不再因未知参数而自动成为随机变量。 | 已清楚；无。 |
| B08-493 目标／分布泛函 | 3888–3896，“τ:Θ→A”；`sec:statistics-model-target` | 允许估计均值、函数或分布。 | 参数、CDF、向量损失例 | 只有由观测律决定时才写成分布泛函。 | 已清楚；无。 |
| B08-494 位置估计与未来预测 | 3888–3909，“预测…还要保留新噪声”；`sec:statistics-model-target` | 提前区分均值精度和结果波动。 | EȲ=θ、Var Ȳ=σ²/n | 方差缩减另用独立性；零均值只给无偏。 | 已清楚；无。 |
| B08-495 目标可识别性 | 3913–3922，“同分布⇒同目标”；`sec:statistics-model-target` | 抽样精度之前排除原理性歧义。 | `def:statistics-identifiability`、温度计例 | 总体层面，不是算法拟合优度。 | 已清楚；无。 |
| B08-496 参数可识别性 | 3923–3925，“τ(ϑ)=ϑ”；`sec:statistics-model-target` | 明确它只是目标识别的特例。 | 取恒等目标 | 参数冗余可不妨碍某些目标可识别。 | 已清楚；无。 |
| B08-497 混合标签交换 | 3927–3937，“换…不改变分布”；`sec:statistics-model-target` | 给模型等价的可计算实例。 | `ex:statistics-mixture-label-switching` | 排序约束只固定表示，不增加信息；混合此前已建。 | 已清楚；无。 |
| B08-498 共同来源偏移 | 3939–3942，“只能识别θ+b”；`sec:statistics-model-target` | 说明大数据不消除系统歧义。 | 温度计θ+b模型 | 随机误差缩小与共同偏差消除不同。 | 已清楚；无。 |
| B08-499 不可识别目标不可能一致恢复 | 3944–3955，“两球不相交”；`sec:statistics-model-target` | 将识别定义转为任何估计程序的限制。 | 三分之一目标间距、概率质量矛盾 | 使用同观测律推同统计量律，非特定算法失败。 | 已清楚；无。 |
| B08-500 目标总体 | 3961–3964，“对象、时间和条件”；`sec:statistics-sampling-population` | 明确统计结论希望对谁成立。 | 工作日传感器／周末设备 | 不等于当前数据集。 | 已清楚；无。 |
| B08-501 抽样制度 | 3962–3966，“如何…产生”；`sec:statistics-sampling-population` | 规定概率计算的联合生成规则。 | iid与后续三类抽样比较 | 总体相同不保证抽样机制相同。 | 已清楚；无。 |
| B08-502 配对抽样 | 3966–3968，“一对…一个单位”；`sec:statistics-sampling-population` | 保留同对象两种条件的共同波动。 | D_i差值及协方差展开 | 独立单位是对，不是两列的2n条。 | 已清楚；无。 |
| B08-503 分层抽样 | 3969，“预先按群组分别抽取”；`sec:statistics-sampling-population` | 控制群组组成。 | π_gμ_g总体加权 | 与随机抽整组不同；具体分配方案未展开。 | 定义可懂；可选给等额与比例分配例。 |
| B08-504 成组抽样 | 3969–3970，“一次抽取整个…群”；`sec:statistics-sampling-population` | 将组内相关纳入抽样单位。 | 十设备万记录例 | 组内多记录不增加独立处理分配次数。 | 已清楚；无。 |
| B08-505 配对差的方差收益 | 3972–3980，“-2Cov”；`sec:statistics-sampling-population` | 说明配对不是必然提高精度。 | 正／负协方差对照 | 已回顾方差展开，不把相关统一视为有害。 | 已清楚；无。 |
| B08-506 群组均值与固定分母精度 | 3982–3991，“p_g(1-p_g)/n_g”；`sec:statistics-sampling-population` | 把小群体误差与总样本数分开。 | 总体加权均值、Bernoulli方差 | 需要组内独立及固定正n_g。 | 已清楚；无。 |
| B08-507 随机群组样本数 | 3992–3997，“N_g>0…条件方差”；`sec:statistics-sampling-population` | 防止以总数或随机分母直接套固定公式。 | N_g指示和、空组事件 | 无条件误差还需平均分母。 | 已清楚；无。 |
| B08-508 逆入样概率恒等式 | 3999–4011，“E[SY/ρ(Z)]=EY”；`sec:statistics-sampling-population` | 将偏选样本接回目标平均。 | 条件期望三步等式 | 正值、给Z后S⊥Y、矩条件；与任意权重不同。 | 已清楚；无。 |
| B08-509 记录数与分析／随机化单位 | 4013–4017、4025–4028，“十台设备…不是一万”；`sec:statistics-sampling-population` | 排除复制和组内重复造成伪信息量。 | 复制记录、设备处理分配 | 影响标准误、划分及置换；不是只改显示分母。 | 已清楚；无。 |
| B08-510 时间选择改变估计目标 | 4019–4023，“告警后加密采样”；`sec:statistics-sampling-population` | 解释时点频率如何改变朴素平均。 | 等间隔／告警采样比较 | 权重需所有时段正覆盖，不能补未观测夜间。 | 已清楚；无。 |
| B08-511 完全随机缺失MCAR | 4032–4036，“R⊥(X,Y)”；`sec:statistics-sampling-population` | 给完整案例可代表总体的强条件。 | 指示与已见／未见变量定义 | 比MAR强，不由缺失比例判断。 | 已清楚；无。 |
| B08-512 随机缺失MAR | 4037–4041，“给定已观测协变量后”；`sec:statistics-sampling-population` | 允许缺失依赖可见特征但不依赖剩余结果。 | R⊥Y∣X、多模式二维例 | 名称不表示完全随机；不能自动保证正覆盖。 | 已清楚；无。 |
| B08-513 非随机缺失MNAR | 4042、4055，“MAR条件失败”；`sec:statistics-sampling-population` | 指出仅凭已见数据通常不够识别。 | 有界Y的端点补全例 | 与参数估计不精确是不同障碍。 | 已清楚；无。 |
| B08-514 观测模式与模式概率核 | 4044–4057，“O(r)、M(r)、g(r∣z)”；`sec:statistics-sampling-population` | 多变量缺失不能用固定条件集概括。 | `def:statistics-missingness`、(1,0)/(0,1) | 每模式分别约束；实际记录包括模式本身。 | 已清楚；无。 |
| B08-515 完整案例分析 | 4059，“仍代表总体，但效率降低”；`sec:statistics-sampling-population` | 给MCAR的直接分析含义。 | P(R=1)>0限制 | 不适用于任意MAR完整子集。 | 已清楚；无。 |
| B08-516 插补与机制加权 | 4060–4061，“建模Y∣X后插补”；`sec:statistics-sampling-population` | 列MAR可用的两类恢复办法。 | 与已证逆概率式对照 | 插补的具体生成法未展开，不宣称单次填值保方差。 | 预告可懂；可选说明插补须传播估计不确定性。 |
| B08-517 缺失机制可忽略／参数及先验可分离 | 4062–4063，“还要求…可分离”；`sec:statistics-sampling-population` | 想限定何时不必联合拟合缺失机制。 | 没有忽略的对象或分离定义 | 似然尚未建立；不同于MCAR或MAR本身。 | 局部费力；B-030，移到似然后给因子分解及参数域条件。 |
| B08-518 缺失导致部分识别区间 | 4065–4083，“两个端点…达到”；`sec:statistics-sampling-population` | 无机制时仍可报告可达边界。 | E[RY]≤EY≤E[RY]+P(R=0) | MAR和正值使识别升级，仍不保证低方差。 | 已清楚；无。 |
| B08-519 传感器校准贯穿数据 | 4084–4097，“教学构造…不是实测”；`sec:statistics-sampling-population` | 固定后续算例对象与数值。 | `ex:statistics-running-sensor-calibration` | 引入x后不再是同一位置分布iid模型。 | 已清楚；无。 |

## 参数、损失与先验构造估计

节标签：`sec:statistics-likelihood-robustness`／`sec:statistics-bayes-hierarchy`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-520 参数与非参数方法的边界 | 4099–4101，“不是…输出的划分”；`sec:stats-parameter-inference-efficiency` | 避免均值=参数法、分布=非参数法的误解。 | 经验均值和整张高斯分布反例 | 方法假设与目标维度不同。 | 已清楚；无。 |
| B08-521 似然 | 4107–4112，“数据固定…参数待比较”；`sec:statistics-likelihood-robustness` | 用观测支持度比较候选模型。 | L(ϑ;y)=p_ϑ(y)、共同参考测度 | 不是参数概率密度，不自动归一。 | 已清楚；无。 |
| B08-522 最大似然估计 | 4112–4114，“argmax”；`sec:statistics-likelihood-robustness` | 形成数据驱动参数选择规则。 | 高斯均值、Bernoulli边界 | 极值集合可能空或多点；不由导数零保证。 | 已清楚；无。 |
| B08-523 负对数似然准则 | 4114–4122，“平方和+C”；`sec:statistics-likelihood-robustness` | 将乘积概率转成可优化加和。 | 已知σ²高斯配方及求导 | 独立结构给和，常数不含θ。 | 已清楚；无。 |
| B08-524 矩估计 | 4123–4125，“样本矩等于总体矩”；`sec:statistics-likelihood-robustness` | 在不使用完整密度时构造估计。 | EθY=θ→样本均值 | 与MLE可同结果但依据不同。 | 已清楚；无。 |
| B08-525 边界最大值与不存在 | 4127–4134，“开区间…只有上确界”；`sec:statistics-likelihood-robustness` | 提醒优化条件决定估计是否存在。 | 全0／全1 Bernoulli | 第4章内点一阶条件可回用。 | 已清楚；无。 |
| B08-526 充分统计量 | 4136–4140，“条件分布…不依赖ϑ”；`sec:statistics-likelihood-robustness` | 说明何种压缩保留全部模型参数信息。 | `def:statistics-sufficient-statistic`、成功次数 | 公共正则条件核；充分相对于模型。 | 已清楚；无。 |
| B08-527 因子分解定理 | 4141–4155，“g_ϑ(T(y))h(y)”；`sec:statistics-likelihood-robustness` | 给充分性的可计算判据。 | 有限离散逆向乘法、Gaussian和统计量 | 连续纤维不直接用普通密度比；一般定理声明有边界。 | 已清楚；可选补来源引用。 |
| B08-528 M估计 | 4157–4167，“最小点…可测选择”；`sec:statistics-likelihood-robustness` | 容纳按目标或稳健性设计的样本准则。 | `def:statistics-m-estimator` | 不必是似然，目标随ρ而变。 | 已清楚；无。 |
| B08-529 估计方程与参数得分ψ | 4168–4174，“∇_ϑρ”；`sec:statistics-likelihood-robustness` | 将可微准则转成求根。 | Σψ=0及平方残差 | 仅内点必要条件；Huber后专门区分残差导数。 | 已清楚；可选将平方损失写成半平方统一常数。 |
| B08-530 绝对损失的总体中位数 | 4175–4179，“总体最小点…中位数”；`sec:statistics-likelihood-robustness` | 展示损失选择改变目标泛函。 | 左右导数条件、P(Y≤θ)与P(Y≥θ) | 首次未限制E\|Y\|；后4297、4480有该条件。 | 技术疑点；B-031，补有限一阶绝对矩或中心化损失。 |
| B08-531 分离的总体最小值 | 4187–4192，“ε球外…正间隔”；`sec:statistics-likelihood-robustness` | 防止远处候选几乎同样好。 | inf球外Q>Q(ϑ*) | 唯一最小本身不在任意空间保证分离。 | 已清楚；无。 |
| B08-532 一致准则逼近推出估计一致 | 4181–4203，“偏差和优化误差…小于间隔”；`sec:statistics-likelihood-robustness` | 连接统计误差与数值误差。 | Q_n/Q定义、o_P优化误差及间隔论证 | 点态LLN不够；非紧空间需防逃逸。 | 已清楚；无。 |
| B08-533 伪真参数 | 4205–4216，“按对数损失最接近”；`sec:statistics-likelihood-robustness` | 解释失配模型的收敛目标。 | `def:statistics-pseudo-true-parameter` | 存在／唯一／分离另需；收敛不证明科学模型正确。 | 已清楚；无。 |
| B08-534 Huber损失 | 4218–4232，“小平方、大线性”；`sec:statistics-likelihood-robustness` | 限制大残差对位置拟合的贡献。 | 分段式与`fig:statistics-huber-loss` | 损失仍无界增长，不是删除异常点。 | 已清楚；无。 |
| B08-535 残差导数与参数导数 | 4233–4237，“整体乘以-1”；`sec:statistics-likelihood-robustness` | 避免两个ψ约定符号混乱。 | -ψ_c(y-θ)、截断±c | ψ有界不单独保证整个估计影响有界。 | 已清楚；无。 |
| B08-536 单点污染模型 | 4239–4244，“(1-ε)P+εΔ_z”；`sec:statistics-likelihood-robustness` | 量化少量异常输入的局部作用。 | 点质量定义及合法定义域要求 | ε是污染比例，不是参数扰动。 | 已清楚；无。 |
| B08-537 影响函数 | 4240–4246，“一阶变化”；`sec:statistics-likelihood-robustness` | 比较统计泛函对污染位置的敏感性。 | `def:statistics-influence-function`、均值z-EY | 有限局部导数，不是任意污染率误差上界。 | 已清楚；无。 |
| B08-538 隐式估计方程的影响函数 | 4247–4268，“-A⁻¹ψ”；`sec:statistics-likelihood-robustness` | 将敏感性接到求根算法。 | `eq:statistics-influence-function`完整隐式求导 | 交换积分、局部根稳定、A可逆；向量用Jacobian。 | 已清楚；无。 |
| B08-539 高杠杆输入的作用 | 4269–4271，“极端输入”；`sec:statistics-likelihood-robustness` | 限定残差稳健对回归的外推。 | 仅文字警告，无回归ψ算式 | 与大残差不同；可由输入乘得分理解。 | 可理解；可选补ψ=xψ_c(y-xᵀθ)。 |
| B08-540 频率学派口径 | 4280，“参数固定…样本随机”；`sec:statistics-likelihood-robustness` | 为后验与重复抽样区别奠基。 | 与Bayes公式并列 | 不否认参数未知。 | 已清楚；无。 |
| B08-541 参数先验 | 4280–4286，“另给参数指定”；`sec:statistics-likelihood-robustness` | 在模型中表达观测前不确定性。 | Gaussian、Beta后续例 | 不是由似然自动产生，也不是物理参数随机的事实断言。 | 已清楚；无。 |
| B08-542 后验分布 | 4282–4289，“数据证据与先验合并”；`sec:statistics-likelihood-robustness` | 将参数不确定性按观测更新。 | Bayes归一公式 | 前条件概率已建；非单一最优参数。 | 已清楚；无。 |
| B08-543 模型证据 | 4289，“分母…严格为正且有限”；`sec:statistics-likelihood-robustness` | 保证后验合法归一。 | ∫p(y∣u)π(u)du | 密度值可依单位，后章模型比较才展开用途。 | 已清楚；无。 |
| B08-544 后验均值的Bayes行动 | 4291–4296，“最小化后验平方损失”；`sec:statistics-likelihood-robustness` | 从后验选择点行动。 | 方差加(a-m)² | 需后验二阶矩；不是普适最优点。 | 已清楚；无。 |
| B08-545 后验中位数的Bayes行动 | 4297，“一阶绝对矩有限”；`sec:statistics-likelihood-robustness` | 对绝对误差选择相应点。 | 回用左右导数 | 此处条件齐；反衬B-031首次遗漏。 | 已清楚；无。 |
| B08-546 最大后验估计 | 4297–4299，“指定参考测度的密度峰值”；`sec:statistics-likelihood-robustness` | 区分众数与期望／中位数。 | 非线性换元Jacobian警告 | 峰不具有任意坐标不变性。 | 已清楚；可选给单调非线性换元小例。 |
| B08-547 共轭更新 | 4301–4316，“配方后”；`sec:statistics-likelihood-robustness` | 让先验与后验在同一分布族内可算。 | Gaussian先验和位置似然 | “共轭”名称由同族公式可读出。 | 已清楚；可选明说后验仍同族即共轭。 |
| B08-548 精度相加与精度加权均值 | 4311–4317，“按精度加权”；`sec:statistics-likelihood-robustness` | 解释观测和先验的相对影响。 | τ_n⁻²、μ_n公式 | 精度为方差倒数，不是误差的概率保证。 | 已清楚；可选直接命名1/方差。 |
| B08-549 Beta–Bernoulli共轭 | 4320–4325，“a+s,b+n-s”；`sec:statistics-likelihood-robustness` | 给离散比例的计数更新。 | 分布已在前半章定义 | 给p后条件iid，不是无条件独立。 | 已清楚；无。 |
| B08-550 Dirichlet类别计数共轭 | 4326–4329，“α_k+n_k”；`sec:statistics-likelihood-robustness` | 扩展到K类概率。 | 加计数公式 | 来源相关／过度离散不能直接沿用信息量。 | 已清楚；无。 |
| B08-551 层次模型 | 4331–4338，“组参数…共同中心尺度”；`sec:statistics-likelihood-robustness` | 不均衡群组间引入结构共享。 | θ_g与Y_gi两层Gaussian | 所有条件独立范围明确。 | 已清楚；无。 |
| B08-552 超参数 | 4338–4353，“共同中心和尺度”；`sec:statistics-likelihood-robustness` | 区分组内参数与描述组间规律的参数。 | μ、τ²固定／由全组估计对照 | 固定超参数时其他组数据尚未进入组后验。 | 已清楚；无。 |
| B08-553 收缩估计 | 4340–4353，“小样本群组…更强”；`sec:statistics-likelihood-robustness` | 用共同中心降低稀疏组波动。 | m_g、V_g精度权重 | 偏差代价由共同总体假设承担。 | 已清楚；无。 |
| B08-554 完全、部分与不汇聚 | 4354–4355，“τ²→0…→∞”；`sec:statistics-likelihood-robustness` | 用组间尺度解释共享程度。 | 两极限与有限正尺度 | 极限说明，不把∞先验直接当正规分布。 | 已清楚；无。 |
| B08-555 经验Bayes | 4355，“同一数据估计超参数”；`sec:statistics-likelihood-robustness` | 标记插入估计超参数的层次分析。 | 与固定外部值比较 | 不自动传播超参数估计不确定性。 | 已清楚；可选明确最后一点。 |
| B08-556 完整Bayes层次推断 | 4355–4359，“继续…指定先验”；`sec:statistics-likelihood-robustness` | 将超参数也纳入后验不确定性。 | 对超参数后验积分的说明 | 结构假设错误会掩盖真实群差。 | 已清楚；无。 |

## 分布与条件函数的估计

节标签：4360–4362仍属上一节；其后`sec:statistics-nonparametric-missing`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-557 经验分布 | 4360–4367，“每点赋质量1/n”；`sec:statistics-likelihood-robustness` | 不指定有限参数族而估计完整规律。 | F̂_n指示平均 | 是离散概率分布，不是密度曲线。 | 已清楚；无。 |
| B08-558 经验分位数 | 4361–4362，“Y_(⌈nq⌉)”；`sec:statistics-likelihood-robustness` | 用经验广义逆估计总体阈值。 | 次序统计量此前已建 | 不同于未来覆盖的(m+1)秩修正；平坦／原子需约定。 | 已清楚；无。 |
| B08-559 Glivenko–Cantelli定理 | 4366–4368，“sup_y…a.s.”；`sec:statistics-nonparametric-missing` | 为整张经验CDF及分位数提供统一收敛。 | 明确iid与一致范数 | 固定y LLN不能代替；定理直接声明。 | 可理解；可选补概率论来源或短网格论证。 |
| B08-560 直方图 | 4373–4375，“箱内数除以nh”；`sec:statistics-nonparametric-missing` | 给最简单的密度平滑表示。 | 分箱宽度与边界敏感性 | 和经验点质量不同。 | 已回顾且清楚；无。 |
| B08-561 核密度估计 | 4375–4381，“每个样本扩散为核”；`sec:statistics-nonparametric-missing` | 减少硬分箱边界影响。 | f̂_h显式和式 | 核非负归一才保证估计本身是密度。 | 已清楚；无。 |
| B08-562 平滑核的条件 | 4381–4385，“有界、紧支撑且对称”；`sec:statistics-nonparametric-missing` | 保证局部Taylor与有限矩计算合法。 | 一阶核矩消失说明 | 此处核不是概率转移核或GP协方差核。 | 已清楚；可选明示三个同名核职责不同。 |
| B08-563 带宽 | 4372、4399，“h→0、nh→∞”；`sec:statistics-nonparametric-missing` | 平衡局部化与可用样本量。 | 偏差随h²、方差随1/(nh) | 当前不依赖本批观测，选择后需重新分析。 | 已清楚；无。 |
| B08-564 核二阶矩μ₂(K) | 4383，“∫u²K”；`sec:statistics-nonparametric-missing` | 决定局部曲率偏差常数。 | Taylor二阶项 | 是核分布矩，不是观测方差。 | 已清楚；无。 |
| B08-565 核平方积分R(K) | 4384，“∫K²”；`sec:statistics-nonparametric-missing` | 决定局部方差常数。 | f(x)R(K)/(nh) | 与积分为1不同。 | 已清楚；无。 |
| B08-566 核密度偏差展开 | 4385–4394，“h²μ₂ f″/2”；`sec:statistics-nonparametric-missing` | 给平滑误差方向及尺度。 | 期望卷积式、对称消一阶 | 内部点及局部C²条件明确。 | 已清楚；无。 |
| B08-567 核密度方差展开 | 4395–4399，“1/(nh)”；`sec:statistics-nonparametric-missing` | 解释带宽增大减少局部噪声。 | 显式渐近式、iid前提 | 不适用相关权重样本。 | 可跟上；可选列单项二阶矩换元一行。 |
| B08-568 密度估计的边界偏差 | 4400，“核质量…支持集外”；`sec:statistics-nonparametric-missing` | 限制对称Taylor在边界的使用。 | 与局部回归边界图衔接 | 密度光滑不自动修复核截断。 | 已清楚；无。 |
| B08-569 高维局部样本体积 | 4401–4403，“h^d”；`sec:statistics-nonparametric-missing` | 说明维度如何改变方差尺度。 | 1/(nh^d) | 不是一维公式原封套用。 | 已清楚；无。 |
| B08-570 回归函数 | 4406–4409，“E[Y∣X=x]”；`sec:statistics-nonparametric-missing` | 从估计边缘密度转到预测条件平均。 | Y可积、联合iid | 条件版本已建；不要求线性关系。 | 已清楚；无。 |
| B08-571 局部常数核回归 | 4408–4414，“权重和为正”；`sec:statistics-nonparametric-missing` | 以邻域加权均值近似m(x)。 | 明确比值、10.25算例 | 随机分母，空邻域不能套式。 | 已清楚；无。 |
| B08-572 局部线性回归 | 4415–4425，“拟合a+b(X_i-x)”；`sec:statistics-nonparametric-missing` | 用局部斜率减少单侧设计的偏差。 | 加权平方最小化、9.2截距 | 与全局线性模型不同，拟合随x改变。 | 已清楚；无。 |
| B08-573 局部设计满秩 | 4416–4418，“至少两个不同取值”；`sec:statistics-nonparametric-missing` | 保证a,b唯一可解。 | 第6章892–954实际核对 | 非负权重中仅正权重输入贡献秩。 | 已清楚；无。 |
| B08-574 k近邻平均 | 4426–4428，“最近的k个”；`sec:statistics-nonparametric-missing` | 用自适应邻域半径替代固定h。 | k范围及预定破并列规则 | k固定不能一般给一致性。 | 已清楚；无。 |
| B08-575 维数灾难 | 4427–4428，“扩大邻域…局部性变差”；`sec:statistics-nonparametric-missing` | 为高维方法限制提供具体机制。 | 与h^d方差相连 | 不是笼统宣称高维不能学习。 | 已清楚；无。 |
| B08-576 局部加权正规方程算例 | 4430–4468，“S₀,S₁,S₂,T₀,T₁”；`sec:statistics-nonparametric-missing` | 让常数与斜线的预测差可手算。 | 9.2+1.4x、`fig:statistics-local-boundary-fit` | 未知真均值未画，不能宣称哪个更准。 | 已清楚；无。 |
| B08-577 邻域收缩与局部样本增长 | 4470–4476，“h→0、nh→∞”；`sec:statistics-nonparametric-missing` | 同时让平滑偏差和方差消失。 | 局部输入密度正、矩和平滑条件；k版两条件 | 当前内部点结果，不自动边界／高维通用。 | 已清楚；无。 |
| B08-578 内插与外推 | 4477–4478，“输入密度为零的区域”；`sec:statistics-nonparametric-missing` | 区分邻域方法可用信息的边界。 | 缩小邻域不会产生新信息 | 外推需额外结构，不只更多优化。 | 已清楚；无。 |
| B08-579 分位数损失 | 4480–4488，“u(q-I{u<0})”；`sec:statistics-nonparametric-missing` | 对非对称偏差选择条件阈值。 | 条件期望、次梯度区间 | q∈(0,1)沿前分位约定；Y可积保证有限。 | 已清楚；无。 |
| B08-580 分位数回归 | 4480、4494–4495，“a=f(x)”；`sec:statistics-nonparametric-missing` | 直接估计条件分位函数。 | 经验损失加正则、线性／样条例 | 不需高斯／等方差；表示限制仍带偏差。 | 已清楚；无。 |
| B08-581 分位最小点集合 | 4486–4493，“F(a⁻)≤q≤F(a)”；`sec:statistics-nonparametric-missing` | 处理原子与非唯一阈值。 | 次微分含0、前Q_q回指 | 第4章979–1016核对；广义逆只是选代表。 | 已清楚；无。 |

## 概率预测与有限样本覆盖

节标签：`sec:statistics-scoring-calibration`、`sec:probability-exchangeability-conformal-ranks`／`sec:rv-prediction-sets`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-582 条件预测分布 | 4497–4503，“先给出预测分布”；`sec:stats-prediction-observation-limits` | 区分预测完整规律与按损失选点。 | 均值／中位数／二元最可能类 | 平方／绝对最优需相应矩条件，前Bayes段已说明。 | 已清楚；可选就地回指矩条件。 |
| B08-583 插件预测 | 4504，“代入估计”；`sec:statistics-scoring-calibration` | 给最直接的未知参数替代。 | P_θ̂(Y_new∈A∣x) | 不传播全部参数不确定性。 | 已清楚；无。 |
| B08-584 后验预测 | 4504–4516，“对参数后验积分”；`sec:statistics-scoring-calibration` | 合并参数不确定性与未来噪声。 | N(μ_n,σ²+τ_n²) | 给参数后新数据与训练数据条件独立。 | 已清楚；无。 |
| B08-585 评分规则与适当性 | 4518–4525，“鼓励…如实报告”；`sec:statistics-scoring-calibration` | 用损失评价整个概率分布。 | `def:statistics-proper-scoring-rule` | 期望有定义、诚实报告有限；不是只奖猜中类别。 | 已清楚；无。 |
| B08-586 严格适当性 | 4523，“最小点唯一”；`sec:statistics-scoring-calibration` | 排除不诚实报告同样最优。 | 后log与Brier证明 | 强于适当性。 | 已清楚；无。 |
| B08-587 有限离散KL散度 | 4527–4534，“Σp log(p/q)”；`sec:statistics-scoring-calibration` | 写出对数评分的额外损失。 | 零质量／漏支持约定 | 一般空间定义在下一章，当前公式足够。 | 已清楚；无。 |
| B08-588 KL非负与等号条件 | 4535–4540，“-log u≥1-u”；`sec:statistics-scoring-calibration` | 证明如实报告确实最佳。 | 有限支持求和及有限Jensen备选 | 此处不需尚缺的一般条件Jensen，B-013不重复套用。 | 已清楚；无。 |
| B08-589 对数评分 | 4542–4550，“-log q(y)”；`sec:statistics-scoring-calibration` | 严厉惩罚给真结果极小概率。 | 期望差=KL | 连续版需共同密度与可积性；坐标值不等于不变概率。 | 已清楚；无。 |
| B08-590 二元Brier评分 | 4552–4560，“(q-Y)²”；`sec:statistics-scoring-calibration` | 给有界概率损失作比较。 | (q-p)²+p(1-p)完整展开 | 和对数评分都适当但尾部惩罚不同。 | 已清楚；无。 |
| B08-591 多类Brier评分 | 4562–4569，“概率向量平方距离”；`sec:statistics-scoring-calibration` | 推广二元结果的诚实激励。 | 范数平方加1-‖p‖² | 概率单纯形上最优，不是KL同一距离。 | 已清楚；无。 |
| B08-592 二元概率校准 | 4572–4578，“E[Y∣Q]=Q”；`sec:statistics-scoring-calibration` | 检查同预测组的真实发生率。 | `def:statistics-probability-calibration` | 总体a.s.条件，不要求有限频数精确相等。 | 已清楚；无。 |
| B08-593 区分能力 | 4578–4580，“更可能…更高分”；`sec:statistics-scoring-calibration` | 区分排序信息与概率数值正确。 | 恒报基准率反例 | 完美校准可以毫无区分。 | 已清楚；无。 |
| B08-594 锐度 | 4579–4581，“分布是否集中”；`sec:statistics-scoring-calibration` | 说明更确定的报告何时有意义。 | 0/1极端报告与0.2/0.8比较 | 集中不能补偿失校准。 | 已清楚；无。 |
| B08-595 Brier校准分解 | 4583–4593，“校准误差…剩余不可分辨”；`sec:statistics-scoring-calibration` | 量化概率错位与可区分信息。 | η(Q)、基准发生率、全方差型式 | 非把随机波动全归校准错误。 | 已清楚；无。 |
| B08-596 多类向量校准 | 4594–4596，“给定整向量”；`sec:statistics-scoring-calibration` | 防止只看各类别边际满足就称联合校准。 | P(Y=k∣p̂)=p̂_k | 条件信息多于仅给p̂_k。 | 定义清楚；可选给边际成立而向量失败的小例。 |
| B08-597 校准与区分的两组比较 | 4598–4613，“排序相同…准确性不同”；`sec:statistics-scoring-calibration` | 让三个性质的区别可手算。 | `tab:statistics-calibration-discrimination`、0.25/0.16/0.20 | 同一个总体固定比较标准。 | 已清楚；无。 |
| B08-598 分类logit | 4616，“分类logit z”；`sec:statistics-scoring-calibration` | 为校准变换标记原始评分。 | softmax前输入；第3章885–949补读 | 术语自身未定义，但实数评分转换已建。 | 可理解；可选加“softmax前的实值评分”。 |
| B08-599 温度缩放 | 4616–4618，“softmax(z/T)”；`sec:statistics-scoring-calibration` | 调整置信程度而保持类别排序。 | T>0、校准集对数损失拟合 | 保排序不保证总体校准；T估计仍有误差。 | 已清楚；无。 |
| B08-600 保序回归校准 | 4618–4621，“单调分数到概率映射”；`sec:statistics-scoring-calibration` | 提供更灵活的后处理。 | 排序后q₁≤…≤q_m最小平方和 | 单调性与校准不同，数据少易过拟合。 | 已清楚；可选明写0≤q_i≤1及分数并列规则。 |
| B08-601 折外预测与数据职责分离 | 4622–4623，“训练、拟合校准、评价”；`sec:statistics-scoring-calibration` | 防止重复使用标签产生乐观效果。 | 明列三个任务；后交叉验证补全 | 当前折外术语未展开但数据分离直觉明确。 | 可理解；可选一句“该样本未参与拟合的模型所给预测”。 |
| B08-602 分箱可靠性图 | 4623–4625，“连续条件近似成有限组”；`sec:statistics-scoring-calibration` | 说明经验校准检查的噪声与分辨率。 | 箱边界、箱内抽样误差说明 | 图不直接证明连续条件校准。 | 已清楚；无。 |
| B08-603 预测集合 | 4630–4631，“覆盖未来Y_(n+1)”；`sec:probability-exchangeability-conformal-ranks` | 用允许结果集合表示预测不确定性。 | 明确训练和未来联合概率 | 非固定参数区间。 | 已清楚；无。 |
| B08-604 Gaussian精确预测区间 | 4632–4643，“σ²(1+1/n)”；`sec:probability-exchangeability-conformal-ranks` | 分开均值误差与新读数噪声。 | z分位、[6.40,14.40] | 新噪声与训练均值独立，已知σ。 | 已清楚；无。 |
| B08-605 Student t分布与未知方差预测 | 4643–4648，“Z/√(U/ν)”；`sec:probability-exchangeability-conformal-ranks` | 在估计噪声尺度后仍得精确比值规律。 | n-1自由度、t分位及独立Z/χ²定义 | 样本残差χ²及与均值独立未建立。 | 局部费力；B-032，补Gaussian正交坐标分解。 |
| B08-606 样本方差S² | 4645，“(n-1)⁻¹Σ(Y_i-Ȳ)²”；`sec:probability-exchangeability-conformal-ranks` | 用数据估计未知噪声方差。 | 显式定义，后5016再回顾 | 分母与经验分布方差1/n不同；自由度待解释。 | 定义清楚；精确分布桥接同B-032。 |
| B08-607 可交换无并列分数的均匀秩 | 4651–4660，“每样本恰占一个秩”；`sec:probability-exchangeability-conformal-ranks` | 不依赖渐近或参数模型的有限样本基准。 | `eq:probability-uniform-rank` | 无并列条件当地齐全；前1106的B-015仍成立。 | 已清楚；无。 |
| B08-608 并列的随机化与保守处理 | 4662，“独立连续随机数…字典序”；`sec:probability-exchangeability-conformal-ranks` | 恢复精确秩或保住下界。 | 明列两种方案 | 随机化后秩均匀；不随机边界通常保守。 | 已清楚；为B-015可直接前指此处。 |
| B08-609 拆分共形预测 | 4664–4677，“条件于训练数据”；`sec:probability-exchangeability-conformal-ranks` | 将固定模型与可交换校准分开。 | `eq:probability-split-conformal-set` | 评分须固定，校准与未来须条件可交换。 | 已清楚；无。 |
| B08-610 不一致性分数 | 4665–4668，“越大…越不相容”；`sec:probability-exchangeability-conformal-ranks` | 将不同预测任务转成同一排序问题。 | s(X,Y)、候选y阈值集合 | 只需同规则，分数不必概率或损失。 | 已清楚；可选给绝对残差具体实例。 |
| B08-611 共形秩修正与无穷阈值 | 4669–4680，“⌈(m+1)(1-α)⌉”；`sec:probability-exchangeability-conformal-ranks` | 有限校准量下保证未来秩覆盖。 | m=9两种α、q=0.8或∞ | 不同于经验q分位的⌈mq⌉；∞可代表无非平凡信息。 | 已清楚；无。 |
| B08-612 拆分共形覆盖定理 | 4682–4697，“至少1-α”；`sec:probability-exchangeability-conformal-ranks` | 把秩均匀转成预测集合保证。 | `thm:probability-split-conformal-coverage`完整补事件证明 | ≤阈值包含并列，随机化须纳入概率空间。 | 已清楚；无。 |
| B08-613 边际覆盖 | 4699–4700，“校准与未来共同平均”；`sec:probability-exchangeability-conformal-ranks` | 说明保证到底平均了哪些随机对象。 | 条件于训练、再解除条件 | 不等于给定已实现校准集后的保证。 | 已清楚；无。 |
| B08-614 逐输入条件覆盖 | 4700–4708，“给定X=x”；`sec:probability-exchangeability-conformal-ranks` | 限制把总体下界推广到每个输入。 | 明确列不被推出的条件式 | 连续输入处版本问题已由前条件概率处理。 | 已清楚；无。 |
| B08-615 分组校准与组内覆盖 | 4708、4714，“预先规定群组”；`sec:probability-exchangeability-conformal-ranks` | 指明平均覆盖不能保护每组。 | 需组内可交换及足够样本 | 不可看校准结果后挑有利分组。 | 已清楚；无。 |
| B08-616 自适应／时间序列破坏秩对称 | 4710–4713，“失效…均匀秩步骤”；`sec:probability-exchangeability-conformal-ranks` | 明确算法或抽样改变后哪里断裂。 | 修改分数、时间未来、选择位置三例 | 不是简单换分位索引可修。 | 已清楚；无。 |

## 估计误差与效率

节标签：`sec:statistics-bias-efficiency`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-617 估计偏差 | 4723–4735，“系统偏移”；`sec:statistics-bias-efficiency` | 将平均位置偏离目标与随机波动分开。 | Eθ̂-θ及收缩例 | 不等于单次误差，也不由一致性排除有限样本偏差。 | 已回顾且清楚；可选在分解前重申二阶矩有限。 |
| B08-618 均方误差分解 | 4724–4735，“方差加偏差平方”；`sec:statistics-bias-efficiency` | 比较有偏与无偏程序总体误差。 | `eq:statistics-mse-decomposition`交叉项为零 | 无偏不等于风险最小。 | 已清楚；无。 |
| B08-619 向量总平方风险 | 4737–4744，“tr Cov+‖Bias‖²”；`sec:statistics-bias-efficiency` | 固定多维误差的聚合口径。 | 向量分解式 | 与最坏坐标或方向风险不同。 | 已清楚；无。 |
| B08-620 收缩的有限样本代价 | 4746–4753，“中心近时…远时”；`sec:statistics-bias-efficiency` | 具体化偏差方差交换。 | aȲ+(1-a)μ₀的MSE公式 | 依赖真实θ距中心，非所有θ统一改进。 | 已清楚；无。 |
| B08-621 估计一致性 | 4755–4758，“偏差概率→0”；`sec:statistics-bias-efficiency` | 将前M估计的一致极限定名。 | ε定义、前argmin论证 | 不承诺有限n误差或收敛速度。 | 已清楚；无。 |
| B08-622 均方一致 | 4759–4760，“MSE→0”；`sec:statistics-bias-efficiency` | 更强的平均平方误差消失。 | Markov推出依概率一致 | 反向需平方误差的一致可积等条件。 | 已清楚；可选明确UI作用于平方误差族。 |
| B08-623 渐近正态性 | 4761–4766，“√n(θ̂-θ)⇒N(0,V)”；`sec:statistics-bias-efficiency` | 给一致性之外的误差形状与尺度。 | 正态极限式 | 不由一致性自动推出，需另证。 | 已清楚；无。 |
| B08-624 Gauss–Markov线性模型 | 4768–4777，“同方差且协方差为零”；`sec:statistics-bias-efficiency` | 比较一组线性观测的估计效率。 | `eq:statistics-gauss-markov-model` | 不要求噪声独立或高斯，列满秩保证参数识别。 | 已清楚；无。 |
| B08-625 最小二乘的条件无偏及协方差 | 4776–4781，“σ²(XᵀX)⁻¹”；`sec:statistics-bias-efficiency` | 将前章代数最小残差接到统计误差。 | C₀X=I的条件均值计算 | 第6章892–954实读；最小残差本身不保证此统计结论。 | 已清楚；无。 |
| B08-626 最佳线性无偏估计 | 4778–4795，“所有θ均无偏的线性估计”；`sec:statistics-bias-efficiency` | 限定“最佳”的比较类。 | `thm:statistics-gauss-markov`、C=C₀+D证明 | 只在线性无偏类，不能排除有偏收缩低MSE。 | 已清楚；无。 |
| B08-627 协方差半正定序比较 | 4783–4796，“任意线性组合方差”；`sec:statistics-bias-efficiency` | 说明矩阵最优性比逐坐标比较强。 | σ²DDᵀ二次型非负 | 非逐元素矩阵大小。 | 已回顾且清楚；无。 |
| B08-628 等权样本均值的最优特例 | 4798–4799，“额外不均衡权重只增加方差”；`sec:statistics-bias-efficiency` | 把矩阵证明压成可手算一维例。 | a_i=1/n+b_i、Σb_i=0 | 需同方差不相关；异方差时不可原样使用。 | 已清楚；无。 |
| B08-629 均值的精确正态与渐近正态 | 4801–4810，“不要求观测本身高斯”；`sec:statistics-bias-efficiency` | 区分模型假设与极限定理。 | 有限正方差iid CLT | 高斯位置样本在每n精确，其他分布只渐近。 | 已清楚；无。 |
| B08-630 标准误的一致代入 | 4811，“依概率趋向正确尺度”；`sec:statistics-bias-efficiency` | 解释为什么可用估计方差标准化。 | Slutsky准确回指 | 数值看似合理不等于一致估计。 | 已清楚；无。 |
| B08-631 估计方程的随机线性展开 | 4813–4826，“-A⁻¹ n^(-1/2)Σψ”；`sec:statistics-bias-efficiency` | 从求根获得渐近误差。 | A、B定义及最终式 | 经验导数一致收敛、A可逆未落实。 | 局部费力；B-033，补随机平均斜率条件。 |
| B08-632 夹心协方差 | 4827–4829，“A⁻¹B(A⁻¹)ᵀ”；`sec:statistics-bias-efficiency` | 在模型失配下保留曲率与噪声差别。 | 标量A⁻²B及多维式 | 不随意把A、B当同一信息矩阵。 | 陈述可懂；展开条件同B-033。 |
| B08-633 似然得分 | 4838–4840，“∇θ log pθ(x)”；`sec:statistics-bias-efficiency` | 记录分布对参数微变的敏感方向。 | Gaussian位置后例 | 与前M准则得分可差符号／意义；当前密度须正且可微。 | 已清楚；无。 |
| B08-634 Fisher信息矩阵 | 4836–4851，“得分外积平均”；`sec:statistics-bias-efficiency` | 给局部可辨信息量及效率下界。 | `def:information-fisher-matrix`、PSD解释 | 定义不自动等于负期望Hessian；需有限二阶得分矩。 | 已清楚；无。 |
| B08-635 得分均值零与信息恒等式 | 4853–4869，“交换微分与积分”；`sec:statistics-bias-efficiency` | 使局部密度变化转成方差尺度。 | 共同正支持、导数支配及完整计算 | 不适用参数改变支持的边界情形。 | 已清楚；前积分下求导已核对。 |
| B08-636 独立观测的信息可加 | 4870–4872，“n/σ²”；`sec:statistics-bias-efficiency` | 将单次信息换到样本规模。 | Gaussian位置1/σ²、批次得分和 | 零均值加独立消交叉项；相关数据不可直接乘n。 | 已清楚；可选补一行交叉项说明。 |
| B08-637 Cramér–Rao界 | 4874–4883，“τ′²/(nI)”；`sec:statistics-bias-efficiency` | 比较任意无偏估计的可达方差。 | `thm:statistics-cramer-rao` | 正信息、无偏、有限二阶矩及估计期望可微分别要求。 | 已清楚；无。 |
| B08-638 目标导数与得分协方差身份 | 4885–4902，“τ′=E[(τ̂-τ)s]”；`sec:statistics-bias-efficiency` | 说明效率下界来自哪里。 | 求导无偏等式再Cauchy–Schwarz | 不只给信息公式后宣称下界。 | 已清楚；无。 |
| B08-639 向量Cramér–Rao界 | 4904–4919，“Jτ I_n⁻¹ Jτᵀ”；`sec:statistics-bias-efficiency` | 适配不同维数目标。 | Jacobian维数、参数恒等特例 | 不是逐坐标界拼接；可逆信息、矩形J可降秩。 | 陈述清楚；可选用线性投影证明入口。 |
| B08-640 选择乐观偏差 | 4921–4941，“各自无偏…最小值偏低”；`sec:statistics-bias-efficiency` | 说明评价已被用于选择时口径改变。 | 两候选±0.8例，Emin=3.6 | 与固定模型区间不同；不只更换最终标签。 | 已清楚；无。 |
| B08-641 交叉验证 | 4943–4947，“轮流训练与验证”；`sec:statistics-bias-efficiency` | 估计完整训练流程的未来误差。 | 明确训练规模、划分单位与调参依赖 | 非模型真伪检验。 | 已清楚；无。 |
| B08-642 嵌套交叉验证／独立测试 | 4940–4947，“评价整个选择流程”；`sec:statistics-bias-efficiency` | 将内层选模型与外层评价分开。 | 两候选例的用途解释 | 未给嵌套步骤细节，可由分工理解。 | 可理解；可选补外层留出、内层调参一句。 |
| B08-643 各折依赖与配对算法比较 | 4949–4952，“训练集大量重叠”；`sec:statistics-bias-efficiency` | 防止将K折分数当K个独立样本。 | 同划分配对、数据及训练随机性 | 交叉验证得分不自动给精确显著性。 | 已清楚；无。 |

## 区间、重抽样与持续覆盖

节标签：`sec:statistics-intervals-quantiles`／`sec:statistics-resampling`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-644 置信区间 | 4959–4967，“重复抽样程序”；`sec:statistics-intervals-quantiles` | 覆盖固定未知参数。 | `def:statistics-interval-coverage` | 数据固定后不是参数以该概率落入固定区间。 | 已清楚；无。 |
| B08-645 可信区间 | 4967–4968，“给定数据和模型”；`sec:statistics-intervals-quantiles` | 表达参数后验质量范围。 | 后验条件概率式 | 先验相关，不自动有频率覆盖；离散可保守。 | 已清楚；无。 |
| B08-646 三类覆盖对象比较 | 4969–4973、5001–5014，“重复样本、参数后验、未来观测”；`sec:statistics-intervals-quantiles` | 防止凭相同端点形式混用含义。 | `tab:statistics-interval-objects` | 预测集合前节已建，这里回顾；联合概率仍含训练样本。 | 已清楚；无。 |
| B08-647 已知方差均值置信区间 | 4975–4999，“σ/√n”；`sec:statistics-intervals-quantiles` | 给可算参数范围并比较未来范围。 | [9.62,11.18]、`fig:statistics-mean-prediction-width` | 新噪声不会随历史n消失。 | 已清楚；无。 |
| B08-648 未知方差t置信区间 | 5016–5026，“精确性依赖高斯性”；`sec:statistics-intervals-quantiles` | 回用样本尺度替代未知σ。 | t_(n-1)比值 | 前预测节同一缺失分解；一般分布仅渐近。 | 局部费力；B-032，补一次分解共同引用。 |
| B08-649 区间与检验的反演 | 5028–5031，“同模型、水平和统计量”；`sec:statistics-intervals-quantiles` | 把参数候选范围转成拒绝规则。 | θ₀不在区间即拒绝 | 检验正式定义稍后，此处前告；选择与单侧不能照搬。 | 预告清楚；无。 |
| B08-650 Bootstrap重抽样 | 5033–5039，“经验分布…有放回”；`sec:statistics-intervals-quantiles` | 近似难解析的重复抽样波动。 | τ̂*−τ̂对照τ̂−τ(P) | 条件于原数据的模拟分布，不是真实新数据生成模型。 | 已清楚；无。 |
| B08-651 百分位Bootstrap区间 | 5038–5039，“估计值的经验分位数”；`sec:statistics-intervals-quantiles` | 直接从重抽样输出构造范围。 | 说明不光滑、边界、尾分位等失效情形 | 不等于所有Bootstrap分布近似自动推出高阶覆盖。 | 定义可懂；可选明确上下α/2分位。 |
| B08-652 条件分布依概率弱收敛 | 5041–5049，“L(√n(Ȳ*−Ȳ)∣Y)⇒N”；`sec:statistics-intervals-quantiles` | 说明Bootstrap和原抽样极限的比较口径。 | 有限正方差iid均值 | 随机概率测度的收敛尚未定义，非普通X_n弱收敛同一对象。 | 局部费力；B-034，给测试函数条件期望含义。 |
| B08-653 条件Lindeberg尾项 | 5050–5057，“极端观测…不可忽略总方差”；`sec:statistics-intervals-quantiles` | 排除重抽样单个大值支配。 | 显式经验截断二阶矩 | 方差一致本身不够；2529仅预告同名条件。 | 白话清楚；定理衔接补B-034。 |
| B08-654 三角阵列CLT | 5058–5060，“给定原样本后…应用”；`sec:statistics-intervals-quantiles` | 每n经验分布不同，需比固定iid定理更广。 | 没有阵列定义或定理陈述 | 前2521只有固定分布iid CLT；不能直接套。 | 局部费力；B-034，陈述行内独立、方差和及尾条件版本。 |
| B08-655 Bootstrap标准误 | 5062–5073，“sqrt(4/25)=0.4”；`sec:statistics-intervals-quantiles` | 给重抽样不确定性的手算实例。 | E*、Var*、SE*三个尺度 | 经验方差分母n，非无偏S²分母n-1。 | 已清楚；无。 |
| B08-656 正态Bootstrap区间 | 5074–5078，“条件分布可由正态近似”；`sec:statistics-intervals-quantiles` | 展示一种使用重抽样尺度的区间。 | 与已知σ构造例重合 | 重合依赖该数值及平滑均值，不普遍等同参数区间。 | 已清楚；无。 |
| B08-657 渐近线性估计 | 5080–5086，“IF平均+o_P(n⁻¹/²)”；`sec:statistics-intervals-quantiles` | 把复杂统计量转成平均波动。 | 影响函数前已定义 | 需要IF均值零与有限方差等；不是任意泛函都成立。 | 形式可懂；后续推论条件见B-035。 |
| B08-658 Bootstrap线性化有效性 | 5087–5088，“也产生相同形式…因此接近”；`sec:statistics-intervals-quantiles` | 试图从原样本展开推广到条件重抽样。 | 未给条件余项／经验IF稳定性 | 单有原P下展开不足保证此推论。 | 技术疑点；B-035，补独立的条件线性化与CLT条件。 |
| B08-659 样本最大值Bootstrap失败 | 5088–5090，“不会生成更大的观测”；`sec:statistics-intervals-quantiles` | 给平滑性不足的直观反例。 | 支持集被当前最大值截断 | 不只是Monte Carlo次数不够。 | 已清楚；无。 |
| B08-660 配对与群组Bootstrap | 5092–5094，“重采样单位…独立单位”；`sec:statistics-intervals-quantiles` | 保留共享对象造成的依赖。 | 整对／整用户组 | 不是逐条记录重抽样。 | 已清楚；无。 |
| B08-661 块Bootstrap | 5093，“保留局部依赖”；`sec:statistics-intervals-quantiles` | 给时间序列的重抽样方向。 | 方法预告，无块长与混合条件 | 不声称任意相关序列即可有效。 | 预告可懂；可选明确需另定块长和依赖条件。 |
| B08-662 置信序列 | 5096–5103，“同一个事件覆盖所有时刻”；`sec:statistics-intervals-quantiles` | 允许根据已见数据持续查看及停止。 | `def:stoch-confidence-sequence` | 强于逐固定n各自置信区间。 | 已清楚；无。 |
| B08-663 按时刻错误预算的置信序列 | 5104–5116，“δ/[n(n+1)]”；`sec:statistics-intervals-quantiles` | 用已知尾界直接构造同时覆盖。 | 求和δ、Hoeffding半宽0.254对0.136 | 牺牲宽度换同时性；不称最紧。 | 已清楚；无。 |
| B08-664 条件均值版本的覆盖 | 5116–5117，“条件均值恒μ”；`sec:statistics-intervals-quantiles` | 放松独立而保留每步条件指数控制。 | 条件Hoeffding回指 | 任意相关观测仍不够。 | 已清楚；无。 |
| B08-665 有限候选的选择后同时覆盖 | 5118，“再将δ分给各候选”；`sec:statistics-intervals-quantiles` | 把时间与候选两个选择维度纳入预算。 | 有限预定类联合界 | 无限搜索／数据后新目标需额外统一控制。 | 已清楚；无。 |
| B08-666 自适应岭回归估计 | 5120–5127，“V_t⁻¹Σx_s y_s”；`sec:statistics-intervals-quantiles` | 从历史选择的特征恢复线性参数。 | `eq:stoch-ridge-estimator` | 复用前可预测设计、V₀=λI；不按固定设计误差证明。 | 已清楚；无。 |
| B08-667 正则偏差与噪声分解 | 5128–5135，“S_t−λθ*”；`sec:statistics-intervals-quantiles` | 区分数据噪声与岭的系统收缩。 | V_t(θ̂−θ*)恒等式 | 参数范数B额外先验界，不由λ自动保证。 | 已清楚；无。 |
| B08-668 自适应置信椭球 | 5135–5169，“β_t…对所有t”；`sec:statistics-intervals-quantiles` | 把向量集中变成可用参数范围。 | `eq:stoch-adaptive-confidence-ellipsoid`三角界 | 用V_t范数而非欧氏球；同一高概率事件。 | 已清楚；上游随机指数参数补B-028。 |
| B08-669 方向性均值预测误差 | 5189–5199，“β‖x‖_(V⁻¹)”；`sec:statistics-intervals-quantiles` | 将参数椭球转成指定线性目标半宽。 | Cauchy–Schwarz式 | 覆盖xᵀθ*，不是含未来噪声的单次y区间。 | 已清楚；可选明说“均值预测”避免术语混淆。 |
| B08-670 二维自适应查询 | 5171–5202，“选择较宽的方向”；`sec:statistics-intervals-quantiles` | 解释历史依赖如何仍满足可预测。 | `ex:stoch-two-dimensional-adaptive-design`、diag(4,2) | 新噪声前选择，非观察后筛样本。 | 已清楚；无。 |
| B08-671 相同预算的方向分配 | 5204–5215，“diag(4,2)与diag(3,3)”；`sec:statistics-intervals-quantiles` | 比较方向信息而非总记录数。 | `fig:stochastic-design-ellipsoids` | 图仅归一几何，真实β随行列式变化。 | 已清楚；无。 |
| B08-672 自适应与偷看当前噪声的边界 | 5217–5223，“指数超鞅第一步失败”；`sec:statistics-intervals-quantiles` | 指明选择偏差如何破坏证明。 | 看噪声再记录、失配条件均值例 | 不只是矩阵可逆就有覆盖。 | 已清楚；无。 |
| B08-673 条件次高斯与有限方差 | 5225–5226，“不是同义词”；`sec:statistics-intervals-quantiles` | 防止重尾下低估尾概率。 | 截断、稳健、有限矩工具预告 | 前定义指数矩比二阶矩强。 | 已回顾且清楚；无。 |
| B08-674 正则化与探索的不同职责 | 5227–5229，“不保证访问所有方向”；`sec:statistics-intervals-quantiles` | 区分估计界与设计成功。 | √λB偏差项 | 置信半径存在不保证任务信息足够。 | 已清楚；无。 |

## 检验与多重错误

节标签：`sec:statistics-testing-errors`／`sec:statistics-selection-multiplicity`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-675 假设检验 | 5235–5236，“数据与命题是否相容”；`sec:statistics-testing-errors` | 从估计范围转向可控拒绝决策。 | Gaussian零均值后例 | 不是为命题真实性直接赋概率。 | 已清楚；无。 |
| B08-676 随机化检验函数／拒绝域 | 5237–5248，“φ:Y^n→[0,1]”；`sec:statistics-testing-errors` | 允许边界随机决策并统一功效表示。 | `def:statistics-randomized-test-function`、独立U构造 | 0/1特例是确定拒绝域；φ非零假设后验。 | 已清楚；无。 |
| B08-677 原假设与备择 | 5250、5262，“被控制误报的情形”；`sec:statistics-testing-errors` | 明确哪类错误优先约束。 | H₀、H₁真假对应 | 并非默认H₀更科学或更可信。 | 已清楚；无。 |
| B08-678 检验大小 | 5250–5254，“sup_(θ∈H₀)Eθφ”；`sec:statistics-testing-errors` | 衡量零假设内最坏误报。 | 显式上确界 | 不等于某单点误拒绝概率。 | 已清楚；无。 |
| B08-679 检验水平 | 5256–5261，“大小≤α”；`sec:statistics-testing-errors` | 规定可容忍的错误预算。 | 不等式 | 大小实际值与水平上限不同。 | 已清楚；无。 |
| B08-680 功效函数 | 5250–5255，“Eθφ”；`sec:statistics-testing-errors` | 描述不同真实参数下发现能力。 | 后Gaussian功效式 | 定义可在全部θ，主要在备择解释。 | 已清楚；无。 |
| B08-681 第一类错误 | 5262，“H₀真时拒绝”；`sec:statistics-testing-errors` | 解释水平控制对象。 | φ拒绝概率 | 不等于发现中假结果的比例。 | 已回顾且清楚；无。 |
| B08-682 第二类错误 | 5262，“H₁真时不拒绝”；`sec:statistics-testing-errors` | 解释低功效时可能漏报。 | 后0.17功效算例 | 不拒绝不能当作证明H₀。 | 已回顾且清楚；无。 |
| B08-683 效应量 | 5263–5264，“差异有多大”；`sec:statistics-testing-errors` | 区分实际差异与证据强度。 | ȳ/σ=0.5在两个n相同 | 不由p值单独代表。 | 已清楚；无。 |
| B08-684 p值 | 5266–5267，“至少同样极端”；`sec:statistics-testing-errors` | 将统计量转为零假设证据尺度。 | 双侧Gaussian尾公式 | 极端规则须预定；不是H₀为真概率。 | 已回顾且清楚；无。 |
| B08-685 有效p值／超均匀性 | 5268–5277，“sup P(p≤u)≤u”；`sec:statistics-testing-errors` | 为复合零假设给准确有效性条件。 | `def:statistics-valid-p-value` | 离散保守可不均匀，阈值仍控制错误。 | 已清楚；无。 |
| B08-686 双侧Gaussian检验 | 5278–5282，“2{1-Φ(\|Z\|)}”；`sec:statistics-testing-errors` | 连接标准化观测和极端尾概率。 | Z=√nȲ/σ | 已知σ、iid高斯位置，不能随意估尺度而仍称精确。 | 已清楚；无。 |
| B08-687 均值变化下的检验功效 | 5283–5291，“√nδ/σ”；`sec:statistics-testing-errors` | 定量展示样本量对可辨差异的影响。 | 两尾正态概率式 | 同效应更大n增强功效，不改变效应本身。 | 已清楚；无。 |
| B08-688 检验族反演置信集合 | 5293–5304，“未被拒绝的候选值”；`sec:statistics-testing-errors` | 证明区间与检验的对应。 | 错覆盖事件等于拒绝真θ事件 | 不需对所有θ同时不拒绝；固定真θ的水平足够。 | 已清楚；无。 |
| B08-689 同效应不同证据算例 | 5306–5319，“n=4和100”；`sec:statistics-testing-errors` | 让不显著、低功效与等效区分。 | `ex:statistics-evidence-power-same-effect` | 观测效应、真实δ及容忍界Δ分开。 | 已清楚；无。 |
| B08-690 简单与复合假设 | 5322–5326、5346，“完全指定”；`sec:statistics-testing-errors` | 限定最强检验结论的适用对象。 | P₀/P₁对照未知参数族 | 复合不是更多样本，而是多候选分布。 | 已清楚；无。 |
| B08-691 似然比排序 | 5325–5327，“dP₁/dP₀”；`sec:statistics-testing-errors` | 比较某结果更支持哪个简单规律。 | Λ阈值 | RN导数此前已建立；此处P₁≪P₀。 | 已清楚；无。 |
| B08-692 Neyman–Pearson引理 | 5323–5344，“同大小最大功效”；`sec:statistics-testing-errors` | 给检验设计的最优证书。 | `thm:statistics-neyman-pearson`及逐点乘积非负证明 | 边界随机化达到α；不推广任意复合族。 | 已清楚；可选写c≥0。 |
| B08-693 一致最强检验 | 5346，“不一定存在”；`sec:statistics-testing-errors` | 限制简单最优性在整个备择族的推广。 | 只有边界提醒，没有完整定义 | 读者可理解为同一规则各备择均最强。 | 可理解；可选把上述含义写出。 |
| B08-694 隐私攻击的分布检验解释 | 5347–5348，“记录不在与在”；`sec:statistics-testing-errors` | 给似然比一个应用目标。 | 两种输出分布 | 实际分布估计及选择偏差不由理想引理解决。 | 预告清楚；无。 |
| B08-695 列联表 | 5350–5354，“两个分类变量”；`sec:statistics-testing-errors` | 将独立性问题写成格数比较。 | N_(r,c)、行列边际 | R,C此处是类别数，不是风险或拒绝数。 | 已回顾；可选直接定义点下标表示求和。 |
| B08-696 独立模型拟合期望格数 | 5351–5354，“行和×列和/N”；`sec:statistics-testing-errors` | 给无关联基准。 | E_(r,c)公式 | 是由边际估计的期望格数，非已知真实概率。 | 已清楚；无。 |
| B08-697 Pearson卡方检验 | 5354–5359，“(R-1)(C-1)自由度”；`sec:statistics-testing-errors` | 汇总标准化格数偏离。 | X²式、独立抽样与不稀疏条件 | 渐近而非任意小样本精确；条件独立另需处理。 | 陈述可读；可选说明自由度扣除边际限制。 |
| B08-698 条件独立检验 | 5358–5359，“还要控制第三个变量”；`sec:statistics-testing-errors` | 避免把边缘独立检验直接当调整后独立。 | 细分太多导致稀疏的限制 | 此处方法预告，不给通用条件独立算法。 | 预告清楚；无。 |
| B08-699 差异与等效命题 | 5361–5363，“无差异…可接受差异界”；`sec:statistics-testing-errors` | 说明未发现差异不等于足够相近。 | 零差异与区间备择对照 | 两检验原假设方向不同。 | 已清楚；无。 |
| B08-700 实际等效界Δ | 5361–5370，“预先…有实际含义”；`sec:statistics-testing-errors` | 把相近的任务标准量化。 | δ∈(-Δ,Δ) | 不是从数据挑最易通过的界。 | 已清楚；无。 |
| B08-701 两个单侧检验TOST | 5362–5381，“两边都拒绝”；`sec:statistics-testing-errors` | 建立等效性证据。 | `eq:statistics-tost-rejection`及1-2α区间 | 同标准误与相应正态近似；非普通1-α双侧差异检验。 | 已清楚；无。 |
| B08-702 并集原假设的交集拒绝控制 | 5382–5384，“至少一个…为真”；`sec:statistics-testing-errors` | 解释TOST总体错误不是2α。 | 事件包含论证 | 与多重候选任一次拒绝的并集不同。 | 已清楚；无。 |
| B08-703 非劣效检验 | 5384–5385，“只排除一个方向”；`sec:statistics-testing-errors` | 给只在意一侧损失的任务口径。 | H₀:δ≤-Δ | 不要求双侧等效。 | 已清楚；无。 |
| B08-704 置换检验 | 5387–5398，“零假设下标签可交换”；`sec:statistics-testing-errors` | 用设计对称性生成零假设分布。 | 全部置换尾比例、区组限制 | 与Bootstrap目标不同；仅均值相同不足交换。 | 已清楚；无。 |
| B08-705 有限模拟置换p值 | 5398–5400，“(1+次数)/(B+1)”；`sec:statistics-testing-errors` | 避免有限模拟给错误零p值。 | 加观测自身的秩修正 | 需从允许置换按对称方案随机抽取；不能挑置换。 | 可理解；可选写独立均匀抽取的具体方案。 |
| B08-706 族错误率FWER | 5402–5411，“至少一次误拒绝”；`sec:statistics-testing-errors` | 对许多候选控制任何错误。 | mα联合界 | 和FDR随机比例不同，不要求独立。 | 已清楚；无。 |
| B08-707 Bonferroni校正 | 5409–5411，“每项α/m”；`sec:statistics-testing-errors` | 简单分配多重检验预算。 | 联合界证明 | 多候选可能保守。 | 已清楚；无。 |
| B08-708 Holm逐步校正 | 5413–5419，“第一个未拒绝即停止”；`sec:statistics-testing-errors` | 利用排序改善固定阈值法。 | 首个真假设位置j、m₀联合界证明 | 任意依赖仍有效，不能在后面跳过失败项继续。 | 已清楚；无。 |
| B08-709 错误发现比例 | 5422–5427，“V/max(R,1)”；`sec:statistics-testing-errors` | 明确拒绝集合的错误占比。 | R=0约定0 | V、R都随机；不是先各自取平均再相除。 | 已清楚；无。 |
| B08-710 错误发现率FDR | 5421–5428，“比例的期望”；`sec:statistics-testing-errors` | 为大量发现任务设较宽松整体标准。 | 显式期望式 | 不保证每批数据错误比例≤q。 | 已清楚；可选明说最后一点。 |
| B08-711 Benjamini–Hochberg过程 | 5428–5437，“最大j:p_(j)≤jq/m”；`sec:statistics-testing-errors` | 在明确依赖条件下控制FDR。 | 排序算法、空集k=0、论文引用 | 当前要求全部p独立与真零超均匀，不只两两正相关。 | 已清楚；无。 |
| B08-712 持续查看p值的选择效应 | 5441–5445，“每t有效不推出存在t有效”；`sec:statistics-testing-errors` | 将时间窥视作为多次选择处理。 | 两个概率量词对照 | 停止规则属于程序，不可事后省略。 | 已清楚；无。 |
| B08-713 e值 | 5444–5445，“由非负超鞅构造的e值”；`sec:statistics-testing-errors` | 预告另一种错误控制尺度。 | 仅名称，后面给超鞅过程阈值 | 未定义非负且零假设均值≤1，亦未区分单值与过程。 | 局部费力；B-036，给一行矩条件及Markov阈值。 |
| B08-714 非负超鞅证据过程 | 5448–5452，“sup E_t≥1/α”；`sec:statistics-testing-errors` | 实现任意时刻同时控制。 | Ville公式，E₀=1 | 逐时刻e值不必构成该过程，不能任意择时。 | 公式清楚；与e值区别补B-036。 |
| B08-715 停止覆盖不等于估计无偏 | 5453–5454，“仍是不同问题”；`sec:statistics-testing-errors` | 限制序贯保证的扩张解释。 | 点估计偏差及多过程选择警告 | 同一过程任意时刻与多个过程任意选择不同。 | 已清楚；无。 |

## 模型证据与观测设计

节标签：`sec:statistics-model-evidence`、`sec:statistics-design-information`；末段`sec:probability-summary`／`sec:stochastic-processes-and-approximation-summary`／`sec:statistics-summary`已完整阅读。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B08-716 模型比较的不同目标 | 5456–5475，“预测、拟合、证据、编码”；`sec:stats-model-comparison-data-acquisition` | 防止各种准则因形式相似被混用。 | 四种对象逐项对照 | 输出模型相同不代表所优化风险相同。 | 已清楚；无。 |
| B08-717 边缘似然 | 5469–5474，“对参数积分”；`sec:statistics-model-evidence` | 在模型层比较数据支持。 | ∫p(y∣ϑ,M)π(ϑ∣M)dϑ | 前Bayes证据在此回顾，不是最大化参数后的似然。 | 已清楚；无。 |
| B08-718 Bayes因子 | 5477–5485，“两个边缘似然之比”；`sec:statistics-model-evidence` | 更新模型之间的相对支持。 | `def:statistics-bayes-factor` | 概率先验、分母正有限、分子有限可零。 | 已清楚；无。 |
| B08-719 模型先验赔率更新 | 5486–5487，“不是模型为真概率”；`sec:statistics-model-evidence` | 说明BF必须结合模型先验。 | 文字联系Bayes | “赔率”为概率比，前基础条件概率可推。 | 可理解；可选写后验赔率=BF×先验赔率。 |
| B08-720 先验尺度对证据的影响 | 5487–5491，“A→∞密度→0”；`sec:statistics-model-evidence` | 反驳更宽先验总是无影响。 | Gaussian Ȳ的边缘方差A²+σ²/n | 似然峰不变而积分变，固定观测比较。 | 已清楚；无。 |
| B08-721 固定维Laplace近似 | 5493–5529，“局部曲率近似积分”；`sec:statistics-model-evidence` | 计算尖峰加权积分的主项。 | `thm:statistics-laplace-approximation` | 内点唯一最大、H≻0、g局部连续正，另需全局尾部。 | 已清楚；无。 |
| B08-722 一致尾间隔及可积尾权重 | 5505–5518，“η>0、n₀…可积”；`sec:statistics-model-evidence` | 防止远处质量压过局部峰。 | 闭球外sup间隔和指数积分条件 | 唯一最大点本身不保证无界域尾部可忽略。 | 已清楚；无。 |
| B08-723 正定曲率产生二次上界 | 5531–5546，“-c‖ϑ-ϑ̂‖²”；`sec:statistics-model-evidence` | 构造局部可积支配函数。 | 缩球、紧环带、Taylor展开 | 第3章1116–1205已核对；负Hessian正定方向正确。 | 已清楚；无。 |
| B08-724 Hessian平方根换元 | 5548–5555，“u=√n H^(1/2)(ϑ-ϑ̂)”；`sec:statistics-model-evidence` | 将局部峰统一成标准Gaussian形状。 | Jacobian n^(-d/2)\|H\|^(-1/2) | 第6章1647–1668已核对；必须H正定可逆。 | 已清楚；无。 |
| B08-725 支配收敛的局部主项 | 5556–5566，“Gaussian控制函数”；`sec:statistics-model-evidence` | 使逐点Taylor极限可移入积分。 | 闭球g有界及(2π)^(d/2) | 第3章DCT已核对，不仅形式配方。 | 已清楚；无。 |
| B08-726 尾项相对主项可忽略 | 5567–5579，“o(n^(-d/2))”；`sec:statistics-model-evidence` | 完成局部近似对全积分的保证。 | e^(-(n-n₀)η)有限积分界 | 不是只说尾概率小，要小于主项尺度。 | 已清楚；无。 |
| B08-727 归一化观测信息 | 5589，“收敛到正定极限”；`sec:statistics-model-evidence` | 将随机似然峰接到固定函数近似。 | 随机ℓ_n及局部曲率条件 | 未显式定义为-∇²ℓ_n/n，但可从前H对应读出。 | 可理解；可选就地写矩阵式，与Fisher期望区别。 |
| B08-728 随机似然序列的Laplace扩展 | 5582–5596，“局部展开与尾控制一致”；`sec:statistics-model-evidence` | 避免把固定h定理直接套随机h_n。 | log证据=ℓ_n−(d/2)log n+O_P(1) | 条件分别列明，固定维、内点极限。 | 已清楚；无。 |
| B08-729 BIC | 5597–5602，“d log n”；`sec:statistics-model-evidence` | 将证据渐近主项转为候选比较准则。 | -2ℓ_n+dlog n、体积n^(-d/2)解释 | 固定有限候选，余项未称精确为零。 | 已清楚；无。 |
| B08-730 AIC | 5604–5611，“2d校正样本外乐观偏差”；`sec:statistics-model-evidence` | 将拟合损失修正到预测目标。 | -2ℓ_n+2d | 失配要另核协方差校正；不等于BIC同目标。 | 陈述可懂；可选给校正来源引用。 |
| B08-731 最小描述长度MDL | 5612–5615，“模型代码加数据代码”；`sec:statistics-model-evidence` | 从可解码描述代价选择模型。 | 对象与精度约定提醒 | 编码理论在下一章，此处明示接口而非证明。 | 预告清楚；无。 |
| B08-732 奇异模型的近似失效 | 5617–5619，“不唯一…曲率退化”；`sec:statistics-model-evidence` | 限制常规维度惩罚的适用性。 | 混合标签、零成分权重、边界、奇异Fisher | 不能把数值近似叫精确证据。 | 已清楚；无。 |
| B08-733 潜在结果 | 5624–5625，“各处理下本会产生的结果”；`sec:statistics-design-information` | 为随机实验的因果目标作入口。 | 明确第10章正式定义 | 当前纯预告，不靠它证明完整因果识别。 | 预告清楚；无。 |
| B08-734 随机分配 | 5625–5626、5641–5644，“指派独立于预先固定结果”；`sec:statistics-design-information` | 解释实验设计消除选择关联的职责。 | 两组均值模型 | 不要求两处理结果同分布，不自动推广目标总体。 | 已清楚；无。 |
| B08-735 配对对照 | 5627–5629，“对内比较…共享噪声”；`sec:statistics-design-information` | 利用相关性减少差值波动。 | 前配对协方差式可回用 | 配对差或错误分析可无收益。 | 已回顾且清楚；无。 |
| B08-736 两独立组均值差 | 5631–5644，“σ_A²/n_A+σ_B²/n_B”；`sec:statistics-design-information` | 给预算设计可优化的具体方差。 | 无偏均值差及组间独立条件 | 不是有限总体固定潜在结果下无条件套式。 | 已清楚；无。 |
| B08-737 消融实验 | 5646–5648，“删除组件…其他不变”；`sec:statistics-design-information` | 评价组件增量作用。 | 强交互、预算不等的边界 | 不给唯一独立贡献，非任意两系统分数相减。 | 已清楚；无。 |
| B08-738 学习曲线与预算类型 | 5650–5652，“数据量或计算量对性能”；`sec:statistics-design-information` | 区分方法效率与额外资源。 | 数据、计算、评价时间预算 | 不将反复占用测试集当免费数据。 | 已清楚；无。 |
| B08-739 Neyman分配 | 5654–5662，“n_A/n_B=σ_A/σ_B”；`sec:statistics-design-information` | 同成本预算下最小化均值差方差。 | 求导或Cauchy–Schwarz入口 | 连续分配近似，未知方差／整数／成本另处理。 | 已清楚；可选注明两方差正的内部解条件。 |
| B08-740 线性设计的方向方差 | 5664–5680，“σ²aᵀ(XᵀX)⁻¹a”；`sec:statistics-design-information` | 根据关心方向配置新观测。 | 满列秩、条件零均值等方差及OLS | 前Gauss–Markov已证明，不重复假定高斯。 | 已清楚；无。 |
| B08-741 最坏、平均与体积设计准则 | 5681–5682，“得到不同设计准则”；`sec:statistics-design-information` | 提醒先声明优化哪个误差摘要。 | 与方向方差式相连 | 当前只预告，不要求读者已知A/D/E最优设计术语。 | 预告清楚；无。 |
| B08-742 主动学习 | 5684–5685，“选择下一批待标注样本”；`sec:statistics-design-information` | 从已有数据分析转向预算内获取新信息。 | 后期望增量公式 | 会改变被标注数据分布，不是固定iid抽样。 | 已清楚；无。 |
| B08-743 期望效用增量 | 5685–5693，“U含收益与查询成本”；`sec:statistics-design-information` | 给查询选择的一般目标。 | argmax_x E[U(D∪(x,Y))−U(D)] | 期望依当前预测Y∣x,D，效用方向须一致。 | 公式清楚；后风险特例符号见B-037。 |
| B08-744 不确定性采样 | 5693，“一种替代规则”；`sec:statistics-design-information` | 区分易实现启发式与任务最优价值。 | 不一定等于最大任务价值的说明 | 高不确定样本可能噪声也大。 | 已清楚；无。 |
| B08-745 后验熵下降与互信息 | 5694–5695，“U=-H”；`sec:statistics-design-information` | 预告信息论的特定效用选择。 | 负熵差式及下一章准确前指 | 熵与互信息尚未定义，纯预告不当作已学结论。 | 预告清楚；无。 |
| B08-746 最优风险与信息价值 | 5696–5697，“U取…最优风险”；`sec:statistics-design-information` | 想把查询效用接到决策误差下降。 | 未加负号，和前argmax方向冲突 | 风险越小越好，效用越大越好。 | 技术疑点；B-037，取U=-最优风险。 |
| B08-747 自适应获取与独立评价边界 | 5699–5705，“池覆盖、噪声、独立评价”；`sec:statistics-design-information` | 说明查询规则本身改变推断保证。 | 三项失败来源及可预测设计回指 | 提高信息不等于任务收益；偷看当前噪声不可套前界。 | 已清楚；无。 |

## 本章结论与后续

本章747项概念均已落盘，1–5715行完整读完，无未完成段落。独立小结5707–5715行逐项收拢了开篇读数对象、联合关系、变换、重复观测、过程、推断及设计问题，没有在结尾新引入未解释的证明依赖。

本章实质问题为`R1-B-011`至`R1-B-037`，共27项；其中技术疑点4项（015、031、035、037）、局部费力23项、阻断理解0项。后文共形秩已正确处理并列，不能倒补1106行的首次遗漏。4537行有限离散Jensen不依赖B-013缺失的一般条件版本。图注提供的教学对象与用途可核对；未做PDF视觉轮，也未将解析图／有限模拟图当作定理证明。

第9–11章现也已完成顺读，整组统计见`reader-b.md`。主代理隔离准备稿未读，正式源未编辑，所有问题仍待统一修订及受影响上下文复读。
