# R3 exact diagnostics assignment

Worker /root/r3_diagnostics, explicitly requested gpt-6-astra / ultra.
Own only this directory. Reuse exact counts to compute Z_A/Z and Z_B/Z at small deliberately selected boundary cases; classify missing components. Independently falsify provers inequalities; no extrapolation of ratios as asymptotic proof. Start cheap timed pilot and increase only for named decisions. Preserve S3m4,S4m4,S4m6,m0,m2,odd,N1,N2,fixed-top-level K, arbitrary-genus small-support regressions. Hash inputs before import, Python -B. No delegation, goals, sessions, services, installs, escalation, configuration, commits, pushes, or edits elsewhere. No blind-referee messages before freeze. Timeout90s initial compute slot; notify root before increasing.

Authoritative UTC2026-09-22: started09:25:28.937730; halfway09:45:28; snapshot10:00:28; wrapup10:15:28.937730(no new construction); saved10:20:28; shutdown10:24:23.937730; deadline10:25:28.937730. Sidecars read on entry; never reset.

Frozen full run brief follows verbatim:

/goal
You ARE the new user-authorized coordinator. Do not launch another run.
Read the cap sidecar immediately and create one native research goal, if
available, without a token budget. Workers must not create competing goals.

# One-Hour Goal: Beyond the Sparse Sampling Boundary

Determine whether the current component sampler can extend beyond the
internally audited m <= N^(2/3) regime. The concrete proposed extension is
every even m with m^4 <= N^3. Seek either a negligible-error polynomial-time
sampling theorem or a rigorous obstruction to the named current sampler.
A genuinely new smaller extension is an acceptable separately stated result,
but does not establish the full benchmark. A precisely isolated gap is useful
partial progress, not a completed proof or refutation.

This is GLOBAL identity-word sampling, not Hurwitz or heat-bath mixing.
Any polynomial-time negligible-error sampler may establish the positive goal.
A negative result about one sampler does not prove sampling hardness.
Do not promise success or preferentially retain positive findings.

Workspace: /home/nico/projects/research_projects/reversible_circuits
Owned experiment: experiments/20260922-sparse-boundary/
Model and reasoning: gpt-6-astra / ultra for coordinator and every worker.
Six total active contexts: one coordinator and five workers, no worker
delegation. The launcher requests five spawned slots. Record observed worker
startup separately from requested capacity; do not evade a lower deployment
limit with extra sessions. Use fresh contexts, fork_turns=none if supported.
Do not silently substitute model or effort.

# Authoritative Timing and Permissions

Read on entry and every continuation:

- experiments/20260922-sparse-boundary/tmux-run.json
- notes/sparse-boundary-run.log.sparse-boundary-20260922.cap-status.json

The user-systemd service enforces 3600 seconds for the entire run, including
descendants and shutdown. started_at, wrapup_at, graceful_shutdown_at and
hard_deadline_at in the sidecar are authoritative. Never reset them.
Give their absolute UTC values to every worker.

Schedule from SERVICE ACTIVATION, not the end of intake:

- 0-5 minutes: freeze targets, dispatch all five workers, first checkpoint.
- By 20 minutes: every role has a halfway checkpoint and a concrete lemma,
  proposed test, or rejected route. Coordinator checks for duplicated work.
- By 30 minutes: blind referee freezes its independent report.
- By 35 minutes: construction snapshots ready; begin cross-audit.
- 35-50 minutes: referee reconciliation, decisive exact tests, version repairs.
- At wrapup_at (50 minutes): no new construction or broad experiments.
- By 55 minutes: report, claim ledger, raw results and resume.md saved.
- Before graceful shutdown: finish proportionate verification and stop.

Write checkpoints at least every ten minutes and after major findings. Do not
wait for wrap-up to save work: the deadline can interrupt a reasoning call.
A fully audited substantive outcome may finish early. Completion of worker
reports alone is not a stopping condition. A missing proof at the cap stays
unfinished; do not mark the native goal complete or blocked merely for time.
No automatic restart, extension, extra coordinator, service, tmux process,
detached computation or remote asynchronous job is authorized. The time cap
is not a token or spending limit.

Run sandbox-only, workspace-write, approval_policy=never. Bubblewrap is fixed
on this host; do not inherit old workarounds or weaken sandboxing. No installs,
machine/config/permission changes, commits, pushes or interactive approvals.
Record unavailable tools as blockers and continue with available work.

# Frozen Model and Questions

Let T_N be all transpositions of S_N. Labels and positions are distinguished.
Compose (alpha beta)(x)=alpha(beta(x)), rightmost factor first. For N>=2:

```text
Omega(N,m) = {w in T_N^m : product(w)=id}.
U_(N,m) = Unif(Omega(N,m)).
P = N+m+2.
K = max{1<=v<=N : v^(2v) <= P^4}, fixed at the TOP-LEVEL input.
```

A nontrivial support component of size v and length ell has
ell=2v-2+2g with integer g>=0. An isolate is (v,ell)=(1,0).

- H0: each nontrivial component has g<=1 OR v<=K. Call its word set A.
- H1: each nontrivial component has v<=K. Call its word set B.
- Thus B is a subset of A, and both include small support of ANY genus.

The existing exact samplers output Unif(A) and Unif(B), respectively, in
expected polynomial bit time. Their exact global TV errors are
1-|A|/|Omega| and 1-|B|/|Omega|. Audit imported claims as they become
load-bearing; unchanged, hash-frozen code need not be reimplemented.

**T0, proposed extension:** one algorithm, expected bit time poly(N,m),
always outputting a length-m identity word, and one explicit eta negligible
in N such that

```text
sup_{even m>=0, m^4<=N^3} TV(Q_(N,m),U_(N,m)) <= eta(N).
For every fixed a>0, eta(N)<=N^(-a) for all sufficiently large N.
```

The algorithm and polynomial exponent must not change for each a. State all
finite thresholds and parameters. Neither o(1) nor a fixed inverse power is
negligible. Complexity is in N and m, not log_2(N) wires.

**P0:** Does unchanged H0 establish T0? **P1:** Does unchanged H1 do so?
Track these separately from existence of another algorithm. A diagnostic
sequence is m_*(N)=max{even m>=0 : m^4<=N^3}; use integer tests, not floating
rounding. A rigorous non-negligible H0 error along an explicit sequence in
this range refutes P0. A bound tending to one is stronger. A vacuous UPPER
bound, a finite bad example, or failure of H1 does not refute P0.

Version any new cutoff, component policy or sampler; never silently enlarge
the H0/H1 allowed sets. Version weaker/stronger length results T1, T2, etc.
If T0 remains open, a proof for m <= c N^(2/3)(log N)^beta with fixed beta>0
would be useful; first check what already follows from the old finite tail,
and label an algebraic corollary honestly rather than a new mechanism.
Check m=0, m=2, odd m, N=1, N=2, zero-count branches and near-minimal words.

# Intake and Existing Evidence

This user-approved sampling objective supersedes the local-mixing objective
still in AGENTS.md and GOAL_SPEC.md, not their safety/proof standards.
HANDOFF.md and the manuscript predate the newest sparse results. Record this
disagreement; do not restart an old local-chain task or alter those files.

Coordinator and nonblind workers read selectively, then dispatch promptly:

1. AGENTS.md, HANDOFF.md, GOAL_SPEC.md; project skill SKILL.md and references
   sampling-problem.md and experiments.md.
2. /home/nico/.codex/skills/mathematical-proof-audit/SKILL.md and references
   audit-protocol.md and probability-regressions.md.
3. experiments/20260922-sparse-global-sampler/proof.md,
   coordinator_report.md, resume.md, regression_registry.md and final ledger.
4. experiments/20260905-bridge-length-phase-diagram/roles/r3-intermediate-hybrid/report.md
   (in particular the embedded-subgroup lower bound and named-method failure).
5. experiments/20260907-genus-one-sampler/global_consequence.md and proof.md
   only for dependencies used in a new argument.

The September 22 internally audited result covers m^3<=N^2 with one negligible
error function, expected O(P^20) bit time and O(P^10) storage. Same-model
acceptance is correlated internal review, not human certification. Preserve
old files and audit version hashes. No novelty-priority claim is inherited.

Useful starting points, all to be checked in their exact scope:

- The old maximum-component estimate contains a factor exp(O(m^3/N^2)).
  This makes the current upper bound ineffective beyond its range, but does
  not show that the actual sampler fails.
- Its genus sum was extended past the finite constraint g<=m/2-v+1, and a
  component-dependent exponent was replaced by a worst-case one. Retaining
  these constraints, or sharpening the exact conditioning ratio, is one
  constructive route. Do not assume it succeeds.
- The old minimal-only obstruction uses the exact lower bound
  Z(N,m)>=2*binom(r,2)^m/r! for positive even m and 2<=r<=N, then a choice
  r near m/log m. Check and reuse rather than rediscover it. It refutes
  minimal-only sampling above exponent 2/3, NOT H0 or H1 automatically.
- The September 7 genus<=1-only obstruction at m=2N is also not an H0
  obstruction. H0 additionally admits arbitrary genus on small support.
- A count recurrence need not furnish a sampler of literal words. Any new
  decoder must provide the actual conditional choices and bit complexity.

Read-only executable inputs (hash before import, Python -B):

- experiments/20260922-sparse-global-sampler/roles/r3-sampler/sampler-v4.py
- experiments/20260922-sparse-global-sampler/sample.py
- experiments/20260922-sparse-global-sampler/roles/r4-diagnostics/
- experiments/20260907-genus-one-sampler/roles/r1-recursive/sampler.py
- experiments/20260905-bridge-length-phase-diagram/roles/r3-intermediate-hybrid/component_audit.py

Primary-source leads, only for named obligations:

- Dubrovin-Yang-Zagier, Proposition 1 Eq(13), Eqs(19)-(20):
  https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf
- Vakil fixed-endpoint genus-zero/one formulas:
  https://math.stanford.edu/~vakil/files/g01hurwitz.pdf
- Chapuy-Louf-Walsh: https://arxiv.org/pdf/2206.11315
  Check the exact length regime and quantitative error; linear-length results
  do not automatically imply sublinear statements or negligible tails.

No broad literature survey, larger mixing grids or infrastructure work.

# Five Workers Plus Coordinator

All workers own only their role directory under the new experiment. Save
their full assignments, IDs/settings, inputs, checkpoints and final reports.
No worker edits another role, old experiment, shared root artifact, HANDOFF,
manuscript, AGENTS, GOAL_SPEC or skills. Only coordinator synthesizes here.

1. roles/r1-upper/: seek the strongest valid H0/H1 omitted-mass upper bound.
   Retain finite-length constraints and examine the exact bridge-conditioned
   normalization. Determine the immediate range of the old finite bound,
   then seek a genuine extension. State the first unproved inequality.
2. roles/r2-obstruction/: try to prove P0 false on m_*(N), or a larger
   explicit range. Use exact included/total count comparisons, preserving
   arbitrary genus on small supports. Distinguish P0 from P1 and from all
   samplers. A precise quantified lower bound, not pessimistic plots.
3. roles/r3-diagnostics/: reuse exact counting to compute Z_A/Z and Z_B/Z
   at small, deliberately chosen boundary cases. Independently test the
   provers' inequalities and classify missing components. Start cheap and
   increase only after a timed pilot. No mass-ratio extrapolation as proof.
4. roles/r4-construction/: investigate ONE targeted sampler modification
   for a plausible excluded component family. Specify exact law, positive
   decoding and polynomial bit cost. If no new construction is viable in
   time, produce a reduction isolating the exact missing connected primitive,
   and audit the final proposed positive theorem's algorithmic dependencies.
5. roles/r5-referee/: start ONLY from notes/sparse-boundary-blind-brief.md
   plus operational deadlines and safety instructions, in a fresh context.
   Do not send this full prompt, other proofs, prior verdicts or suspected
   failure. Freeze blind_report.md by elapsed 30 minutes, then audit the
   strongest current-version positive or negative claim as a nonauthor.
   Preserve complete inputs; disclose any actual isolation limitations.

The coordinator manages the claim graph, reconciles contradictions, preserves
negative/minority findings, reruns decisive tests and checks final delivery.
Close finished threads before recycling slots for fresh reviews. Do not
invent unrelated work merely to fill all slots. Do not describe repeated
same-model review as statistically independent confirmation.

# Experiment and Audit Discipline

Use supervised computations, initially timeout 90s, at most two expensive
checks at once. Prefer exact Python standard-library arithmetic. Larger
computations need a named decision they can resolve and time left to inspect
the output; do not leave sessions running at a report boundary. Fixed seeds
1729,2718,31415 for any stochastic diagnostics; proofs use exact laws.

Test changed sampler logic on S3,m4 and S4,m4, plus S4,m6 when feasible.
Record literal identity, length, exact per-word law when affordable, support
components, edge counts and relevant conditional quantities. Deterministic
exact tests can refute inequalities but do not establish asymptotic tails.

For every mathematical statement record status, assumptions, dependencies,
source/version, finite falsification and the first unproved step. Use exact
conditioning laws; no random-graph independence or unproved marginal products.
Do not evaluate divergent generating series. A repaired lemma reopens all
downstream claims and needs a fresh nonauthor audit of the exact new version.
Retain old counterexamples, including fixed-cutoff recursion, CLI large-int
serialization, ambiguous policy labels, and support-history omissions.

# Deliverables and Completion Gate

All research writes go in experiments/20260922-sparse-boundary/. Create:

- plan.md, run_manifest.md, initial_git_status.txt, source/dependency hashes;
- checkpoint.md and append-only claim_ledger.md with T0, P0, P1 separate;
- per-role plan/checkpoint/report, proof or obstruction, scripts and raw JSON;
- proof.md or obstruction.md for stable results, never a polished false claim;
- coordinator_report.md with a short high-level explanation and parameter map;
- regression_registry.md, resume.md, changed_files.txt and artifact manifest.

Coordinator report names the candidate, exact target, identity validity,
global support coverage, exact checks, asymptotic status and verdict. Give
reproduction commands, repository commit, Python/dependency versions, seeds,
timings, tested domains and known limitations. Inventory every attributable
changed file separately from pre-existing untracked work and launcher files.
Do not edit/commit/push old research or the manuscript during this run.

Complete the native goal early ONLY for an audited new extension theorem or
an audited asymptotic H0 obstruction with all load-bearing claims closed,
decisive tests passed and final artifacts saved. A separately stated smaller
extension can complete that branch of this disjunctive goal, but T0's status
must remain explicit. H1 failure alone or a named missing inequality is
partial progress; continue useful work until wrap-up, then leave the goal
unfinished if neither terminal branch was established. Do not manufacture
an answer to fit the cap. Report native goal usage only as actually returned.
