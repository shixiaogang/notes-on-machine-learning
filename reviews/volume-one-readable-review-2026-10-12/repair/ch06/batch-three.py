exec(open('reviews/volume-one-readable-review-2026-10-12/repair/ch06/batch-edit.py').read().split("change('本章")[0])
change('取$\\bm p\\in S^{D-1}$','取$\\bm p\\in\\mathbb S^{D-1}$')
change('标准局部最短性结论保证可以把这个区域取到足够小，\n使径向测地线段在邻域内达到端点间的最短长度。',r'''长度比较还需要指数映射的另一性质：Gauss引理说明，径向单位速度与
固定半径的横向变化正交，且径向速度的长度保持不变。这里引用该引理，
用它说明最短性怎样得出。把$V$缩成切空间中的小球，记竞争路径为
$\gamma(t)=\operatorname{Exp}_{\bm p}(r(t)\bm u(t))$，其中$\lVert\bm u(t)\rVert_g=1$。
在$r(t)>0$的部分，径向与横向速度正交，故
\[
 \lVert\dot\gamma(t)\rVert_g^2
 =\dot r(t)^2+
 \bigl\lVert\mathrm d(\operatorname{Exp}_{\bm p})_{r(t)\bm u(t)}
              [r(t)\dot{\bm u}(t)]\bigr\rVert_g^2
 \geq\dot r(t)^2.
\]
因此，从中心$\bm p$到$\bm q=\operatorname{Exp}_{\bm p}(\bm v)$、
始终留在此邻域内的任意路径，长度至少为
$\int|\dot r(t)|\,\mathrm dt\geq\lVert\bm v\rVert_g$。
经过中心时可分段取极限，结论不变。
径向路径$t\mapsto\operatorname{Exp}_{\bm p}(t\bm v)$恰有这个长度，因而在邻域内最短。''')
change('这项结论利用指数映射和径向、横向变化的正交性，不是只凭微分方程存在唯一性得到的。','凸正规邻域的存在性在这里作为进一步的局部结论引用；上述径向比较说明了\n长度最短性所需的额外依据，不能只凭微分方程的存在唯一性得到。')
change('割点研究从某点出发的测地线何时失去最短性，\n共轭点涉及相邻测地线的聚焦与变分退化；这些进一步判据不在本章展开，\n不能据术语本身判定一条路径最短。','更精细的失去最短性判据不在本章展开；下面先回答哪些条件能保证最短路存在。')
change('联络给出所需的比较规则。\n\\begin{definition}[Riemann Hessian]',r'''联络给出所需的比较规则。此前联络接受的是向量场，现在要在单点沿给定速度求导。
对$\bm v\in T_{\bm p}\mathcal M$，任选局部光滑场$\bm V$满足$\bm V(\bm p)=\bm v$，
把$(\nabla_{\bm V}\operatorname{grad}f)(\bm p)$简记为$\nabla_{\bm v}\operatorname{grad}f$。
这与延拓无关：两种延拓之差在局部基中的系数都在$\bm p$处为零，
联络对第一个变量按光滑函数线性，故它们给出的导数在该点相同。
\begin{definition}[Riemann Hessian]''')
p.write_text(s)
items=[
('CH06-M-10',['CH06-B-03'],'局部费力','修改','1437–1440','取$\\bm p\\in S^{D-1}$','取$\\bm p\\in\\mathbb S^{D-1}$','统一单位球面的黑板粗体。','初值轨迹小节完整','相同球面对象不再出现无说明的字体变化；公式与零速度约定均保留。'),
('CH06-M-11',['CH06-A-07','CH06-B-06','CH06-C-02'],'理解障碍','修改','1503–1515','标准局部最短性结论保证','Gauss引理说明，径向单位速度与','引用Gauss引理的正交性，补速度平方分解与径向总变差的长度下界；另标凸正规邻域存在性为引用。','端点能量变分至Hopf--Rinow和穿孔平面反例','唯一初速度只建立坐标；正交性才给每条竞争路径的长度下界。比较限于正规邻域，未声称推出任意远端的全局最短或唯一性。'),
('CH06-M-12',['CH06-A-08'],'局部费力','修改','1517–1522','割点研究从某点出发的测地线何时失去最短性','更精细的失去最短性判据不在本章展开','删割点、共轭点两项无后续用途的名称，直接承接存在性问题。','完整圆两条弧到Hopf--Rinow定理','圆弧反例已完成测地不蕴含最短的区分，删名称不删任何随后使用的条件。'),
('CH06-M-13',['CH06-B-07'],'技术问题','修改','1597–1606','联络给出所需的比较规则。','这与延拓无关','补由点处向量到局部场的延拓，以及第一槽函数线性保证延拓无关。','梯度坐标表示至Hessian对称与坐标公式','现在nabla_v是已解释的缩写；局部基系数在点处为零直接保证点处算子良定义，无需改公式。')]
records=json.loads((root/'consolidated-findings.json').read_text())
for mid,ids,sev,dec,lines,bef,aft,act,ran,reason in items:
 records.append(dict(merged_id=mid,original_ids=ids,severity=sev,decision=dec,location_before={'lines':lines,'quote':bef},location_after={'quote':aft},action=act,reread_range=ran,closure_reason=reason,status='已修改待最终自查'))
(root/'consolidated-findings.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
with (root/'repair-notes.md').open('a') as f:f.write('\n第三批完成球面字体、局部最短性、删闲置判据名称、Hessian延拓说明。Gauss引理及凸正规邻域存在性标为引用，正文展示引理到长度下界的实际作用，不冒充完整证明。累计13项，覆盖17个原ID。\n')
