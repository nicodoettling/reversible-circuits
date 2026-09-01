/goal
Conduct a bounded six-hour, multi-agent research run on the rank-recursive
sampler for dense transposition identity bridges.  The run must produce an
audited feasibility resolution, not a broad survey or another unrestricted
attack on the local heat-bath mixing theorem.

# Objective

Let `T_N` be all transpositions in `S_N` and

```text
Omega(N,L;g) = { (t_1,...,t_L) in T_N^L : t_1 ... t_L = g }.
```

The top-level target is the uniform law `U_N` on

```text
Omega(N,L_N;e),  L_N=2N^3.
```

Determine whether the positive `S_(N-1) subset S_N` rank disintegration can
be implemented as an exact or negligible-error sampler in time polynomial in
`N`, `L`, and `log(1/epsilon)`.  Arbitrary-endpoint fibers are internal
recursive states; the public output remains an identity bridge.

The bounded goal is complete only after all assigned roles have final reports,
the coordinator has audited the decisive claims, and
`experiments/20260901-rank-recursive-identity-bridge-goal/coordinator_report.md`
classifies the outcome as exactly one of:

```text
sampler-theorem | strict-reduction | architecture-obstruction | inconclusive
```

An `inconclusive` classification is an honest operational completion of the
six-hour run, not a mathematical resolution.  Do not stop early merely because
one route fails.  Conversely, do not continue beyond the deadline without a
new user instruction; preserve a resumable checkpoint if work remains.

# Authority and read order

Work in:

```text
/home/nico/projects/research_projects/reversible_circuits
```

Before dispatching workers, read in this order:

1. `AGENTS.md`
2. `notes/rank-recursive-identity-bridge-sampling.md`
3. the `Rank-Recursive Transposition Sampler Direction` section of
   `HANDOFF.md`
4. `.codex/skills/reversible-circuit-sampler/SKILL.md`
5. `.codex/skills/reversible-circuit-sampler/references/sampling-problem.md`
6. `.codex/skills/reversible-circuit-sampler/references/experiments.md`
7. `GOAL_SPEC.md` only for target discipline, proof standards, calibration,
   and multi-agent coordination; its local `{3,4,5}` mixing theorem is not the
   objective of this run
8. the following prior reports only where their stated facts are used:
   - `experiments/20260811-polynomial-mixing-resolution/cycle-02/mission-M12-high-surplus/proof_final.md`, Section 6
   - `experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M19-growing-surplus-redteam/report.md`, Sections 2.1 and 2.4
   - `experiments/20260811-polynomial-mixing-resolution/cycle-19/mission-M97-genus-one-hurwitz-gap/report.md`, Section 9
   - `experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M15/report.md`, the exact-sampling literature audit

Do not read the enormous historical run log unless a cited report is missing.
Do not resume the paused local-mixing proof search.  The consolidated note and
the named reports are the inherited project state for this run.

# Exact convention and feasibility

Use permutations as maps and state explicitly whether a displayed word acts
left-to-right or right-to-left.  Translate every external source into that
convention.  A fiber `Omega(N,L;g)` is feasible exactly when

```text
sign(g)=(-1)^L
```

and `L` is at least the transposition length `N-cycles(g)`.  Check `N=2`,
`L=0`, odd `L`, minimal endpoint length, and padding by pairs.

The recursive implementation must support the feasible arbitrary lengths and
endpoints generated internally.  It is not sufficient to implement only the
scheduled top-level lengths `2r^3`.

# Candidate exact rank disintegration

Embed `H=S_(N-1)` as the stabilizer of `N` and put

```text
C_N     = sum_(1<=i<j<=N) (i j),
C_(N-1) = sum_(1<=i<j<N) (i j),
J_N     = sum_(i<N) (i N).
```

The candidate word-level identity to audit is based on

```text
h (i N) = (h(i) N) h,  h in H,
C_N = C_(N-1) + J_N,
C_(N-1) J_N = J_N C_(N-1).
```

Writing `[g]X` for a group-algebra coefficient, the proposed formula is

```text
[g] C_N^L
 = sum_(k=0)^L binom(L,k)
     sum_(h in H)
       [h] C_(N-1)^(L-k) [h^(-1)g] J_N^k.            (D)
```

Its intended positive sampler is:

1. draw `(k,h)` with probability proportional to its summand in `(D)`;
2. draw a uniform old word in `Omega(N-1,L-k;h)`;
3. draw a uniform length-`k` star word with product `h^(-1)g`;
4. draw a uniform binary interleaving and invert the stable-sort bijection.

Treat `(D)` as a candidate proved derivation from the note, not as permission
to skip an independent convention and inverse-bijection audit.  Once audited,
do not spend later waves reproving it.

# Complete-support dense regime: R0

For a word `w`, let

```text
Full_N(w) = every transposition (i j) in T_N occurs at least once in w.
```

Equivalently, the unweighted transposition-support graph on `[N]` is the
complete graph `K_N`.  Do not call this graph `K_(binom(N,2))`.

The dense-support target is a theorem of the form

```text
Pr_(w~U_N)[not Full_N(w)] <= exp(-cN)                 (R0)
```

for a universal `c>0` and all sufficiently large `N`, or another explicit
negligible bound at `L_N=2N^3`.  A coupon-collector calculation for an
unconditioned word is not a proof under the identity-bridge conditioning.
Use bridge return counts, spectral estimates for a generator set with one
transposition removed, inclusion-exclusion, or another argument that controls
the conditioning.  State exactly what remains if only a weaker range or error
is proved.

Keep the canonical target unconditioned.  If `(R0)` holds, replacing `U_N` by
its law conditioned on `Full_N` costs exactly
`Pr_U_N[not Full_N]` in total variation.  Do not burden the rank state with a
full edge-coverage mask unless a proof shows it is necessary.

# Known facts and warnings

Inherit the following only with their cited scope:

1. Avoiding a fixed label identifies that missing-label fiber with
   `Omega(N-1,m)`.
2. A same-product square refresh can introduce a missing label.
3. A designated pendant-square rank insertion can occupy an exponentially
   small fraction at fixed rank and growing genus.
4. Marked deletion is not an everywhere-defined recursive coordinate in the
   audited genus-one route.
5. Duchi--Poulalhon--Schaeffer give an exact linear-time sampler only for
   connected minimal identity factorizations of length `2N-2`.
6. Feray--Louf--Thevenin give an asymptotically uniform genus-recursive sampler
   for factorizations of the long cycle, not dense identity bridges.
7. Feray and the star-factorization literature provide counting structure for
   powers of `J_N`; a counting formula is not automatically a sampler.
8. Pairing newly inserted star factors forces the stable-sorted lower endpoint
   to the special branch `h=e`.  Random conjugation hides the distinguished
   label but does not correct this branch weight.
9. Hurwitz moves may erase pair-insertion ancestry only through a quantitative
   start-specific mixing statement.  Qualitative orbit connectivity is not a
   mixing theorem.
10. Under the uniform identity target, conjugation symmetry gives the exact
    first moment

```text
E[number of factors incident to a fixed label] = 2L/N.
```

    A lift that retains all old factors and inserts only new-label factors
    cannot match a cubic length schedule even at this first moment.

# Research obligations

The run owns exactly these obligations.

## R0: complete transposition coverage

Prove the dense bridge-coverage statement above, prove a useful weaker
version, or isolate the first exact return-count inequality that blocks it.

## R1: positive stable-sort disintegration

Prove `(D)` for arbitrary external endpoint `g`, give the inverse map for
every binary pattern, and audit all multiplication conventions and boundary
cases.  Validate it by exhaustive coefficient checks for at least every
endpoint through `N=5,L=6`.

## R2: weighted branch sampling

Sample `(k,h)` with its exact or negligible-error weight without enumerating
`S_(N-1)`.  A character sum with signed terms is not a probabilistic sampler.
Any compression by cycle type, distinguished cycle, tableaux, or generating
functions must include state count, arithmetic bit complexity, and a method
to sample an actual labeled `h`.

## R3: prescribed-endpoint star bridge

Count and uniformly sample sequences of `k` factors `(i N)` with prescribed
product `q in S_N`.  Identify exactly which star-factorization formulas apply
to transitive versus nontransitive words and to arbitrary versus minimal
length.  Enumeration alone is insufficient: provide a positive recursive
decomposition or a proved reduction to one.

## R4: arbitrary-endpoint recursive closure

Formulate a complete `Count/Sample(N,L,g)` recursion.  Determine whether its
endpoint state can be represented and sampled in polynomial size at every
rank.  If a natural implementation has a superpolynomial state explosion,
prove that claim for the specified implementation; do not promote it to an
unconditional sampling-hardness theorem.

## R5: dense approximation and accumulated error

Investigate whether long random-transposition and star walks make the branch
weights sufficiently flat to avoid exact completion counts.  Every estimate
must be uniform over the endpoints retained by the algorithm and must survive
conditioning on the final product.

For rank lifts `Q_r` with errors `epsilon_r`, use the exact telescope

```text
d_TV(output at rank N,U_N) <= sum_(r=3)^N epsilon_r.  (E)
```

Allocate an explicit summable error budget.  Pointwise mixing of an
unconditioned endpoint walk does not by itself establish `(E)`.

## R6: exact red team and paired-lift bias

Enumerate the smallest feasible ranks and compute the exact `(k,h)` law,
star-fiber sizes, branch probabilities, and paired-lift total-variation
statistics.  Test proposed recurrences and inequalities adversarially.

The already-known observation that pair insertion starts in `h=e` is not a
new obstruction.  A promoted obstruction must address a precisely specified
symmetrized or post-Hurwitz architecture, identify an observable event, and
bound its probability under both laws.

# Worker allocation

Use six worker lanes plus the coordinator.  Request concurrency as available;
if the platform exposes only four active contexts, preserve all six roles in
sequential waves.  Do not reduce the role set merely because not all workers
can run simultaneously.

Each worker owns only its role directory under

```text
experiments/20260901-rank-recursive-identity-bridge-goal/roles/
```

Assign:

1. `r0-coverage`: dense complete-support bridge theorem.
2. `r1-bijection`: independent stable-sort and convention audit.
3. `r3-star`: star-factor count-and-sample algorithm.
4. `r2-branch`: positive branch-weight sampling and complexity.
5. `r4-r5-closure`: arbitrary-endpoint closure, dense approximation, and TV
   error composition.
6. `r6-redteam`: exact enumeration, falsification, and paired-lift diagnostics.

After the first reports, use a second audit wave.  At minimum, send the
strongest proposed algorithm or theorem to a fresh worker that did not author
it.  The coordinator may reassign a completed lane to this audit.  A worker's
`promote` verdict is never accepted automatically.

# Required worker return schema

Each role directory must contain `plan.md`, `checkpoint.md`, and `report.md`,
plus scripts and machine-readable results when computation is used.  Every
final report ends with:

```text
role:
claim:
status: proved | conditional | empirical | conjectured | refuted | unresolved
assumptions:
evidence:
independent_checks:
complexity:
first_unproved_step:
verdict: reject | keep | promote | inconclusive
```

Proof reports state a complete theorem with quantifiers and exceptional cases.
Experiment reports state which universal claim the finite calculation could
falsify.  Literature reports cite primary sources and exact theorem/formula
numbers.

# Coordination and durable outputs

The coordinator exclusively owns:

```text
experiments/20260901-rank-recursive-identity-bridge-goal/run_manifest.md
experiments/20260901-rank-recursive-identity-bridge-goal/claim_ledger.md
experiments/20260901-rank-recursive-identity-bridge-goal/coordinator_report.md
```

At startup, update the manifest with the repository status, exact Codex model
and reasoning effort, UTC start, deadline epoch, Python version, and available
dependencies.  Record pre-existing uncommitted files; never revert them.

The claim ledger uses:

```text
claim | status | assumptions | evidence/artifact | independent check | action
```

Retain negative and minority findings.  Every 45-60 minutes, or after a
decisive result, update the ledger and emit a short stdout status line so the
tmux log shows measurable activity.  Do not use the historical local-mixing
ledger for this run.

Reserve the final 45 minutes for fresh checks and synthesis.  The coordinator
report must contain:

1. the exact outcome classification;
2. the strongest accepted theorem or algorithm;
3. a table for R0--R6;
4. exact dependencies and unresolved assumptions;
5. the first standalone open lemma;
6. whether rank recursion is promoted, retained as speculative, or rejected
   in the specified form;
7. one recommended next action for human review.

Do not edit `HANDOFF.md`, `GOAL_SPEC.md`, the manuscript, `AGENTS.md`, or the
project skill during worker activity.  The coordinator may propose patches in
its report but must not promote them during this bounded run.  Do not commit or
push.

# Time protocol

At coordinator startup record

```text
target_seconds=21600
synthesis_reserve_seconds=2700
```

Use the first 45 minutes for source lock, role dispatch, and exact baseline.
Require a substantive checkpoint from every role by the three-hour mark.
Workers without a named claim by then must narrow to a falsifiable sublemma.
Begin final synthesis no later than 45 minutes before the deadline.

A proof or counterexample may end its role early, but another worker must audit
it.  The run itself does not end before the audit and coordinator report.

# Permissions and environment

Use the existing group-gated Bubblewrap/AppArmor setup.  The outer launch uses
`workspace-write` and `approval_policy=never`; workers inherit sandboxed
execution.  Do not request elevated, unsandboxed, full-access, interactive, or
network shell permission.  Do not install packages or change machine
configuration.  Record a missing dependency and continue with supported work.

Prefer Python exact arithmetic for finite checks.  Use Magma only for a named
group-theoretic check that is awkward in Python.  Use primary literature only
for technical claims.  Keep all writes inside the repository or `/tmp`, and
keep bulk generated output out of Git.

# Acceptance criteria

Classify as `sampler-theorem` only with an exact or negligible-error
polynomial-time sampler, a complete complexity proof, and a TV proof including
rank-error accumulation.

Classify as `strict-reduction` only if R0 and R1 are audited and the run solves
at least one material part of R2--R5, leaving a strictly narrower standalone
lemma than the initial question.

Classify as `architecture-obstruction` only with a rigorous obstruction to a
precisely specified recursive architecture beyond the already-known `h=e`
starting bias, plus the first surviving alternative.

Otherwise classify as `inconclusive`, preserving all reports and the exact
first open step.  Finite experiments alone, a restatement of `(D)`, a generic
literature survey, or failure to find an algorithm do not qualify as progress.
