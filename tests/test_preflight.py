import copy
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from preflight import check
from generate import generate

def fixture():
    return {'systems': {'columns': {'id': {'type':'string'}, 'budget': {'type':'integer'}},
            'rows': [{'id': {'value':'action','verified':True,'evidence':'test fixture'},
                      'budget': {'value':1,'verified':True,'evidence':'test fixture'}}]}}

class PreflightTests(unittest.TestCase):
    def test_missing_and_unverified_are_distinct(self):
        sheets = fixture()
        sheets['systems']['rows'][0]['budget'] = {'value':None,'verified':False}
        self.assertEqual(len(check(sheets)), 2)

    def test_foreign_key_and_duplicate(self):
        sheets = fixture()
        sheets['systems']['columns']['id']['ref'] = 'missing'
        sheets['systems']['rows'] *= 2
        self.assertTrue(any('duplicate' in x for x in check(sheets)))
        self.assertTrue(any('unresolved' in x for x in check(sheets)))

    def test_boolean_is_not_budget(self):
        sheets = fixture()
        sheets['systems']['rows'][0]['budget']['value'] = True
        self.assertTrue(any('wrong type' in x for x in check(sheets)))

    def test_blocked_generation_writes_nothing(self):
        sheets = fixture()
        sheets['systems']['rows'][0]['budget']['verified'] = False
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / 'records.py'
            with self.assertRaises(ValueError):
                generate(sheets, target)
            self.assertFalse(target.exists())

    def test_generated_row_is_immutable_and_matches_sheet(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / 'records.py'
            generate(fixture(), target)
            scope = {}
            exec(compile(target.read_text(), str(target), 'exec'), scope)
            record = scope['systems_action']
            self.assertEqual(record.budget, 1)
            with self.assertRaises(AttributeError):
                record.budget = 2

    def test_no_sheets_is_not_success(self):
        self.assertTrue(check({}))
