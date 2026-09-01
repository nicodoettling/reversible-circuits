# Cycle 06 M23 plan: lower-density support coverage

## Exact target and convention

Use `(pq)(x)=p(q(x))`; words evaluate as `t_1...t_m`.  The target is the
uniform bridge law on `Omega(N,m)`, and `K` is the exact lazy same-product
heat bath with block sizes `{3,4,5}`, uniform block/window scans, and exact
conditional fibers.

For `X(w)` equal to the number of unused labels, study

```text
T_q={X>=q},   1<=q<=N-2,
U=T_1,
```

in the remaining interval below the cycle-06 M21 threshold.  Seek a literal
superpolynomial full-`K` bottleneck; failing that, prove a uniform
inverse-polynomial bound on a new growing-surplus subrange.

## New subrange lane

Let `A>=1` be the audited parity-aware pointwise return constant and define

```text
B_*=32(A+1)=C_*/8.
```

Re-prove the bridge disconnected-support estimate directly at
`j>=B_*N log(N+1)`, retaining:

1. the probability `(L/M)^j` of avoiding a fixed vertex cut;
2. the `Bin(j,alpha)` allocation to its larger side;
3. the parity-zero cases and the exact subgroup return probability;
4. every cut multiplicity and the global even-return denominator.

The target is a rigorous bound `delta_N(j)<1/4`, rather than the much smaller
M21 error.  This is enough to orient every `T_q` and to make exact-support
safe-square incidence polynomial.  Combine it with exact factorial moments
to show that `X=q` carries a constant fraction of `T_q`, then use one actual
`H_3` refresh and retain all `r=4,5` flow.

## Red-team checks

Audit whether the proof fails because of a hidden factorial subgroup-return
loss, parity, the balanced cut, or a small used set.  Failure of the
sufficient estimate is not a bottleneck.  Record the strict residual interval
below `B_*N log(N+1)`.

## Calibration and deliverables

Handle empty/singleton/excluded cases, `27/120/3936`, `m=4` whole-word
`H_4`, near-minimal doubled trees, exact orientation, and all kernel factors.
Write `checkpoint.md` and the required nine-field `report.md`.  Any
computation may only falsify a named claim and must be reproducible.
