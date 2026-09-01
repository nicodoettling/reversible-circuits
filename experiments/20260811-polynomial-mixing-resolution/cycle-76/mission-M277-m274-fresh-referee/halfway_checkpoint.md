# M277 halfway checkpoint

Date: 2026-08-14 UTC.

Status: immutable gates and independent analytic reconstruction complete;
finite reproduction complete; verdict drafting remains.

The supplied M274 checksum-ledger digest is exactly

```text
c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e.
```

All ten M274 payloads and every payload in the fifteen declared predecessor
inventories pass.  M274 was not inspected before the initial checkpoint and
the raw law, target normalization, topology split, two-channel formulas,
reflection, endpoints, PCS--MS identity, and phase-total caveat were
reconstructed independently before its checker was opened.

The clean-room exact checker imports only the Python standard library.  It
reconstructs the quotient kernel and both conditional channel laws from
completion counts.  At `k=3,5` it matches all 18 M274 rows, all four signed
blocks in every row, and the stated MON/FOSD counts.  A fresh frozen-M161
`k=9` run matches every mathematical JSON field; only runtime and the output
path in the command string differ.

Preliminary verdict: `ACCEPT` the mathematical core, subject to nonmaterial
corrections.  The frozen report names only one of the two reflected `k=9`
minimizers (`y=7,18`), and its small-rank checker transitively imports NumPy
despite declaring no nonstandard dependency.  The arbitrary-rank obstruction
is accepted only for the displayed literal raw ordered-atom decomposition;
it does not rule out every conceivable regrouping.

CP, OS+, MS, and FCL1 remain unresolved.  No gap, mixing, or Terminal
conclusion is under audit.
