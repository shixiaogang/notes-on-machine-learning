from pathlib import Path
import json,re
r=Path(__file__).parent
b=[x['text'] for x in json.loads((r/'02-v1-blocks.json').read_text())]
pat=r'\\begin\{(equation\*?|align\*?)\}[\s\S]*?\\end\{\1\}|\\\[[\s\S]*?\\\]'
def p(n,*ss):
 ms=list(re.finditer(pat,b[n-1])); assert len(ss)==len(ms)+1,(n,len(ss),len(ms))
 b[n-1]='\n'.join(s+t.group() for s,t in zip(ss,ms))+('\n' if ms else '')+ss[-1]
p(9,r'''将20\%推广为容限$\varepsilon$。取$Y=\{0,1\}$和$S\sim\mathcal P^n$，先固定$h\in\mathcal H$。若$R_{\mathcal P}(h)>\varepsilon$，它分对一次观测的概率小于$1-\varepsilon$；独立抽样使全部分对的概率连乘，得到
''',r'''这是固定假设的概率。ERM在抽样后才选择输出，须把其失败包含在“某个高风险假设仍与样本一致”的事件中，再对所有候选使用并集界。候选可能同时通过样本检验，并集界仍有效；有限的候选数因此转化为可计算的样本量。''')
p(11,r'''\begin{proof}
可实现性使ERM几乎必然与样本一致。输出风险若超过$\varepsilon$，至少一个高风险候选通过了全部观测的检验。由此
''',r'''将末项限制为$\delta$并解出$n$，即得式~\eqref{eq:finite-realizable-sample}。
\end{proof}''')
p(17,r'''先选阈值再抽样时，所选$h$固定不变，经验风险却因样本而变。对每条观测，零一损失是均值为$R_{\mathcal P}(h)$的Bernoulli变量；$n$个损失相互独立。Hoeffding不等式因此控制经验错误比例的偏差：
''',r'''这一界尚未覆盖抽样后选择的$A(S)$。若同时检验四个阈值，ERM根据四个经验风险选择输出；只保证其中一个阈值估计准确，仍可能选中另一个偏差较大的阈值。若四者的偏差都不超过$\eta$，输出风险就至多比类内最低风险高$2\eta$：输出自身的偏差用去一个$\eta$，参照假设的偏差再用去一个$\eta$。后文将证明这两次比较。图~\ref{fig:learning-uniform-convergence}以竖线显示各自偏差；全部竖线受控时，样本选出的输出也受控。''')
b[17]=b[17].replace('固定一个假设与同时考察全部假设的区别。即使某个假设的经验风险接近其期望风险，\n  ERM仍可能选中其他估计偏差较大的假设。若全部竖线都短，框中由样本选出的假设也有保证。','单个风险估计与共同保证。竖线连接各假设的经验风险与期望风险；只限制其中一条线，不能覆盖ERM在框中选择的输出。限制全部竖线后，这个数据依赖输出也落在保证内。')
p(21,r'''有限类的上确界是有限个可测随机变量的最大值。无限类则须处理整个零一损失函数类
''',r'''本章采用第~\ref{sec:learning-problem}节给出的可测性与可分性条件，使相关上确界和比较事件可测。压缩、重构与学习器的数据依赖映射也须可测。可实现样本可选与它一致的成员，其他存在性论证采用该约定中的可测近似ERM；缺少这些条件时，以下结论不能直接沿用。''')
p(27,r'''\begin{proof}
对每个$h$使用式~\eqref{eq:hoeffding-fixed-hypothesis}。上确界超过$\eta$等价于至少一个候选的偏差超过$\eta$；对这些事件求并集界，得到
''',r'''按式~\eqref{eq:finite-uniform-sample}选择$n$使右侧至多为$\delta$；或令右侧等于$\delta$，反解偏差$\eta$，得到式~\eqref{eq:finite-uniform-bound}。两种写法的样本要求均与具体$\mathcal P$无关。
\end{proof}''')
p(30,r'''\begin{proof}
将一致收敛容限设为$\eta=\varepsilon/2$。式~\eqref{eq:finite-agnostic-sample}使全部风险偏差不超过这个容限的概率至少为$1-\delta$。固定满足条件的样本，再取任意$h\in\mathcal H$；输出$\hat h$也在该空间内，两者均受偏差界约束。结合ERM的经验最优性，有
''',r'''首尾两次比较分别连接输出和参照的经验风险与总体风险，中间一次使用ERM。结论对任意$h$成立，取下确界即得所需保证。
\end{proof}''')
p(33,r'''在抽样前分配$\delta_k>0$，使$\sum_k\delta_k\leq\delta$，并对第$k$个空间设置偏差上界
''',r'''式~\eqref{eq:finite-uniform-bound}将第$k$个空间内的失败概率控制为$\delta_k$。再跨空间使用并集界，就以至少$1-\delta$的概率在同一份样本上得到
''',r'''这个共同事件覆盖后来选择的任意$(k,h)$，其期望风险都不超过经验风险加$p_k$。因此结构风险最小化可选择以下目标最小的组合：
''',r'''扩大$\mathcal H_k$或缩小$\delta_k$都会增大惩罚。一个具体分配为$\delta_k=\delta/[k(k+1)]$；由$1/[k(k+1)]=1/k-1/(k+1)$，总预算恰为$\delta$。''')
p(38,r'''\BookChapterRef{chap:combinatorics}{第一卷“数学准备”的“计数与计算”章}已建立打散、VC维、限制类$\mathcal H|_C$及\term{生长函数}（growth function）的定义。本章沿用记号
''',r'''它计算$m$个输入上最多可出现多少种二元预测。允许输入重复，因而有限输入空间也能使用任意$m$。第一卷给出阈值、单区间和平面仿射半空间的VC维$1,2,3$及前两类的精确生长函数；现在要将这些容量信息转为一致收敛和样本量保证，所需的组合上界如下。''')
b[39]=b[39].replace('令$G(m,d)$表示VC维至多为$d$的二分类假设空间在$m$个输入上能够实现的最大预测数。\n对$m+d$作强归纳。边界情形为$G(0,d)=1$；当$d=0$时，任意一个输入都不能同时取两个\n标签，所以$G(m,0)=1$。','以$G(m,d)$表示VC维至多为$d$时，$m$个输入上的最大预测数，对$m+d$强归纳。没有输入时$G(0,d)=1$；$d=0$时，每个输入的标签都唯一，故$G(m,0)=1$。')
p(41,r'''固定$m\geq1,d\geq1$及$m$个不同输入，令$V\subseteq\{0,1\}^{m}$收集预测向量。删除末坐标得到前缀集合$U$，另取能同时接上两种末标签的前缀
''',r'''每个$U$中前缀贡献一次扩展，$U'$中前缀额外贡献一次，所以$|V|=|U|+|U'|$。删除坐标不会增大VC维，故$U$的VC维至多为$d$；若$U'$能打散$d$个坐标，加入末坐标后$V$就能打散$d+1$个，矛盾，故$U'$的VC维至多为$d-1$。归纳假设给出
''',r'''用Pascal恒等式合并两和，并约定$j>m$时$\binom mj=0$，得到$G(m,d)\leq\sum_{j=0}^{d}\binom mj$。这证明第一道不等式。''')
p(42,r'''为把组合数和化为便于统计估计的表达，令$a=d/m\leq1$。在$j\leq d$时$a^j\geq a^d$，从而
''',r'''除以$a^d$即得第二道不等式。$d=0$时预测唯一，生长函数恒为1，应单独处理，避免使用以$d$作分母的公式。
\end{proof}''')
p(52,r'''\begin{proof}
引入独立副样本$S'\sim\mathcal P^n$。固定已发生原偏差事件的$S$，选$h$使$|R_{\mathcal P}(h)-\hat R_S(h)|>\eta$。条件于$S$及$h$后，副样本经验风险仍为$n$个独立Bernoulli损失的平均，故
''',r'''用Chebyshev不等式控制它相对真实风险的偏差：
''',r'''以至少$1/2$的条件概率，副样本偏差小于$\eta/2$，这时三角不等式使两份经验风险相差大于$\eta/2$。对原样本平均后得到
''','')
p(53,r'''固定两份样本的$2n$个观测，记配对为$(z_i,z_i')$。引入独立Rademacher符号，$\sigma_i=1$时保持该对，$\sigma_i=-1$时交换，形成$S_\sigma,S_\sigma'$。原样本独立同分布，随机交换保持联合分布；固定观测与$h$后的差值则为
''',r'''各项的取值区间长度至多$2/n$，Hoeffding给出尾界$2e^{-n\eta^2/8}$。固定输入上的预测向量至多$\Pi_{\mathcal H}(2n)$种，固定标签后每个预测向量确定一个损失向量。只对这些有限向量作并集界，得到
''',r'''先平均固定观测，再利用交换不改变联合分布，将这一界转回双样本差；乘上对称化的因子2，得到式~\eqref{eq:vc-symmetrization-probability}。代入Sauer--Shelah上界$\Pi_{\mathcal H}(2n)\leq(2en/d)^d$并解出失败概率$\delta$对应的偏差，即得式~\eqref{eq:vc-uniform-bound}。
\end{proof}''')
b[56]=r'''若VC维无限，任意$n$都能找到被打散的$2n$个输入。对任意算法，第~\ref{sec:no-free-lunch}节的定理在这些输入上给出一个可实现分布，使$n$个观测下的风险以固定正概率超过固定误差阈值。任意样本量都存在这样的分布，违反可实现PAC的统一要求，故可实现PAC可学习必有有限VC维。结合正向蕴含，四个命题等价。
\end{proof}'''
p(65,r'''\BookSectionRef{sec:probability-uniform-errors-symmetry}{第一卷“随机变量”章的“对称化与随机复杂度”一节}已定义随机复杂度并计算线性类。本章首先控制经验均值低估期望的方向，故使用不带绝对值的单侧版本。对$S=(z_1,\ldots,z_n)$与非空实值类$\mathcal G$，定义
''',r'''符号$\sigma_i$独立且等概率取$-1,1$，再对样本平均得到
''',r'''第一卷的带绝对值版本在取负封闭的类上与此相同，一般则不小于当前版本。使用收缩或比较结果时须按版本核对常数。''')
p(67,r'''对线性得分$f_{\bm w}(\bm x)=\bm w^\top\bm x$，随机相关和可写成$\bm w^\top\sum_i\sigma_i\bm x_i$。若参数不受限且后一个向量非零，这个量可任意增大，复杂度便不能给出有限控制。为此设$B>0$并限制$\|\bm w\|_2\leq B$，取$\mathcal F=\{\bm x\mapsto\bm w^\top\bm x:\|\bm w\|_2\leq B\}$，假定每个样本输入满足$\|\bm x_i\|_2\leq r$。以$S_X=(\bm x_1,\ldots,\bm x_n)$记输入样本，先计算得分复杂度：
''',r'''固定符号时，参数沿$\sum_i\sigma_i\bm x_i$方向取长度$B$即可达到最大内积。用均方范数的平方根上界期望范数，独立符号又使交叉项的期望为零，剩下$\sum_i\|\bm x_i\|_2^2$。上界虽未显式含维数，却依赖$B$和$r$受控；缺少半径约束时，不能宣称维数无关。''')
p(71,r'''\begin{proof}
令$\Phi(S)=\sup_{g\in\mathcal G}(\mathbb E g-n^{-1}\sum_i g(z_i))$，即经验均值在整个类上的最大低估。引入独立副样本，用“先选择函数再平均”上界“先平均再选择”，得
''',r'''对每对观测随机交换，将独立符号$\sigma_i$引入差值而不改变期望。把两样本和各自取上确界，再用$\sigma_i$与$-\sigma_i$同分布，得到
''','')
p(72,r'''替换一个观测使$\Phi(S)$最多变化$1/n$。有界差分不等式使它以至少$1-\delta$的概率不超过期望加$\sqrt{\log(1/\delta)/(2n)}$，结合上式证明第一界。经验Rademacher复杂度替换一个观测也至多变化$1/n$，所以以至少$1-\delta/2$的概率，
''',r'''再把第一界的失败预算设为$\delta/2$，两个事件的共同概率至少$1-\delta$。替换其中的期望复杂度并合并三项偏差，得到第二界。
\end{proof}''')
p(75,r'''将得分复杂度转为分类风险，还要选择损失。取$y\in\{-1,1\}$、$f(\bm x)=\bm w^\top\bm x$，则$yf(\bm x)$为带符号的分类间隔：正值表示方向正确，绝对大小在得分尺度上衡量距阈值0的距离。几何间隔还须除以$\|\bm w\|_2$。对固定$\rho>0$，用下列间隔损失同时惩罚错分和不足的正间隔：
''',r'''它在错分时为1，在正确但间隔小于$\rho$时仍为正，取值于$[0,1]$、关于得分为$1/\rho$-Lipschitz，且支配零一损失。若$\|\bm w\|_2\leq B$、$\|\bm x\|_2\leq r$几乎处处成立，收缩引理将式~\eqref{eq:linear-rademacher-bound}转为损失复杂度$Br/(\rho\sqrt n)$。风险上界因而以至少$1-\delta$的概率同时覆盖所有这些线性得分：
''',r'''这里$R_{\mathcal P}^{01}$采用零一损失，得分为0时的分类规则预先固定。若经验间隔损失为零，使右侧至多为$\varepsilon$的一项充分样本量为$O(((Br/\rho)^2+\log(1/\delta))/\varepsilon^2)$。控制量是范数与间隔的比值；高维而间隔较大时，它可能优于仅依据半空间VC维的保证。''')
p(77,r'''ERM还要比较输出与参照的两个风险，故需双侧偏差。将第一界分别应用于$\mathcal G$和$1-\mathcal G=\{1-g:g\in\mathcal G\}$，两者均取值于$[0,1]$。平移不改变总体与经验均值之差，符号对称性又给出$\mathfrak R_n(1-\mathcal G)=\mathfrak R_n(\mathcal G)$。各分配$\delta/2$后，以至少$1-\delta$的概率有
''',r'''沿用两次偏差比较，ERM的超额风险因此满足
''',r'''对固定分布，$\mathfrak R_n(\mathcal G)\to0$使输出风险以高概率趋近类内下确界。若有对全部允许分布成立的统一上界$\mathfrak R_n(\mathcal G)\leq a_n\to0$，才可从中选择分布无关的样本量，得到不可知PAC。单个分布上的小复杂度不等于这一统一保证。''')
p(79,r'''\BookSectionRef{sec:probability-uniform-errors-symmetry}{第一卷“随机变量”章的“对称化与随机复杂度”一节}还给出高斯复杂度及比较关系。对独立标准高斯系数$\xi_i$，本章取单侧\term{经验高斯复杂度}（empirical Gaussian complexity）
''',r'''高斯幅度可变，而Rademacher幅度恒为1，二者一般不能双向由普适常数比较。将$\xi_i$写成$\sigma_i|\xi_i|$，由上确界的凸性得到$\widehat{\mathfrak G}_S(\mathcal G)\geq\sqrt{2/\pi}\,\widehat{\mathfrak R}_S(\mathcal G)$。若已有高斯上界$b(S)$，便得Rademacher上界$\sqrt{\pi/2}\,b(S)$，可代入式~\eqref{eq:empirical-rademacher-risk-bound}。''')
b[81]=r'''\begin{proof}
将$g=g_h$代入式~\eqref{eq:empirical-rademacher-risk-bound}，再用$2\widehat{\mathfrak R}_S(\mathcal G)\leq\sqrt{2\pi}\,\widehat{\mathfrak G}_S(\mathcal G)$替换复杂度项，即得结论。
\end{proof}'''
p(97,r'''\begin{proof}
先固定一种描述$(I,u)$，其中$|I|=j\leq k$，而不条件于压缩算法选中它。给定$S_I$，重构$h_{I,u}=\rho(S_I,u)$已确定，余下$n-j$个观测仍独立服从$\mathcal P$。若其风险超过$\varepsilon$，这些观测全被分对的条件概率至多为
''',r'''再平均$S_I$，可知该固定描述同时导致高风险和全样本一致的概率至多$e^{-(n-k)\varepsilon}$。''')
p(98,r'''最终输出总由某个$(I,u)$重构，并与全样本一致。输出风险超过$\varepsilon$时，至少一种描述满足前述失败事件；对全部描述作并集界得到
''',r'''令右侧至多为$\delta$，取对数并整理即得式~\eqref{eq:compression-generalization}。若所列上界不小于1，零一风险本身至多为1已保证结论。
\end{proof}''')
p(99,r'''描述长度通过保留位置数与旁信息数进入分子，至少$n-k$个未保留观测则进入分母。$\log$为自然对数，故$b$比特计为$b\log2$。阈值方案取$k=1,b=0$，组合数和为$n+1$，得到
''',r'''在$n=100,\delta=0.05$时，右侧约为0.077，即以至少95\%的概率错误率不超过7.7\%。这是通用压缩界的充分保证，不能据此断言阈值的最优样本量需要$\log n$因子。''')
b[100]=r'''\begin{proof}
$k=0$时组合数和为1；固定$k\geq1$时，$\sum_{j=0}^k\binom nj\leq(k+1)n^k$。分子至多按$\log n$增长，分母按$n$增长，故任意给定$\varepsilon,\delta$都存在有限阈值，使此后所有$n$满足条件。将这些$n$代入前一定理，即得到分布无关的PAC风险保证。
\end{proof}'''
b[105]=r'''\begin{proof}
把被打散的$m$个输入按固定次序排列，全部$2^m$种标签对应可实现样本。大小$j$的保留集有$\binom mj$种，它的标签有$2^j$种，旁信息另有$2^b$种，合计为右侧的描述数。两份不同完整标签若压缩成同一描述，确定性的重构就须在某个输入给出两种标签，矛盾。故描述数至少$2^m$。固定$k,b$后，描述数随$m$至多多项式增长，无法始终覆盖指数增长的$2^m$，所以VC维有限。
\end{proof}'''
p(114,r'''以下使用$\{-1,1\}$标签，得分为0时预测1。取基假设$h_t:X\to\{-1,1\}$与非负权重$a_t$，满足$\sum_ta_t=1$，定义加权得分和最终分类器
''',r'''等权$a_t=1/T$给出多数投票。允许从$\mathcal B$选有限个基假设及上述权重，全部实值得分组成\term{凸包}（convex hull）$\operatorname{conv}(\mathcal B)$。凸包的成员是得分；应用符号阈值后才得到二分类假设，二者的容量不能直接等同。''')
b[116]=r'''\begin{proof}
条件于$(x,y)$，投票错误要求$T^{-1}\sum_tE_t\geq1/2$，而条件均值至多为$1/2-\gamma$。独立有界变量的Hoeffding不等式给出训练随机性下的错误概率$e^{-2T\gamma^2}$。再平均$(x,y)\sim\mathcal P$，即得期望风险界。
\end{proof}'''
p(119,r'''多个基假设可以用训练扰动产生。\term{装袋法}（bootstrap aggregating, bagging）对原样本有放回地重采样，分别训练后平均得分或投票，试图降低样本扰动造成的预测变化。在固定$x$处，设得分$F_t(x)$各有方差$v$、两两协方差为$c$，展开平均值方差得到
''',r'''$c=0$时方差降至$v/T$，$c=v$时则不降低。随机性来自训练数据与过程，各次重采样共享原样本，不能据此认定得分无条件独立。分类还依赖得分是否跨过0，得分方差降低也不能自动推出零一风险降低。随机森林另随机选择分裂特征，以形成预测不同的基假设，具体算法留待模型章节\scite{shalevshwartz2014}。''')
p(125,r'''沿用$-1,1$标签，$y_ih_t(x_i)=1$表示分对，$-1$表示分错。初始化$D^{(1)}(i)=1/n$，并以$D^{(t)}$表示第$t$轮总和为1的样本权重。获得$h_t$后计算$e^{(t)}=\sum_iD^{(t)}(i)\mathbb I\{h_t(x_i)\neq y_i\}$。若$0<e^{(t)}<1/2$，更新为
''',r'''其中$Z^{(t)}=\sum_iD^{(t)}(i)e^{-\alpha^{(t)}y_ih_t(x_i)}$将新权重归一化。$e^{(t)}=0$时已全样本一致，可输出$h_t$并停止；$e^{(t)}\geq1/2$时未取得所需优势。预先固定平局规则后，最终分类器为$H_T(x)=\operatorname{sign}(\sum_t\alpha^{(t)}h_t(x))$。''')
b[128]=r'''\begin{proof}
展开权重递推可得$D^{(T+1)}(i)=n^{-1}\exp(-y_i\sum_t\alpha^{(t)}h_t(x_i))/\prod_tZ^{(t)}$。样本$i$若被分错，带符号得分不大于0，指数项至少为1。对全部样本求和，利用$\sum_iD^{(T+1)}(i)=1$，便将经验错误率上界为$\prod_tZ^{(t)}$。按分对、分错两组计算$Z^{(t)}=2\sqrt{e^{(t)}(1-e^{(t)})}$，再用$\sqrt{1-4(\gamma^{(t)})^2}\leq e^{-2(\gamma^{(t)})^2}$得到末界。
\end{proof}'''
b[134]=r'''\begin{proof}
固定$m$个输入，每个基假设产生至多$\Pi_{\mathcal B}(m)$种预测，$T$列组成的预测矩阵因而至多$\Pi_{\mathcal B}(m)^T$种。对固定矩阵，将输入表示为$(h_1(x),\ldots,h_T(x))\in\mathbb R^T$，改变权重就是改变其上的线性分类器。该类包含于VC维为$T+1$的仿射半空间类，Sauer--Shelah引理将每个矩阵上的预测数控制为$(em/(T+1))^{T+1}$。乘上矩阵数即得第一式。'''
b[135]=r'''基类VC维为$d$时，代入$\Pi_{\mathcal B}(m)\leq(em/d)^d$再取对数得到第二式。固定$d,T$后，上界对$m$至多多项式增长，不能达到任意大$m$所需的$2^m$，投票类因而具有有限VC维。$d=0$时基类各点预测唯一，仍可由第一式作同样判断。
\end{proof}'''
p(139,r'''\begin{proof}
给定$\varepsilon,\delta$，先于原样本抽取固定$T=\lceil\log(2/\varepsilon)/(2\gamma^2)\rceil$。定理~\ref{thm:vote-growth-infinite}保证$\mathcal V_T$的VC维有限，因此可选分布无关的原样本量$n$，使下列共同偏差事件的概率至少为$1-\delta/2$：
''','')
b[140]=r'''两类成功事件相交时，经验风险至多$\varepsilon/2$且输出在$\mathcal V_T$内，期望风险便至多$\varepsilon$。若提前找到零经验风险基假设，将其他权重取零也使它属于$\mathcal V_T$。两类失败预算相加至多$\delta$，包含原样本、重抽样及内部随机性，故得到PAC保证。
\end{proof}'''
p(147,r'''\begin{proof}
固定随机符号，相关和关于函数值线性。任意凸组合都满足
''',r'''反向由$\mathcal B\subseteq\operatorname{conv}(\mathcal B)$得到，故上确界相等；再平均符号即得结论。
\end{proof}''')
p(148,r'''在抽样前固定$\rho>0$，使用前述支配零一损失、得分Lipschitz常数为$1/\rho$的$\ell_\rho$。收缩引理将得分凸包的复杂度转为损失复杂度，再用经验Rademacher风险界，便以至少$1-\delta$的概率同时得到
''',r'''固定标签乘$y_i$保持符号分布，故复杂度在输入样本上计算。这个链条先控制实值得分，再经间隔损失控制风险，没有直接把凸包复杂度等同于阈值分类类的复杂度。''')
p(149,r'''凸包等式未依赖基假设总数，故上界也可用于无限基类。例如$\mathcal B\subseteq\{-1,1\}^X$、VC维$d$满足$1\leq d\leq n$时，固定样本上的每个预测向量欧氏范数为$\sqrt n$；应用有限向量类的Rademacher界及Sauer--Shelah引理，得到
''',r'''无限多个函数在固定样本上的表现因而可由有限预测数控制。代入式~\eqref{eq:ensemble-margin-bound}，复杂度项至多为$\frac{2}{\rho}\sqrt{2d\log(en/d)/n}$。无限VC维时不能使用这一替换，原始经验Rademacher界仍成立，但须实际得到足够小的复杂度才能提供有效风险保证。''')
p(159,r'''\begin{proof}
取题设ERM程序$A$。有限VC维提供分布无关的一致收敛样本量；设偏差容限$\varepsilon/2$，在共同事件上比较任意$h\in\mathcal H$：
''',r'''对参照$h$取下确界即得风险保证。VC偏差界显式依赖$d,\varepsilon,\delta$；对固定空间，把一个有限VC上界作为常数写入程序即可计算足够样本量。训练与输出程序的停机性则分别由题设保证。
\end{proof}''')
b[165]=r'''\begin{proof}
有效见证对任意$d+1$个输入返回不可实现标签，因此这些输入均不能打散，普通VC维至多为$d$。'''
b[166]=r'''设普通VC维$d<\infty$。给定$d+1$个互异输入，逐一枚举$2^{d+1}$种标签，运行ERM并计算其经验风险；各步骤都停机。至少一种标签不可实现，其最小经验风险为正，ERM也必须返回正风险。输出第一个这样的标签便构成总可计算见证，故有效VC维至多为$d$。与前一方向合并，得到相等。
\end{proof}'''
p(174,r'''\begin{proof}
固定任意参照$h\in\mathcal H$，依次用输出偏差、经验近似最优性和参照偏差：
''',r'''对任意参照成立，取下确界即得结论。
\end{proof}''')
b[179]=r'''\begin{proof}
无正例时恒为0与样本一致。有正例时，目标合取的文字在所有正例上都为1，不会被删除；剩余文字也全在正例上为1，故输出分对全部正例。任意负例上，目标合取至少一个文字为0，这个文字仍被保留，输出也为0。由此输出与全样本一致。每条观测检查至多$2p$个文字，训练耗时$O(np)$；有正例时剩余文字不矛盾且最多$p$个，预测耗时$O(p)$。把$|\mathcal C_p|\leq3^p+1$代入有限类可实现样本界，即得风险保证。
\end{proof}'''
b[185]=r'''\paragraph{延伸阅读}
Bartlett与Mendelson的论文继续推导依赖样本的Rademacher与高斯风险界，并研究组合函数类怎样继承基函数类的复杂度，适合接着线性得分和集成部分阅读\scite{bartlettmendelson2002}。'''
b[6]=b[6].replace('总可','几乎必然可')
f=Path('tex/03-foundations/02-learning-theory/02-binary-classification.tex'); f.write_text('\n\n'.join(b))
(r/'02-v1.tex').write_text(f.read_text()); (r/'02-v1-blocks.json').write_text(json.dumps([{'id':f'02-P{i+1:03}','text':v} for i,v in enumerate(b)],ensure_ascii=False,indent=2))
print('rewritten',sum(x['text']!=y for x,y in zip(json.loads((r/'02-blocks.json').read_text()),b)))
