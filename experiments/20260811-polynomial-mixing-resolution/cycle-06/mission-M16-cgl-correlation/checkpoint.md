# Cycle 06 M16-CGL halfway checkpoint

## 1. Exact leave-one-out theorem

Let E=T_N^2, p(a,b)=ab, and let pi_(l,h) be uniform on the nonempty
microbridge

    Omega_l(h)={x in E^l: p(x_1)...p(x_l)=h}.

Composition is (pq)(x)=p(q(x)).  Let P_ij be conditional expectation given
all raw coordinates outside {i,j}, and set

    C_(l,h)=binom(l,2)^(-1) sum_(i<j) P_ij.

For A_k=sigma(x_k), let R_k=E[.|A_k] and A_(l,h)=l^(-1)sum_k R_k.
Give singleton fibers gap one.  If

    delta_(l-1)^*=min_q gap(C_(l-1,q))

over all feasible endpoints q, then, for every l>=3 and feasible h,

    gap(C_(l,h)) >= delta_(l-1)^* [1-mu_l(h)],          (1.1)

where mu_l(h) is the top eigenvalue of A_(l,h) on mean-zero functions.

### Braid and endpoint orientation

For a microstate x=(a,b) and sigma in S_N, write

    x^sigma=(sigma^-1 a sigma,sigma^-1 b sigma).

The right micro-Hurwitz map

    H(x,y)=(y,x^(p(y)))

is a product-preserving bijection.  On the slice x_k=z with g=p(z), applying
H at k-1,k, then k-2,k-1, down to 1, moves z unchanged to the first
coordinate and gives

    (z, x_1^g,...,x_(k-1)^g,x_(k+1),...,x_l).

Deleting z leaves endpoint g^-1 h.  Moving z unchanged to the right boundary
with inverse Hurwitz moves instead leaves endpoint h g^-1.  These two
endpoints are conjugate, but they must not be interchanged within one chosen
braid convention.

On a fixed z-slice the remaining-coordinate map is a product of individual
bijections: conjugation by g before k and identity after k.  Thus it maps the
sigma-field outside any pair i,j not equal to k onto the sigma-field outside
the corresponding shorter-word pair.  This includes i<k<j.  Conditional
expectation covariance therefore intertwines every leave-one-out P_ij with
the corresponding raw-pair heat bath on Omega_(l-1)(g^-1 h).

Let

    Q_l^(k)=binom(l-1,2)^(-1)
            sum_(i<j, i,j not equal k) P_ij.

Every pair occurs in l-2 of these sums, so

    C_(l,h)=l^(-1)sum_k Q_l^(k).                         (1.2)

On each x_k-slice, Q_l^(k) has gap at least delta_(l-1)^*.  Subtracting the
slice mean R_k f gives

    <f,Q_l^(k)f>
    <=(1-delta^*)||f||^2+delta^*<f,R_k f>.

Averaging proves the quadratic CGL inequality and then (1.1).  No commutation
between crossing P_ij is used.

## 2. Exact block-correlation spectrum

Let rho_k be the x_k marginal, H_k=L^2_0(E,rho_k), and let
J_k:H_k -> L^2_0(Omega_l(h)) be J_k u=u(x_k).  With

    T(u_1,...,u_l)=l^(-1/2)sum_k J_k u_k,

one has

    A_(l,h)=T T^*.

Hence its nonzero mean-zero spectrum is exactly that of the l-by-l block
Gram operator

    G=T^*T,   G_ij=l^-1 J_i^*J_j,                       (2.1)

where J_i^*J_j u=E[u(x_j)|x_i].  This identity is finite-dimensional and
does not assume coordinate exchangeability.

### Central count formula

Put

    W=(sum_(t in T_N)t)^2=sum_(x in E)p(x)

in the group algebra and H_r(q)=[q]W^r.  Since W is central, for a fixed
microstate x with g=p(x),

    Pr(x_i=x)=H_(l-1)(g^-1 h)/H_l(h),                   (2.2)

independently of i.  For i<j and fixed x,y with products g,s,

    Pr(x_i=x,x_j=y)
      =H_(l-2)((gs)^-1 h)/H_l(h),                       (2.3)

independently of the separation j-i.  Thus all marginals are one rho and
G has I/l on its diagonal, K/l above it, and K^*/l below it, where

    (Kf)(x)=sum_y
      H_(l-2)((p(x)p(y))^-1 h)
      /H_(l-1)(p(x)^-1 h) f(y).                        (2.4)

The endpoint constraint depends only on p(x).  Therefore the micro-lift
fiber-centered sector has all off-diagonal blocks zero and exact Gram
eigenvalue 1/l.  Every other nonzero eigenvalue comes from product functions.
The product support has size

    1+2 binom(N,3)+3 binom(N,4)=O(N^4),

so the unresolved correlation operator has dimension O(l N^4), not the size
of the full bridge.

## 3. Cyclic normality and scalar diagonalization

Define theta(x)=h^-1 x h coordinatewise and U f=f composed with theta.
The uniform bridge is invariant under

    (x_1,...,x_l) -> (x_2,...,x_l,theta(x_1)).           (3.1)

Indeed, if g_1...g_l=h, then
g_2...g_l(h^-1 g_1 h)=g_1^-1 h h^-1 g_1 h=h.
Using (2.3) and applying (3.1) l-1 times gives

    (X,Y) has the same law as (Y,theta(X)).              (3.2)

The marginal is theta-invariant, so U is unitary.  Equation (3.2) implies

    <f,Kg>=<Kf,Ug>, hence K=K^*U.                       (3.3)

Taking adjoints and comparing with (3.3) gives

    K^*=U^-1 K=K U^-1,   KU=UK,

and K is normal.  Thus K and U have a simultaneous orthonormal eigenbasis.
If Kv=kappa v and Uv=u v, then

    kappa=conjugate(kappa) u.                            (3.4)

For one such v, the scalar Gram block is l^-1 times the Hermitian matrix
with diagonal 1, every strict upper entry kappa, and every strict lower entry
conjugate(kappa).

Write kappa=r exp(i phi).  If kappa is nonreal, let

    theta_n=(-2phi+2pi n)/l,  n=0,...,l-1.

The l scalar eigenvalues are

    l^-1 [1-r sin(phi+theta_n/2)/sin(theta_n/2)].        (3.5)

Equivalently, the eigenvector ratios q=exp(i theta_n) satisfy
q^l=conjugate(kappa)/kappa.  If kappa is real, the eigenvalues are

    [1+(l-1)kappa]/l                 once,
    (1-kappa)/l                      multiplicity l-1.   (3.6)

For kappa=0 all are 1/l.

## 4. Exact failures and surviving route

The literal product including j=2 is false: for a nontrivial two-coordinate
bridge, p(x_1) determines p(x_2) and conversely, so A_2 has a nonconstant
eigenfunction of eigenvalue one.  The recursion product must start at j=3.

The tempting bound mu_l<=1/(l-1) is also false.  At l=3,

    C_(3,h)=(P_12+P_13+P_23)/3
           =(R_3+R_2+R_1)/3=A_(3,h).

The inherited exact N=6 endpoint type (2,2,1,1) Rayleigh certificate gives

    gap(C_3)
    <=11308644378456917647/39796565095659282750
    <1/3,

so mu_3>2/3>1/2.

A surviving sufficient proposition is a universal maximal-correlation tail:

    ||K_(l,h)||_(L^2_0 -> L^2_0) <= b/l                (4.1)

for all l beyond one universal constant, every N, and every feasible h.
The scalar Gram bound would then give mu_l<=(1+b)/l.  The finitely many
initial factors are inverse-polynomial by the accepted fixed-length bridge
bounds, while the tail product is polynomial in l.

There is also an exact refined CGL dichotomy.  For eta<mu_l, let E_eta be
the sum of mean-zero A_l eigenspaces above eta, V_eta the smallest
C_l-invariant subspace containing E_eta, and nu_eta the top C_l eigenvalue
on V_eta.  Then either

    lambda_2(C_l)<=nu_eta,

or

    gap(C_l)>=delta_(l-1)^*(1-eta).                     (4.2)

This follows by applying the CGL quadratic inequality on V_eta orthogonal.
The normal scalar decomposition makes E_eta explicit and polynomial
dimensional.  What remains is quantitative control of (4.1), or of C_l on
these exceptional scalar blocks.

## 5. Finite audit status

Exact convolution counts and floating diagonalization were run for N=3,4,5,6
at the recorded bounded lengths.  They verify arbitrary-noncentral-endpoint
instances of K=K^*U, KU=UK, normality, and the scalar spectrum to errors below
10^-14.  They also falsify mu_l<=1/(l-1), but the rigorous falsifier is the
exact rational l=3 certificate above.  No finite spectrum is used as a
universal proof.

