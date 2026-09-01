# Cycle 03 M10 plan: two-overlapping-block bridge recursion

## Exact model

Use `(pq)(x)=p(q(x))`.  Pair a length-`2n` transposition word into
`Y_j=t_{2j-1}t_{2j}`.  With `P_N` uniform on the
`M=binom(N,2)` transpositions and `Q_N=P_N^2`, the prefix path
`X_0=e, X_j=Y_1...Y_j, X_n=e` has weight proportional to

```text
product_{j=1}^n Q_N(X_{j-1}^{-1}X_j),
```

including `a_N(y)=M^2Q_N(y)` uniform ordered-transposition
microfactorizations of each increment.  The aligned chain is

```text
B=(1/(n-1)) sum_{j=1}^{n-1} H_j,
```

where `H_j=H_{2j-1,4}` is the exact conditional expectation that refreshes
`X_j` and both adjacent microfactorizations.  Define the continuous-time
Hamiltonian

```text
mathcal H_n=sum_{j=1}^{n-1}(I-H_j),
```

so `gap(B)=gap(mathcal H_n)/(n-1)`.  The inherited full-chain comparison is
`gap(K_{N,2n})>=gap(B)/12` for `n>=3`; `m=4` is handled separately by the
whole-word heat bath.

## Targeted theorem and red team

1. Define the worst fixed-endpoint subinterval gap `Lambda_N(l)` including
   all microfactor labels.
2. Cover a length-`n` bridge by two intervals of equal length `L`, overlap
   `s`, and prove the operator comparison

   ```text
   mathcal H_n >= Lambda_N(L) [I-(P_left+P_right)/2].
   ```

3. Identify the two-projection gap as `(1-rho)/2`, where `rho` is the
   maximal correlation of the two outside tails.  Reduce `rho` exactly to
   the two prefix endpoints surrounding the overlap.
4. Use random-transposition character estimates to prove a uniform relative
   bound for `Q_N^s` at `s=O(N log N)`, with alternating-group parity and
   endpoint tilts explicit.  Convert it into a universal angle bound.
5. Iterate only at geometric scales, with one universal constant loss per
   scale and no hidden factor `n` at each recursion.
6. Seek an endpoint-conditioned family with angle tending to zero.  In
   particular test whether a sublinear overlap is ruled out by the standard
   representation even when both outside tails have mixed.
7. If the recursion stops at length `O(N log N)`, state the exact uniform
   fixed-endpoint base-gap proposition and try a separate local comparison;
   do not claim that the recursion itself proves it.

## Expected failure modes and calibration

- Total-variation mixing alone is insufficient; the endpoint tilts require
  a relative or operator bound.
- Scalar Dobrushin and the two-type synchronous coupling are already
  refuted and will not be reused.
- A worst-subinterval gap must range over every feasible endpoint, not only
  the identity bridge.
- Large block projections must refresh microfactors as well as prefix
  vertices.
- Odd `m`, `m=0`, `N=2`, and `m=2` are boundary/excluded cases.  At `m=4`
  retain the whole-word update.  Check `S_3,m=4`, `S_4,m=4`, and `S_4,m=6`
  against exact inherited counts.
- A slow angle for the auxiliary `B` is not Terminal B for `K`; only a gap
  proof transfers in the useful direction.

## Deliverables

- `checkpoint.md`: exact two-block operator recursion and angle audit.
- `report.md`: the required nine-field schema, including the base-scale gap
  if it remains open.
- Compact exact artifacts only if a named finite angle claim needs
  falsification.
