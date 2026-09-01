# M178 fresh immutable referee report on frozen M174

Date: 2026-08-13 UTC.  Audited repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, convention, and scope

```text
ACCEPT M174'S STRICT PCS BOUNDARY-RESPONSE REDUCTION.
MATERIAL NUMBERED OBJECTIONS: ZERO.
NONMATERIAL NUMBERED OBJECTIONS: TWO.
PCS-BOUND AND (BR): UNRESOLVED.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  The target is only M73's nonlazy cyclic rank-two quotient
under the uniform minimal long-cycle factorization law, for `n=3k`, odd
`k>=3`, at the balanced sources and first fixed separated cell.  This is not
the global identity-word law or the `{3,4,5}` heat-bath chain.

## 2. Frozen provenance

Before mathematical use, `sha256sum -c SHA256SUMS` passed all eight declared
M174 payloads.  The independently observed hashes were:

| M174 artifact | SHA-256 |
|---|---|
| `plan.md` | `eed3871e78171e5a9ad4ecbfd736911162b64228afae85d657e668becd793e86` |
| `checkpoint.md` | `99ee874ed1057500a221d688bea553d8de4a959a28885b809fd7915c15ac7572` |
| `proof.md` | `a950556ea97acdf0507d76e35e20e3d19f75fd34b7e7557acd9ce0f17bbc7326` |
| `pcs_channel_calibration.py` | `eb6bc4f535d53affe87e23c8c4601396c8e5d79f7f55961b1686a1092c25b461` |
| `pcs_channel_exact.json` | `2d103e07bfb834902f790aedf7102a9260a856bfde4551b041a1748cf73d9924` |
| `results.json` | `2e41d26874ed64754ceb26aa3c5278020ac09ab134807bb634d50609de01bc04` |
| `report.md` | `69b10c764620f9ccfe65491fb37fbefadf6c0eac27cb63a8c2b9635dbe00dacb` |
| `freeze_manifest.md` | `f346d050476912f02728a130fb97b1ee21e1717bd099ce8930c06397860e3de8` |
| `SHA256SUMS` itself | `fea1f624d6b65fb8404eee0324832aa601e1bf4f202598b60a6608b1a23a51ba` |

M174 was never edited during this audit.

## 3. Exact probability, normalization, and covariance interface

The literal first-pair product law is correctly

```text
P_g(s)=a(s)F_(n-5)((gs)^-1h)/F_(n-3)(g^-1h),
```

and the phase-collapsed response is `f(s)=S(s)/A_s`.  Therefore

```text
Delta(C_k)=E_(P_B)f-E_(P_A)f.
```

M168's accepted physical-cell identity and the exact completion count give

```text
sum_y z_k(y)=2Delta(C_k)/pi_y,
pi_y=2/(n-2)(1-2/n)^(n-3).
```

Since `n=3k` and the exponential factor is bounded above and below by
absolute positive constants for `n>=9`, PCS-bound is equivalent to
`n^2|Delta(C_k)|=O(1)`.

The common `J=0` submeasures cancel exactly.  For the normalized symmetric
channel law `mu_j` and signed likelihood ratio `sigma_j`, one has
`E_(mu_j)sigma_j=0` and hence

```text
Delta(C_k)=2 sum_(j=1)^2 alpha_j Cov_(mu_j)(f,sigma_j).
```

This is a signed expectation identity, not a Poincare estimate.

## 4. Exact `U,V` and cycle-index response

The one-run decorations

```text
U_1=(d-1)tau(d-1)/tau(d),
V_1=(d-2)(d-3)tau(d-2)/tau(d),
```

and the positive two-run decorations

```text
U_2=(d-2)tau(d-1)/tau(d),
V_2=((d-2)(d-3)-2[(a-2)_+ +(b-2)_+])tau(d-2)/tau(d)
```

follow exactly from the generic-edge and adjacent-pair counts.  With
`R_n=(n-3)(n-4)`, they give

```text
f(s)=R_n^-1[sum_i V_i+2sum_(i<j)U_iU_j].
```

The shifts

```text
sum tau(d)U_1(d)z^d=z^2T'(z),
sum tau(d)V_1(d)z^d=z^4T''(z)
```

are exact.  The two-run term is the stated bivariate positive-composition
convolution, including every `(a-2)_+` and `(b-2)_+` boundary term.

## 5. Uniform residual bounds and affine response

The one-sentence estimate in M174 can be completed rigorously.  Factorial
cancellation and logarithm remainders give, uniformly,

```text
e tau(d-1)/tau(d)=1+3/(2d)+O(d^-2),
e^2 tau(d-2)/tau(d)=1+3/d+O(d^-2).
```

For two positive runs, setting
`I=1[a=1]+1[b=1]` gives the exact numerator

```text
D_2=d^2-7d+14-2I,
```

with `0<=D_2<=d^2`.  Hence

```text
v_2=-7-2I+(42-6I)/d+D_2 O(d^-2),
```

uniformly over all `a,b>=1`.  The same calculation gives bounded `u_1,u_2`
and `v_1=-9+18/d+O(1)`.  `proof_audit.md` records explicit remainder
constants and treats the finite invalid-subscript cases.

The pointwise deterministic linear response is exactly

```text
L_T=0,                 L_D=-2.
```

For a triangle, `-2n` and `+2n` cancel.  For a double with two-run size
`d_*`, the `V` linear term is `-2n-2d_*` and the epsilon-cross term is
`+2d_*`.  This explicitly rejects the transient `7/5` interpretation, which
cannot arise from the correct pointwise kind expansion.

## 6. Kind transfer, reduction, and boundary lemma

M91's exact channel mass is

```text
alpha_2=2(2k-3)/[3(3k-4)].
```

The triangle-probability difference is

```text
3/(2k-1)-3(k-2)/(k(2k-3))
=6(k-1)/[k(2k-3)(2k-1)].
```

Therefore M174's simplification, including its denominator, is correct:

```text
eta(T)=12(k-1)/[3k(3k-4)(2k-1)],
eta(D)=-eta(T).
```

`J=0` cancels as a measure and `J=1` has zero kind transfer.  Applying the
signed source measure to the affine response gives exactly

```text
Delta(C_k)=e^-2/R_n [2n eta(T)+eta(B_k)].
```

Because `2n eta(T)=O(1)` and `R_n` is uniformly comparable with `n^2`, this
proves both directions of

```text
PCS-bound  iff  eta(B_k)=O(1).
```

The boundary-response estimate itself remains unresolved.

## 7. Independent exact/literal reconstruction at `k=3,5`

The clean-room checker imports no M174 code.  It reconstructs the two source
laws from literal ordered first and second transpositions, computes the PC
response by a literal sum over every ordered disjoint boundary-edge phase,
and independently computes the decorated response.  It reads frozen M174
JSON only after those calculations.

| check | `k=3` | `k=5` |
|---|---:|---:|
| distinct source-accessible intermediates | 64 | 810 |
| triangle run profile | `(1,1,1)` | `(1,1,1)` |
| double run profile | `(1,1,2)` | `(1,1,2)` |
| literal/decorated response | exact match | exact match |
| affine/reduction identity | formal-polynomial match | formal-polynomial match |
| frozen event and signed-cell values | exact match | exact match |

The exact triangle transfers are `8/75` and `16/495`.  The exact event
contrasts and signed cell sums match M174 byte-for-value after clean-room
computation.  These checks are finite calibration only; no sign or
asymptotic claim is inferred.

## 8. Numbered objections and status ledger

1. **Nonmaterial exposition gap, repaired here:** M174 asserts uniform
   boundedness of `u_1,v_1,u_2,v_2` using “standard elementary estimates”
   without displaying a remainder or explicitly simplifying the two-run
   boundary numerator.  The assertion is correct; the explicit uniform proof
   in `proof_audit.md` closes the presentation gap.

2. **Nonmaterial wording limitation:** M174 correctly identifies the two-run
   contribution as a bivariate positive-composition convolution but does not
   display a further closed bivariate generating series.  Its exact `U_2,V_2`
   formulas and `(BR)` reduction do not require such a series.  Do not promote
   the report as having solved that coefficient extraction.

Material objections: **none**.

```text
P_g/f/Delta and pi_y normalization                       proved
J0 cancellation and two-channel covariance identity     proved
U,V response and one-run cycle-index shifts              proved
uniform u1,v1,u2,v2 bounds                               proved in audit
affine constants L_T=0,L_D=-2                            proved
kind transfer and its simplified denominator             proved
Delta reduction and equivalence with (BR)                proved
clean-room k=3,5 values                                  exact finite facts
(BR), PCS-bound, FD-bound, and FCL1                       unresolved
```

## 9. Artifacts, reproducibility, hygiene, and final action

The stable deterministic command is

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-41/mission-M178-m174-fresh-referee/cleanroom_pcs_audit.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-41/mission-M178-m174-fresh-referee/cleanroom_results.json \
  --frozen-m174 experiments/20260811-polynomial-mixing-resolution/cycle-40/mission-M174-fixed-cell-pcs-bound/pcs_channel_exact.json
```

Python `3.12.3`; standard library only; deterministic; `seed=null`; exact
scope `k=3,5`.  M178 changed only its owned directory.  No predecessor,
coordinator, manuscript, skill, or shared project file was edited.

**Final action: accept and freeze M174's strict boundary-response reduction
with zero material and two nonmaterial objections.  Keep `(BR)`, PCS-bound,
FD-bound, FCL1, every gap/mixing claim, and both Terminals open.**
