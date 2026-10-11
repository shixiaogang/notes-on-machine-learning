"""Prove render identity after EOF-only source cleanup; no visual verdicts."""
from pathlib import Path
import hashlib, json
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
OUT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for slug in ['full','vol2']:
 before=json.loads((OUT/(slug+'-pdf-locations-before-eof-tidy.json')).read_text())
 after=json.loads((OUT/(slug+'-pdf-locations.json')).read_text())
 assert before['figures']==after['figures']
 a=ROOT/'build/trust-qa'/slug/before['sha256'][:16]
 b=ROOT/'build/trust-qa'/slug/after['sha256'][:16]
 pages=[]
 for n in sorted({r['pdf_page'] for r in after['figures']}):
  name=f'page-{n:04d}-140dpi.png';x=sha(a/name);y=sha(b/name)
  assert x==y,(slug,n)
  pages.append({'pdf_page':n,'before_sha256':x,'final_sha256':y,'identical_file':True})
 row={'edition':slug,'before_pdf_sha256':before['sha256'],'final_pdf_sha256':after['sha256'],'pages':pages}
 if slug=='full':
  gray=[]
  for n in [1238,1256,1266,1271,1296,1313,1315]:
   name=f'page-{n}-140dpi-gray.png';x=sha(a/'gray'/name);y=sha(b/'gray'/name)
   assert x==y,('gray',n)
   gray.append({'pdf_page':n,'before_sha256':x,'final_sha256':y,'identical_file':True})
  row['gray_pages']=gray
 rows.append(row)
previews=json.loads((OUT/'pre-tidy-preview-hashes.json').read_text())
freeze=json.loads((OUT/'figure-freeze.json').read_text())
for_current={r['id']:sha(ROOT/Path(r['asset']).parent/'figure.png') for r in freeze['figures']}
assert for_current==previews
result={'scope':'mechanical file identity after EOF-only tidy, not a repeated visual inspection','editions':rows,'all_29_previews_identical':True}
(OUT/'eof-page-pixel-comparison.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Identical: 28 full + 28 vol2 + 7 grayscale pages; all 29 previews unchanged')
