# M268 run manifest

- Date: 2026-08-14 UTC
- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python: `3.12.3`
- Dependencies: Python standard interpreter only; the checker imports none
- Random seed: `null` (deterministic)
- Owned directory:
  `experiments/20260811-polynomial-mixing-resolution/cycle-73/mission-M268-m266-fresh-referee/`

Principal retained commands:

```text
sha256sum --check SHA256SUMS
python3 -B independent_check.py
env PYTHONPYCACHEPREFIX=/tmp/m268_compile_cache python3 -m compileall -q independent_check.py
python3 -B verify_assembly.py
```

The first command was run in frozen M266 and every direct or delicate
transitive dependency directory recorded in `hash_audit.md`. The last
command was run in M266's directory. All commands passed. Network, Magma,
SAT, ILP, nonstandard packages, and randomness were not used.
