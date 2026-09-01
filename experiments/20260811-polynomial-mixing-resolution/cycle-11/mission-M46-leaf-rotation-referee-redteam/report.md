# M46 final report: leaf-rotation referee and weighted-flow red team

Date: 2026-08-11.  Permutations compose as `(pq)(x)=p(q(x))`; factor
tuples are multiplied left-to-right.  The primary investigation concerns an
auxiliary minimal-long-cycle parking projection.  Sections 2.10--2.11 also
record fresh referee verdicts on two scoped original-`K` anti-bottleneck
theorems.  Nothing here proves a global gap or Terminal A/B.

## 1. Exact quantified claims and conventions

For `r>=1`, let

```text
J_r={d in Z_+^r: sum_i d_i=r and
                    sum_(i=0)^k d_i>=k+1 for 0<=k<r},
pi_r(d)=r!/[(r+1)^(r-1) product_i d_i!].
```

Append `d_r=0` and identify `d` with the unique rooted plane tree having
preorder outdegrees `(d_0,...,d_r)`.  Let `Pbar_r` be the nonlazy uniform
scan of the `r-1` adjacent exact rank-two heat baths in the minimal
factorizations of `(0 1 ... r)`.

I give two referee verdicts.

1. **ACCEPT M35 LEAF-ROTATION COUNT.**  For every `r>=2`, `d in J_r`, and
   nonlast leaf child `j` of parent `i`, with `d'=d-e_i+e_j`,

   ```text
   Pbar_r(d,d')=2d_i/[3r(r-1)],
   Pbar_r(d',d)=2/[3r(r-1)].                         (1.1)
   ```

   The audited immutable hashes are

   ```text
   report.md              1ca18204936040277da472579d0f2070234d94f721d80cdac79e49e078872f65
   leaf_rotation_count.md e4e8da1e66caa28f90155cf750aed4e18c6243fdbb39428dff35920a82b46c7d
   ```

2. **ACCEPT M41 THEOREM 7.1.**  On rooted plane trees with `r` edges and
   law `pi_r(t) proportional to product_v 1/d_v(t)!`, let `Y_r` give every
   distinct root-preserving leaf-replanting neighbour the Metropolis rate

   ```text
   (4r^2)^(-1) min(1,pi_r(t')/pi_r(t)).              (1.2)
   ```

   Then, with the singleton convention at `r=1`,

   ```text
   gap(Y_r)>=1/[16(r+1)^8].                          (1.3)
   ```

   The audited M41 checkpoint hash, including its later root-degree theorem,
   is `9c0fc7da93f9ad18d817af431e45feb8ed871b36e2a1781bcee0d24824c449b3`.

Let `L_r` retain all undirected edges in (1.1) with their exact two
orientations and put unused mass on the diagonal.  Put, for `r>=3`,

```text
n=r-1,  D_r=2+ceil(log_2 n),
b_r=(r+1)(e/D_r)^D_r.
```

3. **ACCEPT M48 AUXILIARY SUPERPOLYNOMIAL CUT.**  There is a set `A_r` such
   that, whenever the displayed denominators are positive,

   ```text
   gap(L_r)
    <= b_r/[(e^(-1)-b_r)(3/(8e^2)-b_r)],             (1.4)
   r^C gap(L_r) -> 0 for every fixed C>0.             (1.5)
   ```

   This refutes every polynomial-congestion comparison from `Y_r` to `L_r`.
   It is not a bottleneck for the full projected chain `Pbar_r`, and it does
   not imply Terminal B for `K`.  The fresh referee found no substantive
   objection to the frozen M48 report
   `a609ecb60f6806d34894b7927d9bb27fdbe3949e59f9e30039e1bf974ce8d40e`
   or theorem
   `032e154ca4de74980b793d74f9970640707e9955a24a78d4b03c12e5147c89d0`;
   see `m48_referee_report.md`.

4. **ACCEPT M41 ROOT-DEGREE PROJECTION GAP.**  The stationary-flow
   projection of `Pbar_r` onto `d_0` has gap at least

   ```text
   4(r+1)/[3r^2(r-1)].                               (1.6)
   ```

   The fresh audit found no normalization or endpoint objection; see
   `m41_root_degree_referee.md`.

5. **PROVED FULL-PROJECTION LEAF-COUNT THRESHOLD FLOW.**  If
   `L(d)=#{0<=i<=r:d_i=0}` and both sides of
   `A_(r,ell)={L<=ell}` have `pi_r`-mass at least `1/4`, then

   ```text
   Q_Pbar(A_(r,ell),A_(r,ell)^c)
      >=1/[60(r+1)(r-1)]                             (1.7)
   ```

   for every `r>=2`.  This rejects a second full-projection threshold
   bottleneck but is not a full conductance or gap bound.  The frozen proof
   is `leaf_count_antibottleneck.md`.

6. **REFUTED PLAIN CYCLIC MACRO SYMMETRY.**  Conjugating a minimal
   long-cycle factorization by the long cycle is not a deterministic cyclic
   shift, nor even a degree-histogram-exchangeable map, on parking degree
   vectors.  The exact transformation needs extra last-label incidence data.

7. **ACCEPT M49 ORIGINAL-`K` BRANCH BALANCE.**  For `N>=4`, `m=2N-2`,
   and every `1<=q<=floor(N/2)`, the literal prefix-join-tree balanced-edge
   threshold has `Phi_pm^K>=1/(96N^6)`.  See `m49_referee_report.md`.

8. **ACCEPT M51 ORIGINAL-`K` DEGREE THRESHOLDS.**  For the same `N,m`,
   every nontrivial prefix-join-tree leaf-count and maximum-degree threshold
   has `Phi_pm^K>=1/(24N^7)`.  See `m51_referee_report.md`.

9. **ACCEPT M41 CAYLEY BASIS EXCHANGE.**  The uniform labelled-Cayley
   delete/add basis chain and its child-sort stationary-flow projection both
   have gap at least `1/r`; the projection has exact law `pi_r` and an exact
   polynomial-time step.  See `m41_cayley_exchange_referee.md`.

10. **ACCEPT M52 MACRO-CLOSED SCALAR THRESHOLDS.**  Both placements of
    `F_N^c` in every nontrivial leaf-count or edge-balance threshold have
    `Phi_pm^K>=1/(24N^7)`.  See `m52_referee_report.md`.

## 2. Full arguments and constructions

### 2.1 Referee proof of (1.1)

For any noncrossing factor tree, delete the least vertex from a current
consecutive interval `I=[a,b]`.  Its components are consecutive intervals.
For every proper initial `J=[a,t]`, each component of the induced forest on
`J` has an edge to `I\J`, so

```text
sum_(h in J)d_h>=|J|,
```

whereas the whole component has `sum_(h in I)d_h=|I|-1`.  Hence `b` is the
unique first index at which the Łukasiewicz sum `sum(d_h-1)` reaches `-1`.
The one possible attachment to an earlier vertex has its lower endpoint
outside `I` and does not change these forward degrees.  Recursion proves
M35 Lemma 2.1 without an uncovered boundary case.

It follows that every source factor tree contains the leaf chord `(i,j)`
and the unique attachment `(i,k)`, `k>j`, of the next child interval.  These
chords are consecutive around `i`.  Delete `(i,j)` from a word-consecutive
pair `(i,k),(i,j)` and close the vertex and factor labels.  Conversely,
insert `(i,j)` immediately after `(i,k)` in factor order.  The insertion is
noncrossing, and at `i` the incident factor labels locally become
`...>q+1>q>...`; all other clockwise-decreasing inequalities are preserved.
Goulden--Yong's necessary-and-sufficient characterization makes deletion and
insertion inverse bijections.  Thus

```text
#marked=(r-1)!/[(d_i-1)! product_(h!=i,j)d_h!]
       =d_i |O_d|/r.                                (2.1)
```

For `i<j<k`, the same-product fibre is exactly

```text
(i,k)(i,j),  (i,j)(j,k),  (j,k)(i,k).
```

The last two, and only the last two, change the lower-label multiset by
`-e_i+e_j`; this verifies completeness of the marked scans as well as their
favourability.  Divide (2.1) by `|O_d|`, by the `r-1` scan sites, and by the
three fibre outcomes to obtain the forward rate.  Since
`pi_r(d')/pi_r(d)=d_i` and the projection is reversible, the reverse rate in
(1.1) follows.  At `r=2`, these rates are respectively `2/3` and `1/3`; a
last child has no next sibling and is correctly excluded.

### 2.2 Referee proof of (1.3)

Fleurat's Theorem 4 applies to `w_k=1/k!`.  Its time reversal gives kernels
`f_n:T_n x T_(n-1)->[0,1]`, supported on deleting a rightmost-child leaf,
with

```text
sum_s f_n(t,s)=1,
sum_t pi_n(t)f_n(t,s)=pi_(n-1)(s).                  (2.2)
```

For each ordered `x,y in T_r`, sample one shared pivot
`z~pi_(r-1)`.  Independently sample deletion trajectories from `x`, `y`,
and two conditionally independent deletion trajectories from the same `z`.
At first-half time `i`, delete one leaf from the residual root tree of `x`
and reinsert that leaf in the location prescribed by the reversed
`z`-trajectory.  The current tree consists of a first-child subtree
`L in T_(i-1)` and a residual root tree `R in T_(r-i)`.  Each nontrivial
step is a literal root-preserving leaf replant; self steps can be suppressed.
At time `r`, both endpoint constructions meet at the same tree consisting of
a unary root above `z`.  Reverse the construction from `y` for the second
half.  Path length is at most `2r`.

Independence and (2.2) give the exact time-`i` marginal

```text
pi_(i-1)(L) pi_(r-i)(R).                            (2.3)
```

Put `N=r+1`, `a=i`, `b=N-i`, and let the current root have degree `k`.
Since `omega(t)=omega(L)omega(R)/k` and
`Z_s=(s+1)^(s-1)/s!`, direct algebra gives

```text
[pi_(a-1)(L)pi_(b-1)(R)]/pi_r(t)
 =k Z_r/[Z_(a-1)Z_(b-1)]
 =kab/[N p_(N,a)],                                  (2.4)

p_(N,a)=binom(N,a)(a/N)^a(b/N)^b.
```

Here `p_(N,a)` is the probability that `Bin(N,a/N)` equals its integer mean.
Uniform Stirling bounds give `p_(N,a)>=1/(3sqrt(N))`, including `a=1` and
`b=1`; hence (2.4) is at most `N^3`.

After deleting a leaf from a parent of degree `u` and inserting it at a
different parent of degree `v`, the exact weight ratio is `u/(v+1)`; a
same-parent reorder has ratio one.  Therefore every replanting-neighbour
ratio lies in `[N^-1,N]`.  There are at most `r(2r-1)<2r^2` distinct
neighbours, so (1.2) has diagonal mass at least `1/2`, and

```text
Q_Y(t,t')>=pi_r(t)/(4N^3).                           (2.5)
```

Use the one-step global `pi_r` heat bath, whose gap is one, as the comparison
source.  For a fixed directed edge, (2.3)--(2.4), at most `2N` path times,
and path length at most `2N` give load at most `4N^5 pi_r(t)`.  Division by
(2.5) gives congestion at most `16N^8` and proves (1.3).  Fleurat is used
only through aggregate balance (2.2), not a pointwise transition bound.

### 2.3 Exact binary/triangulation geometry

Under the left-child/right-sibling encoding, discard the plane root.  Let
`A` be the designated leaf, let `B` be its next plane sibling, let `P` be
the binary encoding of the child forest of `B`, and let `Q` encode the
siblings following `B`.  Locally the source and M35 target are

```text
source = (empty,(P,Q)),
target = ((P,empty),Q).                              (2.6)
```

Equivalently, in the plane-tree Dyck word this is the shift
`UD P <-> U P D`: the left sibling is required to be a leaf, while `P` is
the full next-sibling excursion.  It is therefore an exact leaf-left-sibling
plane-tree shift, but not generally an ordinary associahedron rotation.

An ordinary binary left rotation instead gives `((empty,P),Q)`.  Thus an
M35 move is one standard binary rotation, equivalently one convex-polygon
diagonal flip, **if and only if `P` is empty**, meaning that the next sibling
`B` is also a leaf.  The smallest mismatch occurs at `r=3`:

```text
(2,0,1) -> (1,1,1).
```

Consequently the leaf-rotation graph is not the associahedron graph or its
full flip walk.  Eppstein--Frishberg's polynomial mixing theorem for the
simple full associahedron walk has both the wrong edge set and the wrong
(uniform) stationary law; it does not transfer to `L_r`.

Caraceni--Stauffer's right peak translation is a third move.  In Dyck
notation it replaces `UDU` by `UUD`: a leaf immediately before a sibling is
detached and made the first child of that sibling.  It need not have a path
through M35 shifts whose intermediate stationary density is at least the
smaller endpoint density.  The smallest exact counterexample is at `r=5`:

```text
s=(2,0,2,1,0),  t=(1,3,0,1,0),
w(s)=30,         w(t)=20.
```

Exhaustive maximin search of all 42 states proves that every `L_5` path from
`s` to `t` visits a state of weight at most `5`; a path attaining floor `5`
is recorded in `peak_translation_r9.json`.  Thus direct reuse of the
Caraceni monotone-density routing is false, although this finite obstruction
does not preclude a different polynomial fractional flow.

Conversely, for every `r>=2`, the plane comb and path

```text
C_r=(2,1,...,1,0),  P_r=(1,...,1)
```

are one ordinary binary rotation apart and one root-preserving leaf
replanting apart.  Their stationary weights differ only by a factor two,
but they are not an `L_r` edge for `r>=3`.  This is a sharp test family for
the comparison that (1.5) now refutes.

The primary restricted-rotation results found do not match this chain.
Anoop--Sarma study distances under ordinary rotations with bounded binary
tree rank, and Cleary--Nadeem study ordinary rotations allowed only at
specified locations.  They prove distance algorithms/bounds, not a spectral
gap for the full Catalan state space with weight `product 1/d_v!`; neither
has the move (2.6).  No primary quantitative ``empty/skew rotation'' theorem
located in this audit has simultaneously the exact M35 edge set, full state
space, and stationary law.

### 2.4 Superpolynomial separator for `L_r`

Let the ordered root-branch sizes, including the root edges, be
`a_1,...,a_k`, and set

```text
S(t)={a_1,a_1+a_2,...,a_1+...+a_(k-1)} subset [n].  (2.7)
```

An internal leaf shift fixes `S`.  A root shift merges or splits consecutive
parts `(1,q) <-> (q+1)`, so its projection toggles `s+1` only when `s=0` or
`s` is already in `S`.  Hence every `L_r` path staying below maximum
outdegree `D_r` projects into the reversible-pebble graph on `[n]`, with
toggle rule

```text
toggle i only if i=1 or i-1 is occupied,
```

and at most `D_r-2=ceil(log_2 n)` pebbles.  The empty configuration and
`{n}` are disconnected at that cap.  Indeed a connecting path would be a
persistent reversible pebbling of the directed `n`-vertex path.  The
Komarath--Sarma--Sawlani tree theorem identifies its pebbling number with
one plus the edge-ranking number.  A `k`-color edge ranking covers at most
`2^k-1` path edges (delete the unique highest-colored edge and induct), and
median recursion attains this bound.  The required number of pebbles is
therefore `ceil(log_2 n)+1`.

Let `C_0` be the capped pebble component of the empty configuration, and put

```text
B_r={t:max_v d_v(t)>=D_r},
A_r={t notin B_r:S(t) in C_0}.                       (2.8)
```

Every `L_r` edge leaving `A_r` enters `B_r`.  The cycle-lemma/Vervaat
description of `pi_r` as the unique Lukasiewicz rotation of `r` uniform
balls in `r+1` boxes makes maximum degree rotation-invariant, and gives

```text
pi_r(B_r)<=b_r=(r+1)(e/D_r)^D_r.                    (2.9)
```

This is superpolynomially small because
`log b_r=-Omega(log r log log r)`.

Root-degree-one trees have `S=empty` and exact mass

```text
Z_(r-1)/Z_r=(r/(r+1))^(r-1)>=e^(-1).
```

Trees with ordered root composition `(r-1,1)` have `S={n}` and mass

```text
(1/2)Z_(r-2)/Z_r
 =r(r-1)^(r-2)/[2(r+1)^(r-1)]>=3/(8e^2).
```

Removing `B_r` proves the two denominator bounds in (1.4).  Reversibility
and boundary containment give
`Q_L(A_r,A_r^c)<=pi_r(B_r)`.  The indicator Rayleigh quotient proves
(1.4)--(1.5).  Combined with (1.3), this also rigorously rules out any
polynomial-congestion `Y_r`-to-`L_r` flow, deterministic or fractional.

### 2.5 The separator does not lift to the full projection

Let `E_r` be the same root-composition `(r-1,1)` reservoir and restrict to
`max d<=D_r-2`.  Every `d in E_r` has `d_0=2`, `S(d)={n}`, and lies outside
`A_r`.  M35's exact aggregate departure identity gives

```text
sum_(j>0) Pbar_r(d,d-e_0+e_j)=4/[3r(r-1)].           (2.10)
```

Every positive target in (2.10) has root degree one, hence `S=empty`, and
has maximum degree at most `D_r-1`; it lies in `A_r`.  With

```text
beta_r=r(r-1)^(r-2)/[2(r+1)^(r-1)],
b'_r=(r+1)(e/(D_r-1))^(D_r-1),
```

the same occupancy tail and reversibility give the exact-direction bound

```text
Q_Pbar(A_r,A_r^c)
 =Q_Pbar(A_r^c,A_r)
 >=4(beta_r-b'_r)/[3r(r-1)].                         (2.11)
```

Thus the proposed cut has polynomial, not superpolynomial, boundary flow
under the full parking projection.  The smallest exhaustive calibration is
`r=3`, where the low-degree edge

```text
(2,1,0) -> (1,2,0)
```

has exact projected rate `1/9`.  This proves nonlift to `Pbar_r`; it makes no
claim that some different full-projection or full-`K` bottleneck is absent.

### 2.6 A different full-projection cut also has polynomial flow

For fixed `k>=1`, consider the root-degree threshold

```text
H_(r,k)={d:d_0<=k}.
```

Under `pi_r`, the Cayley-tree Prüfer code gives the exact marginal

```text
pi_r(d_0=k+1)
 =binom(r-1,k)(r+1)^(-k)(r/(r+1))^(r-1-k).           (2.12)
```

Indeed root outdegree is root degree, hence one plus the number of zeroes in
the uniform length-`r-1` Prüfer code.  Every state in this layer has
aggregate projected rate

```text
2k(k+1)/[3r(r-1)]                                   (2.13)
```

to states with root degree `k`, again by M35's duplicate-label identity at
`h=0`.  Therefore

```text
Q_Pbar(H_(r,k),H_(r,k)^c)
 >=pi_r(d_0=k+1) 2k(k+1)/[3r(r-1)].                 (2.14)
```

For every fixed `k`, the probability in (2.12) tends to `e^-1/k!`, so this
boundary is `Omega_k(r^-2)`.  In particular the balanced cut at `k=1` is
not superpolynomial.  This is independent of the reversible-pebble
separator and rules out the simplest root-degree metastability mechanism;
it is not a lower conductance bound for arbitrary cuts.

### 2.7 Root-degree projection gap

Under `pi_r`, the rooted Cayley-tree Prufer code gives

```text
d_0-1 ~ Bin(r-1,1/(r+1)).                            (2.15)
```

For an observable `F(d)=f(d_0)`, reversibility permits every undirected
root-changing edge to be counted once in its lowering orientation.  M35's
exact aggregate identity therefore gives

```text
E_Pbar(F,F)
 >=sum_(k=2)^r Pr(d_0=k)
      2k(k-1)/[3r(r-1)] [f(k)-f(k-1)]^2.            (2.16)
```

The random-scan heat bath on `r-1` independent Bernoulli variables of
parameter `1/(r+1)`, projected onto their sum `b=d_0-1`, has downward rate
`b(1-p)/(r-1)` and gap `1/(r-1)`.  The ratio of (2.16)'s coefficient at
`b>=1` to that downward rate is

```text
2(b+1)(r+1)/(3r^2)>=4(r+1)/(3r^2).                  (2.17)
```

This proves the gap (1.6).  There is no missing factor two: both Dirichlet
forms are written as a sum in the lowering orientation.  At `r=2`, the
bound equals one and agrees with the exact two-state projected chain.

### 2.8 Balanced leaf-count thresholds

Let `L(d)=#{0<=i<=r:d_i=0}` after appending `d_r=0`.  If `U_*` is the
number of nonroot unary vertices, the degree sum gives

```text
U_*>=r+1-2L.                                         (2.18)
```

Each nonroot unary vertex supplies a distinct reverse M35 leaf rotation
which increases `L` by one, at exact rate `2/[3r(r-1)]`.  The cycle-lemma
occupancy representation says that `L` is the number of empty boxes when
`r` balls are thrown independently into `r+1` boxes.  Its exact law is

```text
Pr(L=ell)=(r+1)_(r+1-ell) S(r,r+1-ell)/(r+1)^r.     (2.19)
```

The Stirling row is log-concave by the real-rooted Stirling-polynomial
argument, the falling factorial is log-concave, and hence (2.19) is
unimodal.  Any threshold whose two sides have mass at least `1/4` has
`Pr(L=ell)>=1/[4(r+1)]`.  For `r>=128`, the empty-box mean and McDiarmid's
inequality force every such threshold below `9r/20`, so (2.18) supplies at
least `r/10` reverse moves.  Exact integer arithmetic closes `2<=r<=127`.
Together these facts prove (1.7).  The complete constants, finite-range
audit, and self-contained log-concavity reduction are frozen in
`leaf_count_antibottleneck.md`.

### 2.9 Long-cycle conjugation is not macro-lumpable

Let `G` be the factor tree and let
`epsilon_a=1_{{a,r} in E(G)}` for `0<=a<r`.  If every label is increased
modulo `r+1`, direct relabeling of each edge gives the target lower-endpoint
multiplicities

```text
d'_0=sum_(a=0)^(r-1) epsilon_a=deg_G(r),
d'_j=d_(j-1)-epsilon_(j-1),  1<=j<=r-1.             (2.20)
```

Thus the transformation depends on incidences not retained by `d`.  The
smallest mismatch is `r=2`: the two factorizations with edge lists
`(01),(12)` and `(12),(02)` both have source vector `(1,1)`, but conjugate
to vectors `(1,1)` and `(2,0)`.  Even conditional coordinate
exchangeability within one target histogram fails at `r=3`: from source
`(1,1,1)`, target `(2,0,1)` occurs once while `(2,1,0)` occurs twice.
Conjugation remains a global microstate bijection and hence gives an
averaged stationary macro kernel; it is not a deterministic rerooting of
the degree vector.  `conjugation_macro_audit.py` exactly verifies (2.20)
and records the minimal witnesses through `r=6`; the finite enumeration is
used only to exhibit the universal claim's counterexamples.

### 2.10 Fresh M49 original-`K` referee

I independently audited M49's strand erasure, exactly two null increments,
output join tree, `(N-1)^2` fixed-position lift bound, even endpoint,
injective square reservoir, triple-fiber count, and global stationary
orientation.  The frozen M49 report
`a809459cb1babfa445776d922fc1fa733eb905e1a4bdff6c15fb4f0d9f33dcdc`
is **ACCEPTED with no numbered objection**.  Independent `N=4,5` reruns
reproduced the fixed-position maxima `8<=9` and `13<=16`.  The complete
audit is `m49_referee_report.md`.

### 2.11 Fresh M51 original-`K` referee

I independently audited both reverse-insertion counts, including the
`q=N-1` star layer, the maximum-degree one-attachment reservoir, layer
indexing, exact `H3` normalization, and global mass orientation.  The frozen
M51 report
`919349e3f7ea32eb6f7524a7b22e5679d27a271378c4ff31b2fee9d4c935c62e`
is **ACCEPTED with no numbered objection**.  An independent exact rerun
passed all 20 leaf and 20 maximum-degree rows through `N=8`.  The complete
audit is `m51_referee_report.md`.

### 2.12 Fresh M41 Cayley-exchange referee

The graphic-matroid basis polynomial satisfies the exact hypotheses of
Anari--Liu--Oveis Gharan--Vinzant Theorem 1.1.  Delete-uniform-edge and
add-uniform-cross-edge (including the deleted edge) is literally their
rank-`r` down-up chain, so its gap is at least `1/r`.  The child-sort fiber
has size `r!/product_i d_i!`; regrouping stationary flow preserves macro
variance and Dirichlet form exactly.  The theorem, `r=1,2` normalization,
and exact conditional-fiber runtime are **ACCEPTED with no numbered
objection**.  See `m41_cayley_exchange_referee.md`.

### 2.13 Fresh M52 macro-closed referee

Low-tail deletion, canonical old-leaf/centroid insertion, both global mass
orientations, the even balance endpoint, and the complete six-term
`H3/H4/H5` macro/internal decomposition all survive audit.  The frozen M52
report
`6d157387016e8cc126380e45d3f2d80390ddf338fb6991724073b6ae5cf0db7e`
is **ACCEPTED with no numbered objection**.  The independent exact rerun
passes all 24 low-tail rows through `N=8`; see `m52_referee_report.md`.

## 3. Probability, runtime, path, and congestion accounting

- Exact `L_r` edge rates are `c_r d_i` forward and `c_r` reverse, where
  `c_r=2/[3r(r-1)]`.  The common unnormalized capacity is
  `c_r w(d)d_i=c_r w(d')`.
- `Y_r` has at most `r(2r-1)` neighbours, laziness at least `1/2`,
  polynomial enumeration/weight evaluation per step, and gap lower bound
  `1/[16(r+1)^8]`.
- The M41 comparison paths have length at most `2r`; their proved congestion
  is at most `16(r+1)^8`.
- Equation (1.5) proves that no polynomial-congestion flow from `Y_r` to
  `L_r` exists.  The separator has two stationary reservoirs bounded below
  by constants and boundary flow at most `b_r`.
- The same set has full-projection boundary flow at least
  `4(beta_r-b'_r)/[3r(r-1)]`; the aggregate heat-bath normalization includes
  both the three-outcome fibre and the `r-1` scan sites.
- The exact root-degree projected gap is at least
  `4(r+1)/[3r^2(r-1)]`.  Every balanced leaf-count threshold has stationary
  boundary flow at least `1/[60(r+1)(r-1)]`.
- M49's original-`K` certificate has one-step probability
  `1/[6(2N-4)D_N^3]` and source fraction at least order `N^-3`, yielding
  `Phi_pm>=1/(96N^6)`.  M51's degree-threshold source fraction is at least
  order `N^-4`, yielding `Phi_pm>=1/(24N^7)`.
- The Cayley basis-exchange source and its child-sort projection have gap at
  least `1/r` and exact polynomial-time steps.  M52's macro-closed scalar
  thresholds have full-`K` flow at least `1/(24N^7)` in both orientations.
- Exact leaf graphs through `r=9` are connected.  Their state counts are
  Catalan and their edge counts are
  `1,4,15,56,210,792,3003,11440` for `r=2,...,9`.
- Sparse eigensolves give gaps approximately
  `1.018e-3,2.208e-4,6.555e-5,2.242e-5,8.363e-6` for `r=5,...,9`, close to
  `380r^-8`.  This is numerical evidence only.
- For `C_r` versus `P_r`, exact finite widest-vertex paths lose weight
  factors `3,12,12,60,60,60,60,360,360,360` for `r=3,...,12`.  This
  refutes naive monotone/hub routing in those instances but proves no
  asymptotic lower bound.
- Exact max-flow for the same pair has capacity divided by `w(C_r)` between
  `0.18` and `1` through `r=9`, and the appropriately scaled effective
  resistance stays below `20`.  Parallel paths defeat that one finite
  widest-path obstruction, but the stationary separator proves the global
  simultaneous comparison impossible.
- Among Caraceni right-peak translations, density-monotone M35 simulations
  first fail at `r=5`; through `r=9` the exact failure counts are
  `0,0,0,1,6,26,106,418` for `r=2,...,9`.
- All enumeration runtimes are Catalan/exponential in `r` and are bounded
  falsifiers only.  No finite convergence is used as proof.

## 4. Dependencies, labeled

- **Proved/refereed here:** M35 exact leaf count and reverse rate; M41
  weighted-replanting gap; the superpolynomial `L_r` separator; its exact
  polynomial-flow bypass under `Pbar_r`; the root-degree projection gap;
  balanced leaf-count threshold flow; LCRS pointer identity; smallest
  standard-flip mismatch; the `r=5` monotone-density counterexample; and
  the exact nonlumpability formula for long-cycle conjugation.
- **Fresh-refereed here:** M49's original-`K` symmetric branch-balance
  theorem, M51's original-`K` leaf-count/maximum-degree theorems, M41's
  Cayley basis-exchange source theorem, and M52's macro-closed scalar-profile
  theorem.  All four frozen bundles are accepted with no numbered objection;
  their dependencies and limitations are expanded in the dedicated referee
  reports.
- **Cited and checked:** Goulden--Yong, JCTA 98 (2002), Theorem 2.2,
  Proposition 2.4, Lemma 2.5; the zero-based/project convention agrees after
  the accepted M27 translation.  Fleurat,
  <https://arxiv.org/html/2411.03065v3>, Theorem 4, applies to `1/k!` and
  adds a right-leaning leaf while preserving the root.
- **Cited and checked:** Komarath--Sarma--Sawlani,
  <https://arxiv.org/abs/1604.05510>, Theorem 12, equates persistent
  reversible pebbling on a directed tree with one plus the underlying
  edge-ranking number.  The path off-by-one is proved explicitly in §2.4.
- **Cited but nontransferable:** Eppstein--Frishberg,
  <https://arxiv.org/abs/2207.09972>, proves polynomial mixing for the full
  uniform convex-polygon triangulation flip walk.  Its state weights and
  moves do not match `L_r`.
- **Cited but nontransferable:** Anoop--Sarma,
  <https://arxiv.org/abs/2304.03985>, and Cleary--Nadeem,
  <https://arxiv.org/abs/2005.00518>, concern distances for standard
  rotations under rank/location restrictions, not this weighted chain.
- **Cited and re-derived:** Harper, *Ann. Math. Statist.* 38 (1967),
  410--414, doi:10.1214/aoms/1177698956.  Only the real-rooted
  Stirling-polynomial/log-concavity argument is used, not asymptotic
  normality.
- **Empirical exact/numerical only:** finite connectivity, bridge, degree-cut
  component masses, spectra, widest paths, max-flow, and effective
  resistance.  The asymptotic separator and nonlift use proofs, not these
  finite trends.
- **Not a dependency:** pointwise lower bounds for Fleurat's coupling; its
  compactness construction supplies none and M41 uses only aggregate balance.

## 5. First unproved standalone proposition

> **CAYLEY-EXCHANGE-TO-PARKING FLOW.**  There is a universal `C<infinity`
> such that every transition of the accepted child-sort Cayley
> stationary-flow projection can be routed, fractionally and with its exact
> stationary demand, through the actual nonlazy adjacent rank-two parking
> projection `Pbar_r` with congestion at most `r^C` for every `r>=2`.

Since the Cayley source gap is at least `1/r`, this proposition would prove
`gap(Pbar_r)>=r^(-C-1)`.  M50's root quotient and product restrictions give
the correct recursive geometry but do not yet prevent polynomial Radon
losses from multiplying through linear depth.  The leaf-only comparison
route is refuted by (1.5), and no pointwise child-sort locality is available.
Even a proof here would concern one minimal long-cycle sector and would not
by itself prove a gap for the original identity-word chain `K`.

## 6. Strongest self-attack

The proved bottleneck is deliberately for a strict subchain.  The full
projection has an order-`r^-2` aggregate route across a constant-mass
reservoir of precisely that cut, so treating the leaf rotations as the
dominant support would give the wrong spectral conclusion.  No present
argument controls all other projected transitions or constructs a different
balanced full-projection cut.  Even a full-projection theorem would remain
confined to a minimal long-cycle macro sector; it would not supply fiber
gaps, mean-lift control, or a gap/refutation for the original identity-word
chain `K`.  The new Cayley source avoids factorial stationary-density loss,
but a single labelled edge exchange can reorder a linear number of preorder
positions after child sorting; source labels are then unavailable to a naive
macro route.  M49--M52 reject broad scalar original-`K` cuts but all their
certificates use one-label exits and do not control joint profiles or
internal mixing.  Thus every result here remains nonterminal.

## 7. Calibration

- `r=1`: the auxiliary macro/replanting chains are singletons.
- `r=2`: the exact star-to-path rates are `2/3` and `1/3`; the binary move is
  a standard rotation; the root-degree projected gap is exactly one.
- `r=3`: the pebble cap is one; empty and `{2}` are separated for `L_3`,
  while the full projected edge `(2,1,0)->(1,2,0)` crosses the cut at rate
  `1/9` with both endpoints below `D_3=3`.
- `r=5`: the smallest Caraceni monotone-density obstruction has endpoint
  weights `30,20` and exact maximin floor `5`.
- Star/path stationary weight ratio is exactly `r!`, preventing uniform-law
  measure comparison.
- Repeated labels enter (2.1) through `d_i`; the reverse orientation and a
  newly rare label are covered by detailed balance.
- Exact factorization/count/contraction checks inherited from M35 pass
  through `n<=7`; the current independent interval audit passes every
  noncrossing tree through `n=7`, and the binary audit passes through `r=8`.
- Every balanced leaf threshold for `2<=r<=127` passes the exact occupancy
  audit; the minimum scaled certified flow is `9261/15625` at `(r,ell)=(9,4)`.
- Independent M49 reruns at `N=4,5` reproduce all deletion checks and fixed
  null-position fiber maxima `8<=9` and `13<=16`.  The independent M51
  consequence rerun passes all 40 leaf/maximum-degree rows through `N=8`.
- The Cayley source has exact gaps `1` at `r=1` by convention and `3/4` at
  `r=2`, versus the proved lower bound `1/r`.  The independent M52 rerun
  passes all 24 low-tail rows; at `N=4`, its opposite mass orientations are
  witnessed by closed-side masses `75/164` and `133/164`.
- The factor-three conditional-fibre and `r-1` scan normalization are both
  present in (1.1).  No old `14/15` capacity ratio is used without division
  by `3(r-1)`.
- Odd `m`, `m=0`, `N=2`, `m=2`, `S_3,m=4`, `S_4,m=4`, and `S_4,m=6` are
  outside this minimal long-cycle projection theorem.  Nothing here changes
  their stated empty/singleton/disconnected/exact-chain calibrations.  In
  particular `L_r`, `Y_r`, and the original half-lazy `{3,4,5}` chain `K`
  are explicitly distinguished.

## 8. Artifacts and reproduction commands

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-11/
  mission-M46-leaf-rotation-referee-redteam/
```

Commands:

```text
python3 interval_lemma_audit.py --n-max 7 --output interval_lemma_n7.json
python3 leaf_chain_bridge_probe.py --r-min 2 --r-max 9 --output bridge_results_r9.json
python3 leaf_chain_spectral_probe.py --r-min 2 --r-max 9 --output spectral_results_r9.json
python3 energy_barrier_probe.py --r-min 2 --r-max 12 --output energy_barriers_routes_r12.json
python3 degree_separator_probe.py --r 12 --threshold-min 3 --threshold-max 7 --output degree_separator_r12.json
python3 comb_flow_probe.py --r-min 3 --r-max 9 --output comb_flow_resistance_r9.json
python3 binary_rotation_audit.py --r-min 2 --r-max 8 --output binary_rotation_r8.json
python3 peak_translation_audit.py --max-r 9 --output peak_translation_r9.json
python3 full_projection_separator_audit.py --cycle-size-min 4 --cycle-size-max 7 --output full_projection_separator_n7.json
python3 conjugation_macro_audit.py --n-min 3 --n-max 7 --output conjugation_macro_n7.json
python3 leaf_count_small_r_audit.py --r-min 2 --r-max 127 --output leaf_count_small_r127.json
python3 ../../cycle-12/mission-M49-symmetric-branch-balance/strand_deletion_falsifier.py --N 4 --output /tmp/m46-m49-strand-N4-rerun.json
python3 ../../cycle-12/mission-M49-symmetric-branch-balance/strand_deletion_falsifier.py --N 5 --output /tmp/m46-m49-strand-N5-rerun.json
python3 ../../cycle-12/mission-M51-original-k-degree-profile-redteam/leaf_threshold_audit.py --source-dir ../mission-M47-branch-geometry-redteam --output /tmp/m46-m51-leaf-threshold-rerun.json
python3 ../../cycle-12/mission-M52-macro-closed-tree-profile-redteam/macro_closed_audit.py --source-dir ../mission-M47-branch-geometry-redteam --output /tmp/m46-m52-macro-closed-rerun.json
```

The scripts are deterministic.  No random seed is needed.  They state the
universal claim each bounded run could falsify and do not promote finite
success to an asymptotic theorem.

## 9. Verdict

**PROVED.**
