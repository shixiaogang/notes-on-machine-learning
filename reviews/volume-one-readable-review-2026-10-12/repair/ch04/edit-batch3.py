from pathlib import Path
p=Path('tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/04-optimization.tex'); s=p.read_text()
def sub(a,b):
 global s
 assert a in s,a[:70]
 s=s.replace(a,b,1)
sub('在凸光滑且步长适当时，共同样本的梯度\n更新由刚才的证明为非扩张映射，从而去掉前式中的膨胀因子。','若进一步假设两组数据的每个样本损失都凸，且$0\\leq\\eta^{(t)}\\leq2/L$，\n每个样本的梯度更新由刚才的证明为非扩张映射，从而去掉前式中的膨胀因子。经验目标凸本身不足以替代逐样本凸性。')
sub('参数接近与预测或损失接近仍需这一接口。这称为\n\\term{算法稳定性}（algorithmic stability）：训练集改动一个样本时，输出不会变化太大。',r'''参数接近与预测或损失接近仍需这一接口。这给出\term{算法稳定性}（algorithmic stability）的一种具体界：
对固定的相邻数据集$S,S'$，在两条轨迹使用相同随机索引的耦合下，算法随机性所产生的
期望参数距离不超过$(2G/n)\sum_{t<T}\eta^{(t)}$；固定测试样本上的期望损失差绝对值
不超过这个量乘以$K$。这里没有对数据集或测试样本再取平均。
若要使上界对所有相邻数据集和所有测试样本统一成立，还须使$L,G,K$及步长条件在这些对象上统一成立。''')
sub('均值为零；这展示了偏差怎样产生。对更新式直接减去\n$\\eta\\lambda\\bm{w}$的权重衰减，在普通梯度下降中等价于$\\ell_2$惩罚；使用坐标自适应缩放\n时，两者通常不再等价。',r'''均值为零；这展示了偏差怎样产生。第~\ref{sec:opt-penalty-methods}节比较过的权重衰减也会改变更新：
若本来要对$f+\lambda\|\bm w\|_2^2/2$作预条件更新，却使用直接衰减，
实际方向相对预期方向多出$\lambda(\bm I-\bm P)\bm w$。这是一项确定差异，增加抽样批量无法消除。

前面的稳定性界需要沿途梯度范数上界$G$。当样本损失非负且光滑时，可以改从沿途损失值取得这项控制：
若$\ell(\bm w)\leq B$，下面的引理给出$\|\nabla\ell(\bm w)\|_2\leq\sqrt{2LB}$。
它只在损失值已有上界的点上提供梯度界，不声称所有光滑损失的梯度都全局有界。''')
sub('固定权重找的是目标像某个支撑方向的最优点；\n非凸Pareto前沿的某些点无法由任何固定权重得到。',r'''把所有可行方案的损失向量放在一起，得到目标像$\bm f(C)=\{(f_1(\bm w),f_2(\bm w)):\bm w\in C\}$；
其中不被其他向量支配的部分称为Pareto前沿。固定权重后，等值线
$\alpha u+(1-\alpha)v=c$以权重向量为法向量，最小化加权损失就是寻找与目标像相交的最低等值线。
这条线只接触目标像在该方向上的支撑点，可能漏掉非凸前沿中的其他Pareto点。''')
sub('有些决策必须先经过一次学习过程才能评价。令外层变量为$\\bm{\\theta}$。如果内层问题有','有些决策必须先经过一次学习过程才能评价。令外层变量为$\\bm\\theta\\in\\Theta\\subseteq\\mathbb R^p$，\n其中$\\Theta$是给定的非空允许集合，内层变量取遍$\\mathbb R^d$。如果内层问题有')
sub('上的最小、最大外层损失定义为乐观、悲观值，也可以给定由初始化和算法路径决定的单值\n选择规则。','上的外层损失下确界、上确界分别定义为乐观、悲观值；只有相应极值达到时，才可写成最小值、最大值。\n也可以给定由初始化和算法路径决定的单值选择规则。')
sub('这就是\\term{双层优化}（bilevel optimization）。','外层要解的是$\\min_{\\bm\\theta\\in\\Theta}J(\\bm\\theta)$；上述记号还要求每个允许的$\\bm\\theta$都有可选的内层最小点。\n这种把另一优化问题的解作为评价输入的问题称为\\term{双层优化}（bilevel optimization）。')
sub('外层梯度再把这个Jacobian与\n$\\nabla_{\\bm{w}}L_{\\mathrm{out}}$相乘，并加上外层目标对$\\bm{\\theta}$的直接偏导。\n截断某一步会删除相应乘积项，因而改变所求导的算法，而不只是节省存储。',r'''记有限步外层目标为$J_T(\bm\theta)=L_{\mathrm{out}}(\bm w^{(T)}(\bm\theta),\bm\theta)$。
由于$\bm D_T=d\bm w^{(T)}/d\bm\theta$是$d\times p$矩阵，列梯度的链式法则为
\[
 \nabla_{\bm\theta}J_T
 =\bm D_T^\top\nabla_{\bm w}L_{\mathrm{out}}
  +\nabla_{\bm\theta}L_{\mathrm{out}},
\]
右侧两项都在$(\bm w^{(T)},\bm\theta)$计算，第二项固定$\bm w$求偏导；转置后两项都是$p$维列向量。
减少前向更新步数会改变$J_T$。若仍运行相同的$T$步，只截断反向导数传播，
前向目标不变，但Jacobian中的部分乘积项被舍去，通常得到同一$J_T$的近似梯度。''')
sub('外层仍取$(w-1)^2/2$，在$\\theta=2$有$w^{(2)}=3/2$，','本例另取外层损失$(w-1)^2/2$，它不直接依赖$\\theta$。在$\\theta=2$有$w^{(2)}=3/2$，')
p.write_text(s)
