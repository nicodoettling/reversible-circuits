# M12 Cycle 02 Plan: High-Surplus and Dense Thresholds

## Exact target

Continue the adversarial analysis of the uniform fixed-length law on

```text
Omega(N,m) = {(t_1,...,t_m) in T_N^m : t_1...t_m=id}
```

for the exact lazy random-scan `{3,4,5}` same-product heat-bath kernel.  Maps
compose as `pq=p after q`.  All factors from laziness, block-size choice,
window choice, and exact conditional-fiber sampling remain explicit.

For support components `C`, define

```text
G(w) = sum_C (k_C-2(|C|-1))/2.
A_{<=g} = {w : G(w)<=g}.
```

The cycle seeks either:

1. universal `c>0,C<infinity` with
   `Q(A_{<=g},A_{<=g}^c)/min(pi sides) >= c(Nm)^(-C)` for every nontrivial
   total-surplus threshold, with `C` independent of `g`, including dense
   `m>2(N-1)`; or
2. an explicit infinite threshold family with superpolynomially small
   two-sided conductance, including exact stationary mass and complete
   boundary flow.

Neither outcome alone settles the global spectral-gap question unless it
meets the literal terminal criteria.

## Work program

1. Rewrite total surplus exactly in terms of the number of support components,
   including isolated labels, and classify how inserting or refreshing an
   adjacent square changes that statistic.
2. Audit general simple Hurwitz-number recursions and connected/disconnected
   exponential formulas for a uniform-in-genus bridge-square ratio.  Fixed-
   genus polynomiality will not be extrapolated to growing genus.
3. Derive exact adjacent-layer stationary-flow identities by deleting a square
   at a fixed slot.  Test whether reversibility and the global square-frequency
   lemma control cumulative threshold mass without a hidden exponentially
   small boundary-layer ratio.
4. Search for a counterexample among regimes where genus grows with `N,m`,
   especially full-support dense bridges and transitions between one giant
   support component and fragmented support.
5. If finite exact arithmetic is useful, compute only layer counts and exact
   square-refresh boundary terms tied to a named universal inequality.  Record
   deterministic commands, environment, and machine-readable output; finite
   values may falsify but not prove an asymptotic statement.

## Required audits and calibration

- Preserve the Cycle-01 correction for the `A_2` nonemptiness witness.
- Use the JSTV stationary-flow projection/rejected-exit formulation; do not
  revive a constant-one mean-lift claim.
- Incorporate M13's proof that doubled-tree and midpoint-mountain cuts have
  inverse-polynomial escape, without rediscovering those cuts.
- Check odd `m`, `m=0`, `m=2`, `N=2`, all three exact smoke cases, the whole-
  word `r=4` update at `m=4`, disjoint-component color interleavings, and dense
  full-support states.
- A rare layer is not a bottleneck without its smaller-side mass and full
  boundary flow.

## Deliverables

- `checkpoint.md`: genuine halfway conclusion from the recursion/flow audit.
- Proof notes and, only if needed, reproducible exact-count artifacts.
- `report.md`: the required nine-field schema and exact verdict.
