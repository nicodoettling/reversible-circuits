# M158 fresh referee report on frozen M154

Date: 2026-08-13 UTC. Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — decision, objections, and exact scope

```text
FINAL DECISION: ACCEPT M154 AT ITS EXACT NONTERMINAL SCOPE.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

M154 correctly proves the universal inner-conjugation braid, its application
to accepted `d>=5` M135 matching subfamilies, and the exact absolute-quotient
zero-parity-voltage criterion. The quantitative result retains the necessary
aligned-generator word-length parameter. The complete `d=3` framing split,
the `d=4` exceptional block/witness, and the capped `d=5` quotient facts were
independently reproduced.

```text
candidate                  | inner-Nielsen / parity-voltage routing reduction
claimed target             | product-one generating C_(d,s)-factorizations
identity ok                | Hurwitz and simultaneous conjugation preserve it
crosses Hurwitz components | not applicable; this is an orbit classification
exact diagnostics          | complete d3; bounded d4; capped d5 primitivity
verdict                    | accept strict reduction and finite warnings only
```

No common M135 braid, polynomial braid length, quotient alternating-image
theorem, physical-sector gap, original `{3,4,5}` heat-bath gap, Terminal A,
or Terminal B conclusion follows.

## Field 2 — immutable provenance

All assigned SHA-256 values matched before the proof or computational audit.
No frozen payload was executed or modified.

| frozen M154 artifact | observed SHA-256 |
|---|---|
| `report.md` | `6421f55bccf2c6750f21a7cf9a236f8811c06f5759170d4ca3acae79c9b5d806` |
| `inner_nielsen_voltage_reduction.md` | `e689fec00762b773d56030640aff7af21053cb63901c47571e3c9b33ce48d958` |
| `hurwitz_framing_audit.py` | `0292268cbad8c0c322c440f4ca6596ebfcc3fd3e5b94c500f616859c208dccfc` |
| `results.json` | `13ee821c42f01cc040f4c9a335b6e2acbf38522834e83195dca17a895246f1be` |
| `d4_exceptional_block_audit.py` | `e5cf3ff0d660b5a5e62325c87c8a7c40f4b3a1639d95dd787435f97353947a68` |
| `d4_results.json` | `9d55fb82af30ccfcfc0a39e63c41a77c05518cc79888249678ffbed8183e3cfa` |
| `freeze_manifest.md` | `7adf2270a89ab870335417305ba5db6fb577ded29721a30dc38234eea07b07fa` |
| `SHA256SUMS` | `b5c7273819a6d247836dc596723efb438cb91ae310ced670ad57738a3bb0ba04` |

## Field 3 — target, convention, and accepted dependencies

The physical auxiliary target is uniform on

```text
Z_d={(t_1,...,t_(2d-2)): t_1...t_(2d-2)=id,
                              support connected on [d]}.
```

The orbit theorem packages `s` words into a product-one generating
`C_(d,s)`-factorization. Permutations compose as
`(pq)(x)=p(q(x))`; displayed factors multiply left-to-right. Chronological
right-Hurwitz moves are

```text
R_j(a,b)=(b,b^(-1)ab),
R_j^(-1)(a,b)=(aba^(-1),a).
```

The only external mathematical input used in the `d>=5` application is the
accepted M141/M143 equality of both aligned generated groups with

```text
P_(d,s)={(g_1,...,g_s):sgn(g_1)=...=sgn(g_s)}.
```

M135/M137 supplies the matching setting and accepted rank-four witness. The
inner-conjugation and parity-voltage arguments are self-contained and invoke
no unverified literature classification.

## Field 4 — universal inner-conjugation braid

Let `X=(x_1,...,x_m)` have product one. The descending chronological pass

```text
R_(m-1),...,R_1
```

moves `x_m` to the first slot and conjugates every preceding factor by
`x_m`. The ascending pass `R_1,...,R_(m-1)` moves it back. The product of
the intervening conjugated factors is `x_m^(-1)`, so the final tuple is

```text
x_m^(-1) X x_m.
```

To use the original factor `x_i`, inverse-Hurwitz moves carry it unchanged
to the final slot. Undoing that transport after the loop is valid because
Hurwitz moves commute with simultaneous conjugation. The exact elementary
length is

```text
2(m-i)+2(m-1) <= 4m-4
```

when slots are numbered from one. The inverse braid gives conjugation in the
opposite direction. Applying these elementary words in the order appropriate
to a length-`ell` symmetric-generator expression gives the claimed
`(4m-4)ell` bound for every element of the factor-generated group.

The clean-room checker verified both braid orientations for all `96`
factor choices in the `24` physical `d=3` words and checked the same formula
on a general product-one `S_4` tuple containing a non-involutive 3-cycle.
There were zero failures. The proof, rather than these finite tests, establishes
the universal statement.

It follows correctly that literal signed-Hurwitz equivalence equals braid
equivalence modulo simultaneous conjugation by the generated group. The
converse lift uses the theorem on the conjugated endpoint; no ambient
normalizer or independent coordinate relabeling is silently inserted.

## Field 5 — aligned application and exact voltage criterion

For every nonempty `d>=5` subfamily of one M135 matching, M141/M143 gives
literal generation of the same `P_(d,s)` at source and target. Therefore an
inner `P_(d,s)`-Nielsen equivalence lifts to a literal common braid.

The absolute quotient is handled correctly. Global `S_d` conjugation acts
freely on each connected word: a stabilizer centralizes every factor, hence
the generated `S_d`, whose center is trivial for `d>=3`. Thus a quotient
braid has unique coordinate transporters `rho_q`. Moreover,

```text
S_d^s/P_(d,s) ~= F_2^s/Delta,
Delta={(e,...,e)}.
```

The relative parity voltage vanishes exactly when all transporter parities
agree, equivalently when `rho=(rho_1,...,rho_s)` lies in `P_(d,s)`. In that
case the universal inner-conjugation braid removes `rho`; a literal braid
gives the zero-voltage quotient braid in the reverse direction. This proves
the stated if-and-only-if criterion.

The length clause is both correct and essential:

```text
literal length <= L+(4m-4)ell,
```

where `L` is quotient-braid length and `ell` is transporter word length in
the aligned factors after that braid. M141 proves generation, not a polynomial
bound on `ell`. M154 does not conceal this remaining obligation.

## Field 6 — complete rank-three framing split

The independent checker reconstructed all `24` words in `Z_3`, four free
global classes of size six, physical action-image order `216`, and quotient
image order `12`. Every quotient generator is even on four points, so the
quotient image is `A_4`. Its orbit on ordered distinct quotient points has
all `12` points.

The `432` ordered physical pairs from distinct absolute classes split into
two literal diagonal-braid orbits of sizes `216,216`. Within one fixed
absolute ordered pair, the complete `36` coordinate-conjugation fiber has:

| transporter parity | total | reachable |
|---|---:|---:|
| even/even | 9 | 9 |
| even/odd | 9 | 0 |
| odd/even | 9 | 0 |
| odd/odd | 9 | 9 |

Together with quotient ordered-pair transitivity, this identifies the two
literal orbits exactly with the two relative framing classes in
`S_3^2/P_(3,2)`. It proves the stated low-rank warning and does not refute
the assigned `d>=5` frontier.

## Field 7 — exact rank-four exceptional block and witness

The clean-room computation first reconstructed the action
`pi:S_4->S_3` on the three perfect matchings of `K_4`. Exhaustive checking
over `S_4^2` gave zero homomorphism failures, image order six, and kernel
order four consisting of the identity and the three double transpositions,
namely `V_4`. Each `S_3` transposition has exactly two transposition lifts.

Factorwise projection preserves product and Hurwitz moves. A projected
length-six word is connected: if all projected factors were one
transposition, all original factors would lie in the corresponding pair of
disjoint `S_4` edges, contradicting connected support. Direct enumeration
gave zero product or connectedness failures and

```text
|Z_4/S_4|=120,       |Z_(3,6)/S_3|=40,
40 Phi-fibers, each of size 3.
```

Bounded degree-`120` Schreier--Sims reproduced the transitive imprimitive
image of order

```text
20652142670561646642588549120 = 2^22*3^44*5,
```

with subdegrees `[1,2,36,81]`. Its computed minimal block partition was
literally the forty `Phi` fibers, and every generator mapped each such fiber
to another with zero failures.

For the accepted M135 witness, all four words were independently verified to
be connected identity words. Reconstructing the plus-mirror DPS definition
gave exactly four rooted preimages for each source and a unique root-independent
`tau_1` target equal to the declared target. Both source and target pairs are
nonconjugate. Their paired subgroup orders are independently `96` and `288`.
The sources have equal `Phi` value while the targets do not. Because one
common braid preserves equality of `Phi` values, the claimed literal common-
braid obstruction follows exactly.

## Field 8 — tightly capped rank-five check

Signed quotient BFS reached exactly `8,400` states, the accepted DPS quotient
count. The seven positive generators have common cycle shape

```text
1^660 2^1440 3^1620
```

and are even. The resulting degree-`8,400` action is transitive and
primitive. The checker did not compute its order or enumerate its elements.
These are exact finite facts only: they establish neither an alternating
image nor any all-rank or polynomial-diameter theorem.

## Field 9 — remaining obligation, reproduction, and hygiene

The surviving statement remains M154's **POLYNOMIAL MATCHING
QUOTIENT-VOLTAGE ROUTING**: polynomially refine each `d>=5` matching, find
short quotient braids with zero relative voltage, and polynomially bound the
remaining aligned transporter length. This is unresolved.

Deterministic reproduction from this mission directory, Python `3.12.3`,
SymPy `1.12`, `seed=null`:

```text
python3 -B -c 'from pathlib import Path; compile(Path("independent_referee.py").read_text(), "independent_referee.py", "exec"); print("compile ok")'
python3 -B independent_referee.py
```

The checker imports no M154 or predecessor code or data. It reads only the
assigned frozen payload bytes for SHA-256 verification. Rank five is capped
as stated and no broad group closure is attempted.

Owned artifacts are `plan.md`, `checkpoint.md`, `independent_referee.py`,
`independent_results.json`, this report, `freeze_manifest.md`, and
`SHA256SUMS`. No M154, predecessor, coordinator, manuscript, skill, or other
mission file is edited.

```text
ACCEPT. ZERO MATERIAL NUMBERED OBJECTIONS.
PROMOTE THE INNER-NIELSEN AND EXACT ZERO-VOLTAGE REDUCTIONS ONLY.
KEEP d3/d4 AS EXCEPTIONAL WARNINGS AND d5 AS CAPPED FINITE CALIBRATION.
```
