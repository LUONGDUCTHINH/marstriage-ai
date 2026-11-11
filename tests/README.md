# Tests

Install the package and development tools with `python -m pip install -e ".[dev]"`.
Run `python -m pytest tests/unit` from the repository root.

`unit/` starts with package smoke tests. They verify that the installed
distribution is discoverable and that the intended namespaces can be imported
without datasets, GPUs, credentials, or network services. They make no claims
about model quality or deployed infrastructure.

As features are implemented, add small deterministic tests for their behavior and
error cases. Keep synthetic fixtures small and clearly identified as synthetic.
Do not use a passing dummy assertion or skip an unimplemented feature to suggest
that it has been validated.

See [integration testing](integration/README.md) before adding service-dependent
checks. CI currently runs only `tests/unit/`.
