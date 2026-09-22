# R3 final author report — R3-S1.v3 / implementation v4

Saved 2026-09-22 06:02 UTC. Verdict: **keep; promote restricted-sampler infrastructure after current-version nonauthor review**. Mathematical status: **proved by author / provisional pending review**, explicitly conditional on the named imported count theorem and, for H0 only, the checked prior g0/1 primitive. This report does not establish global T0. No asymptotic tail estimate is inferred from the finite certificates.

## Deliverable

`sampler.py` implements the mandated H0 exactly, with one integer cutoff frozen from the original N,m. It combines the read-only SHA256-checked September7 g0/1 connected decoder, a new iterative arbitrary-length support-marked DP for higher genus v<=K, and exact least-label assembly. `sample_h0(N,m,rng=None)` returns the word and exact counts/TV. `PreparedSampler` reuses tables. CLI output always names the restricted target, candidate, cutoff, exact certificate and T0 range check.

At coordinator request the separate H1 policy keeps only isolates and v<=K components, and uses the marked DP for every connected draw. H0 remains the default. H1 invokes neither the imported g0/1 count formula nor its sampler; tests replace both by functions that fail if called. Shared elementary rejection and subset-unranking utilities remain imported from the same hash-frozen module. A diagnostic cutoff override always receives a separate candidate label.

Both implementations preserve exact identity and length on every output. Each is exactly uniform on its declared A, and `global_tv=1-Z_A/Z` is exact. Odd/empty fibers are rejected; N0/1,m0 gives empty; m0,m2,N2 and high genus are handled. No `m<=2N` restriction is retained. There is no Markov chain or mixing claim.

`proof-v3.md` supplies a disjoint word-level reconstruction, conditional-probability telescoping, all dependencies, edge cases and a bit/storage proof. With M=N+m+2 it gives conservative expected O(M^20) bit time and O(M^10) bit storage. In particular, the support-state cache is bounded by `sum_(v<=K)(m+1)v!Bell(v) <= (m+1)K M^4`; the length factor is not lost. Dictionary worst-case probes, pending stack siblings, count bit lengths, binary cutoff powers and imported primitive work are included.

## Frozen evidence

`review-v3-manifest.json` freezes the review inputs:

- sampler-v3.py: `56b27019396f93d4784032028ca1099d45ddd1cab1f740520c20c8c0169a8e06`
- audit-v3.py: `eeec5e9e9e6e470f8b9c21641ee0103341cac8c48bab805fbff52968673c15df`
- results-v3.json: `84213ab10f0e6955657059a8def62cdafca5705bdf1877c2280982d96d8d30ec`
- proof-v3.md: `f941c5e141e229839813056da1169295b7b2c5d5a052886bc8edb69f096c1868`

At the initial v3 freeze, sampler.py/audit.py/proof.md matched those snapshots. Current sampler.py has the CLI-only v4 metadata repair recorded below; its non-main function/class AST is unchanged from v3, and audit.py/proof.md remain unchanged. The complete audit-v3 ran in18.70s with Python3.12.3, standard library only, using an individual120s timeout. Source hashes, exact commands, commit and initial dirty state are preserved in provenance.json/results. Historical files were hashed before executing any of their code, read-only, and loaded without creating bytecode caches.

| law/case | total | allowed | exact global TV |
|---|---:|---:|---:|
| H0 (3,4) | 27 | 27 | 0 |
| H0 (4,4) | 120 | 120 | 0 |
| H0 (4,6) | 3936 | 3936 | 0 |
| H0 (3,6) | 243 | 243 | 0 |
| H0 (3,8), genus2 included | 2187 | 2187 | 0 |
| H0 (4,8) | 140160 | 140160 | 0 |
| diagnostic K2 (3,8) | 2187 | 3 | 728/729 |
| H1 (4,6), actual K3 | 3936 | 1056 | 30/41 |
| H1 (4,8), actual K3 | 140160 | 9120 | 273/292 |

All literal words in those cases were checked, including exact zero probability for excluded words. The primitive g0/1 law reconstruction uses the previously hashed exact audit; the global support decomposition and H0/H1 assembly factors are checked in the new audit. Prefix cycle types, position-edge values, edge multiplicities, adjacent repeats, weighted support data, and length3 window products are exact pushforwards of the validated literal-word laws. Labeled macro multiplicities independently equal `m! product C(v,ell)/ell!`.

Other checks: all75 marked-DP/count cells v1..5,ell0..14;4941 exact cutoff cells; equality4^8=16^4; fixed-cutoff top(42,12,K5) retaining residual(5,12) whose local cutoff would be4; actual v2 length1200 completion and sample with no recursion limit change;180 seeded validity draws across six cases using seeds1729,2718,31415; four H1 primitive-independence draws. Seeded draws are implementation checks, not the basis of uniformity.

An actual H0 nonzero omitted mass **inside T0** at(128,16,K5) is

```
3015538111971730865520000 / 398488912723604665601813065391959.
```

The result independently agrees with R4's newly authored count code; saved in crosscheck-n128-m16.json. This finite certificate is not a uniform asymptotic estimate.

Root reports an additional genuinely forward execution audit of the production random-choice path, including every140160 word at(4,8) and all three forcedK2(3,8) outputs. R4/R5 are auditing frozen v3 as nonauthors; their final acceptance is owned by their role artifacts and coordinator ledger. Same-model agreement remains correlated internal evidence.

## Retained defect and repair

Root and R5 independently identified a real CLI defect in v1/v2: Python's default4300-digit decimal conversion cap could reject exact count JSON even at a valid T0 input, e.g.N100000,m1000. The exact API and distribution were unaffected. Version3 emits ordinary decimal counts/rational strings when safely below the current cap and otherwise labeled lossless hexadecimal integers/rational parts. A20001-bit synthetic JSON roundtrip passes without changing interpreter settings. The old versions are preserved, and README documents the alternate encoding.

The initial audit-v1 imports a module named sampler. To replay it after current code changed, `replay-v1.py` explicitly preloads and hash-checks frozen sampler-v1.py before executing unchanged audit-v1.py. This preserves old review hashes and avoids accidentally reviewing new code under an old filename.

## Classification and next obligation

- Mathematical novelty: no new asymptotic global theorem claimed by this worker; the elementary support-marked and assembly arguments implement the frozen candidate with explicit resource accounting.
- Imported result: positive scalar connected counts; exact prior genus0/1 decoder for H0 only.
- Implementation: exact H0 and separate H1, fixed cutoff, iterative completion stacks, exact bit choices, reusable API/CLI and certificate.
- Exact finite certificate: all reported counts, full laws and rational omitted masses.
- Empirical observation: seeded validity checks only; no mixing or negligible-tail extrapolation.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| H0-v1 | Unif(A0) | proved/tests | not a chain; positive across allowed component data | complete required laws, high genus, nonzero test exclusion | keep pending v3 review |
| H1-v1 | Unif(A1) | proved/tests | not a chain; positive across its component data | full allowed/excluded laws and primitive-independence check | keep pending v3 review |

The first remaining global lemma is a single explicit negligible-in-N bound on `(Z-Z_A)/Z`, uniformly over every even m with m^5<=N^3. Root reports promising independent proofs but this role has not imported an unreviewed tail claim into its sampler theorem. If that bound is certified for H1, it also bounds H0 by subset inclusion. No failure of either candidate would establish general sampling hardness.

All author files lie under roles/r3-sampler/. No delegation, goal creation, install, permission escalation, external/detached session, commit or push occurred. The authoritative cap was read at entry; deadlines remain wrapup09:13:44Z, report/resume09:38:44Z and hard09:43:44Z. Worker is available for concrete review repairs.

## Current-version review update, 2026-09-22 06:04 UTC

R4 directly reports acceptance of frozen v3 code and proof, with fresh actual-forward H1 laws at(4,6), forcedK2(4,4),(4,6), and(3,8), forbidding g0/1 count/sampler calls; actual frozen-cutoff assembly paths under both policies; v2 length1400 stack execution; and ten independent total/allowed count comparisons including(82,14),(128,16). Its acceptance is the exact restricted-law theorem with explicit imported dependencies, not a standalone global T0 claim. The final report path will be owned and supplied by R4. Root is separately auditing current CLI serialization. Frozen proof/code inputs remain unchanged.

## Integration repair v4, 2026-09-22 06:11 UTC

R1 found that v3 CLI output used the generic name A(N,m) for both policies while the canonical root proof calls H0's setA and H1's setB. Although the candidate field distinguished policies and the law was correct, the target label was ambiguous. Implementationv4 now spells out the allowed nontrivial component predicate: `v<=cutoff or g in{0,1}` forH0 and `v<=cutoff` forH1, with the genus definition and explicit allowance for isolates. It separately reports `top_level_cutoff`, `diagnostic_cutoff_override`, and `cutoff_source`. The new `allowed_count` is policy-neutral; retained `Z_A` is a backward-compatible alias for the same restricted count, not a reference to root's named setA. Candidate versions H0-v1/H1-v1 are unchanged because their laws are unchanged.

`cli_audit_v4.py` passes four actual CLI cases spanning H0/H1 and original/overridden cutoffs, and confirms via AST that every non-main function/class is identical to frozen v3. Exhaustive laws were not redundantly rerun. Current source and focused test hashes are in review-v4-manifest.json; v3 sources/results remain preserved. Mathematical proof-v3.md is unchanged. R1 owns fresh review of the output-only repair.

R4's completed v3 review is roles/r4-diagnostics/sampler_review-v3.md, SHA256 d673444cc3a0273c44a775f69c176b8ac687b8806ef6db272c29a79686fe44b8. It accepts the exact H0/H1 restricted laws and stated polynomial accounting with the explicit imported dependencies, without certifying a standalone T0 mass theorem.
