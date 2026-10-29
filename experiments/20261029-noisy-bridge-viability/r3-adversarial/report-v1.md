# r3 adversarial report v1

Authored 2026-10-29 before the 08:02 UTC deadline. Model: M0 version 1, global uniform labeled ordered identity bridges, rightmost-first products, identical independent uniform-k-subset replacement on both complete-word laws. Public setup is exposed identically; all reply tapes are fresh. There is no decoder oracle. Same-model reviews are correlated and no agreement certifies security.

## Findings and scope

1. **Proved in the reviewed finite model:** T0 gives an efficient one-sample six-window relation attack on concatenated six-gate identity blocks with the stated bounded adjacent-Hurwitz budget, including C1's declared schedule. The exact authored proof passed my blind reconstruction and subsequent exact-version review. It needs no long-walk mixing theorem. My recommendation is acceptance after coordinator provenance/ledger closure.
2. **Proved identity with repaired computational scope:** LC1-v3 transfers any publicly computable fixed-coordinate bias through M0 at the explicit alpha_s/(2*3^s) factor. Versions 1 and 2 are retained with arithmetic/access wording objections. V3 resolves both; the probability identity never changed. A fresh repaired-version reviewer is still the coordinator's responsibility.
3. **Provisional independent C2 attack:** BS3 proves, for the C2 schedule lambda>=81, support-test advantage at least 1-2(18/lambda)^lambda, regardless of the Hurwitz step count. This is an elementary support-count argument, not a sparse-sampler or mixing import. It awaits the coordinator's author-distinct exact-version assessment if promoted.
4. **Exact finite C1 diagnostics:** all 21 combinations N4,L6,s in {0,1,2},k in {0,...,6} completed. Sparse replacements leave substantial complete-word differences even though every single-coordinate edge marginal is exactly uniform. Conversely k=5 and k=6 erase all differences in these cases; this negative finding is preserved.

No generic sparse-noise impossibility, general sampling hardness, negligible semantic correctness, or surviving secure construction is established. Both candidate-specific attack routes are fully separate from endpoint sign/distance/support restrictions shared by the two worlds.

## Blindness and artifact sequence

`blind-report-v1.md` was frozen from M0 and permitted historical projection inputs before any candidate or proposed proof. It contains local relation counting, exact reference beta, support/Hamming-neighborhood tests, and a reused-setup counterexample. `blind-supplement-v1.md` reconstructed LC1 from its statement and assessed C1 from its algorithm. `blind-supplement-v2-T0.md` reconstructed T0 from its statement only. `blind-supplement-v3-C2.md` assessed C2 and its runtime erratum before reading rejection proofs. The C2 algorithm document itself disclosed its support-obstruction motivation; BS3 records that limitation on blindness. Proposed T0/LC1 proofs were read only afterward. The exact task, halfway checkpoint and all complete reviews are retained.

## Exact full-word experiment

Script: `exact_c1.py`, SHA256 `888e9d055381e4083ad24aac7e8240bb928a923eb56dcfdaa6f2453b6c098c8e`.

Raw output: `exact-c1-results-v1.json`, SHA256 `c9a6210d7a92e78a7fe9e99c41d390e9c81834ad5628a3795b3c12bf4582c23c`.

Coordinator job J004 used 120 seconds/1 GiB limits; observed result passed in 4.57577752112411 seconds, Python 3.12.3, standard library, commit `24649e0a2b4fa0d0ede444234bfedfc428453571`. There is no random seed: every probability is exact. The exact launch command was:

```sh
python3 -B /home/nico/projects/harnesses/codex-research-harness-releases/v0.4.4/src/research_harness/bounded.py --run-file /home/nico/projects/research_projects/reversible_circuits/.campaigns/noisy-bridge-20261029/attempts/000001/run.json --timeout 120 --memory-gib 1 -- python3 -B experiments/20261029-noisy-bridge-viability/r3-adversarial/exact_c1.py --output experiments/20261029-noisy-bridge-viability/r3-adversarial/exact-c1-results-v1.json
```

The script refuses to overwrite the immutable result; a separately authorized reproduction must use a new output path. The sealed run file is attempt-specific and must not be silently reused in a later attempt.

All 6^6=46656 literal words are enumerated; 3936 are global identity bridges. The C1 integer tape laws at s=0,1,2 have total masses 24,240,2400 and supports of 24,168,912 words. The channel is the degree-k coefficient of product_i(Id+z E_i), where E_i sums over the old gate and broadcasts over each new gate; normalization is source_mass*binom(6,k)*6^k. Descending-degree updates use each coordinate once. This exactly implements hidden uniform-subset noise rather than independent Bernoulli noise. A separate literal replacement enumeration agrees at k=1 for the reference and unscrumbled C1.

Predeclared diagnostics include all-six-edges-distinct, positive edge multiplicity profile, distinct-edge count, gate-word support, component count and weighted component profile (including isolates as (1,0)), adjacent repeats, prefix/window product cycle types, endpoint cycle type and per-position edge frequencies. Whole-word TV is the exact optimum in this finite state space, a descriptive diagnostic rather than a held-out asymptotic adversary. All raw distributions are in the output.

| s | TV at k=0 | TV at k=1 | TV at k=2 | TV at k=5 | TV at k=6 |
|---|---|---|---|---|---|
| 0 | 163/164 | 323/328 | 12011/14760 | 0 | 0 |
| 1 | 157/164 | 73/82 | 17657/36900 | 0 | 0 |
| 2 | 63/82 | 93437/147600 | 716081/2214000 | 0 | 0 |

The predeclared all-six-edges-distinct event has one-sample advantage 149/984 at s=0,k=1; its structured/reference probabilities are 1/6 and 5/328. At s=1,k=1 its advantage is 139/1640, and at s=2,k=1 it is 253/4920. These are finite matched-world effects. They do not extrapolate the full-TV values to C1's many-block asymptotic schedule; T0 supplies the separate asymptotic attack.

The k=L-1 equality is structural: conditional on the sole retained position, its original gate is uniform and independent of all fresh replacement values, so the whole output is iid uniform. This holds for any source with uniform one-coordinate marginals (conditional on the public setup where required). It does not repair sparse-noise security and must not be suppressed because it is a negative finding.

## Claim/evidence ledger for this role

| Claim | Status | Assumptions | Evidence/artifact | Independent-check scope | Action |
|---|---|---|---|---|---|
| Local exact beta and robust witness attack | proved derivation, provisional role artifact | M0 global U; explicit fixed disjoint relation windows and move budget | B1 and BS1 | Reconstructed before candidate proofs; T0 gives stronger bound | Keep, prefer audited T0 in synthesis |
| T0 six-window theorem | recommend accept as proved | Exact statement; N>=1000 numerical corollary; L>=12; positive witness threshold | review-T0-v1.md and hashed authored proof | Blind reconstruction, proof/script audit, coordinator finite and direct-count rerun | Promote only exact scope through coordinator ledger |
| LC1 probability identity | proved | k<=L-s, independent exact-k channel, finite alphabet | BS1, reviews, 108-case regression | Blind coordinate-decomposition proof and exact nonblind review | Keep |
| LC1-v1 arithmetic wording | refuted/superseded | Variable s and unrelated rational denominators | review-LC1-v1-v2.md | Targeted distinct-denominator fixtures | Retain failure; do not inherit broad complexity claim |
| LC1-v2 efficiency wording | incomplete/superseded | Missing explicit public f cost and output bit-size premise | review-LC1-v1-v2.md | Public-interface/representation audit | Use v3 |
| LC1-v3 efficient transfer | recommend accept | Public polynomial-time f, polynomial-bit outputs or charged table, public positions, fixed s, explicit polynomial schedule | review-LC1-v3.md | Exact proof plus repaired arithmetic fixtures; fresh r2 review pending here | Close only after exact fresh review |
| C2 support-test advantage >=1-2(18/lambda)^lambda | provisional proved argument | C2 schedule, lambda>=81; gate-word support, not endpoint support | BS3 | Independent derivation; not yet a reviewer certification of my own proof | Submit for author-distinct review |
| C1 finite noisy-law gaps | exact finite fact | N4,L6,s0/1/2, all k | exact-c1-results-v1.json | Independent Q1 literal transform and endpoint normalization | Keep; no asymptotic extrapolation |
| C1 finite equality at k=5,6 | exact finite fact with general marginal explanation | Uniform source one-coordinate marginals for k=L-1 | raw results and argument above | Every output word compared | Retain minority finding |
| One-sample security implies reused-key security | refuted | Retained hidden keyed word example | B1.4 | Exact hand counterexample | Retain quantifier regression |

## Candidate and attack tables

| Candidate | Claimed target | Identity ok | Crosses Hurwitz components | Exact diagnostics | Verdict |
|---|---|---|---|---|---|
| C1-v1 plus runtime erratum | Candidate compared with global U; no uniformity assertion | Yes, every block and every move | Hurwitz stage preserves its support-component data; generation can vary labels | Exact 21 matched finite laws; T0 applies to declared sparse-noise schedule | Reject declared hiding schedule |
| C2-v1 | Candidate compared with global U; no uniformity assertion | Yes, path/star inverse products | Fixed-support connected class per draw; no Hurwitz step changes support | Construction-role checks separate; my support proof is analytic | Reject declared schedule subject to exact-version review |

| Attack | One sample / reused setup | Effect | Samples | Time |
|---|---|---|---|---|
| T0 six-window scan | One sample; every-key result survives reused setup | >=7/10 in T0's stated range and C1 application | 1; optional fresh-reference amplification | O(L) label operations |
| C2 gate-word support count | One sample; no secret key in candidate | >=1-2(18/lambda)^lambda for lambda>=81 | 1 | Polynomial, e.g. O(L log L) comparisons |
| C1 all-six-distinct finite test | One sample, finite N4L6 | 149/984 at s0,k1 | 1 for displayed advantage | Six-gate inspection |
| Keyed coordinate collision template | Reused setup only | (1-k/L)^2 E||pi_K-mu||_2^2 for two replies | Two for effect; amplification needs key-wise gap | Polynomial gate comparison |
| LC1 | Transfer lemma, not a standalone attack | alpha_s/(2*3^s) times available local bias | 1 | Explicitly charged q^s evaluations; polynomial for fixed s under v3 premises |

## Recommendation and remaining work

Deprioritize these two constructions as sparse-noise hiding candidates. Retain the window and support attack lemmas as design requirements. A next construction would need to remove both public short-relation surplus and small-support concentration; the existence and security of such a construction remain unresolved. Do not treat surviving finitely many diagnostics as a hardness reduction.

For this role, no further experiment is justified by current evidence. Outstanding coordinator actions are exact repaired-version review closure, reconciliation of the C2 proof variants, and final evidence/claim ledger synthesis. All material counterexamples and negative findings are already durable. No files outside this role directory were edited by r3; no processes, descendants, installs, permission requests or Git mutations were initiated by r3.
