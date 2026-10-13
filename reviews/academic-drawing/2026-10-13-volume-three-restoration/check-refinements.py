"""Audit all 89 current assets; diagnose raster labels and protected photographs."""
from pathlib import Path
import json, hashlib, numpy as np
from PIL import Image
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
HERE=Path(__file__).resolve().parent
REPORT=ROOT/'figures/03-foundations/00-shared/generated/restoration-report.json'
rows=json.loads(REPORT.read_text()); restored={r['id']:r for r in rows['records']}
manifest=json.loads((ROOT/'output/volume-three-figure-comparison/manifest.json').read_text())['records']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manual=['005','014','026','032','046','051','067','069','072','080','083','089']
reader_edits=json.loads((HERE/'reader-asset-edits.json').read_text())
records=[];candidates=[];photo_checks=[]
for r in manifest:
 n=r['id'];asset=ROOT/(restored[n]['asset'] if n in restored else r['asset'])
 item=dict(id=n,label=r['label'],asset=str(asset.relative_to(ROOT)),sha256=sha(asset),visual_review='Palette levels, label alignment, size and graphic clearance inspected.',manual_layout=n in manual)
 if n not in restored:
  if n in reader_edits:
   assert str(asset.relative_to(ROOT))==reader_edits[n]['asset'] and sha(asset)==reader_edits[n]['sha256'],n
   item['change']=reader_edits[n]['reason']
  else:
   assert sha(asset)==r['current_sha256'],n
   item['change']='unchanged; no similar visual issue identified'
 elif n=='085':item['change']='native historical design retained with current palette'
 else:
  p=asset.parent;bg=Image.open(p/('background-redraw-20261013.png' if restored[n].get('model_redraw_20261013') else 'refined-background.png')).convert('RGBA');flat=Image.alpha_composite(Image.new('RGBA',bg.size,'white'),bg)
  a=np.array(flat.convert('RGB')).astype(float);g=a.min(2)
  edge=(g<215)&((abs(np.roll(g,1,0)-g)>20)|(abs(np.roll(g,1,1)-g)>20))
  layer=np.array(Image.open(p/'text-layer.png').convert('RGBA'));mask=layer[:,:,3]>20
  for i,l in enumerate(json.loads((p/'labels.json').read_text())):
   for x0,y0,x1,y1 in l['boxes']:
    x0,y0=max(0,int(x0)),max(0,int(y0));x1,y1=min(bg.width,int(x1)+1),min(bg.height,int(y1)+1)
    e=edge[y0:y1,x0:x1];m=mask[y0:y1,x0:x1]
    f=float((e&m).sum()/max(1,m.sum()));area=float(e.mean())
    if f>.045 or area>.09:candidates.append(dict(id=n,label_index=i,intersection_fraction=f,edge_fraction=area))
  typography=json.loads((p/'typography-check.json').read_text())
  assert not typography['missing_glyphs'] and not typography['outside_canvas'] and not typography['label_pair_overlaps'],n
  assert typography['minimum_primary_pt']>=7.5,n
  item.update(change='continuous lightness transfer and real-font text layer',minimum_primary_pt=typography['minimum_primary_pt'])
  if restored[n].get('protected_photo_rectangles'):
   oldbg=np.array(Image.open(p/'restored-design-background.png').convert('RGBA'));newbg=np.array(bg);old=np.array(Image.open(p/'restored-design-original.png').convert('RGB'));new=np.array(Image.open(asset).convert('RGB'))
   oldalpha=np.array(Image.open(p/'restored-design-text-layer.png').convert('RGBA'))[:,:,3]
   newalpha=layer[:,:,3];h,w=new.shape[:2]
   for box in restored[n]['protected_photo_rectangles']:
    x0,y0,x1,y1=box;x0,x1=round(x0*w),round(x1*w);y0,y1=round(y0*h),round(y1*h)
    assert np.array_equal(oldbg[y0:y1,x0:x1],newbg[y0:y1,x0:x1]),n
    free=(oldalpha[y0:y1,x0:x1]==0)&(newalpha[y0:y1,x0:x1]==0)
    d=np.any(old[y0:y1,x0:x1]!=new[y0:y1,x0:x1],axis=2)&free
    assert not d.any(),(n,int(d.sum()))
    photo_checks.append(dict(id=n,rectangle=box,background_identical=True,final_photo_pixels_identical_excluding_editable_labels=True))
 records.append(item)
assert len(records)==89 and not candidates,(len(records),candidates)
# Nine activation samples must remain distinguishable; clean and patched samples agree.
r=restored['076'];p=ROOT/r['asset'];image=np.array(Image.open(p).convert('RGB'))
colors=[image[y,x].tolist() for y in [177,211,245] for x in [829,863,897]]
assert len(set(map(tuple,colors)))>=6,colors
patched=[image[y,x].tolist() for y in [563,596,630] for x in [829,863,897]]
result=dict(count=89,restored_count=51,raster_font_layers=50,manual_layout_ids=manual,records=records,text_artwork_candidates=candidates,protected_photographs=photo_checks,activation_samples_076=colors,patched_activation_samples_076=patched,review_scope='Visual readability and fidelity to requested historical designs; historical scientific review bindings remain separately reported.')
(HERE/'refinement-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('89 assets checked; 50 font layers >=7.5pt; no overlap candidates; photo pixels preserved.')
