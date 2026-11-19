---
name: play-in-app-review
description: Adds or reviews Google Play in-app rating and review requests, including responsible trigger timing, store quotas and Expo StoreReview usage. Use when a mobile app needs a non-intrusive in-app review prompt.
license: MIT
---

# Google Play In-App Review

## Rules before code

1. Ask for the app's genuinely positive **milestone** (e.g., a task completed successfully, not just first launch). Do not show prompts during onboarding, payment, errors, or urgent flows.
2. Never ask 'Do you like the app?' or condition the rating flow on sentiment. Do not offer rewards for ratings or customize the Play review dialog.
3. Respect Google Play's **undisclosed time-based quota**; `requestReview()` can complete without a visible dialog. Do not report that a rating was submitted.
4. A direct `Rate app` settings button should use the store listing URL, not trigger a review dialog that might be quota-suppressed.
5. For Expo, verify the installed SDK and use `npx expo install expo-store-review` where appropriate. Check `StoreReview.hasAction()` before `StoreReview.requestReview()`.
6. Use local session/attempt throttling **as a UX safeguard**; don't pretend you can discover Google's quota or whether the user reviewed.
7. Test eligibility and no-dialog branches. Record whether test conditions represent a Play-distributed build.

## Useful example

Read [Expo TypeScript example](examples/expo-review.ts) for a minimal function designed to be called after a completed user action, **not directly from a button**.

## Official documentation

- [Google Play In-App Reviews](https://developer.android.com/guide/playcore/in-app-review)
- [Expo StoreReview](https://docs.expo.dev/versions/latest/sdk/storereview/)
