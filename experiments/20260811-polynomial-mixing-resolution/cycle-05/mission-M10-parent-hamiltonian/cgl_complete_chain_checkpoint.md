# Coordinator checkpoint: exact leave-one-coordinate recursion

Status: proved structural reduction; nonterminal.

## 1. Model and convention

Permutations compose as `(pq)(x)=p(q(x))`, and tuple products are read from
left to right.  Put

```text
G=A_N,  E=T_N^2,  q=|E|=M^2,  M=binom(N,2),
p(a,b)=ab,
Q(g)=q^(-1)|{e in E:p(e)=g}|.
```

For `l>=2` and a feasible endpoint `h in G`, let `Omega_l(h)` be the set of
`E`-words `X=(X_1,...,X_l)` with
`p(X_1)...p(X_l)=h`, equipped with its uniform law `pi_(l,h)`.  For
`1<=i<j<=l`, `P_ij` is exact conditional expectation given every coordinate
outside `{i,j}`.  Define the positive semidefinite complete-pair heat-bath
operator

```text
C_(l,h)=binom(l,2)^(-1) sum_(i<j) P_ij.                (1.1)
```

For each `k`, let `R_k=E[ . | X_k]` and

```text
A_(l,h)=l^(-1) sum_k R_k.                              (1.2)
```

All gaps below are Poincare gaps of the displayed discrete-time Markov
operator; singleton fibers have gap one.

## 2. Exact braid-deletion lemma

Fix `k`, a microstate `e in E`, and put `g=p(e)`.  Conditional on `X_k=e`,
delete coordinate `k` and transform every later microstate by simultaneous
conjugation with `g`:

```text
Y_i=X_i                         (i<k),
Y_(i-1)=g X_i g^(-1)            (i>k),                (2.1)
```

where `g(a,b)g^(-1)` means
`(gag^(-1),gbg^(-1))`.  This is a bijection from the conditional fiber onto
`Omega_(l-1)(h g^(-1))`, because, writing the original product as
`P g S=h`,

```text
product(Y)=P(g S g^(-1))=h g^(-1).                    (2.2)
```

It preserves counting measure.  Moreover, for every `i<j` avoiding `k`, it
maps the conditional fiber of `(X_i,X_j)` at fixed complement bijectively to
the corresponding raw two-coordinate conditional fiber after deletion.
Thus it intertwines `P_ij` with the natural pair heat bath on the shorter
bridge.  This includes the case `i<k<j`; no crossing-pair commutation is
being asserted.

For `l>=3`, set

```text
C_l^(k)=binom(l-1,2)^(-1)
          sum_(i<j; i,j != k) P_ij.                   (2.3)
```

Every pair occurs in exactly `l-2` of these sums, hence

```text
C_(l,h)=l^(-1) sum_k C_l^(k).                          (2.4)
```

Let

```text
gamma_l^*=min_(feasible h) gap(C_(l,h)),
mu_l(h)=sup_{f perpendicular 1}
          <f,A_(l,h)f>/||f||_2^2.                     (2.5)
```

Applying the shorter-fiber Poincare inequality conditionally on `X_k` gives

```text
<f,(I-C_l^(k))f>
 >=gamma_(l-1)^* (||f||_2^2-||R_k f||_2^2).           (2.6)
```

Averaging (2.6), using (2.4), and taking mean-zero `f` proves the exact
recursion

```text
gap(C_(l,h))>=gamma_(l-1)^* [1-mu_l(h)],
gamma_l^*>=gamma_(l-1)^* [1-mu_l^*],                  (2.7)
mu_l^*=max_(feasible h) mu_l(h).                       (2.8)
```

The base is `gamma_2^*=1`, because `C_2=P_12` is the whole-fiber heat bath.

This is the ordered-bridge analogue of the leave-one-particle mechanism in
Carlen--Geronimo--Loss, arXiv:0705.3729, Lemma 3.1, but (2.1)--(2.8) are
self-contained and do not import exchangeability from that paper.

## 3. Exact coordinate-correlation block reduction

The centrality of `Q=P_T^2` removes all dependence of one- and ordered
two-coordinate marginals on their locations.  If `x=p(e)` and `y=p(f)`, then
for every `i<j`,

```text
pi_(l,h)(X_i=e)
 =q^(-1) Q^(l-1)(h x^(-1))/Q^l(h),                   (3.1)

pi_(l,h)(X_i=e,X_j=f)
 =q^(-2) Q^(l-2)(h y^(-1)x^(-1))/Q^l(h).             (3.2)
```

Indeed, in the group algebra the three intervening convolution powers of
the central measure `Q` commute with `delta_x` and `delta_y`, leaving
`Q^(l-2) delta_x delta_y`.  Formula (3.2) is ordered and need not be symmetric
under exchanging `e,f` when `h` is noncentral.

Let `H=L^2(E,mu_(l,h))` for the common marginal (3.1), let
`H_0` be its mean-zero subspace, and define the forward correlation operator

```text
<u,K_(l,h)v>_H=E[u(X_i)v(X_j)]   for any i<j.          (3.3)
```

For `J_k:H->L^2(pi)` given by `J_k u=u(X_k)`, put
`J(u_1,...,u_l)=l^(-1/2)sum_k J_k u_k`.  Then

```text
A_(l,h)=J J^*.                                        (3.4)
```

Consequently its nonzero spectrum equals that of the block Gram operator
`J^*J`.  After removing the constant eigenvalue and the constant-coordinate
kernel, `mu_l(h)` is exactly the largest eigenvalue on `H_0^l` of

```text
G_(l,h)=l^(-1)
 [ I    K    K   ... K
   K*   I    K   ... K
   K*   K*   I   ... K
   ...                  ].                            (3.5)
```

The kernel in (3.3) depends on a microstate only through its product in
`supp(Q)`, which consists of the identity, 3-cycles, and double
transpositions.  Every one-coordinate function whose average on each product
fiber is zero lies in the kernel of both `K` and `K*`.  Hence all nonzero
off-diagonal correlation is carried by a space of dimension at most

```text
|supp(Q)|=1+2 binom(N,3)+3 binom(N,4)=O(N^4),          (3.6)
```

rather than by the factorial group algebra or the full `M^2` micro alphabet.

### 3.1 Cyclic covariance makes the forward operator normal

There is a further exact structure which is absent from a generic ordered
law.  Define the marginal-preserving conjugation

```text
theta_h(e)=h^(-1)e h,       (U_h f)(e)=f(theta_h(e)).  (3.7)
```

The uniform bridge is invariant under the cyclic braid

```text
(X_1,...,X_l)
 ->(X_2,...,X_l,theta_h(X_1)),                         (3.8)
```

because, if `p(X_1)S=h`, then
`S h^(-1)p(X_1)h=h`.  Since every ordered pair of locations has the same law
by (3.2), (3.8) implies

```text
(X_i,X_j) law = (X_j,theta_h(X_i)) law,   i<j.         (3.9)
```

For the complex `L^2` inner product, (3.9) gives

```text
<f,Kg>=<Kf,U_h g>,
K=K* U_h,
K*=U_h^(-1)K.                                         (3.10)
```

Substituting the second identity in the first shows that `K` commutes with
`U_h`; hence `KK*=K*K`.  Thus `K` is normal even though it is generally not
self-adjoint.  This corrects the preliminary self-attack that treated `K` as
an arbitrary nonnormal correlation operator.

Because `K` and `U_h` are commuting normal operators, they have a common
orthonormal eigenbasis.  If

```text
Kv=kappa v,  U_h v=zeta v,  kappa!=0,
```

then (3.10) forces `zeta=kappa/conj(kappa)`.  On the corresponding copy of
`C^l`, the unnormalized block in (3.5) is the scalar Hermitian matrix

```text
T_l(kappa)_(ii)=1,
T_l(kappa)_(ij)=kappa       (i<j),
T_l(kappa)_(ij)=conj(kappa) (i>j).                     (3.11)
```

This matrix also has an exact elementary spectrum.  If `kappa` is real, its
eigenvalues are

```text
1+(l-1)kappa                    once,
1-kappa                         multiplicity l-1.      (3.12)
```

If `kappa` is nonreal, its `l` eigenvalues are

```text
1+(z kappa-conj(kappa))/(1-z),
        z^l=conj(kappa)/kappa.                         (3.13)
```

They are real; (3.13) follows by writing the eigenvector equation in terms
of prefix sums.  The eigenvalues of `G_(l,h)` are (3.12)--(3.13) divided by
`l`, together with `1/l` from `ker K`.  Consequently the unresolved norm
`mu_l(h)` is exactly the maximum of these scalar quantities over the
mean-zero spectrum of the `O(N^4)`-dimensional product correlation kernel.

### 3.2 Pointwise smoothing controls the dense correlation tail

The parity-aware Diaconis--Shahshahani estimate already audited in the
cycle-03 M10 and cycle-04 M07 reports has the following strengthened
consequence.  There is a universal `C_mix<infinity` such that, whenever

```text
l>=C_mix N log(N+1),
s in {l-2,l-1,l},
```

the pair walk on `A_N` satisfies

```text
epsilon_s:=max_(g in A_N) ||A_N|Q^s(g)-1|
             <=1/(64l).                              (3.14)
```

Here `Q=P_T^2`.  To check the strengthening from a fixed error to the
`1/l` error in (3.14), pair conjugate representations in the Fourier
expansion as in the cited audits.  At the identity the absolute nontrivial
sum is nonnegative; at any other group element its absolute value is no
larger because `|chi_lambda(g)|<=d_lambda`.  At the first even time beyond
`A N log(N+1)` that sum is at most `1/16`.  Every remaining nonsign
eigenvalue of the transposition walk has modulus at most
`1-2/(N-1)`.  The resulting exponential tail dominates `1/(64l)` uniformly
for all three displayed powers after enlarging one universal `C_mix`.
The finitely many cases `3<=N<=10` are absorbed exactly as in the audited
pointwise argument; `N=3` causes no exceptional support issue.

Let `nu` be the joint law of `(X_i,X_j)`, `i<j`, and let `mu` be the common
one-coordinate marginal.  Dividing (3.2) by the product of two copies of
(3.1) gives, with four pointwise errors of modulus at most
`epsilon:=1/(64l)`,

```text
((1-epsilon)/(1+epsilon))^2
 <=dnu/d(mu tensor mu)
 <=((1+epsilon)/(1-epsilon))^2.                       (3.15)
```

Consequently

```text
||dnu/d(mu tensor mu)-1||_infinity
 <=4epsilon/(1-epsilon)^2
 <=16epsilon=1/(4l).                                 (3.16)
```

For centered `u,v in H_0`, subtract the product law in their covariance and
apply Cauchy--Schwarz.  Equations (3.3) and (3.16) therefore give the
uniform arbitrary-endpoint operator estimate

```text
||K_(l,h)||_(H_0 to H_0)<=1/(4l).                    (3.17)
```

Finally, for `u=(u_1,...,u_l) in H_0^l`, use (3.5), (3.17), and
`2 sum_(i<j)||u_i||||u_j||<=(l-1)sum_i||u_i||^2` to get

```text
<u,G_(l,h)u>
 <=[1+(l-1)/(4l)]/l ||u||^2.
```

Thus the dense scalar tail is proved:

```text
mu_l(h)<5/(4l)                                       (3.18)
```

for every feasible endpoint and every
`l>=C_mix N log(N+1)`.  In particular, if the recursion (2.7) starts at any
such `L_0`, then

```text
product_(l=L_0+1)^L [1-mu_l^*]
 >= product_(l=L_0+1)^L [1-5/(4l)],                  (3.19)
```

which has only a universal polynomial loss in `L/L_0`.  This does not bound
`gamma_(L_0)^*`; all pair lengths below the smoothing scale remain in the
base problem.

## 4. Accounting and dependencies

There are no comparison paths, congestion, or stochastic estimates in this
checkpoint.  Every operator is an exact conditional expectation under the
uniform fixed-endpoint bridge.  The only scan factors are the normalized
averages in (1.1), (1.2), and (2.3); (2.4) checks them exactly.

Dependencies:

- proved: uniform bridge law and exact conditional heat baths;
- proved here: deletion/conjugation bijection, pair-heat-bath intertwining,
  recursion (2.7), marginal formulas, and block Gram reduction;
- cited only for methodological provenance: Carlen--Geronimo--Loss Lemma 3.1;
- not used: crossing-pair commutation, Caputo's three-site threshold,
  canonical routing, or finite-spectrum extrapolation.

## 5. First unproved proposition

**SCALAR CORRELATION ACCUMULATION.**  Prove universal `c>0,C<infinity`
such that, for every `N>=3`, every `3<=L<=C_0N log(N+1)`, and every chain of
feasible endpoints arising in (2.1),

```text
product_(l=3)^L [1-mu_l^*] >= c (NL)^(-C),             (5.1)
```

or prove a sharper CGL-style estimate for `gap(C_(L,h))` from the scalar
spectra (3.12)--(3.13) that has one universal polynomial loss.  A sufficient
but possibly stronger statement is `mu_l^*<=C_1/l` after finitely many
universally controlled initial lengths.

Equation (3.18) proves that sufficient estimate above the universal
`C_mix N log(N+1)` threshold.  Hence the unresolved accumulation range in
(5.1) is now confined to `3<=l<C_mix N log(N+1)`; this interval still grows
with `N` and cannot be treated as finitely many universal exceptions.

This complete-pair gap would still need the separately audited
local-to-complete Dirichlet comparison before it yields the aligned adjacent
bridge gap.

## 6. Self-attack and calibration

The reduction is not a gap estimate.  The forward operator `K_(l,h)` is
normal but generally non-self-adjoint because (3.2) is not exchangeable.
Normality reduces the Gram spectrum to scalar matrices, but it gives no
quantitative separation of a positive real eigenvalue `kappa` from one.  A
mode invariant under conjugation by `h` may have precisely that dangerous
phase.  The block dimension is polynomial, but a dimension bound alone can
still permit exponentially small spectral gaps.
Moreover, a bound of the form `1-mu_l>=poly^(-1)` at every level would multiply
to a superpolynomial loss; the accumulated estimate (5.1), not mere
irreducibility, is required.

Boundary checks:

- `l=2`: (1.1) is a whole-fiber heat bath and has gap one;
- singleton endpoint fibers: all displayed gaps use the stated convention
  one;
- arbitrary nonidentity endpoint: (2.2), (3.1), and (3.2) retain the order of
  `h`, so no central-endpoint assumption is hidden;
- crossing pairs: the proof uses a single global coordinatewise bijection,
  not commutation of `P_ij` and `P_kl`;
- product-fiber multiplicity: (3.1)--(3.3) are on microstates and only then
  quotient the off-diagonal range, so the multiplicities `M,3,2` are retained.

Verdict: **PROVED** for the structural recursion, normality, and scalar block
reduction; **OPEN AT A NAMED STEP: SCALAR CORRELATION ACCUMULATION** for the
gap.  An independent audit of the strengthened normality claim is active.
