# Referee checkpoint: M05 shuttle comparison

## Provisional disposition

No valid objection has survived.  The frozen claim is provisionally
**ACCEPT**.

## Independent algebra audit

The product-mixture normalization is correct.  For

```text
P_*=(Q_col+sum_a P_a)/(q+1),
```

the product Poincare inequality gives

```text
gap(P_*) >= min(gamma_col,min_a gamma_a)/(q+1).
```

The half-lazy adjacent multiset chain has
`gamma_col=[1-cos(pi/m)]/(m-1)>=2/m^3`.  Since
`q+1<=m` and `delta<=1`, this is at least `2delta/m^4`.

For consecutive same-color factors at original positions `u<v`, direct
symbolic execution verifies both schedules

```text
R_u,...,R_(v-2), R_(v-1)^epsilon, R_(v-2),...,R_u.
```

Every outer move swaps disjoint-support factors in either orientation.  The
central move is the requested internal right/inverse Hurwitz generator, and
the return restores the color word.  The length is
`2(v-u-1)+1<=2m-3`.

## Recovery counterexample attempt

Fix a directed used edge with tail `w` and metadata
`(a,u,v,epsilon,s)`.  The first `s` scheduled Hurwitz maps form a fixed
bijective prefix `F_mu`; hence a charged source must equal
`F_mu^{-1}(w)`.  Two distinct sources with the same edge and metadata are
algebraically impossible.  This remains true when:

- intervening colors repeat;
- right and inverse generators have the same output;
- one physical edge is used by several stages or shuttles;
- central and outer edges collide.

Those events merely create different metadata values.  Central self-loop
generator commodities have zero Dirichlet energy and are correctly omitted.

The exact falsifier `shuttle_recovery_audit.py` found no recovery or path
failure for `(N,m)=(3,4),(4,4),(4,6),(5,6)`.  The final case contains genuine
off-diagonal shuttles across a positive disjoint component.  It also observed
duplicate oriented outputs and up to four metadata occurrences on one
physical directed edge, confirming that the proof's multiplicity accounting
rather than a uniqueness-of-edge assumption is doing real work.

## Congestion and heat-bath transfer

The metadata count is

```text
q binom(m,2) 2(2m-3)<m^4.
```

Each labeled internal reference flow is at most `pi/8`, path length is below
`2m`, and a scheduled physical oriented edge has capacity at least
`pi/[4(m-1)]`.  Thus the internal load is below `m^6`.  Direct color flow has
load at most `1/(q+1)`; adding it gives `A<=2m^6`.  Consequently

```text
gap(P_H^alpha)>=gap(P_*)/(2m^6)>=delta/m^10.
```

The original Cycle-01 padded-H3 proof was re-read.  Its factor four is the
maximum assignment multiplicity to one length-three window/output sum; its
Dirichlet coefficients are `1/[16B(m-2)M^2]` for the labeled generator sum
under `K^alpha` and `1/[8(m-1)]` under `P_H^alpha`.  Their ratio is exactly

```text
(m-1)/[2B(m-2)M^2].
```

At `m=4`, `B=2`, giving `3/(8M^2)`; the `H_4` term remains present and is
simply unused in the lower bound.

## Remaining global step

The accepted comparison is conditional only through `delta`.  It does not
prove a polynomial connected-Hurwitz gap, nor any global projection or
mean-lift bound.

