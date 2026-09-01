# M325 pre-obstruction candidate freeze: TOEC_1

Date: 2026-08-14 UTC
Status: frozen analytically before any `k=15` guard

## 1. Exact truncated source measures

Fix odd `k>=3`, `n=3k`, `1<=u<k/2`, an admissible lag
`2<=ell<=n-2`, and a canonical QBD endpoint `T=T_q`.  Use M300's exterior
sets `X_c` (cross chords) and `J_d` (internal chords), seam chord
`z_d={0,d}`, and rational Borel weights

```text
q_d=v_k(d)/2-v_(2k-1)(d),
x_c=2c v_(2k-1)(c),
y_d=(2k-1-2d)q_d+v_k(d)/2.
```

Define rational truncated exterior measures

```text
p_T(e)=lambda_c(T)/(2c)                         for e in X_c,
n_T(e)=rho_d(T)q_d/y_d                          for e in J_d,
n_T(z_d)=rho_d(T)v_k(d)/(2y_d).                 (1.1)
```

Their masses are exactly equal:

```text
sum_e p_T(e)=sum_e n_T(e)=T.                    (1.2)
```

At `T=mu_k`, these are precisely the positive and absolute-negative pieces
of the actual exterior signed Borel law.  At an intermediate canonical
endpoint they are its exact quantile truncations, not invented uniform
weights.

For `a in Z/kZ`, let `f_a=f_(a,u)`.  For `s=ef_a`, let the three residual
owners have sizes `d_i`, and let `o_s(x)` be the literal owner of the generic
boundary edge at phase `x`, with the null owner at support heads.

## 2. Completion signatures

Whenever both `o_s(x)` and `o_s(x+ell)` are nonnull, put `r_i` equal to the
number, zero, one, or two, of these two boundary edges owned by component
`i`.  Define the unordered full completion signature

```text
sigma(s,x)={{(d_1,r_1),(d_2,r_2),(d_3,r_3)}}.       (2.1)
```

It retains inactive owners (`r_i=0`).  Its exact rational completion weight
is

```text
w(sigma)=product_i tau(d_i-r_i)/tau(d_i).           (2.2)
```

Thus `(2.2)` is `b_(d_i)` for a same-owner pair and
`a_(d_i)a_(d_j)` for a cross-owner pair, with the unused owner ratios equal
to one.  It is the literal Borel owner coefficient, not an asymptotic or
PSD replacement.

Aggregate every exterior cell present in the prefix, every middle chord
phase, and every target boundary phase before forming

```text
m_T^+(sigma)=sum_e p_T(e) sum_a sum_x 1[sigma(ef_a,x)=sigma],
m_T^-(sigma)=sum_e n_T(e) sum_a sum_x 1[sigma(ef_a,x)=sigma]. (2.3)
```

All quantities in `(2.3)` are rational.  The actual owner law and the
truncated identity give exactly

```text
Psi(T)=sum_sigma w(sigma)[m_T^+(sigma)-m_T^-(sigma)]. (2.4)
```

## 3. Frozen candidate TOEC_1

`TOEC_1` asserts that, for every allowed parameter tuple and every canonical
endpoint, there is a nonnegative rational transport from the negative
decorated configurations to positive decorated configurations supported on
equal full completion signatures.  Equivalently,

```text
m_T^+(sigma)>=m_T^-(sigma) for every sigma.          (TOEC_1)
```

After matching equal signatures, define the unmatched positive remainder

```text
R_T(sigma)=m_T^+(sigma)-m_T^-(sigma)>=0.
```

The exact transport divergence and owner response are then

```text
Psi(T)=sum_sigma w(sigma)R_T(sigma)>=0.              (3.1)
```

This is a genuinely full-aggregate owner-completion transport: neither a
cell, a fixed middle chord, nor an Abel sign block is required to be
positive.  The matching is asked only after all cells through the prefix,
all `k` middle phases, and all target boundary phases have been combined.
It assumes no MON/FOSD order, signed PSD, or one-direction Abel
monotonicity.  It is stronger than `GQAC_1`, so failure would not refute
`GQAC_1`.

No computation has been run.  The next action is only to audit the support
of `(TOEC_1)` at boundary owner compositions; a `k=15` guard is permitted
only if that analytic audit does not decide it.

