# Endpoint-blind initialization: meaningful consequences and the remaining gap

Verdict: **keep** the scoped proofs and exact checks, provisionally pending
independent review. The proposed identity-to-arbitrary-endpoint implication
for the original local chain remains **unresolved**, not refuted.

## Research conclusion

The user's condition is meaningful, but it controls local observations
while allowing hidden constraints on products of long prefixes. This can
be demonstrated inside the actual transposition-word model, without an
unrelated artificial state space.

Take an independent long identity bridge A and a long g bridge B. Every
short gate window, including windows crossing the join, is nearly iid,
uniformly over g. Nevertheless the product of A is pinned to identity.
Under the uniform full bridge, that prefix product has identity probability
about 2/N!. The global distance is therefore about 1-2/N!.

In S3 this is exact: every set of k<min(|A|,|B|) gates is iid, and the
global TV distance is 2/3. For half-lazy adjacent two-factor heat bath the
distance at time t is exactly (2/3)(1-1/[2(m-1)])^t. All those local gate
marginals remain iid throughout. This is a slowest mode, although its
relaxation time is polynomial. It refutes the intermediate claim that
local blindness removes all slow modes, not the user's mixing conjecture.

Two useful quantitative results follow. A backward influence-interval
argument gives an explicit binomial bound on how long local blindness
persists under the user's finite-range moves. Many hidden prefix pins
give an order m log q coupon lower bound, compatible with rapid mixing.

There is also a positive floating-window theorem. At a smoothing scale L,
partition the word into q blocks of lengths between L and 2L-1. Half-lazy
refresh of a uniform adjacent pair of whole blocks mixes for every
endpoint from every start in O(q log(q/epsilon)) completed exact refreshes.
The proof tracks the intermediate prefix products and then the interiors.
A conservative directly verified scale is L=O(N^2 log N); the archive
already supplies a sharper O(N log N) pointwise-smoothing input.

For the actual adjacent Hurwitz/square chain the precise comparison is

    gap(K_A on Omega_g(N,m)) >= (2L-1) gamma_*/[16(m-1)],

where gamma_* is the minimum gap of the SAME local chain over every
endpoint and block length 2L,...,4L-2. The half mixture with Q345 inherits
half this bound. A polynomial gamma_* would prove all-endpoint polynomial
mixing in the long-circuit regime. An identity-only hypothesis controls
one of those block endpoints and does not yet supply the minimum.

The useful next target is therefore a theorem about arbitrary-endpoint
block relaxation, or an initializer-specific spectral comparison that
bypasses its worst-case minimum. Checking only small gate histograms
cannot settle that target; intermediate prefix products should be included
in diagnostics. The existing experiment guide already requires prefix
cycle diagnostics, so no workflow-skill edit is needed.

## Exact validation and reproducibility

Command:

    python3 -B experiments/20261019-140150-local-endpoint-blindness/check.py

Commit: 4699f218df63bc2ff5c91e645e4bf08300490bfd. Python 3.12.3,
standard library only. No random seeds: checks are deterministic and
exhaustive in their declared domains. The JSONL manifest pins the script.

- 23,823 integer marginal equalities in S3,m4,m5 and S4,m4,m5,m6,
  covering every feasible endpoint cycle type and arbitrary subsets up
  to three positions. Odd endpoint fibers are included.
- 62,571 primitive K_A channels checked for endpoint preservation,
  exact detailed balance and full-fiber connectivity on identity S3,m4
  (27 words), S4,m4 (120), S4,m6 (3936). The pure Hurwitz component
  counts are 4,13,17, respectively.
- All 6561 S3 words at length eight, grouped into three endpoint fibers:
  exact three-wise independence of the pinned initializer, rational
  eigenfunction equalities, and exact distributions through time three.
  Eigenvalues are 13/14 for Q2 and 61/90 for Q345 at the central cut.
- 19,805 influence-interval cases; exact coupon moment inequalities;
  144 conditional coarse-coordinate laws in S4 at block length five;
  8,029 slot normalization checks for the actual-chain comparison.
- Exact bridge-count recurrences through S5,m126; boundary cases
  N2 and m0,1,2. No dense claim is extended to near-minimal fibers.

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
|---|---|---|---|---|---|
| Actual K_A and a specified mixture with Q345 | Uniform fixed-length prescribed-product words | yes for every checked primitive channel | K_A connected in all three required identity cases | detailed balance, prefix pins, exact local marginals; no general gap inferred | keep; global mixing unresolved |
| Ideal overlapping long-block heat bath | Same uniform fixed-product target | exact by construction | full mixing proved under smoothing and an exact block oracle | conditional law/geometry checks; proof applies to all endpoints | keep as analytic comparison; not a small-move implementation |

## Dependencies and limits

The smoothing input uses CLR Theorem 1.1; the primary statement and
normalization were checked. The macro coupling and actual-chain comparison
are proved in proof.md. Archive M10 and its referee were read to reconcile
the existing stronger overlap scale and base-gap reduction. No M340
transport assertion is used. No general mixing conclusion is extrapolated
from finite spectra. There is no independent referee, manuscript change,
HANDOFF change, install, commit, push, or external message.

## Workspace changes

New files in this experiment directory: plan.md, proof.md, check.py,
results.jsonl, claim_ledger.md, report.md.

New map receipt: notes/project-map/integration-2026-10-19-local-endpoint-blindness.md.

Already-dirty map files updated further: PROJECT_MAP.md,
notes/project-map/COVERAGE.md, notes/project-map/RESULTS.md,
notes/project-map/catalogue.json, notes/project-map/inventory.json.

Pre-existing untracked research is preserved: the October 14 cycle-excess
directory; October 15 adjacent-gap-proof, all-pair-interval-gap,
support-marginal-audit, and parallel-hurwitz-layers directories; their
five existing integration receipts. No files in those directories changed.
The new receipt records the map checks and discovery scope.
