# AGENTS.md — Universal Agent & Model Instructions
<!-- Compatible with: OpenAI Codex / ChatGPT, Anthropic Claude, Google Gemini / Antigravity, Cursor, Copilot -->

## Project Context
**Mobile Builder Kit** is an open-source, multi-model Agent Skill and Rule bundle for building mobile apps with AI.
- Architecture: React Native + Expo.
- Skills format: Modular `SKILL.md` following [Agent Skills standard](https://agentskills.io/specification).
- Scope: Idea discovery, architectural blueprint, Arabic RTL & BiDi hygiene, Play updates & reviews, QA audit, store launch, and ASO growth.

---

## Universal Rules for All AI Coding Models (Codex, Claude, Gemini)

### 1. Arabic RTL & BiDi Hygiene Rule
- **Web / IDE / Webview surfaces** (Antigravity, Cursor, VS Code, ChatGPT web): Wrap full Arabic responses with `<div dir="rtl">` at start and `</div>` at end.
- **Terminal / CLI surfaces** (Claude Code CLI, Codex Terminal, GitHub Copilot CLI): Omit HTML tags; enforce Arabic logical order and BiDi hygiene without raw HTML markup.
- **BiDi Hygiene**: Keep Latin technical identifiers in backticks. Never end sentences with Latin text immediately followed by Arabic punctuation.

### 2. Mobile Engineering Constraints
- Always inspect the repository and verify SDK version before adding packages.
- Distinguish Google Play In-App Updates (native binaries) from Expo Updates (OTA JavaScript/assets).
- Acknowledge Google Play In-App Review quotas (display is never guaranteed).
- Do not perform irreversible actions (deploying, deleting files, purchasing services) without explicit developer confirmation.

### 3. Skill Navigation
- Main orchestrator: `skills/mobile-builder-kit/SKILL.md`
- Clarifying requirements: `skills/grill-me/SKILL.md`
- One-shot build prompt: `skills/app-blueprint/SKILL.md`
- Play updates: `skills/play-in-app-updates/SKILL.md`
- Reviews: `skills/play-in-app-review/SKILL.md`
- QA audit: `skills/mobile-quality-audit/SKILL.md`
- Store launch: `skills/play-launch-checklist/SKILL.md`
- Growth: `skills/mobile-aso-growth/SKILL.md`
