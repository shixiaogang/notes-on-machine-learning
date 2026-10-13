"""Verify the rendered book embeds each restored raster at its declared size."""
from pathlib import Path
import re,json,fitz,numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
rows=json.loads((ROOT/'figures/03-foundations/00-shared/generated/restoration-report.json').read_text())['records'];aux=(ROOT/'build/03-foundations.aux').read_text();pdf=fitz.open(ROOT/'target/vol3-foundations.pdf');checked=[]
rows.append(dict(id='new-1.1',label='fig:learning-process-scene',asset='figures/03-foundations/01-basics/generated/learning-process-scene/figure.png',body_width_mm=112))
reader_edits=json.loads((HERE/'reader-asset-edits.json').read_text())
rows.extend(dict(id=n,**r) for n,r in reader_edits.items() if r['asset'].endswith('.png') and n not in {r['id'] for r in rows})
pages_by_label={page.get_label():i+1 for i,page in enumerate(pdf)}
for r in rows:
 if r['id']=='085':continue
 m=re.search(r'\\newlabel\{'+re.escape(r['label'])+r'\}\{\{([^}]+)\}\{(\d+)\}',aux);assert m,r['id'];p=pages_by_label[m[2]];page=pdf[p-1]
 im=Image.open(ROOT/r['asset']).convert('RGB');expected=np.array(im);matches=[]
 for image in page.get_images(full=True):
  if (image[2],image[3])!=im.size:continue
  pix=fitz.Pixmap(pdf,image[0]);actual=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width,pix.n)
  if pix.n==3 and np.array_equal(expected,actual):matches.append(image[0])
 assert len(matches)==1,(r['id'],matches)
 rectangles=page.get_image_rects(matches[0]);assert len(rectangles)==1,(r['id'],rectangles)
 rectangle=rectangles[0];width=rectangle.width/72*25.4
 assert abs(width-r['body_width_mm'])<.03,(r['id'],width,r['body_width_mm'])
 assert rectangle in page.rect,(r['id'],rectangle,page.rect)
 checked.append(dict(id=r['id'],pdf_page=p,pixels_identical=True,body_width_mm=width,inside_page=True))
(HERE/'book-figure-audit.json').write_text(json.dumps(dict(pages=len(pdf),checked=checked),ensure_ascii=False,indent=2)+'\n')
print(len(checked),'actual PDF raster images verified: exact pixels, declared widths, no clipping.')
