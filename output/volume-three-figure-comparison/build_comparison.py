from pathlib import Path
import subprocess, re, json, hashlib, shutil, html, io
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
COMMIT = '71bc2f91250502a79350520302b020e4af94922a'
def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)
BEFORE = git('rev-parse', COMMIT+'^').decode().strip()
CURRENT = git('rev-parse', 'HEAD').decode().strip()
LFS = Path(git('rev-parse','--git-common-dir').decode().strip())
if not LFS.is_absolute(): LFS = ROOT / LFS
def blob(ref, path):
    data = git('show', ref+':'+path)
    if data.startswith(b'version https://git-lfs.github.com/spec/v1'):
        oid = re.search(rb'oid sha256:([0-9a-f]+)', data).group(1).decode()
        p = LFS/'lfs/objects'/oid[:2]/oid[2:4]/oid
        data = p.read_bytes()
        assert hashlib.sha256(data).hexdigest() == oid
    return data
def blocks(text, owner):
    result=[]
    for b in re.findall(r'\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}',text,re.S):
        asset=re.search(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',b)
        label=re.search(r'\\label\{([^}]+)\}',b)
        if not asset: continue
        cap=re.search(r'\\caption(?:\[[^\]]*\])?\{',b)
        caption=''
        if cap:
            i=cap.end(); level=1; start=i
            while i<len(b) and level:
                if b[i]=='{' and b[i-1]!='\\': level+=1
                elif b[i]=='}' and b[i-1]!='\\': level-=1
                i+=1
            caption=b[start:i-1]
        title=re.search(r'\\chapter(?:\[[^\]]*\])?\{([^}]+)\}',text)
        result.append(dict(label=label.group(1) if label else asset.group(1),asset=asset.group(1),owner=owner,chapter=title.group(1) if title else Path(owner).stem,caption=caption))
    return result
def historical(ref):
    names=git('ls-tree','-r','--name-only',ref,'tex/02-foundations').decode().splitlines()
    entries=[]
    for name in sorted(names):
        if name.endswith('.tex'): entries+=blocks(git('show',ref+':'+name).decode(),name)
    return entries
old=historical(BEFORE); changed=historical(COMMIT)
oldmap={x['label']:x for x in old}; changedmap={x['label']:x for x in changed}
def key(p):
    p=p.replace('03-foundations','02-foundations')
    return p
oldasset={key(x['asset']):x for x in old}
current=[]
for p in sorted((ROOT/'tex/03-foundations').rglob('*.tex')):
    current+=blocks(p.read_text(),str(p.relative_to(ROOT)))
assert current
for d in ('before','current','originals/before','originals/current'): (OUT/d).mkdir(parents=True,exist_ok=True)
def render(data,path):
    path.write_bytes(data)
    dest=OUT/path.parent.parent.name/(path.stem+'.png')
    # originals/<version>/<id>.* -> <version>/<id>.png
    dest=OUT/path.parent.name/(path.stem+'.png')
    if dest.exists(): return str(dest.relative_to(OUT))
    if data.startswith(b'%PDF'):
        subprocess.run(['pdftoppm','-f','1','-singlefile','-scale-to','2200','-png',str(path),str(dest.with_suffix(''))],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    else:
        im=Image.open(path).convert('RGB'); im.thumbnail((2600,2600)); im.save(dest)
    return str(dest.relative_to(OUT))
records=[]
for i, entry in enumerate(current,1):
    ident=f'{i:03d}'
    prior=oldmap.get(entry['label']) or oldasset.get(key(entry['asset']))
    atcommit=changedmap.get(entry['label'])
    data=(ROOT/entry['asset']).read_bytes()
    now=render(data,OUT/'originals/current'/(ident+Path(entry['asset']).suffix))
    before=None; oldhash=None; commit_changed=None
    if prior:
        prev=blob(BEFORE,prior['asset']); oldhash=hashlib.sha256(prev).hexdigest()
        before=render(prev,OUT/'originals/before'/(ident+Path(prior['asset']).suffix))
        if atcommit: commit_changed=prev!=blob(COMMIT,atcommit['asset'])
    entry.update(id=ident,before=before,current=now,before_asset=prior['asset'] if prior else None,before_caption=prior['caption'] if prior else None,before_sha256=oldhash,current_sha256=hashlib.sha256(data).hexdigest(),changed_in_commit=commit_changed)
    entry['status']='新增 / 无提交前对应图' if not prior else ('当前与提交前一致' if entry['current_sha256']==oldhash else '当前与提交前不同')
    records.append(entry)
    print(f'{ident}/{len(current)} {entry["label"]}',flush=True)
meta=dict(before_commit=BEFORE,comparison_commit=COMMIT,current_commit=CURRENT,records=records,notes='按当前正文顺序匹配语义标签，路径更名回溯；使用正文实际引用的导出图。所有图片保持原比例，预览同框适配，不代表书页实际缩放。')
(OUT/'manifest.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
cards=[]
for r in records:
    esc=html.escape
    left=f'<a href="{r["before"]}" target="_blank"><img loading="lazy" src="{r["before"]}"></a>' if r['before'] else '<p>提交前没有对应图片</p>'
    cards.append(f'''<article id="fig-{r['id']}" data-search="{esc(r['label']+' '+r['chapter']+' '+r['caption'])}" data-status="{r['status']}"><h2>{r['id']} · {esc(r['chapter'])}</h2><p class="meta">{esc(r['label'])} · {r['status']}</p><div class="pair"><section><h3>提交前 · {BEFORE[:8]}</h3>{left}</section><section><h3>当前 · {CURRENT[:8]}</h3><a href="{r['current']}" target="_blank"><img loading="lazy" src="{r['current']}"></a></section></div><details><summary>图注与来源</summary><p>当前图注：{esc(r['caption'])}</p><p>提交前图注：{esc(r['before_caption'] or '无')}</p><p>当前路径：{esc(r['asset'])}</p><p>提交前路径：{esc(r['before_asset'] or '无')}</p></details></article>''')
page='''<!doctype html><html lang="zh"><meta charset="utf-8"><title>卷三插图版本对比</title><style>body{margin:0;background:#f1f3f5;color:#293447;font:16px system-ui}header{padding:24px 32px;background:white;position:sticky;top:0;z-index:2;border-bottom:1px solid #ccd4dd}h1{margin:0 0 10px;font-size:24px}input,select{padding:10px;border:1px solid #bac4cf;border-radius:6px;margin-right:12px}input{width:36%}main{padding:24px}article{background:white;border-radius:10px;padding:20px;margin:0 0 24px;box-shadow:0 2px 8px #0001}h2{font-size:19px;margin:0}.meta{color:#647082;font-size:13px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:18px}.pair section{border:1px solid #d4dbe2;border-radius:6px;padding:12px;min-width:0}.pair h3{font-size:14px;color:#647082}.pair a{display:flex;align-items:center;justify-content:center;height:420px}.pair img{max-width:100%;max-height:100%;object-fit:contain}details{margin-top:18px;font-size:14px;overflow-wrap:anywhere}footer{padding:20px} @media(max-width:800px){.pair{grid-template-columns:1fr}.pair a{height:320px}}</style><header><h1>卷三《基础、理论与可信性》插图对比</h1><p>左：71bc2f9 的父提交；右：当前任务基线。点击图片可放大；同框等比例适配，不代表书页缩放。</p><input id="search" placeholder="搜索编号、章节、标签、图注"><select id="filter"><option value="">全部图片</option><option>当前与提交前不同</option><option>当前与提交前一致</option><option>新增 / 无提交前对应图</option></select><span id="count"></span></header><main>'''+''.join(cards)+'''</main><footer>版本、原始导出物、路径和校验值见 manifest.json 与 originals/。</footer><script>function update(){let q=document.querySelector('#search').value.toLowerCase(),s=document.querySelector('#filter').value,n=0;document.querySelectorAll('article').forEach(a=>{let ok=(a.dataset.search.toLowerCase()+' '+a.id).includes(q)&&(!s||a.dataset.status===s);a.hidden=!ok;if(ok)n++});document.querySelector('#count').textContent=n+' 张'}document.querySelector('#search').oninput=update;document.querySelector('#filter').onchange=update;update()</script></html>'''
(OUT/'index.html').write_text(page)
pdfmetrics.registerFont(TTFont('ComparisonChinese',str(ROOT/'fonts/LXGWWenKai-Regular.ttf')))
pdf=OUT/'volume-three-figures-before-current.pdf'
c=canvas.Canvas(str(pdf),pagesize=(1190,842))
def txt(x,y,s,size=12):
    c.setFont('ComparisonChinese',size); c.setFillColorRGB(.18,.22,.28); c.drawString(x,y,s)
for r in records:
    txt(30,808,f"{r['id']}  {r['chapter']}",19)
    txt(30,780,r['label']+' | '+r['status'],12)
    for x,version,title in [(30,'before','提交前 · '+BEFORE[:8]),(610,'current','当前 · '+CURRENT[:8])]:
        txt(x,746,title,14)
        c.setStrokeColorRGB(.8,.83,.86); c.rect(x,115,550,610)
        if r[version]:
            im=Image.open(OUT/r[version]); w,h=im.size; scale=min(526/w,586/h)
            compressed=io.BytesIO(); im.save(compressed,format='JPEG',quality=92); compressed.seek(0)
            c.drawImage(ImageReader(compressed),x+(550-w*scale)/2,115+(610-h*scale)/2,width=w*scale,height=h*scale)
        else: txt(x+145,420,'提交前没有对应图片',16)
    # Two short lines of caption for identification; full captions live in HTML.
    plain=re.sub(r'\\[a-zA-Z]+','',r['caption']).replace('{','').replace('}','').replace('$','')
    plain=' '.join(plain.split())
    txt(30,86,'当前图注：'+plain[:95],11)
    txt(30,66,plain[95:190],11)
    txt(30,29,'图片保持原比例；同框适配，仅用于比较独立图。完整图注与源路径见网页及清单。',10)
    txt(1085,29,f"{int(r['id'])} / {len(records)}",10)
    c.showPage()
c.save()
assert len(PdfReader(pdf).pages)==len(records)
stats={s:sum(r['status']==s for r in records) for s in set(r['status'] for r in records)}
(OUT/'summary.json').write_text(json.dumps(dict(total=len(records),statuses=stats,changed_in_commit=sum(r['changed_in_commit'] is True for r in records),missing_before=[r['label'] for r in records if not r['before']]),ensure_ascii=False,indent=2))
print(json.dumps(stats,ensure_ascii=False),flush=True)
