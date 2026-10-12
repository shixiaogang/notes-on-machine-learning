from pathlib import Path
import re, hashlib
r=Path(__file__).parent
base=Path('tex/03-foundations/02-learning-theory')
changes={
'02':{
2:[('前章的阈值','第~\\ref{chap:statistical-learning-framework}章的阈值')],
9:[('这是固定假设的概率。','式~\\eqref{eq:bad-consistent-hypothesis}是固定假设的概率。')],
17:[('这一界尚未覆盖','式~\\eqref{eq:hoeffding-fixed-hypothesis}尚未覆盖')],
30:[('将一致收敛容限设为','在定理~\\ref{thm:finite-uniform-convergence}中将容限设为')],
31:[('可实现样本界的精度依赖','式~\\eqref{eq:finite-realizable-sample}的精度依赖'),('Hoeffding偏差概率按','式~\\eqref{eq:hoeffding-fixed-hypothesis}中的偏差概率按')],
36:[('有限空间可逐候选加失败概率，','有限空间可逐候选加失败概率，得到式~\\eqref{eq:finite-uniform-sample}的样本量；')],
55:[('当前界足以建立等价性，','式~\\eqref{eq:vc-uniform-bound}足以建立等价性，')],
58:[('前章的PAC量词','第~\\ref{chap:statistical-learning-framework}章的PAC量词')],
121:[('前章弱学习只要求','第~\\ref{chap:statistical-learning-framework}章的弱学习只要求')],
},
'03':{
5:[('前章两风险定义在零一损失下为','定义~\\ref{def:general-population-risk}与定义~\\ref{def:general-empirical-risk}在零一损失下为')],
7:[('一般$|Y|=K$时，','当$2\\leq K=|Y|<\\infty$时，'),('编码本身未保证这一容量条件。','编码本身未保证这一容量条件。若$K=1$，唯一标签的常量预测已是零风险规则，无需拆分位任务。')],
19:[('这与二类计数的步骤相同，','这与第~\\ref{sec:binary-growth-sauer}节的二类计数步骤相同，')],
41:[('对各$m$取引理中的$V_m$，','对各$m$取引理~\\ref{lem:low-natarajan-pseudocubes}中的$V_m$，')],
43:[('每个向量先验同重，邻接条件保证至少两种$i$处标签。','给定其余坐标后，不同向量在$i$处必有不同标签；条件分布对这些向量均匀，邻接条件又保证至少两个。')],
46:[('前一节已给维度有限却不可学习的例子。','第~\\ref{sec:multiclass-erm-limitations}节已给维度有限却不可学习的例子。')],
49:[('图维计最大输入规模。','图维取可图打散输入数的上确界。'),('\\]','\\]\n即在$B$上匹配参考，在其补集上偏离参考。')],
60:[('前章的两次$\\varepsilon/2$偏差','第~\\ref{chap:binary-learnability}章的两次$\\varepsilon/2$偏差')],
63:[('故一次非$\\star$观测就能恢复目标；','所以在$\\mathcal H_C$可实现来源下，一次非$\\star$观测就能恢复目标；')],
69:[('前一节的空间完全没有PAC学习器，','第~\\ref{sec:multiclass-erm-limitations}节的空间完全没有PAC学习器，')],
71:[('仍可不可学习','仍可能不可学习')],
74:[('有序点集$C$上的限制类','含$m$个互异输入的有序点集$C$上的限制类')],
75:[('第一卷将六预测画成环，','第~\\ref{sec:multiclass-erm-limitations}节的六种预测在第一卷中画成环，')],
79:[('前述不可学习反例有','第~\\ref{sec:multiclass-erm-limitations}节的不可学习反例有')],
80:[('这项结构足以产生学习失败的概率下界。','若任意大的有限输入集都具有这项结构，就能为每个样本量构造学习失败的概率下界。')],
86:[('本章没有把这项核心组合构造冒充为已证结果。','这项核心组合构造的证明仍依赖原文。')],
87:[('再像二类压缩分析那样','再沿第~\\ref{chap:binary-learnability}章的压缩分析')],
97:[('学习不推UC由集合标签例证明。','学习不推UC由定理~\\ref{thm:multiclass-erm-separation}的集合标签例证明。')],
103:[('沿用二类CPAC的程序要求，','沿用定义~\\ref{def:binary-computable-pac}的程序要求，'),('\\]\n输出','\\]\n。输出')],
105:[('图维等于损失VC维，给显式UC样本界。','定理~\\ref{thm:graph-uniform-convergence}将图维等同于损失VC维，因此给出显式UC样本界。'),('Natarajan有限经维度比较给图维有限，','Natarajan有限经定理~\\ref{thm:learning-multiclass-dimension-comparison}给图维有限，')],
119:[('类别编号长约$\\log K$，','当$K\\geq2$时，类别编号长约$\\log K$；单标签任务只需固定常量描述，')],
126:[('输出表长$O(p\\log K)$也进入资源预算。','当$K\\geq2$时，输出表长$O(p\\log K)$也进入资源预算；$K=1$时，一张含$p$个固定标签的表可用$O(p)$位表示，也可用常量规则表示。')],
133:[('提供对应有效VC的多类计算视角。','提供对应第~\\ref{sec:computable-binary-learning}节有效VC的多类计算视角。')],
}}
for n, cs in changes.items():
 f=base/(n+'-'+{'02':'binary-classification','03':'multiclass-classification'}[n]+'.tex')
 blocks=re.split(r'\n\s*\n',f.read_text().strip())
 for i,reps in cs.items():
  for old,new in reps:
   if blocks[i-1].count(old)!=1:raise ValueError((n,i,old,blocks[i-1].count(old)))
   blocks[i-1]=blocks[i-1].replace(old,new)
 out='\n\n'.join(blocks)+'\n';f.write_text(out)
 version={'02':'04','03':'02'}[n]
 (r/f'{n}-v{int(version)}.tex').write_text(out)
 print(n,len(blocks),hashlib.sha256(out.encode()).hexdigest())
