from pathlib import Path
import json,html,shutil,io
from PIL import Image,ImageDraw
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
ROOT=Path(__file__).resolve().parents[2]; OUT=Path(__file__).resolve().parent
records=json.loads((ROOT/'figures/03-foundations/00-shared/generated/restoration-selection.json').read_text())
report={r['id']:r for r in json.loads((ROOT/'figures/03-foundations/00-shared/generated/restoration-report.json').read_text())['records']}
for v in ['original','restored','qa']: (OUT/v).mkdir(parents=True,exist_ok=True)
cards=[]
pdfmetrics.registerFont(TTFont('Chinese',str(ROOT/'fonts/LXGWWenKai-Regular.ttf')))
c=canvas.Canvas(str(OUT/'selected-figures-restored.pdf'),pagesize=(1190,842))
def text(x,y,s,size=12): c.setFont('Chinese',size);c.setFillColorRGB(.19,.24,.31);c.drawString(x,y,s)
for page,r in enumerate(records,1):
 n=r['id'];source=ROOT/report[n]['asset']
 if n=='085':source=source.with_suffix('.png')
 shutil.copyfile(ROOT/'output/volume-three-figure-comparison/before'/f'{n}.png',OUT/'original'/f'{n}.png')
 shutil.copyfile(source,OUT/'restored'/f'{n}.png')
 label=html.escape(r['label']);chapter=html.escape(r['chapter'])
 note='大模型重新绘制，三个阶段纵向排列' if n=='067' else '恢复旧设计，保留色阶并修正文字排版'
 cards.append(f'<article id="fig-{n}" data-search="{n} {label} {chapter}"><h2>{n} · {chapter}</h2><p>{label} · {note}</p><div class="pair"><section><h3>提交前的原设计</h3><a href="original/{n}.png" target="_blank"><img loading="lazy" src="original/{n}.png"></a></section><section><h3>本次恢复版</h3><a href="restored/{n}.png" target="_blank"><img loading="lazy" src="restored/{n}.png"></a></section></div></article>')
 text(30,807,f'{n}  {r["chapter"]}',19);text(30,780,r['label']+' | '+note,12)
 for x,v,title in [(30,'original','提交前的原设计 · fbb26aec'),(610,'restored','本次恢复版')]:
  text(x,747,title,14);c.setStrokeColorRGB(.82,.85,.88);c.rect(x,80,550,640)
  im=Image.open(OUT/v/f'{n}.png').convert('RGB');w,h=im.size;scale=min(526/w,616/h)
  buf=io.BytesIO();im.save(buf,format='JPEG',quality=94);buf.seek(0)
  c.drawImage(ImageReader(buf),x+(550-w*scale)/2,80+(640-h*scale)/2,width=w*scale,height=h*scale)
 text(30,42,'沿用原对比编号；图片等比例适配对比框，实际书页尺寸以卷三 PDF 为准。',11)
 text(1083,42,f'{page} / {len(records)}',11);c.showPage()
c.save()
page='''<!doctype html><html lang="zh"><meta charset="utf-8"><title>卷三指定插图恢复结果</title><style>body{font:16px system-ui;margin:0;background:#eef1f4;color:#3b4252}header{position:sticky;top:0;background:white;padding:22px 30px;z-index:2;border-bottom:1px solid #ccd4dd}h1{font-size:24px;margin:0}input{padding:10px;width:40%;border:1px solid #bac4cf;border-radius:6px}main{padding:24px}article{background:white;padding:22px;border-radius:10px;margin-bottom:24px}h2{font-size:19px;margin:0}article>p{font-size:13px;color:#6b7280}.pair{display:grid;grid-template-columns:1fr 1fr;gap:20px}.pair section{border:1px solid #d7dce2;border-radius:6px;padding:12px;min-width:0}.pair h3{font-size:14px}.pair a{height:480px;display:flex;align-items:center;justify-content:center}.pair img{max-height:100%;max-width:100%;object-fit:contain}@media(max-width:800px){.pair{grid-template-columns:1fr}}</style><header><h1>卷三指定插图恢复结果</h1><p>左：71bc2f9 之前的原设计。右：本次恢复版。保留原对比编号，共51张；067由大模型重新绘制并纵向排列。点击图片放大。</p><input id="q" placeholder="搜索原编号、章节或标签"><span id="count"></span></header><main>'''+''.join(cards)+'''</main><script>function update(){let q=document.querySelector('#q').value.toLowerCase(),n=0;document.querySelectorAll('article').forEach(a=>{a.hidden=!a.dataset.search.toLowerCase().includes(q);if(!a.hidden)n++});document.querySelector('#count').textContent=' '+n+' 张'}document.querySelector('#q').oninput=update;update()</script></html>'''
(OUT/'index.html').write_text(page)
for start in range(0,len(records),12):
 sheet=Image.new('RGB',(1800,1680),'#E5EAF0');d=ImageDraw.Draw(sheet)
 for j,r in enumerate(records[start:start+12]):
  x=j%3*600;y=j//3*420;im=Image.open(OUT/'restored'/f'{r["id"]}.png').convert('RGB');im.thumbnail((580,380))
  sheet.paste(im,(x+(600-im.width)//2,y+30+(380-im.height)//2));d.text((x+10,y+8),r['id'],fill='black')
 sheet.save(OUT/'qa'/f'contact-{start//12+1}.jpg')
print('Generated 51-page PDF and searchable comparison gallery.')
