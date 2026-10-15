# 卷2《数学准备：概率、因果与决策》：第2部分“演化、控制、决策与博弈”大纲

正文入口：[tex/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/part.tex](../../tex/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/part.tex)。章号按本卷连续编号，以下标题和顺序对应当前入口实际接入的正文。

由状态演化进入可实施策略，分别研究轨迹控制、价值优化和多方响应；区分动态、观测、目标与交互带来的条件。

## 第4章 动力系统

正文：[01-action-and-state.tex](../../tex/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/01-action-and-state.tex)。

### 4.1 状态演化的建模

主要内容：依次建立离散、连续和随机状态更新，明确初值、输入及状态充分性，说明历史依赖何时要求扩充状态。用当前量替代整段历史的前提是该量已概括对未来仍有影响的部分，这一前提在状态充分性处检查。

论证与表述逻辑：

1. 状态、输入与初值的界定：把当前房间温差记作状态，是因为这个模型只需要它和下一段加热量，就能继续计算未来。若历史还通过其他未记录因素起作用，状态就需要扩充。
2. 离散时间下的状态更新：设$\mathcal X$是允许的状态集合，$\mathcal U$是输入集合。一步更新映射$F_t:\mathcal X\times\mathcal U\longrightarrow\mathcal X,\qquad \boldsymbol x_{t+1}=F_t(\boldsymbol x_t,\boldsymbol u_t)$直接规定下一状态。
3. 连续时间下的状态变化：若关注相邻采样时刻之间发生了什么，需要规定瞬时变化率，而不仅是相隔一步的差值。
4. 随机扰动下的状态演化：给定相同初温与加热量，开门、风速等未显式建模的作用仍可能改变真实温度。把这些作用表示成过程噪声后，更新公式不再只产生一条确定轨迹，而是把噪声的联合规律转换为状态的联合规律。
5. 历史依赖下的状态表示：另一种构造从希望保留的历史特征出发。例如为一段输入保留平均值与线性趋势，就可把投影坐标当作状态。

#### 4.1.1 状态、输入与初值的界定

主要内容：把当前房间温差记作状态，是因为这个模型只需要它和下一段加热量，就能继续计算未来。若历史还通过其他未记录因素起作用，状态就需要扩充。

论证与表述逻辑：

1. 若同一室温下，不同墙体蓄热会导致不同的下一步温度，室温一个坐标就不再足够，需要加入墙体温度。传感器滞后同样可能需要独立的内部状态。
2. 初始条件规定轨迹从哪里开始，输入规定沿途施加什么作用，演化规律规定这些作用怎样改变状态。输出则是模型对外显示的量。

#### 4.1.2 离散时间下的状态更新

主要内容：设$\mathcal X$是允许的状态集合，$\mathcal U$是输入集合。一步更新映射$F_t:\mathcal X\times\mathcal U\longrightarrow\mathcal X,\qquad \boldsymbol x_{t+1}=F_t(\boldsymbol x_t,\boldsymbol u_t)$直接规定下一状态。

论证与表述逻辑：

1. 线性模型常写为$\boldsymbol x_{t+1}=\boldsymbol A_t\boldsymbol x_t+\boldsymbol B_t\boldsymbol u_t,\qquad \boldsymbol x_t\in\mathbb R^d,\quad \boldsymbol u_t\in\mathbb R^m$它关于状态与输入的联合变量是线性的；固定非零输入后，它关于状态通常是仿射的。
2. 一个可直接计算的模型是带泄漏的记忆：$x_{t+1}=a x_t+b u_t,\qquad x_0\ \text{给定}$温度例对应$a=0.8,b=1$。

#### 4.1.3 连续时间下的状态变化

主要内容：若关注相邻采样时刻之间发生了什么，需要规定瞬时变化率，而不仅是相隔一步的差值。常微分方程（ordinary differential equation, ODE）初值问题写为$\dot{\boldsymbol x}(t)=\boldsymbol f(t,\boldsymbol x(t),\boldsymbol u(t)),\qquad \boldsymbol x(t_0)=\boldsymbol x_0$给定输入后，右侧是作用在当前状态上的向量场。

论证与表述逻辑：

1. 定义（可分Hamilton系统）：令$\boldsymbol q,\boldsymbol p\in\mathbb R^d$分别为位置与动量，$U$为连续可微的势能，$\boldsymbol M$为对称正定的质量矩阵。可分Hamilton量为$H(\boldsymbol q,\boldsymbol p)=U(\boldsymbol q)+\frac12\boldsymbol p^\top\boldsymbol M^{-1}\boldsymbol p$相应的Hamilton方程为$\dot{\boldsymbol q}=\nabla_{\boldsymbol p}H,\qquad \dot{\boldsymbol p}=-\nabla_{\boldsymbol q}H$。
2. 第一式由动量得到位置速度，第二式由势能坡度得到动量变化。

#### 4.1.4 随机扰动下的状态演化

主要内容：给定相同初温与加热量，开门、风速等未显式建模的作用仍可能改变真实温度。把这些作用表示成过程噪声后，更新公式不再只产生一条确定轨迹，而是把噪声的联合规律转换为状态的联合规律。

论证与表述逻辑：

1. 离散时间下的随机状态更新：独立性使$\mathbb P(\boldsymbol x_{t+1}\in A\mid\boldsymbol x_{0:t})=K_t(\boldsymbol x_t,A)$，这才得到当前状态的Markov性质。
2. 连续时间下的随机状态变化：离散噪声可以逐次相加；连续时间的噪声则要按增量尺度选择驱动。Brownian增量在长度$h$的区间上具有$h$阶方差，Poisson驱动记录区间内到达的事件数。

##### 4.1.4.1 离散时间下的随机状态更新

主要内容：独立性使$\mathbb P(\boldsymbol x_{t+1}\in A\mid\boldsymbol x_{0:t})=K_t(\boldsymbol x_t,A)$，这才得到当前状态的Markov性质。

论证与表述逻辑：

1. 常用的线性加性模型为$\boldsymbol x_{t+1}=\boldsymbol A_t\boldsymbol x_t+\boldsymbol B_t\boldsymbol u_t+\boldsymbol w_{t+1}$若$\boldsymbol w_{t+1}\sim\mathcal N(\boldsymbol0,\boldsymbol Q_{t+1})$且独立于初态与其他过程噪声，$K_t(\boldsymbol x,\cdot)=\mathcal N(\boldsymbol A_t\boldsymbol x+\boldsymbol B_t\boldsymbol u_t,\boldsymbol Q_{t+1})$。
2. 相关噪声需要重新检查条件结构。例如$x_{t+1}=a x_t+w_{t+1}$，而$w_{t+1}=\rho w_t+\varepsilon_{t+1}$，其中新$\varepsilon$独立。
3. 温度模型现在恢复为$x_{t+1}=0.8x_t+u_t+w_{t+1},\qquad w_{t+1}\sim\mathcal N(0,0.04)$取各$w_t$相互独立且独立于初态。

##### 4.1.4.2 连续时间下的随机状态变化

主要内容：离散噪声可以逐次相加；连续时间的噪声则要按增量尺度选择驱动。Brownian增量在长度$h$的区间上具有$h$阶方差，Poisson驱动记录区间内到达的事件数。

论证与表述逻辑：

1. 给定漂移规律、噪声幅度与初值，建模任务是规定这些增量如何进入状态。连续时间并不把驱动强行解释成普通时间导数。

#### 4.1.5 历史依赖下的状态表示

主要内容：另一种构造从希望保留的历史特征出发。例如为一段输入保留平均值与线性趋势，就可把投影坐标当作状态。

论证与表述逻辑：

1. 投影固定$t>0$并使用非负权重测度$\mu_t$，输入与基函数取自L^2等价类。有限维子空间中的基线性无关，使Gram二次型成为非零函数的正平方范数，从而保证坐标唯一；$t=0$的退化区间另给初始化。
2. 窗口本身移动时，状态变化不全来自新输入。
3. 所以有限个历史特征不自动形成能独立接续演化的有限维状态；需要额外状态、特别的基与权重，或对边界项作近似。
4. HiPPO一类方法正是通过历史投影设计状态坐标它保存哪些变化，由窗口、权重和基共同决定。投影理论给出相应度量下的逼近误差，不意味着一般历史被无损保存，也不自动保证所构造递推对扰动稳定。

### 4.2 路径的累计运算与状态变换

主要内容：比较输入累计、跳跃与连续随机积分，再讨论状态函数在不同路径上的变化公式。

论证与表述逻辑：

1. 历史输入的累计作用：先保持离散时间。
2. 跳跃路径上的随机积分：离散更新只需说明每一步使用哪些已知量。把更新间隔缩到连续时间后，还须说明被积系数在时间与随机结果的联合空间中是否可测。
3. 连续路径上的随机积分：以下$\boldsymbol W$是在同一滤过下的$m$维标准Brownian运动，分量独立，其增量独立于过去且协方差为时间长度乘$\boldsymbol I_m$。
4. 连续随机演化下的状态函数变换：读数、能量和损失通常是状态的函数。已知状态怎样累计，怎样求这些函数的变化？
5. 跳跃随机演化下的状态函数变换：考虑连续Itô部分加有限活动跳跃的右连续过程$\boldsymbol X_t=\boldsymbol X_0+\int_0^t\boldsymbol b_s\,\mathrm ds +\int_0^t\boldsymbol\sigma_s\,\mathrm d\boldsymbol W_s +\int_0^t\boldsymbol\gamma_s\,\mathrm dN_s,$其中$\boldsymbol\gamma$可预测、在各事件处有限，$\boldsymbol b,\boldsymbol\sigma$满足前述局部可积条件。

#### 4.2.1 历史输入的累计作用

主要内容：先保持离散时间。

论证与表述逻辑：

1. 前两步为$\boldsymbol x_1=\boldsymbol A\boldsymbol x_0+\boldsymbol B\boldsymbol u_0$及$\boldsymbol x_2=\boldsymbol A^2\boldsymbol x_0+\boldsymbol A\boldsymbol B\boldsymbol u_0+\boldsymbol B\boldsymbol u_1$。
2. 用标量$a=1/2,b=c=1,d=0,x_0=0$核对。依次输入$u_0=1,u_1=2,u_2=1$，递推给出$y_0=0,y_1=1,y_2=5/2,y_3=9/4$。
3. 时变系统用有序乘积$\boldsymbol\Phi(t,s)=\boldsymbol A_{t-1}\cdots\boldsymbol A_s\quad(t>s),\qquad \boldsymbol\Phi(s,s)=\boldsymbol I$传播齐次状态，于是$\boldsymbol x_t=\boldsymbol\Phi(t,0)\boldsymbol x_0+ \sum_{\tau=0}^{t-1}\boldsymbol\Phi(t,\tau+1)\boldsymbol B_\tau\boldsymbol u_\tau$若输出为$\boldsymbol C_t\boldsymbol x_t+\boldsymbol D_t\boldsymbol u_t$，对应核为$\boldsymbol K_{t,t}=\boldsymbol D_t,\qquad \boldsymbol K_{t,\tau}=\boldsymbol C_t\boldsymbol\Phi(t,\tau+1)\boldsymbol B_\tau\quad(\tau<t)$它依赖两个绝对时刻，通常不只依赖滞后$t-\tau$，所以线性仍在，平移不变性却已消失。

#### 4.2.2 跳跃路径上的随机积分

主要内容：离散更新只需说明每一步使用哪些已知量。把更新间隔缩到连续时间后，还须说明被积系数在时间与随机结果的联合空间中是否可测。

论证与表述逻辑：

1. 一个过程$H$适应，表示每个$H_t$对$\mathcal F_t$可测。若对每个$T$，$(t,\omega)\mapsto H_t(\omega)$在$[0,T]\times\Omega$上对$\mathcal B([0,T])\otimes\mathcal F_T$可测，则称它渐进可测。
2. 左极限不是无关紧要的记号。例如单位幅度事件有$\int_0^t N_{s-}\,\mathrm dN_s=\frac{N_t(N_t-1)}2,\qquad \sum_{\tau_j\leq t}N_{\tau_j}=\frac{N_t(N_t+1)}2$右侧第二个和使用了事件后的计数，两者相差$N_t$。

#### 4.2.3 连续路径上的随机积分

主要内容：以下$\boldsymbol W$是在同一滤过下的$m$维标准Brownian运动，分量独立，其增量独立于过去且协方差为时间长度乘$\boldsymbol I_m$。

论证与表述逻辑：

1. 对可预测$H$，若$\mathbb E\int_0^T H_t^2\,\mathrm dt<\infty$，用简单可预测过程在该范数下逼近，等距关系使积分序列在$L^2$中为Cauchy序列，从而定义与逼近选择无关的积分。
2. 定义（连续Itô过程）：设$\boldsymbol X_0$对$\mathcal F_0$可测，$\boldsymbol b_t$渐进可测，$\boldsymbol\sigma_t$可预测，且每个有限$T$上$\int_0^T(\|\boldsymbol b_t\|+\|\boldsymbol\sigma_t\|_{\mathrm F}^2)\,\mathrm dt<\infty$几乎必然。过程$\boldsymbol X_t=\boldsymbol X_0+\int_0^t\boldsymbol b_s\,\mathrm ds +\int_0^t\boldsymbol\sigma_s\,\mathrm d\boldsymbol W_s$称为连续Itô过程。漂移积分有有限变差，随机积分是连续局部鞅。
3. 积分约定可以由Brownian平方直接辨认：$W_{t_{i+1}}^2-W_{t_i}^2 =2W_{t_i}\Delta W_i+(\Delta W_i)^2$求和并回用二次变差，左端点和趋于$(W_T^2-T)/2$，右端点和趋于$(W_T^2+T)/2$。

#### 4.2.4 连续随机演化下的状态函数变换

主要内容：读数、能量和损失通常是状态的函数。已知状态怎样累计，怎样求这些函数的变化？

论证与表述逻辑：

1. 命题（Itô公式）：若要对等式直接取期望，还须漂移项可积，且随机被积项满足例如$\mathbb E\int_0^T\|\nabla f^\top\boldsymbol\sigma_t\|^2\,\mathrm dt<\infty$；局部鞅本身不保证期望为零。
2. 先说明关键估计，以免把二阶项当作形式记忆规则。对有界连续适应系数，局部化后的Taylor展开中，漂移平方和的期望为$O(|\pi|)$，漂移与随机项乘积和的$L^1$范数为$O(|\pi|^{1/2})$；这里$|\pi|$为分割的最大间距。
3. 例如$f(x)=x^2$给出$W_T^2=2\int_0^T W_s\,\mathrm dW_s+T,\qquad \int_0^T W_s\,\mathrm dW_s=(W_T^2-T)/2$常数系数则有$\int_0^T c\,\mathrm dW_s=cW_T$。

#### 4.2.5 跳跃随机演化下的状态函数变换

主要内容：考虑连续Itô部分加有限活动跳跃的右连续过程$\boldsymbol X_t=\boldsymbol X_0+\int_0^t\boldsymbol b_s\,\mathrm ds +\int_0^t\boldsymbol\sigma_s\,\mathrm d\boldsymbol W_s +\int_0^t\boldsymbol\gamma_s\,\mathrm dN_s,$其中$\boldsymbol\gamma$可预测、在各事件处有限，$\boldsymbol b,\boldsymbol\sigma$满足前述局部可积条件。

论证与表述逻辑：

1. 若把$\nabla f^\top\mathrm d\boldsymbol X$统一写在前面，则还须显式加上$\sum_{\tau_j\leq t} [f(\tau_j,\boldsymbol X_{\tau_j})-f(\tau_j,\boldsymbol X_{\tau_j-}) -\nabla f(\tau_j,\boldsymbol X_{\tau_j-})^\top\Delta\boldsymbol X_{\tau_j}]$它不是只有二阶的近似，而是扣掉已计入一阶项后的全部有限差。
2. 令$X=N$、$f(x)=x^2$，每次事件使平方增加$2N_{s-}+1$，所以$N_t^2=\int_0^t(2N_{s-}+1)\,\mathrm dN_s =2\int_0^tN_{s-}\,\mathrm d\widetilde N_s +\widetilde N_t+2\lambda\int_0^tN_s\,\mathrm ds+\lambda t$于是$\mathbb E N_t^2=(\lambda t)^2+\lambda t$。

### 4.3 状态轨迹与分布的求解

主要内容：分别求确定轨迹、随机轨迹和状态分布，再以时间离散化近似原问题，区分演化求解与观测推断。

论证与表述逻辑：

1. 随机扰动下的初值轨迹求解：前面的随机积分累计给定系数；现在让系数随未知状态变化，便要寻找与累计结果相容的整条轨迹。给定初值和同一条噪声驱动后，轨迹能否被唯一确定？
2. 给定初始分布下的状态分布求解：逐路径的积分式不一定最适合回答“某时刻落在何处”的概率问题。线性模型可传播少量矩，一般模型则要传播分布对测试函数的作用。
3. 离散化条件下的轨迹求解：已知轨迹存在唯一，不代表能写出解析式。记从$t_n$到$t_{n+1}=t_n+h$的精确流为$\varphi_{t_{n+1},t_n}$，数值方法以可计算的一步映射$\Psi_{h,t_n}$近似它。

#### 4.3.1 离散时间下的初值轨迹求解

主要内容：给定初值和离散更新后计算轨迹，比较一般逐步递推与仿射结构支持的并行组合。

论证与表述逻辑：

1. 先沿时间应用更新规则，说明一次输入和初态如何确定后继。
2. 在仿射情形中把多个更新写成可结合的复合运算，再说明并行扫描改变执行依赖而不改变所求轨迹。

##### 4.3.1.1 基于逐步递推的轨迹求解

主要内容：把给定输入吸收进$F_t^{\boldsymbol u}(\boldsymbol x)=F_t(\boldsymbol x,\boldsymbol u_t)$，前两步为$\boldsymbol x_1=F_0^{\boldsymbol u}(\boldsymbol x_0),\qquad \boldsymbol x_2=F_1^{\boldsymbol u}\bigl(F_0^{\boldsymbol u}(\boldsymbol x_0)\bigr)$一般状态是有序复合$\boldsymbol x_t=(F_{t-1}^{\boldsymbol u}\circ\cdots\circ F_0^{\boldsymbol u})(\boldsymbol x_0)$。

论证与表述逻辑：

1. 泄漏模型可进一步展开：$x_t=a^t x_0+\sum_{j=0}^{t-1}a^{t-1-j}b u_j$证明从$t=0$的空和开始。
2. 取独立于温度任务的泄漏例$a=1/2,b=1,x_0=0$。仅在第零步输入$u_0=1$时，$x_1=1,x_2=1/2,x_3=1/4$；若$u_0=u_1=1$，则$x_2=3/2$，其中$1/2$来自旧输入，$1$来自新输入。

##### 4.3.1.2 基于并行扫描的仿射轨迹求解

主要内容：逐步递推沿时间产生一条串行依赖链。如果每步都是仿射映射，一整段更新仍可压成同样大小的仿射映射，就能先合并这些映射再求各个中间状态。

论证与表述逻辑：

1. 下传时，节点接收其区间之前已经完成的累计映射$p$。左孩子继续接收$p$；若左块的总映射是$L$，右孩子就接收$L\circ p$。
2. 总工作量统计所有节点执行的合并次数，计算深度统计最长依赖链上的合并次数。$T$步形成的平衡树有$O(T)$个节点、$O(\log T)$层，上下两阶段在每个节点只做常数次合并，同层互不依赖的节点可同时计算。
3. 扫描保留时间次序。若$g_1(\boldsymbol x)=\operatorname{diag}(2,1)\boldsymbol x$、$g_2(\boldsymbol x)=\boldsymbol x+(1,0)^\top$，则$(g_2\circ g_1)(\boldsymbol0)=(1,0)^\top,\qquad (g_1\circ g_2)(\boldsymbol0)=(2,0)^\top$这两个结果说明结合律不能换成交换律。

#### 4.3.2 连续时间下的初值轨迹求解

主要内容：先建立连续初值问题的存在、唯一和延拓条件，再利用线性结构求出初值与输入的作用。

论证与表述逻辑：

1. 从局部条件讨论轨迹能否定义及是否唯一，检查解何时可继续延伸。
2. 在线性模型中使用状态转移与输入累计表达轨迹，区分解析表达成立与数值计算的后续问题。

##### 4.3.2.1 初值约束下的轨迹存在与延拓

主要内容：一个“几乎处处给出斜率”的公式，要能恢复整条曲线，必须排除没有被导数记录的奇异变化。为此采用绝对连续曲线，而非任意连续曲线。

论证与表述逻辑：

1. 引理（Grönwall积分估计）：设$e$为$[a,T]$上非负连续函数，$b$为非负可积函数。更一般地，若右侧另有$\int_a^t r(s)\,\mathrm ds$，其中$r\geq0$可积，则$e(t)\leq c\,\mathrm e^{\int_a^t b} +\int_a^t r(s)\,\mathrm e^{\int_s^t b}\,\mathrm ds$。
2. 推导：令$E(t)=c+\int_a^t[b(s)e(s)+r(s)]\,\mathrm ds$，则$e\leq E$，且$E'\leq bE+r$几乎处处成立。乘以绝对连续的积分因子$\exp(-\int_a^t b)$，使用乘积法则并从$a$积分到$t$，得$E(t)\mathrm e^{-\int_a^t b} \leq c+\int_a^t r(s)\mathrm e^{-\int_a^s b}\,\mathrm ds$再乘回积分因子并用$e\leq E$即可；取$r=0$得到第一式。
3. 若$\|\boldsymbol g(t,\boldsymbol x)\|\leq b(t)\|\boldsymbol x\|+r(t)$，其中$b,r$在每个有限时间区间可积，积分方程与此引理给出有限的状态上界。

##### 4.3.2.2 线性演化下的轨迹求解

主要内容：连续时间对应的时不变方程是$\dot{\boldsymbol x}(t)=\boldsymbol A\boldsymbol x(t)+\boldsymbol B\boldsymbol u(t)$对固定有限方阵$\boldsymbol A$，矩阵指数满足$\frac{\mathrm d}{\mathrm dt}\mathrm e^{t\boldsymbol A} =\boldsymbol A\mathrm e^{t\boldsymbol A}=\mathrm e^{t\boldsymbol A}\boldsymbol A$，且$\mathrm e^{t\boldsymbol A}$的逆为$\mathrm e^{-t\boldsymbol A}$。

论证与表述逻辑：

1. 时变系数需要连续时间的传播算子。
2. 定义（状态转移矩阵）：对连续矩阵函数$\boldsymbol A(t)$，状态转移矩阵$\boldsymbol\Phi(t,s)$是满足$\partial_t\boldsymbol\Phi(t,s)=\boldsymbol A(t)\boldsymbol\Phi(t,s),\qquad \boldsymbol\Phi(s,s)=\boldsymbol I$的矩阵值解。
3. 一般不能令$\boldsymbol\Phi(t,s)=\exp(\int_s^t\boldsymbol A(r)\,\mathrm dr)$。

#### 4.3.3 随机扰动下的初值轨迹求解

主要内容：前面的随机积分累计给定系数；现在让系数随未知状态变化，便要寻找与累计结果相容的整条轨迹。给定初值和同一条噪声驱动后，轨迹能否被唯一确定？

论证与表述逻辑：

1. 定义（Itô随机微分方程与强解）：在给定的通常滤过概率空间上，设$\boldsymbol W$为$m$维Brownian运动，$\boldsymbol X_0$为$\mathcal F_0$可测初值。给定联合Borel可测系数$\boldsymbol b:[0,T]\times\mathbb R^d\to\mathbb R^d$、$\boldsymbol\sigma:[0,T]\times\mathbb R^d\to\mathbb R^{d\times m}$，Itô随机微分方程的扩散形式为$\mathrm d\boldsymbol X_t=\boldsymbol b(t,\boldsymbol X_t)\,\mathrm dt +\boldsymbol\sigma(t,\boldsymbol X_t)\,\mathrm d\boldsymbol W_t$解是满足局部可积条件的连续适应过程，使$\boldsymbol X_t=\boldsymbol X_0+\int_0^t\boldsymbol b(s,\boldsymbol X_s)\,\mathrm ds +\int_0^t\boldsymbol\sigma(s,\boldsymbol X_s)\,\mathrm d\boldsymbol W_s$以概率$1$对所有$t$同时成立。若解适应于初值和给定驱动的历史所生成、完成并取右连续版本的滤过，则称为强解；它不另外使用随机信息。
2. 弱解允许概率空间、驱动和过程一起作为待求对象，但它们必须满足同样的驱动联合条件、初值分布及积分方程。路径唯一性比较同一空间、同一初值和同一驱动上的两个解，要求它们不可区分，即几乎必然在所有时刻相同。

##### 4.3.3.1 随机初值问题的存在与唯一性

主要内容：为证明状态相关的随机积分方程有解，可以反复将上一条候选轨迹代入被积系数。相邻候选的误差需要在整个有限时段上一同控制；Itô等距只给出固定终点的二阶误差，鞅最大不等式将它扩展到时段内的最大波动。

论证与表述逻辑：

1. 命题（SDE强解的存在唯一性）：设$\boldsymbol W$在通常滤过下为标准Brownian运动，$\boldsymbol X_0\in L^2(\mathcal F_0)$。
2. 推导：在短区间$[a,a+h]$固定平方可积初值$\boldsymbol\xi$，取连续适应过程的空间，范数为$\|\boldsymbol Z\|_{\mathcal S^2}^2 =\mathbb E\sup_{a\leq t\leq a+h}\|\boldsymbol Z_t\|^2$，过程按不可区分等价。这是完备空间：Cauchy列可选子列几乎必然一致收敛，极限连续且适应，再用范数Cauchy性质得到$\mathcal S^2$收敛。定义$(\mathcal T\boldsymbol Z)_t=\boldsymbol\xi+\int_a^t\boldsymbol b(s,\boldsymbol Z_s)\,\mathrm ds +\int_a^t\boldsymbol\sigma(s,\boldsymbol Z_s)\,\mathrm d\boldsymbol W_s$Borel系数与连续适应过程的复合渐进可测；增长界、Cauchy--Schwarz、Itô等距和最大不等式使$\mathcal T$映回该空间。
3. 在两次事件间解扩散方程，在$\tau_j$处设$\boldsymbol X_{\tau_j}=\boldsymbol X_{\tau_j-} +\boldsymbol\gamma(\tau_j,\boldsymbol X_{\tau_j-})$。

##### 4.3.3.2 线性随机演化下的轨迹求解

主要内容：线性结构把“系数依赖解”的难点拆开。

论证与表述逻辑：

1. 标量Ornstein--Uhlenbeck（OU）过程把泄漏记忆与持续噪声放在一起：$\mathrm dX_t=-\lambda X_t\,\mathrm dt+\sigma\,\mathrm dW_t,\qquad\lambda>0$由$\mathrm d(\mathrm e^{\lambda t}X_t)= \sigma\mathrm e^{\lambda t}\,\mathrm dW_t$得$X_t=\mathrm e^{-\lambda t}X_0+ \sigma\int_0^t\mathrm e^{-\lambda(t-s)}\,\mathrm dW_s$若$X_0=x_0$为常数，第二项为零均值高斯，因而$X_t\sim\mathcal N(\mathrm e^{-\lambda t}x_0, \sigma^2(1-\mathrm e^{-2\lambda t})/(2\lambda))$。

#### 4.3.4 给定初始分布下的状态分布求解

主要内容：逐路径的积分式不一定最适合回答“某时刻落在何处”的概率问题。线性模型可传播少量矩，一般模型则要传播分布对测试函数的作用。

论证与表述逻辑：

1. 线性演化下的均值与协方差求解：随机积分为零均值、与初值独立，故$\boldsymbol m_t&=\boldsymbol\Phi(t,0)\boldsymbol m_0+\int_0^t\boldsymbol\Phi(t,s)\boldsymbol c_s\,\mathrm ds,\\ \boldsymbol P_t&=\boldsymbol\Phi(t,0)\boldsymbol P_0\boldsymbol\Phi(t,0)^\top +\int_0^t\boldsymbol\Phi(t,s)\boldsymbol G_s\boldsymbol G_s^\top\boldsymbol\Phi(t,s)^\top\,\mathrm ds$这里积分中的$\boldsymbol G_s\boldsymbol G_s^\top$是确定性矩阵。
2. 一般演化下的分布与密度求解：设确定性系数与适当的解唯一性使$\boldsymbol X$成为Markov过程。要知道分布怎样变化，可先观察任意光滑“读数”$\varphi(\boldsymbol X_t)$的短时期望。

##### 4.3.4.1 线性演化下的均值与协方差求解

主要内容：随机积分为零均值、与初值独立，故$\boldsymbol m_t&=\boldsymbol\Phi(t,0)\boldsymbol m_0+\int_0^t\boldsymbol\Phi(t,s)\boldsymbol c_s\,\mathrm ds,\\ \boldsymbol P_t&=\boldsymbol\Phi(t,0)\boldsymbol P_0\boldsymbol\Phi(t,0)^\top +\int_0^t\boldsymbol\Phi(t,s)\boldsymbol G_s\boldsymbol G_s^\top\boldsymbol\Phi(t,s)^\top\,\mathrm ds$这里积分中的$\boldsymbol G_s\boldsymbol G_s^\top$是确定性矩阵。

论证与表述逻辑：

1. OU过程的初值只需平方可积并独立于驱动，就有$\mathbb E X_t&=\mathrm e^{-\lambda t}\mathbb E X_0, \\ \operatorname{Var}(X_t)&=\mathrm e^{-2\lambda t}\operatorname{Var}(X_0) +\frac{\sigma^2}{2\lambda}(1-\mathrm e^{-2\lambda t})$均值衰减；当$\sigma\neq0$时，方差趋于严格正值。

##### 4.3.4.2 一般演化下的分布与密度求解

主要内容：设确定性系数与适当的解唯一性使$\boldsymbol X$成为Markov过程。要知道分布怎样变化，可先观察任意光滑“读数”$\varphi(\boldsymbol X_t)$的短时期望。

论证与表述逻辑：

1. 定义（Itô扩散的生成元）：记$\mathbb E_{t,\boldsymbol x}$为从时刻$t$的状态$\boldsymbol x$出发的期望。对属于算子定义域的测试函数，生成元定义为$(\mathcal L_t\varphi)(\boldsymbol x) =\lim_{h\downarrow0} \frac{\mathbb E_{t,\boldsymbol x}\varphi(\boldsymbol X_{t+h})-\varphi(\boldsymbol x)}h$对连续系数的扩散，令$\boldsymbol a=\boldsymbol\sigma\boldsymbol\sigma^\top$；在极限与期望可交换时，Itô公式给出$\mathcal L_t\varphi=\boldsymbol b^\top\nabla\varphi+ \tfrac12\operatorname{tr}(\boldsymbol a\nabla^2\varphi)$。
2. 从积分Itô公式取条件期望，除以$h$再令$h\downarrow0$，即得最后一式。例如取光滑紧支撑$\varphi$，并使系数在相关区域有界，可以先局部化来核对该极限。
3. 若终点分布已知或便于采样，可以从终点出发沿反方向生成路径。概率流ODE只匹配每个时刻的边缘密度；要恢复相邻时刻的随机反向条件规律，则需要时间反演的SDE。

#### 4.3.5 离散化条件下的轨迹求解

主要内容：已知轨迹存在唯一，不代表能写出解析式。记从$t_n$到$t_{n+1}=t_n+h$的精确流为$\varphi_{t_{n+1},t_n}$，数值方法以可计算的一步映射$\Psi_{h,t_n}$近似它。

论证与表述逻辑：

1. 基于一般数值离散的轨迹求解：显式Euler法在一步内使用当前斜率：$\widehat{\boldsymbol x}_{n+1} =\widehat{\boldsymbol x}_n+h\boldsymbol f(t_n,\widehat{\boldsymbol x}_n)$这里已把给定输入吸收进$\boldsymbol f$。
2. 基于精确线性离散的轨迹求解：前面的数值规则近似瞬时变化率，线性方程却允许在整段区间上求出精确转移。为使输入积分可算，假设$[t_n,t_n+h)$内$\boldsymbol u(t)=\boldsymbol u_n$。
3. 基于几何离散的保守轨迹求解：保守方程的数值计算除了接近状态，还要检查精确演化保持的几何关系。先沿Hamilton方程求出能量和体积的变化，再据此构造离散映射；保持某种结构不等于每一步都精确，也不自动保证任意步长稳定。
4. 基于随机离散的有限时域轨迹模拟：固定$T$，取$t_k=kh$、$n=T/h$为整数，初值$\widehat{\boldsymbol X}_0=\boldsymbol X_0$。

##### 4.3.5.1 基于一般数值离散的轨迹求解

主要内容：显式Euler法在一步内使用当前斜率：$\widehat{\boldsymbol x}_{n+1} =\widehat{\boldsymbol x}_n+h\boldsymbol f(t_n,\widehat{\boldsymbol x}_n)$这里已把给定输入吸收进$\boldsymbol f$。

论证与表述逻辑：

1. 示例（连续稳定与数值稳定不是一回事）：对$\dot x=-\lambda x+u$，其中$\lambda>0$且$u$恒定，精确一步为$x(t+h)=\mathrm e^{-\lambda h}x(t) +\frac{1-\mathrm e^{-\lambda h}}{\lambda}u$Euler一步为$\widehat x_{n+1}=(1-\lambda h)\widehat x_n+hu$。
2. 当$1<h\lambda<2$，数值状态交替变号但幅值缩小；当$h\lambda>2$，它交替增长。若同一系统包含衰减很快与变化很慢的方向，显式方法可能为压住快方向而被迫采用远小于慢变化尺度的步长，这就是刚性带来的主要计算困难。

##### 4.3.5.2 基于精确线性离散的轨迹求解

主要内容：前面的数值规则近似瞬时变化率，线性方程却允许在整段区间上求出精确转移。为使输入积分可算，假设$[t_n,t_n+h)$内$\boldsymbol u(t)=\boldsymbol u_n$。

论证与表述逻辑：

1. 为使输入积分可算，假设$[t_n,t_n+h)$内$\boldsymbol u(t)=\boldsymbol u_n$。
2. 精确性针对区间内保持不变的输入，不表示真实输入在区间内任意变化时也精确。
3. 输入保持误差与计算矩阵指数的数值误差仍可能存在，只是没有Euler式的时间截断误差。

##### 4.3.5.3 基于几何离散的保守轨迹求解

主要内容：保守方程的数值计算除了接近状态，还要检查精确演化保持的几何关系。先沿Hamilton方程求出能量和体积的变化，再据此构造离散映射；保持某种结构不等于每一步都精确，也不自动保证任意步长稳定。

论证与表述逻辑：

1. 精确演化的能量保持：若$H$连续可微、不显含时间，且Hamilton方程的解在所考察区间存在，则$H(\boldsymbol q(t),\boldsymbol p(t))=H(\boldsymbol q(0),\boldsymbol p(0))$。 因此轨迹被限制在初始能量面上，而不是向能量极小值下降。若$H$显含时间，同一计算只给出$\mathrm dH/\mathrm dt=\partial_tH$。
2. 精确演化的辛结构与体积保持：能量只给轨迹上的标量限制，仍未说明一小团相邻初态怎样变形。为比较方向之间的关系，取相空间坐标$\boldsymbol z=(\boldsymbol q^\top,\boldsymbol p^\top)^\top$及前述矩阵$\boldsymbol J$。 反向推断却不成立。在$(q_1,q_2,p_1,p_2)$坐标下，$\operatorname{diag}(2,1,1,1/2)$的行列式为$1$，但它把第一对位置动量的面积乘以$2$，第二对乘以$1/2$，不保持标准辛形式。
3. 离散演化的结构保持：对于可分Hamilton量，势能子系统保持位置、只改变动量；动能子系统保持动量、只改变位置。 所以可逆、辛、体积保持与数值稳定分别需要检查。将这类轨迹用于随机采样时，能量误差还需接受校正，不能把几何积分器直接当作精确采样器。

##### 4.3.5.4 基于随机离散的有限时域轨迹模拟

主要内容：固定$T$，取$t_k=kh$、$n=T/h$为整数，初值$\widehat{\boldsymbol X}_0=\boldsymbol X_0$。

论证与表述逻辑：

1. Poisson驱动须另生成$\Delta N_k\sim\operatorname{Pois}(\lambda h)$，并按驱动假设与Brownian增量独立。

### 4.4 演化与计算序列的收敛

主要内容：区分长时间行为、步长缩小、随机近似和双时间尺度的极限，分别检查状态、计算轨迹与时间平均的收敛。

论证与表述逻辑：

1. 长时间演化下的状态极限：考虑局部Lipschitz自治方程$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$。满足$\boldsymbol f(\boldsymbol x^\star)=\boldsymbol0$的状态称为平衡点。以下性质均要求所涉及初值的解对全部$t\geq0$存在。
2. 步长缩小下的轨迹逼近：固定真实方程、初值和有限时域，改变数值网格的步长$h$。确定性计算比较网格状态与精确轨迹；随机计算可以使用同一噪声比较状态，也可以只比较测试函数的期望。
3. 随机近似下的迭代序列收敛：有些递推状态不是房间温度，而是希望逐步求出的参数。设未知均值为$\mu$，目标是解平均方程$h(\theta)=\mathbb E[Y-\theta]=\mu-\theta=0$每次只能得到一个含噪观测，仍可沿观测建议的方向作小步移动。
4. 双时间尺度下的迭代序列收敛：一个参数可能负责快速跟踪另一个参数尚未解释的误差，另一个参数则慢慢改变目标。
5. 长时间采样下的分布与平均收敛：给定一张目标分布，可以设计演化规律，使长时间模拟产生用于积分的相关样本。需要检查两步：目标是否被演化保持，以及从实际初态出发能否接近它。

#### 4.4.1 长时间演化下的状态极限

主要内容：考虑局部Lipschitz自治方程$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$。满足$\boldsymbol f(\boldsymbol x^\star)=\boldsymbol0$的状态称为平衡点。以下性质均要求所涉及初值的解对全部$t\geq0$存在。

论证与表述逻辑：

1. 定义（平衡点与稳定性）：考虑局部Lipschitz自治方程$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$。满足$\boldsymbol f(\boldsymbol x^\star)=\boldsymbol0$的状态称为平衡点。以下性质均要求所涉及初值的解对全部$t\geq0$存在。平衡点在Lyapunov意义下稳定，是指对每个$\varepsilon>0$，存在$\delta>0$，使$\|\boldsymbol x(0)-\boldsymbol x^\star\|<\delta$蕴含$\|\boldsymbol x(t)-\boldsymbol x^\star\|<\varepsilon$对全部$t\geq0$成立。同时稳定且有局部吸引性称为渐近稳定。若存在$r,C,\alpha>0$，对上述$r$邻域内全部初值和$t\geq0$都有$\|\boldsymbol x(t)-\boldsymbol x^\star\|_2 \leq C\mathrm e^{-\alpha t}\|\boldsymbol x(0)-\boldsymbol x^\star\|_2,$则称为局部指数稳定。若同一估计对全部初值成立，则称为全局指数稳定。
2. 离散时间把$t\geq0$换成非负整数，平衡条件换成$F(\boldsymbol x^\star)=\boldsymbol x^\star$，指数因子可写成$q^t$，其中$0<q<1$。
3. 定义（Lyapunov函数）：对$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$，若上述正定候选还满足$\dot V(\boldsymbol x):=\nabla V(\boldsymbol x)^\top\boldsymbol f(\boldsymbol x)\leq0$，则称其为该邻域内的Lyapunov函数；若非零点处严格小于零，则称为严格Lyapunov函数。
4. 离散方程相应检查$V(F(\boldsymbol x))-V(\boldsymbol x)$。正定性使“小能量”确实限制所有状态方向，非增性才保证轨迹不能穿越更高的能量边界。

##### 4.4.1.1 平衡邻域内的状态极限

主要内容：对已经定义的平衡点，吸引性直接问邻域内的轨迹是否回到该点。温度模型的零输入偏差满足$e_{t+1}=0.8e_t$，因而$e_t=0.8^t e_0\to0$；连续模型$\dot e=-\lambda e$、$\lambda>0$则给出$e(t)=e^{-(t-t_0)\lambda}e(t_0)\to0$。

论证与表述逻辑：

1. 一般非线性方程未必有解析式。下降函数仅有非正导数时，还需检查轨迹是否能停留在较大的零导数集合中。

##### 4.4.1.2 不变区域内的极限集合

主要内容：机械能常只在某些方向上直接耗散，导致$\dot V=0$的集合远大于平衡点。这时应问：轨迹能否一直留在这个集合中？

论证与表述逻辑：

1. 命题（LaSalle不变性原理）：设自治向量场$\boldsymbol f$局部Lipschitz，$\Omega$紧且正向不变，$V$在包含$\Omega$的开邻域上为$C^1$，并有$\dot V\leq0$。令$E=\{\boldsymbol x\in\Omega:\dot V(\boldsymbol x)=0\}$，$M$为$E$中最大不变集，则从$\Omega$出发的每条轨迹满足$\operatorname{dist}(\boldsymbol x(t),M)\to0$。
2. 推导：紧性排除有限时间逃逸，也使$\omega(\boldsymbol x_0)$非空且紧。沿轨迹的$V$单调不增且有下界，故趋于$v_\infty$。对极限点$\boldsymbol z=\lim_j\boldsymbol x(t_j)$，连续性给出$V(\boldsymbol z)=v_\infty$。
3. 能量非增先限制活动区域，动力学再排除不能持续停留的零导数点。把整个$E$直接称为“最终状态”，会丢掉LaSalle论证中最关键的一步。

#### 4.4.2 步长缩小下的轨迹逼近

主要内容：固定真实方程、初值和有限时域，改变数值网格的步长$h$。确定性计算比较网格状态与精确轨迹；随机计算可以使用同一噪声比较状态，也可以只比较测试函数的期望。

论证与表述逻辑：

1. 确定性演化下的离散误差：设$\boldsymbol f$在包含精确轨迹与Euler轨迹的区域内关于状态具有Lipschitz常数$L$，精确解二阶连续可微，且$\|\ddot{\boldsymbol x}(t)\|_2\leq M$。从精确初值出发，若$t_n=t_0+nh\leq t_0+T$，则$L>0$时$\|\widehat{\boldsymbol x}_n-\boldsymbol x(t_n)\|_2 \leq\frac{Mh}{2L}(\mathrm e^{LT}-1)$$L=0$时相应上界为$MTh/2$。
2. 同一噪声下的随机轨迹误差：同一次噪声实现会产生一条真轨迹和一条数值轨迹。要比较两条路径的状态误差，网格算法必须使用真轨迹的同一驱动，即令$\sqrt h\,\boldsymbol\varepsilon_k=\boldsymbol W_{t_{k+1}}-\boldsymbol W_{t_k}$。
3. 测试函数下的随机模拟误差：若只查询终点读数的平均，目标变成测试函数$\varphi$在真终点和数值终点下的期望差，不必把两条路径逐次配对。

##### 4.4.2.1 确定性演化下的离散误差

主要内容：设$\boldsymbol f$在包含精确轨迹与Euler轨迹的区域内关于状态具有Lipschitz常数$L$，精确解二阶连续可微，且$\|\ddot{\boldsymbol x}(t)\|_2\leq M$。从精确初值出发，若$t_n=t_0+nh\leq t_0+T$，则$L>0$时$\|\widehat{\boldsymbol x}_n-\boldsymbol x(t_n)\|_2 \leq\frac{Mh}{2L}(\mathrm e^{LT}-1)$$L=0$时相应上界为$MTh/2$。

论证与表述逻辑：

1. 命题（Euler法的有限时域全局误差）：设$\boldsymbol f$在包含精确轨迹与Euler轨迹的区域内关于状态具有Lipschitz常数$L$，精确解二阶连续可微，且$\|\ddot{\boldsymbol x}(t)\|_2\leq M$。从精确初值出发，若$t_n=t_0+nh\leq t_0+T$，则$L>0$时$\|\widehat{\boldsymbol x}_n-\boldsymbol x(t_n)\|_2 \leq\frac{Mh}{2L}(\mathrm e^{LT}-1)$$L=0$时相应上界为$MTh/2$。
2. 推导：Taylor公式给出$\boldsymbol x(t_{n+1})=\boldsymbol x(t_n)+h\boldsymbol f(t_n,\boldsymbol x(t_n))+\boldsymbol\tau_n$，其中$\|\boldsymbol\tau_n\|_2\leq Mh^2/2$。记$\boldsymbol e_n=\widehat{\boldsymbol x}_n-\boldsymbol x(t_n)$，相减并用Lipschitz条件得$\|\boldsymbol e_{n+1}\|_2\leq(1+Lh)\|\boldsymbol e_n\|_2+Mh^2/2$从$\boldsymbol e_0=\boldsymbol0$展开，$\|\boldsymbol e_n\|_2\leq(Mh^2/2)\sum_{j=0}^{n-1}(1+Lh)^j$。$L>0$时求几何和，并用$(1+Lh)^n\leq\mathrm e^{Lnh}\leq\mathrm e^{LT}$，即得所述界；$L=0$时直接使用$nh\leq T$。
3. 这也是离散Grönwall估计的一个具体推导。局部$O(h^2)$经约$T/h$步累计成为全局$O(h)$，而动力学决定这些误差随后放大多少。

##### 4.4.2.2 同一噪声下的随机轨迹误差

主要内容：同一次噪声实现会产生一条真轨迹和一条数值轨迹。要比较两条路径的状态误差，网格算法必须使用真轨迹的同一驱动，即令$\sqrt h\,\boldsymbol\varepsilon_k=\boldsymbol W_{t_{k+1}}-\boldsymbol W_{t_k}$。

论证与表述逻辑：

1. 估计机制与存在性证明相连。

##### 4.4.2.3 测试函数下的随机模拟误差

主要内容：若只查询终点读数的平均，目标变成测试函数$\varphi$在真终点和数值终点下的期望差，不必把两条路径逐次配对。

论证与表述逻辑：

1. 弱阶较高不说明两条样本轨迹更接近。例如独立生成的两个同分布终点对所有可积测试函数期望完全相同，彼此状态距离却不为零。

#### 4.4.3 随机近似下的迭代序列收敛

主要内容：有些递推状态不是房间温度，而是希望逐步求出的参数。设未知均值为$\mu$，目标是解平均方程$h(\theta)=\mathbb E[Y-\theta]=\mu-\theta=0$每次只能得到一个含噪观测，仍可沿观测建议的方向作小步移动。

论证与表述逻辑：

1. 固定步长的均值例在递推前定义$e_t=\theta^{(t)}-\mu$和$v_t=\operatorname{Var}(e_t)$；确定初值与独立同分布噪声给出稳态方差$\alpha\sigma^2/(2-\alpha)$，说明减小步长降低波动也延缓响应。
2. 引理（固定有限链的加权Poisson分解）：设$P$为固定的有限不可约非周期核，参数递推$\theta^{(t+1)}=\theta^{(t)}+\alpha_tH(\theta^{(t)},Z_t)$始终位于紧集$K$，$H$在$K$上一致有界且关于参数一致Lipschitz。特别地，任意向晚期移动的有限算法时间窗上的尾和趋零。
3. 推导：有限不可约非周期链几何收敛，且$\pi q_\theta=0$，所以$g_\theta=\sum_{j=0}^\infty P^jq_\theta$绝对一致收敛，并满足$g_\theta-Pg_\theta=q_\theta$。对$q_\theta-q_{\theta'}$应用相同几何界，得到有限常数$G,L_g$使$|g_\theta(z)|\leq G$、$|g_\theta(z)-g_{\theta'}(z)|\leq L_g|\theta-\theta'|$。
4. 再用标量递推核对平均稳定与噪声条件怎样配合。设$\theta^{(t+1)}=\theta^{(t)}+\alpha_t[b-a\theta^{(t)}+\xi_{t+1}]$，$a>0$，噪声为条件均值零且条件二阶矩不超过$\sigma^2$，初值二阶矩有限。

#### 4.4.4 双时间尺度下的迭代序列收敛

主要内容：一个参数可能负责快速跟踪另一个参数尚未解释的误差，另一个参数则慢慢改变目标。

论证与表述逻辑：

1. 快时间上把$\boldsymbol v$暂时固定，得到$\dot{\boldsymbol u}=\boldsymbol g(\boldsymbol u,\boldsymbol v)$；若其稳定平衡为$\boldsymbol u^\star(\boldsymbol v)$，慢时间上再使用$\dot{\boldsymbol v}=\boldsymbol f(\boldsymbol u^\star(\boldsymbol v),\boldsymbol v)$。
2. 示例（分解同一个未知均值的快慢更新）：若$\mathbb E[Y_{t+1}\mid\mathcal F_t]=\mu$，取$u^{(t+1)}=u^{(t)}+\beta_t(Y_{t+1}-u^{(t)}-v^{(t)}),\qquad v^{(t+1)}=v^{(t)}+\alpha_t(u^{(t)}-v^{(t)})$冻结$v$后，快方程$\dot u=\mu-v-u$的唯一稳定平衡为$u^\star(v)=\mu-v$。
3. 尺度分离没有保证快平衡存在，也没有保证其稳定或全局最优。两组步长同阶时，前面的均值拆分例仍可用联合系统分析，却不能继续使用冻结慢变量的论证。

#### 4.4.5 长时间采样下的分布与平均收敛

主要内容：给定一张目标分布，可以设计演化规律，使长时间模拟产生用于积分的相关样本。需要检查两步：目标是否被演化保持，以及从实际初态出发能否接近它。

论证与表述逻辑：

1. 命题（HMC提议的细致平衡）：若$T$是可微、体积保持的对合，则以概率$\alpha(\boldsymbol z)$移至$T\boldsymbol z$，否则留在$\boldsymbol z$的核，对密度$\rho$满足细致平衡。
2. 推导：接受部分的密度权重为$\rho(\boldsymbol z)\alpha(\boldsymbol z)=\min\{\rho(\boldsymbol z),\rho(T\boldsymbol z)\}$。对任意有界可测函数$g(\boldsymbol z,\boldsymbol z')$，作变量替换$\boldsymbol y=T\boldsymbol z$，由$T^2=I$和单位绝对Jacobian，$\begin{split} &\int g(\boldsymbol z,T\boldsymbol z)\min\{\rho(\boldsymbol z),\rho(T\boldsymbol z)\}\,\mathrm d\boldsymbol z\\ &\quad=\int g(T\boldsymbol y,\boldsymbol y) \min\{\rho(T\boldsymbol y),\rho(\boldsymbol y)\}\,\mathrm d\boldsymbol y . \end{split}$这证明接受部分在交换出发与到达状态后不变。拒绝部分集中在对角线$\boldsymbol z'=\boldsymbol z$，本身对称，两者相加即为细致平衡。
3. 若提议不保持体积，接受比还需Jacobian因子；状态依赖地改变步数或步长，也须重新核对反向提议。实现中的有限精度可逆误差不是上述精确算术证明的一部分。

### 4.5 状态演化的扰动与稳定性

主要内容：比较初值与输入扰动下的轨迹，利用线性谱和Lyapunov方法区分有限时间控制、稳定与误差消退。

论证与表述逻辑：

1. 初值扰动下的轨迹稳定性：前述原点判据通常对应零输入，或把恒定输入下的平衡平移到原点。温度例的恒定$u_t=0.4$对应平衡$2$，误差$e_t=x_t-2$才满足$e_{t+1}=0.8e_t$。
2. 输入扰动下的轨迹稳定性：初值误差只在开始时注入，输入误差可以在每个时刻持续进入。即使无输入偏差会衰减，持续加热偏多仍可能造成非零温差。

#### 4.5.1 初值扰动下的轨迹稳定性

主要内容：前述原点判据通常对应零输入，或把恒定输入下的平衡平移到原点。温度例的恒定$u_t=0.4$对应平衡$2$，误差$e_t=x_t-2$才满足$e_{t+1}=0.8e_t$。

论证与表述逻辑：

1. 要得到衰减，须利用演化方向，而非只限制变化率；线性传播和Lyapunov下降关系分别提供这样的判据。

##### 4.5.1.1 线性演化下的轨迹稳定性

主要内容：离散齐次系统为$\boldsymbol x_{t+1}=\boldsymbol A\boldsymbol x_t,\qquad \boldsymbol x_t=\boldsymbol A^t\boldsymbol x_0$这里用矩阵幂和Jordan分解把长期轨迹问题化成谱的位置；下面对各Jordan块的幂逐项给出长期估计。

论证与表述逻辑：

1. 长期演化的谱判据：离散齐次系统为$\boldsymbol x_{t+1}=\boldsymbol A\boldsymbol x_t,\qquad \boldsymbol x_t=\boldsymbol A^t\boldsymbol x_0$这里用矩阵幂和Jordan分解把长期轨迹问题化成谱的位置；下面对各Jordan块的幂逐项给出长期估计。 命题（离散线性系统的渐近稳定性）：在此条件下，原点实际上全局指数稳定。
2. 有限时间的瞬态放大：取$\boldsymbol A=\begin{bmatrix}1/2&K\\0&1/2\end{bmatrix},\qquad K>0$无论$K$多大，谱半径均为$1/2$，而$\boldsymbol A^t= \begin{bmatrix} 2^{-t}&tK\,2^{-(t-1)}\\0&2^{-t} \end{bmatrix}$从$\boldsymbol x_0=(0,1)^\top$出发，第一步即为$(K,1/2)^\top$，欧氏范数可以大幅增长；之后$t2^{-t}\to0$才使状态趋零。 $K\neq0$时，$\boldsymbol A^\top\boldsymbol A\neq\boldsymbol A\boldsymbol A^\top$，矩阵非正规。
3. 同谱的非正规矩阵例显示有限时间放大与长期衰减可以并存；伪谱用同维复矩阵小扰动下所有可能特征值的位置解释，反映谱敏感性，不把谱稳定等同于欧氏范数逐步收缩。

##### 4.5.1.2 非线性演化下的轨迹稳定性

主要内容：非线性系统一般无法通过一个固定矩阵构造全局二次能量，因而需要寻找候选函数。

论证与表述逻辑：

1. 命题（连续时间Lyapunov判据）：设原点为$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$的平衡点，$\boldsymbol f$在其邻域内局部Lipschitz。若该邻域存在$C^1$正定候选$V$且$\dot V\leq0$，则原点稳定；若非零点上$\dot V<0$，则原点局部渐近稳定。若这些条件在$\mathbb R^d$上成立，且$V(\boldsymbol x)\to\infty$当$\|\boldsymbol x\|\to\infty$，则所有解正向全局存在；非增情形给出稳定性，严格下降情形给出全局渐近稳定性。
2. 推导：选足够小的$\varepsilon$使闭球位于适用邻域。球面上的连续正函数$V$有最小值$c_\varepsilon>0$。原点处连续性给出$\delta<\varepsilon$，使$\|\boldsymbol x_0\|<\delta$时$V(\boldsymbol x_0)<c_\varepsilon$。
3. 径向无界性控制的是远处状态，不能用“在原点附近正定”代替。若还能找到$c_1,c_2,c_3>0$使$c_1\|\boldsymbol x\|^2\leq V\leq c_2\|\boldsymbol x\|^2$、$\dot V\leq-c_3\|\boldsymbol x\|^2$，则前述线性方程证明中的积分估计同样给出局部指数衰减。

#### 4.5.2 输入扰动下的轨迹稳定性

主要内容：初值误差只在开始时注入，输入误差可以在每个时刻持续进入。即使无输入偏差会衰减，持续加热偏多仍可能造成非零温差。

论证与表述逻辑：

1. 线性演化下的轨迹响应：若$\|\boldsymbol u(s)\|\leq U$，第二项至多$(M\|\boldsymbol B\|U/\alpha)(1-\mathrm e^{-\alpha(t-t_0)})$。
2. 非线性演化下的轨迹响应：在初值连续依赖的基础上，再允许输入与向量场改变。设两条轨迹都留在同一区域，原向量场关于状态的Lipschitz常数为$L$，关于输入的常数为$L_u$；比较模型沿第二条轨迹的向量场误差至多为$r(s)$。

##### 4.5.2.1 线性演化下的轨迹响应

主要内容：在指数稳定线性演化中，由初值与输入的卷积表达控制状态及两条轨迹的差异，区分暂态消退与持续偏差。

论证与表述逻辑：

1. 先用矩阵指数的衰减界代入常数变易公式，分别估计初值项和输入累计项。
2. 再利用两组解之差仍满足同一线性方程，得到扰动响应；有界持续输入可留下非零稳态，温度模型给出固定输入偏差被放大的具体倍数。

##### 4.5.2.2 非线性演化下的轨迹响应

主要内容：在初值连续依赖的基础上，再允许输入与向量场改变。设两条轨迹都留在同一区域，原向量场关于状态的Lipschitz常数为$L$，关于输入的常数为$L_u$；比较模型沿第二条轨迹的向量场误差至多为$r(s)$。

论证与表述逻辑：

1. 设两条轨迹都留在同一区域，原向量场关于状态的Lipschitz常数为$L$，关于输入的常数为$L_u$；比较模型沿第二条轨迹的向量场误差至多为$r(s)$。
2. Gronwall引理将初值误差、持续输入误差和模型误差合在同一传播界中：$\|\boldsymbol x(t)-\widetilde{\boldsymbol x}(t)\| \leq \mathrm e^{L(t-t_0)}\|\boldsymbol x_0-\widetilde{\boldsymbol x}_0\| +\int_{t_0}^t\mathrm e^{L(t-s)} \bigl(L_u\|\boldsymbol u(s)-\widetilde{\boldsymbol u}(s)\|+r(s)\bigr)\,\mathrm ds$初态误差、输入误差、模型误差因此有不同来源，却都要经过后续动态传播。

### 4.6 基于观测的状态推断

主要内容：给定生成和观测模型后，分别建立预测、滤波、平滑与整条轨迹推断，说明各自允许使用的信息。

论证与表述逻辑：

1. 观测条件下的推断目标：在前面的状态转移$K_t$之外增加观测核$G_t(\boldsymbol x,B)=\mathbb P(\boldsymbol y_t\in B\mid\boldsymbol x_t=\boldsymbol x)$。
2. 基于历史观测的状态预测：若已有截至$t-1$的条件分布$\pi_{t-1}$，全概率公式给出$\pi_{t\mid t-1}(A) =\int K_{t-1}(\boldsymbol x,A)\,\pi_{t-1}(\mathrm d\boldsymbol x)$这是把每个候选旧状态的下一步分布，按其当前可信程度混合。
3. 基于当前及历史观测的状态滤波：预测分布已经汇总旧读数对当前状态的判断。获得当前读数后，各候选状态的权重还要按它们产生这次读数的可能性调整；所求对象仍是同一个物理状态，只是条件信息增加了。
4. 基于完整观测的状态平滑：固定终点$T$后，未来读数也能帮助判断旧状态。关键不是再向前预测，而是把新获得的下一状态分布通过反向条件关系传回去。
5. 基于完整观测的联合轨迹推断：各时刻边缘分布回答“那一刻可能在哪里”，整条路径后验还要回答“这些状态如何一起出现”。

#### 4.6.1 观测条件下的推断目标

主要内容：在前面的状态转移$K_t$之外增加观测核$G_t(\boldsymbol x,B)=\mathbb P(\boldsymbol y_t\in B\mid\boldsymbol x_t=\boldsymbol x)$。

论证与表述逻辑：

1. 记$\mathcal Y_t=\sigma(\boldsymbol y_1,\ldots,\boldsymbol y_t)$，$\mathcal Y_0$为无观测信息。
2. 下面的一般核公式只要求前述条件独立结构。

#### 4.6.2 基于历史观测的状态预测

主要内容：若已有截至$t-1$的条件分布$\pi_{t-1}$，全概率公式给出$\pi_{t\mid t-1}(A) =\int K_{t-1}(\boldsymbol x,A)\,\pi_{t-1}(\mathrm d\boldsymbol x)$这是把每个候选旧状态的下一步分布，按其当前可信程度混合。

论证与表述逻辑：

1. 例如隐藏状态为$\{0,1\}$，$\pi_0=(0.7,0.3)$，按当前状态为行、下一状态为列的转移矩阵为$\boldsymbol P=\left[\begin{smallmatrix}0.8&0.2\\0.1&0.9\end{smallmatrix}\right]$。
2. 在线性高斯条件下，仿射变换与独立高斯相加保持高斯性，所以$\boldsymbol m_{t\mid t-1} &=\boldsymbol A_{t-1}\boldsymbol m_{t-1\mid t-1}+\boldsymbol B_{t-1}\boldsymbol u_{t-1}, \\ \boldsymbol P_{t\mid t-1} &=\boldsymbol A_{t-1}\boldsymbol P_{t-1\mid t-1}\boldsymbol A_{t-1}^\top+\boldsymbol Q_t$温度第一步为$m_{1\mid0}=0.4,P_{1\mid0}=0.04$：初值已知并不等于未来状态已知。

#### 4.6.3 基于当前及历史观测的状态滤波

主要内容：预测分布已经汇总旧读数对当前状态的判断。获得当前读数后，各候选状态的权重还要按它们产生这次读数的可能性调整；所求对象仍是同一个物理状态，只是条件信息增加了。

论证与表述逻辑：

1. 命题（有限时域Kalman滤波）：在上述独立线性高斯模型与创新协方差可逆条件下，预测与校正公式精确给出$\boldsymbol x_t\mid\mathcal Y_t\sim \mathcal N(\boldsymbol m_{t\mid t},\boldsymbol P_{t\mid t})$，对每个有限$t$成立。
2. 推导：$t=0$时无观测，条件分布就是给定高斯初值。为核对条件化，令$\boldsymbol e=\boldsymbol x_t-\boldsymbol m_{t\mid t-1}-\boldsymbol K_t\boldsymbol r_t$。在$\mathcal Y_{t-1}$条件下，$\operatorname{Cov}(\boldsymbol e,\boldsymbol r_t) =\boldsymbol P_{t\mid t-1}\boldsymbol C_t^\top-\boldsymbol K_t\boldsymbol S_t=\boldsymbol0$。
3. 两种方法都可能遗漏多峰后验。例如零均值对称先验配上$y=x^2+v$，一个明显正的读数可能支持正负两个状态区间。

#### 4.6.4 基于完整观测的状态平滑

主要内容：固定终点$T$后，未来读数也能帮助判断旧状态。关键不是再向前预测，而是把新获得的下一状态分布通过反向条件关系传回去。

论证与表述逻辑：

1. 命题（有限时域RTS平滑）：在有限时域Kalman条件及每个$\boldsymbol P_{t+1\mid t}$可逆条件下，从终点$(\boldsymbol m_{T\mid T},\boldsymbol P_{T\mid T})$向后递推$\boldsymbol m_{t\mid T} &=\boldsymbol m_{t\mid t}+\boldsymbol J_t(\boldsymbol m_{t+1\mid T}-\boldsymbol m_{t+1\mid t}), \\ \boldsymbol P_{t\mid T} &=\boldsymbol P_{t\mid t} +\boldsymbol J_t(\boldsymbol P_{t+1\mid T}-\boldsymbol P_{t+1\mid t})\boldsymbol J_t^\top,$精确给出$\boldsymbol x_t\mid\mathcal Y_T$的高斯均值与协方差。
2. 推导：给定$\boldsymbol x_{t+1}$后，未来状态和观测与更早状态条件独立，因此$P(\mathrm d\boldsymbol x_t\mid\boldsymbol x_{t+1},\mathcal Y_T) =P(\mathrm d\boldsymbol x_t\mid\boldsymbol x_{t+1},\mathcal Y_t)$。全概率公式给出后向因子化$P(\mathrm d\boldsymbol x_t\mid\mathcal Y_T) =\int P(\mathrm d\boldsymbol x_t\mid\boldsymbol x_{t+1},\mathcal Y_t) P(\mathrm d\boldsymbol x_{t+1}\mid\mathcal Y_T)$将一步条件均值对$\boldsymbol x_{t+1}\mid\mathcal Y_T$取期望，塔式性质得到平滑均值公式。全协方差公式分成两项：条件内协方差为$\boldsymbol P_{t\mid t}-\boldsymbol J_t\boldsymbol P_{t+1\mid t}\boldsymbol J_t^\top$，条件均值的协方差为$\boldsymbol J_t\boldsymbol P_{t+1\mid T}\boldsymbol J_t^\top$；相加即得平滑协方差。
3. 沿用上述有限时域线性高斯条件，有$\boldsymbol P_{t\mid T}\preceq\boldsymbol P_{t\mid t}$，即滤波协方差减去平滑协方差是半正定矩阵。

#### 4.6.5 基于完整观测的联合轨迹推断

主要内容：各时刻边缘分布回答“那一刻可能在哪里”，整条路径后验还要回答“这些状态如何一起出现”。

论证与表述逻辑：

1. 若损失为$\sum_t\|\boldsymbol x_t-\boldsymbol a_t\|^2$，联合条件均值的各分量就是$\boldsymbol m_{t\mid T}$，因此逐时刻平滑均值同时组成最小化该可加平方损失的路径输出。
2. 本节的精确结论都在有限时域成立。在那里输入才由反馈主动选择，本章一直把$\boldsymbol u_t$当作已给定量。

### 4.7 本章小结

主要内容：用温度模型区分演化规律、过程噪声、真实轨迹与观测噪声，归纳求解、收敛、稳定和推断的职责。

论证与表述逻辑：

1. 同一温度模型中的演化规律、真实轨迹与传感器读数承担不同职责。初值和输入给出一次初值问题；过程噪声使轨迹成为随机对象；观测噪声产生用于推断的记录。
2. 给定规律以后，求解轨迹与求解分布也有不同输出。线性传播把各时刻输入的作用累计为和或积分，仿射复合允许并行扫描。
3. 本章把行动序列视为已经给定。演化模型和状态推断为这些任务提供条件，单靠轨迹求解仍不能决定怎样行动最合适。

## 第5章 策略的实现与轨迹控制

正文：[02-policy-realization-and-control.tex](../../tex/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/02-policy-realization-and-control.tex)。

### 5.1 策略的实现与可达轨迹

主要内容：在行动与观测受限的系统中比较开环和反馈策略，建立目标可达、可控与状态可区分的结构条件。

论证与表述逻辑：

1. 开环策略与反馈策略：考虑离散时间线性时不变系统$\begin{aligned} \boldsymbol{x}_{t+1}&=\boldsymbol{A}\boldsymbol{x}_t+\boldsymbol{B}\boldsymbol{u}_t,\\ \boldsymbol{y}_t&=\boldsymbol{C}\boldsymbol{x}_t, \end{aligned}$其中$\boldsymbol{x}_t\in\mathbb R^n$、$\boldsymbol{u}_t\in\mathbb R^m$和$\boldsymbol{y}_t\in\mathbb R^p$分别是状态、输入和输出；$\boldsymbol A,\boldsymbol B,\boldsymbol C$的维度依次为$n\times n,n\times m,p\times n$。
2. 目标状态的可达与可控：要判断一个终态能否由动作实现，可以把前$N$次输入对终态的贡献集中写出。
3. 观测条件下的状态可区分性：同一动作序列可能从不同初态产生不同读数。要检查读数是否足以区分初态，先从观测中扣除已知动作的贡献，留下只由初态产生的自由响应。

#### 5.1.1 开环策略与反馈策略

主要内容：考虑离散时间线性时不变系统$\begin{aligned} \boldsymbol{x}_{t+1}&=\boldsymbol{A}\boldsymbol{x}_t+\boldsymbol{B}\boldsymbol{u}_t,\\ \boldsymbol{y}_t&=\boldsymbol{C}\boldsymbol{x}_t, \end{aligned}$其中$\boldsymbol{x}_t\in\mathbb R^n$、$\boldsymbol{u}_t\in\mathbb R^m$和$\boldsymbol{y}_t\in\mathbb R^p$分别是状态、输入和输出；$\boldsymbol A,\boldsymbol B,\boldsymbol C$的维度依次为$n\times n,n\times m,p\times n$。

论证与表述逻辑：

1. 定义（开环控制与反馈控制）：若输入序列$\boldsymbol u_0,\boldsymbol u_1,\ldots$事先指定，不根据运行中实际出现的状态修正，称为开环控制（open-loop control）。状态可直接取得时，规则$\boldsymbol u_t=\kappa_t(\boldsymbol x_t)$称为状态反馈（state feedback）。仅有观测和已执行动作可用时，规则$\boldsymbol u_t=\mu_t(\boldsymbol y_0,\ldots,\boldsymbol y_t;\boldsymbol u_0,\ldots,\boldsymbol u_{t-1})$称为输出反馈（output feedback），初始控制历史按空序列处理。随机系统中，动作必须对这些允许信息可测，不能使用尚未产生的噪声。
2. 在温度例中，始终取$u_t=0.4$是一条开环策略；若直接测得状态，则可以根据$x_t-2$修正输入。若只有带噪声的$y_t$，把$x_t$写进控制公式并不会使真实状态变得可用，必须说明怎样从读数构造估计。
3. 把反馈代回状态方程后，需要确认给定初态与外部输入后，闭环轨迹存在、唯一，并覆盖任务所需时域；随机情形还要固定噪声实现。

#### 5.1.2 目标状态的可达与可控

主要内容：要判断一个终态能否由动作实现，可以把前$N$次输入对终态的贡献集中写出。

论证与表述逻辑：

1. 区分任意初态到零与任意初态到任意终态：A可逆是零可控推出可控的充分条件，A=B=0说明一般逆推失败，A=0、B=1说明可逆性并非具体系统可控的必要条件。
2. 命题（Popov--Belevitch--Hautus（PBH）可控性判据）：矩阵对$(\boldsymbol A,\boldsymbol B)$可控，当且仅当对每个复特征值$\lambda\in\sigma(\boldsymbol A)$，$\operatorname{rank}[\lambda\boldsymbol I-\boldsymbol A\ \boldsymbol B]=n$等价地，不存在非零左特征向量$\boldsymbol q^\ast$同时满足$\boldsymbol q^\ast\boldsymbol A=\lambda\boldsymbol q^\ast$和$\boldsymbol q^\ast\boldsymbol B=\boldsymbol0$。
3. 推导：若存在这样的向量，则$\boldsymbol q^\ast\boldsymbol A^k\boldsymbol B=\lambda^k\boldsymbol q^\ast\boldsymbol B=\boldsymbol0$对所有$k\geq0$成立，所以可控性矩阵不可能满行秩。反之，其列空间$\boldsymbol R_{\mathrm{reach}}$若不满维，便是一个真$\boldsymbol A$不变子空间。正交补$\boldsymbol R_{\mathrm{reach}}^{\perp}$在$\boldsymbol A^\ast$下不变。
4. 终点可控仍不保证任意指定的中间状态都能实现。给定整条参考$\boldsymbol r_t$，离散系统要求每一步$\boldsymbol r_{t+1}-\boldsymbol A\boldsymbol r_t\in\operatorname{col}(\boldsymbol B)$，并且解出的输入位于允许集合；连续系统则要求参考绝对连续且$\dot{\boldsymbol r}_t-\boldsymbol A\boldsymbol r_t=\boldsymbol B\boldsymbol u_t^r$几乎处处成立。

#### 5.1.3 观测条件下的状态可区分性

主要内容：同一动作序列可能从不同初态产生不同读数。要检查读数是否足以区分初态，先从观测中扣除已知动作的贡献，留下只由初态产生的自由响应。

论证与表述逻辑：

1. 定义（可观测性）：若同一已知输入下的输出序列能够区分任意两个不同初态，称$(\boldsymbol C,\boldsymbol A)$可观测（observable）。对上述线性时不变系统，这等价于$\mathcal O(\boldsymbol C,\boldsymbol A)$满列秩。
2. 反之，若秩不足，存在$\boldsymbol v\neq\boldsymbol0$满足$\mathcal O\boldsymbol v=\boldsymbol0$，初态$\boldsymbol x_0$与$\boldsymbol x_0+\boldsymbol v$的前$n$次输出便相同。
3. 温度模型的$C=1$使无噪声当前读数就能区分状态。有噪声时，同一个读数可能来自多个状态，结构可观测性并不提供单次误差上界。

### 5.2 策略的轨迹收敛与稳定

主要内容：从可稳定、可检测条件进入状态反馈、二次反馈与输出反馈，检查闭环误差的长期行为。

论证与表述逻辑：

1. 不可控与不可观测模式的稳定条件：反馈$\boldsymbol u=-\boldsymbol K\boldsymbol x$把状态矩阵改为$\boldsymbol A-\boldsymbol B\boldsymbol K$。
2. 状态反馈下的闭环稳定：可稳定性保证某个增益能够稳定系统；实际设计仍要给出增益，并检验相应闭环。
3. 二次反馈下的稳定化解：稳定增益通常不唯一：较快纠偏可能需要更大的动作。若用二次型分别计量状态偏差与动作幅值，就能把这种选择写成明确的成本最小化问题。
4. 输出反馈下的估计与闭环稳定：反馈需要状态，但传感器可能只提供状态的一部分。可以先根据模型和已执行动作预测状态，再利用当前读数与预测读数的差纠正估计。

#### 5.2.1 不可控与不可观测模式的稳定条件

主要内容：反馈$\boldsymbol u=-\boldsymbol K\boldsymbol x$把状态矩阵改为$\boldsymbol A-\boldsymbol B\boldsymbol K$。

论证与表述逻辑：

1. 令$\boldsymbol R_{\mathrm{reach}}$为可控性矩阵的列空间，选取以其一组基为前若干列的可逆矩阵$\boldsymbol T$。
2. 定义（可检测性）：若存在$\boldsymbol L$使$\boldsymbol A-\boldsymbol L\boldsymbol C$稳定，称$(\boldsymbol C,\boldsymbol A)$可检测（detectable）。
3. $\boldsymbol C=(1,0)$看得见$1.2$模式，看不见但无需纠正$0.5$模式，所以不可观测却可检测。

#### 5.2.2 状态反馈下的闭环稳定

主要内容：可稳定性保证某个增益能够稳定系统；实际设计仍要给出增益，并检验相应闭环。取线性状态反馈后，动作与状态递推为$\boldsymbol u_t=-\boldsymbol K\boldsymbol x_t, \qquad \boldsymbol x_{t+1}=(\boldsymbol A-\boldsymbol B\boldsymbol K)\boldsymbol x_t$负号只是增益约定。

论证与表述逻辑：

1. 非线性系统在不同状态处具有不同的变化方向，固定矩阵的谱一般不足以判断整个区域。可以改用一个随状态变化的标量$V$衡量偏离，再要求所选动作使它沿轨迹下降。
2. 定义（控制Lyapunov函数接口）：考虑$\dot{\boldsymbol x}_t=\boldsymbol f(\boldsymbol x_t)+\boldsymbol G(\boldsymbol x_t)\boldsymbol u_t$，目标为原点，输入属于$U$。若某邻域内的$C^1$函数$V$满足$V(\boldsymbol0)=0$、$V(\boldsymbol x)>0$（$\boldsymbol x\neq\boldsymbol0$），且有正定连续函数$W$使$\text{对每个 }\boldsymbol x\neq\boldsymbol0\text{，存在 }\boldsymbol u\in U\text{ 使} \quad\nabla V(\boldsymbol x)^\top(\boldsymbol f(\boldsymbol x)+\boldsymbol G(\boldsymbol x)\boldsymbol u) \leq-W(\boldsymbol x),$称$V$提供一个控制Lyapunov函数（control Lyapunov function, CLF）条件：每个非零状态至少应能选择一个使偏离量严格下降的动作。
3. 点态存在动作不等于已经构造出适定反馈。若进一步有$c_1\|\boldsymbol x\|_2^2\leq V\leq c_2\|\boldsymbol x\|_2^2$和$W\geq c_3\|\boldsymbol x\|_2^2$，便有$V_t\leq e^{-c_3t/c_2}V_0$；全局结论还需全域条件与解的延拓。

#### 5.2.3 二次反馈下的稳定化解

主要内容：稳定增益通常不唯一：较快纠偏可能需要更大的动作。若用二次型分别计量状态偏差与动作幅值，就能把这种选择写成明确的成本最小化问题。

论证与表述逻辑：

1. 在有限时域期望二次成本之前说明风险中性：确定成本10与等概率成本0或20打平。评价只看期望，并非否认波动；随后用终端价值反向配方得到Riccati递推，再说明无限时域稳定化所需条件。
2. 命题（无限时域LQR的稳定化解）：设$\boldsymbol Q\succeq\boldsymbol0$、$\boldsymbol R\succ\boldsymbol0$，$(\boldsymbol A,\boldsymbol B)$可稳定且$(\boldsymbol Q^{1/2},\boldsymbol A)$可检测。相应反馈使闭环渐近稳定，并在所有允许控制序列中给出无折扣二次总成本的最优值$V(\boldsymbol x)=\boldsymbol x^\top\boldsymbol P\boldsymbol x$。
3. 推导：取长度$N$、终端代价为零的有限问题，记其初始价值矩阵为$\boldsymbol P^{(N)}$。增加一个非负阶段成本不能降低最优成本，故$\boldsymbol0\preceq\boldsymbol P^{(N)}\preceq\boldsymbol P^{(N+1)}$。可稳定性提供$\overline{\boldsymbol K}$使$\overline{\boldsymbol F}=\boldsymbol A-\boldsymbol B\overline{\boldsymbol K}$稳定。
4. 连续时间也可以直接用代数方程构造稳定反馈，无须先推导有限时域价值。

#### 5.2.4 输出反馈下的估计与闭环稳定

主要内容：反馈需要状态，但传感器可能只提供状态的一部分。可以先根据模型和已执行动作预测状态，再利用当前读数与预测读数的差纠正估计。

论证与表述逻辑：

1. 命题（稳态预测滤波的充分条件）：从任意有限$\boldsymbol\Pi_0\succeq\boldsymbol0$出发的预测协方差递推收敛到$\boldsymbol\Pi$，稳态$\boldsymbol L=\boldsymbol A\boldsymbol M$使$\boldsymbol A-\boldsymbol L\boldsymbol C$稳定。
2. 推导：对偶代换把本定理的两个结构条件分别变为无限LQR定理的可稳定、可检测条件，故解的存在、唯一与稳定性成立。为说明一般初始协方差的收敛，记滤波Riccati映射为$\Phi$。固定任意合并增益$\boldsymbol L$，定义$\Psi_{\boldsymbol L}(\boldsymbol X) =(\boldsymbol A-\boldsymbol L\boldsymbol C)\boldsymbol X(\boldsymbol A-\boldsymbol L\boldsymbol C)^\top+ \boldsymbol\Sigma_{\mathrm w}+\boldsymbol L\boldsymbol\Sigma_{\mathrm v}\boldsymbol L^\top$配方表明$\Phi(\boldsymbol X)\preceq\Psi_{\boldsymbol L}(\boldsymbol X)$，等号在对应Kalman增益处成立。
3. 实际控制可使用当前观测更新后的$\widehat{\boldsymbol x}_{t|t}$。

### 5.3 策略的调节与跟踪

主要内容：将固定设定值与运动参考转成误差系统，先检查参考可实现性，再讨论反馈和扰动下的调节跟踪。

论证与表述逻辑：

1. 先求出维持目标状态或参考轨迹所需的输入，避免误差方程保留未处理的漂移。
2. 随后用闭环误差分析分别讨论固定调节与运动跟踪，并检查持续扰动和模型误差。

#### 5.3.1 固定目标下的轨迹调节

主要内容：先求维持固定设定值的平衡状态与输入，再设计误差反馈，并检查持续扰动下的调节。

论证与表述逻辑：

1. 确认目标可实现后，以实际状态减去目标建立误差系统，避免漏掉维持目标的前馈输入。
2. 利用闭环稳定讨论偏差消退，再分析持续扰动和补偿机制对稳态误差的影响。

##### 5.3.1.1 目标平衡与可行输入

主要内容：设定值（setpoint）是希望状态或输出最终保持的常数。调节（regulation）要求偏离该常数的误差趋于零；它不只要求在某一时刻经过目标。

论证与表述逻辑：

1. 定义（目标平衡与调节误差）：对$\boldsymbol x_{t+1}=\boldsymbol A\boldsymbol x_t+\boldsymbol B\boldsymbol u_t$，状态设定值$\boldsymbol r$与常值输入$\boldsymbol u^r$构成目标平衡，若$(\boldsymbol I-\boldsymbol A)\boldsymbol r=\boldsymbol B\boldsymbol u^r$状态调节误差定义为$\boldsymbol e_t=\boldsymbol x_t-\boldsymbol r$。若只指定输出设定值$\boldsymbol q$，还需寻找平衡状态$\boldsymbol r$使$\boldsymbol C\boldsymbol r=\boldsymbol q$，输出误差为$\boldsymbol e_t^y=\boldsymbol C\boldsymbol x_t-\boldsymbol q$。有输入、状态限制时，目标平衡还须满足$\boldsymbol u^r\in U,\boldsymbol r\in S$。
2. 对只指定输出的任务，可解联立方程$\begin{bmatrix}\boldsymbol I-\boldsymbol A&-\boldsymbol B\\\boldsymbol C&\boldsymbol0\end{bmatrix} \begin{bmatrix}\boldsymbol r\\\boldsymbol u^r\end{bmatrix} =\begin{bmatrix}\boldsymbol0\\\boldsymbol q\end{bmatrix}$方程可能无解或有多个解；输出达到设定值也不自动要求所有内部状态相同。
3. 示例（非零温度需要维持输入）：在无噪声温度模型中，设定值$r=2$要求$2=0.8\times2+u^r$，所以$u^r=0.4$。若直接使用$u_t=-0.3(x_t-2)$，在$x_t=2$处输入变成零，下一步温差便降为$1.6$，因而$2$不是闭环平衡。

##### 5.3.1.2 基于误差反馈的轨迹调节

主要内容：目标平衡方程给出了在目标处仍需持续施加的输入。在这个输入上叠加误差反馈，才使控制器在目标处停止纠偏而继续维持平衡：$\boldsymbol u_t=\boldsymbol u^r-\boldsymbol K(\boldsymbol x_t-\boldsymbol r), \qquad \boldsymbol e_{t+1}=(\boldsymbol A-\boldsymbol B\boldsymbol K)\boldsymbol e_t$第二式由原动态减去平衡方程得到。

论证与表述逻辑：

1. 温度反馈的完整计算为$u_t=0.4-0.3(x_t-2), \qquad e_{t+1}=0.5e_t,\quad e_t=0.5^t(x_0-2)$从$x_0=0$出发，状态依次为$0,1,1.5,1.75,\ldots$，输入依次为$1,0.7,0.55,0.475,\ldots$。
2. 若改用估计状态$\widehat{\boldsymbol x}_t$，令$\boldsymbol e_t^{\mathrm o}=\boldsymbol x_t-\widehat{\boldsymbol x}_t$，则调节误差成为$\boldsymbol e_{t+1}=(\boldsymbol A-\boldsymbol B\boldsymbol K)\boldsymbol e_t+\boldsymbol B\boldsymbol K\boldsymbol e_t^{\mathrm o}$。

##### 5.3.1.3 持续扰动下的轨迹调节

主要内容：平衡输入按名义模型计算。

论证与表述逻辑：

1. 积分器自身带有特征值$1$，不能不经核验就加到控制器上。设计增益前应检查增广对$\left( \begin{bmatrix}\boldsymbol A&\boldsymbol0\\\boldsymbol C&\boldsymbol I\end{bmatrix}, \begin{bmatrix}\boldsymbol B\\\boldsymbol0\end{bmatrix}\right)$可稳定。
2. 输入饱和后，真实误差不再服从上述线性增广方程，积分状态却可能继续累积，造成解除饱和后的大幅动作。限制或回退积分累积是常见的抗积分饱和处理，但处理后的闭环仍需重新验证。

#### 5.3.2 运动参考下的轨迹跟踪

主要内容：先检查参考运动是否符合系统动力学，再结合前馈与反馈控制跟踪误差。

论证与表述逻辑：

1. 给定参考轨迹及其变化，求出可实现它的参考输入。
2. 把实际与参考之差写成误差动态，再检查扰动与模型偏差下能够维持何种跟踪精度。

##### 5.3.2.1 参考轨迹与可实现条件

主要内容：跟踪（tracking）以随时间变化的状态$\boldsymbol r_t$或输出$\boldsymbol q_t$为目标，要求$\boldsymbol x_t-\boldsymbol r_t$或$\boldsymbol C\boldsymbol x_t-\boldsymbol q_t$趋零或保持在规定范围内。

论证与表述逻辑：

1. 定义（可实现参考）：离散线性系统的参考状态、参考输入为$(\boldsymbol r_t,\boldsymbol u_t^r)$。若每一步满足$\boldsymbol r_{t+1}=\boldsymbol A\boldsymbol r_t+\boldsymbol B\boldsymbol u_t^r, \qquad \boldsymbol q_t=\boldsymbol C\boldsymbol r_t,$且参考状态、输入满足所声明的约束，称它为可实现参考。精确从首时刻跟踪还要求$\boldsymbol x_0=\boldsymbol r_0$。连续时间则要求$\boldsymbol r_t$绝对连续，并有$\dot{\boldsymbol r}_t=\boldsymbol A\boldsymbol r_t+\boldsymbol B\boldsymbol u_t^r$几乎处处成立。
2. 若只给输出曲线，需要先找与其一致的内部状态和输入；不同实现可能具有不同内部行为。有输入变化率、采样周期或执行器动态限制时，也必须把这些约束加入可实现性检查。
3. 温度参考的前馈输入由系统方程直接给出：$u_t^r=r_{t+1}-0.8r_t$前馈（feedforward）是由已知目标运动与模型预先计算的动作，不靠当前误差产生。

##### 5.3.2.2 基于前馈与反馈的轨迹跟踪

主要内容：前馈按参考轨迹计算，没有使用实际偏差；从错误初态出发时，它不会额外纠偏。

论证与表述逻辑：

1. 温度例使用$u_t=r_{t+1}-0.8r_t-0.3(x_t-r_t)$，得到$e_{t+1}=0.5e_t$。
2. 误差趋零、误差有界与始终不超过某阈值仍有区别。无扰动时，$|e_t|=0.5^t|e_0|$既给出收敛，也给出从首步起的范围；一般多维稳定矩阵可能先放大误差，需要使用$M\rho^t$而不能省掉$M$。

##### 5.3.2.3 扰动与模型偏差下的轨迹跟踪

主要内容：真实动态与参考规划常有偏差。

论证与表述逻辑：

1. 真实动态与参考规划常有偏差。设实际系统为$\boldsymbol x_{t+1}=(\boldsymbol A+\Delta\boldsymbol A)\boldsymbol x_t+ (\boldsymbol B+\Delta\boldsymbol B)\boldsymbol u_t+\boldsymbol d_t$，名义参考的实现残差为$\boldsymbol\eta_t=\boldsymbol A\boldsymbol r_t+\boldsymbol B\boldsymbol u_t^r-\boldsymbol r_{t+1}$。
2. 固定一种向量范数及相容矩阵范数，假设$\|\boldsymbol F\|\leq\rho<1$，$\|\Delta\boldsymbol A-\Delta\boldsymbol B\boldsymbol K\|\leq\varepsilon$且$q:=\rho+\varepsilon<1$。
3. 在精确温度模型中，若$|d_t|\leq0.1$，则$|e_t|\leq0.5^t|e_0|+0.2(1-0.5^t)$。
4. 如果安全控制器把名义动作改为$\boldsymbol u_t=\boldsymbol u_t^r-\boldsymbol K\boldsymbol e_t+\Delta\boldsymbol u_t^{\mathrm s}$，精确模型的误差方程还多出$\boldsymbol B\Delta\boldsymbol u_t^{\mathrm s}$。

### 5.4 策略的约束与安全

主要内容：以安全区域和一步可行动作为基础，讨论反馈修正，以及扰动和离散执行下逐轨迹安全保证的条件。

论证与表述逻辑：

1. 状态约束下的安全区域：一个制动系统最终停下，仍可能在停下之前越过位置边界；平均成本很小的随机系统，也可能有不可接受的少数路径。安全集合（safe set）直接规定允许出现的状态。
2. 安全条件下的可行动作：函数$h$只用符号区分安全与否，不必等于几何距离。
3. 可行约束下的反馈修正：调节或跟踪已经提出名义动作$\boldsymbol u_{\mathrm{nom}}$，但该动作可能违反安全条件。
4. 扰动与离散执行下的安全保证：名义屏障条件只计算模型给出的变化率。真实连续动态多出加性扰动时，安全函数的导数还多出$\nabla h(\boldsymbol x)^\top\boldsymbol d_t$。

#### 5.4.1 状态约束下的安全区域

主要内容：一个制动系统最终停下，仍可能在停下之前越过位置边界；平均成本很小的随机系统，也可能有不可接受的少数路径。安全集合（safe set）直接规定允许出现的状态。

论证与表述逻辑：

1. 定义（正向不变集）：若任意$\boldsymbol x_0\in S$所产生的闭环解，在其存在的全部未来时刻均位于$S$，称$S$对该闭环正向不变（forward invariant）。
2. 若边界$\partial S=\{h=0\}$光滑且其上$\nabla h\neq\boldsymbol0$，内侧对应$h$增大的方向。

#### 5.4.2 安全条件下的可行动作

主要内容：函数$h$只用符号区分安全与否，不必等于几何距离。

论证与表述逻辑：

1. 命题（CBF条件保证正向不变）：若反馈$\boldsymbol u=\kappa(\boldsymbol x)$局部Lipschitz，并在包含$S$的开区域$D$中始终满足$\kappa(\boldsymbol x)\in K_{\mathrm{cbf}}(\boldsymbol x)$，则$S$在相应闭环解存在的时间区间内正向不变。
2. 推导：沿任意闭环解记$r_t=h(\boldsymbol x_t)$，链式法则和CBF约束给出$\dot r_t\geq-\alpha(r_t)$。考虑比较系统$\dot z_t=-\alpha(z_t),\qquad z_0=r_0\geq0$$\alpha$局部Lipschitz，比较系统局部解唯一，且$z=0$是平衡解；从非负初值出发的解不能穿过零点。又因$\alpha$严格递增且$\alpha(0)=0$，$z_t$留在$[0,z_0]$内，所以比较解在任意有限时间存在。
3. 回到离散温度系统，令$S=[0,3],U=[0,1]$且无噪声。下一步安全要求$0\leq0.8x+u\leq3$，因此精确的一步安全动作集合为$K_{\mathrm{safe}}(x) =[\,\max\{0,-0.8x\},\ \min\{1,3-0.8x\}\,]$对$x\in[0,3]$，下端为$0$，上端至少为$0.6$，所以每个安全状态都有可行动作。

#### 5.4.3 可行约束下的反馈修正

主要内容：调节或跟踪已经提出名义动作$\boldsymbol u_{\mathrm{nom}}$，但该动作可能违反安全条件。

论证与表述逻辑：

1. 示例（一维积分器上的安全投影）：考虑$\dot x_t=u_t$、$S=[0,\infty)$、$h(x)=x$及$\alpha(h)=\gamma h$。
2. 固定状态时，正定二次目标的强制性阻止最小化序列逃向无穷，闭可行域保证取到最小值，凸性与严格凸性保证唯一。约束$xu\geq|x|^{3/2}$下唯一最优动作$\operatorname{sgn}(x)\sqrt{|x|}$仍非局部Lipschitz；约束梯度在零退化，说明调用闭环不变性前必须另验反馈规则性。
3. 于是$x_1=1$，而不是无约束的$1.153$；此时$e_1=1-[2+0.4\sin(\pi/8)]\approx-1.153$，不再等于$0.5e_0=-1$。

#### 5.4.4 扰动与离散执行下的安全保证

主要内容：名义屏障条件只计算模型给出的变化率。真实连续动态多出加性扰动时，安全函数的导数还多出$\nabla h(\boldsymbol x)^\top\boldsymbol d_t$。

论证与表述逻辑：

1. 离散温度系统若$|w_{t+1}|\leq\delta$，最坏扰动下的安全动作集合为$K_{\mathrm{safe}}^\delta(x) =[\,\max\{0,\delta-0.8x\},\ \min\{1,3-\delta-0.8x\}\,]$当$0\leq\delta\leq0.6$，该集合对所有$x\in[0,3]$非空：下端不超过$1$，未截断区间宽度$3-2\delta$非负，且上端在$x=3$也不小于零。
2. CBF还要求用于计算约束的状态信息可靠。若只有估计值，应先给估计误差集合界或概率模型，再收紧安全集合或构造输出反馈屏障。

### 5.5 本章小结

主要内容：区分可实施性、系统结构、闭环稳定、调节跟踪与安全，说明存在一条可达轨迹不足以保证固定反馈的行为。

论证与表述逻辑：

1. 一个可实施策略既要遵守信息时序，也要符合执行器能够改变的方向。可控、可观测要求处理全部状态方向；可稳定、可检测只要求危险的遗漏方向不存在。
2. 在同一温度模型中，固定目标$2$需要平衡输入$0.4$，再加误差反馈才得到$e_{t+1}=0.5e_t$。运动参考改用$u_t^r=r_{t+1}-0.8r_t$抵消参考变化，同一个稳定误差系统便能服务于跟踪。
3. Riccati方法在特定二次成本下选择反馈。有限时域的逐步配方保持二次形式；确定性无折扣无限时域还需可稳定、成本可检测及权重条件，才能同时得到稳定化与成本最优性。
4. 安全性约束全过程。对无噪声温度系统，固定目标反馈已经保持$0\leq u\leq1,0\leq x\leq3$；同一增益的运动参考却可能在初始纠偏时要求过大输入。

## 第6章 策略的价值与优化

正文：[03-policy-value-and-optimization.tex](../../tex/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/03-policy-value-and-optimization.tex)。

### 6.1 策略的表示与价值

主要内容：用可得信息到行动的映射表示策略，说明它与环境怎样共同诱导轨迹，并由轨迹收益建立策略价值。

论证与表述逻辑：

1. 策略的行动与信息：一次加热只需要一个动作值，持续控制却需要回答不同读数下分别采取什么动作。策略（policy）规定这种从已有信息到行动的选择关系。
2. 策略诱导的轨迹：同一项“走捷径”的策略，在不同路况下会有不同后果。要计算这些后果的概率，必须把初始状态、策略选出的行动与环境转移逐步连接。
3. 轨迹收益与策略价值：轨迹概率确定以后，还需指定每种后果的代价。将实际经过的状态与行动的阶段成本相加，再计入终端成本，得到一次执行的总成本。

#### 6.1.1 策略的行动与信息

主要内容：一次加热只需要一个动作值，持续控制却需要回答不同读数下分别采取什么动作。策略（policy）规定这种从已有信息到行动的选择关系。

论证与表述逻辑：

1. 若只能观察$Y_t$，允许信息是$\mathcal I_t=\sigma(Y_0,A_0,\ldots,A_{t-1},Y_t)$，策略不能直接读取$S_t$。
2. 共同温度模型仍为$x_{t+1}=0.8x_t+u_t+w_{t+1}, \qquad y_t=x_t+v_t$$x_t$是相对于环境温度的温差，$u_t$是加热量。

#### 6.1.2 策略诱导的轨迹

主要内容：同一项“走捷径”的策略，在不同路况下会有不同后果。要计算这些后果的概率，必须把初始状态、策略选出的行动与环境转移逐步连接。

论证与表述逻辑：

1. 定义（有限Markov决策过程与策略）：有限状态集$\mathcal S$、各状态的非空有限行动集$\mathcal A(s)$、初始分布$\mu_0$、受控转移概率$P_t$、阶段成本$c_t$和终端成本$c_H$组成有限时域Markov决策过程（Markov decision process, MDP）。允许策略可以根据全部已有历史随机选择行动$\pi_t(a\mid H_t)$；只依赖当前状态时为Markov策略，确定选择时记作$a=\pi_t(s)$。
2. 现在固定策略$\pi$。对一条状态与行动轨迹$\tau=(s_0,a_0,s_1,\ldots,a_{H-1},s_H)$，链式法则给出$\mathbb P^\pi(\tau) =\mu_0(s_0)\prod_{t=0}^{H-1} \pi_t(a_t\mid h_t)P_t(s_{t+1}\mid s_t,a_t)$每个因子都对应实际生成的一步：先抽初态，再按当前历史选行动，再由环境生成下一状态。
3. 用一个可以枚举全部轨迹的路线例子观察策略怎样改变分布。起点$s_0$选择“稳妥”会确定到达终端损失$2$的状态；选择“捷径”以概率$0.8$到达损失$0$的状态，以概率$0.2$到达损失$6$的状态。

#### 6.1.3 轨迹收益与策略价值

主要内容：轨迹概率确定以后，还需指定每种后果的代价。将实际经过的状态与行动的阶段成本相加，再计入终端成本，得到一次执行的总成本。

论证与表述逻辑：

1. 运行到中途，已经支付的成本不再改变，但后续行动仍可比较。对一段末状态为$s$的历史$h_t$，一般历史策略的继续成本定义为$J_t^\pi(h_t)= \mathbb E^\pi_{h_t} \left[\sum_{k=t}^{H-1}c_k(S_k,A_k)+c_H(S_H)\right]$下标$h_t$表示固定已知历史，再用策略和转移核重新生成后续过程。
2. 只有一次行动时，$L$退化为损失$\ell(a,Y)$，收益为$-\ell(a,Y)$。例如同一阳性概率$0.3$，在对称分类损失与高漏诊损失下会对应不同的行动。

### 6.2 策略的轨迹价值与风险

主要内容：固定策略后，比较平均收益、波动、尾部风险、违规概率和动态风险，说明各指标所约束的后果不同。

论证与表述逻辑：

1. 平均收益与价值波动：固定走稳妥路线的期望损失为$2$，固定走捷径的期望损失为$1.2$。捷径在平均成本上占优，却有$20\%$的概率付出损失$6$。
2. 概率约束与模型不确定性：任务也可以直接限制损失超标的概率，将违反要求的策略排除在可行范围之外。固定策略产生损失$L$，给定阈值$b$和$\varepsilon\in(0,1)$，机会约束（chance constraint）为$\mathbb P(L>b)\leq\varepsilon$它控制超标是否发生，不区分超标幅度。

#### 6.2.1 平均收益与价值波动

主要内容：固定走稳妥路线的期望损失为$2$，固定走捷径的期望损失为$1.2$。捷径在平均成本上占优，却有$20\%$的概率付出损失$6$。

论证与表述逻辑：

1. 设随机轨迹损失$L$可积。期望$\mathbb E[L]$按发生概率线性汇总所有后果；对应的期望收益为$-\mathbb E[L]$。
2. 定义（相干风险）：设风险泛函$\rho:L^1(P)\to\mathbb R$按损失越小越好的方向评价。单调性要求$L\leq L'$几乎处处时$\rho(L)\leq\rho(L')$；平移等变性要求$\rho(L+m)=\rho(L)+m$，其中$m$为确定常数。凸性要求$\rho(\tau L+(1-\tau)L') \leq\tau\rho(L)+(1-\tau)\rho(L'),\qquad 0\leq\tau\leq1$若具有单调性、平移等变性、正齐次性$\rho(\lambda L)=\lambda\rho(L)$（$\lambda\geq0$）和次可加性$\rho(L+L')\leq\rho(L)+\rho(L')$，称为相干风险（coherent risk measure）。
3. 将正齐次性用于两项按比例承担的损失，再使用次可加性，就得到前面的凸性不等式。策略随机化通常对应后者，不能直接套用这个凸性公式。

#### 6.2.2 尾部损失与风险评价

主要内容：用分位数、尾部平均和风险包络描述严重损失，比较它们的评价对象与优化表达。

论证与表述逻辑：

1. 先以损失分位数给出风险价值，再转向超过尾部阈值附近的平均损失。
2. 通过条件风险价值的优化和风险包络表示连接尾部评价与加权最坏情形，说明它们不同于只比较期望。

##### 6.2.2.1 基于分位数的风险价值

主要内容：若任务问“至少$95\%$的执行，损失能否控制在某一水平内”，需要的量是损失分位数，不是方差。

论证与表述逻辑：

1. 定义（风险价值）：对实值随机损失$L$与$\alpha\in(0,1)$，左$\alpha$分位数为$q_\alpha(L)=\inf\{z\in\mathbb R:\mathbb P(L\leq z)\geq\alpha\}$同一量在风险管理中称为风险价值（value at risk, VaR），记为$\operatorname{VaR}_\alpha(L)=q_\alpha(L)$。
2. 在前面的等均值例中，$\operatorname{VaR}_{0.95}(L_{\mathrm{safe}})=1,\qquad \operatorname{VaR}_{0.95}(L_{\mathrm{tail}})=0$第二式来自$\mathbb P(L_{\mathrm{tail}}\leq0)=0.95$。
3. VaR单调且平移等变，但一般不次可加。设互斥事件$E_1,E_2$各有概率$0.04$，令$L_i=\mathbb I\{E_i\}$。

##### 6.2.2.2 基于尾部平均的条件风险价值

主要内容：分位数给出尾部开始的阈值，却没有计入阈值以上的损失幅度。要比较严重后果，可以取出损失最大、总概率固定的一部分结果，计算它们的平均损失。

论证与表述逻辑：

1. 定义（条件风险价值）：对$L\in L^1(P)$和$\alpha\in(0,1)$，定义$\operatorname{CVaR}_\alpha(L) =\inf_{\eta\in\mathbb R} \left\{\eta+\frac{1}{1-\alpha}\mathbb E[(L-\eta)_+]\right\}, \qquad (z)_+=\max\{z,0\}$。
2. 候选阈值$\eta$提高时，第一项直接增加，超过阈值的剩余损失却会减少。记花括号中的函数为$\phi(\eta)$。
3. 横轴最优点$2$是VaR，纵轴最小值$5.2$才是CVaR；两个数在计算中承担不同角色。
4. 一般损失分布在分位点处可有原子；用严格超阈值损失加上分位原子的部分质量补齐最坏$1-\alpha$尾部，并引用适用一般损失分布的后续论文。整个超阈值事件的条件均值只在相应质量条件下可直接代入。

##### 6.2.2.3 基于风险包络的尾部评价

主要内容：阈值公式还可以写成概率权重的选择问题：限制每个结果的最大评价权重，再寻找使期望损失最大的重加权。对$L\in L^1(P)$，$\operatorname{CVaR}_\alpha(L) =\sup_\zeta\left\{\mathbb E_P[\zeta L]: 0\leq\zeta\leq\frac{1}{1-\alpha},\quad\mathbb E_P[\zeta]=1\right\}$$\zeta$是相对于原分布的密度比；这些允许密度组成风险包络。

论证与表述逻辑：

1. 一般可积分布也能直接证明等式，不必只诉诸形式对偶。对任意可行$\zeta$和$\eta$，$\mathbb E[\zeta L] =\eta+\mathbb E[\zeta(L-\eta)] \leq\eta+\frac{\mathbb E[(L-\eta)_+]}{1-\alpha}$对$\eta$取下确界，说明任意可行密度的加权期望都不超过CVaR。
2. 模型不确定性则问真实生成机制可能是哪一个分布。二者都能写成最坏期望，但一般不是同一集合，更不能把重加权结果当作重新估计出的真实事故概率。

#### 6.2.3 概率约束与模型不确定性

主要内容：任务也可以直接限制损失超标的概率，将违反要求的策略排除在可行范围之外。固定策略产生损失$L$，给定阈值$b$和$\varepsilon\in(0,1)$，机会约束（chance constraint）为$\mathbb P(L>b)\leq\varepsilon$它控制超标是否发生，不区分超标幅度。

论证与表述逻辑：

1. 必须把违规事件写清楚。温度任务可以限制终端$\{x_H>3\}$、某时刻$\{x_t>3\}$，也可以限制整段$\{\exists t\leq H:x_t\notin[0,3]\}$。
2. 有限样本空间中，非空闭候选集位于紧致概率单纯形内，线性期望必达到最大值。若集合排除某些结果，保证也只覆盖其允许支持。

#### 6.2.4 逐时信息下的动态风险

主要内容：比较出发前的静态尾部评价和逐时条件风险，解释新增信息为何可能改变偏好。

论证与表述逻辑：

1. 先用阶段性信息揭示静态准则下的偏好反转。
2. 再把条件风险逐层嵌套，检查时间一致性以及由此得到的递推评价含义。

##### 6.2.4.1 静态尾部评价与偏好反转

主要内容：从起点评价整条轨迹，与到达某个分支后重新评价剩余损失，是两个不同操作。期望有塔式性质把二者连接起来，静态CVaR一般没有同样的关系。

论证与表述逻辑：

1. 期望有塔式性质把二者连接起来，静态CVaR一般没有同样的关系。
2. 承诺$R$时，起点损失以概率$1/4,1/2,1/4$取$0,2,4$，故$\operatorname{CVaR}_{0.5}(L^R) =\frac{(1/4)\times4+(1/4)\times2}{1/2}=3$静态评价因此偏好$R$。
3. 反转不是算错，而是整条轨迹的尾部与当前分支的尾部并非同一批结果。

##### 6.2.4.2 条件风险与时间一致性

主要内容：前例的排序反转来自整条轨迹尾部与条件尾部的差别。若要求后续节点已有的风险排序传到当前，就可以把评价规则定义为递归：下一节点计算剩余风险，当前节点再汇总这些风险值。

论证与表述逻辑：

1. 静态常数阈值改成当前信息可测的阈值规则：有限树上各当前节点可用不同阈值，但不能偷看未来。单点取负一、其余为零的函数族逐点下确界为负一、本质下确界为零，解释为何必须按几乎处处等价类比较；嵌套风险再由节点向前递归。
2. 定义（一步条件风险映射）：在同一概率空间上，一步条件风险映射（conditional risk mapping）$\rho_t:L^\infty(\mathcal F_{t+1})\longrightarrow L^\infty(\mathcal F_t)$把下一时刻可知的有界随机损失转成当前信息下的风险。输入与输出均按几乎处处相等的等价类理解。
3. 定义（递归意义下的时间一致性）：动态风险族$(\mathcal R_t)$具有时间一致性（time consistency），是指对每个$t<H$、任意两组从$t+1$开始的有界适应损失和同一当前损失$C_t$，只要$\mathcal R_{t+1}(C_{t+1:H})\leq\mathcal R_{t+1}(C'_{t+1:H})$几乎处处成立，就有$\mathcal R_t(C_t,C_{t+1:H})\leq\mathcal R_t(C_t,C'_{t+1:H})$几乎处处成立。
4. 回到两节点例，先固定承诺$F$或$R$。在$B$分别得到风险值$3.5$或$4$，在$N$均为$2$；根节点再对这两个等概率节点值计算CVaR$_{0.5}$，得到$3.5$或$4$。

### 6.3 策略的轨迹价值计算

主要内容：在有限时域、无限折扣及风险评价下计算给定策略的价值，交代递推方程与解的条件。

论证与表述逻辑：

1. 有限时域下的价值递推：评价准则确定以后，可以计算指定策略的剩余成本。有限时域的终端没有后续行动，故$V_H^\pi(s)=c_H(s)$；已知下一时刻价值以后，当前只需按策略和环境的概率汇总它。
2. 无限折扣时域下的价值计算：无限时域没有终端值供反向计算。如果成本有界且折扣小于$1$，远期剩余成本可以统一控制，同一时不变策略的价值便可由“当前成本加折扣后的继续价值”这个固定点关系确定。

#### 6.3.1 有限时域下的价值递推

主要内容：评价准则确定以后，可以计算指定策略的剩余成本。有限时域的终端没有后续行动，故$V_H^\pi(s)=c_H(s)$；已知下一时刻价值以后，当前只需按策略和环境的概率汇总它。

论证与表述逻辑：

1. 恢复随机扰动后，同一反馈诱导轨迹分布而非上述单一路径。若成本可积，可以沿条件分布求期望；不能只把噪声取均值零后代回非线性的平方成本。

#### 6.3.2 无限折扣时域下的价值计算

主要内容：无限时域没有终端值供反向计算。如果成本有界且折扣小于$1$，远期剩余成本可以统一控制，同一时不变策略的价值便可由“当前成本加折扣后的继续价值”这个固定点关系确定。

论证与表述逻辑：

1. 从任意$V^{(0)}$出发令$V^{(k+1)}=T^\pi V^{(k)}$，有$\lVert V^{(k)}-V^\pi\rVert_\infty \leq\gamma^k\lVert V^{(0)}-V^\pi\rVert_\infty$若取$V^{(0)}=0$，右侧可用$\gamma^kC/(1-\gamma)$替代。
2. 将$c^\pi(s),V^\pi(s)$排列为列向量$\boldsymbol c^\pi,\boldsymbol V^\pi$，以$P^\pi(s,s')$为元素组成矩阵$\boldsymbol P^\pi$，则$\boldsymbol V^\pi=(\boldsymbol I-\gamma\boldsymbol P^\pi)^{-1}\boldsymbol c^\pi =\sum_{j=0}^\infty\gamma^j(\boldsymbol P^\pi)^j\boldsymbol c^\pi$无穷级数在最大范数下收敛，故逆矩阵存在。
3. 非平稳或一般历史策略仍有定义良好的有界折扣价值，但其继续规则可能随时间或历史变化，不能直接使用这个单一平稳算子。

#### 6.3.3 风险评价下的价值计算

主要内容：分别计算嵌套风险和预先承诺的静态尾部目标，说明两者为何需要不同的状态与递推。

论证与表述逻辑：

1. 对嵌套风险按当前信息递推，保留各阶段的条件评价。
2. 对静态尾部目标增加必要的累计或阈值信息，说明直接套用普通期望Bellman方程会丢失什么。

##### 6.3.3.1 嵌套风险下的递推计算

主要内容：先固定确定性Markov策略$a=\pi_t(s)$。若当前状态确实包含风险评价所需的信息，一步风险映射可写为$\rho_{t,s,a}$，它作用于按$P_t(\cdot\mid s,a)$分布的下一状态。

论证与表述逻辑：

1. 随机策略需要多说明一层。采取行动之前，$A_t$尚未揭晓；可在联合条件分布$\pi_t(a\mid s)P_t(s'\mid s,a)$上，对行动和下一状态一起评价：$V_t^{\pi,\rho}(s)= \rho^\pi_{t,s}\bigl(c_t(s,A_t)+V_{t+1}^{\pi,\rho}(S_{t+1})\bigr)$这里$\rho^\pi_{t,s}$的输入是$(A_t,S_{t+1})$上的随机损失，连当前阶段成本也必须放在映射内。
2. 定义（条件分布集合的矩形性）：在有限概率树上，为每个历史行动节点给定非空下一步条件分布集合。若允许的路径分布恰好包括从各节点集合任意选取条件核，再按路径相乘得到的全部分布，则称该不确定集合具有矩形性（rectangularity）。
3. 若一个未知参数全程固定，矩形性通常不成立。设$Y_1,Y_2\in\{0,1\}$在给定$p\in\{0.2,0.8\}$后独立，两次共用该$p$。

##### 6.3.3.2 静态尾部风险下的增广计算

主要内容：如果仍然要评价起点处的静态总损失CVaR，就不应更换成嵌套目标。以有限时域折扣损失$L=\sum_{t=0}^{H-1}\gamma^tc_t(S_t,A_t)+\gamma^Hc_H(S_H)$为例，这里也允许$\gamma=1$。

论证与表述逻辑：

1. 把已累计成本记为$B_0=0$、$B_{t+1}=B_t+\gamma^tc_t(S_t,A_t)$。
2. 计算完每个阈值的期望以后，该固定策略的风险为$\operatorname{CVaR}_\alpha(L^\pi) =\inf_{\eta\in\mathbb R} \left\{\eta+\frac{1}{1-\alpha} \sum_s\mu_0(s)W_0^{\pi,\eta}(s,0)\right\}$这里优化$\eta$只是计算CVaR定义中的辅助参数，并没有优化策略。

### 6.4 策略的轨迹价值优化

主要内容：在信息、动作与风险约束下选择策略，分别处理单步、离散多步、连续时间和受限信息的问题。

论证与表述逻辑：

1. 单步价值下的行动选择：只有一次行动时，轨迹损失退化为$\ell(a,Y)$。设观测为$X$，未知结果$Y\in\mathcal Y$，可选行动$a\in\mathcal A$，损失$\ell:\mathcal A\times\mathcal Y\to\mathbb R$给出每种行动在每种结果下的代价。
2. 连续演化下的策略优化：离散递推比较一个完整阶段的成本，连续时间可以比较任意短的一段。将这段成本与终点的继续价值展开，状态速度产生一阶导数，扩散的二次变差产生二阶导数。
3. 风险约束下的策略优化：风险评价同样可以进入策略选择，但递推必须忠实于已经定义的目标。嵌套条件风险按节点递归优化；静态总损失CVaR保留累计成本；概率约束限制违规事件，模型不确定集规定允许的生成机制。

#### 6.4.1 单步价值下的行动选择

主要内容：只有一次行动时，轨迹损失退化为$\ell(a,Y)$。设观测为$X$，未知结果$Y\in\mathcal Y$，可选行动$a\in\mathcal A$，损失$\ell:\mathcal A\times\mathcal Y\to\mathbb R$给出每种行动在每种结果下的代价。

论证与表述逻辑：

1. 定义（条件风险与Bayes决策）：给定条件分布核$P(\mathrm dy\mid x)$，假设损失可测且下列期望有限。行动$a$在观测$x$下的条件风险（conditional risk）为$r(a\mid x)=\mathbb E[\ell(a,Y)\mid X=x] =\int_{\mathcal Y}\ell(a,y)P(\mathrm dy\mid x)$若最小值达到，任取$a^\star(x)\in\argmin_{a\in\mathcal A}r(a\mid x)$称为Bayes行动（Bayes action）。若该选择关于$x$可测，映射$\delta^\star(x)=a^\star(x)$称为Bayes决策规则（Bayes decision rule）。
2. 可测规则$\delta$的总体风险为$R(\delta)=\mathbb E[\ell(\delta(X),Y)]$塔式法则和逐点最小性给出完整的总体比较：$R(\delta^\star) =\mathbb E\!\left[\mathbb E[\ell(\delta^\star(X),Y)\mid X]\right] =\mathbb E[\min_a r(a\mid X)] \leq\mathbb E[r(\delta(X)\mid X)] =R(\delta)$期望存在和可测选择不可省略。
3. 行动集合确定以后，还可以比较确定选择与随机选择。给定$x$，按概率核$q(\mathrm da\mid x)$选行动的风险为$\int_{\mathcal A}r(a\mid x)q(\mathrm da\mid x)\geq\inf_a r(a\mid x)$有限或可数行动时就是加权和。

#### 6.4.2 离散演化下的策略优化

主要内容：在离散演化中选择最优策略，连接有限时域递推、无限折扣不动点、占用流量验证和线性二次结构。

论证与表述逻辑：

1. 先以末端条件作反向最优递推，再在折扣条件下讨论全时域价值与贪心策略。
2. 用价值界和占用约束检查最优性，最后利用线性二次结构将一般策略求解化为专门的矩阵递推。

##### 6.4.2.1 有限时域下的最优策略递推

主要内容：当前行动改变下一状态，也改变以后能选择的行动。因此，要比较当前动作，必须把阶段成本与后继状态的最优继续成本相加。

论证与表述逻辑：

1. 命题（有限时域最优性原理）：各时刻各状态选择一个达到最小值的行动，构成达到该值的确定性Markov策略。
2. 推导：用逆向归纳。时刻$H$没有行动，终端成本就是最小继续成本。假设每段末状态为$s'$的历史$h_{t+1}$的最小继续成本均为$V_{t+1}^\star(s')$。
3. 风险偏好属于任务设定，不能在算完期望最优后将它解释成任意意义下的“最稳妥”。

##### 6.4.2.2 无限折扣时域下的最优策略计算

主要内容：保留有限状态行动、时不变转移、有界成本及$0\leq\gamma<1$。与给定策略的$T^\pi$不同，Bellman最优算子为$(TV)(s)=\min_{a\in\mathcal A(s)} \left\{c(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V(s')\right\}$对有限实数族$(u_a),(v_a)$，$|\min_a u_a-\min_a v_a|\leq\max_a|u_a-v_a|$。

论证与表述逻辑：

1. 再对任意历史依赖随机策略$\pi$比较。固定点满足每个状态行动的不等式$V^\star(s)\leq c(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^\star(s')$沿策略实际选择的行动条件化，再把下一步的不等式代入，重复$n$步得到$V^\star(s)\leq\mathbb E_s^\pi \left[\sum_{t=0}^{n-1}\gamma^tc(S_t,A_t)+\gamma^nV^\star(S_n)\right]$该操作不要求$\pi$平稳，因为每一历史选择的行动都满足同一Bellman不等式。
2. 连续状态或行动中，还需可测转移、适当的成本下半连续性、非空可行动作及紧致性或强制性条件，再用可测选择将点态最小行动拼成策略。

##### 6.4.2.3 基于价值界与占用流量的最优性验证

主要内容：一个策略成本已算出时，还需要下界来判断它离最优有多远。Bellman不等式允许提出状态价值下界，并检查它对全部行动是否成立。

论证与表述逻辑：

1. 在线性规划前先算单状态、单行动、折扣0.9的访问总量10；乘$1-\gamma$后总质量为1，阶段成本2的折扣成本20也缩放为2。随后推导价值不等式的对偶流量守恒，证明合法占用流量可由策略实现，并保持两端使用同一归一化目标。
2. 为每条不等式引入$d(s,a)\geq0$。
3. 定义（归一化折扣占用度量）：给定初始分布$\mu_0$、$0\leq\gamma<1$和允许策略$\pi$，归一化折扣占用度量（occupancy measure）为$d_\pi(s,a)=(1-\gamma)\mathbb E_{S_0\sim\mu_0}^\pi \left[\sum_{t=0}^\infty\gamma^t \mathbb I\{S_t=s,A_t=a\}\right]$。
4. 互补松弛给出$d^\star(s,a)>0\ \Longrightarrow\ V^\star(s)=c(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^\star(s')$最优访问中实际使用的行动必须达到Bellman最小值。

##### 6.4.2.4 线性二次成本下的有限时域策略

主要内容：有限MDP通过逐行动枚举求最小值，线性二次模型则能利用代数结构直接求出最小行动。本节只把这个结果接到本章的策略价值接口，不重复定义或配方证明。

论证与表述逻辑：

1. 该模型的最优继续价值具有$V_t^\star(\boldsymbol x)=\boldsymbol x^\top\boldsymbol P_t\boldsymbol x+\beta_t$的形式。
2. 给定反馈的评价只需代入该反馈；求最优反馈才需要对二次行动项最小化。共同温度例的总输入成本也提醒我们，换成偏移输入$(u-0.4)^2$会改变目标。

#### 6.4.3 连续演化下的策略优化

主要内容：离散递推比较一个完整阶段的成本，连续时间可以比较任意短的一段。将这段成本与终点的继续价值展开，状态速度产生一阶导数，扩散的二次变差产生二阶导数。

论证与表述逻辑：

1. 确定性轨迹的价值方程：考虑从$(\boldsymbol x,t)$出发的受控系统与成本$\dot{\boldsymbol x}(s)&=\boldsymbol f(\boldsymbol x(s),\boldsymbol u(s),s),\qquad \boldsymbol x(t)=\boldsymbol x, \\ J_{t,\boldsymbol x}(\boldsymbol u) &=\phi(\boldsymbol x(T))+\int_t^T\ell(\boldsymbol x(s),\boldsymbol u(s),s)\,\mathrm ds$状态属于$\mathbb R^n$，动作属于非空集合$U$。
2. 随机轨迹的价值方程：随机轨迹无法逐条预先选择，但可以优化允许策略的期望成本。
3. 线性二次成本下的连续策略：在线性动态$\dot{\boldsymbol x}=\boldsymbol A\boldsymbol x+\boldsymbol B\boldsymbol u$下，取$\boldsymbol u\in\mathbb R^m$，阶段成本$\ell(\boldsymbol x,\boldsymbol u)=\boldsymbol x^\top\boldsymbol Q\boldsymbol x+\boldsymbol u^\top\boldsymbol R\boldsymbol u$，终端成本$\phi(\boldsymbol x)=\boldsymbol x^\top\boldsymbol Q_T\boldsymbol x$，其中$\boldsymbol Q,\boldsymbol Q_T\succeq\boldsymbol0$、$\boldsymbol R\succ\boldsymbol0$。
4. 非光滑与受限信息下的价值方程：不同动作的最优成本可能在某处交会，使价值连续却出现折点。此时轨迹成本仍有定义，但经典HJB所用的梯度无法在交会点直接计算。

##### 6.4.3.1 确定性轨迹的价值方程

主要内容：考虑从$(\boldsymbol x,t)$出发的受控系统与成本$\dot{\boldsymbol x}(s)&=\boldsymbol f(\boldsymbol x(s),\boldsymbol u(s),s),\qquad \boldsymbol x(t)=\boldsymbol x, \\ J_{t,\boldsymbol x}(\boldsymbol u) &=\phi(\boldsymbol x(T))+\int_t^T\ell(\boldsymbol x(s),\boldsymbol u(s),s)\,\mathrm ds$状态属于$\mathbb R^n$，动作属于非空集合$U$。

论证与表述逻辑：

1. 命题（确定性HJB验证定理）：假设每个允许控制都产生存在到$T$的轨迹，沿轨迹的链式法则和成本积分成立。若有可实现反馈$\boldsymbol u^\star=\kappa(\boldsymbol x,t)$逐点达到HJB下确界，且闭环轨迹存在到$T$并满足所有可行条件，则$V$为最优价值，$\kappa$为最优反馈。
2. 推导：任取允许控制，HJB的下确界不大于代入该动作的值，所以沿轨迹$\partial_sV(\boldsymbol x(s),s)+ \nabla_{\boldsymbol x}V(\boldsymbol x(s),s)^\top \boldsymbol f(\boldsymbol x(s),\boldsymbol u(s),s) +\ell(\boldsymbol x(s),\boldsymbol u(s),s)\geq0$前两项由链式法则合为$\mathrm dV(\boldsymbol x(s),s)/\mathrm ds$。从$t$积分到$T$，用终端条件得到$J_{t,\boldsymbol x}(\boldsymbol u)\geq V(\boldsymbol x,t)$。因而候选值是所有允许成本的共同下界。
3. HJB是光滑最优价值满足的局部关系；验证定理则把一个候选解变成全程最优性的证书。只在若干采样点降低方程残差还不够，还需终端或边界条件、极小动作的可实现性、轨迹存在性及整个相关区域上的方程关系。

##### 6.4.3.2 随机轨迹的价值方程

主要内容：随机轨迹无法逐条预先选择，但可以优化允许策略的期望成本。

论证与表述逻辑：

1. 随机轨迹无法逐条预先选择，但可以优化允许策略的期望成本。设$\boldsymbol W_s$为$d$维标准Brownian运动，状态满足$\mathrm d\boldsymbol X_s=\boldsymbol f(\boldsymbol X_s,\boldsymbol u_s,s)\,\mathrm ds +\boldsymbol\Sigma(\boldsymbol X_s,\boldsymbol u_s,s)\,\mathrm d\boldsymbol W_s,$其中$\boldsymbol\Sigma$为$n\times d$矩阵。
2. 命题（随机HJB验证）：若可容许反馈$\boldsymbol u^\star=\kappa(\boldsymbol x,t)$逐点达到HJB下确界，则$V$等于最优期望成本，$\kappa$达到该值。
3. 推导：对任意允许控制，HJB给出$\partial_sV+\mathcal L^{\boldsymbol u_s}V+\ell(\boldsymbol X_s,\boldsymbol u_s,s)\geq0$。沿轨迹应用Itô公式、积分并取从$(t,\boldsymbol x)$出发的期望，随机积分因真鞅条件消失，得到$\mathbb E_{t,\boldsymbol x}\left[ \phi(\boldsymbol X_T)+\int_t^T\ell(\boldsymbol X_s,\boldsymbol u_s,s)\,\mathrm ds\right] \geq V(\boldsymbol x,t)$对$\kappa$，生成元不等式取等号，同一计算证明其期望成本等于共同下界$V$。这验证的是期望最优，不是每条噪声实现上的路径最优。
4. 若扩散依赖动作，它直接参与动作最小化；依赖状态时也可能改变价值形状。因此噪声均值为零并不足以保证反馈不变。

##### 6.4.3.3 线性二次成本下的连续策略

主要内容：在线性动态$\dot{\boldsymbol x}=\boldsymbol A\boldsymbol x+\boldsymbol B\boldsymbol u$下，取$\boldsymbol u\in\mathbb R^m$，阶段成本$\ell(\boldsymbol x,\boldsymbol u)=\boldsymbol x^\top\boldsymbol Q\boldsymbol x+\boldsymbol u^\top\boldsymbol R\boldsymbol u$，终端成本$\phi(\boldsymbol x)=\boldsymbol x^\top\boldsymbol Q_T\boldsymbol x$，其中$\boldsymbol Q,\boldsymbol Q_T\succeq\boldsymbol0$、$\boldsymbol R\succ\boldsymbol0$。

论证与表述逻辑：

1. 有限时域上这些条件也保证不会在中途丢失所需解。矩阵常微分方程先在终端附近有唯一局部对称解；在其存在区间，反馈连续，验证定理说明其二次型为非负最优成本，并不大于零控制的有限成本。
2. 还可以直接给出成本差证书。
3. 连续闭环需要特征值实部为负，离散闭环需要特征值位于单位圆内；CARE与DARE分别服务于这两个问题，不能混用。

##### 6.4.3.4 非光滑与受限信息下的价值方程

主要内容：不同动作的最优成本可能在某处交会，使价值连续却出现折点。此时轨迹成本仍有定义，但经典HJB所用的梯度无法在交会点直接计算。

论证与表述逻辑：

1. 测试函数定义前先看$\dot x=u,|u|\leq1$的固定终点任务：可达区间给出价值$\max\{|x|-(T-t),0\}$及延续域内部折点。后续用上下接触导数检验黏性条件，与到达原点即退出时的边界折点分开，再讨论状态约束与信念状态。
2. 定义（连续价值函数的黏性解）：设$V$在方程作用域内连续。对任意光滑测试函数$\varphi$，若$V-\varphi$在内点$(\boldsymbol x,t)$取局部最大值时均有$F(\boldsymbol x,t,\partial_t\varphi,\nabla_{\boldsymbol x}\varphi)\leq0$，称$V$为黏性次解。若局部最小值处均有相应的$F\geq0$，称为黏性上解。同时满足两项，并按当前问题满足终端或边界条件的$V$称为黏性解。
3. 可将测试函数平移常数使接触时$V=\varphi$。局部最大对应$\varphi$从上方接触，局部最小对应从下方接触；不是任取一个斜率代入。
4. HJB比较累计成本，前章的屏障约束限定安全行动。将屏障二次规划用于修正一个性能反馈，通常会改变原成本最优性；在HJB中直接加入约束则是另一个受约束优化问题。

#### 6.4.4 受限信息下的策略选择

主要内容：研究新增观测、未知收益探索与状态估计怎样改变行动选择，说明信息价值与控制之间的联系。

论证与表述逻辑：

1. 先比较得到观测前后可选择的策略及其价值，再讨论行动同时产生收益和辨认信息的作用。
2. 在线性高斯条件下说明估计与行动分离所需结构，并限定这一结论的适用范围。

##### 6.4.4.1 新增观测下的决策收益

主要内容：前面的最优规则都受到已有信息限制。如果先获得一次观测，后面的行动可能随观测改变，这项改进能否抵偿获取成本？

论证与表述逻辑：

1. 定义（期望样本信息价值）：在上述有限行动、可积损失和信号核条件下，期望样本信息价值（expected value of sample information, EVSI）为$\operatorname{EVSI}(Z\mid b) =\mathcal R(b)-\mathbb E_{Z\mid b}[\mathcal R(b_Z)]$。
2. 观察后的$\inf_a$在对$Z$求期望之内：先见信号、再行动。若把$\inf_a$放在外面，就强迫所有信号结果使用同一行动，丢失信息的用途。
3. 互信息衡量关于$\Theta$的不确定性平均减少多少，EVSI衡量给定损失下最优决策改善多少。信号可能精确揭示与行动无关的参数，互信息大而EVSI为零；另一个信号只在决策阈值附近改变信念，却可能避免高代价行动。

##### 6.4.4.2 未知收益下的探索价值

主要内容：信息不一定来自独立购买的信号，也可能来自行动自身的结果。考虑两轮选择，每次成功奖励$1$、失败奖励$0$，本小节改用收益最大化，对应成本为奖励的负值。

论证与表述逻辑：

1. 自适应查询也改变统计证据的条件。因为过去观察决定下一次试验或停止时间，不能把选中样本无条件视为固定设计下的独立同分布数据。
2. 遗憾使用另一个比较对象。令$Y_t$为第$t$轮奖励，$\mathcal H_{t-1}$为行动前信息，行动$A_t$在$Y_t$揭晓前选定，并假设对固定环境参数$\theta$，$\mathbb E[Y_t\mid\mathcal H_{t-1},A_t=a,\Theta=\theta] =\mu(a,\theta)\quad\text{几乎处处}$这里平均奖励不随轮次改变；条件均值假设使自适应选择后当前噪声仍正确中心化，却不使访问次数或全部数据变成非自适应。

##### 6.4.4.3 线性高斯条件下的估计与行动分离

主要内容：探索例中，当前动作改变了未来可获得的信息，因此估计和行动选择必须联合比较。在标准有限时域线性二次高斯控制（linear-quadratic-Gaussian control, LQG）中，已知动作只平移预测均值，不改变估计误差协方差。

论证与表述逻辑：

1. 令$\boldsymbol e_t=\boldsymbol x_t-\widehat{\boldsymbol x}_t$，投影性质说明$\mathbb E[\boldsymbol e_t\mid\mathcal I_t]=\boldsymbol0$，从而$\mathbb E[\boldsymbol x_t^\top\boldsymbol Q_t\boldsymbol x_t\mid\mathcal I_t] =\widehat{\boldsymbol x}_t^\top\boldsymbol Q_t\widehat{\boldsymbol x}_t +\operatorname{tr}(\boldsymbol Q_t\boldsymbol E_t)$交叉项的条件期望为零，因而无条件也有$\mathbb E[\widehat{\boldsymbol x}_t^\top\boldsymbol Q_t\boldsymbol e_t]=0$。
2. 只看这一项分解还不能证明全程最优，需要把所有未来动作的影响合在一起。令$\boldsymbol P_t,\boldsymbol K_t$取前章有限LQR递推的结果，$\boldsymbol M_t=\boldsymbol R_t+\boldsymbol B^\top\boldsymbol P_{t+1}\boldsymbol B\succ\boldsymbol0$。
3. 这就是分离原则：Kalman滤波根据观测创新更新条件均值，增益由误差协方差递推确定；LQR根据二次成本权重计算反馈增益，再将状态估计接入反馈。

#### 6.4.5 风险约束下的策略优化

主要内容：风险评价同样可以进入策略选择，但递推必须忠实于已经定义的目标。嵌套条件风险按节点递归优化；静态总损失CVaR保留累计成本；概率约束限制违规事件，模型不确定集规定允许的生成机制。

论证与表述逻辑：

1. 若声明风险作用于行动和下一状态的联合损失，则应优化概率分布$q\in\Delta(\mathcal A(s))$：$\inf_q\,\rho^q_{t,s}\bigl(c_t(s,A)+V_{t+1}(S')\bigr)$不能无条件用期望的线性性把它写成动作风险的平均，再声称确定策略最优。
2. 最坏模型目标为$\inf_{\pi\in\Pi_{\mathrm{adm}}} \sup_{Q\in\mathcal P}\mathbb E_Q^\pi[L]$单步时退化为$\inf_a\sup_Q\mathbb E_Q[\ell(a,Y)]$，参数模型用$Q=P_\theta$。

### 6.5 本章小结

主要内容：用两阶段路线任务连接策略、轨迹、价值与优化，强调期望最优、尾部风险与逐轨迹安全需要分别评价。

论证与表述逻辑：

1. 同一两阶段路线任务串起了本章四个步骤。策略先规定走捷径的概率$p$，再与环境共同产生概率为$1-p,0.8p,0.2p$的三条轨迹；给每条轨迹计价后，期望损失为$2-0.8p$，尾部指标和违规概率还描述它的其他后果。
2. 平均收益、一次实现收益和尾部损失不是同一个对象。VaR给出分位阈值，CVaR平均最坏尾部，并在分位原子上按需要补足概率质量。
3. 价值迭代收敛描述的是计算序列$V^{(k)}$，闭环状态收敛描述的是执行轨迹$x_t$，二者不是同一个时间轴上的同一结论。

## 第7章 多方策略的响应与演化

正文：[04-multi-agent-response-and-evolution.tex](../../tex/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/04-multi-agent-response-and-evolution.tex)。

### 7.1 策略的多方行动与信息

主要内容：从联合行动建立多方决策，明确各方可见历史、纯策略、混合策略、完整计划与行为策略。

论证与表述逻辑：

1. 参与者与联合行动：房间下一时刻的温度取决于两台加热器的合计供热量。因此，评价任一人的行动都要同时给定另一人的行动。
2. 纯策略与混合策略：在匹配硬币中，双方同时选正面$H$或反面$T$，相同则第1方得$1$，不同则得$-1$，第2方收益相反。固定选择某一面会给对方留下针对它的机会，于是需要随机化：用一个概率分布选择行动，而不是在一局里把两个行动各执行一半。
3. 行动历史与可用信息：矩阵的一行可以表示一份多步计划，其中包含“若看到某种情况，就采取某个行动”。这份计划是否可执行，取决于参与者在相应时刻能否区分那些情况。
4. 完整策略与行为策略：三张牌中，第1方的完整纯计划按“高牌时行动、低牌时行动”有$(P,P),(B,P),(P,B),(B,B)$四种，第2方有$F,C$两种。

#### 7.1.1 参与者与联合行动

主要内容：房间下一时刻的温度取决于两台加热器的合计供热量。因此，评价任一人的行动都要同时给定另一人的行动。

论证与表述逻辑：

1. 定义（有限矩阵博弈）：有限双人矩阵博弈（matrix game）由两组非空有限行动$A_1=\{1,\ldots,m\}$、$A_2=\{1,\ldots,n\}$和两张收益矩阵$\boldsymbol{U}_1,\boldsymbol{U}_2\in\mathbb{R}^{m\times n}$给出。第1位参与者选择行，第2位参与者选择列，落在$(i,j)$时，两人的收益分别为$\bigl((\boldsymbol{U}_1)_{i,j},(\boldsymbol{U}_2)_{i,j}\bigr)$。若存在矩阵$\boldsymbol{M}$使$\boldsymbol{U}_1=\boldsymbol{M}$、$\boldsymbol{U}_2=-\boldsymbol{M}$，双方收益之和恒为零，就得到零和博弈（zero-sum game）。
2. 一个人增加的收益正好是另一个人的损失，因此零和情形只需记录第1位参与者的收益矩阵$\boldsymbol{M}$；一般和情形则不能省略第二张矩阵。
3. 若双方目标同为$2$，维持$x_t=2$要求总输入为$0.4$，并非每人都输入$0.4$。对固定反馈$u_{i,t}=a_i-k_i(x_t-2)$，只有$a_1+a_2=0.4$时，误差才满足$x_{t+1}-2=(0.8-k_1-k_2)(x_t-2)$因此总增益为$0.3$时才复现前章的误差系数$0.5$。

#### 7.1.2 纯策略与混合策略

主要内容：在匹配硬币中，双方同时选正面$H$或反面$T$，相同则第1方得$1$，不同则得$-1$，第2方收益相反。固定选择某一面会给对方留下针对它的机会，于是需要随机化：用一个概率分布选择行动，而不是在一局里把两个行动各执行一半。

论证与表述逻辑：

1. 定义（纯策略与混合策略）：直接选择某一行或某一列称为纯策略（pure strategy）。在行动上选择概率分布称为混合策略（mixed strategy）。记$\Delta_m = \left\{ \boldsymbol{x}\in\mathbb{R}^m: \boldsymbol{x}\geq\boldsymbol{0},\ \boldsymbol{1}^{\top}\boldsymbol{x}=1 \right\}$为$m$个行动上的概率单纯形。双方以各自的混合策略独立抽取行动。
2. 对一般有限行动集写作$\boldsymbol\sigma_i\in\Delta(A_i)$，联合策略为$\boldsymbol\sigma=(\boldsymbol\sigma_1,\ldots,\boldsymbol\sigma_n)$，其余人的策略组合记为$\boldsymbol\sigma_{-i}$。
3. 单纯形$\Delta_m$嵌在$\mathbb R^m$中，维数为$m-1$，顶点对应纯行动。匹配硬币只需一个数$p\in[0,1]$表示第1方选$H$的概率，另一个数$q$表示第2方的同类概率。

#### 7.1.3 行动历史与可用信息

主要内容：矩阵的一行可以表示一份多步计划，其中包含“若看到某种情况，就采取某个行动”。这份计划是否可执行，取决于参与者在相应时刻能否区分那些情况。

论证与表述逻辑：

1. 定义（有限扩展式博弈的历史树）：扩展式博弈（extensive-form game）用历史树保留这些信息。记$\mathcal H$为非空有限历史集合，空历史为$\varnothing$。不能再延长的历史组成终止集合$Z\subset\mathcal H$。若$h\notin Z$，可选行动集合$A(h)$规定合法后继$ha$，参与者函数$P(h)$指出下一步由哪位参与者行动；机会节点记为$P(h)=c$，其行动概率$\sigma_c(a\mid h)$已给定、非负且在$A(h)$上和为$1$。终止历史$z$为每位参与者给出收益$u_i(z)$。对各参与者，还需指定下面的信息集划分，才能完整确定博弈。
2. 定义（信息集）：参与者$i$的信息集（information set）族$\mathcal{I}_i$是$\mathcal H_i$的一个划分，每个信息集$I\in\mathcal{I}_i$收集参与者当时无法区分的决策历史。同一信息集中的历史必须具有相同的合法行动集，记这个共同集合为$A(I)=A(h)$，其中$h\in I$。
3. 参与者2不能规定“高牌质询就应对，低牌质询就退让”，因为他无法区分这两个节点。若公开牌面，信息集就拆成两个单点集合，可实施的策略集合已经改变；不能继续使用隐藏牌博弈的解。

#### 7.1.4 完整策略与行为策略

主要内容：三张牌中，第1方的完整纯计划按“高牌时行动、低牌时行动”有$(P,P),(B,P),(P,B),(B,B)$四种，第2方有$F,C$两种。

论证与表述逻辑：

1. 命题（Kuhn实现等价）：在有限完全回忆扩展式博弈中，对任一参与者，任意混合策略都存在一个行为策略，使二者面对任意固定的对手与机会策略时诱导相同的终止历史分布；任意行为策略也存在具有同样性质的混合策略。
2. 推导：先从混合策略构造行为策略。设$\mu_i$是在有限纯策略集合上的分布。完全回忆保证每个信息集$I$都有唯一的本人前缀$\rho_i(I) = \bigl((I_1,a_1),\ldots,(I_k,a_k)\bigr),$即到达$I$以前本人依次经过的信息集和采取的行动；同一$I$中的所有历史共享这条前缀。
3. 牌面例满足完全回忆，因为每人只行动一次。比如以概率$2/3$抽取$(B,P)$、以概率$1/3$抽取$(B,B)$，等价于$b_H=1,b_L=1/3$的行为策略；此处只验证表示等价，其价值及最优性将在收益计算和响应条件中分别核对。

### 7.2 策略的多方价值

主要内容：在给定联合策略下计算各方收益，比较零和、共同收益及联盟价值，并讨论合作贡献与分配。

论证与表述逻辑：

1. 对抗与共同收益的价值关系：同一行动空间上可以有不同的利益关系。一般和博弈（general-sum game）允许各人收益独立规定；共同收益模型则让所有人使用同一个收益函数。

#### 7.2.1 给定策略下的收益计算

主要内容：把给定联合策略转成各方期望收益，分别处理单轮行动表和具有历史的信息树。

论证与表述逻辑：

1. 先按联合行动的概率加权各方收益，明确混合策略与收益矩阵的角色。
2. 再累计历史到达及终局概率，将完整策略诱导的路径转成整局价值。

##### 7.2.1.1 联合行动下的期望收益

主要内容：$u_i(\boldsymbol{\sigma}) = \sum_{\boldsymbol{a}\in A_1\times\cdots\times A_n} \left( \prod_{j=1}^{n}\sigma_j(a_j) \right) u_i(\boldsymbol{a})$后文仍用$u_i$表示纯行动收益及其混合延拓，参数能区分二者。

论证与表述逻辑：

1. 若改用相关联合分布$\mu$，应计算$u_i(\mu)=\sum_{\boldsymbol a}\mu(\boldsymbol a)u_i(\boldsymbol a),$不能把$\mu$擅自换成边缘概率的乘积。
2. 匹配硬币的行方收益矩阵为$\boldsymbol M_{\mathrm{mp}}= \begin{pmatrix}1&-1\\-1&1\end{pmatrix}$按四个联合行动的概率加权，得到混合收益$\begin{aligned} u_1(p,q)&=pq+(1-p)(1-q)\\ &\quad-p(1-q)-(1-p)q\\ &=(2p-1)(2q-1) \end{aligned}$给定$q$，纯行动$H,T$的收益分别为$2q-1,1-2q$。

##### 7.2.1.2 行动历史下的整局价值

主要内容：历史树中，一条终局路径可能包含多次行动。要算整局收益，先把沿途概率相乘，再按各终局收益求和。

论证与表述逻辑：

1. 从历史$h$继续到终止历史$z$的条件路径概率记为$\pi^{\boldsymbol{\sigma}}(h,z)$。
2. 该矩阵已经对机会发牌取过期望，不能在后续矩阵运算中再乘一次$1/2$。

#### 7.2.2 对抗与共同收益的价值关系

主要内容：同一行动空间上可以有不同的利益关系。一般和博弈（general-sum game）允许各人收益独立规定；共同收益模型则让所有人使用同一个收益函数。

论证与表述逻辑：

1. 一般和行从$(R,R)$换成$(L,L)$能使双方收益由$1$增至$2$，称为Pareto改进：所有人都不变差且至少一人变好。
2. 温度模型也需要保留这项区别。取$x=0,r_1=r_2=2$、$\lambda_1=\lambda_2=1$，若$(u_1,u_2)=(1,0)$，两人成本分别为$2,1$。

#### 7.2.3 合作价值的贡献与分配

主要内容：以联盟可取得的价值定义加入者的边际贡献，再按参与次序平均形成贡献分配。

论证与表述逻辑：

1. 先固定联盟价值函数，比较某人加入前后的收益增量。
2. 遍历或平均不同加入次序，说明分配依据及其与单个行动回报的区别。

##### 7.2.3.1 联盟价值与边际贡献

主要内容：若参与者决定共享信息或资源，问题转为合作能产生多少额外价值，以及如何分给成员。这与把延迟奖励传回同一参与者的不同时刻不同，后者是强化学习中的时序信用分配。

论证与表述逻辑：

1. 定义（可转移效用博弈）：可转移效用合作博弈（transferable-utility cooperative game）由参与者集合$N$和联盟价值函数$v:2^N\to\mathbb{R},\qquad v(\varnothing)=0$组成，$N$为非空有限集合。$v(S)$表示联盟$S$独立合作时可取得并能在成员之间转移的总收益。
2. 联盟价值不是从单个模型输出自动得到的。对牌面判断任务，可以把$v(S)$定义为联盟$S$共享信号后，相对于无信号基线减少的最优期望损失；也可以定义为收入、正确判断数或节省的核验成本。
3. 参与者$i$加入已有联盟$S\subseteq N\setminus\{i\}$的边际贡献为$v(S\cup\{i\})-v(S)$它依赖先到者集合$S$。

##### 7.2.3.2 基于参与顺序的贡献分配

主要内容：同一位信息提供者的贡献取决于已有成员：没有其他线索时，一次校验可能没有用；已有线索时，它却能排除一个错误判断。

论证与表述逻辑：

1. 定义（Shapley值）：对上述可转移效用博弈、$n=|N|$及参与者$i\in N$，其Shapley分配为$\phi_i(v) = \sum_{S\subseteq N\setminus\{i\}} \frac{|S|!(n-|S|-1)!}{n!} \bigl[ v(S\cup\{i\})-v(S) \bigr]$。
2. 推导：每个排列中，所有参与者的边际贡献沿加入次序望远镜相加为$v(N)-v(\varnothing)=v(N),$取期望得到有效性。交换两位对称参与者不会改变排列分布或边际贡献分布，得到对称性。虚设参与者的每项边际贡献都为零。
3. 若把价值改成模型预测分数，Shapley公式仍可计算，但解释也随之改变。特征彼此相关时，“缺少某个特征”的联盟输入怎样构造还需要条件分布、边缘分布或干预语义；这些选择分别回答预测归因与因果效应问题，不能只用同一个Shapley名称消除差异。

### 7.3 策略的多方响应与均衡

主要内容：由单方最佳响应进入Nash均衡，再比较零和保证、共同建议下的偏离和联盟退出约束。

论证与表述逻辑：

1. 给定其他策略下的最佳响应：在牌面任务中，应对概率决定低牌质询是否有利；在温度任务中，对方供热量决定本人还需要供热多少。把其他参与者的策略固定后求本人的最优策略，得到最佳响应（best response）。
2. 零和对抗下的保证与均衡：均衡从双方同时响应出发；零和中还可以从一方防御所有对手策略出发。三张牌矩阵的每行最小收益依次为$0,1/2,-1,0$，每列最大收益均为$1$。
3. 共同建议下的偏离与均衡：Nash均衡要求各人的随机化彼此独立。若一个公共装置先抽取联合行动$\boldsymbol{A}\sim\mu$，再分别向参与者发送建议，建议之间可以相关。
4. 合作分配下的偏离与稳定：按贡献分得收益的成员仍可能退出：若某个联盟自行合作得到的总收益更多，联盟成员就有共同拒绝分配的理由。收益不能转移时，本节还会在可行收益前沿上按分歧点选择协商结果；这是另一项分配选择任务，不能用它代替联盟不阻挡条件。

#### 7.3.1 给定其他策略下的最佳响应

主要内容：在牌面任务中，应对概率决定低牌质询是否有利；在温度任务中，对方供热量决定本人还需要供热多少。把其他参与者的策略固定后求本人的最优策略，得到最佳响应（best response）。

论证与表述逻辑：

1. 定义（最佳响应）：在有限战略式博弈中，给定$\boldsymbol\sigma_{-i}$，参与者$i$的最佳响应集合为$\operatorname{BR}_i(\boldsymbol\sigma_{-i}) =\argmax_{\widetilde{\boldsymbol\sigma}_i\in\Delta(A_i)} u_i(\widetilde{\boldsymbol\sigma}_i,\boldsymbol\sigma_{-i})$。
2. 双人零和时，行方最大化$\boldsymbol x^\top\boldsymbol M\boldsymbol y$，列方最小化同一个式子。
3. 对温度一步成本，固定$u_j$后严格凸性给出唯一响应。求导并令导数为零：$\frac{\partial J_i}{\partial u_i} =2(0.8x+u_i+u_j-r_i)+2\lambda_i u_i=0$于是$B_i(u_j;x)=\frac{r_i-0.8x-u_j}{1+\lambda_i}$在$x=0,r_i=2,\lambda_i=1$时，对方取$0.8$，本人就愿意改为$0.6$。

#### 7.3.2 相互最佳响应下的Nash均衡

主要内容：以所有参与者都无法单方改善定义Nash条件，再用最佳响应映射讨论均衡存在。

论证与表述逻辑：

1. 先固定其他人的策略，写出本人偏离可获得的收益差。
2. 将各人的最佳响应同时满足解释为不动点，再在相应有限或连续条件下讨论存在性。

##### 7.3.2.1 单方偏离与Nash条件

主要内容：只求一人的响应仍没有决定联合结果。把每人的最佳响应条件同时写下，就得到Nash均衡（Nash equilibrium）：只要其他人不变，没有谁能靠单独改策略提高收益。

论证与表述逻辑：

1. 定义（Nash均衡）：联合混合策略$\boldsymbol\sigma^\star$是Nash均衡，若对每个参与者$i$及每个可实施的替代策略$\widetilde{\boldsymbol\sigma}_i$，$u_i(\boldsymbol\sigma_i^\star,\boldsymbol\sigma_{-i}^\star) \geq u_i(\widetilde{\boldsymbol\sigma}_i,\boldsymbol\sigma_{-i}^\star)$。
2. 等价地，各方最大单方改进$\max_{\widetilde{\boldsymbol\sigma}_i}u_i(\widetilde{\boldsymbol\sigma}_i,\boldsymbol\sigma_{-i}^\star) -u_i(\boldsymbol\sigma^\star)$均为零。
3. 三张牌的同时响应要求$b_H=1$、$b_L=1/3$、$c=1/3$。温度一步例则解$2u_1+u_2=2,\ u_1+2u_2=2$，得到唯一解$u_1^\star=u_2^\star=\frac23,\qquad x_1=\frac43,\qquad J_i^\star=\frac89$双方都不愿独改，但共同改成$(0.8,0.8)$可把两人成本降为$0.8<8/9$。

##### 7.3.2.2 响应映射与均衡存在

主要内容：若每个最佳响应都是唯一且连续的，就可以把所有人的响应拼成映射$B(\boldsymbol{\sigma}) = \bigl( \operatorname{BR}_1(\boldsymbol{\sigma}_{-1}),\ldots, \operatorname{BR}_n(\boldsymbol{\sigma}_{-n}) \bigr),$再寻找$B(\boldsymbol{\sigma})=\boldsymbol{\sigma}$。

论证与表述逻辑：

1. 命题（有限博弈存在混合Nash均衡）：参与者数有限、各行动集非空且有限的战略式博弈至少存在一个混合策略Nash均衡。
2. 推导：联合混合策略空间$K=\prod_{i=1}^{n}\Delta(A_i)$是有限维非空紧凸集。定义联合最佳响应对应$F(\boldsymbol{\sigma}) = \prod_{i=1}^{n} \operatorname{BR}_i(\boldsymbol{\sigma}_{-i})$对固定$\boldsymbol{\sigma}_{-i}$，收益关于$\boldsymbol{\sigma}_i$连续，而概率单纯形紧，所以最大值达到，$\operatorname{BR}_i$非空且紧。收益关于自身混合策略线性，两个最佳响应的凸组合仍达到同一最大值，所以最佳响应值集是凸集。
3. 存在性没有给出唯一性、计算效率或学习动态收敛。即便收益矩阵很小，最佳响应也可能在多个均衡之间切换；在“石头、剪刀、布”一类循环响应中，逐轮选择当前最佳纯行动甚至不会收敛。

#### 7.3.3 零和对抗下的保证与均衡

主要内容：均衡从双方同时响应出发；零和中还可以从一方防御所有对手策略出发。三张牌矩阵的每行最小收益依次为$0,1/2,-1,0$，每列最大收益均为$1$。

论证与表述逻辑：

1. 命题（有限零和博弈的极小极大定理）：对任意有限收益矩阵$\boldsymbol{M}$，有$\max_{\boldsymbol{x}\in\Delta_m} \min_{\boldsymbol{y}\in\Delta_n} \boldsymbol{x}^{\top}\boldsymbol{M}\boldsymbol{y} = \min_{\boldsymbol{y}\in\Delta_n} \max_{\boldsymbol{x}\in\Delta_m} \boldsymbol{x}^{\top}\boldsymbol{M}\boldsymbol{y}$共同数值称为博弈值$v^\star$。等式两侧的最优解分别称为双方的极小极大策略。
2. 推导：引入第1位参与者要保证的收益下界$v$。条件$(\boldsymbol{M}^{\top}\boldsymbol{x})_j\geq v$对每一列成立，恰好表示任何纯列都不能把收益压到$v$以下。第1位参与者的问题因此是$\begin{aligned} \max_{\boldsymbol{x},v}\quad&v\\ \text{s.t.}\quad& \boldsymbol{M}^{\top}\boldsymbol{x}\geq v\boldsymbol{1},\\ &\boldsymbol{1}^{\top}\boldsymbol{x}=1,\qquad \boldsymbol{x}\geq\boldsymbol{0} \end{aligned}$它的最优值正是$\underline v$。
3. 鞍点条件恰是双方的Nash条件：行方不能增加收益，列方不能降低行方收益。反过来，任一零和Nash均衡也给出这组鞍点不等式，故其收益等于同一个博弈值。

#### 7.3.4 共同建议下的偏离与均衡

主要内容：Nash均衡要求各人的随机化彼此独立。若一个公共装置先抽取联合行动$\boldsymbol{A}\sim\mu$，再分别向参与者发送建议，建议之间可以相关。

论证与表述逻辑：

1. 定义（粗相关均衡与相关均衡）：设$\mu$为有限战略式博弈中联合行动集$\prod_i A_i$上的概率分布。分布$\mu$是粗相关均衡（coarse correlated equilibrium, CCE），若对每个参与者$i$和任意固定行动$a_i'$，$\mathbb{E}_{\boldsymbol{A}\sim\mu}[u_i(\boldsymbol{A})] \geq \mathbb{E}_{\boldsymbol{A}\sim\mu} [u_i(a_i',\boldsymbol{A}_{-i})]$偏离者必须在看到建议之前承诺改用同一个固定行动。若允许他看到建议$A_i$后按映射$\phi_i(A_i)$改动，则要求$\mathbb{E}_{\boldsymbol{A}\sim\mu}[u_i(\boldsymbol{A})] \geq \mathbb{E}_{\boldsymbol{A}\sim\mu} [u_i(\phi_i(A_i),\boldsymbol{A}_{-i})]$对所有映射$\phi_i:A_i\to A_i$成立，这定义相关均衡（correlated equilibrium, CE）。
2. 在有限行动集上，CE条件等价于对每对$a_i,a_i'\in A_i$要求$\sum_{\boldsymbol{a}_{-i}} \mu(a_i,\boldsymbol{a}_{-i}) \bigl[ u_i(a_i,\boldsymbol{a}_{-i}) - u_i(a_i',\boldsymbol{a}_{-i}) \bigr] \geq0$它把“收到$a_i$建议后改成$a_i'$”的条件收益比较乘上收到该建议的概率，因此$\mu(A_i=a_i)=0$时无需另外定义条件概率。
3. 三行动共同收益矩阵以等概率推荐对角组合：遵从收益0，任一事先固定偏离的收益为-1/3，所以是CCE；第1方收到A后改C可得1，所以不是CE。与后面的二行动协调例共同说明偏离的信息时机和相关随机化的职责。
4. 矩阵博弈中的联合分布也需要与各人的边缘分布区分。收益差来自行动间的相关性，并非某个参与者改变了单独的混合概率。

#### 7.3.5 合作分配下的偏离与稳定

主要内容：按贡献分得收益的成员仍可能退出：若某个联盟自行合作得到的总收益更多，联盟成员就有共同拒绝分配的理由。收益不能转移时，本节还会在可行收益前沿上按分歧点选择协商结果；这是另一项分配选择任务，不能用它代替联盟不阻挡条件。

论证与表述逻辑：

1. 命题（Nash乘积的存在、唯一性与Pareto性质）：设$U$非空、紧且凸，并存在$\widehat{\boldsymbol{u}}\in U$满足$\widehat{\boldsymbol{u}}>\boldsymbol{d}$。若每位参与者的效用与分歧收益同时作正仿射变换$u_i'=a_i u_i+b_i$、$d_i'=a_i d_i+b_i$，其中$a_i>0$，变换后的解正是$\boldsymbol{u}^{\star\prime}=(a_i u_i^\star+b_i)_{i=1}^n$。
2. 推导：个体可接受集合$K=U\cap\{\boldsymbol{u}:\boldsymbol{u}\geq\boldsymbol{d}\}$非空且紧，乘积目标连续，所以最大值能够达到。严格可行点$\widehat{\boldsymbol{u}}$的乘积为正，而任何至少一个坐标等于相应$d_i$的点乘积为零，因此任一最优解都严格满足$\boldsymbol{u}>\boldsymbol{d}$。在这个正增益区域，最大化乘积等价于最大化$F(\boldsymbol{u})=\sum_{i=1}^{n}\log(u_i-d_i)$每个对数项在其坐标上严格凹，故$F$在正增益区域严格凹。
3. 至此，单方策略偏离、依建议改动和联盟退出都有了各自的比较条件。要研究调整以后会不会回到附近、长期会不会停下来，还需要明确下一轮怎样更新。

### 7.4 策略的多方演化与稳定

主要内容：把同时、依次和梯度等更新规则写成策略序列，检查均衡附近的稳定性以及长期收敛或循环。

论证与表述逻辑：

1. 更新规则与策略序列：用$t$表示一局内的物理时间，用$k=0,1,\ldots$表示策略更新轮次。第$k$轮的联合策略为$\boldsymbol\sigma^{(k)}$，该轮温度轨迹若需同时标明两种索引，可写成$x_t^{(k)}$。
2. 均衡邻域内的扰动与稳定：对确定的联合映射$F$，先检查候选均衡$\boldsymbol\theta^\star$是否满足$F(\boldsymbol\theta^\star)=\boldsymbol\theta^\star$。
3. 长期更新的极限与循环：双加热器的响应矩阵给出了收缩，所以误差递推能证明策略收敛。匹配硬币的响应仍然可以精确求出，但对抗收益会使双方依次追逐新的最佳行动。

#### 7.4.1 更新规则与策略序列

主要内容：用$t$表示一局内的物理时间，用$k=0,1,\ldots$表示策略更新轮次。第$k$轮的联合策略为$\boldsymbol\sigma^{(k)}$，该轮温度轨迹若需同时标明两种索引，可写成$x_t^{(k)}$。

论证与表述逻辑：

1. 两方的同时最佳响应使用同一个旧组合：$\sigma_1^{(k+1)}\in\operatorname{BR}_1(\sigma_2^{(k)}), \qquad \sigma_2^{(k+1)}\in\operatorname{BR}_2(\sigma_1^{(k)})$若有并列最优，这只是集合值规则，还须声明怎样选择响应。
2. 精确响应可能代价很高。若第$i$方策略由$\boldsymbol\theta_i\in C_i$参数化、$C_i$非空闭凸，且收益对该参数可微，可采用$\boldsymbol\theta_i^{(k+1)} =\Pi_{C_i}\left( \boldsymbol\theta_i^{(k)} +\eta_i^{(k)} \nabla_{\boldsymbol\theta_i}u_i(\boldsymbol\theta^{(k)}) \right)$这是收益梯度上升；若写成本$J_i=-u_i$，符号改为下降。
3. 两方加热的一步模型使更新次序可以直接计算。固定$x=0,r_1=r_2=2$、$\lambda_1=\lambda_2=1$，把每轮重新选择的一步输入写成$\boldsymbol u^{(k)}=(u_1^{(k)},u_2^{(k)})^\top$，而非局内输入$u_{i,t}$。

#### 7.4.2 均衡邻域内的扰动与稳定

主要内容：对确定的联合映射$F$，先检查候选均衡$\boldsymbol\theta^\star$是否满足$F(\boldsymbol\theta^\star)=\boldsymbol\theta^\star$。

论证与表述逻辑：

1. 在此前提下，稳定问的是初始微小偏差会不会一直小，渐近稳定还要求偏差最终趋零。
2. 固定反馈下的状态稳定条件是$|0.8-k_1-k_2|<1$，其中$k_i$为反馈增益；上述策略更新的条件却由响应矩阵或梯度步长决定。

#### 7.4.3 长期更新的极限与循环

主要内容：双加热器的响应矩阵给出了收缩，所以误差递推能证明策略收敛。匹配硬币的响应仍然可以精确求出，但对抗收益会使双方依次追逐新的最佳行动。

论证与表述逻辑：

1. 梯度小步也不能普遍消除对抗导致的旋转。
2. 定义（演化稳定策略）：设对称双人博弈中使用策略$\boldsymbol p$对阵$\boldsymbol q$的收益为$U(\boldsymbol p,\boldsymbol q)=\boldsymbol p^\top\boldsymbol A\boldsymbol q$。策略$\boldsymbol p^\star$是演化稳定策略（evolutionarily stable strategy, ESS），若对每个$\boldsymbol q\ne\boldsymbol p^\star$，存在$\bar\varepsilon(\boldsymbol q)>0$，使所有$0<\varepsilon<\bar\varepsilon(\boldsymbol q)$都满足$U(\boldsymbol p^\star,(1-\varepsilon)\boldsymbol p^\star+\varepsilon\boldsymbol q) > U(\boldsymbol q,(1-\varepsilon)\boldsymbol p^\star+\varepsilon\boldsymbol q)$。
3. 逐轮策略是$\boldsymbol\sigma^{(k)}$，某个点的收敛是$\|\boldsymbol\sigma^{(k)}-\boldsymbol\sigma^\star\|\to0$；接近均衡集合仅要求到该集合的距离趋零，若集合不止一点，两者不同。

### 7.5 策略的多方累积表现

主要内容：用固定比较策略定义累计遗憾，讨论投影更新、局部遗憾到整局保证，以及平均策略的行为结论。

论证与表述逻辑：

1. 固定比较策略下的累计差距：以下采用损失越小越好的约定。给定前$K$轮的损失函数，分别累计每一个固定行动在这些轮次中的损失，再取最小值。
2. 基于投影更新的累计保证：每轮损失可以不同，因此朝当轮下降方向更新后，下一轮损失仍可能增加。累计保证需要另一项递推：把每轮损失差与到同一个固定比较点的距离变化联系起来，距离项跨轮相加后可以消去。
3. 基于局部遗憾的整局保证：多步计划为每一个可能遇到的信息集指定行动，完整计划数随决策位置迅速增长。如果能在各信息集分别控制局部遗憾，再汇总成整局遗憾，就可以避免直接枚举所有计划。
4. 累计保证与平均策略表现：累计遗憾控制许多轮次的总收益差，要把它转成一个候选策略的均衡误差，还需指定怎样平均。一般和博弈用联合行动的经验分布保留同轮相关性；两人零和博弈可利用收益对各方策略分别线性的性质，控制平均策略的鞍点间隙。

#### 7.5.1 固定比较策略下的累计差距

主要内容：以下采用损失越小越好的约定。给定前$K$轮的损失函数，分别累计每一个固定行动在这些轮次中的损失，再取最小值。

论证与表述逻辑：

1. 若$[R_{\mathrm{ext}}^{(K)}]_+/K\to0$，称该序列无外部遗憾，即平均每轮损失渐近不高于任何固定行动。
2. 定义（内部遗憾）：在同一行动损失序列下，内部遗憾（internal regret）允许把每次实际选择$a$的轮次统一替换成另一行动$b$，对应差距为$R_{a\to b}^{(K)} =\sum_{k=1}^K\mathbb I\{a^{(k)}=a\} [\ell^{(k)}(a)-\ell^{(k)}(b)]$对所有$(a,b)\in A\times A$计算该量，其最大正部称为内部遗憾。
3. 控制所有这类差距，表示在知道“原本要选$a$”以后，也没有持续更好的统一替换。对任意固定$b$，外部比较差距等于$\sum_aR_{a\to b}^{(K)}$；故有限行动下无内部遗憾蕴含无外部遗憾，反向一般不成立。

#### 7.5.2 基于投影更新的累计保证

主要内容：每轮损失可以不同，因此朝当轮下降方向更新后，下一轮损失仍可能增加。累计保证需要另一项递推：把每轮损失差与到同一个固定比较点的距离变化联系起来，距离项跨轮相加后可以消去。

论证与表述逻辑：

1. 命题（在线投影次梯度的外部遗憾）：若$D=0$，则$C$只有一个点；若$G=0$，次梯度不等式说明每轮差值都不大于零。两种退化情形的遗憾上界均为零，无需使用这个步长公式。
2. 推导：当$D,G>0$时，对右侧关于$\eta$配平即得$DG\sqrt{K}$；退化情形按定理后的说明处理。
3. 若只观察抽中的行动损失，通常无法直接取得完整损失向量。可构造估计量，但须声明探索概率、条件无偏性和二阶矩界；期望界与高概率界也要分别推导。

#### 7.5.3 基于局部遗憾的整局保证

主要内容：多步计划为每一个可能遇到的信息集指定行动，完整计划数随决策位置迅速增长。如果能在各信息集分别控制局部遗憾，再汇总成整局遗憾，就可以避免直接枚举所有计划。

论证与表述逻辑：

1. 信息集上的反事实收益比较：若局部差距乘上当前自身到达概率，一个目前很少访问的位置几乎得不到纠正；将来改变上游行动后，它却可能变得重要。下面暂时去掉自身前缀概率，保留对手与机会权重，为之后比较任意完整替代策略准备可重用的局部量。
2. 完全回忆下的局部遗憾汇总：各信息集的局部差距已定义，下一步是表达一份完整替代策略能增加多少收益。对手与机会的到达权重保留在局部量中，本人到达权重则改用这份替代策略的前缀概率。

##### 7.5.3.1 信息集上的反事实收益比较

主要内容：若局部差距乘上当前自身到达概率，一个目前很少访问的位置几乎得不到纠正；将来改变上游行动后，它却可能变得重要。下面暂时去掉自身前缀概率，保留对手与机会权重，为之后比较任意完整替代策略准备可重用的局部量。

论证与表述逻辑：

1. 定义（反事实价值）：给定上述联合行为策略及到达权重，参与者$i$在信息集$I$采取行动$a\in A(I)$的反事实价值（counterfactual value）定义为$v_i^{\boldsymbol{\sigma}}(I,a) = \sum_{h\in I} \pi_{-i}^{\boldsymbol{\sigma}}(h) \sum_{z\succeq ha} \pi^{\boldsymbol{\sigma}}(ha,z)u_i(z)$信息集当前策略的反事实价值为$v_i^{\boldsymbol{\sigma}}(I) = \sum_{a\in A(I)} \sigma_i(a\mid I) v_i^{\boldsymbol{\sigma}}(I,a)$。
2. 在均衡牌面策略下，参与者2的信息集包含高牌质询与低牌质询两个节点。
3. 在第$k$轮扩展式博弈中，联合策略记为$\boldsymbol{\sigma}^{(k)}$。
4. 牌面例中反事实加权和除以正的到达质量才变成条件均值；一般反事实权重删去本人到达因素，不能无条件与实际到达后的条件期望互换。零概率到达时比值公式不可用，策略给定的反事实加权和仍有定义。

##### 7.5.3.2 完全回忆下的局部遗憾汇总

主要内容：各信息集的局部差距已定义，下一步是表达一份完整替代策略能增加多少收益。对手与机会的到达权重保留在局部量中，本人到达权重则改用这份替代策略的前缀概率。

论证与表述逻辑：

1. 命题（CFR的反事实遗憾分解）：在有限完全回忆扩展式博弈中，$R_i^{(K)} \leq \sum_{I\in\mathcal{I}_i} R_{i,+}^{(K)}(I)$。
2. 推导：固定替代行为策略$\widetilde{\sigma}_i$。证明先在一轮中把整局偏离逐层拆开，再对轮次求和。为看清拆分发生在哪里，对$h\in I$定义当前策略在行动$a$后的条件续局收益$q_i^{(k)}(h,a) = \sum_{z\succeq ha} \pi^{\boldsymbol{\sigma}^{(k)}}(ha,z)u_i(z),$并以$\widetilde q_i^{(k)}(h,a)$表示对手和机会仍采用$\boldsymbol{\sigma}_{-i}^{(k)}$，而参与者$i$从$ha$以后采用$\widetilde{\sigma}_i$时的同一数值，即$\widetilde q_i^{(k)}(h,a) = \sum_{z\succeq ha} \pi^{(\widetilde{\sigma}_i,\boldsymbol{\sigma}_{-i}^{(k)})}(ha,z) u_i(z)$当前策略从$h$出发的续局收益为$q_i^{(k)}(h)=\sum_b\sigma_i^{(k)}(b\mid I)q_i^{(k)}(h,b)$。
3. 有限树与有界终局收益保证可以为各信息集选择有限的$\Delta_I$。若信息集本身改变、遗忘破坏完全回忆，或采样值存在未控制的偏差，须重新检查分解与局部算法，不能只引用CFR名称。

#### 7.5.4 累计保证与平均策略表现

主要内容：累计遗憾控制许多轮次的总收益差，要把它转成一个候选策略的均衡误差，还需指定怎样平均。一般和博弈用联合行动的经验分布保留同轮相关性；两人零和博弈可利用收益对各方策略分别线性的性质，控制平均策略的鞍点间隙。

论证与表述逻辑：

1. 一般和条件下的经验分布保证：若所有参与者的平均正外部遗憾趋零，有限联合单纯形的紧性保证经验分布的每个极限点都满足CCE条件，也保证其到CCE集合的距离趋零；未必存在唯一的极限分布。
2. 零和条件下的平均策略保证：矩阵博弈中，$\bar{\boldsymbol x}^{(K)}=K^{-1}\sum_k\boldsymbol x^{(k)}$与$\bar{\boldsymbol y}^{(K)}=K^{-1}\sum_k\boldsymbol y^{(k)}$仍在各自单纯形内。

##### 7.5.4.1 一般和条件下的经验分布保证

主要内容：若所有参与者的平均正外部遗憾趋零，有限联合单纯形的紧性保证经验分布的每个极限点都满足CCE条件，也保证其到CCE集合的距离趋零；未必存在唯一的极限分布。

论证与表述逻辑：

1. 若每个有向替换$a_i\to b_i$的平均内部遗憾至多$\varepsilon_i$，那么对任意映射$\phi_i:A_i\to A_i$，有$\begin{aligned} &\mathbb E_{\widehat\mu^{(K)}}[ u_i(\phi_i(A_i),\boldsymbol A_{-i})-u_i(\boldsymbol A)]\\ &\qquad=\frac1K\sum_{a_i\in A_i}R_{a_i\to\phi_i(a_i)}^{(K)} \leq |A_i|\varepsilon_i \end{aligned}$这里的$R$已改写为收益约定。
2. 保留联合相关性确实必要。经验分布是CE。
3. 若算法控制的是期望损失遗憾，而这里使用抽样行动，还须估计两者之间的随机误差；每轮独立抽样也不消除跨轮共同变化产生的相关性。

##### 7.5.4.2 零和条件下的平均策略保证

主要内容：矩阵博弈中，$\bar{\boldsymbol x}^{(K)}=K^{-1}\sum_k\boldsymbol x^{(k)}$与$\bar{\boldsymbol y}^{(K)}=K^{-1}\sum_k\boldsymbol y^{(k)}$仍在各自单纯形内。

论证与表述逻辑：

1. 行为策略一般须按本人到达概率加权，不能逐信息集随意等权；各轮本人到达权重相同等特殊情形可以等权。完全回忆保证本人行动前缀一致，据此恢复平均实现权重，再由双方外部遗憾界推出平均策略鞍点差距。
2. 行为策略不能在每个信息集直接做普通算术平均。某轮中一个信息集若几乎不会被参与者自己到达，该处局部概率不应与频繁到达轮次具有同样权重。
3. 把平均遗憾转成均衡结论时，还要保留产生平均的联合样本。

### 7.6 本章小结

主要内容：综合信息、收益、均衡与学习动态，区分给定策略的偏离条件、实际更新轨迹和累计表现。

论证与表述逻辑：

1. 多方选择使行动的后果取决于联合策略。信息集先限制每人能够实施的完整计划，到达概率再把这些计划变成各方整局价值。
2. 固定其他策略后可求最佳响应，相互响应形成Nash条件。有限混合均衡的存在由Sperner、Brouwer、闭图近似选择和Kakutani的证明链保证，不意味着唯一、容易计算或能够被任意学习过程找到。
3. 合作价值回答另一类问题。Shapley值在联盟价值已定义后按加入顺序平均边际贡献，并由四项公理唯一刻画；它既不保证成员不退出，也不把预测归因变成因果贡献。
