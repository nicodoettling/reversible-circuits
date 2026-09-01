# M217 freeze manifest

Date: 2026-08-13 UTC.

## Frozen verdict

Strict exact signed-DE three-block reduction with proved uniform normalizer
and macroscopic q_hat-mass lemmas.

WBE, signed averaged DE, IKBE-a/DV, conditional J=2, and every downstream
claim remain open. Pointwise IKBE-b remains refuted.

## Immutable inputs

M192/M195, M199/M207, and M211/M215 passed their full checksum manifests and
were not edited. Their checksum-file digests are recorded in checkpoint.md.

## Reproduction

From this directory:

    python3 signed_de_formula.py signed_de_results.json

The checker is deterministic, standard-library only, seed null, formula-only,
and capped at odd k<=15. Finite Y values make no universal inference.

## Frozen file set

- plan.md
- checkpoint.md
- signed_de_reduction.md
- signed_de_formula.py
- signed_de_results.json
- results.json
- report.md
- freeze_manifest.md

SHA256SUMS is generated last over this exact set. No cache or temporary
output is included. A fresh referee should verify all hashes before auditing
the q_hat weight, A-normalizer cancellation, three-block signs, normalizer
estimate, macroscopic tail, and exact WBE implication.
