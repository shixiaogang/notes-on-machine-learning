from pathlib import Path
import re, json, hashlib, difflib
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'build/cross-volume-theory'
PREFIX=Path('tex/02-foundations/02-learning-theory')
names=['02-binary-classification.tex','03-multiclass-classification.tex','04-convex-learning-and-stability.tex']
texts={n:(BASE/'snapshots/volume-two'/PREFIX/n).read_text() for n in names}
changes=[]
def change(n, id, old, new):
    assert texts[n].count(old)==1,(id,texts[n].count(old))
    before=texts[n]
    start=before.index(old)
    original=(BASE/'snapshots/volume-two'/PREFIX/n).read_text()
    changes.append(dict(id=id,file=str(PREFIX/n),old=old,new=new))
    texts[n]=before.replace(old,new,1)
def lines(n,a,b):
    return '\n'.join((BASE/'snapshots/volume-two'/PREFIX/n).read_text().splitlines()[a-1:b])
B,M,G=names
change(B,'B-UC',lines(B,104,121),r'''% 保留旧位置锚点，不再重复编号定义。
\phantomsection\label{def:learning-uniform-convergence}
这里对零一损失类$\mathcal F_{01}$使用\term{一致收敛}（uniform convergence）：一份样本须同时估准全部候选的风险，而且充分样本量必须统一适用于所有允许的联合分布（可参考\BookDefinitionRef{def:uniform-convergence}{第一卷“随机变量”章的一致收敛定义}）。对任意$\eta,\delta\in(0,1)$，记一个只依赖$\mathcal H,\eta,\delta$的充分门槛为$m_{\mathcal H}^{\mathrm{UC}}(\eta,\delta)$；在第~\ref{sec:learning-problem}节的可测性与可分性约定下，任意$\mathcal P$及$n\geq m_{\mathcal H}^{\mathrm{UC}}(\eta,\delta)$应满足
\begin{equation}
 \mathbb P_{S\sim\mathcal P^n}\left(
   \sup_{h\in\mathcal H}|\hat R_S(h)-R_{\mathcal P}(h)|\leq\eta
 \right)\geq1-\delta.
 \label{eq:learning-uniform-convergence-definition}
\end{equation}

式~\eqref{eq:learning-uniform-convergence-definition}的上确界覆盖$\mathcal H$中全部风险差，不必由某个假设取到。它不超过$\eta$，就表示每个候选在这份样本上估得准；对整批抽样的概率保证允许少数样本失准。$\mathcal P$是输入与标签的联合来源，包含输入频率及条件标签规律，不只是$\mathcal P_X$。各总体风险可以随分布改变，充分样本量$m_{\mathcal H}^{\mathrm{UC}}(\eta,\delta)$须保持统一。这项估计要求不需要零风险成员，故涵盖不可知设定，分布无关的范围与定义~\ref{def:general-pac-learnability}相同。''')
change(B,'B-GROWTH',lines(B,236,236),r'''为处理无限类，我们先统计它在有限输入上可出现的预测模式；后面的对称化会说明为何这项计数能够进入风险分析。\term{限制}（restriction）类$\mathcal H|_C$保留函数在$C$上的取值，\term{生长函数}（growth function）计算$m$个输入上的最大模式数（可参考\BookDefinitionRef{def:growth-function}{第一卷“计数与计算”章的生长函数定义}）。在本章的学习记号下，这个计数为''')
change(B,'B-VC-EXAMPLE',lines(B,243,243),r'''它计算$m$个输入上最多可出现多少种二元预测。允许输入重复，因而有限输入空间也能使用任意$m$。阈值与单区间的VC维分别为1和2，前者的生长函数为$m+1$，后者为$1+m(m+1)/2$（可参考\BookSectionRef{sec:comb-vc-growth}{第一卷“计数与计算”章的“二值函数族的容量”部分}）。平面仿射半空间的VC维为3。现在要将这些容量信息转为一致收敛和样本量保证，所需的组合上界如下。''')
change(B,'B-SAUER',lines(B,248,286),r'''% 保留旧位置锚点；通用引理与组合证明引用卷一。
\phantomsection\label{lem:learning-sauer-shelah}
有限VC维把预测数限制在多项式量级。具体地，设$\mathcal H\subseteq\{0,1\}^X$非空且$1\leq d=\operatorname{VC}(\mathcal H)<\infty$，Sauer--Shelah界对每个整数$m\geq d$给出
\begin{equation}
 \Pi_{\mathcal H}(m)
 \leq\sum_{j=0}^{d}\binom{m}{j}
 \leq\left(\frac{em}{d}\right)^d
 \label{eq:learning-sauer-shelah}
\end{equation}
（可参考\BookLemmaRef{lem:sauer-shelah}{第一卷“计数与计算”章的Sauer--Shelah引理}）。这一界将无限函数类转为合并样本上的有限模式计数，下一小节再把它代入对称化后的失败概率。$d=0$时每个输入的预测唯一，生长函数恒为1，应单独处理，避免使用以$d$作分母的式子。''')
change(B,'B-GROWTH-PLOT',lines(B,290,290),r'''用同一对数坐标比较$2^m$与单区间类的精确模式数$1+m(m+1)/2$，可以看到全部二元组合与有限VC类的增长差别（可参考\BookSectionRef{sec:comb-vc-growth}{第一卷“计数与计算”章的“二值函数族的容量”部分中的模式数图}）。两者差距随$m$扩大，可实现模式占全部组合的比例变小，候选函数本身仍可以无限。''')
change(B,'B-RAD-ENTRY',lines(B,448,448),r'''本章先控制经验均值低估总体均值的方向，使用不带绝对值的单侧随机复杂度：先在类中取最大的随机相关和，再对独立符号平均（可参考\BookDefinitionRef{def:rademacher-complexity}{第一卷“随机变量”章的经验Rademacher复杂度定义}）。对$S=(z_1,\ldots,z_n)$与非空实值类$\mathcal G$，在学习场景中记为''')
change(B,'B-RAD-SIDED',lines(B,460,460),r'''带绝对值的版本等于$\mathcal G\cup(-\mathcal G)$的单侧复杂度；在取负封闭的类上两者相同，一般则绝对值版本不小于单侧版本（可参考\BookSectionRef{sec:probability-uniform-errors-symmetry}{第一卷“随机变量”章的“候选族累计量的统一偏差控制”一节}）。使用收缩或比较结果时须按版本核对常数。''')
change(B,'B-CONTRACTION',lines(B,535,535),r'''得分与零一损失不是同一个函数。若损失对得分为$L$-Lipschitz，得分改变$a$时，损失至多改变$L|a|$，\term{收缩引理}（contraction lemma）便能将预测复杂度转成损失复杂度。本章的单侧版本使用系数$L$；$\phi(0)\neq0$时先减该常数，随机和的期望不变。一般绝对值版本还可能多出因子2，不能混用两种口径（可参考\BookSectionRef{sec:probability-uniform-errors-symmetry}{第一卷“随机变量”章的“候选族累计量的统一偏差控制”一节}）。只有核对这种变化率条件之后才能转界，式~\eqref{eq:linear-rademacher-bound}本身不是零一风险界。''')
change(B,'B-GAUSS-ENTRY',lines(B,574,574),r'''把等幅随机符号换成标准高斯系数，可以从另一种随机相关和估计损失类复杂度。两种系数的幅度规律不同，需要先核对比较方向（可参考\BookDefinitionRef{def:gaussian-complexity}{第一卷“随机变量”章的高斯复杂度定义}及\BookSectionRef{sec:probability-uniform-errors-symmetry}{同章的“候选族累计量的统一偏差控制”一节}）。对独立标准高斯系数$\xi_i$，本章使用单侧\term{经验高斯复杂度}（empirical Gaussian complexity）''')
change(B,'B-CONVEX-HULL',lines(B,954,982),r'''% 保留旧位置锚点；这里回顾投票得分所用的恒等式。
\phantomsection\label{thm:learning-ensemble-convex-hull}
对固定输入样本$S_X=(x_1,\ldots,x_n)$和非空有界基函数类$\mathcal B$，有限非负归一化加权不会增大单侧Rademacher复杂度：
\[
 \widehat{\mathfrak R}_{S_X}(\operatorname{conv}(\mathcal B))
 =\widehat{\mathfrak R}_{S_X}(\mathcal B)
\]
（可参考\BookTheoremRef{thm:ensemble-convex-hull}{第一卷“随机变量”章的凸组合Rademacher复杂度定理}）。这里控制的是归一化得分，而不是取符号后的分类器。接下来通过间隔损失把这项得分控制转为零一风险保证。''')
change(M,'M-BIT-LOSS',lines(M,48,48),r'''逐位学习在不可知情形不一定优化原任务。沿用三类编码，设输入恒定，正常、广告、诈骗的概率为0.40、0.35、0.25，候选为三个常量假设。第一位为1的概率0.60，第二位为1的概率0.65，各位最优都选1，合成诈骗后风险0.75；直接选正常的风险却为0.60。即使已知所有概率，逐位最优仍选错原任务的最优类别。逐位优化分别降低每个编码位的错误概率；多类零一损失只在整个标签正确时计0，其余一律计1。同一错误标签可能在两位上都出错，两项位损失便分别记错，而类别损失只记一次。两个优化目标因此并不相同。''')
change(M,'M-NATARAJAN',lines(M,61,73),r'''固定输入处的两种标签选择能够限制有限标签类的预测数。Natarajan打散要求先为每个输入固定两个不同答案，再由类中的函数实现这组标签对的全部独立选择；标签对可以随输入改变，却不能随待实现的模式改变（可参考\BookDefinitionRef{def:natarajan-dimension}{第一卷“计数与计算”章的Natarajan打散与维度定义}）。本章以$d_N(\mathcal H)$记可打散有限输入集大小的上确界。
% 旧公式位置保留为导航锚点，不再重复通用定义式。
\phantomsection\label{eq:learning-natarajan-shattering}

这一条件不要求标签有限。二类时各处的不同标签对只能取那两个答案，故它退化为VC维。维度0说明各输入预测唯一；可打散点集没有有限规模上界时，维度为无穷。这里继续把所得维度接到预测计数。''')
change(M,'M-GROWTH',lines(M,88,104),r'''% 保留旧位置锚点；这里直接使用组合计数结论。
\phantomsection\label{thm:learning-multiclass-growth-bound}
当$2\leq K=|Y|<\infty$且$d=d_N(\mathcal H)<\infty$时，记$q=K(K-1)/2$为不同无序标签对的数目。对每个整数$m\geq0$，有限标签的计数界给出
\[
 \Pi_{\mathcal H}(m)\leq G_{d,K}(m)
 :=\sum_{j=0}^{\min\{d,m\}}\binom mj q^j
\]
（可参考\BookTheoremRef{thm:multiclass-growth-bound}{第一卷“计数与计算”章的有限标签预测数目上界}）。在学习问题中，$G_{d,K}(2n)$将控制原样本与副样本合并后的不同损失模式数，因而能够进入下一步对称化后的失败概率。''')
change(M,'M-DS-CAPTION','后文定义的DS维为2','后文分析的DS维为2')
change(M,'M-GRAPH',lines(M,285,300),r'''零一损失把无限个错误答案都计为1，风险只看与真值是否匹配。为描述这一二元能力，我们先给每个输入固定参考答案$f(x)$，再问能否任意指定一组匹配位置。\term{图打散}（graph shattering）要求对每个位置子集都有类中函数恰在这些位置匹配参考，在其余位置全部偏离参考；偏离时使用的标签可以随模式改变（可参考\BookDefinitionRef{def:graph-dimension}{第一卷“计数与计算”章的图打散定义}）。

可图打散有限输入集大小的上确界记为$d_G(\mathcal H)$（可参考\BookDefinitionRef{def:graph-dimension-value}{第一卷“计数与计算”章的图维定义}）。图打散只预定参考答案，Natarajan打散还预定每处的替代答案，因此后者推出前者，逆向未必成立。接下来利用“匹配或偏离”的二元模式，将图维转为零一损失类的VC维。''')
change(M,'M-PSEUDOCUBE',lines(M,414,414),r'''为了描述遗漏坐标上的竞争答案，我们在限制类中寻找有限非空的预测集合$V\subseteq Y^m$。要求每个$v\in V$在每个坐标$i$上都有集合内的另一个向量$u$：它只改变该坐标的答案，其余全部坐标与$v$相同。这正是本章下界证明需要的\term{伪立方体}（pseudo-cube）条件（可参考\BookDefinitionRef{def:pseudocube}{第一卷“计数与计算”章的伪立方体定义}）。''')
change(M,'M-DS-DIM',lines(M,418,418),r'''DS维寻找能保留上述逐坐标歧义的最大输入规模。对$m$个互异输入按固定次序组成的$C$，检查限制类$\mathcal H|_C$是否含$m$维伪立方体；满足条件的有限输入规模取上确界，记为$d_{DS}(\mathcal H)$（可参考\BookDefinitionRef{def:ds-dimension}{第一卷“计数与计算”章的DS维定义}）。下面考察它如何决定学习。''')
change(M,'M-DS-RING',lines(M,420,420),r'''图~\ref{fig:learning-theory-ds-neighbors}展示第~\ref{sec:multiclass-erm-limitations}节的六种预测，两种线型分别表示只改变一个坐标的邻接。每个顶点在两个坐标上均有邻居，所以这个两输入类的DS维为2；环缺少固定两标签对的完整四种组合，所以Natarajan维仅1。这个有限类仍可学习；无限标签下的不可学习反例还依赖任意维的局部构造及其在同一假设空间中的合并。''')
change(M,'M-DS-COMPARE-ENTRY',lines(M,422,422),r'''在$m-1$个坐标已知时，剩余邻居使遗漏标签未定。对每个向量、每个坐标都要求邻居，避免仅在个别向量周围留少量分支。固定标签对、固定参考答案与逐坐标邻接因而是不同要求；图中的一段邻接关系只有扩展到有限集合内的每个向量和每个坐标，才满足完整伪立方体条件（可参考\BookSectionRef{sec:comb-multiclass-dimensions}{第一卷“计数与计算”章的“多值函数族的容量”部分}）。''')
change(M,'M-DIM-COMPARE',lines(M,424,433),r'''% 保留旧位置锚点；通用维度比较引用卷一。
\phantomsection\label{thm:learning-multiclass-dimension-comparison}
这些结构满足$d_N(\mathcal H)\leq d_{DS}(\mathcal H)\leq d_G(\mathcal H)$；二标签时三者均等于VC维。有限标签空间下，Natarajan维有限还蕴含图维有限（可参考\BookTheoremRef{thm:multiclass-dimension-comparison}{第一卷“计数与计算”章的多分类维度比较定理}）。这里使用三个关系：固定标签对的全部组合构成伪立方体；逐坐标邻接支持图打散；有限标签的指数图模式又受多项式预测计数限制。''')
change(M,'M-DIM-COMPARE-REF1','依据是定理~\\ref{thm:learning-multiclass-dimension-comparison}和定理~\\ref{thm:finite-label-learnability}。',r'''有限标签的学习等价见定理~\ref{thm:finite-label-learnability}（维度关系可参考\BookTheoremRef{thm:multiclass-dimension-comparison}{第一卷“计数与计算”章的多分类维度比较定理}）。''')
change(M,'M-DIM-COMPARE-REF2','有限标签时，Natarajan有限经定理~\\ref{thm:learning-multiclass-dimension-comparison}给图维有限，所以可替条件。',r'''有限标签时，Natarajan维有限蕴含图维有限，所以可替条件（可参考\BookTheoremRef{thm:multiclass-dimension-comparison}{第一卷“计数与计算”章的多分类维度比较定理}）。''')
change(G,'G-UC',lines(G,46,57),r'''% 保留旧位置锚点；在一般损失上使用一致收敛条件。
\phantomsection\label{def:general-uniform-convergence}
这里仍要求一份样本同时估准整个损失类：对任意$\eta,\delta\in(0,1)$，一个充分门槛$n_{\mathrm{uc}}(\eta,\delta)$应使每个允许分布$\mathcal P$及每个$n\geq n_{\mathrm{uc}}(\eta,\delta)$满足
\[
 \mathbb P_{S\sim\mathcal P^n}\!\left\{
 \sup_{w\in\mathcal W}|\hat R_S(w)-R_{\mathcal P}(w)|\leq\eta
 \right\}\geq1-\delta.
\]
这是一般损失类上的一致收敛要求（可参考\BookDefinitionRef{def:uniform-convergence}{第一卷“随机变量”章的一致收敛定义}）。''')
change(G,'G-UC-FOLLOW','定义中的样本门槛可以随决策空间、损失、精度和置信度改变','这里的样本门槛可以随决策空间、损失、精度和置信度改变')
change(G,'G-PSEUDO-POINTER',lines(G,62,62),r'''比较实值函数时，我们可以在各输入处设置阈值，记录函数值位于阈值的哪一侧。伪维计数能够实现的这类二元模式；胖打散维$\operatorname{fat}_\gamma(\mathcal F)$进一步要求两侧函数值与阈值至少相隔$\gamma$，从而记录指定数值精度下的区分能力（可参考\BookDefinitionRef{def:pseudo-shattering}{第一卷“计数与计算”章的伪打散定义}、\BookDefinitionRef{def:pseudo-dimension}{同章的伪维定义}与\BookDefinitionRef{def:fat-shattering-dimension}{同章的胖打散维定义}）。二值函数的伪维等于VC维；多分类标签若只是名称，任意编号会引入人为的大小关系，因此这种编号后的伪维不能替代多分类维度。''')
change(G,'G-MI-ENTRY',lines(G,1105,1105),r'''数据参与选择后，经验评价会受到样本与输出之间依赖的影响。相对熵比较真实联合规律与消除依赖后的参照规律，互信息据此量化样本—输出依赖，换测度界则把这项依赖代价转为平均评价偏差。相对熵非负，仅在两分布相同时为零，但通常不对称，不能当作距离使用（可参考\BookDefinitionRef{def:information-mutual-information}{第一卷“概率分布”章的互信息定义}及\BookSectionRef{sec:information-change-measure}{同章的“指数矩约束下的期望响应”一节}）。Russo与Zou用信息量控制自适应分析中的选择偏差\scite{russo2016bias}，Xu与Raginsky进一步将样本—输出互信息用于期望泛化差\scite{xu2017information}。''')
change(G,'G-MI-AC','对任意$\\lambda>0$，改变分布的代价可由相对熵控制：',r'''若$I(W;S)=\infty$，所述上界只是平凡界。以下设互信息有限，此时$P\ll Q$；$g$有界，故在$P$下可积，上面的指数矩也有限。对任意$\lambda>0$，改变分布的代价可由相对熵控制：''')
change(G,'G-MI-CHANGE-POINTER',lines(G,1168,1169),r'''这是对当前泛化差应用换测度期望界所得的关系（可参考\BookEquationRef{eq:information-change-measure-expectation}{第一卷“概率分布”章的换测度期望界}）。''')
change(G,'G-CMI-RECALL',lines(G,1258,1266),r'''% 保留旧位置锚点；不再重复条件互信息的编号定义。
\phantomsection\label{def:stability-conditional-information}
给定备选观测后，我们比较输出与选择变量的条件联合分布和条件边缘乘积，再对备选观测平均KL，得到两者的条件互信息。这里在标准Borel空间上使用这一条件核表述，以保证所需正则条件分布存在（可参考\BookDefinitionRef{def:information-conditional-mi}{第一卷“概率分布”章的条件互信息定义}）。''')
change(G,'G-CONVEX-ENTRY',lines(G,1451,1451),r'''为了得到具体学习算法，我们现在对决策空间和损失增加凸性。正则化给经验目标加入曲率，以控制最优解的移动；SGD则逐步比较两条轨迹，再计算经验优化误差。凸性约束插值后的目标值，强凸性进一步使目标值差控制参数距离（可参考\BookDefinitionRef{def:opt-convex-set-function}{第一卷“最优化”章的凸集与凸函数定义}与\BookDefinitionRef{def:opt-strong-convexity}{同章的相对于范数的强凸性定义}）。

分析梯度更新时，光滑性给梯度变化上界；PL条件用梯度大小控制目标误差，弱凸性则限制最坏负曲率（可参考\BookDefinitionRef{def:opt-smoothness}{第一卷“最优化”章的欧氏梯度光滑性定义}、\BookDefinitionRef{def:opt-pl-condition}{同章的PL条件定义}与\BookDefinitionRef{def:opt-weak-convexity}{同章的欧氏弱凸性定义}）。使用这些性质时，我们仍须在当前参数区域与范数下确认条件。例如，强凸惩罚可在不缩小原决策空间时稳定最优解，却也可能使经验风险偏离未正则化的最优值，二者必须一起计算。''')
change(G,'G-WEAK-RECALL',lines(G,1841,1849),r'''我们先看能否用正则项消除负曲率。在欧氏凸决策集$\mathcal W$上，$\kappa$-弱凸性要求加入$\kappa\|\bm w\|_2^2/2$后目标变为凸，其中$\kappa\geq0$（可参考\BookDefinitionRef{def:opt-weak-convexity}{第一卷“最优化”章的欧氏弱凸性定义}）。例如，$-\kappa w^2/2$恰需这一强度才变平，较小二次项仍保留负曲率。在开凸域上二阶可微时，这等价于Hessian特征值不小于$-\kappa$；受限可行集上的弱凸性只约束该集合内的线段。正则强度必须与实际负曲率下界一起选择。
% 保留旧位置锚点，不再重复编号定义。
\phantomsection\label{def:weakly-convex}''')
change(G,'G-PL-RECALL',lines(G,2036,2046),r'''我们现在为经验优化加入结构。Polyak--\L{}ojasiewicz条件，简称PL条件，用梯度范数控制目标高于最优值的差：只要目标尚未最优，梯度就必须具有相应大小。它排除高损失的零梯度点，而不要求所有方向具有非负曲率，因而可以适用于某些非凸问题（可参考\BookDefinitionRef{def:opt-pl-condition}{第一卷“最优化”章的PL条件定义}）。本章将它用于经验目标$F$与指定参数区域，以有限下确界$F_*=\inf_{\bm w\in\mathcal W}F(\bm w)$为基准；同一个$\mu>0$须使指定区域内每点的梯度范数平方至少为$2\mu(F(\bm w)-F_*)$。下面的学习定理进一步说明哪些迭代点及样本需要满足这一要求。
% 保留旧位置锚点，不再重复编号定义。
\phantomsection\label{def:pl-condition}''')
patch=''
for n,t in texts.items():
    path=PREFIX/n
    out=BASE/'proposed'/path
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(t)
    old=(BASE/'snapshots/volume-two'/path).read_text()
    patch+=''.join(difflib.unified_diff(old.splitlines(True),t.splitlines(True),fromfile='a/'+str(path),tofile='b/'+str(path)))
(BASE/'suggested.patch').write_text(patch)
(BASE/'old-new.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
(BASE/'proposal-sha.json').write_text(json.dumps({str(PREFIX/n):hashlib.sha256(t.encode()).hexdigest() for n,t in texts.items()},indent=2)+'\n')
print(json.dumps({'changes':len(changes),'files':len(texts),'patch_lines':len(patch.splitlines())}))

