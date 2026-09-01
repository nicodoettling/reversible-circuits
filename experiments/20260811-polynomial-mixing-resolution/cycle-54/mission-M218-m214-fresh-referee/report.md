# M218 final report: fresh immutable referee of M214

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
ACCEPT M214 AS FROZEN, ONLY FOR THE DECLARED FINITE d5->d6 TEMPLATE.
```

All source-lock, tree-universe, descriptor, word-count, endpoint, and digest
checks pass independently.

## Field 2 — immutable provenance

Every file in M214's complete inventory returned `OK`; the `SHA256SUMS` digest
is

```text
cb63ac879b036d096af369fabf02da9abecba786bcf746ba34d809b8ceaada3f
```

The inventory and independent filesystem listing agree exactly. M214 was not
edited.

## Field 3 — exact target and convention

The target is a finite deterministic endpoint certificate, not a distribution
or sampler kernel. The checker uses chronological signed right-Hurwitz action

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

It imports and reads no M214 code or result data, performs no route search,
and does not enumerate `Q_6`.

## Field 4 — complete tree and descriptor reconstruction

Independent Prüfer generation on `[4]` plus `{1,5}` gives 16 trees. A second
five-vertex filtered Prüfer traversal gives the same set. For every tree, the
checker rebuilds the rooted parent map, stopped path, late-ancestor flag,
direct-child run, and edit-5 exceptional-path test before endpoint comparison.

The 112 rows split into exactly 13 nonempty cases with sizes

```text
5/2/1/8; 16; 7/4/5; 16; 1/15; 16; 16.
```

## Field 5 — correction-word and endpoint replay

The independent transcription contains nine distinct words including the
empty word, with maximum length 13. The checker directly verifies the source
extension, identity of every word, and every one of the 112 literal naive-to-
actual endpoint transformations. All pass.

## Field 6 — normalized digests

The independently regenerated complete payload digests are

```text
classification 96e39aea0f4a7aac3b75cadf286dc9e0343fe47801808c965d0d06545007d10b
class summary  0963d5d0826a70e16dce02ff23e394f5d8fd1edecd79d6dbf3363213770a23c0
```

They equal frozen M214. A separate post-hoc comparison also finds exact
field-for-field equality of all normalized rows and class summaries.

## Field 7 — numbered objections

Material objections:

1. None.

Nonmaterial objections:

1. None.

M214 accurately presents the result as finite exhaustive completeness and
does not promote it to a general recurrence.

## Field 8 — reproduction and hygiene

Environment: Python 3.12.3; dependencies `{}`; seed `null`. Authoritative
command:

```text
python3 -B fresh_contour_referee.py
```

Two consecutive runs produced the same `referee_results.json` hash. An
accidental compilation cache was removed before freeze. All M218 writes are
confined to its owned mission directory.

## Field 9 — disposition and strict boundary

```text
ACCEPT: complete 13-case / nine-word exact classification for the declared
16-tree d5->d6 template and inherited edits 1 through 7.

DO NOT INFER: intrinsic completeness beyond that template, all-d locality,
every-color or arbitrary-representative routing, voltage-corrected or total
route length, polynomial gap/mixing, or Terminal.
```
