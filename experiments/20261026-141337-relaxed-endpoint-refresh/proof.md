# Bounded endpoint error: rigorous progress and the remaining mixing gap

Author status: **proved** for the symbolic statements below, with exact
checks as stated; provisional pending independent review. General rapid
mixing is **unresolved**. No numerical gap is used as an asymptotic bound.

## 1. Target, conventions and kernel

Let N>=2, T be all M=binom(N,2) transpositions, and let products act
rightmost first. Write ell(g)=N-c(g), where fixed points count as cycles.
The main target is uniform on

    A(N,m,k) = {w in T^m : ell(eval(w)) <= k}.

This is a relaxed identity endpoint law, not the uniform exact identity
law and not an orbit law. The declared Markov kernel R holds with
probability 1/2, and otherwise chooses i uniformly in {1,...,m} and s
uniformly in T, replaces t_i by s if the result belongs to A, and rejects
otherwise. For m=0 it holds on the empty word. There is no cyclic seam.
All complexity variables below are N,m and the requested accuracy, not
the number log_2 N of wires.

For m>0 every distinct adjacent state has probability 1/(2mM). Hence
R is symmetric, half-lazy and reversible for the declared uniform law.
This argument does not establish irreducibility. The same stationarity
argument holds for a ball centered at any specified permutation p.
Unless explicitly stated otherwise, the other results below concern p=id.

Odd identity lengths are infeasible for k=0, but odd-length relaxed sets
can be nonempty when k>=1. Since ell(eval(w))=m modulo 2, for even m the
budgets 2j and 2j+1 define the same set. At k=0 or 1 and even m, every
single-coordinate move to a different gate is rejected: the exact states
are isolated for THIS kernel. N=2 has only one word at each length; it
is allowed iff m mod 2 <= k. For m=0 the sole empty word is allowed.
For m=2,k>=2 every word is allowed.

If k is at least the largest feasible endpoint defect, the chain is
independent coordinate refresh. For M>1,m>=1 its gap is 1/(2m), and a
shared-refresh coupling gives TV <= m exp(-t/(2m)). In particular the
even-length k=2 tests in S3 and S4 are unrestricted, not evidence about
a nontrivial endpoint constraint.

## 2. Error metric and single edits

If g moves s>0 labels and has r nontrivial cycles, then ell(g)=s-r, so

    ceil(s/2) <= ell(g) <= s-1.

A k-transposition correction therefore implies at most 2k disagreement
points. This is not a relaxation allowing arbitrary disagreement.

Replacing one gate changes L a B to L b B. Its relative endpoint change
is B^-1 a b B, a product of at most two transpositions. Thus endpoint
defect changes by at most two. In particular every one-gate proposal
from an exact identity state is allowed when k>=2. The error can
accumulate along subsequent accepted moves; this observation alone does
not prove mixing.

## 3. All exact states communicate with a two-transposition budget

**Proved.** For every N>=2 and even m, all exact identity words are in
one component of A(N,m,2). For m>=2, they have pairwise path length at
most 4(N+3)m^2 in the relaxed graph. More generally all words with a
fixed feasible endpoint p communicate inside the radius-two ball about p.

Here is a self-contained qualitative argument. Adjacent signed Hurwitz
moves (a,b)->(b,bab) and (a,b)->(aba,a), together with square refreshes
(a,a)->(s,s), connect every fixed-endpoint fiber. One constructive proof
is the vertex sweep, also recorded in the October 14 nonlocal-lift proof:

* Move a factor (v,a) right. Across a gate b avoiding v use the positive
  Hurwitz move; across a different (v,b) use the negative move to produce
  ((a,b),(v,a)). Equal consecutive v-gates expose a square.
* If the word is longer than ell(p), some sweep must expose a square.
  Otherwise each terminal v-factor increases the endpoint defect by one,
  and induction would make the entire word reduced, a contradiction.
* Move the exposed square to the end using
  (a,a,b)->(a,b,bab)->(b,bab,bab), then refresh it to a fixed gate s0.
  Repeat until a reduced prefix remains.
* A reduced prefix has a unique sweep normal form: its terminal factor
  for a nonfixed largest vertex v is (v,p^-1(v)); if p fixes v, no
  terminal v-factor is present. Continue on the smaller prefix.

Each word reaches C(p)(s0,s0)...(s0,s0) in at most (N+3)m^2 pair moves.
Implement each pair move by first replacing its first gate, then its
second. Only the intermediate state can have a different endpoint; its
distance from p is at most two. This proves the relaxed path claim.

This normal form is used ONLY for connectivity. No polynomial congestion
through it is claimed. The argument needs no unverified Hurwitz
classification theorem. It agrees with the later constructive proof in
experiments/20261014-111117-nonlocal-graph-lift/proof.md, Section 3,
rather than relying on the older conditional classification language.

There is also an interior extension. If even m and ell(eval(w))=d<=k-2,
the same normalization can be simulated within A(N,m,k), since an
intermediate has defect at most d+2. In the resulting reduced prefix,
replace the second gate of its first pair by the first. The pair cancels,
and the remaining reduced prefix has defect d-2. Repetition reaches an
identity word. Therefore only the outermost attainable shell can obstruct
connectivity of the whole relaxed space.

## 4. Strict descent fails, but finite full connectivity survives

**Refuted:** every word with defect two has a single-coordinate edit
that reduces defect to zero. A witness on labels 1,...,4 is

    ((12),(13),(24),(34)).

Its endpoint is (13)(24). Deleting any one gate leaves a four-cycle,
which cannot be corrected by inserting a single transposition. Thus no
single-gate replacement makes the circuit exact. Nevertheless the path

    ((12),(13),(24),(34))
    ((13),(13),(24),(34))
    ((13),(13),(34),(34))

has defects 2,2,0 and consists of allowed moves. audit.jsonl checks all
20 distinct one-gate proposals and records the complete endpoint path
with zero-based labels.

**Exact finite checks:** every allowed word reaches an exact word in
the listed cases. At k=2,m=4: N=3,4,5,6. At k=2,m=6: N=4,5,6,7,8.
The largest case has 46,854,304 labeled words and 7,563 relabeling orbits.
All checked words are at graph distance at most two from some exact word.
This last distance bound is not asserted for arbitrary m.

There is a completeness argument extending qualitative connectivity to
ALL N at the fixed even lengths m<=6:

1. Let r be the rank v-c of the full support graph on used vertices.
   Each first connection between two support components merges two
   current permutation cycles. If u is the total number of cycle-merging
   steps, then u>=r and final defect d=2u-m. Hence 2r<=m+d<=m+k.
   Every used support component has at least two vertices, so v<=2r<=m+k.
2. Therefore every allowed m4,k2 word uses at most six labels, and every
   allowed m6,k2 word at most eight. A relabeling-orbit representative
   fits into S6 or S8, respectively. Connected quotient paths at those
   degrees embed into every larger degree; all their exact endpoints
   communicate by Section 3.
3. The remaining smaller degrees are checked explicitly or are the
   unrestricted S2/S3 cases. m0 and m2 are trivial as stated in Section 1.

The quotient retains the full ordered word modulo simultaneous vertex
relabeling. It is a genuine symmetry quotient of R, unlike merely
forgetting order and retaining an unordered support graph. Its orbit
weight is (N)_v/2^b, where b is the number of support components having
two vertices. Indeed an automorphism preserving EACH ordered edge fixes
every vertex in any component of size at least three, and can flip each
isolated edge component independently. Replacement multiplicities are
1 for two used labels, N-v for one fresh label, and binom(N-v,2) for two
fresh labels. These give exact integer detailed balance.

The canonicalization tries both orientations whenever two fresh labels
first occur in an edge, retaining the lexicographically smallest ordered
edge sequence. Generating words by adding each possible used/fresh edge
is exhaustive up to relabeling. The prefix rank and remaining-length
pruning bounds are necessary bounds, not heuristic truncations.

Independent checks compare full labeled graphs with the quotient in five
overlapping cases, and a separate labeled-permutation count DP checks
all nine quotient counts and the identity counts. Thus the all-N
fixed-length connectivity statement is a finite, complete computer-assisted
claim, pending independent review; it is not a growing-length mixing proof.

## 5. A proved quadratic slowdown, not a superpolynomial obstruction

**Proved.** At m=4,k=2,N>=14, with M=binom(N,2),

    gap(R) <= 5/M,
    tau_mix(1/4) >= floor(M/10).

Let A be the set of words (t,t,u,v). Every such word is allowed, so
|A|=M^3, and under the conditional uniform law on A the gates t,u,v
are independent and uniform. A change in the last two positions cannot
leave A. The half-lazy proposal selects one of the first two positions
with probability 1/4.

If u=v (probability 1/M), pessimistically allow every proposal. Otherwise
g=uv has defect two. Deleting a selected t either splits a cycle of g
or merges two cycles of g, in the transported coordinates. There are at
most three splitting transpositions for a defect-two permutation, so
over uniform t the splitting case has probability at most 3/M. Allow
every proposal in that case too. In the remaining case the deleted word
has defect three. To return to defect at most two the replacement must
split one of its cycles. A defect-three permutation has at most six
splitting transpositions: the maximum is a four-cycle. Thus

    Phi(A) = Q(A,A^c)/pi(A) <= (1/4)(1/M+3/M+6/M)=5/(2M).

For N>=14 the stationary mass of A is at most 1/2. To verify this without
an enumeration formula, count words with three disjoint support edges,
one occurring twice and the others once. The repeated positions have
six choices, giving at least 6 M binom(N-2,2) binom(N-4,2) allowed words.
This is at least 2M^3 at N=14, and the two ratios binom(N-j,2)/M increase
with N. The indicator Rayleigh quotient is Phi(A)/(1-pi(A))<=5/M.

For the mixing lower bound, start with pi conditioned on A. Its density
relative to pi is at most 1/pi(A) at every time. The chance of an exit
in any one step is at most Phi(A), so TV at time t is at least
1-pi(A)-t Phi(A)>=1/2-5t/(2M). The claimed lower bound follows by taking
t<M/10 and using the worst-state definition of mixing time.

audit.jsonl computes the exact cut flux and indicator quotient at eight
degrees, including N=100. Those checks supplement the symbolic proof.
This polynomial slowdown is fully compatible with rapid mixing in N,m;
it refutes only an N-independent coupon-collector rate for the constrained
chain. It makes no claim about k growing as log N.

## 6. Constant error budget would recover exact functionality without repair bias

For even m, let Z_m(g) count length-m transposition words with endpoint g.
**Proved:** Z_m(g)<=Z_m(id) for every g. Write m=2r and f(h)=Z_r(h).
Reversal of a transposition word gives f(h^-1)=f(h). Convolution and
Cauchy--Schwarz give

    Z_2r(g) = sum_h f(h) f(h^-1 g)
             <= sum_h f(h)^2 = Z_2r(id).

Let B_k^even be the even permutations with ell<=k. Uniform relaxed
sampling therefore has exact-endpoint probability

    p_exact = Z_m(id)/sum_{g in B_k^even} Z_m(g) >= 1/|B_k^even|.

At k=2,

    |B_2^even| = 1 + 2 binom(N,3) + 3 binom(N,4) = O(N^4).

The three types are identity, a three-cycle, and two disjoint
transpositions. Rejection on the event eval(w)=id yields EXACTLY the
uniform exact-identity law if relaxed draws are exactly stationary.
If a draw is within delta of relaxed uniform in TV, conditioning changes
the target by at most 2 delta/p_exact, and acceptance is at least
p_exact-delta. Taking delta<=epsilon/(2|B_2^even|) gives error <=epsilon
with polynomial expected overhead. Use independent fresh runs for this
simple rejection construction; no unproved independence of MCMC returns
is assumed. Circuit length stays m, and no deterministic repair is used.

Consequently a polynomial worst-case mixing theorem for R at k=2 would
give a polynomial-time near-uniform sampler of exact identity words at
every feasible length. This is a conditional implication, NOT a proved
mixing theorem or an exact-distribution algorithm from finite-time MCMC.
For constant k the analogous bound is polynomial in N. At k=O(log N),
the crude bound |B_k|<=sum_{j<=k} M^j gives quasipolynomial, not polynomial,
overhead. No hardness conclusion follows from that upper bound.

## 7. First unproved steps and dependencies

Qualitative boundary lemma (unresolved): every even-length word of defect
two can reach an exact word through single-coordinate replacements while
keeping defect at most two. Section 4 proves it at m<=6 only. The stronger
two-edit version is supported by these cases but remains conjectural.

Quantitative target (unresolved): for some fixed polynomial P,

    gap(R on A(N,m,2)) >= 1/P(N,m)

for every N>=3 and even m>=4. A proof would in particular prove full
connectivity. Allowing k=C log N is a separate unresolved variant; adding
states does not make the spectral gap monotone.

Inputs: elementary permutation cycle arithmetic and Cauchy--Schwarz;
the constructive vertex-sweep argument reproduced above; exact finite
classification by ordered-word relabeling with independent count checks.
No literature theorem, original-chain gap assumption, or empirical
spectral lower bound is imported. Spectral power probes are floating-point
Rayleigh estimates from two seeds, providing no certified lower bound.
No stable manuscript paragraph claiming rapid mixing is warranted.
