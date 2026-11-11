"""Load the public AI4MARS dataset at a fixed Hugging Face revision.

Install the optional dependencies with ``pip install -e '.[data]'``.
Run ``python -m marstriage_ai.data.ai4mars`` from the project root to cache
all source splits locally. This module does not train or evaluate a model.
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datasets import Dataset, DatasetDict, IterableDataset, IterableDatasetDict

DATASET_ID = "hassanjbara/AI4MARS"
DATASET_REVISION = "93dbb79de6cd234799750b6129fbfb3b197582fa"
SPLITS = ("train", "test_min1", "test_min2", "test_min3")
DEFAULT_CACHE_DIR = Path("data/cache/ai4mars")


def load_ai4mars(
    split: str | None = None,
    *,
    cache_dir: str | Path = DEFAULT_CACHE_DIR,
    streaming: bool = False,
) -> Dataset | DatasetDict | IterableDataset | IterableDatasetDict:
    """Load source splits without relabeling, filtering, or merging them.

    ``split=None`` returns all four source splits. ``streaming=True`` reads on
    demand instead of downloading the full dataset. The optional dependency is
    imported only when this function is called; public access uses no HF token.
    ``cache_dir`` controls the Datasets cache. The CLI also places the Hub cache
    under this directory; library callers can set ``HF_HOME`` before importing
    Hugging Face libraries if they need to relocate their Hub metadata cache.
    """
    if split is not None and split not in SPLITS:
        raise ValueError(f"Unknown AI4MARS split {split!r}; choose one of {SPLITS}.")

    try:
        from datasets import load_dataset
    except ModuleNotFoundError as error:
        if error.name != "datasets":
            raise
        raise ModuleNotFoundError(
            'AI4MARS requires the data extra: python -m pip install -e ".[data]"'
        ) from error

    return load_dataset(
        DATASET_ID,
        name="default",
        revision=DATASET_REVISION,
        split=split,
        cache_dir=str(Path(cache_dir)),
        streaming=streaming,
        token=False,
    )


def main(argv: list[str] | None = None) -> int:
    """Download all splits or one selected split and record observed metadata."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--split", choices=SPLITS, help="Default: all source splits")
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE_DIR)
    args = parser.parse_args(argv)

    cache_dir = args.cache_dir.resolve()
    # Set this before the lazy HF import. Respect an existing user cache setting.
    os.environ.setdefault("HF_HOME", str(cache_dir / "huggingface"))
    loaded = load_ai4mars(args.split, cache_dir=cache_dir)
    splits = loaded if args.split is None else {args.split: loaded}
    manifest = {
        "dataset_id": DATASET_ID,
        "revision": DATASET_REVISION,
        "loaded_at_utc": datetime.now(UTC).isoformat(),
        "splits": {
            name: {
                "num_rows": dataset.num_rows,
                "features": dataset.features.to_dict(),
            }
            for name, dataset in splits.items()
        },
    }
    cache_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = cache_dir / f"manifest-{args.split or 'all'}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    for name, dataset in splits.items():
        print(f"{name}: {dataset.num_rows:,} rows")
    print(f"Source revision: {DATASET_REVISION}")
    print(f"Local manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
