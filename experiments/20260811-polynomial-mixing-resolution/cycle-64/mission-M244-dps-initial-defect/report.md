# M244 final report: canonical stack pruning toward DPS IDL

Date: 2026-08-14 UTC. Base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Verdict

```text
PROMOTE A PROVED CANONICAL OFF-PATH STACK-PRUNING LEMMA AND A STRICT
REDUCTION OF IDL TO THE RANK-STABLE METRIC INTERFACE LEMMA (RSMI).
DO NOT PROMOTE IDL OR UNCONDITIONAL ALL-RANK Z2 CLOSURE.
```

## Immutable inputs and source

Frozen M240 and fresh M242 verify at their required inventory digests

```text
M240 2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3
M242 49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663.
```

The DPS primary source was read in full. The author PDF SHA-256 is

```text
98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2.
```

Proposition 3 supplies the rooted hairy tree; Lemma 2 and Theorem 5 supply the
valid distance-one/distance-three LIFO closure. They do not state IDL.

## Strongest proved theorem

For a canonical unedited off-path component, every inserted black slot has

```text
L_a=2a-3, R_a=2a-2, hence R_a=L_a+1.
```

Its full hairy-tree outer-contour excursion is a literal contiguous word
given recursively in equation (2.2) of `stack_pruning_reduction.md`. There is
a legal sequence of local closures using only complete nodes of that
excursion's noncrossing rewrite-dependency forest which matches every black
half-edge and leaves exactly one white half-edge, labeled `R_a`. Adding a
formal `B^R_a` balances the colored projection.

The proof is an induction on the rooted component. Child survivors fill
exactly the labels missing from the parent's increasing white gaps. Because
the canonical leading black interval is empty, the resulting increasing
white block is followed by the reverse decreasing black block, so every LIFO
pair is internal and the first `W^R_a` is the sole survivor.

The theorem explicitly excludes the reversed edited slot `x_v`, which lies on
the retained stopped path. It is not a statement about arbitrary DPS label
orientations.

## Exact remaining lemma

The colored pruning does not retain enough information to distinguish a
distance-one closure from a distance-three closure. That side metric decides
the second black endpoint and hence the output transposition.

RSMI is stated with full quantifiers and conventions in Section 4 of the
proof note. After deleting the complete canonical off-path rewrite nodes at
ranks `d` and `d+1`, it requires equality of the actual retained side count
in `{1,3}` and of the distance-three black endpoint, except for the explicitly
listed larger-direct-child interfaces; it also supplies the stopped-path and
root transition table. The reversed `x_v` slot is never pruned.

Conditional on RSMI, the proof note derives the closed equality and every
coordinate of `IDL-a` through `IDL-d`. Thus the former global quadratic-stack
obligation is narrowed to a local side-profile stability statement on
one-open interfaces. A counterexample would be one retained label with its
first differing side count or black endpoint.

## Tiny falsifier

After fixing the analytic recurrence, a no-input independent checker tested
only the permitted ranks `d=5,6`:

```text
d=5: 48 ordinary rows, 0 failures
d=6: 500 ordinary rows, 0 failures
```

The row digest is
`c6f62a955055cbf998e8119acc7dfb7ff1cebfb006fdd7b4c5c5696465f4383c`.
This is exact finite calibration only and proves neither RSMI nor IDL.

Environment: Python 3.12.3, nonstandard dependencies `{}`, seed `null`.

## Scope and objection preservation

M242's `N-1` is preserved: no generic `(R^-1)^2` identity is used. M231/M234
and M236/M237 enter only as finite calibration context, not induction.

No result here proves fixed-edit boundary shapes, every-color routing,
arbitrary-representative routing, voltage correction, total route length,
congestion, a physical gap, polynomial mixing, or Terminal.

## Audit request

Freeze M244 and commission a fresh immutable referee. The referee should
check the primary-source convention, literal excursion factorization (2.2),
the restriction `R_a=L_a+1`, the exclusion of `x_v`, completeness of each
deleted rewrite node, the induction leaving `W^R_a`, the one-open rather than
zero-balanced correction, the exact RSMI statement, the conditional
RSMI-to-IDL implication, checker independence/digest, and every scope refusal.
