# A polynomial mixing bound for literal transpositions in (S3)^k

Author status: **proved by the argument below**, pending independent review.
This is a new, self-contained argument, not a theorem attributed to a paper.
Finite checks in `check.py` are falsification attempts, not proof substitutes.

## 1. Exact statement and conventions

Partition 3k labels into k specified triples, k>=1. Let T be the 3k
transpositions whose two endpoints belong to the same triple. The generated
permutation group is G=(S3)^k, of order 6^k, in its disjoint-block action.
Fix even m>=2 and let Omega be all ordered words in T^m with product identity.
Composition is (ab)(x)=a(b(x)); the rightmost factor acts first. The target
pi is uniform on all of Omega, including every feasible triple occupancy.

Let n=m-1. Each step chooses a uniformly random slot i in {1,...,n} and:

- with probability 1/2 does nothing;
- with probability 1/8 applies H(a,b)=(b,bab);
- with probability 1/8 applies H^{-1}(a,b)=(aba,a);
- with probability 1/4, if a=b, replaces (a,a) by (s,s), s uniform in T;
  if a!=b, this branch does nothing.

Call this kernel K. Slots do not wrap around. All moves preserve product.
Signed Hurwitz maps are inverse permutations of Omega; square-refresh
off-diagonal probabilities are symmetric. Hence K is uniform-reversible and
at least 1/2 lazy.

**Theorem.** K is irreducible and

    gap(K) >= 1 / (200 k m^12).

For 0<epsilon<1 its worst-case total-variation mixing time satisfies

    t_mix(epsilon) <= ceil(200 k m^12
                            [ (m/2) log(3k) + log(1/epsilon) ]).

The bound is deliberately loose. Time counts individual local steps and is
polynomial in k=N/3, m, and log(1/epsilon), not in log N alone.
For m=0 there is one empty word; odd m gives no identity words. At m=2,
K=(3/4)I+(1/4)U on 3k doubled gates and has gap 1/4. The N=2
single-transposition model, outside this family, has a singleton at even m.

## 2. Exact conditional structure

Let 2c_j be the number of gates in triple j. Every c_j is a nonnegative
integer and sum_j c_j=M=m/2. Restricting the word to triple j gives an
identity word in S3: different triples commute and the group is a direct
product. Conversely these conditions suffice.

For even ell>=2 the number of S3 identity words is

    A_ell = 3^(ell-1),                 A_0=1.

Proof: writing x_i=t_1...t_i, each of the ell-1 internal prefixes can
independently be any of the three permutations of parity (-1)^i. Every
successive quotient is odd and therefore a transposition in S3. This is a
bijection, with x_0=x_ell=e. Under the uniform law all internal prefixes are
independent uniform coordinates.

Conditional on c, a word factors bijectively into a uniform color
interleaving with 2c_j occurrences of color j, and independent uniform S3
identity words of lengths 2c_j. Thus

    pi_bar(c) proportional to product_j w(c_j),
    w(0)=1,        w(r)=1/[3(2r)!] for r>=1.

The common factor m! 3^m cancels. In particular one must retain the factor
1/3 for each occupied triple; assigning that factor to empty triples is wrong.

In an S3 bridge of length ell, the probability that a specified adjacent
pair is equal is alpha_2=1 and alpha_ell=1/3 for even ell>=4. Equality is
equivalent to x_(i-1)=x_(i+1); at ell>=4 these are either two independent
uniform prefixes or one uniform prefix and a fixed endpoint. This also
handles the boundary slots.

## 3. The stationary-flow count projection

Use the stationary-flow projection, not an assertion that c(X_t) is itself
Markov for arbitrary initial distributions. For distinct j,h its exact
transition probability is

    K_bar(c,c-e_j+e_h) = g(c_j) / [12 k m(m-1)],

where

    g(0)=0, g(1)=6, g(r)=2r(2r-1) for r>=2.

Indeed, at a uniform full-word slot, the probability that both letters have
color j is (2c_j)(2c_j-1)/[m(m-1)]. Their conditional equality probability
is alpha_(2c_j). A square attempt has probability 1/4 and the new color
is h with probability 1/k. The numerator (2c_j)(2c_j-1)alpha_(2c_j)
is g(c_j)/3. Also g(r)=w(r-1)/w(r), verifying detailed balance directly.

The continuous-time complete-graph zero-range generator

    L f(c) = (1/k) sum_(j,h) g(c_j)[f(c-e_j+e_h)-f(c)]

satisfies K_bar=I+L/[12m(m-1)]. Its gap is at least 6. Here is a
self-contained coupling proof, so no literature theorem is assumed.

For neighboring c,d with c-d=e_u-e_v, couple all common departures at
each site, with equal destinations. At u, only c has excess departure rate
a=g(c_u)-g(d_u)>=6; at v, only d has excess rate
b=g(d_v)-g(c_v)>=6. Couple min(a,b) of those excess departures, using
one uniform destination for both. After such a joint departure the states
coincide. Unmatched excess departures move the single discrepancy or remove
it, never create a second discrepancy. Hence the half-L1 distance contracts
at rate at least 6. The path metric extension gives Wasserstein contraction
exp(-6t). Applied to a nonconstant eigenfunction (which has a finite,
positive Lipschitz seminorm on this finite space), this implies every
nonzero eigenvalue of -L is at least 6. Therefore

    gap(K_bar) >= 1/[2m(m-1)] >= 1/(2m^2).

For k=1 the projection is a singleton and its Poincare inequality is
vacuous; using the displayed lower bound remains valid.

## 4. Mixing inside each count fiber

Fix c and let K_c reject any proposed move changing c. Its stationary law
is the uniform fiber law pi_c. Every nonzero off-diagonal transition needed
below has probability at least 1/[12k(m-1)]: this holds for a within-triple
square refresh, a within-triple Hurwitz move, and a cross-triple swap.

Introduce a comparison chain F=(A+B)/2 on the conditional product space:

- A is the lazy adjacent-color shuffle: half hold, otherwise pick one of
  m-1 slots and swap the colors and their carried letters if the colors
  differ. Equal colors do nothing. All compressed triple words stay fixed.
- B, for every pair of consecutive letters in each compressed triple word,
  gives its exact S3 two-letter heat bath probability 1/m. The remaining
  probability holds. There are m-s such pairs, where s is the number of
  occupied triples, so this defines a Markov kernel.

In prefix coordinates B refreshes each independent ternary coordinate
with probability 1/m, hence has gap 1/m on that part of the product space.

For completeness, a crude uniform bound for A needs no sharp shuffling
theorem. Lift colors to m distinct cards. Every permutation has an adjacent
transposition expression of length at most D=m(m-1)/2. Choose one such
expression for each relative permutation z. Route each complete-refresh
transition sigma -> sigma z along the left translate of this expression.
For a fixed directed edge and fixed (z,path index), sigma is determined
uniquely. Summing path lengths gives load at most D^2/m!, whereas each
lazy adjacent-shuffle directed edge has capacity 1/[2(m-1)m!]. Thus its
gap is at least 1/[2(m-1)D^2]. Projecting to colors preserves that
Poincare bound. These flows use all translates; they do not funnel through
one canonical word. Conditional variance on the independent product gives

    gap(F) >= min(1/[4(m-1)D^2], 1/(2m)) >= m^(-5).

### 4.1 Shuttle comparison and polynomial congestion

An A transition is already a legal K_c cross-triple Hurwitz swap. Its
weight in F equals that swap's K_c weight, so its congestion is at most 1.

For a B update, let u<v be the original positions of two consecutive
occurrences of the same triple. Write the local segment as

    a C b,

where every letter of C belongs to another triple. Move a to the right
through C using commuting Hurwitz swaps, update the now adjacent pair
(a,b) to its chosen same-product pair (a',b'), and move a' back left
through C. This implements exactly the compressed-word heat bath. The
path has length 2(v-u-1)+1 <=2m and stays within the count fiber.
On an unequal S3 pair the nontrivial heat-bath choices are its two
Hurwitz neighbors; on an equal pair they are same-triple square refreshes.
Self transitions need no route.

Here is a bounded-preimage count for a fixed directed physical edge. Encode
the endpoints (u,v) and the phase of the shuttle, at most binom(m,2)*2m
possibilities. Before the central update the source word is recovered by
undoing a known partial shuffle and has at most three possible targets.
At the central update the physical edge identifies both local pairs.
After the central update recover the target by completing the known
shuffle; its original same-product pair has at most three possibilities.
Thus each encoding accounts for at most three source-target pairs. The
argument is a reconstruction, not an assumption about uniformly spread flow.

Each directed nontrivial B transition has weight 1/(3m), hence weight
1/(6m) in F. Because pi_c is uniform, the total length-weighted B load
at the physical edge is at most

    binom(m,2) * (2m) * 3 * [pi_c/(6m)] * (2m)
       <= m^4 pi_c.

Dividing by K_c capacity at least pi_c/[12k(m-1)] bounds the B
congestion by 12k m^5. Adding A gives at most 13k m^5. Therefore

    gap(K_c) >= 1/(13k m^10).

This proves within-fiber connectivity too. Singleton factors in the product
decomposition cause no exception to the Poincare argument.

## 5. Combining projection and restriction

For clarity, a direct variance argument avoids invoking a decomposition
theorem with unchecked normalization. Let V be the mean within-fiber
variance, B0 the variance of the fiber means, E the full Dirichlet form,
a a valid projection gap, and b a common valid restriction gap. Then

    V <= E/b.

For every cross-fiber edge expand the difference of fiber means into the
two endpoint deviations and the difference of actual function values.
The square of a sum of three terms is at most three times the sum of
squares. Reversibility and exit probabilities at most 1 imply

    a B0 <= 3E + 3V.

Consequently, since a,b<=1,

    Var_pi f = V+B0 <= [1/b+3/a+3/(ab)] E <= 7E/(ab).

Using a=1/(2m^2), b=1/(13k m^10) gives

    gap(K) >= 1/(182k m^12) >= 1/(200k m^12).

The positive Poincare bound also proves irreducibility, because a nonconstant
component indicator would have zero energy. Finally, |Omega|<=(3k)^m and
the standard elementary L2-to-TV inequality for a lazy reversible chain gives

    max_x TV(K^t(x,.),pi) <= (1/2) sqrt(|Omega|) exp(-t gap(K)),

which yields the theorem's mixing bound.

## 6. Dependencies, scope, and first unproved extension

All mathematical inputs used above are established here: S3 prefix
bijection, count weights and flow, the discrepancy coupling and its
eigenfunction consequence, translated permutation comparison, the shuttle
encoding, and variance decomposition. Only elementary coupling, Dirichlet
comparison, and spectral inequalities are used as general tools. Background
references are Levin--Peres--Wilmer, *Markov Chains and Mixing Times*,
Chapters 5 and 12--13 (first edition); the argument fixes its own constants.

No unproved lemma is needed for this restricted family. Independent review
of the new proof is still pending. The first unresolved step toward products
of larger symmetric groups is a polynomial bound for unrestricted-length
identity-word dynamics inside each growing block, together with suitable
count-process control; the ternary product-coordinate argument fails there.

The natural action preserves a public partition into triples. No gate joins
two triples, so this is not unrestricted S_(3k), a transitive growing action,
or a cryptographic pseudorandom-permutation construction. Crucially the
target does not fix the numbers of gates per triple: the zero-range part
proves their equilibration, including the creation and removal of occupied
triples. The proof is also not a gap bound for the repository's {3,4,5}
heat-bath kernel without an additional comparison.

There is a structural reason to consider block products. A transposition
alphabet closed under all its Hurwitz conjugations has a gate graph that is
a union of complete graphs: whenever (ab) and (bc) are present, conjugation
forces (ac), and shortening paths inductively completes every connected
component. Thus a connected Hurwitz-closed alphabet of literal
transpositions already contains all transpositions on its support. A
different connected sparse graph requires rejected moves or a changed move
set. This observation is proved directly and is not a mixing obstruction.

## 7. Boundary falsification attempts

- m=2: alpha_2 must equal 1, g(1)=6, and the actual chain is a global
  refresh with probability 1/4. Replacing g(1) by 2 would be wrong.
- m=0 and odd m: respectively singleton and infeasible; no slot is chosen.
- k=1: only the S3 word part survives; the projected variance is zero.
- Empty triples: w(0)=1 is essential; incoming square refresh is allowed.
- Each occupied triple has length two: its compressed word still has one
  ternary prefix coordinate, and recoloring squares changes occupancies.
- Long gaps between occurrences: shuttle lengths are bounded by 2m and
  the encoding includes both endpoints and the exact phase.
- Minimal connected S3 words have length four. The argument includes
  connected and disconnected supports, and never conditions on transitivity.
