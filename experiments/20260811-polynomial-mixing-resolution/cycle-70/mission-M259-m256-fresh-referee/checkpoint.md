# M259 Checkpoint

Status: substantive normalization audit complete; final interface pass in
progress.

The mission is locked to fresh, immutable review of M256. M256's complete
nine-file inventory passes and the SHA-256 digest of its `SHA256SUMS` is

```text
f55b7092a1cc079a8c2d46e978f42772b7c3b5d1747cede45c34d38547524261.
```

All 22 cited predecessor inventories M161, M166, M168, M171, M174, M178,
M180, M182, M186, M189, M192, M195, M217, M222, M235, M238, M239, M246,
M248, M249, M252, and M253 pass; every checksum-file digest matches M256's
dependency table.

One supplementary hash in M256's prose is a transcription error. The actual
M166 freeze-manifest hash is
'a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897f28dfbb6185e30498',
also recorded in the coordinator ledger, rather than M256's
'a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897bb59d63b40705aa9a'.
The latter visibly splices the correct prefix with the tail of M166's report
hash. This is a nonmaterial provenance transcription objection: M166's
checksum-file digest and every inventoried payload still pass.

## Normalization findings

1. M252's channel-one weighted functional is at most
   `3(2K_1+K_2)/k`; channel two is at most
   `6(K_E K_V+7185)/k`. Multiplying by `n=3k` gives exactly
   `18K_1+9K_2+18(K_E K_V+7185)`. There is no hidden `K/n` versus `K/k`
   conversion. The conditional `J=2` prefixes precede multiplication by
   `alpha_2`, while the nonnegative source-independent masses and common
   `J=0` cancellation license the full mixture.
2. With odd `n=3k`, `m=(n-1)/2=floor(n/2)` is the exact small-component
   endpoint. M186's Abel identity retains the singleton
   `M_1(1)u_1(1)`, the endpoint `A_m u_2(m)+C_m r_m`, and every interior
   first difference. Its accepted `M_1(1)=O(1/n)`, `O(1/d)` endpoint
   response, and `O(1/d^2)` first differences make full WPCR sufficient for
   SCBR; PCR and J1-PCR are unused.
3. M180's accepted absolute large-component tail is `O(1/n)`, so SCBR
   gives `eta(Q)=O(1/n)`. The exact bounded-remainder relation
   `eta(B_k)=2n eta(Q)+O(1)` gives BR, and the boundary-incidence identities
   give the two-way BR/BIR normalization at scales `O(1)` and `O(n^-2)`.
4. M174's exact affine response is
   `Delta(C_k)=e^-2[(2n eta(T)+eta(B_k))/R_n]`, with
   `2n eta(T)=O(1)` and `R_n=(n-3)(n-4) asymp n^2`. Thus BR gives the
   physical `Delta(C_k)=O(n^-2)`. Since
   `pi_y=2(n-2)^-1(1-2/n)^(n-3) asymp n^-1` and `k=n/3`, this is exactly
   PCS-bound; M174/M178 also prove the reverse implication, although M256
   only needs the forward direction.
5. PCS controls only `k|sum_y z_k(y)|`. M168's exact inequality has the
   independent term `(n-3)k sum_y|Delta z_k(y)|`; controlling it requires
   `k^2 sum_y|Delta z_k(y)|=O(1)` because `(n-3)/k<=3`. Therefore PCS alone
   does not imply FCL1 or `A_k(1,1)=O(1)`. FD-bound, or M168's distinct
   minority-sign hypothesis, remains mandatory. M161/M166's normalization
   `A_k(1,1)=k(n-3)^-1 sum_y|Z_k(y)|` makes FCL1 and bounded first-cell
   scalar equivalent, but does not prove either.

No material normalization objection has been found. This checkpoint makes
no DV/FD, gap, mixing, or Terminal claim.
