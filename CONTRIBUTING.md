# Contributing

## Development setup

Follow the [README quick start](README.md#quick-start) with Python 3.11 or newer.
All current checks run locally without AWS credentials, datasets, or GPUs.

```bash
python -m pip install -e ".[dev]"
python -m ruff check .
python -m ruff format --check .
python -m pytest tests/unit
python -m build
```

Use `python -m ruff format .` to apply formatting. Development dependencies are
bounded in `pyproject.toml`; a fully pinned application lockfile is not provided
at this foundation stage. Record resolved tool versions when reporting checks.

## Branches and pull requests

1. Start from an up-to-date `main` and create a focused branch, for example
   `git switch -c feat/dataset-manifest` or `codex/initial-project-foundation`.
2. Keep changes small, add behavioral tests for implemented features, and update
   the relevant documentation.
3. Run the checks above and record exactly what ran and what happened. State
   explicitly when a check was not run or failed.
4. Open a pull request targeting `main` using the PR template. Ask the relevant
   owner in the [team table](docs/team.md) for review.
5. Wait for review and required checks. Authors must not merge their own work
   without the team's approval. Branch protection must be configured separately;
   these repository files do not enforce it.

## Ownership

- Thịnh — Project Lead: scope, coordination, architecture, final review.
- Khoa — DevOps & Frontend: CI, tooling, frontend, human review UI.
- Trí — Data & Evaluation: dataset provenance, splits, metrics, evaluation.
- Long — AWS & Backend: backend contracts, AWS, infrastructure.
- Hùng — Computer Vision: segmentation, inference, uncertainty models.

The commented [.github/CODEOWNERS](.github/CODEOWNERS) is a template. Confirm
actual GitHub handles and repository permissions before activating rules. Never
guess a handle from a person's name.

## Engineering and evidence

- Keep Python code under `src/marstriage_ai/` and deterministic unit tests under
  `tests/unit/`. Keep imports free of network calls and infrastructure creation.
- Use [architecture decisions](docs/decisions/README.md) for significant changes
  such as model frameworks, AWS services, or the infrastructure tooling.
- Dataset documentation must include provenance, usage rights, labeling details,
  and split policy. Keep raw data, generated data, weights, and experiment
  artifacts outside Git.
- Report metrics only after an actual run, with dataset and code revisions,
  configuration, seeds, and artifact references. Mark examples as examples.
- AWS folders are planning placeholders. Any future deployment change must
  document its reviewed plan, permissions, costs, validation, and teardown.
- Never commit credentials, access keys, private keys, local `.env` files,
  Terraform state, or account-specific configuration. Unit-test CI must not
  require AWS authentication.

## Maintainer setup still required

Thịnh and Khoa should confirm collaborator access, activate CODEOWNERS with
verified handles, and agree on required reviews and CI checks before configuring
branch protection. No repository setting changes are implied by this scaffold.
The team should also select a project license before publishing distributions.
