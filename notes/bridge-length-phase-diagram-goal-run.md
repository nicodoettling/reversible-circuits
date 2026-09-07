/goal
Conduct a bounded three-hour, four-context research run on the sampling
complexity of uniform transposition bridges across bridge lengths. The run
must produce an audited sparse-to-dense phase diagram or a precise reduction
of the uncovered regime. It must not resume the local Hurwitz or block
heat-bath mixing-time program.

# Objective

Let `T_N` be the set of all transpositions in `S_N` and

```text
Omega(N,m;g) = { (t_1,...,t_m) in T_N^m : t_1 ... t_m = g }.
```

The public target is `U_(N,m)`, the uniform law on `Omega(N,m;e)`. Arbitrary
endpoints may be used internally. Every proposed sampler must output the
requested endpoint exactly; only its distribution over valid words may be
approximate.

Determine, as sharply as the time budget permits, for which regimes of
`(N,m,epsilon)` there is an exact or epsilon-close sampler running in time
polynomial in `N`, `m`, and `log(1/epsilon)`. The current internally audited
baseline is a fixed-negligible-error rank-recursive sampler at `m=2N^3`, not a
Markov-chain mixing theorem.

Do not assume there is a single hardness threshold or that an uncovered
regime is computationally hard. Distinguish:

```text
proved algorithmic regime | plausible regime | uncovered regime |
proved obstruction to a named method | computational hardness result
```

The run is complete only when all three research roles have final reports,
the strongest new claim has received a fresh nonauthor audit, and the
coordinator has written the phase diagram and final classification.

# Frozen decision question

Can the project rigorously narrow the gap between short exact sampling and
the current dense rank-recursive sampler by establishing one or more of:

1. a fixed-parameter exact sampler for short bridges with an explicit runtime;
2. an `m`-dependent dense error theorem substantially broader than `m=2N^3`;
3. an exact component/surplus reduction that identifies the first unsolved
   connected-factorization primitive in the intermediate regime; or
4. a hybrid sampler whose proved regimes overlap?

The coordinator must classify the outcome as exactly one of:

```text
all-length-polytime
quantified-phase-diagram
strict-intermediate-reduction
inconclusive
```

`All-length-polytime` requires an audited algorithm for every feasible
`(N,m)`, not an intuition. `Quantified-phase-diagram` requires at least two
proved regimes and an explicit uncovered band. `Strict-intermediate-reduction`
requires a correct positive disintegration and a standalone unsolved
primitive narrower than the original question. An honest `inconclusive`
classification is allowed at the deadline.

# Authority and read order

Work in:

```text
/home/nico/projects/research_projects/reversible_circuits
```

Before dispatching workers, read in this order:

1. `AGENTS.md`
2. the `Rank-Recursive Transposition Sampler Direction` section of
   `HANDOFF.md`
3. `papers/transposition_identity_samplers/sections/rank_recursive_sampler.tex`
4. `papers/transposition_identity_samplers/sections/next_steps.tex`
5. `notes/rank-recursive-identity-bridge-sampling.md`
6. `experiments/20260901-rank-recursive-identity-bridge-goal/coordinator_report.md`
7. `.codex/skills/reversible-circuit-sampler/SKILL.md`
8. `.codex/skills/reversible-circuit-sampler/references/sampling-problem.md`
9. `.codex/skills/reversible-circuit-sampler/references/experiments.md`
10. `GOAL_SPEC.md` only for target discipline, proof standards, and
    coordination; its local-chain mixing objective is out of scope here.

Use these historical reports only for the indicated inputs:

- `experiments/20260811-polynomial-mixing-resolution/cycle-02/mission-M02-coordinator/proof.md`
  for the exact support-component/interleaving count;
- `experiments/20260811-polynomial-mixing-resolution/cycle-02/mission-M12-intermediate-density/report.md`
  for connected all-genus count ratios;
- `experiments/20260811-polynomial-mixing-resolution/cycle-23/mission-M112-minimal-genus-zero-gap/report.md`
  for the rooted minimal identity-factorization product representation;
- `experiments/20260811-polynomial-mixing-resolution/cycle-24/mission-M119-m112-fresh-referee/report.md`
  for its independent audit; and
- `experiments/20260901-rank-recursive-identity-bridge-goal/roles/r4-r5-closure/report.md`
  for the retained-rank floors and error telescope.

Do not read the enormous historical resolution ledger or old run logs
wholesale. Follow a citation into them only if a named source above is
insufficient, and record why.

# Mathematical conventions and boundaries

Permutations are maps with

```text
(alpha beta)(x) = alpha(beta(x));
```

the rightmost displayed factor acts first. A fiber is nonempty exactly when

```text
sign(g)=(-1)^m and m >= N-cycles(g).
```

Treat `m=0`, odd `m`, `m=2`, `N=2`, minimal endpoint length, and padding by
transposition pairs explicitly. Complexity statements must name whether `m`
is fixed, parameterized, or part of the input. `N^(O(m))` is not polynomial
in `(N,m)`.

The phrase "the bridges become uniform" is forbidden. `U_(N,m)` is uniform
by definition. State instead when an algorithm's output law is close to it.

# Candidate regimes and hypotheses to test

These are research prompts, not inherited theorems.

## Short-support candidate

An identity word of length `m` appears to use at most `m` active labels,
because each nontrivial connected support component on `v` labels requires at
least `2(v-1)` factors. Test and formalize the resulting canonical
first-appearance-pattern sampler. A basic target is an exact runtime

```text
f(m) poly(N), possibly f(m)=m^(O(m)).
```

Then investigate whether cycle-type or cut-and-join dynamic programming
improves `f(m)`, and state the largest growing `m=m(N)` for which the proved
bound remains polynomial in `N`.

## Dense parameterization candidate

The existing result at `m=2N^3` is consistent with, but does not prove, a
bound resembling

```text
d_TV(Q_(N,m,g), U_(N,m,g))
    <= poly(N) exp(-c m/N^2).
```

Test whether the retained-rank proof can replace its hard-coded top-rank
scale by a density parameter such as `q=m/[N(N-1)]`. A desired theorem would
give an epsilon-close sampler for even feasible lengths near

```text
m >= C N^2 (log N + log(1/epsilon)).
```

Do not state this threshold without auditing every rank floor, ceiling loss,
bridge-conditioning denominator, finite-rank fallback, bit-complexity bound,
and accumulated error. If this exact target fails, derive the strongest
correct `m`-dependent bound and identify the inequality causing the loss.

## Intermediate component/surplus candidate

For a connected identity factorization on `v` active labels, parameterize
length as

```text
m_component = 2(v-1) + 2g,  g >= 0.
```

Use the proved support-component factorization to determine the exact global
law of labeled component sets, component lengths/surpluses, internal
connected words, and uniform color interleavings. Preserve every
combinatorial weight. Map which portions are already samplable:

- `g=0` connected minimal words via the audited DPS/Cayley-tree product;
- fixed or slowly growing `g`, if a positive recurrence yields a sampler;
- high surplus via rank-recursive smoothing, if its hypotheses apply.

Try to design a hybrid recursion that switches between short-pattern,
minimal/fixed-surplus, and dense rank-recursive primitives. If it does not
close, state the first missing positive count-and-sample primitive with all
inputs and desired runtime.

# Worker allocation and four-context ceiling

Use at most four simultaneously active agent contexts in total: one
coordinator and three worker contexts. Dispatch these three roles
concurrently:

1. `r1-short-exact`: prove and implement the short-support exact sampler;
   investigate cycle-type compression and give explicit runtime regimes.
2. `r2-dense-threshold`: reparameterize or falsify the dense retained-rank
   theorem and derive the strongest correct length/error tradeoff.
3. `r3-intermediate-hybrid`: derive the exact component/surplus law, audit
   known minimal inputs, and attempt a hybrid sampler or strict reduction.

Workers must not spawn additional subagents. When a worker finishes, the
coordinator may reuse that context for a fresh audit of another role. At
least one such nonauthor audit is mandatory for the strongest claimed result.
The coordinator owns literature reconciliation, cross-role synthesis, and
the final phase diagram.

# Required worker artifacts

Each worker owns only its role directory under:

```text
experiments/20260905-bridge-length-phase-diagram/roles/
```

Each directory must contain updated `plan.md`, `checkpoint.md`, and
`report.md`, plus scripts and machine-readable results when computation is
used. Every final report ends with:

```text
role:
claim:
status: proved | conditional | empirical | conjectured | refuted | unresolved
parameter_regime:
target_distribution:
runtime:
error:
assumptions:
evidence:
independent_checks:
first_unproved_step:
verdict: reject | keep | promote | inconclusive
```

Proof reports must include quantifiers, exceptional cases, and bit
complexity. Experiments can refute universal statements but cannot prove an
asymptotic theorem without a completeness argument.

# Exact checks and literature

For every new sampler or recurrence, test at least `S_3,m=4`, `S_4,m=4`, and
`S_4,m=6` when applicable. Check exact normalization, product convention,
endpoint validity, per-word probabilities, and boundary cases. Use fixed
seeds only for genuinely stochastic diagnostics; exact arithmetic is
preferred.

Live web search is available. Use it only for named technical dependencies
or a focused search for existing bridge/factorization samplers. Cite primary
papers and exact theorem/formula numbers. Failure to find a paper is not a
theorem of novelty.

# Coordinator outputs

The coordinator exclusively owns:

```text
experiments/20260905-bridge-length-phase-diagram/run_manifest.md
experiments/20260905-bridge-length-phase-diagram/claim_ledger.md
experiments/20260905-bridge-length-phase-diagram/phase_diagram.md
experiments/20260905-bridge-length-phase-diagram/coordinator_report.md
```

At startup, update the manifest with the exact repository commit/status,
model, reasoning effort, UTC times, deadline, available context capacity,
Python version, and dependencies. Preserve all pre-existing changes.

The claim ledger has columns:

```text
claim | status | parameter regime | assumptions | artifact |
independent check | action
```

The phase diagram has columns:

```text
regime | sampler | exact/approximate | runtime | TV error |
status | missing primitive
```

The coordinator report must include:

1. the exact outcome classification;
2. the strongest audited new theorem or reduction;
3. the complete sparse-to-dense phase diagram;
4. a distinction between uncovered and provably hard regimes;
5. the first standalone open lemma;
6. all external dependencies and convention translations;
7. the one most valuable next human-review target.

Do not edit `HANDOFF.md`, `GOAL_SPEC.md`, `AGENTS.md`, the manuscript, or the
project skill during this run. Propose durable patches in the coordinator
report. Do not commit or push.

# Time and persistence protocol

At startup record:

```text
target_seconds=10800
synthesis_reserve_seconds=1800
active_context_ceiling=4
```

Dispatch the three workers after the source lock. Require a substantive
checkpoint from every role within 75 minutes. Around the midpoint, compare
the short and dense bounds and redirect the intermediate worker toward the
actual uncovered parameter band. Begin fresh audits by the two-hour mark and
final synthesis no later than 30 minutes before the deadline.

Update the claim ledger and emit a concise stdout heartbeat every 25-35
minutes or after a decisive result so the tmux log shows measurable progress.
Do not stop merely because one route fails or a context temporarily reaches
its thread limit. Work locally, integrate finished reports, close completed
workers, and reuse slots.

The run may finish before three hours only if all role reports, the nonauthor
audit, the phase diagram, and the coordinator classification are complete.
At the deadline, stop starting new work, preserve exact resume instructions,
and synthesize honestly from completed artifacts.

# Permissions

Use workspace-write with `approval_policy=never`. Do not request interactive,
elevated, unsandboxed, or full-access execution. Do not install packages,
change machine configuration, push, publish, or access paths outside the
repository and `/tmp`. Record unavailable dependencies and continue with the
existing environment.

Prefer Python exact arithmetic. Use Magma only for a named group-theoretic
check that is materially awkward in Python. Keep bulk output in `/tmp` and
retain compact reproducible results in the experiment directory.

