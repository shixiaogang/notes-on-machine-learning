"""Compose model raster mechanism + analytical vector charts without flattening charts."""
from pathlib import Path
import json,hashlib
import pymupdf as fitz
ROOT=next(p for p in Path(__file__).resolve().parents if (p/"build.sh").exists())
folder=Path(__file__).resolve().parent/"models-discriminative-generative"
chart=ROOT/"figures/06-foundations/01-basics/matplotlib/models-discriminative-generative/models-discriminative-generative.pdf"
MM=72/25.4
doc=fitz.open(); page=doc.new_page(width=164.6*MM,height=137.8*MM)
page.insert_image(fitz.Rect(0,0,164.6*MM,82.3*MM),filename=str(folder/"figure.png"))
with fitz.open(chart) as source:
 p=source[0]; half=p.rect.height/2
 page.show_pdf_page(fitz.Rect(14.3*MM,88.3*MM,79.3*MM,137.8*MM),source,0,clip=fitz.Rect(0,0,p.rect.width,half))
 page.show_pdf_page(fitz.Rect(85.3*MM,88.3*MM,150.3*MM,137.8*MM),source,0,clip=fitz.Rect(0,half,p.rect.width,p.rect.height))
doc.save(folder/"figure.pdf")
page.get_pixmap(dpi=300).save(folder/"figure-composite.png")
(folder/"composition-20261011.json").write_text(json.dumps(dict(
 physical_size_mm=[164.6,137.8],mechanism_size_mm=[164.6,82.3],
 each_vector_panel_size_mm=[65,49.5],raster_mechanism="figure.png",vector_source=str(chart.relative_to(ROOT)),
 mechanism_sha256=hashlib.sha256((folder/"figure.png").read_bytes()).hexdigest(),
 vector_source_sha256=hashlib.sha256(chart.read_bytes()).hexdigest(),output="figure.pdf",
 status="composed; actual book-page review required"),ensure_ascii=False,indent=2)+"\n")
