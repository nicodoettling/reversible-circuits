# M78 final report: exact positive elimination and a depth-two obstruction family

Date: 2026-08-12.  Recorded repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact claim, convention, and scoped outcome

Permutations compose as `(pq)(x)=p(q(x))`, tuple products are evaluated
left-to-right, and the right Hurwitz generator is

```text
R_i(...,a,b,...)=(...,b,bab,...).
```

The global target is uniform on `Omega(N,m)`.  The literal chain in the
background is M75's lazy exact same-product `{3,4,5}` heat bath at
`N>=5,m=2N-2`; this report concerns only the surviving two-component
positive-braid row lemma.  In a two-component minimal ambient macro the
component genera sum to one.  Hence exactly one component has genus one; on
`d` vertices its factor length is `k=2d`.  Factors from the genus-zero
component merely interleave and commute with this component, so selecting a
uniform ambient order induces a uniform relative order on these `k` labels.

This report has four separate outcomes.

1. **PROVED:** M75's canonical positive permutation braid is exactly a
   uniform random elimination process, with an explicit conjugation formula.
   One successful ordered prefix of length `r` gives endpoint marked
   probability at least `1/(k)_r>=1/(m)_r`.
2. **REFUTED:** depth zero, depth one, and depth two are not universal.
   Depth zero fails at `d=4`; depth one fails on an exact `K_(4,4)` word;
   an explicit infinite `Z_L^2` voltage-lift family has no safe prefix through
   depth two for every `L>=2`.
3. **REFUTED:** a short face of the chronological factor-order map need not
   give a connected deletion certificate.  On the `K_(4,4)` word all eight
   facial 4-cycles create collisions in some order, but no facial order is
   safe.
4. **UNRESOLVED:** the full simple-positive-braid worst-row lower bound is
   neither proved nor refuted.  The first open step is a total-prefix
   probability bound for the voltage family, not merely a lower bound on its
   first possible hit depth.

No Terminal-A or Terminal-B claim is made.  In particular, no stationary cut
or spectral-gap upper bound for the original heat-bath chain is proved.

## 2. Full argument

### 2.1 Canonical positive braid as elimination

Fix original labels `0,...,k-1`.  M75's positive lift `beta_pi` repeatedly
bubbles the next requested original label to the left.  Suppose that label
currently lies at residual position `j`, with current transposition `b`.
Applying `R(a,b)=(b,bab)` successively outputs `b`, deletes its residual
position, conjugates every current factor strictly to its left by `b`, and
leaves every factor to its right unchanged:

```text
(a_1,...,a_j,b,a_(j+2),...)
 -> output b, residual
(b a_1 b,...,b a_j b,a_(j+2),...).                (2.1)
```

Therefore, after previously selected current outputs `b_1,...,b_q`, an
unselected original factor `t_j` has current value

```text
G_j^(-1) t_j G_j,
G_j=product, in selection order, of b_s with original label j_s>j.
                                                               (2.2)
```

This follows by induction: selecting a label to the right conjugates the
current value once; selecting one to the left does not affect it.  Since the
`b_s` are transpositions, reversing their order changes the equivalent
conjugation orientation, so (2.2) also fixes the convention ambiguity.

Call an ordered original-label prefix of length `q+2` **safe at depth q** if
the last two current outputs are equal and deleting them leaves the word
formed by the first `q` outputs followed by the current residual tuple
connected.  Once emitted, the equal pair is the rightmost prefix pair.
Later eliminations act only on the residual suffix, so it remains adjacent.
Those later Hurwitz moves preserve the weighted support component of the
word with the pair deleted.  Thus a safe prefix yields a marked endpoint.
Conversely, any marked endpoint square was emitted at such a prefix.

Under uniform `pi in S_k`, every ordered prefix of length `r=q+2` occurs with
probability exactly

```text
1/(k)_r,  (k)_r=k(k-1)...(k-r+1).                  (2.3)
```

Consequently, one universal constant-length safe prefix per source would
prove an inverse-polynomial row bound.  This report refutes all lengths up to
four.

### 2.2 Exact finite depth obstructions

The deterministic audit exhausts every connected genus-one identity word for
`d=3,k=6` and `d=4,k=8`:

| component | exact word count | first safe depth |
|---|---:|---|
| `d=3,k=6` | 240 | all 240 at depth 0 |
| `d=4,k=8` | 131040 | 130992 at depth 0; 48 at depth 1 |

Thus depth zero is nonuniversal.

On `d=5,k=10`, the all-distinct connected identity word

```text
(01)(02)(03)(12)(14)(24)(04)(23)(13)(34)           (2.4)
```

has zero depth-zero prefixes and exactly 14 safe ordered depth-one prefixes.
An exact absorbing elimination recursion independently counts

```text
1569216 / 10! = 227/525 approximately 0.432381
```

full orders with some marked prefix.  This is positive finite calibration,
not an asymptotic theorem.

On labels `0,...,7`, take the all-distinct word

```text
(35)(34)(15)(25)(16)(04)(37)(27)
(05)(36)(14)(17)(06)(24)(26)(07).                 (2.5)
```

It uses every edge of `K_(4,4)` once, is connected, and evaluates to identity.
Its exact safe-prefix counts are

```text
depth 0: 0,   depth 1: 0,   depth 2: 76.           (2.6)
```

The depth-one zero has a short direct proof.  After selecting one factor
`b`, any equality among remaining current factors must be either an original
repeat, or a cross-boundary identity `bab=c`.  The word is all-distinct.  For
distinct transpositions `a,b,c`, `bab=c` holds exactly when their edges form
a triangle.  The support `K_(4,4)` is triangle-free.

### 2.3 Why the short-face proof fails

The chronological rotation system of (2.5) has eight faces, all of length
four.  Across all 192 facial orders, 32 give equal last current factors, but
zero leave connected support after deletion.  For example, face
`[0,2,4,9]` in order `(2,4,0,9)` emits

```text
(15),(16),(36),(36),                               (2.7)
```

but deletion isolates vertex 3.  A safe nonfacial support 4-cycle is order
`(1,2,0,10)`, which emits

```text
(34),(15),(14),(14)                                (2.8)
```

and whose residual support is connected.  Hence cycle algebra explains the
collision, but face length alone does not prove nonseparating deletion.

### 2.4 An explicit infinite depth-two obstruction

Write the sixteen base edges in the order (2.5) and assign integer voltages

```text
x=(-1,-1,-1,0,0,0,0,1,0,0,0,0,0,0,0,0),
y=(-1, 0, 0,0,1,1,0,0,0,0,1,0,0,0,0,0).          (2.9)
```

For `L>=2`, replace every base vertex `a` by `(a,r,s)` with
`(r,s) in Z_L^2`.  Replace an oriented base edge `a<b` at factor index `i`
by all `L^2` edges

```text
(a,r,s) -- (b,r+x_i,s+y_i),                        (2.10)
```

listed consecutively in lexicographic `(i,r,s)` order.  Call the resulting
word `W_L`.  It has

```text
d_L=8L^2,  k_L=16L^2=2d_L.                         (2.11)
```

The following statements hold for every `L>=2`.

**Identity.**  In the base word, the token trajectories are:

```text
0: +5,-10,+11,-15       4: -1,+6,-7,+13
1: +2,-3,+7,-11         5: -0,+1,-5,+8
2: +3,-8,+12,-14        6: -4,+10,-13,+14
3: +0,-2,+4,-9          7: -6,+9,-12,+15.          (2.12)
```

For each row, both signed voltage sums from (2.9) are zero.  Because each
base factor is replaced by the full matching between fibers, every lifted
token follows its base trajectory and returns to the same fiber coordinate.
Thus `W_L` evaluates to identity.

**Connected simple bipartite support.**  The lift is simple and bipartite by
construction.  The base support is connected.  It has closed walks of
voltages `(-1,0)` and `(0,1)`, for example the base 4-cycles

```text
0-7-2-6-0,    indices (15,7,14,12), voltage (-1,0),
0-7-1-6-0,    indices (15,11,4,12), voltage (0,1). (2.13)
```

These generate `Z_L^2`, so the lift is connected.  Therefore `W_L` is a
connected genus-one identity word.

**No depth 0 or 1.**  The support is simple and bipartite.  The same repeat /
triangle argument used for (2.5) applies verbatim.

**No depth 2.**  Equality after four selected factors is a length-four
transposition relation; with simple triangle-free support it is supported on
a support 4-cycle.  Every support 4-cycle in this voltage lift has zero
voltage and is a lift of a contractible base facial 4-cycle.  Its collision
order deletes the two incident edges needed to attach one corner's fiber
vertex, exactly as in (2.7); hence the residual support is disconnected.
Equivalently, the compact exact enumeration verifies the finite quotient
pattern and the local proof is independent of `L`.  The literal exact audits
give:

| `L` | `d_L` | support 4-cycles | collision orders | safe orders |
|---:|---:|---:|---:|---:|
| 2 | 32 | 32 | 128 | 0 |
| 3 | 72 | 72 | 288 | 0 |

The all-`L` conclusion uses the displayed voltage construction and local
4-cycle classification; the two rows are exact independent finite checks.
Thus no universal safe prefix of length at most four exists.

This family is not a row-probability counterexample.  A longer prefix may
still hit with substantial probability.  Fixed-seed Monte Carlo found zero
hits in 10000 orders at `L=2` and 2000 at `L=3`, versus 1192/20000 for the
base `L=1`; that is only an empirical adversarial signal.  It is not an
upper bound, and zero observed hits is not a zero-row theorem.

## 3. Probability, runtime, path, and congestion accounting

| item | exact accounting | status |
|---|---:|---|
| uniform relative order on genus-one labels | `1/k!` | proved despite ambient interleaving |
| one fixed safe prefix of length `r` | `1/(k)_r >=1/(m)_r` | proved |
| expected canonical braid length on ambient word | `m(m-1)/4` | inherited M75/M77 |
| marked endpoint coarea load | endpoint load `<=1` per braid word | inherited M75/M77 |
| `d=5` exact total hit row | `1569216/10!` | exact finite fact |
| base `K4,4` depth-two prefixes | `76/(16)_4` lower contribution | exact finite fact |
| `W_L` safe depths `0,1,2` | none | proved for every `L>=2` |
| `W_L` total endpoint hit probability | unknown | first missing bound |

The exact small audit is deterministic standard-library Python and takes
about five seconds.  The voltage checks for `L=2,3` take below one second.
The prior naive exact full-row recursion for `K4,4` was stopped after about
29 minutes with no output; no numerical claim is derived from it.  The
factorial support of the braid law remains irrelevant to M75's coarea load if
a row lower bound can be proved.

## 4. Dependencies and claim status

| claim/input | status here | dependence |
|---|---|---|
| M75 randomized endpoint coarea theorem | inherited accepted by M77 | converts row lower bound to partial-macro flow |
| M75 post-certificate null push | inherited accepted by M77 | used after a marked endpoint exists |
| canonical braid = elimination | proved | literal bubble-sort/Hurwitz algebra |
| prefix probability `1/(k)_r` | proved | uniform order only |
| `d=3,4`, N5, K4,4 counts | exact finite facts | exhaustive scripts |
| short facial cycle is safe | refuted | exact K4,4 witness |
| universal depth `<=2` | refuted by `W_L` | explicit voltage construction |
| simple-positive-braid row lower bound | unresolved | needs all-prefix probability |
| full exterior flow / gap / mixing | unresolved | not implied |

No literature theorem is invoked.  The map language is used only as a compact
description of the explicit rotation/voltage construction; every promoted
claim has a direct permutation or graph proof above.

## 5. First unproved standalone step

The exact next lemma is:

> **VOLTAGE-LIFT TOTAL PREFIX INCIDENCE.**  For the explicit `W_L`, determine
> or sharply bound
>
> ```text
> eta_L=Pr_(pi uniform in S_(16L^2))
>   [some canonical-elimination prefix is a connected deletable square].
> ```
>
> Either prove `eta_L >= (L^2)^(-C)` for an absolute `C`, or prove an
> upper bound `eta_L <= exp(-Omega(f(L)))` with `f(L)/log L -> infinity`.

This is strictly narrower than the original row lemma: the source family,
factor order, support graph, voltage coordinates, and exact elimination law
are all explicit.  A lower bound would rescue the canonical law against its
strongest current adversary.  A superpolynomial upper bound would refute the
canonical simple-braid row lemma, though it still would not by itself prove a
Terminal-B bottleneck for the original heat-bath chain.

An auxiliary algebraic obligation is to classify every equal-output prefix
as a closed walk with its voltage/homology and characterize residual
connectivity after deleting the final pair.  Minimum nonseparating cycle
length alone is insufficient: long prefixes may carry high total mass.

## 6. Strongest self-attack

1. The all-`L` depth-two proof depends on the direct classification of
   four-factor transposition relations in a simple bipartite support.  The
   `L=2,3` exhaustive checks support, but do not replace, that elementary
   classification.
2. Large first-hit depth does not imply small endpoint hit probability.  A
   random order has many possible prefixes, and later conjugations create
   edges absent from the original support.
3. The zero-hit Monte Carlo observations are not proof.  Thin probabilities
   below the trial resolution remain possible, as do rare but numerous long
   certificates.
4. The finite base word has total hit probability about six percent by Monte
   Carlo despite only 76 depth-two ordered prefixes; later hits dominate.
5. A counterexample to this canonical law would not rule out another
   state-independent bijective Hurwitz-word law and would not establish a
   full-chain stationary bottleneck.
6. The voltage family has ambient parameters `N=d_L+1,m=2N-2` after adding
   one isolated label, so it lies in the two-component scope.  The isolated
   genus-zero component has length zero; if a formulation insists on two
   nontrivial components, an independent doubled edge can be added and the
   ambient arithmetic adjusted, but that variant has not been audited here.

## 7. Boundary cases and calibrations

- Odd `m` is empty by sign; `m=0,m=2,N=2` do not carry the genus-one
  two-component geometry.
- The theorem target starts at ambient `N>=5`; `d=3,4` are exact structural
  calibrations, not ambient terminal cases.
- For (2.5), the explicit safe prefix `(1,2,0,10)` has current outputs
  `(34),(15),(14),(14)` and connected residual support.
- For `W_2`, exact enumeration of all 32 support 4-cycles finds 128 collision
  orders and zero safe orders.  Exact enumeration of all 64 support 6-cycles
  likewise found 768 collision orders and zero safe orders, but that latter
  finite result is exploratory and not needed for the proved depth-two claim.

## 8. Artifacts and reproduction

All owned artifacts are in this mission directory:

```text
plan.md
checkpoint.md
exact_elimination_audit.py
exact-results.json
voltage_lift_audit.py
voltage-results.json
monte-carlo-prefix-results.json
report.md
```

Exact commands from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M78-positive-braid-row-bound/exact_elimination_audit.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M78-positive-braid-row-bound/exact-results.json

PYTHONDONTWRITEBYTECODE=1 python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M78-positive-braid-row-bound/voltage_lift_audit.py \
  --L 2 3 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-16/mission-M78-positive-braid-row-bound/voltage-results.json
```

Python 3.12.3; exact runs use seed `null`; Monte Carlo uses seed `7808`;
nonstandard dependencies `{}`.  Every computational claim is labeled exact
or empirical in the machine-readable outputs.

## 9. Verdict

**OPEN AT ONE NAMED STEP: VOLTAGE-LIFT TOTAL PREFIX INCIDENCE.**

Within that nonterminal verdict, the canonical elimination formula is proved,
all constant-depth prefix-existence proofs through depth two are refuted by
an explicit infinite family, and the tempting short-face connectivity lemma
is refuted exactly.  The M75 row lemma itself remains unresolved because no
upper or lower bound is yet known for the total long-prefix probability.
