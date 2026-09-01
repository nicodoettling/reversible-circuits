# Fresh referee report on M59 fixed-join-tree chronology theorem

Date: 2026-08-11. Frozen M59 report SHA-256:
`83f7e67ad04a75139de723f10546ad9842789c864008b458a3a24e6079156afc`.
Convention `(pq)(x)=p(q(x))`; factor tuples multiply left-to-right.

## Verdict

**ACCEPT.** Numbered objections: none.

This acceptance is only for M59 Claims 1--3 in their literal scoped form.
It is not acceptance of a universal fixed-tree restriction gap, a mean-lift
bound, Terminal A, or Terminal B.

## Audit

1. **Automaton and literal restriction.** A prefix factor either stays
   inside one component of the used join-edge forest or is an unused edge
   of `T` joining two components. This is necessary and sufficient for the
   prefix join tree to be `T`. Fixing outside word, block product, length,
   and position gives a literal conditional clique. Rejected exits retain
   the global denominator `|F_r(g)|`; they are not renormalized by the
   number of fixed-tree outcomes. The per-outcome coefficient

   ```text
   1/[2|R_m|(m-r+1)|F_r(g)|]
   ```

   is correct.

2. **Chronology source fraction.** Choose a leaf `v` whose incident edge
   `f` differs from the distinguished edge `e`. The accepted strand
   deletion map has exactly two null increments and fibres of size at most

   ```text
   Lambda_N=binom(m,2)(N-1)^2.
   ```

   Hence `|A|<=Lambda_N|Del_v(A)|`. For every image `z`, the canonical
   source `zff` lies in every low join-rank side because deletion can only
   lower `rho_e` by one, while putting `f` last does not restore it. The
   source `ffz` lies in every high side: prepending `f` restores the lost
   rank if `f` preceded `e`, and otherwise raises it. For factor position,
   deletion subtracts `k in {0,1,2}`; appending leaves `j_e-k<=j_e`, and
   prepending gives `j_e-k+2>=j_e`. Distinct bases give distinct sources.
   This proves the exact `1/Lambda_N` source fraction in both orientations.

3. **Literal H3 exit and normalization.** If `c` is the last factor of
   `z`, then

   ```text
   cff -> css,
   ffc -> ssc,
   ```

   for any transposition `s` supported off `v`. Each replacement has the
   same ordered product `c` and produces a word omitting `v`, hence outside
   the global cut. The length-three fibre over a transposition has

   ```text
   D_N=binom(N,2)+6(N-2)+2binom(N-2,2)
      =(3N^2+N-12)/2.
   ```

   I independently enumerated `D_N=9,20,34,51,71` for `N=3,...,7`, matching
   the formula. Laziness, block-length choice, window scan, and target
   heat-bath denominator give exactly

   ```text
   p_0=1/[2|R_m|(m-2)D_N].
   ```

   At `N=3,m=4`, `|R_m|=2`; for `N>=4`, `|R_m|=3`. No factor of three or
   whole-word `H4` contribution is lost. `H4/H5` are simply retained as
   additional nonnegative flow in the analytic bound.

4. **Global mass orientation.** For every labeled tree `T` on `N>=3`, a
   relabeling sends it to a distinct labeled tree `T'`. Conjugation bijects
   `F_N(T)` and the disjoint fibre `F_N(T')`. Therefore every subset
   `A subseteq F_N(T)` has global uniform mass at most one half, so
   `min(pi(A),pi(A^c))=pi(A)`. Target collisions are irrelevant because the
   lower bound sums exit probabilities over distinct sources. Thus

   ```text
   Phi_pm^K(A)>=1/[2|R_m| Lambda_N (m-2)D_N]
               >=1/(48N^7)
   ```

   with the stated integer and small-`N` conventions.

5. **N=5 artifact scope.** The DP enumerates exactly every positive
   completion of the prefix automaton for one star, path, and T-shaped
   labeled representative. Its clique DSU uses every `r=3,4,5` bucket and
   the unrenormalized global product-fibre size. Conjugation equivariance
   transfers connectivity to every labeled tree of the same shape. The
   counts

   ```text
   5(8856)+60(7808)+60(8254)=1,008,000
   ```

   cover all `125=5^3` labeled trees and agree with the exact minimal
   full-support total. Thus the report may claim N=5 connectivity for all
   fixed labeled tree restrictions. The named flow values are only for the
   three representatives/statistics actually tabulated and are correctly
   labelled bounded exact facts. They are not asymptotic evidence.

6. **Boundary calibration.** For `N=3`, a leaf with `f!=e` always exists;
   the base is the singleton `N=2` minimal sector and the same H3 exit works.
   The theorem neither uses `m=2` simulation nor discards whole-word `H4`.
   The N=4 artifact exhausts all 3,936 identity words and all 16 labeled
   tree fibres; its reported minimum exact flows agree with a fresh parse of
   the JSON.

## Accepted scope and remaining step

M59 rigorously excludes join-rank and join-position threshold cuts as
full-`K` bottlenecks at minimal full-support length, with polynomial global
conductance. It does not control cuts internal to every deletion cell. Its
named remaining proposition, FIXED-TREE LEAF-CELL EXPANSION, is therefore
correctly left open.

ACCEPT
