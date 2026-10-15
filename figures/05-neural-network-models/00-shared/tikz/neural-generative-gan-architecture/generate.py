"""Compile this standalone architecture only; do not build any book."""
from pathlib import Path
import hashlib,json,subprocess
import fitz
from fontTools.ttLib import TTFont

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
BASE=Path(__file__).resolve().parent
DATA=json.loads((BASE/'data.json').read_text())
OUT=ROOT/'build/qa/neural-generative-models-followup/figures-a'/BASE.name
OUT.mkdir(parents=True,exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v): p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
r=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',
    '-output-directory='+str(OUT),str((BASE/'wrapper.tex').relative_to(ROOT))],
    cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
(OUT/'compile.log').write_text(r.stdout)
if r.returncode: raise RuntimeError(r.stdout[-4000:])
assert 'Missing character:' not in r.stdout
assert 'Overfull' not in r.stdout
with fitz.open(OUT/'wrapper.pdf') as doc:
    assert len(doc)==1
    page=doc[0]
    size=[page.rect.width*25.4/72,page.rect.height*25.4/72]
    assert all(abs(a-b)<.003 for a,b in zip(size,DATA['native_size_mm'])),size
    assert not page.get_images()
    clipped=[]
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            for span in line.get('spans',[]):
                x0,y0,x1,y1=span['bbox']
                if min(x0,y0)<0 or x1>page.rect.width or y1>page.rect.height: clipped.append(span['text'])
    assert not clipped,clipped
    text=page.get_text()
    fonts=sorted({f[3] for f in page.get_fonts()})
    doc.save(BASE/'figure.pdf')
    page.get_pixmap(dpi=300).save(BASE/'figure.png')
    (BASE/'figure.svg').write_text(page.get_svg_image(text_as_path=True))
font_files=[ROOT/'fonts/SourceHanSansSC-Normal.otf',ROOT/'fonts/FiraMath-Regular.otf',ROOT/'fonts/LXGWWenKai-Regular.ttf']
write(BASE/'generation.json',{
    'key':BASE.name,'route':'TikZ','date':'2026-10-13',
    'generator':str(Path(__file__).relative_to(ROOT)),'generator_sha256':sha(Path(__file__)),
    'input_sha256':{f:sha(BASE/f) for f in ['source.tex','wrapper.tex','data.json']},
    'asset_sha256':sha(BASE/'figure.pdf'),'png_sha256':sha(BASE/'figure.png'),
    'native_size_mm':DATA['native_size_mm'],'include_width_mm':DATA['native_size_mm'][0],
    'scale':1.0,'font_size_pt':8,'font_size_at_include_pt':8,'auxiliary_font_pt':7.5,
    'font_sha256':{p.name:sha(p) for p in font_files},
    'font_versions':{p.name:TTFont(p)['name'].getDebugName(5) for p in font_files},
    'font_licenses':['fonts/licenses/SourceHanSans-OFL.txt','fonts/licenses/FiraMath-font-license.txt','fonts/licenses/LXGWWenKai-OFL.txt'],
    'actual_pdf_fonts':fonts,'checks':{'missing_glyphs':0,'clipped_text':clipped,
    'raster_images_embedded':0,'actual_size_mm':size,'book_page_review':'Pending parent integration'},
    'reference_images':DATA['reference_images']})
print(BASE.name, size, 'font, glyph and clipping checks passed')
