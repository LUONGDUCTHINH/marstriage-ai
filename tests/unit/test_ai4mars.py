"""Offline loader behavior tests using synthetic dependency responses."""

import builtins
import json
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from marstriage_ai.data import ai4mars


def test_loader_pins_source_and_uses_public_access(monkeypatch, tmp_path) -> None:
    load_dataset = Mock(return_value=object())
    monkeypatch.setitem(
        sys.modules, "datasets", SimpleNamespace(load_dataset=load_dataset)
    )

    result = ai4mars.load_ai4mars(cache_dir=tmp_path)

    assert result is load_dataset.return_value
    load_dataset.assert_called_once_with(
        ai4mars.DATASET_ID,
        name="default",
        revision=ai4mars.DATASET_REVISION,
        split=None,
        cache_dir=str(tmp_path),
        streaming=False,
        token=False,
    )


@pytest.mark.parametrize("split", ai4mars.SPLITS)
def test_loader_preserves_split_and_streaming(monkeypatch, split) -> None:
    load_dataset = Mock()
    monkeypatch.setitem(
        sys.modules, "datasets", SimpleNamespace(load_dataset=load_dataset)
    )

    ai4mars.load_ai4mars(split, streaming=True)

    assert load_dataset.call_args.kwargs["split"] == split
    assert load_dataset.call_args.kwargs["streaming"] is True


def test_unknown_split_fails_before_loading(monkeypatch) -> None:
    load_dataset = Mock()
    monkeypatch.setitem(
        sys.modules, "datasets", SimpleNamespace(load_dataset=load_dataset)
    )

    with pytest.raises(ValueError, match="Unknown AI4MARS split"):
        ai4mars.load_ai4mars("validation")

    load_dataset.assert_not_called()


def test_missing_optional_dependency_has_setup_instructions(monkeypatch) -> None:
    original_import = builtins.__import__

    def import_without_datasets(name, *args, **kwargs):
        if name == "datasets":
            raise ModuleNotFoundError("No module named 'datasets'", name="datasets")
        return original_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", import_without_datasets)

    with pytest.raises(ModuleNotFoundError, match=r"\[data\]"):
        ai4mars.load_ai4mars()


@pytest.mark.parametrize("split", [None, "test_min1"])
def test_cli_records_loaded_metadata_without_merging_splits(
    monkeypatch, tmp_path, split
) -> None:
    # Deliberately synthetic: these values are not real dataset statistics.
    dataset = SimpleNamespace(
        num_rows=2,
        features=SimpleNamespace(to_dict=lambda: {"has_labels": {"dtype": "bool"}}),
    )
    returned = {"train": dataset, "test_min1": dataset} if split is None else dataset
    load = Mock(return_value=returned)
    monkeypatch.setattr(ai4mars, "load_ai4mars", load)
    monkeypatch.setenv("HF_HOME", str(tmp_path / "existing-hub"))
    args = ["--cache-dir", str(tmp_path)]
    if split is not None:
        args += ["--split", split]

    assert ai4mars.main(args) == 0

    manifest = json.loads((tmp_path / f"manifest-{split or 'all'}.json").read_text())
    assert manifest["revision"] == ai4mars.DATASET_REVISION
    assert set(manifest["splits"]) == (
        {"train", "test_min1"} if split is None else {split}
    )
    assert all(value["num_rows"] == 2 for value in manifest["splits"].values())
    load.assert_called_once_with(split, cache_dir=Path(tmp_path).resolve())
