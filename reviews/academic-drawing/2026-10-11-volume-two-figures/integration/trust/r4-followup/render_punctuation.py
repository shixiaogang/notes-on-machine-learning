from pathlib import Path
import hashlib
import json
import re
import subprocess
import pymupdf as fitz

OWN = Path(__file__).resolve().parents[2]
ROOT = OWN.parent / 'volume-two-figures'
OUT = Path(__file__).resolve().parent / 'pdf-punctuation'
FIG = json.loads((OWN / 'build/final-root-page-review-r4/manifest.json').read_text())
POPPLER = '/Users/robbieshi/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'
CLAUSES = [
    ('R4T01', '常见损坏基准以噪声、模糊和天气等构造可重复压力'),
    ('R4T02', '行为测试将预期转为用例'),
    ('R4T03', '机会均等与反事实标准使用不同标签和因果条件'),
    ('R4T04', '间接提示注入通过检索内容改变系统行为'),
    ('R4T05', '说明书、模型卡和风险框架保存来源、用途、分组结果、限制及责任'),
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


OUT.mkdir(exist_ok=True)
rows = []
for version in ['vol2-foundations', 'machine-learning-notes']:
    pdf = ROOT / 'target' / (version + '.pdf')
    expected = next(p for p in FIG['pdfs'] if p['version'] == version)['sha256']
    assert sha(pdf) == expected
    doc = fitz.open(pdf)
    first = FIG['figures'][0]['versions'][version]['physical_page_1based'] - 6
    last = FIG['figures'][4]['versions'][version]['physical_page_1based']
    rendered = {}
    for id, clause in CLAUSES:
        found = []
        for number in range(max(1, first), last + 1):
            text = doc[number - 1].get_text()
            normalized = re.sub(r'\s+', '', text)
            if clause in normalized:
                found.append((number, text, normalized))
        assert len(found) == 1, (version, id, found)
        number, text, normalized = found[0]
        if number not in rendered:
            d = OUT / version
            d.mkdir(exist_ok=True)
            prefix = d / f'page-{number:04d}'
            subprocess.run([POPPLER, '-f', str(number), '-l', str(number), '-singlefile', '-r', '150', '-png', str(pdf), str(prefix)], check=True, capture_output=True)
            prefix.with_suffix('.txt').write_text(text)
            rendered[number] = {'proof_png': str(prefix.with_suffix('.png').relative_to(OUT)),
                                'proof_sha256': sha(prefix.with_suffix('.png')),
                                'physical_page_1based': number,
                                'printed_page_label': doc[number - 1].get_label()}
        where = normalized.index(clause)
        rows.append({'id': id, 'version': version, 'pdf_sha256': expected, **rendered[number],
                     'location_clause': clause, 'normalized_text_near_clause': normalized[max(0, where-30):where+220]})
    assert sha(pdf) == expected
    doc.close()
(OUT / 'manifest.json').write_text(json.dumps({'role': 'AI self-check; punctuation proof locating only, actual visual verdict recorded separately', 'phase': 'r4', 'records': rows}, ensure_ascii=False, indent=2) + '\n')
for row in rows:
    print(row['id'], row['version'], row['physical_page_1based'], row['printed_page_label'], row['proof_png'])
