# M268 fresh immutable referee report on M266

Date: 2026-08-14 UTC.

## 1. Verdict, target, convention, and scope

```text
VERDICT: ACCEPT M266 AS FROZEN.
FULL DV WITH K_V=18900: PROVED.
AUXILIARY FIXED-CELL RESPONSE THROUGH PCS-BOUND: PROVED.
FD-BOUND OR MINORITY-SIGN: EXACT REMAINING STOP.
```

The theorem is uniform for odd `k>=3`, `n=3k`, in the auxiliary
minimal-long-cycle first fixed cell under the nonlazy cyclic rank-two
kernel, with `(pq)(x)=p(q(x))`. It is not a theorem about the global
identity bridge or the lazy exact `{3,4,5}` heat-bath chain.

## 2. Frozen provenance

All ten files in M266's inventory pass; its checksum-file digest is
`6203ef0dca1e2c46696cec5bc1446da9656ace2b8a3a4ce9b2131267b200c052`.
All fourteen direct predecessor inventories pass and their checksum-file
digests agree with M266's table. The complete delicate transitive source
and referee inventories also pass. M166's freeze-manifest hash independently
recomputes to
`a78b5ebb9546a409fdd31afd9e5d37c32db4afe495bb897f28dfbb6185e30498`,
confirming the known nonmaterial correction. No predecessor was edited.

## 3. Full-DV interface and constant

M251/M255 Y-DV and M258/M263 TAV use the same normalized literal B-side
ordered-disjoint-double profile, odd-`k` domain, cutoff range
`2<=ell<=(3k-1)/2`, and adjacent-rank range `1<=s<=k-2`.
The identity `Phi(X)=Phi(Y)+Theta` is literal and pointwise. Taking its
adjacent difference first gives

```text
K_V=18400+500=18900.
```

There is no `q` or `qhat` average and no operator-orientation mismatch.

## 4. DE, Hardy/WPCR, and constants

Accepted DE is the original unnormalized `qhat`-weighted signed embedding
response, with common constant `7164`. M192's shared triangles and
unequal-disjoint-mass Abel endpoint remain separate. Thus

```text
K_J=18900K_E+7164+15+6=18900K_E+7185.
```

M252's exact Hardy transfer, the source-independent nonnegative channel
masses, and common `J=0` cancellation give

```text
C_W=18K_1+9K_2+18K_J
   =18K_1+9K_2+340200K_E+129330.
```

The factors `18,9,18` come exactly from `n=3k`. This is WPCR, not PCR;
J1-PCR is unused.

## 5. Singleton, endpoint, and first-difference audit

M186's exact SBP contains all of

```text
M_1(1)u_1(1),  A_m u_2(m),  C_m r_m,
A_d[u_2(d)-u_2(d+1)],  C_d[r_d-r_(d+1)].
```

WPCR supplies precisely `(|A_m|+|C_m|)/m` and the interior
`d^-2` weighted sum. The accepted estimates give `O(d^-1)` endpoints
and `O(d^-2)` differences. The singleton is a separate proved input,
`M_1(1)=O(1/n)`, with fixed finite `u_1(1)`. Hence every SBP term is
licensed and WPCR plus these accepted inputs proves SCBR. Neither endpoint
nor the singleton is hidden inside WPCR.

## 6. Tail, BR/BIR, affine response, and PCS

M180/M182's absolute large-component tail is `O(1/n)`. Together with
SCBR it yields `eta(Q)=O(1/n)`; the bounded remainder proves BR, and the
exact incidence normalization proves BR iff BIR at scale `n^-2`.

M174/M178 keeps `2n eta(T)` in the affine response and divides by
`R_n=(n-3)(n-4)`, uniformly comparable with `n^2`. Its exact event
normalization

```text
sum_y z_k(y)=2Delta_k(C_k)/pi_y,
pi_y=2/(n-2)(1-2/n)^(n-3)
```

with `pi_y` comparable to `1/n` and `k=n/3` proves in both directions

```text
Delta_k(C_k)=O(n^-2) iff k|sum_y z_k(y)|=O(1).
```

## 7. Odd-rank and `k=3` boundary

Odd `k` makes `n=3k` odd and
`m=(n-1)/2=floor(n/2)`, so no half-size component is omitted. At
`k=3`, the exact table is

```text
n=9, m=4, ranks={1}, cutoffs={2,3,4},
(alpha_0,alpha_1,alpha_2)=(1/15,8/15,2/5),
(H_1,H_2)=(1/2,2/9), Abel endpoint=-4/15.
```

All sums and endpoints remain defined; M258's exceptional
`ell=4>D-2` case is covered by the stated empty-sum convention.

## 8. Independent checker and numbered objections

`independent_check.py` imports no modules and reads no predecessor code or
data. It passes 1,000 odd-rank rows, 1,501,500 cutoff rows, 45,147 exact
Hardy rows, 100 exact synthetic SBP rows retaining singleton and endpoints,
1,000 response-scaling rows, and 50 exact target-mass rows.

1. Material objections: none.
2. Nonmaterial objections: none.
3. Scope guard: the checker is finite falsification only; the universal
   proof is the symbolic dependency audit in `proof_audit.md`.

## 9. Exact stop, artifacts, and final action

PCS is only a signed-total estimate. The independent FD-bound
`k^2 sum_y|z_k(y+1)-z_k(y)|=O(1)`, or the minority-sign substitute, remains
necessary for FCL1. This acceptance proves no PCR, FCL1, other fixed cell,
direct L1/all-edge bound, H0, bridge spectral gap, polynomial mixing, or
Terminal.

Artifacts are the plan/checkpoint, hash and proof audits, no-import checker,
machine-readable output, this report, run manifest, freeze manifest, and
`SHA256SUMS`. Final action: **accept M266 at its exact auxiliary scope and
continue only from FD-bound/minority-sign; reject every downstream
overreach.**

