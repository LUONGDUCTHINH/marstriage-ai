# Operations and CI

Owners: Khoa — DevOps & Frontend; Long — AWS & Backend.

## Foundation CI

[CI configuration](../../.github/workflows/ci.yml) runs on pull requests targeting
`main`, pushes to `main`, and manual dispatch. It configures:

- Ruff lint and formatting checks on Python 3.13.
- Source distribution and wheel builds, plus wheel imports in a fresh environment.
- Unit tests on Python 3.11, 3.12, 3.13, and 3.14.

Actions are pinned to commit SHAs, job permissions are `contents: read`, checkout
does not persist credentials, and jobs have timeouts. CI has no AWS login, model
training, dataset downloads, publishing, or deployment steps.

Workflow configuration is not proof that a run passed. Inspect the PR checks and
linked Actions run for actual status. Do not describe an unexecuted matrix as
verified. Tests cover packaging and offline loader behavior, not backend or model
behavior. The optional data extra and real dataset downloads are not part of CI.

The workflow uses the installed development dependency ranges from
`pyproject.toml`; they are not a fully locked environment. Record tool versions
for reproducibility and revisit locking when application dependencies are added.

GitHub Actions references:
[checkout](https://github.com/actions/checkout) and
[setup-python](https://github.com/actions/setup-python).

## AWS work still to design

See [AWS placeholders](../../infra/aws/README.md). Define the environment model,
service selection, least-privilege roles, GitHub OIDC federation, state storage,
cost limits, logging, rollback, and teardown before adding deployment automation.
No AWS infrastructure or deployment workflow exists at this stage.

Thịnh and Khoa still need to agree on required reviews and checks before
configuring branch protection. Long and Khoa must review any future cloud changes.
