---
name: app-blueprint
description: Converts an Android app idea into an MVP product specification, acceptance criteria, data plan, and one AI coding master prompt. Use for vibe coding, Google Stitch-to-Antigravity workflows, or building a React Native Expo app with minimal manual screen-by-screen coding.
license: MIT
---

# App Blueprint — idea to one master prompt

## The outcome

A developer-ready **PRD + single initial build prompt + test plan**, not a promise of production-ready software from one AI generation.

## Steps

1. Inspect the existing repository and constraints. If the idea is ambiguous, route to `grill-me` first.
2. Define the target user, key problem, success event, and the smallest useful version. Explicitly separate MVP from future features.
3. Specify each core flow, navigation, required screens, data storage, failure states, Arabic/English support, offline behavior and permissions.
4. Choose the least complex viable stack. For Expo, distinguish Expo Go-safe libraries from dependencies requiring development builds/prebuild. Avoid guessing SDK/package versions.
5. If using Stitch, create one coherent design brief for the full app, inspect results, and carry design tokens and assets into the coding prompt. Explain where Stitch output may need manual adaptation.
6. Fill [master build prompt template](templates/master-prompt.md). Allow an AI coding agent to create an initial app in a single pass, but never skip testing or pretend payment, auth, security or platform permissions are configured.
7. Define acceptance criteria, must-run commands, device test cases and release blockers. Keep prompts version-aware and project-specific.

## Guardrails

- Avoid fake dashboards, seeded user metrics presented as real, placeholder data shown as production, hardcoded payment success, or unsupported claims of compliance.
- If the user asks for a single prompt, do not require screen-by-screen approvals. Keep a short post-generation testing/repair loop.
- Ask before creating accounts, incurring costs, deleting files, changing secrets or releasing to Google Play.
- Prefer a working small app over a visually ambitious but untestable one.

See the reusable [master prompt](templates/master-prompt.md).
