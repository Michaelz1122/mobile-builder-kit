# Contributing

Thanks for improving Mobile Builder Kit.

- Open an issue explaining a documentation bug or missing workflow.
- Prefer small pull requests that modify one skill at a time.
- Verify changing API guidance against official Android, Google Play, Expo and Agent Skills docs.
- Keep `SKILL.md` frontmatter valid with a unique lowercase hyphenated `name` and a descriptive `description`.
- Do not copy third-party skills verbatim without permission and a compatible license. `grill-me` here is an original question-driven workflow, not a copy of another repository.
- Don't commit API keys, user data, private screenshots or private repository content.
- Run `python scripts/validate_skills.py` and `python -m unittest discover -s tests -v` before proposing a PR.
- Explain why a new capability should be a separate focused skill or a small reference file.
- For policy-driven advice, say when you checked the official source.

## Issue template

**Skill:**  
**Expected behavior:**  
**Actual behavior:**  
**Example prompt:**  
**Official documentation (if relevant):**
