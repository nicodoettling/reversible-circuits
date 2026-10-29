# A tree-and-extra-edges refresh at fixed excess

Author status: **proved**, with the explicit count and codec inputs below;
same-author checking, pending independent review. This is a **different
kernel** from the edge-slide pair lift. It supplies a fast completed-macro
hybrid, not a gap bound for the original Hurwitz/heat-bath walk.

## 1. Target, parameters and proposal

Fix N>=2, c=(0 1 ... N-1), h>=0 and m=N-1+2h. Products act rightmost
first. Write Omega_h for all ordered length-m transposition words with
product c, F_h=|Omega_h|, M=binom(N,2). The target pi_h is uniform on
Omega_h. Every such word has connected support. Edge occurrences retain
their circuit positions; parallel edges count separately.

Let tau(w) be the number of subsets of N-1 edge occurrences forming a
spanning tree. Thus 1<=tau(w)<=binom(m,2h). One attempt Q_h, from any
current word x, is:

1. Draw u uniformly from Omega_0. The rooted time-edge codec in the
   [minimal-cycle proof](../20261013-single-cycle-walk/proof.md), Section 3,
   does this from a uniform length-(N-2) Pruefer code. This is not the
   assertion that ordinary support forgetting is a bijection.
2. Choose a uniform 2h-subset I of the m positions, and independently put
   uniform transpositions in those positions. Fill the other positions
   with u, preserving its order. Call the resulting word v and its product q.
3. If q is not an N-cycle, retain x. Otherwise let lambda be the unique
   permutation fixing 0 with lambda q lambda^{-1}=c. Explicitly,
   lambda(q^j(0))=j. Conjugate every gate of v by lambda to obtain w.
4. With probability 1/tau(w), output w; otherwise retain x.

There are exactly

    D_h = N^(N-2) binom(m,2h) M^(2h)

equiprobable tuples in steps 1-2. The algorithm needs neither F_h nor
its asymptotics. Uniform finite draws and the last Bernoulli decision use
exact independent fair bits. There are no wraparound windows. Each step
above is one global proposal attempt, not one primitive Hurwitz move.

## 2. The preimage lemma

**Lemma (proved).** Every w in Omega_h has exactly tau(w) proposal tuples
that pass step 3 and map to w, before the final rejection correction.

Proof. Given w, select any spanning-tree subset J of its edge occurrences;
let I be its complement. The ordered subword w_J has full-cycle product a.
Indeed, when edges of a tree are added in any order, each next edge joins
two different components of the previous forest. Their product's cycles
are those components, by induction, so the final product is a full cycle.

Let rho fix 0 and conjugate a to c. Conjugate the WHOLE word w by rho.
Its J-subword is a unique u in Omega_0; its I-entries specify the inserted
transpositions. Its whole product is rho c rho^{-1}, so step 3 uses
lambda=rho^{-1} and recovers w.

Conversely, every proposal tuple producing w designates the positions J
occupied by its minimal word. After conjugation these form a spanning
tree. Uniqueness of the root-fixing conjugator shows that the tuple is the
one just constructed. Different J give different position subsets, even
when gates repeat. This proves a bijection, with no extra N or N! factor.

It follows that the unconditional probability of accepting any specified
w in one attempt is tau(w)/D_h times 1/tau(w), namely 1/D_h. Consequently

    Q_h = (1-p_h) I + p_h Pi_h,       p_h = F_h / D_h,                 (1)

where Pi_h refreshes exactly from pi_h. This proves stationarity,
reversibility and uniformity of the accepted word, independently of the
current state. The support-graph law is the pushforward of pi_h, weighted
by the number of compatible ordered words; it is not uniform over graphs.

## 3. Mixing theorem and explicit easy cases

Let L be any pi_h-stationary kernel, for example the half-lazy adjacent
Hurwitz/square kernel K_A, or the original hybrid P defined in proof.md.
Set

    P_tree = (L+Q_h)/2.

**Theorem (proved).** From every starting state, for 0<epsilon<1,

    ||P_tree^t(x,.)-pi_h||_TV <= (1-p_h/2)^t <= exp(-p_h t/2),
    t_mix(epsilon) <= ceil((2/p_h) log(1/epsilon)).                  (2)

If L is reversible, its Poincare gap is at least p_h/2. The first bound
follows by coupling at the first uniform-refresh event; stationarity of
L preserves equality thereafter. Equivalently Pi_h commutes with L and
the uniform component has weight at least 1-(1-p_h/2)^t. If L is half-lazy,
P_tree has holding probability at least 3/4-p_h/2; no additional laziness
is implicit. Singleton targets mix in zero steps regardless of this bound.

The fixed-cycle count formula, normalized in Section 5, is

    F_h = m! N^(m-1)/(N-1)! [z^(2h)] (sinh(z/2)/(z/2))^(N-1).

Since F_0=N^(N-2), (1) simplifies to

    p_h = (2h)! (2/(N-1))^(2h)
          [z^(2h)] (sinh(z/2)/(z/2))^(N-1).                        (3)

In particular:

| Length | Exact p_h | Mixing bound for P_tree |
| --- | --- | --- |
| N-1 | 1 | ceil(2 log(1/epsilon)) |
| N+1 | 1/[3(N-1)] | ceil(6(N-1) log(1/epsilon)) |
| N+3 | (5N-7)/[15(N-1)^3] | ceil(30(N-1)^3/(5N-7) log(1/epsilon)) |

The latter two use coefficients (N-1)/24 and
(N-1)(5N-7)/5760. Thus the macro bounds are respectively
O(N log(1/epsilon)) and O(N^2 log(1/epsilon)), with explicit N as input.

More generally, for fixed h>=1 and N-1>=2h, positivity of coefficients
gives, by selecting h distinct quadratic terms,

    p_h >= (2h)! (2/(N-1))^(2h) binom(N-1,h)/24^h
        >= (2h)! / [12^h h! (N-1)^h].                              (4)

Hence t_mix=O_h(N^h log(1/epsilon)) for every fixed h. This is not a
joint polynomial bound with a fixed exponent when h is part of the input.

There is also a count-formula-free bound for every N>=2,h>=0. Appending
h arbitrarily chosen squares to a minimal word is injective, so
F_h>=F_0 M^h and

    p_h >= 1/[binom(m,2h) M^h].                                   (5)

This alone proves N^{O(h)} macro mixing for fixed excess, including small
N excluded by (4). At N=2 the word is unique and p_h=1/(2h+1), consistently
with (3). At N=1 only the empty word exists. A full-cycle fiber is empty
unless m>=N-1 and m=N-1 modulo 2. Thus odd m is allowed when N is even;
m=0 is only the N=1 exception, and m=2 permits the minimal N=3 case.

## 4. Computation and relation to the authorized moves

One can compute tau by enumerating the binom(m,2h) deleted position sets
and testing whether the retained N-1 edges form a tree, in O(m+N) time
per subset. At fixed h this is polynomial. At h=1 it gives an O(N^3)
elementary-operation bound per attempt, including elementary tree decoding
and permutation operations. All integers have polynomial bit length;
bit costs and exact random-bit costs are polynomial too. No claim of
efficiency in log_2 N wires is made.

If an accepted jump must be enacted on the existing circuit, the vertex
sweep and square transport of the [nonlocal-lift proof](../20261014-111117-nonlocal-graph-lift/proof.md),
Section 3, connect its old and new words in at most 2(N+3)m^2 adjacent
Hurwitz/square moves, preserving length and endpoint at every stage.
For h=1 the crude total cost to obtain an epsilon-close output is
O(N^4 log(1/epsilon)) elementary operations, measured at completed attempt
boundaries; an exact uniform output needs expected 3(N-1) proposals.

The path may go through a normal form. This is permitted for implementing
one sampled macro, but proves no polynomial congestion for local MCMC.
The intermediate distributions need not be uniform. In particular Q_h
regenerates an entire underlying tree, whereas a step of K_G updates one
selected pair with middle conjugation. Equation (2) proves neither the
gap of K_G nor the original conjectured edge-slide-only hybrid gap.

## 5. Dependencies, source normalization and scope

- **Proved input, internal:** rooted time-edge codec and Pruefer bijection
  in the minimal-cycle proof, Section 3. Ordinary support forgetting is
  not substituted for this codec.
- **Proved here:** preimage bijection, rejection correction, (1)-(2),
  elementary lower bound (5), and the coefficient calculations in (3)-(4).
- **Literature theorem, hypotheses checked:** Goulden, Jackson and Vakil,
  *Towards the geometry of double Hurwitz numbers*, January 19, 2005,
  [Proposition 1.1 and Theorem 3.1, equation (21)](https://math.stanford.edu/~vakil/files/Djan2005.pdf).
  Set d=N, alpha=(N), beta=(1^N), genus=h, r=m. Their H counts all
  full-cycle endpoints, so H=(N-1)! F_h: the prefactor in Proposition
  1.1 is |Aut alpha||Aut beta|/N!=1. Transitivity is automatic. Reverse
  their ordered factors to match the rightmost-first convention. Their
  c_1=N-1 and c_i=0 for i>1 give the displayed F_h formula. The result
  is a counting theorem, not their geometric conjecture. This source
  specializes Shapiro-Shapiro-Vainshtein Theorem 6; no unchecked transfer
  from that older source is needed.
- **Proved input, internal, only for implementation paths:** all-endpoint
  connectivity and constructive diameter in the nonlocal-lift proof.
- **Unresolved:** polynomial gap for the original P at growing N,h=1.
  An efficient exact sampler or short implementation paths do not fill
  that stationary-flow obligation.

The repository already has an exact genus-one sampler in
`experiments/20260907-genus-one-sampler/proof.md`; this construction is a
different transparent proposal/correction argument, not a claim that
efficient genus-one sampling was previously unavailable. Related
fixed-genus insertion/relabeling constructions appear in
[Feray, Louf and Thevenin, arXiv:2105.03284](https://arxiv.org/pdf/2105.03284),
Section 1.2 and Remark 1.3. No novelty claim is made, and their asymptotic
sampling statement is not used as a local mixing theorem here.

## 6. Falsification and reproducibility

`tree_jump_check.py` exhausts every proposal tuple for (N,h)=(2,1),(3,1),
(4,1),(5,1),(3,2),(4,2): 922830 tuples in total. It independently enumerates
the endpoint fibers by meet-in-the-middle, checks coverage, and checks
the preimage count against spanning-tree enumeration for EVERY output.
The exact acceptance probabilities are 1/3,1/6,1/9,1/12,1/15,13/405.
These are finite verifications, not the proof of the general bijection.
No empirical mixing inference is used. See `tree_jump_results.json` for
commit, command, Python version and imported-source hashes.
