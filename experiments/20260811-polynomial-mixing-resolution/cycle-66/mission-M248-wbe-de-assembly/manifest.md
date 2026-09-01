# M248 freeze manifest

Date: 2026-08-14 UTC.

## Source lock and environment

- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: `3.12.3`.
- Permutation convention: `(pq)(x)=p(q(x))`, displayed factors
  left-to-right.
- The checker is deterministic, seed null, standard-library syntax with no
  imports, and loads no predecessor code or data.
- No network, nonstandard dependency, Magma, SAT, or ILP was used.

## Frozen dependency inventory digests

```text
M217 7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557
M222 d2a43d9049fcfd5be96f1167142979d4daa6cb72345d3b26f28cdda36aae7ccd
M226 a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a
M229 6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688
M235 7e929497029ae0c007d0544d30f0ad3c0198947ce55f946ee7eb0aaa88b19527
M238 eb7bd2ef5bfb660f0e79978e3e7bd583876abb4f5d33320a97e098b61b33b4e8
M239 66c78dd3aab40acc6166857f96f3afd90bba64184d7f139783d395667d21f542
M246 df0774fc40bc4fc411624c4a7153acda10a16b63bbd2c53600e12944febe2e97
```

Every corresponding `sha256sum -c SHA256SUMS` command passed before proof
assembly. No dependency file was edited.

## Reproduction

From repository root:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-66/mission-M248-wbe-de-assembly/algebra_domain_check.py
```

Its single JSON line agrees exactly with `results.json` modulo whitespace
and object-key order.

## Frozen verdict

WBE is proved with constants `7000` for `Y_ell` and `7160` for `X_ell`.
The exact normalizer remainder is at most `16/k^2`, and signed averaged DE
is proved with constants `7004` and `7164`, respectively. This verdict is
subject to a fresh immutable audit of M248.

DV and all later claims remain open. In particular, M248 makes no conditional
J2, PCR/WPCR/SCBR, comparison, spectral-gap, mixing, or Terminal inference.

## Frozen file set

```text
plan.md
checkpoint.md
wbe_de_theorem.md
algebra_domain_check.py
results.json
report.md
fresh_audit_request.md
manifest.md
```

`SHA256SUMS` is generated last over exactly these eight files. No cache or
temporary output belongs in the mission.

