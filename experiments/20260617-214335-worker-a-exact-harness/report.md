# Worker A Exact Enumeration Harness

## Objective

Build a small exact reference harness for fixed-length identity transposition words in `S_N`, with diagnostics that sampler candidates can compare against.

Target distribution: uniform on

```text
Omega(N,m) = { (t1, ..., tm) : each ti is a transposition in S_N and t1...tm = id }.
```

## Implementation Summary

The script `exact_identity_harness.py` is self-contained Python and uses no third-party packages. It enumerates all transposition words for each requested small case, filters identity words by exact tuple-permutation arithmetic, and builds the pure Hurwitz graph on the retained identity words.

Multiplication convention: permutations are tuples `p[x] = image of x`; a word is evaluated as `(((id*t1)*t2)*...*tm)`, with `(p*t)[x] = p[t[x]]` for a transposition `t`.

## Commands Run

```bash
python3 exact_identity_harness.py --cases 3:4 4:4 4:6 --output results.jsonl --report report.md
```

## Exact Counts

| Case | Total words | Identity words | Expected | Hurwitz components | Expected components | Validated |
|---|---:|---:|---:|---:|---:|---|
| `S_3, m=4` | 81 | 27 | 27 | 4 | 4 | count yes; components yes |
| `S_4, m=4` | 1296 | 120 | 120 | 13 | 13 | count yes; components yes |
| `S_4, m=6` | 46656 | 3936 | 3936 | 17 | 17 | count yes; components yes |

## Diagnostics Implemented

- identity-word count and density among all transposition words
- Hurwitz component count, size histogram, representatives, and invariant checks
- prefix cycle-type counts at every prefix length
- per-position transposition frequencies
- adjacent-repeat count distribution and aggregate adjacent-repeat rate
- support graph component-shape and weighted labeled component-invariant distributions
- support-edge count and edge-multiplicity histogram distributions
- length-2 and length-3 window product cycle-type counts

## Selected Diagnostics

### `S_3, m=4`

- identity density: `0.333333333333`
- Hurwitz component size histogram: `{'1': 3, '24': 1}`
- adjacent repeat distribution: `{'0': 12, '1': 6, '2': 6, '3': 3}`
- support shape distribution: `{'1:0|2:4': 3, '3:4': 24}`

### `S_4, m=4`

- identity density: `0.0925925925926`
- Hurwitz component size histogram: `{'1': 6, '6': 3, '24': 4}`
- adjacent repeat distribution: `{'0': 54, '1': 30, '2': 30, '3': 6}`
- support shape distribution: `{'1:0|1:0|2:4': 6, '1:0|3:4': 96, '2:2|2:2': 18}`

### `S_4, m=6`

- identity density: `0.0843621399177`
- Hurwitz component size histogram: `{'1': 6, '15': 6, '240': 4, '2880': 1}`
- adjacent repeat distribution: `{'0': 1656, '1': 1338, '2': 636, '3': 240, '4': 60, '5': 6}`
- support shape distribution: `{'1:0|1:0|2:6': 6, '1:0|3:6': 960, '2:2|2:4': 90, '4:6': 2880}`

## Limitations

This is direct word enumeration, so it is only intended for small `N,m`. The default guard refuses cases above `--max-total-words` total words. No sampler is implemented here, and no mixing-time claim is made from the Hurwitz components.

## Next Steps

Use `results.jsonl` as an exact baseline for sampler runs. A sampler comparison script can consume the prefix cycle-type, per-position, support-shape, edge-multiplicity, and adjacent-repeat distributions as reference marginals.
