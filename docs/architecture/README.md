# Planned architecture

Status: proposal only. No end-to-end path is implemented or deployed.

The intended flow is:

```text
Versioned terrain images and labels
    -> validated preprocessing
    -> segmentation and uncertainty inference
    -> evaluation and review prioritization
    -> human review UI and recorded decisions
```

## Boundaries

- **Data — Trí:** ingestion, provenance, label schema, and split manifests.
- **Vision — Hùng:** model interface, segmentation outputs, uncertainty methods.
- **Evaluation — Trí with Hùng:** offline metrics, calibration analysis, and
  reproducible reports.
- **Backend — Long:** API contracts, artifact access, and review persistence.
- **Review UI — Khoa with Long:** presentation, review actions, and contracts.
- **AWS and CI — Long with Khoa:** infrastructure design and delivery workflow.
- **Coordination — Thịnh:** scope, interfaces, and architecture decisions.

Python namespaces reserve these boundaries without selecting a model framework,
web framework, or AWS runtime. Unit-test imports must remain independent of cloud
configuration and model downloads.

## Decisions still needed

Dataset provenance and rights; label taxonomy and ignore rules; leakage-safe
splits; baseline model and uncertainty method; artifact formats; API/review
contracts; AWS service selection; identity, retention, cost, and observability.
Record accepted choices in [decision records](../decisions/README.md).
