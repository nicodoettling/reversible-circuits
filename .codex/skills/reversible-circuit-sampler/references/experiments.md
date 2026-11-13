# Experiment Reference

## Exact Small Cases

For small `N,m`, enumerate all transposition words and retain words whose product is identity. Use this to validate:

- identity preservation,
- component/orbit obstruction for pure Hurwitz,
- empirical marginals against exact uniform,
- convergence diagnostics for breakout chains.

Known useful smoke cases:

```text
S_3, m=4: 27 identity words split into 4 Hurwitz components.
S_4, m=4: 120 identity words split into 13 Hurwitz components.
S_4, m=6: 3936 identity words split into 17 Hurwitz components.
```

## Relaxed Endpoint Targets

For an intentionally relaxed endpoint law, check its declared correction
bound instead of requiring every output to be identity. For transposition
words, endpoint defect `N - number_of_cycles` has the parity of the word
length. At even lengths, budgets 0 and 1 are identical; budget 2 already
allows every endpoint in S3 and S4. Retain the standard smoke cases, but
include a genuinely constrained case such as S5,m4,k2 before interpreting
them as evidence about the relaxation. Restoring exact functionality by
appending a correction does not itself preserve a uniform circuit law.

For a correction-gate lift, count extensions per prefix before identifying
the projected target, and check whether the projected kernel is Markovian.
A coupling counterexample refutes its specified distance and time horizon;
it does not by itself prove slow mixing of the chain.
Keep uniform endpoint-permutation laws distinct from uniform circuit laws:
the latter weight endpoints by their word counts. Large pointwise density
ratios can coexist with small total variation; neither statistic alone
supplies a spectral comparison. Test a proposed prefix law by counting
extensions on a concrete endpoint event before inferring uniformity.

## Planted Conditional Mixtures

For hidden index-set planting, distinguish choosing an index set first and
conditioning the word from conditioning on existence of any witness. Derive
the fixed-set event probabilities before sampling: the mixture density is the
average of indicator/event-probability ratios. Equal probabilities reduce it
to witness count divided by its null expectation. Measure both likelihood
fluctuations and null witness existence; finding an accidental witness need
not distinguish the worlds.

In the global all-transposition bridge model, selected-left stable sorting
gives an exact conditional sampler by reversing Hurwitz moves on two uniform
bridges. Ordinary interleaving is not a substitute. Verify the inverse map on
small complete conditional fibers, and state the shorter-bridge sampler cost
separately. Test both short plants and short complements; prefix-conjugated
gates can expose complement witnesses. The worked reference is
`experiments/20261110-planted-subsequence/proof.md` and its exact checker.
For recursive constructions, keep the actual child laws in the analysis.
If a computational hybrid needs an exact reference sibling, check that the
reduction can sample it; hardwiring an unavailable sample invokes a stronger
nonuniform security model.
For a small plant in a long bridge, test random gate-pair equality and label
overlap before expensive subset search. A multiplicative completion estimate
can remain useful after rare-event conditioning; absolute TV alone may not.
Compare any residual inverse-polynomial bias with the declared security
parameter rather than calling a numerically small bias negligible.

## S_10 Testing

`S_10` has `10! = 3628800` elements and 45 transpositions. Direct permutation arithmetic is fine. Full word enumeration is not fine for moderate `m`.

For `S_10`, prefer:

- exact random-walk bridge calculations over cycle types,
- Monte Carlo diagnostics on word-level statistics,
- invariant checks that pure Hurwitz cannot pass,
- comparison between sampler variants at fixed parameters.

## Diagnostics

Collect multiple statistics. A sampler can pass one marginal while failing another.

- Word evaluation: product must be identity.
- Prefix cycle-type distribution.
- Per-position transposition frequencies.
- Edge multiplicity histogram over the transposition support graph.
- Adjacent repeat rate `ti = t{i+1}`.
- Support graph connected components and weighted component invariant.
- Generated subgroup order/orbit partition when feasible.
- Window/block product cycle types.
- Effective sample size and autocorrelation for MCMC chains.


## Candidate Iteration Protocol

Use this loop for each sampler candidate:

1. Name the candidate and declare its target or stationary distribution.
2. State why the move preserves identity, length, and the transposition gate library.
3. Implement the smallest self-contained version with fixed seeds and recorded parameters.
4. Validate on exact small cases before `S_10`: at minimum `S_3,m=4` and `S_4,m=4`; add `S_4,m=6` when feasible.
5. Compare against exact diagnostics: component occupancy, support invariant distribution, adjacent repeats, prefix cycle types, per-position transposition frequencies, and window product cycle types.
6. Classify the candidate as `reject`, `keep`, or `promote`.
7. Record the failure mode or promotion reason in the experiment report.
8. Promote only durable workflow lessons into this skill; promote research-level conclusions into `HANDOFF.md` only when stable.

Promotion requires identity preservation, explicit target discipline, evidence of moving between Hurwitz components when global uniformity is claimed, and exact small-case diagnostics that do not immediately reject the sampler.

## Candidate-Focused Worker Protocol

For agentic runs intended to produce samplers, make each worker own exactly one named candidate. Good worker assignments are implementation tasks, not broad research tasks.

Recommended first candidate assignments:

- Fixed-length block resampling / heat-bath: use exact conditional block enumeration where feasible.
- Square-refresh or null-block-refresh plus Hurwitz scrambling.

Each worker must produce:

- a smallest testable implementation,
- a declared target or stationary distribution,
- proof sketch or invariant check that moves preserve identity, length, and transposition gates,
- exact small-case results before any `S_10` experiment,
- comparison against exact diagnostics,
- raw `results.jsonl` or equivalent data,
- a report with a `reject`, `keep`, or `promote` verdict.

Use these anti-drift rules in worker prompts:

- Do not implement another pure Hurwitz baseline.
- Do not do literature review unless the assigned candidate is blocked by a specific mathematical question.
- Do not run `S_10` until exact small cases pass.
- Do not build infrastructure beyond what the candidate needs.
- Do not claim global uniformity without a stationarity or detailed-balance argument.

The coordinator should consolidate candidates in a table with columns:

```text
candidate | claimed target | identity ok | crosses components | exact diagnostics | verdict
```

Prefer falsifying weak candidates quickly over tuning parameters without changing conclusions.

## Reporting

Every experiment directory should include:

- objective and target distribution,
- parameters `N`, `m`, block size, chain length, burn-in, thinning, seed,
- exact reference method when used,
- commands or scripts run,
- raw data path,
- short interpretation,
- known limitations and next change.

Label empirical convergence as empirical. Do not promote it to a mixing-time claim without proof.
