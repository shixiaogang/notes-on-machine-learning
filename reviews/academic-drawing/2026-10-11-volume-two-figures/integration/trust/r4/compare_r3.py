from pathlib import Path
import hashlib
import json
from PIL import Image, ImageChops

OUT = Path(__file__).resolve().parent
OLD = OUT.parent / 'final-root-page-review'
old = json.loads((OLD / 'manifest.json').read_text())
new = json.loads((OUT / 'manifest.json').read_text())
old_fig = {f['id']: f for f in old['figures']}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def pixels(path):
    with Image.open(path) as im:
        im = im.convert('RGB')
        return im.copy(), sha(str(im.size).encode() + b'RGB' + im.tobytes())


rows = []
for f in new['figures']:
    previous = old_fig[f['id']]
    assert f['label'] == previous['label']
    assert f['asset']['sha256'] == previous['asset']['sha256']
    for version, proof in f['versions'].items():
        before = previous['versions'][version]
        for mode, key, sha_key in [('color', 'proof_png', 'proof_sha256'),
                                   ('gray', 'gray_proof_png', 'gray_proof_sha256')]:
            if key not in proof:
                continue
            assert key in before
            op, np = OLD / before[key], OUT / proof[key]
            assert sha(op.read_bytes()) == before[sha_key]
            assert sha(np.read_bytes()) == proof[sha_key]
            oi, oh = pixels(op)
            ni, nh = pixels(np)
            equal = oi.size == ni.size and oi.tobytes() == ni.tobytes()
            bbox = None if equal else list(ImageChops.difference(oi, ni).getbbox()) if oi.size == ni.size else 'size differs'
            rows.append({'id': f['id'], 'label': f['label'], 'version': version, 'mode': mode,
                         'old_physical_page_1based': before['physical_page_1based'],
                         'new_physical_page_1based': proof['physical_page_1based'],
                         'old_printed_label': before['printed_page_label'],
                         'new_printed_label': proof['printed_page_label'],
                         'old_proof': before[key], 'new_proof': proof[key],
                         'old_png_sha256': before[sha_key], 'new_png_sha256': proof[sha_key],
                         'old_decoded_pixel_sha256': oh, 'new_decoded_pixel_sha256': nh,
                         'pixel_identical': equal, 'difference_bbox_pixels': bbox})
unique = {(r['version'], r['mode'], r['new_proof']): r for r in rows}
counts = {}
for version in ['vol2-foundations', 'machine-learning-notes']:
    counts[version] = {}
    for mode in ['color', 'gray']:
        pages = [r for r in unique.values() if r['version'] == version and r['mode'] == mode]
        counts[version][mode] = {'unique_pages': len(pages),
                                 'pixel_identical': sum(r['pixel_identical'] for r in pages),
                                 'pixel_changed': sum(not r['pixel_identical'] for r in pages)}
record = {'phase': 'r4 vs frozen r3', 'role': 'AI self-check; mechanical pixel comparison only',
          'method': 'stable figure IDs and labels; full-page 150dpi Poppler PNG decoded as RGB; exact byte equality of dimensions and all pixels',
          'r3_manifest_sha256': sha((OLD / 'manifest.json').read_bytes()),
          'r4_manifest_sha256': sha((OUT / 'manifest.json').read_bytes()),
          'pdfs_r3': old['pdfs'], 'pdfs_r4': new['pdfs'], 'counts': counts, 'per_figure_version_mode': rows}
(OUT / 'pixel-compare.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(counts, ensure_ascii=False))
for r in unique.values():
    if not r['pixel_identical']:
        print('ACTUAL_VIEW_REQUIRED', r['version'], r['mode'], r['new_proof'], 'bbox', r['difference_bbox_pixels'])
