"""Mutation tests prove that the checks detect failures, not just the happy path."""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_docs import sha256, validate as validate_docs
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

    def test_private_and_temporary_markdown_is_not_checked(self):
        for folder in ('local-work', 'tmp', '05_PROJECTS', '07_QA', '08_HISTORY',
                       '06_LIBRARY/PROMPTS/PROJECTS', '06_LIBRARY/TEMPLATES',
                       '.playwright-mcp', '.venv', 'node_modules'):
            directory = self.root / folder / 'nested'
            directory.mkdir(parents=True)
            (directory / 'notes.md').write_text('[draft](missing.md)\n', encoding='utf-8')
            (directory / 'non-utf8.md').write_bytes(b'\xff')
        self.assertEqual(validate_docs(self.root), [])

    def test_nested_public_markdown_is_still_checked(self):
        directory = self.root / 'templates/custom'
        directory.mkdir()
        (directory / 'notes.md').write_text('[draft](missing.md)\n', encoding='utf-8')
        errors = validate_docs(self.root)
        self.assertTrue(any('missing link target missing.md' in e for e in errors))

    def add_core_version(self, *, active):
        registry_path = self.root / '00_FOUNDATION/document_registry.json'
        registry = json.loads(registry_path.read_text(encoding='utf-8'))
        old = next(d for d in registry['documents'] if d['id'] == 'COR-001' and d['active'])
        new = dict(old, version='2.0.1', active=active,
                   status='LOCKED' if active else 'REVIEW',
                   path=old['path'].replace('v2.0.0', 'v2.0.1'))
        source = (self.root / old['path']).read_bytes()
        source = source.replace(b'| Version | 2.0.0 |', b'| Version | 2.0.1 |')
        source = source.replace(b'| Status | LOCKED |', f"| Status | {new['status']} |".encode())
        new_path = self.root / new['path']
        new_path.write_bytes(source)
        new['sha256'] = sha256(new_path)
        if active:
            old['active'] = False
        registry['documents'].append(new)
        registry_path.write_text(json.dumps(registry), encoding='utf-8')
        return old, new

    def test_runtime_must_follow_active_core_baseline(self):
        old, new = self.add_core_version(active=True)
        self.assertEqual(validate_docs(self.root), [
            'Runtime: COR-001 source does not match active baseline 2.0.1'])
        manifest_path = self.root / '06_LIBRARY/PROMPTS/CORE/RUNTIME_MANIFEST.md'
        manifest = manifest_path.read_text(encoding='utf-8')
        manifest = manifest.replace(old['path'], new['path']).replace(old['sha256'], new['sha256'])
        manifest = manifest.replace('COR-001~COR-008 v2.0.0 LOCKED',
                                    'COR-001 v2.0.1 LOCKED; COR-002~COR-008 v2.0.0 LOCKED')
        manifest_path.write_text(manifest, encoding='utf-8')
        self.assertEqual(validate_docs(self.root), [])

    def test_inactive_core_candidate_does_not_invalidate_runtime(self):
        self.add_core_version(active=False)
        self.assertEqual(validate_docs(self.root), [])

    def test_runtime_requires_an_active_core_baseline(self):
        registry_path = self.root / '00_FOUNDATION/document_registry.json'
        registry = json.loads(registry_path.read_text(encoding='utf-8'))
        next(d for d in registry['documents'] if d['id'] == 'COR-001')['active'] = False
        registry_path.write_text(json.dumps(registry), encoding='utf-8')
        self.assertEqual(validate_docs(self.root), [
            'Runtime: COR-001 requires exactly one active baseline'])

    def test_runtime_rejects_multiple_active_core_baselines(self):
        self.add_core_version(active=False)
        registry_path = self.root / '00_FOUNDATION/document_registry.json'
        registry = json.loads(registry_path.read_text(encoding='utf-8'))
        next(d for d in registry['documents']
             if d['id'] == 'COR-001' and d['version'] == '2.0.1')['active'] = True
        registry_path.write_text(json.dumps(registry), encoding='utf-8')
        errors = validate_docs(self.root)
        self.assertIn('Runtime: COR-001 requires exactly one active baseline', errors)
        self.assertTrue(any('multiple active baselines' in e for e in errors))

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

    def test_project_identity_fields_are_required_strings(self):
        path = self.root / 'examples/project.json'
        original = json.loads(path.read_text(encoding='utf-8'))
        for field in ('project_id', 'name', 'purpose'):
            for value in (None, '', ' \t', 42, [], {}):
                with self.subTest(field=field, value=value):
                    project = dict(original, **{field: value})
                    path.write_text(json.dumps(project), encoding='utf-8')
                    self.assertIn(f'Missing or invalid project.{field}',
                                  validate_example(self.root / 'examples/request.json', self.root))
            with self.subTest(field=field, missing=True):
                project = dict(original)
                project.pop(field)
                path.write_text(json.dumps(project), encoding='utf-8')
                self.assertIn(f'Missing or invalid project.{field}',
                              validate_example(self.root / 'examples/request.json', self.root))

    def test_project_id_must_follow_initializer_slug_format(self):
        path = self.root / 'examples/project.json'
        project = json.loads(path.read_text(encoding='utf-8'))
        for project_id in ('../escape', 'Team Notes', 'team_notes', '-team', 'team--notes'):
            with self.subTest(project_id=project_id):
                project['project_id'] = project_id
                path.write_text(json.dumps(project), encoding='utf-8')
                self.assertIn('project.project_id must be a lowercase ASCII slug',
                              validate_example(self.root / 'examples/request.json', self.root))

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
