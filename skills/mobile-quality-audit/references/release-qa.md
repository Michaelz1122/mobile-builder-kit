# Mobile QA checklist

## P0 blockers

- [ ] Crash or unusable first-run experience
- [ ] Lost or corrupted user data
- [ ] Anyone can access someone else's records
- [ ] Store purchases incorrectly unlock features without verified state
- [ ] Exposed real secrets or privileged API keys in client bundle
- [ ] Dangerous privacy policy mismatch or misleading disclosure

## P1 functional issues

- [ ] Android back navigation works on deep screens/modals
- [ ] Bad network and offline recover gracefully
- [ ] Notifications respect permissions and user opt-out
- [ ] Purchase cancellation/restoration/acknowledgement behave as designed
- [ ] PDF/file permission and share destinations work on target Android versions
- [ ] State persistence and data migration handle app restart/update

## P2 usability/performance

- [ ] RTL and English mixed strings are displayed correctly
- [ ] Screen-reader labels, touch targets, dynamic font scaling
- [ ] Image memory, large list rendering, slow startup, battery usage
- [ ] Error messages explain recovery without exposing internal stack traces

## P3 polish

- [ ] Consistent spacing, skeletons, transitions, typography
- [ ] Empty states and onboarding copy
- [ ] Correct store metadata and in-app labels

## Audit report template

| Severity | Evidence | Impact | Fix | How to verify |
| --- | --- | --- | --- | --- |
| P0 | `path:line` or steps | What breaks | Exact change | Specific test |

Include environment (OS, Expo SDK, native architecture, build type, test account) and list untested areas. Never treat screenshots as proof of backend security or payment verification.
