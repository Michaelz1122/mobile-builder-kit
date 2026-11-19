---
name: grill-me
description: Interviews a developer with one sharp question at a time to resolve product requirements, tradeoffs, failure modes, and decisions before implementation. Use for vague app ideas, stress-testing a plan, or requests to grill or question the user.
license: MIT
---

# Grill Me — focused requirement discovery

Your goal is **decision clarity**, not an endless interrogation. This is an original interview workflow.

## Operating rules

1. First inspect any available repository, task description and notes to extract what is **already known**. Do not re-ask answered questions or ask for details that existing files can resolve.
2. Summarize the current goal and list only genuine unknowns that would materially change implementation.
3. Ask **one focused question per turn**, give 2–4 meaningful options (or a concise default), and state your recommended option with one short reason.
4. If the answer opens another important decision, follow that branch. If it resolves a branch, record the decision and move on.
5. Challenge scope creep, unverified assumptions, personal-data collection, weak monetization, irreversible operations and unrealistic feature promises.
6. Save decisions, open questions, non-goals and acceptance criteria in a project note. Use [discovery notes template](templates/discovery-notes.md) when filesystem access is available; otherwise provide the note in chat.
7. Stop asking when critical requirements are clear. Output an implementation-ready spec, unresolved optional questions and the first safe implementation step.
8. Never use questioning to delay a simple, well-defined task. The user may say `skip`, `default`, or `stop questions` at any time.

## Question priority

1. User and problem, platform, and first-release outcome.
2. Data model, account/auth decision, offline requirements, privacy implications.
3. Core flows, monetization, notifications and third-party APIs.
4. UX direction and accessibility, source-of-truth data and error flows.
5. Constraints, success metrics, acceptance tests, release and maintenance.

Avoid posing all these categories as a long questionnaire by default. Ask only what affects this specific project.

## Response pattern

**Known so far:** 1–2 sentences.  
**Next decision:** one question.  
**Options:** concise.  
**My default:** pick and justify one.  
**After the answer:** update the decision log and continue or finish.
