# Minimal-long-cycle refutation of the `A/l` product-correlation bound

Date: 2026-08-12.  Permutations compose as `(pq)(x)=p(q(x))`, and tuple
products are multiplied from left to right.  All Hilbert spaces below are
complex.  This note concerns the complete-pair auxiliary bridge, not the
original local `{3,4,5}` chain.

## Theorem

Let `l>=3`, put `n=2l+1`, and let `h_n=(0 1 ... n-1)` in `S_n`.  Group a
uniform minimal transposition factorization

    t_1 ... t_(n-1) = h_n

into `l` raw pairs `X_i=(t_(2i-1),t_(2i))`, and write
`G_i=t_(2i-1)t_(2i)`.  Let `mu_l(h_n)` be M16's top mean-zero eigenvalue of
the averaged one-coordinate projection `A_(l,h_n)`.  Then

    liminf_(l->infinity) sqrt(l) mu_l(h_n)
       >= 24/(sqrt(2)d_0) = 1.5097776...,

where

    d_0 = 8/sqrt(2 pi) int_0^1
              sin^4(pi x)/[x(1-x)]^(3/2) dx
        = 11.2404385....

In particular, there is no universal finite `A` for which

    mu_l(h) <= A/l

holds for every `N>=3`, feasible `h in A_N`, and `l>=3`.

This refutes **PRODUCT-INCREMENT BASE CORRELATION** as literally stated.  It
does not upper-bound the gap of the complete-pair chain, produce a cut for
the original chain, or imply Terminal B.  In particular, an
`O(l^(-1/2))` exceptional mode at one length for each changing value of `N`
does not by itself refute a weaker polynomial accumulated recursion.

## 1. Exact rank-two moment lemma

Let

    omega=exp(2 pi i/n),  u_v=omega^(-v),
    a((r s))=-(u_r-u_s)^2.

Since `sum_v u_v^2=0`, this is the permutation-representation matrix
coefficient

    a(t)=sum_v u_v u_(t(v)).

It transforms by the nontrivial cyclic-conjugation character of frequency
two, and therefore has mean zero.  Put

    A_k=k^(k-2)/(k-1)!=k^(k-1)/k!,  A_1=1.

For a uniform minimal factorization as above and any distinct positions
`i<j`, define

    v_n=E |a(t_i)|^2,
    c_n=E [conj(a(t_i)) a(t_j)].

Then the following statements hold:

    v_n = 8n (n-2)!/n^(n-2)
          sum_(d=1)^(n-1) A_d A_(n-d) sin^4(pi d/n),       (1.1)

    sqrt(n) v_n -> d_0,                                    (1.2)

    Re c_n = 12/n + o(1/n).                                (1.3)

The joint law and hence `c_n` do not depend on `i,j`.

### Counting proof

Let `T=sum_(t in T_n)t` in the group algebra.  It is central.  Thus, in the
project convention,

    Pr(t_i=e,t_j=f)
      = [h_n] e f T^(n-3) / [h_n] T^(n-1),                (1.4)

independently of the separation `j-i`; also
`[h_n]T^(n-1)=n^(n-2)`.

If a permutation has cycle sizes `q_1,...,q_k` and transposition rank `r`,
the number of its minimal transposition factorizations is

    r! product_s A_(q_s).                                  (1.5)

This follows by minimally factoring each disjoint cycle and interleaving
the factors.  It is Féray--Kortchemski, Lemma 2.1.  Applying (1.5) after a
fixed first transposition whose endpoints have clockwise gap `d`, and then
pairing `d` with `n-d`, gives (1.1).

For two disjoint extendible first edges, write their four positive cyclic
gaps as `a,b,u,v`.  The residual cycle sizes are `a,b,u+v`.  Enumerating the
cyclic start and the two noncrossing placements gives the exact disjoint-edge
contribution

    D_n = 16n (n-3)!/n^(n-2)
          sum_(a,b,u,v>=1; a+b+u+v=n)
          A_a A_b A_(u+v)
          sin^2(pi a/n) sin^2(pi b/n)
          cos(2 pi(v-u)/n).                               (1.6)

Pairs sharing one endpoint have three positive cyclic gaps.  The uniform
Stirling bound

    A_k <= C e^k k^(-3/2)                                (1.7)

and

    |a((r s))| <= C min(|r-s|,n-|r-s|)^2/n^2             (1.8)

give an absolute `O(n^(-3/2))` contribution: split the gap sum according to
the number of gaps of order `n`.  The bulk three-macroscopic part is
`O(n^(-2))`; one small and two macroscopic gaps is the worst part and is
`O(n^(-3/2))`; with two small gaps, (1.8) supplies the missing power of
`n`.  These three estimates are geometric sums after (1.7), uniformly in
the dyadic scale of every small gap.

The same Stirling bound, now with the sine zeros at the boundary as an
integrable envelope, turns (1.1) and (1.6) into Riemann sums.  It gives
(1.2) and

    n D_n -> (4/pi^2) int_(x,y>0,x+y<1)
        sin^2(pi x) sin^2(pi y) sin(2pi(1-x-y))
        /[xy(1-x-y)]^(3/2) dx dy = 12.                   (1.9)

For completeness, put `s=x+y`.  The inner convolution has the exact form

    int_0^s sin^2(pi x) sin^2(pi(s-x))
             /[x(s-x)]^(3/2) dx
      = pi^2/s [J_1(2pi s)-2cos(pi s)J_1(pi s)].          (1.10)

Substitution in (1.9), followed by the Bessel equation and integration by
parts, makes the unscaled triangle integral `3pi^2`.  An entirely algebraic
check expands the three sine factors: the resulting absolutely convergent
Dirichlet-integral series is

    sum_(p,q>=1,r>=0) c_p c_q d_r
      Gamma(2p-1/2)Gamma(2q-1/2)Gamma(2r+1/2)
      /Gamma(2p+2q+2r-1/2),                              (1.11)

where

    c_p=(-1)^(p+1)(2pi)^(2p)/[2(2p)!],
    d_r=(-1)^r(2pi)^(2r+1)/(2r+1)!.

Duplication and Chu--Vandermonde twice give `3pi^2`.  Equations
(1.6)--(1.11), plus the `O(n^(-3/2))` shared-edge remainder, prove (1.3).

Féray--Kortchemski multiply permutations in the opposite convention
(`sigma tau=tau o sigma`).  Reversing the tuple translates their Lemma 2.1,
Proposition 1.1, and Corollary 1.2 to the project convention.  The central
class-sum derivation (1.4) is convention-internal, and the real moments are
unchanged by the resulting inversion/conjugation.

## 2. A legitimate product-sector witness

For one raw pair `X=(r,s)`, let `g=rs`, and define

    B(X)=a(r)+a(s),
    f(g)= 1/q(g) sum_(r,s in T_n:rs=g) [a(r)+a(s)],       (2.1)

where `q(g)` is the number of ordered raw lifts of `g`.  Thus `f(G)` is the
conditional expectation of `B(X)` on its product fiber.  It is an explicit
frequency-two matrix-coefficient function on the product support
`{e, 3-cycles, double transpositions}`.  Cyclic covariance gives `E f=0`.

The bridge density depends on a raw pair only through its product.  Given
two product coordinates, their raw lifts are independent and uniform in
their respective product fibers.  Therefore, for `i<j`,

    E[conj(f(G_i)) f(G_j)]
      = E[conj(B(X_i)) B(X_j)]
      = 4c_n.                                             (2.2)

The last equality expands the two transpositions in each raw pair and uses
the position-independence (1.4) for all four cross terms.  Conditional
expectation is an `L^2` contraction, so

    V_f:=E|f(G_i)|^2
      <= E|B(X_i)|^2
       =2v_n+2 Re c_n
       =2d_0 n^(-1/2)+o(n^(-1/2)).                       (2.3)

Let `K_(l,h_n)` be M16's forward product correlation block.  From
(1.3), (2.2), and (2.3), its Rayleigh quotient on `f` obeys

    Re <f,Kf>/||f||^2
       >= (24/d_0)n^(-1/2)+o(n^(-1/2)).                  (2.4)

No assertion that `f` is an eigenfunction is needed.

Put the same `f` in all `l` coordinate slots of M16's exact block Gram
form.  Its Gram Rayleigh quotient is

    1/l + (l-1)/l Re <f,Kf>/||f||^2.                     (2.5)

Since the nonzero spectrum of that Gram operator is the nonzero spectrum of
`A_(l,h_n)`, equations (2.4)--(2.5), with `n=2l+1`, prove the theorem.

## 3. Scope and falsification checks

The proof uses a minimal long-cycle endpoint, not the identity endpoint.
It applies for every sufficiently large `l` (indeed the exact formulas hold
for every `l>=3`).  Odd original word length remains empty; here the original
length is `2l=n-1`, which is even.  The cases `m=0`, `N=2`, and original
`m=2` are outside the theorem.  At `l=2` the complete-pair update is a
whole-state heat bath and the M16 recursion begins later.  Nothing here
changes the exact `S_3,m=4`, `S_4,m=4`, or `S_4,m=6` calibrations.

The deterministic scripts in this directory reproduce the exact finite
counts followed by floating cyclotomic diagonalization.  They match the
inherited full value at `(N,l)=(7,3)` and give

| `l` | `l mu_l(h_(2l+1))` |
|---:|---:|
| 3 | 2.240910774 |
| 4 | 2.533699403 |
| 6 | 3.102797365 |
| 8 | 3.620219404 |
| 10 | 4.091221961 |

These values only falsify finite candidates; the asymptotic proof is
(1.1)--(2.5).  The fiber-averaged witness itself has Gram Rayleigh values
`0.7385356, 0.6228827, 0.5044729, 0.4393296` at `l=3,4,6,8`.

Strongest self-attack: the audit-sensitive enumeration is the factor `16n`
in (1.6), and the audit-sensitive asymptotic estimate is the three-gap
`O(n^(-3/2))` shared-endpoint remainder.  Both are independent of the
product-fiber projection argument in Section 2; exact enumeration through
`n=51` agrees with the formulas.  A referee should check those two items
before promotion.
