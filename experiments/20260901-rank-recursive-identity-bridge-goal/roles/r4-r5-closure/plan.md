# R4/R5 closure role plan

## Target and convention

The public target is the uniform identity bridge on

```text
Omega(N,2N^3;e).
```

Internal calls must support every feasible `Omega(r,L;g)`.  Permutations are
maps with `(alpha beta)(x)=alpha(beta(x))`, so displayed words act
right-to-left and successive right multiplication produces their displayed
product.

## Imported claims to audit

- R1: for a split at rank `r`, sorted old endpoint `h` and star endpoint `q`
  satisfy `q=h^{-1}g`, equivalently `h=gq^{-1}`, and the fixed-pattern map is
  a bijection.
- R3: prescribed-endpoint star counts and exact samples are polynomial-time,
  but this alone does not sample the weighted labeled `h` branch.

I will use neither result until its orientation, scope, and complexity have
been checked against the reports and smallest exact cases.

## Named candidate

For `d=binom(r-1,2)`, old length `a=L-k`, and
`A_a(h)=[h]C_(r-1)^a`, replace

```text
A_a(h) approximately 2 d^a/(r-1)!
```

on the parity-compatible coset.  Under this replacement, a star word `v`
with `q=eval(v)` forces `h=gq^{-1}`.  The stabilizer condition `h(r)=r` is

```text
q^{-1}(r)=g^{-1}(r).
```

The resulting proposed lift should choose `k` with weight

```text
binom(L,k) d^(L-k) Z_r(k,g^{-1}(r)),
```

where `Z_r(k,x)` counts star words with `eval(v)^{-1}(r)=x`, sample such a
word uniformly, recurse on `(r-1,L-k,g eval(v)^{-1})`, choose a uniform
binary pattern, and apply the R1 inverse.

## Work plan

1. State the complete exact `Count/Sample(r,L,g)` recurrence using R1 and R3;
   separate polynomial endpoint description size from factorial explicit
   branch enumeration.
2. Prove or refute the projected-star collapse above, including orientation,
   positive weights, an exact `Z_r` recurrence/closed form, and uniform
   projected-word sampling.
3. Prove a uniform pointwise relative mixing bound for the old
   random-transposition walk on its parity coset.  Translate it into a
   one-rank TV bound without confusing endpoint mixing with bridge
   conditioning.
4. Handle short old lengths by an explicit truncation/failure event.  Find
   rank-dependent retained-length floors whose total bad mass is negligible
   from the top length `2N^3`, uniformly in the retained endpoint.
5. State the recursive TV telescope and allocate explicit per-rank error.
   Identify whether the guarantee is tunable for arbitrary `epsilon` or only
   a fixed negligible function of `N`.
6. Validate the orientation, projected counts, and exact-versus-flat lift on
   the smallest ranks by deterministic exact arithmetic.
7. Audit all boundary cases: `N=2`, `L=0`, odd identity length, arbitrary
   minimal endpoint length, pair padding, and infeasible internal branches.

## Expected failure modes

- using `g^{-1}h` or `q(r)` instead of `h^{-1}g` and `q^{-1}(r)`;
- sampling an unconditioned star word without imposing the stabilizer
  projection;
- treating pointwise endpoint mixing as bridge TV control without comparing
  normalized positive branch weights;
- recursing into an endpoint whose transposition length exceeds `L-k`;
- bounding a short-length branch only under the flat proposal and not under
  the exact conditioned bridge;
- asserting that factorial enumeration by one natural exact implementation
  is unconditional sampling hardness;
- hiding an error floor while claiming arbitrary `epsilon` dependence.

## Deliverables

`checkpoint.md`, `report.md`, and, if the finite checks are used, a
standard-library script plus machine-readable results.  The report will end
with the required role schema and will classify every theorem component as
proved, conditional, empirical, refuted, or unresolved.
