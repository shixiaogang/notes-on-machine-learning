#!/usr/bin/env python3
"""Export Volume 7 teaching geometry with the actual illustration fonts.

Run from any directory. Exports are sequential; compilation uses this worktree's
build directory. Scientific review is recorded separately from rendering.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import pymupdf as fitz

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file())
HERE = Path(__file__).resolve().parent
COMMON = ROOT / 'figures/00-shared/academic-drawing/preamble.tex'

def batch(sources, destination=None):
    sources = [Path(p).resolve() for p in sources]
    work = ROOT / 'build/vol7-figure-proofs/batch'
    work.mkdir(parents=True, exist_ok=True)
    preamble = COMMON.read_text() + '\n\\colorlet{BookRule}{FigureGrid}\n'
    driver = work / 'figure.tex'
    def input_source(p):
        import re
        match=re.search(r'export-reference-width-mm: ([\d.]+)',p.read_text())
        width=match.group(1) if match else '169'
        return ('\\begingroup\\setlength{\\linewidth}{'+width+'mm}'
                +'\\setlength{\\textwidth}{'+width+'mm}\\input{'
                +str(p.relative_to(ROOT))+'}\\endgroup')
    driver.write_text(preamble + '\n\\begin{document}\n' + '\n'.join(
        input_source(p) for p in sources) + '\n\\end{document}\n')
    with (work/'compile.log').open('w') as log:
        for cmd in ([ 'xelatex', '-no-pdf', '-interaction=nonstopmode', '-halt-on-error',
                      '-output-directory='+str(work), str(driver)],
                    ['xdvipdfmx','-o',str(work/'figure.pdf'),str(work/'figure.xdv')]):
            subprocess.run(cmd,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,check=True)
    logtext=(work/'compile.log').read_text()
    if 'Missing character:' in logtext:
        raise ValueError('Missing glyph in batch; inspect compile.log')
    with fitz.open(work/'figure.pdf') as doc:
        if len(doc)!=len(sources):
            raise ValueError(f'Expected {len(sources)} pages; got {len(doc)}')
        for i,source in enumerate(sources):
            dest=Path(destination) if destination else source.parent
            dest.mkdir(parents=True,exist_ok=True)
            page=doc[i]
            one=fitz.open();one.insert_pdf(doc,from_page=i,to_page=i)
            one.save(dest/(source.stem+'.pdf'));one.close()
            page.get_pixmap(dpi=220).save(dest/(source.stem+'.png'))
            size=[round(v*25.4/72,3) for v in (page.rect.width,page.rect.height)]
            report={'source':str(source.relative_to(ROOT)),
                    'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                    'physical_size_mm':size,'method':'TikZ / XeLaTeX / embedded Fira Math',
                    'raster_images_embedded':len(page.get_images()),
                    'font_manifest':'figures/07-reinforcement-learning/00-shared/tikz/font-provenance.json',
                    'review':'Rendering only; see redraw-manifest.json for scientific and book-page review'}
            (dest/(source.stem+'.render.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
            print(source.stem,size,flush=True)

def render(source, destination=None):
    source = Path(source).resolve()
    rel = source.relative_to(ROOT)
    work = ROOT / 'build/vol7-figure-proofs' / source.stem
    work.mkdir(parents=True, exist_ok=True)
    preamble = COMMON.read_text() + '\n\\colorlet{BookRule}{FigureGrid}\n'
    import re
    match=re.search(r'export-reference-width-mm: ([\d.]+)',source.read_text())
    reference_width=match.group(1) if match else '169'
    driver = work / 'figure.tex'
    driver.write_text(preamble + '\n\\begin{document}\n\\setlength{\\linewidth}{'+reference_width
                      +'mm}\\setlength{\\textwidth}{'+reference_width+'mm}\\input{' + str(rel)
                      + '}\n\\end{document}\n')
    with (work / 'compile.log').open('w') as log:
        subprocess.run(['xelatex', '-no-pdf', '-interaction=nonstopmode',
                        '-halt-on-error', '-output-directory=' + str(work),
                        str(driver)], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT,
                       check=True)
        subprocess.run(['xdvipdfmx', '-o', str(work/'figure.pdf'), str(work/'figure.xdv')],
                       cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
    logtext = (work / 'compile.log').read_text()
    if 'Missing character:' in logtext:
        raise ValueError('Missing glyph: ' + str(rel))
    dest = Path(destination) if destination else source.parent
    dest.mkdir(parents=True, exist_ok=True)
    with fitz.open(work / 'figure.pdf') as doc:
        if len(doc) != 1:
            raise ValueError('Expected one figure page: ' + str(rel))
        doc.save(dest / (source.stem + '.pdf'))
        page = doc[0]
        page.get_pixmap(dpi=220).save(dest / (source.stem + '.png'))
        size = [round(v * 25.4/72, 3) for v in (page.rect.width, page.rect.height)]
        report = {'source':str(rel), 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                  'physical_size_mm':size, 'method':'TikZ / XeLaTeX / embedded Fira Math',
                  'raster_images_embedded':len(page.get_images()),
                  'font_manifest':'figures/07-reinforcement-learning/00-shared/tikz/font-provenance.json',
                  'review':'Rendering only; scientific and book-page review recorded in redraw-manifest.json'}
    (dest / (source.stem + '.render.json')).write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(source.stem, size, flush=True)
    return report

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('sources', nargs='+', type=Path)
    parser.add_argument('--output-dir', type=Path)
    parser.add_argument('--batch', action='store_true')
    args = parser.parse_args()
    if args.batch:
        batch(args.sources,args.output_dir)
    else:
        for source in args.sources:
            render(source, args.output_dir)
