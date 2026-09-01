# M266 run manifest

- Date: 2026-08-14 UTC
- Repository commit at start: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python: `3.12.3`
- Dependencies: Python standard library only
- Random seed: `null` (deterministic checker)
- Owned directory:
  `experiments/20260811-polynomial-mixing-resolution/cycle-72/mission-M266-full-dv-pcs-assembly/`

Commands:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-72/mission-M266-full-dv-pcs-assembly/verify_assembly.py
python3 -m compileall -q experiments/20260811-polynomial-mixing-resolution/cycle-72/mission-M266-full-dv-pcs-assembly/verify_assembly.py
```

The predecessor verification command was `sha256sum -c SHA256SUMS` in each
of the fourteen named immutable mission directories.  Every inventoried file
passed; checksum-file digests are in `dependency_manifest.md`.

