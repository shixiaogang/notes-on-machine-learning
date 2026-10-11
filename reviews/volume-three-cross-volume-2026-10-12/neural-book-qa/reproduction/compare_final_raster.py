"""Read-only final PDF replay. Invoke only with parent's final SHA, after its build ends.

All output is in this child's ignored build. Raster equality transfers previous
actual observations; rendering alone never labels an unseen image as accepted.
"""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys
from PIL import Image, ImageChops

BASE = Path(__file__).resolve().parent
ROOT = Path('/Users/robbieshi/Library/Mobile Documents/com~apple~CloudDocs/writings/Notes/Machine Learning/.worktrees/volume-three-optimization')
OLD_SHA = '285ac31a0291e4462199cc7128871409434e07331abc2c2a07d9045e74488e11'
PDFTOPPM = '/Users/robbieshi/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def save(p, o):
    p.write_text(json.dumps(o, ensure_ascii=False, indent=2) + '\n')

def rgb_digest(im):
    return hashlib.sha256(im.tobytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sha', required=True)
    parser.add_argument('--map', type=Path, required=True)
    parser.add_argument('--pdf', type=Path, default=ROOT/'target/vol3-models.pdf')
    parser.add_argument('--preparation', type=Path, required=True)
    args = parser.parse_args()
    if sha(args.pdf) != args.sha:
        raise RuntimeError('Final PDF SHA mismatch before any rendering')
    old = BASE/OLD_SHA[:16]
    old_manifest = json.loads((old/'00-render-manifest.json').read_text())
    old_coverage = json.loads((old/'08-actual-coverage.json').read_text())
    old_figures = json.loads((old/'01-current-figure-pages.json').read_text())
    if old_manifest['pdf_sha256'] != OLD_SHA or old_coverage['pdf_sha256'] != OLD_SHA:
        raise RuntimeError('Old actual-review identity mismatch')
    subprocess.run([sys.executable, str(BASE/'render_final_pages.py'), '--sha', args.sha,
                    '--pdf', str(args.pdf), '--map', str(args.map),
                    '--preparation', str(args.preparation), '--dpi', '180'], check=True)
    new = BASE/args.sha[:16]
    new_figures = json.loads((new/'01-current-figure-pages.json').read_text())
    old_labels = {f['label']: f for f in old_figures['figures']}
    new_labels = {f['label']: f for f in new_figures['figures']}
    relocations = []
    for label, f in old_labels.items():
        g = new_labels[label]
        if (f['new_pdf_page'], f['current_number']) != (g['new_pdf_page'], g['current_number']):
            relocations.append({'label': label, 'old_page': f['new_pdf_page'],
                                'new_page': g['new_pdf_page'], 'old_number': f['current_number'],
                                'new_number': g['current_number']})
    # Re-render every old contact-covered page plus the Maass supplement, and
    # add the following CNN page to inspect any flow from the two-sentence repair.
    old_pages = sorted(set(old_manifest['rendered_pages']) | {454})
    required = sorted(set(old_pages) | {437, 438})
    details = new/'details-180dpi'
    supplement = []
    for p in required:
        dest = details/f'page-{p:04d}.png'
        if not dest.exists():
            subprocess.run([PDFTOPPM, '-f', str(p), '-l', str(p), '-r', '180',
                            '-png', '-singlefile', str(args.pdf), str(dest.with_suffix(''))], check=True)
            supplement.append(p)
    comparisons = []
    for p in old_pages:
        a = Image.open(old/'details-180dpi'/f'page-{p:04d}.png').convert('RGB')
        b = Image.open(details/f'page-{p:04d}.png').convert('RGB')
        same_size = a.size == b.size
        bbox = None if not same_size else ImageChops.difference(a, b).getbbox()
        equal = same_size and bbox is None
        comparisons.append({'pdf_page': p, 'old_size': list(a.size), 'new_size': list(b.size),
                            'old_rgb_sha256': rgb_digest(a), 'new_rgb_sha256': rgb_digest(b),
                            'rgb_identical': equal, 'difference_bbox_pixels': bbox,
                            'old_actual_detail_review': p in old_coverage['actual_detail_pages'],
                            'observation_transfer': 'pixel-identity-eligible' if equal else 'new-actual-view-required'})
    if sha(args.pdf) != args.sha:
        raise RuntimeError('Final root PDF changed during raster replay')
    save(new/'11-raster-identity-comparison.json', {
        'old_pdf_sha256': OLD_SHA, 'new_pdf_sha256': args.sha,
        'old_actual_coverage': str(old/'08-actual-coverage.json'),
        'comparison_mode': 'actual Poppler180dpi RGB raster, full1530x1980 page pixels',
        'figure_relocations': relocations, 'supplement_newly_rendered_pages': supplement,
        'compared_pages': old_pages, 'actual_comparisons': comparisons,
        'rgb_identical_pages': [c['pdf_page'] for c in comparisons if c['rgb_identical']],
        'changed_pages_require_actual_view': [c['pdf_page'] for c in comparisons if not c['rgb_identical']],
        'additional_required_actual_view': [438],
        'warning': 'Pixel equality is replay of prior actual review, not a new human visual pass. Changed or relocated pages require fresh actual viewing.'})
    print(json.dumps({'new_dir': str(new), 'compared': len(comparisons),
                      'same': sum(c['rgb_identical'] for c in comparisons),
                      'changed': [c['pdf_page'] for c in comparisons if not c['rgb_identical']],
                      'relocations': relocations}, ensure_ascii=False), flush=True)

if __name__ == '__main__':
    main()
