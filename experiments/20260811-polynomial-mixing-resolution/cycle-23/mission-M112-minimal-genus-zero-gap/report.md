# M112 final report: minimal genus-zero identity sector

Date: 2026-08-12. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
FINAL VERDICT: KEEP AS A STRICT REDUCTION; GAP UNRESOLVED.
PROVED HERE: exact transfer recurrence, one-level RN bound, moving-square normal form.
PROVED FROM DPS: the rooted sector is exactly UST x uniform permutation.
REFUTED: statewise one-step deletion lift and one-step rooted-product intertwining.
FIRST NONRECURSIVE OPEN STEP: ROOTED PRODUCT LOCAL COMPARISON.
```

For `d>=2`, the target is uniform on

```text
Z_d={w=(t_1,...,t_(2d-2)): t_1...t_(2d-2)=id,
                               support(w) connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed tuple factors multiply
left-to-right.  The exact auxiliary kernel is

```text
P_(0,d)=I/2+[1/(4(2d-3))]sum_(i=1)^(2d-3)(R_i+R_i^(-1)),
R_i(a,b)=(b,bab),       R_i^(-1)(a,b)=(aba,a).
```

The claimed target remains `gap(P_(0,d))>=d^(-O(1))`; it is **UNRESOLVED**.
Nothing here proves the original `{3,4,5}` heat-bath gap, all of `Gamma_0`,
polynomial mixing, Terminal A, or Terminal B.

```text
candidate                 | half-lazy signed adjacent Hurwitz on Z_d
claimed target            | uniform full-label minimal identity sector
identity ok               | exact through d=4; proved for transfer construction
crosses Hurwitz components| one connected minimal identity orbit (accepted input)
exact diagnostics         | marked deletion, transfer DP, projected flow, DPS inverse
verdict                    | strict reductions only; no gap claim
```

## 2. Exact marked-leaf transfer theorem

Mark a leaf `v` of the prefix join tree and apply accepted M49 strand
deletion.  The downstairs word `z=Del_v(w)` lies in `Z_q`, `q=d-1`.  Its two
null increments determine an interval `0<=a<=b<=2q-2`.  While this interval
is open, track the predecessor coordinate `c in [q]` of `v`.

For base factor `s_r=(x,y)`, define a `q x q` transfer matrix

```text
T_r = permutation matrix of (x,y),                  at a support join,
T_r = I with its {x,y} block replaced by all ones,  at a cycle cut.
```

The M49 insertion table gives a bijection between leaf lifts for interval
`[a,b)` and paths through these matrices.  Therefore

```text
L_(a,b)(z)=1^T T_a...T_(b-1)1,
L(z)=sum_(0<=a<=b<=2q-2)L_(a,b)(z).                  (2.1)
```

This is **PROVED**, including injectivity, surjectivity, endpoint identity,
and the leaf condition.  Every interval has at least `q` forced lifts; M49's
fixed-null theorem gives at most `q^2`.  Since there are `binom(2q,2)`
intervals,

```text
q binom(2q,2) <= L(z) <= q^2 binom(2q,2),
max_z L(z)/min_z L(z) <= q.                          (2.2)
```

Thus the raw marked-deletion pushforward has only polynomial one-level
Radon--Nikodym distortion.  It does not prove a recursive gap: multiplying
`q` through all deletion depths is factorial.

M60's null-pushing identities are literally signed Hurwitz moves here.  They
prove that every fixed `(v,z)` state reaches, in `O(d)` physical moves, a
moving-square normal form

```text
z (v,a)(v,a)                                             (2.3)
```

for some uncontrolled `a`.  The square crosses one base factor in two moves,
`(h,h,c)->(c,chc,chc)`.  This is a bounded physical path, but not a hub flow:
M60's later arbitrary square refresh and unchanged-label slide are H3
heat-bath moves and do not belong to `P_(0,d)`.  Polynomial mixing of the
terminal square label/insertion history remains open.  M60's all-original-
leaves core obstruction applies to a different fixed-leaf-cell resampler and
does not prove a single `(v,z)` fiber reducible.

## 3. Exact marked-law and projected-flow audit

Two laws must be separated.  The spectrum-preserving lift of `P_(0,d)` is

```text
tilde_pi(w,v)=1/[|Z_d| number_of_join_tree_leaves(w)],
```

where the word is updated by `P_(0,d)` and the new leaf mark is refreshed
uniformly.  Its spectrum is that of `P_(0,d)` plus zeros.  Uniform counting
on marked incidences is leaf-biased; the one-level density ratio is `O(d)`.

Deletion is equivariant: every physical signed-Hurwitz proposal retaining the
leaf mark deletes to a self-loop or one literal signed-Hurwitz move.  The
converse statewise lift is **REFUTED at d=4**: `10,992` of `29,328` requested
nontrivial oriented base moves have no one-step physical lift from the given
upstairs state.

Fixing one missing label at `d=4`, all 108 oriented off-diagonal base demands
have positive aggregate physical flow.  Normalized raw stationary-flow ratios
range from `0.31881918819188193` to `0.46051660516605164`; mark loss is
`1908/16260`.  These are exact finite facts, not universal domination.

Standard restriction/projection still multiplies a fiber gap by the
downstairs gap.  If the fresh fiber loss is `d^-C` at every level, iteration
gives `(d!)^-C`.  The recursive route therefore requires the standalone
**MARKED-LEAF ADDITIVE POINCARE RECURSION** in the proof note, with only a
`1+O(1/d)` coefficient on the inherited variance.  It remains unresolved.

## 4. Exact rooted DPS product theorem

Duchi--Poulalhon--Schaeffer (DPS), Proposition 1 and Theorem 4, biject `Z_d`
with unrooted Hurwitz trees.  DPS Proposition 3 proves that after choosing a
white root there is a literal bijection

```text
rooted Z_d <--> Cayley trees on [d] x S_(2d-2).       (4.1)
```

The construction roots a Cayley tree at `y_d`, inserts black `x_i` into the
first parent edge of `y_i`, and gives its two halves labels
`pi(2i-1),pi(2i)`.  The rooted tree recovers `(T,pi)` uniquely.  Forgetting
the white root is exactly `d`-to-one.  Consequently uniform rooted `Z_d` is
exactly `UST(K_d) x Unif(S_(2d-2))`, not an approximately weighted map law.

Updating the word by `P_(0,d)` and then refreshing the target white root
uniformly gives a spectrum-preserving lift of the physical chain: its
spectrum is that of `P_(0,d)` plus zeros.  The exact `d`-to-one root quotient
must be included in any future capacity accounting; no physical comparison
loss is asserted here.

This supports the following exact ideal product chain.  For `d>=3`, from `T`
choose independently and uniformly `e in T` and
`f in E(K_d)\T`; with probability `1/2` replace `T` by `T-e+f` if that set is
a tree, and otherwise hold.  The uniform spanning-tree law is homogeneous
strongly Rayleigh, so Anari--Oveis Gharan--Rezaei, Theorem 2.3, gives this
kernel gap at least

```text
1/[2(d-1)(binom(d,2)-d+1)].
```

At `d=2` the tree coordinate is a singleton.

On `pi in S_m`, `m=2d-2`, hold with probability `1/2`; otherwise choose
`j in [m-1]` uniformly and interchange the values `j,j+1` wherever they occur
in `pi`.  Caputo--Liggett--Richthammer, Theorem 1.1, identifies this
interchange gap with path random walk, hence `Theta(m^-3)` in the displayed
random-scan normalization.  The kernel which chooses the tree or permutation
coordinate with probability `1/2` and applies its exact kernel therefore has
an inverse-polynomial gap.

This is a **PROVED ideal-chain gap**, not a gap for the physical Hurwitz walk.

## 5. Exact refutation of one-step product intertwining

I directly implemented DPS Proposition 3 and the quadratic hairy-tree closure
of Theorem 5.  Every `(T,pi)` was exhausted for `d=2,3,4`; every reconstructed
tuple evaluated to identity, had connected support, and every `Z_d` state had
exactly `d` rooted preimages:

| `d` | rooted `(T,pi)` pairs | `|Z_d|` | preimages/state |
|---:|---:|---:|---:|
| 2 | 2 | 1 | 2 |
| 3 | 72 | 24 | 3 |
| 4 | 11,520 | 2,880 | 4 |

The named claim “an adjacent-value swap of `pi` with `T` fixed is one signed
Hurwitz move” is false already at `d=3`.  A smallest stored witness is

```text
T={{1,2},{1,3}}, pi=(1,3,4,2), swap values 1 and 2,
w =((0,1),(1,2),(0,2),(1,2)),
w'=((0,1),(0,2),(0,2),(0,1));
distance_P0(w,w')=2.                                      (5.1)
```

At `d=3`, adjacent-`pi` swap distances have histogram
`{1:132,2:36,3:48}`; Cayley-tree basis-exchange distances have
`{1:48,2:40,3:48,4:8}`.  At `d=4`, their maxima are eight and twelve.
Thus both universal one-step intertwinings are refuted.

One lexicographic shortest-path rule has finite `d=4` maximum action loads
48 and 109 and descriptor/time recovery multiplicities 16 and 7.  These
numbers are **EXACT FINITE DIAGNOSTICS ONLY**.  Polynomial diameter or small
finite load is not asymptotic congestion evidence.

## 6. Sharp remaining nonrecursive lemma

The main route is now the exact standalone obligation:

> **ROOTED PRODUCT LOCAL COMPARISON.**  Assign every adjacent-`pi` or UST
> basis-exchange ideal edge a distribution on signed adjacent-Hurwitz paths
> so that path length, source multiplicity given a physical edge/time/local
> descriptor, and stationary edge congestion are all `d^O(1)`, including the
> exact `d`-to-one white-root quotient.

If proved, standard Dirichlet comparison with the ideal product chain closes
`gap(P_(0,d))>=d^-O(1)` nonrecursively.  It is **UNRESOLVED**.  The global
stack closure means short paths in small ranks do not prove it; no flow is
routed through a canonical hub.  A face-label swap may be literal only under
extra local incidence conditions.  Disjoint factor transpositions do not
suffice, because their quadrangulation faces can still share a white vertex.

## 7. Boundary calculations and named falsifications

The transfer recurrence independently reproduces the direct fibers:

| downstairs `q` | per-missing-label fiber sizes | max/min |
|---:|---:|---:|
| 1 | `1` | 1 |
| 2 | `16` | 1 |
| 3 | `67` (6 words), `68` (18 words) | `68/67` |
| 4 | `170..188` (12-atom stored histogram) | `188/170` |

For `q=3`, size 67 occurs exactly for the six concatenated distinct-square
words.  Every fixed marked fiber is connected at `d=2,3,4`; this is exact
finite evidence only.  The Dyck join/cut path is not lumpable already at
`d=3` (accepted M13), so no Dyck Markov projection is claimed.

The only universal statements falsified by minimal cases are the named
statewise one-step deletion lift (`d=4`) and the named one-step DPS product
intertwinings (`d=3`).  No finite calculation is used to prove a universal
gap.

## 8. Scope inside M104's `Gamma_0`

M104's `Gamma_0(d)` ranges over every connected minimal transitive
factorization

```text
F(C,q,k),          k=|C|+cycles(q)-2.                 (8.1)
```

Only `q=id_C` gives `Z_|C|`.  A full cycle, for example, has length
`|C|-1`.  Appending a fixed factorization of `q^-1` embeds an arbitrary
endpoint sector into an identity word, but seam Hurwitz moves leave the
image and no rejected-exit action-rate or gap comparison follows.  DPS says
its construction extends to general cycle type, but supplies no physical
Hurwitz comparison there.

Therefore a theorem for every `Z_s` would close only M104's identity circular
cell.  The arbitrary-product genus-zero coordinates remain **ADDITIONAL
UNRESOLVED OBLIGATIONS**.

## 9. Dependencies, reproduction, artifacts, and hygiene

Accepted inputs are M49 strand deletion/fixed-null multiplicity, the M13
Dyck non-lumpability witness, M60 only for its literal signed null-pushing
identities and obstruction warning, and M104's definition of `Gamma_0`.
DPS Proposition 1, Proposition 3, Theorems 4 and 5 are primary-source inputs.
The two ideal-chain gap inputs are the primary-source theorems named above.
Exact sources are [DPS](https://www.irif.fr/~poulalho/Articles/DuPoSc13.pdf),
[Anari--Oveis Gharan--Rezaei](https://arxiv.org/abs/1602.05242), and
[Caputo--Liggett--Richthammer](https://arxiv.org/abs/0906.1238).

Deterministic commands, Python 3.12.3, no nonstandard dependency, `seed=null`:

```text
python3 -B marked_leaf_audit.py --d 2 3 4 --output marked_leaf_results.json
python3 -B lift_transfer_audit.py --base-q 1 2 3 4 --output lift_transfer_results.json
python3 -B aggregate_projection_audit.py --d 3 4 --output aggregate_projection_results.json
python3 -B dps_local_audit.py --d 2 3 4 --output dps_local_results.json
```

Owned artifacts are `plan.md`, `checkpoint.md`, `marked_leaf_reduction.md`,
the four scripts and four JSON outputs, this report, `freeze_manifest.md`, and
`SHA256SUMS`.  Source compilation, JSON parsing, exact reruns, manifest
verification, and cache removal are part of the freeze.  No predecessor,
coordinator note, shared manuscript, project skill, or file outside the owned
mission directory is edited.

```text
FINAL VERDICT: KEEP AS A STRICT REDUCTION; GAP UNRESOLVED.
```
