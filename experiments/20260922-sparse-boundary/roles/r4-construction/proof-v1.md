# QC.v1: quotient support-state connected decoder

Status: proved by author, pending nonauthor audit. No asymptotic omitted-mass
claim is attached. Candidate H2-QC.v1 is separate from frozen H0 and H1.

## Target and policy

For N>=2, even m>=0, let P=N+m+2 and

    L=max{1<=v<=N : 3^v<=P^4}.

Compute L once at the top-level input. H2-QC.v1 allows isolates (1,0)
and every feasible connected identity component with size v<=L, of ANY
genus. Its target is exactly uniform on this declared subset D of Omega.
The modification targets arbitrary-genus components K<v<=L that H1 excludes
and whose genus>=2 part H0 excludes. Since 3^v<=v^(2v) for v>=2, L>=K.
H2 is not claimed to contain H0 because it omits low-genus components v>L.
A hybrid union with H0 is possible but is not this candidate's definition.

## Simultaneous-conjugacy invariant

An exposed literal prefix has product p and support partition pi. Every
cycle of p lies wholly inside a block of pi. For each support block take
the integer partition of the lengths of its p-cycles. Let q(p,pi) be the
sorted tuple of these sorted block partitions. Two pairs (p,pi) have the
same q iff a common relabeling of vertices conjugates p to p' and maps pi
to pi'. To construct the relabeling, match support blocks and then match
oriented permutation cycles of equal lengths. Thus this is a complete
orbit invariant, not merely the endpoint's cycle type.

Right-multiplication by every literal transposition is equivariant under
this relabeling, as is joining its endpoints' support blocks. The number
M(q,q') of literal edges producing successor q' is therefore independent
of the representative. It is a nonnegative integer, and its row sum is
binom(v,2). No group-orbit uniformity assertion about an MCMC is used.

Explicitly, within one support block an edge joins distinct permutation
cycles of sizes a,b with a*b choices for that indexed cycle pair; it splits
a cycle of size c into (a,c-a) with c choices for a<c/2 and c/2 choices for
a=c/2. Between distinct support blocks, an indexed a-cycle and b-cycle
merge and their support blocks merge, with a*b edges. Repeated blocks and
cycles are treated as separate indexed objects while adding transition
multiplicities; canonicalization then collects identical successors.

## Exact suffix counts and literal decoder

Let G(r,q) count suffixes of r transpositions which end at identity and
whose union with the exposed support is connected. Put

    G(0,q)=1{q consists of one block (1,...,1)},
    G(r,q)=sum_q' M(q,q') G(r-1,q').

The proof is disjoint first-letter decomposition. The initial state is v
singleton blocks, each containing a 1-cycle. It gives C(v,ell). A branch
with more than r+1 support blocks has count zero and may be pruned.

To produce LITERAL words, retain actual p and pi while using G only for
counts. For every actual edge e compute its actual child (p e,pi join e),
and select e with weight G(r-1,q(child)). All zero branches are ignored.
The denominator is G(r,q(p,pi)), by the orbit transition identity. For any
fixed connected identity word, multiplying these ACTUAL conditional
probabilities telescopes to 1/C(v,ell). The final boundary condition
forces both product identity and complete connected support. Random
integers are exact fair-bit rejection draws, with fewer than two trials
in expectation. The exposed-support regression survives: ((1,1),) and
((1,),(1,)) have the same endpoint cycle type but different G(0,.)=1 and0.

## State count

Every q has a canonical representation as a composition of compositions
of v: canonically order its blocks, then its cycles, recording all positive
cycle sizes. Encode the v units by v-1 separator slots, each either inside
a cycle, between cycles in one block, or between blocks. There are exactly
3^(v-1) such marked compositions. Decoding is unique before canonical
sorting, and the canonical representative encoding is injective. Therefore
there are at most 3^(v-1) quotient states, including unreachable ones.
This bound replaces v! Bell(v); it does not erase pi.

## Uniform expected polynomial bit cost

A conservative literal implementation may build transitions by a canonical
representative and scanning all O(v^2) edges, canonicalizing each in
O(v^2) label operations. The indexed-cycle implementation is faster but
not required by the proof. Across every v<=L and r<=m, at most
Q=(m+1)L P^4<=P^6 count keys arise. A transition list has at most O(v^2)
entries. Count values are bounded by binom(v,2)^r, hence have O((m+1)log P)
bits. Keys, multiplicities, exact edge counts and positive accumulated sums
have polynomially many bits. The explicit-stack evaluation strictly
reduces r, so no recursion-limit change is needed.

Even a deterministic dictionary simulated by linear scans of all Q keys,
O(P^4) label work per state, and schoolbook exact arithmetic fit the loose
fixed bounds expected O(P^24) bit time and O(P^12) bit storage. These
exponents deliberately dominate Q^2 P^4 times O(P^3) arithmetic/key work,
and literal decoding plus polynomial count/assembly tables. They do not
depend on an error exponent. Actual validation uses Python's dictionaries,
whose ordinary behavior is faster but is not assumed for the bound.

L itself is obtained by repeated exact multiplication by3 until crossing
P^4 or reaching N; no floating point or giant trial exponent is needed.

## Global assembly

Use the already checked polynomial connected count recurrence C(v,ell) and
least-label assembly with D(v,ell)=C(v,ell) on this fixed policy and0
otherwise. Explicitly:

 Z_D(n,t)=sum_(v,ell) binom(n-1,v-1)binom(t,ell)D(v,ell)Z_D(n-v,t-ell).

Select (v,ell) by those integer weights, its other labels and positions
uniformly, then use the literal connected decoder above. Each component
choice and interleaving is uniquely recoverable from a resulting word.
Its probability is 1/Z_D(N,m), as each step cancels to the residual count
divided by the current count. Thus exact global TV is 1-Z_D/Z. Nonemptiness
holds for all allowed inputs: L>=2 and a single repeated edge supplies any
even m. There is no conditioning rejection cost.

## Dependencies and first unproved step

The quotient decoder itself is elementary and imports no count formula.
Global assembly uses the checked historical DYZ C-table implementation;
its normalization/source is a load-bearing imported dependency. The exact
law and polynomial cost do not imply T0. The first missing result is a
uniform negligible bound on Pr_U[max component size>L] in the entire
m^4<=N^3 range. No such bound is proved here; a possible H0 obstruction
would not refute this separate candidate automatically.

Boundaries: m0 is the empty word; m2 uses a uniformly repeated edge; N2
has a unique edge for all even m; odd m or N1,m>0 has empty target. The
connected v1 decoder permits only ell0. Zero-count conditional branches
are rejected, never normalized. Near-minimal and high-genus words are
covered by the same exact recurrence.

## Subsequent negative result, R2-O2.v1

The missing T0 mass bound stated above is now refuted, not merely open.
The original proof paragraphs remain to preserve the construction history.
R2's corollary-h2-v1.md, independently checked in h2-obstruction-audit.md,
proves on N=2^(8j),m=2^(6j),j>=64 that
|D|/|Omega|<=2^(-1-jm/2). Consequently H2's global error tends to1.
The same conclusion holds after union with all genus0/1 components.
The exact conditional decoder theorem is unaffected; its role is a larger
small-support primitive, not a solution to T0.
