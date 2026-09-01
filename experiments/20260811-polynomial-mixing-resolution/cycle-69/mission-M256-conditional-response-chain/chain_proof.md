# M256 exact conditional response-chain theorem

Date: 2026-08-14 UTC.

Status: the theorem through `(PCS-bound)` is **proved conditional on full
`(DV)`**. The implication to `FCL1` is **conditional on the additional,
independent `(FD-bound)`**. No gap or mixing statement follows.

## 1. Setting, target, and notation firewall

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right. Fix odd `k>=3` and put

```text
n=3k,                 m=(n-1)/2=floor(n/2).
```

The target in this calculation is the uniform law on minimal length-`n-1`
transposition factorizations of the ambient long cycle, under M73's nonlazy
cyclic rank-two coordinate kernel. It is not the global uniform identity-word
law and not the lazy exact same-product `{3,4,5}` heat-bath chain.

The letter `N` in M168's generic sequence inequality denotes only the number
of phase entries. In its application,

```text
N_phase=n-3=3k-3.
```

It is unrelated to the ambient symmetric-group parameter `N` in
`Omega(N,m)` and will not be reused below. Likewise, the local symbol `m`
in this proof is the component-size cutoff endpoint, not the circuit word
length denoted `m` in the project-level heat-bath problem.

Assume full M192 disjoint split variation: there is an absolute `K_V` such
that for `Z=X_D,Y_D`, every `2<=D<=m` satisfies

```text
sum_(u=1)^(k-2) sqrt(u)
 |Phi_(u+1)^D(Z)-Phi_u^D(Z)| <=K_V sqrt(D).          (DV)
```

M248/M249's signed deletion/embedding response `(DE)` is unconditional and
accepted, with common constant `7164` for the same observables and domain.

## 2. Full DV implies full WPCR

Let `M_r^(j)(d)` be the conditional component coefficient in channel
`J=j`. Put

```text
P_d^(j)=M_1^(j)(d),              N_d^(j)=M_1^(j)(d)+M_2^(j)(d),
C_D^(j)=sum_(d=2)^D P_d^(j),    A_D^(j)=sum_(d=2)^D N_d^(j).
```

The exact common denominator and channel masses are

```text
den=(3k-3)(3k-4),
alpha_0=(k-1)(k-2)/den,
alpha_1=2(k-1)(2k-2)/den,
alpha_2=(2k-2)(2k-3)/den.
```

They are nonnegative and sum to one. The `J=0` laws agree at both sources
and cancel, so coefficientwise and prefixwise

```text
C_D=alpha_1 C_D^(1)+alpha_2 C_D^(2),
A_D=alpha_1 A_D^(1)+alpha_2 A_D^(2).                (2.1)
```

There is no missing conditional normalization in channel two:

```text
C_D^(2)=E_B[Y_D|J=2]-E_A[Y_D|J=2],
A_D^(2)=E_B[X_D|J=2]-E_A[X_D|J=2].                 (2.2)
```

M192/M195's shared-endpoint mass, nonzero unequal-disjoint-mass endpoint,
scalar cumulative bound, assumed DV, and accepted DE give

```text
|A_D^(2)|, |C_D^(2)| <=K_J sqrt(D)/k,
K_J=K_E K_V+7185.                                  (2.3)
```

Here `7185=7164+15+6`: DE, shared endpoints, and the retained Abel endpoint.
Thus no endpoint has been absorbed by renormalizing the disjoint submeasure.

For channel one, write

```text
delta_d=rho_B(d)-rho_A(d),
epsilon_d=sum_(a+b=n-d)delta_a rho_A(b).
```

M186/M189 proves

```text
sum_d |delta_d|/d <=K_1/k,
sum_d |epsilon_d|/d <=K_2/k.                       (2.4)
```

The second inequality is the fixed-`d` triangle consequence of their exact
two-run weighted estimate; every residual size has `d=n-a-b>=2`.

For any finite `x_2,...,x_m`, with `X_D=sum_(d=2)^D x_d`, the exact Hardy--
Abel transfer is

```text
|X_m|/m+sum_(D=2)^(m-1)|X_D|/D^2
 <=3 sum_(d=2)^m |x_d|/d.                          (2.5)
```

Applying (2.5) to `delta`, `delta+epsilon`, and then (2.3), followed by the
nonnegative mixture (2.1), gives exactly M252/M253's conditional theorem:

```text
n[(|A_m|+|C_m|)/m
  +sum_(D=2)^(m-1)(|A_D|+|C_D|)/D^2]
 <=C_W,                                             (WPCR*)

C_W=18K_1+9K_2+18(K_E K_V+7185).                  (2.6)
```

The factor `n=3k` is responsible for the coefficients `18,9,18`; no
`n/k` conversion remains hidden.

## 3. WPCR implies SCBR, including the singleton and endpoint

Use M186's full coefficients

```text
P_d=M_1(d),                 N_d=M_1(d)+M_2(d),
C_D=sum_(d=2)^D P_d,        A_D=sum_(d=2)^D N_d,
r_d=u_1(d)-u_2(d).
```

Because `n` is odd, `m=(n-1)/2` is exactly the largest integer `d<=n/2`.
M186/M189's small-component charge is

```text
S_k=M_1(1)u_1(1)+sum_(d=2)^m[N_d u_2(d)+P_d r_d].  (3.1)
```

Finite Abel summation, with both endpoints retained, gives

```text
S_k=M_1(1)u_1(1)+A_m u_2(m)+C_m r_m
 +sum_(d=2)^(m-1){
    A_d[u_2(d)-u_2(d+1)]
   +C_d[r_d-r_(d+1)]}.                             (3.2)
```

The accepted estimates are

```text
M_1(1)=O(1/n),
|u_2(d)|+|r_d|=O(1/d),
|u_2(d)-u_2(d+1)|+|r_d-r_(d+1)|=O(1/d^2).          (3.3)
```

The zero-shift convention makes `u_1(1)` one fixed finite constant. Taking
absolute values in (3.2) only after the full signed prefixes have been
formed, then substituting `(WPCR*)`, gives

```text
|S_k|=O(1/n).                                      (SCBR)          (3.4)
```

This is the exact point at which the weighted route succeeds. Full `(PCR)`
and its unresolved `J1-PCR` strengthening are unnecessary. Omitting either
`M_1(1)` or the endpoint term `(|A_m|+|C_m|)/m` would leave this implication
unlicensed; both are present and controlled.

## 4. SCBR implies BR and BIR

M180/M182 proves the complementary large-component tail

```text
sum_(d>n/2)|M_1(d)u_1(d)+M_2(d)u_2(d)|=O(1/n).     (4.1)
```

Together with (3.4), this gives `eta(Q)=O(1/n)` and hence
`n eta(Q)=O(1)`. Its exact boundary-response decomposition is

```text
B_k(s)=2nQ(s)-7/2-2I_D(s)+R(s),
sup_(n,s)|R(s)|<infinity.                          (4.2)
```

Since the signed source measure has `eta(1)=0`, total variation at most two,
and `0<=I_D<=2`, (4.2) proves

```text
n eta(Q)=O(1)  iff  eta(B_k)=O(1).                 (BR)             (4.3)
```

Thus the affine constant, collision indicator, and response remainder are
all retained and bounded; none is silently deleted.

For M180's bounded boundary-incidence observable `0<=W<=2`, put
`H=sum_i U_i`. The exact identities are

```text
eta(Q)=e eta(H)-t_k,
eta(H)=(n-3)/2[(bar K^2W)(O_B)-(bar K^2W)(O_A)],
t_k=12(k-1)/[3k(3k-4)(2k-1)]=O(n^-2).             (4.4)
```

Equations (4.3)--(4.4) give the equivalent boundary-incidence statement

```text
|(bar K^2W)(O_B)-(bar K^2W)(O_A)|=O(n^-2).         (BIR)            (4.5)
```

## 5. BR implies PCS-bound

M174/M178's exact affine response is

```text
Delta_k(C_k)=e^-2/R_n[2n eta(T)+eta(B_k)],
R_n=(n-3)(n-4),
eta(T)=12(k-1)/[3k(3k-4)(2k-1)].                  (5.1)
```

The first term is already bounded: `2n eta(T)=O(1)`, and `R_n` is uniformly
comparable with `n^2` (`R_n/n^2>=10/27` at and above `n=9`). Therefore BR
gives

```text
Delta_k(C_k)=O(n^-2).                              (5.2)
```

The exact target mass and signed phase normalization are

```text
pi_y=2/(n-2)(1-2/n)^(n-3),
sum_(y=1)^(n-3) z_k(y)=2Delta_k(C_k)/pi_y.          (5.3)
```

The exponential factor in (5.3) is uniformly bounded above and below away
from zero, while `n=3k`. Hence (5.2) is equivalent to

```text
k |sum_(y=1)^(n-3)z_k(y)|=O(1).                    (PCS-bound)      (5.4)
```

This proves the strongest conclusion downstream of the full-DV hypothesis
without adding another hypothesis.

## 6. Exact stop: FD remains independent

Put `Z_k(y)=kz_k(y)`. M168/M171's deterministic inequality, applied to the
`n-3` phase entries, is

```text
sum_y|Z_k(y)|
 <=k|sum_y z_k(y)|
   +(n-3)k sum_(y=1)^(n-4)|z_k(y+1)-z_k(y)|.       (6.1)
```

Conditional full DV proves that the first term is `O(1)` by (5.4). It says
nothing about the second term. The separately named hypothesis

```text
k^2 sum_(y=1)^(n-4)|z_k(y+1)-z_k(y)|=O(1)          (FD-bound)       (6.2)
```

would control it because `(n-3)/k=3-3/k<=3`. Thus

```text
full DV + FD-bound  =>  sum_y|Z_k(y)|=O(1)          (FCL1).          (6.3)
```

Without `(FD-bound)`, or M168's alternative minority-sign estimate
`k min(P_k,N_k)=O(1)`, the implication stops at `(PCS-bound)`. A signed sum
does not control an absolute sum.

M161/M166's accepted exact normalization is

```text
A_k(1,1)=k/(n-3) sum_y|Z_k(y)|,                    (6.4)
```

where this `A_k(1,1)` is the first fixed-cell scalar, not the source
permutation also denoted `A_k`. Since

```text
1/3 <= k/(n-3) <=1/2,
```

`FCL1` and `A_k(1,1)=O(1)` are equivalent. Consequently FD remains a
separate obligation for both.

## 7. Strongest theorem and first remaining lemmas

> **Conditional response-chain theorem.** Uniformly for odd `k>=3`, full
> `(DV)` plus the already proved `(DE)` implies full `(WPCR)`, `(SCBR)`,
> `(BR)`, `(BIR)`, `Delta_k(C_k)=O(n^-2)`, and `(PCS-bound)`. If
> `(FD-bound)` is added, then `FCL1` and `A_k(1,1)=O(1)` follow.

The first independent unresolved obligations are:

1. the remaining full-DV clause—equivalently `(TAV)` once the proved
   `Y-DV` theorem is accepted—which controls the complementary two-run
   profile; and
2. `(FD-bound)`, or the exact minority-sign substitute, to pass from PCS to
   absolute fixed-cell L1.

Even both would prove only the first auxiliary fixed cell. Other cells,
direct L1, the all-edge bound, H0, every spectral-gap comparison, polynomial
mixing of the identity heat-bath chain, and both Terminals remain open.
