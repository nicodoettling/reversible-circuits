# Exact boundary curvature cases

The normalization and conventions are those of `dense_curvature.md`.

## The first occupancy increment for every degree

The inherited positive-recurrence estimate from DYZ Proposition 1 is

```text
rho_v(g)=a_v(g-1)/a_v(g) >= 12/v^3       (v>=2,g>=1).
```

Since `rho_v(0)=0`, it immediately proves

```text
rho_v(1)-rho_v(0) >= 12/v^3.                              (1)
```

Thus the zero-range increment at occupancy zero is already uniformly
controlled.  The unresolved rate-curvature range starts at `g=1`, not at
`g=0`.

## Degree two

There is one transposition and `C_2(k)=1` for every positive even `k`.
Therefore

```text
rho_2(1)-rho_2(0)=12,
rho_2(g+1)-rho_2(g)=4k+2  for g>=1, k=2+2g.
```

## Degree three, all genera

DYZ Theorem 1 gives, up to a positive constant independent of genus,

```text
gamma_3(s) proportional to 6s^2+s^3=P_3(s)-9P_1(s).
```

Under `s=4sinh^2(x/2)`,
`P_q(s)=2cosh(qx)-2`.  If `n=2+g`, it follows that

```text
a_3(g) proportional to (9^n-9)/(2n)!.
```

Put

```text
r_n=(9^(n-2)-1)/(9^(n-1)-1),
A_n=2n(2n-1).
```

Then `rho_3(g)=A_n r_n`, including `rho_3(0)=0`.  Moreover

```text
(9^(n-1)-1)^2-(9^(n-2)-1)(9^n-1)
  =9^(n-2)(9-1)^2 >0,
```

so `r_(n+1)>=r_n`.  The first increment is
`A_3r_3=3`.  For `n>=3`, `r_n>=r_3=1/10` and
`A_(n+1)-A_n=8n+2`, hence

```text
rho_3(g+1)-rho_3(g) >= (8n+2)/10 >= 13/5.                (2)
```

Thus rate curvature holds for `v=3` in every genus with a universal constant
margin.

## Degree four, all genera

The exact DYZ polynomial is, up to positive scale,

```text
96s^3+54s^4+12s^5+s^6
  =144P_1(s)-9P_2(s)-16P_3(s)+P_6(s).
```

Thus for `n=3+g`, after dropping a common positive factor,

```text
T_n=36^n-16*9^n-9*4^n+144
   =36^n(1+e_n),
|e_n| <= 16/4^n+9/9^n+144/36^n.
```

For `n>=6`, the right side at index `n-1` is at most

```text
16/4^5+9/9^5+144/36^5 < 1/48=1/(8*6),
```

and `n` times this bound decreases thereafter.  Hence, with `k=2n`, the
three adjacent errors have absolute value at most `1/(4k)`.  The same
three-error calculation as in `dense_curvature.md` gives

```text
rho_4(g+1)-rho_4(g) >= (2k-2/k)/6^2 >0       (n>=6).
```

The three remaining increments (`n=3,4,5`) are exactly

```text
16/13,
195/82-16/13=1223/1066,
1164531/935374,
```

respectively.  Therefore curvature also holds for `v=4` in every genus,
with an explicit inverse-polynomial (indeed constant in the finite boundary
and increasing in the tail) margin.

The second value in particular reproduces the supplied calibration

```text
rho_4(2)-rho_4(1)=195/82-16/13=1223/1066>0.
```
