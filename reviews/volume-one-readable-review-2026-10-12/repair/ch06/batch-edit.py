from pathlib import Path
import json
root=Path('reviews/volume-one-readable-review-2026-10-12/repair/ch06')
p=Path('tex/01-mathematical-preliminaries-upper/02-linear-algebra-and-geometry/02-differential-geometry-and-symmetry.tex')
s=p.read_text()
def change(a,b):
 global s
 assert s.count(a)==1,(a,s.count(a))
 s=s.replace(a,b)
change('本章的优化未知量是流形中的点；定义在整个流形上的函数与场，留给下一章研究。','本章用已知函数和向量场描述几何与目标，但优化未知量只是流形中的点；\n下一章再把整个函数或场本身作为可变对象。')
change('度量在这个闭球内有正的下界；任何连接两点的路径都必须\n先到达球的边界，因而已经付出一个正的长度。','设坐标球半径为$r>0$，度量矩阵$\\bm G$的最小特征值\n在其闭包上有统一正下界$m>0$。球内路径的速度至少为坐标速度的$\\sqrt m$倍；\n任何连接两点的路径都必须先到达球的边界，因而长度至少为$\\sqrt m\\,r>0$。')
change('之间可绕过任意小的圆孔，路径长度趋于$2$，却没有长度恰为$2$的允许路径。','之间可沿以被删原点为中心、半径任意小的半圆绕行，路径长度趋于$2$，\n却没有长度恰为$2$的允许路径。空间始终只删去原点，变化的是绕行路径。')
a='若要进一步组织可复合的局部表示，可以简要使用\\term{范畴}（category）：'
start=s.index(a); end=s.index('\\subsection{切向量的映射}',start)
s=s[:start]+s[end:]
p.write_text(s)
items=[
('CH06-M-01',['CH06-A-01'],'理解障碍','修改','14–17','本章的优化未知量是流形中的点；定义在整个流形上的函数与场，留给下一章研究。','本章用已知函数和向量场描述几何与目标','限定本章使用已知函数和场，只优化点；下一章才优化整个函数或场。','章首到元素表示入口；并核对本章小结','入口现在按未知量划分章界，与联络使用向量场、点优化使用已知目标函数相容。'),
('CH06-M-02',['CH06-B-02'],'局部费力','修改','462–467','度量在这个闭球内有正的下界','度量矩阵$\\bm G$的最小特征值','补最小特征值统一正下界m及抵达半径r的长度下界。','测地距离定义到诱导度量的弦长下界','闭球紧且G光滑正定提供m；路径必须先出球，sqrt(m)r明确证明不同点距离为正。'),
('CH06-M-03',['CH06-B-01'],'局部费力','修改','513–516','之间可绕过任意小的圆孔','空间始终只删去原点','明确被删集合不变，小半圆只是竞争路径。','完整圆距离例后至群作用入口','绕行半径与删去集合已分开，与后面穿孔平面的2+(pi-2)epsilon构造一致。'),
('CH06-M-04',['CH06-A-02','CH06-B-04','CH06-C-01'],'理解障碍','修改','739–745','若要进一步组织可复合的局部表示，可以简要使用\\term{范畴}','例如圆上的点在移动时，其横坐标也随之变化','删除不参与本章后续推理的范畴/函子旁支及该处term调用。','相对位置旋转公式到微分与余切空间','前段仍完成代数复合及路径搬运区别；新小节直接问点速度如何改变读数，无概念依赖断裂。')]
records=[]
for mid,ids,sev,dec,lines,bef,aft,act,ran,reason in items:
 records.append(dict(merged_id=mid,original_ids=ids,severity=sev,decision=dec,location_before={'lines':lines,'quote':bef},location_after={'quote':aft},action=act,reread_range=ran,closure_reason=reason,status='已修改待最终自查'))
(root/'consolidated-findings.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
(root/'repair-notes.md').write_text('# 第6章修复记录\n\nAI修订自查，非独立验收。修复基线为本目录before.tex（2110行）；当前阶段完成第一批4项（覆盖6个原ID）。\n\n已修改章界、距离正性证明、穿孔平面路径措辞，删除范畴/函子旁支。该旁支删除一个term调用，无需新增词典项。已连同前后段核对；其余发现和完整三级复读仍待执行。\n')
