---
trigger: always_on
description: Improve Arabic and Egyptian Arabic readability and bidirectional text handling where supported.
---

# Arabic RTL and mixed-language output

- When replying in Arabic, start paragraphs and bullet items with Arabic words when natural.
- Keep code, terminal commands, paths, URLs and identifiers in code spans or fenced code blocks.
- Respect the active renderer. **Do not automatically wrap Markdown messages in HTML**: chat/terminal renderers may escape or display tags literally, and HTML blocks can interfere with Markdown parsing.
- In an HTML surface that is known to render HTML, a scoped element with dir="rtl" may be used. Otherwise rely on clear Arabic text and test the actual app/IDE renderer.
- For programmatically generated UI, set the correct layout direction and test mixed Arabic, Latin words, punctuation, digits, dates and navigation on real devices.
- Use directional isolation only where the output format supports it; do not insert invisible Unicode marks blindly into code or filenames.
- Neither this rule nor a skill can guarantee RTL layout in every model or host.
