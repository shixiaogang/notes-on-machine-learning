# 卷1《数学准备：计算、分析与几何》：第2部分“空间与几何”大纲

正文入口：[tex/01-mathematical-preliminaries-upper/02-linear-algebra-and-geometry/part.tex](../../tex/01-mathematical-preliminaries-upper/02-linear-algebra-and-geometry/part.tex)。章号按本卷连续编号，以下标题和顺序对应当前入口实际接入的正文。

在线性空间、非线性空间与函数空间中，分别建立表示、关系、运算、求解、逼近和稳定性，避免把坐标记录与对象本身混为一谈。

## 第5章 线性空间

正文：[01-linear-algebra-and-matrix-analysis.tex](../../tex/01-mathematical-preliminaries-upper/02-linear-algebra-and-geometry/01-linear-algebra-and-matrix-analysis.tex)。

### 5.1 元素与表示

主要内容：从可线性组合的对象建立线性空间，再选基与坐标；区分换基、数组重排与对对象施加映射。

论证与表述逻辑：

1. 对象与空间的界定：两个位移可以相加，一条信号可以按幅度缩放，两个同形矩阵也可以逐项相加。设标量域$\mathbb F$为$\mathbb R$或$\mathbb C$。
2. 对象的坐标表示：要用有限个数记录对象，可以先选择一组生成方向，再检查这些方向是否足够、是否冗余。
3. 坐标的转换：若$\mathcal C$是另一组基，把各$\boldsymbol b_j$的$\mathcal C$坐标排成列，得到换基矩阵$\boldsymbol S_{\mathcal C\leftarrow\mathcal B}$。

#### 5.1.1 对象与空间的界定

主要内容：两个位移可以相加，一条信号可以按幅度缩放，两个同形矩阵也可以逐项相加。设标量域$\mathbb F$为$\mathbb R$或$\mathbb C$。

论证与表述逻辑：

1. 矩阵有两种角色：在同形矩阵构成的空间中，它本身是一个元素；固定两端坐标后，它又可以记录一个线性作用。若$\boldsymbol A\in\mathbb F^{m\times d}$、$\boldsymbol x\in\mathbb F^d$，则$(\boldsymbol A\boldsymbol x)_i=\sum_{j=1}^d a_{i,j}x_j$属于$\mathbb F^m$。

#### 5.1.2 对象的坐标表示

主要内容：要用有限个数记录对象，可以先选择一组生成方向，再检查这些方向是否足够、是否冗余。

论证与表述逻辑：

1. 固定有序基$\mathcal B=(\boldsymbol b_1,\ldots,\boldsymbol b_d)$后，对象$\boldsymbol v$唯一写成$\sum_j x_j\boldsymbol b_j$。
2. 定义（多维数值数组）：给定正整数$n_1,\ldots,n_k$，形状为$n_1\times\cdots\times n_k$的数值数组，是从$\{1,\ldots,n_1\}\times\cdots\times\{1,\ldots,n_k\}$到$\mathbb F$的映射。第$j$个索引称为第$j$个轴，轴数$k$称为数组的阶。机器学习中常将这样的数组称为张量（tensor）。
3. 本章统一用按列堆叠的向量化（vectorization）：$\operatorname{vec}(\boldsymbol A) =(a_{1,1},\ldots,a_{m,1},a_{1,2},\ldots,a_{m,n})^{\top}, \qquad \boldsymbol A\in\mathbb F^{m\times n}$元素$a_{i,j}$对应索引$i+(j-1)m$。

#### 5.1.3 坐标的转换

主要内容：若$\mathcal C$是另一组基，把各$\boldsymbol b_j$的$\mathcal C$坐标排成列，得到换基矩阵$\boldsymbol S_{\mathcal C\leftarrow\mathcal B}$。

论证与表述逻辑：

1. 维度重排（permutation of axes）改变轴的顺序。例如$y_{i,k,j}=x_{i,j,k}$把$b\times\ell\times d$变为$b\times d\times\ell$。
2. 数值数组也不自动成为几何中的张量对象。区分这些用法，才能避免把存储格式当成几何性质。

### 5.2 关系与结构

主要内容：用子空间、仿射结构、范数与等价关系描述包含、位置、距离及主动忽略的差异。

论证与表述逻辑：

1. 对象集合的包含关系：例如约束$\boldsymbol A\boldsymbol x=\boldsymbol0$保留的全部输入，可以继续相加和缩放；这些可行方向因此构成原空间中的一个线性子空间。
2. 对象的位置与方向关系：一条不经过原点的直线不能自由缩放，却仍有固定的移动方向。给定基点$x_0$与子空间$U$，集合$x_0+U=\{x_0+u:u\in U\}$称为仿射空间：元素表示位置，两点之差属于方向空间$U$。
3. 对象的距离关系：误差$(1,1)$可以按绝对偏差相加计为$2$，也可以按欧氏长度计为$\sqrt2$，还可以只记录最大坐标偏差$1$。
4. 对象的等价关系：半范数下无法区分的方向可以统一归并。若$x,y\in N$，则$p(ax+by)\leq |a|p(x)+|b|p(y)=0$，所以$N$是子空间。

#### 5.2.1 对象集合的包含关系

主要内容：例如约束$\boldsymbol A\boldsymbol x=\boldsymbol0$保留的全部输入，可以继续相加和缩放；这些可行方向因此构成原空间中的一个线性子空间。

论证与表述逻辑：

1. 两个子空间$U,W\subseteq V$的交仍为子空间，它记录共有方向；$U+W=\{u+w:u\in U,w\in W\}$记录两组方向联合能到达的对象。

#### 5.2.2 对象的位置与方向关系

主要内容：一条不经过原点的直线不能自由缩放，却仍有固定的移动方向。给定基点$x_0$与子空间$U$，集合$x_0+U=\{x_0+u:u\in U\}$称为仿射空间：元素表示位置，两点之差属于方向空间$U$。

论证与表述逻辑：

1. 系数满足$\sum_i a_i=1$时，$\sum_i a_i(x_0+u_i)=x_0+\sum_i a_i u_i$仍在该集合中，称为仿射组合。

#### 5.2.3 对象的距离关系

主要内容：误差$(1,1)$可以按绝对偏差相加计为$2$，也可以按欧氏长度计为$\sqrt2$，还可以只记录最大坐标偏差$1$。

论证与表述逻辑：

1. 推导：Young不等式$uv\leq u^p/p+v^q/q$对$u,v\geq0$成立：$u>0$时令$t=v/u^{p-1}$，只需验证$1/p+t^q/q-t\geq0$；其导数为$t^{q-1}-1$，最小值在$t=1$处为零。$u=0$时也成立。若两向量非零，取$u_j=|x_j|/\lVert\boldsymbol x\rVert_p$、$v_j=|y_j|/\lVert\boldsymbol y\rVert_q$并求和，得到$\sum_j u_jv_j\leq1/p+1/q=1$。
2. 定义（由向量范数诱导的矩阵范数）：给定输入范数$\lVert\cdot\rVert_\alpha$和输出范数$\lVert\cdot\rVert_\beta$，诱导矩阵范数（induced matrix norm）为$\lVert\boldsymbol A\rVert_{\alpha\to\beta} =\sup_{\boldsymbol x\neq0}\frac{\lVert\boldsymbol A\boldsymbol x\rVert_\beta} {\lVert\boldsymbol x\rVert_\alpha}$两端采用同一类$p$范数时简写为$\lVert\boldsymbol A\rVert_p$。
3. 例如$\lVert\boldsymbol A\boldsymbol x\rVert_2\leq\lVert\boldsymbol A\rVert_{\mathrm F}\lVert\boldsymbol x\rVert_2$来自对每一行应用Hölder不等式，再求平方和。

#### 5.2.4 对象的等价关系

主要内容：半范数下无法区分的方向可以统一归并。若$x,y\in N$，则$p(ax+by)\leq |a|p(x)+|b|p(y)=0$，所以$N$是子空间。

论证与表述逻辑：

1. 定义（线性空间的商空间）：设$N$为$V$的线性子空间。规定$\boldsymbol x\sim\boldsymbol y$当且仅当$\boldsymbol x-\boldsymbol y\in N$，等价类$\boldsymbol x+N=\{\boldsymbol x+\boldsymbol n:\boldsymbol n\in N\}$组成商空间（quotient space）$V/N$，其运算为$(\boldsymbol x+N)+(\boldsymbol y+N)=(\boldsymbol x+\boldsymbol y)+N,\qquad a(\boldsymbol x+N)=a\boldsymbol x+N$。
2. 若换代表元$\boldsymbol x'=\boldsymbol x+\boldsymbol n_1$、$\boldsymbol y'=\boldsymbol y+\boldsymbol n_2$，结果只相差$\boldsymbol n_1+\boldsymbol n_2$或$a\boldsymbol n_1$，仍属于$N$，所以运算不依赖代表元。
3. 商映射$q:V\to V/N$把对象送到其等价类。半范数在商空间上定义为$\bar p(x+N)=p(x)$；若$x-y\in N$，三角不等式的两个方向给出$p(x)=p(y)$，所以定义与代表无关。

### 5.3 运算与映射

主要内容：建立线性映射的叠加与复合，展开联合运算、分解、投影和标量读取，并说明矩阵幂、指数与平方根的定义条件。

论证与表述逻辑：

1. 空间之间的映射：线性映射（linear map）$T:V\to W$保持线性组合：$T(a\boldsymbol x+b\boldsymbol y)=aT\boldsymbol x+bT\boldsymbol y$，特别有$T\boldsymbol0=\boldsymbol0$。
2. 映射的叠加：两个预测分支接收同一个参数并输出同形预测时，可以先分别计算，再把输出加权相加。若$T,S:V\to W$，这定义$(aT+bS)\boldsymbol x=aT\boldsymbol x+bS\boldsymbol x$；在相同的两端基下其矩阵为$a\boldsymbol A+b\boldsymbol B$。
3. 映射的复合：若$T:U\to V$、$S:V\to W$，复合$S\circ T$在相容基下表示为$[S][T]$。被消去的中间索引对应中间空间。
4. 对象的联合运算：在同一空间内加法与数乘产生新对象。多个数组还可以按元素、成对索引或缩并规则联合计算；先检查轴与形状，再判断固定哪些输入时运算线性。
5. 对象的分解与投影：代数直和只保证分量唯一。若要删去一个方向后让剩余误差最小，还必须规定长度与正交关系。

#### 5.3.1 空间之间的映射

主要内容：线性映射（linear map）$T:V\to W$保持线性组合：$T(a\boldsymbol x+b\boldsymbol y)=aT\boldsymbol x+bT\boldsymbol y$，特别有$T\boldsymbol0=\boldsymbol0$。

论证与表述逻辑：

1. 命题（秩零度定理）：有限维线性映射$T:V\to W$满足$\dim V=\dim\operatorname{null}(T)+\dim\operatorname{range}(T)$。因此对$\boldsymbol A\in\mathbb F^{m\times d}$，$d=\dim\operatorname{null}(\boldsymbol A)+\operatorname{rank}(\boldsymbol A)$。
2. 推导：取零空间的基$\boldsymbol v_1,\ldots,\boldsymbol v_r$并扩充成$V$的基$\boldsymbol v_1,\ldots,\boldsymbol v_d$。前$r$个基向量的像为零，所以其余的像$T\boldsymbol v_{r+1},\ldots,T\boldsymbol v_d$张成值域。若$\sum_{j>r}a_jT\boldsymbol v_j=0$，则$\sum_{j>r}a_j\boldsymbol v_j$属于零空间，能由前$r$个基向量表示。
3. 方阵$\boldsymbol A\in\mathbb F^{d\times d}$若单射，秩零度给出满射，反之亦然。

#### 5.3.2 映射的叠加

主要内容：两个预测分支接收同一个参数并输出同形预测时，可以先分别计算，再把输出加权相加。若$T,S:V\to W$，这定义$(aT+bS)\boldsymbol x=aT\boldsymbol x+bS\boldsymbol x$；在相同的两端基下其矩阵为$a\boldsymbol A+b\boldsymbol B$。

论证与表述逻辑：

1. 例如两个从$\mathbb R^2$到$\mathbb R^3$的映射可以相加，并不要求输入与输出空间相同。固定权重的叠加保持线性：把输入线性组合代入，各分支分别展开，再汇总即可。

#### 5.3.3 映射的复合

主要内容：若$T:U\to V$、$S:V\to W$，复合$S\circ T$在相容基下表示为$[S][T]$。被消去的中间索引对应中间空间。

论证与表述逻辑：

1. 按输入和输出的分组分块，同一规则成为$\boldsymbol C_{i,j}=\sum_\ell\boldsymbol A_{i,\ell}\boldsymbol B_{\ell,j}$，各块的尺寸仍须相容。
2. 若中间空间的范数匹配，连续应用两次界得到次乘性$\lVert\boldsymbol A\boldsymbol B\rVert_{\alpha\to\gamma} \leq\lVert\boldsymbol A\rVert_{\beta\to\gamma} \lVert\boldsymbol B\rVert_{\alpha\to\beta}$。

#### 5.3.4 对象的联合运算

主要内容：在同一空间内加法与数乘产生新对象。多个数组还可以按元素、成对索引或缩并规则联合计算；先检查轴与形状，再判断固定哪些输入时运算线性。

论证与表述逻辑：

1. 查询数也不必等于键数。
2. 两组轴分别作用时，Kronecker积（Kronecker product）记录成对索引：$\boldsymbol A\otimes\boldsymbol B =\begin{bmatrix} a_{1,1}\boldsymbol B&\cdots&a_{1,n}\boldsymbol B\\ \vdots&\ddots&\vdots\\ a_{m,1}\boldsymbol B&\cdots&a_{m,n}\boldsymbol B \end{bmatrix}\in\mathbb F^{mp\times nq}, \quad \boldsymbol A\in\mathbb F^{m\times n},\ \boldsymbol B\in\mathbb F^{p\times q}$按成对索引分别求和可得相容乘积的混合规则$(\boldsymbol A\otimes\boldsymbol B)(\boldsymbol C\otimes\boldsymbol D) =(\boldsymbol A\boldsymbol C)\otimes(\boldsymbol B\boldsymbol D)$对$\boldsymbol A\in\mathbb F^{p\times m}$、$\boldsymbol X\in\mathbb F^{m\times n}$、$\boldsymbol B\in\mathbb F^{n\times q}$，按列向量化给出$\operatorname{vec}(\boldsymbol A\boldsymbol X\boldsymbol B) =(\boldsymbol B^\top\otimes\boldsymbol A)\operatorname{vec}(\boldsymbol X)$证明只需看输出索引$i+(j-1)p$：两侧该元素均为$\sum_{\ell=1}^m\sum_{k=1}^n a_{i,\ell}x_{\ell,k}b_{k,j}$。

#### 5.3.5 对象的分解与投影

主要内容：代数直和只保证分量唯一。若要删去一个方向后让剩余误差最小，还必须规定长度与正交关系。

论证与表述逻辑：

1. 推导：$\boldsymbol y=\boldsymbol0$时直接成立。否则令$a=\langle\boldsymbol y,\boldsymbol x\rangle/\lVert\boldsymbol y\rVert^2$，则$0\leq\lVert\boldsymbol x-a\boldsymbol y\rVert^2 =\lVert\boldsymbol x\rVert^2- \frac{|\langle\boldsymbol x,\boldsymbol y\rangle|^2}{\lVert\boldsymbol y\rVert^2}$移项即得不等式；等号恰好要求$\boldsymbol x=a\boldsymbol y$。
2. 定义（有限向量族的Gram矩阵）：向量$\boldsymbol b_1,\ldots,\boldsymbol b_r$的Gram矩阵（Gram matrix）为$g_{i,j}=\langle\boldsymbol b_i,\boldsymbol b_j\rangle$。若$\boldsymbol B$以它们为列，标准坐标中$\boldsymbol G=\boldsymbol B^*\boldsymbol B$，加权坐标中$\boldsymbol G=\boldsymbol B^*\boldsymbol M\boldsymbol B$。
3. 换基时，保持同一抽象几何需同时变换范数。若新坐标$\boldsymbol z=\boldsymbol S\boldsymbol x$，原长度应写成$\lVert\boldsymbol S^{-1}\boldsymbol z\rVert$。

#### 5.3.6 对象的标量读取

主要内容：从一组样本中读取加权总和，或从一个向量中读取某个坐标，输出都是一个标量。这样的读取先要确定规则及其误差放大率。

论证与表述逻辑：

1. 方阵的迹（trace）为$\operatorname{tr}\boldsymbol A=\sum_i a_{i,i}$，是将两个索引对齐后求和。
2. 定义（有限维伴随）：对内积空间之间的线性映射$T:V\to W$，伴随$T^*:W\to V$满足$\langle Tx,y\rangle_W=\langle x,T^*y\rangle_V$。
3. 复合作用的读取还验证$(\boldsymbol A\boldsymbol B)^*=\boldsymbol B^*\boldsymbol A^*$：配对先经过$\boldsymbol A$再经过$\boldsymbol B$的伴随，次序反向。

#### 5.3.7 方阵的幂、指数和平方根

主要内容：固定一个方阵$\boldsymbol A$以后，可以反复复合它，并叠加不同次数的作用。这定义矩阵多项式$p(\boldsymbol A)=\sum_{j=0}^k a_j\boldsymbol A^j$，其中$\boldsymbol A^0=\boldsymbol I$。

论证与表述逻辑：

1. 命题（自伴矩阵的谱定理）：若$\boldsymbol A\in\mathbb R^{d\times d}$满足$\boldsymbol A^\top=\boldsymbol A$，则全部特征值为实数，并存在正交矩阵$\boldsymbol Q$及实对角矩阵$\boldsymbol\Lambda$使$\boldsymbol A=\boldsymbol Q\boldsymbol\Lambda\boldsymbol Q^\top$复Hermitian矩阵$\boldsymbol A^*=\boldsymbol A$同样有实特征值及酉分解$\boldsymbol A=\boldsymbol Q\boldsymbol\Lambda\boldsymbol Q^*$。
2. 推导：先在复数域取特征对。由$\boldsymbol v^*\boldsymbol A\boldsymbol v=\lambda\boldsymbol v^*\boldsymbol v$，左侧为实数且$\boldsymbol v^*\boldsymbol v>0$，知$\lambda$为实数。实对称时，把$\boldsymbol v$拆成实部和虚部，至少一个给出非零实特征向量。
3. 作为与可对角化例的比较，取$\boldsymbol J=\left[\begin{smallmatrix}0.8&1\\0&0.8\end{smallmatrix}\right]$。

### 5.4 方程与优化

主要内容：比较精确线性约束、最小残差与双侧矩阵方程，说明解的存在、唯一性及矩阵分解求解的条件。

论证与表述逻辑：

1. 精确约束下的线性方程求解：给定目标$\boldsymbol b$以后，首先检查是否有输入能精确产生它。
2. 残差约束下的线性方程求解：不能精确匹配观测时，可以最小化残差，也可以只要求$\lVert\boldsymbol A\boldsymbol x-\boldsymbol b\rVert\leq\tau$。
3. 双侧作用下的矩阵方程求解：未知对象也可以是一张矩阵：左乘对未知矩阵的各行作线性组合，右乘对其各列作线性组合。两端矩阵可逆时，混合乘积规则还给出$(\boldsymbol A\otimes\boldsymbol B)^{-1}=\boldsymbol A^{-1}\otimes\boldsymbol B^{-1}$，从而可以逐侧反演。

#### 5.4.1 精确约束下的线性方程求解

主要内容：给定目标$\boldsymbol b$以后，首先检查是否有输入能精确产生它。目标可达即方程相容，也就是$\boldsymbol b\in\operatorname{range}(\boldsymbol A)$，等价于$\boldsymbol y^*\boldsymbol b=0$对所有$\boldsymbol y\in\operatorname{null}(\boldsymbol A^*)$成立。

论证与表述逻辑：

1. 商空间把这种不可区分性表达为精确对应：$\mathbb F^d/\operatorname{null}(\boldsymbol A) \longrightarrow\operatorname{range}(\boldsymbol A),\qquad \boldsymbol x+\operatorname{null}(\boldsymbol A)\longmapsto\boldsymbol A\boldsymbol x$它良定义、线性、单射且满射，却尚未在每个类中选一个代表。
2. 输入与输出维数不同的矩形矩阵没有方阵意义的双侧逆。
3. 有解时，最小范数等条件可以进一步选定代表；它们不改变等式本身。下面两类方法都求解同一个相容方程，实际误差仍需按残差和选解规则核对。

##### 5.4.1.1 基于消元与分解的直接求解

主要内容：高斯消元用一行的倍数消去另一行的某个系数。例如$\left[\begin{smallmatrix}2&1\\4&3\end{smallmatrix}\right]\boldsymbol x=(1,3)^\top$，第二行减第一行的两倍得到$x_2=1$，再代回得$x_1=0$。

论证与表述逻辑：

1. 正定结构能减少工作。若$\boldsymbol A=\boldsymbol A^\top\succ0$，则存在唯一的对角元为正的下三角矩阵$\boldsymbol L$使$\boldsymbol A=\boldsymbol L\boldsymbol L^\top$这称为Cholesky分解（Cholesky decomposition）。
2. 定义（Schur补）：$\boldsymbol A$在$\boldsymbol M$中的Schur补（Schur complement）为$\boldsymbol S=\boldsymbol D-\boldsymbol C\boldsymbol A^{-1}\boldsymbol B$。
3. 直接解$\left[\begin{smallmatrix}3&1\\1&4\end{smallmatrix}\right]\boldsymbol x=\boldsymbol b$得到$\boldsymbol x=(4/11,-1/11)^\top$。

##### 5.4.1.2 基于Krylov空间的迭代求解

主要内容：大规模稀疏矩阵的分解可能产生过多填充，甚至矩阵本身只以“输入向量，返回乘积”的程序给出。这时迭代法（iterative method）从初值$\boldsymbol x^{(0)}$出发，通过矩阵向量乘法逐渐修正。

论证与表述逻辑：

1. 为更充分利用已经做过的矩阵作用，可在$\mathcal K_k(\boldsymbol A,\boldsymbol r^{(0)}) =\operatorname{span}\{\boldsymbol r^{(0)},\boldsymbol A\boldsymbol r^{(0)},\ldots, \boldsymbol A^{k-1}\boldsymbol r^{(0)}\}$中寻找校正，这称为Krylov搜索空间。
2. 第$k$步除一次矩阵作用外，还要与$k$个基向量正交化，成本$O(kd)$，存储全部基为$O(kd)$。重启GMRES每隔固定步数丢弃旧基并重新开始，降低存储，也放弃了旧搜索空间中的方向。

#### 5.4.2 残差约束下的线性方程求解

主要内容：不能精确匹配观测时，可以最小化残差，也可以只要求$\lVert\boldsymbol A\boldsymbol x-\boldsymbol b\rVert\leq\tau$。

论证与表述逻辑：

1. 命题（最小二乘与最小范数）：给定$\boldsymbol A\in\mathbb F^{m\times d}$和$\boldsymbol b\in\mathbb F^m$，全部最小二乘解为$\boldsymbol A^\dagger\boldsymbol b+\operatorname{null}(\boldsymbol A)$。若方程相容，它就是全部精确解中的最小范数者。
2. 推导：将$\boldsymbol b=\boldsymbol P_R\boldsymbol b+\boldsymbol b_\perp$，$\boldsymbol x=\boldsymbol x_\perp+\boldsymbol x_N$按两端正交分解，则$\lVert\boldsymbol A\boldsymbol x-\boldsymbol b\rVert_2^2 =\lVert\boldsymbol A\boldsymbol x_\perp-\boldsymbol P_R\boldsymbol b\rVert_2^2 +\lVert\boldsymbol b_\perp\rVert_2^2$第二项不能由输入改变；第一项在且仅在$\boldsymbol x_\perp=(\boldsymbol A|_{N^\perp})^{-1}\boldsymbol P_R\boldsymbol b=\boldsymbol A^\dagger\boldsymbol b$时为零。所以全部最优输入为$\boldsymbol A^\dagger\boldsymbol b+\boldsymbol x_N$。两项正交，得到$\lVert\boldsymbol x\rVert_2^2=\lVert\boldsymbol A^\dagger\boldsymbol b\rVert_2^2+\lVert\boldsymbol x_N\rVert_2^2$，最小值仅在$\boldsymbol x_N=0$时达到。
3. 满列秩时，正规方程的唯一解给出$\boldsymbol A^\dagger=(\boldsymbol A^*\boldsymbol A)^{-1}\boldsymbol A^*$；满行秩时，$\boldsymbol A^*(\boldsymbol A\boldsymbol A^*)^{-1}\boldsymbol b$既达到$\boldsymbol b$又属于$N^\perp$，故$\boldsymbol A^\dagger=\boldsymbol A^*(\boldsymbol A\boldsymbol A^*)^{-1}$。

##### 5.4.2.1 基于矩阵分解的直接求解

主要内容：消元改变中间方程的尺度，另一条路线用正交变换保持欧氏长度。

论证与表述逻辑：

1. 消元改变中间方程的尺度，另一条路线用正交变换保持欧氏长度。对$\boldsymbol A\in\mathbb R^{m\times d}$、$m\geq d$且满列秩，经济型QR分解为$\boldsymbol A=\boldsymbol Q\boldsymbol R$，其中$\boldsymbol Q\in\mathbb R^{m\times d}$满足$\boldsymbol Q^\top\boldsymbol Q=\boldsymbol I$，$\boldsymbol R\in\mathbb R^{d\times d}$可逆上三角。
2. Gram--Schmidt将每列减去已有正交方向，再归一化，在精确算术中给出QR。稠密计算常用Householder反射一次消去一列主对角线下的全部元素。
3. 例如$\boldsymbol a=(3,4)^\top$给$\boldsymbol v=(8,4)^\top$，$\boldsymbol H=\left[\begin{smallmatrix}-3/5&-4/5\\-4/5&3/5\end{smallmatrix}\right]$，确实将$\boldsymbol a$送到$(-5,0)^\top$。

##### 5.4.2.2 基于梯度更新的迭代求解

主要内容：矩形最小二乘要先把输出残差搬回输入端。

论证与表述逻辑：

1. 目标$f(\boldsymbol w)=\tfrac12\lVert\boldsymbol X\boldsymbol w-\boldsymbol y\rVert_2^2$的梯度为$\boldsymbol X^\top(\boldsymbol X\boldsymbol w-\boldsymbol y)$，因此$\boldsymbol w^{(t+1)} =\boldsymbol w^{(t)}+\eta\boldsymbol X^\top(\boldsymbol y-\boldsymbol X\boldsymbol w^{(t)})$每步只需一次$\boldsymbol X$和一次$\boldsymbol X^\top$作用，不必形成Gram矩阵；稀疏存储下成本为$O(\operatorname{nnz}(\boldsymbol X))$。
2. 伴随搬回残差而非求逆，正是这里出现$\boldsymbol X^\top$的原因。

#### 5.4.3 双侧作用下的矩阵方程求解

主要内容：未知对象也可以是一张矩阵：左乘对未知矩阵的各行作线性组合，右乘对其各列作线性组合。两端矩阵可逆时，混合乘积规则还给出$(\boldsymbol A\otimes\boldsymbol B)^{-1}=\boldsymbol A^{-1}\otimes\boldsymbol B^{-1}$，从而可以逐侧反演。

论证与表述逻辑：

1. 定义（Sylvester方程）：给定$\boldsymbol A\in\mathbb F^{m\times m}$、$\boldsymbol B\in\mathbb F^{n\times n}$和$\boldsymbol C\in\mathbb F^{m\times n}$，关于$\boldsymbol Z\in\mathbb F^{m\times n}$的方程$\boldsymbol A\boldsymbol Z+\boldsymbol Z\boldsymbol B=\boldsymbol C$称为Sylvester方程（Sylvester equation）。
2. 这让向量系统的求解方法可以直接使用，也说明矩阵未知量依然属于一个线性空间；大规模时应利用左右乘法避免存储$mn\times mn$矩阵。
3. 回用已经建立的三角化，可以求解一般矩阵方程。

### 5.5 收敛与逼近

主要内容：分别研究一般对象序列、矩阵幂和求解迭代的收敛；在秩受限时确定表示规模与最佳矩阵逼近误差的关系。

论证与表述逻辑：

1. 对象序列的收敛：有限坐标逐项收敛，并不自动说明任意误差尺度都给出同一极限。固定基$(b_1,\ldots,b_d)$，令$\lVert x\rVert_c=\max_j|x_j|$为坐标最大范数。
2. 反复作用下的幂序列收敛：对固定矩阵反复作用，初值$\boldsymbol x^{(0)}$在第$k$步变成$\boldsymbol A^k\boldsymbol x^{(0)}$。
3. 求解和优化下的迭代序列收敛：对最小二乘，固定步长使误差更新确实由一个固定自伴矩阵控制。但设计矩阵的零空间不进入残差，梯度也无法修改其中的初值。
4. 秩约束下的矩阵逼近：一个$m\times n$稠密矩阵需要存储$mn$个数，每次作用需要$O(mn)$次运算。若能以$k$个输入输出方向的配对近似它，存储和作用成本便可降到$O((m+n)k)$。

#### 5.5.1 对象序列的收敛

主要内容：有限坐标逐项收敛，并不自动说明任意误差尺度都给出同一极限。固定基$(b_1,\ldots,b_d)$，令$\lVert x\rVert_c=\max_j|x_j|$为坐标最大范数。

论证与表述逻辑：

1. 范数柯西列的各坐标都是标量柯西列，因而逐项有极限；有限个坐标重组为$x\in V$，上界又保证序列在原范数下趋于$x$，所以有限维空间完备。
2. 有限维线性映射的每个输出坐标是有限个输入坐标的线性组合，先有坐标范数下的有限界，再由两端范数等价得到任意范数下的有界性。

#### 5.5.2 反复作用下的幂序列收敛

主要内容：对固定矩阵反复作用，初值$\boldsymbol x^{(0)}$在第$k$步变成$\boldsymbol A^k\boldsymbol x^{(0)}$。

论证与表述逻辑：

1. 命题（固定矩阵幂的衰减判据）：对有限方阵$\boldsymbol A$，$\boldsymbol A^k\to\boldsymbol0$当且仅当$\rho(\boldsymbol A)<1$。
2. 推导：若$\boldsymbol A^k\to0$，对任一复特征向量有$\boldsymbol A^k\boldsymbol v=\lambda^k\boldsymbol v\to0$，故$|\lambda|<1$。反之，Jordan表示中每项都是有限次多项式乘以模小于$1$的指数，因而趋零；零特征值块最终为零。有限块合并、再乘固定换基矩阵，仍趋零。
3. 例如两个幂零矩阵$\boldsymbol B=\left[\begin{smallmatrix}0&2\\0&0\end{smallmatrix}\right]$、$\boldsymbol C=\left[\begin{smallmatrix}0&0\\2&0\end{smallmatrix}\right]$各自谱半径为零，而$\boldsymbol B\boldsymbol C=\operatorname{diag}(4,0)$，交替作用可以增长。

#### 5.5.3 求解和优化下的迭代序列收敛

主要内容：对最小二乘，固定步长使误差更新确实由一个固定自伴矩阵控制。但设计矩阵的零空间不进入残差，梯度也无法修改其中的初值。

论证与表述逻辑：

1. 命题（最小二乘梯度迭代的解选择）：设非零$\boldsymbol X\in\mathbb R^{n\times d}$，$\boldsymbol y\in\mathbb R^n$。对$F(\boldsymbol w)=\lVert\boldsymbol X\boldsymbol w-\boldsymbol y\rVert_2^2/(2n)$使用$\boldsymbol w^{(t+1)} =\boldsymbol w^{(t)}-\frac{\eta}{n}\boldsymbol X^\top(\boldsymbol X\boldsymbol w^{(t)}-\boldsymbol y), \qquad 0<\eta<\frac{2n}{\lVert\boldsymbol X\rVert_2^2}$任意初值均有$\boldsymbol w^{(t)}\longrightarrow \boldsymbol X^\dagger\boldsymbol y+(\boldsymbol I-\boldsymbol X^\dagger\boldsymbol X)\boldsymbol w^{(0)}$零初值选择唯一的最小欧氏范数最小二乘解。若进一步满行秩且$d>n$，则$\widehat{\boldsymbol w}=\boldsymbol X^\top(\boldsymbol X\boldsymbol X^\top)^{-1}\boldsymbol y,\qquad \{\widehat{\boldsymbol w}\}=\argmin_{\boldsymbol X\boldsymbol w=\boldsymbol y}\lVert\boldsymbol w\rVert_2$。
2. 推导：在$\boldsymbol H$的正特征值方向$\boldsymbol q_j$上，$\boldsymbol q_j^\top\boldsymbol e^{(t)} =\left(1-\frac{\eta\lambda_j}{n}\right)^t \boldsymbol q_j^\top\boldsymbol e^{(0)}\longrightarrow0,$因为步长条件使倍率绝对值小于$1$。在$\ker\boldsymbol X$上倍率为$1$，故保留$\boldsymbol P_{\ker\boldsymbol X}\boldsymbol w^{(0)} =(\boldsymbol I-\boldsymbol X^\dagger\boldsymbol X)\boldsymbol w^{(0)}$合并两个正交分量便得到一般极限，整个证明不需要奇异值分解。
3. GMRES在初始残差非零时相应控制$\frac{\lVert\boldsymbol r^{(k)}\rVert_2}{\lVert\boldsymbol r^{(0)}\rVert_2} \leq\min_{p(0)=1,\deg p\leq k}\lVert p(\boldsymbol A)\rVert_2$非正规矩阵的这一范数不由特征值模单独决定；对角化时还出现特征向量基的放大因子，与本章短时放大例中的问题相同。

#### 5.5.4 秩约束下的矩阵逼近

主要内容：一个$m\times n$稠密矩阵需要存储$mn$个数，每次作用需要$O(mn)$次运算。若能以$k$个输入输出方向的配对近似它，存储和作用成本便可降到$O((m+n)k)$。

论证与表述逻辑：

1. 推导：对非零$\boldsymbol A$，写紧致SVD为$\boldsymbol P\boldsymbol\Sigma\boldsymbol Q^\top$。取$\boldsymbol L=\boldsymbol P\boldsymbol\Sigma^{1/2}$、$\boldsymbol R=\boldsymbol Q\boldsymbol\Sigma^{1/2}$，$q>r$时补零列，则乘积为$\boldsymbol A$，两侧平方范数均为$\sum_i\sigma_i$，所以右侧最小值不超过核范数。反过来，令$\boldsymbol C=\boldsymbol P\boldsymbol Q^\top$，则$\lVert\boldsymbol C\rVert_2=1$。
2. 定义（稳定秩）：非零矩阵$\boldsymbol A$的稳定秩（stable rank）为$r_{\mathrm{stable}}(\boldsymbol A) =\frac{\lVert\boldsymbol A\rVert_{\mathrm F}^2}{\lVert\boldsymbol A\rVert_2^2} =\frac{\sum_i\sigma_i^2}{\sigma_1^2}$零矩阵另约定为零。
3. 各层变换还满足$\lVert\boldsymbol A_L\cdots\boldsymbol A_1\rVert_2\leq\prod_{\ell=1}^L\lVert\boldsymbol A_\ell\rVert_2$，但逐层最强方向未必能对齐，上界可能宽松；稳定秩不能按同一方式简单相乘。

### 5.6 扰动与稳定性

主要内容：区分问题对输入的敏感性和计算造成的误差，分析线性方程解、谱分解及矩阵函数随扰动的变化。

论证与表述逻辑：

1. 运算的误差传播：设目标映射为$F$，理想输入为$z$，实际交给算法的是$z+\Delta z$，算法返回$\widehat y$。
2. 线性方程解的稳定性：线性方程解依赖矩阵与右端。下面分别讨论普通逆给出的唯一解，以及伪逆选出的最小范数解。
3. 谱分解的稳定性：压缩误差由奇异值决定，但压缩方向由子空间决定；前者稳定不保证后者稳定。比较方向之前还要排除基选择的任意性。
4. 矩阵函数的稳定性：幂、指数和平方根将一个矩阵变成另一个矩阵。矩阵输入的扰动会插入乘积的不同位置，这些位置一般不能合并。

#### 5.6.1 运算的误差传播

主要内容：设目标映射为$F$，理想输入为$z$，实际交给算法的是$z+\Delta z$，算法返回$\widehat y$。

论证与表述逻辑：

1. 若$F$在所讨论邻域内可微，一阶变化为$F(z+\delta z)-F(z)=DF(z)[\delta z]+o(\lVert\delta z\rVert)$。
2. 定义（范数意义下的后向稳定）：设输入空间给定范数。若算法对声明的非零输入类返回$\widehat y=F(z+\delta z)$，并在充分小的$u$下满足$\lVert\delta z\rVert/\lVert z\rVert\leq C u$，其中$C$不依赖$u$，则称其在此误差口径下后向稳定（backward stability）。必须说明$C$对问题规模及输入类的依赖；零输入另用绝对误差口径。
3. 后向稳定说明算法只引入小的等效输入扰动。若条件数也适中，一阶分析便给小前向误差；条件数很大时，两者可以同时出现：算法很好地解了一个邻近问题，结果却离当前问题的精确答案很远。

#### 5.6.2 线性方程解的稳定性

主要内容：线性方程解依赖矩阵与右端。下面分别讨论普通逆给出的唯一解，以及伪逆选出的最小范数解。

论证与表述逻辑：

1. 定义（可逆矩阵的条件数）：对同一向量范数诱导的矩阵范数，可逆方阵$\boldsymbol A$的条件数（condition number）为$\kappa(\boldsymbol A)=\lVert\boldsymbol A\rVert\lVert\boldsymbol A^{-1}\rVert$。
2. 定义（线性系统的范数型相对后向误差）：对$\boldsymbol A\in\mathbb R^{m\times n}$、$\boldsymbol b\in\mathbb R^m$与候选$\widehat{\boldsymbol x}$，令$\eta_2(\widehat{\boldsymbol x};\boldsymbol A,\boldsymbol b) =\min\left\{\epsilon\geq0: \begin{array}{l} (\boldsymbol A+\Delta\boldsymbol A)\widehat{\boldsymbol x}=\boldsymbol b+\Delta\boldsymbol b,\\ \lVert\Delta\boldsymbol A\rVert_2\leq\epsilon\lVert\boldsymbol A\rVert_2,\quad \lVert\Delta\boldsymbol b\rVert_2\leq\epsilon\lVert\boldsymbol b\rVert_2 \end{array}\right\},$其中最小化也遍历满足条件的$\Delta\boldsymbol A,\Delta\boldsymbol b$，不另要求结构保持。
3. 需要整个逆的许多元素时，可以从稳定分解计算并检验逆；若只需要$\boldsymbol A^{-1}\boldsymbol b$、$\boldsymbol b^\top\boldsymbol A^{-1}\boldsymbol b$或$\boldsymbol A^{-1}\boldsymbol U$，应用求解器通常已足够。

#### 5.6.3 谱分解的稳定性

主要内容：压缩误差由奇异值决定，但压缩方向由子空间决定；前者稳定不保证后者稳定。比较方向之前还要排除基选择的任意性。

论证与表述逻辑：

1. 定义（等维子空间的主角）：设$\boldsymbol Q,\widetilde{\boldsymbol Q}\in\mathbb F^{d\times r}$均有标准正交列，$1\leq r\leq d$。
2. 因为$\boldsymbol Q^*,\widetilde{\boldsymbol Q}$都是收缩映射，上述奇异值位于$[0,1]$。
3. 因此两侧角度的总量至多为$\sqrt{2k}\lVert\boldsymbol E\rVert_2/\operatorname{sep}_{\mathrm W}$；保留残差形式往往比这个粗界更有信息，也能评价近似算出的奇异向量。

#### 5.6.4 矩阵函数的稳定性

主要内容：幂、指数和平方根将一个矩阵变成另一个矩阵。矩阵输入的扰动会插入乘积的不同位置，这些位置一般不能合并。

论证与表述逻辑：

1. 自伴谱使一般函数的一阶变化可按坐标计算。设$\boldsymbol A=\boldsymbol Q\operatorname{diag}(\lambda_i)\boldsymbol Q^*$，$f$在包含该谱的实开区间上连续可微。
2. 幂的快速平方、指数的缩放与平方以及Schur形式上的函数计算都有各自的舍入传播。应把返回值与同一输入的精确函数值比较，并检查方法声明的前向或后向界；一个解析恒等式并不自动证明实现稳定。

### 5.7 本章小结

主要内容：用近共线设计矩阵串联表示、求解和稳定性，强调坐标大小、对象大小与可识别方向需要分别判断。

论证与表述逻辑：

1. 近共线设计矩阵把本章的几种问题串联起来。对象所在的空间决定什么能够线性组合，基决定怎样记坐标，内积和范数决定怎样比较误差；两列几乎同向时，同一个输出可由两个很大的相消系数表示。
2. 反求输入先问输出是否可达。不可达时，投影给最近输出；输入不唯一时，零空间正交补再给最小范数选择，二者共同确定伪逆。
3. 答案存在、表示唯一、近似最优、方向可辨认和计算可靠是不同保证。近共线性使小奇异方向在反求中放大，即使训练拟合稳定，系数与外推仍可能敏感；截断和岭收缩降低敏感性，同时舍弃或削弱信息。

## 第6章 非线性空间与流形

正文：[02-differential-geometry-and-symmetry.tex](../../tex/01-mathematical-preliminaries-upper/02-linear-algebra-and-geometry/02-differential-geometry-and-symmetry.tex)。

### 6.1 元素与表示

主要内容：区分潜在可行对象与带误差的环境坐标，建立流形、局部坐标及重叠区域的坐标转换。

论证与表述逻辑：

1. 对象与空间的界定：圆上两个点的和通常不在圆上，所以可行位置不能直接组成上一章的向量空间。本章改用局部有限自由度描述可行集合。
2. 对象的局部坐标表示：在圆的一小段上，一个角度便能定位一个点；绕完整圆却必然遇到角度断点或重复表示。流形（manifold）把这两件事分开：它要求每个点附近像某个欧氏开集，并不要求整个对象是一张欧氏坐标表。
3. 坐标的转换：同一点可能由两张图记录。要让这两份记录兼容，需要明确坐标之间的转换。

#### 6.1.1 对象与空间的界定

主要内容：圆上两个点的和通常不在圆上，所以可行位置不能直接组成上一章的向量空间。本章改用局部有限自由度描述可行集合。

论证与表述逻辑：

1. 从这个连续模型采样时，潜在点（latent point）$\boldsymbol p_i=\Phi(s_i,u_i)$指误差发生前的真实位置，$\boldsymbol x_i=\boldsymbol p_i+\boldsymbol\epsilon_i$才是观测。

#### 6.1.2 对象的局部坐标表示

主要内容：在圆的一小段上，一个角度便能定位一个点；绕完整圆却必然遇到角度断点或重复表示。流形（manifold）把这两件事分开：它要求每个点附近像某个欧氏开集，并不要求整个对象是一张欧氏坐标表。

论证与表述逻辑：

1. 定义（光滑嵌入流形）：集合$\mathcal M\subseteq\mathbb R^D$称为$d$维光滑嵌入流形，若每个$\boldsymbol p\in\mathcal M$都有包含它的环境开集$O$和欧氏开集之间的微分同胚$\Psi:O\to\Psi(O)\subseteq\mathbb R^D$，满足$\Psi(\mathcal M\cap O) =\Psi(O)\cap(\mathbb R^d\times\{\boldsymbol0_{D-d}\})$。
2. 令$U=\{\boldsymbol z:(\boldsymbol z,\boldsymbol0_{D-d})\in\Psi(O)\}$，则$\varphi(\boldsymbol z)=\Psi^{-1}(\boldsymbol z,\boldsymbol0_{D-d})$从开集$U\subseteq\mathbb R^d$参数化$\mathcal M\cap O$，且Jacobian满列秩。
3. 参数化的逆$\chi=\varphi^{-1}:\mathcal M\cap O\to U$称为坐标图（chart）。

#### 6.1.3 坐标的转换

主要内容：同一点可能由两张图记录。要让这两份记录兼容，需要明确坐标之间的转换。

论证与表述逻辑：

1. 定义（坐标过渡）：两张图的覆盖区域相交时，$\chi_2\circ\chi_1^{-1}$把第一组坐标换成第二组坐标，称为坐标过渡（coordinate transition），定义在交集的第一组坐标像上。
2. 单位圆的参数化$\varphi(\theta)=(\cos\theta,\sin\theta)^\top$限制到$(-\pi,\pi)$时漏掉$(-1,0)^\top$，限制到$(0,2\pi)$时漏掉$(1,0)^\top$。
3. 三张图共同覆盖时，$\chi_3\circ\chi_1^{-1} =(\chi_3\circ\chi_2^{-1})\circ(\chi_2\circ\chi_1^{-1})$，等式只在各步都有定义的重叠区域使用。

### 6.2 关系与结构

主要内容：从邻域与连通性进入切空间和度量，说明可行方向、路径距离与等价关系各保存哪些几何信息。

论证与表述逻辑：

1. 对象的邻域关系：在嵌入模型中，$\mathcal M\cap O$（$O$为环境开集）给出相对开集。包含一个含有该点的相对开集的集合，称为该点的邻域。
2. 对象的位置与方向关系：从$\boldsymbol p=\varphi(\boldsymbol z)$出发，坐标变化$\boldsymbol v$经Jacobian$\boldsymbol J_\varphi(\boldsymbol z)$映为环境空间中的瞬时速度。
3. 对象的距离关系：切空间说明方向可不可行，却没有规定一单位坐标变化有多长。点带外侧与内侧相同的$\mathrm ds$对应不同弧长，因而内积必须按位置指定。
4. 对象的等价关系：坐标可改变，不意味着任务输出必须不变。整体旋转点带时，长度不变，表示朝向的向量却应同步旋转；重排点记录的行，则只改变编号而不移动空间中的点。

#### 6.2.1 对象的邻域关系

主要内容：在嵌入模型中，$\mathcal M\cap O$（$O$为环境开集）给出相对开集。包含一个含有该点的相对开集的集合，称为该点的邻域。

论证与表述逻辑：

1. 推导：$k=1$时由$\partial_0=0$成立。对$k\geq2$，固定$i<j$，两次删除$v_i,v_j$后得到相同的$(k-2)$维面。先删$i$再删原来的$j$，系数为$(-1)^i(-1)^{j-1}$；先删$j$再删$i$，系数为$(-1)^j(-1)^i$，两者相反。
2. 定义（闭链、边界与同调空间）：满足$\partial_kc=0$的链称为闭链（cycle），能写成$c=\partial_{k+1}b$的链称为边界（boundary）。实系数同调空间（homology space）及其维数定义为$H_k(\mathcal K;\mathbb R)=\ker\partial_k/\operatorname{im}\partial_{k+1}, \qquad \beta_k=\dim H_k(\mathcal K;\mathbb R)$$\beta_k$称为第$k$个Betti数（Betti number）。
3. 若$N_k$是$k$维单纯形数，Euler示性数$\chi=\sum_k(-1)^kN_k$是更粗的摘要：空心三角形为$3-3=0$，填充三角形为$3-3+1=1$。

#### 6.2.2 对象的位置与方向关系

主要内容：从$\boldsymbol p=\varphi(\boldsymbol z)$出发，坐标变化$\boldsymbol v$经Jacobian$\boldsymbol J_\varphi(\boldsymbol z)$映为环境空间中的瞬时速度。

论证与表述逻辑：

1. 引理（曲线速度与坐标刻画相容）：$T_{\boldsymbol p}\mathcal M$恰是全部光滑曲线$\gamma:(-\epsilon,\epsilon)\to\mathcal M$、$\gamma(0)=\boldsymbol p$的速度$\gamma'(0)$组成的集合，并且与局部坐标选择无关。
2. 推导：在足够小的参数区间内，曲线落入当前坐标图，写成$\gamma(t)=\varphi(\boldsymbol z(t))$。链式法则给出$\gamma'(0)=\boldsymbol J_\varphi(\boldsymbol z)\boldsymbol z'(0)$，故每个曲线速度都属于所定义的空间。反过来，任意$\boldsymbol v\in\mathbb R^d$给出曲线$t\mapsto\varphi(\boldsymbol z+t\boldsymbol v)$；因为$U$开，足够小的$t$仍在定义域内，其初速度为$\boldsymbol J_\varphi(\boldsymbol z)\boldsymbol v$。
3. 若流形由约束$F(\boldsymbol x)=\boldsymbol0$给出，其中$F:\mathbb R^D\to\mathbb R^{D-d}$在$\boldsymbol p$附近光滑且$\boldsymbol J_F(\boldsymbol p)$行满秩，就能选出$D-d$列组成可逆方阵。

#### 6.2.3 对象的距离关系

主要内容：切空间说明方向可不可行，却没有规定一单位坐标变化有多长。点带外侧与内侧相同的$\mathrm ds$对应不同弧长，因而内积必须按位置指定。

论证与表述逻辑：

1. 嵌入流形可以限制环境欧氏内积，得到诱导度量：$\boldsymbol G(\boldsymbol z)=\boldsymbol J_\varphi(\boldsymbol z)^\top\boldsymbol J_\varphi(\boldsymbol z)$对非零$\boldsymbol a$，满列秩保证$\boldsymbol a^\top\boldsymbol G\boldsymbol a=\lVert\boldsymbol J_\varphi\boldsymbol a\rVert_2^2>0$。
2. 定义（测地距离）：在Riemann流形$(\mathcal M,g)$的同一路径连通分支内，定义测地距离（geodesic distance）为连接两点的全部分段光滑路径长度的下确界：$d_g(\boldsymbol p,\boldsymbol q)= \inf_{\substack{\gamma(a)=\boldsymbol p\\\gamma(b)=\boldsymbol q}}L_g(\gamma)$若无连接路径，约定值为$+\infty$；在可能不连通的整个空间上，它是扩展距离。
3. 定义使用下确界是有意保留存在性问题。在穿孔平面$\mathbb R^2\setminus\{\boldsymbol0\}$中，$(-1,0)^\top$与$(1,0)^\top$之间可沿以被删原点为中心、半径任意小的半圆绕行，路径长度趋于$2$，却没有长度恰为$2$的允许路径。

#### 6.2.4 对象的等价关系

主要内容：坐标可改变，不意味着任务输出必须不变。整体旋转点带时，长度不变，表示朝向的向量却应同步旋转；重排点记录的行，则只改变编号而不移动空间中的点。

论证与表述逻辑：

1. 群描述可以接连施加、也可以撤销的变换规则。集合中若只有若干增强操作，复合后不再属于该集合，或者裁剪已丢失信息而不可逆，就还不能直接称其为群。
2. 定义（群作用）：群作用（group action）是映射$G\times\mathcal X\to\mathcal X$，记$(g,x)\mapsto g\cdot x$，满足$e\cdot x=x,\qquad (g_1g_2)\cdot x=g_1\cdot(g_2\cdot x)$对所有$x\in\mathcal X$和$g_1,g_2\in G$成立。
3. 轨道商在这里只是等价类集合。即使原空间光滑，也不能直接宣布商仍是同维或更低维的光滑流形。

### 6.3 运算与映射

主要内容：讨论位置映射、叠加与复合，建立微分、切向量搬运、位置更新及体积计算，交代各运算的几何条件。

论证与表述逻辑：

1. 空间之间的映射：圆上位置可以映到横坐标，也可以映到另一个曲面上的位置。要判断这样的映射是否光滑，先把两端位置都转成局部欧氏坐标。
2. 映射的叠加：映射叠加要求各分支具有共同定义域，输出落在同一个可加的线性空间。若$F_j:\mathcal M\to V$、$a_j$固定，则$F(p)=\sum_j a_jF_j(p)$定义新的映射；各分支光滑时，坐标表达逐项相加仍光滑。
3. 映射的复合：当$F:\mathcal M\to\mathcal N$、$H:\mathcal N\to\mathcal P$的中间对象匹配时，$(H\circ F)(p)=H(F(p))$。
4. 切向量的映射：例如圆上的点在移动时，其横坐标也随之变化；给定点的瞬时速度，就应能计算读数的瞬时变化。因此，除了点映射本身，还要建立它对切向速度的作用。
5. 切向量的搬运：沿路径计算长度时，每个位置只输出一个标量。若要问速度有没有转弯，或相邻两点的方向是否一致，就必须比较不同切空间中的向量。

#### 6.3.1 空间之间的映射

主要内容：圆上位置可以映到横坐标，也可以映到另一个曲面上的位置。要判断这样的映射是否光滑，先把两端位置都转成局部欧氏坐标。

论证与表述逻辑：

1. 要判断这样的映射是否光滑，先把两端位置都转成局部欧氏坐标。
2. 设$F:\mathcal M\to\mathcal N$，用输入参数化$\varphi$与输出参数化$\psi$记录后，$\psi^{-1}\circ F\circ\varphi$是欧氏开集之间的映射。
3. 例如单位圆上的$(x,y)\mapsto x$读取环境横坐标，仍是合法的光滑映射。

#### 6.3.2 映射的叠加

主要内容：映射叠加要求各分支具有共同定义域，输出落在同一个可加的线性空间。若$F_j:\mathcal M\to V$、$a_j$固定，则$F(p)=\sum_j a_jF_j(p)$定义新的映射；各分支光滑时，坐标表达逐项相加仍光滑。

论证与表述逻辑：

1. 点云分支可以各自接收整幅点云，再把同形特征相加；共享逐点分支也可以先产生各点特征，再求和汇聚。

#### 6.3.3 映射的复合

主要内容：当$F:\mathcal M\to\mathcal N$、$H:\mathcal N\to\mathcal P$的中间对象匹配时，$(H\circ F)(p)=H(F(p))$。

论证与表述逻辑：

1. 定义（等变映射）：若$G$还作用于$\mathcal Y$，把输出作用记为$\rho(g)$，映射$F:\mathcal X\to\mathcal Y$满足$F(g\cdot x)=\rho(g)F(x)\qquad(g\in G,\ x\in\mathcal X),$则称为等变（equivariant）。输出作用不必线性；当$\mathcal Y$是向量空间且$\rho$为线性表示时，右端才是相应线性算子的作用。
2. 例如预测点带朝向时，输入旋转后，输出向量也应旋转。标量类别、位置坐标和分割掩码所需的响应不同，不变性不是比等变性更好的统一目标。
3. 群复合还可以构造相对位置表示。对实数位置$t$和频率$\omega$，令$\boldsymbol R_\omega(t)=\boldsymbol R(\omega t)$。

#### 6.3.4 切向量的映射

主要内容：例如圆上的点在移动时，其横坐标也随之变化；给定点的瞬时速度，就应能计算读数的瞬时变化。因此，除了点映射本身，还要建立它对切向速度的作用。

论证与表述逻辑：

1. 对标量函数$f:\mathcal M\to\mathbb R$，微分读取速度引起的一阶数值变化。有限维向量空间上的全部线性读取组成其对偶空间（dual space）；所以$\mathrm df_{\boldsymbol p}\in T_{\boldsymbol p}^*\mathcal M$，不是一个切向量。

#### 6.3.5 切向量的搬运

主要内容：沿路径计算长度时，每个位置只输出一个标量。若要问速度有没有转弯，或相邻两点的方向是否一致，就必须比较不同切空间中的向量。

论证与表述逻辑：

1. 把圆周上的单位切向速度画在每个位置，得到一个向量场。沿圆周求它的环境导数会出现法向分量，但流形内的方向变化应仍是切向的。
2. 定义（截面曲率）：若$\boldsymbol u,\boldsymbol v\in T_{\boldsymbol p}\mathcal M$线性无关，定义它们张成平面的截面曲率（sectional curvature）为$K_{\boldsymbol p}(\boldsymbol u,\boldsymbol v) =\frac{g(R(\boldsymbol u,\boldsymbol v)\boldsymbol v,\boldsymbol u)} {g(\boldsymbol u,\boldsymbol u)g(\boldsymbol v,\boldsymbol v)-g(\boldsymbol u,\boldsymbol v)^2}$分母是该平行四边形的平方面积，正定性保证它为正。
3. 圆的一维方向沿环境空间转动，产生二阶法向偏离，但其内在Riemann曲率为零；圆柱也有法向弯曲而内在平坦。局部曲率也不替代拓扑：平面与圆柱局部同样平坦，整体的环却不同；局部零曲率本身不保证任意全局闭路上的搬运都平凡。

#### 6.3.6 对象的位置更新

主要内容：给定当前位置和一个切向步，直接沿环境直线前进通常会离开流形。让速度沿自身路径平行移动，在初值解存在的时间内，就能在保持初始速度大小的同时产生流形内的新位置。

论证与表述逻辑：

1. 度量相容进一步给出$\frac{\mathrm d}{\mathrm dt}\lVert\dot\gamma\rVert_g^2 =2g(D\dot\gamma/\mathrm dt,\dot\gamma)=0$，因此速度大小恒定。
2. 定义（回缩）：对每个$\boldsymbol p$，在$T_{\boldsymbol p}\mathcal M$的零向量邻域中给定$\mathcal R_{\boldsymbol p}(\boldsymbol v)\in\mathcal M$，并使其光滑依赖$(\boldsymbol p,\boldsymbol v)$。若$\mathcal R_{\boldsymbol p}(\boldsymbol0)=\boldsymbol p,\qquad \mathrm d(\mathcal R_{\boldsymbol p})_{\boldsymbol0}[\boldsymbol v]=\boldsymbol v,$则称这一族映射为回缩（retraction）。
3. 指数映射是一种局部回缩，其他回缩可有不同的高阶误差。

#### 6.3.7 区域的体积计算

主要内容：要比较区域的大小，路径的一维长度还不够，需要给小区域规定体积。坐标切基围成的微小平行体，其平方体积是Gram行列式$\det\boldsymbol G$，因此几何体积元为$\mathrm dV_g=\sqrt{\det\boldsymbol G(\boldsymbol z)}\,\mathrm d\boldsymbol z$这是由度量产生的测度密度，不要求先为流形选定全局朝向。

论证与表述逻辑：

1. 坐标变换$\boldsymbol z=\psi(\boldsymbol v)$下，$\det\widetilde{\boldsymbol G}=(\det\boldsymbol A)^2\det\boldsymbol G$，所以$\sqrt{\det\widetilde{\boldsymbol G}}\,\mathrm d\boldsymbol v =\sqrt{\det\boldsymbol G(\psi(\boldsymbol v))}\,|\det\boldsymbol A|\,\mathrm d\boldsymbol v$它正是多元积分换元中的Jacobian因子，故对可积函数所得积分不依赖坐标。
2. 点带中$\sqrt{\det\boldsymbol G}=1+u/R>0$，小盒$\mathrm ds\,\mathrm du$在外侧对应较大面积。
3. 当前开带无流形边界，但不是紧集。需要边界积分时，将另取有分片光滑边界的截断闭域，并声明函数在边界的行为；不能只因图上画有虚线就把它当作同一个积分问题。

### 6.4 方程与优化

主要内容：分别求解距离约束下的坐标、给定初值的测地轨迹、固定端点的最短路径，以及流形上的目标最小化问题。

论证与表述逻辑：

1. 距离信息下的坐标重构：设点数$n$为正整数，且只知道这些点之间的距离，能否给它们安排欧氏坐标，并精确保留这些距离？先从反方向计算。
2. 初值条件下的测地轨迹求解：把二阶方程改写为$(z,\dot z)$的一阶系统，局部光滑系数保证解在初值附近存在唯一。只要位置与速度留在一组系数受控的紧区域内，就可继续局部求解；流形缺口或无界离开会阻止这个过程。
3. 端点约束下的最短路径求解：固定时间区间$[a,b]$，定义$E(\gamma)=\frac12\int_a^b\lVert\dot\gamma\rVert_g^2\,\mathrm dt$由Cauchy--Schwarz不等式，$L_g(\gamma)^2\leq2(b-a)E(\gamma)$，等号恰对应几乎处处恒定的速度大小。
4. 流形约束下的点优化：考虑$\min_{\boldsymbol p\in\mathcal M}f(\boldsymbol p)$，其中$f$为至少二阶连续可微的实函数。

#### 6.4.1 距离信息下的坐标重构

主要内容：设点数$n$为正整数，且只知道这些点之间的距离，能否给它们安排欧氏坐标，并精确保留这些距离？先从反方向计算。

论证与表述逻辑：

1. 命题（有限距离的欧氏坐标重构）：设$\boldsymbol\Delta\in\mathbb R^{n\times n}$对称且对角元为零，并令$\boldsymbol B=-\boldsymbol J\boldsymbol\Delta\boldsymbol J/2$。矩阵$\boldsymbol\Delta$是某组欧氏点的平方距离矩阵，当且仅当$\boldsymbol B$半正定。精确保留全部距离所需的最小欧氏维数为$r=\operatorname{rank}(\boldsymbol B)$。
2. 推导：反过来，半正定性和谱定理给出紧谱分解$\boldsymbol B=\boldsymbol Q_r\boldsymbol\Lambda_r\boldsymbol Q_r^\top$，其中$\boldsymbol\Lambda_r$含$r$个正特征值。又因$\boldsymbol B\boldsymbol1=\boldsymbol0$，$\lVert\boldsymbol Y^\top\boldsymbol1\rVert_2^2=\boldsymbol1^\top\boldsymbol B\boldsymbol1=0$，坐标已中心化。$\boldsymbol\Delta'$与$\boldsymbol\Delta$的双重中心化均为$\boldsymbol B$，两者之差对称、对角为零且双重中心化为零。
3. 有限坐标重构也不证明潜在集合是一张光滑曲面。即使点落在圆上，输入欧氏距离记录的仍是弦长，不能把保弦长的坐标自动解释为沿圆排列的一维坐标。

#### 6.4.2 初值条件下的测地轨迹求解

主要内容：把二阶方程改写为$(z,\dot z)$的一阶系统，局部光滑系数保证解在初值附近存在唯一。只要位置与速度留在一组系数受控的紧区域内，就可继续局部求解；流形缺口或无界离开会阻止这个过程。

论证与表述逻辑：

1. 完整单位球面上，取$\boldsymbol p\in\mathbb S^{D-1}$、$\boldsymbol v\perp\boldsymbol p$，则$\gamma(t)=\cos(t\lVert\boldsymbol v\rVert_2)\boldsymbol p +\sin(t\lVert\boldsymbol v\rVert_2)\boldsymbol v/\lVert\boldsymbol v\rVert_2$对全部$t$存在，$\boldsymbol v=\boldsymbol0$时取恒定轨迹。

#### 6.4.3 端点约束下的最短路径求解

主要内容：固定时间区间$[a,b]$，定义$E(\gamma)=\frac12\int_a^b\lVert\dot\gamma\rVert_g^2\,\mathrm dt$由Cauchy--Schwarz不等式，$L_g(\gamma)^2\leq2(b-a)E(\gamma)$，等号恰对应几乎处处恒定的速度大小。

论证与表述逻辑：

1. 在局部坐标中，Lagrange函数为$\mathscr L(\boldsymbol z,\dot{\boldsymbol z})=\frac12\sum_{i,j}g_{i,j}(\boldsymbol z)\dot z^i\dot z^j$。
2. 命题（Hopf--Rinow定理的最短路存在性结论）：设$(\mathcal M,g)$为有限维、连通、无边界的光滑Riemann流形。若它关于$d_g$完备，则任意两点之间存在长度最短测地线。此时任意初速度的测地运动也可以延拓到所有实数时间。
3. 穿孔平面给出省略完备性的反例。用欧氏诱导度量连接$(-1,0)^\top$和$(1,0)^\top$，沿横轴走到$(-\varepsilon,0)^\top$，绕半径$\varepsilon$的半圆，再沿横轴到终点，长度为$(1-\varepsilon)+\pi\varepsilon+(1-\varepsilon) =2+(\pi-2)\varepsilon\longrightarrow2$环境距离给出下界$2$，所以$d_g=2$。

#### 6.4.4 流形约束下的点优化

主要内容：考虑$\min_{\boldsymbol p\in\mathcal M}f(\boldsymbol p)$，其中$f$为至少二阶连续可微的实函数。

论证与表述逻辑：

1. 在选择迭代方法以前，先检查这个最小值是否存在。若非空流形$\mathcal M$紧致且$f$连续，极小值定理保证全局最小值存在；非紧空间上可用紧的非空下水平集等条件替代，不能只凭可微性保证存在。
2. 定义（Riemann Hessian）：在Levi--Civita联络下，定义Riemann Hessian（Riemannian Hessian）为线性算子$\operatorname{Hess}f(\boldsymbol p)[\boldsymbol v] =\nabla_{\boldsymbol v}\operatorname{grad}f \quad\text{从 }T_{\boldsymbol p}\mathcal M\text{ 到自身}$其双线性形式为$\operatorname{Hess}f(\boldsymbol u,\boldsymbol v) =g(\boldsymbol u,\operatorname{Hess}f[\boldsymbol v])$。
3. 欧氏凸性不能不加条件地移到弯曲可行域，因为连接两点的环境线段未必可行。一种替代条件是测地凸性（geodesic convexity）：在一个任意两点都可由域内最短测地线连接的区域$\Omega$上，若$f$沿每条这样的仿射参数测地线都是一元凸函数，就称其在该区域测地凸。

##### 6.4.4.1 基于梯度与回缩的一阶求解

主要内容：用括号上标记录迭代步，梯度更新写成$\boldsymbol p^{(k+1)}=\mathcal R_{\boldsymbol p^{(k)}} (-\alpha^{(k)}\operatorname{grad}f(\boldsymbol p^{(k)}))$回缩的一阶相容性保证，沿该搜索曲线在$\alpha=0$处$\frac{\mathrm d}{\mathrm d\alpha} f(\mathcal R_{\boldsymbol p}(-\alpha\operatorname{grad}f)) \bigg|_{\alpha=0}=-\lVert\operatorname{grad}f\rVert_g^2$因此非驻点处足够小的正步长确实下降。

论证与表述逻辑：

1. 示例（球面上的归一化更新）：单位球面上$\boldsymbol p^\top\boldsymbol v=0$，故$\lVert\boldsymbol p+\boldsymbol v\rVert_2=\sqrt{1+\lVert\boldsymbol v\rVert_2^2}$。
2. 两种更新都可行，但沿大圆走过的角度不同。

##### 6.4.4.2 基于Newton与信赖域的二阶求解

主要内容：梯度只给局部下降方向，Hessian还能描述不同方向的二阶变化。

论证与表述逻辑：

1. 信赖域方法限制模型适用范围，在$\lVert\boldsymbol\eta\rVert_g\leq\Delta$中近似最小化$m_{\boldsymbol p}$。
2. 令拉回目标$\widehat f_{\boldsymbol p}(\boldsymbol\eta)=f(\mathcal R_{\boldsymbol p}(\boldsymbol\eta))$，它定义在固定向量空间$T_{\boldsymbol p}\mathcal M$上。
3. 若算法还复用前一步动量或搜索方向，它们位于旧切空间，不能与当前梯度直接相加。可以沿已选路径作平行移动，也可指定较便宜的向量搬运（vector transport）$\mathcal T_{\boldsymbol\eta}:T_{\boldsymbol p}\mathcal M\to T_{\mathcal R_{\boldsymbol p}(\boldsymbol\eta)}\mathcal M$，要求其对被搬运向量线性、随变量光滑且零步长时为恒等映射。

### 6.5 收敛与逼近

主要内容：区分点列与优化迭代的极限，再讨论局部线性化和有限采样对切空间、距离及拓扑的逼近条件。

论证与表述逻辑：

1. 点序列的收敛：点序列$\boldsymbol p_n$收敛到$\boldsymbol p$，意味着$\boldsymbol p$的每个邻域最终包含全部$\boldsymbol p_n$。
2. 点优化下的迭代序列收敛：回缩梯度法产生的序列还受目标与步长支配。
3. 局部线性表示下的流形逼近：切空间之所以适合近似，由Taylor展开说明。
4. 有限采样下的切空间逼近：只有$\boldsymbol x_i=\boldsymbol p_i+\boldsymbol\epsilon_i$时，参数化与潜在位置通常未知。
5. 有限采样下的距离逼近：只有观测点时，常把距离小于阈值$\varepsilon$的点相连，或连接每个点的$k$个最近邻，再以$\lVert\boldsymbol x_i-\boldsymbol x_j\rVert_2$为边长。

#### 6.5.1 点序列的收敛

主要内容：点序列$\boldsymbol p_n$收敛到$\boldsymbol p$，意味着$\boldsymbol p$的每个邻域最终包含全部$\boldsymbol p_n$。

论证与表述逻辑：

1. Riemann距离给出相同的局部拓扑。取$\boldsymbol p$附近一个闭包仍在图内的小坐标球，光滑正定度量的最小、最大特征值在其上分别有正下界和有限上界。

#### 6.5.2 点优化下的迭代序列收敛

主要内容：回缩梯度法产生的序列还受目标与步长支配。

论证与表述逻辑：

1. 紧性保证有聚点；梯度连续使每个聚点驻定，却不自动保证所有迭代点趋于同一聚点，也不把驻点变成全局最优。Newton局部快速收敛与信赖域全局驻点分析还分别需要非退化性、模型一致性和子问题下降量条件。

#### 6.5.3 局部线性表示下的流形逼近

主要内容：切空间之所以适合近似，由Taylor展开说明。若参数化在当前邻域内二阶导数有界，则$\varphi(\boldsymbol z+\boldsymbol h)-\varphi(\boldsymbol z) =\boldsymbol J_\varphi(\boldsymbol z)\boldsymbol h+O(\lVert\boldsymbol h\rVert_2^2)$一阶项属于切空间，故环境位移投到法向正交补后只剩二阶余项。

论证与表述逻辑：

1. 二阶余项随坐标半径平方缩小；它是确定性局部偏差，不是样本协方差的统计误差。仿射切平面本身可以无限延伸，近似保证却只在当前参数化与余项界有效的小邻域内成立。

#### 6.5.4 有限采样下的切空间逼近

主要内容：只有$\boldsymbol x_i=\boldsymbol p_i+\boldsymbol\epsilon_i$时，参数化与潜在位置通常未知。

论证与表述逻辑：

1. 给观测$\boldsymbol x_i$选择邻居索引集$N_i$和权重$\alpha_{i,j}\geq0$、$\sum_{j\in N_i}\alpha_{i,j}=1$，计算$\overline{\boldsymbol x}_i=\sum_{j\in N_i}\alpha_{i,j}\boldsymbol x_j,\qquad \boldsymbol C_i=\sum_{j\in N_i}\alpha_{i,j} (\boldsymbol x_j-\overline{\boldsymbol x}_i)(\boldsymbol x_j-\overline{\boldsymbol x}_i)^\top$若潜在维数$d$给定，取$\boldsymbol C_i$最大$d$个特征值对应的正交特征向量$\widehat{\boldsymbol U}_i$，其列空间$\widehat T_i$为估计方向子空间。
2. 即使局部方向估计准确，也尚未得到全局坐标。圆的每个邻域只有一个切方向，却不能以单张无断点实坐标图覆盖。

#### 6.5.5 有限采样下的距离逼近

主要内容：只有观测点时，常把距离小于阈值$\varepsilon$的点相连，或连接每个点的$k$个最近邻，再以$\lVert\boldsymbol x_i-\boldsymbol x_j\rVert_2$为边长。

论证与表述逻辑：

1. 潜在对象必须先定。若观测不在潜在流形上，$d_g(\boldsymbol x_i,\boldsymbol x_j)$便未定义；即使观测在二维开带内，也不能因此把它认作$\boldsymbol p_i$。
2. 邻域要小到每条边只跨越近似平直的一段，避免从一折跳到另一折；又要大到样本间的空隙能够连通。超过跨折环境间隔会引入捷径，低估沿潜在空间的距离；小于采样空隙则会把一个真实分支拆开，返回无穷距离。
3. 固定$k$并不固定几何尺度。稀疏处第$k$个邻居可能很远，稠密处则很近，有向近邻关系还可能不对称，需要声明如何对称化。

#### 6.5.6 有限采样下的拓扑逼近

主要内容：固定同一组点和尺度，可以按共同覆盖或成对接近构造复形。

论证与表述逻辑：

1. 定义（Čech复形与Vietoris--Rips复形）：给定欧氏点集$\{\boldsymbol x_i\}$及$\varepsilon>0$，以$B(\boldsymbol x_i,\varepsilon/2)$表示开球。Čech复形（Čech complex）$\mathcal C_\varepsilon$纳入所有满足$\bigcap_{i\in\sigma}B(\boldsymbol x_i,\varepsilon/2)\neq\varnothing$的非空顶点集$\sigma$。Vietoris--Rips复形（Vietoris--Rips complex）$\mathcal R_\varepsilon$纳入所有满足$\lVert\boldsymbol x_i-\boldsymbol x_j\rVert_2\leq\varepsilon$对任意$i,j\in\sigma$成立的非空顶点集。
2. 复形何时能代表球并集的拓扑，还依赖覆盖条件。良好覆盖（good cover）要求每个非空有限交集都可连续收缩到一点；有限欧氏开球的交集为凸集，满足这项要求。
3. 低维图像中的分离簇或孔洞还可能受邻居数、尺度、初始化与优化误差影响。拓扑方法不能修复错误的局部输入：跨折捷径会被忠实组合，完全漏采的区域也无法凭空恢复。

### 6.6 扰动与稳定性

主要内容：比较观测扰动对映射、切空间、重构坐标、拓扑和路径解的影响，先消去基与刚性变换的任意性。

论证与表述逻辑：

1. 运算的误差传播：对光滑点映射$F$，记其局部坐标表达为$\widehat F$。
2. 切空间估计的稳定性：局部PCA从协方差矩阵选出一个子空间。为比较它与真实切空间，先以潜在点处的一阶切向位移构造理想协方差$\boldsymbol C_0$，并假设采样在全部$d$个切方向上都有变化；这样$\boldsymbol C_0$的前$d$维特征子空间才是真实切空间。
3. 坐标重构的稳定性：设平方距离矩阵由$\boldsymbol\Delta$变成$\boldsymbol\Delta+\boldsymbol E$。
4. 拓扑重构的稳定性：固定阈值构造的单个复形可能发生跳变。若成对距离误差不超过$\delta$，所有距离原本小于$\varepsilon-\delta$的边仍会被纳入，原本大于$\varepsilon+\delta$的边仍会被排除；处在中间带内的边不能保证。
5. 路径解的稳定性：初值问题同时更新位置与速度。设另一方程为$\widetilde{\boldsymbol y}'=\widetilde A(\widetilde{\boldsymbol y})$。

#### 6.6.1 运算的误差传播

主要内容：对光滑点映射$F$，记其局部坐标表达为$\widehat F$。在一个凸坐标区域上设$\lVert\boldsymbol J_{\widehat F}\rVert_2\leq L$，沿区域内的线段积分得到$\lVert\widehat F(\boldsymbol z+\boldsymbol h)-\widehat F(\boldsymbol z)\rVert_2 \leq L\lVert\boldsymbol h\rVert_2$。

论证与表述逻辑：

1. 在一个凸坐标区域上设$\lVert\boldsymbol J_{\widehat F}\rVert_2\leq L$，沿区域内的线段积分得到$\lVert\widehat F(\boldsymbol z+\boldsymbol h)-\widehat F(\boldsymbol z)\rVert_2 \leq L\lVert\boldsymbol h\rVert_2$。
2. 跨图时还需计入两端坐标转换及度量的上下界；一个坐标中的小扰动不是坐标无关的数值。
3. 若归一化分母趋零、参数化Jacobian接近降秩，这些界会变差，因此合法运算与数值稳定是两个需要分别核对的条件。

#### 6.6.2 切空间估计的稳定性

主要内容：局部PCA从协方差矩阵选出一个子空间。为比较它与真实切空间，先以潜在点处的一阶切向位移构造理想协方差$\boldsymbol C_0$，并假设采样在全部$d$个切方向上都有变化；这样$\boldsymbol C_0$的前$d$维特征子空间才是真实切空间。

论证与表述逻辑：

1. 当$d<D$时，把$\boldsymbol C_0$的特征值降序排列，设$\delta=\lambda_d-\lambda_{d+1}>0$，并要求$\lVert\boldsymbol E\rVert_2<\delta/2$。
2. 缩小邻域会降低法向二阶偏差，却减少样本并压低真实信号的谱尺度；固定噪声不会随之自动消失。邻域过大时，中心线不同位置的切线已明显转动，PCA得到的是折中方向。
3. 估计子空间内部的基可以旋转，输出应比较投影或主角，而不是逐列比较特征向量。谱隙、邻域尺度和噪声一起决定能否区分切向与法向；增加样本数量不能消除固定尺度带来的几何偏差。

#### 6.6.3 坐标重构的稳定性

主要内容：设平方距离矩阵由$\boldsymbol\Delta$变成$\boldsymbol\Delta+\boldsymbol E$。

论证与表述逻辑：

1. 比较坐标前应先消去平移，再允许整体正交对齐，因为距离本来就不识别这些变换。若点标签也改变，还须先建立点对应。

#### 6.6.4 拓扑重构的稳定性

主要内容：固定阈值构造的单个复形可能发生跳变。若成对距离误差不超过$\delta$，所有距离原本小于$\varepsilon-\delta$的边仍会被纳入，原本大于$\varepsilon+\delta$的边仍会被排除；处在中间带内的边不能保证。

论证与表述逻辑：

1. 若成对距离误差不超过$\delta$，所有距离原本小于$\varepsilon-\delta$的边仍会被纳入，原本大于$\varepsilon+\delta$的边仍会被排除；处在中间带内的边不能保证。
2. 对Rips复形，这直接给出$\mathcal R_{\varepsilon-\delta}\subseteq\widetilde{\mathcal R}_{\varepsilon} \subseteq\mathcal R_{\varepsilon+\delta}$（左侧只在正尺度使用）。
3. 完全漏采的区域、错误点对应或大幅跨折连边并不属于小扰动假设，不能从局部稳定性恢复其中的信息。

#### 6.6.5 路径解的稳定性

主要内容：初值问题同时更新位置与速度。设另一方程为$\widetilde{\boldsymbol y}'=\widetilde A(\widetilde{\boldsymbol y})$。

论证与表述逻辑：

1. 固定端点的最短路有不同边界：距离作为最小代价可能连续，达到它的路线却未必唯一。球面上到对跖点的最短路有多条；终点向不同方向稍微偏离，会选出不同的大圆弧。

### 6.7 本章小结

主要内容：综合局部记录、几何结构与求解，区分迭代收敛、有限采样恢复和扰动稳定性能够支持的不同结论。

论证与表述逻辑：

1. 本章把非线性对象的局部记录、关系、运算、求解、逼近与稳定性分开建立。坐标图记录位置，切空间规定瞬时方向，度量读出长度，路径长度的下确界定义距离；等价关系则明确哪些输入变化被主动忽略。
2. 映射微分传递速度，联络与平行移动比较不同位置的方向，指数映射和回缩产生可行的新点。给定初值求轨迹与给定端点求最短路有不同的唯一性、存在性和稳定性边界。
3. 局部切平面、样本PCA、最短边路径和复形各自逼近方向、距离或拓扑。尺度、覆盖、谱隙与噪声决定适用范围；环境弯曲、内在曲率和整体孔洞不能互相替代。

## 第7章 函数空间

正文：[03-functional-analysis-and-approximation.tex](../../tex/01-mathematical-preliminaries-upper/02-linear-algebra-and-geometry/03-functional-analysis-and-approximation.tex)。

### 7.1 元素与表示

主要内容：界定函数所在的候选空间，比较系数、展开与有限读数的表示方式，说明有限信息何时足以确定函数。

论证与表述逻辑：

1. 函数与空间的界定：设$\mathcal{X}$为输入集合，$\mathbb{R}^{\mathcal{X}}$表示从$\mathcal{X}$到$\mathbb{R}$的全部函数。
2. 函数的表示：若方向相关，同一函数可以有多个系数记录。一般参数族$f_\theta$也不一定是线性子空间；例如固定节点数的非线性神经网络族未必对加法封闭。
3. 函数表示的转换：以$f(t)=a+bt$为例，在基$(1,t-c)$中系数变为$(a+bc,b)$。

#### 7.1.1 函数与空间的界定

主要内容：设$\mathcal{X}$为输入集合，$\mathbb{R}^{\mathcal{X}}$表示从$\mathcal{X}$到$\mathbb{R}$的全部函数。

论证与表述逻辑：

1. 向量值函数$f:\mathcal X\to\mathbb R^r$也可逐点线性组合。输入空间的维数并不决定函数空间的维数：区间只有一个输入坐标，其上所有多项式却包含任意多个线性无关方向。

#### 7.1.2 函数的表示

主要内容：若方向相关，同一函数可以有多个系数记录。一般参数族$f_\theta$也不一定是线性子空间；例如固定节点数的非线性神经网络族未必对加法封闭。

论证与表述逻辑：

1. 允许无限展开时，$\sum_j a_j\phi_j$先是一种待检验的记录形式：它是否收敛、按什么距离收敛、结果是否仍是候选函数，都需要证明。

#### 7.1.3 函数表示的转换

主要内容：以$f(t)=a+bt$为例，在基$(1,t-c)$中系数变为$(a+bc,b)$。若记录已知函数的两个读数，选$t=0,1$便有$\begin{bmatrix}f(0)\\f(1)\end{bmatrix} =\begin{bmatrix}1&0\\1&1\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix}$这次转换可逆；只记录$f(0)$则丢失斜率方向。

论证与表述逻辑：

1. 若记录已知函数的两个读数，选$t=0,1$便有$\begin{bmatrix}f(0)\\f(1)\end{bmatrix} =\begin{bmatrix}1&0\\1&1\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix}$这次转换可逆；只记录$f(0)$则丢失斜率方向。
2. 一般已知系数到读数的矩阵元素为$L_i(\phi_j)$，点值时是$\phi_j(x_i)$，积分时是$\int\phi_jw_i\,\mathrm d\mu$。
3. 按这些规则计算记录不等于有限信息已经识别任意未知函数；后者须限定候选范围并在拟合任务中判断。

### 7.2 关系与结构

主要内容：比较多项式、连续函数及平方可积函数的包含与距离关系，并用等价类处理零测集上不影响整体误差的差异。

论证与表述逻辑：

1. 函数集合的包含关系：固定定义域后，$\operatorname{span}\{\phi_1,\ldots,\phi_m\}$包含于全函数空间，若各$\phi_j$连续，还包含于连续函数集合。
2. 函数的距离关系：如果要保证每个输入上的误差都小，就应控制全域最大偏差。紧区间$[a,b]$上的连续函数空间$C([a,b])$为此常使用一致范数$\lVert f\rVert_{\infty} =\sup_{x\in[a,b]}|f(x)|$这个范数控制每个输入上的最大误差。
3. 函数的等价关系：积分半范数的零方向是几乎处处为零的可测函数。若另用退化权重，零方向由该加权测度决定，而不是由原测度自动决定。

#### 7.2.1 函数集合的包含关系

主要内容：固定定义域后，$\operatorname{span}\{\phi_1,\ldots,\phi_m\}$包含于全函数空间，若各$\phi_j$连续，还包含于连续函数集合。

论证与表述逻辑：

1. 测度还决定积分成员条件。设$0<\mu(\mathcal X)<\infty$，$1\leq p<q<\infty$，Hölder不等式给出$\lVert f\rVert_{L^p}\leq \mu(\mathcal X)^{1/p-1/q}\lVert f\rVert_{L^q}$所以$L^q(\mu)\subseteq L^p(\mu)$；$q=\infty$时由本质上界直接得到同样结论。
2. 紧定义域上的连续函数有界，有限Borel测度保证其属于各有限$p$的积分范围。进入$L^p$时采用自然映射$f\mapsto[f]_\mu$，输出是几乎处处等价类。

#### 7.2.2 函数的距离关系

主要内容：如果要保证每个输入上的误差都小，就应控制全域最大偏差。紧区间$[a,b]$上的连续函数空间$C([a,b])$为此常使用一致范数$\lVert f\rVert_{\infty} =\sup_{x\in[a,b]}|f(x)|$这个范数控制每个输入上的最大误差。

论证与表述逻辑：

1. 加权误差相当于改变测度，权重退化时还会忽略原本可见的区域。系数距离也取决于基：在$[-1,1]$及$\mathrm d\mu=\mathrm dt/2$下，仿射函数差$\delta a+\delta bt$满足$\lVert\delta a+\delta bt\rVert_{L^2(\mu)}^2 =(\delta a)^2+(\delta b)^2/3,$而系数Euclidean距离平方为$(\delta a)^2+(\delta b)^2$。

#### 7.2.3 函数的等价关系

主要内容：积分半范数的零方向是几乎处处为零的可测函数。若另用退化权重，零方向由该加权测度决定，而不是由原测度自动决定。

论证与表述逻辑：

1. 点值读取未必在这个商空间上良定义：改动单点可以不改变等价类却改变读数。具有连续代表且测度全支撑时，连续代表唯一，才可据它读取点值；另一些空间会直接把函数值作为对象的一部分。

### 7.3 运算与映射

主要内容：建立函数投影、标量读取、积分变换与微分运算，再讨论目标泛函的微分，逐项检查定义域和有界性。

论证与表述逻辑：

1. 函数的分解与投影：有限维正交化只处理有限基。无限维中，寻找最近分量往往先产生近似序列，若空间缺少其极限，或候选不保留环境中的极限，就可能没有可用的投影。
2. 函数的标量读取：为计算变换后函数的读数，先说明整函数之间的线性作用。映射$A:\mathcal V\to\mathcal W$称为算子；本节主要研究线性算子，即$A(af+bg)=aAf+bAg$。
3. 函数的积分变换：有限Gram矩阵只访问有限个位置。要考察核如何作用于整个函数，需要先指定积分测度，再把核值累计成新的函数；这个积分算子的谱才描述全域作用。
4. 函数与场的微分运算：经典导数要求逐点极限存在，会排除带尖点但整体仍然规则的函数。为了只保留积分运算真正需要的变化信息，可以反过来要求分部积分恒等式成立：让导数先作用在光滑测试函数上，再检验能否由另一个普通函数表示结果。
5. 目标泛函的微分运算：向量优化中的小位移在这里变为小函数扰动$h$，例如用$f+h$代替$f$。设$J$在$f$的Hilbert空间开邻域内取有限实值。

#### 7.3.1 函数的分解与投影

主要内容：有限维正交化只处理有限基。无限维中，寻找最近分量往往先产生近似序列，若空间缺少其极限，或候选不保留环境中的极限，就可能没有可用的投影。

论证与表述逻辑：

1. 推导：令$d=\inf_{u\in M}\lVert f-u\rVert$，取$u_n\in M$使$\lVert f-u_n\rVert\to d$。因为$(u_n+u_k)/2\in M$，平行四边形恒等式给出$\begin{aligned} \lVert u_n-u_k\rVert^2 &=2\lVert f-u_n\rVert^2+2\lVert f-u_k\rVert^2\\ &\quad-4\left\lVert f-\tfrac12(u_n+u_k)\right\rVert^2\\ &\leq2\lVert f-u_n\rVert^2+2\lVert f-u_k\rVert^2-4d^2\to0 \end{aligned}$完备性给出极限$p$，闭性使$p\in M$，范数连续性使$\lVert f-p\rVert=d$。对任意$h\in M$，$p+th$仍可行，展开其距离平方，在$t=0$取得极小便有$\langle f-p,h\rangle=0$。
2. 定义（正交归一序列与完备正交系）：设$\mathcal H$为Hilbert空间。序列$(e_j)_{j\geq1}$若满足$\langle e_j,e_k\rangle_{\mathcal H}=\mathbb I\{j=k\}$，称为正交归一序列。若它的有限线性张成在$\mathcal H$中稠密，则称为完备正交系（complete orthonormal system）。
3. 正交系的完备性与Hilbert空间的完备性不是同一性质。例如$\ell^2$是完备的Hilbert空间，但只取$(\boldsymbol{e}_{2j})_{j\geq1}$会遗漏所有奇数坐标方向，因此这组正交归一向量不是完备正交系。

#### 7.3.2 函数的标量读取

主要内容：为计算变换后函数的读数，先说明整函数之间的线性作用。映射$A:\mathcal V\to\mathcal W$称为算子；本节主要研究线性算子，即$A(af+bg)=aAf+bAg$。

论证与表述逻辑：

1. 推导：先令$\mathcal{V}_0$为核截面符号$K_x$的形式有限线性组合所成的向量空间：$\mathcal{V}_0 = \left\{ \sum_{i=1}^{n}a_iK_{x_i}: n\in\mathbb{N},\ a_i\in\mathbb{R},\ x_i\in\mathcal{X} \right\}$这里的$K_x$暂时只是由$x$索引的形式符号，尚未把不同形式和按逐点函数值识别。对$f=\sum_i a_iK_{x_i}$和$g=\sum_jb_jK_{z_j}$定义$\langle f,g\rangle_0 = \sum_{i,j}a_i b_jK(x_i,z_j)$正定性只保证$\langle f,f\rangle_0\geq0$，还可能有非零形式和的长度为零。令$\mathcal{N} = \{f\in\mathcal{V}_0:\langle f,f\rangle_0=0\}$半内积仍满足Cauchy--Schwarz不等式：对$\langle g,g\rangle_0>0$，最小化非负二次式$\langle f-tg,f-tg\rangle_0$即可得到原来的证明；若$\langle g,g\rangle_0=0$，非负式$\langle f+tg,f+tg\rangle_0=\langle f,f\rangle_0+2t\langle f,g\rangle_0$对所有实数$t$成立，迫使交叉项为零。
2. 定义（自伴、正与紧算子）：设$T:\mathcal H\to\mathcal H$为实Hilbert空间上的有界线性算子。若对所有$f,g\in\mathcal H$有$\langle Tf,g\rangle=\langle f,Tg\rangle$，称$T$自伴，即$T^*=T$。若$T$自伴且$\langle Tf,f\rangle\geq0$对每个$f\in\mathcal H$成立，称$T$为正算子。若对每个有界序列$(f_n)$，序列$(Tf_n)$都具有在$\mathcal H$中范数收敛的子列，称$T$为紧算子。
3. 紧性也可用于$S:\mathcal H\to\mathcal G$，此时要求有界输入序列的像在$\mathcal G$中有范数收敛子列，不要求两个空间相同。

#### 7.3.3 函数的积分变换

主要内容：有限Gram矩阵只访问有限个位置。要考察核如何作用于整个函数，需要先指定积分测度，再把核值累计成新的函数；这个积分算子的谱才描述全域作用。

论证与表述逻辑：

1. 命题（有限群平均的不变性）：对有限群$G$及任意实函数$h:\mathcal X\to\mathbb R$，定义$\overline h(x)=\frac1{|G|}\sum_{g\in G}h(g\cdot x)$则$\overline h$对给定作用不变。
2. 推导：固定$a\in G$，由作用的复合条件，$\overline h(a\cdot x)=\frac1{|G|}\sum_{g\in G}h((ga)\cdot x)$映射$g\mapsto ga$是$G$上的双射，其逆为$g\mapsto ga^{-1}$。更换求和索引后右端等于$\overline h(x)$，结论对任意$a,x$成立。
3. 平均的代价是信息丢失。例如对$\{\boldsymbol I,-\boldsymbol I\}$作用取$h(\boldsymbol x)=x_1$，平均恒为零；它不仅忽略符号，也失去幅度信息。

#### 7.3.4 函数与场的微分运算

主要内容：经典导数要求逐点极限存在，会排除带尖点但整体仍然规则的函数。为了只保留积分运算真正需要的变化信息，可以反过来要求分部积分恒等式成立：让导数先作用在光滑测试函数上，再检验能否由另一个普通函数表示结果。

论证与表述逻辑：

1. 证明完备性时，取其中的柯西列$(f_n)$。对每个$|\alpha|\leq m$，序列$(D^\alpha f_n)$在$L^2(U)$中都是柯西列，故收敛到某个$g_\alpha\in L^2(U)$，其中$g_0$记为$f$。
2. 定义（Laplace--Beltrami算子）：设$f$为二阶连续可微的实函数。将梯度再取散度，得到Laplace--Beltrami算子（Laplace--Beltrami operator）：$\Delta_g f=\operatorname{div}_g(\operatorname{grad}f) =\frac1{\sqrt{\det\boldsymbol G}}\sum_{i,j} \frac{\partial}{\partial z^i} \left(\sqrt{\det\boldsymbol G}\,g^{i,j} \frac{\partial f}{\partial z^j}\right)$其中$g^{i,j}$是逆度量矩阵$\boldsymbol G^{-1}$的第$(i,j)$项。本章取$\Delta_g$为热方程生成元；适当边界条件下，$-\Delta_g$是非负算子。
3. Green恒等式也联系微分作用与谱，但必须先规定$-\Delta_g$在哪些函数上作用。取能量空间$V$，无边界或齐次Neumann条件下令$V=H^1(\mathcal M)$，齐次Dirichlet条件下令$V=H_0^1(\mathcal M)$。

#### 7.3.5 目标泛函的微分运算

主要内容：向量优化中的小位移在这里变为小函数扰动$h$，例如用$f+h$代替$f$。设$J$在$f$的Hilbert空间开邻域内取有限实值。

论证与表述逻辑：

1. 定义（函数泛函的Fréchet微分与梯度）：设$\mathcal H$为实Hilbert空间，$J$在$f$的开邻域内取有限实值。若存在有界线性泛函$DJ(f):\mathcal H\to\mathbb R$，使$J(f+h)=J(f)+DJ(f)[h]+r_f(h),\qquad \frac{|r_f(h)|}{\lVert h\rVert_{\mathcal H}}\longrightarrow0 \quad(\lVert h\rVert_{\mathcal H}\to0),$则称$J$在$f$处Fréchet可微，$DJ(f)$为其微分，也称Fréchet导数（Fréchet derivative）。由Riesz表示，存在唯一$\nabla_{\mathcal H}J(f)\in\mathcal H$满足$DJ(f)[h]=\langle\nabla_{\mathcal H}J(f),h\rangle_{\mathcal H}$这个空间元素称为相对于该内积的梯度。
2. 微分把一个扰动函数变成一阶目标变化，是有界线性读取；梯度则用空间里的一个方向表示这项读取。Fréchet可微蕴含各方向导数存在且等于$DJ(f)[h]$，反过来未必成立。
3. 梯度还依赖内积的选择，而不只是目标的表达式。例如在仿射函数$f(x)=a+bx$上，目标$J(f)=(a^2+b^2)/2$的微分始终是$DJ(f)[u+vx]=au+bv$。

### 7.4 方程与优化

主要内容：把函数作为未知量，比较闭凸投影、有限观测拟合、整体误差拟合和平滑能量优化，区分目标惩罚与可行约束。

论证与表述逻辑：

1. 闭凸约束下的最近函数求解：有限维最小二乘把观测向量投影到设计矩阵的列空间。函数逼近的对应问题是：给定Hilbert空间$\mathcal H$中的目标$f$与候选集合$C$，能否在$C$中取得最小距离？
2. 有限观测下的函数拟合：有限观测只限制少数读数，候选函数在观测之外仍可能变化。例如不限制次数与系数的多项式既能拟合平滑趋势，也能在观测之间快速振荡。
3. 整体误差下的函数拟合：有限读取只比较若干观测值，整体积分误差则按指定测度评价整条函数。在Mercer条件下，核的谱坐标可以同时展开平方积分误差与核范数，从而逐方向求出拟合和惩罚的取舍。
4. 平滑能量下的函数与场优化：现在不再移动一个点，而是在固定流形上调整整个函数$f$或向量场$\boldsymbol V$。例如给点带上的每处位置分配一个标量，既符合观测又避免局部剧烈变化。

#### 7.4.1 闭凸约束下的最近函数求解

主要内容：有限维最小二乘把观测向量投影到设计矩阵的列空间。函数逼近的对应问题是：给定Hilbert空间$\mathcal H$中的目标$f$与候选集合$C$，能否在$C$中取得最小距离？

论证与表述逻辑：

1. 命题（Hilbert空间投影定理）：设$\mathcal{H}$为实Hilbert空间，$C\subseteq\mathcal{H}$非空、闭且凸。对每个$f\in\mathcal{H}$，存在唯一的$g^\star\in C$满足$\lVert f-g^\star\rVert_{\mathcal{H}} =\inf_{g\in C}\lVert f-g\rVert_{\mathcal{H}}$这个最近点由变分不等式$\langle f-g^\star,g-g^\star\rangle_{\mathcal{H}} \leq0,\qquad g\in C$唯一刻画。若$C=M$是闭线性子空间，则该条件等价于$f-g^\star\perp M$。
2. 推导：记$d=\inf_{g\in C}\lVert f-g\rVert_{\mathcal{H}}$，并取最小化序列$(g_n)\subseteq C$，使$\lVert f-g_n\rVert_{\mathcal{H}}\to d$。凸性保证$(g_n+g_m)/2\in C$。把平行四边形恒等式用于$f-g_n$与$f-g_m$，得到$\lVert g_n-g_m\rVert_{\mathcal{H}}^2 &= 2\lVert f-g_n\rVert_{\mathcal{H}}^2 +2\lVert f-g_m\rVert_{\mathcal{H}}^2\\ &\quad -4\left\lVert f-\frac{g_n+g_m}{2} \right\rVert_{\mathcal{H}}^2\\ &\leq 2\lVert f-g_n\rVert_{\mathcal{H}}^2 +2\lVert f-g_m\rVert_{\mathcal{H}}^2-4d^2$右侧随$m,n\to\infty$趋于$0$，所以$(g_n)$是柯西序列。
3. 区间或权重改变后，正交系数必须随之重算。把$[a,b]$仿射映射到$[-1,1]$可以迁移Legendre或Chebyshev基，但Jacobian因子和权重也会改变。

#### 7.4.2 有限观测下的函数拟合

主要内容：有限观测只限制少数读数，候选函数在观测之外仍可能变化。例如不限制次数与系数的多项式既能拟合平滑趋势，也能在观测之间快速振荡。

论证与表述逻辑：

1. 命题（有限样本表示定理）：设$\mathcal{H}_K$是$\mathcal{X}$上的RKHS，训练输入为$x_1,\ldots,x_n$，其中$n$为正整数。令$\Phi:\mathbb{R}^n\to(-\infty,\infty]$为任意函数，$\Omega:[0,\infty)\to(-\infty,\infty]$单调不减。
2. 推导：这是有限维子空间，因而闭。由投影定理，任意$f\in\mathcal{H}_K$都可唯一分解为$f=f_M+f_{\perp},\qquad f_M\in M,\quad f_{\perp}\perp M$对每个训练输入$x_i$，再生性质给出$f(x_i) = \langle f_M,K_{x_i}\rangle + \langle f_{\perp},K_{x_i}\rangle = f_M(x_i)$因此经验项$\Phi$无法区分$f$与$f_M$。另一方面，正交分解给出$\lVert f\rVert_{\mathcal{H}_K}^2 = \lVert f_M\rVert_{\mathcal{H}_K}^2 + \lVert f_{\perp}\rVert_{\mathcal{H}_K}^2,$故$\lVert f_M\rVert\leq\lVert f\rVert$。
3. 若拟合项为$\Phi(L_1f,\ldots,L_nf)$，其中$L_i$是$\mathcal H$上的有界线性泛函，令$h_i$为各自的Riesz表示元，再取$M=\operatorname{span}\{h_i\}$。

##### 7.4.2.1 基于有限表示的参数求解

主要内容：写$f=\sum_{j=1}^n a_jh_j$，令$\boldsymbol a=(a_1,\ldots,a_n)^\top$，定义Gram矩阵$\boldsymbol G\in\mathbb R^{n\times n}$，$\boldsymbol G_{i,j}=\langle h_j,h_i\rangle_{\mathcal H}$，则$(L_1f,\ldots,L_nf)^\top=\boldsymbol G\boldsymbol a,\qquad \lVert f\rVert_{\mathcal H}^2=\boldsymbol a^\top\boldsymbol G\boldsymbol a$有限表示定理将原问题的下确界化为$\inf_{\boldsymbol a\in\mathbb R^n} \left\{\Phi(\boldsymbol G\boldsymbol a) +\Omega\!\left(\sqrt{\boldsymbol a^\top\boldsymbol G\boldsymbol a}\right)\right\}$点值读取时$h_i=K_{x_i}$、$\boldsymbol G_{i,j}=K(x_i,x_j)$，即通常的核矩阵。

论证与表述逻辑：

1. 平方损失给出可直接核对的实例：$J(f)=\frac1n\sum_{i=1}^n(L_if-y_i)^2+\lambda\lVert f\rVert_{\mathcal H}^2, \qquad\lambda>0$其中$y_i$是第$i$个读取的目标值，$\boldsymbol y=(y_1,\ldots,y_n)^\top$。
2. 附加约束$C$时还要检查$P_M(C)\subseteq C$。核范数球满足这一点，只依赖同一组读数的约束也满足，因为投影不改变读数。

#### 7.4.3 整体误差下的函数拟合

主要内容：有限读取只比较若干观测值，整体积分误差则按指定测度评价整条函数。在Mercer条件下，核的谱坐标可以同时展开平方积分误差与核范数，从而逐方向求出拟合和惩罚的取舍。

论证与表述逻辑：

1. 基于谱表示的函数求解：给定$y\in L^2(\mu)$，紧自伴谱分解将其写为$y=y_0+\sum_{j:\mu_j>0}c_j\psi_j,\qquad y_0\in\ker T_K,\quad \lVert y\rVert_2^2=\lVert y_0\rVert_2^2+\sum_jc_j^2$RKHS中的函数没有$y_0$方向，故这一分量会留下不可消除的误差。

##### 7.4.3.1 基于谱表示的函数求解

主要内容：给定$y\in L^2(\mu)$，紧自伴谱分解将其写为$y=y_0+\sum_{j:\mu_j>0}c_j\psi_j,\qquad y_0\in\ker T_K,\quad \lVert y\rVert_2^2=\lVert y_0\rVert_2^2+\sum_jc_j^2$RKHS中的函数没有$y_0$方向，故这一分量会留下不可消除的误差。

论证与表述逻辑：

1. 附加约束后，配方仍成立，却未必能逐方向独立取极小值。例如要求$\lVert f\rVert_{\mathcal H_K}\leq B$会把所有系数通过$\sum_jb_j^2/\mu_j\leq B^2$耦合；若无约束解超出球，需要重新满足此条件。
2. 仿射核再次给出有限的核对实例。取$K(x,z)=1+xz$、$\mathrm d\mu(x)=\mathrm dx/2$和目标$y(x)=x^2$。
3. 蓝、绿线使用$\lambda=0.01$和$0.1$，点标出前$25$个方向；增大正则化后，各方向的保留比例进一步减小。

#### 7.4.4 平滑能量下的函数与场优化

主要内容：现在不再移动一个点，而是在固定流形上调整整个函数$f$或向量场$\boldsymbol V$。例如给点带上的每处位置分配一个标量，既符合观测又避免局部剧烈变化。

论证与表述逻辑：

1. 定义（Dirichlet能量）：实函数$f$的Dirichlet能量定义为$\mathcal E(f)=\frac12\int_{\mathcal M} \lVert\operatorname{grad}f\rVert_g^2\,\mathrm dV_g$对光滑函数按通常导数理解；积分不有限时取$+\infty$。
2. 在紧域上，不加限制时常量函数已经取得$\mathcal E=0$，所以“最平滑”不会自动保留观测信号。可以规定边界值，加入数据拟合积分$\frac{\lambda}{2}\int|f-y|^2\,\mathrm dV_g$，或施加均值与范数约束。
3. 固定向量场边界迹时$\boldsymbol W=0$；自由边界给出自然条件$\nabla_{\boldsymbol n}\boldsymbol V=0$。

##### 7.4.4.1 基于梯度流的演化求解

主要内容：负梯度流为热方程$\frac{\partial f}{\partial t}=\Delta_gf$对足够光滑且满足相应时间不变边界条件的解，$\frac{\mathrm d}{\mathrm dt}\mathcal E(f_t) =-\int_{\mathcal M}(\Delta_gf_t)^2\,\mathrm dV_g\leq0$热流降低的是整个函数的能量；$\operatorname{grad}f$是每点的切向量，$\operatorname{grad}_{L^2}\mathcal E$却是一个标量函数，二者不可混称。

论证与表述逻辑：

1. 示例（圆上的坐标、能量与谱尺度）：半径为$R$的完整圆采用角坐标$\theta$，$g_{\theta\theta}=R^2$、$\mathrm dV_g=R\,\mathrm d\theta$。
2. 向量场梯度流为$\partial_t\boldsymbol V=-\nabla^*\nabla\boldsymbol V$。
3. 圆上初值$f_0(\theta)=\cos\theta$的直接解为$f_t(\theta)=e^{-t/R^2}\cos\theta$，代入热方程即可核对，其能量为$e^{-2t/R^2}\pi/(2R)$。

### 7.5 收敛与逼近

主要内容：区分函数序列的各种收敛，再分析迭代、展开截断、表示规模、采样与惩罚尺度对函数及函数类逼近的影响。

论证与表述逻辑：

1. 函数序列的收敛：范数收敛要求$\lVert f_n-f\rVert\to0$；逐点收敛要求每个固定$x$的读数收敛，一致收敛则用同一个误差界控制所有输入。
2. 求解和优化下的迭代序列收敛：若$f^{(k)}=\sum_i a_i^{(k)}h_i$且目标函数解由$a^*$表示，则$\lVert f^{(k)}-f^*\rVert_{\mathcal H}^2 =(\boldsymbol a^{(k)}-\boldsymbol a^*)^\top\boldsymbol G(\boldsymbol a^{(k)}-\boldsymbol a^*)$系数趋近一个最优代表因而使函数误差的范数趋零；有界读取又保证预测趋近。
3. 展开截断下的函数序列收敛：固定完备正交系后，前$m$项的投影是一个明确的序列。每个截断在当前方向集合中最佳，却未必在所有同规模非线性表示中最佳。
4. 有限表示约束下的函数逼近：固定定义域、目标集合和误差尺度之后，有限表示可以采取全局多项式、局部片段、非线性单元或可分离因子的形式。下面分别说明怎样构造、误差怎样控制，以及哪些条件不能由“存在一个表示”推出。
5. 有限采样下的能量逼近：只有点云时，常以近邻函数值差构造离散平滑代价$\mathcal E_n(\boldsymbol f)=\frac12\sum_{i,j}w_{i,j}(f_i-f_j)^2$这里约定求和遍历有序点对，取对称非负边权；同一无向边出现两次，其他文献的$1/2$或$1/4$系数需连同边权归一化一起比较。

#### 7.5.1 函数序列的收敛

主要内容：范数收敛要求$\lVert f_n-f\rVert\to0$；逐点收敛要求每个固定$x$的读数收敛，一致收敛则用同一个误差界控制所有输入。

论证与表述逻辑：

1. 峰宽分别为$1/5$和$1/25$；蓝、绿线均由解析式生成。整体能量控制不等于稳定的点值控制。
2. 无限维还使一些有限维中自动成立的性质需要单独检查。有限维子空间仍然总是闭集，但一般无限维子空间未必闭；有限维中的有界序列有收敛子列、线性映射自动连续，在一般无限维空间中也可能失效。
3. 范数变化也可能改变极限是否存在：连续函数以积分误差趋近阶跃函数，并不说明它们在一致范数下形成柯西列。有限维的任意范数等价与闭有界紧性，在无限维函数范围内须重新验证。

#### 7.5.2 求解和优化下的迭代序列收敛

主要内容：若$f^{(k)}=\sum_i a_i^{(k)}h_i$且目标函数解由$a^*$表示，则$\lVert f^{(k)}-f^*\rVert_{\mathcal H}^2 =(\boldsymbol a^{(k)}-\boldsymbol a^*)^\top\boldsymbol G(\boldsymbol a^{(k)}-\boldsymbol a^*)$系数趋近一个最优代表因而使函数误差的范数趋零；有界读取又保证预测趋近。

论证与表述逻辑：

1. 反方向不一定成立：$\ker\boldsymbol G$中的系数变化不改变函数。
2. 一般损失还需验证实际目标的光滑、凸性或其他算法假设，有限表示定理没有额外提供收敛保证。

#### 7.5.3 展开截断下的函数序列收敛

主要内容：固定完备正交系后，前$m$项的投影是一个明确的序列。每个截断在当前方向集合中最佳，却未必在所有同规模非线性表示中最佳。

论证与表述逻辑：

1. Mercer条件下，$f=\sum_j b_j\psi_j$的RKHS截断尾误差为$\sum_{j>m}b_j^2/\mu_j$，$L^2$尾误差为$\sum_{j>m}b_j^2$。

#### 7.5.4 有限表示约束下的函数逼近

主要内容：固定定义域、目标集合和误差尺度之后，有限表示可以采取全局多项式、局部片段、非线性单元或可分离因子的形式。下面分别说明怎样构造、误差怎样控制，以及哪些条件不能由“存在一个表示”推出。

论证与表述逻辑：

1. 先用同一个目标比较这些有限表示。取$f_\star(x)=\left|x-\frac12\right|, \qquad x\in[0,1],$可以看清表示选择的差异。
2. 有限表示的结构与整个表示族的稠密性是不同问题。

##### 7.5.4.1 基于多项式的函数逼近

主要内容：稠密性是一项表示存在性结论：它允许逼近器依赖目标和精度，却没有说明需要多少参数、怎样找到逼近器，或从有限观测能否识别它。

论证与表述逻辑：

1. 命题（Bernstein逼近定理）：对每个$f\in C([0,1])$，$\lVert B_mf-f\rVert_{\infty}\longrightarrow0$因此，多项式在$C([0,1])$的一致范数下稠密。
2. 推导：连续函数在紧区间上一致连续且有界。给定$\varepsilon>0$，可取$\delta>0$使$|u-x|<\delta$时$|f(u)-f(x)|<\varepsilon/2$。
3. 固定$k\geq1$后，取$h>0$且$kh\leq1$，差分$h^{-k}\sum_{j=0}^k(-1)^{k-j}\binom kj K_\sigma(x,jh)$只使用域内中心$0,h,\ldots,kh$。

##### 7.5.4.2 基于样条的函数逼近

主要内容：多项式同时调整全域系数，分段线性样条则把改动限制在少数相邻区间。样条是在每段使用低次多项式、并在结点满足指定衔接条件的函数；这里使用连续的分段直线。

论证与表述逻辑：

1. 若$\omega_f(h)=\sup_{|x-z|\leq h}|f(x)-f(z)|$是$f$的连续模，则$\lVert f-S_hf\rVert_\infty\leq\omega_f(h)$这是因为区间内的插值值是两个端点函数值的凸组合，每个端点距当前点都不超过$h$。
2. 例如$f(x)=x^2$在$[0,1]$只取结点$0,1$时，插值为$x$，最大误差$\max_x(x-x^2)=1/4$，恰好等于$h^2\lVert f''\rVert_\infty/8$。

##### 7.5.4.3 基于神经网络的函数逼近

主要内容：前面的折点目标$f_\star(x)=|x-1/2|$已用两个ReLU单元精确表示。再次写出这个表示，是为了检查每个单元的输入权重与偏置怎样确定折点：$f_\star(x)=\operatorname{ReLU}(x-1/2)+\operatorname{ReLU}(1/2-x)$两个单元的偏置将折点放在$1/2$，输入系数的正负决定折点哪一侧激活。

论证与表述逻辑：

1. 命题（单隐藏层的通用逼近）：设$\mathcal X\subseteq\mathbb R^d$为非空紧集，$f:\mathcal X\to\mathbb R$连续，$\sigma:\mathbb R\to\mathbb R$连续且不是多项式。对任意$\varepsilon>0$，存在有限宽度$m$、实数$a_j,b_j,c$以及$\boldsymbol w_j\in\mathbb R^d$，使$\begin{aligned} g(\boldsymbol x)&=c+\sum_{j=1}^m a_j\sigma(\boldsymbol w_j^{\top}\boldsymbol x+b_j),\\ \sup_{\boldsymbol x\in\mathcal X}|g(\boldsymbol x)-f(\boldsymbol x)|&<\varepsilon \end{aligned}$。
2. 这是Leshno等结果在连续激活情形下的表述。Sigmoid、Tanh与ReLU都满足激活条件；定理不要求处处可微。
3. 误差范数同样决定结论。若只要求$L^2$误差小，逼近器可以在小测度区域出现较大尖峰；若要求一致误差小，则必须同时控制所有输入。

##### 7.5.4.4 基于分离表示的函数逼近

主要内容：前面的基函数、局部片段与非线性单元都描述同一个目标函数。若目标的自变量能够分成两组，还可以把每项写成两组变量各自函数的乘积，以少量乘积项压缩二者的联合作用。

论证与表述逻辑：

1. Cauchy--Schwarz不等式还把因子尺度传到每个矩阵元素：$|E(p,q)| \leq \lVert\boldsymbol{u}(p)\rVert_2 \lVert\boldsymbol{v}(q)\rVert_2$所以秩控制可用方向数，因子范数控制沿这些方向能够产生的幅度。
2. 强化学习中的某些复杂度概念会把模型与分布之间的Bellman残差组织成类似矩阵，再研究其秩或因子化结构。那里的矩阵条目、可实现性、查询协议和样本保证依赖具体决策对象，必须在相应章节重新定义。

#### 7.5.5 有限采样下的能量逼近

主要内容：只有点云时，常以近邻函数值差构造离散平滑代价$\mathcal E_n(\boldsymbol f)=\frac12\sum_{i,j}w_{i,j}(f_i-f_j)^2$这里约定求和遍历有序点对，取对称非负边权；同一无向边出现两次，其他文献的$1/2$或$1/4$系数需连同边权归一化一起比较。

论证与表述逻辑：

1. 先取正整数$n$，在$[0,1]$上取规则网格$x_i=ih$，$i=0,\ldots,n$，$h=1/n$，并固定$f\in C^1([0,1])$。
2. 向量场离散还要给出跨点比较。

#### 7.5.6 惩罚尺度变化下的函数逼近

主要内容：写$y=y_0+y_+$，其中$y_0\in\ker T_K$、$y_+=\sum_jc_j\psi_j$，则$\lVert f_\lambda-y\rVert_{L^2}^2 =\lVert y_0\rVert_{L^2}^2+ \sum_j\left(\frac{\lambda}{\mu_j+\lambda}\right)^2c_j^2$当$\lambda\downarrow0$时，每项正谱误差趋零且不超过$c_j^2$。

论证与表述逻辑：

1. 矩阵迹汇总有限个方向的贡献；无限维空间中的方向可能有无穷多个，因此还要核对这份总量是否有限。下面把算子条件与所选正则化尺度分开。
2. 定义（迹类条件与有效维度）：设$A$为Hilbert空间上的紧线性算子。$A^*A$的正特征值开方后得到奇异值$s_j(A)$，按重数排列；若只有有限个，可在其后补零。若$\sum_j s_j(A)<\infty$，称$A$为迹类算子（trace-class operator）。对正算子，这等价于非负特征值之和有限，它的迹就是这个和。若紧正算子$T_K$的正特征值为$(\mu_j)$，给定$\lambda>0$，其有效维度（effective dimension）定义为$d_{\mathrm{eff}}(\lambda) = \sum_{j:\mu_j>0}\frac{\mu_j}{\mu_j+\lambda},$这里要求右侧级数有限；等价地，$d_{\mathrm{eff}}(\lambda) = \operatorname{tr}\bigl(T_K(T_K+\lambda I)^{-1}\bigr)$并要求$T_K(T_K+\lambda I)^{-1}$为迹类。
3. 有效维度不是代数维数。无限维空间在固定$\lambda$下可以有有限有效维度；反过来，一个有限参数化若参数到函数的映射高度敏感，也可能形成很大的函数集合。

#### 7.5.7 统一误差约束下的函数类逼近

主要内容：本节转向函数近似，问在指定误差范围内，需要多少个代表函数才能近似整个函数类。模式是否可实现与近似误差有多大，是两个需要分别说明的问题。

论证与表述逻辑：

1. 伪维检查能否跨过固定阈值，胖打散维还规定阈值两侧的间隔。函数近似则需要另行规定比较哪些输入、怎样汇总误差：上确界误差关注最坏位置，平方积分误差关注测度加权的整体差异。
2. 定义（序贯覆盖与序贯覆盖数）：给定深度为$T$的查询树$\boldsymbol x$、非空实值函数类$\mathcal F$和$\varepsilon>0$。实数树$v=(v_t)$的每层映射为$v_t:\{-1,1\}^{t-1}\to\mathbb R$。若这些树组成的有限集合$\mathcal C$满足：对每个$f\in\mathcal F$和每条路径$\boldsymbol\epsilon\in\{-1,1\}^T$，都存在$v\in\mathcal C$使$\left( \frac1T\sum_{t=1}^{T} \left| f\bigl(\boldsymbol{x}_t(\epsilon_{1:t-1})\bigr) - v_t(\epsilon_{1:t-1}) \right|^2 \right)^{1/2} \leq\varepsilon,$则称$\mathcal C$为该查询树上的序贯$\varepsilon$-覆盖。再定义$N_2^{\mathrm{seq}}(\varepsilon,\mathcal F,T) =\sup_{\boldsymbol x:\,\text{深度为 }T} N_2^{\mathrm{seq}}(\varepsilon,\mathcal F,\boldsymbol x),$其中上确界遍历全部深度为$T$的查询树。
3. 回到$f_\star(x)=|x-1/2|$，Bernstein多项式在一致范数下随次数增加逼近它；含结点$1/2$的线性样条与两个ReLU单元则能精确表示它。

### 7.6 扰动与稳定性

主要内容：按输出对象分别讨论读取与变换、拟合函数及离散能量的扰动，说明稳定性所依赖的范数与惩罚条件。

论证与表述逻辑：

1. 运算的误差传播：固定有界算子$A$时，$\lVert A(f+h)-Af\rVert\leq\lVert A\rVert_{\mathrm{op}}\lVert h\rVert$。
2. 函数解的稳定性：固定读取方向与$\lambda>0$，平方拟合的代表系数满足$(\boldsymbol G+n\lambda\boldsymbol I)\boldsymbol a=\boldsymbol y$。
3. 离散目标的稳定性：在已规定的离散标量能量上，固定函数记录$\boldsymbol f$，边权变化$\delta w_{i,j}$产生$|\widetilde{\mathcal E}_n(\boldsymbol f)-\mathcal E_n(\boldsymbol f)| \leq\tfrac12\sum_{i,j}|\delta w_{i,j}|(f_i-f_j)^2$这个界比较同一个记录在两个二次型中的目标值。

#### 7.6.1 运算的误差传播

主要内容：固定有界算子$A$时，$\lVert A(f+h)-Af\rVert\leq\lVert A\rVert_{\mathrm{op}}\lVert h\rVert$。

论证与表述逻辑：

1. RKHS中固定位置的读取界为$\sqrt{K(x,x)}$；位置由$x$变为$z$，还需$|f(x)-f(z)|\leq\lVert f\rVert\lVert K_x-K_z\rVert$。

#### 7.6.2 函数解的稳定性

主要内容：固定读取方向与$\lambda>0$，平方拟合的代表系数满足$(\boldsymbol G+n\lambda\boldsymbol I)\boldsymbol a=\boldsymbol y$。

论证与表述逻辑：

1. 整体误差拟合中的谱收缩$t/(t+\lambda)$同样使$L^2$目标扰动的解响应不超过输入误差；RKHS尺度则对小$t$方向另外计价。

#### 7.6.3 离散目标的稳定性

主要内容：在已规定的离散标量能量上，固定函数记录$\boldsymbol f$，边权变化$\delta w_{i,j}$产生$|\widetilde{\mathcal E}_n(\boldsymbol f)-\mathcal E_n(\boldsymbol f)| \leq\tfrac12\sum_{i,j}|\delta w_{i,j}|(f_i-f_j)^2$这个界比较同一个记录在两个二次型中的目标值。

论证与表述逻辑：

1. 若只改变优化用的内积，目标函数并未改变，梯度及演化过程会改变；若该权重同时进入目标二次型，最优任务也已变化。离散非负性不能替代这两种判断。

### 7.7 本章小结

主要内容：连接Hilbert空间、稳定读取、核表示与函数拟合，说明整体误差、点值与极限归属需要分别检查。

论证与表述逻辑：

1. 函数空间沿用线性组合与几何输入域，却必须重新检查整体误差、极限归属和读取是否良定义。Hilbert完备性与闭性让最近分量存在，Riesz表示把稳定读取变为方向，核空间进一步使点值读取可由空间范数控制。
2. 有限观测、整体误差与平滑能量定义不同的求解任务。有限表示定理减少不可见方向，不单独保证存在、系数唯一或算法收敛；展开截断、表示规模、采样与惩罚尺度又分别控制不同的逼近误差。
