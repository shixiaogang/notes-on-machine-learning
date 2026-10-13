"""Bind current reader edits without rewriting historical scientific reviews."""
from pathlib import Path
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scripts'))
from check_figure_integration import figure_blocks
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
registry=ROOT/'figures/00-shared/academic-drawing/integration-manifest.json'
m=json.loads(registry.read_text())
new_folder=ROOT/'figures/03-foundations/01-basics/generated/learning-process-scene'
new_label='fig:learning-process-scene'
if not any(r['label']==new_label for r in m['records']):
    folder=str(new_folder.relative_to(ROOT))
    m['records'].append(dict(key='learning-process-scene',label=new_label,
        owner='tex/03-foundations/01-basics/01-introduction.tex',asset=folder+'/figure.png',
        folder=folder,route='contextual illustration',is_addition=True,volume=2,
        source=[folder+'/typeset.py',folder+'/background-20261013.png'],
        generation=folder+'/generation.json',review=folder+'/review.json'))
    m['expected_counts']['2']['addition']+=1
updated=[]
for r in m['records']:
    if not r['owner'].startswith('tex/03-foundations/'):continue
    owner=ROOT/r['owner'];text=owner.read_text()
    env,block=next((env,b) for env,b,labels in figure_blocks(text) if r['label'] in labels)
    asset=ROOT/r['asset'];folder=asset.parent
    cap=re.search(r'\\caption\{(.*)\}\s*\\label',block,re.S)
    source=set(r.get('source',[]))|set(r.get('current_source_sha256',{}))
    if (folder/'restoration-20261013.json').exists():
        renderer=json.loads((folder/'restoration-20261013.json').read_text()).get('refinement_renderer')
        if renderer:source.add(renderer)
        source.update(str(p.relative_to(ROOT)) for p in [folder/'labels.json',folder/'text-layer.png'] if p.exists())
    if r['label']==new_label:source.update(str(p.relative_to(ROOT)) for p in new_folder.iterdir() if p.name in ['labels.json','text-layer.png','prompt-20261013.txt'])
    if r['label']=='fig:spam-training-loss':
        source.update(str(p.relative_to(ROOT)) for p in [folder/'figure-labels.json',folder/'figure-data.json'])
    r.update(sha256=sha(asset),environment=env,current_body_sha256=sha(owner),
        current_source_sha256={p:sha(ROOT/p) for p in sorted(source) if (ROOT/p).is_file()},
        current_reader_review=str((HERE/'reader-review.json').relative_to(ROOT)),
        body_figure_sha256=hashlib.sha256(block.encode()).hexdigest())
    if cap:r.update(caption=cap[1].strip(),caption_sha256=hashlib.sha256(cap[1].strip().encode()).hexdigest())
    width=re.search(r'includegraphics\[([^]]*)\]',block)
    if width:
        r['graphics_options']=width[1]
        width=re.search(r'width=([^,]+)',width[1])
        if width:
            r['width_expression']=width[1]
            mm=112 if width[1]=='\\linewidth' else float(width[1].removesuffix('mm'))
            r['body_width_mm']=mm
    preview=asset if asset.suffix=='.png' else folder/(asset.stem+'.png')
    if preview.exists():r.update(preview=str(preview.relative_to(ROOT)),preview_sha256=sha(preview))
    updated.append(r['label'])
m['volume_three_reader_revision']={'date':'2026-10-13','labels':updated,
    'review':str((HERE/'reader-review.json').relative_to(ROOT)),
    'scope':'Current assets, contextual terminology and rendered layout; historical scientific review records retained.'}
registry.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
generation=json.loads((new_folder/'generation.json').read_text())
generation['figure_sha256']=sha(new_folder/'figure.png')
generation['body_width_mm']=112
(new_folder/'generation.json').write_text(json.dumps(generation,ensure_ascii=False,indent=2)+'\n')
print('Current reader bindings:',len(updated),'total assets:',len(m['records']))
