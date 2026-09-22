# R1 independent phase report

Frozen 2026-09-22T05:56:11.471631+00:00. Author verdict: **promote for nonauthor audit**, mathematical status proved by author / provisional audit status. H0 and T0 remain exactly as frozen by the user.

## Strongest result

`proof_v1.md` proves a tail bound for **any** support component larger than the fixed top-level K, which dominates H0's omitted event v>K AND g>=2. It supplies eta(N)=1 for N<2^160 and exp(-log(N)^2/(10 loglog(N))) for N>=2^160, uniformly over T0's even lengths m^5<=N^3. Separately versioned T1 extends the same bound and same H0 algorithm to m^3<=N^2. The claim concerns polynomial time in permutation degree N and word length m, not log(N) wires.

The new author derivation is the factorial genus bound A_g(v)<=v^(v-3)((v^3-v)/36)^g/g!, followed by a labeled fresh-pair extension argument paying the identity-conditioning denominator exactly. The imported result is the DYZ positive recurrence and its normalized genus-zero coefficient. A complete independently checked H0 sampler remains the coordinator/R3 dependency; this role does not certify their implementation.

## Evidence

- Frozen proof hash: 43fc4b84c5166ffd42cf838b3080e82c62b35b20f6a9ef2cde01da5c33dcaca0. Actual filesystem freeze time05:52:41.907381352 UTC; the internal manually estimated timestamp is corrected in freeze_manifest.md without changing the proof.
- `verify_v1.py` and `results_v1.json`: all assertions passed in 0.505s, Python3.12.3 standard library, deterministic exact arithmetic. No prior experiment code imported.
- 52 independent endpoint/support DP count cells, N1..4,m0..12.
- 78 rational majorant cells through v13,ell24 and101 elementary series coefficients.
- 7983 exact residual/normalizer inequalities; 1210 marked bound cells; 485 union bounds, across N2..20 and even m<=N.
- Literal enumeration at (3,4),(4,4),(4,6),(3,6),(3,8) verifies marked multiplicities independently of the DYZ recurrence.
- True H0 at (128,16), inside T0, has nonzero omitted mass; the exact fraction is recorded. Size2 and size3 arbitrarily higher-genus cases remain included. Deliberately smaller cutoff2 tests are labeled separately.

No randomized inference is used. These checks can refute errors but do not establish the asymptotic theorem; the uniform proof is in the frozen artifact. No failed mathematical claim or finite counterexample was found. Historical minimal-only and g<=1-only dense obstructions do not concern the all-small-support subset used by the tail proof.

## Exact normalization and first remaining obligation

E X_(v,q)=binom(N,v)binom(2k,2q)C(v,2q)Z(N-v,2k-2q)/Z(N,2k). The normalized macro ratio is bounded using q added unordered disjoint pair components, with matching factor (I)_(2q)/(2^q q!), component weight2^(-q), and reverse multiplicity at most binom(k,q). This handles endpoint conditioning without a random-graph independence assumption.

No missing mathematical lemma is identified by the author in the tail derivation. First remaining certification obligations are a nonauthor audit of the exact current proof and independent verification of H0's sampler primitives/runtime. Every repair will create a new version and reopen downstream claims.

## Operations

All writes are within this role directory. No heavy grid, installation, delegation, goal creation, external process/session, commit or push was performed. Actual model name/effort are requested gpt-6-astra/ultra; separately exposed exact runtime settings were unavailable and not inferred. New check/source metadata are preserved in settings.json and the input copies.

Role attribution inventory at independent freeze: assignment.md, checkpoint.md, freeze_manifest.md, independent_report.md, intake_user_prompt.md, plan.md, proof_v1.md, results_v1.json, settings.json, verify_v1.py, worker_common.md. Further audit artifacts will be added explicitly.
