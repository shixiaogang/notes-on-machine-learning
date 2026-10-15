"""Typeset true-font labels onto the retained model background, without redrawing it."""
from pathlib import Path
import hashlib,json,collections
from PIL import Image,ImageDraw,ImageFont
from fontTools.ttLib import TTFont
import fitz

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
BASE=Path(__file__).resolve().parent
QA=ROOT/'build/qa/neural-generative-models-followup/figures-a'/BASE.name
QA.mkdir(parents=True,exist_ok=True)
BG=Image.open(BASE/'background.png').convert('RGB')
W,H=BG.size
WIDTH_MM=150
PX_PER_PT=W/(WIDTH_MM/25.4*72)
INK='#3B4252'
FONT_FILES={'zh':ROOT/'fonts/SourceHanSansSC-Normal.otf',
            'math':ROOT/'fonts/FiraMath-Regular.otf',
            'note':ROOT/'fonts/LXGWWenKai-Regular.ttf'}
CMAP={role:TTFont(path).getBestCmap() for role,path in FONT_FILES.items()}
LABELS=[]
def label(name,x,y,segments,anchor='mm'):
    LABELS.append({'id':name,'xy':[x,y],'anchor':anchor,'color':INK,'segments':segments})
def seg(t,role='math',pt=8,dy=0): return {'text':t,'font_role':role,'pt':pt,'dy_px':dy}

label('G title',65,125,[seg('生成器 ', 'zh'),seg('G'),seg('𝜽',pt=6,dy=8)],'lm')
label('D title',65,580,[seg('共享判别器 ', 'zh'),seg('D'),seg('𝝓',pt=6,dy=8)],'lm')
for x,name in [(197,'投影'),(428,'转置卷积'),(700,'转置卷积'),(1000,'转置卷积'),(1310,'转置卷积')]:
    label('G operation '+str(x),x,163,[seg(name,'zh')])
gxs=[120,306,566,848,1155,1440]
label('latent',gxs[0],451,[seg('𝐳∈ℝ'),seg('100',pt=6,dy=-10)])
gdims=['4×4×512','8×8×256','16×16×128','32×32×64','64×64×3']
for x,dim in zip(gxs[1:],gdims): label('G dimension '+dim,x,452,[seg(dim)])
for x in gxs[1:-1]: label('G activation '+str(x),x,490,[seg('BN + ReLU',pt=7.5)])
label('G output activation',1440,490,[seg('tanh',pt=7.5)])
label('latent note',120,490,[seg('随机输入','note',7.5)])
for x in [430,740,1000,1228]:
    label('D convolution '+str(x),x,603,[seg('步幅2卷积','zh')])
label('D scalar convolution',1460,603,[seg('4×4'),seg('卷积','zh')])
label('real source',161,630,[seg('真实','zh',7.5)])
label('generated source',315,630,[seg('生成','zh',7.5)])
dxs=[239,590,871,1110,1328,1517]
ddims=['64×64×3','32×32×64','16×16×128','8×8×256','4×4×512','1']
for x,dim in zip(dxs,ddims): label('D dimension '+dim,x,853,[seg(dim)])
label('D alternative inputs',239,892,[seg('两种来源分别输入','note',7.5)])
label('D first activation',590,913,[seg('Leaky ReLU',pt=7.5)])
for x in dxs[2:-1]:
    label('D hidden normalization '+str(x),x,882,[seg('BN',pt=7.5)])
    label('D hidden activation '+str(x),x,913,[seg('Leaky ReLU',pt=7.5)])
label('D scalar activation',1517,913,[seg('sigmoid',pt=7.5)])

layer=Image.new('RGBA',(W,H),(0,0,0,0))
draw=ImageDraw.Draw(layer)
bounds=[]
for item in LABELS:
    widths=[];fonts=[]
    for s in item['segments']:
        assert all(ord(c) in CMAP[s['font_role']] or c.isspace() for c in s['text']),s
        f=ImageFont.truetype(str(FONT_FILES[s['font_role']]),round(s['pt']*PX_PER_PT))
        fonts.append(f);widths.append(draw.textlength(s['text'],font=f))
        s['px_size']=f.size;s['effective_pt']=f.size/PX_PER_PT
    x,y=item['xy'];total=sum(widths)
    if item['anchor']=='mm': x-=total/2
    item_bounds=[]
    for s,f,width in zip(item['segments'],fonts,widths):
        bbox=draw.textbbox((x,y+s['dy_px']),s['text'],font=f,anchor='lm')
        assert bbox[0]>=0 and bbox[1]>=0 and bbox[2]<=W and bbox[3]<=H,(item,bbox)
        draw.text((x,y+s['dy_px']),s['text'],font=f,anchor='lm',fill=INK)
        item_bounds.append(bbox);x+=width
    bounds.append({'id':item['id'],'bbox':[min(b[0] for b in item_bounds),min(b[1] for b in item_bounds),max(b[2] for b in item_bounds),max(b[3] for b in item_bounds)]})
layer.save(BASE/'text-layer.png')
Image.alpha_composite(BG.convert('RGBA'),layer).convert('RGB').save(BASE/'figure.png')
with fitz.open() as d:
    page=d.new_page(width=WIDTH_MM/25.4*72,height=(WIDTH_MM*H/W)/25.4*72)
    page.insert_image(page.rect,filename=str(BASE/'figure.png'))
    d.save(BASE/'figure.pdf')

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
write(BASE/'labels.json',{'native_pixels':[W,H],'include_width_mm':WIDTH_MM,'labels':LABELS,'actual_bounds':bounds})
common=collections.Counter(BG.getdata()).most_common(12)
write(BASE/'generation.json',{
    'key':BASE.name,'date':'2026-10-13','route':'image_gen blank PNG + Pillow true-font text layer',
    'tool':'image_gen.imagegen built-in','model':'Not exposed by tool','parameters':'Not exposed by tool; opaque white background requested',
    'original_output':'exec-815eb5e4-46bf-4157-ba68-6b40e490270f.png',
    'revision_output':'exec-5e874608-39da-4b50-9a83-d8b701e59828.png',
    'revision':'Corrected discriminator scalar output from three circles to one and enlarged label space; original background retained as background-v1.png',
    'source_sha256':{f:sha(BASE/f) for f in ['background.png','background-v1.png','prompt.txt','prompt-revision-1.txt','render.py','labels.json','data.json']},
    'asset_sha256':{f:sha(BASE/f) for f in ['figure.png','figure.pdf','text-layer.png']},
    'native_pixels':[W,H],'native_size_mm':[WIDTH_MM,WIDTH_MM*H/W],
    'include_width_mm':WIDTH_MM,'scale':1,'effective_ppi':W/(WIDTH_MM/25.4),
    'main_label_pt':8,'secondary_label_pt':7.5,
    'font_files':{r:str(p.relative_to(ROOT)) for r,p in FONT_FILES.items()},
    'font_sha256':{r:sha(p) for r,p in FONT_FILES.items()},
    'font_versions':{r:TTFont(p)['name'].getDebugName(5) for r,p in FONT_FILES.items()},
    'font_licenses':['fonts/licenses/SourceHanSans-OFL.txt','fonts/licenses/FiraMath-font-license.txt','fonts/licenses/LXGWWenKai-OFL.txt'],
    'reference_images':[{'path':'figures/05-neural-network-models/00-shared/generated/'+n+'/figure.png','role':role,'actually_passed_to_tool':True} for n,role in [('cnn-resnet','Flat feature sheets and operator chain'),('cnn-encoder-decoder','Expansion and contraction with feature dimensions'),('transformer-architecture-original','Dashed model group boundaries')]],
    'palette_targets':{'blue':'#7188A3','blue_fill':'#E5EAF0','green':'#829C8B','green_fill':'#E8EEE9','ink':INK},
    'background_most_common_colors':common,'palette_note':'Model background contains approximate raster colors; labels use exact ink value, no recoloring or topology redraw performed.',
    'checks':{'font_cmap_coverage':'passed','label_clipping':0,'main_font_effective_pt_range':[min(s['effective_pt'] for l in LABELS for s in l['segments'] if s['pt']==8),max(s['effective_pt'] for l in LABELS for s in l['segments'] if s['pt']==8)],'book_page_review':'Pending parent integration'},
    'pdf_note':'PDF contains the final PNG as a raster image; it is not vector artwork.'})
write(QA/'label-bounds.json',bounds)
print('DCGAN',BG.size,'150 mm width; labels and cmap checks passed')
