# M247 freeze manifest

Date: 2026-08-14 UTC.

Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Immutable inputs verified

- M244 inventory digest:
  `134082cd80dac7dcd890669fb84db0c8a978811c1f177564263c8b56f692628d`.
- M240 inventory digest:
  `2dec3e4da3b977342e8c772e47eb2d713e068d56b2220e443085d8cc36f740a3`.
- M242 inventory digest:
  `49909d402c0876443db0cd395cc54cdba8c6ed7b74f1090e070e5d74171ce663`.
- DPS primary PDF digest:
  `98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2`.

## Frozen M247 payload

- `plan.md` — preconclusion scope and acceptance rule.
- `checkpoint.md` — final status checkpoint.
- `proof_audit.md` — independent pruning proof, exact objections, and repaired
  obligation.
- `cleanroom_token_check.py` — no-input one-row independent DPS replay.
- `cleanroom_token_results.json` — exact counterexample record.
- `report.md` — split ACCEPT/REJECT verdict and scope.

`SHA256SUMS` freezes the payload above.  The accepted claim is only canonical
unedited one-open colored pruning.  Frozen RSMI is refuted and the written
full RSMI-to-IDL package is rejected.  `RSMI+`, IDL, and every downstream
consequence remain unresolved.

