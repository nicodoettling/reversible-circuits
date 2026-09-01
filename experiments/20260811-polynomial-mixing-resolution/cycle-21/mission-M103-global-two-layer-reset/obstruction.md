# Exact obstruction to the global two-layer reset defect

Date: 2026-08-12. This note concerns only the auxiliary full nonlazy
stationary-flow parking-degree projection in the minimal long-cycle sector.

## Statement

Let

```text
U(s,K,R,B)=q_(s,B)(1-q_(s,B)) K/(R+1),
r_U=U-A-QU,
```

with the frozen M90 normalization

```text
Q(x,y)=rho_s(k,t) nu_(K,R,k)(j),       j=1,...,k,
A(x)=sum_e [theta_e^2/Q_G(e)](1-q_(y_e)).
```

Every live attachment rank is retained. Then the proposed global two-layer
condition

```text
(I+Q)r_U(x)>=0                                      (1)
```

is false. At the reachable fresh context

```text
x=(s,K,R,B)=(30,1,0,10),
```

exact rational arithmetic gives

```text
r_U(x)       = -0.003687096818561213...,
(Qr_U)(x)    =  0.003535610344928366...,
(I+Q)r_U(x) = -0.00015148647363284748... < 0.      (2)
```

The normalized value is

```text
(I+Q)r_U(x)/U(x)=-0.006914605163495121... .        (3)
```

Every displayed sign is exact; `two_layer_exact.json` contains the complete
numerators and positive denominators.

## Proof

The transformed recurrence is

```text
g=A+Qg,
```

and the local defect is `r_U=U-A-QU`. Algebra therefore gives

```text
(I+Q)r_U
 = U-A-QU + QU-QA-Q^2U
 = U-A-QA-Q^2U.                                    (4)
```

The standalone `two_layer_exact.py` evaluates (4) through the equivalent
form `r_U+Qr_U`. Its ingredients are finite rational sums:

```text
w_a=a^(a-1)/a!,
c(n,p)=p n^(n-p-1)/(n-p)!,
rho_s(k,t)=w_t c(s-t,k-1)/(k!w_(s+1)),
nu(j)=binom(R+j,j)binom(K-R-1+k-j,k-j)/binom(K+k,k).
```

For each root group it first verifies

```text
sum_(j=0)^k nu(j)=1,
```

then sums every live `j=1,...,k`; `j=0` is the killed branch. Canonical reset
energy is evaluated from the full grouped basin sum `theta_e^2/Q_G(e)` with
exactly one weighted reward `1-q_(y_e)`. Thus no right-heavy `j=k` limiting
shortcut enters (2).

Every live child `y=(t-1,K+k,R+j,B)` satisfies

```text
P(x)-P(y)=s-t-k+j+1>=j>=1,
P=s+K-R,                                           (5)
```

so all required sums are finite. The witness has `(K,R)=(1,0)` and is a
fresh context in the accepted reachable closure. It is active because
`s=30>=2` and `1<=B=10<=s`. Equations (2)--(3), whose exact numerator is
strictly negative and denominator strictly positive, prove the claim.

## What the obstruction does not prove

Nilpotence still gives the complete identity

```text
U-g=(I-Q)^(-1)r_U=sum_(d>=0)Q^d r_U.               (6)
```

The negative first pair in (2) does not determine the sign of (6). A
standalone exact finite-DAG calculation at the same witness gives

```text
weighted full resolvent / U   =0.7372496452184509...<1,
unweighted full resolvent / U =0.8267268839096050...<1.          (7)
```

Both margins and their exact rational representations are stored in
`two_layer_exact.json`. Thus (1) is refuted as a sufficient proof template,
but neither surviving full-excursion inequality is refuted.

The next standalone obligation is therefore:

> **FULL RESET EXCURSION.** For every reachable active context `x`, prove
> ```text
> [(I-Q)^(-1)A](x)<=U(x),
> ```
> or prove the stronger corresponding unweighted resolvent bound.

A fixed block larger than two may be explored, but another finite-depth
pairing is not promoted without a uniform sign theorem; the exact witness
shows why local compensation can alternate across depths.

