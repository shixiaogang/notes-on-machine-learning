"""Verify and render only the chapter 17 deterministic transient comparison."""

from fractions import Fraction
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

import fitz


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
NAME = "same-spectrum-transients"


def verify_coordinates():
    state_a = (Fraction(0), Fraction(1))
    state_c = state_a
    half = Fraction(1, 2)
    for t in range(9):
        assert state_a == (8 * t * half**t, half**t)
        assert state_c == (0, half**t)
        assert sum(x * x for x in state_a) == half ** (2 * t) * (64 * t * t + 1)
        state_a = (half * state_a[0] + 4 * state_a[1], half * state_a[1])
        state_c = (half * state_c[0], half * state_c[1])
    print("Verified all nine states and plotted squared norms using exact fractions.")


def render():
    executable = shutil.which("xelatex")
    converter = shutil.which("xdvipdfmx")
    if not executable or not converter:
        raise RuntimeError("XeTeX is required; this script does not install packages.")
    env = os.environ.copy()
    for key, directory in (
        ("TEXINPUTS", ROOT / "tex"),
        ("T1FONTS", ROOT / "fonts/stix2-type1/type1"),
        ("TFMFONTS", ROOT / "fonts/stix2-type1/tfm"),
        ("ENCFONTS", ROOT / "fonts/stix2-type1/enc"),
    ):
        env[key] = str(directory) + "//" + os.pathsep + env.get(key, "")
    cache = ROOT / "build/math-restructure-figures/ch17"
    cache.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="render-", dir=cache) as output:
        commands = [
            [
                executable, "-no-pdf", "-no-shell-escape",
                "-halt-on-error", "-interaction=nonstopmode",
                f"-output-directory={output}", f"-jobname={NAME}",
                str(HERE / "preview.tex"),
            ],
            [
                converter, "-f", str(ROOT / "fonts/stix2-type1/map/stix2.map"),
                "-E", "-o", str(Path(output) / (NAME + ".pdf")),
                str(Path(output) / (NAME + ".xdv")),
            ],
        ]
        for command in commands:
            result = subprocess.run(
                command, cwd=ROOT, env=env, text=True, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, check=False,
            )
            if result.returncode:
                raise RuntimeError(result.stdout[-12000:])
            for line in result.stdout.splitlines():
                if any(marker in line for marker in ("Missing character", "Overfull", "Underfull")):
                    raise RuntimeError(line)
        source = Path(output) / (NAME + ".pdf")
        with fitz.open(source) as document:
            assert len(document) == 1
            page = document[0]
            size = (page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72)
            assert abs(size[0] - 112) < 0.1 and abs(size[1] - 65) < 0.1, size
            page.get_pixmap(dpi=180, alpha=False).save(HERE / (NAME + ".png"))
            fonts = sorted({font[3] for font in page.get_fonts()})
        shutil.copyfile(source, HERE / (NAME + ".pdf"))
    print(f"Rendered {size[0]:.2f} x {size[1]:.2f} mm; no missing-glyph or box warnings.")
    print("Embedded fonts: " + ", ".join(fonts))


if __name__ == "__main__":
    verify_coordinates()
    render()
