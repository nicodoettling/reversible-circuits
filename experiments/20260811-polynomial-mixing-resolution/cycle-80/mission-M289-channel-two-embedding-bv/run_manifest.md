# M289 run manifest

Date: 2026-08-14 UTC.

## Environment and command

- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python: `3.12.3`
- Nonstandard dependencies: none
- Randomness/seeds: none; the computation is deterministic
- Exact command:

  ```text
  python3 -B cleanroom_cebv_check.py --output cleanroom_results.json
  ```

- Formula scan: odd `k in {3,5,7,9,15,31}`
- Direct minimal-completion enumeration: `k in {3,5}`
- Purpose: formula, convention, and boundary falsification only; no finite
  computation is used to infer the asymptotic theorem.

## Immutable predecessor gate

For each row below, `sha256sum -c SHA256SUMS` returned `OK` for every declared
payload.  The last column is the SHA-256 digest of the checksum file itself.

| mission | declared payloads | checksum-file SHA-256 |
|---|---:|---|
| M192 | 8 | `4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60` |
| M195 | 8 | `1f0c398bd92edf37e16880c239e0bf65d63622e1de9c2c9904a26fd560d93f0a` |
| M199 | 8 | `1de555bba9affef15b7f2b9585de7955f9d9bd23fc838c76508186d7438c25ed` |
| M207 | 8 | `817988cd61ed290b6ce86e90510ee6e1a3358339bff5c8ca757c26acd2e1979d` |
| M217 | 8 | `7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557` |
| M222 | 7 | `d2a43d9049fcfd5be96f1167142979d4daa6cb72345d3b26f28cdda36aae7ccd` |
| M276 | 9 | `882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db` |
| M279 | 8 | `3910c66a134083117e8defce4bf6a3d57fdce3a48b519e7c8271c1864bf52f66` |
| M282 | 9 | `cac6e77151401e708acb5a812097ccce44ed1dce45acefada9a3c13ebcfe5ed7` |
| M286 | 8 | `3778a3884212e4b5403df1d37a1145a2810b77f94b55e84dd84aac1dec6c0f0a` |

The accepted M226/M229 signed-WBE background was also integrity checked
during proof reconstruction; it was not imported into the checker.

## Reproducibility and hygiene

The checker is self-contained and formula-driven.  It imports no M192,
M195, M199, M207, M217, M222, M276, M279, M282, or M286 code or data.  It
does not create a cache, use a temporary directory, or write outside this
mission directory.  Its only output is `cleanroom_results.json`.
