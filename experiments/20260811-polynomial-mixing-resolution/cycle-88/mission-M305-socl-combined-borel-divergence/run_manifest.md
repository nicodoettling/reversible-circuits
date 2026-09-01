# M305 run manifest

Date: 2026-08-14 UTC.

- Mission: `M305-socl-combined-borel-divergence`
- Owner: `/root/m301_sstid_coset_helly`
- Target: the three exact M297/M302 SOCL rows in the auxiliary
  minimal-factorization model
- Convention: `(pq)(x)=p(q(x))`, displayed factors left-to-right
- Analytic scope: every odd `k>=3`, `n=3k`, `h_0=(k-1)/2`
- Computational scope: predeclared `k=11`, `n=33` only
- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Python: `3.12.3`
- Nonstandard dependencies: none
- Seed: null (deterministic exact enumeration)
- Elapsed wall time reported by script: `53.307632458163425` seconds
- Command, run from the mission directory:

```text
python3 -B cbpv_k11_guard.py --output cbpv_k11_results.json
```

- Imported executable: frozen M297 `bodt_k9_probe.py`
- Imported M297 script SHA-256:
  `9809433b8a978831d105f1de71f56f6f63424fa472756c6e3944b87390161b73`
- Imported M297 inventory SHA-256:
  `a1bfa3684113b84cad5741061fcebb860cc52461ef29f0f02e29752a68dc1792`
- Output: `cbpv_k11_results.json`

The script asserts source mass centering, exact 3/4 positive-composition
multiplicity, owner-size agreement, and complete source/type combination
before profile total variation.  It does not run a sampler or use random
data.
