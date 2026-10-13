"""Check every sheet cell and foreign key; never infer verified evidence."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def load_sheets(folder):
    return {p.stem: json.loads(p.read_text(encoding='utf-8'))
            for p in sorted(Path(folder).glob('*.json'))}

def check(sheets):
    issues = []
    if not sheets:
        return ['No sheets found']
    identifiers = {}
    for name, sheet in sheets.items():
        identifiers[name] = set()
        if not sheet.get('rows'):
            issues.append(f'{name}: no rows')
        columns = sheet.get('columns', {})
        if 'id' not in columns:
            issues.append(f'{name}: missing id column')
        for index, row in enumerate(sheet.get('rows', [])):
            label = row.get('id', {}).get('value', index)
            if not isinstance(label, (str, int)):
                label = index
            prefix = f'{name}.{label}'
            if label in identifiers[name]:
                issues.append(f'{prefix}: duplicate id')
            identifiers[name].add(label)
            for column, spec in columns.items():
                cell = row.get(column)
                if not isinstance(cell, dict):
                    issues.append(f'{prefix}.{column}: missing cell')
                    continue
                value = cell.get('value')
                if value is None or value == '':
                    issues.append(f'{prefix}.{column}: unfilled')
                expected = {'string': str, 'integer': int, 'number': (int, float),
                            'boolean': bool}.get(spec.get('type'))
                if expected is None:
                    issues.append(f'{prefix}.{column}: unsupported column type')
                elif value is not None and (not isinstance(value, expected)
                        or isinstance(value, bool) and spec.get('type') in ('integer','number')):
                    issues.append(f'{prefix}.{column}: wrong type')
                if cell.get('verified') is not True or not cell.get('evidence'):
                    issues.append(f'{prefix}.{column}: unverified')
            for column in row.keys() - columns.keys():
                issues.append(f'{prefix}.{column}: undeclared column')
    for name, sheet in sheets.items():
        for row in sheet.get('rows', []):
            for column, spec in sheet.get('columns', {}).items():
                target = spec.get('ref')
                value = row.get(column, {}).get('value')
                if target and value not in identifiers.get(target, set()):
                    issues.append(f'{name}.{column}: unresolved {target}:{value}')
    return issues

def main():
    issues = check(load_sheets(ROOT / 'sheets'))
    for issue in issues:
        print(issue)
    print(f'Preflight: {len(issues)} issues; ' + ('BLOCKED' if issues else 'clean'))
    return bool(issues)

if __name__ == '__main__':
    sys.exit(main())
