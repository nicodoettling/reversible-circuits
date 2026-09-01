# M175 final report: synchronized relative-orientation cycle space

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and exact scope

```text
FINAL VERDICT: KEEP A PROVED EXACT LOCAL-GENERATOR/CYCLE-SPACE REDUCTION AND
AN EXACT RANK-FOUR NONZERO-VOLTAGE CERTIFICATE.

PROVED for every d>=3 and every tuple width: V_stab is exactly the binary
span of fundamental-cycle gains in the actual synchronized signed-Hurwitz
Schreier component.

PROVED for fixed physical endpoints: zero-voltage routing is exactly affine
membership in that chord-column space.

PROVED for accepted d>=5 matching subfamilies: K_mon/P is precisely this
column space, using accepted M169/M172.

EXACT at d=4: one ordered-pair component has full W_2 voltage, witnessed by
the four-move positive braid R_4 R_3 R_5 R_4.

UNRESOLVED: the chord rank and physical endpoint membership for accepted
d>=5 matching subfamilies, quotient-route length, and inner-correction length.
```

This is the permitted rigorous finite combinatorial reduction. It does not
prove a common M135 braid or a uniform full-/zero-voltage theorem.

```text
candidate                  | synchronized relative-orientation gain graph
claimed target             | qualitative diagonal signed-Hurwitz orbit lifting
identity ok                | Hurwitz/relabeling preserve connected product one
crosses Hurwitz components | not applicable; this classifies one action orbit
exact diagnostics          | clean-room complete ordered pairs at d=3,4
verdict                    | keep exact cycle-space theorem and d4 certificate
```

## Field 2 — reconciled target, convention, and immutable dependencies

For `d>=3`, `m=2d-2`, the auxiliary physical space is

```text
Z_d={(t_1,...,t_m):t_1...t_m=id,
                         support connected on [d]},
Q_d=Z_d/S_d.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. Chronological signed right-Hurwitz moves are

```text
R_j(a,b)=(b,b^(-1)ab),
R_j^(-1)(a,b)=(aba^(-1),a).
```

All `SHA256SUMS` lists for M135/M137, M141/M143, M146/M148, M154/M158,
M163/M164, and M169/M172 passed before use. The new theorem uses only the
accepted free quotient action, groupoid parity cocycle, and relative-
orientation interpretation. Its accepted-matching corollary uses

```text
1 -> P_(d,s) -> K_mon(q) -> V_stab(q) -> 1
```

from M169/M172. No literature classification or predecessor computation is
imported.

## Field 3 — explicit local generator and gain graph

Choose a section `sigma:Q_d->Z_d`. For each signed generator `g` and quotient
point `a`, let the unique canonicalization transporter be

```text
g sigma(a)=rho_g(a).sigma(ga),
kappa_g(a)=sgn(rho_g(a)) in F_2.
```

For a synchronized ordered tuple `x=(a_1,...,a_s)`, the local edge gain is

```text
gamma_g(x)=[kappa_g(a_1),...,kappa_g(a_s)]
             in W_s=F_2^s/Delta.
```

The reverse signed-generator edge has the same gain because transporter
inversion preserves sign. The gain of a chronological braid route is the sum
of these local vectors by the accepted cocycle. The graph retains the actual
synchronized tuple endpoint, signed generator label, loops, and parallel
edges. It is not an independent-coordinate product relaxation.

## Field 4 — exact realizable fundamental-cycle theorem

In the connected signed Schreier component `Gamma(q)`, choose a spanning tree
and let `p_T(x)` be the gain of the root-to-`x` tree path. For every directed
edge `e:x->y`, put

```text
z_T(e)=p_T(x)+gamma(e)+p_T(y).
```

The proof in `proof.md` establishes

```text
V_stab(q)=span_F2{z_T(e)}.                            (4.1)
```

Each column is realized by the literal closed signed braid: tree path to
`x`, edge `e`, reverse tree path from `y`. Conversely, summing the columns of
the edges in any closed braid walk cancels every tree potential and recovers
its voltage. Thus (4.1) is exactly realizable, not a merely formal cycle
space.

Consequently full voltage is exactly chord rank `s-1`; trivial voltage is
exactly balancedness, equivalently all chord columns zero. A large spanning
tree can be exponential, so this gives no short word.

## Field 5 — fixed physical endpoints and coboundary

For fixed physical lifts `U,V` over vertices `q,r` in one component, let
`a_T(U,V)` be the relative transporter parity of the tree route, including
the endpoint orientation offsets. The complete fixed-endpoint route-voltage
set is

```text
a_T(U,V)+span_F2{z_T(e)}.                             (5.1)
```

Therefore a zero-voltage quotient route exists exactly when

```text
a_T(U,V) belongs to the chord-column space.           (5.2)
```

Changing the section adds a vertex coboundary to local labels and tree
potentials but leaves every chord gain unchanged. Independently changing
physical endpoint lifts changes `a_T` by the accepted endpoint coboundary;
the complete physical condition transforms with it. Statements of (5.2)
always retain the fixed physical endpoints. Simultaneously relabeling a
matched source/target pair preserves the condition.

## Field 6 — accepted matching quotient and first unresolved lemma

For every accepted nonempty ordered `d>=5` M135 matching subfamily,
M169/M172 plus (4.1) gives

```text
K_mon(q)/P_(d,s) ~= colspan{z_T(e)}.                  (6.1)
```

The exact next qualitative statement is the **ACCEPTED-MATCHING CHORD-RANK
LEMMA**: determine this span for every such tuple; in particular decide
whether its rank is `s-1`, and for the fixed physical DPS source/target
decide membership in (5.2).

This replaces the abstract full-voltage question by explicit local
canonicalization signs and actual synchronized cycle relations. It remains
unresolved. Even a positive full-rank result would not give polynomial
quotient or inner-correction words.

## Field 7 — exact rank-three/four calibration and falsification

The clean-room checker exhausts only `d=3,4`.

At `d=3`, `|Z_3|=24`, `|Q_3|=4`; the two ordered-pair components have

```text
(base size, chord rank)=(4,0),(12,0).
```

This reproduces trivial `V_stab` for every rank-three ordered pair.

At `d=4`, `|Z_4|=2880`, `|Q_4|=120`; all four ordered-pair components have

```text
(120,0), (240,0), (4320,1), (9720,0).                (7.1)
```

For the two canonical words

```text
u=((01),(01),(02),(02),(03),(03)),
v=((01),(01),(02),(02),(13),(13)),
```

the chronological positive braid `R_4 R_3 R_5 R_4` fixes both quotient
points. Its literal transporters in zero-based image notation are

```text
(0,1,3,2), sign 1;       (1,0,3,2), sign 0.
```

It therefore realizes nonzero relative voltage and proves the rank-one row
in (7.1) by a four-move witness. This refutes universal trivial stabilizer
voltage at exceptional rank four, not at `d>=5`.

The stronger formula `kappa_j(a)=theta(a)+theta(R_j a)+c_j` is inconsistent
already at `d=3` and also at `d=4`. Balancedness of a tuple component cannot
be inferred from such a global one-coordinate character.

## Field 8 — reproduction, artifacts, and hygiene

Deterministic reproduction, Python `3.12.3`, dependencies `{}`, `seed=null`:

```text
python3 -m compileall -q relative_orientation_cycle_audit.py
python3 -B relative_orientation_cycle_audit.py
python3 -c 'import json; q=json.load(open("results.json")); r3,r4=q["rows"]; assert r3["ordered_pair_cycle_space"]["all_pair_stabilizer_voltages_trivial"]; h=r4["ordered_pair_cycle_space"]["component_size_voltage_rank_histogram"]; assert h==[{"base_size":120,"count":1,"rank":0},{"base_size":240,"count":1,"rank":0},{"base_size":4320,"count":1,"rank":1},{"base_size":9720,"count":1,"rank":0}]; c=r4["ordered_pair_cycle_space"]["short_positive_certificate"]; assert c["endpoint_quotient_indices"]==c["source_quotient_indices"] and c["relative_voltage"]==1; print("assertions ok")'
sha256sum -c SHA256SUMS
```

The checker imports no predecessor module/data, has no stochastic branch,
and contains an explicit scope string forbidding `d=5` enumeration. Owned
artifacts are `plan.md`, `checkpoint.md`, `halfway_checkpoint.md`, `proof.md`,
`relative_orientation_cycle_audit.py`, `results.json`, this report,
`freeze_manifest.md`, and `SHA256SUMS`. No predecessor, coordinator,
manuscript, skill, or other mission file was edited. No cache is retained.

## Field 9 — final decision and scope boundary

```text
KEEP THE EXACT SYNCHRONIZED GAIN-GRAPH/CYCLE-SPACE THEOREM.
KEEP THE FIXED-ENDPOINT AFFINE COLUMN-SPACE TEST.
KEEP THE d4 FOUR-MOVE NONZERO-VOLTAGE CERTIFICATE AS AN EXCEPTIONAL WARNING.
LEAVE THE d>=5 ACCEPTED-MATCHING CHORD RANK AND ENDPOINT MEMBERSHIP OPEN.
```

No `d=5` quotient orbit, broad quotient group, common M135 braid, polynomial
matching refinement, polynomial word length, physical minimal-sector gap,
original lazy exact `{3,4,5}` heat-bath gap, mixing theorem, Terminal A, or
Terminal B result is claimed.

