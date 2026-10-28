"""Replay actual font labels; improve publication size without changing model artwork."""
from pathlib import Path
import argparse,json,math,itertools,hashlib
from PIL import Image,ImageDraw
from typeset_common import Typeset,SCALE
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())

def rotated(t,a):
 segments=a['segments'];size=segments[0]['size'];side=1000
 tile=Image.new('RGBA',(side,side),(0,0,0,0));d=ImageDraw.Draw(tile)
 for i,s in enumerate(segments):
  by=side/2+(i-(len(segments)-1)/2)*size*1.30*SCALE
  d.text((side/2,by),s['text'],font=t.font(s['font'],s['size']),fill=a['color'],anchor='mm')
 tile=tile.crop(tile.getbbox()).rotate(-a['rotation_clockwise'],resample=Image.Resampling.BICUBIC,expand=True)
 px=round(a['center_x']*SCALE-tile.width/2);py=round(a['center_y']*SCALE-tile.height/2)
 t.layer.alpha_composite(tile,(px,py));bb=tile.getbbox();a['boxes']=[[round((px+bb[0])/SCALE,2),round((py+bb[1])/SCALE,2),round((px+bb[2])/SCALE,2),round((py+bb[3])/SCALE,2)]]
 t.labels.append(a)

def produce(folder,resize=False):
 folder=Path(folder);setting=json.loads((folder/'typesetting.json').read_text());labels=json.loads((folder/('preview-labels.json' if resize else setting['labels_source'])).read_text())
 im=Image.open(folder/setting['background']);point_per_px=setting['width_mm']/25.4*72/im.width
 min_px=math.ceil(setting['min_main_font_pt']/point_per_px)
 if resize:
  for a in labels:
   largest=max(s['size'] for s in a['segments']);factor=max(1,min_px/largest)
   for s in a['segments']:s['size']*=factor;s['dy']*=factor
 t=Typeset(folder/setting['background'],folder,ROOT/'fonts')
 for a in labels:
  if 'rotation_clockwise' in a:rotated(t,a)
  else:t.text(a['center_x'],a['baseline_y'],a['segments'],a['color'])
 t.save()
 def rect(a):return [min(b[0] for b in a['boxes']),min(b[1] for b in a['boxes']),max(b[2] for b in a['boxes']),max(b[3] for b in a['boxes'])]
 overlaps=[]
 for (i,a),(j,b) in itertools.combinations(enumerate(t.labels),2):
  aa=rect(a);bb=rect(b);x=min(aa[2],bb[2])-max(aa[0],bb[0]);y=min(aa[3],bb[3])-max(aa[1],bb[1])
  if x>0 and y>0:overlaps.append({'a':i,'b':j,'overlap':[x,y],'text_a':''.join(s['text'] for s in a['segments']),'text_b':''.join(s['text'] for s in b['segments'])})
 check=json.loads((folder/'typography-check.json').read_text());check.update(label_pair_overlaps=overlaps,width_mm=setting['width_mm'],point_per_px=point_per_px,min_primary_font_pt=min(max(s['size'] for s in a['segments'])*point_per_px for a in t.labels),publication_resized=resize,model_artwork_unchanged=True)
 (folder/'typography-check.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n')
 return check

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('folders',nargs='+');parser.add_argument('--publication-size',action='store_true');args=parser.parse_args()
 for f in args.folders:
  check=produce(ROOT/f,args.publication_size);print(Path(f).name,'overlaps',len(check['label_pair_overlaps']),'minimum pt',round(check['min_primary_font_pt'],2))
