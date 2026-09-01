# Cycle 06 M21 plan: missing-support union and coverage thresholds

## Exact target and convention

Use `(pq)(x)=p(q(x))`; words evaluate as `t_1...t_m`.  The target is the
global uniform law on `Omega(N,m)`, and `K` is the exact lazy same-product
heat bath with block sizes `R_m={r in {3,4,5}:r<=m}`, uniform block-size and
window scans, and exact conditional fibers.

Let

```text
X(w)=#{v in [N]:v occurs in no transposition factor},
U_(N,m)={X>=1}.
```

The terminal red-team target is a correctly oriented infinite family for
which the full-`K` conductance of `U`, or of a missing-label threshold, is
superpolynomially small.  If that fails, prove an inverse-polynomial escape
theorem in a genuinely growing regime while accounting for the overlaps
among the fixed-label events exactly.

## Primary proof lane: factorial moments plus safe squares

1. Write the exact inclusion-exclusion mass of `U` and exact support-layer
   weights.  Use exchangeability to compute the first two factorial moments
   of `X` from `Z_(N-1,m)` and `Z_(N-2,m)`.
2. In the parity-mixed regime `m=Omega(N log N)`, use the audited
   Diaconis--Shahshahani relative return estimate to prove that the
   exactly-one-missing layer carries a constant fraction of all of `U`.
   This step handles overlaps directly; no union bound of fixed-`v`
   conductances is permitted.
3. Conditional on exactly one missing label, count **safe** adjacent squares
   whose deletion leaves exact support on the other `N-1` labels.  The
   insertion/deletion incidence is exact.  Refresh such a square in a
   boundary-safe `H_3` window to an edge containing the missing label.
4. Prove from the same parity-mixed support estimate that `U` itself is the
   smaller side.  Write the full stationary flow as the sum of its
   `r=3,4,5` contributions and retain the latter two as nonnegative terms.

## Counterexample and threshold audit

Below `O(N log N)`, inspect what fails in the argument: a small one-missing
layer, a low density of safe squares, or only an unavailable mass
orientation.  Do not interpret failure of either sufficient condition as a
bottleneck.  Record the exact remaining coverage-threshold proposition.

## Calibration and deliverables

Check the empty/singleton/excluded regimes, the `27/120/3936` cases, the
whole-word `H_4` term at `m=4`, and near-minimal words.  Write a genuine
`checkpoint.md` and final nine-field `report.md`.  Computation, if used, may
only falsify a named universal lemma and must include exact metadata.
