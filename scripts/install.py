#!/usr/bin/env python3
"""Install open-source Agent Skills and Rules for Antigravity, Claude, Codex, and Cursor."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
RULES = ROOT / "rules"


def install_skill(name: str, destination: Path, *, force: bool = False, dry_run: bool = False) -> str:
    source = SKILLS / name
    if not source.is_dir() or not (source / "SKILL.md").is_file():
        raise ValueError(f"Unknown skill: {name}")
    output = destination / name
    if output.exists() and not force:
        return f"SKIP  {name}: already exists (use --force to replace)"
    if dry_run:
        return f"WOULD INSTALL {name} -> {output}"
    destination.mkdir(parents=True, exist_ok=True)
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(source, output)
    return f"OK    {name} -> {output}"


def install_rule(file_name: str, destination: Path, *, force: bool = False, dry_run: bool = False) -> str:
    source = RULES / file_name
    if not source.is_file():
        raise ValueError(f"Unknown rule: {file_name}")
    output = destination / file_name
    if output.exists() and not force:
        return f"SKIP  rule {file_name}: already exists (use --force to replace)"
    if dry_run:
        return f"WOULD INSTALL rule {file_name} -> {output}"
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, output)
    return f"OK    rule {file_name} -> {output}"


def copy_agent_config(source_file: str, destination: Path, *, force: bool = False, dry_run: bool = False) -> str:
    source = ROOT / source_file
    if not source.is_file():
        return f"SKIP  {source_file}: source not found"
    output = destination / source_file
    if output.exists() and not force:
        return f"SKIP  {source_file}: already exists at destination (use --force to replace)"
    if dry_run:
        return f"WOULD INSTALL {source_file} -> {output}"
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, output)
    return f"OK    {source_file} -> {output}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    place = parser.add_mutually_exclusive_group()
    place.add_argument("--target", type=Path, help="Project root; installs skills to .agents/skills and rules to .agents/rules")
    place.add_argument("--global", dest="globally", action="store_true", help="Install into ~/.gemini/config")
    choose = parser.add_mutually_exclusive_group()
    choose.add_argument("--all", action="store_true", help="Install all skills and rules")
    choose.add_argument("--skills", help="Comma-separated skill names to install")
    choose.add_argument("--rules", action="store_true", help="Install rules only")
    parser.add_argument("--agent", choices=["all", "antigravity", "claude", "codex", "cursor"], default="all",
                        help="Target AI agent configuration to install (default: all)")
    parser.add_argument("--list", action="store_true", help="List available skill and rule names")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files (make a backup first)")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without copying files")
    args = parser.parse_args()

    names = sorted(d.name for d in SKILLS.iterdir() if d.is_dir() and (d / "SKILL.md").is_file())
    rule_files = sorted(f.name for f in RULES.glob("*.md")) if RULES.is_dir() else []

    if args.list:
        print("Skills:")
        for n in names:
            print(f"  - {n}")
        if rule_files:
            print("Rules:")
            for r in rule_files:
                print(f"  - {r}")
        print("Supported Agents: Antigravity (Gemini), Claude Code (Anthropic), Codex / ChatGPT (OpenAI), Cursor")
        return 0

    if not args.all and not args.skills and not args.rules:
        parser.error("Choose --all, --skills, --rules (or --list)")
    if not args.target and not args.globally:
        parser.error("Choose --target PROJECT or --global")

    project_root = args.target.expanduser().resolve() if args.target else None
    skills_dest = (Path.home() / ".gemini" / "config" / "skills") if args.globally else (project_root / ".agents" / "skills")
    rules_dest = (Path.home() / ".gemini" / "config" / "rules") if args.globally else (project_root / ".agents" / "rules")

    if args.all or args.skills:
        selected = names if args.all else [x.strip() for x in args.skills.split(",") if x.strip()]
        unknown = sorted(set(selected) - set(names))
        if unknown:
            parser.error(f"Unknown skill names: {', '.join(unknown)}")
        for name in selected:
            print(install_skill(name, skills_dest, force=args.force, dry_run=args.dry_run))

    if args.all or args.rules:
        for r in rule_files:
            print(install_rule(r, rules_dest, force=args.force, dry_run=args.dry_run))

    if project_root:
        if args.agent in ("all", "claude"):
            print(copy_agent_config("CLAUDE.md", project_root, force=args.force, dry_run=args.dry_run))
        if args.agent in ("all", "codex", "antigravity"):
            print(copy_agent_config("AGENTS.md", project_root, force=args.force, dry_run=args.dry_run))
        if args.agent in ("all", "cursor"):
            print(copy_agent_config(".cursorrules", project_root, force=args.force, dry_run=args.dry_run))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
