# M192 report: channel-two prefix response

Date: 2026-08-13 UTC. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, target, and scope

```text
VERDICT: STRICT EXACT J=2 SHARED-ENDPOINT/DISJOINT-PROFILE REDUCTION.
DV, DE, CONDITIONAL J=2 PREFIX, PCR/WPCR, AND ALL DOWNSTREAM CLAIMS: OPEN.
```

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, `n=3k` for odd
`k>=3`, `h=(0,1,...,n-1)`, `A=(0,k,2k)`, and
`B=(0,1)(k,2k)`. The target is the uniform minimal-factorization law of the
long cycle under the fixed-cell nonlazy cyclic rank-two kernel. It is not the
global identity bridge or the lazy `{3,4,5}` heat-bath chain.

## 2. Immutable dependencies and starting point

Every entry in the frozen M180, M182, M186, and M189 checksum manifests
passed before derivation. None was edited.

M186/M189's accepted starting point is the complete `J=2` signed component
pushforward of `Lambda_L-Lambda_F`, where `L` is B's exterior
`(2k-1)`-cycle and `F` is A's pair of exterior `k`-cycles. It already
retains ordered triangles, same/cross-run doubles, both colors, unit gaps,
and repeated component sizes.

## 3. Exact shared-endpoint coefficient

Lagrange inversion gives the Cayley convolution

```text
sum_(c=1)^(r-1)tau(c)tau(r-c)=2(r-1)tau(r)/r.
```

After the first chord creates marked components of sizes `a,b`, summing the
next-factor completion ratio over internal chords incident to either mark
gives `2[(a-1)/a+(b-1)/b]/(2k-3)`. Therefore, conditioned on first smaller
split `s`,

```text
gamma_L(s)=2[2-1/s-1/(2k-1-s)]/(2k-3),
gamma_F(s)=2[2-1/s-1/(k-s)]/(2k-3).
```

Their exact total masses are

```text
sum p_s gamma_L(s)=3/(2k-1),
sum q_s gamma_F(s)=3(k-2)/[k(2k-3)].
```

Each prefix observable counts at most three components, so the entire signed
shared-endpoint contribution is `O(1/k)`, including all small-face
collisions.

## 4. Exact disjoint-pair Abel identity

Remove shared endpoints without renormalizing:

```text
p_hat_s=p_s[1-gamma_L(s)],
q_hat_s=q_s[1-gamma_F(s)],
E_u=sum_(s<=u)(p_hat_s-q_hat_s).
```

Let `Phi_s^D,Psi_s^D` be the normalized B/A component laws conditioned on
first split `s` and a disjoint second edge. These literal double laws retain
every kind and collision. For either prefix observable `Z=X_l,Y_l`, finite
summation by parts gives exactly

```text
R_D(Z)=E_(k-1)Phi_(k-1)^D(Z)
 +sum_(u=1)^(k-2)E_u[Phi_u^D(Z)-Phi_(u+1)^D(Z)]
 +sum_(s<k/2)q_hat_s[Phi_s^D(Z)-Psi_s^D(Z)].         (DA)
```

Because the disjoint submeasures do not have equal mass, the endpoint is
material and is retained:

```text
E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)]=O(k^-2).
```

## 5. Proved scalar cumulative bound

Uniform critical-Borel ratios yield, for the original split cumulative
`D_u=sum_(s<=u)(p_s-q_s)`,

```text
|D_u|<=C sqrt(u)/k.
```

On `u<=k/2`, this follows from
`|p_s-q_s|<=C(s/k)b_s` and `b_s<=Cs^-3/2`. Above `k/2`, normalization and
the long-cycle bulk tail give `|D_u|<=C/sqrt(k)`. Since both exact gamma
coefficients are `O(1/k)`,

```text
E_u=D_u-sum_(s<=u)[p_s gamma_L(s)-q_s gamma_F(s)]
```

proves uniformly

```text
|E_u|<=C sqrt(u)/k.                                  (EW)
```

This is a signed scalar cancellation; it would be lost by bounding the B
and A disjoint laws separately.

## 6. Precise first open lemmas

For `Z=X_l,Y_l`, `(DA)` and `(EW)` reduce the remaining conditional `J=2`
prefix estimate to:

```text
(DV)  sum_(u=1)^(k-2)sqrt(u)
        |Phi_u^D(Z)-Phi_(u+1)^D(Z)| <=C sqrt(l),

(DE)  |sum_(s<k/2)q_hat_s[Phi_s^D(Z)-Psi_s^D(Z)]|
        <=C sqrt(l)/k.
```

`(DV)` is a weighted adjacent-split variation estimate. `(DE)` is one
signed deletion/merge embedding response. Neither is proved. If both hold,
the endpoint, scalar Abel sum, embedding term, and shared endpoints give the
conditional `J=2` bound `O(sqrt(l)/k)`.

This report does not combine separate `J=1` and `J=2` absolute estimates to
claim full `(PCR)`, `(WPCR)`, or `(SCBR)`.

## 7. Compact exact diagnostics

`j2_prefix_check.py` is deterministic, standard-library only, and capped at
exact `k=3,5,7`. It checks the gamma coefficients, total triangle masses,
the nonzero endpoint, and `(DA)` for both prefix observables. It retains 14,
132, and 470 ordered collision events.

| `k` | max `k|E_u|/sqrt(u)` | max `(DV)` ratio | max `(DE)` ratio | max double-prefix ratio |
|---:|---:|---:|---:|---:|
| 3 | 1.0400 | 0.3464 | 0.6333 | 0.6034 |
| 5 | 0.8393 | 1.0483 | 0.4680 | 0.4956 |
| 7 | 0.8301 | 1.2453 | 0.4359 | 0.4908 |

All assertions pass. These three ranks merely fail to falsify `(DV)/(DE)`;
they establish no uniform constant, sign, monotonicity, or asymptotic law.

## 8. Strongest self-attack and unresolved claims

`(EW)` alone does not control `(DA)`: a prefix profile can oscillate rapidly
as the conditioned first split changes, making its weighted variation large.
Nor is `(DE)` a scalar Borel discrepancy; it compares the long exterior cycle
with two separated exterior cycles in the ambient long-cycle embedding.
Global component-count moments do not imply either estimate.

Thus the strict reduction is meaningful but incomplete. `(DV)`, `(DE)`, the
conditional `J=2` prefix estimate, full `(PCR)/(WPCR)`, `(SCBR)`, `(BIR)`,
`(BR)`, PCS-bound, FCL1/direct-L1, H0/gap, mixing, and Terminals remain open.

## 9. Artifacts, hygiene, and action

Owned artifacts are `plan.md`, `checkpoint.md`, `j2_prefix_reduction.md`,
`j2_prefix_check.py`, `j2_prefix_results.json`, `results.json`, this report,
and the freeze files. Retained command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-45/mission-M192-channel-two-prefix-response/j2_prefix_check.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-45/mission-M192-channel-two-prefix-response/j2_prefix_results.json
```

Python `3.12.3`; standard library only; `seed=null`. No broad quotient/shell
computation, final channelwise absolute split, finite-sign inference, or
downstream claim occurred. Final action: **freeze the exact gamma,
shared-endpoint, disjoint Abel, endpoint, and scalar cumulative results; keep
`(DV)/(DE)` and everything downstream open; request a fresh immutable audit.**
