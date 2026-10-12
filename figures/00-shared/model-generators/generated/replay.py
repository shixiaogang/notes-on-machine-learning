"""Replay only actual-font overlays on archived no-text canvases."""
from pathlib import Path
import json,hashlib,argparse,importlib.util
from PIL import Image
from typeset_common import Typeset
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
def replay_figure(folder,out=None):
    folder=Path(folder);config=json.loads((folder/'replay-config.json').read_text())
    out=Path(out) if out else folder
    labels=json.loads((folder/config['labels']).read_text())
    background=folder/config['background']
    composition=config.get('canvas_composition')
    if composition:
        out.mkdir(parents=True,exist_ok=True)
        module_path=folder/composition['panel_renderer']
        spec=importlib.util.spec_from_file_location('analytic_panels',module_path)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        panel_out=out/'analytic-replay';panel_out.mkdir(parents=True,exist_ok=True)
        panels=module.make_panels(panel_out,ROOT/'fonts')
        canvas=Image.open(folder/composition['background']).convert('RGBA')
        canvas=Image.alpha_composite(Image.new('RGBA',canvas.size,'white'),canvas)
        for panel,position in zip(panels,composition['positions']):
            patch=Image.open(panel).convert('RGBA');x,y=position
            assert 0<=x and 0<=y and x+patch.width<=canvas.width and y+patch.height<=canvas.height
            canvas.alpha_composite(patch,(x,y))
        background=out/'replay-composite-canvas.png';canvas.convert('RGB').save(background,dpi=(300,300))
    t=Typeset(background,out,ROOT/'fonts')
    for x in labels:t.text(x['center_x'],x['baseline_y'],x['segments'],x['color'])
    t.save()
    actual=hashlib.sha256(Image.open(out/'figure.png').convert('RGB').tobytes()).hexdigest()
    return actual==config['expected_pixel_sha256']
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--key');p.add_argument('--check-only',action='store_true')
    a=p.parse_args()
    items=json.loads((Path(__file__).parent/'registry.json').read_text())
    for x in items:
        if a.key and x['key']!=a.key:continue
        out=ROOT/'build/figure-replay-check'/x['key'] if a.check_only else None
        ok=replay_figure(ROOT/x['folder'],out);print(x['key'], 'pixel-match' if ok else 'pixel-difference')
        if not ok:raise SystemExit(1)
