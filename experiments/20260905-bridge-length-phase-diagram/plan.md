# Plan: Uniform-Bridge Sampling Across Length Regimes

Status: prepared, not launched

## Objective

Build an audited complexity phase diagram for statistically uniform
transposition bridges in `S_N`, from short exact sampling through the current
dense rank-recursive result. The run asks whether short and dense algorithms
can be strengthened enough to overlap, and otherwise isolates the exact
intermediate connected-factorization primitive.

## Target

```text
Omega(N,m;g) = {w in T_N^m : eval(w)=g}
U_(N,m,g) = Uniform Omega(N,m;g)
```

The public endpoint is `g=e`. Sampler outputs must always have exact endpoint
and length. Approximation refers only to total variation from `U_(N,m,g)`.

## Workstreams

| Role | Question | Primary deliverable |
|---|---|---|
| `r1-short-exact` | How far can active-support compression make short bridges exactly samplable? | exact algorithm, runtime, growing-length range |
| `r2-dense-threshold` | How does the rank-recursive error depend on general `m`? | audited length/error theorem or precise failed inequality |
| `r3-intermediate-hybrid` | What remains after component/surplus decomposition? | hybrid sampler or strict positive reduction |
| coordinator | Which claims survive cross-audit, and do regimes overlap? | claim ledger, phase diagram, final classification |

## Expected failure modes

- treating `N^(O(m))` as polynomial in both inputs;
- inferring a dense threshold from unconditioned coupon collection;
- losing bridge-conditioning factors in rank truncation;
- omitting component interleaving or labeling weights;
- calling an uncovered band computationally hard without a reduction;
- claiming exactness from signed character formulas without a positive sampler;
- returning to local-chain mixing, which is outside this run.

## Runtime

Three hours with four active contexts total. The final 30 minutes are reserved
for nonauthor audit reconciliation and synthesis.

