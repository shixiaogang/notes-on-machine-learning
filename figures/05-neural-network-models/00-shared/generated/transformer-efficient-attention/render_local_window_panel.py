"""Render an independent simple TikZ component for the exact support matrix."""
from pathlib import Path
import json, sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p / "build.sh").exists())
SOURCE = ROOT / "figures/05-neural-network-models/00-shared/generated/transformer-efficient-attention/local-window-panel.tex"

def make_panels(out, fonts):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    assert Path(fonts).resolve() == (ROOT / "fonts").resolve()
    sys.path.insert(0, str(ROOT / "figures/00-shared/academic-drawing"))
    from render_tikz import render
    support = [[int(abs(i-j) <= 1) for j in range(6)] for i in range(6)]
    assert sum(map(sum, support)) == 16
    record = dict(type="exact constructed local-window support, no empirical experiment",
                  tokens=6, radius=1, support=support, valid_pairs=16,
                  input_roles=dict(rows="queries", columns="keys/values"),
                  output_role="one output per query row",
                  source=str(SOURCE.relative_to(ROOT)))
    (out / "local-window-data.json").write_text(json.dumps(record, indent=2))
    render(SOURCE, out)
    return [out / "local-window-panel.png"]

if __name__ == "__main__":
    make_panels(Path(__file__).parent, ROOT / "fonts")
