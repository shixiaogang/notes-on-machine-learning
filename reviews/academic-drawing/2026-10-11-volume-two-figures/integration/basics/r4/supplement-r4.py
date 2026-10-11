#!/usr/bin/env python3
"""Mechanical proof coverage, pixel comparison and immutable version bindings only."""
import hashlib, json, subprocess
from pathlib import Path
import pymupdf
from PIL import Image

BASE = Path(__file__).resolve().parent
OUT = BASE/'r4'
ROOT = BASE.parents[2]/'volume-two-figures'
POPPLER = '/Users/robbieshi/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
m = json.loads((OUT/'render-manifest.json').read_text())
old = json.loads((BASE/'render-manifest.json').read_text())
needles = {'PUNC-01':'经典图半监督方法', 'PUNC-02':'匹配也可以由类别标签定义', 'PUNC-03':'预测时若知道当前任务', 'PUNC-04':'Tent用测试输入及预测'}
targets = []
for pr in m['pdfs']:
    stem=pr['stem']; pdf=Path(pr['path']); doc=pymupdf.open(pdf)
    texts=[''.join(p.get_text().split()) for p in doc]
    requests={}
    for issue,needle in needles.items():
        indices=[i+1 for i,t in enumerate(texts) if needle in t]
        if len(indices)!=1: raise RuntimeError((stem,issue,indices))
        requests.setdefault(indices[0], []).append(issue)
    figure=next(p for p in m['pages'] if p['stem']==stem and p['label']=='fig:models-linear-nonlinear' and p['variant']=='color')
    for physical in [figure['physical_page']-1,figure['physical_page'],figure['physical_page']+1]:
        requests.setdefault(physical, []).append('QA-01-model-and-neighbor')
    for physical,purposes in sorted(requests.items()):
        existing=next((p for p in m['pages'] if p['stem']==stem and p['physical_page']==physical and p['variant']=='color'),None)
        if existing:
            existing.setdefault('additional_purposes',[]).extend(purposes)
            record=existing
        else:
            prefix=OUT/'proofs'/f'{stem}-diagnostic-page-{physical:04d}-color'
            subprocess.run([POPPLER,'-f',str(physical),'-l',str(physical),'-singlefile','-r','150','-png',str(pdf),str(prefix)],check=True,capture_output=True)
            png=Path(str(prefix)+'.png')
            record={'stem':stem,'label':'diagnostic','printed_page':doc[physical-1].get_label(),'physical_page':physical,'variant':'color','pdf_sha256':pr['sha256'],'png':str(png.relative_to(OUT)),'png_sha256':sha(png),'additional_purposes':purposes}
            m['pages'].append(record)
        targets.append({'stem':stem,'physical_page':physical,'printed_page':record['printed_page'],'purposes':purposes,'png':record['png'],'png_sha256':record['png_sha256']})
    assert sha(pdf)==pr['sha256']
comparisons=[]
for p in m['pages']:
    if p['label'].startswith('fig:'):
        q=next(q for q in old['pages'] if (q['stem'],q['label'],q['variant'])==(p['stem'],p['label'],p['variant']))
    else:
        q=next((q for q in old['pages'] if (q['stem'],q['physical_page'],q['variant'])==(p['stem'],p['physical_page'],p['variant'])),None)
    if q:
        before=Image.open(BASE/q['png']); after=Image.open(OUT/p['png'])
        same=before.mode==after.mode and before.size==after.size and before.tobytes()==after.tobytes()
    else: same=False
    comparisons.append({'stem':p['stem'],'label':p['label'],'variant':p['variant'],'physical_page':p['physical_page'],'printed_page':p['printed_page'],'png':p['png'],'png_sha256':p['png_sha256'],'r3_png':q['png'] if q else None,'r3_png_sha256':q['png_sha256'] if q else None,'strict_whole_page_pixels_identical':same,'requires_actual_review':not same,'diagnostic_purposes':p.get('additional_purposes',[])})
common=json.loads((BASE/'common-input-manifest.json').read_text())
def check_common(x):
    if isinstance(x,dict):
        if 'path' in x and 'sha256' in x:
            path=Path(x['path'])
            if not path.is_absolute(): path=ROOT/path
            assert sha(path)==x['sha256'], str(path)
        for v in x.values(): check_common(v)
    elif isinstance(x,list):
        for v in x: check_common(v)
check_common(common)
(OUT/'common-input-manifest.json').write_text(json.dumps(common,ensure_ascii=False,indent=2)+'\n')
(OUT/'render-manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
(OUT/'diagnostic-targets.json').write_text(json.dumps(targets,ensure_ascii=False,indent=2)+'\n')
(OUT/'pixel-comparison.json').write_text(json.dumps({'method':'Strict whole-page mode/size/pixel bytes equality at 150dpi. No crop/masked comparison. Not a semantic verdict.','pages':comparisons},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'proofs':len(m['pages']),'identical':sum(x['strict_whole_page_pixels_identical'] for x in comparisons),'actual_review_required':[x for x in comparisons if x['requires_actual_review']],'diagnostic_targets':targets},ensure_ascii=False,indent=2))
