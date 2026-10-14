# A reversible nonlocal lift of graph moves

Author status: **proved** statements below; not independently reviewed.
**Unresolved:** an inverse-polynomial gap for the resulting chain in general.
No classification theorem or empirical spectral extrapolation is used.
Section 8 proves polynomial mixing for a DIFFERENT, decoded-tree macro
kernel on minimal full-cycle words, using the earlier tree-slide theorem.

## 1. Target and conventions

Let T_N be all M=binom(N,2) transpositions on a fixed vertex set [N]. Fix
g in S_N and a length m. The target is uniform on

    Omega_g(N,m) = {w in T_N^m : t_1 ... t_m = g}.

Products act rightmost first. Write ell(g)=N-c(g), counting fixed-point
cycles. For N>=2, this fiber is nonempty exactly when m>=ell(g) and
m=ell(g) modulo 2. Necessity follows because every transposition changes
cycle count by one; cycle decompositions attain ell(g), and appending
transposition squares proves sufficiency. There is no connected-support
constraint. New squares may use any transposition in T_N, including
vertices previously isolated in the support.

At m=0 only g=id is possible; at m=1 each nonempty fiber is a singleton.
N=2 gives a singleton for each feasible endpoint and length. N=1 permits
only the empty word. Empty fibers have no sampling problem. At identity,
odd m is infeasible; arbitrary endpoints have the parity stated above.

For m>=2 define adjacent moves

    H_i^+: (a,b) -> (b,bab),
    H_i^-: (a,b) -> (aba,a).

These are inverses. Let R_i replace (a,a) by (s,s) for s uniform in T_N,
and hold on unequal factors. Define

    K_A = I/2 + H_A/4 + R_A/4,

where H_A chooses a uniform linear adjacent slot and sign, and R_A a
uniform linear adjacent slot. There are no wraparound windows.

## 2. Nonlocal moves and exact kernel

For i<j write the affected subword a B b, where B is an ordered list of
the intermediate gates. Notation q B q^{-1} means conjugate EACH gate of B;
it is not an instruction to insert additional circuit gates.

The two nonlocal Hurwitz moves are

    F_ij^+: a B b -> b (b a B a b) (b a b),
    F_ij^-: a B b -> (a b a) (a b B b a) a.

Thus the two selected edges undergo precisely the usual Hurwitz pair
update, while every intermediate edge is conjugated. The two maps are
inverse bijections. When the selected edges are incident and unequal, the
selected-pair change is an edge slide. On adjacent disjoint edges it is a
commutation. Intermediate conjugations may change other support edges.

The nonlocal square refresh is

    R_ij(s): a B a -> s (s a B a s) s,

with s uniform in T_N; hold when t_i != t_j. Its inverse channel replaces
s by a at the same pair. Crucially, replacing a B a merely by s B s would
usually change the endpoint.

All these maps have literal Hurwitz lifts. Let T_ij move the gate at i
unchanged to j-1 by H_i^-, H_(i+1)^-, ..., H_(j-2)^-. It sends

    a B b -> (a B a) a b.

Apply the ordinary adjacent move at j-1, then undo T_ij. This gives the
formulas above, i.e. T_ij^{-1} H_(j-1)^sign T_ij and
T_ij^{-1} R_(j-1) T_ij. A path uses at most 2(j-i)-1 <= 2m-3
elementary moves, of which at most one is a square refresh. Every
intermediate word computes g and has length m.

Put C=binom(m,2). Define K_G as follows:

- With probability 1/2 hold.
- With probability 1/4 choose one of the C pairs uniformly, then a uniform
  sign, and apply F_ij^sign.
- With probability 1/4 choose one of the C pairs uniformly and s uniformly
  in T_N, and apply R_ij(s), holding on unequal selected factors.

The state-independent pair choice includes disjoint pairs. This is one
precise implementation of graph-selected moves, not a theorem about every
possible way to choose an available edge slide or its Hurwitz lift.

**Proved: uniform reversibility.** Each signed F channel has its inverse
at the same probability. Each square channel a->s has the reverse s->a
at the same probability. Equivalently, each conditional kernel is a
conjugate by a permutation of states of a symmetric adjacent kernel.
Hence K_G is symmetric and half-lazy on Omega_g(N,m).

If instead choosing uniformly among currently incident distinct gate pairs,
let D(w) count those pairs. The F maps preserve incidence of the two
selected factors, so their channelwise Metropolis acceptance is
min(1,D(w)/D(w')). This restores uniform reversibility for that branch.
The analogous correction uses the current number of equal pairs for a
square-only proposal. A zero-count branch holds. Such branches still need
an appropriate commuting branch for the all-endpoint connectivity claim.
Merely resampling pairs until an applicable move is found changes the kernel.

## 3. Constructive connectivity for every feasible endpoint

**Theorem.** For N>=2, every nonempty Omega_g(N,m) is connected under
adjacent signed Hurwitz moves and arbitrary adjacent square refreshes.
Consequently K_G is irreducible. For m>=2 its underlying graph has diameter
at most D_0=2(N+3)m^2. In particular minimal full-cycle words are connected
using Hurwitz moves alone.

### Vertex sweep

Fix a vertex v, starting with the largest label. Find the first factor
(v,a). Move it right through the word, maintaining a single current
v-incident factor:

1. If the next factor b avoids v, use H^+ to send ((v,a),b) to
   (b,b(v,a)b). The second factor is still incident to v.
2. If the next factor is (v,b) with b!=a, use H^-:

       ((v,a),(v,b)) -> ((a,b),(v,a)).

   This removes one occurrence of v from the prefix.
3. If the next factor is the same (v,a), an adjacent square has been found.

Unless a square is found, this sweep leaves at most one v-factor, at the
end, after at most m-1 moves. The prefix avoids v. Repeat on that prefix
with the next smaller vertex. Sweeping all vertices costs at most Nm.

### Square extraction lemma

If m>ell(g), the sweep must find a square. To see this, suppose the first
sweep ends with one factor (v,a), so g=h(v,a) and h fixes v. Multiplying
h by (v,a) merges its singleton cycle {v} with another cycle. Therefore
ell(g)=ell(h)+1. The prefix still has length strictly greater than ell(h).
If no v-factor occurs, both the word and g simply restrict to fewer
vertices. Induction forces a square. Equivalently, completing all sweeps
without encountering a square produces a reduced factorization, which
cannot have the initial nonminimal length.

### Unique reduced normal form

If m=ell(g), a square cannot appear: deleting it would give a shorter
factorization. If g fixes the largest vertex v, a completed sweep cannot
have a last v-factor, since h(v,a) does not fix v when h fixes v. Otherwise
the last factor is forced to be

    (v,g^{-1}(v)),

because g=h(v,a) with h fixing v. The prefix has the forced product
h=g(v,g^{-1}(v)). Inducting on vertices gives a unique reduced word C(g),
reached in at most Nm Hurwitz moves. This also proves reduced Hurwitz
transitivity directly, for arbitrary endpoints.

### Nonreduced words

Expose a square, then move it to the end via repeated applications of

    (a,a,b) -> (a,b,bab) -> (b,bab,bab).

This uses at most 2m further Hurwitz moves and keeps a square. Refresh the
terminal square to a fixed s_0=(12). Leave it fixed and repeat on the
remaining prefix. When the prefix is reduced, normalize it to C(g).
Every input reaches the SAME word

    C(g) (s_0,s_0) ... (s_0,s_0),

with (m-ell(g))/2 square pairs, in at most (N+3)m^2 elementary moves
for m>=2. Reversing one normalization and composing proves the diameter
bound. K_G includes all adjacent moves with positive probability, so the
same connectivity and diameter bound applies.

This normal form proves connectivity, not polynomial mixing. No assertion
of polynomial congestion through the single normal form is made.

## 4. Quantitative comparison: larger moves do not close the gap problem

Let E_A,E_G be the Dirichlet forms for K_A,K_G under the same uniform law.
For all nontrivial feasible fibers with m>=2,

    (2/m) E_A <= E_G <= A E_A,
    A = 8 M(M+1)m^3.

The same inequalities hold for the spectral gaps. Constants are deliberately
loose. In particular these two chains have inverse-polynomial gaps in N,m
simultaneously; this statement does not prove that either has such a gap.

**Lower bound.** Retain only pairs j=i+1 in K_G. Their mass relative to
the adjacent random scan is (m-1)/C=2/m.

**Upper bound, with explicit congestion accounting.** Route every labeled
macro channel along T_ij, its middle update, then T_ij^{-1}. Each path has
length at most L=2m (using a harmless larger bound). All nonzero local
transition probabilities are at least

    p_A = 1/[8(m-1)M].

Fix a directed local edge z->z'. For Hurwitz channels, specifying the
pair (i,j), sign, and path stage determines the initial state uniquely:
each prefix is a fixed bijective Hurwitz sequence. There are at most 2C L
such specifications, each of macro-channel probability 1/(8C). After
multiplying by the path length, the total stationary flow charge is at
most pi(z)L^2/4.

For refresh channels, specify (i,j), new s, the stage, and the old repeated
factor a. Before the refresh the bijective prefix already recovers the
source; after it, undo the known part of T^{-1}, replace the exposed (s,s)
by the specified (a,a), and undo T. Thus there is at most one source per
specification. There are at most C M^2 L specifications, each of
probability 1/(4CM). Their length-weighted flow charge is at most
pi(z) M L^2/4. Null channels can be omitted.

The total charge divided by local capacity pi(z)p_A is at most

    2(m-1)M(M+1)L^2 <= 8M(M+1)m^3 = A.

Applying Cauchy-Schwarz along each path proves E_G<=A E_A. This argument
uses recoverable path labels, not a normal-form hub. Parallel channels
are routed separately, so coincidences of destinations cause no issue.

Polynomial equivalence of relaxation and mixing follows because the
chains are lazy, reversible, and uniform on the same S-state space with
log S <= m log M. It is polynomial in explicit N,m, not wire count log N.

## 5. An unconditional, but exponential, mixing bound

Write S=|Omega_g(N,m)| and assume S>1. The graph diameter is at most D_0
and each nonzero edge of K_G has probability at least p_G=1/(8CM).
Routing each ordered state pair along a path of length at most D_0,
and using the crude bound of S^2 routes through any directed edge, gives

    gap(K_G) >= p_G/(D_0 S) = 1/(8 C M D_0 S).

For 0<epsilon<1/2, laziness and the standard L2-to-TV inequality then give

    t_mix(epsilon) <= ceil(8 C M D_0 S
                         [0.5 log S + log(1/epsilon)]).

Since S<=M^m, this is an explicit generally exponential bound, not fast
mixing. Its role is to separate proved convergence from the open
inverse-polynomial bound. Singleton fibers mix in zero steps.

**First unproved quantitative lemma.** Find a polynomial p(N,m), uniform
over all feasible endpoints g, such that

    Var_pi(f) <= p(N,m) E_G(f,f).

The comparison proves that this is equivalent up to polynomial losses to
the adjacent Hurwitz/square Poincare problem. A favorable gap on a graph
space alone cannot establish it: the graph marginal, fibers and the lift's
stationary flows must match. Ordinary support forgetting is not generally
a Markov projection.

## 6. Boundaries and falsification

An incident-edge-only walk is not connected for every endpoint. The two
words ((12),(34)) and ((34),(12)) compute the same permutation. Each has
no incident distinct edges and no repeated edge, so both are frozen if
commuting disjoint factors is disallowed. This refutes that narrower
all-endpoint claim; it does not refute the single-full-cycle conjecture.

Also, (12)(23)(12)=(13), whereas (13)(23)(13)=(12). Thus a nonadjacent
double-edge refresh without the middle conjugation is invalid.

check.py exhaustively checks the canonical algorithm on all words for
N=2,3,4 and m<=6, and for N=5,m=4. It checks macro formulas against every
primitive lift, endpoint preservation at every stage, integer detailed
balance and full-fiber connectivity on the listed small kernels. These
are exact finite checks, not independent proof certification.

## 7. Dependencies and limits

The connectivity and comparison proofs in Sections 1--6 are self-contained using
elementary permutation algebra, Cauchy-Schwarz and the finite-state lazy
spectral mixing inequality. No Ben-Itzhak--Teicher, Kluitmann, or other
classification input is required. Existing repository conditional wording
is not silently rewritten; this is a separate new proof for the exact
pair kernel above. The pre-existing {3,4,5} chain is a different kernel.

The graph selected in a move is the CURRENT support multigraph of the word;
the graph is not held fixed. Its stationary law is induced by uniform
circuits and weights each support by its number of realizing words. The
proof does not claim uniform support graphs or a closed Markov chain on
unlabeled graph shapes. Other lifts, such as decoding an independent tree
walk through a bijection, may have different mixing behavior.

## 8. A proved fast implementation for a minimal full cycle

Assume g is one full N-cycle and m=N-1, with N>=3. In this regime the
support is a tree and square refresh never acts. There is a version of
the user's proposal with a proved polynomial bound, if a completed
Hurwitz sequence is counted as one update and global reassignment of
the support's permutation labels is allowed. This is K_T below, not K_G.

Use the shape-preserving bijection Phi from
`../20261013-single-cycle-walk/proof.md`, Section 3. Briefly, root the
support at permutation label 0, keep root label 0, and give each other
vertex the time index of its incoming edge. This encodes a word as an
arbitrary tree S on {0,...,N-1}, with vertex labels now encoding gate
times, not the original permutation symbols.

To decode S, root it at 0 and put e_i=(parent_S(i),i), i=1,...,N-1.
Any ordering of a tree's distinct edges has full-cycle product, since
each edge joins two forest components and merges their product cycles.
Thus h=e_1...e_(N-1) is a full cycle. Define the unique relabeling lambda
by lambda(h^j(0))=g^j(0). Return the word of lambda e_i lambda^{-1}.
Its product is g. Encoding it returns S, and the converse is identical:
the encoding relabeling conjugates g to h, forcing lambda to be its
inverse. This proves the bijection and uniform-law correspondence.

Let U be the half-lazy tree kernel from
`../20261014-tree-slides/proof.md`: otherwise choose a uniform unordered
pair of distinct tree edges, hold on disjoint pairs, and for incident
pairs choose a uniform direction and slide. Define

    K_T(w,w') = U(Phi(w),Phi(w')).

An implementable update is:

1. Encode w as S=Phi(w).
2. Propose one U edge-slide step to S'.
3. Decode w'=Phi^{-1}(S').
4. If actual gate-by-gate execution is wanted, use the reduced sweeps of
   Section 3 to take w to C(g), then reverse the sweep taking w' to C(g).
   Observe the circuit only after this whole macro update is complete.

Step 4 takes at most 2N(N-1) adjacent Hurwitz moves; no heat bath is
needed. The intermediate graphs may differ considerably, as authorized.
The unlabeled support of the final circuit is precisely the proposed
tree shape. The final permutation vertex labels may all be reassigned;
this does NOT perform only a single slide in the original vertex labels.
No claim that K_T equals the pair lift K_G is made.

**Theorem (proved from the preceding inputs).** K_T is uniform-reversible
and irreducible, and

    gap(K_T) = gap(U) >= 2/[(N-1)^2 (N-2)^2],

    t_mix,K_T(epsilon) <= ceil(((N-1)^2 (N-2)^2 / 2)
        [((N-2)/2) log N + log(1/epsilon)]).

Indeed the bijection makes the transition matrices identical after a
permutation of their indices. The tree gap is the exact theorem of the
referenced tree-slide proof, and |Omega_g|=N^(N-2) gives the displayed
lazy spectral TV estimate. Thus the bound is
O(N^4 [N log N + log(1/epsilon)]) macro steps, or at most
O(N^6 [N log N + log(1/epsilon)]) executed elementary Hurwitz moves when
the output is taken at a completed macro step. The decoder and sweep
also require only polynomial computation in explicit N.

Counting completed updates is essential: the intermediate Hurwitz states
are not distributed according to K_T and can pass through C(g) repeatedly.
No uniform distribution at every primitive time, no rapid mixing of the
usual random adjacent Hurwitz chain, and no polynomial congestion through
C(g) is asserted. The choice of macro endpoint already has the correct
Markov transition; the path merely realizes that chosen transition.

Dependency: the tree-slide gap comparison invokes Anari--Liu--Oveis
Gharan--Vinzant, arXiv:1811.01816v3, Theorems 1.1 and 5.2 for the
spanning-tree down-up gap. Its kernel/hypothesis translation and slide
congestion are in the referenced proof. Both that proof and the codec
are same-author inputs pending independent review. This is a derived
macro-chain theorem, not an independent certification of those inputs.

Boundary cases N=1,2 are singleton fibers. tree_check.py verifies every
tree-slide transition through N=6, both codec directions, and each full
Hurwitz implementation including its endpoint and length bound.
