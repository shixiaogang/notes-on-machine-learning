from pathlib import Path
import hashlib
import json
import re
import subprocess

OUT = Path(__file__).resolve().parent
OWN = OUT.parents[1]
manifest = json.loads((OUT / 'manifest.json').read_text())
ROOT = Path(manifest['root_read_only'])


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(root, record):
    actual = sha(root / record['path'])
    assert actual == record['sha256'], record['path']
    return {'path': record['path'], 'sha256': actual}


result = {
    'role': 'AI self-check; mechanical integrity checks only',
    'phase': 'r4; source and proofs bound to actual frozen final PDFs',
    'root_head_at_validation': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
    'own_head_at_validation': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=OWN, text=True).strip(),
    'pdfs': [check(ROOT, p) for p in manifest['pdfs']],
    'source_files': [check(ROOT, p) for p in manifest['source_files']],
    'shared_source_files': [check(ROOT, p) for p in manifest['shared_source_files']],
    'figures': [],
}
for p in manifest['source_files']:
    assert sha(OUT / p['snapshot']) == p['sha256']
assert [f['id'] for f in manifest['figures']] == [f'T{i:02d}' for i in range(1, 30)]
color_paths = set()
gray_paths = set()
for f in manifest['figures']:
    item = {'id': f['id'], 'asset': check(ROOT, f['asset']),
            'sources': [check(ROOT, p) for p in f['sources']], 'versions': {}}
    assert f['asset_matches_own_figure_freeze']
    assert all(p['equals_own_committed_source'] for p in f['sources'])
    source = (OUT / 'source-snapshots' / f['chapter']).read_text()
    label_pos = source.index('\\label{' + f['label'] + '}')
    begin_pos = source.rfind('\\begin{figure', 0, label_pos)
    image = re.search(r'\\includegraphics\[([^\]]+)\]\{([^}]+)\}', source[begin_pos:label_pos])
    assert image, f['id']
    assert image.group(1) == f['source_include_options'], f['id'] + ': include options differ'
    assert image.group(2) == f['asset']['path'], f['id'] + ': included asset differs'
    for version, page in f['versions'].items():
        assert sha(OUT / page['proof_png']) == page['proof_sha256']
        color_paths.add(page['proof_png'])
        checked = {'physical_page_1based': page['physical_page_1based'],
                   'printed_page_label': page['printed_page_label'],
                   'proof_png': page['proof_png'], 'proof_sha256': page['proof_sha256']}
        if 'gray_proof_png' in page:
            assert sha(OUT / page['gray_proof_png']) == page['gray_proof_sha256']
            gray_paths.add(page['gray_proof_png'])
            checked.update({'gray_proof_png': page['gray_proof_png'],
                            'gray_proof_sha256': page['gray_proof_sha256']})
        item['versions'][version] = checked
    result['figures'].append(item)
assert len(color_paths) == 56
assert len(gray_paths) == 14
for version in ['vol2-foundations', 'machine-learning-notes']:
    assert len({p for p in color_paths if p.startswith(version + '/')}) == 28
    assert len({p for p in gray_paths if p.startswith(version + '/')}) == 7
result.update({'figure_count': 29, 'unique_color_proofs': 56,
               'unique_gray_proofs': 14, 'integrity_result': 'all hashes, current source includes, source snapshots, and mechanical coverage agree'})
(OUT / 'mechanical-validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({key: result[key] for key in ['phase', 'root_head_at_validation', 'own_head_at_validation', 'figure_count', 'unique_color_proofs', 'unique_gray_proofs', 'integrity_result']}, ensure_ascii=False))
