# M02 coordinator plan: exact macro projection

## Target

Define the JSTV stationary-flow projection under labeled weighted
support-component data, including exact stationary weights and the exact
`r=3,4,5` transition formula.  Isolate a quantitatively useful family of
projected moves with all kernel normalizations.

## Conventions and scope

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and words evaluate as
`t_1...t_m`.  The target is uniform on `Omega(N,m)` for `N>=3`, even `m>=4`.
The kernel is exactly the half-lazy random scan in `GOAL_SPEC.md`.

This mission may prove an exact reduction but cannot be terminal without a
polynomial projection gap and the other global obligations.  A macro diameter
through the repeated-edge state will be recorded only as connectivity.

## Falsification checks

- exact state and macro counts in `S_3,m=4`, `S_4,m=4`, `S_4,m=6`;
- the whole-word `r=4` term at `m=4`;
- disconnected component interleavings in the macro weight;
- fixed-block product and heat-bath fiber normalization;
- distinction between stationary flow and a conditional proposal rate.
