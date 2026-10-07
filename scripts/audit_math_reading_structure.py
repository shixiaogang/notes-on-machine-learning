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
CONTRACT = Path("docs/math-restructure/authoring-contract.md")
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
        chapter = re.match(r"## 第(\d+)章 (.+)", line)
        if chapter:
            current = int(chapter[1])
            result[current] = [{
                "number": chapter[1], "level": 1,
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
    missing = {
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
    result = {
        "outline": str(OUTLINE),
        "outline_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "scope": "Mechanical checks only; content and PDF require independent review.",
        "baseline_revision": baseline_revision,
        "chapters": reports, "part_guides": part_guides,
        "baseline_stats": dict(baseline_stats),
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
    failed = any(report["issues"] for report in reports)
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
