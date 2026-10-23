# “图”部分完整标题层级总览

当前为详细拟稿，正文及出版入口尚未实施。拟设part为“图”，以下五个chapter沿用部分内设计编号；正式卷内章号待实施时连续生成。

[部分主线与五章分工](part-outline.md) · [当前调整说明](README.md) · [自查与验证](outline-check.md)

标题逐项摘自五份详细分稿。subsection/subsubsection按具体方法组织，必要概念入口按需独立；paragraph帮助辨认概念、思想、实现、算例、核验与分析。标题下的实质内容及自然段顺序见分稿。

[详细分稿：第1章拟调整大纲：图的对象与表示](outline-01-objects-representations.md)

## 1 chapter：图的对象与表示

- paragraph：从局部规则到关系对象

### 1.1 section：二元关系的图表示

#### 1.1.1 subsection：顶点、边与方向

- paragraph：无向图
- paragraph：邻域
- paragraph：顶点的度
- paragraph：有向图与弧
- paragraph：入邻域与出邻域

#### 1.1.2 subsection：边的数值与结构

- paragraph：边长
- paragraph：边容量
- paragraph：相似度权重
- paragraph：零权边
- paragraph：正权支撑图

#### 1.1.3 subsection：限制顶点集与诱导子图

- paragraph：诱导子图

### 1.2 section：高阶关系的因子表示

#### 1.2.1 subsection：局部函数与作用域

- paragraph：局部配置与局部函数
- paragraph：作用域

#### 1.2.2 subsection：作用域的三种表示

- paragraph：超边与超图
- paragraph：因子图
- paragraph：二部图
- paragraph：原始关系图
- paragraph：成对投影的信息损失

### 1.3 section：图的矩阵表示

#### 1.3.1 subsection：邻接访问与存储

- paragraph：邻接表
- paragraph：边表
- paragraph：稠密矩阵与稀疏矩阵
- paragraph：邻接矩阵
- paragraph：矩阵乘法的方向
- paragraph：结构掩码

#### 1.3.2 subsection：关联矩阵与边差

- paragraph：关联矩阵
- paragraph：边差的加权汇总

#### 1.3.3 subsection：组合拉普拉斯与沿边变化

- paragraph：加权度
- paragraph：组合拉普拉斯
- paragraph：沿边变化能量
- paragraph：零能量的逐边条件

#### 1.3.4 subsection：归一化算子与度量

##### 1.3.4.1 subsubsection：对称归一化拉普拉斯

- paragraph：度加权内积与坐标缩放
- paragraph：对称归一化拉普拉斯的定义
- paragraph：归一化后的沿边能量
- paragraph：归一化谱界

##### 1.3.4.2 subsubsection：邻域平均与随机游走拉普拉斯

- paragraph：邻域平均算子
- paragraph：随机游走拉普拉斯
- paragraph：两种归一化算子的关系
- paragraph：函数读取与概率质量推送

### 1.4 section：重编号下的结构等价

- paragraph：图同构
- paragraph：置换矩阵与坐标重排
- paragraph：同谱图与同构的边界

### 1.5 section：本章小结


---

[详细分稿：第2章拟调整大纲：图中的路径与连接关系](outline-02-paths-connectivity.md)

## 2 chapter：图中的路径与连接关系

- paragraph：从直接连接到关系查询

### 2.1 section：顶点之间的邻接关系

- paragraph：邻接查询
- paragraph：邻接与边属性

### 2.2 section：顶点之间的路径关系

#### 2.2.1 subsection：行走、路径与环

- paragraph：行走
- paragraph：简单路径
- paragraph：闭行走与无向环
- paragraph：有向路径与有向环
- paragraph：有向无环图
- paragraph：邻接矩阵幂与行走计数

#### 2.2.2 subsection：路径成本与最短距离

- paragraph：路径成本
- paragraph：简单路径最小值与行走下确界
- paragraph：负闭行走
- paragraph：距离查询的三种状态

### 2.3 section：顶点集合的连通关系

- paragraph：无向连通
- paragraph：连通分量
- paragraph：祖先与后代
- paragraph：强连通与强连通分量
- paragraph：弱连通
- paragraph：树
- paragraph：森林

### 2.4 section：条件约束下的分离关系

- paragraph：无向分隔
- paragraph：路径中的碰撞点
- paragraph：给定条件集后的活跃路径
- paragraph：d-分离
- paragraph：分离规则的边界

### 2.5 section：本章小结


---

[详细分稿：第3章拟调整详细大纲：图的遍历、分解与简化](outline-03-traversal-decomposition.md)

## 3 chapter：图的遍历、分解与简化

- paragraph：本章的计算任务
- paragraph：方法的共同输入与计价

### 3.1 section：基于队列与栈的图遍历法

- paragraph：队列
- paragraph：栈
- paragraph：遍历方法的输出

#### 3.1.1 subsection：基于队列的广度优先遍历法

- paragraph：按层扩展的思想与状态
- paragraph：入队标记与逐步实现
- paragraph：贯穿图的队列轨迹
- paragraph：基本分析与选择边界

#### 3.1.2 subsection：基于栈的深度优先遍历法

- paragraph：保持当前分支的思想与状态
- paragraph：深入、回退与回边恢复
- paragraph：三点分支的执行轨迹
- paragraph：基本分析与输出比较

### 3.2 section：无环依赖下的拓扑排序法

- paragraph：拓扑序
- paragraph：排序的输入条件与输出

#### 3.2.1 subsection：基于零入度队列的Kahn排序法

- paragraph：删除已无前驱的任务
- paragraph：初始化与逐弧减度
- paragraph：菱形依赖的轨迹与分析

#### 3.2.2 subsection：基于DFS逆完成序的拓扑排序法

- paragraph：从分支完成次序构造
- paragraph：同图比较与边界

### 3.3 section：基于邻接检索与标签合并的连通标记法

- paragraph：前景位置集合
- paragraph：4邻接
- paragraph：8邻接
- paragraph：分量标签
- paragraph：种子可达标记

#### 3.3.1 subsection：基于BFS重启的分量标记法

- paragraph：一次标记一个可达区域
- paragraph：数例与基本分析

#### 3.3.2 subsection：基于并查集的两遍扫描标记法

- paragraph：临时标签的等价类
- paragraph：并查集
- paragraph：先给临时标签再合并的思想
- paragraph：两遍实现与区域重逢数例
- paragraph：代价与方法比较

#### 3.3.3 subsection：基于种子队列的掩模重建法

- paragraph：掩模
- paragraph：种子
- paragraph：结构元
- paragraph：累计可达集的思想
- paragraph：队列实现与边界

### 3.4 section：基于发现父边的生成森林提取法

- paragraph：生成树
- paragraph：生成森林
- paragraph：父边提取的目标
- paragraph：只保存首次发现的连接
- paragraph：贯穿图抽取与丢失信息

### 3.5 section：基于给定分隔集的局部分块法

- paragraph：给定的候选分隔集
- paragraph：删除后的连通分量
- paragraph：共享接口
- paragraph：局部因子的归属
- paragraph：固定接口后分别处理的思想
- paragraph：删除、标记与加回接口
- paragraph：贯穿图验证与基本分析

### 3.6 section：基于消元补边的树分解法

#### 3.6.1 subsection：树分解的基本概念

##### 3.6.1.1 subsubsection：原图中的团与计算用袋

- paragraph：团
- paragraph：袋
- paragraph：袋间接口

##### 3.6.1.2 subsubsection：树分解与运行交集

- paragraph：树分解
- paragraph：运行交集
- paragraph：团作用域的整袋容纳

##### 3.6.1.3 subsubsection：顶点消元与填充

- paragraph：顶点消元
- paragraph：填充边

##### 3.6.1.4 subsubsection：分解宽度与树宽

- paragraph：分解宽度
- paragraph：树宽

#### 3.6.2 subsection：基于给定次序的补边分解法

- paragraph：从消元接口构造袋的思想
- paragraph：补边删除与父袋连接
- paragraph：同图好坏次序的逐步比较
- paragraph：结构代价与后续表计算

#### 3.6.3 subsection：基于贪心次序选择的补边分解法

- paragraph：用当前局部代价选下一点
- paragraph：局部选择数例与代价边界

### 3.7 section：弦图条件下的团树构造法

#### 3.7.1 subsection：极大团、弦图与团树的基本概念

##### 3.7.1.1 subsubsection：团与极大团

- paragraph：团的读取
- paragraph：完全图
- paragraph：极大团
- paragraph：最大团

##### 3.7.1.2 subsubsection：弦与弦图

- paragraph：弦
- paragraph：弦图
- paragraph：弦化

##### 3.7.1.3 subsubsection：单纯顶点与完美消元序

- paragraph：单纯顶点
- paragraph：完美消元序
- paragraph：完美序的使用条件

##### 3.7.1.4 subsubsection：团树

- paragraph：以极大团为袋的树
- paragraph：团树的接口
- paragraph：原团构造的适用范围

#### 3.7.2 subsection：基于单纯顶点删除的完美序构造法

- paragraph：无填充删除的思想
- paragraph：候选检验与删除实现
- paragraph：四环补弦的算例核验
- paragraph：输出次序的独立核验
- paragraph：正确性依据
- paragraph：复杂度与方法比较

#### 3.7.3 subsection：基于团交集最大权树的接口构造法

- paragraph：以共享变量连接团的思想
- paragraph：从完美序生成极大团列表
- paragraph：建立交集权并选树边
- paragraph：贯穿图及四环的算例核验
- paragraph：计算代价与构造边界

### 3.8 section：基于祖先道德化的d-分离判定法

- paragraph：条件分离查询的输入
- paragraph：祖先闭包
- paragraph：诱导祖先图
- paragraph：骨架
- paragraph：道德图
- paragraph：逆向检索到无向分隔的五步实现
- paragraph：碰撞及另一条通路的逐步查询
- paragraph：代价、表示与查询边界

### 3.9 section：本章小结

- paragraph：访问次序与查询输出
- paragraph：分解的作用与代价
- paragraph：单次分离查询与后续计算

---

[详细分稿：第4章拟调整详细大纲：图上的约束优化](outline-04-constrained-optimization.md)

## 4 chapter：图上的约束优化

- paragraph：同一张图上的不同选择
- paragraph：本章六类方法的分工
- paragraph：可行性与最优性的检查
- paragraph：图规模与访问表示

### 4.1 section：基于递推与松弛的最短路方法

- paragraph：有向输入与无向边转换
- paragraph：简单路径与有限行走的目标
- paragraph：相关负环与负无穷
- paragraph：Bellman距离关系
- paragraph：循环固定点与标签初始化

#### 4.1.1 subsection：DAG拓扑递推法

- paragraph：拓扑顺序的递推思想
- paragraph：按拓扑序的初始化与松弛实现
- paragraph：带负边DAG的逐点轨迹
- paragraph：拓扑递推的最优性与边界状态
- paragraph：拓扑递推的实现代价与适用范围

#### 4.1.2 subsection：Bellman–Ford松弛法

- paragraph：同步松弛的状态与逐轮更新
- paragraph：同步轮次的含义与算例
- paragraph：轮数上界与就地更新
- paragraph：负环种子与后继标记
- paragraph：负环影响范围的双向证据
- paragraph：三种目标状态的读法
- paragraph：轮次前驱与有限路径回溯
- paragraph：同步松弛与路径记录的代价

#### 4.1.3 subsection：基于贪心选择的Dijkstra法

- paragraph：最小暂定点的确定与松弛
- paragraph：降键与重复插入的两种实现
- paragraph：非负四点图的执行轨迹
- paragraph：二叉堆与顶点位置表
- paragraph：非负边长下的确定证书
- paragraph：索引堆实现的时间与空间
- paragraph：有负边而无负环的失败例

#### 4.1.4 subsection：编辑距离的网格递推法（扩展）

- paragraph：编辑前缀状态
- paragraph：三类末操作与空前缀边界
- paragraph：填表顺序与最优编辑回溯
- paragraph：插入C的完整网格算例
- paragraph：表存储与编辑规则边界

#### 4.1.5 subsection：动态时间规整法（扩展）

- paragraph：重复对应与允许步长
- paragraph：DTW递推与全局对齐边界
- paragraph：对齐表的填写与回溯
- paragraph：不同长度序列的零成本例
- paragraph：带宽及平均成本目标的边界

### 4.2 section：基于多源传播与下包络的距离变换方法

- paragraph：到目标集合的距离
- paragraph：4邻接与8邻接的路径成本
- paragraph：障碍及有向查询方向

#### 4.2.1 subsection：多源BFS传播法

- paragraph：多源队列的初始化与更新
- paragraph：多源分层的正确性与规模
- paragraph：两端源点的队列算例
- paragraph：非负加权边的多源实现

#### 4.2.2 subsection：双向扫描法

- paragraph：矩形网格的两遍扫描
- paragraph：两遍覆盖最短路的条件
- paragraph：带轴向及对角权重的扫描
- paragraph：倒角距离与欧氏距离的对照

#### 4.2.3 subsection：一维二次下包络法

- paragraph：二次候选与下包络思想
- paragraph：候选抛物线的交点
- paragraph：候选栈的初始化与维护
- paragraph：递增位置的查询指针
- paragraph：交点与弹栈的两个算例
- paragraph：下包络正确性与线性代价

#### 4.2.4 subsection：逐轴二次距离变换法

- paragraph：二次成本的逐轴分离
- paragraph：逐轴执行与最近源索引
- paragraph：平方距离到欧氏距离
- paragraph：位移响应及可分离边界

### 4.3 section：基于残量增广的最大流方法

- paragraph：多路线共享容量的任务
- paragraph：网络与容量
- paragraph：弧流量与容量约束
- paragraph：内部顶点的流守恒
- paragraph：流值与源汇净量
- paragraph：顶点割与割容量
- paragraph：任意流的割上界

#### 4.3.1 subsection：残量增广法

- paragraph：残量弧的建立与读取
- paragraph：残量增广的具体更新
- paragraph：单位容量网络的增广轨迹
- paragraph：最大流与最小割的同值证书
- paragraph：流值5的完整算例
- paragraph：整数容量下的停止与选路
- paragraph：输入编码与实数容量边界
- paragraph：残量搜索的时间与空间

### 4.4 section：基于安全选边的最小生成树方法

- paragraph：最小生成树的建造成本目标
- paragraph：两种选边法的共同教学图
- paragraph：轻边与安全选边条件
- paragraph：安全选边的交换论证

#### 4.4.1 subsection：Kruskal分量合并法

- paragraph：Kruskal的分量合并思想与状态
- paragraph：Kruskal的逐边实现与停止
- paragraph：五点七边的逐边轨迹
- paragraph：当前分量的轻边证书
- paragraph：排序和并查集的计算代价

#### 4.4.2 subsection：Prim单树扩展法

- paragraph：Prim的跨割接入思想与键值
- paragraph：Prim的堆更新与停止
- paragraph：从a出发的键值更新
- paragraph：轻边安全性与树形输出
- paragraph：堆和数组实现的计算代价
- paragraph：从e出发的选边顺序
- paragraph：Kruskal与Prim的状态比较
- paragraph：平局、负成本与断开图
- paragraph：团候选图上的最大权版本

### 4.5 section：基于交替增广的匹配与指派方法

- paragraph：二部匹配的输入
- paragraph：极大匹配与最大匹配
- paragraph：配对数量与配对成本
- paragraph：完整指派的行列约束
- paragraph：矩形指派的零成本补齐
- paragraph：未匹配惩罚与专属虚拟对象
- paragraph：虚拟扩展与原成本对应

#### 4.5.1 subsection：交替路径增广匹配法

- paragraph：匹配与单位容量整数流的对应
- paragraph：交替路径的搜索与翻转
- paragraph：撤换一条边的增广算例
- paragraph：无增广路径的最大性证书
- paragraph：重复搜索的计算代价

#### 4.5.2 subsection：匈牙利紧边增广法

- paragraph：指派势与紧边最优证书
- paragraph：紧边交替树的初始化与搜索
- paragraph：调势、扩树与增广实现
- paragraph：两行指派的调势轨迹
- paragraph：列剩余成本维护与稠密实现代价

### 4.6 section：基于图割与谱松弛的标记和划分方法

- paragraph：二值标签的一元与成对成本
- paragraph：平衡划分与边差成本
- paragraph：离散可行集与连续候选
- paragraph：目标延拓与松弛下界
- paragraph：可行上界与次优差距
- paragraph：阈值恢复的可行性
- paragraph：组合拉普拉斯的分量零方向
- paragraph：归一化零方向与零度点

#### 4.6.1 subsection：二值次模图割法

- paragraph：次模图割的条件与思想
- paragraph：四项成对表的边差分解
- paragraph：线性项归并与非负平移
- paragraph：源汇终端弧与成对容量
- paragraph：最小割求解及标记恢复
- paragraph：两点标记的图割轨迹
- paragraph：非次模及其他标签的边界
- paragraph：图割构造与求解代价

#### 4.6.2 subsection：RatioCut谱松弛法

- paragraph：比率割的非空平衡目标
- paragraph：两水平编码的平衡约束
- paragraph：RatioCut的谱松弛方向
- paragraph：谱方向与离散组恢复
- paragraph：特征近似与有效下界
- paragraph：不连通支撑及重根边界
- paragraph：稠密求谱与稀疏算子代价
- paragraph：同值组移动及割值更新
- paragraph：阈值扫描的时间与存储

#### 4.6.3 subsection：NCut谱松弛法

- paragraph：NCut的体积平衡编码
- paragraph：度加权松弛与广义谱方向
- paragraph：正权分量与零度输入分类
- paragraph：变回原坐标后的阈值恢复
- paragraph：正则图及零度点的边界
- paragraph：NCut实现代价与RatioCut对照
- paragraph：四点路径的比率割数值
- paragraph：同一分组的归一化割数值
- paragraph：松弛差距与实际最优的区别

### 4.7 section：本章小结

- paragraph：按选择对象核对方法
- paragraph：按状态与证书理解执行
- paragraph：精确图割与谱松弛的边界
- paragraph：计算代价与后续函数查询

---

[详细分稿：第5章拟调整大纲：图上函数的变换与查询](outline-05-functions-queries.md)

## 5 chapter：图上函数的变换与查询

- paragraph：同一张图上的三种计算任务
- paragraph：本章的基础位置与阅读依赖

### 5.1 section：图上函数计算的基本概念

- paragraph：顶点数值与图信号
- paragraph：离散顶点标记
- paragraph：完整配置的取值范围
- paragraph：配置函数的评价与查询
- paragraph：函数计算的输入与输出
- paragraph：结构邻接与正权支撑
- paragraph：算法状态与更新时机

### 5.2 section：基于谱分解的图信号变换方法

- paragraph：图频率与所选算子
- paragraph：组合拉普拉斯的零模
- paragraph：归一化零模与支撑孤点
- paragraph：标准正交谱基与变化尺度

#### 5.2.1 subsection：实正交图傅里叶变换法

- paragraph：建立并保存实谱基
- paragraph：投影系数与逆变换
- paragraph：三点路径的投影与重构
- paragraph：幅值平方与边差能量
- paragraph：重特征空间与坐标对应
- paragraph：实现代价与适用范围

#### 5.2.2 subsection：环图傅里叶变换法

- paragraph：环图算子与解析模式
- paragraph：复共轭与模态编号
- paragraph：输入环顺序与归一化
- paragraph：正逆变换的同输入核验

##### 5.2.2.1 subsubsection：直接DFT求值法

- paragraph：逐频率累加与逆向重构
- paragraph：直接求和的计算代价

##### 5.2.2.2 subsubsection：FFT求值法

- paragraph：调用既有FFT并转换坐标
- paragraph：解析结构与一般图的边界

### 5.3 section：基于谱响应的图信号处理方法

- paragraph：频率响应与系数处理
- paragraph：重特征值上的共同响应

#### 5.3.1 subsection：谱分解滤波法

- paragraph：投影、逐模态缩放与合成
- paragraph：选基、编号与图改变

#### 5.3.2 subsection：稀疏递推的多项式图滤波法

- paragraph：多项式响应与递推状态
- paragraph：K跳依赖与系数相消
- paragraph：重编号下的同步结果
- paragraph：稀疏乘法成本与轨迹存储
- paragraph：三点路径的源向量与输出

#### 5.3.3 subsection：热扩散的谱求值法

- paragraph：组合拉普拉斯热流与目标时刻
- paragraph：逐模态计算指数作用
- paragraph：总和守恒与分量均值
- paragraph：四顶点图的衰减比例
- paragraph：幅值平方与边差能量的耗散
- paragraph：逐边变化与长期信息损失

#### 5.3.4 subsection：显式Euler的局部扩散近似法

- paragraph：目标时刻与步数选择
- paragraph：非负平均所需的步长
- paragraph：同步读取与缓冲替换
- paragraph：固定时刻的离散误差
- paragraph：严格步长与分量均值收敛
- paragraph：端点步长的交换振荡
- paragraph：代价与方法选择

### 5.4 section：基于多重集合编码的1-WL标记细化法

- paragraph：输入标记与空图约定
- paragraph：邻居类型的多重集合
- paragraph：规范签名与统一字典
- paragraph：同轮读取与整体替换
- paragraph：三点路径的迭代轨迹
- paragraph：细分停止的判据与依据
- paragraph：两图比较的共同编码
- paragraph：六环与双三角形的不可辨性
- paragraph：每轮成本与轨迹存储

### 5.5 section：基于局部表汇总的配置查询方法

- paragraph：非空有限变量域
- paragraph：局部因子与完整作用域
- paragraph：总量、最优值与见证
- paragraph：保留变量的查询表
- paragraph：局部组合与跨配置聚合
- paragraph：交换半环与分配规则
- paragraph：常用运算及无穷约定
- paragraph：空操作与无相关因子的变量

#### 5.5.1 subsection：逐变量消元法

- paragraph：当前因子集合与变量索引
- paragraph：接口配置与内部状态枚举
- paragraph：无关变量与输出展开
- paragraph：两变量手算与贯穿图顺序
- paragraph：为何逐步操作保持查询
- paragraph：极值表与选择表
- paragraph：输出赋值与逆序查回
- paragraph：最大积与对数成本
- paragraph：固定选择与随状态选择
- paragraph：变量角色与合法顺序
- paragraph：表枚举成本与顺序选择

#### 5.5.2 subsection：树上两遍消息传递法

- paragraph：发送侧变量与接收侧索引
- paragraph：子树分组与消息递推
- paragraph：根表与一次向上计算
- paragraph：排除目标分支与向下消息
- paragraph：前后缀组合与零消息
- paragraph：最优回溯与概率归一化
- paragraph：叶消息与根总量
- paragraph：回传消息与三个单点表
- paragraph：树消息的状态枚举成本
- paragraph：消息存储与查询复用

#### 5.5.3 subsection：树分解下的袋消息法

- paragraph：因子唯一归属与本袋函数
- paragraph：交集索引与内部状态汇总
- paragraph：袋表聚合与根总量
- paragraph：回传、回溯与接口一致性
- paragraph：两袋四行接口表
- paragraph：运行交集失效时的错误
- paragraph：袋配置的枚举规模
- paragraph：接口表与回溯表的存储
- paragraph：原有环图上的循环消息边界

### 5.6 section：本章小结

- paragraph：坐标变换与数值处理的区别
- paragraph：数值扩散与类别细化的区别
- paragraph：配置查询的运算与接口
- paragraph：输入输出与计算成本的共同口径

---
