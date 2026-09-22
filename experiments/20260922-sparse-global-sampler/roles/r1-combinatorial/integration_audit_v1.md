# Final synthesis audit — R1-INT.v1

Recorded 2026-09-22T06:11:25.869659+00:00. **Verdict: mathematical integration ACCEPT; final CLI delivery REPAIR REQUIRED pending a policy-label correction.** The required correction concerns output semantics, not the sampler law or tail proof. Its exact version must be rechecked before final acceptance.

Reviewer `/root/r1_combinatorial` authored the analytic subsection underlying the synthesis and therefore supplies a consistency review, not an independent analytic certification, for those sections. The reviewer did not author the coordinator's synthesis/wrapper or R3 sampler. The review is not blind and remains correlated same-model evidence.

## Exact inputs

Complete byte snapshots and hashes are preserved in `integration_audit_inputs/manifest.json`:

- Canonical SG-T1.v1 `proof.md`: d03954bd1530ae0e3a6b8f4feb6c2fa97520c6048f1089f3a3e2bc26ab684319.
- Root `sample.py`: 5e78c049d188280f8df2b7b2fa0ff984fc3e6fd92aadf3eae9d033d1145a6188.
- R3 proof-v3: f941c5e141e229839813056da1169295b7b2c5d5a052886bc8edb69f096c1868.
- R3 sampler-v3: 56b27019396f93d4784032028ca1099d45ddd1cab1f740520c20c8c0169a8e06.
- R4 sampler review-v3: d673444cc3a0273c44a775f69c176b8ac687b8806ef6db272c29a79686fe44b8.

All five files were read completely. The immutable own analytic proof and prior exact results were used for comparison. Cap sidecars were reread first; the original hard deadline remains 09:43:44.791045 UTC, with no extension.

## Mathematical consistency — accepted

**INT-M1, target and quantifiers.** Canonical T0 remains m^5<=N^3. SG-T1.v1 explicitly strengthens to m^3<=N^2, with the same H0 definition and fixed top-level K. H1 is separately named and has B subset A. The asymptotic bound is uniform over all even lengths in the declared range, with no parameter or algorithm depending on the inverse-power exponent. The exact conditional algorithms remain defined at all even lengths, while the negligible error guarantee is expressly confined to T1.

**INT-M2, constants.** The majorant b_v=(v^3-v)/36, fresh-pair factor 4^q q!binom(k,q), finite tail cubic denominator, z=k^2(k+2)/(9D^2), and final eta match R1's frozen proof exactly. N0=2^160 implies L=lnN>100. The inequalities z<=5/18, rho<=64N^(-1/3)<=N^(-1/6), K>=L/lnL and log16+L<=L^2/(15lnL) establish eta=exp(-L^2/(10lnL)). No source normalization or factor of two drift was found.

**INT-M3, newly stated effective per-a threshold.** The synthesis adds the valid effective threshold L>=max(160 ln 2,100 a^2). For L>=100, lnL<=sqrt(L); hence L/(10lnL)>=sqrt(L)/10>=a, and eta<=exp(-aL)=N^(-a). This proof works for every real a>0, including a<1. It does not alter the algorithm or runtime exponent.

**INT-M4, marking and conditioning.** Label choice, position interleaving, connected word count, complementary count and Z(N,2k) denominator remain explicit. Fresh matching insertion uses two distinct powers 2^q (unoriented matching edges and normalized pair weights) and q! for unordered pairs. Reverse multiplicity is at most binom(k,q), with fixed removed labels only reducing it. Zero residual branches and q=0 are handled. The H0 omitted intersection v>K AND g>=2 is bounded by the stronger all-large-support event; no old genus<=1-only obstruction was substituted.

**INT-M5, source dependencies.** DYZ Eq 13, Eqs 19-20 and genus-zero coefficient after Eq 28 are correctly normalized to ordered literal words on fixed labels. No giant-component or fixed-genus asymptotic theorem has been imported. H0 additionally names the checked September 7 exact genus-zero/one decoder and its Vakil source. H1 relies only on the positive count theorem and elementary marked DP. Its implementation imports the historical g01 module for elementary random-choice/unranking utilities, but its mathematical argument and production H1 path do not call the nontrivial g0/1 count/sample formulas. This is consistent with R3 source and the R4 stubbed-primitive tests.

## Decoder, assembly, resources and boundaries — accepted

**INT-C1, sampler connection.** The source's `marked_step` swaps entries of the current permutation, so it is right multiplication in the stated convention. The partition join retains exposed support history. The base case demands both identity and connected support, and the only connectivity pruning is necessary. The explicit stack decreases remaining length at every dependency; cached duplicate children preserve multiplicity because the final sum scans all literal edges. Conditional transition counts telescope. Least-label assembly chooses exact branch weights, label subsets and position subsets, and preserves internal order. K is retained as object state, not recomputed on residual inputs. These facts agree with the mathematical Sections 7-8 synthesis.

**INT-C2, P^20/P^10.** With P=N+m+2, the source uses no hidden variable-genus large-support decoder. For marked counters, Q<=(m+1)K P^4<=P^6, B,D=O(P^2), K<=P. Charging linear dictionary search gives Q K^2(QD+KlogK+B)=O(P^16). The specified additional P^2 bookkeeping charge remains O(P^18), beneath P^20. Memo storage is O(Q(B+D))=O(P^8); stack, count tables, and historical primitive storage fit the looser P^10 envelope. Count arithmetic, cutoff powers, binomial arithmetic and random bits are explicitly paid for. H0's component primitive sum is O(N^10 log^3(N+1))<=O(P^13). These exponents are conservative mathematical bounds, not practical performance promises.

**INT-C3, boundary cases.** For N>=2, K>=2 and repeated-edge words give nonempty allowed sets at every even length. Empty words, uniform repeated edge at m=2, singleton bridge at N=2, N=1 only at m=0, odd sign obstruction, and arbitrary small-support high genus agree with the code. Code also accepts N0,m=0 as an extra harmless boundary outside the theorem; negative or empty fibers are rejected. The theorem is in degree N and length m, not log N wires.

**INT-C4, frozen wrapper and checks.** Root wrapper's expected digest equals current sampler-v3 bytes and is checked before runpy executes them. It forwards CLI arguments to the frozen file without sampling changes. The historical dependencies are hash-checked before execution. Existing root actual-forward complete-law tests and R4 production-path tests address the sampler law; no unnecessary exhaustive rerun was performed in this audit.

## Required correction — INT-L1

Canonical proof defines A for H0 and B for H1. In the reviewed v3 CLI, the `target` JSON string is hard-coded to `Unif(A(N,m)); exact restriction with one fixed top-level cutoff` for both policies. Actual root-wrapper outputs at N=4,m=6 show:

| policy | candidate | allowed count | global TV | reported target |
|---|---|---:|---:|---|
| H0 | H0-v1 |3936|0|Unif(A(N,m))|
| H1 | H1-v1 |1056|30/41|Unif(A(N,m))|

The counts and candidate IDs are correct, but the target string conflicts with the canonical A/B notation and is not self-contained for diagnostic cutoff overrides. Raw exact output and commands are preserved in `integration_cli_results.json`. This was the sole new test, justified by the newly introduced wrapper/canonical notation integration concern.

Required resolution: describe the actual selected policy by a literal component eligibility predicate in output, including its actual fixed cutoff, and provide or clearly document a generic `allowed_count` name if retaining the legacy `Z_A` field. Preserve v3 and this objection. A metadata-only v4 repair can be rechecked by byte/AST diff and targeted CLI output; the exact sampling-law tests need no repetition if mathematical and choice code remains unchanged. The coordinator agreed and assigned the repair to R3. Final CLI delivery acceptance is reopened until the exact repaired bytes are reviewed.

No other required correction was found. The complete global goal remains subject to the coordinator's ledger and R5 current-version audit; this report does not substitute for those gates.
