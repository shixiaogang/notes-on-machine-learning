"""Actual font layer only; model background pixels are never edited or traced."""
from pathlib import Path
import sys,json,hashlib,itertools
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/02-foundations/00-shared/generated'))
from typeset_common import Typeset,run,FONT_FILES
from fontTools.ttLib import TTFont
FONT_FILES["fallback"]="STIXTwoMath-Regular.otf"
fira_cmap=TTFont(ROOT/"fonts"/FONT_FILES["math"]).getBestCmap()
stix_cmap=TTFont(ROOT/"fonts"/FONT_FILES["fallback"]).getBestCmap()
for directory in sys.argv[1:]:
    here=Path(directory)
    config=json.loads((here/'labels-volume-two.json').read_text())
    t=Typeset(here/'background.png',here,ROOT/'fonts')
    fallbacks=[]
    original_text=t.text
    def actual_fonts(x,y,segments,color):
        actual=[]
        for a in segments:
            for ch in a['text']:
                kind=a['font']
                if kind in ('math','en','mi') and not ch.isspace() and ord(ch) not in fira_cmap:
                    assert ord(ch) in stix_cmap,('No true math glyph',ch)
                    kind='fallback';fallbacks.append(ch)
                if actual and actual[-1]['font']==kind and actual[-1]['size']==a['size'] and actual[-1]['dy']==a['dy']:
                    actual[-1]['text']+=ch
                else: actual.append(dict(a,text=ch,font=kind))
        original_text(x,y,actual,color)
    t.text=actual_fonts
    px_per_pt=t.base.width/(config['width_mm']/25.4*72)
    for a in config['labels']:
        x=a['x']*t.base.width;y=a['y']*t.base.height
        if 'segments' in a:
            segments=[run(s['text'],s.get('font','math'),s.get('pt',8)*px_per_pt,s.get('dy_pt',0)*px_per_pt) for s in a['segments']]
            t.text(x,y,segments,a.get('color','#3B4252'))
        else:
            t.label(x,y,a['text'],a.get('pt',8)*px_per_pt,a.get('font','cn'),a.get('color','#3B4252'))
    t.save()
    def rect(a):
        return [min(b[0] for b in a['boxes']),min(b[1] for b in a['boxes']),max(b[2] for b in a['boxes']),max(b[3] for b in a['boxes'])]
    overlaps=[]
    for i,j in itertools.combinations(range(len(t.labels)),2):
        a,b=rect(t.labels[i]),rect(t.labels[j])
        if min(a[2],b[2])>max(a[0],b[0]) and min(a[3],b[3])>max(a[1],b[1]):overlaps.append([i,j])
    check=json.loads((here/'typography-check.json').read_text())
    check.update(label_pair_overlaps=overlaps,stix_fallback_only_for_fira_missing=sorted(set(fallbacks)),publication_width_mm=config['width_mm'],px_per_pt=px_per_pt,main_label_pt=8,auxiliary_label_pt=7.5,background_sha256=hashlib.sha256((here/'background.png').read_bytes()).hexdigest(),model_pixels_unchanged_by_typesetting=True)
    (here/'typography-check.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n')
    (here/'typesetting-volume-two.json').write_text(json.dumps({'renderer':str(Path(__file__).relative_to(ROOT)),'configuration':'labels-volume-two.json','font_manifest':'figures/00-shared/academic-drawing/font-manifest.json','font_sha256':{k:hashlib.sha256((ROOT/'fonts'/v).read_bytes()).hexdigest() for k,v in FONT_FILES.items()},'publication_width_mm':config['width_mm'],'pixels':t.base.size,'ppi_at_publication':t.base.width/(config['width_mm']/25.4),'layer':'text-layer.png','background':'background.png','final':'figure.png','review':'technical checks only; scientific and visual judgment separately recorded'},ensure_ascii=False,indent=2)+'\n')
    assert not overlaps,overlaps
    print(here.name,'font coverage/canvas/pair overlap checked',flush=True)
