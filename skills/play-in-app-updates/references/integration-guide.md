# Play in-app updates — decision & QA guide

## Choose the correct technology

| Need | Mechanism | Native binary change? | Can test inside Expo Go? |
| --- | --- | --- | --- |
| Deliver compatible JavaScript/assets fixes | Expo Updates / EAS Update | No | Not representative for production update behavior |
| Prompt to install a Play Store version | Google Play Core In-App Updates | Yes, new Play Store binary is distributed | No |
| Offer update without Play Core integration | Play Store URL / market intent | Yes, through store install | Fallback only |

**Expo managed workflow:** Play Core integration requires a compatible native module and native build, not a JavaScript-only `expo-updates` call. Check the installed Expo SDK and community package maintenance. Do not assume a package's latest major version works on the user's existing SDK.

## Implementation checklist

- [ ] Check current app `versionCode`, `versionName`, release track and target device's Play account.
- [ ] Inspect dependencies; record the exact supported integration route.
- [ ] Define update policy (optional, critical only, throttle frequency, user interruption).
- [ ] Handle `UPDATE_AVAILABLE`, `DEVELOPER_TRIGGERED_UPDATE_IN_PROGRESS`, unsupported update type, cancellation and errors when applicable.
- [ ] Handle flexible download progress and `DOWNLOADED` → user confirmation → complete update.
- [ ] Handle app resume and process death.
- [ ] Ensure update UX complies with Play Core guidance, no surprise repeated prompts.
- [ ] Test: no update, update available, app canceled, interrupted download, immediate update, flexible completion, bad network.
- [ ] State what could not be tested without an eligible Play Store distribution.

## Acceptance criteria

- The update flow is triggered only when Play Core reports a suitable update.
- Ordinary updates don't unnecessarily block usage.
- Resume/complete-update paths work as appropriate.
- A user who declines an optional update can keep using the app.
- Errors and unsupported environments fail gracefully.
- No test is recorded as passing unless run on a supported build.

## Canonical references

- [Android — In-app updates](https://developer.android.com/guide/playcore/in-app-updates)
- [Expo — Expo Updates overview](https://docs.expo.dev/eas-update/introduction/)
- [Expo — How it works](https://docs.expo.dev/eas-update/how-it-works/)

Review these URLs before selecting a versioned implementation.
