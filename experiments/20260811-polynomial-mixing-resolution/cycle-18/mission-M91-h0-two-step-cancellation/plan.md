# M91 plan: exact H0 two-step cancellation

Date: 2026-08-12.  Scope: fixed-endpoint minimal long-cycle `H0` only.

## Objective and target

Permutations compose as `(pq)(x)=p(q(x))`, and factor tuples multiply
left-to-right.  For odd `n>=7`, the underlying target is the uniform law on
minimal length-`n-1` transposition factorizations of
`h=(0 1 ... n-1)`.  The object studied is M73's exact pair-product kernel
`bar K_n`, quotiented by simultaneous conjugation by `h`.

The target claim is the strict-`Lambda_n` endpoint-sharing lemma

```text
TV(bar K_n^2(alpha,.),bar K_n^2(beta,.)) <= C/n^2.
```

Priority family: `n=3k` with odd `k>=3`,

```text
A_k=(0,k,2k),        B_k=(0,1)(k,2k),
eta_k=bar K(B_k,.)-bar K(A_k,.).
```

M83/M88 proved that the one-step TV for this family is
`Omega(k^-1/2)`, so the only admissible proof mechanism retains signs through
the second step and places the absolute value after summing all sixteen
ordered pairs of the `I3,IS,IN,X` schemas.

## Falsifiable outcomes

1. Prove `||eta_k bar K||_1=O(k^-2)` (and, if possible, the full strict-edge
   statement).
2. Prove a rigorously slower asymptotic for this family, refuting the target.
3. Otherwise reduce the family to one standalone explicit signed summation
   inequality, with every cyclic-orbit and lift multiplicity visible.

## Method

- Reconstruct exact quotient rows and their schema labels from the frozen
  M73/M83 formulas.
- Search for a posterior/data-augmentation identity or Abel summation in a
  one-dimensional gap variable.  Keep all signed terms combined.
- Use exact rational small-`k` evaluation only to test identities and locate
  the first non-cancelling boundary term; it cannot prove an asymptotic claim.
- Record a halfway checkpoint before final synthesis.

## Expected failure modes

- Triangle-bounding schemas separately, losing the `Theta(k^-1/2)` Borel
  boundary mass.
- Dropping quotient orbit stabilizers or the `a(g)=3,2` ordered-lift factors.
- Taking absolute values before the sixteen-schema sum.
- Treating residual-size data as a strong lumping.
- Inferring an asymptotic rate from finite spectra or fixed moments.

No H0 gap, bridge gap, identity heat-bath gap, or Terminal conclusion will be
claimed unless separately proved; those conclusions are outside this role.
