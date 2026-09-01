# M139 plan: two-edge-core curvature

Date: 2026-08-13 UTC.

## Objective

Starting from the accepted M125/M129 exact coefficient formula and the
accepted M133/M136 subtraction-free unique-cycle expansion, determine whether
the two-parallel-edge-core profile

```text
H_2[d,c],  2 <= c <= d,
```

is ordinarily log-concave in `c` for every `d`, and seek a quantitative
curvature surplus that could dominate the higher-core correction in M133
(5.4).

## Target and scope

The target is the auxiliary connected-unicycle incidence-key mass `rho`, not
the original uniform identity-word law.  The exact theorem target is

```text
H_2[d,c]^2 >= H_2[d,c-1] H_2[d,c+1]
for d >= 4 and 3 <= c <= d-1.
```

Only conditional downstream implications for DEFECT NO-VALLEY or a defect
projection gap are in scope.  No claim about `gap(A_d)`, the handle
projection, the original lazy exact `{3,4,5}` heat-bath kernel, or either
terminal outcome will be made.

## Approach

1. Re-express a two-parallel-edge-core incidence graph as a pair of rooted
   bipartite trees joined at their common coloured endpoints, and sum the
   planted-tree weights by exponential generating functions.
2. Incorporate the permutation-cycle-type factor
   `n(lambda) product h(a_i)^2` before coefficient extraction, looking for a
   product, convolution, Stieltjes-moment, or totally-positive kernel in the
   cycle-count variable `c`.
3. Derive exact small and boundary formulas to falsify proposed universal
   strengthenings.  Computation is deterministic exact arithmetic and is
   evidence only unless it yields an exact counterexample.
4. If log-concavity survives, isolate the first missing analytic inequality;
   if it fails, freeze the first exact counterexample.  Quantify the two-edge
   curvature and compare it with the accepted higher-core correction only as
   a bounded diagnostic unless a universal proof is obtained.

## Expected failure modes

- the two-edge profile itself fails log-concavity at larger rank;
- factorial cut weights destroy an otherwise log-concave tree convolution;
- summing unequal atom sizes destroys total positivity;
- ordinary log-concavity holds but has asymptotically vanishing surplus, so
  no uniform multiplicative curvature can dominate higher cores;
- a positive recurrence is obtained without a theorem controlling its
  coefficient minors.

## Reproducibility

Repository base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
Python: standard library only, exact deterministic arithmetic, `seed=null`.
All scripts, JSON output, checkpoint, report, manifest, and hashes will live
only in this mission directory.
