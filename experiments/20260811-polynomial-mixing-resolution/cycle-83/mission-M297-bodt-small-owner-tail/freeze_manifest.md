# M297 freeze manifest

Date: 2026-08-14 UTC.

## Frozen claim

For every odd `k>=3`, the accepted M290/M293 boundary decorated vector BODT
is equivalent up to an `O(1/k)` vector to the small-owner-local field
`(SODT)`, and hence to the exact scalar coefficient vector `(SOCT)` in
`proof.md` plus the controlling size-one clarification in
`proof_addendum.md`.

The phase collapse retains the exact `1/3` triangle and `1/4` `S/N`
coefficients.  The proof removes all large-owner fields, including
small/large cross correlations, even inside boundary states.  The rowwise
Borel coefficient estimate `(SOCL)` is unresolved.  Therefore BODT, DOR,
PBV/FD/FCL1, every gap/mixing statement, and both Terminals remain open.

## Payload hashes before this manifest

```text
7e45a79b105ac8ffede255d81f051b096833c1b8ccae153d66e850922ab37828  plan.md
d78fafaf14f3b8e137dd48733c78b23d2620ed32121fad3e1116afad4911a479  checkpoint.md
e44521e4179d4bc042c995fae407d573a56f291b898a2d3314212d0a544eff00  halfway_checkpoint.md
24597a6f1ce81af0ab69fa6a52620c8c34471e6554e300217983026d833ade09  proof.md
4df9c4f88cb83e08482effd95e5ea1e40fa806df31768f112d22b2c5e35a12d3  proof_addendum.md
9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73  bodt_k9_probe.py
cde2565052b51ac1bcddfe04db20526383633932989293e5f8a388c14b3effba  bodt_k9_results.json
afc8dbd562ac334bb09b7f442a1de0d8d3686e6a6b7f7fb6f345f95ed7ecb88e  bodt_k9_self_rows.py
bb6e5e52dfe8e694c829b1fb603f426df7bc256ec11759adb75bf0184617e82e  bodt_k9_self_results.json
f0ae557f474084a6e1314dfeb70b97e1dc7170db9c3cff6addd00714aa5a9a76  report.md
fa64faebded0ac74745d75967f980c8513cc340ad88b3223601d71b7683a856e  run_manifest.md
```

## Reproducibility

Both exact scripts use Python `3.12.3` and the standard library only.  They
are deterministic (`seed=null`) and evaluate only `k=9`.  Both result JSON
files parse successfully; the scripts compile successfully.  All twelve
required predecessor author/referee inventories passed before the proof was
written.

No file outside this mission directory was edited by M297.

