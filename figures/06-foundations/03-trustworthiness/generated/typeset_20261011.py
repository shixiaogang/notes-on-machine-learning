"""Add exact book-font labels only. Never redraw or clean model backgrounds."""
from pathlib import Path
import argparse, json, sys, hashlib
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/06-foundations/00-shared/generated'))
from typeset_common import Typeset, FONT_FILES

def render(folder):
    folder=Path(folder).resolve()
    config=json.loads((folder/'typesetting-20261011.json').read_text())
    t=Typeset(folder/config['background'],folder,ROOT/'fonts')
    for label in config['labels']:
        if 'segments' in label:t.text(label['x'],label['y'],label['segments'],label['color'])
        else:t.label(label['x'],label['y'],label['text'],label['size'],label['kind'],label['color'])
    t.save()
    px=t.base.width; width=config['physical_width_mm']
    records=[]
    for label in t.labels:
        for segment in label['segments']:
            records.append({'text':segment['text'],'font':FONT_FILES[segment['font']],
                'font_size_pixels':segment['size'],'font_size_at_print_pt':segment['size']*width/25.4*72/px})
    proof={'background':config['background'],'background_sha256':hashlib.sha256((folder/config['background']).read_bytes()).hexdigest(),
        'physical_width_mm':width,'pixel_width':px,'labels':records,
        'font_sha256':{name:hashlib.sha256((ROOT/'fonts'/name).read_bytes()).hexdigest() for name in set(FONT_FILES.values())},
        'font_versions_and_licenses':'figures/00-shared/academic-drawing/font-manifest.json',
        'no_synthetic_bold':True,'background_processing':'none; typesetting overlay only'}
    (folder/'typography-20261011.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
    print(folder.name,'typeset',width,'mm',flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('folders',nargs='+');args=parser.parse_args()
    for folder in args.folders:render(folder)
