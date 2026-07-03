---
name: reversible-circuit-sampler
description: Project-specific workflow for reversible identity-circuit sampler research. Use when Codex works on HANDOFF.md, transposition-gate reversible circuits, identity words in S_N, Hurwitz random walks, breakout MCMC, block heat-bath samplers, exact small-group bridge validation, sampler diagnostics, experiment logs, or self-improving autonomous agent loops for this project.
---

# Reversible Circuit Sampler

## Quick Start

Read `HANDOFF.md` first for project context. For mathematical and experiment details, read only the relevant reference:

- `references/sampling-problem.md`: definitions, target distributions, Hurwitz limitations, breakout moves.
- `references/experiments.md`: exact small-group validation, diagnostics, and reporting expectations.
- `references/self-improvement.md`: how agents should update this skill after durable lessons.

Prefer Python for sampler implementation and statistical experiments. Use Magma only for spot checks, subgroup calculations, or when Python group routines become awkward.

## Operating Workflow

1. State the target distribution before coding: fixed-length uniform bridge, Hurwitz-orbit uniform, sampler-defined MCMC stationary law, or expected-length Boltzmann/Gibbs target.
2. Keep implementations auditable: small pure functions for permutations, transpositions, word evaluation, moves, diagnostics, and experiment drivers.
3. Validate on tiny exact cases before scaling: enumerate identity words for small `S_N,m`; compare sampler output to exact statistics.
4. For `S_10`, avoid word enumeration at moderate lengths. Use exact permutation arithmetic and cycle-type dynamic programming or diagnostics instead.
5. Treat pure Hurwitz random walks as within-orbit scramblers. Do not claim global uniformity unless the chain includes orbit-breaking moves and the target/stationarity argument is explicit.
6. For agentic candidate-generation runs, assign each worker exactly one sampler candidate and require a `reject`, `keep`, or `promote` verdict; see `references/experiments.md`.
7. Record every nontrivial autonomous run in an experiment directory with objective, parameters, commands, results, and next changes.
8. When an experiment reveals a reusable lesson, update this skill or its references in the same turn and validate the skill.

## Recommended Implementation Shape

Use project code or experiment scripts with these layers:

- Core: permutation tuples, transposition enumeration, composition, inverse, word evaluation.
- Moves: Hurwitz step, lazy Hurwitz step, global conjugation, square/null-block refresh, fixed-length block resampling.
- Exact references: enumeration for small `N,m`; cycle-type transition DP for `S_10` bridges where useful.
- Diagnostics: prefix cycle types, transposition edge counts, adjacent repeats, support graph components, weighted component invariant, generated subgroup/order checks when feasible.
- Reports: JSON/CSV for raw runs plus a short markdown interpretation.

Use `scripts/start_experiment.py` to create a timestamped experiment folder with a plan skeleton when starting a new autonomous loop.

## Quality Bar

Before reporting progress:

- Verify sampled words evaluate to identity.
- Compare at least one small case against an exact reference when changing sampler logic.
- Separate implementation bugs from mathematical obstructions.
- Explicitly label empirical convergence evidence as empirical.
- Update `HANDOFF.md` only for durable project-level conclusions, not every transient experiment.
