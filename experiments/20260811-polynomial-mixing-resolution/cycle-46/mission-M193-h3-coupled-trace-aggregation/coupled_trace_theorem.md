# M193 coupled fresh actual-history `h=3` theorem

Date: 2026-08-13 UTC.

## 1. Scope and result

This note treats only fresh retained descendants whose last-root height is
exactly `h=3` in the normalized full unweighted reset excursion `F=H/q` of
the auxiliary nonlazy minimal-long-cycle parking projection. The project
target remains uniform fixed-length identity transposition words, with
`(pq)(x)=p(q(x))` and displayed factors left-to-right.

The accepted M185/M190 branch theorem and actual-history envelope imply:

> **Theorem 1.1 (fresh `h=3` sector).** For every active boundary `B>=1`,
> the complete fresh actual-history `h=3` sector is at most `27/125` when
> `n=L-3>=1`. At the separate boundary `n=0`, it is at most `3/8`.

The result retains the full Hilbert-valued quadratic child, every branch
cross term, and the killed observation `a=d`. It makes no assertion about the
fresh reset, `h>=4`, total AMV, all `L`, a gap, the original chain,
polynomial mixing, or either terminal.

## 2. Branch and exterior normalization end to end

Fix a degree `d` root. A retained attachment `a=0,...,d-1` produces the
suffix-two child

```text
(B+2,d+2,a+1,B),       U~Beta(a+1,d-a+1).           (2.1)
```

There are exactly `d` retained observations. The value `a=d` is killed
before the history direct sum and is never conditioned back in. Write the
child feature in its three orthonormal Jacobi modes with Hilbert coefficients
`A_0,A_1,A_2`, and put

```text
S_a=||A_0||^2+||A_1||^2+||A_2||^2.                 (2.2)
```

For `L_a=binom(d,a)U^a(1-U)^(d-a)` and
`pi_a=E_parent L_a=1/(d+1)`, the accepted exact Bayes normalization is

```text
(eta/pi_a) E_parent[L_a^2||Phi_a||^2]
 =eta E_child[L_a||Phi_a||^2].                     (2.3)
```

After the parent covariance subtraction, the branch divided by `eta` is the
full quadratic form `B_(d,a)=sum_ij G_ij<A_i,A_j>`, including every
off-diagonal term. M185/M190 proves

```text
B_(d,a) <= (3/4)S_a.                               (2.4)
```

Equation (2.3) is why `pi_a` is already inside `G_(d,a)`: there is no extra
`pi_a`, survival probability, or `1/(d+1)` outside the branch sum.

Let `n=L-3` and `r=d-1`. The grouped root mass and child/parent split ratio
are, respectively,

```text
m_group = w_(B+3)c(n,r)/[(r+1)!w_(B+L+1)],

q_child/q_parent
 =[(3/2)w_B/w_(B+3)]/[w_(n+4)w_B/w_(B+L+1)].       (2.5)
```

Cancellation gives one common exterior for every retained observation,

```text
eta^(3)_(n,r)=(3/2)c(n,r)/[(r+1)!w_(n+4)].         (2.6)
```

Consequently the exact sector charge is bounded from the expression

```text
C_3(B,n)=sum_r eta^(3)_(n,r)
                 sum_(a=0)^(d-1) B_(d,a), d=r+1.  (2.7)
```

No observation count has yet been divided out in (2.7).

## 3. Exact observation-averaged actual-history trace

Use M185/M190's accepted actual-history envelope

```text
S_a <= Sbar_(B,d,a)=R_2+D_0+(2/3)W_1,              (3.1)
```

which reconstructs all suffix-two reset coordinates, the two height-one
observations, and the likelihood-weighted unary height-two child. This is a
full trace envelope, not scalar `F`, scalar `T_1`, a diagonal deletion, or a
generic operator supremum.

Put

```text
D=a+1, k=d+2, y=w_B/w_(B+1), b=w_B/w_(B+2),
q=(3/2)w_B/w_(B+3), H0=(B+1)/(B+3), H1=B/(B+2).
```

For `U_D~Beta(D,k-D)`, exact hockey-stick summation over `D=1,...,d`
gives

```text
pbar=(1/d)sum_D E U_D       =(d+1)/[2(d+2)],
m_j =(1/d)sum_D E U_D^j     =(d+1)/[(j+1)(d+j+1)]
                              for j=2,3,4.           (3.2)
```

Let `A_(B,d)=(1/d)sum_a Sbar_(B,d,a)`. Direct expansion of (3.1), with no
inequality yet, gives

```text
Rbar =m2(2/3-(q+y)/3)+(2/3)m3+(1/2+y/6)m4
      +q^2(-2/9-1/(6y))+q(H0-1/3-(8/9)pbar)+y/6,

Dbar =2(d+7)(1-y)/[9(d+4)],

Wbar =N_W/[24(d+3)(d+4)(d+5)],

A_(B,d)=Rbar+Dbar+(2/3)Wbar,                        (3.3)
```

where

```text
N_W =[(12H1-4)d^3+(168H1-56)d^2+(780H1-212)d
      +(1200H1-160)]b
     -(3d^3+42d^2+195d+300)b^2
     +10d^3+148d^2+734d+1172
     -y(8d^3+120d^2+664d+1128).                    (3.4)
```

Thus the `1/d` is only notation for an arithmetic average; it will be
multiplied back before the exterior sum.

## 4. Universal averaged-trace lemma

> **Lemma 4.1.** For every `B,d>=1`, `A_(B,d)<1`. Hence
>
> ```text
> sum_(a=0)^(d-1) S_a <= sum_a Sbar_(B,d,a) < d.    (4.1)
> ```

**Proof for `B>=2`.** Write `y_B=w_B/w_(B+1)`. Then

```text
y_B=(B/(B+1))^(B-1).
```

The function `(x-1)log(1+1/x)` is increasing for `x>=1`, because
`log(1+t)>=t/(1+t)>t(1-t)/(1+t)` at `t=1/x`. Therefore `y_B` decreases to
`e^-1`, so `y>=e^-1>1/3`. Also `b=y_B y_(B+1)<=y_2y_3=3/8`.

Increase `H0,H1` to one in (3.3); their coefficients are nonnegative. Call
the result `A#`. Its exact derivative is

```text
dA#/db=[4d^2+36d+104-b(3d^2+27d+60)]
       /[18(d+3)(d+4)] >0,                          (4.2)
```

because at `b=3/8`, eight times the numerator is
`23d^2+207d+652>0`. Hence set `b=3/8`.

As a function of `q`, `A#` is a strictly concave quadratic: its quadratic
coefficient is `-(4y+3)/(18y)`. Its unconstrained maximum occurs at

```text
q*=y(d^2+11d+22)/[(d+2)(d+3)(4y+3)].               (4.3)
```

Using the unconstrained maximum can only enlarge the actual Cayley value.
After substituting `b=3/8,q=q*`, differentiation in `y` gives

```text
-P_d(y)/[90(d+2)^2(d+3)^2(d+4)(d+5)(4y+3)^2].     (4.4)
```

The coefficients of `P_d(y)` in `(y^2,y,1)`, from `d^6` down to `d^0`,
are

```text
(512,768,273), (11520,17280,6015),
(105472,158208,53583), (492160,738240,240705),
(1231488,1847232,570612), (1571840,2357760,673620),
(803328,1204992,306672).                            (4.5)
```

Every coefficient is positive, so the maximum decreases in `y`; set
`y=1/3`. The resulting exact slack is

```text
1-A# =
[4829d^6+102561d^5+766087d^4+2534491d^3
 +3485988d^2+607388d-1774608]
/[89856(d+2)^2(d+3)^2(d+4)(d+5)].                  (4.6)
```

After `d=1+e`, the numerator, in descending powers, has coefficients

```text
4829,131535,1351327,6721029,16784028,18788964,5726736.
```

They are all positive for `e>=0`. This proves (4.1) for `B>=2`.

**Boundary `B=1`.** Here `y=1,b=2/3,q=9/16,H0=1/2,H1=1/3`.
Inactive rank-one/deep coordinates are deleted in the actual history;
retaining their nonnegative nominal contributions only enlarges the trace.
Substitution into the nominal average gives

```text
A_(1,d)=
[17591d^4+187970d^3+679425d^2+1233430d+1075144]
/[69120(d+2)(d+3)(d+4)(d+5)],                      (4.7)

1-A_(1,d)=
[51529d^4+779710d^3+4228095d^2+9411050d+7219256]
/[69120(d+2)(d+3)(d+4)(d+5)]>0.                    (4.8)
```

This handles inactivity by deletion and exact boundary substitution, not by
applying the `B>=2` bounds. QED.

The old obstruction remains real: at `(B,d,a)=(3,20,19)`,
`Sbar=10249528643/7684875000>1`. But the exact degree average is
`443845801/614790000<1`. Lemma 4.1 is observation-aggregated and does not
reinstate the refuted pointwise claim.

## 5. Sector aggregation for `n>=1`

Summing (2.4) and applying Lemma 4.1 gives, for each degree,

```text
sum_(a=0)^(d-1) B_(d,a)
 <=(3/4)sum_a S_a <(3/4)d.                          (5.1)
```

For `n>=1`, the exact range is `r=1,...,n`, including `r=n`, where
`c(n,n)=1`. The Cayley composition identity gives

```text
sum_(r=1)^n (r+1)eta^(3)_(n,r)
 =(3/2)(n+1)^n(n+2)(n+3)/(n+4)^(n+2)=:M_n.         (5.2)
```

To bound it, apply the first three binomial terms to
`(1+3/(n+1))^n`:

```text
(1+3/(n+1))^n
 >=[17n^2+n+2]/[2(n+1)^2].                         (5.3)
```

This gives an upper bound `U_n` on `M_n`, and exact subtraction yields

```text
36/125-U_n=
3(n-1)(79n^3+848n^2+2107n+366)
/[125(n+4)^2(17n^2+n+2)] >=0.                      (5.4)
```

Equality occurs at `n=1`. Equations (2.7), (5.1), and (5.2)--(5.4) now give

```text
C_3(B,n) <=(3/4)M_n <=(3/4)(36/125)=27/125.        (5.5)
```

The factor `d=r+1` in (5.2) is exactly the number of retained observations
restored after the average in Lemma 4.1. Thus (5.5) has neither a missing
`d` nor an extra `d+1` or `pi_a`.

## 6. Separate `n=0` and other boundaries

At `n=0`, only `r=0,d=1,a=0` occurs and

```text
eta^(3)_(0,0)=(3/2)/w_4=9/16.                      (6.1)
```

The exact accepted degree-one matrix is

```text
G_(1,0)=
[1/2, 0, 0;
 0, 1/5, -sqrt(6)/10;
 0, -sqrt(6)/10, 18/35],                           (6.2)
```

whose norm is

```text
rho_1=(25+sqrt(415))/70<2/3.                       (6.3)
```

The last inequality is equivalent to `9*415<65^2`. Lemma 4.1 at `d=1` is
the exact one-observation actual-history envelope bound, including the
separate `B=1` deletion. Therefore

```text
C_3(B,0)
 <=(9/16)rho_1 Sbar_(B,1,0)
 <9(25+sqrt(415))/1120 <3/8.                       (6.4)
```

The reported `3/8` is deliberately loose: both `rho_1<2/3` and
`Sbar_(B,1,0)<1` are strict. It is not inferred from the `n>=1` constant.

The `B=1`, `n=0`, and `r=n` boundaries have thus been handled separately.
No `L=7` or state graph was enumerated.

## 7. Dependencies, status, and reproducibility

Accepted immutable inputs: M109/M114, M115/M116, M117/M121, M147/M151,
M157/M160, M162/M165, M173/M177, M179/M184, and M185/M190. M193 proves
Lemma 4.1, the exterior maximum (5.4), and Theorem 1.1 from those inputs.

Run from this directory:

```text
python3 -B exact_check.py --output exact_results.json
```

The checker uses standard-library `Fraction`, `seed=null`, imports no
predecessor, compares the closed average with direct beta integration for
named `B=1,2,3,8,16` and every `1<=d<=30`, regenerates the coefficient
certificates, and checks the exact exterior through `n=30`. The proof above,
not the finite grid, certifies all `B,d,n`.
