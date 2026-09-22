# Referee final report

Verdict: **promote the checked obstruction and smaller positive theorem; reject both original full-range truncation claims.** This is same-model internal review, not external human certification.

## Outcome

The frozen blind analysis independently proves that at m=m_*(N), both TV errors tend to one: |A|/|Omega| <= N^(-m/16) for log N>=1024, with B subset A. It uses checked Vakil genus-zero/one counts, a component-assembly upper bound, and Cauchy--Schwarz on a fixed moderate support. The blind report was frozen at 09:34:39 UTC before any candidate proof or coordinator outcome was read; SHA256 76a35688d44c08b39c221778efa1b7a395d7b4bc9e9cc608a68c31b1e3fce22d.

The later nonauthor audit independently reconstructed the DYZ all-genus bound and fresh-pair normalizer comparison. It accepts canonical SB-O1.v1 (obstruction hash bf7b3bed9f0616816e92bfc0c37527c8617abef8c525d15940d9c21b7aa40894) and canonical SB-T1.v1 integration v2 (positive-proof hash 3a54f12e4d172cfdfc5ef6f8e7b84c067e86eba8d10a2f387496ff7bd435d611). Complete exact-version disposition and limitations are in integration_audit_v2.md.

The obstruction gives |A|/|Omega| <=2^(-1-jm/2) at N=2^(8j),m=2^(6j),j>=64, so both original error claims fail. The smaller positive theorem gives the unchanged exact H0/H1 laws a common negligible error exp[-(ln N)^2/(48lnln N)] for N>=2^2048 and even m<=N^(2/3)ln N/4, with expected O((N+m+2)^20) bit time. R4's separately reviewed decoder/resource dependencies are explicit; H1 avoids H0's historical genus-zero/one decoder. Another polynomial sampler throughout m^4<=N^3 remains unresolved.

## Checks and retained issues

finite_checks.py checks the genus-zero/one normalization by exact product/support DP through v=5,ell=10. candidate_checks.py independently checks 370 normalizer ratios, 190 finite-genus sums, 10 genus-majorant cells and 31 normalized-series coefficients. Both pass using Python 3.12.3 and only the standard library, under supervised timeout 90s. Commands, commit and raw counts are in the corresponding JSON files. No stochastic inference or single-seed result is used.

Three textual issues were reported and repaired in the canonical integration: explicit S normalization, integer auxiliary cutoff J, and H0's literal routing of every genus<=1 component to the imported decoder even when v<=K. The prior snapshots and the audit history preserve these issues. No mathematical or exact-version integration obligation remains in this referee's assigned scope.

No sampler logic, shared project file, manuscript, old proof, or another worker directory was edited. No new session, delegation, goal, install, configuration change, commit or push occurred. Unavoidable inherited AGENTS/model framing is recorded in initial_input.md; post-freeze source/context access is recorded separately.

## Sampler distinction

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| H0 | Unif(A) exactly; approximate U only in smaller proved range | proved by unchanged decoder/assembly | global assembly includes allowed macro components | current law/resource audit plus prior complete-word checks | promote smaller-range theorem; reject full benchmark |
| H1 | Unif(B) exactly; approximate U only in smaller proved range | proved by marked DP/assembly | global assembly includes allowed macro components | current law/resource audit plus prior complete-word checks | promote smaller-range theorem; reject full benchmark |

The obstruction is not a mixing or hardness theorem, and all resource claims use N,m rather than log N wires.

## Artifacts written in this role directory

- `blind_phase_artifacts.json`
- `blind_report.draft.md`
- `blind_report.md`
- `blind_report.sha256`
- `candidate_audit_v1.md`
- `candidate_checks.json`
- `candidate_checks.py`
- `checkpoint_0927.md`
- `checkpoint_0934.md`
- `checkpoint_0943.md`
- `entry_cap_status.json`
- `entry_tmux_run.json`
- `finite_checks.json`
- `finite_checks.py`
- `freeze.json`
- `initial_brief.md`
- `initial_brief.sha256`
- `initial_input.md`
- `integration_audit_v2.md`
- `integration_inputs_v1.json`
- `integration_inputs_v2.json`
- `integration_verification.json`
- `plan.md`
- `postfreeze_reading.md`
- `report.md`
- `review_inputs/canonical-obstruction-v1.md`
- `review_inputs/canonical-proof-v1.md`
- `review_inputs/canonical-proof-v2.md`
- `review_inputs/canonical-source-checks-v1.md`
- `review_inputs/coordinator-source-checks-v1.md`
- `review_inputs/r1-proof-freeze.json`
- `review_inputs/r1-proof-read-0937.md`
- `review_inputs/r1-proof-v2.md`
- `review_inputs/r2-obstruction-v1.md`
- `review_inputs/r4-algorithm-audit-input-hashes.json`
- `review_inputs/r4-algorithm-audit-v1.md`
- `review_inputs_0937.json`
- `review_inputs_v2.json`
- `source_checks.md`
