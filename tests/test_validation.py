"""Mutation tests prove that the checks detect failures, not just the happy path."""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_docs import validate as validate_docs
from validate_example import validate as validate_example


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for folder in ('00_FOUNDATION', '01_CORE', '02_DESIGN_SYSTEM', '03_CONTENT_SYSTEM', '04_AUTOMATION', '06_LIBRARY', 'examples', 'templates'):
            shutil.copytree(ROOT / folder, self.root / folder)
        for name in ('README.md', 'QUICKSTART.md', 'CHANGELOG.md', 'CONTRIBUTING.md', 'SECURITY.md', 'LICENSE.md'):
            shutil.copy2(ROOT / name, self.root / name)
        shutil.copytree(ROOT / 'scripts', self.root / 'scripts', ignore=shutil.ignore_patterns('__pycache__'))

    def test_current_package_passes(self):
        self.assertEqual(validate_docs(self.root), [])
        self.assertEqual(validate_example(self.root / 'examples/request.json', self.root), [])

    def test_source_tampering_fails_hash_check(self):
        path = self.root / '01_CORE/COR-001/COR-001_CORE_INSTRUCTIONS_v2.0.0.md'
        with path.open('a', encoding='utf-8') as stream:
            stream.write('\nTampered\n')
        errors = validate_docs(self.root)
        self.assertTrue(any('SHA-256 mismatch' in error for error in errors))
        self.assertTrue(any('source hash mismatch' in error for error in errors))

    def test_runtime_reordered_instructions_fail(self):
        path = self.root / '06_LIBRARY/PROMPTS/CORE/JCOS_CORE_COMPACT_v2.0.0.md'
        text = path.read_text(encoding='utf-8')
        lines = text.splitlines()
        indexes = [i for i, line in enumerate(lines) if line.startswith(('1. ', '2. '))][:2]
        lines[indexes[0]], lines[indexes[1]] = lines[indexes[1]], lines[indexes[0]]
        path.write_text('\n'.join(lines), encoding='utf-8')
        self.assertTrue(any('compact text or order mismatch' in e for e in validate_docs(self.root)))

    def test_missing_link_fails(self):
        with (self.root / 'README.md').open('a', encoding='utf-8') as stream:
            stream.write('\n[missing](does-not-exist.md)\n')
        self.assertTrue(any('missing link target' in e for e in validate_docs(self.root)))

    def test_unresolved_dependency_fails(self):
        path = self.root / '00_FOUNDATION/document_registry.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['documents'][0]['depends_on'].append('FND-999')
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertTrue(any('unresolved dependency' in e for e in validate_docs(self.root)))

    def test_status_mismatch_fails(self):
        path = self.root / '00_FOUNDATION/document_registry.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['documents'][0]['status'] = 'DRAFT'
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertTrue(any('Status metadata mismatch' in e for e in validate_docs(self.root)))

    def test_new_active_baseline_does_not_silently_replace_current(self):
        path = self.root / '00_FOUNDATION/document_registry.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        candidate = next(d for d in data['documents'] if d['id'] == 'AUT-003' and not d['active'])
        candidate['active'] = True
        path.write_text(json.dumps(data), encoding='utf-8')
        errors = validate_docs(self.root)
        self.assertTrue(any('multiple active baselines' in e for e in errors))
        self.assertTrue(any('duplicate active rule' in e for e in errors))

    def mutate_request(self, mutate):
        path = self.root / 'examples/request.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        mutate(data)
        path.write_text(json.dumps(data), encoding='utf-8')
        return validate_example(path, self.root)

    def test_missing_audience_fails(self):
        self.assertIn('Missing or invalid audience', self.mutate_request(lambda d: d.pop('audience')))

    def test_simple_rejects_external_actions(self):
        self.assertIn('SIMPLE requires external_side_effects=false', self.mutate_request(lambda d: d['constraints'].update(external_side_effects=True)))

    def test_simple_rejects_new_facts(self):
        self.assertIn('SIMPLE requires add_new_facts=false', self.mutate_request(lambda d: d['constraints'].update(add_new_facts=True)))

    def test_invalid_field_type_is_reported(self):
        self.assertIn('Invalid required_fields', self.mutate_request(lambda d: d['output_contract'].update(required_fields=[{}])))

    def test_project_reference_cannot_escape_example(self):
        self.assertIn('project_ref must stay inside the example directory', self.mutate_request(lambda d: d.update(project_ref='../README.md')))


if __name__ == '__main__':
    unittest.main()
