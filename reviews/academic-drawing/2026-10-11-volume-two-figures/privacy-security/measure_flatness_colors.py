from pathlib import Path
from PIL import Image
import json,numpy as np,hashlib
r=Path.cwd();p=r/'figures/02-foundations/03-trustworthiness/generated';out={}
targets={'Blue':'#7188A3','Green':'#829C8B','Yellow':'#B4A16F','Red':'#A7787D','Purple':'#9588A5'}
rois={
'membership-inference':{'Blue':(80,49,650,56),'Yellow':(870,48,1150,58),'Purple':(80,607,650,615),'Green':(915,283,1110,291),'Red':(865,628,1150,636)},
'dp-sgd-update':{'Blue':(70,205,200,211),'Green':(464,232,554,327),'Yellow':(920,206,1068,212),'Purple':(1268,568,1399,574),'Red':(940,224,1049,286)},
'unlearning-reference':{'Blue':(35,147,320,153),'Red':(380,280,512,286),'Green':(38,677,318,683),'Yellow':(575,147,835,153),'Purple':(1300,416,1504,422)},
'defense-in-depth':{'Blue':(80,25,1475,32),'Green':(80,353,1475,360),'Purple':(80,699,1475,706),'Red':(1194,250,1310,257),'Yellow':(531,111,588,117)}
}
for name,colors in rois.items():
 f=p/name/'background-20261011-outline-muted.png';a=np.array(Image.open(f).convert('RGB'));h,w=a.shape[:2];d={'background':str(f.relative_to(r)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'size_pixels':[w,h],'roles':{}}
 for role,(x0,y0,x1,y1) in colors.items():
  z=a[y0:y1,x0:x1].reshape(-1,3).astype(float);z=z[(z.min(1)<220)&(z.max(1)-z.min(1)>6)]
  if len(z)<10:d['roles'][role]={'roi':[x0,y0,x1,y1],'status':'no usable stroke sample'};continue
  median=np.median(z,0).round(1);target=np.array([int(targets[role][i:i+2],16) for i in [1,3,5]])
  d['roles'][role]={'roi':[x0,y0,x1,y1],'colored_pixels':len(z),'target':targets[role],'median_rgb':median.tolist(),'median_minus_target_rgb':(median-target).round(1).tolist(),'euclidean_rgb_difference':round(float(np.linalg.norm(median-target)),2)}
 d['manual_conclusion']='actual flat white interiors and empty outline shapes viewed; stroke colors are approximate model outputs, not exact code palette'
 out[name]=d
print({n:{k:v.get('median_rgb',v.get('status')) for k,v in d['roles'].items()} for n,d in out.items()})
review=r/'reviews/academic-drawing/2026-10-11-volume-two-figures/privacy-security';(review/'flatness-color-measurements.json').write_text(json.dumps({'method':'Manual ROI selection on diagram strokes excluding all photos; report median of chromatic nonwhite pixels including antialiasing. This is a descriptive deviation record, not an automatic pass gate. No pixels modified.','figures':out},ensure_ascii=False,indent=2)+'\n')
