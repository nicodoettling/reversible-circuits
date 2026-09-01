# M311 Analytic Attempt at QBP_1

Date: 2026-08-14 UTC
Status: QBD_1 proved; QBP_1 remains unresolved before the authorized guard

## 1. Canonical prefix potential

For `0<=h<=k-1`, define

```text
Phi_h(k,u,ell)
 = integral_0^(M_h)[mathsf X(t)-mathsf Y(t)]dt
 = sum_(pi_cd>0, min(c,d)<=h) pi_cd D_cd,
M_h=max(A_h,B_h),
Phi_0=0.                                                    (1.1)
```

The equivalence follows from the exact rung characterization `(4.2)` in
`staircase_identity.md`.  If a maximal constant-sign run of `R_h` is
`H_q=[a_q,b_q]`, then

```text
C_q=Phi_(b_q)-Phi_(a_q-1).                                 (1.2)
```

Thus QBP_1 is equivalently monotonicity of `Phi` only across the canonical
sign-run endpoints.  It does not require cellwise or every-rung prefix
monotonicity.

## 2. What coefficient geometry proves and does not prove

The signs of `R_h` determine the direction of every off-diagonal rung and
which cumulative endpoint realizes `M_h`:

```text
R_h<0 => M_h=B_h and c>d off the diagonal;
R_h>0 => M_h=A_h and c<d off the diagonal;
R_h=0 => M_h=A_h=B_h and no off-diagonal rung-h cell.
```

This proves the block partition, but it does not sign `(1.2)`.  Indeed,
QTI_1 plus the marginal and support constraints alone permit arbitrary real
values for the finitely many `D_cd`; assigning a negative value on one
block and zero elsewhere preserves every coefficient identity while making
that block negative.  Any proof of QBP_1 must therefore use the literal
owner-response structure, not only the Hahn masses or Abel signs.

## 3. Literal owner response does not close termwise

For each exterior/middle double, the accepted response is a sum over generic
positions of

```text
b_i                         for two points in the same owner i,
a_i a_j                     for points in distinct owners i,j,
a_i=tau(d_i-1)/tau(d_i),    b_i=tau(d_i-2)/tau(d_i).
```

Across even one sign block, changing the exterior cut changes the three owner
sizes, which positions are generic, same-owner interval overlaps, and the
normalization of the cross/internal/seam means.  The block coefficients do
not pair these terms owner-by-owner with a fixed sign.  The accepted `k=9`
QCP obstruction already rules out replacing the full block by independent
cell signs.

No inequality among `a_i,b_i` found in the accepted interface compares the
complete positive and negative owner fields after these simultaneous
changes.  Consequently the analytic proof stops at the standalone weighted
owner statement QBP_1; assuming it here would merely rename the missing
step.

## 4. Authorized next action

QBP_1 is narrow, explicit, and falsifiable.  Since the owner term cannot be
signed analytically from the accepted inputs, execute exactly the frozen
`k=11` guard.  If it fails, retain QBD_1 and record the first exact block
counterexample.  A positive guard would remain finite only.
