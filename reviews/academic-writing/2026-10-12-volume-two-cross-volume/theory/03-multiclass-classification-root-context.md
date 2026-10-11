### tex/02-foundations/02-learning-theory/03-multiclass-classification.tex:38–99
0038 \[
0039  R_{\mathcal P}(\tilde h)\leq\sum_{j=1}^L e_j.
0040 \]
0041 将位风险目标定为$\varepsilon/L$、位学习失败预算定为$\delta/L$，两次并集分别得到类别风险与抽样成功概率，从而以至少$1-\delta$的概率使风险至多$\varepsilon$。位学习可共享样本，错误不必独立，只需共同样本量满足
0042 \[
0043  n\geq\max_{1\leq j\leq L}
0044  m_{\mathcal B_j}(\varepsilon/L,\delta/L).
0045 \]
0046 合成输出未必属于原$\mathcal H$。
0047 
0048 逐位学习在不可知情形不一定优化原任务。沿用三类编码，设输入恒定，正常、广告、诈骗的概率为0.40、0.35、0.25，候选为三个常量假设。第一位为1的概率0.60，第二位为1的概率0.65，各位最优都选1，合成诈骗后风险0.75；直接选正常的风险却为0.60。即使已知所有概率，逐位最优仍选错原任务的最优类别。逐位优化分别降低每个编码位的错误概率；多类零一损失只在整个标签正确时计0，其余一律计1。同一错误标签可能在两位上都出错，两项位损失便分别记错，而类别损失只记一次。两个优化目标因此并不相同。
0049 
0050 有限标签编码给出算法构造，学习保证还须控制诱导二类空间并合并位风险。无限标签无法由任何固定有限位数区分，上述有限次归约也不能直接使用。要直接判断原空间，我们转而分析它在有限输入上产生的预测结构。
0051 
0052 这里不能把“实现全部$|Y|^m$种预测”作为打散要求。有些空间在各输入只用两个标签，却已包含任意大的二类难题，要求用齐所有标签反而漏掉它。我们应先固定各输入的两种答案，再问能否独立切换；\term{Natarajan维}（Natarajan dimension）衡量可以维持这种自由选择的输入数。
0053 
0054 \section{有限标签空间及Natarajan维的边界}
0055 \label{sec:multiclass-dimensions}
0056 
0057 先限定$2\leq K=|Y|<\infty$。找出独立二元选择，再用其最大规模限制预测数，便能沿用前章的对称化与ERM风险比较。
0058 
0059 \subsection{Natarajan维}
0060 
0061 固定输入处的两种标签选择能够限制有限标签类的预测数。Natarajan打散要求先为每个输入固定两个不同答案，再由类中的函数实现这组标签对的全部独立选择；标签对可以随输入改变，却不能随待实现的模式改变（可参考\BookDefinitionRef{def:natarajan-dimension}{第一卷“计数与计算”章的Natarajan打散与维度定义}）。本章以$d_N(\mathcal H)$记可打散有限输入集大小的上确界。
0062 % 旧公式位置保留为导航锚点，不再重复通用定义式。
0063 \phantomsection\label{eq:learning-natarajan-shattering}
0064 
0065 这一条件不要求标签有限。二类时各处的不同标签对只能取那两个答案，故它退化为VC维。维度0说明各输入预测唯一；可打散点集没有有限规模上界时，维度为无穷。这里继续把所得维度接到预测计数。
0066 
0067 \subsection{有限标签的一致收敛}
0068 
0069 固定输入后先合并相同预测。令
0070 \[
0071  V(x_1,\ldots,x_m)
0072  =\{(h(x_1),\ldots,h(x_m)):h\in\mathcal H\}.
0073 \]
0074 再对输入选择取上确界，得到生长函数
0075 \[
0076  \Pi_{\mathcal H}(m)=\sup_{(x_1,\ldots,x_m)\in X^m}|V(x_1,\ldots,x_m)|.
0077 \]
0078 这与第~\ref{sec:binary-growth-sauer}节的二类计数步骤相同，区别是每坐标可取$K$个标签。Sauer--Shelah由VC限制二元数目，下面用Natarajan承担多类的对应职责。
0079 
0080 % 保留旧位置锚点；这里直接使用组合计数结论。
0081 \phantomsection\label{thm:learning-multiclass-growth-bound}
0082 当$2\leq K=|Y|<\infty$且$d=d_N(\mathcal H)<\infty$时，记$q=K(K-1)/2$为不同无序标签对的数目。对每个整数$m\geq0$，有限标签的计数界给出
0083 \[
0084  \Pi_{\mathcal H}(m)\leq G_{d,K}(m)
0085  :=\sum_{j=0}^{\min\{d,m\}}\binom mj q^j
0086 \]
0087 （可参考\BookTheoremRef{thm:multiclass-growth-bound}{第一卷“计数与计算”章的有限标签预测数目上界}）。在学习问题中，$G_{d,K}(2n)$将控制原样本与副样本合并后的不同损失模式数，因而能够进入下一步对称化后的失败概率。
0088 
0089 二类时$q=1$、$d_N=\operatorname{VC}(\mathcal H)$，求和回到Sauer--Shelah的$\sum_{j=0}^{\min\{d,m\}}\binom mj$。多类的$q^j$另计每个参与二元选择的坐标所用的标签对。
0090 
0091 固定$d,K$使上界至多多项式增长。样本标签一经固定，相同预测向量也给出相同损失向量，故这个计数控制经验风险分析中的不同结果。副样本与随机交换于是可以沿用。
0092 
0093 % 避免短定理在页末仅留下标题和半句条件。
0094 \begingroup
0095 \tcbset{lines before break=4}
0096 \begin{theorem}[有限标签的一致收敛保证]
0097 \label{thm:finite-label-uniform-convergence}
0098 设$(X,\mathcal X)$为可测空间，离散标签空间$Y$满足
0099 $2\leq|Y|=K<\infty$，$\mathcal H\subseteq Y^X$是由可测分类器组成的非空集合，

### tex/02-foundations/02-learning-theory/03-multiclass-classification.tex:195–217
0195 \[
0196  (a,u),\ (b,u),\ (b,v),\ (c,v),\ (c,w),\ (a,w),
0197 \]
0198 其中$a,b,c$互异，$u,v,w$互异。每个向量在每坐标都有只改该坐标的邻居，例如$(a,u)$的$(b,u)$和$(a,w)$。但任意两种第一标签至多共享一种第二标签，无法形成固定两对标签的四组合；Natarajan维仅1，两坐标却都留歧义。这一个有限类仍可学习，反例还需任意维的同类结构。
0199 
0200 图~\ref{fig:learning-theory-ds-neighbors}把这六种预测的邻接关系画成环。每个顶点都连接一条只改第一坐标的边和一条只改第二坐标的边，因此两坐标上的局部歧义可以同时保留；这种邻接条件不要求固定两对标签的四种组合全部出现。
0201 
0202 \begin{figure}[htbp]
0203   \centering
0204   \includegraphics[width=93.405mm]{figures/02-foundations/02-learning-theory/tikz/learning-theory-ds-neighbors/figure.pdf}
0205   \caption{六种预测的坐标邻接环。顶点为上文的六个向量，蓝色实线仅改变第一坐标，绿色虚线仅改变第二坐标；边没有方向。每个顶点在两个坐标上分别有邻居，却不存在固定两对标签的完整四种组合。因而这个两输入函数类的Natarajan维为1，后文分析的DS维为2；它仍是可学习的有限类，不能单独证明不可学习性。}
0206   \label{fig:learning-theory-ds-neighbors}
0207 \end{figure}
0208 
0209 若要从二维局部歧义得到不可学习性，需要任意维的对应构造。下面把$V_m$的向量视为坐标集$\{1,\ldots,m\}$上的函数，使其Natarajan维有明确对象。
0210 
0211 \begin{lemma}[低Natarajan维的局部邻接构造]
0212 \label{lem:low-natarajan-pseudocubes}
0213 对每个整数$m\geq1$，把$Y_m^m$中的向量视为定义在坐标集
0214 $\{1,\ldots,m\}$上的分类函数。存在非空有限标签集$Y_m$及有限非空函数集合
0215 $V_m\subseteq Y_m^{\{1,\ldots,m\}}$，使
0216 \begin{enumerate}
0217  \item $d_N(V_m)=1$；

### tex/02-foundations/02-learning-theory/03-multiclass-classification.tex:258–282
0258 
0259 \section{图维、DS维与一般标签空间}
0260 \label{sec:general-multiclass-dimensions}
0261 \label{sec:multiclass-sample-complexity}
0262 有限标签靠Natarajan的预测计数连接UC与学习。去掉标签数有限的条件后，第~\ref{sec:multiclass-erm-limitations}节已给维度有限却不可学习的例子。我们因此分别问：一份样本能否同时估准所有风险，以及是否存在算法选出低风险者？前者约束整个空间，后者只约束算法输出。
0263 
0264 零一风险只问是否匹配标签，图维因此可转为二值损失类的VC问题。学习器则可能利用标签携带的更多信息，DS维用预测之间单坐标变化描述剩余歧义。先建立图维与UC的关系，再分析为什么存在学习器是另一项要求。
0265 
0266 \subsection{一致收敛}
0267 
0268 零一损失把无限个错误答案都计为1，风险只看与真值是否匹配。为描述这一二元能力，我们先给每个输入固定参考答案$f(x)$，再问能否任意指定一组匹配位置。\term{图打散}（graph shattering）要求对每个位置子集都有类中函数恰在这些位置匹配参考，在其余位置全部偏离参考；偏离时使用的标签可以随模式改变（可参考\BookDefinitionRef{def:graph-dimension}{第一卷“计数与计算”章的图打散定义}）。
0269 
0270 可图打散有限输入集大小的上确界记为$d_G(\mathcal H)$（可参考\BookDefinitionRef{def:graph-dimension-value}{第一卷“计数与计算”章的图维定义}）。图打散只预定参考答案，Natarajan打散还预定每处的替代答案，因此后者推出前者，逆向未必成立。接下来利用“匹配或偏离”的二元模式，将图维转为零一损失类的VC维。
0271 
0272 风险要看匹配与否，故将各假设改写为$\mathcal L_{\mathcal H}=\{(x,y)\mapsto\mathbb I\{h(x)\neq y\}:h\in\mathcal H\}$。新函数以输入标签对为自变量，以0或1为输出。
0273 
0274 \begin{theorem}[图维与一致收敛]
0275 \label{thm:graph-uniform-convergence}
0276 设$(X,\mathcal X)$为可测空间，$Y$为取离散$\sigma$代数的非空标签空间，
0277 $\mathcal H\subseteq Y^X$是由可测分类器组成的非空集合，并令
0278 \[
0279  \mathcal L_{\mathcal H}
0280  =\{(x,y)\mapsto\mathbb I\{h(x)\neq y\}:h\in\mathcal H\}.
0281 \]
0282 则$\operatorname{VC}(\mathcal L_{\mathcal H})=d_G(\mathcal H)$。

### tex/02-foundations/02-learning-theory/03-multiclass-classification.tex:374–408
0374 让另一ERM在$n$条全$\star$记录时故意选$h_{A_S}$，其中$A_S=\{1,\ldots,2n\}\setminus\{x_1,\ldots,x_n\}$；其他可实现样本从集合标签恢复目标，不可实现样本则按固定顺序取前述有限候选的经验最小者。全$\star$样本上它零经验错，但目标为空、输入均匀于$\{1,\ldots,2n\}$时，至少$n$个未见输入被误判，风险至少$1/2$。任意$n$都有这样的来源，这个ERM不能分布无关PAC学习。
0375 \end{proof}
0376 
0377 好坏两算法在可实现样本上都达到零经验风险，区别在于怎样使用标签信息。这里“有成功学习器”不能由“所有ERM都成功”代替\scite{daniely2015multiclass}。第~\ref{sec:multiclass-erm-limitations}节的空间完全没有PAC学习器，这个空间则只是某些经验最优选择失败，两例承担不同边界。
0378 
0379 \subsection{DS维与可学习性}
0380 \label{sec:ds-dimension}
0381 
0382 集合标签例说明图维无限仍可学习，另一例的Natarajan维虽有限，却没有PAC学习器。所需充要结构应比固定标签对宽，又不要求全类风险估准。六预测例的线索是：即使知道其他输入的答案，遗漏位置也可能仍有竞争标签。
0383 
0384 为了描述遗漏坐标上的竞争答案，我们在限制类中寻找有限非空的预测集合$V\subseteq Y^m$。要求每个$v\in V$在每个坐标$i$上都有集合内的另一个向量$u$：它只改变该坐标的答案，其余全部坐标与$v$相同。这正是本章下界证明需要的\term{伪立方体}（pseudo-cube）条件（可参考\BookDefinitionRef{def:pseudocube}{第一卷“计数与计算”章的伪立方体定义}）。
0385 
0386 六种预测给二维伪立方体，全部二元$2^m$预测给$m$维伪立方体。多类不要求各坐标固定两种标签，却仍要求预测集合有限；无限邻接集的性质可能不同，不能删除这个条件。
0387 
0388 DS维寻找能保留上述逐坐标歧义的最大输入规模。对$m$个互异输入按固定次序组成的$C$，检查限制类$\mathcal H|_C$是否含$m$维伪立方体；满足条件的有限输入规模取上确界，记为$d_{DS}(\mathcal H)$（可参考\BookDefinitionRef{def:ds-dimension}{第一卷“计数与计算”章的DS维定义}）。下面考察它如何决定学习。
0389 
0390 图~\ref{fig:learning-theory-ds-neighbors}展示第~\ref{sec:multiclass-erm-limitations}节的六种预测，两种线型分别表示只改变一个坐标的邻接。每个顶点在两个坐标上均有邻居，所以这个两输入类的DS维为2；环缺少固定两标签对的完整四种组合，所以Natarajan维仅1。这个有限类仍可学习；无限标签下的不可学习反例还依赖任意维的局部构造及其在同一假设空间中的合并。
0391 
0392 在$m-1$个坐标已知时，剩余邻居使遗漏标签未定。对每个向量、每个坐标都要求邻居，避免仅在个别向量周围留少量分支。固定标签对、固定参考答案与逐坐标邻接因而是不同要求；图中的一段邻接关系只有扩展到有限集合内的每个向量和每个坐标，才满足完整伪立方体条件（可参考\BookSectionRef{sec:comb-multiclass-dimensions}{第一卷“计数与计算”章的“多值函数族的容量”部分}）。
0393 
0394 % 保留旧位置锚点；通用维度比较引用卷一。
0395 \phantomsection\label{thm:learning-multiclass-dimension-comparison}
0396 这些结构满足$d_N(\mathcal H)\leq d_{DS}(\mathcal H)\leq d_G(\mathcal H)$；二标签时三者均等于VC维。有限标签空间下，Natarajan维有限还蕴含图维有限（可参考\BookTheoremRef{thm:multiclass-dimension-comparison}{第一卷“计数与计算”章的多分类维度比较定理}）。这里使用三个关系：固定标签对的全部组合构成伪立方体；逐坐标邻接支持图打散；有限标签的指数图模式又受多项式预测计数限制。
0397 
0398 有限标签的更精细界为$d_G=O(d_N\log K)$，不能外推无限$Y$。第~\ref{sec:multiclass-erm-limitations}节的不可学习反例有$d_N=1,d_{DS}=\infty$，故第一道维度差可以无穷。集合标签类$\mathcal H_C$则有$d_{DS}=1$：出现非$\star$的向量唯一确定假设，不能在别的坐标留邻居，全$\star$独自也不是伪立方体。结合单点可打散得维度1，而图维无限，故第二道也不能反向替换。
0399 
0400 任意坐标都留竞争答案，使未见位置无法由其他标签唯一确定。若任意大的有限输入集都具有这项结构，就能为每个样本量构造学习失败的概率下界。
0401 
0402 \begin{theorem}[无限DS维的不可学习性]
0403 \label{thm:infinite-ds-lower-bound}
0404 设$(X,\mathcal X)$为可测空间，$Y$为离散标签空间，
0405 $\mathcal H\subseteq Y^X$是由可测分类器组成的非空集合，并采用零一损失。
0406 若$d_{DS}(\mathcal H)=\infty$，则对每个整数$n\geq1$及任意可测学习算法$A$
0407 （允许内部随机性，并允许输出$\mathcal H$之外的可测分类器），都存在
0408 $X\times Y$上的联合分布$\mathcal P$及$h^\star\in\mathcal H$，使

### tex/02-foundations/02-learning-theory/03-multiclass-classification.tex:527–549
0527  \item $\mathcal H$不可知PAC可学习。
0528 \end{enumerate}
0529 此外，$d_G(\mathcal H)<\infty$当且仅当零一损失满足分布无关的一致收敛；
0530 有限图维或一致收敛中的任一条件均蕴含前三条，但一般不存在反向蕴含。
0531 \end{theorem}
0532 
0533 \begin{proof}[证明（使用有限DS维的学习器构造结果）]
0534 DS有限时，当样本量足够大，定理~\ref{thm:finite-ds-learning-rates}的两项风险界可分别满足任意给定的误差容限和失败概率要求，因而给出两种分布无关PAC保证。不可知包含可实现，而无限DS已排可实现，故三项等价。图维/UC等价见定理~\ref{thm:graph-uniform-convergence}，学习不推UC由定理~\ref{thm:multiclass-erm-separation}的集合标签例证明。充分性仍依赖已引用的外部学习构造。
0535 \end{proof}
0536 
0537 一般多类有两项刻画：图维有限等价于零一UC，DS维有限等价于PAC学习器存在。前者推后者，逆向失败。有限标签使$d_N,d_{DS},d_G$有限性、UC及两种PAC全部等价；二类时三维都回到VC。有限标签的学习等价见定理~\ref{thm:finite-label-learnability}（维度关系可参考\BookTheoremRef{thm:multiclass-dimension-comparison}{第一卷“计数与计算”章的多分类维度比较定理}）。
0538 
0539 定性维度有限没有确定最优样本量或高效实现，不能在二类样本式中只换VC为DS便得新公式。
0540 
0541 \section{可计算PAC学习}
0542 \label{sec:computable-multiclass-learning}
0543 
0544 \subsection{统计保证与程序实现}
0545 
0546 沿用第~\ref{sec:computable-binary-learning}节的三层区别：统计学习、训练预测总停机、多项式资源。现在标签程序返回$Y$中的值，仍须停机，风险成功标准保持前述PAC要求。
0547 
0548 取$X=\mathbb N$，沿用定义~\ref{def:binary-computable-pac}的程序要求，但须先给标签和假设有效表示：标签编码可计算、相等可判定，有限标签全集可枚举，允许假设及输出由预定可递归枚举表示提供。不可知学习器对每份有限样本停机，返回一个对每输入停机输出$Y$标签的程序，并对所有允许来源和所有足量$n$满足
0549 \[

### tex/02-foundations/02-learning-theory/03-multiclass-classification.tex:572–594
0572  R_{\mathcal P}(A(S))
0573  \leq\inf_{h\in\mathcal H}R_{\mathcal P}(h)+\varepsilon
0574  \right\}\geq1-\delta.
0575 \]
0576 因此，$\mathcal H$恰当地不可知CPAC可学习，且有可计算的样本量上界；概率仅来自
0577 独立同分布样本。若$2\leq|Y|<\infty$且标签全集可有效枚举，则条件
0578 $d_N(\mathcal H)<\infty$可以替代$d_G(\mathcal H)<\infty$。
0579 \end{theorem}
0580 
0581 \begin{proof}
0582 定理~\ref{thm:graph-uniform-convergence}将图维等同于损失VC维，因此给出显式UC样本界。取偏差$\varepsilon/2$，两次比较使ERM超额至多$\varepsilon$；训练和预测停机来自题设。固定空间的有限维上界可写入样本量程序。有限标签时，Natarajan维有限蕴含图维有限，所以可替条件（可参考\BookTheoremRef{thm:multiclass-dimension-comparison}{第一卷“计数与计算”章的多分类维度比较定理}）。
0583 \end{proof}
0584 
0585 这条充分路线与前章可计算ERM对应：二类用VC，多类用零一损失的图维，有限标签又可用Natarajan。维度有限若没有训练与预测程序，不能仅凭统计定理声称可计算。
0586 
0587 \subsection{可计算Natarajan维}
0588 
0589 Natarajan有限保证足量输入的固定标签对中有一种二元预测缺失；程序却需要实际找出它。\term{可计算Natarajan维}（computable Natarajan dimension）在这一组合存在性上增加总可执行的见证。
0590 
0591 \begin{definition}[可计算Natarajan维]
0592 \label{def:computable-natarajan-dimension}
0593 若存在总可计算程序$W$，对任意$d+1$个互异输入$x_i$及标签对$(a_i,b_i)$、
0594 $a_i\neq b_i$，都输出$s\in\{0,1\}^{d+1}$，使得
