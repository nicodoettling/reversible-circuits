# Recommendations

## Immediate Next Worker Batch

Run 2 workers again, each with a 20-30 minute cap:

1. Worker C: implement a fixed-length block-resampling candidate for small `S_N,m`, using exact conditional block enumeration where feasible.
2. Worker D: implement square-refresh or null-block-refresh plus Hurwitz scrambling, then compare component occupancy and diagnostics against Worker A's exact reference.

## Acceptance Criteria for a Sampler Candidate

A candidate should be promoted only if it:

- preserves identity in all sampled words,
- can move between at least two Hurwitz components on exact small cases,
- has a declared target or stationary distribution,
- is compared against exact small-case diagnostics,
- records parameters and random seeds,
- documents a clear limitation or next falsification test.

## Avoid

Do not spend more effort on pure Hurwitz as a global sampler. It is useful as a within-component scrambler and as a negative-control baseline.
