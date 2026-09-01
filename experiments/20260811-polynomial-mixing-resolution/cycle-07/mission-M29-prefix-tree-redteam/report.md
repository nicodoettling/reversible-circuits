# M29 final report: removable-leaf cut rejected; median excursion still open

This mission found no TERMINAL-B family.  It proves an inverse-polynomial
full-`K` conductance bound for a genuinely overlap-heavy tree/peak cut in the
minimal connected macro, proves exact locality for all prefix-height
statistics, and gives two rigorous counterexamples to tempting routes toward
a universal median-shell theorem.  The scoped verdict is `PROVED`; it is not
a global resolution.

## 1. Exact claims, quantifiers, and convention

Permutations are maps on `[N]`; `pq` means `p` after `q`, so
`(pq)(x)=p(q(x))`.  A word evaluates as `t_1...t_m`.  Put

```text
M=binom(N,2),
Omega(N,m)={w in T_N^m:t_1...t_m=id},
R_m={r in {3,4,5}:r<=m},
B=|R_m|,
K=(1/2)I
  +(1/(2B)) sum_(r in R_m) 1/(m-r+1) sum_i H_(i,r),
```

where `H_(i,r)` is uniform on the exact length-`r` same-product fiber.
The target `pi` is uniform on the global `Omega(N,m)`.

For the rest of the theorem let `N>=6`, `m=2N-2` (hence `B=3`), and

```text
F_N={w in Omega(N,m):the support graph is connected on all [N]}.
```

A **removable leaf mark** of `w in F_N` is an adjacent square

```text
t_i=t_(i+1)=(uv)
```

together with a distinguished endpoint `v` such that `v` occurs in no other
factor and deleting the square leaves a word in `F_(N-1)` on
`[N]\{v}`.  Let `Z(w)` be the number of marks and define the global cut

```text
A_N={w in F_N:Z(w)>=1}.                                (1.1)
```

The first copy of a marked square is a join, the second is a cut, and `v` is
a leaf of the prefix join tree.  Thus (1.1) is simultaneously a local Dyck
peak and a join-tree-leaf threshold, not a fixed canonical word or a fixed
balanced separator.

### Theorem A: removable-leaf union anti-bottleneck

For every `N>=6`, `A_N` is nonempty and is the smaller global side.  With

```text
D_N=(3N^2+N-12)/2,                                    (1.2)
```

its exact lazy full-chain conductance satisfies

```text
Phi_pm^K(A_N)
 =Q_K(A_N,A_N^c)/min{pi(A_N),pi(A_N^c)}
 >=1/[144(m-2)D_N]
 >=1/(576N^3).                                         (1.3)
```

All overlap in the union (1.1) is counted exactly.  If `(N)_k` is the falling
factorial and `C_0(N)=(2N-2)!N^(N-3)`, then the number `I_(N,k)` of states
with an **ordered** `k`-tuple of distinct marks is

```text
I_(N,k)
 =(N)_k (2N-k-2)! (N-k)^(N-3),   1<=k<=N-1.           (1.4)
```

The convention `C_0(1)=1` makes the endpoint `k=N-1` literal.  Hence

```text
|A_N|=sum_(k=1)^(N-1)(-1)^(k+1) I_(N,k)/k!,           (1.5)
|{w in F_N:Z(w)=1}|
     =sum_(k=1)^(N-1)(-1)^(k-1) I_(N,k)/(k-1)!.       (1.6)
```

Writing

```text
|Omega(N,m)|
 =(1/N!) sum_(lambda partition N)(f^lambda)^2 c_lambda^m,
```

the exact global stationary mass is (1.5) divided by this character sum.
In particular no union bound or unsupported orientation is used.

### Theorem B: exact full-window locality

For any same-product length-`r` replacement, `r in {3,4,5}`, and each
internal block prefix `1<=k<=r-1`,

```text
|Delta h_(i+k-1)|<=2 min(k,r-k),                       (1.7)
```

where `h_j=N-cycles(t_1...t_j)`.  Therefore an update changes Dyck area by
at most `4,8,12` for `r=3,4,5`, respectively, and changes a fixed-time or
maximum height by at most `4`.  Within `F_N`, it changes at most `r` join
edges, at most `4r` join-tree leaf indicators, and at most `r+1` peaks.

For an area threshold `A_q={w in F_N:Area(w)<=q}`, every internal boundary
transition starts in its width-12 shell; any other boundary transition leaves
`F_N`.  This is an exact reduction, not a shell-mass estimate.

### Two exact route refutations

1. At `N=5`, the area layers on the feasible parity lattice
   `4,6,8,10,12,14,16` have counts

   ```text
   3000,23400,60600,132840,207600,205560,375000.
   ```

   They are neither unimodal nor log-concave.  Universal unimodality cannot
   be used as the missing weighted-shell theorem.

2. At `N=6,m=10`, the exact identity word

   ```text
   (01),(24),(03),(02),(35),(15),(34),(23),(04),(05)   (1.8)
   ```

   remains connected after deleting any five consecutive factors.  Thus
   every `r<=5` update retains an unchanged connected spanning subgraph and

   ```text
   K_(6,10)(w,F_6^c)=0.                                (1.9)
   ```

   This refutes a pointwise macro-exit shortcut, not irreducibility or
   polynomial mixing.

## 2. Full proof and constructions

### 2.1 Ordered multi-mark deletion/insertion

Distinct marks have disjoint square blocks.  Moreover the neighbor of a
marked label cannot itself be marked: otherwise that label would occur both
in its own square and in the other marked square.  Deleting an ordered
`k`-tuple of marks therefore leaves:

1. an ordered choice of omitted labels, in `(N)_k` ways;
2. for each omitted label, a neighbor among the `N-k` base labels, in
   `(N-k)^k` ways;
3. a minimal connected identity word on those base labels, in `C_0(N-k)`
   ways;
4. an interleaving of `k` distinct indivisible two-factor blocks with the
   `L=2(N-k)-2` ordered base factors.

The last count is

```text
binom(L+k,k)k!=(L+k)!/L!
              =(2N-k-2)!/(2N-2k-2)!.                  (2.1)
```

The core support after deletion is connected: marked vertices are graph
leaves, so they cannot connect two core components.  Conversely, inserting
the chosen squares into a connected base makes every chosen label a
removable leaf (the output may have additional unselected marks).  Deletion
recovers every datum, so this is a bijection of ordered marked incidences.
Substituting

```text
C_0(N-k)=(2N-2k-2)!(N-k)^(N-k-3)
```

into the product of the four counts proves (1.4).  A state with `z` marks
occurs `(z)_k` times, so ordinary inclusion-exclusion gives (1.5).  The
identity

```text
sum_(k=1)^z (-1)^(k-1)(z)_k/(k-1)!=1[z=1]
```

gives (1.6).

### 2.2 A constant fraction has exactly one mark

Under the uniform conditional law on `F_N`, (1.4) gives

```text
E Z
 =1/2 ((N-1)/N)^(N-4),                                (2.2)
E (Z)_2
 =N/[2(2N-3)] ((N-2)/N)^(N-3).                        (2.3)
```

For every integer `z>=0`,

```text
1[z=1]>=z-z(z-1).                                      (2.4)
```

Also `log(1-x)>=-x/(1-x)` gives
`(1-1/N)^(N-4)>e^-1`.  The elementary estimate `e<3` follows by comparing
the factorial tail strictly with `sum_(k>=2)2^(-(k-1))=1`, so

```text
E Z>1/6.                                               (2.5)
```

For `N>=6`, the prefactor in (2.3) is at most `1/3`, while

```text
(1-2/N)^(N-3)
 <=exp(-2(N-3)/N)<=e^-1<3/8.
```

The last strict inequality follows already from
`e>1+1+1/2+1/6=8/3`.  Hence

```text
Pr_F[Z=1]
 >=E Z-E(Z)_2>1/6-1/8=1/24.                           (2.6)
```

At the same time

```text
Pr_F[Z>=1]<=E Z<1/2                                   (2.7)
```

because `N>=6` makes the positive exponent in (2.2) strict.  Thus (1.1) is
nonempty and, even before multiplying by `pi(F_N)<=1`, has global mass below
`1/2`.  This proves the exact smaller-side orientation.

### 2.3 Exact three-factor normalization

Fix a transposition `a`.  The number of ordered transposition triples
`x,y,z` with `xyz=a` is `D_N`.  Indeed `yz=xa`.  If `x=a`, there are `M`
choices `y=z`.  There are `2(N-2)` choices of `x` sharing exactly one
endpoint with `a`; `xa` is then a 3-cycle and has exactly three ordered
two-transposition factorizations.  There are `binom(N-2,2)` choices disjoint
from `a`; `xa` is a pair of disjoint transpositions and has exactly its two
orders.  Therefore

```text
D_N=M+3*2(N-2)+2*binom(N-2,2)
   =(3N^2+N-12)/2.                                     (2.8)
```

This independently proves the conditional-fiber normalization used below.

### 2.4 One full-`K` exit from every uniquely marked state

Let `w` have its unique mark `(e,e)` with distinguished leaf `v`.  Choose
any transposition `f` on the connected base labels `[N]\{v}`.  If the square
is not the final pair, take the `H_3` window beginning at it and specify

```text
(e,e,a)->(f,f,a).                                      (2.9)
```

For the final pair use the window ending at `m` and specify

```text
(a,e,e)->(a,f,f).                                      (2.10)
```

Both ordered block products are the transposition `a`.  The outcome removes
every occurrence of `v`, so it lies in `F_N^c`, hence in `A_N^c`.  By (2.8)
the exact probability of the specified outcome, including laziness,
block-size scan, window scan, and heat-bath choice, is

```text
q_N=1/[2B(m-2)D_N].                                    (2.11)
```

There is no extra choice-of-mark or choice-of-`f` probability: both are
selected deterministically for the witness.

### 2.5 Full stationary flow and two-sided conductance

Let `mu` be uniform on `F_N`.  The positive `r=3` contribution gives

```text
Q_K(A_N,A_N^c)
 >=pi(F_N) mu(Z=1) q_N.                                (2.12)
```

The `r=4,5` terms and every other `r=3` outcome remain present and
nonnegative.  Since

```text
pi(A_N)=pi(F_N)mu(Z>=1)<1/2,
```

division by the exact smaller side and (2.6) yield

```text
Phi_pm^K(A_N)
 >=[mu(Z=1)/mu(Z>=1)]q_N
 >=mu(Z=1)q_N
 >1/[48B(m-2)D_N].                                    (2.13)
```

Now `B=3`, `m-2<=2N`, and `D_N<=2N^2`, which proves (1.3).

### 2.6 Prefix-height and tree locality

Suppose old and new blocks `a_1...a_r` and `b_1...b_r` have the same product.
At internal time `k`, their relative prefix is a word of at most `2k`
transpositions.  Equality of the block endpoints expresses the same relative
permutation through the two suffixes, using at most `2(r-k)` transpositions.
The all-transposition Cayley metric is bi-invariant, and
`N-cycles(sigma)` is its distance from identity.  The triangle inequality
therefore proves (1.7).  Summing (1.7) gives `4,8,12`.

Prefixes and factors outside the window agree, so only the `r` internal
join/cut steps can change.  In the minimal macro, join factors form a tree;
therefore at most `r` old and `r` new tree edges differ.  The stated peak,
leaf, and degree bounds follow by counting affected adjacent step pairs and
edge endpoints.

### 2.7 Exact finite counterexamples

The deterministic `N=5` enumeration begins at a paired spanning-tree word,
closes under both project Hurwitz orientations, and obtains exactly

```text
(2N-2)!N^(N-3)=1,008,000
```

states.  Since every generated state lies in `F_5`, equality with the exact
total count proves completeness; no finite-to-asymptotic inference is made.
Its area counts give the first route refutation in field 1.

For (1.8), the fixed-seed search is only a discovery mechanism.  The emitted
witness is independently checked to have product identity and connected
support.  The output also checks all six length-five intervals.  Any shorter
legal window is contained in one of them, and its unchanged complement
connects all labels.  This proves (1.9) without a probabilistic claim.

## 3. Probability, runtime, path length, and congestion accounting

- The exactly counted certified conditional mass is `Pr_F[Z=1]>1/24`.
- One specified exit has probability exactly (2.11).  With `B=3`, the final
  conductance lower bound is `1/[144(m-2)D_N]>=1/(576N^3)`.
- Every certified exit is one original-`K` step.  No comparison path,
  canonical hub, or congestion estimate is used.
- Finding all marks by recording label occurrences and scanning adjacent
  pairs costs polynomial time, for example `O(Nm)`.  Enumerating or directly
  indexing the `D_N=O(N^2)` transposition-product fiber is polynomial.
- The exact `N=5` orbit run visited 1,008,000 states and took 23.9 seconds
  with the extra cut-span diagnostic (8.1 seconds without it).  It is a named
  finite falsifier, not a mixing experiment.
- The exact `N=3,4` full-kernel audit enumerates all 27 and 3936 identity
  states and every conditional outcome for every legal window.  At `N=4`,
  the cut has exact global mass `49/164`; its `r=3,4,5` stationary boundary
  contributions are respectively

  ```text
  4661/157440, 234107/6907680, 5635/161376.
  ```

  Their sum is `222978947/2265719040` in each direction.

## 4. Dependencies, each labeled

1. **PROVED HERE:** ordered multi-mark bijection (1.4), exact
   inclusion-exclusion (1.5)--(1.6), moment bounds (2.2)--(2.7), exact
   three-factor count (2.8), full-`K` exit and normalization
   (2.9)--(2.13), prefix locality (1.7), and both finite counterexamples.
2. **INHERITED PROVED / CITED AND CONVENTION-CHECKED:**
   `C_0(N)=(2N-2)!N^(N-3)` and the fact that minimal connected join factors
   form a spanning tree.  Reversal translates sources that display products
   in the opposite order; the identity count is unchanged.
3. **INHERITED PROVED:** exact heat-bath reversibility/stationarity and the
   character/content formula for `|Omega(N,m)|`.  Reversibility is checked
   again in the finite flows.
4. **CITED RESOURCE, NOT USED AS A DYNAMICAL THEOREM:** Duchi--Poulalhon--
   Schaeffer, *Uniform random sampling of simple branched coverings of the
   sphere by itself*, Proposition 1, Theorem 4, and Proposition 3.  They give
   the quadrangulation/Hurwitz-tree bijections and perfect sampler, but no
   prefix-Dyck marginal or local-move intertwining.
5. **CITED AND FOUND INAPPLICABLE:** Féray--Louf--Thévenin, *Random generation
   and scaling limits of fixed genus factorizations into transpositions*,
   DOI `10.1007/s00440-022-01170-9`, studies a long-cycle endpoint, not the
   identity factorization in this mission.
6. **EXACT FINITE:** the layer arrays, small full-`K` flows, and witness
   checks.  These can refute their named universal lemmas but do not prove an
   asymptotic gap.
7. **EMPIRICAL:** only the number of Hurwitz search steps needed to discover
   (1.8), and nonfinding in other bounded searches.  Neither enters a claim.

## 5. First unproved standalone proposition

> **AREA-MEDIAN INTERNAL SHELL/ACTION.**  There are universal constants
> `c>0,C<infinity` such that for every `N>=6` and every integer `q` satisfying
>
> ```text
> 1/4<=Pr_(uniform F_N)[Area<=q]<=1/2,
> ```
>
> the original full chain satisfies
>
> ```text
> (1/|{w in F_N:Area(w)<=q}|)
> sum_(w in F_N:Area(w)<=q) K(w,Omega(N,2N-2)\{Area<=q})
> >=cN^(-C).                                            (5.1)
> ```

By (1.7), only a width-12 internal area shell plus exits from `F_N` can
contribute.  The exact `N=5` failure of unimodality and the `N=6` zero-macro-
exit witness show that neither term is controlled by the two obvious
shortcuts.  The analogous midpoint-height and join-tree-leaf median
propositions remain open, but (5.1) is the smallest single-statistic gap.

## 6. Strongest self-attack / failure mode

The proved cut sees only leaves whose unique incident factor appears as an
immediately cancelling square.  A word can have many ordinary join-tree
leaves and no such mark, and an arbitrary area or centroid subset can
deliberately avoid the counted certificate.  In fact (1.8) has zero macro
exit for every update, so no pointwise repair of the averaged leaf-square
argument is possible.

The exact multi-mark distribution also says nothing about correlations with
area, midpoint height, ordinary leaf count, or centroid balance.  Area layers
are already nonunimodal at `N=5`; an asymptotic weighted-shell estimate would
need new map/factorization enumeration or an internal isoperimetric argument.
Finally, even proving (5.1) would reject only one family of cuts inside one
macro and would not establish a spectral gap for arbitrary functions.

## 7. Calibration suite

- **Odd `m`:** `Omega(N,m)` is empty by sign; all theorem words have even
  `m=2N-2`.
- **`m=0` and `N=2`:** singleton cases are outside `N>=6`.  The multi-mark
  base convention `C_0(1)=1` is only enumerative.
- **`m=2,N>=3`:** the excluded disconnected-chain regime is not used.
- **`S_3,m=4`:** exact enumeration gives 27 identity words and retains the
  four pure-Hurwitz components.  Here the mark histogram on the 24-state
  full orbit is `{0:12,1:6,2:6}`; `A` has global mass `4/9` and exact
  conductance `5/18`.
- **`S_4,m=4`:** there are 120 identity words and 13 pure-Hurwitz components.
  No full-support minimal word exists because `4<2(4-1)`.  The exact kernel's
  `H_4` is a whole-word heat bath and is never dropped.
- **`S_4,m=6`:** exact enumeration gives 3936 words and 17 pure-Hurwitz
  components.  On the 2880-state full orbit the mark histogram is
  `{0:1704,1:936,2:216,3:24}`.  All three block-length flows are listed in
  field 3.
- **Near-minimal doubled trees:** paired spanning-tree words are included;
  no routing through one such exponentially rare hub is used.
- **Ordered interleavings:** every square is inserted as an indivisible block
  into the ordered base word; equation (2.1) counts its position and the
  ordering among other marked blocks exactly.  Nothing is collapsed to an
  unordered graph.
- **Parity:** no edge- or degree-parity characterization is used.  Identity is
  preserved by exact cancelling-square insertion/deletion and verified word
  products.
- **Failed `L=2` simulation:** the exit is an actual `H_3` outcome; no claim
  about simulating arbitrary length-two fibers is made.
- **Mass orientation:** (1.5) is the exact overlap-aware mass, and (2.7)
  proves `pi(A_N)<1/2`.  A rare fixed hub or an unaccounted union bound is not
  used.

## 8. Artifacts and reproduction commands

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-07/mission-M29-prefix-tree-redteam/
```

Core files are `plan.md`, `checkpoint.md`, this `report.md`,
`exact_peak_tree_layers.py`, `all_state_macro_exit_falsifier.py`, and
`random_cut_span_search.py`.  Machine-readable outputs are `layers_N4.json`,
`layers_N5.json`, `macro_exit_N3.json`, `macro_exit_N4.json`, and the
`cut_span_N6_seed*.json` witness files.

Exact commands:

```bash
python3 experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M29-prefix-tree-redteam/exact_peak_tree_layers.py --N 5 --output experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M29-prefix-tree-redteam/layers_N5.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M29-prefix-tree-redteam/all_state_macro_exit_falsifier.py --N 3 --output experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M29-prefix-tree-redteam/macro_exit_N3.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M29-prefix-tree-redteam/all_state_macro_exit_falsifier.py --N 4 --output experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M29-prefix-tree-redteam/macro_exit_N4.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M29-prefix-tree-redteam/random_cut_span_search.py --N 6 --steps 200000 --seed 290731 --output experiments/20260811-polynomial-mixing-resolution/cycle-07/mission-M29-prefix-tree-redteam/cut_span_N6_seed290731.json
```

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
Python: `3.12.3`; no nonstandard package is used.  The deterministic runs
have seed `null`; stochastic discovery records seed `290731`, but the emitted
witness is checked exactly and does not rely on sampling probability.

## 9. Verdict

PROVED

This verdict is scoped to Theorem A, the removable-leaf-union candidate-cut
rejection (1.3), together with the locality theorem.  It is not TERMINAL A or
TERMINAL B.  The first open implication is the AREA-MEDIAN INTERNAL
SHELL/ACTION proposition (5.1).
