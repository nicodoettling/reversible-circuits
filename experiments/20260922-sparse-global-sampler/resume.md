# Self-contained handoff — sparse global sampler

Saved 2026-09-22T06:16:37.667273+00:00. Coordinator session: `01a0c7a4-3ed2-7372-914a-19f0ed2228c6`. One native goal was created without a token budget. The mathematical objective and current-version audits are complete. The native goal was marked complete at2026-09-22 06:18:04 UTC; exact tool fields are saved in `completion_record.json`:1,080,909 reported tokens and2,044seconds (34minutes4seconds), with no token budget. No automatic resume, cap reset, extra session or extension is authorized.

## Accepted theorem

The unchanged T0 asks for a global sampler for every even m with m^5<=N^3, one uniform polynomial expected bit-time bound, and a single negligible error function. Canonical `proof.md`, SG-T1.v1, proves the stronger range m^3<=N^2. Both H0 and separately labeled H1 preserve identity and length exactly, with expected O((N+m+2)^20) bit time and O((N+m+2)^10) bit storage. Their global TV error is at most

```
eta(N)=1                                      for N<2^160,
eta(N)=exp(-(ln N)^2/[10 ln ln N])             for N>=2^160.
```

For every fixed a>0 this is eventually <=N^(-a), uniformly over all lengths in the theorem. Neither the algorithm nor its polynomial exponent depends on a. The exact per-instance error is 1-Z_allowed/Z. The published DYZ count theorem and, for H0 only, the specified September7 g0/1 decoder/Vakil formulas are checked dependencies. No unproved mathematical step remains for T0/T1. This is internally audited mathematics, not external human certification or a claim of literature priority.

H0 remains the requested default: every component has g<=1 or size v<=K. H1 allows only components with v<=K and uses the elementary support-marked decoder throughout. The integer K=max{v: v^(2v)<=(N+m+2)^4} is computed once at the original input and retained in every residual problem. Small components of arbitrary genus are included. Empty words, m2 and N2 have exact handling; N1 allows only m0, and odd lengths have empty targets. No all-length negligible-error or wire-efficient theorem is claimed.

## Exact accepted versions

- Canonical proof: `proof.md`, SHA256 `f788eaecebefd53373c56a7c0c41d104c34897c4a6aba6c775f5f1ce80ec8da2`.
- Root executable wrapper: `sample.py`, SHA256 `2d74da262e4c53005a05d4f171b85c5469ade520e38b91b1b0df14f4cbe8386e`.
- Final implementation: `roles/r3-sampler/sampler-v4.py`, SHA256 `cdb91799b02539190bc31ce7d6fe31ee5af0477b1cc653f43452eb18de734002`.
- Mathematical sampler/resource proof: `roles/r3-sampler/proof-v3.md`, SHA256 `f941c5e141e229839813056da1169295b7b2c5d5a052886bc8edb69f096c1868`.
- Analytic proof: `roles/r1-combinatorial/proof_v1.md`, SHA256 `43fc4b84c5166ffd42cf838b3080e82c62b35b20f6a9ef2cde01da5c33dcaca0`, accepted by R2 and R5.
- Blind report: `roles/r5-referee/blind_report.md`, frozen at05:55:11 UTC with SHA256 `22f49d8084f9e94e564cae6c6912d74788ebb70b766914ff13877ee36a9bce64`.

R4's `sampler_review-v3.md` and R5's `report.md` accept the exact laws and conservative complexity. R1's canonical integration and v4 recheck close the last labeling issue. Complete input copies, hashes and objections are preserved. R1 authored the analytic subsection and labels its final synthesis review accordingly; independent analytic audits remain R2/R5. Same-model agreement is correlated.

## Reproduction and retained regressions

From repository root:

```
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 82 --m 14 --certificate-only
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 4 --m 6
python3 -B experiments/20260922-sparse-global-sampler/sample.py --n 4 --m 6 --policy H1
```

APIs are `sample_h0`, `sample_h1` and `PreparedSampler` in the final implementation. CLI labels are1-based; Python labels are0-based. A supplied seed is diagnostic only. The mathematical randomness model uses independent fair bits; the default implementation uses SystemRandom.

Root's actual forward production-law enumeration passes all140160 S4,m8 words, each probability1/140160, plus required small, high-genus and forced-exclusion cases. R4's independent counts/certificates and R2's literal weighted-incidence checks pass. Full tested domains and commands are in the reports. Finite counts validate/falsify implementations; the uniform tail is proved separately.

Two delivery defects were preserved and repaired: v1/v2 decimal integer serialization could fail on a valid T0 input due to Python's digit cap (v3 uses exact hex fallback); v3 target text ambiguously reused A for both policies (v4 states literal predicates and cutoff provenance). Both repairs passed fresh nonauthor checks. The v4 non-main sampling AST is identical to v3, so its focused metadata review does not inherit an unexamined law change. All historical mathematical counterexamples remain in `regression_registry.md`.

## Next actions and authority

No research action remains for the achieved T0/T1 goal after final delivery/accounting. Read `coordinator_report.md`, `claim_ledger.md`, and `artifact_manifest.json` for final status and provenance. Further length regimes or external human review require a new user task; do not auto-resume an old local-mixing program.

On any continuation, immediately reread `tmux-run.json` in this experiment and `notes/sparse-global-sampler-run.log.sparse-global-sampler-20260922.cap-status.json`. The original authoritative times are activation2026-09-22T05:43:44.791045Z; wrapup09:13:44.791045Z; saved handoff09:38:44Z; graceful shutdown09:42:39.791045Z; hard deadline09:43:44.791045Z. They were never changed. Early completion is authorized only because the full mathematical objective and audits closed, not because workers finished reports.

All six requested contexts actually started with explicit gpt-6-astra/ultra fresh-context requests. Separate backend model/effort identity is not exposed. Worker task IDs: `/root/r1_combinatorial`, `/root/r2_analytic`, `/root/r3_sampler`, `/root/r4_diagnostics`, `/root/r5_referee`. Workers never delegated or created goals. No extra Codex session/service, installation, commit, push, protected-file edit or detached computation occurred.

All research writes are inside the owned experiment. `changed_files.txt` inventories every attributable file; launcher-owned tmux metadata, all notes and pre-existing September7 work are excluded. The old source hashes remain unchanged and git's tracked diff is empty. Commit: `20e86f665f69053031fe7eec0c3388458affb1fc`; Python3.12.3, standard library only.
