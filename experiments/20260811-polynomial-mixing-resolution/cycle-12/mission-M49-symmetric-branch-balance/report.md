# M49 final report: every symmetric balanced-edge threshold has polynomial full-`K` escape

Date: 2026-08-11.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

This report proves that the strongest natural label-symmetric balanced-edge /
centroid-branch threshold in the minimal full-support macro is not a
superpolynomial bottleneck.  The proof works with the actual weighted
prefix-join-tree law.  It does not prove a global spectral gap and is not
Terminal A or Terminal B.  The scoped verdict is `PROVED`.

## 1. Exact claim, quantifiers, and convention

Permutations are maps on `[N]`; `(pq)(x)=p(q(x))`, and a word evaluates as
`t_1...t_m`.  Put

```text
Omega(N,m)={w in T_N^m:t_1...t_m=id},
R_m={r in {3,4,5}:r<=m},
K=(1/2)I+(1/(2|R_m|)) sum_(r in R_m)
       (1/(m-r+1)) sum_i H_(i,r),
```

where `H_(i,r)` is exactly uniform on the same-product length-`r`
transposition fiber.  The stationary target `pi` is uniform on the **global**
`Omega(N,m)`.

For `N>=4`, set `m=2N-2`; then `|R_m|=3`.  Let

```text
F_N={w in Omega(N,m):the factor support is connected and equals [N]}.
```

The support-joining factors of `w in F_N` form its prefix join tree
`T_J(w)`.  If deleting an edge `e` of a tree `T` gives sides `C_e,C_e^c`,
define

```text
b_N(T)=max_(e in E(T)) min{|C_e|,N-|C_e|}.
```

For every integer `1<=q<=floor(N/2)`, define the literal global cut

```text
B_(N,q)={w in F_N:b_N(T_J(w))>=q}.                    (1.1)
```

All words outside `F_N` are in its complement.  Let

```text
D_N=(3N^2+N-12)/2.                                    (1.2)
```

### Theorem: uniform anti-bottleneck bound

For every `N>=4` and `1<=q<=floor(N/2)`, both sides of (1.1) are nonempty and
the exact full lazy chain satisfies

```text
Phi_pm^K(B_(N,q))
 :=Q_K(B_(N,q),B_(N,q)^c)
     /min{pi(B_(N,q)),pi(B_(N,q)^c)}
 >=1/(96N^6).                                         (1.3)
```

More precisely, if `q<N/2`,

```text
Phi_pm^K(B_(N,q))
 >=1/[3N(2N-2)(N-1)(2N-4)D_N]
 >=1/(24N^6).                                         (1.4)
```

At the exceptional endpoint `N=2q`,

```text
Phi_pm^K(B_(N,q))
 >=(N-2)/[6N(2N-2)(N-1)^2(2N-4)D_N]
 >=1/(96N^6).                                         (1.5)
```

The same statistic is the usual centroid branch radius:

```text
b_N(T)=min_(x in [N]) max{|C|:C is a component of T-{x}}.   (1.6)
```

Thus (1.3) covers both balanced-edge and largest-centroid-branch thresholds,
without choosing a distinguished root in the definition of the cut.

## 2. Full argument

### 2.1 Tree geometry and the even endpoint

Let the right-hand side of (1.6) be `c_N(T)`, and choose a centroid `x`.
Every component of `T-{x}` has size at most `N/2`.  If a largest such
component has size `c_N(T)`, the edge from `x` into it has smaller-side size
`c_N(T)`, so `b_N(T)>=c_N(T)`.  Conversely, for any edge, its side not
containing `x` lies in one centroid branch, has size at most `c_N(T)<=N/2`,
and is therefore the smaller side.  Hence `b_N(T)<=c_N(T)` and (1.6) follows.

Suppose `q<N/2` and `b_N(T)>=q`.  Choose an edge whose two sides both have
size at least `q`; one side has size at least `q+1`.  Its induced subtree has
a leaf other than the bridge endpoint.  That vertex is a leaf `v` of `T`,
and after deleting it the two sides of the witness edge still have size at
least `q`.  Therefore

```text
b_(N-1)(T-v)>=q.                                      (2.1)
```

If `N=2q` and `b_N(T)=q`, the perfectly balanced edge is unique.  No tree
leaf is its bridge endpoint because `q>=2`.  Deleting any leaf leaves that
edge split `q-1` versus `q`; since `q-1` is the maximum possible balance on
`2q-1` vertices,

```text
b_(N-1)(T-v)=q-1.                                    (2.2)
```

### 2.2 Erasing one permutation strand

Fix a label `v` and write `X=[N]\\{v}`.  For `sigma in S_N`, define
`d_v(sigma) in S_X` by erasing `v` from its permutation cycle:

```text
d_v(sigma)(x)=sigma(x),  if sigma(x)!=v,
             sigma(v),  if sigma(x)=v.                (2.3)
```

Every `sigma` is uniquely described by `bar sigma=d_v(sigma)` and an
insertion coordinate `a in X union {bottom}`.  If `a=bottom`, `v` is fixed.
Otherwise

```text
sigma(a)=v, sigma(v)=bar sigma(a),
sigma(x)=bar sigma(x) for x notin {a,v}.              (2.4)
```

The following right-multiplication table is immediate from (2.4).  If
`x,y in X`, then

```text
t=(xy):       d_v(sigma t)=bar sigma (xy),
              new coordinate=(xy)(a),                 (2.5)
```

where `(xy)(bottom)=bottom`.  If `t=(v x)`, then

```text
a=bottom:     d_v(sigma t)=bar sigma,  new coordinate=x;
a=x:          d_v(sigma t)=bar sigma,  new coordinate=bottom;
a notin {x,bottom}:
              d_v(sigma t)=bar sigma (a x), new coordinate=a.  (2.6)
```

Consequently, for a prefix path `sigma_j=t_1...t_j`, every increment

```text
s_j=d_v(sigma_(j-1))^(-1)d_v(sigma_j)                 (2.7)
```

is either the identity or a transposition.

### 2.3 The leaf-strand deletion lemma

Let `w in F_N`, and suppose `v` is a leaf of `T_J(w)`.  Its first incident
factor is its unique support join.  Immediately before that factor `v` is
fixed, so (2.6) shows that this factor gives an identity increment in (2.7).
Every other join-tree edge avoids `v` and survives as the same transposition
under (2.5).  Thus the nonidentity increments have connected support on `X`.
Their product is the identity by telescoping (2.7).

A connected identity transposition word on `N-1` labels has length at least
`2N-4`: it needs at least `N-2` support joins, hence at least `N-2`
permutation-cycle joins, and returning to the identity needs the same number
of cycle cuts.  The nonidentity projected length is therefore at least
`2N-4`.  The number of identity increments is positive and even by sign,
while the old length is `2N-2`.  Hence there are exactly two identity
increments, and deleting them produces a word

```text
Del_v(w) in F_(N-1).                                  (2.8)
```

Its join tree is exactly `T_J(w)-v`.  To see this, consider any prefix join
forest of `w`.  Once the unique join edge at `v` appears, removing leaf `v`
from its component leaves that component connected.  The prefix permutation
preserves every prefix support component.  Thus if an internal factor
`(v,x)` projects by (2.6) to `(a,x)`, both `a` and `x` lie in the same
leaf-deleted prefix component.  It remains internal.  The only projected
support joins are consequently the surviving old join edges, exactly
`T_J(w)-v`.

### 2.4 Polynomial multiplicity of deletion

Fix `v`, a base word `w' in F_(N-1)`, and the two locations of the identity
increments among the `m=2N-2` projected steps.  Before the first null step
the insertion coordinate is `bottom`; this step chooses one of `N-1`
coordinates in `X`.  Between the null steps, table (2.5)--(2.6) describes all
possible lifts.

In any minimal word in `F_(N-1)`, every support join is a permutation-cycle
join and every other factor is a cycle cut.  Indeed, connected support needs
`N-2` support joins; the length `2N-4` identity path has exactly `N-2`
cycle joins and `N-2` cuts.  At a projected support join the lift is forced
to be the same `X`-transposition: a `v`-incident alternative in (2.6) would
create a second join-tree edge at `v`.

At a projected cycle cut, one current lift can branch into at most two.  The
two descendants occupy the two distinct permutation cycles created by that
cut.  Descendants of one initial coordinate thereafter occupy pairwise
distinct cycles.  A support join can merge the current support component
with another component but cannot merge two descendant cycles already in the
same support component; doing so would be an additional internal cycle join,
which minimality forbids.  A later cut splits only one current cycle, so it
preserves the distinct-cycle invariant.  There are at most `N-1` cycles.

There are therefore at most `(N-1)^2` lifts for fixed null positions: `N-1`
initial coordinates, each with at most `N-1` descendants.  The second null
step and every step after it are then forced.  Summing over the two null
positions gives the uniform fiber bound

```text
L_N=binom(m,2)(N-1)^2.                               (2.9)
```

This is an upper bound; invalid branches have only been overcounted.

### 2.5 Exact threshold-count inequalities

Let

```text
H_N(q)=|B_(N,q)|.
```

For `q<N/2`, every word counted by `H_N(q)` has at least one leaf satisfying
(2.1).  Count a word together with one such leaf, apply (2.8), and use the
fiber bound (2.9).  There are `N` possible deleted labels, so

```text
H_N(q)<=N L_N H_(N-1)(q).                            (2.10)
```

For `N=2q`, (2.2) instead gives

```text
H_N(q)<=N L_N H_(N-1)(q-1).                          (2.11)
```

No uniform-Cayley or asymptotic join-tree approximation occurs in these
inequalities.

### 2.6 An overlap-free boundary reservoir

Fix the new label `v=N`.  A base word has length `m-2=2N-4` and hence
`m-1=2N-3` gaps.  For `q<N/2`, take any word counted by `H_(N-1)(q)`, choose
an attachment label `u` in `N-1` ways, and insert

```text
(v,u),(v,u)                                           (2.12)
```

in one gap.  Adding a leaf never decreases the smaller-side size of an old
tree edge, so every resulting word belongs to `B_(N,q)`.  These sources are
distinct: `v` occurs in exactly the displayed adjacent square, which recovers
the base word, attachment, and gap.  Their exact number is

```text
|S_(N,q)|=(N-1)(m-1)H_(N-1)(q).                      (2.13)
```

At the even endpoint `N=2q`, every base tree in the maximum layer `q-1` has
an edge split `q-1,q`.  Select one deterministically, for example the
lexicographically first labeled edge, and orient its side of size `q-1`.
Attach `v` to any of the `q-1` labels on that side.  The chosen edge then
splits `q,q`, and the same uniqueness argument gives

```text
|S_(N,q)|=(q-1)(m-1)H_(N-1)(q-1).                    (2.14)
```

This is the correction needed because `H_(N-1)(q)=0` at the endpoint.

### 2.7 Exact original-`K` exit and full boundary flow

For each source, use the `H3` window beginning with the square in (2.12), or
the window ending with it if the square is the final pair.  With padding
transposition `a` and any fixed transposition `f` on the base labels, specify

```text
((vu),(vu),a) -> (f,f,a),
(a,(vu),(vu)) -> (a,f,f),                             (2.15)
```

respectively.  Old and new block products are equal to `a`.  The target word
contains no factor incident to `v`, so it lies outside `F_N` and hence outside
`B_(N,q)`.

For fixed `a`, the exact length-three fiber size is

```text
D_N=M+6(N-2)+2 binom(N-2,2)
   =(3N^2+N-12)/2,  M=binom(N,2).                     (2.16)
```

Condition on the first factor: if it equals `a`, shares one endpoint with
`a`, or is disjoint from `a`, the remaining two-factor product has
respectively `M`, `3`, or `2` ordered decompositions.  Including laziness,
the uniform choice among three block sizes, the `m-2` three-windows, and the
uniform conditional fiber, the specified transition has exact probability

```text
p_N=1/[6(m-2)D_N].                                    (2.17)
```

Decompose the complete boundary flow as

```text
Q_K(B,B^c)=Q_3(B,B^c)+Q_4(B,B^c)+Q_5(B,B^c)
          >=pi(S_(N,q))p_N.                           (2.18)
```

Thus every `H4,H5` edge and every other `H3` edge is retained as nonnegative
flow; none is discarded from the kernel.  Exact stationary masses are

```text
pi(B_(N,q))=H_N(q)/|Omega(N,m)|,
pi(S_(N,q))=|S_(N,q)|/|Omega(N,m)|.                  (2.19)
```

For either mass orientation,

```text
min{pi(B),pi(B^c)}<=pi(B).                            (2.20)
```

Using (2.10), (2.13), and (2.17) in (2.18)--(2.20) gives

```text
Phi_pm(B)>=2/[Nm(N-1)] * 1/[6(m-2)D_N],              (2.21)
```

which is (1.4).  Using (2.11), (2.14) gives

```text
Phi_pm(B)>=(N-2)/[Nm(N-1)^2] * 1/[6(m-2)D_N],        (2.22)
```

which is (1.5).  Finally `m<=2N`, `m-2<=2N`,
`D_N<=2N^2`, and `N-2>=N/2` establish the displayed coarse constants.

A paired path word has balance `floor(N/2)`, so every cut is nonempty.  The
disconnected identity word `(12)^m` is in the global complement, so the other
side is nonempty even when `q=1`.

## 3. Probability, runtime, path length, and congestion accounting

- Every certified source uses one literal transition of the original chain;
  there is no comparison path, path length, vertex load, or congestion.
- The exact specified-transition probability is (2.17), including every
  normalization.  Since `D_N=O(N^2)` and `m=O(N)`, it is `Omega(N^-3)`.
- The certified source fraction relative to `B_(N,q)` is at least
  `2/[Nm(N-1)]` off the endpoint and
  `(N-2)/[Nm(N-1)^2]` at the endpoint, both `Omega(N^-3)`.
- Their product is the `Omega(N^-6)` bound (1.3).
- Constructing `T_J`, performing strand deletion, or recognizing a source is
  polynomial in `N,m`.  Directly listing the `D_N` triple fiber costs
  `O(N^2)`; the inherited exact block samplers are polynomial.
- The exact falsifier enumerates `|F_N|=(2N-2)!N^(N-3)` states and is
  intentionally exponential.  The complete `N=5` audit took 85.63 seconds
  on Python 3.12.3.  It is not proposed as an implementation of `K`.

## 4. Dependencies, each labeled

1. **PROVED HERE:** the centroid/edge-balance identity; both leaf-deletion
   tree lemmas; the strand-deletion map; exactly two null increments; output
   join tree `T-v`; the `(N-1)^2` fixed-position lift bound; the threshold
   count inequalities; endpoint correction; and Theorem (1.3).
2. **INHERITED PROVED, ALSO RE-DERIVED WHERE USED:** minimal connected
   identity words have `N-1` cycle joins and `N-1` cuts; their join factors
   form a tree; exact heat-bath reversibility/stationarity; and the `D_N`
   triple-fiber formula.
3. **EXACT FINITE:** exhaustive Hurwitz-orbit audits at `N=4,5`.  They can
   falsify the named universal deletion statements but finite agreement is
   not used to prove them.
4. **EMPIRICAL:** none.
5. **LITERATURE:** no new literature theorem is required.  In particular,
   the auxiliary plane-tree/parking growth law is not identified with the
   prefix join-tree law.

## 5. First unproved standalone proposition

> **LABEL-SYMMETRIC DEGREE-PROFILE THRESHOLD FLOW.**  Let
> `ell(T)` be the number of leaves of a tree.  There are universal constants
> `c>0,C<infinity` such that, for every `N>=4` and every nontrivial threshold
> `2<=q<=N-1`, the global cuts
>
> ```text
> L_(N,q)={w in F_N:ell(T_J(w))>=q}
> ```
>
> satisfy
>
> ```text
> Q_K(L_(N,q),L_(N,q)^c)
> /min{pi(L_(N,q)),pi(L_(N,q)^c)} >=cN^(-C).
> ```

This statistic is not determined by the rooted branch threshold of M47 or by
the symmetric centroid threshold proved here.  A theorem for an auxiliary
uniform plane-tree leaf chain does not prove this proposition because both
the stationary join-tree weights and the projected original-`K` moves differ.

## 6. Strongest self-attack / failure mode

The proof depends essentially on defining the cut as a subset of the minimal
macro `F_N`: the certified update deletes label `v` and exits that macro.  An
enlarged cut containing the missing-label target can seal every certified
edge.  Likewise, refinements inside one balance layer, leaf-count or full
degree-profile cuts, and surplus-length words are not controlled.

The deletion bound is only a many-to-one counting inequality; it does not
give a sampling-consistent join-tree growth process or an arbitrary-cut
Poincare inequality.  Ignoring `H4,H5` is legitimate only for this lower-flow
proof; it would be invalid in an upper-flow Terminal-B argument.  Therefore
(1.3) rejects this candidate bottleneck but does not materially imply the
universal gap theorem by itself.

## 7. Calibration suite

- **Odd `m`:** `Omega(N,m)` is empty by sign.  The theorem uses even
  `m=2N-2`.
- **`m=0`, `N=2`:** singleton cases lie outside `N>=4`.
- **`m=2,N>=3`:** excluded disconnected case; no length-two simulation is
  used.
- **`S_3,m=4`:** there are 27 words and four pure-Hurwitz components.  Here
  `R_m={3,4}` and `H4` is a whole-word heat bath of coefficient `1/4`, so it
  cannot be omitted.  This endpoint is outside the theorem's `N>=4` range.
- **`S_4,m=4`:** there are 120 words and 13 pure-Hurwitz components; again
  the whole-word `H4` contribution is retained.
- **`S_4,m=6`:** there are 3936 global words and 17 pure-Hurwitz components;
  `|F_4|=2880`.  Exact balance layers are `744,2136` at balances `1,2`.
  Every leaf deletion has two null steps, the largest fixed-null-position
  fiber is `8<=9`, and the exceptional endpoint construction is nonempty.
- **`S_5,m=8` bounded audit:** all 1,008,000 words of `F_5` pass every leaf
  deletion check; the largest fixed-position fiber is `13<=16`; exact
  balance layers are `44,280` and `963,720`.
- **Near-minimal doubled trees:** included without requiring an adjacent
  square in the input.  A join-tree leaf may occur in more than two factors;
  strand deletion still applies.
- **Disjoint components/order:** source and target remain literal ordered
  words.  The target exits `F_N` but remains in global `Omega`; no graph-only
  chain or color-interleaving quotient is substituted.
- **Parity:** sign is used only to count the two null increments.  Edge or
  degree parity is not asserted to characterize identity words.
- **Canonical hub / `L=2`:** no hub, normal form, or length-two local
  simulation occurs.
- **Mass orientation:** equations (2.19)--(2.20) use the exact global mass
  and handle whichever side is smaller.

## 8. Artifact paths and reproduction commands

Owned artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M49-symmetric-branch-balance/
  plan.md
  checkpoint.md
  report.md
  strand_deletion_falsifier.py
  strand-N4.json
  strand-N5.json
```

There is no bytecode cache in the frozen directory.  Exact deterministic
commands (`seed=null`, no nonstandard dependency):

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M49-symmetric-branch-balance/strand_deletion_falsifier.py --N 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M49-symmetric-branch-balance/strand-N4.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M49-symmetric-branch-balance/strand_deletion_falsifier.py --N 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M49-symmetric-branch-balance/strand-N5.json
```

SHA-256 hashes:

```text
4eb6865697f98607a595cc4b2ca89a8b618a240c4c417281e83ad03f048aebac  strand_deletion_falsifier.py
644c42e4ed4f3af1c2552d5d9f9a147dbec480910731af39f0ba8e582c0cc783  strand-N4.json
aae8da55d2090e52457d510d2aaf1971aea3b83c04dfa63a0d65bd7e259f4bd1  strand-N5.json
```

Both JSON files record commit, Python version, convention, exact claims that
the computation could falsify, elapsed time, and complete integer outputs.

## 9. Verdict

**PROVED.**

This verdict is scoped to the uniform full-`K` inverse-polynomial rejection
of every label-symmetric balanced-edge / centroid-branch threshold cut
(1.1).  It is not Terminal A or Terminal B.  The next distinct original-`K`
candidate is the degree-profile/leaf-count proposition in section 5.
