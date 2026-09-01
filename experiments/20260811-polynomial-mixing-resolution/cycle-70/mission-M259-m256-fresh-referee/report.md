# M259 fresh immutable referee report on M256

Date: 2026-08-14 UTC.

## Verdict

**ACCEPT M256's conditional theorem through PCS-bound, with zero material
objections and one nonmaterial provenance correction.**

Uniformly for odd k at least 3, in the auxiliary minimal-long-cycle
fixed-cell model with n=3k, full DV plus accepted DE implies

~~~text
full WPCR => SCBR => BR <=> BIR => Delta(C_k)=O(n^-2)
          <=> PCS-bound.
~~~

Full DV remains an explicit unresolved hypothesis. This is not a theorem
about the identity-word law or the lazy exact same-product {3,4,5}
heat-bath chain.

## Exact implication audit

1. M192's J=2 observables are exactly the conditional A and C prefixes. Its
   shared-endpoint and unequal-disjoint-mass endpoint terms are retained.
   Full DV controls its Abel variation; accepted M248/M249 DE contributes
   7164. The resulting channel-two constant is K_E K_V+7185.
2. The channel-one Hardy functional is at most 3(2K_1+K_2)/k and channel two
   is at most 6(K_E K_V+7185)/k. The nonnegative, source-independent channel
   masses and common J=0 cancellation license their mixture. Multiplication
   by n=3k gives exactly
   18K_1+9K_2+18(K_E K_V+7185), with no K/n mismatch.
3. Odd n makes m=(n-1)/2=floor(n/2) the exact small-component endpoint.
   M186's Abel identity retains M_1(1)u_1(1), both endpoint prefixes, and all
   interior first differences. The accepted singleton, endpoint O(1/d), and
   first-difference O(1/d^2) bounds make WPCR sufficient for SCBR. PCR and
   J1-PCR are unused.
4. M180/M182's large-component tail is O(1/n). With SCBR it yields
   eta(Q)=O(1/n). The exact collision and bounded-remainder formula proves
   n eta(Q)=O(1) iff BR, and the boundary-incidence identities prove the
   two-way BIR normalization at O(n^-2).
5. M174/M178 retain the affine kind term 2n eta(T)=O(1) and divide by
   R_n=(n-3)(n-4), comparable with n^2. Hence BR is equivalent to the
   physical Delta(C_k)=O(n^-2). The exact target mass is comparable with
   1/n; together with k=n/3 this is PCS-bound in both directions.

## Mandatory stop at FD

PCS controls only the signed term k times the absolute total sum. M168's
deterministic closure has the independent term

~~~text
(n-3)k sum_y |z_k(y+1)-z_k(y)|.
~~~

It requires FD-bound at scale k^2, because (n-3)/k is at most 3, or M168's
separate minority-sign substitute. Thus PCS alone does not imply FCL1 or
A_k(1,1)=O(1). M161/M166's exact factor k/(n-3), between 1/3 and 1/2,
makes FCL1 and bounded first-cell scalar equivalent but proves neither.

## Objections and hashes

1. **Material objections:** none.
2. **Nonmaterial provenance correction:** M256 misprints the M166
   freeze-manifest hash. The correct value is
   a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897f28dfbb6185e30498,
   not
   a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897bb59d63b40705aa9a.
   M166's checksum-file digest and every inventoried payload pass, and the
   coordinator ledger already records the correct value.

M256's full inventory passes and its checksum-file digest is
f55b7092a1cc079a8c2d46e978f42772b7c3b5d1747cede45c34d38547524261.
All 22 cited predecessor inventories pass with the digests recorded in
hash_audit.md.

The compact independent checker passes. It is finite exact falsification
evidence only and attempts neither DV nor FD.

## Scope

This audit makes no DV/TAV proof, FD proof, gap, mixing, or Terminal claim.
Even adding FD would bound only the first auxiliary fixed cell.

