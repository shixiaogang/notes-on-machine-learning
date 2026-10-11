"""Mechanical rendered-page identity and grayscale evidence, not visual verdicts."""
from pathlib import Path
import hashlib, json
import pymupdf as fitz
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
OUT=Path(__file__).resolve().parent
old=json.loads((OUT/'full-pdf-locations-before-label-removal.json').read_text())
new=json.loads((OUT/'full-pdf-locations.json').read_text())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
before=ROOT/'build/trust-qa/full'/old['sha256'][:16]
after=ROOT/'build/trust-qa/full'/new['sha256'][:16]
rows=[]
for n in sorted({r['pdf_page'] for r in new['figures']}):
 name=f'page-{n}-140dpi.png';a=sha(before/name);b=sha(after/name)
 rows.append({'pdf_page':n,'before_sha256':a,'final_sha256':b,'identical_pixels_file':a==b})
doc=fitz.open(ROOT/new['pdf']);gray=after/'gray';gray.mkdir(exist_ok=True)
grayrows=[]
for n in [1238,1256,1266,1271,1296,1313,1315]:
 p=gray/f'page-{n}-140dpi-gray.png'
 doc[n-1].get_pixmap(dpi=140,colorspace=fitz.csGRAY,alpha=False).save(p)
 grayrows.append({'pdf_page':n,'path':str(p.relative_to(ROOT)),'sha256':sha(p)})
(OUT/'page-pixel-comparison.json').write_text(json.dumps({'before_pdf_sha256':old['sha256'],'final_pdf_sha256':new['sha256'],'pages':rows,'gray_pages':grayrows,'scope':'mechanical file identity only; actual visual verdict in pdf-visual-review.md'},indent=2)+'\n')
print('Identical',sum(r['identical_pixels_file'] for r in rows),'of',len(rows),'pages; changed:',[r['pdf_page'] for r in rows if not r['identical_pixels_file']])
