---
name: mobile-quality-audit
description: Audits an Android or React Native Expo app for runtime errors, data integrity, security, privacy, RTL, accessibility, performance, offline handling and release readiness. Use before publishing or after an AI-generated app build.
license: MIT
---

# Mobile Quality Audit — inspect, test, prioritize

## Evidence first

1. Inventory project structure, SDK and native dependencies. Read actual code, routes, permissions, database rules and test config. Never invent code paths, events or successful tests.
2. Map core user journeys and revenue/privacy-sensitive operations.
3. Check data validation, edge cases, offline handling, persistence, loading/error/empty states and crash risks.
4. Check sensitive data, permissions, API key placement, secure secrets, authentication and authorization, request rate limiting and storage rules (e.g. Supabase RLS when used).
5. Check accessibility, Android back button, font scaling, RTL/LTR, navigation, launch responsiveness and low-end performance.
6. Run locally available lint, typecheck and tests only with safe permissions; specify which commands were executed. Do not claim a test passed because it exists.
7. Provide a **P0–P3 report**, each item with evidence (file and line or reproducible steps), impact, concrete fix, and verification path. Do not modify code unless asked.

See [QA checklist](references/release-qa.md).
