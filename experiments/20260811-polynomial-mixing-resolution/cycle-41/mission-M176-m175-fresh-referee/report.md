# M176 fresh referee report on frozen M175

Date: 2026-08-13 UTC. Audited repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — exact verdict and numbered objections

```text
FINAL DECISION: ACCEPT M175 AT ITS EXACT QUALITATIVE, NONTERMINAL SCOPE.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

M175 correctly proves that point-stabilizer relative voltage is exactly the
`F_2` span of literal fundamental-cycle gains in the actual synchronized
signed-Hurwitz Schreier component. It also correctly proves the fixed-
physical-endpoint affine membership criterion and interfaces with M169's
accepted-matching monodromy exact sequence.

Numbered nonmaterial clarifications:

1. The displayed `d=4` symbols denote the chronological application list
   `[R_4,R_3,R_5,R_4]`. Under proof (2.4)'s algebraic notation
   `b=g_L...g_1`, the product is written in reverse order. M175's JSON and
   literal checker make the intended route unambiguous.
2. Proof Section 5 compresses two operations: a section change with fixed
   physical endpoints leaves endpoint-corrected `a_T(U,V)` invariant,
   whereas independently changing the physical endpoints translates it.
   M175's final report distinguishes them correctly.
3. “Every tuple width” means `s>=1`; at `s=1`, `W_1=0`. Empty width is
   outside the declared nonempty matching scope.

```text
candidate                  | synchronized relative-orientation gain graph
claimed target             | qualitative diagonal signed-Hurwitz orbit lift
identity ok                | Hurwitz/relabeling preserve connected product one
crosses Hurwitz components | not applicable; no global sampler claim
exact diagnostics          | all d3 pairs; literal d4 nonzero certificate
verdict                    | accept exact reduction and finite warning only
```

## Field 2 — immutable provenance and hash gate

Before substantive interpretation, `sha256sum -c SHA256SUMS` passed for all
eight frozen M175 payload files. No M175 file was edited.

| frozen M175 artifact | observed SHA-256 |
|---|---|
| `plan.md` | `bd2d635806648a1d581e4dd74147dcc4f6d278154c97916864f4df4a29b6a34a` |
| `checkpoint.md` | `e7416d607f954c921973a5a65a25ec47d7a82eff12e2232d1ba8b3843c0e6a81` |
| `halfway_checkpoint.md` | `3b888e07d2bad6ae94f15af8636e5428cf0991686abd9618bb2cd01aac691850` |
| `proof.md` | `0ea720ce6f6987cc4f39b1cd1bb86dab2f6428ce51140eda77261d4fb4534ea9` |
| `relative_orientation_cycle_audit.py` | `deeef84f4887f16b1e45930187500ac27ecdf184a4679640a632b3fd85fdaf8a` |
| `results.json` | `92f28da805b36577089677c476b517d034d11f5c534becc761e2329b62553a50` |
| `report.md` | `f6293983c2bb6620db3eace9f9f159c4bd12d0c7175c068cfa67818514c7c72a` |
| `freeze_manifest.md` | `42e6ae9ecd4537a79c07ed4fef812f16e3b8d2416c34e416e477b7e62d186e16` |
| `SHA256SUMS` | `f2718a493b7e30a615da1f6e4dbafad9d6501bcbd07822fd791b21eafbb26d88` |

Frozen M169 and its fresh M172 referee checksum lists also passed before the
exact-sequence interface was used. M172 accepted M169 with no material
objection.

## Field 3 — local canonicalization sign and inverse convention

For a section `sigma:Q_d->Z_d`, freeness gives the unique transporter

```text
g sigma(a)=rho_g(a).sigma(ga).
```

Applying `g^{-1}` and commuting it past relabeling gives

```text
rho_(g^{-1})(ga)=rho_g(a)^{-1}.
```

Therefore a directed edge and its signed inverse have equal parity. For a
tuple `x=(a_1,...,a_s)`, M175's local gain

```text
gamma_g(x)=[sgn rho_g(a_1),...,sgn rho_g(a_s)]
             in W_s=F_2^s/Delta
```

is exactly the groupoid parity cocycle. The physical transporter order
abelianizes under parity, so the gain of a chronological route is the sum of
its local gains. The signed formulas

```text
R_j(a,b)=(b,b^{-1}ab),
R_j^{-1}(a,b)=(aba^{-1},a)
```

are mutual inverses and match both frozen and independent checkers.

## Field 4 — exact realizable chord-span theorem

Choose a spanning tree `T` in the actual synchronized signed-generator
component rooted at `q`. Let `p_T(x)` be the gain of its literal tree route
and define for every directed edge `e:x->y`

```text
z_T(e)=p_T(x)+gamma(e)+p_T(y).
```

Both required inclusions hold:

- Realizability: the literal word “tree route `q->x`, edge `e`, inverse tree
  route `y->q`” fixes `q` and has voltage `z_T(e)`. This includes loops and
  parallel edges. Concatenating these literal loops realizes every binary
  column combination.
- Converse: for any closed stabilizer walk with edges `e_l:x_(l-1)->x_l`,
  summing `z_T(e_l)` cancels all tree potentials in pairs and leaves exactly
  `sum_l gamma(e_l)`, its stabilizer voltage.

Hence, for every `d>=3` and `s>=1`,

```text
V_stab(q)=span_F2{z_T(e)}.
```

Full voltage is exactly column rank `s-1`; trivial voltage is exactly
balancedness. This uses the actual synchronized labeled action graph, not a
Cartesian or formal independent-coordinate relaxation. It gives no short
route or polynomial diameter.

## Field 5 — section/coboundary and fixed endpoints

If `sigma'(a)=eta(a).sigma(a)`, then

```text
kappa'_g(a)=sgn eta(a)+kappa_g(a)+sgn eta(ga).
```

This vertex coboundary changes displayed edge labels and tree potentials but
cancels from every chord gain. The chord space and `V_stab` are therefore
section-independent.

For fixed physical endpoints

```text
U=n_U.sigma(q), V=n_V.sigma(r),
b_T sigma(q)=c_T.sigma(r),
```

the tree route's physical transporter is `n_U c_T n_V^{-1}`. Its relative
sign is M175's `a_T(U,V)`. Every other route differs from the tree route by a
literal point-stabilizer loop, so the complete fixed-endpoint route-voltage
set is exactly

```text
a_T(U,V)+V_stab(q).
```

It contains zero iff `a_T(U,V)` belongs to the chord column space. A section
change with `U,V` fixed changes their section coordinates compatibly and
leaves this physical test invariant. Independent changes of `U,V` translate
the affine test by the accepted endpoint coboundary, as they must.

## Field 6 — M169 exact-sequence interface

For each accepted nonempty ordered `d>=5` M135 matching subfamily, M169/M172
proves that relative sign restricts to a surjection

```text
lambda:K_mon(q)->V_stab(q)
```

with kernel exactly `P_(d,s)`. The kernel equality uses the accepted literal
inner-loop realization `P_(d,s)<=K_mon(q)`. Thus

```text
1 -> P_(d,s) -> K_mon(q) -> V_stab(q) -> 1,
K_mon(q)/P_(d,s) ~= colspan{z_T(e)}.
```

M175 uses this only at the accepted matching scope. Its `d=4` warning is not
promoted into that sequence. Neither theorem decides the `d>=5` chord rank,
fixed DPS endpoint membership, quotient route length, or inner-correction
length.

## Field 7 — independent bounded replay and finite table audit

`independent_gain_audit.py` imports no predecessor module or data. It exactly
reconstructs `d=3` and obtains

```text
|Z_3|=24, |Q_3|=4,
(ordered-pair component size, chord rank)=(4,0),(12,0).
```

An independent augmented-cover BFS gives root-voltage set `{0}` for both
components.

At `d=4`, the referee cap was the literal certificate, not a second `Q_4`
closure. The independent replay applies chronological list `[4,3,5,4]` to
M175's two physical words and obtains

```text
transporter images   (0,1,3,2), (1,0,3,2)
sign bits            1, 0
local sign lists     [0,1,0,0], [0,0,0,0]
relative voltage     1
```

Both quotient coordinates close. Since `W_2` has dimension one, this is a
literal full-rank stabilizer certificate for its component.

M175's frozen exhaustive algorithm for the remaining `d=4` table was also
audited. It processes all `14400` ordered pairs, computes fundamental-cycle
bits, and independently cross-checks each component with the augmented
orientation cover. Its recorded rows

```text
(120,0), (240,0), (4320,1), (9720,0)
```

sum to all pairs, and the rank-one row has the independent literal witness
above. No defect was found. This is exact finite calibration only; no `d=5`
closure or asymptotic inference was attempted.

## Field 8 — unresolved obligation and scope boundary

The first surviving qualitative obligation is exactly M175's accepted-
matching chord-rank lemma:

> For each accepted nonempty ordered `d>=5` matching subfamily, determine
> the span of its actual synchronized fundamental-cycle columns, and for the
> fixed physical source/target decide affine membership.

Even full rank would be qualitative. Polynomial quotient word length and a
short aligned inner correction remain separate. M175 proves no common M135
braid, no polynomial matching refinement, no physical-sector spectral gap,
no original lazy exact `{3,4,5}` heat-bath gap, no mixing theorem, and no
Terminal A/B conclusion.

## Field 9 — reproduction, artifacts, hygiene, and final decision

Deterministic reproduction from this M176 directory, Python `3.12.3`,
standard library only, `seed=null`:

```text
python3 -m compileall -q independent_gain_audit.py
python3 -B independent_gain_audit.py
python3 -B -c 'import json; q=json.load(open("independent_results.json")); assert [(r["base_size"],r["chord_rank"]) for r in q["d3"]["ordered_pair_components"]]==[(4,0),(12,0)]; assert q["d4_certificate"]["relative_voltage"]==1; print("assertions ok")'
sha256sum -c SHA256SUMS
```

Owned artifacts are `plan.md`, `checkpoint.md`, `halfway_checkpoint.md`,
`audit_notes.md`, `independent_gain_audit.py`, `independent_results.json`,
this report, `freeze_manifest.md`, and `SHA256SUMS`. No M175, predecessor,
coordinator, manuscript, skill, or other mission file was modified. No cache
is retained.

```text
ACCEPT M175'S EXACT REALIZABLE GAIN-GRAPH/CYCLE-SPACE THEOREM.
ACCEPT ITS FIXED-PHYSICAL-ENDPOINT AFFINE COLUMN-SPACE TEST.
ACCEPT THE d4 FOUR-MOVE NONZERO-VOLTAGE CERTIFICATE AS A FINITE WARNING.
LEAVE d>=5 CHORD RANK, DPS MEMBERSHIP, ALL LENGTHS, GAPS, AND TERMINALS OPEN.
```
