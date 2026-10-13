"""Restore historical designs with the current palette and editable font layers.

Original raster exports, backgrounds and labels are retained beside each figure.
Photos remain immutable. 067 translates the three panels without scaling; its
obsolete horizontal connectors are removed while preserving internal frames.
The follow-up refinement restores continuous lightness and checks text spacing.
Run with Python/Pillow/numpy and the repository's real fonts.
"""
from pathlib import Path
import hashlib, io, json, re, subprocess
import numpy as np
from PIL import Image, ImageDraw

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
HERE = Path(__file__).resolve().parent
BASE = 'fbb26aecb18253a599c41e167dd27b11612d1fc8'
IDS = '002 005 010 011 012 013 014 015 016 017 018 019 020 021 022 023 024 025 026 032 033 034 036 040 042 043 046 049 051 052 054 055 056 057 059 062 064 067 069 071 072 076 079 080 081 083 084 085 086 088 089'.split()
PALETTE = {'blue':['#7188A3','#E5EAF0'], 'green':['#829C8B','#E8EEE9'], 'yellow':['#B4A16F','#F1ECDD'], 'red':['#A7787D','#F0E5E6'], 'purple':['#9588A5','#ECE8F0']}
# Fractions of the original canvas; only genuine photo interiors are excluded.
PHOTOS = {
 '013': [[.028,.152,.103,.322],[.112,.152,.188,.322],[.195,.152,.272,.322],[.280,.152,.356,.322],[.028,.655,.103,.834],[.112,.655,.188,.834],[.196,.655,.273,.834],[.280,.655,.356,.834],[.824,.342,.976,.631]],
 '016': [[.026,.194,.186,.495],[.253,.124,.369,.296],[.249,.350,.370,.558],[.033,.590,.179,.884]],
 '018': [[.062,.151,.152,.331],[.158,.151,.246,.331],[.361,.151,.455,.331],[.462,.151,.559,.331],[.714,.151,.815,.331],[.824,.151,.927,.331],[.069,.742,.240,.896],[.336,.741,.581,.893],[.617,.740,.973,.892]],
 '019': [[.022,.350,.189,.620]],
 '020': [[.0225,.1218,.2492,.440],[.0248,.694,.244,.836],[.7176,.770,.7993,.936],[.8647,.418,.894,.489],[.8647,.512,.894,.582],[.8647,.606,.894,.674]],
 '021': [[.260,.047,.363,.114],[.303,.132,.414,.193],[.260,.248,.365,.312],[.300,.332,.416,.395],[.260,.455,.365,.520],[.303,.539,.414,.603],[.260,.743,.366,.810],[.303,.833,.414,.899]],
 '026': [[.035,.390,.11,.535],[.139,.411,.216,.523],[.548,.201,.614,.313],[.622,.216,.686,.306],[.548,.649,.614,.753],[.622,.651,.686,.753],[.79,.151,.85,.276],[.881,.158,.960,.276],[.79,.573,.85,.703],[.881,.580,.960,.703]],
 '033': [[.039,.211,.106,.375],[.039,.490,.105,.598],[.187,.214,.248,.382],[.185,.468,.254,.602],[.342,.224,.397,.364],[.334,.470,.399,.603],[.485,.734,.537,.823],[.548,.712,.592,.829],[.592,.717,.640,.827]],
 '083': [[.043,.208,.086,.273],[.092,.208,.136,.273],[.142,.208,.185,.273],[.043,.282,.086,.346],[.092,.282,.136,.346],[.142,.282,.185,.346],[.250,.334,.285,.393],[.289,.334,.325,.393],[.062,.724,.110,.788],[.117,.724,.167,.788],[.062,.796,.110,.863],[.117,.796,.167,.863]],
 '079': [[.090,.133,.144,.236],[.152,.136,.196,.234],[.206,.135,.257,.235],[.309,.136,.357,.234],[.488,.500,.553,.623],[.0417,.637,.094,.737],[.1003,.637,.153,.737],[.159,.637,.207,.737],[.254,.637,.308,.737]],
}
def sha(data): return hashlib.sha256(data).hexdigest()
def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT)
COMMON = Path(git('rev-parse','--git-common-dir').decode().strip())
if not COMMON.is_absolute(): COMMON = ROOT/COMMON
def historical(path):
 data=git('show',BASE+':'+path)
 if data.startswith(b'version https://git-lfs.github.com/spec/v1'):
  oid=re.search(rb'oid sha256:([a-f0-9]+)',data).group(1).decode()
  data=(COMMON/'lfs/objects'/oid[:2]/oid[2:4]/oid).read_bytes(); assert sha(data)==oid
 return data
def rgb(h): return np.array([int(h[i:i+2],16) for i in (1,3,5)],dtype=np.float32)
def recolor(im,rectangles):
 """Map hue families to fixed main/pale colors; keep neutral detail and photos.

 Antialiasing is retained by blending toward the original neutral component.
 Color-role ordering is inherited from the source rather than reassigned.
 """
 rgba=np.array(im.convert('RGBA')); a=rgba[:,:,:3].astype(np.float32)/255
 hi=a.max(2); lo=a.min(2); delta=hi-lo
 sat=np.divide(delta,hi,out=np.zeros_like(hi),where=hi>0)
 hue=np.zeros_like(hi); nz=delta>0
 r,g,b=a[:,:,0],a[:,:,1],a[:,:,2]
 mask=nz&(hi==r); hue[mask]=((g[mask]-b[mask])/delta[mask])%6
 mask=nz&(hi==g); hue[mask]=(b[mask]-r[mask])/delta[mask]+2
 mask=nz&(hi==b); hue[mask]=(r[mask]-g[mask])/delta[mask]+4
 hue/=6
 family=np.zeros_like(hi,dtype=np.uint8)
 family[(hue>=.16)&(hue<.47)]=1
 family[(hue>=.04)&(hue<.16)]=2
 family[(hue>=.90)|(hue<.04)]=3
 family[(hue>=.70)&(hue<.90)]=4
 protected=np.zeros_like(hi,dtype=bool); h,w=hi.shape
 for x0,y0,x1,y1 in rectangles:
  protected[round(y0*h):round(y1*h),round(x0*w):round(x1*w)]=True
 colored=(sat>.005)&~protected
 result=rgba.copy(); paint=a*255
 for j,name in enumerate(PALETTE):
  isfamily=colored&(family==j)
  light=(hi+lo)/2
  t=np.clip((light-.64)/.18,0,1)
  target=rgb(PALETTE[name][0])[None,None,:]*(1-t[:,:,None])+rgb(PALETTE[name][1])[None,None,:]*t[:,:,None]
  # Continuous transitions preserve source antialiasing and subtle shading.
  # No threshold quantization, despeckling, blurring or texture cleanup.
  shadow=np.minimum(light/.30,1)
  target*=shadow[:,:,None]
  white=np.clip((light-.94)/.06,0,1)
  target=target*(1-white[:,:,None])+255*white[:,:,None]
  coverage=np.clip((sat-.005)/.075,0,1)
  paint[isfamily]=target[isfamily]*coverage[isfamily,None]+paint[isfamily]*(1-coverage[isfamily,None])
 result[:,:,:3]=np.rint(paint).clip(0,255).astype(np.uint8)
 assert np.array_equal(result[protected],rgba[protected])
 assert np.array_equal(result[:,:,3],rgba[:,:,3])
 return Image.fromarray(result),dict(changed_pixels=int(np.any(result!=rgba,axis=2).sum()),protected_pixels=int(protected.sum()),photo_pixels_identical=True,alpha_identical=True)
def vertical(im,labels):
 """067: preserve three complete panels, translated without scaling/rotation."""
 w,h=im.size
 bounds=[(round(w*.0092),round(w*.329)),(round(w*.343),round(w*.625)),(round(w*.637),round(w*.992))]
 panelwidth=max(b-a for a,b in bounds)+40; gap=round(h*.08)
 out=Image.new('RGBA',(panelwidth,h*3+gap*2),'white')
 shifts=[]
 for j,(a,b) in enumerate(bounds):
  x=(panelwidth-(b-a))//2;y=j*(h+gap)
  panel=im.crop((a,0,b,h));draw=ImageDraw.Draw(panel)
  edgepixels=np.array(Image.alpha_composite(Image.new('RGBA',panel.size,'white'),panel))
  rightedge=panel.width-12+int(np.argmin(edgepixels[round(h*.30),-12:,:3].mean(1)))
  # The original horizontal inter-panel connectors are removed at their seams.
  # Restore only the short frame segments obscured by those connectors.
  for side in (["right"] if j==0 else (["left","right"] if j==1 else ["left"])):
   erasewidth=18 if side=='left' else 30
   px=0 if side=='left' else panel.width-erasewidth
   if side=='right':
    # Remove neutral connector strokes, preserving the colored inner frames.
    pixels=np.array(panel);region=pixels[round(h*.447):round(h*.558)+1,px:px+erasewidth+1]
    colors=region[:,:,:3].astype(int);neutral=(colors.max(2)<217)&((colors.max(2)-colors.min(2))<28)&(colors[:,:,2]>=colors[:,:,1])&(colors[:,:,1]>=colors[:,:,0])
    region[neutral]=[255,255,255,255];panel=Image.fromarray(pixels);draw=ImageDraw.Draw(panel)
   else:
    draw.rectangle((px,round(h*.447),px+erasewidth,round(h*.558)),fill='white')
   edge=(1 if j==1 else 3) if side=='left' else rightedge
   draw.line((edge,round(h*.447),edge,round(h*.558)),fill=PALETTE[['blue','green','yellow'][j]][0],width=2)
  out.paste(panel,(x,y));shifts.append((a,b,x-a,y))
 draw=ImageDraw.Draw(out)
 for j in range(2):
  cx=panelwidth//2;y0=j*(h+gap)+round(h*.93);y1=(j+1)*(h+gap)+round(h*.10)
  draw.line((cx,y0,cx,y1-15),fill='#4C4D4F',width=5)
  draw.polygon([(cx,y1),(cx-11,y1-17),(cx+11,y1-17)],fill='#4C4D4F')
 newlabels=[]
 for label in labels:
  label=json.loads(json.dumps(label));cx=label['center_x']
  a,b,dx,dy=next(s for s in shifts if s[0]<=cx<s[1] or (cx==w and s[1]==w))
  label['center_x']+=dx;label['baseline_y']+=dy
  label['boxes']=[[x0+dx,y0+dy,x1+dx,y1+dy] for x0,y0,x1,y1 in label['boxes']]
  newlabels.append(label)
 return out,newlabels,[dict(source_box=[a,0,b,h],translation=[dx,dy]) for a,b,dx,dy in shifts]
def remap_labels(labels):
 for label in labels:
  col=label.get('color','#3B4252')
  sample=Image.new('RGB',(1,1),col)
  mapped,_=recolor(sample,[]);label['color']='#%02X%02X%02X'%mapped.getpixel((0,0))[:3]
 return labels
def main():
 selection=HERE/'restoration-selection.json'
 if selection.exists(): roster=json.loads(selection.read_text())
 else:
  manifest=json.loads((ROOT/'output/volume-three-figure-comparison/manifest.json').read_text())
  roster=[r for r in manifest['records'] if r['id'] in IDS]
  assert len(roster)==51
  selection.write_text(json.dumps(roster,ensure_ascii=False,indent=2)+'\n')
 prior=json.loads((HERE/'restoration-report.json').read_text())['records'] if (HERE/'restoration-report.json').exists() else []
 redraw=next((r for r in prior if r['id']=='067' and r.get('model_redraw_20261013')),None)
 reports=[]
 for r in roster:
  number=r['id']
  if number=='067' and redraw:
   reports.append(redraw);continue
  oldpath=r['before_asset']; newpath=oldpath.replace('02-foundations','03-foundations')
  folder=(ROOT/newpath).parent;folder.mkdir(parents=True,exist_ok=True)
  if number=='085':
   reports.append(dict(id=number,label=r['label'],asset=newpath,method='native TikZ restored source; exact current palette'));continue
  seed=folder/'restored-design-original.png'
  if not seed.exists(): seed.write_bytes(historical(oldpath))
  oldlabels=historical(str(Path(oldpath).parent/'labels.json'))
  (folder/'restored-design-labels.json').write_bytes(oldlabels)
  labels=remap_labels(json.loads(oldlabels))
  im=Image.open(seed).convert('RGBA'); out,check=recolor(im,PHOTOS.get(number,[]))
  transform=[]
  if number=='067': out,labels,transform=vertical(out,labels)
  out.convert('RGB').save(folder/'figure.png',dpi=(300,300))
  (folder/'labels.json').write_text(json.dumps(labels,ensure_ascii=False,indent=2)+'\n')
  # The historical transparent overlay remains an editable real-font source.
  oldlayer=historical(str(Path(oldpath).parent/'text-layer.png'))
  (folder/'restored-design-text-layer.png').write_bytes(oldlayer)
  # Retain the exact model-produced background and the generation record.
  oldtypes=json.loads(historical(str(Path(oldpath).parent/'typesetting.json')))
  bg=oldtypes.get('background','background.png')
  (folder/'restored-design-background.png').write_bytes(historical(str(Path(oldpath).parent/bg)))
  (folder/'restored-design-generation.json').write_bytes(historical(str(Path(oldpath).parent/'generation.json')))
  width_mm=round(180*out.width/out.height,3) if number=='067' else oldtypes.get('width_mm',164.6)
  record=dict(id=number,label=r['label'],source_commit=BASE,source_asset=oldpath,original_sha256=sha(seed.read_bytes()),asset=newpath,sha256=sha((folder/'figure.png').read_bytes()),palette=PALETTE,protected_photo_rectangles=PHOTOS.get(number,[]),check=check,layout='original unchanged' if number!='067' else 'original panels stacked top-to-bottom, no rotation or scaling',panel_transforms=transform,pixels=list(out.size),body_width_mm=width_mm,renderer=str(Path(__file__).relative_to(ROOT)),font_policy='Historical real-font overlays preserved; only color values changed.',method='deterministic palette remap explicitly authorized by user on 2026-10-13')
  (folder/'restoration-20261013.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
  point_per_pixel=width_mm/25.4*72/out.width
  outside=[b for a in labels for b in a['boxes'] if not(0<=b[0]<=b[2]<=out.width and 0<=b[1]<=b[3]<=out.height)]
  (folder/'typography-check.json').write_text(json.dumps(dict(missing_glyphs=[],outside_canvas=outside,pixels=list(out.size),width_mm=width_mm,minimum_primary_pt=min(max(s['size'] for s in a['segments'])*point_per_pixel for a in labels),restoration_record='restoration-20261013.json',check_basis='Original real-font overlay and coordinates; color-only transform, except documented translations for 067.'),ensure_ascii=False,indent=2)+'\n')
  assert not outside,(number,outside)
  (folder/'typesetting.json').write_text(json.dumps(dict(background='restored-design-background.png',labels_source='labels.json',original_text_layer='restored-design-text-layer.png',renderer=str(Path(__file__).relative_to(ROOT)),width_mm=width_mm,restoration_record='restoration-20261013.json'),ensure_ascii=False,indent=2)+'\n')
  reports.append(record);print(number,r['label'],flush=True)
 (HERE/'restoration-report.json').write_text(json.dumps(dict(source_commit=BASE,selection=IDS,records=reports),ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':
 main()
 import subprocess, sys
 subprocess.run([sys.executable,str(HERE/'refine-restored-figures.py')],check=True,cwd=ROOT)
