# M211 freeze manifest

Date: 2026-08-13 UTC.

## Frozen verdict

Pointwise IKBE-b and hence the two-clause IKBE lemma are refuted by the
proved asymptotic witness k=12q-1, s=3q, l=4q for Y_l, whose profile defect
tends to 7/64.

IKBE-a/DV, signed averaged DE, conditional J=2, PCR/WPCR,
SCBR/BIR/BR/PCS, and every downstream statement remain open.

## Immutable inputs

M192/M195 and M199/M207 passed their complete checksum manifests before use
and were not edited. Their checksum-file digests are recorded in
checkpoint.md.

## Reproduction

From this directory:

    python3 ikbe_formula_check.py ikbe_formula_results.json

The checker uses exact closed formulas only, is deterministic,
standard-library only, seed null, and capped at odd k<=11. Python 3.12.3.
The universal refutation comes from ikbe_obstruction.md, not finite values.

## Frozen file set

- plan.md
- checkpoint.md
- ikbe_obstruction.md
- ikbe_formula_check.py
- ikbe_formula_results.json
- results.json
- report.md
- freeze_manifest.md

SHA256SUMS is generated last over exactly this set. No cache or temporary
output is included. A fresh referee should verify all hashes before auditing
the uniform Borel-tail bound, exact seam cutoffs, and limiting 7/64 constant.
