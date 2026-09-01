# M252 conditional full-WPCR theorem

Date: 2026-08-14 UTC.

Status: **proved conditional on DV**, using accepted DE. Full PCR remains
unresolved. This note makes no SCBR or downstream inference.

## 1. Exact setting and mixture

Use M180/M182 and M186/M189's convention (pq)(x)=p(q(x)), with displayed
factors multiplying left-to-right. Put

~~~text
n=3k,  k>=3 odd,  m=(n-1)/2.
~~~

This fixed-cell calculation concerns the uniform law on minimal length-(n-1)
transposition factorizations of the ambient cycle and the nonlazy cyclic
rank-two coordinate kernel. It is not the global identity bridge or the lazy
{3,4,5} heat-bath chain.

The locked source decomposition has equal nonnegative channel masses at the
two sources. Its J=0 law cancels. Write the remaining masses as
alpha_1,alpha_2, with 0<=alpha_j<=1. For j=1,2 define

~~~text
P_d^(j)=M_1^(j)(d),             N_d^(j)=M_1^(j)(d)+M_2^(j)(d),
C_D^(j)=sum_(d=2)^D P_d^(j),   A_D^(j)=sum_(d=2)^D N_d^(j).       (1.1)
~~~

The full M186 prefixes are exactly

~~~text
C_D=alpha_1 C_D^(1)+alpha_2 C_D^(2),
A_D=alpha_1 A_D^(1)+alpha_2 A_D^(2).                              (1.2)
~~~

For channel two, M192's literal observables give

~~~text
C_D^(2)=E_B[Y_D|J=2]-E_A[Y_D|J=2],
A_D^(2)=E_B[X_D|J=2]-E_A[X_D|J=2].                               (1.3)
~~~

These include shared-endpoint triangles, the unequal disjoint-mass endpoint,
same/cross doubles, seams, and collision multiplicities.

Accepted M248/M249 proves DE for both observables with common constant 7164.
DV remains a hypothesis: assume it holds for X_D,Y_D with absolute constant
K_V. Let K_E be an absolute constant in M192/M195's accepted scalar estimate

~~~text
|E_u|<=K_E sqrt(u)/k.                                             (1.4)
~~~

## 2. Accepted channel-one coefficient bounds

Put

~~~text
delta_d=rho_B(d)-rho_A(d),
epsilon_d=sum_(a+b=n-d)delta_a rho_A(b).                           (2.1)
~~~

M186/M189 proves

~~~text
P_d^(1)=delta_d,                 N_d^(1)=delta_d+epsilon_d,        (2.2)
sum_a |delta_a|/a <=K_1/k,                                     (2.3)
sum_(a,b)|delta_a|rho_A(b)/(n-a-b)<=K_2/k.                      (2.4)
~~~

Here K_1,K_2 are absolute. The two-run residual size d=n-a-b is at
least two. Grouping (2.4) by d and applying the triangle inequality inside
this fixed conditional channel gives

~~~text
sum_(d>=2)|epsilon_d|/d <=K_2/k.                                  (2.5)
~~~

Thus M189's weighted two-run estimate includes the exact triangle step
needed below; it is not merely a bound on the final signed charge.

## 3. Discrete Hardy--Abel transfer

For a finite sequence x_2,...,x_m, put X_D=sum_(d=2)^D x_d. Then

~~~text
|X_m|/m+sum_(D=2)^(m-1)|X_D|/D^2
 <=3 sum_(d=2)^m |x_d|/d.                                        (H)
~~~

Expand each prefix by the triangle inequality and interchange the finite
sums. The coefficient of |x_d| is

~~~text
1/m+sum_(D=d)^(m-1)1/D^2
 <=1/d+1/d^2+integral_d^infinity x^(-2)dx
 <=3/d,                                                           (3.1)
~~~

with the sum empty at d=m. This proves (H).

Apply (H) to delta_d and to delta_d+epsilon_d. Equations (2.3)--(2.5)
give

~~~text
(|A_m^(1)|+|C_m^(1)|)/m
 +sum_(D=2)^(m-1)(|A_D^(1)|+|C_D^(1)|)/D^2
 <=3(2K_1+K_2)/k.                                                 (3.2)
~~~

Since n=3k, the scaled channel-one WPCR constant is at most
18K_1+9K_2.

## 4. Conditional channel-two response

Under DV, M192/M195's disjoint Abel identity and (1.4) bound its variation
term by K_E K_V sqrt(D)/k. Accepted DE contributes at most
7164 sqrt(D)/k.

Because 0<=X_D,Y_D<=3, the shared-endpoint term is at most

~~~text
3[3/(2k-1)+3(k-2)/(k(2k-3))] <=15/k <=15 sqrt(D)/k.              (4.1)
~~~

The unequal-disjoint-mass endpoint is at most

~~~text
18(k-1)/[k(2k-1)(2k-3)] <=18/k^2 <=6 sqrt(D)/k.                  (4.2)
~~~

Therefore, for both exact observables and 2<=D<=m,

~~~text
|A_D^(2)|, |C_D^(2)| <=K_J sqrt(D)/k,
K_J:=K_E K_V+7185.                                                (4.3)
~~~

Consequently

~~~text
(|A_m^(2)|+|C_m^(2)|)/m
 +sum_(D=2)^(m-1)(|A_D^(2)|+|C_D^(2)|)/D^2
 <=(2K_J/k)[m^(-1/2)+sum_(D=2)^infinity D^(-3/2)]
 <=6K_J/k.                                                        (4.4)
~~~

The scaled channel-two WPCR constant is at most 18K_J.

## 5. Conditional full WPCR

The channel masses in (1.2) are nonnegative, so the ordinary triangle
inequality applies to every full prefix and endpoint. Combining (3.2) and
(4.4) proves:

> **Theorem (conditional full WPCR).** Assume DV with absolute constant
> K_V. Since DE is proved by M248/M249, for every odd k>=3,
>
> ~~~text
> n[(|A_m|+|C_m|)/m
>   +sum_(D=2)^(m-1)(|A_D|+|C_D|)/D^2]
> <=18K_1+9K_2+18(K_E K_V+7185).                              (WPCR*)
> ~~~
>
> Thus M186's full WPCR obligation is proved conditional on DV.

No cancellation between J=1 and J=2 is required. The valid split is
licensed by the stronger channel-one weighted coefficient bounds
(2.3)--(2.5) and (H).

## 6. PCR limitation

The accepted channel-one estimates are weighted l1 bounds. They imply WPCR
through (H), but do not by themselves imply the pointwise PCR scale. The
exact additional channel-one lemma is

~~~text
|sum_(d=2)^D delta_d|
+|sum_(d=2)^D(delta_d+epsilon_d)|
 <=C sqrt(D)/k,                    2<=D<=m.                         (J1-PCR)
~~~

The genuinely convolutional missing unweighted term is

~~~text
B_D^(1):=sum_(d=2)^D epsilon_d
 =sum_(a,b: 2<=n-a-b<=D)delta_a rho_A(b).                          (6.1)
~~~

A weighted bound alone cannot force PCR: abstract coefficients
x_r=1,x_(r+1)=-1 at r comparable to k have weighted l1 norm O(1/k) but a
unit prefix, whereas sqrt(r)/k=O(k^(-1/2)). This is only a logical
non-implication, not a counterexample to the literal rho profiles.

## 7. Scope

- **Proved:** exact mixture, Hardy--Abel transfer, and full WPCR conditional
  on DV, with DE unconditional and accepted.
- **Unresolved:** DV and full PCR, including J1-PCR.
- **Not inferred:** SCBR, BIR, BR, PCS-bound, comparison, spectral gap,
  mixing time, or either Terminal.

