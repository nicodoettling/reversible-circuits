# M155 freeze manifest

Date: 2026-08-13 UTC.

## Verdict and exact scope

```text
FINAL VERDICT: STRICT BOUNDARY-CONDENSATE REDUCTION.
DIRECT O(k^-2) L1: UNRESOLVED.
```

The frozen proved result concerns only the balanced strict edge of the
nonlazy cyclic rank-two quotient kernel for uniform minimal factorizations of
the long cycle, with `n=3k`, odd `k>=3`.  It consists of the exact
separated-color L1 disintegration, product-critical-Borel boundary limit,
the `(2/pi)log D+O(1)` minimum-moment threshold, and the conditional
`(BLM)`/`(UBL)` implications.  It proves no direct L1 upper or lower theorem,
general strict-edge theorem, H0 theorem, fixed-endpoint/identity-chain gap,
or Terminal.

## Accepted dependencies

- M73/M80: exact quotient kernel, colored compositions, strict-edge geometry.
- M83/M88: balanced strict edge and one-step obstruction.
- M91: exact posterior/Borel--Abel formula.
- M94/M100: exact signed two-step score, colored double encoding, shell law.
- M102/M105: nonintegrable intermediate collision face and the correction
  that lower-support matching topology is not known complete.

Every collision and lower-support term remains combined inside the exact
score before the absolute value in M155.

## Reproduction

From the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-35/mission-M155-balanced-direct-l1/boundary_condensate_check.py --output experiments/20260811-polynomial-mixing-resolution/cycle-35/mission-M155-balanced-direct-l1/boundary_condensate_results.json
```

Python `3.12.3`; standard library only; deterministic; `seed=null`.  Exact
`Fraction` checks cover the point-cell and total separated-mass identities
for `k=3,5,7,9`.  The inherited shell summaries at `k=7,9` are finite
floating calibration only.  Two capped broad reconstructions produced no
file and are not part of the package.

## Owned pre-freeze hashes

```text
0709b2c0d978926032f0116e6a5c8c2941828ac27d5e222abdd53a702895ce31  plan.md
3a61e1861707d004454370fbaf8a4cd5dcb8a8aa12f33793982958adb205715c  checkpoint.md
ee0092cbf553a4ed317d409f7c99fbd8850a23ebcc12bd3f836aec4a0821850a  boundary_condensate_reduction.md
99262179be2586618165cfcf1ca605d8d18eb6387b728609d5299b4b8fcaadcf  boundary_condensate_check.py
65104f7890dd6c9f37f73cff256a84d7491b820c1799817084c0f86d5e0d1438  boundary_condensate_results.json
1d8d6061aff3c9dc3f7811dbe15be4deb9c17c0e29ada6fb27fa6e9125ee8d2f  report.md
```

`SHA256SUMS` is the final inventory and includes this manifest.  No cache is
retained.  No package, network, commit, push, predecessor, coordinator,
manuscript, goal, or skill file was changed.

