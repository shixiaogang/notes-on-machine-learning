"""Synchronize mechanical evidence metadata; never generate reading judgments."""
import argparse
import hashlib
import json
import re
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("chapter")
parser.add_argument("status")
parser.add_argument("chapter_through_line", type=int)
args = parser.parse_args()
root = Path(__file__).resolve().parent
workspace = root.parents[1]
tracker_path = root / "deliverable-status.json"
tracker = json.loads(tracker_path.read_text())
chapter = next(c for c in tracker["chapters"] if c["id"] == args.chapter)
records = root / "repair" / args.chapter
source = workspace / chapter["source"]
source_bytes = source.read_bytes()
source_hash = hashlib.sha256(source_bytes).hexdigest()
navigation_path = records / "current-navigation-2026-10-14.json"
navigation = json.loads(navigation_path.read_text())
coverage = {}
for name, prefix, kind, total_key in [
    ("self-check-paragraphs.md", "P", "paragraph", "paragraph_anchors"),
    ("self-check-sentences.md", "S", "sentence", "sentence_anchors"),
]:
    path = records / name
    rows = path.read_text().splitlines() if path.exists() else []
    ids = {
        int(match.group(1))
        for row in rows
        if (match := re.match(r"\|" + prefix + r"(\d{4})", row))
    }
    assert ids == set(range(1, len(ids) + 1)), (name, "noncontiguous IDs")
    assert len(ids) <= navigation[total_key], (name, "too many IDs")
    for row in rows:
        if re.match(r"\|" + prefix + r"\d{4}", row):
            assert len(re.findall(r"(?<!\\)\|", row)) == 3, (name, row)
    coverage[kind + "_anchors_total"] = navigation[total_key]
    coverage[kind + "_anchors_completed"] = len(ids)
manifest_path = records / "snapshot-manifest.json"
manifest = json.loads(manifest_path.read_text())
start_snapshot = records / "self-check-start-2026-10-14.tex"
manifest.update(
    after_sha256=source_hash,
    self_check_start_snapshot=start_snapshot.name,
    status=args.status,
    reading_progress={
        "chapter_through_line": args.chapter_through_line,
        "source_total_lines": len(source_bytes.decode().splitlines()),
        "chapter_read_source_sha256": hashlib.sha256(start_snapshot.read_bytes()).hexdigest(),
    },
    navigation=navigation_path.name,
    navigation_source_sha256=navigation["source_sha256"],
    navigation_coverage=coverage,
)
manifest["record_sha256"] = {
    name: hashlib.sha256((records / name).read_bytes()).hexdigest()
    for name in [
        "self-check-chapter.md", "self-check-paragraphs.md", "self-check-sentences.md",
        "repair-notes.md", "consolidated-findings.json",
    ]
    if (records / name).exists()
}
sentence_view = records / "current-sentence-view-2026-10-14.json"
if sentence_view.exists():
    manifest["sentence_view"] = sentence_view.name
    manifest["record_sha256"][sentence_view.name] = hashlib.sha256(sentence_view.read_bytes()).hexdigest()
(records / "after.tex").write_bytes(source_bytes)
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
chapter.update(
    source_sha256=source_hash,
    self_check_status=args.status,
    self_check_manifest=f"repair/{args.chapter}/snapshot-manifest.json",
)
new_findings_path = records / "self-check-new-findings.json"
if new_findings_path.exists():
    chapter["self_check_new_findings"] = json.loads(new_findings_path.read_text())
tracker_path.write_text(json.dumps(tracker, ensure_ascii=False, indent=2) + "\n")
print(args.chapter, source_hash, coverage, args.status)
