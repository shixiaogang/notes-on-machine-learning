from pathlib import Path
p=Path('tex/01-mathematical-preliminaries-upper/01-mathematical-language-combinatorics-analysis-optimization/04-optimization.tex'); s=p.read_text()
def sub(a,b):
 global s
 assert a in s,a[:70]
 s=s.replace(a,b,1)
sub('用它判断对偶下界能否达到原最优值；这里给出完整条件，不把证明提要当作已完成的证明。','用它判断对偶下界能否达到原最优值。')
sub('线性规划的强对偶可以从一个不可行证书推出。先建立所需的择一定理',r'''共轭也能直接计算对偶下界。例如对单一等式约束问题
$\min_{\bm w}\{f(\bm w):\bm a^\top\bm w=b\}$，固定乘子$\nu$后有
\[
 q(\nu)=\inf_{\bm w}\{f(\bm w)+\nu(\bm a^\top\bm w-b)\}
       =-f^*(-\nu\bm a)-\nu b.
\]
最后一步来自把下确界取负后改写成共轭的上确界，因此不必先求出内层最小点。
若$f(\bm w)=\|\bm w\|_2^2/2$且$\bm a\neq0$，逐坐标配方给$f^*(\bm y)=\|\bm y\|_2^2/2$，
于是$q(\nu)=-\nu^2\|\bm a\|_2^2/2-\nu b$。
它在$\nu^\star=-b/\|\bm a\|_2^2$达到$b^2/(2\|\bm a\|_2^2)$；
原始可行点$\bm w^\star=b\bm a/\|\bm a\|_2^2$也取这个值，故弱对偶就足以认证双方最优。
共轭在这里计算下界，双共轭说明闭凸函数不会在收集全部仿射下界时损失函数值；
但对某个约束问题是否零间隙，仍须像这个例子一样另外核验。

接下来改用有限生成锥研究线性约束的可行性。线性规划的强对偶将由不可行证书推出，
不以双共轭等式代替证明。先建立所需的择一定理''')
sub('最优值下降率正是预算乘子的相反数。','最优值对预算的变化率是预算乘子的相反数，即预算增加$\\Delta\\tau>0$时，最优值的一阶下降量为$\\alpha_{\\mathrm{bud}}^\\star\\Delta\\tau$。')
a='''一般地，设问题依赖参数$\\tau$，活跃集在邻域内不变，把驻点条件、等式和活跃约束写成
$\\bm{\\Phi}(\\bm{w},\\bm{\\nu},\\bm{\\alpha},\\tau)=\\bm{0}$。若$\\bm\\Phi$连续可微，且对前三组变量的Jacobian
矩阵可逆，则第~\\ref{chap:mathematical-analysis}章的隐式求导给出'''
b=r'''一般地，设问题依赖参数$\tau$，在一个局部极小点附近固定活跃不等式的指标集$I$。
未活跃乘子恒为零，只把$\bm\alpha_I$作为未知量。将驻点条件、全部等式和活跃不等式的等号条件写成
$\bm\Phi(\bm w,\bm\nu,\bm\alpha_I,\tau)=\bm0$，方程数与未知量数都是$d+m+|I|$。
记这一局部分支为$(\widehat{\bm w},\widehat{\bm\nu},\widehat{\bm\alpha}_I)$。
若$\bm\Phi$连续可微，且对这三组未知量的Jacobian可逆，则第~\ref{chap:mathematical-analysis}章的隐式求导给出'''
sub(a,b)
sub(r'\begin{bmatrix}\bm{w}^{\star}\\\bm{\nu}^{\star}\\\bm{\alpha}^{\star}\end{bmatrix}',r'\begin{bmatrix}\widehat{\bm w}\\\widehat{\bm\nu}\\\widehat{\bm\alpha}_I\end{bmatrix}')
sub(r'{\partial(\bm{w},\bm{\nu},\bm{\alpha})}',r'{\partial(\bm{w},\bm{\nu},\bm{\alpha}_I)}')
sub('更具体地，若目标与约束二阶连续可微，活跃约束Jacobian$\\bm A_I$满行秩，','更具体地，若目标与约束二阶连续可微，记全部等式与活跃不等式的梯度行共同组成$\\bm A_I$，并设它满行秩，')
sub('对最优值应用链式法则并用KKT平衡消去解导数，便得\n$\\partial V/\\partial\\tau_k=-\\alpha_k^\\star$；',r'''定义局部分支值$\widehat V(\bm\tau)=f(\widehat{\bm w}(\bm\tau))$。
对它应用链式法则，并用KKT平衡及活跃约束的导数消去解导数，便得
$\partial\widehat V/\partial\tau_k=-\widehat\alpha_k$，其中未活跃乘子取零。
只有该分支继续为全局最优时，$\widehat V$才等于全局最优值$V$；例如凸问题中满足KKT即可保证这一点。''')
sub('得到更大的多面体，计算较容易而界更松。也可以把乘积$x_ix_j$提升为矩阵变量并要求某个\n块矩阵半正定，得到半正定松弛；它利用二次一致性，代价是矩阵锥约束更昂贵。',r'''得到更大的多面体，计算较容易而界更松。若原问题还含乘积$x_ix_j$，可以引入对称矩阵$\bm X$，
用$X_{i,j}$代替这个乘积。精确表达要求$\bm X=\bm x\bm x^\top$，这是非凸的等式。
将它放宽为
\[
 \begin{bmatrix}1&\bm x^\top\\\bm x&\bm X\end{bmatrix}\succeq0
 \quad\Longleftrightarrow\quad \bm X-\bm x\bm x^\top\succeq0
\]
就得到一种半正定松弛。等价性可由二次型配方核对：该块矩阵在$(t,\bm v)$上的值为
$(t+\bm x^\top\bm v)^2+\bm v^\top(\bm X-\bm x\bm x^\top)\bm v$。
精确乘积总满足新约束，但新约束允许$\bm X$与真实乘积有偏差；原来的其他约束也必须保留或相应转换。
新增矩阵有$O(d^2)$个元素，因而它改善界的可能性伴随着更高的存储和锥约束求解成本。''')
sub('它在当前点切触并全局上界$F$；精确最小化$Q$恰好得到步长$1/L$的梯度更新。','它在当前点切触并全局上界$F$。若$C=\\mathbb R^d$，精确最小化$Q$恰好得到步长$1/L$的梯度更新；\n若$C$是非空闭凸集，配方后得到的是$\\Pi_C(\\bm w^{(t)}-\\nabla F(\\bm w^{(t)})/L)$，即投影梯度。')
p.write_text(s)
