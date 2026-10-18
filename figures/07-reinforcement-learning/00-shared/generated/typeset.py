#!/usr/bin/env python3
"""Real-font overlays on retained, unmodified imagegen backgrounds.

The model artwork is never repainted, traced, recolored or blurred. XeLaTeX
typesets Chinese and exact mathematical notation; its transparent raster layer
is composited at the original background resolution. The final PDF is raster.
"""
from pathlib import Path
import hashlib
from datetime import date
import json
import subprocess
import sys
import pymupdf as fitz
from PIL import Image

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file())
V=ROOT/'figures/07-reinforcement-learning'
COMMON=ROOT/'figures/00-shared/academic-drawing/preamble.tex'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def prepare(folder):
    config=json.loads((folder/'labels.json').read_text())
    bg=Image.open(folder/'background.png')
    w=config['body_width_mm'];h=w*bg.height/bg.width
    lines=['% Text overlay only; model artwork is retained without modification.',
           r'\begin{tikzpicture}[x=1mm,y=1mm,text=BookInk]',
           r'\path[use as bounding box] (0,0) rectangle ('+f'{w},{h}'+');']
    for label in config['labels']:
        x,y=label['xy'];pt=label.get('pt',8);role=label.get('role','primary')
        font=r'\FigureNoteFont' if role=='annotation' else r'\figurefont'
        options=['inner sep=0pt','outer sep=0pt','align='+label.get('align','center'),
                 'anchor='+label.get('anchor','center'),
                 'font='+font+r'\fontsize{'+str(pt)+'}{'+str(pt+2)+r'}\selectfont']
        if 'width' in label:options.append('text width='+str(label['width']*w)+'mm')
        if 'color' in label:options.append('text='+label['color'])
        if label.get('white'):options.extend(['fill=white','inner sep=.5mm'])
        lines.append(r'\node['+','.join(options)+'] at ('+f'{x*w:.4f},{(1-y)*h:.4f}'+') {'+label['text']+'};')
    lines.append(r'\end{tikzpicture}')
    (folder/'labels.tex').write_text('\n'.join(lines)+'\n')
    return w,h,bg.size

def main(keys):
    folders=[]
    for key in keys:
        matches=list(V.glob('*/generated/'+key))
        if len(matches)!=1:raise ValueError('One generated asset expected: '+key)
        folders.append(matches[0])
    sizes=[prepare(p) for p in folders]
    work=ROOT/'build/vol7-generated-typography';work.mkdir(parents=True,exist_ok=True)
    pre=COMMON.read_text().replace(r'\setlength{\PreviewBorder}{2pt}',r'\setlength{\PreviewBorder}{0pt}')
    driver=work/'labels.tex'
    driver.write_text(pre+'\n'+r'\begin{document}'+'\n'+'\n'.join(
        r'\begingroup\input{'+str((p/'labels.tex').relative_to(ROOT))+r'}\endgroup' for p in folders)
        +'\n'+r'\end{document}'+'\n')
    with (work/'compile.log').open('w') as log:
        for cmd in (['xelatex','-no-pdf','-interaction=nonstopmode','-halt-on-error',
                     '-output-directory='+str(work),str(driver)],
                    ['xdvipdfmx','-o',str(work/'labels.pdf'),str(work/'labels.xdv')]):
            subprocess.run(cmd,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,check=True)
    if 'Missing character:' in (work/'compile.log').read_text():raise ValueError('Missing glyph; inspect typography log')
    with fitz.open(work/'labels.pdf') as doc:
        if len(doc)!=len(folders):raise ValueError('Unexpected overlay page count')
        for i,(folder,(w,h,(wp,hp))) in enumerate(zip(folders,sizes)):
            page=doc[i]
            expected=[w*72/25.4,h*72/25.4]
            if max(abs(page.rect.width-expected[0]),abs(page.rect.height-expected[1]))>.8:
                raise ValueError('Overlay exceeds canvas: '+folder.name)
            pix=page.get_pixmap(matrix=fitz.Matrix(wp/page.rect.width,wp/page.rect.width),alpha=True)
            layer=Image.frombytes('RGBA',[pix.width,pix.height],pix.samples)
            if layer.size!=(wp,hp):layer=layer.crop((0,0,wp,hp))
            layer.save(folder/'typography.png')
            bg=Image.open(folder/'background.png').convert('RGBA')
            Image.alpha_composite(bg,layer).convert('RGB').save(folder/'figure.png')
            one=fitz.open();one.insert_pdf(doc,from_page=i,to_page=i);one.save(folder/'typography.pdf');one.close()
            pdf=fitz.open();outpage=pdf.new_page(width=expected[0],height=expected[1])
            outpage.insert_image(outpage.rect,filename=str(folder/'figure.png'))
            pdf.save(folder/'figure.pdf');pdf.close()
            cfg=json.loads((folder/'labels.json').read_text())
            report={'key':folder.name,'date':date.today().isoformat(),'body_width_mm':w,'height_mm':h,
                    'canvas_px':[wp,hp],'effective_ppi':wp/(w/25.4),
                    'main_pt':8,'note_pt':7.5,'label_count':len(cfg['labels']),
                    'font_manifest':'figures/07-reinforcement-learning/00-shared/tikz/font-provenance.json',
                    'fonts':'SourceHanSansSC-Normal; LXGWWenKai-Regular; FiraMath-Regular; only absent math STIXTwoMath',
                    'background_changed_by_typesetter':False,'final_pdf':'raster image, not vector',
                    'generator':str(Path(__file__).relative_to(ROOT)),
                    'assets_sha256':{n:sha(folder/n) for n in ['background.png','labels.json','labels.tex','typography.png','figure.png','figure.pdf']},
                    'review':'Typeset; scientific, collision and final book review required'}
            (folder/'typography-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
            print(folder.name,wp,hp,flush=True)

if __name__=='__main__':
    main(sys.argv[1:] or [p.parent.name for p in V.glob('*/generated/*/labels.json')])
