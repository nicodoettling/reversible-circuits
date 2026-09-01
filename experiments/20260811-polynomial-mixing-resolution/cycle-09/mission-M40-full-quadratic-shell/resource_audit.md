# M40 targeted polymer/animal-neighborhood resource audit

## Local search

The repository's local `Literature/` directory contains the Ben-Itzhak--
Teicher Hurwitz paper, the Chen et al. reversible-circuit paper, and the
local cryptography paper.  None states a polymer/animal shell-boundary
injection theorem for endpoint-conditioned transposition words.

## Primary external source checked

Tobias Friedrich, Andreas Goebel, Martin S. Krejca, and Marcus Pappik,
*Polymer Dynamics via Cliques: New Conditions for Approximations*,
arXiv:2007.08293v4:

<https://arxiv.org/abs/2007.08293v4>

- Equations (1)--(2) define a polymer Gibbs law on pairwise-compatible
  polymer families with multiplicative weight `prod_gamma w_gamma`.
- Definition 3.1 updates one clique by inserting/removing at most one
  polymer.
- The clique-dynamics condition requires, for every polymer `gamma`,
  `sum_{gamma' incompatible gamma, gamma'!=gamma}
  f(gamma')w(gamma')/(1+w(gamma')) <= f(gamma)`.
- Theorem 3.4 gives the clique chain a unique polymer Gibbs stationary law
  and a mixing bound of order
  `m^3 Z_max log(m^2 Z_max^2 f_max/f_min)^2 log(1/epsilon)` under that
  condition.

## Exact hypothesis mismatch

The theorem does not apply literally to `V^(a)` or the chain `K`:

1. An identity bridge word is not uniquely a compatible family of local
   update clusters.  The same word has many update histories and many cluster
   covers.
2. Uniform bridge mass does not factor into positive per-cluster weights;
   the ordered-product endpoint constraint couples all positions.
3. An `H_3/H_4/H_5` heat bath is not the single-polymer insert/delete clique
   chain of Definition 3.1.
4. No clique-dynamics inequality, polynomial `Z_max`, or weight-ratio bound is
   available for a hypothetical shell-polymer representation.

Thus Theorem 3.4 supplies no shell conductance or boundary injection.  The
M40 proof instead uses a self-contained deterministic repair condition:
more than `5a` occurrences across every vertex cut.  Its abundance follows
from an elementary binomial lower-tail bound and remains valid after paying
the exact endpoint-conditioning factor `d!`.

The targeted search did not locate a primary lattice-animal theorem whose
state space, stationary weights, and local transition rule match the literal
fixed-endpoint word chain.  No external resource is used as a mathematical
dependency.
