"""Render actual saved PDFs; mechanical locations and pixels, no visual judgments."""
from pathlib import Path
import json,hashlib,shutil
import fitz
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
HERE=Path(__file__).resolve().parent
out=HERE/'pdf-pages'
manifest=out/'render-manifest.json'
old=json.loads(manifest.read_text())
shutil.copy2(manifest,HERE/'snapshots/render-manifest-before-online-color.json')
for stem,physical in [('vol2',91),('all',991)]:
 row=next(v for v in old['pages'] if v['stem']==stem and v['physical_page']==physical)
 shutil.copy2(ROOT/row['png'],HERE/'snapshots'/f'{stem}-online-before-color-page-{physical:04}.png')
pdfmap={'vol2':'target/vol2-foundations.pdf','all':'target/machine-learning-notes.pdf'}
docs={k:fitz.open(ROOT/v) for k,v in pdfmap.items()}
new={'phase':'final low-saturation online r4','dpi':150,'pdfs':[],'pages':[]}
comparison=[]
for stem,path in pdfmap.items():
 new['pdfs'].append({'path':path,'sha256':hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),'pages':len(docs[stem])})
for row in old['pages']:
 page=docs[row['stem']][row['physical_page']-1]
 assert page.get_label()==row['printed_page'],(row,page.get_label())
 page.get_pixmap(dpi=150,alpha=False).save(ROOT/row['png'])
 sha=hashlib.sha256((ROOT/row['png']).read_bytes()).hexdigest()
 newrow=dict(row,png_sha256=sha);new['pages'].append(newrow)
 comparison.append({'png':row['png'],'previous_sha256':row['png_sha256'],'final_sha256':sha,'identical':sha==row['png_sha256']})
manifest.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
(HERE/'page-repair-to-final-color-pixels.json').write_text(json.dumps(comparison,ensure_ascii=False,indent=2)+'\n')
gray=[]
for number in [59,80,89]:
 p=out/f'vol2-grayscale-page-{number:04}.png'
 docs['vol2'][number-1].get_pixmap(dpi=150,colorspace=fitz.csGRAY,alpha=False).save(p)
 gray.append({'physical_page':number,'printed_page':docs['vol2'][number-1].get_label(),'png':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'diagnostic':'grayscale rendering only, original figure unchanged'})
(HERE/'grayscale-manifest.json').write_text(json.dumps(gray,ensure_ascii=False,indent=2)+'\n')
print(new['pdfs']);print('changed', [v['png'] for v in comparison if not v['identical']])
