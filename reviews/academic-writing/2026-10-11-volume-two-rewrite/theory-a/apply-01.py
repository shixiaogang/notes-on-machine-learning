from pathlib import Path
import re,json
root=Path(__file__).parent
blocks=[x['text'] for x in json.loads((root/'01-blocks.json').read_text())]
edits={int(i):t.strip() for i,t in re.findall(r'@@ (\d+)\n(.*?)(?=\n@@ |\Z)',(root/'01-rewrite.txt').read_text(),re.S)}
for n,t in edits.items(): blocks[n-1]=t
# 混合单元只改写文字，原样保留陈列公式、标签和运算条件。
def around(n,pre=None,post=None):
 b=blocks[n-1]
 m=list(re.finditer(r'\\(?:begin\{(?:equation|align)\}|\[)',b))
 if not m: raise ValueError(n)
 first=m[0].start()
 ends=list(re.finditer(r'\\(?:end\{(?:equation|align)\}|\])',b))
 last=ends[-1].end()
 blocks[n-1]=(pre+'\n' if pre else b[:first])+b[first:last]+('\n'+post if post else b[last:])
around(16,r'先取最常用的同分布基线。以$\mathfrak P$收集允许来源，给定$\mathcal P\in\mathfrak P$后，从中独立抽取$n$条观测：',r'二分类、多分类与一般损失章节以此为起点。迁移学习另行规定源域、目标域、各样本量或环境层抽样，相应风险与概率也随之改变。各章沿用定义~\ref{def:learning-problem-setting}的对象职责，抽样关系则须在当地重新指定。')
around(21,r'算法看过样本再选决策，风险分析因此常须同时比较一组损失。对需要取上确界的$\mathcal W\prime\subseteq\mathcal W^+$，先将其损失写成函数类：'.replace(r'\mathcal W\prime',r'\mathcal W\,'),None)
# 恢复准确的带撇号符号，随后解释可数逼近条件。
blocks[20]=blocks[20].replace(r'$\mathcal W\,\subseteq',r"$\mathcal W'\subseteq")
b=blocks[20]; e=b.index(r'\]')+2
blocks[20]=b[:e]+r'''
直接给定函数类时仍记为$\mathcal F$。本部分要求一致有界类中的函数均可测，且有可数子类$\mathcal F_0$，使任意$f\in\mathcal F$都是其中一个序列的逐点极限。若$\mathcal F=\mathcal F_\ell(\mathcal W')$，为$\mathcal F_0$的每个函数固定一个代表决策，得到可数$\mathcal W_0\subseteq\mathcal W'$及$\mathcal F_0=\mathcal F_\ell(\mathcal W_0)$。学习、压缩、重构及其他数据依赖输出映射还须可测。'''
blocks[21]=r'''这些条件使不可数比较可以回到可数对象上。逐点逼近先保证固定有限样本的经验平均收敛，一致有界再通过有界收敛保证期望平均收敛，相关上确界因此可在可数子类上计算。给定$\rho>0$，按$\mathcal W_0$的固定枚举选第一个满足$\hat R_S(w)\leq\inf_{v\in\mathcal W_0}\hat R_S(v)+\rho$的决策，就得到可测选择：下确界和比较事件都可测，而逐点逼近给出$\inf_{v\in\mathcal W_0}\hat R_S(v)=\inf_{v\in\mathcal W'}\hat R_S(v)$。这也是原集合上的近似ERM。无法建立可数逼近或可测选择时，须改用外概率或另加经验过程条件；无界损失则另行检查可积性与矩条件。'''
around(32,r'算法允许选择的全部假设组成非空的\term{假设空间}（hypothesis space），记为$\mathcal H$。当前只调整阈值，故以全部允许$t$为索引写出候选：',r'下标$t$标明采用哪条规则。$h_{0.4}$与$h_{0.6}$是其中两个成员，训练选择$t$之后，预测再使用对应的$h_t$。')
around(36,r'比较候选时，先把预测错了多少转成代价。\term{损失}（loss）为一次预测计分；当前对两种误判同等计费，错分记1，正确记0。这称为\term{零一损失}（zero-one loss）。以$h(x)$为预测、$y$为真实标签，有',r'若误删正常邮件的代价更大，这一对称计分就须更换。下文先固定零一损失，以免比较时改变评价口径。')
around(39,r'按$\mathcal P$平均未来损失，就得到$h$的期望风险。零一损失只取0或1，其平均也就是分类错误的概率：')
around(40,r'算法无法直接计算这个未知分布平均，但可计算样本平均。对$S=(z_1,\ldots,z_n)$、$z_i=(x_i,y_i)$，定义经验风险为',r'分子累计样本错误数，除以$n$后给出这份样本中的错误比例。')
around(45,r'用样本比例推断未来风险，还须连接两批数据的来源。\term{独立同分布}（independent and identically distributed, i.i.d.）要求训练观测彼此独立，且各自服从评价所用的同一个$\mathcal P$。$n$个观测的联合分布因此是',r'这个理想化条件需要针对数据检查。重复转发可能造成依赖，部署后的邮件类型变化可能使评价不同于训练。后一情形须加入第~\ref{chap:transfer-learning-theory}章分析的跨域条件。')
around(68,r'将定义~\ref{def:general-pac-learnability}的允许族限定为对$\mathcal H$可实现的全部分布，记样本量阈值为$m_{\mathcal H}$。此时类内最低风险为零，成功事件化为',r'若同一个算法对所有这些分布达到该要求，就称$\mathcal H$可实现PAC可学习。$m_{\mathcal H}(\varepsilon,\delta)$可以依赖两项容限及假设空间，不能随具体未知分布改变。')
around(73,r'上面的保证能指定任意小精度，称为\term{强学习}（strong learning）。若只要求成功时比等概率随机猜测好一个固定幅度，则得到\term{弱学习}（weak learning）。在可实现二分类中，要求存在$\gamma\in(0,1/2)$、同一算法$A$和有限$m_{\mathcal H}^{\mathrm{weak}}(\delta)$，对任意$\delta\in(0,1)$、全部可实现$\mathcal P$及$n\geq m_{\mathcal H}^{\mathrm{weak}}(\delta)$满足',r'这时称$\mathcal H$弱PAC可学习。$\gamma$不随分布、样本或$\delta$变化，$U$独立于样本并表示内部随机性，确定性算法省略它。取$\gamma=0.1$时，成功结果至多40\%错误，比不看输入的公平猜测低10个百分点。第~\ref{sec:boosting}节还将区分目标与输出空间：重加权改变各轮分布，同一学习器与优势必须适用于仍由目标空间实现的每轮分布，并分配总失败预算。一次略优于猜测的训练结果尚未满足这一接口。')
around(79,r'我们要比较的是可逼近的最低风险，未必存在恰好最优的成员。因此以$R_{\mathcal P,\mathcal H}^\star$记下确界：',r'例如候选风险依次为$0.08+0.1/k$，可趋近0.08却不必取到0.08。下确界保留这个最佳逼近水平，无需额外假定最优假设存在。')
around(80,r'再将定义~\ref{def:general-pac-learnability}中的允许族取为$X\times Y$的全部相关联合分布，记充分样本阈值为$m_{\mathcal H}^{\mathrm{agn}}$。相对于上述下确界，要求',r'满足该统一保证时，称$\mathcal H$\term{不可知PAC可学习}（agnostic PAC learnable）。容限$\varepsilon$限制的是超额期望风险，而非全部分类风险。')
around(89,r'有限穷举可实现，却可能需要指数时间。设假设由$d$比特索引，有$2^d$个成员且各可多项式时间求值。逐一算经验风险仍要检查指数多个候选。定理~\ref{thm:finite-realizable-pac}给出的可实现充分样本量只按下式增长：',r'样本的线性规模与穷举的指数规模并不冲突，它们分别衡量信息与搜索成本。这个比较只排除了穷举的高效性，未排除利用结构的更快算法。')
around(102,r'将记忆表写成有限分数集合$C$，规则为',r'再令$h_{\mathrm{all}}(x)=1$，把它与全部有限表规则$h_C$一起放入假设空间。每条规则可测，且$h_{\mathrm{all}}$的总体风险为零，故这个分布可实现。')
around(103,r'以$C_S$记录样本$S$出现过的全部不同输入。选择$h_{C_S}$是一个合法的零经验风险选解，但它的两项风险为',r'每个训练点都在表内，所以第一项为零；连续均匀分布落在任意有限集合的概率为零，所以新输入几乎必在表外，第二项为1。零训练错误与几乎处处预测错误在同一规则上同时成立。')
around(114,r'同样的歧义可放在$2n$个等概率输入上。给定$n$个观测，未见集合$U$至少含$n$点。两张表在已见处相同、在$U$上相反时，同一输出$h$在每个未见点的两份零一损失相加为1，故',r'至少一张表使这次输出的风险不低于$1/4$。此处仍在固定样本下对照候选；下文须把候选平均，才能在抽样之前选定一个困难分布。')
blocks[116]=r'''\begin{proof}
固定输入集合$C$并让输入均匀出现，候选分布之间只改变标签表。对任意$g:C\to\{0,1\}$，前提给出$f_g\in\mathcal H$与它在$C$上一致。按先抽输入、再取标签$g(x)$的方式定义$\mathcal P_g$，这个分布就由$f_g$实现，风险为零。'''
around(120,r'每个未见输入占概率$1/(2n)$。风险非负，只累加至少$n$个未见点已给出随机标签表下的下界：',r'三个因子依次为未见点数下界、单点概率与条件错误概率。再平均训练输入、已见标签和内部随机数仍有$\mathbb E_g\mathbb E_{S,U}R_{\mathcal P_g}(A(S,U))\geq1/4$，其中$U$表示内部随机数。')
around(121,r'候选表只有有限张，平均至少为$1/4$就必有固定$g^\star$满足',r'若每张表的平均风险都小于$1/4$，总平均也会小于它，产生矛盾。现在固定$\mathcal P=\mathcal P_{g^\star}$及$f^\star=f_{g^\star}$，后续概率只包含从这个固定来源抽样与算法随机性。')
around(122,r'最后把平均风险下界转成失败概率。令$Z=R_{\mathcal P}(A(S,U))\in[0,1]$、$p=\mathbb P(Z\geq1/8)$。失败事件外$Z<1/8$，事件内$Z\leq1$，从而',r'移项即得$p\geq1/7$。\end{proof}')
around(136,r'\term{贝叶斯风险}（Bayes risk）是在当前输入信息下，全部可测分类器的最低错误概率。第一卷已由条件风险最小化建立Bayes决策，见\BookSectionRef{sec:decision-bayes-rules}{第一卷“策略、价值与优化”章的“Bayes决策”一节}；这里取二分类零一损失。令$\mathcal H_{\mathrm{all}}$为全部可测二分类器，便有共同基准',r'这个基准不限制分类器属于所选$\mathcal H$，表示知道数据规律时可达到的水平，没有假定学习器已经知道它。')
around(137,r'求共同基准可以先在一个输入$x$处比较两种标签。设$X$为标准Borel空间；更一般地，要求$\mathbb E[\mathbb I\{y=1\}\mid x]$有可测版本。该版本按$\mathcal P_X$几乎处处确定，选一个并记为',r'它记录输入$x$处标签为1的条件概率，标签为0的概率相应为$1-\eta(x)$。')
around(138,r'在$x$处预测1的错误概率为$1-\eta(x)$，预测0的错误概率为$\eta(x)$。选择较小错误率，就应在$\eta(x)\geq1/2$时预测1，否则预测0；相等时两者均最优。逐点这样选择得到\term{贝叶斯分类器}（Bayes classifier），用所选可测版本写为',None)
# 第二个陈列公式仍不动，更新其入口。
blocks[137]=blocks[137].replace('它在输入$x$处仍然会犯错的概率为','每个输入处的最小条件错误率因而为')
around(140,r'条件错误率要按输入频率加权才能得到总体风险。例如分数0.5占全部邮件的$q$，0.3的条件错误贡献$0.3q$。由联合分布忽略标签得到输入\term{边缘分布}（marginal distribution）$\mathcal P_X$，用它平均上述逐点最小值，得到',r'若两类标签都有正条件概率的输入集合具有正$\mathcal P_X$测度，这个平均便为正。即使已知分布、采用贝叶斯规则，当前输入仍会留下错误。')
around(145,r'对恰当输出$\hat h=A(S)\in\mathcal H$，在贝叶斯风险与输出风险之间加入类内下确界，便得',r'第一项是近似误差，第二项是估计误差。$\mathcal H\subseteq\mathcal H_{\mathrm{all}}$使第一项非负，$\hat h\in\mathcal H$使第二项非负。允许空间外输出时，它可以优于$\mathcal H$的下确界，第二项便可能为负，原非负分解的解释也须相应改变。')
around(151,r'算法对训练目标的求解差距还须单列。若样本上最好候选错2封、返回者错5封，多出的3次错误来自经验目标未达到最优。\term{经验优化误差}（empirical optimization error）以经验风险之差计量：',r'它比较样本目标，与式~\eqref{eq:approximation-estimation-decomposition}的期望风险差不同，不能把二项恒等式直接变成三个非负期望风险差。须先用泛化控制连接经验与总体，再让$\Delta_{\mathrm{opt}}(S)$进入输出风险保证。')
around(158,r'\term{结构风险最小化}（structural risk minimization, SRM）以带惩罚的经验目标选择空间，因为近似与估计误差依赖未知分布，不能直接最小化。先固定总失败预算$\delta$，分配与样本无关的$\delta_k>0$、$\sum_{k\geq1}\delta_k\leq\delta$。以$\operatorname{pen}(k,n,\delta_k)$记录第$k$个空间的复杂度惩罚，选择',r'经验项衡量训练拟合，惩罚控制由样本推断总体的不确定性，通常随空间复杂度增加。它是估计误差的控制量，并非该误差本身。惩罚偏小可能选中偶然拟合的复杂规则，偏大可能留下简单空间的表达偏差。最小值不可达时，可采用带惩罚目标的近似最优解。')
blocks[161]=r'''\begin{proof}
先把各空间的偏差保证合在一个共同事件中，再在事件内比较输出与任意参照假设。'''
around(163,r'令$E_k$表示$\mathcal H_k$中全部$h$满足$|R_{\mathcal P}(h)-\hat R_S(h)|\leq p_k$的事件，令$E=\bigcap_{k\geq1}E_k$。并集界把至少一个空间失准的概率控制为',r'事件都由同一份样本决定，无需相互独立。已有$\delta_k$预算便给出$\mathbb P(E)\geq1-\delta$。')
blocks[163]=blocks[163].replace('现在固定一份属于$E$的样本。由于$E$同时控制所有假设空间，它也控制由数据选出的$\mathcal H_{\hat k}$及其中的输出$\hat h$。于是','固定$S\in E$后，偏差界也覆盖数据选出的空间$\mathcal H_{\hat k}$及输出$\hat h$，因此').replace('对任意$k$及任意$h\in\mathcal H_k$，近似最优性又给出','以任意$k$及$h\in\mathcal H_k$作参照，带惩罚目标的近似最优性给出').replace('同一个事件$E$还保证','对同一参照，$E$又保证').replace('两个$p_k$的来源不同：第一个是比较假设所属假设空间时显式加入的惩罚，第二个用来控制事件$E$上\n比较假设的经验风险高于期望风险的偏差。这个偏差不等同于前文定义的估计误差；\n两项合在一起构成控制假设空间选择所产生估计误差的统计上界。输出假设所属空间的$p_{\hat k}$已通过\n带惩罚目标的比较一并控制。','第一个$p_k$来自参照目标的显式惩罚，第二个来自参照经验风险与总体风险的偏差。它们共同上界控制空间选择的统计代价，并非估计误差的定义值；输出空间的$p_{\hat k}$已经在带惩罚比较中消去。')
blocks[164]=r'''任意$h\in\mathcal H_k$与任意$k$都满足上式，依次取两层下确界即得式~\eqref{eq:srm-oracle}，无需最优假设或空间实际存在。由于全程在$E$内推导，而$\mathbb P(E)\geq1-\delta$，得到所需高概率结论。
\end{proof}'''
around(167,r'可用望远镜求和分配预算：取$\delta_k=\delta/[k(k+1)]$，因$1/[k(k+1)]=1/k-1/(k+1)$而总和为$\delta$。若各$\mathcal H_k$有限，第~\ref{sec:binary-uniform-convergence}节的一致收敛界给出',r'$|\mathcal H_k|$计入类内选择代价，$\delta_k$还计入跨空间比较代价。无限空间须另用容量工具建立式~\eqref{eq:srm-classwise-confidence}，不可把无限基数直接代入有限空间的计数公式。')
# 图表保留数据和视觉对应，只重写说明。
cap={29:r'四封构造的训练邮件与一封未标注邮件上的阈值预测。两个阈值分对全部训练记录，却在分数0.5处产生分歧；末行没有真实标签，故不能据它判断谁正确。',50:r'两层随机性的评价对象。固定训练输出后，右侧新观测的平均损失给出期望风险；左侧重新抽样则改变输出，学习保证控制这种变化造成高风险结果的概率。',111:r'相同样本与两套隐藏标签。鸟、汽车、狗、船分别表示编号1至4，每个概率为$1/4$；两套来源在已见编号1、2上同为0、1，未见编号3、4则分别全为0或全为1。图示输出$h(3)=0,h(4)=1$在每套来源各错一个点。固定样本与内部随机数后输出相同，任意二元预测在每个未见点的两份损失相加为1，故风险之和至少$1/2$。这里展示固定样本的歧义，下文再证明随机抽样下的固定困难分布。',148:r'风险的两段差距。教学设定中，贝叶斯风险为5\%，阈值空间最低风险为12\%，输出风险为15\%。前两者相差7个百分点，为实线表示的近似误差；后两者相差3个百分点，为虚线表示的估计误差。',155:r'教学示意中的验证选择与独立测试。实线圆点为训练误差，虚线方块为验证误差，圆环的最低验证误差确定$\hat k$。三角形仅为锁定模型后的一次测试评价，未参与选择，故不连成测试曲线。所有数值均为构造示意。'}
for n,v in cap.items():
 b=blocks[n-1]; st=b.index(r'\caption{')+9; pos=st; depth=1
 while depth:
  if b[pos]=='{':depth+=1
  if b[pos]=='}':depth-=1
  pos+=1
 blocks[n-1]=b[:st]+v+b[pos-1:]
# 正式定义及定理条件不作无意义的同义改写；保持它们独立、可逐项核对。
f=Path('tex/02-foundations/02-learning-theory/01-statistical-learning-framework.tex')
f.write_text('\n\n'.join(blocks))
(root/'01-v1.tex').write_text(f.read_text())
(root/'01-v1-blocks.json').write_text(json.dumps([{'id':f'01-P{i+1:03}','text':b} for i,b in enumerate(blocks)],ensure_ascii=False,indent=2))
print('rewritten blocks',sum(a['text']!=b for a,b in zip(json.loads((root/'01-blocks.json').read_text()),blocks)))
