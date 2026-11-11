# Team and review responsibilities

| Member | Role | Primary paths and responsibility |
| --- | --- | --- |
| Thịnh | Project Lead | Scope, README, architecture, decisions, milestones and review coordination |
| Khoa | DevOps & Frontend | `.github/`, developer tooling, `frontend/`, CI and review UI |
| Trí | Data & Evaluation | `src/marstriage_ai/data/`, `evaluation/`, data and evaluation documentation |
| Long | AWS & Backend | `src/marstriage_ai/backend/`, `infra/aws/`, backend and cloud contracts |
| Hùng | Computer Vision | `src/marstriage_ai/vision/`, model documentation, segmentation and uncertainty methods |

Khoa and Long jointly define the human review contract under
`src/marstriage_ai/review/`. Trí and Hùng agree on evaluation protocols before
experiments. Long and Khoa agree on deployment and CI integration before AWS
resources are introduced. Thịnh coordinates decisions across these boundaries.

Ownership identifies who should review a change; it does not claim that a feature
is implemented or that approval has been granted. Ask the relevant member for
review and escalate cross-cutting decisions to Thịnh.

GitHub handles and repository access still need confirmation. The
[CODEOWNERS template](../.github/CODEOWNERS) is inactive until real handles replace
the commented placeholders and rules are enabled. Required reviews and branch
protection are separate maintainer configuration tasks.
