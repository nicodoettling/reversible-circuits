# Fixed and growing genus support obstruction — proof candidate v1

Author: R3 mass/falsification. Frozen 2026-10-28. **Status: proved by author from the inherited checked DYZ identity, provisional pending independent-scope review.** No final campaign acceptance is asserted.

## Exact statements and law

Products are maps composed rightmost first. Labels [N] and all m positions are distinguished. For N>=2 and even m>=0, U_(N,m) is uniform on Omega(N,m), the set of ordered length-m transposition words with product identity. No Markov kernel or sampling algorithm is assumed. A nontrivial connected support component has v>=2 labels, length ell=2v-2+2g and integer genus g>=0; singleton components are unused labels.

Set P=N+m+2 and fix L=max{1<=v<=N:3^v<=P^4} at the original input. For any integer G>=0, let E_(G,L) be the subset in which every nontrivial support component satisfies g<=G OR v<=L. The word support, connected-component lengths and genus are determined by the literal word, so this is an event of the exact bridge law.

**M-GROW.v1.** For every integer j>=64, N=2^(8j), m=2^(6j), and every integer 0<=G<=2^j,

    U_(N,m)(E_(G,L)) <= 2^(-1-jm/2).                 (T)

Consequently any probability law Q supported on E_(G,L) obeys

    d_TV(Q,U_(N,m)) >= 1-2^(-1-jm/2).

**FG.v1.** For each fixed integer G>=0, (T) holds for every integer

    j >= J(G)=max{64, ceil(log_2(max{1,G}))}.

In particular **M2** (G=2) fails as a global support policy on every j>=64 in this sequence, even if exact genus-two decoding is available. This is not the statement that genus-two decoding is impossible or useless, nor a refutation of the global mission. It rules out only laws confined to the declared component event. The uniform-in-G version also rules out this event for G as large as N^(1/8) along the sequence; no decoder complexity assertion is attached to that observation.

## Dependencies, provenance and novelty

D1: DYZ, *Classical Hurwitz numbers and related combinatorics*, Proposition1 Eq(13), Section1.2 Eqs(19)-(20), and genus-zero value following Eq(28). Historical source audit: experiments/20260922-sparse-boundary/source_checks.md; independent reconstruction: roles/r5-referee/candidate_audit_v1.md, section DYZ dependency. Primary URL: https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf. This worker read those exact repository inputs; it does not claim a fresh external source audit. The original primary-source normalization is an explicit inherited checked theorem dependency, and the needed recurrence and its majorant are rederived below.

D2: Unique labeled-component assembly. Reproved below; original exact statement: experiments/20260905-bridge-length-phase-diagram/roles/r3-intermediate-hybrid/report.md, Section1.

D3: Embedded-subgroup return lower bound. Reproved below, including parity.

The accepted September22 H0/H2 obstruction allowed all g<=1 plus arbitrary genus below a size cutoff. Its finite numerator argument and denominator comparison are predecessors, not evidence that enlarging its event must still fail. The new load-bearing step is the positive-genus sum through arbitrary G with an explicit condition6G^3*x<=1/16. In particular the enlarged G=2 event is bounded directly. The September22 blind all-N claim is retained provisional and is not used.

Dependency graph: DYZ count identity plus genus-zero value -> coefficientwise factorial genus majorant -> finite enlarged-event numerator; unique assembly -> same numerator; elementary subgroup bound -> denominator; explicit sequence inequalities -> (T) -> fixed-G and M2 corollaries. No genus-two sampler, Hurwitz classification, random-graph transfer, or mixing statement is a dependency.

## 1. Reconstruct the uniform count majorant

Let C(v,ell) count connected identity words on a fixed labeled v-set, with C(1,0)=1 solely for the singleton recurrence. Put

    F_v(t)=sum_ell C(v,ell)t^ell/ell!,
    A_g(v)=C(v,2v-2+2g)/(2v-2+2g)!.

The DYZ normalization is C(v,ell)=v! ell! h(g,v), and its positive recurrence gives the formal-series identity

    v^2(v-1)F_v(t)
       =2 sum_(a+b=v) binom(v,a) a b^2 (cosh(at)-1)F_a(t)F_b(t).

The degree split is ordered with a,b>=1. F_1=1 and A_0(v)=v^(v-3). Define H_v=F_v/[v^(v-3)t^(2v-2)] for v>=2 and H_1=1. Then H_v is a convex combination of L(at)H_aH_b, where

    L(z)=2(cosh z-1)/z^2,
    w_(a,b)=binom(v,a) a^a b^(b-1)/[v^(v-1)(v-1)].

The weights sum to1 by the genus-zero coefficient identity. The power z^0 term of L is1. Coefficientwise L(z)<=exp(z^2/12), since

    2/(2r+2)! <= 1/(12^r r!),   r>=0,

with equality at r=0 and successive ratio12(r+1)/[(2r+4)(2r+3)]<=1. Let b_v=(v^3-v)/36, including b_1=0. For a+b=v,

    b_v-b_a-b_b=abv/12 >= a^2/12,

because bv>=a. Induction on v and coefficient positivity therefore give

    H_v <= exp(b_v t^2),
    A_g(v) <= v^(v-3)b_v^g/g!,   v>=2,g>=0.      (M)

All comparisons are coefficientwise formal series. No infinite-degree convergence or probability independence is assumed.

## 2. Exact assembly and the enlarged finite numerator bound

Let m=2k>0 and let J be any integer1<=J<=N. Replace L by J for this finite lemma, still fixed at the original input. Write Z_(G,J)=|E_(G,J)|. A profile with a_(v,g) components of each type has total support s=sum v*a_(v,g) and half-length k=sum(v-1+g)*a_(v,g). Its exact normalized contribution to Z_(G,J)/m! is

    (N)_s product_(v,g) [A_g(v)/v!]^a_(v,g) / a_(v,g)!.

To see this, choose disjoint labeled sets with multiplicity divisor a!, choose each connected internal word, and interleave its positions in order. Restrictions of the final literal word recover all these choices uniquely. Unused labels are isolates and contribute no extra factor.

Replace (N)_s by N^s and allow extra profiles with s>N; all coefficients are nonnegative. For a formal variable y this yields

    Z_(G,J)/m! <= [y^k] exp(S_(G,J)(y)),
    S_(G,J)(y)=sum_(v=2..N) N^v/v! sum_(g>=0:g<=G OR v<=J)
                          A_g(v)y^(v-1+g).

At each fixed N the all-genus terms are dominated by exponentials via(M), so evaluation at positive x is legitimate. Alternatively truncate all component half-lengths at k before the comparison. Thus

    Z_(G,J)/m! <= x^(-k) exp(S_(G,J)(x)).         (A)

Set x=k/N^2 and q=3Nx. Assume

    q<=1/2,   b_J*x<=1,   6G^3*x<=1/16.          (F)

For G=0 the final condition holds automatically. Monotonicity of b_v and(M) give, for every v, an upper bound on its permitted genus weight by

    exp(b_J*x) + sum_(g=1..G) (b_v*x)^g/g!
       <=3 + sum_(g=1..G) (b_v*x)^g/g!.

For v<=J this dominates the entire permitted genus series; for v>J its first term dominates the required genus-zero term. Hence

    S_(G,J)(x) <=3S_0(x)+sum_(g=1..G) S_g(x),
    S_g(x)=sum_(v=2..N) N^v/v! v^(v-3)b_v^g x^(v-1+g)/g!.

Using v!>=(v/e)^v>(v/3)^v and q=3Nx,

    S_0 <=3N sum_(v>=2) q^(v-1)/v^3
        <=3N*q/[8(1-q)] =9k/[8(1-q)] <=9k/4.  (B)

For g>=1 put d=3g-3>=0. Since b_v<=v^3/36,

    S_g <=3N*x^g/(36^g g!) sum_(v>=2) v^d q^(v-1).  (C)

For every integer d>=0, v>=1,

    v^d <= d! binom(v+d-1,d).

This also holds when d=0. The binomial generating function and subtraction of its v=1 term imply

    sum_(v>=2) v^d q^(v-1)
      <=d![(1-q)^(-d-1)-1]
      <=(d+1)! q (1-q)^(-d-2)
      <=(d+1)!2^(d+2)q,                         (D)

where the middle inequality follows by integrating the increasing derivative of(1-q)^(-d-1) from0 toq. Substituting(C),(D) and3Nq=9k gives

    S_g <=9k*x^g*c_g,
    c_g=(3g-2)!2^(3g-1)/(36^g g!) <=(6g^3)^g. (E)

The last bound uses(3g-2)!<=(3g)^(3g), g!>=1, and2^(3g-1)/36^g<=(2/9)^g. It intentionally trades sharp constants for uniformity in g. For1<=g<=G, set a=6G^3*x. From(F),

    sum_(g=1..G) S_g <=9k sum_(g=1..G) a^g
                    <=9k*a/(1-a) <=3k/5.

For G=0 the sum is empty. Combining with(B),

    S_(G,J)(x) <=27k/4+3k/5=147k/20<8k.

Therefore the direct enlarged-event numerator bound is

    Z_(G,J) <=m!(N^2/k)^k exp(8k).              (U)

This is a finite theorem under(F), with no implicit dependence on G. It does not rely on inference from an old smaller event.

## 3. Verify the finite conditions for the top-level L

Take integer j>=1, N=2^(8j), m=2^(6j), k=2^(6j-1). Then

    x=2^(-10j-1),
    q=3*2^(-2j-1)<=3/8<1/2.

Since m+2<=N, P<=2N. Since3^L>=2^L,

    L<=4log_2(P)<=32j+4,
    b_L*x <= (32j+4)^3/[72*2^(10j)] <1.

At j=1 the displayed ratio is46656/73728<1. Its consecutive ratio is

    ((32j+36)/(32j+4))^3/1024 <8/1024<1.

Thus this condition holds for every integer j>=1. If0<=G<=2^j,

    6G^3*x <=3*2^(-7j)<=3/128<1/16.

All(F) hold with J=L, uniformly in the admitted G range. The cutoff has never been recomputed after removing a component.

## 4. Exact bridge denominator and final comparison

For2<=r<=N, consider the uniform all-transposition walk on the first r labels. Let p be its midpoint distribution after k=m/2 steps. Inversion symmetry of the generating measure gives

    Pr[X_(2k)=id]=sum_sigma p(sigma)^2.

Since p lies in one parity class containing r!/2 elements, Cauchy-Schwarz yields return probability>=2/r!. Therefore

    Z(N,m)>=2*binom(r,2)^m/r!.                  (L)

This is valid even at r=2 and does not assume mixing. It compares the genuine bridge normalizer, not an unconditioned support graph.

Choose r=floor(m/(6j)). For j>=1, m/(6j)>=2, so

    2<=r<=N,   r>=m/(12j),
    binom(r,2)>=r^2/4>=m^2/(576j^2),
    r!<=r^r<=m^r<=m^(m/(6j))=2^m.

Thus

    Z(N,m)>=2[m^2/(1152j^2)]^m.                 (L2)

Since m!<=m^m and k=m/2, (U) gives

    Z_(G,L)<=[sqrt(2)*exp(4)*N*sqrt(m)]^m.

With N/m^(3/2)=2^(-j), divide by(L2):

    Z_(G,L)/Z(N,m)
      <=(1/2)[1152sqrt(2)exp(4)j^2*2^(-j)]^m
      <=(1/2)[2^18*j^2*2^(-j)]^m.

Indeed sqrt(2)<2 and exp(4)<3^4=81, so the constant is below186624<2^18. For every integer j>=64,

    2^18*j^2 <=2^(j/2).

At j=64 the sides are2^30 and2^32. The right/left ratio increases subsequently because sqrt(2)>(65/64)^2 and((j+1)/j)^2 decreases. This proves(T). For any Q supported on E_(G,L), the event Omega\E_(G,L) has Q-probability0 and U-probability1-Z_(G,L)/Z, proving the TV bound. Equality holds when Q=Unif(E_(G,L)), but uniformity of Q is not needed for the lower bound.

## 5. Boundary falsification and restrictions

- Odd m: Omega(N,m) is empty by sign; its uniform law and these TV assertions are undefined. The theorem quantifies over even m only.
- m=0: the unique empty word belongs to every E_(G,L). Its retained mass is1, which does not intersect the positive-length asymptotic claim or finite lemma.
- m=2: every bridge is(t,t), with v=2,g=0; it is always allowed for G>=0. The finite upper bound can be loose and is not claimed to be useful here.
- N=2: L=2 for every m>=0, since P>=4 and3^2<=P^4; every even bridge uses the unique edge and is allowed. This does not meet the asymptotic sequence.
- Isolates: C(1,0)=1, C(1,ell>0)=0; singleton positive genus is never manufactured by(M) or the assembly.
- Negative g: there is no connected identity word at ell<2v-2, so no such branch enters any sum. The genus-zero boundary is retained for every v.
- Top-level cutoff: all probabilities and counts use the same N,m,L. No adaptive posterior or marginal-product estimate occurs.
- Historical counterexamples (zero-square insertion,81-versus80 support conditioning, unweighted support graphs, cut multiplicities, CP-1) remain valid against their original claims. This proof avoids each failed premise: no insertion/cut decoder, all connected counts retain endpoint/support normalization, and all probabilities are exact global cardinality ratios.

The bound is polynomial-exponent explicit in the degree N, not the wire count log_2(N). It is a counting support obstruction, not hardness and not a spectral-gap claim.

## Review status and first unresolved obligation

The author finds no unproved internal lemma after the explicit DYZ dependency. Required review is still open: fresh blind theorem-only referee, separate nonauthor exact-version argument audit, decisive finite regression reproduction and coordinator dependency closure. These are certification obligations, not grounds to upgrade a mathematical status automatically. The global sampler mission remains unresolved: a successful algorithm must place the appropriate mass on components outside this enlarged event, or use another mechanism entirely.
