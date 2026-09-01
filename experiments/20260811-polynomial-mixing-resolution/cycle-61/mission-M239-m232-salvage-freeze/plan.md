# M239 plan: interrupted-M232 YCM salvage and independent audit

Date: 2026-08-13 UTC.

## Objective

Treat M232 as interrupted before freeze and independently decide the exact
one-run coefficient moment (YCM)

    |sum_(y=2)^ell c^Y_(k,y)| <= C sqrt(ell)/k

uniformly for odd `k>=3` and `2<=ell<=(3k-1)/2`, using only the frozen
M226/M229 coefficient interface and immutable snapshots of M232's durable
`plan.md` and `checkpoint.md`.

The deliverable must be one of:

- a fully quantified proof with an explicit universal constant; or
- a strict reduction that identifies the first unproved constant lemma or an
  exact counterexample.

## Immutable gate and source lock

1. Verify M226 and M229 from within their own directories using their frozen
   `SHA256SUMS`, and record the checksum-file digests.
2. Record SHA-256 hashes of M232 `plan.md` and `checkpoint.md`; never edit M232.
3. Record repository commit, Python version, and the exact checker command.
4. Use the M229-corrected domain
   `1<=x<=(3k-3)/2` for every invocation of `G_k(x)`.

## Independent proof audit

Re-derive the coefficients from M226/M229 rather than accepting M232's
skeleton. Audit, with explicit ranges and constants:

1. the stated elementary Stirling/Borel bounds and ratio recurrence;
2. the small-argument estimate SG;
3. global estimates GG1 and GG2;
4. all four coefficient regions, including both seams;
5. odd boundary ranks and the corrected `G_k` domain.

Use a clean-room exact-formula checker only at odd `k<=21`, and only for
falsification of displayed identities or candidate inequalities.

## Exclusions

No TCM, WBE, DE, J2, downstream spectral-gap or mixing claim, and no Terminal
inference.

## Deliverables and freeze

Write `checkpoint.md`, a proof or strict reduction, checker and raw results,
`report.md`, `freeze_manifest.md`, and `SHA256SUMS`. Freeze all deliverables
before requesting independent review.
