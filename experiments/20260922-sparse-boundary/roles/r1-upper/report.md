# R1 upper-bound report

Verdict: **promote the smaller logarithmic extension after coordinator dependency closure**. Full benchmark T0 is not proved by this role. H0/H1 failure at the benchmark is accepted as a nonauthor audit of R2's separate obstruction, not as an implication of our upper bounds.

## Strongest proved positive result

For N>=2, unchanged H0 and H1 with the original fixed top-level cutoff K sample their exact declared allowed sets. For every even m<=N^(2/3)ln N/4, their global error is at most the single explicit function

eta(N)=1 for N<2^2048;
eta(N)=exp[-(ln N)^2/(48lnln N)] for N>=2^2048.

It is negligible: for fixed a>0, ln N>=max(2048ln2,(48a)^2) suffices for eta<=N^(-a). Their imported expected O((N+m+2)^20) bit-time and O((N+m+2)^10) storage bounds are unchanged. The algorithm and polynomial exponents do not depend on a. Complexity is in N,m, not log2N wires. The rightmost-first convention, labeled positions and support data are unchanged.

Proof: **proof-v2.md**, SHA256 `b76f706aad3dae20ed3550298b98bd260b295f7cc9752eb3f1ecef663c87ac3c`. The first line retains the initial candidate v1 heading; Section3 explicitly states UPPER.v2 and this exact file/hash is the reviewed mathematical artifact. No content edits occurred after freeze. Non-author R2 accepted it in `../r2-obstruction/r1-audit.md`; R3 checked the exact inequalities. All reviews are correlated internal same-model evidence.

The new mathematical step retains the finite constraint g<=k-v+1 and the falling factorial (k)_(v-1+g) from the exact bridge incidence bound. Their sum is a finite binomial:

E X_v <= binom(N,v) v^(v-3)(k)_(v-1)(4/D²)^(v-1)(1+4b_v/D²)^(k-v+1),

where m=2k, D=N-2k+1>0 and b_v=(v³-v)/36. This yields a geometric size tail with per-vertex exponent proportional to k/N^(2/3), instead of the old k³/N² exponent. Section4 records a still sharper finite upper bound replacing D^(2q) by D(D+1)...(D+2q-1). H0 sums genus>=2; H1 sums genus>=0. Both preserve the actual bridge normalizer through exact count incidences.

## Honest baseline comparison and unresolved range

The old finite tail ALREADY implies m=cN^(2/3)(ln N)^(1/3) for any fixed c<24^(1/3). That is an algebraic corollary, not new research. Our log N factor is a genuine larger range obtained from the finite binomial, without changing H0,H1 or K. This does not reach m^4<=N³. A vacuous upper bound is never called a sampler obstruction.

The new proof's first unproved step for the full benchmark would be a negligible upper bound on the actual omitted event over that larger range. R2's separate proof instead establishes that this cannot hold for unchanged H0/H1 along its explicit sequence. Existence of another polynomial-time negligible-error algorithm remains T0 and remains open.

## Nonauthor obstruction audit

R2-O1 input SHA256 `a6716e623768ded49b5ba1a2441abdddc8cb18c61be52d8a96b79387fe68b33f`. Full report: **obstruction_audit.md**. For all j>=64, N=2^(8j),m=2^(6j) satisfies m^4=N³ exactly and has

Z_A/Z<=2^(-1-jm/2).

The proof keeps arbitrary genus for v<=K in the numerator, uses only positive coefficient domination, and uses the exact subgroup bridge lower bound in the denominator. Every displayed constant and top-level cutoff step checks. I accept its mathematics subject only to the explicitly imported genus majorant being verified in the coordinator source audit. No repair requested. This refutes P0 and P1 and leaves T0 open; it is not sampling hardness.

## Evidence, dependencies and reproduction

R3's `finite-inequality-results.json` records 53,300 component-term checks and 7300 size sums/binomial identities (m<=48,N<=1000), all exact. R2's nonauthor review adds 3850 genus/rising comparisons,1045 binomial identities and409 H0-zero cases.

Our own `audit_checks.py` imports only the prehashed old positive connected-count code and compares 567 profile/exponential coefficients,304 numerator S_A bounds,16128 subgroup lower bounds,6300 sharper incidence terms and1000 exact integer j cases. All pass in roughly 0.19 seconds. Complete raw output is **audit_results.json**. Required small counts 27,120,3936 match; no sampler logic was changed, so no new distributional sampler test is claimed. Deterministic exact tests do not prove asymptotics.

Reproduce from repository root:

`timeout 90s python3 -B experiments/20260922-sparse-boundary/roles/r1-upper/audit_checks.py`

Python 3.12.3, standard library only, no stochastic seed. The `python` executable was unavailable; existing `python3` was used. Commit: `20e86f665f69053031fe7eec0c3388458affb1fc`. All old executable hashes are checked before import; no packages, services, sessions, machine changes, commits or pushes were used.

Load-bearing imports are the DYZ-derived factorial genus majorant/minimal count, exact component marking and fresh-pair incidence, and the previous exact H0/H1 algorithms/resources. This role reread the old proofs; coordinator/R4 own fresh primary-source and algorithm closure. HANDOFF/GOAL_SPEC still state the old mixing task; the frozen authorized global-sampling objective supersedes that research direction, and no old files were edited.

Boundaries: m0,m2 and N2 exact; odd m and positive m at N1 have empty target; near-minimal genus budgets and zero-count residuals are handled explicitly. H0 additionally retains all large-support genus0/1 words and all small-support arbitrary-genus words.

Only files in this role directory were written. Final inventory is in changed_files.txt and artifact_manifest.json. No construction or process remains running.
