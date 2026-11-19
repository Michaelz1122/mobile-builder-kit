# Mobile Builder Kit — Codex / AGENTS.md

This project uses reusable Agent Skills for AI-assisted Android apps (primarily React Native + Expo).

## Arabic and RTL

- Respond in the requested language; Egyptian Arabic is appropriate when requested.
- Keep Markdown readable and preserve LTR code, commands, paths and URLs.
- Do **not** force raw `<div dir="rtl">` around chat responses. Only use HTML direction attributes when the renderer is confirmed to support them.
- RTL inside an app is a code-and-testing task, not just a chat-formatting instruction. Verify screens on actual devices.

## Development quality gates

- Inspect package.json, Expo SDK/RN versions, build method, and existing code before changing dependencies.
- Differentiate Expo OTA JS updates and Google Play in-app binary updates.
- Do not promise that Play in-app review dialogs will appear; Google controls quotas.
- Avoid invented API contracts, fictional analytics or mocked success in production.
- Do not publish, pay, delete user data, or overwrite secrets without explicit authorization.

## Skills

Use installed skills as needed:
- app-discovery: one-question-at-a-time requirements interview (our Grill Me workflow).
- app-blueprint: MVP specification and initial master build prompt.
- arabic-rtl: language and app RTL audit.
- play-in-app-updates, play-in-app-review: Play-native engagement features.
- mobile-quality-audit, play-launch-checklist, mobile-aso-growth: release quality and growth.

For Codex CLI and IDE, use /skills or mention a skill with $skill-name.
