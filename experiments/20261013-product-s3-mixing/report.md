# Product-S3 mixing report

Date: 2026-10-13. Verdict: **keep**; author-complete proof with exact finite
falsification checks, pending independent mathematical review.

## Result

For G=(S3)^k acting on k disjoint labeled triples, use all 3k within-triple
transpositions. The target is uniform on every ordered identity word of a
fixed even length m>=2, with no fixed per-triple counts. The exact lazy
signed-Hurwitz / uniform-square-refresh kernel in `proof.md`, Section 1,
satisfies the author-proved bound

    gap >= 1/(200 k m^12),
    t_mix(epsilon) <= ceil(200 k m^12
                            [(m/2) log(3k)+log(1/epsilon)]).

This is a coarse polynomial existence bound, not a recommended practical
burn-in. It uses literal transpositions and a nonabelian group of order 6^k.
It does not cover cross-triple gates, all-transposition S_N, or a transitive
growing permutation action. No claim of novelty in the literature is made.

## Proof mechanism and audit focus

1. For fixed half-counts c, conditional words factor into a uniform color
   interleaving and independent S3 bridges. Each internal S3 prefix is an
   independent ternary coordinate.
2. The exact stationary-flow count projection is a complete-graph zero-range
   chain with g(0)=0, g(1)=6, g(r)=2r(2r-1) for r>=2. A direct discrepancy
   coupling proves its gap is at least 1/[2m(m-1)]. The observed counts of
   a nonequilibrium word chain are not asserted to be Markovian.
3. Within a count fiber, adjacent-color shuffling and compressed S3 heat
   baths have a polynomial gap. A shuttle of length at most 2m implements
   each compressed update with physical adjacent moves. The edge encoding
   by endpoints, phase and at most three choices bounds congestion by
   13k m^5; no atypical common hub is used.
4. An explicit variance decomposition combines the count and restriction
   gaps. The first unproved lemma for this exact family is **none** in the
   written argument; independent review, especially of the congestion
   encoding and variance constants, remains pending.

All inequalities and normalizations were rechecked by the same author.
There was no second agent, independent reviewer, or formal proof assistant.
The map therefore records this theorem as provisional, not accepted-reviewed.

## Exact checks

Command: `python3 -B experiments/20261013-product-s3-mixing/check.py`.
Start commit `1650532de223436eb09abb363e3a09efd6a44aba`.
Environment: Python 3.12.3; standard library only. Seed 20261013 recorded;
no randomness used. `results.json` records the script hash and environment.

| Family | Length | Exact identity words |
|---|---:|---:|
| S3, all transpositions | 4 | 27 |
| S4, all transpositions | 4 | 120 |
| S4, all transpositions | 6 | 3936 |
| S3 | 2 | 3 |
| S3 | 6 | 243 |
| S3 x S3 | 2 | 6 |
| S3 x S3 | 4 | 108 |
| S3 x S3 | 6 | 2916 |
| (S3)^3 | 4 | 243 |
| (S3)^3 | 6 | 10449 |

Every row passed exact word evaluation, row normalization, symmetry/detailed
balance, connectivity, per-position edge frequencies, Hurwitz preservation
of labeled weighted-support signatures, and crossing of those signatures
by the full chain. Raw exact histograms include prefix cycle types, edge
multiplicities, adjacent repeats, weighted supports and two-letter products.
In product cases, the count weights and every projected transition agree
exactly with the derived formulas. S4 checks validate the move harness only;
they imply no asymptotic S4 or S_N theorem.

The zero-range coupling passed 1080 neighboring-state marginal/drift checks
for k=2,3,4 and 1<=m/2<=5. The harness checked 28422 shuttle routes,
including all routes for (S3)^2 at length six. Every step is legal and
count-preserving; the maximum observed encoding multiplicity is two,
below the proved upper bound three. Exact congestion in that length-six
case is 250/3 for the B part of F, below the deliberately loose uniform
bound. The (S3)^3,length-six run checks the projection and kernel but does
not enumerate shuttle encodings. Boundaries m=0, odd lengths, m=2, k=1,
empty triples and the unrelated N=2 singleton passed.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| lazy Hurwitz + square refresh on (S3)^k | uniform fixed-length identity words over the 3k-gate alphabet | yes | yes | exact finite checks above; self-contained asymptotic proof separate | keep, independent review pending |

## Negative findings and limits retained

- Replacing every count by a positive-block formula loses the factor for
  empty triples and gives the wrong stationary law.
- Using square probability 1/3 at length two gives the wrong count rate.
- The direct-product group does not make the full chain a product chain:
  interleavings and variable counts required the additional argument.
- A connected transposition alphabet closed under Hurwitz conjugation is
  already complete on its support; see the elementary gate-graph argument
  in `proof.md`, Section 6. Sparse connected transposition graphs therefore
  do not automatically give a new closed generator model.
- All-transposition growing S_N mixing and products with growing block size
  remain unresolved by this investigation.

## Documentary integration

The project map registers this separate generator model provisionally. The
main all-transposition frontier, manuscript, HANDOFF, and skill are unchanged.
The pre-existing inventory discrepancy for absent
`.claude/settings.local.json` is recorded in the integration receipt; no
machine settings were created, edited or inspected to repair it.
