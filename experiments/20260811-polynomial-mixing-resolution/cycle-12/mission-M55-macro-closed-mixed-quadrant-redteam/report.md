# M55 final report: the high-leaf/low-balance mixed quadrant has polynomial full-`K` escape

The first mixed joint-profile region left by M53 is also not a bottleneck.
Both placements of the nonminimal complement have original-chain two-sided
conductance at least `1/(24N^7)`.  A centroid insertion supplies one side;
a leaf-or-balance-witness insertion supplies the other.

## 1. Exact claim, quantifiers, and conventions

Permutations compose as `(pq)(x)=p(q(x))`, and words evaluate as
`t_1...t_m`.  For `N>=4`, set `m=2N-2`.  Let `F_N` be the connected
full-support minimal identity macro in `Omega(N,m)`, with prefix join tree
`T_J(w)`.  Write `ell(T)` for leaf count and

```text
b(T)=max_(e in E(T)) min{|C_e|,N-|C_e|}.
```

For

```text
2<=q<=N-1,      1<=r<=floor(N/2),
X=X_(N,q,r)={w in F_N:ell(T_J(w))>=q and b(T_J(w))<r},
Y=F_N minus X,
```

define

```text
B_X=F_N^c union X,        B_Y=F_N^c union Y.         (1.1)
```

The literal reviewed kernel is

```text
K=(1/2)I
 +(1/6) sum_(s in {3,4,5})
      (1/(m-s+1)) sum_(i=1)^(m-s+1) H_(i,s),        (1.2)
```

where each `H_(i,s)` is the uniform exact same-product heat bath.  For any
nontrivial cut in (1.1), with uniform stationary law `pi`, define

```text
Phi_pm(B)=Q_K(B,B^c)/min{pi(B),pi(B^c)}.
```

**Theorem.**  Both nontrivial cuts obey

```text
Phi_pm(B_X),Phi_pm(B_Y)
 >=1/[3Nm(N-1)^2(m-2)D_N]
 >=1/(24N^7),                                      (1.3)
D_N=(3N^2+N-12)/2.                                  (1.4)
```

No assertion is made for a trivial cut; for example `r=1` makes `X` empty.
The verdict is scoped to (1.3), not to Terminal A or B.

## 2. Full proof

### 2.1 Strand deletion and statistic changes

The M49 leaf-strand theorem, already accepted by a fresh referee, says that
deleting a leaf label `v` from every prefix permutation of `w in F_N`
creates exactly two identity increments.  Removing them yields a word in
`F_(N-1)` whose join tree is `T_J(w)-v`.  For fixed `v`, output word, and the
two null positions, at most `(N-1)^2` input lifts exist.  The insertion-
coordinate proof is as follows: there are `N-1` initial coordinates for `v`;
a projected support join is forced; descendants created by projected cuts
remain in distinct permutation cycles and minimality forbids their internal
reunion, so one initial coordinate has at most `N-1` descendants.  Hence the
fixed-label deletion fiber, after summing null positions, is at most

```text
Lambda_N=binom(m,2)(N-1)^2.                          (2.1)
```

For tree-leaf deletion,

```text
ell(T)-1<=ell(T-v)<=ell(T),
b(T)-1<=b(T-v)<=b(T).                                (2.2)
```

The leaf formula follows by checking whether its neighbor had degree two.
For balance, every surviving edge changes one side size by at most one and
the removed edge had balance one.

### 2.2 The two deletion inequalities

If `T` lies in `X`, then after deleting any tree leaf,

```text
ell(T-v)>=q-1,          b(T-v)<r.                    (2.3)
```

Define the base set

```text
X^base_(N-1)={w in F_(N-1):ell>=q-1,b<r}.            (2.4)
```

If `T` lies in `Y={ell<q or b>=r}`, deletion either preserves `ell<q` or
leaves `b>=r-1`.  Define

```text
Y^base_(N-1)={w in F_(N-1):ell<q or b>=r-1}.         (2.5)
```

Choose one leaf deterministically from each input.  Sum the `N` possible
deleted labels and use (2.1).  Relabeling makes the base counts independent
of which label was removed.  Thus

```text
|X|<=N Lambda_N |X^base_(N-1)|,
|Y|<=N Lambda_N |Y^base_(N-1)|.                     (2.6)
```

### 2.3 Centroid insertion restores `X`

Take a base tree in (2.4), fix the new label `v=N`, and choose a deterministic
centroid `u`.  A centroid of a tree on `N-1>=3` vertices is not a leaf, so
attaching `v` to `u` increases leaf count by one.

Orient every old edge away from `u`.  Its away-component lies in one centroid
branch and has size at most half the old tree.  After attaching `v` on the
`u` side, that component remains the smaller side of the old edge.  Hence
every old edge balance is unchanged, and the new edge has balance one.  The
new tree therefore satisfies `ell>=q,b<r`.

Insert `(v,u)^2` in any of the `m-1` gaps of the base word.  Its first copy is
the new prefix join and its second copy is a cut, so the join tree is the
claimed leaf attachment.  Since `v` occurs exactly in the marked square, the
source recovers the base and gap.  Consequently

```text
|S_X|=(m-1)|X^base_(N-1)|.                           (2.7)
```

### 2.4 Leaf-or-witness insertion restores `Y`

Take a base in (2.5).

1. If `ell<q`, attach `v` to a deterministic leaf.  The old leaf becomes
   degree two and `v` becomes a leaf, so `ell` is unchanged and remains low.
2. If `ell>=q,b>=r`, any deterministic attachment works because adding a
   leaf cannot lower the balance of an old edge.
3. The remaining case is `ell>=q,b=r-1`.  Choose a balance-witness edge and
   attach anywhere in a smaller side of size `r-1`.  Its split becomes
   `r,N-r`, which has balance at least `r` because `r<=floor(N/2)`.

At even `r=N/2`, the last base split is `r-1,r` and becomes exactly `r,r`.
At `r=1`, every tree already falls under item 2, so no balance-zero witness is
needed.  The same marked-square injectivity gives

```text
|S_Y|=(m-1)|Y^base_(N-1)|.                           (2.8)
```

Equations (2.6)--(2.8) imply, whenever the denominator is nonzero,

```text
|S_X|/|X|, |S_Y|/|Y|
 >=(m-1)/(N Lambda_N)
 =2/[Nm(N-1)^2].                                     (2.9)
```

### 2.5 Exact full-`K` boundary flow

Pad the marked square by a neighboring old-label transposition `a`, using
the right neighbor except at the final gap.  With a fixed old-label
transposition `f`, specify

```text
((vu),(vu),a)->(f,f,a),
(a,(vu),(vu))->(a,f,f).                              (2.10)
```

The ordered product remains `a`; the target omits `v` and belongs to
`F_N^c`.  The exact length-three fiber over a transposition has size

```text
D_N=binom(N,2)+6(N-2)+2binom(N-2,2)
   =(3N^2+N-12)/2.                                   (2.11)
```

The specified transition probability, including laziness, block-size
choice, all `m-2` windows, and the uniform fiber, is

```text
p_N=(1/2)(1/3)(1/(m-2))(1/D_N)
   =1/[6(m-2)D_N].                                   (2.12)
```

Let `Z_N=|Omega(N,m)|`.  The literal global masses are

```text
pi(B_X)=1-|Y|/Z_N,       pi(B_X^c)=|Y|/Z_N,
pi(B_Y)=1-|X|/Z_N,       pi(B_Y^c)=|X|/Z_N.          (2.13)
```

The sources `S_Y` lie in `B_X^c` and move into `B_X`; the sources `S_X` lie
in `B_Y^c` and move into `B_Y`.  Reversibility identifies this directed flow
with the oppositely oriented boundary flow.  Since the smaller global mass
is at most the displayed profile-side mass, (2.9)--(2.12) give the exact
first bound in (1.3).

All other `H3` outcomes and every `H4,H5` transition remain nonnegative
terms in the full boundary flow.  Only one explicit `H3` subflow is dropped
into the lower bound; nothing is omitted from an upper-bound argument.

Finally `m,m-2<=2N`, `(N-1)^2<=N^2`, and `D_N<=2N^2`, proving the coarse
`1/(24N^7)` bound.

## 3. Probability, runtime, path length, and congestion

- Exact specified edge probability: `1/[6(m-2)D_N]`.
- Exact certified source fraction: at least `2/[Nm(N-1)^2]`.
- Their product is the first bound in (1.3); no normalization is hidden.
- A direct prefix-permutation implementation constructs the join tree,
  centroid or witness, and source in `O(Nm)` elementary operations.  The
  used triple fiber has `D_N=O(N^2)` states.
- No multistep route or canonical hub is used; path length is one actual
  `K` edge and there is no congestion claim.
- The deterministic audit checked 61 thresholds and 102 attachment families
  through `N=8`; the observed command wall time was 3.5 seconds.

## 4. Dependency labels

1. **PROVED HERE:** both mixed deletion inequalities, centroid and
   complement insertions, endpoint handling, source injectivity, exact
   orientation, and conductance bound.
2. **PROVED / FRESH-REFEREED:** M49 strand deletion and the `(N-1)^2`
   fixed-position lift bound, restated in section 2.1.
3. **PROVED INHERITED:** reversibility and stationarity of exact same-product
   heat baths.
4. **PROVED BY DIRECT ENUMERATION:** the triple-fiber count (2.11).
5. **EXACT FINITE:** `N<=8` weighted shape/count checks; falsification only.
6. **CONDITIONAL:** none.
7. **EMPIRICAL:** none.

## 5. First unproved standalone proposition

> **OPPOSITE MIXED-QUADRANT FLOW.**  Uniformly for all feasible `N,q,r`, put
>
> ```text
> Z_(N,q,r)={w in F_N:ell(T_J(w))<q and b(T_J(w))>=r}.
> ```
>
> Each nontrivial cut `F_N^c union Z_(N,q,r)` and
> `F_N^c union (F_N minus Z_(N,q,r))` has two-sided original-`K`
> conductance at least `cN^-C` for universal `c,C`.

The tight source must raise balance while keeping leaf count low; a smaller
witness side always contains a tree leaf, suggesting but not yet proving the
needed simultaneous insertion with complete deletion accounting.

## 6. Strongest self-attack

This theorem still sees only the two-dimensional coarse pair `(ell,b)` and a
monotone quadrant.  A fixed joint-profile cell, a thin diagonal union, or an
internal subset chosen to avoid every centroid/witness attachment may have
very different flow.  The strand map is a counting map, not a Poincare
intertwining.  Hence these anti-bottleneck bounds do not imply expansion of
`F_N` or a global spectral gap.

## 7. Calibration suite

- Odd `m` gives empty `Omega`; `m=0` and `N=2` are singletons; excluded
  `m=2,N>=3` is not touched.
- `S_3,m=4` has 27 words/four Hurwitz components and `R_m={3,4}`;
  `S_4,m=4` has 120/13 and a whole-word `H4`.  The theorem starts at
  `N=4,m=6`, where all three block sizes in (1.2) are present.
- At `S_4,m=6`, `|Omega|=3936`, `|F_4|=2880`.  For `r=2` and either feasible
  `q`, `|X|=744`, `|Y|=2136`; the two macro-closed placements have global
  masses `75/164` versus `89/164` and `133/164` versus `31/164`.
- All 61 exact threshold rows and 102 attachment families through `N=8`
  pass; finite success is not the proof.
- Paths, stars, doubled-tree examples, and the even balance endpoint are
  included.  Adjacent squares are built in the counted reservoirs, not
  assumed in arbitrary inputs.
- Words retain their ordering.  The refresh target is a literal global
  identity word with one omitted label; no graph-only or color-commutation
  chain is substituted.
- No edge/degree parity invariant, length-two simulation, or fixed canonical
  hub is used.
- Equation (2.13) gives exact smaller-side orientation without assuming a
  value for `pi(F_N)`.

## 8. Artifacts and reproduction

```text
experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M55-macro-closed-mixed-quadrant-redteam/
  plan.md
  checkpoint.md
  report.md
  mixed_quadrant_audit.py
  mixed-quadrant-N4-N8.json
```

Exact deterministic command (`seed=null`, Python 3.12.3, no nonstandard
dependency):

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M55-macro-closed-mixed-quadrant-redteam/mixed_quadrant_audit.py --source-dir experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M55-macro-closed-mixed-quadrant-redteam/mixed-quadrant-N4-N8.json
```

The JSON records commit, argv, Python, seed, dependency metadata, named
claims, every threshold row, every attachment row, and a finite-scope warning.

```text
d0992a83be7b155c4fb72cd1777a48d529232af101b35c8ba6abc9f79d564261  mixed_quadrant_audit.py
cfb2220d76ee6d873ed45603b644356dabf5ac2a5abcfd50b0a1a13dc9b3d306  mixed-quadrant-N4-N8.json
```

The accidentally numbered M54 planning file is preserved separately with an
append-only supersession notice; no M46/M54 referee artifact was touched.
No bytecode cache is part of M55.

## 9. Verdict

**PROVED.**

This scoped verdict proves (1.3) for both placements of every high-leaf,
low-balance mixed quadrant.  It does not establish Terminal A or Terminal B.
