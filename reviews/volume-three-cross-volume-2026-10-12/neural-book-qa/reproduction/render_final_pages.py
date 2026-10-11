"""Read-only PDF rasterization. Run only after parent supplies the final SHA and page map.

Page map accepted as a list of records or {'neural': {'records': [...]}}.
Rendering and page-text matches are administrative evidence, not visual acceptance.
"""
from pathlib import Path
import argparse, hashlib, json, re, subprocess
from PIL import Image, ImageDraw
from pypdf import PdfReader

BASE = Path(__file__).resolve().parent
ROOT = Path('/Users/robbieshi/Library/Mobile Documents/com~apple~CloudDocs/writings/Notes/Machine Learning/.worktrees/volume-three-optimization')
PDF = ROOT/'target/vol3-models.pdf'
PDFTOPPM = '/Users/robbieshi/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def save(path,obj): path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def flat(s): return re.sub(r'\s+','',s)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--sha',required=True)
    ap.add_argument('--pdf',type=Path,default=ROOT/'target/vol3-models.pdf')
    ap.add_argument('--map',type=Path,required=True)
    ap.add_argument('--preparation',type=Path,default=BASE/'preparation')
    ap.add_argument('--dpi',type=int,default=180)
    a=ap.parse_args()
    PDF=a.pdf
    if sha(PDF)!=a.sha: raise RuntimeError('Final PDF SHA mismatch; no render performed')
    source_identity=json.loads((a.preparation/'00-frozen-source-identity.json').read_text())
    for f in source_identity['source_files']:
        if sha(ROOT/f['path'])!=f['sha256']: raise RuntimeError('Source changed: '+f['path'])
    inventory=json.loads((a.preparation/'01-current-figure-inventory.json').read_text())
    page_map=json.loads(a.map.read_text())
    records=(page_map['neural']['records'] if isinstance(page_map,dict) and 'neural' in page_map
             else page_map['figures'] if isinstance(page_map,dict) and 'figures' in page_map
             else page_map['records'] if isinstance(page_map,dict) else page_map)
    by_label={r['label']:r for r in records}
    missing=[f['label'] for f in inventory['figures'] if f['label'] not in by_label]
    if missing: raise RuntimeError('Missing current figure page labels: '+repr(missing))
    out=BASE/a.sha[:16]
    out.mkdir(parents=True,exist_ok=True)
    reader=PdfReader(PDF)
    text=[p.extract_text() or '' for p in reader.pages]
    norm=[flat(t) for t in text]
    (out/'page-text').mkdir(exist_ok=True)
    figures=[]
    for f in inventory['figures']:
        r=by_label[f['label']]
        figures.append({**f,'new_pdf_page':int(r['pdf_page']),'current_number':r.get('number'),
            'current_page_label':r.get('page_label'),'visual_review_status':'pending-actual-view'})
    prose=json.loads((a.preparation/'02-cross-volume-prose-increments.json').read_text())
    for u in prose:
        # Literal Han runs avoid math and control-sequence interpretations.
        runs=re.findall(r'[\u3400-\u9fff，。；：、（）“”！？]{12,}',u['paragraph'])
        anchors=([r[:28] for r in runs]+[runs[-1][-28:]]) if runs else []
        matches=sorted({i+1 for i,t in enumerate(norm) for anchor in anchors if flat(anchor) in t})
        u['lookup_anchors']=anchors
        u['new_pdf_pages']=matches
        u['visual_review_status']='pending-actual-view'
    pages=sorted({f['new_pdf_page'] for f in figures}|{p for u in prose for p in u['new_pdf_pages']})
    for p in pages:
        (out/'page-text'/f'page-{p:04d}.txt').write_text(text[p-1])
    save(out/'01-current-figure-pages.json',{'pdf_sha256':a.sha,'figures':figures,'pages':sorted({f['new_pdf_page'] for f in figures})})
    save(out/'02-new-prose-pages.json',prose)
    details=out/f'details-{a.dpi}dpi'; details.mkdir(exist_ok=True)
    for p in pages:
        prefix=details/f'page-{p:04d}'
        subprocess.run([PDFTOPPM,'-f',str(p),'-l',str(p),'-r',str(a.dpi),'-png','-singlefile',str(PDF),str(prefix)],check=True)
        print(f'rendered PDF page {p}',flush=True)
    contacts=out/'contacts'; contacts.mkdir(exist_ok=True)
    font_path='/System/Library/Fonts/Supplemental/Arial.ttf'
    from PIL import ImageFont
    try: font=ImageFont.truetype(font_path,18)
    except OSError: font=ImageFont.load_default()
    contact_manifest=[]
    for idx in range(0,len(pages),12):
        batch=pages[idx:idx+12]
        canvas=Image.new('RGB',(4*430,3*640),'#dfe3e7'); draw=ImageDraw.Draw(canvas)
        for j,p in enumerate(batch):
            im=Image.open(details/f'page-{p:04d}.png').convert('RGB'); im.thumbnail((418,606))
            x=(j%4)*430+(430-im.width)//2;y=(j//4)*640+28
            canvas.paste(im,(x,y)); draw.text(((j%4)*430+8,(j//4)*640+4),f'PDF {p}',font=font,fill='#20242b')
        dest=contacts/f'contact-{idx//12+1:02d}.png';canvas.save(dest)
        contact_manifest.append({'path':str(dest),'pdf_pages':batch,'visual_review_status':'pending-actual-view'})
    if sha(PDF)!=a.sha: raise RuntimeError('Root PDF changed during rendering')
    save(out/'00-render-manifest.json',{'pdf_path':str(PDF),'pdf_sha256':a.sha,'page_count':len(reader.pages),'dpi':a.dpi,
        'figure_count':len(figures),'figure_pages':sorted({f['new_pdf_page'] for f in figures}),
        'prose_pages':sorted({p for u in prose for p in u['new_pdf_pages']}),'rendered_pages':pages,'contacts':contact_manifest,
        'unmatched_prose_units':[u['id'] for u in prose if not u['new_pdf_pages']],
        'warning':'Complete render does not constitute visual review. Actual viewing must be recorded separately.'})
    print(str(out),flush=True)
if __name__=='__main__': main()
