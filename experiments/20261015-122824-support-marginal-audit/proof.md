# Support marginals of the actual circuit walk

Author status: **proved** identities and obstructions below, pending
independent review. **Unresolved:** a polynomial worst-case support-marginal
mixing bound for growing N, including full-cycle length m=N+1. Failure of
lumpability is NOT a counterexample to fast marginal mixing.

## 1. Exact target and the weaker mixing question

Let Omega_g(N,m) be ordered transposition words with product g, acting
rightmost first. Let pi be its uniform law. Phi(w) is the labeled support
MULTIGRAPH: vertex labels and transposition multiplicities are retained;
only gate order is forgotten. Let

    A_g(G)=#{w in Omega_g(N,m): Phi(w)=G},
    mu(G)=A_g(G)/|Omega_g(N,m)|.                                  (1)

This is the correct weighted graph law induced by uniform circuits.
Repeated occurrences are not artificially distinguished when counting
words. Forgetting multiplicities too gives the further pushforward of mu.
Forgetting vertex labels would be a different, coarser question.

The kernel is exactly the previously defined all-pair walk

    K=K_G=I/2+H_G/4+R_G/4.

H_G selects a uniform unordered position pair i<j and a uniform sign.
On a B b, its moves are

    a B b -> b [ba B ab] (bab),
    a B b -> (aba) [ab B ba] a.

R_G selects a uniform unordered pair and a uniform transposition s; it
sends a B a to s [sa B as] s and holds on unequal endpoints. Brackets
conjugate every intervening gate. Boundaries are linear, with no wraparound.

The existing constructive proof gives reversibility and irreducibility
on every nonempty fiber; half laziness gives convergence. Consequently
the support marginal converges to (1) from every word. Its rate is the
separate quantity

    d_graph(t)=max_w ||Phi_* K^t(w,.)-mu||_TV.                     (2)

Data processing gives d_graph(t)<=d_circuit(t), but need not give equality.
Thus the user's graph-only target is a weaker legitimate objective.

At stationarity the graph law is already (1). Starting with graph law mu
and an arbitrary choice of circuit above each graph need not preserve mu
at the next step; the conditional gate-order distribution also matters.
Indeed, if w,v have the same graph but different next-graph rows, the
initial law pi+eta(delta_w-delta_v), with 0<eta<=1/|Omega_g|, has graph
marginal exactly mu. After one step its graph marginal differs from mu
by eta times the difference of those rows.

For a fixed full four-cycle and m=3, there are 16 words but only 12 support
trees. Eight trees have weight 1 and four have weight 2. For example, the
star {(12),(13),(14)} has one compatible order, whereas the path
{(12),(13),(34)} has two. Thus the graph marginal is not the uniform
Cayley-tree law, nor is its support all 16 labeled trees.

## 2. Exact failure of graph lumpability for K_G

A support process would be a closed Markov chain for every initial word
only if K(w,Phi^{-1}(G')) depends on w solely through Phi(w).

**Counterexample (proved), already at minimal length.** Take N=4,m=3,
g=(1234), and

    w=((13),(12),(34)),       v=((13),(34),(12)).

Both compute g and have the same support tree. For the star
T={(12),(13),(14)}, direct substitution gives

    K(w,Phi^{-1}(T))=0,       K(v,Phi^{-1}(T))=1/24.              (3)

Indeed from v the inverse Hurwitz move on its first two gates gives
((14),(13),(12)). It is one of the six signed pair choices, with total
Hurwitz-branch probability 1/4. From w none of the six signed choices
gives that star. Their support edge sets, in pair/sign order
(1,2)+,-; (1,3)+,-; (2,3)+,-, are respectively

    {12,23,34}, {13,23,34}, {14,24,34}, {13,14,23},
    {12,13,34}, {12,13,34}.

All square moves hold because every gate is distinct. This is a complete
finite proof of (3), not an asymptotic inference. It also refutes strong
lumpability for simple labeled support graphs.

**Counterexample (proved), in the requested m=N+1 regime.** Take N=4,m=5,
g=(1234), and

    w=((12),(12),(14),(13),(12)),
    v=((14),(12),(12),(13),(12)).

They share the multigraph containing three copies of (12) and one each
of (13),(14). For G' containing three copies of (12) and one each of
(13),(34), exact channel enumeration gives

    K(w,Phi^{-1}(G'))=1/80,       K(v,Phi^{-1}(G'))=0.             (4)

The successful channel from w is H^+ on positions 3,4. The supplied
script checks every one of the 80 labeled channels per word (20 Hurwitz
and 60 square choices). They have a common integer normalization. It
also verifies the entire 640-word endpoint fiber, so no heuristic
state-space sampling is involved. Even after forgetting multiplicities,
the next-step probabilities of the original simple star differ:
37/48 from w and 31/40 from v.

Nonlumpability means gate order can affect the next graph. It does not
imply that graph mixing is slow. In fact S3 exhibits this failure at m=4
while its full chain, hence its graph marginal, provably mixes rapidly.

## 3. What the stationary-flow graph kernel does and does not prove

There is always a reversible averaged graph kernel

    barK(G,G')=(1/A_g(G)) sum_(w:Phi(w)=G) K(w,Phi^{-1}(G')).      (5)

Summing word detailed balance shows mu(G)barK(G,G')=mu(G')barK(G',G).
Equation (5) is the first-step graph law from a UNIFORM circuit in the
given fiber. Without lumpability, repeatedly applying barK is not the
same as following the actual circuit walk and forgetting order.

Let C be conditional expectation onto graph-measurable functions in
L2(pi); C is an orthogonal projection. Restricted to those functions,
barK is C K C. The exact two-step difference is

    C K^2 C - (C K C)^2
      = C K (I-C) K C
      = [(I-C) K C]^* [(I-C) K C].                              (6)

It is nonnegative and is nonzero whenever lumpability fails. Thus even
starting uniformly within a graph fiber does not generally justify
iterating barK. For the star T in the minimal example above, the actual
two-step return probability is 55/96; barK^2(T,T)=41/72. Their difference
is exactly 1/288. The script checks (6) by within-fiber variances in all
six declared endpoint fibers.

**Counterexample (proved): fast barK need not imply fast graph mixing.**
Consider four states a,b,c,d, uniform stationary law, symmetric transition
rates P(a,b)=P(c,d)=1/4 and P(b,c)=delta, with 0<delta<=1/4. Diagonals
complete rows; the chain is half-lazy and irreducible. Project a,b,c to
graph label 0 and d to graph label 1. The stationary-flow projection has

    barP(0,1)=1/12,       barP(1,0)=1/4,       gap(barP)=1/3.

Starting at a, reaching label 1 requires crossing b->c. A union bound
gives P_a(Phi(X_t)=1)<=t delta. Since its stationary probability is 1/4,

    ||law(Phi(X_t))-mu||_TV >= 1/4-t delta.                       (7)

Taking delta=2^(-r) gives exponentially slow marginal convergence in r
despite a constant projected gap. This is a counterexample to a GENERAL
proof shortcut, not a bottleneck claimed for the circuit chain.

Also, a one-step path coupling based solely on a graph distance cannot
contract from every pair of circuits here: circuits in the same graph
have distance zero but different next-graph laws. A successful coupling
may need to track some hidden order information without fully mixing it.

## 4. A sufficient condition that only sees graph observables

The full circuit gap is sufficient but not necessary. The precise
smaller function space is

    H={h o Phi : E_mu h=0},
    V=span{K^t f : f in H, t=0,1,2,...}.                         (8)

It is the smallest K-invariant subspace containing the centered graph
observables. It may be a proper subspace of all centered circuit
functions. Functions forever invisible to the graph are excluded.

**Conditional theorem (proved implication).** If p(N,m)>=1 and

    ||f||_(2,pi)^2 <= p(N,m) E_K(f,f)       for every f in V,     (9)

then, writing S=|Omega_g(N,m)|,

    d_graph(t) <= (sqrt(S)/2) exp(-t/p(N,m)).                    (10)

In particular polynomial p gives polynomial marginal mixing in N,m and
log(1/epsilon), since log S<=m log binom(N,2).

Proof. V is finite-dimensional and invariant, and self-adjoint K is
nonnegative by half laziness. Condition (9) bounds its operator norm on
V by 1-1/p. For any graph function h with |h|<=1, center h o Phi; its
L2(pi) norm is at most 1. Evaluating K^t at a word w costs at most
pi(w)^(-1/2)=sqrt(S) by Cauchy-Schwarz. Take one half the supremum over
|h|<=1 to obtain the total-variation bound (10).

Equivalently, (9) requires a polynomial gap only for spectral modes with
a nonzero component visible in a graph observable. A projected Poincare
bound on H alone is insufficient, because K can send H outside H.

**First unresolved lemma for the user's family.** For the actual K_G on
Omega_(full N-cycle)(N,N+1), establish (9) with p(N,N+1)=poly(N), or
directly couple the two support marginals at polynomial time without
assuming the hidden circuit order is uniform. No such bound is proved
in this audit. The explicit failure of lumpability rules out using an
exact standalone cut-and-join graph kernel without an additional argument.

## 5. Relation to cut-and-join and known easy cases

Standard split-merge for random transpositions projects a CHANGING
permutation to its cycle-length partition. Blumberg, *A Coupling Argument
for the Random Transposition Walk*, arXiv:1109.3915v1, Definitions 2 and
5 (pp. 5 of the PDF), specifies that kernel. Theorem 1 concerns the
ordinary random-transposition permutation walk. Source inspected:
https://www.stat.berkeley.edu/~aldous/206-RWG/RWGpapers/blumberg.pdf .

Our endpoint permutation g is fixed throughout. Its cycle partition is
constant, whereas the support graph changes and retains more information.
Thus that theorem does not identify (5) or prove (2). Likewise the earlier
auxiliary tree-slide theorem concerns a separately declared graph target
and transition rule, not (1) and the order-dependent lifted walk.

Positive cases that DO follow rigorously:

- For S3, every feasible endpoint and m>=2, the previous actual K_G gap
  >=1/(2m) and data processing give
  t_graph(epsilon)<=ceil(2m[(m-1)log(3)/2+log(1/epsilon)]).
- For arbitrary N at m=2,g=id, words are (a,a), graphs are doubled edges,
  and K_G=3I/4+Pi/4. Thus the graph distance to uniform is
  (1-1/M)(3/4)^t, M=binom(N,2). The graph gap is 1/4 when M>1.
- At m=2 and a disjoint-double-transposition endpoint, there are two
  circuit orders but only one graph: graph mixing time is zero. For a
  three-cycle endpoint the three ordered words have distinct supports,
  so graph and circuit mixing coincide (gap 3/8).
- Nonempty fibers at m=0,1 or N=2 have a single graph. Odd identity
  lengths are empty; arbitrary endpoints require m>=N-c(g) and matching
  parity. No mixing time is assigned to an empty fiber.

Dependencies: uniform reversibility and all-endpoint connectivity from
the constructive nonlocal-lift proof; the S3 gap from the interval-gap
proof. Equations (1)--(10), finite witnesses and the four-state example
are self-contained. The split-merge source is a checked scope comparison,
not a mathematical premise of a circuit gap claim.

Stable manuscript-ready paragraph, pending independent review: The
support pushforward of uniform fixed-endpoint circuit words weights each
labeled multigraph by its number of realizing orders. For the uniform
all-pair lifted Hurwitz/square kernel this projection is not strongly
lumpable, already for minimal factorizations of a four-cycle and for
length N+1 at N=4. Its stationary-flow projection is reversible for the
correct weights, but its iterates need not equal the observed graph law.
Polynomial mixing of that marginal remains a separate question; a
Poincare inequality on the invariant space generated by graph observables
would suffice without controlling all circuit modes.
