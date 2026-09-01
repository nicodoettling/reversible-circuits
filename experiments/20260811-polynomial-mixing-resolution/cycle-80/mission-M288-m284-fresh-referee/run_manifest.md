# M288 Run Manifest

- Date: 2026-08-14 UTC
- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python: `3.12.3`
- Nonstandard dependencies: none
- Random seed: none; the guard is deterministic
- Working directory:
  `experiments/20260811-polynomial-mixing-resolution/cycle-80/mission-M288-m284-fresh-referee`
- Command: `python3 -B convention_guard.py`
- Machine-readable output: `guard_results.json`
- Normalized result digest:
  `adcfb4cc7134cedeca1ec5241598dc8ab695cd513aec565fe577944608afe0f8`

The guard imports no M284 or predecessor code/data. It checks finite
convention-sensitive schemas only; the arbitrary-rank conclusions are
proved analytically in `proof_audit.md`.
