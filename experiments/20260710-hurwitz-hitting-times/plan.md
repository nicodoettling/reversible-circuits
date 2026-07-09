# Hurwitz Hitting-Time Tests

- Created: 2026-07-10
- Objective: test **hitting times**, not mixing to stationarity.
- Allowed move: **Hurwitz move only**.
- Forbidden moves: no heat-bath, no block-resampling, no square-refresh, no add/delete move unless it is used only after recording a hit.

This experiment has two separate tests.

```text
Test A: cycle-start hitting time to an adjacent equal pair / star target.
Test B: identity-circuit-start hitting time to a star identity target.
```

The point is to understand whether the ordinary Hurwitz walk finds the useful cancellable/star configuration quickly or whether the hitting time can be very large.

## Common Hurwitz chain

A word is a tuple of transpositions

```text
w = (g_1, ..., g_m),    g_i = (u_i v_i).
```

The lazy Hurwitz step is:

1. with probability `1/2`, stay put;
2. otherwise choose `i in {1,...,m-1}` uniformly;
3. choose forward or inverse with probability `1/2`;
4. apply one of

```text
(g_i, g_{i+1}) -> (g_{i+1}, g_{i+1} g_i g_{i+1})
(g_i, g_{i+1}) -> (g_i g_{i+1} g_i, g_i).
```

For transpositions, the conjugates are transpositions again. The walk preserves length, total product, and Hurwitz orbit.

Implementation shared by both tests should go in:

```text
experiments/20260710-hurwitz-hitting-times/common_hurwitz.py
```

## Test A: cycle-start adjacent-repeat hitting

Script:

```text
experiments/20260710-hurwitz-hitting-times/cycle_adjacent_repeat_hitting.py
```

### Start state

Use the cycle-supported word

```text
C_k = (a_1 a_2)(a_2 a_3)...(a_k a_1).
```

Usually take `a_j = j` inside `S_N`, with `k <= N`.

This word is not necessarily an identity word. That is fine. In this test the target is not the full identity fiber; the target is a hitting event inside the Hurwitz orbit of `C_k`.

### Primary hitting event

Record

```text
tau_adjacent_repeat = min{t >= 0 : exists i with g_i(t) = g_{i+1}(t)}.
```

This is the first time the Hurwitz walk creates two equal adjacent transpositions, hence a local cancellable pair.

### Optional star hitting event

If a canonical star word with the same total product and same length is implemented, also record

```text
tau_star = min{t >= 0 : w_t = star_target(C_k)}.
```

But the primary required event for Test A is `tau_adjacent_repeat`.

### Parameters

Small exact/BFS cases:

```text
N in {4,5,6}
k in {3,4,5}
max_steps in {10^3, 10^4}
trials in {100, 1000}
```

Medium Monte Carlo cases:

```text
N in {8,10,12,16}
k in {4,6,8,10}
max_steps in {10^4, 10^5, 10^6}
trials in {100, 1000}
```

Keep only cases with `k <= N`.

### Output record

Each parameter setting should append one JSON object to `results.jsonl`:

```json
{
  "record_type": "cycle_adjacent_repeat_hitting",
  "walk": "lazy_hurwitz",
  "N": 10,
  "k": 6,
  "m": 6,
  "start_type": "cycle_word_C_k",
  "target_event": "adjacent_equal_transpositions",
  "trials": 1000,
  "max_steps": 100000,
  "hit_count": 0,
  "censored_count": 0,
  "mean_hit_time_conditional": null,
  "median_hit_time_conditional": null,
  "p90_hit_time_conditional": null,
  "product_failures": 0,
  "notes": ""
}
```

## Test B: identity-circuit-start star hitting

Script:

```text
experiments/20260710-hurwitz-hitting-times/identity_star_hitting.py
```

### Start states

The start state must be an identity word, i.e.

```text
eval(w_0) = id.
```

Test both kinds of starts:

```text
random_identity_start
worst_case_identity_start
```

Recommended random identity starts:

1. exact uniform from small identity fiber when feasible;
2. random construction by taking a random transposition word `P` and starting from `P P^{-1}`;
3. previously implemented identity sampler if available.

Recommended worst-case starts:

1. long cycle-like identity word `C_k C_k^{-1}`;
2. words with spread-out support and no adjacent equal pair;
3. any hand-constructed identity word that empirically looks far from the star target.

### Star target

Define a canonical star-supported identity word. For example, with center `a_1`, use a path/star word `P_star` and its inverse:

```text
P_star = (a_1 a_2)(a_1 a_3)...(a_1 a_r)
star_identity = P_star P_star^{-1}.
```

If the length must be exactly `m`, pad by adjacent duplicate pairs only in the construction of the target, for example

```text
sigma sigma
```

so that the total product remains identity.

The hitting time is

```text
tau_star = min{t >= 0 : w_t = star_identity}.
```

If exact equality to one star node is too rare in large cases, also record the relaxed star-support hitting time

```text
tau_star_support = min{t >= 0 : every transposition in w_t is incident to the same center}.
```

But the exact star-node hitting time must still be attempted and reported as censored if it does not happen.

### Parameters

Exact/BFS small cases:

```text
N in {3,4,5}
m in {4,6,8}
start_type in {random_identity_start, worst_case_identity_start}
```

Medium Monte Carlo cases:

```text
N in {8,10,12}
m in {10,20,30,40}
start_type in {random_identity_start, worst_case_identity_start}
max_steps in {10^4, 10^5, 10^6}
trials in {100, 1000}
```

### Output record

Each parameter setting should append one JSON object to `results.jsonl`:

```json
{
  "record_type": "identity_star_hitting",
  "walk": "lazy_hurwitz",
  "N": 8,
  "m": 20,
  "start_type": "worst_case_identity_start",
  "target_event": "exact_star_identity_node",
  "trials": 1000,
  "max_steps": 100000,
  "hit_count": 0,
  "censored_count": 0,
  "mean_hit_time_conditional": null,
  "median_hit_time_conditional": null,
  "p90_hit_time_conditional": null,
  "relaxed_star_support_hit_count": 0,
  "relaxed_star_support_median_conditional": null,
  "product_failures": 0,
  "notes": ""
}
```

## Exact checks when feasible

For small cases, do not rely only on simulation. Use BFS over the Hurwitz orbit of the start word and compute graph distances to the target set.

For Test A, compute distance from `C_k` to the set

```text
{w : exists i with g_i = g_{i+1}}.
```

For Test B, compute distance from the identity start to

```text
{star_identity}
```

and optionally to the relaxed star-support set.

Record exact BFS data as:

```json
{
  "record_type": "exact_hurwitz_hitting_distance",
  "test": "cycle_adjacent_repeat",
  "N": 5,
  "m": 4,
  "orbit_size": 0,
  "target_size": 0,
  "distance_to_target": null,
  "target_reachable": true
}
```

## Required files to produce

```text
experiments/20260710-hurwitz-hitting-times/common_hurwitz.py
experiments/20260710-hurwitz-hitting-times/cycle_adjacent_repeat_hitting.py
experiments/20260710-hurwitz-hitting-times/identity_star_hitting.py
experiments/20260710-hurwitz-hitting-times/results.jsonl
experiments/20260710-hurwitz-hitting-times/report.md
```

## Verdicts

Use separate verdicts for the two tests:

```text
cycle_adjacent_repeat: fast-looking / slow-looking / inconclusive
identity_star_hitting: fast-looking / slow-looking / inconclusive
```

A `slow-looking` verdict means many trials are censored, exact BFS distance is large relative to orbit size, or empirical hitting time grows sharply with `k`, `m`, or `N`.

Do not state a mixing-time claim from this experiment. This is a hitting-time experiment only.
