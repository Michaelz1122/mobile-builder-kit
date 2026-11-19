---
name: mobile-builder-kit
description: Coordinates an AI-assisted Android app project from idea to Google Play release. Use when a beginner wants an end-to-end mobile build workflow, appropriate sibling skills, testing, monetization, or launch planning.
license: MIT
---

# Mobile Builder Kit — workflow orchestrator

Use this as a **router and quality gate**; do not duplicate every child skill's details here. If the following sibling skills are installed, open and follow the ones that match the task:

| Situation | Skill |
| --- | --- |
| Arabic response, Arabic UI, mixed bidirectional text | `arabic-rtl` |
| Vague request, disputed tradeoffs, unclear product requirements | `grill-me` |
| Project idea to one master implementation prompt | `app-blueprint` |
| Play-distributed native update prompt | `play-in-app-updates` |
| In-app rating / review flow | `play-in-app-review` |
| Testing, privacy, security, performance | `mobile-quality-audit` |
| AAB, Play Console, testing, release | `play-launch-checklist` |
| ASO, acquisition, measurement | `mobile-aso-growth` |

## Default journey

1. Identify target platforms, stack, users, core problem, constraints, and what already exists. Inspect the repository before suggesting dependencies.
2. Scope **one realistic MVP**. Avoid inventing features or adding accounts/backends the user does not need.
3. Write an implementation-ready specification and acceptance tests. If appropriate, generate **one master prompt** for the initial app, then plan verification and targeted repairs.
4. Verify the generated implementation: data integrity, offline behavior, navigation, Arabic/LTR, accessibility, errors, and security.
5. Add store-specific features only with confirmed version support and genuine user value. Distinguish EAS/Expo OTA from Play Core binary updates.
6. Prepare privacy disclosures, app signing, release build, Play testing, store listing, billing and marketing.
7. Stop at each irreversible action (deleting data, adding paid services, publishing, editing someone else's repo) and request explicit authorization.

## Required output style

- Use clear steps. Show exactly what you inspected and what remains untested.
- Mark unsupported features as `Not configured`, `Requires native build`, or `Needs Play-distributed test` rather than claiming completion.
- If Arabic is requested, follow `arabic-rtl` whenever available.
- Check official documentation for time-sensitive package and store policy facts; no hardcoded universal testing, billing or target SDK claims.

This is an Agent Skill, **not executable Android SDK code** by itself.
