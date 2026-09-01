# Marked leaf-strand reduction for the minimal genus-zero Hurwitz walk

Date: 2026-08-12.

Every universal statement is labeled.  Permutations compose as
`(pq)(x)=p(q(x))`; displayed factor tuples multiply left-to-right.

## 1. State space and kernel

For `d>=2`, put

```text
Z_d={w=(t_1,...,t_(2d-2)):eval(w)=id,
                              support(w) connected on [d]},
P_(0,d)=I/2+[1/(4(2d-3))]sum_(i=1)^(2d-3)(R_i+R_i^(-1)),
R_i(a,b)=(b,bab),       R_i^(-1)(a,b)=(aba,a).
```

The target is uniform on `Z_d`.  The desired inverse-polynomial gap remains
**UNRESOLVED**.

For `w in Z_d`, the prefix-cycle rank is a Dyck excursion with `d-1` joins
and `d-1` cuts.  The join factors form the prefix join tree `T_J(w)`.  This
is an accepted project fact and follows directly because every support join
joins two prefix permutation cycles and all `d-1` cycle joins are exhausted.

## 2. Marked deletion and two distinct lifted laws

Let

```text
Y_d={(w,v):w in Z_d, v a leaf of T_J(w)},
ell_T(w)=number of leaves of T_J(w).
```

The accepted M49 strand-deletion theorem proves that

```text
D(w,v)=(v,Del_v(w)) in [d] x Z_(d-1),                 (2.1)
```

where deleting `v` from every prefix permutation produces exactly two
identity increments and the remaining word has minimal connected support on
the other labels.  Relabeling the complement increasingly is understood.

Two measures on `Y_d` must not be confused.

1. The spectrum-preserving refresh lift of `P_(0,d)` uses

   ```text
   tilde_pi(w,v)=1/[|Z_d| ell_T(w)].                  (2.2)
   ```

   Update `w` by `P_(0,d)` and then refresh the target leaf mark uniformly.
   Exactly as in M97,
   this lift has the spectrum of `P_(0,d)` plus zeros.

2. Uniform counting measure on marked incidences is

   ```text
   mu_mark(w,v)=1/|Y_d|.                              (2.3)
   ```

Their density ratio is proportional to `ell_T(w)` and, for `d>=3`, can vary
between `2` and `d-1`; at `d=2` it is identically two.  A one-level
comparison costs only a factor `O(d)`, but naively
multiplying that factor through all deletion depths is factorial.  Thus the
raw marked law is useful for exact counting and flow audits, not an automatic
gap recursion for the original chain.

## 3. Exact insertion-coordinate lift recurrence

Fix a missing label `v`, set `q=d-1`, and let

```text
z=(s_1,...,s_L) in Z_q,       L=2q-2.
```

The two null increments in a lift determine two factor positions among the
`L+2=2q` upstairs positions.  Equivalently they determine a unique interval

```text
0<=a<=b<=L                                             (3.1)
```

of consecutive base factors that lie strictly between the opening and
closing nulls.  There are `binom(2q,2)` such intervals, including empty
intervals (`a=b`).

While the insertion coordinate is open, record the predecessor `c in [q]`
of `v` in the current permutation cycle.  Let `J_r` state whether `s_r` is a
prefix support join of `z`.  Define `q x q` nonnegative integer matrices

```text
T_r = permutation matrix of s_r,                 if J_r=join,
T_r = I with the {x,y} block replaced by [[1,1],[1,1]],
                                                if J_r=cut and s_r=(x,y).
                                                               (3.2)
```

### Proposition 3.1 (exact fixed-interval lift count; **PROVED**)

For interval `[a,b)`, the number of leaf lifts with those two null positions
is

```text
L_(a,b)(z)=1^T T_a T_(a+1)...T_(b-1) 1.             (3.3)
```

Consequently the whole fixed-missing-label fiber has exact size

```text
L(z)=|{w:(w,v) in Y_d,Del_v(w)=z}|
    =sum_(0<=a<=b<=L) L_(a,b)(z).                    (3.4)
```

**Proof.**  Immediately before the opening null, `v` is fixed.  Its opening
factor is `(v,c)` for one of the `q` possible coordinates `c`, accounting
for the initial all-ones vector.  Use the M49 right-multiplication table at
one base factor `s=(x,y)`.

- At a support join, a `v`-incident alternative would create a second
  join-tree edge incident to `v`.  The only valid lift is `s`; it sends
  coordinate `c` to `s(c)`, which is the permutation matrix in (3.2).
- At a cycle cut, a coordinate outside `{x,y}` has the unique lift `s` and
  remains fixed.  Starting at `x` or `y`, there are exactly two lifts (`s`
  or the appropriate `v`-incident factor), and the next coordinate can be
  either endpoint.  This is the all-ones block in (3.2).

After the interval, the closing null factor is forced by the final
coordinate; after it every factor lift is forced.  Thus paths through the
transfer matrices are in bijection with lifts having the two specified null
positions.  The join restriction ensures `v` has exactly one join-tree
edge, while the base joins connect the other labels.  Telescoping strand
increments gives endpoint identity.  Conversely, every leaf lift has the
two M49 nulls and follows exactly this table, so the construction is onto and
injective.  Summing the disjoint null-position choices proves (3.4).  QED.

### Corollary 3.2 (polynomial raw projection distortion; **PROVED**)

For every `z in Z_q`,

```text
q binom(2q,2) <= L(z) <= q^2 binom(2q,2),             (3.5)
max_z L(z)/min_z L(z) <= q.                           (3.6)
```

The lower bound holds because each interval has at least the `q` forced
all-non-`v` lifts, one for every opening coordinate.  For the upper bound,
the accepted M49 fixed-null-position multiplicity theorem gives at most
`q^2` lifts for every interval; it was proved by the distinct-current-cycle
invariant under cuts.  There are exactly `binom(2q,2)` intervals.  QED.

This proves only a polynomial one-level Radon--Nikodym comparison between
the `D`-pushforward of raw marked incidence measure and the uniform law on
`[d] x Z_q`.  It does not justify multiplying (3.6) down to `q=1`.

### Proposition 3.3 (signed moving-square normal form; **PROVED**)

Every `(w,v)` in a fixed deletion fiber `D(w,v)=(v,z)` admits a path of at
most `3(2d-2)` signed adjacent-Hurwitz moves, retaining `Del_v=z`, to

```text
z (v,a)(v,a)                                             (3.7)
```

for some `a` in the base support.  The endpoint label `a` is not controlled.

**Proof.**  M60 identities

```text
h_a s=s(sh_as),             h_a h_b=(a,b)h_a             (3.8)
```

are literally one right or inverse Hurwitz move; no H3 padding is needed for
`P_(0,d)`.  Apply the insertion-coordinate table to move the opening null to
the right until it meets the closing null.  The adjacent pair is a square
`h h`, all other factors are `z` in their original order, and at most
`2d-3` swaps were used.  A square crosses one base factor in two right moves:

```text
(h,h,c) -> (h,c,chc) -> (c,chc,chc).                    (3.9)
```

Conjugating `(v,a)` by a base transposition is again `(v,a')`.  Repeating
(3.9) moves the square to the right endpoint while retaining the ordered base
word and deletion `z`.  Hurwitz moves preserve the generated transitive
subgroup, so all intermediates remain in `Z_d`; the displayed construction
retains one join edge at `v`.  The coarse length bound follows.  QED.

M60's subsequent refresh `c h h -> c f f` and unchanged-label slide
`f f c -> c f f` are literal H3 heat-bath transitions, not transitions of
`P_(0,d)`.  Therefore M60's fixed-cell hub theorem does **not** prove a
signed-Hurwitz restriction gap here.  The missing fiber step is polynomial
mixing of the uncontrolled terminal square label/insertion history without a
canonical hub.  M60's reducibility theorem for resampling cells of every
*original* leaf concerns a different auxiliary chain and is retained only as
a warning: its all-original-leaves core invariant does not by itself imply
reducibility of a single fixed `(v,z)` fiber.

## 4. Exact interaction with signed Hurwitz moves

### Proposition 4.1 (deletion equivariance; **PROVED**)

If a signed adjacent-Hurwitz move sends `(w,v)` to `(w',v)` with `v` still a
leaf of `T_J(w')`, then

```text
Del_v(w')=Del_v(w),
```

or `Del_v(w')` is obtained from `Del_v(w)` by one signed adjacent-Hurwitz
move.

**Proof.**  Strand deletion is induced by applying the group map `d_v` to
each prefix and taking successive increments.  A Hurwitz move changes only
one intermediate prefix.  Before and after the two-factor window the erased
prefixes are unchanged.  Hence at most the two corresponding nonidentity
increments can change, and their ordered product is fixed.  If neither
survives, or only the placement of a null changes, the deleted word is
unchanged.  If both survive, the new ordered transposition pair is the right
or inverse Hurwitz image of the old pair.  For a nonidentity two-factor
product this follows from the three 3-cycle decompositions or the two
commuting disjoint-transposition decompositions.  For identity product, the
two-null row of the insertion-coordinate table forces the same surviving
square: a physical two-factor Hurwitz move cannot refresh its label.  Thus
the deleted pair is unchanged in that case.  Retention of the leaf mark
ensures there are still exactly two nulls and the output remains in `Z_q`.
QED.

The converse statewise lift is false.  The exact `d=4` audit finds `10,992`
failures among `29,328` requested nontrivial oriented base moves over all
source lifts.  Thus no pointwise Dirichlet domination follows.

At the aggregate level, fixing one missing label at `d=4`, all 108 oriented
off-diagonal base demands have positive physical lift flow.  Their raw
stationary-flow ratios against the uniform base generator flow range from
`0.3188191881...` to `0.4605166052...`; mark loss is `1908/16260`.
These are **EXACT FINITE** facts.  A universal aggregate lower bound remains
**UNRESOLVED**.

## 5. Why standard decomposition does not close the recursion

Let a raw fixed-mark restriction be partitioned by `z=Del_v(w)`.  If one
proved a polynomial minimum restriction gap `alpha_d` and projection gap
`beta_d`, standard JSTV or the elementary variance decomposition would give
only

```text
gap(fixed-mark chain at d) >= const * alpha_d * beta_d. (5.1)
```

Even if `beta_d` were a constant multiple of `gap(P_(0,d-1))`, a bound
`alpha_d=d^(-C)` iterated in (5.1) yields `(d!)^(-C)`, which is
superpolynomial.  Polynomial fiber cardinality, connectivity, diameter, and
one-level density comparison do not change this multiplication.

A successful recursive theorem therefore needs an additive/martingale
estimate such as the following standalone obligation.

> **MARKED-LEAF ADDITIVE POINCARE RECURSION.**  Construct a reversible lifted
> kernel `M_d` with `Z_d` marginal `P_(0,d)` and constants `c,C>0` such that,
> for every `f`,
> ```text
> Var_(Z_d)(f)
> <=(1+c/d) Var_(Z_(d-1))(E[f|D])
>   +d^C E_(M_d)(f,f),                                (5.2)
> ```
> and compare the first term's Dirichlet form to `P_(0,d-1)` with coefficient
> bounded below by a universal constant (or `1-O(1/d)`).

Iterating the `1+c/d` factors is polynomial and summing the energy terms is
polynomial.  Equation (5.2), or an equivalent actual-edge martingale/Green
contraction, is **UNRESOLVED**.  It must account for collisions among marked
deletion histories; separating a capacity copy for every history is invalid.

## 6. Exact boundary calculations

The deterministic scripts give:

| downstairs `q` | `|Z_q|` | upstairs fiber sizes per missing label | max/min |
|---:|---:|---:|---:|
| 1 | 1 | `1` | 1 |
| 2 | 1 | `16` | 1 |
| 3 | 24 | `67` (6 words), `68` (18 words) | `68/67` |
| 4 | 2880 | `170..188` with the recorded 12-atom histogram | `188/170` |

At `q=3`, `L(z)=67` exactly for the six concatenated-distinct-square words
`(a,a,b,b)` and is `68` for the other 18 words.  Direct upstairs enumeration
agrees with (3.4) for every fiber through `d=4`; evaluating (3.4) on all
`Z_4` bases independently reproduces the `d=5` per-missing-label histogram

```text
170:48, 171:72, 174:24, 175:144, 176:216, 177:528,
179:48, 180:432, 182:384, 184:72, 185:768, 188:144.       (6.1)
```

This does not enumerate `Z_5`.  These finite ratios motivate a sharper constant or
`1+O(1/q)` distortion conjecture, but Corollary 3.2 is the proved universal
bound.

The Dyck path is not a sufficient Markov coordinate: accepted M13 gives two
`d=3` words with the same path `JJCC` but different oriented-generator path
transition counts.  Hence the exact local `JC<->CJ` action does not by itself
produce a projection chain.

## 7. Arbitrary-product coordinates in `Gamma_0`

M104 defines `Gamma_0(d)` over all connected minimal transitive
factorization spaces

```text
F(C,q,k),         k=|C|+cycles(q)-2.                  (7.1)
```

The identity endpoint `q=id_C` gives `k=2|C|-2` and is exactly `Z_|C|`.
Other endpoints generally have shorter lengths and are not identity words.
For example, a full cycle has `cycles(q)=1` and `k=|C|-1`, the classical
minimal long-cycle sector.  Appending any fixed minimal factorization of
`q^(-1)` embeds it into an identity word, but Hurwitz moves across the seam
do not preserve the image and the appended length can be linear; no
rejected-exit action-rate or gap comparison follows.

Therefore an inverse-polynomial gap for every `Z_s` would close only the
same-size circular cell exhibited by M104.  The arbitrary-product spaces in
(7.1) remain additional `Gamma_0` obligations.  Duchi--Poulalhon--Schaeffer's
appendix states that its construction extends to general cycle type, but the
cited enumeration/bijection supplies no signed-Hurwitz spectral comparison.

## 8. Exact rooted Duchi--Poulalhon--Schaeffer product coordinates

Let `H_d` be the unrooted Hurwitz-tree set in Duchi--Poulalhon--Schaeffer
(DPS): `d` unlabelled white vertices, `d-1` labelled degree-two black
vertices, and `2d-2` distinctly labelled edges.  Proposition 1 and Theorem 4
give bijections

```text
Z_d <--> indexed increasing quadrangulations <--> H_d.        (8.1)
```

Here the source writes the reverse word product; reversing the displayed word
translates to the convention of Section 1.  Choose one white vertex of `H` as
a root and write `H_d^bullet` for the resulting set.

### Proposition 8.1 (literal rooted product law; **PROVED FROM DPS**)

There is a bijection

```text
H_d^bullet <--> Cayley_d x S_(2d-2).                           (8.2)
```

Consequently, if a uniform `w in Z_d` is augmented by a uniformly chosen one
of the `d` white vertices of its DPS tree, the corresponding pair `(T,pi)` is
exactly a product of a uniform Cayley tree on `[d]` and an independent uniform
permutation in `S_(2d-2)`.  Forgetting the root makes the map
`(T,pi)->w` exactly `d`-to-one.

**Proof.**  DPS Proposition 3 roots a Cayley tree `T` at `y_d`.  For each
`i<d`, insert a black vertex `x_i` into the first edge on the path from `y_i`
to `y_d`, and label the two resulting edges by `pi(2i-1),pi(2i)`.  The rooted
Hurwitz tree recovers `T` and `pi` uniquely.  Forgetting its white root has
exactly `d` choices.  Combine this with (8.1).  QED.

This corrects the weaker Section 8 draft statement: the fully rooted law is
not merely an indexed-map law with unknown fibers; it is a literal product
law.

The physical chain also has an exact spectrum-preserving rooted lift: update
`w` by `P_(0,d)` and then choose uniformly one of the `d` white roots of the
target DPS tree.  Its spectrum is that of `P_(0,d)` plus zeros.  Thus the
root coordinate does not change the lifted spectrum.  The exact `d`-to-one
quotient must be included in a future comparison's capacity accounting; no
physical comparison loss is asserted here.

### An explicit inverse-polynomial-gap ideal chain

On `Cayley_d x S_m`, `m=2d-2`, let `Q_T` be the natural lazy
basis-exchange chain: choose `e in T` and `f in E(K_d)\T` independently and
uniformly, replace `T` by `T-e+f` with probability `1/2` when the result is a
tree, and otherwise hold.  Uniform spanning trees are a
homogeneous strongly Rayleigh measure.  Anari--Oveis Gharan--Rezaei,
Theorem 2.3, proves that the gap of this exact chain is at least its smallest
positive directed transition probability.  Here that is

```text
1/[2(d-1)(binom(d,2)-d+1)],                                 (8.3)
```

so `gap(Q_T)>=d^(-O(1))`.
For `d=2` the Cayley-tree coordinate is a singleton and is assigned gap one.

Let `Q_pi` be the half-lazy adjacent-value interchange process on `S_m`:
hold with probability `1/2`; otherwise pick `j in [m-1]` uniformly and swap
the values `j,j+1` wherever they occur in `pi`.  Caputo--Liggett--
Richthammer, Theorem 1.1, identifies its gap with the one-particle random walk
on the path, so `gap(Q_pi)=Theta(m^(-3))` under this discrete random-scan
normalization.  The mixture

```text
Q_d=(Q_T tensor I + I tensor Q_pi)/2                         (8.4)
```

therefore has `gap(Q_d)>=d^(-O(1))`.  This is a gap theorem for the ideal
rooted product chain, not for `P_(0,d)`.

## 9. The exact missing nonrecursive comparison

DPS reconstructs a quadrangulation from a Hurwitz tree by globally completing
the cyclic label sequence at every vertex and then applying a stack of local
closures.  Proposition 8.1 alone gives no locality or Dirichlet comparison.
In particular, neither adjacent values in `pi` nor a single basis exchange of
`T` is asserted by DPS to be one physical Hurwitz move.

### Proposition 9.1 (one-step product intertwining; **REFUTED at d=3**)

The claim that every adjacent-value swap of `pi`, with `T` fixed, projects to
one signed adjacent-Hurwitz move is false.  In the `+` mirror convention take

```text
d=3, T={{1,2},{1,3}}, pi=(1,3,4,2), swap values 1 and 2,
w =((0,1),(1,2),(0,2),(1,2)),
w'=((0,1),(0,2),(0,2),(0,1)).                               (9.1)
```

The exact signed-Hurwitz graph distance from `w` to `w'` is two.  Thus even
the permutation coordinate does not globally intertwine in one step.  A
similar one-step claim for a Cayley-tree basis exchange is also false at
`d=3` (maximum tested distance four).

The direct implementation of DPS Proposition 3 and Theorem 5 exhausts every
`(T,pi)` at `d=2,3,4`.  Every reconstructed tuple evaluates to identity, has
connected support, and the map covers each state of `Z_d` exactly `d` times:

| `d` | rooted pairs | `|Z_d|` | preimages/state |
|---:|---:|---:|---:|
| 2 | 2 | 1 | 2 |
| 3 | 72 | 24 | 3 |
| 4 | 11,520 | 2,880 | 4 |

At `d=3`, adjacent-`pi` swap distances are `1:132, 2:36, 3:48`; basis-
exchange distances are `1:48, 2:40, 3:48, 4:8`.  At `d=4`, their maxima are
eight and twelve.  A fixed lexicographic shortest-path rule has finite maximum
physical-action loads `48` and `109` at `d=4`, respectively.  These are
**EXACT FINITE** diagnostics only: distance and small-rank load do not prove
an asymptotic source-recovery or congestion bound.

The exact remaining obligation is:

> **ROOTED PRODUCT LOCAL COMPARISON.**  For every ideal edge of (8.4), assign
> a distribution on signed adjacent-Hurwitz paths between its projected word
> endpoints such that (i) path length is `d^O(1)`, (ii) from a physical
> directed edge, path time, and `d^O(1)` local moved-data descriptor, the
> rooted ideal source has at most `d^O(1)` preimages, and (iii) the resulting
> stationary edge congestion is `d^O(1)` after the exact `d`-to-one root
> quotient.

Proving this lemma would compare the inverse-polynomial-gap `Q_d` to
`P_(0,d)` and close the desired minimal identity-sector gap nonrecursively.
It remains **UNRESOLVED**.  Routing through a canonical quadrangulation or a
single normal form does not satisfy it.  A potentially useful case split is
whether the two faces carrying consecutive labels are vertex-disjoint; merely
having disjoint factor transpositions does not ensure this, because the faces
may share a white vertex.  No local face-swap identification is promoted
without checking increasingness at every shared vertex.

The Caraceni polynomial-gap chain acts on uniform unindexed rooted planar
maps, not the uniform fully indexed objects in (8.1), so its theorem does not
replace ROOTED PRODUCT LOCAL COMPARISON.
