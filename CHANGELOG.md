# Changelog

## 0.2.0 — 2026-11-19

- **GitHub SEO & Discoverability**: Naturally integrated search keywords for Android Agent Skills, Claude Code, Codex, Antigravity, Cursor, and Expo RTL.
- **Conversion-Optimized READMEs**: Redesigned English (`README.md`) and Egyptian Arabic (`README.ar.md`) documentation with clear above-the-fold value proposition, agent support matrix, creator portfolio section with UTM attribution, and first-skill invocation guides.
- **Agent Skills CLI Support**: Documented and verified one-liner installation using `npx skills add Michaelz1122/mobile-builder-kit`.
- **Practical Demonstrations**: Added three comprehensive, production-ready guides in `docs/demos/`:
  - `arabic-rtl-demo.md`: Problematic vs production-ready Arabic RTL React Native implementations and device test checklist.
  - `play-in-app-review-demo.md`: Expo `expo-store-review` integration, milestone triggers, and quota safeguards.
  - `end-to-end-mobile-flow.md`: End-to-end walkthrough from idea to discovery, blueprint, QA audit, and Google Play launch.
- **Distribution Guide**: Overhauled `PUBLISHING.md` with GitHub Topics, release procedures, and `skills.sh` discovery requirements.

## 0.1.1 — 2026-11-19

- Multi-model and cross-agent support for Claude Code (`CLAUDE.md`), OpenAI Codex (`AGENTS.md`), Cursor (`.cursorrules`), and Google Antigravity (`GEMINI.md`).
- Surface-aware RTL formatting (Webview `<div dir="rtl">` vs Terminal CLI plain text).
- Added `app-discovery` skill as the recommended alias to prevent slash-command collision with Antigravity's native `/grill-me`.
- Persistent rules installer and multi-agent test suite.

## 0.1.0 — 2026-11-19

- Initial Agent Skills pack with RTL, Grill Me, AI app specification, Google Play updates/reviews, quality audit, Play release checklist and ASO/growth.
- Arabic and English README files, installation utility, and automated validation.
- No bundled Android APK or auto-installing native library. Workflows must be applied to an actual project and tested.
