#!/usr/bin/env python3
"""Compare the mathematical volume with its approved reading structure.

This checks heading order, hierarchy, label retention, and source structure.
It does not certify mathematical correctness or the quality of explanations.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
VOLUME = Path("tex/01-mathematical-preliminaries")
CURRENT_VOLUMES = (
    Path("tex/01-basic-mathematics"),
    Path("tex/02-abstract-mathematics"),
    Path("tex/03-optimization-evolution-and-signals"),
    Path("tex/04-manifolds-distributions-and-inference"),
    Path("tex/05-control-decision-and-games"),
)
OUTLINE_DIRECTORIES = tuple(Path("plans") / volume.name for volume in CURRENT_VOLUMES)
MIGRATED_CHAPTER_COUNTS = {1: 25, 2: 3, 3: 9, 4: 4, 5: 3}
CONTRACT = Path("tests/fixtures/math-reading-structure/chapter-map.md")
RETIRED_LABELS = Path("tests/fixtures/math-reading-structure/chapter17-retired-labels.json")
CHAPTER17_DELETION = Path("tests/fixtures/math-reading-structure/chapter17-deletion.json")
CHAPTER17_DELETION_REVISION = "5dbfb0e3"
CHAPTER17_DELETION_SOURCE = "tex/02-mathematical-preliminaries-lower/03-mathematics-and-machine-learning/01-mathematics-and-future-research.tex"
CHAPTER1_RETIRED_LABELS = Path("tests/fixtures/math-reading-structure/chapter1-retired-labels.json")
CHAPTER1_BASELINE_REVISION = "f435c9df3d52f2aee75b22e40ed6fc33fd0eca15"
CHAPTER1_PRE_REWRITE_REVISION = "870ef690a9f1cd74a98510b05cc033529986fa4e"
CHAPTER1_BASELINE_SOURCE = Path(
    "01-mathematical-language-combinatorics-analysis-optimization/01-sets-functions-and-proofs.tex"
)
CHAPTER1_PRE_REWRITE_SOURCE = Path("tex/01-mathematical-preliminaries-upper") / CHAPTER1_BASELINE_SOURCE
CHAPTER1_CURRENT_SOURCE = CURRENT_VOLUMES[0] / "01-sets/01-sets-relations-and-maps.tex"
# The authorized topic was section 1.4 in the baseline and 1.5 before removal.
# Bind its real title in each immutable source instead of reusing a section number.
CHAPTER1_REMOVED_SECTION_TITLES = ("命题与证明",)
CHAPTER2_RETIRED_LABELS = Path("tests/fixtures/math-reading-structure/chapter2-retired-labels.json")
CHAPTER2_BASELINE_REVISION = "f435c9df3d52f2aee75b22e40ed6fc33fd0eca15"
CHAPTER2_PRE_REWRITE_REVISION = "870ef690a9f1cd74a98510b05cc033529986fa4e"
CHAPTER2_BASELINE_SOURCE = Path(
    "01-mathematical-language-combinatorics-analysis-optimization/02-combinatorics.tex"
)
CHAPTER2_PRE_REWRITE_SOURCE = Path("tex/01-mathematical-preliminaries-upper") / CHAPTER2_BASELINE_SOURCE
CHAPTER2_CURRENT_SOURCE = CURRENT_VOLUMES[0] / "01-sets/02-counting.tex"
CHAPTER2_BASELINE_SECTION_TITLES = (
    "候选空间上的约束与求解", "问题族的可计算性与复杂度",
)
CHAPTER2_PRE_REWRITE_SECTION_TITLES = (
    "候选解的构造", "候选解的质量核验", "问题族的可计算性", "问题族的计算复杂度",
)
# This summary table recapped the removed solving/computability material.
# The summary's semantic label and all its other labels remain protected.
CHAPTER2_SUMMARY_RETIREMENT = "tab:prelim-four-solution-questions"
CHAPTER2_FORMULA_RETIREMENT = "eq:prelim-binomial-theorem"
CHAPTER2_PATTERN_RELOCATION_TITLE = "有限输入上的可区分模式"
CHAPTER2_PATTERN_DESTINATION = "tex/06-foundations/02-learning-theory/statistical-learning-framework/01-finite-input-patterns.tex"
CHAPTER17_BASELINE_SOURCE = Path(
    "05-dynamical-systems-control-and-decision/06-mathematics-and-future-research.tex"
)
BASELINE = "f435c9d"
LEVELS = {
    "chapter": 1,
    "section": 2,
    "subsection": 3,
    "subsubsection": 4,
    "paragraph": 5,
    "subparagraph": 6,
}
LABEL_RE = re.compile(
    r"\\(?:label|functionalinline(?:figure|table)caption)\{([^{}#]+)\}"
)


def uncomment(text: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def group(text: str, start: int) -> tuple[str, int]:
    """Read a balanced brace group without interpreting its TeX contents."""
    if start >= len(text) or text[start] != "{":
        raise ValueError(f"Expected a brace group at character {start}")
    depth = 1
    pos = start + 1
    while pos < len(text):
        if text[pos] == "\\":
            pos += 2
            continue
        if text[pos] == "{":
            depth += 1
        elif text[pos] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:pos], pos + 1
        pos += 1
    raise ValueError(f"Unclosed brace group at character {start}")


def normalize(title: str) -> str:
    title = title.replace("--", "–").replace("—", "–")
    title = re.sub(r"\\(?:textbf|emph|texorpdfstring)\{([^{}]*)\}", r"\1", title)
    return re.sub(r"\s+", "", title)


def assignments(root: Path) -> list[dict]:
    rows = []
    modern = list(re.finditer(
        r"^\| (\d+) \| ([1-5]) \| (\d+) \| ([^|]+) \| ([^|]+\.tex) \|$",
        (root / CONTRACT).read_text(), re.M,
    ))
    for match in modern:
        number, volume, local, title, path = match.groups()
        rows.append({"chapter": int(number), "volume": int(volume), "local_chapter": int(local),
                     "title": title.strip(), "path": path.strip()})
    for match in re.finditer(
        r"^\| (\d+) \| ([^|]+) \| ([^|]+\.tex) \|$",
        (root / CONTRACT).read_text(), re.M,
    ):
        number, title, path = match.groups()
        rows.append({
            "chapter": int(number),
            "title": title.strip(), "path": path.strip() if path.strip().startswith("tex/") else str(VOLUME / path.strip()),
        })
    # Historical audit identities stay stable when current chapters merge.
    # In particular, ID 17 remains the source governed by the retirement file.
    # Independent one-variable and multivariable calculus retain IDs 18 and 21.
    # The five-chapter probability part adds IDs 42 to 45.
    # The six-chapter graph part retires ID 32 (paths merged into ID 9) and adds IDs 46 and 47.
    migrated = bool(modern and any(row["volume"] > 2 for row in rows if "volume" in row))
    expected_identities = ([n for n in range(1, 48) if n not in {17, 32, 37}] if migrated else list(range(1, 36))) if modern else list(range(1, 18))
    count = len(expected_identities)
    if modern and len(modern) != len(rows):
        raise ValueError("Chapter assignments must not mix current and legacy formats")
    if len(rows) != count:
        raise ValueError(f"Expected {count} assignments, found {len(rows)}")
    identities = [row["chapter"] for row in rows]
    if (sorted(identities) if modern else identities) != expected_identities:
        raise ValueError("Chapter assignments must use current numbers and historical identities exactly once")
    if len({row["path"] for row in rows}) != count:
        raise ValueError("Chapter assignments must have unique source paths")
    if modern:
        counts = MIGRATED_CHAPTER_COUNTS if migrated else {1: 25, 2: 10}
        offset = 0
        for volume, expected_count in counts.items():
            local_numbers = [row["local_chapter"] for row in rows if row["volume"] == volume]
            if local_numbers != list(range(1, expected_count + 1)):
                raise ValueError(f"Volume {volume} assignments must list local chapters 1 through {expected_count} in reading order")
            for row in rows:
                if row["volume"] == volume:
                    row["outline_offset"] = offset
            offset += expected_count
    return rows


def current_outline_chapter(row: dict) -> int:
    """Map stable audit identities to the current concatenated outline."""
    if "local_chapter" not in row:
        return row["chapter"]
    return row["local_chapter"] + row.get("outline_offset", 25 if row["volume"] == 2 else 0)


def chapter17_retirement_source(rows: list[dict]) -> str:
    """Bind the historical retirement contract to its source and stable ID."""
    candidates = [
        row for row in rows
        if Path(row["path"]).name.endswith("mathematics-and-future-research.tex")
    ]
    if len(candidates) != 1 or candidates[0]["chapter"] != 17:
        raise ValueError(
            "Historical chapter 17 must identify the mathematics-and-future-research source"
        )
    return candidates[0]["path"]


def outline_headings(text: str) -> dict[int, list[dict]]:
    result: dict[int, list[dict]] = {}
    offset = 0
    current = None
    for line_no, line in enumerate(text.splitlines(), 1):
        marker = re.fullmatch(r"<!-- audit-volume-offset: (\d+) -->", line)
        if marker:
            offset = int(marker[1])
        elif line.startswith("## 卷二"):
            offset = 25
        chapter = re.match(r"## 第(\d+)章 (.+)$", line)
        if chapter:
            current = int(chapter[1]) + offset
            result[current] = [{
                "number": str(current), "level": 1,
                "title": chapter[2], "outline_line": line_no,
            }]
            continue
        if line.startswith("## "):
            current = None
        if current is None:
            continue
        paragraph = re.match(r"(#{3,7}) (?:段|paragraph)[：:](.+)$", line)
        if paragraph:
            result[current].append({
                "number": f"{current}.paragraph-{line_no}",
                "level": len(paragraph[1]) - 1,
                "title": paragraph[2], "outline_line": line_no,
            })
            continue
        match = re.match(r"#{3,7} (\d+(?:\.\d+)+) (.+)", line)
        if not match:
            match = re.match(r"\s*- \*\*(\d+(?:\.\d+)+) (.+?)\*\*", line)
        if not match:
            match = re.match(r"\s*- (\d+(?:\.\d+)+) ([^：]+)$", line)
        if match and int(match[1].split(".")[0]) + offset == current:
            result[current].append({
                "number": match[1], "level": len(match[1].split(".")),
                "title": match[2], "outline_line": line_no,
            })
    return result


def reading_structure(root: Path) -> tuple[list[Path], str]:
    """Read the current mathematics part outlines, retaining historical audit numbers."""
    paths = []
    texts = []
    offset = 0
    for number, directory in enumerate(OUTLINE_DIRECTORIES, 1):
        parts = sorted((root / directory).glob("*.md"))
        if not parts:
            raise ValueError(f"Expected at least one part outline in {directory}")
        texts.append(f"<!-- audit-volume-offset: {offset} -->")
        offset += MIGRATED_CHAPTER_COUNTS[number]
        for path in parts:
            paths.append(path.relative_to(root))
            texts.append(path.read_text())
    return paths, "\n\n".join(texts)


def tex_headings(text: str) -> list[dict]:
    pattern = r"\\(" + "|".join(LEVELS) + r")(\*)?\s*(?:\[[^\]]*\]\s*)?\{"
    result = []
    for match in re.finditer(pattern, text):
        title, end = group(text, match.end() - 1)
        result.append({
            "level": LEVELS[match[1]], "command": match[1],
            "starred": bool(match[2]), "title": title,
            "line": text.count("\n", 0, match.start()) + 1,
            "start": match.start(), "end": end,
        })
    return result


def source_stats(text: str) -> dict:
    return {
        "characters": len(text),
        "proofs": len(re.findall(r"\\begin\{proof\}", text)),
        "definitions": len(re.findall(r"\\begin\{definition\}", text)),
        "theorems": len(re.findall(r"\\begin\{(?:theorem|lemma)\}", text)),
        "examples": len(re.findall(r"\\begin\{example\}", text)),
        "figures": (len(re.findall(r"\\begin\{figure\*?\}", text))
                    + len(re.findall(r"\\functionalinlinefigurecaption\{fig:", text))),
        "labels": len(LABEL_RE.findall(text)),
    }


def audit_part_guides(root: Path) -> list[dict]:
    reports = []
    for path in sorted(p for volume in CURRENT_VOLUMES for p in (root / volume).glob("*/part.tex")):
        text = uncomment(path.read_text())
        matches = list(re.finditer(r"\\BookPartGuide\s*\{", text))
        issues = []
        guides = []
        for match in matches:
            body, _ = group(text, match.end() - 1)
            guides.append(body)
            if re.search(r"\\(?:part|chapter|section|subsection)\*?\s*\{", body):
                issues.append({"kind": "numbered_or_structural_heading_in_guide"})
            if re.search(r"\\(?:addcontentsline|addtocontents|pdfbookmark)\b", body):
                issues.append({"kind": "guide_added_to_navigation"})
            if re.search(r"推荐|建议阅读顺序|阅读顺序", body):
                issues.append({"kind": "guide_contains_reading_recommendation"})
        if len(guides) != 1:
            issues.append({
                "kind": "part_guide_count",
                "expected": 1,
                "actual": len(guides),
            })
        reports.append({
            "path": str(path.relative_to(root)),
            "guide_count": len(guides),
            "issues": issues,
        })
    return reports


def active_body_sources(root: Path) -> tuple[dict[Path, str], list[str]]:
    """Follow all registered volume entries, excluding obsolete unreferenced chapters."""
    sources: dict[Path, str] = {}
    missing: set[str] = set()

    def walk(path: Path, stack: tuple[Path, ...] = ()) -> None:
        if path in stack:
            raise ValueError(f"Recursive input: {' -> '.join(map(str, (*stack, path)))}")
        if path in sources or str(path) in missing:
            return
        absolute = root / path
        if not absolute.is_file():
            missing.add(str(path))
            return
        text = uncomment(absolute.read_text())
        sources[path] = text
        for match in re.finditer(r"\\input\s*\{([^{}]+)\}", text):
            child = Path(match[1].strip())
            if not child.suffix:
                child = child.with_suffix(".tex")
            walk(child, (*stack, path))

    for entry in sorted((root / "tex").glob("[0-9][0-9]-*/volume.tex")):
        walk(entry.relative_to(root))
    return sources, sorted(missing)


def label_inventory_sha256(labels: list[str]) -> str:
    """Fingerprint the explicitly captured pre-rewrite label inventory."""
    return hashlib.sha256(("\n".join(sorted(labels)) + "\n").encode()).hexdigest()


def references(text: str) -> list[dict]:
    """Find ordinary, range, hyperlink, and project cross-reference targets."""
    result = []
    for match in re.finditer(r"\\([A-Za-z]+)(?:\*)?\s*", text):
        command = match[1]
        lower = command.lower()
        if not (
            lower.endswith(("ref", "refrange"))
            or lower in {"getrefnumber", "getpagerefnumber", "hyperlink"}
        ) or lower == "href":
            continue
        pos = match.end()
        arguments = []
        if lower == "hyperref" and pos < len(text) and text[pos] == "[":
            end = text.find("]", pos + 1)
            if end < 0:
                continue
            arguments.append(text[pos + 1:end])
        else:
            # Reference options are not targets. Project Book*Ref commands
            # have a second, prose fallback argument, which is not a label.
            if pos < len(text) and text[pos] == "[":
                end = text.find("]", pos + 1)
                if end < 0:
                    continue
                pos = end + 1
            for _ in range(2 if lower.endswith("refrange") else 1):
                while pos < len(text) and text[pos].isspace():
                    pos += 1
                if pos >= len(text) or text[pos] != "{":
                    break
                argument, pos = group(text, pos)
                arguments.append(argument)
        for argument in arguments:
            for target in argument.split(","):
                target = target.strip()
                if target and not re.search(r"[{}#\\]", target):
                    result.append({
                        "label": target, "command": command,
                        "line": text.count("\n", 0, match.start()) + 1,
                    })
    return result


def audit_deleted_chapter17(root: Path, baseline_labels: dict, all_locations: dict,
                           body_sources: dict, snapshot: str) -> dict:
    """Verify the explicitly authorized deletion against an immutable source snapshot."""
    report = {"path": str(CHAPTER17_DELETION), "exists": True, "issues": [],
              "retired_labels": [], "approved_baseline_retirements": []}
    issues = report["issues"]
    try:
        manifest = json.loads((root / CHAPTER17_DELETION).read_text())
    except (OSError, json.JSONDecodeError) as error:
        issues.append({"kind": "invalid_chapter_deletion_manifest", "error": str(error)})
        return report
    labels = sorted(set(LABEL_RE.findall(uncomment(snapshot))))
    baseline = sorted(label for label, source in baseline_labels.items()
                      if source == str(CHAPTER17_BASELINE_SOURCE))
    required = {"disposition": "delete-entire-chapter", "chapter": 17,
                "source_revision": CHAPTER17_DELETION_REVISION,
                "source": CHAPTER17_DELETION_SOURCE,
                "source_sha256": hashlib.sha256(snapshot.encode()).hexdigest(),
                "source_labels": labels, "baseline_labels": baseline}
    for key, expected in required.items():
        if manifest.get(key) != expected:
            issues.append({"kind": "chapter_deletion_metadata", "field": key})
    if not manifest.get("authorization"):
        issues.append({"kind": "chapter_deletion_authorization_missing"})
    retired = set(labels) | set(baseline)
    for label in sorted(retired):
        if label in all_locations:
            issues.append({"kind": "deleted_chapter_label_still_defined", "label": label})
    for source, text in body_sources.items():
        for reference in references(text):
            if reference["label"] in retired:
                issues.append({"kind": "deleted_chapter_active_reference", "source": str(source), **reference})
    report["retired_labels"] = sorted(retired)
    if not issues:
        report["approved_baseline_retirements"] = baseline
    return report


def audit_retired_chapter17_labels(
    root: Path, baseline_revision: str, baseline_labels: dict[str, str],
    source_path: str, all_locations: dict, body_sources: dict[Path, str],
) -> dict:
    """Permit only explicit, unreferenced retirements from chapter 17.

    The immutable baseline still protects every other chapter. The captured
    pre-rewrite inventory also detects undeclared removals of newer chapter-17
    labels, while stale exceptions, live references, and malformed manifests
    fail closed rather than disabling preservation checks.
    """
    report = {
        "path": str(RETIRED_LABELS), "exists": (root / RETIRED_LABELS).is_file(),
        "issues": [], "retired_labels": [], "approved_baseline_retirements": [],
    }
    if not report["exists"]:
        return report
    issues = report["issues"]
    try:
        manifest = json.loads((root / RETIRED_LABELS).read_text())
    except (json.JSONDecodeError, OSError) as error:
        issues.append({"kind": "invalid_retirement_manifest", "error": str(error)})
        return report
    if not isinstance(manifest, dict):
        issues.append({"kind": "invalid_retirement_manifest_object"})
        return report
    required = {
        "schema_version": 1, "chapter": 17, "source": source_path,
        "baseline_revision": baseline_revision,
        "baseline_source": str(VOLUME / CHAPTER17_BASELINE_SOURCE),
    }
    for key, value in required.items():
        if manifest.get(key) != value:
            issues.append({
                "kind": "retirement_manifest_metadata", "field": key,
                "expected": value, "actual": manifest.get(key),
            })
    if not isinstance(manifest.get("reason"), str) or not manifest["reason"].strip():
        issues.append({"kind": "retirement_reason_missing"})
    if not re.fullmatch(r"[0-9a-f]{64}", str(manifest.get("pre_rewrite_source_sha256", ""))):
        issues.append({"kind": "pre_rewrite_source_sha256_missing"})
    inventory = manifest.get("pre_rewrite_labels")
    if not isinstance(inventory, list) or any(
        not isinstance(label, str) or not label.strip() for label in inventory
    ):
        issues.append({"kind": "invalid_pre_rewrite_label_inventory"})
        return report
    if len(set(inventory)) != len(inventory):
        issues.append({"kind": "duplicate_pre_rewrite_labels"})
    if manifest.get("pre_rewrite_labels_sha256") != label_inventory_sha256(inventory):
        issues.append({"kind": "pre_rewrite_label_inventory_sha256_mismatch"})
    eligible = {
        label for label, path in baseline_labels.items()
        if path == str(CHAPTER17_BASELINE_SOURCE)
    }
    if not eligible:
        issues.append({"kind": "chapter17_baseline_labels_missing"})
    absent = eligible - set(inventory)
    if absent:
        issues.append({"kind": "baseline_labels_absent_from_inventory", "labels": sorted(absent)})
    foreign = {
        label: baseline_labels[label] for label in inventory
        if label in baseline_labels and label not in eligible
    }
    if foreign:
        issues.append({"kind": "foreign_baseline_labels_in_inventory", "labels": foreign})
    entries = manifest.get("retired_labels")
    if not isinstance(entries, list):
        issues.append({"kind": "invalid_retired_label_entries"})
        return report
    retired = []
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("label"), str):
            issues.append({"kind": "invalid_retired_label_entry", "entry": entry})
            continue
        label = entry["label"]
        retired.append(label)
        if label not in inventory:
            issues.append({"kind": "retired_label_not_in_pre_rewrite_source", "label": label})
        if not isinstance(entry.get("reason"), str) or not entry["reason"].strip():
            issues.append({"kind": "retired_label_reason_missing", "label": label})
        if label in all_locations:
            issues.append({
                "kind": "retired_label_still_defined", "label": label,
                "locations": all_locations[label],
            })
    if len(set(retired)) != len(retired):
        issues.append({"kind": "duplicate_retired_labels"})
    report["retired_labels"] = sorted(set(retired))
    for path, body in body_sources.items():
        for reference in references(body):
            if reference["label"] in retired:
                issues.append({
                    "kind": "retired_label_active_reference", "path": str(path),
                    **reference,
                })
    undeclared = set(inventory) - set(all_locations) - set(retired)
    if undeclared:
        issues.append({"kind": "unrecorded_chapter17_label_removal", "labels": sorted(undeclared)})
    report["pre_rewrite_label_count"] = len(inventory)
    report["active_reference_scope"] = "All active body inputs in the registered volumes."
    if not issues:
        report["approved_baseline_retirements"] = sorted(set(retired) & eligible)
    return report


def section_labels(text: str, titles: tuple[str, ...]) -> set[str]:
    """Locate labels inside specified sections of an immutable source."""
    text = uncomment(text)
    sections = [item for item in tex_headings(text) if item["command"] == "section"]
    result = set()
    for index, section in enumerate(sections):
        if section["title"] in titles:
            end = sections[index + 1]["start"] if index + 1 < len(sections) else len(text)
            result.update(LABEL_RE.findall(text[section["start"]:end]))
    return result


def audit_retired_chapter1_labels(
    root: Path, baseline_revision: str, baseline_labels: dict[str, str],
    source_path: str, all_locations: dict, body_sources: dict[Path, str],
    baseline_source: str, pre_rewrite_source: str,
) -> dict:
    """Retire only explicit labels from the removed propositions/proofs section.

    Both source inventories come from fixed Git objects in main(). A manifest
    cannot widen the eligible topic, hide removals elsewhere in chapter 1, or
    borrow the independent retirement permissions for chapters 2 and 17.
    """
    report = {
        "path": str(CHAPTER1_RETIRED_LABELS),
        "exists": (root / CHAPTER1_RETIRED_LABELS).is_file(),
        "issues": [], "retired_labels": [], "approved_baseline_retirements": [],
    }
    if not report["exists"]:
        return report
    issues = report["issues"]
    try:
        manifest = json.loads((root / CHAPTER1_RETIRED_LABELS).read_text())
    except (json.JSONDecodeError, OSError) as error:
        issues.append({"kind": "invalid_retirement_manifest", "error": str(error)})
        return report
    if not isinstance(manifest, dict):
        issues.append({"kind": "invalid_retirement_manifest_object"})
        return report

    baseline_inventory = set(LABEL_RE.findall(uncomment(baseline_source)))
    inventory = LABEL_RE.findall(uncomment(pre_rewrite_source))
    eligible_baseline = section_labels(baseline_source, CHAPTER1_REMOVED_SECTION_TITLES)
    eligible_baseline &= {
        label for label, path in baseline_labels.items()
        if path == str(CHAPTER1_BASELINE_SOURCE)
    }
    eligible_new = section_labels(pre_rewrite_source, CHAPTER1_REMOVED_SECTION_TITLES)
    required = {
        "schema_version": 1, "chapter": 1, "source": str(CHAPTER1_CURRENT_SOURCE),
        "baseline_revision": CHAPTER1_BASELINE_REVISION,
        "baseline_source": str(VOLUME / CHAPTER1_BASELINE_SOURCE),
        "pre_rewrite_revision": CHAPTER1_PRE_REWRITE_REVISION,
        "pre_rewrite_source": str(CHAPTER1_PRE_REWRITE_SOURCE),
        "authorized_baseline_section_titles": list(CHAPTER1_REMOVED_SECTION_TITLES),
        "authorized_pre_rewrite_section_titles": list(CHAPTER1_REMOVED_SECTION_TITLES),
        "baseline_source_sha256": hashlib.sha256(baseline_source.encode()).hexdigest(),
        "pre_rewrite_source_sha256": hashlib.sha256(pre_rewrite_source.encode()).hexdigest(),
        "baseline_section_labels": sorted(eligible_baseline),
        "pre_rewrite_section_labels": sorted(eligible_new),
        "pre_rewrite_labels": sorted(inventory),
        "pre_rewrite_labels_sha256": label_inventory_sha256(inventory),
    }
    for key, expected in required.items():
        if manifest.get(key) != expected:
            issues.append({
                "kind": "retirement_manifest_metadata", "field": key,
                "expected": expected, "actual": manifest.get(key),
            })
    if baseline_revision != CHAPTER1_BASELINE_REVISION or source_path != str(CHAPTER1_CURRENT_SOURCE):
        issues.append({"kind": "chapter1_retirement_identity_mismatch"})
    if not eligible_baseline or not eligible_new:
        issues.append({"kind": "chapter1_retirement_scope_missing"})
    if not isinstance(manifest.get("reason"), str) or not manifest["reason"].strip():
        issues.append({"kind": "retirement_reason_missing"})

    entries = manifest.get("retired_labels")
    if not isinstance(entries, list):
        issues.append({"kind": "invalid_retired_label_entries"})
        return report
    retired = []
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("label"), str):
            issues.append({"kind": "invalid_retired_label_entry", "entry": entry})
            continue
        label = entry["label"]
        retired.append(label)
        if label not in eligible_baseline | eligible_new:
            issues.append({"kind": "retired_label_outside_chapter1_removal_scope", "label": label})
        if label in baseline_labels and baseline_labels[label] != str(CHAPTER1_BASELINE_SOURCE):
            issues.append({"kind": "foreign_baseline_label_retirement", "label": label})
        expected_versions = [
            name for name, labels in (("baseline", eligible_baseline), ("pre_rewrite", eligible_new))
            if label in labels
        ]
        if entry.get("present_in") != expected_versions:
            issues.append({"kind": "retired_label_source_versions_mismatch", "label": label,
                           "expected": expected_versions, "actual": entry.get("present_in")})
        if not isinstance(entry.get("reason"), str) or not entry["reason"].strip():
            issues.append({"kind": "retired_label_reason_missing", "label": label})
        if label in all_locations:
            issues.append({"kind": "retired_label_still_defined", "label": label,
                           "locations": all_locations[label]})
    if len(set(retired)) != len(retired):
        issues.append({"kind": "duplicate_retired_labels"})
    report["retired_labels"] = sorted(set(retired))
    for path, body in body_sources.items():
        for reference in references(body):
            if reference["label"] in retired:
                issues.append({"kind": "retired_label_active_reference", "path": str(path), **reference})
    undeclared = (baseline_inventory | set(inventory)) - set(all_locations) - set(retired)
    if undeclared:
        issues.append({"kind": "unrecorded_chapter1_label_removal", "labels": sorted(undeclared)})
    report["baseline_section_label_count"] = len(eligible_baseline)
    report["pre_rewrite_section_label_count"] = len(eligible_new)
    report["pre_rewrite_label_count"] = len(inventory)
    report["prior_baseline_only_retirements"] = sorted(set(retired) & (eligible_baseline - eligible_new))
    report["active_reference_scope"] = "All active body inputs in the registered volumes."
    if not issues:
        report["approved_baseline_retirements"] = sorted(set(retired) & eligible_baseline)
    return report


def audit_retired_chapter2_labels(
    root: Path, baseline_revision: str, baseline_labels: dict[str, str],
    source_path: str, all_locations: dict, body_sources: dict[Path, str],
    baseline_source: str, pre_rewrite_source: str,
) -> dict:
    """Retire authorized chapter-2 topics and one explicitly removed formula.

    The older baseline has different section numbers. Topic ranges in that
    source and sections 2.3--2.6 in the pre-rewrite commit determine eligibility;
    neither a manifest inventory nor a mutable build snapshot can widen it.
    The separate formula opt-in accepts only the literal binomial theorem label.
    """
    report = {
        "path": str(CHAPTER2_RETIRED_LABELS),
        "exists": (root / CHAPTER2_RETIRED_LABELS).is_file(),
        "issues": [], "retired_labels": [], "approved_baseline_retirements": [],
    }
    if not report["exists"]:
        return report
    issues = report["issues"]
    try:
        manifest = json.loads((root / CHAPTER2_RETIRED_LABELS).read_text())
    except (json.JSONDecodeError, OSError) as error:
        issues.append({"kind": "invalid_retirement_manifest", "error": str(error)})
        return report
    if not isinstance(manifest, dict):
        issues.append({"kind": "invalid_retirement_manifest_object"})
        return report
    required = {
        "schema_version": 1, "chapter": 2, "source": str(CHAPTER2_CURRENT_SOURCE),
        "baseline_revision": CHAPTER2_BASELINE_REVISION,
        "baseline_source": str(VOLUME / CHAPTER2_BASELINE_SOURCE),
        "pre_rewrite_revision": CHAPTER2_PRE_REWRITE_REVISION,
        "pre_rewrite_source": str(CHAPTER2_PRE_REWRITE_SOURCE),
        "authorized_pre_rewrite_sections": [3, 4, 5, 6],
        "authorized_baseline_section_titles": list(CHAPTER2_BASELINE_SECTION_TITLES),
        "authorized_pre_rewrite_section_titles": list(CHAPTER2_PRE_REWRITE_SECTION_TITLES),
        "authorized_summary_label": CHAPTER2_SUMMARY_RETIREMENT,
        "baseline_source_sha256": hashlib.sha256(baseline_source.encode()).hexdigest(),
        "pre_rewrite_source_sha256": hashlib.sha256(pre_rewrite_source.encode()).hexdigest(),
    }
    for key, expected in required.items():
        if manifest.get(key) != expected:
            issues.append({
                "kind": "retirement_manifest_metadata", "field": key,
                "expected": expected, "actual": manifest.get(key),
            })
    if baseline_revision != CHAPTER2_BASELINE_REVISION or source_path != str(CHAPTER2_CURRENT_SOURCE):
        issues.append({"kind": "chapter2_retirement_identity_mismatch"})
    if not isinstance(manifest.get("reason"), str) or not manifest["reason"].strip():
        issues.append({"kind": "retirement_reason_missing"})

    baseline_inventory = set(LABEL_RE.findall(uncomment(baseline_source)))
    inventory = LABEL_RE.findall(uncomment(pre_rewrite_source))
    if manifest.get("pre_rewrite_labels") != sorted(inventory):
        issues.append({"kind": "pre_rewrite_label_inventory_mismatch"})
    if manifest.get("pre_rewrite_labels_sha256") != label_inventory_sha256(inventory):
        issues.append({"kind": "pre_rewrite_label_inventory_sha256_mismatch"})
    # The user explicitly removed this one formula in the counting lesson.
    # No manifest-supplied label can extend the historical topic ranges.
    formula_labels = manifest.get("authorized_formula_labels", [])
    formula_authorized = formula_labels == [CHAPTER2_FORMULA_RETIREMENT]
    if formula_labels not in ([], [CHAPTER2_FORMULA_RETIREMENT]):
        issues.append({"kind": "invalid_formula_retirement_scope"})
    if formula_authorized and (
        CHAPTER2_FORMULA_RETIREMENT not in baseline_inventory
        or CHAPTER2_FORMULA_RETIREMENT not in inventory
        or baseline_labels.get(CHAPTER2_FORMULA_RETIREMENT) != str(CHAPTER2_BASELINE_SOURCE)
    ):
        issues.append({"kind": "formula_retirement_source_mismatch"})
    eligible_baseline = section_labels(baseline_source, CHAPTER2_BASELINE_SECTION_TITLES)
    eligible_baseline &= {
        label for label, path in baseline_labels.items()
        if path == str(CHAPTER2_BASELINE_SOURCE)
    }
    eligible_new = section_labels(pre_rewrite_source, CHAPTER2_PRE_REWRITE_SECTION_TITLES)
    if CHAPTER2_SUMMARY_RETIREMENT in inventory:
        eligible_new.add(CHAPTER2_SUMMARY_RETIREMENT)
    if formula_authorized:
        eligible_baseline.add(CHAPTER2_FORMULA_RETIREMENT)
        eligible_new.add(CHAPTER2_FORMULA_RETIREMENT)
    if not eligible_baseline or not eligible_new:
        issues.append({"kind": "chapter2_retirement_scope_missing"})
    entries = manifest.get("retired_labels")
    if not isinstance(entries, list):
        issues.append({"kind": "invalid_retired_label_entries"})
        return report
    retired = []
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("label"), str):
            issues.append({"kind": "invalid_retired_label_entry", "entry": entry})
            continue
        label = entry["label"]
        retired.append(label)
        if label not in eligible_baseline | eligible_new:
            issues.append({"kind": "retired_label_outside_chapter2_removal_scope", "label": label})
        if label in baseline_labels and baseline_labels[label] != str(CHAPTER2_BASELINE_SOURCE):
            issues.append({"kind": "foreign_baseline_label_retirement", "label": label})
        if not isinstance(entry.get("reason"), str) or not entry["reason"].strip():
            issues.append({"kind": "retired_label_reason_missing", "label": label})
        if label in all_locations:
            issues.append({"kind": "retired_label_still_defined", "label": label,
                           "locations": all_locations[label]})
    if len(set(retired)) != len(retired):
        issues.append({"kind": "duplicate_retired_labels"})
    report["retired_labels"] = sorted(set(retired))
    for path, body in body_sources.items():
        for reference in references(body):
            if reference["label"] in retired:
                issues.append({"kind": "retired_label_active_reference", "path": str(path), **reference})
    undeclared = (baseline_inventory | set(inventory)) - set(all_locations) - set(retired)
    if undeclared:
        issues.append({"kind": "unrecorded_chapter2_label_removal", "labels": sorted(undeclared)})
    report["pre_rewrite_label_count"] = len(inventory)
    report["active_reference_scope"] = "All active body inputs in the registered volumes."
    # The user moved this exact historical lesson to volume 3. Require live,
    # unique definitions at the declared destination; a deletion cannot pass.
    relocation_entries = manifest.get("relocated_pattern_labels", [])
    relocated = []
    pattern_labels = section_labels(pre_rewrite_source, (CHAPTER2_PATTERN_RELOCATION_TITLE,))
    if not isinstance(relocation_entries, list):
        issues.append({"kind": "invalid_pattern_relocations"})
        relocation_entries = []
    for entry in relocation_entries:
        if not isinstance(entry, dict):
            issues.append({"kind": "invalid_pattern_relocation"})
            continue
        label = entry.get("label")
        if label not in pattern_labels or entry.get("destination") != CHAPTER2_PATTERN_DESTINATION:
            issues.append({"kind": "pattern_relocation_scope", "label": label})
            continue
        found = all_locations.get(label, [])
        if len(found) != 1 or found[0]["path"] != CHAPTER2_PATTERN_DESTINATION:
            issues.append({"kind": "pattern_relocation_definition", "label": label})
        if not isinstance(entry.get("reason"), str) or not entry["reason"].strip():
            issues.append({"kind": "pattern_relocation_reason", "label": label})
        relocated.append(label)
    if len(relocated) != len(set(relocated)):
        issues.append({"kind": "duplicate_pattern_relocations"})
    report["relocated_pattern_labels"] = sorted(set(relocated))
    report["approved_baseline_relocations"] = []
    if not issues:
        report["approved_baseline_retirements"] = sorted(set(retired) & eligible_baseline)
        report["approved_baseline_relocations"] = sorted(set(relocated) & baseline_inventory)
    return report


def expanded_chapter_source(root: Path, path: Path, stack: tuple[Path, ...] = ()) -> str:
    """Read a chapter and its actual inputs in publication order."""
    if path in stack:
        raise ValueError(f"Recursive chapter input: {' -> '.join(map(str, (*stack, path)))}")
    text = (root / path).read_text()

    def expand(match: re.Match) -> str:
        child = Path(match[1].strip())
        if not child.suffix:
            child = child.with_suffix(".tex")
        return expanded_chapter_source(root, child, (*stack, path))

    # Ignore commented-out inputs while preserving source line breaks.
    return re.sub(r"\\input\s*\{([^{}]+)\}", expand, uncomment(text))


def audit_chapter(root: Path, row: dict, expected: list[dict]) -> dict:
    path = root / row["path"]
    report = {**row, "exists": path.exists(), "expected_heading_count": len(expected)}
    if not path.exists():
        report["issues"] = [{"kind": "missing_file"}]
        return report
    raw = expanded_chapter_source(root, Path(row["path"]))
    text = uncomment(raw)
    headings = tex_headings(text)
    issues = []
    if not expected or normalize(row["title"]) != normalize(expected[0]["title"]):
        issues.append({"kind": "chapter_map_title_mismatch"})
    # Extra paragraph labels such as a proof sketch are recorded separately.
    # All outline titles, including the deepest ones, must occur in order.
    expected_titles = {normalize(item["title"]) for item in expected}
    substantive = [
        item for item in headings
        if item["level"] <= 4 or normalize(item["title"]) in expected_titles
    ]
    actual_keys = [(h["level"], normalize(h["title"])) for h in substantive]
    expected_keys = [(h["level"], normalize(h["title"])) for h in expected]
    if actual_keys != expected_keys:
        import difflib
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(
            a=expected_keys, b=actual_keys, autojunk=False
        ).get_opcodes():
            if tag != "equal":
                issues.append({
                    "kind": "heading_" + tag,
                    "expected": expected[i1:i2],
                    "actual": [
                        {k: v for k, v in item.items() if k not in {"start", "end"}}
                        for item in substantive[j1:j2]
                    ],
                })
    sections = [h for h in headings if h["level"] == 2]
    if not sections or sections[-1]["title"] != "本章小结":
        issues.append({"kind": "missing_final_summary"})
    stack = []
    for match in re.finditer(r"\\(begin|end)\{([^{}]+)\}", text):
        command, environment = match.groups()
        if command == "begin":
            if environment in {"figure", "figure*", "table", "table*"} and any(
                parent in {"definition", "theorem", "lemma", "example"}
                for parent in stack
            ):
                issues.append({
                    "kind": "float_inside_math_box",
                    "environment": environment,
                    "parents": list(stack),
                    "line": text.count("\n", 0, match.start()) + 1,
                })
            stack.append(environment)
        elif not stack or stack.pop() != environment:
            issues.append({
                "kind": "environment_mismatch", "environment": environment,
                "line": text.count("\n", 0, match.start()) + 1,
            })
    if stack:
        issues.append({"kind": "unclosed_environments", "environments": stack})
    for match in re.finditer(r"\[待(?:核实来源|补证据|补数据|作者确认)\]", text):
        issues.append({
            "kind": "unresolved_marker",
            "line": text.count("\n", 0, match.start()) + 1,
        })
    report.update(
        sha256=hashlib.sha256(raw.encode()).hexdigest(),
        stats=source_stats(text), actual_heading_count=len(substantive),
        auxiliary_heading_count=len(headings) - len(substantive), issues=issues,
    )
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--baseline", default=BASELINE)
    parser.add_argument("--chapter", type=int, action="append")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    outline_paths, text = reading_structure(root)
    expected = outline_headings(text)
    rows = assignments(root)
    selected = [row for row in rows if not args.chapter or row["chapter"] in args.chapter]
    reports = [
        audit_chapter(root, row, expected[current_outline_chapter(row)]) for row in selected
    ]
    part_guides = audit_part_guides(root)
    # Read immutable Git objects so a clean build directory cannot silently
    # disable the old-label check.
    baseline_revision = subprocess.check_output(
        ["git", "rev-parse", "--verify", f"{args.baseline}^{{commit}}"],
        cwd=root, text=True,
    ).strip()
    baseline_paths = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", baseline_revision, "--", str(VOLUME)],
        cwd=root, text=True,
    ).splitlines()
    baseline_labels = {}
    baseline_stats = Counter()
    chapter1_baseline_source = ""
    chapter2_baseline_source = ""
    for path in baseline_paths:
        if not path.endswith(".tex"):
            continue
        old_source = subprocess.check_output(
            ["git", "show", f"{baseline_revision}:{path}"], cwd=root, text=True,
        )
        old = uncomment(old_source)
        if path == str(VOLUME / CHAPTER1_BASELINE_SOURCE):
            chapter1_baseline_source = old_source
        if path == str(VOLUME / CHAPTER2_BASELINE_SOURCE):
            chapter2_baseline_source = old_source
        baseline_stats.update(source_stats(old))
        for match in LABEL_RE.finditer(old):
            baseline_labels[match[1]] = str(Path(path).relative_to(VOLUME))
    if not baseline_labels:
        raise ValueError(f"No mathematical-volume labels in baseline {baseline_revision}")
    locations = defaultdict(list)
    for row in rows:
        path = root / row["path"]
        if not path.exists():
            continue
        new = uncomment(expanded_chapter_source(root, Path(row["path"])))
        for match in LABEL_RE.finditer(new):
            locations[match[1]].append({
                "path": row["path"], "line": new.count("\n", 0, match.start()) + 1,
            })
    # Part/volume labels are maintained by the integrating agent.
    missing_before_retirements = {
        label: path for label, path in baseline_labels.items()
        if label not in locations and not label.startswith(("part:", "vol:"))
    }
    all_locations = defaultdict(list)
    body_sources, missing_inputs = active_body_sources(root)
    for path, body in body_sources.items():
        for match in LABEL_RE.finditer(body):
            all_locations[match[1]].append({
                "path": str(path), "line": body.count("\n", 0, match.start()) + 1,
            })
    duplicate = {key: value for key, value in all_locations.items() if len(value) > 1}
    chapter17_deleted = not any(row["chapter"] == 17 for row in rows)
    chapter17_source = CHAPTER17_DELETION_SOURCE if chapter17_deleted else chapter17_retirement_source(rows)
    if chapter17_deleted:
        snapshot = subprocess.check_output(
            ["git", "show", f"{CHAPTER17_DELETION_REVISION}:{CHAPTER17_DELETION_SOURCE}"],
            cwd=root, text=True,
        )
        retirements = audit_deleted_chapter17(root, baseline_labels, all_locations, body_sources, snapshot)
    else:
        retirements = audit_retired_chapter17_labels(
            root, baseline_revision, baseline_labels, chapter17_source, all_locations, body_sources,
        )
    chapter1_pre_rewrite_source = subprocess.check_output(
        ["git", "show", f"{CHAPTER1_PRE_REWRITE_REVISION}:{CHAPTER1_PRE_REWRITE_SOURCE}"],
        cwd=root, text=True,
    )
    chapter1_retirements = audit_retired_chapter1_labels(
        root, baseline_revision, baseline_labels,
        next(row["path"] for row in rows if row["chapter"] == 1),
        all_locations, body_sources, chapter1_baseline_source, chapter1_pre_rewrite_source,
    )
    chapter2_pre_rewrite_source = subprocess.check_output(
        ["git", "show", f"{CHAPTER2_PRE_REWRITE_REVISION}:{CHAPTER2_PRE_REWRITE_SOURCE}"],
        cwd=root, text=True,
    )
    chapter2_retirements = audit_retired_chapter2_labels(
        root, baseline_revision, baseline_labels,
        next(row["path"] for row in rows if row["chapter"] == 2),
        all_locations, body_sources, chapter2_baseline_source, chapter2_pre_rewrite_source,
    )
    chapter17_references = references(body_sources.get(Path(chapter17_source), ""))
    chapter17_reference_audit = {
        "source": chapter17_source, "reference_count": len(chapter17_references),
        "undefined_references": [
            reference for reference in chapter17_references
            if reference["label"] not in all_locations
        ],
        "active_source": Path(chapter17_source) in body_sources,
        "expected_active": not chapter17_deleted,
        "resolution_scope": "All active body inputs in the registered volumes.",
    }
    approved_retirements = set(retirements["approved_baseline_retirements"])
    approved_retirements.update(chapter1_retirements["approved_baseline_retirements"])
    approved_retirements.update(chapter2_retirements["approved_baseline_retirements"])
    approved_retirements.update(chapter2_retirements.get("approved_baseline_relocations", []))
    missing = {
        label: path for label, path in missing_before_retirements.items()
        if label not in approved_retirements
    }
    result = {
        "outlines": [str(path) for path in outline_paths],
        "outline_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "scope": "Mechanical checks only; content and PDF require independent review.",
        "baseline_revision": baseline_revision,
        "chapters": reports, "part_guides": part_guides,
        "baseline_stats": dict(baseline_stats),
        "missing_baseline_labels_before_retirements": missing_before_retirements,
        "chapter17_label_retirements": retirements,
        "chapter1_label_retirements": chapter1_retirements,
        "chapter2_label_retirements": chapter2_retirements,
        "chapter17_cross_references": chapter17_reference_audit,
        "missing_baseline_labels": missing, "duplicate_labels": duplicate,
        "duplicate_label_scope": "All active body inputs in the registered volumes.",
        "missing_body_inputs": missing_inputs,
    }
    if args.json:
        destination = args.json if args.json.is_absolute() else root / args.json
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    for report in reports:
        print(
            f"CHAPTER {report['chapter']:02d} exists={report['exists']} "
            f"headings={report.get('actual_heading_count', 0)}/"
            f"{report['expected_heading_count']} issues={len(report['issues'])} "
            f"{report['path']}"
        )
    print(f"LABELS missing={len(missing)} duplicate={len(duplicate)} "
          f"missing_inputs={len(missing_inputs)}")
    if retirements["exists"]:
        print(f"CHAPTER17_RETIREMENTS labels={len(retirements['retired_labels'])} "
              f"issues={len(retirements['issues'])}")
    if chapter1_retirements["exists"]:
        print(f"CHAPTER1_RETIREMENTS labels={len(chapter1_retirements['retired_labels'])} "
              f"issues={len(chapter1_retirements['issues'])}")
    if chapter2_retirements["exists"]:
        print(f"CHAPTER2_RETIREMENTS labels={len(chapter2_retirements['retired_labels'])} "
              f"issues={len(chapter2_retirements['issues'])}")
    print(f"CHAPTER17_REFERENCES count={chapter17_reference_audit['reference_count']} "
          f"undefined={len(chapter17_reference_audit['undefined_references'])} "
          f"active={chapter17_reference_audit['active_source']}")
    failed = any(report["issues"] for report in reports)
    failed = failed or bool(retirements["issues"])
    failed = failed or bool(chapter1_retirements["issues"])
    failed = failed or bool(chapter2_retirements["issues"])
    failed = failed or bool(chapter17_reference_audit["undefined_references"])
    failed = failed or (chapter17_reference_audit["active_source"] != chapter17_reference_audit["expected_active"])
    if not args.chapter:
        print(
            f"PART_GUIDES files={len(part_guides)} "
            f"issues={sum(len(report['issues']) for report in part_guides)}"
        )
        failed = failed or any(report["issues"] for report in part_guides)
        failed = failed or bool(missing or duplicate or missing_inputs)
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
