# M228 halfway checkpoint: clean-room reconstruction matches M225

Date: 2026-08-13 UTC.

## Immutable and source-order gates

All 12 M225 payloads pass the frozen checksum inventory, whose top digest is
`e61d77f0765c9aaba177ef0e0bca8b6f7f94758b7814bb7243846dff3f9f0acd`.
The candidate and symbolic files' recorded mtimes precede the checker/result
files, consistent with their textual source-order assertion.  Because the
inventory was produced only at final freeze, this chronology is supported but
not cryptographically timestamped; retain that caveat in the verdict.

## Independent method

`cleanroom_referee.py` has no input files and no predecessor imports.  It
implements a heap-based Prüfer decoder, an independent DPS rotation/closure
construction, chronological signed-Hurwitz action, and direct transcription
of both frozen formulae.  For each row it calls

```text
formula_assignment(tree,d,edit,candidate)
```

before either endpoint is constructed.  That function cannot access naive,
actual, or replay words, and no route-search/lookup structure exists.  Frozen
counts and digests occur only as terminal assertions.

## Decisive result

The independent checker verifies 840 carrier substitutions, 21 exact
initial-run sign-automaton specializations, 125 unedited leaf extensions, two
equivalent complete 125-tree constructions, and all 1,125 edited endpoints.

```text
Candidate A: 1109 passes, 16 edit-7 failures, 32 classes, 14 words
Candidate B: 1125 passes, 0 failures, 407 classes, 14 words, maximum 17
```

Both normalized complete-row digests reproduce exactly:

```text
A 85b01dc81f7175b8df32d198181e7b898507ec71d0862ca963c431695f0a15f6
B 80ba2016f66f6f8bd9d6cb8a53b276c0ee4403a4ec6747fdd85568299817f78e
```

The first Candidate-A same-descriptor collision is exactly the rank-six star
versus `{{1,3},{1,4},{1,6},{2,3},{2,5}}` at edit 7; the common five-move word
passes the star and fails the second tree at factors 8 and 11.

## Descriptor/claim boundary

For each odd edit, Candidate B produces 101 descriptors for only 125 trees:
83 singleton, 12 doubleton, and 6 tripleton classes.  Across the four odd
edits this gives 332 singleton classes, quantitatively confirming that the
descriptor nearly records the complete contour/tree.  The formula nevertheless
maps all 407 total classes to only 14 words.  This is a substantive finite
collapse, but it is not evidence of all-rank descriptor sufficiency.

Current verdict: **ACCEPT the exact finite theorem**, subject to a nonmaterial
source-order provenance caveat and the already-declared strict finite scope.
Next: deterministic rerun, final objections/report, freeze, and stop.
