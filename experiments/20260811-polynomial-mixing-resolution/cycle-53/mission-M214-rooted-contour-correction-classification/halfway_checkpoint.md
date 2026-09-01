# M214 halfway checkpoint: finite contour key closes all 112 rows

Date: 2026-08-13 UTC.

## Immutable gate

M203/M205/M208/M212 all passed their complete frozen inventories. No
predecessor was edited.

## Rooted-contour key

For an odd inherited edit `i=2v-3` with `v in {2,3,4}`, root the old d=5 tree
at 5 and stop the parent path from `v` upon reaching the leaf-attachment
vertex 1. Define:

- `late_ancestor=1` if an internal path vertex has label greater than `v`;
- `run` as the largest `r` such that `v+1,...,v+r` are consecutive direct
  children of `v` (tested in label order).

The exact finite classes are:

```text
edit 1 (v=2): late ancestor -> id (8 trees);
              otherwise run 0/1/2 -> three 13-move words (5/2/1 trees).

edit 3 (v=3): late ancestor -> id (5 trees);
              otherwise run 0/1 -> two 9-move words (7/4 trees).

edit 5 (v=4): path (4,2,3,1) -> id (1 tree);
              every other path -> the M208 5-move word (15 trees).

edits 2,4: id on all 16 trees;
edit 6: (R5^-)^2 on all 16 trees;
edit 7: R8^- on all 16 trees.
```

Thus there are 13 descriptor cases but only 9 distinct correction words.

## Positive discovery status

A bounded individual-endpoint MITM found the two new edit-1 words and one new
edit-3 word; applying each discovered word to its whole key class gives exact
literal endpoints. The remaining words are M208's accepted positive
certificates or the empty word. The discovery searched only named endpoint
balls and used no miss negatively.

## Remaining work

Write a deterministic no-search checker that rebuilds all 16 trees, classifies
all 112 rows from the key, and replays each archived word. Then state the exact
finite theorem and strict scope. No general-d inference is permitted.

