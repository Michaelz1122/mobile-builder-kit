---
name: arabic-rtl
description: Improves the readability and right-to-left direction of Arabic AI responses and Arabic mobile interfaces. Use for Arabic or Egyptian Arabic chat, mixed Arabic-English technical terms, UI RTL debugging, or bidirectional layout audits.
license: MIT
---

# Arabic RTL — language and interface quality

## First distinguish the surface

- **Chat/Markdown responses:** write correctly ordered Arabic and isolate mixed English spans. The model controls generated text, not the host app's layout engine. Do not promise universal RTL for all models, clients or renderers.
- **Web UI:** apply HTML/CSS directionality and test nested LTR content.
- **React Native / Expo UI:** handle text writing direction, alignment, flex layout and localized navigation explicitly; test on device. Do not force global RTL in an app that must support LTR unless the locale/design requires it.

## Arabic response protocol

1. When the user writes Arabic, respond in Arabic unless they request another language. Prefer natural Egyptian Arabic when the user uses it.
2. Begin each paragraph and list item with **Arabic text**, not an English package name or a number, where practical. This avoids bidirectional surprises in simple clients.
3. Keep Latin identifiers, code, URLs, shell commands and file paths verbatim inside backticks. Don't translate API names.
4. Avoid unnecessary punctuation, diacritics, mixed-direction decorative arrows and manually inserted text direction controls. If a rendering engine demonstrably needs bidirectional isolation, wrap only mixed tokens with Unicode isolates (FSI U+2068 / PDI U+2069) or an appropriate platform component; document and test that choice.
5. Preserve logical reading order in steps and Markdown tables. For severe Markdown misrendering, prefer short paragraphs, a simple list, or an explicit RTL HTML container **only if that output surface supports it**.
6. Before responding, mentally test a line with Arabic + `Expo Router` + `(SDK 57)` + `2026/11/19` + an email address. Do not garble numbers, paths or punctuation.
7. Never claim to have changed the user's app/chat CSS, OS language, or model settings just by applying this skill.

## Mobile UI protocol

1. Detect the stack and locale model. For React Native, inspect `I18nManager`, app restart behavior, `Text` writing direction and actual layout styles before modifying them.
2. Apply `writingDirection: 'rtl'` and appropriate `textAlign` where supported by the native component; handle `flexDirection: 'row-reverse'` only for **directional** rows (not charts or media).
3. Mirror directional UI icons (back/forward) where appropriate, not universal symbols (play, search, logos).
4. Keep phone numbers, code/OTP, email, URLs, currency and Latin app identifiers LTR as semantically appropriate.
5. Check forms (cursor and placeholder), RTL navigation, list alignment, numbers, accessibility reading order, modal dialogs and mixed-language PDF/export content.
6. Supply a screenshot/device test checklist instead of declaring RTL correct based on source inspection alone.

See [RTL test checklist](references/rtl-layout-checklist.md).
