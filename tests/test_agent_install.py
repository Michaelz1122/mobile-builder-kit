"""Regression tests for agent-specific installs, safe defaults and rule formats."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("install_mbk", ROOT / "scripts" / "install.py")
install = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(install)


class AgentInstallTests(unittest.TestCase):
    def test_project_paths_all_agents(self):
        with tempfile.TemporaryDirectory() as temp:
            project = Path(temp) / "project"
            for agent in install.AGENTS:
                with self.subTest(agent=agent):
                    dest, global_mode = install.destinations(agent, project, Path(temp))
                    self.assertEqual(dest, project / install.PROJECT_SKILL_DIRS[agent])
                    self.assertFalse(global_mode)

    def test_global_paths_all_agents(self):
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp)
            for agent in install.AGENTS:
                with self.subTest(agent=agent):
                    dest, global_mode = install.destinations(agent, None, home)
                    self.assertEqual(dest, home / install.GLOBAL_SKILL_DIRS[agent])
                    self.assertTrue(global_mode)

    def test_antigravity_alias_does_not_shadow_builtin(self):
        self.assertEqual(install.installed_skills_for_agent(["grill-me"], "antigravity"), ["app-discovery"])
        self.assertEqual(install.installed_skills_for_agent(["grill-me", "app-discovery"], "antigravity"), ["app-discovery"])
        self.assertEqual(install.installed_skills_for_agent(["grill-me"], "claude"), ["grill-me"])

    def test_project_rules_are_agent_specific(self):
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp) / "home"
            project = Path(temp) / "app"
            paths = [
                ("antigravity", project / ".agents/rules/arabic-rtl.md"),
                ("claude", project / "CLAUDE.md"),
                ("codex", project / "AGENTS.md"),
                ("cursor", project / ".cursor/rules/mobile-builder-kit.mdc"),
            ]
            for agent, output in paths:
                with self.subTest(agent=agent):
                    install.install_agent_rules(agent, project, home)
                    self.assertTrue(output.is_file())
            rtl = (project / ".agents/rules/arabic-rtl.md").read_text(encoding="utf-8")
            self.assertIn("trigger: always_on", rtl)

    def test_global_rules_and_existing_file_safety(self):
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp)
            with patch.object(install.Path, "home", return_value=home):
                self.assertEqual(install.main(["--agent", "claude", "--global", "--all"]), 0)
                self.assertTrue((home / ".claude/skills/app-discovery/SKILL.md").exists())
                self.assertTrue((home / ".claude/CLAUDE.md").exists())
                self.assertEqual(install.main(["--agent", "codex", "--global", "--all"]), 0)
                self.assertTrue((home / ".agents/skills/app-blueprint/SKILL.md").exists())
                self.assertTrue((home / ".codex/AGENTS.md").exists())
                self.assertEqual(install.main(["--agent", "antigravity", "--global", "--all"]), 0)
                self.assertTrue((home / ".gemini/config/skills/arabic-rtl/SKILL.md").exists())
                self.assertTrue((home / ".gemini/GEMINI.md").exists())
                self.assertEqual(install.main(["--agent", "cursor", "--global", "--all"]), 0)
                self.assertTrue((home / ".cursor/skills/app-discovery/SKILL.md").exists())
                stored = home / ".claude/CLAUDE.md"
                stored.write_text("My rules\n", encoding="utf-8")
                self.assertEqual(install.main(["--agent", "claude", "--global", "--all"]), 0)
                self.assertEqual(stored.read_text(encoding="utf-8"), "My rules\n")

    def test_dry_run_copies_nothing(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "app"
            self.assertEqual(install.main(["--agent", "all", "--target", str(path), "--all", "--dry-run"]), 0)
            self.assertFalse(path.exists())

    def test_unrecognized_skill_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(SystemExit):
                install.main(["--target", temp, "--skills", "does-not-exist"])


if __name__ == "__main__":
    unittest.main()
