#!/usr/bin/env python3
"""Replay the two chapter-2 observation-legend TikZ assets.

Uses the project's real font/palette preamble and XeLaTeX -> XDV -> PDF path,
matching figures/00-shared/academic-drawing/render_tikz.py. Compilation is
restricted to build/vol6-ch02-figure-fix, independently of volume builds.
This file is a rendering recipe; source.tex is the editable scientific source.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import fitz

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file())
BASE = ROOT/'figures/06-probabilistic-graphical-models/01-representation/tikz'
KEYS = ('pgm-directed-motifs', 'pgm-directed-collider-descendant')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def render(key):
    dest = BASE/key
    source = dest/'source.tex'
    work = ROOT/'build/vol6-ch02-figure-fix'/key
    work.mkdir(parents=True,exist_ok=True)
    preamble = ROOT/'figures/00-shared/academic-drawing/preamble.tex'
    theme = ROOT/'figures/00-shared/model-generators/muted-theme.tex'
    driver = work/'figure.tex'
    driver.write_text(preamble.read_text()+'\n\\begin{document}\n'
                     +'\\input{'+str(theme.relative_to(ROOT))+'}\n'
                     +'\\input{'+str(source.relative_to(ROOT))+'}\n'
                     +'\\end{document}\n')
    commands = [
        ['xelatex','-no-pdf','-interaction=nonstopmode','-halt-on-error',
         '-output-directory='+str(work.relative_to(ROOT)), str(driver.relative_to(ROOT))],
        ['xdvipdfmx','-o',str((work/'figure.pdf').relative_to(ROOT)),
         str((work/'figure.xdv').relative_to(ROOT))]
    ]
    with (work/'compile.log').open('w') as log:
        for command in commands:
            subprocess.run(command,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,check=True)
    logtext = (work/'compile.log').read_text()
    missing = logtext.count('Missing character:')
    if missing:
        raise ValueError('Missing glyphs in '+key)
    with fitz.open(work/'figure.pdf') as doc:
        if len(doc)!=1:
            raise ValueError('Expected one picture page: '+key)
        page=doc[0]
        doc.save(dest/'figure.pdf')
        (dest/'figure.svg').write_text(page.get_svg_image(text_as_path=True))
        page.get_pixmap(dpi=300,alpha=False).save(dest/'figure.png')
        report={
            'date':'2026-10-16', 'source':str(source.relative_to(ROOT)),
            'source_sha256':sha(source),
            'physical_size_mm':[round(v*25.4/72,3) for v in (page.rect.width,page.rect.height)],
            'raster_images_embedded':len(page.get_images()),
            'actual_pdf_fonts':[item[3] for item in page.get_fonts()],
            'missing_glyphs':missing,'page_count':len(doc),
            'math':'Actual FiraMath-Regular.otf via unicode-math',
            'exports':['PDF','SVG paths','PNG 300 dpi'],
            'status':'rendered; writer visual self-check and final book-page check are separate',
            'volume_theme':str(theme.relative_to(ROOT)), 'theme_sha256':sha(theme),
            'preamble':str(preamble.relative_to(ROOT)), 'preamble_sha256':sha(preamble),
            'recipe':str(Path(__file__).resolve().relative_to(ROOT)),
            'build_directory':str(work.relative_to(ROOT)), 'actual_commands':commands,
            'compile_log':str((work/'compile.log').relative_to(ROOT))
        }
    report['output_sha256']={ext:sha(dest/('figure.'+ext)) for ext in ('pdf','png','svg')}
    (dest/'source.render.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(key,json.dumps(report['physical_size_mm']),'fonts:',report['actual_pdf_fonts'])


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--figure',choices=KEYS,action='append')
    args=parser.parse_args()
    for key in args.figure or KEYS:
        render(key)
