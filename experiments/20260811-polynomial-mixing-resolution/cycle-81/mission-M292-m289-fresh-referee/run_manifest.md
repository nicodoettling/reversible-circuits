# M292 run manifest

Date: 2026-08-14 UTC.

## Environment

- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python: `3.12.3`
- Nonstandard dependencies: none
- Randomness/seeds: none; both computations are deterministic
- Files written only in this M292 mission directory

## Exact commands

```text
python3 -B independent_cebv_audit.py --output independent_results.json
python3 -B ../../cycle-80/mission-M289-channel-two-embedding-bv/cleanroom_cebv_check.py --output m289_rerun_results.json
```

The second command was run only after the independent formulas and checker
were fixed.  `m289_rerun_results.json` is byte-identical to M289's frozen
`cleanroom_results.json`.

## Audit coverage

- exact M289 inventory and checksum ledger;
- every cited predecessor checksum ledger;
- direct B/A ordered completion laws and raw masses;
- literal subprobability normalization and normalizer remainder;
- `E_D`/`E_k` maps and every seam/reflection endpoint;
- Lemma 1 actual weights, Borel tail, and constant tail;
- generalized `Z_(M,r)`, including `r=1,2`, cutoff, reflection, midpoint,
  and zero endpoints;
- untouched and triangular-cross BV;
- direct `k=3,5` enumeration and formula scan through `k=63`.

Finite computation is used only for formula/convention/boundary
falsification, never as the asymptotic proof.
