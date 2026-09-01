# MPS/parent-Hamiltonian audit plan

## Objective

Determine whether the aligned microfactorized bridge Hamiltonian is literally a
normal or block-normal MPS parent Hamiltonian covered by the FNW/Nachtergaele
martingale bounds or by Rozman--Molnar--Schuch, and whether any cited theorem
supplies a lower bound polynomial in `N` and bridge length `n`.

The exact object is `G=A_N`, `E=T_N^2`, uniform `nu` on `E`, and
`p(t,u)=tu`.  On `E^n`, the two-site conditional projection preserves
`p(e_i)p(e_{i+1})`; the Hamiltonian is the sum of `I-P_i`.  Its fixed-product
sector has the uniform microfactorized `Q=P_T^2` bridge law.

## Claims tested

1. The two-site conditional projection is the orthogonal projector onto the
   length-two product-fiber MPS span.
2. The Peter--Weyl tensor
   `A^e=|E|^{-1/2} direct_sum_rho rho(p(e))` is block-normal, and its
   length-`r` MPS span is exactly the set of amplitudes depending only on the
   ordered product.
3. Once arbitrary-product aligned-`H_4` connectivity is used, the full
   Hamiltonian is a parent Hamiltonian and decomposes by endpoint with gap the
   minimum fixed-endpoint Poincare constant.
4. The primary martingale/parent-Hamiltonian theorems either yield an explicit
   inverse-polynomial family bound or retain an unresolved blocked-interval
   gap / exponentially large tensor parameter.

## Exact finite falsification check

`local_projector_check.py` will enumerate `N in {3,4}` and `n in {2,3}`.  It
checks the local fiber-projector formula, its rank, and that adjacent two-site
same-product replacements have exactly one connected component in each
feasible global endpoint sector.  This can falsify the asserted local algebra
or the smallest connectivity instances; it cannot prove the universal
connectivity or any asymptotic gap bound.

- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Deterministic computation; random seed: not applicable.
- Expected failure modes: confusing the heat-bath Markov projection with its
  orthogonal RK conjugate when weights are collapsed from `E` to `G`; treating
  one endpoint as a normal-MPS parent ground state; or dropping the finite
  blocked-interval gap from a martingale bound.

