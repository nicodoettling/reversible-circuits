# Agent Prompt: Hurwitz Hitting-Time Tests

Use `$reversible-circuit-sampler`.

Work only in:

```text
experiments/20260710-hurwitz-hitting-times/
```

Implement two separate Hurwitz-only hitting-time tests. Do **not** add heat-bath moves, block-resampling moves, square-refresh moves, add/delete moves, or any orbit-breaking move.

Allowed move only:

```text
(g_i, g_{i+1}) -> (g_{i+1}, g_{i+1} g_i g_{i+1})
(g_i, g_{i+1}) -> (g_i g_{i+1} g_i, g_i)
```

## Test A: cycle adjacent-repeat hitting

Script:

```text
cycle_adjacent_repeat_hitting.py
```

Start from:

```text
C_k = (a_1 a_2)(a_2 a_3)...(a_k a_1)
```

Measure:

```text
tau_adjacent_repeat = min{t >= 0 : exists i with g_i(t) = g_{i+1}(t)}.
```

This is the first time the Hurwitz walk creates an adjacent cancellable pair.

If a canonical same-product star target is implemented, also record `tau_star`, but the required target for this test is the adjacent equal pair.

## Test B: identity star hitting

Script:

```text
identity_star_hitting.py
```

Start from identity words only:

```text
eval(w_0) = id.
```

Use both:

```text
random_identity_start
worst_case_identity_start
```

Define a canonical star identity target, for example:

```text
P_star = (a_1 a_2)(a_1 a_3)...(a_1 a_r)
star_identity = P_star P_star^{-1}
```

Measure:

```text
tau_star = min{t >= 0 : w_t = star_identity}.
```

Also record relaxed star-support hitting if exact star-node hitting is too rare:

```text
tau_star_support = min{t >= 0 : every transposition in w_t is incident to one common center}.
```

## Shared helper

Put common transposition, permutation, product, Hurwitz-step, BFS, and hitting-time utilities in:

```text
common_hurwitz.py
```

## Required outputs

```text
common_hurwitz.py
cycle_adjacent_repeat_hitting.py
identity_star_hitting.py
results.jsonl
report.md
```

The report must have two separate verdicts:

```text
cycle_adjacent_repeat: fast-looking / slow-looking / inconclusive
identity_star_hitting: fast-looking / slow-looking / inconclusive
```

Do not claim mixing-time results. Report only hitting-time evidence.
