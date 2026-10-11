from pathlib import Path
import json,hashlib,subprocess,concurrent.futures
from PIL import Image,ImageChops,ImageDraw
from pypdf import PdfReader
R=Path("/Users/robbieshi/Library/Mobile Documents/com~apple~CloudDocs/writings/Notes/Machine Learning/.worktrees/volume-three-optimization")
C=Path("/Users/robbieshi/Library/Mobile Documents/com~apple~CloudDocs/writings/Notes/Machine Learning/.worktrees/volume-three-optimization/.worktrees/prose-pgm")
OLD=C/'build/volume-three-cross-volume/pdf-qa-pgm/285ac31a0291e446'
O=C/'build/volume-three-cross-volume/pdf-qa-pgm/5e7c66876bf75810'
O.mkdir(parents=True,exist_ok=True)
PDF=R/'target/vol3-models.pdf'
SHA='5e7c66876bf75810421a25ee2e0f66e0548bcf7fb7e8baad3e7d7d8386ba116b'
OLD_SHA='285ac31a0291e4462199cc7128871409434e07331abc2c2a07d9045e74488e11'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(PDF)==SHA
m1=json.loads((OLD/'render-manifest.json').read_text())
m2=json.loads((OLD/'additional-seam-render-manifest.json').read_text())
assert m1['pdf_sha256']==m2['pdf_sha256']==OLD_SHA
oldrows=m1['rendered']+m2['rendered']
assert len({r['pdf_page'] for r in oldrows})==91
locpath=R/'build/volume-three-cross-volume/final-book-pages/book-page-locations-final.json'
loc=json.loads(locpath.read_text())
assert loc['sha256']==SHA
figs=[f for f in loc['figures'] if '/03-probabilistic-graphical-models/' in f['owner']]
oldfigs=json.loads((OLD/'figures.json').read_text())
assert {f['label']:(f['pdf_page'],f['number']) for f in figs}=={f['label']:(f['pdf_page'],f['number']) for f in oldfigs}
(O/'locator-final.json').write_bytes(locpath.read_bytes())
(O/'figures.json').write_text(json.dumps(figs,ensure_ascii=False,indent=2))
BIN='/Users/robbieshi/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'
def render(r):
 n=r['pdf_page'];old=Path(r['path'])
 assert sha(old)==r['sha256']
 prefix=O/f'page-{n:04d}-140dpi'
 subprocess.run([BIN,'-f',str(n),'-l',str(n),'-r','140','-png','-singlefile',str(PDF),str(prefix)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
 out=Path(str(prefix)+'.png')
 oi=Image.open(old).convert('RGB');ni=Image.open(out).convert('RGB')
 equal=oi.size==ni.size and oi.tobytes()==ni.tobytes()
 bbox=None if equal else (ImageChops.difference(oi,ni).getbbox() if oi.size==ni.size else 'size mismatch')
 return {'pdf_page':n,'new_path':str(out),'old_path':str(old),'dpi':140,'old_sha256':r['sha256'],'new_sha256':sha(out),'png_equal':sha(out)==r['sha256'],'rgb_equal':equal,'difference_bbox':bbox,'old_rgb_sha256':hashlib.sha256(oi.tobytes()).hexdigest(),'new_rgb_sha256':hashlib.sha256(ni.tobytes()).hexdigest(),'size':list(ni.size)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: rows=list(pool.map(render,sorted(oldrows,key=lambda r:r['pdf_page'])))
contacts=[];figurepages=sorted({f['pdf_page'] for f in figs})
for ci in range(0,len(figurepages),12):
 subset=figurepages[ci:ci+12];canvas=Image.new('RGB',(1660,3220),'#eeeeee');draw=ImageDraw.Draw(canvas)
 for j,n in enumerate(subset):
  im=Image.open(O/f'page-{n:04d}-140dpi.png').convert('RGB');im.thumbnail((530,750))
  x=10+(j%3)*550;y=10+(j//3)*800
  nums=','.join(f['number'] for f in figs if f['pdf_page']==n)
  draw.text((x,y),f'PDF {n} / Fig {nums}',fill='black');canvas.paste(im,(x,y+28))
 out=O/f'contact-{ci//12+1:02d}.png';canvas.save(out)
 old=OLD/out.name
 contacts.append({'path':str(out),'pages':subset,'sha256':sha(out),'png_equal_old':sha(out)==sha(old),'rgb_equal_old':Image.open(out).convert('RGB').tobytes()==Image.open(old).convert('RGB').tobytes()})
reader=PdfReader(PDF)
assert len(reader.pages)==1042
assert sha(PDF)==SHA
manifest={'pdf':str(PDF),'pdf_sha256':SHA,'pdf_pages':1042,'old_pdf_sha256':OLD_SHA,'locator_sha256':sha(locpath),'figure_count':len(figs),'figure_pages':figurepages,'rendered_and_compared':rows,'contacts':contacts,'equal_png_pages':sum(r['png_equal'] for r in rows),'equal_rgb_pages':sum(r['rgb_equal'] for r in rows),'changed_pages':[r['pdf_page'] for r in rows if not r['rgb_equal']],'note':'Administrative pixel comparison; visual acceptance is separately bound to the old actual observations or new review of changed pages.'}
(O/'render-and-comparison-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps({'pages':len(rows),'png_equal':manifest['equal_png_pages'],'rgb_equal':manifest['equal_rgb_pages'],'changed':manifest['changed_pages'],'contacts_equal':all(x['rgb_equal_old'] for x in contacts)},ensure_ascii=False),flush=True)

