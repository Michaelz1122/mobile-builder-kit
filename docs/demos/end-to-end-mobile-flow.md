# Practical Demo: End-to-End AI Mobile App Workflow

This guide demonstrates a complete, beginner-friendly journey to plan, build, audit, and prepare an Android app using the **Mobile Builder Kit** Agent Skills with your preferred AI coding agent (Claude Code, Antigravity, Codex, or Cursor).

---

## The 5-Stage Journey

```text
[ 1. App Idea ]
       ↓
[ 2. Discovery Interview ]      → Skill: app-discovery
       ↓
[ 3. MVP Blueprint & Prompt ]   → Skill: app-blueprint
       ↓
[ 4. Automated Code Audit ]     → Skill: mobile-quality-audit
       ↓
[ 5. Google Play Launch Check ] → Skill: play-launch-checklist
```

---

## Stage 1: Requirements Discovery (`app-discovery`)

Instead of letting an AI assume or hallucinate features, use `app-discovery` to lock in requirements one decision at a time.

### Invocation Prompt
```text
Use app-discovery. I want to build an Android habit tracker app for Arabic speakers called "عاداتي" (Aadaty). Interview me one question at a time to determine scope.
```

### Expected Output
The agent asks focused, single questions:
1. Target platform: Android only or cross-platform?
2. Data storage: Local-only (SQLite/AsyncStorage) or synced backend (Supabase/Firebase)?
3. Monetization: Free, Ads, or In-App Purchases?
4. RTL requirements: Full Arabic UI, English UI, or dual-language?

---

## Stage 2: MVP Architecture & Master Prompt (`app-blueprint`)

Once the requirements are agreed upon, convert them into an architectural specification and a single master build prompt.

### Invocation Prompt
```text
Use app-blueprint. Convert our discovery notes for "Aadaty" into an MVP product specification and generate one unified master prompt.
```

### Expected Output
The agent outputs:
- **Core Screen Flows**: Onboarding → Today's Habits → Habit Creation → Completion Analytics.
- **Data Model**: `Habit` (id, title, frequency, reminderTime, isArchived), `HabitLog` (id, habitId, date, completed).
- **Master Prompt**: A comprehensive, self-contained prompt to execute the build in React Native + Expo without endless back-and-forth approval loops.

---

## Stage 3: Building the App Pass

Give the generated Master Prompt to your AI agent (in Claude Code, Antigravity, Cursor, or Codex):

```text
You are an experienced mobile engineer working in this repository.
Build the "Aadaty" MVP based on our blueprint using Expo SDK 52 with React Native:
- Initialize SQLite local storage.
- Implement full Arabic RTL navigation and form inputs.
- Add notification scheduling for daily habit reminders.
- Run typecheck and linting on finished files.
```

---

## Stage 4: Code & Quality Audit (`mobile-quality-audit`)

Before running builds or publishing, audit the code for security, accessibility, and crash risks.

### Invocation Prompt
```text
Use mobile-quality-audit. Audit our new habit tracker codebase for security, memory leaks, offline behavior, and RTL accessibility.
```

### Expected Output
The agent delivers an audit report categorized by priority:
- **P0 Blockers**: Unhandled SQLite migration errors, missing permissions for Android 13+ notifications.
- **P1 Issues**: Placeholder text misaligned in Arabic inputs, unhandled empty habit state.
- **P2 Improvements**: Missing haptic feedback on completion, non-indexed query on `habit_logs`.

---

## Stage 5: Google Play Release Preparation (`play-launch-checklist`)

Prepare the release assets, policy forms, and Android App Bundle (`.aab`).

### Invocation Prompt
```text
Use play-launch-checklist. Walk me through Google Play Console requirements, targetSdk guidelines, app signing, and privacy declarations for our app.
```

### Expected Output
A release checklist:
- [ ] Configure `app.json` with unique `package: "com.michaels.aadaty"` and `versionCode`.
- [ ] Target SDK updated to latest Google Play requirement (API 35+).
- [ ] Data safety form: Declare local-only storage (no user data collected or shared).
- [ ] Build release bundle: `eas build --platform android --profile release`.
- [ ] Setup Google Play Console Internal Testing track for initial closed verification.

---

## Realism Check

> **Important Reminder:** Agent Skills assist and accelerate planning, auditing, and code generation. They do **not** replace:
> 1. Testing on real physical Android hardware.
> 2. Enrolling in the Google Play Console developer program ($25 one-time fee).
> 3. Google Play's 14-day closed testing requirement for personal developer accounts.
