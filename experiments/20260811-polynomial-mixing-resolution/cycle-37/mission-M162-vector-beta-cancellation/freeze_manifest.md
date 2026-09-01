# M162 freeze manifest

Freeze date: 2026-08-13 UTC.

## Immutable scope

Repository base commit:

```text
502a6f031c6d5a4bc0064ee5b370a4fa3914f993
```

Owned frozen artifacts are:

```text
plan.md
checkpoint.md
vector_beta_exact.py
vector_beta_exact.json
vector_beta_theorem.md
report.md
freeze_manifest.md
SHA256SUMS
```

No predecessor, coordinator note, manuscript, project skill, package,
configuration, commit, or remote state was changed.  The generated owned
`__pycache__` directory was removed before freeze.

## Exact command

Run from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-37/mission-M162-vector-beta-cancellation/vector_beta_exact.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-37/mission-M162-vector-beta-cancellation/vector_beta_exact.json \
  --max-B 3 --max-excess 6 --max-kappa 8
```

Environment:

```text
Python 3.12.3
nonstandard dependencies: none
random seed: null (deterministic exact enumeration)
```

The final command reported:

```text
failure_count=0
state_count=588
right_heavy_state_count=147
first_degree_one_failure_state=null
max_minimal_truncation=1
vector_beta_exact.json sha256=fc4b0506e14a044fa0727e08f67d70f3c8caccc77b186184b78fe20ce3b325d3
```

The compact JSON is 17,996 bytes.  No `L=7` enumeration was run.

## Freeze checks

Before writing the final hash list:

- `python3 -m compileall -q .../vector_beta_exact.py` completed successfully;
- the exact capped command above completed successfully;
- JSON parsing and theorem-critical summary extraction succeeded;
- the output contained zero mathematical/checker failures;
- the scoped owned file inventory contained only the listed artifacts;
- the owned bytecode cache was removed;
- Markdown and Python changes were checked for whitespace errors.

`SHA256SUMS` records final bytes of every artifact except itself.  Any later
change to a listed artifact invalidates this freeze and requires a new hash
list and audit.
