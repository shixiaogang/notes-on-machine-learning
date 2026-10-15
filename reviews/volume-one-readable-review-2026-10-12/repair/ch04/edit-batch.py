from pathlib import Path
p=Path('tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/04-optimization.tex')
s=p.read_text()
def sub(a,b):
 global s
 assert a in s, a[:100]
 s=s.replace(a,b,1)
sub('资源约束使最优点处的目标梯度不必为零，因为可行方向受到限制。对','资源约束使最优点处的目标梯度不必为零，因为可行方向受到限制。考虑以下问题：')
sub('  g_k(\\bm{w})\\leq0\\ (k=1,\\ldots,p),','  g_k(\\bm{w})\\leq0\\ (k=1,\\ldots,p)。')
sub('线性无关性使补充后的Jacobian可逆。','把这些线性无关的梯度行向量扩充为$\\mathbb R^d$的一组基，再把新增行作为$\\bm z(\\bm w)$的系数，\n就使$\\bm D\\bm T=[\\bm D\\bm a;\\bm D\\bm g_I;\\bm D\\bm z]$在当前点可逆。')
sub('局部最优时，自由坐标偏导为零，活跃不等式坐标只能朝负方向移动，\n故相应目标偏导非正。取$\\nu_j$为等式坐标偏导的相反数、',r'''记新坐标中的目标为$\widetilde f=f\circ\bm T^{-1}$。局部最优时，自由坐标$\bm z$的偏导为零；
活跃不等式坐标只能朝负方向移动，因此对应偏导必须非正，否则沿负方向就能降低目标。
链式法则将这些偏导还原到原坐标：
\[
 \nabla f=(\bm D\bm a)^\top\nabla_{\bm a}\widetilde f
          +(\bm D\bm g_I)^\top\nabla_{\bm g_I}\widetilde f
          +(\bm D\bm z)^\top\nabla_{\bm z}\widetilde f.
\]
最后一项为零。取$\nu_j$为等式坐标偏导的相反数、''')
sub('给出原问题最优值的下界。最大化这个下界得到对偶问题。由构造立即有\n$d^{\\star}\\leq p^{\\star}$，称为\\term{弱对偶}（weak duality）；差\n$p^{\\star}-d^{\\star}$称为对偶间隙。',r'''给出原问题最优值的下界。我们希望在所有允许的乘子中找到最高的下界，因此定义
\[
 p^\star=\inf_{\bm w:\,\bm a(\bm w)=0,\,\bm g(\bm w)\leq0}f(\bm w),\qquad
 d^\star=\sup_{\bm\nu\in\mathbb R^m,\,\bm\alpha\geq0}q(\bm\nu,\bm\alpha).
\]
这里用下确界和上确界，不预先假定最优点或最优乘子存在。
由构造立即有$d^{\star}\leq p^{\star}$，称为\term{弱对偶}（weak duality）；
两者均有限时，差$p^{\star}-d^{\star}$称为对偶间隙。''')
sub('\\end{definition}例如平面中的线段没有二维内部','\\end{definition}\n\n例如平面中的线段没有二维内部')
sub('本章采用如下Slater版本。设$f$和不等式函数$g_k$都是适当凸函数，即它们不恒为','严格可行点提供了一个不会立即碰到不等式边界的比较位置。下面引用Slater定理的一种有限维版本，\n用它判断对偶下界能否达到原最优值；这里给出完整条件，不把证明提要当作已完成的证明。\n\\begin{theorem}[Slater条件下的强对偶]\n设$f$和不等式函数$g_k$都是适当凸函数，即它们不恒为')
a='''并且原问题最优值有限，则原、对偶最优值相等，且存在最优对偶乘子。证明把可达到的
“约束余量与目标值”集合与严格低于原最优值的点分离；在等式可达的仿射子空间中进行分离，
可先排除冗余等式产生的法向量。相对内部中的严格可行点排除了
目标系数为零的异常分离向量，归一化后便得到所需乘子。这里列出的定义域、仿射等式和
有限最优值都是所采用版本的一部分。凸性本身并不够，也不能把前面的线性规划证明原样
套到任意凸问题。'''
b='''并且原问题最优值有限，则原、对偶最优值相等，且存在最优对偶乘子。
\\end{theorem}
共同定义域$D$是这些函数都取有限值的区域。相对内部允许$D$落在低维仿射空间中；
严格不等式要求在这个空间内仍有可行余量。这个条件保证存在有限乘子，足以把最优下界抬到原最优值，
但不保证原始最小点存在。其一般证明需要凸集的一般分离结论，并处理约束值与目标值组成集合的边界；
这类集合未必闭，不能直接套用前面仅针对闭凸集外一点的严格分离定理。
本章不展开这一证明，后面使用时逐项核对这里列出的共同定义域、仿射等式、严格可行点及有限最优值。'''
sub(a,b)
sub('于是$\\nabla q(\\bm y)=\\bm A\\bm w(\\bm y)-\\bm b$。',r'''这个距离界还可证明$q$确实可微。令$\bm h=\bm y'-\bm y$，
分别把$\bm w(\bm y)$、$\bm w(\bm y')$作为另一内层问题的候选，得到
\[
 \langle\bm A\bm w(\bm y')-\bm b,\bm h\rangle
 \leq q(\bm y')-q(\bm y)
 \leq\langle\bm A\bm w(\bm y)-\bm b,\bm h\rangle.
\]
减去右侧线性主项后，余项绝对值至多为
$\|\bm A\|_2\|\bm w(\bm y')-\bm w(\bm y)\|_2\|\bm h\|_2
\leq\|\bm A\|_2^2\|\bm h\|_2^2/\mu$，是比$\|\bm h\|_2$更小的量。
因此$\nabla q(\bm y)=\bm A\bm w(\bm y)-\bm b$，即内层唯一解的约束残差。''')
p.write_text(s)
