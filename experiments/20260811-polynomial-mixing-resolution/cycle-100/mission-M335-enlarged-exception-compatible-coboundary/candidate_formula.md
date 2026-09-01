# M335 frozen compatible-map and exceptional-mass formulas

Date: 2026-08-14 UTC

Status: frozen analytically before any M335 computation.

## 1. Complete token law

Fix one row `X` and retain the full raw labels described by M323. For each
supported quantile cell `(s,t)`, let

```text
a_st(P)=[g_s(P)-f_t(P)]_+,
b_st(Q)=[f_t(Q)-g_s(Q)]_+,
rho_st=sum_P a_st(P)=sum_Q b_st(Q).
```

Write `u^A_(s,P)(xi)` and `u^B_(t,Q)(eta)` for the exact conditional raw
fiber probabilities after both channels, all `T/S/N` representations,
phases, seams, incidences, representation factors, marked slots, and zero
slots have been combined. A literal residual token

```text
omega=(s,t; xi_A at P, eta_B at Q)
```

has weight

```text
w(omega)=c_X pi_st a_st(P)b_st(Q)/rho_st
         *u^A_(s,P)(xi)u^B_(t,Q)(eta),              (1.1)
c_X=r_X(alpha_1+alpha_2),  r_H=r_A=3, r_C=6.       (1.2)
```

No constituent of `(1.1)` is separately normed.

## 2. Frozen exception and exact flux split

For an endpoint atom `zeta_R`, set

```text
E_R(zeta_R)=Touch_Sigma(zeta_R) or BadPref_R(zeta_R),
Exc_pf^*(omega)=E_A(xi_A) or E_B(eta_B).            (2.1)
```

For the oriented unit profile edge `[P,Q]`, define

```text
J_compatible=sum_omega w(omega)1[not Exc_pf^*(omega)][P,Q],
J_exceptional=sum_omega w(omega)1[Exc_pf^*(omega)][P,Q].
```

The token universe is partitioned literally, hence

```text
J=J_compatible+J_exceptional.                       (2.2)
```

This is an exact signed-edge identity before any absolute value.

## 3. What the source switch already proves

For `zeta_R` with `BadPref_R=false`, the retained prefix has positive
minimal-completion count for the opposite source. Let `sigma(zeta_R)` be
that opposite-source raw atom, with its channel/split recomputed and all
product, positive representation, slot, and profile data retained.

Because switching back restores the original source and prefix,
`sigma^2=id` on this domain. Product and slot retention preserve the response
profile. `Touch` is unchanged, and validity of the return prefix makes
`BadPref` false after switching. Therefore the pair map

```text
S_pf^*(s,t;xi_A,eta_B)
 =(s',t';sigma(eta_B)_A,sigma(xi_A)_B),             (3.1)
```

where `s'` and `t'` are the recomputed splits, is a literal raw-label
involution off `(2.1)` whenever its image belongs to the residual token
universe. It preserves `{P,Q}` and reverses `P->Q` to `Q->P`.

Thus prefix existence, raw involutivity, profile-edge preservation, and
exception invariance are proved. They do not by themselves prove token-law
landing or weight preservation.

## 4. Exact remaining compatible clauses

For an original positive token, the image in `(3.1)` is a reverse residual
token exactly only if

```text
pi_(s',t')>0,
a_(s',t')(Q)>0,
b_(s',t')(P)>0.                                    (4.1)
```

When `(4.1)` holds, the exact weight ratio is

```text
w(S_pf^* omega)/w(omega)
 = [pi_(s',t')/pi_(s,t)] [rho_(s,t)/rho_(s',t')]
   [a_(s',t')(Q)/b_(s,t)(Q)]
   [b_(s',t')(P)/a_(s,t)(P)]
   [u^A_(s',Q)(sigma eta)/u^B_(t,Q)(eta)]
   [u^B_(t',P)(sigma xi)/u^A_(s,P)(xi)].           (4.2)
```

The corrected `c_X` cancels between numerator and denominator but is present
in both token weights. A compatible-part coboundary would require `(4.1)`
and ratio `(4.2)=1` for every token outside `Exc_pf^*`. No aggregate sign or
arbitrary mass matching may be used to repair a failure.

## 5. Exact scalar reduction for the exceptional part

Let

```text
epsilon^A_(s,P)=Pr[E_A(xi_A)|s,P],
epsilon^B_(t,Q)=Pr[E_B(eta_B)|t,Q].
```

Marginalizing the residual-product token law and applying only the union
bound gives

```text
mass_X(Exc_pf^*)
 <=c_X sum_(s,t)pi_st [
       sum_P a_st(P)epsilon^A_(s,P)
      +sum_Q b_st(Q)epsilon^B_(t,Q)].               (5.1)
```

Since `a_st<=g_s`, `b_st<=f_t`, and `pi` has marginals `q,p`, define the
complete endpoint exception probabilities

```text
E_A^X(s)=sum_P g_s(P)epsilon^A_(s,P),
E_B^X(t)=sum_Q f_t(Q)epsilon^B_(t,Q).
```

Then exactly

```text
mass_X(Exc_pf^*)
 <=c_X [sum_s q_s E_A^X(s)+sum_t p_t E_B^X(t)]      (5.2)
```

and, with `D=2k-1`, `h=(k-1)/2`,

```text
<=c_X [ k/(k-1) sum_(s<=h)b_s R_k(s)E_A^X(s)
       +D/(D-1) sum_(t<=k-1)b_t R_D(t)E_B^X(t)].   (5.3)
```

Formula `(5.3)` is the requested explicit combined Borel scalar reduction.
It retains all channel/kind/phase/seam/slot data inside each endpoint
probability. The still-unproved scalar exception lemma is that `(5.3)` is at
most

```text
C d b_d/k                         for X=H_d or A_d,
C max(d,e)b_d b_e/k               for X=C_(d,e).    (5.4)
```

If `(4.1)--(4.2)` held, `J_compatible=0` and
`||J||_edge<=mass_X(Exc_pf^*)`; `(5.4)` would then give the desired localized
edge scale. Neither `(4.1)--(4.2)` nor `(5.4)` is assumed here.

