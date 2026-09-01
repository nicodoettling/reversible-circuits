# M236 plan: exact next-rank test of the M231/M234 route-normal descriptor

Date: 2026-08-13 UTC

## Objective

Perform a deterministic exact next-rank falsification/completeness test of the
finite M231/M234 route-normal descriptor and its assigned Hurwitz word formula.
This mission tests only the complete declared `d=7 -> 8` one-leaf template.

The ambient project target remains the uniform law on fixed-length identity
words

```text
Omega(N,m) = {(t_1,...,t_m) in T_N^m : t_1 ... t_m = id},
```

for the lazy exact same-product `{3,4,5}` block heat-bath kernel fixed in
`GOAL_SPEC.md`.  M236 does not itself prove a statement about that kernel; it
tests one finite combinatorial routing lemma used in the comparison route.

## Source lock and predeclaration

Before implementation, verify the frozen M214/M218, M220/M223, M225/M228, and
M231/M234 artifacts and their coordinator-ledger dispositions.  Copy the M231
route word formula verbatim into an immutable gate.  The descriptor is fixed
in advance as

```text
Z2 = ('closed')                         if late OR ascent,
Z2 = ('open', v, epsilon)               otherwise.
```

Here `late`, `ascent`, `v`, `epsilon`, the route-normal word formula, the DPS
tree/word construction, edit ordering, and Hurwitz convention have exactly the
meanings frozen by M231/M234.  There will be no endpoint-derived adaptation,
formula search, descriptor refinement, quotient/group enumeration, or
post-failure exception rule.

## Exact finite universe

- Rank transition: `d=7 -> 8`.
- Rooted trees: every labeled tree on `[7]` for which root `7` is a leaf
  adjacent to vertex `1`.
- Rows: every ordinary inherited edit in the declared DPS construction.
- Arithmetic/replay: deterministic exact symbolic Hurwitz replay.
- Enumeration mechanism: a direct complete Prüfer-code traversal with the
  root-leaf condition checked exactly; no quotienting.

## Decision rule

Exactly one outcome will be frozen:

1. **Finite pass:** the M231 word formula and `Z2` pass every declared row.
   Record only a finite next-rank theorem.
2. **Finite obstruction:** freeze the first exact failure in deterministic
   `(tree, edit)` order and classify it as either
   - descriptor insufficiency: a same-`Z2` collision needs different replay
     words, or
   - word-formula failure: the predeclared word fails although the descriptor
     is not thereby shown insufficient.

Record total trees and rows, per-edit row/failure counts, the first witness (if
any), descriptor-class counts, replay identities, and normalized digests.

## Expected failure modes and controls

- A convention mismatch could manufacture a false failure: reconstruct the
  frozen DPS word and Hurwitz action directly and assert every input/output
  identity before comparing.
- A hidden lookup could make a pass circular: the checker may depend only on
  the frozen formula and local descriptor fields, never on endpoint labels or
  a target-word table.
- An incomplete tree universe could make a pass meaningless: assert the
  Prüfer count against the exact root-leaf count and report it.
- A late/ascent branch ambiguity could change `Z2`: copy the frozen predicate
  verbatim and emit per-branch counts.

## Deliverables

`checkpoint.md`, `halfway_checkpoint.md`, `immutable_gate.md`, a standalone
exact checker, machine-readable results, a finite theorem or obstruction,
`report.md`, `freeze_manifest.md`, `SHA256SUMS`, and a fresh-audit request.

No finite pass will be extrapolated to all `d`, every color, polynomial route
length, a comparison bound, spectral gap, mixing time, or a terminal result.

