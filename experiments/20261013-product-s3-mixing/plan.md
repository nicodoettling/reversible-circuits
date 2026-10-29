# Product-of-triples Hurwitz / square-refresh mixing

Date: 2026-10-13 (Europe/Berlin).
Start commit: `1650532de223436eb09abb363e3a09efd6a44aba`.
Authorization: user asked to try a more complex permutation family after the
S3 and prime-dihedral examples. Single-coordinator investigation, no workers.

## Target and tested claim

Let k disjoint labeled triples support G=(S3)^k <= S_(3k). The alphabet T
contains all three transpositions in each triple. Target: globally uniform
ordered length-m identity words over T, without fixing the per-triple counts.
Products act rightmost first. Parameters: k>=1, even m>=2.

Kernel: half hold; one quarter uniformly positioned signed Hurwitz; one
quarter uniformly positioned square refresh, choosing the replacement
transposition uniformly from all 3k gates, and holding if the pair is unequal.
Positions are linear, 1 through m-1; there is no wraparound.

Goal: self-contained polynomial spectral-gap bound in k and m, using the
exact stationary-flow projection onto half-counts, within-count fiber
comparison, and a variance decomposition. Provisional until the written
argument and its finite falsification checks are complete; no theorem about
the unrestricted S_N alphabet or the repository's {3,4,5} kernel is intended.

## Failure modes

- Incorrect empty-triple weight or exceptional length-two square frequency.
- Confusing the stationary-flow projection with a Markovian observed process.
- A count process that is slow or has the wrong reversible measure.
- Assuming that consecutive letters in a compressed triple word are adjacent
  in the full word; shuttle paths must account for the discrepancy.
- Exponential comparison congestion from a noninjective path encoding.
- Mistaking a product of groups for independent complete words: the counts
  and interleaving still require mixing.

## Checks and reproducibility

Run `python3 -B experiments/20261013-product-s3-mixing/check.py` from the
repository root. Python 3.12.3, standard library only. All checks are
deterministic exhaustive checks; seed 20261013 is recorded but unused.
Raw output: `results.json`. Check the S3,m4; S4,m4; S4,m6 baseline kernel,
then product-S3 cases including changing occupancies and shuttle paths.
No numerical spectrum or Monte Carlo trace is used as an asymptotic proof.

Boundary checks: odd m, m=0, m=2, k=1, empty triples, all mass in one
triple, and one pair per occupied triple. The unrelated N=2 single-generator
case is a singleton at even length.

## Map baseline

Before writing research artifacts, map validation, deterministic rendering,
and all 19 unit tests passed. Freshness already failed because
`.claude/settings.local.json` is missing from disk relative to the inventory.
Do not attribute that pre-existing discrepancy to this investigation.
