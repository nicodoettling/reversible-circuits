# M220 final report: first next-rank rooted-contour obstruction

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
REJECT THE EXPLICIT LATE/RUN/FORWARD-EXCEPTION RECURRENCE.
KEEP A FIRST EXACT SAME-KEY d6->d7 OBSTRUCTION.
```

The recurrence is exact on all 112 M214 rows but fails at the first tested
next rank. A richer full-contour recurrence remains unresolved.

## Field 2 — immutable provenance

Every payload in M203/M205, M208/M212, and M214/M218 passed its frozen
inventory. Top digests are

```text
M203 584d5110354693e3d5979fc6c1e83193e24754fcba4f51f035c9415cba3816e6
M205 271fcc6909ab45732d55eca0ee3d88ea1d57e5d64548fceed07316c77d734cd3
M208 cda9c3aba4aa058d39576f1656f3ba4158be736684dad4dd64d3c61738a657b8
M212 13136f5a0943ea3955746645bbbce0cf45cacf3f37d16ffcd2e2cdf5432df9e0
M214 cb63ac879b036d096af369fabf02da9abecba786bcf746ba34d809b8ceaada3f
M218 3929f738afcb9834e74eea9610d284ca5cabe2589da05b691bf3b4447b58f656
```

No predecessor was edited.

## Field 3 — exact target, convention, and candidate

There is no probability distribution or Markov kernel in this mission. The
target is exact physical endpoint correction under chronological signed
right-Hurwitz action

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

Before computation, `symbolic_transport.md` declared a closed recurrence:
ordinary odd edits use `Q_(d,v,run) B_d Q^-1`, except for late-ancestor and
one forward-chain identity class; internal even edits use identity; and the
last two edits use universal double-/single-inverse words.

## Field 4 — proved analytic transport identities

The formal carrier

```text
B_p=R_p^- R_(p+1) R_(p+2)^- R_(p+1)^- R_p^-
```

satisfies

```text
B_p[(xy),(zx),(zy),(zn)]=[(xn),(zy),(zy),(zx)]
```

for distinct symbols. The corresponding double-inverse and single-inverse
boundary identities are also proved by literal intermediate tuples. These are
valid group identities independent of the refuted DPS recurrence.

## Field 5 — exact reproduction and complete next-rank check

The closed formula reproduces all `16*7=112` accepted M214 rows at
`d=5 -> 6`. At `d=6`, two Prüfer constructions independently give the full
125-tree root-leaf template. Replaying all nine edits produces

```text
edit       1   2   3   4   5   6   7   8   9
passes   114 125 125 125 125 125 109 125 125
failures  11   0   0   0   0   0  16   0   0
```

Thus 1,098 of 1,125 rows pass. The normalized complete-row digest is

```text
f0deca809ef570f7d557a88a94d517e3885f971f0178ac7ef2938bad651341c0
```

This is exact finite evidence only. In particular, edits 8 and 9 are fully
checked at this rank but not proved universally.

## Field 6 — first same-key obstruction

At edit 1, take

```text
T_0={{1,2},{1,3},{1,4},{1,5},{1,6}},
T_1={{1,2},{1,3},{1,4},{1,6},{2,5}}.
```

Both have descriptor `v=2`, path `(2,1)`, `late=false`, `run=0`, and
`exception=false`. The common displayed 17-move route reaches the exact target
for `T_0`. For `T_1` it leaves factors 7 and 8 equal to `(45)^2`, while the
actual endpoint has `(46)^2`. Full naive, target, and replay words are frozen
in `obstruction.md` and `rooted_recurrence_results.json`.

The missing datum is the nonconsecutive larger child 5 of vertex 2. The
initial run ignores it because label 3 is not a child of 2.

## Field 7 — exact logical conclusion and next lemma

**REFUTED:** the explicit key-to-word recurrence in `symbolic_transport.md`.
The same declared key does not determine whether that displayed conjugator
works at `d=6`.

**NOT REFUTED:** existence of another common braid for the witness, or a
richer descriptor using full larger-child/contour incidence.

The next standalone obligation is the **Full Child-Contour Sign Lemma**:
identify sufficient ordered incidence data for all larger children and all
exceptional identity paths, then prove a local closure formula and explicit
length bound.

## Field 8 — reproduction and hygiene

Environment: Python 3.12.3; dependencies `{}`; seed `null`. Command:

```text
python3 -B rooted_recurrence_audit.py
```

The checker imports no predecessor code or data, performs no route search,
and enumerates neither `Q_6` nor `Q_7`. Consecutive runs produced identical
`rooted_recurrence_results.json` hashes. All writes are confined to M220 and
no bytecode cache is retained.

## Field 9 — strict boundary and audit request

```text
KEEP: formal carrier identities, exact d5 reproduction, exact d6 failure
table, and the first same-key obstruction.

DO NOT INFER: nonexistence of alternative corrections, an all-rank theorem,
every-color or arbitrary-representative routing, voltage-corrected or total
route length, polynomial gap/mixing, or Terminal.
```

Freeze M220 and commission a fresh immutable referee focused on the analytic
carrier identities, exact recurrence specialization, complete 125-tree count,
1,125 replays, first same-key witness, row digest, and scope boundary.

