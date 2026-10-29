# Final theory report v1 — a surviving-relation attack

Role verdict: **keep the quantitative attack, reject the covered relator construction, and redesign beyond the two exposed failure modes**. The supplied theorem gives a deterministic linear-scan attack beyond the known doubled-pair controls. It does not rule out noise hiding for every structured identity sampler. This report is immutable; later coordinator reconciliation is a separate artifact.

## Main result and exact scope

Under frozen M0, write p_s for the s-step uniform-transposition walk and let U(N,L) be the GLOBAL uniform literal identity bridge. For even r and L>=2r, every fixed consecutive r-window after the matched Q_k noise obeys

    Pr[window product=id] <= p_r(id)^2 / p_(2r)(id),

for every k in [0,L]. This is a proved finite statement in the supplied argument, with audit status pending final coordinator reconciliation. It requires no mixing theorem, approximation, connected conditioning or independence between windows. The full proof is [proof-T0.md](proof-T0.md), D1–D2, and the exact frozen statement is [statement-T0.md](statement-T0.md).

For r=6, elementary exact counts give beta_N=p6(id)^2/p12(id)<1/40 for every N>=1000. A concatenation of M length-six identity relators, after an arbitrary global conjugation/cyclic shift, at most B adjacent Hurwitz moves and k replacements, still has at least

    H=M-1-2B-k

identity six-windows. This holds pointwise for all tapes, including adaptively chosen scrambling. The test scans all L-5 windows of L=6M gates and accepts when at least H have identity product. For H>0 its structured acceptance is1 and its global-reference acceptance is at most min(1,(L-5)beta_N/H). For H>=M/2 and N>=1000 its one-sample advantage is at least7/10, with O(L) operations on O(log N)-bit labels.

One explicit polynomial schedule is integer lambda>=32, N=lambda², L=6lambda², M=lambda², k=lambda and B=floor(lambda²/8). It satisfies H>=M/2. This schedule is a parameter choice within the frozen C1 finite construction family, not a third candidate. The construction role's principal C1 schedule N=lambda²,M=lambda^6,B=floor(M/10),k=lambda also satisfies H>=M/2 for lambda>=32 and is therefore covered. To verify the latter without approximation, H>=4M/5-lambda-1 and 3M/10>=lambda+1 for lambda>=2.

The theorem applies to all-distinct-gate six-relators such as the frozen C1 block (ac),(cd),(ab),(ad),(bc),(bd). Its observable is an ordered product relation, not equality of two gates. Other pair statistics may also reject the same candidate; no exclusivity is claimed.

The attack is every-key for any setup/source meeting the structural hypothesis. Reused setup is already broken with one request. On t independent fresh reference replies conditional on public setup, accepting only if all replies pass gives reference probability at most(3/10)^t, while structured acceptance remains1. The actual conditional product law justifies this optional amplification. The semantic error upper bound on the direct schedule is4/lambda, an inverse-polynomial upper bound, not negligible correctness.

## Exact diagnostics and provenance

The coordinator executed the submitted [check-T0-v1.py](check-T0-v1.py) as bounded job J003 using the current v0.4.4 helper, sealed attempt run file, timeout120s and address-space ceiling1GiB. It exited0 in0.666569s. Full machine-readable output is [results-T0-v1.json](results-T0-v1.json), with Python3.12.3, no nonstandard dependencies, exact deterministic arithmetic/no random seed, commit24649e0a2b4fa0d0ede444234bfedfc428453571, and the script hash. The exact harness command and reservation are retained in [the coordinator job registry](../coordinator/job-registry.json).

Checks passed:

* Global literal bridge counts27,120,3936 at S3L4,S4L4,S4L6, with direct enumeration agreeing with projected completion counts.
* Return moments, even-time maxima and36 completion-ratio inequalities per N for N=2,...,7, through time24; exact c6 and all length-three endpoint-type factorization counts agree with full-group DP.
* All local replacement masks and all k for eight exact cases, including S3/S4 length12 six-tuples. The largest tuple table is6^6=46656; long full words are not enumerated.
* The six-window survival inequality on6300 explicitly listed finite transformations, including every adjacent move position and both directions at N4,L36, selected rotations/noise positions and all fresh transposition values. This is bounded falsification evidence, not a proof of the universal budget.
* Exact rational verification of the N1000 constant; direct lambda schedule substitutions; pair-equality attenuation as a smoke regression; CP-1 rejects21/2000<=1/100; and the full-coordinate noise tensor is exactly iid.

The proof is mathematical; these tests can expose errors but cannot establish the universal claim independently. [regression-registry-v1.md](regression-registry-v1.md) retains boundary counterexamples and failed routes. [claim-ledger-v1.md](claim-ledger-v1.md) contains all dependencies and the audit scope.

## Reviews and the second construction

The author-distinct nonblind reviewer found no mathematical flaw in exact T0: [r2 full review](../r2-construction/review-T0-v1.md), with [exact input hashes](../r2-construction/T0-review-inputs-v1.json). I inspected that complete review and its remaining-gates statement. No repair or source edit was requested. The coordinator separately owns the r3 blind input/report and final acceptance decision. All reviewers share the same model and campaign lineage; this is correlated internal review, not independent statistical or human certification.

My complete nonblind review of C2 is [review-C2-v1.md](review-C2-v1.md), with the exact task and input hashes in [review-C2-inputs-v1.json](review-C2-inputs-v1.json). It supports C2's separate planted-support rejection: before noise its support is exactly m+1 even after any number of Hurwitz moves, and afterward it is at most h=m+1+2k. For N>=2m and h<=N, the matched noisy global-reference acceptance probability is bounded by

    min(1, binom(N,h) binom(h,2)^(2m)
           / ((N)_(2m) (2m)!/(4^m m!))).

On frozen C2's schedule N=lambda^6,m=lambda,k=floor(sqrt(lambda)), this is at mostlambda^(-lambda) for lambda>=1024. I found no mathematical defect. I recorded a nonblocking code/documentation precision issue about materializing all labels; the conservative stated polynomial runtime remains valid. No new computation was launched for this analytic review, and C2 implementation tests remain separate coordinator evidence.

## Required comparison tables

| Candidate / result | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
|---|---|---|---|---|---|
| C1 six-distinct-gate relator blocks with bounded signed Hurwitz scrambling | Q_k(C1) compared to matched Q_k(global U) | exact by relator and move identities | pure scrambling does not choose global orbit weights; independent blocks may start in different orbits | mandatory counts; exact local channels; finite witness budgets; construction-side checks separately | reject covered schedules by T0 |
| C2 path/star whole-word relation with planted support | Q_k(C2) compared to matched Q_k(global U) | exact by inverse cycle factorizations | Hurwitz preserves its planted support/subgroup | author-distinct analytic support review; coordinator construction checks separately | reject frozen sparse schedule |
| T0 even-window bound | a theorem about matched noisy global U, not a sampler | not a generation claim | not applicable | exact finite DP/channel tests | keep theorem, coordinator certification pending |

| Attack | One-sample / reused setup | Effect size | Sample cost | Time | Restriction |
|---|---|---|---|---|---|
| T0 count of identity six-windows | every-key one-sample; reused setup already broken | advantage>=7/10 when N>=1000,H>=M/2 |1 |O(L) label operations | bounded local scrambling and disjoint six-relator origin |
| T0 optional repeated-reply conjunction | same setup, fresh independent reference tapes | advantage>=1-(3/10)^t |t |O(tL) | exact conditional reference independence |
| C2 support count | one-sample; no hidden key | advantage>=1-lambda^(-lambda) for lambda>=1024 |1 |expected O(L), or deterministic O(L log L) | frozen sparse-support schedule; N>=2m |

## Limits, recommendation and next obligation

N=2 has identical noisy words; k=L gives identical iid worlds; L=0,2,6 and H<=0 do not satisfy the nontrivial six-window hypotheses. Odd identity length is impossible. The length requirement L>=2r is necessary for the lemma as written: at S3,L=r=6,k0 the sole window is identity with probability1 whereas beta6=1/3. This counterexample is preserved, not suppressed.

Large or nonlocal scrambling can remove the local witness budget. The support attack then rejects only samplers with the specified planted-support deficit. Neither failure establishes an impossibility theorem for all structured sources, a security construction, or general bridge-sampling hardness. Passing these two tests would still not certify security.

Recommendation: **redesign**, without starting a third candidate in this mission. The next meaningful obligation is to specify a generator that has both a reference-compatible support/component profile and a justified account of how its relator structure avoids an efficient full-word detector after the exact M0 noise. Merely adding more pure Hurwitz steps repairs neither global orbit weights nor C2's support defect. This obligation remains unresolved.

## Role handoff and files

Worker identity/root task: /root/r1_theory; inherited Astra/ultra/default-tier policy; no descendants, separate CLI sessions, package installs, permission changes or worker Git operations. The coordinator recorded the start in campaign tasks.json. Completion publication time is in role-finish-v1.json. The attempt cap remains external authority; this role has not created a campaign completion marker or declared the broad objective solved.

Files created under this owned directory: TASK.md, plan.md, checkpoint-v1.md, statement-T0.md, proof-T0.md, check-T0-v1.py, results-T0-v1.json (coordinator-executed checker output), review-C2-inputs-v1.json, review-C2-v1.md, claim-ledger-v1.md, regression-registry-v1.md, checkpoint-final-v1.md, report.md and role-finish-v1.json. No files outside the owned directory were edited by this worker. The coordinator must stage only explicit stable paths and retain other workers' changes; this worker does not stage or commit.
