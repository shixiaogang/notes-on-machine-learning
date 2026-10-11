from pathlib import Path
import hashlib, json, subprocess

B=Path(__file__).parent; R=B.parent.parent; ROOT=R.parent/'volume-two-figures'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manual=json.loads((B/'manual-observations-r3.json').read_text())
m=json.loads((B/'page-binding.json').read_text())
prior=json.loads((R/'reviews/academic-drawing/2026-10-11-volume-two-figures/theory/asset-manifest.json').read_text())
prior_by={f['label']:f for f in prior['figures']}
for edition,meta in m['pdfs'].items():
 assert sha(B/'inputs-r3'/f'{edition}.pdf')==meta['sha256']
for f in m['figures']:
 assert sha(B/'inputs-r3'/f['owner'])==f['source_sha256']
 for a,old in zip(f['assets'],prior_by[f['label']]['assets']):
  assert a['path']==old['path'] and a['sha256']==old['sha256']
  assert a['reference_width_mm']==old['width_mm']
  assert sha(ROOT/a['path'])==a['sha256']
  a['font_geometry_binding']={k:old[k] for k in ('native_width_mm','scale','body_pt','auxiliary_pt') if k in old}
  a['font_geometry_basis']='本组成图阶段的物理字号测量；当前资产SHA及引用宽度完全一致，仅复用机械字号，不复用旧书页判断'
 for e,v in f['editions'].items():
  assert sha(B/v['proof_png'])==v['proof_sha256']
  v['actual_review_status']='r3实际书页图形/排字通过；文字发现另列，不宣称全页无缺陷'
  v['actual_observation']=manual['figure_observations'][f['label']] if e=='vol2-foundations' else manual['main_observations'][f['label']]
 if 'gray' in f:
  v=f['gray'];assert sha(B/v['proof_png'])==v['proof_sha256']
  v['actual_review_status']='r3实际灰度页通过';v['actual_observation']=manual['gray_observations'][f['label']]
m['reading_status']='actual_visual_review_complete_for_25_vol2_figures_5_main_representatives_4_gray_pages'
m['limitations']=manual['limitations'];m['pending_r3_text_findings']=manual['pending_r3_text_findings']
m['mechanical_counts']={'figures':25,'components':sum(len(f['assets']) for f in m['figures']),'vol2_distinct_physical_pages':len({f['editions']['vol2-foundations']['physical_page'] for f in m['figures']}),'main_representatives':5,'gray_pages':4}
(B/'page-binding.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
t=json.loads((B/'text-page-binding.json').read_text())
for x in t:
 assert sha(B/x['proof_png'])==x['proof_sha256']
 assert sha(B/'inputs-r3/tex/02-foundations/02-learning-theory'/x['source_name'])==x['source_sha256']
 x['actual_review_status']='r3实际书页已看'
 if x['id'].startswith('OV-'):x['actual_observation']=manual['overfull_observations'][x['id']]
 else:x['actual_observation']='实际PDF已确认原数量/句末宏标点问题，候选待根改后源与r4 PDF复读'
(B/'text-page-binding.json').write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n')
edits=[
 ('CVT-R-B02','TXT-B94','四个阈值的风险差','图中全部候选的风险差'),
 ('PDF-SCITE-F687','TXT-F687',r'\scite{bartlettmendelson2002}，',r'\scite{bartlettmendelson2002}。'),
 ('PDF-SCITE-F778','TXT-F778',r'\scite{zhou2026ttalearnability}，',r'\scite{zhou2026ttalearnability}。'),
 ('PDF-SCITE-M225','TXT-M225',r'\scite{brukhim2022multiclass}，',r'\scite{brukhim2022multiclass}。'),
 ('PDF-SCITE-G87','TXT-G87',r'\scite{shalevshwartz2014}，',r'\scite{shalevshwartz2014}。'),
 ('PDF-SCITE-G1102','TXT-G1102',r'\scite{russo2016bias}，',r'\scite{russo2016bias}。'),
]
rows=[]
for key,tid,old,new in edits:
 x=next(x for x in t if x['id']==tid);assert x['source_text'].count(old)==1
 rows.append({'id':key,'source_name':x['source_name'],'source_sha256_r3':x['source_sha256'],'source_line_r3':x['source_line_range'][0],'old':old,'new':new,'old_paragraph':x['source_text'],'candidate_paragraph':x['source_text'].replace(old,new),'paragraph_candidate_sha256':hashlib.sha256(x['source_text'].replace(old,new).encode()).hexdigest(),'physical_page_r3':x['physical_page'],'printed_page_r3':x['printed_page'],'proof_sha256_r3':x['proof_sha256'],'r3_status':'已真实发现；候选C/P/W接受；根应用及r4实际复读待另记','review_records':['followup-C-r3.md','followup-P-r3.md','followup-W-r3.md']})
(B/'followup-old-new.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
refbytes=subprocess.check_output(['git','show','HEAD:tex/styles/references.tex'],cwd=ROOT)
assert refbytes==(ROOT/'tex/styles/references.tex').read_bytes()
macro=B/'inputs-r3/tex/styles/references.tex';macro.parent.mkdir(parents=True,exist_ok=True);macro.write_bytes(refbytes)
im={str(p.relative_to(B/'inputs-r3')):sha(p) for p in sorted((B/'inputs-r3').rglob('*')) if p.is_file()}
(B/'inputs-r3-sha.json').write_text(json.dumps(im,ensure_ascii=False,indent=2)+'\n')

md=['# 最终根 r3：理论图页实际检查','','2026-10-12，theory_second_half。AI自查：本组曾制作这25图，本次重新打开最终根PDF渲染页，未将旧工作区书页通过当作根成品通过。root为只读；全部快照、渲染和记录保存在自己的build。','',
 '## 成品与范围','',
 '- 卷二 `vol2-foundations.pdf`：SHA `'+m['pdfs']['vol2-foundations']['sha256']+'`，495物理页。',
 '- 全集 `machine-learning-notes.pdf`：SHA `'+m['pdfs']['machine-learning-notes']['sha256']+'`，2484物理页。',
 '- 25图/26成图组件，24个卷二实际物理页（分布偏移与支持覆盖同在p279）；5个全集代表；4个灰度页。当前aux定位、页码标签、PDF/PNG/资产/源SHA详见 `page-binding.json`。',
 '- 七处原正文overfull另见 `overfull-review-r3.md`。六处文字发现详见 `followup-old-new.json` 与三个局部C/P/W记录。r3含这些文字缺陷，不能称全页无问题。','',
 '## 25图逐张实际判断','',
 '| 图标签 | 卷二物理/印页 | 当前实际观察 |','|---|---|---|']
for f in m['figures']:
 v=f['editions']['vol2-foundations'];md.append(f"| {f['label']} | {v['physical_page']}/{v['printed_page']} | {manual['figure_observations'][f['label']]} |")
md+=['','## 全集5个代表页','', '| 图标签 | 全集物理/印页 | 重新实际观察 |','|---|---|---|']
for f in m['figures']:
 if 'machine-learning-notes' in f['editions']:
  v=f['editions']['machine-learning-notes'];md.append(f"| {f['label']} | {v['physical_page']}/{v['printed_page']} | {manual['main_observations'][f['label']]} |")
md+=['','## 灰度4页','', '| 图标签 | 卷二物理页 | 实际观察 |','|---|---|---|']
for f in m['figures']:
 if 'gray' in f:md.append(f"| {f['label']} | {f['gray']['physical_page']} | {manual['gray_observations'][f['label']]} |")
md+=['','## 尺寸、字体与适用边界','',
 '26成图组件当前SHA及引用物理宽度均与本组成图最终版本一致。真实排字/源字体角色已在成图阶段审查，当前记录复用的仅是相同资产和相同缩放条件下的机械字号：主体约8pt、辅助约7.5pt（舍入误差内），具体尺度见每资产font_geometry_binding；当前书页逐张目检另外确认了字形可辨、上下标完整、无裁切。',
 '模型1536像素在164.6mm处约237DPI；没有人为放大资产以消除默认300DPI验证警告。specs/figures.md并无300DPI硬门槛；本次结论依赖当前两种书版实际物理宽度、真实8/7.5pt排字与整页清晰度。旧验证默认阈值警告仍保留原记录，不以页图渲染的1600像素制造资产通过。',
 '复杂图模型无字底图加真实字体层、纯白平面框与空心节点（照片样例除外）；数据图保留Matplotlib矢量与复现数据，简单图保留TikZ源。当前渲染的科学关系/数量/端点/文字分离如上实际核对，不用类型配置替代视觉判断。',
 '',manual['limitations'],'']
(B/'actual-page-review-r3.md').write_text('\n'.join(md))
ov=['# 根 r3 七处正文 overfull 实页检查','','2026-10-12，theory_second_half，AI局部自查。图像均由保存的当前r3卷二PDF重新渲染并真实查看；源句、页全文和文字坐标见text-page-binding.json。这里只列指定位置，不作全书零Overfull声明。','',
 'TeX警告值是父任务冻结r3日志报告；下表文字最右坐标为PyMuPDF文字外框机械辅助，二者不是同一排版盒度量，不能据坐标取消警告。普通正文右边约382.68pt、证明栏约370.88pt；PDF宽612pt，当前超出行右侧均无同高度边注。','',
 '| ID/源行 | 物理/印页 | 日志溢出pt | 真实页判断 |','|---|---|---|---|']
for x in t[:7]:ov.append(f"| {x['id']} / {x['source_name']}:{x['source_line_range'][0]} | {x['physical_page']}/{x['printed_page']} | {x['reported_overfull_pt']} | {manual['overfull_observations'][x['id']]} |")
ov+=['','这些文字/公式在当前r3页上完整可读，未出页、未与边注碰撞或裁切；不要求本轮为其改变数学内容。保留警告作为版式边界，若以后同高度增加边注或改变文字断行仍应重新检查。未确认未列出的全文其他溢出。','']
(B/'overfull-review-r3.md').write_text('\n'.join(ov))
print(json.dumps({'figures':len(m['figures']),'editions':m['mechanical_counts'],'overfull':7,'local_text_findings':len(rows),'inputs':len(im)},ensure_ascii=False))
