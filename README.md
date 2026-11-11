# marstriage-ai

A project for Martian terrain segmentation, uncertainty estimation, and
human-in-the-loop review, with a planned AWS deployment.

**Status: project foundation with an AI4MARS loader.** This repository provides
Python packaging, an optional Hugging Face dataset loader, contributor guidance,
unit tests, CI configuration, and infrastructure placeholders. Model training,
preprocessing, an API, review UI, and AWS deployment remain planned. No model
metrics or deployment outcomes are reported.

## Quick start

Use Python 3.11 or newer. CI is configured for Python 3.11–3.14.
No AWS account, credentials, GPU, or dataset is needed for the foundation checks.

```bash
git clone https://github.com/LUONGDUCTHINH/marstriage-ai.git
cd marstriage-ai
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

Run the same checks used by CI:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest tests/unit
python -m build
```

These commands are instructions, not a claim that checks have passed. Actual
results belong in the pull request and its GitHub Actions runs. Unit tests check
packaging and loader behavior offline; they do not evaluate a model.

## Load AI4MARS

Install the optional data dependencies and cache the source dataset locally:

```bash
python -m pip install -e ".[data]"
python -m marstriage_ai.data.ai4mars
```

The download is approximately 6.47 GB; the downloaded files and prepared Arrow
cache together need roughly 13 GB. The CLI stores its cache and provenance
manifest under `data/cache/ai4mars/`, which Git ignores. An existing `HF_HOME`
setting takes precedence for the Hugging Face Hub metadata/download cache.

Use the same pinned source from Python:

```python
from marstriage_ai.data.ai4mars import load_ai4mars

ds = load_ai4mars()  # train, test_min1, test_min2, test_min3
sample_stream = load_ai4mars("train", streaming=True)  # read on demand
```

The loader wraps `datasets.load_dataset("hassanjbara/AI4MARS", ...)` with a fixed
source revision and public access without a token. See [data documentation](docs/data/README.md)
for provenance, columns, missing labels, source splits, and smaller loading options.

## Repository layout

```text
.github/                   CI, pull request template, CODEOWNERS template
docs/                      Architecture, data, models, evaluation, operations
frontend/                  Review UI planning placeholder
infra/aws/                 AWS / Terraform planning placeholders
src/marstriage_ai/
    backend/               Backend and AWS integration namespace
    data/                  AI4MARS loader; preprocessing remains planned
    evaluation/            Evaluation and uncertainty analysis namespace
    review/                Human review contract namespace
    vision/                Segmentation and uncertainty model namespace
tests/
    unit/                  Local, credential-free package smoke tests
    integration/           Future integration-test guidance
```

The data namespace provides the loader; other namespaces reserve planned code.

## Team responsibilities

| Member | Role | Primary responsibility |
| --- | --- | --- |
| Thịnh | Project Lead | Scope, architecture decisions, coordination, review |
| Khoa | DevOps & Frontend | CI, developer tooling, frontend and review UI |
| Trí | Data & Evaluation | Data provenance, splits, metrics and evaluation |
| Long | AWS & Backend | Backend contracts, AWS design and infrastructure |
| Hùng | Computer Vision | Segmentation models, inference and uncertainty methods |

See [team ownership](docs/team.md) and the [contribution guide](CONTRIBUTING.md).
GitHub handles have not been assigned to the CODEOWNERS template.

## Documentation and next steps

- [Documentation index](docs/README.md)
- [Planned architecture](docs/architecture/README.md)
- [Foundation roadmap](docs/roadmap.md)
- [AWS placeholders](infra/aws/README.md)

Keep datasets, model weights, generated results, local configuration, and
credentials out of Git. Document the source, revision, configuration, and actual
execution evidence before reporting any experimental or infrastructure outcome.
