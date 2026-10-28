"""Typeset the three new imagegen figures, without writing frozen assets.

Reuse the exact overlay implementation, adding WenKai for explicit note labels.
Only transparent typography is composited; model artwork remains untouched.
"""
from pathlib import Path
import json
import sys
import render_labels as original

ALLOWED = {"cgan", "cyclegan", "stylegan-overall"}
ORIGINAL_RUNS = original.runs

def render(name):
    if name not in ALLOWED:
        raise ValueError("Only new production figures may be written")
    folder = Path(__file__).resolve().parent / name
    config = json.loads((folder / "labels.json").read_text())
    notes = {line for item in config["labels"] if item.get("role") == "note"
             for line in item["text"].split("\n")}
    def typography_runs(text):
        return [("note" if role == "cn" and text in notes else role, value)
                for role, value in ORIGINAL_RUNS(text)]
    original.runs = typography_runs
    original.render(name)
    fonts = json.loads((folder / "font-provenance.json").read_text())
    for item in fonts:
        if item["role"] == "note":
            item["used"] = bool(notes)
    (folder / "font-provenance.json").write_text(
        json.dumps(fonts, ensure_ascii=False, indent=2) + "\n")
    check = json.loads((folder / "typography-check.json").read_text())
    check["note_labels_using_wenkai"] = sorted(notes)
    check["typesetter"] = str(Path(__file__).resolve().relative_to(original.ROOT))
    (folder / "typography-check.json").write_text(
        json.dumps(check, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    for name in sys.argv[1:] or ["cgan", "cyclegan", "stylegan-overall"]:
        render(name)
