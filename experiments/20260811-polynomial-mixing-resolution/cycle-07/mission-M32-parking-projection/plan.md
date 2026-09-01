# Plan: exact parking-multiset projection falsifier

## Objective

Test a named comparison needed only for the minimal long-cycle bridge sector.
For the long cycle on `n` labels, enumerate every reduced transposition
factorization, use Stanley's parking label (the smaller endpoint of each
factor), and aggregate the adjacent rank-two same-product heat bath by the
sorted parking multiset.

The finite calculation can falsify either of these universal support claims:

1. every adjacent Dyck-path raising move
   `c_x,c_(x+1) -> c_x+1,c_(x+1)-1` is an edge of the stationary-flow
   projection;
2. every such move already occurs from the nondecreasing parking-function
   representative.

It also records the smallest exact projected transition probability.  Finite
positivity is not a proof of a universal polynomial rate or gap.

## Convention and target

Permutations compose as `(pq)(x)=p(q(x))`; factor tuples multiply from left
to right.  The target is the uniform law on reduced factorizations of the
cycle `(0 1 ... n-1)`.  The nonlazy test kernel chooses one of the `n-2`
adjacent rank pairs uniformly and heat-bath resamples the two transpositions
uniformly conditional on their ordered product.

## Parameters and expected failure modes

Run exhaustively for `3<=n<=6`.  A zero projected edge refutes the proposed
one-step Dyck comparison.  Positive finite rates may conceal a rate tending
superpolynomially to zero, a different move graph at larger `n`, or poor
weighted-Dyck conductance.

