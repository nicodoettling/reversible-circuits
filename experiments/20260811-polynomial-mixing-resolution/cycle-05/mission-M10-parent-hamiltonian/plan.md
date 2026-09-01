# M10 coordinator plan: exact bridge parent-Hamiltonian algebra

## Target

For `E=T_N^2` with product map `p:E->A_N`, let `Pi_i` be uniform
conditional averaging of `(A_i,A_(i+1))` at fixed ordered product and set

```text
H_l=sum_(i=1)^(l-1)(I-Pi_i).
```

Prove an inverse-polynomial lower bound on the smallest positive eigenvalue of
every fixed-total-product sector for `l<=C_0Nlog(N+1)`, or identify the exact
standalone estimate still missing after the parent-Hamiltonian reduction.

## Exact algebra to establish

1. Map increments to prefix vertices and show `Pi_i` is the one-vertex
   heat bath for the `Q=P_T^2` Markov bridge, retaining ordered pair labels.
2. Show the unconstrained Hilbert space decomposes orthogonally by total
   product and that the zero space in each feasible sector is one-dimensional.
3. Express interval ground-space projections and adjacent-interval angles in
   terms of exact convolution kernels/endpoint tilts.
4. Audit whether a martingale, detectability, or block-normal MPS theorem
   gives a gap with constants polynomial in `N,l`; reject factorial bond
   dimension, `1/min Q^r`, and an unproved base-block gap.
5. Test any proposed local overlap identity on `N=3,4` and on sparse/minimum
   endpoint configurations before stating it universally.

## Known traps

The M10 two-block recursion already controls long lengths but leaves the same
`O(NlogN)` base.  A parent-Hamiltonian theorem that multiplies by
`gap(H_r)` at `r=O(NlogN)` has not advanced the frontier.  Pairwise projector
angles alone need not imply a global gap.  Full-support uniform increments
are a commuting special case and cannot be generalized without accounting
for zeros of `Q`.  No fixed canonical normal form may carry the flow.

## Deliverable

Maintain `checkpoint.md` and `report.md` with the required nine fields:
exact claim; proof; probability/runtime/path/congestion; labeled dependencies;
first unproved proposition; strongest self-attack; calibrations;
artifacts/reproduction; and one of `PROVED`, `REFUTED`, or
`OPEN AT A NAMED STEP`.  Any computation must name the universal identity it
could falsify.

