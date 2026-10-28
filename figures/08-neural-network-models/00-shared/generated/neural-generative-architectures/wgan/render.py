"""Compose only actual-font labels; all structural artwork is an imagegen asset."""
from pathlib import Path
import hashlib,json,collections,platform,math
from PIL import Image,ImageDraw,ImageFont,__version__ as pillow_version
from fontTools.ttLib import TTFont
import fontTools,fitz
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
BASE=Path(__file__).resolve().parent
QA=ROOT/'build/qa/neural-generative-models-followup/figures-a/imagegen-replacements'/BASE.name
QA.mkdir(parents=True,exist_ok=True)
BG=Image.open(BASE/'background.png').convert('RGB');W,H=BG.size
WIDTH_MM=150
PX_PER_PT=W/(WIDTH_MM/25.4*72)
INK='#3B4252'
FONT_FILES={'zh':ROOT/'fonts/SourceHanSansSC-Normal.otf','math':ROOT/'fonts/FiraMath-Regular.otf','note':ROOT/'fonts/LXGWWenKai-Regular.ttf'}
CMAP={r:TTFont(p).getBestCmap() for r,p in FONT_FILES.items()}
LABELS=[]
def seg(t,role='math',pt=8,dy=0):return {'text':t,'font_role':role,'pt':pt,'dy_px':dy}
def label(name,x,y,segments,anchor='mm'):LABELS.append({'id':name,'xy':[x,y],'anchor':anchor,'color':INK,'segments':segments})
def text(name,x,y,t,role='zh',pt=8,anchor='mm'):label(name,x,y,[seg(t,role,pt)],anchor)
text('main network title',523,156,'采样网络与实值评价器')
label('latent',107,377,[seg('随机输入 ','zh'),seg('𝐳')])
label('G generator title',459,337,[seg('生成器 ','zh'),seg('G'),seg('𝜽',pt=6,dy=8)])
label('G mechanism',459,369,[seg('隐藏层','note',7.5),seg('→',pt=7.5),seg('观测层','note',7.5)])
label('generated observation',850,325,[seg('生成 ','zh'),seg('𝐱̃')])
label('real observation',850,510,[seg('真实 ','zh'),seg('𝐱')])
label('shared critic title',1230,149,[seg('共享评价器 ','zh'),seg('f'),seg('𝝓',pt=6,dy=8)])
label('critic features',1230,338,[seg('隐藏层','zh'),seg('/'),seg('特征层','zh')])
label('critic linear',1230,514,[seg('线性：无','zh'),seg('sigmoid')])
label('real score output',1475,501,[seg('f'),seg('𝝓',pt=6,dy=8),seg('(𝐱)∈ℝ')])
text('G training goal',340,495,'训练生成器：提高生成观测的评分','note',7.5)
label('clipping alternative',267,632,[seg('WGAN'),seg('：裁剪参数','zh')])
text('clipping label',267,785,'逐个裁剪参数')
label('clipping formula',267,854,[seg('φ'),seg('j',pt=6,dy=8),seg('∈[−c,c]')])
label('GP alternative',1041,631,[seg('WGAN-GP'),seg('：惩罚插值位置的输入梯度范数','zh')])
text('interpolated input',713,785,'插值观测')
text('reused critic',1041,787,'同一评价器')
text('input gradient norm',1370,786,'梯度范数惩罚')
label('interpolation formula',1041,872,[seg('𝐱̄=u𝐱+(1−u)𝐱̃'),seg('，','zh'),seg('u∼Unif[0,1]')])
text('training constraints note',268,954,'下方两种约束任选其一','note',7.5)
text('GP note',1041,954,'下方支路只用于评价器训练','note',7.5)
SS=4
layer=Image.new('RGBA',(W*SS,H*SS),(0,0,0,0));draw=ImageDraw.Draw(layer);bounds=[]
for item in LABELS:
 widths=[];fonts=[]
 for s in item['segments']:
  assert all(ord(c) in CMAP[s['font_role']] or c.isspace() for c in s['text']),s
  f=ImageFont.truetype(str(FONT_FILES[s['font_role']]),math.floor(s['pt']*PX_PER_PT*SS));fonts.append(f)
  widths.append(draw.textlength(s['text'],font=f));s['supersample_px_size']=f.size;s['effective_pt']=f.size/(PX_PER_PT*SS)
 x,y=item['xy'];x*=SS;y*=SS;total=sum(widths)
 if item['anchor']=='mm':x-=total/2
 bs=[]
 for s,f,width in zip(item['segments'],fonts,widths):
  bbox=draw.textbbox((x,y+s['dy_px']*SS),s['text'],font=f,anchor='lm')
  assert bbox[0]>=0 and bbox[1]>=0 and bbox[2]<=W*SS and bbox[3]<=H*SS,(item,bbox)
  draw.text((x,y+s['dy_px']*SS),s['text'],font=f,anchor='lm',fill=INK);bs.append(bbox);x+=width
 bounds.append({'id':item['id'],'bbox':[min(b[0] for b in bs)/SS,min(b[1] for b in bs)/SS,max(b[2] for b in bs)/SS,max(b[3] for b in bs)/SS]})
layer=layer.resize((W,H),Image.Resampling.LANCZOS)
layer.save(BASE/'text-layer.png')
Image.alpha_composite(BG.convert('RGBA'),layer).convert('RGB').save(BASE/'figure.png')
with fitz.open() as d:
 p=d.new_page(width=WIDTH_MM/25.4*72,height=(WIDTH_MM*H/W)/25.4*72);p.insert_image(p.rect,filename=str(BASE/'figure.png'));d.save(BASE/'figure.pdf')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
write(BASE/'labels.json',{'native_pixels':[W,H],'include_width_mm':WIDTH_MM,'text_supersampling':SS,'labels':LABELS,'actual_bounds':bounds})
output=json.loads((BASE/'tool-output.json').read_text())
write(BASE/'generation.json',{'key':'neural-generative-'+BASE.name+'-architecture','date':'2026-10-13','route':'User-requested imagegen no-text structural artwork + actual-font Pillow text layer','tool':'image_gen.imagegen built-in','model_seed':'not exposed by tool','tool_output':output,'parameters':'opaque white background requested; remaining model parameters not exposed','route_selection':json.loads((BASE/'route-selection.json').read_text()),'source_sha256':{f:sha(BASE/f) for f in ['background.png','background-v1.png','prompt.txt','prompt-revision-1.txt','render.py','labels.json','data.json','tool-output.json','route-selection.json']},'asset_sha256':{f:sha(BASE/f) for f in ['figure.png','figure.pdf','text-layer.png']},'native_pixels':[W,H],'native_size_mm':[WIDTH_MM,WIDTH_MM*H/W],'include_width_mm':WIDTH_MM,'scale':1,'effective_ppi':W/(WIDTH_MM/25.4),'main_label_pt':8,'secondary_label_pt':7.5,'subscript_pt':6,'font_files':{r:str(p.relative_to(ROOT)) for r,p in FONT_FILES.items()},'font_sha256':{r:sha(p) for r,p in FONT_FILES.items()},'font_versions':{r:TTFont(p)['name'].getDebugName(5) for r,p in FONT_FILES.items()},'font_licenses':['fonts/licenses/SourceHanSans-OFL.txt','fonts/licenses/FiraMath-font-license.txt','fonts/licenses/LXGWWenKai-OFL.txt'],'renderer_versions':{'python':platform.python_version(),'Pillow':pillow_version,'fontTools':fontTools.__version__,'PyMuPDF':fitz.VersionBind},'palette_targets':{'blue':'#7188A3','green':'#829C8B','sand':'#B09C72','ink':INK},'palette_note':'The model background uses approximate raster colors. Labels use exact ink. No nodes, arrows or shapes are drawn or retouched by the label renderer.','background_most_common_colors':collections.Counter(BG.getdata()).most_common(8),'checks':{'font_cmap_coverage':'passed','label_clipping':0,'main_font_effective_pt_range':[min(s['effective_pt'] for l in LABELS for s in l['segments'] if s['pt']==8),max(s['effective_pt'] for l in LABELS for s in l['segments'] if s['pt']==8)],'book_page_review':'Pending parent integration'},'pdf_note':'PDF embeds the final production PNG. It is raster artwork, not a claimed vector image.'})
write(QA/'label-bounds.json',bounds)
print(BASE.name,[W,H],[WIDTH_MM,WIDTH_MM*H/W],'font coverage and clipping passed')
