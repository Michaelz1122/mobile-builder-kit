---
name: play-launch-checklist
description: Prepares an Android app for Google Play, including signing, AAB builds, Play Console testing, privacy disclosures, release tracks, in-app purchases and rollout checks. Use before submitting a new app or update.
license: MIT
---

# Play Launch Checklist

## Release workflow

1. Determine developer account type and creation date, package name, target API, app content, countries, billing and permissions.
2. Build a signed Android App Bundle (AAB) suitable for the actual release workflow; verify versionCode increments, package name and signing identity.
3. Prepare app icon, screenshots, feature graphic if required, title, short/full description, support contact, privacy policy and data safety declarations.
4. Validate consent, ads, content declarations, age targeting, permissions, account deletion if applicable, and billing compliance against *current* official policies.
5. Choose internal/closed/open testing based on actual account requirements. For **qualifying new personal developer accounts created after 2023-11-13**, Google documents **12 testers opted in continuously for 14 days** before applying for production access. Do **not** state this applies to every account.
6. Test install/update from eligible tracks, important user journeys, crash logs, billing, RTL, network failures, review and update flows.
7. Prepare staged rollout and rollback/incident response. Publish only with explicit approval and proper account access.

## Do not claim

- That AAB upload proves the app is published.
- That internal testing alone satisfies closed testing requirements.
- That a customer-facing transaction is secure without purchase verification.
- That any app is automatically policy-compliant or guaranteed approval.

Read the [launch checklist](references/google-play-requirements.md) and confirm volatile facts from live official docs.
