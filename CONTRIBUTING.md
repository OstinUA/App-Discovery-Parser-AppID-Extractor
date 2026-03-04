# Contributing Guide

First of all, thanks for considering a contribution.
This project is intentionally simple on the surface, but we still care a lot about maintainability, reproducibility, and clean DX for everyone touching the code.

If you want to improve parser logic, UX, docs, localization, or delivery workflows, you are absolutely welcome.

## Introduction

Contributions are accepted in many forms:

- Bug fixes
- Parser quality improvements
- Performance tuning
- Documentation upgrades
- Localization enhancements
- Developer tooling and CI hygiene

Please keep PRs focused and scoped to one logical change set when possible.

## I Have a Question

Please **do not** use GitHub Issues for general usage questions.
Issues are reserved for actionable bugs and feature work.

Use one of these channels instead:

- GitHub Discussions (preferred, if enabled)
- Project social channels listed in `README.md`
- Community dev chats related to Streamlit/Python parsing workflows

If your question reveals a docs gap, feel free to open a docs PR.

## Reporting Bugs

High-signal bug reports save everyone time. Before opening a bug issue:

1. Search existing Issues to avoid duplicates.
2. Validate the issue on the latest `main` branch.
3. Reduce to a minimal reproducible example.

When opening the issue, include:

- **Environment**
  - OS and version
  - Python version (`python --version`)
  - App version/commit SHA
  - Dependency snapshot (`pip freeze` if relevant)
- **Steps to Reproduce**
  - Exact ordered steps
  - Sample input (or redacted equivalent)
- **Expected Behavior**
  - What should happen
- **Actual Behavior**
  - What currently happens
  - Full traceback/logs if available
- **Impact**
  - Is this blocking, high-priority, or edge-case?

Issue template suggestion:

```markdown
### Environment
- OS:
- Python:
- Commit SHA:

### Steps to Reproduce
1.
2.
3.

### Expected Behavior

### Actual Behavior

### Additional Context
```

## Suggesting Enhancements

Feature requests are welcome, but they should be problem-driven, not just solution-driven.

A solid enhancement request should explain:

- What pain point exists today
- Who is affected (analyst, integrator, maintainer)
- Why current behavior is insufficient
- Proposed solution and trade-offs
- At least one realistic use case

Bonus points for including rough API/UX sketches or implementation notes.

## Local Development / Setup

### 1) Fork and clone

```bash
# Fork on GitHub first, then clone your fork
git clone https://github.com/<your-user>/app-discovery-parser-appid-extractor.git
cd app-discovery-parser-appid-extractor
```

### 2) Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run locally

```bash
streamlit run app.py
```

### 5) Optional local quality tooling

```bash
pip install pytest black flake8 ruff
```

If `.env` is added in future changes, follow the standard pattern:

```bash
cp .env.example .env
```

Then fill in required keys before running the app.

## Pull Request Process

### Branch strategy

Use clear branch names:

- `feature/<short-description>`
- `bugfix/<issue-or-short-description>`
- `docs/<scope>`
- `chore/<scope>`

Examples:

- `feature/add-german-localization`
- `bugfix/fix-ios-id-regex-edgecase`
- `docs/rewrite-readme-and-contributing`

### Commit messages

Use **Conventional Commits** style:

- `feat: add URL mode timeout handling`
- `fix: preserve order in Apple ID dedup`
- `docs: expand deployment section in README`
- `chore: add linting instructions`

### Sync with upstream

Before opening a PR, rebase on latest `main`:

```bash
git fetch upstream
git checkout main
git pull upstream main
git checkout <your-branch>
git rebase main
```

### PR description requirements

A good PR body should include:

- Summary of what changed
- Why it changed
- Linked Issue (`Closes #123` if applicable)
- Testing evidence (commands + outputs)
- Screenshots/GIFs for UI-visible updates

Keep PRs reviewable. Giant mixed-scope PRs will likely be asked to split.

## Styleguides

### Python style

- Follow PEP 8 conventions.
- Prefer explicit, readable naming.
- Keep functions focused and composable.
- Avoid dead code and speculative abstractions.

### Formatting and linting

Recommended tools:

- `black` for formatting
- `flake8` or `ruff` for linting
- `pytest` for tests

Suggested commands:

```bash
black .
flake8 .
# or
ruff check .
pytest
```

### Project-specific architecture preferences

- Keep parsing logic in `parser_logic.py` unless a clear modular split is needed.
- Keep UI concerns in `app.py`.
- Avoid coupling parser core to Streamlit internals.
- Keep localization keys consistent across languages.

## Testing

All non-trivial changes should include validation evidence.

Minimum expectation before PR submission:

- Run local app once: `streamlit run app.py`
- Run parser smoke checks on representative HTML snippets
- Run lint/format checks for touched files

If you add new parser behavior, include unit tests for:

- Positive matches
- False-positive prevention
- Deduplication behavior
- Edge-case input patterns

## Code Review Process

- PRs are reviewed by project maintainers.
- At least one maintainer approval is typically required before merge.
- Review feedback should be addressed with follow-up commits or a clear technical rationale.
- If a reviewer requests changes, update the PR and comment with what was resolved.
- Keep communication technical, direct, and respectful.

By contributing, you agree that your contributions can be distributed under the project license.
