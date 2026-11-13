# Research Ideas: Gate Libraries, Toffoli Rewrites, and Planted Relations

Date: 2026-11-06, Europe/Berlin.

Status: **unresolved research questions and a conjectured assumption template**.
This note reformulates the user's ideas for future agents. It does not launch
an investigation, assert a new theorem, or endorse a hardness assumption.
The user's clarification about Toffoli components concerns permutation parity;
the distinction from connectivity of identity-circuit descriptions is retained
explicitly below. For connectivity, the user permits arbitrarily long sequences
of local moves and prioritizes small working memory; no step-count bound is
required.

## Shared language

Let \(S\) be a specified finite library of gate symbols, with a declared
permutation assigned to each symbol, and let \(G=\langle S\rangle\). Products
act rightmost first. Define

\[
\Omega_S(m;g)=\{(s_1,\ldots,s_m)\in S^m:s_1\cdots s_m=g\},
\qquad U_S(m;g)=\operatorname{Unif}(\Omega_S(m;g)).
\]

The distribution is defined only when the fiber is nonempty. Unless explicitly
changed, circuit descriptions are labeled, ordered, fixed-length words, and
each gate symbol has equal sampling weight. Distinct encodings of the same
gate must not silently change that weight. For wire-local gates, use \(n\)
wires and \(N=2^n\) basis states; for the all-transpositions model, \(N\) is
the explicit permutation degree. Every future complexity claim must identify
whether it is polynomial in \((n,m)\) or \((N,m)\).

## Q1. Can a gate library make representation counts nearly independent of the permutation?

**Clean question.** Uniform sampling of circuit descriptions depends on the
chosen gate library and length. Can we find a useful, efficiently implementable
gate library for which different attainable permutations have approximately
the same number of length-\(m\) circuit descriptions? If so, does this make
sampling circuits with a prescribed endpoint, especially the identity, easier?

The uniform law on a fixed finite group itself is unambiguous. What changes
with the gate library is the map from uniformly sampled words to group elements
and the uniform conditional law on each endpoint fiber. Replace the informal
phrase "no easy and hard distributions" with two separate questions: balanced
representation counts, and efficient sampling within a specified fiber.

A precise count is

\[
A_{S,m}(g)=|\Omega_S(m;g)|,
\qquad \Pr[s_1\cdots s_m=g]=A_{S,m}(g)/|S|^m.
\]

Choose the comparison set \(C_m\subseteq G\) explicitly: the whole generated
group when appropriate, or a specified class permitted by periodicity and
other invariants. Require all endpoints in \(C_m\) to be reachable. One strong
version of the target is

\[
\max_{g\in C_m}
\left|\frac{|C_m|A_{S,m}(g)}{|S|^m}-1\right|\le\varepsilon,
\]

when all length-\(m\) words end in \(C_m\). This is a pointwise relative-error
criterion; total-variation closeness of the endpoint law is a different,
weaker possible target. A choice of \(C_m\) must not hide a large excluded
class of endpoints that the intended application needs.

Questions to make this direction specific:

1. Which restrictions matter: constant gate arity, geometric locality,
   polynomial-size descriptions, no ancillas, or a fixed universal library?
   Taking every group element as an available gate is not an efficient local
   circuit construction without an implementation and sampling model.
2. At what lengths and accuracy does count balance hold? Account for short
   unreachable endpoints, periodicity, and any sign restriction. Does adding
   an identity gate help, and is that change of target acceptable?
3. Can a rapidly mixing unconditioned gate walk provide the required pointwise
   balance? What additional completion-count or bridge-sampling primitive is
   needed to turn that fact into an efficient conditional sampler?
4. Does changing the library remove a specific obstruction found in the
   transposition model, while retaining implementable gates?

**Desired future deliverable:** one explicit gate family, a precise count/error
target and parameter regime, and a separate account of what would make its
identity fibers efficiently samplable. Balanced counts alone are not a
bridge-sampling algorithm. Existing expander benchmarks are relevant background,
with their implementation caveats retained.

## Q2. What is connected for Toffoli gates, and which moves connect identity circuits?

**Clean question.** For a precisely specified Toffoli library, characterize the
connected components of identity-circuit descriptions under chosen local,
function-preserving rewrites. If these rewrites leave multiple components,
what additional local relation or heat-bath update connects them while keeping
the intended identity-circuit target, with arbitrarily much time but small
working memory?

### Connectivity resource convention (also applies to Q3)

The primary target is qualitative reachability: for every two circuits
\(C,D\) in the declared identity fiber, there is a finite sequence
\(C=C_0,C_1,\ldots,C_T=D\) of legal local rewrites. There is no required
polynomial bound on \(T\), no diameter bound, and no mixing-time requirement.
"Infinite time" means arbitrarily long finite paths are acceptable. Each move
must obey the declared locality and memory bounds, however long the path is.

Specify the maximum gates and wires touched by a move, preferably constants
independent of \(n,m\). Account separately for storage of the current circuit
and auxiliary working memory. A useful small-memory target is workspace for
one bounded local patch and its position/wire indices; state any stronger
workspace requirement explicitly. Local edit selection or verification may
also take arbitrarily long time within that memory budget. An implementation
should update the current circuit in place without storing the entire rewrite
history, a global permutation table, or an ever-growing proof. Circuit ancillas
and padding are additional resources to declare; unlimited time does not
implicitly authorize unlimited circuit growth. A smaller workspace guarantee
or a time bound would be an optional strengthening of this connectivity task.

Start, provisionally, with standard positive-control CCNOT gates on arbitrary
triples of distinct wires, \(n\ge3\), without ancillas. A gate with controls
\(a,b\) and target \(c\) acts as
\(x_c\leftarrow x_c\mathbin{\oplus}(x_ax_b)\), fixing other bits.
Variants with NOT/CNOT gates, negative controls, more controls, geometric
restrictions, or clean ancillas are separate models to name explicitly.

### The parity clarification

The user has in mind the separation between even and odd permutations under
parity-preserving operations. Three different graphs must be distinguished:

| Graph | Vertices | Edges to specify |
| --- | --- | --- |
| Basis-state action graph | Bit strings \(x\in\{0,1\}^n\) | Apply one gate to a bit string |
| Permutation graph | Permutations of the basis states | Compose with an allowed gate |
| Identity-circuit rewrite graph | Words in \(\Omega_S(m;\mathrm{id})\) | Replace part of a word without changing its full product |

**Elementary formulation checks (proved directly from the definitions):**
an embedded CCNOT on \(n\) wires is a product of \(2^{n-3}\) disjoint
transpositions, one for each setting of the untouched wires. It is odd at
\(n=3\) and even at \(n\ge4\). Even generators cannot connect opposite signs
in the permutation graph. If their generated subgroup is \(H\), the components
of the graph on the full symmetric group are the cosets of \(H\), and are
isomorphic by translation. There are exactly two only if \(H\) is the full
alternating group. Pure positive-control CCNOT also fixes every bit string of
Hamming weight zero or one, so the full-domain two-component conclusion needs
additional restrictions or a different library. Here parity means permutation
sign, not parity of a bit string's Hamming weight.

Every identity-circuit vertex already has endpoint \(\mathrm{id}\), which is
even. Thus endpoint sign alone cannot distinguish two components of the
identity-circuit rewrite graph. If the intended claim is about that graph,
identify a further invariant of the circuit description and the exact moves
preserving it. The assertion of exactly two such components is **unresolved**.

For comparison, transposition Hurwitz moves preserve the labeled weighted
support-component data, rather than every edge of the starting support graph.
The analogous move on arbitrary group elements is

\[
(a,b)\longmapsto(b,b^{-1}ab).
\]

It preserves the product in the ambient group, but it is a valid move on a
chosen gate library only if the conjugate remains an allowed gate. Whether
standard Toffoli gates have the closure needed here is a question to check;
otherwise specify which pairs are allowed or how the conjugate is compiled.

Questions to make this direction specific:

1. Which of the three graphs is the object of the proposed two-component
   statement? On which domain and for which gate library does it hold?
2. Which same-length identities among Toffoli words supply valid local rewrites?
   Are commutation, cancellation-pair replacement, or larger same-product
   windows sufficient for connectivity?
3. Can a bounded collection of block lengths connect every nonempty fixed
   length identity fiber? If padding or ancillas are essential, state the
   resulting enlarged space and its target law separately.
4. If studying the permutation graph instead, what efficient odd gate can
   cross the sign classes, and does the enlarged library generate the intended
   group? Crossing sign classes does not itself prove identity-word connectivity.

**Desired future deliverable:** a graph and move definition, its actual component
invariant, and a connectivity theorem or counterexample with exceptional small
cases, explicit local move bounds, and auxiliary memory accounting. Arbitrarily
long paths are acceptable. If a Markov chain is additionally proposed, specify
laziness, update probabilities, window boundaries, and why its target is
stationary. Its mixing rate is a separate, optional quantitative question.

## Q3. Can local transposition surgery induce useful Toffoli rewrites?

**Clean question.** Can we transfer our transposition methods to Toffoli circuits
by opening a small Toffoli subcircuit into transpositions, applying
product-preserving Hurwitz or heat-bath changes, and closing the result back
into a short Toffoli subcircuit? Can the resulting moves prove connectivity,
using small working memory and arbitrarily many local steps? As a separate
extension, could additional quantitative conditions imply rapid mixing?

The intended local operation is

\[
LBR\;\longrightarrow\;L\,E(B)\,R
\;\longrightarrow\;L\,\widetilde B\,R
\;\longrightarrow\;LB'R,
\]

where \(E(B)\) expands a gate block, every intermediate edit preserves its
product, and \(B'\) is a valid word over the original library with that same
product. For a fixed-length chain require \(|B'|=|B|\). First use consecutive
blocks; editing arbitrary indexed gates while ignoring intervening gates is
not generally a valid substitution in a noncommutative product.

Here "local" needs two bounds: the number of gates opened, and the number of
wires on which they act. A full-register transposition expansion can be
exponential in \(n\). A potentially useful formulation opens a block acting
on \(q\) wires, performs surgery on its \(2^q\) local states, and extends
the same local permutation identically across all untouched-wire settings.
Constant \(q\) keeps the local expansion bounded. Allowing
\(q=O(\log(n+m))\) is a separately declared relaxation with a potentially
polynomial-size expansion, not automatically a small-memory implementation.
Account for peak workspace throughout expansion, edits, and recompilation;
arbitrary runtime is acceptable for the primary connectivity question.

Questions to make this direction specific:

1. Which transposition edits preserve the structure needed to recompile into
   the chosen Toffoli library, with the allowed wire set and length? Can an
   edit be selected, checked, and recompiled within the declared small workspace,
   even if the procedure takes arbitrarily long?
2. Do these induced rewrites connect the original fixed-length identity-word
   space, or only a space with extra gates, wires, or padding?
3. For the optional sampler question, what is the proposal probability on
   Toffoli words? Different
   words may have different numbers of expansions and recompilations. How are
   these multiplicities corrected to obtain the declared stationary law?
4. For the optional fast-mixing question, is there a useful comparison chain
   whose transitions can be implemented by such local surgery with polynomial
   overhead and congestion? This is not a prerequisite for connectivity.

### Connection to proofs of equivalence

The suggested reference is Abhishek Jain and Zhengzhong Jin,
[Indistinguishability Obfuscation via Mathematical Proofs of Equivalence](https://eprint.iacr.org/2022/1430),
FOCS 2022. The [conference version](https://ieee-focs.org/FOCS-2022-Papers/pdfs/FOCS2022-4Bu7jGV9xIcveUWYj3oWoi/551900b023/551900b023.pdf),
Section II-A, printed pages 1029–1030, describes **Delta-equivalence**:
appropriate propositional proofs yield a sequence of equivalent circuits
whose adjacent members differ by equivalent logarithmic-size subcircuits,
after padding to a common topology. This is the relevant source connection.
The scoped passage was checked for terminology; its full proof and a reversible
Toffoli translation have not been audited here.

**Proposed connection, unresolved:** can an analogous proof system produce
legal local rewrites of reversible Toffoli circuits, executable with small
working memory and controlled padding and ancilla use? Does it provide paths
for every pair of identity words, or only pairs supplied with an equivalence
proof? For connectivity the proof/path may be arbitrarily long; distinguish
its existence from the memory needed to find or execute it without retaining
the whole proof. Short proofs are an optional stronger premise.

**Conditional mixing question:** assuming such paths exist and can be generated
in polynomial time, what further property would bound the gap of a specified
random walk? Candidate obligations are controlled path congestion, a suitable
flow of randomized paths, or projection/restriction estimates. Short proofs
and short paths alone do not establish rapid mixing. A walk using a supplied
proof as extra state also needs its own target and a justified projection onto
circuit descriptions.

**Desired future deliverable:** one explicit expand/edit/recompile rule and its
locality and workspace bounds, followed by a precise connectivity target with
no required step-count bound. Any optional mixing implication must state its
additional quantitative assumption beside the conclusion.

## Q4. A planted identity-subsequence assumption for circuits

**Clean question.** Is it computationally hard to distinguish a uniform
length-\(m\) identity circuit from a length-\(m\) identity circuit containing
a planted, hidden length-\(k\) identity subsequence? Can this serve as a
noncommutative circuit analogue of a planted-XOR-type assumption?

Start with the all-transpositions model, where the word is given explicitly
and evaluating a selected subsequence is efficient in \(N,m\). Let
\(U=\operatorname{Unif}(\Omega(N,m))\). For
\(I=\{i_1<\cdots<i_k\}\subseteq[m]\), define

\[
E_I=\{W=(t_1,\ldots,t_m):t_{i_1}\cdots t_{i_k}=\mathrm{id}\}.
\]

The selected gates retain their original relative order; intervening gates
are omitted. This is an ordered subsequence, not necessarily a contiguous
window. The full circuit must compute identity in both distributions.

Choose a public family \(\mathcal I\) of allowed index sets, each with
\(\Pr_U[E_I]>0\). A concrete **candidate decision game** is:

| World | Sampling rule | Adversary sees |
| --- | --- | --- |
| Null \(D_0\) | Draw \(W\sim U\) | \(N,m,k,\mathcal I,W\) |
| Planted \(D_1\) | Draw \(I\) uniformly from \(\mathcal I\), then \(W\sim U\mid E_I\) | The same public information and \(W\), with \(I\) hidden |

For a declared parameter schedule indexed by \(\lambda\), the proposed
assumption is that every probabilistic polynomial-time adversary has negligible
advantage

\[
\left|\Pr[A(D_1)=1]-\Pr[A(D_0)=1]\right|.
\]

**Status: conjectured template only.** No hard parameter regime, efficient
planted sampler, reduction from planted XOR, or application is asserted.

Formulation choices and first questions:

1. **Hidden versus public positions.** If \(I\) is revealed in the
   transposition model, the direct test \(E_I\) has advantage
   \(1-\Pr_U[E_I]\) for a fixed \(I\). Thus public positions are a control,
   not the intended hidden-plant game. A fixed secret set reused across
   samples is a separate game from a fresh hidden set on every sample.
2. **Planting law.** The table chooses the set first and then conditions the
   word. Conditioning only on the existence of some identity subsequence,
   or generating a word and subsequently choosing one of its witnesses,
   defines potentially different laws. Specify which law a construction
   actually samples and how multiple witnesses affect its probability.
3. **Nontrivial regime.** For transpositions both \(m\) and \(k\) must be
   even. Exclude \(k=0\) and \(k=m\), where the extra condition is automatic.
   Treat \(k=2\), constant \(k\), and contiguous windows as attack controls.
   There are only polynomially many fixed-length contiguous windows, and
   \(\binom{m}{k}\) candidate subsets for general positions. The number of
   accidental witnesses under the null law matters as much as finding one.
4. **Statistical versus computational hiding.** Are the two laws already
   statistically close, or is there a detectable statistical signal that
   appears computationally difficult to exploit? Estimate the null event
   probability and witness-count fluctuations before declaring a regime hard.
5. **Efficient generation.** Can both required ensembles be generated at the
   chosen parameters without assuming the very all-length bridge sampler
   under investigation? A sampler with an error guarantee must account for
   the potentially much smaller conditioning event. Simple interleaving of
   two identity words need not preserve the full product in a noncommutative
   group and is not automatically the planted law.
6. **Adversarial interface.** Begin with one explicit noiseless word and fresh
   planting randomness. Specify the security parameter, runtime model and
   representation. Reused hidden positions, multiple queries, a persistent
   key, or replacement noise require separate games; any noise must be matched
   in both worlds. A succinct Toffoli version changes both sampling and
   subsequence-evaluation complexity and needs its own formulation.
7. **First attack checklist.** Compare gate repetitions and multiplicities,
   prefix/window cycle types, support and weighted support components, fixed
   points and low-dimensional characters of selected products, short-relation
   counts, syntactic leakage, subset search, and meet-in-the-middle attacks.
   The full endpoint's sign and cycle type are identical in both worlds.

The analogy with planted XOR is an analogy of hidden relations. Ordered
noncommutative products do not inherit an XOR assumption or reduction merely
by replacing addition with composition.

**Desired future deliverable:** a fully specified pair of efficiently samplable
ensembles, an explicit parameter schedule and adversarial interface, and the
first attacks or reductions. Only after those checks should a concrete
hardness assumption be proposed for an application.

## Existing work to consult before a future investigation

- [Project map](../PROJECT_MAP.md) and [current targets](project-map/TARGETS.md):
  distinguish these proposed directions from the existing sampler frontier.
- [Expander gate-set discussion](../papers/transposition_identity_samplers/sections/expander_gate_sets.tex):
  relevant to Q1; a base-walk gap does not supply a bridge theorem.
- [Projection and gate-replacement identities](../experiments/20261028-bridge-projections/report.md):
  relevant to Q4's ordered subsequence law; global and connected targets differ.
- [Sparse-noise viability report](../experiments/20261029-noisy-bridge-viability/report.md):
  relevant short-relation/support attacks, with its original scope retained.
- [Failed normal-form routing](project-map/OBSTRUCTIONS.md#o-hub): relevant
  to Q3's distinction between paths and mixing.

A future agent should select one question, preserve its declared distribution
and computational model, and first resolve the indicated formulation gaps.
No Toffoli connectivity theorem or planted-relation hardness is assumed by this
note. Check empty/short fibers, boundary wire counts, sign/period restrictions,
and near-minimal factorizations where applicable; do not transfer the
transposition model's exceptional cases to a new library without checking them.
