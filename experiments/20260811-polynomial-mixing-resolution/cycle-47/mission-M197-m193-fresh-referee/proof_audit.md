# M197 independent proof audit of frozen M193

Date: 2026-08-13 UTC.

## 1. Immutable gate, target, and scope

Before reading M193's conclusions, I verified all eight entries in its
`SHA256SUMS`. Its exact nine-file directory inventory agrees with the frozen
manifest, and its checksum-ledger digest is

```text
aff1302508bfc61727e47649f0810183ff7fc7f28e7840bc3bbc239e828af0b2.
```

Every checksum in the eighteen accepted dependency ledgers cited by M193
also passes. Neither M193 nor any predecessor was edited.

The audited object is only the fresh actual-history `h=3` retained sector of
the normalized full unweighted reset excursion `F=H/q` in the auxiliary
nonlazy minimal-long-cycle parking projection. The project target remains
uniform fixed-length identity transposition words, with `(pq)(x)=p(q(x))`
and displayed factors left-to-right. No reset, `h>=4`, total AMV, all-`L`,
gap, original-chain, mixing, or terminal claim is under audit.

## 2. Exact branch and observation normalization

At fixed degree `d`, a retained attachment satisfies

```text
a=0,...,d-1,       D=a+1=1,...,d.                 (2.1)
```

Thus there are exactly `d` retained branches. The value `a=d` is killed
before the history direct sum and is not restored by survival conditioning.

For the fresh parent, `L_a=binom(d,a)U^a(1-U)^(d-a)` and direct beta
integration gives

```text
pi_a=E_parent L_a=1/(d+1),
L_a dmu_parent=pi_a dmu_a,
mu_a=Beta(a+1,d-a+1).                              (2.2)
```

Therefore the normalized branch feature satisfies

```text
(eta/pi_a)E_parent[L_a^2||Phi_a||^2]
 =eta E_mu_a[L_a||Phi_a||^2].                     (2.3)
```

One likelihood remains inside the branch matrix `G_(d,a)`. The factor
`pi_a` is already included there, while `eta` is common outside. Hence the
exact sector expression has the multiplicity

```text
sum_r eta^(3)_(n,r) sum_(a=0)^(d-1) B_(d,a),
d=r+1,                                             (2.4)
```

with no extra `pi_a`, `1/d`, `1/(d+1)`, or survival factor. This independently
confirms M193's sensitive normalization.

## 3. Clean-room closed beta average

Starting from M185/M190's accepted raw suffix-two trace coordinates, not from
M193's closed formula, the clean-room checker constructs

```text
Sbar_(B,d,a)=R_2+D_0+(2/3)W_1.                    (3.1)
```

It then sums exactly over `D=1,...,d`. Hockey-stick identities give

```text
(1/d)sum_D E U_D=(d+1)/[2(d+2)],
(1/d)sum_D E U_D^j=(d+1)/[(j+1)(d+j+1)],
j=2,3,4.                                           (3.2)
```

Expanding every reset square, both degree-two likelihood ratios, and all
three unary terms regenerates exactly M193 equations (3.3)--(3.4), including
the factors `1/3` and `2/3`. Thus

```text
A_(B,d):=(1/d)sum_(a=0)^(d-1)Sbar_(B,d,a)          (3.3)
```

is M193's stated rational function. The `1/d` is merely the arithmetic
average; it is multiplied back in (2.4).

The diagnostic obstruction also reproduces independently:

```text
Sbar_(3,20,19)=10249528643/7684875000>1,
A_(3,20)=443845801/614790000<1.                    (3.4)
```

This confirms that M193 averages observations and does not reinstate the
refuted pointwise envelope cap.

## 4. Universal `B>=2` certificate

For `y_B=w_B/w_(B+1)=(B/(B+1))^(B-1)`, differentiation of
`(x-1)log(1+1/x)` proves that `y_B` decreases to `e^-1`. Consequently

```text
y>=e^-1>1/3,       b=y_B y_(B+1)<=y_2y_3=3/8.     (4.1)
```

Increasing `H0,H1` to one is sign-safe because their coefficients are
positive. The independently derived relaxed average has

```text
dA#/db=
[4d^2+36d+104-b(3d^2+27d+60)]/[18(d+3)(d+4)]>0.  (4.2)
```

At `b=3/8`, eight times the numerator is
`23d^2+207d+652>0`, so setting `b=3/8` enlarges the expression.

In `q`, the second derivative is `-(4y+3)/(9y)<0`. The unconstrained maximum
is exactly

```text
q*=y(d^2+11d+22)/[(d+2)(d+3)(4y+3)].              (4.3)
```

Using the unconstrained maximum is valid regardless of the actual Cayley
range. After substituting `b=3/8,q=q*`, the derivative in `y` is a negative
positive-denominator multiple of a polynomial whose `(y^2,y,1)` coefficient
rows, from `d^6` through `d^0`, are

```text
(512,768,273), (11520,17280,6015),
(105472,158208,53583), (492160,738240,240705),
(1231488,1847232,570612), (1571840,2357760,673620),
(803328,1204992,306672).                            (4.4)
```

Every entry is positive, so the maximum decreases in `y`; setting `y=1/3`
is sign-safe. The resulting slack numerator, after `d=1+e`, has ascending
coefficients

```text
5726736,18788964,16784028,6721029,1351327,131535,4829. (4.5)
```

All are positive for `e>=0`. This independently proves `A_(B,d)<1` for
every `B>=2,d>=1`.

## 5. Separate `B=1` boundary

At `B=1`, direct Cayley values are

```text
y=1, b=2/3, q=9/16, H0=1/2, H1=1/3.              (5.1)
```

Accepted M179/M184 activity accounting says the rank-one reset and deep
suffix-one targets are inactive; deleting them removes squared Hilbert
coordinates and cannot increase the exact trace. M185/M190 already certifies
that retaining the corresponding nonnegative nominal coordinates is an upper
envelope.

Independent substitution gives

```text
A_(1,d)=
[17591d^4+187970d^3+679425d^2+1233430d+1075144]
/[69120(d+2)(d+3)(d+4)(d+5)],                     (5.2)
```

whose slack numerator is

```text
51529d^4+779710d^3+4228095d^2+9411050d+7219256>0. (5.3)
```

Thus `A_(1,d)<1` without applying any `B>=2` activity or ratio bound.

## 6. Exterior, multiplication, and `r=n`

Direct cancellation of the grouped root mass and child/parent split ratio
gives

```text
eta^(3)_(n,r)=(3/2)c(n,r)/[(r+1)!w_(n+4)].        (6.1)
```

For `n>=1`, `r=1,...,n`, including `r=n` with `c(n,n)=1`. Exact summation
reproduces

```text
M_n:=sum_r(r+1)eta^(3)_(n,r)
 =(3/2)(n+1)^n(n+2)(n+3)/(n+4)^(n+2).             (6.2)
```

The first three binomial terms yield an upper bound `U_n`, and clean-room
subtraction gives

```text
36/125-U_n=
3(n-1)(79n^3+848n^2+2107n+366)
/[125(n+4)^2(17n^2+n+2)]>=0.                      (6.3)
```

The maximum `36/125` occurs at `n=1`. Since M185/M190 proves the complete
three-mode inequality `B_(d,a)<=(3/4)S_a`, Sections 3--5 give

```text
sum_a B_(d,a)<(3/4)d.                              (6.4)
```

Here `d=r+1` is exactly the number of retained observations multiplied back
after (3.3). Combining (6.2)--(6.4) produces

```text
C_3(B,n)<=(3/4)(36/125)=27/125.                   (6.5)
```

There is no omitted observation count or extra Bayes factor.

## 7. Exact `n=0` boundary

At `n=0`, only `r=0,d=1,a=0` occurs and

```text
eta^(3)_(0,0)=(3/2)/w_4=9/16.                     (7.1)
```

Independent diagonalization of the exact matrix

```text
[1/2, 0, 0;
 0, 1/5, -sqrt(6)/10;
 0, -sqrt(6)/10, 18/35]
```

gives top eigenvalue

```text
rho_1=(25+sqrt(415))/70<2/3,                      (7.2)
```

where the last inequality is certified by `9*415<65^2`. At `d=1`, the
observation average is the one actual-history envelope and Sections 4--5
prove it strictly below one; the explicit `B=1` nominal value is
`2957/23040`. Therefore

```text
C_3(B,0)<9(25+sqrt(415))/1120<3/8.                (7.3)
```

The `3/8` statement is deliberately loose and is independent of (6.5).

## 8. Numbered objections and verdict

1. **Material objections: none.** The observation count, Bayes normalization,
   raw-history average, universal signs, sector multiplication, and all stated
   boundaries pass independent derivation.
2. **Nonmaterial external hygiene caveat:** immutable M117, M162, and M165
   currently contain unledgered `__pycache__` directories. Every recorded
   payload checksum passes, M193's own exact inventory is clean, and these
   external caches do not affect M193's proof or reproducibility. This is not
   an objection to M193.
3. **Scope guard:** acceptance covers only the fresh actual-history `h=3`
   sector. It gives no reset, `h>=4`, total AMV, all-`L`, gap, mixing, or
   terminal conclusion.

```text
FINAL REFEREE VERDICT: ACCEPT FROZEN M193.
```

## 9. Reproducibility

From M197 run

```text
python3 -B independent_symbolic.py --output independent_results.json
```

The script uses SymPy 1.12 exact arithmetic, `seed=null`, imports no M193
artifact, and starts from the accepted raw M185/M190 history coordinates.
It performs no `L=7` or state-graph enumeration. Universal acceptance rests
on the analytic identities and coefficient signs above, not the finite
exterior diagnostic rows.
