# M160 halfway checkpoint

Date: 2026-08-13 UTC.

All seven entries in frozen M157's `SHA256SUMS` verify, and the five supplied
payload digests plus plan/checkpoint match exactly.  The accepted predecessor
scope has been checked against M147/M151, M152/M156, and M123/M128.

The shared-observation Bayes identity is correct: if
`dmu_x/dmu=L_x/p_x`, then multiplying the two posterior densities and the
single branch mass gives `p_x mu_x tensor mu_x=(L_x tensor L_x)/p_x` against
`mu tensor mu`.  Consequently the retained and killed double-beta masses are
`1-p_d` and `p_d`; this is not an independent-observation construction.  The
denominators depend on the current beta law, already at degree one.

Inspection of the exact recursion finds the normalizations consistent:
reset contributes `sum theta_E^2/(q c_E)`, while a descendant contributes
`mbar q_child/q` times the shared-X transfer.  The finite PSD claim is a
history-feature/Schur-product claim, not pointwise positivity.  A clean-room
compact `Fraction` checker is being completed for the exact reset expansion,
the `-165/512` endpoint sign, selected recursion equalities, the M152
polarization identity, and the stated diagonal-trace failure.  No material
objection has emerged so far.
