# M255 checkpoint

Status: substantive audit complete; provisional verdict `ACCEPT`.

## Immutable gate

All 11 entries in M251's `SHA256SUMS` pass, and the checksum-file digest is

```text
c4cee2dc9596bb54503f85a7b32b91b360fe22d1aa981eb0dce7e3d7657c04fd
```

M251 has not been edited.

## Algebra checked

- The common triangular domain and added strip in the one-parent increment are exact. With `q=D-s`, the shrinking long parent contributes `-delta U_(q-1)`; all indices remain in range at `s=1` and `s=k-2`. The normalization identity and paired strip identity have the stated signs.
- For Lemma 1, direct division gives M251's coefficient increment. The likelihood ratio lies in the stated interval, so the common-domain absolute sum is below `2/R`; the only possible new atom is `d=r-1`, of mass at most `1/R`. This proves `3/R`, including empty cases. The log-derivative estimates imply the displayed `120 d/r` coefficient remainder and hence `120 sqrt(t)/(Rr)` after the Borel/Stirling sum.
- In Lemma 2, the near/far split conditions hold simultaneously for the paired long parent. The leading `B_t/R` terms cancel. The survivor variation is at most `4 sqrt(t)`, and the normalization contribution is at most `16/3`. The actual denominator bound is valid: at `k=3`, `H_1=1/2` and `H_2=2/9`; for `k>=5`, `H_s >= (D-6)/(D-2) >=3/7`. Thus `2300 sqrt(t)` is safe.
- The three displayed seam profiles follow directly from the accepted three-gap incidence law. Their changes are confined to an initial jump, a slope interval, and at most two cutoff jumps; direct bounds give weighted variation below the claimed `8 sqrt(ell)` in all three regimes, including empty ranges.
- The finite Abel identity has the stated minus sign because `1{d>t}=1-e_t(d)`. Since `L_s(1)=2`, constants are annihilated, and `2300*8=18400` proves exactly `Y-DV`.
- Subtracting the literal `Y` tuple formula from `X` leaves exactly the complementary two-run indicator in M251 (5.1). Therefore the displayed `TAV` is the sole remaining obligation for the `X` clause of `DV`; it is not proved here and gives no downstream inference.

No material objection has been found. A compact bounded exact/algebra checker and frozen report remain to be written.
