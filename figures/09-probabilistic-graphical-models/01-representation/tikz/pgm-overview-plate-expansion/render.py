"""Render this figure with the repository typography and export names."""
from pathlib import Path
import sys
import shutil

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "build.sh").is_file())
sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))
from render_tikz import render

if __name__ == "__main__":
    render(HERE / "source.tex", HERE)
    for extension in ("pdf", "png", "svg"):
        shutil.move(HERE / ("source." + extension), HERE / ("figure." + extension))
