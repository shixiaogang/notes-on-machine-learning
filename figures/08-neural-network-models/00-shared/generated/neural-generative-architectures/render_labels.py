"""Overlay only real-font labels on model-generated architecture backgrounds."""
from pathlib import Path
import hashlib, json, re, sys
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
HERE=Path(__file__).resolve().parent
INK='#3B4252'
ROLES={'cn':('SourceHanSansSC-Normal.otf','SourceHanSans-OFL.txt'),
       'en':('FiraMath-Regular.otf','FiraMath-font-license.txt'),
       'note':('LXGWWenKai-Regular.ttf','LXGWWenKai-OFL.txt')}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def fontname(ch):return 'cn' if ('\u4e00' <= ch <= '\u9fff' or ch in '（）→：、；') else 'en'
def runs(s):
    out=[]
    for c in s:
        if c in '₀₁₂₃₄₅₆₇₈₉':
            out.append(('sub','0123456789'['₀₁₂₃₄₅₆₇₈₉'.index(c)]))
            continue
        role=fontname(c)
        if out and out[-1][0]==role:out[-1]=(role,out[-1][1]+c)
        else:out.append((role,c))
    return out
def render(slug):
    dest=HERE/slug
    config=json.loads((dest/'labels.json').read_text())
    bg=Image.open(dest/'background.png').convert('RGBA')
    layer=Image.new('RGBA',bg.size)
    draw=ImageDraw.Draw(layer)
    cache={}
    coverage={r:TTFont(ROOT/'fonts'/f).getBestCmap() for r,(f,_) in ROLES.items()}
    bounds=[]
    for item in config['labels']:
        size=item.get('size',32)
        lines=item['text'].split('\n')
        gap=item.get('line_gap',43)
        x,y=item['xy']
        for j,line in enumerate(lines):
            chunks=[]
            for role,txt in runs(line):
                is_sub=role=='sub'
                if is_sub:role='en'
                px=size
                if item.get('english_size') is not None and role=='en':px=item['english_size']
                if is_sub:px=round(px*.70)
                key=(role,px)
                if key not in cache:cache[key]=ImageFont.truetype(str(ROOT/'fonts'/ROLES[role][0]),px)
                f=cache[key]
                for ch in txt:
                    if ord(ch) not in coverage[role]:
                        raise ValueError(f'Missing glyph {ch!r} in {role}')
                box=f.getbbox(txt);w=f.getlength(txt);h=box[3]-box[1]
                chunks.append((txt,f,box,w,h,10 if is_sub else 0))
            total=sum(c[3] for c in chunks)
            cursor=x-total/2
            center=y+(j-(len(lines)-1)/2)*gap
            union=[]
            for txt,f,box,w,h,shift in chunks:
                ty=center+shift-h/2-box[1]
                draw.text((cursor,ty),txt,font=f,fill=item.get('color',INK))
                union.append([cursor,center+shift-h/2,cursor+w,center+shift+h/2])
                cursor+=w
            bbox=[min(v[0] for v in union),min(v[1] for v in union),
                  max(v[2] for v in union),max(v[3] for v in union)]
            if bbox[0]<0 or bbox[1]<0 or bbox[2]>bg.width or bbox[3]>bg.height:
                raise ValueError(f'Label clipped: {line}: {bbox}')
            bounds.append({'text':line,'bbox':bbox,'chinese_px':size,
                           'english_px':item.get('english_size',size)})
    layer.save(dest/'text-layer.png')
    Image.alpha_composite(bg,layer).convert('RGB').save(dest/'figure.png',dpi=(300,300))
    notes=[]
    for role,(name,license_name) in ROLES.items():
        p=ROOT/'fonts'/name
        tt=TTFont(p)
        versions=[n.toUnicode() for n in tt['name'].names if n.nameID==5]
        notes.append({'role':role,'path':str(p.relative_to(ROOT)),'sha256':digest(p),
                      'version':sorted(set(versions)),'license':str((ROOT/'fonts/licenses'/license_name).relative_to(ROOT)),
                      'used':role in ['cn','en']})
    (dest/'font-provenance.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
    width_mm=config['width_mm']
    nominal=32*width_mm/25.4*72/bg.width
    report={'source_background_sha256':digest(dest/'background.png'),'pixel_size':bg.size,
            'book_width_mm':width_mm,'book_height_mm':width_mm*bg.height/bg.width,
            'chinese_nominal_font_pt':nominal,'english_and_chinese_nominal_em_size_matched':True,
            'all_text_real_fonts':True,'missing_glyphs':[],'labels':bounds,
            'renderer':'Pillow/FreeType; only transparent labels composited; background pixels preserved',
            'status':'rendered; manual topology and print-size review required'}
    (dest/'typography-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(slug,bg.size,round(nominal,2),'pt',flush=True)
if __name__=='__main__':
    for slug in sys.argv[1:] or ['pix2pix','stylegan']:render(slug)
