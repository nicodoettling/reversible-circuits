# M138 independent proof audit of frozen M131

Date: 2026-08-13 UTC.

## 1. Audited claim, target, and verdict boundary

The surrounding project target is uniform on fixed-length identity
transposition words in `Omega(N,m)`.  Permutations compose as
`(pq)(x)=p(q(x))`, with factors displayed left-to-right.  The claim audited
here is only the auxiliary full nonlazy stationary-flow parking-degree
reset-excursion inequality

```text
H(s,K,K-1,s-5) <= q(1-q),
q=w_6 w_(s-5)/w_(s+1), s>=6, K>=1.
```

M131 claims this unconditionally for `6<=s<=99` and conditionally for
`s>=100` on the scalar lemma `C_s<=3/4`.

```text
FRESH REFEREE VERDICT: REJECT AS FROZEN.
MATERIAL NUMBERED OBJECTIONS: ONE (M-1 IN SECTION 6).
```

The obstruction is a formula/source mismatch in the decisive refined reset
subtraction.  A corrected theorem is independently salvaged in Sections 6--8,
but is not promoted by this report.  Lemma C is not attempted and remains
unresolved.  No auxiliary gap, ROOT-MEAN LIFT, original-chain gap, polynomial
mixing conclusion, Terminal A, or Terminal B is inferred.

## 2. Provenance and accepted dependency boundary

The supplied immutable M131 hashes match exactly:

```text
report       129326b37b8b401e90093012452205ea86db478e57ce6f8c2e24fb9024870eb3
proof        b4b22d9f98109709c7bd81b11b1c0408510ec2c7e6a2d9380601a31dda9c1628
checker      f8a77e8a02881649fe14fac1d8e71412c72680d600ae56d5fbdcdf314a18f724
results      ad8779c8b465110940b2cae351da4ace9df3c4c2d5fb4af379b882ae5fb6d217
manifest     db81797b3d6b56c36166844dde09da7d5552f265f8a65b72618f33836155069c
SHA256SUMS   20b239f7c3d979a5616ed56e3ecd81c1cf7969d5b604118c192e41f3e6bf96f7
```

All checksum inventories for M109/M114, M115/M116, M117/M121, and
M123/M128 pass.  The accepted positive dependencies used here are:

- M109/M114: the all-`j` finite-DAG recurrence, universal all-deficit `L=0`,
  and right-heavy contraction through `L=2`;
- M115/M116: the arbitrary-deficit `L=1` envelope and right-heavy `L=3`;
- M117/M121: the arbitrary-deficit `L=2` envelope and right-heavy `L=4`.

M123/M128 instead delimit discarded generic basin-frame routes.  M131 does
not use those refuted routes, and this audit finds no hidden reuse.

## 3. Exact `L=5` root structure, basins, and boundary

Write the six top-down Cayley ratios as `(b_s,...,b_(s-5))`, put
`B=s-5`, and let `z=1/(K+1)`.  For each `h=0,...,5`, the supported roots are

```text
(P,B+h),  P an ordered composition of 5-h.
```

Their exact normalized masses and contextual means reconstructed from the
root law and attachment law sum to one after division by `q`.  The counts are

```text
supported rows                  32
nominal exceptional basins      31
inactive endpoints               8
positive (k,t) groups           16
live deep groups                11.
```

The eight inactive endpoints are exactly those whose full composition begins
`(1,1)`.  Literal full-composition reconstruction has 23 active basins at
`s=6` and 47 at `s=7`.  At both `K=1,5`, all 23 active supported exceptional
currents and capacities equal the independent prefix formulas exactly.

Every `j=1,...,k` is retained before aggregation.  For a live group at height
`h`, the child has suffix excess `h-1` and deficit `k+1-j`.  At `s=6`, all
nominal `t=2` children have rank one and are absent.  The retained triples are
exactly

```text
(1,6,1);
(2,t,j), t=3,4,5, j=1,2;
(3,t,j), t=3,4, j=1,2,3;
(4,3,j), j=1,2,3,4,
```

for a total of 17.  The zero displayed charge for the absent `t=2` rows is
explained by `b_1=1`; no limiting convention is used.

## 4. Arbitrary-deficit `L=3` envelope

For `K+1=(1+az)/z` and deficit `D=K-R`, direct substitution into the binomial
attachment law gives

```text
nu(a,D,k,0)=(D)_k z^k / product_(r=0)^(k-1)(1+(a+r)z),

nu(a,D,k,j)=binom(k,j)(D)_(k-j)z^(k-j)
             product_(r=0)^(j-1)(1+(a-D+r)z)
             /product_(r=0)^(k-1)(1+(a+r)z).
```

The child parameters are `(a+k,D+k-j,h-1)`.  The root reset is bounded by
the accepted ordinary-basin inequality and exact exceptional currents; all
descendants are then charged inductively.  The new `L=3` level uses only the
accepted arbitrary-deficit `L<=2` envelopes.  This is a structural induction
on the finite DAG, not an extrapolation from the finite checks.

The fresh implementation reproduces the accepted closed `L=1` and `L=2`
formulas exactly on every tested context and checks the recursive `L=3`
bound.  Across all 504 contexts

```text
ell=1,2,3; ell+1<=S<=8; 2<=K<=8; 1<=R<K,
```

there are zero formula mismatches and zero exact-resolvent bound failures.

## 5. Basin coefficient and `C_s`

For a degree-`k` endpoint `E=(A,c_2,...,c_k)`, let

```text
c_E=k rho(E),  b_E=rho(B_E),  lambda_E=b_E/c_E.
```

Summing every refinement of the first total `A` gives exactly

```text
lambda(A,k)
 =(k-1)! sum_(p=1)^A [p/(p+k-1)!] (A)_p/A^p.
```

For `k=2`, telescoping gives `lambda(A,2)=A/(A+1)`.  The coefficient ratio

```text
(k-1)!(p+1)!/(p+k-1)! <= 2/k
```

is largest at `p=1`, so termwise comparison gives

```text
lambda(A,k)<=2A/[k(A+1)]<=1.
```

The fresh checker also verifies `b_E/c_E=lambda(A,k)` directly from literal
basins for `1<=A<=8,2<=k<=8`, with zero failures.

Aggregating endpoints by first total and degree gives

```text
C_s=sum_E c_E lambda_E^2
   =sum_(k=2)^s sum_(A=1)^(s-k+1)
      [w_A c(s-A,k-1)/(k!w_(s+1))] k lambda(A,k)^2.
```

The endpoint-degree marginal is

```text
sum_A w_A c(s-A,k-1)/(k!w_(s+1))
 =binom(s-1,k-1)s^(s-k)/(s+1)^(s-1).
```

Independent exact checks of every degree through `s=20` have no mismatch.
The six audited `C_s` values equal M131 exactly, including
`C_100=.7145417887532552...`.  This finite value does not prove Lemma C.

## 6. M-1: frozen refined-reset formula does not match the certificate

Let `S_x` be the supported root set at the `L=5` context and define, for each
nominal exceptional endpoint,

```text
a_E=rho(B_E intersect S_x),
b_E=rho(B_E),
c_E=degree(E)rho(E),
lambda_E=b_E/c_E.
```

Then exactly

```text
0<=a_E<=b_E=c_E lambda_E,
C_s=sum_E c_E lambda_E^2=sum_E b_E lambda_E.
```

If endpoint `E` were ordinary, its current would be `-q b_E`, so its
contribution after division by the initial `q` would be

```text
(q b_E)^2/(q c_E)=q b_E lambda_E.
```

Consequently the following sharper subtraction is rigorous:

```text
R_corr
 =q[C_s-sum_(exceptional E) a_E lambda_E]
  +sum_(exceptional E) theta_E^2/(q c_E).          (6.1)
```

Indeed, the amount removed from each ordinary baseline is
`q a_E lambda_E<=q b_E lambda_E`; the unremoved remainder is nonnegative.
Inactive exceptional edges are harmless because the envelope includes their
nonnegative exact square terms.  In M131's normalized support notation
`a_E=q(rho_supported/q)`, equation (6.1) is precisely the operation in frozen
`l5_exact.py` line 372: multiplication by one power of `lambda_E`.

Frozen proof equation (5.1), however, prints

```text
R_written
 =q[C_s-sum_(exceptional E) a_E lambda_E^2]
  +sum_(exceptional E) theta_E^2/(q c_E).          (6.2)
```

Because `0<=lambda_E<=1`, (6.2) is a valid but strictly looser upper bound.
It is not the envelope certified by the frozen checker.  The mismatch is
decisive:

- at `(s,K)=(6,64)`, the normalized written-envelope value is exactly
  ```text
  239164429690896046891371756674
  /218369158864796713280022140625 > 1;
  ```
- the degree-12 Bernstein expansion of the written `s=6` slack has four
  nonpositive coefficients, with index two equal to
  ```text
  -19717205656843140443/125254786225637376000 < 0.
  ```

Thus the frozen assertion that equation (5.1)'s envelope receives 1222
positive coefficients is false.  This is material, because the scalar sign
is the step proving the displayed finite-range theorem.  It cannot be treated
as a wording-only correction even though the sharper replacement (6.1) is
short and valid.

## 7. Corrected finite certificate, independently salvaged

After replacing (6.2) by the proved sharper formula (6.1), the independent
checker forms

```text
T_s(z)=product_(a=1)^5(1+az)^2 [1-q-E_5(z)].
```

It evaluates directly at 13 nodes inside `[0,1/2]`, inverts the Bernstein
evaluation matrix over exact rationals, and verifies an independent off-grid
identity.  This differs from M131's integer-node Lagrange path.

For every `s=6,...,99`, all 13 coefficients are positive.  Across all 1222,
the exact minimum is

```text
5307578203959502651/4736091661711441920000 > 0
```

at `s=7`, index zero.  Every one of the 1222 exact fractions equals M131's
frozen checker output after the correction.  Twenty selected full `L=5` DAG
rows, all 504 arbitrary-deficit rows, and all six selected `C_s` values also
match exactly.  Therefore the corrected auxiliary finite-range theorem is
independently salvaged, but it is not promoted from this rejection report.

## 8. Conditional tail certificate and Lemma C boundary

For `b_n=(n/(n+1))^(n-1)`, the function
`(x-1)log(1+1/x)` is increasing, so `b_n` decreases.  Also `b_n>1/e>4/11`,
using `e<11/4`.  At `s>=100`, the smallest ratio index is 95, and

```text
500*95^94 < 187*96^94
```

gives `b_95<187/500`.  Thus all six ratios lie in
`[4/11,187/500]`.

The corrected envelope is increasing in `C_s`.  Every path height enters a
coarse child reset with a nonnegative coefficient, and descendant recursion
uses only nonnegative masses and attachment probabilities; induction therefore
shows that replacing all heights by one enlarges the envelope.  Under the
unproved assumption `C_s<=3/4`, the resulting cleared slack has multidegree

```text
(1,1,2,2,2,2,12).
```

The independent checker evaluates at Bernstein nodes inside the full
seven-dimensional box and transforms one axis at a time.  All 4212 exact
coefficients are positive.  The exact minimum is

```text
4360847276079323/50118750000000000000 > 0
```

at `(1,1,2,2,2,0,0)`, and an independent off-grid identity passes.  All
4212 exact fractions equal M131's checker output after using (6.1).

Hence the following corrected implication is salvaged but not promoted:

> If `C_s<=3/4` for every `s>=100`, then the corrected auxiliary `L=5`
> envelope proves `H<=q(1-q)` for every `s>=6,K>=1`.

Lemma C itself remains the first unproved step.  No monotonicity or asymptotic
bound for `C_s` is inferred from its finite values.

## 9. Coarse obstruction and rational `e` audit

The inherited `beta<=degree` envelope is indeed refuted only as a proof
template.  At `(s,K)=(7,4096)`, independent exact arithmetic gives

```text
coarse envelope / target = 1.0194850323300793... > 1,
actual H / target         = 0.40251029996439475... < 1.
```

Both exact fractions equal M131's output.  This is not an `H` counterexample.

The ratio-box and `e` inequalities are also correct.  Exact arithmetic gives

```text
sum_(n=0)^6 1/n! + 1/4410 = 31967/11760 < 87/32,
```

so `e<87/32` and therefore `2(3-e)>9/16`; the tempting opposite inequality
is false.  Also

```text
e>sum_(n=0)^5 1/n!=163/60
```

proves the corrected strict inequality `2(3-e)<17/30`.  As M131 states,
this does not prove Lemma C.

## 10. Final disposition

No error was found in the root structure, literal basin currents, all-rank
recurrence, arbitrary-deficit `L=3` construction, `lambda` and `C_s`
identities, coarse-envelope scope, ratio box, or rational `e` correction.
The implemented one-power subtraction and all certificates survive a fully
independent exact audit.

Nevertheless, the immutable proof and report identify their `E_5` using the
two-power subtraction (6.2), while the immutable source certifies (6.1).
The written envelope demonstrably fails the claimed sign.  Therefore:

```text
FINAL VERDICT: REJECT AS FROZEN.
MATERIAL OBJECTION M-1: lambda^2 in proof versus lambda in certified source.
CORRECTED THEOREM: independently salvaged, not promoted.
LEMMA C: unresolved and not attempted.
```
