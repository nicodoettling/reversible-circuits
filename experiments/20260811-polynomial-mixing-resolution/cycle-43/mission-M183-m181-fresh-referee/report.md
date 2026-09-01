# M183 fresh referee report on frozen M181

Date: 2026-08-13 UTC.  Audited repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and exact scope

```text
ACCEPT M181 AT ITS STATED STRICTLY NARROWER SCOPE.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

M181 correctly proves that, for every `d>=5`, every M135 perfect-matching
color, and every `1<=s<=1+floor((d-1)/3)`, the color contains an accepted
source subfamily with

```text
V_stab=W_s,       actual Schreier chord rank=s-1.
```

It correctly makes physical endpoint membership conditional on the matched
target quotient tuple being in the source synchronized component.  It does
not prove the universal arbitrary-subfamily rank lemma or that conditional
quotient route.

```text
candidate                  | anchored local closed-braid block family
claimed target             | qualitative synchronized orientation lift
identity ok                | proved; clean-room boundary checks pass
crosses Hurwitz components | no inference; source stabilizer loops only
exact diagnostics          | core B6 replay and d=5,7,10 embeddings
verdict                    | accept narrow theorem; universal step open
```

No word-length theorem, physical gap, mixing bound, or Terminal conclusion is
accepted or implied.

## Field 2 — frozen provenance and exact hashes

The complete M181 `SHA256SUMS` gate passed before any payload was read.
Observed payload hashes are:

| Frozen M181 artifact | SHA-256 |
|---|---|
| `plan.md` | `4da9df3c9c7e0b579fc0e514f1bebc28cd83cdca40a1948909ca416b589f23f3` |
| `checkpoint.md` | `360d107043983bd5aa19f0e203def2de68c69aa7a4fd2fd28ea02462e490f163` |
| `halfway_checkpoint.md` | `652e408dc30f35e943348db762acc231672a48f7c41b27536987d6172e3234df` |
| `proof.md` | `f63ba5480a9dd5660e3c31de576e77cd28c55c1bccf387a219eb0b3346c05bbc` |
| `local_block_voltage.py` | `a10ba39a3391d3233711b9106eba48430182c203b9457cb3922896b47ac8f5d6` |
| `results.json` | `b6135f96d7e2adceb69e2449b4b7b95c4175d6c51c3a3ea4968a70e1be3338e5` |
| `report.md` | `03162d44f56ec72d40752d8df249b1b0233f53455289504fad1050ebf778338e` |
| `freeze_manifest.md` | `2a32e71f589f60d28efa215587ef94662ef94c2070b745a7a62d43848b6387bb` |

The top-level digest is

```text
d2ae8d5a2af347eb74943db1221607d46fc706296ac2802d97abc0a024ec20b0  SHA256SUMS
```

The freeze manifest agrees with the payload and claim boundary.  M181 was
never edited.

## Field 3 — target, convention, and accepted interfaces

For `d>=5`, `m=2d-2`, the auxiliary target is diagonal signed-Hurwitz
orbit lifting on

```text
Z_d={(t_1,...,t_m):t_1...t_m=id, support connected on [d]},
Q_d=Z_d/S_d,       W_s=F_2^s/Delta,
Delta=<(1,...,1)>.
```

Permutations compose as `(p q)(x)=p(q(x))`; factors and signed braid symbols
are applied chronologically left-to-right.  The moves are

```text
R_j(a,b)=(b,b^(-1)ab),       R_j^(-1)(a,b)=(aba^(-1),a).
```

The audited interfaces agree exactly with the accepted chain:

- M135 edges are `H`-orbits, their left/right vertices are global `G`-orbits,
  and each color is a perfect matching.
- M154's elementary word gives literal factor conjugation.
- M169 gives
  `K_mon=relative_sign^(-1)(V_stab)` for accepted `d>=5` matching
  subfamilies.
- M175 identifies `V_stab` with the actual realizable fundamental-cycle
  column space and makes endpoint zero routing an affine membership test.

No probability distribution or Markov kernel is involved in this theorem.

## Field 4 — independent audit of the 200-move relation

The fresh checker reimplements permutation arithmetic and both signed
Hurwitz moves without importing M181.  It reconstructs

```text
U=(01)^2(02)^2(03)^2,       V=(01)^2(02)^2(13)^2
```

and independently recovers the four-move transporters `(23)` and
`(01)(23)`.  At the post-base pair, the displayed position expression

```text
(1,3,1,3,5,3,5,3,5,1,3,1)
```

multiplies to `(id,(01)(23))`.

All twelve combinations of two coordinates and six factor positions pass a
direct check of the elementary formula `E_j X=x_j^(-1)Xx_j`.  Applying the
elementary words in reverse expression order passes all twenty-four
coordinate-prefix identities: the accumulated state is exactly
`q^(-1)Xq` after every prefix.  The correction length is `196`, the full
relation length is `200`, and its final transporters are

```text
(23), id;       signs 1,0;       anchor 0 fixed in both.
```

The independently reconstructed chronological relation has compact JSON
digest

```text
32f90842f682615a72def42e0f940d9125a719ed8b38e9375fe1d81fa5e50629
```

which matches the literal relation frozen in M181.

## Field 5 — minimal all-label embedding and quotient separation

For `r=floor((d-1)/3)` and `t=d-1-3r`, M181 concatenates `r` six-factor
blocks and `t` doubled star fillers.  Each block and filler is a product-one
adjacent double.  The support is connected: a `U` block attaches all three
labels to the anchor, a `V` block attaches its third label through `a`, and
every filler attaches to the anchor.  The exact length is

```text
6r+2t=2d-2.
```

A shifted relation uses only the five braid generators internal to its block.
Its odd swap fixes the anchor, all other block labels, and every filler.  The
claimed endpoint is therefore a relabeling of the entire minimal connected
word, not merely of an isolated six-factor tuple.

The all-`d` nonconjugacy proof is valid.  At a differing block, equality of
the first and third factor positions forces a relabeler to fix `0,a,b`, after
which it cannot map `{0,c}` to `{a,c}`.  Positionwise word equality prevents
block permutation.  The fresh exhaustive `d=5,7` checks agree.

Boundary replay stayed deliberately small:

| `d` | blocks | width | fillers | length | literal endpoints / equivariance |
|---:|---:|---:|---:|---:|---:|
| 5 | 1 | 2 | 1 | 8 | 2 / 2 |
| 7 | 2 | 3 | 0 | 12 | 6 / 6 |
| 10 | 3 | 4 | 0 | 18 | 12 / 12 |

Every row passed identity, all-label connectedness, outside-block fixation,
and the displayed endpoint.  No quotient component was enumerated.

## Field 6 — voltage basis and the even-width issue

On patterns `0,e_1,...,e_(s-1)`, the `k`th shifted relation has a sign
representative with zero in tuple coordinate zero and one only in coordinate
`k`.  A linear combination cannot equal the nonzero diagonal because its
coordinate zero remains zero.  These `s-1` classes are independent and hence
form a basis of `W_s`, for even and odd `s` alike.

Fresh binary ranks for `s=2,...,6` are:

| `s` | `dim W_s` | single-coordinate rank | connected-path edge rank |
|---:|---:|---:|---:|
| 2 | 1 | 1 | 0 |
| 3 | 2 | 2 | 2 |
| 4 | 3 | 3 | 2 |
| 5 | 4 | 4 | 4 |
| 6 | 5 | 5 | 4 |

M181's parity warning is exact.  Connected-graph edge vectors span the
even-weight space `E`; for even `s`, `Delta<=E`, so their image `E/Delta`
has dimension `s-2`, not `s-1`.  In particular the `s=2` edge vector is the
zero diagonal class.  M181 does not use that invalid shortcut.

## Field 7 — every-color matching inclusion and conditional endpoints

A perfect matching has exactly one `H`-orbit edge over every left global
`G`-orbit.  Since M181's patterns are globally nonconjugate, they select
distinct edges in every color, and matching perfectness makes their right
endpoints distinct.

The selected edge need not contain the literal gadget word.  For any chosen
physical representative, `u_c=alpha_c.W_c` for some arbitrary
`alpha_c in G`, not necessarily in `H`.  Hurwitz moves commute with this
independent relabeling in every coordinate, so the transporter becomes

```text
alpha_c delta_(c,k) alpha_c^(-1)
```

and retains its sign.  The clean-room boundary tests use different cyclic
`alpha_c` in each coordinate, generally moving the anchor, and all endpoint
and voltage responses pass.  This validates inclusion in every M135
perfect-matching color rather than only in an abstract tuple family.

For the fixed DPS physical targets, M181 assumes `r in Gamma(q)` before
speaking of a tree route.  Under that assumption the offset belongs to
`W_s=V_stab=colspan(z_T)`, so M175 gives a zero-voltage quotient route.
Without the assumption M181 draws no conclusion.  M169 additionally gives
`K_mon(q)=S_d^s` at the constructed source, but this does not create a target
quotient route or a length bound.  The section/coboundary and conditional-only
scopes are correct.

## Field 8 — clean-room computation, reproduction, and hygiene

The checker uses Python `3.12.3`, the standard library only, and `seed=null`.
It imports no M181 module or result, performs no `d=5` quotient enumeration,
and reconstructs the relation solely from the displayed formulas.  Run from
the M183 directory:

```text
python3 -B independent_referee.py
python3 -c 'from pathlib import Path; p=Path("independent_referee.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
```

The separate read-only relation-digest comparison uses the already-frozen
M181 JSON only after the independent result exists.  Owned artifacts are
`plan.md`, `checkpoint.md`, `audit_notes.md`, `independent_referee.py`,
`independent_results.json`, this report, `freeze_manifest.md`, and
`SHA256SUMS`.  No file outside M183 is edited.

## Field 9 — numbered objections and final decision

```text
NUMBERED MATERIAL OBJECTIONS: NONE.
FINAL DECISION: ACCEPT FROZEN M181 AT ITS EXACT STATED SCOPE.
```

Retain the explicit actual-matching full-rank family and the conditional
endpoint corollary.  Do not promote it to arbitrary accepted matching
subfamilies, do not infer the selected matched target is quotient-reachable,
and do not infer any polynomial word length, gap, mixing, or Terminal result.
