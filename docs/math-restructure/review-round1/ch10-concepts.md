# 第10章概念审读清单（独立读者B，第一轮）

## 版本与覆盖

- 源文件：`tex/01-mathematical-preliminaries/03-random-variables-distributions-and-causality/03-causal-response-and-structure.tex`。
- 冻结 SHA-256：`37cf8ef2788029df6dfb171222dbf1f79c6e44be4341f6913d50876d9ab75ce5`，开始前及完成时已与冻结清单核对；完成时第7–11章的SHA、行数、字符数也全部相符。
- 全章1–1770行、51278源字符已连续完整顺读，读取块为1–230、231–460、461–690、691–920、921–1150、1151–1380、1381–1600、1601–1770。没有跳过证明、算例、图注、表或独立本章小结。
- 本章清单共250项；未新增实质问题。已回顾概念、不同对象及纯预告分别登记，不以专家背景默补。第7–11章整组首轮状态见`reader-b.md`。
- 表前节标签与本章源路径共同适用于各行。首次位置使用实际源行号与短引文。图只判断当前说明是否支持理解，不声称完成PDF视觉检查。

## 已核对的边界依赖

路径以`tex/01-mathematical-preliminaries/`为前缀。

| 前章文件 | 实读范围 | 用途与结论 |
| --- | --- | --- |
| `01-mathematical-language-combinatorics-analysis-optimization/03-mathematical-analysis.tex` | 本章补读770–914、1029–1062 | 导数、方向导数、全微分、Jacobian、链式法则及完整梯度算例；中值定理和导数上界。足以支持局部响应差与差商控制。910–914只读到softmax定义开头，不作为该概念完整核查。 |
| `01-mathematical-language-combinatorics-analysis-optimization/04-optimization.tex` | 本章补读1–113 | 目标、变量、可行域、不可行、下确界与达到、局部全局解；核实补救的优化接口。结论没有把写出min误当已证明存在。 |

第7–9章均由本读者完整顺读。条件核、标准Borel、Bayes更新、可积期望、分布支持、耦合、分布距离与统计识别等回用对应章正文。第3章2350–2463的Fatou和支配收敛、2470–2511的积分下求导已在第8章边界核对时实际展开，沿用其阅读记录，不是只根据标题认定可用。条件Jensen等此前问题仍未修复，不将本章回用当作自动解决。

另实际完整读取`figures/math-preparation/reading-restructure/ch10/local-path-patterns.tex`的1–42行及`d-separation-paths.tex`的1–22行，核对箭头、双边框条件节点和图中文字与正文相符。没有读取作者评价，也未构建或做PDF视觉验收。图论全局对应、后门一般定理、Markov等价充分性与覆盖边变换均在本章明确作为带条件和来源的引用结论；未偷借尚未读的第11章证明。

## 响应接口与潜在结果

节标签：`chap:causal-inference`、`sec:causal-response-representation`、`sec:causal-observation-generation`、`sec:causal-intervention-potential-outcomes`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B10-001 因果响应问题 | 4–10，“主动安排培训以后”；`chap:causal-inference` | 预测记录不能回答行动后果；先说明问题缺口。 | 培训与基础能力的两种解释 | 条件预测已学，不等于改变机制。 | 动机清楚；无。 |
| B10-002 生成结构 | 10–15，“局部关系和机制合成”；`chap:causal-inference` | 预告响应内部如何产生，区别计算与恢复结构。 | 平均响应可识别而局部方程不唯一 | 纯结构预告，后文承担定义。 | 预告清楚；无。 |
| B10-003 处理T及设定值t | 11、33，“可以设定的处理值”；`chap:causal-inference` | 将行动变量与其取值分开。 | 培训0/1 | 随机变量／常量已回顾；后定义行动空间。 | 已清楚；无。 |
| B10-004 结果Y与处理前信息X | 11–12，“结果Y与处理前信息X”；`chap:causal-inference` | 固定贯穿对象和时间先后。 | 成绩与既有能力 | 后CATE保留行动不变性，非任意预测字段。 | 已清楚；无。 |
| B10-005 背景U | 33–35，“模型没有继续解释的差异”；`sec:causal-observation-generation` | 固定同一单位跨行动比较的输入。 | 既有能力、未测环境 | 不等于所有已观测协变量，不默认分量独立。 | 已清楚；无。 |
| B10-006 模型M | 35–36，“联合分布、自然运行规则和允许的行动”；`sec:causal-observation-generation` | 明确计算需要的完整输入。 | 两套二元机制 | 非单个拟合回归函数；唯一性暂作输入要求。 | 已清楚；无。 |
| B10-007 背景概率空间 | 40，“可测空间…概率测度”；`sec:causal-observation-generation` | 使同一背景可被推前为结果分布。 | `def:causal-response-interface` | 第8章可测映射和概率测度已回顾。 | 已清楚；无。 |
| B10-008 自然映射F_M | 41–44，“唯一值的可测自然映射”；`sec:causal-observation-generation` | 描述没有主动替换时怎样生成完整变量。 | 两模型均`F(u)=(u,u)` | 与行动映射不同；状态空间是多坐标记录。 | 已清楚；无。 |
| B10-009 行动映射F_M^a | 43–44，“由…机制替换产生”；`sec:causal-observation-generation` | 记录一次允许行动后的完整状态。 | `(t,u)`与`(t,t)` | 不是任意另选一个函数；保持背景。 | 已清楚；无。 |
| B10-010 设定行动a(t) | 45，“把处理设为t”；`sec:causal-observation-generation` | 把数值输入接到模型允许的机制替换。 | 处理规则改成常量 | 区别改模型参数与在模型内行动。 | 已清楚；无。 |
| B10-011 结果坐标投影π_Y | 45，“取结果坐标”；`sec:causal-observation-generation` | 从全状态映射中读取关心的结果。 | `eq:causal-response-interface` | 坐标读取是已知函数操作。 | 已清楚；无。 |
| B10-012 响应映射R_M | 46–53，“T×U…Y”；`sec:causal-observation-generation` | 以处理、背景为输入，输出唯一结果。 | `R(t,u)=π_Y(F^a(t)(u))` | 联合可测明确，不仅逐t可测。 | 已清楚；无。 |
| B10-013 自然与行动后随机变量 | 53–54，“V=F_M(U)”；`sec:causal-observation-generation` | 将映射应用随机背景形成随机状态。 | V及V_a两式 | 第8章推前已回顾；映射不等于其分布。 | 已清楚；无。 |
| B10-014 个体响应曲线 | 57，“固定u”；`sec:causal-observation-generation` | 只变化可设定输入。 | 二元机制及后平方剂量例 | 与随机U的总体分布不同。 | 已清楚；无。 |
| B10-015 总体响应分布 | 58，“让U按P_U变化”；`sec:causal-observation-generation` | 把个体响应按目标人群聚合。 | Bernoulli背景 | 行动间用同一背景律，不是另换人群。 | 已清楚；无。 |
| B10-016 模型参数θ与行动输入 | 59–61，“修改拟合参数…改变模型”；`sec:causal-observation-generation` | 防止把预测参数敏感度当处理效应。 | 有限维模型M_θ | 与固定模型内设定t的差别直接说明。 | 已清楚；无。 |
| B10-017 观测相同而行动不同 | 63–92，“自然映射相同，行动映射不同”；`sec:causal-observation-generation` | 具体展示关联不能判定作用。 | `eq:causal-observational-equivalence-confounding`、`…-effect`及四格概率 | Bernoulli已回顾；不是样本精度不足。 | 算例完整；无。 |
| B10-018 理想干预do | 97–107，“删除…规则…常量规则替换”；`sec:causal-intervention-potential-outcomes` | 正式规定行动的机制含义。 | `def:causal-intervention` | 筛选已有T=t与替换T不同。 | 已清楚；无。 |
| B10-019 干预后分布P^do | 106–107，“推前得到的分布”；`sec:causal-intervention-potential-outcomes` | 将行动规则接到概率回答。 | 129–134推前恒等式 | do不是自然事件的条件号。 | 已清楚；无。 |
| B10-020 保留机制不等于固定状态 | 110–112，“技能和成绩都应重算”；`sec:causal-intervention-potential-outcomes` | 防止把字段替换当实际行动。 | 培训→技能→成绩 | 后继值可变而规则不变。 | 已清楚；无。 |
| B10-021 多变量行动 | 112，“哪些规则替换、哪些保留”；`sec:causal-intervention-potential-outcomes` | 扩展行动接口而不默许任意组合。 | F_M^a统一写法 | 只说明接口边界，未承诺通用求解。 | 预告清楚；无。 |
| B10-022 潜在结果Y(t) | 114–123，“同一背景概率空间”；`sec:causal-intervention-potential-outcomes` | 聚焦所选处理下的输出随机变量。 | `eq:causal-response-potential-outcome` | 不等于分别抽取两个个体，也不含全部生成规则。 | 已清楚；无。 |
| B10-023 分布记号L与推前# | 126–136，“分布推前”；`sec:causal-intervention-potential-outcomes` | 对接前章数学语言。 | `L(Y(t))=(R(t,·))#P_U` | 已回顾第8章；标明准确节入口。 | 已清楚；无。 |
| B10-024 自然选择造成的条件关联 | 140–156，“进入处理组的选择”；`sec:causal-intervention-potential-outcomes` | 比较do与普通条件概率。 | 甲各干预1/2，乙为t，观测均完全关联 | 与单纯提高预测准确率不同。 | 算式支撑充分；无。 |
| B10-025 随机干预q | 158–161，“新的随机规则替换”；`sec:causal-intervention-potential-outcomes` | 行动不必设为固定常量。 | `T=g_q(X,W)` | 条件核已回顾；W须独立于原背景。 | 已清楚；无。 |
| B10-026 确定性策略 | 162，“不再需要随机化的特例”；`sec:causal-intervention-potential-outcomes` | 将按X选固定动作纳入同一接口。 | 后`π`集中于单一动作 | 与自然分配函数相同形状但机制身份不同。 | 已清楚；无。 |
| B10-027 行动的信息限制 | 162–164，“可使用哪些信息”；`sec:causal-intervention-potential-outcomes` | 防止改概率因子却默认其余机制不变。 | 新增独立W的构造 | 分解公式准确后指，未先借用。 | 已清楚；无。 |

## 自然记录的连接

节标签：`sec:causal-response-observation-link`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B10-028 目标总体 | 169，“对谁平均”；`sec:causal-response-observation-link` | 确定效应的聚合对象。 | 培训人群 | 不同于行动规则本身。 | 已清楚；无。 |
| B10-029 处理版本 | 170–171，“不同课程与时长”；`sec:causal-response-observation-link` | 保证Y(1)确实指单一行动。 | 培训版本例 | 二元标签相同不保证行动相同。 | 已清楚；无。 |
| B10-030 结果测量时间 | 170，“观察何种结果”；`sec:causal-response-observation-link` | 固定目标输出的时间口径。 | 成绩测量 | 与分配时间及版本分开。 | 已清楚；无。 |
| B10-031 处理一致性 | 175–182，“Y=Y(T)”；`sec:causal-response-observation-link` | 将实际记录接到对应潜在结果。 | `eq:causal-consistency`及二元展开 | 与估计量一致性只是同名；上下文足以区别。 | 已清楚；无。 |
| B10-032 无干扰 | 184–187，“只要t_i=t_i'”；`sec:causal-response-observation-link` | 使个体结果可只记自己的处理。 | 197–198平均同伴处理反例 | 不由一致性推出；全处理向量不能一般删掉。 | 已清楚；无。 |
| B10-033 自然映射与响应族相容性 | 190–193，“不能任意拼接”；`sec:causal-response-observation-link` | 明确一致性也约束模型接口。 | `R(F_(M,T)(U),U)` | 无环局部模型证明留后，不以名称代替。 | 已清楚；无。 |
| B10-034 网络暴露与分组干预 | 195–199，“另行规定”；`sec:causal-response-observation-link` | 说明干扰存在时应换目标而非硬套个体效应。 | 疫苗、竞争、显式η反例 | 作为替代建模预告，未用新技术结论。 | 预告清楚；无。 |
| B10-035 稳定单位处理值假设 | 201，“版本唯一性和无干扰”；`sec:causal-response-observation-link` | 解释常见合称组成。 | 两项已分别定义 | 不保证随机分配或无混杂。 | 已清楚；无。 |
| B10-036 分配机制 | 202，“T怎样依赖X,Y(0),Y(1)”；`sec:causal-response-observation-link` | 为识别问题保留独立的条件。 | 主动参加者背景不同 | 一致性只连接结果，不规定谁接受处理。 | 已清楚；无。 |

## 个体、总体与局部比较

节标签：`sec:causal-response-comparison`、`sec:causal-individual-response`、`sec:causal-population-response`、`sec:causal-average-response`、`sec:causal-distribution-response`、`sec:causal-local-response`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B10-037 固定背景响应差Δ_M | 218–221，“固定背景”；`sec:causal-individual-response` | 指定两个处理的可比输入。 | `eq:causal-individual-response-difference` | 实值结果才能直接相减；不是两组个人相减。 | 已清楚；无。 |
| B10-038 个体处理效应 | 223–230，“Y(1)-Y(0)”；`sec:causal-individual-response` | 将同人二元差看成总体中的随机变量。 | `u+(2u-1)t`给±1 | 与给定u的确定差分开。 | 已清楚；无。 |
| B10-039 个体效应的观测缺失 | 232–235，“不会同时包含”；`sec:causal-individual-response` | 定义明确不等于一次记录可恢复。 | 当前零结果仍需背景机制 | 后跨世界联合例继续支撑。 | 已清楚；无。 |
| B10-040 结果效用h | 237–241，“规定目标”；`sec:causal-individual-response` | 给向量／类别结果选择可比较的实值尺度。 | 收入、风险、事件指示量 | 与任意坐标差或纯记号替换不同。 | 已清楚；无。 |
| B10-041 ATE | 254–271，“两种潜在结果都可积”；`sec:causal-average-response` | 报告共同人群的平均处理效果。 | `eq:causal-ate-interventional`及期望差等价式 | 线性期望已回顾；不需要知道两个结果联合。 | 已清楚；无。 |
| B10-042 零平均掩盖异质效应 | 274–275，“没有人的个体效应为零”；`sec:causal-average-response` | 防止平均无效被读作人人无效。 | ±1等概率例 | 不是估计误差造成。 | 已清楚；无。 |
| B10-043 CATE | 280–285，“X…保持同一取值与含义”；`sec:causal-average-response` | 按已知处理前信息划分共同人群。 | `eq:causal-cate`、X=U的±1 | 条件均值不等于同层每个人效应；a.e.口径明确。 | 已清楚；无。 |
| B10-044 处理后分层陷阱 | 289–291，“不是比较同一条件总体”；`sec:causal-average-response` | 解释CATE中X不随处理变的必要性。 | 按处理后的技能筛人 | 不等于普通增加预测字段。 | 已清楚；无。 |
| B10-045 CATE聚合与人群迁移 | 293–297，“条件背景规律…保持不变”；`sec:causal-average-response` | 区分机制变化与总体权重变化。 | `τ=E_Xτ(X)`及`∫τ dQ_X` | 全期望已回顾；跨总体效应保留需另假设。 | 已清楚；无。 |
| B10-046 多值处理平均差 | 299–302，“有限处理集合”；`sec:causal-average-response` | 将二元目标扩成任意一对允许值。 | `τ(t,t')` | 仍要求相应可积性，不自动等于策略价值。 | 已清楚；无。 |
| B10-047 单步策略价值V(π) | 303–311，“独立的新增随机化”；`sec:causal-average-response` | 比较随信息选动作的整体行动规则。 | `eq:causal-policy-value` | π的选择不额外透露U；有限动作保证可积。 | 已清楚；无。 |
| B10-048 策略支持条件 | 313–315，“再检查”；`sec:causal-average-response` | 将模型内目标与观测可恢复性分开。 | 准确后指识别节 | 纯预告；不要求每个连续值有正原子质量。 | 预告清楚；无。 |
| B10-049 干预CDF F_t | 320–328，“低于零代表失败”；`sec:causal-distribution-response` | 均值外还要比较阈值风险。 | Y(0)=0、Y(1)=±1及CDF式 | CDF已回顾第8章，均值不保留分布。 | 已清楚；无。 |
| B10-050 干预分位数Q_t | 324–328，“广义分位数”；`sec:causal-distribution-response` | 比较总体同一分位位置。 | `inf{y:F_t(y)≥p}` | 已回顾广义逆，允许离散结果。 | 已清楚；无。 |
| B10-051 分位数处理差与个体差分位数 | 329–332，“未必是同一个人”；`sec:causal-distribution-response` | 防止边缘排名配对被误作个体变化。 | 排序对应需额外规定 | 耦合在第9章已读；后联合表具体展示。 | 已清楚；无。 |
| B10-052 总变差的响应比较 | 334–335，“不要求矩”；`sec:causal-distribution-response` | 按事件风险判断干预分布差。 | 第9章正式定义与界 | 已回顾，不能由均值差代替。 | 已清楚；无。 |
| B10-053 Wasserstein响应比较 | 335–336，“有限p阶矩条件”；`sec:causal-distribution-response` | 引入结果几何与移动成本。 | 第9章距离定义 | 已回顾，保留空间和矩条件。 | 已清楚；无。 |
| B10-054 KL响应比较 | 336，“绝对连续性…有限”；`sec:causal-distribution-response` | 引入似然差异尺度。 | 第9章KL定义 | 非一般对称距离，不省略支持条件。 | 已清楚；无。 |
| B10-055 跨行动配对 | 339–341，“如何在同一背景上配对”；`sec:causal-distribution-response` | 指出干预边缘仍缺个体联合。 | 精确前指两张表 | 此处预告，后509–528落实。 | 预告清楚；无。 |
| B10-056 局部响应Jacobian | 352–360，“开集…可微”；`sec:causal-local-response` | 计算连续剂量小扰动。 | 明确`DR·h+o(‖h‖)` | 第3章770–908已核对，固定M与u。 | 已清楚；无。 |
| B10-057 局部导数与有限差 | 363–366，“差为3…导数值2”；`sec:causal-local-response` | 限制线性近似可用范围。 | `R=u+t²`、2h+h² | 离散处理没有双侧开邻域。 | 已清楚；无。 |
| B10-058 平均响应m(t) | 368–369，“还包含积分”；`sec:causal-local-response` | 将个体导数问题接到总体。 | `E[R(t,U)]` | 逐个可微不推出可交换期望。 | 已清楚；无。 |
| B10-059 可积导数支配g | 372–378，“t∈I”；`sec:causal-local-response` | 给求导与平均交换的可检验条件。 | `thm:causal-response-differentiation` | 同一可积函数控制邻域，非逐点不同控制。 | 已清楚；无。 |
| B10-060 中值定理控制差商 | 385–392，“≤g(u)”；`sec:causal-local-response` | 把导数界变成支配收敛所需界。 | 显式差商及可积性论证 | 第3章1029–1062已实际核对。 | 已清楚；无。 |
| B10-061 支配收敛交换求导期望 | 393–403，“极限移入期望”；`sec:causal-local-response` | 得到`m'=E∂R`而非形式计算。 | 全部证明及`eq:causal-average-response-derivative` | 第3章2350–2463先前实读可用。 | 已清楚；无。 |
| B10-062 向量逐坐标求导的边界 | 406–408，“完整可微性…余项”；`sec:causal-local-response` | 防止偏导都存在被读作全微分存在。 | 第3章偏导反例 | 仅推广说明，未假称已证明全部向量结论。 | 已清楚；无。 |
| B10-063 因果导数与观测回归斜率 | 410–412，“人群…还可能改变”；`sec:causal-local-response` | 解释改变t可能同时改变被选择背景。 | 后敏感性例准确前指 | 非相同函数的两种求导记号。 | 已清楚；无。 |
| B10-064 Itô微分 | 413–415，“随机轨道…一般不存在普通…导数”；`sec:causal-local-response` | 只划清普通输入微分的边界。 | 时间随机累积的白话 | 纯比较预告，不要求此处会算随机积分。 | 预告足够；无。 |

## 条件反事实与补救

节标签：`sec:causal-counterfactual-recourse`、`sec:causal-factual-counterfactual`、`sec:causal-action-recourse`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B10-065 事实条件反事实变量 | 428–434，“同一外生背景”；`sec:causal-factual-counterfactual` | 已知个人记录后保留其背景信息。 | `def:causal-counterfactual` | V_a沿用行动映射，条件律不是重抽个人。 | 已清楚；无。 |
| B10-066 事实证据E与测量背景 | 437–438，“带噪测量…纳入背景”；`sec:causal-factual-counterfactual` | 使证据条件化有明确生成机制。 | 两点类型加独立测量量 | E可含结果，不等于前面处理前X。 | 已清楚；无。 |
| B10-067 溯因 | 438–440，“背景条件分布”；`sec:causal-factual-counterfactual` | 从事实更新未知背景。 | 484–494 Bayes两点后验 | 条件化不是证明模型正确。 | 已清楚；无。 |
| B10-068 干预预测三步计算 | 438–455，“同一个背景条件分布推到结果”；`sec:causal-factual-counterfactual` | 将溯因、规则替换、输出串成可算式。 | `eq:causal-counterfactual-pushforward` | 推前与条件核均已回顾。 | 已清楚；无。 |
| B10-069 正则条件核版本 | 442–460，“只保证…几乎处处”；`sec:causal-factual-counterfactual` | 连续零概率证据点不靠比值硬定义。 | 标准Borel入口与零点警示 | 第8章已读；指定版本非由恒等式唯一推出。 | 已清楚；无。 |
| B10-070 背景可部分确定而结果点识别 | 462–480，“未确定部分不影响”；`sec:causal-factual-counterfactual` | 避免误认为必须恢复全部U。 | U_Y=1、替代成绩8 | 给定模型内可算，非数据证明结果规则。 | 算例清楚；无。 |
| B10-071 背景后验的反事实推前 | 482–507，“未知背景不必…硬选”；`sec:causal-factual-counterfactual` | 展示反事实可以是分布而非单一点。 | `ex:causal-two-point-background-posterior`、均值5对先验4 | Bayes与δ点质量已回顾；测量随机性另补全。 | 已清楚；无。 |
| B10-072 潜在结果跨世界耦合 | 509–518，“相同边缘的不同耦合”；`sec:causal-factual-counterfactual` | 解释随机试验仍不恢复个体联合。 | 甲(0,0)/(1,1)，乙(0,1)/(1,0) | 第9章coupling定义已读；非实际同人双结果表。 | 已清楚；无。 |
| B10-073 联合表与条件反事实差别 | 520–528，“行和、列和均为1/2”；`sec:causal-factual-counterfactual` | 图支持边缘相同而条件答案不同。 | `fig:causal-cross-world-couplings`完整图注 | 只核解释和概率配对，不作视觉验收。 | 图说明充分；无。 |
| B10-074 重复干预资料的边界 | 530–534，“时间和携带效应假设”；`sec:causal-factual-counterfactual` | 说明重复测量也需跨时间稳定机制。 | 与单次随机试验边缘比较 | 作为资料扩展预告，未给无条件识别保证。 | 预告清楚；无。 |
| B10-075 预测器字段替换 | 539–545，“已训练函数…字段变化”；`sec:causal-action-recourse` | 为补救区分可计算反应与可行动反应。 | `f(x,1)-f(x,0)`和技能／时间联动 | 不是do语义的自动结果。 | 已清楚；无。 |
| B10-076 行动补救 | 547–552，“可实施行动…目标决策”；`sec:causal-action-recourse` | 由反事实计算反推低成本成功行动。 | `def:causal-recourse` | 因果版本按规则重算状态，不只找邻近输入。 | 已清楚；无。 |
| B10-077 可实施行动集合A(x) | 549、557–564，“实际允许做什么”；`sec:causal-action-recourse` | 排除不可能的建议。 | 不可变属性、空可行集 | 第4章1–113已核对；存在性不默认。 | 已清楚；无。 |
| B10-078 行动成本c(a;x) | 549、561–563，“如何比较行动”；`sec:causal-action-recourse` | 规定优化排序。 | 低输入距离不等于低成本 | 与可行性及目标成功分开。 | 已清楚；无。 |
| B10-079 目标集合G与决策d | 550、555–560，“d(F^a(u))∈G”；`sec:causal-action-recourse` | 把改善落实到指定最终决策。 | `eq:causal-recourse-objective` | 不一定优化内部预测分数。 | 已清楚；无。 |
| B10-080 概率型补救约束 | 566–572，“失败概率α”；`sec:causal-action-recourse` | 未知背景时允许明确风险预算。 | `eq:causal-recourse-probability` | 条件成功率，与无条件总体成功不同。 | 已清楚；无。 |
| B10-081 条件背景支持S_e | 573–577，“指定拓扑”；`sec:causal-action-recourse` | 给最坏情形选择候选背景。 | `supp P_(U\|E=e)` | 第8章支持已读；一般可测空间无默认支持。 | 已清楚；无。 |
| B10-082 支持上最坏情形补救 | 578–585，“逐点成功…强于概率一”；`sec:causal-action-recourse` | 不允许支持中的任何背景失败。 | `eq:causal-recourse-robust` | 包含零概率点，不等于α=0自动同义。 | 已清楚；无。 |
| B10-083 概率与稳健成功的差别 | 587–589，“3/4…低类型…2”；`sec:causal-action-recourse` | 用同一后验比较两个约束。 | 目标≥5、α=1/4 | 代表背景法漏掉剩余风险。 | 已清楚；无。 |
| B10-084 补救持久性及多人竞争 | 591–594，“无法共同执行”；`sec:causal-action-recourse` | 限定静态逐人模型可给的保证。 | 价格、名额、规则更新 | 现实可行性／公平性不是模型内成功定理。 | 边界清楚；无。 |

## 公平补救与识别入口

节标签：`sec:causal-fair-recourse`、`sec:causal-effect-identification`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B10-085 受保护属性A | 603，“受保护属性”；`sec:causal-fair-recourse` | 指明要比较同人替代属性世界。 | 后二元A资格例 | 属性干预是比较操作，不是建议个人改变属性。 | 已清楚；无。 |
| B10-086 事实X的局部口径切换 | 603–605，“可能包含…后继变量”；`sec:causal-fair-recourse` | 防止沿用CATE的处理前不变约定。 | 事实X固定于证据，替代X须重算 | 显式提醒同字母此处含义不同。 | 已清楚；无。 |
| B10-087 反事实公平 | 606–620，“每个可测预测值集合”；`sec:causal-fair-recourse` | 同事实背景下比较预测分布。 | `eq:causal-counterfactual-fairness` | 分布相等不等于逐背景点值相等；a.e.证据口径明确。 | 已清楚；无。 |
| B10-088 固定事实条件比较属性世界 | 622–624，“仍以事实A=a为条件”；`sec:causal-fair-recourse` | 防止把公平变成不同群体间直接比较。 | 同一条件核、重算后继 | 不等于锁住全部输入只换A。 | 已清楚；无。 |
| B10-089 兼容联合行动映射 | 626–629，“同一个可比较的行动b”；`sec:causal-fair-recourse` | 公平补救需要联合替换语义。 | `F_M^(b,A←a')` | 不能逐世界另选更有利行动；兼容性需模型给出。 | 已清楚；无。 |
| B10-090 决策条件分布Π_b^a' | 630–637，“d(F…(U))∈B”；`sec:causal-fair-recourse` | 缩写联合行动后的分布对象。 | Π的完整定义 | B为可测决策集合，与培训变量B后例语境不同。 | 已清楚；无。 |
| B10-091 公平约束补救优化 | 638–650，“成功…同背景…不随属性改变”；`sec:causal-fair-recourse` | 同时控制成功率和分布公平。 | `eq:causal-fair-recourse-objective` | 两项约束相互独立，不由成功自动得公平。 | 已清楚；无。 |
| B10-092 近似公平及成本公平 | 649–650，“会改变问题”；`sec:causal-fair-recourse` | 标出替代公平标准不是当前等式推论。 | 无额外算法或定量式 | 纯边界预告；无需此处详细理论。 | 预告清楚；无。 |
| B10-093 公平补救成本算例 | 652–669，“最优行动…b=2”；`sec:causal-fair-recourse` | 给出成功但不公平与公平但失败的不同情况。 | `ex:causal-fair-recourse`，b=1、2、0三种 | 逐世界重算K，阈值计算可直接核算。 | 已清楚；无。 |
| B10-094 分数公平与决策公平 | 671–672，“始终相差1”；`sec:causal-fair-recourse` | 展示选哪个输出会改变可行性。 | 分数1+b-a'与二元阈值 | 同一模型不同目标，不是计算矛盾。 | 已清楚；无。 |
| B10-095 个体行动公平与推荐规则公平 | 673–674，“目标人群几乎处处”；`sec:causal-fair-recourse` | 单个实例约束不能推出总体程序公平。 | 推荐依赖事实的说明 | 需额外量化推荐规则，不偷偷推广。 | 已清楚；无。 |
| B10-096 相容模型类上的公平范围 | 676–679，“报告结论范围”；`sec:causal-fair-recourse` | 机制未知会改变反事实及补救判断。 | 回用跨世界两耦合例 | 模型内等式与资料唯一确定分开。 | 已清楚；无。 |
| B10-097 规范性路径选择 | 679，“另需论证的规范选择”；`sec:causal-fair-recourse` | 指出哪些影响应排除不是数据自动决定。 | 公平性／可解释性准确后指 | 纯应用边界预告，不强加单一价值标准。 | 已清楚；无。 |
| B10-098 统计识别思想回用 | 687–690，“模型索引…完整生成机制”；`sec:causal-effect-identification` | 从给定模型计算转入未知机制推断。 | `def:statistics-identifiability`回指 | 第8章已完整读；正式条件紧接下一段。 | 入口清楚；无。 |
| B10-099 观察资料与试验资料 | 687–688，“观察或试验资料”；`sec:causal-effect-identification` | 明确信息来源也属于识别问题的输入。 | 与前随机试验边缘例呼应 | 不假定可观测分布只含自然观察。 | 已清楚；无。 |

## 点识别与调整

节标签：`sec:causal-effect-identification`、`sec:causal-point-identification`、`sec:causal-randomized-identification`、`sec:causal-adjustment-identification`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B10-100 可观测分布P_obs^M | 692，“已声明观测制度”；`sec:causal-effect-identification` | 比较两个模型究竟给出相同什么信息。 | 695–696蕴含式 | 包括已完成试验，不仅自然分布。 | 已清楚；无。 |
| B10-101 因果目标可识别 | 693–699，“τ(M₁)=τ(M₂)”；`sec:causal-effect-identification` | 同样资料不能容许不同目标答案。 | 开篇两机制反例、明确量词 | 已回顾统计识别；不要求全部机制唯一。 | 已清楚；无。 |
| B10-102 识别、估计与计算 | 701–704，“总体层面的唯一性”；`sec:causal-effect-identification` | 防止准确拟合被当作因果证明。 | 相同观测但不同行动例 | 样本误差和数值误差不消除机制歧义。 | 已清楚；无。 |
| B10-103 随机分配 | 716–718，“独立随机装置”；`sec:causal-randomized-identification` | 直接使分组不透露潜在结果。 | `(Y(0),Y(1))⊥T` | 两种处理须正概率；与实际接受处理分开。 | 已清楚；无。 |
| B10-104 随机化边缘识别 | 719–738，“第一个…随机分配，第二个…一致性”；`sec:causal-randomized-identification` | 用实际组分布恢复每个干预边缘。 | `eq:causal-randomization-marginal-distribution`完整两步 | 不恢复跨世界联合，前表已示例。 | 已清楚；无。 |
| B10-105 不依从与随机化后选择 | 739–741，“邀请不等于实际参加”；`sec:causal-randomized-identification` | 限制简单组均值差适用的记录制度。 | 按参加者重新分组例 | 失访、溢出是明确边界预告，未声称给出修复法。 | 预告清楚；无。 |
| B10-106 条件交换性 | 748–759，“不再额外透露潜在结果的信息”；`sec:causal-adjustment-identification` | 观察资料按处理前共同X建立可比性。 | `eq:causal-conditional-exchangeability` | 与样本重排可交换性明确区分，不能由预测检验。 | 已清楚；无。 |
| B10-107 边缘交换性与联合交换性 | 758–759，“单个边缘…只需”；`sec:causal-adjustment-identification` | 避免为单一目标强加完整联合假设。 | `Y(t)⊥T\|X` | 联合蕴含边缘，反向不默认。 | 已清楚；无。 |
| B10-108 倾向概率e(x) | 763，“P(T=1\|X=x)”；`sec:causal-adjustment-identification` | 用单一量描述二元分配支持。 | e(1)=0.8、e(0)=0.2 | 不是处理效果或个体背景概率。 | 已清楚；无。 |
| B10-109 支持重叠／正值性 | 761–771，“0<e(x)<1”；`sec:causal-adjustment-identification` | 可比人群还必须有对应处理记录。 | `eq:causal-overlap`、某类必处理反例 | a.e.条件，非要求连续X逐点有原子概率。 | 已清楚；无。 |
| B10-110 目标相对支持 | 773–777，“只有它会使用的…组合”；`sec:causal-adjustment-identification` | 让覆盖随目标而非一律全空间要求。 | Y(1)只需e>0，策略只需目标动作 | 改总体同时改支持及可比性条件。 | 已清楚；无。 |
| B10-111 调整公式 | 779–795，“全期望…交换性…一致性”；`sec:causal-adjustment-identification` | 将潜在期望化成可观测层内均值。 | `eq:causal-g-formula`逐步推导 | 三项假设各承担明确替换；潜在结果可积。 | 已清楚；无。 |
| B10-112 结果回归μ_t | 796，“E[Y\|T=t,X=x]”；`sec:causal-adjustment-identification` | 缩写可估计的两组条件均值。 | `eq:causal-ate-adjustment` | 识别假设成立才成为条件因果均值。 | 已清楚；无。 |
| B10-113 ATE调整表示 | 796–801，“两式相减”；`sec:causal-adjustment-identification` | 按同一个目标X分布平均条件差。 | `E_X[μ₁-μ₀]` | 事件指示量也可恢复分布概率。 | 已清楚；无。 |
| B10-114 逆概率加权表示 | 803–824，“较少进入…更大权重”；`sec:causal-adjustment-identification` | 用另一种统计表达实现同一识别目标。 | `eq:causal-ipw-identification`及逐条件核算 | 潜在结果可积与交换性确保加权绝对可积；非新假设。 | 已清楚；无。 |
| B10-115 调整与原始组差算例 | 828–858，“0.44…0.20”；`sec:causal-adjustment-identification` | 具体展示选择构成如何扭曲差异。 | 四格均值表、Bayes组比例、算式 | 全部数值自洽，未把示例当实验数据。 | 已清楚；无。 |
| B10-116 缺重叠与弱重叠 | 860–865，“接近但未等于1”；`sec:causal-adjustment-identification` | 区分识别失败与估计困难。 | e(1)=1对接近1 | 权重大不等于目标不可识别；图证书尚只预告。 | 已清楚；无。 |

## 部分识别、策略界与敏感性

节标签：`sec:causal-partial-identification-sensitivity`、`sec:causal-outcome-bounds`、`sec:causal-support-policy-bounds`、`sec:causal-sensitivity-ranges`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B10-117 部分识别 | 870–872，“排除了哪些答案”；`sec:causal-partial-identification-sensitivity` | 假设不够时保留相容值而非强选一个。 | 后有界结果构造 | 不是计算没收敛或数据量暂小。 | 已清楚；无。 |
| B10-118 相容模型集合M(P_obs) | 875，“分布及已声明假设相容”；`sec:causal-partial-identification-sensitivity` | 给识别范围指定候选域。 | `def:causal-identified-set` | 空集表示假设矛盾，不是目标取空值。 | 已清楚；无。 |
| B10-119 识别集合I(P_obs) | 876–885，“一般…分离的点或区间”；`sec:causal-partial-identification-sensitivity` | 取相容模型目标值的像。 | `eq:causal-identified-set` | 与上下界区间包络不同，区间内可达性另证。 | 已清楚；无。 |
| B10-120 有界潜在结果约束 | 890，“0≤Y(t)≤1”；`sec:causal-outcome-bounds` | 用已知结果范围控制未观察项。 | 拆成TY和缺失部分 | 不需要交换性，但保留一致性。 | 已清楚；无。 |
| B10-121 单处理均值缺失界 | 891–915，“可见与缺失部分”；`sec:causal-outcome-bounds` | 分别限制E Y(1)和E Y(0)。 | `eq:causal-bounded-outcome-y1`、`…-y0` | 概率乘范围，不能把缺失项设零当事实。 | 已清楚；无。 |
| B10-122 Manski型ATE界 | 916–925，“下端减…上端”；`sec:causal-outcome-bounds` | 组合得到效应范围。 | `eq:causal-manski-ate-bounds` | 是当前假设的总体界，尚需证锐性。 | 已清楚；无。 |
| B10-123 锐界 | 928–934，“inf…sup”；`sec:causal-outcome-bounds` | 区分无法改进的边界与方便有效界。 | `def:causal-sharp-bounds` | 端点可以只逼近，不自动达到。 | 已清楚；无。 |
| B10-124 界端点的机制实现 | 936–939，“保持所有实际记录不变”；`sec:causal-outcome-bounds` | 证明界不是代数放松造成。 | 缺失Y(1)、Y(0)分别赋0/1 | 保持事实且满足范围／一致性，构造完整。 | 已清楚；无。 |
| B10-125 混合机制实现中间值 | 941–946，“独立…二元背景标记”；`sec:causal-outcome-bounds` | 证明整个区间是识别集合。 | λτ_up+(1-λ)τ_low | 新限制可能禁止混合，故不推广到所有模型类。 | 已清楚；无。 |
| B10-126 重叠区O与缺口区N | 951–958，“不交且覆盖”；`sec:causal-support-policy-bounds` | 定位效应中哪些背景仍未知。 | 指示函数分解τ | 交换性可信但支持不全，与无交换性前例不同。 | 已清楚；无。 |
| B10-127 支持缺口效应包络 | 959–973，“未声称总是锐界”；`sec:causal-support-policy-bounds` | 用未知区质量量化不可识别部分。 | `eq:causal-overlap-gap-bounds` | 已知一侧结果还可收紧；限制目标会换问题。 | 已清楚；无。 |
| B10-128 日志动作概率e_a | 975–978，“P(T=a\|X=x)”；`sec:causal-support-policy-bounds` | 将倾向概率扩成有限动作记录制度。 | 后逐a求和 | 不等于目标π，已观测制度可不同。 | 已清楚；无。 |
| B10-129 策略绝对覆盖 | 978–982，“π>0⇒e_a>0”；`sec:causal-support-policy-bounds` | 只要求目标使用的动作可被参照。 | a.e.条件及Y(a)∈[L,H] | 第8章换测度支持要求的因果版本。 | 已清楚；无。 |
| B10-130 策略价值加权 | 983–1001，“π(T\|X)/e_T(X)”；`sec:causal-support-policy-bounds` | 将日志平均变为目标动作平均。 | `eq:causal-policy-value-weighting`完整条件期望证明 | 保留给定X、动作的结果机制；只在实际动作求值。 | 已清楚；无。 |
| B10-131 目标缺口质量r | 1003–1006，“e_a(X)=0”；`sec:causal-support-policy-bounds` | 汇总策略会选但日志从不选的部分。 | 明确期望求和 | 不同于日志缺失样本的经验比例。 | 已清楚；无。 |
| B10-132 已识别贡献K | 1007–1010，“e_a(X)>0”；`sec:causal-support-policy-bounds` | 把价值拆成已知贡献与未知余项。 | K的加权条件均值式 | 只对覆盖部分求和，不重新归一化。 | 已清楚；无。 |
| B10-133 策略价值界 | 1012–1016，“K+Lr…K+Hr”；`sec:causal-support-policy-bounds` | 将缺口质量转成结果范围。 | `eq:causal-policy-value-bounds` | r=0恢复点识别；有界结果是所用条件。 | 已清楚；无。 |
| B10-134 策略排序的联合约束 | 1017–1027，“不能…端点…独立可选”；`sec:causal-support-policy-bounds` | 两目标共享未知结果，须直接界价值差。 | 同策略差恒零、显式差公式 | 边际范围相交不代表无法判断所有差。 | 已清楚；无。 |
| B10-135 混杂与覆盖的双面板图 | 1029–1041，“两个独立的教学构造”；`sec:causal-support-policy-bounds` | 把组成偏差与不可观测质量分开可算。 | `fig:causal-confounding-coverage`、r=.2得[.48,.68] | 阴影是识别范围而非置信带；非同一数据集。 | 图注充分；无。 |
| B10-136 序贯策略覆盖 | 1043–1045，“不能…单步权重…整条轨迹”；`sec:causal-support-policy-bounds` | 限定当前单步结果的边界。 | 后动态规划准确引用 | 纯预告历史覆盖与时变混杂。 | 预告清楚；无。 |
| B10-137 敏感性分析 | 1050–1052，“规定其允许强度”；`sec:causal-sensitivity-ranges` | 未记录选择差异不能直接假为零。 | 后Λ与Γ偏差界 | 与样本误差条不同，范围来自机制假设。 | 已清楚；无。 |
| B10-138 线性未观测混杂模型 | 1053–1059，“T=αU+ε_T”；`sec:causal-sensitivity-ranges` | 找到观测斜率偏离因果导数的项。 | 中心化、两两独立、有限方差 | 这些条件足以求协方差，不用额外高斯假设。 | 已清楚；无。 |
| B10-139 总体回归斜率β_obs | 1060–1073，“Cov(T,Y)/Var(T)”；`sec:causal-sensitivity-ranges` | 与固定背景导数β直接比较。 | `eq:causal-linear-confounding-bias`及两条协方差展开 | 第8章线性投影已读；不是任意非线性回归导数。 | 已清楚；无。 |
| B10-140 线性敏感度Λ | 1074–1078，“偏差绝对值不超过”；`sec:causal-sensitivity-ranges` | 把无法分离的结构系数变成范围假设。 | β_obs±Λ | Λ不是由同一回归自动估计的识别量。 | 已清楚；无。 |
| B10-141 选择偏差函数b₁(x) | 1082–1086，“Y(1)…T=1…T=0”；`sec:causal-sensitivity-ranges` | 描述同X下已处理与未处理的处理潜在均值差。 | 显式定义 | 一项均值缺失，不能直接观测。 | 已清楚；无。 |
| B10-142 选择偏差函数b₀(x) | 1087–1089，“Y(0)…T=1…T=0”；`sec:causal-sensitivity-ranges` | 描述未处理潜在均值的对应选择差。 | 显式定义 | 与b₁不是同一个结果量，符号方向统一。 | 已清楚；无。 |
| B10-143 条件均值交换性 | 1091–1093，“反过来只得到…均值”；`sec:causal-sensitivity-ranges` | 区分零偏差函数与全分布独立。 | 恒0对±1等概率 | 不能将两个均值相等当潜在结果分布相同。 | 已清楚；无。 |
| B10-144 选择偏差校正式 | 1095–1117，“-(1-e)b₁-eb₀”；`sec:causal-sensitivity-ranges` | 明确观测条件差中需扣除哪些偏差。 | `eq:causal-selection-bias-function`两侧全期望推导 | 一致性而非完整交换性用于替换可见项。 | 已清楚；无。 |
| B10-145 偏差控制Γ_t与Δ | 1118–1131，“三角不等式”；`sec:causal-sensitivity-ranges` | 给条件效应和总体效应有效范围。 | `eq:causal-sensitivity-bounds`、可积性说明 | Δ不是效应本身；包络不未经可达性称锐。 | 已清楚；无。 |
| B10-146 结论翻转阈值 | 1133–1134，“多大强度下…变号”；`sec:causal-sensitivity-ranges` | 使敏感性报告能判断结论依赖程度。 | Γ的扫描建议 | 不是挑一个保留原结论的参数。 | 已清楚；无。 |
| B10-147 个体单调性 | 1135–1140，“Y(1)≥Y(0)”；`sec:causal-sensitivity-ranges` | 用实质假设排除受损个体、收紧下界。 | ATE≥0 | 比平均有益强，不是响应随任意连续t单调的默认声明。 | 已清楚；无。 |
| B10-148 个体效应范围ρ | 1140–1141，“[-ρ,ρ]”；`sec:causal-sensitivity-ranges` | 在缺口中用更窄机制约束。 | 替换[-1,1] | 与仅有结果范围不同；外推需声明。 | 已清楚；无。 |
| B10-149 跨环境效应运输 | 1143–1153，“条件效应…相同”；`sec:causal-sensitivity-ranges` | 结合源试验与目标背景分布。 | `∫τ_source dP_X,target` | 目标对源绝对连续；拓扑支持包含不够。 | 已清楚；无。 |
| B10-150 将模型歧义传播到补救公平 | 1155–1157，“不是仅报告…模拟精度”；`sec:causal-sensitivity-ranges` | 相同边缘仍可改变条件行动成功。 | 前跨世界配对例 | 计算精度不能替代模型识别。 | 已清楚；无。 |

## 有限样本估计

节标签：`sec:causal-response-estimation`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B10-151 调整代入估计τ̂ | 1162–1169，“μ̂_t代替μ_t”；`sec:causal-response-estimation` | 总体识别量仍须由样本估计。 | `n⁻¹Σ(μ̂₁-μ̂₀)` | 不自动无偏，也未承诺速率。 | 已清楚；无。 |
| B10-152 样本拆分与交叉拟合 | 1170–1172，“哪些样本拟合…评价”；`sec:causal-response-estimation` | 控制数据复用的统计依赖。 | 第8章相关规则回指 | 已回顾；这里不使用未陈述的渐近定理。 | 已清楚；无。 |
| B10-153 倾向估计与权重截断 | 1174–1176，“改变偏差与方差”；`sec:causal-response-estimation` | 弱重叠会带来估计不稳定。 | 小非零真实概率例 | 截断不补支持，灵活模型不修复交换性。 | 已清楚；无。 |
| B10-154 识别集合端点估计 | 1178–1181，“两个端点共同…覆盖”；`sec:causal-response-estimation` | 部分识别也有抽样误差。 | 端点／包络作为估计对象 | 端点估计不等于真锐界；联合覆盖须处理。 | 已清楚；无。 |
| B10-155 置信区间与识别集合 | 1179–1181，“有限样本…估计误差”；`sec:causal-response-estimation` | 区分机制歧义和抽样不确定性。 | 第8章区间概念及前阴影说明 | 已回顾，不把两种范围混成一个误差条。 | 已清楚；无。 |
| B10-156 数值误差 | 1183–1186，“积分或优化”；`sec:causal-response-estimation` | 第三类不确定性来自计算近似。 | 增样本／改算法／改设计各作用分开 | 与机制范围、抽样误差不同。 | 已清楚；无。 |

## 局部机制与响应复合

节标签：`sec:causal-generating-structure`、`sec:causal-local-structural-equations`、`sec:causal-mechanism-composition`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B10-157 内生变量 | 1199，“模型内需要解释”；`sec:causal-local-structural-equations` | 打开响应接口、声明生成方程的输出。 | 培训、技能、成绩 | 相对模型边界，不表示现实必然可控。 | 已清楚；无。 |
| B10-158 外生变量 | 1199–1201，“当前模型不再解释”；`sec:causal-local-structural-equations` | 为局部方程保留未展开背景。 | U_T、U_M、U_Y | 不等于现实无原因，也不自动独立。 | 已清楚；无。 |
| B10-159 父变量pa_j | 1201–1202、1214，“直接读取哪些输入”；`sec:causal-local-structural-equations` | 表示局部函数的内生输入。 | `f_j(pa_j,U_j)` | 不等于所有统计相关量。 | 已清楚；无。 |
| B10-160 无环SCM | 1204–1216，“可测…联合分布…结构函数”；`sec:causal-local-structural-equations` | 从局部机制构造整体响应。 | `eq:causal-scm-definition` | 图、函数、噪声律共同组成，不是图独自决定数值。 | 已清楚；无。 |
| B10-161 无环性与求值次序 | 1215–1216，“更早的节点”；`sec:causal-local-structural-equations` | 提供无歧义逐步生成方法。 | 1255–1267归纳证明 | 不预借图排序算法，次序本身足以使用。 | 已清楚；无。 |
| B10-162 因果DAG | 1219–1222，“作为输入…画箭头”；`sec:causal-local-structural-equations` | 用图压缩直接输入关系。 | T→M、T→Y、M→Y | 条件分解箭头本身不保证因果语义。 | 已清楚；无。 |
| B10-163 相关背景与省略共同原因 | 1230–1233，“三条内生边不足”；`sec:causal-local-structural-equations` | 防止误套独立噪声概率规则。 | U各分量相关的培训例 | 外生相关需完整联合律或显式共同来源。 | 已清楚；无。 |
| B10-164 局部参数θ_j | 1235–1238，“一般SCM…不必有限维”；`sec:causal-local-structural-equations` | 区分边结构未知和函数未知。 | α、β、γ | 参数化是研究者选的函数族，不是SCM定义必需。 | 已清楚；无。 |
| B10-165 无环机制唯一可测响应定理 | 1247–1254，“每个背景…唯一”；`sec:causal-mechanism-composition` | 补足开章接口假定的实现依据。 | `thm:causal-acyclic-response` | 函数可测、有限无环次序充分，非独立噪声才唯一。 | 已清楚；无。 |
| B10-166 可测复合归纳 | 1255–1261，“代入可测的f_j”；`sec:causal-mechanism-composition` | 同时证明存在、可测、唯一。 | 逐坐标完整证明 | 第8章映射复合与有限乘积可用；唯一性另说明。 | 已清楚；无。 |
| B10-167 常量替换保次序 | 1263–1264，“不增加逆向依赖”；`sec:causal-mechanism-composition` | 将自然响应定理扩到理想干预。 | 原次序重算未替换坐标 | 任意新增依赖不享此保证。 | 已清楚；无。 |
| B10-168 联合可测的处理响应 | 1265–1267，“乘积空间上的投影”；`sec:causal-mechanism-composition` | 不只逐固定t可测，满足开章联合要求。 | `(t,u)↦t`再复合 | 无须偷换分别可测与联合可测。 | 已清楚；无。 |
| B10-169 SCM中的一致性证明 | 1270–1274，“自然解也满足…替换”；`sec:causal-mechanism-composition` | 将记录对应潜在结果从条件变为构造结论。 | 唯一性得两解相同 | 同一背景下取自然处理值，非重新抽样。 | 已清楚；无。 |
| B10-170 中介响应M(t) | 1276–1287，“必须先重算”；`sec:causal-mechanism-composition` | 合成结果时不能用事实技能。 | `M(t)=αt+U_M` | 不受处理影响的X可保留，M不行。 | 已清楚；无。 |
| B10-171 总响应系数β+γα | 1288–1290，“直接贡献1…传递6”；`sec:causal-mechanism-composition` | 区分总效应与局部结果偏导。 | α=2、β=1、γ=3得7 | 直接／间接描述是此模型代数，未冒充一般路径识别。 | 已清楚；无。 |
| B10-172 非线性机制链式导数 | 1291–1301，“干预取值处计算”；`sec:causal-mechanism-composition` | 将局部方程导数接成整体响应导数。 | ∂f_Y/∂t+(∂f_Y/∂m)(∂f_M/∂t) | 第3章770–908已核对；再平均仍需支配条件。 | 已清楚；无。 |
| B10-173 机制概率核K_j | 1303–1310，“由机制及噪声分布指定”；`sec:causal-mechanism-composition` | 独立外生噪声时按局部条件规律生成。 | 显式K_j(B\|pa_j)定义 | 概率核已回顾；当前噪声不能被更早变量筛选。 | 已清楚；无。 |
| B10-174 DAG局部因子乘积 | 1310–1313，“沿无环次序复合”；`sec:causal-mechanism-composition` | 将生成过程写成联合质量／密度。 | `p(v)=∏p(v_j\|pa_j)` | 需相应质量或密度，不要求所有空间均有Lebesgue密度。 | 已清楚；无。 |
| B10-175 截断分解 | 1314–1324，“处理核换成点质量”；`sec:causal-mechanism-composition` | 用因子表达机制替换。 | `eq:causal-truncated-factorization` | 不是任意分解删除因子；相关外生噪声时失效。 | 已清楚；无。 |
| B10-176 删除坐标记号v_-T | 1322，“删除处理坐标”；`sec:causal-mechanism-composition` | 说明干预密度对什么变量取值。 | 左侧v_-T | 固定T后只分布剩余变量，避免缺少归一化变量。 | 已清楚；无。 |
| B10-177 机制指定条件版本 | 1326–1328，“未见过的父变量组合”；`sec:causal-mechanism-composition` | 区分模型可算与观测支持上的识别。 | 支持外任意补密度警示 | 第8章核版本已回顾，干预可能走出自然支持。 | 已清楚；无。 |
| B10-178 随机干预的局部因子式 | 1330–1338，“p(x)q(t\|x)p(y\|t,x)”；`sec:causal-mechanism-composition` | 兑现前面随机干预构造。 | `eq:causal-stochastic-intervention` | 独立新噪声及其余机制不变；确定策略用点质量。 | 已清楚；无。 |
| B10-179 反馈／循环方程边界 | 1339–1344，“无解…无穷多组解”；`sec:causal-mechanism-composition` | 说明为何不任意推广无环递归。 | V₁=V₂+1,V₂=V₁及相等例 | 动态演化／平衡选择仅预告所需扩展。 | 已清楚；无。 |

## 图语义与调整条件

节标签：`sec:causal-graph-adjustment`、`sec:causal-local-path-patterns`、`sec:causal-global-path-separation`、`sec:causal-backdoor-selection`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B10-180 共同原因 | 1357–1361，“T←X→Y”；`sec:causal-local-path-patterns` | 用输入关系解释处理组背景差异。 | 风险分层例准确回指 | 混杂的一种机制，不是任何相关都叫共同因果。 | 已清楚；无。 |
| B10-181 中介变量 | 1363–1367，“一部分影响经过它”；`sec:causal-local-path-patterns` | 区分总效应目标与固定中介目标。 | β对β+γα | 联合设定T,M需单独定义；未给一般路径效应识别承诺。 | 已清楚；无。 |
| B10-182 碰撞点 | 1369–1374，“两条箭头在此相遇”；`sec:causal-local-path-patterns` | 解释筛选能制造依赖。 | 总分补偿入选对双阈值入选 | 相关正负取决于机制，不是图方向自动规定。 | 已清楚；无。 |
| B10-183 给定变量的图标记 | 1376–1386，“双边框”；`sec:causal-local-path-patterns` | 图上显式区分条件集节点。 | `fig:causal-local-path-patterns`及TikZ完整读取 | 开闭路径不代表确定相关强度；解释一致。 | 已清楚；无。 |
| B10-184 图G=(V,E) | 1392–1393，“节点集…有向边集”；`sec:causal-global-path-separation` | 从三点模式转为全图规则。 | 后五节点例 | 自含最少图对象，不预设后图论章。 | 已清楚；无。 |
| B10-185 无向意义路径 | 1394，“忽略箭头…互不重复”；`sec:causal-global-path-separation` | 允许追踪非因果方向的联系。 | X-M-Y和X-C-Y | 与有向路径明确分开；排除重复节点。 | 已清楚；无。 |
| B10-186 有向路径 | 1395，“沿箭头前进”；`sec:causal-global-path-separation` | 定义传播方向与祖先后代。 | X→M→Y | 非任意相邻序列。 | 已清楚；无。 |
| B10-187 后代 | 1396–1398，“长度至少为一”；`sec:causal-global-path-separation` | 判断条件化后继是否打开碰撞点。 | C→D | 不含自身，约定明确。 | 已清楚；无。 |
| B10-188 祖先 | 1397–1398，“v是w的祖先”；`sec:causal-global-path-separation` | 反向描述有向可达关系。 | 同一有向路径定义 | 不等于紧邻父变量。 | 已清楚；无。 |
| B10-189 路径相对碰撞／非碰撞 | 1402–1403、1412，“在该路径上”；`sec:causal-global-path-separation` | 防止给节点永久贴一个角色。 | 相邻两箭头汇入的判定式 | 同点在不同路径角色可不同。 | 已清楚；无。 |
| B10-190 活跃路径 | 1404–1405，“每个…且每个”；`sec:causal-global-path-separation` | 给逐路径开闭的充要规则。 | 非碰撞不在S，碰撞自身或后代在S | 包含后代是选择信息回传，非只检查三点。 | 已清楚；无。 |
| B10-191 d-分离 | 1407–1409，“每条路径都不活跃”；`sec:causal-global-path-separation` | 将局部规则提升为集合之间的阻断。 | `def:causal-d-separation` | A,B,S两两不交；单条关闭不够。 | 已清楚；无。 |
| B10-192 d-连接 | 1409，“否则”；`sec:causal-global-path-separation` | 表示存在未阻断联系的图状态。 | 四种条件集例 | 不等于必然统计依赖，后Markov节再次限制。 | 已清楚；无。 |
| B10-193 碰撞后代条件化 | 1413–1427，“给定其后代”；`sec:causal-global-path-separation` | 明确多路径和后代共同作用。 | S=空、{M}、{M,C}、{M,D}逐例 | 不单调：增加条件可破坏原分离。 | 已清楚；无。 |
| B10-194 多路径分离图 | 1428–1437，“上下方路径都关闭”；`sec:causal-global-path-separation` | 支持逐路而非凭局部模式下结论。 | `fig:causal-d-separation-paths`及TikZ全读 | 与正文五条边及条件S={M}一致。 | 已清楚；无。 |
| B10-195 因果Markov性 | 1440–1455，“图规则…分布性质”；`sec:causal-global-path-separation` | 从图阻断推出条件独立。 | 明确单向蕴含式 | 与时序Markov不同，也不自动反推图。 | 已清楚；无。 |
| B10-196 局部Markov表述 | 1457–1462，“给定父变量…非后代”；`sec:causal-global-path-separation` | 对接独立噪声构造的直观根据。 | 噪声不被前变量读取、逆次序核积分为1 | 局部／全局等价明确引用标准结论；未伪称已完整证明。 | 条件和来源足够；无。 |
| B10-197 DAG分解与d-分离全局对应 | 1461–1464，“标准结论”；`sec:causal-global-path-separation` | 将因子计算与路径语义相连。 | Pearl引用及后图章证明边界 | 本处作为声明工具使用，相关背景省略不能套。 | 已清楚；无。 |
| B10-198 后门路径 | 1471–1473，“第一条边指向T”；`sec:causal-backdoor-selection` | 专门追踪自然选择携带的背景联系。 | 共同原因路径 | 路径不必整体有向，已用1394定义。 | 已清楚；无。 |
| B10-199 后门准则 | 1475–1481，“不含…后代…阻断所有”；`sec:causal-backdoor-selection` | 给调整变量一个结构充分条件。 | `def:causal-backdoor-criterion` | 不只是处理前测量或高预测力。 | 已清楚；无。 |
| B10-200 后门调整代表图推导 | 1483–1497，“替换…再对背景积分”；`sec:causal-backdoor-selection` | 把图证书接回已证明调整公式。 | `eq:causal-backdoor-adjustment`及三因子 | 一般空间核积分口径明确。 | 已清楚；无。 |
| B10-201 一般后门调整结论 | 1499–1505，“独立噪声…相关共同原因”；`sec:causal-backdoor-selection` | 将三节点结果扩至全DAG。 | 带条件的Pearl引用 | Markov性本身不提供干预语义；支持条件另需。 | 已清楚；无。 |
| B10-202 后门充分而非必要 | 1507–1512，“其他识别规则”；`sec:causal-backdoor-selection` | 不把本节准则当全部识别边界。 | 共同原因、中介、碰撞逐一复核 | 其他规则仅预告，未依赖未知公式。 | 已清楚；无。 |

## 关系发现与等价类

节标签：`sec:causal-structure-discovery`、`sec:causal-relation-inference`、`sec:causal-observational-structure`、`sec:causal-interventional-structure`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B10-203 变量关系推断 | 1517–1527，“哪些变量直接相连”；`sec:causal-structure-discovery` | 从已知图推出响应改为由数据限制图。 | 结构独立与参数抵消的问题 | 不等于局部函数估计，两种未知分别处理。 | 已清楚；无。 |
| B10-204 忠实性 | 1532–1544，“条件独立…图结构解释”；`sec:causal-observational-structure` | 为由分布反推路径阻断补反向假设。 | `def:causal-faithfulness` | 与Markov性相反方向，不能互换。 | 已清楚；无。 |
| B10-205 参数抵消导致不忠实 | 1546–1551，“β=-γα”；`sec:causal-observational-structure` | 给出独立噪声DAG仍不忠实的算例。 | Y=γU_M+U_Y与X独立 | 图有两条作用而和为零，计算完整。 | 已清楚；无。 |
| B10-206 近忠实边界弱依赖 | 1551，“非常弱…难以检出”；`sec:causal-observational-structure` | 说明总体非零不代表有限样本能判断。 | 接近抵消的连续变化 | 与恰好独立或定理失败不同。 | 已清楚；无。 |
| B10-207 三节点观测方向歧义 | 1553–1562，“无法区分…传递…共同变化”；`sec:causal-observational-structure` | 展示条件独立不足唯一方向。 | 三种非碰撞图同有X⊥Y\|Z | 限无其他路径；碰撞图的逆推需忠实性。 | 已清楚；无。 |
| B10-208 Markov等价 | 1564–1567，“相同的d-分离关系”；`sec:causal-observational-structure` | 将无法由独立模式区分的图归为同类。 | 上述三图 | 不是给定参数下恰好同一联合密度。 | 已清楚；无。 |
| B10-209 Markov等价类MEC | 1568–1569，“全部DAG组成”；`sec:causal-observational-structure` | 给观测结构识别明确的集合目标。 | 后部分有向表示 | 等价类不是选一张最优拟合图。 | 已清楚；无。 |
| B10-210 骨架 | 1572，“忽略箭头…邻接关系”；`sec:causal-observational-structure` | 给结构等价判据的第一部分。 | 非相邻节点分离证明 | 不含方向信息，不等于任意生成树。 | 已清楚；无。 |
| B10-211 无屏蔽碰撞结构 | 1573–1575，“两端…不相邻”；`sec:causal-observational-structure` | 区分可影响分离模式的局部碰撞。 | X→Z←Y且无X-Y边 | 不是全部碰撞节点都具有同一可识别作用。 | 已清楚；无。 |
| B10-212 等价类结构判据 | 1576–1577，“相同骨架…相同无屏蔽”；`sec:causal-observational-structure` | 避免逐枚举全部分离关系。 | Chickering来源 | 双向定理作为引用，必要性接着自行证明。 | 已清楚；无。 |
| B10-213 非相邻节点的父集分离 | 1579–1589，“w不是…后代”；`sec:causal-observational-structure` | 证明骨架由全分离关系确定。 | 入边父点阻断／出边首碰撞阻断两类完整论证 | 无环保节点选择，先前路径定义足够。 | 已清楚；无。 |
| B10-214 单边路径不可分离 | 1588–1589，“没有内部点”；`sec:causal-observational-structure` | 对比相邻与不相邻的分离特征。 | 无内部条件点可阻断 | 条件集不含端点的约定已明确。 | 已清楚；无。 |
| B10-215 无屏蔽碰撞的分离集判别 | 1591–1595，“必须包含…不能包含Z”；`sec:causal-observational-structure` | 证明碰撞差异改变独立模式。 | 长度2路径施加必要限制 | 其他路径增加约束，但不能移除该限制。 | 已清楚；无。 |
| B10-216 等价充分性的引用边界 | 1597–1598，“不把…冒充双向证明”；`sec:causal-observational-structure` | 明确长路径证明未在本章展开。 | 完整判据来源 | 不是隐藏逻辑跳步，读者知道借用哪条定理。 | 已清楚；无。 |
| B10-217 覆盖边 | 1599–1604，“pa(Y)=pa(X)∪{X}”；`sec:causal-observational-structure` | 给等价类内方向变换的可检验局部条件。 | 完整父集式 | 覆盖不是一般边可任意反转。 | 已清楚；无。 |
| B10-218 覆盖边反转定理 | 1605–1606，“仍为DAG…保持全部d-分离”；`sec:causal-observational-structure` | 知道这类方向变化不制造环和新独立。 | Chickering引用 | 条件明确，不从局部Bayes式单独推出。 | 已清楚；无。 |
| B10-219 覆盖边的因子重分解 | 1607–1616，“不改变…条件联合分布”；`sec:causal-observational-structure` | 用已学概率分解解释反转的分布直觉。 | 两项因子交换为逆向条件式 | 条件版本需相容；不冒充全图证明。 | 已清楚；无。 |
| B10-220 等价类覆盖边可达性 | 1617–1619，“有限次…相互到达”；`sec:causal-observational-structure` | 说明上述局部操作可连接全部等价图。 | 完整变换定理引用 | 与单边保持性、判据充分性是三个不同命题。 | 已清楚；无。 |
| B10-221 部分有向等价类表示 | 1621–1625，“同意的方向…其余无向”；`sec:causal-observational-structure` | 忠实、无混杂等条件下输出保留未识别方向。 | 同分布增样本不会创造方向信息 | 不把无向边误认为算法未运行完。 | 已清楚；无。 |
| B10-222 因果充分性 | 1627–1628，“共同原因…纳入可观测变量”；`sec:causal-observational-structure` | 补齐用DAG观测等价类的变量覆盖条件。 | 隐藏共同因不硬转直接边 | 与统计充分统计量非同一概念，当地含义清楚。 | 已清楚；无。 |
| B10-223 潜在混杂及端点标记部分图 | 1629–1631，“已确定的祖先关系…隐藏共同原因”；`sec:causal-observational-structure` | 预告变量不全时需更丰富输出。 | 选择／测量误差也改变模式 | 未使用PAG算法或端点规则，作为扩展预告足够。 | 预告清楚；无。 |
| B10-224 约束型结构算法 | 1633–1636，“未拒绝独立时删除候选边”；`sec:causal-observational-structure` | 描述由独立检验限制图的操作方向。 | 明确H₀及删边规则 | 未声称一种检验决定全部结构。 | 已清楚；无。 |
| B10-225 结构搜索中的第一类错误 | 1635，“可能保留虚假边”；`sec:causal-observational-structure` | 将第8章检验错误接到本地删边约定。 | H₀为独立，误拒绝阻止删边 | 限当前约束型规则，不泛化到评分法。 | 已清楚；无。 |
| B10-226 结构搜索中的第二类错误 | 1636，“可能删除真实边”；`sec:causal-observational-structure` | 说明漏检依赖的相反结构后果。 | 未拒绝即删的规则 | 错误会传播至搜索与定向，不只局部概率。 | 已清楚；无。 |
| B10-227 评分型算法 | 1637，“不能直接套用”；`sec:causal-observational-structure` | 仅限定前述错误对应不适用于所有算法。 | 无具体评分目标 | 纯算法类别边界预告；可选加“按整图拟合与复杂度评分”一句，非实质缺口。 | 无需独立问题；可选白话。 |
| B10-228 结构学习一致性 | 1638–1640，“检验…候选图范围…搜索”；`sec:causal-observational-structure` | 强调总体假设与统计、搜索保证必须共同成立。 | 需要核对的条件列表 | 已回顾估计一致性；未据此推出具体算法保证。 | 已清楚；可选明确恢复对象为等价类。 |
| B10-229 干预提供方向证据 | 1645–1649，“分布随设置值改变”；`sec:causal-interventional-structure` | 增加纯观测没有的约束。 | 保留其余机制、只干预X的条件 | 支持X是上游而非必为直接父点；无改变不排除作用。 | 已清楚；无。 |
| B10-230 实际执行与理想干预区别 | 1651–1654，“鼓励…不等同于…设定”；`sec:causal-interventional-structure` | 防止用错误行动语义解释试验。 | 不完全执行、测量或制度同步改变 | 与前不依从例呼应，未提供未经条件的识别。 | 已清楚；无。 |
| B10-231 环境标签E与条件机制稳定 | 1656–1660，“只改变输入X的分布”；`sec:causal-interventional-structure` | 用多环境限制候选方向。 | P(Y\|X,E)共同支持稳定、反向可变 | 独立噪声和机制不变是输入假设，不是观测稳定自动证明。 | 已清楚；无。 |
| B10-232 环境方向线索的失败边界 | 1662–1670，“共同原因…稳定…变化太弱”；`sec:causal-interventional-structure` | 防止不变预测直接被读作因果发现。 | 同步选择、反馈、时变机制 | 扩展动态／循环模型为边界预告。 | 已清楚；无。 |

## 局部机制推断与本章小结

节标签：`sec:causal-local-mechanism-inference`、`sec:causal-inference-summary`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B10-233 局部机制推断 | 1675–1678，“作用大小…形状和背景分布”；`sec:causal-local-mechanism-inference` | 图已知仍缺响应数值。 | 第8章参数／函数估计回指 | 先声明干预含义，不能只拟合条件关系。 | 已清楚；无。 |
| B10-234 局部线性结构与条件零均值 | 1680–1685，“E[ε_j\|P_j]=0”；`sec:causal-local-mechanism-inference` | 给可以用矩恢复局部参数的具体模型。 | 截距与父变量线性组合 | 比只说噪声均值零更强，条件明确。 | 已清楚；无。 |
| B10-235 增广父向量Z_j | 1686–1687，“(1,P_jᵀ)ᵀ”；`sec:causal-local-mechanism-inference` | 把截距并入同一矩方程。 | 参数向量ϑ_j对应排列 | 第8章线性回归已回顾，维度可跟随。 | 已清楚；无。 |
| B10-236 总体Gram矩Q_j | 1688–1689，“E[Z_jZ_jᵀ]可逆”；`sec:causal-local-mechanism-inference` | 防止不同局部系数无法区分。 | 条件二阶矩有限 | 确定性共线时失去唯一，非图有边就可识别系数。 | 已清楚；无。 |
| B10-237 局部参数矩识别 | 1689–1696，“乘以…再取期望”；`sec:causal-local-mechanism-inference` | 从零条件残差均值推可观测公式。 | `ϑ=Q⁻¹E[ZV]` | 第8章总体线性投影工具足够；结构假设赋因果语义。 | 已清楚；无。 |
| B10-238 局部样本矩估计 | 1696–1705，“前提是样本矩可逆”；`sec:causal-local-mechanism-inference` | 将总体参数式落到iid样本。 | 两个经验矩及求逆公式 | 总体可逆不保证每次样本可逆，正文未混同。 | 已清楚；无。 |
| B10-239 局部估计复合后的共同误差 | 1707–1710，“β̂+γ̂α̂”；`sec:causal-local-mechanism-inference` | 多方程估计后计算总响应。 | 培训总系数例 | 不能只报告β̂；共同样本协方差需传播。 | 已清楚；无。 |
| B10-240 条件核估计 | 1712–1713，“父变量支持上”；`sec:causal-local-mechanism-inference` | 非参数时先说明观测可估计对象。 | P(V_j\|pa_j) | 观测支持外尚无信息，非完整SCM。 | 已清楚；无。 |
| B10-241 稳定机制核解释 | 1713–1715，“正确关系、噪声及机制不变”；`sec:causal-local-mechanism-inference` | 将统计条件核赋予干预保持含义。 | 三层说明的第二层 | 拟合好不自动满足此层。 | 已清楚；无。 |
| B10-242 同背景输入配对的结构表示 | 1714–1718，“不同结构函数和背景耦合”；`sec:causal-local-mechanism-inference` | 个体反事实需要比局部核更强的信息。 | 两种跨世界配对准确回指 | 稳定边缘核也不唯一决定事实后反事实。 | 已清楚；无。 |
| B10-243 SCM重参数化不唯一 | 1720–1723，“相同…可观测与干预分布”；`sec:causal-local-mechanism-inference` | 避免承诺完整背景坐标可恢复。 | 前配对与参数语义对比 | 加性独立噪声、形状、平滑都须列为候选限制。 | 已清楚；无。 |
| B10-244 候选结构集合的响应传播 | 1725–1729，“逐一生成…识别集合”；`sec:causal-local-mechanism-inference` | 把关系、函数、背景三类歧义传到最终目标。 | 候选(G,{f_j},P_U)接口 | 各模型拟合相容不应只挑一个掩盖差异。 | 已清楚；无。 |
| B10-245 小结的开篇回应 | 1734–1737，“两组成绩差…不同背景”；`sec:causal-inference-summary` | 回答培训关联为何不足。 | 自然条件化与规则替换重收拢 | 不引入新数学对象，未用口号代替结论。 | 收束完整；无。 |
| B10-246 小结的效应口径 | 1739–1743，“个体…ATE…CATE…局部”；`sec:causal-inference-summary` | 回顾各比较丢失的信息及补救目标。 | 分布边缘不定跨世界联合 | 已定义概念回顾，不合并它们的含义。 | 已清楚；无。 |
| B10-247 小结的识别条件 | 1745–1749，“后门…不能代替目标支持”；`sec:causal-inference-summary` | 将表示、交换、支持、图证书各作用接齐。 | 调整／逆概率同目标 | 不把充分准则写成必要条件。 | 已清楚；无。 |
| B10-248 小结的三类不确定性 | 1751–1756，“机制歧义…有限样本…数值”；`sec:causal-inference-summary` | 总结改善每类误差需要改变什么。 | 增样本、行动覆盖、限制目标分别解释 | 有效包络／锐界区分保留。 | 已清楚；无。 |
| B10-249 小结的结构边界 | 1758–1762，“通常止于Markov等价类”；`sec:causal-inference-summary` | 回收给定图、发现图、推断函数的层次。 | Markov正向／忠实反向及反事实不足 | 无新增先用后定义对象。 | 已清楚；无。 |
| B10-250 后续章节接口 | 1764–1770，“图…计算工具…序贯价值”；`sec:causal-inference-summary` | 明确图、动态策略、公平应用如何继续使用本章。 | 准确章节标签 | 纯前指；图工具不自行提供因果语义。 | 已清楚；无。 |
