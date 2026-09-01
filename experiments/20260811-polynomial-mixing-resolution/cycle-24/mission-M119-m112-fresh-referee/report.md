# M119 fresh referee report on frozen M112

Date: 2026-08-12 UTC.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict and exact scope

```text
ACCEPT M112 AS A STRICT, NONTERMINAL REDUCTION.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

The exact marked-leaf transfer recurrence, its one-level density bound, the
two lifted-law distinction, deletion equivariance, the finite refutations,
the rooted DPS product theorem, and the ideal product-chain gap are correct.
The exact remaining statement is still **ROOTED PRODUCT LOCAL COMPARISON**.
Neither the cited papers nor the finite calculations provide that comparison.

Accordingly this audit proves no inverse-polynomial gap for the physical
signed-Hurwitz chain on `Z_d`, no bound for all of M104's `Gamma_0(d)`, no
gap for the lazy `{3,4,5}` heat bath, and neither Terminal A nor Terminal B.

The convention throughout is `(pq)(x)=p(q(x))`, with displayed factors
multiplied left-to-right.  The physical auxiliary kernel is

```text
P_(0,d)=I/2+[1/(4(2d-3))]sum_i(R_i+R_i^(-1)),
R_i(a,b)=(b,bab),       R_i^(-1)(a,b)=(aba,a),
```

on uniform connected identity words of length `2d-2` on `[d]`.

## 2. Frozen provenance

All assigned digests match exactly:

| artifact | observed SHA-256 |
|---|---|
| M112 `report.md` | `6364b8c94d507885d5d408c98ba49c9405623e93a5c3bcd043a3c1404f0bf4f3` |
| M112 `marked_leaf_reduction.md` | `dc2c87c2c28deb5438301fb95254040012fc69115bf9c7f547542382ebd82f0a` |
| M112 `dps_local_audit.py` | `b5e193ba0595aaf61d497a3482685b5a5d8c63faaf9f8567931db31629357add` |
| M112 `dps_local_results.json` | `4467ba62dddd4ac3dc351d634d797c4bec011504556867f0f7dc6493d28e4b87` |
| M112 `SHA256SUMS` | `43b5255f014d8d7e480aa6d17130bb982e30b12a763c20a94e8c453de38f9cb3` |

M119 code imports no M112 or predecessor experiment module.  It uses only the
Python standard library and definitions reimplemented in the owned directory.

## 3. Marked deletion and transfer theorem

Fix a missing leaf label `v`, put `q=d-1`, and let `z in Z_q`.  The two null
increments select a unique interval `0<=a<=b<=2q-2`.  While the interval is
open, record the predecessor coordinate `c` of `v`.

The M49 right-multiplication table gives exactly:

- at a support join `(x,y)`, the base factor is forced and `c` is transported
  by `(x,y)`, giving its permutation matrix;
- at a cycle cut `(x,y)`, coordinates outside `{x,y}` have one continuation,
  while either endpoint has the two continuations to `x` and `y`, giving an
  identity matrix with an all-ones `{x,y}` block.

Opening chooses one of `q` coordinates.  The closing factor is forced by the
terminal coordinate.  A matrix path therefore reconstructs every upstairs
factor uniquely.  Conversely a leaf lift has one opening join, follows the
same exhaustive table, and has a unique closing null.  This proves the
bijection and

```text
L_(a,b)(z)=1^T T_a...T_(b-1)1,
L(z)=sum_(0<=a<=b<=2q-2)L_(a,b)(z).
```

For each initial coordinate, the all-base continuation gives a distinct
lift, so every interval has at least `q` lifts.  Under a cut, descendants of
one initial coordinate lie in distinct current permutation cycles; joins in
a minimal word cannot merge two such descendants.  Thus there are at most
`q` descendants per initial coordinate and at most `q^2` lifts per interval.
There are `C=binom(2q,2)` intervals, proving

```text
q C <= L(z) <= q^2 C,       max_z L(z)/min_z L(z)<=q.
```

This is a one-level raw counting-law comparison.  Iterating a factor `q`
over all deletion depths is factorial, so it is not a polynomial gap
recursion.

The signed moving-square statement is also correct: the M60 identities used
before the square forms are literal right/inverse Hurwitz moves, and

```text
(h,h,c)->(h,c,chc)->(c,chc,chc)
```

moves the square across one base factor in two physical moves.  M60's later
arbitrary square refresh is an H3 heat-bath move and is correctly excluded
from `P_(0,d)`.

## 4. Lifted laws, spectrum, and deletion equivariance

On marked leaf incidences `Y_d`, the spectrum-preserving refresh law is

```text
tilde_pi(w,v)=1/[|Z_d| ell_T(w)].
```

The lifted operator first applies `P_(0,d)` to `w` and then averages over the
new word's leaves.  It acts as `P_(0,d)` on functions constant on mark fibers
and annihilates functions with zero conditional mark average.  Its spectrum
is therefore the physical spectrum plus zeros.  Uniform counting on `Y_d`
instead has word marginal proportional to `ell_T(w)` and differs by an
`O(d)` one-level density factor.  M112 keeps these laws separate.

Deletion equivariance is valid when the same leaf mark survives the physical
move.  Only the erased intermediate prefix in the two-factor window changes.
After nulls are removed, the surviving pair is unchanged or is another
two-transposition decomposition of the same product.  Identity has only a
square, a 3-cycle has the three decompositions related by the two signed
Hurwitz moves, and a disjoint double transposition has the two commuting
orders.  Thus the deleted word holds or makes one literal signed move.

The converse is not statewise.  The independent exhaustive check reproduced
exactly `10,992` failures among `29,328` nontrivial oriented downstairs
requests at `d=4`.  It also reproduced, for one fixed missing label, all 108
positive aggregate demands, normalized ratios
`0.31881918819188193..0.46051660516605164`, and mark loss `1908/16260`.
These are exact finite facts only; they prove no universal flow domination.

## 5. DPS primary-source theorem and convention

Duchi--Poulalhon--Schaeffer (DPS), *Uniform random sampling of simple
branched coverings of the sphere by itself*, supplies the following exact
chain of statements:

1. Proposition 1 bijects minimal transitive identity factorizations with
   indexed increasing quadrangulations.
2. Theorem 4 bijects those quadrangulations with unrooted Hurwitz trees.
3. Proposition 3 starts from a Cayley tree rooted at `y_d`, inserts black
   `x_i` in the first parent edge of `y_i`, and labels the two halves by
   `pi(2i-1),pi(2i)`.  Its proof explicitly says this is bijective before
   the white root is forgotten, and exactly `d`-to-one afterward.
4. Theorem 5 proves that the hairy-tree stack closure is the inverse of
   Theorem 4.

Hence the fully rooted law is literally

```text
Cayley trees on [d] x S_(2d-2),
```

with independent uniform coordinates.  This is stronger than a weighted or
approximate map law.  DPS writes `tau_m...tau_1=id`; inversion (all factors
are involutions), or equivalently word reversal, translates to the project
convention.  The independent `+`-mirror implementation reproduces M112's
displayed word exactly.

The paper does not state a Hurwitz/closure intertwining, bounded local
simulation, or congestion theorem.  Its appendix only says the enumerative
approach extends almost directly to a general cycle type.  It supplies no
physical-chain comparison in those sectors.

Primary source: <https://www.irif.fr/~poulalho/Articles/DuPoSc13.pdf>.

## 6. Ideal-chain normalizations

For the UST coordinate, the Anari--Oveis Gharan--Rezaei natural chain chooses
`e in T` and `f outside T` independently and uniformly, then accepts a valid
exchange with probability `1/2`.  This is exactly M112's kernel for the
uniform spanning-tree strongly Rayleigh law.  With ground-set size
`E=binom(d,2)` and rank `k=d-1`, Theorem 2.3 gives

```text
gap(Q_T)>=1/[2k(E-k)]
        =1/[2(d-1)(binom(d,2)-d+1)].
```

At `d=2` the coordinate is a singleton.

Caputo--Liggett--Richthammer Theorem 1.1 equates the continuous-time
interchange and one-particle random-walk gaps.  On the `m`-vertex path with
unit edge rates the latter is `2(1-cos(pi/m))`.  M112's half-lazy random-scan
kernel scales this generator by `1/[2(m-1)]`, so in fact

```text
gap(Q_pi)=(1-cos(pi/m))/(m-1)=Theta(m^-3).
```

Swapping adjacent values rather than adjacent positions is conjugate via
permutation inversion and has the same spectrum.  Finally, the equal
coordinate mixture has gap exactly one half the smaller coordinate gap.
Thus the ideal rooted product chain has an inverse-polynomial gap with all
normalizations correct.

Primary sources: <https://arxiv.org/abs/1602.05242> and
<https://arxiv.org/abs/0906.1238>.

## 7. Root quotient and the exact missing comparison

Uniform `w in Z_d` plus a uniform white root is uniform on the rooted DPS
product, because forgetting the root is exactly `d`-to-one.  Updating `w`
and refreshing the new white root uniformly is again a spectrum-preserving
lift, now with constant fiber size `d`.

Standard Dirichlet comparison would therefore prove the physical gap if one
assigned every ideal edge a signed-Hurwitz path with polynomial stationary
edge congestion in this lifted chain.  Rooted edge capacities include the
root refresh and the exact quotient; ignoring those factors is invalid, but
their cardinality is only polynomial.  M112's standalone **ROOTED PRODUCT
LOCAL COMPARISON** explicitly requires the quotient and the final stationary
congestion, so it is sufficient if proved.

It is unresolved.  DPS closure is global.  The exact audit refutes both
tempting one-step intertwinings: at `d=3`, adjacent-value distances have
histogram `{1:132,2:36,3:48}`, and tree-exchange distances have
`{1:48,2:40,3:48,4:8}`.  At `d=4` their maxima are 8 and 12.  Polynomial
finite distance does not bound asymptotic source multiplicity or congestion.

## 8. Scope relative to `Gamma_0`

M104's `Gamma_0(d)` minimizes over component coordinates of the form

```text
F(C,q, |C|+cycles(q)-2)
```

that occur in realizable genus-zero side cells.  The identity endpoint gives
`Z_|C|`, but a full cycle gives length `|C|-1`, and other endpoints give
further arbitrary-product sectors.  A theorem for every `Z_s` would close
the exact same-size identity circular cell and only that part of the side
obligation.  Appending a fixed factorization of `q^-1` is not a restriction
comparison because seam Hurwitz moves leave the image.  M112's scope warning
is therefore correct.

Connected-support identity Hurwitz transitivity should retain whatever
dependency label the project assigns to its Ben-Itzhak--Teicher source; none
of the newly accepted DPS/transfer claims upgrades that separate literature
dependency.  A proof of ROOTED PRODUCT LOCAL COMPARISON would itself supply
the needed physical connectivity.

## 9. Independent exact audit

The deterministic command was

```text
python3 -B independent_audit.py --max-d 4 --output independent_results.json
python3 -B independent_aggregate_audit.py --output independent_aggregate_results.json
```

Python `3.12.3`, seed `null`, dependencies `{}`.  The first run took
`448.6463074684143` seconds.  Selected exact results are:

| check | result |
|---|---:|
| `|Z_2|,|Z_3|,|Z_4|` | `1,24,2880` |
| marked incidences at `d=4` | `6504` |
| transfer interval rows | `1460`, zero failures |
| direct `q=3` fiber sizes | `67` for 24 marked-label rows, `68` for 72 |
| deletion-equivariant retained proposals | `57640`, zero failures |
| statewise base requests / failures | `29328 / 10992` |
| rooted pairs at `d=2,3,4` | `2,72,11520` |
| rooted preimages per word | exactly `2,3,4` |
| DPS identity/support/coverage failures | zero |
| displayed adjacent-value witness distance | `2` |
| `d=4` adjacent/tree ideal-edge max distance | `8 / 12` |

The full `q=4` transfer histogram `170..188` and both complete `d=3`
distance histograms match M112 byte-for-byte as integer tables.  These checks
are finite falsifiers and convention audits, not asymptotic evidence.

## 10. Final decision

```text
ACCEPT.  ZERO MATERIAL NUMBERED OBJECTIONS.
```

Promote M112's exact marked-transfer theorem and its literal rooted product
reduction.  Preserve the negative one-step findings and the finite-only
labels.  The first nonrecursive open lemma remains **ROOTED PRODUCT LOCAL
COMPARISON**, and arbitrary-product `Gamma_0` coordinates remain additional
obligations.  This report is nonterminal for the global mixing goal.
