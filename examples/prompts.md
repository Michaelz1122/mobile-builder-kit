# Example prompts

All examples work in Arabic or English. Specify the skill name to force explicit discovery when your agent supports it.

## Start an Android app from an idea

> Use **mobile-builder-kit** and **grill-me**. I want to build a simple Android app with React Native, Expo and Antigravity. Ask one important product question per turn, suggest a default answer, and do not implement until the requirements are confirmed.

## Egyptian Arabic and mixed LTR tokens

> Use **arabic-rtl**. رد عليا بالمصري ومن اليمين للشمال. كل جملة عربي تبدأ بكلام عربي، ولو هتذكر `Google Play Billing` أو `Expo Router` خليها واضحة ومش بتقلب ترتيب الكلام. راجع تنسيق Markdown قبل ما تبعت.

## Design once, build with one master prompt

> Use **app-blueprint**. I have a one-person freelancer invoice app idea. Create an MVP spec and a single implementation master prompt for Antigravity + Expo. No login for v1, local storage, PDF export, no fake payment integrations.

## Google Play update and review

> Use **play-in-app-updates** and **play-in-app-review**. Inspect this Expo project's actual SDK and dependencies, distinguish OTA vs native update options, propose a compatible implementation with test cases and request confirmation before installing native packages.

## Release audit

> Use **mobile-quality-audit** and **play-launch-checklist**. Identify P0 blockers for my next Play Store release, citing file paths and current Google Play documentation. Do not claim a test passed unless you ran it.

## Organic discovery

> Use **mobile-aso-growth**. Prepare an ASO experiment for my Android app using actual Play Console data if available; mark assumptions clearly, and don't fabricate ranking or downloads.
