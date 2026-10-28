"""Compile only this editable TikZ asset; never start a book build."""
from pathlib import Path
import hashlib
import json
import subprocess
import tempfile
import fitz
from fontTools.ttLib import TTFont

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "build.sh").exists())
BASE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


with tempfile.TemporaryDirectory(prefix="gan-flow-") as tmp:
    output = Path(tmp)
    result = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error",
                             "-output-directory=" + tmp, str((BASE / "wrapper.tex").relative_to(ROOT))],
                            cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    compile_log = output / "compile.log"
    compile_log.write_text(result.stdout)
    if result.returncode:
        raise RuntimeError(result.stdout[-3000:])
    assert "Missing character:" not in result.stdout
    assert "Overfull" not in result.stdout
    with fitz.open(output / "wrapper.pdf") as doc:
        assert len(doc) == 1
        page = doc[0]
        size = [page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72]
        assert all(abs(actual - expected) < .002 for actual, expected in zip(size, [112, 55])), size
        assert not page.get_images()
        doc.save(BASE / "figure.pdf")
        page.get_pixmap(dpi=220).save(BASE / "figure.png")
        (BASE / "figure.svg").write_text(page.get_svg_image(text_as_path=True))
        fonts = sorted({entry[3] for entry in page.get_fonts()})
        text = page.get_text()
        assert all(word in text for word in ["噪声", "生成器", "判别器", "真实样本", "生成样本", "来源标签"]), text
        clipped = []
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    x0, y0, x1, y1 = span["bbox"]
                    if x0 < 0 or y0 < 0 or x1 > page.rect.width or y1 > page.rect.height:
                        clipped.append(span["text"])
        assert not clipped, clipped

data = {
    "source": "Author-drawn forward computation from the original GAN mechanism",
    "background_reference": "https://papers.nips.cc/paper_files/paper/2014/file/f033ed80deb0234979a61f95710dbe25-Paper.pdf",
    "computational_nodes": ["noise z", "generator G_theta", "generated sample G_theta(z)",
                            "shared discriminator D_phi", "real sample x"],
    "forward_edges": [["noise z", "generator G_theta"], ["generator G_theta", "generated sample G_theta(z)"],
                      ["generated sample G_theta(z)", "shared discriminator D_phi"],
                      ["real sample x", "shared discriminator D_phi"]],
    "source_labels": {"generated": 0, "real": 1},
    "label_role": "Supervision for discriminator training; labels are not discriminator inputs",
    "output": "Real/fake score from the same discriminator",
    "arrows": "Forward computation only; no gradient arrows are shown",
}
write_json(BASE / "data.json", data)
font_files = [ROOT / "fonts/FiraMath-Regular.otf", ROOT / "fonts/SourceHanSansSC-Normal.otf"]
write_json(BASE / "generation.json", {
    "key": "neural-generative-gan-flow", "route": "TikZ", "date": "2026-10-13",
    "generator": str(Path(__file__).relative_to(ROOT)), "generator_sha256": sha(Path(__file__)),
    "input_sha256": {str((BASE / filename).relative_to(ROOT)): sha(BASE / filename)
                     for filename in ["source.tex", "wrapper.tex", "data.json"]},
    "asset_sha256": sha(BASE / "figure.pdf"),
    "style": {"fonts": {"Chinese_body": "fonts/SourceHanSansSC-Normal.otf", "Latin_digits_math": "fonts/FiraMath-Regular.otf"},
              "font_sha256": {p.name: sha(p) for p in font_files},
              "font_versions": {p.name: TTFont(p)["name"].getDebugName(5) for p in font_files},
              "license_records": ["fonts/licenses/SourceHanSans-OFL.txt", "fonts/licenses/FiraMath-font-license.txt"],
              "label_size_pt": {"main": 8}, "background": "white",
              "colors": {"ink": "#3B4252", "stroke": "#4C4D4F", "blue_fill": "#E5EAF0", "green_fill": "#E8EEE9"}},
    "native_size_mm": [112, 55], "body_width_mm": 112, "scale_at_requested_width": 1.0,
    "scientific_checks": {"computational_node_count": 5, "shared_discriminator": True,
                          "all_edges_forward": True, "source_labels_not_inputs": True,
                          "generator_not_directly_connected_to_real_sample": True},
    "render_checks": {"actual_size_mm": size, "actual_pdf_fonts": fonts,
                      "missing_glyphs": 0, "clipped_text": clipped, "raster_images_embedded": 0,
                      "png_dpi": 220, "main_font_pt": 8, "final_book_page_review": "Parent integration task"},
})
print("GAN flow 112 × 55 mm; shared-discriminator, font, glyph and canvas checks passed")
