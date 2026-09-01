# Halfway checkpoint: constant-loss two-block recursion above the mixing scale

## 1. Fixed-endpoint Hamiltonians

Use `(pq)(x)=p(q(x))`.  Let `P_N` be uniform on the
`M=binom(N,2)` transpositions, `Q_N=P_N^2`, and `G_N=A_N`.  A length-`l`
microfactorized `Q_N` bridge from `u` to `v` has prefix weight

```text
product_{i=1}^l Q_N(x_{i-1}^{-1}x_i),
x_0=u, x_l=v,
```

and, conditional on every increment `y`, a uniform choice among its
`a_N(y)=M^2Q_N(y)` ordered transposition-pair factorizations.  Let

```text
mathcal H_[0,l]=sum_{j=1}^{l-1}(I-H_j).
```

Define `Lambda_N(l;u,v)` as its best Poincare constant relative to the full
conditional variance, with value zero if the fixed-endpoint chain is
reducible, and put

```text
Lambda_N(l)=min_{u,v:Q_N^l(u,v)>0} Lambda_N(l;u,v).       (1.1)
```

Translation makes the dependence only on `u^{-1}v`, but retaining both
endpoints avoids a convention shortcut.  For the identity bridge,

```text
B=(1/(n-1))sum_j H_j,
gap(B)=Lambda_N(n;e,e)/(n-1).                             (1.2)
```

## 2. Uniform relative smoothing of Q

**Lemma 2.1.**  There is a universal `C_*<infinity` and integers

```text
s_*(N)<=C_* N log(N+1)                                  (2.1)
```

such that, for every `s>=s_*(N)` and all `x,y in A_N`, with
`g_N=|A_N|=N!/2`,

```text
|g_N Q_N^s(x,y)-1|<=1/16.                               (2.2)
```

Here is the parity and character translation.  If `r_lambda` is the
uniform-transposition character ratio of an `S_N` irreducible and

```text
z_lambda=1/N+(N-1)r_lambda/N,
```

then `z_lambda` is the Fourier scalar for the with-replacement lazy
transposition measure used by Diaconis--Shahshahani.  Since
`Q_N^s=P_N^{2s}` and is supported on `A_N`, Fourier inversion gives, for
`g in A_N`,

```text
g_N Q_N^s(e,g)-1
 =(1/2) sum_{lambda notin {(N),(1^N)}}
       d_lambda r_lambda^(2s) chi_lambda(g).             (2.3)
```

Conjugate partitions have equal dimensions, opposite `r_lambda`, and equal
characters on `A_N`; a self-conjugate partition has `r_lambda=0`.  Choose
from every nontrivial pair the member with `r_lambda>=0`.  Since

```text
0<=r_lambda<=z_lambda,
```

the absolute value in (2.3) is bounded by the sub-sum

```text
sum_{chosen lambda} d_lambda^2 z_lambda^(2s)
 <=sum_{lambda !=(N)} d_lambda^2 |z_lambda|^(2s).        (2.4)
```

Diaconis--Shahshahani, Lemma 14, equation (3.1), identifies the last type of
Plancherel sum.  Their Section 3 bounds its partition zones in equations
(3.2), (3.3), (3.5), (3.7), and (3.13), and the collection at the end of the
proof of Theorem 1 bounds that sum by a universal quantity tending to zero
once `s=(N/2)log N+cN` and then `c -> infinity`, uniformly for `N>10`.
Choose one universal `c` making it at most `1/16`.  For `3<=N<=10`, enlarge
the constant in (2.1); there are only finitely many irreducible aperiodic
walks on `A_N`.  Finally, the direct absolute character sum decreases with
`s` because the `Q_N` eigenvalues are `r_lambda^2 in [0,1]`.  This proves
(2.2) for all later times.  The use of the Section 3 Plancherel sum, rather
than only their total-variation conclusion, is essential for the relative
bound.

## 3. Arbitrary endpoint tilts do not destroy the angle

Let `K(x,y)=g_N^{-1}(1+delta_xy)` with `|delta_xy|<=epsilon<1`.  For arbitrary
probability weights `alpha,beta`, form

```text
mu(x,y)=alpha(x)K(x,y)beta(y)/Z.                         (3.1)
```

Writing `d=E_{alpha x beta}delta`,
`d_x=E_beta delta_xy`, and `e_y=E_alpha delta_xy`, direct cancellation gives

```text
dmu/d(mu_X x mu_Y)
 =(1+delta_xy)(1+d)/[(1+d_x)(1+e_y)].                   (3.2)
```

More explicitly, every factor in (3.2) lies in `[1-epsilon,1+epsilon]`, so

```text
(1-epsilon)^2/(1+epsilon)^2
 <=dmu/d(mu_X x mu_Y)
 <=(1+epsilon)^2/(1-epsilon)^2.                         (3.3)
```

Subtracting one on the upper side gives exactly
`4epsilon/(1-epsilon)^2`; the lower-side deviation is
`4epsilon/(1+epsilon)^2` and is smaller.  In particular the safe relaxed
bound requested in audit is

```text
|dmu/d(mu_X x mu_Y)-1|
 <=(4epsilon+2epsilon^2)/(1-epsilon)^2.                 (3.4)
```

For centered unit-variance `f(X),g(Y)`, insert the density minus one in
`E[f(X)g(Y)]` and use Cauchy--Schwarz.  The maximal correlation is at most
the sharper right side preceding (3.4).  At `epsilon=1/16`, the sharp
calculation gives `64/225`, while the relaxed audited value is

```text
rho(X,Y)<=66/225=22/75<1/3.                             (3.5)
```

This bound is uniform over zero entries and arbitrarily concentrated
`alpha,beta`; all ratios are taken only on their marginal supports.

## 4. Two overlapping interval heat baths

Put `b_N=s_*(N)+1`.  Take a fixed-endpoint length-`n` bridge with
`n>=b_N+2`.  Choose `s in {s_*(N),s_*(N)+1}` having the same parity as
`n`, put

```text
t=(n-s)/2>=1,       L=t+s=(n+s)/2<n.                    (4.1)
```

and use intervals `I_1=[0,L]`, `I_2=[t,n]`.  Let `P_1,P_2` be their exact
heat baths, including every microfactor label.  The outside sigma-fields are
respectively the right tail after `L` and the left tail before `t`.

The left tail determines `X_t`; the right tail and pinned final endpoint
determine `X_L`.  Segment factorization, including the independent uniform
microfactorizations, gives the Markov chain

```text
left tail -> X_t -> X_L -> right tail.                  (4.2)
```

Because both boundary variables are functions of their respective tails,
data processing holds with equality: the tail maximal correlation equals
`rho(X_t,X_L)`.  Their joint law is (3.1) with

```text
alpha(x)=Q_N^t(u,x),
K(x,y)=Q_N^s(x,y),
beta(y)=Q_N^t(y,v).                                    (4.3)
```

Thus (2.2)--(3.5) apply for every pinned pair `(u,v)`.

For two conditional-expectation projections, the exact nontrivial top
eigenvalue of `(P_1+P_2)/2` is `(1+rho)/2`; this is the elementary principal-
angle decomposition of two subspaces.  Since `rho<1`, the intersection of
the two tail sigma-fields contains only constants.  Hence the two-block Gibbs
sampler

```text
G_2=(P_1+P_2)/2
```

has

```text
gap(G_2)=(1-rho)/2>=1/3.                                (4.4)
```

Every local term of `mathcal H_n` belongs to at least one interval Hamiltonian
and to at most two.  Fiberwise use of (1.1) therefore gives the quadratic-form
inequalities

```text
mathcal H_n
 >=(1/2)(mathcal H_I1+mathcal H_I2)
 >=(Lambda_N(L)/2)[(I-P_1)+(I-P_2)]
 =Lambda_N(L)(I-G_2).                                  (4.5)
```

Combining (4.4)--(4.5) proves the constant-loss geometric recursion

```text
Lambda_N(n)>=Lambda_N(L)/3,
L-b_N<=(n-b_N)/2.                                      (4.6)
```

No random-scan factor occurs inside (4.6); the single factor `n-1` is paid
only once in (1.2).

## 5. Iteration and exact remaining base

Put `a=log(3)/log(2)`.  Iterating (4.6) until the length is at most
`b_N+1=s_*(N)+2` gives, for `n>=b_N+2`,

```text
Lambda_N(n;e,e)
 >=(1/3)(n-b_N)^(-a)
   min_{2<=l<=b_N+1} Lambda_N(l).                        (5.1)
```

Thus the first unproved proposition is now the finite-scale but still
uniform-in-`N` statement:

> **BASE-SCALE FIXED-ENDPOINT GAP.**  There exist universal `c>0,C<infinity`
> such that for every `N>=3`, every `2<=l<=s_*(N)+2`, and every feasible
> endpoint pair `(u,v)`, the full microfactorized local Hamiltonian satisfies
> `Lambda_N(l;u,v)>=c(Nl)^(-C)`.

This proposition includes qualitative irreducibility of every fixed-product
subbridge.  Identity-bridge irreducibility alone does not imply it.

## 6. Endpoint-conditioned red team: sublinear overlap is insufficient

The constant-angle statement is false if the overlap is `o(N)`.  For
`N>=4`, the standard representation has uniform-transposition ratio

```text
r_std=(N-3)/(N-1),
```

so `Q_N^s` has the nontrivial eigenvalue `q_std^s=r_std^(2s)`.  Take the
identity bridge with equal outside-tail lengths `t_N=N^3` and overlap
`s_N=floor(sqrt(N))`.  The same character estimates make both tail endpoint
weights uniformly `o(N^-2)`-close, in relative error, to uniform.  Testing
the normalized standard matrix coefficient in the boundary maximal-
correlation variational formula then gives

```text
rho_N >= ((N-3)/(N-1))^(2s_N)-o(1) ->1.                (6.1)
```

Consequently `gap(G_2)=(1-rho_N)/2 ->0`.  This is a rigorous obstruction to
a universal constant-loss recursion with sublinear overlap, not a slow mode
for `B` or `K`.  It is fully compatible with the `O(N log N)` positive
buffer above.

## 7. Halfway verdict

The large-overlap recursion is proved, conditional on no unproved mixing
claim beyond the cited random-transposition Plancherel estimate.  The global
bridge gap remains open exactly at the base-scale fixed-endpoint proposition.
A direct fixed-target path comparison at that scale retains factorial target-
size constants, while routing through an identity-heavy canonical bridge has
the already-known exponentially bad hub congestion; neither closes (5.1).
