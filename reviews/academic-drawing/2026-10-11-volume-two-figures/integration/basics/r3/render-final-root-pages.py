#!/usr/bin/env python3
"""Read-only final-root PDF proofs and mechanical source bindings; no verdicts."""
import hashlib, json, re, subprocess
from pathlib import Path
import pymupdf

OWN = Path(__file__).resolve().parents[2]
ROOT = OWN.parent / 'volume-two-figures'
OUT = Path(__file__).resolve().parent
POPPLER = Path('/Users/robbieshi/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
previous = json.loads((OWN/'reviews/academic-drawing/2026-10-11-volume-two-figures/basics/final-figure-version-manifest.json').read_text())
all_labels = ['fig:spam-training-loss','fig:models-discriminative-generative','fig:models-linear-nonlinear','fig:self-supervised-masked-process','fig:active-learning-loop','fig:meta-learning-process','fig:online-feedback-order','fig:federated-learning-process','fig:paradigm-combination-alphago']
gray_labels = ['fig:models-spatial-objectives','fig:active-learning-loop','fig:meta-learning-process']
manifest = {'render_engine':'Poppler pdftoppm 150dpi; fresh final root PDF', 'pdfs':[], 'pages':[], 'scope':'24 basics figures in vol2; 9 representative basics figures in all; 3 vol2 grayscale proofs; 3 adjacent vol2 pages'}
for stem,pdfrel,auxrel in [('vol2','target/vol2-foundations.pdf','build/02-foundations.aux'),('all','target/machine-learning-notes.pdf','build/main.aux')]:
    pdf=ROOT/pdfrel; doc=pymupdf.open(pdf); aux=(ROOT/auxrel).read_text()
    record={'stem':stem,'path':str(pdf),'sha256':sha(pdf),'pages':len(doc),'aux_path':str(ROOT/auxrel),'aux_sha256':sha(ROOT/auxrel)}
    manifest['pdfs'].append(record)
    pages_by_label={}
    for i,p in enumerate(doc): pages_by_label.setdefault(p.get_label(),[]).append(i+1)
    for f in previous['figures']:
        label=f['label']
        if stem=='all' and label not in all_labels: continue
        m=re.search(r'\\newlabel\{'+re.escape(label)+r'\}\{\{([^}]*)\}\{([^}]*)\}',aux)
        if not m: raise RuntimeError(label)
        fig,printed=m.groups(); choices=pages_by_label.get(printed,[])
        if len(choices)!=1: raise RuntimeError((label,printed,choices))
        physical=choices[0]
        variants=['color'] + (['gray'] if stem=='vol2' and label in gray_labels else [])
        for variant in variants:
            name=f'{stem}-figure-{fig}-page-{physical:04d}-{variant}'
            prefix=OUT/'proofs'/name
            command=[str(POPPLER),'-f',str(physical),'-l',str(physical),'-singlefile','-r','150','-png']
            if variant=='gray': command+=['-gray']
            subprocess.run(command+[str(pdf),str(prefix)],check=True,capture_output=True)
            png=Path(str(prefix)+'.png')
            manifest['pages'].append({'stem':stem,'label':label,'actual_figure':fig,'printed_page':printed,'physical_page':physical,'variant':variant,'pdf_sha256':record['sha256'],'png':str(png.relative_to(OUT)),'png_sha256':sha(png),'asset':f['source'],'asset_sha256':sha(ROOT/f['source']),'source_chapter':f['source_chapter'],'source_chapter_sha256':sha(ROOT/f['source_chapter'])})
    if stem=='vol2':
        for printed in ['63','78','81']:
            physical=pages_by_label[printed][0]; prefix=OUT/'proofs'/f'vol2-adjacent-page-{physical:04d}-color'
            subprocess.run([str(POPPLER),'-f',str(physical),'-l',str(physical),'-singlefile','-r','150','-png',str(pdf),str(prefix)],check=True,capture_output=True)
            png=Path(str(prefix)+'.png')
            manifest['pages'].append({'stem':stem,'label':'adjacent','printed_page':printed,'physical_page':physical,'variant':'color','pdf_sha256':record['sha256'],'png':str(png.relative_to(OUT)),'png_sha256':sha(png)})
sources=[]
for f in previous['figures']:
    d=(ROOT/f['source']).parent
    inputs={ROOT/f['source_chapter'], ROOT/f['source']}
    if f['method']=='tikz': inputs.add(d/'figure.tex')
    elif f['method']=='matplotlib':
        inputs.update(d.glob('*.json'))
        inputs.add(ROOT/'figures/02-foundations/00-shared/matplotlib/redraw/charts.py')
    else:
        for name in ['labels.json','typesetting-20261011.json','text-layer.png']:
            inputs.add(d/name)
        inputs.add(ROOT/'figures/02-foundations/01-basics/generated/render-20261011.py')
        inputs.add(ROOT/'figures/02-foundations/00-shared/generated/typeset_common.py')
        inputs.add(ROOT/f['selected_background'])
    sources.append({'label':f['label'],'method':f['method'],'asset':f['source'],'asset_sha256':sha(ROOT/f['source']),'matches_submitted_asset':sha(ROOT/f['source'])==f['sha256'],'inputs':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)} for p in sorted(inputs) if p.is_file()]})
(OUT/'render-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(OUT/'figure-source-manifest.json').write_text(json.dumps({'mechanical_only':True,'root':str(ROOT),'figures':sources},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pdfs':manifest['pdfs'],'proofs':len(manifest['pages']),'figures':len(sources),'assets_match_submitted':all(f['matches_submitted_asset'] for f in sources)},ensure_ascii=False,indent=2))
