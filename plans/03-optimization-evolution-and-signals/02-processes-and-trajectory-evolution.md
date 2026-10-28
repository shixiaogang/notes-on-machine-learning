# 卷3《数学准备：优化、动力系统与信号处理》：过程与轨迹演化大纲

正文入口：[part.tex](../../tex/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/part.tex)。以下按实际正文顺序保留内容提要；目标细化方案另见数学基础五卷目标目录。

阅读指引：由状态演化与重复观测进入，先概述动力系统的建模、求解、稳定及观测推断，再介绍随机序列与过程的联合规律、依赖、采样、偏差和收敛；区分有限预算概率界与长期极限。

## 第7章 动力系统

正文：[01-action-and-state.tex](../../tex/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/01-action-and-state.tex)。

章首主线：从同样加热量在不同初温下产生不同后继温度，引出用状态保存历史作用的需要；承接前章的行动响应，说明逐次行动的作用须先累计为轨迹。本章给定更新规律、输入序列及所需噪声分布，依次研究状态演化、轨迹与分布求解、收敛、扰动稳定性和观测推断；观测拟合模型的行动解释仍受机制保持与识别条件约束，如何选择行动再交由后续控制与价值优化研究。

### 7.1 状态演化的建模

主要内容：依次建立离散、连续和随机状态更新，明确初值、输入及状态充分性，说明历史依赖何时要求扩充状态。用当前量替代整段历史的前提是该量已概括对未来仍有影响的部分，这一前提在状态充分性处检查。

论证与表述逻辑：

1. 状态、输入与初值的界定：把当前房间温差记作状态，是因为这个模型只需要它和下一段加热量，就能继续计算未来。若历史还通过其他未记录因素起作用，状态就需要扩充。
2. 离散时间下的状态更新：设$\mathcal X$是允许的状态集合，$\mathcal U$是输入集合。一步更新映射$F_t:\mathcal X\times\mathcal U\longrightarrow\mathcal X,\qquad \boldsymbol x_{t+1}=F_t(\boldsymbol x_t,\boldsymbol u_t)$直接规定下一状态。
3. 连续时间下的状态变化：若关注相邻采样时刻之间发生了什么，需要规定瞬时变化率，而不仅是相隔一步的差值。以泄漏记忆为例，冻结左端变化率得到Euler系数$a=1-\lambda\Delta t,b=\Delta t$，再由差商进入$\dot x=-\lambda x+u$。固定同一初值与物理时刻，比较$\Delta t=1$及$0.5$的误差，说明缩小步长改善这一近似；$\lambda>0$且区间输入恒定时，精确系数则为$a=e^{-\lambda\Delta t},b=(1-e^{-\lambda\Delta t})/\lambda$，不要求步长足够小。反推连续参数时，须先约定所用规则、步长及输入单位，单凭$a=0.8$不能唯一决定整个连续模型。
4. 随机扰动下的状态演化：给定相同初温与加热量，开门、风速等未显式建模的作用仍可能改变真实温度。把这些作用表示成过程噪声后，更新公式不再只产生一条确定轨迹，而是把噪声的联合规律转换为状态的联合规律。
5. 历史依赖下的状态表示：另一种构造从希望保留的历史特征出发。例如为一段输入保留平均值与线性趋势，就可把投影坐标当作状态。

#### 7.1.1 状态、输入与初值的界定

主要内容：把当前房间温差记作状态，是因为这个模型只需要它和下一段加热量，就能继续计算未来。若历史还通过其他未记录因素起作用，状态就需要扩充。

论证与表述逻辑：

1. 若同一室温下，不同墙体蓄热会导致不同的下一步温度，室温一个坐标就不再足够，需要加入墙体温度。传感器滞后同样可能需要独立的内部状态。新增室温与墙体温度的双状态教学递推和两条解析轨迹，固定室温初值及加热量，仅改变墙体初值，直接算出不同下一室温，说明为何扩充状态。
2. 把温度递推继续算出$x_4$至$x_6$，并由$x_{t+1}-2=0.8(x_t-2)$说明与平衡值的差距每步乘$0.8$。平衡由系数与输入共同决定；固定系数时改变恒定输入，会移动平衡而不改变偏差的衰减倍率，改变系数则还会改变接近平衡的速度。初始条件规定轨迹从哪里开始，输入规定沿途施加什么作用，演化规律规定这些作用怎样改变状态。输出则是模型对外显示的量。

#### 7.1.2 离散时间下的状态更新

主要内容：设$\mathcal X$是允许的状态集合，$\mathcal U$是输入集合。一步更新映射$F_t:\mathcal X\times\mathcal U\longrightarrow\mathcal X,\qquad \boldsymbol x_{t+1}=F_t(\boldsymbol x_t,\boldsymbol u_t)$直接规定下一状态。

论证与表述逻辑：

1. 线性模型常写为$\boldsymbol x_{t+1}=\boldsymbol A_t\boldsymbol x_t+\boldsymbol B_t\boldsymbol u_t,\qquad \boldsymbol x_t\in\mathbb R^d,\quad \boldsymbol u_t\in\mathbb R^m$它关于状态与输入的联合变量是线性的；固定非零输入后，它关于状态通常是仿射的。
2. 一个可直接计算的模型是带泄漏的记忆：$x_{t+1}=a x_t+b u_t,\qquad x_0\ \text{给定}$温度例对应$a=0.8,b=1$。

#### 7.1.3 连续时间下的状态变化

主要内容：若关注相邻采样时刻之间发生了什么，需要规定瞬时变化率，而不仅是相隔一步的差值。常微分方程（ordinary differential equation, ODE）初值问题写为$\dot{\boldsymbol x}(t)=\boldsymbol f(t,\boldsymbol x(t),\boldsymbol u(t)),\qquad \boldsymbol x(t_0)=\boldsymbol x_0$给定输入后，右侧是作用在当前状态上的向量场。先用单粒子位置、动量更新和势能坡度说明两条方程如何由总能量的不同偏导组织，再给出向量Hamilton表达。

论证与表述逻辑：

1. 将前向Euler明确为冻结左端变化率的近似规则。取$\lambda=0.2,u=0.4$及同一零初值，步长$1$时在$t=5,20$的误差约为$0.08,0.014$；改用步长$0.5$时，输入系数也改为$0.5$，在相同物理时刻分别计算$10,40$步，误差约为$0.038,0.007$。
2. 对区间恒定输入与$\lambda>0$，先令$z=x-u/\lambda$，由$\dot z=-\lambda z$得到平衡偏差的精确指数衰减，再移项求出精确采样系数。指数的一阶展开恢复Euler关系；从离散系数反推时须区分两种规则，并另核对步长与输入缩放。
3. 定义（可分Hamilton系统）：令$\boldsymbol q,\boldsymbol p\in\mathbb R^d$分别为位置与动量，$U$为连续可微的势能，$\boldsymbol M$为对称正定的质量矩阵。可分Hamilton量为$H(\boldsymbol q,\boldsymbol p)=U(\boldsymbol q)+\frac12\boldsymbol p^\top\boldsymbol M^{-1}\boldsymbol p$相应的Hamilton方程为$\dot{\boldsymbol q}=\nabla_{\boldsymbol p}H,\qquad \dot{\boldsymbol p}=-\nabla_{\boldsymbol q}H$。
4. 第一式由动量得到位置速度，第二式由势能坡度得到动量变化。新增同一能量函数$H=(q^2+p^2)/2$下的Hamilton圆周运动与负梯度下降相图，逐项计算能量导数为零与严格负值，区分能量函数和演化方向。

#### 7.1.4 随机扰动下的状态演化

主要内容：给定相同初温与加热量，开门、风速等未显式建模的作用仍可能改变真实温度。把这些作用表示成过程噪声后，更新公式不再只产生一条确定轨迹，而是把噪声的联合规律转换为状态的联合规律。

论证与表述逻辑：

1. 离散时间下的随机状态更新：独立性使$\mathbb P(\boldsymbol x_{t+1}\in A\mid\boldsymbol x_{0:t})=K_t(\boldsymbol x_t,A)$，这才得到当前状态的Markov性质。
2. 连续时间下的随机状态变化：离散噪声可以逐次相加；连续时间的噪声则要按增量尺度选择驱动。Brownian增量在长度$h$的区间上具有$h$阶方差，Poisson驱动记录区间内到达的事件数。

##### 7.1.4.1 离散时间下的随机状态更新

主要内容：独立性使$\mathbb P(\boldsymbol x_{t+1}\in A\mid\boldsymbol x_{0:t})=K_t(\boldsymbol x_t,A)$，这才得到当前状态的Markov性质。

论证与表述逻辑：

1. 常用的线性加性模型为$\boldsymbol x_{t+1}=\boldsymbol A_t\boldsymbol x_t+\boldsymbol B_t\boldsymbol u_t+\boldsymbol w_{t+1}$若$\boldsymbol w_{t+1}\sim\mathcal N(\boldsymbol0,\boldsymbol Q_{t+1})$且独立于初态与其他过程噪声，$K_t(\boldsymbol x,\cdot)=\mathcal N(\boldsymbol A_t\boldsymbol x+\boldsymbol B_t\boldsymbol u_t,\boldsymbol Q_{t+1})$。
2. 相关噪声需要重新检查条件结构。例如$x_{t+1}=a x_t+w_{t+1}$，而$w_{t+1}=\rho w_t+\varepsilon_{t+1}$，其中新$\varepsilon$独立。
3. 温度模型现在恢复为$x_{t+1}=0.8x_t+u_t+w_{t+1},\qquad w_{t+1}\sim\mathcal N(0,0.04)$取各$w_t$相互独立且独立于初态。

##### 7.1.4.2 连续时间下的随机状态变化

主要内容：离散噪声可以逐次相加；连续时间的噪声则要按增量尺度选择驱动。Brownian增量在长度$h$的区间上具有$h$阶方差，Poisson驱动记录区间内到达的事件数。

论证与表述逻辑：

1. 给定漂移规律、噪声幅度与初值，建模任务是规定这些增量如何进入状态。连续时间并不把驱动强行解释成普通时间导数。

#### 7.1.5 历史依赖下的状态表示

主要内容：另一种构造从希望保留的历史特征出发。例如为一段输入保留平均值与线性趋势，就可把投影坐标当作状态。

论证与表述逻辑：

1. 投影固定$t>0$并使用非负权重测度$\mu_t$，输入与基函数取自L^2等价类。有限维子空间中的基线性无关，使Gram二次型成为非零函数的正平方范数，从而保证坐标唯一；$t=0$的退化区间另给初始化。
2. 窗口本身移动时，状态变化不全来自新输入。
3. 所以有限个历史特征不自动形成能独立接续演化的有限维状态；需要额外状态、特别的基与权重，或对边界项作近似。
4. 高阶多项式投影（high-order polynomial projection operators, HiPPO）把历史投影到多项式空间，以随时间更新的投影系数作为状态坐标。它保存哪些历史特征，由窗口、权重和基共同决定；投影误差、演化闭合与扰动稳定性须分别检查，不将逼近误差保证扩张为历史无损保存或递推稳定。

### 7.2 路径的累计运算与状态变换

主要内容：比较输入累计、跳跃与连续随机积分，再讨论状态函数在不同路径上的变化公式。

论证与表述逻辑：

1. 历史输入的累计作用：先保持离散时间。
2. 跳跃路径上的随机积分：离散更新只需说明每一步使用哪些已知量。把更新间隔缩到连续时间后，还须说明被积系数在时间与随机结果的联合空间中是否可测。
3. 连续路径上的随机积分：以下$\boldsymbol W$是在同一滤过下的$m$维标准Brownian运动，分量独立，其增量独立于过去且协方差为时间长度乘$\boldsymbol I_m$。
4. 连续随机演化下的状态函数变换：读数、能量和损失通常是状态的函数。已知状态怎样累计，怎样求这些函数的变化？
5. 跳跃随机演化下的状态函数变换：考虑连续Itô部分加有限活动跳跃的右连续过程$\boldsymbol X_t=\boldsymbol X_0+\int_0^t\boldsymbol b_s\,\mathrm ds +\int_0^t\boldsymbol\sigma_s\,\mathrm d\boldsymbol W_s +\int_0^t\boldsymbol\gamma_s\,\mathrm dN_s,$其中$\boldsymbol\gamma$可预测、在各事件处有限，$\boldsymbol b,\boldsymbol\sigma$满足前述局部可积条件。

#### 7.2.1 历史输入的累计作用

主要内容：先保持离散时间。

论证与表述逻辑：

1. 前两步为$\boldsymbol x_1=\boldsymbol A\boldsymbol x_0+\boldsymbol B\boldsymbol u_0$及$\boldsymbol x_2=\boldsymbol A^2\boldsymbol x_0+\boldsymbol A\boldsymbol B\boldsymbol u_0+\boldsymbol B\boldsymbol u_1$。
2. 用标量$a=1/2,b=c=1,d=0,x_0=0$核对。依次输入$u_0=1,u_1=2,u_2=1$，递推给出$y_0=0,y_1=1,y_2=5/2,y_3=9/4$。
3. 时变系统用有序乘积$\boldsymbol\Phi(t,s)=\boldsymbol A_{t-1}\cdots\boldsymbol A_s\quad(t>s),\qquad \boldsymbol\Phi(s,s)=\boldsymbol I$传播齐次状态，于是$\boldsymbol x_t=\boldsymbol\Phi(t,0)\boldsymbol x_0+ \sum_{\tau=0}^{t-1}\boldsymbol\Phi(t,\tau+1)\boldsymbol B_\tau\boldsymbol u_\tau$若输出为$\boldsymbol C_t\boldsymbol x_t+\boldsymbol D_t\boldsymbol u_t$，对应核为$\boldsymbol K_{t,t}=\boldsymbol D_t,\qquad \boldsymbol K_{t,\tau}=\boldsymbol C_t\boldsymbol\Phi(t,\tau+1)\boldsymbol B_\tau\quad(\tau<t)$它依赖两个绝对时刻，通常不只依赖滞后$t-\tau$，所以线性仍在，平移不变性却已消失。

#### 7.2.2 跳跃路径上的随机积分

主要内容：离散更新只需说明每一步使用哪些已知量。把更新间隔缩到连续时间后，还须说明被积系数在时间与随机结果的联合空间中是否可测。连续累计同时遍历时间与随机结果，需要联合可测性；事件幅度又必须在同次新事件前可用，以此分开引入渐进可测与可预测条件。

论证与表述逻辑：

1. 一个过程$H$适应，表示每个$H_t$对$\mathcal F_t$可测。若对每个$T$，$(t,\omega)\mapsto H_t(\omega)$在$[0,T]\times\Omega$上对$\mathcal B([0,T])\otimes\mathcal F_T$可测，则称它渐进可测。
2. 左极限不是无关紧要的记号。例如单位幅度事件有$\int_0^t N_{s-}\,\mathrm dN_s=\frac{N_t(N_t-1)}2,\qquad \sum_{\tau_j\leq t}N_{\tau_j}=\frac{N_t(N_t+1)}2$右侧第二个和使用了事件后的计数，两者相差$N_t$。

#### 7.2.3 连续路径上的随机积分

主要内容：以下$\boldsymbol W$是在同一滤过下的$m$维标准Brownian运动，分量独立，其增量独立于过去且协方差为时间长度乘$\boldsymbol I_m$。Brownian增量无法按普通导数或有限变差路径累计，但独立增量允许均方误差相加，因此从简单过程的增量和进入均方延拓。从左右端点累计的非零差别出发，引出对称取样所需的二次协变差修正；先声明连续半鞅对象，再说明Stratonovich约定与普通链式法则的关系。区分以连续路径$W$为被积函数的普通时间积分与以$W$为积分器的随机积分；无限总变差妨碍一般Stieltjes构造，但不否定光滑确定性被积函数的特殊路径积分。

论证与表述逻辑：

1. 对可预测$H$，若$\mathbb E\int_0^T H_t^2\,\mathrm dt<\infty$，用简单可预测过程在该范数下逼近，等距关系使积分序列在$L^2$中为Cauchy序列，从而定义与逼近选择无关的积分。
2. 定义（连续Itô过程）：设$\boldsymbol X_0$对$\mathcal F_0$可测，$\boldsymbol b_t$渐进可测，$\boldsymbol\sigma_t$可预测，且每个有限$T$上$\int_0^T(\|\boldsymbol b_t\|+\|\boldsymbol\sigma_t\|_{\mathrm F}^2)\,\mathrm dt<\infty$几乎必然。过程$\boldsymbol X_t=\boldsymbol X_0+\int_0^t\boldsymbol b_s\,\mathrm ds +\int_0^t\boldsymbol\sigma_s\,\mathrm d\boldsymbol W_s$称为连续Itô过程。漂移积分有有限变差，随机积分是连续局部鞅。
3. 积分约定可以由Brownian平方直接辨认：$W_{t_{i+1}}^2-W_{t_i}^2 =2W_{t_i}\Delta W_i+(\Delta W_i)^2$求和并回用二次变差，左端点和趋于$(W_T^2-T)/2$，右端点和趋于$(W_T^2+T)/2$。

#### 7.2.4 连续随机演化下的状态函数变换

主要内容：读数、能量和损失通常是状态的函数。已知状态怎样累计，怎样求这些函数的变化？先说明单位Brownian平方增量和依概率趋于时间，再给一般Itô状态的二次协变差$\int\sigma\sigma^	op\,ds$；$X=2W$产生$4t$，据此解释二阶修正而不丢失扩散系数。新增等分网格下的解析量级图，由独立高斯增量得到Brownian平方和均值1、均方偏差$2/n$，并与光滑路径平方和$1/n$对照；区分随机累计量及其矩。

论证与表述逻辑：

1. 命题（Itô公式）：若要对等式直接取期望，还须漂移项可积，且随机被积项满足例如$\mathbb E\int_0^T\|\nabla f^\top\boldsymbol\sigma_t\|^2\,\mathrm dt<\infty$；局部鞅本身不保证期望为零。
2. 先说明关键估计，以免把二阶项当作形式记忆规则。对有界连续适应系数，局部化后的Taylor展开中，漂移平方和的期望为$O(|\pi|)$，漂移与随机项乘积和的$L^1$范数为$O(|\pi|^{1/2})$；这里$|\pi|$为分割的最大间距。
3. 例如$f(x)=x^2$给出$W_T^2=2\int_0^T W_s\,\mathrm dW_s+T,\qquad \int_0^T W_s\,\mathrm dW_s=(W_T^2-T)/2$常数系数则有$\int_0^T c\,\mathrm dW_s=cW_T$。

#### 7.2.5 跳跃随机演化下的状态函数变换

主要内容：考虑连续Itô部分加有限活动跳跃的右连续过程$\boldsymbol X_t=\boldsymbol X_0+\int_0^t\boldsymbol b_s\,\mathrm ds +\int_0^t\boldsymbol\sigma_s\,\mathrm d\boldsymbol W_s +\int_0^t\boldsymbol\gamma_s\,\mathrm dN_s,$其中$\boldsymbol\gamma$可预测、在各事件处有限，$\boldsymbol b,\boldsymbol\sigma$满足前述局部可积条件。

论证与表述逻辑：

1. 若把$\nabla f^\top\mathrm d\boldsymbol X$统一写在前面，则还须显式加上$\sum_{\tau_j\leq t} [f(\tau_j,\boldsymbol X_{\tau_j})-f(\tau_j,\boldsymbol X_{\tau_j-}) -\nabla f(\tau_j,\boldsymbol X_{\tau_j-})^\top\Delta\boldsymbol X_{\tau_j}]$它不是只有二阶的近似，而是扣掉已计入一阶项后的全部有限差。
2. 令$X=N$、$f(x)=x^2$，每次事件使平方增加$2N_{s-}+1$，所以$N_t^2=\int_0^t(2N_{s-}+1)\,\mathrm dN_s =2\int_0^tN_{s-}\,\mathrm d\widetilde N_s +\widetilde N_t+2\lambda\int_0^tN_s\,\mathrm ds+\lambda t$于是$\mathbb E N_t^2=(\lambda t)^2+\lambda t$。

### 7.3 状态轨迹与分布的求解

主要内容：分别求确定轨迹、随机轨迹和状态分布，再以时间离散化近似原问题，区分演化求解与观测推断。

论证与表述逻辑：

1. 随机扰动下的初值轨迹求解：前面的随机积分累计给定系数；现在让系数随未知状态变化，便要寻找与累计结果相容的整条轨迹。给定初值和同一条噪声驱动后，轨迹能否被唯一确定？
2. 给定初始分布下的状态分布求解：逐路径的积分式不一定最适合回答“某时刻落在何处”的概率问题。线性模型可传播少量矩，一般模型则要传播分布对测试函数的作用。
3. 离散化条件下的轨迹求解：已知轨迹存在唯一，不代表能写出解析式。记从$t_n$到$t_{n+1}=t_n+h$的精确流为$\varphi_{t_{n+1},t_n}$，数值方法以可计算的一步映射$\Psi_{h,t_n}$近似它。

#### 7.3.1 离散时间下的初值轨迹求解

主要内容：给定初值和离散更新后计算轨迹，比较一般逐步递推与仿射结构支持的并行组合。

论证与表述逻辑：

1. 先沿时间应用更新规则，说明一次输入和初态如何确定后继。
2. 在仿射情形中把多个更新写成可结合的复合运算，再说明并行扫描改变执行依赖而不改变所求轨迹。

##### 7.3.1.1 基于逐步递推的轨迹求解

主要内容：把给定输入吸收进$F_t^{\boldsymbol u}(\boldsymbol x)=F_t(\boldsymbol x,\boldsymbol u_t)$，前两步为$\boldsymbol x_1=F_0^{\boldsymbol u}(\boldsymbol x_0),\qquad \boldsymbol x_2=F_1^{\boldsymbol u}\bigl(F_0^{\boldsymbol u}(\boldsymbol x_0)\bigr)$一般状态是有序复合$\boldsymbol x_t=(F_{t-1}^{\boldsymbol u}\circ\cdots\circ F_0^{\boldsymbol u})(\boldsymbol x_0)$。

论证与表述逻辑：

1. 泄漏模型可进一步展开：$x_t=a^t x_0+\sum_{j=0}^{t-1}a^{t-1-j}b u_j$证明从$t=0$的空和开始。
2. 取独立于温度任务的泄漏例$a=1/2,b=1,x_0=0$。仅在第零步输入$u_0=1$时，$x_1=1,x_2=1/2,x_3=1/4$；若$u_0=u_1=1$，则$x_2=3/2$，其中$1/2$来自旧输入，$1$来自新输入。

###### 段：指数递归平均的记忆与方差

把泄漏更新写成指数移动平均，利用仿射递推展开区分初始权重与观测权重；零初值的权重归一化会改变具有先验意义的初值。由旧输入按$(1-\alpha)^k$衰减算出精确衰减步数，说明$1/\alpha$只在小权重时近似成立。在固定真值、独立同方差噪声及平方可积独立初值下推导初始化偏差、方差递推与极限$\alpha\sigma^2/(2-\alpha)$；持续线性变化的真值产生滞后偏差，相关噪声须保留协方差项。对区间保持输入精确积分一阶ODE，得到不等间隔权重$\alpha_n=1-e^{-\Delta t_n/\tau}$，固定物理时间尺度而非步数。

##### 7.3.1.2 基于并行扫描的仿射轨迹求解

主要内容：逐步递推沿时间产生一条串行依赖链。如果每步都是仿射映射，一整段更新仍可压成同样大小的仿射映射，就能先合并这些映射再求各个中间状态。始终称仿射复合，偏移项参与合并，不能用线性复合名称掩盖非零平移项。

论证与表述逻辑：

1. 下传时，节点接收其区间之前已经完成的累计映射$p$。左孩子继续接收$p$；若左块的总映射是$L$，右孩子就接收$L\circ p$。
2. 总工作量统计所有节点执行的合并次数，计算深度统计最长依赖链上的合并次数。$T$步形成的平衡树有$O(T)$个节点、$O(\log T)$层，上下两阶段在每个节点只做常数次合并，同层互不依赖的节点可同时计算。
3. 扫描保留时间次序。若$g_1(\boldsymbol x)=\operatorname{diag}(2,1)\boldsymbol x$、$g_2(\boldsymbol x)=\boldsymbol x+(1,0)^\top$，则$(g_2\circ g_1)(\boldsymbol0)=(1,0)^\top,\qquad (g_1\circ g_2)(\boldsymbol0)=(2,0)^\top$这两个结果说明结合律不能换成交换律。

#### 7.3.2 连续时间下的初值轨迹求解

主要内容：先建立连续初值问题的存在、唯一和延拓条件，再利用线性结构求出初值与输入的作用。

论证与表述逻辑：

1. 从局部条件讨论轨迹能否定义及是否唯一，检查解何时可继续延伸。
2. 在线性模型中使用状态转移与输入累计表达轨迹，区分解析表达成立与数值计算的后续问题。

##### 7.3.2.1 初值约束下的轨迹存在与延拓

主要内容：一个“几乎处处给出斜率”的公式，要能恢复整条曲线，必须排除没有被导数记录的奇异变化。为此采用绝对连续曲线，而非任意连续曲线。连续曲线不必由其几乎处处导数恢复，要求初值加可积速度累计等于曲线自身，才使微分与积分表达对应；区分该曲线性质与前章测度间的零集条件。

论证与表述逻辑：

1. 引理（Grönwall积分估计）：设$e$为$[a,T]$上非负连续函数，$b$为非负可积函数。更一般地，若右侧另有$\int_a^t r(s)\,\mathrm ds$，其中$r\geq0$可积，则$e(t)\leq c\,\mathrm e^{\int_a^t b} +\int_a^t r(s)\,\mathrm e^{\int_s^t b}\,\mathrm ds$。
2. 推导：令$E(t)=c+\int_a^t[b(s)e(s)+r(s)]\,\mathrm ds$，则$e\leq E$，且$E'\leq bE+r$几乎处处成立。乘以绝对连续的积分因子$\exp(-\int_a^t b)$，使用乘积法则并从$a$积分到$t$，得$E(t)\mathrm e^{-\int_a^t b} \leq c+\int_a^t r(s)\mathrm e^{-\int_a^s b}\,\mathrm ds$再乘回积分因子并用$e\leq E$即可；取$r=0$得到第一式。
3. 若$\|\boldsymbol g(t,\boldsymbol x)\|\leq b(t)\|\boldsymbol x\|+r(t)$，其中$b,r$在每个有限时间区间可积，积分方程与此引理给出有限的状态上界。

##### 7.3.2.2 线性演化下的轨迹求解

主要内容：连续时间对应的时不变方程是$\dot{\boldsymbol x}(t)=\boldsymbol A\boldsymbol x(t)+\boldsymbol B\boldsymbol u(t)$对固定有限方阵$\boldsymbol A$，矩阵指数满足$\frac{\mathrm d}{\mathrm dt}\mathrm e^{t\boldsymbol A} =\boldsymbol A\mathrm e^{t\boldsymbol A}=\mathrm e^{t\boldsymbol A}\boldsymbol A$，且$\mathrm e^{t\boldsymbol A}$的逆为$\mathrm e^{-t\boldsymbol A}$。

论证与表述逻辑：

1. 时变系数需要连续时间的传播算子。
2. 定义（状态转移矩阵）：对连续矩阵函数$\boldsymbol A(t)$，状态转移矩阵$\boldsymbol\Phi(t,s)$是满足$\partial_t\boldsymbol\Phi(t,s)=\boldsymbol A(t)\boldsymbol\Phi(t,s),\qquad \boldsymbol\Phi(s,s)=\boldsymbol I$的矩阵值解。
3. 一般不能令$\boldsymbol\Phi(t,s)=\exp(\int_s^t\boldsymbol A(r)\,\mathrm dr)$。

#### 7.3.3 随机扰动下的初值轨迹求解

主要内容：前面的随机积分累计给定系数；现在让系数随未知状态变化，便要寻找与累计结果相容的整条轨迹。给定初值和同一条噪声驱动后，轨迹能否被唯一确定？

论证与表述逻辑：

1. 定义（Itô随机微分方程与强解）：在给定的通常滤过概率空间上，设$\boldsymbol W$为$m$维Brownian运动，$\boldsymbol X_0$为$\mathcal F_0$可测初值。给定联合Borel可测系数$\boldsymbol b:[0,T]\times\mathbb R^d\to\mathbb R^d$、$\boldsymbol\sigma:[0,T]\times\mathbb R^d\to\mathbb R^{d\times m}$，Itô随机微分方程的扩散形式为$\mathrm d\boldsymbol X_t=\boldsymbol b(t,\boldsymbol X_t)\,\mathrm dt +\boldsymbol\sigma(t,\boldsymbol X_t)\,\mathrm d\boldsymbol W_t$解是满足局部可积条件的连续适应过程，使$\boldsymbol X_t=\boldsymbol X_0+\int_0^t\boldsymbol b(s,\boldsymbol X_s)\,\mathrm ds +\int_0^t\boldsymbol\sigma(s,\boldsymbol X_s)\,\mathrm d\boldsymbol W_s$以概率$1$对所有$t$同时成立。若解适应于初值和给定驱动的历史所生成、完成并取右连续版本的滤过，则称为强解；它不另外使用随机信息。
2. 弱解允许概率空间、驱动和过程一起作为待求对象，但它们必须满足同样的驱动联合条件、初值分布及积分方程。路径唯一性比较同一空间、同一初值和同一驱动上的两个解，要求它们不可区分，即几乎必然在所有时刻相同。

##### 7.3.3.1 随机初值问题的存在与唯一性

主要内容：为证明状态相关的随机积分方程有解，可以反复将上一条候选轨迹代入被积系数。相邻候选的误差需要在整个有限时段上一同控制；Itô等距只给出固定终点的二阶误差，鞅最大不等式将它扩展到时段内的最大波动。

论证与表述逻辑：

1. 命题（SDE强解的存在唯一性）：设$\boldsymbol W$在通常滤过下为标准Brownian运动，$\boldsymbol X_0\in L^2(\mathcal F_0)$。
2. 推导：在短区间$[a,a+h]$固定平方可积初值$\boldsymbol\xi$，取连续适应过程的空间，范数为$\|\boldsymbol Z\|_{\mathcal S^2}^2 =\mathbb E\sup_{a\leq t\leq a+h}\|\boldsymbol Z_t\|^2$，过程按不可区分等价。这是完备空间：Cauchy列可选子列几乎必然一致收敛，极限连续且适应，再用范数Cauchy性质得到$\mathcal S^2$收敛。定义$(\mathcal T\boldsymbol Z)_t=\boldsymbol\xi+\int_a^t\boldsymbol b(s,\boldsymbol Z_s)\,\mathrm ds +\int_a^t\boldsymbol\sigma(s,\boldsymbol Z_s)\,\mathrm d\boldsymbol W_s$Borel系数与连续适应过程的复合渐进可测；增长界、Cauchy--Schwarz、Itô等距和最大不等式使$\mathcal T$映回该空间。
3. 在两次事件间解扩散方程，在$\tau_j$处设$\boldsymbol X_{\tau_j}=\boldsymbol X_{\tau_j-} +\boldsymbol\gamma(\tau_j,\boldsymbol X_{\tau_j-})$。

##### 7.3.3.2 线性随机演化下的轨迹求解

主要内容：线性结构把“系数依赖解”的难点拆开。

论证与表述逻辑：

1. 标量Ornstein--Uhlenbeck（OU）过程把泄漏记忆与持续噪声放在一起：$\mathrm dX_t=-\lambda X_t\,\mathrm dt+\sigma\,\mathrm dW_t,\qquad\lambda>0$由$\mathrm d(\mathrm e^{\lambda t}X_t)= \sigma\mathrm e^{\lambda t}\,\mathrm dW_t$得$X_t=\mathrm e^{-\lambda t}X_0+ \sigma\int_0^t\mathrm e^{-\lambda(t-s)}\,\mathrm dW_s$若$X_0=x_0$为常数，第二项为零均值高斯，因而$X_t\sim\mathcal N(\mathrm e^{-\lambda t}x_0, \sigma^2(1-\mathrm e^{-2\lambda t})/(2\lambda))$。

#### 7.3.4 给定初始分布下的状态分布求解

主要内容：逐路径的积分式不一定最适合回答“某时刻落在何处”的概率问题。线性模型可传播少量矩，一般模型则要传播分布对测试函数的作用。

论证与表述逻辑：

1. 线性演化下的均值与协方差求解：随机积分为零均值、与初值独立，故$\boldsymbol m_t&=\boldsymbol\Phi(t,0)\boldsymbol m_0+\int_0^t\boldsymbol\Phi(t,s)\boldsymbol c_s\,\mathrm ds,\\ \boldsymbol P_t&=\boldsymbol\Phi(t,0)\boldsymbol P_0\boldsymbol\Phi(t,0)^\top +\int_0^t\boldsymbol\Phi(t,s)\boldsymbol G_s\boldsymbol G_s^\top\boldsymbol\Phi(t,s)^\top\,\mathrm ds$这里积分中的$\boldsymbol G_s\boldsymbol G_s^\top$是确定性矩阵。
2. 一般演化下的分布与密度求解：设确定性系数与适当的解唯一性使$\boldsymbol X$成为Markov过程。要知道分布怎样变化，可先观察任意光滑“读数”$\varphi(\boldsymbol X_t)$的短时期望。

##### 7.3.4.1 线性演化下的均值与协方差求解

主要内容：随机积分为零均值、与初值独立，故$\boldsymbol m_t&=\boldsymbol\Phi(t,0)\boldsymbol m_0+\int_0^t\boldsymbol\Phi(t,s)\boldsymbol c_s\,\mathrm ds,\\ \boldsymbol P_t&=\boldsymbol\Phi(t,0)\boldsymbol P_0\boldsymbol\Phi(t,0)^\top +\int_0^t\boldsymbol\Phi(t,s)\boldsymbol G_s\boldsymbol G_s^\top\boldsymbol\Phi(t,s)^\top\,\mathrm ds$这里积分中的$\boldsymbol G_s\boldsymbol G_s^\top$是确定性矩阵。

论证与表述逻辑：

1. OU过程的初值只需平方可积并独立于驱动，就有$\mathbb E X_t&=\mathrm e^{-\lambda t}\mathbb E X_0, \\ \operatorname{Var}(X_t)&=\mathrm e^{-2\lambda t}\operatorname{Var}(X_0) +\frac{\sigma^2}{2\lambda}(1-\mathrm e^{-2\lambda t})$均值衰减；当$\sigma\neq0$时，方差趋于严格正值。

##### 7.3.4.2 一般演化下的分布与密度求解

主要内容：设确定性系数与适当的解唯一性使$\boldsymbol X$成为Markov过程。要知道分布怎样变化，可先观察任意光滑“读数”$\varphi(\boldsymbol X_t)$的短时期望。新增稳态OU与零速度概率流ODE的解析对照图，明确初态与Brownian驱动独立：两者共享标准正态边缘，但跨时协方差分别衰减和保持1，故匹配边缘仍不能确定路径联合规律。

论证与表述逻辑：

1. 定义（Itô扩散的生成元）：记$\mathbb E_{t,\boldsymbol x}$为从时刻$t$的状态$\boldsymbol x$出发的期望。对属于算子定义域的测试函数，生成元定义为$(\mathcal L_t\varphi)(\boldsymbol x) =\lim_{h\downarrow0} \frac{\mathbb E_{t,\boldsymbol x}\varphi(\boldsymbol X_{t+h})-\varphi(\boldsymbol x)}h$对连续系数的扩散，令$\boldsymbol a=\boldsymbol\sigma\boldsymbol\sigma^\top$；在极限与期望可交换时，Itô公式给出$\mathcal L_t\varphi=\boldsymbol b^\top\nabla\varphi+ \tfrac12\operatorname{tr}(\boldsymbol a\nabla^2\varphi)$。
2. 从积分Itô公式取条件期望，除以$h$再令$h\downarrow0$，即得最后一式。例如取光滑紧支撑$\varphi$，并使系数在相关区域有界，可以先局部化来核对该极限。
3. 若终点分布已知或便于采样，可以从终点出发沿反方向生成路径。概率流ODE只匹配每个时刻的边缘密度；要恢复相邻时刻的随机反向条件规律，则需要时间反演的SDE。

###### 段：由条件路径构造边缘速度

从绝对连续、可测且速度期望可积的随机路径出发，定义给定当前状态的速度条件均值。对紧支测试函数依次使用路径链式法则、Fubini与条件期望，得到无密度也成立的弱连续性方程；密度逐点形式与ODE传播相同边缘另需正则性和适定条件。直线端点插值提供可采样的速度目标，有限二阶矩下平方损失分解说明回归的总体最优解是边缘速度；条件路径为直线不代表ODE轨迹为直线，也不证明端点耦合最优。

#### 7.3.5 离散化条件下的轨迹求解

主要内容：已知轨迹存在唯一，不代表能写出解析式。记从$t_n$到$t_{n+1}=t_n+h$的精确流为$\varphi_{t_{n+1},t_n}$，数值方法以可计算的一步映射$\Psi_{h,t_n}$近似它。

论证与表述逻辑：

1. 基于一般数值离散的轨迹求解：显式Euler法在一步内使用当前斜率：$\widehat{\boldsymbol x}_{n+1} =\widehat{\boldsymbol x}_n+h\boldsymbol f(t_n,\widehat{\boldsymbol x}_n)$这里已把给定输入吸收进$\boldsymbol f$。
2. 基于精确线性离散的轨迹求解：前面的数值规则近似瞬时变化率，线性方程却允许在整段区间上求出精确转移。为使输入积分可算，假设$[t_n,t_n+h)$内$\boldsymbol u(t)=\boldsymbol u_n$。
3. 基于几何离散的保守轨迹求解：保守方程的数值计算除了接近状态，还要检查精确演化保持的几何关系。先沿Hamilton方程求出能量和体积的变化，再据此构造离散映射；保持某种结构不等于每一步都精确，也不自动保证任意步长稳定。
4. 基于随机离散的有限时域轨迹模拟：固定$T$，取$t_k=kh$、$n=T/h$为整数，初值$\widehat{\boldsymbol X}_0=\boldsymbol X_0$。

##### 7.3.5.1 基于一般数值离散的轨迹求解

主要内容：显式Euler法在一步内使用当前斜率：$\widehat{\boldsymbol x}_{n+1} =\widehat{\boldsymbol x}_n+h\boldsymbol f(t_n,\widehat{\boldsymbol x}_n)$这里已把给定输入吸收进$\boldsymbol f$。

论证与表述逻辑：

1. 示例（连续稳定与数值稳定不是一回事）：对$\dot x=-\lambda x+u$，其中$\lambda>0$且$u$恒定，精确一步为$x(t+h)=\mathrm e^{-\lambda h}x(t) +\frac{1-\mathrm e^{-\lambda h}}{\lambda}u$Euler一步为$\widehat x_{n+1}=(1-\lambda h)\widehat x_n+hu$。
2. 对齐次泄漏递推，当$1<h\lambda<2$，数值状态交替变号但幅值缩小；当$h\lambda>2$，它交替增长。有恒定输入时，这一判断作用于相对平衡点的偏差，原状态不必在零的两侧交替。若同一系统包含衰减很快与变化很慢的方向，显式方法可能为压住快方向而被迫采用远小于慢变化尺度的步长，这就是刚性带来的主要计算困难。

##### 7.3.5.2 基于精确线性离散的轨迹求解

主要内容：前面的数值规则近似瞬时变化率，线性方程却允许在整段区间上求出精确转移。为使输入积分可算，假设$[t_n,t_n+h)$内$\boldsymbol u(t)=\boldsymbol u_n$。

论证与表述逻辑：

1. 为使输入积分可算，假设$[t_n,t_n+h)$内$\boldsymbol u(t)=\boldsymbol u_n$。
2. 精确性针对区间内保持不变的输入，不表示真实输入在区间内任意变化时也精确。
3. 输入保持误差与计算矩阵指数的数值误差仍可能存在，只是没有Euler式的时间截断误差。

###### 段：连续随机模型的精确离散

在常系数、区间固定输入、独立Brownian驱动下，由线性SDE的积分解得到精确采样转移，过程协方差为$\int_0^h e^{r\bm A}\bm G\bm G^\top e^{r\bm A^\top}\,\mathrm dr$；高斯且独立的新增噪声不要求初始状态高斯。位置—速度的连续白加速度模型给出$h^3/3,h^2/2,h$三项；每段保持一个独立随机加速度幅度则给出$h^4/4,h^3/2,h^2$及秩一协方差。两者的随机假设、量纲与秩不同，采样间隔变化时不能互换或固定协方差。

##### 7.3.5.3 基于几何离散的保守轨迹求解

主要内容：保守方程的数值计算除了接近状态，还要检查精确演化保持的几何关系。先沿Hamilton方程求出能量和体积的变化，再据此构造离散映射；保持某种结构不等于每一步都精确，也不自动保证任意步长稳定。由一对位置动量扰动的有向面积扩展到多对共轭坐标的双线性配对，再定义辛形式及其保持条件，说明仅有能量或总体积信息不足。

论证与表述逻辑：

1. 精确演化的能量保持：若$H$连续可微、不显含时间，且Hamilton方程的解在所考察区间存在，则$H(\boldsymbol q(t),\boldsymbol p(t))=H(\boldsymbol q(0),\boldsymbol p(0))$。 因此轨迹被限制在初始能量面上，而不是向能量极小值下降。若$H$显含时间，同一计算只给出$\mathrm dH/\mathrm dt=\partial_tH$。
2. 精确演化的辛结构与体积保持：能量只给轨迹上的标量限制，仍未说明一小团相邻初态怎样变形。为比较方向之间的关系，取相空间坐标$\boldsymbol z=(\boldsymbol q^\top,\boldsymbol p^\top)^\top$及前述矩阵$\boldsymbol J$。 反向推断却不成立。在$(q_1,q_2,p_1,p_2)$坐标下，$\operatorname{diag}(2,1,1,1/2)$的行列式为$1$，但它把第一对位置动量的面积乘以$2$，第二对乘以$1/2$，不保持标准辛形式。
3. 离散演化的结构保持：对于可分Hamilton量，势能子系统保持位置、只改变动量；动能子系统保持动量、只改变位置。 所以可逆、辛、体积保持与数值稳定分别需要检查。将这类轨迹用于随机采样时，能量误差还需接受校正，不能把几何积分器直接当作精确采样器。

##### 7.3.5.4 基于随机离散的有限时域轨迹模拟

主要内容：固定$T$，取$t_k=kh$、$n=T/h$为整数，初值$\widehat{\boldsymbol X}_0=\boldsymbol X_0$。

论证与表述逻辑：

1. Poisson驱动须另生成$\Delta N_k\sim\operatorname{Pois}(\lambda h)$，并按驱动假设与Brownian增量独立。

### 7.4 演化与计算序列的收敛

主要内容：区分长时间行为、步长缩小、随机近似和双时间尺度的极限，分别检查状态、计算轨迹与时间平均的收敛。

论证与表述逻辑：

1. 长时间演化下的状态极限：考虑局部Lipschitz自治方程$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$。满足$\boldsymbol f(\boldsymbol x^\star)=\boldsymbol0$的状态称为平衡点。以下性质均要求所涉及初值的解对全部$t\geq0$存在。
2. 步长缩小下的轨迹逼近：固定真实方程、初值和有限时域，改变数值网格的步长$h$。确定性计算比较网格状态与精确轨迹；随机计算可以使用同一噪声比较状态，也可以只比较测试函数的期望。
3. 随机近似下的迭代序列收敛：有些递推状态不是房间温度，而是希望逐步求出的参数。设未知均值为$\mu$，目标是解平均方程$h(\theta)=\mathbb E[Y-\theta]=\mu-\theta=0$每次只能得到一个含噪观测，仍可沿观测建议的方向作小步移动。
4. 双时间尺度下的迭代序列收敛：承接未知均值$\mu$，先以两个算法变量满足$u+v\approx\mu$为具体任务，让$u$快速估计剩余部分$\mu-v$，让$v$缓慢调整两者的分配。由慢变量改变快变量的目标，引出冻结慢变量的近似分析，再给出两组步长的一般递推与条件。
5. 长时间采样下的分布与平均收敛：给定一张目标分布，可以设计演化规律，使长时间模拟产生用于积分的相关样本。需要检查两步：目标是否被演化保持，以及从实际初态出发能否接近它。

#### 7.4.1 长时间演化下的状态极限

主要内容：考虑局部Lipschitz自治方程$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$。满足$\boldsymbol f(\boldsymbol x^\star)=\boldsymbol0$的状态称为平衡点。以下性质均要求所涉及初值的解对全部$t\geq0$存在。先分别提出初值小误差始终小、最终消失和具有指数速度三个问题，再用对邻域全部初值的条件定义稳定性。正定与非增先限制子水平集，有界性还需适当有界区域与解的延拓；旋转系统的恒定能量反例说明非增不能推出到最低点，严格下降和LaSalle不变集条件分别使用。

论证与表述逻辑：

1. 定义（平衡点与稳定性）：考虑局部Lipschitz自治方程$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$。满足$\boldsymbol f(\boldsymbol x^\star)=\boldsymbol0$的状态称为平衡点。以下性质均要求所涉及初值的解对全部$t\geq0$存在。平衡点在Lyapunov意义下稳定，是指对每个$\varepsilon>0$，存在$\delta>0$，使$\|\boldsymbol x(0)-\boldsymbol x^\star\|<\delta$蕴含$\|\boldsymbol x(t)-\boldsymbol x^\star\|<\varepsilon$对全部$t\geq0$成立。同时稳定且有局部吸引性称为渐近稳定。若存在$r,C,\alpha>0$，对上述$r$邻域内全部初值和$t\geq0$都有$\|\boldsymbol x(t)-\boldsymbol x^\star\|_2 \leq C\mathrm e^{-\alpha t}\|\boldsymbol x(0)-\boldsymbol x^\star\|_2,$则称为局部指数稳定。若同一估计对全部初值成立，则称为全局指数稳定。
2. 离散时间把$t\geq0$换成非负整数，平衡条件换成$F(\boldsymbol x^\star)=\boldsymbol x^\star$，指数因子可写成$q^t$，其中$0<q<1$。
3. 定义（Lyapunov函数）：对$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$，若上述正定候选还满足$\dot V(\boldsymbol x):=\nabla V(\boldsymbol x)^\top\boldsymbol f(\boldsymbol x)\leq0$，则称其为该邻域内的Lyapunov函数；若非零点处严格小于零，则称为严格Lyapunov函数。
4. 离散方程相应检查$V(F(\boldsymbol x))-V(\boldsymbol x)$。正定性使“小能量”确实限制所有状态方向，非增性才保证轨迹不能穿越更高的能量边界。

##### 7.4.1.1 平衡邻域内的状态极限

主要内容：对已经定义的平衡点，吸引性直接问邻域内的轨迹是否回到该点。温度模型的零输入偏差满足$e_{t+1}=0.8e_t$，因而$e_t=0.8^t e_0\to0$；连续模型$\dot e=-\lambda e$、$\lambda>0$则给出$e(t)=e^{-(t-t_0)\lambda}e(t_0)\to0$。

论证与表述逻辑：

1. 一般非线性方程未必有解析式。下降函数仅有非正导数时，还需检查轨迹是否能停留在较大的零导数集合中。

##### 7.4.1.2 不变区域内的极限集合

主要内容：机械能常只在某些方向上直接耗散，导致$\dot V=0$的集合远大于平衡点。这时应问：轨迹能否一直留在这个集合中？

论证与表述逻辑：

1. 命题（LaSalle不变性原理）：设自治向量场$\boldsymbol f$局部Lipschitz，$\Omega$紧且正向不变，$V$在包含$\Omega$的开邻域上为$C^1$，并有$\dot V\leq0$。令$E=\{\boldsymbol x\in\Omega:\dot V(\boldsymbol x)=0\}$，$M$为$E$中最大不变集，则从$\Omega$出发的每条轨迹满足$\operatorname{dist}(\boldsymbol x(t),M)\to0$。
2. 推导：紧性排除有限时间逃逸，也使$\omega(\boldsymbol x_0)$非空且紧。沿轨迹的$V$单调不增且有下界，故趋于$v_\infty$。对极限点$\boldsymbol z=\lim_j\boldsymbol x(t_j)$，连续性给出$V(\boldsymbol z)=v_\infty$。
3. 能量非增先限制活动区域，动力学再排除不能持续停留的零导数点。把整个$E$直接称为“最终状态”，会丢掉LaSalle论证中最关键的一步。

#### 7.4.2 步长缩小下的轨迹逼近

主要内容：固定真实方程、初值和有限时域，改变数值网格的步长$h$。确定性计算比较网格状态与精确轨迹；随机计算可以使用同一噪声比较状态，也可以只比较测试函数的期望。

论证与表述逻辑：

1. 确定性演化下的离散误差：设$\boldsymbol f$在包含精确轨迹与Euler轨迹的区域内关于状态具有Lipschitz常数$L$，精确解二阶连续可微，且$\|\ddot{\boldsymbol x}(t)\|_2\leq M$。从精确初值出发，若$t_n=t_0+nh\leq t_0+T$，则$L>0$时$\|\widehat{\boldsymbol x}_n-\boldsymbol x(t_n)\|_2 \leq\frac{Mh}{2L}(\mathrm e^{LT}-1)$$L=0$时相应上界为$MTh/2$。
2. 同一噪声下的随机轨迹误差：同一次噪声实现会产生一条真轨迹和一条数值轨迹。要比较两条路径的状态误差，网格算法必须使用真轨迹的同一驱动，即令$\sqrt h\,\boldsymbol\varepsilon_k=\boldsymbol W_{t_{k+1}}-\boldsymbol W_{t_k}$。
3. 测试函数下的随机模拟误差：若只查询终点读数的平均，目标变成测试函数$\varphi$在真终点和数值终点下的期望差，不必把两条路径逐次配对。

##### 7.4.2.1 确定性演化下的离散误差

主要内容：设$\boldsymbol f$在包含精确轨迹与Euler轨迹的区域内关于状态具有Lipschitz常数$L$，精确解二阶连续可微，且$\|\ddot{\boldsymbol x}(t)\|_2\leq M$。从精确初值出发，若$t_n=t_0+nh\leq t_0+T$，则$L>0$时$\|\widehat{\boldsymbol x}_n-\boldsymbol x(t_n)\|_2 \leq\frac{Mh}{2L}(\mathrm e^{LT}-1)$$L=0$时相应上界为$MTh/2$。

论证与表述逻辑：

1. 命题（Euler法的有限时域全局误差）：设$\boldsymbol f$在包含精确轨迹与Euler轨迹的区域内关于状态具有Lipschitz常数$L$，精确解二阶连续可微，且$\|\ddot{\boldsymbol x}(t)\|_2\leq M$。从精确初值出发，若$t_n=t_0+nh\leq t_0+T$，则$L>0$时$\|\widehat{\boldsymbol x}_n-\boldsymbol x(t_n)\|_2 \leq\frac{Mh}{2L}(\mathrm e^{LT}-1)$$L=0$时相应上界为$MTh/2$。
2. 推导：Taylor公式给出$\boldsymbol x(t_{n+1})=\boldsymbol x(t_n)+h\boldsymbol f(t_n,\boldsymbol x(t_n))+\boldsymbol\tau_n$，其中$\|\boldsymbol\tau_n\|_2\leq Mh^2/2$。记$\boldsymbol e_n=\widehat{\boldsymbol x}_n-\boldsymbol x(t_n)$，相减并用Lipschitz条件得$\|\boldsymbol e_{n+1}\|_2\leq(1+Lh)\|\boldsymbol e_n\|_2+Mh^2/2$从$\boldsymbol e_0=\boldsymbol0$展开，$\|\boldsymbol e_n\|_2\leq(Mh^2/2)\sum_{j=0}^{n-1}(1+Lh)^j$。$L>0$时求几何和，并用$(1+Lh)^n\leq\mathrm e^{Lnh}\leq\mathrm e^{LT}$，即得所述界；$L=0$时直接使用$nh\leq T$。
3. 这也是离散Grönwall估计的一个具体推导。局部$O(h^2)$经约$T/h$步累计成为全局$O(h)$，而动力学决定这些误差随后放大多少。

##### 7.4.2.2 同一噪声下的随机轨迹误差

主要内容：同一次噪声实现会产生一条真轨迹和一条数值轨迹。要比较两条路径的状态误差，网格算法必须使用真轨迹的同一驱动，即令$\sqrt h\,\boldsymbol\varepsilon_k=\boldsymbol W_{t_{k+1}}-\boldsymbol W_{t_k}$。

论证与表述逻辑：

1. 估计机制与存在性证明相连。

##### 7.4.2.3 测试函数下的随机模拟误差

主要内容：若只查询终点读数的平均，目标变成测试函数$\varphi$在真终点和数值终点下的期望差，不必把两条路径逐次配对。

论证与表述逻辑：

1. 弱阶较高不说明两条样本轨迹更接近。例如独立生成的两个同分布终点对所有可积测试函数期望完全相同，彼此状态距离却不为零。

#### 7.4.3 随机近似下的迭代序列收敛

主要内容：有些递推状态不是房间温度，而是希望逐步求出的参数。设未知均值为$\mu$，目标是解平均方程$h(\theta)=\mathbb E[Y-\theta]=\mu-\theta=0$每次只能得到一个含噪观测，仍可沿观测建议的方向作小步移动。

论证与表述逻辑：

1. 固定步长的均值例在递推前定义$e_t=\theta^{(t)}-\mu$和$v_t=\operatorname{Var}(e_t)$；确定初值与独立同分布噪声给出稳态方差$\alpha\sigma^2/(2-\alpha)$，说明减小步长降低波动也延缓响应。
2. 引理（固定有限链的加权Poisson分解）：设$P$为固定的有限不可约非周期核，参数递推$\theta^{(t+1)}=\theta^{(t)}+\alpha_tH(\theta^{(t)},Z_t)$始终位于紧集$K$，$H$在$K$上一致有界且关于参数一致Lipschitz。特别地，任意向晚期移动的有限算法时间窗上的尾和趋零。
3. 推导：有限不可约非周期链几何收敛，且$\pi q_\theta=0$，所以$g_\theta=\sum_{j=0}^\infty P^jq_\theta$绝对一致收敛，并满足$g_\theta-Pg_\theta=q_\theta$。对$q_\theta-q_{\theta'}$应用相同几何界，得到有限常数$G,L_g$使$|g_\theta(z)|\leq G$、$|g_\theta(z)-g_{\theta'}(z)|\leq L_g|\theta-\theta'|$。
4. 再用标量递推核对平均稳定与噪声条件怎样配合。设$\theta^{(t+1)}=\theta^{(t)}+\alpha_t[b-a\theta^{(t)}+\xi_{t+1}]$，$a>0$，噪声为条件均值零且条件二阶矩不超过$\sigma^2$，初值二阶矩有限。

#### 7.4.4 双时间尺度下的迭代序列收敛

主要内容：把未知均值$\mu$分给两个算法变量，使$u+v$接近$\mu$；$u$快速估计$\mu-v$，$v$缓慢调整分配，再将此关系写成一般的两组递推。算法变量与贯穿温度模型的行动、读数分开说明，避免沿用字母造成角色混淆。

论证与表述逻辑：

1. 在具体分工之后引入快慢步长，要求两组步长各自满足Robbins--Monro条件且$\alpha_t/\beta_t\to0$。快时间上把$\boldsymbol v$暂时固定，得到$\dot{\boldsymbol u}=\boldsymbol g(\boldsymbol u,\boldsymbol v)$；若其稳定平衡为$\boldsymbol u^\star(\boldsymbol v)$，慢时间上再使用$\dot{\boldsymbol v}=\boldsymbol f(\boldsymbol u^\star(\boldsymbol v),\boldsymbol v)$。收敛结论还依赖快慢方程的稳定性、联合迭代有界、噪声矩界和残差条件，尺度分离本身不替代这些假设。
2. 示例（分解同一个未知均值的快慢更新）：若$\mathbb E[Y_{t+1}\mid\mathcal F_t]=\mu$，取$u^{(t+1)}=u^{(t)}+\beta_t(Y_{t+1}-u^{(t)}-v^{(t)}),\qquad v^{(t+1)}=v^{(t)}+\alpha_t(u^{(t)}-v^{(t)})$冻结$v$后，快方程$\dot u=\mu-v-u$的唯一稳定平衡为$u^\star(v)=\mu-v$。
3. 尺度分离没有保证快平衡存在，也没有保证其稳定或全局最优。两组步长同阶时，前面的均值拆分例仍可用联合系统分析，却不能继续使用冻结慢变量的论证。

#### 7.4.5 长时间采样下的分布与平均收敛

主要内容：给定一张目标分布，可以设计演化规律，使长时间模拟产生用于积分的相关样本。需要检查两步：目标是否被演化保持，以及从实际初态出发能否接近它。

论证与表述逻辑：

1. 命题（HMC提议的细致平衡）：若$T$是可微、体积保持的对合，则以概率$\alpha(\boldsymbol z)$移至$T\boldsymbol z$，否则留在$\boldsymbol z$的核，对密度$\rho$满足细致平衡。
2. 推导：接受部分的密度权重为$\rho(\boldsymbol z)\alpha(\boldsymbol z)=\min\{\rho(\boldsymbol z),\rho(T\boldsymbol z)\}$。对任意有界可测函数$g(\boldsymbol z,\boldsymbol z')$，作变量替换$\boldsymbol y=T\boldsymbol z$，由$T^2=I$和单位绝对Jacobian，$\begin{split} &\int g(\boldsymbol z,T\boldsymbol z)\min\{\rho(\boldsymbol z),\rho(T\boldsymbol z)\}\,\mathrm d\boldsymbol z\\ &\quad=\int g(T\boldsymbol y,\boldsymbol y) \min\{\rho(T\boldsymbol y),\rho(\boldsymbol y)\}\,\mathrm d\boldsymbol y . \end{split}$这证明接受部分在交换出发与到达状态后不变。拒绝部分集中在对角线$\boldsymbol z'=\boldsymbol z$，本身对称，两者相加即为细致平衡。
3. 若提议不保持体积，接受比还需Jacobian因子；状态依赖地改变步数或步长，也须重新核对反向提议。实现中的有限精度可逆误差不是上述精确算术证明的一部分。

### 7.5 状态演化的扰动与稳定性

主要内容：比较初值与输入扰动下的轨迹，利用线性谱和Lyapunov方法区分有限时间控制、稳定与误差消退。

论证与表述逻辑：

1. 初值扰动下的轨迹稳定性：前述原点判据通常对应零输入，或把恒定输入下的平衡平移到原点。温度例的恒定$u_t=0.4$对应平衡$2$，误差$e_t=x_t-2$才满足$e_{t+1}=0.8e_t$。
2. 输入扰动下的轨迹稳定性：初值误差只在开始时注入，输入误差可以在每个时刻持续进入。即使无输入偏差会衰减，持续加热偏多仍可能造成非零温差。

#### 7.5.1 初值扰动下的轨迹稳定性

主要内容：前述原点判据通常对应零输入，或把恒定输入下的平衡平移到原点。温度例的恒定$u_t=0.4$对应平衡$2$，误差$e_t=x_t-2$才满足$e_{t+1}=0.8e_t$。

论证与表述逻辑：

1. 要得到衰减，须利用演化方向，而非只限制变化率；线性传播和Lyapunov下降关系分别提供这样的判据。

##### 7.5.1.1 线性演化下的轨迹稳定性

主要内容：离散齐次系统为$\boldsymbol x_{t+1}=\boldsymbol A\boldsymbol x_t,\qquad \boldsymbol x_t=\boldsymbol A^t\boldsymbol x_0$这里用矩阵幂和Jordan分解把长期轨迹问题化成谱的位置；下面对各Jordan块的幂逐项给出长期估计。区分Lyapunov给出的衰减上界与精确模态速率；指数系数约0.38对应时间常数约2.6，减半时间则约为1.8，不能把两者混同。

论证与表述逻辑：

1. 长期演化的谱判据：离散齐次系统为$\boldsymbol x_{t+1}=\boldsymbol A\boldsymbol x_t,\qquad \boldsymbol x_t=\boldsymbol A^t\boldsymbol x_0$这里用矩阵幂和Jordan分解把长期轨迹问题化成谱的位置；下面对各Jordan块的幂逐项给出长期估计。 命题（离散线性系统的渐近稳定性）：在此条件下，原点实际上全局指数稳定。
2. 有限时间的瞬态放大：取$\boldsymbol A=\begin{bmatrix}1/2&K\\0&1/2\end{bmatrix},\qquad K>0$无论$K$多大，谱半径均为$1/2$，而$\boldsymbol A^t= \begin{bmatrix} 2^{-t}&tK\,2^{-(t-1)}\\0&2^{-t} \end{bmatrix}$从$\boldsymbol x_0=(0,1)^\top$出发，第一步即为$(K,1/2)^\top$，欧氏范数可以大幅增长；之后$t2^{-t}\to0$才使状态趋零。 $K\neq0$时，$\boldsymbol A^\top\boldsymbol A\neq\boldsymbol A\boldsymbol A^\top$，矩阵非正规。
3. 同谱的非正规矩阵例显示有限时间放大与长期衰减可以并存；伪谱用同维复矩阵小扰动下所有可能特征值的位置解释，反映谱敏感性，不把谱稳定等同于欧氏范数逐步收缩。

##### 7.5.1.2 非线性演化下的轨迹稳定性

主要内容：非线性系统一般无法通过一个固定矩阵构造全局二次能量，因而需要寻找候选函数。

论证与表述逻辑：

1. 命题（连续时间Lyapunov判据）：设原点为$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$的平衡点，$\boldsymbol f$在其邻域内局部Lipschitz。若该邻域存在$C^1$正定候选$V$且$\dot V\leq0$，则原点稳定；若非零点上$\dot V<0$，则原点局部渐近稳定。若这些条件在$\mathbb R^d$上成立，且$V(\boldsymbol x)\to\infty$当$\|\boldsymbol x\|\to\infty$，则所有解正向全局存在；非增情形给出稳定性，严格下降情形给出全局渐近稳定性。
2. 推导：选足够小的$\varepsilon$使闭球位于适用邻域。球面上的连续正函数$V$有最小值$c_\varepsilon>0$。原点处连续性给出$\delta<\varepsilon$，使$\|\boldsymbol x_0\|<\delta$时$V(\boldsymbol x_0)<c_\varepsilon$。
3. 径向无界性控制的是远处状态，不能用“在原点附近正定”代替。若还能找到$c_1,c_2,c_3>0$使$c_1\|\boldsymbol x\|^2\leq V\leq c_2\|\boldsymbol x\|^2$、$\dot V\leq-c_3\|\boldsymbol x\|^2$，则前述线性方程证明中的积分估计同样给出局部指数衰减。

#### 7.5.2 输入扰动下的轨迹稳定性

主要内容：初值误差只在开始时注入，输入误差可以在每个时刻持续进入。即使无输入偏差会衰减，持续加热偏多仍可能造成非零温差。

论证与表述逻辑：

1. 线性演化下的轨迹响应：若$\|\boldsymbol u(s)\|\leq U$，第二项至多$(M\|\boldsymbol B\|U/\alpha)(1-\mathrm e^{-\alpha(t-t_0)})$。
2. 非线性演化下的轨迹响应：在初值连续依赖的基础上，再允许输入与向量场改变。设两条轨迹都留在同一区域，原向量场关于状态的Lipschitz常数为$L$，关于输入的常数为$L_u$；比较模型沿第二条轨迹的向量场误差至多为$r(s)$。

##### 7.5.2.1 线性演化下的轨迹响应

主要内容：在指数稳定线性演化中，由初值与输入的卷积表达控制状态及两条轨迹的差异，区分暂态消退与持续偏差。

论证与表述逻辑：

1. 先用矩阵指数的衰减界代入常数变易公式，分别估计初值项和输入累计项。
2. 再利用两组解之差仍满足同一线性方程，得到扰动响应；有界持续输入可留下非零稳态，温度模型给出固定输入偏差被放大的具体倍数。

##### 7.5.2.2 非线性演化下的轨迹响应

主要内容：在初值连续依赖的基础上，再允许输入与向量场改变。设两条轨迹都留在同一区域，原向量场关于状态的Lipschitz常数为$L$，关于输入的常数为$L_u$；比较模型沿第二条轨迹的向量场误差至多为$r(s)$。

论证与表述逻辑：

1. 设两条轨迹都留在同一区域，原向量场关于状态的Lipschitz常数为$L$，关于输入的常数为$L_u$；比较模型沿第二条轨迹的向量场误差至多为$r(s)$。
2. Gronwall引理将初值误差、持续输入误差和模型误差合在同一传播界中：$\|\boldsymbol x(t)-\widetilde{\boldsymbol x}(t)\| \leq \mathrm e^{L(t-t_0)}\|\boldsymbol x_0-\widetilde{\boldsymbol x}_0\| +\int_{t_0}^t\mathrm e^{L(t-s)} \bigl(L_u\|\boldsymbol u(s)-\widetilde{\boldsymbol u}(s)\|+r(s)\bigr)\,\mathrm ds$初态误差、输入误差、模型误差因此有不同来源，却都要经过后续动态传播。

### 7.6 基于观测的状态推断

主要内容：给定生成和观测模型后，分别建立预测、滤波、平滑与整条轨迹推断，说明各自允许使用的信息。

论证与表述逻辑：

1. 观测条件下的推断目标：在前面的状态转移$K_t$之外增加观测核$G_t(\boldsymbol x,B)=\mathbb P(\boldsymbol y_t\in B\mid\boldsymbol x_t=\boldsymbol x)$。
2. 基于历史观测的状态预测：若已有截至$t-1$的条件分布$\pi_{t-1}$，全概率公式给出$\pi_{t\mid t-1}(A) =\int K_{t-1}(\boldsymbol x,A)\,\pi_{t-1}(\mathrm d\boldsymbol x)$这是把每个候选旧状态的下一步分布，按其当前可信程度混合。
3. 基于当前及历史观测的状态滤波：预测分布已经汇总旧读数对当前状态的判断。获得当前读数后，各候选状态的权重还要按它们产生这次读数的可能性调整；所求对象仍是同一个物理状态，只是条件信息增加了。
4. 基于完整观测的状态平滑：固定终点$T$后，未来读数也能帮助判断旧状态。关键不是再向前预测，而是把新获得的下一状态分布通过反向条件关系传回去。
5. 基于完整观测的联合轨迹推断：各时刻边缘分布回答“那一刻可能在哪里”，整条路径后验还要回答“这些状态如何一起出现”。

#### 7.6.1 观测条件下的推断目标

主要内容：在前面的状态转移$K_t$之外增加观测核$G_t(\boldsymbol x,B)=\mathbb P(\boldsymbol y_t\in B\mid\boldsymbol x_t=\boldsymbol x)$。

论证与表述逻辑：

1. 记$\mathcal Y_t=\sigma(\boldsymbol y_1,\ldots,\boldsymbol y_t)$，$\mathcal Y_0$为无观测信息。
2. 用无噪二维例核对观测时序：时刻$1$的候选$(1,0)^\top,(0,1)^\top$都有$y_1=1$；随后共同施加已知输入$\boldsymbol u_1=(0.5,0)^\top$，经$\boldsymbol A=\operatorname{diag}(0.5,2)$演化，时刻$2$的候选为$(1,0)^\top,(0.5,2)^\top$，因而$y_2$分别为$1,2.5$。共同输入在候选状态差中抵消，区分来自状态转移把原先看不到的分量差带入后续读数。
3. 下面的一般核公式只要求前述条件独立结构。

#### 7.6.2 基于历史观测的状态预测

主要内容：若已有截至$t-1$的条件分布$\pi_{t-1}$，全概率公式给出$\pi_{t\mid t-1}(A) =\int K_{t-1}(\boldsymbol x,A)\,\pi_{t-1}(\mathrm d\boldsymbol x)$这是把每个候选旧状态的下一步分布，按其当前可信程度混合。

论证与表述逻辑：

1. 例如隐藏状态为$\{0,1\}$，$\pi_0=(0.7,0.3)$，按当前状态为行、下一状态为列的转移矩阵为$\boldsymbol P=\left[\begin{smallmatrix}0.8&0.2\\0.1&0.9\end{smallmatrix}\right]$。
2. 在线性高斯条件下，仿射变换与独立高斯相加保持高斯性，所以$\boldsymbol m_{t\mid t-1} &=\boldsymbol A_{t-1}\boldsymbol m_{t-1\mid t-1}+\boldsymbol B_{t-1}\boldsymbol u_{t-1}, \\ \boldsymbol P_{t\mid t-1} &=\boldsymbol A_{t-1}\boldsymbol P_{t-1\mid t-1}\boldsymbol A_{t-1}^\top+\boldsymbol Q_t$温度第一步为$m_{1\mid0}=0.4,P_{1\mid0}=0.04$：初值已知并不等于未来状态已知。

#### 7.6.3 基于当前及历史观测的状态滤波

主要内容：预测分布已经汇总旧读数对当前状态的判断。获得当前读数后，各候选状态的权重还要按它们产生这次读数的可能性调整；所求对象仍是同一个物理状态，只是条件信息增加了。

论证与表述逻辑：

1. 命题（有限时域Kalman滤波）：在上述独立线性高斯模型与创新协方差可逆条件下，预测与校正公式精确给出$\boldsymbol x_t\mid\mathcal Y_t\sim \mathcal N(\boldsymbol m_{t\mid t},\boldsymbol P_{t\mid t})$，对每个有限$t$成立。
2. 推导：$t=0$时无观测，条件分布就是给定高斯初值。为核对条件化，令$\boldsymbol e=\boldsymbol x_t-\boldsymbol m_{t\mid t-1}-\boldsymbol K_t\boldsymbol r_t$。在$\mathcal Y_{t-1}$条件下，$\operatorname{Cov}(\boldsymbol e,\boldsymbol r_t) =\boldsymbol P_{t\mid t-1}\boldsymbol C_t^\top-\boldsymbol K_t\boldsymbol S_t=\boldsymbol0$。
3. 标量直接观测例用上标$-$、$+$分别表示加入当前读数前的预测与加入后的滤波，$m^\pm,p^\pm$分别为均值与方差。由$K=p^-/(p^-+r)$说明预测与读数怎样加权；独立教学例与温度例各自使用自己的噪声方差，不互换设定。
4. 两种方法都可能遗漏多峰后验。例如零均值对称先验配上$y=x^2+v$，一个明显正的读数可能支持正负两个状态区间。

#### 7.6.4 基于完整观测的状态平滑

主要内容：固定终点$T$后，未来读数也能帮助判断旧状态。关键不是再向前预测，而是把新获得的下一状态分布通过反向条件关系传回去。

论证与表述逻辑：

1. 命题（有限时域RTS平滑）：在有限时域Kalman条件及每个$\boldsymbol P_{t+1\mid t}$可逆条件下，从终点$(\boldsymbol m_{T\mid T},\boldsymbol P_{T\mid T})$向后递推$\boldsymbol m_{t\mid T} &=\boldsymbol m_{t\mid t}+\boldsymbol J_t(\boldsymbol m_{t+1\mid T}-\boldsymbol m_{t+1\mid t}), \\ \boldsymbol P_{t\mid T} &=\boldsymbol P_{t\mid t} +\boldsymbol J_t(\boldsymbol P_{t+1\mid T}-\boldsymbol P_{t+1\mid t})\boldsymbol J_t^\top,$精确给出$\boldsymbol x_t\mid\mathcal Y_T$的高斯均值与协方差。
2. 推导：给定$\boldsymbol x_{t+1}$后，未来状态和观测与更早状态条件独立，因此$P(\mathrm d\boldsymbol x_t\mid\boldsymbol x_{t+1},\mathcal Y_T) =P(\mathrm d\boldsymbol x_t\mid\boldsymbol x_{t+1},\mathcal Y_t)$。全概率公式给出后向因子化$P(\mathrm d\boldsymbol x_t\mid\mathcal Y_T) =\int P(\mathrm d\boldsymbol x_t\mid\boldsymbol x_{t+1},\mathcal Y_t) P(\mathrm d\boldsymbol x_{t+1}\mid\mathcal Y_T)$将一步条件均值对$\boldsymbol x_{t+1}\mid\mathcal Y_T$取期望，塔式性质得到平滑均值公式。全协方差公式分成两项：条件内协方差为$\boldsymbol P_{t\mid t}-\boldsymbol J_t\boldsymbol P_{t+1\mid t}\boldsymbol J_t^\top$，条件均值的协方差为$\boldsymbol J_t\boldsymbol P_{t+1\mid T}\boldsymbol J_t^\top$；相加即得平滑协方差。
3. 标量随机游走教学例沿用$P,Q,R$表示状态与两类噪声方差，并逐步核对算术：由预测方差$P_{1\mid0}=2$得增益$K_1=3/4$，读数$y_1=2$使滤波均值移到$3/2$、滤波方差降为$1/2$；再用$J_0=1/2$回传一半偏差，得平滑均值$3/4$与平滑方差$5/8<1$。比较时固定目标：$x_1$从预测$(0,2)$变为滤波$(3/2,1/2)$，$x_0$从先验$(0,1)$变为吸收$y_1$后的平滑$(3/4,5/8)$，每一对分别表示均值与方差。在时刻$0$不能使用尚未获得的$y_1$；到时刻$1$估计当前$x_1$与回溯$x_0$是两种查询。窗口$T=1$下$x_1$的平滑等于滤波，要展示它再吸收更晚观测的变化，还须增加$y_2$等读数。沿用上述有限时域线性高斯条件，有$\boldsymbol P_{t\mid T}\preceq\boldsymbol P_{t\mid t}$，即滤波协方差减去平滑协方差是半正定矩阵。

#### 7.6.5 基于完整观测的联合轨迹推断

主要内容：各时刻边缘分布回答“那一刻可能在哪里”，整条路径后验还要回答“这些状态如何一起出现”。

论证与表述逻辑：

1. 若损失为$\sum_t\|\boldsymbol x_t-\boldsymbol a_t\|^2$，联合条件均值的各分量就是$\boldsymbol m_{t\mid T}$，因此逐时刻平滑均值同时组成最小化该可加平方损失的路径输出。
2. 本节的精确结论都在有限时域成立。在那里输入才由反馈主动选择，本章一直把$\boldsymbol u_t$当作已给定量。

### 7.7 本章小结

主要内容：用温度模型区分演化规律、过程噪声、真实轨迹与观测噪声，归纳求解、收敛、稳定和推断的职责。

论证与表述逻辑：

1. 同一温度模型中的演化规律、真实轨迹与传感器读数承担不同职责。初值和输入给出一次初值问题；过程噪声使轨迹成为随机对象；观测噪声产生用于推断的记录。
2. 给定规律以后，求解轨迹与求解分布也有不同输出。线性传播把各时刻输入的作用累计为和或积分，仿射复合允许并行扫描。
3. 本章把行动序列视为已经给定。演化模型和状态推断为这些任务提供条件，单靠轨迹求解仍不能决定怎样行动最合适。

## 第8章 随机序列与随机过程

正文：[03-random-sequences-and-processes.tex](../../tex/03-optimization-evolution-and-signals/02-processes-and-trajectory-evolution/03-random-sequences-and-processes.tex)。

相同的单时刻边缘可以来自独立噪声或共享背景，不能单凭单次分布判断重复平均和长期行为。共同随机对象、历史依赖与生成规则提供前提，有限预算的集中与随机积分计算连接到长期极限及整条路径的收敛。

### 8.1 随机序列与过程的表示

主要内容与论证逻辑：主要内容：将单个随机变量扩展为共同定义的变量族，区分有限维联合规律、单条样本路径与随机误差的比较方式。

论证与表述逻辑：以独立噪声、共享背景和累计和说明相同边缘不足以保存依赖；用有限坐标的相容性建立过程规律，用路径版本和正则性约束一次实现，最后先约定后文平方增量和与统计极限需要的收敛和概率阶定义。

#### 8.1.1 共同概率空间上的随机序列与过程

主要内容与论证逻辑：主要内容：随机序列是同一概率空间上的可测映射族；一般索引集给出随机过程。

论证与表述逻辑：先区分固定索引得到的随机变量与固定基础结果得到的实现序列，再比较独立噪声、共同背景读数和累计增量的联合关系。索引可表示轮次、时间或空间，只有解释为时间或算法轮次时才进一步引入历史条件。

#### 8.1.2 基于有限维分布的过程表示

主要内容与论证逻辑：主要内容：通过任意有限坐标的联合分布规定过程，解释投影与重排的相容条件。

论证与表述逻辑：从删去时刻后应得到相同分布进入，构造乘积空间和柱集；说明标准Borel条件，并陈述Kolmogorov扩张定理。明确唯一性属于乘积σ代数，不能由扩张定理直接推出连续路径或时间与基础结果的联合可测性；本处没有重证扩张定理。

#### 8.1.3 基于样本路径的过程表示

主要内容与论证逻辑：主要内容：区分时间索引连续、状态取值连续与路径连续，比较版本、不可区分及Hölder正则性。

论证与表述逻辑：用教学路径图分离时间截面与一次实现；随机尖点例说明逐时刻几乎必然相等不等于整条路径相等。再从短时增量矩界陈述Kolmogorov连续性准则，保留指数端点的限制，并以Brownian增量说明应用方向。

#### 8.1.4 随机误差的收敛与量级

主要内容与论证逻辑：主要内容：先建立随机误差趋小与相对确定尺度的记号，供过程构造和后面的极限证明使用。

论证与表述逻辑：把“误差缩小”分别落实为坏事件概率、逐路径和平均p次误差；分布收敛回接前章的边缘规律比较。这里只给判据，蕴含、反例和极限定理留3.6展开。

###### 段：随机结果的收敛判据

主要内容与论证逻辑：主要内容：定义依概率、几乎必然和L^p收敛，回顾实值依分布收敛。

论证与表述逻辑：逐一写明比较量和概率来源；前三种比较要求共同概率空间，依分布收敛只比较边缘分布，不强求共同实现。

###### 段：随机误差的概率阶

主要内容与论证逻辑：主要内容：定义概率有界、O_P和o_P，并通过除以确定正数列扩展到一般尺度。

论证与表述逻辑：从控制缩放余项的需要引出统一尾概率条件，强调取值每次有限并不等于概率有界；乘积运算与非线性余项的用法在3.6.4证明。

### 8.2 随机序列与过程的依赖关系

主要内容与论证逻辑：主要内容：分别约束重排对称性、给定历史后的状态规律、条件均值和时间平移下的联合规律。

论证与表述逻辑：四种要求针对不同对象，可以同时成立但不能互相代替；从不保留顺序的记录转向有历史的动态记录，再区分机制不变、分布不变和均值不漂移。

#### 8.2.1 序列重排下的交换关系

主要内容与论证逻辑：主要内容：定义有限及无限序列的交换性，以共同随机参数说明交换性并不推出独立性。

论证与表述逻辑：从重排记录不改变联合规律进入；把位置对称性用于无并列分数的秩，说明秩均匀的条件与共形预测的后续入口。没有将交换性代入要求独立乘积的集中证明。

#### 8.2.2 历史条件下的状态依赖

主要内容与论证逻辑：主要内容：用滤过、适应、可预测性和停时表述可用历史，再研究Markov性、时间齐次核、多步转移、平稳分布与细致平衡。

论证与表述逻辑：从当前状态能否概括预测所需历史进入；先限制哪些信息在当步已知，再定义条件分布的Markov等式。用塔式性质证明核复合给出多步转移，区分条件版本的几乎处处意义与核在每个状态上的定义；恒等核和三状态单向循环分别说明保持分布不等于到达分布、平稳不等于细致平衡。

#### 8.2.3 历史条件下的均值关系

主要内容与论证逻辑：主要内容：建立鞅、鞅差、超鞅和次鞅，并解释连续时间版本。

论证与表述逻辑：从新增量给定过去后无平均漂移进入，用公平符号和可预测下注证明累计财富的条件均值保持。分别检查可积性、适应性、噪声条件中心化与信息流；提前揭晓下一符号的扩展滤过给出反例。长期收敛尚需额外条件。

#### 8.2.4 时间平移下的分布关系

主要内容与论证逻辑：主要内容：定义严格平稳与二阶平稳，解释从不变分布启动的齐次Markov链为何平稳。

论证与表述逻辑：先比较完整窗口的联合规律，再把要求减为恒定均值和仅依时间差变化的协方差。奇偶时刻使用不同边缘的独立序列说明二阶平稳不推出严格平稳；联合高斯情形说明何时可以反推。Brownian和随机游走区分过程平稳与增量平稳。

### 8.3 随机序列与过程的生成

主要内容与论证逻辑：主要内容：依次通过增量、转移核、到达计数和高斯协方差生成过程，最后扩展到随机概率测度。

论证与表述逻辑：把上一节对联合规律的约束落到可重复使用的生成规则，分别核对有限维相容性、历史独立性、路径条件和测度的可数可加性。

#### 8.3.1 基于状态转移的随机序列生成

主要内容与论证逻辑：主要内容：比较累计增量和直接抽取下一状态两种逐步生成方式。

论证与表述逻辑：随机游走显示位置共享过去增量；一般核生成允许更广状态空间。一步规律之外，多步边缘与长期平均须分别分析。

##### 8.3.1.1 基于增量累计的随机游走生成

主要内容与论证逻辑：主要内容：定义独立同分布增量的累计和，计算均值、方差和不同时刻的协方差。

论证与表述逻辑：用共享增量解释位置相关；中心化累计和具有鞅关系，当前位置又足以确定下一步条件规律。数值例子说明一次路径不必接近总体平均。

##### 8.3.1.2 基于转移核的Markov链生成

主要内容与论证逻辑：主要内容：通过两状态核生成相关读数，并从状态互达与返回步数提炼不可约性和周期。

论证与表述逻辑：在同一例子中计算平稳质量和从确定初态启动的边缘递推，区别一步转移、几何趋近与已处平稳的解释。

###### 段：状态转移与多步分布

主要内容与论证逻辑：主要内容：转移矩阵为(0.9,0.1;0.2,0.8)的教学链具有平稳质量(2/3,1/3)。

论证与表述逻辑：验证平稳方程后，推导q_(t+1)=0.1+0.7q_t及显式解；从q_0=0计算前两步，说明当前边缘没有立即等于平稳分布。不可约与非周期条件在后文服务于长期结论。

#### 8.3.2 基于到达计数的随机过程生成

主要内容与论证逻辑：主要内容：以Poisson过程统一窗口计数、等待时长、非恒定强度下的首次到达和补偿累计。

论证与表述逻辑：单窗口Poisson边缘不决定过程，必须给出相对于历史的独立增量；从齐次机制扩大到确定强度函数后，重新计算等待规律，再回到补偿增量的条件均值。

###### 段：事件计数与短时跳跃

主要内容与论证逻辑：主要内容：定义相对于指定滤过的齐次Poisson过程和复合Poisson过程。

论证与表述逻辑：从短区间零次、一次、多次到达的概率说明有限活动跳跃；由零计数概率推出指数等待，并用到达时刻密度和无记忆性解释反向构造。复合情形用条件均值与全方差保留事件数本身的随机性。

###### 段：非恒定强度下的首次到达

主要内容与论证逻辑：主要内容：以单位Poisson过程的累计强度时间变换构造非齐次计数，推导首次到达生存概率与密度。

论证与表述逻辑：强度非负且局部可积使有限时间累计强度有限；零计数概率给出生存函数exp(-Λ)，绝对连续性给出几乎处处的密度λexp(-Λ)。累计强度总量有限时保留永不到达的原子质量；线性强度例说明等待不再无记忆，并把同一无事件概率解释为射线透射形式，离散渲染计算留应用卷。

###### 段：平均到达与补偿增量

主要内容与论证逻辑：主要内容：回到齐次计数，减去确定平均趋势得到补偿Poisson鞅，区分实现二次变差与可预测二阶累计。

论证与表述逻辑：独立增量给出条件均值和条件二阶矩，平方展开证明补偿平方再减平均累计仍为鞅。教学图显示减去漂移不会抹平跳跃；复合跳跃和有限可预测系数的积分等距式承接后面的过程积分。

#### 8.3.3 基于高斯规律的随机过程生成

主要内容与论证逻辑：主要内容：由联合高斯有限维规律分别建立独立增量的Brownian模型与一般协方差核的高斯过程。

论证与表述逻辑：均值和协方差确定高斯向量，但核相容性与路径正则性仍需分开核对。

##### 8.3.3.1 独立高斯增量下的布朗路径构造

主要内容与论证逻辑：主要内容：从缩放随机游走说明增量尺度，定义标准Brownian及其滤过条件，研究连续路径和二次变差。

论证与表述逻辑：保留离散累计的均值、方差和独立增量，直接定义连续极限所需性质；函数型极限定理在3.6.7陈述，不由单时刻中心极限定理代替。

###### 段：连续路径与增量尺度

主要内容与论证逻辑：主要内容：建立一维与多维标准Brownian、协方差min(s,t)、缩放规律与路径正则性。

论证与表述逻辑：有限维高斯规律和连续版本条件分别负责构造；额外信息流不能预知增量。固定矩阵混合改变协方差，低秩混合允许退化扩散；时间连续不意味着路径可微。

###### 段：不可微性与二次变差

主要内容与论证逻辑：主要内容：以差商尺度解释粗糙性，用平方增量和计算Brownian的二次变差，并扩展到交叉二次变差。

论证与表述逻辑：先回用收敛和概率阶判据，再由独立增量计算平方和的均值与方差，使网格变细时均方趋于t。与可微路径比较；图只展示计算对象，处处不可微的严格结论仍依赖原文献，差商方差发散本身不充当证明。

##### 8.3.3.2 均值与协方差约束下的高斯过程构造

主要内容与论证逻辑：主要内容：定义一般索引集上的高斯过程和协方差核的半正定条件。

论证与表述逻辑：从独立增量限制转向一般相关曲线，以A+Bx构造可复算例子；有限秩核可能产生奇异协方差。有限维高斯规律不保证连续路径，需回用增量正则性条件。

#### 8.3.4 基于Dirichlet规律的随机概率测度生成

主要内容与论证逻辑：主要内容：将随机对象由数值或参数向量扩大为概率测度，建立随机概率测度与Dirichlet过程。

论证与表述逻辑：回接前章层次模型，再把每个可测区域的质量作为随机变量；有限分割概率的相容性不自动保证每条实现可数可加，存在性回指随机离散测度构造。

###### 段：随机概率测度的有限分割表示

主要内容与论证逻辑：主要内容：在概率测度空间上定义评价σ代数，使每个区域的随机质量均可测。

论证与表述逻辑：先把随机分布投到有限区域概率向量，说明各坐标非负且总和为一；它是以集合为索引的随机对象，不要求索引是时间。

###### 段：相容分割下的Dirichlet过程

主要内容与论证逻辑：主要内容：以任意有限分割服从相应Dirichlet向量定义DP，说明总质量参数、基概率和零参数坐标。

论证与表述逻辑：合并区域使概率和参数同时相加，从而解释相容性；Ferguson的归一化随机质量构造支持标准Borel空间上的存在性，本处不重证。后验、聚类和非参数Bayes算法另有主讲位置。

### 8.4 随机累计量的偏差控制

主要内容与论证逻辑：主要内容：固定累计量、候选函数族及历史相关累计量分别需要单对象、同时性和序贯条件控制。

论证与表述逻辑：固定预算和误差阈值后，逐步改变查询与选择规则；集中控制回答有限预算概率，不用长期极限替代。

#### 8.4.1 单个累计量的偏差控制

主要内容与论证逻辑：主要内容：从独立平均的方差进入，以矩条件与指数矩条件控制尾概率。

论证与表述逻辑：回用前章矩不等式，再利用独立性合成指数矩；范围信息与实际方差信息分别给出Hoeffding和Bernstein尺度。

##### 8.4.1.1 矩条件下的尾概率控制

主要内容与论证逻辑：主要内容：计算独立读数平均的方差，回用Markov和Chebyshev得到误差概率。

论证与表述逻辑：同分布有限方差时得到σ²/(nε²)，相关读数则需保留交叉协方差；没有重复正式定义或证明前章矩不等式。

##### 8.4.1.2 指数矩条件下的累计偏差控制

主要内容与论证逻辑：主要内容：建立Chernoff方法、次高斯条件、Hoeffding引理及不等式、方差敏感的Bernstein界。

论证与表述逻辑：先由指数单调性换成矩母函数，再证明有界变量的指数矩界并独立相乘；Bernstein用二阶矩与幅值控制高阶项。低概率Bernoulli例比较界的数值；重尾情形说明各方法在哪个条件上失效。

#### 8.4.2 候选族累计量的统一偏差控制

主要内容与论证逻辑：主要内容：同时覆盖预先固定的有限候选或无限函数类，处理看过样本后的候选选择。

论证与表述逻辑：从固定函数尾界转到坏事件并集，再使用有限网、随机符号和复杂度处理无限类；可测性、上确界约定与样本依赖必须写入保证。

###### 段：有限候选的联合控制

主要内容与论证逻辑：主要内容：有限函数类的统一误差、经验最优的超额风险，以及随机投影的有限点对距离保持。

论证与表述逻辑：联合界带来log M代价，数值例区分每项95%与全部95%；再证明卡方尾界，对固定点对差联合控制得到Johnson–Lindenstrauss充分维数。点集须在投影前固定，控制的是平方距离，不扩张到事后任造方向。

###### 段：无限候选的统一控制

主要内容与论证逻辑：主要内容：使用有限取值模式、覆盖网和Rademacher/高斯复杂度统一控制无限查询，并给出对称化和收缩论证。

论证与表述逻辑：有限网需验证误差的Lipschitz传递；数据函数转入McDiarmid并在历史控制处补证明。定义复杂度时保留上确界与期望的顺序，证明凸包不增加线性符号复杂度；独立样本副本及交换对称性完成对称化，逐坐标替换证明收缩。线性类得到BR/√n，高斯与符号复杂度只有所证方向的普适比较，坐标向量例排除普适常数反向界。

#### 8.4.3 历史依赖下累计量的偏差控制

主要内容与论证逻辑：主要内容：通过鞅差条件中心化与可预测条件方差分析相关、停止和自适应线性观测。

论证与表述逻辑：独立指数矩乘积改为逐步条件化，再分别处理固定时刻和任意时刻。可预测二次变差与实现平方和承担不同作用，不互换。

###### 段：固定时刻的误差界

主要内容与论证逻辑：主要内容：证明Azuma–Hoeffding，并将独立输入函数逐步揭示为Doob鞅以证明McDiarmid。

论证与表述逻辑：条件Hoeffding界逐步取期望即可合成；数据函数的条件范围由独立输入保证未来积分规律相同，输入依赖时不能只凭坐标有界差沿用结论。

###### 段：任意时刻的同时误差界

主要内容与论证逻辑：主要内容：有界可选停止、无界停止反例、Ville与Freedman界、随机设计下的向量自归一化集中。

论证与表述逻辑：停时指示为可预测使有限和条件均值保持；随机游走击中时间说明无界停时不能直接交换期望。非负指数超鞅给越界控制，Freedman同时限定条件方差预算。对可预测随机特征先验证随机参数指数界，再以高斯混合同时控制各方向；行列式比来自高斯归一化，额外整体可积性与指数界的需求分开。

### 8.5 基于随机采样的积分计算

主要内容与论证逻辑：主要内容：在给定概率规律与积分目标下比较样本平均、方差缩减、未知归一化常数及轨迹换测度。

论证与表述逻辑：固定同一个积分x²在[0,1]上的平均1/3，依次改变抽样位置、辅助贡献和条件内随机性；同时保留均值、方差、支持和可执行性条件。长期一致性和渐近方差在3.6回用大数定律与极限变换证明。

#### 8.5.1 基于独立样本平均的积分计算

主要内容与论证逻辑：主要内容：定义直接蒙特卡洛平均及无偏、有限方差条件。

论证与表述逻辑：由线性性和独立性分别得到均值正确与方差σ_f²/n；固定教学积分的单样本方差为4/45，作为后三种方法的共同基线。

#### 8.5.2 固定积分目标下的方差缩减

主要内容与论证逻辑：主要内容：改变采样规律或每个样本的贡献，比较相同预算下的积分方差。

论证与表述逻辑：保持目标不变并不保证方差降低，须逐项核验支持、权重二阶矩、辅助均值和条件积分所需信息。

##### 8.5.2.1 基于抽样分布的方差缩减

主要内容与论证逻辑：主要内容：建立重要性估计及方差条件，推导固定被积函数下最小二阶矩的理想提议分布。

论证与表述逻辑：q=2x使同一积分的单次方差降到1/72；Cauchy–Schwarz给出q*正比于|f|p。区分整个P对Q绝对连续与只需支配|f|dP；零贡献区域可以不采。理想解常含未知积分或难采密度，混入p保留共同支持也带来实际取舍。

##### 8.5.2.2 基于辅助变量的方差缩减

主要内容与论证逻辑：主要内容：通过已知均值的控制变量调整样本贡献，推导最优固定系数。

论证与表述逻辑：方差二次式给出β*=Cov(f,h)/Var(h)；在同一积分上用h=X得到1/180。若系数由同一批记录估计，须重新分析随机系数，无偏性不自动继承。

##### 8.5.2.3 基于条件平均的方差缩减

主要内容与论证逻辑：主要内容：通过Rao–Blackwell条件平均消去可积分的额外随机性。

论证与表述逻辑：塔式性质保持均值，全方差保证二阶矩下不增方差；命中事件I{U≤X²}的条件均值为X²，单次方差由2/9降到4/45。竖切片教学图解释条件内平均如何保留面积。

#### 8.5.3 未知归一化常数下的积分计算

主要内容与论证逻辑：主要内容：用随机权重比值消去公共归一化常数，并区分方差诊断、截断偏差和重采样随机性。

论证与表述逻辑：分子、分母均随机时不再有直接平均的有限样本无偏结论；通过三点样本同时复算几种调整的不同效果。

###### 段：自归一化权重与比值估计

主要内容与论证逻辑：主要内容：定义在非归一化权重为目标密度比公共倍数时的比值估计。

论证与表述逻辑：归一化消去未知常数，但通常引入有限样本比值偏差；分母须为正，权重不是正确公共倍数时目标也被改变。

###### 段：权重截断、重采样与有效样本量

主要内容与论证逻辑：主要内容：固定三点目标与提议分布，比较原始、截断和重采样贡献。

论证与表述逻辑：截断使均值从0.6降到0.4并降低方差；特定二十粒子样本的多项重采样保持条件均值而增加条件方差。权重ESS仅诊断退化，不等于对所有目标都成立的精确独立样本数，也不同于随机设计自归一化集中。

#### 8.5.4 候选函数族的采样积分误差

主要内容与论证逻辑：主要内容：同一批样本计算并事后选择多个被积函数时，回用整个函数族的统一偏差保证。

论证与表述逻辑：单个固定积分的保证不覆盖数据选择，必须核验函数类可测性、范围及复杂度；无界重要性权重不能直接代入有界函数类结果。

#### 8.5.5 历史依赖观测的轨迹重加权

主要内容与论证逻辑：主要内容：将单次换测度扩大为整段联合观测，写出逐步条件密度比的连乘。

论证与表述逻辑：初始和每步目标核对来源核绝对连续，且权重条件可测和归一化；不预设Markov性。共同初态与环境的离散行动轨迹中，环境因子相消后只剩策略比；环境不同则保留相应比值。有限权重存在不保证长轨迹二阶误差可用。

### 8.6 随机序列与过程的收敛

主要内容与论证逻辑：主要内容：由生成规则和比较方式判断平均、缩放误差、状态规律与整条路径的长期极限。

论证与表述逻辑：先证明随机收敛关系及交换期望所需条件，建立独立样本平均和中心极限，再传递随机比值及非线性变换；最后把独立样本扩到Markov相关平均、状态混合和路径紧性。一般测度弱收敛、Portmanteau、Prokhorov与Lévy均回用前章，不重复陈述。

#### 8.6.1 随机误差的收敛关系

主要内容与论证逻辑：主要内容：比较概率、路径和平均误差收敛，并研究历史均值约束下的鞅极限。

论证与表述逻辑：尾事件反复发生的问题进入Borel–Cantelli，随后用指示函数和事件夹逼证明蕴含；子列判据先于一致可积论证建立，避免原文先用后证。

##### 8.6.1.1 逐次偏差与样本路径的收敛

主要内容与论证逻辑：主要内容：证明Borel–Cantelli两方向、a.s./L^p到概率再到分布的蕴含及依概率收敛的子列判据。

论证与表述逻辑：联合界处理可求和事件，独立性处理概率和发散；固定基础变量的尖峰与独立小概率事件给出反向失败的例子。同分布到随机极限不等于同实现接近。

##### 8.6.1.2 一致尾部控制下的平均误差收敛

主要内容与论证逻辑：主要内容：通过一致可积排除小概率大尖峰承载固定期望，从概率收敛得到L¹收敛。

论证与表述逻辑：子列与Fatou先保证极限可积，再截断并用支配收敛处理有界部分；教学尖峰面积恒为一，说明逐路径趋零仍可能无法交换期望。

##### 8.6.1.3 历史条件均值约束下的序列收敛

主要内容与论证逻辑：主要内容：用上穿论证建立非负超鞅的有限路径极限，并证明二阶矩有界鞅的a.s.与L²收敛及条件期望表示。

论证与表述逻辑：有限上穿排除持续振荡，Fatou排除无穷极限；二阶矩增量正交先给L²柯西，再用最大不等式和可求和坏事件升级到整列路径极限。鞅噪声收敛不代替随机逼近状态的稳定性分析。

#### 8.6.2 重复采样下的平均序列收敛

主要内容与论证逻辑：主要内容：陈述独立同分布且有限一阶绝对矩下的强大数定律，并证明有限方差弱版本。

论证与表述逻辑：将Chebyshev用于平均方差σ²/n即可得到依概率结论，但不能由逐个n的概率界直接声称路径强收敛。强版本的完整证明在原教材，本处说明截断和可求和事件所需步骤，再回到独立带噪读数的平均。

#### 8.6.3 重复采样下的标准化累计偏差序列分布收敛

主要内容与论证逻辑：主要内容：陈述并用特征函数证明独立同分布、有限正方差下的Lindeberg–Lévy中心极限定理。

论证与表述逻辑：零点二阶展开和独立乘积给出标准高斯特征函数极限，回用前章Lévy连续性定理。区分有限样本分布与渐近近似，并说明无限方差、强依赖及变化分布不能直接继承。

#### 8.6.4 随机误差变换后的极限

主要内容与论证逻辑：主要内容：在误差已有极限时，研究随机余项、随机分母及非线性读出的长期波动。

论证与表述逻辑：概率阶先控制余项，连续映射传递极限，Slutsky处理趋常数的随机因子，Delta进一步给出变换后的渐近方差。

##### 8.6.4.1 概率阶运算与随机误差的组合

主要内容与论证逻辑：主要内容：证明依分布收敛推出概率有界，以及o_P(1)乘O_P(1)仍为o_P(1)。

论证与表述逻辑：闭集概率上界控制远尾；先限制概率有界因子，再控制小余项，给出两个坏事件的联合概率界。

##### 8.6.4.2 连续变换与随机因子的极限传递

主要内容与论证逻辑：主要内容：证明连续映射和Slutsky，并将其用于蒙特卡洛、控制变量及自归一化重要性估计。

论证与表述逻辑：a.s.逐路径、概率子列和弱收敛闭集分别传递连续函数；Slutsky先用事件夹逼处理和，再用概率阶处理乘积与比值。对积分改写逐项检查一阶与二阶矩；随机分母最终远离零，得到比值一致性和中心极限方差，但没有消除有限样本偏差。

##### 8.6.4.3 非线性变换后的渐近波动

主要内容与论证逻辑：主要内容：证明一阶Delta方法，以对数变换和退化导数说明尺度及边界。

论证与表述逻辑：先由概率有界得到一致性，再把Taylor余项写成o_P乘O_P并用Slutsky。导数为零时只给退化一阶极限，不可微时不能直接使用该定理。

###### 段：方差稳定化与逆变换偏差

主要内容与论证逻辑：主要内容：由方差函数V(μ)推导g'=1/√V，使样本平均的变换误差具有单位渐近方差；扩展到Poisson与Poisson–Gaussian读数。

论证与表述逻辑：先明确均值内点、正方差和局部可微条件，积分常数不改变误差。Poisson给2√x，Anscombe的3/8来自高阶修正而非一阶Delta；高斯负读数使根号域限制不能省略。对Poisson的Anscombe变换精确推出A⁻¹(EA)=λ−Var(A)/4，区分原始读数的代数互逆与平滑均值后的逆偏差；校正均值映射不意味着任意带估计误差的输出都无偏。

#### 8.6.5 状态转移下的时间平均序列收敛

主要内容与论证逻辑：主要内容：证明有限不可约链的时间占比识别平稳概率，再讨论一般状态空间条件与相关平均的方差。

论证与表述逻辑：几何块尾界保证有限平均返回，强Markov性把游程变为独立同分布；先以Cesàro平均和不可约性建立平稳概率存在唯一，再由游程计数识别极限并控制未完成游程及初始段。周期交替例说明时间平均可收敛而边缘振荡；正Harris常返与可积函数提供一般状态空间入口。平稳初态下展开相关平均方差，区分函数相关ESS和重要性权重ESS，并处理零渐近方差。

#### 8.6.6 状态转移下的分布序列收敛

主要内容与论证逻辑：主要内容：研究从任意初态到平稳规律的总变差收敛、几何遍历和混合时间。

论证与表述逻辑：有限不可约非周期矩阵的其余模态衰减；一般状态需正Harris与非周期条件。回用前章TV而不重复建立距离理论；最坏初态的混合时间与特定观测函数的自相关误差承担不同职责，教学图固定初态条件分别比较。

#### 8.6.7 随机路径的收敛

主要内容与论证逻辑：主要内容：以C空间的一致距离与D空间的J₁时间校正比较路径，建立连续路径紧性与极限识别。

论证与表述逻辑：错时跳跃例可用时间校正完全对齐，窄尖峰例说明有限维极限不足。初值紧性与统一短时模量结合Arzelà–Ascoli构造承载高概率的紧集，再回用Prokhorov并用有限维规律识别极限；跳跃路径需另加J₁紧性条件。最后陈述缩放随机游走到Brownian的Donsker结论，没有把单时刻中心极限定理代作路径证明。

### 8.7 本章小结

主要内容与论证逻辑：主要内容：综合联合规律、历史与路径条件，区分固定预算、候选选择、随机停止、长期平均及整条路径的保证。

论证与表述逻辑：相同边缘不保证相同重复行为；过程的不同依赖条件各自约束不同对象。采样积分在给定规律下借助这些工具计算，但权重存在、有限方差和反变换偏差须分开检查；下一章转向未知观测规律的统计推断。
