/goal
Resolve the polynomial-mixing question for the exact local transposition
identity-bridge heat-bath chain. Remain active until one of the two terminal
outcomes below survives full refereeing. Do not stop after decisive partial
progress.

# Authority and read order

Work in /home/nico/projects/research_projects/reversible_circuits.

Before dispatching research, read these durable sources in order:

1. AGENTS.md
2. GOAL_SPEC.md
3. HANDOFF.md
4. .codex/skills/reversible-circuit-sampler/SKILL.md
5. .codex/skills/reversible-circuit-sampler/references/sampling-problem.md
6. .codex/skills/reversible-circuit-sampler/references/experiments.md
7. papers/transposition_identity_samplers/sections/theoretical_status.tex
8. papers/transposition_identity_samplers/sections/graph_theoretic_interpretation.tex
9. papers/transposition_identity_samplers/sections/conditional_block_sampling.tex
10. papers/transposition_identity_samplers/sections/hurwitz_obstruction.tex
11. papers/transposition_identity_samplers/sections/finite_spectral_evidence.tex
12. papers/transposition_identity_samplers/sections/scalable_diagnostics.tex
13. papers/transposition_identity_samplers/sections/square_refresh.tex
14. papers/transposition_identity_samplers/sections/expander_gate_sets.tex
15. papers/transposition_identity_samplers/sections/next_steps.tex
16. papers/transposition_identity_samplers/sections/internal_sources.tex
17. experiments/INDEX.md and the reports it indexes
18. Literature/0110110v1.pdf, especially Theorem 3.4
19. Literature/2406.07478v3.pdf where expander transfer is relevant
20. relevant git history beginning at commit 502a6f0

GOAL_SPEC.md is authoritative for the mathematical model and kernel. Its
bounded-run success criteria are nonterminal checkpoints in this persistent
goal. This prompt is authoritative for persistence and terminal resolution.

Do not rely on missing disposable /tmp/reversible_runs directories. The
manuscript is the durable synthesis of those earlier runs.

# Exact model

Let T_N be all transpositions in S_N and

    Omega(N,m) =
      { (t_1,...,t_m) in T_N^m : t_1 ... t_m = id }.

The principal regime is N >= 3 and even m >= 4. Let

    R_m = {r in {3,4,5} : r <= m}.

For r in R_m and 1 <= i <= m-r+1, H_{i,r} replaces positions
i,...,i+r-1 by an exactly uniform length-r transposition word with the same
ordered product. The chain under review is

    K_{N,m} = (1/2) I
      + (1 / (2 |R_m|)) sum_{r in R_m}
          (1 / (m-r+1)) sum_{i=1}^{m-r+1} H_{i,r}.

The current block belongs to its conditional fiber, so every update is
well-defined. Fix and document one multiplication convention in every formal
argument and computational check. The uniform law pi_{N,m} is reversible and
stationary. Laziness removes periodicity. Irreducibility and a quantitative
gap are separate claims.

# Terminal outcomes

There are exactly two terminal outcomes.

TERMINAL A: UNIVERSAL PROOF

Produce a complete proof that there are universal constants c > 0 and C < infinity
such that, for every N >= 3 and even m >= 4,

    gap(K_{N,m}) >= c (N m)^(-C).

The proof must include or cite, with checked hypotheses and conventions,
irreducibility for the stated regime. It must account for all transition
normalizations and exceptional cases and yield the standard worst-case
total-variation bound

    tau_mix(epsilon)
      <= gap(K_{N,m})^(-1)
         (m log binom(N,2) + log(1/epsilon)).

Any needed exact block sampler must have polynomial per-step cost in N and m.
A proof only for connected support, only one macro-fiber, m above an
unstated threshold, fixed N, fixed m, or a modified chain is nonterminal.

TERMINAL B: RIGOROUS REFUTATION

Rigorously refute TERMINAL A by proving at least one of:

1. K_{N,m} is not irreducible for some N >= 3 and even m >= 4; or
2. there is an explicit infinite sequence (N_j,m_j), with N_j >= 3 and even
   m_j >= 4, along which the gap is superpolynomially small in N_j m_j.

For item 2, prove a statement strong enough to exclude every inverse
polynomial, for example

    for every C > 0,
    gap(K_{N_j,m_j}) (N_j m_j)^C -> 0.

A bottleneck proof must account for both stationary mass and boundary flow.
A counterexample to an auxiliary lemma, a large polynomial lower bound on
mixing, or slow finite simulations is nonterminal.

Only TERMINAL A or TERMINAL B may cause the goal to be marked complete.

# Nonterminal checkpoints

The following are valuable but never terminal by themselves:

- verifying qualitative irreducibility;
- proving a restricted theorem or one component of a decomposition;
- reducing the gap theorem to a named lemma;
- proving polynomial diameter without polynomial congestion;
- finding a barrier to one proof route;
- finding or rejecting a candidate bottleneck without an asymptotic theorem;
- obtaining exact finite spectra or Monte Carlo scaling;
- producing a publishable partial result;
- receiving referee approval for a partial result;
- defining a cleaner expander-generator benchmark;
- exhausting agent capacity, context, wall time, or a research cycle.

After every nonterminal checkpoint, update the ledger, state the new smallest
open implication, and immediately begin another cycle.

# Inherited results and failures

Treat these as inherited context, subject to exact citation and convention
checks. Do not assign agents to rediscover them from scratch.

1. Exact same-product heat-bath is reversible for the uniform law.
2. Direct exact r=4 and r=5 conditional samplers passed exhaustive checks
   through S_5; the integrated local kernel passed the recorded small cases.
3. Pure Hurwitz dynamics is not a global sampler. It preserves labeled
   weighted support-component data.
4. Ben-Itzhak and Teicher, Literature/0110110v1.pdf, Theorem 3.4, states that
   identity transposition factorizations are Hurwitz-equivalent exactly when
   their factorization graphs have the same labeled connected components and
   component weights. Their Hurwitz generator is inverse to one common project
   convention, but it generates the same equivalence relation. Verify this
   translation once and then use it; do not spend a full cycle reproving the
   classification unless the audit finds a real mismatch.
5. A component on v >= 2 labeled vertices supports a connected identity
   factorization of length k exactly when k is even and k >= 2(v-1).
6. Conditional on labeled weighted support-component data, the state space
   factors into color interleavings and independent connected identity
   factorizations.
7. A projection/fiber/mean-lift variance decomposition would prove the target
   if all three constants are polynomial.
8. A mesoscopic large-block comparison would prove the target if the ideal
   chain has inverse-polynomial gap and randomized local simulations have
   polynomial congestion.
9. K_m is a one-step global heat bath but is too global. Local same-product
   simulation is false for block length L=2 in general.
10. Representative L=6 fibers through S_5 were connected under tested
    pair/block resampling, with sampled BFS distance at most 12. This is finite
    evidence only.
11. Prior runs reported a fresh-square certificate for support expansion from
    a length-4 identity window, but the durable files do not retain its exact
    statement. Do not cite the missing disposable artifact as a proved lemma.
    State and prove any precise version before using it.
12. Deterministic comparison routing through one canonical doubled-tree or
    square-rich normal form has exponentially bad hub congestion. Normal forms
    are connectivity tools, not a rapid-mixing proof.
13. Random-slot square refresh has an action-rate bottleneck of order roughly
    1/binom(N,2) and was deprioritized as a standalone sampler.
14. Exact small-state gaps and conductance scans found no obvious bottleneck,
    but finite data does not imply polynomial mixing.
15. The 20260721 edge-shift experiment is graph-only and drops word ordering;
    it is not evidence for the chain K_{N,m}.
16. The old Hurwitz hitting-time experiment is unexecuted placeholder work and
    is not a result.
17. Polynomial in N is exponential in the wire count log_2 N. The present
    theorem is explicitly parameterized by N and m.
18. Chen--Haah--Haferkamp--Liu--Metger--Tan,
    Literature/2406.07478v3.pdf, proves strong spectral gaps for unconditioned
    random reversible circuits and gives efficient reversible-circuit
    implementations related to Kassabov generators. It does not analyze the
    identity-conditioned word chain K_{N,m}.

# Calibration suite

Every universal statement, comparison, coupling, or obstruction must be
checked against the applicable items below.

- Odd m: Omega(N,m) is empty.
- m=0: singleton state space.
- N=2 and even m: singleton state space.
- m=2 and N>=3: disconnected under block sizes 3,4,5; this case is excluded.
- S_3,m=4: 27 identity words and 4 pure-Hurwitz components.
- S_4,m=4: 120 identity words and 13 pure-Hurwitz components.
- S_4,m=6: 3936 identity words and 17 pure-Hurwitz components.
- For m=4, the r=4 update is a whole-word heat bath and cannot be ignored in
  normalization arguments.
- Connected near-minimal words have length 2(v-1) and doubled-tree examples.
- Disjoint support components commute, but the ordered word still contains a
  nontrivial color interleaving.
- Edge multiplicity parity or vertex-degree parity alone does not characterize
  identity words.
- L=2 local simulation is known to fail in general.
- A fixed canonical hub has exponentially small stationary mass.
- Any proposed asymptotic cut must have nonnegligible stationary mass or
  include an exact argument handling its mass.

Computational agents may use exact permutation arithmetic, Magma spot checks,
or bounded SAT/ILP encodings. They must state what universal claim the finite
calculation could falsify. They must not present finite convergence as proof.

# Machine and permission policy

The group-gated Bubblewrap/AppArmor setup is operational. The outer coordinator
runs under a persistent `workspace-write` sandbox with
`approval_policy="never"`; subagents inherit sandboxed execution. Use normal
sandboxed shell commands and keep all writes in the repository or `/tmp`.
Do not request elevated, unsandboxed, full-access, interactive, or network
execution. Do not run repeated sandbox probes during the research run; the
launcher preflight is authoritative.

Do not install system packages, alter machine configuration, use
`--dangerously-bypass-approvals-and-sandbox`, change the outer sandbox or
approval policy, or use `--ephemeral`. Record an unavailable dependency or
denied operation as a scoped blocker and continue with supported work. If the
platform failure prevents all meaningful work, checkpoint it as an
interruption; it is never mathematical resolution.

Workers do not commit, push, or edit shared durable files. The coordinator owns
the ledger and resolution files. Put reproducible computational artifacts under

    experiments/20260811-polynomial-mixing-resolution/
      cycle-NN/mission-ID/

with fixed seeds, exact commands, and machine-readable output. Keep bulk output
out of Git. Only the coordinator may promote stable conclusions to HANDOFF.md,
the manuscript, or the project skill, and only after refereeing.

# Concurrency contract

Request up to 15 concurrent subagents, excluding the primary coordinator. Use
every available slot productively. Do not require all 15 slots to exist at the
same time. Preserve all 15 lanes through sequential waves when capacity is
lower, and recycle completed threads continuously.

There is no maximum total number of subagent calls and no token cap for this
goal. Temporary thread exhaustion is not completion or blockage. While waiting
for capacity, integrate results, audit accounting, or pursue a coordinator
proof/counterexample lane.

Subagents do not share memory. Every assignment must include:

- the exact target statement;
- the relevant inherited results and failed routes;
- all ledger corrections since the prior assignment;
- the calibration cases it must survive;
- its owned output path, if any;
- the required return schema below.

# Fifteen initial missions

Dispatch these missions initially, using sequential waves if fewer than 15
threads are available.

M01 - Classification and irreducibility closure

Translate Ben-Itzhak--Teicher Theorem 3.4 into the project multiplication and
Hurwitz conventions. Audit the square-refresh plus padded-Hurwitz
irreducibility proof for all N>=3 and even m>=4, including every boundary case.
Do not reprove the classification unless a precise hypothesis mismatch exists.
Return either a complete qualitative theorem or the exact missing implication.
This is a prerequisite, not terminal mixing progress.

M02 - Exact macro projection

Define the stationary-flow projection under labeled weighted
support-component data, including its stationary weights and exact transition
probabilities induced by r=3,4,5 windows. Determine which candidate projected
moves have quantitatively useful probability. Do not infer rates from mere
reachability.

M03 - Projection gap proof

Using M02 or an independently exact formulation, seek an inverse-polynomial
Poincare or conductance bound for the macro chain. Build a comparison to a
well-understood partition/merge-split or allocation chain, with complete
stationary-flow and congestion accounting. If a fresh-square estimate is
needed, formulate and prove it explicitly because the prior run's exact
statement is not durably available.

M04 - Color-interleaving fiber

Inside a fixed weighted-component macro-fiber, isolate the color-word
interleaving chain created by local windows. Prove or refute a polynomial gap,
with dependence on component weights, number of components, and m. Handle rare
colors and near-minimal components explicitly.

M05 - Connected-factorization fiber

Study the restricted chain on connected identity transposition factorizations
of fixed support and length. Quantify padded Hurwitz dynamics and the extra
same-product moves. Seek comparison to interchange, adjacent-transposition,
map-enumeration, or known Hurwitz chains. Qualitative transitivity alone is not
enough.

M06 - Mean-lift comparison

Prove the missing bound relating the projected Dirichlet form of fiber means
to the full-chain Dirichlet form. Track small transition probabilities,
conditional fiber sizes, and normalization exactly. Try to construct a
counterexample function if the proposed mean-lift inequality is false.

M07 - Ideal large-block gap

Choose a mesoscopic L=L(N,m) and analyze the exact same-product K_L block
dynamics under the identity bridge law. Pursue parity-aware bridge smoothing,
return-probability ratios, and one-dimensional block-dynamics contraction.
A theorem for K_m alone is nonresponsive.

M08 - Pair-resampling theorem

Prove or refute that every feasible same-product length-L transposition fiber,
for useful L>=6, is connected by the relevant local pair/block replacements
with polynomial diameter. State the exact move set. Finite L=6 evidence is
calibration, not proof.

M09 - Randomized comparison flow

Construct randomized simulations of K_L transitions by r=3,4,5 updates that
spread flow across typical states. Bound edge and vertex congestion. Explicitly
avoid deterministic routing through one doubled-tree or square-word hub.

M10 - Direct coupling or functional inequality

Attempt path coupling, multicommodity coupling, entropy factorization, spectral
independence, approximate tensorization, or another direct functional
inequality for K_{N,m}. Identify a metric that respects endpoint conditioning.
Test all claims on near-minimal and sparse words where local influence is
largest.

M11 - Representation-theoretic mode analysis

Search for useful eigenfunction bounds or hidden slow modes using prefix
permutations, cycle types, low-dimensional S_N representations, and character
observables. Distinguish the word-chain operator from the ordinary random
transposition walk. Produce either a comparison inequality or an asymptotic
candidate obstruction.

M12 - Sparse and near-minimal red team

Try to refute polynomial mixing in regimes m close to 2(N-1), small support
surplus, thin component merge/split interfaces, or few square opportunities.
For each cut, estimate stationary mass and exact boundary flow. Slow traces
without a conductance calculation are insufficient.

M13 - Full-support and entropic red team

Search for bottlenecks inside full-support fibers that the macro projection
cannot see: tree shape, edge multiplicity profile, prefix geometry, character
statistics, or ordering complexity. Attack the fiber-gap and mean-lift
conjectures with explicit asymptotic families.

M14 - Exact falsification harness

Extend existing exact code only as needed to falsify named lemmas from
M02--M13. Enumerate the smallest decisive cases, verify normalization of the
exact lazy kernel, and use SAT/ILP only for bounded universal encodings.
Maintain a table mapping each computation to the exact claim it tests. Do not
produce another undirected grid of finite spectra.

M15 - Resource and paradigm auditor

Search the local literature first, then authoritative external sources, for
quantitative Hurwitz-action mixing, transposition-factorization enumeration,
random-map surgery chains, bridge block dynamics, decomposition theorems, and
Kassabov-generator transfer. State exact theorem hypotheses and whether they
apply. In parallel, formulate one genuinely different route to the same
terminal theorem. The expander-generator bridge model is a fallback benchmark,
not a refutation of K_{N,m}.

# Persistent cycle protocol

At the start of every cycle:

1. Update the status banner and exact frontier in
   notes/local-heatbath-polynomial-mixing-resolution-resolution-ledger.md.
2. Record all assignments and the inherited ledger entries sent to each agent.
3. Fan out over genuinely different methodological categories.
4. Keep at least two active counterexample lanes and at least one resource
   audit lane while a universal proof remains open.
5. Continue a coordinator proof or integration lane.

Every subagent must return:

1. Exact claim with all quantifiers and conventions.
2. Full argument or construction.
3. Worst-case probability, runtime, path-length, and congestion accounting
   where applicable.
4. Dependencies, each labeled proved, cited, conditional, or empirical.
5. First unproved step, stated as a standalone proposition.
6. Self-attack describing the strongest failure mode.
7. Calibration results against the assigned suite.
8. Artifact paths and reproduction commands, if computation was used.
9. Verdict exactly one of:
   - PROVED;
   - REFUTED;
   - OPEN AT A NAMED STEP: followed by the proposition.

PROVED or REFUTED describes the assigned claim, not automatically the global
goal.

After returns:

1. Append every result and failure to the ledger. Never overwrite history.
2. Reconcile disagreements explicitly.
3. Update the cumulative resolution document with a numbered checkpoint and
   ledger citations.
4. Freeze the strongest integrated proposal of the cycle.
5. Cross-red-team it with fresh agents.
6. Form a three-role strike team:
   - lead prover or constructor;
   - resource/probability/congestion auditor;
   - adversarial counterexample specialist.
7. If the result is nonterminal, formulate and dispatch the next cycle
   immediately.

If two cycles merely reproduce a known barrier, then at least half of the next
cycle must leave the dominant framework. Examples include switching from
canonical paths to functional inequalities, from support projection to
representation modes, from direct proof to asymptotic cut construction, or
from transposition combinatorics to bridge-measure comparison. Record the
pivot and its reason.

# Durable trace contract

The resolution ledger is append-only. Every entry receives a stable ID. Record
assignments, inherited context, returns, calculations, first gaps, self-attacks,
disagreements, reconciliations, frontier changes, referee reports, and next
assignments. Never delete a failed attempt. Append a correction that names the
superseded entry.

Keep this banner at the top of the ledger and update it in place only for
operational status:

    STATUS: ACTIVE | RESOLVED | INTERRUPTED
    STRONGEST RESULT:
    SMALLEST OPEN IMPLICATION:
    ACTIVE ASSIGNMENTS:
    LAST LEDGER ENTRY:
    EXACT RESUME INSTRUCTION:

The resolution document is cumulative synthesis, not a replacement for the
ledger. Preserve numbered checkpoints and cite ledger IDs.

# Terminal refereeing

Do not initiate terminal review until one exact integrated proof or
counterexample satisfies the literal definition of TERMINAL A or TERMINAL B.

Freeze that candidate statement and argument. Give the same frozen bundle to
at least three fresh full-result referees:

1. proof and quantifier referee;
2. probability, spectral, runtime, and congestion-accounting referee;
3. counterexample and construction specialist.

Each referee must return ACCEPT or REJECT with numbered objections. Reconcile
every objection in the ledger. Any valid objection reopens ACTIVE status and
triggers another cycle. A revised candidate must be frozen and reviewed again
by fresh referees.

Mark RESOLVED and complete the goal only if all three accept the same frozen
terminal bundle and every dependency is proved or correctly cited with checked
hypotheses. Agreement that a partial result is publishable is nonterminal.

# Interruption policy

A platform stop, context loss, machine failure, missing permission, exhausted
thread pool, or process termination is never resolution. Before yielding to
such an interruption:

1. append all returned and outstanding assignments;
2. record disagreements and failed routes;
3. update the resolution synthesis;
4. set STATUS: INTERRUPTED;
5. write the exact next assignments;
6. write one exact resume instruction.

On resume, read the ledger and resolution document before dispatching work,
restore ACTIVE status, and continue from the smallest open implication.

# First coordinator actions

1. Verify the repository commit and read all authoritative sources.
2. Initialize or validate the ACTIVE ledger before any fan-out.
3. Confirm the exact kernel and terminal contract in the ledger.
4. Dispatch M01--M15 with inherited context and calibration requirements.
5. Begin an independent coordinator lane on the smallest open implication.
6. Continue until a terminal outcome survives refereeing or an external
   interruption has been durably checkpointed.
