# M34 final report: every median-shell state acts; its weighted mass is open

This mission does not produce TERMINAL B and does not prove the requested
uniform area-median conductance theorem.  It closes the **action** half
universally and sharply: every nonmaximum minimal connected word has an
area-increasing right Hurwitz move, realized by one original `H_3` update.
Consequently the exact conductance question is reduced to one weighted Dyck
area-layer ratio.  The final verdict is therefore
`OPEN AT A NAMED STEP`, not a global resolution.

## 1. Exact claim, quantifiers, kernel, and convention

Permutations are maps on `[N]`; `pq` means `p` after `q`, so
`(pq)(x)=p(q(x))`.  Words evaluate as `t_1...t_m`.  Put

```text
M=binom(N,2),
Omega(N,m)={w in T_N^m:t_1...t_m=id},
R_m={r in {3,4,5}:r<=m},
K=(1/2)I
  +(1/(2|R_m|)) sum_(r in R_m) 1/(m-r+1) sum_i H_(i,r),
```

where `H_(i,r)` is uniform on the exact same-product length-`r` fiber.  The
stationary law `pi` is uniform on the global `Omega(N,m)`.

For the theorem let `N>=6`, `n=N-1`, `m=2n`, so `|R_m|=3`, and let

```text
F_N={w in Omega(N,m):the factor-support graph is connected on [N]},
mu=Uniform(F_N),
h_j=N-cycles(t_1...t_j),
Area(w)=sum_(j=1)^m h_j.
```

The height path is a Dyck path with `n` joins and `n` cuts.  Its maximum area
is `n^2`.

### Theorem 1 (universal valley action)

For every `w in F_N` with `Area(w)<n^2`, there is an index `i` for which
`(t_i,t_(i+1))=(a,b)` is a `DU` valley and

```text
(a,b) -> (b,bab)                                      (1.1)
```

preserves the ordered product and membership in `F_N`, while increasing area
by exactly `2`.

The pair (1.1) can be padded inside one legal `H_3` window.  If `g` is that
window product and `F_3(g)` its exact length-three transposition-fiber size,
the specified transition has exact full-`K` probability

```text
p(w)=1/[6(m-2)F_3(g)] >=1/[6(m-2)M^3].                (1.2)
```

### Theorem 2 (exact threshold-flow reduction)

For every feasible area value `q<n^2`, define the global cut and exact top
layer

```text
A_q={w in F_N:Area(w)<=q},
L_q={w in F_N:Area(w)=q}.
```

Then

```text
Q_K(A_q,A_q^c)
 >=pi(F_N) mu(L_q)/[6(m-2)M^3].                       (1.3)
```

If `mu(A_q)<=1/2`, then `pi(A_q)=pi(F_N)mu(A_q)<=1/2`, so `A_q` is the
exact global smaller side and its two-sided conductance satisfies

```text
Phi_pm^K(A_q)
 >=[mu(L_q)/mu(A_q)]/[6(m-2)M^3].                    (1.4)
```

Every `r=4,5` contribution is retained in `K` and is merely discarded as a
nonnegative term in this lower bound.

### Corollary 3 (weighted Dyck cover monotonicity)

For a fixed Dyck sign path `P`, let `W_N(P)` be the number of words in `F_N`
with that path.  If `P'` is obtained by replacing one valley `DU` by a peak
`UD`, then

```text
W_N(P)<=W_N(P').                                      (1.5)
```

In particular the mountain has the largest fixed-path fiber.  Its exact
count and conditional mass are

```text
W_N(U^n D^n)=(N-1)! N^(2N-4),
mu(U^n D^n)=(N-1)! N^(N-1)/(2N-2)!.                  (1.6)
```

Equation (1.6) also confirms that the mountain is not a constant-mass
canonical hub asymptotically.

## 2. Full argument

### 2.1 The join factors form a spanning tree

Call a factor a join or a cut according as right multiplication raises or
lowers `N-cycles(.)`.  The height starts and ends at zero and has `2N-2`
steps, hence there are exactly `N-1` joins.

At every prefix, each cycle of the prefix permutation is contained in one
connected component of the graph formed by the join factors seen so far.
This follows inductively.  A join merges two cycles and its edge connects the
join-graph components containing them; a cut only splits one cycle, so both
new cycles remain inside the component that contained the old one.

Every cut-factor edge has both endpoints in one prefix cycle and therefore
inside one previous join-graph component.  Thus adding all cut edges cannot
connect two final join-graph components.  Since the full factor-support graph
of `w in F_N` is connected, the final join graph is connected too.  It has
`N` vertices and exactly `N-1` edges, so it is a tree.  Consequently every
join factor connects two distinct components of the previous join forest.

This proves, rather than assumes, the join-tree fact used below.

### 2.2 Every valley is an upper diamond

Let `(a,b)` be an adjacent valley and let `x` be the prefix permutation before
`a`.  Thus

```text
rank(x)=h, rank(xa)=h-1, rank(xab)=h,
```

where `rank=N-cycles(.)`.  Put `z=xa`.  The cut `a` splits one cycle of `x`
into cycles `A,B` of `z`.  The join `b` joins cycles `C,D` of `z`.

The unordered pairs cannot be equal.  If `{C,D}={A,B}`, the endpoints of the
join factor `b` lie in the single cycle of `x` obtained by merging `A,B`.
By the prefix invariant, they already lie in one previous join-forest
component.  Adding `b` would create a cycle in the final join graph,
contradicting Section 2.1.

If `{A,B}` and `{C,D}` are disjoint, the transpositions `a,b` are disjoint
and commute.  Starting from `x=za`, the factor `b` still joins `C,D`.  If the
pairs share exactly one `z`-cycle, `a` first merges `A,B`, while `b` then
joins that merged cycle to the third cycle; again `b` is a join when applied
directly to `x`.  In both cases

```text
b(bab)=ab
```

and the new intermediate prefix `xb` has rank `h+1`.  Thus (1.1) replaces
the valley height `h-1` by the peak height `h+1`, changing no other prefix
height and raising area exactly `2`.

The Hurwitz Nielsen transformation preserves the generated subgroup:
`<a,b>=<b,bab>`, with every other factor fixed.  Hence it preserves
transitivity and stays in `F_N`.

A Dyck path with no adjacent `DU` has all `U` steps before all `D` steps and
is the mountain.  This completes Theorem 1.

### 2.3 Padding and exact original-kernel normalization

If the valley pair is not final, use the `H_3` window `(a,b,c)` and specify

```text
(a,b,c)->(b,bab,c).
```

For the final pair use `(c,a,b)->(c,b,bab)`.  The ordered length-three block
product is unchanged in either case.  Every adjacent pair is covered, with
no random choice of the valley or padding position: both are selected
deterministically for the witness transition.

The active half of `K` chooses `r=3` with probability `1/3`, chooses the
specified window with probability `1/(m-2)`, and chooses the target uniformly
from its exact fiber with probability `1/F_3(g)`.  Including laziness gives
the equality in (1.2); `F_3(g)<=M^3` gives the uniform bound.  No claim that
arbitrary length-two heat baths can be simulated is used.

Summing (1.2) over all `w in L_q` proves (1.3).  Since the stationary law is
uniform and `A_q subset F_N`,

```text
pi(A_q)=pi(F_N)mu(A_q).
```

When `mu(A_q)<=1/2`, this is at most `1/2` even in the global state space.
Dividing (1.3) by that exact smaller-side mass proves (1.4).  Reversibility
also makes the stationary boundary flow two-sided, although only the outward
orientation is needed.

### 2.4 Fixed-path injection and the mountain count

At a specified valley position, (1.1) is an injective map from the path fiber
`F_N(P)` into `F_N(P')`; its inverse is the inverse Hurwitz move on the image.
This proves (1.5).

For the mountain, the first `N-1` factors are a minimum transposition
factorization of an `N`-cycle `sigma`, and the last `N-1` factors minimally
factor `sigma^(-1)`.  There are `(N-1)!` choices of `sigma` and, by Dénes'
tree count, `N^(N-2)` minimum transposition factorizations of each fixed
`N`-cycle.  This gives the first formula in (1.6).  Division by the Hurwitz
count

```text
|F_N|=(2N-2)!N^(N-3)
```

gives the second.

## 3. Probability, runtime, path length, and congestion

- The certified crossing from every exact top-layer state is one original
  `K` step, of exact probability `1/[6(m-2)F_3(g)]` and worst-case probability
  at least `1/[6(m-2)M^3]`.
- The flow lower bound is (1.3), and the exact smaller-side conductance is
  (1.4).  It accounts for laziness, block-size choice, window choice, and the
  conditional-fiber outcome.  `Q_4+Q_5` are present and nonnegative.
- No multistep comparison path, canonical hub, or congestion estimate is
  used.  The path length is exactly one and congestion is inapplicable.
- A valley and its conjugated transposition can be found and evaluated in
  polynomial time, for example `O(Nm)` with direct permutation arithmetic.
- The complete `F_5` run visited exactly `1,008,000` states and took `49.9`
  seconds after adding all path and adjacent-pair statistics.  The `F_4` run
  took below `0.1` seconds.  The fixed-seed `F_6` search checked `100001`
  exact states in `17.3` seconds.  These runtimes are computational metadata,
  not asymptotic mixing evidence.

## 4. Dependencies, each labeled

1. **PROVED HERE:** the join-factor spanning-tree lemma, universal valley
   action, exact `H_3` padding and normalization, threshold stationary flow,
   global smaller-side orientation conditional on `mu(A_q)<=1/2`, fixed-path
   monotonicity, and the mountain count.
2. **INHERITED PROVED:** exact heat-bath reversibility and uniform
   stationarity; odd-length emptiness; qualitative irreducibility of the full
   `{3,4,5}` chain.  Irreducibility is not used to derive (1.3).
3. **CITED / CONVENTION-CHECKED:** Dénes' bijection/count of minimum
   transposition factorizations of a fixed `N`-cycle, used only in (1.6), and
   Hurwitz's count `|F_N|=(2N-2)!N^(N-3)`.
4. **CITED RESOURCE, NOT USED AS A THEOREM:** Luca Ferrari, *Unimodality and
   Dyck paths*, JCMCC 87 (2013), pp. 65--79, records rank-unimodality of the
   Dyck lattice as unresolved and provides only partial chain decompositions.
   Therefore unweighted Dyck-rank unimodality is not silently assumed.
5. **EXACT FINITE:** the complete `F_3,F_4,F_5` orbit closures, exact dynamic
   programming over all same-product local fibers, and the abstract
   `S_N,N<=6` upper-diamond falsifier.  These falsify named claims or calibrate
   the proof; they are not finite-to-universal inferences.
6. **EMPIRICAL:** only nonfinding in the fixed-seed `F_6` search.  It enters no
   theorem.

## 5. First unproved standalone proposition

> **WEIGHTED DYCK MEDIAN-SHELL MASS.**  Let `mu` be uniform on `F_N`.  For
> every `N>=6`, exhibit a feasible integer `q_N` such that
>
> ```text
> 1/4<=mu(Area<=q_N)<=1/2,
> ```
>
> and prove universal constants `c>0,C<infinity` with
>
> ```text
> mu(Area=q_N)/mu(Area<=q_N) >=cN^(-C).                (5.1)
> ```

By (1.4), (5.1) immediately gives the requested original-`K` area-cut bound

```text
Phi_pm^K(A_(q_N)) >= cN^(-C)/[6(m-2)M^3].
```

The explicit natural choice is the first conditional quartile
`q_N=min{q:mu(Area<=q)>=1/4}`; one must still prove that its discrete jump
does not exceed `1/2`.  Equation (1.5) says that fixed-path weights increase
along the dominance Dyck lattice, but it does not compare a union of all
lower ranks with one boundary rank.  Even the corresponding unweighted
rank-unimodality problem is a known open combinatorial problem, so invoking it
would not be a proof.

## 6. Strongest self-attack / failure mode

The theorem proves action, not shell mass.  A bounded-range potential on a
bounded-degree graph can have a median lower tail whose top layer is
superpolynomially small even when every nonmaximum state has an increasing
edge; many ascent paths can coalesce.  Thus (1.1) cannot by itself rule out a
weighted-Dyck bottleneck.

Nor does a hypothetical failure of (5.1) prove TERMINAL B.  Other states in
the width-12 shell can cross through `H_4,H_5`, and some states can leave
`F_N`; a bottleneck upper bound would have to count all those flows.  Theorem
1 only supplies a lower bound.  Finally, this is one family of thresholds in
one macro-fiber and gives no arbitrary-function spectral gap.

The fixed-path monotonicity is also insufficient: injections from many lower
Dyck paths can overlap in a much smaller upper fiber.  Routing all words to
the mountain would recreate a canonical-hub comparison, and (1.6) shows its
stationary mass is exponentially small.

## 7. Calibration suite

- **Odd `m`:** `Omega(N,m)` is empty by sign.  The theorem uses even
  `m=2N-2`.
- **`m=0` and `N=2`:** singleton cases are outside `N>=6`.
- **`m=2,N>=3`:** the excluded disconnected-chain regime is not used.
- **`S_3,m=4`:** there are 27 global identity words and four pure-Hurwitz
  components.  The connected minimal orbit has 24 states, with exact area
  counts `{2:6,4:18}`; adjacent-pair gain is `2` exactly off the mountain.
  Here `H_4` is a whole-word heat bath and remains in the exact harness.
- **`S_4,m=4`:** there are 120 identity words and 13 pure-Hurwitz components;
  this is not the minimal full-support length for `N=4`.  Its whole-word
  `H_4` normalization is not extrapolated to the theorem.
- **`S_4,m=6`:** there are 3936 global words and 17 pure-Hurwitz components.
  The exact connected minimal orbit has 2880 states and area counts
  `{3:96,5:528,7:720,9:1536}`; all 1344 nonmountain states have adjacent-pair
  gain `2`.
- **`S_5,m=8`:** complete enumeration gives area counts
  `{4:3000,6:23400,8:60600,10:132840,12:207600,14:205560,16:375000}`.
  The admissible threshold `q=12` has lower-tail count
  `427440/1008000`; every nonmountain state has pair gain `2`.
- **Near-minimal doubled trees:** all of `F_N`, including paired-tree words,
  is covered.  No route passes through a fixed doubled-tree or mountain hub.
- **Ordered interleavings:** the argument acts on the actual ordered word and
  its prefix permutations; it never collapses to an unordered graph.
- **Parity:** no edge- or vertex-degree parity characterization of identity is
  used.  Product preservation is the exact identity `b(bab)=ab`.
- **Failed `L=2` simulation:** (1.1) is padded inside an actual `H_3` window;
  no arbitrary two-factor heat bath is simulated.
- **Mass orientation:** (1.4) uses the exact identity
  `pi(A_q)=pi(F_N)mu(A_q)` and the stipulated conditional upper bound `1/2`.
  Existence of the requested quartile threshold remains explicitly open.

## 8. Artifacts and reproduction commands

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-08/mission-M34-area-median-shell/
```

Files are `plan.md`, `checkpoint.md`, this `report.md`,
`valley_upper_diamond_falsifier.py`, `exact_local_area_ascent.py`, and
`random_local_ascent_search.py`.  Machine-readable outputs are
`valley_upper_diamond_N6.json`, `local_ascent_N3.json`,
`local_ascent_N4.json`, `local_ascent_N5.json`, and
`local_ascent_search_N6_seed340031.json`.

Exact commands:

```bash
python3 experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M34-area-median-shell/valley_upper_diamond_falsifier.py --max-N 6 --output experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M34-area-median-shell/valley_upper_diamond_N6.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M34-area-median-shell/exact_local_area_ascent.py --N 3 --output experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M34-area-median-shell/local_ascent_N3.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M34-area-median-shell/exact_local_area_ascent.py --N 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M34-area-median-shell/local_ascent_N4.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M34-area-median-shell/exact_local_area_ascent.py --N 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M34-area-median-shell/local_ascent_N5.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M34-area-median-shell/random_local_ascent_search.py --N 6 --steps 500000 --stride 5 --seed 340031 --output experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M34-area-median-shell/local_ascent_search_N6_seed340031.json
```

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
Python: `3.12.3`.  The exact runs have seed `null`; the witness search records
seed `340031`.  No nonstandard package is used.

## 9. Verdict

OPEN AT A NAMED STEP: WEIGHTED DYCK MEDIAN-SHELL MASS (5.1), INCLUDING
EXISTENCE OF AN EXPLICIT FEASIBLE QUARTILE THRESHOLD WITH CONDITIONAL MASS AT
MOST ONE HALF.

The universal action and exact full-`K` flow reduction are proved, but neither
TERMINAL A nor TERMINAL B follows without the named layer-mass theorem (or a
different cut with complete stationary mass and boundary accounting).
