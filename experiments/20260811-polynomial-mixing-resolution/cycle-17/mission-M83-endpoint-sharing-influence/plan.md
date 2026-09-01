# M83 plan: endpoint-sharing two-step influence

Date: 2026-08-12. Repository base commit to be recorded in the final report.

## Objective and target

Work only on the uniform minimal transposition-factorization bridge to the odd
long cycle

```text
n=2l+1 >= 7,  h=(0 1 ... n-1),
Omega_n={(t_1,...,t_(n-1)): t_1...t_(n-1)=h},
```

with `(pq)(x)=p(q(x))` and factors multiplied left-to-right.  Let `bar K_n`
be M73's exact cyclic-orbit product-coordinate correlation kernel.  The named
claim is the endpoint-sharing influence estimate

```text
TV(bar K_n^2(O,.),bar K_n^2(O',.)) <= C/n^2,
```

whenever `O,O'` have lifts `(a,b),(a,c)` with `b,c` sharing one endpoint, or
the second-coordinate analogue.  Prove it with an absolute constant or give
an exact asymptotic refutation.  This is not the identity bridge and does not
itself imply Terminal A/B.

## Method

1. Reconstruct the exact orbit kernel and M73's `I3,IS,IN,X` schema formula;
   independently verify the M80 localized edge witnesses on small odd `n`.
2. Seek an exact signed formula for the difference of the two posterior
   predictive rows, keeping the full sixteen ordered schema pairs together.
   Prioritize cancellation identities, likelihood-ratio/score bounds, and a
   finite set of boundary terms created by the local three-cycle cut/join.
3. If a uniform proof is not obtained, classify endpoint-sharing edge types by
   cyclic gaps, identify a parametric extremal family, compute exact formulas
   or certified asymptotics, and test whether `n^2 TV` stays bounded or grows.
4. Falsify every proposed inequality on boundary cases and balanced/minimal
   components.  Label exact finite computation as finite only.

## Deliverables and stopping rule

- `checkpoint.md` by halfway;
- auditable scripts and machine-readable exact/numeric output for any
  computation;
- a nine-field `report.md` with claim, proof/refutation, dependencies,
  exceptions, self-attack, reproduction, artifacts, and verdict;
- frozen SHA-256 manifest, with no cache files.

Stop only on a complete proof, an exact asymptotic counterfamily, or a strict
new reduction containing a nontrivial proved step and a standalone remaining
lemma.
