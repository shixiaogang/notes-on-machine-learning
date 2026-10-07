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
OUTLINE = Path("plans/mathematical-preliminaries-reading-structure.md")
CONTRACT = Path("plans/mathematical-preliminaries-chapter-map.md")
RETIRED_LABELS = Path("plans/chapter17-retired-labels.json")
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
    for match in re.finditer(
        r"^\| (\d+) \| (\d+) \| ([^|]+) \| ([^|]+\.tex) \|$",
        (root / CONTRACT).read_text(), re.M,
    ):
        number, locator, title, path = match.groups()
        rows.append({
            "chapter": int(number), "outline_locator": int(locator),
            "title": title.strip(), "path": str(VOLUME / path.strip()),
        })
    if len(rows) != 17:
        raise ValueError(f"Expected 17 assignments, found {len(rows)}")
    return rows


def outline_headings(text: str) -> dict[int, list[dict]]:
    result: dict[int, list[dict]] = {}
    current = None
    for line_no, line in enumerate(text.splitlines(), 1):
        chapter = re.match(
            r"## 第(\d+)章 (.+?)(?:（旧细纲定位(\d+)）)?$", line,
        )
        if chapter:
            # Visible chapter numbers follow the current book; subsection
            # locators retain their historical numbering for traceability.
            current = int(chapter[3] or chapter[1])
            result[current] = [{
                "number": str(current), "level": 1,
                "title": chapter[2], "outline_line": line_no,
            }]
            continue
        if line.startswith("## "):
            current = None
        if current is None:
            continue
        match = re.match(r"### (\d+(?:\.\d+)+) (.+)", line)
        if not match:
            match = re.match(r"\s*- \*\*(\d+(?:\.\d+)+) (.+?)\*\*", line)
        if not match:
            match = re.match(r"\s*- (\d+(?:\.\d+)+) ([^：]+)$", line)
        if match and int(match[1].split(".")[0]) == current:
            result[current].append({
                "number": match[1], "level": len(match[1].split(".")),
                "title": match[2], "outline_line": line_no,
            })
    return result


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
        "figures": len(re.findall(r"\\begin\{figure\*?\}", text)),
        "labels": len(LABEL_RE.findall(text)),
    }


def audit_part_guides(root: Path) -> list[dict]:
    reports = []
    for path in sorted((root / VOLUME).glob("*/part.tex")):
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
    """Follow all six volume entries, excluding obsolete unreferenced chapters."""
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

    for entry in sorted((root / "tex").glob("0[1-6]-*/volume.tex")):
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
    report["active_reference_scope"] = "All active body inputs in the six volumes."
    if not issues:
        report["approved_baseline_retirements"] = sorted(set(retired) & eligible)
    return report


def audit_chapter(root: Path, row: dict, expected: list[dict]) -> dict:
    path = root / row["path"]
    report = {**row, "exists": path.exists(), "expected_heading_count": len(expected)}
    if not path.exists():
        report["issues"] = [{"kind": "missing_file"}]
        return report
    raw = path.read_text()
    text = uncomment(raw)
    headings = tex_headings(text)
    issues = []
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
    text = (root / OUTLINE).read_text()
    expected = outline_headings(text)
    rows = assignments(root)
    selected = [row for row in rows if not args.chapter or row["chapter"] in args.chapter]
    reports = [
        audit_chapter(root, row, expected[row["outline_locator"]]) for row in selected
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
    for path in baseline_paths:
        if not path.endswith(".tex"):
            continue
        old = uncomment(subprocess.check_output(
            ["git", "show", f"{baseline_revision}:{path}"], cwd=root, text=True,
        ))
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
        new = uncomment(path.read_text())
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
    chapter17_source = next(row["path"] for row in rows if row["chapter"] == 17)
    retirements = audit_retired_chapter17_labels(
        root, baseline_revision, baseline_labels, chapter17_source,
        all_locations, body_sources,
    )
    chapter17_references = references(body_sources.get(Path(chapter17_source), ""))
    chapter17_reference_audit = {
        "source": chapter17_source, "reference_count": len(chapter17_references),
        "undefined_references": [
            reference for reference in chapter17_references
            if reference["label"] not in all_locations
        ],
        "active_source": Path(chapter17_source) in body_sources,
        "resolution_scope": "All active body inputs in the six volumes.",
    }
    missing = {
        label: path for label, path in missing_before_retirements.items()
        if label not in retirements["approved_baseline_retirements"]
    }
    result = {
        "outline": str(OUTLINE),
        "outline_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "scope": "Mechanical checks only; content and PDF require independent review.",
        "baseline_revision": baseline_revision,
        "chapters": reports, "part_guides": part_guides,
        "baseline_stats": dict(baseline_stats),
        "missing_baseline_labels_before_retirements": missing_before_retirements,
        "chapter17_label_retirements": retirements,
        "chapter17_cross_references": chapter17_reference_audit,
        "missing_baseline_labels": missing, "duplicate_labels": duplicate,
        "duplicate_label_scope": "All active body inputs in the six volumes.",
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
    print(f"CHAPTER17_REFERENCES count={chapter17_reference_audit['reference_count']} "
          f"undefined={len(chapter17_reference_audit['undefined_references'])} "
          f"active={chapter17_reference_audit['active_source']}")
    failed = any(report["issues"] for report in reports)
    failed = failed or bool(retirements["issues"])
    failed = failed or bool(chapter17_reference_audit["undefined_references"])
    failed = failed or not chapter17_reference_audit["active_source"]
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
