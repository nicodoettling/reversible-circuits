# M54 plan: root-composition referee and balanced mean-lift

Date: 2026-08-11.  Convention `(pq)(x)=p(q(x))`; factor tuples multiply
left-to-right.  The chain under audit is the nonlazy uniform adjacent
rank-two stationary-flow projection `Pbar_r` in the minimal factorization
sector of `(0 1 ... r)`.

## Exact targets

1. Independently audit M50's frozen-in-progress root-composition law,
   child-boundary count/rate, reverse rate, Lagrange basin identity, and its
   nonlumping/Radon statements.  Separately referee M41 Section 11's sharper
   stationary-path theorem `gap>=2/[9e r(r-1)]`, including both path halves,
   undirected capacity, and `r=2`.
2. Independently audit the fixed-composition product factorization and exact
   restriction Dirichlet identity
   `s_i(s_i-1)/[r(r-1)]`.
3. Seek either a stronger root quotient gap `Omega(1/[r(r-1)])`, an additive
   inverse-gap recursion
   `g_r^-1<=poly(r)+max_(s<r)g_s^-1`, or an exact counterexample showing that
   equilibrium crossing bias necessarily accumulates.
4. Test universal claims on `r=1,2`, root-unary and many-small-branch
   compositions, balanced splits, and exact bounded data only as
   falsification.
5. Compute the exact quotient spectrum on all `2^(r-1)` compositions for
   moderate `r` to test whether `gap/alpha_r` stays bounded below, and audit
   the aggregate reverse-split target Radon derivative relevant to an
   additive mean lift.

## Frozen inputs

```text
root_composition_projection.md  ba8e9a9c69153fce7f187c7b74438cd7b2e55529a3dd1314bf834ab7bc59d2c5
internal_branch_restrictions.md 70ebf3ca7195e136daaa44710f706473becbf3c419652147677ec5d799a99a89
root_composition_audit.py       73371ff0f3a2963880c300a5948ea2a20bb7a108e3dc0fda7e23428ad6777f0d
root_composition_results.json   8880b0cafe34c74ae18c6d68de52dce48cfca2a9cc469afb47179702a8ff5d1c
```

No shared durable file, M50 artifact, commit, or push will be modified.
