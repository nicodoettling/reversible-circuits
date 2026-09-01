# M22 plan: rare-component desert red team

## Objective

Work with `(pq)(x)=p(q(x))` and the original lazy exact `r in {3,4,5}`
same-product heat-bath kernel.  Test whether the fixed-color obstruction from
M04 can be enlarged to an actual low-conductance subset of the global uniform
identity bridge, rather than merely a zero-gap iterated restriction.

## Named infinite family

For `N>=5`, put `L=N^3` and `m=4(L+1)`.  Let the rare component have three
labels and minimal weight four, and let the complementary connected component
have weight `4L`.  The candidate desert cut contains every interleaving in
which at least `L` large-component factors separate each consecutive pair of
the four rare-component factors.  It contains the rigid pattern
`(A B^L)^4`.

## Claims tested

1. Count the cut exactly in terms of connected identity-factorization counts,
   and prove its global stationary mass is at most `1/2` for all `N>=5`.
2. Count the color-word boundary layer with a tight first gap exactly.
3. From every state in that boundary layer, exhibit one actual `H_3` outcome
   which swaps disjoint-component factors, exits the desert, and has full-`K`
   probability at least `1/[6(m-2)M^2]`.
4. Conclude an inverse-polynomial lower bound on the candidate conductance.
   All `r=4,5` and macro merge/split exits are retained as nonnegative extra
   boundary flow, so the proof does not commit the bottleneck error of omitting
   them from an upper bound.
5. Exactly enumerate the representative `N=5,m=24,L=5` state to classify the
   full `r=3,4,5` heat-bath exit probability into same-macro color exits and
   macro-changing exits.  This computation can falsify the algebra and
   normalization, but cannot prove the asymptotic theorem.

## Expected failure modes

- The candidate macro may have more than half of global stationary mass;
  address this by a global word-count denominator, not a conditional argument.
- Endpoint gaps and internal gaps have different counting conventions.
- A claimed swap may alter within-color order or fail the noncommutative
  ordered-product check.
- Looking only at `H_3` could invalidate a conductance *upper* bound.  Here it
  is used only for a boundary-flow lower bound; every omitted transition can
  only strengthen rejection.

## Reproduction

The exact harness will use only Python's standard library and deterministic
enumeration.  It will record Python/repository metadata and machine-readable
fractions in `results.json`.
