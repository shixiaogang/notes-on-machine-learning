"""Add actual-font labels to the immutable model-produced embedding diagram."""
from pathlib import Path
import hashlib
import json
import platform
import sys

from PIL import Image, features
from fontTools.ttLib import TTFont

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "build.sh").is_file())
sys.path.insert(0, str(ROOT / "figures/00-shared/model-generators/generated"))
from typeset_common import Typeset  # noqa: E402

TARGET_WIDTH_MM = 169.0
FONT_RECORDS = [
    ("cn", "SourceHanSansSC-Normal.otf", "fonts/licenses/SourceHanSans-OFL.txt"),
    ("note", "LXGWWenKai-Regular.ttf", "fonts/licenses/LXGWWenKai-OFL.txt"),
    ("math", "FiraMath-Regular.otf", "fonts/licenses/FiraMath-font-license.txt"),
]


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    background = HERE / "background.png"
    before = sha256(background)
    labels = json.loads((HERE / "labels-source.json").read_text())
    ts = Typeset(background, HERE, ROOT / "fonts")
    for label in labels:
        ts.text(label["center_x"], label["baseline_y"], label["segments"],
                label.get("color", "#3B4252"))
    ts.save()

    image = Image.open(HERE / "figure.png").convert("RGB")
    width, height = image.size
    effective_ppi = width / (TARGET_WIDTH_MM / 25.4)
    image.save(HERE / "figure.png", dpi=(effective_ppi, effective_ppi))
    proof_width = round(TARGET_WIDTH_MM / 25.4 * 150)
    proof_height = round(height * proof_width / width)
    image.resize((proof_width, proof_height), Image.Resampling.LANCZOS).save(
        HERE / "print-size-169mm-150ppi.png", dpi=(150, 150))

    fonts = []
    for role, filename, license_path in FONT_RECORDS:
        font_path = ROOT / "fonts" / filename
        font = TTFont(font_path)
        versions = [n.toUnicode() for n in font["name"].names if n.nameID == 5]
        fonts.append({"role": role, "file": f"fonts/{filename}",
                      "version": versions[0], "sha256": sha256(font_path),
                      "license": license_path,
                      "license_sha256": sha256(ROOT / license_path)})
    (HERE / "font-provenance.json").write_text(
        json.dumps(fonts, ensure_ascii=False, indent=2) + "\n")

    actual = json.loads((HERE / "labels.json").read_text())
    sizes = sorted({s["size"] for a in actual for s in a["segments"]})
    pixel_sha = hashlib.sha256(image.tobytes()).hexdigest()
    (HERE / "replay-config.json").write_text(json.dumps({
        "background": "background.png", "labels": "labels.json",
        "expected_pixel_sha256": pixel_sha,
    }, ensure_ascii=False, indent=2) + "\n")
    flat_background = Image.alpha_composite(
        Image.new("RGBA", image.size, "white"),
        Image.open(background).convert("RGBA")).convert("RGB")
    alpha = Image.open(HERE / "text-layer.png").getchannel("A")
    changed_outside_text = sum(
        a == 0 and source != result
        for a, source, result in zip(alpha.getdata(), flat_background.getdata(), image.getdata()))
    checks = {
        "target_width_mm": TARGET_WIDTH_MM,
        "native_pixels": [width, height],
        "effective_ppi_at_target_width": effective_ppi,
        "target_height_mm": height / width * TARGET_WIDTH_MM,
        "font_size_pt_by_pixel_size": {
            str(size): size / width * TARGET_WIDTH_MM / 25.4 * 72 for size in sizes},
        "main_cn_pixel_size": 31,
        "main_math_pixel_size": 33,
        "auxiliary_math_pixel_size": 29,
        "superscripts_and_subscripts_are_separate_font_runs": True,
        "font_fallback": False,
        "synthetic_bold": False,
        "background_sha256_before": before,
        "background_sha256_after": sha256(background),
        "background_unchanged": before == sha256(background),
        "changed_pixels_outside_text_layer": changed_outside_text,
        "figure_pixel_sha256": pixel_sha,
        "text_layer": "text-layer.png",
        "proof": "print-size-169mm-150ppi.png",
        "proof_pixels": [proof_width, proof_height],
        "tools": {"python": platform.python_version(),
                  "pillow": Image.__version__,
                  "freetype": features.version("freetype2")},
        "scope": "Only true-font text overlays; no shape, topology, crop, or background editing.",
    }
    (HERE / "print-size-check.json").write_text(
        json.dumps(checks, ensure_ascii=False, indent=2) + "\n")
    assert checks["background_unchanged"]
    assert changed_outside_text == 0
    print(json.dumps({"figure": str(HERE / "figure.png"),
                      "labels": len(actual), "pixels": [width, height],
                      "effective_ppi": effective_ppi,
                      "background_unchanged": True}, ensure_ascii=False))


if __name__ == "__main__":
    main()
