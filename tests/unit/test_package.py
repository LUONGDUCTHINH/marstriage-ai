"""Smoke tests for the installed Python project, not model evaluation."""

from importlib import import_module, metadata

import pytest


def test_distribution_metadata_is_available() -> None:
    """Catch missing installation or invalid distribution metadata."""
    distribution = metadata.distribution("marstriage-ai")

    assert distribution.metadata["Name"] == "marstriage-ai"
    assert distribution.version


@pytest.mark.parametrize(
    "module_name",
    [
        "marstriage_ai",
        "marstriage_ai.backend",
        "marstriage_ai.data",
        "marstriage_ai.data.ai4mars",
        "marstriage_ai.evaluation",
        "marstriage_ai.review",
        "marstriage_ai.vision",
    ],
)
def test_package_namespaces_are_importable(module_name: str) -> None:
    """Catch package discovery errors without external runtime dependencies."""
    module = import_module(module_name)

    assert module.__name__ == module_name
