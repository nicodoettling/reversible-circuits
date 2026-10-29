# Arbitrary-pair interval-gap integration, 2026-10-15

Prior commit: `4699f218df63bc2ff5c91e645e4bf08300490bfd`. The user asked
whether applying the displayed lifted move to arbitrary gate pairs gives
fast mixing. Five map files and two prior research directories/receipts
were already dirty; prior research artifacts are preserved unchanged.
No agents, packages, commits or pushes.

## Scope and review

Add HB-ALLPAIR-INTERVAL version 1, provisional. Its all-N stationary-flow
comparison strengthens the constant in HB-NONLOCAL-LIFT without changing
that older record or proof. Its S3 Fourier argument proves an actual mixed
pair-chain gap of order 1/m at every feasible endpoint. A does-not-imply
relation retains the growing-N N+1 gap as unresolved. Project priorities
and every existing status/source fingerprint are unchanged.

The six new artifacts were inspected. The exact script passed. This is
same-author mathematical and computational work, not independent review.
No literature theorem is needed for these new comparisons or Fourier
calculations. All-endpoint connectivity cites the previously inspected
constructive proof. Finite enumeration is not used as an asymptotic proof.

## Discovery

Before new files, validation of 45 records and 87 sources, freshness,
render checking, and all 19 map tests passed. Candidate inventory
`/tmp/reversible-all-pair-candidate.json` records exactly six new research
files and no edits/deletions of prior research. This delta is reviewed;
the new family is mapped explicitly, with no coverage exclusion changes.
All modified and preserved dirty files are listed in the new report.md.

## Source fingerprints

- `experiments/20261015-113600-all-pair-interval-gap/proof.md`: `bdbe27db6be6f89dd227425eb793d0aa7869421dd55862d3c87a09304b781a1d`.
- `experiments/20261015-113600-all-pair-interval-gap/check.py`: `1e6b1d0100c9d316a67a8cb848902bb0af63ee220fbae13557096c784921ae92`.
- `experiments/20261015-113600-all-pair-interval-gap/results.jsonl`: `2b0fa5c769143759eaae0c66f9990345768f7dfd9b8f7205c07ae7512171a2be`.
- `experiments/20261015-113600-all-pair-interval-gap/plan.md`: `75366db8536f44ef6817a51049acc47e24f49688a0a64035eedd0b933806ae49`.
- `experiments/20261015-113600-all-pair-interval-gap/report.md`: `39899ad6264cdcc18f309120e8f23b68c4334b7f4c8c2b42a0cf6ac04f360d18`.
- `experiments/20261015-113600-all-pair-interval-gap/claim_ledger.md`: `f66eb87c49f59005686f7db08203e801315ce5e80248f07fe0cfde1d3aa82bb6`.

## Final checks

Completed: validation passed for 46 records and 93 pinned sources;
freshness reported no new, missing or changed entries; deterministic
render checking and all 19 map tests passed. Retrieval of
HB-ALLPAIR-INTERVAL returned the scoped S3 theorem and unresolved growing-N
limit. `git diff --check` passed, and final `git status --short` matched
the complete changed-file inventory in the report. Prior research hashes
were unchanged in the reviewed discovery delta.
