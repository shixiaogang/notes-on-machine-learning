#!/usr/bin/env python3
"""Bind the seven published PDFs to their source tree and staged commit."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PDFS = ['machine-learning-notes.pdf'] + [
    f'vol{i}-{name}.pdf' for i, name in enumerate([
        'mathematical-preliminaries', 'foundations', 'models',
        'paradigms', 'applications', 'systems'], 1)]
MANIFEST = 'target/.build-manifest.json'


def inputs():
    paths = [ROOT / name for name in ['build.sh', '.latexmkrc', 'scripts/check_target_pdfs.py']]
    for directory in ['tex', 'figures', 'fonts']:
        paths.extend(p for p in (ROOT / directory).rglob('*')
                     if p.is_file() and p.name != '.DS_Store' and '__pycache__' not in p.parts)
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(paths)}


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def check_index():
    current = inputs()
    staged = git('ls-files', '-z', '--', 'tex', 'figures', 'fonts', 'build.sh',
                 '.latexmkrc', 'scripts/check_target_pdfs.py').decode().split('\0')
    staged = {p for p in staged if p and Path(p).name != '.DS_Store'
              and '__pycache__' not in Path(p).parts}
    if staged != set(current):
        raise ValueError('正文或构建输入的暂存文件列表与工作目录不同；请先暂存相应新增和删除。')
    for name in current:
        if git('show', ':' + name) != (ROOT / name).read_bytes():
            raise ValueError(f'正文或构建输入存在未暂存修改：{name}')


def pdf_hashes():
    result = {}
    actual = {p.name for p in (ROOT / 'target').glob('*.pdf')}
    if actual != set(PDFS):
        raise ValueError('target/ 的七个 PDF 文件不完整或存在多余文件。')
    for name in PDFS:
        data = (ROOT / 'target' / name).read_bytes()
        if not data.startswith(b'%PDF-') or not data.rstrip().endswith(b'%%EOF'):
            raise ValueError(f'PDF 为空、损坏或尚未构建完成：{name}')
        result[name] = hashlib.sha256(data).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['snapshot', 'record', 'check', 'check-index'])
    parser.add_argument('--snapshot', type=Path)
    parser.add_argument('--staged', action='store_true')
    args = parser.parse_args()
    if args.command == 'snapshot':
        print(json.dumps(inputs(), sort_keys=True))
    elif args.command == 'check-index':
        check_index()
    elif args.command == 'record':
        if not args.snapshot or json.loads(args.snapshot.read_text()) != inputs():
            raise ValueError('构建过程中正文或输入发生变化，请重新运行 ./build.sh all。')
        manifest = {'version': 1, 'inputs': inputs(), 'pdfs': pdf_hashes()}
        temp = ROOT / (MANIFEST + '.tmp')
        temp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + '\n')
        temp.replace(ROOT / MANIFEST)
    else:
        manifest = json.loads((ROOT / MANIFEST).read_text())
        if manifest.get('version') != 1 or manifest.get('inputs') != inputs():
            raise ValueError('target/ PDF 的构建输入已过期；请运行 ./build.sh all。')
        if manifest.get('pdfs') != pdf_hashes():
            raise ValueError('target/ PDF 与构建记录不同；请运行 ./build.sh all。')
        if args.staged:
            check_index()
            for name in [MANIFEST] + ['target/' + n for n in PDFS]:
                if git('show', ':' + name) != (ROOT / name).read_bytes():
                    raise ValueError(f'成品尚未暂存或暂存版本已过期：{name}；请暂存 target/ 后重试。')
        print('成品检查通过：target/ 七个 PDF 与当前正文一致。')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f'成品检查失败：{error}', file=sys.stderr)
        sys.exit(1)
