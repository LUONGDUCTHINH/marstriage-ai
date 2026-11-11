# AI4MARS data

Owner: Trí — Data & Evaluation, with Hùng for model/label contracts.

The project provides an optional loader for the public
[`hassanjbara/AI4MARS` mirror](https://huggingface.co/datasets/hassanjbara/AI4MARS).
Raw data stays outside Git. The loader does not perform preprocessing, create new
splits, train a model, or establish dataset suitability for an experiment.

## Source and provenance

- Repository: `hassanjbara/AI4MARS` on Hugging Face.
- Fixed revision: `93dbb79de6cd234799750b6129fbfb3b197582fa`.
- Source card: [README at the pinned revision](https://huggingface.co/datasets/hassanjbara/AI4MARS/blob/93dbb79de6cd234799750b6129fbfb3b197582fa/README.md).
- The uploader describes this as Curiosity/MSL data mirrored from a Kaggle
  collection and declares `cc0-1.0` in the card. This records the uploader's
  metadata; the team still needs to confirm upstream provenance and usage terms
  before redistribution or publication.
- `prepare.py` in the source repository is not executed by this integration;
  the loader reads the published Parquet files through Hugging Face Datasets.

The pinned card reports these source split sizes. A successful local download
records the actual loaded sizes and features in its ignored provenance manifest.

| Source split | Rows reported by the pinned card |
| --- | ---: |
| `train` | 18,130 |
| `test_min1` | 322 |
| `test_min2` | 322 |
| `test_min3` | 322 |

Keep the three test variants separate. They are variants of expert annotations;
do not assume they are disjoint samples or use them as training/validation data.
No validation split or leakage-safe new split policy is implemented.

## Loading

From the repository root, after activating `.venv`:

```bash
python -m pip install -e ".[data]"
python -m marstriage_ai.data.ai4mars
```

This loads all splits and writes `data/cache/ai4mars/manifest-all.json` only after
the load succeeds. The manifest contains the source ID, revision, execution time,
and observed split sizes/features. It contains no model metrics. The original
Parquet downloads total approximately 6.47 GB; the Arrow cache adds about 6.52 GB.
Additional temporary space may be needed while preparing the cache.

Download only one source split, for example:

```bash
python -m marstriage_ai.data.ai4mars --split test_min1
```

This writes `manifest-test_min1.json`, not a claim that all splits were downloaded.
Use `--cache-dir PATH` to relocate the Datasets cache and manifest. Unless
`HF_HOME` is already set, the CLI also places the Hub cache under that directory.
Library callers may set `HF_HOME` before importing Hugging Face libraries to
relocate their Hub metadata/download cache.

```python
from marstriage_ai.data.ai4mars import load_ai4mars

ds = load_ai4mars()
train = ds["train"]

# For a quick preview without downloading the entire dataset:
stream = load_ai4mars("train", streaming=True)
example = next(iter(stream))
```

After a complete download, cached loading can be requested without Hub access:

```bash
HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python -m marstriage_ai.data.ai4mars
```

This requires the same source revision, cache location, and Hugging Face library
configuration as the successful download. It is not a substitute for downloading
the files first.

## Columns and labels

The source exposes `image`, `label_mask`, `rover_mask`, `range_mask`, `has_masks`,
and `has_labels`. Image fields use Hugging Face's image feature and Pillow decoding.
Some rows have no segmentation label. Check `has_labels` and `label_mask` before
using a row for supervised training; similarly check masks before using them.
The loader intentionally preserves these rows and flags without filtering.

The pinned source card describes soil, bedrock, sand, and big rock as mask values
0, 1, 2, and 3, with 255 representing unlabeled pixels. It describes masks as RGB
triples with equal channel values. These conventions still need pixel-level and
shape validation before implementing transforms, losses, or evaluation.

## Observed integration check

On 11 November 2026, a complete download of the pinned revision and an offline
cache reload returned the four split sizes listed above. Reading the source
flags found 16,064 train rows with `has_labels=True` and 2,066 without labels;
18,096 train rows had `has_masks=True`. All 322 rows in each test variant had both
flags set. These are source flag counts, not a pixel-level quality assessment.

Using Datasets 5.2.0 and Pillow 13.0.0, one labeled example from each split decoded
all four image fields at 1024×1024 in grayscale mode `L`. Thus, preserve the actual
decoded mode and verify it before assuming the source card's RGB representation.
This was a sample decoding check, not exhaustive image/mask validation or model
evaluation. The local `manifest-all.json` and `inspection.json` were kept in the
ignored cache; no dataset files were committed.

## Remaining data work

Trí and Hùng should validate annotation coverage and image/mask alignment, agree
on ignore-label handling, confirm source identities and split overlap, and define
reproducible preprocessing and any training/validation partition. Record dataset,
code, and configuration revisions for every future experiment. Use small,
explicitly synthetic fixtures for offline unit tests. Do not commit downloaded
data, cache files, weights, or generated model results.
