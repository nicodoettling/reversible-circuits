# M156 plan: fresh referee audit of frozen M152

Date: 2026-08-13 UTC.

## Objective

Audit the immutable M152 beta-Jensen obstruction without importing its code or
editing its directory.  The audit covers the exact killed beta-binomial atom,
the contextual point lift and reset normalization, the Bellman majorant and
minimality claim, the exact right-heavy witness, and the separate true
excursion value.

## Immutable gate

Verify the six coordinator-supplied SHA-256 digests before relying on M152.
Any mismatch is a rejection.  The actual manifest filename is
`freeze_manifest.md`.

## Independent checks

1. Re-derive the posterior/killed-atom identity algebraically.
2. Rebuild canonical basins, point currents, and the normalized Jensen reward
   directly from literal compositions.
3. Rebuild the minimal pointwise Bellman polynomial by literal-root
   enumeration, not M152's grouped root routine.
4. Rebuild the exact nilpotent excursion separately and compare every stated
   witness fraction.
5. Audit the induction proving the global majorant and the induction proving
   pointwise minimality.

The checker is standard-library-only, exact `Fraction` arithmetic, has no
predecessor imports, and performs no broad parameter scan.

## Deliverables

`checkpoint.md`, `fresh_referee.py`, `fresh_referee.json`, `proof_audit.md`,
`report.md`, `freeze_manifest.md`, and `SHA256SUMS`, all confined to M156.

