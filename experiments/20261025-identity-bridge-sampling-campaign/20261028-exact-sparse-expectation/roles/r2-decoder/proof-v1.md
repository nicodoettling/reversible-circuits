# I2-D.v1: unrestricted assembly with selected-component quotient decoding

Author proof, PROVISIONAL until fresh exact-version review. Exact statement is statement-v1.md. All products act rightmost first and public labels are [N]={1,...,N}. Local quotient indices are zero-based and are mapped to the selected actual labels before output. The target is the full uniform law on ordered transposition identity words Omega(N,m), for N>=2 and every even m>=0. There is no Markov kernel, support cutoff, approximation, rejection of large components or test of a sparse-range inequality. The theorem about expected-polynomial time in specified sparse regimes is separate and requires an exponential-moment bound under this exact law.

## D1. Imported polynomial scalar counts and unrestricted macro law

Let C(v,ell) count connected identity words of length ell on a fixed labeled v-set; C(1,0)=1 and other singleton entries are zero. For v>=2, a nonzero entry requires even ell>=2v-2. The exact positive DYZ recurrence and its labeled ordered-word normalization are accepted inherited inputs, read in experiments/20260922-sparse-global-sampler/proof.md Section2 and source_checks.md and their scoped audits. The imported implementation is

`experiments/20260905-bridge-length-phase-diagram/roles/r3-intermediate-hybrid/component_audit.py`, SHA256 a1cd57b6684ea8f116dcbc397a35e856a70526b81f162c113de4216323b721b2.

Its connected_counts and assembly_counts are the only non-elementary scalar-count dependencies. The source normalization is C(v,ell)=v!ell!h_(g,v), ell=2v-2+2g; the precise published dependency is Dubrovin–Yang–Zagier Proposition1 Eq(13), Section1.2 Eqs(19)–(20). No new independent source verification or new counting theorem is claimed in this role.

Define Z(0,0)=1, Z(0,t>0)=0 and

Z(n,t)=sum_(v,ell) binom(n-1,v-1)binom(t,ell) C(v,ell) Z(n-v,t-ell).  (1)

The full range of feasible v,ell is included. Distinguish the component containing the least remaining label, choose its other labels, choose its positions, choose its connected word, and then choose the complementary identity word. Restricting an output word to that connected support recovers every choice uniquely. Therefore Z(n,t)=|Omega(n,t)|, with all label/interleaving multiplicities and no component-symmetry quotient.

The implementation first prepares **only** C and Z, with no quotient counter. It then samples the complete ordered list of least-label components, including their actual labels and position sets. At each stage choose(v,ell) with the summand of(1), then uniform label and position subsets. Continue until all labels have been assigned. An isolate is(v,ell)=(1,0). There is no eligibility predicate and no cutoff to recompute on a residual input.

For a particular complete labeled macro with component positions fixed, multiplying the conditional type/subset choices telescopes to

product_B C(|B|,ell_B) / Z(N,m).  (2)

The decoder will independently give each local word probability1/C, conditional on that exact macro. This is a full exact macro disintegration, not an unconditioned random-graph law.

## D2. Quotient state, completion count and actual literal decoder

The exact quotient decoder QC.v1 is inherited from

`experiments/20260922-sparse-boundary/roles/r4-construction/quotient_sampler.py`, SHA2567cfd9bcaed9cc08d57d2e50564b829d8a54cbc40e89aa5fe445a2a5c2149ee7c,

with proof-v1.md and the nonauthor construction_audit.md in the same investigation. Its old **restricted** global target and failed omitted-mass application remain unchanged; only its all-genus connected decoder is used here. The new file imports the hash-verified source and replaces the count and transition maps with explicit LinearMemo objects. The recurrence, transitions and literal edge selection remain unchanged.

For completeness, an exposed connected-decoding history records its literal permutation p and support partition pi. Every cycle of p lies in one support block. Its quotient q is the sorted multiset of sorted cycle-length lists, one per support block. This is a complete invariant for simultaneous relabeling of p and pi: match support blocks, then oriented cycles of equal lengths. Right multiplication by a transposition and joining support blocks commute with that relabeling. Consequently the number M(q,q') of literal transpositions taking a representative to successor q' is well-defined and the row sum is binom(v,2). Repeated cycles and support blocks are indexed before equal successors are collected.

Let G(r,q) be the number of suffixes of length r that finish at identity and whose combined support with the exposed prefix is connected. Then

G(0,q)=1 iff q consists of one block containing v singleton cycles,

G(r,q)=sum_q' M(q,q')G(r-1,q').  (3)

These equations follow from disjoint first-letter decomposition. Pruning a state with more than r+1 support blocks is valid because each remaining edge can merge at most two blocks. The initial q consists of v singleton support blocks. Its value G(ell,q_initial) equals C(v,ell), which the implementation checks against the imported scalar count.

The sampler retains the **actual** p,pi. For every actual edge e it computes its actual child and chooses e with weight G(r-1,q(child)). The denominator is G(r,q(current)) by equivariance and(3). For every fixed connected identity word, its conditional probabilities telescope to1/C(v,ell); the terminal condition forces identity and connected support. Quotienting therefore does not accidentally sample graph/orbit types uniformly. The exposed-support81-versus80 distinction is retained.

The completion recurrence is evaluated with an explicit continuation stack; dependencies strictly decrease r. Literal decoding is a for-loop in ell. No Python recursion limit is altered. Each selected nontrivial macro component gets a **fresh** counter. It is created only in decode_macro, after sample_macro has completed the full macro, and is explicitly discarded at the end of that component iteration. Isolates invoke no counter. Optional metrics retain integers only, never a counter or table reference.

Multiplying the independent conditional local laws1/C with(2) gives exactly1/Z(N,m) for every literal output word. All components are eligible, so this is the full uniform target with error zero. The conclusion holds outside the sparse regimes too; efficient expectation outside them is not asserted.

## D3. Quotient inventory and deterministic memo accounting

Fix one selected component(v,ell), and let S=3^(v-1). A canonical quotient state can be encoded as an ordered composition of compositions of v, with each of the v-1 gaps marked as inside a cycle, between cycles of a block, or between blocks. Choosing the canonical block/cycle order makes this encoding injective. Hence there are at most S quotient states, whether reachable or not.

The count key includes remaining length. Thus the number of memo entries is bounded by

Q=(ell+1)S.  (4)

The length factor is essential. There are at most S transition-map entries, each with at most binom(v,2) distinct successors. All such entries are constructed only when requested while evaluating this selected component; the algorithm never traverses all component degrees beforehand.

LinearMemo uses arrays of keys/values and scans all existing keys for membership, retrieval or replacement. It has no average-case hashing premise. Each count-map access makes at most Q key comparisons; each transition-map access makes at most S. New keys are appended. Replacing a value does not add a duplicate key.

The explicit DFS expands a particular unfilled(r,q) at most once. A second occurrence cannot be an active ancestor because remaining length strictly decreases; a previously scheduled duplicate is skipped after the first expansion completes. Each unique expansion enqueues O(v^2) children plus its finish action. It makes O(v^2) count-map accesses, up to a constant factor, and O(1) transition requests. Thus the total number of count-map accesses during filling is O(Qv^2), and deterministic key comparisons are O(Q^2v^2). The DFS stack has at most O((ell+1)v^2) pending entries: each active depth contributes at most one finite successor list. Recomputing a successor list at finish changes only a constant factor.

The inherited transition routine lists O(v^2) indexed cycle joins/splits and canonicalizes each successor. Its local Counter has at most O(v^2) entries. Even pessimistically charging linear collision scans and full tuple comparisons in this **polynomial-sized** temporary Counter gives polynomial work in v; it does not introduce a second exponentially sized map. The outer transition map is the explicit linear map just accounted for. No support-state inventory is hidden in a global cache.

## D4. Bit sizes and one fixed P^12 time envelope

Let P=N+m+2, so v<=N<P and ell<=m<P. Work in exact binary arithmetic. Use deliberately loose bounds B,D=O(P^2):

* every completion count is at most binom(v,2)^r, hence has O(1+(ell+1)log(v+1))<=O(P^2) bits;
* positive sums in(3) never exceed their count bound; multiplicities have O(log(v+1)) bits;
* a count/transition key has O(v log(v+1)+log(ell+1)+1)<=O(P^2) bits;
* all C,Z, binomial and positive scalar recurrence intermediates have O((m+1)log P)<=O(P^2) bits, allowing the fixed polynomial numerator factors in the DYZ recurrence;
* memo-operation metric counters, when requested, count at most poly(P)9^v operations and therefore have O(P^2) bits. Metrics are optional and create no higher-cost loop.

With schoolbook arithmetic, a multiplication/division of these integers costs O(P^4); addition/comparison is cheaper. Key hashing/comparison, tuple construction, positive length arithmetic and sorting of each polynomial-sized successor inventory cost at most O(P^6) per previously unseen quotient state. This bound includes pessimistic collision scans of its temporary O(v^2)-entry Counter, tuple comparisons of length O(v), and canonical sorting. No unit-cost large-integer assumption is used.

Equation(4) gives Q<=P3^(v-1). The dominant count-map comparison work is bounded by

O(Q^2 v^2 D) <= O(P^6 9^v).  (5)

The count additions/multiplications require O(Qv^2) operations on B-bit operands, bounded by O(P^7 3^v). Creating all transition lists costs O(P^6 S), and transition-map scans are bounded by O(QS D), covered by(5). The O((ell+1)v^2) literal-edge continuation queries and updates add at most O(P^8 3^v), even allowing fresh missed keys: all new count keys remain inside the same inventory(4). In fact all positive-history child states are already reached by the initial connected-count evaluation, but this stronger fact is not needed for the bound.

Allowing two further powers of P for elementary indexing/address operations and conservative exact-integer/tuple bookkeeping, all deterministic preparation and structural decoding work for one selected component fits

A P^12 9^v  (6)

for one universal constant A. The estimate intentionally leaves slack; it is not a measured complexity claim. It includes linear-map scans and their integer counters, not merely the number of quotient states. The exact exponent does not depend on v, ell, a requested precision, an exceptional-degree threshold or a sparse-regime parameter.

Global scalar preparation is polynomial as well. The positive connected-count and least-label assembly implementations each use O(N^2(m+1)^2) arithmetic operations, with the preceding polynomial bit sizes; schoolbook arithmetic fits O(P^8), before slack. Their binomial/power tables and initialization are also polynomial and fit O(P^12). Sampling the full macro makes at most N component stages and O(Nm) candidate type visits per stage. Even recomputing every binomial by O(P) elementary operations, exact subset unranking, label/position filtering and pessimistic polynomial-size set scans fit O(P^12) nonrandom work. No quotient counter is among these preparation costs.

The algorithm does not compute exp, logarithms, sparse-range thresholds, or a rare-component cutoff. It is the same algorithm for all feasible inputs. Computing C/Z outside an expected-efficient regime remains polynomial, while selected-component decoding may be exponential.

## D5. Fair bits, conditional expectation and storage

The production random interface supplies independent unbiased bits through getrandbits. Exact integers below a bound Z use ceil(log2 Z) bits and reject excess values; bound1 is deterministic and other bounds have conditional acceptance above1/2. The inherited exact_index hook exists for finite audit enumeration and is not part of the production fair-bit interface or its complexity model. The actual implementation’s public default uses SystemRandom; the mathematical theorem is its ideal fair-bit interpretation.

Every count/category bound has polynomial bit size. The macro takes at most3N logical draws; component decoding takes at most ell next-edge draws. Conditional on the sampled complete macro and any preceding decoded components, the next counter is a fresh deterministic function of(v,ell), and its new random bits are independent of that history. Every logical rejection draw has fewer than two expected trials on each positive history. Hence the per-component expected bit work, conditional on the actual earlier history, satisfies(6). No marginal-success product or unproved independence among component sizes is used.

Let M be the complete macro selected by the exact law and W(M)=sum_(nontrivial B in M)9^|B|. Summing the conditional component bounds and applying the tower property gives

E[decoding work | M] <= A P^12 (1+W(M)),

E[total work] <= A' P^12 (1+E_U W(M)).  (7)

The expectation in(7) is over the exact **bridge-conditioned** support macro, whose marginal is the macro law of the final uniform word. The additive1 includes scanning all isolates and producing the empty word when m=0. Preparation and macro selection contribute their unconditional polynomial bound. There is no need to condition the macro-selection running time on a rare completed macro. If such a conditional statement is desired, the number of rejected trials in an exact uniform integer draw is independent of its accepted integer, but(7) does not need that strengthening.

There is no deterministic finite worst-case fair-bit running time: an exact rejection loop may keep rejecting. Equations(5),(6) bound deterministic table/structural work; the full bit-cost statement is conditional expected time, as required by the mission.

Memory is separately exponential. Count keys/values cost O(Q(B+D)) bits. Transition lists cost at most O(Sv^2 D) bits. The explicit DFS stack costs O((ell+1)v^2 D), and the current literal child list and prefix are polynomial. All are bounded by A P^8 3^v bits. The full macro and polynomial C/Z tables remain resident, but only one exponential counter is live. Therefore peak storage is at most

A' P^8(1+max_(nontrivial B)3^|B|).  (8)

No polynomial worst-case memory bound is asserted. Since max3^|B|<=sum9^|B| for nontrivial components, any finite expected exponential-moment bound used in(7) also gives a corresponding expected peak-memory bound from(8). A sparse-regime proof must explicitly supply that expectation; it is not automatic from exactness.

## D6. Boundaries, source scope and remaining obligation

The target has no odd-length identity words; the API rejects odd m and positive m at N<2. It additionally accepts N=0,1 at m0 as the unique empty word. For all N,m0 it selects only isolates and builds no quotient counter. At m2 it chooses a uniform pair of labels and outputs the repeated edge. N2 has the unique edge repeated at every even length. A local singleton positive-length fiber is invalid; zero scalar or continuation weights are never normalized. Every nontrivial feasible(v,ell), including arbitrary high genus, remains eligible.

Historical counterexamples remain evidence. Quotient states retain exposed support, so they do not substitute ordinary81 counts for connected80. The local decoder covers zero-square words such as(ab)^3. The full law uses connected counts and exact macro weights rather than an unweighted support graph. The42/12→5/12 frozen-cutoff witness does not apply as a failure of this algorithm, because it has no cutoff; its positive branch is explicitly retained. H0/H1/H2 omitted-mass obstructions remain true for those restricted targets and do not refute an untruncated expected-cost calculation. The CP1 marginal-product claim remains rejected; only exact conditioning, conditional cost bounds and linearity/tower expectation are used here. Marked-cut parallel-core multiplicities belong to the preserved I1 structural route and are not a hidden step of this sampler.

Dependency graph: accepted DYZ scalar normalization -> C; elementary least-label disintegration -> Z and full macro law; accepted QC orbit invariant/transition decoder plus explicit LinearMemo accounting -> exact connected law and selected-component cost; full macro law + connected laws -> global exactness; conditional cost + **separately proved exact macro exponential moment** -> any expected-polynomial sparse theorem. The final expectation input is deliberately left to R1 and fresh joint review. No global all-length polynomial theorem or mission completion follows from this deliverable.

Author status: D1–D5 proved as proposed, pending exact-version review. The first unproved step for a sparse expected-polynomial corollary is the selected regime’s bound on E_U W(M); this role does not claim it independently. The elementary all-input exact-law and explicit exponential cost claims have no internal missing step identified by the author. Finite validation will be linked in report-v1.md once the reserved job completes; it cannot replace the universal arguments.
