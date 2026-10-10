"""Reproduce only real-font overlays on the model artwork; no image cleanup."""
from pathlib import Path
import sys,json
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
D=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'figures/02-foundations/00-shared/generated'))
from typeset_common import Typeset,FONT_FILES
FONT_FILES['fallback']='STIXTwoMath-Regular.otf'
config=json.loads((D/'typesetting.json').read_text())
t=Typeset(D/config['background'],D,ROOT/'fonts')
for a in config['labels']:
 if 'segments' in a:t.text(a['x'],a['y'],a['segments'],a['color'])
 else:t.label(a['x'],a['y'],a['text'],a['size'],a['kind'],a['color'])
t.save()
