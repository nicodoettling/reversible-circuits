# M140 halfway checkpoint

Date: 2026-08-13 UTC.

## Decisive state

The standalone scalar lemma has a complete proof candidate:

```text
C_s < 74969/100000 < 3/4 for every s>=100.
```

For

```text
m_s(A,k)=k w_A c(s-A,k-1)/(k!w_(s+1)),
L_k=(k-1)! sum_(p>=1)p/(p+k-1)!,
```

the tree equation `T=z exp(T)` gives exactly

```text
sum_A m_s(A,k)lambda(A,k)
 =P[Bin(s-1,1/(s+1))>=k-1].
```

The binomial is stochastically dominated by `Pois(1)`: couple each Bernoulli
as the positivity indicator of a Poisson variable of parameter
`-log(1-p)`, and use
`(s-1)log(1+1/s)<(s-1)/s<1`.  Hence the first part of
`lambda^2=L_k lambda-lambda(L_k-lambda)` is at most

```text
U=sum_(n>=1)2/[n(n+2)n!]
 <41554847/50803200<409/500.
```

## Finite correction and normalization

For the nine pairs

```text
(k=2,A=1,...,4), (k=3,A=1,...,4), (k=4,A=1),
```

an elementary uniform log estimate proves

```text
m_s(A,k)>(99/100)w_A exp(-(A+1))/(k-2)!, s>=100.
```

Its discarded logarithmic error is at most
`23612897/2962759680<1/100`.  With `e<87/32`, `L_2=1`,
`L_3>9/16`, and `L_4>3/8`, the inner selected correction is

```text
D0=78988317872/1121447071575>69/1000.
```

The usable correction includes the mass factor and is therefore

```text
(99/100)D0=217217874148/3115130754375.
```

This distinction repairs a potential normalization ambiguity in the supplied
route.  Thus

```text
C_s<409/500-(99/100)(69/1000)=74969/100000<3/4.
```

The standalone checker reports zero failures on 435 exact first-moment rows,
the theorem-critical rational margins, selected exact masses, and all 31
literal exceptional occurrences at each of `s=6,7`.  The latter confirm the
corrected safe subtraction `q a_E lambda_E` from the ordinary baseline
`q b_E lambda_E`, using `0<=a_E<=b_E=c_E lambda_E`.  The rejected
`a_E lambda_E^2` display is not used.

## Remaining work before freeze

Write the complete analytic proof and independently regenerate the corrected
1222 finite and 4212 tail Bernstein certificates.  Then state the resulting
unconditional auxiliary `L=5` theorem with the `s=6` boundary explicit.
No auxiliary gap, ROOT-MEAN LIFT, original-chain gap, mixing theorem, or
project terminal follows.
