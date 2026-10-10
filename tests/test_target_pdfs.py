import importlib.util
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    'target_pdfs', Path(__file__).resolve().parents[1] / 'scripts/check_target_pdfs.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TargetPdfTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        for name in ['tex', 'figures', 'fonts', 'target', 'scripts']:
            (self.root / name).mkdir()
        for name in ['build.sh', '.latexmkrc', '.gitattributes', 'scripts/check_target_pdfs.py', 'tex/main.tex']:
            (self.root / name).write_text('initial source')
        for name in MODULE.PDFS:
            (self.root / 'target' / name).write_bytes(b'%PDF-1.7\nfixture\n%%EOF\n')
        self.addCleanup(patch.stopall)
        patch.object(MODULE, 'ROOT', self.root).start()
        self.snapshot = self.root / 'snapshot.json'
        self.snapshot.write_text(json.dumps(MODULE.inputs()))
        self.run_command('record', '--snapshot', str(self.snapshot))

    def run_command(self, *args):
        with patch('sys.argv', ['check_target_pdfs.py', *args]):
            MODULE.main()

    def test_accepts_matching_pdfs_and_sources(self):
        self.run_command('check')

    def test_rejects_source_change_even_with_unchanged_timestamp(self):
        source = self.root / 'tex/main.tex'
        previous = source.stat()
        source.write_text('revised source')
        os.utime(source, ns=(previous.st_atime_ns, previous.st_mtime_ns))
        with self.assertRaisesRegex(ValueError, '输入已过期'):
            self.run_command('check')

    def test_rejects_pdf_changed_after_build(self):
        (self.root / 'target' / MODULE.PDFS[0]).write_bytes(b'%PDF-1.7\nchanged\n%%EOF\n')
        with self.assertRaisesRegex(ValueError, '构建记录不同'):
            self.run_command('check')

    def test_rejects_missing_volume(self):
        (self.root / 'target' / MODULE.PDFS[-1]).unlink()
        with self.assertRaisesRegex(ValueError, '不完整'):
            self.run_command('check')

    def test_rejects_source_change_during_build(self):
        (self.root / 'tex/main.tex').write_text('changed during build')
        with self.assertRaisesRegex(ValueError, '构建过程中'):
            self.run_command('record', '--snapshot', str(self.snapshot))

    def test_rejects_staged_pdf_different_from_worktree(self):
        def staged(*args):
            if args[0] == 'ls-files':
                return '\0'.join(MODULE.inputs()).encode() + b'\0'
            name = args[1][1:]
            if name == 'target/' + MODULE.PDFS[0]:
                return b'old staged PDF'
            return (self.root / name).read_bytes()
        with patch.object(MODULE, 'git', side_effect=staged):
            with self.assertRaisesRegex(ValueError, '暂存版本已过期'):
                self.run_command('check', '--staged')

    def check_lfs_pointer(self, oid=None, size=None, tracked=True):
        name = 'target/' + MODULE.PDFS[0]
        data = (self.root / name).read_bytes()
        oid = oid or hashlib.sha256(data).hexdigest()
        size = len(data) if size is None else size
        pointer = (f'version https://git-lfs.github.com/spec/v1\n'
                   f'oid sha256:{oid}\nsize {size}\n').encode()
        def staged(*args):
            if args[0] == 'ls-files':
                return '\0'.join(MODULE.inputs()).encode() + b'\0'
            if args[0] == 'check-attr':
                return (name + ': filter: ' + ('lfs' if tracked else 'unspecified') + '\n').encode()
            path = args[1][1:]
            return pointer if path == name else (self.root / path).read_bytes()
        with patch.object(MODULE, 'git', side_effect=staged):
            self.run_command('check', '--staged')

    def test_accepts_lfs_pointer_matching_pdf_hash_and_size(self):
        self.check_lfs_pointer()

    def test_rejects_lfs_pointer_with_wrong_hash(self):
        with self.assertRaisesRegex(ValueError, '暂存版本已过期'):
            self.check_lfs_pointer(oid='0' * 64)

    def test_rejects_lfs_pointer_with_wrong_size(self):
        with self.assertRaisesRegex(ValueError, '暂存版本已过期'):
            self.check_lfs_pointer(size=1)

    def test_rejects_pointer_without_staged_lfs_attribute(self):
        with self.assertRaisesRegex(ValueError, '暂存版本已过期'):
            self.check_lfs_pointer(tracked=False)
