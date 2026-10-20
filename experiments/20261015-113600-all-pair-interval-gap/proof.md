# Arbitrary-position lifted moves: comparison and an S3 gap

Author status: **proved** statements below, pending independent review.
**Unresolved:** inverse-polynomial mixing for growing N, including a full
N-cycle at m=N+1. These are the actual pair kernels, not a replacement
global-refresh algorithm. Products act rightmost first.

## 1. Target, moves and exceptional cases

The target is uniform pi on ordered words Omega_g(N,m) of m transpositions
in S_N with product g. Assume a nonempty fiber and m>=2. Put
M=binom(N,2), d=m-1, C=binom(m,2). There are no cyclic boundary windows.
Write H_k^+(a,b)=(b,bab), H_k^-(a,b)=(aba,a), and let R_k replace an
equal adjacent pair (a,a) by (s,s), s uniform among all M transpositions;
otherwise R_k holds. H_k averages the two signs. Set

    L_k=I/2+H_k/4+R_k/4,       K_A=(1/d) sum_k L_k.

For i<j, T_ij is the chronological sequence H_i^-,...,H_(j-2)^-.
It sends a B b to (a B a) a b. The kernel L_ij applies T_ij, then
L_(j-1), then the inverse shuttle. Define

    K_G=(1/C) sum_(i<j) L_ij = I/2+H_G/4+R_G/4.

Its explicit nonlocal channels are

    F_ij^+: a B b -> b [ba B ab] (bab),
    F_ij^-: a B b -> (aba) [ab B ba] a,
    R_ij(s): a B a -> s [sa B as] s,

with R_ij holding on unequal endpoints. Brackets mean conjugating EACH
middle gate, not inserting gates. Every pair is selected uniformly,
including disjoint or equal gates; signs and new transpositions are uniform.

Each shuttle is a state permutation; L_k is uniform-reversible. Therefore
L_ij and K_G are uniform-reversible. Connectivity with square refresh is
proved constructively in the prior nonlocal-lift proof, Section 3, and
K_G contains every adjacent move. No external classification is needed.

Pure H_G alone cannot sample every endpoint fiber: it preserves the
generated subgroup, as every elementary Hurwitz step does. For example
((12),(12)) and ((13),(13)) are distinct frozen identity words. The
theorems here include the square-refresh branch.

N=2 and nonempty fibers at m=0,1 are singletons, so mix in zero steps.
N=1 permits only m=0. Feasibility for N>=2 is m>=N-c(g) with matching
parity; identity has no odd-length words. No gap is assigned to empty
fibers, and nontrivial-gap statements exclude singleton fibers.

## 2. All-N comparison with no dependence on the number of gates

**Theorem (proved).** For every N and every nontrivial feasible fiber,

    (2/m) E_(K_A)(f,f) <= E_(K_G)(f,f) <= 4m^2 E_(K_A)(f,f).       (1)

The same inequalities hold for spectral gaps. Thus polynomial relaxation
and mixing in N,m hold for these two kernels simultaneously. This does
not establish either property in general. It strengthens the earlier
8M(M+1)m^3 upper comparison by using stationary path marginals.

Proof. The lower bound retains only adjacent pairs; d/C=2/m. For the
upper bound start X_0 uniformly and realize a single L_ij transition by
the shuttle, its random middle update, and the reverse shuttle. The path
length is ell_ij=2(j-i)-1. EVERY intermediate state is uniform: shuttles
are bijections and the middle update preserves pi. This also holds after
the random square update; no inverse-source counting is required.

For a deterministic Hurwitz sign, its quadratic increment form is the
same for both signs, by changing variables through the inverse map.
Thus it is E_(H_k) <= 4 E_(L_k). Cauchy-Schwarz along the path, followed
by averaging, gives

    E_(L_ij) <= ell_ij [8 sum_(k=i)^(j-2) E_(L_k) + E_(L_(j-1))].

For a fixed k, the sum of ell_ij over shuttle occurrences is

    sum_(i<=k, j>=k+2) [2(j-i)-1] = m k (m-k-1),

and its sum over middle occurrences j=k+1 is k^2. Averaging over pairs
and using sum_k E_(L_k)=d E_(K_A), the comparison constant is at most

    max_(1<=k<=m-1) [16 k(m-k-1) + 2k^2/m] <= 4m^2.

This proves (1). It is a bounded stationary-flow comparison, not an
argument from move length or diameter alone. Both chains are half-lazy,
and log |Omega_g| <= m log M; standard finite-state L2-to-TV estimates
give the stated equivalence of polynomial mixing. Polynomial in N is
not polynomial in a wire count log_2 N.

## 3. Independent coordinates for S3

Represent S3 on F_3, with its three transpositions

    r_a(x)=-x+a,       a in F_3.

For w=(r_(a_1),...,r_(a_m)), the prefix product is

    p_k(x)=(-1)^k x+b_k,       b_k=sum_(l=1)^k (-1)^(l-1) a_l.

Fixing the endpoint fixes b_m and the parity. The m-1 internal b_k are
arbitrary, with each choice giving exactly one word. Consequently

    y_k=(-1)^(k-1) b_k,       1<=k<=m-1,

are independent uniform ternary coordinates under pi.

For a selected pair i<j, write a=a_i, b=a_j. The plus move adds
delta=b-a to both selected gate parameters and adds 2delta=-delta to
every intermediate gate parameter. Its prefix-coordinate effect is

    y_k -> y_k+delta   for i<=k<j,       other y_k unchanged.      (2)

The minus move uses -delta. If a=b, both Hurwitz signs hold, while a
square refresh to r_s gives exactly (2) with delta=s-a uniform in F_3.
These identities follow either from r_b r_a r_c r_a r_b=r_(c+2(b-a))
or by summing the alternating prefix parameters. They remain valid for
the boundary pair (1,m), with the endpoint unchanged.

Define the AUXILIARY comparison kernel

    Q=I/2+(1/(2C)) sum_(i<j) U_ij,

where U_ij adds a uniform delta in F_3 to all y_i,...,y_(j-1).
This is the all-pair transported exact two-factor heat bath in S3.
It is used to analyze the actual K_G, not substituted as the requested
algorithm. On each interval's three-state line:

- If a=b, K_G's nontrivial channel mass is 1/12 per pair, versus
  Q's 1/6: ratio 1/2.
- If a!=b, each signed Hurwitz move has mass 1/8 per pair, versus
  Q's 1/6: ratio 3/4. Along this line b-a stays nonzero.

Summing channels, including coincident destinations from different pairs,

    (1/2) E_Q <= E_(K_G) <= (3/4) E_Q.                           (3)

## 4. Exact auxiliary gap and the actual-chain theorem

**Theorem (proved).** For N=3, every feasible endpoint, and m>=2,

    gap(Q)=1/m,
    1/(2m) <= gap(K_G) <= 3/(4m).                                (4)

In particular the ACTUAL all-pair Hurwitz/square walk has relaxation
time Theta(m), and for 0<epsilon<1/2,

    t_mix(K_G,epsilon)
      <= ceil(2m [(m-1)log(3)/2 + log(1/epsilon)]).               (5)

Proof. The characters chi_z(y)=exp(2 pi i <z,y>/3), z in F_3^(m-1),
diagonalize Q. An interval update preserves this character if its
interval sum of z is zero, and kills it otherwise. Put
s_0=0, s_k=z_1+...+z_k. If D(z) counts unordered pairs of distinct
values among the list s_0,...,s_(m-1), then

    1-lambda_z(Q)=D(z)/(2C).

For nonzero z, the list is not constant. If n_0,n_1,n_2 are its value
counts, then D=(m^2-sum n_a^2)/2 >= m-1; the largest possible sum of
squares of a nonconstant list is (m-1)^2+1. Equality occurs for
z=(1,0,...,0). Hence the gap is (m-1)/(2C)=1/m. Real and imaginary
parts give real eigenfunctions if needed. Equation (3) gives both sides
of (4). The state count is 3^(m-1); applying the half-lazy spectral
TV bound and (4) proves (5).

No growing-N assertion follows: for N>=4, the parity class contains
nontranspositions, so arbitrary internal prefixes are no longer allowed.
The independent ternary-coordinate argument then fails.

## 5. Scope, falsification and first unresolved step

The elementary two-factor S3 case matches the exact gaps: 1/4 for the
identity endpoint and 3/8 for a three-cycle, both within (4). The checks
exhaust all S3 words at m=2,...,7, exact Fourier modes through m=9, and
the specified identity fibers in S4. They test formulas and constants;
the all-m and all-N proofs above supply the completeness arguments.

For the motivating full N-cycle at m=N+1, (1) applies, but an
inverse-polynomial gap remains **unresolved**. The first missing lemma is
a uniform Poincare inequality Var_pi(f)<=poly(N) E_(K_G)(f,f) on that
family. Arbitrary-position moves neither disprove nor prove it, and (1)
shows it is equivalent up to polynomial factors to the adjacent gap.
Uniformly choosing only currently available incident pairs defines a
different kernel and needs its state-dependent correction.

Dependencies: (1)--(5) use elementary finite-state algebra, stationarity,
Cauchy-Schwarz and Fourier characters; no external theorem about Hurwitz
transitivity or literature mixing is used. All-endpoint connectivity and
feasibility are imported from the constructive prior proof
`../20261014-111117-nonlocal-graph-lift/proof.md`, Sections 1--3.

Manuscript-ready statement, pending independent review: On the uniform
fixed-endpoint length-m transposition fiber in S3, the half-lazy walk
choosing a uniformly random position pair, with equal Hurwitz and
transported square-refresh branch weights, has gap between 1/(2m) and
3/(4m). The proof identifies its transported two-factor heat bath with
uniform interval translations on F_3^(m-1), whose gap is exactly 1/m.
For arbitrary S_N the same pair walk and its adjacent version have
Dirichlet forms comparable between factors 2/m and 4m^2; this comparison
alone supplies no growing-N gap bound.
