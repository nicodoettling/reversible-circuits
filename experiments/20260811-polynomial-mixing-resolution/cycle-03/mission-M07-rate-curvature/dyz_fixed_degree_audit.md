# DYZ fixed-degree audit for ordinary genus log-concavity

## Exact primary source

Boris Dubrovin, Di Yang, and Don Zagier, *Classical Hurwitz numbers and
related combinatorics*, Moscow Mathematical Journal 17 (2017), preprint PDF:

<https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf>

Their notation is

```text
h_(g,d)=H_(g,d)/(2g+2d-2)!,
C_d(x)=sum_(g>=0) h_(g,d) x^(2g+2d-2).
```

For fixed labeled sheets, the count in this project is
`C(d,2d-2+2g)=d! H_(g,d)`, as checked by
`C(2,2)=1,C(3,4)=24,C(4,6)=2880`.  Therefore the project's
`a_d(g)` is `d! h_(g,d)` and every adjacent ratio is literally unchanged.

DYZ Theorem 1, equations (14)--(15), states

```text
C_d(x) = gamma_d(4 sinh^2(x/2))/d,
gamma_1(s)=1,
gamma_d(s)=1/[d(d-1)] sum_(q=1)^(d-1)
             (d-q) P_q(s) gamma_q(s) gamma_(d-q)(s),
P_q(s)=2 T_q((s+2)/2)-2.
```

The displayed closed formula for `P_q` immediately before the theorem has
positive coefficients.  The `gamma_d` recurrence consequently has positive
coefficients and degree `binom(d,2)`, with minimum nonzero degree `d-1`.
This is the fixed-degree form most likely to prove ordinary genus
log-concavity.

Equivalently, DYZ Proposition 1, equation (13), is a positive quadratic
recurrence for `h_(g,d)`.  After writing `ell=j+1`, an ordered split
`d=d_1+d_2` contributes, up to a positive genus-independent constant, the
coefficient sequence of

```text
A_(d_1)(z) A_(d_2)(z) B_(d_1,d_2)(z),
B_j=d_1^(2j+3)d_2^2/(2j+2)!.
```

This is the recurrence used for the inherited bound `rho_d(g)>=12/d^3`.
It does not by itself compare two consecutive ratios.

## Why the corollary is not a positive moment proof

The corollary to DYZ Theorem 1, equation (18), gives

```text
H_(g,d)=2/d!^2 sum_(1<=q<=binom(d,2)) b_(d,q) q^(2g+2d-2),
```

but the integers `b_(d,q)` have both signs.  Already at `d=3`, after a
common positive scaling, the exact expansion is

```text
b_(3,1)=-9, b_(3,3)=1.
```

Thus (18) is a signed finite exponential representation, not a Stieltjes
moment representation.  No alternative positive Stieltjes representation
of `a_d(g)` itself can exist in general: Stieltjes moment sequences are
log-convex by Cauchy--Schwarz, whereas at `d=4`

```text
rho_4(2)=195/82 > 16/13=rho_4(1),
```

so `a_4(1)^2>a_4(0)a_4(2)` strictly.

Ordinary genus log-concavity is exactly

```text
a_d(g)^2 >= a_d(g-1)a_d(g+1)
<=> rho_d(g+1)>=rho_d(g).
```

It must not be confused with the stronger ultra-log-concavity inequality,
which has already been refuted at `(d,g)=(4,1)`.

## Two audited insufficient closure principles

1. Pairwise synchronization of the ordered-split sequences in DYZ (13)
   fails exactly at `d=3,g=5`; see `recurrence_sync_results.json`.  Hence
   log-concavity cannot be obtained merely by declaring every summand
   pairwise synchronized before adding them.

2. Even a positive log-concave coefficient vector in `s` need not remain
   log-concave after substitution `s=4sinh^2(x/2)` and factorial
   normalization.  For the exact polynomial

   ```text
   f(s)=s+s^2/5000,
   y_n=[x^(2n)] f(4sinh^2(x/2)),
   ```

   one has

   ```text
   y_6^2-y_5 y_7
     = -8680673/1165137861888000000000000 < 0.
   ```

   Thus positivity plus coefficient log-concavity of `gamma_d` would still
   not, without a stronger DYZ-specific invariant, prove the desired genus
   log-concavity.

The surviving named route is therefore a DYZ-specific quantitative
central-factorial transform theorem, not a generic moment, real-rootedness,
or positive-coefficient theorem.

