# M278 freeze manifest

Date: 2026-08-14 UTC.

## Frozen disposition

**PROVED ANALYTICALLY; PROMOTE TO FRESH AUDIT.**

For every `d>=5` and every tree on `[d]` rooted at leaf `d` with
`{1,d}`, M278 proves the local old-padded/new DPS routes

```text
internal even i<=2d-6 : identity;
i=2d-4                : (R_(2d-5)^(-1))^2;
i=2d-3                : R_(2d-2)^(-1).
```

The exact source/target factors, endpoint tables, signs, chronology,
root/new-child positions, post-wrap regimes, and `d=5` boundary are frozen
in `fixed_edit_boundary_theorem.md`.

## Immutable inputs

Every payload entry in the M225/M228, M231/M234, M236/M237, M240/M242,
M269/M271, and M273/M275 inventories verified.  The top-level inventory
digests are recorded in `checkpoint.md`.  The locked DPS source digest is

```text
98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2
```

for `/tmp/DuPoSc13.pdf`.  No predecessor was modified.

## Analytic/finite boundary

The proof is the arbitrary-rank complete-interval LIFO erasure and literal
endpoint calculation.  Only after its formulas were frozen, the
no-predecessor-import guard checked exactly `d=5,6`: `141` trees,
`407` internal-even rows, `141` cross-boundary rows, and `141`
last-edit rows.  All passed.  The guard performs no route search and is only
a transcription/minimal-boundary falsifier.

Reproduction:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-77/mission-M278-fixed-edit-boundaries/guard.py
```

Python `3.12.3`.

## Formal composition and strict scope

Subject to fresh acceptance of M278, the accepted ordinary route chain
M269/M271 + M273/M275, then M250/M254 ordinary IDL, then M240/M242 ordinary
odd-edit routing, can be formally augmented by the fixed lengths `0,2,1`
to cover every adjacent edit in the local rooted-row table at maximum length
`4d-7`.

This freeze does not assert every-color synchronization, voltage correction,
other routing obligations, congestion, a spectral gap, polynomial mixing,
or Terminal A/B.  No such conclusion is licensed before fresh audit and a
separate assembly.

## Frozen payload

`SHA256SUMS` covers:

- `audit_request.md`
- `checkpoint.md`
- `fixed_edit_boundary_theorem.md`
- `freeze_manifest.md`
- `guard.py`
- `guard_results.json`
- `plan.md`
- `report.md`

The checksum file excludes itself.  The SHA-256 digest of `SHA256SUMS` is
the top-level mission inventory digest reported to the coordinator.
