# M47 final report: rooted largest-branch thresholds have polynomial full-K escape

Date: 2026-08-11.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

This report proves an inverse-polynomial two-sided conductance bound for every
threshold of a genuinely global pendant-branch statistic in the minimal
full-support macro.  It does **not** prove a global spectral gap and does not
refute polynomial mixing.  The scoped verdict is `PROVED`.

## 1. Exact claim, quantifiers, and convention

Permutations are maps on `[N]`; `(pq)(x)=p(q(x))`, and a word evaluates as
`t_1...t_m`.  Put

```text
Omega(N,m)={w in T_N^m:t_1...t_m=id},
R_m={r in {3,4,5}:r<=m},
K=(1/2)I+(1/(2|R_m|)) sum_(r in R_m)
       (1/(m-r+1)) sum_i H_(i,r),
```

where `H_(i,r)` is uniform on the exact same-product length-`r` fiber.  The
stationary target `pi` is uniform on the **global** `Omega(N,m)`.

For `N>=4`, put `m=2N-2`, so `|R_m|=3`, and let

```text
F_N={w in Omega(N,m):support(w)=[N] and is connected}.
```

The join factors of `w in F_N` form its prefix join tree `T_J(w)`.  Fix the
distinguished label `1` and define the rooted largest-pendant-branch statistic

```text
L_1(T)=max{|C|: C is a component of T-{1}}.
```

For every integer `1<=q<=N-1`, define the global cut

```text
A_(N,q)={w in F_N:L_1(T_J(w))>=q}.                    (1.1)
```

States outside `F_N` belong to the complement.  Let

```text
D_N=(3N^2+N-12)/2.                                    (1.2)
```

### Theorem A: all rooted largest-branch thresholds are anti-bottlenecks

For every `N>=4` and every `1<=q<=N-1`, both sides of (1.1) are nonempty and
the exact full lazy chain satisfies

```text
Phi_pm^K(A_(N,q))
 :=Q_K(A_(N,q),A_(N,q)^c)
      /min{pi(A_(N,q)),pi(A_(N,q)^c)}
 >=(1-1/N)^(N-4)/[12N(m-2)D_N]
 >=1/(192N^4).                                        (1.3)
```

The bound is uniform in the threshold `q`.  It uses a positive `H3` boundary
subflow; every `H4` and `H5` contribution remains in the exact kernel and is
nonnegative.  No conditional-mass orientation is assumed.

### Theorem B: exact fixed-join-tree stationary weights

For any fixed labeled spanning tree `T` on `[N]`, let `W_N(T)` be the number
of words in `F_N` whose prefix join tree is exactly `T`.  For
`S subseteq E(T)`, let

```text
C_S=sum_{a<b: a,b lie in one component of ([N],S)} (ab)
```

in the real group algebra of `S_N`.  Define group-algebra elements
`P_(j,S)` by

```text
P_(0,empty)=id,  P_(0,S)=0 for S!=empty,
P_(j+1,S)=P_(j,S) C_S + sum_(e in S) P_(j,S-{e}) e.   (1.4)
```

All products in (1.4) append a factor on the right.  Then the literal
coefficient formula is

```text
W_N(T)=[id] P_(2N-2,E(T)).                            (1.5)
```

Consequently the exact stationary mass of (1.1) is

```text
pi(A_(N,q))
 = [sum_T 1{L_1(T)>=q} W_N(T)] / |Omega(N,2N-2)|,     (1.6)

|Omega(N,m)|
 =(1/N!) sum_(lambda partition N)(f^lambda)^2 c_lambda^m.
```

Thus (1.3) does not replace the actual join-tree law by a uniform Cayley law.
The recurrence also explains exactly what remains to be estimated for
label-symmetric centroid and diameter cuts.

### Theorem C: branch statistics have macroscopic one-step jumps

If two `F_N` words differ by one same-product `r`-window, their join trees
have a common outside forest with at most `r+1` components, completed by the
same number `k<=r` of old and new edges.  Nevertheless one `H4` update can
change join-tree diameter by `Theta(N)`.  Therefore diameter, centroid, and
largest-branch cuts do not have the inherited width-12 area-shell property.

## 2. Full arguments and constructions

### 2.1 The join tree and the marked-root boundary reservoir

In a minimal connected identity word there are exactly `N-1` joins and
`N-1` cuts.  Every join connects two components of the prefix support forest;
the join edges are therefore distinct, acyclic, and spanning.  This is
`T_J(w)`.

Call `w` **root-marked** if it contains an adjacent square

```text
(1u),(1u)
```

and label `1` occurs in no other factor.  Deleting the square leaves an
arbitrary word of `F_(N-1)` on `[N]\{1}`.  Conversely, from such a smaller
word:

1. choose its attachment label `u` in `N-1` ways;
2. choose one of the `2N-3` gaps of its length-`2N-4` factor list; and
3. insert `(1u),(1u)` in that gap.

These operations are inverse.  The first copy of `(1u)` is a join and the
second a cut, so the root has degree one in `T_J(w)` and
`L_1(T_J(w))=N-1`.  Hence the root-marked set `B_N` is contained in **every**
threshold (1.1), and

```text
|B_N|=(N-1)(2N-3) C_0(N-1),
C_0(v)=(2v-2)!v^(v-3).
```

Dividing by `|F_N|=C_0(N)` gives the exact conditional mass

```text
mu_N(B_N):=|B_N|/|F_N|
 =[(N-1)(2N-3)(2N-4)!(N-1)^(N-4)]
    /[(2N-2)!N^(N-3)]
 =(1/(2N))(1-1/N)^(N-4).                              (2.1)
```

There is no overlap factor: the distinguished root occurs in exactly one
square, so the deletion and insertion data are unique.

### 2.2 Exact one-step full-K exit

Fix `w in B_N` and choose deterministically any transposition `f` on the base
labels `[N]\{1}`.  If the marked square is not the last pair, use the `H3`
window starting at it and specify

```text
((1u),(1u),a) -> (f,f,a).                             (2.2)
```

If it is the last pair, use the window ending at `m` and specify

```text
(a,(1u),(1u)) -> (a,f,f).                             (2.3)
```

Both old and new block products equal the padding transposition `a`.  The
outcome contains no factor incident to label `1`, so it lies in
`Omega(N,m)\F_N`, hence outside every `A_(N,q)`.

For a fixed transposition `a`, the exact number of triples with product `a`
is

```text
D_N=M+6(N-2)+2 binom(N-2,2)
   =(3N^2+N-12)/2,
M=binom(N,2).                                          (2.4)
```

Indeed the first factor is respectively equal to `a`, shares one endpoint
with `a`, or is disjoint from `a`; the remaining two-factor product then has
respectively `M`, `3`, or `2` ordered decompositions.  Including laziness,
the uniform choice among three block sizes, the `m-2` length-three windows,
and the exact conditional fiber, the specified transition probability is

```text
p_N=1/[6(m-2)D_N].                                    (2.5)
```

There is no random choice of a mark or of `f` in (2.5).

### 2.3 Stationary flow and two-sided orientation

Write `mu_N` for uniform measure on `F_N`.  Decomposing the full boundary
flow by block size gives

```text
Q_K(A,A^c)=Q_3(A,A^c)+Q_4(A,A^c)+Q_5(A,A^c)
          >=pi(F_N) mu_N(B_N) p_N.                    (2.6)
```

The `Q_4,Q_5` terms and all other `Q_3` outcomes are retained and
nonnegative.  For either possible mass orientation,

```text
min{pi(A),pi(A^c)}<=pi(A)<=pi(F_N).
```

Dividing (2.6) proves the first inequality in (1.3).  Finally,
`(1-1/N)^(N-4)>=(1-1/N)^N>=1/4` for `N>=4`, while

```text
m-2=2N-4<=2N,  D_N<=2N^2.
```

This proves the explicit `1/(192N^4)` bound.  A paired path rooted at `1`
shows `A_(N,q)` is nonempty.  For `q>=2`, a star centered at `1` lies in its
complement; for `q=1`, disconnected identity words lie in the global
complement.

### 2.4 Proof of the fixed-tree recurrence

After the join edges in `S subseteq E(T)` have appeared, the prefix support
components are exactly the components of `([N],S)`.  A next factor internal
to one of those support components leaves the accepted forest unchanged and
contributes the first term of (1.4).  A factor connecting two components must
be the prescribed unused tree edge `e` by which the forest grows from
`S-{e}` to `S`, contributing the second term.  These alternatives are
disjoint and exhaustive.  The recurrence may contain partial sequences in
which an internal-support factor joins two permutation cycles; such a partial
sequence contributes nothing to the final identity coefficient.  Indeed, in
any connected length-`2N-2` identity word the `N-1` support merges already
account for all `N-1` permutation-cycle joins, so every other factor is a
cycle cut.  Induction on the word length therefore proves (1.4)--(1.5).

The implementation stores `(prefix permutation,S)` rather than symbolic
group-algebra elements.  For one fixed tree its worst-case time is
`O(m 2^(N-1) N! M)` and space is `O(2^(N-1)N!)`; it is an exact bounded
falsifier, not a polynomial-time asymptotic algorithm.

### 2.5 Common-forest lemma and explicit macroscopic jump

For two same-product blocks, prefixes agree before the window and from the
window endpoint onward.  Thus every outside factor has the same join/cut
status and every outside join edge is common.  If the old block has `k`
joins, its height increment is `2k-r`; fixed endpoint heights force the new
block to have the same `k`.  Removing those old edges from a spanning tree
leaves exactly `k+1` common components, and both blocks complete that forest.

For the jump, let `N=3s`, `s>=4`, and let `T` be the path `1-2-...-3s`.
Delete

```text
a=(s,s+1),  b=(2s,2s+1).
```

Choose an interior `z in {s+2,...,2s-1}` and insert

```text
c=(s,z),  d=(z,2s+1).
```

The new graph `T'=T-{a,b}+{c,d}` is a tree with `deg_T'(z)=4`.  Its three
old path components each have `s` vertices and both outer components attach
at `z`, so

```text
diam(T)=3s-1,  diam(T')=2s.                            (2.7)
```

Form a paired identity word from the edges of `T` and place the designated
block as `(a,a,b,b)`.  Replacing it by `(c,c,d,d)` is one exact `H4` outcome,
both words are in `F_N`, and their join trees are `T,T'`.  The identity
four-fiber has exact size

```text
E_N=M^2+18 binom(N,3)+12 binom(N,4),                  (2.8)
```

so this outcome has exact probability `1/[6(m-3)E_N]`, at least
`1/[6(m-3)M^4]`.  This is a rigorous infinite refutation of bounded scalar
sensitivity for diameter/centroid branch geometry.

### 2.6 Exact bounded route refutations

Complete orbit enumeration gives a word in `F_4` whose join tree is a path
and for which every oriented adjacent Hurwitz move still has a path join
tree.  In the scripts' zero-based labels it is

```text
(01),(23),(01),(02),(23),(03).                        (2.9)
```

At `N=5`, the paired path `(12)^2,(02)^2,(34)^2,(04)^2` is another such
state.  Thus pointwise Hurwitz action cannot prove the path-cut bound.  A
different complete `N=5` witness has both join-tree leaves occurring in three
factors, refuting the proposed deletion lemma that every path state has a
degree-two factor-graph leaf.

The exact rooted branch layers at `N=5` are

```text
L_0:       1       2       3       4
count:  8,856 192,744 286,440 519,960.
```

They are not log-concave.  The fixed-tree recurrence independently reproduces
all complete `N=4,5` orbit counts and exactly evaluates every unlabeled tree
shape through `N=8`.  Unrooted diameter, centroid-balance, and edge-balance
layers happen to remain unimodal/log-concave through `N=8`; this is finite
calibration only.  The per-labeled-tree weights are nonuniform: at `N=5`
they are `8856,8254,7808` for star, degree-three, and path shapes, and at
`N=8` their exact ratio is about `1.70457`.

## 3. Probability, runtime, path length, and congestion accounting

- The exact certified source fraction is (2.1), at least `1/(8N)`.
- Each certified exit is one original-`K` transition with exact probability
  (2.5), at least `1/(24N^3)`.
- Multiplying them gives (1.3).  There is no comparison path, vertex load,
  or congestion factor.
- Recognizing the root mark and selecting the window costs `O(m)`; listing
  the `D_N=O(N^2)` three-factor fiber is polynomial in `N`.  The inherited
  direct exact `r=4,5` samplers remain part of `K` but are not needed for the
  lower certificate.
- The fixed-tree recurrence has the explicit worst-case complexity stated in
  section 2.4.  Exact all-shape runs use Prüfer enumeration only as bounded
  falsifiers and have no asymptotic runtime claim.
- Complete `F_4` and `F_5` orbit runs have `2,880` and `1,008,000` states.
  The fixed-tree DP checks totals `C_0(N)` through `N=8`; its `N=8` run took
  about 30 seconds on Python 3.12.3.

## 4. Dependencies, each labeled

1. **PROVED HERE:** Theorem A, including exact mass, all kernel
   normalizations, full-flow orientation, and the `N^-4` bound.
2. **PROVED HERE:** fixed-tree recurrence (1.4)--(1.6), the common-forest
   lemma, the `Theta(N)` `H4` diameter jump, and the analytic auxiliary-route
   refutations.
3. **INHERITED PROVED:** exact heat-bath reversibility/stationarity; minimal
   join edges form a spanning tree; `C_0(N)=(2N-2)!N^(N-3)`; and the content
   character formula for `|Omega|`.
4. **CITED / CONVENTION-CHECKED FOR THE COUNT:** Duchi--Poulalhon--Schaeffer,
   *Uniform random sampling of simple branched coverings of the sphere by
   itself*, Theorem 1 and Corollary 2.  Their displayed word order is reverse
   to the project order; reversal preserves an identity factorization and its
   count.  Their auxiliary Cayley tree is **not** used as the prefix join
   tree.
5. **EXACT FINITE:** all JSON layer arrays, zero-exit witnesses, and fixed-tree
   weights.  They refute only their named universal auxiliary lemmas and do
   not imply asymptotic mixing.
6. **EMPIRICAL:** none enters any claim.  All computations are deterministic.

## 5. First unproved standalone proposition

> **LABEL-SYMMETRIC EDGE-BALANCE THRESHOLD FLOW.**  Let
>
> ```text
> b(T)=max_(e in E(T)) min{|C_e|,N-|C_e|},
> C_(N,q)={w in F_N:b(T_J(w))>=q}.
> ```
>
> There are universal `c>0,C<infinity` such that for every `N>=6` and every
> feasible threshold `1<=q<=floor(N/2)`, the original full chain satisfies
>
> ```text
> Q_K(C_(N,q),C_(N,q)^c)
> /min{pi(C_(N,q)),pi(C_(N,q)^c)} >=cN^(-C).           (5.1)
> ```

The exact stationary numerator in (5.1) is computable from (1.4), but no
uniform asymptotic boundary-flow comparison is known.  Unlike (1.1), a
label-symmetric balanced-edge threshold can exclude every fixed-root marked
reservoir simultaneously.

## 6. Strongest self-attack / failure mode

Theorem A applies to the literal cuts (1.1), which put all disconnected words
in the complement.  Its boundary certificate deliberately exits `F_N` by
deleting the distinguished root.  An enlarged cut that also includes those
missing-root states can seal every certified edge.  Thus the proof does not
control arbitrary refinements, unions over roots, centroid cuts, or internal
full-support bottlenecks.

The marked reservoir is only an averaged `Theta(1/N)` part of `F_N`; there are
states with no one-step macro exit and path states with zero adjacent-Hurwitz
exit.  The fixed-tree recurrence supplies exact masses but no asymptotic
isoperimetry.  Finally, the macroscopic `H4` jump shows that the usual thin
shell argument is unavailable for the next label-symmetric cuts.  These are
substantial reasons the result cannot be promoted to Terminal A or B.

## 7. Calibration suite

- **Odd `m`:** `Omega(N,m)` is empty by sign.  The theorem uses even
  `m=2N-2`.
- **`m=0`, `N=2`:** singleton cases are outside `N>=4`.
- **`m=2,N>=3`:** excluded disconnected case; no size-two simulation is used.
- **`S_3,m=4`:** `Omega` has 27 words and four pure-Hurwitz components.  The
  `r=4` update is whole-word heat bath; its contribution alone gives every
  nontrivial cut conductance at least `1/8`, so the small endpoint is safe.
- **`S_4,m=4`:** all 120 words and 13 Hurwitz components are joined by the
  whole-word `H4` contribution; it is never omitted from a normalization.
- **`S_4,m=6`:** `Omega` has 3936 words and 17 Hurwitz components;
  `|F_4|=2880`, the fixed-root leaf layer has 1626 words, and the marked
  reservoir has exactly 360.  Formula (1.3) uses all three block sizes.
- **Near-minimal doubled trees:** included.  The macroscopic-jump construction
  uses paired trees only as a one-edge witness, not as a canonical routing
  hub.
- **Disjoint components/order:** the exit outcome remains the literal ordered
  word and merely omits the root label; no graph-only quotient is substituted.
- **Parity:** neither edge-multiplicity nor vertex-degree parity is used as an
  identity characterization.
- **Canonical hub/L=2:** no hub, normal form, or length-two simulation occurs.
- **Mass orientation:** (1.6) is exact, while the proof handles the unknown
  smaller side by `min<=pi(A)<=pi(F_N)`.

## 8. Artifact paths and reproduction commands

Owned artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/
  plan.md
  checkpoint.md
  report.md
  branch_geometry_falsifier.py
  branch-N4.json
  branch-N5.json
  fixed_join_tree_dp.py
  tree-dp-N4.json
  tree-dp-N5.json
  tree-dp-N6.json
  tree-dp-N7.json
  tree-dp-N8.json
```

Exact deterministic commands (seed is `null`; no nonstandard dependency):

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/branch_geometry_falsifier.py --N 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/branch-N4.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/branch_geometry_falsifier.py --N 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/branch-N5.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/fixed_join_tree_dp.py --N 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/tree-dp-N4.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/fixed_join_tree_dp.py --N 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/tree-dp-N5.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/fixed_join_tree_dp.py --N 6 --output experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/tree-dp-N6.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/fixed_join_tree_dp.py --N 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/tree-dp-N7.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/fixed_join_tree_dp.py --N 8 --output experiments/20260811-polynomial-mixing-resolution/cycle-11/mission-M47-branch-geometry-redteam/tree-dp-N8.json
```

The scripts record Python `3.12.3`, argv, seed, convention, and the exact
universal claim each bounded run can falsify.  The two independent methods
agree at `N=4,5`, and every fixed-tree total agrees with `C_0(N)` through
`N=8`.

## 9. Verdict

**PROVED.**

This verdict is scoped to Theorems A--C, especially the uniform
inverse-polynomial rejection of every rooted largest-pendant-branch threshold
cut.  It is not Terminal A or Terminal B; the first global branch-cut gap is
the label-symmetric proposition (5.1).
