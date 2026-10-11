from pathlib import Path
import json,re,hashlib
r=Path(__file__).parent;b=[x['text'] for x in json.loads((r/'03-blocks.json').read_text())]
for i,t in re.findall(r'@@ (\d+)\n(.*?)(?=\n@@ |\Z)',(r/'03-rewrite.txt').read_text(),re.S):b[int(i)-1]=t.strip()
pat=r'\\begin\{(equation\*?|align\*?)\}[\s\S]*?\\end\{\1\}|\\\[[\s\S]*?\\\]'
def p(n,*ss):
 ms=list(re.finditer(pat,b[n-1])); assert len(ss)==len(ms)+1,(n,len(ss),len(ms))
 b[n-1]='\n'.join(s+t.group() for s,t in zip(ss,ms))+('\n' if ms else '')+ss[-1]
p(5,r'''邮件标签现在分正常、广告、诈骗，输入$x$仍是特征，$h(x)$选择类别；与真实$y$不同即计一次错误。以$X,Y$为两空间、非空$\mathcal H\subseteq Y^X$为候选，对联合来源$\mathcal P$及iid样本$S=((x_i,y_i))_{i=1}^n$，前章两风险定义在零一损失下为
''',r'''后文固定这一计费口径。可实现PAC要求零风险目标来源下输出风险小，不可知PAC要求接近类内下确界；量词沿用第~\ref{sec:pac-learning}节。统计定理仍须满足第~\ref{sec:learning-problem}节的可测性与可分性条件。''')
p(6,r'''有限标签可先编码成二元位。例如对三类取
''',r'''广告邮件于是给两位任务标签1和0。在同一批邮件上训练$b_1,b_2$，新输入先得到$(b_1(x),b_2(x))$，再按表解码；无效$(0,0)$预定解为正常。这样改成两个二类任务，类别信息并未减少。''')
p(7,r'''一般$|Y|=K$时，用$L=\lceil\log_2K\rceil$位赋互异编码$c:Y\to\{0,1\}^L$，以$c_j(y)$记第$j$位。相应二类候选必须来自原空间的这一位投影：
''',r'''每个$h$先编码输出，再保留第$j$位。标签虽二元，诱导类仍可复杂；二类分布无关PAC须有有限VC，编码本身未保证这一容量条件。''')
p(8,r'''可实现来源由$h^\star\in\mathcal H$给零风险时，$c_j\circ h^\star$在每个位类中且几乎处处预测$c_j(y)$，所以全部位任务也可实现。若每个$\mathcal B_j$可PAC学习，令学得$b_j$的位风险为
''',r'''以$\tilde h$记解码分类器。全部位正确必给正确类别，故类别错误包含在位错并集中：
''',r'''将位风险目标定为$\varepsilon/L$、位学习失败预算定为$\delta/L$，两次并集分别得到类别风险与抽样成功概率，从而以至少$1-\delta$的概率使风险至多$\varepsilon$。位学习可共享样本，错误不必独立，只需共同样本量满足
''',r'''合成输出未必属于原$\mathcal H$。''')
p(15,r'''\BookChapterRef{chap:combinatorics}{第一卷“数学准备”的“计数与计算”章}给出两点模式：第一处固定正常/广告，第二处固定正常/诈骗，四个函数实现所有独立选择。标签对可因输入不同，却不能因待实现模式改变。依\BookDefinitionRef{def:natarajan-dimension}{该章Natarajan定义}，有限$C=\{x_1,\ldots,x_m\}$被打散，是指存在$f,g:C\to Y$在每点不同，且任意$B\subseteq C$都有$h_B\in\mathcal H$满足
''',r'''以$\mathcal C_N$收集全部这样的有限输入集，定义
''','')
p(19,r'''固定输入后先合并相同预测。令
''',r'''再对输入选择取上确界，得到生长函数
''',r'''这与二类计数的步骤相同，区别是每坐标可取$K$个标签。Sauer--Shelah由VC限制二元数目，下面用Natarajan承担多类的对应职责。''')
p(25,r'''\begin{proof}
取$\eta>0,n\eta^2\geq2$。独立副样本把总体/经验偏差转成双经验风险差超过$\eta/2$，概率最多增一倍。合并输入上的损失向量至多$G_{d,K}(2n)$种；逐对随机交换后，对固定向量集中，再对这些有限向量求并集界，得到
''',r'''令右侧等于$\delta$即可解出所列偏差；该解自动满足$n\eta^2\geq2$。上界超过1时，零一损失的取值范围已保证结论。
\end{proof}''')
p(31,r'''\begin{proof}
有限Natarajan维先给UC。取偏差$\varepsilon/2$，在共同成功事件内用ERM最优性比较任意$h$：
''',r'''对参照取下确界得不可知PAC。可实现分布属于这一允许族，因此也得到可实现PAC。''')
b[31]=r'''逆向设Natarajan无限。任意$n$都可取被打散的$2n$点及各点两种固定标签，令输入均匀，目标在各标签对中独立公平选择。$n$次观测至多见$n$点，余下标签仍公平，所以随机目标下任意算法平均风险至少$1/4$。平均中必有固定可实现目标也达此值；再由$R\leq1$及$\mathbb E R\leq1/8+(7/8)\mathbb P\{R>1/8\}$，得失败概率至少$1/7$。每个$n$都存在这种来源，违反分布无关可实现PAC。
\end{proof}'''
p(36,r'''先在两坐标看一个有限模式：
''',r'''其中$a,b,c$互异，$u,v,w$互异。每个向量在每坐标都有只改该坐标的邻居，例如$(a,u)$的$(b,u)$和$(a,w)$。但任意两种第一标签至多共享一种第二标签，无法形成固定两对标签的四组合；Natarajan维仅1，两坐标却都留歧义。这一个有限类仍可学习，反例还需任意维的同类结构。''')
p(41,r'''\begin{proof}
对各$m$取引理中的$V_m$，把输入组成互不相交的块$C_m=\{(m,1),\ldots,(m,m)\}$，令$X=\bigcup_{m\geq1}C_m$。局部标签加块编号写为$(m,y)$，因此$(2,a)$与$(3,a)$是不同类别。另设普通标签$\star$表示不在所选块，它不同于全部$(m,y)$，并非未知、缺失或任意值。标签总空间为
''',r'''每个$v\in V_m$扩展为整个输入空间上的假设
''',r'''例如$h_{2,v}$只在$C_2$使用局部答案，其他块均答$\star$。以全部$h_{m,v}$组成$\mathcal H$，各维困难块便属于同一个固定空间。''')
b[43]=r'''$n$次抽样至少遗漏$2n$点的一半，故对目标、样本及内部随机性平均的风险至少$1/4$。有限目标平均中必有固定$v$达到该下界；用$\mathbb E R\leq1/8+(7/8)\mathbb P\{R>1/8\}$，再得风险超过$1/8$的概率至少$1/7$。每个样本量都有如此可实现来源，所以不存在统一PAC样本量。
\end{proof}'''
b[45]=r'''\section{图维、DS维与一般标签空间}
\label{sec:general-multiclass-dimensions}
\label{sec:multiclass-sample-complexity}
有限标签靠Natarajan的预测计数连接UC与学习。撤标签数有限后，前一节已给维度有限却不可学习的例子。我们因此分别问：一份样本能否同时估准所有风险，以及是否存在算法选出低风险者？前者约束整个空间，后者只约束算法输出。'''
p(49,r'''零一损失把无限个错误答案都计为1，风险只看与真值是否匹配。为描述这一二元能力，先给每个输入参考$f(x)$，再问能否独立选择哪些点匹配。\term{图打散}（graph shattering）固定这项参考，图维计最大输入规模。按\BookDefinitionRef{def:graph-dimension}{第一卷图打散定义}，有限$C$被图打散，是指存在$f:C\to Y$，使每个$B\subseteq C$有$h_B\in\mathcal H$对全部$x\in C$满足
''','')
p(51,r'''按\BookDefinitionRef{def:graph-dimension-value}{第一卷图维定义}，令$\mathcal C_G$收集被图打散的有限输入集，有
''','')
b[55]=r'''\begin{proof}
若以$f$图打散$C$，在$\{(x,f(x)):x\in C\}$上，匹配/不匹配使损失实现全部二元赋值，故$\operatorname{VC}(\mathcal L_{\mathcal H})\geq d_G$。'''
b[56]=r'''反过来，损失打散的点集不能含同一$x$配两种$y$，因为两处损失不可能同时为0。输入于是互异，置$f(x_i)=y_i$，损失0/1便表示匹配/偏离，各模式使这些输入图打散。两维相等后，前章二值函数类的VC/UC刻画即给出所述等价。
\end{proof}'''
b[59]=r'''\begin{proof}
将每个$h$换成二值损失函数，经验最优比较保持不变。前章的两次$\varepsilon/2$偏差分别用于输出和任意参照，得到总体超额至多$\varepsilon$；再对参照取下确界即为不可知PAC。可实现来源使该下确界为0，因而也满足可实现保证。
\end{proof}'''
p(63,r'''这个标签传信息的构造取$X=\mathbb N$，用每个有限自然数子集作一个类别，再设与它们均不同的$\star$表示输入在目标集合外。对有限$A$定义
''',r'''标签$\{2,5\}$直接列明集合成员，故一次非$\star$观测就能恢复目标；样本全为$\star$时输出$h_{\varnothing}$。这里的数学标签故意携带整条规则，与通常的语义类别不同。''')
b[64]=r'''\begin{proof}
设目标$h_A$，以$p=\mathcal P_X(A)$记其集合概率。见过非$\star$时恢复目标，风险0；否则输出空集合规则，风险$p$。若$p>\varepsilon$，遗漏事件概率$(1-p)^n\leq e^{-n\varepsilon}$，所以$n\geq\log(1/\delta)/\varepsilon$足够。'''
b[67]=r'''让另一ERM在$n$条全$\star$记录时故意选$h_{A_S}$，其中$A_S=\{1,\ldots,2n\}\setminus\{x_1,\ldots,x_n\}$；其他可实现样本从集合标签恢复目标，不可实现样本则按固定顺序取前述有限候选的经验最小者。全$\star$样本上它零经验错，但目标为空、输入均匀于$\{1,\ldots,2n\}$时，至少$n$个未见输入被误判，风险至少$1/2$。任意$n$都有这样的来源，这个ERM不能分布无关PAC学习。
\end{proof}'''
b[81]=r'''\begin{proof}
取$2n$个DS打散点及其有限伪立方体$V$，输入均匀，从$V$均匀选目标，并为每向量固定一个实现假设。未见坐标即使给其余全标签仍有至少两个等可能答案，平均错误至少$1/2$。至少一半点未见，总平均风险便至少$1/4$。选择达到平均下界的固定目标，再用$\mathbb E R\leq1/8+(7/8)\mathbb P\{R>1/8\}$，得到所列失败概率。
\end{proof}'''
b[88]=r'''\begin{proof}[证明（使用引理~\ref{lem:finite-ds-compression}）]
有序序列允许重复，长度至多$r$时至多$(r+1)n^r$种索引；再计$n+1$种原样本大小，描述总数至多$M=(n+1)(r+1)n^r$。这些索引在看数据前确定，未预先列举无限标签。'''
p(92,r'''不可知算法在有限重构结果中选首个经验最小者。对固定描述，以$\hat R_{\mathrm{rest}}$记未读取观测的损失平均。条件独立性与单侧Hoeffding，再跨$M$个描述求和，使下式以至少$1-\delta/2$的概率同时成立：
''',r'''删去$j$条观测后平均损失最多增加$j/n$。把全样本均值写成剩余与已读两部分的加权平均，就得$\hat R_{\mathrm{rest}}(h)\leq\hat R_S(h)+j/n\leq\hat R_S(h)+r/n$，可以代入上式。''')
p(93,r'''任意预先固定$g\in\mathcal H$，把它分对的样本组成可实现子样本，压缩引理提供在这些观测上全对的重构者；其经验风险至多$\hat R_S(g)$。子样本为空时，$\hat R_S(g)=1$，任意候选都不更大。经验最小重构于是满足$\hat R_S(A^{\mathrm{agn}}(S))\leq\hat R_S(g)$。对固定$g$再用Hoeffding，以至少$1-\delta/2$的概率有
''',r'''合并两个半失败预算即得到相对该$g$的风险界。任取正的$\tau$，在抽样前选风险距类内下确界不足$\tau$的$g$，得到超过所列上界加$\tau$的概率至多$\delta$；令$\tau\downarrow0$，由事件单调收敛得到第二结论，无需所有参照同时估准。
\end{proof}''')
b[96]=r'''\begin{proof}[证明（使用有限DS维的学习器构造结果）]
DS有限时，定理~\ref{thm:finite-ds-learning-rates}的两界随足量$n$达到任意双容限，给两种分布无关PAC。不可知包含可实现，而无限DS已排可实现，故三项等价。图维/UC等价见定理~\ref{thm:graph-uniform-convergence}，学习不推UC由集合标签例证明。充分性仍依赖已引用的外部学习构造。
\end{proof}'''
p(103,r'''取$X=\mathbb N$，沿用二类CPAC的程序要求，但须先给标签和假设有效表示：标签编码可计算、相等可判定，有限标签全集可枚举，允许假设及输出由预定可递归枚举表示提供。不可知学习器对每份有限样本停机，返回一个对每输入停机输出$Y$标签的程序，并对所有允许来源和所有足量$n$满足
''',r'''输出在$\mathcal H$内是恰当，允许其他可计算规则是非恰当。再要求可计算充分样本上界得到strong CPAC，与前章同义，未要求多项式时间。''')
b[104]=r'''\begin{proof}
图维等于损失VC维，给显式UC样本界。取偏差$\varepsilon/2$，两次比较使ERM超额至多$\varepsilon$；训练和预测停机来自题设。固定空间的有限维上界可写入样本量程序。有限标签时，Natarajan有限经维度比较给图维有限，所以可替条件。
\end{proof}'''
t=b[111]; pos=t.index('必要性可通过');b[111]=t[:pos]+r'''必要性使用有效的未见输入论证。设CPAC程序$A$存在，固定使精度与失败概率均为$1/16$的保证成立的样本量$n$。给$2n$个输入及各两标签，有限枚举二元目标，再对每目标枚举这组输入上全部长度$n$的有序样本，训练并计算输出在$2n$点的错误比例。全部训练与预测都停机，有限平均因而可计算。'''
b[113]=r'''充分性在外部扩展$\mathcal H'$上运行：枚举有限样本的可实现预测，选错误最少者并返回其可计算实现，构成可计算ERM。有限标签及$d_N(\mathcal H')$有限给不可知PAC；又因$\mathcal H\subseteq\mathcal H'$，扩展类风险下确界不大于原类，所以同一输出也满足原类超额要求。输出可能在$\mathcal H$外，故为非恰当学习。
\end{proof}'''
p(120,r'''标签数不影响近似ERM的三次比较。若输出$A(S)\in\mathcal H$且
''',r'''全部风险偏差又至多$\eta$，则
''',r'''按定理~\ref{thm:approximate-erm-risk}，$2\eta$来自两次抽样均值替换，$\alpha$来自经验目标求解差。若用规模参数的多项式样本使$\eta\leq\varepsilon/4$，以多项式训练时间取得$\alpha\leq\varepsilon/2$，并使输出长和预测时间也为多项式，就得到高效不可知PAC的充分路线。''')
b[124]=r'''\begin{proof}
$h$分对样本数为$\sum_{x=1}^pN_{x,h(x)}$，逐行选最大计数即使总和最大，也就使经验风险最小。初始化$pK$计数器、扫描$n$观测、再逐行比较，操作数为$O(n+pK)$。有限类大小$K^p$与Hoeffding并集使偏差超过$\varepsilon/2$的概率至多$2K^pe^{-n\varepsilon^2/2}$，令其至多$\delta$再用ERM两次比较，得到风险保证。
\end{proof}'''
f=Path('tex/02-foundations/02-learning-theory/03-multiclass-classification.tex');f.write_text('\n\n'.join(s.rstrip() for s in b));(r/'03-v1.tex').write_text(f.read_text());(r/'03-v1-blocks.json').write_text(json.dumps([{'id':f'03-P{i+1:03}','text':s.rstrip()} for i,s in enumerate(b)],ensure_ascii=False,indent=2))
(r/'03-read-v1.txt').write_text('\n\n'.join(f'03-P{i+1:03}\n'+s.rstrip() for i,s in enumerate(b)))
print('sha',hashlib.sha256(f.read_bytes()).hexdigest());print('changed',sum(x['text']!=y for x,y in zip(json.loads((r/'03-blocks.json').read_text()),b)))
for pattern in [r'\\label\{[^}]+\}',r'\\(?:chapter|section|subsection|subsubsection|paragraph)\{[^}]+\}',pat,r'\\scite\{[^}]+\}']:
 a0=[re.sub(r'\s+','',m.group()) for m in re.finditer(pattern,(r/'03-v0.tex').read_text())];a1=[re.sub(r'\s+','',m.group()) for m in re.finditer(pattern,f.read_text())];print(len(a0),len(a1),a0==a1)
