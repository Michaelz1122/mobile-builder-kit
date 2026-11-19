#!/usr/bin/env python3
"""Install Mobile Builder Kit skills and optional rules into supported coding agents."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
RULES = ROOT / "rules"
AGENTS = ("antigravity", "claude", "codex", "cursor")
PROJECT_SKILL_DIRS = {
    "antigravity": ".agents/skills",
    "claude": ".claude/skills",
    "codex": ".agents/skills",
    "cursor": ".cursor/skills",
}
GLOBAL_SKILL_DIRS = {
    "antigravity": ".gemini/config/skills",
    "claude": ".claude/skills",
    "codex": ".agents/skills",
    "cursor": ".cursor/skills",
}
LEGACY_SKILL = "grill-me"
PREFERRED_SKILL = "app-discovery"


def install_skill(name: str, destination: Path, *, force: bool = False, dry_run: bool = False) -> str:
    source = SKILLS / name
    if not source.is_dir() or not (source / "SKILL.md").is_file():
        raise ValueError(f"Unknown skill: {name}")
    output = destination / name
    if output.exists() and not force:
        return f"SKIP  {name}: already exists (use --force after a backup)"
    if dry_run:
        return f"WOULD INSTALL {name} -> {output}"
    destination.mkdir(parents=True, exist_ok=True)
    if output.exists():
        if output.is_dir() and not output.is_symlink():
            shutil.rmtree(output)
        else:
            output.unlink()
    shutil.copytree(source, output)
    return f"OK    {name} -> {output}"


def copy_file(source: Path, output: Path, *, force: bool = False, dry_run: bool = False) -> str:
    if not source.is_file():
        raise FileNotFoundError(f"Missing source file: {source}")
    if output.exists() and not force:
        return f"SKIP  {output}: already exists (use --force after a backup)"
    if dry_run:
        return f"WOULD INSTALL {source.name} -> {output}"
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, output)
    return f"OK    {source.name} -> {output}"


def install_rule(file_name: str, destination: Path, *, force: bool = False, dry_run: bool = False) -> str:
    return copy_file(RULES / file_name, destination / file_name, force=force, dry_run=dry_run)


def copy_agent_config(source_file: str, destination: Path, *, force: bool = False, dry_run: bool = False) -> str:
    """Legacy helper: copy a named project configuration into a project root."""
    return copy_file(ROOT / source_file, destination / source_file, force=force, dry_run=dry_run)


def installed_skills_for_agent(selected: list[str], agent: str) -> list[str]:
    # Antigravity already reserves /grill-me. Install our non-conflicting name there.
    mapped = [PREFERRED_SKILL if agent == "antigravity" and n == LEGACY_SKILL else n for n in selected]
    return list(dict.fromkeys(mapped))


def destinations(agent: str, project_root: Path | None, home: Path) -> tuple[Path, bool]:
    if project_root is not None:
        return project_root / PROJECT_SKILL_DIRS[agent], False
    return home / GLOBAL_SKILL_DIRS[agent], True


def install_agent_rules(agent: str, project_root: Path | None, home: Path, *,
                        force: bool = False, dry_run: bool = False) -> list[str]:
    """Write rules only to documented locations, without claiming renderer guarantees."""
    if agent == "antigravity":
        if project_root is not None:
            return [install_rule("arabic-rtl.md", project_root / ".agents" / "rules",
                                 force=force, dry_run=dry_run)]
        return [copy_file(ROOT / "GEMINI.md", home / ".gemini" / "GEMINI.md",
                          force=force, dry_run=dry_run)]
    if agent == "claude":
        dest = (project_root / "CLAUDE.md") if project_root else (home / ".claude" / "CLAUDE.md")
        return [copy_file(ROOT / "CLAUDE.md", dest, force=force, dry_run=dry_run)]
    if agent == "codex":
        dest = (project_root / "AGENTS.md") if project_root else (home / ".codex" / "AGENTS.md")
        return [copy_file(ROOT / "AGENTS.md", dest, force=force, dry_run=dry_run)]
    if agent == "cursor":
        if project_root is None:
            return ["NOTE  Cursor global rules are configured in Cursor Settings > Rules; only skills were installed."]
        return [copy_file(ROOT / ".cursor" / "rules" / "mobile-builder-kit.mdc",
                          project_root / ".cursor" / "rules" / "mobile-builder-kit.mdc",
                          force=force, dry_run=dry_run)]
    raise ValueError(f"Unknown agent: {agent}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    place = parser.add_mutually_exclusive_group()
    place.add_argument("--target", type=Path, help="Project root containing the AI agent configuration")
    place.add_argument("--global", dest="globally", action="store_true", help="Install for the current OS user")
    choose = parser.add_mutually_exclusive_group()
    choose.add_argument("--all", action="store_true", help="Install supported skills and rules")
    choose.add_argument("--skills", help="Comma-separated skill names; does not install persistent rules")
    choose.add_argument("--rules", action="store_true", help="Install persistent rules only")
    parser.add_argument("--agent", choices=["all", *AGENTS], default="all",
                        help="Which agent gets the files (default: all)")
    parser.add_argument("--list", action="store_true", help="List skill names and agents")
    parser.add_argument("--force", action="store_true", help="Replace existing files (back up your files first)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change, without writing")
    args = parser.parse_args(argv)

    available = sorted(d.name for d in SKILLS.iterdir() if d.is_dir() and (d / "SKILL.md").is_file())
    if args.list:
        print("Skills:", ", ".join(n for n in available if n != LEGACY_SKILL))
        print("Legacy alias: grill-me (prefer app-discovery; Antigravity reserves /grill-me)")
        print("Agents:", ", ".join(AGENTS))
        return 0

    if not (args.all or args.skills or args.rules):
        parser.error("Choose --all, --skills, --rules (or --list)")
    if not (args.target or args.globally):
        parser.error("Choose --target PROJECT or --global")

    selected = (
        [n for n in available if n != LEGACY_SKILL] if args.all else
        [n.strip() for n in args.skills.split(",") if n.strip()] if args.skills else []
    )
    unknown = sorted(set(selected) - set(available))
    if unknown:
        parser.error("Unknown skill names: " + ", ".join(unknown))

    project_root = args.target.expanduser().resolve() if args.target else None
    home = Path.home()
    agents = AGENTS if args.agent == "all" else (args.agent,)
    printed = set()
    for agent in agents:
        skill_dest, _ = destinations(agent, project_root, home)
        for name in installed_skills_for_agent(selected, agent):
            key = (str(skill_dest), name)
            if key in printed:
                continue
            printed.add(key)
            print(install_skill(name, skill_dest, force=args.force, dry_run=args.dry_run))
        if args.all or args.rules:
            for outcome in install_agent_rules(agent, project_root, home, force=args.force, dry_run=args.dry_run):
                print(outcome)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
