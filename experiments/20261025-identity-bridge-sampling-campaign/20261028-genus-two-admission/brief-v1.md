# Frozen investigation brief I1.v1 — genus-two decoding and usefulness

Frozen 2026-10-28 10:47 UTC. Base commit d8893491e04aff74ff3185f7054470ffa24a44a4. Attempt 000002, not a new mission. Allocation through 13:47 UTC, with construction reports due by 13:00 and at least 47 minutes for review/integration; earlier decisive reports may shorten construction. Attempt wrap-up remains 16:35:16 UTC and hard deadline 16:45:16 UTC. No new long allocation may cross those bounds.

## Targets and conventions

T2: For each v>=2 and b>=1, sample uniformly (or TV <=2^(-b)) from connected ordered transposition identity words on [v] of length 2v+2 in expected poly(v,b) bit time. Prefer the closed endpoint interface F(V,sigma,g), g<=2, length |V|+c(sigma)-2+2g. Rightmost-first map composition; explicit literal words and canonical labels; independent fair bits. Singleton g=0 is the empty word, singleton positive genus is infeasible. Reject zero fibers. This is not the global mission theorem or a Markov-kernel claim.

M2: Determine a rigorous global consequence or obstruction for the fixed top-level policy allowing every g<=2 component plus arbitrary genus on v<=L, where P=N+m+2 and L=max{1<=v<=N:3^v<=P^4}. Compare exact bridge-conditioned mass, not an unconditioned graph. A broader fixed-G obstruction may be investigated if its precise statement is frozen before proof. Do not rerun the old H0/H1/H2 claim as new research.

## Admission and novelty

Read exact S1.v2 proof and its R2 recursive/synthesis audits: final-letter decomposition and conditional cycle-allocation law are accepted only for g<=1. Their scope does not cover T2. Read C1 structural report/proof and its separate exact-version audit: positive unicycle grammar and cut correction are genus one. R4's September22 plan initially mentioned genus two but explicitly changed to quotient-state H2-QC.v1 before construction. The stronger blind all-N sparse obstruction is preserved as provisional in P-BLIND-STRONG, while the accepted canonical obstruction is a subsequence result; neither is claimed new here.

Concrete new ingredients to test:

1. Recursive: the genus-two split introduces (g_A,g_B)=(1,1), in addition to (0,2),(2,0). Tensor moments on individually labeled cycle assignments may aggregate the product of the two existing positive genus-one count formulas. The genus-two single-factor count/allocation formula remains a named obligation; signed exact arithmetic may be used only when the final branch mass is rigorously shown nonnegative with polynomial bit size.
2. Structural: test cuts where the total genus of the prefix components equals one and the suffix total genus is at most one. The candidate identity g=G_left+G_right+beta_1(incidence graph) suggests only trees/unicycles are needed at such a cut, decorated by genus-one vertices. This identity, universal cut coverage, local weights, graph multiplicities and an actual parser are obligations, not assumed facts. First falsify cut coverage on the smallest genus-two words before designing a large grammar.
3. Mass: genus-two extension changes the allowed event. Derive a fixed-genus count envelope from the positive identity-count recurrence or a checked primary source, then assess whether the enlarged event retains substantial mass in the sparse gap. Finite comparisons only support diagnosis; they do not establish an asymptotic regime.

Novelty searches may stop a route if an exact predecessor already covers it. Preserve that overlap and redirect only through coordinator admission.

## Roles and separation

R1 recursive construction: owns roles/r1-recursive; derive all branches, partial-assignment oracle and exact word/bit law or first missing lemma.
R2 structural construction: owns roles/r2-structural; prove/refute cut coverage, then weighted grammar, parser and reciprocal-cut correction.
R3 mass/falsification: owns roles/r3-mass; freeze M2 or a strictly stated fixed-G envelope; check global usefulness and retained historical negative results.

Each role writes full input, plan, halfway checkpoint, proof or obstruction, scripts/raw output if used, and immutable report-v1.md. No descendants, separate research CLI sessions, commits, protected/shared file edits, model/tier/permission changes or installations. Coordinator owns central claim graph and review reconciliation. All workers inherit Astra/ultra/default; metadata limits are disclosed.

## Computation and regression contract

Before a job, send the coordinator the exact command, tested claim, state estimate, memory estimate, wall timeout, seed(s), output path and dependency versions; wait for a job reservation. One heavy job at a time. Current helper is /home/nico/projects/harnesses/codex-research-harness-releases/v0.3.2/src/research_harness/bounded.py and sealed run is /home/nico/projects/research_projects/reversible_circuits/.campaigns/identity-bridge-sampling-20261025/attempts/000002/run.json. Never use older paths. All detailed output goes directly to unique artifact files, with small console summaries. Current-helper inert smoke passed and first checkpoint was verified before this investigation.

Initial finite targets: full S3 genus-two identity law (length8, at most3^8=6561 words); optional S4 length10 (6^10=60,466,176 words) requires a more efficient state/count method and its own resource estimate, not an automatic exhaustive run. Changed sampler logic must retain S3,m4 and S4,m4 checks, and S4,m6 when feasible. Boundary m odd,0,2; N2; minimal connected endpoints; zero branches; label/interleaving multiplicities are required.

Historical regressions: (ab)^3 and extended zero-square insertion fibers; transposition endpoint 81 total versus80 connected in S3,length5; unweighted support graph triangle mass1/4 versus3/4; parallel-core/unequal-cut multiplicities; fixed-top-level cutoff and adaptive posterior normalizers; CP-1 rejects multiplying marginal lightness bounds. All prior failures remain failures of their exact mechanisms.

## Outcomes and review

Positive construction: freeze exact theorem/proof/code/hashes, then fresh blind theorem-only referee and separate exact-version nonauthor audit, followed by coordinator decisive rerun and dependency closure. All same-model reviews are correlated. A repaired version stays REPAIRED-PENDING-RECHECK. No worker promote verdict alone certifies T2.

Negative: preserve exact witness and failed statement, keep surviving auxiliary results, retire only that route/version. Inconclusive: isolate first missing lemma/oracle and HOLD unchanged mechanism pending a new ingredient. Useful positive T2 does not certify global sampling; M2 can fail independently. Main mission remains OPEN unless full terminal criteria are met.
