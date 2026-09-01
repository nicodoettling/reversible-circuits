# M58 final report: every join-tree-measurable minimal-macro cut has polynomial full-`K` escape

The rectangle problem admits a substantially stronger resolution.  No
profile geometry, monotonicity, or label symmetry is needed: for an arbitrary
set of labeled join trees, both placements of the entire nonminimal
complement have original-chain two-sided conductance at least `1/(24N^7)`.
The key is to record the deleted leaf's neighbor and count all valid
base-word/attachment pairs, dividing source collisions by at most `N`.

## 1. Exact claim, quantifiers, and conventions

Permutations compose as `(pq)(x)=p(q(x))`, and a word evaluates as
`t_1...t_m`.  For every `N>=4`, put `m=2N-2`.  Let `F_N` be the connected
full-support minimal identity macro in `Omega(N,m)`.  Its prefix cycle joins
form a labeled tree `T_J(w)` on `[N]`.

Let `mathcal A` be an **arbitrary** subset of the labeled trees on `[N]`.
It need not be invariant under relabeling and need not be related to the
family chosen at another value of `N`.  Define

```text
R_A={w in F_N:T_J(w) in mathcal A},
C_A=F_N minus R_A,
B_A=F_N^c union R_A,
B_C=F_N^c union C_A.                                 (1.1)
```

The exact kernel is

```text
K=(1/2)I
 +(1/6) sum_(s in {3,4,5})
      (1/(m-s+1)) sum_(i=1)^(m-s+1) H_(i,s),        (1.2)
```

where `H_(i,s)` is uniform on the exact same-product length-`s`
transposition fiber.  With uniform stationary law `pi`, let

```text
Phi_pm(B)=Q_K(B,B^c)/min{pi(B),pi(B^c)}.
```

**Theorem.**  Whenever the corresponding cut in (1.1) is nontrivial,

```text
Phi_pm(B_A),Phi_pm(B_C)
 >=1/[3Nm(N-1)^2(m-2)D_N]
 >=1/(24N^7),                                      (1.3)
D_N=(3N^2+N-12)/2.                                  (1.4)
```

Every fixed `(ell,b)` cell, bounded leaf/balance rectangle, arbitrary union
of such cells, diameter/centroid/degree-profile event, and arbitrary labeled
join-tree family is a special case.  The verdict is scoped to (1.3); it is
not Terminal A or Terminal B.

## 2. Full proof

### 2.1 Strand deletion with a recorded neighbor

The M49 leaf-strand theorem, accepted by a fresh independent referee, states
the following.  If `v` is a leaf of `T_J(w)` for `w in F_N`, erase `v` from
every prefix permutation.  Exactly two induced increments are identities.
Deleting them gives a word `z` in the minimal macro on label set
`[N] minus {v}`, and

```text
T_J(z)=T_J(w)-v.                                     (2.1)
```

For a fixed deleted label `v`, output word `z`, and two null positions, there
are at most `(N-1)^2` lifts.  Briefly, a lift is tracked by the insertion
coordinate of `v` in its current permutation cycle.  There are `N-1`
initial coordinates.  Projected support joins have forced lifts; descendants
created by projected cuts occupy distinct cycles, and minimality forbids
their later internal reunion, so one initial coordinate has at most `N-1`
descendants.  Fixing extra information can only shrink this fiber.

Let `u` be the unique neighbor of the leaf `v` in `T_J(w)`.  Recording `u`
in addition to `v,z`, and the null positions therefore leaves the same upper
bound `(N-1)^2`.

### 2.2 Valid attachment-pair sets

For each `v in [N]`, let `F_(N-1)^(v)` denote minimal connected identity
words on the label set `[N] minus {v}`, of length `m-2`.  Define

```text
P_v(mathcal A)
 ={(z,u): z in F_(N-1)^(v), u in [N] minus {v},
           T_J(z)+edge{v,u} in mathcal A}.           (2.2)
```

Choose one tree leaf deterministically from every `w in R_A` and apply
section 2.1.  Its tuple `(v,z,u)` belongs to `P_v(mathcal A)`.  Once `v,z,u`
and the two null positions are fixed, at most `(N-1)^2` original words map to
that tuple.  Summing all labels, valid pairs, and the `binom(m,2)` null-position
pairs gives

```text
|R_A|
 <=binom(m,2)(N-1)^2 sum_(v=1)^N |P_v(mathcal A)|.   (2.3)
```

This is where recording the old neighbor removes every rectangle-specific
insertion problem.  The deleted word itself certifies that the recorded pair
is valid.  No distributional claim about random trees is used.

### 2.3 Reverse sources and exact collision multiplicity

Conversely, take any `(z,u) in P_v(mathcal A)`.  Insert the adjacent square

```text
(v,u),(v,u)                                          (2.4)
```

into any one of the `m-1` gaps of `z`.  Before the square, `v` is fixed
because every base factor avoids it.  The first copy of `(v,u)` is therefore
a prefix cycle join and the second copy cuts back to the old prefix
permutation.  All later prefixes agree with the base.  Hence the resulting
word `x` lies in `F_N` and

```text
T_J(x)=T_J(z)+edge{v,u} in mathcal A.                (2.5)
```

The multiset of generating quadruples `(v,z,u,gap)` has size

```text
(m-1) sum_v |P_v(mathcal A)|.                        (2.6)
```

For a fixed `v`, a generated source has at most one representation.  Indeed,
the base avoids `v`, so the source contains exactly two `v`-incident factors;
they are adjacent, reveal `u` and the gap, and their deletion recovers `z`.
A source can be represented using several different leaf labels, but there
are only `N` labels.  Thus the map from generating quadruples to distinct
source words has multiplicity at most `N`.  If `S_A` is its image,

```text
|S_A| >=(m-1)/N sum_v |P_v(mathcal A)|.              (2.7)
```

If `R_A` is nonempty, the pair sum is nonzero by the forward deletion map.
Combining (2.3) and (2.7) yields

```text
|S_A|/|R_A|
 >=(m-1)/[N binom(m,2)(N-1)^2]
 =2/[Nm(N-1)^2].                                     (2.8)
```

Apply precisely the same construction to the complementary labeled-tree
family `mathcal A^c`.  It supplies a source set `S_C subset C_A` with

```text
|S_C|/|C_A|>=2/[Nm(N-1)^2]                           (2.9)
```

whenever `C_A` is nonempty.

### 2.4 One exact `H3` exit per distinct source

A source may have several generating labels.  Choose one generating
quadruple deterministically for each **distinct** source before assigning a
transition; this prevents any flow overcounting.

For its chosen marked square, pad by a neighboring base transposition `a`,
using the right neighbor unless the square occupies the final gap.  Choose a
fixed transposition `f` on labels other than the marked `v`; this exists
because `N-1>=3`.  Specify

```text
((vu),(vu),a)->(f,f,a),
(a,(vu),(vu))->(a,f,f).                              (2.10)
```

Both ordered block products equal `a`.  The target omits `v`, is still a
global identity word, and lies in `F_N^c`.

The exact length-three transposition fiber over a transposition has size

```text
D_N=binom(N,2)+6(N-2)+2binom(N-2,2)
   =(3N^2+N-12)/2.                                   (2.11)
```

Half-laziness, uniform choice among all three block sizes, all `m-2` triple
windows, and the exact conditional heat bath give the specified outcome
probability

```text
p_N=(1/2)(1/3)(1/(m-2))(1/D_N)
   =1/[6(m-2)D_N].                                   (2.12)
```

### 2.5 Literal global orientation and complete flow

Let `O_N=|Omega(N,m)|`, `a=|R_A|`, and `c=|C_A|`.  Exact masses are

```text
pi(B_A)=1-c/O_N,       pi(B_A^c)=c/O_N,
pi(B_C)=1-a/O_N,       pi(B_C^c)=a/O_N.              (2.13)
```

For `B_A`, sources `S_C` move from the complement into
`F_N^c subset B_A`; for `B_C`, sources `S_A` do the same.  Uniform
heat-bath reversibility permits either direction of the stationary boundary
flow.  Since the minimum of the two global masses is at most the displayed
profile-side mass, (2.8)--(2.12) give the exact first inequality in (1.3).

The literal boundary decomposes into `H3,H4,H5`, and within/macro terms.  The
chosen outcomes form a subset of the `H3` macro term.  Every other outcome
and all `H4,H5` contributions remain nonnegative; they are discarded only
from this lower bound.  No upper-flow Terminal-B claim is made.

Finally `m,m-2<=2N`, `(N-1)^2<=N^2`, and `D_N<=2N^2`, so the exact
denominator in (1.3) is at most `24N^7`.

## 3. Probability, runtime, path length, and congestion

- Exact transition probability per chosen source: `1/[6(m-2)D_N]`.
- Source multiset collision: at most one representation per label and at
  most `N` total; this is the only new multiplicity factor.
- Certified distinct-source fraction: `2/[Nm(N-1)^2]`.
- Their product is exactly the first bound in (1.3), with no hidden kernel
  factor.
- For a rectangle, cell, or explicit tree statistic, direct prefix/join-tree
  construction and membership testing cost `O(Nm)` plus the statistic's own
  evaluation cost.  An arbitrary family `mathcal A` is a mathematical cut
  and need not have an efficient membership oracle.
- Each source uses one actual `K` edge.  There is no multistep path, canonical
  hub, or congestion claim.
- The exact `H3` fiber has `D_N=O(N^2)` elements and is polynomially
  sampleable; no new sampler is required.

## 4. Dependency statuses

1. **PROVED HERE:** valid-pair encoding, arbitrary-label pair sum, exact
   source collision bound `N`, pair/source ratios, global orientation, and
   theorem (1.3).
2. **PROVED / FRESH-REFEREED:** M49 strand deletion, join-tree deletion, and
   fixed-position lift multiplicity `(N-1)^2`; the required statement is
   restated in section 2.1.
3. **PROVED INHERITED:** exact same-product heat-bath reversibility and
   stationarity.
4. **PROVED BY DIRECT ENUMERATION:** triple-fiber formula (2.11).
5. **EXACT FINITE / NOT REUSED AS PROOF:** M49's `N=4,5` strand audits and
   M53/M55/M57 profile checks calibrate special cases.  The arbitrary-family
   theorem is the universal counting argument above.
6. **CONDITIONAL:** none.
7. **EMPIRICAL:** none.

## 5. First unproved standalone proposition

> **JOIN-TREE-FIBER MEAN-LIFT.**  There are universal constants `c,C>0`
> such that for every `N>=4`, `m=2N-2`, and every function `f:F_N->R` with
> zero conditional mean on each join-tree fiber,
>
> ```text
> sum_T pi(T) Var_(pi(.|T))(f)
>   <=c^(-1) N^C E_K(f,f),
> ```
>
> where `E_K` is the full original-chain Dirichlet form after extending `f`
> by zero or an explicitly audited mean lift off `F_N`.

The extension convention and off-macro mean term must be fixed in a proof.
This proposition targets precisely the fluctuations invisible to every
join-tree-saturated cut covered by (1.3).

## 6. Strongest self-attack

The theorem bundles every ordered word with the same join tree.  It gives no
flow bound for a cut that selects half of one join-tree fiber by prefix order,
cut chronology, Hurwitz position, or another word-level statistic.  It also
does not expand `F_N^c`, control surplus lengths, or produce a Poincare
inequality from conductance of this restricted family.  The strand map is a
counting device rather than a variance intertwiner.  Hence even this broad
anti-bottleneck theorem is nonterminal.

## 7. Calibration suite

- Odd `m` gives empty `Omega`; `m=0` and `N=2` are singletons; excluded
  `m=2,N>=3` is not used.
- `S_3,m=4` has 27 words and four pure-Hurwitz components; `R_m={3,4}` and
  `H4` is whole-word.  `S_4,m=4` has 120/13.  The theorem starts at
  `N=4,m=6`, where `R_m={3,4,5}` and normalization (1.2) is exact.
- At `S_4,m=6`, `|Omega|=3936`, `|F_4|=2880`, and there are 16 labeled
  trees.  The theorem covers each of their `2^16` unions, including unions
  mixing path and star fibers with arbitrary labels.  Exact orientation is
  still (2.13), not conditional mass in `F_4`.
- M49 exact checks give maximum fixed-position strand fibers `8<=9` at
  `N=4` and `13<=16` at `N=5`, calibrating the only imported multiplicity.
- Paths, stars, balanced trees, doubled-tree minimal words, singleton witness
  sides, and every tree shape are included by arbitrary `mathcal A`.
- Each source is a literal ordered identity word.  No color commutation,
  graph-only dynamics, degree parity characterization, or length-two
  simulation is substituted.
- A fixed canonical hub is absent: sources are spread over all valid base
  words, attachments, labels, and gaps.
- `H4,H5` and all unused `H3` flow are retained as nonnegative terms.

## 8. Artifacts and reproducibility

Owned proof artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-13/mission-M58-macro-closed-profile-rectangle-redteam/
  plan.md
  checkpoint.md
  report.md
```

Repository commit at freeze: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

No new computation was needed: the valid-pair encoding and collision bound
are exact symbolic arguments.  The imported bounded strand falsifiers are
documented under

```text
experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M49-symmetric-branch-balance/
```

and were rerun by its fresh referee.  There is no random seed, nonstandard
dependency, bulk output, or bytecode cache for M58.

## 9. Verdict

**PROVED.**

This verdict proves the stronger theorem (1.3) for both macro-closed
placements of every arbitrary labeled join-tree family, and therefore for
all assigned profile rectangles and fixed cells.  It is nonterminal.
