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
WIDTH_MM=112
PX_PER_PT=W/(WIDTH_MM/25.4*72)
INK='#3B4252'
FONT_FILES={'zh':ROOT/'fonts/SourceHanSansSC-Normal.otf','math':ROOT/'fonts/FiraMath-Regular.otf','note':ROOT/'fonts/LXGWWenKai-Regular.ttf'}
CMAP={r:TTFont(p).getBestCmap() for r,p in FONT_FILES.items()}
LABELS=[]
def seg(t,role='math',pt=8,dy=0):return {'text':t,'font_role':role,'pt':pt,'dy_px':dy}
def label(name,x,y,segments,anchor='mm'):LABELS.append({'id':name,'xy':[x,y],'anchor':anchor,'color':INK,'segments':segments})
def text(name,x,y,t,role='zh',pt=8,anchor='mm'):label(name,x,y,[seg(t,role,pt)],anchor)
label('G transition title',627,63,[seg('生成器：','zh'),seg('16×16→32×32'),seg('训练过渡','zh')])
text('shared G features',121,438,'旧生成特征')
text('shared G resolution',121,478,'16×16','math')
label('old toRGB',405,180,[seg('旧','zh'),seg('toRGB')])
text('old RGB dimension',405,220,'16×16×3','math')
label('old output upsample',708,180,[seg('上采样','zh'),seg('2×')])
text('upsampling method',708,220,'最近邻')
label('new G upsample',405,407,[seg('上采样','zh'),seg('2×')])
text('new G convolution',405,451,'新增卷积层')
label('new toRGB',708,407,[seg('新','zh'),seg('toRGB')])
text('new RGB dimension',708,451,'32×32×3','math')
text('G weighted sum',929,309,'+','math')
text('old G weight',880,164,'1−α','math')
text('new G weight',879,464,'α','math')
text('G output',1113,359,'输出图像')
text('G output dimension',1113,389,'32×32×3','math',7.5)
text('D transition title',627,627,'判别器：新入口接入旧主体')
text('D input image',120,981,'输入图像')
text('D input dimension',120,1020,'32×32×3','math')
label('old image downsample',411,729,[seg('下采样','zh'),seg('0.5×')])
text('D pooling method',411,770,'平均池化')
label('old fromRGB',702,729,[seg('旧','zh'),seg('fromRGB')])
label('old entry dimension',702,770,[seg('16×16'),seg('特征','zh')])
label('new fromRGB',411,943,[seg('新','zh'),seg('fromRGB')])
label('new entry dimension',411,984,[seg('32×32'),seg('特征','zh')])
text('new D convolution',702,943,'新增卷积层')
label('new D downsample',702,984,[seg('下采样','zh'),seg('0.5×')])
text('D weighted sum',960,865,'+','math')
text('old D weight',887,712,'1−α','math')
text('new D weight',840,932,'α','math')
label('old D body',961,1137,[seg('旧判别层','zh'),seg('→'),seg('得分','zh')])
label('old D resolution',961,1168,[seg('16×16',pt=7.5),seg('及更低分辨率','zh',7.5)])
label('fade in note',251,1145,[seg('α',pt=7.5),seg('从','note',7.5),seg('0',pt=7.5),seg('增至','note',7.5),seg('1',pt=7.5),seg('：训练阶段切换','note',7.5)])
label('remove shortcuts note',251,1197,[seg('完成后移除旧入口','note',7.5),seg('/',pt=7.5),seg('出口支路','note',7.5)])
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
