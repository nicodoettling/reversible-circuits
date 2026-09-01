# M53 final report: macro-closed joint leaf/balance thresholds have polynomial full-`K` escape

The strongest natural two-statistic refinement named by M52 is not a
bottleneck.  Both placements of the entire nonminimal complement have
two-sided conductance at least `1/(24N^7)`.  The proof is for the literal
ordered-word chain and uses an exact `H3` subflow; it is not a projection-only
or auxiliary-tree statement.

## 1. Exact claim, quantifiers, and conventions

Permutations are maps on `[N]`, `(pq)(x)=p(q(x))`, and a word evaluates as
`t_1...t_m`.  Let

```text
Omega(N,m)={t in T_N^m:t_1...t_m=id},
```

with uniform law `pi`.  For `N>=4` put `m=2N-2`, and let `F_N` be the set of
connected full-support words in `Omega(N,m)`.  These are the minimal
connected identity words.  Their prefix cycle-join factors form a labeled
tree `T_J(w)`.

For a tree `T` on `N` vertices define

```text
ell(T)=number of degree-one vertices,
b(T)=max_(e in E(T)) min{|C_e|,N-|C_e|},
```

where `C_e` is either component of `T-e`.  For

```text
2<=q<=N-1,       1<=r<=floor(N/2),
H=J_(N,q,r)={w in F_N:ell(T_J(w))>=q and b(T_J(w))>=r},
C=F_N minus H,
```

consider the two global cuts

```text
A_+=F_N^c union H,          A_-=F_N^c union C.       (1.1)
```

The exact lazy chain is

```text
K=(1/2)I
  +(1/6) sum_(s in {3,4,5})
       (1/(m-s+1)) sum_(i=1)^(m-s+1) H_(i,s),        (1.2)
```

where each `H_(i,s)` is uniform on the exact same-product length-`s`
transposition fiber.  Write

```text
Q_K(A,B)=sum_(x in A,y in B) pi(x)K(x,y),
Phi_pm(A)=Q_K(A,A^c)/min{pi(A),pi(A^c)}.
```

**Theorem.**  Whenever either cut in (1.1) is nontrivial,

```text
Phi_pm(A_+), Phi_pm(A_-)
 >= 1/[3Nm(N-1)^2(m-2)D_N]
 >= 1/(24N^7),                                    (1.3)

D_N=(3N^2+N-12)/2.                                 (1.4)
```

The assertion for a trivial cut is simply omitted.  In particular, (1.3)
does not assume that both `H` and `C` are nonempty and does not guess which
global side has mass at most `1/2`.

The verdict **PROVED** below is scoped to (1.3).  It is neither Terminal A nor
Terminal B.

## 2. Full argument

### 2.1 Minimal join trees and the strand-deletion lemma

For `w in F_N`, every transposition changes the number of cycles of the
prefix permutation by one.  Connected support needs at least `N-1` prefix
cycle joins.  Since the word returns to the identity and has length
`2N-2`, it has exactly `N-1` joins and `N-1` cuts.  The support-join edges are
therefore a tree, denoted `T_J(w)`.

We use the following leaf-strand statement, proved in M49 and accepted by a
fresh independent referee.  If `v` is a leaf of `T_J(w)`, erase `v` from
every prefix permutation.  Each induced increment on the other labels is a
transposition or the identity; exactly two increments are identities.
Deleting those two null increments gives a word in `F_(N-1)`, and its join
tree is exactly `T_J(w)-v`.

Here is the multiplicity argument needed below.  Encode a lift of a
permutation on the old labels by the insertion coordinate of `v` in its
cycle, with a separate symbol when `v` is fixed.  A factor avoiding `v`
projects unchanged.  A factor `(v,x)` either creates a null increment when
it inserts or removes `v`, or projects to the transposition between `x` and
the current insertion coordinate.  The unique support join incident to `v`
supplies a null.  The projected nonnull word is connected and identity, so
it has length at least `2N-4`; parity makes the positive null count even.
Thus there are exactly two nulls.

For a fixed deleted label, projected word, and pair of null positions, there
are at most `(N-1)^2` lifts.  There are `N-1` possible first insertion
coordinates.  A projected support join has a forced lift.  A projected cut
may split one insertion history into two descendants, but the descendants
occupy distinct permutation cycles in the same support component.  Minimality
forbids a later internal cycle join, so one initial coordinate has at most
`N-1` descendants.  The second null and all later lifts are then forced.
Consequently, after summing the two null positions, the deletion fiber for a
fixed deleted label is at most

```text
Lambda_N=binom(m,2)(N-1)^2.                          (2.1)
```

This is a counting map, not a canonical-path route through a small hub.

### 2.2 Effect of leaf deletion on the two statistics

If `v` is a tree leaf, then

```text
ell(T)-1 <= ell(T-v) <= ell(T).                       (2.2)
```

Indeed the old leaf disappears and its neighbor becomes a new leaf exactly
when that neighbor had degree two.

For every surviving edge, deletion of `v` changes one of its two side sizes
by one.  Hence its balance changes by at most one and never increases.  A
balance-witness edge with balance at least two cannot itself be the deleted
leaf edge.  Thus

```text
b(T)-1 <= b(T-v) <= b(T),                             (2.3)
```

where the lower bound is automatic when `b(T)=1`.

Let `H_N(q,r)=|H|`, `C_N(q,r)=|C|`.  Choose one leaf of each input tree
deterministically and apply strand deletion.  The deleted label has `N`
choices; on any fixed remaining label set the profile count equals the
corresponding count on `[N-1]` by relabeling.  Equations (2.1)--(2.3) give

```text
H_N(q,r) <= N Lambda_N H_(N-1)(q-1,r-1),             (2.4)
C_N(q,r) <= N Lambda_N C_(N-1)(q,r).                 (2.5)
```

Thresholds below the minimum statistic are interpreted literally as
vacuous.  No profile-unimodality or stationary-tail estimate is used.

### 2.3 One insertion restores both high constraints

Take a tree `T` on the fixed old label set `[N-1]` satisfying

```text
ell(T)>=q-1,       b(T)>=r-1.                         (2.6)
```

Adding a new leaf never decreases the balance of an old edge.  Choose an
attachment vertex as follows.

1. If `ell(T)>=q` and `b(T)>=r`, any deterministic vertex works.
2. If `ell(T)=q-1` and `b(T)>=r`, choose a nonleaf.  Such a vertex exists in
   every tree on at least three vertices, and the attachment raises `ell` by
   one.
3. If `ell(T)>=q` and `b(T)=r-1`, choose a balance-witness edge, orient a
   smaller side of size `r-1`, and attach anywhere on that side.  The old
   split becomes `r` versus `N-r`, so its balance is at least `r` because
   `r<=floor(N/2)`.
4. If both constraints are tight and `r-1>=2`, use the endpoint of that
   witness edge lying in the smaller side.  It has an internal neighbor on
   its side as well as the bridge edge, so it is a nonleaf.  This attachment
   raises both statistics.

The only apparent missing corner is simultaneous tightness with `r-1=1`.
A tree of balance one is a star, so it has `N-2` leaves.  Tightness then
forces `q=N-1`.  But an `N`-vertex tree with `N-1` leaves is also a star and
has balance one; hence `H_N(N-1,2)=0`.  Therefore whenever the high side is
nonempty every base in (2.6) has a valid attachment.  The same construction
handles the even endpoint `r=N/2`: a base split `r-1,r` becomes `r,r`.

Fix the new label `v=N` and make the choice deterministic using label order.
For each base word counted by `H_(N-1)(q-1,r-1)`, insert the adjacent square
`(v,u),(v,u)` in any one of the `m-1` gaps.  The first copy is the unique new
prefix join and the second copy is a cut, so the new join tree is exactly
`T+{v,u}`.  Since `v` appears nowhere else, the source word recovers `v`, the
base word, its gap, and its attachment.  Thus there are exactly

```text
|S_H|=(m-1)H_(N-1)(q-1,r-1)                          (2.7)
```

distinct high-profile sources whenever `H_N(q,r)>0`.

### 2.4 One insertion preserves the joint complement

Now take a base word counted by `C_(N-1)(q,r)`.

- If `ell(T)<q`, attach `v` to a deterministic old leaf.  The old leaf
  becomes degree two and `v` becomes a leaf, so `ell` is unchanged and the
  result remains in `C`.
- Otherwise `ell(T)>=q` and necessarily `b(T)<r`.  Attach `v` at a
  deterministic centroid `u`.  Orient every old edge away from `u`.  Its
  away-component lies in one centroid branch and has size at most half the
  old tree.  Adding `v` on the `u` side therefore leaves the balance of every
  old edge unchanged; the new leaf edge has balance one.  Hence the new
  balance is exactly `b(T)<r`.

The same recovery argument gives exactly

```text
|S_C|=(m-1)C_(N-1)(q,r)                              (2.8)
```

distinct complement-profile sources whenever `C_N(q,r)>0`.

Combining (2.4)--(2.8), both relevant source fractions obey

```text
|S_H|/H_N(q,r), |S_C|/C_N(q,r)
 >=(m-1)/(N Lambda_N)
 =2/[Nm(N-1)^2].                                     (2.9)
```

Only the ratio whose denominator is nonzero is asserted.

### 2.5 Exact padded-`H3` exit

For a source in (2.7) or (2.8), use the length-three window beginning with
the marked square, except at the final gap use the window ending with it.
Let `a` be the neighboring old-label transposition and fix any old-label
transposition `f`.  Specify the outcome

```text
((vu),(vu),a) -> (f,f,a),
(a,(vu),(vu)) -> (a,f,f).                            (2.10)
```

Both ordered block products are `a`.  The target omits `v`, so it is a
global identity word in `F_N^c`.

For any transposition product `a`, exact enumeration of the length-three
fiber gives

```text
D_N=binom(N,2)+6(N-2)+2binom(N-2,2)
   =(3N^2+N-12)/2.                                   (2.11)
```

Half-laziness, uniform choice among the three block sizes, uniform choice
among all `m-2` triple windows, and uniform conditional-fiber sampling make
the probability of (2.10) exactly

```text
p_N=(1/2)(1/3)(1/(m-2))(1/D_N)
   =1/[6(m-2)D_N].                                   (2.12)
```

### 2.6 Literal global mass orientation and complete boundary flow

Let `Z_N=|Omega(N,m)|`, `H_N=H_N(q,r)`, and `C_N=C_N(q,r)`.  The exact masses
are

```text
pi(A_+)=1-C_N/Z_N,       pi(A_+^c)=C_N/Z_N,
pi(A_-)=1-H_N/Z_N,       pi(A_-^c)=H_N/Z_N.          (2.13)
```

For `A_+`, the sources `S_C` lie in `A_+^c` and (2.10) lands in
`F_N^c subset A_+`.  Uniform heat-bath reversibility gives
`Q_K(A_+,A_+^c)=Q_K(A_+^c,A_+)`.  Since
`min{pi(A_+),pi(A_+^c)}<=C_N/Z_N`, (2.9)--(2.12) yield

```text
Phi_pm(A_+) >= 1/[3Nm(N-1)^2(m-2)D_N].              (2.14)
```

The identical argument from `S_H` proves (2.14) for `A_-`, using
`min mass<=H_N/Z_N`.  This handles either global mass orientation, including
cases in which the side containing `F_N^c` has mass below `1/2`.

For completeness, decompose the literal boundary flow as

```text
Q_K=Q_(3,macro)+Q_(3,internal)
   +Q_(4,macro)+Q_(4,internal)
   +Q_(5,macro)+Q_(5,internal).                      (2.15)
```

The specified outcomes contribute to `Q_(3,macro)`.  Every other `H3`
outcome, every internal crossing, and all `H4,H5` contributions remain in
(2.15) as nonnegative flow.  Dropping them is valid for this lower bound; an
upper-flow Terminal-B argument could not do so.

Finally, `m<=2N`, `m-2<=2N`, `(N-1)^2<=N^2`, and `D_N<=2N^2`, so the exact
denominator in (2.14) is at most `24N^7`.  This proves (1.3).

## 3. Worst-case probability, runtime, path length, and congestion

- Specified transition probability: exactly `p_N=1/[6(m-2)D_N]`.
- Certified source fraction on the needed profile side: at least
  `2/[Nm(N-1)^2]`.
- Total conductance rate: the product in (1.3); no hidden block-size, window,
  laziness, or fiber factor remains.
- A direct prefix-permutation implementation constructs the join tree, a
  leaf, a balance witness or centroid, and one source in `O(Nm)` elementary
  operations (faster dynamic-cycle bookkeeping is unnecessary).  The used
  conditional fiber has explicit size `D_N=O(N^2)`.
- No comparison path is routed and no congestion claim is made.  Each source
  uses one actual `K` edge.
- The exact bounded audit processed 61 threshold pairs and 108 shape-level
  attachment families through `N=8`; the observed shell-command wall time
  was 3.6 seconds on Python 3.12.3.  This runtime is diagnostic only.

## 4. Dependencies with status

1. **PROVED HERE:** the joint deletion inequalities, simultaneous high
   attachment including the star and even-endpoint audit, low-complement
   attachment, source injectivity, global orientation, and full-flow bound.
2. **PROVED / FRESH-REFEREED:** the M49 leaf-strand deletion theorem and
   fixed-position lift multiplicity `(N-1)^2`; its argument is restated in
   section 2.1.
3. **PROVED INHERITED:** exact same-product heat baths are reversible for the
   uniform bridge law.
4. **PROVED BY DIRECT ENUMERATION:** the triple-fiber formula (2.11).
5. **CITED / NOT NEEDED FOR THE INEQUALITY:** the genus-zero count
   `|F_N|=(2N-2)!N^(N-3)` and the character-content formula for `Z_N` are used
   only to calibrate exact finite masses.
6. **EXACT FINITE:** the `N<=8` deletion and attachment audit.  It can refute
   the named universal lemmas but is not their proof.
7. **CONDITIONAL:** none.
8. **EMPIRICAL:** none.

## 5. First unproved standalone proposition

> **MACRO-CLOSED MIXED-QUADRANT FLOW.**  For all `N>=4` and feasible `q,r`,
> let
>
> ```text
> M_(N,q,r)={w in F_N:ell(T_J(w))>=q and b(T_J(w))<r}.
> ```
>
> Whenever nontrivial, each cut `F_N^c union M_(N,q,r)` and
> `F_N^c union (F_N minus M_(N,q,r))` has two-sided conductance at least
> `cN^-C` for universal constants `c,C` independent of `q,r`.

The directions of the two constraints oppose each other, so the attachment
that fixes one tight coordinate can cross the other boundary.  This is the
next simple profile region not implied by the scalar or upper-intersection
theorems.

## 6. Strongest self-attack / failure mode

The theorem certifies only one-label exits from two monotone profile regions.
It does not prove internal expansion of `F_N`, control an arbitrary subset of
one `(ell,b)` cell, or handle a union that excludes every canonical
attachment.  The deletion map is many-to-one and is not a Poincare
intertwining.  A mixed quadrant, thin diagonal band, surplus-length cut, or
non-tree word statistic may still have small conductance.  Thus the
`N^-7` anti-bottleneck bound cannot be promoted to a global spectral gap.

## 7. Calibration suite

- **Odd `m`:** `Omega(N,m)` is empty.  The theorem uses even `m=2N-2`.
- **`m=0` and `N=2`:** singleton regimes are outside `N>=4`.
- **`m=2,N>=3`:** excluded; no length-two simulation is invoked.
- **`S_3,m=4`:** there are 27 words and four pure-Hurwitz components.  Here
  `R_m={3,4}` and `H4` is a whole-word heat bath; the theorem starts at
  `N=4,m=6` and makes no claim about this boundary case.
- **`S_4,m=4`:** 120 words and 13 pure-Hurwitz components; whole-word `H4`
  remains in the exact kernel and is not represented by (1.2), which is used
  only at `m>=6`.
- **`S_4,m=6`:** `|Omega(4,6)|=3936`, `|F_4|=2880`, and
  `pi(F_4)=30/41`.  At `(q,r)=(2,2)`, the exact joint split is
  `2136+744`; the two global placements have masses `89/164` versus
  `75/164` and `133/164` versus `31/164`.  This explicitly checks why the
  smaller side cannot be guessed from conditional profile mass.
- **Exact `N<=8`:** all 61 deletion rows and 108 shape attachment families
  pass.  Finite success is only a falsification check.
- **Near-minimal doubled trees:** every state in `F_N`, including paths,
  stars, and the even `r=N/2` endpoint, is covered.  Adjacent squares are
  constructed in the source reservoir rather than assumed in arbitrary
  inputs.
- **Ordering and components:** each source and target is a literal ordered
  word.  The target after (2.10) omits one label but stays in global `Omega`;
  no graph-only chain or commuting-color simplification is used.
- **Parity:** parity enters only in proving exactly two strand nulls; edge or
  degree parity is not treated as an identity characterization.
- **Canonical hub / `L=2`:** neither is used.  Sources are distributed over
  every lower-dimensional base word and every insertion gap.
- **Mass orientation:** equation (2.13) is literal global mass accounting for
  both placements.

## 8. Artifacts and exact reproduction

Owned files:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M53-macro-closed-joint-profile-redteam/
  plan.md
  checkpoint.md
  report.md
  joint_profile_audit.py
  joint-profile-N4-N8.json
```

Exact deterministic command (`seed=null`; Python 3.12.3; no nonstandard
dependency):

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M53-macro-closed-joint-profile-redteam/joint_profile_audit.py --source-dir experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M53-macro-closed-joint-profile-redteam/joint-profile-N4-N8.json
```

The machine-readable output records the repository commit, exact argv,
Python version, seed, dependency list, 61 threshold rows, 108 attachment rows,
global masses, and the finite-scope warning.

SHA-256 at freeze time:

```text
61cdc58d2a689247bdd047b95ff978e55fbc940cf5a56468f8ecb6a0fea70bc1  joint_profile_audit.py
1f33385acd2f2ae48c83a02b9c2d3defa69966e150324ae249aeff97ea2cf5e8  joint-profile-N4-N8.json
```

No bytecode cache is part of the artifact.

## 9. Verdict

**PROVED.**

This verdict is scoped to the exact theorem (1.3): both macro-closed
orientations of every joint upper leaf-count/edge-balance threshold have
inverse-polynomial original-`K` conductance.  It does not resolve Terminal A
or Terminal B.
