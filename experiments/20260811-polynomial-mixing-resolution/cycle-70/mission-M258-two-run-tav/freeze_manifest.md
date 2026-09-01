# M258 freeze manifest

Date: 2026-08-14 UTC.

Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Immutable dependency gate

Every dependency inventory passed `sha256sum -c` before use. Top checksum
digests are:

```text
M199  1de555bba9affef15b7f2b9585de7955f9d9bd23fc838c76508186d7438c25ed
M207  817988cd61ed290b6ce86e90510ee6e1a3358339bff5c8ca757c26acd2e1979d
M235  7e929497029ae0c007d0544d30f0ad3c0198947ce55f946ee7eb0aaa88b19527
M238  eb7bd2ef5bfb660f0e79978e3e7bd583876abb4f5d33320a97e098b61b33b4e8
M251  c4cee2dc9596bb54503f85a7b32b91b360fe22d1aa981eb0dce7e3d7657c04fd
M255  d9a4e48e25b829bd06b098719b239587b8be5553a6f965b315e9d5efc55875a8
```

No dependency file was edited.

## Claim-bearing payload

- `tav_cyclic_coefficient.md`: exact cyclic-start coefficient and overlap
  spikes.
- `tav_theorem.md`: reflected-head, cutoff, placement-moment, and TAV proof.
- `tav_exact_check.py`, `tav_exact_results.json`: restricted deterministic
  `k=3,5,7` falsification certificate.
- `results.json`: compact claim/constant ledger.
- `report.md`: scoped verdict and reproducibility.
- `fresh_audit_request.md`: independent-referee instructions.
- `plan.md`, `checkpoint.md`: mission provenance.
- this `freeze_manifest.md`.

All ten files above are recorded in `SHA256SUMS`. M258 is immutable after
that checksum inventory is written.

## Reproduction

```text
python3 tav_exact_check.py --output tav_exact_results.json
python3 -m compileall -q .
```

Python `3.12.3`, standard library only, deterministic, `seed=null`. No
network, nonstandard package, Magma, SAT, ILP, or broad parameter census was
used.

## Frozen verdict and exclusions

TAV is proved with universal constant 500, subject to fresh independent
audit. Full DV, conditional J2, WPCR, SCBR, response, spectral gap, mixing,
and every Terminal remain outside this mission and are not claimed.
