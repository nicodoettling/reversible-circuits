# M205 proof audit of M203

## Exact finite setup

For each `d in {5,6}`, the two audited source patterns are

```text
X_0=(01)^2(02)^2(13)^2 product_{j=4}^{d-1}(0j)^2,
X_1=(01)^2(02)^2(03)^2 product_{j=4}^{d-1}(0j)^2.
```

For every root, the clean checker swaps that root with label `d-1`, recovers
the first rooted DPS tree/order descriptor in a declared lexicographic
Prüfer/order traversal, and swaps adjacent DPS values `i,i+1` for every
`1 <= i < 2d-2`. This gives exactly

```text
d=5: 2 patterns * 5 roots * 7 edits = 70 rows,
d=6: 2 patterns * 6 roots * 9 edits = 108 rows.
```

No quotient state graph is generated. Quotient representatives used only for
the fourteen named comparisons are the lexicographic minima over all global
coordinate relabelings in `S_d`; hence representative equality is an exact
test of the relevant relabeling orbit, not a search heuristic.

## Physical locality audit

The clean row table reproduces M203 exactly. Of 178 rows, 110 change a factor
outside the two edited indices and 106 change a factor outside the nominal
six-factor region. The six-factor failures split as 43 at d=5 and 63 at d=6.

With M203's precise directional definitions at d=6:

- 29 rows with edit `i<=5` change at least one factor position `>=7`;
- 22 rows with edit `i>=7` change at least one factor position `<=6`.

These counts deliberately exclude boundary edit 6 from both directional
categories. They do not purport to classify arbitrary notions of support
locality.

At the distinguished d=6 root, pattern 0 and edit 1, the recovered descriptor
takes 37 trials and sends

```text
(01),(01),(02),(02),(13),(13),(04),(04),(05),(05)
```

to

```text
(01),(15),(02),(02),(35),(35),(04),(04),(01),(05).
```

The changed positions are `[2,5,6,9]`; position 9 lies in the added filler.

## Quotient-level leaf-stabilization audit

For each pattern and each old d=5 edit `1..7`, the clean checker compares:

1. the exact d=5 DPS target with `(05)^2` appended, and
2. the actual distinguished-root d=6 DPS target.

The exact representative classifications are

```text
equal:   (0,2) (0,4) (0,6) (1,2) (1,4)
unequal: (0,1) (0,3) (0,5) (0,7) (1,1) (1,3) (1,5) (1,6) (1,7).
```

Thus 5 of 14 agree and 9 of 14 disagree. For the first disagreement,
pattern 0/edit 1, the representative digests are

```text
naively stabilized: bd651af9408f609196bcf37c3b6bfec37a7c126bd7b1ff2cfc11c7492e8d324f
actual d6 target:   bed555f8c63642f18b33d3c0f2d6175fd96ff5afa467e8def150a7c44f5ee35b
```

The checker first compared the canonical representatives themselves and only
then checked their digests, so the inequality is not inferred merely from an
unexamined hash.

## Logical conclusion

The proposed fixed-filler construction requires the actual d=6 matched target
to lie in the same global-relabeling orbit as the naively stabilized d=5
target. Pattern 0/edit 1 violates that necessary condition. Therefore M203's
rejection of this particular independent-block proof route is valid.

This counterexample says nothing about whether the actual d=6 target is
reachable by another synchronized quotient word. It neither refutes an all-d
route theorem nor changes M181's source-voltage theorem. An ordinary quotient
route, if later found, would still require the distinct qualitative voltage
correction argument; no corrected length follows here.

