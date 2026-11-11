# Data plan

Owner: Trí — Data & Evaluation. Status: no dataset is included or validated.

Before ingestion is implemented, document:

- Source URL, version, collection context, usage rights, and attribution.
- Image and annotation formats, coordinate conventions, label taxonomy,
  ignore labels, quality checks, and known gaps.
- Immutable dataset/split manifests and checksums. Split by an appropriate
  grouping unit before augmentation to avoid train/evaluation leakage.
- Reproducible preprocessing configuration and links to input revisions.
- Storage, retention, access, and any download instructions.

Keep raw and processed data outside Git. Use tiny synthetic fixtures for unit
tests; label them as synthetic and do not present them as Martian observations.
Agree on the label and split contract with Hùng before training or evaluation.
