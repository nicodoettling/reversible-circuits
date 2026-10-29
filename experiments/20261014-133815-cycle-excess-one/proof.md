# The original pair walk at excess one: bounds and an obstruction

Author status: **proved** scoped results below, pending independent review.
**Unresolved:** polynomial mixing of the original growing-N full-cycle
walk at m=N+1. A separately proved fast global-refresh hybrid is in
[tree_jump_proof.md](tree_jump_proof.md); its kernel is not substituted here.

## 1. Exact kernels and targets

Products act rightmost first. Let T_N be all M=binom(N,2) transpositions,
and Omega_g(N,m) the ordered length-m words computing a fixed g. Uniform
on this fiber is the target. For m>=2 write

    K_A=I/2+H_A/4+R_A/4,   K_G=I/2+H_G/4+R_G/4,   P=(K_A+K_G)/2.

H_A chooses a uniform linear adjacent slot and a uniform sign, using
(a,b)->(b,bab) or its inverse (aba,a). R_A chooses a uniform adjacent slot,
refreshes (a,a) to (s,s) for uniform s in T_N, and otherwise holds.
No cyclic boundary window is used.

K_G chooses a uniform pair i<j among C=binom(m,2) pairs. On a B b, its
signed Hurwitz maps are

    a B b -> b (ba B ab) (bab),
    a B b -> (aba) (ab B ba) a.

The notation q B q^{-1} conjugates each intervening gate. The square map
on equal endpoints is a B a -> s (sa B as) s, for uniform s, and it holds
otherwise. The two Hurwitz maps are inverse bijections, and square
channels reverse by choosing the former gate. Thus all three kernels
are uniform-reversible and half-lazy. Each macro is a Hurwitz shuttle,
one adjacent update, and the inverse shuttle; it uses <=2m-3 primitive
moves. These facts and all-endpoint connectivity are proved in the
[prior proof](../20261014-111117-nonlocal-graph-lift/proof.md), Sections 1-3.

The principal family here is g=c=(0 1 ... N-1), m=N+1, N>=2. Every word
has connected support. In Section 2 alone g is any feasible endpoint
of S_3 and m is arbitrary. Empty fibers are excluded. N=2 gives a unique
word at each feasible length. m=0,1 give singleton or empty fibers. Full
cycles require m=N-1 modulo 2, not necessarily even m; m=2 for a full
cycle is the minimal S_3 case. Identity odd-m fibers are empty.

## 2. Actual walk theorem on S_3, all lengths and endpoints

**Theorem (proved).** For N=3, m>=2, every g with sign(g)=(-1)^m, and
d=m-1,

    gap(K_A)>=1/(4d),        gap(P)>=1/(8d),
    t_mix(K_A,epsilon)<=ceil(12d log(d/epsilon)),
    t_mix(P,epsilon)<=ceil(8d [(d/2)log 3+log(1/epsilon)]).

Proof. Prefixes p_i=t_1...t_i have fixed parity. Every odd permutation
in S_3 is a transposition, so arbitrary choices of the d internal prefixes
in their three-element parity classes give exactly one word, using
t_i=p_(i-1)^{-1}p_i. Thus the uniform bridge is an independent uniform
ternary product measure. A two-factor conditional refresh is exactly a
single-prefix refresh.

The half-lazy random-coordinate refresh Q has gap 1/(2d): tensor
products of constants and zero-mean coordinate functions diagonalize it,
with eigenvalues 1-k/(2d). For an equal adjacent pair, K_A's off-diagonal
probability is one half of Q's; for a distinct pair it is three quarters.
Indeed there are three factorizations of each feasible two-factor product;
the two Hurwitz directions give the other two in the distinct case.
Dirichlet-form comparison proves the gaps. The displayed P mixing bound
uses |Omega_g(3,m)|=3^d and the lazy reversible spectral inequality.

For the sharper K_A bound, its exact prefix-coordinate decomposition is:

- probability 5/8: hold;
- probability 1/4: uniformly refresh a uniform internal prefix;
- probability 1/8: choose a uniform internal prefix; refresh it uniformly
  only when its two neighboring prefixes differ, otherwise hold.

The endpoints p_0=id,p_m=g stay fixed. Neighboring prefixes in this test
have the same parity, so equality is well-defined. Couple configurations
differing only at position k by the same branch, coordinate and fresh
value. The unconditional-refresh branch removes that discrepancy with
probability 1/(4d). In the conditional branch, only positions k-1,k+1 can
create a new discrepancy: each has probability at most (1/(8d))(2/3).
The conditional update at k has the same activation in both copies and
can only help. Hence the expected Hamming distance is at most
1-1/(12d). Boundary positions have fewer possible discrepancy births.
Extend these neighboring couplings along shortest Hamming paths and
iterate the resulting Wasserstein contraction. Since the diameter is d,
TV is at most d exp(-t/(12d)), proving the bound. This is an actual
local-chain theorem, but N is fixed at 3.

## 3. Repeated-edge exposure at m=N+1

For w let Y(w) count unordered equal position pairs, and X(w) count equal
adjacent pairs. Write F_0=N^(N-2) and
F_1=N^(N+1)(N^2-1)/24, from the checked fixed-cycle count normalization
in tree_jump_proof.md, Section 5.

**Lemma (proved).** Under the uniform genus-one full-cycle law,

    0<=Y<=3,                    E Y=6/N,
    Pr(t_i=t_j)=12/[N^2(N+1)]   for EVERY i<j,
    E X=12/[N(N+1)],
    Pr(X>0)=12(N^2-2)/[N^3(N+1)],
    2/N <= Pr(Y>0) <= min(1,6/N).

Proof. A connected support has at least N-1 distinct edges. There are
only two excess occurrences, so the largest Y is attained by one tripled
edge and equals 3. For a specified adjacent pair, deleting equal gates
gives a minimal word; insertion of any s,s reverses this bijection. There
are M F_0 possibilities. For a nonadjacent pair, the fixed Hurwitz shuttle
that moves the first gate unchanged to immediately before the second is
a bijection preserving their literal equality. Thus all pairs have the
same probability M F_0/F_1, which gives the expectations. Two disjoint
adjacent squares would delete four gates and contradict minimal length.
Consequently X<=2, and X=2 occurs precisely at a triple a,a,a. Expanding
one gate in a minimal word gives all such words uniquely, so their number
is (N-1)F_0. Therefore Pr(X>0)=E X-Pr(X=2), giving the formula. Finally
Y/3<=1_{Y>0}<=Y proves the last bounds.

In particular a typical large-N word has no repeated edge at all. Merely
choosing a uniform pair from all positions does not increase the average
square-update success: both R_A and R_G change the word with probability

    (1-1/M) 12/[N^2(N+1)]

at stationarity. Graph-aware selection of an AVAILABLE pair is a different
proposal and needs a correction.

## 4. Balanced graph selection accelerates the square branch

Define R_* by holding when Y=0. Otherwise choose an equal pair uniformly
among the Y choices, choose s uniformly from T_N, perform its transported
square replacement to w', and accept with

    min(1,Y(w)/Y(w')).

The selected pair is still equal in w', so Y(w')>=1. Reverse the channel
at the same pair by choosing the old gate. Detailed balance holds with
uniform target. A nontrivial accepted channel has probability
1/[M max(Y(w),Y(w'))], versus 1/(MC) in R_G. Thus at m=N+1,

    (C/3) E_(R_G) <= E_(R_*) <= C E_(R_G),

and every proposed replacement is accepted with probability at least 1/3.
Here these are Dirichlet forms of the square branches alone; neither
branch is by itself irreducible. At stationarity R_* changes the word
with probability between (1-1/M)2/N and (1-1/M)6/N. This is a
Theta(N^2) acceleration of this branch relative to uniform-pair scanning.

Let K_G*=I/2+H_G/4+R_*/4, and P_*=(K_A+K_G*)/2. Both are
uniform-reversible and half-lazy; P_* has gap at least gap(P), because
C>=3 in this family. **Unresolved:** a polynomial lower bound for either
gap at growing N. The branch comparison does not turn into an N^2
improvement for the full gap without controlling the Hurwitz directions.
The 1/3 acceptance bound is specific to this genus-one full-cycle family,
not a claim for arbitrary identity words.

## 5. Exact support multigraph restrictions can be frozen

**Obstruction (proved).** For every N>=3, there is a labeled support
multigraph whose restricted K_A, K_G, P and P_* chains have at least two
isolated states. Restriction means rejecting every move leaving the fiber.

Let the reduced star word be

    r=((0,N-1),(0,N-2),...,(0,1))=(a,b,T),

which computes c. The distinct words

    w_1=(a,a,a,b,T),      w_2=(a,b,a,a,T)

both compute c, have length N+1 and share the same exact support
multigraph: spoke a has multiplicity three, every other spoke one.
Every nontrivial Hurwitz update on two distinct spokes creates an edge
between leaves in one selected position, so leaves this fiber. Equal-pair
Hurwitz updates hold, including their middle conjugations. The only
repeatable square is a; replacing it by s!=a creates two occurrences of
s, although the required multigraph has at most one. No middle change
can remove those two selected occurrences. Such a refresh also exits.
Therefore each witness is isolated in the restriction.

This refutes the proposed proof step that all EXACT MULTIGRAPH fibers
mix under rejected-exit restrictions. It does not refute full-chain fast
mixing, nor address fibers that forget multiplicities or vertex labels.
A different partition, excursions outside fibers, or a flow proof is needed.

## 6. The first unproved step and dependency ledger

One sufficient standalone missing lemma for the user-requested growing-N
result is:

> There are constants A,b independent of N such that for every real f
> on Omega_c(N,N+1), Var_pi(f)<=A N^b E_P(f,f).

A more specific comparison route uses the proved Q_1 in tree_jump_proof.md:
establish E_(Q_1)(f,f)<=N^{O(1)} E_P(f,f) by recoverable, bounded-congestion
routes. Since gap(Q_1)=1/[3(N-1)] on nontrivial fibers, that would finish
the conjecture. The available polynomial-length normal-form routes do
not prove this inequality; their load can concentrate. Fixed-multigraph
restriction gaps cannot supply it because Section 5 gives zero gaps.

Dependencies: the precise macros and connectivity use the internal prior
nonlocal proof; F_0,F_1 use the explicitly normalized literature count and
minimal codec listed in tree_jump_proof.md. The S_3 proof, collision
inequalities, balanced-channel comparison and star obstruction are given
here without external classification assumptions. Every positive claim
is same-author proof work, not independently certified. No manuscript or
existing accepted result is silently upgraded.

## 7. Exact falsification checks

`check.py` verifies genus-one counts and every fixed-pair collision count
for N=2,...,5; exact rational reversibility of R_* and the channel
comparison for N<=4; all macro channels on the two star witnesses for
N=3,...,12; all feasible S_3 endpoints for m=2,...,7; and the explicit
coupling inequality for d=1,...,5. Identity regressions pass at S_3,m=4
and S_4,m=4,6. Word endpoints, equal-pair/adjacent-square statistics and
support multiplicities are checked exactly, not by a time-series claim.
See results.json. These finite checks falsify implementations or formulas;
the proofs above, not finite spectra, establish their asymptotic scope.
