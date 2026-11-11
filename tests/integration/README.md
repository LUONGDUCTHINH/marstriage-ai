# Integration tests — planned

Owners: Long (backend and AWS), Khoa (CI), Trí (data and evaluation).

There are no integration tests yet. Future integration tests belong here and
must use `@pytest.mark.integration`. They must document their dependencies,
required configuration, expected costs, and cleanup before they are enabled.

Keep unit tests independent of this folder and external services. Run approved
integration tests explicitly with `python -m pytest tests/integration -m integration`.
An empty integration suite is not evidence that AWS or backend integration works.
