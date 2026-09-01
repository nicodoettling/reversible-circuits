# M295 run manifest

- Date: 2026-08-14 UTC
- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python: `3.12.3`
- Nonstandard dependencies: none
- Random seed: none; deterministic exact rational calculation
- Target: accepted auxiliary first separated fixed-cell `GOCI_1` algebra,
  not the global identity-word law
- Convention: `(pq)(x)=p(q(x))`; displayed factors left-to-right
- Sole tested rank: `k=5`, `n=15`
- Admissible lags: `ell=2,...,13`
- Candidate: pre-frozen `(FMCP_1)` in `checkpoint.md`
- Exact command, run from this directory:

```text
python3 fmcp_k5.py --output fmcp_k5.json
```

- Raw output: `fmcp_k5.json`
- Expected failure mode: some fixed-middle cells are negative while the
  required positive `nu_M` average remains positive
- Observed: 16/120 cells negative; full channel-one lag row positive
- Downstream inference authorized: none

