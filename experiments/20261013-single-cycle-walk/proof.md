# Minimal factorizations of a single full cycle

Status: **proved** structural lemmas and coded benchmark below;
**unresolved** polynomial mixing of the adjacent Hurwitz/square-refresh walk.
Arguments and finite checks are by one author, without independent review.

## 1. Target, regime and actual local kernel

Use labels {0,...,N-1}, c=(0 1 ... N-1), and the uniform law on

    F_N = {(t_1,...,t_(N-1)): t_i a transposition, t_1...t_(N-1)=c}.

Products act rightmost first. This is a fixed endpoint law, not identity.
For N>=3 write d=N-2, the number of adjacent slots. Let H choose a slot
uniformly and apply one of the inverse moves, each with probability 1/2:

    (a,b) -> (b,bab),             (a,b) -> (aba,a).

Let R choose a uniform slot and, on an equal pair, refresh it to (s,s), s
uniform over all binom(N,2) transpositions; on unequal pairs R holds. The
kernel matching the preceding conversation is K=I/2+H/4+R/4. There are no
circular word windows. All three branches preserve the full-cycle endpoint.

Every support graph is connected: the product preserves every component,
whereas c is transitive. There are N-1 factors, so connectedness forces the
support to be a tree with N-1 distinct edges. In particular no equal pair
occurs anywhere. Hence, on this target,

    R=I,                     K=(3/4)I+(1/4)H.

The uniform law is reversible because signed Hurwitz maps are inverses.
Connectedness of this Hurwitz graph is recorded by Adin--Roichman,
arXiv:1201.4669v3, Remark 2.6 (citing Bessis Proposition 1.6.1). Their
Definition 2.3 calls our two moves L_i and R_i respectively. Definition 2.1
uses the same product t_1...t_(N-1)=c. Uniform signed-generator choice is
important: unweighted simple-graph neighbor choice need not be uniform.

Boundary cases: N=1 has the empty word; N=2 has the unique word (01), and
we define K=I. For an N-cycle and arbitrary length m, feasibility requires
m=N-1+2g, g>=0; appending g doubled transpositions shows sufficiency.
Thus parity is m congruent to N-1, not necessarily even. Extra-pair regimes
are not resolved by the minimal-length argument.

## 2. Exact local heat-bath comparison

Let Q select a uniform slot and uniformly resample its ordered two-factor
same-product fiber, with probability 1/2; with probability 1/2 it holds.
There are only two cases on F_N:

- Disjoint factors: two ordered factorizations of their product. H swaps
  them with probability 1, so K's swap probability is 1/(4d), equal to Q's.
- Overlapping distinct factors: three ordered factorizations of the
  three-cycle product. Each alternative gets 1/(8d) under K and 1/(6d)
  under Q; the ratio is 3/4.

Consequently, for every function f,

    (3/4) E_Q(f,f) <= E_K(f,f) <= E_Q(f,f),

and the corresponding gaps satisfy the same comparison. This is a
self-contained reduction, not an inverse-polynomial bound for either chain.

Writing p_i=t_1...t_i, a two-factor update changes only p_i. The prefixes
form a maximal chain in the absolute-order interval [e,c], the noncrossing
partition lattice. To verify membership directly, reflection lengths of
p_i and p_i^{-1}c are at most i and N-1-i; their sum is at least N-1 by
the triangle inequality, so both bounds are equalities. Conversely a
maximal chain recovers its transpositions by successive quotients.
This is the model identified in Adin--Roichman, Definitions 2.1--2.3 and
Observation 2.5. Their diameter/radius statements do not give a mixing bound.

## 3. An explicit tree bijection

The ordinary operation of forgetting factor order is not a bijection. For
the cycle (1 2 3 4), both

    ((13),(12),(34))       and       ((13),(34),(12))

have the same product and the same support tree. In particular uniform
factorizations cannot be identified with uniform support trees by forgetting
order. The following different relabeling is a genuine bijection.

### Encode

Given w in F_N, root its support tree at permutation label 0. Assign the
root the new label 0. For each nonroot vertex v, let i be the position of
the edge connecting v to its parent, and assign v the new label i, where
1<=i<=N-1. Relabel the whole tree in this way. The result is an ordinary
labeled tree S on {0,...,N-1}, rooted at 0. Every time index is used once.

### Decode

Given any labeled tree S rooted at 0, write

    e_i=(parent_S(i),i),       i=1,...,N-1,
    h=e_1...e_(N-1).

The permutation h is a full cycle. Indeed, in any ordering of the distinct
edges of a tree, each successive edge joins different components of the
previous forest; inductively each such component supports one cycle of the
partial product, and the next transposition merges two cycles.

There is a unique relabeling lambda with lambda(0)=0 and

    lambda(h^j(0))=c^j(0)     for j=0,...,N-1.

Output t_i=lambda e_i lambda^{-1}. Their product is c. Encoding this
output recovers S, since child lambda(i) has incoming edge at time i.
Conversely, encoding an input w by a relabeling rho gives h=rho c rho^{-1}
with rho(0)=0. The decoder's lambda is then rho^{-1}, so it recovers w.
This proves both inverse identities, without assuming an arbitrary tree
bijection preserves Hurwitz moves.

Composing with the classical Prüfer bijection gives

    F_N <-> {0,...,N-1}^{N-2},

and |F_N|=N^(N-2) for N>=2. The bijection and its inverse can be implemented
in O(N^2) elementary operations by simple array algorithms. The Prüfer
bijection is used with its usual repeated-smallest-leaf convention; its
inverse repeatedly joins the smallest absent leaf to the next code entry.

## 4. A proved fast walk on this same target, with different moves

For N>=3, express w by its Prüfer code. With probability 1/2 hold;
otherwise choose a uniform one of the d=N-2 code coordinates, resample it
uniformly in {0,...,N-1}, and decode. Call this chain C, to distinguish it
from the requested local chain K.

It is uniform-reversible and irreducible. In code coordinates it is a
random-scan product heat bath, so

    gap(C)=1/[2(N-2)],
    max_w TV(C^t(w,.),uniform) <= (N-2) exp(-t/[2(N-2)]).

Thus

    t_mix,C(epsilon) <= ceil(2(N-2) log((N-2)/epsilon)).

This follows by coupling the refreshed coordinates; once all coordinates
have refreshed the coupled codes agree. Each materialized word update
costs O(N^2) using the simple decoder. Alternatively all code coordinates
can be sampled independently once and decoded, giving an exact direct
sampler. That sampler regime is already covered in the repository's
S-MINIMAL record; it is not a newly discovered sampling frontier.

The benchmark is not an implementation of one local Hurwitz move. The
checks retain a concrete code-coordinate change whose decoded words differ
in more than two positions and are not K-neighbors. Even a polynomial-length
Hurwitz simulation would still require a congestion proof.

## 5. First unproved step for the requested walk

**Unresolved comparison lemma.** For each nontrivial code-refresh transition
w->w', route its stationary flow pi(w)C(w,w') along legal adjacent Hurwitz
paths, possibly randomly, such that the maximum length-weighted directed
edge congestion is bounded by poly(N), with K's actual edge capacities.

Combined with Section 4, this lemma would prove an inverse-polynomial gap
for K. Section 2 gives an equivalent route: prove a polynomial gap for the
single-rank heat bath on uniform maximal chains of NC(N). Neither route is
proved here. No claim that all published work lacks such a theorem is made;
the targeted sources checked here did not supply one.

The support-tree argument, exact local comparison, and explicit codec are
proved here. Prüfer encoding is the standard tree bijection. Minimal
Hurwitz connectivity is a literature input with the above exact source and
convention translation, not something certified by our finite checks.
No connected-identity classification assumption is used to claim a gap.

## 6. Literature scope

- Ron M. Adin and Yuval Roichman, *On maximal chains in the non-crossing
  partition lattice*, arXiv:1201.4669v3 (2013), Definitions 2.1--2.3,
  Observation 2.5, Remark 2.6. Primary text checked for the model and moves:
  https://arxiv.org/pdf/1201.4669 . This provides structural context, not
  the missing spectral comparison.
- Joel Brewster Lewis, *The Hurwitz action in complex reflection groups*,
  FPSAC 2021, Theorem 2.2 quotes Kluitmann's transitivity theorem for
  fixed-length generating transposition factorizations. The original
  Kluitmann source was not re-audited here, so no new all-length theorem is
  promoted from that quotation. https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2021/19Lewis.pdf .
- The fixed-genus generation/scaling results of Féray--Louf--Thévenin are
  different algorithms, not a mixing bound for K. They are not used as a
  proof dependency here.
