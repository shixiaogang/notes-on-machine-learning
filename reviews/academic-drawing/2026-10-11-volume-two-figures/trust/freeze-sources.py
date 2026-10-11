"""Freeze scoped sources and exact figure dimensions; no semantic judgements."""
from pathlib import Path
import hashlib, json, re, subprocess
import pymupdf as fitz
from PIL import Image
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
OUT=Path(__file__).resolve().parent
SOURCES=ROOT/'tex/02-foundations/03-trustworthiness'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
records=[];texts=[]
for chapter in sorted(SOURCES.glob('0[1-6]-*.tex')):
 text=chapter.read_text();before=subprocess.check_output(['git','show','HEAD:'+str(chapter.relative_to(ROOT))],cwd=ROOT)
 snaps=OUT/'snapshots';snaps.mkdir(exist_ok=True)
 (snaps/(chapter.stem+'-before.tex')).write_bytes(before)
 (snaps/(chapter.stem+'-final.tex')).write_bytes(chapter.read_bytes())
 texts.append({'path':str(chapter.relative_to(ROOT)),'before_sha256':hashlib.sha256(before).hexdigest(),'final_sha256':sha(chapter),'before_snapshot':str((snaps/(chapter.stem+'-before.tex')).relative_to(ROOT)),'final_snapshot':str((snaps/(chapter.stem+'-final.tex')).relative_to(ROOT))})
 for block in re.findall(r'\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}',text,re.S):
  m=re.search(r'\\includegraphics\[([^]]+)\]\{([^}]+)\}',block)
  if not m:continue
  opts,rel=m.groups();path=ROOT/rel
  label=re.search(r'\\label\{([^}]+)\}',block).group(1)
  width_match=re.search(r'width=([0-9.]+)mm',opts)
  width=float(width_match.group(1)) if width_match else 111.404
  item={'id':f'T{len(records)+1:02d}','chapter':chapter.name,'label':label,'asset':rel,'asset_sha256':sha(path),'include_options':opts,'physical_width_mm':width}
  folder=path.parent
  if path.suffix=='.pdf':
   with fitz.open(path) as doc:item['export_size_mm']=[round(x*25.4/72,6) for x in [doc[0].rect.width,doc[0].rect.height]]
   item['scale']=width/item['export_size_mm'][0]
   source=folder/'figure.tex'
   if source.exists():
    s=source.read_text()
    sizes=[float(x) for x in re.findall(r'\\fontsize\{([0-9.]+)\}',s)]
    item['source_font_sizes_pt']=sorted(set(sizes))
    item['scaled_font_sizes_pt']=[round(n*item['scale'],4) for n in item['source_font_sizes_pt']]
    item['source']=str(source.relative_to(ROOT));item['source_sha256']=sha(source)
   else:
    labels=folder/'figure-labels.json';data=folder/'figure-data.json'
    item['label_metadata']=str(labels.relative_to(ROOT));item['data_metadata']=str(data.relative_to(ROOT))
    item['scaled_font_sizes_pt']=sorted({round(x['size_pt']*item['scale'],4) for x in json.loads(labels.read_text())})
  else:
   item['pixel_size']=list(Image.open(path).size)
   proof=json.loads((folder/'typography-20261011.json').read_text())
   item['scaled_font_sizes_pt']=sorted({round(x['font_size_at_print_pt'],4) for x in proof['labels']})
   item['font_proof']=str((folder/'typography-20261011.json').relative_to(ROOT))
  preview=folder/'figure.png';item['preview_sha256']=sha(preview)
  records.append(item)
 baseline=json.loads((OUT/'baseline.json').read_text()) if False else None
(OUT/'figure-freeze.json').write_text(json.dumps({'date':'2026-10-11','basis':'b0ffa7ff754e0cb39ea261c2e680ff5c7ba38017','sources':texts,'figures':records,'scope':'Mechanical freeze only. Visual and semantic judgement in figure-review.md and caption-review.md'},ensure_ascii=False,indent=2)+'\n')
nav={}
for chapter in sorted(SOURCES.glob('0[1-6]-*.tex')):
 old=subprocess.check_output(['git','show','HEAD:'+str(chapter.relative_to(ROOT))],cwd=ROOT).decode();new=chapter.read_text()
 calls=lambda text:re.findall(r'\\(?:ref|eqref|BookChapterRef|BookSectionRef|term)\{[^}]+\}',text)
 from collections import Counter
 nav[chapter.name]={'removed_calls':list((Counter(calls(old))-Counter(calls(new))).elements()),'added_calls':list((Counter(calls(new))-Counter(calls(old))).elements())}
(OUT/'navigation-diff.json').write_text(json.dumps(nav,ensure_ascii=False,indent=2)+'\n')
print('Frozen',len(records),'figures;',len(texts),'chapters')
print('Navigation/term changes:',nav)
