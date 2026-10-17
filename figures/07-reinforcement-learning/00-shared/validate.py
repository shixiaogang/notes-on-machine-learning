#!/usr/bin/env python3
"""Verify the 113 production bindings, actual exports and teaching quantities.

This is file/numeric validation. It does not replace the recorded independent
scientific and visual review of figures and final book pages.
"""
from pathlib import Path
import hashlib
import json
import math
import re
import sys
import pymupdf as fitz
from PIL import Image

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file())
V=ROOT/'figures/07-reinforcement-learning'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def check():
    data=json.loads((V/'redraw-manifest.json').read_text());items=data['figures']
    assert len(items)==113
    assert len({x['key'] for x in items})==113
    labels=set();counts={};errors=[]
    for item in items:
        try:
            key,route=item['key'],item['route'];counts[route]=counts.get(route,0)+1
            p=ROOT/item['chapter'];s=p.read_text()
            blocks=re.findall(r'\\begin\{(figure\*?)\}(.*?)\\end\{\1\}',s,re.S)
            matches=[b for env,b in blocks if r'\label{'+item['label']+'}' in b]
            assert len(matches)==1,(key,'caption binding')
            assert item['asset'] in matches[0] and r'\caption{' in matches[0]
            assert item['label'] not in labels;labels.add(item['label'])
            asset=ROOT/item['asset'];assert asset.is_file()
            assert item['production_sha256']==sha(asset),(key,'stale production manifest hash')
            assert item['scientific_source_sha256']==sha(ROOT/item['source']),(key,'stale scientific source hash')
            if route in ['tikz','mixed']:
                source=ROOT/item['source'];meta=json.loads(source.with_suffix('.render.json').read_text())
                assert meta['source_sha256']==sha(source),(key,'stale native export')
                with fitz.open(asset) as doc:
                    assert len(doc)==1 and doc[0].rect.width>10
                    assert doc[0].get_text().strip(),(key,'blank vector export')
            elif route=='matplotlib':
                meta=json.loads(asset.with_suffix('.render.json').read_text())
                assert (ROOT/meta['source']).is_file() and (ROOT/meta['data']).is_file()
                with fitz.open(asset) as doc:assert len(doc)==1 and doc[0].rect.width>10
            else:
                folder=asset.parent;meta=json.loads((folder/'typography-check.json').read_text())
                for name,digest in meta['assets_sha256'].items():
                    assert sha(folder/name)==digest,(key,'stale text layer',name)
                assert Image.open(folder/'background.png').size==Image.open(asset).size
                assert Image.open(folder/'typography.png').mode=='RGBA'
                refs=json.loads((folder/'references/sources.json').read_text())
                assert len(refs)>=2
                for ref in refs:assert sha(folder/ref['retained'])==ref['sha256']
            assert item['body_width_mm']<=169.01
        except Exception as e:errors.append(str(e))
    assert counts==dict(tikz=69,matplotlib=20,generated=22,mixed=2),counts
    for font in json.loads((V/'00-shared/tikz/font-provenance.json').read_text())['fonts']:
        assert sha(ROOT/font['path'])==font['sha256']
        assert sha(ROOT/font['license'])==font['license_sha256']
    # Independent checks of the teaching quantities most likely to be misread.
    assert math.isclose(math.sqrt(.4),.6324555320336759)
    assert math.isclose(math.sqrt(1+1-2*.98),.2)
    assert math.isclose(1.96*.2,.392)
    assert math.isclose(.2+1.2*.6-.6**2,.56)
    assert 100*(1-.05**(1/299))<1<100*(1-.05**(1/298))
    assert math.isclose((.01*20+.09*10)/.1,11)
    game=json.loads((V/'00-shared/matplotlib/matching-pennies-data.json').read_text())
    assert all(len(game[k])==121 for k in ['Sim','Alt','Hist','CurrentGap','AverageGap','Regret'])
    assert game['Sim'][0]==game['Alt'][0]==game['Hist'][0]==[.7,.5]
    active=[]
    for p in (ROOT/'tex/07-reinforcement-learning').glob('*/*.tex'):
        active+=re.findall(r'\\label\{(fig:[^}]+)\}',p.read_text())
    assert set(active)==labels,(set(active)-labels,labels-set(active))
    return {'figures':len(items),'counts':counts,'errors':errors,
            'checks':['production caption/asset bindings','native source hashes','font and license hashes',
                      'generated background and transparent typography hashes','actual reference images',
                      'physical width limit','critical independent teaching quantities','121-point shared game data']}

if __name__=='__main__':
    result=check();print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(bool(result['errors']))
