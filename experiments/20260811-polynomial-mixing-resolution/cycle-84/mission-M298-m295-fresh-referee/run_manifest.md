# M298 run manifest

- Date: 2026-08-14 UTC
- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python: `3.12.3`
- Nonstandard dependencies: none
- Random seed: none; every decisive calculation is deterministic and exact
- Target: accepted auxiliary first separated fixed-cell channel-one algebra
- Convention: `(pq)(x)=p(q(x))`; displayed factors multiply left-to-right
- Sole independently computed rank: `k=5`, `n=15`
- Admissible lags: `ell=2,...,13`
- Frozen package under review:
  `cycle-82/mission-M295-goci-signed-composition`
- Referee role directory:
  `cycle-84/mission-M298-m295-fresh-referee`

## Commands

Integrity, run from each relevant frozen directory:

```text
sha256sum SHA256SUMS
sha256sum -c SHA256SUMS
```

Independent exact calculation, run from this directory:

```text
python3 independent_fmcp_audit.py --output independent_results.json
```

Post-hoc comparison, run only after the independent output existed:

```text
python3 compare_frozen.py \
  --independent independent_results.json \
  --frozen ../../cycle-82/mission-M295-goci-signed-composition/fmcp_k5.json \
  --output frozen_comparison.json
```

Frozen reproducibility replay, written outside the repository:

```text
python3 fmcp_k5.py --output /tmp/m298-m295-replay.json
sha256sum /tmp/m298-m295-replay.json fmcp_k5.json
```

The replay and frozen raw output both have digest
`6a3609c86cab162b530f4543b2b98a9165c7243a545252d9b583d3164e3e7c05`.

## Raw outputs

- `independent_results.json`: clean-room exact data, generated without
  reading or importing M295.
- `frozen_comparison.json`: post-hoc equality checks against M295.

## Expected and observed failure modes

Expected: a negative fixed-middle cell might coexist with positive full
middle-weighted lag totals, so a local counterexample must not be called a
GOCI/OCI counterexample.

Observed: exactly that pattern occurs—16/120 fixed-middle cells are negative,
while all twelve complete `eta_1` lags are strictly positive.
