# Agent Operating Guide

Current research navigation: read [PROJECT_MAP.md](PROJECT_MAP.md) before
selecting a research target. Its evidence-linked catalogue reconciles later
sampler results and archived audits with the historical status below. Follow
[the map update protocol](notes/project-map/UPDATE_PROTOCOL.md) when integrating
new results; a map entry is not independent proof certification.

This repository studies sampling and hardness questions for reversible
circuits that compute the identity.  The current mathematical model is

```text
Omega(N,m) = { (t_1,...,t_m) : each t_i is a transposition in S_N,
               t_1 ... t_m = id }.
```

The main sampler candidate is the lazy exact same-product block heat-bath chain
using block sizes `{3,4,5}`.  The uniform law on `Omega(N,m)` is reversible
and stationary for this chain.  Irreducibility is needed to make that law
unique and to obtain convergence from every initial state.  Polynomial mixing
is open.

## Source of Truth

Before substantial work, read:

1. `HANDOFF.md`
2. `GOAL_SPEC.md`
3. `.codex/skills/reversible-circuit-sampler/SKILL.md`
4. `.codex/skills/reversible-circuit-sampler/references/sampling-problem.md`
5. `references/experiments.md` before computational work, or
   `references/self-improvement.md` before changing the skill
6. only the manuscript sections relevant to the assigned task under
   `papers/transposition_identity_samplers/sections/`

Repository files are the durable project state.  Do not rely on an old
`/tmp/reversible_runs` directory unless the current run manifest names it.
When documents disagree, report the disagreement instead of silently choosing
the more convenient claim.

## Current Research State

Proved or directly verified project inputs:

- Exact same-product heat-bath updates are reversible for the uniform
  fixed-length bridge law.
- Pure Hurwitz walks are within-orbit samplers and are not global samplers for
  `Omega(N,m)`.
- Direct exact conditional samplers for block sizes `r=4` and `r=5` passed
  the recorded small-case checks.
- A connected component on `v >= 2` vertices supports an identity word of
  length `k` exactly when `k` is even and `k >= 2(v-1)`.
- The state space conditional on labeled weighted support-component data
  factors into a color interleaving and connected identity-factorization
  problems.

Unresolved or conditional inputs:

- Connected-support identity Hurwitz transitivity appears to follow from
  Ben-Itzhak--Teicher, Theorem 3.4.  The exact source, hypotheses, and
  convention translation require verification before this is used as an
  unconditional theorem.
- Irreducibility of the local `{3,4,5}` chain is currently conditional on
  that classification input in the manuscript.
- No unconditional inverse-polynomial spectral-gap or mixing-time bound is
  proved.

Finite spectral gaps and conductance values are empirical or exact finite-state
facts, not asymptotic evidence strong enough to establish polynomial mixing.

Keep the parameterization explicit.  A bound polynomial in `N` and `m` for
`S_N` is not automatically efficient in the number `n=log_2 N` of wires
when the permutation domain is `{0,1}^n`.

## Research Rules

- Declare the target distribution before proving or coding: global fixed-length
  uniform, Hurwitz-orbit uniform, a conditional fiber law, a sampler-defined
  stationary law, or an expected-length Gibbs law.
- State the permutation-composition convention and the exact Markov kernel,
  including laziness, block-length probabilities, boundary handling, and the
  parameter regime.
- Label every material claim as `proved`, `conditional`, `empirical`,
  `conjectured`, `refuted`, or `unresolved`.
- Put every unproved hypothesis next to the result that depends on it.
- Do not claim global uniformity for a pure Hurwitz walk.
- Do not infer polynomial mixing from finite spectra, apparent convergence, or
  failure to find a bottleneck.
- When claiming a polynomial bound, name the variables and input model.
- Do not route all comparison paths through one canonical normal form unless a
  polynomial congestion bound is proved.  Existing work shows why this can
  incur exponentially large congestion.
- Treat a literature theorem as a dependency until its hypotheses,
  multiplication convention, and conclusion have been checked.  Record the
  exact source and theorem number.
- Prefer Python for exact small cases and diagnostics.  Use Magma only for
  group-theoretic spot checks that are awkward in Python.
- Use SAT or ILP only for a named finite encoding, such as bounded obstruction
  search or counterexample search.
- Do not spend a run on broad literature review or infrastructure unless it
  discharges a named obligation in `GOAL_SPEC.md`.

## Experiment Standard

Put each nontrivial experiment in:

```text
experiments/YYYYMMDD-short-slug/
```

Every experiment directory contains:

- `plan.md`: objective, target, tested claim, parameters, and expected failure
  modes
- the scripts or notebooks required to reproduce it
- machine-readable raw output such as `results.jsonl` or `results.csv`
- `report.md`: interpretation and a `reject`, `keep`, `promote`, or
  `inconclusive` verdict

Record the repository commit, exact command, parameter values, random seeds,
Python version, and nonstandard dependency versions.  A fixed seed is required,
but a stochastic conclusion should not depend on only one seed.

For sampler work, the report includes:

```text
candidate | claimed target | identity ok | crosses Hurwitz components |
exact diagnostics | verdict
```

Validate changed sampler logic on at least `S_3,m=4` and `S_4,m=4`; include
`S_4,m=6` when feasible.  Check word evaluation, prefix cycle types,
per-position edge frequencies, edge multiplicities, adjacent repeats, support
components, weighted-component invariants, and window product types as
appropriate.

## Proof Standard

A proof-oriented deliverable contains:

- a precise statement with all parameters, exceptional cases, and conventions
- a proof, or a clearly labeled obstruction
- a dependency list distinguishing proved inputs from conjectures
- the first unproved step, stated as a standalone lemma when possible
- a falsification attempt on boundary and minimal cases
- a manuscript-ready paragraph only when the claim is stable

Always check `m` odd, `m=0`, `m=2`, `N=2`, and near-minimal connected
factorizations when relevant.  Distinguish qualitative irreducibility from a
quantitative gap bound.  Symbolic checks and finite enumeration can refute a
universal statement but cannot prove it without a separate completeness
argument.

Preferred proof routes are:

- Projection/decomposition: projection Poincare or conductance, restricted
  fiber Poincare, and a mean-lift comparison.
- Large-block comparison: an inverse-polynomial gap for a useful ideal block
  chain, followed by randomized local simulation with polynomial congestion.
- Expander bridge benchmark: a separately declared generator model in which
  endpoint-conditioned bridge dynamics, rather than all-transposition support
  geometry, is the central issue.

## Hardness Standard

Hardness work must specify the group, representation, public structure, noise
model, parameter regime, and adversarial interface.  At minimum test sign,
cycle type, fixed points, support, low-dimensional characters,
meet-in-the-middle recovery, and syntax leakage.

The baseline candidate is a noisy permutation-code problem:

```text
Given public A_{i,b}, secret x in {0,1}^k, and noise E near id,
distinguish Z = A_{1,x_1} ... A_{k,x_k} E from uniform in G.
```

This assumption alone does not produce pseudorandom identity words.  The
identity-circuit construction likely needs a second, explicit
equivalent-circuit or relator-mixing assumption.

## Multi-Agent Coordination

Each worker owns one role and one role directory.  Workers do not edit
`HANDOFF.md`, the manuscript, `AGENTS.md`, `GOAL_SPEC.md`, the project
skill, or another worker's directory.  Only the coordinator synthesizes
durable project changes.

Use two phases:

1. Independent work: each worker writes a halfway checkpoint and a final
   report in its role directory.
2. Audit and synthesis: after reports are final, the coordinator inspects the
   artifacts, resolves contradictory claims, reruns the smallest decisive
   checks, and writes a claim ledger.

The claim ledger has:

```text
claim | status | assumptions | evidence/artifact | independent check | action
```

The coordinator must retain negative and minority findings, not only results
supporting the preferred conjecture.  A worker's `promote` verdict is not
accepted automatically.

Unattended workers do not install system packages, change machine
configuration, commit, push, or request interactive permission.  They record a
missing dependency as a blocker and continue with work supported by the
existing environment.

## Repository Hygiene

- Keep large generated output outside Git unless it is compact and necessary
  for reproducibility.
- Update `HANDOFF.md` only for durable project-level conclusions.
- Update the manuscript only for results stable enough for human review.
- Update the project skill only for reusable workflow knowledge, then validate
  it as required by the self-improvement reference.
- Preserve unrelated user changes.
- Before finishing, run `git status --short` and report every changed file.
