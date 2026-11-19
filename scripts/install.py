#!/usr/bin/env python3
"""Install the open-source Agent Skills into an Antigravity project or user profile."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    place = parser.add_mutually_exclusive_group()
    place.add_argument("--target", type=Path, help="Android project root; installs to .agents/skills")
    place.add_argument("--global", dest="globally", action="store_true", help="Install into ~/.gemini/config/skills")
    choose = parser.add_mutually_exclusive_group()
    choose.add_argument("--all", action="store_true", help="Install all skills")
    choose.add_argument("--skills", help="Comma-separated names to install")
    parser.add_argument("--list", action="store_true", help="List available skill names")
    parser.add_argument("--force", action="store_true", help="Overwrite existing skills (make a backup first)")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without copying files")
    args = parser.parse_args()
    names = sorted(d.name for d in SKILLS.iterdir() if d.is_dir() and (d / "SKILL.md").is_file())
    if args.list:
        print("\n".join(names))
        return 0
    if not args.all and not args.skills:
        parser.error("Choose --all or --skills (or --list)")
    if not args.target and not args.globally:
        parser.error("Choose --target PROJECT or --global")
    selected = names if args.all else [x.strip() for x in args.skills.split(",") if x.strip()]
    unknown = sorted(set(selected) - set(names))
    if unknown:
        parser.error(f"Unknown skill names: {', '.join(unknown)}")
    dest = Path.home() / ".gemini" / "config" / "skills" if args.globally else args.target.expanduser().resolve() / ".agents" / "skills"
    for name in selected:
        print(install_skill(name, dest, force=args.force, dry_run=args.dry_run))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
