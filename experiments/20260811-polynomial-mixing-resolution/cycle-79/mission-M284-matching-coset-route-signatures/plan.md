# M284 plan: matching-coset route signatures

## Objective

Advance the exact routing frontier after the accepted complete local rooted
adjacent-edit table.  The target is the M135 polynomial matching-coset
refinement: determine the minimal state needed to concatenate the accepted
local correction words along a valid base route, and decide whether the
resulting common-action classes over one perfect-matching color are bounded by
`poly(d)`.

## Mathematical target and status discipline

The ambient target remains the global fixed-length uniform bridge law on

```text
Omega(N,m) = { (t_1,...,t_m) in T_N^m : t_1...t_m = id },
```

with the project composition convention recovered explicitly from the frozen
inventories.  This mission proves only a combinatorial routing statement for
the doubled-tree model.  It will label all claims `proved`, `conditional`,
`empirical`, `refuted`, or `unresolved` and will make no voltage-length,
congestion, spectral-gap, mixing, or Terminal claim.

## Immutable inputs to verify

- M135/M137: perfect-matching conflict coloring and polynomial-refinement
  obligation.
- M175/M176: relative-orientation routing inventory.
- M181/M183: conditional matching-Schreier voltage theorem.
- M200/M202: every-color route coverage only at finite rank `d=5`.
- M240/M242: all-rank conditional ordinary-edit closure.
- M269/M271 and M273/M275: decorated directional/root-seam transducers.
- M278/M281: complete local rooted adjacent-edit correction table.

All cited inventories are read-only.  Their frozen hashes and exact scopes
will be checked before use.

## Proof program

1. Fix notation for a base route, its old-padded/new-rank local states, and the
   accepted correction word at each adjacent edit.
2. Separate that rank-changing correction problem from the fixed-rank coset
   `K_Q={a : a(w_Q)=tau_i(w_Q)}`.  No identification between the two is
   permitted without an explicit intertwining map.
3. Derive by induction the exact interface state required when local
   correction words are concatenated.  Prove sufficiency and test necessity by
   constructing two partial routes with the same proposed compressed state but
   different legal next actions.
4. Express M135 common-action compatibility as equality/intersection of these
   route signatures over one perfect-matching color.  Count the possible
   signature classes analytically.
5. If a polynomial bound follows, freeze the theorem with explicit exponent
   and exceptional ranks.  Otherwise refute the naive compression by an
   arbitrary-rank family, or freeze the first standalone schedule-intersection
   lemma that is both proved and strictly narrower.
6. Only after formulas are fixed, permit one compact predeclared `d=5` or
   `d=6` falsifier.  No broad `Q_d` or product enumeration is allowed.

## Expected failure modes

- Confusing the M278 rank-changing padded lift with a same-rank group action.
- Treating a local correction table as a global common-action schedule without
  checking moving ports, rank maps, chronology, and cancellation at seams.
- Counting route words rather than equivalence classes under their exact
  future interface state.
- Promoting M200's finite `d=5` every-color fact to all ranks.
- Using M181's voltage conclusion without first supplying quotient routing.

## Deliverables

- `checkpoint.md` with the exact frontier and halfway claim.
- A proof note containing definitions, route-signature recurrence,
  sufficiency/necessity analysis, class count, and boundary cases.
- At most one compact formula-driven checker and machine-readable output if a
  finite falsifier is needed.
- `report.md` with a `promote`, `keep`, `reject`, or `inconclusive` verdict,
  dependency list, first remaining lemma, and immutable freeze manifest.

