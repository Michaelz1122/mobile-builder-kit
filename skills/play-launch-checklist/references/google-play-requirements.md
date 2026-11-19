# Google Play release gate

## Required checks

- [ ] Package name, version code, signing, release build integrity
- [ ] App bundle AAB and Play App Signing setup
- [ ] Current target SDK policy checked for release date and device category
- [ ] App content: privacy policy, Data Safety, content rating, audience, ads declaration
- [ ] Account creation/type and applicable production access/testing requirements
- [ ] Screenshots, icon, descriptions, localization and screenshots tested on small displays
- [ ] Native modules tested in the same track/build type as customers
- [ ] Crash and ANR monitoring; release stop/rollback plan
- [ ] In-app purchases: entitlement, verification, acknowledgement and restoration
- [ ] AdMob: test ads before release, consent/privacy requirements and non-disruptive placements
- [ ] Security: credentials, Supabase RLS if relevant, user data deletion where applicable
- [ ] Version upgrades and database migrations preserve user data

## Android / Expo tips

- APK is useful for direct testing; Play distribution generally uses AAB.
- `expo-updates` is OTA JavaScript/assets delivery, not a replacement for native Play Store releases.
- Certain native dependencies require development builds, not Expo Go.
- Use `eas build` and release workflows only after checking the project's current configuration.

## Official references

- [Google Play personal developer testing requirements](https://support.google.com/googleplay/android-developer/answer/14151465)
- [Google Play Developer Program Policy](https://play.google.com/about/developer-content-policy/)
- [Google Play Billing](https://developer.android.com/google/play/billing)
- [Google Play In-App Updates](https://developer.android.com/guide/playcore/in-app-updates)
- [Google Play In-App Reviews](https://developer.android.com/guide/playcore/in-app-review)
- [Expo Build](https://docs.expo.dev/build/introduction/)

As of initial release (2026-11-19), Google documents the 12-testers/14-days rule for eligible newly created personal accounts. Always reconfirm before advising a specific user.
