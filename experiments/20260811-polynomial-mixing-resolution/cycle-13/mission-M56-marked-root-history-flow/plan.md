# M56 plan: marked root-history flow

Date: 2026-08-11.  Convention: `(pq)(x)=p(q(x))`; minimal long-cycle
factor tuples multiply left-to-right.  Scope: the full nonlazy parking
projection `Pbar_r`, not the original identity chain `K`.

## Exact target

Starting from the accepted M50 child-boundary bijection, enrich each plane
tree with valid root split/attachment histories.  Either prove ROOT-MEAN
LIFT with a fixed polynomial, or construct a direct all-pairs flow proving
`gap(Pbar_r)>=r^-C`.  The first named test is whether canonical marked
coalescence to the unary-root fiber sends `pi_r` exactly to
`pi_r(.|d_0=1)`; if not, give the smallest exact counterexample and quantify
the endpoint density distortion.

## Routes

1. Compute the exact canonical coalescence kernel: merge the first two root
   branches, choosing a destination proportional to its actual `Pbar_r`
   rate, and iterate to root degree one.
2. Express its endpoint density by reversing marked histories using detailed
   balance.  Seek a universal polynomial bound without multiplying one-step
   Radon factors.
3. Test randomized-boundary and micro-level cyclic-root averaging only with
   all hidden incidence/order data retained.  Do not assume cyclic conjugacy
   descends to parking macros.
4. If a controlled endpoint law is proved, audit additive recursive
   congestion using the M41 Section 11 root-quotient gap
   `2/[9e r(r-1)]` and M50 product restriction rates.

Exact calculations through `n=r+1<=8` are bounded falsifiers only.  Scripts
use fixed deterministic commands and machine-readable JSON.
