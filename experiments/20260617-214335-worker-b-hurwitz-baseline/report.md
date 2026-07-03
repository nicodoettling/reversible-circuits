# Worker B: Pure Hurwitz Baseline

## Objective

Implement a self-contained pure Hurwitz sampler baseline for identity words in
transposition generators of `S_N`, then demonstrate on exact small cases that
pure Hurwitz moves are orbit/component samplers rather than global samplers for
the fixed-length uniform identity-word target.

Target distribution tested against: uniform on
`Omega(N,m) = { length-m transposition words with product id }`.

Sampler distribution: lazy pure Hurwitz random walk, which can only become
uniform within its starting Hurwitz component.

## Implementation Summary

Script: `hurwitz_baseline.py`

- Enumerates all length-`m` transposition words for the requested small `S_N`
  cases and filters to identity words.
- Applies right Hurwitz moves `(a,b) -> (b, b^-1 a b)` and inverse moves
  `(a,b) -> (a b a^-1, a)`.
- Builds exact Hurwitz components by BFS over the enumerated identity set.
- Records the weighted support-component invariant: connected components of
  the transposition support graph, weighted by number of factors in each
  component.
- Runs a lazy pure Hurwitz trace from the lexicographically first word and from
  a representative of the largest component.

Raw output: `results.jsonl`

## Commands Run

```sh
python3 -m compileall experiments/20260617-214335-worker-b-hurwitz-baseline/hurwitz_baseline.py
python3 experiments/20260617-214335-worker-b-hurwitz-baseline/hurwitz_baseline.py --output experiments/20260617-214335-worker-b-hurwitz-baseline/results.jsonl
sed -n '1,80p' experiments/20260617-214335-worker-b-hurwitz-baseline/results.jsonl
sed -n '81,160p' experiments/20260617-214335-worker-b-hurwitz-baseline/results.jsonl
```

The first sandboxed script run failed with `bwrap: loopback: Failed
RTM_NEWADDR: Operation not permitted`; the same local command was rerun outside
the sandbox with approval and completed successfully.

## Cases Tested

| Case | Identity words | Hurwitz components | Component sizes | Weighted invariant classes | Best pure-Hurwitz TV lower bound vs global uniform |
| --- | ---: | ---: | --- | ---: | ---: |
| `S_3, m=4` | 27 | 4 | `24, 1, 1, 1` | 4 | `0.111111` |
| `S_4, m=4` | 120 | 13 | `24x4, 6x3, 1x6` | 13 | `0.800000` |
| `S_4, m=6` | 3936 | 17 | `2880, 240x4, 15x6, 1x6` | 17 | `0.268293` |

All three identity-word and component counts match the project reference smoke
cases. Hurwitz product-preservation failures during component construction:
`0` for all cases.

## Orbit/Component Evidence

Pure Hurwitz moves did not leave the starting component in any trace:

| Case | Seed | Seed component size | Unique words seen / steps | Visited components | Identity failures | Invariant changed |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `S_3, m=4` | lexicographic first | 1 | `1 / 20000` | 1 | 0 | false |
| `S_3, m=4` | largest component | 24 | `24 / 20000` | 1 | 0 | false |
| `S_4, m=4` | lexicographic first | 1 | `1 / 20000` | 1 | 0 | false |
| `S_4, m=4` | largest component | 24 | `24 / 20000` | 1 | 0 | false |
| `S_4, m=6` | lexicographic first | 1 | `1 / 20000` | 1 | 0 | false |
| `S_4, m=6` | largest component | 2880 | `2596 / 20000` | 1 | 0 | false |

For these exact small cases, every Hurwitz component had a single weighted
support invariant, and the number of weighted invariant classes equaled the
number of Hurwitz components. Thus the obstruction is visible without any
mixing-time argument: starting in one component assigns zero probability to all
identity words outside it. Even choosing the largest component leaves exact TV
distance at least `1 - |C|max / |Omega|`, shown in the table above.

## Limitations

- This is not a broad exact harness; it is a small self-contained baseline for
  `S_3,m=4`, `S_4,m=4`, and `S_4,m=6`.
- The lazy walk traces are empirical sanity checks only. They are not mixing
  proofs within a component.
- The obstruction shown here is for pure Hurwitz moves. It does not test
  orbit-breaking moves such as square refresh, null-block refresh, or exact
  fixed-length block resampling.

## Next Steps

- Add an orbit-breaking move and compare exact component masses against the
  global fixed-length uniform target on the same small cases.
- Use Worker A's exact-reference harness later only as a validator, not as part
  of this Worker B baseline.
- For larger `N`, skip enumeration and track invariant diagnostics plus
  identity preservation under the proposed orbit-breaking chain.
