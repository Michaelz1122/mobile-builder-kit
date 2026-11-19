"""Checks basic skill validity and non-destructive installation behavior."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(relative_path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


validate = load('scripts/validate_skills.py', 'validate_skills')
installer = load('scripts/install.py', 'install_skills')


class SkillPackTests(unittest.TestCase):
    def test_all_skills_validate(self):
        skill_paths = sorted(p for p in (ROOT / 'skills').iterdir() if p.is_dir())
        self.assertGreaterEqual(len(skill_paths), 8)
        for path in skill_paths:
            with self.subTest(skill=path.name):
                self.assertEqual(validate.validate_skill(path), [])

    def test_installer_does_not_overwrite_by_default(self):
        with tempfile.TemporaryDirectory() as dirname:
            dest = Path(dirname) / '.agents' / 'skills'
            self.assertTrue(installer.install_skill('arabic-rtl', dest).startswith('OK'))
            installed = dest / 'arabic-rtl' / 'SKILL.md'
            installed.write_text('user-edited\n', encoding='utf-8')
            self.assertTrue(installer.install_skill('arabic-rtl', dest).startswith('SKIP'))
            self.assertEqual(installed.read_text(encoding='utf-8'), 'user-edited\n')
            self.assertTrue(installer.install_skill('arabic-rtl', dest, force=True).startswith('OK'))
            self.assertIn('name: arabic-rtl', installed.read_text(encoding='utf-8'))

    def test_dry_run_does_not_create_files(self):
        with tempfile.TemporaryDirectory() as dirname:
            dest = Path(dirname) / 'missing' / 'skills'
            self.assertTrue(installer.install_skill('grill-me', dest, dry_run=True).startswith('WOULD'))
            self.assertFalse(dest.exists())


if __name__ == '__main__':
    unittest.main()
