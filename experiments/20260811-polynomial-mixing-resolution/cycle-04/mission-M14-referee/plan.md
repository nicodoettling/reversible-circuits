# M14 referee plan

## Frozen claim

Audit the computer-assisted theorem that for every N>=3 and every feasible
endpoint pair (u,v), the aligned pair-length-three bridge heat bath B_3 is
irreducible and has gap at least M^-16, where M=binom(N,2). Equivalently its
two-term local Hamiltonian has Poincare constant at least 2M^-16.

Use (pq)(x)=p(q(x)) throughout.

## Referee tests

1. Reconstruct the exact microfactor-to-product-path quotient and the l=3
   bipartite incidence graph.
2. Audit the supportwise reduction from arbitrary N to N<=12, with special
   attention to fixed ambient labels and the identity endpoint.
3. Read the complete enumeration source and check endpoint-type completeness,
   microfactor multiplicities, composition order, class-mass checks, and split
   alternating-group classes.
4. Independently enumerate the actual six-microfactor heat-bath graph for
   N=3,4 and compare it with a separately implemented product incidence
   quotient.
5. Rerun the author harness at N=3,...,6 and N=12.
6. Re-derive the spanning-tree Poincare estimate, including scan probability,
   p_min, stationary mass, path length, and ordered-pair load.

A finite run is accepted as a universal proof only if the finite-basis lemma
is valid independently of the code.
