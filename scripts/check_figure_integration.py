#!/usr/bin/env python3
"""Check the archived, labelled replacements actually used by the book."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'figures/00-shared/academic-drawing/integration-manifest.json'


def figure_blocks(text):
    """Include the numbered non-floating figures used in function spaces."""
    result = []
    for env, block in re.findall(r'\\begin\{(figure\*?)\}(.*?)\\end\{\1\}', text, re.S):
        labels = re.findall(r'\\label\{(fig:[^}]+)\}', block)
        result.append((env, block, labels))
    for block in re.findall(r'\\begin\{minipage\}.*?\\end\{minipage\}', text, re.S):
        labels = re.findall(r'\\functionalinlinefigurecaption\{(fig:[^}]+)\}', block)
        if labels:
            result.append(('inline', block, labels))
    return result


def check(registry):
    records = registry['records']
    labels = set()
    errors = []
    counts = {}
    for item in records:
        label, owner, asset = item['label'], item['owner'], item['asset']
        if label in labels:
            errors.append(f'Duplicate registry label: {label}')
        labels.add(label)
        source = ROOT / owner
        graphic = ROOT / asset
        if not source.is_file() or not graphic.is_file():
            errors.append(f'Missing body or graphic: {label}')
            continue
        text = source.read_text()
        blocks = figure_blocks(text)
        matches = [(env, block) for env, block, labels in blocks if label in labels]
        if len(matches) != 1:
            errors.append(f'Expected one figure block: {label}')
        elif asset not in matches[0][1]:
            errors.append(f'Figure does not use archived asset: {label}')
        elif matches[0][1].count('\\begingroup') != matches[0][1].count('\\endgroup'):
            errors.append(f'Unbalanced figure group: {label}')
        elif not any(cmd in matches[0][1] for cmd in ['\\caption', '\\functionalinlinefigurecaption']):
            errors.append(f'Missing caption: {label}')
        # A legacy inline TikZ source is itself executed by the book. Redrawn
        # standalone exports use PDF, with the source kept separately.
        inline_source = graphic.suffix == '.tex' and len(matches) == 1 and matches[0][0] == 'inline'
        if graphic.suffix not in {'.pdf', '.png'} and not inline_source:
            errors.append(f'Unexpected production format: {asset}')
        digest = hashlib.sha256(graphic.read_bytes()).hexdigest()
        if item.get('sha256') != digest:
            errors.append(f'Changed asset since registry: {asset}')
        if item.get('current_body_sha256') and item['current_body_sha256'] != hashlib.sha256(source.read_bytes()).hexdigest():
            errors.append(f'Changed body since current review binding: {owner}')
        for path, expected_digest in item.get('current_source_sha256', {}).items():
            dependency = ROOT / path
            if not dependency.is_file() or hashlib.sha256(dependency.read_bytes()).hexdigest() != expected_digest:
                errors.append(f'Changed source since current review binding: {path}')
        if item.get('is_addition') and not re.search(r'\\(?:ref|autoref|cref)\{' + re.escape(label) + r'\}', text):
            errors.append(f'Addition has no introduction reference: {label}')
        group = str(item['volume'])
        counts.setdefault(group, {'replacement': 0, 'addition': 0})
        counts[group]['addition' if item.get('is_addition') else 'replacement'] += 1
    expected = registry.get('expected_counts', {'1': {'replacement': 116, 'addition': 5},
                '2': {'replacement': 83, 'addition': 7},
                '3': {'replacement': 211, 'addition': 8}})
    if counts != expected:
        errors.append(f'Integration counts differ: {counts}')
    # Cover both ordinary floating figures and explicitly numbered inline
    # figures; the latter must not disappear from the inventory.
    active = set()
    for slug in ['01-mathematical-preliminaries', '02-foundations', '03-models']:
        for path in (ROOT / 'tex' / slug).rglob('*.tex'):
            for _, _, block_labels in figure_blocks(path.read_text()):
                if block_labels:
                    active.add(block_labels[0])
    if active != labels:
        errors.append(f'Body/registry mismatch: missing={sorted(active-labels)}, unused={sorted(labels-active)}')
    return {'figures': len(records), 'counts': counts, 'errors': errors,
            'checks': ['unique labels', 'caption and body asset', 'asset SHA-256',
                       'complete three-volume coverage', 'addition references',
                       'current source and body bindings when recorded']}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    result = check(json.loads(REGISTRY.read_text()))
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(bool(result['errors']))


if __name__ == '__main__':
    main()
