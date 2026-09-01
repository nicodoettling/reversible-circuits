# M119 plan: fresh audit of M112 minimal genus-zero gap

## Objective

Independently audit the frozen M112 reduction concerning minimal connected
identity factorizations `Z_d`, marked-leaf deletion, and the rooted
Duchi--Poulalhon--Schaeffer product representation.  Determine exactly which
claims are proved, refuted, finite-only, or still conditional, without
importing M112 implementation code.

## Target and conventions

- Project target remains the uniform fixed-length identity-word law and the
  lazy exact `{3,4,5}` same-product heat-bath kernel from `GOAL_SPEC.md`.
- The object audited here is the auxiliary signed adjacent Hurwitz chain on
  `Z_d`, the length `2d-2` transposition factorizations of a fixed `d`-cycle.
- Permutations compose as `(pq)(x)=p(q(x))`; word factors are multiplied in
  displayed left-to-right order.

## Named claims to test

1. The marked-deletion transfer is a bijection with a null interval, singleton
   join entries, and `2 x 2` all-ones cut blocks, yielding
   `q C <= L <= q^2 C` with all measures explicitly distinguished.
2. Deletion equivariance and any spectrum-lift statement use the correct
   stationary laws; the finite statewise lifting counterexample has only its
   claimed scope.
3. DPS Proposition 3 / Theorem 5 gives the stated constant-degree rooted
   factorization-to-`UST x permutation` correspondence under the project's
   convention, and the independently implemented inverse is exact in small
   cases.
4. The ideal UST basis-exchange and adjacent-value permutation chains have the
   claimed gap normalizations.
5. The reported one-step intertwining witnesses and local Hurwitz distances
   reproduce independently.
6. A rooted-product local comparison, including handling the root quotient,
   would be sufficient for a polynomial gap on `Z_d`; identify every missing
   comparison/congestion hypothesis and the scope with respect to arbitrary
   product fibers `Gamma_0`.

## Computation

Write an independent compact enumerator in this directory for `d <= 4` (with
the decisive exhaustive comparison at `d <= 3` where appropriate), save raw
machine-readable output, and record exact commands and environment.  Do not
import M112 modules.

## Verdict

Issue `ACCEPT` or `REJECT` with numbered material objections.  This audit is
nonterminal for the overall polynomial-mixing goal.
