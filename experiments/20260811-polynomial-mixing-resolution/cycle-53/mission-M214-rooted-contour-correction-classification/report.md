# M214 final report: complete d5 rooted-contour correction classification

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
KEEP A COMPLETE EXACT CLASSIFICATION FOR THE DECLARED 16-TREE d5->d6
ONE-LEAF TEMPLATE. DO NOT PROMOTE IT TO GENERAL d.
```

All 112 tree/edit rows are partitioned into 13 intrinsic rooted-tree cases and
realized by nine distinct correction words of maximum length 13.

## Field 2 — immutable provenance

Every payload listed by M203/M205/M208/M212 passed its frozen checksum
inventory before substantive work. Top inventory digests are

```text
M203 584d5110354693e3d5979fc6c1e83193e24754fcba4f51f035c9415cba3816e6
M205 271fcc6909ab45732d55eca0ee3d88ea1d57e5d64548fceed07316c77d734cd3
M208 cda9c3aba4aa058d39576f1656f3ba4158be736684dad4dd64d3c61738a657b8
M212 13136f5a0943ea3955746645bbbce0cf45cacf3f37d16ffcd2e2cdf5432df9e0.
```

No predecessor was edited.

## Field 3 — exact template, target, and convention

The template consists of every Cayley tree on `[5]` rooted at leaf 5 with
neighbor/attachment vertex 1, common order
`pi_5=(7,8|1,2|3,4|5,6)`, its extension by edge `{1,6}` with
`pi_6=(9,10|1,2|3,4|5,6|7,8)`, and edits 1 through 7. Removing leaf 5 gives
a bijection with Cayley trees on `[4]`, so this is exactly `4^2=16` trees and
112 rows.

There is no probability distribution or Markov kernel in this mission. Signed
right-Hurwitz words act chronologically under

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

## Field 4 — intrinsic contour descriptor

For odd edit `i=2v-3`, root the old tree at 5 and follow the parent path from
edited black-slot vertex `v` until attachment 1. The key records:

- whether an internal path vertex has label greater than `v`; and
- the initial consecutive run `v+1,v+2,...` attached directly below `v`.

At edit 5 the only extra case is the intrinsic path `(4,2,3,1)`. Even edits
and edit 7 need no tree data. The key is computed from the rooted tree and
edit before endpoint comparison; it is not a tree-ID or route-output lookup.

## Field 5 — exact 13-case classification

The exact case sizes and words are:

```text
edit 1: late ancestor -> id (8);
        direct child run 0/1/2 -> three 13-move words (5/2/1).

edit 2: id (16).

edit 3: late ancestor -> id (5);
        direct child run 0/1 -> two 9-move words (7/4).

edit 4: id (16).

edit 5: path (4,2,3,1) -> id (1);
        otherwise -> R6^- R7 R8^- R7^- R6^- (15).

edit 6: (R5^-)^2 (16).
edit 7: R8^- (16).
```

All nontrivial words are displayed in `contour_classification.md`. Identity is
shared across five cases, leaving nine distinct correction words total.

## Field 6 — complete proof and exact certificates

`contour_classification_audit.py` independently generates the full template by
Prüfer codes, derives every key from its parent/child map, performs the exact
DPS closure, selects the declared word, and replays every signed generator.
All 112 literal physical endpoint comparisons pass. It performs no route
search and imports no predecessor implementation.

Normalized digests are

```text
complete 112-row classification:
96e39aea0f4a7aac3b75cadf286dc9e0343fe47801808c965d0d06545007d10b

13-case summary:
0963d5d0826a70e16dce02ff23e394f5d8fd1edecd79d6dbf3363213770a23c0.
```

Completeness is an exact finite theorem for this full template, not evidence
extrapolated from the two M208 trees.

## Field 7 — relation to M208 and first unresolved lemma

M208's 21 known-word failures are repaired exactly by the late-ancestor
identity cases, two extra edit-1 run words, one extra edit-3 run word, and the
exceptional edit-5 identity case. Thus M208's nonuniversal table becomes a
complete finite classification after adding intrinsic local tree data.

The key's sufficiency at arbitrary d is unresolved. The next lemma is to
derive an all-d analogue from local DPS closure identities and prove a bounded
schedule family, length bound, and synchronized compatibility. This mission
does not claim that theorem.

## Field 8 — computation and hygiene

Environment: Python 3.12.3; nonstandard dependencies `{}`; seed `null`.
Authoritative command:

```text
timeout 120s python3 -B contour_classification_audit.py
```

`discover_schedule_cover.py` is positive-certificate discovery history only;
its targeted endpoint balls do not enumerate Q6 and no miss is used
negatively. All writes are confined to M214 and no cache is retained.

## Field 9 — final boundary and audit request

```text
PROVED: complete 13-case / nine-word correction classification for all 16
trees and seven inherited edits in the declared d5->d6 template.

NOT PROVED: a recurrence at d>=6, other root/attachment templates, edits newly
introduced by extension, arbitrary H-orbit representatives, every matching
color, or a voltage-corrected route length.
```

The maximum 13 is correction-word length only. It is not a total route bound
and supports no polynomial-length, spectral-gap, mixing, or Terminal claim.
Freeze this package and request a fresh immutable referee of the intrinsic key,
case completeness, all 112 replays, and both digests.

