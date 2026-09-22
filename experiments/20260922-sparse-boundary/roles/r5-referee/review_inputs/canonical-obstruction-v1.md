# Canonical H0 boundary obstruction — SB-O1.v1

Audit disposition of these exact bytes is recorded in claim_ledger.md. This
is a count argument about unchanged H0, not a hardness result or a
refutation of the existence target T0. The load-bearing genus majorant is
rederived from the checked primary source in source_checks.md. Canonical
synthesis preserves the frozen R2-O1 mathematical argument; complete
nonauthor reports remain in their role directories. Internal same-model
review is correlated and is not external human certification.

## Frozen model and claim

Let N>=2, m=2k>0. All labels and word positions are distinguished. Products
act rightmost first. Let Z=|Omega(N,m)| and Z_A=|A|, where A consists of
identity words whose nontrivial support components satisfy g<=1 OR v<=K,
with K=max{v<=N:v^(2v)<=(N+m+2)^4} fixed at the original input. The sampler
H0 has law Unif(A), so its exact error is 1-Z_A/Z. No Markov kernel is used.

**Claim R2-O1.** For every integer j>=64, set

    N=2^(8j), m=2^(6j).

Then m is even, m^4=N^3, and

    Z_A/Z <= 2^(-1-jm/2).

Thus H0 error tends to one on a subsequence of the benchmark. This refutes
P0. Since B subset A, it also refutes P1. It says nothing against another
algorithm satisfying T0. In fact m is exactly m_*(N) on this sequence.

## Inputs and dependency graph

1. Elementary unique decomposition of an identity word into its connected
   support words and order-preserving position interleaving.
2. C(v,2v-2+2g)/(2v-2+2g)! <= v^(v-3) b_v^g/g!, where
   b_v=(v^3-v)/36. This is SG-T1.v1 equation(3), whose derivation from the
   DYZ positive recurrence is in the hash-frozen September22 proof. It is
   uniform over all integer g>=0. Coordinator source_checks.md records the fresh source audit.
3. The September5 subgroup return bound Z(N,m)>=2*binom(r,2)^m/r!
   for even m>0,2<=r<=N. An elementary proof is repeated below to close
   the imported argument in the exact current convention.
4. Standard coefficient positivity and elementary factorial inequalities.

No sequential conditional probabilities or independence assumptions are
multiplied. The normalizer is the actual endpoint-conditioned word count.

## A finite H0 numerator bound

Write A_g(v)=C(v,2v-2+2g)/(2v-2+2g)!. For real x>0 define

    S_A(x)=sum_(v=2..N) N^v/v! *
           sum_(g>=0: g<=1 or v<=K) A_g(v) x^(v-1+g).

This is a well-defined finite sum over v of entire series in x: each fixed-v
component count is bounded by binom(v,2)^ell. We can alternatively truncate
all component costs at k before any coefficient comparison, then dominate
by the convergent expressions below. No divergent all-genus sum over
unbounded v is evaluated.

For component multiplicities a_(v,g), the exact normalized word count is

    (N)_s product_(v,g) [A_g(v)/v!]^a_(v,g) / a_(v,g)!,
    s=sum v a_(v,g), sum (v-1+g)a_(v,g)=k.

This includes arbitrary genus on every size-v<=K component. Bounding
(N)_s<=N^s, then allowing profiles with s>N, gives coefficientwise

    Z_A/m! <= [x^k] exp(S_A(x)).

Consequently Z_A/m! <= x^(-k) exp(S_A(x)) at every positive x. In this
display the coefficient notation refers to a formal variable first; the
last expression evaluates the series at the chosen positive real x.

Set x=k/N^2, q=3Nx and suppose

    q<=1/2, x<=1, b_K x<=1.                         (F)

For v<=K the genus sum is at most exp(b_K x), using the full factorial
majorant, while for v>K it is at most 1+b_v x. Thus for every v, it is
at most exp(b_K x)+b_v x <=3+b_v x. Therefore

    S_A(x) <= 3 S_0(x)+S_1(x),
    S_0=sum_(v=2..N) N^v/v! v^(v-3) x^(v-1),
    S_1=sum_(v=2..N) N^v/v! v^(v-3) b_v x^v.

Since v! >= (v/e)^v > (v/3)^v,

    S_0 <=3N sum_(v>=2) q^(v-1)/v^3
        <=3N q/[8(1-q)] =9k/[8(1-q)],
    S_1 <=(3Nx/36) sum_(v>=2) q^(v-1)(1-1/v^2)
        <=3Nx q/[36(1-q)] =kx/[4(1-q)].

Under (F), S_A <=27k/4+k/2=29k/4<8k. We have proved the finite bound

    Z_A <=m! (N^2/k)^k exp(8k).                     (U)

The bound is deliberately loose and need not be numerically informative
at small parameters. Its role is to certify an asymptotic count scale.

## Verification of (F) on the exact subsequence

For j>=1, m=2^(6j), N=2^(8j), k=2^(6j-1), x=2^(-10j-1).
Then x<=1 and q=3*2^(-2j-1)<=3/8<1/2.
Also P=N+m+2<=2N. Since K>=2 and log_2 K>=1,

    2K <=2K log_2 K<=4 log_2 P<=32j+4,
    K<=16j+2.

Thus

    b_K x <= (16j+2)^3/[72*2^(10j)]<1.

At j=1 the right side is5832/73728<1. Its consecutive ratio is
((16j+18)/(16j+2))^3/1024<8/1024<1. Therefore (F), and hence(U), holds
for every integer j>=1, without floating rounding or a changing cutoff.

## Exact denominator comparison

For a fixed r-subset, let p be the midpoint distribution after m/2 steps
of the uniform all-transposition walk on S_r. Symmetry gives the return
probability at m as sum_sigma p(sigma)^2. The midpoint is supported in
one parity class of size r!/2. Cauchy-Schwarz therefore gives return
probability >=2/r!, including r=2. Those words embed in S_N, proving

    Z(N,m)>=2*binom(r,2)^m/r!.                       (L)

This audits the September5 input without upgrading its former minimal-only
conclusion. The new work is the full H0 numerator bound(U).

For the subsequence choose r=floor(m/(6j)), using exact integer division.
For j>=1, m/(6j)>=2, so

    2<=r<=N, r>=m/(12j),
    binom(r,2)>=r^2/4>=m^2/(576j^2),
    r!<=r^r<=m^r<=m^(m/(6j))=2^m.

Substitution into(L) gives

    Z>=2 [m^2/(1152j^2)]^m.                        (D)

On the other hand m!<=m^m and k=m/2 transform(U) into

    Z_A<=[sqrt(2) exp(4) N sqrt(m)]^m.

Combining these bounds, using N/m^(3/2)=2^(-j), yields

    Z_A/Z <=(1/2)[1152 sqrt(2) exp(4) j^2 2^(-j)]^m
           <=(1/2)[2^18 j^2 2^(-j)]^m.             (R)

Indeed sqrt(2)<2 and exp(4)<3^4=81, so the constant is below
186624<262144=2^18. For every integer j>=64,

    2^18 j^2 <=2^(j/2).

At j64 this is 2^30<=2^32. The ratio of the right side to left side
increases at each subsequent integer step because sqrt(2)>(65/64)^2
and ((j+1)/j)^2 decreases. This proves R2-O1 from(R).

## Boundaries and first remaining obligation

m0 gives the unique empty word. m2 gives a repeated transposition, allowed
by H0. At N2 every positive even identity word uses the unique edge and is
allowed by H0. Odd m and positive lengths at N1 have empty target; N1,m0
is exact. These facts do not contradict the asymptotic subsequence. A
connected component is feasible exactly at ell=2v-2+2g, and both minimal
and genus1 components, including arbitrarily large v, were retained in
the numerator. No edge or near-minimal branch was discarded.

No unproved internal inequality is used beyond the explicitly checked
published count input. Exact current-version acceptance is recorded in the
append-only ledger, with source, coefficient, label, constant and finite-test
audits. T0 remains unresolved: failure of H0/H1 does not rule out another
polynomial-time global sampler.
