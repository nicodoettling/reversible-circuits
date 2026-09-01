# M140 final report: scalar Cayley lemma and corrected auxiliary L=5

Date: 2026-08-13 UTC.  Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and claim status

Verdict: **PROMOTE TWO PROVED AUXILIARY RESULTS FOR FRESH REFEREE AUDIT**.

**PROVED:** for every integer `s>=100`, the exact canonical-basin scalar
coefficient satisfies

```text
C_s<74969/100000<3/4.
```

**PROVED, relative only to the accepted M109/M114, M115/M116, and M117/M121
recurrence and lower-excess inputs:** for every `s>=6,K>=1`,

```text
H(s,K,K-1,s-5)<q(1-q),
q=w_6 w_(s-5)/w_(s+1).
```

This theorem uses M138's valid corrected exceptional subtraction with one
power `a_E lambda_E`.  The rejected frozen M131 display with
`a_E lambda_E^2` is never used.

**UNRESOLVED and out of scope:** an auxiliary spectral gap, ROOT-MEAN LIFT,
an original-chain gap, polynomial mixing, Terminal A, and Terminal B.

## Field 2 — target, normalization, and convention

The project target remains uniform on fixed-length identity transposition
words.  This mission concerns only the auxiliary full nonlazy stationary-flow
parking-degree projection in the minimal-long-cycle sector.  Permutations
compose as `(pq)(x)=p(q(x))`, factors left-to-right.

With

```text
w_n=n^(n-1)/n!,
m_s(A,k)=k w_A c(s-A,k-1)/(k!w_(s+1)),

lambda(A,k)
 =(k-1)! sum_(p=1)^A [p/(p+k-1)!](A)_p/A^p,
```

the scalar coefficient is

```text
C_s=sum_(k=2)^s sum_(A=1)^(s-k+1)m_s(A,k)lambda(A,k)^2.
```

Every nominal positive attachment rank is represented before boundary
killing.  Only `j=0` and auxiliary rank-one targets are killed in the accepted
recurrence.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| M140 corrected auxiliary `L=5` resolvent | `H<=q(1-q)` for all right-heavy `L=5` contexts | N/A: no word sampler | N/A: auxiliary projection recurrence | scalar proof; literal subtraction; 1,222+4,212 exact coefficients | proved; fresh referee requested |

## Field 3 — exact tree-EGF first moment

For `T=z exp(T)`, Lagrange inversion gives `[z^n]T^p=c(n,p)`.  The identity

```text
w_A p(A)_p/A^p=c(A,p)
```

then converts the first lambda moment into

```text
sum_A m_s(A,k)lambda(A,k)
 =[z^s]sum_(j>=k)T^j/j! / w_(s+1)
 =P[Bin(s-1,1/(s+1))>=k-1].
```

The standalone checker verifies 435 exact rows for `2<=s<=30` with zero
failures.  This finite check audits the indexing; the displayed coefficient
derivation is the universal proof.

## Field 4 — Poisson majorant and exact rational bound

Put

```text
L_k=(k-1)!sum_(p>=1)p/(p+k-1)!.
```

Then `lambda<=L_k` and

```text
C_s=M_s-D_s,
M_s=sum_(k>=2)L_k P[X_s>=k-1],
D_s=sum_(k,A)m_s lambda(L_k-lambda)>=0.
```

Couple each Bernoulli with the positivity indicator of a Poisson variable of
parameter `-log(1-p)`.  The total parameter is

```text
(s-1)log(1+1/s)<(s-1)/s<1,
```

so `X_s<=st Pois(1)`.  The direction was self-attacked over 7,140
high-precision tail comparisons with zero failures; the coupling, not that
finite diagnostic, proves the claim.

A beta integral and the Poisson tail generating function give

```text
M_s<=U
 =integral_0^1(1-t^2)(e^t-1)/t dt
 =sum_(n>=1)2/[n(n+2)n!]
 <41554847/50803200<409/500.
```

## Field 5 — uniform endpoint mass and finite correction

For the nine pairs

```text
(k=2,A=1,...,4), (k=3,A=1,...,4), (k=4,A=1),
```

put `n=s-A`, `u=A+1`, and `h=k-2`.  The exact mass ratio is

```text
R=e^u(n/(n+u))^(n+u-1)product_(r=-h)^u(1+r/n).
```

The complete logarithmic estimate in the proof note has a nonnegative
first-order term and discards at most

```text
23612897/2962759680<1/100
```

uniformly for `n>=96,2<=u<=5,0<=h<=2`.  Hence

```text
m_s(A,k)>(99/100)w_A e^(-(A+1))/(k-2)!.
```

The exact bound `e<31967/11760<87/32`, together with
`L_2=1,L_3>9/16,L_4>3/8`, gives the inner correction

```text
D_0=78988317872/1121447071575>69/1000.
```

The usable lower correction retains the mass factor:

```text
(99/100)D_0=217217874148/3115130754375.
```

Therefore

```text
C_s<409/500-(99/100)(69/1000)
   =74969/100000<3/4.
```

This is a universal analytic theorem for all `s>=100`, not a finite scan.

## Field 6 — corrected reset and strict smallest boundary

For each exceptional endpoint,

```text
c_E=degree(E)rho(E),
b_E=rho(B_E)=c_E lambda_E,
a_E=rho(B_E intersect S_x)<=b_E.
```

The ordinary baseline after division by the initial split mass is
`q b_E lambda_E`.  Thus subtracting `q a_E lambda_E` is safe because the
remainder is `q(b_E-a_E)lambda_E>=0`.  The corrected reset is

```text
R_corr=q[C_s-sum_E a_E lambda_E]
       +sum_E theta_E^2/(q c_E).
```

The scalar checker reconstructs all 31 supported occurrences at each of
`s=6,7` and verifies `a_E<=b_E=c_E lambda_E` exactly, with zero failures.

At `s=6`, `B=1`; every nominal `t=2` child has rank one and is inactive,
its terminal charge is zero because `b_1=1`, and exactly 17 actual children
remain.  All 13 exact `s=6` Bernstein coefficients are positive; their
minimum is

```text
13461835439971/11861248695609600>0
```

at index zero.  The finite boundary is therefore strict for every `K>=1`.

## Field 7 — independent corrected certificates

The standalone M140 regenerator imports no predecessor source.  It rebuilds
32 supported roots, 31 exceptional occurrences, 11 live groups, all 31
nominal positive rank terms, the arbitrary-deficit descendants through
`L=3`, and the corrected one-power reset.

For `s=6,...,99`, all 1,222 exact one-variable Bernstein coefficients are
positive.  The global minimum is

```text
5307578203959502651/4736091661711441920000
```

at `s=7`, index zero.  Their canonical coefficient digest is
`733243ff50622263540085ff0d6d4b01246164cc8119003cacb5dbeda11684f7`.

For `s>=100`, the six Cayley ratios lie in `[4/11,187/500]`.  With heights
set to one and `C_s` set to `3/4`, the cleared slack has multidegree
`(1,1,2,2,2,2,12)`.  All 4,212 tensor Bernstein coefficients are positive;
the minimum is

```text
4360847276079323/50118750000000000000
```

at `(1,1,2,2,2,0,0)`.  Their canonical digest is
`2c1aa8475dba3ae3d3c09f587662facb78b1c11e14aec2d04ae8d87bb5adf22f`.
Exact off-grid identities pass.  A post-hoc comparison finds all 1,222 and
all 4,212 values exactly equal to M138's independently generated fractions.

Theorem `C_s<3/4` discharges the only scalar assumption in this tail
certificate, proving the corrected auxiliary `L=5` theorem for every
`s>=6,K>=1`.

## Field 8 — reproducibility and dependency audit

Run from this mission directory:

```text
python3 -B scalar_cayley_exact.py --output scalar_cayley_exact.json

python3 -B corrected_l5_certificates.py \
  --output corrected_l5_certificates.json \
  --reference-json \
  ../../cycle-31/mission-M138-m131-fresh-referee/independent_m131_referee.json
```

Environment: Python 3.12.3, standard library only, deterministic
`seed=null`.  Every theorem-critical finite calculation uses
`fractions.Fraction`.  Both result files report zero failures.  Full
coefficient lists are regenerated by the checker but compacted in the result
artifact to exact digests, row minima, and decisive boundary rows.

Immutable M138 hashes observed before freeze:

```text
report       bb6501ae5a7386e70e00ce520449af27aef4a0e32b944aff9a734f082d87cd5e
proof        a08a6d99d843c21f9f822b139f625ffe56e456c90e22ea2c4b899fb57c6573d6
checker      4e07c4e4202c764a56400945316604ddb2352d4de128aa8e45ec614f3a2ce94e
results      f631c9134b02c29a90e87d564e8a2dd8f020d714b9652679ef14b712fab9fc00
manifest     40bd1d07000e4517e8d1a1f5ac1b40ab3ca7530d8835a55b0f32a1e5ffdc328e
SHA256SUMS   5eb1b857b567b4f3256917cd6648c67aef4fd8cedced3edb59c8ab607ac4a50b
```

M109/M114, M115/M116, and M117/M121 supply only the accepted recurrence and
lower-excess theorems listed in the proof note.  M138 supplies the corrected
structural implication.  M131's rejected frozen theorem is not a positive
dependency.

## Field 9 — limitations, action, and hygiene

This mission closes the standalone scalar Lemma C and removes the last
assumption from the corrected auxiliary right-heavy `L=5` contraction.  It
does not by itself establish the weighted auxiliary contraction, an
auxiliary spectral gap, ROOT-MEAN LIFT, or mixing of the original chain.

The next action is a fresh referee audit of the immutable M140 payload,
prioritizing the EGF index shift, stochastic-order direction, uniform log
bound, `99/100` correction normalization, one-power reset subtraction,
strict `s=6` boundary, and both coefficient digests.  No package was
installed; no M131, M138, predecessor, coordinator, manuscript, project
skill, or other worker file was edited.
