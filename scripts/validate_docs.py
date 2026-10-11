"""Validate the public JCOS package using only the Python standard library."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compact_lines(text: str, section: str) -> list[str]:
    lines = text.splitlines()
    start = next((i for i, line in enumerate(lines) if line.lstrip('# ').strip() == section), None)
    if start is None:
        raise ValueError(f"Missing section: {section}")
    block = []
    for line in lines[start + 1:]:
        if re.match(r'^#{1,2} ', line):
            break
        if re.match(r'^\d+\. ', line):
            block.append(line.strip())
    return block


def validate(root: Path) -> list[str]:
    errors = []
    registry_path = root / '00_FOUNDATION/document_registry.json'
    try:
        registry = json.loads(registry_path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return [f"Registry: {exc}"]
    documents = registry.get('documents', [])
    seen_entries, active_ids, rules = set(), set(), {}
    states = {'DRAFT', 'REVIEW', 'APPROVED', 'LOCKED', 'DEPRECATED', 'ARCHIVED'}
    registered_paths = set()
    for doc in documents:
        label = f"{doc.get('id')} {doc.get('version')}"
        required = {'id', 'version', 'status', 'path', 'sha256', 'active', 'depends_on'}
        if not required <= doc.keys():
            errors.append(f"{label}: missing registry fields")
            continue
        key = (doc['id'], doc['version'])
        if key in seen_entries:
            errors.append(f"{label}: duplicate document version")
        seen_entries.add(key)
        if doc['status'] not in states:
            errors.append(f"{label}: invalid status")
        if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-z]+\.\d+)?', doc['version']):
            errors.append(f"{label}: invalid version")
        if doc['active']:
            if doc['id'] in active_ids:
                errors.append(f"{label}: multiple active baselines")
            active_ids.add(doc['id'])
        path = root / doc['path']
        registered_paths.add(doc['path'])
        if not path.is_file():
            errors.append(f"{label}: missing file {doc['path']}")
            continue
        if sha256(path) != doc['sha256']:
            errors.append(f"{label}: SHA-256 mismatch")
        text = path.read_text(encoding='utf-8')
        for field, expected in [('Document ID', doc['id']), ('Version', doc['version']), ('Status', doc['status'])]:
            match = re.search(rf'^\| {field} \| ([^|]+) \|', text, re.M)
            if not match or match.group(1).strip() != expected:
                errors.append(f"{label}: {field} metadata mismatch")
        if doc['active']:
            definitions = re.findall(r'^### ([A-Z]+-\d{3})\s*[-–]', text, re.M)
            for rule in definitions:
                if rule in rules:
                    errors.append(f"{label}: duplicate active rule {rule} ({rules[rule]})")
                rules[rule] = label
            if 'rule_count' in doc and len(definitions) != doc['rule_count']:
                errors.append(f"{label}: rule count mismatch")
        for dependency in doc['depends_on']:
            if dependency not in {d.get('id') for d in documents}:
                errors.append(f"{label}: unresolved dependency {dependency}")
    for path in root.glob('0[1-4]_*/**/*_v*.md'):
        if path.relative_to(root).as_posix() not in registered_paths:
            errors.append(f"Unregistered document: {path.relative_to(root)}")
    for path in root.rglob('*.md'):
        if any(p in {'.git', '.venv', 'node_modules'} for p in path.relative_to(root).parts):
            continue
        text = path.read_text(encoding='utf-8')
        # Local Markdown targets; external URL availability is deliberately not tested.
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            target = target.strip('<>').split('#', 1)[0]
            if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                continue
            if not (path.parent / target).is_file():
                errors.append(f"{path.relative_to(root)}: missing link target {target}")
    manifest_path = root / '06_LIBRARY/PROMPTS/CORE/RUNTIME_MANIFEST.md'
    try:
        manifest = manifest_path.read_text(encoding='utf-8')
        runtime_name = re.search(r'\| Runtime File \| `([^`]+)`', manifest).group(1)
        runtime_path = manifest_path.parent / runtime_name
        runtime = runtime_path.read_text(encoding='utf-8')
        expected = re.search(r'\| Runtime SHA-256 \| `([a-f0-9]{64})`', manifest).group(1)
        if sha256(runtime_path) != expected:
            errors.append('Runtime: SHA-256 mismatch')
        manifest_status = re.search(r'\| Runtime Status \| `([^`]+)`', manifest).group(1)
        if f'Runtime Status: {manifest_status}' not in runtime:
            errors.append('Runtime: status mismatch')
        rows = re.findall(r'^\| (COR-\d{3}) \| `([^`]+)` \| `([^`]+)` \| `([a-f0-9]{64})` \|', manifest, re.M)
        if [r[0] for r in rows] != [f'COR-{i:03}' for i in range(1, 9)]:
            errors.append('Runtime: source map must contain COR-001 through COR-008 in order')
        actual_sections = re.split(r'^## COR-\d{3} .*$', runtime, flags=re.M)[1:]
        if len(actual_sections) != len(rows):
            errors.append('Runtime: section count mismatch')
        for index, (doc_id, source_path, section, source_hash) in enumerate(rows):
            source = root / source_path
            if sha256(source) != source_hash:
                errors.append(f'Runtime: {doc_id} source hash mismatch')
            source_lines = compact_lines(source.read_text(encoding='utf-8'), section)
            runtime_lines = re.findall(r'^\d+\. .+$', actual_sections[index], re.M) if index < len(actual_sections) else []
            if not source_lines or source_lines != [line.strip() for line in runtime_lines]:
                errors.append(f'Runtime: {doc_id} compact text or order mismatch')
    except (OSError, AttributeError, ValueError) as exc:
        errors.append(f'Runtime manifest: {exc}')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root)
    for error in errors:
        print(f'FAIL: {error}')
    if errors:
        print(f'{len(errors)} error(s)')
        return 1
    print('PASS: registry, metadata, dependencies, active rule IDs, local links, hashes and Core Runtime')
    print('Scope: static package checks; not semantic approval, external URL checks or project execution QA.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
