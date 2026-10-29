# Sparse-Noise Identity Words: Bounded Viability Study

Authorized 2026-10-29. Run ID: noisy-bridge-20261029. One fresh session,
90 minutes including shutdown, four total contexts (one coordinator and at
most three workers), all gpt-6-astra with reasoning effort ultra and default
service tier. Workspace-write with auto-review is for legitimate scoped
execution/checkpoints, not a sandbox workaround. No automatic restart, refill
resume, separate manager, successor mission, funding change or push.

## Mission and Scope

Determine whether sparse independent replacement of transposition gates can
hide a concrete structured identity-word construction from the SAME noise
applied to a globally uniform identity bridge. Seek either a quantitatively
proved efficient attack on a meaningful family beyond the known trivial
pairing controls, or at most two completely specified candidates with an honest
account of which attacks they survive. Testing cannot certify pseudorandomness.
Do not assume that any candidate exists or that general sampling hardness
follows if the candidates fail. A precise unresolved obstruction is a valid
time-limited outcome, not a theorem or a successful security construction.

This is a user-approved new cryptographic target, not GOAL_SPEC.md's historical
heat-bath assignment. Read PROJECT_MAP.md before choosing routes, plus AGENTS.md,
HANDOFF.md's hardness sections, the sampler skill and its sampling/experiment
references. Record source disagreements instead of silently adopting an old
claim. Do not spend the allocation redoing the all-length sampler or mixing
frontier. Existing direct global samplers in short/sparse/dense regimes and
the recent connected low-genus sampler are separate scoped inputs.

## Frozen Game M0

Use an explicit security index lambda and declare polynomial relationships
among N, L, k and lambda for each asymptotic claim. Time polynomial in N,L is
not automatically polynomial in log2(N) wires. N>=2, L even, 0<=k<=L.
T_N is all q=binom(N,2) transpositions; mu is its uniform law. Products act
rightmost first. U(N,L) is uniform on ALL labeled ordered length-L words with
product identity, not only connected-support words or a Hurwitz orbit.

Q_k chooses a uniform k-subset of positions without replacement, independently
of the word and all other tapes, and replaces those gates by independent mu
draws. A replacement may equal the old gate. The positions and tapes are hidden
from the adversary. Fixed-known positions and Bernoulli noise are different,
separately versioned variants, not silent substitutes.

Each candidate freezes Setup, public data A, any secret setup K, an exact
identity-word sampler D_{A,K}, its uniform random tapes, representation and
runtime. State whether sampling requires public A only or a secret key, and
whether fresh per-word secrets are used. Expose identical public A in both
worlds. The reference is independent global U(N,L) with fresh Q_k in each
reply. A reused-setup experiment gives every polynomial number of requests
fresh word/noise tapes under the same setup. No decoder oracle is supplied.
Compare complete observed words, not just endpoints:

    (A, fresh Q_k(D_{A,K}) replies) versus (A, fresh Q_k(U(N,L)) replies).

Freeze one-sample and reused-setup claims separately. Distinguish average setup
security from every-key security and statistical from computational bounds.
Any claim of computational hardness is conjectured unless reduced to an
explicit established assumption with all interfaces and parameters checked.
Merely naming the desired indistinguishability is not a hardness reduction.

Correctness here is semantic: disagreement of the computed permutation with
identity on uniform x in [N], not PRC detection/decoding or false-positive
soundness. A k-replacement error is a product of at most 2k transpositions,
so disagreement is at most min(1,4k/N). This is a bound, not equality or a
guarantee of negligible error for nonzero k polynomially related to N. Keep
hiding noise separate from any later transmission/adversarial noise.

## Mandatory Prior Work and Regressions

The operator will snapshot the foreground projection report/checker/results
under this run's inputs/ directory. Read those proofs and exact-law tests;
they are foreground derivations, not independent proof certification.

1. Under exact GLOBAL U, every fixed ordered k-subsequence has the first-k law
   by a stable-sort Hurwitz bijection. For h=a1...ak,
   Pr[t_I=a]=q^(-k) p_(L-k)(h^(-1))/p_L(id), with p_r=mu^{*r}.
   This formula does NOT hold after conditioning on connected support.
2. Replacements have product product_j(A_j B_j), where P_j is the original
   prefix, B_j=P_j t_j P_j^(-1), and the fresh conjugated A_j are iid mu and
   independent of the old word. The B tuple is not iid in general. For any
   original law the endpoint is p_k convolved with the product law of B_j.
   Replacing that by the raw selected-gate product law needs word-law invariance.
3. For global U the replacement endpoint tends to p_(2k) when the unselected
   completion length is sufficiently long. Period-two parity must be respected.
   This endpoint condition is only necessary for full-word security.
4. With fixed i!=j, if p=Pr[t_i=t_j], after uniform k-subset replacement,
   Pr[t'_i=t'_j]=alpha*p+(1-alpha)/q,
   alpha=(L-k)(L-k-1)/(L(L-1)), L>=2. Pair-equality advantage between sources
   is exactly alpha times its original advantage. Reprove only as a smoke
   regression, not this run's main contribution.
5. A word repeating one uniform transposition at every position (even L)
   has uniform single gates, and with k=1 its endpoint is exactly p_2, yet
   its noisy full word is easily distinguishable. Doubled adjacent iid pairs
   and mirrored inverse words are additional syntax-leakage controls, not
   novel candidate successes.
6. Pure Hurwitz evolution cannot choose global orbit weights. Conjugation
   only relabels; cyclic shifts do not independently randomize construction
   structure. Finite spectra, passing diagnostics, or failure to recover a
   secret do not establish computational indistinguishability.
7. Sign, transposition distance <=2k, and support <=4k are common to both
   matched noisy worlds. They alone are not distinguishers. A baseline of
   unrestricted random words, uniform S_N, or an unmatched connected law is
   invalid unless explicitly used for a separate statement.

## Team and Time Allocation

Read the CURRENT attempt's cap/status metadata on entry and at continuations.
Its absolute time limits override suggestions below. All workers inherit
Astra/ultra/default tier, have no descendants, and own separate directories.
Record their actual start/finish IDs, not just the configured thread ceiling.
Recycle closed slots for reviews but never exceed four active contexts or
start another CLI/tmux/service. No native goal or token budget is requested.

- T+0..10min: freeze M0 variants, inventory inputs, create live partial report,
  perform tiny actual-sandbox bounded smoke, and delegate focused roles.
- T+10..55min: construction, rigorous attacks and bounded exact diagnostics.
- T+55..80min: freeze authored versions, cross-review, decisive reruns and
  reconciliation. Close or cancel unnecessary workers early.
- T+80..90min: delivery only, with graceful shutdown inside the envelope.

Roles:

1. r1-theory: derive an attack/noise-survival bound that extends beyond the
   already-known pair controls, preferably addressing relator locality,
   bounded scrambling, support structure, or short subword relations. State
   all hypotheses so it applies to an explicit family rather than claiming
   all structured samplers fail. Own proof and finite counterexamples.
2. r2-construction: specify at most two candidates beyond the obvious controls.
   Identity before noise, fixed length, setup exposure, entropy, polynomial
   generation and any scrambling must be explicit. Supply a small executable
   implementation or exact pseudocode and document failures. One candidate
   at a time; use the first rejection to inform the second, not parameter
   tuning of an unchanged known failure. Do not smuggle a near-uniform sampler
   or an assumed secure relator compiler into the alleged noise mechanism.
3. r3-adversarial: first reconstruct attacks from M0 and candidate algorithms
   WITHOUT r1's proposed proof/status. Freeze a short complete blind report.
   Then run matched-reference tests, audit the exact authored theorem versions
   nonblind, and retain every negative/minority finding. Separate training
   choices from held-out tests; no post-selected empirical security claims.

The coordinator owns security quantifiers, synthesis and final proof graph.
Use the mathematical-proof-audit skill/probability regressions for material
claims. Preserve full reviewer inputs and reports. Repairs reopen downstream
claims and need an author-distinct exact-version recheck. Same-model reviews
are correlated; a blind report is not human or statistically independent
certification. A quota/time interruption can leave a claim provisional.

## Computation and Resource Contract

Use existing Python/stdlib first; do not install packages or change services,
machine/user configuration, permissions, authentication or the harness.
Use only the CURRENT attempt's sealed run file and bounded helper from the
injected startup instructions. First execute a tiny actual-sandbox inert job
through that helper; metadata-only checks are not sufficient admission.
One mathematical job at a time under coordinator reservation, <=16GiB
address space, explicit timeout inside the remaining budget; prefer 1GiB and
120s for tiny checks. Detailed results go to unique files, not long console
capture. Admission failure is not permission to run unbounded outside scope.
The whole attempt has MemoryMax128GiB, MemoryHigh96GiB, swap0.

Validate S3,L4 and S4,L4; add S4,L6 if feasible. Include k0, k1, kL, N2,
L0 where meaningful and reject odd identity lengths. Exact global bridge
counts 27/120/3936 are distinct from connected counts. Use the snapshotted
checker as a reusable exact reference only after inspecting its conventions.
Avoid full-word enumeration at long L; exact permutation/cycle-type DP may
provide small-group long-bridge baselines. Explain any approximation and its
TV cost. Prove matching of literal-word sampling, not merely scalar counts.
Use several fixed seeds for empirical statements; give exact commands,
commit, Python/dependency versions, parameter ranges, resource estimates,
effect sizes and raw machine-readable output. No finite check proves an
asymptotic attack bound or security claim.

## Cross-Project Reading and Ownership

The separate project /home/nico/projects/research_projects/continuous-prc is
READ-ONLY. Its project map and frozen Gaussian/binary source model may inform
cover/noise separation, reused-key quantifiers and fixed-word rejection, but
do not import a claimed compiler or hardness theorem without checking scope.
No edits, experiments, Git operations or launched agents in that project.
Do not turn this allocation into a survey or audit of its large archive.

Write only under:

    research-campaigns/noisy-bridge-20261029/
    experiments/20261029-noisy-bridge-viability/

Workers own only their role directories beneath the experiment root. The
coordinator owns plan/report/reviews/ledgers and campaign handoff files.
Protect all historical artifacts, primary worktree, central maps, manuscript,
HANDOFF.md, AGENTS.md, GOAL_SPEC.md and skills. This brief explicitly permits
COORDINATOR local checkpoint commits on the isolated campaign branch under
those two roots, superseding historical unattended-worker commit bans only
for that coordinator/scope. No push or publication. Review exact paths before
staging; retain unrelated changes and never reset them. The operator's sealed
input snapshot is provenance, not a mathematical acceptance.

## Quota, Checkpoints and Delivery

The external account guard wraps at remaining<=8% and stops at<=6%, providing
a best-effort buffer above the requested5% reserve. Time stops at90minutes,
whichever limit arrives first. Read current compact quota/cap status at normal
checkpoints (roughly every5-10minutes), not tight polling. Wrap-up notices are
cooperative metadata, not guaranteed injected messages: at wrap-up, stop new
experiments, collect drafts and write the handoff immediately. Missing or stale
quota readings do not authorize more inference. Do not lower thresholds, keep
working after stop, redeem credits/reset, or resume after refill. Other sessions
and in-flight requests can overshoot; never promise exact reserve preservation.

Create report.md and RECOVERY.md early. Each worker checkpoints by T+25min and
publishes a full final report by T+55min or earlier quota wrap. Coordinator
checkpoint commits roughly every20minutes and at coherent handoffs. No empty
commits, no hidden pending results. Publish incomplete work as clearly labelled
drafts before an external interruption. No automatic restart or successor.

Required outputs: plan.md; model-v1.md; candidate algorithms/implementations;
raw results and reproducible scripts; full proofs or precise failed steps;
complete reviews and reconciliation; claim ledger with status, assumptions,
evidence, independent-check scope and action; regressions; report.md; and a
short self-contained campaign RECOVERY.md with exact continuation tasks.
The main report contains the project candidate/target/identity/diagnostic
table, plus a noisy-word attack table distinguishing one-sample/reused-setup
tests and effect size/sample/time complexity. Give a short continue/redesign/
deprioritize recommendation with the highest-value next obligation.

Finish early only after meaningful attack-or-candidate outcomes and their
proportionate review are delivered, not merely after repeating the known
pairing counterexample. At the cap, an honest inconclusive scoped outcome is
acceptable. If the mission is finished, commit a scoped COMPLETION.json for
operator review, not self-certified security. If unfinished at quota/time,
save the precise gap without claiming completion. No completion marker,
agent agreement or successful Git checkpoint certifies cryptographic hardness.
