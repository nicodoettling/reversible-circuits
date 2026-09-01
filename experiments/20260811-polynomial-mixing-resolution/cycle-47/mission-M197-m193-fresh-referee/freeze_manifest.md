# M197 freeze manifest

Date: 2026-08-13 UTC.
Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Verdict

```text
FINAL REFEREE VERDICT: ACCEPT FROZEN M193.
MATERIAL OBJECTIONS: none.
```

M193's eight payload hashes and exact inventory passed before conclusions;
its checksum-ledger digest is
`aff1302508bfc61727e47649f0810183ff7fc7f28e7840bc3bbc239e828af0b2`.
Every recorded checksum in its eighteen accepted dependency ledgers passed.
No predecessor was edited.

## Frozen payload inventory

```text
plan.md
checkpoint.md
independent_symbolic.py
independent_results.json
proof_audit.md
report.md
freeze_manifest.md
```

`SHA256SUMS` is the self-excluded ledger added after this manifest. No cache,
bytecode, or temporary file belongs to M197's payload.

## Reproduction

```text
python3 -B independent_symbolic.py --output independent_results.json
sha256sum -c SHA256SUMS
```

Environment: Python 3.12.3, SymPy 1.12, seed `null`. The checker imports no
M193 artifact and performs no `L=7` or state-graph enumeration.

## Claim and hygiene boundary

Acceptance covers only M193's fresh actual-history `h=3` sector theorem:
`h3<=27/125` for `n>=1` and the separate `h3<3/8` boundary for `n=0`.
It does not include reset, `h>=4`, total AMV, all-`L`, a gap, mixing, or a
terminal.

Pre-existing unledgered `__pycache__` directories in immutable M117, M162,
and M165 are recorded solely as an external hygiene caveat. Their ledgered
payload hashes pass, M193's own inventory is clean, and this is not an M193
objection.
