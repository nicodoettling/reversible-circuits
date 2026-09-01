# Cycle 05 M18 halfway checkpoint

## Frozen scoped theorem

Put `M=binom(N,2)`. For integers `g>=1` and `N>=max(4,g+1)`, let

```text
m=2(N-1)+2g
```

and let `F_(N,g)` be the connected exact-full-support macro in
`Omega(N,m)`. Preliminary accounting gives

```text
Phi_pm^K(F_(N,g))
 >= (3/4)^g / [192 N^(5g+6)].                         (C.1)
```

Thus, for every fixed `g_0`, all bottom-layer cuts `F_(N,g)`,
`1<=g<=g_0`, have an inverse-polynomial two-sided conductance bound, uniformly
in `N`. The exponent is not uniform in growing `g`.

## Count ratio

Let `C_g(d)` count connected exact-support identity transposition words on a
fixed labeled `d`-set, of length `k_(g,d)=2d-2+2g`, and put

```text
a_(g,d)=C_g(d)/k_(g,d)!.
```

The proved DYZ recurrence consequence says

```text
a_(g,d)<= (d^3/12)^g a_(0,d).                         (C.2)
```

Conversely, fixing one edge `e` on a labeled `d`-set, the map

```text
w -> (e,e)^g w
```

injects connected genus-zero words into connected genus-`g` words. Hence
`C_g(d)>=C_0(d)`. Since

```text
C_0(d)=(2d-2)! d^(d-3),
```

we obtain

```text
C_g(N-1)/C_g(N)
 >= 12^g C_0(N-1)
    /[N^(3g) C_0(N) product_(j=1)^(2g)(2N-2+j)].       (C.3)
```

For `N>=4`,

```text
C_0(N-1)/C_0(N)
 = (1-1/N)^(N-4)/[N(2N-2)(2N-3)]
 >=1/(16N^3).                                          (C.4)
```

For `N>=g+1`, every factorial-ratio factor in (C.3) is at most `4N`.
Consequently

```text
C_g(N-1)/C_g(N)
 >=(3/4)^g/[16 N^(5g+3)].                              (C.5)
```

## Marked leaf squares and exact `K` exit

A mark in `w in F_(N,g)` is an adjacent square `(uv),(uv)` such that `v`
occurs nowhere else and deleting the square leaves a connected genus-`g`
word on `[N] minus {v}`. Deletion/insertion is a bijection between marked
incidences and the data

```text
v, u, a word counted by C_g(N-1), and one of m-1 gaps.
```

Therefore, for `Z(w)` the number of marks,

```text
E_F Z=N(N-1)(m-1) C_g(N-1)/C_g(N)
     >=(3/4)^g/[32 N^(5g)].                            (C.6)
```

Each omitted label determines at most one mark, so `Z<=N` and

```text
Pr_F[Z>=1]>=(3/4)^g/[32 N^(5g+1)].                     (C.7)
```

Choose one mark deterministically. Pad it on the available side to an
`H_3` window and replace `(e,e,a)` by `(f,f,a)`, or `(a,e,e)` by
`(a,f,f)`, where `f` avoids `v`. The output has the same ordered block
product and omits `v`, hence is outside `F_(N,g)`. A three-factor fiber has
size at most `M^2`, so the specified outcome has probability at least

```text
q=1/[2*3*(m-2)M^2]>=1/(6N^5).                          (C.8)
```

Here `m-2<4N` follows from `N>=g+1`, and `M<=N^2/2`. Multiplying
(C.7)--(C.8) proves (C.1), after dividing by
`min(pi(F),pi(F^c))<=pi(F)`.

## Halfway self-attack

The proof deliberately fixes `g`. The constant and exponent in (C.1)
deteriorate with `g`, and the known fixed-degree large-genus asymptotic shows
that no genus-uniform pendant-square density can be true. Thus (C.1) does
not decide the actual growing-surplus phase window. Its value is that it
rigorously eliminates every bounded-surplus instance of the most obvious
bottom component-layer cut, including the first untreated case `g=2`,
without any `W_c` unimodality assumption.
