# Evaluation plan

Owner: Trí — Data & Evaluation, with Hùng for model outputs and uncertainty.
Status: no evaluation has been run and no scores are reported.

Agree on the protocol before comparing models:

- Versioned train/validation/test splits and a leakage review.
- Label mapping, ignore-mask handling, class imbalance, and aggregation rules.
- Candidate segmentation measures such as per-class IoU and mean IoU; final
  metrics and acceptance criteria remain to be agreed.
- Uncertainty assessment, calibration measures, and how uncertainty informs
  human review. An uncertainty score is not automatically a calibrated probability.
- Reproducibility, seeds, missing/invalid inputs, and reporting of limitations.

Every future result must identify the dataset and code revisions, split,
configuration, checkpoint, environment, execution date, and real artifact
references. Do not substitute example values or unit-test results for measured
model performance.
