# M02 report: exact macro projection

## 1. Exact claim

For every `N>=3` and even `m>=4`, under `(pq)(x)=p(q(x))`, the stationary-flow
projection of the exact lazy `{3,4,5}` heat bath onto labeled weighted
support-component data has stationary weights (1.1)--(1.2) and transition
formula (2.1) in `proof.md`.

The fixed-first-slot square-refresh projection `S` is the exact down-up chain
(3.2), is irreducible, and satisfies

```text
gap(bar_K) >= [M/(2|R_m|(m-2)D_N)] gap(S)
           >= gap(S)/[24(m-2)],
D_N=(3N^2+N-12)/2.                                        (R1)
```

## 2. Argument

The full proof is in `proof.md`.  Fiber sizes are the multinomial color
interleaving count times independent connected-factorization counts.  Formula
(2.1) simply averages each exact conditional block count over a macro-fiber.

For (R1), deleting a fixed square gives a unique length-`m-2` core.  Inserting
source and target square edges gives the symmetric common-core count in
(3.2).  Padding the square by the third transposition turns every such move
into one actual `H_{1,3}` outcome.  Its product is a transposition, whose exact
triple-fiber size is `D_N`; comparison with the uniform `1/M` square refresh
loses at most `24(m-2)`.

## 3. Probability, runtime, path, and congestion accounting

- The specified square outcome has exact `K` contribution
  `1/[2|R_m|(m-2)D_N]`, including laziness, block-size selection, window
  selection, and uniform conditional sampling.
- `D_N<=4M`, so the comparison loses no hidden exponential factor in `N`.
- A common-core flow is exactly weighted by `W_{m-2}(gamma)/Z_m`; no lower
  bound on this ratio is assumed.
- The macro connectivity route has length at most `m` between two states via
  the repeated-edge macro.  No congestion bound is claimed; the route is not
  used for a Poincare inequality.
- Sampling an actual fixed block of `K` is polynomial by inherited exact
  samplers (brute force is already polynomial for fixed `r`).  Evaluating the
  closed macro probabilities may require Hurwitz counts and is not claimed as
  a new polynomial-time algorithm.

## 4. Dependencies

- **Proved/inherited:** macro-fiber factorization, feasible component lengths,
  exact heat-bath reversibility, and polynomial fixed-block samplers.
- **Proved here:** exact macro weights and transition formula, the common-core
  down-up formula, `D_N`, comparison (R1), and qualitative macro
  irreducibility.
- **Cited:** none beyond the inherited audited inputs.
- **Empirical:** the smoke-case macro counts below; they are not used in the
  proof.
- **Conditional:** SQUARE-DOWN-UP-GAP and every global conclusion depending
  on it.

## 5. First unproved step

**SQUARE-DOWN-UP-GAP.** There are universal `c>0,C<infinity` such that
`gap(S)>=c(Nm)^(-C)` for all `N>=3`, even `m>=4`.

## 6. Strongest self-attack

`S` acts only through words exposing a square in one fixed slot after
conditioning on a macro-fiber.  Its action rate can vary strongly between
macros, and the exact common-core weight ratio in (4.6) may be small.  A
polynomial diameter through one repeated-edge macro says nothing about
stationary-flow congestion.  Thus (R1) is a precise projection reduction, not
a projection-gap proof.  Other `r=3,4,5` outcomes may bypass a bottleneck in
`S`, so a slow `S` would not refute `bar_K` or `K`.

## 7. Calibration

- Odd `m` is empty; `m=0` and `N=2` are singletons; `m=2` is excluded.
- At `m=4`, `R_m={3,4}` and (R1) retains the exact `r=3` coefficient; the
  stronger independent whole-word bound `gap(K)>=1/4` is not discarded.
- `S_3,m=4`, `S_4,m=4`, and `S_4,m=6` have respectively 4, 13, and 17 macro
  states, matching the audited pure-Hurwitz component counts; exact target
  state counts remain 27, 120, and 3936.
- Near-minimal doubled trees supply paired representatives but are never used
  as a stationary hub.
- Formula (1.1) explicitly includes disjoint-support color interleavings.
- No edge- or vertex-parity statistic is used as an identity criterion.
- This is an actual padded `r=3` move, not an invalid internal simulation of
  a general length-two block.

## 8. Artifacts and reproduction

- `plan.md`
- `proof.md`
- `report.md`

No computation or randomness was used.  The formulas can be falsified by the
existing exact audit harness in the three smoke cases; an M14 audit is queued
before manuscript promotion.

## 9. Verdict

PROVED

This verdict concerns the exact M02 projection and comparison, not the global
mixing theorem.  The goal remains nonterminal at SQUARE-DOWN-UP-GAP and the
rejected-exit fiber gaps.
