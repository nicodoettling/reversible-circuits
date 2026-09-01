# M309 fresh immutable referee plan

Date: 2026-08-14 UTC.

## Mission and source lock

Audit the frozen M306 agreement-hypergraph package without editing it.  The
coordinator-supplied top `SHA256SUMS` digest is

```text
f5d3c549d4fc7562953b2b577ba1b272e75f4d7a82e208f230983e77294bfe7f.
```

This referee owns only this cycle-90 mission directory.

## Exact audit scope

Independently check:

1. the RCOM conditional identity and the implication `RCOM => MRAD`;
2. the exact WRAD linear program and fractional-cover dual;
3. both directions of the claimed `MRAD <=> WRAD` equivalence with the
   stated harmonic `O(d log d)` loss;
4. the abstract symmetric/alternating-group identity-matching score-two
   obstruction and its exact statement that generic RCOM is too strong;
5. the sole `d=3` guard, including `RCOM=11/9`, maximum agreement `2`, and
   the absence of any Helly inference;
6. the explicit stop at actual `d>=6` and the still-open literal route-length
   representative problem.

Use at most one compact no-import reconstruction if a finite check is needed.

## Required scope firewall

No audited identity, LP equivalence, abstract obstruction, or `d=3` fact may
be promoted to MRAD, SSTID, a literal routing/voltage/congestion theorem, a
spectral gap, mixing, or a Terminal conclusion.  Abstract permutation-family
counterexamples must not be asserted to occur in the actual chart family
without a separate realization argument.

## Procedure

1. Read the project source of truth, then open M306.
2. Verify the supplied top digest, every M306 payload, and every cited frozen
   dependency inventory.
3. Re-derive each identity and implication from the displayed definitions,
   checking quantifiers, normalizations, constants, and small/actual-rank
   restrictions.
4. Reconstruct only the smallest decisive finite fact if necessary.
5. Freeze `ACCEPT` or `REJECT` with numbered material and nonmaterial
   objections and a new top digest.

## Expected failure modes

- Interchanging a worst-case maximum and an average in RCOM/MRAD.
- Writing a set-cover LP whose dual misses a candidate or chart constraint.
- Losing a harmonic factor or claiming the reverse MRAD/WRAD direction with
  the wrong dependence on `d`.
- Treating an abstract Sym/Alt family as an actual-chart realization.
- Inferring Helly structure from the finite `d=3` score-two fact.
- Suppressing the actual `d>=6` or literal representative-length stops.
