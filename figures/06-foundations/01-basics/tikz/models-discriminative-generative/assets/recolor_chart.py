"""Retain analytical vector panels; match class y=1 to the green mechanism route.
Run from the task repository with PyMuPDF. No curves, coordinates, labels or fonts change.
"""
from pathlib import Path
import fitz
root=Path(__file__).resolve().parents[6]
src=root/'figures/06-foundations/01-basics/matplotlib/models-discriminative-generative/models-discriminative-generative.pdf'
out=Path(__file__).with_name('probability-panels.pdf')
doc=fitz.open(src)
old=b'0.6549019608 0.4705882353 0.4901960784 RG'
new=b'0.5098039216 0.6117647059 0.5450980392 RG'
count=0
for page in doc:
 for xref in page.get_contents():
  stream=doc.xref_stream(xref)
  count+=stream.count(old)
  doc.update_stream(xref,stream.replace(old,new))
if not count: raise RuntimeError('Expected original red class curve not found')
doc.save(out,garbage=3,deflate=True)
print(f'Recolored {count} class-curve and legend strokes')
