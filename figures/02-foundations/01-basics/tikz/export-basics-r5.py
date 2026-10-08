"""Export the already typeset vector-only chapter 1–3 proof, without rasterization.

Run from repository root after compiling build/volume1-r5-basics/proof.tex.
Requires PyMuPDF. SVG glyph outlines preserve the exact WenKai appearance;
editable text and geometry remain in the accompanying TikZ sources.
"""
from pathlib import Path
import argparse
import json
import fitz
import xml.etree.ElementTree as ET

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--proof', type=Path, default=ROOT / "build/volume1-r5-basics/cache/proof.pdf")
parser.add_argument('--qa', type=Path, default=ROOT / "build/volume1-r5-basics")
args = parser.parse_args()
PROOF = args.proof.resolve()
OUT = ROOT / "figures/02-foundations/01-basics/tikz"
QA = args.qa.resolve()
FIGURES = [
    ("1.2", "introduction-nlp-tasks", 111, 59, "v1r3-nlp-tasks.png"),
    ("2.3", "models-discriminative-generative", 168, 113, None),
    ("3.1", "paradigms-supervised-process", 168, 80, "v1r3-supervised.png"),
    ("3.3", "paradigms-reinforcement-loop", 168, 82, "v1r3-reinforcement-upper.png"),
    ("3.5", "paradigms-self-supervised-mask", 111, 81, "v1r4-self-supervised-mask.png"),
    ("3.13", "paradigms-federated-process", 168, 103, "v1r3-federated.png"),
    ("1.3", "introduction-vision-tasks", 168, 60, "v1r4-vision-tasks.png"),
    ("1.4", "introduction-data-split", 111, 60, "v1r3-data-split.png"),
    ("3.7", "paradigms-contrastive-process", 168, 91, "v1r3-contrastive.png"),
    ("3.8", "paradigms-active-learning", 168, 95, "v1r3-active-learning.png"),
    ("3.12", "paradigms-meta-learning", 168, 115, "v1r3-meta-learning.png"),
]

OUT.mkdir(exist_ok=True)
QA.mkdir(exist_ok=True)
proof = fitz.open(PROOF)
assert len(proof) == len(FIGURES)
manifest = []
for index, (number, name, width, height, reference) in enumerate(FIGURES):
    page = proof[index]
    assert not page.get_images(full=True), f"Raster image on proof page {index + 1}"
    boxes = [fitz.Rect(path["rect"]) for path in page.get_drawings()]
    # The section heading ends before y=86pt; all figure spans begin below y=90pt.
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                if span["bbox"][1] >= 90:
                    boxes.append(fitz.Rect(span["bbox"]))
    assert boxes
    crop = fitz.Rect(boxes[0])
    for box in boxes[1:]:
        crop |= box
    crop += (-2, -2, 2, 2)
    target = fitz.open()
    drawing = target.new_page(width=crop.width, height=crop.height)
    drawing.show_pdf_page(drawing.rect, proof, index, clip=crop)
    assert not drawing.get_images(full=True)
    pdf = OUT / f"{name}.pdf"
    svg = OUT / f"{name}.svg"
    target.save(pdf, garbage=4, deflate=True)
    svg_text = drawing.get_svg_image(text_as_path=True)
    assert "<image" not in svg_text
    svg_root = ET.fromstring(svg_text)
    svg_root.set('width', f'{drawing.rect.width * 25.4 / 72:.6f}mm')
    svg_root.set('height', f'{drawing.rect.height * 25.4 / 72:.6f}mm')
    svg_text = ET.tostring(svg_root, encoding='unicode')
    svg.write_text(svg_text, encoding="utf-8")
    # QA previews are rasterizations of the vector export, never production art.
    drawing.get_pixmap(matrix=fitz.Matrix(3, 3)).save(QA / f"vector-{number.replace('.', '-')}.png")
    drawing.get_pixmap(matrix=fitz.Matrix(3, 3), colorspace=fitz.csGRAY).save(QA / f"gray-{number.replace('.', '-')}.png")
    page.get_pixmap(matrix=fitz.Matrix(2.45, 2.45)).save(QA / f"proof-{number.replace('.', '-')}.png")
    manifest.append({
        "figure": number,
        "source": f"figures/02-foundations/01-basics/tikz/{name}.tex",
        "pdf": str(pdf.relative_to(ROOT)),
        "svg": str(svg.relative_to(ROOT)),
        "source_canvas_mm": [width, height],
        "export_crop_pt": list(crop),
        "raster_images": 0,
        "reference_bitmap": f"figures/02-foundations/01-basics/generated/{reference}" if reference else None,
        "route": "complete TikZ reconstruction of accepted model design" if reference else "existing exact TikZ mechanism refined",
    })
    target.close()
(OUT / "records/basics-r5-vector-manifest.json").write_text(
    json.dumps({"date": "2026-10-05", "proof": str(PROOF.relative_to(ROOT)), "figures": manifest}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({"exports": len(manifest), "pdf_rasters": 0, "svg_images": 0}, ensure_ascii=False))
