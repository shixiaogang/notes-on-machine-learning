exec(open('reviews/volume-one-readable-review-2026-10-12/repair/ch06/batch-edit.py').read().split("change('本章")[0])
change('硬阈值还会使略跨尺度的一对点从相连突然变为不相连。','固定阈值时，若一对点的距离由阈值以下扰动到阈值以上，相应的边会突然消失。')
change('这只是隶属度，不自动是事件概率。高阶强度例如可取全部边强度的最小值，\n但必须声明采用哪种规则。一种常见的合并运算是','这只是隶属度，不自动是事件概率。若两个点各按自己的局部尺度确定邻居，\n同一对点可能得到不同的有向强度。令$a=\\mu_{i,j}$、$b=\\mu_{j,i}$，\n可以把二者合成一条无向边的强度。一种合并规则是')
change('结果仍在$[0,1]$内；交换性由对称式给出，结合性由','例如$a=0.6$、$b=0.5$时，无向强度为$0.8$，表示按此规则综合两端的邻接支持。\n高阶面的强度还需另定规则，例如取其全部边强度的最小值，并不由这个二元运算自动给出。\n合并结果仍在$[0,1]$内；交换性由对称式给出，结合性由')
a='局部PCA从协方差矩阵选出一个子空间。因此，先比较理想与实际协方差，'
b='若已知$d=D$，目标切空间就是整个环境空间$\\mathbb R^D$，'
start=s.index(a);end=s.index(b,start)
s=s[:start]+r'''局部PCA从协方差矩阵选出一个子空间。为比较它与真实切空间，
先以潜在点处的一阶切向位移构造理想协方差$\bm C_0$，
并假设采样在全部$d$个切方向上都有变化；这样$\bm C_0$的前$d$维特征子空间才是真实切空间。
设实际协方差为$\bm C_0+\bm E$，用正交投影$\bm P$、$\widehat{\bm P}$
分别表示真实与估计子空间。两投影之差的算子范数衡量最大方向偏差，
等于定义~\ref{def:matrix-analysis-principal-angles}中最大主角的正弦，且不受各自基选择影响。

当$d<D$时，把$\bm C_0$的特征值降序排列，设
$\delta=\lambda_d-\lambda_{d+1}>0$，并要求$\lVert\bm E\rVert_2<\delta/2$。
第~\ref{sec:linear-algebra-spectral-stability}节的单侧谱隙界和Weyl界给出
\[
 \lVert\widehat{\bm P}-\bm P\rVert_2
 \leq\frac{\lVert\bm E\rVert_2}{\delta-\lVert\bm E\rVert_2}
 \leq\frac{2\lVert\bm E\rVert_2}{\delta}.
\]
这里$\bm E$包括有限样本波动、噪声、邻域错选及非线性近似误差，
不能只代入测量噪声方差；若理想协方差未在全部切方向上展开，也不能把它的主子空间认作真实切空间。
'''+s[end:]
p.write_text(s)
items=[
('CH06-M-14',['CH06-A-09'],'局部费力','修改','1976–1987','硬阈值还会使略跨尺度的一对点从相连突然变为不相连。','固定阈值时，若一对点的距离','固定阈值、改变成对距离，明确边消失的扰动方向。','持续同调句至软并集概率边界','与前段尺度增大时复形嵌套的方向不再冲突；软关系回应固定阈值的不连续性。'),
('CH06-M-15',['CH06-B-09'],'理解障碍','修改','1976–1987','一种常见的合并运算是','令$a=\\mu_{i,j}$、$b=\\mu_{j,i}$','指定两个局部有向强度合成无向边，补0.6和0.5合成0.8；高阶面强度另行约定。','持续同调至UMAP概览及采样边界','公式操作数、输出对象与数值例完整；没有从[0,1]或并集公式推断概率解释。'),
('CH06-M-16',['CH06-A-10'],'理解障碍','修改','2020–2038','估计子空间的偏转受','两投影之差的算子范数衡量最大方向偏差','定义理想切向协方差、投影差、谱隙与扰动阈值，并给显式常数2及前章定位。','切空间估计稳定性全小节至坐标重构入口','前章实际有单侧谱隙界，Weyl保证剩余分离量至少delta-||E||；<delta/2还保证扰动后边界不交叉。理想子空间等于真实切空间有非退化切向采样前提，不能混为一般曲面总体协方差。')]
records=json.loads((root/'consolidated-findings.json').read_text())
for mid,ids,sev,dec,lines,bef,aft,act,ran,reason in items:
 records.append(dict(merged_id=mid,original_ids=ids,severity=sev,decision=dec,location_before={'lines':lines,'quote':bef},location_after={'quote':aft},action=act,reread_range=ran,closure_reason=reason,status='已修改待最终自查'))
(root/'consolidated-findings.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
with (root/'repair-notes.md').open('a') as f:f.write('\n第四批完成固定阈值的扰动方向、软并集操作数与数值例、切空间投影误差界。20个原始ID已映射到16项：15修改、1有据撤销；尚须全文三级自查及只读结构审计。\n')
