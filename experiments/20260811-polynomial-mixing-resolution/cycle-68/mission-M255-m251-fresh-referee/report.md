# M255 report: fresh immutable referee of M251

Date: 2026-08-14 UTC.

## Verdict

```text
ACCEPT: exact paired-domain identities.
ACCEPT: Y-DV with universal constant 18400.
UNRESOLVED: literal two-run TAV, hence X-DV and full DV.
NO DOWNSTREAM INFERENCE.
```

All 11 M251 source entries verify, and its top checksum-file digest is
`c4cee2dc9596bb54503f85a7b32b91b360fe22d1aa981eb0dce7e3d7657c04fd`.
M251 remained immutable.

The clean-room audit verified the common and strip domains, the shrinking
long-parent sign, both endpoint cases, and the exact normalization and strip
cancellations. Lemma 1 includes the only new boundary atom and proves both
the global `3/R` and far `120sqrt(t)/(Rr)` estimates from the Borel
coefficient and log-derivative bounds. No false coefficient monotonicity is
used.

For Lemma 2, both paired parents satisfy the far condition whenever that
range is nonempty. The exact denominator bound is valid at the sensitive
minimal case: for `k=3`, `H_1=1/2` and `H_2=2/9`; for `k>=5`, the lower
bound is at least `3/7`. The near/far, survivor, and normalization constants
therefore assemble safely to `2300sqrt(t)`.

The accepted three-gap seam law gives all three displayed `F_ell` profiles.
Their changes have weighted variation below `8sqrt(ell)`. Constant
annihilation and the finite Abel identity, with its correct minus sign, then
give `2300*8=18400` for `Y-DV`.

Subtracting the literal `Y` law from `X` leaves exactly M251's normalized
complementary two-run formula. Therefore `(TAV)` as displayed in M251 (5.1)
is the sole remaining scalar obligation for the `X` clause of `DV`. This
audit does not attempt or assume it.

Material objections: none. Two nonmaterial exposition qualifications are
recorded in `proof_audit.md`: display the `k=3` denominator values and the
short seam-variation accounting when the theorem is reused.

The independent import-free rational certificate checks every allowed
`ell` for bounded `k=3,5,7` and passes 952 assertions. It is finite
falsification only and does not prove the universal theorem; the proof audit
does that algebraically.

No claim about conditional `J2`, PCR/WPCR, SCBR, a spectral gap, polynomial
mixing, or either Terminal follows from this mission.

## Reproducibility

- Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: standard interpreter; checker imports no modules and uses no seed.
- Command: `python3 cleanroom_check.py` from this directory.
- Output: the `certificate` object in `results.json`.

