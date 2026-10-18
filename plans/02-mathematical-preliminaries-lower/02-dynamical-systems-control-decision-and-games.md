# 卷2《数学准备：概率、因果与决策》：第2部分“演化、控制、决策与博弈”大纲

正文入口：[tex/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/part.tex](../../tex/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/part.tex)。章号按本卷连续编号，以下标题和顺序对应当前入口实际接入的正文。

承接前一部分对行动响应计算与识别的区分，本部分先在更新规律、输入和噪声规律给定时研究状态怎样形成轨迹，再研究观测与执行限制下的策略实现、价值优化和多方响应。若动态规律来自观测拟合，把不同输入下的模拟解释为实际改变行动的后果，仍需检查机制保持与识别条件；给定模型下的轨迹求解不代替这一核验。

## 第6章 动力系统

正文：[01-action-and-state.tex](../../tex/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/01-action-and-state.tex)。

章首主线：从同样加热量在不同初温下产生不同后继温度，引出用状态保存历史作用的需要；承接前章的行动响应，说明逐次行动的作用须先累计为轨迹。本章给定更新规律、输入序列及所需噪声分布，依次研究状态演化、轨迹与分布求解、收敛、扰动稳定性和观测推断；观测拟合模型的行动解释仍受机制保持与识别条件约束，如何选择行动再交由后续控制与价值优化研究。

### 6.1 状态演化的建模

主要内容：依次建立离散、连续和随机状态更新，明确初值、输入及状态充分性，说明历史依赖何时要求扩充状态。用当前量替代整段历史的前提是该量已概括对未来仍有影响的部分，这一前提在状态充分性处检查。

论证与表述逻辑：

1. 状态、输入与初值的界定：把当前房间温差记作状态，是因为这个模型只需要它和下一段加热量，就能继续计算未来。若历史还通过其他未记录因素起作用，状态就需要扩充。
2. 离散时间下的状态更新：设$\mathcal X$是允许的状态集合，$\mathcal U$是输入集合。一步更新映射$F_t:\mathcal X\times\mathcal U\longrightarrow\mathcal X,\qquad \boldsymbol x_{t+1}=F_t(\boldsymbol x_t,\boldsymbol u_t)$直接规定下一状态。
3. 连续时间下的状态变化：若关注相邻采样时刻之间发生了什么，需要规定瞬时变化率，而不仅是相隔一步的差值。以泄漏记忆为例，冻结左端变化率得到Euler系数$a=1-\lambda\Delta t,b=\Delta t$，再由差商进入$\dot x=-\lambda x+u$。固定同一初值与物理时刻，比较$\Delta t=1$及$0.5$的误差，说明缩小步长改善这一近似；$\lambda>0$且区间输入恒定时，精确系数则为$a=e^{-\lambda\Delta t},b=(1-e^{-\lambda\Delta t})/\lambda$，不要求步长足够小。反推连续参数时，须先约定所用规则、步长及输入单位，单凭$a=0.8$不能唯一决定整个连续模型。
4. 随机扰动下的状态演化：给定相同初温与加热量，开门、风速等未显式建模的作用仍可能改变真实温度。把这些作用表示成过程噪声后，更新公式不再只产生一条确定轨迹，而是把噪声的联合规律转换为状态的联合规律。
5. 历史依赖下的状态表示：另一种构造从希望保留的历史特征出发。例如为一段输入保留平均值与线性趋势，就可把投影坐标当作状态。

#### 6.1.1 状态、输入与初值的界定

主要内容：把当前房间温差记作状态，是因为这个模型只需要它和下一段加热量，就能继续计算未来。若历史还通过其他未记录因素起作用，状态就需要扩充。

论证与表述逻辑：

1. 若同一室温下，不同墙体蓄热会导致不同的下一步温度，室温一个坐标就不再足够，需要加入墙体温度。传感器滞后同样可能需要独立的内部状态。新增室温与墙体温度的双状态教学递推和两条解析轨迹，固定室温初值及加热量，仅改变墙体初值，直接算出不同下一室温，说明为何扩充状态。
2. 把温度递推继续算出$x_4$至$x_6$，并由$x_{t+1}-2=0.8(x_t-2)$说明与平衡值的差距每步乘$0.8$。平衡由系数与输入共同决定；固定系数时改变恒定输入，会移动平衡而不改变偏差的衰减倍率，改变系数则还会改变接近平衡的速度。初始条件规定轨迹从哪里开始，输入规定沿途施加什么作用，演化规律规定这些作用怎样改变状态。输出则是模型对外显示的量。

#### 6.1.2 离散时间下的状态更新

主要内容：设$\mathcal X$是允许的状态集合，$\mathcal U$是输入集合。一步更新映射$F_t:\mathcal X\times\mathcal U\longrightarrow\mathcal X,\qquad \boldsymbol x_{t+1}=F_t(\boldsymbol x_t,\boldsymbol u_t)$直接规定下一状态。

论证与表述逻辑：

1. 线性模型常写为$\boldsymbol x_{t+1}=\boldsymbol A_t\boldsymbol x_t+\boldsymbol B_t\boldsymbol u_t,\qquad \boldsymbol x_t\in\mathbb R^d,\quad \boldsymbol u_t\in\mathbb R^m$它关于状态与输入的联合变量是线性的；固定非零输入后，它关于状态通常是仿射的。
2. 一个可直接计算的模型是带泄漏的记忆：$x_{t+1}=a x_t+b u_t,\qquad x_0\ \text{给定}$温度例对应$a=0.8,b=1$。

#### 6.1.3 连续时间下的状态变化

主要内容：若关注相邻采样时刻之间发生了什么，需要规定瞬时变化率，而不仅是相隔一步的差值。常微分方程（ordinary differential equation, ODE）初值问题写为$\dot{\boldsymbol x}(t)=\boldsymbol f(t,\boldsymbol x(t),\boldsymbol u(t)),\qquad \boldsymbol x(t_0)=\boldsymbol x_0$给定输入后，右侧是作用在当前状态上的向量场。先用单粒子位置、动量更新和势能坡度说明两条方程如何由总能量的不同偏导组织，再给出向量Hamilton表达。

论证与表述逻辑：

1. 将前向Euler明确为冻结左端变化率的近似规则。取$\lambda=0.2,u=0.4$及同一零初值，步长$1$时在$t=5,20$的误差约为$0.08,0.014$；改用步长$0.5$时，输入系数也改为$0.5$，在相同物理时刻分别计算$10,40$步，误差约为$0.038,0.007$。
2. 对区间恒定输入与$\lambda>0$，先令$z=x-u/\lambda$，由$\dot z=-\lambda z$得到平衡偏差的精确指数衰减，再移项求出精确采样系数。指数的一阶展开恢复Euler关系；从离散系数反推时须区分两种规则，并另核对步长与输入缩放。
3. 定义（可分Hamilton系统）：令$\boldsymbol q,\boldsymbol p\in\mathbb R^d$分别为位置与动量，$U$为连续可微的势能，$\boldsymbol M$为对称正定的质量矩阵。可分Hamilton量为$H(\boldsymbol q,\boldsymbol p)=U(\boldsymbol q)+\frac12\boldsymbol p^\top\boldsymbol M^{-1}\boldsymbol p$相应的Hamilton方程为$\dot{\boldsymbol q}=\nabla_{\boldsymbol p}H,\qquad \dot{\boldsymbol p}=-\nabla_{\boldsymbol q}H$。
4. 第一式由动量得到位置速度，第二式由势能坡度得到动量变化。新增同一能量函数$H=(q^2+p^2)/2$下的Hamilton圆周运动与负梯度下降相图，逐项计算能量导数为零与严格负值，区分能量函数和演化方向。

#### 6.1.4 随机扰动下的状态演化

主要内容：给定相同初温与加热量，开门、风速等未显式建模的作用仍可能改变真实温度。把这些作用表示成过程噪声后，更新公式不再只产生一条确定轨迹，而是把噪声的联合规律转换为状态的联合规律。

论证与表述逻辑：

1. 离散时间下的随机状态更新：独立性使$\mathbb P(\boldsymbol x_{t+1}\in A\mid\boldsymbol x_{0:t})=K_t(\boldsymbol x_t,A)$，这才得到当前状态的Markov性质。
2. 连续时间下的随机状态变化：离散噪声可以逐次相加；连续时间的噪声则要按增量尺度选择驱动。Brownian增量在长度$h$的区间上具有$h$阶方差，Poisson驱动记录区间内到达的事件数。

##### 6.1.4.1 离散时间下的随机状态更新

主要内容：独立性使$\mathbb P(\boldsymbol x_{t+1}\in A\mid\boldsymbol x_{0:t})=K_t(\boldsymbol x_t,A)$，这才得到当前状态的Markov性质。

论证与表述逻辑：

1. 常用的线性加性模型为$\boldsymbol x_{t+1}=\boldsymbol A_t\boldsymbol x_t+\boldsymbol B_t\boldsymbol u_t+\boldsymbol w_{t+1}$若$\boldsymbol w_{t+1}\sim\mathcal N(\boldsymbol0,\boldsymbol Q_{t+1})$且独立于初态与其他过程噪声，$K_t(\boldsymbol x,\cdot)=\mathcal N(\boldsymbol A_t\boldsymbol x+\boldsymbol B_t\boldsymbol u_t,\boldsymbol Q_{t+1})$。
2. 相关噪声需要重新检查条件结构。例如$x_{t+1}=a x_t+w_{t+1}$，而$w_{t+1}=\rho w_t+\varepsilon_{t+1}$，其中新$\varepsilon$独立。
3. 温度模型现在恢复为$x_{t+1}=0.8x_t+u_t+w_{t+1},\qquad w_{t+1}\sim\mathcal N(0,0.04)$取各$w_t$相互独立且独立于初态。

##### 6.1.4.2 连续时间下的随机状态变化

主要内容：离散噪声可以逐次相加；连续时间的噪声则要按增量尺度选择驱动。Brownian增量在长度$h$的区间上具有$h$阶方差，Poisson驱动记录区间内到达的事件数。

论证与表述逻辑：

1. 给定漂移规律、噪声幅度与初值，建模任务是规定这些增量如何进入状态。连续时间并不把驱动强行解释成普通时间导数。

#### 6.1.5 历史依赖下的状态表示

主要内容：另一种构造从希望保留的历史特征出发。例如为一段输入保留平均值与线性趋势，就可把投影坐标当作状态。

论证与表述逻辑：

1. 投影固定$t>0$并使用非负权重测度$\mu_t$，输入与基函数取自L^2等价类。有限维子空间中的基线性无关，使Gram二次型成为非零函数的正平方范数，从而保证坐标唯一；$t=0$的退化区间另给初始化。
2. 窗口本身移动时，状态变化不全来自新输入。
3. 所以有限个历史特征不自动形成能独立接续演化的有限维状态；需要额外状态、特别的基与权重，或对边界项作近似。
4. 高阶多项式投影（high-order polynomial projection operators, HiPPO）把历史投影到多项式空间，以随时间更新的投影系数作为状态坐标。它保存哪些历史特征，由窗口、权重和基共同决定；投影误差、演化闭合与扰动稳定性须分别检查，不将逼近误差保证扩张为历史无损保存或递推稳定。

### 6.2 路径的累计运算与状态变换

主要内容：比较输入累计、跳跃与连续随机积分，再讨论状态函数在不同路径上的变化公式。

论证与表述逻辑：

1. 历史输入的累计作用：先保持离散时间。
2. 跳跃路径上的随机积分：离散更新只需说明每一步使用哪些已知量。把更新间隔缩到连续时间后，还须说明被积系数在时间与随机结果的联合空间中是否可测。
3. 连续路径上的随机积分：以下$\boldsymbol W$是在同一滤过下的$m$维标准Brownian运动，分量独立，其增量独立于过去且协方差为时间长度乘$\boldsymbol I_m$。
4. 连续随机演化下的状态函数变换：读数、能量和损失通常是状态的函数。已知状态怎样累计，怎样求这些函数的变化？
5. 跳跃随机演化下的状态函数变换：考虑连续Itô部分加有限活动跳跃的右连续过程$\boldsymbol X_t=\boldsymbol X_0+\int_0^t\boldsymbol b_s\,\mathrm ds +\int_0^t\boldsymbol\sigma_s\,\mathrm d\boldsymbol W_s +\int_0^t\boldsymbol\gamma_s\,\mathrm dN_s,$其中$\boldsymbol\gamma$可预测、在各事件处有限，$\boldsymbol b,\boldsymbol\sigma$满足前述局部可积条件。

#### 6.2.1 历史输入的累计作用

主要内容：先保持离散时间。

论证与表述逻辑：

1. 前两步为$\boldsymbol x_1=\boldsymbol A\boldsymbol x_0+\boldsymbol B\boldsymbol u_0$及$\boldsymbol x_2=\boldsymbol A^2\boldsymbol x_0+\boldsymbol A\boldsymbol B\boldsymbol u_0+\boldsymbol B\boldsymbol u_1$。
2. 用标量$a=1/2,b=c=1,d=0,x_0=0$核对。依次输入$u_0=1,u_1=2,u_2=1$，递推给出$y_0=0,y_1=1,y_2=5/2,y_3=9/4$。
3. 时变系统用有序乘积$\boldsymbol\Phi(t,s)=\boldsymbol A_{t-1}\cdots\boldsymbol A_s\quad(t>s),\qquad \boldsymbol\Phi(s,s)=\boldsymbol I$传播齐次状态，于是$\boldsymbol x_t=\boldsymbol\Phi(t,0)\boldsymbol x_0+ \sum_{\tau=0}^{t-1}\boldsymbol\Phi(t,\tau+1)\boldsymbol B_\tau\boldsymbol u_\tau$若输出为$\boldsymbol C_t\boldsymbol x_t+\boldsymbol D_t\boldsymbol u_t$，对应核为$\boldsymbol K_{t,t}=\boldsymbol D_t,\qquad \boldsymbol K_{t,\tau}=\boldsymbol C_t\boldsymbol\Phi(t,\tau+1)\boldsymbol B_\tau\quad(\tau<t)$它依赖两个绝对时刻，通常不只依赖滞后$t-\tau$，所以线性仍在，平移不变性却已消失。

#### 6.2.2 跳跃路径上的随机积分

主要内容：离散更新只需说明每一步使用哪些已知量。把更新间隔缩到连续时间后，还须说明被积系数在时间与随机结果的联合空间中是否可测。连续累计同时遍历时间与随机结果，需要联合可测性；事件幅度又必须在同次新事件前可用，以此分开引入渐进可测与可预测条件。

论证与表述逻辑：

1. 一个过程$H$适应，表示每个$H_t$对$\mathcal F_t$可测。若对每个$T$，$(t,\omega)\mapsto H_t(\omega)$在$[0,T]\times\Omega$上对$\mathcal B([0,T])\otimes\mathcal F_T$可测，则称它渐进可测。
2. 左极限不是无关紧要的记号。例如单位幅度事件有$\int_0^t N_{s-}\,\mathrm dN_s=\frac{N_t(N_t-1)}2,\qquad \sum_{\tau_j\leq t}N_{\tau_j}=\frac{N_t(N_t+1)}2$右侧第二个和使用了事件后的计数，两者相差$N_t$。

#### 6.2.3 连续路径上的随机积分

主要内容：以下$\boldsymbol W$是在同一滤过下的$m$维标准Brownian运动，分量独立，其增量独立于过去且协方差为时间长度乘$\boldsymbol I_m$。Brownian增量无法按普通导数或有限变差路径累计，但独立增量允许均方误差相加，因此从简单过程的增量和进入均方延拓。从左右端点累计的非零差别出发，引出对称取样所需的二次协变差修正；先声明连续半鞅对象，再说明Stratonovich约定与普通链式法则的关系。区分以连续路径$W$为被积函数的普通时间积分与以$W$为积分器的随机积分；无限总变差妨碍一般Stieltjes构造，但不否定光滑确定性被积函数的特殊路径积分。

论证与表述逻辑：

1. 对可预测$H$，若$\mathbb E\int_0^T H_t^2\,\mathrm dt<\infty$，用简单可预测过程在该范数下逼近，等距关系使积分序列在$L^2$中为Cauchy序列，从而定义与逼近选择无关的积分。
2. 定义（连续Itô过程）：设$\boldsymbol X_0$对$\mathcal F_0$可测，$\boldsymbol b_t$渐进可测，$\boldsymbol\sigma_t$可预测，且每个有限$T$上$\int_0^T(\|\boldsymbol b_t\|+\|\boldsymbol\sigma_t\|_{\mathrm F}^2)\,\mathrm dt<\infty$几乎必然。过程$\boldsymbol X_t=\boldsymbol X_0+\int_0^t\boldsymbol b_s\,\mathrm ds +\int_0^t\boldsymbol\sigma_s\,\mathrm d\boldsymbol W_s$称为连续Itô过程。漂移积分有有限变差，随机积分是连续局部鞅。
3. 积分约定可以由Brownian平方直接辨认：$W_{t_{i+1}}^2-W_{t_i}^2 =2W_{t_i}\Delta W_i+(\Delta W_i)^2$求和并回用二次变差，左端点和趋于$(W_T^2-T)/2$，右端点和趋于$(W_T^2+T)/2$。

#### 6.2.4 连续随机演化下的状态函数变换

主要内容：读数、能量和损失通常是状态的函数。已知状态怎样累计，怎样求这些函数的变化？先说明单位Brownian平方增量和依概率趋于时间，再给一般Itô状态的二次协变差$\int\sigma\sigma^	op\,ds$；$X=2W$产生$4t$，据此解释二阶修正而不丢失扩散系数。新增等分网格下的解析量级图，由独立高斯增量得到Brownian平方和均值1、均方偏差$2/n$，并与光滑路径平方和$1/n$对照；区分随机累计量及其矩。

论证与表述逻辑：

1. 命题（Itô公式）：若要对等式直接取期望，还须漂移项可积，且随机被积项满足例如$\mathbb E\int_0^T\|\nabla f^\top\boldsymbol\sigma_t\|^2\,\mathrm dt<\infty$；局部鞅本身不保证期望为零。
2. 先说明关键估计，以免把二阶项当作形式记忆规则。对有界连续适应系数，局部化后的Taylor展开中，漂移平方和的期望为$O(|\pi|)$，漂移与随机项乘积和的$L^1$范数为$O(|\pi|^{1/2})$；这里$|\pi|$为分割的最大间距。
3. 例如$f(x)=x^2$给出$W_T^2=2\int_0^T W_s\,\mathrm dW_s+T,\qquad \int_0^T W_s\,\mathrm dW_s=(W_T^2-T)/2$常数系数则有$\int_0^T c\,\mathrm dW_s=cW_T$。

#### 6.2.5 跳跃随机演化下的状态函数变换

主要内容：考虑连续Itô部分加有限活动跳跃的右连续过程$\boldsymbol X_t=\boldsymbol X_0+\int_0^t\boldsymbol b_s\,\mathrm ds +\int_0^t\boldsymbol\sigma_s\,\mathrm d\boldsymbol W_s +\int_0^t\boldsymbol\gamma_s\,\mathrm dN_s,$其中$\boldsymbol\gamma$可预测、在各事件处有限，$\boldsymbol b,\boldsymbol\sigma$满足前述局部可积条件。

论证与表述逻辑：

1. 若把$\nabla f^\top\mathrm d\boldsymbol X$统一写在前面，则还须显式加上$\sum_{\tau_j\leq t} [f(\tau_j,\boldsymbol X_{\tau_j})-f(\tau_j,\boldsymbol X_{\tau_j-}) -\nabla f(\tau_j,\boldsymbol X_{\tau_j-})^\top\Delta\boldsymbol X_{\tau_j}]$它不是只有二阶的近似，而是扣掉已计入一阶项后的全部有限差。
2. 令$X=N$、$f(x)=x^2$，每次事件使平方增加$2N_{s-}+1$，所以$N_t^2=\int_0^t(2N_{s-}+1)\,\mathrm dN_s =2\int_0^tN_{s-}\,\mathrm d\widetilde N_s +\widetilde N_t+2\lambda\int_0^tN_s\,\mathrm ds+\lambda t$于是$\mathbb E N_t^2=(\lambda t)^2+\lambda t$。

### 6.3 状态轨迹与分布的求解

主要内容：分别求确定轨迹、随机轨迹和状态分布，再以时间离散化近似原问题，区分演化求解与观测推断。

论证与表述逻辑：

1. 随机扰动下的初值轨迹求解：前面的随机积分累计给定系数；现在让系数随未知状态变化，便要寻找与累计结果相容的整条轨迹。给定初值和同一条噪声驱动后，轨迹能否被唯一确定？
2. 给定初始分布下的状态分布求解：逐路径的积分式不一定最适合回答“某时刻落在何处”的概率问题。线性模型可传播少量矩，一般模型则要传播分布对测试函数的作用。
3. 离散化条件下的轨迹求解：已知轨迹存在唯一，不代表能写出解析式。记从$t_n$到$t_{n+1}=t_n+h$的精确流为$\varphi_{t_{n+1},t_n}$，数值方法以可计算的一步映射$\Psi_{h,t_n}$近似它。

#### 6.3.1 离散时间下的初值轨迹求解

主要内容：给定初值和离散更新后计算轨迹，比较一般逐步递推与仿射结构支持的并行组合。

论证与表述逻辑：

1. 先沿时间应用更新规则，说明一次输入和初态如何确定后继。
2. 在仿射情形中把多个更新写成可结合的复合运算，再说明并行扫描改变执行依赖而不改变所求轨迹。

##### 6.3.1.1 基于逐步递推的轨迹求解

主要内容：把给定输入吸收进$F_t^{\boldsymbol u}(\boldsymbol x)=F_t(\boldsymbol x,\boldsymbol u_t)$，前两步为$\boldsymbol x_1=F_0^{\boldsymbol u}(\boldsymbol x_0),\qquad \boldsymbol x_2=F_1^{\boldsymbol u}\bigl(F_0^{\boldsymbol u}(\boldsymbol x_0)\bigr)$一般状态是有序复合$\boldsymbol x_t=(F_{t-1}^{\boldsymbol u}\circ\cdots\circ F_0^{\boldsymbol u})(\boldsymbol x_0)$。

论证与表述逻辑：

1. 泄漏模型可进一步展开：$x_t=a^t x_0+\sum_{j=0}^{t-1}a^{t-1-j}b u_j$证明从$t=0$的空和开始。
2. 取独立于温度任务的泄漏例$a=1/2,b=1,x_0=0$。仅在第零步输入$u_0=1$时，$x_1=1,x_2=1/2,x_3=1/4$；若$u_0=u_1=1$，则$x_2=3/2$，其中$1/2$来自旧输入，$1$来自新输入。

###### 段：指数递归平均的记忆与方差

把泄漏更新写成指数移动平均，利用仿射递推展开区分初始权重与观测权重；零初值的权重归一化会改变具有先验意义的初值。由旧输入按$(1-\alpha)^k$衰减算出精确衰减步数，说明$1/\alpha$只在小权重时近似成立。在固定真值、独立同方差噪声及平方可积独立初值下推导初始化偏差、方差递推与极限$\alpha\sigma^2/(2-\alpha)$；持续线性变化的真值产生滞后偏差，相关噪声须保留协方差项。对区间保持输入精确积分一阶ODE，得到不等间隔权重$\alpha_n=1-e^{-\Delta t_n/\tau}$，固定物理时间尺度而非步数。

##### 6.3.1.2 基于并行扫描的仿射轨迹求解

主要内容：逐步递推沿时间产生一条串行依赖链。如果每步都是仿射映射，一整段更新仍可压成同样大小的仿射映射，就能先合并这些映射再求各个中间状态。始终称仿射复合，偏移项参与合并，不能用线性复合名称掩盖非零平移项。

论证与表述逻辑：

1. 下传时，节点接收其区间之前已经完成的累计映射$p$。左孩子继续接收$p$；若左块的总映射是$L$，右孩子就接收$L\circ p$。
2. 总工作量统计所有节点执行的合并次数，计算深度统计最长依赖链上的合并次数。$T$步形成的平衡树有$O(T)$个节点、$O(\log T)$层，上下两阶段在每个节点只做常数次合并，同层互不依赖的节点可同时计算。
3. 扫描保留时间次序。若$g_1(\boldsymbol x)=\operatorname{diag}(2,1)\boldsymbol x$、$g_2(\boldsymbol x)=\boldsymbol x+(1,0)^\top$，则$(g_2\circ g_1)(\boldsymbol0)=(1,0)^\top,\qquad (g_1\circ g_2)(\boldsymbol0)=(2,0)^\top$这两个结果说明结合律不能换成交换律。

#### 6.3.2 连续时间下的初值轨迹求解

主要内容：先建立连续初值问题的存在、唯一和延拓条件，再利用线性结构求出初值与输入的作用。

论证与表述逻辑：

1. 从局部条件讨论轨迹能否定义及是否唯一，检查解何时可继续延伸。
2. 在线性模型中使用状态转移与输入累计表达轨迹，区分解析表达成立与数值计算的后续问题。

##### 6.3.2.1 初值约束下的轨迹存在与延拓

主要内容：一个“几乎处处给出斜率”的公式，要能恢复整条曲线，必须排除没有被导数记录的奇异变化。为此采用绝对连续曲线，而非任意连续曲线。连续曲线不必由其几乎处处导数恢复，要求初值加可积速度累计等于曲线自身，才使微分与积分表达对应；区分该曲线性质与前章测度间的零集条件。

论证与表述逻辑：

1. 引理（Grönwall积分估计）：设$e$为$[a,T]$上非负连续函数，$b$为非负可积函数。更一般地，若右侧另有$\int_a^t r(s)\,\mathrm ds$，其中$r\geq0$可积，则$e(t)\leq c\,\mathrm e^{\int_a^t b} +\int_a^t r(s)\,\mathrm e^{\int_s^t b}\,\mathrm ds$。
2. 推导：令$E(t)=c+\int_a^t[b(s)e(s)+r(s)]\,\mathrm ds$，则$e\leq E$，且$E'\leq bE+r$几乎处处成立。乘以绝对连续的积分因子$\exp(-\int_a^t b)$，使用乘积法则并从$a$积分到$t$，得$E(t)\mathrm e^{-\int_a^t b} \leq c+\int_a^t r(s)\mathrm e^{-\int_a^s b}\,\mathrm ds$再乘回积分因子并用$e\leq E$即可；取$r=0$得到第一式。
3. 若$\|\boldsymbol g(t,\boldsymbol x)\|\leq b(t)\|\boldsymbol x\|+r(t)$，其中$b,r$在每个有限时间区间可积，积分方程与此引理给出有限的状态上界。

##### 6.3.2.2 线性演化下的轨迹求解

主要内容：连续时间对应的时不变方程是$\dot{\boldsymbol x}(t)=\boldsymbol A\boldsymbol x(t)+\boldsymbol B\boldsymbol u(t)$对固定有限方阵$\boldsymbol A$，矩阵指数满足$\frac{\mathrm d}{\mathrm dt}\mathrm e^{t\boldsymbol A} =\boldsymbol A\mathrm e^{t\boldsymbol A}=\mathrm e^{t\boldsymbol A}\boldsymbol A$，且$\mathrm e^{t\boldsymbol A}$的逆为$\mathrm e^{-t\boldsymbol A}$。

论证与表述逻辑：

1. 时变系数需要连续时间的传播算子。
2. 定义（状态转移矩阵）：对连续矩阵函数$\boldsymbol A(t)$，状态转移矩阵$\boldsymbol\Phi(t,s)$是满足$\partial_t\boldsymbol\Phi(t,s)=\boldsymbol A(t)\boldsymbol\Phi(t,s),\qquad \boldsymbol\Phi(s,s)=\boldsymbol I$的矩阵值解。
3. 一般不能令$\boldsymbol\Phi(t,s)=\exp(\int_s^t\boldsymbol A(r)\,\mathrm dr)$。

#### 6.3.3 随机扰动下的初值轨迹求解

主要内容：前面的随机积分累计给定系数；现在让系数随未知状态变化，便要寻找与累计结果相容的整条轨迹。给定初值和同一条噪声驱动后，轨迹能否被唯一确定？

论证与表述逻辑：

1. 定义（Itô随机微分方程与强解）：在给定的通常滤过概率空间上，设$\boldsymbol W$为$m$维Brownian运动，$\boldsymbol X_0$为$\mathcal F_0$可测初值。给定联合Borel可测系数$\boldsymbol b:[0,T]\times\mathbb R^d\to\mathbb R^d$、$\boldsymbol\sigma:[0,T]\times\mathbb R^d\to\mathbb R^{d\times m}$，Itô随机微分方程的扩散形式为$\mathrm d\boldsymbol X_t=\boldsymbol b(t,\boldsymbol X_t)\,\mathrm dt +\boldsymbol\sigma(t,\boldsymbol X_t)\,\mathrm d\boldsymbol W_t$解是满足局部可积条件的连续适应过程，使$\boldsymbol X_t=\boldsymbol X_0+\int_0^t\boldsymbol b(s,\boldsymbol X_s)\,\mathrm ds +\int_0^t\boldsymbol\sigma(s,\boldsymbol X_s)\,\mathrm d\boldsymbol W_s$以概率$1$对所有$t$同时成立。若解适应于初值和给定驱动的历史所生成、完成并取右连续版本的滤过，则称为强解；它不另外使用随机信息。
2. 弱解允许概率空间、驱动和过程一起作为待求对象，但它们必须满足同样的驱动联合条件、初值分布及积分方程。路径唯一性比较同一空间、同一初值和同一驱动上的两个解，要求它们不可区分，即几乎必然在所有时刻相同。

##### 6.3.3.1 随机初值问题的存在与唯一性

主要内容：为证明状态相关的随机积分方程有解，可以反复将上一条候选轨迹代入被积系数。相邻候选的误差需要在整个有限时段上一同控制；Itô等距只给出固定终点的二阶误差，鞅最大不等式将它扩展到时段内的最大波动。

论证与表述逻辑：

1. 命题（SDE强解的存在唯一性）：设$\boldsymbol W$在通常滤过下为标准Brownian运动，$\boldsymbol X_0\in L^2(\mathcal F_0)$。
2. 推导：在短区间$[a,a+h]$固定平方可积初值$\boldsymbol\xi$，取连续适应过程的空间，范数为$\|\boldsymbol Z\|_{\mathcal S^2}^2 =\mathbb E\sup_{a\leq t\leq a+h}\|\boldsymbol Z_t\|^2$，过程按不可区分等价。这是完备空间：Cauchy列可选子列几乎必然一致收敛，极限连续且适应，再用范数Cauchy性质得到$\mathcal S^2$收敛。定义$(\mathcal T\boldsymbol Z)_t=\boldsymbol\xi+\int_a^t\boldsymbol b(s,\boldsymbol Z_s)\,\mathrm ds +\int_a^t\boldsymbol\sigma(s,\boldsymbol Z_s)\,\mathrm d\boldsymbol W_s$Borel系数与连续适应过程的复合渐进可测；增长界、Cauchy--Schwarz、Itô等距和最大不等式使$\mathcal T$映回该空间。
3. 在两次事件间解扩散方程，在$\tau_j$处设$\boldsymbol X_{\tau_j}=\boldsymbol X_{\tau_j-} +\boldsymbol\gamma(\tau_j,\boldsymbol X_{\tau_j-})$。

##### 6.3.3.2 线性随机演化下的轨迹求解

主要内容：线性结构把“系数依赖解”的难点拆开。

论证与表述逻辑：

1. 标量Ornstein--Uhlenbeck（OU）过程把泄漏记忆与持续噪声放在一起：$\mathrm dX_t=-\lambda X_t\,\mathrm dt+\sigma\,\mathrm dW_t,\qquad\lambda>0$由$\mathrm d(\mathrm e^{\lambda t}X_t)= \sigma\mathrm e^{\lambda t}\,\mathrm dW_t$得$X_t=\mathrm e^{-\lambda t}X_0+ \sigma\int_0^t\mathrm e^{-\lambda(t-s)}\,\mathrm dW_s$若$X_0=x_0$为常数，第二项为零均值高斯，因而$X_t\sim\mathcal N(\mathrm e^{-\lambda t}x_0, \sigma^2(1-\mathrm e^{-2\lambda t})/(2\lambda))$。

#### 6.3.4 给定初始分布下的状态分布求解

主要内容：逐路径的积分式不一定最适合回答“某时刻落在何处”的概率问题。线性模型可传播少量矩，一般模型则要传播分布对测试函数的作用。

论证与表述逻辑：

1. 线性演化下的均值与协方差求解：随机积分为零均值、与初值独立，故$\boldsymbol m_t&=\boldsymbol\Phi(t,0)\boldsymbol m_0+\int_0^t\boldsymbol\Phi(t,s)\boldsymbol c_s\,\mathrm ds,\\ \boldsymbol P_t&=\boldsymbol\Phi(t,0)\boldsymbol P_0\boldsymbol\Phi(t,0)^\top +\int_0^t\boldsymbol\Phi(t,s)\boldsymbol G_s\boldsymbol G_s^\top\boldsymbol\Phi(t,s)^\top\,\mathrm ds$这里积分中的$\boldsymbol G_s\boldsymbol G_s^\top$是确定性矩阵。
2. 一般演化下的分布与密度求解：设确定性系数与适当的解唯一性使$\boldsymbol X$成为Markov过程。要知道分布怎样变化，可先观察任意光滑“读数”$\varphi(\boldsymbol X_t)$的短时期望。

##### 6.3.4.1 线性演化下的均值与协方差求解

主要内容：随机积分为零均值、与初值独立，故$\boldsymbol m_t&=\boldsymbol\Phi(t,0)\boldsymbol m_0+\int_0^t\boldsymbol\Phi(t,s)\boldsymbol c_s\,\mathrm ds,\\ \boldsymbol P_t&=\boldsymbol\Phi(t,0)\boldsymbol P_0\boldsymbol\Phi(t,0)^\top +\int_0^t\boldsymbol\Phi(t,s)\boldsymbol G_s\boldsymbol G_s^\top\boldsymbol\Phi(t,s)^\top\,\mathrm ds$这里积分中的$\boldsymbol G_s\boldsymbol G_s^\top$是确定性矩阵。

论证与表述逻辑：

1. OU过程的初值只需平方可积并独立于驱动，就有$\mathbb E X_t&=\mathrm e^{-\lambda t}\mathbb E X_0, \\ \operatorname{Var}(X_t)&=\mathrm e^{-2\lambda t}\operatorname{Var}(X_0) +\frac{\sigma^2}{2\lambda}(1-\mathrm e^{-2\lambda t})$均值衰减；当$\sigma\neq0$时，方差趋于严格正值。

##### 6.3.4.2 一般演化下的分布与密度求解

主要内容：设确定性系数与适当的解唯一性使$\boldsymbol X$成为Markov过程。要知道分布怎样变化，可先观察任意光滑“读数”$\varphi(\boldsymbol X_t)$的短时期望。新增稳态OU与零速度概率流ODE的解析对照图，明确初态与Brownian驱动独立：两者共享标准正态边缘，但跨时协方差分别衰减和保持1，故匹配边缘仍不能确定路径联合规律。

论证与表述逻辑：

1. 定义（Itô扩散的生成元）：记$\mathbb E_{t,\boldsymbol x}$为从时刻$t$的状态$\boldsymbol x$出发的期望。对属于算子定义域的测试函数，生成元定义为$(\mathcal L_t\varphi)(\boldsymbol x) =\lim_{h\downarrow0} \frac{\mathbb E_{t,\boldsymbol x}\varphi(\boldsymbol X_{t+h})-\varphi(\boldsymbol x)}h$对连续系数的扩散，令$\boldsymbol a=\boldsymbol\sigma\boldsymbol\sigma^\top$；在极限与期望可交换时，Itô公式给出$\mathcal L_t\varphi=\boldsymbol b^\top\nabla\varphi+ \tfrac12\operatorname{tr}(\boldsymbol a\nabla^2\varphi)$。
2. 从积分Itô公式取条件期望，除以$h$再令$h\downarrow0$，即得最后一式。例如取光滑紧支撑$\varphi$，并使系数在相关区域有界，可以先局部化来核对该极限。
3. 若终点分布已知或便于采样，可以从终点出发沿反方向生成路径。概率流ODE只匹配每个时刻的边缘密度；要恢复相邻时刻的随机反向条件规律，则需要时间反演的SDE。

###### 段：由条件路径构造边缘速度

从绝对连续、可测且速度期望可积的随机路径出发，定义给定当前状态的速度条件均值。对紧支测试函数依次使用路径链式法则、Fubini与条件期望，得到无密度也成立的弱连续性方程；密度逐点形式与ODE传播相同边缘另需正则性和适定条件。直线端点插值提供可采样的速度目标，有限二阶矩下平方损失分解说明回归的总体最优解是边缘速度；条件路径为直线不代表ODE轨迹为直线，也不证明端点耦合最优。

#### 6.3.5 离散化条件下的轨迹求解

主要内容：已知轨迹存在唯一，不代表能写出解析式。记从$t_n$到$t_{n+1}=t_n+h$的精确流为$\varphi_{t_{n+1},t_n}$，数值方法以可计算的一步映射$\Psi_{h,t_n}$近似它。

论证与表述逻辑：

1. 基于一般数值离散的轨迹求解：显式Euler法在一步内使用当前斜率：$\widehat{\boldsymbol x}_{n+1} =\widehat{\boldsymbol x}_n+h\boldsymbol f(t_n,\widehat{\boldsymbol x}_n)$这里已把给定输入吸收进$\boldsymbol f$。
2. 基于精确线性离散的轨迹求解：前面的数值规则近似瞬时变化率，线性方程却允许在整段区间上求出精确转移。为使输入积分可算，假设$[t_n,t_n+h)$内$\boldsymbol u(t)=\boldsymbol u_n$。
3. 基于几何离散的保守轨迹求解：保守方程的数值计算除了接近状态，还要检查精确演化保持的几何关系。先沿Hamilton方程求出能量和体积的变化，再据此构造离散映射；保持某种结构不等于每一步都精确，也不自动保证任意步长稳定。
4. 基于随机离散的有限时域轨迹模拟：固定$T$，取$t_k=kh$、$n=T/h$为整数，初值$\widehat{\boldsymbol X}_0=\boldsymbol X_0$。

##### 6.3.5.1 基于一般数值离散的轨迹求解

主要内容：显式Euler法在一步内使用当前斜率：$\widehat{\boldsymbol x}_{n+1} =\widehat{\boldsymbol x}_n+h\boldsymbol f(t_n,\widehat{\boldsymbol x}_n)$这里已把给定输入吸收进$\boldsymbol f$。

论证与表述逻辑：

1. 示例（连续稳定与数值稳定不是一回事）：对$\dot x=-\lambda x+u$，其中$\lambda>0$且$u$恒定，精确一步为$x(t+h)=\mathrm e^{-\lambda h}x(t) +\frac{1-\mathrm e^{-\lambda h}}{\lambda}u$Euler一步为$\widehat x_{n+1}=(1-\lambda h)\widehat x_n+hu$。
2. 对齐次泄漏递推，当$1<h\lambda<2$，数值状态交替变号但幅值缩小；当$h\lambda>2$，它交替增长。有恒定输入时，这一判断作用于相对平衡点的偏差，原状态不必在零的两侧交替。若同一系统包含衰减很快与变化很慢的方向，显式方法可能为压住快方向而被迫采用远小于慢变化尺度的步长，这就是刚性带来的主要计算困难。

##### 6.3.5.2 基于精确线性离散的轨迹求解

主要内容：前面的数值规则近似瞬时变化率，线性方程却允许在整段区间上求出精确转移。为使输入积分可算，假设$[t_n,t_n+h)$内$\boldsymbol u(t)=\boldsymbol u_n$。

论证与表述逻辑：

1. 为使输入积分可算，假设$[t_n,t_n+h)$内$\boldsymbol u(t)=\boldsymbol u_n$。
2. 精确性针对区间内保持不变的输入，不表示真实输入在区间内任意变化时也精确。
3. 输入保持误差与计算矩阵指数的数值误差仍可能存在，只是没有Euler式的时间截断误差。

###### 段：连续随机模型的精确离散

在常系数、区间固定输入、独立Brownian驱动下，由线性SDE的积分解得到精确采样转移，过程协方差为$\int_0^h e^{r\bm A}\bm G\bm G^\top e^{r\bm A^\top}\,\mathrm dr$；高斯且独立的新增噪声不要求初始状态高斯。位置—速度的连续白加速度模型给出$h^3/3,h^2/2,h$三项；每段保持一个独立随机加速度幅度则给出$h^4/4,h^3/2,h^2$及秩一协方差。两者的随机假设、量纲与秩不同，采样间隔变化时不能互换或固定协方差。

##### 6.3.5.3 基于几何离散的保守轨迹求解

主要内容：保守方程的数值计算除了接近状态，还要检查精确演化保持的几何关系。先沿Hamilton方程求出能量和体积的变化，再据此构造离散映射；保持某种结构不等于每一步都精确，也不自动保证任意步长稳定。由一对位置动量扰动的有向面积扩展到多对共轭坐标的双线性配对，再定义辛形式及其保持条件，说明仅有能量或总体积信息不足。

论证与表述逻辑：

1. 精确演化的能量保持：若$H$连续可微、不显含时间，且Hamilton方程的解在所考察区间存在，则$H(\boldsymbol q(t),\boldsymbol p(t))=H(\boldsymbol q(0),\boldsymbol p(0))$。 因此轨迹被限制在初始能量面上，而不是向能量极小值下降。若$H$显含时间，同一计算只给出$\mathrm dH/\mathrm dt=\partial_tH$。
2. 精确演化的辛结构与体积保持：能量只给轨迹上的标量限制，仍未说明一小团相邻初态怎样变形。为比较方向之间的关系，取相空间坐标$\boldsymbol z=(\boldsymbol q^\top,\boldsymbol p^\top)^\top$及前述矩阵$\boldsymbol J$。 反向推断却不成立。在$(q_1,q_2,p_1,p_2)$坐标下，$\operatorname{diag}(2,1,1,1/2)$的行列式为$1$，但它把第一对位置动量的面积乘以$2$，第二对乘以$1/2$，不保持标准辛形式。
3. 离散演化的结构保持：对于可分Hamilton量，势能子系统保持位置、只改变动量；动能子系统保持动量、只改变位置。 所以可逆、辛、体积保持与数值稳定分别需要检查。将这类轨迹用于随机采样时，能量误差还需接受校正，不能把几何积分器直接当作精确采样器。

##### 6.3.5.4 基于随机离散的有限时域轨迹模拟

主要内容：固定$T$，取$t_k=kh$、$n=T/h$为整数，初值$\widehat{\boldsymbol X}_0=\boldsymbol X_0$。

论证与表述逻辑：

1. Poisson驱动须另生成$\Delta N_k\sim\operatorname{Pois}(\lambda h)$，并按驱动假设与Brownian增量独立。

### 6.4 演化与计算序列的收敛

主要内容：区分长时间行为、步长缩小、随机近似和双时间尺度的极限，分别检查状态、计算轨迹与时间平均的收敛。

论证与表述逻辑：

1. 长时间演化下的状态极限：考虑局部Lipschitz自治方程$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$。满足$\boldsymbol f(\boldsymbol x^\star)=\boldsymbol0$的状态称为平衡点。以下性质均要求所涉及初值的解对全部$t\geq0$存在。
2. 步长缩小下的轨迹逼近：固定真实方程、初值和有限时域，改变数值网格的步长$h$。确定性计算比较网格状态与精确轨迹；随机计算可以使用同一噪声比较状态，也可以只比较测试函数的期望。
3. 随机近似下的迭代序列收敛：有些递推状态不是房间温度，而是希望逐步求出的参数。设未知均值为$\mu$，目标是解平均方程$h(\theta)=\mathbb E[Y-\theta]=\mu-\theta=0$每次只能得到一个含噪观测，仍可沿观测建议的方向作小步移动。
4. 双时间尺度下的迭代序列收敛：承接未知均值$\mu$，先以两个算法变量满足$u+v\approx\mu$为具体任务，让$u$快速估计剩余部分$\mu-v$，让$v$缓慢调整两者的分配。由慢变量改变快变量的目标，引出冻结慢变量的近似分析，再给出两组步长的一般递推与条件。
5. 长时间采样下的分布与平均收敛：给定一张目标分布，可以设计演化规律，使长时间模拟产生用于积分的相关样本。需要检查两步：目标是否被演化保持，以及从实际初态出发能否接近它。

#### 6.4.1 长时间演化下的状态极限

主要内容：考虑局部Lipschitz自治方程$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$。满足$\boldsymbol f(\boldsymbol x^\star)=\boldsymbol0$的状态称为平衡点。以下性质均要求所涉及初值的解对全部$t\geq0$存在。先分别提出初值小误差始终小、最终消失和具有指数速度三个问题，再用对邻域全部初值的条件定义稳定性。正定与非增先限制子水平集，有界性还需适当有界区域与解的延拓；旋转系统的恒定能量反例说明非增不能推出到最低点，严格下降和LaSalle不变集条件分别使用。

论证与表述逻辑：

1. 定义（平衡点与稳定性）：考虑局部Lipschitz自治方程$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$。满足$\boldsymbol f(\boldsymbol x^\star)=\boldsymbol0$的状态称为平衡点。以下性质均要求所涉及初值的解对全部$t\geq0$存在。平衡点在Lyapunov意义下稳定，是指对每个$\varepsilon>0$，存在$\delta>0$，使$\|\boldsymbol x(0)-\boldsymbol x^\star\|<\delta$蕴含$\|\boldsymbol x(t)-\boldsymbol x^\star\|<\varepsilon$对全部$t\geq0$成立。同时稳定且有局部吸引性称为渐近稳定。若存在$r,C,\alpha>0$，对上述$r$邻域内全部初值和$t\geq0$都有$\|\boldsymbol x(t)-\boldsymbol x^\star\|_2 \leq C\mathrm e^{-\alpha t}\|\boldsymbol x(0)-\boldsymbol x^\star\|_2,$则称为局部指数稳定。若同一估计对全部初值成立，则称为全局指数稳定。
2. 离散时间把$t\geq0$换成非负整数，平衡条件换成$F(\boldsymbol x^\star)=\boldsymbol x^\star$，指数因子可写成$q^t$，其中$0<q<1$。
3. 定义（Lyapunov函数）：对$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$，若上述正定候选还满足$\dot V(\boldsymbol x):=\nabla V(\boldsymbol x)^\top\boldsymbol f(\boldsymbol x)\leq0$，则称其为该邻域内的Lyapunov函数；若非零点处严格小于零，则称为严格Lyapunov函数。
4. 离散方程相应检查$V(F(\boldsymbol x))-V(\boldsymbol x)$。正定性使“小能量”确实限制所有状态方向，非增性才保证轨迹不能穿越更高的能量边界。

##### 6.4.1.1 平衡邻域内的状态极限

主要内容：对已经定义的平衡点，吸引性直接问邻域内的轨迹是否回到该点。温度模型的零输入偏差满足$e_{t+1}=0.8e_t$，因而$e_t=0.8^t e_0\to0$；连续模型$\dot e=-\lambda e$、$\lambda>0$则给出$e(t)=e^{-(t-t_0)\lambda}e(t_0)\to0$。

论证与表述逻辑：

1. 一般非线性方程未必有解析式。下降函数仅有非正导数时，还需检查轨迹是否能停留在较大的零导数集合中。

##### 6.4.1.2 不变区域内的极限集合

主要内容：机械能常只在某些方向上直接耗散，导致$\dot V=0$的集合远大于平衡点。这时应问：轨迹能否一直留在这个集合中？

论证与表述逻辑：

1. 命题（LaSalle不变性原理）：设自治向量场$\boldsymbol f$局部Lipschitz，$\Omega$紧且正向不变，$V$在包含$\Omega$的开邻域上为$C^1$，并有$\dot V\leq0$。令$E=\{\boldsymbol x\in\Omega:\dot V(\boldsymbol x)=0\}$，$M$为$E$中最大不变集，则从$\Omega$出发的每条轨迹满足$\operatorname{dist}(\boldsymbol x(t),M)\to0$。
2. 推导：紧性排除有限时间逃逸，也使$\omega(\boldsymbol x_0)$非空且紧。沿轨迹的$V$单调不增且有下界，故趋于$v_\infty$。对极限点$\boldsymbol z=\lim_j\boldsymbol x(t_j)$，连续性给出$V(\boldsymbol z)=v_\infty$。
3. 能量非增先限制活动区域，动力学再排除不能持续停留的零导数点。把整个$E$直接称为“最终状态”，会丢掉LaSalle论证中最关键的一步。

#### 6.4.2 步长缩小下的轨迹逼近

主要内容：固定真实方程、初值和有限时域，改变数值网格的步长$h$。确定性计算比较网格状态与精确轨迹；随机计算可以使用同一噪声比较状态，也可以只比较测试函数的期望。

论证与表述逻辑：

1. 确定性演化下的离散误差：设$\boldsymbol f$在包含精确轨迹与Euler轨迹的区域内关于状态具有Lipschitz常数$L$，精确解二阶连续可微，且$\|\ddot{\boldsymbol x}(t)\|_2\leq M$。从精确初值出发，若$t_n=t_0+nh\leq t_0+T$，则$L>0$时$\|\widehat{\boldsymbol x}_n-\boldsymbol x(t_n)\|_2 \leq\frac{Mh}{2L}(\mathrm e^{LT}-1)$$L=0$时相应上界为$MTh/2$。
2. 同一噪声下的随机轨迹误差：同一次噪声实现会产生一条真轨迹和一条数值轨迹。要比较两条路径的状态误差，网格算法必须使用真轨迹的同一驱动，即令$\sqrt h\,\boldsymbol\varepsilon_k=\boldsymbol W_{t_{k+1}}-\boldsymbol W_{t_k}$。
3. 测试函数下的随机模拟误差：若只查询终点读数的平均，目标变成测试函数$\varphi$在真终点和数值终点下的期望差，不必把两条路径逐次配对。

##### 6.4.2.1 确定性演化下的离散误差

主要内容：设$\boldsymbol f$在包含精确轨迹与Euler轨迹的区域内关于状态具有Lipschitz常数$L$，精确解二阶连续可微，且$\|\ddot{\boldsymbol x}(t)\|_2\leq M$。从精确初值出发，若$t_n=t_0+nh\leq t_0+T$，则$L>0$时$\|\widehat{\boldsymbol x}_n-\boldsymbol x(t_n)\|_2 \leq\frac{Mh}{2L}(\mathrm e^{LT}-1)$$L=0$时相应上界为$MTh/2$。

论证与表述逻辑：

1. 命题（Euler法的有限时域全局误差）：设$\boldsymbol f$在包含精确轨迹与Euler轨迹的区域内关于状态具有Lipschitz常数$L$，精确解二阶连续可微，且$\|\ddot{\boldsymbol x}(t)\|_2\leq M$。从精确初值出发，若$t_n=t_0+nh\leq t_0+T$，则$L>0$时$\|\widehat{\boldsymbol x}_n-\boldsymbol x(t_n)\|_2 \leq\frac{Mh}{2L}(\mathrm e^{LT}-1)$$L=0$时相应上界为$MTh/2$。
2. 推导：Taylor公式给出$\boldsymbol x(t_{n+1})=\boldsymbol x(t_n)+h\boldsymbol f(t_n,\boldsymbol x(t_n))+\boldsymbol\tau_n$，其中$\|\boldsymbol\tau_n\|_2\leq Mh^2/2$。记$\boldsymbol e_n=\widehat{\boldsymbol x}_n-\boldsymbol x(t_n)$，相减并用Lipschitz条件得$\|\boldsymbol e_{n+1}\|_2\leq(1+Lh)\|\boldsymbol e_n\|_2+Mh^2/2$从$\boldsymbol e_0=\boldsymbol0$展开，$\|\boldsymbol e_n\|_2\leq(Mh^2/2)\sum_{j=0}^{n-1}(1+Lh)^j$。$L>0$时求几何和，并用$(1+Lh)^n\leq\mathrm e^{Lnh}\leq\mathrm e^{LT}$，即得所述界；$L=0$时直接使用$nh\leq T$。
3. 这也是离散Grönwall估计的一个具体推导。局部$O(h^2)$经约$T/h$步累计成为全局$O(h)$，而动力学决定这些误差随后放大多少。

##### 6.4.2.2 同一噪声下的随机轨迹误差

主要内容：同一次噪声实现会产生一条真轨迹和一条数值轨迹。要比较两条路径的状态误差，网格算法必须使用真轨迹的同一驱动，即令$\sqrt h\,\boldsymbol\varepsilon_k=\boldsymbol W_{t_{k+1}}-\boldsymbol W_{t_k}$。

论证与表述逻辑：

1. 估计机制与存在性证明相连。

##### 6.4.2.3 测试函数下的随机模拟误差

主要内容：若只查询终点读数的平均，目标变成测试函数$\varphi$在真终点和数值终点下的期望差，不必把两条路径逐次配对。

论证与表述逻辑：

1. 弱阶较高不说明两条样本轨迹更接近。例如独立生成的两个同分布终点对所有可积测试函数期望完全相同，彼此状态距离却不为零。

#### 6.4.3 随机近似下的迭代序列收敛

主要内容：有些递推状态不是房间温度，而是希望逐步求出的参数。设未知均值为$\mu$，目标是解平均方程$h(\theta)=\mathbb E[Y-\theta]=\mu-\theta=0$每次只能得到一个含噪观测，仍可沿观测建议的方向作小步移动。

论证与表述逻辑：

1. 固定步长的均值例在递推前定义$e_t=\theta^{(t)}-\mu$和$v_t=\operatorname{Var}(e_t)$；确定初值与独立同分布噪声给出稳态方差$\alpha\sigma^2/(2-\alpha)$，说明减小步长降低波动也延缓响应。
2. 引理（固定有限链的加权Poisson分解）：设$P$为固定的有限不可约非周期核，参数递推$\theta^{(t+1)}=\theta^{(t)}+\alpha_tH(\theta^{(t)},Z_t)$始终位于紧集$K$，$H$在$K$上一致有界且关于参数一致Lipschitz。特别地，任意向晚期移动的有限算法时间窗上的尾和趋零。
3. 推导：有限不可约非周期链几何收敛，且$\pi q_\theta=0$，所以$g_\theta=\sum_{j=0}^\infty P^jq_\theta$绝对一致收敛，并满足$g_\theta-Pg_\theta=q_\theta$。对$q_\theta-q_{\theta'}$应用相同几何界，得到有限常数$G,L_g$使$|g_\theta(z)|\leq G$、$|g_\theta(z)-g_{\theta'}(z)|\leq L_g|\theta-\theta'|$。
4. 再用标量递推核对平均稳定与噪声条件怎样配合。设$\theta^{(t+1)}=\theta^{(t)}+\alpha_t[b-a\theta^{(t)}+\xi_{t+1}]$，$a>0$，噪声为条件均值零且条件二阶矩不超过$\sigma^2$，初值二阶矩有限。

#### 6.4.4 双时间尺度下的迭代序列收敛

主要内容：把未知均值$\mu$分给两个算法变量，使$u+v$接近$\mu$；$u$快速估计$\mu-v$，$v$缓慢调整分配，再将此关系写成一般的两组递推。算法变量与贯穿温度模型的行动、读数分开说明，避免沿用字母造成角色混淆。

论证与表述逻辑：

1. 在具体分工之后引入快慢步长，要求两组步长各自满足Robbins--Monro条件且$\alpha_t/\beta_t\to0$。快时间上把$\boldsymbol v$暂时固定，得到$\dot{\boldsymbol u}=\boldsymbol g(\boldsymbol u,\boldsymbol v)$；若其稳定平衡为$\boldsymbol u^\star(\boldsymbol v)$，慢时间上再使用$\dot{\boldsymbol v}=\boldsymbol f(\boldsymbol u^\star(\boldsymbol v),\boldsymbol v)$。收敛结论还依赖快慢方程的稳定性、联合迭代有界、噪声矩界和残差条件，尺度分离本身不替代这些假设。
2. 示例（分解同一个未知均值的快慢更新）：若$\mathbb E[Y_{t+1}\mid\mathcal F_t]=\mu$，取$u^{(t+1)}=u^{(t)}+\beta_t(Y_{t+1}-u^{(t)}-v^{(t)}),\qquad v^{(t+1)}=v^{(t)}+\alpha_t(u^{(t)}-v^{(t)})$冻结$v$后，快方程$\dot u=\mu-v-u$的唯一稳定平衡为$u^\star(v)=\mu-v$。
3. 尺度分离没有保证快平衡存在，也没有保证其稳定或全局最优。两组步长同阶时，前面的均值拆分例仍可用联合系统分析，却不能继续使用冻结慢变量的论证。

#### 6.4.5 长时间采样下的分布与平均收敛

主要内容：给定一张目标分布，可以设计演化规律，使长时间模拟产生用于积分的相关样本。需要检查两步：目标是否被演化保持，以及从实际初态出发能否接近它。

论证与表述逻辑：

1. 命题（HMC提议的细致平衡）：若$T$是可微、体积保持的对合，则以概率$\alpha(\boldsymbol z)$移至$T\boldsymbol z$，否则留在$\boldsymbol z$的核，对密度$\rho$满足细致平衡。
2. 推导：接受部分的密度权重为$\rho(\boldsymbol z)\alpha(\boldsymbol z)=\min\{\rho(\boldsymbol z),\rho(T\boldsymbol z)\}$。对任意有界可测函数$g(\boldsymbol z,\boldsymbol z')$，作变量替换$\boldsymbol y=T\boldsymbol z$，由$T^2=I$和单位绝对Jacobian，$\begin{split} &\int g(\boldsymbol z,T\boldsymbol z)\min\{\rho(\boldsymbol z),\rho(T\boldsymbol z)\}\,\mathrm d\boldsymbol z\\ &\quad=\int g(T\boldsymbol y,\boldsymbol y) \min\{\rho(T\boldsymbol y),\rho(\boldsymbol y)\}\,\mathrm d\boldsymbol y . \end{split}$这证明接受部分在交换出发与到达状态后不变。拒绝部分集中在对角线$\boldsymbol z'=\boldsymbol z$，本身对称，两者相加即为细致平衡。
3. 若提议不保持体积，接受比还需Jacobian因子；状态依赖地改变步数或步长，也须重新核对反向提议。实现中的有限精度可逆误差不是上述精确算术证明的一部分。

### 6.5 状态演化的扰动与稳定性

主要内容：比较初值与输入扰动下的轨迹，利用线性谱和Lyapunov方法区分有限时间控制、稳定与误差消退。

论证与表述逻辑：

1. 初值扰动下的轨迹稳定性：前述原点判据通常对应零输入，或把恒定输入下的平衡平移到原点。温度例的恒定$u_t=0.4$对应平衡$2$，误差$e_t=x_t-2$才满足$e_{t+1}=0.8e_t$。
2. 输入扰动下的轨迹稳定性：初值误差只在开始时注入，输入误差可以在每个时刻持续进入。即使无输入偏差会衰减，持续加热偏多仍可能造成非零温差。

#### 6.5.1 初值扰动下的轨迹稳定性

主要内容：前述原点判据通常对应零输入，或把恒定输入下的平衡平移到原点。温度例的恒定$u_t=0.4$对应平衡$2$，误差$e_t=x_t-2$才满足$e_{t+1}=0.8e_t$。

论证与表述逻辑：

1. 要得到衰减，须利用演化方向，而非只限制变化率；线性传播和Lyapunov下降关系分别提供这样的判据。

##### 6.5.1.1 线性演化下的轨迹稳定性

主要内容：离散齐次系统为$\boldsymbol x_{t+1}=\boldsymbol A\boldsymbol x_t,\qquad \boldsymbol x_t=\boldsymbol A^t\boldsymbol x_0$这里用矩阵幂和Jordan分解把长期轨迹问题化成谱的位置；下面对各Jordan块的幂逐项给出长期估计。区分Lyapunov给出的衰减上界与精确模态速率；指数系数约0.38对应时间常数约2.6，减半时间则约为1.8，不能把两者混同。

论证与表述逻辑：

1. 长期演化的谱判据：离散齐次系统为$\boldsymbol x_{t+1}=\boldsymbol A\boldsymbol x_t,\qquad \boldsymbol x_t=\boldsymbol A^t\boldsymbol x_0$这里用矩阵幂和Jordan分解把长期轨迹问题化成谱的位置；下面对各Jordan块的幂逐项给出长期估计。 命题（离散线性系统的渐近稳定性）：在此条件下，原点实际上全局指数稳定。
2. 有限时间的瞬态放大：取$\boldsymbol A=\begin{bmatrix}1/2&K\\0&1/2\end{bmatrix},\qquad K>0$无论$K$多大，谱半径均为$1/2$，而$\boldsymbol A^t= \begin{bmatrix} 2^{-t}&tK\,2^{-(t-1)}\\0&2^{-t} \end{bmatrix}$从$\boldsymbol x_0=(0,1)^\top$出发，第一步即为$(K,1/2)^\top$，欧氏范数可以大幅增长；之后$t2^{-t}\to0$才使状态趋零。 $K\neq0$时，$\boldsymbol A^\top\boldsymbol A\neq\boldsymbol A\boldsymbol A^\top$，矩阵非正规。
3. 同谱的非正规矩阵例显示有限时间放大与长期衰减可以并存；伪谱用同维复矩阵小扰动下所有可能特征值的位置解释，反映谱敏感性，不把谱稳定等同于欧氏范数逐步收缩。

##### 6.5.1.2 非线性演化下的轨迹稳定性

主要内容：非线性系统一般无法通过一个固定矩阵构造全局二次能量，因而需要寻找候选函数。

论证与表述逻辑：

1. 命题（连续时间Lyapunov判据）：设原点为$\dot{\boldsymbol x}=\boldsymbol f(\boldsymbol x)$的平衡点，$\boldsymbol f$在其邻域内局部Lipschitz。若该邻域存在$C^1$正定候选$V$且$\dot V\leq0$，则原点稳定；若非零点上$\dot V<0$，则原点局部渐近稳定。若这些条件在$\mathbb R^d$上成立，且$V(\boldsymbol x)\to\infty$当$\|\boldsymbol x\|\to\infty$，则所有解正向全局存在；非增情形给出稳定性，严格下降情形给出全局渐近稳定性。
2. 推导：选足够小的$\varepsilon$使闭球位于适用邻域。球面上的连续正函数$V$有最小值$c_\varepsilon>0$。原点处连续性给出$\delta<\varepsilon$，使$\|\boldsymbol x_0\|<\delta$时$V(\boldsymbol x_0)<c_\varepsilon$。
3. 径向无界性控制的是远处状态，不能用“在原点附近正定”代替。若还能找到$c_1,c_2,c_3>0$使$c_1\|\boldsymbol x\|^2\leq V\leq c_2\|\boldsymbol x\|^2$、$\dot V\leq-c_3\|\boldsymbol x\|^2$，则前述线性方程证明中的积分估计同样给出局部指数衰减。

#### 6.5.2 输入扰动下的轨迹稳定性

主要内容：初值误差只在开始时注入，输入误差可以在每个时刻持续进入。即使无输入偏差会衰减，持续加热偏多仍可能造成非零温差。

论证与表述逻辑：

1. 线性演化下的轨迹响应：若$\|\boldsymbol u(s)\|\leq U$，第二项至多$(M\|\boldsymbol B\|U/\alpha)(1-\mathrm e^{-\alpha(t-t_0)})$。
2. 非线性演化下的轨迹响应：在初值连续依赖的基础上，再允许输入与向量场改变。设两条轨迹都留在同一区域，原向量场关于状态的Lipschitz常数为$L$，关于输入的常数为$L_u$；比较模型沿第二条轨迹的向量场误差至多为$r(s)$。

##### 6.5.2.1 线性演化下的轨迹响应

主要内容：在指数稳定线性演化中，由初值与输入的卷积表达控制状态及两条轨迹的差异，区分暂态消退与持续偏差。

论证与表述逻辑：

1. 先用矩阵指数的衰减界代入常数变易公式，分别估计初值项和输入累计项。
2. 再利用两组解之差仍满足同一线性方程，得到扰动响应；有界持续输入可留下非零稳态，温度模型给出固定输入偏差被放大的具体倍数。

##### 6.5.2.2 非线性演化下的轨迹响应

主要内容：在初值连续依赖的基础上，再允许输入与向量场改变。设两条轨迹都留在同一区域，原向量场关于状态的Lipschitz常数为$L$，关于输入的常数为$L_u$；比较模型沿第二条轨迹的向量场误差至多为$r(s)$。

论证与表述逻辑：

1. 设两条轨迹都留在同一区域，原向量场关于状态的Lipschitz常数为$L$，关于输入的常数为$L_u$；比较模型沿第二条轨迹的向量场误差至多为$r(s)$。
2. Gronwall引理将初值误差、持续输入误差和模型误差合在同一传播界中：$\|\boldsymbol x(t)-\widetilde{\boldsymbol x}(t)\| \leq \mathrm e^{L(t-t_0)}\|\boldsymbol x_0-\widetilde{\boldsymbol x}_0\| +\int_{t_0}^t\mathrm e^{L(t-s)} \bigl(L_u\|\boldsymbol u(s)-\widetilde{\boldsymbol u}(s)\|+r(s)\bigr)\,\mathrm ds$初态误差、输入误差、模型误差因此有不同来源，却都要经过后续动态传播。

### 6.6 基于观测的状态推断

主要内容：给定生成和观测模型后，分别建立预测、滤波、平滑与整条轨迹推断，说明各自允许使用的信息。

论证与表述逻辑：

1. 观测条件下的推断目标：在前面的状态转移$K_t$之外增加观测核$G_t(\boldsymbol x,B)=\mathbb P(\boldsymbol y_t\in B\mid\boldsymbol x_t=\boldsymbol x)$。
2. 基于历史观测的状态预测：若已有截至$t-1$的条件分布$\pi_{t-1}$，全概率公式给出$\pi_{t\mid t-1}(A) =\int K_{t-1}(\boldsymbol x,A)\,\pi_{t-1}(\mathrm d\boldsymbol x)$这是把每个候选旧状态的下一步分布，按其当前可信程度混合。
3. 基于当前及历史观测的状态滤波：预测分布已经汇总旧读数对当前状态的判断。获得当前读数后，各候选状态的权重还要按它们产生这次读数的可能性调整；所求对象仍是同一个物理状态，只是条件信息增加了。
4. 基于完整观测的状态平滑：固定终点$T$后，未来读数也能帮助判断旧状态。关键不是再向前预测，而是把新获得的下一状态分布通过反向条件关系传回去。
5. 基于完整观测的联合轨迹推断：各时刻边缘分布回答“那一刻可能在哪里”，整条路径后验还要回答“这些状态如何一起出现”。

#### 6.6.1 观测条件下的推断目标

主要内容：在前面的状态转移$K_t$之外增加观测核$G_t(\boldsymbol x,B)=\mathbb P(\boldsymbol y_t\in B\mid\boldsymbol x_t=\boldsymbol x)$。

论证与表述逻辑：

1. 记$\mathcal Y_t=\sigma(\boldsymbol y_1,\ldots,\boldsymbol y_t)$，$\mathcal Y_0$为无观测信息。
2. 用无噪二维例核对观测时序：时刻$1$的候选$(1,0)^\top,(0,1)^\top$都有$y_1=1$；随后共同施加已知输入$\boldsymbol u_1=(0.5,0)^\top$，经$\boldsymbol A=\operatorname{diag}(0.5,2)$演化，时刻$2$的候选为$(1,0)^\top,(0.5,2)^\top$，因而$y_2$分别为$1,2.5$。共同输入在候选状态差中抵消，区分来自状态转移把原先看不到的分量差带入后续读数。
3. 下面的一般核公式只要求前述条件独立结构。

#### 6.6.2 基于历史观测的状态预测

主要内容：若已有截至$t-1$的条件分布$\pi_{t-1}$，全概率公式给出$\pi_{t\mid t-1}(A) =\int K_{t-1}(\boldsymbol x,A)\,\pi_{t-1}(\mathrm d\boldsymbol x)$这是把每个候选旧状态的下一步分布，按其当前可信程度混合。

论证与表述逻辑：

1. 例如隐藏状态为$\{0,1\}$，$\pi_0=(0.7,0.3)$，按当前状态为行、下一状态为列的转移矩阵为$\boldsymbol P=\left[\begin{smallmatrix}0.8&0.2\\0.1&0.9\end{smallmatrix}\right]$。
2. 在线性高斯条件下，仿射变换与独立高斯相加保持高斯性，所以$\boldsymbol m_{t\mid t-1} &=\boldsymbol A_{t-1}\boldsymbol m_{t-1\mid t-1}+\boldsymbol B_{t-1}\boldsymbol u_{t-1}, \\ \boldsymbol P_{t\mid t-1} &=\boldsymbol A_{t-1}\boldsymbol P_{t-1\mid t-1}\boldsymbol A_{t-1}^\top+\boldsymbol Q_t$温度第一步为$m_{1\mid0}=0.4,P_{1\mid0}=0.04$：初值已知并不等于未来状态已知。

#### 6.6.3 基于当前及历史观测的状态滤波

主要内容：预测分布已经汇总旧读数对当前状态的判断。获得当前读数后，各候选状态的权重还要按它们产生这次读数的可能性调整；所求对象仍是同一个物理状态，只是条件信息增加了。

论证与表述逻辑：

1. 命题（有限时域Kalman滤波）：在上述独立线性高斯模型与创新协方差可逆条件下，预测与校正公式精确给出$\boldsymbol x_t\mid\mathcal Y_t\sim \mathcal N(\boldsymbol m_{t\mid t},\boldsymbol P_{t\mid t})$，对每个有限$t$成立。
2. 推导：$t=0$时无观测，条件分布就是给定高斯初值。为核对条件化，令$\boldsymbol e=\boldsymbol x_t-\boldsymbol m_{t\mid t-1}-\boldsymbol K_t\boldsymbol r_t$。在$\mathcal Y_{t-1}$条件下，$\operatorname{Cov}(\boldsymbol e,\boldsymbol r_t) =\boldsymbol P_{t\mid t-1}\boldsymbol C_t^\top-\boldsymbol K_t\boldsymbol S_t=\boldsymbol0$。
3. 标量直接观测例用上标$-$、$+$分别表示加入当前读数前的预测与加入后的滤波，$m^\pm,p^\pm$分别为均值与方差。由$K=p^-/(p^-+r)$说明预测与读数怎样加权；独立教学例与温度例各自使用自己的噪声方差，不互换设定。
4. 两种方法都可能遗漏多峰后验。例如零均值对称先验配上$y=x^2+v$，一个明显正的读数可能支持正负两个状态区间。

#### 6.6.4 基于完整观测的状态平滑

主要内容：固定终点$T$后，未来读数也能帮助判断旧状态。关键不是再向前预测，而是把新获得的下一状态分布通过反向条件关系传回去。

论证与表述逻辑：

1. 命题（有限时域RTS平滑）：在有限时域Kalman条件及每个$\boldsymbol P_{t+1\mid t}$可逆条件下，从终点$(\boldsymbol m_{T\mid T},\boldsymbol P_{T\mid T})$向后递推$\boldsymbol m_{t\mid T} &=\boldsymbol m_{t\mid t}+\boldsymbol J_t(\boldsymbol m_{t+1\mid T}-\boldsymbol m_{t+1\mid t}), \\ \boldsymbol P_{t\mid T} &=\boldsymbol P_{t\mid t} +\boldsymbol J_t(\boldsymbol P_{t+1\mid T}-\boldsymbol P_{t+1\mid t})\boldsymbol J_t^\top,$精确给出$\boldsymbol x_t\mid\mathcal Y_T$的高斯均值与协方差。
2. 推导：给定$\boldsymbol x_{t+1}$后，未来状态和观测与更早状态条件独立，因此$P(\mathrm d\boldsymbol x_t\mid\boldsymbol x_{t+1},\mathcal Y_T) =P(\mathrm d\boldsymbol x_t\mid\boldsymbol x_{t+1},\mathcal Y_t)$。全概率公式给出后向因子化$P(\mathrm d\boldsymbol x_t\mid\mathcal Y_T) =\int P(\mathrm d\boldsymbol x_t\mid\boldsymbol x_{t+1},\mathcal Y_t) P(\mathrm d\boldsymbol x_{t+1}\mid\mathcal Y_T)$将一步条件均值对$\boldsymbol x_{t+1}\mid\mathcal Y_T$取期望，塔式性质得到平滑均值公式。全协方差公式分成两项：条件内协方差为$\boldsymbol P_{t\mid t}-\boldsymbol J_t\boldsymbol P_{t+1\mid t}\boldsymbol J_t^\top$，条件均值的协方差为$\boldsymbol J_t\boldsymbol P_{t+1\mid T}\boldsymbol J_t^\top$；相加即得平滑协方差。
3. 标量随机游走教学例沿用$P,Q,R$表示状态与两类噪声方差，并逐步核对算术：由预测方差$P_{1\mid0}=2$得增益$K_1=3/4$，读数$y_1=2$使滤波均值移到$3/2$、滤波方差降为$1/2$；再用$J_0=1/2$回传一半偏差，得平滑均值$3/4$与平滑方差$5/8<1$。比较时固定目标：$x_1$从预测$(0,2)$变为滤波$(3/2,1/2)$，$x_0$从先验$(0,1)$变为吸收$y_1$后的平滑$(3/4,5/8)$，每一对分别表示均值与方差。在时刻$0$不能使用尚未获得的$y_1$；到时刻$1$估计当前$x_1$与回溯$x_0$是两种查询。窗口$T=1$下$x_1$的平滑等于滤波，要展示它再吸收更晚观测的变化，还须增加$y_2$等读数。沿用上述有限时域线性高斯条件，有$\boldsymbol P_{t\mid T}\preceq\boldsymbol P_{t\mid t}$，即滤波协方差减去平滑协方差是半正定矩阵。

#### 6.6.5 基于完整观测的联合轨迹推断

主要内容：各时刻边缘分布回答“那一刻可能在哪里”，整条路径后验还要回答“这些状态如何一起出现”。

论证与表述逻辑：

1. 若损失为$\sum_t\|\boldsymbol x_t-\boldsymbol a_t\|^2$，联合条件均值的各分量就是$\boldsymbol m_{t\mid T}$，因此逐时刻平滑均值同时组成最小化该可加平方损失的路径输出。
2. 本节的精确结论都在有限时域成立。在那里输入才由反馈主动选择，本章一直把$\boldsymbol u_t$当作已给定量。

### 6.7 本章小结

主要内容：用温度模型区分演化规律、过程噪声、真实轨迹与观测噪声，归纳求解、收敛、稳定和推断的职责。

论证与表述逻辑：

1. 同一温度模型中的演化规律、真实轨迹与传感器读数承担不同职责。初值和输入给出一次初值问题；过程噪声使轨迹成为随机对象；观测噪声产生用于推断的记录。
2. 给定规律以后，求解轨迹与求解分布也有不同输出。线性传播把各时刻输入的作用累计为和或积分，仿射复合允许并行扫描。
3. 本章把行动序列视为已经给定。演化模型和状态推断为这些任务提供条件，单靠轨迹求解仍不能决定怎样行动最合适。

## 第7章 策略的实现与轨迹控制

正文：[02-policy-realization-and-control.tex](../../tex/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/02-policy-realization-and-control.tex)。

### 7.1 策略的实现与可达轨迹

主要内容：在行动与观测受限的系统中比较开环和反馈策略，建立目标可达、可控与状态可区分的结构条件。

论证与表述逻辑：

1. 开环策略与反馈策略：考虑离散时间线性时不变系统$\begin{aligned} \boldsymbol{x}_{t+1}&=\boldsymbol{A}\boldsymbol{x}_t+\boldsymbol{B}\boldsymbol{u}_t,\\ \boldsymbol{y}_t&=\boldsymbol{C}\boldsymbol{x}_t, \end{aligned}$其中$\boldsymbol{x}_t\in\mathbb R^n$、$\boldsymbol{u}_t\in\mathbb R^m$和$\boldsymbol{y}_t\in\mathbb R^p$分别是状态、输入和输出；$\boldsymbol A,\boldsymbol B,\boldsymbol C$的维度依次为$n\times n,n\times m,p\times n$。
2. 目标状态的可达与可控：要判断一个终态能否由动作实现，可以把前$N$次输入对终态的贡献集中写出。
3. 观测条件下的状态可区分性：同一动作序列可能从不同初态产生不同读数。要检查读数是否足以区分初态，先从观测中扣除已知动作的贡献，留下只由初态产生的自由响应。

#### 7.1.1 开环策略与反馈策略

主要内容：考虑离散时间线性时不变系统$\begin{aligned} \boldsymbol{x}_{t+1}&=\boldsymbol{A}\boldsymbol{x}_t+\boldsymbol{B}\boldsymbol{u}_t,\\ \boldsymbol{y}_t&=\boldsymbol{C}\boldsymbol{x}_t, \end{aligned}$其中$\boldsymbol{x}_t\in\mathbb R^n$、$\boldsymbol{u}_t\in\mathbb R^m$和$\boldsymbol{y}_t\in\mathbb R^p$分别是状态、输入和输出；$\boldsymbol A,\boldsymbol B,\boldsymbol C$的维度依次为$n\times n,n\times m,p\times n$。

论证与表述逻辑：

1. 定义（开环控制与反馈控制）：若输入序列$\boldsymbol u_0,\boldsymbol u_1,\ldots$事先指定，不根据运行中实际出现的状态修正，称为开环控制（open-loop control）。状态可直接取得时，规则$\boldsymbol u_t=\kappa_t(\boldsymbol x_t)$称为状态反馈（state feedback）。仅有观测和已执行动作可用时，规则$\boldsymbol u_t=\mu_t(\boldsymbol y_0,\ldots,\boldsymbol y_t;\boldsymbol u_0,\ldots,\boldsymbol u_{t-1})$称为输出反馈（output feedback），初始控制历史按空序列处理。随机系统中，动作必须对这些允许信息可测，不能使用尚未产生的噪声。
2. 在温度例中，始终取$u_t=0.4$是一条开环策略；若直接测得状态，则可以根据$x_t-2$修正输入。若只有带噪声的$y_t$，把$x_t$写进控制公式并不会使真实状态变得可用，必须说明怎样从读数构造估计。
3. 把反馈代回状态方程后，需要确认给定初态与外部输入后，闭环轨迹存在、唯一，并覆盖任务所需时域；随机情形还要固定噪声实现。

#### 7.1.2 目标状态的可达与可控

主要内容：要判断一个终态能否由动作实现，可以把前$N$次输入对终态的贡献集中写出。

论证与表述逻辑：

1. 区分任意初态到零与任意初态到任意终态：$\boldsymbol A$可逆是零可控推出可控的充分条件，$A=B=0$说明一般逆推失败，$A=0,B=1$说明可逆性并非具体系统可控的必要条件。
2. 命题（Popov--Belevitch--Hautus（PBH）可控性判据）：矩阵对$(\boldsymbol A,\boldsymbol B)$可控，当且仅当对每个复特征值$\lambda\in\sigma(\boldsymbol A)$都有$\operatorname{rank}[\lambda\boldsymbol I-\boldsymbol A\ \boldsymbol B]=n$；等价地，不存在非零左特征向量$\boldsymbol q^\ast$同时满足$\boldsymbol q^\ast\boldsymbol A=\lambda\boldsymbol q^\ast$和$\boldsymbol q^\ast\boldsymbol B=\boldsymbol0$。
3. 推导：若存在这样的向量，则$\boldsymbol q^\ast\boldsymbol A^k\boldsymbol B=\lambda^k\boldsymbol q^\ast\boldsymbol B=\boldsymbol0$对所有$k\geq0$成立，所以可控性矩阵不可能满行秩。反之，其列空间$\boldsymbol R_{\mathrm{reach}}$若不满维，便是一个真$\boldsymbol A$不变子空间。正交补$\boldsymbol R_{\mathrm{reach}}^{\perp}$在$\boldsymbol A^\ast$下不变。
4. 终点可控仍不保证任意指定的中间状态都能实现。给定整条参考$\boldsymbol r_t$，离散系统要求每一步$\boldsymbol r_{t+1}-\boldsymbol A\boldsymbol r_t\in\operatorname{col}(\boldsymbol B)$，并且解出的输入位于允许集合；连续系统则要求参考绝对连续且$\dot{\boldsymbol r}_t-\boldsymbol A\boldsymbol r_t=\boldsymbol B\boldsymbol u_t^r$几乎处处成立。

#### 7.1.3 观测条件下的状态可区分性

主要内容：同一动作序列可能从不同初态产生不同读数。要检查读数是否足以区分初态，先从观测中扣除已知动作的贡献，留下只由初态产生的自由响应。

论证与表述逻辑：

1. 定义（可观测性）：若同一已知输入下的输出序列能够区分任意两个不同初态，称$(\boldsymbol C,\boldsymbol A)$可观测（observable）。对上述线性时不变系统，这等价于$\mathcal O(\boldsymbol C,\boldsymbol A)$满列秩。
2. 反之，若秩不足，存在$\boldsymbol v\neq\boldsymbol0$满足$\mathcal O\boldsymbol v=\boldsymbol0$，初态$\boldsymbol x_0$与$\boldsymbol x_0+\boldsymbol v$的前$n$次输出便相同。
3. 新增$\boldsymbol C=(1,1)$的两组二维系统读数图：不同衰减模态使相同首读数随后分开，并由两行观测矩阵的行列式恢复初态；相同模态只能观察坐标和，增加观测时长仍不能补出遗漏方向。
4. 温度模型的$C=1$使无噪声当前读数就能区分状态。有噪声时，同一个读数可能来自多个状态，结构可观测性并不提供单次误差上界。

### 7.2 策略的轨迹收敛与稳定

主要内容：从可稳定、可检测条件进入状态反馈、二次成本下的反馈设计与输出反馈，检查闭环误差的长期行为。

论证与表述逻辑：

1. 不可控与不可观测模式的稳定条件：反馈$\boldsymbol u=-\boldsymbol K\boldsymbol x$把状态矩阵改为$\boldsymbol A-\boldsymbol B\boldsymbol K$。
2. 状态反馈下的闭环稳定：可稳定性保证某个增益能够稳定系统；实际设计仍要给出增益，并检验相应闭环。
3. 二次成本下的稳定化反馈：稳定增益通常不唯一，较快纠偏可能需要更大的动作。以二次型分别计量状态偏差与动作幅值，便能将增益选择写成成本最小化问题；所得反馈律仍是线性的。
4. 输出反馈下的估计与闭环稳定：反馈需要状态，但传感器可能只提供状态的一部分。可以先根据模型和已执行动作预测状态，再利用当前读数与预测读数的差纠正估计。

#### 7.2.1 不可控与不可观测模式的稳定条件

主要内容：反馈$\boldsymbol u=-\boldsymbol K\boldsymbol x$把状态矩阵改为$\boldsymbol A-\boldsymbol B\boldsymbol K$。观测增益使线性估计误差按$\boldsymbol A-\boldsymbol L\boldsymbol C$传播；因此可检测性检查是否存在使误差消退的校正，而不是要求全部初态均可恢复。

论证与表述逻辑：

1. 令$\boldsymbol R_{\mathrm{reach}}$为可控性矩阵的列空间，选取以其一组基为前若干列的可逆矩阵$\boldsymbol T$。
2. 定义（可检测性）：若存在$\boldsymbol L$使$\boldsymbol A-\boldsymbol L\boldsymbol C$稳定，称$(\boldsymbol C,\boldsymbol A)$可检测（detectable）。
3. $\boldsymbol C=(1,0)$看得见$1.2$模式，看不见但无需纠正$0.5$模式，所以不可观测却可检测。

#### 7.2.2 状态反馈下的闭环稳定

主要内容：可稳定性保证某个增益能够稳定系统；实际设计仍要给出增益，并检验相应闭环。取线性状态反馈后，动作与状态递推为$\boldsymbol u_t=-\boldsymbol K\boldsymbol x_t, \qquad \boldsymbol x_{t+1}=(\boldsymbol A-\boldsymbol B\boldsymbol K)\boldsymbol x_t$，负号只是增益约定。

论证与表述逻辑：

1. 非线性系统在不同状态处具有不同的变化方向，固定矩阵的谱一般不足以判断整个区域。可以改用一个随状态变化的标量$V$衡量偏离，再要求所选动作使它沿轨迹下降。
2. 定义（控制Lyapunov函数条件）：考虑$\dot{\boldsymbol x}_t=\boldsymbol f(\boldsymbol x_t)+\boldsymbol G(\boldsymbol x_t)\boldsymbol u_t$，目标为原点，输入属于$U$，并假设$\boldsymbol f,\boldsymbol G$在原点的某邻域内局部Lipschitz。若该邻域内的$C^1$函数$V$满足$V(\boldsymbol0)=0$、$V(\boldsymbol x)>0$（$\boldsymbol x\neq\boldsymbol0$），且有正定连续函数$W$使$\text{对每个 }\boldsymbol x\neq\boldsymbol0\text{，存在 }\boldsymbol u\in U\text{ 使} \quad\nabla V(\boldsymbol x)^\top(\boldsymbol f(\boldsymbol x)+\boldsymbol G(\boldsymbol x)\boldsymbol u) \leq-W(\boldsymbol x),$称$V$提供一个控制Lyapunov函数（control Lyapunov function, CLF）条件：每个非零状态至少应能选择一个使偏离量严格下降的动作。
3. 点态存在动作不等于已经构造出适定反馈。还须选出取值于$U$的局部Lipschitz反馈，使原点为平衡并保持严格下降；模型与反馈的规则性共同保证闭环右端$\boldsymbol f+\boldsymbol G\kappa$局部Lipschitz，补齐前章Lyapunov定理的条件后才得到局部渐近稳定。
4. 若进一步有$c_1\|\boldsymbol x\|_2^2\leq V\leq c_2\|\boldsymbol x\|_2^2$和$W\geq c_3\|\boldsymbol x\|_2^2$，便有$V_t\leq e^{-c_3t/c_2}V_0$；全局结论还需全域条件与解的延拓。三次系统的抵消算例展示下降反馈的构造，并以输入限幅说明结论的区域边界。

#### 7.2.3 二次成本下的稳定化反馈

主要内容：稳定增益通常不唯一，较快纠偏可能需要更大的动作。二次成本同时评价状态偏差与动作幅值，通过有限时域配方构造线性反馈，再讨论确定性无限时域下稳定化与成本最优如何联系。区分稳定性、衰减率、瞬态峰值和输入成本；温度模态$0.8-K$由$K=0.3$时的0.5变为$K=2$时的$-1.2$，说明增大增益可破坏稳定，再引出成本选择。新增同一初态下$K=0.3,1.6,2$的闭环解析轨迹，以模态绝对值和符号分别解释单调衰减、交替衰减及交替发散，不把增益大小视为稳定性指标。

论证与表述逻辑：

1. 在有限时域期望二次成本之前说明风险中性：确定成本10与等概率成本0或20打平。评价只看期望，并非否认波动；随后用终端价值反向配方得到Riccati递推，再说明无限时域稳定化所需条件。
2. 无限时域定理之前先用$\boldsymbol x^\top\boldsymbol Q\boldsymbol x=\|\boldsymbol Q^{1/2}\boldsymbol x\|_2^2$解释成本输出。成本可检测要求沿动态始终不被该输出辨认的模式自行衰减，不能把瞬时零成本方向等同于不可观测模式，也不能用传感器输出的可检测条件替换。
3. 命题（无限时域LQR的稳定化解）：在确定性、时不变、无折扣条件下，设$\boldsymbol Q\succeq\boldsymbol0$、$\boldsymbol R\succ\boldsymbol0$，$(\boldsymbol A,\boldsymbol B)$可稳定且$(\boldsymbol Q^{1/2},\boldsymbol A)$可检测。DARE存在唯一半正定稳定化解，相应反馈使闭环渐近稳定，并在所有允许控制序列中给出二次总成本的最优值$V(\boldsymbol x)=\boldsymbol x^\top\boldsymbol P\boldsymbol x$。
4. 推导：由零终端代价有限问题的价值矩阵单调性与稳定反馈提供的上界构造DARE解，再以闭环谱与成本可检测性证明稳定。对任意有限成本控制，先证明状态及终端项趋零，再对累加配方取极限，得到成本最优性与稳定化解唯一性。
5. $Q=0$的标量反例说明缺少成本可检测时，成本最优可能选择不稳定反馈；持续非零噪声下的无折扣总期望成本通常发散，不能直接沿用确定性定理。
6. 连续时间借用CARE稳定化解的标准存在性结论，并直接核验闭环谱；连续有限时域Riccati与价值最优性留给后章，不写成此处已经证明。

#### 7.2.4 输出反馈下的估计与闭环稳定

主要内容：反馈需要状态，但传感器可能只提供状态的一部分。可以先根据模型和已执行动作预测状态，再利用当前读数与预测读数的差纠正估计。随机部分区分预测协方差与更新后协方差，在独立零均值噪声及有限初态二阶矩的设定下分析线性滤波误差；联合高斯时再把估计解释为精确条件均值。先以无噪声、不完全观测推导Luenberger谱分离；有噪声时显式写$y=Cx+v$。残差是观测空间向量，校正由增益$L$映回状态空间，正残差上调只用于正测量与正增益的标量例。

论证与表述逻辑：

1. 确定性Luenberger观测器合并模型预测与读数残差校正，负责更新下一时刻的估计；控制器单独按尚未使用当前读数的估计选择当前动作。联合矩阵的上三角分块给出谱分离，说明状态反馈与估计误差可以分别作稳定设计。
2. 命题（稳态预测滤波的充分条件）：若$(\boldsymbol C,\boldsymbol A)$可检测、$(\boldsymbol A,\boldsymbol\Sigma_{\mathrm w}^{1/2})$可稳定，且$\boldsymbol\Sigma_{\mathrm v}\succ\boldsymbol0$，预测协方差方程有唯一半正定稳定化解。从任意有限$\boldsymbol\Pi_0\succeq\boldsymbol0$出发的递推收敛到$\boldsymbol\Pi$，稳态$\boldsymbol L=\boldsymbol A\boldsymbol M$使$\boldsymbol A-\boldsymbol L\boldsymbol C$稳定。
3. 推导：对偶代换给出稳态解的存在、唯一与稳定性；固定增益配方给出$\Phi(\boldsymbol X)\preceq\Psi_{\boldsymbol L}(\boldsymbol X)$。在$\boldsymbol X\succeq\boldsymbol Y$时选取在$\boldsymbol X$处取等号的增益，依次用固定增益保序与任意增益上界，展开$\Phi(\boldsymbol X)\succeq\Psi_{\boldsymbol L_{\boldsymbol X}}(\boldsymbol Y)\succeq\Phi(\boldsymbol Y)$，再以零初值和稳态增益两端夹逼一般初始协方差。
4. 转用当前观测更新后的$\widehat{\boldsymbol x}_{t|t}$控制时，先写残差校正式与更新误差，明确时序改为先用当前读数更新、再确定动作。稳态联合矩阵仍可分块检查；持续噪声下的二阶矩有界与协方差收敛不能解释为路径趋零，也不能仅凭谱分离推出成本最优。

### 7.3 策略的调节与跟踪

主要内容：将固定设定值与运动参考转成误差系统，先检查参考可实现性，再讨论反馈和扰动下的调节跟踪。

论证与表述逻辑：

1. 先求出维持目标状态或参考轨迹所需的输入，避免误差方程保留未处理的漂移。
2. 随后用闭环误差分析分别讨论固定调节与运动跟踪，并检查持续扰动和模型误差。

#### 7.3.1 固定目标下的轨迹调节

主要内容：先求维持固定设定值的平衡状态与输入，再设计误差反馈，并检查持续扰动下的调节。

论证与表述逻辑：

1. 确认目标可实现后，以实际状态减去目标建立误差系统，避免漏掉维持目标的前馈输入。
2. 利用闭环稳定讨论偏差消退，再分析持续扰动和补偿机制对稳态误差的影响。

##### 7.3.1.1 目标平衡与可行输入

主要内容：设定值（setpoint）是希望状态或输出最终保持的常数。调节（regulation）要求偏离该常数的误差趋于零；它不只要求在某一时刻经过目标。

论证与表述逻辑：

1. 定义（目标平衡与调节误差）：对$\boldsymbol x_{t+1}=\boldsymbol A\boldsymbol x_t+\boldsymbol B\boldsymbol u_t$，若状态设定值$\boldsymbol r$与常值输入$\boldsymbol u^r$满足$(\boldsymbol I-\boldsymbol A)\boldsymbol r=\boldsymbol B\boldsymbol u^r$，则称$(\boldsymbol r,\boldsymbol u^r)$构成目标平衡。状态调节误差为$\boldsymbol e_t=\boldsymbol x_t-\boldsymbol r$。若只指定输出设定值$\boldsymbol q$，还需寻找平衡状态$\boldsymbol r$使$\boldsymbol C\boldsymbol r=\boldsymbol q$，输出误差为$\boldsymbol e_t^y=\boldsymbol C\boldsymbol x_t-\boldsymbol q$。有输入、状态限制时，目标平衡还须满足$\boldsymbol u^r\in U,\boldsymbol r\in S$。
2. 对只指定输出的任务，可解联立方程$\begin{bmatrix}\boldsymbol I-\boldsymbol A&-\boldsymbol B\\\boldsymbol C&\boldsymbol0\end{bmatrix} \begin{bmatrix}\boldsymbol r\\\boldsymbol u^r\end{bmatrix} =\begin{bmatrix}\boldsymbol0\\\boldsymbol q\end{bmatrix}$。方程可能无解或有多个解；输出达到设定值也不自动要求所有内部状态相同。
3. 示例（非零温度需要维持输入）：在无噪声温度模型中，设定值$r=2$要求$2=0.8\times2+u^r$，所以$u^r=0.4$。若直接使用$u_t=-0.3(x_t-2)$，在$x_t=2$处输入变成零，下一步温差便降为$1.6$，因而$2$不是闭环平衡。

##### 7.3.1.2 基于误差反馈的轨迹调节

主要内容：目标平衡方程给出了在目标处仍需持续施加的输入。在这个输入上叠加误差反馈，才使控制器在目标处停止纠偏而继续维持平衡：$\boldsymbol u_t=\boldsymbol u^r-\boldsymbol K(\boldsymbol x_t-\boldsymbol r), \qquad \boldsymbol e_{t+1}=(\boldsymbol A-\boldsymbol B\boldsymbol K)\boldsymbol e_t$，第二式由原动态减去平衡方程得到。

论证与表述逻辑：

1. 温度反馈的完整计算为$u_t=0.4-0.3(x_t-2), \qquad e_{t+1}=0.5e_t,\quad e_t=0.5^t(x_0-2)$。从$x_0=0$出发，状态依次为$0,1,1.5,1.75,\ldots$，输入依次为$1,0.7,0.55,0.475,\ldots$。
2. 若改用估计状态$\widehat{\boldsymbol x}_t$，令$\boldsymbol e_t^{\mathrm o}=\boldsymbol x_t-\widehat{\boldsymbol x}_t$，则调节误差成为$\boldsymbol e_{t+1}=(\boldsymbol A-\boldsymbol B\boldsymbol K)\boldsymbol e_t+\boldsymbol B\boldsymbol K\boldsymbol e_t^{\mathrm o}$。

##### 7.3.1.3 持续扰动下的轨迹调节

主要内容：持续扰动在名义误差系统中形成受迫项。先由误差方程区分常值偏差、有界时变扰动与随机噪声，再通过累积输出误差的积分状态讨论常值偏差补偿及其可实现条件。

论证与表述逻辑：

1. 积分调节累积的是指定输出误差$\boldsymbol C\boldsymbol e_t$。增广闭环稳定且扰动为常值时，积分方程强制平衡输出误差为零，不要求全部状态误差为零，也不保证任意时变扰动下零误差。
2. 积分器自身带有特征值$1$，不能不经核验就加到控制器上。设计增益前应检查增广对$\left( \begin{bmatrix}\boldsymbol A&\boldsymbol0\\\boldsymbol C&\boldsymbol I\end{bmatrix}, \begin{bmatrix}\boldsymbol B\\\boldsymbol0\end{bmatrix}\right)$可稳定。
3. 输入饱和后，真实误差不再服从上述线性增广方程，积分状态却可能继续累积，造成解除饱和后的大幅动作。限制或回退积分累积是常见的抗积分饱和处理，但处理后的闭环仍需重新验证。

#### 7.3.2 运动参考下的轨迹跟踪

主要内容：先检查参考运动是否符合系统动力学，再结合前馈与反馈控制跟踪误差。

论证与表述逻辑：

1. 给定参考轨迹及其变化，求出可实现它的参考输入。
2. 把实际与参考之差写成误差动态，再检查扰动与模型偏差下能够维持何种跟踪精度。

##### 7.3.2.1 参考轨迹与可实现条件

主要内容：跟踪（tracking）以随时间变化的状态$\boldsymbol r_t$或输出$\boldsymbol q_t$为目标，要求$\boldsymbol x_t-\boldsymbol r_t$或$\boldsymbol C\boldsymbol x_t-\boldsymbol q_t$趋零或保持在规定范围内。

论证与表述逻辑：

1. 定义（可实现参考）：离散线性系统的参考状态、参考输入为$(\boldsymbol r_t,\boldsymbol u_t^r)$。若每一步满足$\boldsymbol r_{t+1}=\boldsymbol A\boldsymbol r_t+\boldsymbol B\boldsymbol u_t^r, \qquad \boldsymbol q_t=\boldsymbol C\boldsymbol r_t,$且参考状态、输入满足所声明的约束，称它为可实现参考。精确从首时刻跟踪还要求$\boldsymbol x_0=\boldsymbol r_0$。连续时间则要求$\boldsymbol r_t$绝对连续，并有$\dot{\boldsymbol r}_t=\boldsymbol A\boldsymbol r_t+\boldsymbol B\boldsymbol u_t^r$几乎处处成立。
2. 若只给输出曲线，需要先找与其一致的内部状态和输入；不同实现可能具有不同内部行为。有输入变化率、采样周期或执行器动态限制时，也必须把这些约束加入可实现性检查。
3. 温度参考的前馈输入由系统方程直接给出：$u_t^r=r_{t+1}-0.8r_t$。前馈（feedforward）是由已知目标运动与模型预先计算的动作，不靠当前误差产生。

##### 7.3.2.2 基于前馈与反馈的轨迹跟踪

主要内容：前馈按参考轨迹计算，没有使用实际偏差；从错误初态出发时，它不会额外纠偏。

论证与表述逻辑：

1. 温度例使用$u_t=r_{t+1}-0.8r_t-0.3(x_t-r_t)$，得到$e_{t+1}=0.5e_t$。
2. 误差趋零、误差有界与始终不超过某阈值仍有区别。无扰动时，$|e_t|=0.5^t|e_0|$既给出收敛，也给出从首步起的范围；一般多维稳定矩阵可能先放大误差，需要使用$M\rho^t$而不能省掉$M$。

##### 7.3.2.3 扰动与模型偏差下的轨迹跟踪

主要内容：将模型矩阵偏差、参考实现残差与外扰写入完整误差方程，再用Lyapunov加权范数建立名义收缩和受迫误差界，说明持续修正对跟踪结论的影响。

论证与表述逻辑：

1. 真实动态与参考规划常有偏差。设实际系统为$\boldsymbol x_{t+1}=(\boldsymbol A+\Delta\boldsymbol A)\boldsymbol x_t+ (\boldsymbol B+\Delta\boldsymbol B)\boldsymbol u_t+\boldsymbol d_t$，名义参考的实现残差为$\boldsymbol\eta_t=\boldsymbol A\boldsymbol r_t+\boldsymbol B\boldsymbol u_t^r-\boldsymbol r_{t+1}$。
2. 对稳定的$\boldsymbol F$，先解$\boldsymbol P_{\mathrm F}-\boldsymbol F^\top\boldsymbol P_{\mathrm F}\boldsymbol F=\boldsymbol I$，由$\boldsymbol P_{\mathrm F}\succ\boldsymbol0$构造加权向量范数及其诱导矩阵范数，使$\|\boldsymbol F\|<1$。随后在同一范数下检查$\|\boldsymbol F\|\leq\rho<1$、$\|\Delta\boldsymbol A-\Delta\boldsymbol B\boldsymbol K\|\leq\varepsilon$及$q:=\rho+\varepsilon<1$，展开几何级数得到误差界；这不要求欧氏范数中的名义矩阵也一步收缩。
3. 在精确温度模型中，若$|d_t|\leq0.1$，则$|e_t|\leq0.5^t|e_0|+0.2(1-0.5^t)$。
4. 如果安全控制器把名义动作改为$\boldsymbol u_t=\boldsymbol u_t^r-\boldsymbol K\boldsymbol e_t+\Delta\boldsymbol u_t^{\mathrm s}$，精确模型的误差方程还多出$\boldsymbol B\Delta\boldsymbol u_t^{\mathrm s}$。

### 7.4 策略的约束与安全

主要内容：以安全区域和一步可行动作为基础，讨论反馈修正，以及扰动和离散执行下逐轨迹安全保证的条件。

论证与表述逻辑：

1. 状态约束下的安全区域：一个制动系统最终停下，仍可能在停下之前越过位置边界；平均成本很小的随机系统，也可能有不可接受的少数路径。安全集合（safe set）直接规定允许出现的状态。
2. 安全条件下的可行动作：函数$h$只用符号区分安全与否，不必等于几何距离。
3. 可行约束下的反馈修正：调节或跟踪已经提出名义动作$\boldsymbol u_{\mathrm{nom}}$，但该动作可能违反安全条件。
4. 扰动与离散执行下的安全保证：名义屏障条件只计算模型给出的变化率。真实连续动态多出加性扰动时，安全函数的导数还多出$\nabla h(\boldsymbol x)^\top\boldsymbol d_t$。

#### 7.4.1 状态约束下的安全区域

主要内容：一个制动系统最终停下，仍可能在停下之前越过位置边界；平均成本很小的随机系统，也可能有不可接受的少数路径。安全集合（safe set）直接规定允许出现的状态。

论证与表述逻辑：

1. 定义（正向不变集）：若任意$\boldsymbol x_0\in S$所产生的闭环解，在其存在的全部未来时刻均位于$S$，称$S$对该闭环正向不变（forward invariant）。
2. 若边界$\partial S=\{h=0\}$光滑且其上$\nabla h\neq\boldsymbol0$，内侧对应$h$增大的方向。在闭集、正则边界与适定闭环等条件下，以闭环速度朝内或相切给出Nagumo边界判据。
3. 用$h(x)=x^3$表示同一半轴却在零点丢失梯度方向的反例，引出由集合内邻近点逼近速度方向的切锥。半轴的$T_S(0)=[0,\infty)$排除负速度；在已声明的正则边界条件下，切锥简化为梯度半空间。退化边界的方向检查与下一节沿轨迹的CBF比较证明分别处理。

#### 7.4.2 安全条件下的可行动作

主要内容：函数$h$只用符号区分安全与否，不必等于几何距离。从边界上的$\dot h\geq0$出发，先用$\dot h\geq-\gamma h$、$\gamma>0$限制内部安全余量的下降，再推广为扩展类$\mathcal K$函数；内部可下降、接近边界时下降限额趋零的机制引出CBF。

论证与表述逻辑：

1. 命题（CBF条件保证正向不变）：在已声明的动态与安全函数正则条件下，若反馈$\boldsymbol u=\kappa(\boldsymbol x)$局部Lipschitz，并在包含$S$的开区域$D$中始终满足$\kappa(\boldsymbol x)\in K_{\mathrm{cbf}}(\boldsymbol x)$，则$S$在相应闭环解存在的时间区间内正向不变。
2. 推导：沿任意闭环解记$r_t=h(\boldsymbol x_t)$，链式法则和CBF约束给出$\dot r_t\geq-\alpha(r_t)$。考虑比较系统$\dot z_t=-\alpha(z_t),\qquad z_0=r_0\geq0$；$\alpha$局部Lipschitz，比较系统局部解唯一，且$z=0$是平衡解，从非负初值出发的解不能穿过零点。又因$\alpha$严格递增且$\alpha(0)=0$，$z_t$留在$[0,z_0]$内，所以比较解在任意有限时间存在。
3. 回到离散温度系统，令$S=[0,3],U=[0,1]$且无噪声。下一步安全要求$0\leq0.8x+u\leq3$，因此精确的一步安全动作集合为$K_{\mathrm{safe}}(x) =[\,\max\{0,-0.8x\},\ \min\{1,3-0.8x\}\,]$；对$x\in[0,3]$，下端为$0$，上端至少为$0.6$，所以每个安全状态都有可行动作。

#### 7.4.3 可行约束下的反馈修正

主要内容：调节或跟踪已经提出名义动作$\boldsymbol u_{\mathrm{nom}}$，但该动作可能违反安全条件。

论证与表述逻辑：

1. 示例（一维积分器上的安全投影）：考虑$\dot x_t=u_t$、$S=[0,\infty)$、$h(x)=x$及$\alpha(h)=\gamma h$。
2. 固定状态时，正定二次目标的强制性阻止最小化序列逃向无穷，非空闭可行域保证取到最小值，凸性与严格凸性保证唯一。约束$xu\geq|x|^{3/2}$下唯一最优动作在零点为零、非零处为$\operatorname{sgn}(x)\sqrt{|x|}$，仍非局部Lipschitz；约束梯度在零退化，说明调用闭环不变性前必须另验反馈规则性。
3. 对无噪声温度模型，先命名状态相关的安全动作界$\underline u_{\mathrm{safe}}(x)=\max\{0,-0.8x\}$与$\overline u_{\mathrm{safe}}(x)=\min\{1,3-0.8x\}$，再把名义动作投影到已核验非空的安全区间。正弦跟踪的首步投影给出$x_1=1$，而不是无约束的$1.153$；此时$e_1=1-[2+0.4\sin(\pi/8)]\approx-1.153$，不再等于$0.5e_0=-1$。投影保证该区间内的逐步安全，跟踪误差须保留安全修正项重新分析。

#### 7.4.4 扰动与离散执行下的安全保证

主要内容：名义屏障条件只计算模型给出的变化率。真实连续动态多出加性扰动时，安全函数的导数还多出$\nabla h(\boldsymbol x)^\top\boldsymbol d_t$。以余距和速度的制动相图展示二阶约束：最大加速度2时，负速度状态需有余距至少v²/4；同速度的两个起点分别能在边界前停下和必然越界。这一解析可保持域不等同于一般高阶CBF可行集。

论证与表述逻辑：

1. 离散温度系统若$|w_{t+1}|\leq\delta$，最坏扰动下的安全动作集合为$K_{\mathrm{safe}}^\delta(x) =[\,\max\{0,\delta-0.8x\},\ \min\{1,3-\delta-0.8x\}\,]$；当$0\leq\delta\leq0.6$，该集合对所有$x\in[0,3]$非空：下端不超过$1$，未截断区间宽度$3-2\delta$非负，且上端在$x=3$也不小于零。
2. 采样点满足连续CBF条件不自动保证采样间安全；在有效的速度界与Lipschitz区域中预留保持动作所需的裕量，或另以离散屏障作逐步归纳，再检查连续采样间轨迹。
3. 双积分器的位置约束先显示一阶导数没有动作、二阶导数才出现输入，再命名相对阶。高阶屏障还要求初态同时满足位置与新增速度条件、约束始终可行且闭环适定；制动距离反例说明安全位置不等于可避免后续越界。
4. CBF还要求用于计算约束的状态信息可靠。若只有估计值，应先给估计误差集合界或概率模型，再收紧安全集合或构造输出反馈屏障。

### 7.5 本章小结

主要内容：区分可实施性、系统结构、闭环稳定、调节跟踪与安全，说明存在一条可达轨迹不足以保证固定反馈的行为。

论证与表述逻辑：

1. 一个可实施策略既要遵守信息时序，也要符合执行器能够改变的方向。可控、可观测要求处理全部状态方向；可稳定只要求不可控模式自行衰减，可检测只要求不可观测模式自行衰减。结构条件仍需由实际闭环矩阵、误差动态或Lyapunov不等式完成行为核验。
2. 在同一温度模型中，固定目标$2$需要平衡输入$0.4$，再加误差反馈才得到$e_{t+1}=0.5e_t$。运动参考改用$u_t^r=r_{t+1}-0.8r_t$抵消参考变化，同一个稳定误差系统便能服务于跟踪。
3. Riccati方法在特定二次成本下选择反馈。有限时域的逐步配方保持二次形式；确定性无折扣无限时域还需可稳定、成本可检测及权重条件，才能同时得到稳定化与成本最优性。
4. 安全性约束全过程。对无噪声温度系统，固定目标反馈已经保持$0\leq u\leq1,0\leq x\leq3$；同一增益的运动参考却可能在初始纠偏时要求过大输入。

## 第8章 策略的价值与优化

正文：[03-policy-value-and-optimization.tex](../../tex/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/03-policy-value-and-optimization.tex)。

本章从温度调节中舒适偏差与能耗的取舍进入，研究可实施策略的后果怎样计价、怎样计算以及怎样优化。初态给定、策略确定且状态演化唯一确定时才得到单条轨迹；初态、行动或环境含随机性时，通常需要评价策略诱导的轨迹分布。期望递推中，固定策略按行动概率加权，优化才改变行动规则；非线性风险还须明确行动随机性是否进入风险映射，不能直接沿用线性加权。

### 8.1 策略的表示与价值

主要内容：用可得信息到行动的映射表示策略，说明它与环境怎样共同诱导轨迹，并由轨迹收益建立策略价值。

论证与表述逻辑：

1. 策略的行动与信息：一次加热只需要一个动作值，持续控制却需要回答不同读数下分别采取什么动作。策略（policy）规定这种从已有信息到行动的选择关系。
2. 策略诱导的轨迹：同一项“走捷径”的策略，在不同路况下会有不同后果。要计算这些后果的概率，必须把初始状态、策略选出的行动与环境转移逐步连接。
3. 轨迹收益与策略价值：轨迹概率确定以后，还需指定每种后果的代价。将实际经过的状态与行动的阶段成本相加，再计入终端成本，得到一次执行的总成本。

#### 8.1.1 策略的行动与信息

主要内容：一次加热只需要一个动作值，持续控制却需要回答不同读数下分别采取什么动作。策略（policy）规定这种从已有信息到行动的选择关系。

论证与表述逻辑：

1. 由状态行动历史定义历史依赖随机策略，再限制为只读当前状态的Markov策略及不随时间改变的平稳Markov策略。随机数不得包含未来环境噪声，去掉历史依赖也不等于去掉时间依赖。
2. 若只能观察$Y_t$，允许信息是$\mathcal I_t=\sigma(Y_0,A_0,\ldots,A_{t-1},Y_t)$，策略不能直接读取$S_t$。条件分布$b_t(\mathrm ds)=\mathbb P(S_t\in\mathrm ds\mid\mathcal I_t)$称为信念状态；只有在模型已知且它连同时间足以预测后续观测与成本时，才可用它作为决策状态。
3. 共同温度模型为$x_{t+1}=0.8x_t+u_t+w_{t+1}$、$y_t=x_t+v_t$，其中$x_t$是相对于环境温度的温差，$u_t$是加热量。无噪声反馈使误差收敛，但尚未给出策略成本；恢复观测噪声后，状态反馈也不能直接当作同一输出反馈。

#### 8.1.2 策略诱导的轨迹

主要内容：同一项“走捷径”的策略，在不同路况下会有不同后果。要计算这些后果的概率，必须把初始状态、策略选出的行动与环境转移逐步连接。

论证与表述逻辑：

1. 定义（有限Markov决策过程与策略）：有限状态集$\mathcal S$、各状态的非空有限行动集$\mathcal A(s)$、初始分布$\mu_0$、受控转移概率$P_t$、阶段成本$c_t$和终端成本$c_H$组成有限时域Markov决策过程（Markov decision process, MDP）。允许策略可以根据全部已有历史随机选择行动$\pi_t(a\mid H_t)$；只依赖当前状态时为Markov策略，确定选择时记作$a=\pi_t(s)$。
2. 现在固定策略$\pi$。对一条状态与行动轨迹$\tau=(s_0,a_0,s_1,\ldots,a_{H-1},s_H)$，链式法则给出$\mathbb P^\pi(\tau) =\mu_0(s_0)\prod_{t=0}^{H-1} \pi_t(a_t\mid h_t)P_t(s_{t+1}\mid s_t,a_t)$每个因子都对应实际生成的一步：先抽初态，再按当前历史选行动，再由环境生成下一状态。
3. 用一个可以枚举全部轨迹的路线例子观察策略怎样改变分布。起点$s_0$选择“稳妥”会确定到达终端损失$2$的状态；选择“捷径”以概率$0.8$到达损失$0$的状态，以概率$0.2$到达损失$6$的状态。

#### 8.1.3 轨迹收益与策略价值

主要内容：轨迹概率确定以后，还需指定每种后果的代价。将实际经过的状态与行动的阶段成本相加，再计入终端成本，得到一次执行的总成本。持续成本有统一正下界时才直接得到无限累计发散，严格正项本身不够；折扣有限性配合有界成本或相应增长条件，并用正几何级数与过快增长成本分别核对边界。

论证与表述逻辑：

1. 运行到中途，已经支付的成本不再改变，但后续行动仍可比较。对一段末状态为$s$的历史$h_t$，一般历史策略的继续成本定义为$J_t^\pi(h_t)= \mathbb E^\pi_{h_t} \left[\sum_{k=t}^{H-1}c_k(S_k,A_k)+c_H(S_H)\right]$下标$h_t$表示固定已知历史，再用策略和转移核重新生成后续过程。
2. 持续运行的系统可能始终支付能耗，无折扣无限累计因而可能发散。几何折扣让成本每延后一步就乘一次$\gamma$，第$t$步权重为$\gamma^t$；改变$\gamma$可能改变策略排序，这是评价目标的选择。时不变成本满足$|c|\leq C$且$0\leq\gamma<1$时，几何级数保证$|V^\pi(s)|\leq C/(1-\gamma)$；无界二次成本仍需另证可积性或矩界。
3. 温度例用$(x-2)^2+u^2$计价舒适偏差和总输入；改成偏移输入$(u-0.4)^2$会改变目标。只有一次行动时，$L$退化为损失$\ell(a,Y)$，收益为$-\ell(a,Y)$；同一阳性概率$0.3$在对称分类损失与高漏诊损失下会对应不同的行动。

### 8.2 策略的轨迹价值与风险

主要内容：固定策略后，比较平均损失、损失波动、尾部风险、违规概率和动态风险，说明各指标所约束的后果不同。

论证与表述逻辑：

1. 平均损失与损失波动：固定走稳妥路线的期望损失为$2$，固定走捷径的期望损失为$1.2$。捷径在平均成本上占优，却有$20\%$的概率付出损失$6$。
2. 概率约束与模型不确定性：任务也可以直接限制损失超标的概率，将违反要求的策略排除在可行范围之外。固定策略产生损失$L$，给定阈值$b$和$\varepsilon\in(0,1)$，机会约束（chance constraint）为$\mathbb P(L>b)\leq\varepsilon$它控制超标是否发生，不区分超标幅度。

#### 8.2.1 平均损失与损失波动

主要内容：固定走稳妥路线的期望损失为$2$，固定走捷径的期望损失为$1.2$。捷径在平均成本上占优，却有$20\%$的概率付出损失$6$。均值--方差反例引出评价应尊重的逐场景单调性、确定常数平移、比例缩放与合并损失关系，将相干公理表述为准则要求而非分布自动性质。

论证与表述逻辑：

1. 设随机轨迹损失$L$可积。期望$\mathbb E[L]$按发生概率线性汇总所有后果；对应的期望收益为$-\mathbb E[L]$。
2. 定义（相干风险）：设风险泛函$\rho:L^1(P)\to\mathbb R$按损失越小越好的方向评价。单调性要求$L\leq L'$几乎处处时$\rho(L)\leq\rho(L')$；平移等变性要求$\rho(L+m)=\rho(L)+m$，其中$m$为确定常数。凸性要求$\rho(\tau L+(1-\tau)L') \leq\tau\rho(L)+(1-\tau)\rho(L'),\qquad 0\leq\tau\leq1$若具有单调性、平移等变性、正齐次性$\rho(\lambda L)=\lambda\rho(L)$（$\lambda\geq0$）和次可加性$\rho(L+L')\leq\rho(L)+\rho(L')$，称为相干风险（coherent risk measure）。
3. 将正齐次性用于同一场景中按比例承担的两份损失，再使用次可加性，得到凸性不等式。策略随机化通常是先抽一个方案、再完整承担该方案损失，与按比例承担不同，不能直接套用该凸性公式。

#### 8.2.2 尾部损失与风险评价

主要内容：用分位数、尾部平均和风险包络描述严重损失，比较它们的评价对象与优化表达。

论证与表述逻辑：

1. 先以损失分位数给出风险价值，再转向超过尾部阈值附近的平均损失。
2. 通过条件风险价值的优化和风险包络表示连接尾部评价与加权最坏情形，说明它们不同于只比较期望。

##### 8.2.2.1 基于分位数的风险价值

主要内容：若任务问“至少$95\%$的执行，损失能否控制在某一水平内”，需要的量是损失分位数，不是方差。

论证与表述逻辑：

1. 定义（风险价值）：对实值随机损失$L$与$\alpha\in(0,1)$，左$\alpha$分位数为$q_\alpha(L)=\inf\{z\in\mathbb R:\mathbb P(L\leq z)\geq\alpha\}$同一量在风险管理中称为风险价值（value at risk, VaR），记为$\operatorname{VaR}_\alpha(L)=q_\alpha(L)$。
2. 在前面的等均值例中，$\operatorname{VaR}_{0.95}(L_{\mathrm{safe}})=1,\qquad \operatorname{VaR}_{0.95}(L_{\mathrm{tail}})=0$第二式来自$\mathbb P(L_{\mathrm{tail}}\leq0)=0.95$。
3. VaR单调且平移等变，但一般不次可加。设互斥事件$E_1,E_2$各有概率$0.04$，令$L_i=\mathbb I\{E_i\}$。

##### 8.2.2.2 基于尾部平均的条件风险价值

主要内容：分位数给出尾部开始的阈值，却没有计入阈值以上的损失幅度。要比较严重后果，可以取出损失最大、总概率固定的一部分结果，计算它们的平均损失。固定阈值时先计基准再按尾部概率折算超额损失，在全部阈值中最小化；单侧导数将这个构造接到分位数，并在原子处只取补足尾部所需的质量。

论证与表述逻辑：

1. 定义（条件风险价值）：对$L\in L^1(P)$和$\alpha\in(0,1)$，定义$\operatorname{CVaR}_\alpha(L) =\inf_{\eta\in\mathbb R} \left\{\eta+\frac{1}{1-\alpha}\mathbb E[(L-\eta)_+]\right\}, \qquad (z)_+=\max\{z,0\}$。
2. 候选阈值$\eta$提高时，第一项直接增加，超过阈值的剩余损失却会减少。记花括号中的函数为$\phi(\eta)$。
3. 横轴最优点$2$是VaR，纵轴最小值$5.2$才是CVaR；两个数在计算中承担不同角色。
4. 一般损失分布在分位点处可有原子；用严格超阈值损失加上分位原子的部分质量补齐最坏$1-\alpha$尾部，并引用适用一般损失分布的后续论文。整个超阈值事件的条件均值只在相应质量条件下可直接代入。

##### 8.2.2.3 基于风险包络的尾部评价

主要内容：阈值公式还可以写成概率权重的选择问题：限制每个结果的最大评价权重，再寻找使期望损失最大的重加权。对$L\in L^1(P)$，$\operatorname{CVaR}_\alpha(L) =\sup_\zeta\left\{\mathbb E_P[\zeta L]: 0\leq\zeta\leq\frac{1}{1-\alpha},\quad\mathbb E_P[\zeta]=1\right\}$$\zeta$是相对于原分布的密度比；这些允许密度组成风险包络。

论证与表述逻辑：

1. 一般可积分布也能直接证明等式，不必只诉诸形式对偶。对任意可行$\zeta$和$\eta$，$\mathbb E[\zeta L] =\eta+\mathbb E[\zeta(L-\eta)] \leq\eta+\frac{\mathbb E[(L-\eta)_+]}{1-\alpha}$对$\eta$取下确界，说明任意可行密度的加权期望都不超过CVaR。
2. 模型不确定性则问真实生成机制可能是哪一个分布。二者都能写成最坏期望，但一般不是同一集合，更不能把重加权结果当作重新估计出的真实事故概率。

#### 8.2.3 概率约束与模型不确定性

主要内容：用机会约束限制固定策略损失超标的概率，再用参数族和候选分布集评价模型不确定性。机会约束$\mathbb P(L>b)\leq\varepsilon$控制事件发生概率，最坏模型期望则在允许生成机制中比较平均损失，二者都不同于逐路径最坏损失。

论证与表述逻辑：

1. 必须把违规事件写清楚。温度任务可以限制终端$\{x_H>3\}$、某时刻$\{x_t>3\}$，也可以限制整段$\{\exists t\leq H:x_t\notin[0,3]\}$。
2. 不给参数概率权重时，以$\sup_\theta\mathbb E_{P_\theta}^\pi[L]$覆盖各候选参数；分布鲁棒评价将参数族推广为$\mathcal P$，每个$Q$与固定策略共同生成完整轨迹分布。固定共享参数与逐节点改换最坏模型的候选集合不同，集合构造及真实分布覆盖保证也需另证。
3. 有限样本空间中，非空闭候选集位于紧致概率单纯形内，线性期望必达到最大值。若集合排除某些结果，保证也只覆盖其允许支持；最坏分布存在不能替代极小极大交换和对偶所需条件。

#### 8.2.4 逐时信息下的动态风险

主要内容：比较出发前的静态尾部评价和逐时条件风险，解释新增信息为何可能改变偏好。

论证与表述逻辑：

1. 先用阶段性信息揭示静态准则下的偏好反转。
2. 再把条件风险逐层嵌套，检查时间一致性以及由此得到的递推评价含义。

##### 8.2.4.1 静态尾部评价与偏好反转

主要内容：从起点评价整条轨迹，与到达某个分支后重新评价剩余损失，是两个不同操作。期望有塔式性质把二者连接起来，静态CVaR一般没有同样的关系。

论证与表述逻辑：

1. 期望有塔式性质把二者连接起来，静态CVaR一般没有同样的关系。
2. 承诺$R$时，起点损失以概率$1/4,1/2,1/4$取$0,2,4$，故$\operatorname{CVaR}_{0.5}(L^R)=3$，小于承诺$F$的$3.5$；到达$B$后，$R$的条件CVaR变为$4$，$F$仍为$3.5$，因此偏好反转。
3. 反转不是算错，而是整条轨迹的尾部与当前分支的尾部并非同一批结果。

##### 8.2.4.2 条件风险与时间一致性

主要内容：前例的排序反转来自整条轨迹尾部与条件尾部的差别。若要求后续节点已有的风险排序传到当前，就可以把评价规则定义为递归：下一节点计算剩余风险，当前节点再汇总这些风险值。历史可测阈值产生的条件评价是只按几乎处处确定的随机变量，因此取其最大共同下界来最小化，以此说明本质下确界为何先于条件CVaR公式所需。

论证与表述逻辑：

1. 静态常数阈值改成当前信息可测的阈值规则：有限树上各当前节点可用不同阈值，但不能偷看未来。单点取负一、其余为零的函数族逐点下确界为负一、本质下确界为零，解释为何必须按几乎处处等价类比较；嵌套风险再由节点向前递归。
2. 定义（一步条件风险映射）：在同一概率空间上，一步条件风险映射（conditional risk mapping）$\rho_t:L^\infty(\mathcal F_{t+1})\longrightarrow L^\infty(\mathcal F_t)$把下一时刻可知的有界随机损失转成当前信息下的风险。输入与输出均按几乎处处相等的等价类理解。
3. 定义（递归意义下的时间一致性）：动态风险族$(\mathcal R_t)$具有时间一致性（time consistency），是指对每个$t<H$、任意两组从$t+1$开始的有界适应损失和同一当前损失$C_t$，只要$\mathcal R_{t+1}(C_{t+1:H})\leq\mathcal R_{t+1}(C'_{t+1:H})$几乎处处成立，就有$\mathcal R_t(C_t,C_{t+1:H})\leq\mathcal R_t(C_t,C'_{t+1:H})$几乎处处成立。
4. 回到两节点例，先固定承诺$F$或$R$。在$B$分别得到风险值$3.5$或$4$，在$N$均为$2$；根节点再对这两个等概率节点值计算CVaR$_{0.5}$，得到$3.5$或$4$。

### 8.3 策略的轨迹价值计算

主要内容：在有限时域、无限折扣及风险评价下计算给定策略的价值，交代递推方程与解的条件。

论证与表述逻辑：

1. 有限时域下的价值递推：评价准则确定以后，可以计算指定策略的剩余成本。有限时域的终端没有后续行动，故$V_H^\pi(s)=c_H(s)$；已知下一时刻价值以后，当前只需按策略和环境的概率汇总它。
2. 无限折扣时域下的价值计算：无限时域没有终端值供反向计算。如果成本有界且折扣小于$1$，远期剩余成本可以统一控制，同一时不变策略的价值便可由“当前成本加折扣后的继续价值”这个固定点关系确定。

#### 8.3.1 有限时域下的价值递推

主要内容：在期望准则下，从终端价值$V_H^\pi(s)=c_H(s)$向前计算指定策略的剩余成本。给定Markov策略时，先按转移概率汇总后继价值，再按指定行动概率平均；整个求值过程不改变策略。

论证与表述逻辑：

1. 将累计和拆为当前成本与后续和，使用塔式法则得到固定策略Bellman式。历史依赖策略仍须保留$J_t^\pi(h_t)$；只有继续规则与预测信息都由当前状态概括，才能缩写为状态价值。
2. 路线例的固定随机比例给出$2-0.8p$，与枚举三条轨迹一致。温度例逐项算出固定反馈成本$6.74$、固定输入成本$8.5184$，说明舒适偏差与输入成本的取舍；两项策略比较不等于全策略最优性证明。
3. 恢复随机扰动后，须沿条件分布求可积成本的期望。平方成本包含状态方差，不能只将零均值噪声代回确定性轨迹而遗漏该项。

#### 8.3.2 无限折扣时域下的价值计算

主要内容：无限时域没有终端值供反向计算。在有限状态行动、时不变转移、有界成本、$0\leq\gamma<1$和给定平稳Markov策略下，以“当前成本加折扣继续价值”的算子压缩性确定唯一固定点，再证明该固定点正是策略期望成本。平稳策略的时间齐次价值关系不要求状态已处稳态；价值函数迭代、执行状态平衡及分布不变律使用不同对象。

论证与表述逻辑：

1. 从任意$V^{(0)}$出发令$V^{(k+1)}=T^\pi V^{(k)}$，有$\lVert V^{(k)}-V^\pi\rVert_\infty \leq\gamma^k\lVert V^{(0)}-V^\pi\rVert_\infty$若取$V^{(0)}=0$，右侧可用$\gamma^kC/(1-\gamma)$替代。
2. 将$c^\pi(s),V^\pi(s)$排列为列向量$\boldsymbol c^\pi,\boldsymbol V^\pi$，以$P^\pi(s,s')$为元素组成矩阵$\boldsymbol P^\pi$，则$\boldsymbol V^\pi=(\boldsymbol I-\gamma\boldsymbol P^\pi)^{-1}\boldsymbol c^\pi =\sum_{j=0}^\infty\gamma^j(\boldsymbol P^\pi)^j\boldsymbol c^\pi$无穷级数在最大范数下收敛，故逆矩阵存在。
3. 单状态例以$\gamma=0.9$和每步期望成本1得到$V^{(k)}=10(1-0.9^k)$，新增价值与几何误差并列图，明确横轴为计算迭代，区别于物理状态演化。
4. 非平稳或一般历史策略仍有定义良好的有界折扣价值，但其继续规则可能随时间或历史变化，不能直接使用这个单一平稳算子。

#### 8.3.3 风险评价下的价值计算

主要内容：分别计算嵌套风险和预先承诺的静态尾部目标，说明两者为何需要不同的状态与递推。

论证与表述逻辑：

1. 对嵌套风险按当前信息递推，保留各阶段的条件评价。
2. 对静态尾部目标增加必要的累计或阈值信息，说明直接套用普通期望Bellman方程会丢失什么。

##### 8.3.3.1 嵌套风险下的递推计算

主要内容：先固定确定性Markov策略$a=\pi_t(s)$。若当前状态确实包含风险评价所需的信息，一步风险映射可写为$\rho_{t,s,a}$，它作用于按$P_t(\cdot\mid s,a)$分布的下一状态。用固定参数0.2、0.8及跨时参数拼接的三张联合表解释模型集合扩大；事件(1,0)的质量由两个原模型共同的0.16变为0.64，逐节点局部合法并不保证属于原共享参数族。

论证与表述逻辑：

1. 随机策略需要多说明一层。采取行动之前，$A_t$尚未揭晓；可在联合条件分布$\pi_t(a\mid s)P_t(s'\mid s,a)$上，对行动和下一状态一起评价：$V_t^{\pi,\rho}(s)= \rho^\pi_{t,s}\bigl(c_t(s,A_t)+V_{t+1}^{\pi,\rho}(S_{t+1})\bigr)$这里$\rho^\pi_{t,s}$的输入是$(A_t,S_{t+1})$上的随机损失，连当前阶段成本也必须放在映射内。
2. 先评价各行动的环境风险再平均行动，是另一个评价目标。路线$p=1/2$时，联合CVaR$_{0.9}$为$6$，先算行动CVaR$_{0.9}$再平均为$4$。单调性和平移等变性给出一步非扩张，明确约定折扣位置并取$0\leq\gamma<1$后，再得到无限时域压缩与误差界。
3. 有限维相干风险的支撑表示给出概率单纯形内的非空闭凸包络；一般凸风险还含罚项。若有限树允许从各节点候选集合任取条件核并拼成全部路径模型，称为矩形性，才可用逆向归纳将嵌套风险解释为该集合的局部最坏期望。
4. 固定共享参数$p\in\{0.2,0.8\}$时，两次Bernoulli结果的事件概率$p(1-p)=0.16$；逐节点改换参数却能给出$0.64$。后者扩大了候选机制，不能当作原固定参数问题的精确求值。

##### 8.3.3.2 静态尾部风险下的增广计算

主要内容：如果仍然要评价起点处的静态总损失CVaR，就不应更换成嵌套目标。以有限时域折扣损失$L=\sum_{t=0}^{H-1}\gamma^tc_t(S_t,A_t)+\gamma^Hc_H(S_H)$为例，这里也允许$\gamma=1$。

论证与表述逻辑：

1. 把已累计成本记为$B_0=0$、$B_{t+1}=B_t+\gamma^tc_t(S_t,A_t)$。在增广状态上，$W_t^{\pi,\eta}$计算终端正部$(B_H+\gamma^Hc_H(S_H)-\eta)_+$的条件期望；非线性留在终端，递推仍按给定策略与转移概率求和。策略若还读取其他历史，也须继续保留。
2. 计算完每个阈值的期望以后，该固定策略的风险为$\operatorname{CVaR}_\alpha(L^\pi) =\inf_{\eta\in\mathbb R} \left\{\eta+\frac{1}{1-\alpha} \sum_s\mu_0(s)W_0^{\pi,\eta}(s,0)\right\}$这里优化$\eta$只是计算CVaR定义中的辅助参数，并没有优化策略。

### 8.4 策略的轨迹价值优化

主要内容：在信息、动作与风险约束下选择策略，分别处理单步、离散多步、连续时间和受限信息的问题。

论证与表述逻辑：

1. 单步价值下的行动选择：只有一次行动时，轨迹损失退化为$\ell(a,Y)$。设观测为$X$，未知结果$Y\in\mathcal Y$，可选行动$a\in\mathcal A$，损失$\ell:\mathcal A\times\mathcal Y\to\mathbb R$给出每种行动在每种结果下的代价。
2. 连续演化下的策略优化：离散递推比较一个完整阶段的成本，连续时间可以比较任意短的一段。将这段成本与终点的继续价值展开，状态速度产生一阶导数，扩散的二次变差产生二阶导数。
3. 风险约束下的策略优化：风险评价同样可以进入策略选择，但递推必须忠实于已经定义的目标。嵌套条件风险按节点递归优化；静态总损失CVaR保留累计成本；概率约束限制违规事件，模型不确定集规定允许的生成机制。

#### 8.4.1 单步价值下的行动选择

主要内容：只有一次行动时，轨迹损失退化为$\ell(a,Y)$。设观测为$X$，未知结果$Y\in\mathcal Y$，可选行动$a\in\mathcal A$，损失$\ell:\mathcal A\times\mathcal Y\to\mathbb R$给出每种行动在每种结果下的代价。

论证与表述逻辑：

1. 定义（条件风险与Bayes决策）：给定条件分布核$P(\mathrm dy\mid x)$，假设损失可测且下列期望有限。行动$a$在观测$x$下的条件风险（conditional risk）为$r(a\mid x)=\mathbb E[\ell(a,Y)\mid X=x] =\int_{\mathcal Y}\ell(a,y)P(\mathrm dy\mid x)$若最小值达到，任取$a^\star(x)\in\argmin_{a\in\mathcal A}r(a\mid x)$称为Bayes行动（Bayes action）。若该选择关于$x$可测，映射$\delta^\star(x)=a^\star(x)$称为Bayes决策规则（Bayes decision rule）。
2. 可测规则$\delta$的总体风险为$R(\delta)=\mathbb E[\ell(\delta(X),Y)]$塔式法则和逐点最小性给出完整的总体比较：$R(\delta^\star) =\mathbb E\!\left[\mathbb E[\ell(\delta^\star(X),Y)\mid X]\right] =\mathbb E[\min_a r(a\mid X)] \leq\mathbb E[r(\delta(X)\mid X)] =R(\delta)$期望存在和可测选择不可省略。
3. 用有限损失表按整行计算期望，说明行动不能在结果揭晓后再逐列挑选。二分类的非对称代价给出阈值$c_{\mathrm{FP}}/(c_{\mathrm{FP}}+c_{\mathrm{FN}})$；只有约定风险并列时选阳性，才将预测阳性写成不小于阈值的充要条件，等号处改用其他并列规则仍最优。
4. 增加拒答行动后，比较最小分类风险与拒答成本，并区分接受覆盖率和预测集合覆盖率。正覆盖率下优先拒绝条件错误风险较高的输入，可以降低接受风险，却减少接受比例；任意增加拒答不保证风险下降，须同时报告风险和覆盖率。覆盖预算会耦合各观测点，随机规则下的线性规划与确定规则下的整数约束也需分别处理。
5. 行动集合确定以后，再比较确定选择与随机选择。给定$x$，按概率核$q(\mathrm da\mid x)$选行动的风险为$\int_{\mathcal A}r(a\mid x)q(\mathrm da\mid x)\geq\inf_a r(a\mid x)$；无额外耦合约束且最小值达到时，最佳纯行动已经足够，预算等约束下随机化仍可改变可行比例。

#### 8.4.2 离散演化下的策略优化

主要内容：在离散演化中选择最优策略，连接有限时域递推、无限折扣不动点、占用流量验证、参数化轨迹期望微分和线性二次结构。

论证与表述逻辑：

1. 先以末端条件作反向最优递推，再在折扣条件下讨论全时域价值与贪心策略。
2. 用价值界和占用约束检查最优性；对参数化策略，先把轨迹概率的导数分成各步行动得分，再讨论剩余收益、历史基线与直接参数依赖。最后利用线性二次结构将一般策略求解化为专门的矩阵递推。

##### 8.4.2.1 有限时域下的最优策略递推

主要内容：当前行动改变下一状态，也改变以后能选择的行动。因此，要比较当前动作，必须把阶段成本与后继状态的最优继续成本相加。

论证与表述逻辑：

1. 定理（有限时域最优性原理）：在有限MDP中，最优递推给出全部允许历史依赖随机继续策略的成本下确界；各时刻各状态选择一个达到最小值的行动，构成达到该值的确定性Markov策略。
2. 推导：用逆向归纳。时刻$H$没有行动，终端成本就是最小继续成本。假设每段末状态为$s'$的历史$h_{t+1}$的最小继续成本均为$V_{t+1}^\star(s')$。
3. 风险偏好属于任务设定，不能在算完期望最优后将它解释成任意意义下的“最稳妥”。

##### 8.4.2.2 无限折扣时域下的最优策略计算

主要内容：保留有限状态行动、时不变转移、有界成本及$0\leq\gamma<1$。与给定策略的$T^\pi$不同，Bellman最优算子为$(TV)(s)=\min_{a\in\mathcal A(s)} \left\{c(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V(s')\right\}$对有限实数族$(u_a),(v_a)$，$|\min_a u_a-\min_a v_a|\leq\max_a|u_a-v_a|$。

论证与表述逻辑：

1. 再对任意历史依赖随机策略$\pi$比较。固定点满足每个状态行动的不等式$V^\star(s)\leq c(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^\star(s')$沿策略实际选择的行动条件化，再把下一步的不等式代入，重复$n$步得到$V^\star(s)\leq\mathbb E_s^\pi \left[\sum_{t=0}^{n-1}\gamma^tc(S_t,A_t)+\gamma^nV^\star(S_n)\right]$该操作不要求$\pi$平稳，因为每一历史选择的行动都满足同一Bellman不等式。
2. 折扣取$1$不再自动保证压缩或尾项消失。长期平均成本改用每步平均这一目标；有限单链模型的平均成本方程将长期主项$g$与状态偏移$h$分开，其存在性不能由折扣压缩证明推出。
3. 连续状态或行动中，还需可测转移、适当的成本下半连续性、非空可行动作及紧致性或强制性条件，再用可测选择将点态最小行动拼成策略。

##### 8.4.2.3 基于价值界与占用流量的最优性验证

主要内容：一个策略成本已算出时，还需要下界来判断它离最优有多远。Bellman不等式允许提出状态价值下界，并检查它对全部行动是否成立。

论证与表述逻辑：

1. 在线性规划前先算单状态、单行动、折扣0.9的访问总量10；乘$1-\gamma$后总质量为1，阶段成本2的折扣成本20也缩放为2。随后推导价值不等式的对偶流量守恒，证明合法占用流量可由策略实现，并保持两端使用同一归一化目标。
2. 为每条不等式引入$d(s,a)\geq0$。
3. 定义（归一化折扣占用度量）：给定初始分布$\mu_0$、$0\leq\gamma<1$和允许策略$\pi$，归一化折扣占用度量（occupancy measure）为$d_\pi(s,a)=(1-\gamma)\mathbb E_{S_0\sim\mu_0}^\pi \left[\sum_{t=0}^\infty\gamma^t \mathbb I\{S_t=s,A_t=a\}\right]$。
4. 新增从$s_0$出发的两状态确定性交替例，由几何级数算出归一化占用$1/(1+\gamma),\gamma/(1+\gamma)$并画出折扣因子响应；平稳分布为$(1/2,1/2)$，执行时分布却一直交替，只有折扣占用在$\gamma\uparrow1$时趋近该平稳分布。
5. 互补松弛给出$d^\star(s,a)>0\ \Longrightarrow\ V^\star(s)=c(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^\star(s')$最优访问中实际使用的行动必须达到Bellman最小值。

##### 8.4.2.4 轨迹期望的参数微分

主要内容：有限时域、有限状态与行动、初始和环境规律不含参数时，研究参数化历史策略怎样改变轨迹期望。以共同支持和可微行动概率建立似然比恒等式，离散行动无需对参数可微；连续空间和无限时域另需可积支配条件。

论证与表述逻辑：

1. 将轨迹对数概率的导数分成各步行动得分之和，用$\nabla p=p\nabla\log p$逐项微分有限求和，再用路线算例核对导数$0.8$。
2. 给定行动前历史，行动得分的条件均值为零，因而可删去过去收益并减去历史基线；行动相关基线一般改变导数，减基线也不自动降低方差。
3. 回报直接依赖参数时保留直接导数项；固定打分参数后得到的是冻结回报目标，不能把它当作策略和打分同时变化目标的完整导数。

###### 段：行动得分与轨迹价值导数

将参数微分作用于策略所诱导的轨迹概率，得到回报乘轨迹得分的期望。用单步选路的各分支贡献算出$0.8$，说明收益不显含参数时，行动概率变化仍改变价值。

###### 段：剩余收益与历史基线

由固定历史下行动概率和为一推导得分条件均值为零，再以塔式法则删除过去收益、加入当前行动前确定的基线。用Bernoulli行动相关基线给出导数改变的反例，并限制对组内均值与训练基线的无偏性解释。

###### 段：直接参数依赖与冻结回报的范围

在逐轨迹回报关于参数可微时，用乘积法则分开回报规则的直接导数与轨迹概率的得分项；环境因子含参数时也须加入轨迹得分。固定打分参数的一轮更新具有独立目标；在策略参数等于冻结点处，补入回报直接项才能得到同时变化目标的完整导数，离开冻结点后还存在旧回报与当前回报的值差别。停止打分分支梯度不构成对同时变化目标的精确求导证明。

##### 8.4.2.5 线性二次成本下的有限时域策略

主要内容：有限MDP通过逐行动枚举求最小值，线性二次模型则能利用代数结构直接求出最小行动。本节只把这个结果接到本章的策略价值接口，不重复定义或配方证明。

论证与表述逻辑：

1. 该模型的最优继续价值具有$V_t^\star(\boldsymbol x)=\boldsymbol x^\top\boldsymbol P_t\boldsymbol x+\beta_t$的形式。
2. 给定反馈的评价只需代入该反馈；求最优反馈才需要对二次行动项最小化。共同温度例的总输入成本也提醒我们，换成偏移输入$(u-0.4)^2$会改变目标。

#### 8.4.3 连续演化下的策略优化

主要内容：离散递推比较一个完整阶段的成本，连续时间可以比较任意短的一段。将这段成本与终点的继续价值展开，状态速度产生一阶导数，扩散的二次变差产生二阶导数。连续时间仍对允许控制取下确界；由任意短时段的动态规划关系取光滑极限得到HJB，局部最小值达到与全程验证另列条件。

论证与表述逻辑：

1. 确定性轨迹的价值方程：从给定状态与时间出发，在非空动作集合中选择使轨迹存在、成本有限并满足信息与状态约束的控制。先由控制截断和拼接建立动态规划，再在光滑及一致展开条件下得到HJB，沿全程轨迹验证候选价值。
2. 随机轨迹的价值方程：随机轨迹无法逐条预先选择，但可以优化允许策略的期望成本。
3. 线性二次成本下的连续策略：在线性动态$\dot{\boldsymbol x}=\boldsymbol A\boldsymbol x+\boldsymbol B\boldsymbol u$下，取$\boldsymbol u\in\mathbb R^m$，阶段成本$\ell(\boldsymbol x,\boldsymbol u)=\boldsymbol x^\top\boldsymbol Q\boldsymbol x+\boldsymbol u^\top\boldsymbol R\boldsymbol u$，终端成本$\phi(\boldsymbol x)=\boldsymbol x^\top\boldsymbol Q_T\boldsymbol x$，其中$\boldsymbol Q,\boldsymbol Q_T\succeq\boldsymbol0$、$\boldsymbol R\succ\boldsymbol0$。
4. 非光滑与受限信息下的价值方程：不同动作的最优成本可能在某处交会，使价值连续却出现折点。此时轨迹成本仍有定义，但经典HJB所用的梯度无法在交会点直接计算。

##### 8.4.3.1 确定性轨迹的价值方程

主要内容：对从$(\boldsymbol x,t)$出发的确定性受控轨迹，最小化运行成本积分与终端成本之和。允许控制必须满足信息、动作与状态条件，使轨迹存在且成本有限；由短时动态规划推导HJB，再把局部方程转成全程最优性证书。

论证与表述逻辑：

1. 动态规划要求允许控制可截断和拼接，并具有可测的近似最优继续选择。常值动作给出HJB不等式的一个方向，短段近似最优控制配合局部一致余项给出反向不等式。Hamilton量是瞬时成本$\ell$与沿状态速度的价值变化率$\nabla V^\top\boldsymbol f$之和，时间导数另计；它是动作比较的目标，不是前章的Hamilton能量函数。
2. 定理（确定性HJB验证）：候选$V\in C^1$满足HJB与终端条件，且每个允许控制都产生存在到$T$的轨迹，链式法则和成本积分成立。若可实现反馈$\kappa$逐点达到下确界，闭环轨迹存在到$T$并满足所有可行条件，则$V$为最优价值，$\kappa$为最优反馈。
3. 任意允许控制下，HJB给出沿轨迹$\partial_sV+\nabla V^\top\boldsymbol f+\ell\geq0$。将前两项合为价值导数，从$t$积分到$T$并代入终端条件，得到$J_{t,\boldsymbol x}(\boldsymbol u)\geq V(\boldsymbol x,t)$；达到下确界的反馈使等号成立。只在采样点降低方程残差还不足以验证全程最优。

##### 8.4.3.2 随机轨迹的价值方程

主要内容：随机轨迹无法逐条预先选择，但可以优化允许策略的期望成本。

论证与表述逻辑：

1. 随机轨迹无法逐条预先选择，但可以优化允许策略的期望成本。设$\boldsymbol W_s$为$d$维标准Brownian运动，状态满足$\mathrm d\boldsymbol X_s=\boldsymbol f(\boldsymbol X_s,\boldsymbol u_s,s)\,\mathrm ds +\boldsymbol\Sigma(\boldsymbol X_s,\boldsymbol u_s,s)\,\mathrm d\boldsymbol W_s,$其中$\boldsymbol\Sigma$为$n\times d$矩阵。
2. 定理（随机HJB验证）：候选价值满足状态二阶、时间一阶连续可微及HJB和终端条件；各允许控制须使过程存在到$T$，成本与有限变差项可积，Itô随机积分为真鞅。可容许反馈若逐点达到下确界，才由验证得到最优期望成本。
3. 推导：对任意允许控制，HJB给出$\partial_sV+\mathcal L^{\boldsymbol u_s}V+\ell(\boldsymbol X_s,\boldsymbol u_s,s)\geq0$。沿轨迹应用Itô公式、积分并取从$(t,\boldsymbol x)$出发的期望，随机积分因真鞅条件消失，得到$\mathbb E_{t,\boldsymbol x}\left[ \phi(\boldsymbol X_T)+\int_t^T\ell(\boldsymbol X_s,\boldsymbol u_s,s)\,\mathrm ds\right] \geq V(\boldsymbol x,t)$对$\kappa$，生成元不等式取等号，同一计算证明其期望成本等于共同下界$V$。这验证的是期望最优，不是每条噪声实现上的路径最优。
4. 若扩散依赖动作，它直接参与动作最小化；依赖状态时也可能改变价值形状。因此噪声均值为零并不足以保证反馈不变。

##### 8.4.3.3 线性二次成本下的连续策略

主要内容：在线性动态$\dot{\boldsymbol x}=\boldsymbol A\boldsymbol x+\boldsymbol B\boldsymbol u$下，取$\boldsymbol u\in\mathbb R^m$，阶段成本$\ell(\boldsymbol x,\boldsymbol u)=\boldsymbol x^\top\boldsymbol Q\boldsymbol x+\boldsymbol u^\top\boldsymbol R\boldsymbol u$，终端成本$\phi(\boldsymbol x)=\boldsymbol x^\top\boldsymbol Q_T\boldsymbol x$，其中$\boldsymbol Q,\boldsymbol Q_T\succeq\boldsymbol0$、$\boldsymbol R\succ\boldsymbol0$。

论证与表述逻辑：

1. 有限时域上这些条件也保证不会在中途丢失所需解。矩阵常微分方程先在终端附近有唯一局部对称解；在其存在区间，反馈连续，验证定理说明其二次型为非负最优成本，并不大于零控制的有限成本。
2. 沿轨迹的二次价值导数与运行成本相加，等于反馈偏差的非负二次型；积分后得到任意策略成本与候选价值之差，最优反馈使它为零。标量例$P(t)=\tanh(T-t)$展示截止时间怎样改变反馈增益。
3. 连续闭环需要特征值实部为负，离散闭环需要特征值位于单位圆内；CARE与DARE分别服务于这两个问题，不能混用。

##### 8.4.3.4 非光滑与受限信息下的价值方程

主要内容：不同动作的最优成本可能在某处交会，使价值连续却出现折点。此时轨迹成本仍有定义，但经典HJB所用的梯度无法在交会点直接计算。

论证与表述逻辑：

1. 测试函数定义前先看$\dot x=u,|u|\leq1$的固定终点任务：可达区间给出价值$\max\{|x|-(T-t),0\}$及延续域内部折点。后续用上下接触导数检验黏性条件，与到达原点即退出时的边界折点分开，再讨论状态约束与信念状态。
2. 定义（连续价值函数的黏性解）：设$V$在方程作用域内连续。对任意光滑测试函数$\varphi$，若$V-\varphi$在内点$(\boldsymbol x,t)$取局部最大值时均有$F(\boldsymbol x,t,\partial_t\varphi,\nabla_{\boldsymbol x}\varphi)\leq0$，称$V$为黏性次解。若局部最小值处均有相应的$F\geq0$，称为黏性上解。同时满足两项，并按当前问题满足终端或边界条件的$V$称为黏性解。
3. 可将测试函数平移常数使接触时$V=\varphi$。局部最大对应$\varphi$从上方接触，局部最小对应从下方接触；不是任取一个斜率代入。
4. HJB比较累计成本，前章的屏障约束限定安全行动。将屏障二次规划用于修正一个性能反馈，通常会改变原成本最优性；在HJB中直接加入约束则是另一个受约束优化问题。

#### 8.4.4 受限信息下的策略选择

主要内容：研究新增观测、连续查询与停止、未知收益探索及状态估计怎样改变行动选择，说明信息价值与控制之间的联系。

论证与表述逻辑：

1. 先比较得到观测前后可选择的策略及其价值，再讨论行动同时产生收益和辨认信息的作用。
2. 在线性高斯条件下说明估计与行动分离所需结构，并限定这一结论的适用范围。

##### 8.4.4.1 新增观测下的决策收益

主要内容：前面的最优规则都受到已有信息限制。如果先获得一次观测，后面的行动可能随观测改变，这项改进能否抵偿获取成本？

论证与表述逻辑：

1. 定义（期望样本信息价值）：在上述有限行动、可积损失和信号核条件下，期望样本信息价值（expected value of sample information, EVSI）为$\operatorname{EVSI}(Z\mid b) =\mathcal R(b)-\mathbb E_{Z\mid b}[\mathcal R(b_Z)]$。
2. 观察后的$\inf_a$在对$Z$求期望之内：先见信号、再行动。若把$\inf_a$放在外面，就强迫所有信号结果使用同一行动，丢失信息的用途。
3. 互信息衡量关于$\Theta$的不确定性平均减少多少，EVSI衡量给定损失下最优决策改善多少。信号可能精确揭示与行动无关的参数，互信息大而EVSI为零；另一个信号只在决策阈值附近改变信念，却可能避免高代价行动。

###### 段：继续查询与停止的比较

在未知参数固定、查询与返回集合有限、已知返回核及条件独立假设下，以当前后验和剩余查询次数作为状态。逆向归纳比较立即停止的任务风险与查询成本加后续最优风险，得到有限预算Bellman式；剩余一次时还原EVSI与查询成本的比较，多次查询不能反复套用短视准则。裁剪或取帧只有在实际规定返回规律、任务损失和充分状态后才能纳入此模型，固定前缀的得分对照也不等同于EVSI。

##### 8.4.4.2 未知收益下的探索价值

主要内容：行动结果既带来即时收益，也可能更新环境认识，从而改变后续选择。两轮先验例计算探索的决策价值，再转向固定环境下与已知参数基准比较的累计伪遗憾，说明可用信息下的最优策略仍可能承担学习代价。

论证与表述逻辑：

1. 两轮选择按成功奖励$1$、失败奖励$0$计收益。已知臂成功概率为$0.6$，未知臂两轮共用参数$\Theta\in\{0.3,0.9\}$，先验各为$1/2$；给定参数奖励条件独立，每轮只观察所选臂。两臂当前均值相同，未知臂成功和失败后却分别给出下一轮成功率$0.75$和$0.375$，从而决定继续或改选已知臂。
2. 先选未知臂并按首轮结果调整，期望收益为$1.29$；先选已知臂及其最优后续给出$1.2$。比较两项首轮行动及后续后，才确定前者是这个两轮先验问题的最优适应策略。额外$0.09$来自后续信息用途；剩余时域、先验、反馈范围或参数变化都会改变计算。
3. 过去观察会决定下一次试验或停止时间，选中数据不能无条件视为固定设计的独立同分布样本。置信与识别保证须检查行动的可预测性及序贯误差条件，探索价值计算本身不能代替这些统计证明。
4. 遗憾改用额外掌握真实参数、每轮选平均奖励最高行动的基准，将两轮先验问题推广为固定环境$\theta$下的$T$轮比较。行动在当前奖励揭晓前选定，且$\mathbb E[Y_t\mid\mathcal H_{t-1},A_t=a,\Theta=\theta]=\mu(a,\theta)$几乎处处成立，才以$\operatorname{Reg}_T(\theta)=\sum_{t=1}^T[\mu(a^\star(\theta),\theta)-\mu(A_t,\theta)]$累计平均奖励差；该量不同于两条实现奖励轨迹之差。
5. 回到原例，先知在两种参数下的基准期望收益为$1.2$和$1.8$，现有适应策略的条件期望收益为$0.81$和$1.77$。条件均值假设把期望伪遗憾接到收益差，按先验再平均得到$\tfrac12(1.2-0.81)+\tfrac12(1.8-1.77)=0.21=1.5-1.29$。这是先验平均的期望伪遗憾，不是随机变量每次实现的取值；EVSI也不能替代长期伪遗憾的序贯证明。

##### 8.4.4.3 线性高斯条件下的估计与行动分离

主要内容：探索例中的动作改变未来信息，估计与行动因而需要联合比较。标准有限时域线性二次高斯控制（linear-quadratic-Gaussian control, LQG）在独立高斯噪声、控制无关协方差、不施加输入或状态约束等条件下，所有允许输出策略共享同一误差协方差序列，由此把估计与期望成本优化分开。

论证与表述逻辑：

1. 控制对当前观测信息$\mathcal I_t$可测且具有有限二阶矩。Kalman条件均值的投影误差满足$\mathbb E[\boldsymbol e_t\mid\mathcal I_t]=\boldsymbol0$，将状态二次成本拆为估计均值的二次项与$\operatorname{tr}(\boldsymbol Q_t\boldsymbol E_t)$，交叉项的条件期望为零。
2. 给定当前信息，动作是已知平移；扣除预测均值后，下一步误差为$\boldsymbol A\boldsymbol e_t+\boldsymbol w_{t+1}$，预测协方差为$\boldsymbol E_{t+1}^{-}=\boldsymbol A\boldsymbol E_t\boldsymbol A^\top+\boldsymbol W_t$。观测校正使用$\boldsymbol L_{t+1}=\boldsymbol E_{t+1}^{-}\boldsymbol C^\top(\boldsymbol C\boldsymbol E_{t+1}^{-}\boldsymbol C^\top+\boldsymbol N_{t+1})^{-1}$，再得$\boldsymbol E_{t+1}=(\boldsymbol I-\boldsymbol L_{t+1}\boldsymbol C)\boldsymbol E_{t+1}^{-}$。这些式子不含动作值或观测实现值，因此同一初始协方差产生策略共有的协方差序列；校正增益$\boldsymbol L$与LQR行动增益$\boldsymbol K$不同。
3. 仅拆分单步状态成本不足以证明全程最优。回用有限LQR配方与时间求和，将任意输出策略成本分为策略无关的初态、过程噪声及估计误差迹项，再加非负的$\boldsymbol u_t+\boldsymbol K_t\widehat{\boldsymbol x}_t$二次项。可实施反馈$\boldsymbol u_t^\star=-\boldsymbol K_t\widehat{\boldsymbol x}_t$使余项同时为零，因而在允许输出策略中达到最小期望成本。
4. 分离原则允许Kalman滤波估计状态、LQR计算行动反馈，既不要求有限时域滤波已达稳态，也不消除估计误差成本。受控观测、动作相关噪声、风险目标或输入状态约束可能破坏分解；温度安全例的有界两点噪声也不能直接替换成本节高斯假设。

#### 8.4.5 风险约束下的策略优化

主要内容：风险评价同样可以进入策略选择，但递推必须忠实于已经定义的目标。嵌套条件风险按节点递归优化；静态总损失CVaR保留累计成本；概率约束限制违规事件，模型不确定集规定允许的生成机制。

论证与表述逻辑：

1. 有限状态行动、确定策略、充分状态和可逐历史拼接的规则下，用风险映射单调性作逆向归纳，得到嵌套风险的最优递推。若先算每项行动的环境风险再平均行动，线性组合仍由纯行动达到最小；若风险作用于行动和下一状态的联合损失，则应优化$q\in\Delta(\mathcal A(s))$，不能把联合风险直接改成行动风险的平均。
2. 有界成本、$0\leq\gamma<1$及归一化、单调和平移等变的一步风险，使“后续风险值再乘折扣”的算子成为压缩；固定点还须通过贪心策略达到性及有限截断的全策略比较，才能解释为最优值。包络的局部最坏解释要求矩形机制，非矩形共享参数与凸风险罚项不能省略。
3. 静态总损失CVaR保留累计成本状态，固定阈值后作行动最小化，再在起点优化常数阈值。两层下确界可以交换，但必须保留增广策略类、可测选择与达到性条件；只允许物理状态策略时，增广递推可能扩大可行域。
4. 机会约束须明确终端、逐时或全程违规事件，必要时增广违规标记或剩余预算。路线例要求$0.2p\leq0.1$，最优随机比例$p=1/2$给出期望成本$1.6$；仅允许确定行动时只有成本$2$的稳妥路线可行，随机化在此改变可行比例。
5. 最坏模型目标为$\inf_{\pi\in\Pi_{\mathrm{adm}}}\sup_{Q\in\mathcal P}\mathbb E_Q^\pi[L]$。单步有限行动允许私有随机化，且每个模型给出不随行动改变的结果分布时，目标为$\inf_{q\in\Delta(\mathcal A)}\sup_{Q\in\mathcal P}\sum_aq(a)\mathbb E_Q[\ell(a,Y)]$。固定$Q$后私有随机数与结果独立，模型可针对已确定的$q$取最坏，却不能看到实际抽中行动后再更换；只有限制$q$为点质量时才退化为纯行动公式。
6. 二结果、二行动的损失分别为$(0,1)$和$(1,0)$，候选模型确定产生其中一个结果。每项纯行动最坏损失为$1$，以概率$p$混合后的最坏期望为$\max\{1-p,p\}$，在$p=1/2$达到$1/2$。该反例说明无约束期望下纯行动足够不能推及最坏模型目标；若模型能观察实际行动再选择，须另行定义信息次序。对偶、极小极大交换和局部递推仍各有条件。

### 8.5 本章小结

主要内容：用两阶段路线任务连接策略、轨迹、价值与优化，强调期望最优、尾部风险与逐轨迹安全需要分别评价。

论证与表述逻辑：

1. 同一两阶段路线任务串起了本章四个步骤。策略先规定走捷径的概率$p$，再与环境共同产生概率为$1-p,0.8p,0.2p$的三条轨迹；给每条轨迹计价后，期望损失为$2-0.8p$，尾部指标和违规概率还描述它的其他后果。
2. 平均收益、一次实现收益和尾部损失不是同一个对象。VaR给出分位阈值，CVaR平均最坏尾部，并在分位原子上按需要补足概率质量。
3. 价值迭代收敛描述的是计算序列$V^{(k)}$，闭环状态收敛描述的是执行轨迹$x_t$，二者不是同一个时间轴上的同一结论。

## 第9章 多方策略的响应与演化

正文：[04-multi-agent-response-and-evolution.tex](../../tex/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/04-multi-agent-response-and-evolution.tex)。

章首主线：双加热器把给定环境中的单方最优选择扩为相互响应的问题；本章依次明确合法策略与信息、给定策略的收益、获利偏离的检验、指定规则下的更新轨迹，以及轨迹持续变化时的累计保证。

### 9.1 策略的多方行动与信息

主要内容：从联合行动和可用信息建立多方决策的共同对象，区分单轮随机行动、开局抽取完整计划与信息集上的局部随机化。

论证与表述逻辑：

1. 双加热器说明一人的行动后果依赖另一人的选择，有限战略式与矩阵形式记录联合行动及各方收益。
2. 匹配硬币说明固定行动可能被针对，以概率单纯形表示独立混合策略，并把它与共同装置产生的相关建议区分。
3. 三张牌质询把多步计划展开为历史树，以信息集限制行动规则，再用完全回忆刻画混合计划与行为策略的实现等价。

#### 9.1.1 参与者与联合行动

主要内容：以两台加热器共同推动温度为入口，明确参与者、联合行动与各方收益，区分有限行动模型和本章另行计算的连续调温模型。

论证与表述逻辑：

1. 定义有限战略式博弈，再将双人有限行动写成两张收益矩阵，零和时才可用一张矩阵及其相反数概括双方收益。
2. 给出双输入温度递推、局内先观察后同时行动的信息约定，以及温差和能耗组成的各方成本，最大化收益取成本的相反数。
3. 明确前章温度阶段成本按行动前的$x_t$计价，本例改按行动后形成的$x_{t+1}$计价，使本轮两人输入的共同影响直接进入本轮温差成本。后文温度例的单步响应按这一新约定求解；改变计价时点时须重新推导相应的最佳响应。
4. 在无扰动、目标温差为2的反馈算例中，维持目标要求两人基准输入之和为0.4，状态误差的衰减由总反馈增益决定，此计算不证明反馈是最佳响应。

#### 9.1.2 纯策略与混合策略

主要内容：由匹配硬币中固定选面容易被针对，引出在行动上随机化的混合策略，并以概率单纯形给出合法策略域。

论证与表述逻辑：

1. 纯策略选择一个行动，混合策略选择行动的概率分布，单轮抽样不等于在一局中把不同行动各执行一部分。
2. 联合策略记录各人的规则，独立抽样产生乘积分布，共同装置的建议则可以相关，边缘相同不保证联合收益相同。
3. 匹配硬币的两方策略由$p,q\in[0,1]$表示，联合策略空间是概率正方形，四个纯行动组合只是其顶点。

#### 9.1.3 行动历史与可用信息

主要内容：三张牌质询任务用隐藏高、低牌与公共中牌区分真实历史和参与者可见信息，使完整计划的可执行性成为明确约束。

论证与表述逻辑：

1. 定义有限前缀封闭历史树、终止历史、行动者与机会概率，再用同一信息集收集参与者当时无法区分的决策历史。
2. 同一信息集必须有相同合法行动集，参与者2看不见隐藏牌，故高、低牌质询后的应对概率必须相同。
3. 图表并列实际节点和可见信息，说明信息集不同于用于预测未来的Markov状态，公开牌面会改变合法策略集而成为另一个博弈。
4. 完整策略还要为零概率到达的信息集规定行动，Nash的事前偏离比较不自动包含序贯理性，后者另需信念及相容条件。

#### 9.1.4 完整策略与行为策略

主要内容：比较开局随机抽取完整纯计划与到达信息集后局部随机化，以完全回忆保证二者面对任意固定对手和机会策略时具有相同终局分布。完全回忆包括本人过去信息和行动；缺少该条件只是不再具有一般实现等价保证，不推断每个有遗忘的博弈都必不等价。补充遗忘第一步行动的树和终局概率表：合并信息集限制第二步的条件选择，混合完整计划与逐处独立随机化虽有相同边缘，终局联合规律却不同，直观呈现完全回忆条件的作用。

论证与表述逻辑：

1. 三张牌列出四项完整计划与$b_H,b_L,c$三个行为概率，再定义完全回忆为同一信息集内本人既往信息集和行动序列一致。
2. Kuhn实现等价的正向构造按唯一本人前缀对混合计划取条件概率，沿路径用链式法则证明终局概率相同，零概率前缀可任意补全。
3. 反向构造在开局独立抽取各信息集的行动并组成完整计划，未经过的信息集求和后贡献因子1，从而保留各终局概率。
4. 忘记本人第一步行动的反例展示跨时相关性无法由独立局部随机化复现，三张牌的等价表示只验证实现等价，其价值与最优性留待后文检验。

### 9.2 策略的多方价值

主要内容：在联合策略固定后计算各方期望收益，分别处理行动表、历史树和另行定义的联盟价值，避免把收益评价混同于后续改进或均衡判断。

论证与表述逻辑：

1. 行动表按联合行动概率加权，历史树按终局路径概率加权，机会概率只计入一次。
2. 固定行动集合而改变收益规则，比较零和、一般和与共同收益，并用Pareto改进区分共同改变与单方偏离。
3. 合作共享信息时先声明联盟能取得的价值及转移语义，再以加入顺序平均边际贡献形成Shapley分配。

#### 9.2.1 给定策略下的收益计算

主要内容：把已给定的联合行动规则转成各方期望收益，使单步矩阵和多步历史树采用一致的概率加权原则。

论证与表述逻辑：

1. 独立混合策略使用各方概率的乘积，相关建议则直接使用联合分布，不能擅自拆成边缘乘积。
2. 历史树将到达概率按本人、对手及机会归组，再对终止历史求和，以三张牌核对行为式与战略式的同一整局价值。

##### 9.2.1.1 联合行动下的期望收益

主要内容：独立抽样的联合行动概率为各方概率之积，据此延拓纯行动收益，并在双人矩阵中写成双线性期望收益。

论证与表述逻辑：

1. 一般$n$人收益按所有联合行动求和，双人零和时用$\boldsymbol{x}^{\top}\boldsymbol{M}\boldsymbol{y}$记录行方收益，列方收益取其相反数。
2. 若共同装置给出相关联合分布$\mu$，应直接按$\mu$加权，不能以各方边缘概率的乘积替换。
3. 匹配硬币得到$u_1(p,q)=(2p-1)(2q-1)$，以给定概率复算收益，同时明确评价结果尚未检验参与者是否愿意改变策略。

##### 9.2.1.2 行动历史下的整局价值

主要内容：沿历史相乘的行动概率确定各终局权重，再以终局收益求和得到整局价值，策略本身定义的续局概率不要求对零概率事件作除法。

论证与表述逻辑：

1. 把路径概率分成本人行动因子和对手、机会因子，说明这只是按行动者归组乘积，并非额外声称随机变量独立。
2. 三张牌列出六类终局及其概率，得到$u_1=\tfrac12 b_H(1+c)+\tfrac12 b_L(1-3c)$，再比较事前收益与质询后的条件收益。
3. 将四份完整计划代入得到战略式收益矩阵，该矩阵已经对发牌取过期望，后续矩阵计算不能再次乘发牌概率。
4. 回接后续反事实比较将去掉本人到达权重的用途，避免把尚未归一化的局部量误认成条件期望。

#### 9.2.2 对抗与共同收益的价值关系

主要内容：在相同联合行动集合上改变各方收益，区分零和冲突、一般和利益关系和共同收益，明确共同改善与个人响应是不同判断。

论证与表述逻辑：

1. 教学收益表展示零和收益互为相反数、一般和同时具有冲突和共同改善、共同收益逐格相同三种关系。
2. Pareto改进与最优相对于声明的可行方案集比较共同收益变化，不等于固定其他人后的单方偏离条件。
3. 协调博弈中相同边缘的独立抽样与相关建议分别给出收益1和2，双加热器的一步算例再说明共同降低成本后仍需检查个人响应。

#### 9.2.3 合作价值的贡献与分配

主要内容：把共享资源或信息带来的联盟价值作为额外模型，先比较加入者的边际增益，再按参与顺序平均这些增益。

论证与表述逻辑：

1. 声明联盟价值的收益单位、无信息基线与可转移效用假设，区分多方信用分配和单个参与者跨时刻的奖励分配。
2. 不同前驱联盟产生不同边际贡献，Shapley值通过所有参与顺序的等权平均反映这种互补性，其公理刻画与退出稳定性分别检验。

##### 9.2.3.1 联盟价值与边际贡献

主要内容：共享信息时先规定每个联盟能取得并在成员之间转移的总收益，再比较一人加入前后的价值增量。

论证与表述逻辑：

1. 可转移效用博弈由有限参与者集合和满足$v(\varnothing)=0$的联盟价值函数组成，预算平衡要求分配总和等于$v(N)$。
2. 牌面任务可按相对基线减少的最优期望损失定义联盟价值，也可采用收入或成本等口径，不同定义对应不同分配。
3. 边际贡献$v(S\cup\{i\})-v(S)$依赖先到者集合，收益不能在同一尺度转移时须另用非可转移模型，不能直接相加拆分。

##### 9.2.3.2 基于参与顺序的贡献分配

主要内容：在所有加入排列中平均某人的边际贡献得到Shapley值，以四项公理及唯一性证明说明分配规则的依据。

论证与表述逻辑：

1. 公式系数由恰好让联盟$S$先于$i$加入的排列数得到，随机排列解释有效性、对称性、虚设参与者性质和可加性。
2. 唯一性证明将价值函数展开为一致联盟博弈的有限和，以对称性、虚设参与者性质和有效性直接确定任意实系数项，再由可加性确定一般分配。
3. 三位信息提供者的教学价值给出$5/3,5/3,2/3$，第三位单独价值为零但具有互补贡献，故不是虚设参与者。新增六种等权加入次序的边际贡献分段图，再按参与者取平均；第三位在四种次序中各增加1，所以均值为$4/6=2/3$。
4. 若价值改为预测分数，公式分配的是声明的相对基线差，特征缺失语义还取决于条件、边缘或干预选择，预测归因不自动成为因果贡献。

### 9.3 策略的多方响应与均衡

主要内容：按偏离者可用的信息和可联合行动的人数检验候选结果，区分单方最佳响应、共同建议下的条件偏离、联盟退出及协商选择。

论证与表述逻辑：

1. 固定其他人策略求本人最佳响应，相互最佳响应形成Nash条件，不动点证明建立有限混合均衡的存在性。
2. 零和结构把双方最坏情形保证写成线性规划原对偶，给出共同博弈值与Nash鞍点的对应。
3. 收到建议前的固定偏离和收到建议后的映射偏离分别形成CCE与CE，联盟阻挡形成核心，分歧收益与乘积目标则另行选择协商结果。

#### 9.3.1 给定其他策略下的最佳响应

主要内容：固定他人策略后在本人合法策略集中最大化收益，以集合保留所有并列最优选择，并用牌面和温度任务核对响应的依赖对象。

论证与表述逻辑：

1. 有限博弈的收益对本人混合概率线性，至少有一个纯行动最佳，所有并列纯行动的混合也最佳，零和双方分别最大化与最小化同一标量收益。
2. 匹配硬币写出随对手概率切换的响应集合，图中整段并列响应属于静态允许集合，不能当作学习轨迹。
3. 三张牌按应对阈值和高、低牌质询权重求响应，参与者2的概率始终受同一信息集约束。
4. 连续温度模型由严格凸成本求唯一响应，加入输入区间或状态安全条件后必须重新核对约束与共同可行性。

#### 9.3.2 相互最佳响应下的Nash均衡

主要内容：把每人的合法单方偏离同时排除定义Nash均衡，再将联合最佳响应的不动点问题与其存在条件分开论证。

论证与表述逻辑：

1. 用匹配硬币、三张牌与双加热器具体求解相互响应，区分Nash条件、共同最优和状态稳态。
2. 收益并列时保留集合值响应，经Sperner、Brouwer、连续近似选择和Kakutani的证明链，逐项验证有限混合博弈的存在条件。

##### 9.3.2.1 单方偏离与Nash条件

主要内容：联合策略满足Nash条件，是指固定所有其他人以后，每位参与者的最大合法单方改进都为零。偏离可保持相同收益，不能加强成严格吃亏；匹配硬币中对手均匀混合使本人任意混合的期望收益为零，静态条件也不自动保证动态到达。

论证与表述逻辑：

1. 正式不等式对每位参与者和每项可实施替代策略成立，纯策略与混合策略均以同一偏离口径检验。
2. 匹配硬币没有纯均衡而有唯一均匀混合均衡，三张牌的同时响应要求$b_H=1,b_L=c=1/3$。
3. 温度一步模型得到$u_1=u_2=2/3$和成本$8/9$，共同改为$(0.8,0.8)$仍能降低双方成本，故Nash不等于Pareto最优或总成本最优。

##### 9.3.2.2 响应映射与均衡存在

主要内容：本节把并列最佳响应保留为集合值对应，按编号择优可能跳跃，收益恒等时却可得到常值连续选择，因而不能靠编号保证连续；随后建立有限混合均衡的存在证明链。

论证与表述逻辑：

1. 先用二维铺三角形解释相容剖分的覆盖与公共面条件，排除一侧新增顶点而另一侧未切边的情形，由此得到内部小面邻接两块、边界小面邻接一块的计数依据。
2. Sperner引理按边界允许标签作奇偶计数，以维数归纳得到全标号小单纯形，再令网格直径趋零并取紧性子列，证明单纯形上的Brouwer不动点结论。
3. 到紧凸集的欧氏投影把Brouwer结论推广到一般非空紧凸域，随后给出上半连续与紧域、紧值条件下闭图性质的等价判据。
4. 相容细分的公共面使用相同顶点值，重心插值构造连续近似选择，再由Brouwer、紧性、凸值和闭图把近似不动点极限送回原对应，证明Kakutani定理。
5. 联合混合策略域紧凸，有限博弈的期望收益连续且对本人策略线性，故最佳响应非空、紧、凸并有闭图，Kakutani由此给出混合Nash；存在性不保证唯一、计算效率或任意更新的收敛。

#### 9.3.3 零和对抗下的保证与均衡

主要内容：在双方收益互为相反数时，从保证最坏对手下的期望收益进入极小极大问题，用线性规划对偶证明双方保证达到同一博弈值。

论证与表述逻辑：

1. 三张牌的纯计划上下保证有缺口，混合后分别最大化最低收益与最小化最高收益，先得到弱极小极大不等式。
2. 行方以概率归一化和逐列收益下界建立线性规划，拉格朗日乘子形成列方混合策略及逐行收益上界，有限可行最优值下用强对偶证明两值相等。
3. 三张牌的行、列策略分别给出收益下界和上界$2/3$，原对偶可行证书直接确认最优，再将零和鞍点不等式与双方Nash条件对应。
4. 博弈值唯一不等于最优策略唯一，期望保证不等于单局实现收益，非零和或无限连续行动不能直接沿用有限矩阵的同一证明。

#### 9.3.4 共同建议下的偏离与均衡

主要内容：公共装置抽取相关联合行动并私下发送建议，偏离发生在看到建议之前或之后，决定需要检验固定替代还是依建议替代。装置可公开存在，但联合建议分别私下发送；公开整组建议会扩大偏离信息。交叉车流例给通行、停车、碰撞的收益，计算协调与独立随机化的收益差，再按本人建议检验偏离。

论证与表述逻辑：

1. CCE排除事前固定行动偏离，CE排除所有行动映射偏离，有限行动下CE还等价于逐对建议替换的线性约束，零概率建议无需定义条件比值。
2. 固定偏离是映射偏离的特例，独立Nash乘积分布的支持行动又各为最佳响应，因此Nash乘积分布属于CE，CE属于CCE，反向均不普遍成立。
3. 三行动共同收益例构造CCE而非CE，二行动协调例说明同样边缘的相关建议可优于一个独立混合均衡，但不因此优于每个纯Nash均衡。
4. 概率图与表分别显示、列出联合质量，后续把固定和依建议偏离改写为累计遗憾时仍须保留这一联合对象。

#### 9.3.5 合作分配的稳定与协商

主要内容：先以联盟不能获利退出定义可转移收益的合作稳定性，再转向非可转移收益的Pareto前沿和分歧点，按Nash乘积选择协商结果。

论证与表述逻辑：

1. 核心要求总收益完全分配且每个联盟所得不少于独立合作价值，三人多数联盟例证明Shapley值可能不在核心，核心本身也可能为空。
2. Pareto条件通常形成整个前沿，不能唯一选择结果；声明谈判失败收益后，以各人非负合作增益的乘积加入额外协商准则。
3. 可行收益域非空、紧、凸且存在共同严格正增益时，连续性保证最大值达到，正增益区域的对数严格凹性给出唯一收益向量，乘积递增再证明Pareto性质。
4. 效用与分歧点同时正仿射变化只给乘积乘上共同正常数，教学三角域中的两个分歧点分别得到$(3,3)$和$(5/2,7/2)$，说明选择相对于退出收益而定。
5. 非凸域或缺少共同严格增益时不能沿用该唯一性证明，Nash协商解也不因此属于核心或使指定策略更新稳定。

### 9.4 策略的多方演化与稳定

主要内容：从候选结果的偏离检验转向明确的策略更新递推，分别研究不动点附近的扰动、长期极限与循环，以及群体模型中的少量策略入侵。

论证与表述逻辑：

1. 将局内物理时间和跨局更新轮次分开，比较同时响应、交替响应与投影梯度，必要时把历史量和噪声纳入动态状态。
2. 先确认候选均衡是所选映射的不动点，再以局部线性化或直接递推研究稳定，双加热器展示更新次序和步长的作用。
3. 匹配硬币的周期与梯度旋转说明存在均衡不保证轨迹收敛，复制动态与ESS另行检验群体比例变化和稀少策略的入侵。

#### 9.4.1 更新规则与策略序列

主要内容：用$t$表示局内状态时间、$k$表示策略更新轮次，在相同初态、收益和信息条件下定义可实际分析的更新过程。

论证与表述逻辑：

1. 一般更新可依赖可用历史和估计噪声，采用累计遗憾、历史平均或动量时须把这些内部量加入状态，当前策略未必单独决定下一步。
2. 同时最佳响应使用同一个旧组合，交替响应让第二人使用第一人的新选择，并列最优还需声明选择规则，因此两者产生不同联合映射。
3. 投影收益梯度上升保持闭凸策略域的可行性，成本约定则改为下降，投影本身不保证联合收缩或带噪估计满足所需条件。
4. 固定初态的一步双加热器例列出同时与交替响应的前几轮数值，随后交由误差递推证明收敛，有限步观察本身不作结论。

#### 9.4.2 均衡邻域内的扰动与稳定

主要内容：候选均衡先须是所选确定更新映射的不动点，稳定才比较附近初值的长期偏差，渐近稳定还要求偏差趋零。

论证与表述逻辑：

1. 并列响应的任意选择可能移走均衡，投影梯度不动点通常只给一阶条件，各方收益对自身策略凹等条件才支持进一步的最佳响应判断。
2. 在内点连续可微条件下，Jacobian谱半径小于1给出局部渐近稳定的充分条件，出现模大于1的特征值可判不稳定，单位模情形须进一步分析，边界投影和集合值跳变也不能直接套普通线性化。
3. 双加热器同时、交替响应的误差矩阵分别具有特征值$\pm1/2$和$0,1/4$，线性递推对任意初值收敛；同时成本梯度下降另需$0<\eta<1/3$。
4. 这些递推收敛到固定初态的一步Nash输入，状态在固定反馈下的稳定却由$|0.8-k_1-k_2|<1$判断，学习与状态同时运行时须另建联合系统。

#### 9.4.3 长期更新的极限、循环与入侵

主要内容：以匹配硬币明确展示响应和梯度的非收敛轨迹，再由群体复制动态与ESS比较循环、静止和抗入侵这些不同性质。

论证与表述逻辑：

1. 同时最佳响应从纯组合产生四周期，交替响应产生两周期；内部离散梯度的平方半径每轮乘$1+16\eta^2$，触边以后必须按投影规则重新分析。
2. 连续梯度流的非零平面轨道守恒半径且周期为$\pi/2$，$0<r_0<1/2$保证整圆位于合法开概率域，零半径是静止中心，内点$(0.9,0.9)$说明仅有内点初值仍不足以保证整圆合法。
3. 半径恰为$1/2$的圆切触边界，边界规则须另行核对；复制动态按相对收益改变群体占比，保持单纯形，但纯顶点静止不保证Nash或抗入侵。
4. 匹配硬币须用双群体复制方程，其守恒水平集给出一般非圆形周期；对称单群体的ESS比较原策略和稀少新策略面对同一混合群体的收益，并推得其蕴含对称Nash。
5. 两行动ESS算例同时验证内部吸引与顶点可被侵入，结尾区分末次策略、到均衡集合的距离、策略平均和行动经验分布，某条周期的平均正确不保证任意算法低遗憾。

### 9.5 策略的多方累积表现

主要内容：策略持续变化时，在同一已记录损失或对手序列上比较累计差距，建立投影更新和局部CFR的保证，再区分经验联合分布与合法平均策略的均衡结论。

论证与表述逻辑：

1. 外部、内部和交换遗憾分别规定固定行动、逐对原行动替换和整份替换映射，不比较本人改变后对手重新学习的另一套过程。
2. 凸损失下的投影距离递推给出固定比较点的累计界，有限完全回忆下的反事实分解再把各信息集遗憾汇总为整局保证。
3. 一般和以同轮联合行动频数保留相关性，零和以双方合法平均策略控制鞍点间隙，扩展式行为策略须从平均本人实现计划恢复。

#### 9.5.1 固定比较策略下的累计差距

主要内容：先以实际损失减事后最佳固定行动损失定义外部遗憾，再允许依本人原行动作固定替换，以区分外部、内部和交换比较类。

论证与表述逻辑：

1. 无外部遗憾要求累计差距正部除以轮数趋零，实际序列可能优于所有固定行动，故不要求未经截断的负差距也趋零。
2. 交替损失的两行动例区分最佳固定行动与逐轮事后先知，分布期望损失和抽样实际损失也需分别处理。新增12轮累计损失图，始终选$B$与最佳固定行动的损失相同、外部遗憾为零，逐轮先知却无损失；差异来自允许的比较策略集合。
3. 内部遗憾按原行动$a$分组比较统一换成$b$的增益，有限行动下无内部遗憾蕴含无外部遗憾，反向一般不成立。
4. 交换遗憾对所有固定映射$\phi:A\to A$比较总改进，恒等映射保证其非负，它同时替换各类原行动但不允许每轮另选事后最佳行动。
5. 从损失改为收益约定时，差距改写为替代收益减实际收益，正号始终表示偏离有利，后续据此连接CCE和CE条件。

#### 9.5.2 基于投影更新的累计保证

主要内容：当损失逐轮变化时，以同一个固定可行比较点为参照，通过投影非扩张和凸函数次梯度不等式建立累计遗憾界。

论证与表述逻辑：

1. 可行域非空闭凸且直径至多为$D$，当前行动在当前损失揭晓前确定，随后取得范数至多为$G$的真实次梯度并执行固定正步长$\eta$的投影更新。
2. 对任意固定比较点，累计损失差不超过$D^2/(2\eta)+\eta G^2K/2$；当$D,G>0$时取$\eta=D/(G\sqrt K)$，得到$DG\sqrt K$及$O(K^{-1/2})$平均遗憾。
3. 证明展开一次更新到比较点的距离平方，以凸性把内积接到损失差，再跨轮望远镜消去距离项；$D=0$或$G=0$的退化情形另给零上界。
4. 概率单纯形上的两行动例说明线性期望损失的投影更新，未知时域步长和仅观察抽中行动的反馈都需额外论证，低遗憾本身不保证末次策略收敛。

#### 9.5.3 基于局部遗憾的整局保证

主要内容：完整多步计划数迅速增长，局部算法要控制任意完整替代计划，就须拆开本人、对手和机会的到达权重。

论证与表述逻辑：

1. 两层本人决策说明当前很少访问的位置仍可能被替代计划频繁使用，因此局部反事实比较先去掉当前本人前缀权重，保留对手与机会权重。
2. 各信息集用遗憾匹配控制局部差距，再由完全回忆确定唯一本人前缀与信息集森林，将固定替代策略的局部偏离汇总成整局外部遗憾界。

##### 9.5.3.1 信息集上的反事实收益比较

主要内容：反事实价值保留对手与机会到达信息集的权重，去掉当前本人前缀权重，使当前不访问的下游位置仍有学习信号。

论证与表述逻辑：

1. 两层小树中整局收益为$pq$，当$p=0$时改第二步的实际增益虽为零，同时改变上游和下游的完整计划仍可获益，故先以局部量$1-q$保留改进。
2. 正式价值对信息集内历史及后续终局求加权和，牌面例中参与者2的反事实价值与正到达条件期望相差归一化因子，零概率到达时前者仍有定义，且此处不提供因果识别。
3. 将替代行动价值减当前局部价值定义即时反事实遗憾，跨轮累计后按正遗憾归一化产生下一轮策略，并同步累计平均策略所需的本人实现权重。
4. 若各轮局部行动价值差至多为$\Delta_I$，势函数的平方增量及遗憾匹配的零交叉项给出$R_{i,+}^{(K)}(I)\leq\Delta_I\sqrt{|A(I)|K}$。
5. 三张牌的一次更新得到应对与退让的即时遗憾$1/4,-1/4$，下一轮纯应对只描述局部响应，不能由该一步推出收敛或均衡。

##### 9.5.3.2 完全回忆下的局部遗憾汇总

主要内容：以固定完整替代策略的本人到达概率补回局部反事实差距，在有限完全回忆树上证明整局外部遗憾由各信息集正部遗憾之和上界。

论证与表述逻辑：

1. 两层小树的恒等式把同时改变两步的增益分成当前局部改动与替代前缀下的后续改动，为一般树中的逐层拆分提供可复核入口。
2. 一般证明先在逐历史收益中加减中间策略，再对信息集内历史加权求和，保留到下一本人决策前的对手和机会概率。
3. 完全回忆使每个非根信息集有唯一本人前驱，信息集森林的递归因而恰好计算每个位置一次，得到以替代本人前缀权重乘局部差距的整局恒等式。
4. 固定替代策略后跨轮求和，再对行动和完整替代策略取最大，得到$R_i^{(K)}\leq\sum_I R_{i,+}^{(K)}(I)$，结合局部界得到$O(\sqrt K)$整局及$O(K^{-1/2})$平均正遗憾。
5. 结论针对有限完全回忆、固定信息结构和准确遍历完整树的反事实值，遗忘、信息集变化或未控制的采样偏差都需重新检查。

#### 9.5.4 累计保证与平均策略表现

主要内容：把累计偏离界转成均衡误差前先指定平均对象，一般和使用联合行动经验分布，两人零和使用双方合法平均策略。

论证与表述逻辑：

1. 一般和的外部、内部或交换遗憾分别控制经验联合分布的CCE或CE偏离，保留同轮相关性是这一经验分布结论的要求。
2. 零和的收益对双方实现计划分别线性，平均本人序列权重并恢复行为策略以后，双方外部遗憾之和控制平均策略的鞍点间隙。

##### 9.5.4.1 一般和条件下的经验分布保证

主要内容：把实际联合行动的累计偏离不等式除以轮数，得到经验联合分布的近似CCE或CE条件，极限结论不要求经验分布收敛到唯一点。

论证与表述逻辑：

1. 每位参与者的外部遗憾至多$\varepsilon_iK$时，经验联合分布的固定偏离收益至多为$\varepsilon_i$，平均正遗憾趋零和紧性进一步给出CCE极限点及到CCE集合距离趋零。
2. 每个有向替换的平均内部遗憾至多$\varepsilon_i$时，按原行动分组的任意映射改进至多为$|A_i|\varepsilon_i$；直接控制交换遗憾则得到$\varepsilon_i$松弛。
3. 两行动教学序列的一半轮次为$(A,A)$、一半为$(B,B)$，其联合经验分布为CE，边缘平均的乘积却不是Nash，说明独立相乘会丢失需要的相关性。
4. 上述结论针对已记录联合序列，期望损失遗憾转成抽样实际行动遗憾时还需控制随机误差，每轮独立抽样也不消除跨轮共同变化形成的相关性。

##### 9.5.4.2 零和条件下的平均策略保证

主要内容：矩阵策略可直接算术平均，扩展式行为策略一般须按本人到达概率加权，合法平均与零和的分别线性共同把双方遗憾转成鞍点间隙。

论证与表述逻辑：

1. 两层小树中先混合两轮完整计划给出终局概率$1/2$，逐节点等权却给出$1/4$，按本人到达权重平均后恢复$1/2$，本人到达权重各轮相同等特殊情形仍可等权。
2. 实现权重等于本人前缀权重乘当前行动概率，各行动权重之和等于进入该信息集的本人权重，空序列权重为1，唯一本人前驱使这些流量关系及其平均保持一致。
3. 用平均行动实现权重除以平均进入权重恢复行为概率，并从本人前缀为空的根信息集归纳，证明得到的策略实现各轮实现计划的平均，零分母位置可任意补全。
4. 对双方外部遗憾界分别除以轮数，以收益对实现计划的分别线性移入平均，再相加消去逐轮平均收益，得到不超过$\varepsilon_1+\varepsilon_2$的联合可利用度。
5. 三张牌的本人前缀权重均为1，故可直接平均$b_H,b_L,c$；一般和需保留联合频数或等价相关信息，两人零和需形成双方合法平均策略，完整树CFR不以抽取实际联合样本为前提。
6. 上述保证针对平均对象，末次策略仍可能循环，采样CFR另需无偏性、方差与集中工具，不能沿用完整树确定性分解代替有限样本分析。

### 9.6 本章小结

主要内容：把合法信息、固定策略收益、偏离条件、指定更新轨迹和累计保证放回同一多方任务，按各自对象和成立条件收束全章。

论证与表述逻辑：

1. 信息集决定可实施计划，完全回忆既支持混合与行为策略的实现等价，也为局部遗憾分解和合法平均提供唯一本人前缀。
2. 有限混合Nash由不动点证明链保证存在，零和原对偶给出共同博弈值，CE与CCE则按偏离信息区分，均不自动提供任意更新的收敛性。
3. 双加热器的响应收缩与局内状态稳定属于不同递推，匹配硬币的循环、连续轨道和ESS入侵检验也各有规则与比较条件。
4. 投影更新与CFR控制累计遗憾，一般和对应经验联合分布的偏离误差，两人零和对应合法平均策略的联合可利用度，末项与采样保证另需分析。
5. Shapley值分配所定义的贡献，核心排除联盟阻挡，Pareto排除共同改善，Nash乘积在紧凸域、共同严格增益和分歧点下作协商选择，这些性质不能仅凭名称互推。
