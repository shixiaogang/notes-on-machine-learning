# 卷6《模型：概率图模型》：第3部分“学习”大纲

正文入口：[tex/06-probabilistic-graphical-models/03-learning/part.tex](../../tex/06-probabilistic-graphical-models/03-learning/part.tex)。章号按本卷连续编号，以下标题和顺序对应当前入口实际接入的正文。

从数据估计固定图参数或选择结构，区分潜变量、缺失机制、局部归一化和因果识别带来的额外条件。

## 第9章 参数学习

正文：[01-parameter-learning.tex](../../tex/06-probabilistic-graphical-models/03-learning/01-parameter-learning.tex)。

### 9.1 参数学习的定义

主要内容：固定图与数据设计，区分观测字段、主动设置的潜变量和漏记字段，明确点估计与参数后验的学习目标。

论证与表述逻辑：

1. 设$\mathcal{G}=(V,E)$为固定图，$d=|V|$。记全部节点随机变量为$\boldsymbol{W}=(W_1,\ldots,W_d)^\top$，按照数据设计，将其划分为直接记录的字段$\boldsymbol{X}$与模型主动设置的潜变量$\boldsymbol{Z}$，即在固定排列下$\boldsymbol{W}=(\boldsymbol{X}^\top,\boldsymbol{Z}^\top)^\top$。
2. MLE与MAP输出一个参数点。
3. 训练准则决定哪些数据分布受到约束。

### 9.2 观测完整且不含潜变量的参数学习

主要内容：在完整可见记录上比较有向、联合无向与条件无向模型的MLE和MAP，说明局部与全局归一化的不同计算。

论证与表述逻辑：

1. 有向图模型：对有向图，联合分布已经写成局部条件分布的乘积。
2. 联合无向图：联合无向模型通过全局配分函数归一化局部势的乘积。
3. 条件无向图：若目标是根据已经给出的测量$\boldsymbol{x}$预测一组标签$\boldsymbol{y}$，就可以只归一化标签空间。

#### 9.2.1 有向图模型

主要内容：对有向图，联合分布已经写成局部条件分布的乘积。

论证与表述逻辑：

1. 对离散节点，条件概率表（conditional probability table, CPT）逐行列出每种父节点配置下的子节点分布。
2. 连续节点也能利用局部分解。

#### 9.2.2 联合无向图

主要内容：联合无向模型通过全局配分函数归一化局部势的乘积。

论证与表述逻辑：

1. 参数改变一个局部势时，也会改变全局归一化常数。
2. 持久链（persistent chain）在下一次参数更新时沿用上次的链状态，避免每次都从数据重新启动。充分混合的MCMC与有限步持久链使用同一个模型期望公式，区别在于后者依赖跨迭代跟踪的近似；CD还固定采用数据初始化。

#### 9.2.3 条件无向图

主要内容：若目标是根据已经给出的测量$\boldsymbol{x}$预测一组标签$\boldsymbol{y}$，就可以只归一化标签空间。

论证与表述逻辑：

1. 对完整标签训练集$\{(\boldsymbol{x}_j,\boldsymbol{y}_j)\}_{j=1}^n$，以$\lambda\geq0$控制二次正则化，目标及梯度为$\begin{aligned} J(\boldsymbol{\theta}) &=\sum_{j=1}^n \left[\boldsymbol{\theta}^\top\boldsymbol{f}(\boldsymbol{x}_j,\boldsymbol{y}_j) -\log Z_{\boldsymbol{\theta}}(\boldsymbol{x}_j)\right]\\ &\quad-\frac{\lambda}{2}\lVert\boldsymbol{\theta}\rVert_2^2,\\ \nabla_{\boldsymbol{\theta}}J &=\sum_{j=1}^n \left[\boldsymbol{f}(\boldsymbol{x}_j,\boldsymbol{y}_j) -\mathbb{E}_{p_{\boldsymbol{\theta}}(\boldsymbol{Y}\mid\boldsymbol{x}_j)} \boldsymbol{f}(\boldsymbol{x}_j,\boldsymbol{Y})\right]\\ &\quad-\lambda\boldsymbol{\theta} \end{aligned}$推导与无向联合模型相同，只是每次都固定输入再求和。
2. 例如，只有一个二元标签、一个标量特征$f(x,y)=yx$时，$p_\theta(Y=1\mid x)=\operatorname{sigmoid}(\theta x)$。

### 9.3 观测完整但含潜变量的参数学习

主要内容：对主动引入的未观测状态进行边缘化，依次讨论精确EM、广义EM、近似E步及摊销和Wake--Sleep学习。

论证与表述逻辑：

1. 观测数据似然：当前记录可能由潜变量的多种取值产生。
2. 精确EM：将观测量与潜变量合在一起，得到完全数据（complete data）$(\boldsymbol{X},\boldsymbol{Z})$。
3. 广义EM与近似E步：广义EM（generalized EM, GEM）保留精确E步，只要求M步改进同一个$Q$。例如，对$Q$做带回溯检查的梯度上升，或依次改进几个参数块，只要总更新不降低$Q$，就仍能保证观测似然不下降。
4. 摊销推断与Wake--Sleep：变分EM若为每条记录分别保存$q_j$，新记录到来时还要重新求解一个局部优化问题。摊销推断（amortized inference）改用共享映射$q_{\boldsymbol{\phi}}(\boldsymbol{z}\mid\boldsymbol{x})$，由识别参数$\boldsymbol{\phi}$直接把观测映射为近似后验。

#### 9.3.1 观测数据似然

主要内容：当前记录可能由潜变量的多种取值产生。

论证与表述逻辑：

1. 当前记录可能由潜变量的多种取值产生。将这些取值的联合概率加总，才能得到该记录在候选参数下的概率：$\ell(\boldsymbol{\theta}) =\sum_{j=1}^n\log p_{\boldsymbol{\theta}}(\boldsymbol{x}_j) =\sum_{j=1}^n \log\int p_{\boldsymbol{\theta}}(\boldsymbol{x}_j,\boldsymbol{z}_j) \,\mathrm{d}\boldsymbol{z}_j$离散变量把积分换成求和。
2. 每条记录的概率包含潜变量积分，因而对数似然通常无法按完整配置的真实计数直接分解。
3. 为了只研究一个未知量，把过热条件概率固定为另行给定的校准值$p(H=1\mid F=1)=0.8$和$p(H=1\mid F=0)=0.1$，仅学习$\pi=p(F=1)$。

#### 9.3.2 精确EM

主要内容：将观测量与潜变量合在一起，得到完全数据（complete data）$(\boldsymbol{X},\boldsymbol{Z})$。

论证与表述逻辑：

1. 命题（EM的观测似然单调性）：设$\boldsymbol{x}_1,\ldots,\boldsymbol{x}_n$为固定观测，$\boldsymbol{Z}_j$为第$j$条记录的潜变量。对每个$j$，分别在观测空间和潜变量空间上给定$\sigma$有限基准测度$\nu_j$与$\mu_j$；对每个$\boldsymbol{\theta}\in\Theta$，$p_{\boldsymbol{\theta}}(\boldsymbol{x},\boldsymbol{z})$是相对于共同乘积测度$\nu_j\otimes\mu_j$的联合密度。有限离散情形取计数测度，此时该密度就是联合概率质量函数。定义观测边缘密度，并在该边缘正且有限时定义后验密度：$\begin{aligned} p_{\boldsymbol{\theta}}(\boldsymbol{x}_j) &\mathrel{:=}\int p_{\boldsymbol{\theta}}(\boldsymbol{x}_j,\boldsymbol{z})\, \mathrm{d}\mu_j(\boldsymbol{z}),\\ r_{j,\boldsymbol{\theta}}(\boldsymbol{z}\mid\boldsymbol{x}_j) &\mathrel{:=} \frac{p_{\boldsymbol{\theta}}(\boldsymbol{x}_j,\boldsymbol{z})} {p_{\boldsymbol{\theta}}(\boldsymbol{x}_j)},\\ \ell(\boldsymbol{\theta}) &\mathrel{:=}\sum_{j=1}^n \log p_{\boldsymbol{\theta}}(\boldsymbol{x}_j) \end{aligned}$取$\boldsymbol{\theta}^{(t)},\boldsymbol{\theta}^{(t+1)}\in\Theta$，假设对$s\in\{t,t+1\}$及每个$j$都有$0<p_{\boldsymbol{\theta}^{(s)}}(\boldsymbol{x}_j)<\infty$。E步精确取$q_j^{(t)}(\boldsymbol{z})=r_{j,\boldsymbol{\theta}^{(t)}}(\boldsymbol{z}\mid\boldsymbol{x}_j)$，并定义$Q(\boldsymbol{\theta}\mid\boldsymbol{\theta}^{(t)}) \mathrel{:=}\sum_{j=1}^n\int q_j^{(t)}(\boldsymbol{z}) \log p_{\boldsymbol{\theta}}(\boldsymbol{x}_j,\boldsymbol{z})\, \mathrm{d}\mu_j(\boldsymbol{z})$假设对每个$j$及$s\in\{t,t+1\}$，都有$\int q_j^{(t)}(\boldsymbol{z}) \log p_{\boldsymbol{\theta}^{(s)}}(\boldsymbol{x}_j,\boldsymbol{z})\, \mathrm{d}\mu_j(\boldsymbol{z})\in\mathbb{R},$并且$\operatorname{KL}\!\left( q_j^{(t)}\,\middle\|\, r_{j,\boldsymbol{\theta}^{(t+1)}}(\,\cdot\mid\boldsymbol{x}_j) \right) \mathrel{:=}\int q_j^{(t)}(\boldsymbol{z}) \log\frac{q_j^{(t)}(\boldsymbol{z})} {r_{j,\boldsymbol{\theta}^{(t+1)}}(\boldsymbol{z}\mid\boldsymbol{x}_j)} \,\mathrm{d}\mu_j(\boldsymbol{z}) <\infty,$其中不满足绝对连续时按惯例令KL散度为$+\infty$。若新参数满足$Q(\boldsymbol{\theta}^{(t+1)}\mid\boldsymbol{\theta}^{(t)}) \geq Q(\boldsymbol{\theta}^{(t)}\mid\boldsymbol{\theta}^{(t)}),$则$\ell(\boldsymbol{\theta}^{(t+1)})\geq\ell(\boldsymbol{\theta}^{(t)})$。
2. 推导：由$q_j^{(t)}=r_{j,\boldsymbol{\theta}^{(t)}}(\,\cdot\mid\boldsymbol{x}_j)$及后验密度的定义，对$q_j^{(t)}$几乎处处有$\log\frac{q_j^{(t)}(\boldsymbol{z})} {r_{j,\boldsymbol{\theta}^{(t+1)}}(\boldsymbol{z}\mid\boldsymbol{x}_j)} = \log\frac{p_{\boldsymbol{\theta}^{(t)}}(\boldsymbol{x}_j,\boldsymbol{z})} {p_{\boldsymbol{\theta}^{(t+1)}}(\boldsymbol{x}_j,\boldsymbol{z})} +\log\frac{p_{\boldsymbol{\theta}^{(t+1)}}(\boldsymbol{x}_j)} {p_{\boldsymbol{\theta}^{(t)}}(\boldsymbol{x}_j)}$定理中的有限性条件允许对该等式积分并重排有限项。逐个$j$相加得到$\begin{aligned} \ell(\boldsymbol{\theta}^{(t+1)})-\ell(\boldsymbol{\theta}^{(t)}) &= Q(\boldsymbol{\theta}^{(t+1)}\mid\boldsymbol{\theta}^{(t)})\\ &\quad-Q(\boldsymbol{\theta}^{(t)}\mid\boldsymbol{\theta}^{(t)})\\ &\quad+\sum_{j=1}^n \operatorname{KL}\!\left( q_j^{(t)}\,\middle\|\, r_{j,\boldsymbol{\theta}^{(t+1)}}(\,\cdot\mid\boldsymbol{x}_j) \right) \end{aligned}$右侧的$Q$函数之差由假设非负，各KL散度也非负，因此观测对数似然不下降。
3. M步到达旧后验所构下界的最大值，新参数处的后验则已经变化，因而下界与似然产生新的间隙。下一次精确E步更新后验，使下界在新点再次贴合。

#### 9.3.3 广义EM与近似E步

主要内容：广义EM（generalized EM, GEM）保留精确E步，只要求M步改进同一个$Q$。例如，对$Q$做带回溯检查的梯度上升，或依次改进几个参数块，只要总更新不降低$Q$，就仍能保证观测似然不下降。

论证与表述逻辑：

1. 如果后验推断本身难以完成，则可以限制$q$属于某个可计算分布族$\mathcal{Q}$。
2. 随机梯度或有噪声的下界估计，还可能连逐步ELBO单调性都不具备。Monte Carlo E步则用有限样本估计$Q$，其更新需控制采样误差，并核查实际改进。
3. MAP也可以采用EM式更新：E步仍计算给定当前参数的潜变量后验，M步改进$Q(\boldsymbol{\theta}\mid\boldsymbol{\theta}^{(t)})+\log p(\boldsymbol{\theta})$。

#### 9.3.4 摊销推断与Wake--Sleep

主要内容：变分EM若为每条记录分别保存$q_j$，新记录到来时还要重新求解一个局部优化问题。摊销推断（amortized inference）改用共享映射$q_{\boldsymbol{\phi}}(\boldsymbol{z}\mid\boldsymbol{x})$，由识别参数$\boldsymbol{\phi}$直接把观测映射为近似后验。

论证与表述逻辑：

1. Wake--Sleep的两个阶段因此对应不同目标与输入分布。Wake使用摊销后验更新生成参数，Sleep用生成数据训练识别参数；有限随机更新还包含抽样和求解误差。

### 9.4 观测缺失下的参数学习

主要内容：明确缺失机制与可忽略性条件，再说明如何复用未观测变量方法，以及不可忽略缺失的识别困难。

论证与表述逻辑：

1. 缺失变量与缺失机制：以$\boldsymbol{Y}$表示本应完整记录的数据向量，$R_i=1$表示$Y_i$已观测，$R_i=0$表示缺失。
2. 可忽略性：MAR条件下，固定实际观测值后，记录概率与待积分的缺失值无关，因而可从积分中提出。
3. 可忽略缺失下复用未观测变量方法：模型若还含主动设置的潜变量$\boldsymbol{h}_j$，就把未观测量合并为$\boldsymbol{z}_j=(\boldsymbol{y}_{j,\mathrm{mis}},\boldsymbol{h}_j)$；不同记录可以有不同缺失模式，但每次推断都必须固定该记录实际观测到的分量。
4. 不可忽略缺失与可识别性：此时应为$p_{\boldsymbol{\theta},\boldsymbol{\psi}}(\boldsymbol{y},\boldsymbol{r}) =p_{\boldsymbol{\theta}}(\boldsymbol{y}) p_{\boldsymbol{\psi}}(\boldsymbol{r}\mid\boldsymbol{y})$建立联合模型，把$\boldsymbol{R}$作为已观测变量，并对$\boldsymbol{Y}_{\mathrm{mis}}$以及原有潜变量共同边缘化。

#### 9.4.1 缺失变量与缺失机制

主要内容：以$\boldsymbol{Y}$表示本应完整记录的数据向量，$R_i=1$表示$Y_i$已观测，$R_i=0$表示缺失。

论证与表述逻辑：

1. 可用漏记概率依赖哪些值来判断设备记录机制。

#### 9.4.2 可忽略性

主要内容：MAR条件下，固定实际观测值后，记录概率与待积分的缺失值无关，因而可从积分中提出。若还保留参数后验，先验分离$p(\boldsymbol\theta,\boldsymbol\psi)=p(\boldsymbol\theta)p(\boldsymbol\psi)$是一组充分条件：机制因子与其先验的积分有限且为正时，积分$\boldsymbol\psi$只留下与$\boldsymbol\theta$无关的常数。

论证与表述逻辑：

1. 若还保留参数后验，先验分离$p(\boldsymbol\theta,\boldsymbol\psi)=p(\boldsymbol\theta)p(\boldsymbol\psi)$是一组充分条件：机制因子与其先验的积分有限且为正时，积分$\boldsymbol\psi$只留下与$\boldsymbol\theta$无关的常数。
2. 相关先验则可能使该积分仍依赖$\boldsymbol\theta$，此时后验需保留它。
3. 下一小节据此接入每条记录的可见字段。

#### 9.4.3 可忽略缺失下复用未观测变量方法

主要内容：模型若还含主动设置的潜变量$\boldsymbol{h}_j$，就把未观测量合并为$\boldsymbol{z}_j=(\boldsymbol{y}_{j,\mathrm{mis}},\boldsymbol{h}_j)$；不同记录可以有不同缺失模式，但每次推断都必须固定该记录实际观测到的分量。

论证与表述逻辑：

1. 这组记号将两类未观测量接入同一个积分工具，它们在数据获取上的含义仍不同。删除不完整记录会改变拟合所用的记录集合；单次均值或众数填补又省去了条件分布的变动。

#### 9.4.4 不可忽略缺失与可识别性

主要内容：此时应为$p_{\boldsymbol{\theta},\boldsymbol{\psi}}(\boldsymbol{y},\boldsymbol{r}) =p_{\boldsymbol{\theta}}(\boldsymbol{y}) p_{\boldsymbol{\psi}}(\boldsymbol{r}\mid\boldsymbol{y})$建立联合模型，把$\boldsymbol{R}$作为已观测变量，并对$\boldsymbol{Y}_{\mathrm{mis}}$以及原有潜变量共同边缘化。

论证与表述逻辑：

1. 联合模型的可识别性仍需检查。不同的数据分布与缺失机制可能诱导同一个$p(\boldsymbol{y}_{\mathrm{obs}},\boldsymbol{r})$，仅凭现有记录便无法区分它们。

### 9.5 基于分布估计的参数学习

主要内容：把参数本身作为随机对象，比较共轭后验、含未观测量的近似后验及后验预测中的不确定性传播。

论证与表述逻辑：

1. 不含未观测变量的共轭后验：不含未观测变量时，局部统计量不仅能用来找最优点，也能更新参数分布。共轭先验（conjugate prior）是与似然相乘后仍留在同一分布族中的先验，因此可通过更新有限组超参数表示整个后验。
2. 含未观测变量的近似后验：一旦含有潜变量或缺失值，参数后验通常要与未观测变量联合推断；非共轭局部模型和复杂参数共享还会进一步破坏解析形式。
3. 后验预测：得到参数后验后，新设备的状态仍具有随机性，而故障率本身也不完全确定。

#### 9.5.1 不含未观测变量的共轭后验

主要内容：不含未观测变量时，局部统计量不仅能用来找最优点，也能更新参数分布。共轭先验（conjugate prior）是与似然相乘后仍留在同一分布族中的先验，因此可通过更新有限组超参数表示整个后验。

论证与表述逻辑：

1. 在所有节点均已观测、没有参数共享且先验也按节点和CPT行独立分解时，似然的分解使后验同样局部分解：$p(\boldsymbol{\theta}\mid\mathcal{D}) =\prod_{i,a} \operatorname{Dirichlet} (\boldsymbol{\theta}_{i,a}; \boldsymbol{\alpha}_{i,a}+\boldsymbol{N}_{i,a})$数据沿图结构的作用在这里很具体：每条记录只给各节点家庭的相应单元格增加计数。
2. 设备例子也能展示后验保留了多少信息。同一份数据的MLE、MAP与后验均值分别为$1/4$、$3/11$和$7/24$；前两者是不同目标的最优点，第三个数只是后验的一项摘要。

#### 9.5.2 含未观测变量的近似后验

主要内容：一旦含有潜变量或缺失值，参数后验通常要与未观测变量联合推断；非共轭局部模型和复杂参数共享还会进一步破坏解析形式。

论证与表述逻辑：

1. 在共轭的变分更新中，期望计数确实可能作为超参数出现，但那属于特定变分族下的坐标更新。相应局部状态更新通常使用$\exp\{\mathbb{E}[\log\theta_{i,a,k}]\}$，而不是把后验均值代入$\theta$；一般有$\mathbb{E}[\log\theta]\ne\log\mathbb{E}[\theta]$。
2. 若后验在一个内部峰附近集中，还可以用拉普拉斯近似（Laplace approximation），即用峰值附近的二次曲率构造高斯分布。

#### 9.5.3 后验预测

主要内容：得到参数后验后，新设备的状态仍具有随机性，而故障率本身也不完全确定。

论证与表述逻辑：

1. 得到参数后验后，新设备的状态仍具有随机性，而故障率本身也不完全确定。后验预测（posterior predictive）将这两种不确定性合并：在每个可能参数下计算新观测的分布，再按参数后验加权，$p(\boldsymbol{x}_*\mid\mathcal{D}) =\int p_{\boldsymbol{\theta}}(\boldsymbol{x}_*) p(\boldsymbol{\theta}\mid\mathcal{D})\,\mathrm{d}\boldsymbol{\theta}$若预测还涉及新潜变量，应在内层同时消去它们。
2. 对单台设备的Bernoulli故障变量，后验预测恰好等于代入后验均值的结果：$p(F_*=1\mid\mathcal{D})=\mathbb{E}[\pi\mid\mathcal{D}]=7/24$。
3. 条件预测还要说明新输入怎样被处理。纯条件模型把$\boldsymbol{x}_*$视为给定设计，使用$\int p_{\boldsymbol{\theta}}(\boldsymbol{y}_*\mid\boldsymbol{x}_*)p(\boldsymbol{\theta}\mid\mathcal{D})\,\mathrm{d}\boldsymbol{\theta}$。

### 9.6 学习算法分析

主要内容：分析表达与识别、学习和推断耦合、优化可扩展性及结果评价，区分推断误差、求解误差与预测误差。

论证与表述逻辑：

1. 学习与推断的耦合：先从模型表达与学习所需的信息看各节的差异。固定图及局部分布族限定了候选分布：缺少必要的相互作用或使用不合适的局部族时，即使求解充分，也可能无法拟合目标观测分布。
2. 优化与可扩展性：收敛速度的判断需要同时计算每轮成本与达到所需目标差距的轮数。样本数很大时，遍历全部记录可能成为每轮的主要成本。
3. 学习结果的评价：预测新记录时，训练样本的数量与局部配置覆盖决定可用于估计的信息，图结构、参数共享和正则化则限制所选候选的自由度。

#### 9.6.1 学习与推断的耦合

主要内容：先从模型表达与学习所需的信息看各节的差异。固定图及局部分布族限定了候选分布：缺少必要的相互作用或使用不合适的局部族时，即使求解充分，也可能无法拟合目标观测分布。

论证与表述逻辑：

1. 例如，对充分统计量为$\boldsymbol{T}(\boldsymbol{x},\boldsymbol{z})$的无向指数族潜变量模型，平均观测似然梯度为$\begin{aligned} \frac{1}{n}\nabla_{\boldsymbol{\theta}}\ell &=\frac{1}{n}\sum_{j=1}^n \mathbb{E}_{p_{\boldsymbol{\theta}}(\boldsymbol{Z}\mid\boldsymbol{x}_j)} [\boldsymbol{T}(\boldsymbol{x}_j,\boldsymbol{Z})]\\ &\quad-\mathbb{E}_{p_{\boldsymbol{\theta}}(\boldsymbol{X},\boldsymbol{Z})} [\boldsymbol{T}(\boldsymbol{X},\boldsymbol{Z})] \end{aligned}$第一项问的是“这条观测记录可能来自哪些状态”，第二项问的是“模型不附加证据时会产生哪些状态”。
2. 学习的内层推断成本随图结构变化。离散完整有向图可以一次扫描累加家庭计数，但表格存储量约为$\sum_i r_i\prod_{v\in\operatorname{pa}(i)}r_v$，高入度节点仍可能很贵。

#### 9.6.2 优化与可扩展性

主要内容：收敛速度的判断需要同时计算每轮成本与达到所需目标差距的轮数。样本数很大时，遍历全部记录可能成为每轮的主要成本。

论证与表述逻辑：

1. 小批量降低经验项的每轮成本，内层推断仍决定更新的准确性。可把实际更新使用的梯度写成$\widehat{\boldsymbol{g}}^{(t)} =\nabla J(\boldsymbol{\theta}^{(t)}) +\boldsymbol{b}_{\mathrm{inf}}^{(t)} +\boldsymbol{\xi}^{(t)},$其中$\boldsymbol{b}_{\mathrm{inf}}^{(t)}$表示近似推断带来的系统偏差，$\boldsymbol{\xi}^{(t)}$表示中心化后的抽样波动。
2. 收敛诊断还需区分目标误差来自何处。统计误差（statistical error）来自有限数据，即使精确求出样本目标的最优解，也未必接近总体最优参数；推断误差（inference error）来自近似边缘、期望或积分；优化误差（optimization error）则是相对于所选目标尚未充分求解的差距。

#### 9.6.3 学习结果的评价

主要内容：预测新记录时，训练样本的数量与局部配置覆盖决定可用于估计的信息，图结构、参数共享和正则化则限制所选候选的自由度。

论证与表述逻辑：

1. 解释参数时，先区分候选分布与其参数表示。若不同参数产生相同观测分布，就存在不可识别性（non-identifiability）；增加观测数量也只能确定该等价类。
2. 后验预测检查定位已观察数据与模型的哪些统计特征不相容。检查范围也取决于所选统计量，未被检查的结构可能仍有失配。

### 9.7 本章小结

主要内容：归纳数据可见性与估计方式两条交叉维度，说明局部计数、模型期望、后验期望及缺失过程的分工。

论证与表述逻辑：

1. 参数学习根据记录估计固定图模型的局部概率。完整可见的有向模型可直接聚合计数或回归矩，无向归一化与未观测状态则分别引入模型期望和后验期望；缺失字段还涉及记录机制。
2. 算法结论应对应实际目标。精确EM用贴合下界推出观测似然不下降，GEM允许M步只改进同一$Q$；变分EM的两步改进对应ELBO，Monte Carlo E步还需控制抽样误差。
3. 表达能力由固定图、局部分布和参数约束限定；收敛性受目标形状、初始化、内层推断和计算规模影响；泛化性则需用新记录上的预测分数、校准及参数不确定性检验。
4. Bishop的PRML第9章将完整数据估计、潜变量与EM联系起来；Koller与Friedman的教材补充图模型中的充分统计量和缺失机制。

## 第10章 结构学习

正文：[02-structure-learning.tex](../../tex/06-probabilistic-graphical-models/03-learning/02-structure-learning.tex)。

### 10.1 结构学习的定义

主要内容：固定变量与观测后明确待选图、局部分布和结构目标，区分统计依赖结构与可作干预解释的因果结构。

论证与表述逻辑：

1. 我们从同一组变量的完整记录开始。记节点集合为$V=\{1,\ldots,d\}$，随机向量为$\boldsymbol{X}=(X_1,\ldots,X_d)^{\top}$，数据为$\mathcal{D}=\{\boldsymbol{x}_r:r=1,\ldots,n\}$，暂取样本独立同分布。
2. 学习结果应表示数据能够确定的信息。用于预测时，可以选择拟合与复杂度折中的图；保留不确定性时，可以给出结构后验；高斯条件依赖可以用稀疏精度矩阵表示。
3. 候选空间还决定学习的计算规模。$d$个节点共有$2^{\binom d2}$种简单无向图；有向无环图即使固定拓扑序，也有这么多种边集。

### 10.2 有向图结构学习

主要内容：分别以条件独立检验、结构评分和后验形成证据，再通过搜索选择合法有向图，并讨论缺失下的结构EM。

论证与表述逻辑：

1. 条件独立约束：由独立性删边，需要让独立关系确实反映图结构。忠实性（faithfulness）要求分布的条件独立与图上的d-分离一致，排除参数抵消带来的额外独立性。
2. 结构评分与后验：检验逐个考察独立关系，评分则汇总整张图对数据的拟合。先取观测完整、无潜变量的离散模型：$X_i$有$r_i$个状态，父集有$q_i$种配置。
3. 结构空间搜索：评分给定后，搜索仍要找到合法的高分图。局部方法从满足约束的图出发，检查加边、删边、反向的候选，验证无环和领域限制，再选得分增益最大的正增益操作。
4. 观测缺失与结构EM：若部分记录缺少$X_2$，家庭计数$N_{i,j,k}$便无法直接取得。每条记录需先边缘化未测变量，观测似然因此失去简单的节点分解。

#### 10.2.1 条件独立约束

主要内容：由独立性删边，需要让独立关系确实反映图结构。忠实性（faithfulness）要求分布的条件独立与图上的d-分离一致，排除参数抵消带来的额外独立性。

论证与表述逻辑：

1. 离散记录可以按条件配置分层计数。令$N_{a,b,s}$统计$(X_i,X_j,\boldsymbol{X}_S)=(a,b,s)$的次数，点号表示对相应指标求和。
2. 局部误判还会传递到后续步骤。若把$1,3$误判为边缘独立，空分离集可能导致错误碰撞定向；误删边又会缩小后面的候选邻域。

#### 10.2.2 结构评分与后验

主要内容：检验逐个考察独立关系，评分则汇总整张图对数据的拟合。先取观测完整、无潜变量的离散模型：$X_i$有$r_i$个状态，父集有$q_i$种配置。

论证与表述逻辑：

1. 增加边会扩大拟合空间。若$\mathcal{M}(\mathcal{G}_1)\subseteq\mathcal{M}(\mathcal{G}_2)$，则最大对数似然满足$\ell_2\geq\ell_1$，因为大模型至少能令新增依赖不起作用。
2. 多张候选获得支持时，可以保留预测中的结构不确定性。

#### 10.2.3 结构空间搜索

主要内容：评分给定后，搜索仍要找到合法的高分图。局部方法从满足约束的图出发，检查加边、删边、反向的候选，验证无环和领域限制，再选得分增益最大的正增益操作。

论证与表述逻辑：

1. 一次移动的收益还可分解为拟合与复杂度两项。向$X_i$的父集$P$加入$X_j$时，以$\widehat I$表示经验条件互信息，离散BIC增益为$\Delta\operatorname{Score}_{\mathrm{BIC}} =n\widehat I(X_i;X_j\mid\boldsymbol{X}_P) -\frac{\Delta k}{2}\log n$新增条件变量减少的经验条件熵带来第一项，额外自由参数带来第二项。
2. 检验与评分还可以分阶段配合。先用条件独立证据筛选邻接或父集，再在缩小空间内优化BIC、BDe等评分，能降低搜索量；筛选漏掉的真边也因此失去后续竞争机会。

#### 10.2.4 观测缺失与结构EM

主要内容：若部分记录缺少$X_2$，家庭计数$N_{i,j,k}$便无法直接取得。每条记录需先边缘化未测变量，观测似然因此失去简单的节点分解。

论证与表述逻辑：

1. 结构期望最大化（structural expectation maximization，结构EM）用当前图推断缺失量，再据此比较新的图。
2. 近似E步改变的是下界或估计误差：变分更新可提高自身下界，采样误差则可能影响结构接受决定，真实观测似然需另查。新增潜变量或改变状态数还会改变隐空间，应固定候选潜变量再优化，或分别初始化、拟合与比较。

### 10.3 无向图结构学习

主要内容：比较树结构的Chow--Liu优化、高斯精度矩阵选择、离散高阶结构与潜变量情形的学习。

论证与表述逻辑：

1. 树结构与Chow--Liu算法：先把候选限制为有限离散变量的树，每棵树保留$d-1$条成对连接。任选根并向外定向后，每个非根节点只有一个父节点且没有碰撞，因此无向树分解也能写为有向条件分解。
2. 高斯图结构学习：连续变量的条件依赖在高斯情形也有简洁表示。
3. 离散与高阶Markov网络结构学习：一般离散分布需要直接选择相互作用。
4. 潜变量结构的学习：稠密观测关系还可能由共同隐变量产生。此时直接恢复观测边缘图，会把共同隐变量造成的关系与观测变量之间的条件关系混在一起。

#### 10.3.1 树结构与Chow--Liu算法

主要内容：先把候选限制为有限离散变量的树，每棵树保留$d-1$条成对连接。任选根并向外定向后，每个非根节点只有一个父节点且没有碰撞，因此无向树分解也能写为有向条件分解。

论证与表述逻辑：

1. 命题（Chow--Liu最优树）：设$V=\{1,\ldots,d\}$为有限节点集合，每个$X_i$取值于有限非空状态空间，数据由$n\geq1$条完整记录组成。假定每个声明状态$a$均有$\widehat p_i(a)>0$；成对经验边缘允许取零。候选模型类由$V$上的全部生成树及其不受额外参数约束的局部概率表组成。定义自然对数下的经验互信息$\widehat I(X_i;X_j) =\sum_{a,b}\widehat p_{i,j}(a,b) \log\frac{\widehat p_{i,j}(a,b)} {\widehat p_i(a)\widehat p_j(b)}$其中$\widehat p_{i,j}(a,b)=0$的项按$0\log 0=0$解释。
2. 推导：固定候选树$\mathcal{T}$，选根$o$，令$\pi(i)$表示非根节点$i$的父节点。树分布的局部条件分解为$q_{\mathcal{T}}(\boldsymbol{x}) =q_o(x_o)\prod_{i\ne o}q_i(x_i\mid x_{\pi(i)})$对数似然分别作用于根边缘和条件表各行。每行在概率和为1的约束下独立极大化，得到$q_o=\widehat p_o$、$q_i=\widehat p_{i,\pi(i)}/\widehat p_{\pi(i)}$。
3. 树约束同时简化学习与推断，也排除了环和不可约高阶作用。总体分布超出树族时，算法仍只能返回最佳树近似；互信息差异小时，抽样波动可能改变所选边。

#### 10.3.2 高斯图结构学习

主要内容：连续变量的条件依赖在高斯情形也有简洁表示。

论证与表述逻辑：

1. 由样本计算$\widehat{\boldsymbol{\Sigma}}=n^{-1}\sum_r(\boldsymbol{x}_r-\overline{\boldsymbol{x}})(\boldsymbol{x}_r-\overline{\boldsymbol{x}})^{\top}$，高斯负对数似然去常数并缩放后成为$-\log\det\boldsymbol{K}+\operatorname{tr}(\widehat{\boldsymbol{\Sigma}}\boldsymbol{K})$。
2. 例如取以下精度与协方差：$\boldsymbol{K}= \begin{pmatrix} 2&-1&0\\ -1&2&-1\\ 0&-1&2 \end{pmatrix}, \qquad \boldsymbol{\Sigma}=\frac14 \begin{pmatrix} 3&2&1\\ 2&4&2\\ 1&2&3 \end{pmatrix}$两矩阵相乘为单位阵，精度矩阵顺序主子式为$2,3,4$，故正定。

#### 10.3.3 离散与高阶Markov网络结构学习

主要内容：一般离散分布需要直接选择相互作用。

论证与表述逻辑：

1. 一般离散分布需要直接选择相互作用。先规定特征字典$\{f_a(\boldsymbol{x}_{C_a})\}$，$C_a\subseteq V$表示每个特征涉及的节点，再用有限状态的正指数模型表示概率：$p_{\boldsymbol{\theta}}(\boldsymbol{x}) =\exp\!\left\{\sum_a\theta_a f_a(\boldsymbol{x}_{C_a}) -A(\boldsymbol{\theta})\right\}$参数的非零模式决定哪些相互作用参与模型。
2. 梯度含模型期望，每轮都要进行推断；大团或大树宽会反复增加这项成本。伪似然（pseudolikelihood）改用各节点条件概率的乘积$\prod_{r,i}p_{\boldsymbol{\theta}}(x_{r,i}\mid\boldsymbol{x}_{r,-i})$。
3. 成对边缘还可能隐藏高阶关系。以下正分布给出一个三变量反例：$p(x_1,x_2,x_3) =\frac{\exp(\theta x_1x_2x_3)}{8\cosh\theta}, \qquad x_i\in\{-1,1\},\quad \theta\ne0$消去任一变量，分子变为$2\cosh\theta$，每对边缘都是$1/4$，故成对互信息为零。

#### 10.3.4 潜变量结构的学习

主要内容：稠密观测关系还可能由共同隐变量产生。此时直接恢复观测边缘图，会把共同隐变量造成的关系与观测变量之间的条件关系混在一起。

论证与表述逻辑：

1. 取$X_i=Z+\varepsilon_i$，$i=1,2,3$，并令$Z,\varepsilon_1,\varepsilon_2,\varepsilon_3$相互独立且均为标准高斯。
2. 若某分量同时稀疏、低秩，它可以在两项间移动而不改变差，精确边缘精度也可能无法确定唯一分解。满足识别条件时，$\boldsymbol{L}$的秩表示有效潜在维数，潜变量的物理个数、旋转与含义仍需额外信息。

### 10.4 因果发现

主要内容：加入因果假设和识别目标，比较观测及干预数据能确定的关系，明确等价类和不可识别边界。

论证与表述逻辑：

1. 因果假设与识别目标：因果Markov性要求每个变量在给定其直接原因后，与非后代独立；忠实性则要求分布中的条件独立都由图上的d-分离解释。
2. 基于观测数据的因果发现：PC在因果Markov性、忠实性、充分性、无环性及准确独立判定下返回CPDAG，有限样本返回其估计。GES则需要评分等价、可分解且局部一致，真实分布忠实于候选有向图，并满足固定维大样本条件。
3. 基于干预数据的因果发现：观测和干预的差别可以继续用计数表说明。观测$X_2=1$时，$X_1=1$的频率为$0.9$；外部设置$X_2$却改变了数据产生方式。
4. 因果发现的边界：不确定性需要按来源判断。样本误差使检验和评分偏离总体结果，增加同类记录有机会降低它。

#### 10.4.1 因果假设与识别目标

主要内容：因果Markov性要求每个变量在给定其直接原因后，与非后代独立；忠实性则要求分布中的条件独立都由图上的d-分离解释。

论证与表述逻辑：

1. 当前变量是否覆盖共同原因，也影响图的解释。因果充分性（causal sufficiency）要求它们的共同原因都已观测，即当前模型没有遗漏潜在混杂。
2. 因果充分、无环且忠实时，观测独立信息一般确定CPDAG。允许潜变量后，需表示边缘化留下的关系。
3. 多张MAG也可能具有相同独立关系，部分祖先图（partial ancestral graph, PAG）保留这类图共同的端点信息。

#### 10.4.2 基于观测数据的因果发现

主要内容：PC在因果Markov性、忠实性、充分性、无环性及准确独立判定下返回CPDAG，有限样本返回其估计。GES则需要评分等价、可分解且局部一致，真实分布忠实于候选有向图，并满足固定维大样本条件。

论证与表述逻辑：

1. 潜在混杂会改变需要检查的分离集合。快速因果推断算法（fast causal inference, FCI）扩展PC的搜索范围并采用祖先图定向规则，在相应Markov性、忠实性和准确独立信息下输出PAG。
2. 分布形状可以提供独立关系之外的方向信息。线性非高斯无环模型（linear non-Gaussian acyclic model, LiNGAM）以独立扰动驱动各节点：$X_j=\sum_{i\in\operatorname{pa}(j)}b_{j,i}X_i+\varepsilon_j,$图取无环，扰动相互独立、非高斯且方差有限非零，并排除未观测混杂。
3. 非线性函数也可能使方向不对称。加性噪声模型（additive noise model, ANM）取$Y=f(X)+\varepsilon$、$\varepsilon\perp X$；在满足相应光滑性、非退化和可识别性条件的模型中，反向无法同时写成$X=g(Y)+\eta$、$\eta\perp Y$。

#### 10.4.3 基于干预数据的因果发现

主要内容：观测和干预的差别可以继续用计数表说明。观测$X_2=1$时，$X_1=1$的频率为$0.9$；外部设置$X_2$却改变了数据产生方式。

论证与表述逻辑：

1. 为计算这种改变，完美干预（perfect intervention）替换目标节点的机制、切断它对原父节点的依赖，同时保持其他机制。
2. 路线可以交叉：ANM可使用回归及独立检验，连续优化也可处理特定函数模型。识别能力由数据和模型条件决定，求解工具规定如何利用这些信息。

#### 10.4.4 因果发现的边界

主要内容：不确定性需要按来源判断。样本误差使检验和评分偏离总体结果，增加同类记录有机会降低它。

论证与表述逻辑：

1. 等价类中的未定向边和PAG圆圈保留的是资料尚未确定的信息。领域知识可以排除候选，应标明它贡献的方向；函数形式可以缩小等价范围，也需核验对应假设。
2. 结构发现之后，干预效应是否可计算仍是另一项识别问题，do演算和反事实查询有各自定义及条件。本节得到的部分结构为这些查询提供约束，具体效应和个体反事实还需按对应问题分析。

### 10.5 算法分析

主要内容：分别检查统计一致性、有限样本误差、搜索复杂度和结构评价，说明预测质量与图恢复并非同一目标。

论证与表述逻辑：

1. 统计一致性与有限样本误差：先把可识别目标记为$\mathcal{C}^{*}$，例如CPDAG；结构一致性（structural consistency）要求$\mathbb{P}(\widehat{\mathcal{C}}_n=\mathcal{C}^{*})\to1$。
2. 计算复杂度与可扩展性：计算成本要按实际搜索规模估计。PC枚举条件集并逐项检验；整个过程中候选邻域至多$q$时，粗略检验数为$O(d^2 2^q)$，总时间还乘单次检验成本。
3. 结构评价与稳定性：仿真有已知生成结构时，可分别测量骨架与方向。骨架精确率为正确边数除以预测边数，召回率为正确边数除以真实边数，零分母规则需预设。

#### 10.5.1 统计一致性与有限样本误差

主要内容：先把可识别目标记为$\mathcal{C}^{*}$，例如CPDAG；结构一致性（structural consistency）要求$\mathbb{P}(\widehat{\mathcal{C}}_n=\mathcal{C}^{*})\to1$。

论证与表述逻辑：

1. PC需要全部相关独立判定同时正确。若检验集合大小为$M$、每项错误概率至多$\delta$，联合界给出至少一项检验出错的概率至多$M\delta$，无需检验独立。
2. 树的稳定性可以由边权间隔直接说明。取$d\geq3$且总体最大权生成树唯一，对非树边$e$与其连接路径上的树边$f$，定义$\Delta=\min_{e\notin E_{\mathcal{T}^{*}}} \min_{f\in\operatorname{path}_{\mathcal{T}^{*}}(e)} \{I_f-I_e\}$若$\Delta>0$且所有互信息估计误差小于$\Delta/2$，非树边与路径边的次序保持，最大权树也保持。

#### 10.5.2 计算复杂度与可扩展性

主要内容：计算成本要按实际搜索规模估计。PC枚举条件集并逐项检验；整个过程中候选邻域至多$q$时，粗略检验数为$O(d^2 2^q)$，总时间还乘单次检验成本。

论证与表述逻辑：

1. 离散有向图可缓存局部评分，候选父集数量仍可能指数增长。预计算最佳父集表后，常见动态规划递推约需$O(d2^d)$时间，表的准备及内存另计；整数规划的分支搜索同样可能指数增长。
2. 状态数有界时，Chow--Liu以$O(nd^2)$时间汇总成对计数，再以稠密Prim的$O(d^2)$或排序Kruskal的$O(d^2\log d)$求树。
3. 稠密NOTEARS每次残差乘法约需$O(nd^2)$，矩阵指数通常需$O(d^3)$规模的线性代数，总时间还乘内部优化及惩罚更新轮数。

#### 10.5.3 结构评价与稳定性

主要内容：仿真有已知生成结构时，可分别测量骨架与方向。骨架精确率为正确边数除以预测边数，召回率为正确边数除以真实边数，零分母规则需预设。

论证与表述逻辑：

1. 领域知识也可明确限制候选。禁止$i\to j$就排除$X_j$父集中含$X_i$的选项，必选$i\to j$则保留包含$X_i$的父集；时间顺序排除逆时间箭头。

### 10.6 本章小结

主要内容：归纳独立证据、模型得分与合法搜索的分工，说明可识别性、精确求解和可扩展性的不同条件。

论证与表述逻辑：

1. 从记录到图，需要分别判断局部独立证据、整体模型得分和合法空间搜索。检验说明哪些联系可由给定变量隔断，评分权衡拟合与复杂度，搜索组织候选比较。
2. 同一张计数表可支持无向链、观测等价类及结构后验，却不能仅由频率选定因果方向。缺失观测引入后验统计量，潜变量边缘化可能使稀疏条件图变稠密；改变的不只是运算，也包括可识别对象。
3. Koller与Friedman的教材进一步展开条件独立检验与评分搜索，可按本章的计数、等价类和搜索目标继续阅读。
