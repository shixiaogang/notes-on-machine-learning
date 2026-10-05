"""Export 15 accepted chapter 4–9 diagrams as genuine vector PDF and SVG.

Run from the repository root with Python 3 and PyMuPDF installed. By default
compile the accompanying project-dependent TeX export sheet with XeLaTeX.
--proof PATH reuses an already compiled vector-only sheet in the same order.
The SVG contains font outlines; editable text remains in figures/*.tex.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import xml.etree.ElementTree as ET
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "figures/vectors"
BUILD = ROOT / "build/theory-vector-export"
FIGURES = [
    ("4.2", "no-free-lunch", 112, 50),
    ("5.5", "rademacher-flips", 167.76, 105.99),
    ("8.3", "spectral-product", 112, 70),
    ("8.4", "ntk-linearization", 169, 74),
    ("8.6", "minimum-norm", 86.67, 63.72),
    ("9.2", "support-coverage", 112, 57),
    ("9.3", "alignment-counterexample", 112, 77),
    ("9.4", "domain-classifier", 112, 62),
    ("9.5", "importance-weighting", 112, 66),
    ("7.2", "stability", 169, 56),
    ("7.3", "conditional-information", 112, 76),
    ("8.1", "deep-selection", 112, 72),
    ("8.5", "ntk-features", 112, 69),
    ("9.6", "environment-sampling", 112, 78),
    ("4.4", "model-selection", 112, 70),
]
MODEL_REFERENCE = {
    suffix: f"figures/scenes/v1r4-theory-{suffix}.png"
    for suffix in ("stability", "conditional-information", "deep-selection", "ntk-features", "environment-sampling")
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proof", type=Path)
    args = parser.parse_args()
    BUILD.mkdir(parents=True, exist_ok=True)
    if args.proof:
        proof_path = args.proof.resolve()
    else:
        # The export sheet has no index entries. Avoid the book's index style
        # path, which is relative to its different build-directory depth.
        subprocess.run([
            "latexmk", "-g", "-xelatex", "-interaction=nonstopmode", "-halt-on-error",
            "-e", '$makeindex = "makeindex %O -o %D %S";',
            f"-outdir={BUILD}", "figures/vectors/theory-r5-export.tex",
        ], cwd=ROOT, check=True)
        proof_path = BUILD / "theory-r5-export.pdf"
    proof = pymupdf.open(proof_path)
    assert len(proof) == len(FIGURES)
    manifest = []
    for i, (number, suffix, width, height) in enumerate(FIGURES):
        name = f"learning-theory-{suffix}"
        assert not proof[i].get_images(full=True), f"Raster on page {i+1}"
        target = pymupdf.open()
        target.insert_pdf(proof, from_page=i, to_page=i)
        pdf = OUT / f"{name}.pdf"
        svg = OUT / f"{name}.svg"
        target.save(pdf, garbage=4, deflate=True)
        page = target[0]
        svg_text = page.get_svg_image(text_as_path=True)
        tree = ET.fromstring(svg_text)
        # MuPDF's unitless dimensions are PDF points; browsers assume CSS px.
        # Keep the coordinate viewBox and explicitly restore physical size.
        tree.set("width", f"{page.rect.width * 25.4 / 72:.6f}mm")
        tree.set("height", f"{page.rect.height * 25.4 / 72:.6f}mm")
        tags = {node.tag.rsplit("}", 1)[-1] for node in tree.iter()}
        assert "image" not in tags and "text" not in tags
        for node in tree.iter():
            for key, val in node.attrib.items():
                if key.rsplit("}", 1)[-1] == "href":
                    assert val.startswith("#"), f"External SVG reference: {val}"
        ET.register_namespace("", "http://www.w3.org/2000/svg")
        ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
        svg.write_text(ET.tostring(tree, encoding="unicode"), encoding="utf-8")
        fonts = []
        for font in page.get_fonts(full=True):
            xref, extension, kind, name_ = font[:4]
            font_bytes = target.extract_font(xref)[3]
            assert font_bytes, f"Unembedded font {name_}"
            fonts.append({"name": name_, "type": kind, "embedded": True})
        assert not page.get_images(full=True)
        source = ROOT / f"figures/{name}.tex"
        manifest.append({
            "number": number, "source": str(source.relative_to(ROOT)),
            "source_sha256": sha(source), "source_canvas_mm": [width, height],
            "pdf": str(pdf.relative_to(ROOT)), "pdf_sha256": sha(pdf),
            "svg": str(svg.relative_to(ROOT)), "svg_sha256": sha(svg),
            "export_canvas_mm": [page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72],
            "border_mm": 0.5, "pdf_image_count": 0, "svg_image_count": 0,
            "svg_text_mode": "actual glyph outlines", "fonts": fonts,
            "model_reference": MODEL_REFERENCE.get(suffix),
            "route": "TikZ reconstruction of accepted model design" if suffix in MODEL_REFERENCE else "existing exact TikZ construction maintained",
        })
        target.close()
    data = {
        "date": "2026-10-05", "pymupdf_version": pymupdf.VersionBind,
        "proof_sha256": sha(proof_path), "figures": manifest,
        "note": "PDF paths and embedded fonts; SVG paths and actual font outlines. No image embedding or raster-to-vector claim.",
    }
    (OUT / "theory-r5-vector-manifest.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"exports": len(manifest), "pdf_images": 0, "svg_images": 0, "svg_text_as_path": True}))


if __name__ == "__main__":
    main()
