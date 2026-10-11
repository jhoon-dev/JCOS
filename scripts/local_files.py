"""Shared new-directory writes for the two local-only commands."""
import json
from pathlib import Path


def new_destination(destination: Path) -> Path:
    if '..' in destination.parts:
        raise ValueError('Destination must not contain parent traversal (..)')
    if destination.drive.startswith('\\\\'):
        raise ValueError('UNC and device namespace destinations are not supported')
    if destination.drive and not destination.is_absolute():
        raise ValueError('Drive-relative destinations are not supported')
    destination = destination.absolute()
    for component in (destination, *destination.parents):
        if component.is_symlink() or component.is_junction():
            raise ValueError('Destination must not traverse symlinks or junctions')
    if destination.exists():
        raise FileExistsError('Destination already exists; choose a new directory')
    return destination


def write_json_files(destination: Path, files: dict) -> Path:
    destination = new_destination(destination)
    texts = {}
    for name, data in files.items():
        if Path(name).name != name or not name.endswith('.json'):
            raise ValueError('Output filenames must be plain JSON filenames')
        texts[name] = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    destination.mkdir(parents=True, exist_ok=False)
    created = []
    try:
        for name, text in texts.items():
            target = destination / name
            with target.open('x', encoding='utf-8', newline='\n') as stream:
                created.append(target)
                stream.write(text)
    except OSError as exc:
        try:
            for target in reversed(created):
                target.unlink()
            destination.rmdir()
        except OSError as cleanup_error:
            raise OSError(f'Write failed; cleanup incomplete at {destination}: {cleanup_error}') from exc
        raise
    return destination
