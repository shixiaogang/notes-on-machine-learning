"""Export the checked TikZ vector panels from the scoped ten-page proof.

Run after compiling figures/trust-vector-proof.tex with jobname figures-proof
into build/volume1-r5-trust/ from repository root.
Book inclusion remains the editable .tex source; this is a separate vector export.
SVG glyphs are true outlines from the PDF's embedded fonts, not bitmap tracing.
"""
from pathlib import Path
import re, json
import pymupdf
import xml.etree.ElementTree as ET
ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
ROOT=Path(__file__).resolve().parent.parent
PROOF=ROOT/'build/volume1-r5-trust'
OUT=ROOT/'figures/vectors'
OUT.mkdir(parents=True,exist_ok=True)
names=['trust-three-layers','trust-uncertainty-sources','trust-certified-region','trust-fairness-incompatibility','trust-decision-consequences','trust-conformal-construction','trust-adversarial-training-loops','trust-fairness-intervention-stages','trust-authorized-execution','trust-fairness-intervention-mechanism']
fonts=[]; objects=[]
with pymupdf.open(PROOF/'figures-proof.pdf') as doc:
    assert len(doc)==len(names)
    for i,name in enumerate(names):
        page=doc[i]
        rects=[pymupdf.Rect(b['bbox']) for b in page.get_text('dict')['blocks'] if b['bbox'][1]>50]
        rects += [r['rect'] for r in page.get_drawings() if r['rect'].y0>50]
        assert rects, name
        box=pymupdf.Rect(min(r.x0 for r in rects)-4,min(r.y0 for r in rects)-4,max(r.x1 for r in rects)+4,max(r.y1 for r in rects)+4)
        out=pymupdf.open()
        out.insert_pdf(doc,from_page=i,to_page=i)
        out[0].set_cropbox(box)
        out.save(OUT/(name+'.pdf'))
        out[0].get_pixmap(dpi=300).save(str(OUT/(name+'.png')))
        svg=out[0].get_svg_image(text_as_path=True)
        assert '<image' not in svg, name
        svg_root=ET.fromstring(svg)
        svg_root.set('width',f'{out[0].rect.width*25.4/72:.6f}mm')
        svg_root.set('height',f'{out[0].rect.height*25.4/72:.6f}mm')
        svg=ET.tostring(svg_root,encoding='unicode')
        (OUT/(name+'.svg')).write_text(svg)
        images=len(out[0].get_images())
        assert images==0,(name,images)
        spans=[s for b in out[0].get_text('dict')['blocks'] if b['type']==0 for l in b['lines'] for s in l['spans']]
        objects.append({'figure':name,'pdf_images':images,'pdf_drawings':len(out[0].get_drawings()),'svg_bitmap_images':svg.count('<image'),'export_size_mm':[out[0].rect.width*25.4/72,out[0].rect.height*25.4/72], 'text_sizes_pt':sorted(set(round(s['size'],2) for s in spans)), 'source':f'figures/{name}.tex'})
        for f in out[0].get_fonts(full=True):
            ex=out.extract_font(f[0]); embedded=len(ex[3]); kind=f[2]
            if kind=='Type3':
                cp=out.xref_get_key(f[0],'CharProcs'); ref=int(cp[1].split()[0])
                refs=re.findall(r'(\d+) 0 R',out.xref_object(ref))
                embedded=sum(len(out.xref_stream(int(x)) or b'') for x in refs)
            fonts.append({'figure':name,'font':f[3],'type':kind,'embedded_program_bytes':embedded})
        out.close()
assert all(f['embedded_program_bytes']>0 for f in fonts)
log=(PROOF/'figures-proof.log').read_text().replace('\n','')
dims=[]
for m in re.finditer(r'TRUSTCHECK\|([^|]+)\|([0-9.]+)pt\|([0-9.]+)pt\|([0-9.]+)pt\|([0-9.]+)mm',log):
    name,w,h,d,limit=m.groups()
    width=float(w)*25.4/72.27; height=(float(h)+float(d))*25.4/72.27
    dims.append({'figure':name,'book_width_mm':width,'book_height_mm':height,'limit_mm':float(limit),'fits':width<=float(limit)+.01})
dims=list({x['figure']:x for x in dims}.values())
assert len(dims)==len(names) and all(x['fits'] for x in dims),dims
for fn,data in [('fonts.json',fonts),('objects.json',objects),('dimensions.json',dims)]:
    (PROOF/fn).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
(PROOF/'validation.json').write_text(json.dumps({'panels':len(names),'pdf_bitmap_images':sum(x['pdf_images'] for x in objects),'svg_bitmap_images':sum(x['svg_bitmap_images'] for x in objects),'all_fonts_embedded':True,'all_fit':True},indent=2)+'\n')
print(f'Exported {len(names)} genuine PDF/SVG/PNG panels; zero bitmap objects; fonts embedded; sizes fit.')
