"""Connect restored images and synchronize exact figure registry bindings."""
from pathlib import Path
import re,json,hashlib
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
HERE=Path(__file__).resolve().parent
selection=json.loads((HERE/'restoration-selection.json').read_text())
reports=json.loads((HERE/'restoration-report.json').read_text())['records']
reportmap={r['id']:r for r in reports}
hashfile=lambda p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
changes=[]
for r in selection:
 number=r['id']; newpath=reportmap[number]['asset'];owner=ROOT/r['owner'];text=owner.read_text()
 pattern=r'\\begin\{figure\*?\}.*?\\end\{figure\*?\}'
 found=0
 def change(m):
  global found
  block=m.group(0)
  if '\\label{'+r['label']+'}' not in block:return block
  found+=1
  width=reportmap[number].get('body_width_mm',164.6)
  block=re.sub(r'\\includegraphics\[[^\]]*\]\{[^}]+\}',lambda _:r'\includegraphics[width='+f'{width:.3f}'+r'mm]{'+newpath+'}',block,count=1)
  # Tall 067 fits an ordinary text column; other historical figures retain
  # their original publication width and remain across the two columns.
  if number=='067':block=block.replace(r'\begin{figure*}',r'\begin{figure}').replace(r'\end{figure*}',r'\end{figure}')
  cap=r['caption']
  if number in ['002','012','033']:cap=r['before_caption']
  if number=='017':cap=cap.replace('蓝色直线','蓝色曲线').replace('，未标注池由10个候选减为9个','')
  if number=='018':cap=cap.replace('下方评价范围依次覆盖2、4、6类','下方评价集合逐步纳入已经出现的类别')
  if number=='062':cap=cap.replace('花朵样本和箭头','数字样本和箭头')
  if number=='081':cap=cap.replace('蓝线为公开查询，灰线为训练与投票，虚线为隐私记账；','')
  if number=='067':cap=cap.replace('数据环节补充遗漏人群并核实标签，训练环节调整风险目标及公平约束；','从上到下依次展示数据、训练与决策阶段。数据环节补充遗漏人群并核实标签，训练环节调整风险目标及公平约束；')
  pos=re.search(r'\\caption\{',block);i=pos.end();start=i;level=1
  while level:
   if block[i]=='{' and block[i-1]!='\\':level+=1
   elif block[i]=='}' and block[i-1]!='\\':level-=1
   i+=1
  oldcap=block[start:i-1]
  block=block[:start]+cap+block[i-1:]
  changes.append(dict(id=number,label=r['label'],owner=r['owner'],asset=newpath,body_width_mm=width,caption_changed=oldcap!=cap,caption=cap))
  return block
 text=re.sub(pattern,change,text,flags=re.S);assert found==1,(number,found);owner.write_text(text)
registry_path=ROOT/'figures/00-shared/academic-drawing/integration-manifest.json'
registry=json.loads(registry_path.read_text());bylabel={r['label']:r for r in changes}
for item in registry['records']:
 if item['label'] in bylabel:
  r=bylabel[item['label']]; folder=str(Path(r['asset']).parent)
  sources=[folder+'/figure.tex',folder+'/restored-design-symbols.tex'] if r['id']=='085' else [str(Path(__file__).with_name('restore-pre-71bc2f9.py').relative_to(ROOT)),folder+'/restored-design-original.png',folder+'/restored-design-labels.json',folder+'/restored-design-text-layer.png',folder+'/restoration-20261013.json']
  item.update(asset=r['asset'],folder=folder,source=sources,route='simple' if r['id']=='085' else 'complex',sha256=hashfile(r['asset']),body_width_mm=r['body_width_mm'],caption=r['caption'],source_sha256={p:hashfile(p) for p in sources},current_source_sha256={p:hashfile(p) for p in sources},current_review='reviews/academic-drawing/2026-10-13-volume-three-restoration/README.md')
  item.pop('companion_assets',None)
  for stale in ['pdf_width_pt','native_size_mm','current_method','method_override_reason']:
   item.pop(stale,None)
 # Bind every figure in an edited chapter to the final body, including figures
 # whose artwork was not selected. They share the same chapter hash.
 if any(r['owner']==item['owner'] for r in changes):
  item['body_sha256']=hashfile(item['owner']);item['current_body_sha256']=hashfile(item['owner'])
registry_path.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
review=ROOT/'reviews/academic-drawing/2026-10-13-volume-three-restoration';review.mkdir(parents=True,exist_ok=True)
(review/'changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
(review/'README.md').write_text('''# 卷三插图旧设计恢复

用户按对比编号选择50张图恢复71bc2f9之前的布局与样式，并将067的三个原面板纵向排列；仅调整配色。基线为fbb26aec，工作区正文基线为7dd5e395。用户于2026-10-13明确授权程序调整配色与面板排列。

恢复保留原始PNG、真实字体文字层、标签坐标、背景和原生成记录；颜色变换的五色角色沿用原图，照片矩形内的像素必须与原图一致。067只平移原面板，移除原水平面板间连接并改为向下连接。085恢复原TikZ图源和局部图元，使用现行色板重新导出PDF/SVG/PNG。

恢复清单及源文件在figures/06-foundations/00-shared/generated/restoration-selection.json和restoration-report.json，各图目录中的restoration-20261013.json记录校验值、照片保留矩形、出版宽度和067的坐标变换。changes.json登记正文引用与必要的图注一致性修改。

图片来源为历史模型生成图，配色通过连续变换逼近现行五色主色与浅底；保留原图的轻微明暗和抗锯齿，没有清理、模糊或新生成图元。真实照片的色彩不作为技术图元色板检查对象。未选择图片没有替换图像内容。

验证与书页检查结果将记入validation.json；登记校验值仅表示文件版本绑定，不替代科学关系和最终书页的视觉验收。
''')
print('Connected',len(changes),'figures; caption edits:',[r['id'] for r in changes if r['caption_changed']])
