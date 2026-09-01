# M217 exact signed-DE three-block reduction

Date: 2026-08-13 UTC.

Status: the exact reduction, its normalizer estimate, and the macroscopic-mass
lemma are **proved**. The weighted boundary-envelope lemma, hence signed
averaged DE, remains **unresolved**. IKBE-a/DV and every downstream claim
remain open.

## 1. Setting

Let `k>=3` be odd, `D=2k-1`, `R=2k-3`, `n=3k`, and

    b_d=e^(-d)d^(d-1)/d!,
    K_R(r,d)=b_d b_(r-d)/(R b_r),
    h(r)=(r-1)(r-2)/(rR),
    u=(k-1)/R.

For `Z=X_l,Y_l`, the original signed averaged deletion response is

    DE_Z=sum_(1<=s<k/2) q_hat_s
           [Phi_s^D(Z)-Psi_s^D(Z)].                   (1.1)

The profiles in (1.1) are the normalized literal disjoint ordered-double
laws of M199/M207. Thus both B/A signs and run channels, every same/cross
kind, the complementary two-run face, seams, and repeated-size collisions
remain present.

## 2. Exact signed weight and cancellation of the A normalizer

The normalized smaller first split in either A exterior `k`-cycle is

    q_s=[k/(k-1)] b_s b_(k-s)/b_k,
             1<=s<k/2,                               (2.1)

and `sum_s q_s=1`. Put

    gamma_L(s)=2[2-1/s-1/(D-s)]/R,
    gamma_F(s)=2[2-1/s-1/(k-s)]/R,
    a_L(s)=1-gamma_L(s)=h(s)+h(D-s),
    a_F(s)=1-gamma_F(s)=h(s)+h(k-s)+u.               (2.2)

The exact unnormalized disjoint A weight is

    q_hat_s=q_s a_F(s).                               (2.3)

Writing the literal profile numerators as `B_s^Z,A_s^Z`, substitution into
(1.1) cancels the A conditional normalizer exactly:

    DE_Z=sum_s q_s{[a_F(s)/a_L(s)]B_s^Z-A_s^Z}.      (2.4)

No probability renormalization has been introduced.

## 3. Literal Y blocks

Define

    W_r(f)=sum_(d=1)^(r-1)(r-d-1)K_R(r,d)f(d),

let `F_l` be the literal B two-seam incidence average, and put

    J_l(x)=(k-x)/k 1{2<=x<=l},
    C_l=sum_(d=1)^(k-1)(k-d)K_R(k,d)1{2<=d<=l}.      (3.1)

M199's exact formulas are

    B_s^Y=B_(s,surv)^Y+B_(s,frag)^Y,
    B_(s,surv)^Y=h(s)F_l(D-s)+h(D-s)F_l(s),
    B_(s,frag)^Y=W_s(F_l)+W_(D-s)(F_l),              (3.2)

    A_s^Y=A_(s,surv)^Y+A_(s,frag)^Y,
    A_(s,surv)^Y=h(s)J_l(k-s)+h(k-s)J_l(s)
                  +u[J_l(s)+J_l(k-s)],
    A_(s,frag)^Y=W_s(J_l)+W_(k-s)(J_l)+C_l.          (3.3)

Here `Phi_s^D(Y_l)=B_s^Y/a_L(s)` and
`Psi_s^D(Y_l)=A_s^Y/a_F(s)`.

Define the three signed blocks

    S_Y=sum_s q_s[B_(s,surv)^Y-A_(s,surv)^Y],
    K_Y=sum_s q_s[B_(s,frag)^Y-A_(s,frag)^Y],
    N_Y=sum_s q_s[a_F(s)/a_L(s)-1]B_s^Y.             (3.4)

Then (2.4) gives the exact identity

    DE_(Y_l)=S_Y+K_Y+N_Y.                            (3.5)

This is a signed identity: in particular, `S_Y` and `K_Y` are not bounded
separately by absolute values.

## 4. Literal X blocks

For `X_l`, let `B_(s,surv)^X,A_(s,surv)^X` denote exactly the surviving
one-run terms of the literal M199 numerators. Define

    B_(s,frag)^X=B_s^X-B_(s,surv)^X,
    A_(s,frag)^X=A_s^X-A_(s,surv)^X.                 (4.1)

Thus the fragmentation blocks in (4.1), by definition, retain every
remaining one-run term, the complementary two-run face, both seam
indicators, and all collision multiplicities. With

    S_X=sum_s q_s[B_(s,surv)^X-A_(s,surv)^X],
    K_X=sum_s q_s[B_(s,frag)^X-A_(s,frag)^X],
    N_X=sum_s q_s[a_F(s)/a_L(s)-1]B_s^X,             (4.2)

the same algebra proves

    DE_(X_l)=S_X+K_X+N_X.                            (4.3)

No X channel or kind has been removed; (4.1) is a partition of the literal
numerator, not a schematic replacement for it.

## 5. Uniform normalizer remainder

The ratio in the third block has the exact form

    a_F(s)/a_L(s)-1
      =[gamma_L(s)-gamma_F(s)]/a_L(s)
      =2(k-1)/[R(k-s)(D-s)a_L(s)].                  (5.1)

For `s<k/2`, `k-s>k/2`, `D-s>3(k-1)/2`, and
`a_L(s)>=h(D-s)>=1/2`; the last inequality is sharp at `(k,s)=(3,1)` and
follows directly from the displayed formula for `h`. Hence (5.1) is
`O(k^-2)` uniformly.

Both literal observables are nonnegative and at most three, so
`B_s^Z/a_L(s)=Phi_s^D(Z)<=3`, whence `B_s^Z<=3`. Since `sum_s q_s=1`,

    |N_Z|<=C/k^2,             Z=X_l,Y_l.             (5.2)

This estimate is signed-normalizer algebra; it invokes no pointwise bound
on `Phi-Psi`.

## 6. Macroscopic signed-mass lemma

### Lemma

Uniformly in odd `k` and `1<=m<k/2`,

    sum_(m<=s<k/2) q_hat_s <= C/sqrt(m).             (6.1)

Consequently, for fixed `epsilon>0`,

    sum_(epsilon k<=s<k/2) q_hat_s
       =O_epsilon(k^-1/2).                           (6.2)

### Proof

Uniform Stirling bounds give `b_r asymp r^-3/2`. For `s<k/2`,

    b_(k-s)/b_k <= C[k/(k-s)]^(3/2)<=C.

Also `0<=a_F(s)<=1` and `k/(k-1)<=3/2`. Equations (2.1)--(2.3) therefore
give `q_hat_s<=C b_s<=C s^-3/2`; summation proves (6.1), and
`m=ceil(epsilon k)` proves (6.2). QED.

Since the prefix observables are bounded by three, (6.2) controls an entire
macroscopic split region by `O(k^-1/2)`. When `l` is proportional to `k`,
this is the desired `sqrt(l)/k` scale. It does **not** reach the fixed-`l`
target `O(k^-1)`. Thus the `7/64` bulk-face limit found in M211 is not an
asymptotic obstruction after signed averaging, but the mass lemma alone
does not establish the needed cancellation either.

## 7. First open standalone lemma

> **SIGNED WEIGHTED BOUNDARY ENVELOPE (WBE), unresolved.** Uniformly in odd
> `k>=3`, `2<=l<=(3k-1)/2`, and `Z=X_l,Y_l`, the exact literal blocks above
> obey
>
>     |S_Z+K_Z| <= C sqrt(l)/k.                      (WBE)

Together with (5.2), WBE implies the original DE bound. It must preserve
the signed cancellation between the surviving and fragmentation blocks;
replacing it by `sum_s q_hat_s|Phi_s-Psi_s|` is invalid because M211/M215
refute the required pointwise estimate.

The exact endpoint term

    E_(k-1)=-6(k-1)/[k(2k-1)(2k-3)]

belongs to M192's outer Abel identity rather than DE itself. It remains
explicitly present there and is `O(k^-2)`; nothing in this reduction drops
or changes it.

## 8. Calibration and scope

The formula-only checker uses (2.1)--(3.3), reconstructs no topology, and is
capped at odd `k<=15`. For `Y_l`, the largest observed
`k|DE_(Y_l)|/sqrt(l)` is about `0.406`. These finite values are calibration
only and make no universal inference. `X_l` is retained literally in
(4.1)--(4.3) but was not scanned at the cap.

Conclusion: M217 proves the exact signed three-block reduction, the
`O(k^-2)` normalizer block, and the macroscopic-mass lemma. WBE, DE,
IKBE-a/DV, conditional J=2, and all downstream statements remain open.
