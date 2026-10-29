# Adjacent-chain gap: a three-gate theorem and the unresolved N+1 bound

Author status: **proved** scoped statements below, pending independent
review. **Unresolved:** an inverse-polynomial gap in growing N for a full
N-cycle at length N+1. No replacement sampler is used in this proof attempt.

## 1. Model and exact two-factor comparison

Let T_N contain all M=binom(N,2) transpositions, with N>=2. Products act
rightmost first. Fix a feasible endpoint g and length m, and let pi be
uniform on Omega_g(N,m). For m>=2 define

    K_A=I/2+H/4+R/4.

H chooses uniformly among the m-1 linear adjacent slots and two signs,
using (a,b)->(b,bab) or (aba,a). R chooses a uniform adjacent slot,
refreshes equal a,a to uniform s,s, and otherwise holds. There is no
wraparound slot. These are the originally requested adjacent moves.

Let E_i resample gates i,i+1 uniformly conditional on their product and
the other gates. It is an orthogonal conditional-expectation projection
in L2(pi). Define half-lazy exact two-factor heat bath

    Q=I/2 + [1/(2(m-1))] sum_i E_i.

For a reversible kernel P, write
E_P(f,f)=<f,(I-P)f>_pi. Let gamma(P) be its Poincare gap.

**Proposition (proved).** On every feasible fiber,

    (1/2) E_Q <= E_(K_A) <= E_Q,
    (1/2) gamma(Q) <= gamma(K_A) <= gamma(Q).                       (1)

Proof. A product of two transpositions has exactly three possibilities:

| Product | Number of ordered factorizations | Ratio K_A/Q on each nontrivial update |
| --- | --- | --- |
| identity | M, all s,s | 1/2 |
| a 3-cycle | 3 | 3/4 |
| two disjoint transpositions | 2 | 1 |

For the identity case, Q gives each new pair probability 1/[2(m-1)M]
and K_A gives 1/[4(m-1)M]. For a 3-cycle, the two signed Hurwitz moves
give the other two pairs, each with probability 1/[8(m-1)], versus
1/[6(m-1)] in Q. For disjoint transpositions, both signs perform the
same swap, giving 1/[4(m-1)] in both chains. Sum the off-diagonal
Dirichlet-form contributions. The three-case classification is complete,
so this is an all-N,m proof, not extrapolation from finite enumeration.

## 2. A genuine uniform-in-N bound when m=3

**Theorem (proved).** For every N>=3 and every feasible nontrivial
Omega_g(N,3),

    gamma(K_A) >= 1/24.                                           (2)

This fixes the length at three; it is not the growing-length N+1 theorem.

Put a=t_1 and b=t_3. The middle gate is forced to be a g b. Thus
Omega_g(N,3) is the set of edges of a bipartite graph whose two vertex
sets are feasible outer transpositions, with incidence matrix

    A_ab = 1_{a g b is a transposition}.

Write r_a=sum_b A_ab and c_b=sum_a A_ab. The uniform word law is uniform
on these edges; the outer marginals are proportional to r and c. Define
the normalized incidence matrix

    W = diag(r)^(-1/2) A diag(c)^(-1/2).

Its trivial singular value is 1. Let s be its largest singular value on
the orthogonal complements of the marginal constants. Equivalently, s
is the largest absolute correlation of centered functions of a and b.

E_1 projects onto functions of b; E_2 onto functions of a. The two-projection
calculation gives

    gap(2I-E_1-E_2) >= 1-s.                                      (3)

For completeness, take paired singular functions u(a),v(b) with unit norm
and E[u|b]=sigma v, E[v|a]=sigma u. On their span E_1+E_2 has eigenvalues
1+sigma and 1-sigma. Subspaces orthogonal to both ranges give eigenvalue
zero for E_1+E_2; unmatched range vectors give eigenvalue one. Constants
give eigenvalue two. Thus (3) follows, and s<1 also excludes additional
invariant components. This argument is finite-dimensional linear algebra.

At length three, I-Q=(2I-E_1-E_2)/4. It remains to prove s<=2/3 for
all possible endpoints. An odd permutation of reflection length at most
three has one of four nontrivial cycle types: (2), (4), (3,2), (2,2,2).

### 2.1 Transposition endpoint, all ambient N

By conjugation take g=(01). Feasible outer gates are all T_N, and A is
symmetric. The gate g is adjacent to every gate, including itself. For
each k>=2 the pair (0k),(1k) spans a complete 2-by-2 block with loops,
and each is adjacent to g. Every gate disjoint from g is adjacent only
to itself and g. No other edges occur: this follows from the two-factor
product classification in Section 1. Row degrees are respectively M,3,2.

Set k=N-2 and d=binom(N-2,2), so M=1+2k+d. Antisymmetric vectors inside
each two-gate block have eigenvalue zero. In the remaining orthonormal
basis, W is an arrowhead matrix: center diagonal 1/M, k peripheral
diagonals 2/3 with squared couplings 2/(3M), and d peripheral diagonals
1/2 with squared couplings 1/(2M).

On the codimension-one subspace with zero center coordinate, its Rayleigh
quotient is at most 2/3. By the variational principle the second-largest
eigenvalue is at most 2/3. Also W+(1/2)I is positive definite: its
peripheral block is positive, and its scalar Schur complement is

    1/2 + 1/M - 4k/(7M) - d/(2M)
      = (3/2 + 3k/7)/M > 0.

Therefore all negative eigenvalues have magnitude less than 1/2. It
follows that s<=2/3. For N>=4 equality holds: assign outer-gate value +1
on (02),(12), -1 on (03),(13), and zero elsewhere. This is centered
and its conditional expectation at the other end is exactly 2/3 times
the same function. For N=3, W has only singular values 1,0,0. N=2 is
a singleton target and needs no positive-gap assertion.

### 2.2 The three minimal endpoint types

For the other endpoint types, length three is minimal. Every prefix
step merges two permutation cycles, so its support is a forest whose
components are exactly the endpoint's nontrivial cycles. Unused ambient
vertices cannot appear. Therefore all N reduce exactly to representatives
on four, five, or six labels. This is a completeness argument.

Here are their incidence matrices, with feasible gates in lexicographic
order and endpoints (0123), (012)(34), (01)(23)(45):

    A_4 = [[0,0,0,1,1,1],       A_32 = [[0,0,1,1],
           [1,0,0,0,0,1],               [1,0,0,1],
           [1,1,0,1,0,0],               [0,1,0,1],
           [0,1,1,0,0,1],               [1,1,1,0]],
           [0,0,1,1,0,0],
           [1,0,1,0,1,0]],      A_222 = [[0,1,1],[1,0,1],[1,1,0]].

One can certify s^2<=4/9 with rational arithmetic as follows. Let

    G=(4/9)diag(r)-A diag(c)^(-1) A^T.

Write f_last=-sum_(i<last) r_i f_i/r_last, and let V map the free
coordinates to this weighted-mean-zero vector f. Then s^2<=4/9 is
equivalent to positive semidefiniteness of B=V^T G V. The exact LDL^T
pivots of B in the displayed order are:

| Endpoint type | Pivots |
| --- | --- |
| (4) | 4/3, 16/27, 31/48, 20/31, 16/45 |
| (3,2) | 35/54, 49/90, 1/2 |
| (2,2,2) | 7/9, 7/12 |

They are all positive, certifying the desired inequality. The matrices
B and the exact elimination are also recorded in results.json/check.py.
This finite certificate covers ALL minimal length-three endpoints by the
preceding classification, unlike an unqualified finite spectral table.

Combining s<=2/3, (3), and (1) yields

    gamma(K_A) >= (1/2)(1/4)(1-2/3)=1/24,

proving (2).

## 3. Consequence for a three-factor block chain, on any endpoint fiber

For m>=3 let Q_3 be half-lazy random-scan exact same-product resampling
of a length-three linear block, chosen uniformly among m-2 choices.
Let Q_2=Q from Section 1. Then, for every f,

    E_(Q_3)(f,f) <= [12(m-1)/(m-2)] E_(K_A)(f,f)
                 <= 24 E_(K_A)(f,f).                             (4)

Proof. Conditional on the outside of any triple, (2) gives
Var(f|outside)<=24 E_(K_A,triple)(f,f). Average over all triples and
multiply by the half-lazy coefficient 1/2. The local K_A,triple chooses
either of its two pair slots with probability 1/2. An interior global
slot belongs to two triples, a boundary slot to one, so summing these
local forms is at most (m-1) E_(K_A). This proves (4).

In the other direction conditional variance increases on average when
more coordinates are left free. Every pair slot is contained in at least
one triple, with at most two assigned pairs per triple. Therefore

    E_(K_A) <= E_(Q_2) <= [2(m-2)/(m-1)] E_(Q_3) <= 2 E_(Q_3).

Thus K_A and Q_3 have comparable gaps with absolute factors, for all
N,m>=3. This comparison is a proved reduction, NOT a gap for Q_3.
No polynomial gap for that block chain is asserted here.

## 4. Why the local calculation does not prove the N+1 gap

Let h_i=I-E_i and G_m=sum_i h_i, so I-Q=G_m/[2(m-1)]. The terms are
projections; terms on disjoint pairs commute. If every three-site
generator h_i+h_(i+1) has gap at least delta, then

    {h_i,h_(i+1)} >= -(1-delta)(h_i+h_(i+1)).

Expand G_m^2, retain the positive products on disjoint pairs, and sum:

    G_m^2 >= (2delta-1) G_m
             + (1-delta)(h_1+h_(m-1)).                           (5)

This elementary open-chain calculation gives a positive uniform gap
from delta>1/2. Our uniform three-gate gap is exactly delta=1/3 once
N>=4, so (5) gives no positive bulk bound. Boundary terms do not by
themselves dominate G_m. This is the first failed step of the tested
local-to-global route, not evidence of slow mixing of K_A.

The bad conditional case really occurs in the requested family. Let
g_0=(01), T=((12),(23),...,(N-2,N-1)). Every word u of length three
with product g_0 gives (u,T) of length N+1 and product c=(0 1 ... N-1).
Fixing T leaves EXACTLY the entire transposition-endpoint three-gate
fiber. The 2/3-correlation function of Section 2.1 therefore cannot be
excluded by requiring the whole circuit to compute a full cycle.

The related periodic finite-size threshold is described in Gosset and
Mozgunov, [arXiv:1512.00088v1](https://arxiv.org/pdf/1512.00088), Corollary 2
and Theorem 3. No periodic theorem is transferred to the open endpoint
fiber; equation (5) is derived directly here. A search also found Lemm's
arXiv:1709.02756, but its primary page marks it superseded by
arXiv:1801.08915. The withdrawn version is not a proof dependency.

## 5. An explicit actual-K_A lower bound at m=N+1, but not polynomial

**Proposition (proved using the prior constructive connectivity and checked
count formula).** For N>=3 and g=c a full N-cycle, m=N+1,

    gamma(K_A) >= 3/[N^(N+3) (N-1)^2 (N+1)^3].                    (6)

This is N^{-N-O(1)}, not inverse-polynomial in N. It does not prove the
user's fast-mixing conjecture.

Here is the full quantitative argument. By the vertex-sweep construction
in the [nonlocal-lift proof](../20261014-111117-nonlocal-graph-lift/proof.md),
Section 3, expose one square in at most Nm adjacent Hurwitz moves. Move
it to the end in at most 2m further moves and refresh it to a fixed square
in one move. The remaining prefix is a minimal factorization of c, since
its length is m-2=N-1; normalize it in at most N(m-2) Hurwitz moves.
Every word reaches the same canonical word in at most

    Nm+2m+1+N(m-2) <= 2(N+1)m

moves. Consequently the move graph has diameter at most
D=4(N+1)m=4(N+1)^2. Each nonzero K_A edge has probability at least

    p_min=1/[4(m-1)M]=1/(4NM).

Indeed square edges have that probability, incident Hurwitz edges have
probability 1/[8(m-1)], and disjoint swaps have 1/[4(m-1)]. Since
N>=3 gives M>=3, the displayed minimum is valid.

For S states with uniform law, choose a simple path of length <=D for
each ordered pair, erasing loops in the canonical routes if necessary.
Cauchy-Schwarz on each path and the crude bound of S^2 routes through
any directed edge give

    Var_pi(f) <= (D S/p_min) E_(K_A)(f,f),
    gamma(K_A) >= p_min/(D S).

The fixed-cycle count is S=N^(N+1)(N^2-1)/24; its source normalization
is checked in the [excess-one proof](../20261014-133815-cycle-excess-one/tree_jump_proof.md),
Section 5, from Goulden-Jackson-Vakil Proposition 1.1 and Theorem 3.1,
equation (21). Substitution yields (6).

The exponential loss is explicit: it is the factor S in the congestion
bound. No assertion of polynomial congestion through the normal form is
made. Eliminating this loss needs more than the short paths proved here.

## 6. Boundary cases, dependencies and remaining target

At N=1 only the empty word exists. At N=2 every feasible fiber is a
singleton. At m=0,1 every nonempty fiber is a singleton. For m=2 and a
nontrivial fiber, the exact K_A gaps are 1/4 for endpoint identity, 3/8
for a 3-cycle and 1/2 for two disjoint transpositions. These follow
directly from the table in Section 1. For a full cycle, feasibility is
m>=N-1 with m=N-1 modulo 2; thus odd m is legitimate when N is even.
Identity with odd m is empty. The theorem (2) covers odd endpoint parity,
including the minimal four-cycle case. S_3 admits the stronger already
proved bound 1/[4(m-1)] at all feasible lengths; it is not upgraded to N>3.

Dependencies distinguish the claims:

- Sections 1-4: self-contained two-factor classification, exact rational
  certificates and finite-dimensional projection algebra. No external
  Hurwitz classification or finite-size theorem is assumed.
- Section 5: the prior constructive vertex sweep and the checked full-cycle
  count formula. The spectral comparison is explicitly proved here with
  its exponential factor retained.
- **Unresolved:** an inverse-polynomial Poincare bound for G_(N+1) in the
  full-cycle sector. By (1), this is equivalent up to a factor two to the
  requested bound for K_A. By (4), the exact three-factor block version
  is equivalent up to constants too, but remains unresolved.

The local correlation obstruction is stable enough to retain. The proof
attempt does not justify promoting the full conjecture or changing the
manuscript's unresolved polynomial-mixing status.
