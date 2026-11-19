---
name: play-in-app-updates
description: Plans and reviews native Google Play in-app updates for Android, including flexible and immediate flows, Play-distributed testing, and Expo React Native compatibility. Use when an app should prompt users to update after a new Play Store release.
license: MIT
---

# Google Play In-App Updates

## First avoid the common confusion

- **Play Core native in-app updates** deliver new **Play Store binaries** to users through Google's flexible/immediate UX.
- **Expo Updates (OTA)** distributes compatible JS/assets changes and does **not** install native Android binary changes.
- A generic "new version available" dialog that opens Play Store is a third option. It is not the Play Core in-app update flow.

## Integration workflow

1. Inspect stack, Expo SDK/RN versions, package versions, native configuration, build pipeline, and distribution method.
2. Confirm the app is Google Play-distributed and a higher version is available on an eligible testing/release track. Don't promise native update prompts on a sideloaded APK or inside Expo Go.
3. Choose **flexible** for normal non-breaking updates; choose **immediate** only if continuing without an update is unacceptable and justified.
4. For native Android, follow current official Play Core docs. For Expo/React Native, **verify the exact third-party/native module supports the installed SDK and new architecture** before recommending it. Custom native integration or a store redirect may be necessary.
5. Implement lifecycle handling, update eligibility checks, error/cancel handling, resumed flexible downloads, install completion, and graceful fallback. Do not block all users by default.
6. Test with an older Play-distributed build, a newer eligible Play build and a real test account/device; validate flexible/immediate and no-update branches.
7. Report actual test status and remaining Play-track dependency. Do not claim success based on compilation alone.

Read [integration guide](references/integration-guide.md) for acceptance criteria and sources.
