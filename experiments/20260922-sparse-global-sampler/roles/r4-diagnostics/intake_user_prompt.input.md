/goal
Launch no additional process yourself: you ARE the new user-authorized
coordinator for the four-hour, six-context Astra Ultra goal run below.
Read the cap sidecar immediately. Create one native goal for the research
objective below if that tool is available, without a token budget. Workers
must not create goals. This run is not a resume of the local mixing program.

# Objective and Scope

Establish and adversarially audit a new GLOBAL sampling theorem for moderately
short transposition identity bridges. The benchmark is every even m with
m^5 <= N^3, expected bit time polynomial in N,m, and a single explicit error
bound negligible in N uniformly over that length range. Build and test the
component-based candidate below. If the benchmark cannot be established,
prove a genuinely new smaller regime or a precise obstruction to the named
candidate, and isolate the first remaining mathematical obligation.

This is a research target, NOT an inherited theorem. Scalar counts, plots,
per-instance mass certificates, and finishing reports do not by themselves
establish the asymptotic goal. Failure of the candidate is not sampling
hardness. Any exact or statistically close-to-uniform polynomial algorithm
is acceptable; no Hurwitz or heat-bath mixing theorem is required.

The current user objective supersedes the old local-chain objective in
AGENTS.md and GOAL_SPEC.md. Their safety, experiment and proof standards
remain in force. HANDOFF.md's dense-only summary predates the September 5
and September 7 results. Record conflicts; do not silently choose convenient
claims. Prior agent acceptance remains internal evidence, not external human
certification. Verify inherited inputs when they become load-bearing.

Workspace: /home/nico/projects/research_projects/reversible_circuits
Owned experiment: experiments/20260922-sparse-global-sampler/
Coordinator and all workers: model gpt-6-astra, reasoning effort ultra.
User-authorized team: SIX active contexts total, coordinator plus five
workers. The launcher requests agents.enabled=true and a per-session spawned
thread ceiling of five. Check reported slots and actual worker startup;
configured capacity is not proof of effective capacity. Record a mismatch,
work locally while slots are occupied, and recycle completed threads. Never
evade a deployment limit by launching another Codex process or session.
Workers must not delegate. Do not silently substitute a model or effort.

# Enforced Four-Hour Envelope

On entry and every continuation read:

- experiments/20260922-sparse-global-sampler/tmux-run.json
- notes/sparse-global-sampler-run.log.sparse-global-sampler-20260922.cap-status.json

The external user-systemd service enforces 14400 seconds for the whole run,
including local descendants and shutdown. Its activation starts the clock,
not the end of intake. The sidecar's started_at, wrapup_at,
graceful_shutdown_at and hard_deadline_at are authoritative. Send absolute
deadlines to each worker. Wrap-up starts 1800 seconds before the deadline.

Wrap-up metadata does not inject a model message. Check the clock yourself.
Write a first checkpoint within 20 minutes, then at least every 15 minutes
while active and after major results. Stop starting new construction at
wrapup_at. Save reports, raw partial results and a self-contained resume.md
at least five minutes before hard_deadline_at. External shutdown can occur
while a model is reasoning, so checkpointing cannot wait for a final answer.

No cap reset, extra coordinator, external service, detached computation,
remote asynchronous job, automatic restart or extension is authorized.
Keep local computations as supervised descendants with individual timeouts.
Do not alter launcher files, cap metadata, system configuration or permissions.
The runtime cap is not a hard token/spending budget or a guarantee of instant
cancellation of already accepted remote requests.

If the cap ends unresolved work, preserve a time-limited checkpoint and
leave the native goal unfinished. Do not mark it complete or blocked merely
because time ran out; process termination does not pause native goal state.
An actually audited completed objective can finish early, but one finished
worker or a collection of reports is not a mathematical stopping criterion.

# Frozen Goal T0

Let T_N be all transpositions of S_N. Labels and positions are distinguished.
Products compose as (alpha beta)(x)=alpha(beta(x)), rightmost factor first.

```text
Omega(N,m) = { w in T_N^m : product(w)=id }.
U_(N,m) = Unif(Omega(N,m)).
```

For N>=2 and every even m>=0 with m^5<=N^3, seek one uniform algorithm
returning a word in Omega(N,m) exactly, in expected bit time poly(N,m), with

```text
sup_{even 0<=m, m^5<=N^3} TV(Q_(N,m),U_(N,m)) <= eta(N),
for every fixed a>0, eta(N) <= N^(-a) for all sufficiently large N.
```

Supply an explicit effective bound, constants and exceptional small cases.
The same algorithm and polynomial runtime bound must work throughout the
declared range; do not change the algorithm separately for each exponent a.
An illustrative stronger sufficient tail is exp(-c log(N)^2/loglog(N)) for
large N and fixed c>0, but this shape is not assumed. Proving only o(1), a
fixed inverse power, or fixed-accuracy convergence must be labeled weaker.
No tunable poly(log(1/epsilon)) guarantee at fixed (N,m) is assumed.
Complexity is in permutation degree N, not the wire count log_2 N.

The exponent 3/5 is a benchmark, not a sharp threshold. A stretch target is
m<=N^(2/3-delta) for fixed 0<delta<2/3 with explicit dependence on delta.
Version any changed theorem as T1, T2, etc.; preserve T0 and report whether
it was achieved. A refuted tail estimate need not refute existence of any
sampler in T0's range. Treat N=1, m=0, m=2, odd m and N=2 separately.

# Candidate H0: Exact Restricted Assembly Plus an Omitted-Mass Bound

A nontrivial connected support component on v vertices with ell factors
has ell=2v-2+2g for an integer g>=0. Here g is just the number of extra
pairs beyond the minimum. Isolated vertices have v=1,ell=0 separately.

Define an integer work cutoff once from the TOP-LEVEL (N,m):

```text
K(N,m) = max{v in {1,...,N}: v^(2v) <= (N+m+2)^4}.
Allowed(v,ell) iff (v=1 and ell=0), or, for feasible v>=2,
                   [g in {0,1} OR v<=K(N,m)].
A(N,m) = {w in Omega(N,m): every component is Allowed}.
```

Keep this cutoff fixed during the whole component recursion; recomputing it
on a remaining-label subproblem changes the declared subset. The cutoff is
O(log(N+m)/loglog(N+m)); use exact integer comparisons, not floating logs,
and handle small N. A different fixed polynomial work budget may be tested
as a versioned candidate, with a revised complexity proof and mass bound.

Use these three primitives, checking precise hypotheses:

1. Exact connected g=0/1 generation from the September 7 construction.
2. For v<=K, exact connected generation at any feasible ell using DP on
   (current permutation, exposed support partition, remaining length).
   Its v! Bell(v) state factor is <=v^(2v), hence polynomial under this
   cutoff, with polynomial ell and integer-bit costs still to account for.
   The old Python routine is recursively coded: use iteration/explicit
   stacks for unbounded ell rather than raising interpreter limits.
3. The positive exact component-count and least-label assembly recurrence,
   uniform label choice and uniform position interleaving. This targets
   Unif(A(N,m)), not an unweighted graph law or a random Hurwitz orbit.

For exact restricted sampling and positive Z_A=|A|, the error is exactly

```text
TV(Unif(A),Unif(Omega)) = 1 - Z_A(N,m)/Z(N,m).
```

Exact polynomial counting of Z_A and Z supplies a per-instance certificate.
The NEW core lemma is that this omitted mass is negligible uniformly in
T0's range. Do not assume it. A union bound on expected numbers of excluded
components is one route, but any marked-component identity must be derived
with its label and interleaving multiplicities and endpoint conditioning.
The problematic components have BOTH v>K and g>=2; small components may
have arbitrarily high genus and are INCLUDED. Do not substitute the old
g<=1-only obstruction for an obstruction to H0.

If finite certificates suggest a poor cutoff or a hidden component class,
investigate that cause. Permit a focused alternate construction that fixes
the named issue, but do not drift into general all-genus sampling or local
mixing without a direct reduction to this run's target.

# Intake: Reuse the Completed Runs

Coordinator reads the following selectively, dispatching workers promptly:

1. AGENTS.md; HANDOFF.md (context and rank-recursive direction); GOAL_SPEC.md
   for standards rather than its superseded local-chain objective.
2. .codex/skills/reversible-circuit-sampler/SKILL.md and its references
   sampling-problem.md and experiments.md.
3. /home/nico/.codex/skills/mathematical-proof-audit/SKILL.md and its
   references audit-protocol.md and probability-regressions.md.
4. experiments/20260907-genus-one-sampler/resume.md, proof.md,
   coordinator_report.md, global_consequence.md, regression_registry.md,
   and accepted claim-ledger rows. Follow exact audit versions as needed.
5. experiments/20260905-bridge-length-phase-diagram/phase_diagram.md and
   roles/r3-intermediate-hybrid/report.md, especially sparse bounds,
   the named-method obstruction, support-marked DP and hybrid certificate.

Useful existing code, read-only and hash before importing:

- experiments/20260907-genus-one-sampler/roles/r1-recursive/sampler.py
- experiments/20260907-genus-one-sampler/sample.py and global_mass.py
- experiments/20260905-bridge-length-phase-diagram/roles/r3-intermediate-hybrid/component_audit.py

Do not read enormous old logs/ledgers wholesale. Follow only dependencies
needed by a named obligation. Retain historical counterexamples. Important
boundaries already known internally:

- The previous explicit minimal-only sparse bound is
  min(1,m^4/[48(N-m+1)^2]), for even m<=N; it is not a negligible-error
  theorem through sqrt(N).
- Minimal-only assembly fails for fixed power lengths N^alpha with alpha>2/3.
  This is a named-method result, not a sharp threshold or hardness theorem.
- Genus<=1-only assembly loses almost all mass at m=2N. It does not include
  the arbitrary-genus small components now proposed in H0.
- Uniformly sampling graphs, blindly inserting squares, scalar counts
  without a word decoder, and ignoring prefix support connectivity can fail.

Targeted primary-source leads (verify hypotheses/conventions before use):

- Dubrovin, Yang, Zagier, Classical Hurwitz numbers, Proposition 1 Eq(13),
  Section 1.2 Eqs(19)-(20):
  https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf
- Vakil, Genus 0 and 1 Hurwitz numbers, Section 1.2 and Corollary 1.5:
  https://math.stanford.edu/~vakil/files/g01hurwitz.pdf
- Chapuy, Louf, Walsh, Random partitions under the Plancherel-Hurwitz
  measure: https://arxiv.org/pdf/2206.11315
  Its linear-length asymptotics and component results are boundary checks,
  not an automatic sublinear or negligible-tail theorem. Respect the
  separate parameter assumptions of each theorem, including theta>1 in
  the stated giant-edge-component result.
- DPS minimal sampler: https://www.irif.fr/~poulalho/Articles/DuPoSc13.pdf

Literature work must discharge a named count/tail/sampling obligation.
If the target already follows from a published result, adapt and audit it
rather than inventing novelty. A theorem with only convergence in probability
does not supply negligible error without an additional quantitative bound.

# Five Worker Roles and Coordinator

Use fresh non-inherited contexts where supported, with task identifiers
r1_combinatorial, r2_analytic, r3_sampler, r4_diagnostics, r5_referee.
All use gpt-6-astra / ultra. Each worker owns only its role directory under
the new experiment. Save complete assignment inputs, IDs, observed settings,
absolute deadlines, checkpoints, code, raw results and final reports.

1. roles/r1-combinatorial/: derive a quantitative excluded-component bound
   from positive recurrences and labeled incidences. First identify the
   exact normalized probability being bounded. Aim for T0, exposing every
   factorial and conditioning cost. Produce proof or smallest failed lemma.
2. roles/r2-analytic/: independently seek a count estimate, generating
   function argument, or checked literature input for the SAME tail.
   Remain independent of R1's candidate initially. Do not import ordinary
   random-graph independence into the identity-conditioned word law.
   A rigorous counterexample to H0 or a sharper regime boundary is useful.
3. roles/r3-sampler/: implement H0 using existing exact primitives with
   correct top-level cutoff, explicit stacks, exact integer choices, and
   polynomial bit/storage accounting. Emit the exact omitted-mass
   certificate; never label uncertified restricted output as global uniform.
   Include a clean sampler API, small-case full-law tests and reproducible CLI.
4. roles/r4-diagnostics/: independently implement or cross-check the exact
   allowed-mass certificate and marked-component diagnostics. Separate large
   support, high genus, and long length effects. Test the proposed bound
   where it is nontrivial; distinguish K from a deliberately smaller test
   cutoff. Coordinate bounded parameter grids with the sampler author.
   Give concrete stress cases to the provers, never extrapolate finite
   curves to an asymptotic theorem. No empirical mixing diagnostics.
5. roles/r5-referee/: start from ONLY notes/sparse-global-sampler-blind-brief.md
   plus operational deadlines and repository safety instructions. Use
   fork_turns=none or equivalent if supported. Do not send this full prompt,
   candidate proofs, historical verdicts or coordinator confidence. Freeze
   a blind_report.md by elapsed 90 minutes, then review the strongest
   current-version proof and sampler as a nonauthor. If true context
   isolation is unavailable, record the limitation rather than claiming
   blindness. Preserve exact review inputs and objections.

Coordinator owns integration and shared experiment artifacts, checks
primitive dependencies, reconciles conflicting claims, and reruns the
smallest decisive tests. Do not invent five unrelated problems to fill slots.
Close completed workers before reusing slots for fresh audits. Workers never
delegate. Six requested contexts do not authorize extra external sessions.
Same-model agreement is correlated evidence, not independent certification.

# Schedule and Decision Gates

All times are elapsed from service activation, not prompt receipt:

- 0-30 minutes: freeze T0/H0, source normalization, launch five workers,
  record actual capacity and first checkpoint.
- 30-120 minutes: independent proof routes, sampler, finite certificates
  and blind analysis. At elapsed 60 minutes record which specific tail
  bound remains plausible, which inputs are checked and any candidate flaw.
- 120-210 minutes: concentrate effort on the strongest mathematical route,
  expose candidate to nonauthors, repair and freshly recheck it. A weaker
  theorem must retain its true quantifiers and be labeled separately.
- 210-240 minutes: no new construction; gather incomplete as well as
  completed reports, reconcile versions, verify artifacts, and save handoff.

Periodic checkpoints matter more than the nominal stage labels. If a proof
route is refuted, adapt within scope and the same deadline. Genus-two-only
sampling is not this run's standalone goal. Do not burn the cap on broad
literature review, polishing an unresolved proof, or rebuilding infrastructure.

# Verification, Resources and Proof Discipline

Use python3 -B and standard-library/existing dependencies. No installs,
sudo, escalations, machine changes, network mutations, commits or pushes.
Built-in web search is enabled for focused primary-source checks. Prefer
Python over Magma. Missing optional dependencies are recorded, not repaired
by relaxing the sandbox. Do not write caches into old experiments.

Use bounded local subprocesses, initially <=120 seconds per experiment,
and at most two heavy enumerations/count grids at once across the team.
Checkpoint partial grids before expanding. Larger justified checks must fit
inside the remaining verification and wrap-up budget. Do not execute a
huge N^2*m^2 sweep merely because its theoretical complexity is polynomial.

Test new shared logic at S_3,m=4; S_4,m=4; S_4,m=6, plus high-genus small
supports, a deliberately excluded component and cutoff boundary cases.
Reuse the genus-one S_3,m=6 and S_4,m=8 law tests where feasible. Verify
endpoint, support, length, per-word probabilities, interleavings, label
multiplicities, and equality of full-minus-allowed counts. Include N=1,
N=2, m=0, m=2, odd m and length beyond the supported theorem range.
Tiny cases where every word is allowed cannot validate a nonzero tail bound.

Record commit, initial dirty state, Python/dependency versions, commands,
seeds and complete tested domain. Separate deterministic exact checks from
seeded implementation diagnostics. Tests can refute a theorem but cannot
replace its uniform proof or establish negligible error from finite N.

Freeze claims by ID and version. Maintain dependencies and an append-only
ledger with statement, status, assumptions, evidence, reviewer/version,
regressions and action. Use proved/conditional/empirical/conjectured/refuted/
unresolved labels, plus provisional/repaired-pending-recheck audit states.
Every repair reopens downstream claims and requires a fresh nonauthor check.
Retain negative findings and disagreement, including minority reports.

For probabilistic lemmas state exact laws, conditional histories, support,
normalizers and zero branches. No multiplication of marginal bounds or
unjustified use of independent-edge random graph results. Check finite
counterexamples with exact rational arithmetic. Use the proof-audit skill's
cached-prefix regression if a sequential-independence argument makes it
relevant. Do not add unrelated audit exercises mechanically.

# Deliverables, Ownership and Stopping

Coordinator-owned experiment files:

- plan.md, run_manifest.md, checkpoint.md (update throughout)
- claim_ledger.md, regression_registry.md
- proof.md or obstruction.md with the first open lemma if any
- coordinator_report.md, including T0 status and the exact proved regime
- resume.md with exact session ID, reviewed versions and next actions
- changed_files.txt and a compact artifact/provenance manifest

Workers provide plan, checkpoints, final report, proofs/code and machine-
readable results under their role directories. The referee preserves the
blind brief/report and complete subsequent review inputs. Final report
must distinguish: mathematical novelty, imported result, implementation,
exact finite certificate, and empirical observation.

Classification: global-negligible-sampler, weaker-new-global-theorem,
checked-candidate-obstruction, or time-limited-unresolved. Supply the exact
statement supporting the classification. A polynomial sampler conditional
on A, without a new uniform mass estimate, is useful infrastructure but
does not satisfy T0. A named-method failure is not global impossibility.
Do not mark a native goal complete just because deliverable files exist.
Report recorded token/time usage on genuine completion without inventing
an allocation. At a cap, preserve unresolved status and do not auto-resume.

Only write research outputs inside experiments/20260922-sparse-global-sampler/.
AGENTS.md, GOAL_SPEC.md, HANDOFF.md, the manuscript, skills, old experiments,
launch prompts/runbook, runner scripts and all unrelated files are read-only.
The September 7 untracked artifacts are pre-existing user work: preserve
them and exclude them from this run's change attribution. Only the launcher
maintains the tmux/cap sidecars and transcript. End with git status and a
precise inventory of attributable changes. No commits or pushes.
