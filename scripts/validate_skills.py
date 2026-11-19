#!/usr/bin/env python3
"""Dependency-free validator for portable Agent Skills bundles."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    md = skill_dir / "SKILL.md"
    if not md.is_file():
        return [f"{skill_dir.name}: missing SKILL.md"]
    content = md.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", content, re.DOTALL)
    if not match:
        return [f"{skill_dir.name}: missing YAML frontmatter"]
    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"{skill_dir.name}: malformed frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("'\"")
    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not name or not NAME_PATTERN.fullmatch(name) or len(name) > 64:
        errors.append(f"{skill_dir.name}: invalid name {name!r}")
    if name != skill_dir.name:
        errors.append(f"{skill_dir.name}: frontmatter name and folder name differ")
    if not description or len(description) > 1024:
        errors.append(f"{skill_dir.name}: description missing or too long")
    if not content[match.end():].strip():
        errors.append(f"{skill_dir.name}: SKILL.md has no instructions")
    for dest in LINK_PATTERN.findall(content):
        if dest.startswith(("http://", "https://", "mailto:", "#")):
            continue
        dest = dest.split("#", 1)[0].split("?", 1)[0]
        if not dest:
            continue
        resolved = (skill_dir / dest).resolve()
        if not resolved.is_relative_to(skill_dir.resolve()) or not resolved.exists():
            errors.append(f"{skill_dir.name}: broken or escaping relative link: {dest}")
    return errors


def main() -> int:
    if not SKILLS.exists():
        print("Missing skills directory", file=sys.stderr)
        return 1
    dirs = sorted(d for d in SKILLS.iterdir() if d.is_dir())
    if not dirs:
        print("No skills found", file=sys.stderr)
        return 1
    failures = [error for d in dirs for error in validate_skill(d)]
    if failures:
        print("VALIDATION FAILED:")
        for error in failures:
            print("-", error)
        return 1
    print(f"PASS: validated {len(dirs)} Agent Skills with valid frontmatter and local links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
