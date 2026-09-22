# Nonauthor sampler review — R4-REVIEW.v3

Verdict: **ACCEPT for the exact restricted sampling theorem and implementation/accounting stated below**, conditional on the named imported count theorem and, for H0 only, its named imported genus-zero/one sampler theorem. This is internal same-model nonauthor review. It does not independently certify the global negligible-error theorem T0 or replace human review of the imported mathematics.

Reviewed source SHA256: `56b27019396f93d4784032028ca1099d45ddd1cab1f740520c20c8c0169a8e06` (`sampler-v3.py`). Reviewed proof SHA256: `f941c5e141e229839813056da1169295b7b2c5d5a052886bc8edb69f096c1868` (`proof-v3.md`, containing the R3-S1.v2 theorem plus v3 serialization repair). Complete source/proof/audit/raw author-result inputs are preserved in `review-input-v3/`; hashes and receipt time are in `review-input-v3-manifest.json`. Earlier H0-only v1 review inputs remain in `review-input-v1/`. Acceptance is tied to these exact bytes.

## Accepted statement and scope

For N>=2 and every even m>=0, freeze K at the original input by the exact integer work-budget inequality. H0 samples exactly uniformly from words whose components have genus<=1 or support size<=K. H1 samples exactly uniformly from words whose nontrivial components have support size<=K. Both return exact length-m identity words and the exact rational retained-mass certificate. A diagnostic cutoff is a different labeled candidate. The exceptional empty word and rejected odd/empty fibers are stated correctly.

The elementary marked-state decoder and least-label assembly proofs are accepted on their merits. H1 requires the positive connected-count recurrence but no genus-zero/one endpoint-count or decoding theorem. The implementation imports the historical module to reuse elementary exact choices/unranking; its H1 path does not invoke the module's nontrivial count or sampling formulas. H0 additionally relies on the explicitly hash-frozen September7 primitive. The reviewer read its production choice/stack code and audited the integration; a new line-by-line external-source proof of that historical theorem is not claimed here.

## Source and probability audit

- `MarkedCounter` tracks `(remaining length, actual prefix permutation, canonical exposed-support partition)`. Right multiplication swaps permutation entries, matching the declared rightmost-first convention. Partition merging preserves the full support history needed by connected completions.
- The zero terminal state requires both identity endpoint and connected support. Its only pruning rule is sound: one further edge merges at most two support components. All nonzero transition probabilities are exact continuation-count ratios under the current prefix, so the telescoping proof is valid without an independence assertion.
- The explicit work stack is acyclic because every dependency lowers remaining length. A key is expanded once: pending same-depth siblings cannot be reached from lower-depth descendants. A cached duplicate is skipped. Finishing a parent sees all child counts. This validates the source's iterative execution rather than merely an equivalent recursive specification.
- Assembly branch weights are exactly `binom(n-1,v-1)binom(k,ell)C(v,ell)A(n-v,k-ell)`. `is_allowed` retains the original cutoff through every table cell and sampled residual problem. The uniform subset ranks cover all label and position subsets once; sorted selections preserve local word order under interleaving. For a fixed word the binomial and internal-count factors cancel, leaving `A(n-v,k-ell)/A(n,k)` and hence `1/A(N,m)`.
- The source uses integer rejection for random choices, with expected fewer than two attempts; one-element choices are exact. It returns a uniform restriction, and `(Z-A)/Z` is precisely its global TV distance. It never labels a positive certificate as global uniformity or derives negligibility from it.

## New current-version execution checks

`review_forward.py` loads only the frozen v3 bytes after checking their hash. It retains the original source filename for the historical loader's repository-root calculation; that does not alter the preserved bytes. The harness replaces abstract integer choices by exhaustive positive branches, executes the actual production sampler, and compares its literal-word law to an independently enumerated reference. It does not call the author's `word_probability` reconstruction. Before all H1 runs, the historical `g01.count` and `g01.sample` are replaced by functions that raise immediately.

| Policy/input | Actual forward paths = distinct words | Exact probability of every word | Global TV |
|---|---:|---:|---:|
| H1 N4,m6,actual K3 | 1056 | 1/1056 | 30/41 |
| H1 N4,m4,diagnostic K2 | 24 | 1/24 | 4/5 |
| H1 N4,m6,diagnostic K2 | 96 | 1/96 | 40/41 |
| H1 N3,m8,actual K3 | 2187 | 1/2187 | 0 |

All branches, literal endpoints, label/interleaving choices, total counts, and exact output probabilities pass. The poor small-instance H1 coverage is retained; these instances are outside T0 and are not counterexamples to its asymptotic claim.

A separate actual execution forces 37 isolated labels from top-level (42,12,K5), then selects the size5,length12 component on the remaining labels. Recomputing K on that residual problem would give4 and delete the branch. Both H0 and H1 production paths retain it. The selected concrete word consists of six repetitions of edge(37,38) followed by doubled edges(37,39),(37,40),(37,41), all zero-based. Its actual choice probability is respectively

    H0: 1/6771247112604328676721,
    H1: 1/6567808153112291607921,

exactly 1/A for each policy. This tests the residual behavior through actual forward execution, not only a branch-list assertion.

The actual marked decoder also generates the unique v2,length1400 identity word using1401 memo entries, with no recursion-limit modification. This supplements the author's recorded length1200 test. The factor m+1 in cache size is exercised directly.

`review_certificates.py` independently recomputes full-active-support coefficients and binomially embeds them into ambient N. Its ten exact current-v3 Z/A comparisons cover both policies at (42,12),(82,14),(128,16),(8,12),(6,16). All match. This includes the nonzero H0 tail inside T0 at (82,14), plus the independently repeated (128,16) row. It separates the H1 size-only error from H0's smaller intersection error.

Raw execution results are `review-forward-results.json` and `review-certificate-results.json`. Commands:

    timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r4-diagnostics/review_forward.py
    timeout 120s python3 -B experiments/20260922-sparse-global-sampler/roles/r4-diagnostics/review_certificates.py

The first run took about0.61s; the second about0.17s. The tests are deterministic exact choice enumeration. The singleton length1400 draw has no nontrivial randomness. No distributional conclusion is inferred from seeded Monte Carlo samples.

## Resource accounting audit

Let M=N+m+2, W=M^4, and Q=(m+1)KW. For each small support, `v! Bell(v)<=v^(2v)<=W`. The source retains all r<=m, so the full memo inventory is at most Q, including every retained component-size counter. Keys require O(K log(K+1)+log(m+1)+1) bits and values O((m+1)log M) bits. The pending explicit stack holds at most O((m+1)K^2) keys. Cache values are positive completion counts bounded by the number of all suffixes; no unit-cost exponential-count arithmetic is assumed.

The positive connected-count and assembly tables have polynomially many positive operations on polynomial-bit integers. Generation scans at most m next-edge choices plus polynomial label/position bookkeeping. Even charging a linear search for every dictionary operation, and charging standard integer and tuple operations conservatively, all costs remain polynomial. The stated coarse expected O(M^20) bit-time and O(M^10) storage bounds dominate the displayed contributions, including the m+1 factor, the fixed-capacity historical caches/explicit stack used only for H0, and integer powers used during cutoff binary search. Complexity is in N and m; nothing here makes it polynomial in log2N wires.

The author accounts for `Bell(v)` by least-element block encoding and for arbitrary ell by retaining its length index. No interpreter recursion bound or real-number arithmetic is hidden in this argument. The bound describes theoretical polynomiality; it is not a practical runtime guarantee for huge inputs.

## Repairs, negative findings, and limits

The v1/v2 CLI's direct decimal serialization is not uniformly robust under Python3.12's default large-integer conversion limit. Root/R5 identified this; the old snapshots are retained. v3 adds a lossless hex or hex-rational fallback without changing interpreter configuration. This reviewer inspected the source delta: the decimal-safety test conservatively implies the printed digit count is below the current limit, and base16 output is exact. R5 owns the dedicated serialization adversarial checks; this report does not substitute for them.

The v1 audit file imported mutable `sampler.py`; its frozen replay wrapper repairs review reproducibility by explicitly preloading hash-frozen `sampler-v1.py`. R4's own v3 harness directly checks and compiles frozen bytes and so does not inherit that ambiguity.

No new source or mathematical defect was found in current v3. Acceptance of the exact restriction and polynomial accounting does not certify the independent uniform omitted-mass proof. Root must close that claim graph with its primary-source and nonauthor theorem audits. All agreement here is correlated model-based review, not independent human certification.
