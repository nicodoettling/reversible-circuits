# Worker B bounded sandbox smoke report

## Scope

This was an infrastructure smoke test, not a goal run or a mixing experiment.
All writes were limited to the assigned `worker-b` directory except for the
single required attempt to create `/home/nico/.codex-bwrap-smoke-forbidden-b`.
No escalation, network access, external service, package installation, Magma,
commit, or push was used.

## Environment

The recorded sandbox environment has groups `nico nogroup`, bubblewrap at
`/usr/bin/bwrap` with version `0.9.0`, and Python `3.12.3`. Full command output
is in `environment.txt`.

## Write-boundary check

Writing `workspace-write-ok.txt` in the assigned workspace directory
succeeded. The one forbidden command attempted was:

```text
touch /home/nico/.codex-bwrap-smoke-forbidden-b
```

It returned exit code `1` with stderr:

```text
touch: cannot touch '/home/nico/.codex-bwrap-smoke-forbidden-b': Read-only file system
```

The outside file was absent after the attempt. The exit code and stderr are
preserved in `denial-exit-code.txt` and `denial-stderr.txt`.

## Exact finite permutation check

`permutation_dp.py` represents a permutation `p` by its images and defines
`compose(p, q) = p o q`, so `q` acts first. Starting at the identity, each DP
step appends every transposition on the right; thus states track the ordered
product `t1 t2 ... tm`. Counts are propagated over permutation states with
integer arithmetic for four steps. Complete words are not enumerated with
`itertools.product`.

Command:

```text
python3 permutation_dp.py
```

Output:

```json
{"S3_m4": 27, "S4_m4": 120, "method": "permutation_state_dp"}
```

Both exact finite counts match the supplied smoke criteria. These are exact
finite-state facts used only to validate the smoke script; they imply no
research, asymptotic, irreducibility, spectral-gap, or mixing claim.

## Verdict

`pass`: sandboxed workspace writing and exact Python execution succeeded, and
the required outside-workspace write was denied with the outside file absent.
