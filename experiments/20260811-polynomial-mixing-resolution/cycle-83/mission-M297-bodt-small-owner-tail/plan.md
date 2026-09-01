# M297 plan: exact small-owner decorated tail (BODT)

## Objective

Independently attack the exact small-owner tail `(BODT)` isolated by the
M290/M293 decorated-owner reduction.  The target is the lag-vector estimate

```text
sum_l |eta(Delta Q_l)| = O(1/k)
```

for the already-combined signed positive-composition vector restricted to
triangle/side/negative states whose residual owner is at most `(k-1)/2`.
All channel weights `omega(s)`, the triangle factor `1/3`, the side/negative
factor `1/4`, owner seams, topology kinds, and phases remain inside the signed
sum.

## Target and status discipline

The ambient target is the fixed-length uniform identity bridge law on
`Omega(N,m)` for the lazy exact same-product `{3,4,5}` heat-bath kernel in
`GOAL_SPEC.md`.  This mission addresses only the analytic `(BODT)` sublemma.
It will not infer PBV/FD/FCL1, a gap, mixing, or a terminal outcome.

## Inputs to verify

Read the frozen M261/M264, M267/M270, M276/M279, M282/M286, M289/M292, and
M290/M293 artifacts, including hashes, conventions, and referee caveats.
Reconstruct the exact signed coefficient vector from the definitions rather
than from a prose paraphrase.

## Method

1. Freeze the exact owner/topology/phase coefficient table and state the
   small-owner restriction without taking triangle inequalities across source
   laws, T/D, or IS/IN/X.
2. Select one analytic candidate after that reconstruction and before any new
   finite-rank calculation.  Preferred candidate: a signed first-difference
   or Abel/telescoping identity in the residual-owner coordinate, with boundary
   terms kept explicitly.
3. Test the chosen identity symbolically from the accepted formulas.  Use at
   most one compact new rank only as a falsification/calibration check.
4. If the full estimate does not close, freeze the first strict scalar
   coefficient lemma or an exact obstruction, with the smallest unresolved
   implication stated standalone.

## Failure modes

- silently discarding channel or topology coefficients;
- applying absolute values before source-law or phase cancellation;
- confusing the collision-vector `(CIBV)` estimate with decorated `(BODT)`;
- invoking DSR/DTR without an all-rank proof;
- promoting a `k=9` finite row into an asymptotic theorem.

## Deliverables

- `checkpoint.md` (initial and halfway checkpoints),
- `proof.md` with the exact coefficient reduction and proof/obstruction,
- optional one-rank exact script and machine-readable output,
- `report.md`, `freeze_manifest.md`, and `SHA256SUMS`.

