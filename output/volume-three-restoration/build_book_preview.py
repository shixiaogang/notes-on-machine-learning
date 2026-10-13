from pathlib import Path
import re,json,fitz
from PIL import Image,ImageDraw
root=Path.cwd();out=root/'output/volume-three-restoration/qa';dest=out/'all-book-pages';dest.mkdir(exist_ok=True)
rs=json.loads((root/'output/volume-three-figure-comparison/manifest.json').read_text())['records'];aux=(root/'build/03-foundations.aux').read_text();book=fitz.open(root/'target/vol3-foundations.pdf');mapping=[]
rs.append(dict(id='new-1.1',label='fig:learning-process-scene'))
pages_by_label={page.get_label():i+1 for i,page in enumerate(book)}
for r in rs:
 m=re.search(r'\\newlabel\{'+re.escape(r['label'])+r'\}\{\{([^}]+)\}\{(\d+)\}',aux);assert m,r['id'];p=pages_by_label[m[2]]
 mapping.append(dict(id=r['id'],label=r['label'],figure=m[1],printed_page=int(m[2]),pdf_page=p))
 book[p-1].get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False).save(dest/f'{r["id"]}.png')
for start in range(0,len(mapping),9):
 sheet=Image.new('RGB',(2100,2400),'#E5EAF0');draw=ImageDraw.Draw(sheet)
 for j,r in enumerate(mapping[start:start+9]):
  x=j%3*700;y=j//3*800;im=Image.open(dest/f'{r["id"]}.png');im.thumbnail((680,755));sheet.paste(im,(x+(700-im.width)//2,y+32));draw.text((x+10,y+10),r['id']+' / PDF '+str(r['pdf_page']),fill='black')
 sheet.save(out/f'all-book-contact-{start//9+1}.jpg')
(root/'build/figure-restoration/all-page-map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n');print('Rendered',len(mapping),'figure pages; book pages',len(book))
# Sample the comparison PDF at introduction, contour, portrait fairness and text layout.
pdf=fitz.open(root/'output/volume-three-restoration/selected-figures-restored.pdf');sel=json.loads((root/'figures/03-foundations/00-shared/generated/restoration-selection.json').read_text())
for n in ['043','051','067','072','076']:
 idx=next(i for i,r in enumerate(sel) if r['id']==n);pdf[idx].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False).save(out/f'comparison-{n}.png')
