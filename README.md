# Mobile Builder Kit

**Free, open-source Agent Skills for AI-assisted Android development** — especially React Native and Expo. [العربية](README.ar.md) · [Agent Skills specification](https://agentskills.io/specification)

Use the skills to define a realistic MVP, improve Arabic RTL, conduct a focused requirements interview, plan native updates and reviews, audit app quality, and prepare for Google Play release.

> These are **instructions for compatible coding agents**, not an Android APK or a guarantee that a particular feature is implemented. Each host has its own skill discovery and rendering rules.

## Included skills

| Skill | Purpose |
| --- | --- |
| `mobile-builder-kit` | Coordinate the end-to-end app workflow |
| `arabic-rtl` | Arabic language readability and app RTL QA |
| `app-discovery` | Structured one-question-at-a-time app interview (**recommended** instead of the built-in Antigravity `/grill-me`) |
| `grill-me` | Legacy alias, retained for compatibility; not installed by `--all` |
| `app-blueprint` | MVP requirements and a single master build prompt |
| `play-in-app-updates` | Plan Google Play native binary update flows |
| `play-in-app-review` | Plan responsible Play in-app review prompts |
| `mobile-quality-audit` | Review security, performance, accessibility and testing |
| `play-launch-checklist` | Release and Google Play policy checklist |
| `mobile-aso-growth` | ASO and measured app acquisition |

## Install — recommended

Requires Python 3.10+ and a local copy of the repository:

```bash
git clone https://github.com/Michaelz1122/mobile-builder-kit.git
cd mobile-builder-kit
python scripts/install.py --list
python scripts/install.py --agent antigravity --target /path/to/your-app --all --dry-run
python scripts/install.py --agent antigravity --target /path/to/your-app --all
```

Change the agent name to `claude`, `codex`, or `cursor`; or use `--agent all` to install for all supported agents. On Windows, use your project directory as the target. An existing configuration is **never overwritten** unless `--force` is explicitly supplied. Make a backup before `--force`.

### Where the installer puts files

| Agent | Project skills | User/global skills | Project rules/config |
| --- | --- | --- | --- |
| Google Antigravity | `.agents/skills/` | `~/.gemini/config/skills/` | `.agents/rules/arabic-rtl.md` with `trigger: always_on` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | `CLAUDE.md` |
| OpenAI Codex | `.agents/skills/` | `~/.agents/skills/` | `AGENTS.md` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` | `.cursor/rules/mobile-builder-kit.mdc` |

Use `python scripts/install.py --agent claude --global --all` for a user-level installation. Cursor's persistent **global** rules are configured in Cursor Settings rather than written automatically by this installer. Antigravity's global guidance is placed in `~/.gemini/GEMINI.md`.

Run `python scripts/install.py --agent all --target /path/to/app --all` to install for multiple tools in one project. Different tools may read the same skill names differently; **test each host rather than assuming universal automatic activation**.

### One skill or rules only

```bash
python scripts/install.py --agent antigravity --target /path/to/app --skills arabic-rtl,app-discovery
python scripts/install.py --agent antigravity --target /path/to/app --rules
```

`--all` installs all recommended skills plus the appropriate rules/config; `--skills` installs only the selected skill folders; `--rules` installs only rules/config. You can still explicitly request `--skills grill-me` for the legacy folder; in Antigravity it maps to `app-discovery` to avoid collision with its built-in command.

## Invoke the skills

After installing and restarting/reloading the agent if necessary, ask:
- "Use **app-discovery** and ask me the key questions for my app, one at a time."
- "Use **arabic-rtl** to audit navigation, mixed Arabic/English text and inputs in this Expo app."
- "Use **app-blueprint** and create an MVP + one build prompt."
- "Use **play-in-app-updates** to inspect my Expo app and plan compatible Play-native updates."
- "Use **mobile-quality-audit** to identify release blockers with evidence."

Some agents provide skill slash commands or picker UI; when unsure, mention the skill name in plain language.

## RTL and safety limitations

- HTML wrappers like `<div dir="rtl">` **must not be forced** into every reply. Markdown renderers, IDEs and terminals vary. Prefer natural Arabic-first sentences and test the real output surface; use HTML direction only where verified.
- Real app RTL is a **UI implementation and device-test requirement**, not a chat formatting trick.
- Play Core in-app updates require Play-distributed eligible builds. Expo OTA updates distribute compatible JS/assets, not native binaries.
- In-app review prompts can be suppressed by Play quotas.
- Audit installed SDK versions and dependencies before implementation; don't imply implementation or production readiness on the basis of instructions alone.
- Publishing, spending money, deleting data and changing credentials require the developer's explicit approval.

## Verify

```bash
python scripts/validate_skills.py
python -m unittest discover -s tests -v
python scripts/install.py --agent all --target /path/to/test-project --all --dry-run
```

See [Arabic README](README.ar.md), [contribution guide](CONTRIBUTING.md), and [publishing instructions](PUBLISHING.md). License: [MIT](LICENSE).

Maintainer: Michael Zahy.
