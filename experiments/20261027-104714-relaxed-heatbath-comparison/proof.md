# Correction gates resolve connectivity, but preserve the mixing difficulty

Author status: **proved** arguments below, provisionally recorded pending
independent review. General polynomial mixing is **unresolved**. No finite
spectrum or numerical convergence inference is used.

## 1. Models and the main comparison

Let T_N be all M=binom(N,2) transpositions. Products act rightmost first.
Let ell(g)=N-c(g), counting fixed-point cycles. The relaxed target is uniform
on A={w in T_N^m:ell(eval(w))<=2}, with N>=3 and even m>=2. Write H for
the half-lazy heat bath that chooses a uniform coordinate i and replaces
that gate uniformly among all legal gates, conditional on the other m-1.
The prior rejection kernel R instead proposes uniformly from all M gates
and rejects illegal choices. Both have exactly the same move graph.

Put L=m+2. On the SEPARATE uniform exact identity law on Omega(N,L), let

    Q = I/2 + (1/[2(L-1)]) sum_{i=1}^{L-1} H_{i,i+1},
    S = I/2 + (1/[2(L-1)]) sum_{i=1}^{L-1} H_{i,L},
    T = I/2 + (1/[2m]) sum_{i=1}^m H_{i,L-1,L}.

Here H_J refreshes exactly the named positions with uniform same-product
replacements, leaving ALL other gates fixed. In particular H_{i,L} does
not conjugate or reorder the intervening gates. These conditional kernels
are reversible projections. Q has linear adjacent slots, no circular seam.
All state choices and rejection handling are included in the definitions.

**Main proved comparison:** with deliberately loose constants,

    gap(Q)/(9 M^7 L) <= gap(H)
        <= 4 M^13 (L-1) L^3 gap(Q).                         (1)

Also gap(R)<=gap(H)<=M gap(R). Thus these two-error chains have
inverse-polynomial gaps in explicit N,m if and only if the exact adjacent
pair heat bath at length m+2 does. This is not an inverse-polynomial gap
bound for either chain. It is not a theorem about the original {3,4,5}
kernel without a separately supplied comparison to that kernel.

Both main laws are uniform and their state counts are at most M^L, so
the lazy spectral bound TV<=sqrt(M^L) exp(-t gap)/2 transfers any
inverse-polynomial gap to polynomial worst-case TV mixing. The usual
single-eigenfunction lower bound gives the converse polynomial implication.

**Unconditional S4 corollary.** At N=4 every even permutation has defect
at most two, so H is independent coordinate refresh with gap 1/(2m).
Substituting into (1), for every even L>=4 the EXACT identity adjacent-pair
chain has

    gap(Q on S4,length L) >= 1/[8 * 6^13 * L^5].          (1a)

It therefore mixes in O(L^6+L^5 log(1/epsilon)), with an explicit but
large absolute constant. This corollary is all-length at fixed degree
four; it is not a growing-N result or a claim of an optimized rate.
L2 has the direct uniform-pair refresh and L0 is the empty word.

All these moves are computable in polynomial time in N,m: the refreshes
involve at most three transpositions and can even be enumerated in M^3
trials. No arbitrary-length exact-bridge oracle is assumed. Polynomial
in N is not polynomial in the wire count log_2 N.

## 2. Legal-gate classification and rejection comparison

For a word A a B, temporarily delete a. Write h=BA, where A,B now denote
their permutation products. The endpoint A s B is conjugate to s h.
Since the current endpoint has even defect at most two, ell(h) is either
one or three. If ell(h)=1, all M replacements are allowed. If ell(h)=3,
s must split a cycle of h. There are exactly 6,4,3 choices when the
nontrivial cycle type is respectively (4), (3,2), or (2,2,2).

The legal set depends only on the other coordinates, so H is the exact
conditional heat bath for uniform A. On an off-diagonal move in a fiber
of size a, H/R=M/a, between 1 and M. Comparing Dirichlet forms under the
same uniform target proves gap(R)<=gap(H)<=M gap(R). Rejection overhead
therefore cannot by itself distinguish polynomial from superpolynomial
mixing in N,m.

## 3. Pair moves through one helper position

Consider positions i<j with intervening word B, product also denoted B,
and selected gates a,c. Define the contextual positive Hurwitz move

    F^+_{i,j}: a B c -> (B c B^-1) B (c B^-1 a B c).

It changes ONLY the two selected gates, and both remain transpositions.
The products agree because the displayed right side reduces to a B c.
Its inverse F^- is obtained by conjugating the ordinary inverse Hurwitz
move on the pair (B^-1 a B,c). Every F channel is an allowed conditional
pair move. This differs from the October 14 K_G operation, which modifies
the intervening gates. Only that work's exact-fiber connectivity argument
is imported here, not its nonlocal kernel formula.

Fix a final helper position h. Every adjacent Hurwitz move at i,i+1<h
is simulated, in chronological order, by

    F^+_{i+1,h}, F^{sign}_{i,h}, F^-_{i+1,h}.              (2)

To check this identity, write the selected triple as a,b,d after
conjugating the last gate by the fixed word between i+1 and h. The
positive sequence is

    (a,b,d) -> (a,d,dbd) -> (b,d,dbabd) -> (b,bab,d).

The negative middle move gives the inverse adjacent Hurwitz move. The
intervening word stays fixed throughout, so this triple calculation
applies at every separation.

For an adjacent square refresh (a,a)->(s,s), the corresponding sequence
is

    (a,a,d) -> (a,d,dad) -> (s,d,dsd) -> (s,s,d).         (3)

The middle step is a conditional pair refresh between i and h; it
preserves a d (d a d)=d=s d (d s d). The first and last steps are the
same contextual Hurwitz moves as in (2). Adjacent moves involving h
are already helper-pair moves.

Every adjacent two-factor conditional fiber has size M,3,2, or 1.
Its nontrivial transitions are square refreshes or signed Hurwitz moves.
Thus (2)--(3) simulate every Q transition using at most three S moves.

The exact fixed-endpoint pair graph is connected. For completeness, the
vertex-sweep proof is: move a v-incident edge right by Hurwitz moves,
eliminating v from the prefix until a square is found. A nonreduced word
must expose a square, because a completed square-free sweep would make
each remaining factor increase reflection length. Move each square to the
end, refresh it to a fixed edge, and repeat. A reduced remainder has a
unique sweep normal form, with terminal edge (v,g^-1(v)) when g moves v.
This is the self-contained argument in the October 14 nonlocal proof,
Section 3, and gives exact-fiber diameter <=2(N+3)L^2. We use this normal
form only for qualitative connectivity, not global congestion.

It follows from (2)--(3) that S is connected, with diameter at most
6(N+3)L^2, for every nonempty fixed-endpoint fiber.

## 4. All-length relaxed connectivity

**Proved:** for every N>=2 and even m, the whole space A(N,m,2) is
connected under single-gate legal replacements. This discharges the
boundary-access obligation left open in the October 26 report.

Any allowed prefix w can be extended to an exact identity word w u v:
factor eval(w)^-1 into two transpositions, using a repeated pair if the
endpoint is identity. Conversely every exact length-m+2 word has an
allowed length-m prefix. Each S move changes at most one prefix gate,
and the two trailing gates still correct its endpoint. Projecting an S
path between any two such extensions gives the required path in A.
The prefix graph diameter is at most 6(N+3)(m+2)^2.

The same qualitative argument applies to any correction budget. Choose
b<=k with b=m modulo 2, maximal with that parity. Whenever b>=1, pad a
minimal correction with repeated pairs to length b and use one of these
b correction positions as helper. S paths on length m+b exact words
project to legal single-gate paths with correction budget k. For even m,
every k>=2 therefore gives connectivity; for odd m every k>=1 does.
This says nothing quantitative about a growing budget's spectral gap.

Boundary cases: m0 has the empty word; N2 has at most one word at each
length. At even m and k0/1 the single-gate graph on exact words is frozen
except for singleton cases. Odd m,k0 is empty. At m2,k2 all words are
allowed and gap(H)=1/4 for N>=3. At N3/N4 and even m, k2 allows all words
and gap(H)=1/(2m). These exceptions agree with the construction.

## 5. The correction multiplicity must not be dropped

Write q=eval(w). The number a(q) of ordered correction pairs is

    a(id)=M;  a(three-cycle)=3;  a(two disjoint transpositions)=2.

Consequently the prefix marginal nu of UNIFORM exact length-L words is
proportional to a(q), not uniform on A. Uniform exact extensions must
not be claimed to give an exact uniform relaxed sampler. The density
ratio max(nu/pi)/min(nu/pi) is at most M, where pi is uniform on A.

The T chain DOES project to a Markov chain G on prefixes: each active
update refreshes both correction gates and one prefix gate, so the new
prefix gate has its conditional law under nu, proportional to a(q_new).
Thus G is half-lazy coordinate heat bath for nu. The S chain need not
have this projection property, and no such assertion is used.

For any two measures with density ratio between r_min and r_max, the
variational identity

    E_mu Var_mu(f | outside i) = min_{u(outside i)} E_mu (f-u)^2

compares their coordinate heat-bath Dirichlet forms between r_min and
r_max, and the same comparison holds for unconditional variance. Hence

    gap(H)/M <= gap(G) <= M gap(H).                       (4)

For an exact-extension observable f write f=E[f|prefix]+f_perp. Every
active T update kills f_perp, by conditioning first on the complete
new prefix. The holding half maps it to f_perp/2. Prefix observables
evolve exactly by G. Therefore gap(T)=min(gap(G),1/2)=gap(G): G is
half-lazy average of conditional projections and its nontrivial
eigenvalues are at least 1/2. The main regime has nontrivial prefix space.

## 6. Explicit polynomial comparison on the exact lifted space

All Dirichlet forms in this section use uniform Omega(N,L). For every
nontrivial pair transition the probability in Q or S is at least
1/[2(L-1)M]. Null steps can be omitted from paths.

### Q compared to S

Route each Q channel using (2)--(3), with length at most three. For any
fixed directed S edge, specify the adjacent index i, the path stage,
the source values at i,i+1,L, and the two destination adjacent gates.
There are at most 3 L M^5 such labels. All other positions remain fixed
throughout this route, so these labels and the current state recover
the source uniquely. Each source channel has probability at most
1/[2(L-1)]. Multiplying the channel bound by path length and dividing
by the minimum S capacity proves

    E_Q <= 9 L M^6 E_S.                                  (5)

This is an overcount of recoverable labeled paths, not routing all flow
through a normal form.

### S compared to Q

For a pair i,L, bubble the factor at i to L-1 using positive adjacent
Hurwitz moves. This is a bijective map A_i sending a B c to
B (B^-1 a B) c. Refresh the final adjacent pair, then undo A_i. The
result is exactly the conditional uniform pair update H_{i,L}, since
the intervening word remains fixed at the endpoints of the procedure.
The path length is at most 2L.

Fix a directed Q edge. Specify i, the stage, and the old and new central
pairs at the single refresh. There are at most 2 L^2 M^4 choices.
Before that refresh, the known bijective prefix recovers the source.
After it, invert the known suffix, restore the specified old pair,
then invert A_i. Thus the labels again recover at most one source.
Using channel probability <=1/[2(L-1)], length <=2L and the minimum
Q capacity gives

    E_S <= 4 M^5 L^3 E_Q.                                (6)

### T compared to S

Let a_i=E Var(f | outside {i,L}), b=E Var(f | outside {L-1,L}),
and c_i=E Var(f | outside {i,L-1,L}). Then a_i<=c_i and b<=c_i.
Consequently E_S<=E_T.

For the reverse direction, condition on all coordinates outside the
three-position block. Conjugating each selected transposition by the
fixed intervening products bijects this conditional fiber with a usual
three-transposition fixed-endpoint fiber. Its size s is at most M^3.
The half-lazy two-helper-pair heat bath on these three positions is
connected by Section 3, and its minimum nonzero transition is 1/(4M).
The elementary all-pairs path bound for a connected uniform s-state
chain of diameter <=s-1 gives gap>=p_min/s^2>=1/(4M^7).
Singleton conditional fibers have zero variance and need no gap convention.

Its conditional Dirichlet form is one fourth the sum of its two pair
conditional variances. Integrating this local Poincare bound gives
c_i<=M^7(a_i+b). Since m=L-2,

    E_S <= E_T <= M^7(L-1) E_S.                          (7)

Combining (4)--(7) and gap(T)=gap(G) proves (1). The intentionally large
exponents are harmless for polynomial equivalence; no sharp rate is claimed.
The only normal-form bound used quantitatively is on a THREE-factor
conditional fiber with at most M^3 states, not on a growing-length bridge.

## 7. Ordinary Hamming contraction is exactly refuted

Let x,y differ only at coordinate i. If L_j(x) is the legal set at j,
the optimal one-step transport distance for ordinary Hamming distance is

    W_1(H(x,.),H(y,.))
      = 1 - 1/(2m) + (1/(2m)) sum_{j!=i}
            TV(Unif L_j(x), Unif L_j(y)).                (8)

For a lower bound, sum the total variation distances of the individual
coordinate marginals of the two one-step laws. The i-th distance is
1-1/(2m); at every other coordinate it is the displayed scaled TV.
For the matching upper bound, use the same hold/update decision and
same update coordinate, and a maximal coupling of its legal-gate laws.
At coordinate i the conditionals coincide, so that discrepancy vanishes.
Thus (8) concerns the BEST coupling, not merely a failed chosen coupling.

For N>=6 choose disjoint a=(12), b=(56), c=(34), and even m>=4. Set

    x=(a,a,c,c,...,c),       y=(b,a,c,c,...,c).

x is exact and y has defect two. At every position all gates are legal
for x. At coordinate 2 all gates are also legal for y, but at each
j>=3 its legal set is exactly {a,b,c}. Therefore

    W_1 = 1 - 1/(2m) + ((m-2)/(2m))(1-3/M) > 1.        (9)

For N6,m4 this equals 43/40. A smaller constrained witness in N5 uses
a=(12), b=(23), c=(45), with four legal choices at j>=3, and gives
41/40 at m4. Exact rational one-step rows verify these values.

No fixed positive coordinate-weighted Hamming metric can contract
uniformly either: place the differing gate in a coordinate of minimum
weight, put its paired a in any other position, and put c elsewhere.
The gain from the m-2 affected coordinates is at least (m-2)(1-3/M)
times that minimum weight, larger than the possible loss. All these
gates commute in the N>=6 witness, so reordering positions preserves it.

This refutes one-step Hamming and fixed-coordinate-weight contraction,
not polynomial mixing. State-dependent metrics, multi-step couplings,
or a direct Poincare argument remain possible. The first missing step
is now quantitative; general connectivity is no longer missing.

## 8. Dependencies, checks and limits

The fixed-endpoint vertex sweep from HB-NONLOCAL-LIFT is the only
substantial project input; its constructive proof is summarized above.
All conjugation identities, multiplicity correction, conditional projection,
Dirichlet comparisons, and Hamming transport witnesses are derived here.
No new external literature theorem or asymptotic empirical inference is used.

The harness checks both routed directions exhaustively on six identity
fibers, including required S3,m4 and S4,m4,m6 and constrained-lift S5,m6.
It checks every three-factor endpoint fiber through S5, legal conditional
sets in four relaxed spaces, correction counts against independently
enumerated extended bridges, and direct selected-triple rows in S3/S4.
The Hamming witnesses are evaluated by exact rational full transition rows.

The comparison is for the fixed budget TWO. General-budget connectivity
extends as in Section 4, but correction-word multiplicities and local
conditional sizes can cost powers depending on k. Formula (1) is not
asserted for k=C log N. General rapid mixing of H, R and Q remains open,
and this author proof still requires independent mathematical review.
