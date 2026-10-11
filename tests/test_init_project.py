"""Exercise independent user settings and refusal paths without external actions."""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from init_project import initialize
from validate_example import validate


class InitProjectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.destination = Path(self.temp.name) / 'new project'
        self.settings = dict(project_id='team-notes', name='Team Notes',
                             purpose='Clarify an internal reminder', audience='New teammates',
                             language='en', source_text='Please send feedback after reviewing.')

    def test_independent_users_and_unicode_paths(self):
        variants = [self.settings, dict(project_id='study-guide', name='학습 안내',
                    purpose='안내문 명료화', audience='신규 학습자', language='ko',
                    source_text='검토 후 의견을 보내 주세요.')]
        for i, settings in enumerate(variants):
            with self.subTest(language=settings['language']):
                path = initialize(self.destination / f'사용자 {i}', **settings)
                self.assertEqual(validate(path), [])
                request = json.loads(path.read_text(encoding='utf-8'))
                project = json.loads((path.parent / 'project.json').read_text(encoding='utf-8'))
                self.assertEqual(project['name'], settings['name'])
                self.assertEqual(project['project_id'], settings['project_id'])
                for field, key in [('purpose', 'purpose'), ('audience', 'audience'),
                                   ('output_language', 'language'), ('source_text', 'source_text')]:
                    self.assertEqual(request[field], settings[key])
                self.assertFalse(request['constraints']['external_side_effects'])
                self.assertIsNone(project['master'])

    def test_existing_directory_is_preserved(self):
        self.destination.mkdir()
        sentinel = self.destination / 'project.json'
        sentinel.write_text('keep', encoding='utf-8')
        with self.assertRaises(FileExistsError):
            initialize(self.destination, **self.settings)
        self.assertEqual(sentinel.read_text(encoding='utf-8'), 'keep')
        self.assertFalse((self.destination / 'request.json').exists())

    def test_invalid_settings_create_nothing(self):
        for changes in [dict(audience=' '), dict(project_id='../escape'), dict(source_text='')]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                initialize(self.destination, **(self.settings | changes))
            self.assertFalse(self.destination.exists())

    def test_parent_traversal_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'parent traversal'):
            initialize(self.destination / '..' / 'escaped', **self.settings)
        self.assertFalse(self.destination.exists())

    @unittest.skipUnless(sys.platform == 'win32', 'Windows path semantics')
    def test_windows_nonlocal_and_drive_relative_paths_are_rejected(self):
        for value in ('C:relative', r'\\server\share\new-project', r'\\?\C:\new-project'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                initialize(Path(value), **self.settings)

    def test_cleanup_failure_reports_remaining_path(self):
        original_open = Path.open
        def fail_second_file(path, *args, **kwargs):
            if path == self.destination / 'request.json' and args and args[0] == 'x':
                raise OSError('simulated write failure')
            return original_open(path, *args, **kwargs)
        original_unlink = Path.unlink
        def fail_owned_unlink(path, *args, **kwargs):
            if path == self.destination / 'project.json':
                raise PermissionError('simulated cleanup failure')
            return original_unlink(path, *args, **kwargs)
        with patch.object(Path, 'open', fail_second_file), patch.object(Path, 'unlink', fail_owned_unlink):
            with self.assertRaisesRegex(OSError, 'cleanup incomplete') as result:
                initialize(self.destination, **self.settings)
        self.assertIn(str(self.destination), str(result.exception))
        self.assertTrue((self.destination / 'project.json').is_file())

    def test_existing_file_is_preserved(self):
        self.destination.write_text('keep', encoding='utf-8')
        with self.assertRaises(FileExistsError):
            initialize(self.destination, **self.settings)
        self.assertEqual(self.destination.read_text(encoding='utf-8'), 'keep')

    def test_linked_ancestor_is_rejected(self):
        for method in ('is_symlink', 'is_junction'):
            with self.subTest(method=method):
                with patch.object(Path, method, lambda p: p == self.destination.parent):
                    with self.assertRaisesRegex(ValueError, 'symlinks or junctions'):
                        initialize(self.destination, **self.settings)
                self.assertFalse(self.destination.exists())

    def test_strings_are_json_data(self):
        text = '"quoted" \\path\n[link](missing.md) `code` $(command); <script> & 한글'
        settings = self.settings | dict(name=text, purpose=text, audience=text, source_text=text)
        path = initialize(self.destination, **settings)
        request = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(request['source_text'], text)
        self.assertEqual(request['audience'], text)
        self.assertEqual(validate(path), [])
        self.assertEqual(sorted(p.name for p in path.parent.iterdir()), ['project.json', 'request.json'])

    def test_write_failure_rolls_back_created_files(self):
        original_open = Path.open
        def fail_second_file(path, *args, **kwargs):
            if path == self.destination / 'request.json' and args and args[0] == 'x':
                raise OSError('simulated disk failure')
            return original_open(path, *args, **kwargs)
        with patch.object(Path, 'open', fail_second_file):
            with self.assertRaisesRegex(OSError, 'simulated disk failure'):
                initialize(self.destination, **self.settings)
        self.assertFalse(self.destination.exists())

    def test_broken_baseline_creates_nothing(self):
        fixture = Path(self.temp.name) / 'fixture'
        for folder in ('templates', '00_FOUNDATION', '01_CORE'):
            shutil.copytree(ROOT / folder, fixture / folder)
        source = fixture / '01_CORE/COR-001/COR-001_CORE_INSTRUCTIONS_v2.0.0.md'
        with source.open('a', encoding='utf-8') as stream:
            stream.write('\nTampered\n')
        with self.assertRaisesRegex(ValueError, 'Baseline hash mismatch'):
            initialize(self.destination, root=fixture, **self.settings)
        self.assertFalse(self.destination.exists())

    def test_unsafe_template_creates_nothing(self):
        fixture = Path(self.temp.name) / 'fixture'
        for folder in ('templates', '00_FOUNDATION', '01_CORE'):
            shutil.copytree(ROOT / folder, fixture / folder)
        path = fixture / 'templates/local-editing/request.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['constraints']['external_side_effects'] = True
        path.write_text(json.dumps(data), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'external_side_effects=false'):
            initialize(self.destination, root=fixture, **self.settings)
        self.assertFalse(self.destination.exists())


if __name__ == '__main__':
    unittest.main()
