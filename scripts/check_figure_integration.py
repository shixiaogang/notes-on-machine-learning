#!/usr/bin/env python3
"""Check the archived, labelled replacements actually used by the book."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'figures/00-shared/academic-drawing/integration-manifest.json'


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
        blocks = re.findall(r'\\begin\{(figure\*?)\}(.*?)\\end\{\1\}', text, re.S)
        matches = [block for _, block in blocks if '\\label{' + label + '}' in block]
        if len(matches) != 1:
            errors.append(f'Expected one figure block: {label}')
        elif asset not in matches[0]:
            errors.append(f'Figure does not use archived asset: {label}')
        elif matches[0].count('\\begingroup') != matches[0].count('\\endgroup'):
            errors.append(f'Unbalanced figure group: {label}')
        elif '\\caption' not in matches[0]:
            errors.append(f'Missing caption: {label}')
        if graphic.suffix not in {'.pdf', '.png'}:
            errors.append(f'Unexpected production format: {asset}')
        digest = hashlib.sha256(graphic.read_bytes()).hexdigest()
        if item.get('sha256') != digest:
            errors.append(f'Changed asset since registry: {asset}')
        if item.get('is_addition') and not re.search(r'\\(?:ref|autoref|cref)\{' + re.escape(label) + r'\}', text):
            errors.append(f'Addition has no introduction reference: {label}')
        group = str(item['volume'])
        counts.setdefault(group, {'replacement': 0, 'addition': 0})
        counts[group]['addition' if item.get('is_addition') else 'replacement'] += 1
    expected = {'1': {'replacement': 111, 'addition': 5},
                '2': {'replacement': 83, 'addition': 7},
                '3': {'replacement': 216, 'addition': 8}}
    if counts != expected:
        errors.append(f'Integration counts differ: {counts}')
    # The original inventory was exhaustive: all first-three-volume figures
    # must have an entry, including the newly added diagrams.
    active = set()
    for slug in ['01-mathematical-preliminaries', '02-foundations', '03-models']:
        for path in (ROOT / 'tex' / slug).rglob('*.tex'):
            for _, block in re.findall(r'\\begin\{(figure\*?)\}(.*?)\\end\{\1\}', path.read_text(), re.S):
                block_labels = re.findall(r'\\label\{(fig:[^}]+)\}', block)
                if block_labels:
                    active.add(block_labels[0])
    if active != labels:
        errors.append(f'Body/registry mismatch: missing={sorted(active-labels)}, unused={sorted(labels-active)}')
    return {'figures': len(records), 'counts': counts, 'errors': errors,
            'checks': ['unique labels', 'caption and body asset', 'asset SHA-256',
                       'complete three-volume coverage', 'addition references']}


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
