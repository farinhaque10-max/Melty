"""Generate immutable row records only after a completely clean preflight."""
import json
import re
from pathlib import Path
from preflight import ROOT, check, load_sheets

def generate(sheets, destination):
    issues = check(sheets)
    if issues:
        raise ValueError('Preflight blocked generation:\n' + '\n'.join(issues))
    lines = ['# Generated from sheets; do not edit.',
             'from dataclasses import dataclass', 'import json', '']
    types = {'string':'str','integer':'int','number':'float','boolean':'bool'}
    for name, sheet in sheets.items():
        if not name.isidentifier() or any(not c.isidentifier() for c in sheet['columns']):
            raise ValueError('Invalid sheet or column identifier')
        class_name = ''.join(part.title() for part in name.split('_')) + 'Row'
        lines += ['@dataclass(frozen=True)', f'class {class_name}:']
        lines += [f'    {column}: {types[spec["type"]]}' for column, spec in sheet['columns'].items()]
        for row in sheet['rows']:
            identity = row['id']['value']
            if not isinstance(identity, str) or not re.fullmatch(r'[a-z][a-z0-9_]*', identity):
                raise ValueError('Row id must be a lowercase Python identifier')
            values = {c: row[c]['value'] for c in sheet['columns']}
            lines += [f'{name}_{identity} = {class_name}(**json.loads({json.dumps(values)!r}))']
        lines += ['']
    source = '\n'.join(lines)
    compile(source, '<generated>', 'exec')
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(source, encoding='utf-8')

if __name__ == '__main__':
    generate(load_sheets(ROOT / 'sheets'), ROOT / 'build' / 'records.py')
