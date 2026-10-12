### tex/03-foundations/02-learning-theory/02-binary-classification.tex:94–126
0094 图中的竖线表示各候选的估计偏差。固定容限$\eta$，四个阈值的风险差都不超过它，才算这份样本同时估得准。我们要找一个统一邮件数，使独立抽样得到这种共同事件的概率至少$1-\delta$，而不按未知邮件与标签分布另定样本量。下面正式定义这个要求。
0095 
0096 \paragraph{可测性与可分性约定}
0097 
0098 有限类的上确界是有限个可测随机变量的最大值。无限类则须处理整个零一损失函数类
0099 \[
0100  \mathcal F_{01}=\{(x,y)\mapsto\ell_{01}(h(x),y):h\in\mathcal H\}
0101 \]
0102 本章采用第~\ref{sec:learning-problem}节给出的可测性与可分性条件，使相关上确界和比较事件可测。压缩、重构与学习器的数据依赖映射也须可测。可实现样本可选与它一致的成员，其他存在性论证采用该约定中的可测近似ERM；缺少这些条件时，以下结论不能直接沿用。
0103 
0104 % 保留旧位置锚点，不再重复编号定义。
0105 \phantomsection\label{def:learning-uniform-convergence}
0106 这里对零一损失类$\mathcal F_{01}$使用\term{一致收敛}（uniform convergence）：一份样本须同时估准全部候选的风险，而且充分样本量必须统一适用于所有允许的联合分布（可参考\BookDefinitionRef{def:uniform-convergence}{第一卷“随机变量”章的一致收敛定义}）。对任意$\eta,\delta\in(0,1)$，记一个只依赖$\mathcal H,\eta,\delta$的充分门槛为$m_{\mathcal H}^{\mathrm{UC}}(\eta,\delta)$；在第~\ref{sec:learning-problem}节的可测性与可分性约定下，任意$\mathcal P$及$n\geq m_{\mathcal H}^{\mathrm{UC}}(\eta,\delta)$应满足
0107 \begin{equation}
0108  \mathbb P_{S\sim\mathcal P^n}\left(
0109    \sup_{h\in\mathcal H}|\hat R_S(h)-R_{\mathcal P}(h)|\leq\eta
0110  \right)\geq1-\delta.
0111  \label{eq:learning-uniform-convergence-definition}
0112 \end{equation}
0113 
0114 式~\eqref{eq:learning-uniform-convergence-definition}的上确界覆盖$\mathcal H$中全部风险差，不必由某个假设取到。它不超过$\eta$，就表示每个候选在这份样本上估得准；对整批抽样的概率保证允许少数样本失准。$\mathcal P$是输入与标签的联合来源，包含输入频率及条件标签规律，不只是$\mathcal P_X$。各总体风险可以随分布改变，充分样本量$m_{\mathcal H}^{\mathrm{UC}}(\eta,\delta)$须保持统一。这项估计要求不需要零风险成员，故涵盖不可知设定，分布无关的范围与定义~\ref{def:general-pac-learnability}相同。
0115 
0116 一致收敛评价的是风险估计，而非风险大小。高风险候选若在样本上也表现为高风险，仍符合估计准确的要求。
0117 
0118 有限空间的共同偏差事件等价于没有候选的风险差超过$\eta$。式~\eqref{eq:hoeffding-fixed-hypothesis}先控制一个固定候选失准的概率，将这些有限个概率相加，就控制了至少一个候选失准的事件。
0119 
0120 \begin{theorem}[有限假设空间的一致收敛样本量界]
0121 \label{thm:finite-uniform-convergence}
0122 设$(X,\mathcal X)$为可测空间，$Y=\{0,1\}$取离散$\sigma$代数，
0123 $\mathcal H\subseteq Y^X$是由可测分类器组成的非空有限集合，$\mathcal P$是
0124 $X\times Y$上的任意联合分布。对零一损失，记
0125 \[
0126  R_{\mathcal P}(h)=\mathbb P_{(x,y)\sim\mathcal P}\{h(x)\neq y\},\qquad

### tex/03-foundations/02-learning-theory/02-binary-classification.tex:219–266
0219 失败预算还可以按空间的描述长度分配。给序号$k$预定一个二进制编码，并要求任一编码都不是另一个的开头，得到前缀编码，例如$0,10,11$标记三个空间。设编码长为$L_k$。在足够长的二进制串中，以该编码开头者占$2^{-L_k}$，不同前缀对应的串互不重叠，任意有限组的比例和便不超过1。由此全部编码也满足$\sum_k2^{-L_k}\leq1$，可以取$\delta_k=\delta2^{-L_k}$。由于$\log(1/\delta_k)=\log(1/\delta)+L_k\log2$，较长空间描述带来较小预算与较大$p_k$。这里编码只描述选哪个空间，作用是有效分配失败概率，并非PAC定义另加的必要条件。
0220 
0221 \section{无限假设空间}
0222 \label{sec:binary-infinite-class}
0223 
0224 有限空间可逐候选加失败概率，得到式~\eqref{eq:finite-uniform-sample}的样本量；无限空间这样求和则失去有限上界。我们改问：在一组有限输入上，这些函数能产生多少种不同预测？很多函数若在该组输入上回答相同，就无需在经验风险分析中分别计数。
0225 
0226 \subsection{VC维与生长函数的学习论接口}
0227 \label{sec:binary-shattering-vc}
0228 
0229 为处理无限类，我们先统计它在有限输入上可出现的预测模式；后面的对称化会说明为何这项计数能够进入风险分析。\term{限制}（restriction）类$\mathcal H|_C$保留函数在$C$上的取值，\term{生长函数}（growth function）计算$m$个输入上的最大模式数（可参考\BookDefinitionRef{def:growth-function}{第一卷“计数与计算”章的生长函数定义}）。在本章的学习记号下，这个计数为
0230 \begin{equation}
0231  \Pi_{\mathcal H}(m)
0232  =\max_{x_1,\ldots,x_m\in X}
0233    \left|\{(h(x_1),\ldots,h(x_m)):h\in\mathcal H\}\right|.
0234  \label{eq:learning-growth-function}
0235 \end{equation}
0236 它计算$m$个输入上最多可出现多少种二元预测。允许输入重复，因而有限输入空间也能使用任意$m$。阈值与单区间的VC维分别为1和2，前者的生长函数为$m+1$，后者为$1+m(m+1)/2$（可参考\BookSectionRef{sec:comb-vc-growth}{第一卷“计数与计算”章的“二值函数族的容量”部分}）。平面仿射半空间的VC维为3。现在要将这些容量信息转为一致收敛和样本量保证，所需的组合上界如下。
0237 
0238 \subsection{Sauer--Shelah引理}
0239 \label{sec:binary-growth-sauer}
0240 
0241 % 保留旧位置锚点；通用引理与组合证明引用卷一。
0242 \phantomsection\label{lem:learning-sauer-shelah}
0243 有限VC维把预测数限制在多项式量级。具体地，设$\mathcal H\subseteq\{0,1\}^X$非空且$1\leq d=\operatorname{VC}(\mathcal H)<\infty$，Sauer--Shelah界对每个整数$m\geq d$给出
0244 \begin{equation}
0245  \Pi_{\mathcal H}(m)
0246  \leq\sum_{j=0}^{d}\binom{m}{j}
0247  \leq\left(\frac{em}{d}\right)^d
0248  \label{eq:learning-sauer-shelah}
0249 \end{equation}
0250 （可参考\BookLemmaRef{lem:sauer-shelah}{第一卷“计数与计算”章的Sauer--Shelah引理}）。这一界将无限函数类转为合并样本上的有限模式计数，下一小节再把它代入对称化后的失败概率。$d=0$时每个输入的预测唯一，生长函数恒为1，应单独处理，避免使用以$d$作分母的式子。
0251 
0252 固定$d$时，Sauer--Shelah的界至多按$m^d$增长，全部二元预测却有$2^m$种。有限VC维因而阻止生长函数持续指数增长。它给的是上界，实际可以更慢；例如VC维3的平面仿射半空间只有$m^2$量级的预测数。
0253 
0254 用同一对数坐标比较$2^m$与单区间类的精确模式数$1+m(m+1)/2$，可以看到全部二元组合与有限VC类的增长差别（可参考\BookSectionRef{sec:comb-vc-growth}{第一卷“计数与计算”章的“二值函数族的容量”部分中的模式数图}）。两者差距随$m$扩大，可实现模式占全部组合的比例变小，候选函数本身仍可以无限。
0255 
0256 \subsection{二分类可学习性基本定理}
0257 \label{sec:binary-learnability-characterization}
0258 
0259 一致收敛已说明怎样把ERM的训练比较转成总体比较。现在候选无限，所需的是所有风险差的共同概率控制。生长函数只数有限输入上的预测，接下来用第二份样本把未知总体风险换成有限输入上的可比较量。
0260 
0261 在证明中独立抽取副样本$S'=(z_1',\ldots,z_n')$，与$S=(z_1,\ldots,z_n)$同来自联合分布$\mathcal P$，$z_i=(x_i,y_i)$。这份\term{副样本}（ghost sample）使未知风险能够通过另一份经验平均分析，学习算法不需要实际得到它。
0262 
0263 固定$S$选定$h$后，$S'$未参与选解，因此$\hat R_{S'}(h)$对其独立评价，平均值就是$R_{\mathcal P}(h)$。若原经验风险偏离总体很大、副样本风险又接近总体，两份经验风险必有较大差异。我们因此以双样本差事件控制原样本偏差事件。此步骤只对原样本选出的那个假设使用副样本估计，尚不要求副样本同时估准全部候选。
0264 
0265 双样本只涉及$2n$个输入，同预测的函数给出相同经验风险，故至多需要区分$\Pi_{\mathcal H}(2n)$种结果。再让每对$(z_i,z_i')$独立公平交换或保持原位。iid使联合分布不变，固定预测的差贡献则随机变号，可以应用集中不等式。将各预测的尾概率相加，就控制了任意候选产生大差的概率。副样本与随机交换构成\term{对称化}（symmetrization），作用是把总体比较转成有限计数及随机符号比较。
0266 

### tex/03-foundations/02-learning-theory/02-binary-classification.tex:402–436
0402 
0403 \section{估计期望风险}
0404 \label{sec:rademacher-complexity}
0405 
0406 VC维回答了二分类是否能统一学习。对于样本已经选出的一个假设，我们还想知道它的总体风险上限。经验损失可直接计算，未知来源上的损失则需要在经验值之外补一个偏差控制量。
0407 
0408 VC界按全输入空间的打散能力控制偏差，尚未利用当前样本位置和函数值。Rademacher与高斯复杂度保留这些信息，给出“经验风险加复杂度及抽样误差”的高概率上界。这里估计的是风险上限，没有宣称有限样本能够精确恢复未知总体风险。
0409 
0410 \subsection{Rademacher复杂度}
0411 
0412 本章先控制经验均值低估总体均值的方向，使用不带绝对值的单侧随机复杂度：先在类中取最大的随机相关和，再对独立符号平均（可参考\BookDefinitionRef{def:rademacher-complexity}{第一卷“随机变量”章的经验Rademacher复杂度定义}）。对$S=(z_1,\ldots,z_n)$与非空实值类$\mathcal G$，在学习场景中记为
0413 \begin{equation}
0414  \widehat{\mathfrak R}_S(\mathcal G)
0415  =\mathbb E_\sigma\left[\sup_{f\in\mathcal G}
0416        \frac1n\sum_{i=1}^n\sigma_i f(z_i)\right].
0417  \label{eq:learning-empirical-rademacher}
0418 \end{equation}
0419 符号$\sigma_i$独立且等概率取$-1,1$，再对样本平均得到
0420 \[
0421  \mathfrak R_n(\mathcal G)=\mathbb E_{S\sim\mathcal P^n}
0422        \widehat{\mathfrak R}_S(\mathcal G).
0423 \]
0424 带绝对值的版本等于$\mathcal G\cup(-\mathcal G)$的单侧复杂度；在取负封闭的类上两者相同，一般则绝对值版本不小于单侧版本（可参考\BookSectionRef{sec:probability-uniform-errors-symmetry}{第一卷“随机变量”章的“候选族累计量的统一偏差控制”一节}）。使用收缩或比较结果时须按版本核对常数。
0425 
0426 \subsection{线性预测的复杂度}
0427 
0428 对线性得分$f_{\bm w}(\bm x)=\bm w^\top\bm x$，随机相关和可写成$\bm w^\top\sum_i\sigma_i\bm x_i$。若参数不受限且后一个向量非零，这个量可任意增大，复杂度便不能给出有限控制。为此设$B>0$并限制$\|\bm w\|_2\leq B$，取$\mathcal F=\{\bm x\mapsto\bm w^\top\bm x:\|\bm w\|_2\leq B\}$，假定每个样本输入满足$\|\bm x_i\|_2\leq r$。以$S_X=(\bm x_1,\ldots,\bm x_n)$记输入样本，先计算得分复杂度：
0429 \begin{align}
0430  \widehat{\mathfrak R}_{S_X}(\mathcal F)
0431  &=\frac1n\mathbb E_\sigma\sup_{\lVert\bm{w}\rVert_2\leq B}
0432    \bm{w}^\top\sum_i\sigma_i \bm{x}_i\nonumber\\
0433  &\leq\frac{B}{n}\sqrt{\sum_i\lVert\bm{x}_i\rVert_2^2}
0434  \leq\frac{Br}{\sqrt n}.
0435  \label{eq:linear-rademacher-bound}
0436 \end{align}

### tex/03-foundations/02-learning-theory/02-binary-classification.tex:489–511
0489 \[
0490  \mathfrak R_n(\mathcal G)
0491  \leq\widehat{\mathfrak R}_S(\mathcal G)
0492  +\sqrt{\frac{\log(2/\delta)}{2n}}.
0493 \]
0494 再把第一界的失败预算设为$\delta/2$，两个事件的共同概率至少$1-\delta$。替换其中的期望复杂度并合并三项偏差，得到第二界。
0495 \end{proof}
0496 
0497 取$g=g_h$后，左侧是总体风险，右侧首项是经验风险，另外两项补偿由样本均值推断总体均值的复杂度与抽样代价。共同保证覆盖全部$h$，所以也覆盖数据选解。经验版本可按当前样本估复杂度，同VC维空间也可能因样本函数值不同得到不同风险界，这正是数据相关分析的用途\scite{bartlettmendelson2002}。
0498 
0499 得分与零一损失不是同一个函数。若损失对得分为$L$-Lipschitz，得分改变$a$时，损失至多改变$L|a|$，\term{收缩引理}（contraction lemma）便能将预测复杂度转成损失复杂度。本章的单侧版本使用系数$L$；$\phi(0)\neq0$时先减该常数，随机和的期望不变。一般绝对值版本还可能多出因子2，不能混用两种口径（可参考\BookSectionRef{sec:probability-uniform-errors-symmetry}{第一卷“随机变量”章的“候选族累计量的统一偏差控制”一节}）。只有核对这种变化率条件之后才能转界，式~\eqref{eq:linear-rademacher-bound}本身不是零一风险界。
0500 
0501 将得分复杂度转为分类风险，还要选择损失。取$y\in\{-1,1\}$、$f(\bm x)=\bm w^\top\bm x$，则$yf(\bm x)$为带符号的分类间隔：正值表示方向正确，绝对大小在得分尺度上衡量距阈值0的距离。参数向量非零时，几何间隔还须除以$\|\bm w\|_2$。对固定$\rho>0$，用下列间隔损失同时惩罚错分和不足的正间隔：
0502 \[
0503  \ell_\rho(f(\bm x),y)=
0504  \begin{cases}
0505   1,&yf(\bm x)\leq0,\\
0506   1-yf(\bm x)/\rho,&0<yf(\bm x)<\rho,\\
0507   0,&yf(\bm x)\geq\rho.
0508  \end{cases}
0509 \]
0510 它在错分时为1，在正确但间隔小于$\rho$时仍为正，取值于$[0,1]$、关于得分为$1/\rho$-Lipschitz，且支配零一损失。若$\|\bm w\|_2\leq B$、$\|\bm x\|_2\leq r$几乎处处成立，收缩引理将式~\eqref{eq:linear-rademacher-bound}转为损失复杂度$Br/(\rho\sqrt n)$。风险上界因而以至少$1-\delta$的概率同时覆盖所有这些线性得分：
0511 \begin{equation}

### tex/03-foundations/02-learning-theory/02-binary-classification.tex:528–550
0528 \begin{equation}
0529  R_{\mathcal P}(\hat h)-\inf_{h\in\mathcal H}R_{\mathcal P}(h)
0530  \leq4\mathfrak R_n(\mathcal G)
0531  +2\sqrt{\frac{\log(2/\delta)}{2n}}.
0532  \label{eq:rademacher-excess-risk}
0533 \end{equation}
0534 对固定分布，$\mathfrak R_n(\mathcal G)\to0$使输出风险以高概率趋近类内下确界。若有对全部允许分布成立的统一上界$\mathfrak R_n(\mathcal G)\leq a_n\to0$，才可从中选择分布无关的样本量，得到不可知PAC。单个分布上的小复杂度不等于这一统一保证。
0535 
0536 \subsection{高斯复杂度}
0537 
0538 把等幅随机符号换成标准高斯系数，可以从另一种随机相关和估计损失类复杂度。两种系数的幅度规律不同，需要先核对比较方向（可参考\BookDefinitionRef{def:gaussian-complexity}{第一卷“随机变量”章的高斯复杂度定义}及\BookSectionRef{sec:probability-uniform-errors-symmetry}{同章的“候选族累计量的统一偏差控制”一节}）。对独立标准高斯系数$\xi_i$，本章使用单侧\term{经验高斯复杂度}（empirical Gaussian complexity）
0539 \[
0540  \widehat{\mathfrak G}_S(\mathcal G)
0541  =\mathbb E_\xi\left[\sup_{g\in\mathcal G}\frac1n\sum_i \xi_i g(z_i)\right].
0542 \]
0543 高斯幅度可变，而Rademacher幅度恒为1，二者一般不能双向由普适常数比较。将$\xi_i$写成$\sigma_i|\xi_i|$，由上确界的凸性得到$\widehat{\mathfrak G}_S(\mathcal G)\geq\sqrt{2/\pi}\,\widehat{\mathfrak R}_S(\mathcal G)$。若已有高斯上界$b(S)$，便得Rademacher上界$\sqrt{\pi/2}\,b(S)$，可代入式~\eqref{eq:empirical-rademacher-risk-bound}。
0544 
0545 将这种比较代入经验风险式，就得到以高斯复杂度表示的总体风险上界。
0546 
0547 \begin{theorem}[高斯复杂度给出的期望风险上界]
0548 \label{thm:gaussian-risk-bound}
0549 设$(Z,\mathcal A)$为可测空间，$\mathcal P$为$Z$上的概率分布，$n\geq1$，
0550 $S=(z_1,\ldots,z_n)\sim\mathcal P^n$。令

### tex/03-foundations/02-learning-theory/02-binary-classification.tex:908–937
0908 \end{proof}
0909 
0910 这项构造可处理无限基空间，依靠的是有限VC与全可实现分布上的统一弱优势。有限VC并不单独保证能够弱学任意目标空间$\mathcal H$，优势条件须另证；各轮错误也没有被假定独立\scite{shalevshwartz2014}。
0911 
0912 证明先按精度固定$T$，再选充分样本量。无限VC基空间，或固定样本量任意增轮，都不能直接套这个结论；经验损失继续下降仍需额外复杂度控制。噪声还可能使某轮重加权分布失去弱优势，故可实现提升不能原样改成不可知保证。
0913 
0914 \subsection{估计期望风险}
0915 
0916 轮数计数可能高估实际投票的复杂度，可以改看归一化得分$f=\sum_ta_th_t$。其间隔$yf(x)$是正确权重减错误权重：正确权重0.9给间隔0.8，0.51给0.02。两者预测均正确，后者更接近改变符号的边界。这让我们用Rademacher复杂度研究投票的具体函数值。
0917 
0918 % 保留旧位置锚点；这里回顾投票得分所用的恒等式。
0919 \phantomsection\label{thm:learning-ensemble-convex-hull}
0920 对固定输入样本$S_X=(x_1,\ldots,x_n)$和非空有界基函数类$\mathcal B$，有限非负归一化加权不会增大单侧Rademacher复杂度：
0921 \[
0922  \widehat{\mathfrak R}_{S_X}(\operatorname{conv}(\mathcal B))
0923  =\widehat{\mathfrak R}_{S_X}(\mathcal B)
0924 \]
0925 （可参考\BookTheoremRef{thm:ensemble-convex-hull}{第一卷“随机变量”章的凸组合Rademacher复杂度定理}）。这里控制的是归一化得分，而不是取符号后的分类器。接下来通过间隔损失把这项得分控制转为零一风险保证。
0926 
0927 在抽样前固定$\rho>0$，使用前述支配零一损失、得分Lipschitz常数为$1/\rho$的$\ell_\rho$。收缩引理将得分凸包的复杂度转为损失复杂度，再用经验Rademacher风险界，便以至少$1-\delta$的概率对所有$f\in\operatorname{conv}(\mathcal B)$同时得到
0928 \begin{equation}
0929  R_{\mathcal P}^{01}(\operatorname{sign}f)
0930  \leq\frac1n\sum_i\ell_\rho(f(x_i),y_i)
0931  +\frac{2}{\rho}\widehat{\mathfrak R}_{S_X}(\mathcal B)
0932  +3\sqrt{\frac{\log(2/\delta)}{2n}}.
0933  \label{eq:ensemble-margin-bound}
0934 \end{equation}
0935 固定标签乘$y_i$保持符号分布，故复杂度在输入样本上计算。这个链条先控制实值得分，再经间隔损失控制风险，没有直接把凸包复杂度等同于阈值分类类的复杂度。
0936 
0937 凸包等式未依赖基假设总数，故上界也可用于无限基类。例如$\mathcal B\subseteq\{-1,1\}^X$、VC维$d$满足$1\leq d\leq n$时，固定样本上的每个预测向量欧氏范数为$\sqrt n$；应用有限向量类的Rademacher界及Sauer--Shelah引理，得到
