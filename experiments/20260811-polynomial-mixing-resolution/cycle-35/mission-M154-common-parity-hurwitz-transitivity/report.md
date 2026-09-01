# M154 final report: inner-Nielsen and parity-voltage reduction

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and exact scope

```text
FINAL VERDICT: KEEP AS A PROVED STRICT REDUCTION WITH EXACT LOW-RANK
OBSTRUCTIONS.

PROVED universally: every inner conjugation by the factor-generated group
is realized by an explicit literal signed braid.

PROVED for every d>=5 M135 matching subfamily: literal common-braid
equivalence is exactly inner P_(d,s)-Nielsen equivalence, and equivalently
absolute quotient routing plus zero parity voltage.

EXACT at d=3: the framed generating-pair space has two literal braid orbits,
distinguished by relative parity framing.

EXACT at d=4: the quotient action is imprimitive with 40 blocks of size 3,
exactly the fibers of S_4 -> S_4/V_4 ~= S_3; this invariant detects the
accepted M135 rank-four pair witness.

UNRESOLVED for d>=5: quotient/voltage routing, short transporter correction,
the broad one-orbit theorem, and polynomial braid length.
```

This mission does not prove a simultaneous braid for an M135 matching, a
minimal-sector gap, or a terminal outcome.

```text
candidate                  | inner-Nielsen / absolute parity-voltage routing
claimed target             | generating product-one C_(d,s)-factorizations
identity ok                | Hurwitz and conjugation preserve product one
crosses Hurwitz components | not applicable; this classifies action orbits
exact diagnostics          | complete d3; d4 Schreier--Sims/DPS; capped d5 quotient
verdict                    | keep strict reduction and exceptional obstructions
```

## Field 2 — target, action, and the three quotients

For `d>=3`, `m=2d-2`, the physical auxiliary target is uniform on

```text
Z_d={(t_1,...,t_m):t_1...t_m=id,
                         support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. The chronological moves are

```text
R_j(a,b)=(b,b^(-1)ab),
R_j^(-1)(a,b)=(aba^(-1),a).
```

The literal action does not include simultaneous conjugation. The proof
separates:

1. literal framed braid orbits;
2. the inner quotient by simultaneous `P_(d,s)` conjugation;
3. the absolute coordinate quotient by `S_d^s`, with residual deck group
   `S_d^s/P_(d,s) ~= F_2^s/Delta`.

Conflating items 2 and 3 is precisely the framing error exposed at rank
three.

## Field 3 — explicit inner-conjugation braid

For any product-one group factorization `X=(x_1,...,x_m)`, chronologically
apply

```text
R_(m-1),...,R_1,R_1,...,R_(m-1).
```

The descending half gives

```text
(x_m,x_m^(-1)x_1x_m,...,x_m^(-1)x_(m-1)x_m),
```

and the ascending half returns `x_m` to the end. The product-one equation
makes the final conjugator simplify exactly, so the output is

```text
x_m^(-1) X x_m.
```

To use original factor `x_i`, inverse-Hurwitz it unchanged to the last slot,
apply this loop, and undo the transport. The resulting braid has length at
most `4m-4`. Concatenating along a length-`ell` expression for
`p in <x_1,...,x_m>` realizes `p^(-1)Xp` with length at most

```text
(4m-4)ell.
```

Thus literal orbit equivalence and braid equivalence modulo simultaneous
inner conjugation coincide on generating product-one tuples. This is
**PROVED** in `inner_nielsen_voltage_reduction.md` without a literature
input.

The quantitative caveat is essential: generation does not bound `ell`.

## Field 4 — exact application to M135/M141

For a nonempty subfamily `I` of an M135 matching, align its physical source
and target factors as

```text
X_j=(u_j^q)_(q in I),       Y_j=(v_j^q)_(q in I).
```

Accepted M141/M143 gives, for every `d>=5`,

```text
<X_1,...,X_m>=<Y_1,...,Y_m>=P_(d,|I|).
```

The explicit loop therefore upgrades any inner `P_(d,|I|)`-Nielsen
equivalence to a literal common braid. In particular, a connected-Hurwitz
classification stated modulo inner conjugacy would suffice qualitatively;
one stated modulo all coordinatewise relabelings would not.

No polynomial braid bound follows: the remaining inner transporter still
needs a polynomial aligned-generator word.

## Field 5 — exact absolute quotient-voltage criterion

Let `Q_d=Z_d/S_d`. Global conjugation is free for `d>=3`. If a braid `b`
maps each source class `[u^q]` to its target class `[v^q]`, there is a unique
transporter `rho_q in S_d` satisfying

```text
b.u^q=rho_q.v^q.
```

Its relative voltage is the transporter parity vector modulo the diagonal:

```text
epsilon_b=(sgn(rho_1),...,sgn(rho_s)) mod Delta
             in F_2^s/Delta.
```

When the aligned target factors generate `P_(d,s)`, a literal common braid
exists **if and only if** some quotient braid maps every ordered source to
its target and has `epsilon_b=0`. Zero voltage places the transporter tuple
inside `P_(d,s)`; the loop from Field 3 then removes it.

If the quotient word has length `L` and the transporter has aligned word
length `ell`, the constructed literal word has length at most

```text
L+(4m-4)ell.
```

The trivial centralizer makes voltage well-defined. It does not prove that
every quotient stabilizer has zero voltage.

## Field 6 — complete rank-three framing split

Independent exact closure reconstructs `|Z_3|=24`, four free global orbits,
and literal action image order `216`. The quotient image has order `12` and
is `A_4` on four points.

All `432=4*3*6^2` ordered physical pairs from distinct global classes
generate `P_(3,2)`. They split into exactly two literal diagonal-braid orbits
of size `216`. From one representative, even/even and odd/odd coordinate
conjugates are reachable, whereas even/odd and odd/even are not. The two
orbits are exactly the two classes in `S_3^2/P_(3,2)`.

This **refutes framed one-orbit transitivity at `d=3`**, outside the assigned
`d>=5` range, and proves that absolute quotient transitivity alone is
insufficient.

Every one of the twelve quotient actions has exactly two parity-voltage
vectors in the framed action. The positive quotient generators have cycle
shape `1^1 3^1` and are even.

## Field 7 — exact rank-four exceptional quotient

The exceptional map `pi:S_4->S_3` is the action on the three perfect
matchings of `K_4`; its kernel is `V_4`. Every transposition maps to a
transposition, so factorwise projection is product- and Hurwitz-equivariant.
It defines

```text
Phi:Q_4 -> Q_(3,6).
```

The exact clean-room reconstruction finds `120` source classes, `40` target
classes, and fibers of size three. Independent Schreier--Sims gives the
degree-120 quotient image

```text
order      20652142670561646642588549120 = 2^22*3^44*5
transitive true
primitive  false
subdegrees [1,2,36,81]
blocks     40 of size 3.
```

The computational minimal blocks equal the `Phi` fibers literally. Thus the
all-rank quotient-alternating-image proposal is **refuted at `d=4`**.

For the accepted M135 rank-four pair witness, both source words have the
same `Phi` value while the two target words have different values. Equality
of `Phi` values is preserved by a common braid, so this is an exact common-
braid obstruction. It algebraically explains the same `V_4` exception for
which M135 already uses singleton classes; it gives no `d>=5` obstruction.

Across one independently reconstructed deterministic Hall decomposition,
only two of twenty matching-color maps preserve the entire block relation.
This finite calibration is not promoted beyond rank four.

## Field 8 — tightly capped rank-five check

At `d=5`, quotient BFS reaches all

```text
5^2*8!/5! = 8400
```

accepted DPS quotient states. The seven positive generators are even, with
cycle shape

```text
1^660 2^1440 3^1620,
```

and generate a transitive, primitive degree-8400 group. The group order was
deliberately not computed. These are **EXACT FINITE** facts and do not prove
an alternating image, high transitivity, or an asymptotic theorem.

The bounded quotient summary is:

| `d` | degree | transitive | primitive | positive generators even |
|---:|---:|:---:|:---:|:---:|
| 3 | 4 | yes | yes | yes |
| 4 | 120 | yes | no | yes |
| 5 | 8,400 | yes | yes | yes |

## Field 9 — strict remaining lemma

The new first unproved step is **POLYNOMIAL MATCHING QUOTIENT-VOLTAGE
ROUTING**:

> For `d>=5`, refine every M135 perfect matching into at most `d^C` total
> subfamilies. For each subfamily, find a braid of length at most `d^C` that
> maps its ordered source classes in `Q_d` to their matched targets, has zero
> relative parity voltage, and leaves a transporter of aligned-generator word
> length at most `d^C`.

This is a strict, falsifiable replacement of the abstract action-coset
intersection. Quotient routing, parity voltage, and short inner correction
are now separate obligations.

The candidate `image(B_m on Q_d)=Alt(Q_d)` for `d>=5` is unresolved. The
exact primitive even `d=5` image is consistent with it, while `d=4` refutes
the all-rank extension. Even the candidate theorem would not supply zero
voltage or a polynomial braid diameter.

No Conway--Parker or other classification is invoked. Any future use must
check literal versus inner versus absolute conventions, stable range, class
and generation hypotheses, and effective word length.

## Field 10 — dependencies, reproduction, and hygiene

Accepted inputs are M135/M137's incidence construction, M141/M143's
common-parity generation theorem, M146/M148's factor-class collapse, and
M150/M153's constant reduced Pin descriptor. The inner-conjugation and
voltage theorems are self-contained here.

Deterministic reproduction from this directory, Python `3.12.3`, SymPy
`1.12`, `seed=null`:

```text
python3 -c 'from pathlib import Path; [compile(Path(f).read_text(),f,"exec") for f in ("hurwitz_framing_audit.py","d4_exceptional_block_audit.py")]; print("compile ok")'
python3 -B hurwitz_framing_audit.py --output results.json
python3 -B d4_exceptional_block_audit.py
python3 -c 'import json; q=json.load(open("results.json")); assert q["d3"]["generating_ordered_pair_orbit_sizes"]==[216,216]; assert [(r["d"],r["transitive"],r["primitive"],r["all_positive_generators_even"]) for r in q["quotient_components"]]==[(3,True,True,True),(4,True,False,True),(5,True,True,True)]; r=json.load(open("d4_results.json"))["d4"]; assert r["sympy_blocks_equal_S4_mod_V4_fibers"] and r["accepted_M135_rank4_witness"]["therefore_common_literal_braid_obstructed"]; print("assertions ok")'
sha256sum -c SHA256SUMS
```

The checkers import no predecessor module or output. They record predecessor
report hashes read-only for provenance. Owned artifacts are `plan.md`,
`checkpoint.md`, `inner_nielsen_voltage_reduction.md`,
`hurwitz_framing_audit.py`, `results.json`,
`d4_exceptional_block_audit.py`, `d4_results.json`, this report,
`freeze_manifest.md`, and `SHA256SUMS`.

No predecessor, coordinator, manuscript, skill, or file outside this mission
directory was edited. No cache directory is part of the freeze.

```text
KEEP THE INNER-CONJUGATION AND QUOTIENT-VOLTAGE THEOREMS.
KEEP THE d3 FRAMING SPLIT AND d4 EXCEPTIONAL BLOCK AS EXACT WARNINGS.
DO NOT INFER THE d>=5 ONE-ORBIT THEOREM, A POLYNOMIAL BRAID, OR A GAP.
```

