# M61 plan: product-increment base correlation

Date: 2026-08-11. Convention `(pq)(x)=p(q(x))`; tuple products are
left-to-right. The chain is the nonlazy complete-pair heat bath `C_(l,h)`
on `l` raw microcoordinates in `E=T_N^2`, conditioned on product endpoint
`h in A_N`. The auxiliary coordinate operator is
`A_(l,h)=l^(-1)sum_i E[.|X_i]`, with top mean-zero eigenvalue `mu_l(h)`.

## Exact target

For every `N>=3`, every feasible endpoint `h`, and
`3<=l<C_mix N log(N+1)`, prove one of:

1. `mu_l(h)<=A/l` for a universal `A`;
2. a direct inverse-polynomial gap for `C_(l,h)` on the invariant closure
   of additive modes violating such a bound; or
3. an explicit rigorous family refuting the proposed correlation or gap
   statement.

## Independent lanes

1. **Proof/representation lane.** Derive the exact product-support
   conjugation representation, audit what survives arbitrary endpoint
   tilting, and attack near-minimal endpoints separately. Test whether
   positivity/exchangeability or a low-degree representation argument gives
   `O(1/l)`.
2. **Primary-resource lane.** Search only primary sources for
   noncommutative bridge Efron--Stein inequalities, Kac/CGL exceptional-mode
   estimates, random-transposition bridge correlations, and low-degree
   `S_N` representation bounds. Record exact hypotheses and mismatches.
3. **Falsification lane.** Reuse inherited exact calculations only to test
   named formulas. Retain the `N=6,l=3` rational Rayleigh witness, identity
   square/fixed-label modes, parity `Q=P_T^2`, and all endpoint cycle types.
   Explore analytically structured near-minimal long-cycle endpoints; finite
   spectra will not be promoted.

## Inherited results

- Leave-one-out recursion and all straddling pairs: proved.
- Normal scalar Toeplitz Gram reduction and product-support dimension
  `O(N^4)`: proved.
- Microfiber eigenvalue `1/l`: proved.
- Dense `l>=C_mix N log(N+1)` bound `mu_l<5/(4l)`: accepted.
- `mu_l<=1/(l-1)` refuted by exact rational `N=6,l=3` witness.
- Fixed `l=3,4` arbitrary-endpoint gaps and long-length MPS reduction:
  accepted, but do not give a universal base exponent.

## Deliverables

Write a halfway checkpoint and nine-field final report in this directory.
Every computation records the exact claim it can falsify, command, commit,
Python version, and deterministic/no-seed status. No shared durable file is
edited.
