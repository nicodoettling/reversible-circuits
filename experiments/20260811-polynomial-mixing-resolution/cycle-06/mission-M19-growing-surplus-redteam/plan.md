# Cycle 06 M19 plan: growing-surplus full-K red team

## Exact target and convention

Use `(pq)(x)=p(q(x))`.  The target is uniform on

```text
Omega(N,m)={t in T_N^m:t_1...t_m=id}
```

and `K` is exactly the lazy `{3,4,5}` same-product heat-bath kernel from
`GOAL_SPEC.md`, with its block-size and window normalizations retained.

Seek a superpolynomial-conductance cut in a growing-surplus regime.  If none
survives, rigorously reject a named refinement of the unresolved component
phase and retain exact smaller-side stationary orientation and all `r=3,4,5`
flow.

## Primary named cut

For a fixed label `v`, define

```text
A_v={w in Omega(N,m):no factor contains v}.
```

This is the exact isolated-label refinement of the disconnected side.  Its
mass is `Z_(N-1,m)/Z_(N,m)`, where `Z_(d,k)=|Omega(d,k)|`; orient the cut by
choosing `A_v` or its complement according to whether this exact ratio is at
most one half.

The proposed escape proof is:

1. Conditional on `A_v`, the state is uniform on `Omega(N-1,m)`.
2. Count adjacent equal pairs exactly by deleting a marked square.  Use the
   regular-character formula to prove even return probabilities decrease in
   time, yielding a square with probability at least
   `1/binom(N-1,2)`.
3. Pad the first square on its available side to an actual `H_3` window and
   replace it by a square containing `v`.  Track laziness, block-size scan,
   window scan, and conditional fiber size.
4. Divide the exact global stationary flow by the oriented smaller mass.
   The `r=4,5` contributions are retained as nonnegative flow.

## Secondary counterexample lanes

- Audit whether the connected bottom layer `F_(N,g)` could become a phase
  cut when `g` grows, without assuming component-count unimodality.
- Examine minimum full-cycle Hurwitz fibers for nonnormal internal cuts, but
  require stationary mass and complete local boundary flow.  Slow traces,
  a unique macro, or a rare canonical state are nonresponsive.

## Calibration and failure modes

Handle odd/zero/`m=2`, `N=2`, `m=4` whole-word `H_4`, and the 27/120/3936
cases.  Do not infer Terminal B from slow auxiliary `B`, pendant-square decay,
or fixed-genus estimates.  A fixed-label cut can be exponentially rare and
still fail as a bottleneck; its conductance must use the exact smaller side.

## Deliverables

Write a genuine `checkpoint.md` and final nine-field `report.md`.  Any
bounded computation must name the universal statement it can falsify and
include commands, metadata, and exact output.
