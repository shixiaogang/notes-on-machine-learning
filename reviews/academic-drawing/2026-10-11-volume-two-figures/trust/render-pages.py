"""Locate real caption pages by TeX aux labels and PDF printed labels, render evidence."""
from pathlib import Path
import json, re, hashlib, argparse, subprocess
import pymupdf as fitz
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
OUT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('slug',choices=['full','vol2']);args=parser.parse_args()
pdf=ROOT/('target/machine-learning-notes.pdf' if args.slug=='full' else 'target/vol2-foundations.pdf')
aux=ROOT/('build/main.aux' if args.slug=='full' else 'build/02-foundations.aux')
freeze=json.loads((OUT/'figure-freeze.json').read_text())
data=aux.read_text();doc=fitz.open(pdf);bylabel={p.get_label():i+1 for i,p in enumerate(doc)}
rows=[]
for figure in freeze['figures']:
 m=re.search(r'\\newlabel\{'+re.escape(figure['label'])+r'\}\{\{([^}]+)\}\{([^}]+)',data)
 assert m,figure['label']
 n=bylabel[m[2]];text=re.sub(r'\s+','',doc[n-1].get_text())
 assert '图'+m[1] in text,(figure['label'],n)
 rows.append({'id':figure['id'],'label':figure['label'],'figure_number':m[1],'printed_page':m[2],'pdf_page':n})
digest=hashlib.sha256(pdf.read_bytes()).hexdigest()
record={'pdf':str(pdf.relative_to(ROOT)),'sha256':digest,'figures':rows,'status':'located and rendered only; visual verdict must be separately recorded'}
(OUT/(args.slug+'-pdf-locations.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
pages=sorted({r['pdf_page'] for r in rows})
subprocess.run(['/Users/robbieshi/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3','scripts/render_pdf_review.py',str(pdf),'--output','build/trust-qa/'+args.slug,'--pages',','.join(map(str,pages)),'--detail','--dpi','140'],cwd=ROOT,check=True)
print(args.slug,digest,','.join(map(str,pages)))
