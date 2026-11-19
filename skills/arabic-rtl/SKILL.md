---
name: arabic-rtl
description: Improves Arabic and Egyptian Arabic readability, mixed Arabic/English bidirectional text, and React Native/Expo RTL layouts. Use for Arabic answers, chat presentation issues and Arabic mobile app UI review; renderer support must be verified.
license: MIT
---

# Arabic RTL — renderer-aware chat and mobile UI

## 1. Arabic replies

- Reply in Egyptian Arabic when that is the user's language or stated preference. Keep prose natural.
- Prefer Arabic-first sentences, especially for list items and headings with Latin technical terms.
- Wrap paths, code, commands, identifiers and URLs in backticks rather than injecting direction marks into source code.
- **Do not wrap every response in raw HTML.** Markdown hosts, terminals and IDE chat clients may show tags literally or change how fenced code and lists render.
- If the target is known to support HTML, `<div dir="rtl">` can be an opt-in wrapper for that particular renderer. Never claim this works on every model or chat interface.
- Handle mixed Arabic/English punctuation without blanket bans on sentences ending in English. Prefer correct isolation when supported by the actual output format.
- When a display defect is reported, inspect the real renderer, test a small sample and choose a renderer-specific fix.

## 2. React Native / Expo app layout

1. Inspect the app's localization, React Native I18nManager configuration and the installed Expo/RN versions before changing direction settings.
2. Apply `writingDirection: "rtl"` and `textAlign: "right"` where Arabic inputs/text require them, based on the specific component. Do not globally flip every flex row or override all user-entered text.
3. Mirror only directional icons and semantics; do not mirror logos, video playback, charts or every numeric token.
4. Use LTR isolation for URLs, email, phone numbers and code-like tokens as appropriate; localized currencies and dates must follow product requirements.
5. Inspect text cursor, placeholders, truncation, fonts, modals, navigators and Android back behavior.
6. Test both Arabic RTL and English LTR on a real Android device. Check dynamically switched language and app restart if the framework requires it.

## Acceptance

No clipped or reversed labels, readable mixed-script text, correctly directional navigation, and working input cursor/selection. Document test environment and anything not verified.

See [RTL test checklist](references/rtl-layout-checklist.md).
