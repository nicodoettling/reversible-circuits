# M08 report: fixed-endpoint aligned-H4 connectivity scan

## Candidate and claimed target

The candidate is the exact microfactorized `Q=P_transposition^2` bridge at a
fixed arbitrary endpoint, updated by aligned length-four same-product heat
baths. Equivalently, it is the length-`2l` transposition-word fiber of a
fixed even permutation, with windows starting at odd transposition positions.
The exact universal claim tested is qualitative connectivity of every such
nonempty fiber for `N>=3,l>=2`.

## Exact result

Every endpoint fiber is connected in all enumerated cases:

```text
N=3: l=2,3,4,5       (3 feasible endpoints)
N=4: l=2,3           (12 feasible endpoints)
N=5: l=3             (60 feasible endpoints)
```

The `N=5,l=3` run covers one million transposition words and is the first
listed case in which the two-step increment support is a proper subset of
the alternating group. Its endpoint-fiber sizes range from 15,625 to 20,860.
No fixed endpoint splits into multiple components.

This is an exact finite fact, not a universal proof. It cannot establish a
diameter, spectral gap, or mixing rate, and it cannot close M10's
`BASE-SCALE FIXED-ENDPOINT GAP` proposition.

## Method and normalization

Permutations use `(pq)(x)=p(q(x))`; a word is `t_1...t_{2l}`. For each
aligned window, the harness keys a heat-bath clique by its window position,
the exact outside word, and the ordered four-factor product. Unioning each
clique through one representative produces exactly the support graph of the
nonlazy aligned heat-bath chain. A runtime assertion verifies that no union
crosses a fixed endpoint. Connectivity is independent of the scan and
heat-bath probabilities, but no quantitative inference is made from that
fact.

The computation is deterministic, uses no random seed, and records Python
and commit metadata. Runtime is proportional to the number of enumerated
words times `l`; the largest run enumerates `10^6` words.

## Calibration and self-attack

- `l=2` is a whole-word heat bath and is necessarily connected; it is kept as
  a normalization check, not evidence for longer paths.
- `N=3` and `N=4` reproduce identity-fiber sizes 27/120 at word length four
  and 3,936 for `S_4` at word length six.
- All even endpoints are included, so the check is stronger than an identity
  bridge scan but still bounded.
- Odd transposition-word lengths, `m=2` for the original `{3,4,5}` chain,
  and the global stationary law are outside this harness.
- The strongest failure mode is a new fixed-endpoint component first appearing
  at larger `N` or `l`; absence through `N=5,l=3` gives no completeness
  argument.

## Artifacts and reproduction

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M08-fixed-endpoint-pair-resampling/exact_fixed_endpoint_connectivity.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M08-fixed-endpoint-pair-resampling/results.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M08-fixed-endpoint-pair-resampling/exact_fixed_endpoint_connectivity.py \
  --case 5,3 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-03/mission-M08-fixed-endpoint-pair-resampling/results_N5_l3.json
```

## Verdict

INCONCLUSIVE. The named universal connectivity claim survives its bounded
falsification suite; `BASE-SCALE FIXED-ENDPOINT GAP` remains open.
