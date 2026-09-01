# M249 freeze manifest

Date: 2026-08-14 UTC.

## Source and environment

- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
- Python: `3.12.3`.
- Permutation convention inherited from the audited sources:
  `(pq)(x)=p(q(x))`, displayed factors left-to-right.
- Checker: deterministic, seed null, no imports, no predecessor code or data.
- No network, nonstandard dependency, Magma, SAT, or ILP was used.

## Audited source locks

```text
M248 c3726d05943b696c11f8e984fae9aa0ee342d00c0744bd7bf0a0f665acbe8bd8
M217 7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557
M222 d2a43d9049fcfd5be96f1167142979d4daa6cb72345d3b26f28cdda36aae7ccd
M226 a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a
M229 6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688
M235 7e929497029ae0c007d0544d30f0ad3c0198947ce55f946ee7eb0aaa88b19527
M238 eb7bd2ef5bfb660f0e79978e3e7bd583876abb4f5d33320a97e098b61b33b4e8
M239 66c78dd3aab40acc6166857f96f3afd90bba64184d7f139783d395667d21f542
M246 df0774fc40bc4fc411624c4a7153acda10a16b63bbd2c53600e12944febe2e97
```

Every entry in every named inventory passed before the proof audit. The
values above are SHA-256 digests of the corresponding `SHA256SUMS` files.

## Reproduction

From repository root:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-67/mission-M249-m248-fresh-referee/independent_check.py
```

The single JSON line agrees with `results.json` on every checker-produced
field.

## Frozen verdict and scope

ACCEPT M248: WBE constants `7000,7160`, normalizer bound `16/k^2`, and
signed averaged DE constants `7004,7164` are proved on the complete stated
domain. DV and all named downstream consequences remain open.

## Frozen file set

```text
plan.md
checkpoint.md
proof_audit.md
independent_check.py
results.json
report.md
manifest.md
```

`SHA256SUMS` is generated last over exactly these seven files.
