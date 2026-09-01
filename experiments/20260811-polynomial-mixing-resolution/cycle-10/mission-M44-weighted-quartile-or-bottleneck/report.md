# M44 final report — graphic-rank reduction; weighted quartile remains open

This mission does **not** prove the requested weighted quartile-shell bound and
does **not** construct a Terminal-B sequence.  It gives a new exact
graphic-matroid representation of the statistic, a complete upper reduction
for every `H_3,H_4,H_5` boundary contribution (including exits from the
minimal macro), and an exact `N=4` refutation of the most natural Lorentzian
positive-transfer route.  A separately declared tilted-perfect-matching law
has a polynomial-looking quartile shell in bounded calculations, but it is not
the factorization law and no uniform Radon comparison has been proved.

## 1. Exact claims, quantifiers, kernel, and convention

Permutations are maps on `[N]`; `pq` means `p` after `q`, so
`(pq)(x)=p(q(x))`.  Words evaluate as `t_1...t_m`.  The global chain is

```text
M=binom(N,2),
R_m={r in {3,4,5}:r<=m},
K=(1/2)I
  +(1/(2|R_m|)) sum_(r in R_m) 1/(m-r+1) sum_i H_(i,r),             (1.1)
```

where `H_(i,r)` is uniform on the exact same-product length-`r`
transposition fiber.  Its stationary law `pi` is uniform on `Omega(N,m)`.

For the area problem put `N>=3`, `n=N-1`, `m=2n`, and

```text
F_N={w in Omega(N,m):the factor-support graph is connected on [N]},
mu_N=Uniform(F_N),
x_j=t_1...t_j,
h_j=N-cycles(x_j),
Area(w)=sum_(j=1)^m h_j,
H_N(a)=#{w in F_N:Area(w)=a}.                                     (1.2)
```

The following statements are proved.

### Theorem 1 (prefix graphic rank and greedy-basis positions)

Let `G_j(w)` be the support multigraph of the first `j` factor occurrences,
let `c_j` be its number of connected components including isolated labels,
and let `r_j=N-c_j` be its graphic rank.  For every `w in F_N` and every
`0<=j<=m`,

```text
h_j=2r_j-j=2(N-c_j)-j.                                             (1.3)
```

If `J_1<...<J_n` are the positions at which the ordered greedy scan of the
support multigraph accepts an edge into its spanning forest, then

```text
Area(w)=2 sum_(j=1)^m r_j-m(m+1)/2
       =n(2n+1)-2 sum_(k=1)^n J_k.                                (1.4)
```

Thus the weighted Dyck area is exactly an integrated graphic-rank statistic,
or equivalently an affine transform of the total greedy-basis acceptance
time, on uniform increasing planar maps.

### Theorem 2 (exact full-`K` boundary upper reduction)

For any same-product replacement of a length-`r` window, with `r=3,4,5`,

```text
|Delta Area|<=delta_r:=2 floor(r^2/4),
(delta_3,delta_4,delta_5)=(4,8,12).                                (1.5)
```

For a feasible `q` let

```text
A_q={w in F_N:Area(w)<=q}.
```

Let `Sep_(i,r)(w)` be the event that deleting factor positions
`i,...,i+r-1` from the support multigraph of `w` leaves a disconnected graph
on `[N]` (isolated labels count as components).  With `B=|R_m|`, the complete
stationary boundary satisfies

```text
Q_K(A_q,A_q^c)
 <=pi(F_N)/(2B) sum_(r in R_m) [
      mu_N(q-delta_r<Area<=q)
      +1/(m-r+1) sum_i mu_N(A_q intersect Sep_(i,r))
   ].                                                               (1.6)
```

This accounts for every `H_3,H_4,H_5` crossing and for every exit from
`F_N`; it is not a graph-only surrogate.  Consequently a superpolynomially
thin area shell is not by itself a Terminal-B bottleneck.  One must also make
the consecutive-window separator term in (1.6) superpolynomially small.

### Theorem 3 (the direct Lorentzian route is refuted)

For the exact fixed-path weights from M38 define the homogeneous multiaffine
join-position polynomial

```text
F_N(z_0,...,z_(2n-1))
 =sum_(Dyck P) W_N(P) product_(j:P_j=U) z_j.                        (1.7)
```

Then `F_4` is not Lorentzian.  More precisely, after differentiating in
`z_0`, the quadratic Hessian on variables `z_1,z_2,z_3,z_4` has inertia
exactly `(2 positive,2 negative)`.  This refutes the universal claim, not
merely a numerical sufficient test.  Since an exponential area tilt in (1.4)
is a positive diagonal rescaling of the variables, no such tilt repairs the
obstruction.

### Theorem 4 (exact positive matching reference and its un-tilted moments)

For a Dyck path `P` of semilength `n`, put

```text
p(P)=product_(D steps) (height immediately before the D step).
```

This is the number of perfect matchings of `[2n]` with opener/closer path
`P`.  Its area coefficients

```text
G_n(a)=sum_(P:Area(P)=a) p(P)                                     (1.8)
```

are given exactly by the positive transfer

```text
(h,a)->(h+1,a+h+1)  with multiplicity 1,
(h,a)->(h-1,a+h-1)  with multiplicity h,                           (1.9)
```

starting and ending at height zero.  In particular
`sum_a G_n(a)=(2n-1)!!`.

Under the un-tilted uniform-matching law, if `A_match` is this path area,

```text
E[A_match]=n+(4/3)binom(n,2),
Var(A_match)=4n(n-1)(2n+1)/45.                                    (1.10)
```

Equation (1.10) is a genuine moment theorem, but a variance estimate cannot
lower-bound a specified lattice atom and therefore does not settle the
quartile shell.

## 2. Full arguments

### 2.1 Proof of the graphic-rank identity

M34 proved that the `n=N-1` factors that raise prefix permutation rank form a
spanning tree.  Recall the short reason needed here.  At every prefix, each
cycle of the prefix permutation lies inside a component of the graph formed
by join factors already seen.  A cut factor has both endpoints in one prefix
cycle and therefore cannot connect two join-graph components.  Since the full
support is connected, the final join graph is connected; it has `N` vertices
and exactly `N-1` edges, so it is a tree.  Every join factor therefore joins
two distinct current join-forest components.

It follows inductively that the components of the full prefix support graph
`G_j` are exactly the components of the prefix join forest: cut edges stay
inside one such component and join edges merge exactly two.  Hence the number
of joins through time `j` equals `r_j=N-c_j`.  The other `j-r_j` factors are
cuts, so

```text
h_j=(# joins)-(# cuts)=r_j-(j-r_j)=2r_j-j,
```

which proves (1.3).

The greedy scan accepts precisely those join-tree edges, at positions
`J_1,...,J_n`.  Thus

```text
sum_(j=1)^m r_j=sum_(k=1)^n (m-J_k+1).
```

Substitution in (1.3), using `m=2n`, gives (1.4).

Duchi--Poulalhon--Schaeffer, Proposition 2.1, identifies these ordered
support multigraphs with increasing edge-labelled planar maps.  Their factor
convention is `tau_m...tau_1=id`; reversing the factor list translates it to
the convention here.  This reversal preserves area: the length-`j` reverse
prefix equals the original length-`m-j` prefix, and the endpoint ranks at
times zero and `m` are both zero.  No convention change is hidden in (1.4).

### 2.2 Proof of the width bounds and all-boundary formula

Consider old and new length-`r` block paths with the same starting prefix and
the same endpoint.  At internal offset `k`, their intermediate permutations
are at Cayley distance at most `2k` via the common start, and at most
`2(r-k)` via the common endpoint.  Cayley rank is one-Lipschitz in Cayley
distance, hence the two intermediate ranks differ by at most

```text
2 min(k,r-k).
```

Summing for `1<=k<=r-1` gives `2 floor(r^2/4)`, proving (1.5).

If an update stays in `F_N` but crosses from `A_q` to its complement, its old
state must lie in `q-delta_r<Area<=q`.  For a fixed `r`, averaging over the
`m-r+1` windows and bounding each conditional crossing probability by one
therefore contributes at most

```text
pi(F_N) mu_N(q-delta_r<Area<=q)/(2B).
```

Now suppose an update exits `F_N`, and let `rho` be the labeled support
component partition of the new word, including isolated labels.  Every factor
outside the updated window is unchanged and has both endpoints in one block
of `rho`.  Deleting the old window therefore leaves no edge crossing `rho`,
so `Sep_(i,r)` is necessary for this exit.  The exact conditional-fiber exit
probability is at most one, giving

```text
Q_K(A_q,F_N^c)
 <=1/(2B) sum_r 1/(m-r+1) sum_i pi(A_q intersect Sep_(i,r)).        (2.1)
```

Adding the internal-crossing bound and using
`pi(E)=pi(F_N)mu_N(E)` for `E subset F_N` proves (1.6).  The factor `1/2`
is laziness, `1/B` is block-size selection, and `1/(m-r+1)` is window
selection.  No conditional-fiber normalization is omitted: for an upper bound
it is used only through `H_(i,r)(w,event)<=1`.

For comparison, for `N>=6` the inherited M34 lower action says that if
`mu_N(A_q)<=1/2`, then

```text
Phi_pm^K(A_q)
 >=[H_N(q)/sum_(a<=q)H_N(a)]/[6(m-2)M^3].                          (2.2)
```

Thus the requested coefficient theorem would reject the median-area cut at
once.  Conversely, a Terminal-B proof from this cut would need upper bounds
on both terms in (1.6), divided by the exact global mass
`pi(A_q)=pi(F_N)mu_N(A_q)`.

### 2.3 Exact Lorentzian obstruction

For `N=4`, the five path weights are

```text
UDUDUD:96, UDUUDD:264, UUDDUD:264,
UUDUDD:720, UUUDDD:1536.
```

After `partial/partial z_0`, the Hessian on variables `[1,2,3,4]` is

```text
H=[[0,1536,720,264],
   [1536,0,264,96],
   [720,264,0,0],
   [264,96,0,0]].                                                    (2.3)
```

In `2 by 2` block form this is `[[A,B],[B^T,0]]` with

```text
B=[[720,264],[264,96]],   det(B)=-576.
```

Since `B` is nonsingular, a triangular congruence eliminates `A` and turns
the quadratic form into `2x^TBy`; hence its inertia is `(2,2)`.  A
Lorentzian quadratic has at most one positive Hessian eigenvalue.  This is the
exact obstruction; NumPy was used only to locate it.

By (1.4), multiplication of every coefficient by `s^Area(P)` is, up to the
common factor `s^[n(2n+1)]`, the variable rescaling
`z_j -> s^(-2j)z_j`.  Hessians transform by positive diagonal congruence, so
the same inertia obstruction survives every positive exponential area tilt.

### 2.4 Perfect-matching reference, endpoint matching, and moments

At a down-step from height `h`, a matching may close any one of the `h` open
endpoints.  This proves `p(P)` and the exact transfer (1.9).

The direct un-tilted comparison with the factorization law is exponentially
false.  For the bottom and mountain paths, inherited exact formulas give

```text
W_N((UD)^n)=n! N^(n-1),       p((UD)^n)=1,
W_N(U^nD^n)=n! N^(2n-2),      p(U^nD^n)=n!.
```

Therefore

```text
[W(top)/p(top)]/[W(bottom)/p(bottom)]=N^(n-1)/n!,                  (2.4)
```

which is exponential in `n`.  The unique exponential tilt matching these two
endpoint densities is

```text
q_n=[N^(n-1)/n!]^[1/(n(n-1))],
R_n(P)=p(P)q_n^Area(P).                                             (2.5)
```

It is a useful benchmark, not an asserted identity.

For (1.10), view a uniform matching as `n` exchangeably labelled intervals.
For two edges let `X=1` when they cross or nest rather than align.  Of the
three relative pairings of four endpoints, two overlap, so
`E[X]=2/3` and `Var(X)=2/9`.  Indicators for disjoint pairs of edge labels are
independent.  For two indicators sharing one edge, the 90 equiprobable words
with two copies of each of three edge labels split as

```text
(both overlap, first only, second only, neither)=(44,16,16,14).
```

For example, the `14` in the last cell consists of six orders with the shared
edge before the other two, six with it after them, and the two orders with it
strictly between them.  Hence the shared-edge covariance is
`44/90-4/9=2/45`.  With `K_match` the number of crossing-or-nesting edge
pairs,

```text
Var(K_match)
 =binom(n,2)2/9+2[3binom(n,3)]2/45
 =n(n-1)(2n+1)/45.                                                   (2.6)
```

Every pair of matching edges contributes zero extra span if aligned and two
if crossing or nesting, so `A_match=n+2K_match`.  This proves (1.10).

Duchi--Poulalhon--Schaeffer, Proposition 4.1, supplies an `N`-to-one
Cayley-tree/permutation encoding of the actual Hurwitz trees.  Pairing the two
permutation labels placed at each inserted black degree-two vertex indeed
produces a uniform perfect matching.  However, their subsequent closure
algorithm changes the factor support map; it does not identify the actual
join/cut path with this matching's opener/closer path.  Already at `N=4`, the
actual path coefficients above are not proportional to the matching
coefficients.  Thus (2.5) is not promoted without a new comparison theorem.

### 2.5 A concrete sufficient statement weaker than global unimodality

Let `q_N` be the first feasible area with lower CDF at least `1/4`, and put

```text
L_N=1+(n^2-n)/2,
```

the total number of parity-compatible layers.  It would suffice to prove

```text
mu_N(Area<=q_N)<=1/2,
H_N(q_N)>=H_N(a) for every feasible a<=q_N.                         (2.7)
```

Indeed, if `H_N(q_N)>=|F_N|/8`, its shell/CDF ratio is at least `1/4`.
Otherwise the preceding CDF is at least `1/8`; (2.7) and the `L_N` possible
layers give `L_N H_N(q_N)>=|F_N|/8`, hence

```text
H_N(q_N)/sum_(a<=q_N)H_N(a)>=1/(4L_N)=Omega(N^-2).                  (2.8)
```

This **first-quartile prefix-record** condition is strictly weaker than global
rank unimodality.  It holds in the exact tables through `N=14`, but no
universal injection, recurrence inequality, or positive-transfer theorem is
known.  M38's one-sided no-cliff inequality
`H_N(a+2)>=H_N(a)/(N-1)` does not imply it over `Theta(N^2)` layers.

## 3. Probability, runtime, path length, and congestion accounting

- The exact lower crossing used if the coefficient proposition is proved is
  one padded `H_3` transition.  Its probability is
  `1/[6(m-2)F_3(g)]>=1/[6(m-2)M^3]`; this includes laziness, the `1/3`
  block-size choice, the specified window, and its exact conditional outcome.
  `H_4,H_5` are retained and discarded only as nonnegative flow in (2.2).
- The upper accounting is exactly (1.6).  It includes all three block sizes,
  all windows, macro exits, and the global stationary mass.  No proposed
  Terminal-B cut is claimed because neither the width-12 band nor the
  separator incidence has a superpolynomial upper bound.
- No multicommodity paths or canonical normal form are used; path length and
  congestion are inapplicable.
- The exact matching transfer has at most `O(n^3)` height/area states over all
  times and admits the conservative bound `O(n^4)` arithmetic operations and
  `O(n^3)` memory.  Integer coefficients have polynomial bit length.
- The inherited support-Mobius/cut-join recurrence has the exact complexity
  stated in M38.  The new run through `N=14` took `93.23` seconds overall,
  with the `N=14` record taking `60.20` seconds, and validated the Hurwitz
  total and mountain coefficient exactly.
- The complete full-block reverse-action falsifier enumerated all
  `1,008,000` states of `F_5` in `40.23` seconds.  It found a lower-area
  `r=3,4,5` outcome for every nonminimum state even when disconnected targets
  were allowed.  At `N=4`, exact support-resolved checking also found a
  within-`F_4` descent for all `2784` nonminimum states.  These bounded facts
  do not prove a universal reverse action.
- The Lorentzian calculation used NumPy `1.26.4` only to locate the exact
  integer Hessian.  The inertia proof itself is exact and dependency-free.

## 4. Dependencies, with status

1. **PROVED HERE:** Theorems 1--4, including the prefix graphic-rank formula,
   exact area-change constants, complete boundary/separator reduction, exact
   Lorentzian counterexample, matching transfer, endpoint mismatch, and
   un-tilted matching moments.
2. **INHERITED PROVED:** M34 join-factor spanning tree, valley action and
   exact padded-`H_3` probability; M38 support-Mobius/cut-join recurrence,
   exact bottom/mountain coefficients, and adjacent-layer no-cliff;
   reversibility/stationarity of exact heat baths; qualitative irreducibility
   of `K`.
3. **CITED AND CONVENTION-CHECKED:** Enrica Duchi, Dominique Poulalhon, and
   Gilles Schaeffer, *Uniform random sampling of simple branched coverings of
   the sphere by itself*, SODA 2014: Proposition 2.1 (increasing maps),
   Theorem 3.3 (Hurwitz trees), and Proposition 4.1 (Cayley tree times a
   permutation).  Their reversed product convention is translated explicitly
   in Section 2.1.
4. **CITED DEFINITION:** Petter Branden and June Huh, *Lorentzian
   polynomials*, Annals of Mathematics 192 (2020), for the necessary
   quadratic Hessian-signature condition.  The concrete violation is proved
   directly from (2.3).
5. **EXACT FINITE ONLY:** connected area coefficients through `N=14`;
   reference transfer through `n=60`; fixed-path coefficients through `N=8`;
   full reverse-action checks at `N=3,4,5`.  These can falsify named universal
   statements but are not finite-to-universal proofs.
6. **EMPIRICAL/FLOATING ONLY:** normalized actual/reference density ratios and
   tilted-reference quartile locations.  Exact integer `G_n(a)` are used, but
   `q_n` normalization and comparisons use floating logarithms.
7. **UNRESOLVED:** any polynomial comparison between `H_N` and the tilted
   matching law, any universal first-quartile prefix-record theorem, and any
   superpolynomial separator-incidence upper bound.

## 5. First unproved standalone proposition

> **WEIGHTED DYCK QUARTILE-SHELL COEFFICIENT BOUND.**  For every `N>=6`, let
> `mu_N` be uniform on `F_N`.  There are universal `c>0,C<infinity` and an
> explicit feasible `q_N` such that
>
> ```text
> 1/4<=mu_N(Area<=q_N)<=1/2,
> H_N(q_N)/sum_(a<=q_N)H_N(a)>=cN^(-C).                            (5.1)
> ```

The natural explicit choice is the first conditional quartile.  The
first-quartile prefix-record statement (2.7) would prove (5.1) with
`cN^(-C)=1/(4L_N)`.  Alternatively, a polynomial local-limit/Radon theorem
for the actual integrated graphic-rank law, not merely for the reference
matching law, would suffice.

## 6. Strongest self-attack / failure mode

The graphic-rank identity is a representation, not an isoperimetric theorem.
The ordered support map is correlated with its edge labels by the increasing
map condition; it is not a fixed graph in a uniformly random edge order.
Therefore generic random-MST or uniform-matching anti-concentration cannot be
imported without a new comparison.

The endpoint-matched reference is especially vulnerable.  Matching the bottom
and mountain densities removes one exponential discrepancy, but it does not
control intermediate paths.  The bounded area-marginal density distortion
`1.4783` through `N=14` may grow superpolynomially.  The actual and reference
first-quartile areas already disagree at `N=13` (`108` versus `106`) and
`N=14` (`127` versus `125`), so equality of thresholds is exactly refuted.
The Lorentzian failure also rules out the cleanest complete-log-concavity
upgrade, including after any exponential area tilt.

Most importantly, even a superpolynomial failure of (5.1) would not establish
Terminal B.  Equation (1.6) shows two missing upper bounds: all width-12
`H_3,H_4,H_5` crossings, not only the exact top layer, and every local exit
from `F_N`.  A candidate bottleneck must make both the band mass and the
consecutive support-separator incidence small relative to the correctly
oriented global mass.  No such family is proved here.

## 7. Calibration results

- Odd `m` gives an empty bridge space; `m=0` and `N=2` even give singleton
  cases; `m=2,N>=3` is excluded and disconnected.  The scoped minimal macro
  uses even `m=2N-2` and `N>=3`.
- At `N=3,m=4`, global `Omega` has `27` words and four pure-Hurwitz
  components, while the connected minimal macro has `24` words.  The `r=4`
  update is the whole-word heat bath and is never removed from (1.1).
- At `N=4,m=4`, global `Omega` has `120` words and 13 pure-Hurwitz
  components; this is not the full-support minimal macro and no M44 theorem
  silently substitutes it.  At `N=4,m=6`, global `Omega` has `3936` words and
  17 pure-Hurwitz components, while `F_4` has exactly `2880` words.  The exact
  support-resolved reverse-action check reproduces the `F_4` area layers
  `96,528,720,1536`.
- The bottom path consists of adjacent doubled tree edges and has exact weight
  `n!N^(n-1)`; the mountain has weight `n!N^(2n-2)`.  Both are used in the
  reference audit rather than routed through as canonical hubs.
- Disjoint support components still have ordered factor interleavings.  The
  prefix products and the literal ordered cut/join transfer retain this
  ordering; no graph-only dynamics is substituted for `K`.
- No vertex-degree parity or edge-multiplicity parity invariant is used, and
  no length-two simulation claim is made.  The reverse-action diagnostic uses
  actual same-product `r=3,4,5` fibers.
- For a proposed lower threshold with `mu_N(A_q)<=1/2`, the exact global mass
  is `pi(A_q)=pi(F_N)mu_N(A_q)<=1/2`, so (2.2) has the correct smaller-side
  orientation.  For a Terminal-B upper bound, division by this same global
  mass cancels `pi(F_N)` in (1.6); neither stationary mass nor macro flow may
  be omitted.

## 8. Artifacts and exact reproduction commands

Owned directory:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-10/
  mission-M44-weighted-quartile-or-bottleneck/
```

Main artifacts:

```text
plan.md
checkpoint.md
report.md
lorentzian_path_falsifier.py
lorentzian-results.json
tilted_matching_reference.py
tilted-matching-results.json
full_block_descent_falsifier.py
full-block-descent-N3.json
full-block-descent-N4.json
full-block-descent-N5.json
actual-area-N14.json
```

Commands, from the repository root:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/lorentzian_path_falsifier.py \
  --input experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M38-weighted-dyck-shell/results-paths-N8.json \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/lorentzian-results.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M38-weighted-dyck-shell/weighted_dyck_recurrence.py \
  --max-n 14 --path-validation-max-n 2 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/actual-area-N14.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/tilted_matching_reference.py \
  --actual experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/actual-area-N14.json \
  --reference-max-n 60 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/tilted-matching-results.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/full_block_descent_falsifier.py \
  --N 4 --within-connected \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/full-block-descent-N4.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/full_block_descent_falsifier.py \
  --N 5 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-10/mission-M44-weighted-quartile-or-bottleneck/full-block-descent-N5.json
```

All runs are deterministic and use no seed.  The JSON records repository
commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, Python `3.12.3`, exact
commands, platform, and nonstandard dependencies where applicable.

## 9. Verdict

**OPEN AT A NAMED STEP: WEIGHTED DYCK QUARTILE-SHELL COEFFICIENT BOUND (5.1).**
