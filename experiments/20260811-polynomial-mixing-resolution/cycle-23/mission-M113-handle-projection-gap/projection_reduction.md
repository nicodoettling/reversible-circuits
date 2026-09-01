# M113 exact handle-cell projection reduction

Date: 2026-08-12 UTC.

## 1. Target and convention

For d at least 2, let X_d be the connected-support transposition words of
length 2d evaluating to the identity, and let pi_d be uniform on X_d.
Permutations compose as (pq)(x)=p(q(x)), and tuple factors multiply
left-to-right.  Put D=2d-1.  The base kernel and M97 lift are

    P_d=I/2+[1/(4D)] sum_i (R_i+R_i^{-1}),
    tilde_pi(w,j)=1/(|X_d| ell(w)),
    L((w,j),(w',j'))=P_d(w,w')/ell(w').

Here J(w) is the set of central cuts and ell(w)=|J(w)|.  The cell key is
kappa=(j,p,Q_L,Q_R), exactly as in M104.  This note analyzes the exact
stationary-flow projection bar L.  It does not prove a polynomial gap for
bar L, gamma_1, or the full heat-bath chain.

## 2. Exact projected stationary law and cut-refresh flow

For a key kappa, write w incident to kappa if the cut at the j recorded in
kappa has that key, and define

    S_kappa = sum_{w incident to kappa} 1/ell(w).

PROVED.  The projected stationary law is

    bar_pi(kappa)=S_kappa/|X_d|.                         (2.1)

Isolate only the explicit holding I/2 in P_d.  It keeps w fixed and refreshes
the new cut uniformly in J(w).  Doubling this half-kernel gives a Markov
kernel G_d on keys with

    G_d(kappa,lambda)
      = S_kappa^{-1}
        sum_{w incident to both kappa and lambda} ell(w)^{-2},       (2.2)
    Q_G(kappa,lambda)
      = |X_d|^{-1}
        sum_{w incident to both kappa and lambda} ell(w)^{-2}.       (2.3)

Rows sum to one and Q_G is symmetric.  Equivalently, under

    Pr(W=w,K=kappa(w,j))=1/(|X_d|ell(w)),                (2.4)

W is uniform on X_d, K conditional on W is a uniform central cut, and G_d is
the two-block Gibbs update K to W to K'.  All signed physical Hurwitz
proposals add nonnegative Dirichlet flow, so

    beta(d)=gap(bar L) >= gap(G_d)/2.                    (2.5)

The compression inequality beta(d)>=gamma_1(d) is true but circular for the
M104 program and is not used.

## 3. Exact key space

Let Cyc(p) be the cycle partition of p.  A tuple
(j,p,Q_L,Q_R) is realizable if and only if:

1. Q_L and Q_R coarsen Cyc(p);
2. the bipartite multigraph with vertices Q_L union Q_R and one edge for
   every p-cycle is connected and unicyclic;
3. j=d+|Q_R|-|Q_L|.

PROVED.  Necessity is M97's accepted incidence theorem and the two side
genus equations.  Conversely, connected-unicyclic gives
c(p)=|Q_L|+|Q_R|.  On any block B, a connected factorization of p restricted
to B of length |B|+c(p_B)-2 is obtained by factoring each permutation cycle
minimally and appending adjacent squares along a tree joining the cycles.
Interleave the block words on each side.  The two lengths are

    d+c(p)-2|Q_L|=d+|Q_R|-|Q_L|=j,
    d+c(p)-2|Q_R|=2d-j.

The incidence graph makes the combined support connected, proving
sufficiency.  This also audits zero-cell endpoints: only keys satisfying the
three displayed conditions occur.

## 4. Adjacent-cut chain and exact comparison

Let kappa=(j,p,Q_L,Q_R) and
lambda=(j+1,p',Q'_L,Q'_R).  If join(Q,t) means the support partition after
adjoining the edge t, then the two cells share a word exactly when

    t=p^{-1}p' is a transposition,
    Q'_L=join(Q_L,t),
    Q_R=join(Q'_R,t).                                   (4.1)

PROVED.  In this case every common word is uniquely u,t,v', giving

    C_kappa intersect C_lambda = U_kappa x {t} x V_lambda,
    |C_kappa intersect C_lambda|=|U_kappa||V_lambda|.    (4.2)

Indeed eval(t v')=t p'^{-1}=p^{-1}; the support joins are exactly (4.1).
The converse follows by inspecting the factor that crosses the cut.

There are exactly two local incidence forms.  If t joins two p-cycles in
distinct Q_L blocks, then p'=pt joins those cycles, Q'_L merges the blocks,
and Q'_R=Q_R.  If t cuts a p-cycle, Q'_L=Q_L, and Q'_R splits the old right
block so that joining it by t recovers Q_R.  Thus the move is a local left
coagulation or right fragmentation, with reversal exchanging the roles.

Put

    Z_inc=sum_kappa |C_kappa|=sum_w ell(w),
    rho(kappa)=|C_kappa|/Z_inc.

Define A_d through its off-diagonal stationary flows

    Q_A(kappa,lambda)
      =|C_kappa intersect C_lambda|/(2Z_inc)             (4.3)

for adjacent compatible keys, holding all unused row mass.  Equivalently,
sample w uniformly in C_kappa, choose left or right with probability 1/2,
and shift the central cut one place when that adjacent cut exists.  A word
has at most two such shifts, so A_d is a valid rho-reversible chain.

Since 1<=ell(w)<=D and |X_d|<=Z_inc<=D|X_d|,

    D^{-1} <= bar_pi(kappa)/rho(kappa) <= D,             (4.4)
    Q_G(kappa,lambda) >= (2/D^2)Q_A(kappa,lambda).       (4.5)

The upper side of (4.4) gives
Var_{bar_pi}(f)<=D Var_rho(f).  Therefore

    gap(G_d) >= (2/D^3)gap(A_d),
    beta(d) >= gap(A_d)/D^3.                            (4.6)

This D^{-3} comparison is the rigorous constant.  A preliminary D^{-1}
constant would use the measure comparison in the wrong direction.

## 5. Exact cell weights

The convention-checked genus-zero simple-Hurwitz formula used in the project
gives, for a block B containing c_B cycles of p and
k_B=|B|+c_B-2,

    |F(B,p_B,k_B)|
      =k_B! |B|^{c_B-3}
       product_{p-cycle a in B} |a|^{|a|}/(|a|-1)!.     (5.1)

The side interleavings cancel all k_B! factors.  Hence

    |C_kappa|
      =j!(2d-j)!
       product_{B in Q_L union Q_R}|B|^{c_B-3}
       product_{p-cycle a}
         [|a|^{|a|}/(|a|-1)!]^2.                       (5.2)

The last product is independent of the incidence grouping.  Equations
(4.2), (4.3), and (5.2) remove every hidden-word count from A_d.
The exact d<=4 enumeration found no failure of (4.2) or (5.2).

## 6. Qualitative connectivity

PROVED.  The adjacent key graph of A_d is connected for every d>=2.

If p has a nontrivial cycle, choose x on it and
t=(x,p^{-1}(x)).  Then p'=pt splits off the singleton cycle {x}.  Keep Q_L
fixed and split the Q_R block containing that cycle into {x} and its
complement.  In the incidence graph one old cycle edge is replaced by a
residual edge and a singleton leaf.  Connectedness and the unique cycle are
preserved, and (4.1) holds.  Repeat until p=id.

For p=id, |Q_L|+|Q_R|=d.  If |Q_L|>1, connectedness gives a Q_R block
containing labels x,y in distinct Q_L blocks.  Moving t=(x,y) joins the two
cycles and merges those left blocks; the incidence graph contracts the
corresponding two-edge path and remains connected-unicyclic.  A singleton
split then restores p=id, decreases |Q_L| by one, and increases |Q_R| by
one.  Iteration reaches an extreme key

    kappa_e=(2d-2,id,{[d]},
             {{the two endpoints of e}, all other singletons}).    (6.1)

For d>=3, kappa_{x,y} and kappa_{y,z} share the intermediate key with
p=(x,z), one left block, a right block {x,y,z}, and all other right blocks
singleton.  Since the graph of two-subsets under one-label replacement is
connected, all extreme keys communicate.  For d=2 there is exactly one key.

This is a reachability proof only.  The extreme family is not used as a
canonical-path hub, and no congestion claim follows.

## 7. Fixed-p Higgs-lift skeleton and a decisive SLC obstruction

For c=c(p)>=2 cycle atoms, take red and blue copies of the edges of K_c.
Let M be the direct sum of the red and blue graphic matroids, and N the
graphic matroid of the doubled multigraph after colors are forgotten.  Every
N-flat consists of all colored edges internal to blocks of a vertex
partition, hence is an M-flat; N is a quotient of M.  The first Higgs lift
has

    r_H(X)=min(r_M(X),r_N(X)+1).                         (7.1)

PROVED.  Its rank-c bases are exactly the size-c colored edge sets whose two
color classes are forests and whose uncolored union is connected.
Contracting the red and blue forest components gives exactly a
connected-unicyclic incidence graph.  Conversely, choosing a spanning tree
inside every Q_L and Q_R block lifts every incidence key to such a basis.

This skeleton does not by itself implement A_d: a nontrivial A_d move joins
or cuts p-cycle atoms, hence changes the ground set.  More strongly, the
natural exact Hurwitz weighting fails the standard Lorentzian/SLC route
already on the fixed p=id slice at d=4.

For p=id, let r be the number of red forest edges.  A basis witness B for a
key has exact coefficient

    w(B)=(2r)!(2d-2r)!
         / product_{C in Q_L union Q_R}|C|.             (7.2)

This follows because the number of tree witnesses for the key is
product_C |C|^{|C|-2}, while (5.2) is
(2r)!(2d-2r)! product_C |C|^{|C|-3}.

REFUTED, named comparison.  Let F_4 be the multiaffine degree-four basis
polynomial with coefficients (7.2).  After differentiating in red edges
01 and 02, the Hessian principal submatrix on variables
red03, blue01, blue02, blue13 is exactly

    [  0 180 180 180 ]
    [180   0   0  64 ]
    [180   0   0  48 ]
    [180  64  48   0 ],

with determinant 8,294,400>0.  It is nonsingular with trace zero, so its
inertia is (2 positive, 2 negative).  By interlacing, the full derivative
Hessian has at least two positive eigenvalues.  This violates the necessary
quadratic-derivative signature for a Lorentzian homogeneous polynomial.
Even removing the factorial tilt and retaining only reciprocal component
sizes gives the same sign obstruction, with determinant 1/82944.

Thus the accepted Lorentzian matroid down-up theorem cannot be applied
directly to the natural exact Hurwitz-weighted Higgs basis polynomial.
This does not refute a tailored comparison, another augmentation, or a
polynomial gap for A_d.

## 8. Sharp split-family flow audit

The cell ratios can make a single valid edge exponentially small, so a
pointwise minimum-edge comparison is impossible.  This does not automatically
create a bottleneck because the family multiplicity cancels the loss.

For even d>=6 define

    sigma_d=(3,(01),
             {{0,1,2},{3},...,{d-1}},
             {[d]}).

For A containing 0 but not 1, let lambda_A have j=4, p'=id, the same Q_L,
and Q'_R={A,A^c}.  These are valid adjacent keys: the seam transposition
(01) cuts the nontrivial p-cycle and joins the two new right blocks back to
[d].  If |A|=a and b=d-a, (4.2) and (5.1) give

    A_d(sigma_d,lambda_A)
      = a^{a-3}b^{b-3}/[8(2d-3)d^{d-4}].               (8.1)

Indeed the source suffix count is
4(2d-3)!d^{d-4}, while the target suffix count is
(2d-4)!a^{a-3}b^{b-3}; the common prefix cancels.
At a=b=d/2,

    A_d(sigma_d,lambda_A)
      =2^{-d+3}/[(2d-3)d^2].                            (8.2)

There are binomial(d-2,d/2-1) such targets.  Since the central binomial
coefficient is at least 2^{d-2}/(d-1), their aggregate transition
probability is at least

    2/[(d-1)(2d-3)d^2].                                 (8.3)

PROVED.  Equations (8.1)--(8.3) are an infinite-family obstruction to
pointwise edge lower bounds and, simultaneously, a polynomial aggregate
lower bound for this particular source.  They neither prove nor refute a
uniform aggregate bound over every key.  Exact enumeration gives no zero
singleton-split-or-reverse rate for d=3,4 (minimum 1/4 and 1/3,
respectively); d=2 is the one-state exception.  This finite fact is only a
falsification check.

## 9. First open lemma

LOCAL UNICYCLE INCIDENCE GAP.  For d>=3, the chain A_d on realizable
connected-unicyclic keys, with stationary law (5.2) normalized and local
coagulation/fragmentation flows (4.2)--(4.3), satisfies

    gap(A_d) >= d^{-O(1)}.

By (4.6), this lemma alone implies beta(d)>=d^{-O(1)} for the exact M104
handle-cell projection.  A useful strictly weaker first step would prove
that, from every key, the total A_d probability of all singleton-cycle split
moves and their reverses is at least d^{-O(1)}.  That aggregate statement is
unresolved: d<=4 and the family (8.1) survive it, but neither constitutes an
asymptotic proof.

