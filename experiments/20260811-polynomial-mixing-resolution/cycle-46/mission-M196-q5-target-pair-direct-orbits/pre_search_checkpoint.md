# M196 pre-search checkpoint

Date: 2026-08-13 UTC.

## Immutable gate

M191 and M194 pass their complete manifests, with top digests

```text
a2aeba9feb5a4bbc3f2161864cfa42ecbc0ef3a578f6a3222c1a9e07c73ab42e
f51442fac7e1ebd5dc9f62dd2803d7ecd3863f10e5205927fd51e50ade4e4830
```

respectively. The frozen action digest independently recomputes to

```text
160bcae167e754af4ff55356a2ab25526bf53d03ebc23bd974938fb8370c67ae.
```

## Deduplication

The chronological BFS transversal from first source ID 16 reaches all 8,400
states, has maximum depth 13, and every tree word replays exactly. Applying
the inverse tree word to the second coordinate maps the 54 named targets to
41 distinct adjusted second IDs.

Thus only 41 target-directed stabilizer decisions are required. Search will
be performed in the simultaneous/product action with early stopping and
deduplicated certificate reuse. It will not construct the full stabilizer
orbit or enumerate `Q_5^2`.

Positive results require directly replayed words. A target not found within
the five-minute cap remains undecided; no bounded miss is a negative result.
