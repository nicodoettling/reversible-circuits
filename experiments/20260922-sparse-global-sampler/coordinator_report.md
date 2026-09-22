# Coordinator report — sparse global sampling

Classification: **global-negligible-sampler**. The unchanged T0 objective and the stronger T1 theorem are proved and accepted by the closed mathematical, implementation and canonical-integration audits. The full argument is `proof.md` (SG-T1.v1). Native completion accounting is recorded separately in `completion_record.json`; no token budget was imposed.

## Exact theorem and scope

For every N>=2 and every even m with m³<=N², the fixed H0 algorithm outputs a length-m identity transposition word in expected O((N+m+2)^20) bit time, with O((N+m+2)^10) bit storage and

```
TV(Q,U_(N,m)) <= eta(N),
eta(N)=1 for N<2^160,
eta(N)=exp(-(ln N)^2/[10 ln ln N]) for N>=2^160.
```

This single explicit function is negligible in N, uniformly over the entire stated length range. It establishes unchanged T0, m⁵<=N³, and the stronger separately versioned T1, m³<=N². The same algorithm and polynomial exponents work for every inverse-power target; there is no accuracy parameter. The threshold is deliberately conservative. The exact finite certificate often gives a much sharper error.

Labels and positions are distinguished; products act rightmost first. The sampler is exactly uniform conditional on the declared allowed subset A, with exact global error 1-Z_A/Z. It preserves endpoint and length on every output. The top-level integer cutoff K is never recomputed in residual subproblems. H0 includes all genus0/1 components and all components of size<=K. A separately labeled H1, keeping only size<=K components, satisfies the same global bound and needs only the elementary support-marked connected decoder. H0 remains the default requested implementation.

m0, m2 and N2 have exact boundary samplers; N1 allows only m0, and odd m has an empty identity fiber. The implementation supports even lengths beyond T1 as a conditional sampler with an exact certificate, but no uniform negligible-error theorem is claimed there. Complexity is in N, not log2N wires. No mixing, sharp-threshold or hardness theorem is asserted.

## Mathematical result and dependencies

The new project-level argument combines a factorial genus majorant

```
C(v,2v-2+2g)/(2v-2+2g)! <= v^(v-3) ((v³-v)/36)^g/g!
```

with a weighted incidence comparison obtained by inserting fresh isolated pair components. The latter pays for the exact endpoint-conditioned bridge normalizer. Together they bound the stronger event that *any* support component has size>K, not merely H0's excluded intersection v>K and g>=2. Positivity, all label/interleaving factors and reverse multiplicities are explicit. No ordinary random-graph independence enters the proof.

Imported mathematical inputs are the exact DYZ positive count recurrence and genus-zero normalization, and, for H0 alone, the specified September7 exact genus0/1 decoder based on the checked Vakil fixed-endpoint formulas. Primary sources were reopened and their normalization checked in this run. H1 avoids the nontrivial genus0/1 sampler dependency. No unresolved primitive is hidden behind scalar counts. Literature priority beyond these named project inputs has not been established or claimed.

Two implementation delivery issues were repaired and freshly rechecked. Version3 fixes exact CLI serialization above Python's decimal-digit limit with a lossless hex fallback, without changing interpreter settings. Version4 makes the H0/H1 target predicates and original versus diagnostic cutoffs explicit in output; its sampling code is unchanged. Earlier code, both counterexamples and review snapshots remain preserved. Mathematical laws and API correctness were unaffected.

## Audit and evidence

All six requested contexts actually started: coordinator plus five fresh gpt-6-astra/ultra workers. No capacity mismatch was observed. Tool task identifiers and explicit spawn settings are recorded; the backend does not separately expose model/effort verification. Workers did not delegate or create goals. Same-model agreement is correlated internal evidence, not external human certification.

| Role | Contribution | Review disposition |
|---|---|---|
| R1 combinatorial | factorial majorant, marked incidence, explicit T0/T1 tail | accepted by R2 and R5; canonical synthesis checked |
| R2 analytic | independently derived sharper genus budget and same size-tail mechanism | accepted by R1; separately audited R1 reverse incidences |
| R3 sampler | exact H0/H1 API/CLI, iterative support DP, fixed cutoff, bit/storage proof | v3 law/resource proof accepted by R4/R5; v4 metadata repair accepted by R1 |
| R4 diagnostics | independent counts, marked moments, exact certificates, actual forward H1/cutoff tests | complete exact finite evidence and v3 restricted-law review |
| R5 referee | frozen blind distinct real-variable tail proof, then nonauthor theorem/code audit | blind report preserved; full current-version audit accepted |
| Coordinator | source checks, integration, actual forward H0 law, decisive reruns, claim ledger | canonical integration and v4 repair accepted |

R5 froze its blind report at05:55:11 UTC, before receiving candidate material, well before the90-minute deadline. It independently obtained an all-large-component bound through a different connected-series majorant. Its isolation excludes current proof attempts and prior verdicts; unavoidable repository-wide framing remains disclosed in the report. Complete initial and later inputs are preserved.

Exact finite evidence includes:

- All required small laws and all140160 words at S4,m8. Root exhaustively replayed the *actual production* choices in v1 and then final v3; every S4,m8 word has probability1/140160. High-genus S3,m8 and a deliberately excluded cutoff2 case are included.
- R4's992 genus-count and517616 marked-incidence inequalities, plus root's smaller decisive240/90168 rerun, all exact. These are falsification checks, not the asymptotic proof.
- R2's237 literal macro-incidence cells and8107 extensions check reverse multiplicity with the removed-label condition;45 nontrivial exact tail comparisons pass.
- Fixed-cutoff execution from top(42,12,K5), through37 isolates, to residual(5,12) retains the branch that recomputing K4 would wrongly exclude. Both H0/H1 actual probabilities match1/Z_A.
- Arbitrary-length small-support execution at length1200/1400 works with explicit stacks. Prefix permutation and support partition remain distinct state coordinates.
- Actual nonzero H0 omitted mass inside T0 at(82,14,K5) is7633925094110515200/255443972184307397709618401, approximately2.98849e-8. The stronger size-only omitted event there is approximately0.0094813; the two are explicitly distinguished.
- Complete per-word laws certify all listed deterministic diagnostics; seeded tests with1729,2718,31415 check validity only. No empirical mixing evidence is used.

Negative historical findings are retained in regression_registry.md, including old minimal-only and genus<=1-only obstructions, graph/square insertion bias, prefix support omissions, and the CLI failure. No mathematical repair to the frozen analytic argument was needed. The old obstructions are not recast as failures of H0.

## Reproduction and remaining scope

From repository root:

```
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 82 --m 14 --certificate-only
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 4 --m 6 --seed 1729
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 4 --m 6 --policy H1
```

Omit seed for the default SystemRandom implementation; mathematical exactness uses independent fair bits. The CLI always names its conditional target; the canonical theorem provides the global interpretation. Detailed APIs, large-integer encoding and all author tests are documented in roles/r3-sampler/README.md. Exact review inputs and hashes are in the role manifests; top-level provenance and attributable changes are inventoried separately.

The first remaining mathematical obligation for T0/T1 is **none**: the current-version proof graph is closed. Longer regimes and general all-genus large-support decoding remain outside this run's theorem, with no impossibility claim. The reviewed canonical proof hash is `f788eaecebefd53373c56a7c0c41d104c34897c4a6aba6c775f5f1ce80ec8da2`; the final sampler-v4 hash is `cdb91799b02539190bc31ce7d6fe31ee5af0477b1cc653f43452eb18de734002`. Complete frozen inputs and acceptance records are preserved. Final artifact consistency is checked against these versions.

The authoritative four-hour cap was never reset. Activation05:43:44Z; wrapup09:13:44Z; saved-handoff deadline09:38:44Z; hard deadline09:43:44Z. If final acceptance completes early, the objective may finish early as authorized. No installs, extra Codex sessions, services, commits, pushes, protected-file edits or automatic continuation are authorized or performed.

## Completed native goal and final delivery

The native goal was marked complete at2026-09-22 06:18:04 UTC, after all mathematical, code, repair and integration obligations closed. The tool reports1,080,909 tokens and2,044seconds (34minutes4seconds) of native goal time, with no token budget. Service activation was05:43:44.791045 UTC, so the entire run finished well before wrap-up. Exact tool fields are saved in completion_record.json. Final delivered files are inventoried in changed_files.txt and hashed in artifact_manifest.json; git_status_final.txt records every repository status entry. Existing September7 and external note/launcher changes are excluded from attribution. No further action or automatic resumption is pending.
