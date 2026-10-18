"""Serial export of the editable Volume 3 architecture series.

Run at any location: python3 <this-file> [figure-key ...]. Defaults to the
complete manifest. Requires XeLaTeX, xdvipdfmx and PyMuPDF. Matplotlib mixed
panels are recreated by the two adjacent render-panel.py scripts first.
"""
from pathlib import Path
import json,sys,hashlib,subprocess
import pymupdf as fitz
r=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists()); out=r/'build/volume-three-tikz-redraw';out.mkdir(parents=True,exist_ok=True)
manifest=json.loads((Path(__file__).parent/'architecture-manifest.json').read_text())
keys=set(sys.argv[1:]);rows=[x for x in manifest['records'] if not keys or x['key'] in keys]
if keys-{x['key'] for x in rows}:raise ValueError('Unknown figure key')
sources=[Path(x['source']) for x in rows]
inputs=[r/s for s in sources]+list((Path(__file__).parent/'icons').glob('*.pdf'))+[Path(__file__).parent/'architecture-style.tex']
before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
pre=(r/'figures/00-shared/academic-drawing/preamble.tex').read_text()
pre=pre.replace(r'\input{figures/00-shared/academic-drawing/font-exceptions.tex}',r'''\setmathfont{STIXTwoMath-Regular.otf}[Path=fonts/,range={cal,scr,frak,"2216,"22EE,"22A4,"2713}]
\newfontfamily\FigureMissingMathGlyphFont{STIXTwoMath-Regular.otf}[Path=fonts/]
\usepackage{newunicodechar}
\newunicodechar{✓}{{\FigureMissingMathGlyphFont\char"2713}}''')
driver=out/'batch.tex';driver.write_text(pre+'\n\\begin{document}\n'+''.join('\\begingroup\\input{'+str(s)+'}\\endgroup\n' for s in sources)+'\\end{document}\n')
with (out/'batch-compile.log').open('w') as log:
 subprocess.run(['xelatex','-no-pdf','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(out.relative_to(r)),str(driver.relative_to(r))],cwd=r,stdout=log,stderr=subprocess.STDOUT,check=True)
 subprocess.run(['xdvipdfmx','-o',str(out/'batch.pdf'),str(out/'batch.xdv')],cwd=r,stdout=log,stderr=subprocess.STDOUT,check=True)
log=(out/'batch-compile.log').read_text();missing=[x for x in log.splitlines() if 'Missing character:' in x]
if missing:raise RuntimeError('\n'.join(missing))
after={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
if before!=after:raise RuntimeError('Inputs changed during compilation; export again serially')
records=[]
with fitz.open(out/'batch.pdf') as doc:
 if len(doc)!=len(sources):raise RuntimeError(f'{len(doc)} pages for {len(sources)} sources')
 for i,s in enumerate(sources):
  p=doc[i];dest=r/s.parent;pdf=fitz.open();pdf.insert_pdf(doc,from_page=i,to_page=i);pdf.save(dest/'figure.pdf',garbage=4,deflate=True);pdf.close();p.get_pixmap(dpi=200).save(dest/'figure.png');(dest/'figure.svg').write_text(p.get_svg_image(text_as_path=True))
  item={'source':str(s),'source_sha256':hashlib.sha256((r/s).read_bytes()).hexdigest(),'physical_size_mm':[round(v*25.4/72,3)for v in [p.rect.width,p.rect.height]],'raster_images_embedded':len(p.get_images()),'font_policy':'SourceHanSansSC Normal + LXGWWenKai Regular + FiraMath; STIX Two for cal/scr/frak and U+2216/22EE/22A4/2713 only','status':'rendered; scientific and visual review recorded separately'}
  (dest/'figure.render.json').write_text(json.dumps(item,ensure_ascii=False,indent=2)+'\n');records.append(item);print(str(s),item['physical_size_mm'],flush=True)
(out/'batch-render.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
