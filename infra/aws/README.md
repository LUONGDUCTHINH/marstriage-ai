# AWS infrastructure — placeholders only

Owner: Long — AWS & Backend, with Khoa for CI and delivery tooling.

No resources, providers, backend, credentials, account identifiers, deployment
outputs, or deployment commands are configured. The comment-only `.tf` files
reserve a possible Terraform layout; selecting Terraform and AWS services still
requires a documented team decision. They are not a deployable stack.

| Path | Intended future purpose |
| --- | --- |
| `main.tf` | Reviewed resource/module declarations |
| `variables.tf` | Documented, validated configuration inputs |
| `outputs.tf` | Useful non-sensitive outputs from actual resources |
| `environments/dev/` | Development environment planning |
| `environments/prod/` | Production environment planning |

## Before provisioning

- Agree on IaC tooling, region/environment strategy, service selection, and costs.
- Define storage and artifact lifecycle, compute/inference, backend/review
  persistence, IAM boundaries, and observability based on actual requirements.
- Design state storage/locking and access if Terraform is selected. Keep state,
  plans, environment-specific variable values, and credentials out of Git.
- Prefer short-lived AWS access, including GitHub OIDC if deployment CI is later
  approved; do not add long-lived keys to the repository.
- Review the actual change plan, validation, rollback, and teardown with Long,
  Khoa, and Thịnh before deploying. Record actual execution evidence separately.

The foundation CI only checks Python packaging and unit tests. It neither
validates AWS configuration nor authenticates to AWS or deploys infrastructure.
