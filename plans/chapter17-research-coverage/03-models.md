# 第17章数学问题框架对第三卷的覆盖审查

本表记录本轮来源审查；章节职责与补充建议以[统一大纲](../chapter17-learning-framework-outline.md)及[总报告](../chapter17-research-coverage.md)为准。一般的可行性与静态约束求解归17.4，涉及行动反馈和长期要求时再联合17.7。文中现有第17章行号用于说明原有内容可保留的位置，不代表正文已按新大纲重构。

审查日期：2026-10-07。本分表只读审查正文来源与大纲，未作逐图验收；本轮未改正文、图片和PDF，仅维护大纲与覆盖计划。

## 范围与读法

检查了 `tex/03-models/` 下全部50份 `.tex`，以及三份部分大纲，共53份文件、31,090行。49份tex从 `volume.tex` 的正文链可达，另1份 `main.tex` 是独立出版入口。全部文件做标题与包含关系清点；实质正文检查章/节的主要问题入口、代表性的定义/目标/算法判断段、理论分析和评价边界。大纲检查完整标题层级及与这些问题对应的范围说明。没有逐行复核所有证明、参考文献或全部数值算例，也没有本轮PDF视觉验收。逐文件粒度在文末列明。

三份大纲不是“只有规划尚无正文”的文件：经典6章、神经9章、概率图14章的实质源文件均已存在并被正文链调用。大纲中“初稿”或“写作基线”不据此判作未实现；正文与大纲的细节差异另列。

本报告用“主要”表示这组问题直接要回答的数学判断；“联合”表示同一个问题还依赖另一组判断。多个落点允许交叉，不把模型领域强制划成互斥类别。

## 核心结论与范围边界

五类问题可以承接第三卷主要学习研究问题，不需要另立“概率模型”或“纯计算”主节。17.4保持“优化与收敛分析”：研究固定学习问题是否可解，学习算法是否收敛以及收敛速度和误差。近邻检索、概率边缘化、积分、随机生成、滤波等模型运算作为来源和工具记录保留，不要求在17.4增加独立计算接口。

判断归属时，应把研究问题与所用工具分开。例如，EM的近似E步使用概率推断，所问学习问题仍是近似误差是否破坏参数更新的收敛；贝叶斯学习使用后验积分，所问统计问题可以是后验是否集中、预测风险是否一致。单独计算一次边缘概率或从固定模型生成样本，不因使用相同工具就成为同一种学习问题。

下列来源记录同时含学习问题和模型运算。P3、P4、P6等固定模型计算明确标为“工具，不单列学习研究问题”；其他混合条目按具体判断归类。模拟样本量、环境样本量和训练步数仍需区分，但只在相关学习分析依赖它们时说明，不为覆盖所有运算另设章节。

需要保留两项建模边界：

1. **模型律与评价律分开。** 静态密度学习中，真实环境观测分布P固定，候选h给出模型律q_h。统计目标可为 `E_P[-log q_h(X)]`；模型生成的X~q_h不自动成为真实评价环境P。模型族能否逼近P、训练能否收敛、有限样本能否识别或恢复总体结论分别进入17.3、17.4和17.5。
2. **有状态不自动是策略闭环。** RNN内部状态、HMM状态推断和扩散人工噪声过程不自动属于行动反馈。其表示、学习收敛和统计问题按所问结论归类；固定模型的状态递推可只作为运算工具。17.7承接行动反馈、在线累计表现与长期要求的分析。

## 逐组覆盖：经典模型

### C1 核与特征空间是否是合法且适合任务的表示

主要落点：**17.3**。联合落点：17.4、17.5。

对象：核K、特征映射φ、函数族及有限Gram矩阵。 判断：先判断能否精确写成内积 K(x,z)=〈φ(x),φ(z)〉；再区分扩大可表示函数族、核矩阵的数值计算成本以及该几何对真实任务是否合适。

正文证据：[正定条件与特征空间](../../tex/03-models/01-classic-models/common/kernels.tex)（`tex/03-models/01-classic-models/common/kernels.tex:22`）；[核矩阵的使用与中心化](../../tex/03-models/01-classic-models/common/kernels.tex)（`tex/03-models/01-classic-models/common/kernels.tex:271`）；[经典模型的建模思路](../../tex/03-models/01-classic-models/01-overview.tex)（`tex/03-models/01-classic-models/01-overview.tex:18`）。

大纲证据：[共享机制与差异](../classic-models-outline.md)（`plans/classic-models-outline.md:316`）；[降维](../classic-models-outline.md)（`plans/classic-models-outline.md:105`）。

状态：有正文；大纲有对应职责说明。

归属边界：一个有限训练矩阵半正定不等于已经验证任意输入上的核合法性；核平滑权重、核PCA几何、GP协方差承担不同角色。

### C2 监督任务到底预测什么，以及输出怎样转为决策

主要落点：**17.3、17.5**。联合落点：17.4；采用行动损失时17.7。

对象：条件均值、分位数、类别标签、得分、条件概率和预测分布；各自的损失。 判断：平方损失的总体最优预测为条件均值，分位数损失对应条件分位点，概率评分与硬类别错误比较不同对象。比较经验目标与总体表现；任务给定后才研究求解。

正文证据：[回归章开篇](../../tex/03-models/01-classic-models/02-regression.tex)（`tex/03-models/01-classic-models/02-regression.tex:4`）；[分位数回归](../../tex/03-models/01-classic-models/02-regression.tex)（`tex/03-models/01-classic-models/02-regression.tex:441`）；[Logistic回归](../../tex/03-models/01-classic-models/classification/04-probability.tex)（`tex/03-models/01-classic-models/classification/04-probability.tex:6`）；[模型选择与评价](../../tex/03-models/01-classic-models/03-classification.tex)（`tex/03-models/01-classic-models/03-classification.tex:21`）。

大纲证据：[四个任务章节的职责与核心问题](../classic-models-outline.md)（`plans/classic-models-outline.md:27`）；[回归](../classic-models-outline.md)（`plans/classic-models-outline.md:36`）；[分类](../classic-models-outline.md)（`plans/classic-models-outline.md:60`）。

状态：有正文；大纲有对应职责说明。

归属边界：分类阈值/拒答若由不同误判成本选择，是决策准则问题；分布报告不因分类准确便自动校准。

### C3 参数拟合、正则化和病态方向

主要落点：**17.4**。联合落点：17.3、17.5、17.6。

对象：固定设计X、响应y、系数w、惩罚及可行集。 判断：min_w ||Xw-y||² 与惩罚目标是否可解/唯一；目标、参数与驻点的收敛；数值条件数和迭代预算；另以模型与抽样条件判断参数误差、预测误差、稀疏支持恢复。

正文证据：[OLS理论分析](../../tex/03-models/01-classic-models/02-regression.tex)（`tex/03-models/01-classic-models/02-regression.tex:111`）；[正则化线性回归理论分析](../../tex/03-models/01-classic-models/02-regression.tex)（`tex/03-models/01-classic-models/02-regression.tex:316`）；[感知机](../../tex/03-models/01-classic-models/classification/01-lda-perceptron.tex)（`tex/03-models/01-classic-models/classification/01-lda-perceptron.tex:255`）；[支持向量机](../../tex/03-models/01-classic-models/classification/01-svm.tex)（`tex/03-models/01-classic-models/classification/01-svm.tex:1`）。

大纲证据：[回归](../classic-models-outline.md)（`plans/classic-models-outline.md:36`）；[分类](../classic-models-outline.md)（`plans/classic-models-outline.md:60`）；[统一术语与理论口径](../classic-models-outline.md)（`plans/classic-models-outline.md:329`）。

状态：有正文；大纲有对应职责说明。

归属边界：固定训练集可分时感知机有限更新、SVM全局优化、Lasso解唯一性、统计支持恢复是不同判断。

### C4 基于邻域的预测与样本外一致性

主要落点：**17.5**。联合落点：17.4、17.3、17.6。

对象：邻居集合、局部权重、带宽、条件均值或类别决策。 判断：在邻域收缩且邻居数量增加等条件下，预测是否趋近总体目标；固定查询的近邻检索是否正确、近似搜索带来多大偏差；LOESS的局部加权线性系统是否可解。

正文证据：[k-NN理论分析](../../tex/03-models/01-classic-models/02-regression.tex)（`tex/03-models/01-classic-models/02-regression.tex:879`）；[LOESS理论分析](../../tex/03-models/01-classic-models/02-regression.tex)（`tex/03-models/01-classic-models/02-regression.tex:987`）；[k近邻分类](../../tex/03-models/01-classic-models/classification/02-neighborhood.tex)（`tex/03-models/01-classic-models/classification/02-neighborhood.tex:6`）。

大纲证据：[回归](../classic-models-outline.md)（`plans/classic-models-outline.md:36`）；[分类](../classic-models-outline.md)（`plans/classic-models-outline.md:60`）。

状态：有正文；大纲有对应职责说明。

归属边界：精确k-NN选邻居后直接平均/投票，没有必须迭代收敛的参数训练。近邻搜索是工具；近似搜索误差若影响样本外一致性，再进入该统计结论的误差分析，不由此扩大17.4。

### C5 树、规则与分段函数怎样构造且控制复杂度

主要落点：**17.3、17.4**。联合落点：17.5、17.6。

对象：分区、阈值、路径、叶输出、规则覆盖、剪枝路径及样条基。 判断：哪些函数可由结构表达；贪心分裂/条件搜索改善哪个局部目标、如何停止、成本如何随结构增长；验证剪枝与留出风险是否支持选择。

正文证据：[基于树与规则的回归](../../tex/03-models/01-classic-models/02-regression.tex)（`tex/03-models/01-classic-models/02-regression.tex:1092`）；[基于树与规则的分类](../../tex/03-models/01-classic-models/classification/03-trees.tex)（`tex/03-models/01-classic-models/classification/03-trees.tex:1`）；[规则分类与RIPPER](../../tex/03-models/01-classic-models/classification/03-rules.tex)（`tex/03-models/01-classic-models/classification/03-rules.tex:1`）。

大纲证据：[回归](../classic-models-outline.md)（`plans/classic-models-outline.md:36`）；[分类](../classic-models-outline.md)（`plans/classic-models-outline.md:60`）。

状态：有正文；大纲有对应职责说明。

归属边界：剪枝或规则启发式不保证全局最优或最小总体风险；MARS重叠基不是标准树的互斥叶分区。

### C6 从原型与图割定义簇并求解

主要落点：**17.3、17.4**。联合落点：17.5、17.6。

对象：划分、中心/medoid、图边权、离散图割及连续谱松弛。 判断：Lloyd是否有限停止到分块不动点；谱子问题是否达到Rayleigh–Ritz最优、离散化损失是否可控；原型约束和样本外量化风险是否支持任务。

正文证据：[基于原型的聚类](../../tex/03-models/01-classic-models/04-clustering.tex)（`tex/03-models/01-classic-models/04-clustering.tex:12`）；[K-means理论分析](../../tex/03-models/01-classic-models/04-clustering.tex)（`tex/03-models/01-classic-models/04-clustering.tex:101`）；[基于图的聚类](../../tex/03-models/01-classic-models/04-clustering.tex)（`tex/03-models/01-classic-models/04-clustering.tex:614`）；[谱聚类理论分析](../../tex/03-models/01-classic-models/04-clustering.tex)（`tex/03-models/01-classic-models/04-clustering.tex:720`）。

大纲证据：[聚类](../classic-models-outline.md)（`plans/classic-models-outline.md:77`）。

状态：有正文；大纲有对应职责说明。

归属边界：连续谱松弛全局最优不等于原始图割或后续K-means全局最优。

### C7 密度、网格、子空间与层次结构怎样发现

主要落点：**17.3、17.5、17.6中的结构表示、统计恢复与稳定性**。连通分量遍历和合并规则作为工具记录，不单列学习问题；有明确学习目标的求解分析再联合17.4。

对象：邻域核心图、密度吸引域、网格统计、候选子空间、嵌套簇树。 判断：遍历是否完整找到核心连通分量；网格统计如何近似细节及节省访问；层次合并是否满足指定链接规则、有限停止或局部贪心准则；样本新增如何改变结构。

正文证据：[基于邻域的聚类](../../tex/03-models/01-classic-models/04-clustering.tex)（`tex/03-models/01-classic-models/04-clustering.tex:320`）；[DBSCAN理论分析](../../tex/03-models/01-classic-models/04-clustering.tex)（`tex/03-models/01-classic-models/04-clustering.tex:398`）；[基于网格与子空间的聚类](../../tex/03-models/01-classic-models/04-clustering.tex)（`tex/03-models/01-classic-models/04-clustering.tex:814`）；[基于层次的聚类](../../tex/03-models/01-classic-models/04-clustering.tex)（`tex/03-models/01-classic-models/04-clustering.tex:914`）；[AGNES理论分析](../../tex/03-models/01-classic-models/04-clustering.tex)（`tex/03-models/01-classic-models/04-clustering.tex:996`）。

大纲证据：[聚类](../classic-models-outline.md)（`plans/classic-models-outline.md:77`）。

状态：有正文；大纲有对应职责说明。

归属边界：DBSCAN的连通结构计算、AGNES的合并执行规则作为工具记录；它们本身不要求归入训练收敛。学习研究问题是候选结构表达什么、由有限样本恢复的结构是否代表总体，以及样本变化怎样影响结果。

### C8 低维表示究竟保留哪种量

主要落点：**17.3**。联合落点：17.4、17.5、17.6。

对象：投影/字典、成对视图的相关坐标、坐标Gram矩阵、距离、邻域、图路径、布局。 判断：判断精确重构/精确保距是否可行，或最佳逼近误差；CCA在成对视图和方差约束下最大化相关，区别于PCA重构；谱截断与应力/布局优化是否求到各自目标；低维坐标非唯一时比较子空间/Gram矩阵而不是逐坐标。

正文证据：[PCA理论分析](../../tex/03-models/01-classic-models/05-dimensionality-reduction.tex)（`tex/03-models/01-classic-models/05-dimensionality-reduction.tex:74`）；[典型相关分析](../../tex/03-models/01-classic-models/05-dimensionality-reduction.tex)（`tex/03-models/01-classic-models/05-dimensionality-reduction.tex:208`）；[基于距离的降维](../../tex/03-models/01-classic-models/05-dimensionality-reduction.tex)（`tex/03-models/01-classic-models/05-dimensionality-reduction.tex:708`）；[基于邻域的降维](../../tex/03-models/01-classic-models/05-dimensionality-reduction.tex)（`tex/03-models/01-classic-models/05-dimensionality-reduction.tex:871`）；[评价与选择](../../tex/03-models/01-classic-models/05-dimensionality-reduction.tex)（`tex/03-models/01-classic-models/05-dimensionality-reduction.tex:2287`）。

大纲证据：[降维](../classic-models-outline.md)（`plans/classic-models-outline.md:105`）。

状态：有正文；大纲有对应职责说明。

归属边界：t-SNE/UMAP训练点布局需另定样本外映射；二维分离、重构、距离、邻域与下游预测是不同证据。

### C9 随机投影的有限点几何保证

主要落点：**17.3的表示分析工具**。随机矩阵构造不单列学习问题；研究映射误差对学习风险或扰动响应的影响时，再联合17.5或17.6。

对象：抽样前固定的有限点集、随机矩阵Π、输出维数k。 判断：以高概率同时控制所有固定点对的距离相对失真；所需k与点数/失败概率/误差容限的关系。

正文证据：[随机投影](../../tex/03-models/01-classic-models/05-dimensionality-reduction.tex)（`tex/03-models/01-classic-models/05-dimensionality-reduction.tex:495`）；[随机投影理论分析](../../tex/03-models/01-classic-models/05-dimensionality-reduction.tex)（`tex/03-models/01-classic-models/05-dimensionality-reduction.tex:525`）。

大纲证据：[降维](../classic-models-outline.md)（`plans/classic-models-outline.md:105`）。

状态：有正文；大纲有对应职责说明。

归属边界：此处随机性来自计算中的矩阵抽取，既没有数据拟合迭代，也不是从总体采样引出的学习泛化。

### C10 潜在成分与生成因素是否可识别

主要落点：**17.5**。联合落点：17.3、17.4、17.6。

对象：混合分布、ICA源、载荷、低维潜变量、观测律与等价参数。 判断：观测律相同是否仍允许不同潜在解释；识别可恢复到排列/尺度/旋转等什么等价类；模型阶数、噪声和附加假设提供哪些信息；计算边缘/后验与EM求解分开。

正文证据：[基于概率的聚类](../../tex/03-models/01-classic-models/04-clustering.tex)（`tex/03-models/01-classic-models/04-clustering.tex:1080`）；[GMM编号置换与泛化分析](../../tex/03-models/01-classic-models/04-clustering.tex)（`tex/03-models/01-classic-models/04-clustering.tex:1266`）；[ICA模型结构](../../tex/03-models/01-classic-models/05-dimensionality-reduction.tex)（`tex/03-models/01-classic-models/05-dimensionality-reduction.tex:277`）；[基于概率的降维](../../tex/03-models/01-classic-models/05-dimensionality-reduction.tex)（`tex/03-models/01-classic-models/05-dimensionality-reduction.tex:1782`）；[PPCA与FA理论分析](../../tex/03-models/01-classic-models/05-dimensionality-reduction.tex)（`tex/03-models/01-classic-models/05-dimensionality-reduction.tex:1993`）。

大纲证据：[聚类](../classic-models-outline.md)（`plans/classic-models-outline.md:77`）；[降维](../classic-models-outline.md)（`plans/classic-models-outline.md:105`）。

状态：有正文；大纲有对应职责说明。

归属边界：更充分优化不能消除总体不可识别；成分数不自动等于业务类别数；GMM退化也不是标签置换。

### C11 标签稀缺、未标注数据与关系知识如何进入学习

主要落点：**17.5**。联合落点：17.3、17.4；可靠性变化联合17.6；用于行动要求时才联合17.7。

对象：有/无标签集合、图平滑、伪标签、潜变量、must/cannot-link或种子。 判断：输入分布中的结构是否携带类别信息；给定监督目标与假设后怎样形成经验目标/约束；传播是否达到边界条件下的解、伪标签错误怎样传播；监督质量是否足以支持语义。

正文证据：[半监督分类](../../tex/03-models/01-classic-models/classification/06-semisupervised.tex)（`tex/03-models/01-classic-models/classification/06-semisupervised.tex:1`）；[Label Propagation](../../tex/03-models/01-classic-models/classification/06-semisupervised.tex)（`tex/03-models/01-classic-models/classification/06-semisupervised.tex:164`）；[TSVM](../../tex/03-models/01-classic-models/classification/06-semisupervised.tex)（`tex/03-models/01-classic-models/classification/06-semisupervised.tex:373`）；[半监督聚类](../../tex/03-models/01-classic-models/04-clustering.tex)（`tex/03-models/01-classic-models/04-clustering.tex:1311`）。

大纲证据：[分类](../classic-models-outline.md)（`plans/classic-models-outline.md:60`）；[聚类](../classic-models-outline.md)（`plans/classic-models-outline.md:77`）。

状态：有正文；大纲有对应职责说明。

归属边界：未标注样本增多不自动使分类好；半监督标签条件可叠加不同模型，不宜作为额外互斥数学主类。

### C12 多成员的依赖与序贯/二阶段组合

主要落点：**17.5、17.4**。联合落点：17.3、17.6。

对象：成员输出、误差协方差、Bootstrap机制、函数增量、折外元特征。 判断：平均风险/方差是否因成员依赖降低；Boosting的每轮增量怎样近似降低固定损失；Stacking的元特征是否遵守信息隔离、验证选择是否接近指定库内oracle风险。

正文证据：[集成学习](../../tex/03-models/01-classic-models/06-ensemble-learning.tex)（`tex/03-models/01-classic-models/06-ensemble-learning.tex:1`）；[成员质量、错误依赖与多样性](../../tex/03-models/01-classic-models/ensemble-learning/01-overview.tex)（`tex/03-models/01-classic-models/ensemble-learning/01-overview.tex:45`）；[基于Bagging的集成](../../tex/03-models/01-classic-models/ensemble-learning/02-bagging.tex)（`tex/03-models/01-classic-models/ensemble-learning/02-bagging.tex:1`）；[基于Boosting的集成](../../tex/03-models/01-classic-models/ensemble-learning/03-boosting.tex)（`tex/03-models/01-classic-models/ensemble-learning/03-boosting.tex:1`）；[基于Stacking的集成](../../tex/03-models/01-classic-models/ensemble-learning/04-stacking.tex)（`tex/03-models/01-classic-models/ensemble-learning/04-stacking.tex:1`）。

大纲证据：[集成概述](../classic-models-outline.md)（`plans/classic-models-outline.md:126`）；[Bagging](../classic-models-outline.md)（`plans/classic-models-outline.md:150`）；[Boosting](../classic-models-outline.md)（`plans/classic-models-outline.md:182`）；[Stacking](../classic-models-outline.md)（`plans/classic-models-outline.md:228`）。

状态：有正文；大纲有对应职责说明。

归属边界：Bootstrap成员通常依赖同一份原数据，不能当作新增独立观测；Boosting重加权不必是环境P→Q迁移。

### C13 选择、路由、蒸馏与资源约束

主要落点：**17.3、17.4**。联合落点：17.5；资源预算的优化仍属17.4，影响后续行动环境时才联合17.7。

对象：固定成员子集、输入相关路由、教师与学生映射、存储/延迟成本。 判断：固定池内组合的经验最优和资源权衡；学生类能否逼近教师、拟合误差如何影响下游表现；按输入选成员的能力估计是否可靠。

正文证据：[成员选择与集成简化](../../tex/03-models/01-classic-models/ensemble-learning/05-selection-compression.tex)（`tex/03-models/01-classic-models/ensemble-learning/05-selection-compression.tex:1`）；[预测质量与资源成本](../../tex/03-models/01-classic-models/ensemble-learning/06-evaluation.tex)（`tex/03-models/01-classic-models/ensemble-learning/06-evaluation.tex:56`）。

大纲证据：[成员选择与集成简化](../classic-models-outline.md)（`plans/classic-models-outline.md:262`）；[模型选择与评价](../classic-models-outline.md)（`plans/classic-models-outline.md:284`）。

状态：有正文；大纲有对应职责说明。

归属边界：名称含“动态选择”不意味着行动改变环境；通常是静态输入映射的一部分。

### C14 评价协议、覆盖与结构的外部验证

主要落点：**17.5**。联合落点：17.6、17.4；任务用途判断联合17.7。

对象：训练/验证/校准/测试样本、评分、覆盖事件、簇匹配和样本外机制。 判断：独立证据能否支持总体风险、概率校准、区间覆盖、结构可复制性；预处理和选择是否泄漏；预算和用途一致时比较哪些量。

正文证据：[评价与选择](../../tex/03-models/01-classic-models/02-regression.tex)（`tex/03-models/01-classic-models/02-regression.tex:1540`）；[模型选择与评价](../../tex/03-models/01-classic-models/03-classification.tex)（`tex/03-models/01-classic-models/03-classification.tex:21`）；[评价与选择](../../tex/03-models/01-classic-models/04-clustering.tex)（`tex/03-models/01-classic-models/04-clustering.tex:1524`）；[评价与选择](../../tex/03-models/01-classic-models/05-dimensionality-reduction.tex)（`tex/03-models/01-classic-models/05-dimensionality-reduction.tex:2287`）；[数据隔离与泄漏控制](../../tex/03-models/01-classic-models/ensemble-learning/06-evaluation.tex)（`tex/03-models/01-classic-models/ensemble-learning/06-evaluation.tex:30`）。

大纲证据：[四个任务章节的职责与核心问题](../classic-models-outline.md)（`plans/classic-models-outline.md:27`）；[模型选择与评价](../classic-models-outline.md)（`plans/classic-models-outline.md:284`）。

状态：有正文；大纲有对应职责说明。

归属边界：泛化、校准、覆盖、训练目标和聚类稳定性不能互相替代；泛化不要求P改变。

## 逐组覆盖：神经网络模型

### N1 函数复合与结构先验带来哪些表达能力

主要落点：**17.3**。联合落点：17.5、17.4、17.6。

对象：前馈复合、激活、深宽、局部共享、置换/几何对称的函数类。 判断：目标能否精确表示/以何规模逼近；结构是否满足平移或重编号等变性；参数共享怎样限制候选类及偏差。

正文证据：[从人工特征到可学习的表示](../../tex/03-models/02-neural-network-models/01-overview.tex)（`tex/03-models/02-neural-network-models/01-overview.tex:11`）；[表达性](../../tex/03-models/02-neural-network-models/02-feedforward-networks.tex)（`tex/03-models/02-neural-network-models/02-feedforward-networks.tex:833`）；[卷积神经网络概述](../../tex/03-models/02-neural-network-models/03-convolutional-networks.tex)（`tex/03-models/02-neural-network-models/03-convolutional-networks.tex:9`）；[网络结构](../../tex/03-models/02-neural-network-models/05-graph-networks.tex)（`tex/03-models/02-neural-network-models/05-graph-networks.tex:46`）；[几何关系与对称性约束](../../tex/03-models/02-neural-network-models/05-graph-networks.tex)（`tex/03-models/02-neural-network-models/05-graph-networks.tex:660`）。

大纲证据：[可学习表示](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:37`）；[前馈理论分析](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:177`）；[图神经网络概述](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:578`）；[图网络扩展](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:670`）。

状态：有正文；大纲有对应职责说明。

归属边界：参数数量不是全部表达/学习复杂度；对称性正确还不等于任务信息充分。

### N2 固定网络运算的等价性、可见范围与执行资源

判定：**固定运算与实现主要是工具记录，不单列学习研究问题**。候选表示限制归17.3；近似运算对学习收敛、总体风险或扰动响应的影响分别联合17.4、17.5、17.6。

对象：卷积及快速变换、注意力掩码、位置表示、缓存、稀疏/低秩读取、条件计算路径。 判断：不同实现是否保留同一映射，近似算子误差多大；输入在计算时是否可见；计算量、存储、访存和序贯深度怎样改变。

正文证据：[卷积的实现](../../tex/03-models/02-neural-network-models/03-convolutional-networks.tex)（`tex/03-models/02-neural-network-models/03-convolutional-networks.tex:274`）；[与RNN/LSTM的比较](../../tex/03-models/02-neural-network-models/06-transformer.tex)（`tex/03-models/02-neural-network-models/06-transformer.tex:53`）；[Transformer的扩展](../../tex/03-models/02-neural-network-models/06-transformer.tex)（`tex/03-models/02-neural-network-models/06-transformer.tex:650`）；[混合专家](../../tex/03-models/02-neural-network-models/06-transformer.tex)（`tex/03-models/02-neural-network-models/06-transformer.tex:1014`）；[序列转换与生成](../../tex/03-models/02-neural-network-models/06-transformer.tex)（`tex/03-models/02-neural-network-models/06-transformer.tex:1221`）。

大纲证据：[卷积运算](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:211`）；[Transformer概述](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:742`）；[Transformer扩展](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:849`）；[序列转换与生成](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:962`）。

状态：有正文；大纲有对应职责说明。

归属边界：训练目标仍同一不代表运算必为训练优化；训练并行不推出自回归采样并行；MoE路由通常不是环境闭环策略。

### N3 隐状态保留历史与固定状态计算

主要落点：**17.3的历史表示能力**。截断等近似对学习收敛的影响联合17.4，预测与响应联合17.5、17.6；固定状态计算仅作工具记录，参与行动决策时联合17.7。

对象：RNN/储备池状态、门、记忆投影、神经SSM、递推或关联扫描。 判断：历史经压缩后能否区分任务所需输入；固定参数的状态递推是否稳定/忘记初态；递推与卷积/扫描何时等价；截断梯度误差及执行代价。

正文证据：[循环神经网络概述](../../tex/03-models/02-neural-network-models/04-recurrent-networks.tex)（`tex/03-models/02-neural-network-models/04-recurrent-networks.tex:8`）；[储备池](../../tex/03-models/02-neural-network-models/04-recurrent-networks.tex)（`tex/03-models/02-neural-network-models/04-recurrent-networks.tex:311`）；[状态空间模型](../../tex/03-models/02-neural-network-models/04-recurrent-networks.tex)（`tex/03-models/02-neural-network-models/04-recurrent-networks.tex:641`）；[理论分析](../../tex/03-models/02-neural-network-models/04-recurrent-networks.tex)（`tex/03-models/02-neural-network-models/04-recurrent-networks.tex:1260`）。

大纲证据：[基础循环网络](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:362`）；[储备池](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:424`）；[状态空间模型](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:466`）；[理论分析](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:540`）。

状态：有正文；大纲有对应职责说明。

归属边界：内部状态反馈不是行动经环境反馈；状态收敛、参数训练收敛和预测风险不同。

### N4 图传播的固定点、区分信息与瓶颈

主要落点：**17.3的表示与信息限制**。扰动响应和泛化联合17.6、17.5；固定点计算作为工具，其误差影响训练收敛时联合17.4。

对象：消息聚合、重复传播算子、图拓扑、有限维表示。 判断：固定参数传播是否有唯一固定点及误差残差；深度增加是否造成节点表示趋同或远程信息压缩；输入/边变化如何影响输出；样本单位是否独立。

正文证据：[循环图神经网络](../../tex/03-models/02-neural-network-models/05-graph-networks.tex)（`tex/03-models/02-neural-network-models/05-graph-networks.tex:508`）；[收敛与信息传播](../../tex/03-models/02-neural-network-models/05-graph-networks.tex)（`tex/03-models/02-neural-network-models/05-graph-networks.tex:690`）；[泛化能力](../../tex/03-models/02-neural-network-models/05-graph-networks.tex)（`tex/03-models/02-neural-network-models/05-graph-networks.tex:778`）。

大纲证据：[循环图网络](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:650`）；[理论分析](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:690`）。

状态：有正文；大纲有对应职责说明。

归属边界：过平滑、过压缩及状态求根不是同一“泛化不好”；固定点梯度不能直接用于尚未收敛的有限展开。

### N5 梯度计算与近似信用分配

判定：**求导本身是求解工具**。近似梯度是否改变学习目标、破坏下降或收敛，归17.4；其引起的响应变化再联合17.6。

对象：计算图、前/后向自动微分、共享参数贡献、时间展开、阈值替代导数。 判断：所得梯度是否为指定固定参数程序的正确导数；舍入、数值差分、截断、替代梯度造成什么误差；求导成本和状态存储如何控制。

正文证据：[反向传播](../../tex/03-models/02-neural-network-models/02-feedforward-networks.tex)（`tex/03-models/02-neural-network-models/02-feedforward-networks.tex:595`）；[自动梯度计算](../../tex/03-models/02-neural-network-models/02-feedforward-networks.tex)（`tex/03-models/02-neural-network-models/02-feedforward-networks.tex:751`）；[卷积层反向传播](../../tex/03-models/02-neural-network-models/03-convolutional-networks.tex)（`tex/03-models/02-neural-network-models/03-convolutional-networks.tex:1020`）；[替代梯度与时间反向传播](../../tex/03-models/02-neural-network-models/07-spiking-networks.tex)（`tex/03-models/02-neural-network-models/07-spiking-networks.tex:255`）。

大纲证据：[参数学习](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:149`）；[卷积参数学习](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:292`）；[脉冲参数学习](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1018`）。

状态：有正文；大纲有对应职责说明。

归属边界：正确求导不等于更新下降或全局收敛；局部生物可塑性规则也不自动优化同一任务损失。

### N6 非凸与随机优化怎样达到可声明的结果

主要落点：**17.4**。联合落点：17.5、17.6。

对象：参数目标、曲率、梯度噪声、动量/预条件状态、初始化、批量和步长。 判断：确定/随机序列是否到驻点、目标或参数是否收敛；误差与时间/存储预算如何折中；不同优化器是否选出不同低经验误差解。

正文证据：[主要挑战](../../tex/03-models/02-neural-network-models/08-training.tex)（`tex/03-models/02-neural-network-models/08-training.tex:16`）；[优化方法](../../tex/03-models/02-neural-network-models/08-training.tex)（`tex/03-models/02-neural-network-models/08-training.tex:112`）；[收敛性](../../tex/03-models/02-neural-network-models/06-transformer.tex)（`tex/03-models/02-neural-network-models/06-transformer.tex:1120`）；[优化算法的隐式偏置](../../tex/03-models/02-neural-network-models/09-generalization.tex)（`tex/03-models/02-neural-network-models/09-generalization.tex:189`）。

大纲证据：[神经网络的训练](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1056`）；[优化方法](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1082`）；[隐式偏置](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1342`）。

状态：有正文；大纲有对应职责说明。

归属边界：噪声方差和有偏截断不同；Muon更新整形不等于损失上的牛顿法；优化停滞不证明好解。

### N7 归一化与连接改变什么计算/信息/训练条件

主要落点：**17.3、17.4**。联合落点：17.5、17.6。

对象：输入/隐藏统计、权重参数化、Jacobian、残差/门/密集路径、持续参数约束。 判断：是否保留任务需要的信息、如何改变导数尺度和条件数；统计估计的采样范围是否与部署相符；对输入扰动的放大和训练误差如何变化。

正文证据：[归一化方法](../../tex/03-models/02-neural-network-models/08-training.tex)（`tex/03-models/02-neural-network-models/08-training.tex:564`）；[参数与结构的改进](../../tex/03-models/02-neural-network-models/08-training.tex)（`tex/03-models/02-neural-network-models/08-training.tex:1004`）；[支持更深的网络结构](../../tex/03-models/02-neural-network-models/03-convolutional-networks.tex)（`tex/03-models/02-neural-network-models/03-convolutional-networks.tex:1091`）。

大纲证据：[归一化方法](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1162`）；[参数与结构的改进](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1230`）；[更深网络结构](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:306`）。

状态：有正文；大纲有对应职责说明。

归属边界：优化器改更新，归一化改程序，连接改路径；不得把三者都写成同一固定目标的求解器。

### N8 有限样本与结构/算法选择怎样决定泛化

主要落点：**17.5**。联合落点：17.3、17.4、17.6。

对象：总体P、训练样本集、样本单位、候选函数/范数、实际学得的参数与解。 判断：经验到总体风险差、不同选择后的留出风险和有效复杂度；序列/图内依赖与独立序列/图数量怎样进入保证；长度外推和分布变化另外比较。

正文证据：[可学习性](../../tex/03-models/02-neural-network-models/02-feedforward-networks.tex)（`tex/03-models/02-neural-network-models/02-feedforward-networks.tex:886`）；[理论分析](../../tex/03-models/02-neural-network-models/03-convolutional-networks.tex)（`tex/03-models/02-neural-network-models/03-convolutional-networks.tex:1216`）；[泛化能力](../../tex/03-models/02-neural-network-models/04-recurrent-networks.tex)（`tex/03-models/02-neural-network-models/04-recurrent-networks.tex:1294`）；[泛化能力](../../tex/03-models/02-neural-network-models/05-graph-networks.tex)（`tex/03-models/02-neural-network-models/05-graph-networks.tex:778`）；[泛化能力](../../tex/03-models/02-neural-network-models/06-transformer.tex)（`tex/03-models/02-neural-network-models/06-transformer.tex:1168`）；[主要挑战](../../tex/03-models/02-neural-network-models/09-generalization.tex)（`tex/03-models/02-neural-network-models/09-generalization.tex:18`）。

大纲证据：[前馈理论](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:177`）；[卷积理论](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:322`）；[循环泛化](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:548`）；[图泛化](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:708`）；[Transformer泛化](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:940`）；[泛化主要挑战](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1276`）。

状态：有正文；大纲有对应职责说明。

归属边界：同分布泛化、长度外推、OOD不能混用；单图节点不是自动独立数据样本。

### N9 增强、随机训练、停止/平均与邻域目标

主要落点：**17.5**。联合落点：17.3、17.4、17.6。

对象：变换与标签规则、随机子网络、参数/激活噪声、轨迹选解、参数邻域。 判断：增强语义是否成立；随机化改变的期望训练目标为何；提前停止/平均选出的函数有何统计性质；SAM内层一阶近似与指定参数邻域最坏损失如何比较。

正文证据：[数据增强](../../tex/03-models/02-neural-network-models/09-generalization.tex)（`tex/03-models/02-neural-network-models/09-generalization.tex:56`）；[模型侧的泛化控制](../../tex/03-models/02-neural-network-models/09-generalization.tex)（`tex/03-models/02-neural-network-models/09-generalization.tex:100`）；[训练侧的泛化控制](../../tex/03-models/02-neural-network-models/09-generalization.tex)（`tex/03-models/02-neural-network-models/09-generalization.tex:140`）；[邻域最坏损失与SAM](../../tex/03-models/02-neural-network-models/09-generalization.tex)（`tex/03-models/02-neural-network-models/09-generalization.tex:221`）；[Dropout](../../tex/03-models/02-neural-network-models/09-generalization.tex)（`tex/03-models/02-neural-network-models/09-generalization.tex:268`）；[模型集成](../../tex/03-models/02-neural-network-models/09-generalization.tex)（`tex/03-models/02-neural-network-models/09-generalization.tex:329`）。

大纲证据：[数据增强](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1296`）；[模型侧控制](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1310`）；[训练侧控制](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1326`）；[模型集成](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1370`）。

状态：有正文；大纲有对应职责说明。

归属边界：生成视图不等于新增独立样本；Dropout可改期望目标；SAM是参数坐标邻域而非输入鲁棒；不必每项都硬落扰动。正文有SAM，大纲9.4未列单独SAM条目，属正文更细，不是正文缺失。

### N10 脉冲编码、事件动态与精度资源

主要落点：**17.3、17.4**。联合落点：17.6、17.5；进入行动策略时才17.7。

对象：事件时刻/计数编码、膜电位、阈值复位、延迟、观察窗口。 判断：整个编码—状态—读出是否区分任务信息；阈值切换是否破坏局部收缩；ANN→SNN转换的有限窗口误差以及事件执行成本/延迟如何比较。

正文证据：[网络结构](../../tex/03-models/02-neural-network-models/07-spiking-networks.tex)（`tex/03-models/02-neural-network-models/07-spiking-networks.tex:85`）；[人工网络到脉冲网络的转换](../../tex/03-models/02-neural-network-models/07-spiking-networks.tex)（`tex/03-models/02-neural-network-models/07-spiking-networks.tex:296`）；[时序表达与动态稳定性](../../tex/03-models/02-neural-network-models/07-spiking-networks.tex)（`tex/03-models/02-neural-network-models/07-spiking-networks.tex:323`）；[精度、延迟与事件数量](../../tex/03-models/02-neural-network-models/07-spiking-networks.tex)（`tex/03-models/02-neural-network-models/07-spiking-networks.tex:332`）。

大纲证据：[网络结构](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1004`）；[网络转换](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1028`）；[理论分析](../neural-network-models-outline.md)（`plans/neural-network-models-outline.md:1032`）。

状态：有正文；大纲有对应职责说明。

归属边界：α<1只是固定发放模式下的泄漏稳定性，不能证明含阈值循环网络全局稳定；低脉冲数不自动等于低端到端成本。

## 逐组覆盖：概率图模型

### P1 概率模型表示的合法性与条件独立语义

主要落点：**17.3**。联合落点：17.4、17.5。

对象：DAG/无向图、条件分布/势、模型族、归一化与图分离。 判断：局部分解是否定义合法联合律；Markov性与分解何时等价、图声明哪些独立性；严格正性、可归一化和量词边界。

正文证据：[图模型上的表示](../../tex/03-models/03-probabilistic-graphical-models/01-overview.tex)（`tex/03-models/03-probabilistic-graphical-models/01-overview.tex:30`）；[定义](../../tex/03-models/03-probabilistic-graphical-models/02-directed.tex)（`tex/03-models/03-probabilistic-graphical-models/02-directed.tex:8`）；[全局独立性](../../tex/03-models/03-probabilistic-graphical-models/02-directed.tex)（`tex/03-models/03-probabilistic-graphical-models/02-directed.tex:107`）；[因子分解](../../tex/03-models/03-probabilistic-graphical-models/03-undirected.tex)（`tex/03-models/03-probabilistic-graphical-models/03-undirected.tex:436`）。

大纲证据：[有向图模型](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:86`）；[无向图模型](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:165`）。

状态：有正文；大纲有对应职责说明。

归属边界：箭头不自动因果；图相连不证明固定参数分布依赖。

### P2 表示转换究竟保持分布还是模型类语义

主要落点：**17.3**。联合落点：17.4。

对象：道德化/弦化、因子作用域、同一p、独立性集合。 判断：转换能否保持同一联合函数/全部查询；是否丢失独立性或放宽模型族；团增大如何改变计算成本。

正文证据：[条件独立性关系](../../tex/03-models/03-probabilistic-graphical-models/04-representations.tex)（`tex/03-models/03-probabilistic-graphical-models/04-representations.tex:90`）；[因子分解关系](../../tex/03-models/03-probabilistic-graphical-models/04-representations.tex)（`tex/03-models/03-probabilistic-graphical-models/04-representations.tex:445`）；[因子图](../../tex/03-models/03-probabilistic-graphical-models/04-representations.tex)（`tex/03-models/03-probabilistic-graphical-models/04-representations.tex:670`）。

大纲证据：[图表示的转换与因子图](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:249`）。

状态：有正文；大纲有对应职责说明。

归属边界：改变图画法但保持p不必是17.6环境/模型扰动；图模型族比较应按17.3表示判断。

### P3 固定模型上的概率查询、归一化与消息缓存

判定：**工具，不单列学习研究问题**。固定模型的查询与缓存留在模型章；近似误差影响学习收敛或统计结论时，分别联合17.4或17.5。

对象：给定θ与证据e的边缘/条件概率、配分函数Z、后验期望及因子运算。 判断：求和/积分消元是否保持原查询答案；树宽/中间团、矩阵块决定多少资源；多次查询/新证据时缓存怎样正确复用；代数精确性与浮点误差分开。

正文证据：[推断问题与因子运算](../../tex/03-models/03-probabilistic-graphical-models/05-elimination.tex)（`tex/03-models/03-probabilistic-graphical-models/05-elimination.tex:8`）；[边缘概率变量消除](../../tex/03-models/03-probabilistic-graphical-models/05-elimination.tex)（`tex/03-models/03-probabilistic-graphical-models/05-elimination.tex:78`）；[算法分析](../../tex/03-models/03-probabilistic-graphical-models/05-elimination.tex)（`tex/03-models/03-probabilistic-graphical-models/05-elimination.tex:481`）；[团树传播](../../tex/03-models/03-probabilistic-graphical-models/06-junction-tree.tex)（`tex/03-models/03-probabilistic-graphical-models/06-junction-tree.tex:287`）；[算法分析](../../tex/03-models/03-probabilistic-graphical-models/06-junction-tree.tex)（`tex/03-models/03-probabilistic-graphical-models/06-junction-tree.tex:548`）。

大纲证据：[变量消除](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:323`）；[团树传播](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:389`）。

状态：正文与大纲均完整设置专章；作为工具来源保留，不要求第17章为其新增计算接口。

归属边界：这一组讨论固定模型的运算正确性，不计作学习研究问题的覆盖缺口。查询结果用于学习时，再明确它支持哪个收敛或统计判断。

### P4 最可能配置与边缘MAP优化

判定：**固定模型上的求解工具，不单列学习研究问题**。结构学习中调用此类求解时，其近似误差对学习收敛的影响可联合17.4。

对象：MPE完整配置、MAP目标子集、非目标未观测变量。 判断：max_z p(z,e) 与 max_y Σ_z p(y,z,e) 求什么配置；求和/最大化次序是否正确；凸/整数松弛、取整与原始—对偶间隙是否提供最优性证书。

正文证据：[MPE与MAP变量消除](../../tex/03-models/03-probabilistic-graphical-models/05-elimination.tex)（`tex/03-models/03-probabilistic-graphical-models/05-elimination.tex:354`）；[近似MPE](../../tex/03-models/03-probabilistic-graphical-models/07-variational.tex)（`tex/03-models/03-probabilistic-graphical-models/07-variational.tex:725`）；[条件能量模型](../../tex/03-models/03-probabilistic-graphical-models/12-energy-models.tex)（`tex/03-models/03-probabilistic-graphical-models/12-energy-models.tex:345`）。

大纲证据：[MPE与MAP](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:359`）；[近似MPE](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:499`）。

状态：有正文；大纲有对应职责说明。

归属边界：属于给定概率目标的优化，仍不是经验风险训练；MAP点不能替代边缘概率。

### P5 分布近似与数值求解误差分别是什么

判定：**固定后验的近似推断是工具记录**。学习推断网络的表示误差、训练收敛与样本外风险分别归17.3、17.4、17.5；近似E步对学习结论的影响也归相应分析。

对象：近似族Q、后验p(z|x)、伪边缘、局部曲率、消息固定点。 判断：min_{q∈Q}KL(q||p) 的最佳近似误差、数值优化误差、摊销误差；自由能驻点/消息收敛与边缘准确性有何关系；合法分布和伪边缘各能回答什么。

正文证据：[变分统一视角](../../tex/03-models/03-probabilistic-graphical-models/07-variational.tex)（`tex/03-models/03-probabilistic-graphical-models/07-variational.tex:17`）；[近似后验与边缘](../../tex/03-models/03-probabilistic-graphical-models/07-variational.tex)（`tex/03-models/03-probabilistic-graphical-models/07-variational.tex:168`）；[潜变量参数学习](../../tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex)（`tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex:317`）。

大纲证据：[变分与确定性近似](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:459`）；[潜变量参数学习](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:629`）。

状态：有正文；大纲有对应职责说明。

归属边界：VI确实有优化形式；Laplace局部展开和EP矩匹配不能仅凭“近似推断”一词继承全局KL最优化保证。

### P6 随机积分和目标分布采样是否正确

判定：**工具，不单列学习研究问题**。随机积分与固定分布采样留在模型章；仅在近似样本或积分误差影响学习收敛、统计结论时联合17.4、17.5。

对象：固定p、I=E_pφ、算法随机样本、重要性权重、Markov核、SMC粒子。 判断：控制积分误差/MCSE；加权估计支撑与矩条件；μK^k是否逼近目标p、长期平均是否一致；固定时间粒子数极限与链长度极限分别判断。

正文证据：[采样推断定义](../../tex/03-models/03-probabilistic-graphical-models/08-sampling.tex)（`tex/03-models/03-probabilistic-graphical-models/08-sampling.tex:8`）；[独立MC](../../tex/03-models/03-probabilistic-graphical-models/08-sampling.tex)（`tex/03-models/03-probabilistic-graphical-models/08-sampling.tex:73`）；[MCMC](../../tex/03-models/03-probabilistic-graphical-models/08-sampling.tex)（`tex/03-models/03-probabilistic-graphical-models/08-sampling.tex:201`）；[SMC](../../tex/03-models/03-probabilistic-graphical-models/08-sampling.tex)（`tex/03-models/03-probabilistic-graphical-models/08-sampling.tex:435`）；[算法分析](../../tex/03-models/03-probabilistic-graphical-models/08-sampling.tex)（`tex/03-models/03-probabilistic-graphical-models/08-sampling.tex:655`）。

大纲证据：[基于采样的近似推断](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:527`）。

状态：正文与大纲均有专章；保留工具来源，不作为第17章需补的独立研究类别。

归属边界：模拟样本数N不等于环境采样预算n；后验标准差不等于MCSE；平稳性不等于有限预算混合充分。该组不是必然优化。

### P7 已知结构下参数点与参数后验的学习

主要落点：**17.5、17.4**。联合落点：17.3、17.6。

对象：固定图族、θ、经验似然/先验、θ后验、模型期望、潜变量后验统计。 判断：MLE/MAP优化哪一个点目标；参数后验怎样由样本更新、后验预测如何积分；EM/GEM、近似E步与替代准则分别改善什么；有限样本、推断和优化误差如何拆开。

正文证据：[参数学习定义](../../tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex)（`tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex:8`）；[完整且无潜变量](../../tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex)（`tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex:61`）；[完整但有潜变量](../../tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex)（`tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex:317`）；[分布估计](../../tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex)（`tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex:710`）；[学习算法分析](../../tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex)（`tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex:836`）。

大纲证据：[参数学习](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:603`）。

状态：有正文；大纲有对应职责说明。

归属边界：完整记录可仍有主动设置的潜变量；保留后验不等于求MAP；对比散度有限链偏差不能伪装为精确似然梯度。

### P8 缺失与潜变量下观测究竟能确定什么

主要落点：**17.5**。联合落点：17.3、17.4、17.6。

对象：缺失指示机制、可见字段、潜变量、观测律、等价参数。 判断：缺失机制是否可忽略；相同观测律能否区分参数/潜在解释；还需什么外部测量、设计或约束；拟合给定模型不创造识别信息。

正文证据：[观测缺失下参数学习](../../tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex)（`tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex:641`）；[潜变量模型](../../tex/03-models/03-probabilistic-graphical-models/11-static-directed.tex)（`tex/03-models/03-probabilistic-graphical-models/11-static-directed.tex:187`）；[模型比较](../../tex/03-models/03-probabilistic-graphical-models/11-static-directed.tex)（`tex/03-models/03-probabilistic-graphical-models/11-static-directed.tex:563`）。

大纲证据：[观测缺失](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:649`）；[潜变量模型](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:799`）。

状态：有正文；大纲有对应职责说明。

归属边界：MNAR联合建模不自动可识别；标签交换、旋转等价、未充分优化是不同原因。

### P9 从依赖结构走到可识别的因果结构

主要落点：**17.5**。联合落点：17.3、17.4、17.6；主动受成本约束干预联合17.7。

对象：图族、独立性检验、结构分数、搜索、MEC/CPDAG/PAG、干预目标。 判断：数据和假设能确定哪个等价类/方向；检验/评分统计一致性与搜索最优性分开；Chow–Liu和图Lasso求给定准则；主动干预能增加何种信息。

正文证据：[结构学习定义](../../tex/03-models/03-probabilistic-graphical-models/10-structure-learning.tex)（`tex/03-models/03-probabilistic-graphical-models/10-structure-learning.tex:8`）；[有向结构学习](../../tex/03-models/03-probabilistic-graphical-models/10-structure-learning.tex)（`tex/03-models/03-probabilistic-graphical-models/10-structure-learning.tex:30`）；[无向结构学习](../../tex/03-models/03-probabilistic-graphical-models/10-structure-learning.tex)（`tex/03-models/03-probabilistic-graphical-models/10-structure-learning.tex:313`）；[因果发现](../../tex/03-models/03-probabilistic-graphical-models/10-structure-learning.tex)（`tex/03-models/03-probabilistic-graphical-models/10-structure-learning.tex:524`）；[算法分析](../../tex/03-models/03-probabilistic-graphical-models/10-structure-learning.tex)（`tex/03-models/03-probabilistic-graphical-models/10-structure-learning.tex:626`）。

大纲证据：[结构学习](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:703`）。

状态：有正文；大纲有对应职责说明。

归属边界：统计边恢复不自动因果；干预是改变机制的建模操作，但效应识别的主要判断仍属信息/识别，不能只按扰动归类。

### P10 模型模板怎样换取可计算的分布和结构输出

主要落点：**17.3**。联合落点：17.4、17.5；规则规定行动要求时才联合17.7。

对象：NB/TAN/AR、混合/线性/层次潜变量、Ising/Potts/RBM、神经能量、CRF、逻辑与关系模板。 判断：哪个变量参与归一化、哪个结构限制可表达关系；似然、后验、补全和生成分别能否计算；参数共享、落地规模和不可识别边界如何改变。

正文证据：[直接模型](../../tex/03-models/03-probabilistic-graphical-models/11-static-directed.tex)（`tex/03-models/03-probabilistic-graphical-models/11-static-directed.tex:10`）；[潜变量模型](../../tex/03-models/03-probabilistic-graphical-models/11-static-directed.tex)（`tex/03-models/03-probabilistic-graphical-models/11-static-directed.tex:187`）；[无向共同形式](../../tex/03-models/03-probabilistic-graphical-models/12-energy-models.tex)（`tex/03-models/03-probabilistic-graphical-models/12-energy-models.tex:8`）；[联合能量模型](../../tex/03-models/03-probabilistic-graphical-models/12-energy-models.tex)（`tex/03-models/03-probabilistic-graphical-models/12-energy-models.tex:58`）；[条件能量模型](../../tex/03-models/03-probabilistic-graphical-models/12-energy-models.tex)（`tex/03-models/03-probabilistic-graphical-models/12-energy-models.tex:345`）。

大纲证据：[静态有向](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:785`）；[静态无向](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:825`）。

状态：有正文；大纲有对应职责说明。

归属边界：预测条件概率、生成联合配置、最优标签序列的数学任务不同；关系模板共享参数不使实例独立。

### P11 状态预测、滤波、平滑与最可能路径

判定：**固定模型的滤波、平滑和路径求解是工具记录**。状态表示限制归17.3；模型由样本估计及统计恢复归17.5，学习收敛归17.4；响应扰动和行动后果分别联合17.6、17.7。

对象：动态随机状态、观测历史、时间接口、条件分布和路径。 判断：p(z_t|x_{1:t})、p(z_t|x_{1:T})等不同证据范围的查询如何递推；有限状态/线性高斯闭包何时精确；EKF/UKF/粒子近似误差、存储/在线成本分别判断。

正文证据：[动态共同形式](../../tex/03-models/03-probabilistic-graphical-models/13-dynamic.tex)（`tex/03-models/03-probabilistic-graphical-models/13-dynamic.tex:10`）；[离散状态](../../tex/03-models/03-probabilistic-graphical-models/13-dynamic.tex)（`tex/03-models/03-probabilistic-graphical-models/13-dynamic.tex:73`）；[连续与混合状态](../../tex/03-models/03-probabilistic-graphical-models/13-dynamic.tex)（`tex/03-models/03-probabilistic-graphical-models/13-dynamic.tex:305`）；[模型比较](../../tex/03-models/03-probabilistic-graphical-models/13-dynamic.tex)（`tex/03-models/03-probabilistic-graphical-models/13-dynamic.tex:637`）。

大纲证据：[动态有向与状态空间](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:885`）。

状态：有正文；大纲有对应职责说明。

归属边界：Kalman或HMM存在真实状态时间，也不能因此将主要问题硬落策略学习；没有行动时是动态概率推断。

### P12 密度建模、随机生成与人工噪声过程

主要落点：**17.3、17.5；训练收敛归17.4**。固定模型的采样执行只作工具记录；指定扰动/条件改变时联合17.6。

对象：数据真实律P、模型律q_θ、噪声U及生成器G_θ、Flow换元、VAE潜变量、人工扩散过程、概率电路结构。 判断：模型是否归一化/能逼近数据律；训练的是似然、ELBO还是简化去噪目标；给定θ后密度、条件后验和随机样本各如何获得；生成律与数值步数误差怎样比较；概率电路的光滑/可分解结构何时换取精确边缘化。

正文证据：[生成共同问题](../../tex/03-models/03-probabilistic-graphical-models/14-generative.tex)（`tex/03-models/03-probabilistic-graphical-models/14-generative.tex:8`）；[VAE](../../tex/03-models/03-probabilistic-graphical-models/14-generative.tex)（`tex/03-models/03-probabilistic-graphical-models/14-generative.tex:27`）；[Flow](../../tex/03-models/03-probabilistic-graphical-models/14-generative.tex)（`tex/03-models/03-probabilistic-graphical-models/14-generative.tex:215`）；[扩散与分数生成](../../tex/03-models/03-probabilistic-graphical-models/14-generative.tex)（`tex/03-models/03-probabilistic-graphical-models/14-generative.tex:356`）；[关系比较](../../tex/03-models/03-probabilistic-graphical-models/14-generative.tex)（`tex/03-models/03-probabilistic-graphical-models/14-generative.tex:742`）。

大纲证据：[概率生成模型](../probabilistic-graphical-models-outline.md)（`plans/probabilistic-graphical-models-outline.md:915`）。

状态：有正文；大纲有对应职责说明。

归属边界：基础U经G推送产生模型律(G_θ)#ν；生成质量不能只用训练目标值证明；人工扩散索引不是任务时间/策略环境。GAN本部分只作边界对照，并未承诺完整对抗博弈训练。

## 本轮发现的边界与正文/大纲差异

- P3/P4/P6的纯计算以及P11、C4、C7中的运算部分作为工具记录，不计作第17章学习研究问题的遗漏；不再据此建议扩大17.4。模型表示、参数学习、训练收敛、总体恢复和稳定性等实际研究问题仍保留相应落点。
- 群体、公平、隐私与状态安全在第三卷不是独立主体；本报告不因未来可能应用就给每个模型强贴17.7。第三卷主要提供映射、估计和计算工具。
- 神经泛化正文有“邻域最坏损失与SAM”（09-generalization.tex:221）；现大纲9.4.4后直接权重衰减，未给SAM单项标题。正文更细，不构成第17章框架漏覆盖，也不在本轮修改计划。
- 概率图大纲将决策网络/影响图只作推断接口，GAN只作隐式分布边界；因果效应、do演算和反事实不在这一部分系统展开。不能把这些范围外任务宣称为第三卷已完成的研究覆盖。
- 神经概述的生物启发和历史，以及各部分历史/应用动机，提供背景而不是每段都承诺一个独立数学保证；本轮没有把这些叙述拆成虚构研究任务。

## 检查文件与粒度

粒度代码：**B**＝完整标题清点＋主要章/节问题入口＋对应代表定义/求解/分析/评价段；**F**＝片段全部标题＋主要问题入口/对应关键说明（未逐条证明）；**I**＝入口/包含链检查；**O**＝完整大纲标题＋对应问题的职责、分析和边界说明。状态“接入”仅指源链可达，不等于已经验证全部排版/证明。

| 文件 | 行数 | 源链/状态 | 本轮粒度与重点 |
| --- | ---: | --- | --- |
| [tex/03-models/01-classic-models/01-overview.tex](../../tex/03-models/01-classic-models/01-overview.tex) | 96 | 接入 | B：任务差异、五种建模思路、公共核入口 |
| [tex/03-models/01-classic-models/02-regression.tex](../../tex/03-models/01-classic-models/02-regression.tex) | 1574 | 接入 | B：预测对象；OLS/正则化/局部拟合理论；GPR后验与超参数；评价协议 |
| [tex/03-models/01-classic-models/03-classification.tex](../../tex/03-models/01-classic-models/03-classification.tex) | 89 | 接入 | B：类别/得分/概率区分；片段引用与测试/校准协议 |
| [tex/03-models/01-classic-models/04-clustering.tex](../../tex/03-models/01-classic-models/04-clustering.tex) | 1580 | 接入 | B：原型、密度、图、网格/子空间、层次、混合、共识、约束与评价 |
| [tex/03-models/01-classic-models/05-dimensionality-reduction.tex](../../tex/03-models/01-classic-models/05-dimensionality-reduction.tex) | 2381 | 接入 | B：线性/核、距离/邻域/概率表示；ICA识别、JL随机保证、PCA/MDS及评价 |
| [tex/03-models/01-classic-models/06-ensemble-learning.tex](../../tex/03-models/01-classic-models/06-ensemble-learning.tex) | 27 | 接入 | B：成员依赖、三类机制、全部片段入口与小结 |
| [tex/03-models/01-classic-models/classification/01-lda-perceptron.tex](../../tex/03-models/01-classic-models/classification/01-lda-perceptron.tex) | 537 | 接入 | F：LDA统计/几何、可分性与错误驱动更新 |
| [tex/03-models/01-classic-models/classification/01-linear.tex](../../tex/03-models/01-classic-models/classification/01-linear.tex) | 94 | 接入 | F：线性学习依据、LDA/SVM包含链、扩展模型角色 |
| [tex/03-models/01-classic-models/classification/01-svm.tex](../../tex/03-models/01-classic-models/classification/01-svm.tex) | 676 | 接入 | F：间隔/约束/核分开；固定优化问题与边界 |
| [tex/03-models/01-classic-models/classification/02-neighborhood.tex](../../tex/03-models/01-classic-models/classification/02-neighborhood.tex) | 319 | 接入 | F：局部类别信息、风险与近邻压缩 |
| [tex/03-models/01-classic-models/classification/03-rules.tex](../../tex/03-models/01-classic-models/classification/03-rules.tex) | 167 | 接入 | F：规则覆盖、剪枝/启发式、树/规则比较 |
| [tex/03-models/01-classic-models/classification/03-trees.tex](../../tex/03-models/01-classic-models/classification/03-trees.tex) | 185 | 接入 | F：结构搜索、叶输出、复杂度 |
| [tex/03-models/01-classic-models/classification/04-probability.tex](../../tex/03-models/01-classic-models/classification/04-probability.tex) | 625 | 接入 | F：Logistic/NB/GDA的条件/联合假设、概率与决策 |
| [tex/03-models/01-classic-models/classification/05-ensemble.tex](../../tex/03-models/01-classic-models/classification/05-ensemble.tex) | 25 | 接入 | F：组合输出的分类语义 |
| [tex/03-models/01-classic-models/classification/06-semisupervised.tex](../../tex/03-models/01-classic-models/classification/06-semisupervised.tex) | 660 | 接入 | F：标签条件、输入结构假设、自训练/传播/TSVM与扩展 |
| [tex/03-models/01-classic-models/common/kernels.tex](../../tex/03-models/01-classic-models/common/kernels.tex) | 282 | 接入 | F：合法内积核与Mercer条件分开、矩阵成本/中心化 |
| [tex/03-models/01-classic-models/ensemble-learning/01-overview.tex](../../tex/03-models/01-classic-models/ensemble-learning/01-overview.tex) | 92 | 接入 | F：成员接口、输出语义与协方差 |
| [tex/03-models/01-classic-models/ensemble-learning/02-bagging.tex](../../tex/03-models/01-classic-models/ensemble-learning/02-bagging.tex) | 117 | 接入 | F：Bootstrap/特征/阈值随机性及成本和质量 |
| [tex/03-models/01-classic-models/ensemble-learning/03-boosting.tex](../../tex/03-models/01-classic-models/ensemble-learning/03-boosting.tex) | 312 | 接入 | F：加法目标、近似梯度/曲率、统计量压缩及目标泄漏 |
| [tex/03-models/01-classic-models/ensemble-learning/04-stacking.tex](../../tex/03-models/01-classic-models/ensemble-learning/04-stacking.tex) | 110 | 接入 | F：折外输入、受约束组合、库内oracle风险 |
| [tex/03-models/01-classic-models/ensemble-learning/05-selection-compression.tex](../../tex/03-models/01-classic-models/ensemble-learning/05-selection-compression.tex) | 76 | 接入 | F：固定子集、输入路由、教师逼近及资源 |
| [tex/03-models/01-classic-models/ensemble-learning/06-evaluation.tex](../../tex/03-models/01-classic-models/ensemble-learning/06-evaluation.tex) | 76 | 接入 | F：数据职责隔离、成员依赖、全路径质量与资源 |
| [tex/03-models/01-classic-models/part.tex](../../tex/03-models/01-classic-models/part.tex) | 9 | 接入 | I：完整入口及包含关系 |
| [tex/03-models/02-neural-network-models/01-overview.tex](../../tex/03-models/02-neural-network-models/01-overview.tex) | 451 | 接入 | B：学习表示、结构/编码交叉分类；生物历史作为背景 |
| [tex/03-models/02-neural-network-models/02-feedforward-networks.tex](../../tex/03-models/02-neural-network-models/02-feedforward-networks.tex) | 1021 | 接入 | B：复合/激活/输出、求导/自动微分、表达与可学习性 |
| [tex/03-models/02-neural-network-models/03-convolutional-networks.tex](../../tex/03-models/02-neural-network-models/03-convolutional-networks.tex) | 1374 | 接入 | B：局部共享、卷积实现、结构/求导、泛化与空间输出 |
| [tex/03-models/02-neural-network-models/04-recurrent-networks.tex](../../tex/03-models/02-neural-network-models/04-recurrent-networks.tex) | 1381 | 接入 | B：状态/读出/梯度分开、储备池/门/注意力/SSM、泛化单位 |
| [tex/03-models/02-neural-network-models/05-graph-networks.tex](../../tex/03-models/02-neural-network-models/05-graph-networks.tex) | 890 | 接入 | B：编号对称、消息/谱空域、固定点、过平滑/过压缩、图数据依赖 |
| [tex/03-models/02-neural-network-models/06-transformer.tex](../../tex/03-models/02-neural-network-models/06-transformer.tex) | 1261 | 接入 | B：可见性/位置/注意力、实现资源、求导、结构与外推边界 |
| [tex/03-models/02-neural-network-models/07-spiking-networks.tex](../../tex/03-models/02-neural-network-models/07-spiking-networks.tex) | 372 | 接入 | B：事件编码/状态/复位、替代梯度、转换误差及动态/成本 |
| [tex/03-models/02-neural-network-models/08-training.tex](../../tex/03-models/02-neural-network-models/08-training.tex) | 1117 | 接入 | B：非凸/曲率/非精确梯度、更新算法、归一化、参数与连接 |
| [tex/03-models/02-neural-network-models/09-generalization.tex](../../tex/03-models/02-neural-network-models/09-generalization.tex) | 359 | 接入 | B：经验到总体、增强/目标/算法位置、SAM、随机化/选解/集成 |
| [tex/03-models/02-neural-network-models/part.tex](../../tex/03-models/02-neural-network-models/part.tex) | 12 | 接入 | I：完整入口及包含关系 |
| [tex/03-models/03-probabilistic-graphical-models/01-overview.tex](../../tex/03-models/03-probabilistic-graphical-models/01-overview.tex) | 143 | 接入 | B：分布/单值、图表示、推断/学习区别 |
| [tex/03-models/03-probabilistic-graphical-models/02-directed.tex](../../tex/03-models/03-probabilistic-graphical-models/02-directed.tex) | 633 | 接入 | B：Markov语义、全称/存在量词、归一化分解及局部参数化 |
| [tex/03-models/03-probabilistic-graphical-models/03-undirected.tex](../../tex/03-models/03-probabilistic-graphical-models/03-undirected.tex) | 877 | 接入 | B：对称关系、正性/归一化、Markov与因子分解条件 |
| [tex/03-models/03-probabilistic-graphical-models/04-representations.tex](../../tex/03-models/03-probabilistic-graphical-models/04-representations.tex) | 793 | 接入 | B：同一分布与图模型族、独立性转换、局部计算 |
| [tex/03-models/03-probabilistic-graphical-models/05-elimination.tex](../../tex/03-models/03-probabilistic-graphical-models/05-elimination.tex) | 712 | 接入 | B：查询/证据、求和与最大化顺序、答案/宽度/资源 |
| [tex/03-models/03-probabilistic-graphical-models/06-junction-tree.tex](../../tex/03-models/03-probabilistic-graphical-models/06-junction-tree.tex) | 695 | 接入 | B：子树消息、运行交集、缓存/证据更新及精确性 |
| [tex/03-models/03-probabilistic-graphical-models/07-variational.tex](../../tex/03-models/03-probabilistic-graphical-models/07-variational.tex) | 962 | 接入 | B：后验与MPE两线、合法分布/伪边缘、逼近和优化误差 |
| [tex/03-models/03-probabilistic-graphical-models/08-sampling.tex](../../tex/03-models/03-probabilistic-graphical-models/08-sampling.tex) | 801 | 接入 | B：积分/生成目标、IID/加权/相关/粒子、MCSE与诊断边界 |
| [tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex](../../tex/03-models/03-probabilistic-graphical-models/09-parameter-learning.tex) | 910 | 接入 | B：点/分布估计、潜变量/缺失、EM/近似/后验与误差分解 |
| [tex/03-models/03-probabilistic-graphical-models/10-structure-learning.tex](../../tex/03-models/03-probabilistic-graphical-models/10-structure-learning.tex) | 689 | 接入 | B：检验/评分/搜索、结构/因果识别与干预信息 |
| [tex/03-models/03-probabilistic-graphical-models/11-static-directed.tex](../../tex/03-models/03-probabilistic-graphical-models/11-static-directed.tex) | 631 | 接入 | B：直接与潜变量、共享/层次、后验/似然/生成与非唯一性 |
| [tex/03-models/03-probabilistic-graphical-models/12-energy-models.tex](../../tex/03-models/03-probabilistic-graphical-models/12-energy-models.tex) | 592 | 接入 | B：联合/条件归一化、潜变量/关系模板、结构输出 |
| [tex/03-models/03-probabilistic-graphical-models/13-dynamic.tex](../../tex/03-models/03-probabilistic-graphical-models/13-dynamic.tex) | 677 | 接入 | B：状态时间/查询时间、滤波/平滑/路径、解析与近似计算 |
| [tex/03-models/03-probabilistic-graphical-models/14-generative.tex](../../tex/03-models/03-probabilistic-graphical-models/14-generative.tex) | 847 | 接入 | B：真实/模型律、密度/后验/生成四查询；VAE/Flow/扩散 |
| [tex/03-models/03-probabilistic-graphical-models/part.tex](../../tex/03-models/03-probabilistic-graphical-models/part.tex) | 17 | 接入 | I：完整入口及包含关系 |
| [tex/03-models/main.tex](../../tex/03-models/main.tex) | 6 | 独立单卷入口 | I：完整入口及包含关系 |
| [tex/03-models/volume.tex](../../tex/03-models/volume.tex) | 11 | 接入 | I：完整入口及包含关系 |
| [plans/classic-models-outline.md](../classic-models-outline.md) | 378 | 对应正文均存在 | O：全章/节职责与四任务评价；集成6.1–6.6、共享机制及口径 |
| [plans/neural-network-models-outline.md](../neural-network-models-outline.md) | 1386 | 对应正文均存在 | O：九章标题与表达/可学习/动态/运算/训练/泛化职责及条件；SAM差异 |
| [plans/probabilistic-graphical-models-outline.md](../probabilistic-graphical-models-outline.md) | 983 | 对应正文均存在 | O：十四章标题与表示/查询/近似/学习/识别/动态/生成职责及边界 |

文件及摘要另见[来源清单](sources.json)。临时关键词命中不是未完成任务判定；例如“尚未收敛”属于正文概念边界而不是TODO。

## 审查结论的可执行范围

第17章无需复刻第三卷算法专章，也无需覆盖每项纯计算。保留学习问题的对象与所求结论，再按证明需要引入概率推断、求导、随机积分等工具。这里的“覆盖”指主要学习研究问题具有明确归属；工具记录用于保留来源与数学依赖，不计作另一类学习问题，也不表示已经证明各模型性质。
