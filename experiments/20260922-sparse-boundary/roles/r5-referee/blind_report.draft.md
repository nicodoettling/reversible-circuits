# Independent blind report — draft awaiting freeze

**Verdict: reject both original negligible-error assertions.** There is a counting proof that, at the maximal permitted even length, both errors tend to one. This does not establish sampling hardness. No alternative polynomial-time sampler is certified here.

## Input and blindness

The exact question and K definition are preserved in initial_brief.md, with its SHA256. Initial operational instructions and unavoidable inherited repository/model framing are recorded in initial_input.md. Until this report is frozen, no other role directory, old proof/verdict, HANDOFF, GOAL_SPEC, or coordinator prompt has been read. Same-model review remains correlated.

## Precise statement

Use fixed labels, ordered positions, and (ab)(x)=a(b(x)). Let U be uniform on identity words in all transpositions of S_N. Let A allow every support component of genus at most one, together with arbitrary-genus components having at most the fixed top-level K vertices. Let B allow only components of at most K vertices. Set m=m_*(N)=2 floor(N^(3/4)/2).

**Proved, with the checked primary-source count formulas below:** for every integer N >= ceil(exp(1024)),

    |B|/|Omega(N,m)| <= |A|/|Omega(N,m)| <= N^(-m/16).

Consequently each TV error is at least 1-N^(-m/16). In particular neither is uniformly bounded by a negligible function of N over all permitted even lengths.

## Dependency and normalization check

Let c(v,ell) count identity words of length ell whose support is connected on a fixed labeled v-set. Vakil, *Genus 0 and 1 Hurwitz numbers*, Section 1.2 and Corollary 1.5, gives

    c(v,2v-2)=(2v-2)! v^(v-3),
    c(v,2v)=(2v)! v^(v-2)/24
      * [v^2-v-sum_(j=2)^v v^(2-j)(j-2)! binomial(v,j)].

The convention is a fixed permutation, ordered transposition factors; for alpha=[1^v], his c=G. Connected support is exactly transitivity of the generated transposition group. Thus, for g=0,1 and ell=2v-2+2g,

    c(v,ell)/(v! ell!) <= e^v,                 (1)

using v! >= (v/e)^v and dropping nonnegative subtractions in genus one. See source_checks.md and https://math.stanford.edu/~vakil/files/g01hurwitz.pdf. This is a checked theorem dependency, not an unchecked identification of differently normalized Hurwitz numbers. No connected Hurwitz-orbit classification is needed.

## Proof

### 1. An upper bound for A

For positive t let C_A(N,t) be the sum of

    N^v c(v,ell) t^ell / (v! ell!)

over allowed nontrivial connected component types. Exact assembly of support components gives

    |A| <= m! [t^m] exp(C_A(N,t))
         <= m! t^(-m) exp(C_A(N,t)).          (2)

Indeed, if n_(v,ell) components of each type use s vertices, their contribution to the count is

    m! (N)_s product_(v,ell)
       [ (c(v,ell)/(v! ell!))^n_(v,ell) / n_(v,ell)! ],

with total length m. Replace (N)_s by N^s and, if necessary, add nonnegative terms with s>N. Isolates are precisely the unused labels and do not appear as components in this formula.

Take N>=1024, 2<=m<=N^(3/4), and

    t=sqrt(m)/(N K^2),  y=K^2 t=sqrt(m)/N.

For small components v<=K use c(v,ell)<=K^(2ell) and ell>=2v-2. Since sum_(ell>=a) y^ell/ell! <= e^y y^a/a!, their total contribution is at most

    e^y sum_(v>=2) N^v y^(2v-2)
      = e^y m/(1-m/N) <= 2 e m.              (3)

The extension to all v only enlarges this bound. For all genus-zero components, (1) gives

    sum_(v>=2) e^v N^v t^(2v-2)
      = e^2 N^2 t^2/(1-e N t^2) <= 2 e^2 m. (4)

For genus-one components it gives

    sum_(v>=2) e^v N^v t^(2v)
      = (e N t^2)^2/(1-e N t^2) <= 1.        (5)

Here y<=1, m/N<=1/2 and eNt^2<=e m/N<=1/2. Overcounting the overlap of the small and low-genus classes is harmless. Since 2e+2e^2+1<22, equations (2)--(5), with m!<=m^m, imply

    log |A| <= m log N + (m/2) log m
               + 2m log K + 22m.            (6)

### 2. A lower bound for all identity words

For any 2<=r<=N, let a_sigma count length-m/2 words on the first r labels with product sigma. Reversal inverts products, so

    |Omega(N,m)| >= sum_(sigma in S_r) a_sigma^2
                  >= binomial(r,2)^m / r!.  (7)

This is Cauchy--Schwarz. It neither assumes an unconditioned graph model nor requires connectedness or rapid mixing.

Choose r=floor(m/log m), with m large enough that m/log m>=2. Then r>=m/(2 log m), binomial(r,2)>=r^2/4 and log(r!)<=r log r<=m. Hence

    log |Omega(N,m)| >= 2m log m-2m log log m
                         -(log 16+1)m.      (8)

### 3. Compare on the prescribed boundary sequence

For m=m_*(N) and the stated N range, m>=N^(3/4)/2. Also K<=6 log N: the defining inequality gives K log 2 <=2 log(N+m+2), and N+m+2<=3N. Put L=log N. From (6)--(8),

    (1/m) log(|A|/|Omega|)
      <= -(1/8)L + 4 log L + 31
      <= -(1/16)L                         (9)

for L>=1024. The constant 31 dominates

    22 + log 16 + 1 + (3/2)log 2 + 2 log 6.

The final inequality follows from 4 log(1024)+31<64 and monotonicity of L/16-4 log L for L>=1024. This proves the assertion, and B subset A proves the B assertion as well.

## Boundary and falsification checks

- m odd: Omega is empty by sign, so its uniform law and the displayed TV comparisons are undefined. The requested theorem only quantifies over even m.
- m=0: the unique word is empty; A=B=Omega and both errors are zero.
- m=2: each identity word is (t,t), has a two-vertex genus-zero component, and K>=2 for N>=2. Again both errors are zero.
- N=2: there is one word at every even length, K=2, so A=B=Omega. Under m^4<=N^3 only m=0 occurs.
- N=1: only the empty word exists, as stipulated in the brief.
- Minimal connected lengths and the first positive-genus case were checked exactly on v=2,3,4,5. finite_checks.py evaluates all product/support-partition states through ell=2v and reproduces both source formulas; finite_checks.json includes command, repository commit, Python version and raw counts. The script uses deterministic exhaustive aggregation and no third-party dependency.
- The concentrated-support lower bound (7) was independently checked in every even finite test. These finite checks validate normalization and potential implementation errors, not the asymptotic conclusion.

## What is and is not discharged

The two original approximation questions are refuted, separately via the same stronger A bound. There is no missing lemma in the above count comparison beyond the stated checked literature theorem. An efficient scalar recurrence for total Hurwitz counts would still require a literal sampler/decoder and bit-cost proof; no such implication is used here. Polynomial-time sampling of U in this range remains unresolved by this referee. This report proves no Markov mixing claim and makes no computational-hardness inference.

## Claim ledger

| Claim | Status | Assumptions | Evidence/artifact | Independent check | Action |
|---|---|---|---|---|---|
| Both original negligible-error claims | refuted | exact A,B,K and original range | inequalities (1)--(9) | finite normalization DP; analytic constants | reject |
| Concentrated-support lower bound | proved | even m, 2<=r<=N | Cauchy--Schwarz (7) | all even finite cases | keep |
| Low-genus normalized count bound | proved from checked source | fixed labeled identity words | Vakil Section 1.2, Cor. 1.5 | exact v=2,...,5 | keep |
| Polynomial sampler for U throughout range | unresolved | none supplied | no decoder audited yet | none | reserve for candidate audit |

## Referee recommendation

A candidate that claims either Q_A or Q_B has negligible error uniformly over the original range must address this count separation. Shrinking the length range or enlarging the allowed component class changes the theorem and must retain the original negative result. Failure of these two truncations is compatible with an entirely different efficient sampler.
