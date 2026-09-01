# M127 final report: DPS fixed-braid intertwining

Date: 2026-08-13 UTC.  Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — decision and exact scope

```text
FINAL VERDICT: REJECT THE FIXED-BRAID INTERTWINING PROPOSITION.
PROVED: adjacent-value DPS edits descend to involutions on physical Z_d.
REFUTED at d=3: one source-independent signed Hurwitz word implements an edit.
EXACT FINITE at d=3: five fixed schedules are necessary and sufficient.
ROOTED PRODUCT LOCAL COMPARISON AND EVERY GAP CLAIM REMAIN UNRESOLVED.
```

The tested proposition allowed `beta_(d,i)` to depend on rank `d` and
adjacent value index `i`, but not on the Cayley tree, permutation coordinate,
root, or physical source.  A two-source generated-subgroup invariant refutes
it for every adjacent index at `d=3` (and independently at `d=4`), with no
bound on braid length.

```text
candidate                 | fixed braid for a whole DPS adjacent-value action
claimed target            | uniform rooted minimal identity sector Z_d
identity ok               | exact d=3,4; Hurwitz/DPS constructions preserve identity
crosses Hurwitz components| not applicable; one connected minimal identity orbit
exact diagnostics         | complete DPS roots/edits; pair subgroup; d=3 action image/cover
verdict                    | reject fixed braid; retain descent and source-dependent routes
```

## Field 2 — target, convention, kernel, and dependencies

The auxiliary target is uniform on

```text
Z_d={w=(t_1,...,t_(2d-2)):t_1...t_(2d-2)=id,
                              support(w) connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  The signed actions are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

The physical auxiliary kernel, not analyzed spectrally here, is

```text
P_(0,d)=I/2+[1/(4(2d-3))]sum_j(R_j+R_j^(-1)).
```

Accepted inputs are M112/M119's DPS bijections

```text
Z_d <-> unrooted Hurwitz trees,
rooted Z_d <-> Cayley_d x S_(2d-2),
```

and M122/M126 only for the warning that a structured square-prefix family has
a fixed braid while all-edge congestion remains open.  This mission imports
no predecessor code or result file and uses no new external theorem.

## Field 3 — universal root-fiber descent

Let `F(T,pi)` be the accepted rooted DPS map and let `s_i pi` swap the values
`i,i+1`.  Replacing `pi` by `s_i pi` simply swaps those two global edge labels
of the rooted Hurwitz tree.  Edge relabeling commutes with forgetting the
white root.  The unrooted DPS bijection therefore proves a well-defined
involution

```text
tau_i:Z_d->Z_d,        tau_i(F(T,pi))=F(T,s_i pi).       (3.1)
```

This is **PROVED for every `d>=2` and every adjacent index**.  Thus the
failure below is not a collision among the exact `d` root preimages.  An
arbitrary source-independent permutation `tau_i` of the state space exists;
it is not one action in the signed Hurwitz image.

The independent exact implementation confirms zero root-fiber target
collisions in all complete small cases:

| `d` | rooted pairs | `|Z_d|` | root fiber | adjacent indices | collisions/index |
|---:|---:|---:|---:|---:|---:|
| 3 | 72 | 24 | 3 | 3 | 0 |
| 4 | 11,520 | 2,880 | 4 | 5 | 0 |

## Field 4 — paired-source action invariant

For two source words `x,y in G^m`, package their factors as one word in the
direct product:

```text
((x_1,y_1),...,(x_m,y_m)) in (G x G)^m.
```

Applying the same signed Hurwitz word to `x` and `y` is exactly the ordinary
Hurwitz action on this direct-product tuple.  Replacing adjacent factors
`(a,b)` by `(b,b^(-1)ab)` preserves the subgroup they generate, and the
inverse replacement recovers `a`.  Hence every common action word preserves

```text
< (x_1,y_1),...,(x_m,y_m) > <= G x G                 (4.1)
```

as a literal subgroup.  This **PROVED** invariant tests fixed words of
arbitrary length, not only a bounded BFS radius.

## Field 5 — exact `d=3` fixed-braid counterexample

At `d=3`, use the Cayley star `T={{1,2},{1,3}}`, rooted at `y_3`, and adjacent
index `i=3`.  The independent DPS closure gives

```text
pi_A=(3,4,1,2): x =((12),(12),(13),(13)),
pi_B=(1,2,4,3): y =((12),(13),(12),(23)),

s_3 pi_A=(4,3,1,2): x'=((23),(23),(13),(13)),
s_3 pi_B=(1,2,3,4): y'=((13),(13),(12),(12)).          (5.1)
```

Writing `A=(12),B=(13),C=(23)`, the source coordinate pairs

```text
(A,A),(A,B),(B,A),(B,C)
```

generate the parity-diagonal subgroup

```text
{(p,q):sgn(p)=sgn(q)} <= S_3 x S_3,
```

of order 18.  Indeed, products with `(A,A)` give nontrivial 3-cycles in
each separate coordinate, hence `A_3 x A_3`, and `(A,A)` supplies the odd
coset.  The target pairs are only `(C,B)` and `(B,A)`.  If `rho=(123)`, then
`rho C rho^(-1)=B` and `rho B rho^(-1)=A`, so they generate the graph of
conjugation by `rho`, of order 6.  Equation (4.1) forbids a common braid.

Therefore the fixed-braid proposition is **REFUTED at `d=3,i=3`**.  The raw
checker finds analogous subgroup-order contradictions for all three indices
at `d=3` and all five at `d=4`:

| `d` | adjacent indices | source/target subgroup orders |
|---:|---|---|
| 3 | `1,2,3` | `18 -> 6` for each |
| 4 | `1,2,3,4` | `24 -> 288` for each |
| 4 | `5` | `288 -> 24` |

## Field 6 — complete `d=3` action image

The checker builds all signed generator action tables on the 24 physical
words of `Z_3`, then closes their generated permutation group exactly.  The
action image has order `216`.  Each of the three descended involutions
`tau_i` is a bijection and an involution but is absent from this image.

This is an independent finite confirmation of Field 5.  The subgroup proof,
not the finite group closure, establishes the no-fixed-word conclusion.
At `d=4`, the physical orbit from one word has all 2,880 states, but the full
permutation action image is intentionally not enumerated; the two-source
invariant already decides the proposition.

The boundary case `d=2` has singleton `Z_2`; its only adjacent edit acts
trivially and the empty word works.

## Field 7 — smallest recovered schedule metadata and root cost

For fixed `i` and braid action `b`, define

```text
A_i(b)={w in Z_3:b(w)=tau_i(w)}.
```

A `q`-class fixed-schedule cover is a list of `q` actions whose agreement
sets cover `Z_3`; a source is assigned to one covering action, and the class
index selects its schedule.  Complete enumeration of all 216 action-image
elements and exact union DP proves, for every `i=1,2,3`,

```text
max_b |A_i(b)|=6,       minimum schedule classes=5.      (7.1)
```

There are 23 distinct nonempty agreement masks.  The exact numbers of
reachable coverage masks with zero through five schedules are

```text
1, 23, 206, 811, 1640, 2021,
```

and the full 24-source mask first appears at five.  The JSON stores one
minimum cover for each index, explicit disjoint source assignments, and
schedules of maximum lengths `3,4,5` for indices `1,2,3`, respectively.
Every recorded endpoint is re-evaluated directly.

This is **EXACT FINITE ONLY**.  It is the minimum alphabet cardinality among
metadata that merely selects one fixed schedule at `d=3`; it is not a local
descriptor or an asymptotic upper bound.  Conditional on index, schedule
class, and scheduled time, prefix inversion recovers the physical source
uniquely.  Recovering the rooted ideal source still has the exact `d` root
possibilities; deterministic tracking in the spectrum-preserving lift retains
the factor-`d` root cost audited by M122/M126.

## Field 8 — computation, artifacts, and hygiene

The exact command is

```text
python3 -B fixed_braid_audit.py --d 3 4 --action-table-d 3 4 \
  --output fixed_braid_results.json
```

Python is `3.12.3`; dependencies are `{}`; the experiment is deterministic
with `seed=null`.  The final run took `4.918109367135912` seconds.  It checks
every rooted DPS coordinate, identity, connected support, exact root-fiber
size, every adjacent edit, the first subgroup obstruction per index, signed
generator bijectivity/orbit size, complete `d=3` action-image closure, exact
set-cover minimality, and every selected schedule endpoint.

Owned artifacts are `plan.md`, `checkpoint.md`, `fixed_braid_obstruction.md`,
`fixed_braid_audit.py`, `fixed_braid_results.json`, this report,
`freeze_manifest.md`, and `SHA256SUMS`.  No predecessor, coordinator,
manuscript, project skill, or file outside this mission directory is edited.

## Field 9 — final verdict and open obligations

```text
REJECT FIXED-BRAID INTERTWINING.
KEEP THE UNIVERSAL UNROOTED DESCENT AND THE PAIRED-SOURCE INVARIANT.
KEEP THE FIVE-CLASS RESULT AS EXACT FINITE ONLY.
```

The obstruction forces a general adjacent-value comparison to use genuinely
source-dependent paths or randomized flow.  It does **not** imply many route
descriptors, high congestion, or a small physical gap asymptotically.

The sharp surviving adjacent-coordinate lemma is **ADJACENT-VALUE POLYNOMIAL
SCHEDULE COVER**: cover `Z_d`, for each `i`, by `d^O(1)` agreement sets of
fixed signed braid words of length `d^O(1)`.  With a deterministic class
assignment, prefix inversion and the exact factor-`d` root quotient would
give polynomial descriptor load for the adjacent-value demands.  This lemma
is **UNRESOLVED**; the five-class `d=3` cover is finite only.

ROOTED PRODUCT LOCAL COMPARISON still requires polynomial path length and
total stationary edge load for all adjacent-value and UST basis-exchange
demands, including the root quotient.

No all-edge congestion bound, `gap(P_(0,d))`, arbitrary-product `Gamma_0`
bound, original lazy exact `{3,4,5}` heat-bath gap, Terminal A, or Terminal B
is proved or refuted here.
