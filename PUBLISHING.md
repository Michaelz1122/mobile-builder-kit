# Mobile Builder Kit — Distribution & Publishing Guide

This guide explains how to maintain, version, and distribute **Mobile Builder Kit** across GitHub, the Agent Skills ecosystem (`skills.sh`), and developer communities.

---

## 1. Repository Discovery & GitHub SEO

To maximize organic discoverability on GitHub and search engines, maintain these verified repository settings:

### Description
> `AI Agent Skills for Android & Expo: Claude Code, Codex, Cursor and Antigravity. Arabic RTL, Google Play updates, in-app review, QA and ASO.`

### Topics
Ensure the following topics are attached to the repository on GitHub:
`agent-skills`, `claude-code`, `google-antigravity`, `codex`, `cursor`, `react-native`, `expo`, `android-development`, `arabic-rtl`, `google-play`, `vibe-coding`

To update topics via GitHub CLI:
```bash
gh repo edit Michaelz1122/mobile-builder-kit \
  --add-topic "agent-skills" \
  --add-topic "claude-code" \
  --add-topic "google-antigravity" \
  --add-topic "codex" \
  --add-topic "cursor" \
  --add-topic "react-native" \
  --add-topic "expo" \
  --add-topic "android-development" \
  --add-topic "arabic-rtl" \
  --add-topic "google-play" \
  --add-topic "vibe-coding"
```

---

## 2. Agent Skills Directory & `skills.sh` Compatibility

Mobile Builder Kit complies with the [Agent Skills standard](https://agentskills.io/specification).

### Verified Discovery with `npx skills`
Developers can discover and install skills from this repository directly using the `skills` CLI:

```bash
# List all discovered skills in this repository
npx skills add Michaelz1122/mobile-builder-kit --list

# Install all skills into detected agents (non-interactively)
npx skills add Michaelz1122/mobile-builder-kit --all

# Install a specific skill (e.g. arabic-rtl) into Claude Code and Cursor
npx skills add Michaelz1122/mobile-builder-kit --skill arabic-rtl --agent claude-code cursor
```

> **Important Difference:**  
> The `skills` CLI installs the modular `SKILL.md` folders into `.agents/skills`, `.claude/skills`, or `.cursor/skills`. However, it does **not** install persistent rules files (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`, or `rules/arabic-rtl.md`).  
> For full rules and skills installation in one step, recommend running the included Python installer:
> `python scripts/install.py --agent all --target /path/to/project --all`

### Directory Submissions (Status & Next Steps)
- **skills.sh**: Automatically indexes public GitHub repositories that follow the Agent Skills folder convention (`skills/<name>/SKILL.md`).
- **External Registries & Awesome Lists**: Before submitting to third-party lists (e.g., `awesome-agent-skills`), ensure CI validation passes on `main` and release tags are created. Do not claim an active listing until a pull request to the respective registry is merged and verified.

---

## 3. Releases, Versioning & Tags

Follow Semantic Versioning (`vMAJOR.MINOR.PATCH`):
- `v0.1.0`: Initial open-source release with 9 skills.
- `v0.1.1`: Multi-model support (Claude Code, OpenAI Codex, Cursor, Antigravity) and persistent rules.

### Creating a New Release
1. Update `CHANGELOG.md` with new features, fixes, and migration notes.
2. Run full local validation:
   ```bash
   python scripts/validate_skills.py
   python -m unittest discover -s tests -v
   ```
3. Commit and tag:
   ```bash
   git tag -a v0.1.2 -m "Release v0.1.2: Brief description"
   git push origin v0.1.2
   ```
4. Create a GitHub Release via CLI:
   ```bash
   gh release create v0.1.2 --title "v0.1.2" --notes "Release notes summary..."
   ```

---

## 4. Community Sharing Channels

When sharing Mobile Builder Kit with developers, focus on authentic problem-solving:
- **React Native & Expo Communities**: Share [arabic-rtl-demo.md](docs/demos/arabic-rtl-demo.md) highlighting solutions for BiDi layout bugs, Arabic phone number flipping, and navigation mirroring.
- **AI Coding Agent Communities**: Share [end-to-end-mobile-flow.md](docs/demos/end-to-end-mobile-flow.md) demonstrating how `app-discovery` and `app-blueprint` prevent hallucinated backends and scope creep.
- **Arabic Developer Groups**: Highlight the native Egyptian Arabic documentation in [README.ar.md](README.ar.md).

---

## 5. Security & Pre-Release Checklist

Never commit:
- Personal Access Tokens (PATs) or Google Play Console service account JSONs.
- Android keystores or `.jks` signing files.
- `.env` files or production API secrets.
- Private app assets or proprietary business logic.
