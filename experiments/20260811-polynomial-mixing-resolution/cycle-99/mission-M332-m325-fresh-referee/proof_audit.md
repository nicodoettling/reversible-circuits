# M332 independent proof audit of M325

Date: 2026-08-14 UTC

Provisional verdict: **ACCEPT** at the exact frozen scope.

## 1. Truncated full-signature expansion

For cut class `c`, the positive chord set has `|X_c|=2c`, so M325's measure

```text
p_T(e)=lambda_c(T)/(2c),       e in X_c,
```

has total class mass `lambda_c(T)`. For the negative cut class `d`, there are `D-2d` internal chords, each of mass `rho_d(T)q_d/y_d`, and one seam chord of mass `rho_d(T)v_k(d)/(2y_d)`. Since

```text
y_d=(D-2d)q_d+v_k(d)/2,
```

its total class mass is `rho_d(T)`. The locked truncated marginals give

```text
sum_e p_T(e)=sum_c lambda_c(T)=T
            =sum_d rho_d(T)=sum_e n_T(e).           (1.1)
```

At `T=mu_k`, `lambda_c=x_c=2c v_D(c)` and `rho_d=y_d`; hence `p_T` is exactly the positive exterior Hahn mass and `n_T` is exactly the absolute negative internal/seam mass. At intermediate endpoints the same calculation uses the exact truncated marginals, with no uniformization.

For a state `s=e f_a` and target phase `x`, let owner `i` have size `d_i` and be hit `r_i` times by the two target edges. The literal completion ratio factorizes as

```text
w(sigma)=product_i tau(d_i-r_i)/tau(d_i).            (1.2)
```

It equals `b_d` for a same-owner pair and `a_d a_e` for a cross-owner pair; every inactive owner contributes exactly one. Summing (1.2) first over all target phases `x`, then all `k` middle phases `a`, and finally every exterior atom in the complete truncated positive/negative measures gives

```text
Psi(T)=sum_sigma w(sigma)(m_T^+(sigma)-m_T^-(sigma)). (1.3)
```

Thus the expansion retains boundary phases, all middle phases, every exterior cell present in the prefix, and the exact common mass. No cell, middle, or sign-block positivity is inserted.

For finite rational measures, a transport from every negative atom to positive capacity with the same signature exists exactly when `m_T^+(sigma)>=m_T^-(sigma)` for every signature. Hence TOEC's transport and capacity formulations are equivalent.

## 2. Independent `k=5` seam reconstruction

Take `k=5`, `n=15`, `u=2`, `ell=2`, `T=mu_5`, seam `e={0,1}`, and middle phase `f_(0,2)={5,7}`. The cyclicly ordered support points are `0,1,5,7`, giving gaps

```text
(g_1,g_2,g_3,g_4)=(1,4,2,8).
```

This is the separated `S` double, whose exact residual owner sizes are

```text
(g_1,g_3,g_2+g_4)=(1,2,12).                         (2.1)
```

The size-12 owner is the two-run owner `I_2 union I_4`. From the literal interval definition,

```text
I_2={1,2,3},       I_4={7,8,9,10,11,12,13}.
```

At target phase `x=1`, both `x=1` and `x+ell=3` belong to `I_2`. The other owners are inactive. Therefore the unordered full signature is exactly

```text
sigma_*={{(1,0),(2,0),(12,2)}},
w(sigma_*)=tau(10)/tau(12)>0.                       (2.2)
```

The terminal seam mass is `v_5(1)/2`. Directly from

```text
tau(d)=d^(d-2)/(d-1)!,
```

one has `tau(4)=8/3`, `tau(5)=125/24`, and

```text
v_5(1)=tau(1)tau(4)/(4tau(5))=16/125.
```

Thus this single decorated atom contributes exactly `8/125`, proving

```text
m^-_(mu_5)(sigma_*)>=8/125>0.                       (2.3)
```

## 3. Positive support has no matching signature

Every positive exterior chord is `{i,j}` with `1<=i<=4` and `10<=j<=14`. Write the middle chord as `{p,q}`, `5<=p<q<=9`. These are nested doubles. The exact residual sizes are

```text
q-p,       15-j+i,       (p-i)+(j-q).                (3.1)
```

For the complete `u=2` orbit on the five middle vertices, `q-p` is two or three. The other terms satisfy

```text
15-j+i>=2,
(p-i)+(j-q)>=1+1=2.                                  (3.2)
```

Hence every positive nested state has all owner sizes at least two. This conclusion is state-level and therefore includes every target phase, including null boundary phases. No positive full signature can contain `(1,0)`, so

```text
m^+_(mu_5)(sigma_*)=0.                              (3.3)
```

Equations (2.3) and (3.3) refute TOEC exactly. The endpoint is terminal, so no quantile cell is sliced and all sign blocks are present.

## 4. Exact scope

The singleton owner is inactive and contributes the factor `tau(1)/tau(1)=1`. Therefore positive mass with different inactive-owner data can still compensate the negative atom after weighting and summing over signatures. The obstruction refutes same-full-signature domination only; it does not refute GQAC or MCLP.

Projecting away inactive owners gives the exact active types

```text
S_d       (same owner),
X_(d,e)   (distinct owners, d<=e).
```

Direct grouping of the literal response gives

```text
Psi(T)=sum_(d>=3)b_d Delta_T^S(d)
      +sum_(2<=d<=e)a_d a_e Delta_T^X(d,e).          (AOTI_1)
```

A size-two owner has only one generic boundary-tail phase and cannot own both distinct target phases at admissible nonzero lag, while a singleton has none; hence the displayed lower bounds are exact. All coefficients are positive. Consequently active-profile inequalities `Delta_T^S(d)>=0` and `Delta_T^X(d,e)>=0` at the canonical endpoints imply `Psi(T)>=0`, which is AOEC `=>` GQAC. AOTI itself assigns no sign.

The quotient is strict: it forgets the inactive singleton that obstructs TOEC. AOEC, GQAC, and MCLP remain unresolved. No `k=15` guard, new transport, or downstream inference is justified.

## 5. Numbered objections

1. **Material objections:** none.
2. **Nonmaterial objections:** none.
