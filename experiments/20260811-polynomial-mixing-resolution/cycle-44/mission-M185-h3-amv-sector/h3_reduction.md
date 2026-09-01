# M185 fresh actual-history `h=3` reduction

Date: 2026-08-13 UTC.

## 1. Scope and verdict

This note treats only retained descendants whose last-root height is exactly
`h=3` at a fresh right-heavy parent.  The object is the normalized full
unweighted reset excursion `F=H/q` in the auxiliary nonlazy
minimal-long-cycle parking projection.  The project target remains uniform
fixed-length identity transposition words, with `(pq)(x)=p(q(x))` and factors
displayed left-to-right.

The outcome is a **strict standalone reduction**:

1. the exact three-mode branch is derived;
2. its proposed `2/3` Loewner factor is exactly refuted;
3. the replacement `3/4` Loewner factor is proved for every retained branch;
4. the actual-history suffix-two trace is reconstructed, and a uniform
   `S_child<=1` route is exactly obstructed by its envelope; and
5. the first unproved step is the coupled observation/degree trace aggregate.

No complete `h=3` sector budget is claimed.  Nothing here includes the reset
term, `h>=4`, all suffixes, a gap, the original chain, polynomial mixing, or
either terminal.

## 2. Exact degree-two child and branch matrix

Fix

```text
xi=(B+L,2,1,B),             U_parent~Beta(1,1),
```

a root with last part `B+3` and degree `d`, and a retained observation
`a=0,...,d-1`.  The accepted update gives

```text
xi_a=(B+2,d+2,a+1,B),       mu_a=Beta(a+1,d-a+1).       (2.1)
```

The child suffix excess is two.  M162/M165's accepted degree theorem makes
its full actual-history Hilbert feature a polynomial of degree at most two.
Put

```text
p=E_a U,       v=E_a(U-p)^2,
m_3=E_a(U-p)^3,       m_4=E_a(U-p)^4,
gamma=m_3/v,
P_2=(U-p)^2-gamma(U-p)-v,
h_2=E_a P_2^2=m_4-m_3^2/v-v^2.                         (2.2)
```

With the orthonormal Jacobi basis

```text
e_0=1,       e_1=(U-p)/sqrt(v),       e_2=P_2/sqrt(h_2),
```

write

```text
Phi=A_0e_0+A_1e_1+A_2e_2,
S_a:=E_a||Phi||^2=||A_0||^2+||A_1||^2+||A_2||^2.       (2.3)
```

Let `L_a=binom(d,a)U^a(1-U)^(d-a)`,
`pi_a=E_parent L_a=1/(d+1)`, and `delta=p-1/2`.  The exact Bayes
normalization is

```text
(eta/pi_a)E_parent[L_a^2||Phi||^2]
 =eta E_a[L_a||Phi||^2].                              (2.4)
```

Moreover orthogonality gives

```text
E_parent[(U-1/2)sqrt(eta/pi_a)L_a Phi]
 =sqrt(eta pi_a)(delta A_0+sqrt(v)A_1).                (2.5)
```

Thus, after division by `eta`, the complete retained branch is

```text
B_(d,a)=sum_(i,j=0)^2 G_ij <A_i,A_j>,

G_ij=E_a[L_a e_i e_j]-12 pi_a z_i z_j,
z=(delta,sqrt(v),0).                                  (2.6)
```

Every likelihood-weighted moment and every off-diagonal term is retained.
Multiplication of `mu_a` by `L_a` produces the second posterior

```text
hat mu=Beta(2a+1,2d-2a+1),
lambda_0=E_aL_a=(d+1)/(2d+1) binom(d,a)^2/binom(2d,2a),
```

so the positive part of `G` is exactly
`lambda_0 E_hat[e e^T]`.  The killed `a=d` is absent before taking the
direct-sum norm; there is no survival conditioning.

## 3. Exact `2/3` obstruction

The direct analogue of the accepted affine-sector constant is false.  At
the named endpoint `(d,a)=(20,0)`, exact rational arithmetic gives

```text
det((2/3)I-G_(20,0))
 =-1731224299/244943654967<0.                          (3.1)
```

Here the determinant is in the normalized orthonormal basis (equivalently,
the determinant in `(1,U-p,P_2)` divided by `v h_2`).  Therefore the slack
is not positive semidefinite.  The independent second row `(50,0)` gives

```text
-104272204769339/7259860744068816<0.                  (3.2)
```

This is an exact obstruction, not an eigenvalue scan.

At the minimal row `(1,0)`, direct substitution gives

```text
G=
[ 1/2       0             0          ]
[ 0         1/5          -sqrt(6)/10 ]
[ 0        -sqrt(6)/10    18/35      ],               (3.3)
```

and its top eigenvalue is `(25+sqrt(415))/70`, approximately `0.648165`.

## 4. Universal `3/4` branch theorem

> **Theorem 4.1.** For every `d>=1` and every retained `0<=a<d`,
>
> ```text
> B_(d,a) <= (3/4) S_a.                               (4.1)
> ```

**Proof.**  Vandermonde gives

```text
lambda_0 <= lambda_*=(d+1)/(2d+1).                    (4.2)
```

Since `E_hat[e e^T]` is positive semidefinite, replacing `lambda_0` by
`lambda_*` increases `G` in Loewner order.  It remains to prove positivity
of the resulting slack.  To avoid radicals, use the orthogonal basis
`(1,U-p,P_2)` with Gram matrix `D=diag(1,v,h_2)`.  Put

```text
t=2a-d,       x=t^2,       0<=x<=d^2,
R=(3/4)D-lambda_* E_hat[q q^T]
  +12/(d+1)(delta,v,0)(delta,v,0)^T,                 (4.3)
```

where `q=(1,U-p,P_2)`.  Sylvester's criterion applies because this change
of basis is invertible.

The first leading minor is

```text
R_00=[2d^4+9d^3+11d^2-4+(24d+12)x]
 /[4(d+1)(d+2)^2(2d+1)]>0.                          (4.4)
```

For `d=1`, the numerator is positive directly.  For `d>=2`, every displayed
term except `-4` is already positive.

After removing its positive denominator, the second leading minor has
numerator

```text
P_2(x)=P_20+P_21 x-P_22 x^2,                        (4.5)
```

where `P_22=192d^3+768d^2+1128d+396>0`.  It is concave on `[0,d^2]` and

```text
P_2(0)=(d+2)^3(2d-1)
 (8d^4+40d^3+101d^2+108d+27)>0,

P_2(d^2)=4(d+1)(2d+1)
 (4d^5+108d^4+351d^3+410d^2-27d-54)>0.             (4.6)
```

The final factor in (4.6) is positive already at `d=1`; after the shift
`d=1+e`, all coefficients are positive.  Concavity proves the second minor.

After removing the positive factor

```text
(d-t+2)(d+t+2)
 /[2048(d+1)(d+2)^4(d+3)^4(d+4)^2(d+5)
    (2d+1)^3(2d+3)^3(2d+5)],                       (4.7)
```

the determinant is a cubic `P_3(x)`.  Write it in the degree-three Bernstein
basis on `[0,d^2]`.  Its four coefficients, up to the standard positive
binomial normalization, are

```text
b_0=A_0,
b_1=A_0+A_1d^2/3,
b_2=A_0+2A_1d^2/3+A_2d^4/3,
b_3=A_0+A_1d^2+A_2d^4+A_3d^6.                     (4.8)
```

Exact expansion after `d=1+e` gives respectively coefficient lists

```text
b_0: 448,16320,272552,2765312,19026066,93739864,
     340088204,919045485,1847545129,2724847168,
     2862840630,2031385481,881598831,188426610,9009900;

3b_1: 448,30208,719752,9317488,76782682,434965816,
      1764366668,5230686821,11406181505,18190750532,
      20824203446,16507746845,8499715779,2516417010,318411000;

3b_2: 6976,295008,5175888,51897928,337719576,1519324344,
      4881459896,11355312756,19110062172,22923549140,
      18975908292,10209326904,3178141920,429235200;

b_3: 1792,184192,3626304,34950048,204663936,795646848,
     2137163840,4020127040,5262781248,4668894432,
     2654951040,864535680,121305600.                (4.9)
```

The lists run from the leading coefficient down to the constant coefficient;
every entry is strictly positive for `e>=0`.  Hence all Bernstein
coefficients are positive and `P_3(x)>0` throughout `[0,d^2]`.  All three
leading minors of `R` are positive, proving (4.1).  QED.

The compact checker audits selected rational rows only; equations
(4.2)--(4.9), not finite computation, prove the universal theorem.

## 5. Actual-history suffix-two trace reduction

The matrix theorem compares to the full child trace `S_a`, not child `T_1`
or scalar `F`.  The trace must therefore be reconstructed from actual
history.  Put

```text
k=d+2, D=a+1, U~Beta(D,k-D),
y=w_B/w_(B+1), b=w_B/w_(B+2),
q=(3/2)w_B/w_(B+3),
H_0=(B+1)/(B+3), H_1=B/(B+2).                       (5.1)
```

At suffix two, the exceptional reset coordinates arising from
`(1,1,B)`, `(2,B)`, and `(1,B+1)` give

```text
R_2=
 q(H_0-5q/9-q/(3y))
 +E(3U^2-q)^2/27
 +E(3U^2+6U-4q)^2/54
 +E(y(1-U^2)-q)^2/(6y).                            (5.2)
```

The first term is the accepted canonical-basin envelope for all ordinary
reset coordinates.  The three squares retain the full quadratic child
structure.

The height-one root `(1,B+1)` has two retained observations `j=0,1`; its
suffix-zero child has squared feature at most `1-y`.  If
`lambda_(2,j)=E[L_(2,j)^2]/E[L_(2,j)]` under the present beta law, its exact
trace contribution is bounded by

```text
D_0=[lambda_(2,0)+lambda_(2,1)](1-y)/3.             (5.3)
```

For the unary height-two root, the surviving observation changes the law to

```text
mu_1=Beta(D,k-D+1),       p_1=D/(k+1).
```

M179/M184's accepted suffix-one history, now retaining its outer likelihood,
gives

```text
W_1 <= (1-p_1)b(H_1-b/2)
       +E_mu1[(1-U)(U-b/2)^2]
       +E_mu1[(1-U)^3](1-y)/(1-p_1).               (5.4)
```

Its height-two exterior is `2/3`.  Thus the full actual-history trace obeys

```text
S_a <= Sbar_(B,d,a):=R_2+D_0+(2/3)W_1.             (5.5)
```

This is not M117's scalar `F=H/q` envelope, a generic operator supremum,
Jensen, or a diagonal-mode estimate.  It retains every trace coordinate
before bounding accepted lower-boundary children.

The simple uniform route `Sbar<=1` is false.  At the single named row

```text
(B,d,a)=(3,20,19),

R_2=24302327/19673280,
D_0=511/14400,
W_1=3257413/34500000,

Sbar=10249528643/7684875000>1.                     (5.6)
```

This does not refute a sharper inequality for the exact child trace; (5.5)
is an envelope.  It does rigorously refute the attempted proof route that
combines Theorem 4.1 with a universal bound of one on this accepted
actual-history envelope.  Because endpoint branch matrices are much smaller
on the high-`a` side, the correct next lemma must aggregate the
observation-dependent matrix charge and trace envelope before taking a
supremum.

For `B=1`, inactive rank-one reset/deep targets must be removed in the exact
history.  Formula (5.5), which harmlessly retains nonnegative nominal terms,
is still an upper envelope; the compact row `(B,d,a)=(1,1,0)` gives
`Sbar=2957/23040`.  No generic `B>=2` activity statement is imposed at this
boundary.

## 6. Exact exterior and aggregation boundary

Let

```text
n=L-3,       r=d-1.
```

Summing prefix compositions of total `n` and length `r` gives root mass

```text
m_group=w_(B+3)c(n,r)/[(r+1)!w_(B+L+1)].           (6.1)
```

The child and parent split ratio is

```text
q_child/q_parent=
 [(3/2)w_B/w_(B+3)]/[w_(n+4)w_B/w_(B+L+1)],
```

hence the exact normalized exterior is

```text
eta^(3)_(n,r)= (3/2)c(n,r)/[(r+1)!w_(n+4)].        (6.2)
```

At `n=0`, only `r=0,d=1` occurs, and

```text
eta^(3)_(0,0)=(3/2)/w_4=9/16.                     (6.3)
```

This boundary must not be inferred from the `n>=1` formula.  For `n>=1`,
`r=1,...,n`, including the endpoint `r=n`.  The Cayley composition identity
gives

```text
sum_(r=1)^n (r+1)eta^(3)_(n,r)
 =(3/2)(n+1)^n(n+2)(n+3)/(n+4)^(n+2).              (6.4)
```

The first value is `36/125` at `n=1`; the exact formula is recorded for the
future coupled aggregate.  M185 does not multiply (6.4) by separate worst
matrix and trace constants, because (5.6) shows why the observation
dependence matters.

## 7. Dependencies and first open lemma

Proved/accepted inputs used here are the M109/M114 all-deficit boundary,
M115/M116 suffix-one envelope, M117/M121 suffix-two support accounting,
M147/M151 canonical-basin inequality, M157/M160 actual-history kernel,
M162/M165 feature-degree theorem, M173/M177 exact AMV recursion, and
M179/M184 affine-sector theorem.  Every cited frozen ledger passed before
substantive work.

The first unproved step is now the standalone lemma:

> For fixed degree `d`, combine each actual branch matrix `G_(d,a)` with its
> actual-history suffix-two trace/mode constraints and sum only
> `a=0,...,d-1`, obtaining a degree-dependent charge strong enough to sum
> against the exact exteriors (6.2), with `n=0` separate.

The universal three-mode matrix comparison is no longer open.  The coupled
actual-history trace lemma is.

## 8. Reproducibility

Run from this directory:

```text
python3 -B h3_exact.py --output h3_exact.json
```

The script uses standard-library `Fraction` arithmetic, `seed=null`, and
only the named decisive matrix and trace rows.  It imports no predecessor and
does not enumerate `L=7` or any state graph.
