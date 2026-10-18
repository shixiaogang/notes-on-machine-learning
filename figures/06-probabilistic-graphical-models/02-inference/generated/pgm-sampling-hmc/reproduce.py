"""Replay the retained no-text HMC artwork with actual-font labels only.

The background and topology are immutable for this symbol correction. This is
font composition using the existing project Typeset backend, not image editing.
"""
from pathlib import Path
import argparse,json,hashlib,sys
from PIL import Image
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'build.sh').exists())
SHARED=ROOT/'figures/00-shared/model-generators/generated'
sys.path.insert(0,str(SHARED))
from typeset_common import Typeset,run

def render(out):
    background=HERE/'background.png'
    before=hashlib.sha256(background.read_bytes()).hexdigest()
    t=Typeset(background,out,ROOT/'fonts')
    source=json.loads((HERE/'label-source.json').read_text())
    for a in source:
        if a.get('kind')=='hmc-map':
            # Explicit stacked sub/superscript with a common anchor after Phi.
            size=a['size'];script_size=size*.65
            f=t.font(a['font'],size);fs=t.font(a['font'],script_size)
            pw=t.draw.textlength(a['prefix'],font=f)/3
            sw=t.draw.textlength(a['subscript'],font=fs)/3
            uw=t.draw.textlength(a['superscript'],font=fs)/3
            left=a['center_x']-(pw+max(sw,uw))/2
            t.text(left+pw/2,a['baseline_y'],[run(a['prefix'],a['font'],size)],a['color'])
            t.text(left+pw+sw/2,a['baseline_y'],[run(a['subscript'],a['font'],script_size,size*.18)],a['color'])
            t.text(left+pw+uw/2,a['baseline_y'],[run(a['superscript'],a['font'],script_size,-size*.45)],a['color'])
        else:t.text(a['center_x'],a['baseline_y'],a['segments'],a['color'])
    t.save()
    assert before==hashlib.sha256(background.read_bytes()).hexdigest()
    rgb=Image.open(Path(out)/'figure.png').convert('RGB')
    return {'file_sha256':hashlib.sha256((Path(out)/'figure.png').read_bytes()).hexdigest(),
            'pixel_sha256':hashlib.sha256(rgb.tobytes()).hexdigest(),
            'background_sha256':before,'pixels':list(rgb.size)}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=HERE)
    parser.add_argument('--check',action='store_true');args=parser.parse_args()
    result=render(args.output)
    if args.check:
        expected=json.loads((HERE/'replay-config.json').read_text())['expected_pixel_sha256']
        assert result['pixel_sha256']==expected,(result,expected)
    print(json.dumps(result,indent=2))
