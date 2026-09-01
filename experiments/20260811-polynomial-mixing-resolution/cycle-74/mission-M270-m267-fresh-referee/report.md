# M270 fresh immutable referee report on M267

Date: 2026-08-14 UTC.

## 1. Verdict, target, convention, and scope

```text
VERDICT: ACCEPT M267 AS FROZEN.
LITERAL ENDPOINT-PROFILE/REFLECTION REDUCTION: PROVED.
UNIFORM STATEWISE SUM_ell |E_ell(s)| <=1232/e^2: PROVED.
SET / SR / TPR / PBV / FD / FCL1: UNRESOLVED.
```

The accepted theorem is uniform for odd `k>=3`, `n=3k`, in the balanced
first fixed cell of the auxiliary minimal-long-cycle factorization law under
the nonlazy cyclic rank-two quotient kernel, using `(pq)(x)=p(q(x))`.  It is
not a theorem about the global identity-word law or the lazy exact
same-product `{3,4,5}` heat-bath chain.

## 2. Frozen provenance

All eight M267 payloads pass, and the SHA-256 digest of its checksum file is

```text
001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6.
```

Every cited M91/M94, M161/M166, M168/M171, M256/M259, and M261/M264
inventory also passes; exact digests are recorded in `hash_audit.md`.  The
known M166 freeze-manifest hash independently recomputes to the accepted
corrected value.  No predecessor was edited.

## 3. Null-owner tensor and exact normalization

Extending the residual owner by `empty` at support heads and setting every
null-owner `kappa` coefficient to zero gives, exactly,

```text
E_ell(s)=sum_x [kappa(o(x-ell),o(x+1))
                 -kappa(o(x-ell),o(x))].
```

Only literal owner jumps contribute.  The phase-averaged endpoint signature
records enough owner sizes/equalities to determine each charge.  Averaging
over all `n` phases is representative-independent even for short orbits and
gives

```text
nu(E_ell)=n sum_K <w,Gamma_(nu,K,ell)>.
```

M91's `p_u,q_u` divisions normalize both channels exactly.  The fair
separate-component choice is explicit in channel one and already contained
in channel two's raw ordered-pair completion law.  Triangle/double kinds,
ordered lifts, seams, collisions, and both source channels are retained.
Applying the profile map to the complete Abel identity proves

```text
eta(E_ell)=alpha_1 Xi_(1,ell)+alpha_2 Xi_(2,ell)
          =n sum_(K in {T,D})<w,T_(K,ell)>.
```

## 4. Reflection and PBV/SET equivalence

The symmetric owner correlation satisfies `F_ell=F_(n-ell)`.  Therefore,
pointwise,

```text
E_ell=-E_(n-ell-1),       E_((n-1)/2)=0.
```

The involution preserves `2,...,n-3`; its lower half is precisely
`2,...,(n-3)/2`.  The outside factor `n` then makes PBV exactly equivalent,
up to the reflection factor two, to M267's named half-profile estimate

```text
(SET)  sum_(ell=2)^((n-3)/2)
       |sum_K<w,T_(K,ell)>|=O(n^-2).
```

`(SET)` itself remains open.

## 5. Statewise lag-variation envelope

Each owner set has at most four circular boundary jumps, so every owner-pair
correlation has variation at most four times the smaller owner-set size.
The exact Cayley-tree ratios satisfy, including invalid small shifts,

```text
|e^2 kappa_ii-1|<=20/d_i,
|e^2 kappa_ij-1|<=20(1/d_i+1/d_j).
```

The three diagonal correlations contribute at most `240`; the six ordered
off-diagonal correlations contribute at most `960`.  The support-head
collision histogram contributes at most `32`.  Combining these with the
exact affine derivative gives, for every supported triangle or double,

```text
sum_(ell=2)^(n-3)|E_ell(s)|<=(240+960+32)/e^2=1232/e^2.
```

This removes a possible statewise factor `n`, but it does not provide PBV's
additional signed `1/n` gain.

## 6. Conditional SR/TPR route and firewall

If the unresolved one-threshold signs `(SR)` held, lower-half telescoping
and reflection would give exactly

```text
sum_ell |eta(E_ell)|
 =2(n-3)(n-4)
  [G_2+G_((n-1)/2)-2G_(k-1)].
```

Thus, conditional on `(SR)`, PBV is equivalent to the bracket being
`O(n^-3)`, namely `(TPR)`, or to the corresponding three `z_k` scores being
`O(n^-2)`.  Neither `(SR)` nor `(TPR)` is proved or promoted.

M264's firewall remains decisive.  The two `k=3` products have identical
residual size/run profile `((1,1),(2,1),(6,2))` but endpoint values
`-625/1296` and `-20/81`.  Accepted `X_D,Y_D` cutoff profiles therefore do
not determine `E_ell` and cannot replace the literal endpoint tensor.

## 7. Independent checker

`independent_check.py` contains no import statement and reads no predecessor
code or data.  It exhaustively checks 336 supported products at `k=3` and
3,185 at `k=5`, including null owners, jump/correlation equality, the factor
`n`, all reflection indices, central zero, interval variation, the statewise
bound, kind counts, and the M264 witness.  It also checks exact split/channel
mass normalization and synthetic `(SR)=>(TPR)` endpoints at five odd ranks,
plus finite Cayley-ratio boundary guards.

The retained output reproduces M267's exact maximal statewise values
`16/3` and `20014594024/2357947691`.  These computations are finite
falsification only and do not prove any asymptotic sign or transport bound.

## 8. Numbered objections and status ledger

1. Material objections: none.
2. Nonmaterial objections: none.
3. Scope guard: a statewise `O(1)` envelope cannot be inserted after
   absolute Abel/source masses to obtain PBV; all signed channel, kind,
   split, and endpoint cancellation is still required.

```text
M267 and cited inventories                                  verified
null-owner endpoint formula and outside phase factor n      proved
two-channel/T-D endpoint transport tensor                    proved
reflection, central zero, and PBV iff half-profile SET       proved
uniform statewise 1232/e^2 envelope                          proved
M264 size/run-profile firewall                               proved obstruction
finite k=3,5 and boundary checks                             exact/finite only
SET, SR, TPR, PBV, FD-bound, minority sign, FCL1             unresolved
gap, polynomial mixing, Terminal                             unresolved
```

## 9. Exact stop, artifacts, and final action

The first unproved endpoint statement remains `(SET)`.  `(SR)` and `(TPR)`
are a separate conditional route, not consequences of the accepted
representation.  No FD-bound, minority-sign theorem, FCL1, all-cell/direct
L1 bound, H0 result, bridge spectral gap, polynomial mixing, or Terminal
follows.

Artifacts are the plan/checkpoint, immutable hash audit, proof audit,
no-import checker and retained results, this nine-field report, run manifest,
freeze manifest, and `SHA256SUMS`.  Final action: **accept M267 at its exact
auxiliary scope and continue from `(SET)` or an independently proved
`(SR)+(TPR)` route; reject every downstream overreach.**

