# M08 coordinator plan: fixed-endpoint aligned-H4 pair resampling

## Objective

Test the qualitative premise in the M10 bridge base case.  For `N>=3` and
`l>=2`, identify a microfactorized `Q=P_transposition^2` path with a length
`2l` transposition word.  At each `j=0,...,l-2`, resample positions
`2j,...,2j+3` uniformly conditional on their ordered product.  The endpoint
is the ordered product of the whole word.

The named universal claim that the calculation can falsify is:

> Every nonempty fixed-endpoint length-`l` fiber is connected under these
> aligned length-four same-product replacements.

The finite calculation cannot prove that claim, a polynomial diameter, a
spectral gap, or mixing of `B` or `K`.  If all tested fibers are connected,
the verdict remains `inconclusive` pending a universal proof.

## Conventions and cases

Permutations are tuples of images of `0,...,N-1`; `pq` means `p` after `q`,
and words evaluate from left to right as `t_1...t_m` in that convention.
The deterministic default cases are `(N,l)=(3,2),(3,3),(3,4),(3,5),
(4,2),(4,3)`.  They include every feasible endpoint, not only identity.
The named extension `(5,3)` is also run because `supp(Q)` is then a proper
subset of `A_5`.  No random seed is used.

## Exact method

Enumerate every transposition word.  For each aligned window, two states are
in one heat-bath clique exactly when their factors outside the window agree
and the four-factor ordered products agree.  Union each clique through its
first representative, then count components separately inside every endpoint
fiber.  Assert that unions never cross endpoints.

## Expected failure modes

- A nonidentity endpoint may possess a support or monodromy invariant absent
  from the identity bridge.
- Connectivity in all bounded cases may conceal a first obstruction at
  larger `N` or `l`.
- Qualitative connectivity, even universally, gives no inverse-polynomial
  gap without stationary-flow or congestion control.
