# 第11章概念审读清单（独立读者B，第一轮）

## 版本与覆盖

- 源文件：`tex/01-mathematical-preliminaries/04-graphs-and-signals/01-graph-structure-and-computation.tex`。
- 冻结 SHA-256：`7966f2c47a69b32996f180e78dbfdeb6f734b280e68f4d6184ce559ac1b74c72`，本章开始前与冻结清单复核一致。
- 已连续完整顺读1–2551／2551行、71727源字符。读取块为1–220、221–440、441–660、661–880、881–1100、1101–1320、1321–1540、1541–1760、1761–1820、1821–1826、1827–1833、1834–2053、2054–2273、2274–2493、2494–2551；块内证明、算例、图注与表均未跳过。
- 概念清单434项，覆盖全章。本章实质问题R1-B-041、042、043三项：技术疑点2项，局部费力1项；无阻断理解项。此处完成的是冻结版首轮独立审读，不表示修订后复读通过。
- 表前节标签与本章路径共同适用于各行；首次位置为实际行号和短引文。纯预告单列，熟悉概念也记录回顾。图仅核对说明、节点与关系，不作正式PDF视觉验收。

## 已核对的边界依赖

路径以`tex/01-mathematical-preliminaries/`为前缀，以下均实际展开。

| 前章文件 | 实读范围 | 用途与结论 |
| --- | --- | --- |
| `01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex` | 108–164、774–838 | 二元关系、等价关系及划分证明、偏序／全序；赋值、文字、子句、CNF与贯穿四变量公式。准确核对图的五条边来自四个子句作用域，不是猜测其前文含义。774从赋值定义正文起，838到下一公式结尾，不声称额外逻辑节完整审读。 |
| `01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex` | 1–50、870–945 | 四变量选择语义、基本计数；硬约束、SAT／搜索／验证、子句数值化和完整四变量约束。945止于软约束公式结尾，不作为其后节完整核对。 |
| `02-linear-algebra-and-geometry/01-linear-algebra-and-matrix-analysis.tex` | 419–456、1435–1498、1518–1535 | 相似换基式、特征值与代数／几何重数、特征多项式、Cayley–Hamilton全证明、对角化与一般相似／酉相似区别。1497–1498仅触及Schur定理开头，1535仅触及Jordan块说明，均不视作这两项完整核查。当前同构谱论证只需已展开的相似与特征值知识。 |
| `01-mathematical-language-combinatorics-analysis-optimization/03-mathematical-analysis.tex` | 718–758 | 核对722–753行的紧致性、有限维闭有界刻画和连续极值定理，足以支撑最大流存在性；边界两端的连续性语句也读过，不声称完整补读其邻节。 |
| `01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex` | 929–1025、1025–1105、1106–1146 | 离散实值最优存在、软代价、近似口径、次模边际与交并等价定义及1103–1120全证明。四项二值不等式正是交并式的两元素情形。1146止于覆盖函数证明中段，该旁支不作为已核查完整证明。 |
| `01-mathematical-language-combinatorics-analysis-optimization/04-optimization.tex` | 1409–1504 | 拉格朗日函数、驻点、等式乘子、LICQ与必要性证明；当前归一化割的两个约束可据正度及加权平衡辨认，谱展开另保证全局最优。 |
| `02-linear-algebra-and-geometry/01-linear-algebra-and-matrix-analysis.tex` | 312–348、1568–1615、2060–2200、2836–2944 | 核对加权正定内积／半内积，自伴谱定理全证明，Rayleigh商及极值、迹最小化、正定广义特征问题，谱隙与重特征子空间稳定性。348只触及投影开头，2197–2200只触及截断SVD开头，2941–2944只触及非自伴扰动式，均不当作该旁支完整核验。2836–2840为前段证明末尾；当前只回用2842–2939已展开的自伴稳定性。 |

为判定实现术语入口，另在第1–10章实际检索“二叉堆／优先队列／并查集”，未见定义；不以这项检索代替第11章逐段顺读。

最后两节补读：第6章736–773、1613–1670行，核对矩阵多项式、指数幂级数、谱函数对重特征空间的同标量作用及线性ODE指数解；736–737与773仅是相邻内容边界，不称几何级数部分完整核验。第3章1719–1805行核对乘积测度、Tonelli／Fubini准确声明、证明范围及行列求和反例，1805仅触及下一例开头。第7章连续Dirichlet能量与流形图离散化所需概念已完整顺读，无须借用本章之后的信号分析。

第7–10章已完整順读；第7章置换作用、第8章条件独立、第10章d-分离、Markov性、忠实性和等价类均可准确回用。当前未读的本章后文不用于补齐当前位置条件。

另读取图源：`figures/math-preparation/reader-revision-graph/factor-scope.tex`1–17、`ancestor-moral-query.tex`1–22、`figures/math-preparation/reading-restructure/ch11/active-paths.tex`1–34。三图节点、箭头及标注与当前正文一致；公共样式文件不涉及新概念，未据此作排版验收。

## 图对象与作用域

节标签：`chap:graph-theory`、`sec:graph-theory-objects-representations`、`sec:graph-theory-local-relations`、`sec:graph-theory-binary-relations`、`sec:graph-theory-higher-order-scopes`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-001 四二值变量与CNF | 11–17，“四个二值变量”；`chap:graph-theory` | 给全章固定可核算的离散对象。 | `eq:comb-running-cnf`已实读及当前四项解释 | 第1、2章变量／规则已回顾，不预设全部赋值可行。 | 已清楚；无。 |
| B11-002 作用域导出的关系图 | 18–25，“共同出现…每一对…连接”；`chap:graph-theory` | 把局部约束之间的联系压缩为边。 | `eq:graph-theory-running-edges`、完整内嵌图及图注 | 边不记录真值表；三元约束不等价于三个二元约束。 | 已清楚；无。 |
| B11-003 共享变量接口 | 23–25，“固定这两个变量以后”；`chap:graph-theory` | 预告如何将左右计算分开。 | 两三角共享{2,3} | 只先解释局部计算；未冒称概率独立。 | 预告清楚；无。 |
| B11-004 顶点函数与配置函数 | 52–54，“两种定义域”；`chap:graph-theory` | 为谱运算与精确查询预留根本区别。 | 每顶点一个数／每完整赋值一个数 | 后文正式展开，这里只预告。 | 预告清楚；无。 |
| B11-005 有限无向简单图 | 69–73，“不同顶点的无序对”；`sec:graph-theory-binary-relations` | 定义一条边记录什么。 | G=(V,E)、贯穿五条边 | 默认无自环和平行边，不能忽略此限制。 | 已清楚；无。 |
| B11-006 自环与平行边边界 | 72–73，“身份及重数”；`sec:graph-theory-binary-relations` | 防止拓展多重图时仍用普通边集合。 | 同一对顶点多边的保存说明 | 此处边界预告，后DFS另说明按边身份跳父边。 | 已清楚；无。 |
| B11-007 相邻与邻居 | 75，“{i,j}∈E”；`sec:graph-theory-binary-relations` | 规定一步关系。 | 顶点1与2 | 不等于经其他顶点可达。 | 已清楚；无。 |
| B11-008 邻域N(i) | 76–80，“全部邻居”；`sec:graph-theory-binary-relations` | 为局部检索和汇总给集合接口。 | N(2)={1,3,4} | 未含自身的开邻域，简单图条件下明确。 | 已清楚；无。 |
| B11-009 度d_i | 77–82，“邻居的数量”；`sec:graph-theory-binary-relations` | 衡量直接连接规模。 | d₂=3、d₁=2 | 不统计所有可达顶点，也不是权重和。 | 已清楚；无。 |
| B11-010 有向图与弧 | 84–86，“有序对…不自动包含反向”；`sec:graph-theory-binary-relations` | 保存有方向的作用或通行。 | i→j | 一般弧无自动因果意义，与第10章SCM分开。 | 已清楚；无。 |
| B11-011 入邻域N⁻ | 87，“指向本点”；`sec:graph-theory-binary-relations` | 读取直接前驱。 | N⁻(j)={i:i→j} | 因果父点是此对象的特例。 | 已清楚；无。 |
| B11-012 出邻域N⁺ | 87–88，“从本点指出”；`sec:graph-theory-binary-relations` | 读取可沿弧前往的邻居。 | N⁺(j)={i:j→i} | 不与入邻域混用。 | 已清楚；无。 |
| B11-013 入度 | 88–89，“它们的大小”；`sec:graph-theory-binary-relations` | 计数直接前驱，为后拓扑排序准备。 | 入邻域基数 | 与无向度不同，有向两方向可能不等。 | 已清楚；无。 |
| B11-014 出度 | 88–89，“出度”；`sec:graph-theory-binary-relations` | 计数直接后继。 | 出邻域基数 | 不代表多步后代数。 | 已清楚；无。 |
| B11-015 边权重 | 93–95，“每条边附带的数值”；`sec:graph-theory-binary-relations` | 将结构与数值任务分开。 | 对称无向权、有向可不同 | 加权／方向是可组合属性，不是互斥类别。 | 已清楚；无。 |
| B11-016 边长 | 96，“成本越高”；`sec:graph-theory-binary-relations` | 给路径选择定义代价语义。 | 后两步比一步短的例 | 不能直接当相似度。 | 已清楚；无。 |
| B11-017 容量 | 96，“允许通过的总量”；`sec:graph-theory-binary-relations` | 为流量约束区分数值含义。 | 246–250零容量解释 | 纯任务预告，未使用未定义流量方程。 | 预告清楚；无。 |
| B11-018 相似度权重 | 97，“越大…越接近”；`sec:graph-theory-binary-relations` | 为图平滑解释相反于边长的作用。 | 零相似度不贡献差分 | 不自动删除结构边。 | 已清楚；无。 |
| B11-019 正权支撑E₊ | 99–106，“w_i,j>0”；`sec:graph-theory-binary-relations` | 谱／扩散只沿正权发生耦合。 | 零权单边例、G₊ | 结构相邻与数值贡献分开。 | 已清楚；无。 |
| B11-020 诱导子图 | 108–112，“两端…全部边”；`sec:graph-theory-binary-relations` | 研究部分顶点而不悄悄删边。 | {1,2,3}必须留三边 | 一般子图不必保留全部，反例具体。 | 已清楚；无。 |
| B11-021 因子 | 117–118，“这种局部函数”；`sec:graph-theory-higher-order-scopes` | 保存约束的数值／真假功能。 | 三元子句 | 不等于图上边或方框图形本身。 | 已清楚；无。 |
| B11-022 作用域 | 118，“依赖的变量集合”；`sec:graph-theory-higher-order-scopes` | 指明因子需要同时查看哪些变量。 | {2,3,4} | 不由所有两两关系唯一恢复因子身份。 | 已清楚；无。 |
| B11-023 超图 | 119–121，“共同属于同一个因子”；`sec:graph-theory-higher-order-scopes` | 保存多元关系而不限二元边。 | 三元作用域 | 超图仍不存函数真值表。 | 已清楚；无。 |
| B11-024 超边 | 120，“一个顶点子集”；`sec:graph-theory-higher-order-scopes` | 表示单项高阶关系的变量集合。 | 超边{2,3,4} | 不限两个端点，区别普通边。 | 已清楚；无。 |
| B11-025 二部图 | 123–125，“两组顶点内部都没有边”；`sec:graph-theory-higher-order-scopes` | 为变量／因子双类型表示准备。 | 变量组与因子组 | 一般二部图两组不一定恰是这两类。 | 已清楚；无。 |
| B11-026 因子图 | 125，“方形…因子…圆形…变量”；`sec:graph-theory-higher-order-scopes` | 同时保留因子身份与作用域归属。 | `fig:graph-theory-factor-scope`及图源全读 | 连接表示归属，不等于变量间直接作用。 | 已清楚；无。 |
| B11-027 原始关系图 | 126–128，“作用域内…两两相连”；`sec:graph-theory-higher-order-scopes` | 将因子计算的相互依赖压缩为变量图。 | 贯穿图及右侧三角形 | 会丢因子分组和函数值，非等价因子分解。 | 已清楚；无。 |
| B11-028 三元奇偶约束的不可二元恢复 | 130–135，“错误地允许001”；`sec:graph-theory-higher-order-scopes` | 给丢失高阶约束的可核查反例。 | 000,011,101,110及全部二元投影 | 基础组合已足，图同不代表函数族同。 | 已清楚；无。 |

## 矩阵表示与同构

节标签：`sec:graph-theory-matrix-representations`、`sec:graph-theory-graph-isomorphism`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-029 邻接表 | 149–152，“存实际邻居及…属性”；`sec:graph-theory-matrix-representations` | 支持局部遍历且不为无边留稠密槽。 | O(V+E)、无向存两次为常数 | 第2章复杂度记号已回顾；不同于邻接矩阵。 | 已清楚；无。 |
| B11-030 邻接矩阵A | 154–177，“行是起点、列是终点”；`sec:graph-theory-matrix-representations` | 用线性代数保存边权。 | `eq:graph-theory-running-adjacency` | 无权用1，零权与无边需额外掩码。 | 已清楚；无。 |
| B11-031 出邻居汇总Af | 164、178–180，“汇总出邻居的值”；`sec:graph-theory-matrix-representations` | 把矩阵方向约定接到运算。 | f=(1,2,3,4)得(5,8,7,5) | 非在全部变量配置求和，定义域不同。 | 已清楚；无。 |
| B11-032 沿出弧发送Aᵀf | 165–166，“发送到终点”；`sec:graph-theory-matrix-representations` | 解释为什么传播方向可能需要转置。 | 行起点的索引求和 | 无向对称时才与Af重合。 | 已清楚；无。 |
| B11-033 结构掩码M | 181–182，“存在相应结构边”；`sec:graph-theory-matrix-representations` | 保存数值0无法区分的结构信息。 | m_i,j指示式、空图对零权单边 | 与权重矩阵不是同一对象。 | 已清楚；无。 |
| B11-034 关联矩阵B | 184–188，“任选临时方向”；`sec:graph-theory-matrix-representations` | 逐边保存端点差。 | 起点+1、终点-1，Bᵀf=f_i-f_j | 临时定向不把无向图变成因果或通行有向图。 | 已清楚；无。 |
| B11-035 加权差分B W_E Bᵀ | 189–190，“求边差…缩放…汇总”；`sec:graph-theory-matrix-representations` | 将局部差分拼成顶点算子。 | 对角W_E定义 | 暂未命名Laplacian，后再建立性质。 | 已清楚；无。 |
| B11-036 临时方向反转不变性 | 191–194，“R W_E R=W_E”；`sec:graph-theory-matrix-representations` | 保证无向算子与任选方向无关。 | B'=BR，R对角±1 | 不能推真实有向图方向无关。 | 证明清楚；无。 |
| B11-037 图同构 | 199–208，“忽略顶点名称…完全相同”；`sec:graph-theory-graph-isomorphism` | 区分结构与编号。 | 双射ρ保邻接充要条件 | 有向、权重、属性各须保留对应信息。 | 已清楚；无。 |
| B11-038 置换矩阵与置换共轭 | 209–214，“只挪动坐标位置”；`sec:graph-theory-graph-isomorphism` | 将重编号写成矩阵关系。 | `eq:graph-theory-adjacency-relabel` | 第7章置换已读，Pᵀ为逆。 | 已清楚；无。 |
| B11-039 一般相似与图重编号 | 215–222，“允许混合坐标”；`sec:graph-theory-graph-isomorphism` | 防止把任意换基当同构。 | 第6章相似式实读、结构掩码同时变换 | 零权边例说明A本身未必够。 | 已清楚；无。 |
| B11-040 邻接谱 | 224，“相同邻接谱”；`sec:graph-theory-graph-isomorphism` | 给同构的必要数值不变量。 | 相似保持特征值 | 第6章特征值／重数已实读，不称任意算子的谱。 | 已清楚；无。 |
| B11-041 同谱不同构 | 225–229，“四叶星…四环加…孤立顶点”；`sec:graph-theory-graph-isomorphism` | 显示谱不保完整结构。 | 两谱均2,-2,0,0,0 | 一图连通另一不连通，星与环形状名称足够辨认。 | 已清楚；可选给5×5矩阵便于验算，非必需。 |

## 路径、可达与树

节标签：`sec:graph-theory-paths-traversal`、`sec:graph-theory-active-paths`；未单独标标签的小节沿用其最近有标签的父节。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-042 游走／行走 | 257–258，“允许重复顶点和边”；`sec:graph-theory-paths-traversal` | 将单步连接扩成任意多步。 | 1,2,3,1,2 | 不等于简单路径。 | 已清楚；无。 |
| B11-043 简单路径 | 259–260，“顶点两两不同”；`sec:graph-theory-paths-traversal` | 排除重复以表达基本连接路线。 | 1,2,4 | 本章默认路径简单，与第10章一致。 | 已清楚；无。 |
| B11-044 边数长度与零步路径 | 260，“单个顶点…长度为零”；`sec:graph-theory-paths-traversal` | 确定距离基准并保证自身可达。 | k条边、后A⁰=I | 不等于权重和。 | 已清楚；无。 |
| B11-045 无向环 | 261–263，“k≥3…除首尾互异”；`sec:graph-theory-paths-traversal` | 区分回到原点与真正简单环。 | 1,2,3,1 | 无向单边往返不是环。 | 已清楚；无。 |
| B11-046 有向行走与有向路径 | 265，“每一步…沿弧”；`sec:graph-theory-paths-traversal` | 指定带方向的可达。 | 顺弧序列 | 用不用重复沿用游走／路径区分。 | 已清楚；无。 |
| B11-047 有向环 | 266–268，“可短至两条弧”；`sec:graph-theory-paths-traversal` | 给DAG判据明确环口径。 | i→j→i | 与无向环最短长度不同。 | 已清楚；无。 |
| B11-048 DAG | 268–271，“忽略方向后…不要求无环”；`sec:graph-theory-paths-traversal` | 回顾第10章无环依赖对象。 | 1→2、1→3、2→3 | 底层三角形仍可DAG。 | 已清楚；无。 |
| B11-049 邻接幂的游走计数 | 273–280，“按倒数第二个顶点分类”；`sec:graph-theory-paths-traversal` | 用矩阵乘法检索固定步数路线。 | A⁰基例、A^(k+1)归纳式 | 不自动排除重复；证明可跟随。 | 已清楚；无。 |
| B11-050 加权邻接幂的贡献和 | 281–286，“权重乘积之和”；`sec:graph-theory-paths-traversal` | 明确加权时矩阵幂计算的对象。 | 对路线求和、沿边权重相乘 | 非路线条数，更非边长加和。 | 已清楚；无。 |
| B11-051 布尔矩阵运算 | 287–288，“可达性”；`sec:graph-theory-paths-traversal` | 预告换运算规则可换查询语义。 | 无详细公式 | 纯运算扩展预告，不据此要求实现算法。 | 预告清楚；无。 |
| B11-052 最小加法运算 | 287–288，“固定步数的最低成本”；`sec:graph-theory-paths-traversal` | 预告后距离递推与普通矩阵乘法不同。 | 无正式代数定义 | 纯预告，后续实际使用时须再核对定义。 | 暂不作为已建立工具。 |
| B11-053 活跃路径规则回顾 | 293–298，“每个非碰撞…每个碰撞”；`sec:graph-theory-active-paths` | 从沿箭头可达转为条件分离。 | 第10章`def:causal-d-separation` | 已完整读，当前准确复述。 | 已清楚；无。 |
| B11-054 碰撞后代打开路径 | 300–305，“条件点甚至不在路径上”；`sec:graph-theory-active-paths` | 强化路径角色与全图后代的区别。 | a→c←b、c→d三条件集 | 与链／分叉给定中间点相反。 | 已清楚；无。 |
| B11-055 活跃性与删除节点连通性 | 306–319，“不是简单删除条件顶点”；`sec:graph-theory-active-paths` | 避免对有向条件查询误用无向遍历。 | `fig:graph-theory-active-paths`全图源及图注 | 图判据仍需模型假设才对应概率独立。 | 已清楚；无。 |
| B11-056 路径代价ℓ(P) | 323–327，“边…长度或代价”；`sec:graph-theory-paths-traversal` | 将最短任务的数值对象固定为边长和。 | 显式Σℓ | 与相似度及矩阵幂贡献不同。 | 已清楚；无。 |
| B11-057 最短路径 | 328–330，“使此和最小”；`sec:graph-theory-paths-traversal` | 选择总代价最小的简单路径。 | 直边5对两边各1 | 无权才等于最少边数。 | 已清楚；无。 |
| B11-058 简单路径与行走的最优值 | 332–338，“有限…无限”；`sec:graph-theory-paths-traversal` | 说明负环时两个优化任务会分开。 | 删去非负闭合段论证 | 可达的简单路径有限，所以仍有最小值。 | 已清楚；无。 |
| B11-059 可影响目标的负闭行走 | 334–336，“可从s到达…继续到t”；`sec:graph-theory-paths-traversal` | 给行走下确界-∞精确条件。 | 重复负段可任意降低 | 不声称存在长度-∞的简单路径；需与s,t相关。 | 已清楚；无。 |
| B11-060 无向负边往返 | 336–338，“即使…不在…简单环”；`sec:graph-theory-paths-traversal` | 防止将有向负环条件生搬到无向图。 | 单负边往返一次负闭行走 | 闭行走和简单环已区分，说明准确。 | 已清楚；无。 |
| B11-061 无向可达 | 344，“存在路径”；`sec:graph-theory-paths-traversal` | 从直接邻接拓展到多步联系。 | 贯穿1与4 | 允许零步保证自反。 | 已清楚；无。 |
| B11-062 连通分量 | 344–347，“分量内部…不同分量…没有路径”；`sec:graph-theory-paths-traversal` | 按可达划分顶点。 | 删除边后替代路径例 | 第1章等价类已实读，不只是任意分组。 | 已清楚；无。 |
| B11-063 可达等价关系证明 | 346–347，“拼接…删去重复段”；`sec:graph-theory-paths-traversal` | 保证分量唯一划分。 | 自反、反向对称、拼接传递 | 第1章108–164具备完整入口。 | 已清楚；无。 |
| B11-064 无向连通 | 348–352，“一个分量的非空…图”；`sec:graph-theory-paths-traversal` | 指定整体连接性质及空图边界。 | 删{1,2}仍由1-3-2相连 | 删环边不一定断图。 | 已清楚；无。 |
| B11-065 有向祖先与后代 | 356–360，“其他顶点…不含自身”；`sec:graph-theory-paths-traversal` | 回顾正长度有向可达。 | 有环时可互为祖先 | 祖先闭包后显式加自身，避免约定漂移。 | 已清楚；无。 |
| B11-066 强连通 | 362–363，“任意有序顶点对”；`sec:graph-theory-paths-traversal` | 要求方向上彼此都能到达。 | 对比1→2→3 | 非忽略箭头的连通。 | 已清楚；无。 |
| B11-067 强连通分量 | 363，“互相可达的极大…集合”；`sec:graph-theory-paths-traversal` | 分组互相通信的有向区域。 | 链的三个单顶点分量 | “极大”意为不能扩充，不要求全图最大基数。 | 已清楚；无。 |
| B11-068 弱连通 | 364–367，“忽略弧方向”；`sec:graph-theory-paths-traversal` | 保留更弱的连接判断。 | 链弱连通但不强连通 | 不回答能否双向传递。 | 已清楚；无。 |
| B11-069 树 | 371–373，“连通且无环”；`sec:graph-theory-paths-traversal` | 为唯一接口传递建立结构。 | 随后树等价定理 | 指无向树，非任意画成分叉的图。 | 已清楚；无。 |
| B11-070 森林 | 371，“若干互不相连的树”；`sec:graph-theory-paths-traversal` | 允许多个无环连通块。 | 树的集合描述 | 不自动连通。 | 已清楚；无。 |
| B11-071 树的唯一路径刻画 | 375–388，“恰有一条简单路径”；`sec:graph-theory-paths-traversal` | 解释树为何没有循环重复返回。 | `thm:graph-theory-tree-characterizations`、两路分叉形成环证明 | 单顶点零步路径也纳入。 | 已清楚；无。 |
| B11-072 树的n-1边刻画 | 381、390–400，“连通…恰有n-1条边”；`sec:graph-theory-paths-traversal` | 给可计算的结构证书。 | 叶删归纳及逐点接入证明 | 三角加孤点说明只数边不够。 | 已清楚；无。 |
| B11-073 叶顶点 | 390–394，“度为1”；`sec:graph-theory-paths-traversal` | 作为树归纳证明的删除对象。 | 最长简单路径端点证明 | 限至少两顶点有限树，单点单独处理。 | 已清楚；无。 |
| B11-074 生成树抽取预告 | 396–404，“覆盖全部顶点…舍弃其他边”；`sec:graph-theory-paths-traversal` | 在证明中给出连通图取树构造。 | 每步接入未加入顶点、不成环 | 后文正式命名；当前只保证连通，不保证所有查询。 | 预告清楚；无。 |

## 遍历与拓扑次序

节标签：`sec:graph-theory-bfs`、`sec:graph-theory-dfs`、`sec:graph-theory-topological-order`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-075 广度优先搜索BFS | 411–415，“先查一跳…再查两跳”；`sec:graph-theory-bfs` | 列出起点可达区域并分层。 | 初始化、出队、邻居扫描完整规则 | 有向只扫描出邻居。 | 已清楚；无。 |
| B11-076 先进先出队列 | 412–415，“每次取出队首”；`sec:graph-theory-bfs` | 保存按发现时间处理的次序。 | 入队／出队叙述 | 与后DFS后进先出栈不同。 | 白话足够；无。 |
| B11-077 入队即标记 | 413–416，“防止…重复入队”；`sec:graph-theory-bfs` | 保证遍历不重复及复杂度。 | 两个已发现点可共享邻居 | 不延迟到出队，操作时点明确。 | 已清楚；无。 |
| B11-078 BFS层数d(v) | 413–415，“d(u)+1”；`sec:graph-theory-bfs` | 保存发现路径的边数。 | 427–429层{1},{2,3},{4} | 稍后证明才得到最短，不先靠直觉断言。 | 已清楚；无。 |
| B11-079 父指针与搜索树 | 415、420–422，“指向较早发现”；`sec:graph-theory-bfs` | 恢复具体路径。 | 回溯父边且不会成环 | 不保留原图全部边，父亲可不唯一。 | 已清楚；无。 |
| B11-080 BFS邻接表成本 | 418–419，“每点…每边…常数次”；`sec:graph-theory-bfs` | 从具体操作数得到资源界。 | O(V+E)及来源 | 与稠密矩阵扫描成本不同，表示条件明确。 | 已清楚；无。 |
| B11-081 BFS最少边数证明 | 424–429，“倒数第二个顶点…更早”；`sec:graph-theory-bfs` | 证明第一次发现的层数最优。 | 按层归纳和更短路径矛盾 | 不推广为任意权重最短路。 | 已清楚；无。 |
| B11-082 深度优先搜索DFS | 434–439，“持续深入…回退”；`sec:graph-theory-dfs` | 检索路径结构及完成次序。 | 未探索邻居与重启规则 | 无向重启可求分量，有向不能直接求SCC。 | 已清楚；无。 |
| B11-083 递归／显式栈 | 435，“保存尚未完成的路径”；`sec:graph-theory-dfs` | 记录当前搜索分支及返回位置。 | 深入与回退的说明 | 与BFS队列不同，不需预设具体语言递归实现。 | 已清楚；无。 |
| B11-084 DFS三色状态 | 436，“未发现、在栈内、已完成”；`sec:graph-theory-dfs` | 区分回到当前祖先与访问已完成分支。 | 判环后续使用 | 单一visited不足代替这三个状态。 | 已清楚；无。 |
| B11-085 回边 | 441–445，“指向当前栈内顶点”；`sec:graph-theory-dfs` | 从弧构造有向环证书。 | 栈路径加u→v | 指向已完成点不是环证据。 | 已清楚；无。 |
| B11-086 有向DFS回边充要性 | 443–445，“完成先后…循环矛盾”；`sec:graph-theory-dfs` | 保证不是仅找到环的充分方法。 | 首发现环点与完成序论证 | 全部可达区域完成前必有回边，条件可跟随。 | 已清楚；无。 |
| B11-087 无向DFS父边排除 | 447–450，“不能把返回父顶点…当成环”；`sec:graph-theory-dfs` | 避免同条边双向存储造成假环。 | 非父边加树路径至少三边 | 多重图须按边身份，当前简单图假设明确。 | 已清楚；无。 |
| B11-088 逆完成次序 | 452–455，“晚完成者指向…早完成者”；`sec:graph-theory-dfs` | 从DFS构造满足依赖的处理序。 | 未发现／已完成／在栈内三情况完整覆盖 | 仅无回边时成立。 | 已清楚；无。 |
| B11-089 拓扑序 | 460–467，“每条弧起点先于终点”；`sec:graph-theory-topological-order` | 将依赖图排成可执行线性顺序。 | `thm:graph-theory-topological-order` | 不是只看相邻名次；可达也产生先后限制。 | 已清楚；无。 |
| B11-090 可达偏序与线性扩展 | 461，“偏序扩展为线性次序”；`sec:graph-theory-topological-order` | 对接第1章排序语言。 | DAG不可互达及零步自反 | 第1章偏序定义已实际展开。 | 已清楚；无。 |
| B11-091 DAG与拓扑序等价 | 470–479，“有环…次序循环…零入度”；`sec:graph-theory-topological-order` | 给存在性的双向证据。 | 环矛盾、反向追溯有限重复、逐点删除 | 不预设已知排序算法定理。 | 完整证明；无。 |
| B11-092 零入度队列算法 | 474–479，“维护新产生的零入度”；`sec:graph-theory-topological-order` | 将存在性证明变成线性成本程序。 | 删除点和出弧、更新入度 | 与DFS方法存在条件相同但输出可不同。 | 已清楚；无。 |
| B11-093 拓扑序中不可比点的交换 | 481–483，“互相不可达…可以交换”；`sec:graph-theory-topological-order` | 用局部自由度解释不唯一性。 | 当前无例子限定交换位置 | 非相邻两位置交换可跨越第三点的依赖。 | 技术疑点R1-B-041；加“在序列中相邻”或改述存在不同相对次序。 |

## 分隔与祖先道德化

节标签：`sec:graph-theory-traversal-separation-decomposition`、`sec:graph-theory-separators`、`sec:graph-theory-conditional-separation`、`sec:graph-theory-directed-transformations`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-094 无向分隔集S | 501–503，“每条…路径都经过S”；`sec:graph-theory-separators` | 给局部分块定义接口。 | 删除S后分量不横跨A,B | 三集两两不交，A,B非空；与DAG活跃规则不同。 | 已清楚；无。 |
| B11-095 接口加回的局部块 | 504–509，“G[C_r∪S]”；`sec:graph-theory-separators` | 分块时保留与外界相接变量。 | {1,2,3}和{2,3,4} | 块允许重叠，不是简单把S丢弃。 | 已清楚；无。 |
| B11-096 接口因子唯一归属 | 510–511，“不能…重复计入”；`sec:graph-theory-separators` | 防止两个袋共享作用域导致权重或约束重复。 | 贯穿图接口因子 | 图组织不自动是概率条件独立。 | 已清楚；无。 |
| B11-097 割点 | 513–516，“分量数增加”；`sec:graph-theory-separators` | 衡量单节点删除是否破坏连接。 | 贯穿删各点仍连通 | 无割点仍可能有两点分隔。 | 已清楚；无。 |
| B11-098 桥 | 513–517，“删除一条边”；`sec:graph-theory-separators` | 给单边连接故障结构证书。 | 每边处三角、有替代路径 | 与权重大小无关。 | 已清楚；无。 |
| B11-099 分离关系集合I(G) | 519–522，“元素…(A,B\|S)”；`sec:graph-theory-separators` | 比较不同图给出的全部图查询答案。 | 无向分隔／DAG d-分离两口径 | 不包含尚未指定的分布模型。 | 已清楚；无。 |
| B11-100 分离关系中的邻接判据 | 524–544，“不存在S…分离”；`sec:graph-theory-separators` | 说明全部分离足以恢复骨架。 | `lem:graph-theory-separation-adjacency`及双图完整证明 | DAG父集证法回顾第10章，不保证方向唯一。 | 已清楚；无。 |
| B11-101 单路径与全图查询 | 552–560，“找到一条…不足以肯定分离”；`sec:graph-theory-conditional-separation` | 阻止只检查局部碰撞就下全图结论。 | a-c-b旁加a-e-b | 无向条件增大会删路径，DAG可能打开路径。 | 已清楚；无。 |
| B11-102 骨架skel(G) | 571–573，“i→j或j→i存在”；`sec:graph-theory-directed-transformations` | 为忽略方向后的图操作固定记号。 | 与第10章骨架定义一致 | 不添加共同父节点边。 | 已回顾；无。 |
| B11-103 祖先闭包An_G(U) | 574–579，“显式包含U本身”；`sec:graph-theory-directed-transformations` | 按当前查询保留可能影响端点和条件的变量。 | 明确集合式 | 不同于此前不含自身的祖先用语。 | 已清楚；无。 |
| B11-104 诱导祖先图 | 580–582，“G[An_G(U)]”；`sec:graph-theory-directed-transformations` | 只保留查询相关祖先及其所有原有弧。 | 597–600碰撞例 | 诱导子图已定义，不随意删内部边。 | 已清楚；无。 |
| B11-105 父集与an⁺记号 | 584–586，“父集只走一步”；`sec:graph-theory-directed-transformations` | 避免直接前驱与所有祖先混淆。 | pa=N⁻、an⁺=An_G | 一个局部，一个递归且含自身。 | 已清楚；无。 |
| B11-106 道德图mor(G) | 588–592，“任意两个不同父节点连…边”；`sec:graph-theory-directed-transformations` | 把共同子节点产生的路径联系转为无向边。 | 1→3←2补1-2 | 不等于原骨架。 | 已清楚；无。 |
| B11-107 道德化 | 591–592，“再去掉全部弧的方向”；`sec:graph-theory-directed-transformations` | 指明从DAG到道德图的操作顺序。 | 共同父连接再无向化 | 不是随意把所有祖先两两相连。 | 已清楚；无。 |
| B11-108 完美有向图 | 593–595，“每个父集…已两两相邻”；`sec:graph-theory-directed-transformations` | 定义不需要道德补边的特殊DAG。 | 加1→2后的三节点例 | 尚未将它与弦图等价，后文再核对。 | 已清楚；无。 |
| B11-109 祖先筛选与道德化次序 | 597–610，“不能先道德化整图”；`sec:graph-theory-directed-transformations` | 查询条件决定共同子点应否保留。 | `fig:graph-theory-ancestor-moral-query`、空S对S={3} | 补边是否出现依赖查询，非固定全图。 | 图和例完整；无。 |
| B11-110 祖先道德化判据 | 613–619，“当且仅当”；`sec:graph-theory-directed-transformations` | 将DAG分离转换成可遍历的无向分隔。 | `thm:graph-theory-ancestral-moralization` | 三集不交、非空端点、有限DAG明确。 | 已清楚；无。 |
| B11-111 活跃路径落在祖先图 | 622–625，“走到端点或碰撞点”；`sec:graph-theory-directed-transformations` | 证明裁掉非祖先不丢所需活跃路径。 | 碰撞为S祖先，非碰撞沿一侧走 | 每个点为何保留都有论证。 | 已清楚；无。 |
| B11-112 道德边绕过条件碰撞点 | 625–627，“用…u-v绕过”；`sec:graph-theory-directed-transformations` | 从活跃路径生成避S无向路径。 | 替换u→c←v并删重复段 | 非碰撞点本不在S，故绕过足够。 | 已清楚；无。 |
| B11-113 展开道德边的路线 | 629–634，“可能重复顶点，暂称路线”；`sec:graph-theory-directed-transformations` | 反向转换中不假定展开后已简单。 | 每补边展开共同子节点 | 与正式简单路径区分，后处理重复。 | 已清楚；无。 |
| B11-114 未打开碰撞位置的修复 | 636–643，“至少减少一个…不增加新的”；`sec:graph-theory-directed-transformations` | 解决共同子节点仅为端点祖先、不被S打开的问题。 | 沿到A或B有向路替换前缀／后缀 | 新段避S，接合处非碰撞，下降量说明终止。 | 已清楚；无。 |
| B11-115 最短活跃路线论证 | 645–648，“只有接合处…可能改变”；`sec:graph-theory-directed-transformations` | 将允许重复路线压成简单路径。 | 对重复v分是否在S两类 | 不草率认为删环自动保活跃。 | 已清楚；无。 |
| B11-116 接合新碰撞风险的排除 | 648–654，“后代…属于an⁺(S)”；`sec:graph-theory-directed-transformations` | 完成反向证明中最易漏的一步。 | 被删段首方向反转构成后代碰撞，推出v也被打开 | 端点重复另截断，证明覆盖边界。 | 已清楚；无。 |
| B11-117 查询图与统一无向图 | 657–658，“每次查询…并未给出…固定”；`sec:graph-theory-directed-transformations` | 限定判据转换保证，预告弦图工具。 | 同一碰撞例不同S不同祖先图 | 不把一问一图误当全部分离永久等价。 | 已清楚；无。 |

## 树分解与消元宽度

节标签：`sec:graph-theory-tree-decomposition`、`sec:graph-theory-spanning-skeleton`、`sec:graph-theory-elimination-width`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-118 团 | 669，“两两相邻的顶点集合”；`sec:graph-theory-tree-decomposition` | 指明哪些变量可能需要整体容纳。 | 贯穿图两个三角形 | 不等于因子函数值。 | 已清楚；无。 |
| B11-119 完全图 | 670，“全部顶点构成团”；`sec:graph-theory-tree-decomposition` | 给整个图的全连接性质命名。 | 团的定义直接覆盖 | 团是子集，完全图是图性质。 | 已清楚；无。 |
| B11-120 极大团 | 671–673，“不被更大团包含”；`sec:graph-theory-tree-decomposition` | 列出不能再扩展的局部全连接块。 | 两个三元团 | 极大按包含关系，不按全局基数。 | 已清楚；无。 |
| B11-121 最大团 | 671–673，“顶点数最多”；`sec:graph-theory-tree-decomposition` | 区分最优大小和不可扩张。 | 贯穿图二者恰合 | 不把所有极大团都当最大。 | 已清楚；无。 |
| B11-122 袋B_t | 679、689，“袋不是原图顶点”；`sec:graph-theory-tree-decomposition` | 在更高层图中用集合组织局部变量。 | 三个二元袋的图 | 袋节点与原变量两层对象显式区分。 | 已清楚；无。 |
| B11-123 树分解 | 678–685，“每个…每条…全部…连通”；`sec:graph-theory-tree-decomposition` | 同时覆盖原关系与保存共享变量一致性。 | `def:graph-theory-tree-decomposition` | 不是任选树状块覆盖。 | 已清楚；无。 |
| B11-124 运行交集性质 | 684–690，“出现位置构成连通子树”；`sec:graph-theory-tree-decomposition` | 保证远端同变量的值能经接口传递。 | `fig:graph-theory-running-intersection`正反例 | 袋树连通不够，必须逐变量连通。 | 已清楚；无。 |
| B11-125 袋交集接口 | 689，“只需交流交集上的信息”；`sec:graph-theory-tree-decomposition` | 给局部通信确定索引范围。 | 图上{2}、{3}和空交集 | 当前为结构接口，数值正确性后证。 | 已清楚；无。 |
| B11-126 子树Helly性质 | 706–712，“任意两棵…则…公共”；`sec:graph-theory-tree-decomposition` | 从两两边覆盖推出整个团共袋。 | `lem:graph-theory-subtree-helly`全证明 | 非任意集合的性质，限树上非空连通子树。 | 已清楚；无。 |
| B11-127 树的根 | 716，“任选根”；`sec:graph-theory-tree-decomposition` | 将唯一路径转换成上下次序。 | 根到x的唯一通路 | 不改变无向树边，只增加参照点。 | 已清楚；无。 |
| B11-128 深度与最近根点 | 716–725，“离根最近…深度最大”；`sec:graph-theory-tree-decomposition` | 构造所有子树的公共交点。 | 路径必须留在连通子树的论证 | 深度可由已学边数距离理解，最近点唯一有证明。 | 已清楚；无。 |
| B11-129 团必须同袋 | 728–731，“C⊆B_t”；`sec:graph-theory-tree-decomposition` | 说明大团不能被拆袋规避联合状态。 | T_v子树族及Helly | 仅边覆盖不足，运行交集是关键。 | 已清楚；无。 |
| B11-130 分解宽度 | 735，“max…减一”；`sec:graph-theory-tree-decomposition` | 衡量一项具体分解最大局部规模。 | 二元袋宽度1 | 不等于已经优化的图不变量。 | 已清楚；无。 |
| B11-131 树宽 | 735–736，“所有…最小值”；`sec:graph-theory-tree-decomposition` | 定义最优结构复杂度。 | 贯穿图上界下界同为2 | 区别任选分解宽度。 | 已清楚；无。 |
| B11-132 树与单点的树宽 | 736–740，“根自身…二元袋”；`sec:graph-theory-tree-decomposition` | 解释减一约定并给基准例。 | 根袋／父子袋构造 | 有边树为1，单点为0，条件未混。 | 已清楚；无。 |
| B11-133 团大小下界 | 746–748，“r−1”；`sec:graph-theory-tree-decomposition` | 证明特定宽度不能再降。 | 三角形完整同袋 | 是下界，不声称一般达到。 | 已清楚；无。 |
| B11-134 构造分解上界 | 748–749，“实际构造…上界”；`sec:graph-theory-tree-decomposition` | 给启发式结果可核查的保证。 | 两袋分解 | 与最小树宽及最优性证书不同。 | 已清楚；无。 |
| B11-135 稠密袋状态规模 | 751–754，“q^(k+1)…条目”；`sec:graph-theory-tree-decomposition` | 将结构宽度接到显式表成本。 | 有限候选乘法计数 | 第2章已回顾；因子访问、袋数等另计。 | 已清楚；无。 |
| B11-136 树宽的消元刻画预告 | 755–756，“最大剩余邻居数”；`sec:graph-theory-tree-decomposition` | 给下一结构操作的目的。 | 后文定理准确前指 | 不当作已证明的数值消元正确性。 | 预告清楚；无。 |
| B11-137 生成树 | 763–765，“覆盖全部顶点的树”；`sec:graph-theory-spanning-skeleton` | 仅为保持连接抽取原边。 | BFS／DFS父边 | 非树分解，不增加袋或变量副本。 | 已清楚；无。 |
| B11-138 生成森林 | 764–771，“每个分量…一棵树”；`sec:graph-theory-spanning-skeleton` | 覆盖不连通图的全部分量。 | n−c条边 | 每分量n_i−1求和，已学树边数足够。 | 已清楚；无。 |
| B11-139 遍历父边的生成构造 | 767–771，“新顶点…只保留…父边”；`sec:graph-theory-spanning-skeleton` | 将存在性变成可执行方法。 | 覆盖及无环证明 | 不保证最小成本生成树。 | 已清楚；无。 |
| B11-140 连接骨架的保真边界 | 773–779，“距离…割点”；`sec:graph-theory-spanning-skeleton` | 说明删边不能替代全部原查询。 | 1到3从一步变两步、2成为割点 | BFS只保特定源无权距离。 | 已清楚；无。 |
| B11-141 顶点消元 | 784–788，“先…两两连接，再删除”；`sec:graph-theory-elimination-width` | 用剩余变量表吸收被删变量影响。 | 好坏两种消元次序 | 不等于删边抽骨架。 | 已清楚；无。 |
| B11-142 填充边 | 789–790，“中间表可能的联合依赖”；`sec:graph-theory-elimination-width` | 记录计算产生的作用域。 | 新增1–4 | 不是新增独立约束，也不保证特殊函数不可再分。 | 已清楚；无。 |
| B11-143 消元次序π | 792–802，“处理次序…变量数”；`sec:graph-theory-elimination-width` | 让算法代价依赖可比较的排列。 | (1,4,2,3)对(2,1,3,4) | 同原图可不同中间表。 | 已清楚；无。 |
| B11-144 剩余邻域N⁺_π | 814–816，“次序中的后继”；`sec:graph-theory-elimination-width` | 指定每步依赖于当前填充图。 | 上标含义明示 | 不是原图邻域，也不是有向出邻域。 | 已清楚；无。 |
| B11-145 诱导宽度k_π | 816–820，“max…剩余邻居”；`sec:graph-theory-elimination-width` | 衡量一项次序最坏一步。 | 好坏宽度2、3 | 取最优次序后才等于树宽。 | 已清楚；无。 |
| B11-146 联合工作表规模 | 821、824–826，“q^(k_π+1)”；`sec:graph-theory-elimination-width` | 计入被消变量那一维。 | 图中不同首步表索引 | 工作空间与输出接口空间分开。 | 已清楚；无。 |
| B11-147 输出接口规模 | 822–827，“q^k_π”；`sec:graph-theory-elimination-width` | 表达消去一维后的存储。 | `fig:graph-theory-elimination-fill`4项对8项 | 所有接口还乘顶点数，原始因子另计。 | 已清楚；无。 |
| B11-148 全填充图H_π | 839–841，“保留全部原顶点”；`sec:graph-theory-elimination-width` | 在一张图中比较不同删除步骤。 | 原边加全部曾出现填充边 | 与每步缩小的当前图不同。 | 已清楚；无。 |
| B11-149 消元父袋p(v) | 841–853，“其中最早消去的”；`sec:graph-theory-elimination-width` | 将每步袋连成森林并保持共享变量。 | z沿父链一直保留至B_z | 非任选后继；跨分量空交集可接树。 | 已清楚；无。 |
| B11-150 消元序产生树分解 | 831–856，“宽度不超过”；`sec:graph-theory-elimination-width` | 从实际算法次序取得合法分解。 | `thm:graph-theory-elimination-tree-decomposition`全证明 | 顶点覆盖、边覆盖、运行交集分别证明。 | 已清楚；无。 |
| B11-151 冗余叶袋 | 861–863，“被相邻袋包含”；`sec:graph-theory-elimination-width` | 反向构造中先删不提供新变量的袋。 | X=B_ℓ∖B_p非空条件 | 不随意删除任意叶袋变量。 | 已清楚；无。 |
| B11-152 叶袋消元不变量 | 858–870，“当前填充图的树分解”；`sec:graph-theory-elimination-width` | 保证填充不破坏宽度上界。 | X只在叶袋，全部邻居同袋 | 不是只覆盖原图的一次性证明。 | 已清楚；无。 |
| B11-153 最优诱导宽度等于树宽 | 871–874，“tw=min k_π”；`sec:graph-theory-elimination-width` | 合并双向构造得优化等价。 | 前后两种上界 | 不等于任意启发式均最优。 | 已清楚；无。 |
| B11-154 最小度启发式预告 | 875，“最小度…等启发式”；`sec:graph-theory-elimination-width` | 提醒实际次序只给上界。 | 没有执行步骤，未用于后续证明 | 仅命名预告，不据此认定已教算法。 | 可选加“每步取当前度最小点”；非实质问题。 |
| B11-155 最少填充启发式预告 | 875，“最少填充”；`sec:graph-theory-elimination-width` | 同上，提示另一局部选择准则。 | 没有运行实例 | 与全局最小树宽不同。 | 可选加“每步新增边最少”；非实质问题。 |

## 弦图、团树与等价分离

节标签：`sec:graph-theory-chordal-elimination`、`sec:graph-theory-clique-trees`、`sec:graph-theory-separation-correspondence`、`sec:graph-theory-exact-approximate-algorithms`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-156 弦 | 889–895，“非相邻环顶点”；`sec:graph-theory-chordal-elimination` | 找出长环阻碍无填充的原因。 | 四环对角线 | 是否弦与画线弯直无关。 | 已清楚；无。 |
| B11-157 弦图 | 890，“每个这类环都有弦”；`sec:graph-theory-chordal-elimination` | 定义存在无填充次序的候选图类。 | 树、补一条对角线的四环 | 三角不需要弦，长度至少4条件明确。 | 已清楚；无。 |
| B11-158 弦化 | 891，“补边直到成为弦图”；`sec:graph-theory-chordal-elimination` | 为一般图建立可分解的完成图。 | `fig:graph-theory-chordal-cycle` | 会改变分离，不能称全部查询等价。 | 已清楚；无。 |
| B11-159 弦图的诱导遗传性 | 896，“仍是弦图”；`sec:graph-theory-chordal-elimination` | 允许删除后重复构造。 | 无弦环仍是原图无弦环的反证 | 一般删边子图没有该保证。 | 已清楚；无。 |
| B11-160 单纯顶点 | 910、915，“邻居组成团”；`sec:graph-theory-chordal-elimination` | 给一步无需填充命名。 | 四环补弦后顶点2 | 空邻域和单点邻域显式纳入。 | 已清楚；无。 |
| B11-161 完美消元序 | 911–916，“每个…剩余图中…单纯”；`sec:graph-theory-chordal-elimination` | 定义全程无填充的次序。 | (2,1,3,4) | 不是仅原图中每点单纯。 | 已清楚；无。 |
| B11-162 弦图的单纯顶点存在性 | 918–926、938–943，“两个互不相邻”；`sec:graph-theory-chordal-elimination` | 保证可以逐步消去而非假定能找。 | 归纳区分完全／不连通／连通不完全 | 加强版支持从两个局部块各取一点。 | 完整证明；无。 |
| B11-163 包含极小分隔集 | 928–932，“恢复s…极小性”；`sec:graph-theory-chordal-elimination` | 在归纳中构造边界团。 | 恢复单点可接通a,b | 极小不是最小基数，删除单项已足以用。 | 已清楚；无。 |
| B11-164 弦图极小分隔集成团 | 933–936，“同侧没有弦…跨分量没有边”；`sec:graph-theory-chordal-elimination` | 让归纳保证单纯点落在块内部。 | 两条最短路径组成无弦环 | 最短指已学无权边数，论证齐全。 | 已清楚；无。 |
| B11-165 弦图与完美消元序等价 | 945–956，“当且仅当”；`sec:graph-theory-chordal-elimination` | 给结构和计算次序的双向判据。 | `thm:graph-theory-chordal-perfect-elimination`全证明 | 反向取无弦环最早删除点，不循环引用。 | 已清楚；无。 |
| B11-166 填充完成图的完美次序 | 958–962，“该次序…成为完美”；`sec:graph-theory-chordal-elimination` | 解释任意消元为何得到弦化。 | 原弦图坏次序仍补边 | 存在好次序不等于任意次序好，无填充也可大宽度。 | 已清楚；无。 |
| B11-167 团树 | 967–968，“极大团作袋”；`sec:graph-theory-clique-trees` | 压缩一般袋树到结构上不可再扩张块。 | 贯穿图两个三元团 | 需运行交集，非任意连接。 | 已清楚；无。 |
| B11-168 团交集加权候选图 | 969、975–977，“完全…包括…零权边”；`sec:graph-theory-clique-trees` | 将连接方式转为明确的优化对象。 | w(C,D)=交集大小 | 零交集边用于连接非连通原图，不自动删除。 | 已清楚；无。 |
| B11-169 最大权树的运行交集刻画 | 973–979、999–1012，“当且仅当…总…权最大”；`sec:graph-theory-clique-trees` | 为团树选择给可验证准则。 | `thm:graph-theory-clique-tree-maximum-weight` | 算法尚未建立，有准确后指，不影响证明。 | 已清楚；无。 |
| B11-170 包含袋的收缩 | 990–997，“相邻超集袋”；`sec:graph-theory-clique-trees` | 从消元袋树得到仅极大团的树。 | 运行交集保证到极大袋路径全含小袋 | 不是直接删小袋使树断开；“收缩”可按邻边合并理解。 | 已清楚；无。 |
| B11-171 逐变量森林计边 | 999–1009，“e_v≤k_v−1”；`sec:graph-theory-clique-trees` | 将全树目标拆成每变量是否连通。 | 交换有限求和，取等当且仅当连通 | 已学森林n−c，无需额外优化定理。 | 已清楚；无。 |
| B11-172 非弦图的团树障碍 | 1014–1019，“四个必要连接又成环”；`sec:graph-theory-clique-trees` | 限制最大权方法适用范围。 | 四环边团反例 | 连接已知弦图与寻找最小宽度弦化是两任务。 | 已清楚；无。 |
| B11-173 全部分离关系等价 | 1024–1026，“同一顶点集…I相等”；`sec:graph-theory-separation-correspondence` | 从每问一图提高到固定表示。 | 与祖先道德化范围对照 | 不只单个S恰好同答。 | 已清楚；无。 |
| B11-174 弦图的完美DAG表示 | 1028–1035，“当且仅当…弦图”；`sec:graph-theory-separation-correspondence` | 判定无向分离何时可整体有向表示。 | `thm:graph-theory-chordal-perfect`全证明 | 同顶点集限制重要。 | 已清楚；无。 |
| B11-175 消元序的逆向定向 | 1033、1038–1039，“较晚…指向…较早”；`sec:graph-theory-separation-correspondence` | 同时保证无环及父集成团。 | 序号下降、父集等于后继邻域 | 不混同拓扑序方向，箭头约定明确。 | 已清楚；无。 |
| B11-176 最短路径排除碰撞 | 1040–1046，“绕过而缩短”；`sec:graph-theory-separation-correspondence` | 在完美DAG上对应活跃与避S路径。 | 父点相邻捷径、反向绕过S碰撞 | 回用本章活跃规则；不是一般DAG结论。 | 已清楚；无。 |
| B11-177 未遮蔽碰撞的等价障碍 | 1048–1053，“pa(i)…共同子点…不在”；`sec:graph-theory-separation-correspondence` | 证明一般DAG无法对应某无向图。 | 已证邻接判据及骨架两步路 | 第10章此结构已读；这里完整重接父集分离。 | 已清楚；无。 |
| B11-178 无弦环的最晚拓扑点 | 1055–1058，“两…邻居都指向它”；`sec:graph-theory-separation-correspondence` | 从无碰撞障碍反推骨架弦性。 | 环上两不相邻父节点 | 仅用已经建立的拓扑序，不需新图论工具。 | 已清楚；无。 |
| B11-179 完美DAG的无向表示 | 1061–1067，“当且仅当…完美”；`sec:graph-theory-separation-correspondence` | 判定给定DAG是否有固定无向替代。 | `thm:graph-theory-perfect-undirected`全证明 | 不是每张有弦骨架DAG都自动满足。 | 已清楚；无。 |
| B11-180 逆拓扑序作为完美消元序 | 1070–1075，“剩余邻居恰为其父集”；`sec:graph-theory-separation-correspondence` | 把第二定理接到已证第一定理。 | 每步先删全部后代，父集成团 | 消元方向与拓扑方向相反，明确展示。 | 已清楚；无。 |
| B11-181 条件集合单调性的障碍 | 1084–1086，“增加而重新接通”；`sec:graph-theory-separation-correspondence` | 给两个等价定理的直觉反例。 | 1→3←2给定3会打开 | 无向删点只会失去路径，与DAG条件化不同。 | 已清楚；无。 |
| B11-182 图等价与数值分解边界 | 1087–1088，“不是任意分布…保证”；`sec:graph-theory-separation-correspondence` | 防止结构定理越界成概率结论。 | 第10章Markov及忠实性已完整读 | 不预设任意分布遵守图。 | 已清楚；无。 |
| B11-183 选择对象决定优化任务 | 1093–1097，“路径…流量…树…匹配…配置”；`sec:graph-theory-exact-approximate-algorithms` | 为下一节列出待解决对象，限定统一性。 | 尚无新算法公式 | 流量、匹配与松弛仅预告，后文正式引入。 | 预告清楚；无。 |

补充图源核对：`graph-running-intersection.tex`1–20（`concept-revision-linear-geometry/`）与`elimination-fill.tex`1–25（`reader-revision-graph/`）已全文读取，节点／袋／填充边与图注一致；弦图图注901–904行已随正文完整阅读。

## 最短路与流量

节标签：`sec:graph-theory-shortest-paths`；容量约束小节无独立标签，沿用父节`sec:graph-theory-exact-approximate-algorithms`，各定理／图另有精确标签。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-184 无向边的双弧转换 | 1102–1103，“两条同长度的反向弧”；`sec:graph-theory-shortest-paths` | 统一加权路径算法口径。 | 无向负边变二弧负环 | 不等于抹去无向负边往返风险。 | 已清楚；无。 |
| B11-185 简单路径最小值 | 1104–1111，“d_path=min”；`sec:graph-theory-shortest-paths` | 明确有限候选的优化对象。 | 本章前述路径有限性 | 可达时取得最小；空集约定正无穷。 | 已回顾；无。 |
| B11-186 行走下确界 | 1105–1115，“d_walk=inf”；`sec:graph-theory-shortest-paths` | 说明标准算法负环时在求什么。 | 重复负环趋负无穷 | 非简单路径最优值；只计能影响目标的环。 | 已回顾；无。 |
| B11-187 最后一条弧的Bellman关系 | 1117–1123，“按最后一条弧分类”；`sec:graph-theory-shortest-paths` | 给递推的局部条件。 | `eq:graph-theory-shortest-path-bellman` | 起点单独零值，假定源可达区域无负环。 | 已清楚；无。 |
| B11-188 正无穷距离约定 | 1111、1124–1125，“+∞+c=+∞”；`sec:graph-theory-shortest-paths` | 使不可达点也参与同一更新式。 | 空前驱集合 | 不把正无穷当可达路径见证。 | 已清楚；无。 |
| B11-189 Bellman固定点非唯一 | 1128–1132，“任意…≤5”；`sec:graph-theory-shortest-paths` | 说明局部方程不能代替算法初始化。 | 零环a↔b、入口边长5 | 与真实距离的唯一数值不同。 | 反例清楚；无。 |
| B11-190 DAG最短路递推 | 1136–1141，“按拓扑序更新”；`sec:graph-theory-shortest-paths` | 在无环依赖中一次完成。 | L初始化与入邻居最小式 | 允许负边，靠次序而非非负性。 | 已清楚；无。 |
| B11-191 路径见证与拓扑归纳 | 1142–1146，“每个有限候选值…实际路径”；`sec:graph-theory-shortest-paths` | 同时证明不会低估也不会漏优解。 | 前缀最后弧分解、零步保留 | 不可达情形也覆盖。 | 全证明可跟随；无。 |
| B11-192 DAG线性遍历代价 | 1148–1150，“O(V+A)”；`sec:graph-theory-shortest-paths` | 把前面排序和边扫描合并。 | 每条入弧只检查一次 | 非一般有环图复杂度。 | 已清楚；无。 |
| B11-193 距离松弛 | 1154–1162，“前驱…以后下降”；`sec:graph-theory-shortest-paths` | 允许有环时逐步改进暂定标签。 | 新旧标签取最小 | 与永久确定一个点的贪心不同。 | 已清楚；无。 |
| B11-194 同步轮标签L^(k) | 1163–1166，“至多…k条边”；`sec:graph-theory-shortest-paths` | 给每轮确切语义及归纳不变量。 | 零步基例、前缀加一弧 | 不是恰好k边，也非就地版的精确含义。 | 已清楚；无。 |
| B11-195 Bellman–Ford算法 | 1168–1171，“n−1轮…正确距离”；`sec:graph-theory-shortest-paths` | 将有限简单见证转为轮数上界。 | O(nA)、删非负闭合段 | 目标不能受可达负环影响。 | 已清楚；无。 |
| B11-196 就地更新与同步更新 | 1172–1175，“提前传播…等式只属于…同步”；`sec:graph-theory-shortest-paths` | 防止实现方式改变不变量却仍照抄证明。 | 覆盖全部至多k边且仍有行走见证 | 轮数上界保留，但精确k语义不保留。 | 已清楚；无。 |
| B11-197 负环影响种子 | 1177–1185，“固定…标签…严格改善”；`sec:graph-theory-shortest-paths` | 找到必须标为负无穷的起始点。 | n边优于所有n−1边候选的重复点论证 | 先固定标签再检测，不混用传播中的状态。 | 已清楚；无。 |
| B11-198 种子后继覆盖的充要性 | 1187–1194，“这些且仅这些”；`sec:graph-theory-shortest-paths` | 标出全部且仅受影响目标。 | 环上不等式相加矛盾、后继遍历 | 负环证据、影响范围和简单路径最小值分开。 | 已清楚；无。 |
| B11-199 Dijkstra算法 | 1198–1202，“每次…暂定距离最小”；`sec:graph-theory-shortest-paths` | 用非负边长永久确定一项距离。 | 初始化、选点、松弛及前驱记录 | 全部边非负，零边允许。 | 已清楚；无。 |
| B11-200 暂定距离与已确定集合 | 1199–1201，“维护…S”；`sec:graph-theory-shortest-paths` | 分清仍能更新与已经定值。 | 出邻居松弛 | 与真实D的先前记号同字母但此处明确重新定义。 | 已清楚；无。 |
| B11-201 贪心正确性 | 1204–1225，“第一个尚不属于S”；`sec:graph-theory-shortest-paths` | 找出非负性在证明中的具体作用。 | `thm:graph-theory-dijkstra-correctness` | 前缀不大于全路；不可达尾部另证。 | 已清楚；无。 |
| B11-202 二叉堆 | 1227，“二叉堆…O((V+A)log V)”；`sec:graph-theory-shortest-paths` | 支撑取最小和标签更新的效率声明。 | 后面算例只演示距离，没有堆操作 | 前1–10章未见定义，操作成本来由悬空。 | 局部费力R1-B-042；补优先队列操作及二叉堆成本接口。 |
| B11-203 无负环仍会贪心失败 | 1233–1238，“真实距离…1”；`sec:graph-theory-shortest-paths` | 区分非负边和无负环两个条件。 | 三弧含−4、正权五弧成功例 | DAG递推／Bellman–Ford可处理同一失败例。 | 已清楚；无。 |
| B11-204 网络源点与汇点 | 1242–1244，“不同的…s…t”；`sec:graph-theory-exact-approximate-algorithms` | 将路径选择改为共同输送。 | s与t指定且不同 | 内部点守恒而端点承担净流量。 | 已清楚；无。 |
| B11-205 容量 | 1244、1247，“有限非负”；`sec:graph-theory-exact-approximate-algorithms` | 限制每条原弧能承载的流量。 | c_i,j及0≤f≤c | 不作为距离或相似度使用。 | 已正式建立；无。 |
| B11-206 流 | 1245–1250，“弧数值”；`sec:graph-theory-exact-approximate-algorithms` | 定义可行方案而非只选一条路线。 | 全部弧的f_i,j | 可通过多路输送，不是路径条数。 | 已清楚；无。 |
| B11-207 内部流守恒 | 1248–1249，“流入…=…流出”；`sec:graph-theory-exact-approximate-algorithms` | 防止中途创造或丢失输送量。 | v≠s,t的方程 | 源汇不要求零净流。 | 已清楚；无。 |
| B11-208 流值 | 1251，“源点的净流出量”；`sec:graph-theory-exact-approximate-algorithms` | 指定最大化目标。 | 后面跨割净流式 | 不是所有弧的f求和。 | 已清楚；无。 |
| B11-209 s–t割及容量 | 1252–1255，“s∈S,t∉S”；`sec:graph-theory-exact-approximate-algorithms` | 由顶点分组给全部流的上界。 | 仅计S指向补集的容量 | 有向割不把反向容量加进上界。 | 已清楚；无。 |
| B11-210 流割弱界 | 1256–1257，“内部…相消”；`sec:graph-theory-exact-approximate-algorithms` | 给最优性的可核验比较。 | 守恒求和、反向流入非负 | 可行流下界与任意割上界方向明确。 | 已清楚；无。 |
| B11-211 最大流最小割 | 1259–1262，“最大…等于…最小”；`sec:graph-theory-exact-approximate-algorithms` | 证明上下界可同时达到。 | `thm:graph-theory-max-flow-min-cut`全证明 | 有限非负容量，非算法无限循环的存在证明。 | 已清楚；无。 |
| B11-212 最大流的紧致存在性 | 1265–1266，“闭有界…连续”；`sec:graph-theory-exact-approximate-algorithms` | 先取得最优对象再反证无增广路。 | 第3章722–753已实际展开 | 有限维、零流可行、每弧容量有限齐全。 | 已回顾；无。 |
| B11-213 正向残量弧 | 1267–1268，“c−f”；`sec:graph-theory-exact-approximate-algorithms` | 表达还能追加多少。 | 容量3已发2剩1 | 非新实际通道。 | 已清楚；无。 |
| B11-214 反向残量弧 | 1268、1289–1291，“允许撤回”；`sec:graph-theory-exact-approximate-algorithms` | 使先前选择能够调整。 | 已发2可撤回2 | 不要求原网络有反向运输通道。 | 已清楚；无。 |
| B11-215 残量弧身份 | 1269，“不把两种作用混为…流变量”；`sec:graph-theory-exact-approximate-algorithms` | 处理原图同时有相反方向弧时的歧义。 | 追加另一原弧与撤销本弧分开 | 与此前简单图默认并不冲突，残量网络可多弧。 | 已清楚；无。 |
| B11-216 增广瓶颈δ | 1271–1274，“最小残量容量”；`sec:graph-theory-exact-approximate-algorithms` | 给保持可行又增加流值的步长。 | 正向加、反向减、内部变化相消 | 只走正残量弧故δ>0。 | 已清楚；无。 |
| B11-217 残量可达割 | 1276–1284，“原弧必须已满…必须…零”；`sec:graph-theory-exact-approximate-algorithms` | 从无增广路径提取同值割。 | S是残量可达集 | 原网络可达不等于残量可达。 | 已清楚；无。 |
| B11-218 同值流割证书 | 1286、1303–1318，“两者分别最优”；`sec:graph-theory-exact-approximate-algorithms` | 无需遍历所有方案即可认证答案。 | 流2+2+1=5，割3+2=5及图 | 不是只给一个可行流就称最大。 | 已清楚；无。 |
| B11-219 整数最优流 | 1293–1296，“始终为整数”；`sec:graph-theory-exact-approximate-algorithms` | 支持后续真实匹配而非分数边。 | 整数瓶颈每次至少加1 | 从零开始与有限终止共同完成存在证。 | 已清楚；无。 |
| B11-220 容量值依赖的次数界 | 1294–1297，“未必…二进制位数…多项式”；`sec:graph-theory-exact-approximate-algorithms` | 区分数值大小与输入长度复杂度。 | C_s次增广上界 | 不是强多项式声明。 | 已清楚；无。 |
| B11-221 BFS残量增广路预告 | 1298–1300，“边数最少…次数界”；`sec:graph-theory-exact-approximate-algorithms` | 指出有有限步保证的选择规则。 | 引用已学BFS操作，未给次数常数 | 扩展算法提示，不把未证明界用于本处最优性。 | 预告清楚；可选给算法来源。 |
| B11-222 实数存在与有效计算边界 | 1300–1301，“紧性…却不能…有限终止”；`sec:graph-theory-exact-approximate-algorithms` | 防止存在性等同机器可精确计算。 | 任意实容量／有效表示区别 | 与整数和有理输入不同。 | 已清楚；无。 |

## 生成树与匹配优化

节标签：`sec:graph-theory-minimum-spanning-tree`；匹配小节沿用父节`sec:graph-theory-exact-approximate-algorithms`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-223 最小生成树MST | 1324–1328，“成本之和最小”；`sec:graph-theory-minimum-spanning-tree` | 在连接骨架中增加全局建造成本目标。 | 三角2,2,3 | 不保所有端点最短距离。 | 已清楚；无。 |
| B11-224 轻边 | 1330–1331，“跨割成本最小”；`sec:graph-theory-minimum-spanning-tree` | 给可安全加入的局部选择。 | 非平凡划分 | 负成本允许，轻指相对最小。 | 已清楚；无。 |
| B11-225 MST割性质 | 1333–1337，“不切断A…共同包含”；`sec:graph-theory-minimum-spanning-tree` | 保证当前部分方案仍可扩为最优。 | `lem:graph-theory-mst-cut-property` | 不声称任意轻边属于所有MST。 | 已清楚；无。 |
| B11-226 加边删环的交换证明 | 1340–1344，“T+e−f”；`sec:graph-theory-minimum-spanning-tree` | 将局部轻边替进最优树。 | 唯一环另有跨割边、f不在A | 已学树唯一路径足够。 | 已清楚；无。 |
| B11-227 Kruskal算法 | 1347–1350，“从小到大…连接两个当前分量”；`sec:graph-theory-minimum-spanning-tree` | 扫描所有边逐步构树。 | 割性质归纳 | 判断当前分量，不能仅按原分量。 | 已清楚；无。 |
| B11-228 Prim算法 | 1351–1352，“维护一个已连通顶点集”；`sec:graph-theory-minimum-spanning-tree` | 用单个增长区域实现同一割性质。 | 每次跨S轻边 | 与Kruskal全图森林生长不同。 | 已清楚；无。 |
| B11-229 并查集 | 1352，“排序与并查集支持”；`sec:graph-theory-minimum-spanning-tree` | 实现动态分量检测和合并。 | 没有定义或操作示例 | 前1–10章未见说明，名字不能解释支持何事。 | 局部费力R1-B-042；补find判同组、union合并两组。 |
| B11-230 优先队列 | 1352，“优先队列支持Prim”；`sec:graph-theory-minimum-spanning-tree` | 高效选出当前最小候选。 | 未给维护对象及取最小／降键操作 | 抽象操作接口与二叉堆具体实现未区分。 | 局部费力R1-B-042；在Dijkstra首次成本处前置短解释。 |
| B11-231 最优值与最优树非唯一 | 1354–1355，“多棵…总成本仍唯一”；`sec:graph-theory-minimum-spanning-tree` | 澄清并列、负成本、非连通图边界。 | 最小生成森林逐分量求 | 方案不唯一不表示数值不确定。 | 已清楚；无。 |
| B11-232 最大权生成树转换 | 1356–1358，“相反数…反向排序”；`sec:graph-theory-minimum-spanning-tree` | 接回团交集权优化。 | 负权仍适用交换论证 | 运行交集来自团树结构定理，不由贪心单独保证。 | 已清楚；无。 |
| B11-233 匹配 | 1362，“不共享端点”；`sec:graph-theory-exact-approximate-algorithms` | 表达候选配对互斥约束。 | 二部图U,W | 此处选择边，不是给每点连续信号。 | 已清楚；无。 |
| B11-234 极大匹配 | 1363–1364，“不能直接再加入”；`sec:graph-theory-exact-approximate-algorithms` | 定义只对添加操作无改进。 | 后c不能直接连y | 不排除替换已有边改进。 | 已清楚；无。 |
| B11-235 最大匹配 | 1363，“边数…最多”；`sec:graph-theory-exact-approximate-algorithms` | 固定全局基数目标。 | 后大小2改为3 | 与最大权匹配另分。 | 已清楚；无。 |
| B11-236 单位容量匹配归约 | 1366–1373，“同值整数流”；`sec:graph-theory-exact-approximate-algorithms` | 将最大匹配精确转为已解决流问题。 | s→u→w→t，源汇两侧容量1 | 整数最优流已证，避免分数边误解。 | 双向解释齐全；无。 |
| B11-237 匹配增广路径 | 1375–1376，“交替…首尾…未匹配”；`sec:graph-theory-exact-approximate-algorithms` | 找到允许撤销再补选的改进路线。 | c-y-b-z | 两端均尚未匹配，普通路径不足。 | 已清楚；无。 |
| B11-238 沿增广路翻转 | 1377–1383，“大小增加1”；`sec:graph-theory-exact-approximate-algorithms` | 验证改进仍是匹配。 | 撤b-y，加c-y、b-z及图 | 内部仍一条、端点各增加。 | 已清楚；无。 |
| B11-239 无增广路的最大性证书 | 1379–1380，“无残量路径…割证书”；`sec:graph-theory-exact-approximate-algorithms` | 接回全局而非局部最优。 | 未匹配正向、已匹配反向 | 当前二部单位网络的精确对应已建立。 | 已清楚；无。 |
| B11-240 非二部与加权匹配边界 | 1395–1397，“奇环…总权重”；`sec:graph-theory-exact-approximate-algorithms` | 限定归约的图类及目标。 | 无新算法，边界预告 | 非二部不能分U,W；最多边不等于最大收益。 | 预告清楚；无。 |

## 拉普拉斯与二值能量

节标签：`sec:graph-theory-spectrum-discrete-symmetry`、`sec:graph-theory-vertex-configuration`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-241 加权度 | 1407–1413，“Σ_j w_i,j”；`sec:graph-theory-spectrum-discrete-symmetry` | 根据连接总量设置尺度。 | 普通度比较 | 只有全结构边权1时等于邻居数。 | 已清楚；无。 |
| B11-242 加权度矩阵D^(w) | 1411，“diag”；`sec:graph-theory-spectrum-discrete-symmetry` | 把局部权重和写成顶点算子。 | 对角d_i^(w) | 不是边权矩阵W_E，也不是邻接W。 | 已清楚；无。 |
| B11-243 组合图拉普拉斯L | 1417–1423，“D^(w)−W”；`sec:graph-theory-spectrum-discrete-symmetry` | 用边差表达配置不平滑。 | `def:graph-theory-combinatorial-laplacian` | 有限无向非负权条件明确。 | 已清楚；无。 |
| B11-244 顶点差汇总Lf | 1426–1430，“本点与邻居的差”；`sec:graph-theory-spectrum-discrete-symmetry` | 解释矩阵作用而非只给名字。 | Σw(f_i−f_j) | 与Af汇总邻值不同。 | 已清楚；无。 |
| B11-245 关联矩阵分解L | 1431–1435，“B W_E Bᵀ”；`sec:graph-theory-spectrum-discrete-symmetry` | 把逐边差分合成连接到此前表示。 | 每列给四个矩阵位置贡献 | 临时方向不变性前面已证明。 | 已清楚；无。 |
| B11-246 图Dirichlet能量 | 1437–1448、1472，“沿边的平方变化”；`sec:graph-theory-spectrum-discrete-symmetry` | 定量衡量平滑与边界成本。 | `eq:graph-theory-dirichlet-energy` | 与顶点平方和不同；有序双计故乘1/2。 | 已清楚；无。 |
| B11-247 对称半正定性 | 1451、1455–1463，“各项非负”；`sec:graph-theory-spectrum-discrete-symmetry` | 允许自伴谱及能量最小化。 | 二次型展开全证明 | 第6章加权几何和谱结论已补读。 | 已回顾；无。 |
| B11-248 分量常量零空间 | 1465–1468，“正权边…值相等”；`sec:graph-theory-spectrum-discrete-symmetry` | 识别完全不受惩罚的方向。 | 沿支撑路径传等值，逆向检验Lf=0 | 结构零权边不强迫两端同值。 | 已清楚；无。 |
| B11-249 零空间维数 | 1451–1452、1469，“分量的个数”；`sec:graph-theory-spectrum-discrete-symmetry` | 将线性代数维数对应图结构。 | 各分量指示向量独立并张成 | 只数正权支撑分量。 | 已清楚；无。 |
| B11-250 负权／有向谱边界 | 1473–1474，“不能直接继承”；`sec:graph-theory-spectrum-discrete-symmetry` | 避免将同名拉普拉斯都视为对称半正定。 | 负权可使平方项贡献负 | 不展开其他定义，纯边界提示。 | 已清楚；无。 |
| B11-251 对称归一化拉普拉斯 | 1476–1483，“按连接总量调整”；`sec:graph-theory-spectrum-discrete-symmetry` | 改变顶点尺度以比较不同度。 | `eq:graph-theory-normalized-laplacian` | 是左右度缩放，不是一般相似变换L。 | 已清楚；无。 |
| B11-252 零度逆平方根约定 | 1485–1486，“条目为0”；`sec:graph-theory-spectrum-discrete-symmetry` | 处理无法求逆的孤立支撑点。 | 对应行列为零 | “孤立”针对正权支撑，非必结构孤点。 | 已清楚；无。 |
| B11-253 归一化算子的零模 | 1489–1493，“D^(w)^(1/2)1”；`sec:graph-theory-spectrum-discrete-symmetry` | 说明改坐标后常量零模怎样变化。 | f→g换元及零点单独坐标向量 | 不是全部分量仍用常数向量。 | 已清楚；无。 |
| B11-254 随机游走拉普拉斯 | 1495–1496，“D^(w)^−1 L”；`sec:graph-theory-spectrum-discrete-symmetry` | 为按度平均的运算引入另一表示。 | 零逆条目约定 | 与L_sym通常不同，后文才解释游走动力学。 | 定义清楚；无。 |
| B11-255 L_sym与L_rw相似 | 1497–1502，“因此两者相似”；`sec:graph-theory-spectrum-discrete-symmetry` | 比较谱而保留坐标差异。 | 显式D^(1/2)换基式 | 先限全部正度，不能在零度处用不可逆换基。 | 已清楚；无。 |
| B11-256 度加权内积下自伴 | 1503–1506，“D L_rw=L=Lᵀ”；`sec:graph-theory-spectrum-discrete-symmetry` | 解释非欧氏对称仍有自伴几何。 | xᵀD y、零度需限制子空间 | 第6章正定／半正定内积已实读。 | 已清楚；无。 |
| B11-257 三种几何的对应表 | 1508–1523，“改变坐标与改变内积”；`sec:graph-theory-spectrum-discrete-symmetry` | 集中比较算子、零模和内积。 | `tab:graph-theory-laplacian-geometries`全表及图注 | 表先假设全正度，不与零点约定矛盾。 | 已清楚；无。 |
| B11-258 一元成本D_i | 1528–1534，“该点选某标签”；`sec:graph-theory-spectrum-discrete-symmetry` | 给二值变量的局部偏好。 | 两变量算例0/2与2/0 | 不是度矩阵，带函数自变量可辨别。 | 已清楚；无。 |
| B11-259 成对成本θ_i,j | 1529–1534，“相邻标签的相容性”；`sec:graph-theory-spectrum-discrete-symmetry` | 表示边上四种联合取值代价。 | θ(0,0)…θ(1,1) | 不只是一项权重，未必可图割。 | 已清楚；无。 |
| B11-260 二值成对能量E(z) | 1531–1538，“一元…加…成对”；`sec:graph-theory-spectrum-discrete-symmetry` | 将目标统一成显式配置函数。 | `eq:graph-theory-binary-pairwise-energy` | 能量与边集E区别明示；平方差等于绝对差仅二值。 | 已清楚；无。 |
| B11-261 二值成对次模性 | 1541–1547，“θ00+θ11≤θ01+θ10”；`sec:graph-theory-spectrum-discrete-symmetry` | 给非负边界代价的准确条件。 | `eq:graph-theory-pairwise-submodularity` | 第2章交并式已实读；不要求每项同标签都较便宜。 | 已清楚；可选加两元素集合对应式。 |
| B11-262 次模成对能量割表示 | 1549–1555，“能量加同一个常数”；`sec:graph-theory-spectrum-discrete-symmetry` | 保证最小割解决原全局目标。 | `thm:graph-theory-submodular-cut-representation`全证明 | 限有限实值二元成对项。 | 已清楚；无。 |
| B11-263 成对割权w | 1558–1567，“差…除2”；`sec:graph-theory-spectrum-discrete-symmetry` | 从任意次模四项表提取非负边界权。 | `eq:graph-theory-cut-pair-weight` | 次模恰保证w≥0。 | 已清楚；无。 |
| B11-264 一元修正α_i,α_j | 1563–1565，“θ10−θ00−w”；`sec:graph-theory-spectrum-discrete-symmetry` | 吸收不对称标签偏好。 | `eq:graph-theory-cut-unary-shifts` | 可为负，后统一平移，不要求原四项全非负。 | 已清楚；无。 |
| B11-265 四项分解恒等式 | 1568–1585，“逐项核对四种配置”；`sec:graph-theory-spectrum-discrete-symmetry` | 证每个配置而非仅最优点对应。 | `eq:graph-theory-pairwise-cut-decomposition` | 常数、线性和边差分别归并，检查完整。 | 已清楚；无。 |
| B11-266 一元非负平移 | 1586–1588，“减去m_i”；`sec:graph-theory-spectrum-discrete-symmetry` | 让终端容量合法而不变最优配置。 | m_i=min两个值、C′补回 | 只改变常数，不声称比例近似不变。 | 已清楚；无。 |
| B11-267 终端弧与标签约定 | 1590–1594，“源侧…0…汇侧…1”；`sec:graph-theory-spectrum-discrete-symmetry` | 防止将一元支付方向接反。 | s→i付标签1，i→t付标签0 | 给出两侧逐一核验。 | 已清楚；无。 |
| B11-268 反向双弧只付一次 | 1595–1597，“只有…一条计费”；`sec:graph-theory-spectrum-discrete-symmetry` | 保证异标签边界权不翻倍。 | `fig:graph-theory-binary-energy-cut` | 有向割只计源侧到汇侧，和流量节一致。 | 已清楚；无。 |
| B11-269 配置与割一一对应 | 1599–1601，“唯一决定…也唯一给出”；`sec:graph-theory-spectrum-discrete-symmetry` | 完成值和最优方案的双向保证。 | 割容量=E−C′ | 不是只构造一个方向的上界。 | 已清楚；无。 |
| B11-270 有效容量编码条件 | 1604–1606，“实际精确计算”；`sec:graph-theory-spectrum-discrete-symmetry` | 再次区分实值存在与执行能力。 | 有理数／有限精度、准确文献 | 没把任意实数当机器输入。 | 已清楚；无。 |
| B11-271 非次模及多标签边界 | 1626–1628，“不能自动…一次最小割”；`sec:graph-theory-spectrum-discrete-symmetry` | 限定构造，不泛称全部标签问题容易。 | w<0破坏容量 | 辅助点等纯后续方法预告，仍须各证。 | 已清楚；无。 |

## 比率割与归一化割

节标签仍为`sec:graph-theory-vertex-configuration`；近似质量小节无独立标签，沿用`sec:graph-theory-exact-approximate-algorithms`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-272 划分规模平衡 | 1632–1634，“孤立…稀少…空侧…零割”；`sec:graph-theory-spectrum-discrete-symmetry` | 避免仅压低边界产生无意义区域。 | 单点和空侧反例 | 顶点数平衡与体积平衡后分开。 | 已清楚；无。 |
| B11-273 拉普拉斯升序谱 | 1636–1640，“0=λ1≤λ2”；`sec:graph-theory-spectrum-discrete-symmetry` | 指定平滑方向的排列。 | 连通时u1=常量、λ2>0 | 第6章谱定理已实读；n≥2条件明确。 | 已回顾；无。 |
| B11-274 Rayleigh商 | 1641–1644，“单位平方范数”；`sec:graph-theory-spectrum-discrete-symmetry` | 比较方向而排除任意缩小幅度。 | fᵀLf/fᵀf | 第6章2065–2089已实读。 | 已回顾；无。 |
| B11-275 费德勒向量 | 1645–1647，“第二特征向量”；`sec:graph-theory-spectrum-discrete-symmetry` | 取正交常量后的最低能量方向。 | 两内部紧密区域近常量的解释 | 受连通条件和重数边界限制，不假定方向唯一。 | 已清楚；无。 |
| B11-276 阈值化 | 1648，“才会得到离散划分”；`sec:graph-theory-spectrum-discrete-symmetry` | 将实值方向恢复成标签集合。 | 后例零阈值、同号分组 | 连续特征向量本身不是分组。 | 已清楚；无。 |
| B11-277 指示向量割能量 | 1650–1657，“异侧平方差为一”；`sec:graph-theory-spectrum-discrete-symmetry` | 把离散边界接到拉普拉斯二次型。 | `eq:graph-theory-indicator-cut-energy` | 无向跨边每次计一次。 | 已清楚；无。 |
| B11-278 RatioCut | 1658–1664，“1/a+1/b”；`sec:graph-theory-spectrum-discrete-symmetry` | 用顶点数惩罚过小一侧。 | `eq:graph-theory-ratio-cut` | 两侧非空，不是流网络固定源汇割目标。 | 已清楚；无。 |
| B11-279 两水平平衡向量 | 1665–1678，“sqrt(b/a)…−sqrt(a/b)”；`sec:graph-theory-spectrum-discrete-symmetry` | 将离散大小限制编码进向量。 | `eq:graph-theory-ratio-cut-balanced-vector` | 均值零、范数平方n均逐式验证。 | 已清楚；无。 |
| B11-280 RatioCut二次型等价 | 1679–1686，“n RatioCut”；`sec:graph-theory-spectrum-discrete-symmetry` | 说明后续松弛是在放宽同一目标。 | `eq:graph-theory-ratio-cut-energy` | 先限定两水平，不能直接省略离散约束。 | 已清楚；无。 |
| B11-281 谱松弛 | 1687–1693，“去掉两水平限制”；`sec:graph-theory-spectrum-discrete-symmetry` | 扩大可行域求易计算下界。 | `eq:graph-theory-ratio-cut-relaxation` | 平衡和尺度仍保留，不是全空间无约束。 | 已清楚；无。 |
| B11-282 λ2下界及达到 | 1694–1702，“谱…加权平均”；`sec:graph-theory-spectrum-discrete-symmetry` | 证明松弛全局解而非仅驻点。 | 特征展开、sqrt(n)u2取等 | 不保证离散取整达到同值。 | 完整推导；无。 |
| B11-283 不连通支撑的零下界 | 1702–1703，“按分量取相反常量”；`sec:graph-theory-spectrum-discrete-symmetry` | 处理多个零模造成的不唯一。 | 分量常量满足平衡 | 零值不保证固定单个划分方向。 | 已清楚；无。 |
| B11-284 图体积 | 1705–1710，“Σ_i d_i^(w)”；`sec:graph-theory-spectrum-discrete-symmetry` | 用连接量替代顶点数度量规模。 | 内边计两端、跨边本侧一次 | 相同基数可以不同体积。 | 已清楚；无。 |
| B11-285 NCut | 1711–1717，“1/p+1/q”；`sec:graph-theory-spectrum-discrete-symmetry` | 用两侧体积惩罚小区域。 | `eq:graph-theory-normalized-cut` | 当前全正度、两侧正体积；与RatioCut不同。 | 已清楚；无。 |
| B11-286 度加权两水平向量 | 1718–1736，“sqrt(q/p)”；`sec:graph-theory-spectrum-discrete-symmetry` | 将体积平衡转成D内积约束。 | yᵀD1=0、yᵀDy=p+q | 不再用普通坐标和当平衡。 | 已清楚；无。 |
| B11-287 度加权Rayleigh问题 | 1738–1743，“yᵀLy/yᵀDy”；`sec:graph-theory-spectrum-discrete-symmetry` | 放宽NCut二水平条件。 | `eq:graph-theory-normalized-cut-relaxation` | 第6章广义Rayleigh定义已实读。 | 已回顾；无。 |
| B11-288 约束拉格朗日函数 | 1745–1754，“λ…μ”；`sec:graph-theory-spectrum-discrete-symmetry` | 从范数和正交两条件导出方程。 | J及两个梯度项 | 第4章乘子与驻点已展开；不把驻点等同全局最优。 | 已清楚；无。 |
| B11-289 消去平衡乘子μ | 1756–1757，“左乘1ᵀ”；`sec:graph-theory-spectrum-discrete-symmetry` | 简化为广义特征方程。 | 1ᵀL=0、yᵀD1=0 | 正总体积使μ=0。 | 已清楚；无。 |
| B11-290 NCut广义特征问题 | 1758–1762，“Ly=λDy”；`sec:graph-theory-spectrum-discrete-symmetry` | 明确正确谱对象。 | `eq:graph-theory-normalized-cut-generalized-eigenproblem` | 不是组合L普通特征方程。 | 已清楚；无。 |
| B11-291 归一化坐标x | 1763–1768，“x=D^(1/2)y”；`sec:graph-theory-spectrum-discrete-symmetry` | 将加权几何改为欧氏谱问题。 | 与D^(1/2)1正交的商 | 正度保证可逆；第6章换元已核对。 | 已清楚；无。 |
| B11-292 第二方向与任意驻点 | 1769–1770，“全局最小…而不只是…驻点”；`sec:graph-theory-spectrum-discrete-symmetry` | 完成最优性而非停在方程。 | L_sym正交谱展开 | 解任意特征对不足，须排零模后取最小。 | 已清楚；无。 |
| B11-293 正度正则图 | 1771–1772，“D=dI”；`sec:graph-theory-spectrum-discrete-symmetry` | 给两种方向必然重合的特殊条件。 | L_sym=L/d可由公式直接算 | 一般不规则图不保证重合。 | 白话由等式明确；无。 |
| B11-294 零度体积边界 | 1773，“不能直接除以p,q”；`sec:graph-theory-spectrum-discrete-symmetry` | 防止归一化式除零。 | 零度点单独处理 | 与前面L_sym零行列约定相容。 | 已清楚；无。 |
| B11-295 四点路径的L及D | 1775–1785，“可以手算”；`sec:graph-theory-spectrum-discrete-symmetry` | 给所有谱／割比较一个具体矩阵。 | 完整4×4 L和diag(1,2,2,1) | 从此前度和邻接定义可逐元核对。 | 已清楚；无。 |
| B11-296 离散最优与谱下界差距 | 1786–1798，“1…不等于…2−sqrt2”；`sec:graph-theory-spectrum-discrete-symmetry` | 防止把求谱当已解离散优化。 | f=(1,1,−1,−1)、显式u2 | 原候选有限，可手枚举7个二分。 | 已清楚；无。 |
| B11-297 同分组但不同几何 | 1800–1812，“特征方程、向量幅度和下界不同”；`sec:graph-theory-spectrum-discrete-symmetry` | 比较RatioCut与NCut避免只看标签。 | 2/3对1/2，y=(1,1/2,−1/2,−1) | 与上一组1对2−sqrt2不同。 | 已清楚；无。 |
| B11-298 显示归一化与任务归一化 | 1817–1820，“欧氏范数2…不替代”；`sec:graph-theory-spectrum-discrete-symmetry` | 解释图上振幅缩放不改变任务定义。 | `fig:graph-theory-spectral-coordinates`全图注 | 离散横轴连线仅阅读引导。 | 图注支持比较；未做PDF视觉验收。 |
| B11-299 谱隙与方向稳定性 | 1824–1825，“间隔很小…明显旋转”；`sec:graph-theory-spectrum-discrete-symmetry` | 提醒取整后的方向易受数据扰动影响。 | 第6章2842–2904含完整界及二维算例已实读 | 特征值稳定不等于特征向量稳定。 | 已回顾；无。 |
| B11-300 重特征子空间 | 1826–1827，“不能把任意单个基向量”；`sec:graph-theory-spectrum-discrete-symmetry` | 保留有辨认意义的稳定对象。 | 第6章2906–2939子空间界及旋转例 | 需与其余谱分离，不假定簇内基唯一。 | 已回顾；无。 |
| B11-301 连续域目标延拓 | 1831–1833，“必须说明…目标怎样定义”；`sec:graph-theory-exact-approximate-algorithms` | 引入离散松弛的下一层条件。 | 仅把二值改区间不足的提醒 | 是新节引入；后续B11-302至305已核对正式条件。 | 预告与展开相符；无。 |

本段另全文核对`reader-revision-graph/chordal-cycle.tex`1–22、`flow-cut-certificate.tex`1–20、`matching-augmentation.tex`1–23、`binary-energy-cut.tex`1–16；节点、方向、容量与已选边均符合对应图注。`spectral-coordinates.pdf`仅随正文完整读其解释与解析数值，未作PDF图形视觉判断。

## 松弛、图信号与扩散

节标签：`sec:graph-theory-exact-approximate-algorithms`、`sec:graph-theory-functions-propagation`、`sec:graph-theory-vertex-functions`、`sec:graph-theory-structure-comparison`、`sec:signal-analysis-graph-state-kernels`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-302 扩大的可行集 | 1834–1835，“Z̃⊇Z”；`sec:graph-theory-exact-approximate-algorithms` | 给松弛下界的集合条件。 | 原离散点全部保留 | 不是任意连续问题都叫原问题松弛。 | 已清楚；无。 |
| B11-303 一致目标延拓 | 1835–1838，“离散点上…相等”；`sec:graph-theory-exact-approximate-algorithms` | 保证扩大域后仍比较同一原目标。 | 显式Ẽ(z)=E(z) | 不同延拓可以给不同下界。 | 已清楚；无。 |
| B11-304 松弛下界 | 1839–1846，“inf…≤…min”；`sec:graph-theory-exact-approximate-algorithms` | 用较大范围限制最优可改善空间。 | L_relax不等式 | 未达下确界也有数值下界，但算法求得值另核对。 | 已清楚；无。 |
| B11-305 松弛精确性证书 | 1847，“最优解属于原可行集”；`sec:graph-theory-exact-approximate-algorithms` | 指出何时不需恢复近似方案。 | 同值可行点夹住最优值 | 须真正达到松弛最优，不是任一整数候选。 | 已清楚；无。 |
| B11-306 取整 | 1848、1858，“分数解…还需要”；`sec:graph-theory-exact-approximate-algorithms` | 将连续候选恢复为离散方案。 | 1/2阈值 | 取整不自动保全局约束。 | 已清楚；无。 |
| B11-307 局部搜索预告 | 1848，“取整、局部搜索”；`sec:graph-theory-exact-approximate-algorithms` | 提示改善离散候选的方法。 | 第2章一交换局部最优反例已补读 | 此处没有算法或保证，仅预告。 | 不据此认定已解全局问题；无。 |
| B11-308 分支定界预告 | 1848，“或分支定界”；`sec:graph-theory-exact-approximate-algorithms` | 提示另一个后续精确求解方向。 | 未给步骤，未用于本段推导 | 纯名称预告，不是当前必须执行的工具。 | 可选补一句分支与界剪除的含义；非实质问题。 |
| B11-309 可行方案上界U | 1850–1854，“E(ẑ)”；`sec:graph-theory-exact-approximate-algorithms` | 用已经实现的目标给原最优值上界。 | 0≤U−E*≤U−L | 先检查ẑ原问题可行。 | 已清楚；无。 |
| B11-310 证书差距U−L | 1853–1855，“不是实际误差”；`sec:graph-theory-exact-approximate-algorithms` | 正确解释数值质量报告。 | 下界紧才等于真实次优差距 | 不把松弛差距当实际误差。 | 已清楚；无。 |
| B11-311 连续可行值与有效下界 | 1856–1857，“通常…上界”；`sec:graph-theory-exact-approximate-algorithms` | 防止把未求准的松弛候选当下界。 | 对偶证书／误差控制提示 | 连续求解器下降不等于原离散最优证书。 | 已清楚；无。 |
| B11-312 取整后的可行性 | 1858–1859，“总数、连通”；`sec:graph-theory-exact-approximate-algorithms` | 说明逐坐标合法仍可能整体违规。 | 两类全局约束具体举出 | 未经可行检查，U也不成立。 | 已清楚；无。 |
| B11-313 随机取整的随机性与修复 | 1861–1862，“期望对哪种随机性”；`sec:graph-theory-exact-approximate-algorithms` | 区分随机输出与逐实例保证。 | 明确需计修复可行代价 | 没给具体随机算法，属于质量要求。 | 已清楚；无。 |
| B11-314 乘法近似比 | 1862–1863，“U≤αE*”；`sec:graph-theory-exact-approximate-algorithms` | 固定正最优目标下的相对保证。 | 第2章1011–1029已实读 | 最小化α应≥1，前章口径明确。 | 已回顾；无。 |
| B11-315 加法误差 | 1863–1865，“U−E*≤ε”；`sec:graph-theory-exact-approximate-algorithms` | 处理零值或负目标的更稳妥口径。 | 与乘法并列比较 | 运行快、连续下降与离散最优不同。 | 已回顾；无。 |
| B11-316 顶点函数定义域 | 1870–1875，“f:V→R”；`sec:graph-theory-functions-propagation` | 分清每点一个数的处理对象。 | 四顶点只需四个值 | 邻居汇总改变顶点信号。 | 已正式展开；无。 |
| B11-317 配置函数定义域预告 | 1872–1875，“四个二值…16种”；`sec:graph-theory-functions-propagation` | 预先阻止将消息与信号相混。 | 乘积配置空间 | 实际定义与运算在2163行后展开。 | 预告清楚；无。 |
| B11-318 图信号 | 1888–1892，“每个顶点一个数”；`sec:signal-analysis-graph-state-kernels` | 为一般图定义适合连接结构的数值坐标。 | 温度、得分；一般图无唯一下一点 | 不预设下一章规则傅里叶知识。 | 已清楚；无。 |
| B11-319 顶点离散标记 | 1881–1883，“未必有加法”；`sec:graph-theory-vertex-functions` | 为后邻域细化分出非数值对象。 | 类别／局部结构类型 | 不能自动线性叠加。 | 预告清楚；无。 |
| B11-320 图傅里叶变换 | 1901–1908，“Uᵀf”；`sec:signal-analysis-graph-state-kernels` | 将信号写成拉普拉斯模态坐标。 | `def:signal-analysis-graph-fourier-transform` | 实正交基，当前无向非负权图已限定。 | 已清楚；无。 |
| B11-321 图傅里叶逆变换 | 1907、1912，“f=Uf̂”；`sec:signal-analysis-graph-state-kernels` | 说明坐标改变可完整恢复原信号。 | UᵀU=I | 不是压缩或截断。 | 已清楚；无。 |
| B11-322 系数平方和守恒 | 1912–1914，“‖f‖²=Σ…²”；`sec:signal-analysis-graph-state-kernels` | 核对正交换基不改长度。 | Parseval型等式直接给出 | 第6章正交几何已读，不需连续傅里叶定理。 | 已回顾；无。 |
| B11-323 图频率尺度 | 1915–1919，“小…变化较小”；`sec:signal-analysis-graph-state-kernels` | 用能量解释特征值为何称频率。 | Σλ_k\|f̂_k\|² | 与规则时间每秒振荡次数不是同一自动单位。 | 已清楚；无。 |
| B11-324 重谱坐标与投影不变量 | 1920–1922，“单个坐标…投影…不变”；`sec:signal-analysis-graph-state-kernels` | 限制频率向量唯一性的说法。 | 重空间正交旋转与简单特征向量符号自由 | 能量属于特征空间，不固定某基名。 | 已清楚；无。 |
| B11-325 环图的模N索引 | 1924–1929，“左右邻居”；`sec:signal-analysis-graph-state-kernels` | 建立规则序列与一般图的具体桥接。 | N≥3、r=0,…,N−1 | k采用复指数顺序，非升序谱号。 | 已清楚；无。 |
| B11-326 环图复指数模态 | 1931，“N^−1/2 exp…”；`sec:signal-analysis-graph-state-kernels` | 给可直接代入的显式基。 | 复指数、单位归一化 | 基础复数和有限和足够，无须预先学DFT。 | 已清楚；无。 |
| B11-327 环图模态特征值 | 1932–1936，“2−2cos(2πk/N)”；`sec:signal-analysis-graph-state-kernels` | 验证模态确是L特征向量。 | 两邻居相位求和 | k与N−k同值稍后解释。 | 已清楚；无。 |
| B11-328 有限几何和正交性 | 1937–1939，“否则为0”；`sec:signal-analysis-graph-state-kernels` | 证明这些模式足够且彼此正交。 | 非平凡单位根有限和 | 本科有限等比和工具适用。 | 已清楚；无。 |
| B11-329 复酉变换与DFT预告 | 1940–1942，“U*…不能…转置”；`sec:signal-analysis-graph-state-kernels` | 正确处理复基，并接到下一章。 | 正交性刚直接证明 | DFT只是后文命名，不作本处前提。 | 已清楚；无。 |
| B11-330 N=2环公式边界 | 1943，“左右邻居重合”；`sec:signal-analysis-graph-state-kernels` | 防止简单图度数被重复计两次。 | 单边图非度2环 | 与默认简单图相容。 | 已清楚；无。 |
| B11-331 跨图谱坐标可比性 | 1945–1948，“没有天然相同的物理频率”；`sec:signal-analysis-graph-state-kernels` | 限制按序号拼接不同图的系数。 | 环中反方向重谱、一般图依赖权重 | 需共同图构造或子空间语义。 | 已清楚；无。 |
| B11-332 标量谱响应g | 1950–1955，“放大或缩小不同模态”；`sec:signal-analysis-graph-state-kernels` | 定义频率选择性处理。 | ŷ_k=g(λ_k)f̂_k | 第6章矩阵谱函数已实际补读。 | 已清楚；无。 |
| B11-333 谱滤波的基选择不变性 | 1956–1957，“相同特征值…相同”；`sec:signal-analysis-graph-state-kernels` | 保证g(L)由算子而非任意基决定。 | 重特征空间整块乘同标量 | 随意逐基加权不是同一标量函数。 | 已清楚；无。 |
| B11-334 多项式图滤波 | 1959–1968，“Σα_r L^r”；`sec:signal-analysis-graph-state-kernels` | 无需谱分解即可执行响应。 | `eq:graph-theory-polynomial-filter`与信号式 | 矩阵幂为复合作用，非逐元幂。 | 已清楚；无。 |
| B11-335 K跳局部性 | 1969–1971，“至多r步…对角…停留”；`sec:signal-analysis-graph-state-kernels` | 把多项式阶数变成依赖范围。 | 矩阵乘法逐项路径归纳 | 距离超过K必为零，不逆推范围内非零。 | 已清楚；无。 |
| B11-336 滤波系数相消 | 1972–1973，“可能相消”；`sec:signal-analysis-graph-state-kernels` | 区分最大可能范围与实际响应支撑。 | 多项式权重带符号可抵消 | 不声称恰好每个K跳点都收到值。 | 已清楚；无。 |
| B11-337 稀疏局部计算成本 | 1974–1975，“每步O(V+E₊)”；`sec:signal-analysis-graph-state-kernels` | 解释为何不必显式对角化。 | 反复稀疏矩阵向量乘 | 依赖给定系数和稀疏图表示。 | 已清楚；无。 |
| B11-338 三点一跳与两跳算例 | 1977–2004，“第三点才收到非零值”；`sec:signal-analysis-graph-state-kernels` | 同时核对谱响应和空间依赖。 | Hf=(2/3,1/3,0)，H²f=(5/9,1/3,1/9)及图 | 谱0,1,3响应1,2/3,0；数值可手算。 | 已清楚；无。 |
| B11-339 图卷积名称及边界 | 2008–2010，“有时也称…没有…唯一…平移”；`sec:signal-analysis-graph-state-kernels` | 说明常见名称不等于规则网格操作。 | 多项式函数依赖当前图 | 普通卷积仅比较预告，未用未定义公式推导。 | 已清楚；无。 |
| B11-340 置换等变性 | 2012–2030，“结果…同步重排”；`sec:signal-analysis-graph-state-kernels` | 检查任意顶点编号不改变运算语义。 | `eq:graph-theory-laplacian-relabel`及PᵀP消去 | 第7章群作用、等变定义已完整读。 | 已清楚；无。 |
| B11-341 对称读出的图级不变性 | 2031–2032，“对顶点求和”；`sec:signal-analysis-graph-state-kernels` | 从顶点表示构造编号无关摘要。 | 求和例 | 不变不保证非同构图可区分。 | 已清楚；无。 |
| B11-342 图热方程 | 2034–2041，“按邻居与自身的差调整”；`sec:signal-analysis-graph-state-kernels` | 将反复局部作用改为连续时间动力学。 | `eq:graph-theory-heat-equation` | f′=−Lf，不与流网络容量守恒混同。 | 已清楚；无。 |
| B11-343 矩阵指数扩散解 | 2042–2047，“e^(−tL)f₀”；`sec:signal-analysis-graph-state-kernels` | 由已学线性ODE求显式状态。 | 谱展开式；第6章736–773、1613–1670已核对 | 不是逐元素指数。 | 已回顾；无。 |
| B11-344 模态衰减率 | 2048，“大特征值…更快”；`sec:signal-analysis-graph-state-kernels` | 解释扩散的低频保留。 | e^(−tλ)、零模保持 | 全部λ非负来自前证能量。 | 已清楚；无。 |
| B11-345 分量平均极限 | 2049–2052，“各自的初始平均”；`sec:signal-analysis-graph-state-kernels` | 说明长期状态不是任意常量。 | 指示单位向量投影算式 | 只有正权支撑连通才全图同平均。 | 已清楚；无。 |
| B11-346 顶点总和守恒 | 2054–2058，“1ᵀL=0”；`sec:signal-analysis-graph-state-kernels` | 不经对角化核对扩散保存什么。 | d(1ᵀf)/dt=0 | 不保证每个点数值不变。 | 已清楚；无。 |
| B11-347 平方范数耗散 | 2059–2064，“−fᵀLf”；`sec:signal-analysis-graph-state-kernels` | 给整体幅度变化的精确关系。 | 半范数平方导数 | 与Dirichlet边差能量不是同一对象。 | 已清楚；无。 |
| B11-348 Dirichlet能量耗散 | 2065–2073，“−2‖Lf‖²”；`sec:signal-analysis-graph-state-kernels` | 证明全图总边差随时间不增。 | 完整乘积求导 | 不推出每条边分别的差值都单调。 | 公式清楚；2090行范围另见R1-B-043。 |
| B11-349 四点扩散的零模保留 | 2075–2087，“极限…1/4”；`sec:signal-analysis-graph-state-kernels` | 用具体谱纠正全部衰减归零的误解。 | 谱0,2,4,4及解析图注 | 重谱两方向同速，总和1。 | 已清楚；无。 |
| B11-350 指数传播与固定跳数 | 2089，“不是固定低阶多项式”；`sec:signal-analysis-graph-state-kernels` | 限制前面的K跳结论。 | 指数包含不限次数的矩阵幂 | 有限图可另插值，但不能套固定低阶局部范围。 | 已清楚；无。 |
| B11-351 扩散平滑的逐边表述 | 2090，“使相邻值更接近”；`sec:signal-analysis-graph-state-kernels` | 试图解释耗散与任务边界的关系。 | 前面只证明总能量下降 | 相等邻点也可能因其他邻居影响而分开。 | 技术疑点R1-B-043；改“总边差能量不增”，不声称逐边单调。 |
| B11-352 长时过度平滑 | 2090–2091，“抹去…全部非恒定差异”；`sec:signal-analysis-graph-state-kernels` | 指明数值平滑未必保任务类别边界。 | 分量平均极限已证 | 收敛不等于预测有用。 | 已清楚；无。 |
| B11-353 离散与连续Dirichlet对应 | 2093–2103，“形式相似不构成收敛定理”；`sec:signal-analysis-graph-state-kernels` | 把图能量接到第7章但限制推广。 | 连续∫‖grad f‖² dV、采样尺度与密度警示 | 核带宽、边界与归一化决定极限，不自动是Laplace–Beltrami。 | 已清楚；无。 |

## 邻域标记细化

节标签：`sec:graph-theory-vertex-functions`、`sec:graph-theory-structure-comparison`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-354 多重集合 | 2107–2110，“保留种类与次数、忽略排列”；`sec:graph-theory-vertex-functions` | 不丢邻居计数又不依赖编号顺序。 | {a,a,b}对{a,b} | 普通集合丢重数，有序表保多余次序。 | 已清楚；无。 |
| B11-355 一维WL细化 | 2112–2120，“自身旧标记…邻居…多重集合”；`sec:graph-theory-vertex-functions` | 用局部结构更新离散类型。 | `eq:graph-theory-wl-refinement` | 同步更新，无数值相加假设。 | 已清楚；无。 |
| B11-356 无碰撞数学编码 | 2122–2125，“不同输入对…不同新标记”；`sec:graph-theory-vertex-functions` | 让相异邻域一定分开。 | HASH定义与有限哈希边界 | 不把理论单射当工程哈希永无碰撞。 | 已清楚；无。 |
| B11-357 两图共享编码 | 2126–2127，“不交并上统一编码”；`sec:graph-theory-vertex-functions` | 使标签字面比较有相同含义。 | 两图共同初始规则 | 不能各自任意命名再比字符串。 | 已清楚；无。 |
| B11-358 WL等变与计数不变 | 2128–2129，“每轮…同步重排”；`sec:graph-theory-vertex-functions` | 验证该结构摘要不取决于编号。 | 同构重排邻域、多重集合不变 | 当前无向无边属性版本；扩展不能丢方向。 | 已清楚；无。 |
| B11-359 标记分区P^(t) | 2131–2133，“只能细分，不能合并”；`sec:graph-theory-vertex-functions` | 定义过程进度，不盯标签名称。 | 旧标记进入HASH保证区分保留 | 与每轮符号换名不同。 | 已清楚；无。 |
| B11-360 严格细分次数界 | 2134–2135，“至多n−1次”；`sec:graph-theory-vertex-functions` | 证明有限图不会无限产生新分组。 | 每次块数至少加1且最多n块 | 不等于标签字符串必在n轮固定。 | 已清楚；无。 |
| B11-361 分区稳定后持续稳定 | 2136–2138，“各旧块邻居计数”；`sec:graph-theory-vertex-functions` | 排除停一轮后又继续分裂。 | 同块计数一致、统一重命名归纳 | 稳定对象是等价类。 | 已清楚；无。 |
| B11-362 1-WL的不可区分反例 | 2140–2151，“六环…两个…三角形”；`sec:graph-theory-vertex-functions` | 说明稳定与同构判定不同。 | 每点两个同标记邻居、图源完整核对 | 连通性本可遍历求出，只是此摘要漏掉。 | 已清楚；无。 |
| B11-363 唯一编号作为额外属性 | 2154–2156，“问题已变成带属性图”；`sec:graph-theory-vertex-functions` | 阻止用任意ID掩盖区分能力不足。 | 重赋编号与随置换搬属性两情况 | 等变性与问题语义分别核对。 | 已清楚；无。 |
| B11-364 图网络表达能力预告 | 2157–2158，“依据函数族证明”；`sec:graph-theory-vertex-functions` | 限定WL与神经网络比较的后续任务。 | 无具体网络定理，准确标后续 | 等变、完全可辨、泛化不是同一保证。 | 预告清楚；无。 |

## 配置查询与半环

节标签：`sec:graph-theory-semiring-dynamic-programming`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-365 变量有限非空状态域 | 2163–2164，“Z_i…非空有限”；`sec:graph-theory-semiring-dynamic-programming` | 给可枚举查询和极值见证定基础。 | 二值贯穿例 | 不自动推广到连续变量。 | 已清楚；无。 |
| B11-366 配置函数F | 2165–2167，“评价…一次完整赋值”；`sec:graph-theory-semiring-dynamic-programming` | 把定义域从顶点改为变量乘积空间。 | 前述四变量16态 | 图只记局部作用域，不决定查询输出。 | 已清楚；无。 |
| B11-367 总权重查询 | 2171–2183，“Σg=10”；`sec:graph-theory-semiring-dynamic-programming` | 先用小表建立跨配置求和语义。 | 1,3／2,4完整表 | 不等于最佳值或概率，尚未归一化。 | 已清楚；无。 |
| B11-368 最佳权重与见证 | 2182–2184，“max=4…(1,1)”；`sec:graph-theory-semiring-dynamic-programming` | 分清最优数值与达到它的配置。 | 同一四项表 | 后续须保存选择才能恢复见证。 | 已清楚；无。 |
| B11-369 最低成本查询 | 2185–2186，“1…(0,0)”；`sec:graph-theory-semiring-dynamic-programming` | 展示同表不同含义得不同答案。 | 把数字解释为成本 | 不能由关系图决定最小还是最大。 | 已清楚；无。 |
| B11-370 保留变量的查询表 | 2188–2190，“m(0)=3,m(1)=7”；`sec:graph-theory-semiring-dynamic-programming` | 区分部分汇总与最终标量。 | 保留y后再汇总得10 | 消元不等于删除约束。 | 已清楚；无。 |
| B11-371 边缘概率与条件最优表 | 2191–2193，“g/10…m/10”；`sec:graph-theory-semiring-dynamic-programming` | 防止把任意求和或最大表称概率。 | max表为(2,4) | 只有正总权重归一化后和表才是边缘概率。 | 已清楚；无。 |
| B11-372 配置内组合⊗ | 2195–2197，“固定配置组合局部项”；`sec:graph-theory-semiring-dynamic-programming` | 把多个局部评价合成一个配置值。 | 权重相乘、成本相加 | 不与跨配置汇总混同。 | 已清楚；无。 |
| B11-373 配置间汇总⊕ | 2195–2197，“跨不同配置”；`sec:graph-theory-semiring-dynamic-programming` | 指定求和、择优或可行性等查询。 | 权重加和、成本取最小 | 更换此操作会改变问题。 | 已清楚；无。 |
| B11-374 交换半环 | 2199–2205，“一个集合、两种运算”；`sec:graph-theory-semiring-dynamic-programming` | 为统一消元证明列出足够代数条件。 | `def:graph-theory-semiring` | 不靠“普通加乘都能推广”的直觉。 | 已清楚；无。 |
| B11-375 结合律 | 2206，“分别结合”；`sec:graph-theory-semiring-dynamic-programming` | 允许局部合并时改变括号。 | 后面消元按因子分组 | 未允许跨不同运算任意交换。 | 已清楚；无。 |
| B11-376 交换律 | 2206，“且交换”；`sec:graph-theory-semiring-dynamic-programming` | 允许同类有限汇总换次序及因子重排。 | 后消元不变量证明 | 这是本章交换半环假设，不声称所有代数都满足。 | 已清楚；无。 |
| B11-377 单位元及空运算 | 2206、2211，“空汇总…空组合”；`sec:graph-theory-semiring-dynamic-programming` | 处理叶消息和空因子集。 | e_⊕与e_⊗分别定义 | 求和空值与乘积空值不能混用。 | 已清楚；无。 |
| B11-378 分配律 | 2208，“a⊗(b⊕c)”；`sec:graph-theory-semiring-dynamic-programming` | 支撑不依赖被消变量的项外提。 | 显式分配式与2197白话 | 这是查询保持的关键，不由图形本身保证。 | 已清楚；无。 |
| B11-379 吸收元 | 2209，“a⊗e_⊕=e_⊕”；`sec:graph-theory-semiring-dynamic-programming` | 使不可行或零贡献组合保持无贡献。 | 后max积0与min加∞ | 不等于组合单位元。 | 已清楚；无。 |
| B11-380 不要求逆元 | 2214，“不需减法和除法”；`sec:graph-theory-semiring-dynamic-programming` | 区分半环与熟悉实数域。 | 布尔和最小加法实例 | 归一化是查询之后另加步骤。 | 已清楚；无。 |
| B11-381 和积半环 | 2219，“非负实数、+、×”；`sec:graph-theory-semiring-dynamic-programming` | 累计总权重。 | 单位元(0,1) | 非负条件连接概率解释与Tonelli边界。 | 已清楚；无。 |
| B11-382 最大积半环 | 2220、2226，“max、×”；`sec:graph-theory-semiring-dynamic-programming` | 选最大非负组合权重。 | 0既为max单位又为乘法吸收 | 不允许任意负权仍沿用单调分配。 | 已清楚；无。 |
| B11-383 最小加法半环 | 2221、2227，“min、+”；`sec:graph-theory-semiring-dynamic-programming` | 以加总成本表示最优查询。 | (+∞,0)、∞+c=∞ | 正无穷表不可行，不引入未定义∞−∞。 | 已清楚；无。 |
| B11-384 布尔半环 | 2222–2223，“或、且”；`sec:graph-theory-semiring-dynamic-programming` | 汇总是否存在可行配置。 | false／true的两个单位元 | 数值计数与逻辑存在不同。 | 已清楚；无。 |
| B11-385 对数域最大加法 | 2228–2229，“max,+,−∞,0”；`sec:graph-theory-semiring-dynamic-programming` | 连接乘积权重与对数表示。 | −∞吸收约定 | 与负对数后的最小加法方向不同。 | 已清楚；无。 |
| B11-386 一元与成对因子分解 | 2231–2237，“⊗_i φ_i…⊗_E φ_i,j”；`sec:graph-theory-semiring-dynamic-programming` | 将全配置评价拆为局部作用域。 | `eq:graph-theory-factorized-objective` | 因子是函数，不是图边本身。 | 已清楚；无。 |
| B11-387 一般高阶因子作用域 | 2238–2242，“仍须保留φ_2,3,4”；`sec:graph-theory-semiring-dynamic-programming` | 防止关系三角形丢失三元约束。 | 任意S_a形式 | 成对公式明确仅专门情形。 | 已清楚；无。 |
| B11-388 输出变量查询Q及总权重Z | 2244–2248，“保留z4”；`sec:graph-theory-semiring-dynamic-programming` | 定义部分查询与全汇总的联系。 | Q(z4)=Σ前三变量，Z=ΣQ | 后算法可在保留变量处停止。 | 已清楚；无。 |
| B11-389 配置分布归一化条件 | 2249–2250，“0<Z<∞”；`sec:graph-theory-semiring-dynamic-programming` | 说明何时F/Z才是分布。 | Q/Z边缘 | 零总权重不能除，有限状态不代替正性。 | 已清楚；无。 |
| B11-390 成本查询更换两运算 | 2251–2252，“同时更换组合和汇总”；`sec:graph-theory-semiring-dynamic-programming` | 防止只改外层max/min而保留错误乘法。 | min[Σ一元成本+Σ成对成本] | 图不自带概率、因果、时间语义。 | 已清楚；无。 |

## 变量消元与见证恢复

节标签：`sec:graph-theory-semiring-dynamic-programming`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-391 当前因子桶F_i | 2258，“全部含z_i”；`sec:graph-theory-semiring-dynamic-programming` | 定义一次消元必须处理哪些项。 | 含i／不含i两类 | 必须是当前因子，含此前生成表。 | 已清楚；无。 |
| B11-392 剩余接口R_i | 2258–2259，“合并…去掉i”；`sec:graph-theory-semiring-dynamic-programming` | 指定生成表的全部自变量。 | 与结构剩余邻域一致 | 不仅原始邻居；填充可扩大接口。 | 已清楚；无。 |
| B11-393 新因子ψ_i | 2260–2265，“对每个…接口值…全部贡献”；`sec:graph-theory-semiring-dynamic-programming` | 用局部汇总代替内部变量。 | ⊕_zi⊗桶内因子 | 不是把变量约束丢弃。 | 已清楚；无。 |
| B11-394 因子替换操作 | 2264，“删去…以ψ_i替换”；`sec:graph-theory-semiring-dynamic-programming` | 防止新旧局部贡献重复计算。 | 其他因子保持不动 | 数值与作用域一起替换。 | 已清楚；无。 |
| B11-395 半环变量消除正确性 | 2276–2283，“等于直接枚举”；`sec:graph-theory-semiring-dynamic-programming` | 证明局部算法保持指定查询。 | `thm:graph-theory-semiring-elimination`全证明 | 有限取值、有限因子、交换半环三条件。 | 已清楚；无。 |
| B11-396 逐剩余配置不变量 | 2285–2288，“当前组合等于…已消变量汇总”；`sec:graph-theory-semiring-dynamic-programming` | 强化只保全局值的证明以支持部分输出。 | 初始无已消变量 | 不只证明最后标量碰巧相等。 | 已清楚；无。 |
| B11-397 分配外提与有限换序 | 2290–2314，“不含它…移到…外”；`sec:graph-theory-semiring-dynamic-programming` | 完成每一步不变量保持。 | 全公式及归纳到标量 | 用结合、交换、分配各有明确位置。 | 全证明可跟随；无。 |
| B11-398 保留变量时提前停止 | 2282、2314，“逐个输出配置”；`sec:graph-theory-semiring-dynamic-programming` | 得到函数表而非仅一个数。 | 强不变量直接推出 | 不把未消变量随意赋默认值。 | 已清楚；无。 |
| B11-399 次序正确性与成本差异 | 2317–2320，“任意次序…成本却不同”；`sec:graph-theory-semiring-dynamic-programming` | 接回树宽及填充分析。 | 接口{2,3}对{1,3,4} | 同一查询相同，运行资源不相同。 | 已清楚；无。 |
| B11-400 条件最优选择记录 | 2328–2329，“每个接口配置保存…z_i”；`sec:graph-theory-semiring-dynamic-programming` | 弥补只存最优值无法恢复方案。 | 达到最大值的有限状态见证 | 与和积消息无需选择指针不同。 | 已清楚；无。 |
| B11-401 逆消元回溯 | 2329–2332，“用已知接口值查回”；`sec:graph-theory-semiring-dynamic-programming` | 恢复相互一致的全局配置。 | 每步条件选择达到记录值的归纳 | 不能独立拼接各变量无条件最优。 | 已清楚；无。 |
| B11-402 并列最优处理 | 2332–2333，“固定平局…任意一个…全部”；`sec:graph-theory-semiring-dynamic-programming` | 说明输出约定与规模。 | 全部见证可很大 | 最优值唯一不意味着配置唯一。 | 已清楚；无。 |
| B11-403 最小加法回溯与不可行 | 2335–2340，“+∞…没有有限成本”；`sec:graph-theory-semiring-dynamic-programming` | 对成本查询恢复同类见证并报告失败。 | minΣ及选择回溯 | 不将∞配置当有限成本可行解。 | 已清楚；无。 |
| B11-404 负对数转换 | 2341–2344，“乘积变和…反转大小”；`sec:graph-theory-semiring-dynamic-programming` | 将最大积改成最小加法。 | 正权、零映∞、普通log变max加 | 负权无直接实对数解释。 | 已清楚；无。 |
| B11-405 最大与求和换序反例 | 2346–2366，“4…8”；`sec:graph-theory-semiring-dynamic-programming` | 阻止把混合查询套到任意消元序。 | `eq:graph-theory-max-sum-order-a/b`，对角4表 | 是否允许x依赖y是决策信息差异。 | 已清楚；无。 |
| B11-406 max-sum的一般不等式 | 2367–2372，“≤”；`sec:graph-theory-semiring-dynamic-programming` | 为不同次序给准确比较方向。 | 固定x逐项≤再取max | 限有限实值表，避免不可达极值。 | 已清楚；无。 |
| B11-407 共同最优选择的等号条件 | 2373–2375，“每项都为零”；`sec:graph-theory-semiring-dynamic-programming` | 说明何时恰可无损交换。 | 逐项非负差和为零的必要性 | 不是每个y各有最优就够，需同一个x。 | 已清楚；无。 |
| B11-408 查询约束下的消元宽度 | 2377，“可能超过普通树宽”；`sec:graph-theory-semiring-dynamic-programming` | 解释最小结构宽度未必可执行。 | 混合汇总限制合法次序 | 先核运算合法，再优化次序。 | 已清楚；无。 |
| B11-409 边缘概率查询回顾 | 2378，“边缘概率”；`sec:graph-theory-semiring-dynamic-programming` | 将求和归一化目标与择优分开。 | 前面Q/Z | 第8章已建立边缘分布，当前仅回用。 | 已回顾；无。 |
| B11-410 最可能联合配置查询回顾 | 2378，“最可能联合配置”；`sec:graph-theory-semiring-dynamic-programming` | 对全部变量同时找一项最高权重见证。 | 前面M及回溯 | 不等于各边缘独立最大后拼接。 | 已清楚；无。 |
| B11-411 部分变量的边缘最大化 | 2378，“对部分变量…最大化”；`sec:graph-theory-semiring-dynamic-programming` | 先累计未关心变量再选关心变量。 | 紧邻max_x Σ_y=4实例 | 与Σ_y max_x=8不同，非同一种查询。 | 已清楚；无。 |
| B11-412 Tonelli换序边界 | 2379–2380，“σ有限…非负可测”；`sec:graph-theory-semiring-dynamic-programming` | 说明从有限表走向积分需额外分析。 | 第3章1719–1805已实际展开 | 允许∞不等于可归一化或有限表可执行。 | 已回顾；无。 |
| B11-413 Fubini换序边界 | 2381–2382，“绝对可积”；`sec:graph-theory-semiring-dynamic-programming` | 限制带符号累次积分改写。 | 前章完整声明、行列和0与1反例 | 只改求和符号不足以保证正确性。 | 已回顾；无。 |

## 树形消息与章末核对

节标签：`sec:graph-theory-semiring-dynamic-programming`、`sec:graph-theory-summary`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B11-414 接口消息 | 2386–2393，“m_1→{2,3}”；`sec:graph-theory-semiring-dynamic-programming` | 用固定接口复用消元结果。 | `eq:graph-theory-interface-message` | 表保留z2,z3，不是顶点信号的一个数。 | 已清楚；无。 |
| B11-415 两侧消息合并 | 2394–2397，“φ2,φ3,φ2,3”；`sec:graph-theory-semiring-dynamic-programming` | 示范左右内部变量各算一次后接接口。 | 三元因子完整纳入4侧 | 不重复计接口因子，也不丢高阶作用域。 | 已清楚；无。 |
| B11-416 消息合法性的代数依据 | 2399–2406，“直接原因是分配律”；`sec:graph-theory-semiring-dynamic-programming` | 分开图结构与运算条件。 | c(z2,z3)从z1汇总外提 | 看似可分块不能代替半环证明。 | 已清楚；无。 |
| B11-417 删边一侧子树T_(u\|v) | 2408–2409，“u侧连通分量”；`sec:graph-theory-semiring-dynamic-programming` | 定义消息所代表的全部内部变量。 | 树删边分两侧 | 不只是邻点u自身。 | 已清楚；无。 |
| B11-418 整侧消息语义 | 2410–2425，“唯一保留…z_v”；`sec:graph-theory-semiring-dynamic-programming` | 固定递推要等于哪个完整查询。 | `eq:graph-theory-tree-message-semantics` | 包括跨接口边φ_u,v，不漏边贡献。 | 已清楚；无。 |
| B11-419 树消息递推式 | 2427–2438，“邻居除v的入消息”；`sec:graph-theory-semiring-dynamic-programming` | 用较小子树表构造整侧汇总。 | `thm:graph-theory-tree-message-recursion` | 排除接收方v，避免沿同边立即重复。 | 已清楚；无。 |
| B11-420 叶消息基例 | 2441–2442，“空组合为单位元”；`sec:graph-theory-semiring-dynamic-programming` | 为递归启动给出确定数值规则。 | 对φ_u⊗φ_u,v汇总z_u | 回用半环空组合，不需特殊任意初始化。 | 已清楚；无。 |
| B11-421 子树不交的归纳证明 | 2443–2448，“每个…恰好一次”；`sec:graph-theory-semiring-dynamic-programming` | 保证消息合并不重复计项。 | 删除u后各子树无交无跨边 | 关键依赖树唯一路径，不适用原始有环图。 | 已清楚；无。 |
| B11-422 叶到根汇集 | 2451–2455，“Z=⊕根配置…”；`sec:graph-theory-semiring-dynamic-programming` | 从消息获得全局标量。 | 根一元乘所有入消息 | 未汇总根时仍为根查询表。 | 已清楚；无。 |
| B11-423 根向各枝回传 | 2456–2457，“每个顶点…全部入消息”；`sec:graph-theory-semiring-dynamic-programming` | 复用双向消息得到多点查询。 | 同一局部组合在不同点执行 | 不是对每个点重新全图枚举。 | 已清楚；无。 |
| B11-424 消息后归一化与回溯 | 2458，“仍遵循上一小节”；`sec:graph-theory-semiring-dynamic-programming` | 防止把消息本身当最终概率或配置。 | 正总权重与选择指针入口准确 | 和积与最优查询的后处理不同。 | 已清楚；无。 |
| B11-425 因子唯一分配到袋 | 2460–2462，“完整…只分配一次”；`sec:graph-theory-semiring-dynamic-programming` | 将树变量消息推广到一般图。 | 团入袋性质已完整证明 | 不能把一个高阶因子拆给两边或重复挂载。 | 已清楚；无。 |
| B11-426 袋内因子组合Φ_B | 2462，“袋B的因子组合”；`sec:graph-theory-semiring-dynamic-programming` | 汇聚唯一归属此袋的局部项。 | 后袋消息公式 | 袋可能没有原因子，空组合单位元可用。 | 已清楚；无。 |
| B11-427 袋接口S_(B,C) | 2463，“B∩C”；`sec:graph-theory-semiring-dynamic-programming` | 指定跨树边只保留哪些变量。 | 贯穿两袋共享{2,3} | 与原图边两端不同，是变量集合。 | 已清楚；无。 |
| B11-428 袋消息递推 | 2464–2472，“汇总B∖S”；`sec:graph-theory-semiring-dynamic-programming` | 用入消息和袋内项消掉非接口变量。 | 显式m_B→C公式 | 各入消息在自己交集取值，统一由袋配置指定。 | 已清楚；无。 |
| B11-429 运行交集的数值正确性 | 2473–2477，“两侧…必属于…接口”；`sec:graph-theory-semiring-dynamic-programming` | 完成结构条件到合法局部查询的桥接。 | 袋外变量分离；失效会各枝取不同值 | 不是仅有袋树就够。 | 已清楚；无。 |
| B11-430 袋消息的复杂度条件 | 2479–2485，“固定k,q…有效…才有”；`sec:graph-theory-semiring-dynamic-programming` | 给小树宽何时带来多项式保证。 | q^(k+1)、袋数与运算成本 | 找最优分解另算，宽度增长时保证不保留。 | 已清楚；无。 |
| B11-431 有环直接消息的重复计数 | 2487–2488，“经不同路线返回”；`sec:graph-theory-semiring-dynamic-programming` | 解释树公式直接搬回原图何处失证。 | 子树不交归纳失效 | 与先构造合法袋树再精确计算不同。 | 已清楚；无。 |
| B11-432 循环消息近似边界 | 2489–2491，“收敛…到什么…误差”；`sec:graph-theory-semiring-dynamic-programming` | 限定近似方法不能继承树上精确保证。 | 不给未证明收敛声明 | 消息、扩散和有限邻域传播不是同一计算。 | 已清楚；无。 |
| B11-433 章末条件与输出汇总 | 2496–2547，“关键条件…正确性依据”；`sec:graph-theory-summary` | 回答开篇关系、接口及查询问题。 | `tab:graph-algorithm-conditions`七行逐一核对 | 均是已建立概念，无突增结论；含完整表注。 | 已清楚；R1-B-041至043仍须局部修订。 |
| B11-434 规则索引信号的后续入口 | 2549–2551，“规则索引额外提供了什么”；`sec:graph-theory-summary` | 为下一章平移／卷积比较留出问题。 | 本章环图模式已直接建立 | 纯后续预告，不用下一章知识反向填缺。 | 衔接清楚；无。 |

最后图源核对：`reading-restructure/ch11/polynomial-locality.tex`1–34、`reader-revision-graph/wl-local-ambiguity.tex`1–20均全文读取，逐顶点数值、边和共同标记符合正文。`probability-discrete/graph-diffusion-spectrum.pdf`仅核对2082–2085行图注与正文谱0,2,4,4及平均值推导，未作PDF视觉验收。

全章自查：按顺序完成全部定义、证明、算例、正文图注和表，未仅按术语检索。图对象、结构改写、最优性、顶点函数与配置函数各有当地动机；除报告的三项实质问题外，不需用后文或研究生专门常识补齐主要推导。已读范围无遗漏，新增术语和非术语对象已逐项入表；读者任务之外的PDF视觉检查、主代理统一修订及修订后复读仍未执行。
