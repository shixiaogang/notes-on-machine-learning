#!/usr/bin/env python3
"""Check that page-broken headings keep their PDF targets and TOC pages."""

from pathlib import Path
import os
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
HEADINGS = {
    "numbered": ("Numbered moved heading", 6),
    "starred": ("Starred moved heading", 8),
    "subsection": ("Subsection moved heading", 10),
    "subsubsection": ("Subsubsection moved heading", 12),
    "paragraph": ("Run-in moved heading", 13),
}


def check_pdf(output_dir):
    pdf = output_dir / "heading-anchors.pdf"
    env = dict(os.environ, LC_ALL="C")
    info = subprocess.check_output(["pdfinfo", str(pdf)], env=env, text=True)
    assert re.search(r"^Pages:\s+13$", info, re.MULTILINE), info
    targets = subprocess.check_output(["pdfinfo", "-dests", str(pdf)], env=env, text=True)
    destinations = {
        target: int(page)
        for page, target in re.findall(r'^\s*(\d+)\s+\[[^\n]*\]\s+"([^"]+)"$',
                                      targets, re.MULTILINE)
    }
    assert all(destinations[f"page.{p}"] == p for p in range(1, 14)), destinations
    aux = (output_dir / "heading-anchors.aux").read_text()
    labels = {
        key: (int(page), target)
        for key, page, target in re.findall(
            r"\\newlabel\{heading:([^}]+)\}\{\{[^}]*\}\{(\d+)\}"
            r"\{[^}]*\}\{([^}]+)\}",
            aux,
        )
    }
    assert labels.keys() == HEADINGS.keys(), labels
    toc = {
        title: (int(page), target)
        for title, page, target in re.findall(
            r"\\contentsline\s+\{(?:section|subsection|subsubsection|paragraph)\}"
            r"\{(?:\\numberline\s*\{[^}]*\})?([^}]+)\}\{(\d+)\}\{([^}]+)\}",
            aux,
        )
    }
    for key, (title, expected) in HEADINGS.items():
        page, target = labels[key]
        assert page == expected, (title, page, expected)
        actual = destinations[target]
        assert actual == page, f"{title}: target page {actual}, printed page {page}"
        assert toc[title] == (page, target), (title, toc[title], labels[key])
    bookmarks = re.findall(r"\\BOOKMARK\s+\[[^\]]+\]\[[^\]]*\]\{([^}]+)\}",
                           (output_dir / "heading-anchors.out").read_text())
    for key in ("numbered", "starred"):
        assert bookmarks.count(labels[key][1]) == 1, (key, bookmarks)
    assert labels["numbered"][1] != labels["starred"][1], labels


def run(command, env):
    result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)


def main():
    build = ROOT / "build"
    build.mkdir(exist_ok=True)
    env = os.environ.copy()
    for key, prefix in {
        "TEXINPUTS": "./tex//:",
        "TFMFONTS": "./fonts/stix2-type1/tfm//:",
        "ENCFONTS": "./fonts/stix2-type1/enc//:",
        "T1FONTS": "./fonts/stix2-type1/type1//:",
    }.items():
        env[key] = prefix + env.get(key, "")
    with tempfile.TemporaryDirectory(prefix="heading-anchors-", dir=build) as temporary:
        output_dir = Path(temporary)
        for _ in range(3):
            run(
                ["xelatex", "-no-pdf", "-interaction=nonstopmode", "-halt-on-error",
                 f"-output-directory={output_dir}", "-jobname=heading-anchors",
                 "tests/check-heading-anchors.tex"],
                env,
            )
        run(
            ["xdvipdfmx", "-f", "fonts/stix2-type1/map/stix2.map", "-E", "-z", "1",
             "-o", str(output_dir / "heading-anchors.pdf"),
             str(output_dir / "heading-anchors.xdv")],
            env,
        )
        check_pdf(output_dir)
    print("标题锚点回归通过：编号节、星号节、子节和行内标题的页码与 PDF 目标一致。")


if __name__ == "__main__":
    main()
