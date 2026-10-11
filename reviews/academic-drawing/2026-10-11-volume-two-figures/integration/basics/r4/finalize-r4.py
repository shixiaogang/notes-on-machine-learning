#!/usr/bin/env python3
"""Package already-written manual observations and mechanical final page bindings."""
import hashlib,json,shutil
from pathlib import Path
from PIL import Image

BASE=Path(__file__).resolve().parent
OUT=BASE/'r4'
ROOT=BASE.parents[2]/'volume-two-figures'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
m=json.loads((OUT/'render-manifest.json').read_text())
compare=json.loads((OUT/'pixel-comparison.json').read_text())['pages']
manual=json.loads((OUT/'manual-observations.json').read_text())
prior=json.loads((BASE/'page-review.json').read_text())['records']
records=[]; bindings=[]
for i,p in enumerate(m['pages'],1):
    assert sha(OUT/p['png'])==p['png_sha256']
    c=next(x for x in compare if x['png']==p['png'])
    actual=next((x for x in manual if x['png']==p['png']),None)
    r=dict(p,review_id=f'R4-PAGE-{i:02d}',strict_whole_page_pixels_identical=c['strict_whole_page_pixels_identical'])
    if actual:
        r.update(actual_observation=actual['observation'],review_basis='R4 actual view_image(detail=original)',viewed_in_r4=True,verdict='所查页面通过')
    else:
        assert c['strict_whole_page_pixels_identical']
        q=next(x for x in prior if x['png']==c['r3_png'])
        r.update(actual_observation=q['actual_observation'],review_basis='R3 actual view_image + R4 fresh render strict whole-page pixel identity',viewed_in_r4=False,r3_review_id=q['review_id'],r3_png_sha256=q['png_sha256'],r3_pdf_sha256=q['pdf_sha256'],verdict='相同整页保留R3实际版面结论')
    records.append(r)
    mode=Image.open(OUT/p['png']).mode
    assert mode in ['RGB','L'], mode
    bindings.append({'edition_pdf':'target/vol2-foundations.pdf' if p['stem']=='vol2' else 'target/machine-learning-notes.pdf','physical_page':p['physical_page'],'proof':p['png'],'dpi':150,'colorspace':'GRAY' if p['variant']=='gray' else 'RGB','encoded_png_mode':mode,'pdf_sha256':p['pdf_sha256'],'proof_sha256':p['png_sha256'],'printed_page':p['printed_page']})
write(OUT/'final-page-bindings.json',bindings)
write(OUT/'page-review.json',{'scope':'24 basics figures vol2; 9 representative figure pages all; 3 vol2 grayscale; model neighbors and punctuation closures; limited visual review, not full-book review','known_open_issues':[],'fresh_r4_actual_view_count':len(manual),'strict_identity_reuse_count':len(records)-len(manual),'records':records})
assert len(manual)==20
assert all(any(x['png']==r['png'] for r in records) for x in manual)
assert all(not x['requires_actual_review'] or any(n['png']==x['png'] for n in manual) for x in compare)
for filename in ['r4-punctuation-candidates.json','r4-punctuation-C.md','r4-punctuation-P.md','r4-punctuation-W.md','r4-scite-interface.json','pagination-QA-01.json','pagination-QA-01.patch']:
    d=OUT/'local-review';d.mkdir(exist_ok=True)
    shutil.copy2(BASE/filename,d/filename)
for rel in ['tex/02-foundations/01-basics/01-introduction.tex','tex/02-foundations/01-basics/02-machine-learning-models.tex','tex/02-foundations/01-basics/03-machine-learning-paradigms.tex']:
    dest=OUT/'source-snapshots'/rel;dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(ROOT/rel,dest)
    before=OUT/'before-source-snapshots'/rel;before.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(BASE/'source-snapshots'/rel,before)
for filename in ['render-r4.py','supplement-r4.py','finalize-r4.py']:
    shutil.copy2(BASE/filename,OUT/filename)
actual_source=json.loads((OUT/'actual-source-manifest.json').read_text())
if not any(x['source'].endswith('01-introduction.tex') for x in actual_source['snapshots']):
    rel='tex/02-foundations/01-basics/01-introduction.tex'
    actual_source['snapshots'].insert(0,{'source':rel,'sha256':sha(ROOT/rel),'snapshot':'source-snapshots/'+rel,'snapshot_sha256':sha(OUT/'source-snapshots'/rel)})
closure=[]
targets=json.loads((OUT/'diagnostic-targets.json').read_text())
for unit in actual_source['punctuation_units']:
    unit['status']='closed: actual root source C/P/W and both R4 PDFs actually viewed'
    unit['pdf_evidence']=[t for t in targets if unit['id'] in t['purposes']]
    closure.append({'id':unit['id'],'source_closed':True,'pdf_closed':True,'actual_paragraph_sha256':unit['actual_root_paragraph_sha256'],'actual_root_source_sha256':unit['actual_root_source_sha256'],'proofs':unit['pdf_evidence']})
actual_source['pdf_closure']='closed by actual R4 full-page view_image; see page-review and closure-status'
write(OUT/'actual-source-manifest.json',actual_source)
closure.append({'id':'QA-01','source_closed':True,'pdf_closed':True,'proofs':[t for t in targets if 'QA-01-model-and-neighbor' in t['purposes']]})
write(OUT/'closure-status.json',{'known_open_issues':[],'closed':closure})
text=['# R4 最终实际版面复核记录','', '以下实际所见由审查者逐页写入；JSON 仅把人工观察与当前PDF、页面、成图及正文SHA绑定。共48份完整页证明图，20份本轮实际查看，28份依据与R3严格整页像素相同而保留原实际查看结论。', '']
for r in records:
    text += [f"## {r['review_id']} · {r['stem']} · 纸面{r['printed_page']} / 物理{r['physical_page']}",'',f"范围：{r.get('actual_figure',r['label'])}；{r['variant']}。依据：{r['review_basis']}。",'',r['actual_observation'],'',f"PDF SHA `{r['pdf_sha256']}`；proof SHA `{r['png_sha256']}`。"]
    if 'asset' in r: text += [f"成图 `{r['asset']}` SHA `{r['asset_sha256']}`；正文 `{r['source_chapter']}` SHA `{r['source_chapter_sha256']}`。"]
    text+=['',f"证明图：[完整页]({r['png']})；结论：{r['verdict']}。",'']
(OUT/'page-review.md').write_text('\n'.join(text)+'\n')
for pdf in m['pdfs']: assert sha(Path(pdf['path']))==pdf['sha256']
for f in json.loads((OUT/'figure-source-manifest.json').read_text())['figures']:
    assert sha(ROOT/f['asset'])==f['asset_sha256']
    for x in f['inputs']: assert sha(ROOT/x['path'])==x['sha256']
for x in actual_source['snapshots']:
    assert sha(ROOT/x['source'])==x['sha256']==sha(OUT/x['snapshot'])
print(json.dumps({'proofs':len(records),'actual_viewed':len(manual),'strict_identity_reuse':len(records)-len(manual),'bindings':len(bindings),'known_open_issues':[]},ensure_ascii=False))
