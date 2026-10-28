#!/usr/bin/env python3
"""Render the exact uniform mean-field triangle teaching diagram with repository fonts and palette.
Run from any directory. Writes only this asset and its worktree-local build folder.
"""
from pathlib import Path
import hashlib, json, subprocess
import fitz
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file())
DEST=Path(__file__).resolve().parent
WORK=ROOT/'build/vol6-ch07-figure-fix/pgm-variational-triangle'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p): return str(p.relative_to(ROOT))
def main():
    WORK.mkdir(parents=True,exist_ok=True)
    preamble=ROOT/'figures/00-shared/academic-drawing/preamble.tex'
    theme=ROOT/'figures/00-shared/model-generators/muted-theme.tex'
    source=DEST/'source.tex'
    driver=WORK/'figure.tex'
    driver.write_text(preamble.read_text()+'\n\\setlength{\\PreviewBorder}{0pt}\n\\begin{document}\n'
                     +'\\input{'+rel(theme)+'}\n\\input{'+rel(source)+'}\n\\end{document}\n')
    commands=[['xelatex','-no-pdf','-interaction=nonstopmode','-halt-on-error',
               '-output-directory='+rel(WORK),rel(driver)],
              ['xdvipdfmx','-o',rel(WORK/'figure.pdf'),rel(WORK/'figure.xdv')]]
    with (WORK/'compile.log').open('w') as log:
        for command in commands: subprocess.run(command,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,check=True)
    logs=(WORK/'compile.log').read_text()
    if 'Missing character:' in logs: raise ValueError('Missing glyphs')
    with fitz.open(WORK/'figure.pdf') as doc:
        if len(doc)!=1: raise ValueError('Expected one picture page')
        page=doc[0]
        doc.save(DEST/'figure.pdf')
        page.get_pixmap(dpi=300,alpha=False).save(DEST/'figure.png')
        page.get_pixmap(dpi=150,alpha=False).save(WORK/'body-size-150dpi.png')
        (DEST/'figure.svg').write_text(page.get_svg_image(text_as_path=True))
        report={'date':'2026-10-16','source':rel(source),'source_sha256':sha(source),
                'physical_size_mm':[round(v*25.4/72,4) for v in (page.rect.width,page.rect.height)],
                'page_count':len(doc),'raster_images_embedded':len(page.get_images()),
                'actual_pdf_fonts':[f[3] for f in page.get_fonts()],
                'actual_font_sizes_pt':sorted(set(round(s['size'],3) for b in page.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans'])),
                'missing_glyphs':0,'recipe':rel(Path(__file__).resolve()),'actual_commands':commands,
                'preamble':rel(preamble),'preamble_sha256':sha(preamble),
                'theme':rel(theme),'theme_sha256':sha(theme),
                'compile_log':rel(WORK/'compile.log'),'body_preview':rel(WORK/'body-size-150dpi.png'),
                'status':'rendered; standalone visual review and final book-page acceptance separate'}
    report['output_sha256']={e:sha(DEST/('figure.'+e)) for e in ('pdf','png','svg')}
    (DEST/'source.render.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
