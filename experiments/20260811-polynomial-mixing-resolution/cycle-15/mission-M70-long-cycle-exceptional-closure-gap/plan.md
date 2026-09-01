# M70 plan: long-cycle exceptional closure

Date: 2026-08-12. Repository commit at assignment:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`. Convention
`(pq)(x)=p(q(x))`; tuple products are left-to-right.

Fix `n=2l+1`, `m=2l=n-1`, and the endpoint
`h=(0 1 ... n-1)`. Start with M67 v4's accepted frequency-two product
feature and aligned additive witness `F=sum_i f(G_i)`.

## Exact targets

1. Define the smallest exact invariant closure of `F` for the full
   complete-pair heat bath `C_l`, aligned adjacent-pair heat bath `B_l`, and
   the fixed-endpoint local `{3,4,5}` analogue `K^h`.
2. Track the exact coordinate covariance, total variance, scan normalization,
   and Rayleigh dissipation of `F`.
3. Use cyclic label conjugation and explicit Hurwitz full-twist paths to prove
   an inverse-polynomial Poincare bound on the entire frequency-two sector,
   hence on each exceptional Krylov closure.
4. Distinguish `K^h` from the goal's identity bridge `K`; audit whether any
   stationary-mass and boundary-flow lift exists.
5. Use `n=7,l=3` exact enumeration only to falsify normalization and closure
   claims, never as asymptotic evidence.

## Candidate bounds

For `V=E|f(G_1)|^2`,
`C=Re E[conj(f(G_1))f(G_2)]`, and `kappa=C/V`,

```text
Var(F)=lV[1+(l-1)kappa],
kappa>=Omega(n^-1/2).
```

Conditional-variance contraction should give the polynomial slow Rayleigh
upper bound `O(l^-3/2)` for `C_l`, `B_l`, and `K^h`. In the opposite
direction, a full Hurwitz twist implements simultaneous conjugation by `h`.
Since the witness has character `omega^2`, telescoping the twist should give
sector gaps with the exact polynomial loss retained.  The final padding
comparison contributes `M^-4=binom(n,2)^-4`; the proved bounds are of order
at least `n^-15` for `C_l` and `n^-14` for `B_l,K^h`.

## Scope

Even a proved polynomial sandwich is nonterminal. It refutes the fear that
M67's mode alone creates a superpolynomial exceptional closure, but it neither
proves the full bridge gap nor lifts automatically to identity-conditioned
original `K`.
