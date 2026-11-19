# Mobile Builder Kit: Android & Expo Agent Skills

**Open-source Agent Skills and persistent rules for AI Android development with React Native and Expo.**  
Designed for **Claude Code Skills**, **Google Antigravity Skills**, **OpenAI Codex Skills**, and **Cursor Skills**.

[العربية (README.ar.md)](README.ar.md) · [Agent Skills Specification](https://agentskills.io/specification) · [Practical Demos](docs/demos/)

---

## What is Mobile Builder Kit?

**Mobile Builder Kit** is a modular collection of verified **Android Agent Skills** and always-on rules that guide AI coding agents through the full mobile app lifecycle—from requirements discovery and master prompt generation to Google Play in-app updates, review prompts, QA auditing, and store publishing.

> ⭐ **Star this repository** if you build mobile apps with AI and want cleaner prompts, better RTL layouts, and fewer AI hallucinations.

---

## Supported AI Coding Agents

Every skill is packaged according to the open [Agent Skills specification](https://agentskills.io/specification) (`SKILL.md`), paired with agent-native persistent configurations:

| AI Coding Agent | Primary Skill Path | Persistent Config / Rules | Best For |
| :--- | :--- | :--- | :--- |
| **Claude Code** (Anthropic) | `.claude/skills/` | `CLAUDE.md` | Terminal-first autonomous coding |
| **Google Antigravity** | `.agents/skills/` | `.agents/rules/` & `GEMINI.md` | Multimodal agent workflows |
| **OpenAI Codex / ChatGPT** | `.agents/skills/` | `AGENTS.md` | Step-by-step feature implementation |
| **Cursor IDE** | `.cursor/skills/` | `.cursor/rules/*.mdc` | Interactive pair programming |

---

## Problems It Solves

- **Vague Prompts & Scope Creep**: Prevents AI agents from guessing complex backends or unnecessary screens by conducting a disciplined, one-question-at-a-time discovery interview.
- **Arabic RTL & BiDi Layout Bugs**: Enforces strict text direction, layout mirroring, and BiDi punctuation hygiene in **Arabic RTL React Native** and **Expo RTL** apps.
- **Update Confusion**: Clarifies the architectural difference between **Google Play In-App Updates** (native binary releases) and Expo EAS Updates (OTA JavaScript/asset bundles).
- **Google Play In-App Review Pitfalls**: Implements compliant, milestone-based rating requests while respecting Google Play's undisclosed display quotas.
- **Pre-Launch Blind Spots**: Audits apps for security vulnerabilities, permission leaks, Android back button handling, and Google Play Console policies before submission.

---

## Quick Installation

Choose the installation method that fits your workflow:

### Option 1 — Fastest One-Liner (Agent Skills CLI)

Install the skills directly into your detected coding agent using the verified [skills.sh](https://skills.sh) CLI:

```bash
# Add all skills to detected agents in your project
npx skills add Michaelz1122/mobile-builder-kit --all
```

To install specific skills (e.g. `arabic-rtl` and `app-discovery`):
```bash
npx skills add Michaelz1122/mobile-builder-kit --skill arabic-rtl app-discovery
```

> **Note on Persistent Rules:** The `npx skills` CLI installs modular `SKILL.md` folders. To also install persistent agent rules (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`, or `rules/arabic-rtl.md`) for unconditional RTL enforcement, use Option 2 below.

---

### Option 2 — Full Installation with Rules (Python Installer)

Clone the repository and run the non-destructive cross-agent installer:

```bash
git clone https://github.com/Michaelz1122/mobile-builder-kit.git
cd mobile-builder-kit

# Preview changes safely with a dry-run
python scripts/install.py --agent all --target /path/to/your-app --all --dry-run

# Install skills and persistent rules for all agents
python scripts/install.py --agent all --target /path/to/your-app --all
```

You can target a single agent by replacing `--agent all` with `antigravity`, `claude`, `codex`, or `cursor`.  
For a user-level global install across all your projects, run:
```bash
python scripts/install.py --agent claude --global --all
```

*Existing files are never overwritten without `--force`.*

---

## Included Skills

| Skill | Description | Primary Use Case |
| :--- | :--- | :--- |
| [`mobile-builder-kit`](skills/mobile-builder-kit/SKILL.md) | Central workflow orchestrator | End-to-end Android app lifecycle coordination |
| [`app-discovery`](skills/app-discovery/SKILL.md) | Structured requirements interview | Locks in requirements one decision at a time (avoids slash command collisions) |
| [`arabic-rtl`](skills/arabic-rtl/SKILL.md) | Arabic readability & layout QA | **Arabic RTL React Native**, BiDi punctuation hygiene, and mobile UI audit |
| [`app-blueprint`](skills/app-blueprint/SKILL.md) | MVP specification & master prompt | Converts app ideas into a single comprehensive implementation prompt |
| [`play-in-app-updates`](skills/play-in-app-updates/SKILL.md) | Native update planning | Flexible vs immediate **Google Play In-App Updates** (distinguished from Expo OTA) |
| [`play-in-app-review`](skills/play-in-app-review/SKILL.md) | Milestone-based review prompts | Compliant **Expo In-App Review** triggers with store quota safeguards |
| [`mobile-quality-audit`](skills/mobile-quality-audit/SKILL.md) | Pre-release code & security audit | Evidence-based P0–P3 audit for security, offline handling, and accessibility |
| [`play-launch-checklist`](skills/play-launch-checklist/SKILL.md) | Google Play release readiness | AAB signing, targetSdk, 14-day tester requirements, and store compliance |
| [`mobile-aso-growth`](skills/mobile-aso-growth/SKILL.md) | App Store Optimization & metrics | Keyword prioritization, store listing conversion, CPI, and analytics |
| [`grill-me`](skills/grill-me/SKILL.md) | Legacy interview alias | Retained for backward compatibility; prefer `app-discovery` in Antigravity |

---

## How to Invoke Your First Skill

Once installed, open a conversation with your AI coding agent (Claude Code, Antigravity, Codex, or Cursor) and prompt:

### 1. Requirements Discovery
```text
Use app-discovery. I want to build a React Native habit tracker app for Android.
Interview me one question at a time to clarify scope and prevent assumptions.
```

### 2. Arabic & RTL Layout Audit
```text
Use arabic-rtl. Audit this Expo app's navigation, form inputs, and mixed Arabic/English
text layout. Provide code fixes with writingDirection: 'rtl' and BiDi isolation.
```

### 3. Master Implementation Prompt
```text
Use app-blueprint. Convert our discovery notes into a complete MVP specification
and generate one unified master prompt for this repository.
```

### 4. Quality & Pre-Launch Audit
```text
Use mobile-quality-audit. Inspect this codebase for security risks, unhandled offline
errors, Android back button handling, and performance bottlenecks.
```

---

## Practical Demonstrations

Explore real-world guides and code examples in [`docs/demos/`](docs/demos/):

- 📱 [**Arabic RTL React Native & Expo Guide**](docs/demos/arabic-rtl-demo.md) — Problematic vs production-ready implementations, BiDi text isolation, and physical device test checklists.
- ⭐ [**Google Play In-App Review Demo**](docs/demos/play-in-app-review-demo.md) — Production milestone triggers, Expo `expo-store-review` integration, and managing Google Play quotas.
- 🚀 [**End-to-End AI Mobile App Workflow**](docs/demos/end-to-end-mobile-flow.md) — Complete walkthrough from rough idea to discovery, blueprint, audit, and Google Play publishing.

---

## Important Constraints & Honest Realities

1. **Host Renderer Variations**: Prompt instructions alone cannot override every chat client's Markdown renderer. In IDE/Webview chats, `<div dir="rtl">` enables right-to-left layout; in CLI terminals (like Claude Code), HTML tags are omitted to prevent terminal clutter.
2. **Real App RTL Requires UI Implementation**: True RTL support requires `I18nManager`, directional style rules, and real device validation.
3. **Google Play In-App Updates ≠ Expo OTA**: Play Core native updates deliver compiled Android binaries (`.aab`/`.apk`). Expo Updates (`expo-updates`) distribute JavaScript bundles and assets over-the-air.
4. **In-App Review Quotas**: Google Play strictly suppresses review dialogs if a user has recently rated or reviewed an app. The API never confirms whether a dialog was displayed or a review was submitted.
5. **Google Play App Publishing**: Google enforces 14-day continuous closed testing with 12 opted-in testers for personal developer accounts created after November 2023. No skill can bypass official Google Play policies.

---

## Verification & Testing

Mobile Builder Kit includes standalone test suites and zero-dependency validators:

```bash
# Validate all skills frontmatter and local links
python scripts/validate_skills.py

# Run unit tests for installer and agent path resolution
python -m unittest discover -s tests -v

# Dry-run test the installer across all supported agents
python scripts/install.py --agent all --target /tmp/test-app --all --dry-run
```

---

## About the Creator

Hi, I'm **Michael Zahy** — an AI Engineer and Mobile Specialist building production-grade mobile applications with React Native, Expo, and AI Coding Agents.

[![Website](https://img.shields.io/badge/Portfolio-michaelzahy.com-0066cc?style=flat-square&logo=google-chrome&logoColor=white)](https://michaelzahy.com?utm_source=github&utm_medium=readme&utm_campaign=mobile-builder-kit)
[![GitHub](https://img.shields.io/badge/GitHub-@Michaelz1122-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Michaelz1122)

- 💼 **Available for Consulting & Freelance**: Need help building an AI-assisted MVP, fixing complex Arabic RTL layouts, or preparing an Android app for Google Play release?
- 🌐 **Explore My Work**: Discover my latest apps, case studies, and services at [michaelzahy.com](https://michaelzahy.com?utm_source=github&utm_medium=readme&utm_campaign=mobile-builder-kit).

---

## Contributing & Distribution

Contributions, bug reports, and enhancements backed by official Android, Expo, or Google Play documentation are welcome!

- See [CONTRIBUTING.md](CONTRIBUTING.md) for code of conduct and pull request guidelines.
- See [PUBLISHING.md](PUBLISHING.md) for release versioning, GitHub Topics, and Skills directory distribution.
- See [CHANGELOG.md](CHANGELOG.md) for release history.

**License**: [MIT](LICENSE) © 2026 Michael Zahy.
