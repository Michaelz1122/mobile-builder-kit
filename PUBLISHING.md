# Publish Mobile Builder Kit to GitHub

This repository contains reusable Agent Skills, not an Android app. Publishing it on GitHub makes the instruction files reusable; it does not publish an APK to Google Play.

## Option 1 — GitHub website (beginner friendly)

1. Sign in to GitHub and create a new public repository named `mobile-builder-kit` under your own account. Do **not** initialize it with a README, license, or `.gitignore` because this package already includes those files.
2. Download and unzip this project. Open a terminal in the `mobile-builder-kit` directory.
3. Run the commands below (requires Git installed). Replace `YOUR_USERNAME` with your real GitHub login.

```bash
git init
git add .
git commit -m "Initial open-source Mobile Builder Kit skills"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/mobile-builder-kit.git
git push -u origin main
```

GitHub may ask you to sign in through a credential manager; don't put access tokens in source files.

## Option 2 — GitHub CLI

Requires the official GitHub CLI (`gh`) and login with `gh auth login`.

```bash
git init
git add .
git commit -m "Initial open-source Mobile Builder Kit skills"
git branch -M main
gh repo create mobile-builder-kit --public --source=. --remote=origin --push
```

## Before sharing the link

```bash
python scripts/validate_skills.py
python -m unittest discover -s tests -v
python scripts/install.py --target /path/to/test-project --all --dry-run
```

Then open the repository's `README.md` page, confirm `skills/` directories and `.github/workflows/validate.yml`, enable GitHub Actions if needed, and test installation in a disposable Antigravity project.

## Recommended repository settings

- Description: `Open-source Agent Skills for Android AI app builders: Arabic RTL, Grill Me, Expo, Play Updates, Reviews, QA & ASO.`
- Topics: `agent-skills`, `google-antigravity`, `react-native`, `expo`, `android`, `rtl`, `vibe-coding`, `google-play`
- Public, MIT license (already included).
- First release tag after verification: `v0.1.0`.

Do not copy secrets, app signing keys, Play Console credentials, API keys, `.env` files, or private project assets into this public repository.
