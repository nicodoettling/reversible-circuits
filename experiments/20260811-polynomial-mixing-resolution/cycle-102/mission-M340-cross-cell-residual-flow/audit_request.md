# M340 request for fresh immutable audit

Date: 2026-08-14 UTC

Please assign a genuinely fresh referee for frozen M340.  The audit should:

1. verify the M340 top digest, every payload, and every frontier/raw-law gate
   in `source_lock.md`, retaining M329's append-only repair of M326;
2. reconstruct the complete token weight and corrected `c_X` without
   separating channels, kinds, cells, orientations, zero slots, or other raw
   constituents;
3. verify that retaining every raw source-switch label makes `Phi`
   deterministic and the frozen XCRF graph degree at most one;
4. independently derive the atom Hall criterion, cell cut conditions, and
   exact divergence identity;
5. verify from frozen M335/M336 that the displayed off-`Exc_pf^*` token has
   positive complete weight, unchanged cell `(1,1)`, and zero canonical
   reverse residual factors;
6. confirm that singleton Hall refutes only this XCRF and that the partial-flow
   identity proves no nonzero final edge coefficient.

The referee must not inspect a new rank/cell, run a new guard, invent a broader
relation, pair by final sign, or infer MPCF or any downstream theorem.

