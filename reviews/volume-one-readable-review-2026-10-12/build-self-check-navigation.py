"""Build mechanical paragraph/sentence navigation without semantic judgments."""

import argparse
import hashlib
import json
import re
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("chapter")
args = parser.parse_args()

root = Path(__file__).resolve().parent
workspace = root.parents[1]
tracker = json.loads((root / "deliverable-status.json").read_text())
chapter = next(item for item in tracker["chapters"] if item["id"] == args.chapter)
source = workspace / chapter["source"]
source_text = source.read_text()
lines = source_text.splitlines()

blocks = []
current = []
for line_number, line in enumerate(lines, 1):
    if line.strip():
        current.append((line_number, line))
    elif current:
        blocks.append(current)
        current = []
if current:
    blocks.append(current)

paragraphs = []
sentence_number = 0
for paragraph_number, block in enumerate(blocks, 1):
    text = "\n".join(line for _, line in block)
    fragments = []
    for fragment in re.split(r"(?<=[。！？])", text):
        if not fragment.strip():
            continue
        sentence_number += 1
        fragments.append({"id": f"S{sentence_number:04d}", "text": fragment})
    paragraphs.append(
        {
            "id": f"P{paragraph_number:04d}",
            "start": block[0][0],
            "end": block[-1][0],
            "text": text,
            "sentence_fragments": fragments,
        }
    )

result = {
    "source": chapter["source"],
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "paragraph_anchors": len(paragraphs),
    "sentence_anchors": sentence_number,
    "paragraphs": paragraphs,
}
output = root / "repair" / args.chapter / "current-navigation-2026-10-14.json"
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(args.chapter, len(paragraphs), sentence_number, result["source_sha256"])
