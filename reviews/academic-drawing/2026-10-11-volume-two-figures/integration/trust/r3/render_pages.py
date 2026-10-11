from pathlib import Path
import hashlib
import json
import re
import subprocess
import pymupdf as fitz

OWN = Path(__file__).resolve().parents[2]
ROOT = OWN.parent / 'volume-two-figures'
OUT = Path(__file__).resolve().parent
FREEZE = OWN / 'reviews/academic-drawing/2026-10-11-volume-two-figures/trust/figure-freeze.json'
POPPLER = Path('/Users/robbieshi/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm')
GRAY_IDS = {'T04', 'T09', 'T13', 'T16', 'T18', 'T23', 'T27'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entry(path):
    return {'path': str(path.relative_to(ROOT)), 'sha256': sha(path), 'bytes': path.stat().st_size}


def matching_close(text, left):
    depth = 0
    for i in range(left, len(text)):
        if text[i] in '{}':
            # TeX control-symbol braces are not grouping tokens.
            n = 0
            j = i - 1
            while j >= 0 and text[j] == '\\':
                n += 1
                j -= 1
            if n % 2:
                continue
            depth += 1 if text[i] == '{' else -1
            if depth == 0:
                return i
    raise ValueError('unclosed brace')


def source_caption(text, label):
    label_pos = text.index('\\label{' + label + '}')
    start = text.rfind('\\begin{figure', 0, label_pos)
    cap = text.rfind('\\caption', start, label_pos)
    brace = text.index('{', cap)
    end = matching_close(text, brace)
    fig_end = text.index('\\end{figure', label_pos)
    contexts = []
    for match in re.finditer(r'\\(?:ref|hyperref)\{?' + re.escape(label), text):
        a = max(0, text.rfind('\n\n', 0, match.start()))
        z = text.find('\n\n', match.end())
        contexts.append(text[a:z if z >= 0 else len(text)].strip())
    return text[brace + 1:end], text[start:fig_end + 25], contexts


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    frozen = json.loads(FREEZE.read_text())
    figures = frozen['figures']
    manifest = {'role': 'AI self-check; author participated in drawing',
                'root_read_only': str(ROOT), 'proof_output': str(OUT),
                'rendering': {'tool': str(POPPLER), 'dpi': 150, 'full_page': True},
                'figures': [], 'pdfs': [], 'source_files': []}
    chapter_text = {}
    source_out = OUT / 'source-snapshots'
    source_out.mkdir(exist_ok=True)
    for source in frozen['sources']:
        p = ROOT / source['path']
        chapter_text[p.name] = p.read_text()
        dst = source_out / p.name
        dst.write_bytes(p.read_bytes())
        manifest['source_files'].append(entry(p) | {'snapshot': str(dst.relative_to(OUT))})
    common = [
        'figures/02-foundations/00-shared/academic-drawing/preamble.tex',
        'figures/02-foundations/00-shared/academic-drawing/palette.tex',
        'figures/02-foundations/00-shared/academic-drawing/plot_style.py',
        'figures/02-foundations/00-shared/generated/replay_labels.py',
        'figures/02-foundations/00-shared/generated/typeset_common.py',
        'figures/02-foundations/00-shared/matplotlib/redraw/charts.py',
        'figures/02-foundations/00-shared/matplotlib/redraw/quantitative-redraw-functions.py',
    ]
    manifest['shared_source_files'] = [entry(ROOT / p) for p in common if (ROOT / p).exists()]
    for f in figures:
        asset = ROOT / f['asset']
        src = []
        if 'source' in f:
            src.append(ROOT / f['source'])
        else:
            for key in ['label_metadata', 'data_metadata', 'font_proof']:
                if key in f:
                    src.append(ROOT / f[key])
            if '/generated/' in f['asset']:
                config = asset.parent / 'typesetting-20261011.json'
                src.extend([config, asset.parent / 'text-layer.png'])
                bg = json.loads(config.read_text())['background']
                src.append(asset.parent / bg)
        src_records = []
        for p in dict.fromkeys(src):
            src_records.append(entry(p) | {'equals_own_committed_source': sha(p) == sha(OWN / p.relative_to(ROOT))})
        caption, block, contexts = source_caption(chapter_text[f['chapter']], f['label'])
        manifest['figures'].append({
            'id': f['id'], 'label': f['label'], 'chapter': f['chapter'],
            'asset': entry(asset), 'asset_matches_own_figure_freeze': sha(asset) == f['asset_sha256'],
            'sources': src_records, 'source_include_options': f['include_options'],
            'physical_width_mm': f['physical_width_mm'], 'caption_tex': caption,
            'figure_block_tex': block, 'body_reference_contexts': contexts, 'versions': {}})
    for name, aux in [('vol2-foundations', '02-foundations.aux'), ('machine-learning-notes', 'main.aux')]:
        pdf = ROOT / 'target' / (name + '.pdf')
        document = fitz.open(pdf)
        destinations = document.resolve_names()
        aux_text = (ROOT / 'build' / aux).read_text()
        aux_copy = OUT / (name + '-figure-labels.aux')
        aux_copy.write_bytes((ROOT / 'build' / aux).read_bytes())
        d = OUT / name
        d.mkdir(exist_ok=True)
        pdf_entry = entry(pdf) | {'pages': len(document), 'version': name, 'aux_snapshot': str(aux_copy.relative_to(OUT))}
        manifest['pdfs'].append(pdf_entry)
        rendered = {}
        for f in manifest['figures']:
            match = re.search(r'\\newlabel\{' + re.escape(f['label']) + r'\}\{\{([^{}]+)\}\{([^{}]+)\}', aux_text)
            assert match, f['label']
            num, logical = match.groups()
            target = destinations['figure.' + num]
            physical = target['page'] + 1
            assert document[physical-1].get_label() == logical
            if physical not in rendered:
                prefix = d / f'page-{physical:04d}'
                subprocess.run([str(POPPLER), '-f', str(physical), '-l', str(physical), '-singlefile', '-r', '150', '-png', str(pdf), str(prefix)], check=True, capture_output=True)
                png = prefix.with_suffix('.png')
                text = d / f'page-{physical:04d}.txt'
                text.write_text(document[physical-1].get_text())
                rendered[physical] = {'physical_page_1based': physical, 'printed_page_label': logical,
                                      'proof_png': str(png.relative_to(OUT)), 'proof_sha256': sha(png),
                                      'page_text': str(text.relative_to(OUT))}
            f['versions'][name] = rendered[physical] | {'figure_number': num, 'destination': target}
            if f['id'] in GRAY_IDS:
                prefix = d / f'gray-page-{physical:04d}'
                subprocess.run([str(POPPLER), '-f', str(physical), '-l', str(physical), '-singlefile', '-r', '150', '-gray', '-png', str(pdf), str(prefix)], check=True, capture_output=True)
                png = prefix.with_suffix('.png')
                f['versions'][name]['gray_proof_png'] = str(png.relative_to(OUT))
                f['versions'][name]['gray_proof_sha256'] = sha(png)
        pdf_entry['unique_figure_pages_rendered'] = len(rendered)
        assert sha(pdf) == pdf_entry['sha256'], 'root PDF changed during read-only rendering'
        document.close()
    assert len(manifest['figures']) == 29
    assert all(f['asset_matches_own_figure_freeze'] for f in manifest['figures'])
    assert all(s['equals_own_committed_source'] for f in manifest['figures'] for s in f['sources'])
    (OUT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    for f in manifest['figures']:
        print(f['id'], f['label'], {k: (v['physical_page_1based'], v['printed_page_label'], v['figure_number']) for k, v in f['versions'].items()})
    print('PDFs', json.dumps(manifest['pdfs'], ensure_ascii=False))


if __name__ == '__main__':
    main()
