# Mobile Builder Kit — Claude Code instructions

Modular Agent Skills for Android app building (especially React Native and Expo).

## Answer and UX rules

- Use clear Egyptian Arabic when requested and keep technical terms readable.
- Never force raw HTML wrappers around Markdown or terminal answers; use renderer-aware bidi text.
- Review Arabic app UI directionality, navigation, mixed-script labels and inputs on real devices.

## Engineering workflow

- Inspect project structure, SDK versions, package.json and installed dependencies before implementing.
- Separate Play binary updates from Expo OTA updates; review prompts are quota-controlled and may not display.
- Don't claim native code works just because it compiles or generated code exists.
- Require approval for destructive actions, publishing, paid services and security-sensitive changes.
- Prefer the installed .claude/skills (project) or ~/.claude/skills (user) directory.

## Skill routing

- app-discovery — original Grill Me-style product interview.
- app-blueprint — MVP requirements and a single initial build prompt.
- arabic-rtl — Arabic chat hygiene and React Native RTL testing.
- play-in-app-updates / play-in-app-review — Play feature planning and verification.
- mobile-quality-audit / play-launch-checklist / mobile-aso-growth — QA, release, growth.
