# M47 plan: original-K branch-geometry red team

Date: 2026-08-11

## Exact target and convention

Permutations are maps on `[N]`; `(pq)(x)=p(q(x))`, and a word evaluates as
`t_1...t_m`.  The target law is the uniform law `pi` on

```text
Omega(N,m)={w in T_N^m:t_1...t_m=id}.
```

The reviewed kernel is

```text
K=(1/2)I+(1/(2|R_m|)) sum_(r in R_m)
       (1/(m-r+1)) sum_i H_(i,r),
R_m={r in {3,4,5}:r<=m},
```

with each `H_(i,r)` the exact uniform same-product heat bath.  The principal
sector here is `N>=3`, `m=2N-2`, and the minimal connected full-support macro
`F_N`.

The mission seeks either a literal Terminal-B cut based on global geometry of
the prefix join tree, with global mass orientation and complete `H3+H4+H5`
boundary flow, or a rigorous inverse-polynomial rejection of the strongest
branch family that can be completely counted.

## Work program

1. Prove the common-forest lemma: an `r`-window replacement leaves a common
   outside join forest and replaces at most `r` join-tree edges.  Audit what it
   does and does not imply for centroid, height, diameter, and pendant-branch
   statistics.
2. Test the named pointwise premise that every path/centroid-extreme join tree
   has an immediate branch-changing Hurwitz (hence padded-`H3`) move.  Small
   exact computation, if used, is only a falsifier of this premise.
3. Select the strongest family admitting exact mass and overlap accounting.
   Preferred candidates are path/diameter-extreme trees or a canonical
   largest-pendant-branch threshold; fixed-leaf, star, two-lobe, separator,
   prefix-renewal, and area cuts are excluded as inherited work.
4. For a surviving candidate, count or inject the entire smaller side into
   its true full-`K` boundary with polynomial multiplicity.  Include updates
   leaving `F_N` and exact block/window/fiber normalization.
5. If this fails, freeze the exact structural obstruction and state the first
   standalone stationary branch-shell proposition, rather than inferring a
   bottleneck from locality or finite data.

## Candidate claims the computation may falsify

- **P1 (pointwise path action):** every `w in F_N` whose prefix join tree is a
  labeled path has an adjacent Hurwitz move whose new join tree is not a path.
- **P2 (centroid-shell action):** every `w in F_N` whose join tree has a unique
  centroid and a branch of size in `[floor(N/2)-2,floor(N/2)]` has an adjacent
  Hurwitz move changing that largest branch size.
- **P3 (bounded tree-weight distortion):** all labeled join-tree fibers in
  `F_N` have sizes within a fixed polynomial factor in `N`.

Any bounded result is reported only as a counterexample or calibration; it is
not an asymptotic theorem without a separate completeness argument.

## Expected failure modes

- One local edge exchange can change a global branch statistic by order `N`,
  so edge-count locality is not scalar Lipschitz locality.
- The prefix join tree is not uniform Cayley and is not a Markov lumping.
- Pointwise macro escape is false in `F_6`; a branch cut may concentrate on
  zero-exit states.
- A small conditional side inside `F_N` must still be oriented against the
  global complement in `Omega(N,2N-2)`.
- Short paths through a canonical tree can have exponential congestion.

## Deliverables

`checkpoint.md`, any compact exact falsification artifact with fixed command
and metadata, and a final nine-field `report.md`.  No shared durable file is
modified.
