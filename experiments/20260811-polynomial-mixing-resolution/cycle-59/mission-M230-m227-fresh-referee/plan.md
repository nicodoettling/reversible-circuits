# M230 plan: fresh immutable audit of M227

Date: 2026-08-13 UTC.

## Objective

Audit frozen M227 independently and return explicit `ACCEPT` or `REJECT`.
Verify the freeze inventory, reconstruct the degree-one-to-six atom and
first-Jacobi charge matrix, rederive the exact bandwidth primal/dual, and
check every rational certificate and strict comparison with exact arithmetic.

## Immutable source and ownership lock

M230 owns only

```text
experiments/20260811-polynomial-mixing-resolution/cycle-59/
mission-M230-m227-fresh-referee/
```

M227 is immutable. Before substantive audit work, verify its complete
`SHA256SUMS` payload inventory and expected ledger digest

```text
7b679294f7c6a4aa956a3577ae3350880698eb92d7b5776157f5f0e444e09105.
```

Refresh the project skill and source-of-truth documents. Record any conflict
rather than selecting a convenient statement.

## Clean-room audit protocol

1. Independently derive the elevated atom
   `e=(1,5/6,2/3,1/2,1/3,1/6,0)` and `M=ee^T`.
2. Independently derive the uniform degree-six fresh first-Jacobi charge
   matrix `G` from Bernstein integrals.
3. Prove the zero-coordinate six-dimensional reduction and rederive

   ```text
   p_w=min <G,C>, C-M>=0, C off-band=0;
   p_w=max <M,X>, X>=0, X=G on-band.
   ```

4. Transcribe the four M227 rational matrices only after the clean-room
   derivation is fixed. Verify band indexing and equalities, exact positive
   `LDL^T` pivots for both dual matrices and both primal slacks, endpoint
   contractions, brackets, and strict separations.
5. Independently check the generic rank-one elevation formula, positive
   homogeneity under exact `eta/pi_a`, and preservation of killed `a=d`
   deletion.
6. Freeze explicit `ACCEPT` or `REJECT`, numbered objections, a standalone
   checker/results, manifest, checksum ledger, and audit request/status.

The clean-room checker must import/read no M227 code or data. It may contain
the certificate entries under audit as independently transcribed constants.

## Required boundaries

Do not claim exact optimal values, a degree-uniform compression factor,
aggregation over retained atoms, recursive closure or contraction, all-state
control, a gap, mixing, or Terminal A/B.

