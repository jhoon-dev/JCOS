"""Check the bounded public local-editing example; never execute external actions."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from validate_docs import ROOT, sha256


def validate(path: Path, root: Path = ROOT) -> list[str]:
    errors = []
    try:
        request = json.loads(path.read_text(encoding='utf-8'))
        if not isinstance(request, dict):
            return ['Request must be an object']
        for field in ('request_id', 'project_ref', 'purpose', 'audience', 'output_language', 'source_text'):
            if not isinstance(request.get(field), str) or not request[field].strip():
                errors.append(f'Missing or invalid {field}')
        if errors:
            return errors
        if request.get('profile') != 'SIMPLE':
            errors.append('This example validator only supports SIMPLE local editing')
        constraints = request.get('constraints')
        if not isinstance(constraints, dict):
            errors.append('Missing constraints')
        else:
            for field in ('add_new_facts', 'external_side_effects', 'change_master'):
                if constraints.get(field) is not False:
                    errors.append(f'SIMPLE requires {field}=false')
        contract = request.get('output_contract')
        if not isinstance(contract, dict):
            errors.append('Missing output_contract')
        else:
            fields = contract.get('required_fields')
            if not isinstance(fields, list) or not all(isinstance(f, str) for f in fields):
                errors.append('Invalid required_fields')
            elif not {'status', 'revised_text', 'checks', 'limitations'} <= set(fields):
                errors.append('Incomplete output_contract')
            criteria = contract.get('completion_criteria')
            if not isinstance(criteria, str) or not criteria.strip():
                errors.append('Missing completion_criteria')
        project_path = (path.parent / request['project_ref']).resolve()
        if not project_path.is_relative_to(path.parent.resolve()):
            return errors + ['project_ref must stay inside the example directory']
        project = json.loads(project_path.read_text(encoding='utf-8'))
        if not isinstance(project, dict):
            return errors + ['Project must be an object']
        for field in ('project_id', 'name', 'purpose'):
            if not isinstance(project.get(field), str) or not project[field].strip():
                errors.append(f'Missing or invalid project.{field}')
        project_id = project.get('project_id')
        if isinstance(project_id, str) and project_id.strip():
            if not re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', project_id):
                errors.append('project.project_id must be a lowercase ASCII slug')
        if project.get('scope') != 'LOCAL_INTERNAL_DRAFT' or project.get('external_side_effects') is not False:
            errors.append('Project must be a local internal draft without external side effects')
        if project.get('master') is not None:
            errors.append('This example has no approved MASTER')
        refs = project.get('baseline_refs')
        if not isinstance(refs, list) or not refs or not all(isinstance(ref, str) for ref in refs):
            return errors + ['Missing or invalid baseline_refs']
        registry = json.loads((root / '00_FOUNDATION/document_registry.json').read_text(encoding='utf-8'))
        active = {d['id']: d for d in registry['documents'] if d['active']}
        for ref in refs:
            if ref not in active or active[ref]['status'] not in {'APPROVED', 'LOCKED'}:
                errors.append(f'Unavailable baseline {ref}')
            elif sha256(root / active[ref]['path']) != active[ref]['sha256']:
                errors.append(f'Baseline hash mismatch: {ref}')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f'Example: {exc}')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('request', type=Path)
    args = parser.parse_args()
    errors = validate(args.request)
    for error in errors:
        print(f'FAIL: {error}')
    if errors:
        return 1
    print('PASS: local editing example input')
    print('Scope: input validation only; no generated output, publication or operational approval.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
