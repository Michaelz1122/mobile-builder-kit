# Mobile Builder Kit

**An open-source Agent Skills pack for people building Android apps with AI.**  
Built with a React Native + Expo workflow in mind, but most skills are framework-agnostic.

[العربية](README.ar.md) · [Agent Skills specification](https://agentskills.io/specification) · [Antigravity Skills documentation](https://antigravity.google/docs/skills)

> **What it is:** reusable AI-agent instructions packaged as `SKILL.md` folders.  
> **What it is not:** an Android APK, a Play Store application, an automatic plugin, or a guarantee that every AI model will obey its instructions.

## Skills included

| Skill | When to use |
| --- | --- |
| `mobile-builder-kit` | Start or coordinate a complete AI-assisted Android app workflow. |
| `arabic-rtl` | Produce readable Arabic/English mixed responses and audit app UI directionality. |
| `grill-me` | Interview the developer about uncertain requirements, one decision at a time. |
| `app-blueprint` | Turn a rough app idea into an MVP specification and a single master build prompt. |
| `play-in-app-updates` | Plan Google Play native in-app updates; distinguish these from Expo OTA updates. |
| `play-in-app-review` | Add compliant, milestone-based Google Play in-app review prompts. |
| `mobile-quality-audit` | Audit mobile code, security, user data, accessibility, testing and performance. |
| `play-launch-checklist` | Prepare Android releases, Play Console, billing, privacy, testing and rollout. |
| `mobile-aso-growth` | Plan App Store Optimization, analytics and small-budget acquisition tests. |

### Always-On Rules
In addition to on-demand skills, the kit includes persistent rules in `rules/` (`rules/arabic-rtl.md` and `rules/AGENTS.md`). While skills are activated contextually, rules placed in `.agents/rules/` or project root `AGENTS.md` enforce RTL message wrapping (`<div dir="rtl">`) and punctuation hygiene unconditionally on every response.

Each skill can be installed **individually**. The umbrella `mobile-builder-kit` skill points to the others, but agent support for discovering sibling skills varies; install all skills for the broadest coverage.

## Install in Google Antigravity

Antigravity looks for project skills in `<project>/.agents/skills/<skill-name>/SKILL.md` and global skills under `~/.gemini/config/skills/<skill-name>/SKILL.md` (see its current documentation).

**Option A — after cloning or downloading this repository:**

```bash
python scripts/install.py --target /path/to/your-android-project --all
```

The command copies every folder from `skills/` into `/path/to/your-android-project/.agents/skills/`. It will **not overwrite existing skills by default**. Use `--force` only after reviewing changes.

**Option B — copy manually:**

```text
my-app/
  .agents/
    skills/
      arabic-rtl/SKILL.md
      grill-me/SKILL.md
      app-blueprint/SKILL.md
      ...
```

**Global installation:** pass `--global` to copy into your user-level Antigravity skills directory. On Windows, the installer uses your home directory too.

**Install selected skills:**

```bash
python scripts/install.py --target /path/to/your-android-project --skills arabic-rtl,grill-me,play-in-app-review
```

Antigravity should discover applicable skills automatically; you can explicitly ask the agent to use one by name. Other tools supporting the [Agent Skills standard](https://agentskills.io/specification) may use different installation directories.

## Example prompts

```text
Use grill-me to question me about my app idea until we have a buildable specification.
```

```text
Use arabic-rtl. Reply in Egyptian Arabic with correct RTL and readable English terms.
```

```text
Use app-blueprint. Turn this app idea into an MVP and one Antigravity master prompt.
```

```text
Use play-in-app-updates and play-in-app-review. Inspect my existing Expo app, check current
SDK compatibility, propose implementation, and only edit the project after my approval.
```

```text
Use mobile-quality-audit and play-launch-checklist. Identify release blockers and provide
P0/P1/P2 fixes with evidence. Do not claim a feature is implemented without testing it.
```

More examples in [examples/prompts.md](examples/prompts.md).

## Important limitations

1. **RTL is best effort:** a skill can direct the model to write Arabic clearly. It cannot force the chat application's renderer, override higher-priority instructions, or guarantee that every model follows it. App UI RTL requires UI implementation and real-device tests.
2. **Google Play in-app updates ≠ Expo OTA updates:** native binary updates use Google Play's update experience; Expo Updates distributes compatible JS/assets changes. Both have different eligibility and testing requirements.
3. **In-app review is not guaranteed to display:** Google Play applies undisclosed quotas. Never promise a dialog or infer that a review was submitted.
4. **Native features require platform checks:** Expo Go, development builds and Play-distributed builds behave differently. Verify versions and compatibility before adding a package.
5. **Google Play policies change:** always check official requirements for the actual account, targetSdk, permission set, region and release date.
6. **Do not auto-modify someone else's repo:** the skills propose a plan and request confirmation before destructive, paid, security-sensitive or publishing actions.

## Publish this repository

See [PUBLISHING.md](PUBLISHING.md) for GitHub website and CLI instructions.

## Validate this pack

Requires Python 3.10+; no third-party packages:

```bash
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Corrections backed by official Android/Expo/Play sources are welcome. Original content under [MIT](LICENSE).

## Primary sources

- [Agent Skills specification](https://agentskills.io/specification)
- [Google Antigravity agent skills](https://antigravity.google/docs/skills)
- [Google Play in-app updates](https://developer.android.com/guide/playcore/in-app-updates)
- [Google Play in-app reviews](https://developer.android.com/guide/playcore/in-app-review)
- [Expo StoreReview](https://docs.expo.dev/versions/latest/sdk/storereview/)
- [Expo Updates](https://docs.expo.dev/eas-update/introduction/)
- [Google Play Billing](https://developer.android.com/google/play/billing)
- [Personal developer testing requirements](https://support.google.com/googleplay/android-developer/answer/14151465)

_Maintainer: Michael Zahy. Initial release: November 2026._
