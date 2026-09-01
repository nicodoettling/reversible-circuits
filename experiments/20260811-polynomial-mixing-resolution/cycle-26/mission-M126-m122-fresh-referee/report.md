# M126 fresh referee report on frozen M122

Date: 2026-08-13 UTC.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — decision, scope, and numbered objections

```text
ACCEPT M122 AS A SCOPED THEOREM/OBSTRUCTION.
Material numbered objections: none.
```

M122 correctly proves one infinite rooted DPS adjacent-value family, refutes
universal bounded output/route locality for adjacent DPS value swaps, and
gives two source-recoverable signed-Hurwitz routes for the resulting
square-prefix conjugation.  It correctly leaves all-edge congestion and
**ROOTED PRODUCT LOCAL COMPARISON** unresolved.

This acceptance proves no gap for the physical signed-Hurwitz chain on
`Z_d`, no route for every ideal adjacent-value or UST basis-exchange edge, no
arbitrary-product `Gamma_0` estimate, no gap for the lazy exact `{3,4,5}`
same-product heat bath, and neither Terminal A nor Terminal B.

## Field 2 — frozen provenance, target, convention, and kernels

The frozen M122 checksum file verifies in full.  The assigned payload hashes
independently match:

| frozen artifact | required and observed SHA-256 |
|---|---|
| `report.md` | `c4c4d305d1800aa8edbde6ca10484928bdfd36f0bf447c33f0a759f780b4401a` |
| `star_cascade_obstruction.md` | `70d5b4ca80bbc1f81adefbb671c17395b0a08dd89bd7bf9318daa0e3b193ed32` |
| `star_cascade_audit.py` | `19160f865a8a24b69f511b1108ba32808f2ca097dc83b86b24e3c3b3bdce6605` |
| `star_cascade_results.json` | `2affa2c0621f5e024977da4950309afe62f18ce83bf7ab2eeaeb42cabe0a22a6` |
| `freeze_manifest.md` | `513c296d933768ecefa5cfe801191be24c4606e97a0d07326901637cc5c9d932` |
| `SHA256SUMS` | `554370997c6e75604b3f88b5d98abc0b4806ce673784b7994c5531722689afa0` |

The audited auxiliary target is uniform on

```text
Z_d={w=(t_1,...,t_(2d-2)): t_1...t_(2d-2)=id,
                              support(w) connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`, and displayed tuple factors
multiply left-to-right.  The physical kernel is

```text
P_(0,d)=I/2+[1/(4(2d-3))] sum_i (R_i+R_i^(-1)),
R_i(a,b)=(b,bab),       R_i^(-1)(a,b)=(aba,a).
```

The accepted M112/M119 input is the literal rooted DPS bijection

```text
rooted Z_d <-> Cayley trees on [d] x S_(2d-2),
```

with exactly `d` roots above each unrooted word.  DPS supplies the bijection
and closure, not a local Hurwitz simulation or congestion theorem.

## Field 3 — exact DPS star endpoints

For `d>=3`, let `T_d` be the white Cayley star centered at `y_1`, rooted at
`y_d`, and take `pi=id` in `S_(2d-2)`.  Swapping the adjacent values `1,2`
changes only the two labels incident with the first inserted black vertex.
M122's symbolic outer-contour calculation correctly gives

```text
w_d =((1,d),(1,d),(1,2),(1,2),...,(1,d-1),(1,d-1)),
w'_d=((1,d),(1,d),(2,d),(2,d),...,(d-1,d),(d-1,d)).
```

For the source, labels `1,2` each make `d-2` distance-one closures and every
label `3,...,2d-2` makes `d-3` distance-one closures followed by one
distance-three closure against `x_1`.  For the swapped input every label
makes `d-2` distance-one closures and no distance-three closure; the new
black vertex supplies the second endpoint.  The displayed cyclic intervals
exhaust every loose half-edge, and the branchwise cancellations plus the
descending residual stack give an induction valid for every `d>=3`.

Both outputs are products of adjacent squares and their support graphs are
stars on all `d` labels, so they lie in `Z_d`.  The independent M126 closure
implementation reconstructs the rotations and cyclic local closure directly
from hairy-tree incidences rather than importing M122 code or output; it
reproduces both formulas and complete closure tables through `d=24`.

## Field 4 — factor cascade and route lower bound

The first two factors of `w_d,w'_d` agree.  At every remaining position the
source factor `(1,k)` and target factor `(k,d)`, `2<=k<=d-1`, are distinct.
Their exact factor Hamming distance is therefore

```text
2d-4.
```

One signed adjacent-Hurwitz action changes at most its two selected
coordinates.  The Hamming triangle inequality along any route of length `r`
gives `2d-4<=2r`, hence

```text
r>=d-2.
```

Thus M122 validly refutes exactly the two named universal premises that every
adjacent DPS value swap changes `O(1)` output factors or has an `O(1)`
signed-Hurwitz route.  This is only a linear lower bound and is fully
compatible with polynomial comparison; M122 does not promote it to a slow-
mixing obstruction.

## Field 5 — universal square-prefix full twist

Let `h,u_1,...,u_L` be transpositions, `L>=2`, and suppose
`u_1...u_L=id`.  Put

```text
C_L=R_2 R_3 ... R_(L+1).
```

For a general `n`-tuple with product `P`, one sweep
`R_1...R_(n-1)` moves the first factor to the end as `P^(-1)g_1P`.
Because Hurwitz moves preserve `P`, exactly `n` sweeps restore the order and
conjugate every coordinate by `P`.  Applying this to the subtuple
`(h,u_1,...,u_L)`, whose product is `h`, proves

```text
C_L^(L+1)(h,h,u_1,...,u_L)
  =(h,h,h u_1 h,...,h u_L h).
```

The schedule has exactly `L(L+1)` actions and depends only on `L`.  Deleting
actions that hold leaves a physical path no longer than this schedule.
Hurwitz actions preserve product and generated subgroup, so all star-family
intermediates remain in `Z_d`.  For the star suffix, `L=2d-4`, giving the
valid universal scheduled length `(2d-4)(2d-3)`.

## Field 6 — shorter shared-endpoint route and its boundary

If `u_L=h` or `u_L` shares exactly one endpoint with `h`, M122's shorter word

```text
R_2 R_3 ... R_L R_(L+1)^(-1) R_L ... R_3 R_2
```

also has the required endpoint and contains `2L-1` scheduled actions.  After
the forward sweep, the penultimate factor is

```text
k=u_L h u_L.
```

The equality/shared-endpoint transposition identities give
`k u_L k=h` and `k=h u_L h`; the middle inverse action therefore creates
`(h,h u_L h)`, and the descending sweep moves `h` left while conjugating the
remaining suffix entries.  This proves the route universally under the
stated hypothesis.

For the DPS star, `u_L=(1,d-1)` shares endpoint `1` with `h=(1,d)`, so the
route has length `4d-9`; direct inspection shows every star-family action is
off diagonal.  The independent exhaustive `S_4` audit checks all 36 sources
with identity suffix length two and all 720 sources with identity suffix
length four; all 630 applicable shorter-route cases have the claimed
endpoint.

The hypothesis is not silently dropped.  With disjoint
`h=(1,4)`, `u=(2,3)`, and `U=(u,u)`, the three-action word
`R_2 R_3^(-1) R_2` ends at `(h,u,u,h)` rather than `(h,h,u,u)`, while the
six-action full twist succeeds.  This is a counterexample only to the
overgeneralized short braid; its support is disconnected and it is not a
`Z_d` obstruction.

## Field 7 — scheduled/compressed recovery and root capacity

For fixed `L`, route direction, descriptor, and scheduled time, a physical
oriented edge determines at most one source: invert the known bijective
Hurwitz prefix.  Holding actions do not alter this argument.  If holds are
deleted and only compressed physical time is retained, each of the at most
`L(L+1)` scheduled times yields at most one candidate, so source
multiplicity is at most `L(L+1)`.  This is conditional descriptor recovery;
it does not count the distinct ideal descriptors whose routes can share one
physical edge.

The independent checker explicitly reconstructs candidates after deleting
holds.  On the star routes through `d=24`, it never loses the actual source
and finds maximum candidate multiplicity one; the proof uses only the safe
universal scheduled-length bound.

The spectrum-preserving rooted lift has stationary mass `1/(d|Z_d|)` and,
after a word move, refreshes the target root uniformly.  For `M=2d-2`, a
specified nontrivial lifted signed action has capacity at least

```text
[1/(d|Z_d|)] [1/(4(M-1))] [1/d],
```

while the corresponding adjacent-value ideal demand has capacity

```text
[1/(d|Z_d|)] [1/(4(M-1))].
```

Thus selecting a deterministic legal root sequence loses exactly the one
refresh factor `d` in this comparison bound.  A single full-twist demand has
load at most `dL(L+1)` and the shorter star demand at most `d(2L-1)`.
These are single-demand bounds only, not a sum over ideal demands and not an
all-edge congestion estimate.

## Field 8 — independent computation, dependencies, and hygiene

`independent_star_referee.py` imports no M122 or predecessor experiment code
or output.  It independently implements permutation evaluation, both signed
Hurwitz actions, the rooted hairy-star incidences, vertex-rotation contour,
cyclic local closure, both braid schedules, compressed-time recovery, and
the root-capacity ratio.  Its deterministic reproduction command is

```text
python3 -B independent_star_referee.py \
  --min-d 3 --max-d 24 --output independent_results.json
```

Python is `3.12.3`; dependencies are `{}`; seed is `null`; repository commit
is the one stated above.  Every finite check passes.  The exact rows are
convention checks and falsifiers, not the proof of a universal formula.

Before judgment I read the repository source of truth, project skill,
sampling and experiment references, relevant manuscript status, accepted
M112 construction, M119 fresh audit, and every frozen M122 proof/report
artifact.  M122 uses no new external theorem beyond the already source-
audited DPS construction.  No predecessor, coordinator, manuscript, project
skill, or file outside the owned M126 directory was edited.

## Field 9 — final verdict and open obligations

**ACCEPT, with zero material numbered objections.**

Promote only these scoped conclusions:

```text
PROVED: one adjacent-value DPS star family changes exactly 2d-4 factors;
PROVED: every physical route for that family has length at least d-2;
PROVED: the universal square-prefix full twist has length L(L+1);
PROVED: the shared-endpoint short route has length 2L-1;
PROVED: scheduled recovery is unique and compressed recovery is polynomial;
PROVED: the root refresh contributes one factor d for this single demand;
REFUTED: universal O(1) output/route locality for adjacent DPS swaps.
```

The first open obligation remains **ROOTED PRODUCT LOCAL COMPARISON** for all
adjacent-value and UST basis-exchange ideal edges, including the total
stationary descriptor load.  Arbitrary-product `Gamma_0`, every physical
gap, the original heat-bath gap, and both terminal outcomes remain open.
