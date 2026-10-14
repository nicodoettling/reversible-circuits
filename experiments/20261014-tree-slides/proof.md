# Polynomial mixing of labeled-tree edge slides

Status: **proved**, using the checked external down-up gap theorem stated
in Section 3. This is a same-author proof with exact finite checks, pending
independent review. The claim concerns labeled trees after dropping circuit
order and functionality. Transfer to adjacent Hurwitz circuits remains
**unresolved**.

## 1. States, targets and kernels

Let T_N be the set of all simple trees on the distinguishable vertices
{0,...,N-1}. There is no edge ordering, root constraint, planar embedding,
degree restriction, or permutation-product constraint. For N>=3 set

    r=N-1,  D=binom(N-1,2),  C=|T_N|=N^(N-2),
    W(T)=sum_v binom(deg_T(v),2),  Wbar=E_uniform W.

A wedge is an unordered pair of edges sharing a vertex. Given edges ab,bc,
its two directions are

    {ab,bc} -> {ac,bc},       {ab,bc} -> {ab,ac}.

Only the displayed edge is replaced; all other edges stay. Each result is
a tree, since ac crosses the cut created by deleting the replaced edge.
Different wedge/direction choices have different outcomes: the removed
edge and added edge identify the retained edge uniquely. Every move has
a unique reverse. Thus a tree has exactly 2W(T) slide neighbors. Also

    N-2 <= W(T) <= D.

The lower bound follows from binom(d,2)>=d-1 for d>=1 and sum_v d_v=2N-2;
the upper bound counts all unordered pairs of the N-1 edges. Paths and
stars attain the two bounds, respectively.

All three kernels below include a separate probability 1/2 of holding.

P, the requested proposal: otherwise choose a uniform wedge and a uniform
direction, and perform the slide. Its target is the sampler-defined law

    mu(T)=W(T)/(C Wbar),      P(T,T')=1/[4W(T)] for slide neighbors.

U, a uniform-target comparison variant: otherwise choose a uniform
unordered pair of distinct tree edges among all D pairs. If disjoint,
hold; if incident, choose a uniform direction and slide. Its target nu is
uniform on T_N and U(T,T')=1/(4D) for slide neighbors.

M, the uniform-target Metropolis variant: use P's proposal and accept T'
with probability min(1,W(T)/W(T')). Hence

    M(T,T')=1/[4 max(W(T),W(T'))],

and its target is nu. These formulas prove detailed balance for every
claimed law. All diagonal probabilities are at least 1/2. No circular
window convention applies because the states have no edge order.

## 2. The quantitative claim

For N>=3, all three kernels are irreducible and satisfy

    gap(P), gap(U), gap(M) >= gamma_N
        := 1/[r D (N-2)] = 2/[(N-1)^2 (N-2)^2].                 (1)

The gap means 1 minus the second-largest eigenvalue in the relevant
stationary L2 space. Half laziness makes all eigenvalues nonnegative.
For 0<epsilon<1/2, from every starting tree, all three obey the conservative
common total-variation bound

    t_mix(epsilon) <= ceil(gamma_N^(-1) *
        [(N-2) log N + log((N-1)/(2 epsilon))]).                (2)

Thus mixing takes O(N^4 [N log N + log(1/epsilon)]) discrete steps. This
is a polynomial, deliberately non-sharp estimate, in the number N of
explicitly labeled vertices. It is not polynomial in log N wires.
Each step can be implemented in polynomial time by degree counts and
adjacency lists. No large hidden move is counted as a single slide.

For N=1 and N=2 there is only one tree and mixing time is zero; define the
walks to hold. In the minimal circuit analogy m=N-1. Odd m is permitted
when N is even: these are not identity words. N=3 corresponds to m=2,
and N=1 to m=0. The theorem imposes no identity-word parity condition.

## 3. Checked external dependency: spanning-tree down-up gap

Let B choose a uniform edge e of T, remove it, and let F=T-e have
components A,B with sizes a,b. Reinsert a uniformly selected edge between
A and B, including the removed edge among the ab choices. For distinct
trees T=F+e and T'=F+f,

    B(T,T')=1/(r ab).

The unchanged forest is unique for this off-diagonal transition, so this
is the full transition probability. B is uniform-reversible, and

    gap(B) >= 1/r.                                            (3)

Source: Nima Anari, Kuikui Liu, Shayan Oveis Gharan, Cynthia Vinzant,
*Log-Concave Polynomials II: High-Dimensional Walks and an FPRAS for
Counting Bases of a Matroid*, arXiv:1811.01816v3,
https://arxiv.org/pdf/1811.01816v3 . Theorem 1.1 (PDF p.2) gives the
gap 1/d for their explicitly defined drop-one/uniformly-complete walk;
Theorem 5.2 (PDF p.23) gives strong log-concavity of matroid basis
generating polynomials, with all external weights set to one here.

Hypothesis and normalization translation: use the graphic matroid of K_N,
whose ground set is its binom(N,2) possible edges, whose bases are exactly
T_N, and whose rank d is r=N-1. After deleting one basis edge the valid
completions are exactly the ab cross-component edges. Their chain includes
reinsertion of e, and no added half-laziness. Thus it is precisely B,
with the gap in (3), not a differently normalized edge-swap proposal.
Scalar normalization of the generating polynomial does not affect strong
log-concavity. The paper's definition, both theorem statements, and the
specialization were checked; the external theorem is invoked, not reproved.

## 4. Bridge-slide paths and congestion

For each off-diagonal B transition, orient the components of F so that
0 belongs to A, and write e={u,v}, f={x,y}, with u,x in A and v,y in B.
Keep every edge of F fixed throughout. First slide the A endpoint of the
bridge along the unique path u -> x within A, keeping v fixed. Then slide
the B endpoint along its path v -> y within B, keeping x fixed. Every step
is one permitted slide. Its length L obeys

    L <= (a-1)+(b-1)=N-2.                                    (4)

This also proves connectivity: ordinary spanning-tree exchanges connect
all trees, and each exchange has such a slide path. For completeness, to
move T toward a chosen target S, insert an edge of S minus T; its cycle
contains an edge outside S, which can be deleted. Repeat. This argument
is only for connectivity; no comparison flow is routed through S.

Fix a directed physical slide Z -> Z'. Its removed edge h is uniquely
Z minus Z'. Any comparison path using that step must have the same fixed
forest

    F=Z-h.                                                   (5)

Indeed the only changing edge on any routed path is its bridge. This
reconstruction is the crucial congestion control.

Suppose this slide moves the A endpoint across the oriented internal
edge p -> q of A, with the B endpoint fixed at v. Removing pq splits A
into sets of sizes a1,a2, with p on the first side and q on the second.
The possible original bridge e and final bridge f are characterized by:
u in the first side, x in the second side, the initial B endpoint equal
to v, and the final B endpoint y arbitrary. Thus exactly a1*a2*b ordered
B transitions route through this directed slide. Each has probability
1/(r ab), and (4) gives the length-weighted load

    sum_{(T,T'): path uses (Z,Z')} B(T,T') L(T,T')
       <= (N-2) a1 a2/(r a)
       <= (N-2) a/(4r)
       <= (N-2)/4.                                          (6)

If it moves the B endpoint, the corresponding count is a*b1*b2 and the
same bound follows. A fixed slide cannot be in both phases for this F,
because its moving endpoint belongs to exactly one component. A route
does not repeat a directed slide. No division by the number C of trees
has been included in (6).

Write E_K(g,g)=1/2 sum_{s,t} pi(s)K(s,t)(g(s)-g(t))^2.
Telescoping along a comparison path and Cauchy--Schwarz give

    E_B(g,g)
      <= (1/(2C)) sum_{directed slides Z->Z'}
           (g(Z)-g(Z'))^2 * load(Z,Z')
      <= D(N-2) E_U(g,g),                                    (7)

since U(Z,Z')=1/(4D). Combining (3) and (7),

    Var_nu(g) <= r E_B(g,g) <= r D(N-2) E_U(g,g).

This proves (1) for U. The argument uses an explicit polynomial
congestion bound, not just short paths or a graph-diameter bound.

## 5. Transfer to the requested and uniform-corrected kernels

For M, every off-diagonal transition is at least that of U and both have
target nu. Therefore E_M>=E_U and gap(M)>=gamma_N.

For P, detailed balance gives mu(T)P(T,T')=1/(4C Wbar), so

    E_P=(D/Wbar) E_U.

Furthermore, using the nu-mean as a candidate in the variance minimum,

    Var_mu(g)=min_c E_mu[(g-c)^2]
       <= (D/Wbar) Var_nu(g)
       <= (D/Wbar) gamma_N^(-1) E_U(g,g)
        = gamma_N^(-1) E_P(g,g).

This proves the same gap for P without an extra factor N.

For U and M, pi_min=1/C; for P, pi_min>= (N-2)/(CD)=2/[(N-1)C].
For any of these lazy reversible chains the usual spectral calculation
gives TV(K^t(z,.),pi)<=1/2 pi(z)^(-1/2) exp(-gamma_N t).
Using the common lower bound on pi_min and the looser sufficient time
gamma_N^(-1) log(1/(epsilon pi_min)) proves (2).

## 6. Boundaries, falsification and circuit scope

The requested P is not uniform for N>=4: an N-vertex star has W=D and
a path W=N-2, so the probability ratio of these particular labeled trees
is (N-1)/2. For N=3 the three trees all have W=1; P=U=M has diagonal 1/2,
off-diagonal 1/4 and gap 3/4, exceeding the bound gamma_3=1/2.

There is a tree/minimal-factorization bijection, but ordinary support
forgetting is not that bijection. Under rightmost-first permutation
composition, the ordered words

    ((13),(12),(34)),          ((13),(34),(12))

both have product (1234) and the same support tree. Their sets of pairs
adjacent in the word differ. Arbitrary graph-adjacent slides therefore
do not simply describe the original adjacent-slot Hurwitz kernel.
This negative witness and exact checks of all routed transitions through
N=6 accompany the analytic proof; finite tests do not supply the proof.

The first remaining obligation for a circuit theorem is a separate lift:
relate the correct ordered-factorization target to a tree law, and route
the induced moves through adjacent Hurwitz moves with polynomial
stationary-flow congestion. Neither that comparison nor mixing in the
discarded order information follows from this graph theorem.

Dependencies: (3) is the checked literature theorem; Cayley's count is
the classical Pruefer bijection, only needed for the stated TV bound.
The slide counting, stationarity, path reconstruction, congestion,
variance comparisons and boundary analysis are proved above. No
Hurwitz transitivity or unproved graph-expansion premise is used.

## 7. Paragraph for mathematical review

On labeled trees with N>=3 vertices, consider the half-lazy walk which
chooses an incident edge pair uniformly and then slides either edge
across the other with equal probability. Its stationary measure is
proportional to the number of incident edge pairs, and its spectral gap
is at least 2/[(N-1)^2(N-2)^2]. The same bound holds after Metropolis
correction to uniform labeled trees, or if all edge pairs are proposed
and disjoint pairs rejected. To prove this, compare with the uniform
spanning-tree down-up chain, whose gap is at least 1/(N-1). A down-up
exchange is implemented by sliding the bridge between its unchanged
two forest components, first at one endpoint and then at the other.
The simulation takes at most N-2 steps. Each physical slide determines
the unchanged forest uniquely, giving comparison congestion at most
binom(N-1,2)(N-2). Variance comparison transfers the resulting bound
to the incident-pair stationary law. This graph result leaves the
ordered adjacent Hurwitz mixing problem open.
