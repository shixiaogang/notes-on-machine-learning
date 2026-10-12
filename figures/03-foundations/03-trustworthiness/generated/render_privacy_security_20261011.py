"""Real-font overlays. Model backgrounds are read verbatim; no image cleanup."""
from pathlib import Path
import json, sys, hashlib, shutil, unicodedata
from PIL import Image
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
BASE=ROOT/'figures/03-foundations/03-trustworthiness/generated'
sys.path.insert(0,str(ROOT/'figures/03-foundations/00-shared/generated'))
from typeset_common import Typeset,INK,FONT_FILES
# Actual Fira Math lacks U+2216; this single glyph uses the approved STIX2 exception.
FONT_FILES['stix']='STIXTwoMath-Regular.otf'
POSITIONS={
 'membership-inference':[(365,38),(1010,42),(1010,336),(1010,602),(366,594),(1010,859),(1430,450),(1562,707),(1562,801)],
 'dp-sgd-update':[(136,185),(330,196),(507,196),(640,196),(320,247),(507,288),(640,247),(320,408),(507,449),(640,408),(320,570),(507,610),(640,570),(851,361),(852,457),(996,187),(996,361),(996,457),(1168,361),(1168,455),(1338,361),(1338,457),(1520,356),(1520,550),(1334,558),(1334,713),(825,806),(825,879)],
 'pate-private-teachers':[(620,177),(125,392),(310,380),(310,540),(310,706),(480,235),(480,393),(480,552),(710,280),(709,557),(843,423),(940,264),(936,532),(777,727),(1160,684),(1358,681),(720,862),(720,908)],
 'unlearning-reference':[(175,133),(442,270),(709,133),(709,650),(1107,150),(1401,402),(173,630),(175,956),(707,956),(1106,685),(1190,1010)],
 'backdoor-poisoning':[(1094,145),(395,348),(744,348),(1025,375),(472,498),(389,562),(770,556),(1090,552),(389,762),(770,753),(1090,762),(884,728),(726,1009)],
 'defense-in-depth':[(172,82),(489,82),(818,82),(1113,82),(1382,82),(686,247),(1252,247),(159,412),(436,412),(672,412),(896,412),(1107,412),(1392,412),(608,587),(1258,587),(1436,683),(232,774),(626,774),(982,754),(1338,774)]
}
BACKGROUND={k:('background-20261011-r3.png' if k in ['pate-private-teachers','defense-in-depth'] else 'background-20261011-final.png') for k in POSITIONS}
for _name in ['membership-inference','dp-sgd-update','unlearning-reference','defense-in-depth']:
 BACKGROUND[_name]='background-20261011-outline-muted.png'
def italic(s):
 out=''
 for c in s:
  if c.isalpha() and ord(c)<128:
   name=unicodedata.name(c).replace('LATIN ','').replace(' LETTER','')
   try:c=unicodedata.lookup('MATHEMATICAL ITALIC '+name)
   except KeyError:
    if c=='h':c='ℎ'
  elif c in 'θσ':c=unicodedata.lookup('MATHEMATICAL ITALIC '+unicodedata.name(c).replace('GREEK ','').replace(' LETTER',''))
  out+=c
 return out
for name,positions in POSITIONS.items():
 d=BASE/name
 old=d/'labels-before-20261011.json'
 if not old.exists():shutil.copy2(d/'labels.json',old)
 config=d/'labels-20261011.json'
 if not config.exists():
  labels=json.loads(old.read_text())
  assert len(labels)==len(positions),(name,len(labels),len(positions))
  width=Image.open(d/BACKGROUND[name]).width
  main_px=8*width/(164.6/25.4*72);note_px=7.5*width/(164.6/25.4*72)
  for row,(x,y) in zip(labels,positions):
   row.pop('boxes',None);row.update(center_x=x,baseline_y=y,color=INK)
   is_note=any(s['font']=='note' for s in row['segments'])
   old_max=max(s['size'] for s in row['segments'])
   factor=(note_px if is_note else main_px)/old_max
   for s in row['segments']:
    s['size']=round((note_px if is_note else main_px) if s['size']>=.8*old_max else s['size']*factor,4);s['dy']=round(s.get('dy',0)*factor,4)
    if s['font']=='mi' or (s['font'] in ['math','en'] and s['text'].strip() not in ['clip','Laplace']):
     s['text']=italic(s['text'])
    s['text']=s['text'].replace('\\','∖')
   if name=='unlearning-reference' and row is labels[5]:row['segments']=[dict(text='比较模型分布',font='cn',size=main_px,dy=0)]
   if name=='unlearning-reference' and row is labels[10]:row['segments']=[dict(text='精确遗忘要求模型输出同分布',font='note',size=note_px,dy=0)]
  config.write_text(json.dumps(labels,ensure_ascii=False,indent=2)+'\n')
 labels=json.loads(config.read_text())
 # Explanatory conclusions and update formula are already stated in captions/body.
 omitted={'dp-sgd-update':{26,27},'pate-private-teachers':{16,17},'unlearning-reference':{10},'backdoor-poisoning':{12}}
 labels=[r for i,r in enumerate(labels) if i not in omitted.get(name,set())]
 for row in labels:
  split=[]
  for s in row['segments']:
   if '∖' not in s['text']:split.append(s);continue
   for c in s['text']:split.append(dict(s,text=c,font='stix' if c=='∖' else s['font']))
  row['segments']=split
 t=Typeset(d/BACKGROUND[name],d,ROOT/'fonts')
 for r in labels:t.text(r['center_x'],r['baseline_y'],r['segments'],r['color'])
 t.save()
 report={'background':BACKGROUND[name],'background_sha256':hashlib.sha256((d/BACKGROUND[name]).read_bytes()).hexdigest(),'width_mm':164.6,'source_labels':'labels-20261011.json','font_roles':{'body':'SourceHanSansSC-Normal.otf','note':'LXGWWenKai-Regular.ttf','Latin_digits_math':'FiraMath-Regular.otf','only_missing_U2216':'STIXTwoMath-Regular.otf'},'font_size_pt':{'main':8,'note':7.5,'sub_sup':'65% of base where source uses a mathematical script'},'layer':'text-layer.png, actual fonts; transparent overlay only','figure_sha256':hashlib.sha256((d/'figure.png').read_bytes()).hexdigest(),'status':'rendered; manual review required'}
 (d/'typesetting-20261011.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(name,t.base.size,flush=True)
