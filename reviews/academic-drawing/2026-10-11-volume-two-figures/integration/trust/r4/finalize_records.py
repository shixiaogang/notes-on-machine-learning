"""Mechanical page bindings, hash validation, and delivery inventories only."""
from pathlib import Path
import hashlib
import json
from PIL import Image

OUT = Path(__file__).resolve().parent
OWN = OUT.parents[1]
FOLLOW = OWN / 'build/r4-followup'
manifest = json.loads((OUT / 'manifest.json').read_text())
comparison = json.loads((OUT / 'pixel-compare.json').read_text())
ROOT = Path(manifest['root_read_only'])


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


pdfs = {r['version']: r for r in manifest['pdfs']}
for r in pdfs.values():
    assert sha(ROOT / r['path']) == r['sha256']
assert sha(OWN / 'build/final-root-page-review/manifest.json') == comparison['r3_manifest_sha256']
assert sha(OUT / 'manifest.json') == comparison['r4_manifest_sha256']
assert all(r['pixel_identical'] and r['difference_bbox_pixels'] is None for r in comparison['per_figure_version_mode'])


def binding(proof_root, version, page, proof, proof_sha, colorspace):
    path = proof_root / proof
    assert sha(path) == proof_sha
    with Image.open(path) as img:
        if colorspace == 'GRAY':
            assert img.mode in ['L', 'RGB'], (path, img.mode)
            if img.mode == 'RGB':
                red, green, blue = img.split()
                assert red.tobytes() == green.tobytes() == blue.tobytes(), path
        else:
            assert img.mode == 'RGB', (path, img.mode)
        size = list(img.size)
        png_mode = img.mode
    return {
        'edition_pdf': pdfs[version]['path'],
        'edition_pdf_sha256': pdfs[version]['sha256'],
        'physical_page': page,
        'proof': proof,
        'proof_sha256': proof_sha,
        'dpi': 150,
        'colorspace': colorspace,
        'png_encoding_mode': png_mode,
        'pixel_dimensions': size,
        'full_page': True,
    }


bindings = {}
for f in manifest['figures']:
    for version, p in f['versions'].items():
        for mode, prefix in [('RGB', ''), ('GRAY', 'gray_')]:
            if prefix + 'proof_png' not in p:
                continue
            record = binding(OUT, version, p['physical_page_1based'], p[prefix + 'proof_png'], p[prefix + 'proof_sha256'], mode)
            existing = bindings.setdefault(record['proof'], record)
            assert existing == record
assert len(bindings) == 70
assert set(bindings) == {str(p.relative_to(OUT)) for p in OUT.rglob('*.png')}
save(OUT / 'final-page-bindings.json', {
    'phase': 'r4', 'role': 'mechanical bindings only',
    'page_numbering': 'physical_page is 1-based',
    'renderer': manifest['rendering']['tool'],
    'records': [bindings[k] for k in sorted(bindings)],
})

lines = [
    '# r4逐图最终页面绑定（机械索引）', '',
    '页码按最终PDF标签与目的地重新定位。本表只列页码与像素比较结果；科学、排字与裁切判断按review.md声明继承冻结r3实际目检。每页proof、PNG与像素SHA见manifest.json及pixel-compare.json。', '',
    '|稳定图ID / 标签|卷二图号|卷二物理页 / 印刷页|全集图号|全集物理页 / 印刷页|完整页像素比较|',
    '|---|---|---|---|---|---|',
]
for f in manifest['figures']:
    a = f['versions']['vol2-foundations']
    b = f['versions']['machine-learning-notes']
    lines.append(f"|{f['id']} / `{f['label']}`|{a['figure_number']}|{a['physical_page_1based']} / {a['printed_page_label']}|{b['figure_number']}|{b['physical_page_1based']} / {b['printed_page_label']}|两版与r3完全相同|")
lines.extend(['', '## 灰度页索引', '', '|代表图|卷二物理页 / 印刷页|全集物理页 / 印刷页|完整页像素比较|', '|---|---|---|---|'])
for f in manifest['figures']:
    a = f['versions']['vol2-foundations']
    b = f['versions']['machine-learning-notes']
    if 'gray_proof_png' not in a:
        continue
    lines.append(f"|{f['id']}|{a['physical_page_1based']} / {a['printed_page_label']}|{b['physical_page_1based']} / {b['printed_page_label']}|两版与r3完全相同|")
lines.extend(['', 'T16/T17共页；灰度T16页同样包含T17。全部逐图绑定共58个彩色图—版本记录，对应56张唯一完整页；灰度14张唯一完整页。', ''])
(OUT / 'page-binding.md').write_text('\n'.join(lines))

pm = json.loads((FOLLOW / 'pdf-punctuation/manifest.json').read_text())
punct = {}
for r in pm['records']:
    assert r['pdf_sha256'] == pdfs[r['version']]['sha256']
    proof = 'pdf-punctuation/' + r['proof_png']
    record = binding(FOLLOW, r['version'], r['physical_page_1based'], proof, r['proof_sha256'], 'RGB')
    existing = punct.setdefault(proof, record)
    assert existing == record
assert len(pm['records']) == 10 and len(punct) == 8
assert set(punct) == {str(p.relative_to(FOLLOW)) for p in FOLLOW.rglob('*.png')}
save(FOLLOW / 'final-page-bindings.json', {
    'phase': 'r4', 'role': 'mechanical bindings only',
    'page_numbering': 'physical_page is 1-based',
    'renderer': manifest['rendering']['tool'],
    'records': [punct[k] for k in sorted(punct)],
})

closure = json.loads((FOLLOW / 'mechanical-closure.json').read_text())
actual01 = ROOT / 'tex/03-foundations/03-trustworthiness/01-foundations.tex'
assert sha(actual01) == closure['actual_root_sha256'] == closure['candidate_sha256']
assert sha(FOLLOW / '01-foundations-root-applied.tex') == sha(actual01)
assert sha(ROOT / 'tex/styles/references.tex') == closure['macro_sha256']
save(FOLLOW / 'mechanical-pdf-validation.json', {
    'phase': 'r4', 'role': 'AI self-check; mechanical integrity only',
    'source01_sha256': sha(actual01),
    'macro_sha256': closure['macro_sha256'],
    'pdfs': list(pdfs.values()),
    'punctuation_bindings_count': len(pm['records']),
    'unique_punctuation_proofs': len(punct),
    'integrity_result': 'current PDFs, source, macro, and all punctuation proofs match frozen SHA records',
    'manual_visual_record': 'pdf-punctuation/visual-review.md',
    'manual_visual_record_sha256': sha(FOLLOW / 'pdf-punctuation/visual-review.md'),
})
if 'pdf_status' in closure:
    closure['pdf_status_at_source_closure'] = closure.pop('pdf_status')
closure['pdf_followup_record'] = 'pdf-punctuation/visual-review.md'
closure['pdf_followup_integrity'] = 'mechanical-pdf-validation.json'
save(FOLLOW / 'mechanical-closure.json', closure)

for directory in [OUT, FOLLOW]:
    records = []
    for p in sorted(directory.rglob('*')):
        if not p.is_file() or p.name == 'delivery-inventory.json':
            continue
        records.append({'path': str(p.relative_to(directory)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
    inventory = {
        'role': 'mechanical delivery inventory only',
        'directory': str(directory),
        'file_count_excluding_inventory': len(records),
        'bytes_excluding_inventory': sum(r['bytes'] for r in records),
        'records': records,
    }
    save(directory / 'delivery-inventory.json', inventory)
    print(json.dumps({k: inventory[k] for k in ['directory', 'file_count_excluding_inventory', 'bytes_excluding_inventory']}, ensure_ascii=False))
print(json.dumps({'r4_graph_page_bindings': len(bindings), 'r4_punctuation_page_bindings': len(punct), 'pixel_changes': 0, 'punctuation_sha_integrity': True}, ensure_ascii=False))
