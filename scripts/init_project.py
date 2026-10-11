"""Create a local editing contract from templates; never run AI or external actions."""
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path

from validate_docs import ROOT
from validate_example import validate
from local_files import new_destination, write_json_files


def initialize(destination: Path, *, project_id: str, name: str, purpose: str,
               audience: str, language: str, source_text: str,
               root: Path = ROOT) -> Path:
    """Validate before writing, and refuse any existing destination."""
    values = dict(project_id=project_id, name=name, purpose=purpose,
                  audience=audience, language=language, source_text=source_text)
    for field, value in values.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f'Missing or invalid {field}')
    if not re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', project_id):
        raise ValueError('project_id must be a lowercase ASCII slug (for example team-notes)')
    destination = new_destination(destination)
    template_dir = root / 'templates/local-editing'
    project = json.loads((template_dir / 'project.json').read_text(encoding='utf-8'))
    request = json.loads((template_dir / 'request.json').read_text(encoding='utf-8'))
    project.update(project_id=project_id, name=name, purpose=purpose)
    request.update(request_id=f'{project_id}-edit-001', purpose=purpose,
                   audience=audience, output_language=language, source_text=source_text)
    # Staging keeps invalid contracts away from the user's destination.
    with tempfile.TemporaryDirectory() as temp:
        staging = Path(temp)
        for filename, data in [('project.json', project), ('request.json', request)]:
            (staging / filename).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        errors = validate(staging / 'request.json', root)
        if errors:
            raise ValueError('; '.join(errors))
        write_json_files(destination, {'project.json': project, 'request.json': request})
    return destination / 'request.json'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path)
    parser.add_argument('--project-id', required=True)
    parser.add_argument('--name', required=True)
    parser.add_argument('--purpose', required=True)
    parser.add_argument('--audience', required=True)
    parser.add_argument('--language', required=True)
    parser.add_argument('--source-text', required=True)
    args = parser.parse_args()
    try:
        request = initialize(args.destination, project_id=args.project_id, name=args.name,
                             purpose=args.purpose, audience=args.audience,
                             language=args.language, source_text=args.source_text)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1
    print(f'PASS: created local editing contract at {request}')
    print('Scope: validated input only; no AI execution, publication, schedule or approval.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
