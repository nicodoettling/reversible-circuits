# M219 independent proof audit of frozen M216

Date: 2026-08-13 UTC.

## 1. Verdict and strict scope

```text
FINAL VERDICT: ACCEPT.
MATERIAL OBJECTIONS: NONE.
```

M216 proves an exact obstruction only to the degree-cap diagonal Bernstein
PSD-envelope ansatz. This audit makes no claim about an all-degree Bernstein
dictionary, arbitrary nondiagonal Bernstein/Jacobi/Green kernels, fresh
contraction, total AMV, a spectral gap, mixing, or Terminal A/B.

## 2. Immutable source gate

The frozen M216 directory contains exactly the nine payloads declared in its
manifest plus `SHA256SUMS`; there are no hidden or extra files. The
independently computed checksum-ledger digest is

```text
2c25bb31839bf8ff64181b9e4437fe70f5530bf5e7d0aa4eca8de4c21388d414.
```

Every ledger entry passes. Only then were the conclusions and checker read.
A replay into `/tmp`, leaving M216 unchanged, reproduced the frozen result
digest
`cb653878ab44462a8fb636a5808acaffae41c48e3b9710af28f53eff449eedb3`.

## 3. Bernstein cone and exact closure audit

For `b_(n,j)(u)=C(n,j)u^j(1-u)^(n-j)`, M216 fixes

```text
B_L^diag={sum_(j=0)^L c_j b_(L,j) tensor b_(L,j): c_j>=0}.
```

Direct polynomial multiplication gives

```text
b_(d,a)b_(ell,j)
 =[C(d,a)C(ell,j)/C(d+ell,a+j)] b_(d+ell,a+j).       (3.1)
```

Thus a diagonal atom remains exactly diagonal when `d+ell=L`. If
`n=d+ell<L`, exact degree elevation is

```text
b_(n,k)=sum_r e_r b_(L,r),
e_r=C(n,k)C(L-n,r-k)/C(L,r)>=0.                       (3.2)
```

The raw lifted outer product is generally `ee^T`, hence nondiagonal. Put
`s=sum_r e_r`. The claimed envelope follows from the exact identity

```text
s diag(e)-ee^T
 =sum_(i<j)e_i e_j (unit_i-unit_j)(unit_i-unit_j)^T >=_PSD 0.  (3.3)
```

The independent checker verifies all 182 products relevant through cap six,
including 77 saturated cases, and all 28 elevations. All 105 unsaturated
product cases have more than one positive elevated coordinate. For example,

```text
b_(5,2)=(2/3)b_(6,2)+(1/2)b_(6,3),
```

so the raw outer product has the nonzero off-diagonal coefficient `1/3`.
Equations (3.2)--(3.3) verify that M216 does not silently assert raw diagonal
closure and that its named repair is positive-linear and PSD-order valid.

## 4. Exact recursion and boundary handling

The accepted full-Gram recursion can also be derived directly from the Bayes
feature coordinate. If a retained observation `a<d` has likelihood
`L_a=b_(d,a)`, marginal `pi_a=E L_a`, exterior branch mass `eta`, and child
feature `Phi_a`, its parent feature is

```text
sqrt(eta/pi_a) L_a Phi_a.
```

Therefore its Gram contribution has exactly one normalization factor:

```text
(eta/pi_a)L_a(u)L_a(v)K_a(u,v).                     (4.1)
```

For a root ordered composition `lambda` of `s`, with `d=|lambda|` and last
part `t`, the clean-room reconstruction uses

```text
rho(lambda)=prod_i w(lambda_i)/(d! w(s+1)),
eta=rho(lambda)q_(t-1,B)/q_(s,B),
pi_a=C(d,a)(D)_a(kappa-D)_(d-a)/(kappa)_d,
child=(t-1,kappa+d,D+a,B).
```

It enumerates literal ordered compositions rather than M216's grouped Cayley
roots. The reset kernel is reconstructed independently from exact basin
currents. Every beta-binomial law sums to one, and only `a=0,...,d-1` is
lifted; `a=d` is counted once per live root and omitted.

Across the 32 reachable recursive states, the checker sees 51 live root rows,
108 retained observations, and exactly 51 killed `a=d` omissions. The final
kernel has 49 nonzero monomial coefficients. Without reading predecessor data,
the checker obtains

```text
kernel SHA256      d2ee4261fd89e712d0649d9cea3c30952256bff82c99134a59fce7b151505152
coefficient SHA256 d1dd37fe74b894523b4b049099d194ed34fb64fb36d144b48ff3746a34e1ccae
```

which exactly match M216 after the independent result had been generated.
This verifies the reset, exterior `eta`, single `1/pi_a`, child update, and
killed-boundary convention for the named row.

## 5. Necessary coefficient inequality

Let `b(u)` be the degree-six Bernstein feature vector and write the actual
kernel `K(u,v)=b(u)^T A b(v)`. The clean-room conversion uses exact Gaussian
inversion rather than M216's monomial-to-Bernstein formula. Its Bernstein
basis matrix has determinant `162000`. More directly, the evaluation matrix
at `u=0,1/6,...,1` has determinant `3125/17006112`, hence is invertible.

For any symmetric coefficient matrix `M`, the kernel
`b(u)^T M b(v)` is PSD iff `M` is PSD: one direction factors a PSD matrix;
for the converse, evaluate at the seven points above and conjugate their PSD
Gram matrix by the inverse evaluation matrix. Consequently every
`J_c in B_6^diag` satisfying `J_c>=_PSD K` necessarily obeys

```text
diag(c)-A >=_PSD 0.                                  (5.1)
```

Put `w_j=Q[b_(6,j) tensor b_(6,j)]`. Then
`Q[J_c]=sum_j w_j c_j`. If `X>=_PSD0` and `diag(X)=w`, taking the trace of
the product of the two PSD matrices in (5.1) gives

```text
Q[J_c] >= Tr(A X).                                   (5.2)
```

This is a necessary lower bound for every final degree-cap diagonal
majorant, independently of how reset and lift envelopes were selected.

## 6. Exact rational certificate

At `(B,L,kappa,D)=(1,6,2,1)`, the independent calculation gives

```text
q=(7/8)^6=117649/262144,
1-q=144495/262144,
w=(433/10192, 747/28028, 3491/112112, 100/3003,
   3491/112112, 747/28028, 433/10192).
```

With M216's declared signs and radii, define `v_j=sign_j r_j` and
`X=vv^T+diag(w-r^2)`. The independently reconstructed remainders are

```text
(633/254800, 18427/17517500, 39213/17517500,
 6757/7507500, 39213/17517500, 18427/17517500,
 633/254800),
```

all strictly positive. Hence `X` is PSD and `diag(X)=w` exactly. Exact matrix
contraction gives

```text
Tr(A X)
=27574523089250503170656957870808157889213
 /48209994003606915089647408250880000000000,

Tr(A X)-(1-q)
=1000948704365931347999936328408157889213
 /48209994003606915089647408250880000000000 > 0.
```

By (5.2), no degree-six diagonal Bernstein kernel can both PSD-dominate the
actual kernel and fit the fresh budget. M216's named-ansatz obstruction is
therefore exact.

## 7. Actual contraction slack and limitation

The actual kernel itself has

```text
T_1
=100831060869578347854833692341308821
 /459142800034351572282356269056000000,

(1-q)-T_1
=152250599938846145694280798538691179
 /459142800034351572282356269056000000 > 0.
```

Thus the rational row is not a contraction counterexample. It measures the
cost of forcing the actual full kernel into `B_6^diag`. It says nothing about
the larger all-degree dictionary or a nondiagonal structured majorant.

## 8. Numbered objections

1. **Material objections:** none.
2. **Algebra or normalization objections:** none. Saturated and unsaturated
   closure, the `eta/pi_a` factor, reset, and killed `a=d` treatment all pass.
3. **Certificate objections:** none. The dual feasibility, exact objective,
   positive excess, actual charge, and positive actual slack all reproduce.
4. **Scope objections:** none. M216 explicitly limits the result to the named
   degree-cap diagonal cone and leaves contraction and broader kernel families
   unresolved.

