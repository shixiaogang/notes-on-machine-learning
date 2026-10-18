"""Produce a vector-preserving, same-physical-width before/after proof.

The baseline snapshot directory must contain files at their repository paths.
The task snapshot is made before exporting any native TikZ replacement.
"""
from pathlib import Path
import argparse,json
import pymupdf as fitz

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
MM=72/25.4

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--originals',type=Path,default=ROOT/'build/volume-three-tikz-redraw/originals')
    parser.add_argument('--output',type=Path,default=ROOT/'build/volume-three-tikz-redraw/comparison.pdf')
    args=parser.parse_args()
    records=json.loads((Path(__file__).parent/'architecture-manifest.json').read_text())['records']
    doc=fitz.open();toc=[]
    for item in records:
        old=args.originals/item['old_asset'];new=ROOT/item['asset'];width=item['width_mm']*MM
        with fitz.open(old) as before,fitz.open(new) as after:
            bh=width*before[0].rect.height/before[0].rect.width
            ah=width*after[0].rect.height/after[0].rect.width
            page=doc.new_page(width=390*MM,height=max(bh,ah)+47*MM)
            page.insert_font(fontname='bookcn',fontfile=str(ROOT/'fonts/SourceHanSansSC-Normal.otf'))
            page.insert_text((12*MM,13*MM),'图 '+item['number']+'  '+item['key'],fontname='bookcn',fontsize=12,color=(.23,.26,.32))
            page.insert_text((12*MM,26*MM),'重绘前',fontname='bookcn',fontsize=10,color=(.42,.45,.5))
            page.insert_text((205*MM,26*MM),'TikZ 重绘后',fontname='bookcn',fontsize=10,color=(.28,.39,.51))
            for x,h,pdf,is_original in [(12*MM,bh,before,True),(205*MM,ah,after,False)]:
                box=fitz.Rect(x,33*MM,x+width,33*MM+h)
                if is_original and old.suffix.lower()!='.pdf':page.insert_image(box,filename=str(old))
                else:page.show_pdf_page(box,pdf,0)
            toc.append([1,'图 '+item['number'],len(doc)])
    doc.set_toc(toc);args.output.parent.mkdir(parents=True,exist_ok=True)
    doc.save(args.output,garbage=4,deflate=True);doc.close()
    print(args.output)

if __name__=='__main__':main()
