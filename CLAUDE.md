# CLAUDE.md — Claude Code & Anthropic Models Configuration

## Project Overview
**Mobile Builder Kit** is an open-source Agent Skills and Rules pack for developers building Android mobile applications with AI assistants (React Native + Expo). It provides 9 specialized skills and persistent rules designed to work seamlessly across **Claude (Anthropic)**, **Codex / ChatGPT (OpenAI)**, and **Gemini / Antigravity (Google)**.

---

## Guidelines for Claude & Claude Code

### 1. Arabic Language & RTL Protocol
- **Terminal / CLI mode (`claude` CLI)**:
  - Do NOT wrap responses in raw HTML tags like `<div dir="rtl">` because terminal emulators render HTML literally.
  - Start paragraphs and list items with Arabic words to preserve natural logical reading order.
  - Maintain strict BiDi punctuation hygiene: never end a sentence with an English token followed directly by punctuation.
- **Web / Desktop mode (Claude Web / GUI)**:
  - Wrap full Arabic responses with `<div dir="rtl"> ... </div>` to enforce right-to-left alignment.

### 2. Mobile Development Principles (React Native + Expo)
- **Inspect First**: Always inspect `package.json`, Expo SDK version, and existing architecture before proposing dependencies or native code.
- **Expo Updates vs Google Play Updates**: Never confuse Expo EAS OTA updates (JavaScript / asset bundles) with Google Play In-App Updates (native binaries).
- **Google Play In-App Reviews**: Google Play enforces undisclosed quotas; never promise a review dialog will definitely appear.
- **No Hallucinated Packages**: Verify that libraries are compatible with the specific Expo SDK and New Architecture (if enabled).

### 3. Agent Skills & Rules Layout
- Skills live in `skills/<skill-name>/SKILL.md` following the [Agent Skills specification](https://agentskills.io/specification).
- When a user asks for an end-to-end mobile flow, load `skills/mobile-builder-kit/SKILL.md`.
- When requirements are vague, load `skills/grill-me/SKILL.md` to conduct a focused interview.
- When generating prompts, refer to `skills/app-blueprint/templates/master-prompt.md`.

---

## Validation & Test Commands

```bash
# Validate all skills frontmatter and links
python scripts/validate_skills.py

# Run test suite
python -m unittest discover -s tests -v

# Test skill installer (dry-run)
python scripts/install.py --target /path/to/project --all --dry-run
```
