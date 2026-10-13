from pathlib import Path
import json,html,fitz
from PIL import Image,ImageDraw
root=Path.cwd();out=root/'output/volume-three-restoration';(out/'all-current').mkdir(exist_ok=True)
audit=json.loads((root/'reviews/academic-drawing/2026-10-13-volume-three-restoration/refinement-audit.json').read_text());cards=[]
audit['records'].append(dict(id='new-1.1',label='fig:learning-process-scene',asset='figures/03-foundations/01-basics/generated/learning-process-scene/figure.png',manual_layout=False,change='new contextual illustration'))
for r in audit['records']:
 n=r['id'];p=root/r['asset'];dest=out/'all-current'/f'{n}.png'
 if p.suffix=='.pdf':
  d=fitz.open(p);d[0].get_pixmap(matrix=fitz.Matrix(1.8,1.8),alpha=False).save(dest);d.close()
 else:Image.open(p).convert('RGB').save(dest)
 note='新增学习过程插画' if n=='new-1.1' else '修正文字位置、对齐与留白' if r['manual_layout'] else ('保留色阶，重排真实字体文字层' if r['change'].startswith('continuous') else '已检查，设计保留')
 cards.append(f'<article id="fig-{n}" data-search="{n} {html.escape(r["label"])}"><h2>{n}</h2><p>{html.escape(r["label"])} · {note}</p><a href="all-current/{n}.png" target="_blank"><img loading="lazy" src="all-current/{n}.png"></a></article>')
page='''<!doctype html><html lang="zh"><meta charset="utf-8"><title>卷三全部90张插图检查</title><style>body{font:16px system-ui;background:#E5EAF0;color:#3B4252;margin:0}header{position:sticky;top:0;background:white;padding:20px;z-index:2}main{padding:20px;display:grid;grid-template-columns:1fr 1fr;gap:20px}article{padding:20px;background:white;border-radius:8px}h2{margin:0;font-size:24px}p{font-size:13px}a{height:400px;display:flex;align-items:center;justify-content:center}img{max-width:100%;max-height:100%}input{padding:10px;width:40%}@media(max-width:800px){main{grid-template-columns:1fr}}</style><header><h1>卷三全部90张插图检查结果</h1><p>按原对比编号排列。点击图片查看完整尺寸；067维持纵向。新增图1.1位于末尾，其余沿用原编号。</p><input id="q" placeholder="搜索编号或标签"><span id="count"></span></header><main>'''+''.join(cards)+'''</main><script>function update(){let q=document.querySelector('#q').value.toLowerCase(),n=0;document.querySelectorAll('article').forEach(a=>{a.hidden=!a.dataset.search.toLowerCase().includes(q);if(!a.hidden)n++});document.querySelector('#count').textContent=' '+n+' 张'}document.querySelector('#q').oninput=update;update()</script></html>'''
(out/'all-figures-review.html').write_text(page)
for start in range(0,len(audit['records']),9):
 sheet=Image.new('RGB',(2400,1800),'#E5EAF0');draw=ImageDraw.Draw(sheet)
 for j,r in enumerate(audit['records'][start:start+9]):
  x=j%3*800;y=j//3*600;im=Image.open(out/'all-current'/f'{r["id"]}.png');im.thumbnail((780,550));sheet.paste(im,(x+(800-im.width)//2,y+35+(550-im.height)//2));draw.text((x+15,y+10),r['id'],fill='black')
 sheet.save(out/'qa'/f'all-figures-{start//9+1}.jpg')
print(f'{len(audit["records"])}-figure searchable gallery generated.')
