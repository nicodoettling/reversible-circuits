# M135 plan: conflict coloring and simultaneous realization

Date: 2026-08-13 UTC.

## Objective

Continue the accepted M132/M134 frontier for the DPS adjacent-value edit on
the uniform minimal connected identity sector

```text
Z_d={(t_1,...,t_(2d-2)):t_1...t_(2d-2)=id,
                              support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors multiply
left-to-right.  Signed right-Hurwitz generators are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

For each adjacent DPS edge-label edit `tau_i`, test the surviving statement:
`Z_d` admits `d^O(1)` conflict-independent classes, each simultaneously
realized by one fixed signed braid of length `d^O(1)`.

## Work program

1. Reconstruct the exact DPS target/action and accepted paired-subgroup
   obstruction without importing predecessor code or output.
2. Search for an intrinsic global compression: paired-subgroup signatures,
   canonical braid normal forms, or a randomized polynomial family.
3. Separate the two logical obligations: conflict-independent coloring and
   simultaneous realization.  Test stronger multi-source Hurwitz invariants
   whenever pairwise compatibility is insufficient.
4. Use complete `d=3` and targeted `d=4` calculations only to falsify named
   universal claims or calibrate a rigorous structural reduction.
5. If no full theorem closes, freeze either a strict structural reduction or
   a minimal universal obstruction, with explicit first unproved lemma.

## Expected failure modes

- A descriptor has superpolynomial raw range.
- Pairwise subgroup equality is not sufficient for one diagonal braid orbit.
- A canonical schedule depends on the whole source, giving exponentially many
  schedules or superpolynomial length.
- Small-rank cover numbers do not control asymptotic coloring or realization.
- A randomized family covers sources only with unquantified probability or
  without source recovery.

## Scope exclusions

No use of the refuted `O(d^40)` contour key as a positive selector.  No UST
basis-exchange, all-edge comparison, `Gamma_0`, physical-gap, original
heat-bath-gap, or Terminal claim.

## Reproducibility

Repository base commit will be recorded at freeze.  Exact scripts use Python
3 from the repository environment, deterministic enumeration (`seed=null`),
and no nonstandard dependency unless explicitly recorded.
