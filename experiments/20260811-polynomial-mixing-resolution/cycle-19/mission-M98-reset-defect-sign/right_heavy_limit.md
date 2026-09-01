# Right-heavy boundary formula and an infinite negative-defect family

Date: 2026-08-12. This note concerns only the auxiliary nonlazy
minimal-long-cycle parking projection and its canonical reset operator. It is
not a statement about the identity-word heat-bath chain.

## 1. Setup

Put

```text
w_a=a^(a-1)/a!,
c(n,p)=[z^n]T(z)^p=p n^(n-p-1)/(n-p)!,
rho_s(k,t)=w_t c(s-t,k-1)/[k!w_(s+1)],
q_(s,B)=w_(s+1-B)w_B/w_(s+1).
```

Here `T=z exp(T)`, `c(0,0)=1`, and impossible `c(n,p)` is zero. For a
right-heavy context

```text
x_K=(s,K,K-1,B),
```

M90's transformed local budget and defect are

```text
U(x_K)=q_(s,B)(1-q_(s,B)),
r_U(x_K)=U(x_K)-A(x_K)-Q U(x_K),                   (1.1)
```

where `A=sum_e (theta_e^2/Q_G(e))(1-q_(y_e))` and `Q` retains every
attachment rank `j=1,...,k`.

## 2. Right-heavy limit

The right-heavy attachment law is

```text
nu_(K,K-1,k)(j)=binom(K-1+j,j)/binom(K+k,k).       (2.1)
```

Thus `nu(k)->1` and `nu(j)->0` for every `j<k`. The exact contextual mean
also has the limit

```text
H_infty(k,t)=0,                        t<B,
              1,                        t=B and k=1,
              0,                        t=B and k>=2,
              q_(t-1,B),                t>B.       (2.2)
```

For the deep child selected by `j=k`, the positional multiplier
`(K+k)/(K+j)` is one. Hence

```text
lim_(K->infty) Q U(x_K)
 =sum_(k,t>B)rho_s(k,t)q_(t-1,B)(1-q_(t-1,B)).     (2.3)
```

Stationary averaging of (2.2), equivalently the finite closed-mean identity
followed by finite convergence, gives `E_rho H_infty=q_(s,B)`. For each
deep group, `q_child(1-q_child)=H_infty-H_infty^2`; on killed and terminal
groups the same difference is zero. Therefore

```text
U_infty-Q_infty U=Var_rho(H_infty).                (2.4)
```

No Bernoulli event is used: (2.4) is an algebraic finite-sum identity.

## 3. Last-part reset-energy coefficients

For `A>=1, ell>=1`, define

```text
L_(A,ell)=sum_(p=1)^A c(A,p)/(p+ell)!.             (3.1)
```

The beta integral

```text
1/(p+ell)!
 =1/[p!(ell-1)!] integral_0^1 u^p(1-u)^(ell-1)du
```

and Lagrange inversion

```text
[z^A]exp(uT(z))=u(u+A)^(A-1)/A!
```

give the positive closed form

```text
L_(A,ell)
 =1/(ell-1)! integral_0^1 (1-u)^(ell-1)
    u(u+A)^(A-1)/A! du.                            (3.2)
```

Let `m_(s,t)=sum_k rho_s(k,t)`. Explicitly,

```text
m_(s,t)=w_t a_(s-t)/w_(s+1),
a_0=1,
a_n=n w_n/(n+1),                    n>=1.          (3.3)
```

Define `e_(s,t)` by the following finite positive sum. The two-part term is

```text
1_(1<=t<s) w_t L_(s-t,1)^2/[w_(s-t)w_(s+1)]
  *[1-w_(s-t)w_t/w_s].                            (3.4)
```

For every `ell>=2`, sum over `A,b>=1` and `u>=0` satisfying
`A+b+u+t=s`, retaining only `c(u,ell-2)>0`, the term

```text
w_b w_t c(u,ell-2) ell! L_(A,ell)^2/[w_Aw_(s+1)]
  *[1-w_Aw_b/w_(A+b)].                             (3.5)
```

Then `e_(s,t)` is (3.4) plus all terms (3.5). To prove this, take a
canonical endpoint `(A,b,c_3,...,c_(ell+1))` with last part `t`. Every
source in its basin refines `A` into `p` parts and has the same limiting
mean (2.2), so

```text
theta_infty
 =[product_(i>=2)w_(c_i)/w_(s+1)]
   L_(A,ell)[H_infty(t)-q].                        (3.6)
```

The normalized endpoint capacity is

```text
Q_G=w_A product_(i>=2)w_(c_i)/[ell!w_(s+1)].       (3.7)
```

Dividing (3.6)^2 by (3.7), multiplying by the reset reward
`1-w_Aw_b/w_(A+b)`, and summing the middle parts by `c(u,ell-2)` proves

```text
A_infty=sum_(t=1)^s e_(s,t)[H_infty(t)-q]^2.       (3.8)
```

Combining (2.4) and (3.8) gives the exact signed decomposition

```text
r_infty(s,B)
 =sum_(t=1)^s [m_(s,t)-e_(s,t)]
    [H_infty(t)-q_(s,B)]^2.                        (3.9)
```

## 4. Exact negative family

At `(s,B)=(16,4)`, exact evaluation of (3.9) gives

```text
r_infty(16,4)
=-9227444489897033899069928546555383705889289522405715688049247702588321735512746884149350887011428507035652533537
 /206939781608101554317882579170416040081179045783441942415142310077467888193085115142449958815210345070592000000000000
<0.                                                    (4.1)
```

The negative last-part coefficients are `t=3,...,8`; their total weighted
contribution is about `-2.49600456e-4`, while the positive fibres contribute
about `2.05010458e-4`. This is the mechanism behind (4.1), not numerical
cancellation in one unevaluated expression.

There is also an explicit integer tail proof. Put

```text
P(K)=r_U(16,K,K-1,4) product_(i=1)^16(K+i)^2.      (4.2)
```

From (2.1), the closed contextual formula, and the squared basin currents,
the positive product in (4.2) clears every `K`-dependent denominator and
`P` is a rational-coefficient polynomial of degree at most `32`. Exact
forward differences satisfy

```text
Delta^d P(710)<0,          0<=d<=32,
Delta^33 P(710)=0.                                  (4.3)
```

All 34 exact values are frozen in `defect_counterexample.json`. Newton's
formula now gives, for every integer `n>=0`,

```text
P(710+n)=sum_(d=0)^32 Delta^dP(710)binom(n,d)<0.    (4.4)
```

Since the clearing factor is positive, (4.4) proves

```text
r_U(16,K,K-1,4)<0             for every K>=710.    (4.5)
```

The first displayed finite witness is therefore

```text
x=(16,710,709,4),
r_U(x)
=-661615179812287703733401538288146672176656056694303980320445480238015535840763927227096436539021950529551118381660089830702424942161641416917615391141563
 /15460100025816349488410112953706549354494952698029896882055642399736857012069212448884171351353755919509119530816720904828324088359963688078474739712000000000000
<0.                                                    (4.6)
```

It is reachable: from the fresh context `(K+15,1,0,4)`, take the positive
root composition `(1^(K-2),17)` with part count `K-1` and attachment rank
`j=K-1`. The resulting deep child is `(16,K,K-1,4)`.

## 5. Exact scope

Equation (4.5) refutes only the local nonfresh sign used in M90's proposed
boundary-layer proof. It does not refute the full weighted resolvent, the
stronger unweighted resolvent, a `Pbar` gap, or the original heat-bath mixing
conjecture. At the finite witness (4.6), the complete weighted and unweighted
resolvent ratios are still exactly below one. Any surviving proof must allow
compensation across multiple nonfresh depths.
