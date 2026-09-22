# Independent blind argument: all large components

Status: **proved using the cited established Hurwitz recurrence**, subject to later independent audit. This is the frozen blind report. Input is the copied blind brief only. No candidate proof or other worker report was read.

Let B(n,t) count all ordered identity words of length t over the transpositions of S_n, and let C(v,ell) count those whose support graph is connected on all v labels. Set b(n,t)=B(n,t)/t! and

F_v(x)=sum_{ell>=0} C(v,ell)x^ell/(v! ell!).

The transpositions are involutions; products compose rightmost first. Labels and factor positions are distinguished. Target distribution throughout is global fixed-length uniform.

## 1. Source input and its normalization

Dubrovin–Yang–Zagier, *Classical Hurwitz numbers and related combinatorics*, Proposition 1, equations (13), (17), and the discussion around (19)–(20):

https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf

The source identifies n! H^*_(t,n) with ordered t-tuples of transpositions having product one. The exponential formula separates support components. Consequently its C_v(x) is exactly F_v(x) above, with F_1(x)=1. Equation (17) is

v^2(v-1) F_v(x) = sum_{k=1}^{v-1} k(v-k)^2 [2 cosh(kx)-2] F_k(x)F_(v-k)(x).

The genus-zero coefficient is a_v=v^(v-3)/v!, so F_v(x)=a_v x^(2v-2)+higher terms. The n=1 coefficient is a_1=1. The paper derives the positive recurrence from a published Hurwitz generating-series identity; this is a literature dependency, not an elementary identity newly proved here.

Composition convention does not change the counts: reversing all factors takes either multiplication convention to the other while fixing the identity endpoint and support.

## 2. A uniform all-genus majorant

For z>=0, 2(cosh z-1)<=z^2 exp(z). This follows, for example, by integrating the bound cosh(tz)<=exp(z) twice, or from sinh(u)<=u exp(u).

For every v>=1 and x>=0,

F_v(x) <= a_v x^(2v-2) exp[x v(v-1)/2].                 (M)

At x=0 interpret the displayed expression continuously. For x>0 proceed by induction on v using the positive recurrence. The k-th summand gains at most the exponential with exponent

x {k + k(k-1)/2 + (v-k)(v-k-1)/2} <= x v(v-1)/2,

because the difference is x k(v-k-1)>=0. The nonexponential leading coefficients sum to a_v by taking the lowest coefficient in the same recurrence. Thus the induction is valid uniformly over all genera, with no use of a fixed-genus asymptotic.

## 3. Elementary ratio comparison by inserting isolated double edges

For m=2q, N>=m, and 0<=r<=q,

b(N,m-2r)/b(N,m)
 <= 4^r (q)_r / (N-m+2r)_(2r)
 <= [4q/(N-m+1)^2]^r.                                 (R)

Here (z)_j denotes a falling factorial. To prove it, an identity word of length m-2r uses at most m-2r vertices: every used vertex appears at least twice, since a unique occurrence would prevent that vertex being fixed by the product. Choose r disjoint unordered edges on unused vertices. There are at least (N-m+2r)_(2r)/(2^r r!) choices. Interleave their two identical copies with the old word in m!/((m-2r)!2^r) ways. Mark the r inserted components. Every output has at most q components consisting of a single edge used exactly twice, so at most binom(q,r) such marked preimages. Division gives (R). This is an inequality between counts on the same N labels; no independence assumption appears.

## 4. Effective component tail

Take even m>=2 with m^5<=N^3. Then m<N and define

D=N-m+1, x=sqrt(2m)/D,
rho=e N x^2 exp(xm/4).

For each feasible v>=2 and ell=2v-2+2g<=m, the expected number of support components with those parameters under U_(N,m) is exactly

binom(N,v) C(v,ell)/ell! * b(N-v,m-ell)/b(N,m).

Embed the remaining word into N labels and apply (R). This expectation is at most

N^v C(v,ell) x^ell/(v!ell!).

Summing ell and using (M), v<=m/2+1, and v!>=(v/e)^v, gives

E[number of components on v vertices] <= x^(-2) rho^v/v^3.

Therefore, whenever rho<1,

Pr[max component size>K] <= min{1, x^(-2) rho^(K+1)/(1-rho)}.             (T)

If K>=m/2+1, the left side is exactly zero. The requested bad event (g>=2 and v>K) is contained in this event, so (T) also controls the fixed cutoff in the brief.

For an explicit uniform asymptotic bound, N>=8 gives D>=N/2 and xm/4<=1. Thus rho<=8 e^2 N^(-2/5)<60 N^(-2/5). For N>=60^5, rho<=N^(-1/5)<=1/2 and x^(-2)<=N^2. With K0(N)=max{v<=N:v^(2v)<=(N+2)^4}, one obtains

sup_(even m>=0,m^5<=N^3) Pr[max component size>K(N,m)]
 <= min{1, 2 N^[2-(K0(N)+1)/5]}                        (U)

for N>=60^5; use 1 for smaller N and 0 for m=0. Since K0(N) tends to infinity, this is negligible. An explicit sufficient threshold for any fixed a>0 is N>=max{60^5,L^L}, L=ceil(5(a+3)); then K0>=L and the right side is at most N^(-a).

## 5. Exact restricted sampler and T0

A stronger restriction suffices: keep only words all of whose components have size at most K(N,m), with no genus restriction. Fix this top-level K for every subproblem.

For each v<=K, count completions on states (p,pi), where p is a permutation on v labels and pi is the support partition accumulated so far. Initially p=id and pi is discrete. Appending transposition tau=(a,b) sends (p,pi) to (p tau,pi join {a,b}); terminal state requires p=id and pi to be the one-block partition. Backward dynamic programming to every length ell<=m counts connected words exactly and samples them exactly by integer continuation weights. The state space has at most v! Bell(v)<=v^(2v)<=(N+m+2)^4 states. No connectedness rejection is needed.

Let Z(n,t) count allowed words on n labels with t factors. The component containing the smallest label gives

Z(n,t)=Z(n-1,t)+sum_(v=2..min(K,n)) sum_(ell=2v-2..t, even)
 binom(n-1,v-1) binom(t,ell) C(v,ell) Z(n-v,t-ell),

with Z(0,0)=1 and Z(0,t>0)=0. Choose (v,ell) by these integer weights; choose its other labels and positions uniformly; sample its connected word; recurse on the remainder. The decomposition is bijective, so the output law is exactly uniform on the restriction. Its TV distance from U_(N,m) equals the probability of the discarded set and obeys (T)/(U).

All counts have O(m log N) bits up to polynomial overhead, and there are polynomially many arithmetic operations in N,m. Uniform integer sampling by bit rejection has expected polynomial cost. Thus the same algorithm, without an accuracy parameter, satisfies T0. The argument is about polynomial complexity in N,m, not the number of permutation wires.

Boundary cases: m=0 yields the unique empty word; m=2 is a uniformly selected repeated transposition; N=2 has one word at every even length (only m=0 lies in its sparse regime); N=1 has only m=0; odd m has an empty bridge set and lies outside the target domain. K>=2 whenever N>=2, so the allowed set is nonempty at every even length.

## 6. Checks and limitations

`exact_checks.py` independently counts words by full permutation DP for 1<=n<=7, 0<=m<=12 and removes smaller support components by the rooted exponential formula. All 78 coefficient checks of the positive Hurwitz recurrence, 20 insertion-ratio checks, and genus-zero minimal-length counts passed. These finite checks validate normalization and small boundary cases; they do not substitute for the universal arguments.

The all-genus majorant uses a verified published recurrence. Whether that is a satisfactory dependency for an unconditional project theorem remains a coordinator/source-audit decision. No current candidate proof has been compared yet. Model/runtime identity is not independently exposed; the launch manifest requests gpt-6-astra at ultra effort. Same-model internal review cannot provide independent human certification.

## 7. Blind referee verdict and falsification record

**Promote for independent audit:** the proposed fixed-threshold tail statement follows from the stronger all-large-component tail (T)/(U). The exact small-component sampler described above establishes T0 if the displayed proof withstands independent audit. This is an existence/complexity theorem; the supplied Python files are bounded verification prototypes, not a production sampler.

**Proved inputs used:** sign parity; a used vertex occurs at least twice; support-component decomposition; the published normalized positive Hurwitz recurrence and its genus-zero coefficient; elementary counting inequalities. No mixing, Hurwitz-transitivity, approximate independence, fixed-genus uniformity, or hardness assumption enters the argument.

**First unproved step:** none identified in this argument after accepting the explicitly cited established recurrence. The recurrence is the sole non-elementary mathematical dependency; its source normalization was checked against the source and against independent exact enumeration. This statement is a blind review finding, not a claim of human certification.

**Falsification attempts:** direct word enumeration passed 78 recurrence-coefficient checks and 20 insertion-ratio checks. A separate local-completion and rooted-assembly unranking implementation matched the complete allowed word sets in S_3,m=4; S_4,m=4; S_4,m=6 with both K=3 and K=4; and N=2 at m=0,2,8. The restricted S_4,m=6 counts are 1056 for K=3 and 3936 for K=4. Exact equality of word sets certifies all word-level diagnostics on these finite cases, including identity, prefix cycle types, position/edge frequencies, multiplicities, adjacent repeats, and support components.

**Retained cautions:** the two-variable Hurwitz generating function diverges at positive arguments. The proof never evaluates that function: it evaluates each fixed-v entire F_v, and retains the feasible bound v<=m/2+1 before extending the resulting geometric upper bound. Fixed-genus asymptotics in the cited DYZ source do not provide a uniform genus estimate; they were not used. The Chapuy–Louf–Walsh linear-length regime does not establish the present sparse statement; it was not used. Failure of the restriction would not imply hardness; no such failure was found. No heavy computational grid was run.

**Isolation statement:** the only task-specific mathematical input was blind-brief.input.md and the permitted primary sources. The worker necessarily inherited repository-wide AGENTS framing and the operational parent task; therefore isolation is from current proof attempts, previous verdicts, and other workers, not from every piece of project context. No such proof/report file was opened before freezing. The tool runtime does not expose a separately verified model/effort identity; the launch manifest specifies gpt-6-astra and ultra. Same-model internal audits are correlated evidence.

## 8. Claim ledger

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
|---|---|---|---|---|---|
| DYZ recurrence has the needed normalization | proved literature input | cited source, finite labeled words | Proposition 1, (17), (19)–(20) | 78 exact coefficients | retain with citation |
| Entire connected-series majorant (M) | proved | positive recurrence | section 2 induction | algebraic self-audit | promote to coordinator audit |
| Coefficient ratio (R) | proved | N>=m even | marked isolated-edge insertion | 20 exact inequalities | promote |
| All-large-component tail (T)/(U) | proved | m^5<=N^3, established recurrence | sections 3–4 | boundary and normalization checks | promote |
| Requested bad event is negligible | proved | same | event containment | no extra hypothesis | promote |
| Exact restricted sampler is polynomial in N,m | proved algorithmic construction | exact integer arithmetic/random bits | section 5 | exhaustive unrank bijections | promote conceptual result |
| Prototype is production-ready for arbitrary inputs | unresolved / not claimed | implementation engineering | bounded scripts only | none | do not promote |
| Existing candidate proof/sampler is correct | unresolved | current version not yet received | none | blind restriction | request review inputs |

Frozen at 2026-09-22T05:55:11.341362+00:00. Later review changes must go in separate files.
