# M108 plan: direct adjacent-pair bridge gap

Date: 2026-08-12.

## Objective

Attack the exact auxiliary proposition sufficient for Terminal A. For
`T=T_N`, `M=binom(N,2)`, a feasible endpoint `h in S_N`, and

```text
Omega_m(h)={t in T^m:t_1...t_m=h},
```

let `pi_(m,h)` be uniform and let `H_(i,2)` exactly resample positions
`i,i+1` conditional on their ordered product. Define

```text
J_(m,h)=1/2 I + 1/[2(m-1)] sum_(i=1)^(m-1) H_(i,2).
```

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
The primary target is `h=id`, `N>=3`, even `m>=4`. The proof may require
uniform all-endpoint estimates with `sign(h)=(-1)^m`. The desired bound is
`gap(J_(m,id))>=c(Nm)^(-C)` with universal constants. M01's accepted
comparison would then give `gap(K)>=gap(J)/(3M^2)`.

## Audit and attack

1. Reconstruct M01/M01-audit's exact one-step comparison and exceptional
   cases without using its qualitative canonical hub quantitatively.
2. Identify precisely what the complete-pair/CGL reductions prove and the
   smallest all-endpoint length/sector they leave open; do not transfer the
   fixed-long-cycle H0 result to arbitrary endpoints.
3. Select one concrete sufficient theorem at that first open sector, or name
   and rigorously refute a proposed route by an exact symbolic or bounded
   finite witness.
4. Preserve target, laziness, scan factors, endpoint order, parity, and
   singleton-fiber conventions in every claim.

## Falsification rules

- No global gap from qualitative connectivity, stationary average square
  frequency, finite spectra, or a fixed endpoint.
- No canonical normal-form hub without polynomial congestion.
- No ordinary exchangeable Caputo--Sasada transfer to a noncommutative
  ordered-product bridge.
- A one-way auxiliary comparison cannot establish Terminal B.

## Outputs

`checkpoint.md`, a proof or obstruction note, reproducible exact diagnostics
only if tied to the named lemma, a nine-field `report.md`, and `SHA256SUMS`.
No M105 or predecessor file will be edited.
