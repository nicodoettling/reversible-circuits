# M128 fresh referee report on frozen M123

Date: 2026-08-13 UTC.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — decision, scope, and numbered objections

```text
ACCEPT M123'S EXPLICITLY UNRESTRICTED THEOREM AND AUXILIARY IDENTITIES,
WITH A REQUIRED CENTERING SCOPE SUPPLEMENT.
Material numbered objections: none.
```

M123 correctly refutes the universal canonical-basin analysis-frame bound on
all of `L2(rho)` at local rank `s=5`, proves the complete success-history mass
and signed two-copy identities, and refutes the unique-category and extra-
alpha shortcuts.  Its report explicitly says that the rank-five coefficient
vector is arbitrary and need not be an actual contextual function, so it does
not claim that its witness is centered.

The necessary supplement is that the displayed `s=5` witness has nonzero
mean.  The centered generic frame remains bounded through `s=5`, but fails at
`s=6`; a centered indicator witness fails at `s=8`.  These append-only
supplements strengthen the same proof-route refutation without changing
M123's verdict.  They still do not refute the all-suffix contraction.

## Field 2 — frozen provenance, target, convention, and operator

The frozen M123 `SHA256SUMS` verified completely before its artifacts were
used.  Assigned payload hashes independently match:

| frozen artifact | observed SHA-256 |
|---|---|
| `report.md` | `05a65a8f6111029a93a1c06e1dc014579ae013ff3d0ccaa356050189437afb9c` |
| `proof_notes.md` | `b214d4efaf27bb706b85d162a07fa2179679feb8d80da79443b8660a7e36e754` |
| `history_frame_search.py` | `bbbff2b52a8e639ab5d09b60c4782e693f614150d36e6c07a18346f1e2a79836` |
| `results.jsonl` | `cf4f4ff792e71a83ecf0976ebe400c90c05b1c6f1f525af1fe179414a0b7b58a` |
| `summary.json` | `f4fa2b7952e700b4abd679b1aab5b1261ff0fb48e0377b6045f6ad04cb62c39a` |
| `micro_history_collision.py` | `c85974e8b739eca52f5e2519d540554fa6bc760426be943dea0562eea810156e` |
| `micro_collision.json` | `79a2bda224d680b2a617ac3511d8a60f3a8d5e75447f2f162e7e97340b1f15b8` |
| `hidden_frame_spectrum.py` | `f8aa025594bbe695c04ad6888b03e93c8e2d10877e20a7760b6c366d80413fdd` |
| `hidden_frame_spectrum.json` | `5a0247db16a0af0f0d68dbf357415f4da216fdfb5dbde7a9caf42261bf8f153b` |
| `freeze_manifest.md` | `72c8c7387fd71d0556ca91ebcc09ed2462aae891b6ad71342b64bbad7c5c51bd` |

The surrounding sampler target remains uniform on fixed-length identity words
in `Omega(N,m)`.  Permutations compose as `(pq)(x)=p(q(x))`; factors are
displayed left-to-right.  This audit concerns only the auxiliary nonlazy
minimal-long-cycle parking reset recurrence

```text
H=(I-Q)^(-1)A0,
Q(x,y)=rho_s(k,t) nu_(K,R,k)(j),  j=1,...,k.
```

It does not concern the original lazy `{3,4,5}` heat-bath kernel directly.

## Field 3 — exact composition law, basins, and unrestricted rank-five failure

For every ordered composition `C` of `s`, independent reconstruction uses

```text
rho_s(C)=prod_i [c_i^(c_i-1)/c_i!]
         /[len(C)! (s+1)^s/(s+1)!].
```

For an active endpoint `e`, `B_e` consists of compositions refining its first
part, and `c_e=len(e)rho_s(e)`.  With

```text
O_(e,f)=rho_s(B_e intersect B_f),
C_(e,f)=c_e 1[e=f],
```

the analysis Gram matrix is `C^(-1/2) O C^(-1/2)`.  On

```text
E={(1,3,1),(2,2,1),(3,1,1),(4,1)},
```

the independent `C-O` matrix is exactly

```text
[ 5/108       0        0       -5/216   ]
[    0     35/1296     0      -25/1296  ]
[    0        0      49/1296  -41/1296  ]
[ -5/216  -25/1296  -41/1296    4/81    ].
```

Its determinant is `-27125/235092492288`.  For
`a=(1/2,5/7,41/49,1)`, exact independent arithmetic gives

```text
a^T(C-O)a = -155/63504,
a^T C a   = 2094265/6223392,
a^T O a   = 2109455/6223392,
(a^T O a)/(a^T C a)=421891/418853>1.
```

This proves the unrestricted frame failure exactly.  Exhaustive principal-
minor reconstruction finds no unrestricted failure for `s=2,3,4`; at `s=5`
all `231` principal minors of size at most three are nonnegative.  Thus the
claimed first-rank and first-found-minor scope is correct.

## Field 4 — required centering supplement and bounded-event witness

The reset inputs are centered functions such as `h-q`, so unrestricted and
centered frame statements must be distinguished.  For the rank-five vector
above, the represented function has mean

```text
15835/63504 != 0.
```

Centering that same function changes its Rayleigh quotient to
`223235923/271416744<1`.  More generally, on the centered subspace the defect
matrix is

```text
C-O+b b^T,  b_e=rho_s(B_e).
```

Independent exact enumeration checks every principal minor of this matrix:
`3` at `s=3`, `31` at `s=4`, and `2047` at `s=5`; all are strictly positive.
Hence the first centered generic-frame failure is not `s=5`.

At `s=6`, let integer `z(C)` have the 27 nonzero values recorded in
`independent_results.json`, zero elsewhere, and set
`f=z-E_rho z`.  Independent exact arithmetic gives

```text
E_rho z              = -642/16807,
||f||^2_(L2(rho))    = 369677976/282475249,
sum_e theta_e(f)^2/c_e
 = 588390548570425199/427280535894870000,
energy/norm
 = 18980340276465329/18038257962480000 > 1.
```

Thus centering does not rescue the generic Bessel route.  A still cleaner
bounded-event witness occurs at `s=8`: take `S=B_(6,2)`,
`q=rho_8(S)=512/6561`, and `f=1_S-q`.  Then

```text
||f||^2 = 3097088/43046721,
energy  = 128297435442762499633/1751104078464989745000,
energy/norm
 =128297435442762499633/125986911480783360000 > 1.
```

Both are valid append-only referee supplements.  Neither function is proved
to belong to the actual contextual family generated by `(K,R,B)`.

## Field 5 — complete success histories and signed two-copy identity

For `x=(s,K,R,B)`, the accepted closed contextual mean and attachment law give

```text
Q(x,y)=rho_s(k,t)nu_(K,R,k)(j),
y=(t-1,K+k,R+j,B), t>B, j=1,...,k.
```

The phase `s+K-R` strictly decreases.  Induction over this finite DAG proves
that the total terminal success-history mass equals

```text
q_x=w_(s+1-B)w_B/w_(s+1).
```

Every live attachment rank is retained; `j=0` is killed; no child/parent
action factor occurs.  Independently expanding each basin current

```text
theta_e=sum_(C in B_e)rho_s(C)[h_x(C)-q_x]
```

into its ordered left and right signed copies gives
`theta_e^2/c_e` by distributivity.  Summing this equality over every
nilpotent prefix proves the all-j signed two-copy identity for `H`.  This is
an algebraic equality, not positivity or a Bessel estimate.

The fresh no-import checker verifies `162` right-heavy success-mass identities
through `s=10,K in {1,2,5}` and `722` direct signed-resolvent identities when
the multitype scan is included.  It sees every attachment pair `(k,j)` for
`1<=j<=k<=8`.

## Field 6 — collision, first-edge mismatch, and extra-alpha falsifiers

At `x=(4,1,0,1)`, the source `C=(1,1,1,1)` has
`rho_4(C)=1/125`, `h_x(C)=1`, and lies in both active canonical basins

```text
B_(2,1,1), B_(3,1).
```

The true later current is `1647/15625`; assigning each source only to its
first active edge changes it to `1098/15625`.  Correspondingly,

```text
true A0                   =1351279/28125000,
first-edge partition value= 748477/28125000.
```

Thus finer hidden marks cannot make these source-defined nested basin
memberships disjoint.  Independently rebuilding the ambient `n=6,r=5`
parking factor words, all four scan sites, and their actual two/three-element
pair fibres finds five source words and exactly two favourable marked atoms.
Their normalized total rate is `1/30=alpha_5`, and both lie over the same
double-basin local composition.

At `x=(3,1,0,1)`, the correct success mass is `q=9/16`.  Inserting
`alpha_child/alpha_parent` gives `15/16`; inserting its inverse gives `7/16`.
Both extra-alpha normalizations are therefore exactly false.

## Field 7 — full pullback, success weighting, and cross-prefix scope

If a full marked probability space `(Omega,mu)` has a forgetful map
`kappa` with `kappa_*mu=rho_s`, then

```text
U:f -> f composed with kappa
```

is an isometry.  Hence the constant-pullback basin vectors with unchanged
capacities have exactly overlap matrix `O` and inherit both the unrestricted
and centered obstructions above.  Adding positive frame coordinates cannot
remove a bad root block.

This does not identify either of two different operators.  The successful
submeasure has pushforward `rho_s(C)h_x(C)`, so its overlaps are

```text
O^succ_(e,f)=sum_C rho_s(C)h_x(C)1_Be(C)1_Bf(C),
```

not `O`.  A genuine all-prefix history frame additionally requires joint
intersections between different prefix events and their local basin pulls.
M123's aggregate recursion computes neither its failure atoms nor those
cross-prefix Gram entries.  Therefore the unrestricted, centered,
success-weighted, cross-prefix, and actual contextual-family questions cannot
be conflated.

## Field 8 — computation, finite scope, dependencies, and hygiene

`independent_referee.py` imports no predecessor experiment code or result.  It
implements composition weights, capacities, basin intersections, exact
determinants, all principal-minor checks, both centered witnesses, contextual
means, all attachment ranks, nilpotent resolvents, the collision, and the
literal parking-word witness.  Reproduce with

```text
python3 -B independent_referee.py --output independent_results.json
```

Python is `3.12.3`; dependencies are `{}`; seed is `null`; arithmetic is
`fractions.Fraction`.  The exact finite scan finds zero right-heavy target
failures through `s=10` and zero stronger multitype-envelope failures through
`s=8,K<=6`; its respective largest ratios reproduce M123's
`.6731838254...` at `(10,1,0,4)` and `.6210042669...` at `(8,1,0,3)`.
These are finite falsifiers only.

Fresh predecessor reruns reproduced its frame and literal-collision JSON
byte-for-byte and all declared history-scan fields.  During the audit the
coordinator's separate `importlib` check created one M123 `__pycache__`; the
coordinator identified and removed exactly that generated cache.  It is not
an M123 hygiene objection.  No predecessor, coordinator note, manuscript,
project skill, or file outside the owned M128 directory was edited by M128.

## Field 9 — final verdict and open obligations

**ACCEPT, with zero material numbered objections and the centering supplement
in Field 4.**

Promote only the following scoped conclusions:

```text
PROVED: complete normalized success-history mass equals q;
PROVED: the universal all-j signed two-copy expansion equals H;
PROVED: canonical reset basins are not disjoint categories;
PROVED: full measure-preserving constant pullback is isometric;
REFUTED: both extra-alpha history normalizations;
REFUTED: the generic unrestricted canonical-basin Bessel bound, first at s=5;
PROVED SUPPLEMENT: the centered generic frame is bounded through s=5;
REFUTED SUPPLEMENT: the centered generic frame fails at s=6;
REFUTED SUPPLEMENT: it fails even for a centered basin indicator at s=8.
```

The first open obligation remains a new inequality specialized to the actual
contextual reset functions, or a correctly defined success-weighted/cross-
prefix history operator with an exact equality to `H`.  `L=5`, all-suffix
contraction, ROOT-MEAN LIFT, every original-chain gap, polynomial mixing, and
both terminal outcomes remain unresolved.

