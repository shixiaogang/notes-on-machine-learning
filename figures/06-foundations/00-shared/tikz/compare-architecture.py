"""Produce a vector-preserving, same-physical-width before/after proof.

The baseline snapshot directory must contain files at their repository paths.
The task snapshot is made before exporting any native TikZ replacement.
"""
from pathlib import Path
import argparse,json,subprocess,hashlib
import pymupdf as fitz

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
MM=72/25.4

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--originals',type=Path,default=ROOT/'build/volume-three-tikz-redraw/originals')
    parser.add_argument('--output',type=Path,default=ROOT/'build/volume-three-tikz-redraw/comparison.pdf')
    parser.add_argument('--checkpoint',help='Optional earlier TikZ commit, shown between original and current')
    parser.add_argument('--checkpoint-label',default='首轮重绘',help='Visible name for the optional middle version')
    parser.add_argument('--keys',nargs='*',help='Optional figure keys for a shorter proof')
    args=parser.parse_args()
    manifest=json.loads((Path(__file__).parent/'architecture-manifest.json').read_text())
    records=[q for q in manifest['records'] if not args.keys or q['key'] in args.keys]
    def git_bytes(commit,path):
        return subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT)
    doc=fitz.open();toc=[]
    for index,item in enumerate(records,1):
        old=args.originals/item['old_asset'];new=ROOT/item['asset'];width=item['width_mm']*MM
        raw=old.read_bytes() if old.exists() else git_bytes(manifest['baseline_commit'],item['old_asset'])
        if hashlib.sha256(raw).hexdigest()!=item['old_sha256']:
            raise ValueError('Original snapshot identity changed: '+item['key'])
        with fitz.open(stream=raw,filetype=old.suffix[1:]) as before,fitz.open(new) as after:
            bh=width*before[0].rect.height/before[0].rect.width
            ah=width*after[0].rect.height/after[0].rect.width
            middle=fitz.open(stream=git_bytes(args.checkpoint,item['asset']),filetype='pdf') if args.checkpoint else None
            mh=width*middle[0].rect.height/middle[0].rect.width if middle else 0
            content_top=126
            page=doc.new_page(width=(583 if middle else 390)*MM,height=max(bh,ah,mh)+content_top+14*MM)
            page.insert_font(fontname='bookcn',fontfile=str(ROOT/'fonts/SourceHanSansSC-Normal.otf'))
            ink=(59/255,66/255,82/255)
            page.insert_text((12*MM,43),f'对照 {index:02d} / {len(records)}   ·   图 '+item['number'],fontname='bookcn',fontsize=32,color=ink)
            page.insert_text((12*MM,98),'图 '+item['number']+' · 原图',fontname='bookcn',fontsize=26,color=ink)
            current_x=398 if middle else 205
            if middle:page.insert_text((205*MM,98),'图 '+item['number']+' · '+args.checkpoint_label,fontname='bookcn',fontsize=26,color=ink)
            page.insert_text((current_x*MM,98),'图 '+item['number']+' · 本次修订',fontname='bookcn',fontsize=26,color=ink)
            panels=[(12*MM,bh,before,True),(current_x*MM,ah,after,False)]
            if middle:panels.insert(1,(205*MM,mh,middle,False))
            for x,h,pdf,is_original in panels:
                box=fitz.Rect(x,content_top,x+width,content_top+h)
                if is_original and old.suffix.lower()!='.pdf':page.insert_image(box,stream=raw)
                else:page.show_pdf_page(box,pdf,0)
            if middle:middle.close()
            toc.append([1,f'对照 {index:02d} · 图 '+item['number'],len(doc)])
    doc.set_toc(toc);args.output.parent.mkdir(parents=True,exist_ok=True)
    doc.save(args.output,garbage=4,deflate=True);doc.close()
    print(args.output)

if __name__=='__main__':main()
