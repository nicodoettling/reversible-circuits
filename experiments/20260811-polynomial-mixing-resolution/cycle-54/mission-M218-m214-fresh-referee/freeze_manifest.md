# M218 freeze manifest

Date: 2026-08-13 UTC.

## Frozen verdict

`ACCEPT M214 AS FROZEN` for exactly its complete finite 16-tree `d=5` to
`d=6` one-leaf correction classification. Material objections: none.
Nonmaterial objections: none.

## Exact certificates

```text
M214 SHA256SUMS digest   cb63ac879b036d096af369fabf02da9abecba786bcf746ba34d809b8ceaada3f
tree count               16
row count                112
descriptor case count    13
distinct words           9
maximum word length      13
all literal replays      true
classification digest    96e39aea0f4a7aac3b75cadf286dc9e0343fe47801808c965d0d06545007d10b
class-summary digest      0963d5d0826a70e16dce02ff23e394f5d8fd1edecd79d6dbf3363213770a23c0
```

The normalized 112 rows and 13 class summaries also compare exactly against
frozen M214 in a post-hoc read-only check.

## Method boundary

`fresh_contour_referee.py` is the authoritative deterministic checker. It
generates the complete tree set independently, derives every descriptor from
the rooted tree, rebuilds both DPS endpoints, and replays every chronological
signed-Hurwitz generator. It reads and imports no M214 code or result data,
performs no route search, and enumerates no `Q_6` state space.

## Logical boundary

The accepted theorem is exact only for the declared finite template. This
package proves no descriptor completeness outside it, all-`d` recurrence,
every-color result, arbitrary-representative compatibility, voltage-corrected
length, total polynomial length, spectral gap, mixing, or Terminal outcome.

## Payload inventory

The frozen payload is exactly the files listed in `SHA256SUMS`. No bytecode
cache is part of the package.

