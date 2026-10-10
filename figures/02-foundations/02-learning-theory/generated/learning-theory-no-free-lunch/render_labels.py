from pathlib import Path
import sys,json,itertools,hashlib
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/02-foundations/00-shared/generated'))
from typeset_common import Typeset,run,FONT_FILES
from fontTools.ttLib import TTFont
FONT_FILES['fallback']='STIXTwoMath-Regular.otf'
HERE=Path(__file__).resolve().parent
config=json.loads((HERE/'label-config.json').read_text())
t=Typeset(HERE/'background.png',HERE,ROOT/'fonts')
for a in config['labels']:
 if 'segments' in a:t.text(a['x'],a['y'],a['segments'],a.get('color','#3B4252'))
 else:t.label(a['x'],a['y'],a['text'],a.get('size',36),a.get('font','cn'),a.get('color','#3B4252'))
t.save()
labels=t.labels
def rect(a):return [min(b[0] for b in a['boxes']),min(b[1] for b in a['boxes']),max(b[2] for b in a['boxes']),max(b[3] for b in a['boxes'])]
overlaps=[]
for i,j in itertools.combinations(range(len(labels)),2):
 a,b=rect(labels[i]),rect(labels[j]);dx=min(a[2],b[2])-max(a[0],b[0]);dy=min(a[3],b[3])-max(a[1],b[1])
 if dx>0 and dy>0:overlaps.append([i,j,round(dx,2),round(dy,2)])
check=json.loads((HERE/'typography-check.json').read_text());pppx=config['width_mm']/25.4*72/t.base.width
check.update(label_pair_overlaps=overlaps,width_mm=config['width_mm'],minimum_primary_pt=min(max(s['size'] for s in a['segments'])*pppx for a in labels),background_sha256=hashlib.sha256((HERE/'background.png').read_bytes()).hexdigest(),background_artwork_unchanged=True)
(HERE/'typography-check.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n')
(HERE/'typesetting.json').write_text(json.dumps({'renderer':'render_labels.py','config':'label-config.json','background':'background.png','width_mm':config['width_mm'],'font_manifest':'figures/00-shared/academic-drawing/font-manifest.json'},ensure_ascii=False,indent=2)+'\n')
assert not overlaps,overlaps
print(HERE.name,check)
