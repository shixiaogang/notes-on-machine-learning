# 第7章概念审读清单（独立读者B，第一轮）

## 版本与覆盖

- 源文件：`tex/01-mathematical-preliminaries/02-linear-algebra-and-geometry/02-differential-geometry-and-symmetry.tex`。
- 冻结 SHA-256：`6fe044e5c6f4e05193c3efbd069588e1b954a2e33271573c6e088e1ed7831d30`，开始审读及整章完成后实际校验均一致。
- 源文件共2072行。已逐段完整顺读1–2072行，包含全部证明、算例、表格和图注。后半章连续读取块为1026–1245、1246–1500、1501–1740、1741–1960、1961–2072；未跳过块内正文。
- 每张表的节标签与上述源路径共同适用于该表各行；位置为实际源行号，短引文供修订后定位。章首纯预告与正式建立的位置分开写。
- 读者背景：基础分析、线代、概率、组合；不预设拓扑、微分几何或研究生统计知识。“已回顾”不表示靠专家常识补读。

## 已核对的边界依赖

以下均实际展开阅读，而非只检索标题。路径以`tex/01-mathematical-preliminaries/`为前缀。

| 前章文件 | 实读范围 | 用途与核对结果 |
| --- | --- | --- |
| `01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex` | 108–138 | 等价关系、等价类、商集，支持轨道解释。 |
| `01-mathematical-language-combinatorics-analysis-optimization/03-mathematical-analysis.tex` | 225–248、343–422、610–757、848–893、1210–1304、1811–1855、2085–2138 | 零测例外、Cauchy与度量完备、连续性、紧致性、Jacobian与链式法则、隐函数定理完整证明、多元换元及极坐标实例、L^p等价类。紧致性已讲，但未找到同胚定义；不能用紧致标题替同胚补前提。逆函数结论可由已读隐函数定理取F(y,x)=H(x)-y得到，不把它冒充前文独立定理。 |
| `01-mathematical-language-combinatorics-analysis-optimization/04-optimization.tex` | 548–600、687–726、2099–2135 | 回溯的具体缩步与下降检验、Newton二次模型与不定风险、凸包定义和三点实例；未定义仿射独立。687–696是加速证明尾部，仅为读取上下文，不宣称完整核验该证明。 |
| `01-mathematical-language-combinatorics-analysis-optimization/05-functional-analysis-and-approximation.tex` | 309–483、1253–1322、1615–1670、1860–1946 | 弱导数、Sobolev空间与点值控制及其证明，线性泛函、Riesz表示及证明前段，有界算子伴随、积分算子伴随算例、函数方向导数与Fréchet梯度。没有把有界伴随定理直接外推到微分算子的形式伴随。 |
| `02-linear-algebra-and-geometry/01-linear-algebra-and-matrix-analysis.tex` | 61–116、145–185、260–310、345–406、461–480、627–653、1560–1615、2190–2308、2870–2942 | 商空间、数组张量与几何张量的预告性区分、对偶范数、正交投影、Gram矩阵、伴随和行列式体积、有限卷积窗口、谱定理完整证明、低秩近似完整证明、PCA、子空间扰动。第6章并无“对偶空间/对偶基”的正式建立，见B-004；几何张量只预告，见B-007。 |

## 距离坐标

节标签：`sec:geometry-distance-coordinate-embedding`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B07-001 平方距离矩阵 | 26–33，“精确保留这些距离”；`sec:geometry-distance-coordinate-embedding` | 由距离反求点；δ为欧氏距离平方，点按行排。 | `eq:geometry-distance-from-gram`、三点例 | 已回顾距离、范数；平方距离不是距离本身。 | 已清楚；无。 |
| B07-002 Gram矩阵 | 28–29，“记录两两内积”；`sec:geometry-distance-coordinate-embedding` | 把坐标问题变为矩阵问题；B=YYᵀ。 | 同上；第6章365–378 | 已回顾；本章按行，前章按列，公式已配合改变。 | 已清楚；无。 |
| B07-003 中心化矩阵J | 35–44，“固定平移自由度”；`sec:geometry-distance-coordinate-embedding` | 减去均值，J对称幂等且消去全一向量。 | `eq:geometry-centering-matrix` | 正交投影已回顾；不负责旋转。 | 已清楚；无。 |
| B07-004 双重中心化 | 50–57，“在两个点索引上消去均值项”；`sec:geometry-distance-coordinate-embedding` | 从平方距离恢复中心化内积。 | `eq:geometry-double-centering`及前两项消失的推导 | 与低维投影明确区分。 | 已清楚；无。 |
| B07-005 双重中心化的核 | 61–76，“排除…非零距离差”；`sec:geometry-distance-coordinate-embedding` | 对称H满足JHJ=0时只剩均值型项，零对角进一步迫零。 | `lem:geometry-double-centering-kernel`完整证明 | 矩阵核与零矩阵；这是重构充分性的证明工具。 | 已清楚；无。 |
| B07-006 半正定性 | 59–60，“任何真实坐标…都半正定”；`sec:geometry-distance-coordinate-embedding` | 检验矩阵能否来自内积；二次型非负。 | cᵀBc=‖Yᵀc‖² | 已回顾第6章；非负谱不等于元素全非负。 | 已清楚；无。 |
| B07-007 欧氏距离重构判据 | 79–105，“当且仅当B半正定”；`sec:geometry-distance-coordinate-embedding` | 判断给定对称零对角矩阵可实现性。 | `thm:geometry-euclidean-distance-embedding`完整双向证明 | 不预先假定输入必是合法距离；与近似重构分开。 | 已清楚；无。 |
| B07-008 最小欧氏实现维数 | 83–84，“r=rank(B)”；`sec:geometry-distance-coordinate-embedding` | 确定精确保距所需维数，含r=0。 | 103–105秩下界及达到构造 | 与流形局部维数不同。 | 已清楚；无。 |
| B07-009 谱坐标／经典尺度分析 | 90–108，“取Y=QΛ^{1/2}”；`sec:geometry-distance-coordinate-embedding` | 利用正谱显式恢复坐标。 | `eq:geometry-classical-scaling-coordinates`、三点例 | 谱定理已核对；坐标带噪与逐对距离误差明确区分。 | 已清楚；无。 |
| B07-010 正交不确定性与手性 | 113–138，“绝对位置、朝向或手性”；`sec:geometry-distance-coordinate-embedding` | 说明恢复结果为什么不唯一；旋转和反射均保距。 | 范数恒等式与M正交的完整论证 | 已回顾正交变换；手性可从反射说明理解。 | 已清楚；无。 |
| B07-011 Gram低秩近似 | 161–166，“Frobenius误差最小”；`sec:geometry-distance-coordinate-embedding` | 低维只能近似，需规定目标；PSD时尾特征值平方和。 | 第6章2197–2246；三点丢失竖直方向 | 与坐标误差及距离误差分开；负谱需PSD约束。 | 已清楚；无。 |
| B07-012 PCA坐标重构误差 | 163–164，“误差则为…λ_j”；`sec:geometry-distance-coordinate-embedding` | 同一次截断在坐标目标下误差不同。 | 第6章2264–2288；本章三点例 | 已回顾；Σλ与Σλ²比较清楚。 | 已清楚；无。 |
| B07-013 距离应力 | 164，“距离应力”；`sec:geometry-distance-coordinate-embedding` | 用于限制谱最优性的外推，但未说该量如何定义。 | 无公式或例 | 前1–6章检索未见该术语，不能据名称得知比较对象。 | 局部费力；B-001，补一个原始应力例或改普通描述。 |
| B07-014 最大相对距离误差 | 165，“最大相对距离误差”；`sec:geometry-distance-coordinate-embedding` | 另一类误差口径，不受谱目标直接保证。 | 无独立式 | 从通常相对误差可读，但重合点分母为零需约定。 | 局部费力；并入B-001，若保留需限定非零原距离。 |

## 局部坐标

节标签：`sec:geometry-local-coordinate-representation`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B07-015 流形 | 14预告；175–178，“每个点附近像…欧氏开集”；`chap:differential-geometry-and-symmetry` | 有限保距不能描述连续自由度；圆局部可定位、全局有断点。 | 单位圆双图例 | 与有限点集、全局一张坐标图区分。 | 已清楚；无。 |
| B07-016 光滑 | 178，“各阶导数连续”；`sec:geometry-local-coordinate-representation` | 明确本章正则性。 | 欧氏参数化 | 已回顾可微但本章明确强化至C∞。 | 已清楚；无。 |
| B07-017 微分同胚 | 178，“映射及其逆都光滑”；`sec:geometry-local-coordinate-representation` | 建立可逆局部拉直规则。 | `def:geometry-embedded-manifold` | 欧氏光滑映射已知，避免循环定义。 | 已清楚；无。 |
| B07-018 光滑嵌入流形 | 180–191，“把对象局部拉直”；`sec:geometry-local-coordinate-representation` | 环境开集经Ψ变换成为坐标平面；0≤d≤D。 | 正式定义与后续开带 | 不把自交参数曲线自动算嵌入。 | 已清楚；无。 |
| B07-019 局部参数化 | 193–197，“坐标到点”；`sec:geometry-local-coordinate-representation` | 从拉直映射得到φ，满列秩且像上有连续逆。 | φ=Ψ⁻¹(z,0) | 与反向读坐标图区别直接。 | 已清楚；无。 |
| B07-020 坐标图 | 199–202，“参数化的逆”；`sec:geometry-local-coordinate-representation` | 将点记为欧氏坐标。 | `def:geometry-chart-transition`、圆角度区间 | 不与参数化方向混同。 | 已清楚；无。 |
| B07-021 坐标过渡 | 203–206，“第一组坐标换成第二组”；`sec:geometry-local-coordinate-representation` | 拼接重叠坐标，域是交集坐标像。 | 圆上θ或θ+2π | 依赖可逆映射复合；方向已说明。 | 已清楚；无。 |
| B07-022 图册 | 207，“覆盖整个流形的一组坐标图”；`sec:geometry-local-coordinate-representation` | 一张图不够时覆盖全体。 | 单位圆两张图 | 与单图区别；不要求环境平直。 | 已清楚；无。 |
| B07-023 同胚 | 213，“不可能同胚于”；`sec:geometry-local-coordinate-representation` | 用于全局坐标不可能性及开带拉直；未当地定义。 | 213–215、232、590–591 | 前文连续与紧致已读，未见同胚；不能与微分同胚等同。 | 局部费力；B-002，补连续双射且逆连续。 |
| B07-024 紧致性的全局坐标障碍 | 213–215，“完整圆是紧集”；`sec:geometry-local-coordinate-representation` | 证明无一张无重复实坐标覆盖。 | 圆；第3章722–752 | 紧致已回顾；连续像紧致这一步未接出。 | 局部费力；B-002，接出像紧致而非空实开集不紧致。 |
| B07-025 局部维数 | 191，“前d个坐标…局部自由度”；`sec:geometry-local-coordinate-representation` | 数可独立改变的局部位置参数。 | 圆一维、开带二维 | 与环境维数区别已明示。 | 已清楚；无。 |
| B07-026 环境维数 | 191，“D只是容纳对象的环境维数”；`sec:geometry-local-coordinate-representation` | 区分记录长度与内在自由度。 | 圆在R² | 不由噪声自由度决定。 | 已清楚；无。 |
| B07-027 最小全局嵌入维数 | 214–215，“至少需要二维环境”；`sec:geometry-local-coordinate-representation` | 全局无自交也有约束。 | 圆不能无重复嵌入实直线 | 与前两种维数及有限保距维数不同。 | 已清楚；依B-002补拓扑依据即可。 |
| B07-028 弯曲点带Φ | 9预告；217–233，“s沿中心线定位”；`chap:differential-geometry-and-symmetry` | 贯穿比较对象，R>0、w<R、I长度<2πR。 | `eq:geometry-curved-strip-parameterization` | 二维开带不含端点，后文核对满秩。 | 已清楚；无。 |
| B07-029 中心线C | 10预告；229–241，“u_i=0”；`chap:differential-geometry-and-symmetry` | 同一公式限定横向参数得到一维对象。 | Φ(s,0) | 与二维开带、细窄点云分开。 | 已清楚；无。 |
| B07-030 潜在点p_i | 235–236，“误差发生前的真实位置”；`sec:geometry-local-coordinate-representation` | 明确要恢复什么。 | p_i=Φ(s_i,u_i) | 不是观测，也不是均值。 | 已清楚；无。 |
| B07-031 观测噪声模型x_i=p_i+ε_i | 237–241，“才是观测”；`sec:geometry-local-coordinate-representation` | 区分对象自由度和测量偏离。 | 开带小扰动与中心线一般扰动比较 | 未声称随机分布性质；无须预借第8章。 | 已清楚；无。 |

## 对称变换

节标签：`sec:geometry-group-invariance-equivariance`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B07-032 群 | 250–257，“可…施加、也可以撤销”；`sec:geometry-group-invariance-equivariance` | 规定可复合变换；封闭、结合、恒等、逆。 | 裁剪不可逆反例、SO(2) | 不把任意增强集合当群。 | 已清楚；无。 |
| B07-033 群作用 | 259–271，“先做g₂、再做g₁”；`sec:geometry-group-invariance-equivariance` | 连接抽象复合与实际对象操作。 | `eq:geometry-group-action` | 同群可作用不同对象；光滑要求额外给。 | 已清楚；无。 |
| B07-034 线性表示ρ | 273–286，“用线性算子实现…复合”；`sec:geometry-group-invariance-equivariance` | 向量输出保留线性组合。 | `eq:geometry-linear-representation` | 群作用未必线性；输入输出可取不同表示。 | 已清楚；无。 |
| B07-035 GL(V) | 277–282，“全部可逆线性算子组成的群”；`sec:geometry-group-invariance-equivariance` | 指定ρ的值域。 | 恒等和复合式 | 可逆线性算子已回顾。 | 已清楚；无。 |
| B07-036 平面旋转群SO(2) | 288–299，“行列式为1的二维正交矩阵”；`sec:geometry-group-invariance-equivariance` | 第一个可算连续变换群。 | `eq:geometry-planar-rotation-group` | 不含反射；内部参数可不变。 | 已清楚；无。 |
| B07-037 对称群S_n | 301，“全部置换”；`sec:geometry-group-invariance-equivariance` | 记录次序也是一种变换。 | 点云重排行 | 已回顾置换；不与几何旋转混同。 | 已清楚；无。 |
| B07-038 置换矩阵作用 | 302–306，“X_{π⁻¹(i),:}”；`sec:geometry-group-invariance-equivariance` | 规定复合顺序及行索引。 | P_{π₁π₂}=P_{π₁}P_{π₂} | 行作用与旋转列作用不同。 | 已清楚；无。 |
| B07-039 轨道 | 308–312，“从x出发能够得到的所有输入”；`sec:geometry-group-invariance-equivariance` | 明确哪些记录等价。 | 群三公理推等价关系 | 第1章等价类已核对。 | 已清楚；无。 |
| B07-040 轨道商X/G | 311，“轨道的集合”；`sec:geometry-group-invariance-equivariance` | 忽略某类变换的表示对象。 | SO(2)半径商例 | 与线性商空间不同，未默认光滑。 | 已清楚；无。 |
| B07-041 不变映射 | 314–326，“同一轨道上取相同值”；`sec:geometry-group-invariance-equivariance` | 输出要忽略变换时的条件。 | `eq:geometry-invariant-map`、范数 | 不变不保证区分不同轨道。 | 已清楚；无。 |
| B07-042 商映射与因子化 | 323–325，“f=…∘π”；`sec:geometry-group-invariance-equivariance` | 说明不变输出如何只读等价类。 | 代表元无关的说明 | 等价类已有；π非可逆坐标。 | 已清楚；无。 |
| B07-043 轨道商的奇异边界 | 328–332，“商可识别为[0,∞)”；`sec:geometry-group-invariance-equivariance` | 防止机械做维数相减。 | 原点轨道与圆轨道比较 | 无边界流形定义已有；非所有商都是流形。 | 已清楚；无。 |
| B07-044 等变映射 | 334–348，“按约定同步变化”；`sec:geometry-group-invariance-equivariance` | 朝向、位置输出不能不变。 | `eq:geometry-equivariant-map` | 输出作用不必线性；不变是另种输出要求。 | 已清楚；无。 |
| B07-045 逐点共享映射 | 350–359，“对每行使用同一个映射”；`sec:geometry-group-invariance-equivariance` | 给出置换等变的构造。 | 逐行三项等式 | 不自动保证信息完备。 | 已清楚；无。 |
| B07-046 不变汇总 | 348、357–359，“再对行求和”；`sec:geometry-group-invariance-equivariance` | 等变中间量转为不变输出。 | 求和顺序不影响值 | 不可从丢失的朝向反求方向。 | 已清楚；无。 |
| B07-047 平移算子T_a | 361–362，“f(x-a)”；`sec:geometry-group-invariance-equivariance` | 对函数而非点定义作用。 | 换元z=y-a | 全空间定义域不可遗漏。 | 已清楚；无。 |
| B07-048 连续卷积 | 363–374，“相乘并积分”；`sec:geometry-group-invariance-equivariance` | 验证一种等变算子；L¹保证a.e.。 | `eq:geometry-translation-convolution-equivariance` | 第6章有限互相关已读；本处明确连续卷积公式。 | 已清楚；无。 |
| B07-049 L¹及几乎处处 | 362、372，“等式几乎处处成立”；`sec:geometry-group-invariance-equivariance` | 限定卷积的存在口径。 | 第3章225–248、2085–2138 | 已回顾；逐点绝对收敛另列充分条件。 | 已清楚；无。 |
| B07-050 边界导致等变失效 | 373–374，“零填充、裁剪和下采样”；`sec:geometry-group-invariance-equivariance` | 防止把全空间恒等式搬到有限图像。 | `tab:geometry-invariance-equivariance` | 循环平移是不同作用。 | 已清楚；无。 |
| B07-051 有限群平均 | 397–414，“缺少直接的不变构造”；`sec:geometry-group-invariance-equivariance` | 对有限群逐变换平均。 | `thm:geometry-finite-group-average`完整证明 | 双射换索引；有限性明确。 | 已清楚；无。 |
| B07-052 紧拓扑群／紧群 | 415，“紧拓扑群可使用”；`sec:geometry-group-invariance-equivariance` | 从有限平均转为连续平均，群与拓扑兼容未说明。 | 无具体连续群积分例 | 已知SO(2)和紧致性，不足自行定义拓扑群。 | 局部费力；B-003，先给圆旋转均匀角积分。 |
| B07-053 Haar测度 | 415–416，“对群平移保持不变的概率测度”；`sec:geometry-group-invariance-equivariance` | 用积分代替群求和，说明左右不变。 | 仅指同样换元证明 | 概率总质量可懂，但存在性和左右条件以专门结论带过。 | 局部费力；B-003，连续例后标扩展结论及来源。 |
| B07-054 局部紧群上的非紧障碍 | 417–418，“没有有限的…均匀概率测度”；`sec:geometry-group-invariance-equivariance` | 限制对所有实平移平均。 | 无实轴平移反例计算 | “局部紧”未定义，且此结论并非有限证明直接推出。 | 局部费力；B-003，用等长区间的总质量矛盾作就地说明。 |
| B07-055 数据增强与结构恒等式 | 420–423，“只鼓励…近似关系”；`sec:geometry-group-invariance-equivariance` | 区分训练经验与构造保证。 | ±I平均把幅度也清零 | 平均不只消去指定差别；数值与边界仍需查。 | 已清楚；无。 |
| B07-056 旋转相对位置表示 | 425–442，“只通过相对位移出现”；`sec:geometry-group-invariance-equivariance` | 群复合编码位置差。 | `eq:geometry-rotary-relative-position`及点积式 | q、k作为给定向量；网络只预告，不借注意力原理。 | 已清楚；无。 |
| B07-057 频率周期与位置碰撞 | 437–441，“不能…无限长度无碰撞”；`sec:geometry-group-invariance-equivariance` | 限定相对位置公式的可辨认性。 | 单频周期2π/\|ω\| | 与网络整体是否绝对位置不变分开。 | 已清楚；无。 |

## 邻域与拓扑

节标签：`sec:geometry-local-relations-topology`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B07-058 拓扑 | 11–12预告；447–451，“连续连接与孔洞”；`chap:differential-geometry-and-symmetry` | 局部自由度不能确定整体结构。 | 两开弧、完整圆、开带 | 不保持长度角度；本节非一般拓扑公理教程。 | 已清楚；无。 |
| B07-059 连通分支 | 448，“两个连通分支”；`sec:geometry-local-relations-topology` | 比较对象分成几块。 | 两条互不相交开圆弧；β₀ | 直观足够本例，后文路径分支有专门范围。 | 已清楚；无。 |
| B07-060 不可收缩的环 | 448，“不可在圆内缩到点”；`sec:geometry-local-relations-topology` | 区分局部一维但整体不同对象。 | 完整圆与开弧 | 与边图的一圈和填充面随后区分。 | 已清楚；无。 |
| B07-061 有限点集的离散拓扑 | 453，“继承的拓扑是离散的”；`sec:geometry-local-relations-topology` | 必须额外构建邻域关系。 | 无孤立球计算 | 第3章已读离散度量对连续性影响；此处词义可跟上。 | 已清楚；可选补每点可被小球单独隔离。 |
| B07-062 凸包 | 455，“顶点的凸包”；`sec:geometry-local-relations-topology` | 几何上填满单纯形。 | 第4章2099–2135三点凸包 | 已回顾，区别只列顶点。 | 已清楚；无。 |
| B07-063 仿射独立 | 455、457，“保证几何维数”；`sec:geometry-local-relations-topology` | 需排除三点共线等退化。 | 点、边、填充三角形，但无判据 | 前1–6章未见定义，只有线性无关可用。 | 局部费力；B-005，补v₁-v₀,…,v_k-v₀线性无关。 |
| B07-064 单纯形 | 454–457，“k+1个…顶点”；`sec:geometry-local-relations-topology` | 成对边不足表达高阶填充。 | 点、线段、填充三角形 | 几何与组合版本已区分；依B07-063。 | 已清楚（补B-005后）；无其他修改。 |
| B07-065 抽象单纯复形 | 459–471，“向下封闭”；`sec:geometry-local-relations-topology` | 一致记录各维面集合。 | `eq:geometry-simplicial-complex-closure` | 有面须有边，反向不成立。 | 已清楚；无。 |
| B07-066 Čech复形 | 474–490，“共同交集”；`sec:geometry-local-relations-topology` | 用球覆盖解释高阶相连。 | `def:geometry-cech-rips-complexes`、`fig:geometry-cech-rips-intersection` | 半径ε/2开球，边严格小于ε。 | 已清楚；无。 |
| B07-067 Vietoris–Rips复形 | 480–490，“对任意i,j…成立”；`sec:geometry-local-relations-topology` | 只凭成对距离构造高阶面。 | 同组边长0.9三角形 | ≤ε与Čech临界边界、共同交集差别都保留。 | 已清楚；无。 |
| B07-068 尺度包含关系 | 503–512，“Cε⊂Rε⊂C₂ε₊η”；`sec:geometry-local-relations-topology` | 比较两种复形但不混用同尺度。 | 三角不等式、任选顶点完整说明 | η>0解决开球等号问题；不声称最紧常数。 | 已清楚；无。 |
| B07-069 良好覆盖 | 514–515，“交集都可连续收缩到一点”；`sec:geometry-local-relations-topology` | 给复形代表球并集的条件。 | 凸球交集 | 收缩直觉已有；只陈述有限欧氏球情形。 | 已清楚；无。 |
| B07-070 神经引理 | 516–518，“Čech复形与球并集同伦等价”；`sec:geometry-local-relations-topology` | 连接组合与连续拓扑。 | 良好覆盖条件；无证明 | 是专门定理陈述，不是潜在流形恢复保证。 | 已清楚（概述深度）；可给来源，不要求全证。 |
| B07-071 同伦等价 | 516–517，“来回复合…变形到恒等映射”；`sec:geometry-local-relations-topology` | 解释神经引理保留何种结构。 | 当前Čech与球并集 | 与前面的同胚不同，但此前同胚未定义。 | 局部费力；B-002补一句不要求互逆双射，不能替同胚。 |
| B07-072 有向单纯形 | 520–521，“交换两顶点使符号反转”；`sec:geometry-local-relations-topology` | 对端点和边缘作有符号抵消。 | [1,2]与三角形边界 | 顶点次序不同不是新增几何面。 | 已清楚；无。 |
| B07-073 k维链及链空间 | 522–523，“实系数线性组合”；`sec:geometry-local-relations-topology` | 把边缘计算线性化。 | C_k(K;R)、后续c闭环 | 向量空间已回顾；与单个单纯形不同。 | 已清楚；无。 |
| B07-074 边界算子∂_k | 523–532，“读取…有向边缘”；`sec:geometry-local-relations-topology` | 从高维面取低维边缘。 | `eq:geometry-simplicial-boundary`、∂[1,2]=[2]-[1] | 帽号删除顶点；线性延伸清楚。 | 已清楚；无。 |
| B07-075 非约化同调约定 | 531，“C₋₁={0}、∂₀=0”；`sec:geometry-local-relations-topology` | 固定零维计数口径。 | β₀=1三角形例 | 无需预学约化同调；约定已足以计算。 | 已清楚；无。 |
| B07-076 边界的边界为零 | 534–549，“成对抵消”；`sec:geometry-local-relations-topology` | 保证边界是闭链，能作商。 | `lem:geometry-boundary-squared-zero`完整证明 | 证明工具为删除次序符号；k=1单独处理。 | 已清楚；无。 |
| B07-077 闭链 | 553–555，“∂_k c=0”；`sec:geometry-local-relations-topology` | 没有剩余端点／边缘。 | c=[1,2]+[2,3]-[1,3] | 闭合不等于被填充。 | 已清楚；无。 |
| B07-078 边界链 | 556，“c=∂_{k+1}b”；`sec:geometry-local-relations-topology` | 识别可由已有高阶面消去的圈。 | 加入[1,2,3] | 与闭链的包含关系有∂²=0依据。 | 已清楚；无。 |
| B07-079 同调空间 | 559–569，“无法用已有高阶填充消去”；`sec:geometry-local-relations-topology` | 闭链模去边界，数剩余孔洞。 | H_k=ker/im；`fig:geometry-cycle-filled-simplex` | 第6章商空间已实读；不是全部闭链空间。 | 已清楚；无。 |
| B07-080 Betti数 | 562–578，“β_k=dim H_k”；`sec:geometry-local-relations-topology` | 定量记录独立类。 | 空心／填充三角形β₀、β₁可复算 | 实系数、非约化约定已给；不直接等同任意环数。 | 已清楚；无。 |
| B07-081 持续同调 | 597–598，“何时出现、何时消失”；`sec:geometry-local-relations-topology` | 单尺度受采样空隙和跨折边影响。 | 开带／圆的尺度风险，无条形码计算 | 是跨尺度概述，不用于后续证明；寿命不自动等于语义。 | 已清楚（概述）；无必需修改。 |
| B07-082 Euler示性数 | 599–604，“更粗的摘要”；`sec:geometry-local-relations-topology` | 用交替计数给一个标量。 | 空心0、填充1；秩项抵消 | 与完整Betti数组明确比较。 | 已清楚；无。 |
| B07-083 软邻接隶属度μ | 606–609，“邻接支持强度”；`sec:geometry-local-relations-topology` | 避免硬阈值骤变。 | μ∈[0,1]，高阶取边最小值示例 | 不是事件概率；规则需声明。 | 已清楚；无。 |
| B07-084 软并集 | 609–617，“a+b-ab”；`sec:geometry-local-relations-topology` | 合并软关系强度。 | `eq:geometry-fuzzy-union`；结合律与恒等元验证 | 类似概率公式不等于独立事件模型。 | 已清楚；无。 |
| B07-085 UMAP | 619–624，“具体目标…留给…降维”；`sec:geometry-local-relations-topology` | 指示软关系的后续应用。 | 无本章训练算例，明确跨卷入口 | 纯预告；不作本章推理前提。 | 纯预告；无。 |
| B07-086 范畴 | 626–632，“对象…箭头…复合”；`sec:geometry-local-relations-topology` | 扩展组织可复合表示的语言。 | 坐标过渡例，但无具体图 | 仅延伸，不参与距离与同调推导；不是已建恢复工具。 | 纯延伸；已明确边界，无必需修改。 |
| B07-087 函子 | 629–632，“保持恒等与复合”；`sec:geometry-local-relations-topology` | 描述结构保持的映射。 | 无具体双范畴算例 | 依赖刚给范畴，不用于本章证明。 | 纯延伸；无。 |

## 局部线性化

节标签：`sec:geometry-analytic-local-linearization`（B07-088至B07-100）；`sec:geometry-sampled-local-linearization`（B07-101起）。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B07-088 切空间 | 14–15预告；644–661，“所有这样的可行速度”；`chap:differential-geometry-and-symmetry` | 位置已知后问怎样动；Jacobian列空间。 | `eq:geometry-tangent-space-chart`、开带两方向 | 不是可行集合的一块，零点为零速度。 | 已清楚；无。 |
| B07-089 仿射切平面 | 660，“p+T_p M”；`sec:geometry-analytic-local-linearization` | 解释图中箭头为何画在点旁。 | `fig:geometry-strip-tangent-coordinates` | 与线性速度空间区分。 | 已清楚；无。 |
| B07-090 曲线速度刻画 | 663–675，“恰是全部光滑曲线…速度”；`sec:geometry-analytic-local-linearization` | 验证参数化定义反映真实可行动作。 | `lem:geometry-tangent-curves`双向证明 | 开参数域保证小步曲线存在。 | 已清楚；无。 |
| B07-091 切空间坐标无关性 | 667、677–680，“右乘可逆矩阵不改变值域”；`sec:geometry-analytic-local-linearization` | 排除换图改变可行方向。 | Jacobian链式法则 | 第3章848–893与第6章列空间已回顾。 | 已清楚；无。 |
| B07-092 点带切向／径向方向 | 683–711，“第一列不为零”；`sec:geometry-analytic-local-linearization` | 直接核对开带两个自由度。 | 两个偏导公式、图注0.7与0.9 | 中心线只保留s方向；不是固定全局直线。 | 已清楚；无。 |
| B07-093 二阶局部近似 | 715–722，“二阶导数有界”；`sec:geometry-analytic-local-linearization` | 说明切空间能近似多大误差。 | `eq:geometry-manifold-local-taylor` | 已回顾Taylor；局部O(h²)非全局保证。 | 已清楚；无。 |
| B07-094 法向空间及法向偏离 | 721–724，“法向正交补”；`sec:geometry-analytic-local-linearization` | 分离环境弯曲产生的剩余误差。 | 开带法向为零、中心线弯曲 | 正交补已回顾；与尚待建立的内在曲率不同。 | 已清楚；无。 |
| B07-095 正则水平集的切空间 | 726–732，“T_p M=ker J_F(p)”；`sec:geometry-analytic-local-linearization` | 没有显式参数化时用约束求速度。 | x²+y²在原点反例 | 第3章IFT已读；从行满秩选可逆子块的连接省略。 | 局部费力；B-006，补选D-d个变量作可逆子块并回指定理。 |
| B07-096 流形间光滑映射 | 734–736，“坐标表达…光滑”；`sec:geometry-analytic-local-linearization` | 映射后也需追踪变化。 | ψ⁻¹∘F∘φ | 前文欧氏光滑性；目标参数化ψ未就地明说。 | 已清楚；可选加“ψ为目标参数化”。 |
| B07-097 映射微分dF_p | 737–755，“输入速度转成输出速度”；`sec:geometry-analytic-local-linearization` | 传递可行方向而非只传位置。 | `eq:geometry-map-differential`、曲线无关论证 | 矩阵是坐标记录；复合链式法则明确。 | 已清楚；无。 |
| B07-098 余切空间 | 757–760，“线性泛函空间”；`sec:geometry-analytic-local-linearization` | 方向引起的标量变化是读取规则。 | 圆上f=cosθ例 | 所谓“上一章的对偶空间”未实际建立；第5章泛函可支撑。 | 局部费力；B-004，更正回指并就地定义代数对偶。 |
| B07-099 坐标切基与对偶基dz^i | 761–763，“dz^i(∂_j)=δ_{i,j}”；`sec:geometry-analytic-local-linearization` | 将读取规则展开为坐标。 | 分量配对式 | 上标编号已解释；对偶基未在前章讲，但本式给条件。 | 局部费力；B-004，补dz^i读取第i个系数。 |
| B07-100 标量微分df | 757、765–772，“不是一个切向量”；`sec:geometry-analytic-local-linearization` | 区分导数读取和最陡方向。 | 角速度a产生-a sinθ | 梯度留待度量建立，未倒置定义。 | 已清楚；无。 |
| B07-101 局部PCA | 777–780，“估计真实切空间”；`sec:geometry-sampled-local-linearization` | 没有解析模型时由样本估方向。 | `eq:geometry-local-weighted-covariance` | 第6章PCA已有；不是流形定义。 | 已清楚；无。 |
| B07-102 加权局部均值与协方差 | 782–793，“α≥0、和为1”；`sec:geometry-sampled-local-linearization` | 构造可分解的样本矩阵。 | 均值与C_i公式 | 均值不必是潜在点；协方差不等于后续度量。 | 已清楚；无。 |
| B07-103 估计切子空间T̂_i | 790–801，“以零向量为原点”；`sec:geometry-sampled-local-linearization` | 区分真实方向与估计对象。 | 最大d个特征向量 | 指定d不是发现维数；观测不在M时T_x M未定义。 | 已清楚；无。 |
| B07-104 局部谱尺度h²/h⁴ | 803–807，“非退化局部采样”；`sec:geometry-sampled-local-linearization` | 解释切向信号与弯曲误差不同量级。 | Taylor后平方量级推演 | 光滑性本身不保证谱隙；条件已明示。 | 已清楚；无。 |
| B07-105 子空间扰动／谱间隙δ | 809–813，“‖E‖₂/δ”；`sec:geometry-sampled-local-linearization` | 把观测误差变为方向偏转。 | 第6章2870–2942已读 | E含采样、邻域、噪声和非线性；不只测量噪声。 | 已清楚；无。 |
| B07-106 邻域尺度的偏差与信号权衡 | 815–824，“减少样本并压低…谱尺度”；`sec:geometry-sampled-local-linearization` | 防止无限缩邻域的错误推断。 | 窄带、非均匀采样、圆的全局障碍 | 局部估计准确不等于全局坐标正确。 | 已清楚；无。 |

## 度量、路径和距离

节标签：`sec:geometry-same-point-metric`（107–111）、`sec:geometry-path-speed-length`（112–115）、`sec:geometry-continuous-geodesic-distance`（116–121）、`sec:geometry-sampled-geodesic-distance`（122–123）。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B07-107 Riemann度量 | 15预告；836–847，“长度与夹角规则”；`chap:differential-geometry-and-symmetry` | 可行方向还没有长度；各点光滑正定内积。 | `def:geometry-riemannian-metric` | 同点比较，不是协方差或全局常矩阵。 | 已清楚；无。 |
| B07-108 度量矩阵G | 844–854，“g(∂_i,∂_j)”；`sec:geometry-same-point-metric` | 将内积转成可算坐标二次型。 | aᵀGb及角度公式 | 已回顾加权内积；光滑依赖位置。 | 已清楚；无。 |
| B07-109 欧氏诱导度量 | 856–864，“限制环境欧氏内积”；`sec:geometry-same-point-metric` | 使用已知嵌入的长度规则。 | `eq:geometry-induced-metric`、满秩推出正定 | 任意另选度量改变几何，不只是换坐标。 | 已清楚；无。 |
| B07-110 度量的坐标变换 | 866–875，“AᵀGA”；`sec:geometry-same-point-metric` | 换图仍保持同一内积。 | `eq:geometry-metric-coordinate-transform` | 向量分量和矩阵须一起变。 | 已清楚；无。 |
| B07-111 点带度量 | 877–887，“(1+u/R)²”；`sec:geometry-same-point-metric` | 同一坐标步在内外侧长度不同。 | `eq:geometry-strip-metric`；R=2数值 | 与采样密度不混同。 | 已清楚；无。 |
| B07-112 Riemann速度 | 892–899，“平方速度”；`sec:geometry-path-speed-length` | 沿路径逐点读取速度长度。 | `eq:geometry-riemannian-speed` | 不需要先比较异点向量。 | 已清楚；无。 |
| B07-113 路径长度 | 900–914，“标量速度按时间累计”；`sec:geometry-path-speed-length` | 评价给定路线。 | `eq:geometry-riemannian-curve-length`、换图不变推导 | 多图有限分段依紧致路径像；长度不是端点距离。 | 已清楚；无。 |
| B07-114 重参数化不变性 | 916–922，“不依赖…快慢”；`sec:geometry-path-speed-length` | 分离路径几何与走路速度。 | τ'换元，反向／停顿说明 | 重复经过不是单纯重参数化。 | 已清楚；无。 |
| B07-115 切线有限步不可行 | 924–927，“√(1+t²)>1”；`sec:geometry-path-speed-length` | 解释速度不等于可直接平移的位置增量。 | 单位圆p=(1,0)、v=(0,1) | 为后续回缩铺垫，未提前依赖它。 | 已清楚；无。 |
| B07-116 测地距离d_g | 938–949，“全部…长度的下确界”；`sec:geometry-continuous-geodesic-distance` | 路线可选时优化长度。 | `eq:geometry-geodesic-distance` | 距离不预设最短路径存在，不依赖测地线方程。 | 已清楚；无。 |
| B07-117 扩展距离 | 947，“无连接路径…+∞”；`sec:geometry-continuous-geodesic-distance` | 覆盖不连通情形。 | 定义中的约定 | 各路径连通分支有限度量；范围清楚。 | 已清楚；无。 |
| B07-118 距离公理的路径证明 | 950–952，“反向…拼接”；`sec:geometry-continuous-geodesic-distance` | 验证这确为度量。 | 对称性、三角不等式、局部正定界 | 常规局部界需防路径逃出邻域，但说明属摘要而非完整证明。 | 已清楚（概要）；无必需修改。 |
| B07-119 弦长与内在距离 | 954–995，“环境距离比较…不能照搬”；`sec:geometry-continuous-geodesic-distance` | 同端点不同允许路线的量。 | `eq:geometry-strip-chord-distance`、`fig:geometry-circle-distances` | 诱导度量、开弧、开带、完整圆各自区分。 | 已清楚；无。 |
| B07-120 开带／中心线距离比较 | 965–981，“中心线弧只是候选”；`sec:geometry-continuous-geodesic-distance` | 使用贯穿例比较约束集合改变。 | ‖p-q‖≤d_strip≤d_C | 不把“沿带距离”混作一种量。 | 已清楚；无。 |
| B07-121 下确界不达到 | 998–1001，“长度趋于2…没有…恰为2”；`sec:geometry-continuous-geodesic-distance` | 距离存在不意味着最短路径存在。 | 穿孔平面反例 | 已回顾inf/min区别；全局存在性后续处理。 | 已清楚；无。 |
| B07-122 邻域图最短边路径 | 1006–1015，“最短边路径试图近似”；`sec:geometry-sampled-geodesic-distance` | 样本条件下估计潜在距离。 | ε阈值或k近邻，边长欧氏范数 | 图只借直观并注明后章入口；观测端点与潜在点分开。 | 已清楚；无。 |
| B07-123 捷径、断连与近邻对称化 | 1017–1024，“不能…总在真实距离的同一侧”；`sec:geometry-sampled-geodesic-distance` | 说明邻域近似的失败方式。 | 跨折、稀疏、k近邻不对称 | 采样绕行与弦长误差方向不同。 | 已清楚；无。 |

## 采样条件与体积

节标签：`sec:geometry-sampled-geodesic-distance`（124）、`sec:geometry-riemannian-volume`（125–130）。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B07-124 距离近似的一致性条件 | 1025–1029，“邻域半径…缩小而仍足以覆盖”；`sec:geometry-sampled-geodesic-distance` | 给离散最短路接近连续距离的前提，兼顾密度、噪声和几何尺度。 | 前段捷径与断连反例 | 不将定性要求冒充具体收敛率；不保证后续坐标恢复。 | 已清楚；无。 |
| B07-125 Gram行列式体积 | 1034–1036，“平方体积是…det G”；`sec:geometry-riemannian-volume` | 长度不足累计区域，需把切基平行体换成体积。 | 第6章469–475；点带面积 | 行列式体积已回顾；平方根来自Gram而非有向行列式。 | 可理解；可选补正交基下G=AᵀA的一行。 |
| B07-126 Riemann体积元 | 1037–1042，“由度量产生的测度密度”；`sec:geometry-riemannian-volume` | 对区域规定坐标无关非负体积，不需全局朝向。 | `eq:geometry-riemannian-volume` | 一维长度、二维面积；不是有向微分形式。 | 已清楚；无。 |
| B07-127 体积的换图相容性 | 1044–1050，“正是…Jacobian因子”；`sec:geometry-riemannian-volume` | 保证积分不随坐标记录改变。 | 行列式变换及第3章1811–1855 | 已回顾多元换元，绝对值保留。 | 已清楚；无。 |
| B07-128 跨图局部权重拼接 | 1051–1052，“和为1的局部权重”；`sec:geometry-riemannian-volume` | 防止重叠区域重复累计。 | 可测分片为另一可行办法 | 未强加“单位分解”专名；本处只解释作用，不以它承担未证结论。 | 已清楚（概要）；无。 |
| B07-129 采样测度q dV_g | 1057–1059，“并非自动近似…dV_g”；`sec:geometry-riemannian-volume` | 区分几何体积与出现频率。 | 点带内外侧面积；2007–2021再算加权梯度 | 密度是相对所选测度的权重；不等于度量。 | 已清楚；无。 |
| B07-130 截断紧积分域 | 1061–1062，“另取…截断闭域”；`sec:geometry-riemannian-volume` | 边界积分需要另定实际区域。 | 1808–1814闭带明确构造 | 开流形无边界不等于紧致；图中边缘不自动是积分边界。 | 已清楚；无。 |

## 联络与方向搬运

节标签：`sec:geometry-connection-comparison`（131–140）、`sec:geometry-parallel-transport`（141–147）。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B07-131 光滑向量场 | 1077、1083–1084，“每个位置指定一个可行方向”；`sec:geometry-connection-comparison` | 要讨论随位置变的方向。 | 球面逐段V(t) | 与单点切向量不同，分量需光滑。 | 已清楚；无。 |
| B07-132 联络 | 1078–1087，“跨点比较规则”；`sec:geometry-connection-comparison` | 普通相减会带法向分量，需额外微分规则。 | `def:geometry-connection` | 不是把不同切空间无条件认同。 | 已清楚；无。 |
| B07-133 协变导数 | 1086–1099，“V沿U的…导数”；`sec:geometry-connection-comparison` | 输出仍是切向量，保留方向变化。 | `eq:geometry-projected-connection` | 与环境普通导数、标量方向导数区别清楚。 | 已清楚；无。 |
| B07-134 联络的函数线性与乘积法则 | 1088–1104，“系数本身的变化必须保留”；`sec:geometry-connection-comparison` | 明确两输入槽的不同线性要求。 | 三条规则及欧氏方向导数 | 常数线性不能替代第二槽的Leibniz规则。 | 已清楚；无。 |
| B07-135 向量场交换子 | 1108–1114，“先后作用的顺序…不同”；`sec:geometry-connection-comparison` | 扣除方向场本身不可交换的影响。 | 对任意f的定义及分量公式 | 坐标方向为零，一般方向场未必为零。 | 已清楚；无。 |
| B07-136 度量相容 | 1118–1126，“内积的求导…乘积法则”；`sec:geometry-connection-comparison` | 新导数必须尊重已有长度判断。 | 定义首式；1197–1201保内积证明 | 不由联络三公理自动推出。 | 已清楚；无。 |
| B07-137 无挠 | 1118–1129，“不产生交换子之外的差异”；`sec:geometry-connection-comparison` | 从联络排除额外扭转。 | 定义第二式 | 明确不等于二阶协变导数可交换。 | 已清楚；无。 |
| B07-138 Levi–Civita联络 | 1116–1131，“每个…度量唯一确定”；`sec:geometry-connection-comparison` | 使度量选择唯一的自然比较规则。 | `def:geometry-levi-civita-connection` | 相容与无挠同时要求；不是任意联络。 | 已清楚；无。 |
| B07-139 Koszul公式 | 1131–1144，“右端只含已知度量”；`sec:geometry-connection-comparison` | 证明唯一性并构造存在。 | `eq:geometry-koszul-formula` | 使用正定配对读出向量；存在验证是摘要非逐项全算。 | 可跟随（公式用途明确）；无必需修改。 |
| B07-140 投影联络 | 1146–1157，“先求环境导数再投影”；`sec:geometry-connection-comparison` | 嵌入且诱导度量时给具体算法。 | `eq:geometry-projected-connection`及两条件核验 | 任意度量不能沿用欧氏投影。 | 已清楚；无。 |
| B07-141 Christoffel系数Γ | 1164–1167，“∇_∂i ∂j=ΣΓ…∂k”；`sec:geometry-parallel-transport` | 记录切基自身变化；1290–1296给度量计算式。 | `eq:geometry-christoffel-symbols` | 与张量对比缺正式判准，不能靠“有坐标系数”区分。 | 局部费力；B-007补几何张量的一句话和非齐次变化例。 |
| B07-142 沿曲线协变导数D/dt | 1168–1180，“第一项…第二项修正”；`sec:geometry-parallel-transport` | 把场的规则应用到给定路径上的向量。 | `eq:geometry-covariant-derivative-along-path` | 普通分量导数与基变化共同构成几何导数。 | 已清楚；无。 |
| B07-143 平行移动P_γ | 1182–1192，“联络测得的变化为零”；`sec:geometry-parallel-transport` | 给定路径和起始方向，定义终值。 | `def:geometry-parallel-transport` | 路径是输入，不要求向量沿前进方向。 | 已清楚；无。 |
| B07-144 线性ODE初值唯一性与路径拼接 | 1193–1195，“连续系数的线性常微分方程”；`sec:geometry-parallel-transport` | 保证搬运有确定结果、可跨图拼接。 | 初值方程；反向和拼接关系 | 前1–6章未建立ODE定理；当地明确引用其条件和结论，不靠流形完备。 | 作为辅助结论可接受；可选标“这里引用线性ODE定理”。 |
| B07-145 平行移动的保内积性 | 1196–1202，“保持长度和夹角”；`sec:geometry-parallel-transport` | 判断搬运保留什么。 | 内积导数为零的计算 | 只对度量相容联络成立；与任意线性映射不同。 | 已清楚；无。 |
| B07-146 搬运的路径依赖 | 1204–1206、1227–1228，“仅给起终点不能决定”；`sec:geometry-parallel-transport` | 排除只按端点定义方向比较。 | 球面闭路与静止路径 | 不是任意环境旋转对齐，也不是群作用。 | 已清楚；无。 |
| B07-147 球面分段平行场的构造 | 1208–1239，“环境导数全部是法向或零”；`sec:geometry-parallel-transport` | 让路径依赖成为可复算结果。 | `ex:geometry-sphere-parallel-transport`、同名图、三段表 | 各接点一致；投影长度与真实向量长度区别已说明。 | 已清楚；无。 |

## 测地运动与最短路

节标签：`sec:geometry-geodesic-initial-value`（148–155）、`sec:geometry-endpoint-minimizing-path`（156–169）。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B07-148 测地线 | 1257–1265，“路径自己的速度平行移动”；`sec:geometry-geodesic-initial-value` | 从给定路径搬向量转为求路径。 | `def:geometry-geodesic`、球面大圆核验 | 零协变加速度不等于环境直线或全局最短。 | 已清楚；无。 |
| B07-149 仿射参数 | 1259、1271–1279，“t=ar+b”；`sec:geometry-geodesic-initial-value` | 固定运动方程允许的重参数化。 | τ'与τ''链式项 | 长度任意重参数化不变不适用于测地方程。 | 已清楚；无。 |
| B07-150 测地运动恒速 | 1266–1269，“速度大小恒定”；`sec:geometry-geodesic-initial-value` | 从度量相容说明物理直觉。 | 速度平方导数等于零 | 恒速只是必要特征，不能反推测地性。 | 已清楚；无。 |
| B07-151 测地线坐标方程 | 1298–1306，“ddot z+Γ dot z dot z=0”；`sec:geometry-geodesic-initial-value` | 可数值求解的运动规则。 | `eq:geometry-geodesic-equation` | 来自沿曲线协变导数而非最短路定义。 | 已清楚；无。 |
| B07-152 测地初值的局部解与延拓 | 1308–1313，“局部唯一…光滑依赖初值”；`sec:geometry-geodesic-initial-value` | 保证初速度可生成短时轨迹。 | 开球速度2e₁在1/2退出反例 | 辅助ODE结论当地陈述；不把局部存在当全时间存在。 | 已清楚（引用结论深度）；无。 |
| B07-153 指数映射 | 1315–1324，“γ_v(1)”；`sec:geometry-geodesic-initial-value` | 把切向初速度转成附近可行点。 | `def:geometry-exponential-map`、球面显式公式 | Exp不是矩阵指数；定义域需解存在至1。 | 已清楚；无。 |
| B07-154 指数映射的缩放与一阶相容 | 1325–1328，“初速度缩放对应时间缩放”；`sec:geometry-geodesic-initial-value` | 连接速度与点坐标，为回缩准备。 | Exp_p(tv)=γ_v(t)、零点导数为id | 仅在两边存在时成立。 | 已清楚；无。 |
| B07-155 指数坐标的局部可逆性 | 1329–1343，“不保证全局一一对应”；`sec:geometry-geodesic-initial-value` | 可用切向量表示附近点但不能覆盖全局。 | 球面对跖点使不同初速度合并 | 第3章隐函数定理可推出逆函数结论；不是先验全局坐标。 | 可理解；可选引用IFT并给F(y,x)=Exp_p(x)-y。 |
| B07-156 路径能量E(γ) | 1350–1353，“固定时间区间”；`sec:geometry-endpoint-minimizing-path` | 用可微平方速度目标连接最短路与运动方程。 | 积分定义 | 与路径长度、后面的函数Dirichlet能量对象不同。 | 已清楚；无。 |
| B07-157 长度—能量不等式 | 1354–1357，“等号…恒定的速度大小”；`sec:geometry-endpoint-minimizing-path` | 限定长度与能量优化如何互换。 | Cauchy–Schwarz及非退化匀速条件 | 能量本身不任意重参数化不变。 | 已清楚；无。 |
| B07-158 路径Lagrange函数 | 1359–1360，“1/2 Σg…dot z…dot z”；`sec:geometry-endpoint-minimizing-path` | 把积分目标写为位置和速度的局部函数。 | 后续两个偏导显式计算 | 与第4章乘子Lagrange函数用途不同；当地公式足以确定对象。 | 已清楚；可选点明只是积分被积函数。 |
| B07-159 一阶变分δE[h] | 1361–1369，“端点为零的扰动”；`sec:geometry-endpoint-minimizing-path` | 对整条路径而非单点位置判驻定。 | 分部积分式；1844后才显式定义ε扰动 | 第5章方向导数已读，但δ符号与路径扰动未接出。 | 局部费力；B-009补δE[h]=dE(z+εh)/dε在0的定义。 |
| B07-160 Euler–Lagrange方程 | 1369–1387，“任意这样的h…为零”；`sec:geometry-endpoint-minimizing-path` | 把积分驻定条件变成局部方程。 | 两偏导、速度项对称化、乘G⁻¹ | 需解释任意局部支撑扰动迫使被积系数为零。 | 局部费力；B-009补连续非零系数可取同号局部扰动的理由。 |
| B07-161 驻定与最短性的单向关系 | 1388–1400，“不说明每个能量驻点都是最短路”；`sec:geometry-endpoint-minimizing-path` | 阻止把解ODE当全局路线最优。 | 圆上3π/2与π/2两弧 | 与第4章驻点不保证极小呼应。 | 已清楚；无。 |
| B07-162 正规邻域 | 1391–1394，“足够小的正规邻域”；`sec:geometry-endpoint-minimizing-path` | 确定径向测地线最短结论的局部范围。 | 只有文字结论，未说明由Exp构造 | 前面局部可逆性可承接，但名称未定义。 | 局部费力；B-008补Exp在零点星形邻域上微分同胚的像。 |
| B07-163 凸正规邻域 | 1392–1394，“任意两点…唯一的邻域内最短”；`sec:geometry-endpoint-minimizing-path` | 从固定中心加强到域中任意端点。 | 2040用于边搬运唯一选择 | “凸”不是环境线段凸；与正规邻域区别需点明。 | 局部费力；B-008补这一加强而非仅换名称。 |
| B07-164 长度最短测地线 | 1396，“达到d_g”；`sec:geometry-endpoint-minimizing-path` | 给运动且实现全局距离的路径命名。 | 圆的两弧比较 | 距离下确界与局部驻点已分别定义。 | 已清楚；无。 |
| B07-165 割点 | 1401，“何时失去最短性”；`sec:geometry-endpoint-minimizing-path` | 纯延伸预告，提示局部结论的边界。 | 没有展开算例；明确不在本章展开 | 不依靠该术语作后续推导。 | 纯预告；无。 |
| B07-166 共轭点 | 1402，“聚焦与变分退化”；`sec:geometry-endpoint-minimizing-path` | 纯延伸预告，与割点提供不同研究问题。 | 没有展开算例 | 不预设读者已会判定共轭点。 | 纯预告；无。 |
| B07-167 Hopf–Rinow存在性结论 | 1405–1415，“任意两点之间存在”；`sec:geometry-endpoint-minimizing-path` | 补足全局最短路存在条件。 | 定理完整条件、穿孔平面反例 | 明确只引用不证；存在不等于唯一。 | 已清楚（引用结论深度）；无。 |
| B07-168 d_g完备性 | 1408、1412–1413，“Cauchy序列…内收敛”；`sec:geometry-endpoint-minimizing-path` | 排除有限长度到达空间缺口。 | 第3章343–422；1421长度趋于2 | 已回顾度量完备，不是测度完备或环境闭性。 | 已清楚；无。 |
| B07-169 测地完备与紧致情形 | 1409、1415，“延拓到所有实数时间”；`sec:geometry-endpoint-minimizing-path` | 区分全时间运动与局部解，并给常用充分场景。 | 球面多条最短弧；开球反例 | 作为Hopf–Rinow推论，未声称任意非紧都失败。 | 已清楚；无。 |

## 曲率

节标签：`sec:geometry-riemannian-curvature`。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B07-170 Riemann曲率算子 | 1432–1449，“扣除…交换子”；`sec:geometry-riemannian-curvature` | 测量附近路径顺序的几何响应。 | `eq:geometry-riemann-curvature`、球面推导 | 与无挠不同；符号约定明确。 | 已清楚；无。 |
| B07-171 点上的几何张量 | 1305先用；1448–1453，“不依赖…附近的具体延拓”；`sec:geometry-geodesic-initial-value` | 说明曲率是点处对象，而非任意场的导数记录。 | 乘函数导数项相消的说明 | 第6章只预告几何张量，多线性与换坐标规则未建立。 | 局部费力；B-007补点处多线性对象及零张量换基仍零的判准。 |
| B07-172 小闭路搬运的面积阶响应 | 1453–1455，“由R…乘闭路面积尺度控制”；`sec:geometry-riemannian-curvature` | 把二阶导数式接回搬运直觉。 | 前面的球面有限闭路作背景 | 明确有限大闭路不能只用一点曲率乘面积。 | 可理解（渐近说明）；可选把“首个非零”改“面积阶首项”，该项可为零。 |
| B07-173 截面曲率 | 1457–1470，“选定一个二维切平面”；`sec:geometry-riemannian-curvature` | 将多方向算子变成可比较标量。 | `eq:geometry-sectional-curvature` | 分母是平方面积，需u、v线性无关。 | 已清楚；无。 |
| B07-174 Gauss曲率 | 1471–1472，“二维流形…整个切平面”；`sec:geometry-riemannian-curvature` | 二维情况下不再需选截面。 | 球面1/R₀²、圆柱0 | 不给一维圆硬套截面曲率。 | 已清楚；无。 |
| B07-175 一维Riemann曲率为零 | 1472–1473，“没有二维切平面”；`sec:geometry-riemannian-curvature` | 阻止把环境圆弯曲当内在曲率。 | 1500–1504回看PCA法向误差 | 二维截面不存在不等于一维曲线在环境不弯。 | 已清楚；可选由R对前两槽反对称接一行。 |
| B07-176 内在平坦与外在弯曲 | 1475–1504，“可以局部无伸缩地展开”；`sec:geometry-riemannian-curvature` | 区分度量曲率与嵌入形状。 | 圆柱常度量、球面投影推得正曲率、开带变系数 | Γ非零和二阶法向偏离均不是内在非零曲率证据。 | 已清楚；无。 |
| B07-177 曲率与整体拓扑的独立信息 | 1505–1506，“整体的环却不同”；`sec:geometry-riemannian-curvature` | 限制局部量的全局外推。 | 平面与圆柱 | 局部零曲率不自动使所有全局闭路搬运平凡。 | 已清楚；无需补用本章尚未建立的全局分类。 |

## 流形点优化

节标签：`sec:geometry-point-optimality`（178–189）、`sec:geometry-riemannian-gradient-method`（190–195）、`sec:geometry-riemannian-newton-trust-region`（196–202）。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B07-178 流形点优化的存在性与边界范围 | 1519、1527–1530，“非空…紧致且f连续”；`sec:geometry-point-optimization` | 先说明最小值是否存在，再谈求解。 | 极小值定理、紧下水平集 | 已回顾局部／全局极小；活动不等式边界不在本条件范围。 | 已清楚；无。 |
| B07-179 Riemann梯度 | 1532–1545，“用度量把它表示成向量”；`sec:geometry-point-optimality` | 从df的读取规则选下降方向。 | `eq:geometry-riemannian-gradient-definition` | 微分不依赖度量，梯度依赖；有限维Riesz已核对。 | 已清楚；无。 |
| B07-180 负梯度的最陡性 | 1546–1548，“单位…方向中”；`sec:geometry-point-optimality` | 解释负梯度为何用于优化。 | Cauchy–Schwarz达到条件 | 需非驻点才有唯一归一化负梯度方向。 | 已清楚；无。 |
| B07-181 逆度量抬升偏导分量 | 1550–1560，“G⁻¹∇_z f”；`sec:geometry-point-optimality` | 将余切记录换为可行切向量。 | `eq:geometry-riemannian-gradient-coordinates`完整配对推导 | 不把普通偏导列表自动当梯度。 | 已清楚；无。 |
| B07-182 环境梯度投影 | 1561–1563，“P_p∇bar f”；`sec:geometry-point-optimality` | 诱导度量时给实用计算。 | 与任意切向量内积不变 | 需环境光滑延拓；不对任意度量使用。 | 已清楚；无。 |
| B07-183 Riemann Hessian算子 | 1565–1574，“梯度的一阶变化…不同…切空间”；`sec:geometry-point-optimality` | 用联络比较梯度得到二阶信息。 | `def:geometry-riemannian-hessian` | 输出仍在同一切空间；不直接减异点梯度。 | 已清楚；无。 |
| B07-184 Hessian双线性形式 | 1575–1591，“g(u,Hess f[v])”；`sec:geometry-point-optimality` | 用二次型判断曲率和最优性。 | 对称性完整消项证明；B_ij公式 | 双线性矩阵B与算子矩阵G⁻¹B不是同一矩阵。 | 已清楚；无。 |
| B07-185 G自伴性 | 1593–1594，“相对于内积G自伴”；`sec:geometry-point-optimality` | 解释算子坐标看似不对称。 | B对称而G⁻¹B一般不普通对称 | 已回顾伴随依赖内积，不是算法出错。 | 已清楚；无。 |
| B07-186 沿曲线的函数二阶导数 | 1596–1602，“Hess项…协变加速度项”；`sec:geometry-point-optimality` | 连接Hessian与真实函数变化。 | `eq:geometry-function-second-derivative` | 测地线消去加速度项；为二阶回缩留准确入口。 | 已清楚；无。 |
| B07-187 极小点一二阶必要条件 | 1603–1609，“任意初速度”；`sec:geometry-point-optimality` | 将一元极小条件沿所有切方向使用。 | grad=0、Hessian二次型非负 | 无边界条件重要；半正定不充分。 | 已清楚；无。 |
| B07-188 严格局部极小的充分条件 | 1610–1611，“零梯度且Hessian正定”；`sec:geometry-point-optimality` | 何时局部二阶检验足够。 | 指数坐标Taylor说明；球面正负驻点例 | 已回顾二阶Taylor；不把驻点当极小。 | 已清楚；无。 |
| B07-189 测地凸性 | 1613–1621，“沿每条…一元凸函数”；`sec:geometry-point-optimality` | 环境线段不可行时替代欧氏凸性。 | 一阶支持不等式及驻点全局最优推导 | 先查域内最短连接，再查沿路凸；欧氏凸目标限制后不自动满足。 | 已清楚；无。 |
| B07-190 回缩 | 1626–1643，“保留起点…初速度”；`sec:geometry-riemannian-gradient-method` | 降低精确测地计算成本并保持可行。 | `def:geometry-retraction` | 一阶相容不等于精确测地运动或任意大步定义。 | 已清楚；无。 |
| B07-191 Riemann梯度更新 | 1645–1656，“R_p(-α grad f)”；`sec:geometry-riemannian-gradient-method` | 将瞬时下降方向变为实际可行点。 | `eq:geometry-riemannian-gradient-step`及零步导数 | 正步下降只先保证足够小步。 | 已清楚；无。 |
| B07-192 回缩上的回溯线搜索 | 1657–1660，“在回缩定义域内回溯”；`sec:geometry-riemannian-gradient-method` | 找到可接受有限步。 | 充分下降不等式；第4章572–584算法已核对 | 普通回溯已回顾，这里另查回缩域。 | 已清楚；无。 |
| B07-193 驻点收敛的附加条件 | 1660–1663，“统一局部光滑界”；`sec:geometry-riemannian-gradient-method` | 防止逐步下降被误认作完整收敛证明。 | 列出下水平集、下界、回溯条件 | 梯度趋零、点列收敛、全局最优三者不同。 | 已清楚；无。 |
| B07-194 球面归一化回缩 | 1665–1676，“角度是arctan r”；`sec:geometry-riemannian-gradient-method` | 给不需求ODE的可算更新。 | `eq:geometry-sphere-retraction`、`fig:geometry-sphere-retraction` | Exp角度r与归一化角度arctan r不同。 | 已清楚；无。 |
| B07-195 球面线性目标的驻点分类 | 1678–1684，“正向…极小，反向…极大”；`sec:geometry-riemannian-gradient-method` | 实际联合使用梯度和Hessian。 | 显式grad及Hess公式 | 梯度清零不能区分两点。 | 已清楚；无。 |
| B07-196 Riemann Newton模型与方向 | 1703–1718，“在当前点…切空间建立模型”；`sec:geometry-riemannian-newton-trust-region` | 利用二阶信息决定步。 | m_p及Bη=-∇_z f；第4章698–726 | 奇异／不定风险与局部快速收敛条件分开。 | 已清楚；无。 |
| B07-197 流形信赖域 | 1720–1728，“限制模型适用范围”；`sec:geometry-riemannian-newton-trust-region` | 模型远处不可靠时限制切向步长。 | ‖η‖_g≤Δ子问题 | 不只截断Newton步；需要子问题下降量。 | 已清楚（算法概述）；无。 |
| B07-198 实际／预测下降比ρ | 1721–1726，“只在分母为正时使用”；`sec:geometry-riemannian-newton-trust-region` | 决定是否接受及调整半径。 | ρ分式 | 与距离或曲率无关，是模型质量检验。 | 已清楚；无。 |
| B07-199 回缩拉回目标 | 1730–1742，“定义在固定向量空间”；`sec:geometry-riemannian-newton-trust-region` | 判断切空间模型是否等于实际回缩后的二阶展开。 | `eq:geometry-retraction-pullback-hessian` | 与原流形点函数同值但自变量空间不同。 | 已清楚；无。 |
| B07-200 二阶回缩 | 1743–1749，“D dot c/dt在0为零”；`sec:geometry-riemannian-newton-trust-region` | 消除拉回Hessian里的额外梯度—加速度项。 | Exp与球面归一化的法向二阶导数 | 普通回缩只保一阶；驻点处额外项也消失。 | 已清楚；无。 |
| B07-201 向量搬运 | 1752–1759，“旧切空间…不能…直接相加”；`sec:geometry-riemannian-newton-trust-region` | 复用动量、旧搜索方向时定义跨点运算。 | T_η的定义域和值域；投影例 | 线性、光滑、零步恒等不意味着等距或可逆。 | 已清楚；无。 |
| B07-202 投影搬运与平行移动之别 | 1757–1759，“甚至可能压掉某些方向”；`sec:geometry-riemannian-newton-trust-region` | 说明便宜算法替代物保留性质较少。 | 旧方向投到新切空间 | 路径和Levi–Civita规则不能由投影名称替代。 | 已清楚；无。 |

## 函数与向量场优化

节标签：`sec:geometry-smoothness-energy-boundary`（203–213）、`sec:geometry-energy-variation-solvers`（214–230）、`sec:geometry-sampled-geometric-operators`（231–239）。

| ID／概念 | 首次位置与短引文 | 为什么引入；当地解释与条件 | 理解支撑 | 依赖与相近概念 | 判断与最小修改 |
| --- | --- | --- | --- | --- | --- |
| B07-203 函数Dirichlet能量 | 1764–1782，“累计单位长度上的变化”；`sec:geometry-smoothness-geometric-operators` | 优化整函数平滑程度，而非移动单点。 | `eq:geometry-dirichlet-energy` | 与路径能量未知量不同；发散可取+∞。 | 已清楚；无。 |
| B07-204 点带平滑能量的双重度量权重 | 1783–1793，“梯度和体积”；`sec:geometry-smoothness-energy-boundary` | 避免只改偏导或只改面积。 | `eq:geometry-strip-dirichlet-energy` | 内外侧单位长度变化与面积权重来自同一G。 | 已清楚；无。 |
| B07-205 流形H¹候选空间 | 1795–1804，“函数及其弱一阶导数…平方可积”；`sec:geometry-smoothness-energy-boundary` | 容纳有限能量但不逐点光滑的极限。 | H¹范数；第5章309–424 | 已回顾弱导数与Sobolev；本处加几何梯度及体积。 | 已清楚；无。 |
| B07-206 弱解与测试范围 | 1796、1803–1806，“通过分部积分定义”；`sec:geometry-smoothness-energy-boundary` | 以积分条件延伸经典求导和方程。 | 第5章\|x\|、阶跃反例已核对 | 非紧时需额外无穷远与测试函数约定。 | 已清楚（弱解只引方向）；无。 |
| B07-207 边界迹 | 1815–1817，“从内部接近边界…适当极限”；`sec:geometry-smoothness-energy-boundary` | H¹等价类不能任意直接读取边缘值。 | 闭带域及四角测度零说明；第5章420–424 | 光滑迹与弱迹算子意义分开。 | 已清楚（概述）；无。 |
| B07-208 固定与自由边界变分 | 1817，“扰动…为零／变分决定”；`sec:geometry-smoothness-energy-boundary` | 完整指定可行函数及允许扰动。 | 后续Green公式推出两类条件 | 不把流形无边界与函数边界自由混同。 | 已清楚；无。 |
| B07-209 常量零能量与信号丢失 | 1819–1820，“最平滑不会自动保留观测”；`sec:geometry-smoothness-energy-boundary` | 提醒单纯平滑目标退化。 | grad常量=0 | 不是算法故障，是目标未包含拟合要求。 | 已清楚；无。 |
| B07-210 数据拟合积分 | 1821–1822，“λ/2∫\|f-y\|²”；`sec:geometry-smoothness-energy-boundary` | 在平滑之外保留信号。 | 显式平方拟合项 | 已回顾正则化目标；当前不声称已给全部求解方程。 | 已清楚；无。 |
| B07-211 均值与范数约束 | 1822–1823，“零均值加单位L²范数”；`sec:geometry-smoothness-energy-boundary` | 排除全局常量并引向谱模态。 | 后续特征函数与零模 | 不连通时仍可能有分支常量零模，1938已说明。 | 已清楚；无。 |
| B07-212 H¹点值评价限制 | 1824–1825，“一般维数下未必…连续评价”；`sec:geometry-smoothness-energy-boundary` | 检查点观测是否为候选空间合法数据。 | 第5章449–483一维与三维对照 | 局部平均／提高正则性不同于任意指定代表值。 | 已清楚；无。 |
| B07-213 向量场协变平滑能量 | 1827–1839，“Σ‖∇_e_a V‖²”；`sec:geometry-smoothness-energy-boundary` | 方向不能逐坐标相减，需按联络度量变化。 | 正交换基保持平方和的说明 | 场范数还含V本身；坐标常量不等于平行场。 | 已清楚；无。 |
| B07-214 函数能量的一阶变分 | 1844–1854，“f_ε=f+εh”；`sec:geometry-energy-variation-solvers` | 求整函数目标的下降方向。 | `eq:geometry-dirichlet-first-variation` | 第5章函数方向导数已回顾；与沿点轨迹求导明确区分。 | 已清楚；无。 |
| B07-215 Riemann散度 | 1856–1864，“相对于几何体积的局部净流出”；`sec:geometry-energy-variation-solvers` | 把h上的导数通过积分转走。 | J_g⁻¹Σ∂_i(J_g V^i) | 不等于任意坐标的Σ∂_i V^i。 | 已清楚；无。 |
| B07-216 几何散度定理 | 1865–1869，“内部…边界”；`sec:geometry-energy-variation-solvers` | 识别变分的边界贡献。 | 积分恒等式、随后Green推导 | 区域及光滑条件沿用1795；不自动用于所有非紧域。 | 已清楚；无。 |
| B07-217 边界外单位余法向与dS_g | 1868–1869，“在T M内垂直于边界”；`sec:geometry-energy-variation-solvers` | 明确通量读取方向和面积。 | 闭带四边；∂_n f定义 | 与流形在环境中的法向空间不同；两对象同式中各有解释。 | 已清楚；无。 |
| B07-218 Laplace–Beltrami算子 | 1871–1885，“梯度再取散度”；`sec:geometry-energy-variation-solvers` | 几何平滑的二阶算子。 | `eq:geometry-laplace-beltrami`、圆例 | 符号取Δ为热方程右端，-Δ非负；不是偏导平方和。 | 已清楚；无。 |
| B07-219 热方程生成元用语 | 1883，“取Δ_g为…生成元”；`sec:geometry-energy-variation-solvers` | 预告即将写出的时间演化符号。 | 1910–1914热方程 | 没有借用半群理论作证明；“生成元”尚未系统定义。 | 纯预告性命名；可选写“热方程右端算子”减轻专名负担。 |
| B07-220 Green恒等式 | 1886–1896，“散度的乘积法则”；`sec:geometry-energy-variation-solvers` | 将梯度内积变成h与Δf的配对。 | `eq:geometry-green-identity`完整来源 | 边界项没有被无条件略去。 | 已清楚；无。 |
| B07-221 Dirichlet边界条件 | 1898–1899，“固定f的边界迹”；`sec:geometry-energy-variation-solvers` | 固定边缘值使h在边界为零。 | Green边界项 | Dirichlet能量名称相同但不意味着自动取Dirichlet边界。 | 已清楚；无。 |
| B07-222 齐次Neumann自然边界条件 | 1899–1902，“∂_n f=0”；`sec:geometry-energy-variation-solvers` | 自由边界的任意扰动要求通量为零。 | Green边界项，闭带全部边需处理 | 与固定值不同；非齐次通量未在本节展开。 | 已清楚；无。 |
| B07-223 调和驻点方程 | 1901，“内部驻点满足Δ_g f=0”；`sec:geometry-energy-variation-solvers` | 写出无数据项平滑的局部解条件。 | Green式对内部h | 正文没有使用“调和”专名，记录其新方程对象；不是数据拟合的完整方程。 | 已清楚；无。 |
| B07-224 L²能量梯度 | 1904–1909，“grad_L² E=-Δ_g f”；`sec:geometry-energy-variation-solvers` | 用函数内积把能量微分表示成函数。 | δE=<−Δf,h>，算子域与边界限制 | 不等于每点的切向量grad f；第5章内积依赖已读。 | 已清楚；无。 |
| B07-225 热流与能量耗散 | 1910–1923，“∂_t f=Δ_g f”；`sec:geometry-energy-variation-solvers` | 用负函数梯度连续平滑整幅函数。 | `eq:geometry-heat-equation`及dE/dt非正计算 | 时间t不是点带空间s；改变函数内积也改变流。 | 已清楚；无。 |
| B07-226 Laplace谱与特征函数 | 1925–1937，“离散谱…完备正交系”；`sec:geometry-energy-variation-solvers` | 用全局模态描述平滑尺度。 | 非负性证明及`ex:geometry-circle-energy-scale` | 正维、紧致、无边界条件明确；椭圆理论的离散完备结论单独标明引用。 | 已清楚（结论深度）；无。 |
| B07-227 常量零模及边界对谱的影响 | 1938–1941，“每个连通分支上为常量”；`sec:geometry-energy-variation-solvers` | 说明最低模态是否能保留常数。 | Neumann保留、Dirichlet首值正 | 连通性不可省；已限定紧光滑域而非任意有边界集合。 | 已清楚；无。 |
| B07-228 形式L²伴随∇* | 1970–1977，“给定体积及边界条件下的形式…伴随”；`sec:geometry-energy-variation-solvers` | 把向量场导数转移到另一侧。 | `eq:geometry-connection-laplacian-variation` | 第5章只建立有界算子Hilbert伴随；形式表达式与算子域易混。 | 局部费力；B-010补由分部积分确定微分表达式、边界域另定。 |
| B07-229 联络拉普拉斯∇*∇ | 1978–1989，“本章取非负号约定”；`sec:geometry-energy-variation-solvers` | 向量场平滑的二阶算子。 | 局部标架公式及非负内积式 | 标架变化修正不能删；不是逐分量标量Δ。 | 已清楚（依B-010补伴随）；无其他修改。 |
| B07-230 向量场热流及平行零模 | 1986–1992，“零能量场必须处处平行”；`sec:geometry-energy-variation-solvers` | 给场优化演化并限制其平衡态。 | ∂_t V=−∇*∇V、自然∇_n V=0 | 非零平行场未必存在；不能照搬标量常量零模。 | 已清楚；无。 |
| B07-231 离散标量平滑能量 | 1997–2005，“1/2 Σw_ij(f_i-f_j)²”；`sec:geometry-sampled-geometric-operators` | 有限点云上替代连续积分。 | 有序对重复边的系数说明 | 图拉普拉斯仅预告到后章；非负对称权重不证明连续一致性。 | 已清楚；无。 |
| B07-232 双重采样的密度因子 | 2007–2010，“可能带入两个…密度因子”；`sec:geometry-sampled-geometric-operators` | 限制离散求和与几何积分的等同。 | 单样本q dV与双求和对照 | 核宽、维数尺度及归一化共同决定极限。 | 已清楚（风险提示而非定理）；无。 |
| B07-233 加权平滑能量E_q | 2011–2017，“1/2∫q‖grad f‖²”；`sec:geometry-sampled-geometric-operators` | 给一个明确的非均匀连续目标。 | 分部积分得到div(q grad f) | q>0光滑，边界项须消失。 | 已清楚；无。 |
| B07-234 加权函数内积下的负梯度 | 2018–2021，“q⁻¹div_g(q grad f)”；`sec:geometry-sampled-geometric-operators` | 说明同一能量换内积也会换演化。 | 与L²(dV)无q⁻¹的比较 | 能量权重与内积权重是两项独立指定。 | 已清楚；无。 |
| B07-235 离散质量权重 | 2023–2024，“代表局部体积”；`sec:geometry-sampled-geometric-operators` | 说明有限维函数内积也有几何权重。 | 无单独矩阵算例；承接前述两种L² | 不是边权，影响同能量的梯度算子。 | 可理解（概述）；可选补Σm_i f_i h_i。 |
| B07-236 离散算子一致性条件 | 2025–2029，“不能证明它逼近指定…算子”；`sec:geometry-sampled-geometric-operators` | 区分代数正性与几何近似。 | 条件清单：覆盖、密度、尺度、噪声、边界 | 固定值和无通量不能由同一未说明边规则自动实现。 | 已清楚；无。 |
| B07-237 邻边搬运P_(i←j) | 2031–2033，“先…给出跨点比较”；`sec:geometry-sampled-geometric-operators` | 将两点向量送到同一空间再相减。 | 显式定义域、值域 | 不是直接减环境分量。 | 已清楚；无。 |
| B07-238 离散向量场能量 | 2034–2038，“‖V_i-P V_j‖²”；`sec:geometry-sampled-geometric-operators` | 对采样方向建立平滑目标。 | 显式平方和 | 与标量离散能量相同目的但额外需要搬运。 | 已清楚；无。 |
| B07-239 边搬运的路径选择与对称性条件 | 2039–2044，“等距…反向为逆”；`sec:geometry-sampled-geometric-operators` | 确保两端比较一致并评估近似误差。 | 凸正规邻域、估计切平面对齐、投影反例 | 非负能量不保证逼近联络拉普拉斯。 | 已清楚（正规邻域依B-008）；无其他修改。 |

## 整章结论与交接

- 已完成1–2072行完整顺读，登记239项。重复回用沿原项补证据，不把章末总结机械重复计数；纯延伸预告已明确标注。
- 2046–2072行独立小结回应开篇的表示、可行方向、长度、跨点比较与优化问题，且明确接到第8章随机观测。小结没有新建必须另行定义的技术对象。
- 10项实质问题见`reader-b.md`的R1-B-001至010，均为局部费力；未发现需要依靠本章后文反向补齐才能继续主线的阻断性问题，也没有确认的技术错误。小表内“可选”不计入问题数。
- 本章正式PDF视觉验收未做且不属于本轮职责；图注、正文对图的解释和对应解析算例均已读。
- 第7章已完成，下一章为冻结清单中的第8章“随机变量”，从源第1行开始。
