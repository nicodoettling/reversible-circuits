# M57 final report: the low-leaf/high-balance quadrant has polynomial full-`K` escape

The fourth axis-aligned joint leaf/balance quadrant is not a bottleneck.
Both placements of `F_N^c` have literal original-chain two-sided conductance
at least `1/(24N^7)`.  The tight move attaches a new leaf to an old tree leaf
inside a smaller balance-witness side, raising balance without changing leaf
count.

## 1. Exact claim, quantifiers, and conventions

Permutations compose by `(pq)(x)=p(q(x))`; a word evaluates as
`t_1...t_m`.  For `N>=4`, let `m=2N-2`, and let `F_N` be the minimal
connected full-support identity macro.  Its prefix cycle joins form a labeled
tree `T_J(w)`.  For

```text
2<=q<=N-1,       1<=r<=floor(N/2),
Z=Z_(N,q,r)={w in F_N:ell(T_J(w))<q and b(T_J(w))>=r},
W=F_N minus Z,
```

where `ell` is leaf count and
`b(T)=max_e min{|C_e|,N-|C_e|}`, define

```text
B_Z=F_N^c union Z,         B_W=F_N^c union W.        (1.1)
```

The reviewed chain is exactly

```text
K=(1/2)I
 +(1/6) sum_(s in {3,4,5})
      (1/(m-s+1)) sum_(i=1)^(m-s+1) H_(i,s),        (1.2)
```

with uniform exact same-product heat baths.  For uniform `pi` on
`Omega(N,m)`, let

```text
Phi_pm(B)=Q_K(B,B^c)/min{pi(B),pi(B^c)}.
```

**Theorem.**  Whenever the corresponding cut is nontrivial,

```text
Phi_pm(B_Z),Phi_pm(B_W)
 >=1/[3Nm(N-1)^2(m-2)D_N]
 >=1/(24N^7),                                      (1.3)
D_N=(3N^2+N-12)/2.                                  (1.4)
```

The verdict **PROVED** is scoped to (1.3); it is not Terminal A or B.

## 2. Full proof

### 2.1 Strand deletion and the two count maps

The fresh-refereed M49 strand lemma says that deleting a join-tree leaf label
from every prefix permutation creates exactly two null increments; after
removing them, the output lies in `F_(N-1)` and has join tree `T-v`.  For a
fixed deleted label, output word, and two null positions, the insertion-
coordinate argument gives at most `(N-1)^2` lifts.  Hence the fixed-label
fiber after summing positions is at most

```text
Lambda_N=binom(m,2)(N-1)^2.                          (2.1)
```

For any tree leaf `v`,

```text
ell(T)-1<=ell(T-v)<=ell(T),
b(T)-1<=b(T-v)<=b(T).                                (2.2)
```

The first statement checks whether the old neighbor had degree two.  The
second follows because each surviving split changes one side size by at most
one and the removed leaf edge had balance one.

Deleting one deterministic leaf from a tree in `Z` lands in

```text
Z^base={w in F_(N-1):ell<q,b>=r-1}.                  (2.3)
```

Deleting from `W={ell>=q or b<r}` lands in

```text
W^base={w in F_(N-1):ell>=q-1 or b<r}.               (2.4)
```

Sum the `N` possible deleted labels and use relabeling symmetry and (2.1):

```text
|Z|<=N Lambda_N |Z^base|,
|W|<=N Lambda_N |W^base|.                            (2.5)
```

### 2.2 A witness side always contains a global leaf

Let an edge `e` separate a tree into a side `S` and its complement, and let
`x in S` be the bridge endpoint.  If `|S|=1`, `x` is a global tree leaf.  If
`|S|>=2`, choose a vertex `z` farthest from `x` in the induced tree on `S`.
Then `z!=x`, so it is not incident to the bridge; it has exactly one neighbor
on the path back to `x` and no neighbor farther away.  Thus `z` is a global
tree leaf.  This proves that every side of every tree edge contains a global
leaf.

### 2.3 Reverse insertion into `Z`

Fix the new label `v=N` and take a base tree in (2.3).

- If `b>=r`, attach `v` to any deterministic old leaf.  Total leaf count is
  unchanged and adding a leaf never lowers an old edge balance.
- If `b=r-1`, choose a balance-witness edge, orient a smaller side of size
  `r-1`, and choose the deterministic global leaf in that side supplied by
  section 2.2.  Attaching `v` to it keeps total leaf count unchanged.  The
  witness split becomes `r,N-r`, whose balance is at least `r` because
  `r<=floor(N/2)`.

The `r=1` case always falls under the first bullet.  For `r=2`, a singleton
smaller side supplies its leaf endpoint.  At even `r=N/2`, the old split
`r-1,r` becomes `r,r`.  Thus all endpoints survive.

Insert `(v,u)^2` in any of the `m-1` gaps of the base word.  Its first copy
is a prefix join, its second a cut, and the new join tree is the claimed leaf
attachment.  Because `v` occurs exactly in that adjacent square, base, gap,
and attachment are recovered.  Therefore

```text
|S_Z|=(m-1)|Z^base|.                                 (2.6)
```

### 2.4 Reverse insertion into `W`

For a base in (2.4):

- if `b<r`, attach `v` at a deterministic centroid; every old edge balance
  is unchanged and the new edge has balance one, so the result remains in
  `W`;
- otherwise `b>=r` and necessarily `ell>=q-1`; attach at a deterministic
  nonleaf, which raises leaf count by one and puts the result in `W`.

A tree on `N-1>=3` vertices has a nonleaf, and a centroid is a nonleaf.  The
same marked-square recovery gives

```text
|S_W|=(m-1)|W^base|.                                 (2.7)
```

Combining (2.5)--(2.7), for either nonempty profile side,

```text
|S_Z|/|Z|, |S_W|/|W|
 >=(m-1)/(N Lambda_N)
 =2/[Nm(N-1)^2].                                     (2.8)
```

### 2.5 Exact `H3` action and global orientation

Pad the marked square by a neighboring old-label transposition `a`; use the
right neighbor unless the square occupies the final gap.  For a fixed
old-label transposition `f`, specify

```text
((vu),(vu),a)->(f,f,a),
(a,(vu),(vu))->(a,f,f).                              (2.9)
```

The ordered product remains `a`, while the target omits `v` and lies in
`F_N^c`.  The exact triple fiber over a transposition has size

```text
D_N=binom(N,2)+6(N-2)+2binom(N-2,2)
   =(3N^2+N-12)/2.                                   (2.10)
```

Thus the specified outcome has exact probability

```text
p_N=(1/2)(1/3)(1/(m-2))(1/D_N)
   =1/[6(m-2)D_N].                                   (2.11)
```

Let `O_N=|Omega(N,m)|`.  Literal masses are

```text
pi(B_Z)=1-|W|/O_N,       pi(B_Z^c)=|W|/O_N,
pi(B_W)=1-|Z|/O_N,       pi(B_W^c)=|Z|/O_N.          (2.12)
```

Sources `S_W` cross from `B_Z^c` into `F_N^c subset B_Z`, while `S_Z` cross
from `B_W^c` into `B_W`.  Reversibility permits either boundary orientation.
The minimum global mass is at most the displayed profile-side mass, so
(2.8)--(2.11) prove the exact bound in (1.3).

All other `H3` outcomes and all `H4,H5` transitions are retained as
nonnegative full boundary flow.  Finally use `m,m-2<=2N`,
`(N-1)^2<=N^2`, and `D_N<=2N^2` to obtain `1/(24N^7)`.

## 3. Probability, runtime, path, and congestion accounting

- Exact edge probability: `1/[6(m-2)D_N]`.
- Certified source fraction: `2/[Nm(N-1)^2]`.
- Their product is the first bound in (1.3), with every kernel normalization
  explicit.
- Direct prefix/join-tree and witness construction costs `O(Nm)` elementary
  operations; the used conditional fiber has `O(N^2)` states.
- Each certificate is one actual `K` edge.  No canonical path, hub, or
  congestion bound is invoked.
- The exact bounded audit checked 61 threshold rows and 108 attachment
  families through `N=8`; observed wall time was 3.6 seconds.

## 4. Dependency statuses

1. **PROVED HERE:** side-leaf lemma, both reverse insertions, deletion count
   inequalities, endpoint cases, exact global orientation, and (1.3).
2. **PROVED / FRESH-REFEREED:** M49 strand deletion and fixed-position lift
   multiplicity, restated in section 2.1.
3. **PROVED INHERITED:** exact heat-bath reversibility/stationarity.
4. **PROVED BY DIRECT ENUMERATION:** triple-fiber formula (2.10).
5. **EXACT FINITE:** `N<=8` shape/count falsification; not the proof.
6. **CONDITIONAL:** none.
7. **EMPIRICAL:** none.

## 5. First unproved standalone proposition

> **MACRO-CLOSED PROFILE-RECTANGLE FLOW.**  Uniformly in all feasible integer
> endpoints, let
>
> ```text
> R={w in F_N:q_1<=ell(T_J(w))<q_2,
>                 r_1<=b(T_J(w))<r_2}.
> ```
>
> Every nontrivial cut `F_N^c union R` and
> `F_N^c union (F_N minus R)` has two-sided original-`K` conductance at least
> `cN^-C` for universal `c,C` independent of all four endpoints.

The four quadrant theorems do not automatically control an intersection of
both an upper and a lower boundary in each coordinate.

## 6. Strongest self-attack

The result remains a coarse profile anti-bottleneck.  It neither controls a
bounded rectangle or fixed `(ell,b)` cell nor gives internal expansion of
`F_N`.  A thin band can exclude every insertion used here.  Strand deletion
is many-to-one and not a variance comparison, so accumulating these scalar
cut theorems does not establish a spectral gap.

## 7. Calibration suite

- Odd `m` is empty; `m=0`/`N=2` are singletons; excluded `m=2` is unused.
- `S_3,m=4` has 27 words/four Hurwitz components; `S_4,m=4` has 120/13 and
  whole-word `H4`.  The theorem starts at `N=4,m=6`, where all three block
  sizes occur.
- At `S_4,m=6`, `|Omega|=3936`, `|F_4|=2880`.  For `(q,r)=(3,2)`,
  `|Z|=2136`, `|W|=744`; the two global placements have masses `133/164`
  versus `31/164` and `75/164` versus `89/164`.
- All 61 thresholds and 108 attachment families through `N=8` pass, as
  bounded falsification only.
- Singleton witness sides, paths, stars, doubled-tree words, and even
  `r=N/2` are covered.  Squares are constructed in the reservoir rather than
  assumed in arbitrary inputs.
- Literal ordered words and global identity targets are retained.  No
  graph-only chain, parity characterization, `L=2` simulation, or fixed hub
  is used.
- Equation (2.12) handles exact smaller-side orientation.

## 8. Artifacts and reproduction

```text
experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M57-macro-closed-opposite-quadrant-redteam/
  plan.md
  checkpoint.md
  report.md
  opposite_quadrant_audit.py
  opposite-quadrant-N4-N8.json
```

Exact deterministic command (`seed=null`, Python 3.12.3, no nonstandard
dependency):

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M57-macro-closed-opposite-quadrant-redteam/opposite_quadrant_audit.py --source-dir experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam --output experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M57-macro-closed-opposite-quadrant-redteam/opposite-quadrant-N4-N8.json
```

The JSON records commit, argv, Python, seed, named claims, every exact row,
and the finite-scope warning.

```text
e0d6f01b94cf6fa1966fdda35860d1ee663eaefe6db2072d7514c1deb33fd642  opposite_quadrant_audit.py
be80b944012177eaec9f404b2d8e69b6545d44d807a86a8460a66f4c0a39c008  opposite-quadrant-N4-N8.json
```

The accidentally numbered M56 plan is preserved with an append-only
supersession notice.  No M48 artifact was touched, and no bytecode cache is
part of M57.

## 9. Verdict

**PROVED.**

This verdict is scoped to both macro-closed placements of the low-leaf,
high-balance quadrant.  It is nonterminal.
