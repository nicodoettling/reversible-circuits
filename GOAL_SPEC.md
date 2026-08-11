# Goal Specification: Resolve the Local Heat-Bath Mixing Frontier

Date: 2026-08-11

## Decision Question

Resolve, or materially narrow, the main mathematical uncertainty:

```text
Does the lazy exact same-product {3,4,5} block heat-bath chain on
Omega(N,m) have mixing time polynomial in N and m?
```

The run must end with an evidence-backed decision about this chain, not just a
collection of experiments.  A useful outcome is one of:

- an inverse-polynomial spectral-gap proof or a manuscript-ready new lemma
  that removes a central proof obligation
- a narrower and falsifiable reduction with substantive progress on its new
  lemma
- a concrete asymptotic bottleneck or obstruction candidate
- a rigorous reason to deprioritize this chain, paired with a more tractable
  theorem target

Finite experiments matter only when they test a named proof obligation or can
falsify a proposed universal statement.

Hardness assumptions and practical circuit compilers remain important to the
larger project, but they are out of scope for this mixing-focused run unless
the coordinator first records a decisive obstruction to both primary proof
routes.  Failure to find a proof within the run budget is not such an
obstruction.

## Target and Kernel

Let `T_N` be the set of transpositions in `S_N`.  The target is uniform on

```text
Omega(N,m) = { (t_1,...,t_m) in T_N^m : t_1 ... t_m = id }.
```

The primary regime is `N >= 3` and even `m >= 4`.  Odd `m` gives an empty
state space; `m=0`, `m=2`, and `N=2` are exceptional cases to state
separately.

Use one precise kernel in all proof and experiment reports.  Let

```text
R_m = {r in {3,4,5} : r <= m}.
```

For `r in R_m` and `1 <= i <= m-r+1`, let `H_{i,r}` replace positions
`i,...,i+r-1` by a uniformly random length-`r` transposition word having the
same ordered product as the old block.  Define

```text
K = (1/2) I
    + (1 / (2 |R_m|)) sum_{r in R_m}
        (1 / (m-r+1)) sum_{i=1}^{m-r+1} H_{i,r}.
```

The old block belongs to its conditional fiber, so every `H_{i,r}` is
well-defined.  Implementations must document whether permutations act on the
left or right and test that convention.

The uniform law `pi` on `Omega(N,m)` is reversible and stationary for
`K`.  Irreducibility, uniqueness, and convergence are separate issues.  Use
worst-case total-variation mixing:

```text
tau_mix(epsilon) =
    min{t : max_x ||K^t(x,.) - pi||_TV <= epsilon}.
```

The desired result is an explicit polynomial `p` such that, for all
nonexceptional `N,m`,

```text
gap(K) >= 1 / p(N,m),
```

or an equivalent polynomial bound on `tau_mix(epsilon)`.  State all
dependence on `N`, `m`, and `epsilon`.  Polynomial time in `N` is
exponential in the wire count `n=log_2 N` when the domain is
`{0,1}^n`.

## Evidence Baseline

Proved or directly verified project inputs:

- exact block heat-bath stationarity and reversibility
- direct exact conditional samplers for block lengths `4` and `5`
- pure Hurwitz confinement to weighted support-component orbits
- the feasible connected identity-component criterion:
  `k` even and `k >= 2(v-1)`
- macro-fiber factorization by labeled weighted support-component data

External dependency requiring audit:

- Ben-Itzhak--Teicher, Theorem 3.4, appears to imply connected-support identity
  Hurwitz transitivity.  Its statement, conventions, and bibliographic data
  must be checked before it is used unconditionally.

Empirical evidence only:

- finite checks in small `S_N,m` found no obvious support-size or
  weighted-component bottleneck
- representative same-product length-six fibers were connected under the
  tested local pair/block moves

These finite observations do not establish irreducibility in general,
conductance bounds, or polynomial mixing.

## Primary Proof Obligations

### Route A: Projection and Decomposition

Let `Phi` map a word to its labeled weighted support-component data.  Prove:

1. an inverse-polynomial projection Poincare or conductance bound
2. an inverse-polynomial restricted-fiber Poincare bound
3. a polynomial mean-lift comparison from the projection to the full chain

The run should identify the exact projected transition probabilities rather
than reason only from possible macro-moves.

### Route B: Large-Block Comparison

For a mesoscopic exact same-product block chain `K_L`, prove:

1. an inverse-polynomial gap for a useful `L=L(N,m)`
2. connectivity and polynomial-length randomized simulations of its
   transitions by local `{3,4,5}` updates
3. polynomial comparison congestion

Canonical doubled-tree normal forms may establish connectivity, but routing
all flow through one such word is not an acceptable mixing proof.

### Adversarial Route

Search for a statistic or family of cuts with superpolynomially small
conductance.  Prioritize sparse and near-minimal regimes, full-support fibers,
component merge/split transitions, and any quantity that local windows change
only rarely.  A proposed bottleneck must include its stationary mass and
boundary-flow estimates, not just slow-looking traces.

## Worker Roles

Each worker owns one role and produces a final verdict.

### Role 1: Projection Gap

Deliver:

- the exact projected state space and stationary-flow kernel
- a comparison chain or direct inequality
- a proof attempt with constants
- the first unresolved lemma or a concrete obstruction

### Role 2: Fiber Gap

Deliver:

- a decomposition into color interleavings and within-component chains
- quantitative treatment of both subproblems
- the role of Hurwitz transitivity stated precisely
- the first unresolved lemma in standalone form

### Role 3: Large-Block Comparison

Deliver:

- a precise ideal chain `K_L` and justified choice of `L`
- a Pair-Resampling or replacement-connectivity lemma
- randomized routing designed to avoid atypical hubs
- either a congestion estimate or a sharply identified failure

### Role 4: Adversarial Bottleneck Search

Deliver:

- named candidate cuts and why their stationary mass is nontrivial
- exact or Monte Carlo boundary-flow estimates where useful
- SAT or ILP encodings only for named bounded questions
- a verdict: credible obstruction, tested and rejected, or inconclusive

### Role 5: Theorem and Convention Audit

Deliver:

- the exact identity-Hurwitz source and theorem number
- a convention-by-convention translation to the project
- a minimal sufficient theorem statement
- an audit of every dependency in the conditional irreducibility proof

### Role 6: Exact Harness and Claim Testing

Deliver:

- exact references for the specific finite claims requested by Roles 1--4
- adversarial tests of proposed lemmas and inequalities
- reproducible scripts, fixed seeds, and machine-readable output
- a report separating exact facts from Monte Carlo evidence

This role is a proof-audit service, not a mandate for larger spectral tables.

### Role 7: Expander Bridge Benchmark

Deliver:

- a separate abstract model with a symmetric bounded-degree generating set and
  a uniform base-walk spectral gap
- a precise bridge heat-bath chain and theorem target
- the endpoint-conditioning estimate that remains missing
- a comparison with the transposition chain and the reversible-gate
  implementation caveat

This role is a fallback benchmark.  It does not establish that the
all-transposition chain should be abandoned.

### Role 8: Coordinator

Deliver:

- a claim ledger:

```text
claim | status | assumptions | evidence/artifact | independent check | action
```

- a summary table:

```text
role | strongest claim | evidence | verdict | next lemma
```

- a final project decision
- proposed durable updates only for claims that pass audit
- the single most valuable item for human mathematical review

The coordinator starts final synthesis after worker reports are present.  It
must inspect cited proof passages and rerun the smallest decisive computational
checks.  A worker's `promote` verdict is not accepted automatically.

## Run Protocol

Recommended configuration:

```text
agents: 6 to 8
wall time: 4 hours
synthesis reserve: final 30 minutes
mode: independent role work, followed by coordinator audit
```

With six agents, use Roles 1--5 and 8.  With seven, add Role 6.  With eight,
add Role 7.  Do not add a hardness worker at the expense of a primary mixing
role.

Create:

```text
experiments/YYYYMMDD-goal-run/
```

The root contains:

- `run_manifest.md`: start commit, model/configuration, roles, commands,
  wall-time budget, and environment assumptions
- one subdirectory per worker role
- `claim_ledger.md`: coordinator-owned claim status
- `coordinator_report.md`: final decision

Each role directory contains:

- `plan.md`
- `checkpoint.md`, written by halfway through the worker budget
- proof notes or reproducible scripts
- raw machine-readable output when computation is used
- `report.md`

Workers do not edit shared durable files or another worker's directory.  Only
the coordinator may update `HANDOFF.md`, the manuscript, or the project skill,
and only after recording the supporting evidence in the claim ledger.  Agents
do not commit or push during the run.

## Acceptance Criteria

The run succeeds only if it produces at least one of:

- a manuscript-ready lemma removing a current central proof obligation
- a strictly narrower reduction plus a nontrivial proved step toward it
- a reproducible asymptotic bottleneck candidate with stationary-mass and
  boundary-flow analysis
- a rigorous reason to deprioritize the local transposition chain, plus a
  precise alternative theorem target

Restating an existing conditional theorem, merely naming an unproved lemma,
adding finite spectral data, or failing to find a bottleneck does not count as
success.  A reduction counts only if the remaining statement is narrower and
falsifiable.

Every proof claim must state assumptions and exceptional cases.  Every
computational claim must identify code and raw output.  Every literature claim
must identify a source and exact result.  The coordinator labels each claim
as one of:

```text
proved | conditional | empirical | conjectured | refuted | unresolved
```

## Termination and Decision

Stop a worker early when:

- a decisive counterexample invalidates its assigned route
- it has a complete theorem, obstruction, or strict reduction to report
- its next step requires a new external assumption or unavailable dependency
- its work has drifted into unrelated review or infrastructure

At halfway, a worker without a named claim or falsifiable subproblem must
narrow scope.  Reserve enough time for a complete report; unfinished scratch
work is not a deliverable.

The coordinator classifies the run as:

```text
proof-progress | obstruction-progress | tooling-progress | inconclusive
```

and chooses exactly one project decision:

```text
continue-local-chain | revise-local-chain | pivot-to-expander-benchmark |
no-decision
```

`pivot-to-expander-benchmark` requires a mathematical obstruction or a
well-supported structural failure of both primary proof routes.  Expiration of
the wall-time budget alone implies `no-decision`.
