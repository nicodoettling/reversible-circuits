# M192 Checkpoint

## Start checkpoint

- The owned M192 plan and checkpoint were initialized before substantive work.
- The reversible-circuit-sampler skill and required source-of-truth references
  were read for this assignment.
- The target, convention, exact prefix claim, computation cap, and prohibited
  downstream inferences are fixed in `plan.md`.
- Next gate: verify immutable M180/M182 and M186/M189 manifests. No conclusion
  on `(PCR)` or `(WPCR)` has yet been adopted.

## First substantive checkpoint

### Immutable gate

Every entry in the frozen M180, M182, M186, and M189 checksum manifests
passed before derivation. No predecessor was edited.

### Exact shared-endpoint coefficient

Let `p_s` and `q_s` be M91's B/A laws of the first smaller exterior split,
with `q_s=0` above `(k-1)/2`. After a first chord splits an active cycle into
sizes `a,b`, the second factor shares an endpoint with it exactly when it is
an internal chord incident to the marked endpoint in either new component.
The Cayley convolution

```text
sum_(c=1)^(r-1) tau(c)tau(r-c)=2(r-1)tau(r)/r
```

therefore gives the exact conditional triangle probabilities

```text
gamma_L(s)=2[2-1/s-1/(2k-1-s)]/(2k-3),
gamma_F(s)=2[2-1/s-1/(k-s)]/(2k-3).                 (G)
```

The first is for B's `(2k-1)`-cycle; the second is for the A cycle cut by
the first chord, with the untouched `k`-cycle retained in the denominator.
Summing over the split laws recovers

```text
sum_s p_s gamma_L(s)=3/(2k-1),
sum_s q_s gamma_F(s)=3(k-2)/[k(2k-3)].              (TM)
```

Thus every shared-endpoint triangle, including repeated small component
sizes, contributes `O(1/k)` to either prefix observable because each counts
at most three components. This is already stronger than the required
`O(sqrt(ell)/k)` scale for `ell>=2`.

### Exact disjoint-pair Abel reduction

For `Z` equal to either

```text
X_ell=sum_(2<=d<=ell)[N_1(d)+N_2(d)],
Y_ell=sum_(2<=d<=ell)N_1(d),
```

let `Phi_s^D(Z),Psi_s^D(Z)` be the normalized B/A expectations conditioned
on the first split `s` and a disjoint second edge. These literal profiles
retain same-run and cross-run doubles, both colors, unit gaps, and all size
collisions. Put

```text
p_hat_s=p_s[1-gamma_L(s)],
q_hat_s=q_s[1-gamma_F(s)],
E_u=sum_(s<=u)(p_hat_s-q_hat_s).
```

Finite signed summation by parts gives the exact double-prefix contrast

```text
R_ell^D=E_(k-1)Phi_(k-1)^D(Z)
 +sum_(u=1)^(k-2)E_u[Phi_u^D(Z)-Phi_(u+1)^D(Z)]
 +sum_(s<k/2)q_hat_s[Phi_s^D(Z)-Psi_s^D(Z)].         (DA)
```

The endpoint is explicit:

```text
E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)]=O(k^-2).           (EP)
```

Uniform critical-Borel ratio estimates give

```text
|sum_(s<=u)(p_s-q_s)|<=C sqrt(u)/k.
```

Since both gamma coefficients are `O(1/k)`, this proves the sharper scalar
weight bound

```text
|E_u|<=C sqrt(u)/k,              1<=u<=k-1.         (EW)
```

### Precise remaining obstruction

By `(DA)`--`(EW)`, the disjoint-pair `J=2` prefix estimate follows from the
two explicit profile bounds, for `Z=X_ell,Y_ell`,

```text
sum_(u=1)^(k-2)sqrt(u)|Phi_u^D(Z)-Phi_(u+1)^D(Z)|
 <=C sqrt(ell),                                      (DV)

|sum_(s<k/2)q_hat_s[Phi_s^D(Z)-Psi_s^D(Z)]|
 <=C sqrt(ell)/k.                                    (DE)
```

`(DV)` is a weighted split-variation estimate; `(DE)` is a signed
deletion/merge embedding response. Neither is proved. They are strictly
narrower than `(PCR)`: the shared-endpoint law, scalar Borel mismatch, and
endpoint mass have been discharged, while every kind and collision remains
inside the literal profiles. No `(SCBR)` or downstream inference is made.

## Final checkpoint

- The coordinator cap was honored after isolating `(DV)` and `(DE)`; neither
  lemma nor `(PCR)` was pursued further.
- A compact exact checker capped at `k=3,5,7` verifies the shared-endpoint
  coefficient, triangle masses, disjoint Abel endpoint, and prefix identity.
- Final verdict is a strict exact reduction. `(DV)`, `(DE)`, conditional
  `J=2` prefix, full `(PCR)/(WPCR)`, and all downstream claims remain open.
- Final parse, hygiene, manifest, and hash validation are recorded in the
  freeze files.

