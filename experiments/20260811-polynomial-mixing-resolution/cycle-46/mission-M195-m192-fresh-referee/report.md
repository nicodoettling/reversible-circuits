# M195 report: fresh referee of immutable M192

Date: 2026-08-13 UTC. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Verdict, objections, and scope

```text
VERDICT: ACCEPT M192'S STRICT EXACT J=2 REDUCTION.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL NUMBERED QUALIFICATIONS: NONE.
```

Accepted: the exact Cayley convolution, shared-endpoint laws and masses,
complete triangle-prefix `O(1/k)` bound, endpoint-bearing disjoint Abel
identity, and universal scalar cumulative estimate. Not accepted or proved:
`(DV)`, `(DE)`, the conditional `J=2` prefix estimate, full
`(PCR)/(WPCR)`, `(SCBR)`, `(BIR)`, `(BR)`, PCS-bound, FCL1/direct-L1,
H0/gap, mixing, or either Terminal.

## 2. Immutable provenance and dependency gate

All eight entries in frozen M192's `SHA256SUMS` passed before any conclusion.
Fresh top-level hashes are

```text
report      005c63d4c2d8b86ec37855f91229dd668cd8e2c750ebfedd0ff1a789c572c3c7
proof       d2c609d7884dcd667e24d65bc653079479aef326daade0bf005917c6ac6b8399
manifest    92b7311587ef24bbeea6c02a9948c76a0fb95a13bae58b49db6090d51c526f31
checksums   4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60
```

M192 was never edited. Its proof and checker were inspected only after the
independent derivation and clean-room reconstruction.

## 3. Target, convention, and Cayley convolution

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, `n=3k` for odd
`k>=3`, `h=(0,1,...,n-1)`, `A=(0,k,2k)`, and
`B=(0,1)(k,2k)`. The target is the uniform minimal-factorization law of the
long cycle under the fixed-cell nonlazy cyclic rank-two coordinate kernel.

With `tau(r)=r^(r-1)/r!` and `T=ze^T`, Lagrange inversion independently
gives
```text
sum_(c=1)^(r-1)tau(c)tau(r-c)=2(r-1)tau(r)/r.
```
This is exactly the convolution required for the shared-endpoint completion
row.

## 4. Shared-endpoint coefficients and triangle response

After the first exterior edge creates marked pieces of sizes `a,b`, the
completion mass of internal second edges incident to a mark in a size-`r`
piece is `2(r-1)/[r(2k-3)]`. Summing the two marked pieces gives
```text
gamma_L(s)=2[2-1/s-1/(2k-1-s)]/(2k-3),
gamma_F(s)=2[2-1/s-1/(k-s)]/(2k-3).
```
The untouched A-side `k`-cycle belongs in the residual rank but supplies no
marked endpoint, so these numerators and the common denominator are exact.

The independently recovered masses are
```text
sum p_s gamma_L(s)=3/(2k-1),
sum q_s gamma_F(s)=3(k-2)/[k(2k-3)].
```
Both prefix observables lie in `[0,3]`; hence the complete signed
shared-endpoint response is `O(1/k)`. Literal multiplicities remain in the
observable, so this includes small-face collisions.

## 5. Disjoint endpoint and Abel identity

Removing shared endpoints without renormalization gives
`p_hat_s=p_s(1-gamma_L(s))`, `q_hat_s=q_s(1-gamma_F(s))`, and
`E_u=sum_(s<=u)(p_hat_s-q_hat_s)`. Their unequal total masses yield
```text
E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)].
```
The sign is negative and the size is `O(k^-2)`. Writing
`p_hat_s-q_hat_s=E_s-E_(s-1)` reproduces M192's finite Abel identity,
including the endpoint, followed by the signed embedding contrast. No
normalization, sign, or endpoint is missing.

## 6. Universal cumulative estimate and profile implication

Uniform Stirling ratios give, for `s<=k/2`,
```text
p_s+q_s<=C b_s,             |p_s-q_s|<=C(s/k)b_s,
b_s<=Cs^-3/2.
```
Thus the original cumulative is `O(sqrt(u)/k)) below the midpoint. Above
the midpoint it equals the negative long-cycle tail; the uniform bulk bound
sums to `O(k^-1/2)<=O(sqrt(u)/k)`. Since both exact gamma coefficients are
uniformly `O(1/k)`, the same bound holds for the disjoint cumulative:
```text
|E_u|<=C sqrt(u)/k.
```
This is a universal analytic estimate, not a finite-rank inference.

Combining it with proposed `(DV)` bounds the Abel variation term by
`O(sqrt(l)/k)`; proposed `(DE)` controls the embedding term. The endpoint
and triangles are already smaller. Because `Phi_s^D,Psi_s^D` are literal
ordered-double profile laws, all colors, same/cross-run kinds, unit gaps, and
collisions remain inside these two lemmas. They suffice exactly for the
conditional `J=2` prefix claim—not full `(PCR)`—as M192 states.

## 7. Clean-room exact check

`cleanroom_j2_audit.py` is self-contained, standard-library only, imports no
M192 code or data, and runs only exact `k=3,5`. It reconstructs the exterior
minimal-factorization recurrence, split laws, marked-endpoint events, literal
component profiles, disjoint submeasures, and Abel terms. All assertions pass.

| `k` | triangle masses `(B,A)` | endpoint | max `k|E_u|/sqrt(u)` | disjoint collisions |
|---:|---:|---:|---:|---:|
| 3 | `(3/5,1/3)` | `-4/15` | 1.0400 | 14 |
| 5 | `(1/3,9/35)` | `-8/105` | 0.83922032 | 132 |

The disjoint collision counts exactly match M192's convention; the audit also
retains 18 and 78 shared-endpoint collision events. It checks 18 exact Abel
identities over both prefix observables. These ranks are falsification only:
they prove no universal sign, constant, or asymptotic law.

## 8. Numbered objections and first open step

1. **Material objections:** none.
2. **Nonmaterial qualifications:** none.

M192 already distinguishes proved scalar cancellation from the two unproved
profile estimates and explicitly rejects a channelwise full-prefix inference.
The precise first open steps remain `(DV)` and `(DE)`; consequently the
conditional `J=2` prefix estimate and every downstream claim remain open.

## 9. Artifacts, hygiene, and action

Owned artifacts are `plan.md`, `checkpoint.md`, `proof_audit.md`,
`cleanroom_j2_audit.py`, `cleanroom_j2_results.json`, `results.json`,
this report, and the freeze files. Retained command:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-46/mission-M195-m192-fresh-referee/cleanroom_j2_audit.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-46/mission-M195-m192-fresh-referee/cleanroom_j2_results.json
```

Python `3.12.3`; standard library only; `seed=null`. No M192 import/edit,
`k=7`, DV/DE proof attempt, broad shell computation, finite-sign inference,
channelwise downstream claim, PCS/FCL1/direct-L1, gap/mixing, or Terminal
inference occurred. Final action: **accept and freeze only M192's strict exact
reduction; keep `(DV)`, `(DE)`, the `J=2` prefix estimate,
`(PCR)/(WPCR)`, `(SCBR)`, and everything downstream open.**
