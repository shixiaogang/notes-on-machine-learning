### tex/03-foundations/02-learning-theory/04-convex-learning-and-stability.tex:36–71
0036 
0037 \section{一致收敛}
0038 \label{sec:real-valued-classes}
0039 
0040 从零一损失换成平方损失后，我们仍要估计每个决策的期望风险，但函数取值已不再只有0和1。为此，应把每个决策对应的损失函数放在一起，得到
0041 \[
0042  \mathcal F_\ell=\{z\mapsto\ell(w,z):w\in\mathcal W\},
0043 \]
0044 再控制这组函数的样本平均与总体平均之差。这里选择损失函数空间，是因为风险直接平均损失；同一组预测函数配上不同损失，可能得到有界性和复杂度不同的函数空间。预测函数本身的维度因而不能未经转换就代入风险界。
0045 
0046 % 保留旧位置锚点；在一般损失上使用一致收敛条件。
0047 \phantomsection\label{def:general-uniform-convergence}
0048 这里仍要求一份样本同时估准整个损失类：对任意$\eta,\delta\in(0,1)$，一个充分门槛$n_{\mathrm{uc}}(\eta,\delta)$应使每个允许分布$\mathcal P$及每个$n\geq n_{\mathrm{uc}}(\eta,\delta)$满足
0049 \[
0050  \mathbb P_{S\sim\mathcal P^n}\!\left\{
0051  \sup_{w\in\mathcal W}|\hat R_S(w)-R_{\mathcal P}(w)|\leq\eta
0052  \right\}\geq1-\delta.
0053 \]
0054 这是一般损失类上的一致收敛要求（可参考\BookDefinitionRef{def:uniform-convergence}{第一卷“随机变量”章的一致收敛定义}）。
0055 这里的样本门槛可以随决策空间、损失、精度和置信度改变，却必须同时适用于每个允许分布。上确界则要求样本对所有决策的风险估计都达到精度。实值函数有连续取值，要检验这样的保证，我们需要将前章的打散扩展为函数值与阈值的比较。
0056 
0057 \subsection{伪维与胖打散维}
0058 
0059 比较实值函数时，我们可以在各输入处设置阈值，记录函数值位于阈值的哪一侧。伪维计数能够实现的这类二元模式；胖打散维$\operatorname{fat}_\gamma(\mathcal F)$进一步要求两侧函数值与阈值至少相隔$\gamma$，从而记录指定数值精度下的区分能力（可参考\BookDefinitionRef{def:pseudo-shattering}{第一卷“计数与计算”章的伪打散定义}、\BookDefinitionRef{def:pseudo-dimension}{同章的伪维定义}与\BookDefinitionRef{def:fat-shattering-dimension}{同章的胖打散维定义}）。二值函数的伪维等于VC维；多分类标签若只是名称，任意编号会引入人为的大小关系，因此这种编号后的伪维不能替代多分类维度。
0060 
0061 阈值比较与带间隔比较的差别，可以用一个幅度逐渐衰减的函数类说明。令$X=\mathbb N$，每个有限集$C\subset\mathbb N$对应$f_C(i)=1/i$（$i\in C$）和$f_C(i)=0$（$i\notin C$）。任取有限多个点$i_1,\ldots,i_m$，将阈值设为$r_j=1/(2i_j)$，再通过选择$C$决定哪些点位于阈值上方，就能实现全部高低模式，故伪维无限。胖打散却要求每个点的两个可选值相差至少$2\gamma$。由于这里的差只能是$1/i$，被胖打散的点必须满足$i\leq1/(2\gamma)$，所以每个正尺度的胖打散维都有限。接下来要检验的是：哪一种区分能力能够控制风险估计的统一偏差？
0062 
0063 \subsection{一致收敛与期望风险}
0064 
0065 风险估计只要求达到指定精度，因而相关的容量也应在这个数值尺度上衡量。下面的定理表明：对$[0,1]$值函数，若允许全部概率分布，一致收敛等价于每个正尺度的胖打散维有限。一般有界区间可先平移缩放到这一范围。若只允许较小分布族$\mathfrak P$，有限胖打散维仍足以保证一致收敛，但反向结论可能失败，因为受限分布未必能显露全部函数差异。无界损失还需尾部控制。这里及下文假定涉及的上确界、算法和期望满足所需可测性条件。
0066 
0067 \begin{theorem}[胖打散维与一致收敛]
0068 \label{thm:fat-uniform-convergence}
0069 设$(X,\mathcal A)$为可测空间，$\mathcal F$为非空的$[0,1]$值可测函数空间。
0070 假定存在可数子空间$\mathcal F_0\subseteq\mathcal F$，使每个$f\in\mathcal F$都是
0071 $\mathcal F_0$中某个函数序列的逐点极限。则以下两个命题等价：

### tex/03-foundations/02-learning-theory/04-convex-learning-and-stability.tex:1092–1114
1092 代入定理~\ref{thm:generalization-optimization-learning}即得结论。
1093 \end{proof}
1094 
1095 例如，$M$固定且$c_n\leq C<\infty$时，$b_n\to0$与$\rho_n\to0$便足以使$q_n\to0$。若$c_n$增长，则还需$b_n\sqrt{c_n}\to0$。光滑性因此可以替代全局Lipschitz条件，但转换代价保留了损失大小。后面的正则化与SGD分析将先控制参数距离，再使用这些关系估计风险。
1096 
1097 \subsection{互信息稳定性}
1098 \label{sec:information-stability}
1099 
1100 除了比较相邻样本，我们还可以直接考察输出对训练样本保留了多少信息。恒定输出不包含样本信息，逐字保存观测则保留全部样本。信息论量化两者之间的统计依赖，因而无需先给决策空间指定参数距离。这提供了分析同一个泛化问题的另一种入口。
1101 
1102 数据参与选择后，经验评价会受到样本与输出之间依赖的影响。相对熵比较真实联合规律与消除依赖后的参照规律，互信息据此量化样本—输出依赖，换测度界则把这项依赖代价转为平均评价偏差。相对熵非负，仅在两分布相同时为零，但通常不对称，不能当作距离使用（可参考\BookDefinitionRef{def:information-mutual-information}{第一卷“概率分布”章的互信息定义}及\BookSectionRef{sec:information-change-measure}{同章的“指数矩约束下的期望响应”一节}）。Russo与Zou用信息量控制自适应分析中的选择偏差\scite{russo2016bias}，Xu与Raginsky进一步将样本—输出互信息用于期望泛化差\scite{xu2017information}。
1103 
1104 为了量化训练引入的依赖，记$W=A(S,U)$，比较两个过程的分布。实际训练先抽样再计算输出，得到$P_{S,W}$；参照过程分别从边缘分布抽取样本与输出，得到$P_S\otimes P_W$。参照过程保留两者各自的分布，却消除依赖，所以当前互信息为
1105 \[
1106  I(W;S)=D_{\mathrm{KL}}(P_{S,W}\|P_S\otimes P_W).
1107 \]
1108 
1109 $I(W;S)=0$等价于输出与样本独立。学习需要利用样本，因此我们不要求这一值总为零，而要求它相对于样本量的增长足够慢，具体条件如下。
1110 
1111 \begin{definition}[互信息稳定性]
1112 \label{def:mutual-information-stability}
1113 设$S\sim\mathcal P^n$，$W=A_n(S,U)$，$U$独立于$S$。
1114 若存在不依赖$\mathcal P$的非负序列$\iota_n$，满足

### tex/03-foundations/02-learning-theory/04-convex-learning-and-stability.tex:1149–1177
1149 \end{theorem}
1150 \begin{proof}
1151 令$P=P_{S,W}$、$Q=P_S\otimes P_W$，并记
1152 $g(S,W)=R_{\mathcal P}(W)-\hat R_S(W)$。
1153 在$Q$下，给定$W$后，样本仍然独立同分布，所以$\mathbb E_Qg=0$。
1154 损失位于$[0,1]$，Hoeffding引理给出
1155 \[
1156  \log\mathbb E_Q e^{\lambda g}\leq\frac{\lambda^2}{8n},
1157  \qquad \lambda\in\mathbb R.
1158 \]
1159 若$I(W;S)=\infty$，所述上界只是平凡界。以下设互信息有限，此时$P\ll Q$；$g$有界，故在$P$下可积，上面的指数矩也有限。对任意$\lambda>0$，改变分布的代价可由相对熵控制：
1160 \begin{equation}
1161  \lambda\mathbb E_Pg
1162  \leq D_{\mathrm{KL}}(P\|Q)+\log\mathbb E_Q e^{\lambda g}.
1163  \label{eq:information-change-measure}
1164 \end{equation}
1165 这是对当前泛化差应用换测度期望界所得的关系（可参考\BookEquationRef{eq:information-change-measure-expectation}{第一卷“概率分布”章的换测度期望界}）。
1166 因此$\mathbb E_Pg\leq I(W;S)/\lambda+\lambda/(8n)$。
1167 对$-g$作相同推导，再对$\lambda$取最优值得到结论。
1168 互信息为零时取极限；互信息无穷时上界不提供有效保证。
1169 \end{proof}
1170 
1171 证明的参照过程让输出与样本独立，所以经验风险对期望风险无偏。真实训练引入依赖后，相对熵控制平均偏差增加的代价。这一比较仍然只约束期望泛化差，尚未给出单次训练的高概率误差界。
1172 
1173 \begin{theorem}[互信息稳定性与可学习性]
1174 \label{thm:mutual-information-learning}
1175 设$(Z,\mathcal Z)$与$(\mathcal W,\mathcal B_{\mathcal W})$为可测空间，
1176 $\mathcal W$非空，$\ell:\mathcal W\times Z\to[0,1]$可测。对每个允许分布
1177 $\mathcal P$，令$S=(z_1,\ldots,z_n)\sim\mathcal P^n$，令算法内部随机数

### tex/03-foundations/02-learning-theory/04-convex-learning-and-stability.tex:1244–1268
1244 \]
1245 对$n$项求和，再用三角不等式即可。
1246 \end{proof}
1247 
1248 将右侧逐观测信息代价记为$\zeta_n(\mathcal P)$，它与经验优化误差相加后给出$\zeta_n(\mathcal P)+\rho_n(\mathcal P)$的平均超额风险界。两项若都有分布无关且趋于零的上界，同样能够推出PAC学习。
1249 
1250 普通互信息可能因连续输出的精确性而无穷。例如，在$[0,1]$上均匀抽样并精确输出均值，平方损失下的期望泛化差为$2\sigma^2/n$。但$W$由$S$确定，联合分布集中在$W=\bar z$这一集合上，独立乘积分布却赋予该集合零概率，所以$I(W;S)=\infty$。这个算法可以泛化，只是普通互信息界无法给出有效数值。
1251 
1252 为避免记录连续观测的无限精度，Steinke与Zakynthinou改为衡量选择信息\scite{steinke2020conditional}。先独立抽取$n$对观测，每对随机选一个训练；在已知全部$2n$个备选观测的条件下，只考察输出额外透露了哪一项被选中。每个位置的选择只有两个结果，因此连续观测不会自动使这项信息无穷。
1253 
1254 % 保留旧位置锚点；不再重复条件互信息的编号定义。
1255 \phantomsection\label{def:stability-conditional-information}
1256 给定备选观测后，我们比较输出与选择变量的条件联合分布和条件边缘乘积，再对备选观测平均KL，得到两者的条件互信息。这里在标准Borel空间上使用这一条件核表述，以保证所需正则条件分布存在（可参考\BookDefinitionRef{def:information-conditional-mi}{第一卷“概率分布”章的条件互信息定义}）。
1257 
1258 将这个过程写成随机变量：备选样本为$\tilde S=((z_{i,0},z_{i,1}))_{i=1}^n\sim\mathcal P^{2n}$，独立选择变量$\bm B=(B_1,\ldots,B_n)$均匀取自$\{0,1\}^n$。训练样本为$S_{\bm B}=(z_{1,B_1},\ldots,z_{n,B_n})$。算法只访问选中的$n$项，输出$W=A(S_{\bm B},U)$，且$U$独立于$\tilde S,\bm B$。图~\ref{fig:conditional-information}以三个观测对说明这一选择。
1259 
1260 \begin{figure*}[!htb]
1261   \centering
1262   \includegraphics[width=164.600mm]{figures/03-foundations/02-learning-theory/generated/learning-theory-conditional-information/figure.png}
1263   \caption{条件互信息的抽样构造。每行有两个独立观测，左、右分别编号0、1；选择变量决定哪一个进入训练样本。图中$\bm B=(1,1,1)$，箭头与训练集中的内容同时标出选中的观测。算法接收选中的三个观测与独立随机种子$U$；条件互信息衡量已知全部六个观测时，输出对选择变量揭示了多少信息。}
1264  \label{fig:conditional-information}
1265 \end{figure*}
1266 
1267 \begin{definition}[算法的条件互信息量]
1268 \label{def:algorithm-cmi}

### tex/03-foundations/02-learning-theory/04-convex-learning-and-stability.tex:1431–1455
1431   \caption{期望风险的两条分析路线。左侧同时控制整个决策空间，右侧控制算法输出的期望
1432  泛化差；两条路线都要结合经验最优性。右侧用$\beta_n$泛指所选稳定性定理提供的代价项。}
1433  \label{fig:learning-risk-routes}
1434 \end{figure*}
1435 
1436 \FloatBarrier
1437 \section{凸学习问题}
1438 \label{sec:regularized-learning}
1439 \label{sec:convex-learning-problem}
1440 
1441 为了得到具体学习算法，我们现在对决策空间和损失增加凸性。正则化给经验目标加入曲率，以控制最优解的移动；SGD则逐步比较两条轨迹，再计算经验优化误差。凸性约束插值后的目标值，强凸性进一步使目标值差控制参数距离（可参考\BookDefinitionRef{def:opt-convex-set-function}{第一卷“最优化”章的凸集与凸函数定义}与\BookDefinitionRef{def:opt-strong-convexity}{同章的相对于范数的强凸性定义}）。
1442 
1443 分析梯度更新时，光滑性给梯度变化上界；PL条件用梯度大小控制目标误差，弱凸性则限制最坏负曲率（可参考\BookDefinitionRef{def:opt-smoothness}{第一卷“最优化”章的欧氏梯度光滑性定义}、\BookDefinitionRef{def:opt-pl-condition}{同章的PL条件定义}与\BookDefinitionRef{def:opt-weak-convexity}{同章的欧氏弱凸性定义}）。使用这些性质时，我们仍须在当前参数区域与范数下确认条件。例如，强凸惩罚可在不缩小原决策空间时稳定最优解，却也可能使经验风险偏离未正则化的最优值，二者必须一起计算。
1444 
1445 \subsection{凸性与损失函数}
1446 
1447 优化分类器时，我们需要知道分数改变是否降低损失。设真实标签为$+1$，分数从$-2$提高到$-0.1$，零一损失仍为1；它在零点跳变，在其余区域没有梯度变化，作为分数函数也不凸。将标签写为$y\in\{-1,1\}$后，线性分类可以采用合页损失$\max\{0,1-y\bm w^\top\bm x\}$或逻辑损失$\log(1+e^{-y\bm w^\top\bm x})$。合页损失在这个例子中从3降到1.1，分数达到1后才为零，因而同时要求正确预测和一定间隔。这些损失关于线性参数凸，便于求解，但改变了总体评价目标。\term{分类校准}（classification calibration）条件负责说明：替代风险趋于最优时，何时能够使零一风险也趋于最优。
1448 
1449 校准考察固定输入下的标签选择。记$\eta(x)=\mathbb P(y=1\mid x)$，按这个条件分布对替代损失取期望，得到条件替代风险。$\eta(x)>1/2$时，最优分数应选择正号；$\eta(x)<1/2$时应选择负号。例如，正标签概率为0.7时，预测正类错误率为0.3，负类为0.7，校准要求替代最优分数也偏好正号。凸性帮助求解，校准则联系不受限函数空间中的替代最优风险与贝叶斯风险。在受限线性类中，替代最优解未必也是零一最优解，还须检查近似能力。这里也区别于第~\ref{sec:reliability-output-evaluation}节的概率校准：后者比较预测概率与事件频率，两者没有一般相互蕴含关系。
1450 
1451 凸学习需要能够在两个决策之间插值，并约束插值后的损失。本节固定实赋范线性空间$(V,\|\cdot\|)$，取$\mathcal W\subseteq V$。除非另行改用欧氏空间，凸性、Lipschitz性和强凸性都相对于这个空间及同一范数。
1452 
1453 \begin{definition}[凸学习问题]
1454 \label{def:convex-learning-problem}
1455 若$\mathcal W$是凸集，并且对每个$z\in Z$，函数$w\mapsto\ell(w,z)$为凸函数，则称

### tex/03-foundations/02-learning-theory/04-convex-learning-and-stability.tex:1823–1847
1823  凸且$M$-光滑时，$\eta\leq2/M$保证不扩张；满足本章强凸光滑条件时，
1824  $\eta\leq1/M$保证至多以$1-\mu\eta$收缩。仅有光滑性不能排除扩张。}
1825  \label{fig:stability-curvature}
1826 \end{figure*}
1827 \FloatBarrier
1828 
1829 替换样本恒等式没有使用凸性，因此只要能控制轨迹距离，仍可得到期望泛化差。取消凸性后，需要补证的是轨迹为何接近，以及经验风险为何接近最优。下面分别处理这两个缺口。
1830 
1831 \subsection{非凸学习问题的正则化}
1832 
1833 我们先看能否用正则项消除负曲率。在欧氏凸决策集$\mathcal W$上，$\kappa$-弱凸性要求加入$\kappa\|\bm w\|_2^2/2$后目标变为凸，其中$\kappa\geq0$（可参考\BookDefinitionRef{def:opt-weak-convexity}{第一卷“最优化”章的欧氏弱凸性定义}）。例如，$-\kappa w^2/2$恰需这一强度才变平，较小二次项仍保留负曲率。在开凸域上二阶可微时，这等价于Hessian特征值不小于$-\kappa$；受限可行集上的弱凸性只约束该集合内的线段。正则强度必须与实际负曲率下界一起选择。
1834 % 保留旧位置锚点，不再重复编号定义。
1835 \phantomsection\label{def:weakly-convex}
1836 \begin{theorem}[弱凸损失的正则化稳定性]
1837 \label{thm:weakly-convex-regularization}
1838 设$(Z,\mathcal Z)$为可测观测空间，
1839 $\mathcal W=\{\bm w\in\mathbb R^d:\|\bm w\|_2\leq B\}$，其中$B\geq0$，
1840 并设$\ell:\mathcal W\times Z\to\mathbb R$可测。固定$\kappa\geq0$和$L\geq0$；
1841 对每个$z\in Z$，函数
1842 $\bm w\mapsto\ell(\bm w,z)+\kappa\|\bm w\|_2^2/2$在$\mathcal W$上凸，且
1843 \[
1844  |\ell(\bm u,z)-\ell(\bm v,z)|\leq L\|\bm u-\bm v\|_2
1845  \quad\text{对任意 }\bm u,\bm v\in\mathcal W.
1846 \]
1847 固定$n\geq1$并取$\lambda>\kappa$。对$S=(z_1,\ldots,z_n)\in Z^n$，假设

### tex/03-foundations/02-learning-theory/04-convex-learning-and-stability.tex:2012–2036
2012  \frac{2cL^2T^a}{n}\sum_{t=t_0}^{T-1}(t+1)^{-a-1}
2013  \leq\frac{2cL^2T^a}{an}\,t_0^{-a}.
2014 \]
2015 这里使用$\sum_{t=t_0}^{T-1}(t+1)^{-a-1}\leq\int_{t_0}^{T}x^{-a-1}\,dx\leq t_0^{-a}/a$。
2016 合并两种事件，并代入$a=Mc$得到第一式。再代入所给$t_0$，利用
2017 $T^{a/(a+1)}\leq t_0\leq T^{a/(a+1)}+1$即得第二式。
2018 \end{proof}
2019 
2020 固定$L,M,c$，令$T=n$，上界为$n^{-1/(a+1)}$量级。若$T$按$n^p$增长，$p<(a+1)/a$仍足以使稳定性代价下降，因此允许一定次数的重复访问。不过，得到的仍是期望泛化差。要接近最优期望风险，还须证明$\rho_{n,T}\to0$；步长和轮数条件本身不会保证算法找到经验好解。
2021 
2022 我们现在为经验优化加入结构。Polyak--\L{}ojasiewicz条件，简称PL条件，用梯度范数控制目标高于最优值的差：只要目标尚未最优，梯度就必须具有相应大小。它排除高损失的零梯度点，而不要求所有方向具有非负曲率，因而可以适用于某些非凸问题（可参考\BookDefinitionRef{def:opt-pl-condition}{第一卷“最优化”章的PL条件定义}）。本章将它用于经验目标$F$与指定参数区域，以有限下确界$F_*=\inf_{\bm w\in\mathcal W}F(\bm w)$为基准；同一个$\mu>0$须使指定区域内每点的梯度范数平方至少为$2\mu(F(\bm w)-F_*)$。下面的学习定理进一步说明哪些迭代点及样本需要满足这一要求。
2023 % 保留旧位置锚点，不再重复编号定义。
2024 \phantomsection\label{def:pl-condition}
2025 
2026 $F(w)=w^2/2$在$\mu=1$时满足等式；前面的$(w^2-1)^2$却在$w=0$处违反条件，因为梯度为零而最优值差为正。非凸函数也可能满足PL，例如$w^2+3\sin^2w$具有正参数的全局PL条件，但部分位置的二阶导数为负\scite{karimi2016pl}。PL限制的是梯度与最优值差，而不是逐方向曲率。
2027 
2028 SGD使用单样本梯度，即使经验目标满足PL，当前梯度仍会围绕经验梯度波动。下面保留这一方差代价，与初始优化误差及稳定性一起计算。
2029 
2030 \begin{theorem}[PL条件下非凸SGD的学习保证]
2031 \label{thm:pl-stability-learning}
2032 设$(Z,\mathcal Z)$为可测观测空间，
2033 $\mathcal W\subseteq\mathbb R^d$为非空凸Borel区域，
2034 并令$\mathcal O\subseteq\mathbb R^d$为包含$\mathcal W$的开集。
2035 设$\ell:\mathcal O\times Z\to\mathbb R$可测，且各单样本损失在$\mathcal O$上
2036 关于参数可微；存在$M>0$和$L\geq0$，使任意$\bm u,\bm v\in\mathcal W,z\in Z$都满足
