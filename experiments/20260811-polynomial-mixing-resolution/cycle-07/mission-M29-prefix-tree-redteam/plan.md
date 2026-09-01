# M29 plan: prefix-height and join-tree red team

## Exact target and convention

Permutations are maps on `[N]`, with `pq` meaning `p` after `q`:
`(pq)(x)=p(q(x))`.  Put `m=2(N-1)` and

    F_N={w=(t_1,...,t_m): t_1...t_m=id and the support graph is connected}.

The ambient target is uniform on `Omega(N,m)`.  The exact chain is

    K=(1/2)I+(1/(2|R_m|)) sum_{r in R_m} 1/(m-r+1) sum_i H_{i,r},
    R_m={r in {3,4,5}:r<=m},

where `H_{i,r}` is uniform on the length-`r` transposition fiber with the
same ordered product.  All conductance calculations will use the smaller
side in the full `Omega(N,m)` law and include every `r=3,4,5` contribution.

The literal goal is either a superpolynomial-conductance cut proving
TERMINAL B, or a rigorous polynomial shell/action rejection of a natural
prefix-height or join-tree cut.  Results only for the Hurwitz subchain are
explicitly nonterminal.

## Candidate statistics

For `X_j=t_1...t_j`, let `h_j=N-cycles(X_j)`.  In `F_N`, inherited proved
facts give a Dyck excursion of semilength `N-1`; its join factors form a
labeled spanning tree.  The first candidates are:

1. the Dyck area `A(w)=sum_j h_j`, oriented at an exact median;
2. a midpoint-height or maximum-height threshold;
3. a label-symmetric join-tree statistic (centroid balance or a prescribed
   broad degree/shape event), only if its stationary mass can be counted.

Previously rejected midpoint-articulation, adjacent doubled-tree,
`N`-cycle mountain, star, fixed canonical hub, and fixed balanced-separator
families will not be reused.

## Work program

1. Prove deterministic full-heat-bath locality: an `r`-window changes only
   the `r-1` internal prefix permutations and hence changes area, midpoint
   height, and related Lipschitz statistics by explicit constants.  Convert
   this into an exact shell containment for all `r=3,4,5` and retain the
   kernel normalization.
2. Audit whether the minimal-factorization/Hurwitz-tree bijection supplies
   an exact marginal distribution or enough uniform shell bounds.  Do not
   assume the Dyck path or join tree is a Markov lumping; exact `S_3,m=4`
   and `S_4,m=6` already refute that shortcut.
3. If an exact law is available, calculate the cut mass and complete
   two-sided full-`K` boundary flow.  If not, identify the precise weighted
   shell ratio proposition needed and attack it by injection, recurrence, or
   a named finite falsifier.
4. Record a genuine halfway checkpoint after deterministic locality and the
   first stationary-law audit.  Freeze a nine-field final report with scoped
   verdict only.

## Expected strongest failure modes

- `F_N` is only one macro-fiber of `Omega(N,m)`; a cut defined solely inside
  it is not automatically correctly oriented or large in the global law.
- Locality gives only an upper bound on boundary support, not a lower bound
  on shell mass or action probability.
- The Dyck path, join tree, degree profile, and Pruefer coordinates are not
  exact lumpings, and the join tree is not uniform.
- A slow Hurwitz statistic may be crossed efficiently by the `r=4,5` heat
  baths.
- Any median shell may have only polynomially small mass, which would reject
  rather than prove a bottleneck; proving that requires exact weighted-path
  enumeration rather than ordinary Catalan heuristics.

## Calibration obligations

Audit odd `m`, `m=0`, `N=2`, excluded `m=2`, `S_3,m=4` (27 words and four
Hurwitz components), `S_4,m=4` (120/13), `S_4,m=6` (3936/17), the whole-word
`H_4` at `m=4`, minimal doubled-tree words, ordered interleavings, failure of
parity-only invariants and of `L=2` simulation, and exact smaller-side mass.

