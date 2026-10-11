"""Check current scoped files against freezes; never infer scientific/visual pass."""
from pathlib import Path
import json, hashlib, subprocess
import pymupdf as fitz
from PIL import Image
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
OUT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
freeze=json.loads((OUT/'figure-freeze.json').read_text())
assert len(freeze['figures'])==29 and len(freeze['sources'])==6
for s in freeze['sources']:
 assert sha(ROOT/s['path'])==s['final_sha256']
 assert sha(ROOT/s['final_snapshot'])==s['final_sha256']
 assert sha(ROOT/s['before_snapshot'])==s['before_sha256']
nav=json.loads((OUT/'navigation-diff.json').read_text())
assert all(not v['removed_calls'] and not v['added_calls'] for v in nav.values())
fonts=json.loads((ROOT/'figures/00-shared/academic-drawing/font-manifest.json').read_text())
for font in fonts:assert sha(ROOT/'fonts'/font['file'])==font['sha256']
rows=[]
for f in freeze['figures']:
 asset=ROOT/f['asset'];folder=asset.parent
 assert sha(asset)==f['asset_sha256']
 assert sha(folder/'figure.png')==f['preview_sha256']
 with Image.open(folder/'figure.png') as im:im.verify()
 row={'id':f['id'],'asset':f['asset'],'sha256':sha(asset)}
 if asset.suffix=='.pdf':
  with fitz.open(asset) as doc:
   assert len(doc)==1
   row['pdf_fonts']=[list(x) for x in doc[0].get_fonts(full=True)]
  for suffix in ['.svg','.png']:assert (folder/('figure'+suffix)).is_file()
  if (folder/'figure.render.json').exists():
   r=json.loads((folder/'figure.render.json').read_text())
   assert sha(ROOT/r['source'])==r['source_sha256']
 else:
  proof=json.loads((folder/'typography-20261011.json').read_text())
  check=json.loads((folder/'typography-check.json').read_text())
  assert not check['missing_glyphs'] and not check['outside_canvas']
  assert sha(folder/proof['background'])==proof['background_sha256']
  row['background_sha256']=proof['background_sha256']
  for name,digest in proof['font_sha256'].items():assert sha(ROOT/'fonts'/name)==digest
  row['approximate_pixel_density_at_print_dpi']=round(proof['pixel_width']/proof['physical_width_mm']*25.4,2)
 rows.append(row)
shared=['figures/02-foundations/00-shared/academic-drawing/'+n for n in ['plot_style.py','preamble.tex','palette.tex','render_tikz.py','README.md']]
shared+=['figures/02-foundations/00-shared/matplotlib/redraw/'+n for n in ['charts.py','analytic-redraw-functions.py','risk-shift-functions.py','quantitative-redraw-functions.py']]
root=ROOT.parent/'volume-two-figures'
sharedrows=[]
for p in shared:
 a=sha(ROOT/p);b=sha(root/p);assert a==b,p
 sharedrows.append({'path':p,'sha256':a,'identical_to_root':True})
pdfs=[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)} for p in sorted((ROOT/'target').glob('*.pdf'))]
assert len(pdfs)==7
licenses=[str(p.relative_to(ROOT)) for p in sorted((ROOT/'fonts').rglob('*')) if p.is_file() and ('license' in p.name.lower() or 'ofl' in p.name.lower())]
result={'status':'mechanical invariants passed; manual judgements are separate','figures':rows,'fonts':fonts,'font_licenses':licenses,'shared_dependencies':sharedrows,'target_pdfs':pdfs,'build_manifest_sha256':sha(ROOT/'target/.build-manifest.json')}
(OUT/'final-assets-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Verified',len(rows),'figures, 6 source snapshots, 4 font files, 9 identical shared dependencies, 7 PDFs')
