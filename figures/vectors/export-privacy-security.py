from pathlib import Path
import subprocess,os
root=Path(__file__).resolve().parents[2]; out=root/'build/volume1-r7-privacy';out.mkdir(exist_ok=True);cache=out/'cache';cache.mkdir(exist_ok=True)
# 原七图顺序保持，R7新增图17.3的独立矢量资源放在最后。
figs=['trust-membership-inference','trust-dp-neighbors','trust-unlearning-reference','trust-threat-model-coordinates','trust-security-entrypoints','trust-prompt-injection-boundary','trust-defense-in-depth','trust-adversarial-perturbation']
wide={'trust-membership-inference','trust-unlearning-reference','trust-threat-model-coordinates','trust-security-entrypoints','trust-prompt-injection-boundary','trust-defense-in-depth'}
s=r'''\PassOptionsToPackage{no-math}{fontspec}
\documentclass[justified,openany,nobib,nols]{tufte-book}
\newif\ifBookVolumeEdition\BookVolumeEditionfalse
\input{tex/preamble}\input{tex/styles/foundation-visual-overrides}
\newsavebox{\ReviewFigureBox}
\begin{document}
'''
for n in figs:
 s+='\\clearpage\n'
 if n in wide:s+='\\begin{fullwidth}\n'
 s+='\\sbox{\\ReviewFigureBox}{\\input{figures/'+n+'}}\n'
 s+='\\typeout{R7PRIVACY|'+n+'|\\the\\wd\\ReviewFigureBox|\\the\\ht\\ReviewFigureBox|\\the\\dp\\ReviewFigureBox|\\the\\linewidth}\n'
 s+='\\noindent\\usebox{\\ReviewFigureBox}\n'
 if n in wide:s+='\\end{fullwidth}\n'
s+='\\end{document}\n';(out/'root-proof.tex').write_text(s)
env=dict(os.environ,TEXINPUTS='./tex//:',T1FONTS='./fonts/stix2-type1/type1//:',TFMFONTS='./fonts/stix2-type1/tfm//:',ENCFONTS='./fonts/stix2-type1/enc//:')
with (out/'root-proof-build.txt').open('w') as log:
 subprocess.run(['xelatex','-no-pdf','-interaction=nonstopmode','-halt-on-error',f'-output-directory={cache}',str(out/'root-proof.tex')],cwd=root,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
 subprocess.run(['xdvipdfmx','-f','fonts/stix2-type1/map/stix2.map','-E','-z','1','-o',str(cache/'root-proof.pdf'),str(cache/'root-proof.xdv')],cwd=root,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
print('Compiled privacy/security proof:',len(figs),'figures')

# 裁切PDF对象后导出；SVG使用真实字体轮廓，无嵌入栅格。
import pymupdf,json,hashlib
import xml.etree.ElementTree as ET
ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
export=root/'figures/vectors'; export.mkdir(exist_ok=True)
doc=pymupdf.open(cache/'root-proof.pdf'); records=[]
for name,page in zip(figs,doc):
 bounds=[pymupdf.Rect(p['rect']) for p in page.get_drawings()]
 bounds += [pymupdf.Rect(s['bbox']) for b in page.get_text('dict')['blocks'] for l in b.get('lines',[]) for s in l['spans'] if s['bbox'][1]>60]
 clip=pymupdf.Rect(bounds[0])
 for r in bounds[1:]: clip|=r
 clip=pymupdf.Rect(clip.x0-2,clip.y0-2,clip.x1+2,clip.y1+2)
 dst=pymupdf.open(); p=dst.new_page(width=clip.width,height=clip.height); p.show_pdf_page(p.rect,doc,page.number,clip=clip)
 pdf=export/(name+'.pdf'); dst.save(pdf,garbage=4,deflate=True)
 # 预览按PDF真实物理尺寸以300dpi渲染；书内仍直接载入矢量TeX。
 p.get_pixmap(dpi=300).save(export/(name+'.png'))
 svg_root=ET.fromstring(p.get_svg_image(text_as_path=True))
 svg_root.set('width',f'{p.rect.width*25.4/72:.6f}mm')
 svg_root.set('height',f'{p.rect.height*25.4/72:.6f}mm')
 (export/(name+'.svg')).write_text(ET.tostring(svg_root,encoding='unicode'))
 assert not p.get_images(full=True)
 records.append({'name':name,'source':'figures/'+name+'.tex','source_sha256':hashlib.sha256((root/'figures'/(name+'.tex')).read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'svg_sha256':hashlib.sha256((export/(name+'.svg')).read_bytes()).hexdigest(),'width_mm':p.rect.width*25.4/72,'height_mm':p.rect.height*25.4/72,'vector':True,'raster_objects':0})
(export/'privacy-security-vector-manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
(out/'export-validation.json').write_text(json.dumps({'proof_sha256':hashlib.sha256((cache/'root-proof.pdf').read_bytes()).hexdigest(),'shared_symbols_sha256':hashlib.sha256((root/'figures/trust-vector-symbols.tex').read_bytes()).hexdigest(),'records':records},ensure_ascii=False,indent=2))
print('Exported',len(records),'true vector PDFs and SVGs')
