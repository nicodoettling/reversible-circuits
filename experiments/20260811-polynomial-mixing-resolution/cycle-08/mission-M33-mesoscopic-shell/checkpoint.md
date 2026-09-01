# M33 halfway checkpoint: entropy-matched mesoscopic boundary family

## Frozen theorem under final constant audit

Let `N>=10^6`, `m=4N^3+4`, `M=binom(N,2)`, `d=N-1`, and
`E=binom(d,2)`.  With the project convention and original lazy exact kernel,
put

```text
A_N=floor(N log(N+1)/100).
```

The proof below gives, simultaneously for every `1<=a<=A_N`,

```text
pi(V^(a))<=exp(-4N^2),
Phi_pm^K(V^(a))>=N^(-25).                              (C.1)
```

Since `A_N/log N -> infinity`, this is genuinely beyond the logarithmic M31
range.  The numerical exponent and threshold are deliberately loose.

## 1. Minimal active-cluster encoding

Take the M31 overlap-cluster certificate for `y in V^(a)`.  Shrink every
active hull to its first and last crossing factors.  Removed prefixes and
suffixes are internal, so the shrunken ordered product remains in the cut
subgroup.  For length `l`, set

```text
q=ceil((l-1)/4).
```

Then `q` is no larger than the number of updates in the original overlap
cluster,

```text
l in {4q-2,4q-1,4q,4q+1},             sum_j q_j<=a.   (C.2)
```

For a cut with `e` internal and `x=M-e` crossing transpositions, a block on a
fixed interval has at most

```text
x M^(l-2)                                                   (C.3)
```

choices: choose the first crossing and every middle factor; subgroup
membership forces the last crossing by its action on the cut side.  For
fixed ordered lengths, the number of disjoint interval layouts is at most
`m^c/c!`.  Combining (C.3) with the dense direct-product trace gives

```text
O_P(a)
 <=4 e^m/|H_P| (M/e)^(4a) T_a(beta_P),                 (C.4)

beta_P=m x/e^2,
T_a(beta)=1+sum_{Q=1}^a sum_{c=1}^Q
 binom(Q-1,c-1)(4beta)^c/c!.
```

This removes the spurious ordered-placement `C_0^a` loss from M31.

## 2. Exact two-crossing source blocks

Fix the isolate cut `{z}|[d]`.  For a source interval with endpoints
crossing, let the first crossing be `s=(z,i)`, let the internal middle word
have product `g`, and take the last crossing to be `g^(-1)sg`.  Then

```text
s g (g^(-1)sg)=g.                                      (C.5)
```

Thus replacing each internal middle segment by this excursion does not change
the product of the internal skeleton.

If the interval length satisfies (C.2), this block can be made internal in
exactly `q` positive local updates.  While the two crossings are more than
four positions apart, a same-product `H_5` outcome shifts the last crossing
left through four internal factors.  One final `H_3,H_4`, or `H_5` resamples
the window containing both crossings to an internal factorization.  When its
length is two, one following internal padding position supplies the required
`H_3`; this is not an `L=2` update.

## 3. Product rigidity from distinct excursion states

For a fixed internal skeleton, let `P_j in H` be the prefix permutation before
source block `j`.  Its state after the first crossing is

```text
y_j=P_j(i_j) in [d].                                   (C.6)
```

The complete block product is internal and independent of `i_j`, so the
`P_j` are skeleton-determined.  Choose the `i_j` so that all `y_j` are
distinct.  There are exactly `(d)_c` choices.

Outside a pair the prefix image of `z` is `z`; between its two crossings it
is `y_j`.  A contiguous crossing interval has product in the isolate subgroup
exactly when its prefix states at the two ends agree.  Distinctness implies
that it must begin at the first crossing of one pair and end at the second
crossing of a later pair.  Hence every subgroup-valued active cluster contains
whole consecutive source pairs.  This rules out the three-crossing regrouping
that invalidates a parity-only argument.

Require at least two internal positions between source intervals.  If a
cluster contains consecutive pairs of budgets summing to `Q`, its hull has
length at least

```text
sum_j(4q_j-2)+2(number_of_pairs-1)=4Q-2,               (C.7)
```

so it needs at least `Q` update windows.  Reserve four trailing internal
positions.  A final `H_5` shift of the rightmost last crossing enlarges its
pair by four; every cluster grouping containing that pair now needs one extra
window.  A total-budget-`a` source therefore moves outside `V^(a)` in one
actual `H_5` step.

## 4. Robust skeleton and source count

Erase the `2c` crossing coordinates.  Require the remaining length-`m-2c`
identity word on `[d]` to stay connected after deletion of any union of `a`
five-windows.  The same crude cut union bound as M31 has logarithm

```text
a log m+d log 2+log(d!)-2(m-2c-5a)/d <=-N^2,           (C.8)
```

uniformly for `c<=a<=A_N`.  At least `E^(m-2c)/d!`
robust skeletons therefore exist for every layout.

For fixed lengths, layouts with two-position internal gaps and four trailing
positions number at least

```text
(m-8a)^c/c!.                                           (C.9)
```

Put

```text
beta=md/E^2,              beta_-=(m-8a)d/E^2,
eta_c=(d)_c/d^c,
C=ceil(2sqrt(80a)).
```

The total boundary-source count `B_a` obeys

```text
B_a >=E^m/d! S_a,
S_a=sum_{c=1}^{min(a,C)}
 binom(a-1,c-1)(4beta_-)^c eta_c/c!.                  (C.10)
```

The map from skeleton, layout, and first-crossing choices to the source word
is injective because the ordered crossing positions identify the consecutive
pairs.

## 5. Entropy match

For the isolate cut, `beta<=20`, so `lambda=4beta<=80`.  Write

```text
w_{a,c}(lambda)=binom(a-1,c-1)lambda^c/c!.
```

For `c<=C<=d/2`,

```text
eta_c>=exp(-C^2/d)>=N^(-5),                            (C.11)
```

and replacing `beta_-` by `beta` costs less than `e`.  For `c>=C`,

```text
w_{a,c+1}/w_{a,c}
 =lambda(a-c)/[c(c+1)]<=1/4.                           (C.12)
```

Thus the large-`c` tail is controlled by its first term, and

```text
T_a(beta)<=N^9 S_a.                                   (C.13)
```

Here the factor `a` accounts for all total budgets `Q<=a`; it is polynomial.
Also

```text
(M/E)^(4a)<=N,
```

because `M/E=N/(N-2)` and `a<=A_N`.  Summing the `N` isolate cuts in (C.4)
therefore costs only another polynomial.

For non-isolate cut size `s>=2`, use `beta_P<=200s`, `M/e<=5/2`, and

```text
T_a(beta_P)
 <=1+sqrt(800sa) exp(2sqrt(800sa)).                    (C.14)
```

The factorial cut ratio contributes
`exp[-8N(s-1)(N-s-1)]`, which dominates (C.14),
`(5/2)^(4a)`, and all labeled-cut multiplicities for `N>=10^6`.  Their total
is smaller than `E^m/d!`, hence smaller than (C.10).

The resulting deliberately rounded comparison is

```text
|V^(a)|<=N^12 B_a.                                    (C.15)
```

The same outer count divided by `|Omega|>=2M^m/N!` gives the global
orientation in (C.1).

## 6. Full-kernel flow

The final rightmost `H_5` output has conditional probability at least
`M^-4`.  Including laziness, block-size selection, and scan position gives

```text
p_exit>=1/[6(m-4)M^4].                                 (C.16)
```

Tail robustness forces any hypothetical alternate initial cut to be the
isolate cut.  Product rigidity and (C.7) then put the target outside
`V^(a)`.  Retaining only these `Q_5` transitions and using (C.15) gives

```text
Phi_pm^K(V^(a))
 >=N^-12/[6(m-4)M^4]
 >=N^-25.                                              (C.17)
```

All `Q_3,Q_4,Q_5` terms not charged in (C.17) are nonnegative.  The final
report will retain the conservative exponent `25` and make the small-regime
calibration/nonterminal scope explicit.
