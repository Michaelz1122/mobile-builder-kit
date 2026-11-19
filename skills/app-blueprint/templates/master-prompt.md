# One-shot Android app build — master prompt template

Fill **all bracketed values**. This template is intended to be customized, not pasted unchanged.

```text
You are an experienced mobile engineer working in my existing repository.

PROJECT
- App name: [NAME]
- Users and their problem: [AUDIENCE + PROBLEM]
- Platform: Android [OTHER TARGETS IF ACTUALLY NEEDED]
- Stack: [REACT NATIVE/EXPO SDK FROM REPOSITORY]
- MVP scope: [SHORT BULLET LIST]
- Out of scope: [SHORT BULLET LIST]
- Design source: [STITCH EXPORT/IMAGES/LINKS OR TEXT DESIGN TOKENS]
- Language: [AR/EN/BOTH] and RTL behavior: [EXPLICIT REQUIREMENTS]
- Data storage: [LOCAL/REMOTE; OWNERSHIP; SYNC/OFFLINE]
- Monetization for MVP: [NONE / ADMOB / STORE-BILLING; ONLY IF CONFIGURED]

HOW TO WORK
1. Inspect the repository, package versions, existing conventions and available test scripts first.
2. Create or update the complete MVP in one coherent implementation pass instead of requiring screen-by-screen user approvals.
3. Use actual implementations for the core data model, navigation and storage; do not fake login, billing, analytics or backend data.
4. Preserve existing work and secrets. No destructive migrations, paid services, publishing or remote writes without approval.
5. Only introduce libraries compatible with the project's SDK, native architecture and build setup. Document any development-build requirement.
6. Implement loading, empty, offline and error states. Validate inputs and calculations.
7. For Arabic, test mixed Arabic and Latin text, directional layouts and data display.
8. Run available lint/typecheck/unit tests and describe which tests actually ran.
9. Finish with (A) implemented features; (B) changed files; (C) commands to reproduce;
   (D) known limitations; (E) manual Android test checklist; (F) next fixes in priority order.

ACCEPTANCE CRITERIA
- [CORE FLOW 1 AND EXPECTED RESULT]
- [CORE FLOW 2 AND EXPECTED RESULT]
- [DATA PERSISTENCE / PDF / SHARE IF APPLICABLE]
- [OFFLINE, PRIVACY, RTL, ACCESSIBILITY]
- [ERROR CASES]

Do not claim that Play Store deployment, In-App Billing, or Google Play in-app updates
are tested unless they were validated in the appropriate distributed build.
```
