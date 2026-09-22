# Independent analytic proof R2-A.v1

Frozen 2026-09-22 at 05:52 UTC. Status: **proved candidate / provisional pending nonauthor audit**. This derivation was made before reading any R1 proof. Parent subsequently reported agreement with the factorial-majorant idea; that does not count as independent statistical certification.

## Statement and conventions

Let N>=2, m=2k>=0, with ordered labeled transpositions in S_N and rightmost-first multiplication. Write U_(N,m) for the global uniform identity-word law. A support component of v>=2 vertices has length 2p=2(v-1+g), g>=0. Isolates have (v,p)=(1,0). Fix K from top-level N,m as in H0. All logs below are natural.

**R2-TAIL.v1.** For 1<=k and 2k<=N, put d=N-2k+1, a=k(k+1)^2/(9d^2), and q=4 exp(1+a)Nk/d^2. If q<1, then

    U_(N,2k){some support component has more than K vertices}
      <= min(1, N exp(1+a) q^K/(1-q)).                 (R2.1)

If K>=min(N,k+1), the left side is zero. The H0 excluded event is contained in this event, so the same bound applies to 1-Z_A/Z.

**T0 analytic corollary.** If m^5<=N^3 and N>=2^145, then the H0 omitted mass is at most

    eta_0(N)=exp(-log(N)^2/[12 loglog(N)]).             (R2.2)

For N<2^145 take eta_0(N)=1. This is one explicit negligible-in-N bound, uniform in every feasible even m in T0. For m=0 the error is zero.

**T1 stronger analytic corollary.** If m^3<=N^2 and N>=2^145, the omitted mass is at most

    eta_1(N)=exp(-log(N)^2/[16 loglog(N)]).             (R2.3)

Below that threshold take eta_1=1. This includes the stretch m<=N^(2/3-delta) for every fixed 0<delta<2/3, with constants independent of delta. T0 remains separately recorded.

The same statements hold for the strictly smaller subset in which EVERY support component has size <=K. Thus H0's genus-zero/one primitives are unnecessary for existence of an approximate global sampler, although they remain part of H0 itself.

## Dependency R2-DYZ.v1: normalized connected recurrence

Let C(v,2p) count connected words on a fixed labeled v-set, and define A_g(v)=C(v,2v-2+2g)/(2v-2+2g)!. Put h_g,v=A_g(v)/v!. For v=1 set h_0,1=1, h_g,1=0 (g>0). DYZ, *Classical Hurwitz numbers and related combinatorics*, Proposition 1 Eq(13), gives

    h_g,v = 2/[v^2(v-1)] sum_(a+b=v) sum_(i+j+r=g)
              a^(2r+3)b^2/(2r+2)! h_i,a h_j,b.       (R2.4)

The minimal formula is A_0(v)=v^(v-3), v>=2. DYZ Eq(19)–(20), and the immediately following labeled-tuple interpretation, show that h=C/(v! length!): v! restores sheet labels, and length! restores distinguished ordered branch positions. Connected covers correspond to transitive generated subgroups, equivalently connected transposition support. Reversal transports opposite composition conventions without changing the identity target or component data.

Source checked directly on PDF pages 4–5:
https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf

This is the only imported count dependency. No asymptotic result from fixed-genus or linear-length literature is used.

## R2-MAJORANT.v1: factorial genus bound

For every v>=1 define

    B_v=(1/12) sum_(j=1)^(v-1) j^2
       =(v-1)v(2v-1)/72 <= v^3/36.

Then, for every g>=0,

    A_g(v) <= A_0(v) B_v^g/g!,                       (R2.5)

with the evident v=1 convention (the sole nonzero term is g=0).

Proof. Let H_v(z)=sum_(g>=0) [h_g,v/h_0,v] z^g, a formal series. At genus zero (R2.4) implies that

    pi_(a,b)=a^3 b^2 h_0,a h_0,b /[v^2(v-1)h_0,v]

are positive and sum to one over ordered a+b=v. Thus (R2.4) is exactly

    H_v(z)=sum_(a+b=v) pi_(a,b) H_a(z)H_b(z) F(a^2z),
    F(z)=sum_(r>=0) 2z^r/(2r+2)!.

Coefficientwise, F(z)<=exp(z/12). Indeed (2r+2)!>=2*12^r*r!, with equality at r=0,1; the induction multiplier is (2r+4)(2r+3)>=12(r+1), since the difference is 4r^2+2r>=0. If a+b=v, then

    12(B_v-B_a-B_b)
      = a^2 + sum_(j=1)^(b-1) [(a+j)^2-j^2] >= a^2.

Inducting on v therefore bounds each summand H_a H_b F(a^2z) coefficientwise by exp(B_v z). Taking the convex average proves H_v<=exp(B_v z), and comparison of coefficients proves (R2.5). Every operation is between formal series with nonnegative coefficients, so no analytic convergence or unproved multiplication of marginal probabilities is involved.

## R2-INCIDENCE.v1: matching insertion ratio

Let F(N,k)=Z(N,2k)/(2k)!. A macro is a set partition of the N labeled vertices into components, each with a feasible integer genus and hence cost p=v-1+g; isolates cost zero. Its weight is the product of A_g(v) over nontrivial components. The sum of macro weights of total cost k is F(N,k): the position-interleaving count is (2k)!/product_(components)(2p)!, and internal word counts give the remaining factors.

For 0<=p<=k and 2k<=N,

    F(N,k-p)/F(N,k)
      <= 4^p (k)_p / (N-2k+2p)_(2p)
      <= (4k/d^2)^p,                               (R2.6)

where falling factorials and d=N-2k+1 are used; p=0 means ratio one.

Proof. A macro of cost k-p uses at most 2(k-p) nonisolated labels, because v<=2(v-1+g) for v>=2. Thus it has at least s=N-2k+2p isolated labels. Choose an unordered matching of p pairs on isolated labels. There are s_actual_(2p)/(2^p p!) choices. Each new pair component has weight A_0(2)=1/2, so total weighted extensions of the macro are at least its weight times (N-2k+2p)_(2p)/(4^p p!). Conversely, a macro of cost k can be obtained this way only by deleting p distinct minimal size-two components; it has at most k such components, so at most binom(k,p) preimages. The weight accounting in this reverse count is exact: original weight times 2^(-p) equals target weight. Summing both sides gives (R2.6), since p!binom(k,p)=(k)_p. No component or edge independence is assumed.

## R2-MARKED.v1: exact expectation and tail

For fixed v>=2 and g>=0 with p=v-1+g<=k, the expected number X_(v,g) of components of this type is exactly

    E X_(v,g)=binom(N,v) A_g(v) F(N-v,k-p)/F(N,k).     (R2.7)

Choose its labeled v-set, its internal word, its 2p distinguished positions, and the identity word on the complementary labels. Dividing the resulting raw count by Z(N,2k) gives (R2.7); the factorials cancel because F uses length factorials. Each actual component is marked once, so equal sizes cause no extra symmetry factor.

Adding v specified isolated labels injects macros counted by F(N-v,k-p) into those counted by F(N,k-p), with the same weights. Apply (R2.6) and (R2.5), then sum g:

    E X_v <= binom(N,v) v^(v-3) (4k/d^2)^(v-1)
                 exp(4k B_v/d^2)
            <= N exp(1+a)/v^3 * q^(v-1).            (R2.8)

Here v<=k+1 whenever the component is feasible; 4kB_v/d^2<=kv^3/(9d^2)<=av. Also binom(N,v)<=N^v/v! and v!>=(v/e)^v. Extending the finite nonnegative genus sum to all g only increases it. Finally, the union bound and v^-3<=1 give

    P(max component size>K) <= sum_(v=K+1)^min(N,k+1) E X_v
                             <= N exp(1+a) q^K/(1-q),

which proves (R2.1). The expectation and the incidence comparison both use the exact endpoint-conditioned bridge law.

## Effective constants and uniformity

Write L=log N and assume N>=2^145, hence L>100. If 1<=k and m^3<=N^2, then m<=N^(2/3)<=N/2, k+1<=m, and d>=N/2. Consequently

    a <= 2m^3/(9N^2) <= 2/9,
    exp(1+a)<4,
    q <= 32m/N.

For T0, m<=N^(3/5), so q<=32N^(-2/5)<=N^(-1/3), since log32<100/15. For T1, q<=32N^(-1/3)<=N^(-1/4), since log32<100/12. In both cases q<1/2 and N exp(1+a)/(1-q)<=8N.

Let j=floor(L/log L). We have 1<=j<=L and

    2j log j <= 2(L/log L)log L=2L <=4log(N+m+2).

Thus j is an eligible cutoff value (and j<=N), so K>=j>=L/(2log L). For T0 this gives error<=8N exp(-L^2/(6log L)); for T1 it gives error<=8N exp(-L^2/(8log L)). For L>=100,

    L+log8 <= L^2/(16log L) <= L^2/(12log L).

For verification of the first inequality, L/log L is increasing for L>e and at L=100 exceeds 21; hence L^2/(16log L)>=1.31L>=L+log8. This establishes both (R2.2) and (R2.3). Each bound is negligible because L/log L tends to infinity; the algorithm and exponents are fixed, not chosen separately for an accuracy power.

## Exceptional cases and first remaining obligations

Odd m has empty identity fiber by sign and is outside the sampling theorem. m=0 is the unique empty word; m=2 is a uniform repeated edge. N=2 has a singleton bridge for every feasible even m. N=1 permits only m=0. The tail event is empty whenever K>=min(N,k+1), including all sufficiently short cases. No claim is made that the estimates are sharp near m=N^(2/3), or that sampling is impossible at greater lengths.

Mathematical dependencies remaining for global algorithm certification: confirm exact small-support DP and least-label assembly implementation; verify polynomial bit/runtime accounting; obtain a nonauthor audit of this exact version and the imported count normalization. The analytic derivation itself contains no unresolved inequality as presently written, but is provisional until those audit gates close.
