# Halfway checkpoint

## Frozen candidate statement

Let `alpha=((C_a,k_a))` be any feasible labeled weighted support-component
datum for `N>=3` and even `m>=4`, let `K^alpha` be the standard rejected-exit
restriction, and project it by stationary flow onto the multiset words with
color multiplicities `(k_a)`.  Put `M=binom(N,2)` and
`B=|R_m|` (`B=2` at `m=4`, `B=3` at even `m>=6`).  The candidate bound is

```text
gap(Kbar_color^alpha)
  >= [1-cos(pi/m)]/[B (m-2) M^2]
  >= 2/[3 m^3 M^2]
  >= 8/[3 N^4 m^3].
```

For a one-color datum the projection is a singleton, with gap convention one.

## Completed argument core

The macro-fiber is bijective with a uniform fixed-content color word and a
tuple of independent connected identity words inside the labeled support
components.  If adjacent colors differ, their actual transpositions have
disjoint support and commute.  Swap them and retain a neighboring factor in a
length-three window.  The resulting triple has the same ordered product,
stays in `alpha`, and leaves every within-color subsequence unchanged.

The exact `r=3` contribution gives every specified swap probability at least

```text
beta = 1/[2 B (m-2) M^2],
```

because `F_3(h)<=M^2`.  End pair `m-1,m` uses the window beginning at
`m-2`; every other pair uses the window beginning at the pair.  The
`r=4` whole-word heat bath at `m=4` remains in the kernel and only adds
nonnegative flow.

Comparison is to

```text
Q = (1/2)I + [1/(2(m-1))] sum_j S_j
```

on multiset words.  Thus the Dirichlet comparison factor is

```text
rho = 2(m-1) beta = (m-1)/[B(m-2)M^2].
```

The multiset walk is a quotient of the interchange process on the path.  By
Caputo--Liggett--Richthammer, its gap is at least the lazy path value
`[1-cos(pi/m)]/(m-1)`; rare colors cause no loss.

## Remaining audit before final

- Write the stationary-flow averaging formula explicitly and verify that the
  same-internal-tuple target supplies the lower bound before aggregation.
- Prove that two distinct adjacent unequal-color swaps cannot yield the same
  off-diagonal color word; in any event aggregation can only add flow.
- Record the one-edge comparison path length and congestion, exact sampler
  runtime, all calibration cases, and the two-stage JSTV restriction
  consequence.
- Red-team the distinction between this proved color projection and the still
  open fixed-color internal restrictions.

## Literature dependency

Caputo, Liggett, and Richthammer, *Proof of Aldous' spectral gap conjecture*,
Theorem 1.1, identifies the interchange-process and single-particle gaps on
every weighted graph.  For the unit-rate path the latter eigenvalue is checked
directly as `2(1-cos(pi/m))`; the discrete half-lazy normalization is done in
the proof rather than imported.
