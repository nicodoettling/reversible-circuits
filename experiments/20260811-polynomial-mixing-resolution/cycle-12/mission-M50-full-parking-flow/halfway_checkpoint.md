# M50 halfway checkpoint: full actual parking flow

Date: 2026-08-11.  Convention: `(pq)(x)=p(q(x))`; factor tuples multiply
left-to-right.  Scope: the nonlazy adjacent rank-two stationary-flow
projection `Pbar_r` in the minimal long-cycle sector, not the original
identity chain `K`.

The assigned full polynomial gap remains open, but three universal pieces
are now proved.

1. Every child boundary at a vertex `h` has exact aggregate upward rate
   `2d_h/[3r(r-1)]`; its destinations attach the later branch along the
   earlier branch right spine.
2. The stationary-flow quotient `Rroot_r` on ordered root branch-size
   compositions has law
   `(Z_r k!)^(-1) product_i a_i^(a_i-1)/a_i!`, exact adjacent merge/split
   rates, and gap at least `2/[9e r(r-1)]` after stationary path-length
   accounting.
3. Conditional on a root composition, the rejected-exit restriction is the
   exact product of smaller `Pbar_s` chains with coordinate action rate
   `s(s-1)/[r(r-1)]`.

The exact remaining implication is ROOT-MEAN LIFT in
`balanced_mean_lift.md`.  That note proves a polynomial mean-lift bound
would close `gap(Pbar_r)>=r^-D` by a balanced strong induction; the loss does
not multiply down tree depth.  The alternative accepted Cayley-exchange
source has gap `>=1/r`, but an explicit one-exchange family in
`cayley_exchange_geometry.md` requires at least `r-4` actual macro moves
after child sorting.  This rejects bounded-length domination only.

Exact reconstruction through `n=r+1<=8` finds no boundary-rate,
right-spine-support, quotient-normalization, or internal-product-scaling
failure.  These computations are falsifiers; the universal statements use
the combinatorial proofs in the owned notes.
