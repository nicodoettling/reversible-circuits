# M59 halfway checkpoint: exact fixed-tree automaton and bounded red team

## Exact characterization proved

Fix `N>=2`, a labeled tree `T` on `[N]`, and `m=2N-2`.  With
`(pq)(x)=p(q(x))`, scan an ordered transposition word from left to right.  A
prefix state is `(p,S)`, where `p` is the prefix product and `S` is the set of
join edges already accepted.  Since `S` is a forest contained in `T`, the
next transposition `e={a,b}` is allowed exactly when either

1. `a,b` lie in the same component of `(V,S)`, in which case `S` is unchanged;
   or
2. `e` is an unused edge of `T` joining two components, in which case
   `S` becomes `S union {e}`.

The fixed join-tree fiber `F_N(T)` is exactly the set of length-`m` automaton
paths from `(id,empty)` to `(id,E(T))`.  Necessity follows from the definition
of the first graph-component joins.  Conversely, every cross-component step
accepted by the automaton is a distinct edge of `T`; reaching `E(T)` makes
these precisely the `N-1` join edges, while the endpoint condition gives an
identity word.

For a block length `r`, position `i`, outside prefix/suffix, and block product
`g`, the fixed-fiber words form a conditional bucket.  The literal rejected-
exit restriction is the union of these bucket cliques, with every ordered
target in the global length-`r` product fiber weighted

```text
1 / [6 (m-r+1) |F_r(g)|].
```

Thus, if a bucket contains `b` fixed-tree words and `a` words in a candidate
side `A`, its exact directed boundary contribution is

```text
full K:         [1/(6(m-r+1))] a(|F_r(g)|-a)/|F_r(g)|,
rejected exit:  [1/(6(m-r+1))] a(b-a)/|F_r(g)|.
```

These formulas retain laziness, uniform block-size choice, uniform window
choice, conditional-fiber multiplicity, and all `r=3,4,5` outcomes.

## Exact bounded falsification

The N=4 exhaustive calculation covers all 16 labeled trees and all 3,936
identity words.  Every fixed-tree restriction is connected; star fibers have
size 186, path fibers size 178, and maximum support-graph diameter is 2.

The new dynamic-programming/bucket calculation covers the three unlabeled
N=5 tree shapes.  Conjugation equivariance therefore covers every one of the
`5^3=125` labeled trees.  It reproduces the independently known exact fixed-
tree weights and finds one component in every case:

| shape | fiber size | components | minimum tested full-K escape | minimum tested restriction escape |
|---|---:|---:|---:|---:|
| star | 8,856 | 1 | 0.392878 | 0.000842605 |
| path | 7,808 | 1 | 0.381385 | 0.00200936 |
| T | 8,254 | 1 | 0.386357 | 0.00192674 |

The tested statistics are the rank and time of a canonical join edge, leaf
strand null separation, midpoint join count, and midpoint largest accepted
component.  The weakest restriction cut is the N=5 star event that the
canonical edge has join rank at most 2: its conditional side has exactly
4,428 of 8,856 states and restriction escape

```text
110972985703459 / 131702333737927680 = 0.0008426045503816381...
```

but its full-K escape is

```text
2267545133196643259 / 5487597239080320000 = 0.413212747657236...
```

so tree-changing moves overwhelmingly bypass this apparent internal
chronology boundary.  The global bridge has 1,770,940 states at `(N,m)=(5,8)`;
every tested side is globally below mass one half.

## Interpretation and remaining gap

The exact calculations could have falsified universal fixed-tree restriction
irreducibility, or exposed a bounded instance of a zero-flow chronology cut.
They did neither.  They cannot prove universal connectivity or a polynomial
gap.  In particular, the N=5 restriction escape near `8.4e-4` is a finite fact,
not asymptotic evidence.

The smallest analytic gap is now the following standalone proposition.

**FIXED-TREE LEAF-STRAND LOCALIZATION.** There are universal constants
`c>0,C<infinity` such that, for every `N>=4`, every labeled tree `T`, every
leaf `v` of `T`, and every deleted base word/null-position cell in the exact
leaf-strand decomposition of `F_N(T)`, the literal rejected-exit
`{H3,H4,H5}` dynamics mixes the at most `(N-1)^2` insertion histories and
communicates between neighboring null-position cells with comparison loss at
most `c^{-1}N^C`; moreover the induced base-word mean-lift Dirichlet form
dominates the `F_{N-1}(T-v)` restriction form with the same universal
polynomial loss.

An induction that pays a fresh polynomial factor at every deleted leaf is not
enough; the loss must be organized without exponent accumulation.  A slow
rejected-exit restriction alone also does not refute global `K`, as the exact
full-flow calculation demonstrates.

## Artifacts

- `fixed_tree_restriction_audit.py`, `fixed-tree-N4.json`
- `fixed_tree_dp_bucket_audit.py`, `fixed-tree-N5-all.json`
- exact commands are recorded in the final report; no random seed or
  nonstandard dependency is used.

