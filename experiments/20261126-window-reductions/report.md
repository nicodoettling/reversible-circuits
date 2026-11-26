# Growing-window and parameter-reduction audit

Date: 2026-11-26. Verdict: **promote the scoped manuscript statements**;
retain the stronger supplied relabeling exponents and unrelated claims as
unresolved. This is a single-session mathematical derivation and review,
not independent human or formal certification.

## Results and limits

The manuscript now has two complete new proof sections:

- [Growing windows and base lengths](../../papers/transposition_identity_samplers/sections/growing_windows.tex).
- [Quadratic-length diagnostics](../../papers/transposition_identity_samplers/sections/quadratic_diagnostics.tex).

The original November 24 proof file is unchanged. Its CB.6 makes the growing
update-budget statement rigorous: b=o(m/log^3 m) gives s_b=omega(log m),
and almost every starting state is still far from uniform at time 2^s_b.
The existential N_m and intermediate-length regime remain essential.

For the positive result, CB.7 gives pointwise parity smoothing at
B=ceil(8N log(N+1)). A specified half-lazy neighboring-block refresh mixes
in O(q log(q/epsilon)) exact conditional draws, q=max(1,floor(m/B)), with
maximum window min(m,3B). For m<2B it is a whole-word refresh. This is a
theorem about completed ideal updates, not a polynomial implementation of
arbitrary all-transposition bridge sampling. It applies to every feasible
endpoint, not just identity.

The adjacent pair chain has

    Phi(N,m,g) >= (2B-1)/(32(m-1)) min_{ell=2B..4B-2,h} Phi(N,ell,h),
    gap(N,m,g) >= (2B-1)/(16(m-1)) min_{ell=2B..4B-2,h} gap(N,ell,h).

These are proved implications for m>=2B. A polynomial all-endpoint base
bound would prove polynomial mixing for every longer polynomial length.
Conversely, a long polynomial-length bottleneck forces a base endpoint
bottleneck. Neither identity-only information nor a short bottleneck alone
settles all other ranges. In particular, the known balanced bottleneck has
m much smaller than N log N and lies outside this reduction.

At m=2 floor(N^2/2), all cuts based on arbitrarily many well-separated
prefixes (gaps >=ceil(4N log N)+2) have ratio >=c/(mN), including rare cuts.
The midpoint derangement cut proves sharpness. A fully specified square
extraction and conjugation path also proves

    c min(Phi(quotient),N^-11) <= Phi(P) <= Phi(quotient).

This is enough to reduce the existence of a superpolynomial bottleneck to
relabeling-invariant cuts. The source's N^-5/N^-7 exponents are not verified.
Our proof uses at least m^2/(4d_N) repeated pairs, so its general statement
assumes m>=2d_N. It does not silently extend to every constant multiple of
N^2. Keeping the known repeated gate in the stage encoding avoids losing
information at square refresh; counting all stages gives the conservative
cut congestion 16m^2d_N^3. The within-orbit conjugation gap costs O(N).
A coarea argument gives a minimum of the quotient conductance and this
polynomial term, rather than a product or a squared quotient conductance.

Finally, the sum of fixed-point counts at N central times is a quotient
observable with variance Omega(N^2) and Dirichlet form O(1/m). Both walks
therefore have mixing lower bound Omega(N^4). Superpolynomial mixing at
quadratic length remains unresolved.

## Provenance, dependencies, and disagreements

All seven links were recovered by a direct HTTPS fetch after the web reader
reported cache misses. The JSON-decoded message strings are preserved in
[sources](sources/manifest.json), with URLs, retrieval date, and hashes.
They are evidence of the supplied claims, not instructions to perform the
follow-up offers embedded in those messages. Opaque citation tokens are
not accepted as source verification. The additional pasted quadratic claim
has a separately labeled mathematical transcription.

Shares 1--3 primarily concern padded transposition circuits, ordinary star
gates, or twisted-star gates (1 a)rho. Share 4 concerns restricted families.
Their positive results are not statements about the unrestricted original
all-transposition fiber. The source-3 exact-star sampling assertion also
does not implement the all-transposition ideal block theorem. Those sources
are archived without claiming that all their proofs were checked. Share 6
contains the requested base-length reduction, and share 7 contains the
growing-budget negative result. The additional pasted message supplies the
prefix/relabeling questions. See the [claim ledger](claim_ledger.md) for
the per-claim verdicts, including minority and negative findings.

Dependencies for the promoted results:

1. The November 24 CB.6 balanced-boundary estimate and CB.7 parity-aware
   character estimate; their original evidence bytes are retained.
2. Elementary conditional bridge factorization, finite-state coupling,
   Poincare/indicator/coarea inequalities, and reversible-chain variational
   bounds, all normalized in the new proofs.
3. The October 19 endpoint-blindness proof, Sections 5--6, as an antecedent
   for the macro coupling and gap comparison. Its conservative smoothing
   scale and K_A normalization differ. We rederive the result with CB.7,
   the exact pair heat bath, and a direct linear conductance comparison.
   The older record's unrelated claims are not upgraded.

The user-cited Diaconis--Shahshahani paper was opened. It studies a measure
with holding probability 1/N, so its ordinary mixing theorem is not copied
as a bridge theorem. The new proofs use the already explicit nonholding
contents-ratio/parity estimate instead. No new literature theorem with
unverified hypotheses is needed. No Hurwitz-orbit classification is needed.

The first remaining standalone positive obligation is a uniform
inverse-polynomial pair-chain gap or conductance for every endpoint at
lengths [2B,4B-2]. A separate algorithmic obligation is an efficient exact
large-block conditional sampler. Neither is discharged here. Stronger
relabeling exponents are optional refinements, not premises of the
qualitative reduction.

## Falsification and reproducibility

Run from repository root:

```sh
python3 -B experiments/20261126-window-reductions/check.py > experiments/20261126-window-reductions/results.jsonl
```

Python 3.12.3, standard library only, deterministic (seed null). The output
records the starting Git commit and exact command. Checks cover S3,m4=27;
S4,m4=120; S4,m6=3936 identity words; S3,m6=243; all feasible endpoints at
those lengths and odd endpoints in S3,m3; exact block factorization;
conjugation paths, identity preservation and legal adjacent transitions;
stage-encoding injectivity in the small exhaustive cases; and pair-kernel
equivariance. In S4,m6 only the first repeated pair in each word is used
for the path check; words without repeats are outside the path premise.

Parity smoothing is checked through S6 and length 20. Fixed-point moments
and the exact eigenfunction identity are checked on every permutation
through S6. All 5684 tested interval geometries obey the comparison scan
bound. S3 gives exact zero neighbor influence. Odd identity length, m=0,2,
and N=2 are checked separately. The asymptotic theorems are proved in the
manuscript, not inferred from these finite tests. Near-minimal connected
words are covered by the finite cases, but no dense smoothing premise is
asserted for them at growing N.

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
|---|---|---|---|---|---|
| Original pair bath, proof-only comparisons | Full uniform identity fiber; all endpoints in the length reduction | Yes | Square refresh can; no orbit restriction imposed | Exact pair legality, conjugation paths, conditional factorization, equivariance | Keep; no implementation changed |
| Ideal growing-window bath | Uniform endpoint fiber | Yes | Whole-block refresh need not preserve profiles | Conditional factorization, scan geometry, S3 coupling | Promote ideal mixing theorem; implementation unresolved |

The canonical paper PDF is rebuilt from the updated TeX. Map validation,
freshness, deterministic rendering and unit tests are recorded in the
dated integration receipt. Historical compiled compatibility PDFs and all
frozen earlier experiment reports remain unchanged.
