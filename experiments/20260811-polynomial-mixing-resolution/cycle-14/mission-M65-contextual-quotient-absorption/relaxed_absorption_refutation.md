# Uniform refutation of the relaxed scalar absorption bound

Date: 2026-08-12.  This is a rigorous obstruction to the M56 scalar
recurrence template, not a slow-mixing theorem for the parking projection
and not a statement about `K`.

## 1. Extreme contextual family

Fix local rank `s>=2`, suffix `B=1`, and synthetic external parameters

```text
R=K-1.
```

Let `H=E[phi|root composition]` be the closed normalized contextual mean,
`G_s=R_s/alpha_s`, and

```text
m_s=E_rho H=w_s/w_(s+1)=(s/(s+1))^(s-1)>=e^(-1).
```

The mean identity is the exact stationary root-split flow from branch size
`s+1` to `(s,1)` and is independent of `(K,R)`.

Put `Z={C:last(C)=1}` and `p_s=rho_s(Z)`.  The single composition
`(s-1,1)` gives

```text
p_s >= s(s-1)^(s-2)/[2(s+1)^(s-1)]
    = [s/(2(s+1))][(s-1)/(s+1)]^(s-2)
    >=1/(3e^2)=:p_0.                                (1.1)
```

For the last inequality use
`log(1-x)>=-x/(1-x)` with `x=2/(s+1)`.

## 2. A one-coordinate variational lower bound

The only normalized quotient edges crossing `Z` toggle the cut immediately
before the final unit part.  From a composition with last part `t>1`, the
crossing split rate is `w_(t-1)w_1/w_t`.  Summing stationary flow gives

```text
E_(G_s)(1_Z,1_Z)=m_s.                               (2.1)
```

This is also obtained by taking `K->infinity` in the closed mean: the deep
value tends to that crossing rate, the terminal value tends to zero, and
the mean remains `m_s`.

Write

```text
q_T=E[H 1_Z],      x=q_T/m_s.
```

The variational definition of the Green norm, tested on `1_Z`, yields

```text
A_s:=||H-m_s||_(-1,G_s)^2
 >= <H-m_s,1_Z>^2/E_G(1_Z,1_Z)
 =m_s(p_s-x)^2.                                    (2.2)
```

Every composition in `Z` has at least two parts.  For `R=K-1`, its
terminal value is

```text
K/binom(K+k-1,k)<=2/(K+1),          k>=2.
```

Consequently

```text
x<=2/[m_s(K+1)]<=2e/(K+1).                         (2.3)
```

Choose once and for all

```text
K+1>=144e^5.
```

Then (1.1)--(2.3) give `x<=p_0^2/8<=p_s^2/8`.

## 3. Constant excess

In M56 notation,

```text
delta=1-x,       a=A_s/m_s.
```

Therefore (2.2) implies, uniformly for every `s>=2`,

```text
delta+a-1
 >=(p_s-x)^2-x
 >=p_s^2-(2p_s+1)x
 >=5p_0^2/8
 =5/(72e^4)>0.                                     (3.1)
```

Thus no universal estimate

```text
delta+a<=1+C/s
```

can hold for all contextual suffix statistics and all `s`, for any fixed
finite `C`: take the fixed `K` above and let `s` tend to infinity.  This
is stronger than the rank-two exact refutation of `delta+a<=1`.

Equation (3.1) still does not prove a slow mode.  It lower-bounds the
coefficient produced by one particular quotient-disintegration recurrence;
the full parking chain may route the same demand through other actual
edges, and marked child mixtures can interfere or cancel.  A genuine gap
upper bound requires an explicit global Rayleigh test or a stationary cut.
