# R3 exact diagnostics report

**Verdict: promote the exact finite certificates and regression results.** The R3 nonauthor audit accepts R2-O1's internal obstruction argument under its explicit imported uniform genus-majorant dependency. The coordinator owns final mathematical certification. This is same-model internal review, not external human certification.

## Target and scope

The target is the global uniform law U_(N,m) on distinguished-label, distinguished-position transposition identity words. Composition is (alpha beta)(x)=alpha(beta(x)), rightmost first. H0 is exactly uniform on A, where every component satisfies g<=1 OR v<=K. H1 is exactly uniform on B, where every component has v<=K. The integer K=max{v<=N:v^(2v)<=(N+m+2)^4} remains fixed at the original input. Both include arbitrary genus on small supports. Their exact global errors are 1-Z_A/Z and 1-Z_B/Z. No Markov kernel is involved.

T0 (existence of some sampler), P0 (unchanged H0) and P1 (unchanged H1) are distinct. Finite mass ratios do not establish or refute asymptotic negligibility. If the reviewed R2-O1 dependency graph is accepted, it refutes P0 and P1 by an asymptotic count comparison; it does not refute T0 or prove hardness.

## Exact finite conclusions

| Claim | Status | Evidence and limitation |
|---|---|---|
| Total/connected/active counts agree with independent small permutation and support DPs | proved finite fact | 91 count cells and 23 weighted-support/cutoff cases in pilot-results.json |
| First H0 omission in all benchmark pairs with N<=128 is (28,12,K4) | proved finite fact | 1,463 pairs in first-omission-classification.json; criterion K<N and m>=2K+4 |
| Required frozen H1 output laws and fixed-K branches are correct | proved finite fact | sampler-regression-results.json; complete actual forward laws, not frequency estimates |
| R1 falling-factorial finite-genus inequalities survive selected tests | proved finite fact | 53,300 component terms, 7,300 size sums and 7,300 exact binomial identities |
| R2 relaxed component exponent survives selected tests | proved finite fact | 150 cases, m<=64 and N through 10^6; allowed-exponent-results-v2.json |
| R2-O1 obstruction internal proof | conditional accepted audit | r2-obstruction-audit-v1.md; explicit imported majorant/source and sampler-law dependencies; root certifies final claim |

The elementary omission criterion follows directly: an excluded component needs v>=K+1 and g>=2, hence length at least 2K+4. Conversely, if K<N and even m>=2K+4, a connected identity word of length m on K+1 labels exists and is excluded, with all other labels isolated. The finite scan uses exact integer m_*(N).

At (N,m,K)=(28,12,4),

    H0 error = 18339750000 / 714036684356251,
    H1 error = 190337199624000 / 714036684356251.

These are approximately 0.0000256846 and 0.266565. The only excluded H0 component type is (v,ell,g)=(5,12,2). At (256,64,6), H0 error is approximately 0.0000130806, versus H1 error 0.203676. Its leading excluded H0 marks have genus two on support sizes seven through twelve. Exact counts and all omitted component marks are in boundary-results.json. The finite gap between the two policies must not be replaced by a genus<=1-only policy or extrapolated into an asymptotic conclusion.

| candidate | claimed target | identity ok | global support coverage | exact diagnostics | verdict |
|---|---|---|---|---|---|
| unchanged H0 | Unif(A) | imported exact law; boundary outputs and forced path pass | excludes v>K AND g>=2 | exact counts, marked moments, fixed original K | keep finite evidence; R2 obstruction separately audited |
| unchanged H1 | Unif(B) | complete small forward laws pass | excludes v>K | required cases, high genus, deliberate exclusion | keep finite evidence; subset implication separate |

## Falsification and versioning

R1's tested claim is

    E X_(v,g) <= binom(N,v) v^(v-3) b_v^g/g!
                 * (4/D²)^(v-1+g) (k)_(v-1+g),

with m=2k<=N, D=N-m+1 and b_v=(v³-v)/36. Its feasible genus sum equals the stated finite binomial expression. All 53,300 component cells and 7,300 sums/identities passed for N=2,...,48 and N in {64,82,100,128,181,256,512,1000}, even m<=min(N,48), and all feasible component types. These are falsification checks, not an asymptotic proof.

R2 diagnostics v1 used binom(N,v) for the component exponent. Root correctly identified that R2-O1's relaxed exponent uses N^v/v!. This scope mismatch is retained in allowed_exponent_checks-v1.py and allowed-exponent-results.json. Repaired v2 computes both and checks the larger relaxed exponent. In 150 eligible cases it satisfies S_relaxed<=8k and even the 20-term Taylor LOWER bound for the stronger proposed RHS. Thus no floating exponential decides a comparison. The maximum tested S_relaxed/(8k) was about 0.03548 at (36,12). Component costs are truncated at k; greater costs cannot affect the coefficient of x^k, so these checks address the coefficient-relevant inequality without computational evaluation of an infinite series.

The actual frozen v4 sampler passes complete H1 forward laws on S3,m4; S4,m4; S4,m6; S3,m8; and deliberately smaller cutoff K2 at S3,m8. The laws have respectively 27,120,1056,2187,3 words. S4,m6 has full total 3936 and exact H1 error 30/41; forced K2 at S3,m8 has error 728/729. Both H0 and H1 preserve top-level (42,12,K5) through 37 isolates to residual (5,12), where recomputing K4 would incorrectly delete a genus-two branch. Length 1400 on N2 (genus 699) passes explicit-stack execution. N1,m0; N2,m0,m2,m12; odd and empty targets; support history at zero remaining length; and 5001-digit exact hexadecimal serialization all pass. Seeds 1729,2718,31415 are used only for boundary validity smoke draws. No stochastic distribution claim is made.

A harness-only call to a nonexistent method was repaired to the inspected count API and rerun; the correction and a genus-label typo are preserved in harness_repairs.md. No source or sampler bug was discovered, and no read-only input was edited.

## R2-O1 proof audit

The reviewed file hash is a6716e623768ded49b5ba1a2441abdddc8cb18c61be52d8a96b79387fe68b33f. Its exact bytes are preserved in audit-input-r2-v1.md. The review independently reconstructed labeled component-profile coefficients, the replacement (N)_s<=N^s, the all-genus small-support term, the S0/S1 factors, the parity-supported midpoint return lower bound, the cutoff bound and every subsequence constant. No internal gap was found.

The audited conclusion is that for integers j>=64, N=2^(8j), m=2^(6j), unchanged H0 has Z_A/Z<=2^(-1-jm/2). These parameters satisfy m^4=N^3 exactly and m=m_*(N). Hence the audited count proof, once its explicit dependencies are certified, makes H0 error tend to one. H1 follows by B subset A. Boundary cases m0,m2,N2 and odd/empty fibers do not contradict it. No sequential marginal-product bound appears; cached-prefix CP1 is therefore not invoked.

## Reproduction, provenance and ownership

Run from repository root:

```text
timeout 90s python3 -B experiments/20260922-sparse-boundary/roles/r3-diagnostics/boundary_diagnostics.py --m-max 16 --checks --output experiments/20260922-sparse-boundary/roles/r3-diagnostics/pilot-results.json
timeout 90s python3 -B experiments/20260922-sparse-boundary/roles/r3-diagnostics/boundary_diagnostics.py --m-max 64 --output experiments/20260922-sparse-boundary/roles/r3-diagnostics/boundary-results.json
timeout 90s python3 -B experiments/20260922-sparse-boundary/roles/r3-diagnostics/finite_inequality_checks.py --m-max 48 --output experiments/20260922-sparse-boundary/roles/r3-diagnostics/finite-inequality-results.json
timeout 90s python3 -B experiments/20260922-sparse-boundary/roles/r3-diagnostics/allowed_exponent_checks.py --m-max 64 --output experiments/20260922-sparse-boundary/roles/r3-diagnostics/allowed-exponent-results-v2.json
timeout 90s python3 -B experiments/20260922-sparse-boundary/roles/r3-diagnostics/sampler_regressions.py
```

Each raw JSON records its exact arguments, parameters, rational results, timing and source hashes. Pilot, boundary, R1, R2-v2 and sampler runs took approximately 0.024,0.184,0.797,0.186 and 0.581 seconds. Every supervised computation finished without an outstanding session. Commit: 20e86f665f69053031fe7eec0c3388458affb1fc. Python 3.12.3; standard library only; python3 -B throughout executable research. The unavailable `python` alias was immediately replaced by `python3`, without installation.

All 35 initial inputs were hashed before research-code import and checked again in final-source-integrity.json. The requested worker identity is /root/r3_diagnostics, gpt-6-astra / ultra; the backend does not independently expose model/effort verification. Full assignment, frozen run brief, authoritative cap paths and immutable timing are preserved in assignment.md. GOAL_SPEC/HANDOFF concern the older local-chain objective; the user-approved frozen global-sampling task supersedes that objective, while its proof/safety standards remain.

All writes belong to this role directory. No delegation, native goals, installs, new sessions/services, machine/configuration changes, permission requests, commits or pushes occurred. Source input files and other roles are untouched. changed_files.txt inventories all role artifacts; git_status_final.txt records the repository status seen at this report boundary. The expensive compute slot was released to root at 09:36 UTC.

No role task remains except any targeted follow-up on a changed candidate version. A changed proof hash reopens the associated audit.
