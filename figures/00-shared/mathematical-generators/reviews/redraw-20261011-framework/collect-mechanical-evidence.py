"""Read-only facts and input hashes; deliberately no semantic acceptance fields."""
from pathlib import Path
from collections import Counter
import hashlib,json
from PIL import Image
from fontTools.ttLib import TTFont
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
HERE=Path(__file__).resolve().parent
PART5='figures/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/'
PART6='figures/02-mathematical-preliminaries-lower/03-mathematics-and-machine-learning/'
MODEL=[PART5+'generated/temperature-state-observation',PART6+'generated/static-learning-process',PART6+'generated/interactive-learning-process']
TIKZ=[PART5+'tikz/observer-output-feedback',PART5+'tikz/bellman-policy-and-optimality',PART6+'tikz/learning-task-analysis-tools']
REGIONS=[{'blue':(631,345,642,584),'yellow':(108,384,389,395),'green':(1416,352,1430,429),'red':(1040,141,1063,223)}, {'blue':(412,194,666,204),'green':(68,193,301,203),'red':(1140,194,1429,205),'purple':(1532,539,1790,550),'yellow':(1021,539,1360,550)}, {'blue':(554,64,781,75),'green':(64,283,346,295),'red':(1580,251,1803,264),'purple':(1100,324,1344,337),'yellow':(1574,634,1790,648)}]
TARGETS={'blue':'7188A3','green':'829C8B','yellow':'B4A16F','red':'A7787D','purple':'9588A5'}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'method':'mechanical facts only; samples include antialiasing; not whole-image palette quantization or visual acceptance','models':[],'tikz':[],'fonts':[]}
for relative,regions in zip(MODEL,REGIONS):
 p=ROOT/relative;im=Image.open(p/'background.png').convert('RGB');count=Counter(im.get_flattened_data())
 r={'directory':relative,'pixels':list(im.size),'background_sha256':sha(p/'background.png'),'main_nominal_pt':8,'note_nominal_pt':7.5,'body_width_mm':169,'white_rgb_modes':[{'rgb':list(rgb),'pixels':n} for rgb,n in count.most_common(6)],'stroke_region_samples':[],'label_count':len(json.loads((p/'labels.json').read_text())),'typography':json.loads((p/'typography-check.json').read_text())}
 for meaning,bbox in regions.items():
  crop=im.crop(bbox);sample=Counter(crop.get_flattened_data());dark=[(n,rgb) for rgb,n in sample.items() if min(rgb)<190 and max(rgb)-min(rgb)>12]
  top=sorted(dark,reverse=True)[:5];target=tuple(int(TARGETS[meaning][i:i+2],16) for i in (0,2,4))
  r['stroke_region_samples'].append({'meaning':meaning,'target':'#'+TARGETS[meaning],'bbox':list(bbox),'most_common_chromatic_rgbs':[{'rgb':list(rgb),'pixels':n,'signed_target_delta':[a-b for a,b in zip(rgb,target)]} for n,rgb in top]})
 record['models'].append(r)
for relative in TIKZ:
 p=ROOT/relative;r=json.loads((p/'source.render.json').read_text());r['body_width_mm']=169;r['body_scaling']=169/r['physical_size_mm'][0];r['main_pt_at_body_width']=8*r['body_scaling'];record['tikz'].append(r)
for filename,role,version,license_file in [('SourceHanSansSC-Normal.otf','Chinese main','2.005','SourceHanSans-OFL.txt'),('LXGWWenKai-Regular.ttf','Chinese auxiliary','1.522','LXGWWenKai-OFL.txt'),('FiraMath-Regular.otf','Latin, digits, math','0.3.4','FiraMath-font-license.txt'),('STIXTwoMath-Regular.otf','Only explicit missing script C/H/K/E/M','2.12 b168','STIX-OFL.txt')]:
 p=ROOT/'fonts'/filename;f=TTFont(p);cmap=f.getBestCmap();r={'file':'fonts/'+filename,'role':role,'version':version,'sha256':sha(p),'license':'fonts/licenses/'+license_file,'license_sha256':sha(ROOT/'fonts/licenses'/license_file),'missing_requested_script_glyphs':[f'U+{ord(ch):04X}' for ch in '𝒞ℋ𝒦ℰℳ' if ord(ch) not in cmap]};record['fonts'].append(r)
(HERE/'mechanical-evidence.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
files=[]
for d in MODEL+TIKZ:
 files.extend(p for p in (ROOT/d).rglob('*') if p.is_file())
files.extend(ROOT/p for p in [PART5.replace('figures/','tex/')+'01-action-and-state.tex',PART5.replace('figures/','tex/')+'02-policy-realization-and-control.tex',PART5.replace('figures/','tex/')+'03-policy-value-and-optimization.tex',PART6.replace('figures/','tex/')+'01-mathematics-and-future-research.tex','figures/00-shared/academic-drawing/render_tikz.py','figures/00-shared/academic-drawing/preamble.tex','figures/00-shared/academic-drawing/font-exceptions.tex','tex/styles/figure-palette.tex','tex/styles/figure-common.tex'])
files.extend(HERE/p for p in ['semantic-and-visual-review.md','author-pre-independent-discovery.md','collect-mechanical-evidence.py','mechanical-evidence.json','resource-registry.json','book-page-review.md','book-proof-binding.json','README.md'])
(HERE/'frozen-sources.json').write_text(json.dumps({'date':'2026-10-11','scope':'six figure sources, exact assets, changed body sources and author review','files':{str(p.relative_to(ROOT)):sha(p) for p in sorted(files)}},ensure_ascii=False,indent=2)+'\n')
print('label counts',[(Path(m['directory']).name,m['label_count'],len(m['typography']['missing_glyphs']),len(m['typography']['outside_canvas']),len(m['typography']['label_overlap_pairs']),len(m['typography']['annotated_object_or_line_collisions'])) for m in record['models']])
print('stroke modes',[(Path(m['directory']).name,[(s['meaning'],s['most_common_chromatic_rgbs'][:1]) for s in m['stroke_region_samples']]) for m in record['models']])
