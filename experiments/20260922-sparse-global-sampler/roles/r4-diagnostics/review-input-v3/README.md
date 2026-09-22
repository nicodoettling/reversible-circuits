# Exact restricted sampler

From repository root:

```
timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r3-sampler/sampler.py --n 128 --m 16 --certificate-only
timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r3-sampler/sampler.py --n 5 --m 12 --seed 1729
timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r3-sampler/sampler.py --policy H1 --n 4 --m 6 --seed 1729
timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r3-sampler/audit.py experiments/20260922-sparse-global-sampler/roles/r3-sampler/results.json
```

Python API: `sample_h0(N,m,rng=None)` and `sample_h1(N,m,rng=None)` return a `RestrictedSample` with zero-based `word`, `cutoff`, candidate identity, exact total/allowed counts, `covered_mass` and `global_tv` as Fractions. `PreparedSampler(N,m,policy='H0')` reuses count and completion tables for repeated `.sample(rng)` calls. The CLI emits one-based labels, the target, exact certificate, source hashes and whether the input lies in T0's length range. H0 remains the default. `--test-cutoff` labels a different diagnostic candidate.

Both laws are uniform on their declared restricted subsets, not automatically globally uniform. No global negligible-error theorem is asserted by the code. The default `SystemRandom` interface models independent fair bits; seeded PRNG draws support reproducibility only. No nonstandard packages are required.

`sampler-v1.py`, `audit-v1.py`, `results-v1.json` preserve the initial H0-only review snapshot. To rerun that exact pair use `replay-v1.py` (which preloads and hash-checks sampler-v1), rather than launching audit-v1 directly after the current sampler has changed. All historical dependencies are read-only and hashed before execution; the loader does not create their bytecode caches.

Large exact counts that exceed Python's configured decimal conversion limit are emitted as `{"encoding":"hex","value":"0x..."}`. Large exact TV values use `{"encoding":"hex-rational","numerator":"0x...","denominator":"0x..."}`. These are exact representations; the API always returns native integers and Fractions. Interpreter limits are never changed.
