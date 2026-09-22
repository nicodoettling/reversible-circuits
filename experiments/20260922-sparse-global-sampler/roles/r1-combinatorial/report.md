# R1 final role report — 2026-09-22T06:00:52.903722+00:00

**Verdict: promote the quantitative tail theorem to coordinator audit.** The independent derivation and full mathematical argument are frozen in `proof_v1.md`; `independent_report.md` preserves the independent-phase result. Mathematical status is author-proved with exact finite tests, awaiting the coordinator's current-version integration verdict. A separate nonauthor audit accepts R2-A.v1's mathematical tail derivation; its complete inputs, report, and fresh checks are preserved here.

The proved-by-author statement is: for every N>=2 and every feasible even m with m^3<=N^2, the H0 omitted mass is at most eta(N), where eta(N)=1 below 2^160 and eta(N)=exp(-log(N)^2/(10 loglog(N))) above that threshold. This stronger separately versioned T1 implies the unchanged user benchmark T0, m^5<=N^3. The same eta is uniform over m, negligible in N, and uses the same fixed top-level work cutoff. This is a global-law tail theorem, not local-chain mixing or computational hardness.

The exact normalized quantity is E X_(v,q)=binom(N,v)binom(2k,2q)C(v,2q)Z(N-v,2k-2q)/Z(N,2k). The new factorial majorant A_g(v)<=v^(v-3)((v^3-v)/36)^g/g! and a weighted matching insertion inequality bound the stronger event of any component with v>K. They therefore apply to H0, whose excluded components require both v>K and g>=2. Arbitrarily high genus at small support remains included.

## Deliverables and evidence

- `proof_v1.md`: complete normalized law, source translation, majorant, incidence ratio, finite tail, explicit constants, boundary treatment, and dependency list.
- `freeze_manifest.md`: immutable proof hash and correction of its manually estimated internal timestamp. Actual artifact freeze is 05:52:41.907381352 UTC, SHA256 43fc4b84c5166ffd42cf838b3080e82c62b35b20f6a9ef2cde01da5c33dcaca0.
- `verify_v1.py`, `results_v1.json`: independent support-state counts, rational inequalities, direct marked-word enumeration, high-genus small supports, and nonzero actual H0 omission inside T0. All assertions passed.
- `r2_audit.md`, `r2_audit_inputs/`, `audit_r2_check.py`, `r2_audit_results.json`: complete nonauthor audit of R2 proof SHA256 518a5392f305aa7a7838a52ef8c28a2cacbb2e6bb52d285be7f0a8c01aa7a8d3. ACCEPT, no mathematical repair. Bibliographic locator and algorithm-certification scope notes retained.
- `assignment.md`, `intake_user_prompt.md`, `worker_common.md`, `settings.json`, `plan.md`, `checkpoint.md`, `independent_report.md`, `resume.md`: complete role provenance, plan, progress and resumption state.

Imported result: DYZ Proposition 1 Eq 13, Eqs 19-20 normalization, genus-zero value after Eq 28. New derivation: factorial genus majorant, labeled incidence conditioning bound, and quantitative maximum-support tail. Implementation: only compact exact proof-checking scripts in this role; H0 implementation belongs to R3. Exact finite certificates: raw JSON, including nonzero omitted mass at (N,m)=(128,16). Empirical observations: none; all tests are deterministic exact arithmetic, with decimal boundary regressions explicitly secondary to symbolic proof.

## Limits and unresolved certification

No first missing mathematical lemma was found in the tail route. Global algorithm certification still requires the coordinator's synthesis, exact sampler primitive/runtime audit, and designated referee process. Same-model agreement is correlated internal evidence, not human certification. No sharpness or impossibility claim above exponent 2/3 follows. Source publication novelty was not surveyed or asserted.

All writes are confined to this role. All computations were supervised standard-library Python 3 -B with timeout 120s, took less than one second per script, and did not occupy a heavy enumeration grid. No old script was imported; no install, delegation, goal creation, machine change, commit or push occurred. Exact runtime model/effort were not separately exposed; requested gpt-6-astra/ultra are recorded without invented observed values. Historical September 7 user files and launcher sidecars remain unmodified by this worker.

`changed_files.txt` lists every attributable role file. `git_status.txt` preserves the final repository status, which includes unrelated pre-existing untracked September 7 and launcher artifacts; those are excluded from this role's attribution.

## Authorized final integration follow-up — 2026-09-22T06:16:07.761457+00:00

Completed the coordinator's concrete final integration audit. `integration_audit_v1.md` preserved one required CLI labeling repair (INT-L1), and `integration_audit_v4.md` freshly accepts the corrected exact version and closes it. Current canonical proof hash is f788eaecebefd53373c56a7c0c41d104c34897c4a6aba6c775f5f1ce80ec8da2; wrapper hash is 2d74da262e4c53005a05d4f171b85c5469ade520e38b91b1b0df14f4cbe8386e; sampler-v4 hash is cdb91799b02539190bc31ce7d6fe31ee5af0477b1cc653f43452eb18de734002. All mathematical/choice code is unchanged from reviewed v3, and the proof changed only its executable reference. Fresh root CLI metadata checks pass. No further required correction remains from this role. Analytic authorship is disclosed; this is not a blind independent analytic review.
