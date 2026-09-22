/goal
Run the user-authorized four-hour, four-context Astra Ultra research effort
below. This is a NEW capped goal run, not a continuation of the old local
mixing program. Read the external cap status immediately. Create one native
goal for this objective if the goal tool is available; omit token_budget.
Only the coordinator creates a goal. Do not launch another Codex process.

# Objective and Authority

Construct and adversarially audit a polynomial-time uniform sampler for
connected transposition identity words on [N] of length 2N. Determine the
consequence for the existing global component-assembly sampler. If the
construction remains unresolved, produce a materially narrower, proved
reduction or a checked obstruction to a named construction, with an exact
statement of the first remaining lemma. Do not equate failing to find a
sampler with computational hardness.

The user accepts ANY polynomial-time statistically close-to-uniform sampler.
Hurwitz or heat-bath mixing is not the objective. The older local-chain
objective in GOAL_SPEC.md and AGENTS.md is superseded for this run; their
safety, proof, experiment, and coordination standards continue to apply.
The September 5 reports are newer research inputs than the dense-only
summary in HANDOFF.md. Record any conflict rather than silently changing a
theorem. All inherited project proofs remain subject to verification when
they become load-bearing; prior agent acceptance is not external certification.

Workspace: /home/nico/projects/research_projects/reversible_circuits
Owned experiment: experiments/20260907-genus-one-sampler/
Model for coordinator and workers: gpt-6-astra
Reasoning effort: ultra (do not substitute max)
Maximum simultaneously active agent contexts: FOUR TOTAL, coordinator plus
three workers. Workers do not spawn agents. Recycle completed slots for fresh
reviews, never exceed the ceiling, and do not change machine configuration.

# External Deadline Contract

Read these exact files on entry and at every continuation:

- experiments/20260907-genus-one-sampler/tmux-run.json
- notes/genus-one-sampler-run.log.genus-one-sampler-20260907.cap-status.json

The user-systemd service enforces a 14400-second whole-run envelope, including
local descendants and shutdown, with a 1800-second wrap-up reserve. The
service activation time, NOT when you finish reading, starts the clock.
Use its started_at, wrapup_at, graceful_shutdown_at and hard_deadline_at as
authoritative. Pass the absolute deadlines to every worker.

The wrap-up time is metadata, not an injected message. Check time proactively.
Write an initial checkpoint within 20 minutes and update it after each major
result or at least every 15 minutes while active. By wrapup_at stop new
construction work and gather reports. Save the self-contained handoff at
least five minutes before hard_deadline_at. The service may terminate a busy
model without a final message, so durable partial outputs are mandatory.

Do not reset the clock, alter the cap or its sidecars, start another service,
tmux session, coordinator, or detached work outside this capped scope. No
automatic restart or continuation is authorized. No remote asynchronous
compute jobs. Run local computations as supervised descendants with bounded
individual runtimes. The cap is not a token budget or guaranteed immediate
cancellation of a request already accepted remotely.

At a timeout, record time-limited-unresolved if work remains. Do not mark a
native goal complete or blocked just because time is running out; termination
does not pause native goal state. Preserve the exact session ID for a later
user-authorized resume. An actually completed, audited objective may finish
early, but completion of a worker report or one review wave is not sufficient.

# Frozen Target T0

Let T_N be all transpositions in S_N, and define

```text
X_N = { (t_1,...,t_(2N)) in T_N^(2N) :
        t_1 ... t_(2N) = id,
        support graph is connected on all N labeled vertices }.
```

Support means the graph with an edge for each transposition used; connected
does NOT mean every transposition appears. Labels and word positions are
distinguished. Permutations compose as (a b)(x)=a(b(x)); rightmost acts first.

Desired output for every N>=2 and positive integer b: a word in X_N exactly,
whose law is at total-variation distance at most 2^(-b) from Unif(X_N), in
expected bit time poly(N,b). Exact uniform sampling in expected poly(N) time
is stronger and welcome. Prove precision, integer bit lengths, branch costs,
and any rejection acceptance bound; N-dependent enumeration is not polynomial
merely because the surplus is fixed. N=2 is a singleton; N=1 is infeasible.

Connected identity words have length 2v-2+2g for g>=0. The target is g=1,
two swaps beyond the minimal g=0 length. Internal connected endpoints sigma
may be generalized to length v+cycles(sigma)-2+2g, with g in {0,1}, if that
makes recursion tractable. Distinguish these from unconstrained endpoint
bridges and from prefixes whose eventual support connectivity is prescribed.

The public global target remains Unif(Omega(N,m)), with unrestricted support.
Even a complete solution for X_N is not a global sampler for m=2N. A global
claim must include exact component-selection/interleaving weights and the
probability of component types that the algorithm excludes.

# Intake and Reusable Inputs

Coordinator: read these before construction, with targeted reading rather
than entire historical logs. Dispatch workers promptly after the target and
deadlines are frozen; do not spend the first hour on intake.

1. AGENTS.md; HANDOFF.md (context and rank-recursive section); GOAL_SPEC.md
   for standards, not its obsolete-for-this-run objective.
2. .codex/skills/reversible-circuit-sampler/SKILL.md and its references
   sampling-problem.md and experiments.md.
3. /home/nico/.codex/skills/mathematical-proof-audit/SKILL.md and references
   audit-protocol.md and probability-regressions.md.
4. experiments/20260905-bridge-length-phase-diagram/phase_diagram.md,
   coordinator_report.md, claim_ledger.md, and
   roles/r3-intermediate-hybrid/report.md, especially its missing primitive.
5. experiments/20260811-polynomial-mixing-resolution/cycle-19/
   mission-M97-genus-one-hurwitz-gap/report.md, especially Sections 3-7.
6. As needed, cycle-23/mission-M112-minimal-genus-zero-gap/report.md and
   cycle-24/mission-M119-m112-fresh-referee/report.md under the same historical
   experiment, for the minimal sampler and its source audit.

Read the relevant manuscript section rank_recursive_sampler.tex only if using
the dense sampler. Follow any missing dependency to its exact historical
artifact. Do not load the full old resolution ledger or rerun old mixing
diagnostics. Preserve every relevant historical failure as a regression.

Current useful inputs (verify the precise version before use):

- Exact polynomial scalar counts C(v,k) for connected identity words and
  Z(N,m) for all identity words, using the positive DYZ recurrence.
- Exact component assembly with weight
  m! product_B C(|B|,ell_B)/ell_B!, and uniform position interleaving.
- Exact minimal connected sampling via the DPS construction.
- An everywhere-defined genus-one cut into componentwise genus-zero pieces
  in M97. The uniform-word lift weights a valid cut j by 1/|J(w)|.
- Literal adjacent-square insertion has zero fibers on some genus-one words.
  In particular (a b)^3 for intersecting transpositions a,b is a connected
  identity word on three vertices with no adjacent square. Tree extensions
  and the M92/M95 dependencies are recorded in M97.
- General fixed-genus sampling was NOT solved by the September 5 run.

Primary-source leads, not automatically accepted sampler theorems:

- Ravi Vakil, Genus 0 and 1 Hurwitz Numbers, Corollary 1.5 and conventions
  Section 1.2: https://math.stanford.edu/~vakil/files/g01hurwitz.pdf
  Gives arbitrary-endpoint transitive counts in genera zero and one.
  Check conversion from weighted covers to labeled words. Section 4.1
  discusses removing the last transposition. A count formula is not itself
  a completion oracle with exposed-support constraints.
- Duchi, Poulalhon, Schaeffer, Uniform random sampling of simple branched
  coverings: https://www.irif.fr/~poulalho/Articles/DuPoSc13.pdf
- Their higher-genus bijection: https://arxiv.org/pdf/1410.6521, Theorem 4.
  Sampling coherent mobiles remains an obligation; a bijection alone does
  not prove a polynomial algorithm.
- Dubrovin, Yang, Zagier, Proposition 1 equation (13):
  https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf
- https://arxiv.org/abs/2105.03284 treats a long-cycle endpoint, not identity;
  do not import its asymptotic sampler as the target theorem.

Allow targeted new literature searches for a named missing lemma, with exact
sources and conventions. If a published solution is located, verify and
adapt it, then spend remaining time on the global consequence and audit;
do not seek novelty by ignoring prior work.

# Roles

Use identifiers r1_recursive, r2_structural, r3_referee (underscores avoid
the naming error of the prior run). Store exact assignment prompts, agent
IDs, settings, deadlines, and complete reports. Worker-owned directories:

1. roles/r1-recursive/: one count-guided recursive sampler candidate.
   Use arbitrary-endpoint g=0/1 formulas with a word-level decomposition,
   such as deletion of the final swap. Prove branching probabilities,
   connectivity handling, and reconstruction multiplicities. Investigate
   positive dynamic programming to aggregate choices of cycle subsets;
   explicitly reject an exponential listing masquerading as a polynomial
   recursion. Produce an algorithm or a precise completion-count obstacle.
2. roles/r2-structural/: one sampler based on the M97 cut into simpler
   pieces, or an explicitly justified structural replacement. Show how to
   sample the decorated objects and forget decorations without bias. Track
   coverage, 1/|J(w)| corrections, and rejection cost. The published mobile
   representation is a backup if it resolves a named obstruction.
3. roles/r3-referee/: blind construction/falsification first, then exact
   tests and candidate audit. Use a fresh context without inherited
   coordinator history if supported. Initial input is ONLY the separate
   notes/genus-one-sampler-blind-brief.md plus operational deadlines,
   sandbox/ownership rules and required repo safety instructions. Do not
   pass this full prompt, candidate arguments, old verdicts, or coordinator
   confidence. Ask the referee not to inspect other roles or old reports
   until its blind report is frozen. If context isolation is unavailable,
   document the limitation and do not claim a blind review.

Workers must not recursively delegate, commit, push, install dependencies,
request approvals, edit shared project files, or modify another role's files.
When a role finishes, preserve its complete report and close it before
reusing a slot. Same-model agreement is not statistically independent evidence.

The coordinator owns integration, the claim graph, tests across candidates,
and the global consequence. Compute, using the existing positive count and
assembly code, the exact mass Z_(g<=1)/Z of words whose every connected
component has genus at most one. This is a certificate about an algorithm's
covered subset, not an asymptotic theorem inferred from a plot. If component
samplers are approximate, allocate at most epsilon/(2N) to each component
and pay the omitted mass explicitly. An asymptotic improvement of the global
length/accuracy range is a stretch target, not a prerequisite to recognizing
a valid connected sampler theorem.

# Time Allocation and Decision Gates

Times below are elapsed from the cap's service activation:

- 0-30 minutes: target T0, dependency intake, source normalization, three
  worker assignments, and first durable checkpoint.
- 30-120 minutes: two constructive routes and blind referee work. Each role
  writes a halfway checkpoint and a concrete algorithm or missing lemma.
- 120-180 minutes: select the strongest route, expose the frozen candidate
  proof to a nonauthor after its blind report is saved, run exact checks,
  repair failures, and compute global consequences.
- 180-210 minutes: final verification, complexity and normalization audit,
  and fresh recheck of repairs. Do not promote unchecked late discoveries.
- 210-240 minutes: synthesis only; stop new work, gather even incomplete
  worker reports, save a resumable handoff before the shutdown margin.

Adapt allocations to evidence within the same deadline. Do not spend all
remaining time polishing a failed idea. Continue useful in-scope work after
a rejected attempt or completed worker, but do not invent infrastructure or
unrelated conjectures to consume the full allowance.

# Proof and Experiment Gates

Freeze claims with IDs and versions. Ledger columns:

```text
claim | status | assumptions/dependencies | evidence | reviewer/version |
regressions | action
```

Use project labels proved, conditional, empirical, conjectured, refuted,
unresolved; distinguish provisional and repaired-pending-recheck proof status
in the audit ledger. A changed dependency reopens downstream claims. Keep
rejected arguments and minimal witnesses. Every nontrivial probabilistic
step needs its exact conditional law, normalization, and support, with a
finite-support falsification attempt where possible. Never multiply marginal
error bounds without a valid conditional or coupling argument. Apply the
audit skill's cached-prefix regression when sequential-independence claims
are relevant, not as unrelated busywork.

Use existing Python permutation helpers and exact rational tests. For new
genus-one logic, check N=2,length=4; N=3,length=6; N=4,length=8 if feasible.
Archive M97 gives respectively 1, 240, 131040 connected words as cross-checks,
not as a replacement for independent validation. Also run relevant shared
logic regressions S_3,m=4; S_4,m=4; S_4,m=6. State infeasible branches and
ordinary m=0, odd m, m=2 boundaries. Check full small-case word probabilities
or reconstruction multiplicities, not only marginal histograms.

Record commands, seeds, tested domain, bit-complexity model, Python and
dependency versions, repository commit and initial dirty state. Nontrivial
experiments need plan, reproducible scripts, machine-readable raw results,
and a report verdict. Bound exhaustive work; do not enumerate large word
spaces or run broad S_10 diagnostics. No package installation is authorized.

# Durable Deliverables and Stopping

Only the coordinator writes these top-level experiment artifacts:

- plan.md and run_manifest.md (actual model, effort, agent IDs and deadlines)
- checkpoint.md, updated throughout with explicit next actions
- claim_ledger.md and regression_registry.md
- proof.md for the precise strongest claim, or obstruction.md if no proof
- coordinator_report.md, including disagreements and the global implication
- resume.md with exact session ID, source files, open claims, and next steps

Workers write their own plan, checkpoint, report, proofs/code, raw results,
and review inputs under their role directory. Preserve full audit reports.

The main success is an audited polytime sampler theorem for all N in X_N,
including a correct implementation/pseudocode and expected bit-time bound.
A valuable partial result must discharge a named mathematical obligation or
refute a specific construction with a checked witness; merely renaming the
open problem or computing more scalar counts is not progress.

Final classification: sampler-theorem, strict-constructive-reduction,
checked-method-obstruction, or time-limited-unresolved. A method obstruction
does not refute existence of a sampler. If the native goal's actual objective
remains unfinished at the time cap, leave it unfinished regardless of the
report classification. Do not turn artifact completion into theorem completion.

Do not modify AGENTS.md, GOAL_SPEC.md, HANDOFF.md, the manuscript, skills,
old experiments, launcher code, system configuration, or unrelated files.
Keep all research edits in the new experiment directory; the launch prompt
and runbook are inputs, not editable coordinator outputs. No commits or
pushes. End with git status and an exact list of changes attributable to
this run. Preserve existing user work and unrelated running services.
