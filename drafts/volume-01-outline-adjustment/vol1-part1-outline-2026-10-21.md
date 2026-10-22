# 第一卷第一部分：章节调整细纲

> **2026-10-22结构更新：** 原第4章拟提升为独立的第二部分“线性空间”，拆为第4章“表示”、第5章“运算”、第6章“方程和优化”、第7章“分析”。最新结构见[线性空间部分：标题版](vol1-linear-space-part-headings-2026-10-22.md)。本文件下面的原第4章及七章统计保留作为详细材料底稿，不再代表最新部分划分。原第1—3章构成第一部分；原第5—7章拟顺延为第8—10章，构成第三部分“微积分与优化”。精确线性方程和最小二乘在新6.2、6.3分别成节且相邻，不合并为同一个问题。首次提升时的材料迁移记录保存在build/outline-preview/linear-part-heading-map.json；后续按问题重排的当前依据见[各节的问题与组织说明](vol1-linear-space-organization-2026-10-22.md)。

本稿根据实际正文整理，保留第一部分此前调整的详细材料。**以下原第四章按“表示—运算—方程和优化—分析”四节保存；最新标题结构采用上方链接的四章版本。** “极限”在前、“线性空间”在后的阅读顺序，其余已核对内容及原1.5.7—1.5.9的删除保持此前安排。

- 正文基线：337b382b。现有正文入口和文件名用于定位材料；新章号表示拟实施顺序。
- 活跃入口：[第一部分 part.tex](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/part.tex)，按章及章内输入核对；原有提要见[当前第一部分大纲](../../plans/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization.md)。
- 交付范围：本文件为调整方案，细化到subsubsection和paragraph。正文、plans/当前正文提要、图片和PDF未改；原检查时未提交、未集成（本次归档状态见README）。
- 工作区：.worktrees/vol1-outline-adjustment；分支：codex/vol1-outline-adjustment。

## 本轮调整与阅读顺序

第一部分按“数学对象—集合的计数—极限—线性空间—一元函数微积分—多元函数微积分—最优化”推进。极限章提供实数收敛的依据，线性章随后用有限维表示和代数计算建立求解问题。线性章仍在微积分之前，最小二乘与二次目标先由平方展开、正交关系和配方论证，正式微积分响应另设回读标记。

| 节 | 核心问题 | 材料归属 |
| --- | --- | --- |
| 4.1 表示 | 对象是什么，怎样用有限个独立系数记录？ | 标量、向量、矩阵、张量；线性相关与无关、基、维数；子空间；坐标与换基；线性映射及核像秩；对偶、商空间；相似、相抵与合同的坐标含义。 |
| 4.2 运算 | 已给定对象后，怎样计算并核对规则？ | 加减、数乘、逐项与矩阵乘法；转置、迹；内积、加权内积、范数、伴随；外积、行列式；幂与矩阵函数；张量积、重排、reshape、Kronecker积和缩约。 |
| 4.3 方程和优化 | 未知量要满足什么条件，怎样求得？ | 子空间最近点；$AX=B$；二次优化；$\min_X\|AX-B\|_F^2$；低秩与映射逼近；双侧、Sylvester及Lyapunov矩阵方程。 |
| 4.4 分析 | 固定问题的迭代趋向哪里，误差又会怎样改变答案？ | 收敛分析：对象序列、幂与级数、定常迭代、最小二乘迭代、Krylov及谱方向迭代。扰动分析：条件数、方程解、残差与数值稳定性、正则化、谱方向和矩阵函数。 |

“表示”中的商和对偶先建立代数对象；商上的长度、对偶范数及内积表示归“运算”。三种换基关系的定义与条件放在表示中，行列式和迹的不变量在相应运算建立后补齐，合同标准形的构造在二次优化建立实对称谱后完成。

“运算”按实际计算类型安排，内积之后紧接加权内积，再抽取范数公理。每类先讲输入输出、定义与性质，再讲基础实现、可利用的结构及近似误差；轴收缩、注意力和局部汇集在缩约运算内说明。已有低秩因子的应用归计算，未知因子的拟合及最佳近似归求解问题。

“方程和优化”按六类问题分组，各问题内再分可解性、唯一性、分解法、迭代法和计算边界。子空间最近点建立正交化与QR；线性方程区分形状、满秩、秩亏及相容性；二次优化明确无约束、单位球面、闭球和等式约束的区别。实对称谱从单位方向的能量极值引出，先于最小二乘中的SVD，避免在表示部分预列分解。

“分析”用收敛和扰动两类问题统领旧材料。算法更新在求解节建立，收敛节判断极限、速度与初值条件；扰动节区分问题敏感性和计算过程的稳定性，不用小残差代替参数误差。全章限于实数，一般实矩阵不被假定存在完整实特征向量基。

## 沿用的章节与迁移边界

1. 第1章继续删除原1.5.7“逆矩阵”、1.5.8“矩阵的迹”、1.5.9“矩阵的行列式”及其11个段落；这些知识在新线性章按使用依赖建立。第2章沿用实际结构，并保留已恢复的“组合数的拆分（Pascal恒等式）”段落。
2. 新第3章“极限”沿用原极限章的实际细纲，只调整章名与编号；章内“函数的极限”一节仍保留该名称。一般度量内容的后移标记继续保留，实轴邻域与闭区间结论留在本章。
3. 第5、6章保留已有大部分subsubsection与paragraph。一元直接使用绝对值，多元直接使用向量距离；一般度量、一般测度与一般乘积测度后移，实轴及欧氏勒贝格积分、三大收敛定理、换序条件和反例保留。具体迁移边界沿用下文各处标记。
4. 第7章沿用现有实际细纲，承担一般最优化理论；线性章只先建立可由代数和谱分解说明的二次／线性约束任务。第二部分五章的安排继续采用[已有第二部分细纲](vol1-part2-outline-2026-10-21.md)。

引用框中的“后移”“限于实轴／欧氏版本”“必要改名”仍是待实施标记。后移条目留在当前位置用于定位原文，不能理解为拟继续保留在第一部分；它们移走后的连续编号在正文实施时统一处理。第4章则直接展示重组后的连续编号。

## 调整稿的层级统计

| 章 | section | subsection | subsubsection | paragraph |
| --- | ---: | ---: | ---: | ---: |
| 1 数学对象 | 6 | 18 | 0 | 70 |
| 2 集合的计数 | 3 | 6 | 10 | 41 |
| 3 极限 | 4 | 13 | 5 | 45 |
| 4 线性空间 | 5 | 28 | 108 | 315 |
| 5 一元函数微积分 | 4 | 17 | 57 | 176 |
| 6 多元函数微积分 | 6 | 26 | 70 | 120 |
| 7 最优化 | 7 | 18 | 11 | 11 |

合计：7章，35个section、126个subsection、261个subsubsection、778个paragraph。第四章的五个section包含四个主体部分及独立小结；统计包含拟新增及待迁移条目，不能当作正文已经实施的数量。

---

<!-- OUTLINE BEGIN -->

## 第1章 数学对象

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1 -->

正文入口：[`01-sets-functions-and-proofs.tex`](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex)。

章首以三次观测和“由输入预测输出”的任务提出四个问题：讨论范围、对应规则、候选规则的编号与比较、多次观测的整体计算，并说明集合、关系、函数、确界、索引族与向量矩阵依次回答它们。关键概念用独立段标题标明，定义、表示、运算及性质按依赖展开。

矩阵部分保留表示、常见类型、基本运算与运算规则，作为后续线性空间和微积分的记号基础。

### 1.1 集合

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:16 -->

用整数集合建立对象范围，先说明集合及其描述，再用同一组有限集合定义交、并、差、补；对象之间的关系移到独立一节。

#### 1.1.1 集合的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:21 -->

依次解释集合、子集、集合的相等与描述，再把集合本身作为元素引入幂集和集合族；逐段给出定义与小例子。

###### 段：集合

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:24 -->

用整数集合建立对象范围，先说明集合及其描述，再用同一组有限集合定义交、并、差、补；对象之间的关系移到独立一节。

###### 段：子集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:32 -->

由每个元素均属于另一集合定义包含关系，补充真子集，并区分成员关系与包含关系。

###### 段：集合的相等

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:39 -->

由“集合只由元素决定”推出相等等价于双向包含，说明两个方向分别排除多出和遗漏的元素，并约定后文核对集合恒等式均采用双向包含。

###### 段：集合的描述

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:46 -->

列举法与条件法表示同一有限集合，说明冒号的条件含义。就地约定常用数集及开、闭、半开区间记号。

###### 段：幂集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:56 -->

定义所有子集组成的集合，并列出二元素集合的四个子集。区分原集合的元素与幂集的集合元素。

###### 段：集合族

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:65 -->

定义以集合为元素的集合，用只含两个单元素子集的族说明子集族可以小于完整幂集。

#### 1.1.2 集合的运算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:71 -->

在小节开头固定全集与C、D两个有限子集，作为所有运算共用的例子，再分别按成员同时满足、至少满足、排除及全集内取反定义运算；说明差集的次序和补集的全集依赖。

###### 段：交集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:77 -->

承接小节开头已经固定的全集与C、D，按同时属于两集合的条件定义交集，例中只留下2和3。

###### 段：并集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:84 -->

用至少属于一集合的条件定义并集，解释或允许同时成立。C与D的并集覆盖全集，共同元素仍只记录一次。

###### 段：差集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:93 -->

定义属于前集合而不属于后集合的元素范围。C减D与D减C分别给出1和4，直接说明次序影响结果。

###### 段：补集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:100 -->

把补集定义为固定全集减去指定子集。将全集增加一个元素后重算同一集合的补集，说明结果依赖讨论范围。

#### 1.1.3 集合运算的基本规律

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:109 -->

给出交、并的交换律、结合律与分配律，以及两个集合的De Morgan律，并用双向包含证明第一式、以C、D核对；说明“不满足任一条件”与“每个条件都不满足”相同，为补集计数和可测集合构造作准备。

### 1.2 二元关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:144 -->

把满足条件的对收集起来，定义二元关系为笛卡尔积的任意子集及X上的关系；以不大于关系说明方向，指出相等关系对称、关系允许一对多或无对应；全部关系组成笛卡尔积的幂集，空集与整个积分别表示无对和全对满足。

###### 段：有序对

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:153 -->

说明记录两个对象时需要区分位置，定义有序对相等为对应位置分别相等，用交换1和2对照集合；把章首三次观测写成三个有序对。

###### 段：笛卡尔积

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:161 -->

定义第一项取自X、第二项取自Y的全部有序对，给出二乘二例，说明一般不能交换两个因子；推广到d元组并约定R^d为平面坐标等实数组。

###### 段：二元关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:173 -->

把满足条件的对收集起来，定义二元关系为笛卡尔积的任意子集及X上的关系；以不大于关系说明方向，指出相等关系对称、关系允许一对多或无对应；全部关系组成笛卡尔积的幂集，空集与整个积分别表示无对和全对满足。

###### 段：等价关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:186 -->

以按余数分组为例，由“自己同组、同组可交换、同组可传递”三项要求引出反身、对称、传递的定义，并逐条验证余数关系。

###### 段：等价类

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:207 -->

定义与指定元素等价的对象组成的集合，用余数例说明同一类可由不同代表元写出。引入划分的定义，证明全部等价类构成划分：反身性给出覆盖，对称与传递给出两类相交即相等；再说明划分反过来确定等价关系，二者是同一件事的两种写法。

###### 段：商集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:229 -->

把每组当作新对象，定义全部等价类组成的商集，强调其元素是原集合的子集。平面非原点的比例关系逐条验证三性质，等价类为去掉原点的直线；只允许正比例时类变为射线，并用图比较两种分类。

###### 段：偏序关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:251 -->

由等价关系转向比较关系，先以实数可比、幂集中两个单元素集合互不包含说明比较缺口，再定义反身、传递、反对称以及全序，比较实数大小与集合包含，并区别反对称性和对称性。

### 1.3 函数与函数族

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:269 -->

由“关系允许一对多或无对应”转向预测所需的唯一输出，平方运算作为例子；依次说明函数的定义、组合与反求，把整个函数作为对象得到函数族，再为比较候选函数引入实值输出的界、确界和最值。

#### 1.3.1 函数的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:280 -->

以平方函数说明定义域、陪域和求值规则，再给出像、值域与原像。原像为集合，不要求逆函数存在。

###### 段：函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:283 -->

把函数定义为每个输入恰有一个输出的关系，引出图像；以不大于关系说明并非每个关系都是函数。强调完整函数包含所声明的定义域与陪域，平方函数在两个定义域上是不同的函数；引入全部函数组成的集合Y^X。

###### 段：像与值域

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:297 -->

定义子集的像和整个定义域的像，用平方函数比较实际输出集合与预先指定的陪域。

###### 段：原像

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:306 -->

将输出集合的成员条件转为输入条件，逐项计算平方函数的三个原像，说明结果可以多元素或为空，不要求函数可逆。再证明原像保持并、交与补，并用平方函数举例说明像不保持交集；指出这一性质将用于可测函数。

#### 1.3.2 函数的运算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:337 -->

节首说明函数可组合成新函数。先对同域实值函数逐点作四则运算与数乘，再说明函数复合的输入输出相容条件（以平方根复合说明定义域缩小）、次序差异，并逐层代入证明结合律。

###### 段：实值函数的四则运算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:343 -->

对同一定义域的实值函数按点定义和、差、积与实数倍，商函数限制到分母非零的子集；用两个一次表达式说明运算可能改变定义域。

###### 段：函数的复合

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:361 -->

定义先后求值的组合并检查定义域相容性。平方和加一的两个次序给出不同结果，三函数复合则逐点验证结合律。

#### 1.3.3 函数的类型

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:383 -->

由“希望从输出唯一恢复输入”引出两项要求，把恒等映射、单射、满射以及双射和逆映射放在同一小节。用平方函数的不同范围逐项对照性质，证明“可以双向撤销”等价于双射，并验证复合反求的次序。

###### 段：恒等映射

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:390 -->

定义将元素送回自身的映射，并说明它与函数复合时保持原函数。

###### 段：单射

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:396 -->

用不合并不同输入定义单射，以实轴上的平方函数及其非负限制对照。

###### 段：满射

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:402 -->

用值域覆盖陪域定义满射，以平方函数改变陪域说明该性质依赖声明的范围。

###### 段：双射与逆映射

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:408 -->

双射同时满足单射和满射，满射与单射分别保证每个输出至少、至多有一个原输入，逆映射唯一恢复输入并满足两个恒等式；反向证明存在双侧撤销映射必为双射。有限映射图区分原像与逆求值，随后验证双射复合求逆须倒转次序。

#### 1.3.4 函数族与参数化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:456 -->

用一元仿射函数族说明整函数、参数和一次函数值的三个角色，不提前调用向量内积。可识别性用参数到完整函数的单射定义，乘积参数化展示不同编号对应同一函数。

###### 段：函数族

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:459 -->

回到章首的预测问题，说明候选规则本身组成以整个函数为元素的集合；定义同一定义域与陪域的一组函数，以选定斜率截距、再代入自变量的两步计算说明族中元素是函数。

###### 段：函数参数化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:470 -->

定义参数到函数的对应，区分参数选择一条规则与自变量指定求值位置；说明参数化把在函数中挑选改写为在熟悉的参数集合中挑选。

###### 段：函数参数化的可识别性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:479 -->

定义完整函数唯一确定参数的要求。仿射函数由0、1两点恢复参数，而乘积参数化中的多组参数表示同一函数；图示后用等价关系收束这些不同表示，说明商集与函数族一一对应，可识别恰为每个等价类只含一个参数。

#### 1.3.5 实值函数的界与极值

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:525 -->

由“把候选优劣写成实数并寻找最小者”引出本小节。先在非空实数集合上定义界与确界，再应用到函数值域。区分最值、取最值的位置及未取得的确界，有限多项式算例与端点图分别说明多解与达到性。

###### 段：上界与下界

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:532 -->

明确比较对象为非空实数集合，给出对全部元素成立的不等式及上下有界的含义；开区间展示界未必属于集合或唯一。

###### 段：上确界与下确界

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:539 -->

将上确界定义为最小上界，下确界定义为最大下界；说明“最小上界存在”不能由定义直接得到，把确界原理作为实数的基本性质（完备性），并用有理数集合{q^2<2}说明有理数没有这一性质。用任意小正误差刻画边界的可逼近性。

###### 段：函数的有界性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:554 -->

通过函数像的有界性定义函数的有界性，说明确界的函数记法和无有限界时的扩展符号。

###### 段：最小值与最小点

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:565 -->

以对整个定义域的比较定义全局最小点，解释全称符号及min、argmin的不同输出类型；逐步证明最小值存在时等于下确界。开区间上的恒等函数说明下确界存在但不取得。

###### 段：最大值与最大点

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:584 -->

对称定义最大值、最大点和argmax，比较开闭区间下的达到性；多项式例完整计算最小与最大值及对应的全部输入。

### 1.4 索引族

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:619 -->

从重复的数值不能由取值集合恢复出发，介绍编号、有限汇总和逐项生成。收敛结论不混入有限记号的定义。

#### 1.4.1 索引族与序列

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:625 -->

由重复值的位置不能从取值集合中恢复，引出索引到对象的映射及整数索引序列，区分坐标编号、迭代步与幂，再以两个索引集合的笛卡尔积定义二维索引族，给出固定行或列的六项示例。

###### 段：索引族

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:628 -->

先说明直接组成集合会丢掉重复值的位置，由保留编号的需要引出索引到对象的函数。

定义索引集合到对象集合的映射，指出编号不同仍可取相同对象；城市名例说明一般索引集未必有序。

###### 段：序列

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:640 -->

以正整数顺序定义有限和无限序列，并约定从0开始时明写索引范围。实数值序列称为数列。

###### 段：二维索引族

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:650 -->

为同时记录观测与坐标，将索引集合取为两个集合的笛卡尔积，定义a(i,j)及双下标记号；用两行三列、取值1至6的表格说明必须同时确定两个索引，并解释固定一个索引后的对象族。

#### 1.4.2 集合族的并与交

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:666 -->

由已定义索引族取集合值，把两个集合的并与交推广到任意多个；以[1/n,1]的并为(0,1]逐点验证，给出一般De Morgan律及成员资格证明，衔接集合测量中的可数并交。

#### 1.4.3 有限和与有限积

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:696 -->

定义有限求和与连乘及空项约定，解释索引换名，再分别说明有限和、有限积的运算法则及多重求和、求积的换序范围。

###### 段：有限和与有限积

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:699 -->

用三个实数计算有限和与有限积，解释空和0与空积1为何保持已有运算结果。

###### 段：哑索引与自由索引

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:714 -->

求和变量只是遍历占位，可统一换名；未被求和的下标保留输出坐标，换名不得占用这一自由索引。

###### 段：有限和的运算法则

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:729 -->

由实数分配律给出有限求和的线性公式，明确系数和两列数的范围。

###### 段：有限积的运算法则

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:738 -->

由实数乘法交换律与结合律推出逐项积、常数因子及非零分母下的商公式；数例说明常数提出的幂次，并反例排除求和式的线性拆法。

###### 段：多重求和

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:756 -->

矩形索引区域按行或按列汇总得到同一结果。三角索引区域换序必须同时改写范围，逐项列出n为3时的六个索引对以检验。

###### 段：多重求积

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:781 -->

以矩形数组定义二重积，按行按列计算均为720；三角索引换序须同步修改范围，有限乘积允许零因子。

#### 1.4.4 递推关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:800 -->

用累计和说明初值与更新共同确定序列，引入数学归纳法确认通项对每一步成立，再分别介绍每步加定值的等差递推和每步乘定值的等比递推，最后由错位相减和裂项得到有限几何和与裂项求和；不在本节展开误差递推不等式。

###### 段：递推关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:803 -->

定义由初值和已知项生成后续项的关系，用1、4、9的累计和逐步计算并与求和记法对照。

###### 段：数学归纳法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:813 -->

说明猜出的通项需对每个t成立，由“初值成立且每步可推进”引出归纳基础、归纳步与归纳假设，并用归纳法证明累计和的递推式与求和式一致。

###### 段：等差递推

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:826 -->

每步增加固定实数，从初值累加得到第t步的显式表达式并用归纳法写出；以初值2、公差3计算，并按公差符号说明增减与常值。

###### 段：等比递推

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:839 -->

由每步乘二分之一推广为固定实系数递推，给出有限步表达式及一行归纳步，并区分系数大小、符号和零初值。

###### 段：有限几何和

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:855 -->

用错位相减求出有限几何和公式并以数例核对；推广为一般的裂项求和，以1/(n(n+1))为例。说明项数无限增大时的行为留待第3章，第3章的几何级数直接引用这里的公式。

### 1.5 向量与矩阵

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:877 -->

先规定向量坐标及矩阵行列的表示，再分别定义运算、推导规则；本章在矩阵的运算规则处结束这一节，逆矩阵、迹、矩阵内积与行列式在后面的线性空间章中使用和展开。

#### 1.5.1 向量的表示

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:885 -->

定义有序实坐标、维数、相等与零向量，再说明行列排列及转置记号。三个观测分成输入、输出两个列记录。

###### 段：坐标向量

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:888 -->

给出正整数维的列向量表示，按坐标定义相等，交换两个坐标显示次序不能忽略。

###### 段：行向量与列向量

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:899 -->

按横排或竖排区分两种表示，以转置连接它们；输入和输出记录的同一位置对应同次观测。

#### 1.5.2 向量的运算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:910 -->

加减、数乘、线性组合、内积和欧氏范数各自独立定义并给数值例，输出类型与维数要求就地说明。

###### 段：向量的加法与减法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:913 -->

同维向量按对应坐标加减，以两个二维向量复算；实际记录须保持相同坐标含义。

###### 段：数乘

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:923 -->

定义一个实标量同时乘各坐标，给出倍数、零倍与相反向量。

###### 段：线性组合

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:931 -->

以任意实系数加权若干同维向量，系数无概率限制；预测与观测相减得到残差向量。

###### 段：内积

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:941 -->

定义对应坐标乘积之和，说明结果为标量并完成一个二维计算；由有限和法则列出对称、线性与非负性质。

###### 段：欧氏范数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:954 -->

以自内积平方根定义欧氏长度，用三个残差的平方和说明误差汇总，并由向量差定义欧氏距离。再用“长度平方非负的二次式取最小值”证明Cauchy--Schwarz不等式及取等条件，由它推出长度和距离的三角不等式，指出后文控制误差主要依靠这一不等式。

#### 1.5.3 矩阵的表示

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:989 -->

开头直接用观测输入排成数表，说明预测与平方误差的合写，仿射例解释常数列；随后定义形状、行列、元素及相等，不加入正则化目标。

###### 段：矩阵的行与列

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1021 -->

定义实矩阵的形状、行列元素和冒号取行取列，说明矩阵相等要求形状及元素都相同。

#### 1.5.4 常见的矩阵

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1029 -->

从方阵及主对角线进入，分别用位置条件与小矩阵说明零矩阵、对角矩阵、单位矩阵、上下三角矩阵和对称矩阵；运算符号留在后面定义。

###### 段：方阵

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1032 -->

定义行列数相同及阶数，以二阶矩阵定位主对角元素，为按元素位置分类建立记号。

###### 段：零矩阵

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1040 -->

定义全部元素为零，给二行三列例子，强调零矩阵可以不是方阵且应说明形状。

###### 段：对角矩阵

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1047 -->

定义主对角线外全零的方阵并给diag记法，说明省略位置为零而对角元素允许为零。

###### 段：单位矩阵

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1055 -->

定义对角元素全为1的对角矩阵，以二阶例写出元素，乘法单位性质在矩阵乘法之后说明。

###### 段：三角矩阵

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1063 -->

以i大于j或小于j的元素为零分别定义上下三角矩阵，给三阶例子并说明对角矩阵同时属于两类。

###### 段：对称矩阵

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1075 -->

按交换行列索引后元素相等定义对称方阵，给二阶例子；转置等式作为后续记号的简写说明。

#### 1.5.5 矩阵的运算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1084 -->

将原基本运算提升为独立小节，按输入与输出形状依次定义同形加减、标量数乘、转置、矩阵向量积及矩阵乘法；每项给出独立成行的小矩阵运算，不在这里混入运算规则。

###### 段：矩阵加法与减法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1089 -->

同形矩阵对应元素相加相减，加法和减法算例分别独立成行，结果保持原形状。

###### 段：矩阵数乘

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1108 -->

标量逐元素相乘，以二阶矩阵完成数值计算。

###### 段：矩阵转置

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1116 -->

按元素索引交换行列，三行两列的例子变为两行三列。

###### 段：矩阵与向量的乘法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1129 -->

以每行与向量的内积定义输出坐标，说明维数相容条件；再从列看成按参数作线性组合。

###### 段：矩阵乘法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1147 -->

直接给出左矩阵行与右矩阵列的求和公式、内维相等条件及结果形状，逐项核对二阶矩阵乘积。

#### 1.5.6 矩阵的运算规则

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1171 -->

将原运算性质提升为独立小节；在形状相容条件下说明结合律与分配律，以同一对二阶矩阵反序计算说明无交换律，再从规则推导矩阵映射保线性组合，区分有非零截距的仿射函数。

###### 段：结合律与分配律

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1176 -->

在形状相容条件下陈述矩阵结合与双侧分配律，指出其依据为乘法定义及有限和规则；连续作用相当于一次乘积。

###### 段：无交换律

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1190 -->

反序计算同一对二阶矩阵，给出与原乘积不同的结果，说明矩阵乘法一般不交换；另明确左右单位矩阵的形状与保持作用。

###### 段：线性性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1201 -->

先用矩阵运算法则推导保线性组合，再命名线性映射。说明矩阵作用的线性和含非零截距的仿射函数不同。

### 1.6 本章小结

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex:1387 -->

收束集合与关系、函数与函数族、确界与最值、索引族与集合族运算、归纳法和有限累计；区分向量、矩阵的表示、基本运算与运算规则，为后面的线性空间和微积分准备共同记号。

## 第2章 集合的计数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:1 -->

正文入口：[`02-combinatorics.tex`](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex)。

本章只处理有限结果与有限输入上的输出模式。章首说明逐个列举的困难与函数类计数的动机；先以双射、加法规则、乘法规则和等倍归并作为全部计数的依据，推出排列与组合，再计数子集与划分，随后用容斥、补集计数及累计反演处理重叠与累计；最后比较二值、多分类与实值函数类的模式与打散要求，并完整证明Sauer--Shelah引理。实轴集合测量由后面的“一元函数微积分”章建立。

### 2.1 有限集合的计数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:13 -->

对象是有限集合及其构造出的结果集合；先确定“怎样才算两个不同结果”，以同一对象的有序与无序记录说明数量依赖记录方式。随后以双射、加法、乘法和等倍归并作为依据推出排列与组合，再计数子集与划分，最后说明交集校正与累计反演。

#### 2.1.1 基础计数方法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:22 -->

节首说明全部计数依赖三件事：换成更易数的集合、不重不漏分类、拆成依次选择。先建立这些规则，再推出排列数、组合数、子集与划分的数量；不讲二项式定理。

##### 2.1.1.1 加法规则和乘法规则

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:30 -->

把双射、不重不漏的分类、完整有序记录和均匀重数分别作为计数依据，说明各自条件及来源，再用于后续计数公式。

###### 段：双射与计数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:33 -->

把“数出n个元素”解释为给出到{1,…,n}的双射，由双射与编号的复合说明双射保持元素个数；指出计数子集时将先建立到零一记录的双射。

###### 段：加法规则

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:41 -->

陈述有限不交并的基数等于各项之和，并用编号拼接说明不重与不漏分别对应两两不交与并等于全体；用两本数学书与三本计算机书中选一本说明2+3，明确重叠时不能直接相加。

###### 段：乘法规则

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:53 -->

先给有限笛卡尔积的基数公式，按第一位置分类、每类与后一因子双射，由加法规则与对位置数归纳证明；列2×3的六条记录并得出零一记录有2^n条。再说明后一步选项内容可依赖前一步、只要选项个数固定也能连乘，并给出按第一步分类的论证。

###### 段：等倍归并

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:75 -->

记录多于结果且每个结果恰被记录k次时，结果数为记录数除以k，依据是加法规则；强调重复次数必须相同，并预告由排列推出组合、由有名称推出无名称划分都使用这一规则。

##### 2.1.1.2 排列数和组合数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:82 -->

先对保留位置的不重复记录使用乘法，再把表示同一子集的记录分类，用等倍归并得到组合数，并用双射、双重计数与配对推出组合数恒等式。

###### 段：排列数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:88 -->

定义有序k元组及0≤k≤n，逐步选择推导下降连乘，四人两个职位说明12；空排列对应空积1。阶乘只在此作为连乘简写引入，包含0!约定，不另设阶乘段落。

###### 段：组合数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:106 -->

定义k元子集与组合数记号，说明每个排列确定一个子集、每个子集恰对应k!个排列，用等倍归并推出P(n,k)=组合数乘k!及阶乘公式；列六个二人组，保留边界与范围外取零约定。

###### 段：组合数的对称性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:126 -->

以取补集建立k元子集和n−k元子集的一一对应，给出组合数对称公式与四选一的解释。

###### 段：组合数的总和

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:134 -->

按大小把全部子集分成互斥类别，另由子集与零一记录的双射得到总数2^n，两种数法相等给出各阶组合数之和为2^n，复算n=4，并点明双重计数的方法。

###### 段：组合数的拆分 (Pascal恒等式)

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:144 -->

Pascal恒等式：按是否包含固定元素分成两类，推出组合数递推；列初值和前几行，图示3+3的分类来源。

###### 段：组合数的交错和

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:165 -->

固定一个元素，定义“删去或加入该元素”的映射，说明它作用两次回到原子集、因而是双射，且每次改变大小1，从而配对偶数与奇数大小的子集，证明n≥1时交错和为0、n=0时为1，供容斥与反演的抵消使用。

##### 2.1.1.3 子集与划分的计数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:176 -->

不限制选取个数或要把全部对象分组时，仍先用双射换成零一记录，再用乘法规则与等倍归并计数。

###### 段：幂集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:182 -->

写出子集与长度n零一记录之间的双射，逐项说明单射与满射，由乘法规则得到2^n，包含n=0的空集情况。允许的部分子集构成集合族，与第1章同一概念，以二元子集族含6个成员为例。

###### 段：二分划分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:198 -->

有名称两侧由第一侧唯一确定，得到2^n；无名称时说明n≥1时S与其补集总不相同，每个结果恰有两个表示，用等倍归并得到2^(n−1)，再作非空修正；单列n=0时两侧相同、等倍归并条件失效，不能统一除以2。

#### 2.1.2 存在重叠关系的计数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:211 -->

互斥条件失效后，需用交集校正重复；本小节只讲容斥及补集应用，不与Möbius混成一个方法。

###### 段：容斥原理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:217 -->

先逐元素说明A={1,2,3,4}、B={3,4,5}为何4+3−2=5，并由三块互斥区域的加法规则推出两集合公式；图示公共区域，加入第三集合逐类核对元素被计次数，解释加回三重交集。陈述一般有限公式，证明中把右侧按元素合并，对恰属于r个集合的元素用已证的交错和恒等式算出总系数为1。

###### 段：补集计数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:276 -->

说明多条限制同时成立时先数违规结果更方便。就地说明四门课的三条选择规则，定义三个违规集合，由De Morgan律把合法结果写成违规并集的补集；用乘法规则逐项读出三个集合及交集大小，由16−11得到五个合法课程子集，并直接枚举核对。

#### 2.1.3 Möbius反演

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:306 -->

以课程组合总得分与单个组合自身贡献的关系引出问题，从元素个数推广到任意实值集合函数的累计；先给集合函数与子集格，再陈述并证明反演公式、给出四元素算例，最后说明一般有限偏序上的系数。

###### 段：集合函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:315 -->

定义以子集为输入的函数；用基数函数及二元值7而两个单项各2的例子说明它未必可加，并指出多出的3正是二元组合自身的贡献。

###### 段：子集格

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:323 -->

说明累计沿包含关系进行，回接第1章包含关系是偏序的结论；解释包含次序、交与并的上下界作用，为子集累计和的索引关系提供对象说明。

###### 段：Möbius反演

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:332 -->

区分累计值g和自身贡献h；保留正反公式与有限双重求和证明，说明换序依据是遍历同一批集合对，把中间集合写成R与差集子集的并、按差集大小分类，算出内层交错和在差集为空时为1、非空时为0，因此只保留目标子集。

###### 段：反演的算例

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:388 -->

首次使用前解释条件指示记号，用四元素解析集合函数、16项表、两项反演和配图展示局部贡献，最后区分容斥与反演所保留的对象。

###### 段：Möbius函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:439 -->

说明系数只依赖相对位置，在一般有限偏序上用递归定义Möbius函数并解释递归式即区间内系数和为零；验证子集格上的正负一满足递归，与反演定理一致。

### 2.2 有限输入上的可区分模式

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:454 -->

回接第1章函数族：数据只能区分规则在有限观测输入上的输出。对象从有限候选扩展到可能无限的函数类；固定有限输入后合并相同输出，分别研究模式数量与打散条件能够成立的输入规模。二值、多分类、实值按输出类型分层。

#### 2.2.1 二值函数类

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:465 -->

固定非空输入空间与非空二值函数类，说明{0,1}^X沿用第1章的函数集合记号，并以垃圾邮件判断为例；从限制类到最大模式数，再研究全体二值模式是否都能实现。

##### 2.2.1.1 生长函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:472 -->

先定义固定输入上的输出记录，再对输入组取最大；有限子集计数给出可计算实例。

###### 段：限制类

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:475 -->

先限定有限观察范围，说明不同函数可能留下相同记录，再正式定义互异输入按固定次序组成的输出向量集合，并由乘法规则得到至多2^m个模式。用阈值函数在1、2、3上按阈值所在段逐一列出四模式，说明相同模式不等于同一函数。

###### 段：生长函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:495 -->

定义m个输入上的最大模式数及空输入；解释重复输入、最大值存在的理由（可能取值是有限多个整数），按阈值落在m+1段之一计算阈值类的m+1。

###### 段：指示函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:519 -->

说明二值函数与子集一一对应，定义I_S在S上取1、S外取0，从而模式可看作标为1的输入子集；固定无限输入空间，以至多k个正点的子集指示函数类得到二项式和，用k=1、m=3列四模式，不引入概率。

##### 2.2.1.2 VC维

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:536 -->

依据全部2^m模式可实现的判据定义打散与维数；用区间给具体判断，再用删除坐标证明一般计数界。

###### 段：打散

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:539 -->

定义对每个二值标记均存在实现函数；阈值类能打散一点但不能实现有序两点上的10，给出判定过程。

###### 段：VC维

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:551 -->

定义被打散有限集大小的上确界和0、无穷约定；算阈值维数1，并用冗余参数说明维数不等于参数个数。

###### 段：区间指示函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:568 -->

固定实轴区间类，按连续正块计出1+m(m+1)/2；由两点全实现、三点缺101得VC维2，图示与至多两正点类的模式差别。

###### 段：Sauer--Shelah引理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:603 -->

由阈值类与区间类的多项式增长引出问题，先定义模式族打散坐标集并联系函数类的打散。证明推广命题：不能打散超过d个坐标的模式族至多有二项式和个模式；处理m=0与d=0基例，删除末坐标后按前缀分类得到|A|=|U|+|W|，分别论证U、W的打散上界，再用归纳假设与Pascal恒等式逐项合并。简化界说明e^u≥1+u的来源与二项式展开的组合解释，明确1≤d≤m条件，回算区间类达到界。

#### 2.2.2 多分类函数类

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:675 -->

固定非空X、Y及函数类，说明二值打散中“另一个标签”唯一，而多标签时替代标签不再唯一，“任意安排输出”有不同严格程度；按固定标签对、逐坐标邻居、相对基准匹配三种要求组织，限制由强到弱，最后比较三者大小。

##### 2.2.2.1 Natarajan维

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:685 -->

先定义固定每点两标签的打散，再定义规模上确界；有限标签时另给计数界。

###### 段：Natarajan打散

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:688 -->

写清先固定两标签、后要求所有子集选择的量词，列两个输入的四角模式。

###### 段：Natarajan维

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:701 -->

从逐个判断输入集能否实现固定标签对的所有选择，转向输入规模的汇总。

保留上确界定义；以三封邮件四个函数判断维数恰2，并说明二标签退化为VC维。

###### 段：生长函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:736 -->

先由有限标签数给出粗界K的m次幂，再说明有限Natarajan维为何能改进它。

有限K时沿用最大模式数，保留含q=K(K−1)/2的二项式和界及前缀分组证明，补出|V|−|U|与各U_{a,b}大小之和的双重计数关系；列K=3、d=1、m=4的13与81比较，二标签回接Sauer。

##### 2.2.2.2 DS维

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:793 -->

不固定替代标签，改为有限模式族内每点每坐标都有单坐标邻居；先解释伪立方体，再定义打散和规模。

###### 段：伪立方体

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:796 -->

保留有限、非空、每个模式每个坐标的正式要求；六模式表格逐行逐列都有邻居但无四角，展示与Natarajan的差别。

###### 段：DS打散

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:820 -->

定义限制类包含同维伪立方体；把六模式视为两输入上的完整限制类，按定义验证。

###### 段：DS维

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:826 -->

由逐坐标替代的输入规模引出维数，采用有限伪立方体的正式表述。

给出Daniely--Shalev-Shwartz名称、有限伪立方体表述来源和上确界；计算六模式族DS维2、Natarajan维1，图示两种邻居。

##### 2.2.2.3 图维

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:849 -->

以固定参照标签的匹配关系替代固定第二标签，定义图打散及其规模，并在同一条件下比较三种维数。

###### 段：图打散

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:852 -->

写清每个子集匹配、补集不匹配的判据；列四种匹配安排，允许不同模式使用不同替代标签。

###### 段：图维

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:869 -->

先回接独立匹配与不匹配的安排，再汇总能够承受这些安排的输入数。

保留有限集大小的上确界定义；用第三输入恒定的三点四函数例子证明图维恰2，并配图逐项对应。

###### 段：维数比较

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:900 -->

先说明同一模式族可接受三种打散要求的检验，再给出维数比较及有限标签时的推论。

表格（按Natarajan、DS、图维的限制强弱排序）、图和正式定理说明d_N≤d_DS≤d_G及二标签等同VC；保留构造证明。有限K、有限d_N推出图维有限时，直接用固定大小子集的数量下界和有限多项式上界给有限m界，不依赖后移的渐近符号；最后回算六模式及无限标签常值类。

#### 2.2.3 实值函数类

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:975 -->

固定非空实值函数类；说明单点上精确输出可能无限、按数值计数没有意义，因而先与固定阈值比较转为二值信息，再增加指定正间隔。

##### 2.2.3.1 伪维

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:982 -->

按同组阈值能否实现所有高低组合定义伪打散，再取规模上确界。

###### 段：伪打散

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:985 -->

保留严格高低阈值和量词；就地解释⇒，用常值函数一点可行、两点不可能的判定说明要求。

###### 段：伪维

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:1008 -->

由常值函数的输入数限制引出伪维，用独立高低选择的规模说明上确界的用途。

保留0及无穷约定；算常值实函数类伪维1，二值取阈值1/2回接VC维。

##### 2.2.3.2 胖打散维

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:1022 -->

把越过阈值加强为离阈值至少γ；以尺度、维数和系数幅度的关系组织。

###### 段：胖打散

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:1025 -->

保留双边间隔与正负编码公式；用单点输出19.999、20.001说明间隔0.001可行而1不可行。

###### 段：胖打散维

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:1050 -->

先固定间隔尺度并说明输入数会随尺度改变，再汇总满足胖打散要求的集合大小。

定义给定γ的打散规模上确界；在同一个单点函数类中计算尺度分界，说明固定尺度的作用。

###### 段：单调性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:1065 -->

证明γ增大维数不增、胖打散维不超过伪维；从固定有限集的有限见证取最小正距离，说明反向尺度依赖该集合。

###### 段：分块常值函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:1075 -->

保留完整算例和证明：m块、系数幅度B时，0<γ≤B维数恰m，γ>B为0；配图展示允许输出正方形与间隔区域，最后区分模式、数量、打散和后文函数空间距离。

### 2.3 本章小结

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex:1117 -->

收束结果身份、表示重数和有限输入模式：双射、加法、乘法与等倍归并是全部计数的依据，双重计数与配对给出组合恒等式，容斥与补集计数校正重叠，Möbius恢复累计贡献；限制类、生长函数与各类打散维数刻画有限输入上的区分能力，Sauer--Shelah说明VC维有限时模式数多项式增长。由下一章的级数与可数覆盖另行建立集合测量，不再把测度当作本章前置成果。

## 第3章 极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/04-function-limits.tex:1 -->

正文入口：[04-function-limits.tex](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/04-function-limits.tex)。

由前两章的索引、等比递推与有限几何和进入，按现有顺序建立实数列极限（含级数）、实函数极限；原“集合的度量”只保留实轴邻域与闭区间结论，一般空间版本按下文标记后移。

### 3.1 序列的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:1 -->

先以全部尾部项的误差定义收敛，再建立未知极限的存在性判别，随后集中讨论已收敛数列的基本性质、运算与夹逼；通过尾部确界和部分和延伸到上下极限与级数，最后检验重排和保序分组的影响。下一节另行建立实函数极限。

#### 3.1.1 数列的收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:19 -->

以实数列的ε–N条件定义收敛，用1/n与交替数列分别说明收敛及不收敛的量词检验；极限的基本性质、运算和夹逼集中放在收敛判别之后。

###### 段：收敛与发散

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:21 -->

给出实数列、全部尾部项的ε–N定义；通过1/n说明先误差后下标、不要求极限被取到。

增加交错数列的误差带与尾部起点图，由1/n的解析界说明必须控制全部尾部项，有限点展示不代替极限证明。

#### 3.1.2 数列的收敛判别

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:52 -->

候选极限未知时，依次利用单调性与界、有界范围内的子序列、尾部各项互近判断收敛；三个下级小节各给正式定理和证明，明确有界列只保证存在收敛子列。

##### 3.1.2.1 单调数列的收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:57 -->

先定义单调不减与单调不增，再形式化陈述不减且有上界时趋于上确界、不增且有下界时趋于下确界；用确界与单调性控制全部尾部项，说明条件不可省。

##### 3.1.2.2 有界数列的子序列收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:86 -->

定义严格递增下标选出的子序列，区别原列收敛与子列收敛；以Bolzano–Weierstrass定理命名正式表述，明确统一界、严格递增下标和有限极限的量词条件；以反复二分闭区间和左端点上确界完成构造证明；二分长度由2^k≥k+1独立说明趋零，不提前使用已移到基本性质末尾的等比极限。

##### 3.1.2.3 柯西数列的收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:116 -->

先用双尾部下标定义柯西条件，再正式陈述实数列收敛当且仅当为柯西列；必要性用三角不等式，充分性先证有界、取收敛子列，再控制全列。用调和增量反例说明相邻差趋零不足。

#### 3.1.3 极限的基本性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:156 -->

在收敛判别之后，集中研究已收敛实数列的唯一性与有界性，再将和、差、数乘、积、商逐项给出条件、公式及误差控制，最后正式陈述并证明夹逼定理及其振荡项与等比数列应用。各运算法则要求有限极限存在，商还要求分母极限非零。

###### 段：极限的唯一性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:161 -->

假设有两个不同候选极限，以两点距离的三分之一控制同一个尾部项，再用三角不等式导出矛盾。

###### 段：收敛数列的有界性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:167 -->

误差取1控制整个尾部，再把有限前项并入共同界；用(-1)^n说明有界不推出收敛。

###### 段：和的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:172 -->

在两列均有有限极限的条件下给出和的极限等于极限的和，以两个ε/2误差控制证明。

###### 段：差的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:180 -->

单独给出差的极限等于极限的差，用两个原数列的误差之和控制相减误差。

###### 段：数乘的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:187 -->

写明常数倍可与有限极限交换，区分零常数与非零常数，以按绝对值缩放的误差证明。

###### 段：积的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:194 -->

先用收敛数列有界控制变化因子，再拆分乘积误差，明确两列均有限收敛。

###### 段：商的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:205 -->

要求分母极限非零，先证明尾部分母远离零，再估计倒数误差并调用积的法则；用n/(n+1)示例，指出未定式不可代数代入。

###### 段：夹逼定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:215 -->

正式定理明确三列实数、最终夹持及上下界同趋有限值的条件；ε–N证明取三个尾部起点的最大值，再以同一误差区间控制中间项。振荡项除以n和等比数列为应用。

#### 3.1.4 数列的上极限与下极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:246 -->

先说明扩展实数与无穷趋向，再以单调尾部确界定义上下极限；区别有限收敛和无穷趋向，联系夹逼与可达到边界的子列。

#### 3.1.5 级数的收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:274 -->

以部分和作为新的数列建立收敛，非负部分和用上确界允许扩展总和；先建立几何与p级数基准，再判别正项与变号，最后分别讨论重排和保序有限块分组。

###### 段：级数与部分和

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:276 -->

由有限和上限变化定义部分和、级数及其有限和；a_N=s_N−s_{N−1}证明单项趋零只为必要条件。非负总和由上确界定义，允许∞但区别于有限收敛。

###### 段：几何级数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:296 -->

由有限几何和与r^N→0推求和式、截断误差和|r|≥1的发散条件。

###### 段：$p$级数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:311 -->

用2^k至2^{k+1}−1的有限区块上下界，把p>1归约为几何上界，0<p≤1归约为每块固定正贡献，p≤0单项不趋零；不调用积分或尚未证明的无穷分组规则。

##### 3.1.5.1 级数的收敛判别

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:328 -->

先由非负部分和的单调性建立比较与比值判别，再区分绝对收敛和条件收敛；证明绝对收敛蕴含收敛，以Leibniz和Dirichlet处理抵消，并强调判定条件收敛还须排除绝对收敛。

###### 段：正项级数的收敛判别

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:333 -->

先比较、再极限比较；比值<1时统一用q<1几何控制，>1时单项不趋零，=1同时存在收敛/发散例说明无法判断。

###### 段：变号级数的两种收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:350 -->

正负抵消使部分和不再单调，引出绝对值和有限的绝对收敛与原和有限但绝对值和无穷的条件收敛；强调条件收敛的两个判断缺一不可。

###### 段：绝对收敛的判定

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:357 -->

对绝对值级数用正项判别，经部分和柯西估计证明原和存在；附绝对尾和误差界和交错平方倒数例。

###### 段：条件收敛的判定

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:372 -->

先Leibniz单调趋零条件、奇偶部分和证明与余项；交错调和级数为条件收敛例。再有限求和分部推Dirichlet尾和≤2Mb_m，注明该准则本身不保证非绝对收敛。

并排增加项与部分和的解析图，调和与交错调和固定相同绝对值，说明项趋零并不保证累计收敛。

##### 3.1.5.2 级数的重排和分组对收敛的影响

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:407 -->

分别检验改变项次序与合并有限相邻项：非负和绝对收敛级数允许任意重排，条件收敛可能改和；任何已经收敛的级数均允许保序有限分组，但分组后收敛不能反推原级数收敛。

###### 段：级数的重排

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:412 -->

用双射定义每项恰取一次的重新编号。非负重排以有限选项上确界证明，绝对收敛以共同绝对尾部控制，实数条件收敛以正负两端均∞和越过目标值构造说明可改和或发散。

###### 段：级数的分组

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:433 -->

仅允许保序有限相邻块；新部分和为旧部分和子列，所以原收敛时任何此类分组同和，包括条件收敛。1−1反例否定逆向；非负扩展和以共同上确界保持，作为覆盖求和的局部基础。

### 3.2 函数的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:450 -->

以去掉中心的约分函数引出实函数极限；先统一有限点、单侧、无穷远输入与值为无穷的极限，再直接用误差界建立常用极限，随后经序列判据逐项建立运算法则，最后讨论无穷小和渐近比较。

#### 3.2.1 函数极限与单侧极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:455 -->

从定义域聚点建立去心ε–δ条件，比较单侧与双侧，再分别改变输入趋向和输出取值范围，区分无穷远处的有限极限与值为无穷的极限。

###### 段：聚点

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:456 -->

先问定义域是否存在任意靠近中心的异点，再给去心条件；0属于(0,1)的聚点而非集合元素，解释为何排除孤立输入。

###### 段：函数极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:464 -->

由输入误差控制输出误差，给ε–δ条件，解释去心不约束f(a)，以约分函数逐项验证δ=ε。

增加输入δ邻域与输出ε带的对应图，用基点改值说明函数极限不要求等于基点取值。

###### 段：左极限与右极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:487 -->

分别限制输入方向，须该侧有趋近点；双侧判据有两侧均能趋近的前提，指示函数示范不同单侧极限。

###### 段：无穷远处的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:499 -->

分别在定义域向右、向左无界的条件下，以所有越过输入门槛的点控制输出误差；以1/x说明两个无穷远方向的有限极限。

###### 段：值为无穷的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:508 -->

输出逐一越过任意实数门槛；单侧附方向限制，1/x示范双侧并无同向无穷极限。

#### 3.2.2 常用极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:513 -->

三角函数以单位圆不等式给出直接误差界，指数函数以绝对收敛级数构造并给出二阶余项界；先于一般函数极限运算建立结论，不预用后面的运算法则、求导或积分。

###### 段：三角函数的基本极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:515 -->

弧度制与几何面积不等式给出0≤1−sin(h)/h≤h²/2；直接选择δ控制误差，偶性处理负方向，再由|1−cos(h)|/|h|≤|h|/2得到第二个极限。

###### 段：自然指数函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:533 -->

比值/几何控制指数级数收敛；绝对矩形尾部证明可按总次数合并，有限系数递推得加法公式。二阶余项界得标准极限，再推正性、严格递增、两端趋向及点处连续。

#### 3.2.3 极限的性质与运算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:580 -->

先证明任意趋近输入列的序列判据，再分别讨论和、差、常数倍、积、商及夹逼；共同定义域与聚点固定，运算针对有限极限，商另要求分母极限非零。

###### 段：序列判据

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:581 -->

正向把共同δ用于尾部，反向从每个1/n邻域选固定输出误差反例列；必须对任意允许列成立。

###### 段：和的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:585 -->

固定共同定义域D、聚点a和有限极限b、c；任意允许输入列上调用数列和的法则，再由序列判据得到函数和的极限公式。

###### 段：差的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:595 -->

单独列出函数差的极限公式，通过任意允许输入列的差极限和序列判据推出结论。

###### 段：数乘的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:602 -->

固定实数倍数λ，明确极限与常数倍交换；以数列法则和序列判据证明，补充λ=0情形。

###### 段：积的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:609 -->

两个函数均有有限极限时，输出积沿每列允许输入趋于极限之积，由序列判据控制全部趋近方式。

###### 段：商的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:616 -->

额外要求分母有限极限非零，以误差|c|/2保证邻域内分母远离零，再调用数列商法则；约分示例说明0/0情形须另作处理。

###### 段：夹逼定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:626 -->

在共同去心邻域中假设上下界函数趋于同一有限值，用同一输入邻域控制中间函数；以x sin(1/x)在零点附近的极限说明运用。

#### 3.2.4 无穷小与无穷大

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:635 -->

统一趋零与绝对值趋无穷的过程性语言，再比较相对大小；不将无穷小当固定非零数。

###### 段：无穷小

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:637 -->

由函数、数列和余项共同需要引出趋零名称，保留指定趋向和固定小数的区别。

###### 段：无穷大

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:643 -->

通过任意固定门槛与倒数衔接趋零，区分|f|→∞与单一符号的无穷极限。

###### 段：渐近记号

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/01-limits.tex:649 -->

对最终非零基准定义o、O和比值→1，逐例比较趋零/增长；图示3n+7、n/10、10√n与n的比值，随后在最终正项条件下定义Ω、Θ并指出上界未必精确阶。

### 3.3 集合的度量

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:1 -->

> 【最小调整】本节拟改名为“实数集的邻域与闭区间性质”。一般度量的公理、伪距离与一般空间极限后移；保留本节已有的实轴邻域、开闭集与闭区间有限覆盖材料。以下暂沿用原编号逐项定位，不另造 subsubsection 或 paragraph。

正文入口：[`02-metric-spaces.tex`](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex)。从前两节数列与函数极限中的误差条件出发，指出这些定义都在控制距离，而向量、函数之间的远近不能直接用绝对值表示。本节把绝对值距离抽象为度量，再用开球描述开集与闭集，把收敛、柯西条件与完备性写成一般空间中的条件，最后证明闭区间的紧致性；这些工具在下一节用于连续函数的最值与一致连续，在测量一节用于把可数覆盖化为有限覆盖。

#### 3.3.1 度量的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:14 -->

> 【后移】本 subsection 及其“度量”“伪距离”两个 paragraph 整体移入第二部分“度量空间”；第一部分直接使用绝对值距离，不再陈述一般度量公理。

以实数和向量距离说明一般距离应满足的三项规则，保留伪距离及按零距离取商的实际例子，以区分原对象相等与比较规则不能分辨。

###### 段：度量

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:16 -->

给出度量与度量空间的定义，分别解释零距离判别、对称性和三角不等式的职责，以欧氏距离、离散距离说明同一抽象条件容许不同的接近规则。

###### 段：伪距离

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:38 -->

由只比较二维向量第一坐标的例子引出伪距离，定义零距离等价关系，证明商距离不依赖代表元，并解释商对象并未恢复被忽略的坐标。

#### 3.3.2 邻域与开闭集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:69 -->

> 【保留，限于实轴】原标题与下级顺序保留；对象固定为实数子集，用开区间说明邻域与开闭性，为闭区间定理及一元连续性提供当地前提。任意度量空间的版本移至第二部分。

由距离阈值建立开球与邻域，再定义开闭集并核查空间相对性，利用三角不等式证明开球是开集，说明开集的任意并和有限交封闭。

###### 段：开球与邻域

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:71 -->

> 【必要改名】此 paragraph 拟由“开球与邻域”改为“开区间与邻域”，使用 (x-r,x+r)；不引入一般空间中的球。

以中心与正半径收集足够接近的点，定义开球，并将包含某个开球的集合称为邻域；配图以虚线圆盘和包含它的闭矩形，区分开球与邻域，说明邻域本身不必开。

###### 段：开集与闭集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:92 -->

通过每个点均具有内部小球定义开集，以补集定义闭集；三面板图比较实轴开区间、闭区间端点及子空间中的半开区间，说明开闭性相对于所在空间；再证明开球开、任意并开、有限交开，给出无限交不一定开的反例。

#### 3.3.3 度量空间中的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:121 -->

> 【后移】本 subsection 的一般空间版本及全部下级标题移入“度量空间”。其中实数柯西列有实数极限、而有理近似可在有理数域内没有极限的例子和相关图保留为实数完备性的补充，接回本章已有“柯西数列的收敛”，不新增一般完备空间定义。

先把实数序列的收敛与柯西条件推广到一般距离，比较不同度量的影响；继而用完备性与闭集序列判据检查极限是否保留在空间内，最后为输入与输出分别指定度量，推广函数极限。

###### 段：序列的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:123 -->

由二维点列的坐标误差进入一般度量收敛与柯西定义，通过同一实数列在通常和离散度量下的不同结论说明距离是结构的一部分。

###### 段：完备度量空间

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:156 -->

由尾部互近不保证域内极限引出完备性，说明实数和有限维欧氏空间完备，以逼近根号二的有理数列说明有理数空间不完备，并保留误差界图。

###### 段：闭集的序列判据

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:181 -->

将补集为开改写为保留母空间内序列极限的条件，双向证明判据，再说明完备母空间的闭子集完备及完备子空间必闭，区分闭性与有界性。

###### 段：函数的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:202 -->

分别为输入与输出指定度量，在输入聚点处定义函数极限，解释这只是替换实数误差的两种距离，并回顾序列判据失败时逐邻域选点的证明机制。

#### 3.3.4 闭区间的有限子覆盖性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:217 -->

> 【保留，限于实轴】本 subsection 及“开覆盖与有限子覆盖”“闭区间的紧致性”两个 paragraph 保留；证明直接使用开区间和实数确界。实轴有界闭集的推广保留，一般度量空间中紧致与序列紧致的关系后移。

先定义开覆盖、有限子覆盖与紧致性，再只依赖有界实数列存在收敛子列证明闭区间的有限子覆盖，避免提前使用连续函数理论。

###### 段：开覆盖与有限子覆盖

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:219 -->

由可数区间覆盖将用于长度下界的需要引出覆盖语言，强调有限子覆盖须从原集合族选择，不能另造覆盖。

###### 段：闭区间的紧致性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/02-metric-spaces.tex:234 -->

先以带语义标签的量词公式给共同邻域半径结论，反证时构造区间内点列并取收敛子列，用一个开覆盖成员的局部半径取得矛盾；该结论供后面黎曼可积性判据直接引用；再有限分割区间选取有限子覆盖，并推广到有界闭集。

用闭区间的有限开覆盖与开区间的U_n=(1/n,1)对照；最大下标留下未覆盖区间，说明有限子覆盖与定义域边界的联系。

### 3.4 本章小结

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/04-function-limits.tex:16 -->

总结极限存在与计算、级数重排与分组的区别，以及距离如何支持收敛和紧致性。

## 第4章 线性空间

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex:1 -->

正文基底：[原线性空间章](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex)。以下是拟实施的重组细纲；标题和编号是本次方案，来源对应关系见文末迁移表。

同一组观测既可以写成向量，也可以写成矩阵；选定坐标后，还需比较空间、度量误差并反求输入。本章全部在实线性空间与实矩阵上展开，向量和矩阵的转置统一记为$^{\top}$。由“极限”章进入后，矩阵序列与迭代极限已有实数收敛作为依据。

本章按四个问题组织：怎样表示对象，怎样计算，怎样求未知量，以及怎样判断近似和误差。表示部分建立线性组合、基、坐标与映射的语言；运算部分说明输入输出、计算规则与实现；方程和优化部分按目标区分问题，并在各问题内部建立所需分解和迭代；分析部分分别研究固定问题的收敛与扰动后的变化。

> 【重组边界】本章沿用现有正文材料，按本轮授权重新拆分、归位并补齐求解分类。新增方法与必要桥接标“补充”。本章仍先于微积分：最小二乘与二次目标先由正交分解、增量展开或配方论证；一般求导、一般非线性优化、无限维函数空间留在后文。行列式、逆与迹在本章建立，不恢复已删除的1.5.7—1.5.9。

### 4.1 表示

先辨认要记录的对象，再确定允许的线性组合、独立方向和坐标。子空间说明对象所在的范围，映射及其矩阵说明输入怎样对应输出，对偶说明如何读取坐标；商空间和换基关系分别描述忽略差别与改变记录的两种方式。这里回用第1章的基础计算记号，计算方法及度量规则在运算节集中展开。

#### 4.1.1 对象

本小节辨认标量、向量、矩阵与张量，先说明对象及其记录方式，再核对坐标、轴与形状。张量在这里建立对象层面的认识；张量积的正式构造、多重坐标及相应运算在4.2展开。

##### 4.1.1.1 标量

以一个观测值或系数说明实标量的作用，所有线性组合使用实数系数。标量、坐标列和矩阵具有不同角色，不能因记录中都出现数值而混淆类型。

###### 段：数值与系数

说明标量既可作为结果，也可用于缩放其他对象。区分一个标量、由标量组成的坐标列及矩阵，不用形状相同的记号替代对象类型的说明。

##### 4.1.1.2 向量

用三维位移、有限信号和固定次数上界的多项式说明向量是可相加和缩放的对象，不天然等同于一串数。选定坐标后用行向量或列向量记录；第1章的加减、数乘和线性组合规则在此只作回用。

###### 段：对象与坐标

同一几何位移在不同坐标系中的数值可以改变，对象本身不因此改变。基和坐标唯一性的依据在下一小节建立，当前只明确坐标是一种记录方式。

##### 4.1.1.3 矩阵

说明矩阵的尺寸、行、列与分块约定，把一张矩阵看成矩阵空间中的一个元素。矩阵也能记录线性映射，但需额外指定输入、输出及两端坐标，在4.1.5建立这种角色；此处不因同一份数表而混同两个数学对象。

###### 段：形状与角色

沿用第1章的行列、常见矩阵与基本运算，检查记录的观测、特征或输入输出维数。保留必要的小矩阵例子，不重复逐项加减及行乘列的计算教程。

##### 4.1.1.4 张量

从多个方向或多路输入共同决定一个量的例子，介绍对每个输入分别保持相加与缩放的多线性对象；选定各方向的坐标后，用多索引数组记录其系数。这里先辨认对象、槽位和记录，正式空间构造与运算由4.2的张量积承担。

###### 段：阶、轴与形状

用一个三阶系数表说明阶是槽位数，形状记录各坐标轴的长度，轴的含义还需由所属空间和输入输出角色确定。不能把一个轴的长度与张量的阶混为一谈，也不能只按数组外形判断两个对象是否相同。

###### 段：对象与数组

同一张量在不同坐标约定下可以有不同数表，改变坐标时各轴的记录须同步变换。矩阵可记录二阶对象，也可记录线性映射，两种角色须根据其槽位类型区分；4.1.6的对偶与4.2.9的张量积将补齐这种类型及换基规则，数组本身不自动提供这些约定。

#### 4.1.2 线性空间

由相加与缩放规定对象组成的实线性空间，再研究线性组合能覆盖多大范围、系数是否唯一。张成回答表示能否存在，线性无关回答表示是否有冗余；二者共同引出基和维数。子空间的最小定义在此建立，包含、交、和与直和随后展开。

##### 4.1.2.1 线性空间

由位移、有限信号、多项式和同形矩阵的相加、数乘进入，明确元素集合、标量域和允许运算必须共同指定。说明封闭性、零向量和加法逆元各自保证什么，再建立线性组合，为后续“能否表示全部对象、系数是否唯一”提供语言。

###### 段：空间公理

在实数上逐条解释相加和缩放的规则。非负向量集合对任意实数数乘不封闭，展示仅知道对象外观仍不足以确定线性空间。

###### 段：空间的例子

将几何位移、有限信号、固定次数上界的多项式和同形矩阵作为沿用相同线性规则的例子。矩阵空间按逐项相加、数乘构成有限维线性空间；矩阵作为空间元素的这一角色，与它在线性映射部分记录作用的角色分开说明。集合在原运算下自身构成线性空间时称为子空间；先给出这一检验规则，供张成空间、核与像使用；此处不展开空间之间的关系。

##### 4.1.2.2 线性相关与线性无关

先问候选方向能否到达全部对象，再问同一对象的系数是否有冗余。用张成描述能够到达的范围，存在一组不全为零的系数使线性组合为零时称为线性相关；只有全部系数为零才能表示零对象时称为线性无关。用线性无关排除零对象的非平凡表示；这两个条件分别对应表示的存在与唯一，不能互相替代。

###### 段：表示的存在与唯一

用同一组方向分别展示“不够张成”“张成但冗余”“恰好唯一表示”三种情形。坐标的唯一性来自线性无关，不能由能够表示所有对象单独推出。

##### 4.1.2.3 基与维数

将既张成又线性无关的一组方向称为基，说明有限维对象由基系数唯一确定。保留从张成族删去冗余、把独立族扩充为基的论证，再由基之间的比较证明有限维数不依赖所选基；这些是后面秩—零度与坐标变换的依据。

###### 段：维数

沿用基的扩充论证，把维数解释成独立系数的个数。零空间允许空基、维数为零；对零对象和退化情形单独说明，避免后续秩判据遗漏边界。

#### 4.1.3 子空间

固定同一个有限维实空间$V$，研究它的子空间如何包含、相交与共同容纳方向。先判断一个范围是否属于另一个范围，再分别寻找最大的公共子空间和最小的共同容纳空间，最后讨论两部分是否有重复方向。这里的四块始终比较同一环境中的子空间。

##### 4.1.3.1 子空间包含

由一条直线是否位于某个平面内进入$U\subseteq W\subseteq V$，说明包含表示$U$的每个方向均属于$W$。包含比较的是对象范围，维数只记录独立方向的个数。

###### 段：范围与维数

由基的扩充证明包含时$\dim U\leq\dim W$，包含且同维时二者相等。用平面中的两条不同直线说明同维本身不能推出同一子空间，也不能推出其中一者包含另一者。

###### 段：补充方向

把$U$的一组基扩充为$W$的基，解释新增方向记录了哪些原范围之外的自由度。回用4.1的基扩充结论，不把相同证明重新写成另一套定义。

##### 4.1.3.2 交空间

以两组方向的公共部分定义$U\cap W$，验证其封闭性，并证明它是同时包含在$U$与$W$中的最大子空间。把两个范围之间的共同信息转成一个明确的空间对象。

###### 段：公共方向

沿用同一平面中重合与不同的两条直线，分别得到整条直线与零子空间。交为零只说明没有共同的非零方向，此时尚未声称二者能共同覆盖整个环境空间。

###### 段：共同约束

当$U,W$分别由齐次线性约束描述时，同时满足两组约束的向量组成交空间。这里建立集合和约束的对应，具体消元求基在4.3的方程问题中回用。

##### 4.1.3.3 和空间

以$U+W=\{u+w:u\in U,w\in W\}$定义共同容纳两组方向的空间，证明它是同时包含$U,W$的最小子空间。与并集比较：并集未必对相加封闭，和空间则补入必要的线性组合。

###### 段：维数公式

先取$U\cap W$的基，再分别扩充为$U,W$的基，从张成与无关推出$\dim(U+W)=\dim U+\dim W-\dim(U\cap W)$。被减去的维数正是两边重复计入的公共方向，而非两个集合元素个数的差。

##### 4.1.3.4 直和

在和空间中进一步要求每个向量的两部分表示唯一，证明这等价于$U\cap W=\{0\}$，此时记为$U\oplus W$。用同一组直线例子区分能够相加、没有重复方向与覆盖整个环境空间三个判断。

###### 段：补空间

要写$V=U\oplus W$，还须满足$U+W=V$。有限维中可由基扩充选出这样的$W$，但选择一般不唯一；指定内积后的正交补由4.2.4.4介绍，不能把一般补空间自动称为正交补。

#### 4.1.4 坐标与换基

基保证表示唯一以后，分别研究如何读取坐标，以及改变基时如何转换同一对象的记录。

##### 4.1.4.1 坐标

对有序基$\mathcal B=(b_1,\ldots,b_n)$，由$x=\sum_i x_i b_i$定义坐标列$[x]_{\mathcal B}$。对象的空间、基的顺序和坐标列的顺序同时固定，坐标映射因唯一展开而是线性双射。

###### 段：基的顺序

用同一组二维方向交换排列，说明向量不变而坐标次序随之改变；再用多项式在单项式基中的系数说明，向量可以不是几何箭头。坐标个数是维数，不能由某个冗余记录的长度直接推断。

##### 4.1.4.2 换基

将新旧基之间的展开系数排成换基矩阵，从对象相等推导坐标转换式，并由两组基均能唯一表示对象说明转换可以双向进行。反向换基矩阵表示双向坐标转换；一般映射的可逆条件在4.1.5.4建立。固定对象换坐标与固定坐标系移动对象使用相似的乘法形式，但输入输出含义不同。

###### 段：被动换基与主动作用

在二维斜基和标准基中记录同一向量，逐项检查坐标改变而向量不变。再固定标准基施加线性作用，比较两种操作，说明不能把所有乘矩阵都理解成换基。

#### 4.1.5 线性映射

从保持线性组合的对应关系出发，分别选定输入和输出基，用基向量的像构造矩阵表示。核、像、秩和零度随后描述丢失与保留的自由度，并用于判断单射、满射与可逆性；这些是后面反求未知量的依据。

##### 4.1.5.1 线性映射

把保持相加和数乘的作用定义为线性映射，对定义域与值域分别选基，用输入基向量的输出坐标构成矩阵列。由任意输入的基展开推导矩阵乘向量，明确一个映射依赖两端空间，而它的矩阵记录还依赖两端选基。

###### 段：基向量的像

逐个记录输入基向量被送往哪里，再由线性性恢复任意输入的输出。矩阵的列数对应输入坐标维数，行数对应输出坐标维数；改变两端任一组基通常改变数表，却仍可记录同一个映射。

###### 段：线性映射与仿射映射

说明固定矩阵作用保持线性叠加；带常数偏置的作用一般为仿射映射，仅在偏置为零时才线性。齐次坐标可将仿射复合记成增广矩阵，具体形式放在4.2.2.2，但原变量中的作用类型不能因此混淆。

##### 4.1.5.2 核与像

定义核为被送到零的输入集合，像为所有可到达的输出集合，并通过相加与数乘验证二者为子空间。由$Tx=Ty$当且仅当$x-y\in\ker T$，说明输入相差核方向时输出无法辨认。将这些不可辨认输入合成等价类的商空间构造在4.1.7建立，此处先用核描述不可辨认的输入。

###### 段：核与像的例子

用二维到一维的线性读取同时画出输入端的核和输出端的像。核描述输入的丢失方向，像描述输出的可达范围，不能把它们当成同一空间中的两个集合直接比较；方程右端是否可达在4.3据此判断。

##### 4.1.5.3 秩与零度

将秩定义为像的维数，将零度定义为核的维数。取核的一组基并扩充成输入空间的基，证明新增基向量的像构成像空间的基，从而得到秩—零度关系；这一论证只使用基与维数。

###### 段：满秩与形状

对$m\times n$矩阵分别定义满列秩$r=n$、满行秩$r=m$和未达到可能最大秩的情形；宽矩阵满行秩仍可能有非零输入核。当前以列张成空间读取秩，行秩等于列秩的证明在4.1.6.2由对偶映射补齐，4.3再用消元作计算检验。

##### 4.1.5.4 单射、满射与可逆性

由核为零刻画单射，由像等于整个输出空间刻画满射，两者同时成立时得到双射和线性逆映射。有限维等维空间中，单射、满射、双射等价；维数不同则须分别判断，不把矩形矩阵的满秩直接说成双侧可逆。

###### 段：逆与单侧逆

在选定坐标后将逆映射记为$A^{-1}$。方阵的左逆或右逆足以推出双侧逆；满列秩长矩阵可有左逆，满行秩宽矩阵可有右逆，但这些单侧逆一般不唯一。此处判断恢复关系是否存在，如何通过分解应用逆以及多解时如何选最小范数代表由运算及方程和优化回答。

#### 4.1.6 对偶表示

把向量读成标量的线性规则也组成空间。先由原基构造对偶基，再由映射复合解释读取怎样从输出端转到输入端；这一代数表示不要求先有内积。

##### 4.1.6.1 对偶空间

从读取一个坐标、计算一个线性加权和的例子进入，说明一个向量可以接受多种标量读取。把这些读取规则收集起来时，需要明确它们怎样相加与缩放，以及由多少独立系数决定。

###### 段：线性泛函

把保持相加和数乘的$\varphi:V\to\mathbb R$称为线性泛函，并用逐点加法与数乘建立对偶空间$V^*$。输入向量是被读取的对象，泛函是读取规则，二者属于不同类型，此处不依赖内积来识别它们。

###### 段：对偶基

对$V$的一组基逐个定义读取相应坐标的泛函，证明任意泛函都能唯一展开在这组读取下。由此得到对偶基及$\dim V^*=\dim V$；用向量与对偶基的配对值解释坐标为什么能够逐项恢复。

##### 4.1.6.2 对偶映射

已知$T:V\to W$以及输出端的读取$f$，输入$x$经过$T$后被读成$f(Tx)$。由这项复合定义$T'f=f\circ T$，得到$T':W^*\to V^*$；反向传递的是读取规则，并非对$T$求逆。

###### 段：转置表示

在对应的原空间基与对偶基下，逐项推导$T'$的矩阵为$A^{\top}$。读取回传的公式只使用线性性和坐标，不需要长度、夹角或内积；换基时须同时遵守向量与对偶坐标的配对关系。

###### 段：行秩与列秩

把$\ker T'$刻画为在$\operatorname{im}T$上恒为零的读取，用像空间的基扩充计算其维数，再由秩—零度得到$\operatorname{rank}T'=\operatorname{rank}T$。在矩阵记录下完成行秩等于列秩的证明，闭合4.1.5留下的秩判据。

#### 4.1.7 等价类与商空间

当相差某个子空间内方向的对象应视为同一结果时，用等价类表示保留下来的信息，再核对类上的线性运算和维数。这里只消去指定的代数差别；度量能否在等价类上成立，在范数运算中判断。

##### 4.1.7.1 等价类

以$x\sim y$当且仅当$x-y\in U$定义关系，验证自反、对称与传递性，并将$x$的等价类写成$x+U$。区分一个向量、表示它所在类别的代表元，以及整个等价类；两个类相等不要求当前选取的代表元相等。

##### 4.1.7.2 商空间

全部等价类组成$V/U$，通过代表元规定类上的加法与数乘。这里构造的是忽略指定方向后的对象空间，不需要先为每一类选一个固定代表。

###### 段：代表元无关

更换代表元只会给其线性组合增加$U$内的向量，因此加法和数乘仍得到同一等价类。核对零类与逆元，证明商空间满足实线性空间公理。

###### 段：维数

把$U$的基扩充为$V$的基，证明新增方向的等价类构成商空间的基，得到$\dim(V/U)=\dim V-\dim U$。与直和按独立分量组合的作用对照，取商消除的是指定的差别。

##### 4.1.7.3 商映射

自然映射$q:V\to V/U$把向量送到其等价类，证明它线性、满射且核为$U$。用这项映射把线性映射中的核像语言与当前等价关系联系起来。

###### 段：核与可达输出

对$T:V\to W$取$U=\ker T$，验证$[x]\mapsto Tx$不依赖代表元，并建立$V/\ker T$到$\operatorname{im}T$的线性同构。压去全部丢失方向后，每个等价类恰对应一个可达输出，但原映射本身未必具有双侧逆。

#### 4.1.8 换基下的矩阵表示

比较同一对象在不同坐标下的数表。相似固定同一自映射，相抵允许输入输出独立换基，合同同时改变二次型的两个输入位置；每种关系内部依次说明定义、含义、不变量和判定条件，避免混用三种坐标约定。

##### 4.1.8.1 相似

比较同一个实线性自映射在不同基下的矩阵记录，分别回答相似表示什么、保留哪些性质，以及两个已给矩阵怎样判定相似。定义时写明对象与可逆条件，判定部分再区分必要条件和充要条件。

###### 段：定义与含义

对同阶实方阵$A,B$，若存在实可逆矩阵$S$使$B=S^{-1}AS$，称二者相似。它记录同一个自映射使用不同基，两端坐标变换由同一个$S$联系；不要求$A,B$自身可逆。

###### 段：坐标解释

从$x=Sz$将旧坐标换成新坐标，再把同一作用的输出也换到该新基，推导$S^{-1}AS$。说明固定对象换基与固定坐标主动作用不同，相似只改变记录方式。

###### 段：性质

证明相似具有自反、对称与传递性，再由可逆坐标对应研究哪些数量保持。核和像在换基下相互对应，坐标集合本身未必逐点不变。

###### 段：不变量

推导$\ker B=S^{-1}\ker A$、$\operatorname{im}B=S^{-1}\operatorname{im}A$，从而得到秩、零度与各次作用的核维数不变。行列式与特征多项式在4.2.7.2的运算定义建立后补充其相似不变性，迹在迹运算中核对；当前位置只使用已有的坐标和维数。

###### 段：反复作用

由两次作用的中间换基相消，推导$B^k=S^{-1}A^kS$，说明反复作用仍表示同一个过程。相应核的维数等信息保留，但一般换基不保持当前坐标下的欧氏长度与夹角。

###### 段：条件

同阶方阵与可逆的实换基矩阵是适用前提。秩、零度以及$\ker(A-tI)$的维数相同是可直接检查的必要条件，仍须说明它们是否足以建立整个作用的坐标对应。

###### 段：充要条件

将相似等价改写为$AS=SB$存在一个可逆的实解$S$。前一个等式是关于各元素的线性限制，后一个条件保证它确为换基；只找到非零但奇异的$S$并不充分。行列式建立后，可把可逆性改写为$\det S\ne0$；具体求解归矩阵方程。

###### 段：必要条件的边界

用$I_2$与$\left[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right]$说明同秩并不足够：二者的$\ker(A-I)$维数不同，因而不相似。行列式运算建立后进一步核对它们同行列式、同特征多项式，仍不能相似；后文具体问题再建立谱分解或Jordan表示。


##### 4.1.8.2 相抵

比较两个实空间之间的线性映射在输入、输出独立换基下的矩阵记录。先解释两端坐标怎样分别改变，再研究不变量，并给出同形矩阵之间的完整判据。

###### 段：定义与含义

对同为$m\times n$的实矩阵$A,B$，若存在实可逆矩阵$P\in\mathbb R^{m\times m}$和$Q\in\mathbb R^{n\times n}$使$B=P^{-1}AQ$，称二者相抵。矩阵可以为长方形，输入与输出的基分别选择，两端不必由同一个换基矩阵联系。

###### 段：坐标解释

从输入$x=Qz$和输出$y=Pw$分别代入$y=Ax$，推导双侧换基公式并核对尺寸。与相似比较时，固定的是两个空间间的作用，不要求把它当作同一空间上的自映射。

###### 段：性质

证明相抵具有自反、对称与传递性，再追踪核和像在各自坐标中的变化。可逆坐标变换保留自由度，但不保证保留与某一端特定坐标有关的几何数值。

###### 段：不变量

由$\ker B=Q^{-1}\ker A$和$\operatorname{im}B=P^{-1}\operatorname{im}A$证明秩、输入零度$n-r$和输出缺失维数$m-r$不变，其中$r$为秩。这里保持的是两端方向的独立个数，不能宣称原坐标中的核或像逐点不动。

###### 段：改变的量

以同阶可逆矩阵均相抵为例，说明相抵允许的记录变化比相似更宽。两端坐标独立改变，不能要求同一组方向的大小、角度或单端作用的数值信息保持；相应行列式变化公式在行列式运算中建立。

###### 段：条件

同形是比较前提，$P,Q$分别可逆是合法换基条件；$A,B$本身无需满秩。固定形状之后，秩就是相抵的完整不变量。

###### 段：充要条件

证明两个同形实矩阵相抵当且仅当秩相同。必要性由两端可逆得到；充分性通过核基扩充、把新增方向的像作为输出基并补齐，使两者都得到相同的$I_r$与零块记录。这是基和维数的关系证明，具体消元与SVD算法仍在后面的实际任务中建立。

###### 段：退化情形

分别核对零秩、满行秩、满列秩与一般秩亏，保留矩阵形状对可能秩的限制。同秩但不同形状的矩阵不直接称为相抵；零、非零行列式的关系在后面的方阵体积计算中回读。


##### 4.1.8.3 合同

本节在实对称矩阵及其二次型范围内，比较同一能量配对使用不同坐标时的表达。分别建立合同的含义、保持的符号结构，以及允许退化时的完整判据；充分性的构造证明在实对称谱建立后回读。

###### 段：定义与含义

对同阶实对称矩阵$A,B$，若存在实可逆矩阵$S$使$B=S^{\top}AS$，称二者合同。把同一个坐标代换同时作用于二次配对的两个位置，记录的是同一个二次型，而非同一自映射的输入输出换基。

###### 段：坐标解释

由$x=Sy$代入$x^{\top}Ax$，得到$y^{\top}(S^{\top}AS)y$，逐项比较合同、相似与相抵两端变换的含义。先称$q_A(x)=x^{\top}Ax$为二次型，用正、负或零的数值描述方向能量。对所有非零$x$都有$q_A(x)>0$时称为正定，对所有$x$都有$q_A(x)\geq0$时称为半正定；既取正值又取负值时称为不定。后面建立加权内积时，其权矩阵换基回用同一公式。

###### 段：性质

证明合同具有自反、对称与传递性，并由可逆坐标对应比较二次型的正、负和核方向。惯性记录这些方向的独立个数，不要求保持各方向原有的数值尺度。

###### 段：不变量

以使二次型严格为正或严格为负的最大子空间维数，以及$\dim\ker A$，定义惯性三元组$(n_+,n_-,n_0)$。证明这些维数在合同下不变，因而秩、正定、半正定和不定等符号性质保持。零指标取核维数，不是不定二次型中所有零能量向量的数目或集合维数。

###### 段：行列式

当前先比较能量符号：$I_2$与$-I_2$同秩，但一个在全部非零方向为正、另一个全部为负，故不合同。行列式建立后再得到$\det B=(\det S)^2\det A$，并用同一对矩阵补充“同行列式仍不足以判定合同”的边界。

###### 段：条件

本节的完整判据针对同阶实对称矩阵，要求换基矩阵实可逆，允许系数矩阵退化或不定。正定不是定义合同的前提，秩相同也不足以判定合同。

###### 段：充要条件

陈述实对称矩阵合同当且仅当惯性三元组相同，说明惯性在本范围内是完整不变量。必要性在当前由子空间的可逆对应证明；充分性需把正、负、零方向化为相同标准坐标，在4.3.3.2的二次极值问题建立实对称谱后完成，不把未展开的分解构造当作本节先修。

###### 段：条件的边界

以一正一负的二维二次型说明非零向量可能具有零能量，但不属于矩阵的核，故不能从某个方向的零能量判定零惯性。这里的同惯性充要分类不扩大到任意非对称矩阵；正定情形则只含正方向，因此同阶正定二次型彼此合同。

### 4.2 运算

对已经表示出来的对象执行计算，先给加法、数乘与乘法，再建立配对、大小、伴随和体积，随后讨论反复作用与多槽位运算。每项说明输入输出和相容条件，给出基础计算与性质，再按实际结构讨论高效实现或可控近似。第一章已出现的算式在这里接到空间、映射与计算代价，不重复一套记号教程。

本节给出算什么以及怎样执行，未知因子的拟合、最佳近似和方程求解在方程和优化节展开；迭代极限与系统的扰动界在分析节集中说明。

#### 4.2.1 加法与数乘

在同一实线性空间内合并或缩放对象，分别核对向量、矩阵、张量系数与映射的类型。把第1章的逐项公式解释成线性结构，并讨论显式记录和已有因子表示的计算成本。

##### 4.2.1.1 加法与减法

同空间元素按加法组成新元素，减法是加上加法逆元；矩阵和张量的逐项实现要求对应槽位、形状与坐标约定一致。检查交换律、结合律、零元和逆元，说明改变数表的坐标规则必须与相加保持一致。

###### 段：计算与结构

对$N$个显式系数逐项相加；已知稀疏支持时可按支持并集计算，但结果仍需记录所有非零位置。低秩因子表示的和可先保留为因子拼接，秩可能增加；强行压缩到固定秩是近似问题，最佳压缩在低秩逼近问题中建立。

##### 4.2.1.2 数乘与线性组合

把同一个实标量作用到全部系数，核对分配律、数乘结合律和单位作用，再以有限和$\sum_i a_i v_i$连接张成与坐标表示。系数与向量同时变化时是双线性计算；固定系数才是关于对象的线性作用。

###### 段：映射的叠加

对同一输入、输出空间的线性映射定义$(aT+bS)x=aTx+bSx$，相同基下由矩阵逐项叠加记录。若权重依赖$x$，所得作用通常不再线性；广播或跨槽位复制必须另给索引规则，不能由数乘公理自动推出。

#### 4.2.2 乘法

固定参与运算的对象角色，区分同形数组逐项相乘与矩阵作用的复合。它们都使用实数乘法，但输入约束、输出形状与交换规则不同；已有加减数乘只在分配律和线性组合中回用。

##### 4.2.2.1 逐项乘法

对同形向量、矩阵或张量数组定义对应系数的乘积，逐项检查输出形状、交换性、结合性与分配律。非同形输入必须另给索引扩展规则，不能默认存在一种自动匹配；逐项乘法也不等于矩阵复合或张量积。

###### 段：基础与结构化计算

显式遍历对应位置计算，按块或只访问已知非零项可以改变实现和中间存储。若要求完整稠密输出，仍需计入输出规模；使用截断或采样时须另报误差，不能把省略系数直接视为相同运算。

##### 4.2.2.2 矩阵乘法

回用矩阵乘向量及矩阵乘矩阵的系数规则，把$BA$解释为先施加$A$再施加$B$。明确中间维数相容，输入和输出所属空间清楚；固定系数矩阵作用线性，两个矩阵共同作为输入时乘积则分别线性。

###### 段：性质

证明相容尺寸下的结合律、分配律和单位元，保留一般不交换的反例。相同定义域和值域的映射可逐点相加或作固定系数混合；权重依赖输入时整体一般非线性，不能直接继承固定矩阵的叠加性质。

###### 段：基础计算

按输出位置累计内指标，给出$m\times n$与$n\times p$矩阵直接相乘的$mnp$次标量乘法计数。矩阵链的不同加括号方式可能改变计算量和中间数组，但不能交换因子顺序；更一般的缩约次序在4.2.12回用。

###### 段：仿射复合

用附加一维常数坐标的增广矩阵记录偏置，并通过分块乘法解释仿射作用的复合。增广记录不改变原变量中带偏置作用未必线性的性质。

###### 段：分块与结构化计算

按相容块大小将中间指标分组，得到分块乘法，并说明分块重用如何避免重复读取和不必要的中间展开。若输入已有稀疏、对角或低秩结构，按结构应用；例如给定$A=UV^{\top}$时，计算$AX=U(V^{\top}X)$，不必先展开整张$A$。

###### 段：代价条件

比较的是同一输出下的实际维数、非零项、因子规模和中间存储。保持因子形式只在后续允许隐式作用时减少展开；若必须输出全部系数，输出工作仍需完成，不以代数改写自动承诺运行时间降低。

###### 段：近似计算

若以已有近似矩阵替代原矩阵，先记录改变了哪个因子以及节省了哪些工作。误差的数值上界需要先建立范数，因此在矩阵范数中给出乘法误差界；已有低秩因子的作用仍可直接计算，最佳因子的求取归低秩逼近问题。


#### 4.2.3 转置与迹

转置改变行列记录，迹读取方阵的对角总量。它们分别产生矩阵和标量；在同一小例中核对尺寸、线性性和与复合运算的关系。

##### 4.2.3.1 转置

定义$(A^{\top})_{ij}=A_{ji}$并核对输出尺寸，证明两次转置恢复输入、转置保持加法，以及$(AB)^{\top}=B^{\top}A^{\top}$。更高阶数组的轴置换在4.2.10统一建立，不把所有换形都称为转置。

###### 段：计算与逆

转置按索引交换读取或重排，是否需要实际搬运取决于允许的存储和访问方式。对可逆因子另证明$(AB)^{-1}=B^{-1}A^{-1}$，强调相似的倒序形式具有不同成立条件。

##### 4.2.3.2 迹

对实方阵定义$\operatorname{tr}A=\sum_i a_{ii}$，直接逐项求和，并说明其读取所有同编号输入输出的总配对。矩形矩阵没有同一自映射意义下的迹；两矩阵乘积的迹须先核对乘积为方阵。

###### 段：性质与相似不变量

由有限求和证明线性性以及$\operatorname{tr}(AB)=\operatorname{tr}(BA)$，其中$A$可为$m\times n$、$B$为$n\times m$。循环移动相容因子时逐次核对尺寸，不能任意交换因子；由此得到$\operatorname{tr}(S^{-1}AS)=\operatorname{tr}A$，补齐相似表示中的这项不变量。

###### 段：结构化计算

若只需要迹，可直接累加所需的对角项；例如$\operatorname{tr}(AB)=\sum_{i,j}a_{ij}b_{ji}$可避免先形成整个乘积。后面的张量缩约把这种求和视作一个具体实例；此处不把精确改写当作随机近似。

#### 4.2.4 内积

先建立实内积的定义与不等式，再紧接加权内积，说明配对怎样产生长度、角度和正交。随后用同一配对读取子空间方向与线性泛函；一般范数在下一小节抽取长度公理。

##### 4.2.4.1 内积

从两个坐标向量的配对$x^{\top}y$进入，研究怎样用一个实数同时反映长度和方向关系。先规定配对规则，再证明它所产生的长度与夹角具有哪些性质。

###### 段：定义与含义

在实线性空间上规定内积的双线性、对称与正定条件，标准坐标配对作为最小例子。定义内积长度$\ell(x)=\sqrt{\langle x,x\rangle}$，解释自身配对怎样衡量一个方向的大小；此时先使用长度语言，范数公理在4.2.5.1建立。

###### 段：性质

证明Cauchy–Schwarz不等式及其等号条件，由此推出内积长度的绝对齐次性和三角不等式。由配对展开得到勾股关系与平行四边形恒等式，明确这些结论来自内积结构，而非任意长度函数。

###### 段：条件

非零向量才能由归一化内积定义夹角，Cauchy–Schwarz保证余弦处于$[-1,1]$；零向量没有方向角。两个不同向量的配对可以为负，自身配对则必须非负且仅在零向量处为零；双线性、对称与正定三项须分别检验。

###### 段：例子

在标准二维坐标下比较同向、正交与反向向量的配对，核对长度和夹角。用$x_1y_1-x_2y_2$说明对称双线性配对可能不正定，因而不能直接用来定义内积长度；不在这里加入正交化算法。

###### 段：基础计算

标准坐标中直接累计对应分量的乘积，两个$n$维向量需要$n$次标量乘法和相应求和；已知稀疏支持时只需访问共同非零位置。分块或改变求和次序保持精确实数结果，浮点舍入的差异在扰动分析中核对。

##### 4.2.4.2 加权内积

当不同方向需要使用不同单位时，在已有内积概念内改变配对规则。加权内积先作为内积的具体构造介绍，再由它产生长度和角度，阅读上紧接一般内积。

###### 段：定义与含义

对实对称正定矩阵$M$定义$\langle x,y\rangle_M=x^{\top}My$及长度$\ell_M(x)=\sqrt{x^{\top}Mx}$，以位移$x-y$的加权长度比较两点。对角权重改变各坐标方向的单位，非对角项还会耦合不同坐标，不能只按逐项缩放解释一般权矩阵。

###### 段：性质

回用一般内积的Cauchy–Schwarz、长度与夹角性质，说明$M=I$回到标准内积，严格正定保证非零向量具有正长度。由$x=Sz$推导换基后权矩阵变为$S^{\top}MS$，同一几何长度的数值保持；这一坐标关系回用表示部分的合同定义，不借分解定义加权配对。

###### 段：条件

$x^{\top}My$构成实内积当且仅当$M$对称且正定，仅检验自身配对为正不足以省去对称性。用$M=\left[\begin{smallmatrix}1&1\\-1&1\end{smallmatrix}\right]$说明$x^{\top}Mx=x^{\top}x$仍可能对应不对称配对；若$M$对称半正定但奇异，则得到退化配对，可能出现非零的零长度方向，半范数的名称和公理在4.2.5.1再建立。

###### 段：例子

用$M=\operatorname{diag}(1,4)$比较两个坐标单位方向的长度并解释椭圆等长度集合，再用$\operatorname{diag}(1,0)$展示不可见方向。给定实对称正定矩阵$\Sigma$时，取$M=\Sigma^{-1}$建立Mahalanobis型长度；协方差的统计来源在后续概率内容承接，当前先把它当作给定权重。实际坐标变换及退化权重下的选解由4.3.4处理。

###### 段：加权计算

直接计算$x^{\top}(My)$，一般稠密权矩阵需二次量级的标量运算；对角或稀疏权重按实际非零项计数。若已经给定$M=C^{\top}C$，可改为$(Cx)^{\top}(Cy)$并复用变换后的坐标；这里使用已给结构，如何构造该因子在正定方程求解中建立。

##### 4.2.4.3 正交

定义$u\perp v$当且仅当$\langle u,v\rangle=0$。零向量与所有向量正交，但没有方向角，也不能加入标准正交族；两两正交且每个向量长度为一的族称为标准正交族，若它张成整个空间则称为标准正交基。先辨认这些条件，再讨论如何读取坐标。


###### 段：正交坐标的读取

标准正交基下由与各基向量的内积直接读取坐标；正交但非单位的非零基向量还须除以其自身配对。由勾股关系核对重构与长度，把已有正交方向的使用同后面由一般方向构造正交基的算法分开。

###### 段：Gram矩阵与独立性

对方向族$u_1,\ldots,u_k$定义$G_{ij}=\langle u_i,u_j\rangle$，由$c^{\top}Gc=\ell(\sum_i c_i u_i)^2$证明$G$半正定，且正定当且仅当该方向族线性无关。此处用内积长度和相关性的定义证明，不依赖行列式或谱分解；Gram行列式所给的体积在行列式运算后建立。


##### 4.2.4.4 子空间的距离与夹角

先用内积长度定义点间距离，再定义正交补。若候选$p\in U$满足$x-p\perp U$，用勾股恒等式证明它是唯一最近点；存在性的实际构造留4.3.1。子空间之间的主夹角按单位向量配对的极值定义，再逐步限制先前方向的正交补，具体计算在谱子空间稳定性问题中展开。

##### 4.2.4.5 内积表示

为同一空间指定实内积后，研究一个读取是否能写成与某个向量的配对。这里把已有泛函表示成向量，不额外引入新的映射运算。

###### 段：表示向量

选定基，以Gram矩阵的正定性和可逆性证明每个泛函都能唯一写成$\varphi(x)=\langle a,x\rangle$。这一步建立存在与唯一，不调用尚未介绍的矩阵分解。

###### 段：内积的影响

同一个坐标读取$c^{\top}x$在权矩阵为$M$的内积下由$M^{-1}c$表示。改变内积可能改变表示向量，读取规则本身保持不变；因此不能省略所选内积的约定。

##### 4.2.4.6 矩阵配对

对同形实矩阵定义Frobenius内积$\langle A,B\rangle_F=\sum_{ij}a_{ij}b_{ij}=\operatorname{tr}(A^{\top}B)$，逐项验证内积公理。矩阵可以是长方形，乘积$A^{\top}B$为方阵；需内积的是同形系数对象，而不是任意两映射的复合。

###### 段：配对的计算

直接逐元素乘加即可得到标量，无需先形成$A^{\top}B$。标准系数配对对应固定正交坐标；若矩阵的行列各自采用不同的度量，须显式给出相应权重，不能把数表形状相同当作几何配对已确定。

#### 4.2.5 范数

从内积长度抽取大小的公理，再分别衡量向量、矩阵和线性读取。距离由差向量的范数产生；半范数允许不可分辨方向，利用已有商空间消除这些方向后再检验零分离。

##### 4.2.5.1 范数

从内积长度和加权长度中抽取共有公理，研究不必依赖配对也能衡量大小的长度尺度。一般范数只规定大小与两点距离，是否还能恢复内积和夹角须另外判断。

###### 段：定义与含义

规定非负、绝对齐次、三角不等式和零分离条件，并用前两块已经证明的长度性质说明内积长度都是范数。由$d(x,y)=\|x-y\|$定义两点距离，明确向量的大小和两个向量之间的距离是两个相关对象。

###### 段：性质

由三角不等式推出反三角不等式，说明长度之差受到位移长度控制，再验证所诱导距离的对称、三角不等式与平移不变性。这些性质只使用范数公理，不能自动带来夹角、正交或勾股关系。

###### 段：条件

一个实范数来自内积，当且仅当满足平行四边形恒等式；在此条件下用$\langle x,y\rangle=\tfrac14(\|x+y\|^2-\|x-y\|^2)$恢复内积，并列明双线性、对称与正定的验证路线。这一判据区分内积诱导的范数与一般范数，不把恢复公式无条件用于任意长度尺度。

###### 段：常用范数

先定义$1\leq p<\infty$的$p$范数及$\infty$端点，再用Hölder建立配对界、用Minkowski证明三角不等式，保留等号条件与端点处理。比较$1$、$2$、$\infty$范数对分散误差和极端分量的读法；取$p=\tfrac12$与两个坐标单位向量，说明相同形式在$p<1$时可能破坏三角不等式。再用二维$1$范数的两个坐标单位向量验证平行四边形等式左边为8、右边为4，说明该范数不能由内积诱导。

###### 段：分组范数

按行、列或固定分组先计算组内长度，再在组间累计，明确组内与组间指数均至少为1，且分组覆盖全部被计量坐标。用$\left[\begin{smallmatrix}3&0\\4&0\end{smallmatrix}\right]$比较组内欧氏长度、组间求和时按行得到7、按列得到5，说明分组会改变尺度；未覆盖坐标时可能留下零方向。

###### 段：半范数

放宽零分离条件得到半范数，接回前一块半正定权重产生的零长度方向。由齐次性和三角不等式证明$N=\{x:p(x)=0\}$是子空间，$p(x-y)=0$只表示当前尺度无法分辨两点；回用已经建立的商空间，在本小节最后构造消去全部零方向后的范数。

##### 4.2.5.2 矩阵范数

把矩阵当作一个元素时，可以衡量全部系数的大小；把它当作映射时，则需衡量它怎样放大输入。先区分这两种对象角色，再给出定义、性质和相容条件。

###### 段：定义与含义

以全部元素的欧氏长度定义Frobenius范数，以指定输入和输出范数下单位输入的输出大小上确界定义诱导范数。欧氏输入输出对应谱范数；先建立定义，奇异值计算公式在4.3.4.5服务任意秩选解时推导。

###### 段：性质

验证两类尺度各自的范数公理，并对相容的输入、中间和输出空间逐步推出诱导范数估计$\|AB\|\leq\|A\|\|B\|$。Frobenius范数与谱范数的数值及最佳逼近含义不同，后文误差估计须保留实际所用尺度。

###### 段：条件

乘法估计要求矩阵尺寸相容，而且相接空间使用一致的范数；不能把任意矩阵元素范数都自动称为相容范数。有限维一般范数下的有界性及最坏值达到在4.4.1.1补齐，当前位置不调用一般度量空间的紧性理论。

###### 段：常用公式

按定义推导诱导$1$范数为最大列绝对和、诱导$\infty$范数为最大行绝对和，以小矩阵核对二者的方向含义。Frobenius按全部元素累计，而谱范数按最大输出放大累计；SVD建立后再回读相应方向公式。

###### 段：乘法误差的度量

回到矩阵乘法中已有近似因子的计算，由相容性给出$\|(A-\widetilde A)X\|_2\leq\|A-\widetilde A\|_2\|X\|_2$。写明近似误差的尺度后才能比较允许误差与计算节省；最优低秩拟合在相应问题中建立，数据和浮点误差的系统分析归分析节。


##### 4.2.5.3 对偶范数

在读取规则已经建立以后，为输入指定范数，研究单位输入最多能产生多大的绝对读数。这是对已有泛函赋予尺度，须与向量的输入范数分别记号。

###### 段：读取的大小

以单位球上$|\varphi(x)|$的上确界定义$\|\varphi\|_{V^*}$，推导$|\varphi(x)|\leq\|\varphi\|_{V^*}\|x\|$。有限维一般范数下的有界性与最坏值达到在4.4.1.1补齐，这里不提前引用后面度量空间的紧性理论。

###### 段：常用尺度

回用Hölder不等式，逐项给出$p$范数与$q$范数在$1/p+1/q=1$时的对偶关系，并保留$1$与$\infty$两个端点。上界之后给出取等方向，说明为何得到精确的对偶范数，而非只有一个估计。

###### 段：内积读取的大小

回用已经建立的泛函内积表示，由Cauchy–Schwarz和取等方向证明：内积诱导范数下，泛函的对偶范数等于其表示向量的长度，零泛函单独处理。向量表示依赖所选内积，读取规则和对偶范数还分别依赖对应的配对与输入尺度。


##### 4.2.5.4 等价类上的长度

对本小节已经定义的半范数$p$及其零子空间$N$，在$V/N$上定义$\bar p([x])=p(x)$。用$|p(x)-p(y)|\leq p(x-y)$证明代表元无关，再验证范数公理和零分离，说明原空间的半距离怎样在等价类上成为真正距离。

###### 段：条件

这一直接公式使用全部零方向$N$，不能对任意子空间都无条件写成$\bar p([x])=p(x)$。等价类中的零差别与原空间中两个相同向量仍须区分，后面的退化权重问题回用此结论。

#### 4.2.6 伴随

已有对偶读取与内积表示以后，把输出端的向量配对转换成输入端的向量配对。先确定唯一的伴随作用，再区分标准坐标、加权坐标以及实际执行所需的线性求解。

##### 4.2.6.1 定义与计算

回用对偶映射和已经建立的内积表示，定义唯一的$S:W\to V$满足$\langle Tx,y\rangle_W=\langle x,Sy\rangle_V$，说明它把输出配对改写成输入配对。标准坐标内积下矩阵为$A^{\top}$，对偶映射作用于读取，伴随则作用于所选内积表示的向量。

###### 段：加权伴随

两端内积矩阵为$M_V,M_W$时，推导伴随矩阵$M_V^{-1}A^{\top}M_W$。计算时可通过转置作用、权重作用和线性求解执行，不必先形成完整伴随矩阵；实际求解方法在4.3展开。

###### 段：性质与条件

由配对证明线性叠加逐项取伴随、复合按相反次序取伴随，且在固定两端内积下再取伴随回到原映射。伴随不是逆映射，权矩阵须来自真正内积；伪逆仍记为$A^\dagger$并在选解任务中建立。

#### 4.2.7 外积与行列式

从两个方向围成的有向面积元素进入，先说明交换方向会改变符号、相关方向会使展开塌缩，再推广到多方向的有向体积。外积记录方向组合，行列式读取顶阶体积相对既定单位体积的系数；先固定实基和取向，不把较低阶的体积元素直接当成一个实数长度。

##### 4.2.7.1 外积

本节的外积指楔积$u\wedge v$。在实基$e_1,\ldots,e_n$下，用$i<j$的形式基$e_i\wedge e_j$记录系数$u_i v_j-u_j v_i$，验证双线性、交换变号及$u\wedge u=0$，并用二维、三维最小例子解释方向和塌缩。这一坐标构造不依赖后面的张量积；它与秩一矩阵$uv^{\top}$是不同对象。

###### 段：高阶外积

用交替规则记录多个方向的有向展开，说明有重复方向时为零，线性相关时整体也为零。在顶阶只有一个独立体积方向，较低阶则还保留平面或子空间的方向信息；这里只建立交替关系，不提前构造一般张量的因子模型。

##### 4.2.7.2 行列式

固定单位体积$e_1\wedge\cdots\wedge e_n$，以$Ae_1\wedge\cdots\wedge Ae_n$的系数定义$\det A$，连接多重线性、交替性与单位矩阵的归一化。证明交换两列改号、相关列体积为零，进而连接行列式非零与方阵可逆；乘法性由连续两次作用的体积比例得到。

###### 段：定向与尺度

行列式的符号记录相对取向，绝对值在标准欧氏坐标中给出平行多面体体积；抽象空间中还需指定体积单位，取向本身不确定尺度。已有行列式后，回到表示部分的相似、相抵与合同，补齐本小节最后所列的体积不变量，实际通过三角因子读取行列式与对数行列式则放在方程求解中。

###### 段：坐标构造

【补充】本节采用交替符号的坐标构造，让外积和顶阶体积先于张量积出现。交替坐标与顶阶外幂读取行列式可参考[Stanford的外代数讲义](https://math.stanford.edu/~conrad/diffgeomPage/handouts/tensor.pdf)及[Harvard关于顶阶外幂的课程说明](https://people.math.harvard.edu/~elkies/M55a.17/)；这里的交替坐标先行于一般张量积，内积已在本节前部建立。

###### 段：Gram行列式

在内积和行列式均已建立以后，以Gram行列式的平方根衡量由多个方向形成的实际无向体积，说明这一步把本小节的有向体积元素赋予数值大小。标准欧氏空间的顶阶情形回到$|\det A|$，未指定度量时不把低阶外积元素直接当作实数体积。

###### 段：基础与高效计算

用交替求和公式计算小阶行列式，再比较逐项展开、利用三角结构以及通过消元计算的工作量。稠密一般情形逐排列展开包含$n!$项，消元可把主要工作控制在三次量级；换行、缩放行与加另一行的倍数怎样改变结果须逐步记录，消元分解的完整构造在线性方程问题中建立。奇异情形不能对零主元直接作除法。

###### 段：换基不变量

对相似关系由乘法性证明行列式保持，并定义特征多项式$\chi_A(t)=\det(tI-A)$，证明它也相似不变；再次核对$I_2$与$\left[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right]$同特征多项式仍不相似。对相抵得到$\det B=(\det Q/\det P)\det A$，只保证方阵行列式是否为零保持；对合同得到$\det B=(\det S)^2\det A$，符号保持而数值一般改变。$I_2$与$-I_2$同行列式但不合同，完整判据仍需惯性。


#### 4.2.8 幂与矩阵函数

由有限次复合建立幂、多项式和快速乘幂，再用实数极限定义指数。平方根、实幂与对数先明确要求计算哪个对象及其定义域；实对称谱的构造及逐方向求值在二次极值问题中完成，当前位置不预用该分解。

##### 4.2.8.1 幂的定义与性质

规定$A^0=I$，负幂只对可逆矩阵定义。$P^2=P$表示第二次作用不再改变第一次结果；$N^q=0$表示有限次作用后归零，二者不能因都带“幂”就混成相似性质。

###### 段：幂等与投影

用$P=\operatorname{diag}(1,0)$说明$P^2=P$使正整数次作用等于一次作用，再以幂零矩阵比较有限步归零。一般幂等映射沿核投到像的代数解释使用4.1.3.4的直和；最近点意义和正交投影的计算在4.3.1建立，此处不预用该构造。

##### 4.2.8.2 实特征方向与幂增长尺度

以$Av=\lambda v$且实数$\lambda$、非零实向量$v$定义实特征方向，回用4.2.7.2已经定义的特征多项式说明它对应一个实根。有完整实特征向量基时才可写成$A=S\Lambda S^{-1}$并沿各方向计算幂；重根不自动导致方向缺失，实矩阵也不保证具备全部实特征值。

###### 段：缺少方向与旋转例子

保留只有一条特征方向的二维上三角例子；再用平面直角旋转$R=\left[\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right]$说明实作用可能没有实特征方向，却能直接计算各次幂。不可对角化、没有实特征方向和不可逆是不同性质，分别用核和实际作用检查。

###### 段：用实范数定义幂增长率

对任意实方阵，固定欧氏诱导范数并定义$\rho(A)=\inf_{k\geq1}\|A^k\|_2^{1/k}$，作为渐近幂增长率（谱半径）的实数表述。4.4.1.2证明它等于相应根式序列的极限及其与衰减的联系；当前只建立共同符号，已有完整实特征方向时可沿各方向读取该尺度；实对称矩阵一定存在这类方向的证明由二次极值问题建立，不以“全部实根都存在”为定义前提。

##### 4.2.8.3 幂的计算

把标量多项式代入矩阵，解释Cayley–Hamilton如何让高次幂用有限个低次幂表示。保留二进制反复平方的计算方式与代价；改变乘法顺序可能改变舍入误差，不能只凭乘法次数判断数值可靠性。

###### 段：近似与误差

以矩阵多项式或已有近似因子计算幂时，分别说明截断和因子扰动的来源。利用$A^k-B^k=\sum_{j=0}^{k-1}A^{k-1-j}(A-B)B^j$在相容范数下控制误差，保留非交换次序；运算次数减少不能单独保证更小的浮点误差，长期极限与稳定性仍归4.4.1、4.4.2。

##### 4.2.8.4 指数

用矩阵幂级数定义$e^A$，收敛依据接4.4.1；由同一生成矩阵的乘法规律说明$e^{(s+t)A}=e^{sA}e^{tA}$。一般$e^{A+B}$不能拆成$e^Ae^B$，除非补充可交换等充分条件；线性ODE中的用途在微分方程章展开。

###### 段：基础与近似计算

先以有限Taylor和近似指数，用标量指数尾项及相容范数控制截断。再由$e^A=(e^{A/2^s})^{2^s}$建立缩放与反复平方的精确关系；截断阶数、缩放量和平方次数共同影响实际误差与工作，舍入误差另作核验。

##### 4.2.8.5 平方根、实幂与对数

先从对角矩阵逐项使用实标量函数，区分矩阵函数与对全部系数逐项计算。对一般实对称半正定$A$，平方根的目标是满足$S^2=A$且对称半正定的$S$；严格正定时还可要求实幂和满足$e^L=A$的实对称对数。上述对象的存在唯一性和谱坐标计算在二次极值建立实对称谱后完整证明，此处只说明问题及分支条件。

###### 段：定义域与核验

指数可作用于任意实方阵；本章的实对称平方根限定半正定输入，负幂与对数限定严格正定输入。核验平方根须同时检查对称、半正定与平方残差；仅有$S^2=A$不足以选定要求的根。先用对角例子展示零方向为何阻止负幂和对数，再由后文的正交谱坐标推广。

#### 4.2.9 张量积

由分别线性的联合输入构造产品空间，再计算简单张量与一般张量的坐标。最后讨论哪些结构允许保留因子、延后展开，以及已有近似的误差怎样传递。

##### 4.2.9.1 定义与含义

固定有限维实线性空间 $U,V$，从一个联合输入分别对两端线性的读取出发，说明为何需要把两路输入记录为一个可线性操作的对象。构造 $U\otimes V$及映射 $(u,v)\mapsto u\otimes v$，规定对两端分别满足加法与数乘关系；它不是将两个向量首尾拼接。

###### 段：产品基与维数

给定两组基 $\{e_i\}_{i=1}^m$、$\{f_j\}_{j=1}^n$，以基对 $e_i\otimes f_j$构造有限维空间，并用坐标验证其张成与无关。由此得到 $\dim(U\otimes V)=mn$，与直和的维数相加区分。再证明任意双线性映射 $B:U\times V\to Z$唯一对应线性映射 $\widetilde B:U\otimes V\to Z$，满足 $\widetilde B(u\otimes v)=B(u,v)$；通过有限基展开证明，不要求读者预先掌握范畴语言。

###### 段：多重张量积

将构造推广到多重张量积：输入来自各指定空间，输出保留这些空间的全部槽位。两个一般张量的张量积也只是把两组槽位并置；每个槽位属于哪个原空间或对偶空间须持续标明。

##### 4.2.9.2 基础计算

对 $u=\sum_i u_i e_i$、$v=\sum_j v_jf_j$计算

\[
u\otimes v=\sum_{i,j}u_iv_j(e_i\otimes f_j).
\]

以二维向量示范四个坐标如何产生。一个简单张量的数组坐标可以写成秩一矩阵 $uv^{\top}$，但这张数组的两轴仍分别属于 $U,V$；若要将它解释为输入到输出的线性映射，还需指定对偶槽位或内积识别，不能仅凭矩阵形状自动增加这一角色。

###### 段：简单与一般张量

对一般张量展开到产品基，区分一个简单乘积与简单乘积的有限和。用 $e_1\otimes f_1+e_2\otimes f_2$说明一般元素未必能写成一个 $u\otimes v$。多重产品基产生多索引数组，但数组是选基后的记录，不以轴数或形状替代空间定义。

###### 段：张量与映射

回用4.1.6的对偶，对 $w\otimes\varphi\in W\otimes V^*$规定其作用为 $x\mapsto\varphi(x)w$；由原空间基和对偶基的展开证明 $W\otimes V^*$与有限维线性映射空间之间的一一对应。这里的输入槽位本来就是读取规则，不需要内积；若将一个普通向量放到该槽位，则须先说明用哪个内积把它识别为读取，不能把数组形状相同当作类型相同。

##### 4.2.9.3 性质

由双线性得到对两端分别的分配律及标量移动规则。分别构造 $(U\otimes V)\otimes W$与 $U\otimes(V\otimes W)$之间、$U\otimes V$与 $V\otimes U$之间的自然对应；前者重新加括号，后者交换槽位，不能把交换后的坐标表未经重排就直接判为相等。

###### 段：系数范数

在已指定标准正交产品坐标、以全部系数的欧氏长度计量时，证明 $\|A\otimes B\|_F=\|A\|_F\|B\|_F$。这项等式来自有限求和分离，既不需要SVD，也不自动说明任意自选张量范数具有相同规则。

###### 段：不同乘积的比较

将 $u\otimes v$、同形数组的逐项乘法和有向面积中的 $u\wedge v$放在同一小例中核对输入、输出与交换规则。逐项乘法属于对应元素的乘法任务，楔积属于体积结构；不把三者当作同一种“外积”。

##### 4.2.9.4 高效与近似计算

若要求显式返回全部 $mn$个系数，需输出相应规模的数据；不能仅凭保留两个输入向量就宣称已经产生完整数组。若后续只会使用因子、缩约或某些读取，可以保留已给定的因子形式，延后展开；此时节省的是未被要求显式输出的中间数组。

###### 段：误差传播

若两侧因子已带近似，可由

\[
A\otimes B-\widehat A\otimes\widehat B
=(A-\widehat A)\otimes B
+\widehat A\otimes(B-\widehat B)
\]

配合上述系数范数等式控制误差。这里只传播已有近似的误差，不在这里寻找最佳CP表示或训练因子；那些任务继续由后文明确的预算、误差与目标函数承担。

#### 4.2.10 重排与reshape

固定各轴的含义与索引次序，分别讨论交换轴、改变形状和矩阵展开。它们可以改变后续计算的实现方式，是否改变数学对象则须核对槽位及坐标识别。

##### 4.2.10.1 轴置换

按一个明确置换重新排列槽位及其坐标轴，写出新旧多索引的对应，并用逆置换恢复原记录。轴长度相等也不意味着槽位类型相同，置换时须同步记录每个轴所属空间及输入输出角色。

##### 4.2.10.2 reshape

在总元素数相同、线性遍历次序固定时，改变同一批系数的数组形状，给出可逆的索引双射。若合并或拆分的轴要对应某个新的空间，还需指定产品基识别及其含义；仅有相同元素数不构成几何换基、投影或降维。

##### 4.2.10.3 向量化与矩阵展开

用同一份小数组依次写出列优先向量化、改变形状、交换两轴和按若干轴组成行列的矩阵展开，逐个位置核对去向。先写输入轴的名称、长度及索引，再写输出索引规则；矩阵行列所组合的轴集合也必须明确。

###### 段：逆操作

说明reshape与轴置换通常不是同一操作，先后执行也可能给出不同记录。反向操作必须使用匹配的线性索引和逆置换，才能恢复输入。局部窗口提取另按缩约实例中的索引映射处理，不伪装成可逆reshape。

##### 4.2.10.4 性质

纯重排和等元素数reshape在给定记录之间是可逆的坐标双射，对数组元素的线性叠加可交换，并保持全部元素的 $p$尺度，特别是Frobenius长度。它们不自动保持重新解释后的矩阵秩、谱范数、特征值或新分组下的混合范数。

###### 段：形状与矩阵性质

用 $I_2$展成行向量 $(1,0,0,1)$说明：元素平方和不变，矩阵秩却由2变为1，谱范数由1变为 $\sqrt2$。这是输出对象的行列分组已经改变，不与同一矩阵按可逆行列置换保秩的结论冲突。轴重排还须同步记录对偶类型，不能仅凭轴长相同交换配对含义。

##### 4.2.10.5 实现与代价

在数学层面，它们只重新指定索引，不做近似；显式搬运全部 $N$个元素需要相应规模的读写。能否只改记录而无需搬运，取决于既定存储次序及允许的访问方式，此处不依赖某个软件库，也不承诺reshape或轴置换一律零成本。

###### 段：记录的选择

为后续矩阵乘法或缩约选择展开方式时，比较的是计算路径、中间存储与输出布局。仅改变精确记录不减少信息；若随后截断、量化、聚合或舍弃轴，应另列为产生近似或改变对象的操作，并检验对应误差，不能把收益归给reshape本身。

#### 4.2.11 Kronecker积

把两个映射的联合作用写成产品基下的块矩阵，先建立索引规则，再利用向量化把大矩阵作用改成小矩阵计算。结构近似另作有误差的任务说明。

##### 4.2.11.1 定义与含义

先把它解释为两个线性映射的张量积在产品基下的矩阵记录。若 $A:U\to U'$、$B:V\to V'$，则 $A\otimes B$将 $u\otimes v$送为 $Au\otimes Bv$；由简单张量的张成性扩展为整个张量积空间上的线性作用。

###### 段：尺寸与类型

对于矩阵 $A\in\mathbb R^{m\times n}$、$B\in\mathbb R^{p\times q}$，得到 $A\otimes B\in\mathbb R^{mp\times nq}$。这一段固定输入是两个映射及其矩阵，区别于前面“把两张矩阵本身作为元素相乘形成更高阶张量”的输入类型。

##### 4.2.11.2 基础计算

以块矩阵定义每个 $a_{ij}$缩放一份 $B$，明确索引规则

\[
(A\otimes B)_{(i-1)p+k,\,(j-1)q+\ell}=a_{ij}b_{k\ell}.
\]

给一个小矩阵计算完整块排列，固定产品基及行列次序。回用4.2.10.3的列优先向量化，逐项验证

\[
(A\otimes B)\operatorname{vec}(X)
=\operatorname{vec}(BXA^{\top}),\qquad X\in\mathbb R^{q\times n}.
\]

由同一规则导出 $\operatorname{vec}(CXD)=(D^{\top}\otimes C)\operatorname{vec}(X)$，每次先检查尺寸与向量化约定，不能只背转置位置。

##### 4.2.11.3 性质

在相容尺寸下证明混合乘积规则 $(A\otimes B)(C\otimes D)=(AC)\otimes(BD)$以及转置规则；当两因子都是可逆方阵时，乘回验证其逆为 $A^{-1}\otimes B^{-1}$。如需秩的乘积规则，可用已经建立的基变换与相抵标准块证明，不提前依赖SVD。

###### 段：因子交换

一般 $A\otimes B$与 $B\otimes A$的形状或排列不同，交换因子时须连同输入、输出产品基一起置换，不能把张量积的自然交换对应当作矩阵按现有坐标直接交换。

##### 4.2.11.4 高效与近似计算

当只求作用结果而不要求完整大矩阵时，利用 $BXA^{\top}$执行两次小矩阵乘法，不必显式形成含 $mpnq$个元素的Kronecker矩阵。先算 $BX$约需 $pqn+pnm$次标量乘法，先算 $XA^{\top}$约需 $qnm+pqm$次；选择依赖实际维数，中间数组与输出也须计入。若明确要求输出整个Kronecker矩阵，其输出规模仍不能消失。

###### 段：结构与近似

精确Kronecker结构由题设、构造或已经验证的表示提供。一般大矩阵未必等于一个Kronecker积；用积或积的有限和近似它是另一个优化任务，须报告残差。对已给定近似，可用 $\|(K-\widehat K)x\|\leq\|K-\widehat K\|\|x\|$传播作用误差，不把结构化实现本身当成近似精度保证。

#### 4.2.12 张量缩约

以匹配的槽位配对并求和为共同运算，先建立一般规则，再把迹、注意力与局部窗口作为具体实例。运算本身与它在模型中的参数拟合分别说明。

##### 4.2.12.1 定义与含义

以对偶配对 $\varphi(v)$为最小缩约：输入为 $\varphi\in V^*$与 $v\in V$，输出为一个实数。再在多重张量中选定一个 $V$槽位及一个 $V^*$槽位，用该配对消去它们，保留其他槽位；每缩约一对匹配槽位，张量阶数减少二。单个混合张量内部的匹配槽位也可缩约，矩阵的迹是其重要例子。

###### 段：配对条件

匹配要求由空间类型及配对决定，不能只看两个轴的长度相等。若两槽位均为 $V$而非 $V,V^*$，须先指定内积以把其中一路变为读取；一般坐标内积矩阵为 $G$时得到 $u^{\top}Gv$，只有标准正交坐标下才是直接逐坐标相乘求和。

##### 4.2.12.2 基础计算

先写出自由索引、求和索引及各自范围，再计算有限和。例如 $A\in U\otimes V^*$、$B\in V\otimes W^*$时，缩约中间的 $V^*,V$槽位得到 $C\in U\otimes W^*$，其坐标为

\[
c_{ij}=\sum_k a_{ik}b_{kj}.
\]

这与矩阵复合一致。再以矩阵—向量作用、一个标量多线性读取说明不同槽位匹配产生不同阶数的输出。每个例子都同时给出空间类型、数组尺寸和求和式，不用“沿某个轴求和”替代必要的配对解释。

##### 4.2.12.3 迹与Frobenius配对

回用转置与迹、矩阵内积中已经建立的定义，把迹写为同一线性映射输入输出指标的缩约，把Frobenius配对写为同形数组全部对应指标的乘积求和。逐项核对自由指标、被消去的指标及输出为标量的原因；两例共用缩约记号，却依赖不同的槽位识别。

###### 段：配对与坐标条件

迹使用原空间与对偶空间的自然配对；两个普通向量槽位的Frobenius读取须约定标准正交坐标或指定内积。非正交坐标中不能把简单的同编号求和无条件当作原有几何内积，权矩阵的插入规则回用内积与伴随。

##### 4.2.12.4 性质

用配对和有限和证明缩约对各独立输入分别线性，说明同一张量内部的缩约对该张量线性。正确匹配并同步换基时，原空间与对偶空间的坐标变换相互抵消，输出张量按剩余槽位变换；未经匹配的同长度轴逐项相乘，不具有这一一般结论。

###### 段：次序与非线性

没有非线性节点隔开的有限缩约网络，可由有限和的交换与结合改变计算次序，但所有自由槽位、配对及系数须保持。若中间存在归一化、截断或其他非线性运算，则不能把它们任意移过求和或配对。

##### 4.2.12.5 高效与近似计算

以 $A\in\mathbb R^{m\times n}$、$B\in\mathbb R^{n\times p}$、$C\in\mathbb R^{p\times q}$比较两种精确次序：先算 $AB$再乘 $C$约需 $mnp+mpq$次标量乘法，先算 $BC$再左乘 $A$约需 $npq+mnq$次；中间数组分别为 $m\times p$与 $n\times q$。这些是相应直接计算路径的计数，不声称达到任何问题的最小复杂度。

###### 段：结构化实现

根据维数选择次序，利用已知零项、局部支持和已给定因子，或按块累计结果，均可以避免某些不必要的中间展开。计算量、输出规模与暂存量分别说明；精确实数中的代数等价不保证不同浮点求和次序逐位相同，也不能无依据宣称某一种次序总更稳定。

###### 段：近似边界

若使用截断、采样或低秩替代，必须说明所改的是哪个输入或哪一步、采用什么误差指标及是否仍计算原缩约。基础运算只解释如何应用已给出的结构，近似的求取与训练留给对应任务。

##### 4.2.12.6 注意力中的缩约

以 $Q\in\mathbb R^{n_q\times d}$、$K\in\mathbb R^{n_k\times d}$、$V\in\mathbb R^{n_k\times d_v}$说明注意力中两项不同的计算。特征空间取标准内积时，$S=QK^{\top}$缩约特征轴，得到查询—位置分数；若该空间采用其他内积，需在配对中保留相应权矩阵。

###### 段：值汇集

由分数生成并归一化权重 $P$后，$Y=PV$缩约位置轴，得到 $n_q\times d_v$的输出。固定 $P$时对 $V$线性，权重依赖输入时整体一般非线性；$Q,K$的双线性配对也不等于对联合输入线性。注意力放在缩约的例子中，网络结构、权重学习和训练目标不在这里展开。

##### 4.2.12.7 局部汇集

把局部汇集写成先按索引取窗口、再缩约窗口和通道槽位的复合运算。设一维输入长度为 $L$、输入通道数为 $c$，核宽为 $k$、输出通道数为 $o$，步长为正整数 $s$；给定左、右填充 $p_L,p_R$，约定填充后的取值。输出位置 $t$从0开始，输出通道 $b=1,\ldots,o$，再写

\[
y_{t,b}=\sum_{a=0}^{k-1}\sum_{j=1}^c
w_{a,j,b}\,\widetilde x_{ts+a-p_L,j}.
\]

在填充长度至少为核宽、只保留完整窗口的设定下，输出长度为 $1+\lfloor(L+p_L+p_R-k)/s\rfloor$；若连一个完整窗口都放不下，则输出为空，具体约定须明确。先用一个小窗口逐项核对，再展示窗口矩阵乘法是同一有限和的改写。

###### 段：卷积约定

明确上式采用向前索引的互相关约定；数学卷积常写为 $y_t=\sum_a w_a x_{t-a}$，核翻转与索引偏移要一并核对。窗口展开可能重复输入元素、加入填充值或省略位置，通常不是单纯reshape，不能继承纯重排的可逆性或范数保持结论。

##### 4.2.12.8 多路读取

回用张量积与对偶配对，保留原多路输入的多线性读取例子，说明已给定简单张量或其有限和怎样逐路读取。比较完整参数表与因子表示的系数规模；这里计算已有表示的作用，项数预算、CP拟合任务及最佳逼近是否达到在4.3.5展开，具体非凸训练方法及其收敛条件由最优化章承接。

### 4.3 方程和优化

本节把已知作用与未知对象放进明确的方程或目标函数：先计算子空间中的最近点，再判断线性目标能否精确达到；目标带有曲率、残差或结构限制时，分别研究二次最小化、最小二乘、低秩与映射逼近，最后处理双侧耦合的矩阵未知量。全部向量、矩阵与标量均取实数，转置记为 $A^{\top}$。分解与迭代都在它们实际解决的问题内部建立，先说明存在性、唯一性及所选代表，再给出构造、计算与代价。二次任务以平方展开、正交分解、配方和增量恒等式证明，梯度及积分的正式解释留待微积分后回读；算法的极限与速度在4.4.1分析，数据扰动与有限精度误差在4.4.2分析。

#### 4.3.1 子空间最近点

4.2.4.4给出最近点的正交判据，当前优化问题是从一般方向与目标向量计算最近分量。先逐方向去除已解释的部分，构造标准正交基；把这种构造写成QR形式，再读取投影系数，并据此证明有限维最近分量存在。这样正交化与分解都有明确的输入、输出和用途。

##### 4.3.1.1 基于正交化的方向构造

从候选方向中减去已有正交方向的分量，构造Gram–Schmidt过程。每步残余与先前方向正交，残余为零则表明当前输入方向冗余；保留归纳论证、单位化条件和相关方向的处理，不把正交基作为未说明来源的前提。

###### 段：正交化与Gram矩阵

从候选方向中减去已表示的正交分量，构造Gram–Schmidt正交化；新残余长度为零说明该方向已在已有张成空间中，应跳过该方向且不执行单位化。用两两内积组成的Gram矩阵检查独立性，保留后续QR所需的基构造；浮点计算中的正交性损失留4.4.2讨论。

##### 4.3.1.2 基于QR的最近分量计算

一般基下直接读取系数需要求解Gram系统，而标准正交基可逐个内积读取；因此把基矩阵写成正交列与三角系数的乘积$B=QR$。先由逐列正交化证明形式，再以反射构造适合计算的因子，最后计算$Q(Q^{\top}x)$并验证4.2.4.4给出的最近点判据。

###### 段：正交列与上三角系数

从逐列正交化得到$A=QR$，解释完整QR、经济型QR的形状与适用情况。对满列秩长矩阵，经济型$Q$只有正交列；列秩不足时不能假装方阵$R$可逆。

###### 段：反射与正交化的计算

沿用Householder反射把一列的尾部归零，并说明如何选择符号避免相近数相减。反射可隐式保存，求解时应用反射序列即可，无需显式构造完整$Q$。

###### 段：一般基下的投影系数

对基矩阵$B$推导$B^{\top}(x-Bc)=0$和Gram系数方程；正交基时简化为内积读取。加权内积替换为$B^{\top}M(x-Bc)=0$，并说明可逆性依赖基列独立与权矩阵正定。

###### 段：基于QR的分量读取

对基矩阵做经济型QR，以正交列$Q$计算$Q(Q^{\top}x)$；无需构造整个$QQ^{\top}$即可得到投影结果。比较分解建立、每个新向量的读取及输出工作，说明病态基下显式形成Gram系统可能增加数值损失，误差分析回4.4.2。

##### 4.3.1.3 投影映射与复合

在标准内积下，正交基给出$P=QQ^{\top}$，一般基给出$P=B(B^{\top}B)^{-1}B^{\top}$。从输入输出和正交分量验证$P^2=P$与$P^{\top}=P$；在加权内积下改用相应伴随条件，不能要求普通矩阵转置形式保持不变。

###### 段：正交投影与斜投影

一般幂等作用表示把空间沿其核投到像上，未必使残差正交，也未必得到最近点。正交投影的自伴条件来自所选内积；保留二维斜投影可放大长度的反例，前面的幂运算已按代数方式解释幂等，此处补最近点与计算意义。

###### 段：多个投影的顺序

【补充】通过两个二维子空间的例子说明先后执行两个正交投影通常不同，乘积也未必仍是正交投影。可交换时再检验乘积的幂等与自伴，并说明其像对应交空间；反复投影的极限属于收敛问题，不由一次复合直接保证。

#### 4.3.2 线性方程

【沿用重组】研究 $AX=B$，其中 $A\in\mathbb R^{m\times n}$、$B\in\mathbb R^{m\times s}$已知，$X\in\mathbb R^{n\times s}$未知，$s\geq1$；单个右端 $Ax=b$是逐列的基本情形。先回答相容性、解的自由度与选解，再在同一个方程问题中按可利用的矩阵结构、可访问信息和资源选择三角分解、分块消元、固定校正或Krylov方法。方法的前提与方程本身的可解条件分别陈述，不能由一个算法失败推断问题无解。相容性与选解依据为原正文1601—1645、2100—2134、2175—2271行。

##### 4.3.2.1 目标可达与精确解的自由度

从不同输入可能产生相同输出的例子出发，以值域判断目标可达性，以零空间刻画未被输出识别的自由度。论证相容时全部解构成一个平移后的零空间，唯一性取决于列满秩。

###### 段：四个基本子空间

在标准内积下，由配对恒等式证明$(\operatorname{im}A)^\perp=\ker A^{\top}$和$(\operatorname{im}A^{\top})^\perp=\ker A$。回用已经构造的正交投影，将输入空间分成$\ker A$与$\operatorname{im}A^{\top}$，输出空间分成$\operatorname{im}A$与$\ker A^{\top}$；每端都是正交直和。这些关系分别刻画无法恢复的输入方向与无法达到的输出方向，SVD在后面计算它们的坐标。

###### 段：由值域与左零空间判断相容性

对方程 $Ax=b$说明 $b\in\operatorname{range}A$、$\operatorname{rank}[A\ b]=\operatorname{rank}A$及 $y^{\top}b=0$对全部 $y\in\ker A^{\top}$成立三种等价表述。前两种分别连接几何可达性与消元检验，第三种给出不相容的证明：存在一个读取方向，使全部可达输出读数为零而目标读数非零。

###### 段：仿射解集

有特解 $x_0$时，证明全部解恰为 $x_0+\ker A$，并把这种固定位置加线性方向的集合称为仿射空间，其自由度为 $n-r$。更换特解只改变基点，不改变整个解集；非齐次解集一般不经过零点。用 $A=(1,1)$说明一条输入直线对应同一个输出；欠定且相容必有非零自由度，超定系统也可能相容，不能仅凭方程数判断存在性。

###### 段：多右端下的相容性与共同自由度

把 $X$、$B$按列写成 $x_j$、$b_j$，则 $AX=B$相容当且仅当每个 $b_j\in\operatorname{range}A$，等价于 $\operatorname{rank}[A\ B]=\operatorname{rank}A$，也等价于所有 $y\in\ker A^{\top}$都满足 $y^{\top}B=0$。相容时全部解为 $X_0+N$，其中 $AN=0$，即每列可独立加入 $\ker A$中的向量；解集自由度为 $s(n-r)$，唯一性仍由 $r=n$决定。共享系数允许多个右端复用同一分解，但不同右端的相容性必须分别核验。

##### 4.3.2.2 形状、秩与选解

先用矩阵形状限定可能的秩，再以实际秩和右端位置判断精确解、最小残差与最小范数代表。下表对一列 $b$陈述；多右端逐列使用同一判据，若按Frobenius尺度累计，各列的平方误差与输入平方长度相加。这里先说明所求对象，后面的三角系统、正交变换或迭代都须返回这一对象核对。

###### 段：不同形状与秩下的求解对象

将形状作为可能秩的限制，把相容性与秩作为解的性质的直接依据。用共同表格确定各情形求精确解、最小残差还是最小范数代表，后面的算法都回到这里核对所求对象。

###### 段：满秩与秩亏的情况表

设 $r=\operatorname{rank}A$，先按形状区分满行秩与满列秩，再处理未达到可能最大秩及零矩阵的情形。“列秩亏”取 $r<n$，因此满行秩的宽矩阵也可能有输入自由度，不能把列秩亏等同于未达到可能最大秩。

| 矩阵与右端条件 | 精确方程 | 最小二乘及进一步选解 | 主要计算入口 |
| --- | --- | --- | --- |
| $m=n=r$ | 任意右端存在唯一解 | 最小残差为零，最优输入唯一 | LU；正定时Cholesky；大规模时按结构选迭代 |
| $m>n=r$且 $b\in\operatorname{range}A$ | 存在唯一解 | 最小残差为零，最优输入唯一 | QR；SVD也适用 |
| $m>n=r$且 $b\notin\operatorname{range}A$ | 无精确解 | 最小残差非零，最小二乘输入唯一 | QR；矩形最小二乘迭代 |
| $m=r<n$ | 任意右端都相容，存在无穷多解 | 最小残差为零，最小范数代表唯一 | 对 $A^{\top}$做QR／LQ；SVD；零初始化的适当最小二乘迭代 |
| $0<r<\min(m,n)$且右端相容 | 全部解为 $x_0+\ker A$ | 全部精确解中有唯一最小欧氏范数代表 | SVD或含完整选解步骤的秩揭示分解 |
| $0<r<\min(m,n)$且右端不相容 | 无精确解 | 拟合输出唯一，最优输入不唯一，最小范数代表唯一 | SVD；须核对选解的矩形迭代 |
| $A=0$ | $b=0$时任意输入都是解；否则无解 | 任意输入的残差相同，最小范数代表为零 | 直接判断，避免使用含零分母的公式 |

###### 段：单侧逆能恢复什么

满列秩时存在左逆，可恢复全部输入，但只能对值域中的输出执行精确反演；满行秩时存在右逆，可为每个输出挑选输入，却不能恢复零空间中丢失的信息。说明单侧逆一般不唯一，并将单侧逆的代数公式与实际通过三角求解应用它区分开来。

###### 段：多解与不可达目标下的选择

先固定误差尺度和输入尺度，再选择最小残差、最小范数或允许残差下的输入。不同准则改变的对象不同，不能将它们混称为“方程的解”。

###### 段：精确解中的最小范数代表

相容时按 $x=x_\perp+x_N$分解输入，其中 $x_N\in\ker A$、$x_\perp\perp\ker A$；去掉 $x_N$保留输出并严格减小非零零空间分量造成的范数。以 $x_1+x_2=2$得到 $(1,1)^\top$为例，解释选代表依赖所指定的输入内积，不能默认任意坐标缩放下仍选择同一点。

###### 段：最小残差与残差容限

当目标不可达时，先求距离目标最近的可达输出；若只要求 $\|Ax-b\|\leq\tau$，则先判断容限是否不小于可达到的最小残差，再在可接受集合中添加选解准则。用“所有最优输入可能相同拟合但不同范数”连接后面的伪逆与正则化，说明容限自身不提供噪声大小或参数准确性的证据。

##### 4.3.2.3 基于三角分解的方阵求解

【沿用重组；补充对称不定情形】在方阵求解任务中首次构造LU、Cholesky与$LDL^{\top}$，把因子为什么存在、如何构造及如何用于右端求解连续讲清。先解方阵任务，再在4.3.4处理矩形最小二乘；分解成本、每个新右端的成本与存储分别计数。原正文基础为1647—1693行，并接收原集中分解草稿中属于这些求解方法的构造、证明与边界；$LDL^{\top}$及对称不定求解明确新增。

###### 段：基于消元与LU的求解

从两行方程的消元出发，说明每一步保持解集的行变换怎样累计成 $PA=LU$，使一次全局反求转为两次三角求解。分解构造与右端变换使用同一例子，随后比较矩阵和多个右端共享分解的收益；矩阵改变后不能无条件复用原因子。

###### 段：消元乘子与三角因子的构造

将初等行倍加写成矩阵左作用，逐列记录消去下方元素所用的乘子，解释它们如何进入单位下三角因子 $L$，而剩余系数构成上三角因子 $U$。需要交换行时将置换累计到 $P$，并同步交换前面已记录的乘子；从实际消元过程证明因子乘积确为原置换后的系数矩阵，不只给出分解的名称和形式。

###### 段：部分主元与前代回代

在当前列的剩余元素中选择绝对值最大的可用主元，区分“当前对角元为零但交换后可继续”与“剩余子块失去独立方向”。给出 $Lz=Pb$、$Ux=z$的输入输出与计算次序，并用同一右端逐步复核前代回代。非奇异方阵在精确算术下应有可回代的因子，出现无可用主元则转入秩判断，交换不会把奇异矩阵变成可逆矩阵；某个小主元也不能独自证明精确奇异，浮点阈值决定的数值秩在4.4.2说明。

###### 段：分解复用与稀疏填充

稠密 $n\times n$的LU分解约为 $2n^3/3$次基本浮点运算，每个新右端三角求解为 $O(n^2)$，存储为 $O(n^2)$。稀疏场景解释填充、排序与因子非零结构；“原矩阵稀疏”不足以保证分解存储低，主元增长和舍入影响留到稳定性节。

###### 段：基于Cholesky的正定求解

当 $A=A^{\top}\succ0$时，从消去一个未知量的配方出发构造 $A=LL^{\top}$，证明正对角因子存在且唯一。随后应用因子求解、统计存储，并说明正定条件消失时应怎样重新判断任务；前面的几何节只建立正定关系，不提前教授这项算法。

###### 段：逐步配方与正主元的依据

把第一个坐标与其余坐标分块配方，证明消去首变量后剩余的系数矩阵仍正定，再按维数归纳构造各列。写出 $l_{jj}=\sqrt{a_{jj}-\sum_{k<j}|l_{jk}|^2}$及相应非对角递推，正定性保证开方中的量严格为正；正对角约定逐步确定每一列，从而证明唯一性。这里直接展示剩余矩阵的来源，在4.3.2.4中再将同一消元作用命名为Schur补。

###### 段：正定结构与两次三角求解

应用本处构造的对角与非对角因子，顺次解 $Lz=b$和 $L^{\top}x=z$。非对角因子按 $l_{ij}=(a_{ij}-\sum_{k<j}l_{ik}l_{jk})/l_{jj}$计算，代回 $LL^{\top}$逐项核对原系数；半正定矩阵可能出现零主元，不能直接套同一递推。

###### 段：正定求解的成本与退化边界

稠密实对称正定分解约为 $n^3/3$次运算，只保存一个三角因子；多个右端复用同一因子。将真实半正定、约束造成的零空间和数值误差分开，说明加对角项会改变原方程，只有任务本身明确引入阻尼或惩罚时才采用相应系统。

###### 段：基于LDLᵀ的对称不定求解

【补充】正定条件消失后，对称结构仍能保留，但Cholesky与CG的保证不能沿用。引入带对称置换的 $PAP^{\top}=LDL^{\top}$，其中 $D$可以包含一阶与二阶对角块，服务于后面的等式约束二次方程。

###### 段：对称置换与块主元

由 $\left[\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right]$说明可逆对称矩阵也可能没有可直接使用的一阶对角主元；同时交换行列以保留对称性，选择可逆的一阶或二阶块，消去与剩余变量的耦合，再递归得到 $LDL^{\top}$。用块乘回验证构造，求解依次通过置换、下三角系统、小对角块系统和上三角系统；不定矩阵的负主元不是算法失败，零主元则需另判结构和秩。

###### 段：不定性、奇异性与求解边界

区分“具有负方向”和“具有零空间”：前者仍可唯一求解，后者需重新判断相容性与选解。稠密成本仍为立方量级、三角存储为平方量级；这里只说明结构与求解路径，不承诺无主元算法的数值可靠性，求解相应驻点方程也不等于最小化对应的二次目标。

##### 4.3.2.4 基于分块的求解复用

【沿用重组】以变量分组和矩阵低秩改变为共同问题，研究如何把已有求解工作复用于新任务。先消去一组变量，再处理新增的低维耦合；所有含逆表达式都说明如何通过线性求解实现。依据为原正文1695—1815行。

###### 段：基于Schur补的分块消元

对 $\left[\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right](x,y)^\top=(f,g)^\top$，在 $A$可逆时先反求 $x$再代入第二组方程，得到约化系统。Schur补表示消去内部变量后剩下的有效耦合。

###### 段：约化系统与回代

推导 $S=D-CA^{-1}B$和 $Sy=g-CA^{-1}f$，解释 $A$与 $S$可逆时全系统可逆，以及约化解怎样回代得到原解。通过求 $AZ=B$、$Az=f$来应用 $A^{-1}$，矩阵分块大小决定约化规模，不能为了使用公式先构造整个逆。

###### 段：正定块与规范零空间

对称且 $A\succ0$时用配方证明整块正定等价于 $S\succ0$；若 $A$奇异，说明伪逆版本还需值域包含条件，不能仅把逆替换为伪逆。沿用全局／局部参数的二部残差例子，解释分块消元减少求解规模，而固定参考坐标、真实约束和正阻尼分别改变什么。

###### 段：基于低秩更新的求解复用

当矩阵由 $A$变为 $A+UCV^{\top}$，新增耦合只经过较少中间坐标时，利用原 $A$的求解器和一个小系统处理更新。与低秩逼近区别开来：这里精确改变矩阵，不是近似丢弃信息。

###### 段：Woodbury与小系统可逆性

在 $A,C$和 $C^{-1}+V^{\top}A^{-1}U$可逆的条件下，由块消元推导Woodbury恒等式；再说明 $C=I$时对矩形 $U,V$不要求逆。实现使用若干次原系统求解、少量矩阵乘法和秩规模的小系统；小系统奇异或近奇异时分别涉及可解性与敏感性。

###### 段：秩一更新与行列式更新

用 $k=1$得到Sherman–Morrison公式，明确分母 $1+v^{\top}A^{-1}u\ne0$；以原稿二维数值例子复核更新后的解。说明行列式恒等式在小系统奇异时仍可能成立，求逆公式则不能使用；复用收益取决于已有分解、更新秩及多个右端，成本不能只计小系统。

###### 段：显式矩阵与矩阵作用下的方法选择

比较同一求解任务可以读取整张矩阵、局部行块，或只能调用 $v\mapsto Av$时的计算选择。这是信息条件的变化，不是不同方程目标。

###### 段：按可访问数据选择求解路径

直接分解需要修改或存储因子，分裂迭代需要读取对角／三角或局部块，Krylov方法主要依靠矩阵向量作用。矩形最小二乘还需伴随作用 $u\mapsto A^{\top}u$；只有 $Av$接口时，不能默认伴随同样可用，也不能把所有迭代都概括为无需读取矩阵元素。

###### 段：按总工作比较直接法与迭代法

固定矩阵、多右端、可容忍误差和存储预算，比较分解建立与复用、每次矩阵作用、预条件建立与应用、向量存储和停止条件。直接法与迭代法都可能复用已有计算；本段不依据稀疏性或维数单独宣布某类方法更快，而为后续分类给出可比较口径。

##### 4.3.2.5 基于固定校正的迭代求解

【沿用重组；补充机制名称与分块接口】从可逆方阵的精确任务建立误差递推，说明每轮以相同线性规则校正的定常迭代。这里交代何种更新可合法执行及何时收敛，精确速率与暂态行为放到4.4.1。依据为原正文1817—1892、1905—1910行。

###### 段：基于Richardson校正的定常迭代

对当前残差 $r^{(k)}=b-Ax^{(k)}$，使用 $x^{(k+1)}=x^{(k)}+\omega r^{(k)}$；解释残差位于输出坐标，只有同维方阵的标准坐标设定下才能这样直接加回输入，矩形情形需要伴随或其他搬回映射。

###### 段：误差矩阵与步长的作用

【补充命名】把原稿已有残差更新命名为Richardson迭代，并推导误差矩阵 $I-\omega A$。回用4.2.8.2定义的实矩阵幂增长率 $\rho(C)=\inf_{k\geq1}\|C^k\|_2^{1/k}$，对全部初值收敛需 $\rho(I-\omega A)<1$，完整证明放到4.4.1。本处可直接用 $\|I-\omega A\|_2<1$检验一个充分条件；后面的实对称谱坐标将为SPD矩阵给出完整步长区间 $0<\omega<2/\lambda_{\max}(A)$，并据此计算速率。一般可逆矩阵不保证存在可用的正步长，不能在谱坐标尚未建立时把特征方向当作当前证明前提。

###### 段：一般分裂与预条件校正

写 $A=M-N$且 $M$可逆，得到 $Mx^{(k+1)}=Nx^{(k)}+b$与 $x^{(k+1)}=x^{(k)}+M^{-1}r^{(k)}$。每轮实际求 $Mz=r$而不形成逆；$M$易解与迭代有效需同时考虑，本段建立共同机制，具体对角、三角和块选择在下文实例化。

###### 段：基于Jacobi与Gauss–Seidel的逐行校正

沿用 $A=D-L-U$的符号约定，比较同一轮全部读取旧值和立即读取已更新值两种规则。给出逐行公式与迭代矩阵，再用同一个二阶方程计算一轮，保留可复核过程。

###### 段：旧值并行与新值顺序

Jacobi取 $M=D$，需要非零对角元，各行可同时更新；Gauss–Seidel取 $M=D-L$，按顺序使用新值。说明未知量排序改变后者的迭代矩阵，矩阵稀疏时每轮运算随非零元素数增长，额外向量存储为线性量级，不能把扫描依赖忽略为实现细节。

###### 段：对角占优、正定与分块推广

严格行对角占优保证两法收敛，SPD保证Gauss–Seidel，却不能单凭SPD保证Jacobi，保留原文正定但Jacobi发散的反例。【补充】将单个坐标换为可解变量块得到块Jacobi／块Gauss–Seidel接口，说明块划分改变每轮子问题成本与耦合，收敛仍需检查相应迭代矩阵。

###### 段：基于松弛的SOR校正

在Gauss–Seidel候选更新上按 $\omega$调整幅度，推导SOR的矩阵形式，解释欠松弛、原步与超松弛的实际含义。松弛参数是校正规则的一部分，不能只按数值大小判断快慢。

###### 段：松弛参数与收敛条件

沿用 $\omega=1$退回Gauss–Seidel以及SPD时 $0<\omega<2$收敛的结论；用二次能量中单坐标配方说明条件的作用。该充分条件不推广到任意可逆矩阵，最优参数也依赖矩阵结构；无条件宣称超松弛更快会超出本节保证。

###### 段：定常分裂的用途与停止

比较每轮局部计算、同步与排序代价，说明定常分裂可独立求解，也可成为预条件器中的辅助步骤。停止时复核原方程真实残差，并将残差小与参数准确分开；长期误差收敛、短时放大和速率的统一解释回到4.4.1，误差可信度回到4.4.2。

##### 4.3.2.6 基于Krylov空间的迭代求解

【沿用重组；补充对称不定分支】分解产生过多填充或只提供矩阵作用时，将已计算的 $r_0,Ar_0,\ldots$组合成逐步扩大的校正空间。按正定能量、对称残差和一般残差选择候选，说明“生成空间”与“在空间内优化”是两项共同机制。原正文基础为1894—2092行；MINRES明确新增。

###### 段：基于CG的正定能量求解

对SPD矩阵，用代数配方建立二次目标 $\phi(x)=\tfrac12x^{\top}Ax-b^{\top}x$与方程等价，以及目标差等于能量误差平方的一半。CG在当前仿射Krylov空间中最小化该能量误差，不能据此宣称欧氏残差每一步单调。

###### 段：共轭方向与短递推

沿用方向上的精确一维最小化，解释 $A$共轭使新移动保留旧方向已达到的最优条件，再给出残差、方向与系数递推。正定性保证非零方向的分母为正；零残差立即停止。每步一次矩阵作用、若干内积与向量更新，额外存储 $O(n)$，精确算术有限步终止与有限精度的区别在4.4.1—4.4.2展开。

###### 段：PCG与对称预条件

以SPD预条件器 $M=LL^{\top}$建立对称化系统，说明实现只求 $Mz=r$，初始方向与后续系数都须一致改变。一般 $M^{-1}A$不在标准欧氏内积下对称，不能配任意非对称预条件器而继承CG保证；预条件作用、内积通信和辅助求解均计入每步成本。

###### 段：基于MINRES的对称不定求解

【补充】当矩阵仍实对称但不正定时，沿Krylov空间最小化残差，避免依赖正定能量。主线先取对称非奇异系统，解释Lanczos三对角化怎样将大问题化为逐步更新的小最小二乘。

###### 段：对称结构下的残差最小化

将CG的能量目标改为当前子空间中的原方程残差，说明三对角关系与短递推减少基存储；每轮仍以一次矩阵作用和少量向量更新为主，重正交化会增加实际存储与计算。对称不定性本身不导致不可解，但不能继续使用CG的正分母或能量范数论证。

###### 段：奇异系统与最小范数边界

说明MINRES可扩展到对称奇异系统的最小二乘任务，但一般不保证最小欧氏范数代表；该选解需另核，主线不把MINRES-QLP等变体展开成方法清单。标准预条件保证仍要求SPD预条件器；适用条件依据[Stanford SOL的MINRES说明](https://web.stanford.edu/group/SOL/software/minres/)。

###### 段：基于GMRES的一般方阵求解

对可逆的一般方阵，以Arnoldi过程建立正交Krylov基，再将原残差最小化转成小型最小二乘。相对于前两种方法，放宽对称性要求，但保留方阵、可逆性与原目标的边界。

###### 段：Arnoldi扩基与小问题

沿用 $AV_k=V_{k+1}\overline H_k$和 $\min_y\|\gamma e_1-\overline H_ky\|_2$的推导，说明用QR更新小问题；扩基余量为零时检查当前不变空间内的解并停止扩基，不继续归一化零向量。第 $k$步正交化为 $O(kn)$量级，基存储为 $O(kn)$，每次矩阵作用另计。

###### 段：重启与左右预条件的残差

重启保留当前输入但丢弃部分搜索方向，降低基存储，可能停滞并失去至多 $n$步终止的保证。左预条件最小化变换后的残差，右预条件需将方向映回输入且可保留原残差口径；停止时报告所检验对象。CG、MINRES、GMRES的适用性按矩阵结构选择，梯度更新与Krylov空间生成可能重叠，不宣称这些名称构成互斥分类。

###### 段：多右端下的分解复用与迭代口径

LU、Cholesky、$LDL^{\top}$及分块消元对每列执行相同因子求解，建立因子和应用因子的成本分别累计。对独立右端，定常或Krylov方法可逐列求解并报告各列真实残差，也可在明确的块算法下共同生成候选；不能把逐列实现直接称为块Krylov方法。以 $\|AX-B\|_F$累计停止误差时，仍需防止个别右端的相对误差被其他列的尺度掩盖；预条件建立、矩阵作用、内积通信和存储都按实际列数计入。

#### 4.3.3 二次优化

【沿用重组；补充无约束任务分类】固定目标和可行集合，研究 $q(x)=\tfrac12x^{\top}Hx-g^{\top}x$何时有最小点、最小点是否唯一，以及能否由线性方程求得。先用代数增量处理无约束任务，再由单位球面上的二次极值建立实对称谱坐标，研究方向与子空间约束，最后处理线性等式限制。正定、半正定、负曲率、不可行和无下界是不同条件与结论，不能只给一个驻点方程后宣称任务已经解决。

##### 4.3.3.1 无约束二次函数的最小化

从一维抛物线推广到实向量 $x$，先说明目标中 $H$的反对称部分不贡献二次型，因此一般实矩阵应先取 $H_s=(H+H^{\top})/2$，以下按 $H=H^{\top}$讨论。目标是全空间中的全局最小值，尚未加入单位长度、球内、等式或非负约束；不同可行集合将得到不同答案。

###### 段：代数增量与必要条件

对任意增量 $h$完整展开
$q(x+h)-q(x)=h^{\top}(Hx-g)+\tfrac12h^{\top}Hh$。若 $x$为局部最小点，对任意固定方向分别取正、负小增量，一次项必须为零，因而 $Hx=g$；若存在负二次方向，沿该方向仍可下降，所以还需 $H\succeq0$。反过来，$Hx=g$且 $H\succeq0$使上述增量非负，直接证明全局最优。该论证只用多项式与符号比较，后续微积分才将 $Hx-g$称为梯度。

###### 段：唯一、多解与无下界

当 $H\succ0$时，$Hx=g$有唯一解，由配方得到唯一全局最小点。若 $H\succeq0$且奇异，先利用四个基本子空间判断 $g\in\operatorname{range}H$：相容时任取 $Hx_0=g$，全部最小点为 $x_0+\ker H$，最小值为 $-\tfrac12g^{\top}x_0$且不随所选代表变化；不相容时存在 $v\in\ker H$、$g^{\top}v\ne0$，沿某一符号的 $tv$使目标趋向负无穷。若有 $v^{\top}Hv<0$，二次负项支配一次项，同样无下界。$H=0,g=0$时所有输入都最优；$H=0,g\ne0$时为无下界的线性目标。

###### 段：方程解与最小点的区别

当 $H$不定而可逆时，$Hx=g$仍有唯一解，但该点具有下降方向，不能称为最小点。以 $H=\operatorname{diag}(1,-1),g=0$展示唯一驻点与无下界同时发生；以 $H=\operatorname{diag}(1,0)$分别取 $g=(1,0)^{\top}$和 $g=(1,1)^{\top}$，比较一条最小点直线与零曲率方向上的无界下降。正定任务可复用Cholesky或CG，半正定相容任务先在可识别子空间内选代表，不把求得某个驻点作为任意二次优化的结束条件。

##### 4.3.3.2 单位球面上的二次极值

直接最小化 $x^{\top}Ax$且允许任意尺度时，正半定情形会由零向量给出平凡最小值，负方向则可无限放大。要研究方向本身，改为约束 $\|x\|_2=1$；对一般实 $A$仍先取对称部分。以下先在单位球面上的二次型极值中证明实对称作用存在标准正交特征基，再用所得坐标求最优方向，避免以尚未证明的Rayleigh结论反过来论证谱定理。

###### 段：实对称谱与方向能量

为了分开单位方向中的二次能量，也为后面逐方向开方，证明实对称矩阵可以写成 $A=Q\Lambda Q^{\top}$，其中 $Q^{\top}Q=I$、$\Lambda$为实对角矩阵。单位球面上的二次型由实数逐坐标紧性取得最大值；对最大方向加入任意正交方向并比较正、负小增量，迫使一次交叉项为零，从而得到一个实特征向量。其正交补仍不变，再按维数归纳获得全部实方向。

###### 段：存在极值与代数增量

用第3章的实数有界序列逐坐标抽取子列，说明单位球面上连续二次型的最大值能达到。增量比较只用平方展开，不依赖多元求导或后面的Rayleigh优化理论；取得谱坐标后立即回到单位方向与子空间极值，因而没有把后面的优化结论作为当前证明前提。

###### 段：正交补与归纳

对已取到的单位特征向量$v$，用$x=(v^{\top}x)v+[x-(v^{\top}x)v]$显式分开平行分量与正交分量，说明$v^\perp$的维数少一。对称性保证该正交补在作用下不变，因此可在其中继续归纳；证明不以QR或一般投影算法作为必要前提，而是直接按上述显式分量构造正交补。

###### 段：惯性与谱方向

回到4.1.8.3以最大正、负子空间维数定义的惯性，先说明正特征方向组成的子空间达到对应的正维数；若还有更大的正子空间，它必与非正谱子空间非零相交，和该方向的能量符号矛盾。负方向同理，核恰由零特征方向张成，因此惯性指标分别等于正、负、零谱方向的个数，三者之和为总维数。

###### 段：合同判据的回读

在上述正交谱坐标中，分别缩放正、负特征方向，把二次型化为$\operatorname{diag}(I_{n_+},-I_{n_-},0_{n_0})$，核方向保持为零。相同惯性的矩阵因而具有相同标准坐标表达，完成合同判据的充分性；这一步在谱坐标建立后证明，未被4.1提前当作前提。

###### 段：Rayleigh问题与谱展开

对实对称二次型，固定方向尺度后以Rayleigh商寻找最大或最小作用方向，再由子空间上的极值建立Rayleigh–Ritz及广义特征值问题。代数谱展开承担推导，不预设流形微积分。

###### 段：Rayleigh极值与子空间选取

由正交特征坐标将单位二次型写成特征值的加权平均，得到最大／最小值及达到条件；再通过子空间维数交叠建立极小极大表述。重特征值对应整个最优子空间，方向仅在单特征值时才只差符号地确定，不能把特征值有序当作特征向量唯一。

###### 段：同一二次型在不同约束下的答案

令 $S=(A+A^{\top})/2$，$\mu=\lambda_{\min}(S)$；零维空间与空单位球面单独处理，下表假设维数至少为一。先写清可行集合，再比较最优值与达到条件。

| 任务与条件 | 最小值与最小点 |
| --- | --- |
| $\min_{x\in\mathbb R^n}x^{\top}Ax$，$S\succ0$ | 最小值为 $0$，唯一最小点为 $x=0$ |
| 同一无约束任务，$S\succeq0$但奇异 | 最小值为 $0$，全部最小点为 $\ker S$ |
| 同一无约束任务，存在负二次方向 | 下确界为 $-\infty$，无最小点；包括负定与不定情形 |
| $\min_{\|x\|_2=R}x^{\top}Ax$，$R>0$ | 最小值为 $R^2\mu$，最小点为最小特征子空间中长度为 $R$的向量 |
| $\min_{\|x\|_2\leq R}x^{\top}Ax$，$R>0,\mu<0$ | 最小值为 $R^2\mu$，最小点落在相应负方向与球面上 |
| 同一球内任务，$\mu\geq0$ | 最小值为 $0$，最小点为 $\ker S$与闭球的交；$\mu>0$时仅有零点 |

半径 $R=0$时球面与闭球均只剩零点；负半径时上述范数约束的可行集为空。单位方向的重特征值保留整组最优方向，单特征值也只确定到符号。若另加 $Cx=d$，需使用可行方向上的约化二次型；若另加非负、区间或其他不等式，普通最小特征值公式一般不再成立，完整不等式理论留到最优化章。

###### 段：谱坐标下的平方根、实幂与对数

在正交谱坐标中由二次型符号得到非负或正特征值，逐项开方构造唯一半正定平方根，对严格正特征值定义实幂和唯一实对称对数。零方向阻止负幂和对数，这些是对矩阵作用的函数，不是对元素逐项运算；后面的SVD与极分解回用这里的实谱和平方根。 对 $A\succeq0$构造 $A^{1/2}=Q\operatorname{diag}(\sqrt{\lambda_i})Q^{\top}$；若另有实对称半正定 $T$满足 $T^2=A$，则 $T$与 $A$可交换并保持各特征子空间，在每个特征子空间内再正交对角化 $T$，非负特征值只能取对应的 $\sqrt{\lambda_i}$，由此证明所要求的平方根唯一。对 $A\succ0$用正实数标量函数定义 $A^{\alpha}=Q\operatorname{diag}(\lambda_i^\alpha)Q^{\top}$和 $\log A=Q\operatorname{diag}(\log\lambda_i)Q^{\top}$；实对称对数的唯一性同理由 $\exp$在实数上的单射性得到。运算节已给出的级数与函数定义在这里获得实际谱计算坐标，不重新把任意实方阵称为可实对角化。

###### 段：定义域与实际核验

矩阵指数对任意实方阵定义；本处的半正定平方根限定于实对称半正定矩阵，任意实幂与实对称对数则限定于实对称正定矩阵。核验平方根时同时检查对称、半正定和平方残差，不能仅凭$S^2=A$就认定选到了所要求的根。逆、平方根和对数的扰动响应在4.4.2研究，正式求导与积分公式仍标微积分后回读。

###### 段：基础与近似计算

在已经建立的正交谱坐标中逐项计算，再乘回得到原坐标结果；只需作用于向量时可按所给坐标或多项式实现，避免不必要的完整输出。若实对称矩阵的谱落在指定区间，以区间上标量函数与多项式的最大误差控制矩阵欧氏诱导误差；平方根、负幂和对数分别核验半正定、正定及零方向边界，不把任意实矩阵无条件实对角化。

##### 4.3.3.3 子空间与加权约束下的二次极值

单个单位方向只描述最强或最弱的一个响应；指定多个正交方向或改变方向的长度度量时，任务的可行集合随之改变。回用刚证明的实对称谱，分别处理定维子空间的极小极大、正交列的总二次响应与正定加权约束，每次写出达到条件以及多解的来源。

###### 段：Courant–Fischer与中间特征值

对降序 $\lambda_1\geq\cdots\geq\lambda_d$明确给出 $\lambda_i=\max_{\dim S=i}\min_{x\in S\setminus\{0\}}R_A(x)=\min_{\dim T=d-i+1}\max_{x\in T\setminus\{0\}}R_A(x)$。由任意候选子空间与相应头部／尾部特征子空间必有非零交向量，分别建立上下界，再选特征子空间达到界；不能只用最大最小两个方向替代中间谱的论证。

###### 段：正交列约束下的迹最大与最小

对 $U^{\top}U=I_k$解释 $\operatorname{tr}(U^{\top}AU)$是所选 $k$维子空间的总二次响应，在降序约定下最大值为 $\sum_{i=1}^k\lambda_i$，最小值为 $\sum_{i=d-k+1}^d\lambda_i$。将正交列展开到特征基，得到每个方向权重在 $[0,1]$且权重和为 $k$，通过向大／小特征值转移权重证明极值。严格边界间隙使最优子空间唯一，正交基本身仍可旋转；仅要求每列单位长度会允许重复方向，不能替代列间正交。

###### 段：广义特征与齐次方向估计

在 $x^{\top}Bx=1$、$B\succ0$时变换为普通实对称问题，解释 $Ax=\lambda Bx$中的度量作用；加权正交约束 $U^{\top}BU=I_k$下的迹最大／最小对应最大／最小的 $k$个广义特征值之和。用Cholesky三角求解实施变换，$B$奇异或不定时不直接沿用正定最值。对 $\min_{\|h\|=1}\|Ah\|^2$先对 $A^{\top}A$应用当前实对称谱与单位方向极值；其零方向恰为 $\ker A$，宽矩阵的完整右零空间不能遗漏。后面的SVD会把这些方向解释为最弱右奇异方向；坐标归一化若未同步改变约束和误差，可能改变含噪任务。

###### 段：基于重复作用的方向估计

【补充基础算法】只提供实对称矩阵作用 $v\mapsto Av$时，从非零初始向量单位化开始，逐轮计算 $w_k=Av_k$、$v_{k+1}=w_k/\|w_k\|_2$；若 $w_k=0$，说明当前方向已落在核中，应按零特征方向处理，不能继续除零。每轮一次矩阵作用、一次长度读取与向量缩放，另以 $\theta_k=v_k^{\top}Av_k$和真实残差 $Av_k-\theta_kv_k$检验候选。普通幂迭代针对的是绝对值较大的谱方向，并不自动求最大代数特征值或最小二次能量；负的主导值可造成符号交替，绝对值并列或初值缺少目标分量时需另判极限。若专门求代数最大／最小方向，可用已知界 $\beta\geq\|A\|_2$把作用改为 $A+\beta I$或 $\beta I-A$，但仍需目标分离及非零初始投影；变换后的归一化同样检查非零，若整个变换作用为零则所有方向并列最优。分离、初值、重复谱与残差能证明到哪里，由4.4.1.6的谱方向收敛分析接续，不由一次归一化保证。

###### 段：基于实移位求解的近谱方向估计

【补充基础算法】对当前实对称矩阵 $A$，若希望寻找靠近指定实数 $\mu$的方向，先检查 $A-\mu I$可逆，再固定该移位重复求解 $(A-\mu I)w_k=v_k$并单位化。其机制是在相同特征坐标中把作用尺度改为 $(\lambda_i-\mu)^{-1}$，因此需要最近方向的分离与初值条件，不能仅说“取一个移位就收敛到目标”。固定移位可复用LU或对称 $LDL^{\top}$因子；每轮成本包括三角求解、归一化及残差核验，因子建立与存储另计。移位恰落在特征值上时系统奇异，原公式失效；接近目标时系统可能敏感，内部线性求解的精度会影响外部方向估计。只调用 $Av$尚不足以免费执行移位反求，若内层采用迭代，还须报告其真实残差与工作。

###### 段：基于子空间投影的谱方向提取

【补充基础算法】对实对称 $A$，沿 $v,Av,A^2v,\ldots$扩展标准正交基 $V_k$，先选 $v\ne0$并令 $v_1=v/\|v\|_2$，设 $v_0=0,\beta_0=0$，在第 $j$步依次计算 $w=Av_j-\beta_{j-1}v_{j-1}$、$\alpha_j=v_j^{\top}w$、$w\leftarrow w-\alpha_jv_j$、$\beta_j=\|w\|_2$，非零时令 $v_{j+1}=w/\beta_j$。这一Lanczos递推在精确算术下得到小型实对称三对角矩阵 $T_k=V_k^{\top}AV_k$；从 $T_ky=\theta y$、$\|y\|_2=1$提取近似方向 $x=V_ky$，这就是在当前子空间中执行前面已经建立的二次极值。若扩展残余为零，则当前空间已不变，停止扩基并求解其中的小问题；不能再归一化零向量。精确短递推每步以一次矩阵作用和少量向量更新为主，保存全部基以重建多个方向需 $O(nk)$存储，重正交化增加工作；只保存少量递推向量时，后续重建必须另计保存或重新生成的成本。用原作用计算 $Ax-\theta x$，不要把小问题求得精确等同于原问题已有精确方向；谱间隙、初值分量和浮点正交性损失的分析分别接4.4.1.6、4.4.2.3与4.4.2.5。一般方阵的Arnoldi扩基已在方程求解中建立，这里利用对称性取得实对称投影，不提前假定一般实矩阵均有实特征方向。

##### 4.3.3.4 线性等式约束下的二次最小化

【补充】以 $\min_x\tfrac12x^{\top}Hx-g^{\top}x$且 $Cx=d$为任务，先判断约束相容性，再沿可行方向研究目标。该问题将正定能量、零空间和分块方程结合起来，不引入尚未学习的一般非线性最优性条件。

###### 段：仿射组合与凸组合

对满足同一等式$Cx=d$的可行点，证明系数和为一的仿射组合仍满足该约束。若系数进一步非负，就得到保留这些等式的凸组合；额外的不等式约束是否保留须核验其具体条件。这里解释可行集合的结构，一般凸集及凸优化理论由第7章展开。

###### 段：零空间消元与可行方向配方

找一个可行点 $x_p$和 $\ker C$的一组基 $Z$，令 $x=x_p+Zz$，用配方把任务化为 $\tfrac12z^{\top}Kz-\ell^{\top}z$加常数，其中 $K=Z^{\top}HZ$、$\ell=Z^{\top}(g-Hx_p)$。$H$在 $\ker C$上正定时可行最优解唯一；判断依据是可行方向上的约化矩阵，不能只检查 $H$是否可逆。

###### 段：可行方向上的有界与无界

若存在 $v$使 $v^{\top}Kv<0$，沿 $z=tv$的二次项趋向负无穷，任务无下界。若 $K\succeq0$但奇异，最小点存在当且仅当 $\ell\in\operatorname{range}K$；条件不满足时零曲率方向上的一次项使目标无界，条件满足时，先取任一 $Kz_0=\ell$的解，全部约化最优解为 $z_0+\ker K$；到4.3.4.3几何构造伪逆后，同一集合也可写为 $K^\dagger\ell+\ker K$，此处的存在与最优性不依赖该后续记号。约化矩阵正定时唯一，奇异且有最小点时保留自由度；没有可行点时则先判为不可行，不能混入无界情形。

###### 段：分块驻点方程与KKT接口

对实对称 $H$、满行秩 $C$，在 $H$对 $\ker C$正定时建立 $\left[\begin{smallmatrix}H&C^{\top}\\C&0\end{smallmatrix}\right](x,\nu)^\top=(g,d)^\top$的唯一求解与全局最优性；乘子只是使线性项在可行方向上消失的系数。系数矩阵通常对称不定，可调用 $LDL^{\top}$、分块消元或MINRES，不套Cholesky／CG；只标明与后续KKT条件的联系，不在这里展开完整理论。

#### 4.3.4 最小二乘

【沿用重组】研究 $\min_X\|AX-B\|_F^2$，单列形式为 $\min_x\|Ax-b\|_2^2$。Frobenius平方误差等于各列平方误差之和，因此在无跨列约束时可逐列寻找最近可达输出，再在输入零空间的正交补中选择代表；输出拟合唯一与系数唯一必须分开说明。接着按秩与可访问信息选择QR、SVD或只调用正向／转置作用的迭代；加入输出权重、输入惩罚或残差容限时重新说明任务改变了什么。最优目标不保证不同初始化、预条件和停止点选择同一个输入。原正文依据为2094—2334、2492—2554、2627—2740、3570—3675行。

##### 4.3.4.1 最近可达输出与最优输入

把 $\min_x\|Ax-b\|_2^2$解释为寻找最近的可达输出。有限维列空间闭，正交投影使拟合输出存在且唯一；输入唯一还需要零空间平凡。

###### 段：正规方程与代数最优性

由最优残差与列空间正交得到 $A^{\top}(b-A\widehat x)=0$，再展开任意增量 $h$下的平方误差，证明交叉项消失且剩余项为 $\|Ah\|_2^2\geq0$。用这一完整恒等式证明正规方程必要且充分，不依赖尚未介绍的多元微分；精确解只是最小残差为零的特殊情形。

###### 段：拟合唯一与系数不唯一

满列秩时 $A^{\top}A\succ0$，最小二乘输入唯一；否则所有最优输入相差零空间向量。沿用近共线例子，使读者看到零残差可与巨大系数并存，秩改变时精确插值也可能消失；这里只确定所求对象，敏感程度在4.4.2量化。

###### 段：多右端的平方误差与正规条件

写 $B=[b_1,\ldots,b_s]$、$X=[x_1,\ldots,x_s]$，由 $\|AX-B\|_F^2=\sum_j\|Ax_j-b_j\|_2^2$，逐列最优当且仅当 $A^{\top}(AX-B)=0$。最优拟合矩阵由各列的唯一正交投影组成，输入矩阵唯一当且仅当 $A$满列秩。以Frobenius内积展开矩阵增量得到同一个非负剩余项 $\|AH\|_F^2$；若目标另含跨列耦合或结构约束，就不能把独立逐列求解当作完整答案。

##### 4.3.4.2 加权残差的最小化

当输出坐标量纲或可信程度不同，以正定权重 $W$建立 $\|Ax-b\|_W^2=(Ax-b)^{\top}W(Ax-b)$。改变残差度量会改变最优拟合，不能自动当作只改求解实现。

###### 段：加权正交与白化求解

推导 $A^{\top}W(A\widehat x-b)=0$，再用 $W=C^{\top}C$将任务化为对 $(CA,Cb)$的普通最小二乘，沿用QR或矩形迭代。固定 $W\succ0$时输入唯一仍由列满秩决定；应用 $C$的成本和结构必须计入，不能默认稠密权重免费可用。

###### 段：半正定权重与输入尺度

当 $W\succeq0$但不正定时，非零残差可能被完全忽略，连原输出中的最优拟合也未必唯一；保留 $A=I$、$W=\operatorname{diag}(1,0)$的反例。若输入范数也加权，最小范数代表应使用对应正交补，不直接套标准伪逆；输出加权、变量缩放与预条件分别交代其是否改变任务。

###### 段：多输出权重与误差累计

公共输出权重 $W\succ0$时，矩阵目标为 $\sum_j(Ax_j-b_j)^{\top}W(Ax_j-b_j)=\operatorname{tr}((AX-B)^{\top}W(AX-B))$，仍可逐列白化并共享变换后的系数。不同列使用不同权重时分别检查条件，不能无条件共享同一分解；若权重还耦合不同右端，则先在整个矩阵空间中写清新的二次型，避免把一个更改了误差的任务简化为原来的Frobenius最小二乘。

##### 4.3.4.3 基于伪逆的两次正交选择

先把 $b$投影到 $R=\operatorname{range}A$，再由 $A|_{(\ker A)^\perp}$的逆恢复唯一的零空间正交补输入，构造 $A^\dagger$。由此理解伪逆，而非先背诵分解公式。

###### 段：Penrose条件与全部最优输入

沿用 $AA^\dagger=P_R$、$A^\dagger A=P_{(\ker A)^\perp}$及四个Penrose条件，说明其唯一性。全部最小二乘解为 $A^\dagger b+\ker A$，其中 $A^\dagger b$唯一最小范数；保留“先选最近输出，再选最小输入”的二阶例子，不暗示伪逆恢复了零空间信息。

###### 段：满秩公式与秩改变边界

满列秩由正规方程给出 $(A^{\top}A)^{-1}A^{\top}$，满行秩由行空间中的精确恢复给出 $A^{\top}(AA^{\top})^{-1}$；一般秩的伪逆继续使用本节已经完成的几何构造，其SVD计算公式在4.3.4.5首次构造奇异方向后导出。说明这些是映射表达式，实际用分解与求解应用；伪逆在秩改变处未必连续，截断阈值意味着另一个选解或近似任务，稳定性条件归入4.4.2。

###### 段：任意秩下的全部矩阵最优输入

对多右端得到全部最小二乘解 $X=A^\dagger B+(I-A^\dagger A)Z$，其中 $Z\in\mathbb R^{n\times s}$任意；括号内为输入零空间的正交投影。最小Frobenius范数代表唯一且为 $A^\dagger B$，因为各列的零空间分量与已选行空间分量正交；若输入尺度或跨列度量改变，须在对应内积下重新选代表。这一结论先由几何构造完成，SVD只负责后面的可计算坐标。

##### 4.3.4.4 基于QR的最小二乘求解

对满列秩矩阵用正交变换保留残差长度；回用4.3.1.2为投影计算构造的QR与Householder反射，在当前秩判断问题中再补列置换，展开从因子得到指定最优输入的过程。欠定问题需要在行空间内选解，秩亏问题需要额外处理，不能把全部情况都送入同一个可逆三角系统。

###### 段：满列秩QR与宽矩阵的最小范数求解

满列秩 $m\geq n$时，由 $A=QR$将任务化为 $Rx=Q^{\top}b$，不可消除的正交残差单独保留；Householder反射以向量形式存储并作用于右端，稠密分解成本为 $O(mn^2)$。宽矩阵满行秩时对 $A^{\top}$做QR或回用LQ，先在行空间内求解，再将行空间坐标映回原输入，不用任意自由变量零置换冒充最小范数。

###### 段：列置换、秩揭示与QR的选解边界

在这里首次引入带列置换的 $A\Pi=QR$：每轮从剩余列的正交残余中选择主元候选，交换到当前列，累计置换$\Pi$并继续更新三角块，由此记录独立列和依赖列。数值秩需要结合阈值，普通无主元QR的单个小对角元不是全部秩信息。奇异三角因子不能直接回代，任意基本解也未必最小范数，需要补充正交处理或使用下一小节构造的SVD。QR避免显式形成 $A^{\top}A$，仍不能消除原问题的近相关方向敏感性。

##### 4.3.4.5 基于SVD的任意秩选解

【沿用迁入】满秩三角系统不再适用时，需要同时读出哪些输入方向被消去、哪些输出方向无法达到，以及非零方向怎样逐一反求。以这一求解问题首次引入奇异值分解，完整接收原集中分解草稿中奇异值表示的构造、形状、四个子空间与非唯一性材料；低秩截断和核范数优化不在这里提前展开。

###### 段：由非负方向能量构造奇异方向

回用4.3.3.2为单位球面上二次极值建立的实对称谱定理，对 $A^{\top}A$取标准正交特征基；由 $x^{\top}A^{\top}Ax=\|Ax\|_2^2\geq0$说明谱非负，定义 $\sigma_i=\sqrt{\lambda_i}$。正值方向令 $u_i=Av_i/\sigma_i$，逐对验证这些输出向量正交归一；零值方向由 $\ker(A^{\top}A)=\ker A$保证确实被消去。补齐输出正交基后从全部输入基向量的作用证明 $A=U\Sigma V^{\top}$，构造只需已经完成的实对称谱证明与正交补基，随后才用所得奇异坐标执行任意秩选解。

###### 段：完整、经济与紧致形式中的零方向

设 $A\in\mathbb R^{m\times n}$、$q=\min(m,n)$、$r=\operatorname{rank}A$。完整形式为 $U\in\mathbb R^{m\times m}$、$\Sigma\in\mathbb R^{m\times n}$、$V\in\mathbb R^{n\times n}$；经济形式取两侧 $q$列与 $q\times q$对角块，仍可能包含零奇异值；紧致形式只保留 $r$个正值方向。三种形式都精确表示同一矩阵，尚未截断近似；分别指出何种零空间信息需由补基恢复，$r=0$用空和处理，不能除以零奇异值。

###### 段：四个子空间与任意秩反求

用右正值方向张成 $\operatorname{range}A^{\top}$、右零方向张成 $\ker A$，用左正值方向张成 $\operatorname{range}A$、剩余左方向张成 $\ker A^{\top}$，将4.3.2.1已证明的正交互补关系落实为可计算坐标。将 $b$分成可达输出和不可达残差，再得到 $A^\dagger b=\sum_{i=1}^r\sigma_i^{-1}v_i u_i^{\top}b$；一般最小二乘解加任意右零空间分量，取零分量得到本章先前几何定义的唯一最小范数代表。

###### 段：重复奇异值与因子非唯一

有序奇异值由 $A^{\top}A$的谱唯一确定，重复正奇异值的左右基可以同步旋转，零空间的补基也不唯一。证明这些改变不影响矩阵作用、伪逆及完整目标子空间；单个方向是否可辨认和随扰动是否可靠则留4.4.2。保留“方向基不唯一”与“最优输入不唯一”并非同一结论的区别。

###### 段：由奇异方向读取范数与计算代价

在此由 $\|Ax\|_2^2=\sum_i\sigma_i^2|v_i^{\top}x|^2$证明4.2.5.2按定义建立的欧氏诱导范数等于 $\sigma_1$，由正交不变的元素平方和得到 $\|A\|_F^2=\sum_i\sigma_i^2$，零矩阵分别取零。区分用 $A^{\top}A$作存在性推导与显式形成Gram矩阵计算小奇异值：后者会增加数值损失，可靠计算路径及成本在4.4.2评估；主夹角的SVD公式进入4.4.2.5的方向比较，Schatten与核范数进入4.3.5.1的矩阵逼近。

##### 4.3.4.6 基于转置作用的迭代求解

只需矩阵作用而不宜形成因子时，对同一个最小二乘目标比较固定伴随残差校正与逐步扩大的Krylov候选。Landweber、CGLS与LSQR都需要正向及转置作用；分别说明初始化、零空间分量、步长或短递推如何影响所选输入，不以“不形成正规矩阵”替代完整条件。

###### 段：基于伴随残差的Landweber更新

沿用 $x^{(k+1)}=x^{(k)}+\eta A^{\top}(b-Ax^{(k)})$，将其作为直接残差校正，或对应目标 $\tfrac12\|Ax-b\|_2^2$的更新。先从这一半平方误差的增量一次项识别校正方向，再在后续微积分章节解释为步长 $\eta$的梯度下降；若目标写成不带 $\tfrac12$的平方误差，梯度会多一个因子 $2$，不能沿用同一“梯度步长”名称而漏改公式。输出残差通过伴随搬回输入，不是通过逆映射；矩阵右端按列更新即 $X^{(k+1)}=X^{(k)}+\eta A^{\top}(B-AX^{(k)})$。

###### 段：步长、每步工作与选解

【补充命名】将现有固定步长最小二乘梯度更新标明为Landweber型迭代。非零 $A$下 $0<\eta<2/\|A\|_2^2$给出上述直接校正的收敛范围；单右端时每轮一次 $A$与一次 $A^{\top}$作用，稀疏存储下为 $O(\operatorname{nnz}A)$量级，向量存储为 $O(m+n)$；$s$列右端的直接逐列实现把相应作用与向量存储按 $s$累计，分块实现则另列实际工作与中间存储，不形成Gram矩阵。

###### 段：零空间初值与停止误差

更新始终位于 $\operatorname{range}A^{\top}$，故保留初值的零空间分量；零初值选择最小范数最小二乘解，非零初值的极限需加入零空间投影。$A=0$单独处理，步长端点可能振荡；极限与速率的证明放到4.4.1。迭代停止带来的近似不能直接解释为恢复无噪参数，真实残差与正规方程残差在4.4.2配合判断。

###### 段：基于CGLS与LSQR的矩形Krylov求解

【补充】当逐步沿当前校正方向速度不足时，利用 $A$与 $A^{\top}$反复作用生成更丰富的候选。先以CGLS说明正规方程的Krylov思路，再以LSQR说明双对角化怎样在不显式构造Gram矩阵的情况下实现相同最小二乘任务。

###### 段：CGLS与正规方程的隐式作用

将CG用于 $A^{\top}Ax=A^{\top}b$，通过先算 $Ap$再算 $A^{\top}(Ap)$实现作用；满列秩时对应SPD正规方程，列秩亏时须把迭代限制在可识别的行空间并核对零空间初值。精确算术的等价不等于有限精度行为相同，避免形成 $A^{\top}A$可省去存储与一项舍入损失，却不取消正奇异值平方进入正规算子的问题。

###### 段：LSQR双对角化与最小范数边界

通过Golub–Kahan双对角化将问题化为小型最小二乘，并用短递推更新候选；适用于任意形状与秩，调用 $Av$和 $A^{\top}u$，无重正交化时只需保存少量输入／输出向量。标准零初始化、无阻尼的精确任务得到最小范数最小二乘解；阻尼、右预条件或变量缩放需重新说明所选择的范数，有限停止精度也需报告。适用性依据[Stanford SOL的LSQR说明](https://web.stanford.edu/group/SOL/software/lsqr/)。

##### 4.3.4.7 二次惩罚下的正则化求解

从未被观测约束或易被放大的输入方向进入 $\min_x\|Ax-b\|_2^2+\lambda\|Lx\|_2^2$。$L$决定压小何种变化，$\lambda>0$决定拟合与惩罚的权衡；二者属于任务定义。

###### 段：岭与一般Tikhonov的唯一性

用增量展开推导 $(A^{\top}A+\lambda L^{\top}L)x=A^{\top}b$；解唯一当且仅当 $\ker A\cap\ker L=\{0\}$，因为二次型在方向 $v$上为 $\|Av\|^2+\lambda\|Lv\|^2$。岭取 $L=I$自动保证唯一，一阶差分惩罚则可能保留常量歧义；正则化不能恢复同时未被观测和惩罚识别的方向。

###### 段：增广最小二乘与求解器选择

写成 $[A;\sqrt\lambda L]$与 $[b;0]$的最小二乘，允许QR／SVD或LSQR；公共零空间为零时正规系统正定，可用Cholesky／PCG。分别说明显式构造正规矩阵与仅调用 $A,A^{\top},L,L^{\top}$的工作量；一般 $L$不共享 $A$的奇异方向，不能直接套岭的逐奇异值收缩公式。

###### 段：正则化任务与误差分析的边界

本处从原稳定性材料迁入的是正则化目标、唯一性与求解路径；任务已经改变后，偏差、误差放大与参数选择的可信程度在4.4.2继续分析。线性等式约束的二次任务已经由可行方向与分块线性系统处理；一般非线性约束、完整KKT理论与通用优化算法仍由最优化章建立。

##### 4.3.4.8 残差约束下的输入选择

当观测误差容限来自任务外的知识时，研究残差不超过 $\tau$的候选中惩罚最小者。将“残差越小”与“已拟合到足够精度”分开，并说明惩罚形式与残差约束形式何时有关联。

###### 段：残差容限与差异原则

先检查约束可行性，再比较正则化参数增大时残差不减、惩罚不增的关系；证明来自把两个最优点代入对方目标。参数选择可用残差夹逼和二分，但容限必须落在可达到的范围内，端点可能仅由参数极限取得，噪声尺度不能从当前残差本身推断。

###### 段：惩罚任务与约束任务的条件关系

给定正参数的最优解，也最小化其自身残差容限内的惩罚；由任意约束任务反求正参数则需约束活跃和正乘子等额外条件。本节只用目标比较说明这一方向，并记录哪些条件留到最优化章建立，不把等号残差约束无条件改成某个正参数目标。

#### 4.3.5 低秩与映射逼近

【沿用重组】普通最小二乘允许所有输入方向或矩阵系数变化，当前任务进一步限制子空间维数、矩阵秩、长度保持或定向。前面的二次优化已经解决方向尺度与正交列的极值；这里固定谱范数或Frobenius误差，再回用SVD与实对称平方根求低秩和正交映射近似。最优误差值、最佳对象、因子表示的唯一性以及实际计算代价分别说明，不把有限步最优解混同为迭代收敛或方向稳定。原正文依据为2605—3317行。

##### 4.3.5.1 秩与子空间预算下的逼近

固定谱范数或Frobenius范数误差，回用4.3.4.5已经为任意秩选解构造的SVD，用截断求低秩矩阵近似，再将其解释为子空间投影与数据重构。为比较不同保留谱的规模和建立核范数惩罚，在当前逼近任务中引入Schatten尺度、对偶与奇异值配对；先说明最佳值及其条件，再讲如何按预算或容许误差反求秩。

###### 段：Schatten尺度与核范数

对已经建立的非负奇异值取 $p$范数，定义 $\|A\|_{S_p}=(\sum_i\sigma_i^p)^{1/p}$，$1\leq p<\infty$，并令 $\|A\|_{S_\infty}=\sigma_1$；$p=1$为核范数，$p=2$和 $p=\infty$分别回到Frobenius与谱范数。说明左右正交变换不改变这些尺度，固定秩 $r$时有 $\|A\|_2\leq\|A\|_F\leq\sqrt r\|A\|_2$、$\|A\|_F\leq\|A\|_*\leq\sqrt r\|A\|_F$；零矩阵直接处理。4.2.5.1的混合（分组）范数按行列分组，本处尺度按奇异值分组，不混用其不变性与乘法估计。

###### 段：奇异值配对、对偶与范数论证

为控制矩阵逼近中的配对项，保留 $|\operatorname{tr}(B^{\top}A)|\leq\sum_i\sigma_i(A)\sigma_i(B)$的论证；先补齐相同长度的非负谱，再通过奇异基间的权重和重排建立上界。结合标量Hölder并选择相同左右奇异方向达到界，证明共轭指数 $1/p+1/q=1$时 $\|A\|_{S_p}=\sup_{\|B\|_{S_q}\leq1}|\operatorname{tr}(B^{\top}A)|$，包括端点情形。由配对上确界证明三角不等式，正定性和齐次性由奇异值验证；核范数与谱范数对偶将用于后面的因子下界及软阈值最优性，不能只给名称后直接使用。

###### 段：两种误差下的最佳秩约束逼近

令 $r=\operatorname{rank}A$，对 $0\leq k<r$分别给出谱范数最低误差 $\sigma_{k+1}$和Frobenius范数最低误差 $(\sum_{j>k}\sigma_j^2)^{1/2}$，通过维数交叠与正交展开建立Eckart–Young–Mirsky最优性，$k\geq r$时最低误差为零。前者控制最坏单位输入的输出误差，后者累计正交输入方向的平方误差；带权或逐元素误差不自动继承截断最优性。

###### 段：最佳矩阵唯一性与谱误差反例

Frobenius目标在 $1\leq k<r$且 $\sigma_k>\sigma_{k+1}$时的最佳矩阵唯一：严格谱隙确定保留子空间，正交分解中剩余平方项为零确定投影结果；边界相等时可能存在多个最佳矩阵。谱范数目标即使有严格谱隙也未必唯一：对 $A=\operatorname{diag}(2,0.4)$，全部 $\operatorname{diag}(2+t,0)$、$|t|\leq0.4$都是秩一候选，谱误差均为 $0.4$。最优误差值、最佳矩阵与其因子表示的唯一性分别说明。

###### 段：中心化数据的PCA重构

对按行排列且已中心化的数据 $X$，用 $\|X-XUU^{\top}\|_F^2=\|X\|_F^2-\operatorname{tr}(U^{\top}X^{\top}XU)$、$U^{\top}U=I_k$，将最佳子空间重构转成迹最大化，解释前 $k$个右奇异方向与PCA。样本数 $N\geq2$时以 $1/(N-1)$归一化连接保留样本方差，中心化、恢复均值与不同量纲是否标准化均须说明；最大样本方差不自动保证预测价值或总体统计结论。

###### 段：由误差容限反求最小整数秩

令 $\sigma_{r+1}=0$、$\tau\geq0$，明确 $k_2(\tau)=\min\{k\in\{0,\ldots,r\}:\sigma_{k+1}\leq\tau\}=\#\{i:\sigma_i>\tau\}$，以及 $k_F(\tau)=\min\{k\in\{0,\ldots,r\}:\sum_{i>k}\sigma_i^2\leq\tau^2\}$。以低秩误差下界排除所有更小秩，再用截断达到所求整数；阈值恰等于某奇异值时允许舍弃该方向，所以计数用严格大于。沿用谱 $(8,3,1,0.2)$、$\tau=1$在两种误差下分别需要秩 $2$与 $3$的例子，保留 $\tau=0$、秩零、负容限不可行和零矩阵的边界；相对容限乘以对应范数后再计算。

###### 段：核范数的因子化与平衡因子

对任意 $q\geq\operatorname{rank}B$，保留 $\|B\|_*=\min_{U\in\mathbb R^{m\times q},\,V\in\mathbb R^{n\times q},\,UV^{\top}=B}\tfrac12(\|U\|_F^2+\|V\|_F^2)$。由SVD把每个奇异值的平方根分配给两侧构造达到上界的平衡因子，再用Frobenius的Cauchy–Schwarz和 $2ab\leq a^2+b^2$建立下界；$q<\operatorname{rank}B$时精确因子约束不可行。乘积不变的两侧逆向缩放通常改变因子惩罚，因子联合目标仍非凸，恒等式不保证任意交替或梯度算法得到全局最优。

###### 段：硬秩约束、核范数与连续规模

对 $\lambda\geq0$，在 $\tfrac12\|A-B\|_F^2+\lambda\|B\|_*$中用奇异值配对将任务化为非负标量收缩，得到 $(\sigma_i-\lambda)_+$，与仅保留原值的截断区分。稳定秩、熵型有效秩和给定误差阈值的最小整数秩回答不同问题；只在同一尺度和归一化下比较，不能将连续规模替代代数秩。因子存储与作用的工作为 $O((m+n)k)$量级，分解建立成本另计；只有 $k$相对两端维数足够小时才节省资源，小奇异方向的真实信息仍需在4.4.2结合数据精度判断。

###### 段：多路张量的秩预算与逼近

回用4.2.9已经建立的张量积，在多路近似任务中用若干简单张量之和构造CP表示，以最少项数定义相应张量秩。比较完整系数表与各轴因子的参数规模，说明缩放和因子重排造成的非唯一；高阶情形不能直接继承矩阵SVD的正交方向和最佳截断定理，给定项数的最佳近似还可能不达到。这样因子表示在明确的预算与误差任务中引出，不把CP当成张量本身的定义。

##### 4.3.5.2 正交与定向约束下的映射逼近

未知量受保持长度或保持定向的限制时，回用已建立的奇异方向和平方根，将作用的伸缩与方向变换分开，再利用迹配对求最近映射。极分解在这里为这项具体逼近任务首次构造；该约束改变可行集合，不把普通矩阵最小二乘直接搬到正交矩阵集合。

###### 段：由SVD构造极分解

设紧致SVD为 $A=U_r\Sigma_rV_r^{\top}$，取 $H=V_r\Sigma_rV_r^{\top}=(A^{\top}A)^{1/2}$、$Q=U_rV_r^{\top}$，逐项验证 $A=QH$。对 $m\times n$矩阵，$Q$也为 $m\times n$，在 $\ker A$上取零，且 $Q^{\top}Q$、$QQ^{\top}$分别投影到 $\operatorname{range}A^{\top}$与 $\operatorname{range}A$；所以它在有效输入子空间保持长度，称为部分等距映射。保留非负平方根唯一性，并说明秩亏时这一规范的部分等距选择与后面的完整延拓不是同一对象。

###### 段：矩形条件与正交延拓的非唯一

满列秩且 $m\geq n$时规范 $Q$有正交列，满行秩且 $m\leq n$时有正交行；不能对任意矩形矩阵同时要求这两项。方阵的规范部分等距可在核与输出正交补之间选择等距对应，延拓为完整正交因子；可逆时无需补全且该因子唯一，秩亏时完整延拓一般不唯一。矩形秩亏情形若希望补成正交列或正交行，也需相应维数条件及补基，不把所有部分等距映射直接称为完整保长度变换。

###### 段：最近正交矩阵与最近旋转

由方阵任务 $\|A-R\|_F^2$展开转为最大化 $\operatorname{tr}(R^{\top}A)$，用本处刚建立的极分解与奇异值配对证明完整正交延拓达到最近误差。实旋转额外要求 $\det R=1$，行列式修正放在最弱奇异方向；保留最近正交矩阵为反射而最近旋转不同的例子，说明定向约束可能增加误差，零或重复弱方向可保留多解。

###### 段：对应点对齐与输入误差尺度

对 $\min_{R\in\mathrm{SO}(n)}\|RX-Y\|_F^2$使用交叉矩阵 $YX^{\top}$的SVD，允许平移时先减均值再恢复平移。明确输入为已建立对应的点组，最优对齐不同时解决对应关系估计；加权、缩放或只约束比例时需重写目标与可行集合，不将代数残差最小称为任意几何距离最小。

#### 4.3.6 矩阵方程

【沿用重组；补充Lyapunov特例】未知量仍是一张实矩阵，但除了前面 $AX=B$的共同系数与多右端，还可能受到右侧作用或左右作用之和的耦合。沿用线性空间、向量化与左右作用判断结构化线性算子的相容性、自由度和可逆性，再选逐侧求解、实Schur块回代或矩阵作用迭代；通用向量化用于论证，不要求实际建立过大的Kronecker矩阵。原正文依据为2336—2391行。

##### 4.3.6.1 单侧与双侧乘法下的矩阵求解

由 $AX=C$、$XB=C$进入 $AXB=C$，说明左乘和右乘作用于未知矩阵的不同坐标维度。未知矩阵包含多个右端或双侧耦合，两类信息可用于复用分解。

###### 段：逐列求解与逐侧反演

单侧方程按列或转置后按列求解，共享同一个系数分解；两侧矩阵为可逆方阵时先后解两侧系统即可得到唯一 $X$。矩形或奇异情形通过 $AA^\dagger CB^\dagger B=C$判断相容性，相容时 $A^\dagger CB^\dagger$为最小Frobenius范数代表；由左右正交投影说明其选解依据，不直接套不存在的 $A^{-1}CB^{-1}$。

###### 段：向量化与最小二乘编码

回用 $\operatorname{vec}(AXB)=(B^\top\otimes A)\operatorname{vec}X$，沿列堆叠逐项核对转置位置。以实Kronecker系数的值域和零空间表达相容性／自由度，也可求 $\|AXB-C\|_F$最小；大规模时通过 $X\mapsto AXB$和Frobenius内积下的转置作用 $Y\mapsto A^{\top}YB^{\top}$执行计算，避免保存乘积维数的系数矩阵。

##### 4.3.6.2 Sylvester型矩阵方程

研究实矩阵方程 $AX+XB=C$，将左右作用之和看作对未知矩阵的实线性算子；为把耦合方程改写成可顺序回代的小问题，在这里首次构造实Schur表示。一般实矩阵不保证存在实特征方向或实上三角表示，因此使用一阶／二阶对角块的块上三角形式，再通过适当次序逐小块回代。

###### 段：实多项式因子与一维、二维不变子空间

从实多项式可分解为实线性因子与实不可约二次因子的代数背景出发，说明前者对应实特征方向，后者需要二维不变子空间，不能强行寻找两个实特征向量。以Cayley–Hamilton保证存在消去 $A$的非零实多项式，取最低次数首一式，再用互素因子的多项式恒等式将空间分成相应广义核，交代各因子不变部分的非零性。对二次因子 $p(t)=t^2+at+b$，从非零广义核取出 $p(A)v=0$的非零向量，以 $v,Av$构造二维不变空间；不可约性保证二者独立。由此获得一维／二维不变空间并逐步正交约化，保留来源及归纳论证，所有坐标和计算均为实数。

###### 段：实Schur小块与数值计算入口

将每次选出的实不变子空间补成标准正交基，得到 $A=QTQ^{\top}$，其中 $T$为一阶／二阶对角块组成的实块上三角矩阵；对剩余块递归建立实Schur形式。二维旋转展示没有实特征方向仍有合法二维块的情形，实对称矩阵则由4.3.3.2得到更强的正交对角化。正交变换保持当前误差尺度，一般矩阵函数通过实小块计算；4.4.1的实标量Jordan分析另加特征多项式在实数上分裂的条件，不作为所有矩阵的通用数值算法。

###### 段：实线性算子的可逆性与唯一可解性

先由向量化得到实矩阵 $K=I_n\otimes A+B^{\top}\otimes I_m$，建立“对任意实右端唯一可解”等价于 $K$可逆，也等价于齐次方程 $AX+XB=0$只有零解。实Schur回代将其化为一阶／二阶对角块配对形成的一、二或四维小系统，需每个相应系数块可逆；仅当两侧特征多项式均在实数上分裂时，才简化为全部实特征值和 $\lambda_i(A)+\lambda_j(B)\ne0$。用旋转矩阵 $J=\left[\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right]$、$A=J,B=-J$说明两者都无实特征值，齐次方程仍含 $X=I$，不能仅凭“没有相遇的实特征值”判唯一。系数各自可逆仍非充分或必要条件，算子奇异时须分别判断相容性与自由度。

###### 段：三角求解与结构成本

在实Schur形式中按块列从左向右、每列从下向上的顺序求解一、二或四维子问题；只有实一阶块配对时才用标量和直接相除。交代两侧分解与块三角求解的工作，标准稠密规模下为 $O(m^3+n^3+m^2n+mn^2)$量级，矩阵存储为 $O(m^2+n^2+mn)$。小块接近奇异造成的敏感性与非正规影响留到4.4.2，不把“标量和不为零”用于判断一般二维块，也不把代数可逆当作数值可靠性的充分条件。

##### 4.3.6.3 Lyapunov方程

【补充】把Sylvester系数联系起来，介绍连续型 $A^{\top}P+PA=-Q$和离散型 $P-A^{\top}PA=Q$，明确已知 $A,Q$、未知 $P$。两种方程分别与连续时间导出能量变化、离散重复作用下的能量变化相连，具体动力学解释由微分方程章承接。

###### 段：连续型Lyapunov与正定能量

将Sylvester左系数取为 $A^{\top}$、右系数取为 $A$，回用实Kronecker算子的可逆性判据；另给出实数形式的充分条件：存在 $C,c>0$使 $\|e^{tA}\|_2\leq Ce^{-ct}$对全部 $t\geq0$成立。由此构造 $P=\int_0^\infty e^{tA^{\top}}Qe^{tA}\,\mathrm dt$，说明对每个实对称 $Q$唯一可解，$Q\succeq0$给 $P\succeq0$，$Q\succ0$给 $P\succ0$；积分验证与轨迹能量解释放在微积分／微分方程章回读。实Schur一阶块为负、二阶块的迹为负且行列式为正可作为指数衰减的块条件，其作用由实小块计算解释，不能只由唯一性推出正定性。

###### 段：离散型Lyapunov与重复作用

对 $\rho(A)<1$，用 $P=\sum_{k\geq0}(A^{\top})^kQA^k$构造并检验解，连接固定矩阵幂的衰减；级数收敛的完整依据放到4.4.1。说明正半定 $Q$给正半定解，正定 $Q$给正定解；一般唯一可解还需对应线性算子不含零特征值，不能把 $\rho(A)<1$说成任意给定方程唯一可解的必要条件。

### 4.4 分析

前面已经确定对象的表示、运算规则和问题的求解方法，本节检验这些方法产生的结果。固定数据和目标时，收敛分析研究近似序列是否达到目标、趋近多快，以及初值和停止时刻改变什么；改变输入或允许计算误差时，扰动分析研究结果如何响应、哪些误差可以被残差证据控制。全节沿用近共线设计矩阵和非正规二维迭代例，分别追踪参数、拟合值与目标值，不能用其中一项的表现替代其余判断。

论证先从有限维坐标极限建立收敛语言，再研究具有指定生成规则的矩阵幂和迭代。扰动部分先约定误差与条件数，再依次处理解、计算过程、正则化估计、谱方向和矩阵函数。精确算术下的极限、问题本身的敏感性和算法产生的舍入误差分别交代；涉及一般导数、Fréchet导数和积分导数的内容保留【微积分后回读】标记。

#### 4.4.1 收敛分析

固定问题、数据和算法，研究有限维近似对象是否趋于指定目标。任意序列先以范数和逐坐标极限比较，再按生成规则讨论反复作用、定常校正、最小二乘更新、Krylov搜索及谱方向迭代。有限维范数等价连接坐标极限与几何误差，谱表示解释固定作用，二次能量和残差多项式解释搜索方向改变的更新。

沿同一问题同时记录极限对象、成立条件、初值依赖、速度及停止依据。一次误差下降不构成整个序列收敛的证明，精确算术的有限步结论也不能替代浮点运算中的真实残差核验。
##### 4.4.1.1 有限维对象序列

讨论向量、矩阵及固定有限基下的其他对象，回答逐坐标趋近能否保证对象整体趋近，以及换用误差尺度是否改变结论。从范数的双侧比较建立有限维统一性，再利用实数完备性与有限坐标紧性说明极限的存在；所有常数均固定于当前空间和范数，不据此给出维数一致的保证。原文来源：线性章第2402—2434行，并承接第333—492行的具体范数比较。

###### 段：逐坐标极限与范数极限

固定一组有限基，用坐标最大范数控制任意范数的上界，再在坐标单位球面上取得正的最小值，得到反向控制。先从前章的实数有界序列逐坐标抽取子列，建立这里所需的有限维紧性，避免把后面度量空间章的结论当作前提。

先以二维向量逐项趋近的例子建立整体误差，再将有限个坐标误差合并为最大误差；反向由每个坐标的连续读取得到各坐标趋零。矩阵采用固定向量化次序同样处理，不能把轴数增加或维数随步数增长的数组混入这个固定空间结论。

###### 段：有限维范数等价

对任意两个范数给出正的双侧比较常数，说明它们保留收敛、柯西与有界性的判断。用常见范数之间的维数因子解释“同样收敛”不等于“数值误差相同”，并为后续条件数使用指定范数保留位置。

###### 段：完备性与闭子空间

将有限维柯西序列拆成有限条标量柯西序列，逐项取极限再重组对象，得到完备性。随后研究闭集合和有界集合分别提供什么，以闭且有界时的收敛子列结论连接单位球上的最坏误差达到。

说明柯西性仅比较序列后段的内部差异，完备性才保证极限留在空间内。用实数坐标极限完成有限维完备性证明，再说明闭子空间保留这些极限；此处只处理有限维，不提前建立一般Banach空间理论。

###### 段：闭有界集合与收敛子列

以有限个坐标依次抽取子列，再用闭性保证共同子列的极限仍在可行集合中，建立有限维闭有界集合的紧性。由单位球紧性与线性映射连续性，补齐诱导范数、对偶范数最大值可达的依据；两个点交替的序列说明存在收敛子列不足以保证原序列收敛。

##### 4.4.1.2 矩阵幂与级数

固定一个实方阵，分别研究矩阵幂的长期极限和由幂构造的无穷级数。回用4.2.8.2定义的实矩阵幂增长率，用次乘性和分段幂证明一般收敛判据，不假设存在实特征值或实Jordan形式。实Schur已在4.3.6.2服务于矩阵方程；这里仅在特征多项式于实数上分裂的附加条件下构造实标量Jordan链，作为耦合与多项式增长的计算例，完整保留该范围内的构造和证明。原文来源：线性章第1199—1239、1454—1569、2435—2482行，并接收原集中分解草稿中的相应分析材料。

###### 段：实幂增长率的下确界与增长极限

从所有初值均趋于零的要求进入整个矩阵幂的控制，先以实范数建立增长率与衰减的等价，再用不变的固定点空间及变化空间判断有限极限。实分裂时的Jordan块为这些一般结论提供显式计算，并解释单方向缩放之外的耦合；旋转例子同时说明没有实特征方向也不妨碍直接分析矩阵幂。

设 $\rho(A)=\inf_{j\geq1}\|A^j\|_2^{1/j}$，说明它也等于 $\lim_{k\to\infty}\|A^k\|_2^{1/k}$。固定一段长度 $j$，将 $k=qj+r$、$0\leq r<j$代入 $\|A^k\|_2\leq\|A^j\|_2^q\|A^r\|_2$，对上极限取界后再对 $j$取下确界；反向下界由下确界定义直接得到。若某个幂为零则其后全为零，先独立处理，不对零取对数。这里的 $\rho$从实矩阵作用定义，不用全部特征值模的列表充当其前提。

###### 段：幂增长率与所有初值的衰减

证明 $A^k\to0$当且仅当 $\rho(A)<1$：必要性由某个足够大的 $j$使 $\|A^j\|_2<1$得到；充分性选择这样的分段长度，把余下有限个幂的最大范数并入常数，得到几何衰减界。结合有限维基向量逐列读取说明矩阵范数衰减与全部实初值轨迹衰减等价；范数 $\|A\|_2<1$只是可直接检验的充分条件，原有非正规二维例仍保留先放大后衰减，不能只看一次作用。

###### 段：固定点空间与一般有限极限

令 $E=\ker(I-A)$、$F=\operatorname{range}(I-A)$。证明 $A^k$有有限极限的充要条件为 $\ker(I-A)=\ker((I-A)^2)$且限制作用 $A|_F$的幂增长率小于1；前一条件使 $E\cap F=\{0\}$，结合秩—零度得到实直和 $\mathbb R^n=E\oplus F$。$A$在 $E$上恒等，在 $F$上衰减，所以极限是沿 $F$投到 $E$的投影，未必是正交投影。反向由 $A^k(I-A)y\to0$及固定点始终保持，得到两个子空间的分工和必要性；$F=\{0\}$时衰减条件按空作用直接处理。

###### 段：实分裂条件下的广义特征向量链

明确假设特征多项式在实数上分裂，回用4.2.8.2的二维不可对角化例子，比较实特征值代数重数和特征空间维数，再以 $(A-\lambda I)v_{j+1}=v_j$定义实广义特征向量链。沿 $\ker(A-\lambda I)^j$的递增序列选择链端、向下递推并逐层补齐独立方向，说明各链长度与广义特征子空间维数的关系，再将不同实特征值的广义子空间合并为实基；保留构造、线性无关与张成的证明。若不满足实分裂条件，则使用一般实增长率与实Schur小块，不把实标量Jordan形式强加给旋转矩阵。

###### 段：Jordan块幂与多项式增长因子

在上述实分裂条件下写实相似变换 $A=SJS^{-1}$、$J_\lambda=\lambda I+N$且 $N^q=0$，由可交换二项式展开推导 $J_\lambda^k=\sum_{j=0}^{\min(k,q-1)}\binom{k}{j}\lambda^{k-j}N^j$。非零实特征值产生有限次多项式乘指数，零特征值块则在有限步后直接归零，分开处理以避免含负幂或 $0/0$的错误改写。由块公式证明本情形 $\rho(A)=\max_i|\lambda_i|$，不是据此将所有实矩阵的增长率定义改成实特征值最大绝对值；有完整实特征向量基时各块为一阶，重根本身不必然导致缺少方向。

###### 段：分析表示与数值表示的边界

实Jordan链记录精确代数耦合，适合在实分裂范围内解释幂中的多项式因子；链长与块数可在微小实扰动下改变，甚至实分裂条件也可能失效，不能据此设计通用数值算法。回用已经建立的实Schur作为一般实矩阵的数值表示入口，区分一般实相似变换的条件放大与正交变换的保长度性质；非正规性和Jordan邻近的实根变化在4.4.2继续分析。

###### 段：实Schur二维块与旋转的增长

以 $R_\theta=\left[\begin{smallmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{smallmatrix}\right]$说明正交旋转保持长度，$\rho(R_\theta)=1$；$0<c<1$时 $cR_\theta$的增长率为 $c$且所有轨迹衰减，通常仍无实特征方向。对不可约实二次因子对应的二维块，可在实坐标中改写成伸缩与旋转的组合；保留实小块的计算依据，使一般Schur与增长率分析覆盖实标量Jordan例子以外的对象。

###### 段：单位圆边界与变化的作用矩阵

在实分裂例子中把一般有限极限条件读成：各实特征值位于 $(-1,1)$或等于1，且特征值1的Jordan块为一阶。用特征值 $-1$展示符号振荡，特征值1的非平凡Jordan块展示多项式增长，非平凡旋转展示无实特征方向时仍可能持续振荡；再保留两幂零矩阵交替相乘可能增长的例子，说明各步增长率小于1不能直接保证时变乘积衰减。

###### 段：Neumann级数与逆的构造

回用次乘性和前章实幂级数，先以矩阵范数小于标量收敛半径给出充分条件，再用分段幂的几何界将条件放宽到实幂增长率小于该半径。边界与函数的实定义域分别检查，截断误差也与浮点计算误差分开；实分裂时再用Jordan块作计算说明，有限幂、反复平方和矩阵多项式的算法仍由4.2.8承担。

由有限几何和恒等式证明，当实幂增长率 $\rho(A)<1$时，\(\sum_{k\geq0}A^k\)收敛到\((I-A)^{-1}\)；分段幂提供绝对收敛界，极限乘回证明逆的存在。在给定诱导范数满足\(\|A\|<1\)时写出可直接计算的几何尾界；增长率条件成立但当前范数大于1时，不能照用以一次范数为公比的尾界。

###### 段：指数级数与一般幂级数

说明矩阵指数对任意有限实方阵绝对收敛，并用实标量指数尾项控制截断；一般实幂级数在增长率严格小于其标量收敛半径时由几何界保证，边界另核。回用运算部分定义的矩阵函数以及方程和优化部分建立的实对称谱；这里仅在实分裂的Jordan块上补充分析接口：【微积分后回读】实标量函数具有所需导数并满足相应定义条件时，$f(\lambda I+N)=\sum_{j=0}^{q-1}f^{(j)}(\lambda)N^j/j!$。不逐元素套用标量函数，也不把该实标量块公式用于任意二维旋转块；一般实小块计算回用实Schur，积分和连续时间解释在后续章节承接。

##### 4.4.1.3 定常迭代

接住方程求解节的Jacobi、Gauss–Seidel与SOR，固定矩阵、右端和更新规则，从误差传递矩阵判断所有初值能否达到同一个精确解。统一判据与容易核验的充分条件分别给出，再借相同输入解释并行更新、扫描顺序和松弛参数怎样改变收敛。原文来源：线性章第1817—1893行。

###### 段：分裂矩阵与误差传播

将\(A=M-N\)的更新减去精确解，得到\(e^{(k+1)}=M^{-1}Ne^{(k)}\)。回用固定实矩阵幂判据，说明对所有初值收敛的充要条件是迭代矩阵的实幂增长率小于1；仅对某个特殊初值成功不构成这个保证，也不要求迭代矩阵先拥有完整实特征方向。

明确\(M\)须可逆，并记录误差、真实残差及更新量之间的关系。用同一二维方程比较一次Jacobi与Gauss–Seidel更新，说明它们即使求同一精确解，生成序列也不同，不能共享未经核对的收敛结论。

###### 段：对角占优下的收缩控制

在各行严格对角占优时，以无穷范数逐行估计Jacobi误差；Gauss–Seidel则沿扫描次序归纳控制已更新分量，给出收敛充分条件。强调这一条件并非必要条件，且排序改变Gauss–Seidel的迭代矩阵及实际进展。

###### 段：逐坐标能量下降

对实对称正定系统，用二次能量的下降解释逐坐标校正，证明Gauss–Seidel及固定\(0<\omega<2\)的SOR收敛。将能量有下界、残差趋零与参数趋近三步连起来，并解释这个论证不适用于同时读取旧值的Jacobi。

计算一次SOR坐标更新造成的精确能量差，由正定性与\(\omega(2-\omega)>0\)控制每次校正。再由同轮变化趋零推得各行残差共同趋零，最后利用系统可逆性得到解误差趋零，保留中间逻辑。

###### 段：参数选择与条件失效

说明\(\omega=1\)回到Gauss–Seidel，欠松弛与超松弛改变校正幅度；较大的参数没有统一的加速保证。保留正定矩阵上Jacobi发散的反例，展示正定性能够支持某些更新规则，却不足以保证所有分裂方法收敛。

##### 4.4.1.4 最小二乘迭代

固定矩形设计矩阵和平方残差目标，研究方程和优化部分的Landweber更新的严格步长范围、初值依赖及趋近速度。利用\(A^{\top}A\)的正交谱方向分别处理可辨认部分和零空间，明确算法收敛到哪个系数向量；用原文近共线例比较拟合准确与参数可靠这两个问题。原文来源：线性章第2320—2335、2483—2553行。

###### 段：各谱方向的衰减与步长端点

把更新与一个最小范数最小二乘解相减，在正特征方向得到\(1-\eta\sigma_i^2\)的倍率，在核方向得到恒等作用。对\(x^{(k+1)}=x^{(k)}+\eta A^{\top}(b-Ax^{(k)})\)这一更新约定，说明\(0<\eta<2/\|A\|_2^2\)的严格范围；若使用样本平均目标，同步调整步长尺度。

在每个正奇异方向逐项判断误差倍率的绝对值，并由有限方向合并得到收敛。说明上端点使最大奇异方向一般发生等幅振荡，零矩阵则保持任意初值，不能使用分母为零的步长公式。

###### 段：初值决定的极限代表

得到极限\(A^\dagger b+(I-A^\dagger A)x^{(0)}\)，解释梯度更新无法改变原有零空间分量。零初值因而选择最小范数最小二乘解；满行秩欠定时，该解还是最小范数插值解，其他初值可能得到相同拟合而不同系数。

###### 段：三个收敛对象的区别

沿同一谱展开分别观察平方目标差、可达输出误差与系数误差，说明它们受奇异值的权重不同。对于满列秩或去掉核方向后的正谱，给出以最大和最小正奇异值控制的几何收敛尺度，再说明近共线为何造成缓慢或敏感。

目标值趋近最小值只控制可观测输出，不能据此判定所有参数都趋向某个预先指定的向量。对照精确插值和秩亏例子，说明残差下限、唯一拟合值与不唯一系数如何同时成立，并记录报告训练结果时所用的误差对象。

###### 段：小正奇异值与停止时刻

解释小正奇异值使相应系数方向的收缩倍率接近1，固定步长必须同时服从最大方向的限制。有限步停止只保证已计算的误差水平；其抑制尚未学得的小尺度方向的作用可在扰动分析中与显式滤波比较，不能把早停称作无条件恢复真参数。

##### 4.4.1.5 Krylov迭代

对实对称正定系统，研究方程和优化部分的CG如何在逐步扩大的仿射Krylov空间内逼近精确解，并分析正定预条件改变后的谱尺度。精确算术的有限终止、按步数的误差上界和有限精度下的实际停止分别说明，避免以理论步数替代误差核验。原文来源：线性章第1928—2058、2554—2591行。

###### 段：能量误差的逐步选优

回用CG的共轭方向和残差正交性，说明第\(k\)步在当前候选空间内最小化能量误差。非零共轭方向线性无关给出精确算术下至多维数步终止；算法构造与归纳证明保留在方程求解节，本处解释这项结论对收敛的含义。

由二次目标差等于\(A\)范数误差平方的一半，连接优化值与解误差。嵌套候选空间保证最佳能量误差不增，但不要求每个坐标误差或欧氏残差都逐步单调下降。

###### 段：有限步结论与浮点计算

明确精确算术、对称正定和非零搜索方向等前提，并在残差为零时停止。浮点运算可能损害正交性与共轭性，实际终止需重新计算真实残差，不能承诺在机器计算中严格不超过维数步。

###### 段：Chebyshev界与谱聚簇

把候选误差写成\(p_k(A)e^{(0)}\)，其中\(p_k(0)=1\)，再用Chebyshev多项式在正谱区间控制最坏误差。由此建立条件数与速度的联系，同时说明只使用谱端点的界可能忽略特征值聚簇带来的更快进展。

令\(q=(\sqrt\kappa-1)/(\sqrt\kappa+1)\)，明确经典界为\(\|e^{(k)}\|_A\leq2q^k\|e^{(0)}\|_A\)，其中先取\(\kappa=\lambda_{\max}(A)/\lambda_{\min}(A)\)；扰动分析再说明这个比值作为欧氏条件数的含义。这是相对初始误差的能量范数缩减，目标差等于该范数平方的一半，不能直接套用同一个无量纲因子作为目标差上界。标量倍单位矩阵单独处理为一步求解；聚簇谱可按实际谱点选择更有利的多项式，不把最坏区间界当成逐例精确预测。

###### 段：正定预条件的条件数

以\(M^{-1/2}AM^{-1/2}\)的对称正定系统应用相同界，说明PCG要求预条件器与内积相容。评价预条件收益时同时计入构造、辅助求解、每步作用和存储，减少迭代次数并不自动减少总成本。

###### 段：原系统残差与非正规作用

对缺少正定能量的一般系统，改用原系统残差及搜索空间判断进展；进一步将同一搜索空间语言用于特征方向估计。先完整保留原文GMRES的可逆性、非正规与重启边界，再把方向估计作为明确标记的必要补充，新增内容不声称来自既有正文。原文来源：线性章第2059—2093、2592—2604行；方向迭代为拟补充内容。

由GMRES的嵌套实Krylov候选集得到精确算术下欧氏残差不增，并在可逆矩阵条件下解释Arnoldi提前停止和有限步求解。将残差多项式的矩阵范数作为一般速度依据；已有实特征值不能记录全部作用，缺少实特征方向时也可直接使用这一范数表述。

以实系数多项式的\(\min_{p(0)=1,\deg p\leq k}\|p(A)\|_2\)控制相对残差；仅在 $A$可由实基对角化时，进一步用实特征值上的多项式值和特征向量基放大因子估计。一般情况保留矩阵作用或实Schur小块，不用不存在的实谱分解。左预条件最小化变换后的残差，右预条件保留原系统残差口径，报告收敛曲线时须说明具体对象。

###### 段：重启、提前停止与残差核验

说明Arnoldi剩余向量为零时应结束扩基并求当前小问题，在可逆前提下精确解已位于当前候选集。重启减小存储同时丢弃旧空间信息，可能停滞且不再保留至多维数步的保证；递推残差最终须与重新计算的真实残差核对。

##### 4.4.1.6 谱方向迭代

将搜索空间用于估计特征方向或不变子空间时，目标从满足给定右端的方程转为寻找作用后保持方向或子空间的对象。先分析单方向幂迭代及实移位反迭代的分离和初值条件，再研究Arnoldi、Lanczos及实Schur小块的残差；这些方法中的新增推导仍按拟补充内容标记。

###### 段：单方向迭代的谱分离与初值

拟补充按矩阵反复作用寻找方向的基本问题，以幂迭代与移位反迭代连接前文谱表示，再说明Arnoldi及实对称情形的Lanczos如何在较小搜索空间提取近似谱。当前大纲要求实施时补充推导与来源，不把这些新增方法写成原文已完成的内容。

在可由实基对角化、具有绝对值严格大于其他值的单个实特征值时，计划沿实谱展开说明归一化幂迭代如何趋近主导方向，并指出初值必须含该方向分量；负号导致符号交替，按直线方向而非固定符号判断。移位反迭代采用实移位并要求移位系统可解，其速度与目标实特征值的分离有关；旋转没有相应实特征方向时不宣称单方向迭代收敛，聚集、重数和非正规性均需另核。

###### 段：子空间提取与近似谱的残差

回用实Arnoldi形成的小矩阵；出现实特征值与实特征向量时，映回原空间并计算特征残差，一般情况则保留实Schur的一阶／二阶小块，核验 $AU-UT$的近似不变子空间残差。实对称矩阵进一步得到Lanczos三对角形式与实谱读取。残差先说明作用关系是否近似成立，再由扰动分析中的间隙结论判断相应方向或子空间是否可靠，不能据小残差强求一般矩阵存在单个实特征向量。

#### 4.4.2 扰动分析

固定输入输出映射和误差口径，研究数据变化或计算误差怎样改变结果。先用前向误差、后向误差和条件数区分结果偏离、等效输入改变和问题本身的放大能力，再分别分析方程解、拟合值、谱方向及矩阵函数。浮点舍入和分解路径的误差归入计算过程的扰动，后向稳定与前向准确仍需分别判断。

延续近共线例，解释拟合值稳定、系数敏感和算法后向稳定可以同时成立。正则化已经在方程和优化部分定义，本处研究改变估计目标后得到的抗扰动效果及其偏差；每个结论保留允许扰动的集合、所用范数、秩或谱隙条件和定义域边界。

##### 4.4.2.1 误差与条件数

固定映射、输入和输出的含义，再分别讨论真实数据到输入数据的误差、精确输入到算法结果的误差。前向误差直接比较输出，后向误差寻找等效输入改变；条件数负责连接两者，浮点模型负责说明算法如何产生舍入。原文来源：线性章第3336—3393行。

###### 段：数据误差与算法误差的分解

通过一次线性读取和一个近奇异方程的对照，说明小输入误差可能被问题本身放大。后向误差必须写明允许改动哪些输入、用什么尺度以及是否保持对称等结构，不用一个含混的“误差小”覆盖不同问题。

分别记真实输入、实际输入及计算结果，把数据扰动造成的输出变化与算法对实际输入的误差拆开。用同一输出尺度解释两者怎样累积，避免把病态数据导致的误差全部归因于求解器。

###### 段：后向误差的允许集合

说明仅改右端、同时改矩阵和右端、或只允许结构化矩阵扰动会得到不同的后向误差。条件数同样依赖输入输出范数；后向稳定只保证结果对应一个邻近允许问题，前向准确还需要该邻域内的敏感性适中。

###### 段：舍入累积与后向稳定

在明确无异常溢出等前提后引入基本浮点运算的相对误差模型，说明多步运算的界还须累计舍入和中间量增长。一般映射的导数条件数作为微积分后回读内容，当前以线性读取、乘法和求解的显式有限扰动界支撑判断。

从基本运算的单位舍入误差进入算法级误差，保留运算规模、中间量增长和输入结构的影响。给出范数意义下后向稳定的对象与量级含义，并说明一次计算残差小还不能自动证明整个算法对所有输入后向稳定。

###### 段：局部条件数的导数表达

【微积分后回读】将绝对局部条件数写为导数算子范数，相对条件数还需乘输入尺度、除输出尺度，并要求相应分母非零。解释这是一阶小扰动的最坏放大率，有限扰动仍需余项或额外邻域控制；当前可先利用前文已经给出的线性界。

##### 4.4.2.2 方程解与拟合

先固定可逆方阵研究逆与解，再转向满列秩、满行秩以及保持秩的伪逆。用最小正奇异值控制可恢复方向的敏感性，明确跨越秩变化时原有连续性保证会失效；同一例中同时报告输入系数与输出拟合的变化。原文来源：线性章第3394—3572行。

###### 段：逆的扰动与条件数

对\(A+E\)与\(b+f\)共同改变的方程，在\(\|A^{-1}E\|<1\)下由Neumann级数控制新逆，再得到解误差。条件数记录当前范数下的最坏放大，分母余量记录扰动距离奇异边界还剩多少保证。

推导\((A+E)^{-1}-A^{-1}\)的有限范数界，并定义\(\kappa(A)=\|A\|\|A^{-1}\|\)。欧氏情形回用SVD得到最大与最小奇异值之比；保证条件失效只表示当前界不能使用，不等于扰动后的矩阵必定奇异。

###### 段：右端与矩阵误差的共同作用

从误差方程拆出\(f\)和\(Ex\)两项，得到含条件数和扰动余量的相对解误差界。沿近共线小奇异方向演示响应的微小变化怎样产生大系数变化，明确最坏方向上界并不意味着所有扰动都会达到该倍率。

###### 段：伪逆的秩条件与奇异边界

对于固定秩邻域，要求原矩阵与扰动矩阵的最小正奇异值均远离零，再控制伪逆及最小范数解变化。随后把\(Ax\)的拟合误差与\(x\)的系数误差分开，说明投影造成的稳定输出不能反推出稳定参数。

保留原文同秩伪逆恒等式和有限界，以两侧最小正奇异值下界给出适用区域。用标量\(\varepsilon\)的伪逆说明秩变化处可能不连续，单独给出非零奇异值间隙不能排除原零方向出现新的微小正奇异值。

###### 段：最小二乘的输入与输出误差

将扰动后的最小范数系数、最近可达输出和不可拟合残差分别比较，说明它们的误差来源不同。满列秩或满行秩时结合对应伪逆公式与谱下界说明稳定范围；秩亏情形仍须明确选解准则和秩是否保持，不能只报告最小残差。

###### 段：算子可逆与数值分离

【补充桥接】回到方程和优化部分的Sylvester方程，把$\mathcal L(X)=AX+XB$看成矩阵空间上的线性作用。在Frobenius误差下定义分离量$\operatorname{sep}(A,-B)=\min_{\|X\|_F=1}\|AX+XB\|_F$，它是向量化系数矩阵的最小奇异值；正分离量给可逆性，大小决定最坏误差放大。

对同一实系数的近似解，用$\|X-\widehat X\|_F\leq\|C-A\widehat X-\widehat XB\|_F/\operatorname{sep}(A,-B)$解释残差证据。实Kronecker算子可逆只保证分离量非零，不能给出其大小；一般实Schur二维块必须按整个小系统判断，不能仅比较已有实特征值的和。即便两侧均实分裂，非正规耦合也会使最小奇异值与最小实特征值和的绝对值不同，不能用后者无条件替代分母。

###### 段：系数扰动与结构残差

将$A,B,C$同时改变时的误差写成原Sylvester算子作用下的右端扰动，并在扰动算子范数小于原分离量时控制新逆。Lyapunov任务还需核验实对称结构及目标要求的正定性；小代数残差不能单独证明这些性质，平方根响应在4.4.2.6再次回用同一分离判断。

##### 4.4.2.3 残差与数值稳定性

将实际返回值带回原方程，研究能够直接计算的残差怎样支持前向或后向判断，再比较分解及迭代的误差来源。数值求解的选择与算法构造已在方程优化节说明，本处集中解释为何某种计算路径多损失了精度，以及停止证据必须包含哪些量。原文来源：线性章第3676—3806行。

###### 段：小残差的解释范围

对可逆方程由\(x-\widehat x=A^{-1}r\)连接真实残差和解误差，再在不同扰动口径下计算后向误差。相对公式的分母为零时改报绝对量；矩形最小二乘还应核验最优性残差，不能套用精确方程的全部评价。

给出相对残差乘条件数控制相对解误差的条件，说明病态系统中小残差仍可能伴随大参数误差。矩形问题同时检查拟合残差及\(A^{\top}r\)是否接近零，因为非零的最优拟合残差本来就可能无法消除。

###### 段：联合扰动下的后向误差

以\(\|r\|/(\|A\|\|\widehat x\|+\|b\|)\)说明范数型相对后向误差，并交代适用范数和零分母情况。结构化问题保留允许扰动的额外限制；最小二乘算法的完整评价还须保持其最小残差任务，不能只证明返回值解了一个邻近精确方程。

###### 段：分解误差与正规方程的额外损失

对相同系统解释主元LU、Cholesky、Householder QR和SVD各自的误差依据，再用SVD说明显式形成正规方程为何把条件数平方。由重新计算残差进入迭代改进，说明它能利用既有分解修正结果，但仍受条件数和残差精度限制。

LU的后向误差需计入消元增长，成功完成的正定Cholesky和Householder QR各有相应的范数误差条件。对满列秩矩阵给出\(\kappa_2(A^{\top}A)=\kappa_2(A)^2\)，解释QR/SVD避免显式Gram形成的额外损失，却不能消除原矩阵小奇异值带来的敏感性。

###### 段：真实残差与迭代改进的停止依据

重新计算\(b-A\widehat x\)，使用既有分解解校正方程，再更新结果；解释提高残差计算精度何时有帮助。对于递推求解同时核对真实残差、相对后向误差及条件数估计，记录停滞或精度下限，不承诺任意病态问题都能由改进恢复准确参数。

##### 4.4.2.4 正则化估计

回用方程优化节已经定义的截断、岭和一般Tikhonov目标，研究它们怎样削弱不稳定方向，以及同时引入什么偏差。参数选择以噪声尺度和可接受残差为依据，明确正则化改变估计任务，不能解释为将原问题无条件算得更准确。原文来源：线性章第3561—3675行，并联系第3105—3158行的核范数收缩。

###### 段：截断与连续收缩的不同代价

在标准欧氏残差和零阶二次惩罚下，以SVD逐方向比较伪逆、截断与岭滤波；将观测噪声项和估计偏差分别列出。硬阈值、连续收缩和有限迭代的滤波机制各有边界，不把所有压缩方式等同为同一种最优解。

说明伪逆中的\(1/\sigma_i\)会放大小正奇异方向的观测误差；截断直接舍去小尺度，岭将其改为\(\sigma_i/(\sigma_i^2+\lambda)\)。两者都可能降低放大率，同时删去或压低真实信号；截断阈值附近的奇异值越界还可能使估计发生跳变。

###### 段：参数尺度与有限步滤波

说明\(\lambda\)、截断阈值和特征单位共同决定效果，不能在任意缩放后的矩阵之间直接比较同一数值参数。最小二乘迭代的有限步响应可与显式滤波对照，但早停效果仍受初始化、步长与噪声方向影响；核范数收缩针对矩阵估计，不能和向量岭回归的滤波公式混用。

###### 段：一般Tikhonov的零方向与唯一性

将惩罚从系数本身改为\(Lx\)，分析相邻差分或其他已说明的结构偏好。用共同核条件说明唯一性，再通过差异原则把残差容限与惩罚参数连接；一般\(L\)不共享\(A\)的奇异方向，须回到增广系统或相应联合结构分析。

对\(\|Ax-b\|^2+\lambda\|Lx\|^2\)，在\(\lambda>0\)时以\(\ker A\cap\ker L=\{0\}\)保证唯一极小点。共同零方向仍不可辨识；即使另选最小范数代表，也不能声称恢复了观测中不存在的信息，更不能对任意\(L\)逐个套普通SVD滤波。

###### 段：差异原则与可接受的残差

利用目标比较说明惩罚参数增加时允许拟合残差和惩罚量的变化方向，再按已知误差容限选择参数。容限须与不可达到的残差下限及噪声口径相容；残差约束与某个惩罚解的对应不等于参数之间总存在唯一的一一映射。

##### 4.4.2.5 谱值与子空间

先在实对称情形比较有序实谱值，再比较方向；重复特征值的方向基可以自由旋转，必须改为比较整个子空间。以主角和投影差统一方向误差，再讨论实可对角化且只追踪实特征值的条件性结论，以及适用于任意实矩形矩阵的奇异值和子空间界；将结果用于PCA与低秩截断的可辨认性。原文来源：线性章第3807—4057行。

###### 段：由交叉Gram矩阵计算主夹角

由变分原理得到Weyl逐指标谱值界，再从扰动特征方程的残差得到Davis–Kahan型方向控制。内积运算已按几何关系定义主夹角，这里首次把它变成两组谱方向之间可实际计算的比较量，所需SVD回用4.3.4.5；明确谱值稳定不需要谱隙，单个方向或目标簇与其余谱分离时才有相应的方向稳定保证。

对等维子空间的标准正交基 $Q,\widetilde Q$，计算 $Q^{\top}\widetilde Q$的SVD并取 $\sigma_i=\cos\theta_i$、$0\leq\theta_1\leq\cdots\leq\theta_r\leq\pi/2$；由两端正交投影为收缩作用证明奇异值位于 $[0,1]$，再将逐对几何最优读取化为该小矩阵的奇异方向，核对与内积运算中的定义相同。换子空间基只会左右乘正交矩阵，所以角度不依赖选取的基；零维没有角度列表，维数不同时须另外说明未配对方向，不套等维公式。

###### 段：投影差与基旋转无关的距离

对同秩正交投影 $P=QQ^{\top}$、$\widetilde P=\widetilde Q\widetilde Q^{\top}$，沿主方向平面说明 $\|P-\widetilde P\|_2=\sin\theta_{\max}$及 $\|P-\widetilde P\|_F^2=2\sum_i\sin^2\theta_i$。这使谱子空间扰动能在不固定单个基向量符号或簇内旋转的条件下表达；维数改变会留下额外投影方向，不能继续用同秩公式解释为仅有微小方向转动。

###### 段：Weyl界与谱值排序

对同维实对称矩阵及实对称扰动，将两组特征值按同一顺序排列，以扰动谱范数控制对应谱值差。给出二维近重根例子，观察谱值变化小而方向转动大的情形，避免从数值接近直接推断特征向量接近。

###### 段：谱隙、主角与整簇子空间

先以符号无关的一维夹角比较方向，再以主角或正交投影差比较等维子空间。方向界的分母使用扰动后仍为正的分离量；目标簇内部可重复，关键是簇与外部谱之间的间隙，若在重复谱中间切开则不能要求唯一方向。

###### 段：Bauer–Fike界与非正规敏感性

对实可对角化矩阵，只在扰动后仍有实特征值可追踪的范围内给出计入实特征向量基条件数的谱值界；不可对角化邻域展示实根更强的敏感性，也说明实根可能不再存在。矩形情形不受这一限制：通过实对称扩张得到奇异值界，再用两侧残差与边界谱隙控制左右奇异子空间；两端分别使用本小节前面建立的交叉Gram矩阵SVD计算主夹角，不能将位于不同空间中的左、右基直接相减。

在 $V$可逆、$\Lambda$为实对角矩阵的 $A=V\Lambda V^{-1}$中，对实扰动后矩阵的任一实特征值 $\mu$证明 $\min_i|\mu-\lambda_i|\leq\kappa_2(V)\|E\|_2$，推导使用实坐标中的残差与对角逆，不把扰动后仍实分裂视为自动成立。保留 $\left[\begin{smallmatrix}0&1\\\varepsilon&0\end{smallmatrix}\right]$在 $\varepsilon>0$时实根为 $\pm\sqrt\varepsilon$的例子，说明Jordan邻近处可有平方根量级变化；$\varepsilon<0$时无实根，不能继续追踪两条实特征方向。正交实谱基得到更有利的界，但实对称Weyl结论仍不能照搬到一般实矩阵。

###### 段：Wedin型残差界与PCA边界

由奇异方程的左右残差控制目标左右子空间，分母要求保留簇与被舍弃奇异值之间仍有正间隙。说明奇异值误差可不依赖间隙，方向误差却可能放大；PCA应同时报告重构误差、谱边界与子空间可靠性，单个基向量的符号或簇内旋转不代表数据结构变化。

##### 4.4.2.6 矩阵函数

研究把矩阵送到幂、指数、平方根、逆与对数时，输入扰动如何进入结果。先用有限代数恒等式说明非交换性，再在适用定义域中安排局部线性响应；平方根的分支与对数的定义域须同残差一起检查，不能只评价返回矩阵是否满足某个代数等式。原文来源：线性章第4058—4206行，并承接第1454—1518行的函数定义。

###### 段：幂运算中的位置依赖

对矩阵幂写出扰动插入不同位置的精确有限展开或望远镜恒等式，再控制范数；由此解释标量求导公式为何不能直接用于任意矩阵扰动。一般Fréchet响应及指数积分表达安排在微积分后回读，当前读者可先掌握有限扰动界。

将\((A+E)^k-A^k\)写成含左右不同幂次的插入项，逐项估计扰动传播。只有\(A\)与\(E\)交换时才可合并为标量式系数；固定维数和幂次的有限界不自动给出长时间矩阵幂的一致稳定保证。

###### 段：Fréchet响应与指数导数

【微积分后回读】以\(f(A+E)-f(A)=L_f(A,E)+o(\|E\|)\)定义矩阵输入的一阶响应，说明它对扰动线性，却保留非交换插入位置。实对称谱坐标中使用差商，指数使用相应的积分导数表达；回读时补充余项和定义域条件，不在当前主线提前调用尚未建立的积分或微分规则。

###### 段：平方根响应与Sylvester分离

先限定正定或其他已经选定的合法分支，再研究接近奇异边界时响应怎样放大。平方根连接前文Sylvester方程，逆连接已有有限扰动界，对数区分矩阵值函数和标量logdet；最后说明残差核验为何必须同时检查分支。

【微积分后回读】对正定主平方根\(S^2=A\)作一阶变化，得到\(S\Delta+\Delta S=E\)，由正谱保证每个谱和为正，联系Sylvester唯一性。当前可先用候选平方根残差及谱下界建立有限误差解释；若不检查半正定分支，负平方根也可能具有零代数残差。

###### 段：逆、对数与接近奇异的放大

回用逆的有限扰动界，说明负幂和实对称正定对数均受零特征值阻断。对数响应在已经建立的实对称正定定义域内展开；一般实矩阵是否存在实对数、是否唯一需另外判断，例如负实标量没有实标量对数，而二维旋转可由实矩阵指数产生，不能逐元素套标量限制。区分\(\log A\)的矩阵输出与\(\log\det A\)的标量输出，后者的导数表达安排在微积分后回读；报告结果时同时说明实定义域、选定解、残差及可用的前向或后向界。

### 4.5 本章小结

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex:4207 -->

同一对象可以用不同基与坐标记录；表示中的自由度、运算所需的结构和求解目标须分别说明。基、核像与秩回答能记录和恢复哪些方向，内积与范数规定误差口径，精确方程、最小残差、二次目标和低秩预算则要求不同的解与最优性条件。选择分解或迭代时，要同时考虑矩阵形状、秩、结构、可访问的作用及计算代价。

收敛说明固定任务的近似序列趋向哪里，扰动分析说明数据或计算改变后答案怎样变化；小残差、迭代稳定和参数准确各需对应证据。后续微积分补一般求导的语言，最优化章推广目标和约束，函数空间与微分方程继续使用本章的投影、算子、离散求解及误差判断。全章的实数范围、退化情形和微积分后回读边界在这些衔接处继续保留。

## 第5章 一元函数微积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/05-univariate-calculus.tex:1 -->

正文入口：[05-univariate-calculus.tex](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/05-univariate-calculus.tex)。

承接极限与度量，先研究一元连续与微分，再由集合测量建立一般积分，比较黎曼与勒贝格积分并说明基本定理与极限交换的条件。

### 5.1 一元函数的连续性和微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:1 -->

承接函数极限与上一节的开闭集、紧致性，区分函数值趋近和增量的线性近似；先建立各类连续条件，并用Bolzano--Weierstrass定理与闭集序列判据说明闭区间上最值定理的依据，再讲微分、运算法则、中值定理与高阶近似。函数列结论移到积分后的统一位置。

#### 5.1.1 连续函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:13 -->

从通常距离下的点处连续定义出发，立即推广到输入、输出分别指定度量的情形；随后建立运算规则，比较不同连续性条件并在此证明一致连续性定理；闭区间性质部分再研究最值与介值。

##### 5.1.1.1 连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:16 -->

先由平方函数给出ε–δ定义，说明端点与孤立点；紧接着把两个绝对值替换成所选度量并比较恒等映射的两个方向，随后给序列判据与间断分类。

###### 段：连续函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:18 -->

以平方函数误差引出点处连续的邻域条件，定义采用相对定义域；说明端点和孤立点，并验证平方函数在任意点连续。

###### 段：度量下的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:33 -->

> 【后移】本 paragraph 的一般度量连续性及通常／离散度量对照图移至第二部分；实函数连续性的绝对值定义、序列判据和其他段落均保持原位。

紧接连续性定义，为一般度量空间X、Y写出完整误差条件；输入聚点不是必要条件，孤立点自动连续；通常与离散距离的恒等映射说明改变距离可能改变连续性，保留原比较图。

###### 段：连续性的序列判据

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:49 -->

从连续定义得到输入点列的像收敛；反向用不连续所留下的固定误差构造1/n邻域反例列，说明两个条件等价。

###### 段：间断点

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:53 -->

按点值和左右极限的失配解释可去与跳跃间断，以改值平方函数和阶跃函数举例，并说明分类未穷尽所有间断。

##### 5.1.1.2 连续函数的运算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:57 -->

由已建立的函数极限运算法则，按和、差、数乘、积、商和复合逐段说明连续性保持的条件与公式；严格单调连续函数的反函数先按相对像集证明连续，不预用介值定理。

###### 段：和的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:62 -->

分别令两个连续函数趋于基点值，以和的极限公式证明相加保持连续。极限公式针对聚点，孤立点直接使用连续定义。

###### 段：差的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:70 -->

单独写出差的极限公式，按两项误差之和控制相减后的误差，得到差函数连续。

###### 段：数乘的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:77 -->

固定实数倍只缩放输出误差，给出数乘的极限公式，零常数对应连续的常函数。

###### 段：积的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:84 -->

两因子具有有限极限时，乘积极限等于点值乘积，从而得到乘积连续。

###### 段：商的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:92 -->

要求分母在基点非零，先由连续性使邻近分母绝对值大于基点绝对值的一半，再用商的极限得连续。

###### 段：复合函数的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:100 -->

先说明内层输出必须位于外层定义域，再按外层误差、内层输出误差、输入误差的次序选择尺度，直接证明复合连续。

###### 段：反函数的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:106 -->

对严格递增函数在基点两侧选输入，用像点的严格夹持控制反像；端点采用单侧，结论在像集的相对距离下成立，并设语义标签供反函数求导复用。

##### 5.1.1.3 连续性条件及其关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:111 -->

依次定义一致连续、Lipschitz、局部Lipschitz与绝对连续，以共同误差尺度、线性界、局部界和区间总变化区分控制要求；平方根的绝对连续性直接用区间增量验证，不预先调用积分。

###### 段：一致连续函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:116 -->

交换误差定义中基点与δ的量词次序；以实轴平方函数的两列相近输入说明逐点连续不保证一致连续。

###### 段：Lipschitz连续函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:127 -->

以常数倍输入距离控制输出距离，有限区间平方函数给正例；定义后的蕴含证明统一放在同一小节的关系定理中，平方根的逆向检验只保留一次。

###### 段：局部Lipschitz连续函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:140 -->

允许邻域和常数随基点改变，并用平方函数说明局部控制与全实轴共同常数的区别。

###### 段：绝对连续函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:149 -->

直接以有限个内部不交区间的总长度和端点总变化定义，避免依赖积分；直接验证平方根例子，随后在本小节集中证明条件间的蕴含。

固定同一闭区间比较四种连续性，先证明紧致性如何把逐点控制提升为共同控制，再形式化证明蕴含链并检查逆命题。

###### 段：一致连续性定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:164 -->

> 【保留，补足当地依据】标题和实轴闭有界集上的一致连续性定理保留；证明使用前章保留的实轴闭集判据与闭区间性质，不再回指后文的一般度量空间结论。

正式陈述闭且有界实数定义域上的连续函数一致连续，给出全体ε、共同δ与任意输入对的量词；反证取距离趋零但输出差有固定下界的点对，以收敛子列及闭性得到矛盾，不依赖后面的最值或介值定理。

###### 段：闭区间上的蕴含关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:188 -->

Lipschitz增量求和得到绝对连续，绝对连续取单个区间得到一致连续，共同δ得到连续；闭区间上由一致连续性定理得到末尾逆向。

###### 段：逆向关系与定义域的作用

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:210 -->

在固定闭区间归纳Lipschitz⇒绝对连续⇒一致连续⇒连续，由本小节已证定理补充连续与一致连续等价。四面板图区分局部与整体、绝对连续与Lipschitz、一致连续与绝对连续；康托尔图用八级折线示意，明确有限近似本身为Lipschitz，非绝对连续性须另证。

##### 5.1.1.4 闭区间上连续函数的性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:232 -->

以闭有界集的收敛子列证明有界与达到最值；介值定理用正式量词陈述并给上确界构造证明，强调整个区间条件。最后比较一般紧致定义域上的最值、一致连续与额外依赖区间的介值。

###### 段：有界性与最值

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:234 -->

> 【保留】本段本来就是实轴上的有界性和极值结论；只修正对已后移的一般闭集判据的依赖。

先用无界函数值列导出子列矛盾，再从接近下确界的输入列取得最小点；对负函数得最大点，并逐项展示缺闭、缺有界、缺连续的反例。

###### 段：介值定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:252 -->

形式化陈述所有介于端点值之间的c均有原像，严格介于时原像可取内点；用f(x)≤c的输入集合上确界与序列连续性构造，排除严格小于及边界；反向次序用−f处理，不连通定义域反例说明区间条件不可省。

###### 段：紧致集上的结论

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:280 -->

> 【后移】本 paragraph 是一般度量紧致集上的推广，移入第二部分“度量空间”；前面的实轴版本已足以支撑本章。

回用前面开覆盖紧致定义及其收敛子列结论，解释最值和一致连续证明可推广到一般紧致定义域；介值性不由紧致性单独推出。

#### 5.1.2 微分的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:285 -->

由差商的有限极限定义导数，区分单侧与双侧；将可导改写为线性主部与高阶余项，定义可微及微分，以平方和立方函数作比较。随后说明可微必连续、方向导数必须与同一线性映射相容，以及导函数连续的C^1条件。

##### 5.1.2.1 导数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:290 -->

以差商有限极限定义导数，说明导函数、瞬时变化率及平方函数的计算；相应下级段落区分双侧与单侧导数。

###### 段：差商

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:292 -->

先定义输入增量、函数增量及二者比值，解释平均变化率与割线斜率，为取局部极限提供对象。

###### 段：导数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:295 -->

以差商有限极限定义导数，说明导函数、瞬时变化率及平方函数的计算；相应下级段落区分双侧与单侧导数。

###### 段：单侧导数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:302 -->

分别限制增量正负，说明双侧导数存在当且仅当左右有限导数相等；闭区间端点采用内部单侧约定。

##### 5.1.2.2 可微函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:306 -->

将可导性改写为同一线性映射对全部足够小增量的近似，并通过数值例子显示主部与余项的差别。

证明一元可导等价于增量表示Ah+o(|h|)，且系数A必为导数；回用先前渐近记号，明确只讨论有限双侧内点导数。

微分是增量到预测输出增量的线性映射，导数是其系数；用平方与立方函数展示实际增量、线性模型和遗漏量。

###### 段：可微与微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:308 -->

以增量的一阶表示定义可微，说明一元可导与可微等价；区分实数导数与增量到预测输出增量的线性映射，通过平方、立方函数计算主部及遗漏量。



##### 5.1.2.3 连续可微函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:339 -->

可导后进一步要求导函数连续，定义开区间与闭区间C1约定；用x²sin(1/x)展示可导未必导数连续。

#### 5.1.3 微分的运算法则

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:345 -->

以差商或一阶展开推导四则、链式与反函数求导规则，再建立基本初等函数公式；把导数式转为微分式时核对复合次序及定义域条件。

##### 5.1.3.1 四则运算的求导

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:350 -->

和与数乘直接作用于差商；乘积取一次项、商要求分母非零，保留各项的一阶余项依据。

###### 段：和与数乘

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:352 -->

差商对有限和及常数缩放保持线性，减法归入负数倍，不另加不必要假设。

###### 段：乘积法则

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:355 -->

将两函数写成一阶主部，交叉增量为高阶小量，只保留两个一次项得到乘积导数。

###### 段：商法则

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:365 -->

先由分母连续与点值非零取得非零邻域，再整理差商得到分母平方的公式。

##### 5.1.3.2 复合函数求导

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:373 -->

陈述链式求导公式并从内层增量k=O(|h|)、外层余项o(|k|)推得o(|h|)；k=0时取余项为零，避免除以可能为零的中间增量。

##### 5.1.3.3 反函数求导

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:383 -->

回用反函数连续性，以反像增量转换差商得到倒数导数；要求单调区间上一一对应及基点导数非零，避免先假定逆映射可导。

###### 段：微分形式的运算法则

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:392 -->

把求导公式改写为作用于增量的微分，乘积保持加法，复合按内层到外层的线性映射顺序计算。

##### 5.1.3.4 基本初等函数的导数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:402 -->

逐个从差商、标准极限或逆映射规则推导整数幂、三角、指数、对数与实幂，逐项列明定义域。

###### 段：常数函数与整数幂函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:407 -->

常数和恒等函数的差商给基础公式；反复乘积求导得到正整数幂，商法则扩到负整数并排除零点，不调用二项式定理。

###### 段：正弦函数与余弦函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:417 -->

使用弧度制、三角加法公式和sin(h)/h极限推导导数，说明角度制还需换算因子。

###### 段：指数函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:426 -->

指数乘法公式将一般点差商归结为原点基本极限，得到自然指数导数等于自身。

###### 段：对数函数与实数幂函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:433 -->

介值与严格单调保证指数值域及逆映射存在，再推对数、一般底指数和正底实数幂的导数，保留底数与定义域条件。

#### 5.1.4 闭区间上可微函数的性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:441 -->

以闭区间连续、内点可导的条件联系局部变化与整段增量；按局部极值与驻点、中值定理、单调性、Lipschitz条件组织。Fermat与三个中值定理均正式陈述并证明；一阶导数判别法紧接Fermat陈述，明确其证明在单调性定理之后补出，避免循环。

##### 5.1.4.1 局部极值与驻点

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:446 -->

先定义邻域内极值，再用两侧差商证明内点可导极值必为驻点；紧接给出一阶导数符号判别及成立条件，说明充分性证明将在单调性建立后补出。

###### 段：局部极值

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:448 -->

区分非严格与严格局部极值，也区别邻域比较与整个定义域最值。

###### 段：Fermat定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:453 -->

正式写明区间内点、该点可导与局部极值条件，以及导数为零的结论；分别比较正负增量差商证明，补充驻点不一定是极值及端点不满足内点条件的反例。

###### 段：一阶导数判别法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:473 -->

正式陈述驻点左负右正得严格局部极小、左正右负得严格局部极大，明确邻域连续与可导条件；先解释先降后升、先升后降的含义，证明留到后面的单调性小节完成。

##### 5.1.4.2 中值定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:490 -->

先由闭区间最值与Fermat证明Rolle，再减割线证明Lagrange；将两函数端点增量组合成两端同值的辅助函数，证明Cauchy交叉形式，并单独核验比值形式的分母条件。

###### 段：Rolle定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:492 -->

用正式定理写明a<b、闭区间连续、开区间可导、端点同值及内部零导数点存在；恒定情形直接处理，非恒定时由最值定理和Fermat证明。

###### 段：Lagrange中值定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:511 -->

正式陈述内点导数等于整段平均变化率，保留原中值公式标签；证明构造减去端点连线的H并应用Rolle，注明不要求导函数连续。

增加割线与平行切线图，以平方函数核对c=1/2，区分平均变化率与瞬时变化率相等和直线位置相同。

###### 段：Cauchy中值定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:544 -->

在两个函数闭区间连续、内部可导的条件下正式给出交叉乘积等式；辅助函数消去端点值后用Rolle。若g′处处非零，另以Rolle排除g两端同值，再安全写为比值等式。

##### 5.1.4.3 单调性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:573 -->

放在中值定理之后，正式给出四种导数符号与单调性的充分关系及零导数推出常数；任取两点用Lagrange证明。随后回到前述一阶导数判别法，在驻点左右分别使用单调性完成证明，并以x³说明导数处处正不是严格递增的必要条件。

##### 5.1.4.4 Lipschitz条件

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:604 -->

独立小节用统一导数绝对值上界控制任意两点增量，正式陈述闭区间连续、内点可导和有限L的条件，由Lagrange证明；用平方函数L=2衔接连续性部分，强调不能跨定义域缺口，Lipschitz也不蕴含处处可导。

闭区间C1函数的导数有界，因而Lipschitz，再联系连续性蕴含链；绝对值函数说明Lipschitz不保证处处可导。

#### 5.1.5 高阶微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:631 -->

由反复求导记录更高阶变化，先定义二阶与高阶导数、C^r及高阶微分，再比较立方函数的二阶近似，以Taylor公式与余项控制一般误差。标题与段落按当前正文的既有编辑同步。

##### 5.1.5.1 高阶导数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:633 -->

先以导函数再次求导定义二阶导数，再递归定义高阶导数与C^r条件，最后解释高阶微分与有限增量、Taylor近似的区别。

###### 段：二阶导数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:635 -->

从斜率本身的变化引出导函数的导数，定义f″，为更高阶递归提供起点。

###### 段：高阶导数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:639 -->

递归定义f^(r)并约定零阶为原函数，给出C^r及闭区间内部导数延拓约定；说明高阶微分给变化系数，有限近似仍需Taylor系数和余项。

##### 5.1.5.2 二阶近似

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:645 -->

在原立方函数的相同基点与位移上加入3h²/2，比较二次模型与线性模型遗漏；以h=0.1时误差从0.016降为0.001及带符号余项图解释弯曲方向。

##### 5.1.5.3 Taylor公式

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:654 -->

从反复Rolle构造Lagrange余项，再降一阶推出Peano形式，区分有限位移数值界与局部误差阶。

###### 段：Lagrange余项

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:657 -->

构造消去端点和低阶导数的辅助函数，反复Rolle得到余项中间点；给导数界对应的误差上界及立方精确展开。

###### 段：Peano余项

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:689 -->

对低一阶Taylor应用Lagrange余项，再利用最高阶导数连续性减去基点系数，得到o(|h|^r)。

###### 段：二阶导数判别法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/03-continuity-differentiation.tex:697 -->

在C2驻点附近用二阶余项及导数连续保持符号，推出严格极值；二阶导数为零时以±x⁴和x³说明无结论。

### 5.2 集合的测量

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:1 -->

正文入口：[`04-set-measurement.tex`](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex)。在连续性与微分之后、积分之前，回到“集合有多大”的问题：距离作用于一对点，大小作用于一个集合，同一距离不唯一决定测度。本节先提出把区间长度推广到一般集合的问题，用有限加权计数说明有限可加规则，再从有限区间并的长度与一般集合的内外逼近得到Jordan测量，用有理点集说明有限覆盖的局限；再引入可数集，用可数覆盖定义勒贝格外测度，经Carathéodory分割条件选出可测集并证明可数可加性；最后抽象为测度空间，研究集合列、零测集、完备化与集合的逼近。

#### 5.2.1 有限集与Jordan测量

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:18 -->

先明确将区间长度推广到一般有界实数集合的问题，以两段不交区间说明有限可加性要求；有限计数与加权计数只用于解释相加规则，随后独立从区间长度构造初等集与Jordan内外容量，最后以有理点集暴露有限覆盖的局限。

##### 5.2.1.1 有限集的测量

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:29 -->

从元素个数扩展到每点非负权重，核对有限可加性，再区分集合大小与函数累计；通过两个区间的点数都无穷而长度不同，说明长度需要另行从几何区间构造。

###### 段：计数与加权计数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:31 -->

先说明每点计一与不同元素具有不同份量的两种需求，再定义非负权重之和；两点例子及每点恰进入一个不交分组的事实推导有限可加性。

###### 段：集合权重与函数值

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:50 -->

说明μ(A)只测量集合，在其上累计函数值还需乘点权重；沿用两点空间，通过等权与加权算例和表格区分元素个数、集合权重和函数累计，衔接后面的积分。

###### 段：点数与长度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:73 -->

明确这一段承担从计数转向区间长度的过渡：逐点计一使两个区间的点数都无穷，无法得到长度1与2；由区间长度规则得到单点长度零，有限可加性再给有限点集长度零。

##### 5.2.1.2 Jordan测量

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:83 -->

先用不交和重叠区间例子建立有限区间并的长度，通过共同端点细分证明表示无关；再用倒数点集说明有界不等于有限区间并，引出初等集内外估计与容量相等的可测条件，并完整计算倒数点集的Jordan测量为零。

###### 段：区间长度与初等集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:85 -->

说明有限区间并可先拆成互不重叠部分再求长，定义初等集及空集约定；以两段不交区间与重叠区间比较直接相加的条件，通过共同端点细分证明表示无关，并给一般有限覆盖的上界。

###### 段：内容量与外容量

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:107 -->

用E={1/n}⊂[0,1]说明有界只保证外部范围有限；由远离零的部分只有有限点证明E不含正长度区间，从而不是有限区间并。内部包含给下界、外部覆盖给上界，分别取上确界与下确界，二者相等才定义Jordan可测。用有限单点加[0,1/N]的外逼近完整算出倒数点集内外容量均零，说明定义确实超出初等集。

###### 段：有限逼近与可加性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:164 -->

将内外容量相等改写为任意小夹逼误差，以并、交、差的内外近似控制新误差；不交集合的内部近似可相加，结合外部上界推出Jordan有限可加性。

##### 5.2.1.3 Jordan测量的局限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:188 -->

承接倒数点集可用有限逼近得到长度零，转问所有有界集是否都能如此；用有理点集内外容量0和1说明失败来自有限覆盖本身，再提出逐点分配几何长度区间的可数覆盖方案及其编号前提。

###### 段：有理点集的内外容量

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:190 -->

先证明每段正长度区间都含有理和无理点，内部初等集因而只有有限点，容量为零；有限外部区间并补齐端点后必须覆盖整个单位区间，容量为一，有限逼近误差不能趋零。

###### 段：有限覆盖的限制

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:221 -->

任何有限个区间的完整覆盖都受总长度至少一的下界约束，区别于倒数点集可收拢尾部；若有理点可编号，则每点分配ε/2、ε/4等长度，总和可任意小，但必须使用一列完整覆盖而非某个有限前段，故先准备可数性。
以图对照有限覆盖与可数覆盖；标明仅画可数覆盖前四项，完整覆盖依赖全部区间，各段长度按几何级数分配，避免把任意有限前段误认成完整覆盖。


#### 5.2.2 可数集与勒贝格外测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:246 -->

从有理点集的有限覆盖障碍出发，以自然数编号配合非负级数控制总长度；可数并可数保证合并覆盖仍允许，非负双重和规则保证按组求和与统一列举一致，随后检验新区间估计既改进点集又保持区间长度。

##### 5.2.2.1 可数集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:256 -->

依次说明可数定义、整数与有理数列举、自然数对的对角列举、区间不可数和可数并可数，再以有限索引和的上确界证明非负双重级数合并，为覆盖证明准备工具。

###### 段：可数集的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:258 -->

区分有限、可数无限与不可数，以能列尽且可去重的序列解释一一对应定义，说明可数子集仍可数。

###### 段：自然数对与有理数的可数性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:272 -->

指出逐行无限列举无法到达下一行，改用坐标和分层列举自然数对；再列举整数分子与正分母并去重，证明有理数及有限可数笛卡尔积可数。

###### 段：区间的不可数性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:286 -->

假设列尽单位闭区间，选定无无限尾九的十进制表示，逐位取一或二构造遗漏点；再由线性缩放说明任意非退化区间不可数。

###### 段：可数个可数集的并

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:295 -->

先给每组成员编号，有限非空组用重复项补齐、空组跳过，再沿双指标对角线列举并去重，证明可数个可数集的并可数。

###### 段：非负双重级数的合并

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:304 -->

回用非负和的部分和上确界定义，将双指标总和写成全部有限索引集之和的上确界，双向证明它等于逐行求和，单独解释无穷行和情形，不借用积分换序。

##### 5.2.2.2 勒贝格外测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:332 -->

解释可数限制覆盖区间个数而非被覆盖集合点数，允许重叠与伸出；对覆盖总长取下确界，利用紧致性保留区间长度，再用逐点几何误差覆盖把可数点集外测度压至零，明确尚未建立不交精确可加性。

###### 段：可数区间覆盖

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:335 -->

由已证的有理点列举实施逐点覆盖，再推广到任意集合；区间数可数不要求集合可数，用非负级数累计并支持覆盖合并。采用开区间使紧致性可用于检验闭区间长度不变。

###### 段：勒贝格外测度的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:347 -->

单次覆盖可能伸出集合或重复覆盖，长度只给外部估计；取所有允许覆盖总长的下确界排除选择依赖。候选总存在、可为无穷、最优覆盖不必存在，保留有限与空覆盖约定。

###### 段：空集与单调性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:369 -->

用空覆盖核对空集赋零，由大集合的覆盖同时覆盖小集合证明外测度单调性，解释下确界方向。

###### 段：区间的外测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:376 -->

扩大覆盖候选可能降低下确界，须验证普通区间保持原值；略放大开区间给上界，任意可数开覆盖取有限子覆盖后用有限长度不等式给下界，再推广端点型式及无界区间。

###### 段：可数点集的外测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:390 -->

明确构造以第n点为中心、长ε2^{-n}的开区间，整个可数覆盖总长至多ε，从任意ε得到零；比较有理点集Jordan外容量一，解释与不可数区间正长度并不矛盾，并区分外部赋值与后续精确分割。

##### 5.2.2.3 可数可加性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:412 -->

从可数覆盖转向可数不交分割的目标等式；证明覆盖合并只能自动给次可加上界，三条一般外测度公理不包括反向不等式，由此引出可测集的精确分割要求。

###### 段：可数可加性的要求

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:414 -->

将有限不交分割推广到可数列，以可列举点集与单点长度的目标相容性说明用途；并集与各部分均须在赋值范围内，区间不可数，不能把全部单点当作可数级数相加。

###### 段：外测度的可数次可加性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:430 -->

先解释并集覆盖可以由各部分覆盖合并，因此得到无须不交的上界；近似最优覆盖未必达到下确界，故逐组分配ε2^{-n}并用可数并与非负双重和控制总误差，完整证明后令ε趋零。

###### 段：一般外测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:469 -->

> 【后移一般定义】“一般外测度”的任意集合版本移入第二部分“测度空间”；实轴勒贝格外测度的单调性、可数次可加性及“不等式尚非等式”的过渡保留在前一个现有 paragraph 中。

抽取空集赋零、单调性、可数次可加性；不交集合的区间覆盖仍可能重叠，按任意集合切分区间又未必留下区间，所以未得反向界。提出用集合精确切分任意测试集的相容性条件。

#### 5.2.3 可测集与勒贝格测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:494 -->

区分每个集合已有外测度值与是否能够精确参与分割两个问题；保留数值、以所有测试集的分割等式筛选范围，再证明范围封闭性以及限制后的可数可加性。

##### 5.2.3.1 可测性的要求

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:504 -->

将测试集分成集合内部与外部两块，指出次可加上界之外尚需反向界；完整核验一般两点外测度反例，并明确它不代替勒贝格不可测集构造。定义全体测试集上的精确分割，再直接验证零外测度的有理点集可测。

###### 段：精确分割

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:506 -->

> 【保留，限于实轴】保留实轴区间分割与精确分割的动机；两点集合上的一般外测度反例及相应图示分支后移。

固定待检集合A、任取测试集E，写出不交分解及已有不等式；两点空间非空子集统一赋一满足外测度公理却切分后总和变大，说明三公理不足，并区分一般公理反例与勒贝格具体构造。
以图并列区间的长度分拆与两点空间的一般外测度反例，明确一般公理允许分拆总和变大；区间示例不代替所有测试集的可测性检验，也不把有限图形充作勒贝格不可测集。


###### 段：可测集的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:537 -->

要求每个测试集都满足Carathéodory等式，解释只取E=A无法检验；任意集合已有m*值，可测性新增分割相容性。先正式证明零外测度集的任意子集可测这一通用引理，再将其用于Q0；再由单位区间分割得无理点部分外测度一，说明稠密性不决定长度。

##### 5.2.3.2 可测集族

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:575 -->

先以Jordan可测单点的可数并Q0不可Jordan测说明逐个可测不足以支持无限合并，再由精确分割证明取补、有限并和可数并封闭；由已证封闭性提炼σ代数，区分允许对象的范围保证与测量数值的精确可加。

###### 段：取补与有限并

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:584 -->

任意测试集下先验证空集，补集只交换分割两项；用A切分E再用B切分余部，解释次可加性如何给有限并所需反向界。由补、并得到交与差，并另行验证不交有限分割的精确加法，为可数过程准备。

###### 段：可数并

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:611 -->

不预用待证的无限可加性，先精确切出前N个不交集合，用单调性保留最终余部，再对非负部分和取上确界、用外测度次可加性合并，证明并集可测；一般集合列逐项去掉此前部分化为不交列。

###### 段：$\sigma$代数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:636 -->

> 【保留实轴所需内容】可沿用本 paragraph 标题；只说明实轴上的勒贝格可测集合族、Borel集合族及其可数运算封闭性。任意集合 X 上的正式 σ 代数定义和抽象比较后移。

由已证的全集、补集及可数并封闭性引出统一名称，定义后推空集、有限并、可数交，并以单点为邻域可数交说明无限运算用途。当前勒贝格族先由分割条件构造再证明为σ代数，抽象问题也可先指定σ代数；它只规定允许范围，不提供数值或数值可加性。

##### 5.2.3.3 勒贝格测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:667 -->

可测族的封闭性保证合并后仍是允许输入，限制外测度保留原数值；精确分割给有限部分和下界，结合次可加上界证明可数等式。随后确认区间等常用集合可测，解释Borel生成范围和Jordan构造的相容性。

###### 段：限制外测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:669 -->

区分m*的赋值职责与L(R)的范围职责，将定义域限制而不重算数值，定义m并核对Q0和空集原值；是否满足测度可数等式仍须后证。

###### 段：不交可测并的可数可加性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:685 -->

先说明σ代数保证左侧并集可测，精确分割使每个有限部分和不超过总量；正式证明对部分和取上确界后得到下界，与外测度次可加上界合为等式，区分对象封闭与数值可加两项作用。

###### 段：区间与常见可测集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:711 -->

可数等式只适用于已可测集合，故先从只需在一点切分区间的半直线验证Carathéodory条件；再由可数集合运算得到区间、开闭集，确认保留通常长度。

###### 段：Borel集合

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:740 -->

从区间和开集反复可数运算的需求提出最小范围；幂集提供候选，全部候选σ代数取交仍封闭，证明生成范围存在后正式定义Borel及相对Borel族。解释B(R)包含于L(R)来自后者是含开区间的σ代数，并区分集合族与赋值函数。

###### 段：Jordan测量与勒贝格测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:770 -->

检验每个Jordan可测集是否被保留且数值相同；回用已证的零外测度子集引理，再由Jordan内外逼近构造Borel夹逼并控制差集为零，得到可测性和测量值一致，Q0说明逆向不成立。

#### 5.2.4 测度空间与测度的性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:787 -->

> 【必要改名】本 subsection 拟由“测度空间与测度的性质”改为“勒贝格测度的性质”。保留下面的集合列、零测例外、实轴完备性及集合逼近；先抽象再应用的一般框架后移。

从已经建立的勒贝格长度与有限加权计数识别对象范围、允许集合族、具体赋值三层结构；分别抽象为可测空间、测度与测度空间，并将基本性质、集合列和零测例外统一从共同条件推出。关系图先回顾区间长度、外测度、精确分割与勒贝格测度的具体构造，再逐项对应一般的(X,A,μ)，明确抽象不改变已有m而是扩大适用对象；同一实轴可测空间上的长度与计数赋值不同，一般测度无需重做区间覆盖构造。图内仅保留构造节点、三项结构及对应箭头，测度公理、可测空间与测度空间的区别、单点赋值对照在图注中说明。

##### 5.2.4.1 测度空间

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:810 -->

> 【后移】本 subsubsection 及“可测空间”“测度”“测度空间”“计数测度”“点质量”“可数加权计数”六个 paragraph 整体移入第二部分。前面用于引出长度测量的有限计数示例保留。

先把对象X与封闭的允许范围A组成可测空间，明确尚无数值；以已证勒贝格等式为模型定义一般测度，再由三元组记录完整设定。用粗分块族、不同点权重及计数等例子说明允许范围与赋值可分别选择。

###### 段：可测空间

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:812 -->

对象集合之外还需指定对补和可数并封闭的允许范围。三点空间把a、b视作同一块、c单列，以块的各种并核查σ代数；{a}不在当前范围不代表天生不可测，改选幂集即可。区分相对于指定A的抽象可测与由精确分割得到的勒贝格可测。

###### 段：测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:831 -->

可测空间只保证操作后的对象仍在定义域；以已经证明的勒贝格可数可加性为模型，正式要求空集零、非负扩展实数值及不交可数精确相加，得到一般测度。

###### 段：测度空间

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:845 -->

同一可测范围仍可选择不同权重，因此用(X,A,μ)记录完整测量设定；两点空间的两种点权重给出不同总量但都可数可加。明确σ代数决定允许对象、测度决定大小，并写出勒贝格三元组衔接其他例子。

###### 段：计数测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:860 -->

在任意集合幂集上给有限子集赋元素个数、无限子集赋无穷，分别核对有限不交并与无限并的可数可加性。

###### 段：点质量

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:872 -->

固定一点，以集合是否包含该点赋零或一；因为不交集合族中至多一个成员包含它，得到点质量测度并给出两组具体计算。

###### 段：可数加权计数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:880 -->

将有限逐点权重扩展为非负级数，用有限索引和的上确界保证不交分组可数相加；比较几何权重与单位权重，与勒贝格长度的构造方式区别。回到三层结构，说明后续统一从共同测度条件推性质。

##### 5.2.4.2 基本性质与集合列

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:893 -->

> 【保留，限于勒贝格测度】本 subsubsection 与四个现有 paragraph 全部保留；对象改为实轴勒贝格可测集与长度测度 m。递减集合列的有限测度条件必须保留。

从测度只直接规定不交可数并出发，将包含与重叠转为不交分割，推出单调性与次可加；再把递增过程分成不交增量，得到下连续性，将递减过程改为有限总量中的递增补集得到上连续性，突出相减与尾部控制的有限性条件。

###### 段：单调性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:901 -->

包含的大集合拆成小集合与可测差集，非负可加性给大小比较；有限总量时才能相减计算余量，明确不可使用∞−∞。

###### 段：次可加性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:911 -->

重叠集合逐项去掉已出现的部分，按不交化与单调性给并集上界；由此证明可数零测并仍零测，为共同例外范围作准备。有限测度时再给容斥公式，说明减去重复部分的条件。

###### 段：递增集合列

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:930 -->

以逐步加入范围的用途引出并集测度能否取极限的问题；可数并封闭保证对象可测，不交增量与非负部分和上确界给测度等于sup及极限，允许无穷值，以开区间例子检验。

###### 段：递减集合列

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:946 -->

逐步去掉范围得到交集；以有限测度首项为相减起点，把已去掉部分转为递增列，推出inf及极限。某一步有限即可舍去前项；无穷射线移向远处的例子说明数值全为∞时不能恢复空交集，保留原对照图。

##### 5.2.4.3 零测集与完备性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:974 -->

> 【保留实轴版本】本 subsubsection 保留；零测、几乎处处、Cantor集和零测子集的可测性均是实数积分的必要内容。一般未完备空间及更换测度的对照例子后移。此处测度的完备性指零测子集可测，不是柯西完备性。

由测度为零但仍可能有例外点的范围，分别引出零测集、几乎处处和例外子集的可测资格；用不可数Cantor零测集区分点数与测度，再用三点不完备例子及最小完备化构造补齐资格，衔接后面Borel与勒贝格关系。

###### 段：零测集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:981 -->

从单点存在却勒贝格长度零的现象引出正式定义，可测且测度零两项均明确；以可数零测并及计数测度单点为一说明零测性依赖具体测度。

###### 段：几乎处处

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:993 -->

比较函数不只看是否有不同点，还看不同位置是否落在零测范围内。正式以可测零测集包住全部例外定义a.e.；单点改值与有理点指示函数说明例外可稠密且不保连续性。可数个a.e.结论可合并共同零测例外，不可数族反例限定范围；实际例外集无需预先可测，进而引出完备性。

###### 段：Cantor集

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:1014 -->

用零测是否必可数的问题引入三分删除构造，证明Borel且各层长度(2/3)^n迫使零测；零一序列到三进制0、2数字的单射及对角法证明不可数，说明零测例外不能用除去可数点替代。

增加康托尔删除过程图，区分每个有限阶段的正长度与交集的零测度，说明零测不等于空集。

###### 段：完备性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:1037 -->

> 【保留，限于勒贝格测度】保留原标题；说明勒贝格零测集的任意子集仍可测且零测。一般测度空间的完备性定义及三点反例后移，不删掉实轴结论。

若零测子集可测则单调性自动给值零，真正缺口是它可能不在σ代数中；正式定义完备性，区别度量完备。三点空间中{a,b}零测而{a}不被允许，性质x≠a仍a.e.成立但尚不能给{a}写测度值，说明补齐资格的用途。

###### 段：完备化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:1052 -->

> 【后移】本 paragraph 的任意测度空间完备化构造及证明移入第二部分；勒贝格测度已经包含零测集全部子集的特定结论在本地保留。

从补齐零测子集且保留旧值的目标出发，为保持σ代数还须加入A∪D形式，正式给新范围和赋值。依次验证表示无关（不用无穷减法）、取补及可数并封闭、可数可加性继承与新零测子集均已纳入；证明任何完备扩展都包含这些集合，说明最小性；勒贝格已完备直接回用零外测度子集引理，不另证明一次。

##### 5.2.4.4 集合的逼近

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:1101 -->

由已知集合列的并交反问能否为给定集合构造简单近似；回到具有区间覆盖与拓扑的勒贝格测度，区分一般测度公理与额外正则性。先按多出、漏掉的测度内外逼近，再用对称差放宽为有限区间并近似，最终由近似构造解释Borel完备化等于勒贝格范围。

###### 段：内外正则性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:1109 -->

正式陈述有限测度E可由开集外包、有界闭集内含且各误差任意小；例子说明误差是集合差测度而非边界距离。外逼近由近似最优开覆盖和有限相减得到，内逼近先用下连续性控制远处尾部，再外逼近有限区间中的补集，分配两份误差。实轴全体的反例说明有限性与有界内近似不可省，建议一般集合先局部处理。
以同尺度区间图给E、闭集K和开集O，明确多出与遗漏对应两种集合差；孤立点必须外包但遗漏其本身无测度损失，具体数值示例与任意小误差定理分开。


###### 段：有限区间并

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:1161 -->

有限测度E先开外近似，再将有限测度开集列成有理端点区间并，以递增连续性截取有限前段；分别控制遗漏和多出，定义对称差并得其测度小于ε。明确不要求内含或外包，Q0可用空集作零误差近似，因不构成外部覆盖而不违背Jordan外容量一；函数积分误差另需控制。

###### 段：Borel范围的完备化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/04-set-measurement.tex:1183 -->

> 【保留实轴特定结论】保留标题，表述为每个勒贝格可测集与某个Borel集只相差Borel零测集的一个子集；不依赖前文已后移的一般完备化构造。

先为有限测度E选择内部闭近似，其可数并给Borel部分F，余量测度零；再用小测度开覆盖的交构造Borel零测包络N，写E=F∪D、D⊂N，恰为完备化形式。一般E按有界截断处理再合并；反向用勒贝格完备性，双向证明范围恰好一致且保留原Borel长度。

### 5.3 一元函数的可测性和积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1 -->

> 【本节全量保留层级】本文件的 section、subsection、subsubsection、paragraph 标题与顺序全部保留；内容统一在勒贝格可测 E⊂R 上陈述，测度固定为 m 或 dx。三大收敛定理的证明、反例和交换运算的条件完整保留，不以删减推理实现实数化。

从区间取样的局限引出可测原像与勒贝格积分，定义后集中证明积分性质及与黎曼积分的一致性。基本定理按导数的积分、积分的导数组织；从运算法则起后续积分统一采用勒贝格定义。函数列先区分收敛方式，再分别研究连续、微分和积分的保持条件；函数项级数另以部分和、收敛判别及逐项运算独立组织；无穷范围和无界函数先定义，再用截断累计判据处理可积性。

#### 5.3.1 黎曼定积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:19 -->

以常数密度乘区间长度为起点，沿输入区间有限分段取样，以全部细分与取样的共同有限极限定义累计。上下和将此要求改写为误差条件，连续及有限间断函数说明可行范围；狄利克雷函数表明短区间取样仍可分歧，促使改用可测取值集合。

##### 5.3.1.1 积分的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:26 -->

沿有限区间分割与取样建立黎曼和，以全部足够细分割及任意取样的共同有限极限定义积分；再区分积分值、积分变量及有向端点约定，不预先定义原函数与累计函数。

###### 段：区间分割

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:31 -->

定义有限分割、各段长度和最大段长，说明细度趋零要求每段都缩小，不能仅增加点数。

###### 段：黎曼和

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:38 -->

在各段选取样点，以函数值乘长度后求和；非负时对应矩形面积，有负值时按符号累计。

###### 段：黎曼积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:45 -->

要求所有足够细分割及任意取样同时接近同一有限数；以常数函数验证定义，后用上下和判断共同极限。

###### 段：定积分与积分变量

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:58 -->

区分积分值、上下限及哑变量，规定反向和相同端点；说明勒贝格定积分同样给定范围数值但可积要求不同。

##### 5.3.1.2 可积性的要求

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:61 -->

用上下和将所有取样的共同极限改写为可检验的振幅误差，证明Darboux判据及其与黎曼定义的等价；给出连续、有限间断等充分条件，并从定义提前建立子区间可积与累计估计。

###### 段：上和与下和

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:66 -->

用每段上确界和下确界同时包住所有取样和，有界未必取到最值因而不能用最大最小代替。

###### 段：Darboux判据

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:78 -->

公共加细使任意下和不超过任意上和；证明上下积分相等与小差分割等价，再估计跨固定分割点的短段，连接到任意细黎曼和定义。

###### 段：连续函数的可积性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:91 -->

闭区间有界且一致连续提供全域共同尺度，以每段振幅乘长度之和控制上下和差。

###### 段：有限间断点函数的可积性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:99 -->

用总长度很小的区间包住有限例外，余下有限闭区间上应用一致连续，证明有界有限间断函数仍黎曼可积。

###### 段：区间分拆与基本估计

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:103 -->

在FTC之前从上下和证明限制到子区间仍可积，从合并黎曼和取得区间加性，给线性和有界值对应的积分估计，避免循环调用后面的运算结论。

增加上下和夹住积分的加细过程图，按同一函数与两种分割核对U_n-L_n=1/n，回接Darboux判据。

##### 5.3.1.3 黎曼积分的局限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:119 -->

用同一狄利克雷函数比较两种累计依据：细分输入区间时上下和始终相差一，按两个取值集合的测度累计却可得到零。再以有限集指示函数递增到该函数，说明黎曼可积类在非负单调极限下不封闭；新定义须同时扩大范围与保留旧值。

###### 段：狄利克雷函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:124 -->

Q0在每段内与其补集都非空，全部有理或无理取样分别给一与零，细度趋零仍无共同极限。前节证明Q0零测，因而按取值乘测度应得零；列举Q0并取前n点指示函数，每项黎曼可积且积分零，而递增极限不黎曼可积，明确单调极限的范围障碍。

#### 5.3.2 勒贝格定积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:146 -->

> 【保留，限于实轴】可测函数、简单函数、非负和有符号积分、可积性及各项性质均保留，去掉任意 (X,A,μ) 的前置设定；同一两点集合更换 σ 代数的例子后移。一般可测空间之间的复合框架后移，本地保留实际需要的实函数复合结论及其边界。

先以可测原像保证取值分层资格，经简单函数和下方上确界定义非负积分，再作正负分解与绝对可积规定；新增独立的积分性质小节，分别正式陈述并证明非负线性、有符号线性比较、零积分判别和区域可数可加性。随后证明与黎曼积分的一致性和间断点零测判据，明确有限、无穷与零测修改的边界。

##### 5.3.2.1 可测函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:157 -->

为按取值分层累计，先要求输出Borel集合的原像可测；说明测度作用在输入原像而非输出数值。射线生成Borel结构给阈值等价条件，连续及狄利克雷例子划分范围，再验证运算与复合的结构条件，可测性本身不保证积分有限。

###### 段：可测函数的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:163 -->

从测量阈值以上输入引出Borel原像条件，显式写出输出集合到输入原像再到测度的关系；原像保持补和可数并，故射线条件足够。取值档与狄利克雷四类原像给具体解释，不可测集合的示性函数说明缺少分层资格时不能直接赋予测度；有限空间例子说明可测性依赖指定σ代数，并区分分层资格与有限总量。

###### 段：连续函数与可测函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:190 -->

连续函数的开集原像为开集，因而Borel可测，在更大勒贝格结构下仍可测；狄利克雷函数说明逆向不成立。

###### 段：可测函数的运算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:194 -->

以有理阈值可数并证明和可测，借连续标量复合得到平方、绝对值和乘积；商及一般复合明确中间可测结构与无穷运算限制。

##### 5.3.2.2 积分的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:204 -->

以有限可测块定义简单函数积分，再由下方非负简单函数积分的上确界定义非负积分；给规范截断和二进制舍入逼近，最后正负分解定义有符号积分并排除∞−∞。积分运算的定理及证明统一放到后面的独立小节。

###### 段：简单函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:209 -->

有限取值可测函数在不交取值块上按函数值乘测度求和，公共交集细分及有限可加性证明表示无关。示性函数的积分等于集合测度，说明测量集合是函数积分的特例；狄利克雷积分零由此直接得到，并澄清不使用不可数单点求和。
用同一抛物线对照区间取样与取值分档；一档原像可有两段，测度作用在这些输入段上，有限档取下界并不等于已经取完积分极限。

###### 段：非负勒贝格积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:241 -->

一般非负可测函数不能直接用有限和累计，以下方简单函数给出的总量为下界，取其上确界定义积分，可为无穷。说明子集积分与dx记号，线性函数阶梯及平方函数图示给有限近似，不在这里预设一般极限交换。

###### 段：可测函数的简单逼近

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:265 -->

只加细网格仍可能无限取值，只截断高度仍可能连续取值，因此同时截断到n并向下舍入至二进制网格；逐项验证有限取值、可测、递增和点态逼近。这里不先断言积分收敛，后由单调收敛定理完成。

###### 段：有符号勒贝格积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:278 -->

拆分正负部分，在二者积分不同时无穷时定义差值；保留单个无穷值，禁止∞−∞。

##### 5.3.2.3 可积性的要求

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:287 -->

以绝对值积分有限定义有限的有符号可积性，正负两项分别被绝对值控制；讨论有限总量的必要要求、有界与有限测度的充分条件和总量归一化。等价判别和线性证明留到下一小节，不在定义处混入性质定理。

###### 段：有限积分的条件

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:303 -->

区分非负积分有定义与有限、有符号积分有限与正负两项均有限，绝对值积分等价判别由下一性质小节证明。有限测度上有界可测给可积充分条件，无穷范围上的常数一及无界可积幂函数说明边界。

###### 段：积分与平均值

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:309 -->

> 【保留，限于实轴】标题保留；在 0<m(E)<∞ 时用 (1/m(E))∫_E f dm 说明平均值，更换两点测度的例子后移。

同一两点函数在权重一、二的测度下累计为一、绝对累计为五，归一化平均为三分之一；改用勒贝格测度积分为零，说明累计规则由测度决定。平均值要求总测度有限且非零，零测范围不可再作归一化。

##### 5.3.2.4 积分的性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:315 -->

从已定义的积分出发，先用简单函数及集合测度递增连续性证明非负线性与a.e.单调、不变性；正负分解给有限有符号线性和估计。再证明非负零积分等价于a.e.为零，以及直接从测度可数可加性推出区域可数可加性和有限容斥，全程不调用后面的函数列收敛定理。

###### 段：非负积分的基本性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:321 -->

正式定理规定非负可测函数的非负线性、a.e.单调与可测零测修改不变性，允许无穷并保留0·∞约定。完整证明用下方简单函数集合包含、零测块积分零，以及规范简单逼近的达标集递增与测度下连续性；证明与后面的MCT独立。

###### 段：有符号勒贝格积分的性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:364 -->

正式定理规定绝对可积等价于正负两项均有限、有限实线性、a.e.比较、绝对值界及可测a.e.修改不变性。证明先确认非负可积差分解无关，再核对和可积并推出线性与估计，所有移项只涉及有限数。

###### 段：零积分与零测例外

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:400 -->

非负函数无抵消，正式证明积分零当且仅当a.e.为零：以阈值1/k的集合控制测度，再可数并得到正值集零测。绝对值积分的对应结论用于有符号函数；x在对称区间积分零的反例说明不能省去非负或绝对值条件。

###### 段：积分范围的可加性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:419 -->

正式陈述非负函数对不交可测并的积分可数可加，允许无穷；有符号绝对可积时级数绝对收敛，并给有限并交容斥和差集公式。正向用有限部分和比较，反向把下方简单函数按区域分拆并用测度可数可加性，随后正负分解，不预用MCT。

##### 5.3.2.5 与黎曼积分的关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:457 -->

先正式陈述并完整证明有界黎曼可积蕴含勒贝格可测可积且数值相同，再以局部振幅和闭阈值集证明黎曼可积当且仅当不连续点集零测。区分保留数值与扩大可积范围，零测修改区分积分数值不变与黎曼可积性可能失效。

###### 段：黎曼积分与勒贝格积分的关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:462 -->

以正式一致性定理规定有限闭区间、有界黎曼可积及同值结论，狄利克雷函数排除逆向。证明取互相加细分割构造上下简单函数包络，差的积分为零推出包络a.e.相等，勒贝格完备性保证夹于其中的f可测；有界有限测度保证可积，再以同一上下和夹出数值一致。

###### 段：黎曼可积性的测度判据

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:493 -->

正式定理给有界函数的间断点集可测且黎曼可积iff该集零测。先定义局部振幅，振幅阈值集为闭集，间断集为其可数并。必要性用上下和误差控制阈值集覆盖长度；充分性用开集包住紧零测阈值集，其余点取小振幅邻域，直接回用度量一节已证的开覆盖共同尺度，再控制Darboux误差；双向证明均保留，覆盖尺度的同一反证不再重写。

###### 段：零测集上的改值

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:531 -->

直接引用积分性质中已证的零测改值结论，不再从简单函数重做；勒贝格完备性保证任意有限实值零测修改仍可测，一般未完备空间必须另查。零函数有理点改一破坏黎曼可积性，区分几乎处处连续与几乎处处等于连续函数。


#### 5.3.3 不定积分和变上限积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:540 -->

将求原函数产生的函数族与定积分上端点变化产生的累计函数分开定义，避免从记号预设基本定理。

##### 5.3.3.1 不定积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:545 -->

从原函数定义及中值定理得到区间上全部原函数只差常数；它表示函数族，不是定积分数值，分离区间可有不同常数。

###### 段：原函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:550 -->

寻找导数处处等于给定函数的可微函数，先只依赖求导关系，以平方原函数为例，不预设由积分获得。

###### 段：不定积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:553 -->

从原函数定义及中值定理得到区间上全部原函数只差常数；它表示函数族，不是定积分数值，分离区间可有不同常数。

##### 5.3.3.2 变上限积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:556 -->

分别由黎曼可积与勒贝格可积函数构造变上限累计，说明上限变量与积分哑变量、子区间累计差和有限性；在共同可积范围两类累计一致，可导性与函数恢复留给基本定理。

###### 段：变上限积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:561 -->

固定下端点、让上端点变化得到累计函数，区分积分变量与自变量；分别定义黎曼及勒贝格版本，其可导性由后面的基本定理决定。

###### 段：变上限勒贝格积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:568 -->

绝对可积保证每个子区间累计有限，区间拆分给累计差的积分表示；黎曼可积时两类累计一致，一般可积时不承诺处处可导。

##### 5.3.3.3 原函数与累计函数的关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:571 -->

指出二者的定义来源不同，连续函数时由经典FTC相连，仅勒贝格可积时一般只能几乎处处恢复；阶跃提示不存在处处原函数的边界。

#### 5.3.4 微积分基本定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:575 -->

直接分成两个问题：先给G，导数积分何时恢复端点差；先给f，累计函数求导何时恢复点值。第一问以导数黎曼可积统一包含C1特例，再比较绝对连续与过弱a.e.条件；第二问比较连续点的黎曼恢复与勒贝格点的a.e.恢复。一般AC正向与Lebesgue微分定理明确引用，其余局部推导和累计绝对连续性给完整证明。

##### 5.3.4.1 导数的积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:583 -->

统一陈述导数黎曼可积时的Newton–Leibniz，以C1为特例，仅保留一次中值定理求和证明；先用Cantor函数说明连续、a.e.可导且导数可积仍不足，再引出控制短区间总变化的绝对连续条件，引用一般导数可积与恢复结论。Lipschitz经AC给可用充分条件与Rademacher结论。

###### 段：黎曼可积导数的基本定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:588 -->

正式陈述G闭区间连续、内点可导，导数有黎曼可积延拓g时的端点公式。完整证明用各段中值表达、端点相消和g的任意细取样极限，不要求导数连续，端点有限赋值不影响积分；C1情形由连续函数黎曼可积直接得到，不再另证同一求和过程。

###### 段：康托尔函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:612 -->

先回用集合测量中Cantor集已证的零测性，再用保留三分支决定0/2三进制位，再映为0/1二进制和并在删去区间常值延伸；首次不同二进制位与后续几何尾和比较，证明非减与删区间端点同值，有限层振幅估计直接证连续；导数a.e.为零但端点差1，保留区间增量总和说明不AC。

###### 段：绝对连续函数的导数基本定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:630 -->

在导数积分问题中正式陈述AC保证a.e.导数存在、可积并恢复全部区间增量，保留表示公式和语义标签。这一一般测度论方向明确为引用，不将后面累计⇒AC的初等证明充作AC⇒导数恢复证明；与第二问结合后再收拢等价关系。

###### 段：局部Lipschitz连续函数的导数基本定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:646 -->

以Lipschitz作为能保证a.e.导数存在与闭区间恢复的充分条件；正式定理给局部Lip函数a.e.有限导数及导数上界，存在性依赖前面引用的AC结论，紧区间Lip经AC给a.e.可导；用含于Lip邻域的有理端点闭区间组成可数覆盖并合并零测例外，最后由差商得到导数界。定理后紧接这一证明，不另设重复的证明段落。

##### 5.3.4.2 积分的导数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:663 -->

按被积函数的条件分三种情况：黎曼可积时在连续点恢复，局部勒贝格可积时借勒贝格点在几乎每一点恢复，整个闭区间勒贝格可积时进一步得到全区间绝对连续性。各情形明确累计下限、定义域与结论边界，避免将几乎处处恢复误写为处处恢复。

###### 段：黎曼可积函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:668 -->

正式定理给黎曼可积函数的累计在每个连续内点导数等于被积函数，端点对应单侧；全区间连续则累计连续可微。以短区间平均误差证明，再由间断点集零测得到几乎处处恢复；阶跃反例说明不能普遍加强为处处可导。

###### 段：局部勒贝格可积函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:689 -->

定义开集上每个紧子集绝对可积，正式陈述并明确引用Lebesgue微分定理，定义勒贝格点。固定同一开区间内的下限，紧区间可积保证累计有限；差商误差由对称平均绝对差的两倍控制，证明每个勒贝格点处恢复，从而几乎处处恢复。用1/t说明局部可积不能保证定义域边界处累计有限。

###### 段：勒贝格可积函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:721 -->

在整个闭区间绝对可积时，正式定理给累计函数全区间绝对连续，以及勒贝格点处与几乎处处的导数恢复。简单函数下方近似先建立小测度集合上的统一积分估计，再控制有限不交区间的总增量以证明绝对连续；导数直接回用局部情形。结合前一问得到绝对连续与常数加L1累计表示等价，狄利克雷函数说明零测点值不能普遍恢复。

增加被积函数短区间面积与累计函数增量的对应图，同一端点和数值核验积分恢复；区分有限平均值与求导极限。

在勒贝格可积函数的累计结论之后，以一处公式收束绝对连续与可积函数变上限积分表示的等价关系；两个方向分别回用已有基本定理，保留狄利克雷函数说明点值不能处处恢复。

#### 5.3.5 积分的运算法则

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:767 -->

统一采用勒贝格积分，绝对可积保证有符号有限运算。基本运算分函数线性、范围分拆和误差界；换元使用微分同胚与绝对导数，另外解释有向端点；分部积分直接用AC乘积与端点恢复，并导出Taylor积分余项。

##### 5.3.5.1 积分的基本运算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:773 -->

回用已证勒贝格积分定理，将和、差、数乘与乘积的区别、不交范围、重叠范围、差集、区间分拆与方向、比较、绝对值界和误差估计逐段展开；每段写明条件、公式与推导依据，移项前检查绝对可积。

###### 段：和的积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:778 -->

同一测度和范围上两函数可积，绝对值上界保证和可积，再用已证线性定理给积分等于两积分之和，可反向合并。

###### 段：差的积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:786 -->

先以绝对值和控制差的绝对值，再写差的积分等于有限积分相减，排除无穷减无穷。

###### 段：数乘的积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:793 -->

固定实常数可移出可积函数的积分，零常数时两侧均零。

###### 段：积的积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:800 -->

一个因子可积、另一可测因子几乎处处有界时，用绝对值上界保证乘积可积；x与自身相乘的例子否定积分乘积公式，区分乘积与线性。

###### 段：不交范围的积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:804 -->

固定函数，将两个可测不交区域的累计相加得到并集累计，区分区域可加性与函数加法的线性。

###### 段：重叠范围的积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:812 -->

并集积分用两个区域积分之和减去交集积分；以差集与交集组成的三个不交部分推导容斥式。

###### 段：差集上的积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:821 -->

对可测B包含于A且函数在A上可积，利用A分成A\B和B的不交并，推出差集积分等于两积分相减。

###### 段：区间的分拆与方向

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:828 -->

勒贝格零测端点不影响区间积分，给中间点拆分公式；另交代一元有向上下限和相同端点零积分的约定，区别普通集合积分。

###### 段：积分的比较

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:836 -->

两可积函数几乎处处有序时，其差非负，非负积分和线性给出积分有序。

###### 段：积分的绝对值界

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:843 -->

从-|f|≤f≤|f|及比较得到积分绝对值不超过绝对值积分，条件保证两侧有限。

###### 段：积分的误差估计

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:850 -->

将绝对值界用于函数差，控制两积分之差；有限总测度与共同点值误差进一步给出误差乘总测度的界，承接极限与积分。

##### 5.3.5.2 换元积分法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:859 -->

固定勒贝格积分体系，用变量变换改变函数表达、以绝对导数改变长度权重；先陈述非负和可积函数的微分同胚换元，再在可积像区间说明有向端点写法。

###### 段：可测函数的换元公式

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:865 -->

正式陈述开区间C1微分同胚下非负可测换元允许无穷，绝对值换元给有符号可积性的等价，再拆正负部分得到有限公式。一般集合到函数的测度论证明仍明确引用。

###### 段：有向区间的换元

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:880 -->

在紧子区间及可积像范围上，普通像区间使用绝对导数，有向端点使用带符号导数；T=2x的平方函数例子核对权重与8/3的积分值。

##### 5.3.5.3 分部积分法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:892 -->

绝对连续是直接采用的条件，连续可微仅为特例。由AC乘积、a.e.乘积求导和端点恢复给勒贝格分部公式，并保留Taylor余项推导。

###### 段：分部积分公式

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:898 -->

正式定理陈述两AC因子的乘积仍AC、有界因子乘可积导数可积及端点公式；用有限不交区间增量估计证明乘积AC，再积分乘积导数。xe^x例子保留端点，无穷范围需另查绝对可积与边界极限。

###### 段：Taylor公式的积分余项

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:927 -->

沿位移参数化后迭代分部积分推导积分余项，全部使用勒贝格积分；高阶导数连续保证可积，给导数界与立方函数算例，正负位移统一处理。

#### 5.3.6 函数列的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:956 -->

> 【保留，固定勒贝格零测例外】函数列全部既有层级保留；几乎处处收敛与量词在实轴上说明，一般未完备空间和一般度量空间函数列的推广后移。

先区分点态、一致及几乎处处收敛，并分别给点态与一致柯西判据；再研究连续性、微分和积分的保持条件。一般函数列结论集中在这里，函数项级数的部分和、收敛判别及逐项运算另设下一小节。

##### 5.3.6.1 函数列的收敛方式、判别与关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:965 -->

对比逐点稳定、全域共同稳定与固定零测例外；点态与一致收敛各有柯西判据，以实数完备性保证未知极限存在，量词次序区分两个结论。

###### 段：点态收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:971 -->

固定每个输入后按数列极限定义，开始下标可依赖输入，定义不要求输入集合另有距离。

###### 段：点态收敛的判据

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:993 -->

正式陈述每个输入分别满足实数柯西条件当且仅当存在有限点态极限。证明固定输入后应用实数柯西准则，尾部起点可依赖输入，不提供全域共同下标。

###### 段：一致收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1012 -->

同一N控制全部输入，等价于上确界误差趋零；定义旁给一致柯西判据，量词比较及x^n的完整逆向检验集中在后面的条件关系中。

###### 段：一致收敛的判据

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1039 -->

正式给实值函数列存在一致极限iff全域两后项误差一致小；必要性用三角不等式，充分性逐点用实数完备性构造f，再固定后项让另一指标趋极限取得统一界。无需各函数有界，有界时极限也有界作为补充。

###### 段：几乎处处收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1059 -->

先固定一个可测零测例外，再在补集点态收敛；可数例外可合并，不可任意丢弃正测度区域，未完备空间仍需核对可测性。

固定同一非空测度空间、可测函数列与指定极限，比较一致误差、逐点尾部起点、共同零测例外；将函数性质比较转为函数列的收敛比较，保持积分所用测度明确。

###### 段：蕴含关系与量词

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1081 -->

正式给出一致收敛蕴含点态收敛、再蕴含几乎处处收敛，正向关系不要求有限测度。证明以共同N控制每个点和空例外集完成；零测例外若按n出现可用可数并统一，函数项级数对部分和适用同样关系。

###### 段：点态收敛不保证一致收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1103 -->

单位闭区间上的x^n点态趋向单点指示函数，但一致误差上确界恒一；改以零函数为指定极限时只几乎处处收敛。两个极限几乎处处相等而逐点不同，明确量词与代表元的区别。

增加幂函数列与线性缩小函数列的误差带对照，固定点态极限代表元并解释靠近边界的坏点可随n移动，共同1/n界才给一致收敛。

###### 段：几乎处处收敛不保证点态收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1131 -->

n倍原点指示函数在零测集外恒零，在原点却无有限极限；逐项改原点为零后得到另一列一致趋零函数，说明零测改值保留积分而未必保留实际函数列的点态或一致收敛。

##### 5.3.6.2 极限与连续

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1137 -->

以三项误差控制证明连续函数的一致极限连续，局部一致可逐点应用；x的n次幂说明逐点收敛不足，也不能从连续极限反推一致收敛。函数级数材料移至独立小节。

###### 段：连续函数的一致极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1142 -->

正式定理与三项epsilon/3误差证明共同近似保连续；回用已计算的x^n闭区间点态极限说明连续性丢失，半开区间上的连续零极限再排除连续极限反推一致收敛。随后解释局部一致的相对邻域版本。

##### 5.3.6.3 极限与微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1164 -->

函数值一致收敛可能伴随高频导数或尖点极限；连续可微函数列导数一致收敛加单点值收敛给连续可微一致极限，绝对连续函数列导数的绝对积分误差趋零则给绝对连续极限及几乎处处导数。

###### 段：一致收敛与导数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1169 -->

sin(nx)/n一致趋零但导数不趋零；平滑绝对值一致趋不可导极限，移动点说明导数收敛仍非一致。

###### 段：连续可微函数列导数的一致收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1179 -->

导数一致收敛加一个基点值收敛，经中值估计得到函数列一致柯西，再控制差商证明极限导数；常数竖移说明基点条件不可省。

###### 段：绝对连续函数列导数按积分误差的收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1209 -->

正式定理设fn为AC、某基点值收敛、导数到可积g的绝对误差积分趋零，则fn一致趋于c加g的累计，极限AC且导数a.e.等于g。证明用FTC将所有点误差统一控制为基点误差加导数误差积分，明确不承诺C1。

##### 5.3.6.4 极限与积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1231 -->

先确认极限可测，并以等面积窄峰否定仅点态条件。按有限测度一致收敛、非负单调递增、非负下极限估计、共同可积支配四种条件说明积分关系，保留相应正式定理与证明；简单函数与截断逼近移至反常积分，逐项积分集中移至函数项级数。

###### 段：可测函数的逐点极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1236 -->

可数上确界和下确界的阈值集合仍可测，尾部上、下确界给limsup/liminf，故存在的点态极限可测，区别于连续类。

###### 段：逐点收敛的反例

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1245 -->

同一三角峰支撑缩小，两列高度分别一与2n，均处处趋零但勒贝格积分分别趋零与恒一；并非被积资格丢失，而是点态控制不能控制总面积。

###### 段：有限测度上一致收敛下的积分极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1268 -->

> 【保留原标题与论证】将“有限测度范围”具体写为勒贝格可测 E⊂R 且 m(E)<∞；无限长度范围上一致收敛不足的实轴反例继续保留。

正式定理假设总测度有限、各项可积且一致收敛，先由固定后项加共同误差确认极限可积，再将误差积分控制为总测度乘上确界误差。实轴上n倒数乘[0,n]示性函数一致趋零却积分一，说明有限测度不可直接删除。

###### 段：非负可测函数列的单调递增收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1291 -->

> 【重点保留】本 paragraph 的单调收敛定理、证明和允许无穷积分的边界完整保留，仅将陈述限于实轴勒贝格积分。

任意下方简单函数按固定比例c的达标集递增耗尽，利用测度连续性逼近其积分，再取c趋1和简单函数上确界；允许无穷且不要求可积支配。 有限有理点集示性函数与正半轴区间示性函数分别说明零积分保持及允许无穷总量，不另设示例段落标题。

###### 段：非负可测函数列的下极限与积分估计

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1322 -->

> 【重点保留】本 paragraph 的 Fatou 引理、证明、非负条件及尖峰反例完整保留，固定为实轴勒贝格积分。

尾部下确界形成非负递增函数列，先用MCT后比较尾部积分下界；先定义积分恒一的正矩形尖峰g_n，再取其相反数说明非负性不能省，共同可积下界是可行推广；同一g_n供后图使用。 标题明确只给下极限积分关系，不额外要求函数列已经收敛。

###### 段：共同可积上界下的收敛与积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1351 -->

> 【重点保留】本 paragraph 的支配收敛定理、共同可积支配条件、证明及积分误差结论完整保留，固定为实轴勒贝格积分。

共同L1绝对上界保证极限可积，对g±f_n分别用Fatou夹出积分极限，再对误差用已证结论得到L1收敛，统一可数零测例外。 保留常数支配的幂函数、低峰、高峰无共同可积支配的完整小集合积分估计及移动指示函数的应用；小节末只比较连续、微分、积分的条件，不重复计算同一幂函数或矩形尖峰。

#### 5.3.7 函数项级数的极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1418 -->

把不断增加函数项的部分和视为函数列，先区分收敛方式，再以点态和一致尾和判据及Weierstrass判别保证收敛，最后分别判断求导与积分能否逐项进行。

##### 5.3.7.1 收敛方式与判别

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1425 -->

明确所有收敛方式约束的是部分和函数列；分别说明点态、一致、几乎处处与绝对收敛，避免将单项趋零误作级数收敛。

###### 段：点态收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1429 -->

对每个输入要求有限部分和有有限极限，将其定义为和函数；尾部下标可随输入改变，单项趋零只为必要条件。

###### 段：点态收敛的判据

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1433 -->

对每个输入分别控制任意有限尾和，以点态柯西判据给级数有有限点态和的充要条件；尾部起点仍可依赖输入。

###### 段：一致收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1444 -->

部分和到和函数的上确界误差趋零即一致收敛；[0,1)上的几何级数和无界而部分和有界，否定一致收敛；连续函数项的一致和仍连续。

###### 段：一致收敛的判据

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1452 -->

有限尾和对全部输入、全部较晚端点共同小于给定误差，当且仅当部分和一致收敛；尾部起点先于输入选择，区别于点态判据。

###### 段：几乎处处收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1464 -->

在固定可测零测集之外要求部分和点态收敛，可测函数项的和在例外集取零可保持可测性；不产生全域一致误差界。

###### 段：绝对收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1468 -->

各点绝对值级数有限称逐点绝对收敛，只在全测范围成立时称几乎处处绝对收敛；与一致收敛分别约束位置和尾和，不能互相混同。

###### 段：Weierstrass判别法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1472 -->

正式陈述每项绝对值由可求和非负数列共同控制时，级数在各点绝对收敛且一致收敛，截断误差由数项尾和控制。证明先比较绝对和再令尾部上限趋无穷；x^n/2^n给共同几何误差，指出条件仅充分。

##### 5.3.7.2 逐项求导

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1497 -->

正式定理要求各项连续可微、某一点的级数收敛且导数级数一致收敛；将部分和代入函数列导数定理，得到连续可微和函数及导数求和公式。另说明绝对连续函数项可用导数积分误差条件得到几乎处处结论，不把积分误差极限误作处处导数级数收敛。

##### 5.3.7.3 逐项积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1516 -->

非负项、绝对积分总和有限、有限测度上的部分和一致收敛分别提供三种充分条件；每类说明成立范围及不同的误差控制。

###### 段：非负函数项级数的逐项积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1521 -->

正式定理允许非负可测项和及积分为无穷；对递增部分和用单调收敛，再用有限加法得到逐项积分公式。

###### 段：绝对积分总和有限时的逐项积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1536 -->

正式定理保证几乎处处绝对收敛、和函数可积及部分和的绝对误差积分由绝对积分尾和控制；先用非负级数积分构造可积绝对上界，再积分尾和估计，最后由有限线性得到逐项积分。

###### 段：有限测度上一致收敛时的逐项积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1560 -->

各函数项可积、部分和一致收敛且总测度有限时，直接应用前面的函数列积分极限定理；区别于绝对积分总和有限这一充分条件。

#### 5.3.8 反常积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1570 -->

按范围无穷与函数无界两种情况分别规定勒贝格积分记号及截断计算，再统一用递增范围判断非负或绝对累计是否有限。示例、比较过程、尾误差与抵消边界并入对应论述，不单列过程或示例段落标题。

##### 5.3.8.1 无穷区间上反常积分的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1577 -->

先假设每个有限截断可积，正式定义半轴上的勒贝格积分及其记号；非负时允许无穷，有符号有限积分要求绝对可积。单调或支配收敛给截断公式，任意端点截断与左右两端分别处理的条件明确。

##### 5.3.8.2 无界函数反常积分的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1606 -->

先假设避开奇异端点的紧区间可积，正式定义端点反常积分的勒贝格记号及有限性约定；非负和绝对可积分别用单调或支配收敛恢复。右端点及内部奇点分侧处理，单点有限赋值不影响附近累计。

增加无穷端与奇点端两类反常积分的截断图，分别用指数尾部与平方根奇点核对完整遗漏积分，明确有限显示窗口不改变积分定义域。

##### 5.3.8.3 反常积分的可积性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1636 -->

先用简单函数递增、高度截断及范围扩大说明积分逼近，再以递增可测范围统一两类截断，把是否存在有限积分化为截断非负累计或绝对累计有共同有限上界；形式化给充要判据和截断误差，比较与幂函数验证阈值，截断抵消及主值界定不适用范围。

###### 段：简单函数与截断函数的积分收敛

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1641 -->

MCT补足规范简单函数的积分递增极限，DCT处理可积函数的高度截断及实轴范围截断，把函数值分层、高度截断与范围扩大统一到反常积分的逼近处理中。

###### 段：非负函数的可积性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1644 -->

正式定理以单调收敛证明全域积分有限当且仅当所有截断积分共同有界。上下比较与二进制区间推导x^-p在零附近p<1、无穷远p>1的阈值，原函数给x^-1/2、x^-1、x^-2的数值；这些计算不另设段落标题。

###### 段：有符号函数的可积性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/05-measurability-integration.tex:1682 -->

将非负判据用于绝对值，正式给绝对截断累计有共同界的充要条件、遗漏范围的积分误差趋零与穷尽方式无关性。后续保留几何尾界、无界可积支配、sin(x)/x条件抵消及1/x对称主值的推导；高峰无共同可积支配已在积分极限中证明，此处不再另用幂函数阈值重证，均作为同一问题的例证与边界，不另设过程标题。

### 5.4 本章小结

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/05-univariate-calculus.tex:17 -->

归纳连续性、局部近似、集合测量与累计的关系，保留积分范围、导数恢复、极限交换及无穷累计的条件。

## 第6章 多元函数微积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/06-multivariate-calculus.tex:1 -->

正文入口：[06-multivariate-calculus.tex](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/06-multivariate-calculus.tex)。

承接线性映射、一元微分与勒贝格积分，区分联合趋近和坐标切片，建立全微分，依次研究区域、路径、曲面累计及内部与边界的关系。

### 6.1 多元函数的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:2 -->

先完整研究多元标量函数的极限、连续、梯度、可微性及高阶局部近似，再推广到向量输出的Jacobian与链式法则；矩阵自变量及隐式方程的局部求解各自集中讨论。梯度列向量与Jacobian矩阵的对象、形状及作用始终区分。

#### 6.1.1 多元标量函数的极限和连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:12 -->

> 【保留，直接在欧氏空间建立】本 subsection 原有全部标题与例子保留；输入距离用向量欧氏范数，实值输出用绝对值。序列判据、联合连续及闭有界集性质直接在 R^d 中说明，不回指后文一般度量空间。

固定输入为d维点、输出为一个实数；按定义、共同趋近的极限判别、连续运算及闭有界集上的整体性质展开。

##### 6.1.1.1 多元标量函数的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:17 -->

正式定义d维输入到实数的映射，以贯穿二次函数的点值7与固定坐标切片说明多元输入和一元切片的差别。

##### 6.1.1.2 极限的定义与判别

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:26 -->

共同邻域控制覆盖全部允许路径；先定义，再以序列和反例判断，最后用统一距离上界证明存在性。

###### 段：极限的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:30 -->

在定义域聚点处正式给欧氏距离的ε—δ定义，解释同一δ必须同时控制不同速度、不断改变方向的输入。

###### 段：序列判据与路径检验

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:48 -->

明确输入取欧氏度量、输出取绝对值距离，直接应用已证的度量空间序列判据；坐标轴、所有固定直线仍不足以证明联合极限，分别用两类反例展示遗漏路径。

增加联合极限的标量值图与路径函数对照，直线和抛物线使用相同表达式，解释固定直线检验遗漏弯曲路径。

###### 段：累次极限与联合极限

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:78 -->

逐次取极限改变原来的量词，两次序可以不同，也可相等却没有联合极限；说明联合极限传递到累次极限仍需内层极限存在。

###### 段：统一误差估计

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:91 -->

用内积型不等式把误差界化成仅依赖欧氏距离的表达式，得到覆盖所有路径的证明；极坐标估计也须同时控制全部角度。

##### 6.1.1.3 连续性的定义与运算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:102 -->

正式给相对定义域的共同扰动定义，说明孤立点与聚点情形；切片连续仅为必要条件，和差数乘积商与标量复合逐项说明。

###### 段：和的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:118 -->

和函数的输出误差由两个原函数误差之和控制，说明和保留共同输入下的连续性。

###### 段：差的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:121 -->

差函数的输出误差同样被两个原函数误差之和控制，单列减法的连续结论。

###### 段：数乘的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:124 -->

固定实数非零时按ε除以系数绝对值控制原误差，零系数时直接得到常函数连续。

###### 段：积的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:127 -->

对两个实数输出使用积的极限法则，说明多元输入不改变标量乘法的连续规则。

###### 段：商的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:130 -->

要求基点分母非零，连续性保证邻近分母远离零，再使用商的极限法则；多项式与有理函数提供直接例子。

###### 段：标量复合函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:134 -->

内层多元标量输出与外层一元函数的定义域相容时，先控制中间实数误差再控制输入距离，得到复合连续。

##### 6.1.1.4 一致连续性与闭有界集上的性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:138 -->

以有限维闭有界集的子序列性质为共同依据，分别研究统一误差尺度、有界性与极值达到，不把不同结论合成一个含混性质。

###### 段：有限维闭有界集的收敛子列

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:143 -->

形式化陈述有限维有界序列必有欧氏收敛子列，闭集额外保证极限仍在原集合；逐坐标使用实数Bolzano–Weierstrass并有限次选子列，以范数界证明联合收敛，连接前面的紧致性子列性质。

###### 段：一致连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:158 -->

恢复统一δ的定义，形式化陈述闭有界集上连续函数一致连续，回用前文只依赖收敛子列性质的证明，将输入距离换成欧氏距离；有限维所需子列性质已在本小节完整证明。Lipschitz界另给充分条件。

###### 段：有界性与极值达到

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:172 -->

形式化陈述非空闭有界集上的连续标量函数有界且取得最大最小值，说明前文无界序列及趋近确界的子列证明在这里直接适用，不重复书写；整个平面的平方函数回用一元限制反例，开圆盘反例保留以说明缺闭的影响。

#### 6.1.2 偏导数和梯度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:189 -->

同一标量函数先求各坐标切片变化率，再排成梯度列向量，最后扩展为固定一般方向的一元切片；这些定义尚不自动保证可微。

##### 6.1.2.1 偏导数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:193 -->

在开集内部以坐标向量定义双侧偏导数，逐坐标计算贯穿二次函数在(1,2)处的4、5并给出差商，说明只改变一个坐标的含义。

##### 6.1.2.2 梯度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:214 -->

正式定义各一阶偏导按输入坐标排列的列向量，计算二次函数梯度，指出偏导存在只记录坐标切片，统一增量预测仍待可微性。

##### 6.1.2.3 方向导数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:228 -->

以固定方向向量正式定义双侧差商，允许非单位方向并区分参数速度与单位路程变化率；二次函数沿(1,1)及其单位方向分别给9、9/√2。

#### 6.1.3 多元标量函数的可微性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:251 -->

将分别检查固定方向的变化，提升为同一个线性映射控制所有小扰动；按定义、必要/充分判别、微分运算、中值估计组织。

##### 6.1.3.1 微分的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:256 -->

由扰动叠加相容性引出线性映射，正式定义小于扰动长度阶的统一余项与全微分，明确不是逐方向分别选取误差尺度。

##### 6.1.3.2 可微性的要求与判别

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:274 -->

在同一开域和基点上依次建立必要条件、充分判别、蕴含链及失败逆命题。每个结论的证明与反例只讲一次，关系段直接使用已证结果，不重复陈述全微分和方向导数公式。

###### 段：可微的必要条件

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:280 -->

正式陈述可微蕴含连续、各偏导存在，且全微分和全部双侧方向导数由梯度给出；通过线性映射的有界性和坐标扰动证明。二次函数展开核对统一余项，切平面图显示全方向界，等值曲线图说明单位方向下的最快上升。

###### 段：偏导数连续给出的充分条件

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:332 -->

形式化要求各偏导在邻域存在且在基点连续；坐标逐段应用一元中值定理，有限和范数界把偏导误差合为统一小量，证明其足以可微。

###### 段：连续可微函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:356 -->

规定C1及Ck为相应阶数偏导存在且连续，由充分判别得到C1处处可微；随后比较邻域C1与基点可微的强弱。

###### 段：条件之间的蕴含关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:361 -->

集中写出邻域C1蕴含基点可微、再蕴含全部双侧方向导数存在、再蕴含各偏导存在；前两步直接用已经给出的证明，最后取坐标方向。可微蕴含连续另列说明，区分邻域条件、基点条件及一元与多元的差别。

###### 段：偏导数存在不保证可微

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:377 -->

保留xy除以距离的一个完整反例，坐标偏导为零而对角线统一余项比恒二分之一；给其连续性估计，说明补上连续性仍不够。单侧方向极限存在而双侧可能不存在，需遵守本节双侧约定。

###### 段：全部方向导数存在不保证可微

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:394 -->

先用x³除以平方和函数说明全部双侧方向变化率未必线性，再以q函数说明即使连续且所有方向导数为零，沿抛物线仍无统一小量余项。两种缺口各保留一次计算，不再在关系段复述。

###### 段：可微不保证连续可微

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:421 -->

零点置零的x²sin(1/x²)处处可微，导数沿指定序列无界，故不C1；依赖首坐标得到多元版本，也说明可微不保证局部Lipschitz。

###### 段：连续不保证偏导数存在

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:431 -->

绝对值x的平面函数在全域Lipschitz，却在原点缺少关于x的双侧偏导；反向回用前面极限反例中坐标偏导存在而不连续的函数，明确连续与偏导存在没有一般单向蕴含。

###### 段：梯度与线性近似的使用条件

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:437 -->

梯度记录坐标变化率，可微才保证其能统一预测增量和计算任意方向导数；连续偏导只给充分判别，必要时直接验证统一余项，向量输出留到后面按分量检查。

##### 6.1.3.3 微分的运算法则

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:442 -->

固定同一基点可微的标量函数，从一阶展开逐项说明和、差、数乘、积、商及标量外层复合的线性项和余项，并以二次型应用。

###### 段：和的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:447 -->

共同基点的两个一阶线性项相加，两个小量余项之和仍为小量，得到和函数的微分公式。

###### 段：差的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:454 -->

共同基点的线性项相减，余项之差仍满足统一小量要求，得到差函数可微与公式。

###### 段：数乘的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:461 -->

固定系数缩放线性项和余项，得到常数倍规则，并包括零系数情形。

###### 段：积的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:464 -->

展开两标量函数的一阶近似并保留一次项，线性增量乘积为二阶可并入余项，得到乘积法则。

###### 段：商的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:471 -->

分母基点非零保证邻近远离零，先用一元倒数展开再用积法则，给出商的微分和余项控制。

###### 段：标量复合函数的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:478 -->

外层一元函数在中间标量处可微，复合在邻域有定义，内层增量O(‖h‖)将外层余项转成输入尺度的小量。

###### 段：二次型的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:485 -->

二次型仍为标量函数，乘积展开得到(A+Aᵀ)x的梯度；只有A对称才可简为2Ax，保留输入/输出类型和矩阵次序。

##### 6.1.3.4 中值定理与Lipschitz条件

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:505 -->

形式化给沿定义域内线段的一元中值公式，并通过方向导数链式关系证明；梯度有共同上界得到两点差界，凸域上的统一上界导出全域Lipschitz。C1函数在域内闭球上梯度有界，因而局部Lipschitz；实轴平方函数说明不能自动推广为全域共同常数。

#### 6.1.4 多元标量函数的高阶微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:526 -->

先定义二阶偏导与Hessian，再由Taylor公式控制局部二次误差，最后讨论内部无约束驻点的极值判别，避免尚无余项便使用充分条件。

##### 6.1.4.1 二阶偏导数与Hessian矩阵

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:532 -->

定义二次求偏导的次序，贯穿二次函数计算四个二阶偏导；先说明混合偏导交换所需条件，再建立Hessian及方向二次型。

###### 段：混合偏导数的交换

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:537 -->

形式化陈述两混合偏导在邻域存在、在基点连续即可交换；二阶差分按两次序分别应用两次一元中值定理，除以hk并取极限证明。

###### 段：Hessian矩阵

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:561 -->

正式定义各二阶偏导组成的方阵，区分二阶偏导存在与导数映射本身可微；C2保证对称及方向二阶导数公式，以二次函数和不同曲率说明正定、半正定、负定、半负定与不定。

##### 6.1.4.2 Taylor公式与局部近似

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:596 -->

对C2标量函数和域内整条线段，形式化给二阶中间点式及基点Hessian的小量式；用一元Taylor和Frobenius界证明，指数函数展示切平面与二次修正。再将同一线段函数代入已经证明的一元Taylor积分余项r=1公式，结合已算的一、二阶导数得到Hessian积分余项，不重复分部积分，说明一点局部展开不自动提供全区域统一余项。

##### 6.1.4.3 局部极值的判别

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:637 -->

先定义局部与严格局部极值并限定开集内部，再按一阶必要、二阶必要、二阶充分三个问题给出正式结论；Taylor余项已前置。

###### 段：局部极值的一阶必要条件

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:643 -->

沿所有方向应用Fermat定理，正式给内部可微极值点梯度为零并证明；称其为驻点，明确驻点未必极值。

###### 段：局部极值的二阶必要条件

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:660 -->

C2内部极小点Hessian半正定、极大点半负定，沿每个方向的一元二阶必要条件证明；x⁴、−x⁴、x³说明必要条件不充分。

###### 段：驻点的二阶充分条件

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:677 -->

形式化给C2驻点Hessian正定/负定/不定的分类；在单位球面取得共同正曲率下界并用Taylor误差证明严格极值，不定以正负方向给鞍点；半定可能未决，边界与约束点另论。

增加正定、不定、零Hessian的局部曲面对照，固定显示尺度，说明退化二次型仍需高阶信息，不能等同于没有极值。

#### 6.1.5 多元向量值函数的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:725 -->

对象切换为同一d维输入到m维输出，先按输出分量建立极限与微分，再组织Jacobian运算和向量增量估计；与只固定输入坐标的切片区分。

##### 6.1.5.1 向量值函数及其极限与连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:730 -->

正式定义F=(F1,…,Fm)的向量值映射；欧氏范数与分量最大值的两侧界证明有限个输出分量的极限/连续性等价于整体结论。

##### 6.1.5.2 微分与Jacobian矩阵

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:745 -->

正式定义m×d Jacobian表示向量输出的线性近似，余项按输出欧氏范数度量；证明逐输出分量可微的等价性，明确单输出Jacobian是梯度的转置。

增加向量值映射的网格变形及局部平行四边形对照，固定映射和Jacobian，说明有限非线性像与一阶近似不同并承接体积换元。

###### 段：Jacobian矩阵的计算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:772 -->

先逐输出求偏导再按行排列，二维二次映射给具体扰动；归一化指数映射作为另一计算例，逐项商法则推导diag(s)−ssᵀ及其对角、非对角项和行和为零。

##### 6.1.5.3 向量值函数的微分运算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:811 -->

相同形状输出分别允许和、差、数乘；复合要求中间输出落在后层定义域。没有指定向量乘法便不套用标量乘积法则。

###### 段：和的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:817 -->

同形向量值映射逐输出使用和法则，Jacobian相加并检查输出与矩阵形状。

###### 段：差的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:824 -->

相同形状和共同基点条件下逐分量使用差法则，Jacobian相减。

###### 段：数乘的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:830 -->

固定实系数逐分量作用，Jacobian整体乘同一个系数。

###### 段：复合函数的链式法则

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:836 -->

对两层可微映射正式给Jacobian按计算次序相乘，利用内层增量O(‖h‖)控制外层余项证明；以(p×m)(m×d)核对次序。

###### 段：标量复合函数的梯度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:855 -->

末端输出为标量时转写为列梯度的Jacobian转置传递，说明中间向量和目标函数角色；保留二维输入、三维中间量、平方目标的完整计算并与直接展开交叉核对(6,4)。

增加前向类型与反向梯度的简图，按2→3→1核对Jacobian转置的形状，区分梯度传递和求逆映射。

##### 6.1.5.4 向量增量的中值估计

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:904 -->

多个输出一般不能共用同一个中值点，因此改用线性映射最大放大率控制增量范数。

###### 段：算子范数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:909 -->

正式定义欧氏诱导算子范数并以diag(2,1)说明；形式化给向量值中值上界，通过将输出差投影到其单位方向后使用一元中值定理证明，不预先依赖积分。凸域统一Jacobian界导出Lipschitz并供后续收缩构造使用。

#### 6.1.6 矩阵自变量函数的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:966 -->

定义域固定为全矩阵空间的开集，允许全部充分小的同形扰动；先处理标量输出与同形梯度，再将矩阵输出另作线性映射，保持乘法次序。

##### 6.1.6.1 矩阵标量函数的微分与梯度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:971 -->

回用线性空间章的Frobenius内积/范数和迹，正式定义矩阵扰动的线性泛函与同形梯度；逐元素扰动证明唯一，迹循环移位不能替换成任意因子交换，对称子空间输入需另定允许方向。

###### 段：迹函数的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:998 -->

线性迹函数的全微分直接符合内积表示，因此梯度为固定系数矩阵；保留原公式与读取梯度的用途。

###### 段：行列式的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:1009 -->

在可逆方阵处分离扰动，排列展开识别一次迹项；有限多项式的统一二阶余项保证全微分而非仅固定方向导数，得到Jacobi一阶公式。

###### 段：对数行列式的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:1025 -->

在detX>0的开集应用一元对数链式法则，得到迹微分与逆转置梯度；仅在对称时可去掉转置。

##### 6.1.6.2 矩阵值函数的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:1040 -->

将矩阵输入到矩阵输出的扰动表示为两个矩阵空间间的线性映射，余项按输出Frobenius范数；不能把所有输出挤进一个标量梯度。

###### 段：逆矩阵的微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:1046 -->

先用代数余子式/非零行列式确认逆映射逐元素C1，再对XX逆=I微分并左乘逆；保留扰动两侧的逆矩阵和非交换算例，用对称性检查错误的标量式类推。

#### 6.1.7 隐函数与反函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:1078 -->

从对已给映射求导转到给方程寻找局部函数，先证明存在、唯一、可微，再由此解决向量值映射的局部反求；待解变量对应方阵Jacobian必须可逆。

##### 6.1.7.1 隐函数的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:1084 -->

区分显式映射与方程关系；y²−x=0的两支、原点失效和分支图说明必须固定起始解及邻域，并先问唯一选解再求导。

##### 6.1.7.2 隐函数的存在、唯一性与微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:1102 -->

形式化给C1方程映射、已知零点和待解变量Jacobian可逆条件，结论为邻域零点集与唯一C1分支逐点等价。完整证明检查统一收缩与闭球自映射，用几何尾和、欧氏完备性取得唯一不动点；再用参数中值界得局部Lipschitz，以联合展开和逆矩阵连续性证明可微及C1。

###### 段：隐函数的导数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:1198 -->

存在唯一C1分支已由前一定理保证，回用该定理证明中已推导的导数公式，不再重做链式法则与逆矩阵运算；正、负平方根分支核对导数±1/2，说明选定分支的作用。

##### 6.1.7.3 反函数的存在与微分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:1214 -->

以输出为参数构造G(x)−y=0，正式给Jacobian非奇异处的C1局部逆；从隐函数构造两个开邻域间的双射，再链式法则得到逆Jacobian公式。

###### 段：局部可逆与整体单射

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/06-multivariable-differentiation.tex:1241 -->

指数极坐标的周期性说明处处非奇异仍不全局单射，x³的逆说明连续逆不保证可微；明确局部逆定理的范围。

### 6.2 区域积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:1 -->

固定被积对象为多元标量函数；从多维测度建立积分，再按累次积分、坐标换元、参数变化三个计算问题说明成立条件。坐标变换属于向量值映射，与标量被积函数分开。

#### 6.2.1 多维测度与乘积测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:13 -->

> 【必要改名】本 subsection 拟由“多维测度与乘积测度”改为“欧氏空间的体积测量”；原有“多维勒贝格测度”分支及其两个 paragraph 保留，一般乘积测度分支后移。

从长度与矩形面积的乘法规则出发，先构造欧氏多维测度，再说明一般测度空间乘积及二者在欧氏空间的联系。

##### 6.2.1.1 多维勒贝格测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:20 -->

以坐标盒体积取代区间长度，沿外覆盖、可测分割、测度限制的路线推广一维构造。

###### 段：坐标盒

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:22 -->

定义开坐标盒为区间的笛卡尔积，体积为边长之积；以长方形面积作例，并引出开盒生成的Borel范围。

###### 段：多维勒贝格测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:31 -->

以坐标盒体积取代区间长度，沿外覆盖、可测分割、测度限制的路线推广一维构造。

##### 6.2.1.2 乘积测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:46 -->

> 【后移】本 subsubsection 及“σ有限测度”“乘积σ代数”“乘积测度”“欧氏乘积与完备化”四个 paragraph 移入第二部分“测度空间”。本章已有基于坐标盒覆盖的 R^d 勒贝格测度构造继续保留。

从一般测度空间的矩形赋值出发，按σ有限条件、可测范围、测度构造、欧氏完备化的依赖顺序介绍。

###### 段：$\sigma$有限测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:51 -->

正式定义由可数个有限测度集合覆盖的空间，比较有限、可数计数测度、实轴长度与不可数计数测度。

###### 段：乘积$\sigma$代数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:63 -->

矩形不对并补封闭，因此取包含全部可测矩形的最小σ代数；有限网格展示生成后得到的可测范围。

###### 段：乘积测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:70 -->

在可测矩形上规定两侧测度之积；正式定义乘积测度，并形式化给出σ有限条件下的存在唯一性。扩展定理明确引用Folland；有限加权网格说明矩形规则的含义。

增加按边权重等比例绘制的有限乘积测度格表，以格面积体现乘法、格求和体现累计，并保留一般联合分布未必乘积分解的边界。

###### 段：欧氏乘积与完备化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:107 -->

证明Borel乘积与高维Borel范围相同；由矩形赋值与唯一性联系多维测度，再强调乘积空间需作完备化，不能由因子完备自动推出乘积完备。

#### 6.2.2 区域积分的定义与可积性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:127 -->

按标量函数的可测性、积分定义、有限可积性判别组织，避免矩形与一般区域重复定义。

##### 6.2.2.1 多元可测函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:132 -->

以阈值原像正式定义多元可测标量函数，说明连续性如何保证可测，并以有理点指示函数区分可测与连续。

##### 6.2.2.2 区域积分的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:147 -->

先定义非负累计，再定义有符号绝对可积性，最后统一二重、三重和d维积分记号。

###### 段：非负标量函数的积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:149 -->

以可测简单函数积分的上确界定义非负区域积分，允许无穷值；通过零延拓处理任意可测区域，不要求边界零测。

###### 段：有符号标量函数的积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:166 -->

形式化规定绝对积分有限，并由正负部分之差定义有限积分；说明无穷值的零测改值及有理点指示函数积分为零。

###### 段：二重积分与多重积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:185 -->

说明面积、体积、d维体积所用记号；重数表示输入维数，不表示已经完成积分换序。常数薄片说明累计的几何意义。

##### 6.2.2.3 可积性的判别

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:199 -->

分别使用有限测度与有界性、可积上界、递增截断判断绝对积分有限。

###### 段：有限测度区域上的有界函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:201 -->

由绝对积分不超过M乘区域测度给出充分条件，覆盖紧长方体上的连续函数；指出无界函数可能可积及无限体积区域上有界函数未必可积。

###### 段：可积控制函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:210 -->

利用绝对值被同一可积非负函数控制的比较判别，将无界函数可积性转为上界函数的可积性。

###### 段：递增区域上的截断

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:215 -->

由单调收敛给出绝对积分等于递增截断绝对积分的极限；有限上界等价于可积，再用支配收敛恢复有符号积分并说明截断无关。

#### 6.2.3 区域积分的基本性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:225 -->

> 【保留，限于欧氏勒贝格积分】本 subsection 的所有运算标题和公式保留，直接回用当前 R^d 体积积分的性质，不以一般测度空间作前提。

各性质直接继承一般勒贝格积分，并明确固定可测区域及有符号绝对可积条件；不同运算分别成段。

###### 段：加法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:229 -->

以绝对值的次可加界确认和函数可积，再给出两个可积标量函数积分的加法公式。

###### 段：减法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:237 -->

单独给出两个有限可积函数的差与积分相减公式，排除无穷减无穷。

###### 段：常数倍

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:245 -->

明确实标量与可积函数的关系，给出常数倍积分公式及其权重含义。

###### 段：区域可加性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:253 -->

给出两两不交可测区域上的可数可加公式及绝对收敛条件，再由指示函数恒等式推导重叠区域的容斥式。

###### 段：单调性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:267 -->

用几乎处处的函数比较推出积分比较，并用有限区域上的常数上界解释小区域误差控制。

###### 段：绝对值不等式

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:275 -->

由正负比较给出积分绝对值界；说明零测改值不影响积分，完备性保证可测性。

#### 6.2.4 累次积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:283 -->

> 【保留原有全部层级】截面与累次积分、Tonelli/Fubini条件、计算及换序边界均保留；对象统一为 R^p×R^q 与对应勒贝格测度。一般乘积空间和 σ 有限的混合测度反例后移；截面仅几乎处处可测、非负或绝对可积等必要条件保留。现有行列配对反例可实现为单位方格上的常值函数，保留原计算含义。

将一次区域累计改写为逐坐标累计，按截面定义、成立条件、计算、适用边界组织。

##### 6.2.4.1 截面与累次积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:288 -->

定义固定一个坐标的截面与先内后外的累次积分，强调记号不保证换序；有限网格建立直觉，乘积权重与一般联合分布保持区分。

##### 6.2.4.2 累次积分的成立条件

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:300 -->

固定σ有限的两个因子空间，分别陈述非负与绝对可积两个条件；区分原乘积可测范围与完备化后的几乎处处截面。

###### 段：非负可测函数的累次积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:305 -->

形式化陈述Tonelli：截面及内积分函数可测，两个次序与乘积积分相等，允许无穷值；完备因子的乘积完备化只保留几乎处处截面结论。

###### 段：绝对可积函数的累次积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:326 -->

形式化陈述Fubini：绝对积分有限保证几乎每个截面可积，内积分在例外集置零后可积，两个次序相等且有限；保留集合扩展→简单函数→单调逼近的证明路线及引用边界。

##### 6.2.4.3 累次积分的计算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:361 -->

连续矩形函数先核对绝对可积，再计算x+y的例子；三角形区域改变次序时重新描述同一集合，不能只交换微分符号。

增加同一三角形的纵横切片图，按集合重新读取两种积分限，强调示意窄条不等于微元，换序仍须Tonelli/Fubini条件。

##### 6.2.4.4 积分换序的适用边界

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:394 -->

用无穷双重级数展示行列各自有限仍不保证换序，保留对角线图；再以长度×不可数计数测度的对角线说明σ有限条件的作用。

#### 6.2.5 区域积分的换元

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:436 -->

将坐标变换作为向量值映射，与标量被积函数区分；同时改写函数和体积权重。

##### 6.2.5.1 换元公式与适用条件

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:441 -->

先解释行列式为何是局部体积缩放，再给出统一勒贝格换元定理及可测子区域版本。

###### 段：体积的局部缩放

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:443 -->

由线性映射的行列式绝对值解释体积比例，连接Jacobian局部线性化；强调局部近似还不等于整体公式。

###### 段：勒贝格积分的换元

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:453 -->

对开集间C1微分同胚形式化给出非负与绝对可积版本；说明零测集保持、集合体积变换的引用依赖，以及简单函数/单调逼近的推广，保留两个原公式标签。

##### 6.2.5.2 常用坐标变换

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:481 -->

在统一换元定理之下集中计算极坐标、柱坐标、球坐标，分别说明Jacobian权重与接缝、坐标退化的零测处理。

###### 段：极坐标

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:483 -->

推导Jacobian为r，保留单位圆盘例子和面积权重图；用截断与极限处理中心、接缝和边界，并防止重复覆盖。

###### 段：柱坐标

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:511 -->

给出柱坐标映射及体积权重r，计算半径R、高H圆柱体的体积。

###### 段：球坐标

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:518 -->

明确径向、极角和方位角约定，给出ρ²sinφ的体积权重并计算球体体积，说明单次覆盖范围和零测退化集合。

#### 6.2.6 参数积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:532 -->

> 【保留，限于欧氏可测积分域】参数积分现有全部 subsubsection、条件、证明与例子保留；积分域统一为可测 D⊂R^d，使用 m_d。共同零测集与统一可积控制不得删去。

固定区域而改变标量函数的实参数，分别处理连续性、积分号下求导和变限积分边界贡献。

##### 6.2.6.1 参数积分的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:537 -->

在一般测度空间定义G(θ)=积分g(x,θ)，明确x为积分变量、θ为参数，点态变化尚不能控制积分变化。

##### 6.2.6.2 参数积分的连续性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:545 -->

形式化给出同一个零测例外集与同一个局部可积控制函数下的连续性，利用支配收敛和序列判据证明；指数积分说明控制只需覆盖参数点附近。

##### 6.2.6.3 积分号下求导

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:561 -->

形式化给出可积截面、共同零测集、整个参数邻域可微及统一可积偏导界条件，保留中值定理控制差商→支配收敛的完整推导；指数例子及边界失效例子说明适用范围。

##### 6.2.6.4 变限积分的求导

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/07-regional-integrals.tex:634 -->

形式化给出连续被积函数和参数偏导、可微端点下的三项公式；将积分差分成旧区间函数变化、上端新增、下端移去三部分证明，说明一般可测函数的端点值不能任意选取。

### 6.3 路径积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:2 -->

区分沿路径的标量密度累计与向量场有向位移累计；共同路径几何先行，两类积分分别介绍定义、可积要求、性质和计算，最后回答路径无关。

#### 6.3.1 参数路径与弧长

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:10 -->

用参数路径记录位置与次序，用弧长把参数增量换成实际路程。

##### 6.3.1.1 路径的定义

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:15 -->

分别正式定义连续参数路径和分段光滑条件，区分像集、方向、速度与重复行进。

###### 段：参数化路径

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:17 -->

正式定义路径、起终点、闭路径及像集；同线段不同速度例子说明参数信息不能简化为点集。

###### 段：分段光滑路径

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:28 -->

正式定义有限分段C1与分段正则路径，说明折点和速度为零处的处理范围。

##### 6.3.1.2 路径的长度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:39 -->

通过折线上确界建立几何长度，再证明它等于速度范数的勒贝格积分。

###### 段：弧长

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:41 -->

正式定义可求长性并证明分段C1弧长公式：弦长由速度积分控制，速度一致连续给出反向逼近；定义累计路程和ds，使用对角线段说明范数权重。

#### 6.3.2 第一类路径积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:72 -->

固定标量被积对象和非负弧长权重，独立说明这类积分的要求、性质、计算。

##### 6.3.2.1 定义与可积性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:76 -->

按标量函数与弧长权重定义第一类积分，区分非负累计和绝对可积性，连续性仅作充分条件。

###### 段：按弧长的积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:78 -->

正式定义参数复合可测条件下的非负第一类积分及有符号绝对可积条件；连续函数为充分条件，线密度给出质量。平面零测而线长为正的例子说明需指定路径上实际取值。

##### 6.3.2.2 积分的基本性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:102 -->

第一类路径积分的加法、减法、常数倍及路径操作分别成段，所有有符号公式明确有限可积条件。

###### 段：加法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:106 -->

对沿路径可积的标量函数单独给出加法公式，依据参数表达与一元勒贝格积分性质；说明相应可积性或有限性。

###### 段：减法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:114 -->

对沿路径可积的标量函数单独给出减法公式，依据参数表达与一元勒贝格积分性质；说明相应可积性或有限性。

###### 段：常数倍

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:122 -->

对沿路径可积的标量函数单独给出常数倍公式，依据参数表达与一元勒贝格积分性质；说明相应可积性或有限性。

###### 段：路径拼接

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:130 -->

第一类积分在首尾相接路径上逐段相加；保留重复行进的次数。

###### 段：重参数化与方向无关

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:139 -->

用速度范数的绝对值与一元换元证明单调分段C1微分同胚下积分不变，包括方向反转；行进次数仍保留。

###### 段：单调性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:148 -->

同一路径上标量函数的大小比较，经非负弧长权重保留为积分大小比较。

###### 段：绝对值不等式

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:156 -->

给出积分绝对值不超过绝对值的弧长积分，并在有界时再由函数上界乘路径长度控制。

##### 6.3.2.3 积分的计算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:166 -->

按参数化、速度范数、逐段一元积分计算；保留对角线标量例子与平面图像路径的根号权重公式。

#### 6.3.3 第二类路径积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:182 -->

固定向量场为被积对象，先与速度取内积成为标量，再进行一元勒贝格积分。

##### 6.3.3.1 定义与可积性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:186 -->

先定义向量场，再定义与有向位移内积的标量积分；复合可测性、内积的绝对可积性及连续充分条件分别明确。

###### 段：向量场

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:188 -->

正式定义位置到同维向量的映射，旋转场说明向量的大小方向及做功中的切向分量。

###### 段：有向线积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:198 -->

正式定义参数复合分量可测且场与速度内积绝对可积时的第二类积分；连续性或范数之积可积是充分条件，说明坐标记号、单位切向量与环流。

增加同一路径的标量密度累计与向量场做功对照，弧长√2和水平投影累计1分别核对，明确两类积分的对象与局部权重。

##### 6.3.3.2 积分的基本性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:228 -->

第二类路径积分的加法、减法、常数倍及路径操作分别成段，所有有符号公式明确有限可积条件。

###### 段：加法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:232 -->

对沿路径可积的向量场单独给出加法公式，依据参数表达与一元勒贝格积分性质；说明相应可积性或有限性。

###### 段：减法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:241 -->

对沿路径可积的向量场单独给出减法公式，依据参数表达与一元勒贝格积分性质；说明相应可积性或有限性。

###### 段：常数倍

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:250 -->

对沿路径可积的向量场单独给出常数倍公式，依据参数表达与一元勒贝格积分性质；说明相应可积性或有限性。

###### 段：路径拼接

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:259 -->

第二类积分在首尾相接路径上逐段相加；保留重复行进的次数，并逐段保持方向。

###### 段：方向反转

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:269 -->

明确反向参数路径γ−，由速度变号和一元换元证明第二类积分变号。

###### 段：重参数化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:278 -->

在保向分段C1微分同胚下证明积分不变，反向变号，重复次数仍影响累计。

###### 段：绝对值不等式

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:288 -->

由内积Cauchy–Schwarz与一元积分三角不等式，给出第二类积分绝对值不超过向量场范数的弧长积分；右侧无限不能证明有限性。

##### 6.3.3.3 积分的计算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:297 -->

按参数化、场与速度内积、逐段一元积分计算；保留常场对角线、图像路径公式及半圆/直径的旋转场对比，说明路线可能影响结果。

增加半圆与直径穿过同一旋转场的图，保留行进方向并核对π与0，说明相同端点和光滑场不足以保证路径无关。

#### 6.3.4 路径无关与势函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:330 -->

用梯度场把第二类积分化为端点差，再建立路径无关等价判别和势函数存在的局部/域条件。

##### 6.3.4.1 势函数与路径积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:335 -->

先正式定义势函数，再通过链式法则和一元基本定理证明路径积分基本定理。

###### 段：势函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:337 -->

在开集上将C1标量函数的梯度定义为连续向量场的势表示；平方范数例子说明加常数不影响场。

###### 段：路径积分基本定理

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:347 -->

对C1势函数和分段C1路径给出端点差公式，并逐段链式法则积分证明；闭路径零积分与方向变号由此得到。

##### 6.3.4.2 路径无关的等价判别

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:369 -->

在非空开且路径连通的域上，组织路径无关、闭路径零积分、存在C1势函数三者的等价关系。

###### 段：路径无关

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:371 -->

正式定义同端点的任意分段C1路径积分相同；形式化给出三条件等价定理，证明通过拼接反向路径与固定起点积分构造势函数。

##### 6.3.4.3 势函数存在的微分判别

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:402 -->

将向量场交叉偏导相等作为必要条件，在星形域加上域条件得到充分性，并用穿孔平面说明不能去掉域条件。

###### 段：交叉偏导相等的必要条件

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:404 -->

对C1向量场正式陈述保守场的交叉偏导条件；由势函数自动属于C2与混合偏导交换证明。

###### 段：星形域上的充分条件

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/08-path-integrals.tex:419 -->

定义星形域并形式化给出线段积分构造势函数的定理；共同紧邻域有界控制保证积分号内求导，交叉偏导化成参数全导数。穿孔平面旋转场的非零圆周积分排除全局势函数。

### 6.4 曲面积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:2 -->

以被积对象为依据分开标量面积累计与向量场通量。共同基础先解释向量值曲面参数化如何把曲面拉回二维区域，利用叉积长度建立面积测度并证明重参数化下不变；之后两类积分分别按定义与可积性、性质、计算展开，全部为勒贝格积分。原有平面和球面例子保留，面积计算归第一类，法向通量计算归第二类。

#### 6.4.1 参数曲面与面积

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:13 -->

曲面上的累计既要标记位置，也要确定实际面积权重。先以两个实参数到三维向量的映射描述曲面，再从切向量和叉积得到面积测度；参数替换与有限分片是两类积分共用的几何基础。

##### 6.4.1.1 曲面的参数化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:18 -->

明确参数化 $r:E\subseteq\mathbb R^2\to\mathbb R^3$ 是向量值映射，其两个偏导仍是三维向量。规定内部独立性和单次覆盖，防止两个参数塌成一维像或重复累计同一片面。

###### 段：正则曲面片

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:20 -->

以参数化需要描述一张面引出形式化定义：参数域是有界闭区域、为其内部闭包且边界二维零测；参数化在闭域开邻域 $C^1$，两个切向量在内部处处独立，不同参数仅允许在参数边界重复。定义后就地解释线性无关：实数线性组合为零仅当两个系数均为零。参数边界接缝或退化点为零面积例外。沿两个参数方向分别形成参数曲线，以平面 $z=x+y$ 的单位参数片计算两切向量。

###### 段：叉积

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:46 -->

小参数矩形两边的线性像需要合成实际面积，由此引入三维叉积的分量定义、垂直性、长度与平行四边形面积的关系及交换次序变号。正则性等价于叉积非零，小片面积的一阶权重为叉积长度。

##### 6.4.1.2 曲面面积的表示

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:59 -->

把叉积长度作为二维勒贝格测度的权重，得到曲面面积和面积元；再用链式法则与区域换元证明这些量不会随合法参数替换而改变，并说明有限分片接缝的处理。

###### 段：面积元与面积测度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:61 -->

正式定义曲面可测集为原像勒贝格可测的子集，以及 $\sigma_S(A)=\int_E1_A(r)J_S$、$J_S=\|r_u\times r_v\|$。由原像保持集合运算和积分可数可加得到曲面测度；闭域上连续有界权重保证有限面积。参数零测边界不计面积，斜平面片面积为 $\sqrt3$ 而参数面积为 $1$。

增加参数区域与斜面片的逐块对应，按实际参数化及两切向量核对√3的面积权重，区分参数面积与曲面面积。

###### 段：重参数化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:96 -->

对闭域邻域 $C^1$、内部为微分同胚且仍满足单次覆盖条件的参数变换，正式陈述并证明叉积带行列式、面积权重带行列式绝对值。证明逐项使用链式法则、叉积双线性和二维勒贝格换元，得到面积测度一致；同时保留行列式符号供法向选择使用。正面积多次覆盖仍会重复累计。

###### 段：分片曲面

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:132 -->

将无法由一张参数片表示的曲面分成有限片，内部不重叠且接缝在相邻片上均零面积，定义面积测度逐片相加。接缝无需额外贡献；无界或超出有限正则覆盖的曲面需要另行核查覆盖与可积条件。

#### 6.4.2 第一类曲面积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:140 -->

对象为曲面上的可测标量函数，累计权重为已建立的面积测度。先区分非负积分和有限可积，再逐项说明标量运算、曲面分割及比较，最后通过图像曲面和球面给出参数计算。

##### 6.4.2.1 积分的定义和可积性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:145 -->

承接面积测度，把面密度累计定义为测度积分。可测函数可带跳跃；非负积分可为无穷，一般实值函数以绝对积分有限作为可积要求，连续性只是便于核查的充分条件。

###### 段：按面积的积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:147 -->

用小片密度乘面积引出第一类曲面积分的正式定义，保留原参数公式标签；$h=1$ 给面积，非负面密度给质量，单位斜面常数密度 $2$ 得 $2\sqrt3$。由于不使用法向，翻转朝向不改变结果。

###### 段：可积性的要求

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:172 -->

把有限可积性准确写成 $\int_E|h(r)|J_S<\infty$。紧致曲面上的连续函数有界，结合有限面积给出充分条件；可测性不保证有限绝对积分。积分与几乎处处均相对于曲面面积，三维体积为零不表示曲面面积积分为零。

##### 6.4.2.2 积分的性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:184 -->

在函数曲面可积的统一前提下，按标量密度的运算、积分范围的分割和大小比较分别给出公式及依据，不与向量场通量运算混列。

###### 段：加法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:189 -->

曲面可积的两个标量函数之和仍可积，其积分等于两个积分之和；用和的绝对值不超过两项绝对值之和说明可积性，等式归结为勒贝格加法性质。

###### 段：减法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:197 -->

曲面可积的两个标量函数之差仍可积，其积分等于两个积分之差；用差的绝对值不超过两项绝对值之和解释绝对可积，等式归结为勒贝格减法性质。

###### 段：数乘

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:205 -->

实数倍函数的绝对积分仍有限，常数可提出积分号；用 $|ch|=|c||h|$ 解释可积性。

###### 段：曲面分割的可加性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:213 -->

对两两不交的曲面可测集列，函数在全曲面可积时，其并上的积分为各部分积分之和，且级数绝对收敛。绝对值和由全曲面绝对积分控制；有限曲面分片和零面积接缝属于该结论的情形。

###### 段：单调性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:223 -->

曲面面积几乎处处的函数序关系传递到积分；对非负差函数使用积分非负性和减法公式证明。明确此处允许忽略的是零曲面面积集合。

###### 段：绝对值不等式

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:232 -->

将单调性应用于 $-|h|\le h\le|h|$，得到原积分绝对值不超过绝对值的面积积分，给出控制积分大小的上界。

##### 6.4.2.3 积分的计算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:240 -->

按单次覆盖参数化、函数复合、乘叉积长度的顺序计算。对 $C^1$ 标量图像 $z=\psi(x,y)$ 求得叉积 $(-\psi_x,-\psi_y,1)$，面积根号因子给斜平面单位圆盘面积 $\pi\sqrt{1+a^2+b^2}$；投影不是单值时改参数或分片。球面采用 $(\varphi,\theta)$ 参数，内部正则且单次覆盖，参数边界的两极和接缝为零面积，积分 $R^2\sin\varphi$ 得 $4\pi R^2$。例子和中间计算未另设段标题。

#### 6.4.3 第二类曲面积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:274 -->

对象改为向量场，通量只累计其沿所选法向的标量分量。先规定单位法向和全局相容性，再定义通量及准确可积条件，分别说明场的运算、曲面分割、法向反转和参数替换，最后计算图像曲面与球面通量。

##### 6.4.3.1 曲面的定向

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:279 -->

面积不提供正反方向，通量需要在每个光滑点选择一个单位法向，并让选择在全曲面相容。局部参数叉积可给一个选择，但全局可定向性必须另行检查。

###### 段：单位法向量

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:281 -->

在内部正则点将参数叉积归一化，得到垂直于两个切向量的单位法向；参数换序使它反转。参数边界退化时不除以零，零面积例外不影响通量。

###### 段：定向与可定向性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:292 -->

正式定义光滑曲面的连续单位法向选择和可定向性。分片曲面在光滑接合处选同一侧，折角处要求侧向约定相容而无需唯一法向。向上图像和外向球面为例，闭曲面采用外法向；不可全局相容选法向时仍能作面积积分，但不能直接作这里的全局定向通量。

##### 6.4.3.2 积分的定义和可积性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:309 -->

法向分量 $F^\top n$ 是标量，第二类曲面积分是它相对于面积测度的积分。其条件仅要求该分量可测并绝对可积；整个场的范数可积是更强且容易验证的充分条件。

###### 段：通量积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:311 -->

以单位面积穿过的法向分量引出正式定义，保留原通量公式标签。参数叉积需与选定法向相容，反向时校正负号，分片逐片相加。说明通量输出标量，区别于分量分别积分的向量；$dy\,dz,dz\,dx,dx\,dy$ 是按法向解释的有向投影面积分量。

增加局部法向截面上的正交分解图，区分有符号法向标量和法向投影向量；翻转n使前者变号而后者不变，说明通量朝向规则。

###### 段：可积性的要求

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:348 -->

将准确条件写成参数内积的绝对积分有限。由 Cauchy--Schwarz 得 $|F^\top n|\le\|F\|$，范数面积积分有限足以保证通量可积；紧致有限分片曲面上的连续场满足此条件。切向分量不进入通量，故不能将法向可积与各分量可积混同。

##### 6.4.3.3 积分的性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:362 -->

统一固定曲面和法向，并假定相关法向分量可积，然后分别考察场的线性运算、相容定向下的分片累计，以及改变几何朝向和改变参数的差别。

###### 段：加法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:367 -->

固定法向时，场之和的法向分量等于两场法向分量之和，标量面积积分的加法性质给出通量相加；两项法向分量绝对可积保证和可积。

###### 段：减法

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:379 -->

固定法向时，场之差的法向分量等于两场法向分量之差，标量面积积分的减法性质给出通量相减；两项法向分量绝对可积保证差可积。

###### 段：数乘

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:391 -->

固定法向时缩放场等于缩放法向分量，因此常数可提出通量积分号。

###### 段：曲面分割的可加性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:400 -->

有限片采用原曲面定向的限制，内部不重叠且接缝零面积时通量相加。单独反转一片会改变其贡献符号，不能继续声称同一定向求和。

###### 段：法向反转

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:409 -->

固定场与曲面而将法向反转，法向分量随之反号，通量变号，单列相应公式。

###### 段：重参数化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:417 -->

更换参数而保留所选几何定向，参数叉积带行列式，而区域换元使用其绝对值；方向翻转时校正叉积与法向的符号，校正后通量不变。

##### 6.4.3.4 积分的计算

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/09-surface-integrals.tex:423 -->

按先固定法向、再选相容参数、最后积分有向面积内积的顺序计算。图像曲面向上通量为 $\int_D(-P\psi_x-Q\psi_y+R)$，向下时反号；该式已含有向面积，不能再乘一次叉积长度。竖直单位场通过单位参数斜面的通量为 $1$，通过斜面单位圆盘的通量为 $\pi$，与实际面积分别比较。球面径向单位场法向分量为 $1$，外向通量 $4\pi R^2$、内向为负值，为下一节 Gauss 公式核对保留同一例子。

### 6.5 三类积分之间的关系

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:1 -->

本节围绕内部导数的积分何时等于边界积分展开，分别处理平面区域—边界路径、空间区域—边界曲面、定向曲面—边界路径三种几何关系。入口回接一元基本定理，先明确环流累计切向分量、通量累计法向分量，采用一贯的勒贝格积分框架。共同算子和方向前置，三类关系分别给出正式条件、可跟随的局部推导、计算例子和适用限制，最后比较对象与边界。

#### 6.5.1 积分公式中的微分算子

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:12 -->

以已有梯度为起点，为后续边界公式分别建立不同类型的偏导数组合。向量场输入的散度与旋度独立说明；标量函数输入的Laplace算子另设下级标题，避免把输入和输出混为同一类对象。

##### 6.5.1.1 散度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:17 -->

从小长方体各方向的净流入流出引出定义，以一般 d 维向量场为输入，输出为各对应坐标偏导之和的标量函数。径向场与旋转场展示散度的直接计算，说明零散度不等于零向量场，并写出二维形式供Green通量公式使用。

##### 6.5.1.2 旋度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:36 -->

散度为零的旋转场提示净流出不足以记录环流，由此正式定义三维向量场的旋度及其向量输出。以半速旋转场和径向场说明计算，随后单独说明二维标量 Q_x-P_y 等于补零三维场旋度的第三分量。解释法向分量服务于Stokes公式，且算子记号不是普通数值向量的运算。

增加同一圆周上的径向场与旋转场对照，以实际散度、旋转率、通量和环流辨别两种算子，不以零散度误推零场。

##### 6.5.1.3 Laplace算子

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:69 -->

以二阶连续可微标量函数为输入，由梯度后取散度正式定义 Laplace 算子，输出仍是标量函数。给出二次函数计算，并明确其与旋度的对象类型差别，用途是后面的多元分部积分。

#### 6.5.2 边界的定向

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:84 -->

以区域拼接时内部边、面的贡献应抵消为共同问题，分别给出路径方向、外法向和曲面诱导边界方向；每种方向仅在其对应的几何对象上解释。

##### 6.5.2.1 平面区域的正向边界

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:89 -->

先说明简单闭曲线，再以行进时区域在左侧定义正向。外边界逆时针、孔洞边界顺时针，圆环例子说明两圈方向相反。分段相接不增加转角积分，公共边的反向路径积分相消。

##### 6.5.2.2 区域边界的外法向

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:98 -->

通量以法向为输入，区别于行进方向。外法向从区域内部指向外部，孔洞边界指向孔洞；公共面上两侧外法向相反。二维情况仍按同一规则取外法向，但边界累计使用弧长。

##### 6.5.2.3 定向曲面边界的诱导方向

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:104 -->

给定曲面法向后，以右手约定确定边界方向，向上圆盘例子给出逆时针方向。翻转法向需同时翻转边界方向，片间相容定向使公共边贡献抵消。

增加四块公共边抵消与圆环内外边界方向图，说明相容方向的机制并回接Green与Stokes的拼接。

#### 6.5.3 平面区域积分与边界路径积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:122 -->

固定二维向量场和平面区域，把边界的切向累计与法向累计分开，分别联系对应的偏导数组合。

##### 6.5.3.1 Green公式的环流形式

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:127 -->

正式陈述有限条分段 C1 简单闭边界、局部单侧区域、闭包开邻域内 C1 向量场及正向条件，给出环流与区域旋转率积分相等的公式。矩形情形完整使用一元基本定理和Fubini定理证明，并逐条说明四条边的方向。有限矩形拼接的公共边抵消是机制说明，一般规则区域证明明确作为引用。旋转场在单位圆盘上的环流为 2π，保留直接参数化核对。

##### 6.5.3.2 Green公式的通量形式

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:163 -->

先推明外法向与正向切向的有向弧长关系，再正式给出二维散度积分等于边界外向通量的结论。完整证明只需将Green环流形式的场改为 (-F2,F1)。单位圆盘径向场给出 2π 通量并核对参数计算；与零通量、非零环流的旋转场作同一边界上的对照，防止混淆两种积分。

#### 6.5.4 空间区域积分与边界曲面积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:193 -->

从二维通量关系推广到三维区域，边界对象由曲线变为曲面；内部仍累计散度。由此进一步研究标量函数乘积场给出的分部积分。

##### 6.5.4.1 Gauss公式

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:198 -->

正式陈述有限正则 C1 曲面片、有限曲线/点接缝、局部单侧区域、闭包开邻域内 C1 场与外法向条件，保留原散度公式标签。一般经典定理作为引用；长方体情形完整按三个坐标方向用一元基本定理与Fubini定理推导。说明公共面相消不能代替一般区域逼近证明。球面外通量例子保留，由散度和球体积算得 4πR²，与参数化面积核对。

增加相邻立方体的公共面通量图，固定常向量场和相反外法向核对±1抵消，保留特殊机制与一般Gauss定理的论证边界。

##### 6.5.4.2 多元分部积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:253 -->

以一元分部积分的端点项为起点，正式陈述三维规则区域、u 为 C1、v 为 C2 下的区域积分—边界法向项公式。完整证明由 F=u∇v 的散度乘积法则与Gauss公式得到。说明二维版本用Green通量公式同样推出，边界项是否消失由边界条件决定。

#### 6.5.5 曲面积分与边界路径积分

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:278 -->

区别于Gauss的闭曲面，固定有边界的定向曲面，研究旋度法向分量的曲面积分与原场的边界环流，不要求补成闭曲面。

##### 6.5.5.1 Stokes公式

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:283 -->

由向上平面曲面上的Green环流公式进入，正式陈述紧致、可定向的分片 C2 曲面、有限分段 C1 简单闭边界、相容定向及曲面开邻域内 C1 场的条件。说明可定向指公共边诱导方向相反。单个正则参数片的推导先把边界积分写成 A du+B dv，再用链式法则和混合偏导相等得到 B_u-A_v=curl F·(r_u×r_v)，最后应用参数域Green公式。一般曲面拼接的完整论证明确作为引用，不把参数片推导冒充所有边界情形的完整证明。

##### 6.5.5.2 跨接曲面的选择

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:322 -->

从相同有向边界给出相同环流推出，在两个曲面附近场均 C1 时旋度通量相等，从而可改选较简单的跨接曲面。半速旋转场在单位圆盘与外向上半球上的旋度通量均为 π；翻转法向需同时翻转边界方向。替换曲面不得穿过向量场奇点。

增加同一有向单位圆的圆盘与半球跨接图，核对常旋度通量均π但两面面积不同，说明换面保留的是有条件的旋度通量。

#### 6.5.6 积分公式的比较

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-function-analysis/10-integral-relations.tex:346 -->

以表格对照Green环流、Gauss与Stokes三者的内部对象、边界对象及定向，解释Stokes的平面特例与Green通量的二维散度版本。强调任意标量区域积分不会自动具有所列边界表达，须先找到满足条件的导数场。最后以穿孔场和体积零测边界说明定义域、边界值与规则性条件不可忽略；弱导数、边界迹版本未在本节建立。

### 6.6 本章小结

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/06-multivariate-calculus.tex:18 -->

总结共同线性近似与逐方向信息的区别，比较体积、弧长、面积和方向，并说明边界公式的正则性、可积性和定向要求。

## 第7章 最优化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1 -->

正文：[07-optimization.tex](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex)。

补充组织：非线性残差的LM控制局部步长，MM中的IRLS改变残差代价与逐轮权重，STE则改变离散运算的反向规则；三者按各自原问题归入现有求解分支，有限码率—失真取舍回用多目标几何，不新增章。


> 本章范围：保留现有全部层级，以有限维欧氏变量为主；函数作为未知量、流形上的内在优化分别在第二部分相应章节展开。

### 7.1 优化问题的定义与基本性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:40 -->

主要内容：明确可行域、目标与解，分别检查最优值能否达到、候选是否最优，以及凸性和曲率怎样支持唯一性与误差界。节首说明把一个实际问题写成优化问题需要四项约定——变量、可行域、目标函数、是否要求达到最优，其中任一项改动都会改变答案；并要求把“最优值是多少”与“是否有可行点达到”分开报告（$\min_{w\in[0,1]}w$与$\min_{w>0}w$的最优值同为$0$，结论却不同）。

论证与表述逻辑：

1. 优化问题与解：一个优化问题必须同时给出目标函数、变量和可行域。
2. 最优解的存在：即使暂时不知道如何求解，也能选择一列目标值越来越接近下确界的候选，称为最小化序列。有限下确界$m$时，可逐项选取$F(\boldsymbol w^{(k)})\leq m+1/k$；若下确界为$-\infty$，则可逐项要求$F(\boldsymbol w^{(k)})\leq-k$。
3. 凸性条件下的最优解性质：凸性支持由局部到全局的最优性，严格凸性排除多个最小点，强凸性再以统一曲率常数控制误差；这些保证不能互相替代。

#### 7.1.1 优化问题与解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:45 -->

主要内容：规定变量、可行域、目标及近似标准，再区分目标差、参数距离和预测差。可行域是满足约束的变量集合，目标函数可同时含样本损失和正则项，不能把可行域混称为约束、把完整目标缩称为损失。

论证与表述逻辑：

1. 先区分全局与局部最优、最优值与最小点，再把目标值$\varepsilon$近似与小梯度的近似驻点分开。$10^{-8}x^2/2$在$x=10^6$处梯度仅$0.01$，目标差仍为$5000$；把残差转成目标差或距离须另带定量条件与常数。
2. 在同一个正则最小二乘问题中分别写出目标差、参数差和预测差，说明不同误差对象不能互换；再引入适当扩展实值函数与约束指标，用$+\infty$把不可行点排除，以统一有约束与复合目标的表达。

#### 7.1.2 最优解的存在

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:150 -->

主要内容：通过最小化序列和紧子集取得最小点，说明闭域、下半连续及强制性分别补上的条件。

论证与表述逻辑：

1. 最小化序列只保证目标值趋向下确界，不自动给参数极限；紧致域上连续函数达到极值。进一步以下半连续性允许极限点向下跳，但不允许其值高于邻近极限下界。
2. 对非空闭可行域上的适当、下半连续、强制目标，取一个有限值的下水平集；强制性使其有界，下半连续使其闭，有限维紧性遂使最小化序列有域内极限并达到有限最小值。存在性仍没有规定求解方法或唯一性。

图解与表述作用：下水平集图比较全实线上的$x^2$与$e^{-x}$：前者的$K_1=[-1,1]$有界，后者的最小化序列$x_n=n$逃向无穷远且下确界不达到。图解强制性在存在性证明中的职责，不把强制性表述为所有最小点存在的必要条件。

#### 7.1.3 凸性条件下的最优解性质

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:209 -->

主要内容：依次讨论凸性、严格凸性与强凸性怎样支持全局最优、解唯一和定量误差控制。

论证与表述逻辑：

1. 先用凸函数的全局支撑关系解释局部最优为何也是全局最优。
2. 增加严格凸性排除两个不同最小点，再增加强凸下界，把目标值差转成距离或收敛分析可用的量。

##### 7.1.3.1 凸性与全局最优

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:212 -->

在凸函数不等式后就地解释加权平均：两个非负系数之和为1，分别表示两个端点值在平均中所占的份额。

主要内容：局部最优只比较附近候选；要把这项保证扩展到全部可行域，需要让远处更优的候选也能影响附近的比较。正文用两个互相隔开的山谷建立直觉：普通函数的一个谷底可能只是局部更低；凸性保证远处若有更低点，连向它的线段就在当前点附近给出下降方向，从而排除假谷底。若任意两个可行点之间的线段都可行，而且沿线段的目标值不超过两端值的加权平均，任何更优端点都会给出附近的下降方向。

论证与表述逻辑：

1. 命题（凸函数的一阶与二阶判据）：设$C$为开凸集。可微函数$f:C\to\mathbb{R}$凸，当且仅当对任意$\boldsymbol{u},\boldsymbol{v}\in C$，$f(\boldsymbol{v})\geq f(\boldsymbol{u}) +\langle\nabla f(\boldsymbol{u}),\boldsymbol{v}-\boldsymbol{u}\rangle$若$f$二阶可微，则这又等价于$\nabla^2f(\boldsymbol{w})\succeq\boldsymbol{0}$对所有$\boldsymbol{w}\in C$成立。
2. 推导：若$f$凸，令$\phi(t)=f(\boldsymbol{u}+t(\boldsymbol{v}-\boldsymbol{u}))$。由凸性，$[\phi(t)-\phi(0)]/t\leq\phi(1)-\phi(0)$。
3. 凸性还把最优性变成可核验的一阶条件。因此凸问题的驻点是全局最小点。

##### 7.1.3.2 严格凸性与解的唯一性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:308 -->

主要内容：凸函数可以沿某个方向保持不变，局部到全局的保证并没有排除多个最小点。若希望排除这种平坦的最优线段，需要把不同点之间的凸性不等式加强为严格不等式。

论证与表述逻辑：

1. 若两个不同点$\boldsymbol u,\boldsymbol v$都达到最小值$m$，严格凸性使其中点的函数值严格小于$(m+m)/2=m$，矛盾。

##### 7.1.3.3 强凸性与误差控制

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:327 -->

主要内容：以统一曲率下界加强严格凸性，并据此控制目标差、参数误差及扰动敏感性。正文先说明严格凸只要求“中点严格更低”却没规定低多少，浅口碗与深漏斗可同为严格凸；这一“低多少”决定目标差能换回的参数误差和算法收敛快慢。

论证与表述逻辑：

1. 先在一般范数下定义强凸的弦段间隔，再在欧氏光滑情形给出一阶与Hessian刻画；一般范数平方不必是欧氏二次型，不能直接把Hessian写法当通用定义。强凸下界给出最小点唯一性与目标差对距离平方的控制。
2. 在正则最小二乘中比较零空间平坦与正曲率。为解释逆Hessian的放大界，陈述实对称矩阵可沿完整单位正交特征方向展开，并明确其证明留在线性代数章；正定使全部特征值为正，最小者控制线性项扰动被解放大的上界。

### 7.2 无约束光滑目标的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:432 -->

主要内容：从梯度下降出发，比较动量、预条件与二阶方法使用的信息、每步代价和收敛条件。

论证与表述逻辑：

1. 基于一阶信息的求解：一阶方法在当前候选附近计算线性变化，借此选择新的参数。梯度下降只用当前梯度；动量和加速还保留已有更新的信息，但基本更新不要求显式构造Hessian。
2. 基于二阶信息的求解：在共同二次例子中，两坐标的曲率相差$16$倍，一个标量步长必须兼顾两个方向。若在局部模型中保留不同方向的曲率，就能分别调整位移，这是一阶方向之外的另一种计算选择。

#### 7.2.1 基于一阶信息的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:444 -->

主要内容：一阶方法在当前候选附近计算线性变化，借此选择新的参数。梯度下降只用当前梯度；动量和加速还保留已有更新的信息，但基本更新不要求显式构造Hessian。

论证与表述逻辑：

1. 基于梯度下降的求解：负梯度只保证足够小的位移在当前点附近下降，不能直接确定有限步长。为了给出可用的步长范围，需要控制移动后梯度会改变多少。
2. 基于动量与加速的求解：对二次函数$f(\boldsymbol{w})=\frac12\boldsymbol{w}^{\top}\boldsymbol{H}\boldsymbol{w} -\boldsymbol{c}^{\top}\boldsymbol{w}$，设$\boldsymbol H\succ\boldsymbol 0$，则唯一最小点为$\boldsymbol w^\star=\boldsymbol H^{-1}\boldsymbol c$。

##### 7.2.1.1 基于梯度下降的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:455 -->

主要内容：用梯度Lipschitz条件控制有限步下降，再按一般光滑、凸与更强误差条件分别取得有限预算保证。正文以“梯度只告知哪边最陡，却不知坡势多远后变缓转弯”说明梯度不含步长信息，并指出光滑常数$L$给“每移动单位距离梯度最多改变多少”定上限，从而支撑$1/L$量级的安全步长。

论证与表述逻辑：

1. 沿位移线段积分得到下降引理，选择步长后把单步目标下降累加成最佳梯度残差界；凸目标再用到最小点的距离递推获得目标差$O(1/T)$，回溯通过可核验的不等式寻找可接受步长。
2. PL条件把梯度平方定量压住目标差，配合光滑下降可得目标差几何收敛；它不自动给出参数唯一或参数距离收敛。强凸又可支持距离控制，使用时带上相应常数。
3. 对共同二次目标逐坐标核对步长：较大曲率限制统一步长，振荡下降、等幅振荡与发散由各方向的乘子决定，不能从负梯度方向直接推断任意有限步长下降。

图解与表述作用：步长图固定$f(w)=w^2/2$、$w^{(0)}=1$，用精确式$(1-\eta)^t$比较$\eta=0.5,1.5,2,2.1$的同侧收缩、换侧收缩、等幅振荡与发散；稳定边界为$2/L$。

##### 7.2.1.2 基于动量与加速的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:680 -->

主要内容：比较历史方向与前瞻梯度怎样改变更新，并用二次递推及势函数解释相应收敛条件。正文用小球在又陡又窄的滑槽里左右撞击、沿槽前进很慢类比梯度在狭长谷底的摆动，由此引出对历史方向取平均的动量。

论证与表述逻辑：

1. 动量法每轮用一次当前梯度和历史方向；对正定二次目标沿特征方向得到二阶标量递推，核对稳定范围与优化参数，二次目标的结论不自动推广到一般非二次目标。
2. 对凸$L$光滑且最小点存在的目标，Nesterov在前瞻点求梯度。证明选择当前点与最小点的凸组合，令比较权重与$q$递推相配，再用辅助点统一相邻两步距离；这些点仅用于证明，不增加算法计算。
3. 显式核对$E^{(1)}\leq E^{(0)}$和$E^{(2)}\leq E^{(1)}$的启动，再用$q^{(t)}(q^{(t)}-1)=(q^{(t-1)})^2$把旧目标差与旧距离接成不增势函数，得到$O(1/T^2)$目标差。目标未必逐轮单调，一般凸速率也未指定参数距离速率。

#### 7.2.2 基于二阶信息的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:829 -->

主要内容：在共同二次例子中，两坐标的曲率相差$16$倍，一个标量步长必须兼顾两个方向。正文以“梯度只说往哪边倾斜，曲率才说再走一步坡面转多少”的类比说明二阶信息：一阶方法用同一标尺对待所有方向，缓坡太慢、陡坡冲过头；若在局部模型中保留不同方向的曲率，就能分别调整位移，这是一阶方向之外的另一种计算选择。

论证与表述逻辑：

1. 基于牛顿与Gauss–Newton更新的求解：前章的二阶展开把当前点附近的目标近似为关于位移$\boldsymbol p$的二次函数。曲率矩阵正定时，这个模型有唯一最小点，可以用该点的位移作为更新方向。
2. 基于拟牛顿更新的求解：完整Hessian可能难以获得，但走过一步后，已经知道位移与梯度变化。拟牛顿法（quasi-Newton method）用这两份信息修正曲率模型，不显式计算Hessian矩阵。

##### 7.2.2.1 基于牛顿与Gauss–Newton更新的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:837 -->

主要内容：最小化局部二次模型形成Newton方向，再在非线性最小二乘中比较Gauss–Newton近似、位移阻尼和实际下降的接受规则。

论证与表述逻辑：

1. 正定Hessian使二次模型有唯一最小位移，实际执行解线性方程而非显式求逆；配合试探步长或阻尼处理模型与原目标的差异。Hessian有统一正下界且局部Lipschitz时，足够近初值的误差满足二次递推，局部速率不等于全局保证。
2. 将最小二乘Hessian拆成$J^\top J$与残差加权二阶项，Gauss–Newton舍去后者；零残差、满列秩与邻域正则性支持局部二次误差，残差不小或Jacobian病态时需重查近似和线性系统。

###### 段：残差线性化下的阻尼控制

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:929 -->

主要内容：从Gauss–Newton线性化可能走出可信邻域进入LM，把步长惩罚与永久参数正则分开。阻尼使子问题严格凸并限制位移；与信赖域的乘子条件逐项核对，固定半径仍需选择相容阻尼。

论证与表述逻辑：用原残差模型的预报下降作分母、真实目标下降作分子，给出接受/拒绝及阻尼增减的连续流程；预报非正与驻点另行处理。沿同一残差w²−4比较无阻尼和阻尼步，实际复算目标与77/48下降比，不把单次接受写成全局收敛保证。

##### 7.2.2.2 基于拟牛顿更新的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:959 -->

主要内容：用位移和梯度差更新曲率模型，并把拟牛顿近似与一般预条件的职责分开。

论证与表述逻辑：

1. 割线条件要求近似曲率解释刚走过的一步；BFGS更新在正曲率条件下保持正定，证明分别控制两个组成项。保存全矩阵与有限历史的存储、运算代价不同，不能只因未显式求Hessian就忽略这些成本。
2. 对正定预条件矩阵作可逆坐标变换，变换后的Hessian决定稳定步长及最坏收缩因子；相似变换保留特征值可由特征向量的坐标变换直接核对。预条件改变方向尺度，也可用于迭代解Newton方程，不必是Hessian近似逆。

### 7.3 无约束非光滑目标的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1181 -->

主要内容：面对不可微目标，先用凸次梯度构造更新，再用Clarke广义梯度描述非凸驻点，并以邻近映射构造更新，比较可计算条件及相应的收敛保证。

论证与表述逻辑：

1. 基于次梯度的求解：绝对值损失和$\ell_1$稀疏惩罚在零点不可微，因而不能直接代入普通梯度更新。凸函数仍可用全局仿射下界描述：允许同一点有多个支撑斜率，就能保留用于比较目标值的方向信息。
2. 基于邻近映射的求解：完整保留尖点两侧的函数形状，加二次距离代价求折中点；软阈值的精确零区间来自子问题平衡，而非任取一条次梯度更新。

#### 7.3.1 基于次梯度的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1191 -->

主要内容：以凸函数的全局仿射支撑构造次梯度更新，并通过加权距离递推取得有限预算界。 正文先点明$|x|$在$0$处左右斜率为$-1$与$+1$、不存在能同时描述两边的导数，因此无法套用普通梯度更新；再由“过该点且处处不超过函数的支撑直线在尖点处不止一条”引出次梯度集合。用$|x|+|y|$说明$(0.5,0)$处次微分为$\{1\}\times[-1,1]$，$(1,0)^\top$只是一个选择；区分不保证单步下降与可评价加权平均或历史最佳点。

论证与表述逻辑：

1. 绝对值尖点允许一段支撑斜率，零属于次微分等价于凸最优；次微分也可能为空，任意负次梯度方向未必单步下降。与局部Lipschitz函数的Clarke梯度、人工反向替代信号比较时保留各自定义和适用结论。
2. 在可行参照距离与沿途次梯度范数有界的条件下，展开一步距离平方并累加，得到步长加权平均与最佳候选的目标差界。累计步长是平均的总权重，平方步长和控制平方更新代价；实际路长还含次梯度范数，不能用累计步长代替。

图解与表述作用：沿负次梯度的解析图固定$f(x,y)=|x|+y/2$、$\bm g=(1,1/2)^\top$，对$t\geq0$比较真实值$3t/4$与支撑下界$-5t/4$，说明全局下界有效并不意味着所选方向下降。

#### 7.3.2 非凸目标的驻点

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1290 -->

局部Lipschitz条件由邻近可微点给出有界斜率。先定义一元Clarke广义梯度，再比较广义驻点与凸最优条件，最后推广到多元；这里陈述移动基点差商与邻近梯度闭凸包的等价性，完整证明指向Clarke教材。

###### 段：一元Clarke广义梯度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1292 -->

收集邻近可微点导数的极限，定义有限凸组合与闭凸包，构造一元广义梯度。再按缩小邻域中的差商上确界定义移动基点方向上导数，说明局部Lipschitz条件保证有限性；仅当前点可导不足以把广义梯度缩成单点，连续可微时才有这一结论。

###### 段：广义驻点

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1334 -->

以绝对值及其相反数得到同一个广义梯度区间，说明含零条件允许局部极大。逐项验证负绝对值在原点没有凸次梯度，配图比较真实函数与候选仿射下界，保留局部信息与全域支撑的区别。

###### 段：多元局部Lipschitz函数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1358 -->

明确按欧氏距离控制函数差的局部条件，陈述多元Rademacher几乎处处全微分结论。指出切片上的例外集合不能直接代替多元证明，完整理论依据指向几何测度教材。

###### 段：多元Clarke广义梯度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1368 -->

在实向量空间中收集邻近梯度极限、凸组合和闭包，并给出移动基点差商的等价表述。沿用正负绝对值的二维例子核对驻点边界；凸性才进一步保证全域仿射下界。

#### 7.3.3 基于邻近映射的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1392 -->

主要内容：完整保留非光滑函数形状并加二次距离项，通过邻近子问题生成更新和残差。正文说明其思路：与其在多个支撑斜率里只挑一个（未必反映尖点两侧全部信息），不如把“尖点附近应走到哪”直接当作一个加了二次距离代价的小优化问题来解。

论证与表述逻辑：

1. 对适当、下半连续凸函数及正步长$\eta$，二次距离使邻近子问题有唯一最小点；最优性条件同时读取尖点两侧的支撑斜率。逐坐标求解$\lambda|w|+(w-z)^2/(2\eta)$得到软阈值，零区间来自所需斜率落在$\lambda[-1,1]$，而非任取原点次梯度走一步。
2. 与二次惩罚的连续缩幅比较，证明邻近非扩张，再建立光滑加非光滑目标的近端梯度及梯度映射停止标准；光滑性、凸性与最小点存在条件分别支持下降和目标差保证。
3. 弱凸性允许加二次项后成为凸函数，在受限步长下使邻近问题稳定；比较同一二次族的强凸、凸且PL、弱凸无下界情形，区分曲率、驻点残差与全局最优。

图解与表述作用：邻近子问题图固定$r(w)=|w|$、$\eta=1$，对$z=0.5,2$同时画完整目标及两项组成，精确最小点分别为$0,1$；图解尖点与二次距离的斜率平衡，区别于随后已有的邻近输入输出映射比较。

### 7.4 有约束优化的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1616 -->

主要内容：围绕可行性与目标质量，比较投影、惩罚、乘子和对偶方法，说明约束残差与最优性应怎样分别核验。节首指出三种做法的共同问题是“怎样在移动方向上体现约束”，并说明各自只保证可行性或目标质量中的一项。KKT条件定义后补出四组条件各自的几何含义：驻点性对应梯度被约束法向抵消，可行性与非负价格分别对应原始与对偶可行性，互补松弛表示只有卡住的约束才标价；乘子法一节说明同一惩罚系数对不同约束影响差别很大，需要反复试算。

论证与表述逻辑：

1. 基于投影的求解：对非空闭凸集$C$，约束指标$\iota_C$适当、下半连续且凸，其邻近子问题只在$C$内比较平方距离。
2. 基于惩罚的求解：投影可能很贵，而违反约束的程度常容易计算。将约束写为$a_j(\boldsymbol w)=0$与$g_k(\boldsymbol w)\leq0$后，可将等式残差与不等式正部写成$V(\boldsymbol w)=\sum_j|a_j(\boldsymbol w)|+\sum_k[g_k(\boldsymbol w)]_+$，再最小化$f+\rho V$。
3. 基于乘子与对偶的求解：有限惩罚系数由任务设定，并不自动等于最优约束的影响。乘子把每项约束对目标的作用写成额外变量：在最优点处，目标变化与约束作用应当平衡。

#### 7.4.1 基于投影的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1624 -->

主要内容：对非空闭凸集$C$，约束指标$\iota_C$适当、下半连续且凸，其邻近子问题只在$C$内比较平方距离。

论证与表述逻辑：

1. 推导（最近点的直接几何证明）：任取$\boldsymbol{x}_0\in C$并令$R=\lVert\boldsymbol{z}-\boldsymbol{x}_0\rVert_2$。集合$C_R=C\cap\{\boldsymbol{x}:\lVert\boldsymbol{z}-\boldsymbol{x}\rVert_2\leq R\}$非空、闭且有界，因而在有限维空间中紧。连续函数$\lVert\boldsymbol{z}-\boldsymbol{x}\rVert_2^2$在$C_R$上达到最小值；球外各点到$\boldsymbol{z}$的距离大于$R$，而$\boldsymbol{x}_0$的距离等于$R$，所以该最小点也是$C$上的最近点。
2. 这说明投影不增加到任何可行参照点的距离；两个投影输出间的非扩张性则回用邻近证明。盒约束投影只需逐坐标截断，成本为$O(d)$。
3. 投影保持可行性，软阈值产生稀疏性，二次惩罚改变幅度，它们都可以写成邻近算子，但输出行为和所解决的问题不同。

图解与表述作用：圆盘投影图将$\bm z-\bm p$与$\bm x-\bm p$画在共同起点，外法向与任一可行弦的内积非正，从几何上解释参照距离不增的不等式；图中一个参照点仅用于展示，对所有参照点成立仍由正文证明。

#### 7.4.2 基于惩罚的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1734 -->

主要内容：把约束违反量加到目标中减少直接投影需求，分别检查平方惩罚的极限可行性与绝对残差惩罚的有限参数精确性。

论证与表述逻辑：

1. 比较绝对残差的尖点与平方残差的连续可微性；一般非线性约束的平方不自动凸或全局光滑。在共同二次等式例中，有限惩罚解仍违约，参数增大使违反量趋零却改变曲率和稳定步长，成本不能省略。
2. 一般极限结论要求可行比较点、原目标统一下界及精确子问题；有界子列和下半连续性才把极限转成可行全局最优。若原目标Lipschitz且可行修复距离被违反量控制，超过相应常数的非平方惩罚可有限参数精确。
3. 范数硬约束规定允许范围，正则项按规模计价；报告原目标与违反量而非只看惩罚驻点。普通欧氏梯度中的二次正则等同直接权重衰减，预条件后两者分别带有和不带有矩阵缩放，不能继续混用。

图解与表述作用：罚参数的两个解析分面分别画约束残差$16/(16+17\rho)$和Hessian最大特征值，展示有限参数下残差仍非零以及大参数带来的曲率代价；明确最大特征值不等于条件数，不宣称条件数随参数单调。

#### 7.4.3 基于乘子与对偶的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1813 -->

主要内容：有限惩罚系数由任务设定，并不自动等于最优约束的影响。正文先建立“最优解处把紧约束预算放宽一点点，目标能改善多少”的边际价格直觉，说明乘子不是拍定的罚权而是由问题自身决定的价格；乘子把每项约束对目标的作用写成额外变量：在最优点处，目标变化与约束作用应当平衡。

论证与表述逻辑：

1. 乘子条件与局部最优：资源约束使最优点处的目标梯度不必为零，因为可行方向受到限制。
2. 对偶下界与全局最优：对固定乘子$\boldsymbol{\alpha}\geq\boldsymbol{0}$，任意可行$\boldsymbol{w}$都满足$\mathcal{L}(\boldsymbol{w},\boldsymbol{\nu},\boldsymbol{\alpha})\leq f(\boldsymbol{w})$。
3. 乘子更新与原始—对偶求解：KKT是判据，对偶值是证书，它们还没有规定怎样更新未知的乘子。把乘子合记为$\boldsymbol y=(\boldsymbol\nu,\boldsymbol\alpha)$，允许域为$Y=\mathbb R^m\times\mathbb R_+^p$。
4. 约束变化与解的敏感性：在$1<\tau<3$时，$d\boldsymbol{w}^{\star}/d\tau=(1/2,1/2)^{\top}$；在$0<\tau<1$时则为$(1,0)^{\top}$。

##### 7.4.3.1 乘子条件与局部最优

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:1825 -->

主要内容：由可行扰动的几何限制导出乘子平衡，明确KKT必要性与充分性所需的不同条件。

论证与表述逻辑：

1. 先对仿射等式说明$\ker A$是与每一行正交的扰动集，行空间为$\operatorname{range}(A^\top)$；有限维正交分解给出$(\ker A)^\perp=\operatorname{range}(A^\top)$，所以最优点梯度可用等式法向量组合，等式乘子不受符号限制。
2. 不等式在活跃边界只限制一侧可行移动；由Lagrangian给出驻点、原始可行、对偶可行和互补松弛四组KKT关系。独立性等资格条件支持局部最优的乘子必要性；$x^2\leq0$说明退化梯度为何会使线性化失真。
3. 目标与不等式凸、等式仿射时，支撑不等式使KKT候选全局最优，这项充分性不另依赖Slater；同一预算例逐项求出活跃集、解与乘子，为后续敏感性分析提供依据。

图解与表述作用：法向平衡图沿用$(w_1^2+16w_2^2)/2$及$w_1+w_2=1$，在$(16/17,1/17)$画目标等值线、可行直线与等长反向的$\nabla f,\nu\nabla a$；$\nu=-16/17$说明等式乘子不受非负限制。

##### 7.4.3.2 对偶下界与全局最优

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:2012 -->

主要内容：从弱对偶构造上下界证书，再沿仿射分离与重建建立强对偶的工具及条件。

论证与表述逻辑：

1. 对非负不等式乘子把Lagrangian对全部原变量取下确界，取得原最优值下界$L$；原始可行候选给上界$U$，因此$0\leq U-p^\star\leq U-L$。内层点可能不可行，近似内层函数值也不能直接当可信下界；某组乘子值为负无穷不等于乘子域为空。
2. 由闭凸集投影证明集外点严格分离，再用仿射下界定义共轭、双共轭并证明有限维Fenchel–Moreau。随后证明有限生成锥闭与多面体线性像仍为多面体，由分离得到Farkas择一证书，再证明可行且有限最优值的线性规划原、对偶均达到同值。
3. 对一般凸问题引入共同有效定义域的相对内部，再引用Slater强对偶：仿射等式、严格可行点和有限最优值保证零间隙与对偶达到。本章未展开一般Slater证明；$e^x$例子说明这些条件不额外保证原始最小点达到。

##### 7.4.3.3 乘子更新与原始—对偶求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:2445 -->

主要内容：把对偶证书转为乘子更新，说明内层求解、约束残差和原始可行恢复各自的作用。

论证与表述逻辑：

1. 给定乘子先求Lagrangian内层最小点，再用等式残差与不等式残差形成对偶上升方向，对不等式乘子投影保持非负。对偶凹性给次梯度式界；$-q$光滑时可回用投影梯度的目标差速率，内层唯一及曲率条件须支持所用光滑常数。
2. 最优乘子也不使任意内层最小点自动成为原解；原始可行性和互补松弛仍需核对。用共同例子追踪残差、原始与对偶值，分开乘子收敛、下界改善与恢复可行候选。

##### 7.4.3.4 约束变化与解的敏感性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:2525 -->

先从内部无约束解说明隐式求导与最优值求导的区别，再纳入约束预算、活跃集和KKT系统。

主要内容：研究约束参数变化时解向量与最优值的不同响应，并说明活跃集切换和乘子达到的边界。

论证与表述逻辑：

1. 在同一预算例中逐段计算解导数与值导数，后者为预算乘子的相反数；活跃集在切换点改变，解可以连续而不可微，约束取等号也未必有正乘子。
2. 固定活跃集后对完整KKT系统隐式求导，要求其Jacobian可逆，不能仅查原目标Hessian。约束梯度满行秩、切空间上Lagrangian曲率正定及严格余量支持局部分支；只有该分支保持全局最优，局部值导数才等于全局最优值导数。
3. 原、对偶均达到且零间隙时，用最优乘子匹配硬约束和惩罚目标；反向可从某个惩罚最小点构造相应半径，但不保证参数一一对应。超过达到乘子大小的绝对残差惩罚可有限参数精确，二次惩罚则可能只在极限可行。

###### 段：无约束目标的包络导数

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:2528 -->

用带参数的严格凸二次目标，分别通过隐函数方程和显式解计算最优解导数，再用链式法则计算最优值导数。内部驻点使决策变量的一阶导数项消失，但解导数本身仍存在；边界、多解或约束情形需要重新核对。

###### 段：预算约束的敏感性

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:2573 -->

沿原预算例逐段计算解坐标、最优值和乘子，说明最优值对预算的导数等于预算乘子的相反数。再把固定活跃集的KKT系统视为隐式方程，在正则条件下求局部解导数；切换处不能直接沿用同一支路。

### 7.5 计算预算有限时的近似优化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:2658 -->

主要内容：说明约束松弛、代理目标、分块更新与近似信息各省去了哪些计算，以及相应的近似误差怎样受到控制。

论证与表述逻辑：

1. 基于约束松弛的近似求解：正文以选课变量只能取$0$或$1$、孤立点上无斜率、无法沿梯度移动引出凸松弛。现在还需区分两件事：连续集合能否精确包住原候选，以及返回的连续最优点能否恢复为原问题的解。把原候选的加权平均一并纳入，可以得到包含这些候选的最小凸集。
2. 基于代理目标的近似求解：梯度下降利用一个可计算二次上界。若上界来自别的可解结构，同一下降逻辑也能使用，而不要求变量分块或目标本身是二次函数。
3. 基于分块更新的近似求解：若变量自然分成$\boldsymbol{u}$与$\boldsymbol{v}$两组，可以固定一组更新另一组。
4. 基于近似更新的求解：有限和目标$F_S(\boldsymbol{w})=\frac1n\sum_{i=1}^n\ell_i(\boldsymbol{w}) +\frac{\lambda}{2}\lVert\boldsymbol{w}\rVert_2^2$的经验损失梯度要读取全部$n$项。

#### 7.5.1 基于约束松弛的近似求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:2663 -->

主要内容：比较精确凸包与较大连续松弛，分别核验最优值、求解器返回点及可行恢复。 在三点集$S=\{(0,0),(1,0),(0,1)\}$中，分数点$(1/2,1/2)$只属于凸包；它与原候选$(1,0)$同为目标值$1$，说明最优数值保持不等于返回点原本可行。

论证与表述逻辑：

1. 有限点集的凸组合给最小包含凸集，线性目标值是候选值的加权平均，因此精确凸包保持最优值；其最优面是原最优点的凸包，仍可含分数最优点。整数极点存在不保证任意输出直接取整可行。
2. 局部线性松弛可能大于精确凸包，产生依目标而定的整数间隙；半正定提升用矩阵变量放宽乘积等式，同时增加$O(d^2)$存储与锥求解成本。连续扩展也须单独检验凸凹性，不能由次模名称自动推出。
3. 在同一容量例中检查分数最优、向上取整违约与向下取整损失；以可行上界和松弛或对偶下界的差形成停止证书，不能用松弛值替代可行解质量。

#### 7.5.2 基于代理目标的近似求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:2788 -->

主要内容：梯度下降利用一个可计算二次上界。正文把MM概括为“以退为进”：原目标形状复杂、没有闭式最优步长，便造一个在当前点贴合且处处盖住它的简单函数，最小化它可保证原目标不增；若上界来自别的可解结构，同一下降逻辑也能使用，而不要求变量分块或目标本身是二次函数。

论证与表述逻辑：

1. 定义（主化代理与MM更新）：给定目标$F:C\to\mathbb R$、当前点$\boldsymbol w^{(t)}\in C$，主化--最小化方法（majorization--minimization, MM）在当前点$\boldsymbol{w}^{(t)}$构造代理函数$Q(\boldsymbol{w}\mid\boldsymbol{w}^{(t)})$，满足$F(\boldsymbol{w})\leq Q(\boldsymbol{w}\mid\boldsymbol{w}^{(t)}), \qquad F(\boldsymbol{w}^{(t)})=Q(\boldsymbol{w}^{(t)}\mid\boldsymbol{w}^{(t)})$上界关系要求对所有$\boldsymbol w\in C$成立。若新点$\boldsymbol w^{(t+1)}\in C$满足代理值不增，就称这一步为MM改善更新。
2. 此时$F(\boldsymbol{w}^{(t+1)}) &\leq Q(\boldsymbol{w}^{(t+1)}\mid\boldsymbol{w}^{(t)})\\ &\leq Q(\boldsymbol{w}^{(t)}\mid\boldsymbol{w}^{(t)}) =F(\boldsymbol{w}^{(t)})$第一步用全局上界，第二步用代理改善，最后一步用切触条件。
3. 同一数值例中，代理为$Q(x\mid1)=(x-1/2)^2+1/4$。若只求到$x=3/4$，其代理值为$5/16<1/2$，原目标为$9/32$，仍严格改善；若返回$x=5/4$，代理误差为$9/16>\Delta^{(t)}=1/4$，原目标反而升为$25/32$。

###### 段：偏大残差下的代价控制

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:2873 -->

主要内容：平方代价使少量偏大读数支配拟合，改用ρ(r²)/2重新规定目标。以Cauchy和Tukey给出尺度、残差斜率与再下降行为，解释非凸性和初始化条件；目标改动不自动产生统计抗污染保证。

论证与表述逻辑：先保持同一残差，再改变代价增长并比较残差方向的边际代价；实际参数梯度还要乘残差Jacobian，不能仅由大残差判断参数更新作用。尺度与残差同单位，不能脱离单位解释阈值。

###### 段：二次代理下的残差重加权

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:2885 -->

主要内容：对非减、可微且关于平方残差凹的ρ，用切线上界构造加权平方残差，得到IRLS的权重—求解—重算流程。

论证与表述逻辑：由凹性推导非负权重ρ′(r²)，线性残差给加权最小二乘，非线性残差的内层仍需验证完整代理改善。常数拟合0、0、10给出首轮10/203，全部零权重说明信息丢失；MM目标下降与全局最优、永久正则及步长阻尼分别限定。

#### 7.5.3 基于分块更新的近似求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:2902 -->

主要内容：按变量块或可分副本减少每次求解范围，并区分同一原目标下降与对偶协调。

论证与表述逻辑：

1. 逐块降低同一个目标可得目标单调，耦合正定二次例有收缩递推；$(uv-1)^2$的零初值反例说明逐块精确和分别凸都不单独保证全局最优。无约束可微时，块最优给驻点，联合凸再给全局最优，仍须证明实际迭代到达块最优。
2. 复制变量后以一致性约束协调子问题，用乘子残差上升改善对偶而不保证原目标逐轮下降；强凸或有界残差分别支持相应速率。近似内层误差进入加权累计项，可信下界要从内层值减去误差界，并另查副本恢复可行性。
3. 有限支持上的分布块是概率单纯形中的变量，更新须保留归一化、非负与支持约束；以二点投影给出具体更新，概率方法的进一步对象留到后续卷。

#### 7.5.4 基于近似更新的求解

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:2999 -->

主要内容：通过抽样或近似梯度减少读取量，并把有限步误差、轨迹偏差和数据替换稳定性分别累计；末尾以离散前向的替代反向更新说明另一种近似不自动满足光滑下降条件。

论证与表述逻辑：

1. 均匀抽样给无偏梯度，非均匀抽样须按$1/(np_I)$重加权，确定正则项无需抽样。固定历史后的独立抽样平均降低波动但不自动消除偏差；这里只建有限加权接口，长期随机收敛需后续概率条件。
2. 确定更新误差在光滑下降中贡献步长加权的平方范数和，取得最佳驻点残差界；比较两条轨迹却需要一次范数误差和及更新映射传播因子。统一压缩、仅非扩张和膨胀分别给不同结论，逐项小于一不保证乘积趋零。
3. 以共同抽样索引耦合仅差一个样本的数据集，在逐样本凸光滑、梯度有界等条件下取得期望参数距离界；测试损失Lipschitz条件才把它转为损失差。这是稳定性接口，不能代替算法收敛。
4. 裁剪和预条件下直接衰减可引入确定偏差，扩大批量不会自动消除；非负光滑损失的下降引理给梯度自界，但需沿途损失已有上界才能得到所用梯度常数。总成本还应计入样本、试探、局部子问题和恢复。

###### 段：替代梯度

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:3185 -->

主要内容：先定义替代梯度为算法指定的反向信号，并区分它与经典导数、凸次梯度及前向函数的有限差分；再以round前向和恒等反向解释STE的具体计算。真实导数局部为零，指定斜率仍可推动跨阈值。

论证与表述逻辑：同一w=0.2分别用a=1与a=0.4复算损失下降和上升，说明不能直接套用光滑下降证明；再用停止传播标记说明向量量化怎样保留码向量前向并指定单位反向，区分计算图规则、经典函数及有限差分核验。

### 7.6 多目标、对抗与双层优化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:3202 -->

主要内容：在多个指标、对抗选择及嵌套问题中重新明确解的含义，讨论Pareto取舍、极小极大次序和内层选解的影响。

论证与表述逻辑：

1. 多目标优化：一个标量不能完整表示互相竞争的任务，需先规定怎样比较损失向量。
2. 极小极大优化：另一类问题让两个变量方向相反：$\min_{\boldsymbol{w}\in W}\max_{\boldsymbol{z}\in Z}\phi(\boldsymbol{w},\boldsymbol{z})$。正文以生成对抗（生成方造假、判别方识破）与鲁棒训练（决策者降损、扰动方抬损）引出：决策者先定策略、对手看到后选最狠回应，故按“最坏情况下仍有多好”评价；外层先选择$\boldsymbol w$，内层在看到它后选择使损失最大的$\boldsymbol z$。
3. 双层优化：有些决策必须先经过一次学习过程才能评价。正文以超参数调优为例：真正决定外层损失的是内层训练结束后的参数，外层变量先改变内层解、再间接影响评价，因而是嵌套结构，不能合成一个普通优化问题。令外层变量为$\boldsymbol\theta\in\Theta\subseteq\mathbb R^p$，其中$\Theta$是给定的非空允许集合，内层变量取遍$\mathbb R^d$。

#### 7.6.1 多目标优化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:3211 -->

主要内容：以损失向量的支配关系定义Pareto取舍，再比较加权标量化与共同下降的一阶信息。

论证与表述逻辑：

1. 严格正权重的全局加权最小点是Pareto最优，允许零权重通常只保弱Pareto；三个可行损失向量例子说明非凸前沿上的Pareto点可能无法由任何加权和选到。
2. 证明无共同严格下降方向等价于零在梯度凸包中，反向利用分离定理；此判据只排除一阶共同改善，不保证全局Pareto。将零投影到梯度凸包可求共同方向，光滑条件支持统一下降步长；有约束时还需可行方向限制。

###### 段：有限工作点下的预算取舍

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:3309 -->

主要内容：把已有Pareto前沿与支撑点结论用于有限码率—失真方案，区分预算约束与加权和，保留混合是否实际可行的条件。

论证与表述逻辑：回访已有三点反例而不重复定理；在可支撑的光滑下降曲线上由D′(R)+λ=0解释斜率，在成本可加且选择独立时才逐块分解。概率率失真函数仍需后续信息论前提。

#### 7.6.2 极小极大优化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:3317 -->

主要内容：将最坏响应、优化次序与全局鞍点分开，以原始—对偶间隙核验候选并检查更新动力学。用固定样本$(\boldsymbol x,y)$上的特征扰动$\boldsymbol\delta\in\Delta$明确鲁棒训练的角色：扰动集合非空紧致且损失关于扰动连续时，内层最大化$\ell(\boldsymbol w,\boldsymbol x+\boldsymbol\delta,y)$的最大值能达到，外层选择模型参数降低最坏损失；标签保持不变，允许的扰动由集合给出。

论证与表述逻辑：

1. 先定义全局鞍点不等式及候选最坏上界、最好下界，零间隙给出鞍点；它不同于单个函数由Hessian正负曲率刻画的微分鞍点。非空紧凸域与连续凸凹目标支持最值达到和值交换，证明用有限覆盖、分离及凸组合逐步取得反向界。
2. 即使存在零间隙鞍点，同时梯度下降—上升仍可能旋转发散；双线性盒约束例既有无投影的范数增大，也有投影后的周期。最优值存在定理不自动保证算法收敛。
3. 外梯度先试探再校正，增加一次方向求值与投影；在给定小初值和步长的双线性例中核对投影未激活、距离因子小于一，证明该例收敛。一般映射仍需另查单调性、Lipschitz等条件，不能由多算一次方向自动推广。

图解与表述作用：轨迹与距离平方图对$\phi(x,z)=xz$固定步长$1/2$及初值$(1/2,0)$，比较无投影同时下降—上升与外梯度。两者距离平方因子分别为$1+\eta^2$、$1-\eta^2+\eta^4$；明确蓝线离开盒后只是无投影计算，绿线试探与校正始终在盒内，故投影未激活。

#### 7.6.3 双层优化

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:3439 -->

主要内容：把内层选解作为外层评价输入，明确不同求导方法所对应的目标与误差。超参数调优的内层训练模型、外层评价训练结果；鲁棒训练的内层求扰动、外层训练参数，二者不能套用同一角色说明。一般嵌套需保留内层最优性，内层最大化可改写为负目标最小化。

论证与表述逻辑：

1. 内层须对每个允许外层参数有最小点，且唯一或已规定单值选择；多解时乐观、悲观或算法选解可能产生不同外层值。有限步展开求的是实际$T$步算法的复合目标梯度，减少前向步数与仅截断反向传播改变的对象不同。
2. 隐函数定理在Hessian可逆时跟踪非退化局部最小分支，以伴随线性方程计算超梯度；只有该分支符合全局选解规则时才对应原双层目标。二次例子直接消元核对公式，有限步导数与精确解导数不必相同。
3. 在局部统一强凸及导数有界、Lipschitz等条件下，将内层驻点残差和伴随线性系统残差分开控制；小曲率同时放大两项。取得明确对象和误差界后，才把外层方向用于前述带误差优化更新。

### 7.7 本章小结

<!-- source: tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/07-optimization.tex:3624 -->

主要内容：区分解的存在、最优性判定、求解过程与误差收敛，归纳选择算法时需要同时检查的结构条件和计算预算。

论证与表述逻辑：

1. 最优化需要分别回答四个问题：候选解是否存在，某个点为何最优，算法怎样到达它，以及误差按什么尺度收敛。连续性配合紧致性保证存在；在闭域上，下半连续性与强制性也能通过紧下水平集保证存在。
2. 共同二次目标$(w_1^2+16w_2^2)/2$展示了这些条件怎样进入计算：统一梯度步受曲率$16$限制，动量改变历史响应，预条件调整两个方向的尺度，牛顿法则直接解曲率方程。
3. 带资源约束后，KKT条件描述目标梯度与约束法向量的平衡，对偶变量提供界和敏感性解释。Farkas证书与线性规划强对偶说明最优值相等需要证明，不能从凸性直接跳得。
4. 计算预算不足时，可以组合代理、分块及近似更新，但必须分别记录误差来源及其累计方式。目标下降中的平方误差和，与轨迹偏差中的一次范数和，控制不同对象；副本一致、块最优和联合最优也需要不同条件。
5. LM以实际下降核验局部阻尼步，IRLS以同一残差目标的切线上界重加权，STE另定离散反向；三者的保证分别检查。有限码率—失真选择回到实际工作点，不把支撑点当作全部预算最优解。

<!-- OUTLINE END -->

---

## 原线性章的内容去向

这张表以实际正文的44个结构节点逐项定位，包括原章、7个section、26个subsection、7个subsubsection和3个paragraph。它用于检查拆分与迁移，不表示原来每个大块仍须保留为单一新小节。实数范围内的定义、证明、例子与图解随其所说明的命题迁移；原文超出实数范围的推广按本轮要求移除，相关一般结论改用实数表述并注明必要条件。

| 原有条目与位置 | 拟归入位置 | 保留的内容与迁移理由 |
| --- | --- | --- |
| chapter：线性空间（[原文第1行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L1)） | 4.1—4.5 | 按表示、运算、方程和优化、分析四部分组织，另设独立小结。 |
| section：元素与表示（[原文第45行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L45)） | 4.1 | 对象包含标量、向量、矩阵与张量；空间建立基维数及坐标，映射建立核像、秩与单满可逆。 |
| subsection：对象与空间的界定（[原文第54行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L54)） | 4.1.1、4.1.2.1 | 实标量、线性空间、抽象向量与矩阵元素的区分。 |
| subsection：对象的坐标表示（[原文第84行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L84)） | 4.1.1.4、4.1.2.2—4.1.2.3、4.2.9—4.2.10 | 张量在对象层先辨认阶与轴，产品基和正式构造归张量积；重排、reshape与向量化单独说明坐标规则。 |
| subsection：坐标的转换（[原文第188行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L188)） | 4.1.4.2、4.1.8.1—4.1.8.3、4.2.2.2、4.2.10 | 被动换基、主动作用及三种矩阵关系分清；数组轴置换、reshape与向量化各自建立索引映射。 |
| section：关系与结构（[原文第268行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L268)） | 4.1.3、4.1.6—4.1.8、4.2.4—4.2.7 | 子空间、对偶、商及坐标关系归表示；长度、体积与配对归对应运算。 |
| subsection：对象集合的包含关系（[原文第292行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L292)） | 4.1.3 | 子空间包含、交、和、维数公式、直和与补空间分别展开；比较范围与独立分量，子空间最小定义仍在4.1。 |
| subsection：对象的位置与方向关系（[原文第319行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L319)） | 4.3.2.1、4.3.3.4 | 仿射解集、基点不唯一及不变的方向空间归精确解集合；仿射与凸组合归等式约束可行集合。 |
| subsection：对象的距离关系（[原文第333行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L333)） | 4.2.4—4.2.5、4.3.4.5、4.3.5.1、4.4.1.1 | 内积、范数和半范数先建立；商上的长度接回表示，奇异值公式、核范数和有限维收敛在对应问题中展开。 |
| subsection：对象的等价关系（[原文第493行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L493)） | 4.1.7、4.2.5.4 | 等价类、商空间与商映射建立代数表示；半范数消除零方向后的长度在范数中建立。 |
| section：运算与映射（[原文第525行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L525)） | 4.1.5、4.1.8、4.2—4.4 | 映射与换基解释表示，基础运算集中于运算节；分解由求解、优化和收敛问题引出。 |
| subsection：空间之间的映射（[原文第540行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L540)） | 4.1.5、4.1.8.1—4.1.8.2、4.2.2 | 定义域／值域选基、核像、秩—零度和单侧逆在基本语言中；换基关系与仿射增广随后建立。 |
| subsection：映射的叠加（[原文第625行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L625)） | 4.2.1.2、4.2.2.2 | 同输入输出映射的线性叠加归加法和数乘，复合的分配律归矩阵乘法，依赖输入权重的非线性边界保留。 |
| subsection：映射的复合（[原文第640行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L640)） | 4.2.2.2、4.2.3.1、4.2.5.2、4.2.6 | 矩阵乘法说明复合与结构化计算，转置、逆与伴随分别说明倒序条件，范数建立后再给乘法近似界。 |
| subsection：对象的联合运算（[原文第668行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L668)） | 4.1.1.4、4.2.2.1、4.2.9—4.2.12 | 张量对象先介绍，张量积、重排、Kronecker与缩约按运算分开；Hadamard归逐项乘法，局部汇集归具体缩约实例。 |
| paragraph：多路输入的秩一读取（[原文第785行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L785)） | 4.2.12.8、4.3.5.1 | 多路读取讲已有因子的应用；秩预算、CP拟合和高阶最佳近似边界由后面的逼近任务承担。 |
| subsection：对象的分解与投影（[原文第846行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L846)） | 4.2.4、4.2.4.5、4.2.6.1、4.3.1、4.3.2.1 | 几何关系与读取表示先建立，伴随归对应运算；正交化、QR和投影构造归最近点优化任务，四个子空间服务可解性。 |
| subsection：对象的标量读取（[原文第1023行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L1023)） | 4.1.6、4.2.3.2、4.2.4.5—4.2.4.6、4.2.6—4.2.7、4.2.12.3 | 对偶读取归表示；迹、内积表示、Frobenius配对、伴随与行列式归各自运算，缩约回用这些实例。 |
| subsection：方阵的幂、指数和平方根（[原文第1199行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L1199)） | 4.2.8、4.3.3.2、4.3.6.2、4.4.1.2、4.4.2.6 | 幂和函数定义归运算；实对称谱在二次极值建立后用于平方根、实幂和对数；实Schur、实分裂Jordan及扰动各归具体问题。 |
| section：方程与优化（[原文第1570行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L1570)） | 4.3 | 精确方程、残差任务与矩阵未知量保留，并补全分类。 |
| subsection：精确约束下的线性方程求解（[原文第1601行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L1601)） | 4.3.2 | 相容性、左零空间反证、x0+ker、形状与秩、单侧逆及最小范数选解。 |
| subsubsection：基于消元与分解的直接求解（[原文第1647行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L1647)） | 4.3.2.3—4.3.2.4 | LU／Cholesky／LDL构造和证明在方阵求解中建立；前代回代、Schur补、规范零空间与低秩更新同实际求解衔接。 |
| subsubsection：基于矩阵分裂的迭代求解（[原文第1817行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L1817)） | 4.3.2.5、4.4.1.3 | Jacobi／GS／SOR的更新与收敛条件分开。 |
| subsubsection：基于Krylov空间的迭代求解（[原文第1894行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L1894)） | 4.3.2.6、4.4.1.5 | Richardson共同机制归4.3.2.5；CG／PCG／GMRES、Arnoldi、预条件和重启保留。 |
| subsection：残差约束下的线性方程求解（[原文第2094行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L2094)） | 4.3.2.2、4.3.4、4.3.4.8 | 最小残差与容限、加权／退化尺度、投影、正规方程、伪逆与两次正交选择。 |
| subsubsection：基于矩阵分解的直接求解（[原文第2273行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L2273)） | 4.3.1.2、4.3.4.4 | QR由子空间投影引入，在那里建立正交化与Householder；矩形求解再补列置换、秩判断及选解。 |
| subsubsection：基于梯度更新的迭代求解（[原文第2320行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L2320)） | 4.3.4.6、4.4.1.4 | Landweber更新、严格步长、初值核分量及零矩阵分别处理，构造与极限分开。 |
| subsection：双侧作用下的矩阵方程求解（[原文第2336行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L2336)） | 4.3.6、4.4.2.6 | AXB及Sylvester、vec／Kronecker和Schur求解；平方根响应回用Sylvester条件。 |
| section：收敛与逼近（[原文第2393行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L2393)） | 4.3.3、4.3.5、4.4.1 | 有限预算最优任务归二次优化和逼近；生成序列的极限、速度与初值条件归收敛分析。 |
| subsection：对象序列的收敛（[原文第2402行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L2402)） | 4.4.1.1 | 坐标／范数／柯西、等价、完备、闭子空间、闭有界紧与最坏值达到。 |
| subsection：反复作用下的幂序列收敛（[原文第2435行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L2435)） | 4.4.1.2 | 实范数幂增长率、暂态增长、固定空间与衰减空间、实分裂条件下的Jordan、旋转及变化矩阵乘积反例。 |
| subsection：求解和优化下的迭代序列收敛（[原文第2483行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L2483)） | 4.4.1.4—4.4.1.5 | LS步长及三类误差、CG多项式／Chebyshev／PCG、GMRES非正规与重启。 |
| subsection：秩约束下的矩阵逼近（[原文第2605行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L2605)） | 4.3.4.5、4.3.5、4.4.2.5 | SVD先服务任意秩选解；Schatten／核范数、低秩最优性、PCA、因子化及误差选秩服务逼近；极分解服务最近正交问题，谱隙服务可靠性判断。 |
| subsection：归一化与定向约束下的估计（[原文第3242行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L3242)） | 4.3.3.2—4.3.3.3、4.3.5.2 | 单位方向和广义度量约束归二次优化，定向映射逼近归最邻近映射问题。 |
| subsubsection：单位范数约束下的方向估计（[原文第3251行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L3251)） | 4.3.3.2—4.3.3.3 | 单位尺度、Rayleigh极值和广义二次约束先说明；齐次方向估计注明多维零空间和可识别性。 |
| subsubsection：定向约束下的正交逼近（[原文第3277行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L3277)） | 4.3.5.2 | 正交Procrustes、最近旋转、det=1修正与零／重奇异值非唯一。 |
| section：扰动与稳定性（[原文第3320行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L3320)） | 4.4.2 | 按误差口径、求解、正则化、谱方向和矩阵函数组织。 |
| subsection：运算的误差传播（[原文第3336行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L3336)） | 4.4.2.1 | 数据／舍入、前向／后向、绝对／相对条件数、浮点和结构扰动。 |
| subsection：线性方程解的稳定性（[原文第3394行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L3394)） | 4.3.4.7—4.3.4.8、4.4.2.2—4.4.2.4 | 正则化与残差约束的目标和算法归最小二乘问题，逆与同秩伪逆、残差、迭代改进及滤波的扰动效果归分析。 |
| paragraph：惩罚相邻变化的一般正则化（[原文第3596行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L3596)） | 4.3.4.7、4.4.2.4 | 相邻差分、一般L、共同核唯一性和增广最小二乘；不套普通SVD滤波。 |
| paragraph：按允许残差选择惩罚参数（[原文第3642行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L3642)） | 4.3.4.8、4.4.2.4 | 目标比较证明残差单调、差异原则、容限范围与尺度条件。 |
| subsection：谱分解的稳定性（[原文第3807行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L3807)） | 4.4.2.5 | 实对称Weyl／Davis–Kahan、实SVD与Wedin、实可对角化条件下对扰动后实特征值的Bauer–Fike、方向簇与PCA边界。 |
| subsection：矩阵函数的稳定性（[原文第4058行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L4058)） | 4.4.2.6 | 非交换插入、差商／指数导数、平方根Sylvester、逆与logdet，微积分部分回读。 |
| section：本章小结（[原文第4207行](../../tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/03-linear-algebra-and-matrix-analysis.tex#L4207)） | 4.5 | 收拢求解对象、计算选择、收敛与可信度的独立证据。 |

## 拟补充的内容与前置边界

原正文的44个结构节点均保留去向。此前补充的LDLᵀ、MINRES、CGLS／LSQR、线性等式约束、张量积及多路计算、Lyapunov和谱方向迭代继续保留；本轮新增的是四部分分工所需的连接，以及无约束、单位球面和闭球二次极值的明确分类。新增内容仍是写作计划，不能据本稿声称正文已经证明或实现。

| 位置 | 当地建立的内容 | 前置条件与回用 |
| --- | --- | --- |
| 4.1 表示 | 对象、基维数、坐标、映射核像秩、对偶与商、换基关系 | 回用第1章的基础算式；不预用范数或分解证明。 |
| 4.2.4—4.2.6 | 内积、加权内积、范数、读取的内积表示及伴随 | 先定义配对，再抽取长度公理；代数对偶与商已建立。 |
| 4.2.7—4.2.8 | 行列式、特征多项式、幂与矩阵函数的定义及计算目标 | 行列式补齐换基不变量；幂级数用实数极限，实对称谱的证明留二次极值。 |
| 4.2.9—4.2.12 | 张量积、重排、Kronecker积与缩约 | 先产品基，再确定索引顺序；缩约明确对偶槽位或内积。 |
| 4.3.1 | 最近点、正交化、QR与投影 | 已有基、内积和正交判据，不依赖SVD。 |
| 4.3.2 | 精确方程、直接分解、定常与Krylov迭代 | 先判可解与唯一，再构造求解；收敛与扰动证明后续回用算法。 |
| 4.3.3 | 二次极值、实对称谱、惯性标准形、等式约束 | 单位球极值用实数逐坐标子列及代数增量，不提前调用微分；谱计算随后支持矩阵函数。 |
| 4.3.4—4.3.5 | 最小二乘、SVD、正则化、低秩及正交映射逼近 | SVD回用实对称谱，先给最优性条件再讲直接与迭代方法。 |
| 4.3.6、4.4 | 矩阵方程、收敛和扰动 | 实Schur保留二维块；算法极限、秩保持、谱隙、允许扰动与定义域分别说明。 |

## 本稿核对结果

- 第一部分仍为七章，其余章节的提要与此前核对稿一致；原1.5.7—1.5.9继续删除。
- 第四章按四个主体部分重组并保留独立小结；原线性章44个结构节点和此前列明的求解方法均有对应位置。
- 编号、父子层级、来源位置、文件链接和章内引用按新结构核对；分解和迭代保留具体问题、成立条件及计算边界。
- 本文件是大纲调整方案。本轮未修改正文或出版成品，未编译、原检查时未提交、未集成（本次归档状态见README）。
