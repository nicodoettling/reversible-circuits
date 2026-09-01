# M130 fresh referee report on frozen M127

Date: 2026-08-13 UTC.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict and exact scope

```text
ACCEPT M127 AT ITS STATED NONTERMINAL SCOPE.
MATERIAL NUMBERED OBJECTIONS: NONE.
```

M127 correctly proves that every adjacent-value DPS edit descends through
the white-root quotient, proves a general paired-source subgroup invariant,
and uses that invariant to refute a source-independent fixed braid already at
`d=3`.  Its complete `d=3` action-image and schedule-cover figures, and its
all-index `d=3,4` witnesses, are also correct as **EXACT FINITE** claims.

M127 does not prove an asymptotic schedule cover, path congestion, a gap for
the physical minimal-sector Hurwitz chain, a gap for the original heat-bath
chain, Terminal A, or Terminal B.  Its report preserves these boundaries.

```text
candidate                  | fixed braid for a whole DPS adjacent-value action
claimed target             | uniform physical Z_d (via its constant-d rooted lift)
identity ok                | exact d=2,3,4; general DPS/Hurwitz constructions preserve it
crosses Hurwitz components | not applicable in the connected minimal orbit
exact diagnostics          | brute Z_d, DPS roots, pair subgroups, d=3 action/cover
verdict                    | reject fixed braid; accept M127 with zero objections
```

## 2. Frozen provenance

All assigned digests match exactly:

| M127 artifact | observed SHA-256 |
|---|---|
| `report.md` | `d7983caa8cc20bc0e882d11afed3b1953a940b98c56299d2e956d625deb6acc0` |
| `fixed_braid_obstruction.md` | `0f8c1ce6d5ddc8f54bd3a1fe366f49b512fe8ee5e03a5a68cf547adbaaeb534a` |
| `fixed_braid_audit.py` | `4fe5a897d3dc38e6c92216a2c576e20ac82e83bbf2038af571b255833bf3718d` |
| `fixed_braid_results.json` | `51c2e14f868bf433852b606ec71faf9dacc6537b6e2a788373cdbdc10cfbdb9c` |
| `freeze_manifest.md` | `04b37e3e6a3127137c46a655009ccd18960118138f1c1f1b004528e45e76d7b3` |

M127 remained immutable.  The M130 checker imports no M127 or predecessor
module or result file.

## 3. Target, convention, and dependency audit

The auxiliary physical target is uniform on

```text
Z_d={w=(t_1,...,t_(2d-2)):t_1...t_(2d-2)=id,
                              support(w) connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`, with displayed factors multiplied
left-to-right.  For transpositions the signed right Hurwitz actions are

```text
R_j(a,b)=(b,bab),        R_j^(-1)(a,b)=(aba,a).
```

The only non-elementary input to the all-rank descent is the already accepted
M112/M119 DPS theorem:

```text
Z_d <-> unrooted Hurwitz trees,
rooted Z_d <-> Cayley trees on [d] x S_(2d-2),
```

with exactly `d` white roots over each physical word.  M127 uses no new
literature or unproved mixing input.

## 4. Adjacent-value edits descend through root forgetting

For a rooted coordinate `(T,pi)`, DPS inserts black vertex `x_k` into the
first parent edge from `y_k` toward `y_d` and labels its two halves by
`pi(2k-1),pi(2k)`.  Swapping the values `i,i+1` throughout `pi` therefore
does precisely one intrinsic operation on the rooted Hurwitz tree: exchange
those two global edge labels.

Edge relabeling commutes with forgetting the chosen white root.  Two rooted
coordinates over the same physical word first give the same unrooted
Hurwitz tree, then still give the same relabeled unrooted tree.  The unrooted
DPS bijection supplies one target word.  Thus

```text
tau_i(F(T,pi))=F(T,s_i pi)
```

is well-defined for every `d>=2`; swapping the same labels twice proves
`tau_i^2=id`.  M127's universal descent and involution claims are **PROVED**.
They do not assert that `tau_i` belongs to the signed braid action image.

## 5. Paired-source subgroup invariant

For source words `x,y in G^m`, form the tuple of pairs

```text
((x_1,y_1),...,(x_m,y_m)) in (G x G)^m.
```

One common signed Hurwitz generator on `x` and `y` is exactly an ordinary
Hurwitz generator on this tuple.  For adjacent factors `a,b in G x G`, the
replacement

```text
(a,b) -> (b,b^(-1)ab)
```

generates the same literal subgroup: both outputs lie in `<a,b>`, while
`a=b(b^(-1)ab)b^(-1)` lies in the output-generated subgroup.  The inverse
move gives the reverse containment.  Induction over any signed braid word
proves invariance of

```text
< (x_1,y_1),...,(x_m,y_m) > <= G x G.
```

This is a **PROVED** arbitrary-length obstruction, not a bounded search.

## 6. Hand-checkable `d=3,i=3` counterexample

For the star `T={{1,2},{1,3}}`, rooted at `y_3`, the fresh DPS reconstruction
reproduces M127's rows exactly:

```text
pi_A=(3,4,1,2): x =((12),(12),(13),(13)),
pi_B=(1,2,4,3): y =((12),(13),(12),(23)),

s_3 pi_A:       x'=((23),(23),(13),(13)),
s_3 pi_B:       y'=((13),(13),(12),(12)).
```

Put `A=(12), B=(13), C=(23)`.  The source pair generators are

```text
(A,A), (A,B), (B,A), (B,C).
```

They lie in the parity-diagonal subgroup of `S_3 x S_3`.  Multiplication by
`(A,A)^(-1)` produces `(id,AB)` and `(AB,id)`, which generate
`A_3 x A_3`; adjoining `(A,A)` gives the whole parity-diagonal subgroup,
of order `18`.

The target pair generators reduce to `(C,B)` and `(B,A)`.  Conjugation by
`rho=(123)` sends `C` to `B` and `B` to `A`; since `C,B` generate `S_3`,
these pairs generate exactly the graph of that conjugation, of order `6`.
The subgroups differ, so Section 5 forbids any common signed braid word.

Therefore the universal fixed-braid proposition is **REFUTED at `d=3`**.
The conclusion is independent of braid length.

## 7. Independent exact finite audit

The fresh checker separately brute-forces the physical target before
reconstructing it by the accepted plus-mirror DPS closure.  The two sets are
identical:

| `d` | rooted coordinates | brute `|Z_d|` | root-fiber histogram | physical Hurwitz orbit |
|---:|---:|---:|---:|---:|
| 2 | 2 | 1 | `{2:1}` | 1 |
| 3 | 72 | 24 | `{3:24}` | 24 |
| 4 | 11,520 | 2,880 | `{4:2880}` | 2,880 |

There are zero word-identity failures and zero connected-support failures.
Every adjacent index has zero root-fiber target collisions, and every
resulting `tau_i` is a bijective involution.

The first lexicographic paired-subgroup witnesses reproduce M127 exactly:

| rank | adjacent indices | source order -> target order | pairs tested to first witness |
|---:|---|---|---|
| 3 | 1,2,3 | `18 -> 6` | 11, 5, 3 |
| 4 | 1,2,3,4 | `24 -> 288` | 15 each |
| 4 | 5 | `288 -> 24` | 4 |

These complete small-rank results can refute the universal fixed-word claim,
but they are not asymptotic congestion or gap evidence.

## 8. Complete `d=3` action image and schedule cover

On the independently enumerated 24 words of `Z_3`, exact closure of the six
signed adjacent-Hurwitz generator tables gives action-image order `216`.
For each of the three adjacent-value indices:

- `tau_i` is absent from the action image;
- exactly 23 distinct nonempty agreement masks occur;
- one fixed braid agrees on at most 6 of the 24 sources;
- the exact union-DP frontier sizes through depth five are
  `1,23,206,811,1640,2021`;
- the full 24-source mask is absent through four schedules and present with
  five schedules.

Thus five fixed schedule classes are necessary and sufficient at `d=3`.
The union DP is exhaustive over all 216 action-image elements, so both the
lower and upper bounds are exact.  This result is **EXACT FINITE ONLY**.  It
does not prove that the number or length of schedules is polynomial in `d`.

## 9. Reproduction and hygiene

The exact command, run from the M130 directory, is

```text
python3 -B independent_referee.py
python3 -c 'from pathlib import Path; p=Path("independent_referee.py"); compile(p.read_text(), str(p), "exec"); print("compile ok")'
python3 -c 'import json; q=json.load(open("independent_results.json")); assert q["verdict"]=="ACCEPT"; assert q["d3_complete_action_image"]["action_image_order"]==216; print("assertions ok")'
```

Python is `3.12.3`; dependencies are `{}`; the computation is deterministic
with `seed=null`.  The final main run took `3.6502991328015924` seconds.  Raw output
is `independent_results.json`.

M130 owns only `plan.md`, `checkpoint.md`, `independent_referee.py`,
`independent_results.json`, this report, `freeze_manifest.md`, and
`SHA256SUMS`.  No M127, coordinator, manuscript, project-skill, or other
mission file was edited.

## 10. Final decision

```text
ACCEPT.  ZERO MATERIAL NUMBERED OBJECTIONS.
```

Promote only M127's exact scope: universal root-independent endpoint descent,
the paired-source subgroup invariant, and the fixed-braid counterexample.
Retain the `d=3,4` action and cover results as exact finite facts.

The surviving **ADJACENT-VALUE POLYNOMIAL SCHEDULE COVER** is unresolved, as
are UST basis-exchange routes and the full **ROOTED PRODUCT LOCAL COMPARISON**.
No all-edge congestion bound, physical `P_(0,d)` gap, arbitrary-product
`Gamma_0` bound, original lazy exact `{3,4,5}` heat-bath gap, Terminal A, or
Terminal B is proved or refuted by M127 or this audit.
