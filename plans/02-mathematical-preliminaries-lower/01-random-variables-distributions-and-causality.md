# 卷2《数学准备：概率、因果与决策》：第1部分“随机变量、分布与因果响应”大纲

正文入口：[tex/02-mathematical-preliminaries-lower/01-random-variables-distributions-and-causality/part.tex](../../tex/02-mathematical-preliminaries-lower/01-random-variables-distributions-and-causality/part.tex)。章号按本卷连续编号，以下标题和顺序对应当前入口实际接入的正文。

先建立随机对象及其生成与推断，再比较和优化概率分布，最后讨论改变生成机制后的因果响应及识别条件。

## 第1章 随机变量

正文：[01-random-variables.tex](../../tex/02-mathematical-preliminaries-lower/01-random-variables-distributions-and-causality/01-random-variables.tex)。

### 1.1 随机对象的表示

主要内容：用概率空间与可测映射规定随机对象的生成，比较完整分布、数值特征、分布模型以及随机序列的表示。

论证与表述逻辑：

1. 随机变量与概率空间的界定：设一次带噪观测只能取有限个结果$\Omega=\{\omega_1,\ldots,\omega_m\}$，并为每个结果指定权重$p_j\geq0$，满足$\sum_{j=1}^{m}p_j=1$。
2. 随机变量的分布表示：$X$在实数轴上诱导的概率测度称为它的分布（distribution）：$\mathbb{P}_X(B) =\mathbb{P}(X\in B),\qquad B\in\mathcal{B}(\mathbb{R})$分布函数$F_X(x)=\mathbb{P}(X\leq x)$单调不减、右连续，并满足$\lim_{x\to-\infty}F_X(x)=0$与$\lim_{x\to\infty}F_X(x)=1$。
3. 随机变量的数值特征：完整分布能回答所有可测取值事件的概率，但一次计算往往只需要一个平均或波动尺度。数值特征通过对分布积分提取这些量。
4. 随机变量的分布模型表示：一次试验的成功标记只能取零或一，固定次数中的成功数取整数，等待时间和随机比例则分别有非负与区间取值限制。分布模型要先满足这些取值要求，再说明各个概率由什么假设决定。
5. 随机序列与过程的表示：反复测量得到的$X_1,X_2,\ldots$必须一起定义，才能说明两次读数是否共享噪声。索引$n$记录测量轮次；把轮次换成连续时间后，同样的思路给出随机过程。

#### 1.1.1 随机变量与概率空间的界定

主要内容：用概率空间描述基础结果及其概率，再用可测映射将基础结果转换成读数或向量，区分一次实现与完整规则。

论证与表述逻辑：

1. 先从有限结果的权重推广到事件族与概率测度，说明可列可加性以及补事件、单调极限的概率性质。
2. 再要求读数落入任一可测范围的原像都是事件，以此建立随机变量和随机向量；实值情形可用半无限区间核验。
3. 最后以同一基础结果到不同读数的映射说明变量、实现值与联合抽样规律的区别，指出重复使用规则不自动产生独立性。

#### 1.1.2 随机变量的分布表示

主要内容：用诱导概率测度保存随机变量的取值规律，比较分布函数、离散质量与相对于参考测度的密度，并说明密度存在和唯一的条件。

论证与表述逻辑：

1. 先定义读数事件的概率和分布函数，再区分点质量与密度，强调密度数值必须连同参考测度解释。
2. 从有限分块上的概率比进入绝对连续，说明参考测度看不到的正质量无法靠重加权恢复。
3. 在σ有限条件下给出Radon--Nikodym表示：先对有限测度之和建立平方可积空间中的有界泛函，用Riesz表示构造权重，再由绝对连续排除坏集合并证明几乎处处唯一。
4. 最后通过可数有限分块拼接到σ有限情形，说明该结论给出可测密度而不自动给出逐点有界的密度比。

#### 1.1.3 随机变量的数值特征

主要内容：完整分布能回答所有可测取值事件的概率，但一次计算往往只需要一个平均或波动尺度。数值特征通过对分布积分提取这些量。

论证与表述逻辑：

1. 示例（带噪观测的平均目标）：设未知信号为$\theta$，观测为$Y=\theta+\varepsilon, \qquad\mathbb{E}[\varepsilon]=0$只要$\varepsilon$可积，就有$\mathbb{E}[Y]=\theta$。
2. 变换还有一个有限低阶矩所没有的性质：保留完整的特征函数，就保留了分布。
3. 命题（变换函数的分布唯一性）：同维随机向量的特征函数在所有实向量参数上相同，当且仅当它们的分布相同。若两个矩母函数都在原点的某个共同开邻域内有限，并在该邻域内相同，它们也确定相同的分布。

#### 1.1.4 随机变量的分布模型表示

主要内容：一次试验的成功标记只能取零或一，固定次数中的成功数取整数，等待时间和随机比例则分别有非负与区间取值限制。分布模型要先满足这些取值要求，再说明各个概率由什么假设决定。

论证与表述逻辑：

1. 离散取值下的分布表示：Bernoulli分布以参数$p\in[0,1]$描述一次二元结果：$\mathbb{P}(X=x)=p^x(1-p)^{1-x}, \qquad x\in\{0,1\},$且$\mathbb{E}X=p$、$\operatorname{Var}(X)=p(1-p)$。
2. 连续取值下的分布表示：指数分布以速率$\lambda>0$描述等待时间，密度为$f_T(t)=\lambda e^{-\lambda t}\mathbb I_{\{t\geq0\}}$其均值为$1/\lambda$、方差为$1/\lambda^2$，并对$s,t\geq0$满足无记忆性：$\mathbb{P}(T>s+t\mid T>s)=\mathbb{P}(T>t)$无记忆性只适用于已经等待的时长不改变剩余等待分布，不表示不同等待时间自动独立。
3. 基于指数族的参数化表示：Poisson计数和高斯读数具有不同的取值空间，但其密度中的参数依赖都能集中到少量摘要与一个归一化项。指数族把这种共同结构写出来，使均值、协方差和似然计算能够复用同一组公式。

##### 1.1.4.1 离散取值下的分布表示

主要内容：Bernoulli分布以参数$p\in[0,1]$描述一次二元结果：$\mathbb{P}(X=x)=p^x(1-p)^{1-x}, \qquad x\in\{0,1\},$且$\mathbb{E}X=p$、$\operatorname{Var}(X)=p(1-p)$。

论证与表述逻辑：

1. Poisson计数没有固定的最大次数；二项计数的上界则是已知试验次数$n$。二者不能只按均值接近就视为同一个模型。

##### 1.1.4.2 连续取值下的分布表示

主要内容：指数分布以速率$\lambda>0$描述等待时间，密度为$f_T(t)=\lambda e^{-\lambda t}\mathbb I_{\{t\geq0\}}$其均值为$1/\lambda$、方差为$1/\lambda^2$，并对$s,t\geq0$满足无记忆性：$\mathbb{P}(T>s+t\mid T>s)=\mathbb{P}(T>t)$无记忆性只适用于已经等待的时长不改变剩余等待分布，不表示不同等待时间自动独立。

论证与表述逻辑：

1. 高斯分布（Gaussian distribution，也称正态分布）$X\sim\mathcal{N}(\mu,\sigma^2)$具有密度$f_X(x) =\frac{1}{\sqrt{2\pi\sigma^2}}\exp\left\{-\frac{(x-\mu)^2}{2\sigma^2}\right\},\qquad \sigma^2>0$其均值为$\mu$，方差为$\sigma^2$。
2. 若其协方差$\boldsymbol{\Sigma}$正定，多元高斯密度为$p(\boldsymbol{x}) = \frac{1}{(2\pi)^{d/2}\det(\boldsymbol{\Sigma})^{1/2}} \exp\left\{ -\frac12 (\boldsymbol{x}-\boldsymbol{\mu})^{\top} \boldsymbol{\Sigma}^{-1} (\boldsymbol{x}-\boldsymbol{\mu}) \right\}$奇异协方差仍定义高斯分布，但它集中在低维仿射子空间上，不具有相对于$d$维Lebesgue测度的密度。
3. 定义（卡方分布）：若$G_1,\ldots,G_k$相互独立且都服从标准高斯分布$\mathcal N(0,1)$，则称$Z=\sum_{j=1}^{k}G_j^2$服从自由度为$k$的卡方分布（chi-square distribution），记为$Z\sim\chi_k^2$，其中$k$为正整数。

##### 1.1.4.3 基于指数族的参数化表示

主要内容：Poisson计数和高斯读数具有不同的取值空间，但其密度中的参数依赖都能集中到少量摘要与一个归一化项。指数族把这种共同结构写出来，使均值、协方差和似然计算能够复用同一组公式。

论证与表述逻辑：

1. 定义（指数族）：在可测空间上固定一个$\sigma$有限参考测度$\mu$，非负可测基准项$h$和可测向量函数$\boldsymbol T$。一类由$\boldsymbol{\eta}$索引的分布若都被$\mu$支配，且能写成$\frac{\mathrm{d}P_{\boldsymbol{\eta}}}{\mathrm{d}\mu}(x) = h(x)\exp\left\{ \boldsymbol{\eta}^{\top}\boldsymbol{T}(x)-A(\boldsymbol{\eta}) \right\},$就称为指数族（exponential family）。负责归一化的对数配分函数为$A(\boldsymbol{\eta}) =\log\int h(x)e^{\boldsymbol{\eta}^{\top}\boldsymbol{T}(x)}\,\mathrm{d}\mu(x),$自然参数空间由该积分严格为正且有限的参数组成；所用参数集合可以是这个空间的子集。
2. Bernoulli分布提供另一个核对。取$0<p<1$，令$\eta=\log(p/(1-p))$，则$p_\eta(x)=\exp\{x\eta-\log(1+e^\eta)\}, \qquad x\in\{0,1\}$所以$A(\eta)=\log(1+e^\eta)$，$A'(\eta)=p$、$A''(\eta)=p(1-p)$。

#### 1.1.5 随机序列与过程的表示

主要内容：反复测量得到的$X_1,X_2,\ldots$必须一起定义，才能说明两次读数是否共享噪声。索引$n$记录测量轮次；把轮次换成连续时间后，同样的思路给出随机过程。

论证与表述逻辑：

1. 例如取相互独立的噪声$(\varepsilon_i)$，并取与全部噪声独立的非退化可积背景变量$\Theta$。
2. 随机过程允许索引取自更一般的集合。时间索引可以离散或连续，空间索引也可以标记图上的顶点或欧氏空间的位置；指定索引集合后，各坐标仍须作为同一概率空间上的随机变量共同定义。
3. 定义（随机过程）：给定概率空间$(\Omega,\mathcal F,\mathbb P)$、索引集$T$和状态可测空间$(\mathcal X,\mathcal A)$，随机过程（stochastic process）是一族随机变量$(X_t)_{t\in T}$，其中每个$X_t:\Omega\to\mathcal X$均可测。

##### 1.1.5.1 基于有限维分布的过程表示

主要内容：设每次只能观察有限个时刻，我们可以分别指定这些读数的联合分布。现在要检查：删去部分时刻或重排时刻后，这些指定是否相容，从而能否来自同一个过程。

论证与表述逻辑：

1. 命题（Kolmogorov扩张的标准Borel版本）：设状态空间$E$是标准Borel空间，$T$为任意索引集。若给定每个有限索引集合$J\subset T$上的概率测度$P_J$，且对有限集合$J\subset K$，从$E^K$投影到$E^J$把$P_K$推送为$P_J$，则存在唯一的概率测度定义在$E^T$的乘积$\sigma$代数上，使各坐标过程具有这些有限维分布。用有序时刻元组表示时，还必须满足重排坐标的相容性。
2. 相容性意味着同一个两时刻问题，不论直接指定还是从三时刻问题删掉一个坐标，都应得到同一答案。高斯过程的半正定核会提供一组相容的高斯向量，因而可用此定理建立过程。

##### 1.1.5.2 基于样本路径的过程表示

主要内容：离散时间通常取$T=\mathbb N_0$，连续时间取$T=[0,\infty)$。固定时刻$t$，$\omega\mapsto X_t(\omega)$是随机变量；固定基础结果$\omega$，$t\mapsto X_t(\omega)$是样本路径。

论证与表述逻辑：

1. 描述连续路径的粗糙程度时，称$x$在紧时间区间上具有正指数$\alpha$的Hölder连续性，是指存在有限$C_x$，使$|x(t)-x(s)|\leq C_x|t-s|^\alpha \quad\text{对区间内所有 }s,t\text{成立}$随机路径允许常数$C_x$依赖具体实现。
2. 得到连续版本的一项常用充分条件是Kolmogorov连续性准则：若在紧时间区间上存在$p>0,\beta>0,C<\infty$，使$\mathbb E|X_t-X_s|^p\leq C|t-s|^{1+\beta},$则存在连续版本，并可取得任意小于$\beta/p$的正Hölder指数；该条件本身不保证达到端点$\beta/p$。

### 1.2 随机对象的依赖关系

主要内容：由联合与条件规律讨论独立性、交换性、历史依赖和时间平移，区分边缘分布相同与共同变化方式相同。

论证与表述逻辑：

1. 随机变量的联合关系：随机向量$(X,Y)$的联合分布是映射$\omega\mapsto(X(\omega),Y(\omega))$在乘积空间上诱导的概率测度。
2. 随机变量的条件关系：看到第一台设备的读数后，第二台设备原来的边缘描述可能不再充分。若查询的是平均读数，可以把已见信息固定下来计算条件期望；若查询的是越界概率、分位数或下一次随机生成的规律，则需要条件分布。
3. 随机变量的独立关系：独立、不相关与非线性依赖若随机变量$X,Y$满足$\mathbb{P}(X\in A,Y\in B) =\mathbb{P}(X\in A)\mathbb{P}(Y\in B)$对所有Borel集合$A,B$成立，就称二者独立（independent）。
4. 随机序列的交换关系：若一批观测没有需要保留的顺序，可以检查重排记录以后联合规律是否改变。
5. 历史条件下的状态依赖：预测下一时刻时，完整历史通常含有很多记录。若当前状态已经概括其中与下一步有关的信息，给定当前状态后继续加入旧记录就不应改变下一步条件分布。

#### 1.2.1 随机变量的联合关系

主要内容：随机向量$(X,Y)$的联合分布是映射$\omega\mapsto(X(\omega),Y(\omega))$在乘积空间上诱导的概率测度。

论证与表述逻辑：

1. 对二阶可积的$X,Y$，协方差为$\operatorname{Cov}(X,Y) =\mathbb{E}\bigl[(X-\mathbb{E}X)(Y-\mathbb{E}Y)\bigr]$Cauchy--Schwarz不等式保证它有限。
2. 定义（多元高斯随机向量）：若对每个$\boldsymbol{u}\in\mathbb{R}^d$，标量$\boldsymbol{u}^{\top}\boldsymbol{X}$都服从一维高斯分布，就称$\boldsymbol{X}$为多元高斯随机向量（multivariate Gaussian random vector）。
3. 把读数转换成二元误差标记$U,V\in\{0,1\}$。

#### 1.2.2 随机变量的条件关系

主要内容：看到第一台设备的读数后，第二台设备原来的边缘描述可能不再充分。若查询的是平均读数，可以把已见信息固定下来计算条件期望；若查询的是越界概率、分位数或下一次随机生成的规律，则需要条件分布。

论证与表述逻辑：

1. 条件信息下的均值关系：子$\sigma$代数$\mathcal{G}\subseteq\mathcal{F}$表示当前可用信息。预测值必须只使用这些信息，又应在每个可识别的分组内保持平均值。
2. 条件信息下的分布关系：当条件变量连续时，事件$\{X=x\}$常有零概率，直接相除不再可行。需要把“每个条件值对应一个分布”组织成能继续积分的对象。

##### 1.2.2.1 条件信息下的均值关系

主要内容：子$\sigma$代数$\mathcal{G}\subseteq\mathcal{F}$表示当前可用信息。预测值必须只使用这些信息，又应在每个可识别的分组内保持平均值。

论证与表述逻辑：

1. 命题（条件均值的平方损失最优性）：在所有$\mathcal{G}$-可测且二阶可积的随机变量$U$中，$m=\mathbb{E}[X\mid\mathcal{G}]$唯一地在几乎处处意义下最小化$\mathbb{E}[(X-U)^2]$。
2. 推导：$L^2(\mathcal{G})$是$L^2(\mathcal{F})$的闭线性子空间，上文直接证明的条件平方界已经说明$m\in L^2(\mathcal{G})$。对每个$U\in L^2(\mathcal{G})$，Cauchy--Schwarz不等式保证$(X-m)U$可积，因而可以提出已知因子并使用塔式性质，得到$\mathbb{E}[(X-m)U] =\mathbb{E}\left[U\mathbb{E}[X-m\mid\mathcal{G}]\right]=0$所以$X-m$与整个$L^2(\mathcal{G})$正交，$m$就是$X$到该闭子空间的正交投影。直接展开$\mathbb{E}[(X-U)^2] = \mathbb{E}[(X-m)^2] + \mathbb{E}[(m-U)^2],$交叉项因正交性消失。
3. 条件期望的存在只需要$X\in L^1$，这时它由Radon--Nikodym导数给出。“正交投影”和平方损失最优性则需要$X\in L^2$。

##### 1.2.2.2 条件信息下的分布关系

主要内容：当条件变量连续时，事件$\{X=x\}$常有零概率，直接相除不再可行。需要把“每个条件值对应一个分布”组织成能继续积分的对象。

论证与表述逻辑：

1. 可测并不等于连续。例如取$X\sim\mathcal N(0,1)$、$Y=\mathbb I\{X\geq0\}$，则$K(x,\{1\})=\mathbb I\{x\geq0\}$是合法概率核在事件$\{1\}$上的取值，却在$x=0$处跳变。
2. 总体分位数来自混合不同输入后的边缘分布；若不同$x$对应不同位置或尾部，还需要按输入报告条件分位数。
3. 定义（条件分位数）：给定$Y$关于$X=x$的正则条件分布，记$F_x(y)=\mathbb P(Y\leq y\mid X=x)$。对$0<q<1$，下条件$q$分位数为$F_x^{-1}(q)=\inf\{y:F_x(y)\geq q\}$；完整条件分位数集合为$\{a:F_x(a^-)\leq q\leq F_x(a)\}$。

#### 1.2.3 随机变量的独立关系

主要内容：独立、不相关与非线性依赖若随机变量$X,Y$满足$\mathbb{P}(X\in A,Y\in B) =\mathbb{P}(X\in A)\mathbb{P}(Y\in B)$对所有Borel集合$A,B$成立，就称二者独立（independent）。

论证与表述逻辑：

1. 引理（严格正离散分布的交性质）：设$I$为有限索引集，每个$i\in I$对应取值于有限非空状态空间$\mathcal{X}_i$的随机变量$X_i$。令$p$为$\boldsymbol{X}=(X_i)_{i\in I}$在乘积状态空间$\mathcal{X}=\prod_{i\in I}\mathcal{X}_i$上的联合质量函数，且$p(\boldsymbol{x})>0$对所有$\boldsymbol{x}\in\mathcal{X}$成立。对两两不交的索引集$A,B,C,D\subseteq I$，若$\boldsymbol{X}_A\perp\boldsymbol{X}_B\mid(\boldsymbol{X}_C,\boldsymbol{X}_D), \qquad \boldsymbol{X}_A\perp\boldsymbol{X}_D\mid(\boldsymbol{X}_C,\boldsymbol{X}_B),$则$\boldsymbol{X}_A\perp(\boldsymbol{X}_B,\boldsymbol{X}_D)\mid\boldsymbol{X}_C$。
2. 推导：严格正性保证以下每个条件概率都有定义。对任意取值$\boldsymbol{a},\boldsymbol{b},\boldsymbol{c},\boldsymbol{d}$，两个前提分别给出$p(\boldsymbol{a}\mid\boldsymbol{b},\boldsymbol{c},\boldsymbol{d}) =p(\boldsymbol{a}\mid\boldsymbol{c},\boldsymbol{d}), \qquad p(\boldsymbol{a}\mid\boldsymbol{b},\boldsymbol{c},\boldsymbol{d}) =p(\boldsymbol{a}\mid\boldsymbol{b},\boldsymbol{c})$因此$p(\boldsymbol{a}\mid\boldsymbol{c},\boldsymbol{d})=p(\boldsymbol{a}\mid\boldsymbol{b},\boldsymbol{c})$对每个$\boldsymbol{b},\boldsymbol{d}$成立。固定任意基准值$\boldsymbol{b}^{\circ}$，右侧等于$q(\boldsymbol{a},\boldsymbol{c})=p(\boldsymbol{a}\mid\boldsymbol{b}^{\circ},\boldsymbol{c})$，不再依赖$\boldsymbol{b}$或$\boldsymbol{d}$。
3. 多元高斯分布是一个特殊情形：联合高斯随机向量的两个子向量若协方差为零，则它们独立；条件高斯中的条件协方差为零也对应条件独立。

#### 1.2.4 随机序列的交换关系

主要内容：若一批观测没有需要保留的顺序，可以检查重排记录以后联合规律是否改变。

论证与表述逻辑：

1. 定义（可交换随机变量）：随机变量$Z_1,\ldots,Z_m$若对每个排列$\pi$都有$(Z_1,\ldots,Z_m) \overset{\mathrm{d}}{=}(Z_{\pi(1)},\ldots,Z_{\pi(m)}),$就称它们可交换（exchangeable）。
2. 独立同分布蕴含可交换，但反向不成立。例如先抽取取值于$[0,1]$的非退化随机概率$\Theta$，再条件于$\Theta$独立生成Bernoulli观测；边缘上这些观测可交换，却因共享$\Theta$而相关。
3. 可交换性不提供样本平均的独立乘积结构，因而不能直接代入Hoeffding证明。因为所有标签机会相同，而每个秩又恰由一个标签占据，概率总和必须为$1$。

#### 1.2.5 历史条件下的状态依赖

主要内容：预测下一时刻时，完整历史通常含有很多记录。若当前状态已经概括其中与下一步有关的信息，给定当前状态后继续加入旧记录就不应改变下一步条件分布。

论证与表述逻辑：

1. 先约定时刻$t$已知哪些记录。滤过使“完整历史”成为可用于条件期望的数学对象；适应性检查当前状态是否已经可知，可预测性则检查下一步所用系数是否在新噪声揭晓前确定。
2. 定义（细致平衡）：概率核$P$与概率测度$\pi$满足细致平衡（detailed balance），若以下两个联合测度在$\mathcal Z\times\mathcal Z$上相同：$\pi(\mathrm{d}z)P(z,\mathrm{d}z') =\pi(\mathrm{d}z')P(z',\mathrm{d}z)$。
3. 反向不成立：围绕三个状态单向循环的链可以保持均匀分布，却没有逐边对称的反向流。细致平衡是构造采样链的便利证书，不是遍历平均成立的必要定义。

#### 1.2.6 历史条件下的均值关系

主要内容：完整条件分布不变是一项强要求。有时只知道新增量在已有历史下没有平均漂移，方差和其他形状仍可随历史改变。

论证与表述逻辑：

1. 定义（鞅与鞅差）：可积过程$(M_t)$若适应于$(\mathcal{F}_t)$，并对每个整数$t\geq1$满足$\mathbb{E}[M_t\mid\mathcal{F}_{t-1}]=M_{t-1},$就称为鞅（martingale）。增量$X_t=M_t-M_{t-1}$满足$\mathbb{E}[X_t\mid\mathcal{F}_{t-1}]=0,$称为鞅差（martingale difference）。若条件等式改为$\mathbb E[M_t\mid\mathcal F_{t-1}]\leq M_{t-1}$，称$(M_t)$为超鞅；改为$\geq$时称为次鞅。
2. 连续时间的定义把相邻时刻条件换成：对任意$0\leq s\leq t$，$\mathbb E[M_t\mid\mathcal F_s]=M_s$几乎必然；每个时刻仍须可积且适应。
3. 条件均值保持本身没有规定长期极限。

#### 1.2.7 时间平移下的分布关系

主要内容：把观测窗口从今天移到明天后，若整组读数的联合规律保持不变，就可以用时间平移来表达这种稳定的统计结构。

论证与表述逻辑：

1. 对时间齐次Markov链，若$Z_0\sim\pi$且$\pi P=\pi$，则$\mathbb{P}(Z_0\in\mathrm{d}z_0,\ldots,Z_m\in\mathrm{d}z_m) = \pi(\mathrm{d}z_0) \prod_{j=1}^{m}P(z_{j-1},\mathrm{d}z_j)$把起点向后平移一格时，先对$z_0$积分，$\pi P=\pi$把$Z_1$的边缘重新化为$\pi$，其余转移核不变；反复应用便证明所有有限维分布都不随平移改变。
2. 定义（二阶平稳）：实值过程二阶矩有限，若均值与时间无关，且$\operatorname{Cov}(X_s,X_t)$只依赖时间差$t-s$，称为二阶平稳（second-order stationarity），也称弱平稳。
3. 严格平稳加有限二阶矩推出二阶平稳；反向一般不成立。例如相互独立的序列在偶数时刻取标准高斯分布，在奇数时刻等概率取$\pm1$。

### 1.3 随机对象的变换与生成

主要内容：比较确定性变换、条件抽样与概率重加权，进一步构造状态转移、到达计数及高斯规律下的随机过程。

论证与表述逻辑：

1. 随机变量的确定性变换：设随机对象$X$已经给出，并选定可测函数$g$。每次取得$X=x$后，新对象都按同一规则取$g(x)$；因而变换没有增加新的随机抽样。
2. 条件规律下的随机生成：混合模型先抽取离散指标$Z$，再从分量分布生成$X$：$p(x)=\sum_{k=1}^{K}\mathbb{P}(Z=k)p(x\mid Z=k)$边缘化$Z$得到混合密度，条件化$X$则得到分量责任概率。
3. 概率加权下的分布变换：保持同一个取值函数$g$，把事件权重从$\mu$改成$\nu$，会改变它的积分。现在把这个比值直接乘入旧积分，便能计算新权重下的平均。
4. 基于状态转移的随机序列生成：给定当前状态后抽取一步增量，再重复这一操作，可以生成整条随机序列。随机游走用增量相加确定下一位置；一般Markov链则直接用转移核给出下一状态的条件分布。
5. 基于到达计数的随机过程生成：事件到达使状态按次跳变。固定窗口内的计数可以服从Poisson分布，但只有规定不同窗口间的联合关系，才能得到Poisson过程。

#### 1.3.1 随机变量的确定性变换

主要内容：设随机对象$X$已经给出，并选定可测函数$g$。每次取得$X=x$后，新对象都按同一规则取$g(x)$；因而变换没有增加新的随机抽样。

论证与表述逻辑：

1. 随机变量的分布变换：若$X$取值于$(E,\mathcal E)$，$g:E\to F$可测，则$Y=g(X)$的分布是$P_Y=g_\#P_X$，即$P_Y(B)=P_X(g^{-1}(B)),\qquad \mathbb E h(Y)=\int_E h(g(x))\,P_X(\mathrm dx)$对非负可测$h$或可积$h$成立。
2. 数值随机变量的组合运算：相同边缘并没有给出相同的累计波动。若只知两个变量可积，乘积未必可积；二阶可积则由Cauchy--Schwarz保证乘积可积。

##### 1.3.1.1 随机变量的分布变换

主要内容：若$X$取值于$(E,\mathcal E)$，$g:E\to F$可测，则$Y=g(X)$的分布是$P_Y=g_\#P_X$，即$P_Y(B)=P_X(g^{-1}(B)),\qquad \mathbb E h(Y)=\int_E h(g(x))\,P_X(\mathrm dx)$对非负可测$h$或可积$h$成立。

论证与表述逻辑：

1. 设$\mathcal X,\mathcal Y$为$\mathbb R^d$中的开域，$\boldsymbol X$取值于$\mathcal X$且具有相对于$d$维Lebesgue测度的密度。
2. 若映射可分为有限或可数个一一对应的$C^1$分支，各分支Jacobian非零，则在正则值处把各逆像分支的换元密度相加。

##### 1.3.1.2 数值随机变量的组合运算

主要内容：相同边缘并没有给出相同的累计波动。若只知两个变量可积，乘积未必可积；二阶可积则由Cauchy--Schwarz保证乘积可积。

论证与表述逻辑：

1. 独立性还把变换函数化为乘积：$\varphi_{X+Y}(t)=\mathbb E(e^{\mathrm itX}e^{\mathrm itY}) =\varphi_X(t)\varphi_Y(t)$在矩母函数共同有限的邻域，同样有$M_{X+Y}=M_XM_Y$、$K_{X+Y}=K_X+K_Y$。
2. 对次序统计量$Y_{(1)}\leq\cdots\leq Y_{(n)}$，经验分位数由相应秩位置给出。若$Y_1,\ldots,Y_n$是来自连续分布$F$的独立同分布样本，则$F(Y_{(k)})$服从$\operatorname{Beta}(k,n+1-k)$，因此可以用秩而不是高斯近似构造分位数区间。

#### 1.3.2 条件规律下的随机生成

主要内容：混合模型先抽取离散指标$Z$，再从分量分布生成$X$：$p(x)=\sum_{k=1}^{K}\mathbb{P}(Z=k)p(x\mid Z=k)$边缘化$Z$得到混合密度，条件化$X$则得到分量责任概率。

论证与表述逻辑：

1. 层次模型把参数本身也视为随机变量，例如$\Theta\sim\pi,\qquad X_i\mid\Theta\mathrel{\overset{\mathrm{ind}}{\sim}}p_\Theta$给定$\Theta$时，观测条件独立；边缘化共同参数后，观测通常相关。
2. 定义（Dirichlet过程）：设$(\mathcal X,\mathcal A)$为标准Borel空间，$G_0$为其上的概率测度，$\alpha>0$。随机概率测度$G$称为参数$(\alpha,G_0)$的Dirichlet过程，记作$G\sim\operatorname{DP}(\alpha,G_0)$，若对任意有限可测分割$(A_1,\ldots,A_K)$，$(G(A_1),\ldots,G(A_K)) \sim\operatorname{Dirichlet}(\alpha G_0(A_1),\ldots,\alpha G_0(A_K))$其中$\alpha>0$是总质量参数，$G_0$是基概率测度；若$G_0(A_k)=0$，则相应坐标满足$G(A_k)=0$几乎必然，应删除该零参数坐标后理解Dirichlet向量。
3. 合并两个分块时，概率质量相加，Dirichlet参数也相加；这说明不同分割规律彼此相容。相容性还不足以保证每条实现都可数可加。

#### 1.3.3 概率加权下的分布变换

主要内容：保持同一个取值函数$g$，把事件权重从$\mu$改成$\nu$，会改变它的积分。现在把这个比值直接乘入旧积分，便能计算新权重下的平均。

论证与表述逻辑：

1. 命题（换测度积分公式）：若$\nu\ll\mu$，$r=\mathrm{d}\nu/\mathrm{d}\mu$，则对每个非负可测函数$g$，$\int g\,\mathrm{d}\nu =\int gr\,\mathrm{d}\mu$只要$g$在$\nu$下可积，同一等式也对实值$g$成立。
2. 推导：对指示函数$g=\mathbb{I}_A$，结论就是Radon--Nikodym表示。由线性性，它对非负简单函数成立。任取非负可测$g$，选择简单函数$g_n\uparrow g$，分别在$\nu$和$\mu$下使用单调收敛定理即可。
3. 换测度也可作用于整段观测，而不只作用于一个随机变量。考虑长度$T$的轨迹$\tau=(s_0,a_0,s_1,a_1,\ldots,s_T)$，其中$s_t$记录当前状态，$a_t$记录当步行动。

#### 1.3.4 基于状态转移的随机序列生成

主要内容：给定当前状态后抽取一步增量，再重复这一操作，可以生成整条随机序列。随机游走用增量相加确定下一位置；一般Markov链则直接用转移核给出下一状态的条件分布。

论证与表述逻辑：

1. 基于增量累计的随机游走生成：给定独立同分布增量$\xi_i$，定义$S_0=0$、$S_n=\sum_{i=1}^n\xi_i$，称为随机游走（random walk）。
2. 基于转移核的Markov链生成：Markov核给出一步条件规律；多步计算、边缘极限和长期平均还分别需要核复合及返回条件。

##### 1.3.4.1 基于增量累计的随机游走生成

主要内容：给定独立同分布增量$\xi_i$，定义$S_0=0$、$S_n=\sum_{i=1}^n\xi_i$，称为随机游走（random walk）。

论证与表述逻辑：

1. 若$\mathbb E\xi_i=\mu$、$\operatorname{Var}(\xi_i)=\sigma^2<\infty$，则$\mathbb ES_n=n\mu,\qquad \operatorname{Var}(S_n)=n\sigma^2,\qquad \operatorname{Cov}(S_m,S_n)=\min(m,n)\sigma^2$当$\sigma^2>0$且$m,n\geq1$时，位置之间的协方差为正，所以不能把不同位置当作独立观测。
2. $S_n-n\mu$相对于增量的自然滤过是鞅，$S_n$本身还具有Markov性。
3. 取$p=0.6$，十步均值为$2$、方差为$9.6$；某一条十步路径却不必靠近均值。

##### 1.3.4.2 基于转移核的Markov链生成

主要内容：Markov核给出一步条件规律；多步计算、边缘极限和长期平均还分别需要核复合及返回条件。

论证与表述逻辑：

1. 示例（相关的两状态观测）：令$Z_t\in\{0,2\}$，并把观测直接取为$Y_t=Z_t$。转移矩阵按状态$0,2$排序为$\boldsymbol{P} = \begin{pmatrix} 0.9 & 0.1\\ 0.2 & 0.8 \end{pmatrix}$平稳分布为$\boldsymbol{\pi}=(2/3,1/3)^\top$，因为$\boldsymbol{P}^{\top}\boldsymbol{\pi}=\boldsymbol{\pi}$。
2. 定义（有限链的不可约性与周期）：有限状态Markov链满足不可约性（irreducibility），若对任意状态$i,j$存在整数$m\geq0$，使$P^m(i,\{j\})>0$。若返回步数集合非空，状态$i$的周期（period）定义为$d_i=\gcd\{m\geq1:P^m(i,\{i\})>0\}$不可约链的全部状态具有共同周期；该周期为$1$时，称链为非周期的（aperiodic）。
3. 在前面的两状态例子中，令$q_t=\mathbb P(Y_t=2)$。一步转移给出$q_{t+1}=0.1(1-q_t)+0.8q_t=0.1+0.7q_t, \qquad q_t=\frac13+0.7^t\left(q_0-\frac13\right)$从$q_0=0$出发，前两步为$q_1=0.1,q_2=0.17$，而不是立即得到$1/3$。

#### 1.3.5 基于到达计数的随机过程生成

主要内容：事件到达使状态按次跳变。固定窗口内的计数可以服从Poisson分布，但只有规定不同窗口间的联合关系，才能得到Poisson过程。

论证与表述逻辑：

1. 事件计数与短时跳跃：给定速率$\lambda>0$和滤过$(\mathcal F_t)_{t\geq0}$，计数过程$(N_t)_{t\geq0}$称为相对于该滤过的齐次泊松过程（Poisson process），若它适应于滤过，$N_0=0$几乎必然，路径几乎必然右连续、非减、取非负整数且每次跳跃为一，并满足$N_t-N_s\ \perp\ \mathcal F_s,\qquad N_t-N_s\sim\operatorname{Poisson}(\lambda(t-s)), \quad 0\leq s<t$。 若每次到达还带来随机量$J_k$，其中$J_k$独立同分布且独立于计数过程，则$C_t=\sum_{k=1}^{N_t}J_k$称为复合泊松过程（compound Poisson process）。
2. 平均到达与补偿增量：计数每段时间平均增加$\lambda h$。从原计数中减去这一可预测平均趋势，得到补偿泊松过程（compensated Poisson process）$\widetilde N_t=N_t-\lambda t$。 复合情形若$\mathbb E|J_1|<\infty$，则$C_t-\lambda t\,\mathbb EJ_1$相对于只揭示已到达标记的自然历史是鞅。

#### 1.3.6 基于高斯规律的随机过程生成

主要内容：规定多个时刻的联合高斯分布，可以用均值和协方差组织全部有限维规律。独立增量给出Brownian模型；一般协方差核则允许不同的时间依赖。

论证与表述逻辑：

1. 独立高斯增量下的布朗路径构造：与一次一次的跳跃相对，连续波动的每段增量可越来越小，但累计波动仍然非零。布朗运动给出这种尺度的基本模型；连续路径不等于可微路径。
2. 均值与协方差约束下的高斯过程构造：实值随机过程$(F(x))_{x\in\mathcal X}$称为高斯过程（Gaussian process），若任意正整数$m$及任意$x_1,\ldots,x_m\in\mathcal X$上的向量$(F(x_1),\ldots,F(x_m))^\top$均服从多元高斯分布，允许协方差奇异。索引$x$不必代表时间。

##### 1.3.6.1 独立高斯增量下的布朗路径构造

主要内容：与一次一次的跳跃相对，连续波动的每段增量可越来越小，但累计波动仍然非零。布朗运动给出这种尺度的基本模型；连续路径不等于可微路径。

论证与表述逻辑：

1. 连续路径与增量尺度：设$\xi_{1},\xi_{2},\ldots$独立同分布， $\mathbb{E}\xi_{i}=0$、$\operatorname{Var} (\xi_{i})=1$。 相对于同一滤过，$m$维标准Brownian运动$\boldsymbol W_t=(W_t^{(1)},\ldots,W_t^{(m)})^\top$由相互独立的实值标准Brownian运动组成，并要求$\boldsymbol W_t-\boldsymbol W_s\ \perp\ \mathcal F_s,\qquad \boldsymbol W_t-\boldsymbol W_s\sim\mathcal N(\boldsymbol0,(t-s)\boldsymbol I_m)$若以固定矩阵$\boldsymbol A$混合这些分量，增量协方差变成$(t-s)\boldsymbol A\boldsymbol A^\top$，不再是标准Brownian的单位协方差；低秩$\boldsymbol A$允许退化扩散。
2. 不可微性与二次变差：长度为$h$的增量典型尺度为$\sqrt h$，所以差商$\frac{W_{t+h}-W_{t}}{h}$的标准差为$1/\sqrt{h}$， 随$h\to0$反而发散。 对同一确定分割，交叉二次变差使用增量乘积而非平方：$[X,Y]_t=\lim_{|\pi|\to0}\sum_{[u,v]\in\pi} (X_v-X_u)(Y_v-Y_u),$这里按存在时的依概率极限理解。

##### 1.3.6.2 均值与协方差约束下的高斯过程构造

主要内容：实值随机过程$(F(x))_{x\in\mathcal X}$称为高斯过程（Gaussian process），若任意正整数$m$及任意$x_1,\ldots,x_m\in\mathcal X$上的向量$(F(x_1),\ldots,F(x_m))^\top$均服从多元高斯分布，允许协方差奇异。索引$x$不必代表时间。

论证与表述逻辑：

1. 定义（高斯过程）：实值随机过程$(F(x))_{x\in\mathcal X}$称为高斯过程（Gaussian process），若任意正整数$m$及任意$x_1,\ldots,x_m\in\mathcal X$上的向量$(F(x_1),\ldots,F(x_m))^\top$均服从多元高斯分布，允许协方差奇异。索引$x$不必代表时间。
2. 协方差函数必须对称，且对任意有限输入和实系数$c_i$满足$\sum_{i,j}c_ic_jk(x_i,x_j)\geq0$这正是有限协方差矩阵半正定的条件。
3. 例如令$A,B$是独立标准高斯变量，定义$F(x)=A+Bx$。任意有限函数值都是$(A,B)$的线性变换，所以构成高斯过程，且$m(x)=0$、$k(x,x')=1+xx'$。

### 1.4 随机累计量的偏差控制

主要内容：分别控制固定累计量、候选族和历史依赖累计量的偏差，说明同时性、条件化与停止规则改变了哪些保证。

论证与表述逻辑：

1. 单个累计量的偏差控制：如果一个非负累计量经常超过阈值，它的平均值就不能太小。设非负随机变量为$X$，阈值为$a>0$，则$\mathbb{P}(X\geq a) \leq \frac{\mathbb{E}X}{a}$证明只需写$\mathbb{E}X\geq \mathbb{E}[X\mathbb{I}\{X\geq a\}] \geq a\mathbb{P}(X\geq a)$。
2. 候选族累计量的统一偏差控制：设同一批记录用于计算多个候选的平均，再从中挑选一个结果。如果选择规则偏向偶然偏低的平均，预先固定一个候选时的误差保证就未必适用。
3. 历史依赖下累计量的偏差控制：逐步采集记录时，下一次观测的位置或噪声尺度可以依赖已见历史。即使每个新增量在历史条件下均值为零，它们也未必独立，不能直接乘上独立样本的指数矩。

#### 1.4.1 单个累计量的偏差控制

主要内容：如果一个非负累计量经常超过阈值，它的平均值就不能太小。设非负随机变量为$X$，阈值为$a>0$，则$\mathbb{P}(X\geq a) \leq \frac{\mathbb{E}X}{a}$证明只需写$\mathbb{E}X\geq \mathbb{E}[X\mathbb{I}\{X\geq a\}] \geq a\mathbb{P}(X\geq a)$。

论证与表述逻辑：

1. 命题（Hoeffding不等式）：设$X_1,\ldots,X_n$相互独立，且$X_i\in[a_i,b_i]$几乎处处成立。若$\sum_i(b_i-a_i)^2>0$，则对$t>0$，$\mathbb{P}\left( \sum_{i=1}^{n}(X_i-\mathbb{E}X_i)\geq t \right) \leq \exp\left\{ -\frac{2t^2}{\sum_{i=1}^{n}(b_i-a_i)^2} \right\}$当全部区间宽度为零时，中心化和恒为零，上述右尾概率为零。
2. 推导：只需证明总区间宽度平方和为正的情形。对$\lambda>0$，独立性使指数矩分解：$\begin{aligned} \mathbb{P}(S\geq t) &\leq e^{-\lambda t}\mathbb{E}[e^{\lambda S}]\\ &= e^{-\lambda t} \prod_{i=1}^{n} \mathbb{E}\left[ e^{\lambda(X_i-\mathbb{E}X_i)} \right]\\ &\leq \exp\left\{ -\lambda t+ \frac{\lambda^2}{8} \sum_{i=1}^{n}(b_i-a_i)^2 \right\} \end{aligned}$右侧关于$\lambda$的最小点为$\lambda^\star =\frac{4t}{\sum_i(b_i-a_i)^2}$代回即得结论。对$-S$使用同一结果，再用联合界可得双侧版本。
3. 经验有效样本量常写成$\widehat{n}_{\mathrm{eff}} =\frac{(\sum_i\widetilde{w}_i)^2}{\sum_i\widetilde{w}_i^2}$它是权重退化的诊断量，不是对所有估计目标都成立的精确独立样本数。

#### 1.4.2 候选族累计量的统一偏差控制

主要内容：设同一批记录用于计算多个候选的平均，再从中挑选一个结果。如果选择规则偏向偶然偏低的平均，预先固定一个候选时的误差保证就未必适用。

论证与表述逻辑：

1. 有限候选的联合控制：设有限候选类$\mathcal{H}=\{h_1,\ldots,h_M\}$，损失$\ell(h,Z)\in[0,1]$。 命题（有限函数类的一致误差界）：在上述条件下，对任意$\delta\in(0,1)$，以至少$1-\delta$的概率同时对所有$h\in\mathcal{H}$有$|\widehat{R}_n(h)-R(h)| \leq \sqrt{\frac{\log(2M/\delta)}{2n}}$。
2. 无限候选的统一控制：无限函数类不能直接按元素做联合界。样本上的有限取值模式与覆盖网中的有限代表，提供两种有限化方法。 引理（覆盖数的有限网控制）：设$(\mathcal{F},d)$具有有限$\varepsilon$-网$\mathcal{N}_\varepsilon$，其大小为$N(\mathcal{F},d,\varepsilon)$。若随机过程$\{Z_f:f\in\mathcal{F}\}$满足$|Z_f-Z_g|\leq Ld(f,g)$几乎处处对所有$f,g$成立，并且相关上确界可测，则对任意$t>0$，$\mathbb{P}\left\{ \sup_{f\in\mathcal{F}}|Z_f|>t+L\varepsilon \right\} \leq N(\mathcal{F},d,\varepsilon) \sup_{f\in\mathcal{F}}\mathbb{P}(|Z_f|>t)$。
3. 候选函数族的采样积分误差：对每个候选函数$f\in\mathcal F$，都可用同一组独立样本计算$n^{-1}\sum_i f(X_i)$。

#### 1.4.3 历史依赖下累计量的偏差控制

主要内容：逐步采集记录时，下一次观测的位置或噪声尺度可以依赖已见历史。即使每个新增量在历史条件下均值为零，它们也未必独立，不能直接乘上独立样本的指数矩。

论证与表述逻辑：

1. 固定时刻的误差界：若只知道每个鞅差的范围，可以把独立变量的指数矩方法逐步条件化。 命题（Azuma--Hoeffding不等式）：设$(X_t,\mathcal{F}_t)_{t=1}^{n}$为鞅差，并且几乎必然有$a_t\leq X_t\leq b_t$，其中$a_t,b_t$为确定常数。若$\sum_t(b_t-a_t)^2>0$，则对任意$x>0$，$\mathbb{P}(S_n\geq x)\leq\exp\left\{ -\frac{2x^2}{\sum_{t=1}^{n}(b_t-a_t)^2} \right\}$若全部宽度为零，鞅差条件均值零使每个$X_t=0$几乎必然，正尾概率为零。
2. 任意时刻的同时误差界：设$(M_t,\mathcal{F}_t)$为可积鞅，$\tau$为满足$\tau\leq n$几乎必然成立的停时。 证明中的各项假设承担不同作用。条件次高斯性构造每一步指数超鞅；特征可预测性允许在条件期望中把$\boldsymbol{x}_t$视为已知；$\boldsymbol{V}_0\succ\boldsymbol{0}$使高斯混合与逆矩阵从$t=0$起有定义。

### 1.5 随机对象的统计推断

主要内容：从有限记录推断参数、函数和未来观测，区分目标识别、估计误差、模型比较与观测设计。

论证与表述逻辑：

1. 观测条件下的目标识别：设两套生成规则会产生完全相同的可见记录，却给出不同的目标均值。增加这类记录只能把共同的观测规律估计得更准，仍无法确定目标属于哪套规则。
2. 参数与函数的估计：目标能够由观测规律确定后，有限记录仍只提供它的近似。估计一个均值时，输出是一个数；估计分布或条件函数时，输出是一整条规律。
3. 未来观测的预测：即使总体均值已知，下一次传感器读数仍会受新噪声影响。预测要把这种结果波动与估计未知规律的误差同时纳入。
4. 推断误差的评估：一个估计数值需要评价平均损失或误差分布，一段参数范围需要评价重复抽样下的覆盖率，拒绝一个命题则需要控制误拒概率。
5. 候选模型的比较：上一组工具评价预测分布；多个模型竞争时，还需先决定比较的是训练拟合、未来预测还是模型证据。边缘似然对参数积分，Laplace近似用局部曲率近似这项积分。

#### 1.5.1 观测条件下的目标识别

主要内容：设两套生成规则会产生完全相同的可见记录，却给出不同的目标均值。增加这类记录只能把共同的观测规律估计得更准，仍无法确定目标属于哪套规则。

论证与表述逻辑：

1. 观测规律下的目标可识别性：统计模型（statistical model）是一族候选分布$\mathcal{P}=\{P_\vartheta:\vartheta\in\Theta\}$这些分布定义在同一个可测观测空间上，参数$\vartheta$是描述候选分布的未知索引。观测$\boldsymbol{Y}=(Y_1,\ldots,Y_n)$由其中某个分布产生，但真实索引不可见。参数未必是一个物理常数；它也可以是一组回归系数、一个混合比例，或者无限维的分布函数。
2. 抽样与观测机制下的识别条件：统计结论必须先回答“想对谁成立”。目标总体（target population）是推断希望覆盖的对象、时间和条件的集合；抽样制度（sampling regime）描述观测如何从这些对象产生。

##### 1.5.1.1 观测规律下的目标可识别性

主要内容：统计模型（statistical model）是一族候选分布$\mathcal{P}=\{P_\vartheta:\vartheta\in\Theta\}$这些分布定义在同一个可测观测空间上，参数$\vartheta$是描述候选分布的未知索引。观测$\boldsymbol{Y}=(Y_1,\ldots,Y_n)$由其中某个分布产生，但真实索引不可见。参数未必是一个物理常数；它也可以是一组回归系数、一个混合比例，或者无限维的分布函数。

论证与表述逻辑：

1. 定义（统计模型与统计量）：统计模型（statistical model）是一族候选分布$\mathcal{P}=\{P_\vartheta:\vartheta\in\Theta\}$这些分布定义在同一个可测观测空间上，参数$\vartheta$是描述候选分布的未知索引。观测$\boldsymbol{Y}=(Y_1,\ldots,Y_n)$由其中某个分布产生，但真实索引不可见。参数未必是一个物理常数；它也可以是一组回归系数、一个混合比例，或者无限维的分布函数。统计量（statistic）是只依赖样本的可测函数$T(\boldsymbol{Y})$。当统计量被设计来逼近某个未知目标$\tau(\vartheta)$时，它称为估计量（estimator），通常记为$\widehat{\tau}$。在一批已经观测的数据$\boldsymbol{y}$上算出的$\widehat{\tau}(\boldsymbol{y})$是估计值（estimate）。参数属于模型，估计量在重复抽样中是随机变量，估计值则是一次计算得到的数；混淆三者会使“偏差”和“不确定性”失去对象。
2. 推断目标可以有不同层次。估计$\theta$是在参数空间中找一个点；估计分布函数$F(y)$是在函数空间中恢复整体规律；预测未来观测$Y_{n+1}$则还要保留新噪声。
3. 定义（目标可识别性）：给定统计模型$\{P_\vartheta:\vartheta\in\Theta\}$和目标泛函$\tau:\Theta\to\mathcal T$，若对所有$\vartheta_1,\vartheta_2\in\Theta$有$P_{\vartheta_1}=P_{\vartheta_2} \quad\Longrightarrow\quad \tau(\vartheta_1)=\tau(\vartheta_2),$就称目标$\tau$在模型中是可识别的（identifiable）。
4. 不可识别还直接限制任何估计程序。对赋范目标空间，若在每个允许的样本量$n$下都有$P_{\vartheta_1}^{(n)}=P_{\vartheta_2}^{(n)}$，但$\tau(\vartheta_1)\neq\tau(\vartheta_2)$，取两目标值距离的三分之一为$\epsilon>0$。

##### 1.5.1.2 抽样与观测机制下的识别条件

主要内容：统计结论必须先回答“想对谁成立”。目标总体（target population）是推断希望覆盖的对象、时间和条件的集合；抽样制度（sampling regime）描述观测如何从这些对象产生。

论证与表述逻辑：

1. 独立同分布抽样把每个$Y_i$视为来自同一分布的独立重复。配对抽样则把$(Y_{i,A},Y_{i,B})$视为一个单位，例如同一对象在两种条件下的读数。
2. 定义（观测模式与缺失机制）：设完整数据为$\boldsymbol Z=(Z_1,\ldots,Z_d)$，观测指示$\boldsymbol R\in\{0,1\}^d$。对每种模式$\boldsymbol r$，定义$O(\boldsymbol r)=\{j:r_j=1\},\qquad M(\boldsymbol r)=\{j:r_j=0\}$实际记录为$(\boldsymbol r,\boldsymbol Z_{O(\boldsymbol r)})$。令$g(\boldsymbol r\mid\boldsymbol z)$为给定完整数据时的模式概率核。若对每种$\boldsymbol r$都存在只依赖已见坐标的可测函数$g_{\boldsymbol r}$，使$g(\boldsymbol r\mid\boldsymbol z)=g_{\boldsymbol r}(\boldsymbol z_{O(\boldsymbol r)})$对完整数据分布几乎处处成立，则称机制为MAR。若$g(\boldsymbol r\mid\boldsymbol z)$对全部模式均不依赖$\boldsymbol z$，则为MCAR；若MAR条件失败，则为MNAR。
3. 识别障碍在有界结果上已经出现。若$0\leq Y\leq1$且$\mathbb{P}(R=0)>0$，观测数据只给出已见部分的$RY$与缺失指示；把所有未见$Y$设为$0$或设为$1$会产生相同观测，却给出不同总体均值。

#### 1.5.2 参数与函数的估计

主要内容：目标能够由观测规律确定后，有限记录仍只提供它的近似。估计一个均值时，输出是一个数；估计分布或条件函数时，输出是一整条规律。

论证与表述逻辑：

1. 有限维目标的估计：给定观测$\boldsymbol{y}$后，似然（likelihood）$L(\vartheta;\boldsymbol{y})=p_\vartheta(\boldsymbol{y})$相对于模型共同的参考测度定义，把数据固定，把参数看作待比较的变量。
2. 分布与条件函数的估计：经验分布把每个样本点赋质量$1/n$，因而是完整的概率分布而不是密度曲线。独立同分布样本下，Glivenko--Cantelli定理给出$\sup_y|\widehat F_n(y)-F(y)|\to0$几乎必然；固定$y$的大数定律本身尚不等于这个统一结论。

##### 1.5.2.1 有限维目标的估计

主要内容：给定观测$\boldsymbol{y}$后，似然（likelihood）$L(\vartheta;\boldsymbol{y})=p_\vartheta(\boldsymbol{y})$相对于模型共同的参考测度定义，把数据固定，把参数看作待比较的变量。

论证与表述逻辑：

1. 对$Y_i\overset{\mathrm{iid}}{\sim}\mathcal{N}(\theta,\sigma^2)$，且$\sigma^2>0$已知，$-\log L(\theta;\boldsymbol{y}) =\frac{1}{2\sigma^2}\sum_{i=1}^n(y_i-\theta)^2+C$对$\theta$求导并令其为零，得到$\widehat\theta=\overline y$。
2. 定义（影响函数）：设$T$为定义在概率分布上的实值或向量值统计泛函，$\Delta_z$为全部质量集中在$z$的概率测度。假定充分小的正$\epsilon$所对应的污染分布仍在$T$的定义域内；若右侧极限存在且有限，定义影响函数（influence function）为$\operatorname{IF}(z;T,P)=\lim_{\epsilon\downarrow0} \frac{T((1-\epsilon)P+\epsilon\Delta_z)-T(P)}{\epsilon}$。
3. 有限维推断的目标也可以是一组总体分位数。设$Y_1,\ldots,Y_n$独立同分布且$0<q<1$，经验分布$\widehat F_n(y)=n^{-1}\sum_i\mathbb I_{\{Y_i\leq y\}}$的广义逆给出$\widehat q=Y_{(\lceil nq\rceil)}$。

##### 1.5.2.2 分布与条件函数的估计

主要内容：经验分布把每个样本点赋质量$1/n$，因而是完整的概率分布而不是密度曲线。独立同分布样本下，Glivenko--Cantelli定理给出$\sup_y|\widehat F_n(y)-F(y)|\to0$几乎必然；固定$y$的大数定律本身尚不等于这个统一结论。

论证与表述逻辑：

1. 有限维模型可能把真实分布限制得过强。非参数方法不预先固定有限个参数，但仍通过带宽、邻域或平滑度控制复杂度。
2. 条件分位数可由分位数回归估计。假设$Y$可积，使下面损失的条件期望对几乎每个$x$有限。

#### 1.5.3 未来观测的预测

主要内容：即使总体均值已知，下一次传感器读数仍会受新噪声影响。预测要把这种结果波动与估计未知规律的误差同时纳入。

论证与表述逻辑：

1. 预测分布的计算与评价：若参数给定，条件预测使用概率核$P_\theta(Y_{\rm new}\in\cdot\mid X_{\rm new}=x)$；代入估计得到插件预测，Bayes方法则对参数后验积分：$P(Y_{\rm new}\in A\mid\boldsymbol y,x) =\int P_\theta(Y_{\rm new}\in A\mid x)\,\pi(\mathrm d\theta\mid\boldsymbol y),$这里假设给定参数后新观测与训练数据按模型条件独立。
2. 预测集合的构造与覆盖：预测集合$C(\boldsymbol Y)$在规定的训练数据与未来观测联合规律下要求$\mathbb P\{Y_{n+1}\in C(\boldsymbol Y)\}\geq1-\alpha$，其中$0<\alpha<1$。

##### 1.5.3.1 预测分布的计算与评价

主要内容：若参数给定，条件预测使用概率核$P_\theta(Y_{\rm new}\in\cdot\mid X_{\rm new}=x)$；代入估计得到插件预测，Bayes方法则对参数后验积分：$P(Y_{\rm new}\in A\mid\boldsymbol y,x) =\int P_\theta(Y_{\rm new}\in A\mid x)\,\pi(\mathrm d\theta\mid\boldsymbol y),$这里假设给定参数后新观测与训练数据按模型条件独立。

论证与表述逻辑：

1. 对$K$个类别，令真实概率向量为$\boldsymbol p$，报告为$\boldsymbol q$，Brier评分可写成$S(\boldsymbol q,Y)=\sum_{k=1}^K(q_k-\mathbb{I}\{Y=k\})^2$。
2. 定义（二元概率校准）：设$Y\in\{0,1\}$，预测概率为随机变量$Q\in[0,1]$。若$\mathbb E[Y\mid Q]=Q\quad\text{几乎必然},$则称预测相对于当前联合总体分布是校准（calibration）的。等价地，$\mathbb P(Y=1\mid Q=q)=q$对$P_Q$-几乎每个$q$成立。
3. 后处理校准与评价条件温度缩放把分类器输出的未归一化实数得分$\boldsymbol z$（logit）先除以$T>0$，再使用归一化指数映射$\operatorname{softmax}(\boldsymbol z/T)$得到类别概率：对各分量取指数，再除以共同的指数和。

##### 1.5.3.2 预测集合的构造与覆盖

主要内容：预测集合$C(\boldsymbol Y)$在规定的训练数据与未来观测联合规律下要求$\mathbb P\{Y_{n+1}\in C(\boldsymbol Y)\}\geq1-\alpha$，其中$0<\alpha<1$。

论证与表述逻辑：

1. 命题（拆分共形的有限样本覆盖）：在上述条件下，$\mathbb{P}\bigl( Y_{m+1}\in C(X_{m+1})\bigr)\geq 1-\alpha$。
2. 推导：先假设分数无并列值。若未来真实标签未被覆盖，则$S_{m+1}>q$，所以未来分数在全部$m+1$个分数中的秩严格大于$k$。
3. 证明依赖两处对称性。训练与校准拆分使评分规则在校准阶段保持固定；校准样本与未来样本可交换，使未来分数的秩没有特殊位置。

#### 1.5.4 推断误差的评估

主要内容：一个估计数值需要评价平均损失或误差分布，一段参数范围需要评价重复抽样下的覆盖率，拒绝一个命题则需要控制误拒概率。

论证与表述逻辑：

1. 估计误差与效率：估计量的误差既来自系统偏移，也来自样本波动。设标量估计量$\widehat\theta\in L^2$。
2. 区间估计的覆盖：点估计没有说明误差尺度。覆盖区间需要先说明概率来自哪一次随机化，以及要覆盖的对象。
3. 假设检验的错误控制：区间描述目标的可能范围，假设检验（hypothesis testing）则检查数据与一个命题是否相容。

##### 1.5.4.1 估计误差与效率

主要内容：估计量的误差既来自系统偏移，也来自样本波动。设标量估计量$\widehat\theta\in L^2$。

论证与表述逻辑：

1. 命题（Cramér--Rao下界）：设$Y_1,\ldots,Y_n$独立同分布于$p_\theta$，并且上述正则条件成立且单样本Fisher信息满足$0<\mathcal I(\theta)<\infty$。若$\widehat\tau$对可微目标$\tau(\theta)$无偏、二阶矩有限，且其期望可对参数求导并移入积分，则$\operatorname{Var}_\theta(\widehat\tau) \geq\frac{\tau'(\theta)^2}{n\mathcal I(\theta)}$。
2. 推导：由无偏性$\mathbb{E}_\theta[\widehat\tau]=\tau(\theta)$对参数求导，并把导数移入积分，得到$\tau'(\theta) =\mathbb{E}_\theta[ (\widehat\tau-\tau(\theta))s_\theta(\boldsymbol Y)]$Cauchy--Schwarz不等式给出$\tau'(\theta)^2\leq \operatorname{Var}_\theta(\widehat\tau) \operatorname{Var}_\theta(s_\theta(\boldsymbol Y)) = \operatorname{Var}_\theta(\widehat\tau)n\mathcal I(\theta),$整理即得结论。
3. 交叉验证各折的误差通常相关，因为训练集大量重叠，不能默认它们独立。因此不能把$K$个折分数当成$K$个独立观测，再用普通样本方差构造过窄区间。

##### 1.5.4.2 区间估计的覆盖

主要内容：点估计没有说明误差尺度。覆盖区间需要先说明概率来自哪一次随机化，以及要覆盖的对象。

论证与表述逻辑：

1. 定义（置信、可信与预测覆盖）：置信区间（confidence interval）是一项重复抽样程序：若每次按同一制度抽样并构造$C(\boldsymbol Y)$，则对模型中的每个$\theta$都有$\mathbb{P}_\theta\{\theta\in C(\boldsymbol Y)\}\geq1-\alpha$频率学派参数始终视作固定值；数据固定后，得到的区间也固定，不能把它解释为“以$1-\alpha$概率包含参数”。Bayes可信区间（credible interval）则在给定数据和模型后满足$\mathbb{P}(\theta\in C\mid\boldsymbol y)\geq1-\alpha$，其数值依赖先验；连续后验常可取到等号，离散后验可能只能给出更大的覆盖概率。预测集合（prediction set）把覆盖对象改成未来结果，在规定的训练样本与未来观测联合分布下要求$\mathbb{P}\{Y_{n+1}\in C(\boldsymbol Y)\}\geq1-\alpha$。三者的概率分别来自重复样本、参数后验，以及训练样本与未来观测的联合抽样，不能只按区间端点的外观解释。
2. 定义（置信序列）：对参数为$\theta$时的数据分布$\mathbb P_\theta$，数据依赖集合$(C_t)_{t\geq1}$若在时刻$t$由$\mathcal F_t$确定，且对每个允许的$\theta$满足$\mathbb P_\theta(\theta\in C_t\text{ 对所有 }t\geq1)\geq1-\delta,$则称为覆盖水平$1-\delta$的置信序列（confidence sequence），其中$0<\delta<1$。
3. 条件次高斯性也不是有限方差的同义词。$\lambda$保证初期矩阵可逆并编码参数范数先验，但过大的$\lambda$会增加$\sqrt{\lambda}B$偏差项。

##### 1.5.4.3 假设检验的错误控制

主要内容：区间描述目标的可能范围，假设检验（hypothesis testing）则检查数据与一个命题是否相容。

论证与表述逻辑：

1. 命题（Neyman--Pearson引理）：对两个完全指定的简单假设$H_0:P=P_0$与$H_1:P=P_1$，设$P_1\ll P_0$，似然比为$\Lambda=\mathrm dP_1/\mathrm dP_0$。在所有大小不超过$\alpha$的检验中，拒绝大似然比并在边界适当随机化的检验具有最大功效。
2. 推导：取常数$c\geq0$与边界随机化概率，使检验$\varphi^\star$满足$\mathbb{E}_0[\varphi^\star]=\alpha$，并在$\Lambda>c$时拒绝、在$\Lambda<c$时接受。对任意$\mathbb{E}_0[\varphi]\leq\alpha$的检验，$(\varphi^\star-\varphi)(\Lambda-c)\geq0$逐点成立，因为$\varphi^\star$在$\Lambda>c$处取最大允许值，在$\Lambda<c$处取最小允许值。对$P_0$积分得到$\mathbb{E}_1[\varphi^\star-\varphi] \geq c\,\mathbb{E}_0[\varphi^\star-\varphi]\geq0$所以$\varphi^\star$的备择拒绝概率不小于任何同大小检验。
3. 已有观测可以用来选择候选规律，剩余预算则允许选择新的观测。两类选择的目标不同：模型证据、未来风险和信息价值不能直接共用一个解释。

#### 1.5.5 候选模型的比较

主要内容：上一组工具评价预测分布；多个模型竞争时，还需先决定比较的是训练拟合、未来预测还是模型证据。边缘似然对参数积分，Laplace近似用局部曲率近似这项积分。

论证与表述逻辑：

1. 命题（固定维Laplace局部积分近似）：设$\Theta\subseteq\mathbb{R}^d$为可测集，$\widehat{\boldsymbol\vartheta}\in\operatorname{int}(\Theta)$。函数$h:\Theta\to\mathbb{R}$可测，并在$\widehat{\boldsymbol\vartheta}$的某个邻域内二阶连续可微；该点是$h$在$\Theta$上的唯一全局最大点，且$\boldsymbol H=-\nabla^2h(\widehat{\boldsymbol\vartheta})$正定。函数$g:\Theta\to[0,\infty)$局部可积，在该点的某个邻域内连续，并满足$g(\widehat{\boldsymbol\vartheta})>0$。进一步假设存在$\delta,\eta>0$和$n_0\geq1$，使$\overline{B_\delta(\widehat{\boldsymbol\vartheta})}\subseteq\Theta$，$h,g$在该闭球所在的邻域内分别满足上述光滑性与连续性，并且$\sup_{\boldsymbol\vartheta\in \Theta\setminus B_\delta(\widehat{\boldsymbol\vartheta})} h(\boldsymbol\vartheta) \leq h(\widehat{\boldsymbol\vartheta})-\eta, \qquad \int_\Theta \exp\!\left\{n_0\bigl[h(\boldsymbol\vartheta) -h(\widehat{\boldsymbol\vartheta})\bigr]\right\} g(\boldsymbol\vartheta)\,\mathrm d\boldsymbol\vartheta<\infty$则当$n\to\infty$时，$\int_\Theta \exp\{n h(\boldsymbol\vartheta)\}g(\boldsymbol\vartheta)\, \mathrm d\boldsymbol\vartheta = \exp\{nh(\widehat{\boldsymbol\vartheta})\} g(\widehat{\boldsymbol\vartheta}) \left(\frac{2\pi}{n}\right)^{d/2} |\boldsymbol H|^{-1/2}\{1+o(1)\}$。
2. 推导：正定性与二阶连续性保证：必要时缩小$\delta$，存在$c>0$，使闭球内有$h(\boldsymbol\vartheta)-h(\widehat{\boldsymbol\vartheta}) \leq-c\lVert\boldsymbol\vartheta-\widehat{\boldsymbol\vartheta}\rVert_2^2$缩小闭球后，原闭球中剩余的紧致环带由唯一最大性给出严格间隔；把它与原来的尾部间隔合并，仍可取某个$\eta>0$满足定理中的一致上界。另一方面，在最大点附近作多元Taylor展开：$h(\boldsymbol\vartheta) = h(\widehat{\boldsymbol\vartheta}) -\frac12(\boldsymbol\vartheta-\widehat{\boldsymbol\vartheta})^\top \boldsymbol H(\boldsymbol\vartheta-\widehat{\boldsymbol\vartheta}) +o(\lVert\boldsymbol\vartheta-\widehat{\boldsymbol\vartheta}\rVert_2^2)$令$\boldsymbol u=\sqrt n\,\boldsymbol H^{1/2} (\boldsymbol\vartheta-\widehat{\boldsymbol\vartheta})$，则逆变换的Jacobian行列式绝对值为$n^{-d/2}|\boldsymbol H|^{-1/2}$，即$\mathrm d\boldsymbol\vartheta =n^{-d/2}|\boldsymbol H|^{-1/2}\mathrm d\boldsymbol u$。对每个固定的$\boldsymbol u$，Taylor展开与$g$的连续性使变换后的被积函数收敛到$g(\widehat{\boldsymbol\vartheta})\exp(-\lVert\boldsymbol u\rVert_2^2/2)$。
3. 混合模型的标签交换、参数位于边界、额外成分权重为零或Fisher信息奇异时，最大点可能不唯一，局部曲率可能退化，常规Laplace展开和$d\log n$惩罚随之失效。

#### 1.5.6 预算约束下的观测设计

主要内容：推断质量不仅由分析方法决定，也由数据如何取得决定。随机分配使处理指派在设计上独立于这些预先固定的结果，从而把系统差异转成可量化的随机误差。

论证与表述逻辑：

1. 消融实验删除一个组件并保持其他条件不变，用来判断该组件对整体结果的增量贡献。基线、随机种子、停止规则和评价集都应在比较前固定。
2. 主动选择会改变被标注样本的分布。若候选池不覆盖目标总体，算法无法询问缺失区域；若标注噪声随难度变化，不确定样本还可能最不可靠；若最终指标用同一批自适应选择数据计算，评价也会偏移。

### 1.6 随机序列与过程的收敛

主要内容：明确概率、几乎处处与分布等收敛方式，分别研究样本平均、标准化累计偏差、状态分布、时间平均和随机路径的极限。

论证与表述逻辑：

1. 随机变量序列的收敛：“越来越接近”可能说的是几乎每条实现，也可能只是大误差事件越来越少，或分布整体趋近。先规定接近方式，再讨论平均和缩放波动各自趋向什么。
2. 重复采样下的平均序列收敛：每增加一个独立读数，都把累计和除以新的样本数，得到$\overline X_n=n^{-1}\sum_{i=1}^nX_i$。
3. 重复采样下的标准化累计偏差序列分布收敛：平均值接近总体均值后，仍可考察剩下的随机波动。先从累计和中减去$n\mu$，再除以独立累计的标准差$\sigma\sqrt n$，得到$(\sum_{i=1}^nX_i-n\mu)/(\sigma\sqrt n)$。
4. 状态转移下的时间平均序列收敛：沿同一条Markov轨迹计算$n^{-1}\sum_{t=1}^n f(Z_t)$，每次新读数都与此前状态相关。
5. 状态转移下的分布序列收敛：上一节的时间平均可以在逐时刻分布振荡时仍然收敛。现在固定初始状态，比较每步状态的分布$P^t(z,\cdot)$是否趋于$\pi$。

#### 1.6.1 随机变量序列的收敛

主要内容：“越来越接近”可能说的是几乎每条实现，也可能只是大误差事件越来越少，或分布整体趋近。先规定接近方式，再讨论平均和缩放波动各自趋向什么。

论证与表述逻辑：

1. 随机结果的收敛：逐个时刻的尾概率还不足以判断一条样本路径是否反复进入坏事件。记$\limsup_{n\to\infty}A_n = \bigcap_{m=1}^{\infty}\bigcup_{n\geq m}A_n,$它表示事件$A_n$发生无穷多次。
2. 概率分布的弱收敛：此前的依分布收敛比较数值随机结果。路径、随机向量和最优传输中的联合分布也需要同一种比较，但未必共用基础概率空间。

##### 1.6.1.1 随机结果的收敛

主要内容：逐个时刻的尾概率还不足以判断一条样本路径是否反复进入坏事件。记$\limsup_{n\to\infty}A_n = \bigcap_{m=1}^{\infty}\bigcup_{n\geq m}A_n,$它表示事件$A_n$发生无穷多次。

论证与表述逻辑：

1. 命题（二阶矩有界鞅的收敛）：若$(M_n,\mathcal F_n)$是平方可积鞅且$\sup_n\mathbb E M_n^2<\infty$，则存在$M_\infty\in L^2$，使$M_n\to M_\infty$几乎必然且在$L^2$中成立，并且$M_n=\mathbb E[M_\infty\mid\mathcal F_n]$。
2. 推导：对$m\geq n$，条件均值性质给出$\mathbb E[M_n(M_m-M_n)]=0$，所以$\mathbb E(M_m-M_n)^2=\mathbb EM_m^2-\mathbb EM_n^2$右侧来自单调有界数列，故$M_n$在$L^2$中Cauchy，有$L^2$极限$M_\infty$。还需将均方极限提升到整条序列的几乎必然极限。对有限鞅$Y_j$及$Y^*=\max_{j\leq N}|Y_j|$，按首次越过水平$a$的时刻分解事件，并用$|Y_j|\leq\mathbb E[|Y_N|\mid\mathcal F_j]$，得$a\,\mathbb P(Y^*\geq a) \leq\mathbb E[|Y_N|\mathbb I_{\{Y^*\geq a\}}]$积分并用Cauchy--Schwarz，得到$\begin{aligned} \mathbb E(Y^*)^2 &\leq2\mathbb E(|Y_N|Y^*)\\ &\leq2\|Y_N\|_2\|Y^*\|_2, \end{aligned}$故$\mathbb E(Y^*)^2\leq4\mathbb E Y_N^2$。
3. 随机逼近将用平方可和步长控制累计鞅噪声；状态本身是否收敛，还要结合稳定性与漂移，不能只用这一定理替代。

##### 1.6.1.2 概率分布的弱收敛

主要内容：此前的依分布收敛比较数值随机结果。路径、随机向量和最优传输中的联合分布也需要同一种比较，但未必共用基础概率空间。

论证与表述逻辑：

1. 弱收敛的另一困难是质量可能不断远移，使任何候选极限都留不住总概率。需要紧性把绝大部分质量统一留在可控区域。
2. 命题（Prokhorov定理）：Polish空间上的Borel概率测度族一致紧，当且仅当它相对弱序列紧，即每个序列都能抽出弱收敛到该空间上某个概率测度的子列。每个单独的Borel概率测度都是紧的。
3. 在$\mathbb R^d$中，若$\sup_n\mathbb E\|X_n\|^p\leq C<\infty$，其中$p>0$，则$\sup_n\mathbb P(\|X_n\|>R)\leq C/R^p$闭球紧，故这些分布一致紧。

#### 1.6.2 重复采样下的平均序列收敛

主要内容：每增加一个独立读数，都把累计和除以新的样本数，得到$\overline X_n=n^{-1}\sum_{i=1}^nX_i$。

论证与表述逻辑：

1. 命题（强大数定律）：若$X_1,X_2,\ldots$独立同分布，且$\mathbb{E}[|X_1|]<\infty$，则$\overline{X}_n =\frac{1}{n}\sum_{i=1}^{n}X_i\to_{\mathrm{a.s.}}\mathbb{E}[X_1]$。
2. 强大数定律说明同一分布下的独立重复观测，其平均几乎必然接近期望。有限方差是许多初等证明使用的方便条件，但独立同分布版本的结论只需有限一阶绝对矩。
3. 有限方差时，较弱的依概率结论可以在这里完整得到。强大数定律只要求有限一阶绝对矩，但其证明还需截断大取值、控制截断变量的独立和，并把可求和坏事件转成几乎必然结论；不能由上面的逐个$n$概率界直接推出。

#### 1.6.3 重复采样下的标准化累计偏差序列分布收敛

主要内容：平均值接近总体均值后，仍可考察剩下的随机波动。先从累计和中减去$n\mu$，再除以独立累计的标准差$\sigma\sqrt n$，得到$(\sum_{i=1}^nX_i-n\mu)/(\sigma\sqrt n)$。

论证与表述逻辑：

1. 命题（Lindeberg--L\'evy中心极限定理）：若$X_1,X_2,\ldots$独立同分布，$\mathbb{E}X_1=\mu$，$0<\operatorname{Var}(X_1)=\sigma^2<\infty$，则$\frac{\sqrt{n}(\overline{X}_n-\mu)}{\sigma} \Rightarrow\mathcal{N}(0,1)$。
2. 大数定律研究未缩放误差是否趋于零，中心极限定理研究乘以$\sqrt{n}$后的剩余波动近似什么分布。若方差无限、样本依赖过强或分布随$n$变化而不满足相应Lindeberg条件，$\sqrt{n}$缩放与高斯极限都可能失效。
3. 自归一化重要性估计是两个平均的比。设非归一化权重$\widetilde w\geq0$，$0<Z=\mathbb E_Q\widetilde w<\infty$，且$\mathbb E_Q|\widetilde wf|<\infty$。

#### 1.6.4 状态转移下的时间平均序列收敛

主要内容：沿同一条Markov轨迹计算$n^{-1}\sum_{t=1}^n f(Z_t)$，每次新读数都与此前状态相关。

论证与表述逻辑：

1. 从$i$出发，把从一次访问$i$起、到下一次返回$i$前为止的路径作为一个游程。Markov性质在这类随机时刻之后仍成立，称为强Markov性；在有限离散链中，把返回时刻的各个可能取值分别代入Markov条件即可验证。
2. 定义（一般状态空间的不可约性与Harris常返性）：固定$(\mathcal{Z},\mathcal{A})$上的非零参考测度$\varphi$。常用的$\varphi$不可约性要求：对每个满足$\varphi(B)>0$的$B\in\mathcal{A}$以及每个初态$z\in\mathcal{Z}$，链从$z$出发都有正概率在有限时间内到达$B$；若只研究某个不可约类，就先把$\mathcal{Z}$限制为该类。在此基础上，Harris常返性（Harris recurrence）要求这些正测度集合以概率$1$被反复访问；正Harris常返性（positive Harris recurrence）再要求存在不变概率分布。
3. 若自相关为负，$\tau_f$也可能小于$1$；有效样本量是特定估计量的方差等价口径，不是链中“真正保留下来”的样本条数。

#### 1.6.5 状态转移下的分布序列收敛

主要内容：上一节的时间平均可以在逐时刻分布振荡时仍然收敛。现在固定初始状态，比较每步状态的分布$P^t(z,\cdot)$是否趋于$\pi$。

论证与表述逻辑：

1. 几何遍历是方便而有力的充分条件，不是所有遍历链都必须满足的定义。
2. 分布收敛所需的步数逐时刻分布趋近平稳分布以后，还可以问：从最不利的初态出发，需要多少步才能达到指定的分布误差？
3. 定义（有限链的混合时间）：对具有平稳分布$\pi$的有限时间齐次链，定义$d(t) = \sup_{z\in\mathcal{Z}} \lVert P^t(z,\cdot)-\pi\rVert_{\mathrm{TV}},$对$0<\varepsilon<1$，混合时间为$t_{\mathrm{mix}}(\varepsilon)=\inf\{t\in\mathbb N_0:d(t)\leq\varepsilon\}$，空集的下确界约定为$\infty$。

#### 1.6.6 随机路径的收敛

主要内容：前面讨论同一个过程是否有连续版本；现在比较的是一列过程及其极限。路径极限把整条函数当成随机对象，必须先规定函数之间怎样接近。

论证与表述逻辑：

1. 命题（连续路径的紧性与极限识别）：设$X_n$是$C([0,T])$值随机对象。令$w(x,\delta)=\sup_{\substack{s,t\in[0,T]\\|t-s|\leq\delta}}|x(t)-x(s)|$若$(X_n(0))$的分布一致紧，且对每个$\varepsilon>0$，$\lim_{\delta\downarrow0}\sup_n \mathbb P\{w(X_n,\delta)>\varepsilon\}=0,$则路径分布一致紧。若其有限维分布还收敛到某个连续过程$X$的有限维分布，则$X_n\Rightarrow X$于$C([0,T])$。
2. 为把概率条件对应到这两项要求，固定$0<\epsilon<1$。由初值一致紧选$M<\infty$，使$\sup_n\mathbb P(|X_n(0)|>M)\leq\epsilon/2$。
3. 缩放随机游走给出重要入口。若$\xi_i$独立同分布、均值零、方差一，令$S_k=\sum_{i=1}^k\xi_i$，在网格$k/n$上取$S_k/\sqrt n$并作线性插值。

### 1.7 本章小结

主要内容：以传感器读数串联生成规律、依赖、统计推断和极限，强调每类随机对象与结论都需要相应的概率条件。

论证与表述逻辑：

1. 传感器的一次读数、反复读数得到的平均值、未来读数的预测，以及一段时间内的完整记录，是不同的随机对象。概率空间规定哪些结果可以比较概率，可测映射规定怎样把结果变成读数，分布则保存这些读数的取值规律。
2. 有限观测的精度与无穷观测的极限回答不同的问题。集中界给定观测次数后控制偏差；统一界还覆盖看过样本以后作出的候选选择。
3. 规律未知时，要从观测模型出发确定目标能否识别，再讨论估计误差与未来结果的波动。置信区间覆盖固定总体参数，后验可信区间描述参数的后验质量，预测范围覆盖未来结果；对应概率分别来自重复抽样、参数后验，以及训练样本与未来结果的联合抽样。
4. 函数变换、条件随机生成和概率加权为后续分布比较与状态建模提供了共同运算。可积性、支持、依赖和正则条件决定哪些公式能够复用，不能仅凭模型名称作出保证。

## 第2章 概率分布

正文：[02-information-theory-and-statistical-geometry.tex](../../tex/02-mathematical-preliminaries-lower/01-random-variables-distributions-and-causality/02-information-theory-and-statistical-geometry.tex)。

### 2.1 观测的信息量

主要内容：从编码长度引出离散信息量、熵与条件熵，再说明连续情形的信息量及其坐标与密度条件。

论证与表述逻辑：

1. 连续观测的信息量：连续结果若要求无限精度，单次记录通常不能用有限比特无失真描述。可以先把实轴分成宽度$\Delta$的小格；在密度足够规则时，格子概率近似$p(x)\Delta$，格子编码熵便近似$-\int p\log p-\log\Delta$。

#### 2.1.1 离散观测的信息量

主要内容：从离散观测的描述代价建立自信息与平均熵，再讨论给定已有观测后的剩余不确定性。

论证与表述逻辑：

1. 先用事件概率与编码长度的联系说明平均信息量。
2. 再固定已见变量，逐条件计算剩余信息并对条件加权，区分无条件与条件描述的对象。

##### 2.1.1.1 无条件观测的平均信息量

主要内容：设结果$x$的发生概率为$p(x)>0$。两个独立结果的联合概率相乘，而描述长度应相加，这使负对数成为自然的计量方式。

论证与表述逻辑：

1. 命题（无失真前缀码的平均长度界）：对熵有限的质量函数$p$，任意满足Kraft约束的二进制码长均满足$\mathbb E\ell(X)\geq H(X)/\log2$在有效字母表$\mathcal X_+=\{x:p(x)>0\}$上，$\ell(x)=\lceil-\log_2p(x)\rceil$可由前缀码实现，并且$\mathbb E\ell(X)<H(X)/\log2+1$。
2. 推导：若平均码长无限，下界直接成立。否则令$K=\sum_x2^{-\ell(x)}\in(0,1]$、$q(x)=2^{-\ell(x)}/K$。由$-\log u\geq1-u$，在$p>0$的点上求和得到$\sum_xp(x)\log\frac{p(x)}{q(x)} \geq1-\sum_{x:p(x)>0}q(x)\geq0$所以$0\leq-H(X)+(\log2)\mathbb E\ell(X)+\log K$因$\log K\leq0$，移项即得下界。
3. Bernoulli例子的两个有效结果都必须使用至少一位，逐符号码长为$1$ bit；与$0.8113$ bit的差来自整数限制。

##### 2.1.1.2 条件观测的剩余信息量

主要内容：若发送者和接收者都知道$Y=y$，需要描述的是条件分布$p(x\mid y)$，而不是重新描述整个$X$。前章的条件分布使这一点可以逐个条件值计算。

论证与表述逻辑：

1. 定义（离散条件熵）：对离散随机变量$X,Y$，在$p(y)>0$处令$H(X\mid Y=y)=-\sum_xp(x\mid y)\log p(x\mid y)$。条件熵（conditional entropy）定义为这些剩余信息量的平均：$H(X\mid Y)=\sum_yp(y)H(X\mid Y=y) =-\sum_{x,y}p(x,y)\log p(x\mid y)$零质量条件值可以任意指定条件分布，贡献为零；结果允许为$+\infty$。
2. 在联合质量为正的点，$p(x,y)=p(y)p(x\mid y)$。对负对数取期望得到$\begin{aligned} H(X,Y) &=-\sum_{x,y}p(x,y)\log p(y) -\sum_{x,y}p(x,y)\log p(x\mid y)\\ &=H(Y)+H(X\mid Y) \end{aligned}$这些项非负，非负求和换序保证等式在扩展值意义下也成立。
3. 示例（一次带噪二元观测）：令$X$在$\{0,1\}$上均匀，观测$Y=X\oplus N$，其中$\oplus$为异或，$N\sim\operatorname{Bernoulli}(\varepsilon)$独立于$X$，$0\leq\varepsilon\leq1/2$。

#### 2.1.2 连续观测的信息量

主要内容：连续结果若要求无限精度，单次记录通常不能用有限比特无失真描述。可以先把实轴分成宽度$\Delta$的小格；在密度足够规则时，格子概率近似$p(x)\Delta$，格子编码熵便近似$-\int p\log p-\log\Delta$。

论证与表述逻辑：

1. 定义（微分熵）：固定参考测度$\mu$。若$P\ll\mu$、$p=\mathrm dP/\mathrm d\mu$，且$\mathbb E_P|\log p(X)|<\infty$，定义相对于$\mu$的熵$h_\mu(P)=-\int p\log p\,\mathrm d\mu$在$\mathbb R^d$上取Lebesgue测度时，称为微分熵（differential entropy），简记为$h(\boldsymbol X)$。
2. 指定参考测度是定义的一部分。若换成$\mu'=a\mu$，其中$a>0$，密度变为$p/a$，故$h_{\mu'}(P)=h_\mu(P)+\log a$。
3. 坐标变化有相同影响。设$\boldsymbol X$具有Lebesgue密度$p_{\boldsymbol X}$，且$\mathbb E|\log p_{\boldsymbol X}(\boldsymbol X)|<\infty$。

### 2.2 概率分布之间的关系

主要内容：比较事件概率、函数期望、质量搬运和对数评分下的分布差异，并讨论联合分布内部的依赖。

论证与表述逻辑：

1. 分布的差异关系：下面始终比较同一空间上的两张分布$P,Q$。事件概率差关注发生与否，函数期望差关注特定读数，搬运成本关注位置，对数评分关注为真实结果分配的概率。
2. 联合分布的依赖关系：现有差异工具还可以用于两个变量之间的关系。固定它们的真实联合分布，再用各自边缘的独立乘积作参照：两张分布有相同的单变量边缘，差异只来自共同变化。

#### 2.2.1 分布的差异关系

主要内容：下面始终比较同一空间上的两张分布$P,Q$。事件概率差关注发生与否，函数期望差关注特定读数，搬运成本关注位置，对数评分关注为真实结果分配的概率。

论证与表述逻辑：

1. 概率权重的差异：报警规则由一个事件$A$指定。若尚未决定具体规则，可以问所有事件中，哪一个的发生概率改变最多。
2. 函数期望的差异：如果任务只计算指定的一类函数，控制所有可测事件可能超出需要。可以把每个允许的测试函数当作一种观测，再比较它在两个分布下的平均读数。
3. 质量位置的差异：两个不同位置上的点质量没有重叠，TV因而始终为一。若结果是温度读数，把全部质量移动$0.01$度与移动$10$度却有不同意义。
4. 对数评分的差异：仍然编码结果，但接收者现在只持有预测分布$Q$，真实结果却来自$P$。按$Q$分配的理想码长为$-\log q(x)$；高概率真实结果若被$Q$低估，平均描述就会变长。

##### 2.2.1.1 概率权重的差异

主要内容：报警规则由一个事件$A$指定。若尚未决定具体规则，可以问所有事件中，哪一个的发生概率改变最多。

论证与表述逻辑：

1. 有时需要对称地比较密度形状，又希望使用Hilbert空间的几何。把密度开平方便得到单位$L^2$范数的函数。
2. 定义（Hellinger距离）：在共同支配测度$\mu$下，定义平方Hellinger距离为$d_{\mathrm H}^2(P,Q)=\tfrac12\int(\sqrt p-\sqrt q)^2\,\mathrm d\mu =1-\int\sqrt{pq}\,\mathrm d\mu,$距离本身为其非负平方根。
3. 更换共同支配测度时，两个平方根都乘以同一密度因子的平方根，积分换元后不变。对三个分布可统一使用其和作支配测度，从$L^2$三角不等式得到$d_{\mathrm H}$的三角不等式。

##### 2.2.1.2 函数期望的差异

主要内容：如果任务只计算指定的一类函数，控制所有可测事件可能超出需要。可以把每个允许的测试函数当作一种观测，再比较它在两个分布下的平均读数。

论证与表述逻辑：

1. 再生性质给出$|f(x)|\leq\|f\|_{\mathcal H}\sqrt{k(x,x)}$，所以$f\mapsto\mathbb E_Pf$是有界线性泛函。
2. 定义（核的特征性）：在核均值均存在的指定分布类$\mathcal P$上，若$\boldsymbol\mu_P=\boldsymbol\mu_Q$蕴含$P=Q$，即核均值映射为单射，则称核$k$在$\mathcal P$上具有特征性（characteristic）。
3. 零MMD能否推出同分布，取决于这个条件。取同一对分布$P=\delta_0$、$Q=(\delta_{-1}+\delta_1)/2$。

##### 2.2.1.3 质量位置的差异

主要内容：两个不同位置上的点质量没有重叠，TV因而始终为一。若结果是温度读数，把全部质量移动$0.01$度与移动$10$度却有不同意义。

论证与表述逻辑：

1. 定义（Wasserstein距离）：设$(\mathcal X,d)$为完备可分度量空间，$1\leq r<\infty$，固定基点$x_0$并令$\mathcal P_r(\mathcal X)= \left\{P:\int d(x,x_0)^r\,\mathrm dP(x)<\infty\right\}$对$P,Q\in\mathcal P_r(\mathcal X)$，定义$W_r(P,Q)=\left[ \inf_{\gamma\in\Pi(P,Q)}\int d(x,y)^r\,\mathrm d\gamma(x,y) \right]^{1/r}$。
2. 由$d(x,x_1)^r\leq2^{r-1}\{d(x,x_0)^r+d(x_0,x_1)^r\}$，矩条件不依赖基点；同一不等式说明独立耦合的成本有限。
3. 对有限一阶矩的$P,Q$，Kantorovich--Rubinstein对偶给出$W_1(P,Q)=\sup_{\operatorname{Lip}(f)\leq1} |\mathbb E_Pf-\mathbb E_Qf|$其中$\operatorname{Lip}(f)\leq1$表示$|f(x)-f(y)|\leq d(x,y)$。

##### 2.2.1.4 对数评分的差异

主要内容：仍然编码结果，但接收者现在只持有预测分布$Q$，真实结果却来自$P$。按$Q$分配的理想码长为$-\log q(x)$；高概率真实结果若被$Q$低估，平均描述就会变长。

论证与表述逻辑：

1. 推导：KL无限时无需证明；否则$P\ll Q$。在$A$及其补集分别对密度比使用条件Jensen不等式，得到$D_{\mathrm{KL}}(P\Vert Q)\geq a\log\frac ab+(1-a)\log\frac{1-a}{1-b}$固定$b\in(0,1)$，右侧作为$a$的函数在$a=b$处值和一阶导数为零，二阶导数为$1/[a(1-a)]\geq4$。Taylor积分余项给出至少$2(a-b)^2$。
2. 定义（高于一阶的Rényi散度）：对$\alpha>1$及$P\ll Q$，R\'enyi散度定义为$D_\alpha(P\Vert Q) =\frac1{\alpha-1}\log\mathbb E_Q \left[\left(\frac{\mathrm dP}{\mathrm dQ}\right)^\alpha\right]$若绝对连续性失败或该阶矩无限，结果为$+\infty$。
3. 对点质量$\delta_0,\delta_\varepsilon$，只要$\varepsilon\neq0$，TV恒为一、两个方向KL均无限，而$W_r=|\varepsilon|\to0$。

#### 2.2.2 联合分布的依赖关系

主要内容：现有差异工具还可以用于两个变量之间的关系。固定它们的真实联合分布，再用各自边缘的独立乘积作参照：两张分布有相同的单变量边缘，差异只来自共同变化。

论证与表述逻辑：

1. 无条件下的依赖关系：对具有联合分布$P_{XY}$的随机元素$X,Y$，互信息（mutual information, MI）定义为$I(X;Y)=D_{\mathrm{KL}}(P_{XY}\Vert P_X\otimes P_Y)$定义适用于一般可测空间，允许值为$+\infty$，不要求先存在密度或有限熵。
2. 条件观测下的依赖关系：已经知道$Z$时，应在同一个条件值下判断$X,Y$是否还有关系，再按$Z$的发生概率平均。不能把三者的边缘依赖随意相减。

##### 2.2.2.1 无条件下的依赖关系

主要内容：对具有联合分布$P_{XY}$的随机元素$X,Y$，互信息（mutual information, MI）定义为$I(X;Y)=D_{\mathrm{KL}}(P_{XY}\Vert P_X\otimes P_Y)$定义适用于一般可测空间，允许值为$+\infty$，不要求先存在密度或有限熵。

论证与表述逻辑：

1. 定义（互信息）：对具有联合分布$P_{XY}$的随机元素$X,Y$，互信息（mutual information, MI）定义为$I(X;Y)=D_{\mathrm{KL}}(P_{XY}\Vert P_X\otimes P_Y)$定义适用于一般可测空间，允许值为$+\infty$，不要求先存在密度或有限熵。
2. Gibbs不等式给出非负性，而且$I(X;Y)=0$当且仅当$X,Y$独立。这强于零协方差：例如$X$在$\{-1,0,1\}$上均匀，$Y=X^2$，协方差为零，但$Y$完全由$X$确定，互信息为$H(Y)=H_{\mathrm b}(1/3)>0$。
3. 由于对两个变量分别施加可逆变换会同时推送联合分布与边缘乘积，互信息继承KL的不变性。这与微分熵随坐标单位改变形成区别。

##### 2.2.2.2 条件观测下的依赖关系

主要内容：已经知道$Z$时，应在同一个条件值下判断$X,Y$是否还有关系，再按$Z$的发生概率平均。不能把三者的边缘依赖随意相减。

论证与表述逻辑：

1. 命题（数据处理不等式）：若标准Borel随机元素满足Markov关系$X\to Y\to Z$，即$X\perp Z\mid Y$，则$I(X;Z)\leq I(X;Y)$，允许扩展值。
2. 推导：用两种顺序分解同一联合信息量：$\begin{aligned} I(X;Y,Z)&=I(X;Y)+I(X;Z\mid Y)=I(X;Y),\\ I(X;Y,Z)&=I(X;Z)+I(X;Y\mid Z)\geq I(X;Z) \end{aligned}$第一行的条件项由条件独立为零，第二行的条件项非负，合并即得。证明只作非负项的相加和比较，不需要有限熵，也没有无穷相减。
3. 处理可以是$Z=g(Y)$，也可以是仅依赖$Y$的随机通道。若额外随机性还与$X$关联，Markov前提可能不成立。

### 2.3 基于观测的分布区分

主要内容：由观测分布难以区分推出估计目标的误差下界，分别处理固定样本与序贯观测的辨认限制。

论证与表述逻辑：

1. 固定观测下的分布区分：先把整批观测的分布视为已给定，不让程序根据中途结果改变取样位置。两候选比较利用TV，多候选比较则需要把候选数量也纳入信息预算。
2. 序贯观测下的分布区分：若观测位置根据已获得的结果改变，最终资料的联合分布也随算法改变。仍可使用前面的检验不等式，但比较对象应当是包含行动与结果的完整轨迹。

#### 2.3.1 固定观测下的分布区分

主要内容：先把整批观测的分布视为已给定，不让程序根据中途结果改变取样位置。两候选比较利用TV，多候选比较则需要把候选数量也纳入信息预算。

论证与表述逻辑：

1. 两个候选的区分下界：设观测$Z$来自$P_0$或$P_1$，先验各为$1/2$。 命题（Le Cam两点下界）：设观测模型$P_0,P_1$对应目标$\theta_0,\theta_1$，在目标空间度量$d$下有$d(\theta_0,\theta_1)\geq2s$，$s>0$。任意估计量$\widehat\theta$均满足$\max_{j\in\{0,1\}}P_j\{d(\widehat\theta,\theta_j)\geq s\} \geq\frac{1-d_{\mathrm{TV}}(P_0,P_1)}2$。
2. 多个候选的区分下界：两点只要求区分一个二元选择；高维问题可能同时包含许多不同目标。令$V$在$\{1,\ldots,M\}$上均匀，给定$V=v$后观测$Z\sim P_v$。 命题（Fano不等式）：对$M\geq2$及上述观测模型，$p_{\mathrm e}\geq1-\frac{I(V;Z)+\log2}{\log M}$。

#### 2.3.2 序贯观测下的分布区分

主要内容：若观测位置根据已获得的结果改变，最终资料的联合分布也随算法改变。仍可使用前面的检验不等式，但比较对象应当是包含行动与结果的完整轨迹。

论证与表述逻辑：

1. 重复与时序观测的信息累积：独立重复是简单情形。固定有限个分量$t=1,\ldots,T$，假设$P_t\ll Q_t$，密度比为$L_t$。 固定有限时域无需停止论证。若共同停止规则给出$\tau\leq T$，停止后补同一个吸收符号，其条件信息代价为零，公式仍适用。
2. 自适应观测的区分下界：固定有限时域$T$，设算法$\mathcal A$在时刻$t$根据历史，从有限或可数位置集合中选择来源或状态行动对$(s,a)$。 考虑两个可选Bernoulli来源$A,B$。环境$0$的均值为$(1/2+\varepsilon,1/2)$，环境$1$为$(1/2+\varepsilon,1/2+2\varepsilon)$，$0<\varepsilon<1/4$。

### 2.4 概率分布变化下的期望响应

主要内容：在评价函数有界、变化受限或指数矩受控时，分别用分布距离控制期望的变化。

论证与表述逻辑：

1. 有界函数的期望响应：设固定可测损失$f$取值于$[0,1]$。
2. 敏感性约束下的期望响应：若损失不会因输入小幅移动而剧变，就应让这种敏感性进入界。由于$|f(x)|\leq|f(x_0)|+Ld(x,x_0)$，两边期望均有限。
3. 指数矩约束下的期望响应：有些损失没有统一上界，也难以给出输入空间的敏感常数，但在参考分布下可控制其尾部。证明的关键是指数倾斜：按$e^f$重新加权参考分布，使较大函数值获得更多质量。

#### 2.4.1 有界函数的期望响应

主要内容：设固定可测损失$f$取值于$[0,1]$。逐点恒等式$f(x)=\int_0^1\mathbb I\{f(x)>t\}\,\mathrm dt$与Tonelli定理给出$|\mathbb E_Pf-\mathbb E_Qf| \leq\int_0^1|P(f>t)-Q(f>t)|\,\mathrm dt \leq d_{\mathrm{TV}}(P,Q)$这也说明事件概率控制为何足以控制所有这一范围内的损失。

论证与表述逻辑：

1. 对罕见失败事件，除了TV的加性误差，还可以利用似然比高阶矩。设$P\ll Q$、$L=\mathrm dP/\mathrm dQ$，并且某个$\alpha>1$满足$D_\alpha(P\Vert Q)<\infty$。
2. 有界性不能只在常见样本上成立。取$Q=\delta_0$、$P_\varepsilon=(1-\varepsilon)\delta_0+ \varepsilon\delta_{1/\varepsilon}$，对无界函数$f(x)=x$，TV为$\varepsilon$，期望差却恒为$1$。

#### 2.4.2 敏感性约束下的期望响应

主要内容：若损失不会因输入小幅移动而剧变，就应让这种敏感性进入界。由于$|f(x)|\leq|f(x_0)|+Ld(x,x_0)$，两边期望均有限。

论证与表述逻辑：

1. 对$\delta_0,\delta_\varepsilon$，其中$\varepsilon>0$，均值函数$f(x)=x$的变化恰为$\varepsilon=W_1$，事件函数$g(x)=\mathbb I\{x>0\}$的变化却为$1$。
2. MMD提供另一种敏感性约束。若同一损失$f$属于核$k$的RKHS$\mathcal H_k$，且核均值存在，则再生性质和Cauchy--Schwarz不等式给出$|\mathbb E_Pf-\mathbb E_Qf| =|\langle f,\boldsymbol\mu_P-\boldsymbol\mu_Q\rangle_{\mathcal H_k}| \leq\|f\|_{\mathcal H_k}\operatorname{MMD}_k(P,Q)$下标$k$显式标明这里沿用的核空间和MMD。

#### 2.4.3 指数矩约束下的期望响应

主要内容：有些损失没有统一上界，也难以给出输入空间的敏感常数，但在参考分布下可控制其尾部。证明的关键是指数倾斜：按$e^f$重新加权参考分布，使较大函数值获得更多质量。

论证与表述逻辑：

1. 命题（Donsker--Varadhan变分表达）：对每个有界可测实函数$f$，$D_{\mathrm{KL}}(P\Vert Q) \geq\mathbb E_Pf-\log\mathbb E_Qe^f$而且在扩展实数意义下，$D_{\mathrm{KL}}(P\Vert Q) =\sup_{f\ \text{有界可测}}\{\mathbb E_Pf-\log\mathbb E_Qe^f\}$。
2. 推导：给定有界$f$，令$Z_f=\mathbb E_Qe^f$，并定义$\frac{\mathrm dQ_f}{\mathrm dQ}=\frac{e^f}{Z_f}$因$0<Z_f<\infty$，且密度比严格正，$Q_f$与$Q$等价。若$D_{\mathrm{KL}}(P\Vert Q)<\infty$，对数密度比可积，乘法法则给出完整的倾斜恒等式$\begin{aligned} D_{\mathrm{KL}}(P\Vert Q_f) &=\mathbb E_P\left[\log\frac{\mathrm dP}{\mathrm dQ}-f+\log Z_f\right]\\ &=D_{\mathrm{KL}}(P\Vert Q)-\mathbb E_Pf+\log Z_f \end{aligned}$左侧非负即得下界；若原KL无限，右侧有限，下界仍成立。
3. 现在令$g$允许无界。假设$P\ll Q$、$g\in L^1(P)$，并且对所选$\lambda>0$有$\mathbb E_Qe^{\lambda g}<\infty$。

### 2.5 概率分布的优化

主要内容：将分布作为待选对象，讨论目标与矩约束下的选择、表示受限的逼近，以及固定边缘下的最优耦合。

论证与表述逻辑：

1. 目标约束下的分布选择：为了得到一张新的概率规律，可以规定平均收益，并限制它偏离参考分布的程度；也可以只给出均值等矩条件，在相容规律中最大化熵。
2. 表示约束下的分布逼近：联合模型和观测可以确定一张后验分布，但归一化积分难以计算时，精确表示和采样仍可能不可行。我们把未知量改成可计算候选族中的密度$q$，以它逼近已经确定的后验。
3. 边缘约束下的分布耦合：把两个固定边缘$P,Q$配成联合分布时，可以有许多不同的配对。未知量是$\gamma\in\Pi(P,Q)$，每个候选都须保留这两个边缘。

#### 2.5.1 目标约束下的分布选择

主要内容：为了得到一张新的概率规律，可以规定平均收益，并限制它偏离参考分布的程度；也可以只给出均值等矩条件，在相容规律中最大化熵。

论证与表述逻辑：

1. 参考分布下的收益与偏离权衡：设$P_0$是可以采样的参考规律，$f$为有界可测收益。只追求最大收益可能把质量全部集中到极少数点；同时扣除偏离参考规律的KL，就得到下面的分布优化。
2. 矩约束下的最大熵选择：若只知道均值或协方差，没有指定收益函数，哪些分布与这些信息相容？最大熵原理（maximum entropy principle）在相容分布中选择熵最大的一个。

##### 2.5.1.1 参考分布下的收益与偏离权衡

主要内容：设$P_0$是可以采样的参考规律，$f$为有界可测收益。只追求最大收益可能把质量全部集中到极少数点；同时扣除偏离参考规律的KL，就得到下面的分布优化。

论证与表述逻辑：

1. 命题（Gibbs变分式）：对有界可测$f$，$\log\mathbb E_{P_0}e^f =\sup_{Q\ll P_0}\{\mathbb E_Qf-D_{\mathrm{KL}}(Q\Vert P_0)\}$KL无限时目标约定为$-\infty$，唯一最优分布为$\frac{\mathrm dQ^\star}{\mathrm dP_0} =\frac{e^f}{Z_f},\qquad Z_f=\mathbb E_{P_0}e^f$。
2. 推导：有界性保证$0<Z_f<\infty$，且$Q^\star$与$P_0$等价。对任何有限KL的$Q\ll P_0$，$\log\frac{\mathrm dQ}{\mathrm dQ^\star} =\log\frac{\mathrm dQ}{\mathrm dP_0}-f+\log Z_f$各项在$Q$下可积，故倾斜恒等式给出$\mathbb E_Qf-D_{\mathrm{KL}}(Q\Vert P_0) =\log Z_f-D_{\mathrm{KL}}(Q\Vert Q^\star)\leq\log Z_f$无限KL候选的目标已为$-\infty$。对$Q^\star$，$\log(\mathrm dQ^\star/\mathrm dP_0)=f-\log Z_f$有界，所以自身收益与KL都有限，可以直接代入取到等号。
3. 对有界收益$r$加入温度$\beta>0$，令$f=r/\beta$，可得$\sup_{Q\ll P_0}\{\mathbb E_Qr-\beta D_{\mathrm{KL}}(Q\Vert P_0)\} =\beta\log\mathbb E_{P_0}e^{r/\beta},\qquad Q^\star\propto P_0e^{r/\beta}$较小温度更偏向高收益区域，也可能使重要性权重集中、采样方差增大。

##### 2.5.1.2 矩约束下的最大熵选择

主要内容：若只知道均值或协方差，没有指定收益函数，哪些分布与这些信息相容？最大熵原理（maximum entropy principle）在相容分布中选择熵最大的一个。

论证与表述逻辑：

1. 命题（有限配置上的配分函数与最大熵对偶）：设$D$为有限非空配置集，$\boldsymbol T:D\to\mathbb R^m$，基准权重恒为$1$。定义$A(\boldsymbol\theta)=\log\sum_{z\in D}e^{\langle\boldsymbol\theta,\boldsymbol T(z)\rangle}, \qquad\mathcal M=\operatorname{conv}\{\boldsymbol T(z):z\in D\}$对$\boldsymbol\mu\in\mathcal M$，令$H^\star(\boldsymbol\mu)=\max_{q:\,\mathbb E_q\boldsymbol T=\boldsymbol\mu}H(q),$其中$q$遍历$D$上的全部概率质量函数。则在整个$\mathcal M$上有$A^\star(\boldsymbol\mu)=-H^\star(\boldsymbol\mu)$，在外部有$A^\star=+\infty$，且$A(\boldsymbol\theta)=\max_{\boldsymbol\mu\in\mathcal M} \{\langle\boldsymbol\theta,\boldsymbol\mu\rangle+H^\star(\boldsymbol\mu)\}$。
2. 推导：有限概率单纯形紧；给定可行均值后的约束闭且非空，熵在单纯形上连续，因此每个$H^\star(\boldsymbol\mu)$都能达到。对任意质量函数$q$，展开有限KL得到$\langle\boldsymbol\theta,\mathbb E_q\boldsymbol T\rangle+H(q) =A(\boldsymbol\theta)-D_{\mathrm{KL}}(q\Vert p_{\boldsymbol\theta}) \leq A(\boldsymbol\theta),$且在$q=p_{\boldsymbol\theta}$处取等号。
3. 在$\{0,1,2\}$上要求$\mathbb EX=1/2$时，最大熵分布为$p_j=t^j/(1+t+t^2)$。

#### 2.5.2 表示约束下的分布逼近

主要内容：联合模型和观测可以确定一张后验分布，但归一化积分难以计算时，精确表示和采样仍可能不可行。我们把未知量改成可计算候选族中的密度$q$，以它逼近已经确定的后验。

论证与表述逻辑：

1. 定义（证据下界）：若$q\ll\pi$且$D_{\mathrm{KL}}(q\Vert\pi)<\infty$，定义证据下界（evidence lower bound, ELBO）为$\mathcal L(q,\boldsymbol\theta;x) =\mathbb E_q\log\frac{p_{\boldsymbol\theta}(x,Z)}{q(Z)}$按对数比整体取期望，不要求$\mathbb E_q\log p_{\boldsymbol\theta}(x,Z)$与$\mathbb E_q\log q(Z)$各自有限。
2. 有限KL保证上述整体对数比可积，因为它等于$\log p_{\boldsymbol\theta}(x)-\log(q/\pi)$。
3. 等价地，先在$K$个位置中均匀选正样本位置$J$，令该位置与$X$按目标联合分布配对，其余位置仍为独立边缘样本。

#### 2.5.3 边缘约束下的分布耦合

主要内容：把两个固定边缘$P,Q$配成联合分布时，可以有许多不同的配对。未知量是$\gamma\in\Pi(P,Q)$，每个候选都须保留这两个边缘。

论证与表述逻辑：

1. 边缘约束下的最优耦合存在：一般空间中的测度序列可能把质量送往越来越远处，存在性证明因而需要排除质量逃逸。在当前耦合问题中，固定边缘的紧性将给出对全部可行耦合统一适用的紧集。
2. 有限空间下的最优耦合求解：设来源点为$x_i$、目标点为$y_j$，概率向量为$\boldsymbol p,\boldsymbol q$，各成本$c_{i,j}$有限且非负。

##### 2.5.3.1 边缘约束下的最优耦合存在

主要内容：一般空间中的测度序列可能把质量送往越来越远处，存在性证明因而需要排除质量逃逸。在当前耦合问题中，固定边缘的紧性将给出对全部可行耦合统一适用的紧集。

论证与表述逻辑：

1. 命题（最优耦合存在）：设$\mathcal X,\mathcal Y$为Polish空间，$P,Q$为其Borel概率测度。若成本$c:\mathcal X\times\mathcal Y\to[0,\infty]$下半连续，且至少有一个$\gamma_0\in\Pi(P,Q)$满足$\int c\,\mathrm d\gamma_0<\infty$，则存在有限成本耦合$\gamma^\star$达到$\mathcal T_c(P,Q)=\inf_{\gamma\in\Pi(P,Q)}\int c\,\mathrm d\gamma$。
2. 推导：可行集合非空，且成本非负、有有限可行值，所以最优下确界有限。取近最优序列$\gamma_n\in\Pi(P,Q)$，使$\int c\,\mathrm d\gamma_n\to\mathcal T_c(P,Q)$。
3. 最后一步的积分测度随$k$改变，不能用固定测度下的Fatou引理直接替代。非负性避免成本的负部失控，下半连续性保证极限不会突然增加成本；若修改这些假设，需要另给能实现同样作用的条件。

##### 2.5.3.2 有限空间下的最优耦合求解

主要内容：设来源点为$x_i$、目标点为$y_j$，概率向量为$\boldsymbol p,\boldsymbol q$，各成本$c_{i,j}$有限且非负。

论证与表述逻辑：

1. 把有限搬运视为线性规划，并为两组边缘约束引入势函数$u_i,v_j$，保留$\gamma_{i,j}\geq0$作为取下确界的定义域：$\mathcal L(\boldsymbol\gamma,\boldsymbol u,\boldsymbol v) &=\sum_{i,j}c_{i,j}\gamma_{i,j} +\sum_i u_i\left(p_i-\sum_j\gamma_{i,j}\right) +\sum_j v_j\left(q_j-\sum_i\gamma_{i,j}\right)\notag\\ &=\sum_i u_ip_i+\sum_jv_jq_j +\sum_{i,j}(c_{i,j}-u_i-v_j)\gamma_{i,j}$如果某个系数$c_{i,j}-u_i-v_j<0$，将对应非负变量趋向无穷，Lagrangian下确界就是$-\infty$。
2. 取来源和目标位置均为$0,2$，令$\boldsymbol p=(3/4,1/4)$、$\boldsymbol q=(1/4,3/4)$，$c_{i,j}=|x_i-y_j|$。

### 2.6 参数化分布的迭代优化

主要内容：用参数变化诱导的分布距离建立局部几何，说明基于分布几何的参数更新及其可行条件。

论证与表述逻辑：

1. 参数变化下的分布距离：改变参数值通常会改变分布；更换表示同一分布的坐标则不应该改变几何对象。先分析前一种真实扰动，再检查后一种坐标变化。
2. 基于分布几何的参数更新：有了局部长度和目标微分，就可以确定在给定分布变化预算内怎样下降。这仍是原优化任务的局部求解步骤：若参数表示有约束，应在相应可行切空间中求解，或结合约束优化和回缩；Fisher矩阵本身不会自动保持矩与固定边缘。

#### 2.6.1 参数变化下的分布距离

主要内容：改变参数值通常会改变分布；更换表示同一分布的坐标则不应该改变几何对象。先分析前一种真实扰动，再检查后一种坐标变化。

论证与表述逻辑：

1. 小参数变化下的分布差异：设参数域$\Theta\subseteq\mathbb R^d$，共同参考测度为$\mu$。固定内点$\boldsymbol\theta$，假设存在开邻域$U$和共同可测支持$S$，使所有$\boldsymbol\eta\in U$都在$S$上满足$p_{\boldsymbol\eta}>0$，在外部为零。 命题（KL的局部二阶展开）：在上述共同支持、交换微分及可积条件下，进一步设$U$可取为凸集，且对$P_{\boldsymbol\theta}$-几乎处处的$x$，$\nabla^2_{\boldsymbol\eta}\log p_{\boldsymbol\eta}(x)$在$\boldsymbol\theta$处连续。假设存在$M\in L^1(P_{\boldsymbol\theta})$，使$\sup_{\boldsymbol\eta\in U} \|\nabla^2_{\boldsymbol\eta}\log p_{\boldsymbol\eta}(x)\|_{\mathrm{op}}\leq M(x)$几乎处处成立。则当$\boldsymbol\delta\to\boldsymbol0$且$\boldsymbol\theta+\boldsymbol\delta\in U$时，$D_{\mathrm{KL}}(P_{\boldsymbol\theta}\Vert P_{\boldsymbol\theta+\boldsymbol\delta}) =\tfrac12\boldsymbol\delta^\top\boldsymbol F(\boldsymbol\theta)\boldsymbol\delta +o(\|\boldsymbol\delta\|_2^2)$。
2. 重参数化下的几何保持：令$\boldsymbol\theta=\boldsymbol\theta(\boldsymbol\phi)$为光滑局部可逆坐标变换，Jacobian为$\boldsymbol J=\partial\boldsymbol\theta/\partial\boldsymbol\phi$。 另一个常见混淆发生在样本矩阵与模型期望之间。固定输入分布$d$，取条件高斯$Y\mid\boldsymbol X=\boldsymbol x\sim\mathcal N(\boldsymbol\theta^\top\boldsymbol x,\sigma^2)$，其中$\sigma>0$已知，$\mathbb E_d\|\boldsymbol X\|^2<\infty$。

#### 2.6.2 基于分布几何的参数更新

主要内容：有了局部长度和目标微分，就可以确定在给定分布变化预算内怎样下降。这仍是原优化任务的局部求解步骤：若参数表示有约束，应在相应可行切空间中求解，或结合约束优化和回缩；Fisher矩阵本身不会自动保持矩与固定边缘。

论证与表述逻辑：

1. 分布变化约束下的自然梯度：设目标$L(\boldsymbol\theta)$可微，$\boldsymbol g=\nabla L(\boldsymbol\theta)$，且$\boldsymbol F(\boldsymbol\theta)$正定。 保持的是无穷小方向，不是任意有限离散步。
2. 奇异与近似条件下的几何更新：参数冗余、退化坐标或不足的输入方向都可能使Fisher奇异。因而不能把所有零方向都理解成有限移动后分布完全不变。 经验Fisher、分块或对角近似可能降低计算量，却分别引入抽样、模型期望或跨块相关性的近似。即使每个近似矩阵都正定，也只说明定义了某种局部内积，不说明它等于真实分布Fisher，更不保证同样的坐标保持结论。

### 2.7 样本评价的总体误差

主要内容：分析模型选择与评价共用样本产生的偏差，分别建立平均偏差与同时风险控制所需的信息条件。

论证与表述逻辑：

1. 从同一批训练样本中挑选样本损失最小的模型，再报告它的样本损失，可能偏向这批记录中的偶然低值。问题不在于总体分布改变，而在于模型选择与评价共享样本。
2. 前面的工具提供两条分析路径。比较真实联合规律与解除依赖的边缘乘积，可以控制平均评价偏差；建立同时覆盖全部候选分布的概率事件，则允许看过样本以后选择候选。

#### 2.7.1 数据依赖下的平均评价偏差

主要内容：设可测损失$\ell(w,Z)\in[0,1]$，新样本$Z$服从与训练样本相同的总体规律，定义$\begin{aligned} R(w)&=\mathbb E_Z\ell(w,Z),& \widehat R_S(w)&=\frac1n\sum_{i=1}^n\ell(w,Z_i),\\ g(S,w)&=R(w)-\widehat R_S(w) \end{aligned}$固定$w$时，$\mathbb E_Sg(S,w)=0$。

论证与表述逻辑：

1. 例如算法只能输出$M$种预测器，则$I(S;W)\leq H(W)\leq\log M$，平均偏差至多$\sqrt{\log M/(2n)}$。

#### 2.7.2 数据依赖下的同时风险控制

主要内容：有时学习规则报告的是候选模型上的一张分布$Q_S$，评价量便是按这张分布平均的总体风险。为了覆盖根据样本作出的选择，我们先建立对全部允许候选分布同时成立的事件。

论证与表述逻辑：

1. 命题（固定参数的基础PAC--Bayes界）：在上述独立同分布样本和$[0,1]$损失设定下，令$P_0$在观察$S$前固定，且与$S$独立。对任意预先固定的$\lambda>0$与$0<\delta<1$，以至少$1-\delta$的概率，同时对所有$Q\ll P_0$有$\mathbb E_QR(w) \leq\mathbb E_Q\widehat R_S(w) +\frac{D_{\mathrm{KL}}(Q\Vert P_0)+\log(1/\delta)}{\lambda} +\frac{\lambda}{8n}$KL无限时将右侧解释为无限。
2. 推导：对每个固定$w$，Hoeffding引理给出$\mathbb E_Se^{\lambda(R(w)-\widehat R_S(w))} \leq e^{\lambda^2/(8n)}$。先验独立于样本，Tonelli定理允许对同一个$P_0$平均：$\mathbb E_S\mathbb E_{w\sim P_0} e^{\lambda(R(w)-\widehat R_S(w))} \leq e^{\lambda^2/(8n)}$由Markov不等式，事件$\mathcal E= \left\{S:\mathbb E_{P_0}e^{\lambda(R-\widehat R_S)} \leq\frac{e^{\lambda^2/(8n)}}{\delta}\right\}$满足$P_S(\mathcal E)\geq1-\delta$。对任意固定在这个事件内的样本，实现后的函数$f(w)=\lambda(R(w)-\widehat R_S(w))$有界。
3. “固定$\lambda$”是事件成立的条件。观察数据后逐个候选优化右侧的$\lambda$，或根据同一评价样本重选先验，都超出了上述事件。

### 2.8 本章小结

主要内容：区分码长、分布差异、依赖和预测损失，说明这些量怎样支持区分下界、分布优化与学习风险分析。

论证与表述逻辑：

1. 报警概率差、平均预测损失和记录所需的码长不能用同一个数字替代。熵回答一张规律下平均需要描述多少信息，条件熵记录已有观测后剩余的部分；比较真实规律与预测规律的对数评分，多出的代价由KL给出。
2. 两张分布是否接近，取决于关注的量。事件概率、核函数期望和质量位移给出不同尺度；同均值可以隐藏差异，小位移也可以跨过阈值。
3. 选择一张分布、逼近一张既定分布与配对两个固定边缘，改变的是不同未知量。收益与偏离权衡给出指数倾斜，矩约束选择相容的最大熵规律，受限表示留下后验逼近误差，耦合优化保留两侧边缘。
4. 样本评价要额外检查模型选择怎样使用这批样本。互信息控制平均有符号评价偏差，固定先验和调节参数$\lambda$下的PAC--Bayes界控制同时覆盖候选分布的事件；平均保证不能替代高概率保证。

## 第3章 因果响应

正文：[03-causal-response-and-structure.tex](../../tex/02-mathematical-preliminaries-lower/01-random-variables-distributions-and-causality/03-causal-response-and-structure.tex)。

### 3.1 因果响应的表示

主要内容：从处理、背景与结果的生成建立响应映射和潜在结果，说明观测条件均值与主动干预的区别及连接条件。

论证与表述逻辑：

1. 原因与背景的响应表示：比较同一人的行动后果时，需要固定两种行动共同具有的背景。用$t$记处理值，用$\boldsymbol u$记这些背景因素，例如既有能力与未测量因素；可见协变量只可能记录其中一部分。
2. 机制干预下的潜在结果：在二元例子中，行动直接把$T=U$换成$T=t$，并沿用原来的结果规则。这项替换就是机制干预：它规定处理如何产生，再让保留的规则使用新的处理值。
3. 观测结果与干预响应的连接：一名接受培训的人的实际成绩，能否作为$Y(1)$的记录，取决于潜在结果所指的培训方案是否与实际执行一致。不同课程、时长和测量日期会给出不同的结果变量；先把这些条件固定，才能把记录接到相应的潜在结果上。

#### 3.1.1 原因与背景的响应表示

主要内容：比较同一人的行动后果时，需要固定两种行动共同具有的背景。用$t$记处理值，用$\boldsymbol u$记这些背景因素，例如既有能力与未测量因素；可见协变量只可能记录其中一部分。

论证与表述逻辑：

1. 定义（因果响应与自然、行动映射）：给定背景可测空间$(\mathcal U,\mathscr U)$及概率测度$P_{\boldsymbol U}$，自然变量的可测状态空间$\mathcal V$，以及可测的处理空间$\mathcal T$和结果空间$\mathcal Y$。状态空间包含处理、结果及其他内生坐标，并配有可测坐标映射$\pi_T:\mathcal V\to\mathcal T$、$\pi_Y:\mathcal V\to\mathcal Y$。固定模型$M$提供唯一值的可测自然映射$F_M:\mathcal U\to\mathcal V$，以及每个允许行动$a$的唯一值可测映射$F_M^a:\mathcal U\to\mathcal V$。若$a(t)$表示将处理生成规则替换为常量$t$的允许行动，即$\pi_T(F_M^{a(t)}(\boldsymbol u))=t$，则因果响应（causal response）是映射$R_M:\mathcal T\times\mathcal U\longrightarrow\mathcal Y, \qquad R_M(t,\boldsymbol u)=\pi_Y\bigl(F_M^{a(t)}(\boldsymbol u)\bigr)$本章要求$R_M$对乘积可测结构可测。自然变量为$\boldsymbol V=F_M(\boldsymbol U)$，行动后的变量为$\boldsymbol V_a=F_M^a(\boldsymbol U)$。
2. 固定$\boldsymbol u$时，$t\mapsto R_M(t,\boldsymbol u)$回答同一单位怎样响应不同处理；让$\boldsymbol U$按$P_{\boldsymbol U}$变化，才得到总体响应分布。
3. 下面用两套二元机制计算这一区别。设背景满足$U\sim\operatorname{Bernoulli}(1/2)$处理与结果均取$0,1$。

#### 3.1.2 机制干预下的潜在结果

主要内容：在二元例子中，行动直接把$T=U$换成$T=t$，并沿用原来的结果规则。这项替换就是机制干预：它规定处理如何产生，再让保留的规则使用新的处理值。

论证与表述逻辑：

1. 定义（潜在结果）：对明确的目标总体、处理版本和结果测量时间，潜在结果（potential outcome）是随机变量$Y(t)=R_M(t,\boldsymbol U)$对二元处理，$(Y(0),Y(1))$定义在同一背景概率空间上；两项分别表示同一单位在两种处理下的结果，而不是分别抽取两个人。
2. 观察条件分布$p(y\mid T=t)$会筛选自然规则恰好给出处理$t$的单位，因而同时包含处理作用和进入处理组的选择。
3. 固定处理值并非唯一行动。随机干预（stochastic intervention）用新的随机规则替换处理规则，例如给定处理前信息$X=x$时，按概率核$q(\cdot\mid x)$安排培训。

#### 3.1.3 观测结果与干预响应的连接

主要内容：一名接受培训的人的实际成绩，能否作为$Y(1)$的记录，取决于潜在结果所指的培训方案是否与实际执行一致。不同课程、时长和测量日期会给出不同的结果变量；先把这些条件固定，才能把记录接到相应的潜在结果上。

论证与表述逻辑：

1. 定义（处理一致性与无干扰）：对明确的处理版本，一致性（consistency）要求实际处理对应的结果满足$Y=Y(T)$几乎必然成立；特别地，$\begin{gathered} T=t\Longrightarrow Y=Y(t),\\ \text{二元处理时，}\quad Y=TY(1)+(1-T)Y(0). \end{gathered}$对$n$个单位，无干扰要求：每个$i$及任意两个处理向量$\boldsymbol t,\boldsymbol t'$，只要$t_i=t_i'$，就有$Y_i(\boldsymbol t)=Y_i(\boldsymbol t')$几乎必然成立。因此单位$i$的潜在结果才可简记为$Y_i(t_i)$。
2. 一致性连接自然记录与行动响应，没有把未采取行动的结果变成可见记录。若模型给出自然处理$T=F_{M,T}(\boldsymbol U)$，这一条件要求自然结果与$R_M(F_{M,T}(\boldsymbol U),\boldsymbol U)$相合；不能任意拼接不相容的自然函数与响应族。
3. 通常所说的稳定单位处理值假设把处理版本唯一性和无干扰合在一起。即使处理版本清楚且单位互不干扰，主动选择培训的人也可能具有不同背景。

### 3.2 因果响应的比较与变化

主要内容：固定处理版本与总体，分别比较个体、总体和分布层面的响应，再研究连续处理的小幅变化。

论证与表述逻辑：

1. 同一背景下的响应比较：已经给定$R_M$时，计算同一人的两种结果只改变处理值$t$，背景$\boldsymbol u$保持不动。对实值成绩，可以直接相减；所得差值刻画这一背景下的处理作用，而不是两名不同人的成绩差。
2. 背景总体下的响应比较：如果目标是决定一项培训是否适用于指定人群，两项行动都应按目标人群的同一个背景分布平均。这样得到的是总体作用，允许不同背景的个体效应互相抵消。
3. 连续处理下的局部响应变化：二元处理适合比较有无行动；连续剂量还可以询问“在当前剂量附近再增加一点会怎样”。局部线性近似把小输入增量的响应写成线性主部与高阶余项；这里用它描述固定模型、固定背景下的响应变化，而不是观测人群随剂量改变产生的回归变化。

#### 3.2.1 同一背景下的响应比较

主要内容：已经给定$R_M$时，计算同一人的两种结果只改变处理值$t$，背景$\boldsymbol u$保持不动。对实值成绩，可以直接相减；所得差值刻画这一背景下的处理作用，而不是两名不同人的成绩差。

论证与表述逻辑：

1. 定义（同一背景下的响应差）：对实值结果及允许的处理值$t,t'$，固定背景$\boldsymbol u$的响应差定义为$\Delta_M(t,t';\boldsymbol u)=R_M(t,\boldsymbol u)-R_M(t',\boldsymbol u)$二元处理的个体处理效应（individual treatment effect）是随机变量$Y(1)-Y(0)=\Delta_M(1,0;\boldsymbol U)$。
2. 给定模型和背景时，两个响应都可以计算。但每个单位的实际记录只能包含$Y(T)$，不会同时包含同一时刻的$Y(1)$与$Y(0)$。
3. 对向量结果，可以先报告各坐标差，也可以指定具有实质含义的效用函数$h:\mathcal Y\to\mathbb R$，比较$h(R_M(t,\boldsymbol u))-h(R_M(t',\boldsymbol u))$。

#### 3.2.2 背景总体下的响应比较

主要内容：如果目标是决定一项培训是否适用于指定人群，两项行动都应按目标人群的同一个背景分布平均。这样得到的是总体作用，允许不同背景的个体效应互相抵消。

论证与表述逻辑：

1. 总体与条件总体的平均响应比较：对二元处理，假设$Y(0),Y(1)$都可积，平均处理效应（average treatment effect, ATE）定义为$\tau = \mathbb E[Y\mid\operatorname{do}(T=1)] - \mathbb E[Y\mid\operatorname{do}(T=0)]$。
2. 干预结果的分布响应比较：平均值只记录分布的一个特征。设$U$等概率取$-1,1$，$Y(0)=0,Y(1)=U$，则ATE为零，但处理后从人人得到零变成两种相反结果。

##### 3.2.2.1 总体与条件总体的平均响应比较

主要内容：对二元处理，假设$Y(0),Y(1)$都可积，平均处理效应（average treatment effect, ATE）定义为$\tau = \mathbb E[Y\mid\operatorname{do}(T=1)] - \mathbb E[Y\mid\operatorname{do}(T=0)]$。

论证与表述逻辑：

1. 定义（平均处理效应）：对二元处理，假设$Y(0),Y(1)$都可积，平均处理效应（average treatment effect, ATE）定义为$\tau = \mathbb E[Y\mid\operatorname{do}(T=1)] - \mathbb E[Y\mid\operatorname{do}(T=0)]$。
2. 两个干预总体使用同一个$P_{\boldsymbol U}$。由潜在结果与干预分布的对应关系及期望线性性，$\tau =\mathbb E[Y(1)-Y(0)] =\mathbb E[Y(1)]-\mathbb E[Y(0)]$可积性排除了$\infty-\infty$这样的未定义运算。
3. 定义（条件平均处理效应）：设$X$在所比较干预下保持同一取值与含义，且两种潜在结果可积。条件平均处理效应（conditional average treatment effect, CATE）是$\tau(x)=\mathbb E[Y(1)-Y(0)\mid X=x], \qquad P_X\text{几乎处处}$。
4. 对有限处理集合$\mathcal T$，同样定义$\tau(t,t')=\mathbb E[Y(t)-Y(t')]$若行动由处理前信息决定，则要比较整个策略。

##### 3.2.2.2 干预结果的分布响应比较

主要内容：平均值只记录分布的一个特征。设$U$等概率取$-1,1$，$Y(0)=0,Y(1)=U$，则ATE为零，但处理后从人人得到零变成两种相反结果。

论证与表述逻辑：

1. 对实值结果，定义干预分布函数与其广义分位数$F_t(y)=\mathbb P(Y(t)\leq y),\qquad Q_t(p)=\inf\{y:F_t(y)\geq p\},\quad 0<p<1$$F_t(y)-F_{t'}(y)$比较不高于阈值的概率，$Q_t(p)-Q_{t'}(p)$比较两个总体处于同一分位位置的结果。
2. 总变差比较事件概率而不要求矩；采用$p$阶Wasserstein距离时应满足所用空间和有限$p$阶矩条件；使用KL散度则须检查绝对连续性及其值是否有限。
3. 两个干预边缘即使完全已知，仍没有说明它们如何在同一背景上配对。

#### 3.2.3 连续处理下的局部响应变化

主要内容：二元处理适合比较有无行动；连续剂量还可以询问“在当前剂量附近再增加一点会怎样”。局部线性近似把小输入增量的响应写成线性主部与高阶余项；这里用它描述固定模型、固定背景下的响应变化，而不是观测人群随剂量改变产生的回归变化。

论证与表述逻辑：

1. 命题（平均响应的求导）：设$I$是包含$t_0$的开区间，$R_M(t_0,\boldsymbol U)$可积。若对几乎每个$\boldsymbol u$，$R_M(\cdot,\boldsymbol u)$在$I$可微，且存在非负可积函数$g(\boldsymbol U)$，使$|\partial_tR_M(t,\boldsymbol u)|\leq g(\boldsymbol u), \qquad t\in I,$则$m$在$t_0$可微，且$m'(t_0)=\mathbb E[\partial_tR_M(t_0,\boldsymbol U)]$。
2. 推导：对足够小的非零$h$，中值定理给出$\left| \frac{R_M(t_0+h,\boldsymbol u)-R_M(t_0,\boldsymbol u)}{h} \right|\leq g(\boldsymbol u)$因而$R_M(t_0+h,\boldsymbol U)$可积，且差商几乎处处收敛到$\partial_tR_M(t_0,\boldsymbol U)$。可积的$g$统一控制这些差商，支配收敛定理允许将极限移入期望，得到$\lim_{h\to0}\frac{m(t_0+h)-m(t_0)}{h} = \mathbb E\!\left[ \lim_{h\to0} \frac{R_M(t_0+h,\boldsymbol U)-R_M(t_0,\boldsymbol U)}{h} \right],$即所述结论。
3. 局部响应导数也不等于观测回归斜率$\partial_t\mathbb E[Y\mid T=t,X=x]$。因此模型的光滑性支持局部计算，却不同时保证这个导数能由观测识别或能外推到大幅行动。

### 3.3 给定事实后的因果响应

主要内容：得到个体事实后先更新背景条件分布，再在同一背景下改变行动，说明反事实、行动补救与公平补救的计算。

论证与表述逻辑：

1. 事实条件下的反事实计算：给定事实$\boldsymbol E=\boldsymbol e$，所求对象是这个单位在替代行动下的条件结果。
2. 目标约束下的行动补救：反事实计算还可以反过来服务于行动选择：怎样以尽量低的代价，让同一个人的决策达到目标？先区分两种看似相近的操作。
3. 目标属性干预下的公平补救：设行动已经能改变当前决策，我们还可能要求这种成功不依赖某项受保护属性。检验这一要求，需要在同一背景下替换属性，并重新计算属性改变所影响的其他变量。

#### 3.3.1 事实条件下的反事实计算

主要内容：给定事实$\boldsymbol E=\boldsymbol e$，所求对象是这个单位在替代行动下的条件结果。

论证与表述逻辑：

1. 定义（给定响应模型的反事实变量）：在同一外生背景$\boldsymbol U$上，反事实（counterfactual）变量定义为$\boldsymbol V_a=F_M^a(\boldsymbol U)$。给定实际证据$\boldsymbol E$后的反事实分布是$\boldsymbol V_a$关于该证据的条件分布，而不是重新按背景总体抽取一个人。
2. 事实证据可来自自然变量的一部分，也可包括带噪测量；后一情形把测量随机性一并纳入背景，使证据的生成规则明确。反事实计算通常称为“溯因、干预、预测”：溯因由事实得到背景条件分布，干预切换到允许的行动映射，预测将同一个背景条件分布推到结果空间。
3. 两套配对连完整随机试验的两组边缘也无法区分。要回答条件个体反事实，还需要关于跨世界联合结构的机制限制，或具有适当稳定性、时间和携带效应假设的重复干预资料；否则应保留相容范围。

#### 3.3.2 目标约束下的行动补救

主要内容：反事实计算还可以反过来服务于行动选择：怎样以尽量低的代价，让同一个人的决策达到目标？先区分两种看似相近的操作。

论证与表述逻辑：

1. 定义（因果行动补救）：给定事实证据$\boldsymbol E=\boldsymbol e$，以$x=\xi(\boldsymbol e)$表示由事实确定的行动信息摘要，其中$\xi$为预先指定的可测映射。给定可实施行动集合$\mathcal A(x)$、响应模型、行动成本$c(a;x)$与目标决策集合$G$，行动补救（algorithmic recourse）寻找能够使行动后的决策落入$G$的可行行动。因果行动补救用同一背景下的干预状态$\boldsymbol V_a=F_M^a(\boldsymbol U)$评价成功条件，并按机制重算所有受行动影响的状态。
2. 多数事实只能给出背景条件分布。给定可容许失败概率$\alpha\in[0,1]$，可以采用概率型约束$\mathbb P\bigl(d(F_M^a(\boldsymbol U))\in G\mid\boldsymbol E=\boldsymbol e\bigr) \geq1-\alpha$若背景空间为Polish空间，且所用条件分布版本是其Borel概率测度，支持由每个开邻域都有正条件概率的背景点组成。
3. 补救也有时间和多人联动的边界。许多人同时接受建议可能改变价格、名额或审核规则；决策系统更新后，原建议未必仍有效；资源竞争也可能使原先逐人可行的行动无法共同执行。

#### 3.3.3 目标属性干预下的公平补救

主要内容：设行动已经能改变当前决策，我们还可能要求这种成功不依赖某项受保护属性。检验这一要求，需要在同一背景下替换属性，并重新计算属性改变所影响的其他变量。

论证与表述逻辑：

1. 定义（反事实公平）：在给定响应模型与预测规则下，反事实公平（counterfactual fairness）要求：对每个允许的替代属性$a'$和每个可测预测值集合$B$，以下等式对事实证据分布几乎处处的$(x,a)$成立：$\begin{aligned} &\mathbb P(\widehat Y_{A\leftarrow a}\in B\mid X=x,A=a)\\ &\qquad= \mathbb P(\widehat Y_{A\leftarrow a'}\in B\mid X=x,A=a) \end{aligned}$两个属性世界均使用同一个事实背景条件分布，并重新计算由属性影响的状态及预测。
2. 等式右侧仍以事实$A=a$为条件，而不是改用另一群人的证据$A=a'$。属性干预在这里是明确模型下的比较操作，也不表示应建议个人改变该属性。
3. 若多个模型与证据相容，应在该模型类上报告结论范围。哪些属性或路径属于不应进入决策的因素，则是另需论证的规范选择。

### 3.4 因果响应的推断

主要内容：在与观测和机制假设相容的模型中检查响应是否唯一，区分点识别、部分识别和有限样本估计误差。

论证与表述逻辑：

1. 响应计算已经给出每套模型的答案，实际研究却可能不知道哪套模型产生了记录。现在固定可观测分布和机制假设，保留与两者相容的模型，再检查这些模型是否给出同一个响应目标。
2. 记$P_{\mathrm{obs}}^M$为模型$M$在已声明观测制度下给出的可观测分布，$\tau(M)$为目标。
3. 这是总体层面的唯一性，须与有限样本估计、数值计算区分。估计用样本逼近总体量，计算求出给定表达式或优化问题的答案。

#### 3.4.1 响应目标的点识别

主要内容：目标处理下的结果只在实际得到该处理的人身上可见。要用他们代表目标总体，需要限制处理选择与潜在结果之间的关系。

论证与表述逻辑：

1. 随机分配下的边缘识别：若处理由独立随机装置分配，且两种处理都有正概率，则$(Y(0),Y(1))\perp T$。
2. 条件交换下的调整识别：观察研究不能随意重排处理，但可以尝试用处理前$X$解释分配差异。

##### 3.4.1.1 随机分配下的边缘识别

主要内容：若处理由独立随机装置分配，且两种处理都有正概率，则$(Y(0),Y(1))\perp T$。结合一致性，对任意可测集合$B$及$t\in\{0,1\}$，有$\mathbb P(Y(t)\in B) = \mathbb P(Y(t)\in B\mid T=t) = \mathbb P(Y\in B\mid T=t)$第一个等号来自随机分配，第二个来自实际处理与潜在结果的一致性；正概率保证右侧有相应处理组。

论证与表述逻辑：

1. 若实际分析存在失访、不依从、处理溢出或随机化后的样本筛选，应按真实目标重新检查独立性和一致性。例如随机分配的邀请不等于实际参加培训，按参加者重新分组不会自动继承原随机化。

##### 3.4.1.2 条件交换下的调整识别

主要内容：观察研究不能随意重排处理，但可以尝试用处理前$X$解释分配差异。

论证与表述逻辑：

1. 定义（条件交换性）：对二元处理，条件交换性（conditional exchangeability）要求$(Y(0),Y(1))\perp T\mid X$。
2. 定义（二元处理的支持重叠）：记倾向概率为$e(x)=\mathbb P(T=1\mid X=x)$。对需要比较两种处理的目标总体，支持重叠（overlap），也称正值性（positivity），要求$0<e(x)<1,\qquad P_X\text{几乎处处}$。
3. 这也说明三项假设各管什么。一致性连接观测和潜在结果，交换性允许同层比较，重叠让每层都有所需的处理记录。

#### 3.4.2 响应目标的部分识别

主要内容：若不愿接受完整交换性，或目标行动落入无数据的区域，仍可询问现有信息排除了哪些答案。这就是部分识别（partial identification）：保留所有相容机制给出的目标值，不用一个未经支持的点掩盖机制歧义。

论证与表述逻辑：

1. 定义（识别集合）：设$\mathcal M(P_{\mathrm{obs}})$是与可观测分布及已声明假设相容的模型集合，目标为$\tau(M)$。
2. 相容类为空意味着假设与观测不相容，并不是“目标取空值”。以下讨论相容类非空的情形。

##### 3.4.2.1 结果约束下的效应界

主要内容：先只保留一致性及结果范围$0\leq Y(t)\leq1$，不假设交换性。二元处理下，$\begin{aligned} \mathbb E[Y(1)] &=\mathbb E[TY(1)]+\mathbb E[(1-T)Y(1)]\\ &=\mathbb E[TY]+\mathbb E[(1-T)Y(1)] \end{aligned}$第一项已经观察到；第二项是未处理者接受处理后的结果。

论证与表述逻辑：

1. 定义（相容机制类中的锐界）：对非空相容类$\mathcal M(P_{\mathrm{obs}})$与实值目标，若下界与上界分别等于$\inf_{M\in\mathcal M}\tau(M)$及$\sup_{M\in\mathcal M}\tau(M)$，就称为该机制类中的锐界（sharp bounds）。端点可以达到，也可以仅由相容机制序列任意逼近。
2. 中间值也可构造。独立抽取一个概率为$\lambda$的二元背景标记，按该标记选择上端构造，否则选择下端构造；事实记录不变，只切换缺失结果的赋值。

##### 3.4.2.2 支持缺口下的效应与策略界

主要内容：现在假设条件交换性可信，但双侧重叠只在协变量区域$\mathcal O$成立。用$\mathcal N$表示目标总体中缺少某种处理的区域，两者不交且覆盖目标总体。

论证与表述逻辑：

1. 单步策略评价需要的支持可以更少。假设对所有动作，$L\leq Y(a)\leq H$，且一致性和给定$X$的交换性成立。
2. 覆盖失败时，记目标策略落入缺口的概率质量及已识别贡献为$\begin{aligned} r&=\mathbb E_X\left[\sum_{a:e_a(X)=0}\pi(a\mid X)\right],\\ K&=\mathbb E_X\left[ \sum_{a:e_a(X)>0}\pi(a\mid X)\mathbb E[Y\mid T=a,X] \right] \end{aligned}$缺口部分的贡献在$[Lr,Hr]$内，因而$K+Lr\leq V(\pi)\leq K+Hr$两个策略的价值范围若完全分离，就能确定排序；若重叠，单独看边际范围未必能判断。
3. 在$r=0.2$时，价值范围为$[0.48,0.68]$。宽度$0.2$来自缺口中的未知结果机制，不会因增加同一覆盖区域内的样本而消失。

##### 3.4.2.3 未观测混杂下的敏感性范围

主要内容：另一种缺口不是某类记录完全没有，而是相同已观测背景下仍存在未观测选择差异。敏感性分析不强行断言该差异为零，而是规定其允许强度，检查结论随强度怎样变化。

论证与表述逻辑：

1. 先用一个最小线性模型定位偏差。设变量中心化，$T=\alpha U+\varepsilon_T,\qquad Y=\beta T+\gamma U+\varepsilon_Y,$其中$U,\varepsilon_T,\varepsilon_Y$两两独立、方差有限，且$\operatorname{Var}(T)>0$。
2. 跨世界配对不同的模型可能同样解释试验边缘，却改变行动成功概率或公平判断。此时应传播这些模型差异，而不是仅报告选定生成模型内的模拟精度。

#### 3.4.3 有限样本下的响应估计

主要内容：即使识别式成立，条件响应、处理概率与总体权重通常仍需从样本估计。比如调整法用$\widehat\mu_t$代替$\mu_t$，再在目标背景样本上平均：$\widehat\tau =\frac1n\sum_{i=1}^n \bigl(\widehat\mu_1(X_i)-\widehat\mu_0(X_i)\bigr)$这只是识别式的一种代入估计，不自动具有无偏性或某种收敛速度。

论证与表述逻辑：

1. 逆概率法还要估计倾向概率。很小但非零的真实概率允许总体识别，却可能使估计方差很大；截断权重可改变偏差与方差，但不能被解释为凭空补足支持。
2. 部分识别时，估计对象可以是识别集合的端点或其外包络。识别集合在总体分布已知时仍可能不是单点，表达机制歧义；置信区间来自有限样本，表达总体目标、识别集合或端点的估计误差。
3. 实际报告应分别列出相容机制留下的范围、抽样造成的不确定性，以及积分或优化中的数值误差。增加样本主要改善第二项，改善算法主要影响第三项；改变设计、扩大目标行动覆盖或加入可辩护的机制限制，才可能缩小第一项。

### 3.5 因果生成结构的表示

主要内容：用局部结构方程和背景联合分布生成整体响应，再以图记录变量依赖并讨论调整条件。

论证与表述逻辑：

1. 局部机制的结构方程表示：把模型内需要解释的变量称为内生变量，把当前模型不再解释的背景称为外生变量。“外生”是相对于模型边界而言，并不意味着这些量在现实中没有原因，也不自动意味着它们彼此独立。
2. 局部机制的复合与响应生成：无环次序让每一步只读取已经得到的值，因此既给出计算过程，也排除了同一背景下出现多个自然解的歧义。
3. 变量关系的图表示与调整条件：给定结构函数以后，逐个代入就能生成干预响应。选择调整变量时却未必需要知道每个函数的具体形式：我们要判断哪些处理前背景足以阻断处理选择与结果之间的联系。

#### 3.5.1 局部机制的结构方程表示

主要内容：把模型内需要解释的变量称为内生变量，把当前模型不再解释的背景称为外生变量。“外生”是相对于模型边界而言，并不意味着这些量在现实中没有原因，也不自动意味着它们彼此独立。

论证与表述逻辑：

1. 定义（无环结构因果模型）：本章的结构因果模型（structural causal model, SCM）由内生变量$\boldsymbol V=(V_1,\ldots,V_d)$的可测状态空间、外生背景$\boldsymbol U=(U_1,\ldots,U_d)$的联合分布及可测结构函数组成：$V_j=f_j(\operatorname{pa}_j,U_j), \qquad j=1,\ldots,d$其中$\operatorname{pa}_j$收集进入第$j$个函数的其他内生变量。无环（acyclic）要求存在节点次序$j_1,\ldots,j_d$，使每个函数的内生输入都来自次序中更早的节点。外生分量可以相关。
2. 有限维模型可以把局部函数写成$f_{j,\boldsymbol\theta_j}$，并用$\boldsymbol\theta=(\boldsymbol\theta_1,\ldots,\boldsymbol\theta_d)$汇集参数。

#### 3.5.2 局部机制的复合与响应生成

主要内容：无环次序让每一步只读取已经得到的值，因此既给出计算过程，也排除了同一背景下出现多个自然解的歧义。

论证与表述逻辑：

1. 命题（无环机制的唯一可测响应）：所得自然映射$F_M:\mathcal U\to\mathcal V$可测。将任意指定的一组方程替换为常量方程后，所得映射$F_M^a$同样存在、唯一且可测。对单变量理想干预，响应$(t,\boldsymbol u)\mapsto R_M(t,\boldsymbol u)$联合可测。
2. 推导：取符合无环性的次序$j_1,\ldots,j_d$。第一个变量没有内生父变量，因而$v_{j_1}=f_{j_1}(u_{j_1})$唯一确定，且是$\boldsymbol u$的可测函数。假设前$k-1$个变量已唯一确定为可测函数。
3. 循环方程说明这一边界并非形式问题。例如$V_1=V_2+1,V_2=V_1$无解，而$V_1=V_2,V_2=V_1$有无穷多组解。

#### 3.5.3 变量关系的图表示与调整条件

主要内容：给定结构函数以后，逐个代入就能生成干预响应。选择调整变量时却未必需要知道每个函数的具体形式：我们要判断哪些处理前背景足以阻断处理选择与结果之间的联系。

论证与表述逻辑：

1. 局部因果关系与调整影响：结构$T\leftarrow X\to Y$把$X$称为$T$与$Y$的共同原因（common cause）。
2. 全图路径分离与概率约束：设$\mathcal G=(V,E)$是有向无环图，$V$是节点集、$E$是有向边集。沿一条路径检查时，条件集中的非碰撞点会阻断路径；碰撞点自身及其后代都未被给定时，该位置也阻断路径。
3. 后门条件下的调整变量选择：现在可以反过来问：一张已经具有生成语义的图，能否为调整变量的选择提供充分依据？从$T$到$Y$且第一条边指向$T$的路径称为后门路径（back-door path），它从处理的自然生成来源进入比较，而非沿处理对结果的有向作用出发。

##### 3.5.3.1 局部因果关系与调整影响

主要内容：结构$T\leftarrow X\to Y$把$X$称为$T$与$Y$的共同原因（common cause）。

论证与表述逻辑：

1. 结构$T\to M\to Y$中的$M$是中介变量（mediator）：处理对结果的一部分影响经过它传递。若目标是总效应，固定$M$会阻断这部分变化；若研究同时设定$T=t,M=m$的响应，则需明确这是不同的联合干预。
2. 结构$T\to C\leftarrow Y$中的$C$是碰撞点（collider），两条箭头在此相遇。不以$C$筛选时，这条路径本身不要求两端相关；一旦给定$C$，却可能引入关联。
3. 共同原因和中介在所画路径上都是非碰撞点，给定它们会关闭该路径；给定碰撞点则会打开原本关闭的路径，但路径活跃并不保证实际分布一定存在非零统计依赖。

##### 3.5.3.2 全图路径分离与概率约束

主要内容：设$\mathcal G=(V,E)$是有向无环图，$V$是节点集、$E$是有向边集。沿一条路径检查时，条件集中的非碰撞点会阻断路径；碰撞点自身及其后代都未被给定时，该位置也阻断路径。

论证与表述逻辑：

1. 定义（图分离与概率独立的记号）：若各节点承载随机变量，$X_A\perp X_B\mid X_S$则表示给定$X_S$后，$X_A,X_B$的条件联合分布分解为条件边缘分布的乘积。前一个记号只依赖图，后一个记号依赖概率分布；二者之间的联系需要模型假设。
2. 定义（因果Markov性）：分布$P$相对于因果DAG $\mathcal G$满足因果Markov性（causal Markov property），是指对任意两两不交的节点集$A,B,S$，$A\perp_{\mathcal G}B\mid S \quad\Longrightarrow\quad \boldsymbol V_A\perp\boldsymbol V_B\mid\boldsymbol V_S$其中$\boldsymbol V_A,\boldsymbol V_B,\boldsymbol V_S$分别收集对应节点的随机变量。
3. 对DAG，这一全局表述等价于局部表述：每个变量在给定父变量后，与其非后代中除自身和父变量外的变量条件独立。独立外生噪声的无环SCM满足这一性质。

##### 3.5.3.3 后门条件下的调整变量选择

主要内容：现在可以反过来问：一张已经具有生成语义的图，能否为调整变量的选择提供充分依据？从$T$到$Y$且第一条边指向$T$的路径称为后门路径（back-door path），它从处理的自然生成来源进入比较，而非沿处理对结果的有向作用出发。

论证与表述逻辑：

1. 定义（单处理、单结果的后门准则）：设$T,Y$是因果DAG中的不同节点，$Z$与$\{T,Y\}$不交。若$Z$不含$T$的后代，且给定$Z$阻断所有从$T$到$Y$、第一条边指向$T$的路径，则称$Z$满足相对于$(T,Y)$的后门准则（back-door criterion）。
2. 一般后门准则在独立噪声无环SCM、图正确包含相关共同原因且干预保留其他机制的条件下，给出同样的调整结论阻断全部后门路径排除了自然处理选择沿这些路径携带的背景差异，非后代条件保证用于平均的$Z$不先被行动改变。
3. 三个局部图可以核对变量角色。在$T\leftarrow X\to Y$中，$X$关闭后门；在$T\to M\to Y$中，$M$是后代，固定它会改变总效应目标；在$T\to C\leftarrow Y$中，空条件集已经关闭碰撞路径，加入$C$反而打开它。

### 3.6 因果生成结构的推断

主要内容：区分变量关系推断与给定关系下的机制推断，说明两类不确定性怎样影响响应结论。

论证与表述逻辑：

1. 变量关系的推断：从图推出分布约束与从分布反推图，是方向相反的两项任务。要用条件独立排除候选关系，需要说明哪些独立是真正的结构阻断，哪些可能来自参数抵消。
2. 局部机制的推断：即使关系已经给定，箭头也没有给出作用大小、非线性形状和背景分布。局部机制推断要在声明的函数族、噪声条件和观测制度内估计这些未知部分。

#### 3.6.1 变量关系的推断

主要内容：从图推出分布约束与从分布反推图，是方向相反的两项任务。要用条件独立排除候选关系，需要说明哪些独立是真正的结构阻断，哪些可能来自参数抵消。

论证与表述逻辑：

1. 观测资料下的关系识别：分布$P$相对于DAG $\mathcal G$满足忠实性（faithfulness），若对任意两两不交的节点集$A,B,S$，$\boldsymbol V_A\perp\boldsymbol V_B\mid\boldsymbol V_S \quad\Longrightarrow\quad A\perp_{\mathcal G}B\mid S$。
2. 干预与环境变化下的方向识别：要打破观测方向歧义，需要增加具有不同约束的信息。理想干预切断目标变量的原进入机制：若随机设置$X$后，$Y$的分布随设置值改变，在其余机制不变、行动确实只作用于$X$的模型中，这支持$X$位于$Y$的上游。

##### 3.6.1.1 观测资料下的关系识别

主要内容：分布$P$相对于DAG $\mathcal G$满足忠实性（faithfulness），若对任意两两不交的节点集$A,B,S$，$\boldsymbol V_A\perp\boldsymbol V_B\mid\boldsymbol V_S \quad\Longrightarrow\quad A\perp_{\mathcal G}B\mid S$。

论证与表述逻辑：

1. 定义（相对于DAG的忠实性）：分布$P$相对于DAG $\mathcal G$满足忠实性（faithfulness），若对任意两两不交的节点集$A,B,S$，$\boldsymbol V_A\perp\boldsymbol V_B\mid\boldsymbol V_S \quad\Longrightarrow\quad A\perp_{\mathcal G}B\mid S$。
2. 忠实性要求分布中出现的条件独立能由图结构解释，不是由特殊参数抵消、确定性约束或未处理的误差相关造成。因果Markov性给出正向蕴含，忠实性补上反向蕴含，两者不能互相替代。
3. 定义（Markov等价与等价类）：同一节点集上的两张DAG若具有完全相同的d-分离关系，就称它们Markov等价（Markov equivalent）。与给定图Markov等价的全部DAG组成其Markov等价类（Markov equivalence class, MEC）。
4. 有限样本中的关系发现还要通过检验或评分近似总体判断。以$H_0:V_i\perp V_j\mid\boldsymbol V_S$为原假设，若约束型算法在未拒绝独立时删除候选边，那么第一类错误把真实独立误判为依赖，可能保留虚假边；第二类错误把实际依赖误判为独立，可能删除真实边。

##### 3.6.1.2 干预与环境变化下的方向识别

主要内容：要打破观测方向歧义，需要增加具有不同约束的信息。理想干预切断目标变量的原进入机制：若随机设置$X$后，$Y$的分布随设置值改变，在其余机制不变、行动确实只作用于$X$的模型中，这支持$X$位于$Y$的上游。

论证与表述逻辑：

1. 干预目标未知、执行不完全，或干预同时改变测量、选择和其他机制时，都应将这些不确定性纳入模型。不能把“鼓励参加培训”无条件等同于“把培训处理设为指定值”，也不能把伴随整套制度改变的干预解释成单个节点的理想替换。
2. 对于反馈环、随时间改变的机制或处理定义不稳定的系统，无环静态模型本身可能不合适，需要改用动态或循环模型并重新定义行动；方向识别不能先忽略模型边界，再用搜索算法的精度弥补。

#### 3.6.2 局部机制的推断

主要内容：即使关系已经给定，箭头也没有给出作用大小、非线性形状和背景分布。局部机制推断要在声明的函数族、噪声条件和观测制度内估计这些未知部分。

论证与表述逻辑：

1. 例如，对已给定的父变量向量$\boldsymbol P_j$，假设局部方程为$V_j=\theta_{j0}+\boldsymbol\theta_j^{\mathsf T}\boldsymbol P_j+\varepsilon_j, \qquad \mathbb E[\varepsilon_j\mid\boldsymbol P_j]=0$令$\boldsymbol Z_j=(1,\boldsymbol P_j^{\mathsf T})^{\mathsf T}$，并令$\boldsymbol\vartheta_j=(\theta_{j0},\boldsymbol\theta_j^{\mathsf T})^{\mathsf T}$。
2. 关系不确定、局部参数或函数不确定、跨世界背景配对不确定可能贡献不同范围；样本有限还会增加估计误差。把这些来源分别传到平均效应、策略价值或补救约束，才不会用一个最优拟合模型掩盖其他同样相容的行动后果。

### 3.7 本章小结

主要内容：以培训任务综合观测差异、主动安排和事实条件下的反事实，强调因果结论依赖生成假设与识别条件。

论证与表述逻辑：

1. 开篇的培训问题不能只由两组成绩差回答，因为自然接受处理的人可能具有不同背景。给定生成模型和背景分布以后，响应映射能计算主动改变处理的后果；得知某人的事实以后，则先更新背景分布，再在同一背景下改变行动。
2. 能够在模型内计算，不等于能够由资料识别。明确的处理版本、一致性和无干扰使目标与实际记录相连，随机分配或条件交换性支持响应识别，支持条件保证资料覆盖目标会使用的协变量--行动组合。
3. 路径、分离和结构分解为这里的图判断提供计算工具，图本身的因果解释则来自本章的机制假设。后续公平与解释专题分别回用反事实公平和行动补救，并补充规范要求与现实验证条件。
