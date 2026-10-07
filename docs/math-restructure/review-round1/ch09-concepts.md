# 第9章概念审读清单（独立读者B，第一轮）

## 版本与覆盖

- 源文件：`tex/01-mathematical-preliminaries/03-random-variables-distributions-and-causality/02-information-theory-and-statistical-geometry.tex`。
- 冻结 SHA-256：`ceeeac93830b50eb100620d9f02383be69de07845b841ba86923b5556b6d1f6b`，本章开始前及完成时均已与冻结清单核对；完成时也重核第7、8、10、11章，均一致。
- 全章2300行、67733源字符已连续完整顺读；读取块为1–240、241–470、470–710、710–930、930–1145、1145–1360、1361–1580、1580–1800、1801–2020、2020–2250、2250–2300，重叠行用于接续定义和图注。没有跳过块内证明、算例、图注或表，独立本章小结也已读完。
- 清单共314项，本章审读完成；第7–11章整组首轮状态见`reader-b.md`。
- 表前节标签及本章源路径共同适用于各行。首次位置给实际行号和短引文；纯预告与正式定义区别记录。图仅核对当前说明的理解支撑，不作PDF视觉验收。

## 已核对的边界依赖

路径以`tex/01-mathematical-preliminaries/`为前缀；均实际展开，未以标题替代阅读。

| 前章文件 | 实读范围 | 用途与结论 |
| --- | --- | --- |
| `01-mathematical-language-combinatorics-analysis-optimization/05-functional-analysis-and-approximation.tex` | 112–181、1253–1439 | L²积分内积、平行四边形恒等式、L²版Minkowski完整证明；有界线性泛函、Riesz表示全部证明、再生性质、点值界、正定核和仿射RKHS算例。MMD中的期望泛函确实有前置工具。1439是下一图开始，不据此认定该图已读。 |
| `01-mathematical-language-combinatorics-analysis-optimization/03-mathematical-analysis.tex` | 1859–1919 | 微积分基本定理、分部积分、Taylor积分余项及全部推导，支持Pinsker的二階下界。 |
| `02-linear-algebra-and-geometry/01-linear-algebra-and-matrix-analysis.tex` | 196–276、966–1065、2489–2534 | Cauchy–Schwarz、有限维Hölder、Young证明及有限维三角不等式；伪逆的构造、唯一性、最小范数全部证明及算例图注；逆扰动和条件数。前1–8章检索未见一般积分Hölder；第5章只建立L²版Minkowski。本章一般指数使用缺少推广桥，见R1-B-038。 |
| `01-mathematical-language-combinatorics-analysis-optimization/04-optimization.tex` | 1544–1629、1640–1730、1808–1867 | 对偶函数与弱对偶、闭凸集严格分离及证明、共轭与双共轭定义、Fenchel–Moreau完整证明、有限维LP强对偶完整证明。1544–1571是此前算例的尾部，不据此声称整个算例补读完整；1615后支撑面为附带完整阅读。支持有限熵共轭和有限OT对偶的准确回指。 |
| `03-random-variables-distributions-and-causality/01-random-variables.tex` | 全章已完整读；另重核493–552 | 指数族、自然参数空间、配分导数和冗余警示已有；但未定义“最小正则表示”。552是Bernoulli例接续行，本次复核不取代原先完整阅读。 |

第7章1–2072、第8章1–5715已由本读者完整顺读。第8章的分布、条件核、RN换测度、次高斯、独立样本集中、停时和统计风险可回用；其未解决缺口不因本章再次引用而视为已建立。特别是条件Jensen沿用R1-B-013、白化沿用R1-B-017、Hoeffding常数证明沿用R1-B-018，不在本章重复编号。第3章测度／收敛、前章覆盖与伪距离的已实际补读范围见ch08清单；后续若新增边界调用再追加。

## 信息量

节标签：章首`chap:information-theory-and-statistical-geometry`；`sec:information-uncertainty-prediction`、`sec:information-entropy`、`sec:information-unconditional-information`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-001 固定分布与随机概率测度 | 11–14，“不表示P自身必然随机”；`chap:information-theory-and-statistical-geometry` | 限定本章研究对象；算法输出分布才另带样本随机性。 | 记录／预测开篇问题 | 第8章已回顾；随机变量的规律不等于随机规律。 | 已清楚；无。 |
| B09-002 参数距离与分布距离 | 16–18，“噪声较小时更容易被辨认”；`chap:information-theory-and-statistical-geometry` | 动机预告，参数坐标不是客观差异。 | 高斯均值及立方根参数例；后319 | 不是正式引入特定距离。 | 预告清楚；无。 |
| B09-003 信息单位nat | 19，“自然对数”；`chap:information-theory-and-statistical-geometry` | 固定数值与常数口径。 | 与bit换算式 | 不等于概率单位。 | 已清楚；无。 |
| B09-004 信息单位bit | 19–20，“以二为底”；`chap:information-theory-and-statistical-geometry` | 对接二进制编码。 | `1 bit=(log 2) nat` | 编码处与一般自然对数明确分开。 | 已清楚；无。 |
| B09-005 自信息 | 35–38，“单次结果的量”；`sec:information-unconditional-information` | 独立概率相乘但描述长度相加；p>0。 | `-log p(x)`、Bernoulli的2 bit | 单次意外程度，不是平均熵。 | 已清楚；无。 |
| B09-006 字母表 | 42，“有限或可数字母表”；`sec:information-unconditional-information` | 规定离散结果集合X。 | Bernoulli的两个结果 | 已回顾离散取值集合；名称可由此句读懂。 | 已清楚；无。 |
| B09-007 离散熵 | 40–48，“自信息的平均”；`sec:information-unconditional-information` | 测量已知规律的不确定性。 | `eq:information-discrete-entropy`、0.5623 nat | 与单次自信息不同。 | 已清楚；无。 |
| B09-008 零概率项与扩展熵 | 49–53，“可以为+∞”；`sec:information-unconditional-information` | 避免零乘对数和无穷减法问题。 | `0 log 0=0`及绝对可积式 | 非负扩展积分已回顾；有限性不是自动。 | 已清楚；无。 |
| B09-009 常量熵与均匀熵 | 56，“熵为零…log m”；`sec:information-unconditional-information` | 给熵的两个基准。 | 常量及m个等概率结果 | 这里先算均匀值，最大性后由Gibbs建立。 | 已清楚；无。 |
| B09-010 二进制前缀码 | 65–66，“都不是另一个…前缀”；`sec:information-unconditional-information` | 平均理想长度必须配合可解码性。 | `0,10,11`正例与`0,01`反例 | 不仅是给结果分配任意串。 | 已清楚；无。 |
| B09-011 整数码长ℓ | 67，“非负整数”；`sec:information-unconditional-information` | 与实数理想长度区分。 | Bernoulli逐符号1 bit | 允许空码字的边界后114说明。 | 已清楚；无。 |
| B09-012 Kraft约束 | 67–73，“后代不能重叠”；`sec:information-unconditional-information` | 给前缀可实现长度的质量预算。 | 二叉树解释与`Σ2^-ℓ≤1` | 二叉树直观已足，不需后图论定理。 | 已清楚；无。 |
| B09-013 理想实数码长 | 72，“恰好使总和为一”；`sec:information-unconditional-information` | 解释负对数如何接到编码。 | `-log₂p`代入Kraft | 未声称实数长度能逐符号实现。 | 已清楚；无。 |
| B09-014 无失真平均码长下界 | 75–80，“任意满足Kraft约束”；`sec:information-unconditional-information` | 从可解码性得熵下界。 | `thm:information-source-coding-bound`及88–100证明 | 无需预借KL；用基本对数不等式。 | 已清楚；无。 |
| B09-015 有效字母表 | 81，“p(x)>0”；`sec:information-unconditional-information` | 明确取整方案不为零质量符号留空间。 | X₊、113–115边界说明 | 与原声明字母表区别清楚。 | 已清楚；无。 |
| B09-016 Shannon取整码长 | 82–85，“ceil(-log₂p)”；`sec:information-unconditional-information` | 给离熵不足一位的可实现方案。 | 102–108二进区间构造 | 上界是平均冗余，不是每个码长等于自信息。 | 已清楚；无。 |
| B09-017 二进区间的码构造 | 103–107，“左端点…网格对齐”；`sec:information-unconditional-information` | 证明Kraft充分性而非只引用。 | 半开区间互不相交与前缀嵌套矛盾 | 可数字母表按长度排序已有有限层说明。 | 已清楚；无。 |
| B09-018 块编码与每符号冗余 | 111–114，“小于1/n bit”；`sec:information-unconditional-information` | 把逐符号整数损失摊薄。 | iid块熵nH与长度上界 | 独立性必要；148–154正式链式分解补接。 | 已清楚；无。 |
| B09-019 空码字约定 | 114–115，“符号个数已知”；`sec:information-unconditional-information` | 解释单一结果时零长度为何可解码。 | 一个有效符号 | 与传输未知消息长度不同。 | 已清楚；无。 |
| B09-020 有失真编码 | 115–116，“另一任务”；`sec:information-unconditional-information` | 限制熵编码结论的范围。 | 无算法或公式 | 纯边界预告，明说需失真准则。 | 预告清楚；无。 |

## 条件及连续信息量

节标签：`sec:information-remaining-information`、`sec:information-continuous-information`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-021 给定值的条件熵 | 121–127，“都知道Y=y”；`sec:information-remaining-information` | 编码对象改为当地条件分布，p(y)>0。 | `H(X\|Y=y)` | 第8章条件分布已回顾；不是平均条件熵。 | 已清楚；无。 |
| B09-022 平均条件熵 | 128–135，“这些剩余信息量的平均”；`sec:information-remaining-information` | 把各条件值的描述量合起来。 | `eq:information-conditional-entropy` | 零质量版本随意，非负项允许∞。 | 已清楚；无。 |
| B09-023 联合熵及二元分解 | 137–147，“H(Y)+H(X\|Y)”；`sec:information-remaining-information` | 先描述Y再描述X。 | 联合质量分解及负对数平均 | 非负求和换序已回顾；无需独立。 | 已清楚；无。 |
| B09-024 熵链式法则 | 148–155，“反复分解”；`sec:information-remaining-information` | 多变量顺次记录信息。 | `eq:information-entropy-chain-rule` | 独立才能删条件；熵差需有限。 | 已清楚；无。 |
| B09-025 独立二元翻转通道 | 157–165，“Y=X⊕N”；`sec:information-remaining-information` | 可算剩余不确定性实例。 | `ex:information-binary-channel` | 异或已写名称；独立Bernoulli噪声条件明确。 | 已清楚；无。 |
| B09-026 二元熵函数H_b | 166–171，“端点沿用零项约定”；`sec:information-remaining-information` | 汇总翻转噪声的信息损失。 | ε=1/4、0、1/2三个值 | 不等于翻转概率本身；平均不保证恢复。 | 已清楚；无。 |
| B09-027 精度／量化格熵 | 181–185，“宽度Δ的小格”；`sec:information-continuous-information` | 解释连续记录为何额外付精度代价。 | `-∫p log p-log Δ` | 仅规则密度近似，未冒充一般极限定理。 | 已清楚；无。 |
| B09-028 参考测度下的熵h_μ | 187–193，“固定参考测度”；`sec:information-continuous-information` | 连续密度必须有比较基准。 | `-∫p log p dμ`、对数绝对可积条件 | RN密度已回顾；不是坐标无关绝对量。 | 已清楚；无。 |
| B09-029 微分熵 | 194–202，“取Lebesgue测度”；`sec:information-continuous-information` | 给通常欧氏连续熵口径。 | 区间[0,1/2]的`-log2` | 密度可大于1，负值不是负码长。 | 已清楚；无。 |
| B09-030 参考测度缩放效应 | 198–199，“μ′=aμ”；`sec:information-continuous-information` | 说明参考选择进入数值。 | `h_μ′=h_μ+log a` | 与分布本身改变不同。 | 已清楚；无。 |
| B09-031 微分熵换元 | 204–214，“Jacobian”；`sec:information-continuous-information` | 区分坐标单位与观测信息。 | `eq:information-differential-entropy-transform`及密度推导 | 第8章换元、第7章微分同胚已回顾；需对数Jacobian可积。 | 已清楚；无。 |
| B09-032 仿射尺度效应 | 215–219，“米改成厘米”；`sec:information-continuous-information` | 给换元公式可感知的特例。 | `log\|det A\|`、`log100` | 与下节比值中Jacobian相消对比。 | 已清楚；无。 |

## 对数评分与KL

节标签：`sec:information-log-score-kl`，上层`sec:information-comparison-identification`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-033 对数损失 | 232–234，“按Q分配的理想码长”；`sec:information-log-score-kl` | 评价预测概率低估真实结果的代价。 | `-log q(x)` | 与真实p的自信息不同。 | 已清楚；无。 |
| B09-034 离散交叉熵 | 236–246，“平均…仍是P”；`sec:information-log-score-kl` | 把失配编码代价在真实规律下平均。 | `eq:information-cross-entropy` | 不是Q的熵；p正q零为∞。 | 已清楚；无。 |
| B09-035 绝对连续P≪Q | 248–259，“若P不≪Q…+∞”；`sec:information-log-score-kl` | 判断参考规律是否覆盖全部真实事件。 | q=0<p支持例 | 第8章已回顾，方向不对称。 | 已清楚；无。 |
| B09-036 RN密度比L | 252–256，“dP/dQ”；`sec:information-log-score-kl` | 统一离散连续比较。 | 两种积分形式相等 | 第8章RN及换测度已回顾。 | 已清楚；无。 |
| B09-037 相对熵／KL散度 | 250–265，“预测失配”；`sec:information-log-score-kl` | 从描述差剥离真实不确定性。 | `eq:information-kl-divergence` | 可∞，绝对连续不保证有限。 | 已清楚；无。 |
| B09-038 KL负部可积 | 262–264，“≤1/e”；`sec:information-log-score-kl` | 使扩展值定义无∞−∞。 | `-L log L`的有界性 | 与绝对可积／有限KL不同。 | 已清楚；无。 |
| B09-039 交叉熵分解 | 266–273，“多余代价恰是KL”；`sec:information-log-score-kl` | 联系预测目标与分布失配。 | `eq:information-cross-entropy-decomposition` | 真实熵∞时不能用无限交叉熵排序。 | 已清楚；无。 |
| B09-040 Gibbs不等式 | 275–291，“等号当且仅当P=Q”；`sec:information-log-score-kl` | 确立KL的零基准与辨别性。 | 完整共同支配测度及对数不等式证明 | 未把KL当度量。 | 已清楚；无。 |
| B09-041 共同支配测度P+Q | 281，“取…μ=P+Q”；`sec:information-log-score-kl` | 同时写两密度并处理额外支持。 | r=q/p、Q在p=0的质量 | 测度求和已可读；不要求Lebesgue密度。 | 已清楚；无。 |
| B09-042 严格适当性 | 293–297，“如实报告概率…最优”；`sec:information-log-score-kl` | 从Gibbs解释概率预测的总体准则。 | KL唯一零；连续需额外可积 | 不是经验最优必拟合正确。 | 已清楚；无。 |
| B09-043 KL方向性 | 299–305，“谁来加权”；`sec:information-log-score-kl` | 防止交换P,Q。 | Bernoulli 0.2263／0.3112 | 支持失败也依方向。 | 已清楚；无。 |
| B09-044 KL非三角性 | 306–312，“不是…距离”；`sec:information-log-score-kl` | 阻止把散度直接当度量。 | Bernoulli三点0.1163>0.0624 | 对称化也不在此自动解决三角性。 | 已清楚；无。 |
| B09-045 等方差高斯位置KL | 314–321，“交叉项均值为零”；`sec:information-log-score-kl` | 回应开篇噪声和均值位移。 | `eq:information-gaussian-location-kl` | 第8章Gaussian密度可回顾。 | 已清楚；无。 |
| B09-046 向量高斯的协方差加权差 | 322–329，“低方差方向…更容易辨认”；`sec:information-log-score-kl` | 将一维尺度推广为方向尺度。 | `eq:information-vector-gaussian-translation-kl` | 正定Σ；白化在第8章仍有B-017缺口。 | 公式清楚；白化术语沿B-017补，不重复编号。 |
| B09-047 奇异高斯的仿射支持 | 330–333，“同…range(Σ)”；`sec:information-log-score-kl` | 限制伪逆公式合法范围。 | 支持同则Σ†，不同则∞ | 第8章退化Gaussian与第6章值域／伪逆已回顾。 | 已清楚；无。 |
| B09-048 KL可逆推送不变性 | 335–336，“L∘g⁻¹”；`sec:information-log-score-kl` | 建立不同坐标下同一个差异。 | 密度比换元；Jacobian抵消 | 逆也须可测，强于任意可测处理。 | 已清楚；无。 |
| B09-049 共同核后的密度比 | 337–341，“E_Q[L(X)\|Y]”；`sec:information-log-score-kl` | 非可逆处理后只保留Y所见的权重。 | 显式RN式 | 第8章条件换测度、共同核已回顾。 | 已清楚；无。 |
| B09-050 KL后处理收缩 | 342–348，“必须…同一处理规则”；`sec:information-log-score-kl` | 量化丢失差异而非坐标改变。 | u log u条件Jensen证明 | 条件Jensen的前置缺口已报B-013。 | 结论清楚；沿B-013补依据，不重复编号。 |

## 联合与条件信息

节标签：`sec:information-unconditional-mi`、`sec:information-conditional-mi`，上层`sec:information-mutual-relations`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-051 边缘乘积规律 | 353–365，“保持…边缘，却令…独立”；`sec:information-mutual-relations` | 设立只去掉依赖的比较基准。 | P_X⊗P_Y | 第8章独立分布已回顾；不改变边缘。 | 已清楚；无。 |
| B09-052 互信息 | 360–369，“联合关系”；`sec:information-unconditional-mi` | 用KL测依赖，允许一般空间与∞。 | `eq:information-mutual-information` | 不要求先有联合Lebesgue密度。 | 已清楚；无。 |
| B09-053 零互信息与独立 | 371，“当且仅当…独立”；`sec:information-unconditional-mi` | 给信息量可解释零点。 | Gibbs直接应用 | 与零协方差不同。 | 已清楚；无。 |
| B09-054 非线性依赖的识别 | 372–374，“Y=X²”；`sec:information-unconditional-mi` | 说明二阶摘要可能漏掉依赖。 | 三点均匀X及H_b(1/3)>0 | 第8章零相关反例回顾，现换信息计量。 | 已清楚；无。 |
| B09-055 互信息的熵减表达 | 375–382，“平均消除的不确定性”；`sec:information-unconditional-mi` | 接回条件编码。 | `eq:information-mi-entropy-reduction` | 联合熵有限才能直接相减；连续更需有限微分熵。 | 已清楚；无。 |
| B09-056 奇异联合的无限互信息 | 383–384，“落在对角线上”；`sec:information-unconditional-mi` | 限制连续密度公式。 | 连续Y=X | 与离散确定映射有限熵例不同。 | 已清楚；无。 |
| B09-057 二元通道的信息分配 | 386–395，“两条曲线相加…log2”；`sec:information-unconditional-mi` | 可视解释噪声改变哪一部分。 | `fig:information-binary-channel-information`及解析图注 | 输入熵固定，剩余熵和MI互补。 | 图注支持理解；无。 |
| B09-058 互信息的可逆不变性 | 396–397，“分别施加可逆变换”；`sec:information-unconditional-mi` | 区别微分熵的单位敏感性。 | 联合及边缘同时推送 | 来自KL，要求保留全部信息。 | 已清楚；无。 |
| B09-059 正则条件分布版本 | 407、415–418，“标准Borel空间”；`sec:information-conditional-mi` | 保证条件核定义可用。 | 对P_Z-a.e.版本平均 | 第8章已建立存在边界；一般拓扑表述B-014仍待修。 | 当前条件明确；不重复编号。 |
| B09-060 条件互信息 | 402–416，“同一个条件值下”；`sec:information-conditional-mi` | 衡量已知Z后残余关联。 | `eq:information-conditional-mutual-information` | 非负KL积分，不是任意三个MI相减。 | 已清楚；无。 |
| B09-061 零条件互信息与条件独立 | 419–421，“条件边缘乘积”；`sec:information-conditional-mi` | 将信息零点与前章结构条件相连。 | 条件KL为零a.e. | 条件熵差需有限。 | 已清楚；无。 |
| B09-062 条件化可增减依赖 | 423–426，“并不一定…变小”；`sec:information-conditional-mi` | 防止把数据处理错误用于条件化。 | XOR增至log2；X=Y=Z降至0 | 约束揭示与去除共享信息不同。 | 已清楚；无。 |
| B09-063 KL条件链式分解 | 428–439，“边缘比与条件比的乘积”；`sec:information-conditional-mi` | 供后处理和序贯信息累积。 | `eq:information-kl-conditional-chain` | 条件核存在、绝对连续及负部可积已说明。 | 已清楚；无。 |
| B09-064 互信息链式法则 | 440–447，“I(X;Y)+I(X;Z\|Y)”；`sec:information-conditional-mi` | 分解新增观测带来的信息。 | 选Q=P_X⊗P_YZ的实际对应 | 不靠无限熵相减。 | 已清楚；无。 |
| B09-065 Markov关系X→Y→Z | 451–452，“即X⊥Z\|Y”；`sec:information-conditional-mi` | 指定后处理无额外输入信息。 | 确定映射及随机通道例 | 第8章条件独立回顾；不是一般因果箭头。 | 已清楚；无。 |
| B09-066 数据处理不等式 | 449–464，“I(X;Z)≤I(X;Y)”；`sec:information-conditional-mi` | 证明共同后处理不能增信息。 | 两种MI链式分解完整证明 | 只加非负项，允许∞。 | 已清楚；无。 |
| B09-067 后处理独立随机性与取等 | 466–468，“额外随机性…与X关联”；`sec:information-conditional-mi` | 限制不等式的外推。 | 仅依赖Y的通道、任务无关内容 | MI不增不意味着每任务严格变差。 | 已清楚；无。 |

## 概率权重差异

节标签：`sec:information-probability-discrepancy`，上层`sec:information-distribution-discrepancies`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-068 总变差距离 | 480–491，“所有事件中…改变最多”；`sec:information-probability-discrepancy` | 控制未指定报警规则。 | `eq:information-total-variation` | 事件概率与对数评分不同。 | 已清楚；无。 |
| B09-069 TV半L¹表达 | 493–500，“正部与负部积分相等”；`sec:information-probability-discrepancy` | 给可计算密度式。 | `eq:information-tv-density`完整推导 | 1/2来自两边质量相等。 | 已清楚；无。 |
| B09-070 最优区分事件A* | 495，“{p≥q}达到”；`sec:information-probability-discrepancy` | 识别最能看出差异的事件。 | P(A*)−Q(A*) | 共同支配测度，不需绝对连续方向。 | 已清楚；无。 |
| B09-071 TV测试函数对偶 | 501–509，“值域宽度”；`sec:information-probability-discrepancy` | 将事件控制推广至函数期望。 | `eq:information-tv-dual`、符号函数取等 | [-1,1]常数2，[0,1]常数1。 | 已清楚；无。 |
| B09-072 平方根密度嵌入 | 511–512，“单位L²范数”；`sec:information-probability-discrepancy` | 用Hilbert几何对称比较概率。 | ∫p=1 | 与直接比较密度的L¹不同。 | 已清楚；无。 |
| B09-073 Hellinger距离 | 514–523，“距离本身…平方根”；`sec:information-probability-discrepancy` | 定义平方根函数的L²距离。 | `eq:information-hellinger`及Bernoulli算例 | d_H²不是d_H；约定1/2明确。 | 已清楚；无。 |
| B09-074 Hellinger亲和积分 | 519，“1−∫√pq”；`sec:information-probability-discrepancy` | 给距离的等价计算形式。 | 展开平方 | 原文未另命名，作为新积分对象记录。 | 已清楚；无。 |
| B09-075 Hellinger测度无关性 | 524–526，“同一密度因子”；`sec:information-probability-discrepancy` | 确保结果不随共同参考变化。 | 换元及三分布和测度 | L²三角不等式已有。 | 已清楚；无。 |
| B09-076 Hellinger–TV比较界 | 527–535，“≤√2 d_H”；`sec:information-probability-discrepancy` | 将两类比较尺度衔接。 | 因式分解与Cauchy–Schwarz | 只给控制方向，不说数值相等。 | 已清楚；无。 |
| B09-077 Pinsker不等式 | 537–545，“自然对数”；`sec:information-probability-discrepancy` | 从KL推出事件稳定性。 | `eq:information-pinsker` | 对数底影响常数。 | 已清楚；无。 |
| B09-078 二元化证明工具 | 547–554，“A及其补集”；`sec:information-probability-discrepancy` | 将一般KL缩为可算二元KL。 | a=P(A)、b=Q(A)的式子 | 此处用积分Jensen，B-013的前置问题仍影响。 | 证明方向清楚；沿B-013补，不重复编号。 |
| B09-079 二元KL曲率下界 | 555–558，“二阶导数…≥4”；`sec:information-probability-discrepancy` | 得到Pinsker的1/2常数。 | Taylor积分余项 | 第3章1859–1919已实际补读。 | 已清楚；无。 |
| B09-080 TV小不反控KL | 561–570，“这个控制不能反用”；`sec:information-probability-discrepancy` | 避免把单向界当等价尺度。 | Bernoulli数值、稀有新支持使KL∞ | 支持与概率质量大小区别明确。 | 已清楚；无。 |
| B09-081 高阶密度比矩 | 572–584，“极端密度比…放大”；`sec:information-probability-discrepancy` | 为稀有事件迁移换一种控制。 | E_Q L^α | 是权重尾部，不是样本位置尾部。 | 已清楚；无。 |
| B09-082 Rényi散度α>1 | 575–585，“该阶矩无限…+∞”；`sec:information-probability-discrepancy` | 规范化高阶矩的对数。 | `eq:information-renyi-divergence` | 未声称覆盖α≤1；方向同KL。 | 已清楚；无。 |
| B09-083 Rényi非负性 | 587–588，“E L^α≥1”；`sec:information-probability-discrepancy` | 验证零基准。 | Jensen及E_QL=1 | 一般积分Jensen沿B-013。 | 结论清楚；不重复编号。 |
| B09-084 对数矩凸性 | 589，“由Hölder…凸”；`sec:information-probability-discrepancy` | 为阶数排序提供证明。 | K(α)=log E L^α | 积分Hölder未建立，仅有限维已核对。 | 局部费力；R1-B-038补积分式与Young积分证明。 |
| B09-085 Rényi阶数单调性 | 590，“割线斜率…不减”；`sec:information-probability-discrepancy` | 解释高阶更强调大权重。 | K(1)=0、凸函数割线 | 凸性前提承接B09-084。 | 随B-038补接；无需另项。 |
| B09-086 Rényi趋于KL | 591–595，“某个α₀…有限”；`sec:information-probability-discrepancy` | 连接新旧散度。 | 右导数E L log L，D₂=log1.25 | 第3章积分求导已核对；局部更高矩可支配导数。 | 基本清楚；可选补一句支配依据，不计实质问题。 |

## 测试函数尺度

节标签：`sec:information-test-functions`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-087 积分概率度量IPM | 602–614，“允许的测试函数”；`sec:information-test-functions` | 只比较任务能读到的期望。 | `eq:information-ipm` | 每函数P,Q可积；非空函数类。 | 已清楚；无。 |
| B09-088 伪距离与分布分离 | 615–617，“零值…不同分布”；`sec:information-test-functions` | 限制“度量”名称。 | 有界函数类给2TV；线性核反例 | 前第5章伪距离已回顾；可为∞。 | 已清楚；无。 |
| B09-089 RKHS单位球 | 618–630，“核能够表示的函数”；`sec:information-test-functions` | 固定一类有范数约束的测试。 | ‖f‖_H≤1 | 第5章点值及核已实际补读。 | 已回顾且衔接清楚；无。 |
| B09-090 MMD | 620–632，“最大均值差异”；`sec:information-test-functions` | 在核测试类内取最大期望差。 | 定义式、后线性／Gaussian对照 | 不是只比较普通数值均值。 | 已清楚；无。 |
| B09-091 核均值可积条件 | 622–626、634–636，“E√k(X,X)<∞”；`sec:information-test-functions` | 保证每个RKHS函数期望及有界读取。 | 再生点值界 | 比先假定Hilbert值积分存在更具体。 | 已清楚；无。 |
| B09-092 期望有界泛函 | 634–638，“f↦E_P f”；`sec:information-test-functions` | 将分布读数表示为一个空间向量。 | ‖f‖√k界、Riesz定理 | 第5章1253–1341完整补读可用。 | 已清楚；无。 |
| B09-093 核均值嵌入μ_P | 637–640，“全部核函数的平均作用”；`sec:information-test-functions` | 给分布在H中的代表。 | E_P f=〈f,μ_P〉 | E k(X,·)由代表元解释，不越过向量积分前提。 | 已清楚；无。 |
| B09-094 MMD的范数表达 | 641–648，“归一化方向达到”；`sec:information-test-functions` | 由无限测试化成两个代表元距离。 | ‖μ_P−μ_Q‖_H及取等函数 | Cauchy–Schwarz、Riesz范数已回顾。 | 已清楚；无。 |
| B09-095 特征核 | 650–655，“核均值映射为单射”；`sec:information-test-functions` | 判断MMD是否真正分离分布。 | `def:information-characteristic-kernel` | 指定分布类，不等于正定核或有限Gram可逆。 | 已清楚；无。 |
| B09-096 线性核只读均值 | 657–660，“只比较普通均值”；`sec:information-test-functions` | 展示非特征测试类遗漏差异。 | δ₀与对称±1混合 | 相同一阶均值不等于同分布。 | 已清楚；无。 |
| B09-097 MMD独立副本展开 | 661–670，“展开核均值范数”；`sec:information-test-functions` | 让总体MMD可由核期望计算。 | 三个独立乘积期望及核Cauchy界 | 不是同一变量重复代入的对角期望。 | 已清楚；无。 |
| B09-098 Gaussian核区分算例 | 661–678，“不代替…特征性证明”；`sec:information-test-functions` | 固定分布只改变核来解释敏感性。 | 精确式、`fig:information-kernel-distinguishability`、约0.595 | 总体算例不冒充样本估计或全类定理。 | 图注支持且边界清楚；无。 |

## 搬运尺度

节标签：`sec:information-optimal-transport`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-099 最优传输OT | 683–687，“最便宜配对”；`sec:information-optimal-transport` | TV无法表达相邻点质量的小位移。 | 0.01度温度例 | 比较位置，不只概率权重。 | 已清楚；无。 |
| B09-100 耦合 | 689–698，“乘积空间…边缘”；`sec:information-optimal-transport` | 配对但保持两边概率。 | 两个边缘约束、Π(P,Q) | 不等于独立，也不改变质量。 | 已清楚；无。 |
| B09-101 独立耦合 | 699–700，“总存在”；`sec:information-optimal-transport` | 保证可行集合非空。 | P⊗Q | 存在不等于最优。 | 已清楚；无。 |
| B09-102 非负成本c | 701，“非负可测成本”；`sec:information-optimal-transport` | 明确搬运什么代价。 | ∫c dγ | 一般c未必是距离；后749明说。 | 已清楚；无。 |
| B09-103 Kantorovich代价 | 701–708，“对耦合取下确界”；`sec:information-optimal-transport` | 在可行配对中找最便宜。 | `eq:information-kantorovich-transport` | 达到性和求解被明确留后，不伪称已证。 | 已清楚；无。 |
| B09-104 有限r阶矩类P_r | 712–717，“固定基点”；`sec:information-optimal-transport` | 保证距离有限并控制函数增长。 | ∫d(x,x₀)^r dP<∞ | Polish度量本处明确完备可分。 | 已清楚；无。 |
| B09-105 Wasserstein距离W_r | 710–725，“1≤r<∞”；`sec:information-optimal-transport` | 以底层距离幂定义分布位移。 | `eq:information-wasserstein-distance` | 取r次根，区别一般T_c。 | 已清楚；无。 |
| B09-106 矩条件基点无关 | 727–728，“不依赖基点”；`sec:information-optimal-transport` | 防止定义被任意x₀改变。 | 2^(r−1)幂和界 | 同式保证独立配对成本有限。 | 已清楚；无。 |
| B09-107 对角耦合 | 729，“W_r(P,P)=0”；`sec:information-optimal-transport` | 证明同分布可零位移。 | X=Y配对 | 不是独立耦合。 | 已清楚；无。 |
| B09-108 近最优耦合 | 730–733、748，“误差趋零”；`sec:information-optimal-transport` | 不预设最优解达到也能证度量性质。 | 期望差上界及取极限 | 下确界定义已回顾。 | 已清楚；无。 |
| B09-109 Lipschitz测试分离分布 | 730–733，“逼近闭集…指标”；`sec:information-optimal-transport` | 从W_r=0推出P=Q。 | max{1−kd(x,C),0} | 第8章Portmanteau中已读闭集逼近；非有界任意函数。 | 已清楚；无。 |
| B09-110 粘合引理 | 735–741，“两个配对接起来”；`sec:information-optimal-transport` | 使三角比较有同一个三变量联合。 | P(dx\|y)Q(dy)R(dz\|y) | 第8章正则条件核已有；两相邻边缘核实即可。 | 已清楚；无。 |
| B09-111 一般L^r Minkowski | 742–748，“及Minkowski不等式”；`sec:information-optimal-transport` | 把点间三角性变为平均幂距离三角性。 | 三项L^r式 | 前文只有L²及有限维版本，r一般时未接出。 | 局部费力；R1-B-038补积分Hölder后的同样证明。 |
| B09-112 Kantorovich–Rubinstein对偶 | 752–761，“反向…实质内容”；`sec:information-optimal-transport` | 把W₁与测试函数期望连接。 | `eq:information-kr-duality` | Polish及一阶矩明确；一般反向按定理引用，有限版留后。 | 引用边界清楚；可选加精确定理引文，不计实质问题。 |
| B09-113 锚定Lipschitz函数 | 758–759，“固定f(x₀)=0”；`sec:information-optimal-transport` | 消去常数自由度并保证可积。 | 一阶增长界 | 不改变P,Q期望差。 | 已清楚；无。 |
| B09-114 W₁与IPM的交叠 | 762，“r>1…没有…同一个…表达”；`sec:information-optimal-transport` | 防止把比较方式当互斥类别或机械推广。 | KR等式 | W_r非同一Lipschitz单位球。 | 已清楚；无。 |
| B09-115 高斯恒定位移耦合 | 764–771，“Y=X+ν−μ”；`sec:information-optimal-transport` | 计算同方差W₂精确值。 | `eq:information-gaussian-location-wasserstein`及均值下界 | 只需二阶Cauchy／方差非负。 | 已清楚；无。 |
| B09-116 高斯TV交点计算 | 772–780，“c=(μ+ν)/2”；`sec:information-optimal-transport` | 对照可辨识性与位移。 | 正密度差半轴及Φ式 | 第8章标准正态CDF已回顾。 | 已清楚；无。 |
| B09-117 高斯三尺度对照 | 779–790，“纵轴不同”；`sec:information-optimal-transport` | 直接回答开篇噪声与均值移动。 | `fig:information-gaussian-distances`及数值例 | 不按曲线高度排名概念强弱。 | 图注支持；无。 |
| B09-118 点质量移动的极限 | 792–794，“TV恒为一…W_r→0”；`sec:information-optimal-transport` | 给拓扑／支持敏感度差别。 | δ₀、δ_ε | 两方向KL都∞，不意味着位置差大。 | 已清楚；无。 |
| B09-119 边缘距离不决定轨迹 | 795–797，“初次抽样永远复制”；`sec:information-optimal-transport` | 限制分布比较对时序的解释。 | iid公平币与固定公平币 | 第8章随机过程有限维联合已回顾。 | 已清楚；无。 |
| B09-120 总体距离与样本估计 | 798–799，“不自动给出便宜…估计”；`sec:information-optimal-transport` | 分开数学量与计算／统计代价。 | 高维经验搬运的边界说明 | 纯后续估计预告，无给速率的承诺。 | 预告清楚；无。 |

## 固定观测下界

节标签：`sec:information-two-candidates`、`sec:information-many-candidates`，上层`sec:information-fixed-observations`、`sec:information-lower-bounds`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-121 观测可区分性下界 | 804–806，“任何程序”；`sec:information-lower-bounds` | 观测接近却目标不同，限制全部估计程序。 | 两点及四点Gaussian例 | 信息下界不是计算复杂度下界。 | 已清楚；无。 |
| B09-122 二元检验规则 | 817–820，“A={ψ=1}”；`sec:information-two-candidates` | 把观测转为候选选择。 | 两种条件错误概率 | 第8章检验背景已回顾。 | 已清楚；无。 |
| B09-123 最小检验错误与TV | 822–829，“1−d_TV”；`sec:information-two-candidates` | 将距离变为不可消除错误。 | `eq:information-binary-testing-tv` | 错误和与等先验总体错误差1/2。 | 已清楚；无。 |
| B09-124 随机化检验 | 828，“[0,1]值函数”；`sec:information-two-candidates` | 检查随机算法能否突破下界。 | TV函数表达 | 不是额外获得关于候选的观测。 | 已清楚；无。 |
| B09-125 Le Cam两点下界 | 831–843，“目标…≥2s”；`sec:information-two-candidates` | 将估计准确性转成可检验选择。 | `thm:information-le-cam` | 目标度量与观测TV是不同空间。 | 已清楚；无。 |
| B09-126 最近目标解码 | 845–852，“距离相等时选0”；`sec:information-two-candidates` | 证明坏事件包含关系。 | 三角不等式及严格误差<s | 并列与阈值≥已相容。 | 已清楚；无。 |
| B09-127 iid KL线性累积 | 854–857，“密度比…乘积”；`sec:information-two-candidates` | 计算整批而非单次信息。 | n D_KL | 要求独立同分布，后文一般历史另算。 | 已清楚；无。 |
| B09-128 Gaussian两点难例 | 858–864，“a=σ/(2√n)”；`sec:information-two-candidates` | 给实际概率及风险尺度。 | KL=1/2、坏概率≥1/4 | 参数间距要随n缩；常数不声称最优。 | 已清楚；无。 |
| B09-129 事件下界转风险下界 | 863，“平方误差…σ²/(16n)”；`sec:information-two-candidates` | 将概率限制转为期望损失限制。 | 平方阈值乘事件概率 | 非负积分下界已回顾。 | 已清楚；无。 |
| B09-130 有限候选索引V | 870–872，“均匀…给定V=v”；`sec:information-many-candidates` | 把多模型识别变为有限消息解码。 | M个条件观测规律P_v | 即使Z连续，索引条件熵仍由有限后验计算。 | 已清楚；无。 |
| B09-131 Fano不等式 | 874–881，“1−(I+log2)/log M”；`sec:information-many-candidates` | 候选数进入信息预算。 | `thm:information-fano` | M≥2；负右侧仅平凡界。 | 已清楚；无。 |
| B09-132 错误指示E的熵分解 | 883–899，“至多…M−1”；`sec:information-many-candidates` | 给Fano可跟随的证明。 | H(V\|Z)按E分解 | 有限均匀熵最大可由Gibbs推出；随机种子可并入Z。 | 已清楚；无。 |
| B09-133 分离／打包候选集 | 901–904，“两两距离至少2s”；`sec:information-many-candidates` | 将计数候选接成估计误差下界。 | 最近邻解码 | 此前虽未查到“打包”正式定义，当地已给完整所需条件。 | 已清楚；可选将泛称“前面打包工具”改准确入口。 |
| B09-134 候选混合观测分布 | 905–908，“P̄=M⁻¹ΣP_u”；`sec:information-many-candidates` | 表达观测中关于索引的信息。 | I=M⁻¹ΣKL(P_v‖P̄) | 不是单个候选模型。 | 已清楚；无。 |
| B09-135 MI的成对KL上界 | 908–914，“负对数…平均”；`sec:information-many-candidates` | 免算混合对数密度。 | 有限Jensen完整不等式 | 第4章有限Jensen足够，不沿用B-013问题。 | 已清楚；无。 |
| B09-136 四候选Gaussian例 | 916–925，“{-3a,-a,a,3a}”；`sec:information-many-candidates` | 同时核对分离和观测接近。 | 有序平均平方距10a²、p_e≥0.2746 | 不仅枚举模型；全批n进入KL。 | 已清楚；无。 |

## 序贯信息

节标签：`sec:information-sequential-accumulation`、`sec:information-adaptive-lower-bounds`，上层`sec:information-sequential-observations`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-137 完整行动观测轨迹 | 930–931，“联合分布…随算法改变”；`sec:information-sequential-observations` | 自适应选择下确定正确比较对象。 | 后两来源例 | 不是只比较无条件单次边缘。 | 已清楚；无。 |
| B09-138 独立Rényi可加性 | 936–948，“独立性使…相乘”；`sec:information-sequential-accumulation` | 为重复机制累积高阶信息。 | 乘积L_t的α矩 | KL取对数和；Rényi需矩的独立乘积。 | 已清楚；可选在乘积符号标有限T。 |
| B09-139 历史条件密度比 | 950–956，“相关的P历史”；`sec:information-sequential-accumulation` | 在非独立序列中分解联合权重。 | L₀∏L_t(Z_t\|Z_<t) | 条件绝对连续、标准Borel已明说。 | 已清楚；无。 |
| B09-140 轨迹KL链式法则 | 957–971，“沿…P实际…历史”；`sec:information-sequential-accumulation` | 累积每步可区分性。 | `eq:information-trajectory-kl-chain` | 与平均两个历史规律不同；负部及有限时域已交代。 | 已清楚；无。 |
| B09-141 同算法的行动核抵消 | 973–974，“历史频率…不会相消”；`sec:information-sequential-accumulation` | 在两个环境间保留真正信息源。 | 同一历史条件行动核 | 算法相同不等于访问分布相同。 | 已清楚；无。 |
| B09-142 同环境的环境核抵消 | 975–976，“剩下条件行动KL”；`sec:information-sequential-accumulation` | 比较策略时改变抵消对象。 | 条件核分解 | 两边同时改变时不能删任一组。 | 已清楚；无。 |
| B09-143 Rényi逐历史统一界 | 978–997，“不能…按P平均”；`sec:information-sequential-accumulation` | 使自适应组合仍可逐步控制。 | Q下反复条件期望、Σ ε_t | 统一确定界比平均历史界强。 | 已清楚；无。 |
| B09-144 有界停止的吸收补齐 | 999–1000，“同一个吸收符号”；`sec:information-sequential-accumulation` | 把随机停止转固定时域。 | 停止后信息代价0 | 第8章停时已回顾；共同规则必要。 | 已清楚；无。 |
| B09-145 无界停止的KL极限条件 | 1001–1005，“均匀可积并收敛”；`sec:information-sequential-accumulation` | 避免由终止直接交换极限期望。 | 截断log L及非负KL单调收敛 | 第8章UI已建立；仅给充分条件。 | 已清楚；无。 |
| B09-146 隐私组合的额外量词 | 1006–1007，“全部相邻输入”；`sec:information-sequential-accumulation` | 限制单对散度的隐私解释。 | 无正式隐私定义，明确需另规定邻接与机制 | 纯应用边界预告。 | 预告清楚；无。 |
| B09-147 访问次数N_T | 1012–1024，“算法和环境共同产生”；`sec:information-adaptive-lower-bounds` | 按来源聚合信息预算。 | 指标求和与E₀N_T乘单次KL | 例子为有限来源；连续状态一般需占用测度。 | 基本清楚；可选显式限定有限／可数(s,a)，不另计实质问题。 |
| B09-148 自适应两来源难例 | 1026–1037，“全部区分信息只来自B”；`sec:information-adaptive-lower-bounds` | 说明信息必须实际访问才获得。 | κ(ε)=−½log(1−16ε²) | 来源选择可自适应，新观测条件独立。 | 已清楚；无。 |
| B09-149 正确识别所需访问下界 | 1038–1048，“至少约14.68次”；`sec:information-adaptive-lower-bounds` | 将错误要求转为采样预算。 | TV≥1−2δ、Pinsker、E₀N_T界 | 是必要预算，不是算法达到性。 | 已清楚；无。 |
| B09-150 小间隔ε⁻²尺度 | 1046–1050，“κ=8ε²+O(ε⁴)”；`sec:information-adaptive-lower-bounds` | 解释难以区分时的信息成本。 | 前式Taylor | 第3章展开已回顾；无界停止另有条件。 | 已清楚；无。 |

## 固定评价的稳定性

节标签：`sec:information-bounded-evaluation`、`sec:information-sensitive-evaluation`、`sec:information-change-measure`，上层`sec:information-fixed-evaluation`、`sec:information-task-stability`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-151 固定评价与选择依赖 | 1055–1065，“只改变数据分布”；`sec:information-task-stability` | 分开分布迁移与挑选评价规则。 | 同预测器两总体的设问 | 有界、Lipschitz、尾部条件可重叠。 | 已清楚；无。 |
| B09-152 分层积分／尾积分表示 | 1070–1075，“f=∫I{f>t}dt”；`sec:information-bounded-evaluation` | 从事件变化直接控制有界损失。 | Tonelli与逐层TV界 | 第3、8章积分及尾概率已回顾。 | 已清楚；无。 |
| B09-153 有界范围的TV期望界 | 1078–1087，“(b−a)d_TV”；`sec:information-bounded-evaluation` | 显示常数来自振幅而非绝对值界名称。 | [-1,1]两点取等、Pinsker联用 | a=b可单独常量处理；不是无界函数保证。 | 已清楚；无。 |
| B09-154 Rényi事件迁移界 | 1089–1108，“单向风险迁移”；`sec:information-bounded-evaluation` | 用高阶权重矩保护罕见事件。 | `eq:information-renyi-event-bound`及0.02例 | α与共轭指数调用积分Hölder，见B-038。 | 公式和零概率条件清楚；补证明工具入口。 |
| B09-155 稀有极端值反例 | 1110–1114，“期望差却恒为1”；`sec:information-bounded-evaluation` | 说明TV小不足控制无界平均。 | ε质量移至1/ε | 与前点质量小位移例的尾部机制不同。 | 已清楚；无。 |
| B09-156 Lipschitz期望稳定界 | 1119–1134，“≤L W₁”；`sec:information-sensitive-evaluation` | 按输入敏感性保护无界但平滑评价。 | 任意耦合积分差的完整推导 | 一阶矩保可积；不依赖KR难方向。 | 已清楚；无。 |
| B09-157 阈值评价的不稳定 | 1136–1151，“变化却为1”；`sec:information-sensitive-evaluation` | 同一位移下区分受保护的任务。 | `fig:information-small-shift-task`及f=x、指标函数 | 指标不连续，不属于统一Lipschitz类。 | 图注支持；无。 |
| B09-158 RKHS任务稳定界 | 1153–1162，“‖f‖ MMD”；`sec:information-sensitive-evaluation` | 核空间敏感性给另一种保护。 | 再生表示与Cauchy–Schwarz | 特征核不保证任意损失在空间且范数小。 | 已清楚；无。 |
| B09-159 底层成本与任务匹配 | 1163–1164，“只比较…亮度”；`sec:information-sensitive-evaluation` | 防止任意距离被解释成任务保障。 | 亮度成本漏掉位置变化 | 距离／核选择本身属于假设。 | 已清楚；无。 |
| B09-160 指数倾斜 | 1172、1190–1194，“按e^f重新加权”；`sec:information-change-measure` | 用指数矩取代逐点密度比控制。 | dQ_f/dQ=e^f/Z_f、两点例 | 第8章指数倾斜可回顾；不搬动样本位置。 | 已清楚；无。 |
| B09-161 配分／归一化因子Z_f | 1190–1194，“0<Z_f<∞”；`sec:information-change-measure` | 使倾斜成为概率且与Q等价。 | Z_f=E_Q e^f | 有界实f保证有限且正。 | 已清楚；无。 |
| B09-162 DV变分下界 | 1174–1181，“每个有界可测”；`sec:information-change-measure` | 将KL转换为期望和对数矩之差。 | `eq:information-dv-lower` | P≪Q；不是任意无界f可直接代。 | 已清楚；无。 |
| B09-163 DV变分等式 | 1182–1187，“sup…有界可测”；`sec:information-change-measure` | 说明测试最优值恰是KL。 | `eq:information-dv-variational` | 允许∞，不保证某个有界函数达到。 | 已清楚；无。 |
| B09-164 倾斜KL恒等式 | 1195–1204，“完整的倾斜恒等式”；`sec:information-change-measure` | 把DV下界化为Gibbs非负性。 | KL(P‖Q_f)=KL(P‖Q)−E_Pf+logZ | 有限KL先分解，∞时另处理。 | 已清楚；无。 |
| B09-165 对数密度比截断 | 1206–1218，“不能…假设…有界”；`sec:information-change-measure` | 建立DV上确界的达到极限。 | f_n夹在±n，e^f_n≤1+L | 支配／单调收敛已回顾；L=0也处理。 | 已清楚；无。 |
| B09-166 两点指数倾斜例 | 1221–1226，“Q_f=(1/4,3/4)”；`sec:information-change-measure` | 给抽象变分恒等式可复算实例。 | Z=2、KL=(3/4)log3−log2 | 改权重不改取值。 | 已清楚；无。 |
| B09-167 无界期望换测度界 | 1228–1238，“g∈L¹(P)”；`sec:information-change-measure` | 将DV延伸到可积但无界损失。 | `eq:information-change-measure-expectation` | P可积及Q指数矩分别列出，用截断支配证明。 | 已清楚；无。 |
| B09-168 参考规律的次高斯条件 | 1239–1242，“所有t∈R”；`sec:information-change-measure` | 提供可优化的对数MGF上界。 | σ²方差代理 | 第8章已回顾；不是P下次高斯假设。 | 已清楚；无。 |
| B09-169 次高斯KL期望差界 | 1243–1258，“√(2σ²KL)”；`sec:information-change-measure` | 两侧倾斜并择最优λ。 | `eq:information-subgaussian-change-measure`及Gaussian取等 | 零KL／零代理分别处理；不是高概率结论。 | 已清楚；无。 |

## 数据依赖评价

节标签：`sec:information-mi-generalization`、`sec:information-pac-bayes`，上层`sec:information-data-dependent-evaluation`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-170 随机算法输出W | 1264–1267，“根据S输出”；`sec:information-data-dependent-evaluation` | 评价参数不再可当抽样前固定。 | 比较P_SW与P_S⊗P_W | 第8章数据依赖选择已回顾。 | 已清楚；无。 |
| B09-171 总体风险R | 1272–1278，“新样本…同…总体”；`sec:information-mi-generalization` | 固定w的真实评价基准。 | E_Z ℓ(w,Z) | 第8章风险已回顾，ℓ∈[0,1]。 | 已清楚；无。 |
| B09-172 经验风险R̂_S | 1277，“样本平均”；`sec:information-mi-generalization` | 记录训练样本给出的评价。 | n⁻¹Σℓ(w,Z_i) | 不等于数据依赖w下无偏估计。 | 已清楚；无。 |
| B09-173 有符号泛化差g | 1278–1281，“R−R̂”；`sec:information-mi-generalization` | 量化选择产生的平均偏差。 | 固定w时E_Sg=0 | 与绝对误差及高概率不同。 | 已清楚；无。 |
| B09-174 解除依赖的参考分布 | 1282–1291，“边缘乘积”；`sec:information-mi-generalization` | 固定参数集中界在独立组合下成立。 | MGF≤exp(t²/8n)、Q=P_S⊗P_W | Hoeffding常数入口B-018仍待修，后续逻辑完整。 | 已清楚；沿既有问题补工具。 |
| B09-175 互信息泛化界 | 1292–1300，“平均有符号…绝对值”；`sec:information-mi-generalization` | 用输出依赖量付换测度代价。 | `eq:information-mi-generalization` | 不是E\|差\|也不是逐样本界，∞无保证。 | 已清楚；无。 |
| B09-176 有限输出的信息预算 | 1302–1304，“只能输出M种”；`sec:information-mi-generalization` | 给MI界容易使用的上界。 | I≤H(W)≤logM；忽略数据时I=0 | 零平均偏差仍可样本波动。 | 已清楚；无。 |
| B09-177 确定连续输出的无限信息 | 1305–1306，“维数有限…不能保证”；`sec:information-mi-generalization` | 限制用参数个数替信息量。 | 前Y=X对角奇异例提供机制 | 不声称所有连续输出都无限。 | 已清楚；无。 |
| B09-178 PAC–Bayes候选分布 | 1311–1314，“见数据后选择”；`sec:information-pac-bayes` | 需要一个覆盖所有分布选择的事件。 | Q_S及KL(Q_S‖P₀) | “先验”不是必须有Bayes生成模型。 | 已清楚；无。 |
| B09-179 数据独立参考先验P₀ | 1313、1318–1319，“观察S前固定”；`sec:information-pac-bayes` | 让先验平均的集中步骤合法。 | Tonelli先对同一P₀平均 | 不允许随当前S任意改参考。 | 已清楚；无。 |
| B09-180 预固定温度λ与失败率δ | 1319，“预先固定”；`sec:information-pac-bayes` | 控制同一事件中复杂度权衡。 | KL/λ+λ/(8n) | 后见数据调λ尚未在此获保证。 | 条件清楚；后文继续核对。 |
| B09-181 PAC–Bayes基础界 | 1316–1329，“同时对所有Q≪P₀”；`sec:information-pac-bayes` | 风险上界可用于样本后候选选择。 | `eq:information-pac-bayes-basic` | 候选分布期望风险，不是单点参数无条件界。 | 已清楚；无。 |
| B09-182 先验指数积分 | 1331–1339，“Tonelli…平均”；`sec:information-pac-bayes` | 将逐候选集中化为一个随机非负量。 | 双重期望≤e^(λ²/8n) | 损失有界与样本独立明确。 | 已清楚；无。 |
| B09-183 共同高概率事件E | 1340–1346，“事件只包含先验积分”；`sec:information-pac-bayes` | 避免对数据依赖Q再做未经允许的代入。 | Markov阈值e^(λ²/8n)/δ | 第8章Markov已回顾；事件不随Q变。 | 已清楚；无。 |
| B09-184 逐实现应用DV | 1347–1356，“实现后的函数…有界”；`sec:information-pac-bayes` | 在同一事件内同时控制所有候选。 | f(θ)=λ(R−R̂)、KL不等式 | 随机性已冻结，故无需预固定Q。 | 已清楚；无。 |
| B09-185 同时量词容许后选择 | 1357–1358，“Q_S也被同时覆盖”；`sec:information-pac-bayes` | 回应开篇数据依赖选择障碍。 | 共同事件加确定DV | 与固定Q的单独高概率界不同。 | 已清楚；无。 |

## PAC–Bayes的选择边界

节标签：`sec:information-pac-bayes`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-186 有限先验的点候选 | 1361–1363，“KL为log M”；`sec:information-pac-bayes` | 从分布风险界恢复有限预测器同时控制。 | 均匀先验及δ候选 | 与前有限输出MI界形式相近，概率保证不同。 | 已清楚；无。 |
| B09-187 连续先验与点候选支持 | 1364–1365，“通常不…绝对连续”；`sec:information-pac-bayes` | 限制任意点估计代入。 | 连续P₀、单点Q | 不能把密度值非零当单点质量非零。 | 已清楚；无。 |
| B09-188 参数网格及失败率分配 | 1367–1369，“预设可数…并集界”；`sec:information-pac-bayes` | 允许事后选λ而保同时事件。 | 可数网格方案 | 第8章联合界已回顾；原定理不能直接逐Q优化λ。 | 已清楚；无。 |
| B09-189 独立数据选先验 | 1370，“再对剩余…条件化”；`sec:information-pac-bayes` | 允许先验利用不属于当前评价的数据。 | 数据分割的短方案 | 不是同一S任意重选P₀。 | 已清楚；无。 |
| B09-190 MI与PAC–Bayes保证区别 | 1371–1372，“不是同一个保证”；`sec:information-pac-bayes` | 防止共用换测度就混淆对象。 | 联合／乘积对比候选／先验 | 平均偏差与同时风险明确比较。 | 已清楚；无。 |

## 收益权衡与最大熵

节标签：`sec:information-gibbs-optimization`、`sec:information-maximum-entropy`，上层`sec:information-target-distribution`、`sec:information-variational-learning`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-191 Gibbs变分式 | 1393–1409，“收益…扣除…KL”；`sec:information-gibbs-optimization` | 从参考规律选择新分布而非仅比较。 | `eq:information-gibbs-variational` | f有界，Q≪P₀；∞KL目标为−∞。 | 已清楚；无。 |
| B09-192 唯一最优倾斜分布 | 1404–1426，“Q*…e^f/Z”；`sec:information-gibbs-optimization` | 给分布优化可求解形式及最优性证明。 | 目标=log Z−KL(Q‖Q*) | 有界log比保最优候选可代入，Gibbs唯一零。 | 已清楚；无。 |
| B09-193 两条变分式的优化对象 | 1428–1429，“交换了固定对象”；`sec:information-gibbs-optimization` | 区分DV与Gibbs。 | 分布优化对比测试函数优化 | 代数同源不等于同一个优化任务。 | 已清楚；无。 |
| B09-194 无界收益的有限目标域 | 1430–1439，“只有…有限并不够”；`sec:information-gibbs-optimization` | 防止归一化成功就误算∞−∞。 | e^(−k)/k²参考、倾斜k^(−2)反例 | Z有限不等于倾斜收益和KL有限。 | 已清楚；无。 |
| B09-195 截断支持逼近上确界 | 1440–1447，“不必有…最优分布”；`sec:information-gibbs-optimization` | 无界问题仍可通过有限目标逼近。 | Q_n∝e^f I{\|f\|≤n}，目标log Z_n | 与DV截断测试函数不同，此处截断支持。 | 已清楚；无。 |
| B09-196 温度β | 1449–1454，“f=r/β”；`sec:information-gibbs-optimization` | 控制收益与参考偏离的权衡。 | βlog E e^(r/β)、Q*∝P₀e^(r/β) | 不是编码底数或概率温度的任意装饰。 | 已清楚；无。 |
| B09-197 倾斜权重集中 | 1455，“采样方差增大”；`sec:information-gibbs-optimization` | 连接低温目标与实际重要性采样成本。 | 小β强化高收益权重 | 第8章重要性权重及方差已回顾；非无条件定量断言。 | 已清楚；无。 |
| B09-198 KL正则不等于安全约束 | 1456–1457，“仍需…风险迁移条件”；`sec:information-gibbs-optimization` | 限制优化罚项的解释。 | 回接本章事件界 | 优化偏好不是自动失败概率保证。 | 已清楚；无。 |
| B09-199 最大熵原理 | 1462–1465，“相容分布…熵最大”；`sec:information-maximum-entropy` | 只有部分矩信息时选择规律。 | 后Gaussian与三点例 | 是建模准则，不是观测已证明真实。 | 已清楚；无。 |
| B09-200 统计量矩约束 | 1467–1471，“∫T p=τ”；`sec:information-maximum-entropy` | 明确可行密度集合。 | 归一化和向量期望等式 | 第8章矩／统计量回顾，参考μ固定。 | 已清楚；无。 |
| B09-201 指数最大熵候选 | 1472–1478，“若存在有限参数”；`sec:information-maximum-entropy` | 给满足矩约束的候选形式。 | p_λ=exp(λᵀT−A) | 配分有限、归一化、矩可达需分别核验。 | 已清楚；无。 |
| B09-202 密度Lagrange一阶条件 | 1479–1482，“形式上”；`sec:information-maximum-entropy` | 提供指数形式的发现路线。 | −log p−1+λᵀT+a=0 | 明确不据此证明无限维合法性或存在性。 | 证明边界清楚；无。 |
| B09-203 最大熵的KL证书 | 1484–1494，“h(p_λ)−h(p)≥0”；`sec:information-maximum-entropy` | 在给定候选后直接核验全局最优。 | 有限可积条件下完整展开 | 与形式驻点不同；边界可能无有限参数。 | 已清楚；无。 |
| B09-204 定均值协方差的Gaussian最大熵 | 1496–1514，“trace…=d”；`sec:information-maximum-entropy` | 给可算连续实例。 | h≤½log((2πe)^d detΣ) | 需正定Σ和有限微分熵；固定Lebesgue参考。 | 已清楚；无。 |
| B09-205 奇异协方差的子空间参考 | 1515–1516，“改用子空间参考测度”；`sec:information-maximum-entropy` | 防止把低维规律当环境全维密度。 | 与前退化Gaussian支持一致 | 第8章支持和第6章值域已回顾。 | 已清楚；无。 |
| B09-206 指数族与自然参数 | 1518–1527，“前章的指数族”；`sec:information-maximum-entropy` | 将最大熵形式接到既有参数模型。 | p_η=h exp(ηᵀT−A) | 第8章493–552重核；不是所有分布都属于该族。 | 已回顾；无。 |
| B09-207 配分函数的一二阶导数 | 1524–1526，“E T…Cov(T)”；`sec:information-maximum-entropy` | 把参数变化与矩变化联系。 | ∇A=τ、∇²A=Cov | 前章已给积分求导条件和证明入口。 | 已回顾；无。 |
| B09-208 均值参数τ | 1525–1527，“指定统计量平均”；`sec:information-maximum-entropy` | 提供与自然权重不同的坐标。 | τ=∇A(η) | 不是观测x的普通均值，取决于T。 | 已清楚；无。 |
| B09-209 配分凸共轭A* | 1528–1538，“sup…ηᵀτ−A”；`sec:information-maximum-entropy` | 在均值约束侧重写目标。 | `eq:information-log-partition-conjugate`及一阶凸性证明 | 第4章1640–1730完整补读，有限参数可达才当处取等。 | 已清楚；无。 |
| B09-210 基准项下的负熵 | 1539–1542，“只有h=1…普通负熵”；`sec:information-maximum-entropy` | 区分一般指数族基准与计数／Lebesgue常量基准。 | ∫p log(p/h) | h为概率密度才是KL。 | 已清楚；无。 |
| B09-211 最小表示 | 1543–1545，“在最小正则表示中”；`sec:information-maximum-entropy` | 用来保证协方差正定，却未定义判据。 | 只有“线性冗余”提示 | 第8章仅警示某方向线性冗余，未讲含常量的仿射冗余。 | 局部费力；R1-B-040补无非零a使aᵀT为常量。 |
| B09-212 正则指数族表示 | 1543，“正则表示”；`sec:information-maximum-entropy` | 标注参数内部求导及局部坐标范围。 | 无独立定义或例 | “正则”在前文多处含义不同，不能自动等同自然参数开域。 | 局部费力；R1-B-040明确这里的参数域条件，或直接写所需条件。 |
| B09-213 自然／均值局部可逆 | 1543–1545，“Jacobian可能奇异”；`sec:information-maximum-entropy` | 说明什么时候两组参数能互换。 | dτ=∇²A dη | Jacobian可逆的前置依赖第3章及第7章已有，满秩需B-040。 | 随B-040补接；无需另项。 |
| B09-214 有限配置集D | 1547–1554，“有限非空”；`sec:information-maximum-entropy` | 不靠有限自然参数覆盖闭域。 | A(θ)=logΣ_D e^(θᵀT) | 基准恒1明确，不混一般h。 | 已清楚；无。 |
| B09-215 可实现均值凸包M | 1554–1560，“conv{T(z)}”；`sec:information-maximum-entropy` | 描述所有可行矩，而非仅参数像内部。 | E_qT遍历凸组合 | 第4章凸包已补读，有限点凸包紧。 | 已清楚；无。 |
| B09-216 条件最大熵值H* | 1556–1570，“max…E_qT=μ”；`sec:information-maximum-entropy` | 组内只保留最分散的概率表。 | 闭非空单纯形切片紧、熵连续 | 与A*星号的对象不同，定义明确。 | 已清楚；无。 |
| B09-217 有限熵／配分对偶 | 1561–1579，“整个M…外部+∞”；`sec:information-maximum-entropy` | 连边界也保证最优值等价。 | `eq:information-finite-gibbs-duality`、KL按均值分组 | 值相等不保证有限乘子达到。 | 已清楚；无。 |
| B09-218 熵凹性 | 1583–1591，“混合…熵凹性”；`sec:information-maximum-entropy` | 证明最大熵值凹，负值凸。 | 两个最大熵分布的混合 | 可由−t log t二阶导数及连续端点回顾得到。 | 可读；可选写一句二阶判据来源，不计实质问题。 |
| B09-219 可行域外的扩展目标 | 1581–1582、1600–1601，“f=+∞…适当”；`sec:information-maximum-entropy` | 把受约束最大熵纳入全空间共轭。 | f=−H*于M、外部∞ | 第4章适当扩展函数已有；非普通实函数。 | 已清楚；无。 |
| B09-220 最大熵值的上半连续 | 1592–1599，“先取…上极限…子列”；`sec:information-maximum-entropy` | 确保边界不丢失共轭闭性。 | 概率表紧子列及H(q)≤H*(μ) | 与每个固定q的连续性不同，正文有实际证明。 | 已清楚；无。 |
| B09-221 Fenchel–Moreau回用 | 1601–1605，“A*=f**=f”；`sec:information-maximum-entropy` | 完成边界及域外等式。 | 适当、凸、下半连续逐项已证 | 第4章定理及证明已实际核对。 | 已清楚；无。 |
| B09-222 边缘多面体 | 1607–1612，“同一全局分布”；`sec:information-maximum-entropy` | 描述多个局部概率表的共同可实现性。 | 边缘0.1却交集0.9反例 | 各表独自归一化不够。 | 已清楚；无。 |
| B09-223 三点最大熵算例 | 1614–1623，“3t²+t−1=0”；`sec:information-maximum-entropy` | 同时演示矩匹配、自然参数及熵对偶。 | 0.6162／0.2676／0.1162 | 以t=e^λ表达，不凭算法名称。 | 已清楚；无。 |
| B09-224 边界均值与无穷参数 | 1624–1626，“λ→−∞”；`sec:information-maximum-entropy` | 区分分布最优存在和有限坐标实现。 | E X=0只有δ₀ | 对应前双共轭证明为何需要闭域。 | 已清楚；无。 |

## 后验与目标逼近

节标签：`sec:information-elbo-approximation`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-225 固定后验目标π | 1631–1637，“不再自由选择规律”；`sec:information-elbo-approximation` | 区分选分布与近似已有模型后验。 | π=p_θ(z\|x) | 第8章Bayes后验已回顾，θ和x先固定。 | 已清楚；无。 |
| B09-226 证据p_θ(x) | 1634、1638，“证据积分可能难算”；`sec:information-elbo-approximation` | 说明近似推断的计算动机。 | 0<∫p(x,z)dz<∞ | 是密度值而非必须≤1的概率；第8章已回顾。 | 已清楚；无。 |
| B09-227 ELBO | 1640–1650，“证据下界”；`sec:information-elbo-approximation` | 用可采样q评价模型证据的下界。 | E_q log[p(x,Z)/q(Z)] | 定义先要求q≪π、KL有限。 | 已清楚；无。 |
| B09-228 整体对数比可积口径 | 1648–1653，“不要求…各自有限”；`sec:information-elbo-approximation` | 避免将有效比值期望拆成∞−∞。 | log p(x)−log(q/π) | 比q熵有限的条件更宽。 | 已清楚；无。 |
| B09-229 证据／ELBO／KL分解 | 1654–1660，“等号当且仅当q=π”；`sec:information-elbo-approximation` | 给下界精确误差量。 | `eq:information-elbo-decomposition` | 不以Jensen覆盖条件定义ELBO。 | 已清楚；无。 |
| B09-230 无限KL的扩展ELBO | 1661–1663，“使用…减KL这一方向”；`sec:information-elbo-approximation` | 明确支持失败时的合法赋值。 | ELBO=log证据−KL | 不把−∞+∞作为等式。 | 已清楚；无。 |
| B09-231 重要性证据覆盖条件 | 1665–1677，“相反方向…π≪q”；`sec:information-elbo-approximation` | 说明乘除q的证据等号为何有额外前提。 | `eq:information-elbo-jensen` | q≪π保证反向KL，不等于π≪q完整覆盖。 | 已清楚；Jensen前置仍沿B-013。 |
| B09-232 两种支持方向反例 | 1678–1681，“只恢复一半证据”；`sec:information-elbo-approximation` | 用两点让支持差别可复算。 | π=(1/2,1/2)、q=(1,0)及反例 | 有限ELBO不保证重要性等号，反向也不保证。 | 已清楚；无。 |
| B09-233 候选族表示误差 | 1683–1693，“第一项是表示限制”；`sec:information-elbo-approximation` | 将后验近似误差归因。 | inf_Q KL | 分布最优可不存在，仍可用有限下确界。 | 已清楚；无。 |
| B09-234 族内求解误差 | 1689–1693，“未达到族内最优”；`sec:information-elbo-approximation` | 分开表示上限与算法没收敛。 | 当前KL−inf KL | 默认沿定义域有限KL候选，故不是∞−∞。 | 已清楚；无。 |
| B09-235 同时拟合模型的第三层误差 | 1694–1695，“证据和后验…改变”；`sec:information-elbo-approximation` | 避免近似目标准确就当模型真实。 | 模型θ随数据拟合 | 模型拟合不等于上述两项之和。 | 已清楚；无。 |
| B09-236 Gaussian后验ELBO算例 | 1697–1707，“三者满足精确分解”；`sec:information-elbo-approximation` | 核对有限连续比值。 | log证据−1.5155、KL0.4034、ELBO−1.9189 | 第8章高斯配方可用。 | 已清楚；无。 |
| B09-237 分块独立近似族 | 1708–1709，“无法表示的后验相关性”；`sec:information-elbo-approximation` | 说明表示误差不会由多迭代消失。 | 无数值独立块例，已有相关高斯背景 | 类限制是人为假设，不是真后验自动独立。 | 已清楚；无。 |
| B09-238 分布蒸馏 | 1711–1716，“教师的条件分布”；`sec:information-elbo-approximation` | 将既定目标从后验换成教师。 | KL(P_T‖Q_φ) | 学生接近教师不等于接近真实标签。 | 已清楚；无。 |
| B09-239 教师软标签交叉熵 | 1713–1714，“教师软标签”；`sec:information-elbo-approximation` | 说明用分布而非单一类别训练。 | 前向KL与交叉熵等价 | 第8章软概率标签已读；固定输入权重。 | 已清楚；无。 |
| B09-240 反向蒸馏KL | 1715，“改由学生平均”；`sec:information-elbo-approximation` | 再次强调目标方向改变。 | 支持与最优近似皆变 | 不能交换加权方并保同一目标。 | 已清楚；无。 |
| B09-241 对比任务的正配对 | 1718–1719，“目标联合分布产生”；`sec:information-elbo-approximation` | 通过分类识别联合依赖。 | 仅文字，未写采样元组 | 前文MI定义可用，但具体构造未完整。 | 局部费力；R1-B-039若保留定量界须定义采样。 |
| B09-242 对比任务的边缘负样本 | 1718–1720，“按指定边缘独立采样”；`sec:information-elbo-approximation` | 构造独立参照。 | 未明与X、正样本及其他负样本的独立关系 | 名称不是自动样本制度。 | 局部费力；并入B-039补条件采样式。 |
| B09-243 标准对比损失L_contrast | 1721–1722，“标准对比损失”；`sec:information-elbo-approximation` | 承担定量MI解释，却未定义分数、softmax或期望。 | 只有log K−L的式子 | 前1–8章未见该损失定义，不能据“标准”补专家知识。 | 局部费力；B-039补InfoNCE式，或删定量断言改纯预告。 |
| B09-244 对比MI下界及饱和 | 1720–1725，“至多为log K”；`sec:information-elbo-approximation` | 限制有限负样本可见信息量。 | 上限来自损失非负，但损失本身未给 | 合法下界需采样前提与定理入口。 | 局部费力；随B-039补或撤回到预告。 |
| B09-245 对比目标与任务保证 | 1724–1725，“不自动保证校准…”；`sec:information-elbo-approximation` | 防止信息代理被当语义或风险保证。 | 条件性边界说明 | 校准和风险第8章已建立；语义质量仅应用提示。 | 边界清楚；核心目标仍须B-039。 |

## 最优耦合与有限求解

节标签：`sec:information-optimal-coupling-existence`、`sec:information-finite-transport`，上层`sec:information-coupling-optimization`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-246 最优耦合存在定理 | 1739–1753，“防止质量逃逸”；`sec:information-optimal-coupling-existence` | 将此前下确界升级为达到的最小值。 | `thm:information-optimal-coupling-existence` | Polish、非负下半连续、一个有限成本可行者。 | 已清楚；无。 |
| B09-247 两种弱收敛语言 | 1741–1744，“不能…互换结论”；`sec:information-optimal-coupling-existence` | 指明变化的是概率测度而非线性空间向量。 | 有界连续函数对比连续线性泛函 | 第8章弱收敛已读；第5章概念不冒充此工具。 | 比较清楚；无。 |
| B09-248 耦合族的一致紧性 | 1759–1770，“紧集对全部…适用”；`sec:information-optimal-coupling-existence` | 用固定边缘阻止质量逃逸。 | 两边紧集乘积、补集概率联合界 | 第8章Polish概率紧已建立；不是每项各自紧就够。 | 已清楚；无。 |
| B09-249 Prokhorov子列 | 1771–1772，“给出子列”；`sec:information-optimal-coupling-existence` | 从近最优方案取得概率极限。 | 精确回指`thm:rv-prokhorov` | 第8章该定理实际完整读过。 | 已回顾；无。 |
| B09-250 固定边缘弱闭性 | 1774–1781，“极限仍可行”；`sec:information-optimal-coupling-existence` | 防止取极限破坏约束。 | 测试函数a(x)的显式积分极限 | 边缘推送不需联合密度。 | 已清楚；无。 |
| B09-251 成本积分下半连续 | 1783–1794，“不能用固定测度下Fatou”；`sec:information-optimal-coupling-existence` | 使极限成本不比近最优更大。 | `thm:rv-portmanteau`及liminf | 第8章工具已读；积分测度随n变。 | 已清楚；无。 |
| B09-252 确定搬运映射的障碍 | 1795–1797，“必须…分成两半”；`sec:information-optimal-coupling-existence` | 分开联合耦合存在与单值映射存在。 | δ₀到±1均分 | 未强加Monge名称；点图像不能拆质量。 | 已清楚；无。 |
| B09-253 有限搬运表 | 1802–1809，“行和…列和”；`sec:information-finite-transport` | 把耦合变成可计算非负矩阵。 | Σc_ijγ_ij及边缘等式 | 与概率转移矩阵行和1不同。 | 已清楚；无。 |
| B09-254 紧多面体可行域 | 1810–1811，“闭…[0,1]内”；`sec:information-finite-transport` | 直接保证有限表最优值达到。 | 有限维闭有界及线性目标连续 | 不需一般概率紧性定理。 | 已清楚；无。 |
| B09-255 对偶势u_i、v_j | 1813–1814，“两组边缘约束”；`sec:information-finite-transport` | 用价格变量给成本下界。 | 每行、每列一个乘子 | 只是等式乘子，不是预猜物理势。 | 已清楚；无。 |
| B09-256 OT Lagrangian | 1815–1823，“c_ij−u_i−v_j”；`sec:information-finite-transport` | 显式消掉搬运变量。 | `eq:information-discrete-ot-lagrangian` | 第4章对偶已实际核对，保留非负定义域。 | 已清楚；无。 |
| B09-257 对偶函数有限性的条件 | 1824–1837，“零表虽不是…可行表”；`sec:information-finite-transport` | 解释为何得u_i+v_j≤c_ij。 | 负系数趋∞给−∞，非负系数零表取等 | 原始边缘约束已移入Lagrangian，域不能混淆。 | 已清楚；无。 |
| B09-258 有限OT对偶问题 | 1838–1844，“最大化它”；`sec:information-finite-transport` | 寻找最紧搬运下界。 | `eq:information-discrete-ot-dual` | 约束来自下确界，不是额外搬运规则。 | 已清楚；无。 |
| B09-259 OT弱对偶证书 | 1845–1846，“逐项乘γ…求和”；`sec:information-finite-transport` | 任何可行势即给可核验成本下界。 | 显式一行证明及两点例 | 只需可行，不依赖已知最优解。 | 已清楚；无。 |
| B09-260 有限LP强对偶回用 | 1847，“可行且最优值有限”；`sec:information-finite-transport` | 保证最紧下界就是最优搬运成本。 | 第4章`thm:opt-lp-strong-duality`已读全文证明 | 不从“凸”直接跳强对偶。 | 已清楚；无。 |
| B09-261 两点搬运原始／对偶取等 | 1849–1872，“总成本2−4a”；`sec:information-finite-transport` | 给可以手算的最优性证书。 | γ(a)、最优a=1/4、势值=1 | 弱对偶已足够验本例。 | 已清楚；无。 |
| B09-262 同边缘不同成本图 | 1873–1883，“独立…5/4，最优…1”；`sec:information-finite-transport` | 可视解释为什么要优化联合配对。 | `fig:information-transport-tables`及行列颜色说明 | 边缘相同不指定相关性或成本。 | 图注支持；无。 |

## Fisher局部几何

节标签：`sec:information-local-kl`、`sec:information-fisher-reparameterization`，上层`sec:information-local-metric`、`sec:information-global-local-geometry`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-263 参数族中的分布优化 | 1889–1895，“减少表示和计算负担”；`sec:information-global-local-geometry` | 将此前分布任务限制到可求解表示。 | 等参数步不等可辨识度的高斯动机 | 矩／边缘可行性仍需额外约束。 | 已清楚；无。 |
| B09-264 局部KL的度量目标 | 1894、1900–1903，“真实扰动…坐标变化”；`sec:information-global-local-geometry` | 从模型建立客观局部长度。 | 后二阶KL式 | 第7章切向量、度量已完整读；不是目标L的Hessian。 | 已清楚；无。 |
| B09-265 共同正支持S | 1908–1910，“在S上…>0”；`sec:information-local-kl` | 让对数微分和密度比在同域可算。 | 移动均匀支持反例 | 固定μ不自动保证固定支持。 | 已清楚；无。 |
| B09-266 密度导数的积分控制 | 1911–1913，“μ可积…一致控制”；`sec:information-local-kl` | 允许两次微分归一化等式。 | 一二阶导数支配条件 | 第3章积分求导已有实读，不能只说可微。 | 已清楚；无。 |
| B09-267 得分及零均值 | 1914–1919，“∫∇p=0”；`sec:information-local-kl` | 把局部响应表示为随机向量。 | `eq:information-score-zero` | 第8章得分正式定义已读，本处补更强几何条件。 | 已回顾且推导清楚；无。 |
| B09-268 Fisher矩阵有限性 | 1921–1929，“二阶可积”；`sec:information-local-kl` | 外积期望作为局部二次量。 | F=E ssᵀ | 单个样本外积不是F，本节后面专门比较。 | 已清楚；无。 |
| B09-269 信息恒等式 | 1929–1943，“积分权重…也依赖参数”；`sec:information-local-kl` | 连接得分方差与期望对数Hessian。 | `eq:information-fisher-hessian-identity`、乘积求导 | 不是忽略密度导数地对E s=0求导。 | 已清楚；无。 |
| B09-270 移动支持均匀族反例 | 1944–1946，“均值不为零”；`sec:information-local-kl` | 说明共同支持条件真有作用。 | Unif(0,θ)内部得分−1/θ | 边界质量变化不能省掉。 | 已清楚；无。 |
| B09-271 KL局部二阶展开 | 1948–1965，“½δᵀFδ+o(‖δ‖²)”；`sec:information-local-kl` | 将Fisher解释为小分布差异。 | `thm:information-kl-local-fisher` | 固定前向P_θ，余项需对数Hessian支配。 | 已清楚；无。 |
| B09-272 积分Taylor与支配余项 | 1967–1996，“矩阵o(1)…成为o(‖δ‖²)”；`sec:information-local-kl` | 防止逐点Taylor直接搬进期望。 | 全部展开及乘积测度支配收敛 | 第3章1859–1919已补读；有限维矩阵范数可用。 | 证明完整；无。 |
| B09-273 得分满秩 | 1998–2002，“每个v≠0…>0”；`sec:information-local-kl` | 判断半正定F何时可作度量。 | E(vᵀs)²>0 | 不是单次得分矩阵或参数个数的秩。 | 已清楚；无。 |
| B09-274 局部可识别与微分可辨 | 2003–2010，“一一对应，但…F=0”；`sec:information-local-kl` | 限制从参数不重复推可逆F。 | N(θ³,σ²)、KL始于δ⁶ | 第8章可识别已回顾；两个条件不等同。 | 已清楚；无。 |
| B09-275 Fisher度量 | 2012–2019，“uᵀFv”；`sec:information-local-kl` | 给参数切向量一个模型决定的内积。 | `def:information-fisher-metric` | 需正定正则点，不能给所有参数无条件定义。 | 已清楚；无。 |
| B09-276 Gaussian局部长度 | 2020–2021，“\|dμ\|/σ”；`sec:information-local-kl` | 与开篇噪声尺度闭合。 | F=1/σ² | 长度与KL近似中的长度平方差1/2。 | 已清楚；无。 |
| B09-277 Bernoulli Fisher | 2022–2026，“1/[p(1−p)]”；`sec:information-local-kl` | 提供非恒定局部曲率实例。 | 两种得分逐项加权 | 0<p<1，不覆盖边界。 | 已清楚；无。 |
| B09-278 局部二次式与远处KL | 2027–2041，“不能…当成全域散度”；`sec:information-local-kl` | 显示Taylor使用尺度。 | q=0.22数值与q↓0反例；`fig:information-fisher-local` | 固定p二次式可能有限而真KL∞。 | 图注支持；无。 |
| B09-279 可逆重参数化 | 2046–2049，“同一张分布”；`sec:information-fisher-reparameterization` | 将坐标替换与真实模型变化分开。 | θ(φ)、J | 第7章坐标图及过渡已读；J须可逆。 | 已清楚；无。 |
| B09-280 得分协变坐标 | 2051，“s_φ=Jᵀs_θ”；`sec:information-fisher-reparameterization` | 用链式法则改变对参数的读数。 | 显式式子 | 第7章余切／微分回用，B-004缺口已有当地解释。 | 已清楚；无。 |
| B09-281 Fisher矩阵换坐标 | 2052、2064，“JᵀFJ”；`sec:information-fisher-reparameterization` | 证明几何量不等于矩阵数值。 | 得分外积的变换 | 第7章度量换基可回顾。 | 已清楚；无。 |
| B09-282 切向量与二次长度不变 | 2054–2058，“dθ=J dφ”；`sec:information-fisher-reparameterization` | 正确配对向量坐标与度量坐标。 | 二次型等式 | 不是要求F两个坐标相等。 | 已清楚；无。 |
| B09-283 目标微分不变 | 2059–2063，“g_φ=Jᵀg_θ”；`sec:information-fisher-reparameterization` | 为自然梯度的内积代表准备。 | gᵀdθ不变 | 普通梯度坐标按链式法则，不等于切向推送。 | 已清楚；无。 |
| B09-284 logit坐标下Fisher | 2066–2073，“一个…变大，另一个变小”；`sec:information-fisher-reparameterization` | 用同一Bernoulli显示矩阵数值可反向变化。 | φ=log[p/(1−p)]、F_φ=p(1−p) | 第8章自然参数logit已回顾；二次长度仍相同。 | 已清楚；无。 |
| B09-285 退化坐标边界 | 2074，“Jacobian为零”；`sec:information-fisher-reparameterization` | 限制重参数化不变结论。 | 立方高斯零点 | 一一函数不一定是当地微分同胚。 | 已清楚；无。 |
| B09-286 固定状态的条件Fisher | 2076–2082，“单步Fisher”；`sec:information-fisher-reparameterization` | 序贯任务先指定概率对象。 | E_{A\|s} ssᵀ | π(a\|s)是条件行动核；不先假定状态分布。 | 已清楚；无。 |
| B09-287 固定访问权重平均Fisher | 2083–2085，“指定并保持固定”；`sec:information-fisher-reparameterization` | 汇总条件策略变化。 | F_d=E_d F_S | 权重固定，不对d求导。 | 已清楚；无。 |
| B09-288 联合状态行动Fisher | 2086–2094，“还包含∇log d_θ”；`sec:information-fisher-reparameterization` | 解释完整模型的额外信息。 | F_joint=F_state+E F_S | 条件得分零均值消交叉项；与固定权重不同。 | 已清楚；无。 |
| B09-289 完整轨迹得分 | 2096–2100，“Σs_t”；`sec:information-fisher-reparameterization` | 汇总随历史选择的参数响应。 | 初始／环境不含θ、固定有限T | 不是每步独立假设。 | 已清楚；无。 |
| B09-290 得分跨时正交 | 2101–2105，“对H_t可测”；`sec:information-fisher-reparameterization` | 使轨迹外积只留下对角步项。 | 塔式期望消E[s_u s_tᵀ] | 第8章鞅差与条件期望已回顾。 | 已清楚；无。 |
| B09-291 轨迹Fisher累积 | 2106–2114，“Σ E F_Ht”；`sec:information-fisher-reparameterization` | 对齐真实历史下的全部信息预算。 | 各时刻平均访问时为T倍平均矩阵 | 环境或初始含θ须另加得分。 | 已清楚；无。 |
| B09-292 观测负Hessian | 2116–2135，“xxᵀ/σ²”；`sec:information-fisher-reparameterization` | 区分每样本曲率与模型Fisher。 | 条件线性Gaussian三量并列 | 第8章观测信息已有；本例与y残差无关。 | 已清楚；无。 |
| B09-293 经验得分外积 | 2127–2137，“残差为零…外积…零”；`sec:information-fisher-reparameterization` | 给经验Fisher与Hessian不等的直接反例。 | 残差²xxᵀ/σ⁴ | 模型期望相等，不是每样本相等。 | 已清楚；无。 |
| B09-294 模型错设下的信息差别 | 2136–2138，“总体极限…不一定等于”；`sec:information-fisher-reparameterization` | 防止数据平均自动当模型期望。 | 真实残差方差可不同 | 与抽样误差、输入权重变化分别处理。 | 已清楚；无。 |

## 几何更新及边界

节标签：`sec:information-natural-gradient-update`、`sec:information-singular-approximate-update`，上层`sec:information-geometric-update`；末项为`sec:information-theory-statistical-geometry-summary`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B09-295 可行切空间与回缩 | 2143–2145，“不会自动保持…边缘”；`sec:information-geometric-update` | 将局部方向接回原分布约束。 | 指向约束优化／回缩的边界 | 第7章回缩及切空间完整已读；不是F逆自动处理可行性。 | 已回顾；无。 |
| B09-296 自然梯度 | 2150–2163，“Fisher内积…代表向量”；`sec:information-natural-gradient-update` | 在模型长度下表示同一目标微分。 | `def:information-natural-gradient`、F⁻¹∇L | 与普通梯度代表同一微分但用不同内积；F不是任意L的Hessian。 | 已清楚；可选再明确与Newton一步之别。 |
| B09-297 局部KL信赖域 | 2165–2171，“一阶线性化…二阶近似”；`sec:information-natural-gradient-update` | 根据分布变化预算选下降方向。 | `eq:information-natural-gradient-trust-region` | 原目标与KL都已近似，不是全局约束。 | 已清楚；无。 |
| B09-298 归一化自然下降步 | 2172–2185，“最小值在椭球边界”；`sec:information-natural-gradient-update` | 确定方向与预算对应的步长。 | Lagrange驻点及`eq:information-natural-gradient-step` | ε>0、g≠0、F正定明确。 | 已清楚；无。 |
| B09-299 平方根白化的全局子问题证书 | 2187–2197，“不依赖驻点必要条件”；`sec:information-natural-gradient-update` | 核验求出的确为椭球上线性最优。 | u=F^(1/2)δ及Cauchy取等 | 第6章正定平方根已在ch08补读；此处变换已明确。 | 已清楚；无。 |
| B09-300 零目标梯度边界 | 2197–2198，“不再选出唯一方向”；`sec:information-natural-gradient-update` | 避免归一化式分母为零。 | 一阶目标处处零 | 需高阶信息或停止，不能默认唯一零步。 | 已清楚；无。 |
| B09-301 自然方向的重参数不变 | 2200–2213，“同一个分布切向方向”；`sec:information-natural-gradient-update` | 实现局部更新不随坐标单位任意改变。 | J F_φ⁻¹g_φ=F_θ⁻¹g_θ及Bernoulli例 | 连归一化因子也核验，不只矩阵形式。 | 已清楚；无。 |
| B09-302 有限加法步不保持终点 | 2215–2219，“一般不同”；`sec:information-natural-gradient-update` | 限制无穷小不变性外推。 | 非线性坐标Taylor的二阶项 | 同方向不等于任意步长同分布终点。 | 已清楚；无。 |
| B09-303 二次预算不保证真实KL阈值 | 2220–2222，“还有o(‖δ‖²)”；`sec:information-natural-gradient-update` | 提醒实际求解需步长及真值检查。 | 局部展开余项 | 正则二阶式不等于全局上界。 | 已清楚；无。 |
| B09-304 Fisher零空间 | 2227–2230，“一阶得分为零”；`sec:information-singular-approximate-update` | 说明奇异性来源不只参数冗余。 | 立方高斯再次对照 | 高阶仍可变分布，零二次预算不等于有限移动无成本。 | 已清楚；无。 |
| B09-305 伪逆自然方程解 | 2232–2238，“g∈range(F)”；`sec:information-singular-approximate-update` | 在兼容时求Fv=g。 | 全部解F†g+ker F | 第6章966–1065已实际核对；最小欧氏范数依当前坐标。 | 已清楚；无。 |
| B09-306 可辨切向商空间 | 2239–2240，“零空间分量不影响一阶”；`sec:information-singular-approximate-update` | 分开参数代表不唯一与分布方向唯一。 | 模去ker F的解类 | 第6章商空间、第7章局部切向已读；未声称有限商流形总存在。 | 已清楚；无。 |
| B09-307 不兼容奇异信赖域无界 | 2241–2244，“不消耗二次预算”；`sec:information-singular-approximate-update` | 说明不能总用伪逆替普通逆。 | 沿核方向gᵀz≠0放大 | 对称F的值域与核正交已回顾。 | 已清楚；无。 |
| B09-308 阻尼F+λI | 2246–2247，“新增欧氏二次项”；`sec:information-singular-approximate-update` | 保可逆、改善谱条件但改变模型。 | λ‖δ‖² | 第6章条件数2489–2534已核对；不是无代价修复。 | 已清楚；无。 |
| B09-309 阻尼的坐标依赖 | 2248–2254，“JᵀJ≠I”；`sec:information-singular-approximate-update` | 区分数值稳定和原Fisher几何。 | 明确换坐标不等式 | 一般非正交变换下固定I不协变。 | 已清楚；无。 |
| B09-310 线性系统求解误差 | 2255–2256，“不显式构造逆矩阵”；`sec:information-singular-approximate-update` | 交代自然步的实际计算对象。 | 容差、谱条件与矩阵误差提示 | 第6章求解工具及条件数已核对；未给新算法。 | 已回顾；无。 |
| B09-311 分块Fisher近似 | 2258–2263，“跨块相关性…近似”；`sec:information-singular-approximate-update` | 降低计算量的结构限制。 | 无具体分块算法，作为实现边界 | 正定不保证等于原F或坐标不变。 | 范围清楚；不要求在此补算法。 |
| B09-312 对角Fisher近似 | 2258–2263，“对角近似”；`sec:information-singular-approximate-update` | 只保各参数局部尺度。 | 无独立算例，矩阵对角已属本科背景 | 比分块更少相关信息，不能据正定推真实几何。 | 范围清楚；无。 |
| B09-313 优化与统计保证分离 | 2264–2265，“各有自己的条件”；`sec:information-singular-approximate-update` | 收拢本节适用边界。 | 校准／隐私／模型正确性对比 | 第8章校准与风险已读，隐私仅边界预告。 | 已清楚；无。 |
| B09-314 观测规律到因果干预的衔接 | 2267–2300，“还需要…生成机制与识别条件”；`sec:information-theory-statistical-geometry-summary` | 小结回应信息、稳定、优化问题后说明下一缺口。 | 熵／KL、三尺度、下界、三种优化与局部几何分别收拢 | 干预是下一章纯预告，不视为已经建立。 | 小结独立且呼应开篇；无。 |

## 本章完成记录

1–2300行全部完整顺读，314项概念与三项本章新增实质问题已保存：R1-B-038一般积分不等式入口、R1-B-039对比损失未定义、R1-B-040最小正则指数族条件未解释，均为局部费力。前章已报问题的继承影响在表中明确标出，不重复编号。源SHA及行字数重核一致；无本章未读范围。第10、11章现已完成，整组统计见`reader-b.md`；本读者未读取主代理修订准备稿。
