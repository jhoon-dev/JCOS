"""Shared JSON writes must leave no partial destination after encoding failures."""
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from local_files import write_json_files


class LocalFilesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.destination = Path(self.temp.name) / 'new-parent/output'

    def test_unencodable_later_file_creates_no_directories(self):
        with self.assertRaises(UnicodeEncodeError):
            write_json_files(self.destination, {
                'project.json': {'name': 'Valid project'},
                'request.json': {'source_text': 'draft \ud800'},
            })
        self.assertFalse(self.destination.parent.exists())

    def test_unicode_write_error_cleans_created_files(self):
        original_open = Path.open

        @contextmanager
        def fail_second_write(path, *args, **kwargs):
            with original_open(path, *args, **kwargs) as stream:
                if path == self.destination / 'request.json' and args and args[0] == 'x':
                    failing_stream = Mock(wraps=stream)
                    failing_stream.write.side_effect = UnicodeEncodeError(
                        'utf-8', '\ud800', 0, 1, 'simulated encoding failure')
                    yield failing_stream
                else:
                    yield stream

        sentinel = Path(self.temp.name) / 'keep.txt'
        sentinel.write_text('keep', encoding='utf-8')
        with patch.object(Path, 'open', fail_second_write):
            with self.assertRaises(UnicodeEncodeError):
                write_json_files(self.destination, {
                    'project.json': {'name': 'Valid project'},
                    'request.json': {'source_text': 'Valid draft'},
                })
        self.assertFalse(self.destination.exists())
        self.assertEqual(sentinel.read_text(encoding='utf-8'), 'keep')


if __name__ == '__main__':
    unittest.main()
