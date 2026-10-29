# Connected Identity Bridges: Uniform Genus Dependence

User-authorized single four-hour research attempt, 2026-10-28.
Run ID: genus-scaling-20261028. Fresh native session, not a resume of the old
identity-bridge-sampling campaign. Four total agents, coordinator plus at most
three workers, all model gpt-6-astra, effort ultra, default service tier,
workspace-write with auto-review. No automatic research restart, quota resume,
between-attempt manager, successor mission or extra coordinator session.

## Scope and Source Precedence

The user is satisfied with any polynomial-time statistically-close-to-uniform
sampler, not specifically fast mixing. This allocation explores the reviewed
connected genus-two constructions and their dependence on genus. It is not
a heat-bath proof run, a rerun of the completed genus-two construction, or a
new attempt to close the interrupted exact sparse-sampling reviews.

Read PROJECT_MAP.md for the historical frontier, then notes/project-map/FRONTIER.md
and the current programme/decisions on this branch. Read AGENTS.md, HANDOFF.md,
GOAL_SPEC.md and the project sampler skill/references as required, but explicitly
record their historical heat-bath/conditional-classification disagreements.
This user-approved brief supplies THIS run's target; do not silently substitute
the older mixing objective or rewrite protected instructions to resolve it.

Scientific baseline is the committed, reviewed I1 outcome inherited from
commit1fe07986764490ebeabb9bccf77e3d713e2a8f95. Main source directory:

    experiments/20261025-identity-bridge-sampling-campaign/20261028-genus-two-admission/

Read report.md and reconciliation-v1.md first. Trace only needed statements,
proofs and implementations in roles/r1-recursive, roles/r2-structural and their
exact-version reviews. These are source-scoped INTERNAL acceptances with
correlated same-model reviews, not human/external proof certification. Preserve
author banners and all old hashes. The recursive construction handles connected
arbitrary fixed endpoints at genus0/1/2; the second construction handles
connected identity genus2. Neither is a global all-length sampler.

I1 also proved the M-GROW.v1 obstruction to low-genus/small-support eligibility
policies on its explicit m=N^(3/4) subsequence. Even genus growing up to N^(1/8)
does not fix that policy on the stated sequence. An FPT-in-genus result would
be a meaningful primitive, not a solution of that global obstruction.

The old campaign's newer uncommitted I2 sparse candidates and reviews remain
preserved in its separate worktree. They are not promoted by this fresh run.
Do not duplicate its completed authors, production-law audits or theory review.

## Frozen Mathematical Target T0

For N>=2 and integer g>=0, let F(N,g) contain the ordered transposition words
on exactly the labels [N], with rightmost-first product identity, CONNECTED
support on all N labels, and length m=2N-2+2g. The target is uniform on F(N,g),
not uniform on support graphs, conjugacy classes or all identity words.
Use independent fair bits and explicit output. Count bit operations, not just
unit-cost arithmetic, and distinguish expectation from worst-case bounds.

Primary OPEN target: one uniform algorithm and absolute constants C>1,c,A
such that sampling is exact and expected bit time is at most

    A C^(g+1) (N+g+2)^c

for every N>=2,g>=0. C,c,A may not depend on either parameter. This would
give polynomial time when g=O(log N) for each fixed constant in that O bound.
No external source or existing report is assumed to prove this target.

Acceptable substantial partial targets, each frozen under a separate version:
an explicit f(g)(N+g+2)^c bound with absolute c and uniformly computable f;
a 2^(O(g log(g+2))) dependence; an exact reduction isolating one concrete
genus-dependent coefficient/allocation primitive; or a checked obstruction to
a proposed encoding. A bound N^(O(g)) is NOT FPT in genus. A diagnostic g3
extension alone is not this run's main success criterion. Approximate sampling
is allowed as a separately versioned target with TV<=2^(-b), the same explicit
parameter dependence times poly(b), and no hidden b-dependent N exponent.

First diagnostic: g3, identity length2N+4. For a recursive auxiliary theorem,
freeze the arbitrary-endpoint version separately: for sigma with k cycles,
connected words have length N+k-2+2g. Do not infer the identity sampler from
unavailable uniform endpoint conditioning. Track every auxiliary dependency.

## Team and Four-Hour Allocation

The external cap starts at service activation. Read the current cap sidecar on
entry and at continuations; give workers its absolute deadlines. Never reset
the clock, launch another service/CLI session, or move work outside the scope.
The installed cap enforces the whole team's four hours, including shutdown.
Reserve the final20minutes for delivery. No native goal or token budget is
requested. Do not create worker goals or use sleeps to consume the allowance.

Suggested timeline, always subordinate to the actual sidecar:

- T+0..20min: focused recovery/novelty and exact target/claim graph; assign roles.
- T+20..130min: complementary construction, generalization and falsification.
- By T+130min: freeze candidate proofs/code or exact unresolved obligations.
- T+130..200min: fresh statement-only and exact-version reviews; repair/recheck.
- T+200..220min: reconcile findings, rerun smallest decisive checks, scope verdicts.
- T+220..240min: stop new experiments; final report, artifact inventory and handoff.

Roles (one owned directory per worker):

1. r1-recursion: continue the reviewed final-letter/positive-marker construction.
   Derive g3 as a diagnostic; expose which table dimensions grow with g.
   Seek a genuine compression or coefficient oracle with N exponent independent
   of g. Separate coefficient evaluation, restricted allocation and literal-word
   decoding. Scalar counts alone are not a sampler. Exact signed computation
   of positive total masses is permitted if bit cost and cancellation are paid;
   signed summands may not be sampled as probabilities.
2. r2-structure: continue the reviewed marked-cut construction with complete
   incidence multiplicities, ports, equal-child symmetries and rejection cost.
   Seek a genus-uniform grammar/core representation or a new structural
   ingredient. Do not assume the genus-two cut probability generalizes.
3. r3-adversarial: begin in a fresh non-inheriting thread with T0, definitions,
   boundary cases and permitted PRIOR sources only. Withhold the other workers'
   new proofs, confidence and suspected failure. Independently test the target
   and its complexity barriers. Freeze a complete statement-only report before
   reading new candidates; disclose same-model correlation and visible project
   context. After freeze, it may perform an explicitly NONBLIND exact audit.

Coordinator: produce the exact worker input files before delegation; preserve
full prompts/reports. Use no worker descendants and at most three live workers.
Recycle closed slots for fresh reviews; do not exceed four total contexts or
invent tasks just to fill slots. Record actual worker startup and any capacity
shortfall. Work locally rather than launching independent CLI workers.

## Proof and Experiment Gates

Use the mathematical-proof-audit skill, including the audit protocol and
probability regressions. Preserve all project counterexamples: missing
support-connectivity conditioning, 81-versus80 fibers, unweighted-graph bias,
(ab)^3 insertion, equal-child/parallel-cut multiplicities, incorrect adaptive
marginal products, and the existing low-genus policy obstructions.

Keep a versioned claim graph and ledger. A repair reopens dependent claims
until a fresh exact-version audit. No claim is accepted without a complete
proof, explicit imported-source verification, boundary checks, blind statement
review and exact-version nonauthor review. Reviews share model lineage. A
finite successful check cannot prove a universal theorem or complexity bound.

Validate N2,N3,N4 and g0,1,2,3 as appropriate. Include singleton recursion
bases (empty only at genus0), odd identity lengths, m0,m2, minimum connected
length and zero-count branches. Preserve global S3m4/S4m4/S4m6 regressions when
using global helpers, but do not confuse those reference counts with CONNECTED
counts. Use exact DP/quotient counts rather than huge full-word enumeration;
in particular do not enumerate all N4,g3 words. Named finite checks may compare
counts and forced-allocation masses or full small output laws.

For each computation record claim, exact command, commit, Python/dependency
versions, ranges, deterministic seeds where relevant, resource estimate and raw
output. Use existing Python; Magma/SAT only for a named essential finite check
through an already authorized bounded path. No installs or machine changes.

Use the CURRENT attempt's sealed run-file and bounded helper from its startup
instructions. Build argv from current metadata, never copy old absolute paths.
First run a tiny inert actual-sandbox bounded smoke. One mathematical job at a
time with a coordinator reservation; maximum16GiB address space per job and
an explicit timeout fitting the remaining envelope. Prefer <=1GiB/180s for
tiny checks. Detailed output goes to unique artifact files, not the console.
Do not weaken admission on a rejection; preserve the diagnostic and continue
supported symbolic work where safe. Never accept incomplete output as success.

## Ownership and Outputs

New research only under:

    experiments/20261028-genus-scaling/
    research-campaigns/genus-scaling-20261028/

All previous sources, the old campaign, HANDOFF.md, AGENTS.md, GOAL_SPEC.md,
manuscript, skills and central project map/programme are read-only for this run.
Provide a proposed programme/map delta in the new experiment, not central edits.
Workers edit only their role directory. Coordinator owns synthesis and scoped
LOCAL checkpoint commits on this new run's branch; no push, amend, reset,
branch changes, global Git configuration changes or unrelated staging.
Respect the launcher's current checkpoint/attention protocol. A commit is not
proof certification. Do not refresh source hashes to conceal changed evidence.

Maintain plan.md, claim_ledger.md/json, dependency graph, failed-approaches.md,
machine-readable finite outputs, role checkpoints/full reports, and RECOVERY.md
from early in the run. Final report.md must explain in plain language:

- what is genuinely new beyond reviewed genus2;
- exact distribution, parameter regime and accuracy;
- derived dependence on N,g,b and the first unproved step;
- which constructions survived, failed or remain provisional, and why;
- full review and experiment evidence, not vote counts;
- whether any global sampling consequence actually follows;
- the single highest-value next investigation and its first test.

Keep a compact resume.md with exact file/claim versions and unfinished tasks.
Partial, negative and minority findings survive interruption. Do not mark T0
proved merely because g3 works, a draft exists, or a time cap is reached.
Completion may be early only after T0 or a checked refutation closes with all
required reviews; otherwise pursue substantive in-scope work until wrap-up,
or isolate an honest obstruction without filler. The four-hour cap authorizes
no automatic continuation. A timeout leaves all unresolved claims unresolved.
