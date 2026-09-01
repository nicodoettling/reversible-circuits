# M16 plan: braided binary-collision algebra

Date: 2026-08-11  
Base commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

## Exact target

Use `(pq)(x)=p(q(x))`, `G=A_N`, `E=T_N^2`, uniform `nu` on `E`, and
`p(s,t)=st`.  On the uniform fixed ordered-product bridge in `E^l`:

1. define the micro Hurwitz bijection and the exact conditional heat bath on
   any two raw coordinates;
2. audit the projection algebra needed by Caputo Theorem 2.1, especially
   commutation/nonnegativity for disjoint pairs and the uniform
   three-coordinate gap;
3. determine whether Hurwitz/braid covariance repairs Sasada's
   local-to-complete comparison with polynomial loss;
4. if an identity fails, give the smallest exact positive-support witness
   and isolate the strongest star, laminar, or noncrossing statement that
   survives.

## Claims finite computation may refute

The deterministic harness will test the universal claims that:

- the proposed two-coordinate kernel is a self-adjoint idempotent preserving
  every endpoint fiber;
- its definition is independent of alternative braid shuttles;
- projections for every two disjoint coordinate pairs commute;
- the Caputo cross term for disjoint pairs is always nonnegative;
- a nonadjacent twisted update has a uniformly bounded adjacent-`H_4`
  simulation in the smallest cases.

A finite counterexample refutes one of these universal algebraic claims.  A
finite positive gap or successful simulation does not prove an asymptotic
comparison.

## Work split

1. Prove the micro Hurwitz and raw conditional formulas.
2. Classify pair-chord geometries and derive commutation where possible.
3. Enumerate `N=3,4`, beginning at `l=4`, to seek the smallest crossing-pair
   witness and an explicit rational test function.
4. Audit Caputo/Sasada proof dependencies and formulate the surviving named
   proposition.
5. Record a halfway checkpoint and final nine-field report.

