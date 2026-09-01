# M195 freeze manifest

Freeze date: 2026-08-13 UTC.

## Decision

```text
ACCEPT M192'S STRICT EXACT J=2 REDUCTION.
MATERIAL OBJECTIONS: NONE. NONMATERIAL QUALIFICATIONS: NONE.
```

## Immutable M192 gate

All eight entries in M192's frozen `SHA256SUMS` passed before conclusions.
Its checksum-file digest is
`4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60`.
M192 was never edited.

## Frozen M195 artifacts

- `plan.md`
- `checkpoint.md`
- `proof_audit.md`
- `cleanroom_j2_audit.py`
- `cleanroom_j2_results.json`
- `results.json`
- `report.md`
- this `freeze_manifest.md`
- `SHA256SUMS`

## Accepted audited content

- Exact Cayley `tau` convolution and `gamma_L,gamma_F`.
- Exact triangle masses and complete shared-prefix `O(1/k)` bound.
- Exact unnormalized disjoint Abel identity with negative
  `O(k^-2)` endpoint.
- Universal `|E_u|<=C sqrt(u)/k`.
- Exact sufficiency of `(DV)+(DE)` for only the conditional `J=2` prefix
  estimate, with colors, kinds, and collisions retained.

## Validation and scope

The deterministic standard-library clean-room checker is capped at exact
`k=3,5`, imports no M192 code/data, and all assertions pass. It reproduces
M192's disjoint collision counts 14 and 132. Python syntax, both JSON files,
nine report fields, whitespace, and cache hygiene pass.

No `k=7`, DV/DE proof attempt, broad computation, finite-sign inference,
channelwise full-prefix claim, PCS/FCL1/direct-L1, H0/gap, mixing, or Terminal
inference. `(DV)`, `(DE)`, the conditional `J=2` prefix estimate,
`(PCR)/(WPCR)`, `(SCBR)`, and everything downstream remain open. Request a
fresh immutable audit before any further promotion.
