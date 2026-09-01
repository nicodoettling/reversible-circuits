# Fresh immutable audit request for M282

Please audit frozen M282 independently and do not edit it.

## Required gates

1. Verify every M282 checksum and every cited M272/M276/M279, M192/M195,
   M217/M222, and M248/M249 inventory.
2. Reconstruct the endpoint-bearing Abel collapse
   `CSBV=sum_s(p_hat_s-q_hat_s)Phi_s^D`.
3. Derive the literal raw kernel `U_r(x)` from completion weights, retaining
   ordered factors, both components, disjoint kind, phase, and collisions.
4. Independently verify the abstract coefficient `(3.1)` and both-seam
   ambient phase map `(4.1)`, including `c_0,c_k` padding and the nonzero Abel
   endpoint.
5. Audit Lemma 1 in detail: `r=1,2`; both Borel half-ranges of `e_r`; the
   `d=r-1/r` cutoff; inactive tail; reflected support; and zero endpoints.
6. Verify the exact cancellation
   `sum W=-sum q(a_F/a_L-1)=O(k^-2)` and that the common profile is removed
   before every norm.
7. Verify the low/bulk/junction/endpoint proof of `TV(A)=O(1/k)`, explicitly
   including `k=3`.
8. Check that the final embedding inequality gives the exact restricted
   CSBV lag norm and that no CEBV or downstream claim is inferred.

The most important possible objection is a hidden `O(1)` endpoint or cutoff
inside the claimed `O(1/R)` stabilization error. A clean-room coefficient
reconstruction is preferred. The retained finite checker is calibration,
not proof.

