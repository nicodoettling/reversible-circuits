# M181 final report: an actual-matching full-rank family

Date: 2026-08-13 UTC.  Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and exact scope

```text
FINAL VERDICT: KEEP AS A STRICTLY NARROWER PROVED REALIZATION LEMMA.

PROVED: for every d>=5, every M135 perfect-matching color, and every
1<=s<=1+floor((d-1)/3), the color contains an accepted source subfamily
whose actual Schreier chord-gain space is W_s, of rank s-1.

PROVED, CONDITIONALLY ON A QUOTIENT ROUTE: every required fixed-physical-
endpoint tree offset for that subfamily lies in the chord space.

UNRESOLVED: arbitrary accepted matching subfamilies and existence of the
source-to-matched-target quotient route, including for the explicit family.
```

This is a nontrivial positive instance of L-0259's first open structural
step.  It does not settle the universal accepted-matching chord-rank lemma.

```text
candidate                  | anchored local closed-braid block family
claimed target             | qualitative synchronized relative-orientation lift
identity ok                | exact product one, connected, length 2d-2
crosses Hurwitz components | no inference; source stabilizer loops only
exact diagnostics          | one B6 relation, embeddings d=5,...,13
verdict                    | keep narrow all-d theorem; universal step open
```

No physical gap, mixing bound, or Terminal conclusion is claimed.

## Field 2 — target, conventions, and immutable dependencies

The auxiliary target is diagonal signed-Hurwitz orbit lifting on

```text
Z_d={(t_1,...,t_(2d-2)):t_1...t_(2d-2)=id,
                              support connected on [d]},
Q_d=Z_d/S_d,
W_s=F_2^s/<(1,...,1)>.
```

Permutations compose as `(p q)(x)=p(q(x))`; factors and signed generators
are applied chronologically left-to-right, with

```text
R_j(a,b)=(b,b^(-1)ab),       R_j^(-1)(a,b)=(aba^(-1),a).
```

There is no probability distribution or Markov kernel in this structural
mission.  All fourteen assigned immutable manifests passed before use:
M135/M137, M141/M143, M146/M148, M154/M158, M163/M164, M169/M172, and
M175/M176.  No disagreement was found.

The accepted chain supplies: M135's `H`-orbit-edge/global-orbit-vertex
perfect matchings; M141's aligned `P_(d,s)` group; M154's literal inner
conjugation loops; M169's monodromy exact sequence; and M175's exact
Schreier-cycle column space and affine endpoint test.

## Field 3 — the anchored local closed-braid generator

In zero-based labels, start with the M175 pair

```text
U=(01)^2(02)^2(03)^2,       V=(01)^2(02)^2(13)^2.
```

The chronological braid `(4,3,5,4)` has transporters `(23)` on `U` and
`(01)(23)` on `V`.  The latter is even but moves the shared anchor.

At the resulting aligned pair, the factor-position expression

```text
(1,3,1,3,5,3,5,3,5,1,3,1)
```

evaluates to `(id,(01)(23))`.  Applying M154 elementary factor-conjugation
words in reverse expression order removes that transporter.  The resulting
literal `B_6` word has 200 moves and satisfies

```text
h U=(23).U,                 h V=V.                   (3.1)
```

Both transporters fix anchor `0`.  Under any relabeling
`0,1,2,3 -> 0,a,b,c`, (3.1) becomes

```text
U(a,b,c)=(0a)^2(0b)^2(0c)^2  ->  (b c).U(a,b,c),
V(a,b,c)=(0a)^2(0b)^2(ac)^2  ->  V(a,b,c).           (3.2)
```

This is a literal local relation, not an abstract tuple-group element.

## Field 4 — minimal connected embedding on all d labels

Put `r=floor((d-1)/3)`.  Use `r` disjoint triples of nonanchor labels,
all sharing anchor `0`, and choose independently the `U` or `V` pattern
in each six-factor block.  For each of the remaining
`d-1-3r` labels, append a doubled star edge `(0x)^2`.

Every block and filler has product identity.  Every label lies in the
connected component of `0`, including the `c`-label of a `V`-block
through its edge `(ac)`.  The total length is exactly

```text
6r+2(d-1-3r)=2d-2.
```

Thus every constructed word lies in the actual minimal connected sector
`Z_d`.  Shifting (3.2) to one six-position block does not touch any other
factor.  Its odd swap fixes the anchor, every other block, and every filler
edge.  Hence the embedded endpoint is a global relabeling of the **entire**
word; no disconnected or moving filler is hidden.

## Field 5 — literal voltage basis and exact chord rank

For `1<=s<=r+1`, use the binary block patterns

```text
0,e_1,...,e_(s-1).
```

They give pairwise distinct points of `Q_d`.  At a block where two patterns
differ, the first two distinct local edges force any positionwise relabeler
to fix `0,a,b`; it then cannot map the last edge `{0,c}` to `{a,c}`.

For each `k=1,...,s-1`, the shifted local braid is a closed synchronized
walk on this tuple.  Its transporter-sign vector has representative `e_k`
with zero in tuple coordinate zero.  These `s-1` classes are independent
modulo the diagonal and form a basis of `W_s`.  Therefore

```text
V_stab=W_s,       dim V_stab=s-1.                    (5.1)
```

M175 identifies (5.1) with the span and rank of the **actual realizable**
Schreier fundamental-cycle columns.  The explicit loops prove inclusion of
the basis in `V_stab`; dimension of `W_s` proves equality.

The discarded symmetry shortcut would not prove this.  M135 supplies no
coordinate-permutation action on a fixed ordered tuple.  Moreover,
connected-graph vectors `e_i+e_j` span the even-weight space `E`; when
`s` is even, `Delta<=E` and their image `E/Delta` has dimension `s-2`,
not `s-1`.  At `s=2` the sole edge vector is the zero diagonal class.
The single-coordinate generators above work for both parities of `s`.

## Field 6 — exact M135 matching inclusion and representative audit

Fix an adjacent DPS edit and one M135 perfect-matching color.  The color has
exactly one `H`-orbit edge `Q_c` over each left global orbit
`[W_c] in Q_d`.  Selecting the edges over the constructed pairwise
distinct quotient vertices gives an actual matching subfamily; their right
endpoints are distinct by perfectness.

The color need not contain the literal word `W_c`.  Choose any physical
`u_c in Q_c`.  There is an arbitrary `alpha_c in G`, not necessarily in
`H`, with `u_c=alpha_c.W_c`.  Since braid action commutes with relabeling,

```text
h_k u_c=(alpha_c delta_(c,k) alpha_c^(-1)).u_c.
```

The sign equals that of `delta_(c,k)`.  Hence the same synchronized local
word realizes the voltage basis on the actual representatives of the
selected matching edges.  The conjugated odd transporter need not fix the
M135 white root; M169's quotient-stabilizer monodromy explicitly permits
that motion and records its orientation.

This proves the theorem for every perfect-matching color, not merely for
some abstract tuple family or a specially chosen color.

## Field 7 — fixed endpoints, M169, and the exact unresolved step

For selected representatives `U=(u_c)`, take their physical DPS targets
`V=(tau_i(u_c))` and quotient tuples `q,r`.  If `r` lies in the actual
synchronized component `Gamma(q)`, every fixed-endpoint tree offset
`a_T(U,V)` is an element of `W_s`; (5.1) therefore gives

```text
a_T(U,V) in V_stab(q)=colspan(z_T).
```

M175's affine theorem then gives a zero-relative-voltage route.  Section and
endpoint-lift changes add the accepted coboundaries and leave this physical
membership statement invariant.

M169's accepted exact sequence becomes

```text
1 -> P_(d,s) -> K_mon(q) -> W_s -> 1,
```

so the source monodromy is `K_mon(q)=S_d^s`.  This does not establish
`r in Gamma(q)`.  The first remaining obligations are therefore:

1. prove or refute full chord rank and endpoint membership for arbitrary
   accepted matching subfamilies;
2. prove a synchronized quotient route for the constructed source/target
   family before asking for any quantitative length bound.

No qualitative connectivity is inferred from full voltage.

## Field 8 — minimal symbolic audit, reproduction, and hygiene

The standard-library checker imports no predecessor code or result and does
not enumerate `Q_5` or any quotient component.  It directly verifies:

```text
base transporters              (23), (01)(23)
inner correction product       id, (01)(23)
correction / total moves        196 / 200
final transporter signs         1,0
both transporters fix anchor    yes
elementary-relation failures    none
```

It also embeds the relation directly for `d=5,...,13`.  Every tested word
has product one, connected all-label support, and length `2d-2`; every
shifted relation has the claimed endpoint.  The resulting basis
representatives have widths `2,2,3,3,3,4,4,4,5`.  These finite rows audit
conventions only; the all-`d` result is the proof in `proof.md`.

Deterministic reproduction, Python `3.12.3`, dependencies `{}`, seed
`null`:

```text
python3 -B local_block_voltage.py
python3 -c 'from pathlib import Path; p=Path("local_block_voltage.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
```

Owned artifacts are `plan.md`, `checkpoint.md`, `halfway_checkpoint.md`,
`proof.md`, `local_block_voltage.py`, `results.json`, this report,
`freeze_manifest.md`, and `SHA256SUMS`.  No predecessor, coordinator,
manuscript, skill, or file outside this mission directory is edited.

## Field 9 — final decision and audit request

```text
KEEP THE EXPLICIT ACTUAL-MATCHING FULL-RANK FAMILY.
KEEP ENDPOINT MEMBERSHIP CONDITIONAL ON QUOTIENT-ROUTE EXISTENCE.
DO NOT PROMOTE TO EVERY ACCEPTED MATCHING SUBFAMILY.
```

The theorem disproves any universal zero-voltage invariant for accepted
`d>=5` matchings and gives full rank at widths
`s<=1+floor((d-1)/3)` inside every matching color.  It leaves the universal
L-0259 step and the selected matched-target quotient route unresolved.

A fresh immutable referee should independently check the 200-move anchored
relation, the all-label minimal embedding, the matching-edge versus
physical-representative argument, the basis modulo `Delta` for even and odd
`s`, and the conditional endpoint/M169 interface.  No polynomial word
length, gap, mixing, or Terminal claim should be audited into existence.
