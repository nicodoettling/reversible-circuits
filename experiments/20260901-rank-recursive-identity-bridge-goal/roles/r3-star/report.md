# R3 final report: exact prescribed-endpoint star bridges

Date: 2026-09-01
Target: the exact uniform law on length-`k` words in
`{(i N):1<=i<N}` with prescribed displayed product `q in S_N`
Outcome: **proved polynomial-time exact count and sampler**

## 1. Precise convention and theorem

Permutations are maps, and throughout

```text
(p q)(x) = p(q(x)).
```

Thus the displayed word `t_1 ... t_k` applies `t_k` first as a map.  This is
also the convention in Irving--Rattan and in the star-factorization formula
used below.  Put

```text
J_N = sum_(1<=i<N) (i N),
A_N(k,q) = [q] J_N^k.
```

### Theorem R3 (proved, with one audited enumerative input)

Let `N>=1`, `k>=0`, and `q in S_N`.  Let the cycle containing `N` have
length `a`.  Let `b_1,...,b_r` be the lengths of the nontrivial cycles not
containing `N`, and let `f` be the number of fixed points in `[N-1]`.  Define

```text
mu       = (a,b_1,...,b_r),
n_0      = a + sum_j b_j,
c_0      = 1+r,
ell_*(q) = n_0+c_0-2
         = (a-1) + sum_j (b_j+1).                         (1)
```

Parts equal to one in `mu` occur only when `a=1`; all fixed nonpivot labels
are accounted for by `f`.  Let

```text
F(t) = 2 sinh(t/2)/t
     = sum_(d>=0 even) t^d / (2^d (d+1)!).                (2)
```

For `s=0,...,f`, put

```text
n_s      = n_0+s,
lambda_s = mu union 1^s,
g_s      = k-(n_s+length(lambda_s)-2)
         = k-ell_*(q)-2s.
```

For `n_s>=2`, define the nonnegative integer

```text
T_k(lambda_s)
 = (k!/n_s!) (product_(u in lambda_s) u)
   [t^g_s] F(t)^(n_s-2) product_(u in lambda_s) F(u t).   (3)
```

Use the natural singleton convention `T_0((1))=1` and
`T_k((1))=0` for `k>0`.  Then

```text
A_N(k,q)
 = sum_(s=0)^f binom(f,s) T_k(lambda_s).                  (4)
```

Formula (4) is computable with positive rational coefficient arithmetic in
time polynomial in `N` and `k`.  Moreover, there is a Las Vegas exact sampler
for the uniform law on the `A_N(k,q)` words using a conservative
`O(N^3 k^3)` exact-rational operations on polynomial-bit integers and
`O(k^2 log N)` expected unbiased random bits.  Its total-variation error is
zero.  It supports every feasible arbitrary endpoint and length, not only a
top-level schedule.

For `N>=2`, feasibility is exactly

```text
k >= ell_*(q) and k == ell_*(q) (mod 2).                  (5)
```

For `N=1`, the sole feasible instance is `(k,q)=(0,e)`.

## 2. Feasibility and minimal star length

### 2.1 Lower bound

The following elementary lemma is useful beyond star words.  Suppose a word
of `j` transpositions has factor graph with `d_j` connected components on a
fixed `v`-vertex set and prefix product with `c_j` cycles.  Define

```text
Phi_j = j-v-c_j+2d_j.
```

Initially `Phi_0=0`.  Adding an edge between two graph components joins two
permutation cycles, so `d` and `c` both decrease by one and `Phi` is
unchanged.  Adding an edge inside one graph component leaves `d` unchanged
and either splits a cycle, leaving `Phi` unchanged, or joins two cycles,
increasing `Phi` by two.  Hence `Phi_j>=0`.  In particular, a connected
transposition factorization of a permutation with `c` cycles on `v` active
vertices has length at least

```text
v+c-2.                                                       (6)
```

For a star word, its exact used-label set together with `N` is connected.
Every lower label moved by `q` must be used.  Taking no extra fixed label gives
`v=n_0`, `c=c_0`, and (6) gives (1).  If the word additionally uses `s`
fixed lower labels, both `v` and `c` rise by `s`, so its lower bound is
`ell_*(q)+2s`.

### 2.2 Construction, parity, and padding

For the cycle containing the pivot,

```text
(N x_2 ... x_a)
 = (N x_a)(N x_(a-1))...(N x_2).
```

For a nonpivot cycle,

```text
(y_1 ... y_b)
 = (N y_1)(N y_b)(N y_(b-1))...(N y_2)(N y_1).
```

Concatenating these blocks over the disjoint cycles constructs `q` in exactly
the length (1).  Each star factor is odd, and (1) has the sign parity of `q`.
For `N>=2`, appending `(1 N)(1 N)` pads by two without changing the product.
This proves (5).

The minimal count is the `s=0,g_0=0` term of (4):

```text
A_N(ell_*(q),q) = ell_*(q)!/n_0! * product_(u in mu) u.       (7)
```

This agrees with Irving and Rattan, Theorem 1.1 and Corollary 1.2, after
renaming their pivot `1` to `N`.

## 3. Positive count formula

### 3.1 Exact-support decomposition

For a word `w`, let

```text
U(w) = {i<N : (i N) occurs in w}.
```

The set contains every moved lower label of `q`.  Its other elements are
fixed lower labels of `q`.  If exactly `s` of the `f` optional fixed labels
are selected, there are `binom(f,s)` possible labeled supports.

For each fixed support `U`, restrict to the active set `{N} union U`.  By the
definition of `U`, every star generator on this active set occurs.  The star
factor graph is therefore connected, equivalently the factorization is
transitive on the active set.  Its endpoint cycle type is precisely
`lambda_s`.  Conversely, every transitive factorization on that labeled
active set has exact support `U`.  This is a disjoint bijection and proves

```text
A_N(k,q) = sum_s binom(f,s) T_k(lambda_s).                    (8)
```

### 3.2 Audited primary enumerative input

Féray, [*Partial Jucys--Murphy elements and star
factorizations*](https://arxiv.org/html/0904.4854v2), Proposition 1.1 proves
that the transitive count depends only on ordinary cycle type, and Theorem
1.2 gives exactly (3) for arbitrary factor count.  Lemma 3.1 identifies
transitivity with full active support.  The source defines the factors
`(i n)` and uses ordinary map composition, so no reversal or inverse is
needed here.

The distinction in scope is exact:

- `s=f` is the transitive count on all `N` ambient labels;
- summing all `s` gives arbitrary, possibly nontransitive star words;
- `g_s=0` is minimal transitive length on the selected support;
- `s=0,g_0=0` is minimal length without a transitivity requirement in the
  ambient `S_N`;
- `g_s>0` covers arbitrary nonminimal length.

The minimal special case is independently stated in Irving--Rattan,
[*Minimal Factorizations of Permutations Into Star
Transpositions*](https://arxiv.org/html/math/0610640v2), Theorem 1.1 and
Corollary 1.2.  Those results do not by themselves cover arbitrary length;
Féray Theorem 1.2 does.

Crucially, (3) is positive for this purpose.  By (2), every factor in its
coefficient product has nonnegative rational coefficients.  Formula (8) is a
sum over disjoint labeled supports.  There is no signed character expansion
and no cancellation posing as a sampling probability.

## 4. Exact labeled sampler

For any endpoint `q` and `r>=1`, partition a word according to its last
factor.  Since `(i N)` is its own inverse,

```text
A_N(r,q) = sum_(i=1)^(N-1) A_N(r-1,q(i N)).                  (9)
```

The algorithm is:

```text
StarSample(N,r,q):
    if r=0: return the empty word (necessarily q=e)
    for i=1,...,N-1:
        w_i <- A_N(r-1,q(i N)) using (3)--(4)
    draw I with probability w_I / sum_i w_i
    prefix <- StarSample(N,r-1,q(I N))
    return prefix followed by (I N)
```

Only `N-1` labeled candidates are considered at a step; no permutation group
and no partition family is enumerated.  If the chosen last factor is `i`, the
prefix fiber has size `w_i`.  By induction, a word in this branch has
probability

```text
(w_i/A_N(r,q)) * (1/w_i) = 1/A_N(r,q).
```

Thus the output is exactly uniform and evaluates to the requested actual
labeled `q`.  The implementation stores the chosen factors from last to first
and reverses them before returning, matching the displayed-word convention.

To make each weighted choice exact, draw a uniform integer in
`{0,...,W-1}`, where `W=sum_i w_i`, using fair-bit rejection, then locate its
cumulative-weight interval.  This is a Las Vegas procedure with expected
fewer than two bit blocks per choice and introduces no approximation.

## 5. Arithmetic and bit complexity

For a single term (3), truncate every series at `g_s<=k`.  There are

```text
(n_s-2) + length(lambda_s) <= 2N-2
```

series factors.  Sequential schoolbook convolution costs `O(N k^2)` rational
operations.  Formula (4) has at most `N` support-size terms, hence one
`A_N(k,q)` count costs `O(N^2 k^2)` rational operations.  At backward level
`r` the sampler evaluates at most `N-1` child counts.  Summing the bound over
`r=1,...,k` gives

```text
O(N^3 k^3) exact rational operations.                         (10)
```

This is deliberately conservative; caching equal cycle types can improve it
but is unnecessary for polynomiality.

Here is an explicit bit bound.  Up to degree `k`, every coefficient of
`F(a t)`, `a<=N`, has denominator dividing

```text
D = 2^k (k+1)!.
```

At most `2N-2` such series are multiplied.  Putting intermediate
coefficients over the common denominator `D^(2N-2)`, and bounding the number
of convolution summands by `(k+1)^(2N-2)`, shows that all unreduced
intermediate numerators and denominators have

```text
B = O(N k log(N+k))                                          (11)
```

bits.  Factorial prefactors have `O(k log k)` bits and do not change this
polynomial bound.  Therefore (10), with ordinary polynomial-time integer
arithmetic and gcd reduction on `B`-bit integers, is a polynomial Turing-time
algorithm.  Also `A_N(r,q)<=(N-1)^r`, so exact range draws use
`O(r log N)` expected fair bits per level and `O(k^2 log N)` over the sample.

The algorithm is polynomial in the numerical parameters `N` and `k` (and
hence in the internal length `L` when `k<=L`).  It is exact, so there is no
`epsilon` dependence and no error to add in a rank telescope.

## 6. The natural `H`-orbit DP and its state count

Although it is not needed by the polynomial sampler, the requested natural
orbit-state construction gives an independent exact recurrence.

Let `H=S_(N-1)` fix `N`.  An `H`-conjugacy orbit is described exactly by

```text
(a,lambda),
a      = length of the cycle containing N,
lambda = sorted multiset of lengths of all other cycles.      (12)
```

For `lambda=1^m_1 2^m_2 ...`, its labeled orbit has size

```text
(N-1)! / z_lambda,
z_lambda = product_j j^m_j m_j!.                             (13)
```

Indeed, a centralizer element in `H` must fix the pivot cycle pointwise up to
the only power fixing `N`, namely the identity, while its action on the other
cycles has centralizer size `z_lambda`.

Right multiplication of a representative by one star factor has these
pointed-type transitions:

```text
join:  (a,lambda) -> (a+j,lambda minus one j),
       multiplicity j*m_j(lambda);

split: (a,lambda) -> (b,lambda union {a-b}),
       multiplicity 1 for each b=1,...,a-1.                  (14)
```

The multiplicities sum to `N-1`.  If `D_r(alpha)` is the number of length-`r`
words ending at each one labeled endpoint of type `alpha`, then

```text
D_0(alpha) = 1{alpha=(1,1^(N-1))},
D_(r+1)(alpha) = sum_beta M(alpha,beta) D_r(beta).            (15)
```

Equation (15) is just the last-factor identity (9) grouped by type.  It also
supports exact backward labeled sampling by applying the individual factors
to the current actual endpoint.

The number of states is exactly

```text
S_N = sum_(a=1)^N p(N-a) = sum_(u=0)^(N-1) p(u),             (16)
```

and

```text
p(N-1) <= S_N <= N p(N-1).                                  (17)
```

This is rigorously superpolynomial.  Put `n=N-1` and choose the largest `m`
with `2+3+...+(m+1)=m(m+3)/2<=n`.  Every subset of
`{2,...,m+1}`, padded with enough parts `1` to sum to `n`, gives a different
partition of `n`.  Hence `p(n)>=2^m=2^Omega(sqrt(N))`.  The full orbit table
therefore has partition-scale state explosion; a stored all-length backward
table takes `Theta(k S_N)` integer entries and transitions take
`O(k N S_N)` arithmetic operations.

This is an obstruction only to that specified full-orbit-table
implementation.  It is not sampling hardness.  Equations (3)--(4) bypass the
table and demonstrate why the distinction matters.

## 7. Boundary and adversarial checks

- **`N=1`:** there is no generator; only the empty identity word exists.
- **`N=2`:** the unique generator `(1 2)` forces one word at each length;
  identity occurs exactly at even `k`, and `(1 2)` at odd `k`.
- **`k=0`:** (4) is one for `q=e` and zero otherwise.
- **Odd `k`:** possible exactly for odd `q`, subject to the minimal length.
- **Minimal endpoint length:** only `s=0,g_0=0` contributes and gives (7).
- **Pair padding:** for `N>=2`, every feasible word extends by any adjacent
  repeated star factor; this proves existence, not uniformity.  The sampler
  counts all padded and non-padded histories via (4) and (9).
- **Transitive versus nontransitive:** retaining only Féray's transitive term
  at ambient rank would incorrectly discard every support with `s<f`; (4)
  retains them all.

## 8. Reproducible exact checks

Artifacts:

- `star_bridge.py`: exact formula, feasibility, pointed-orbit DP, and sampler;
- `run_checks.py`: direct labeled walk, orbit-transition, recurrence, boundary,
  and fixed-seed sampler checks;
- `results.json`: machine-readable output;
- `plan.md`, `checkpoint.md`, and this report.

Reproduction command (CPython 3.12.3, no nonstandard dependencies):

```bash
python3 experiments/20260901-rank-recursive-identity-bridge-goal/roles/r3-star/run_checks.py \
  --max-n 5 --max-k 6 --seed 20260901 --draws 2000 \
  --output experiments/20260901-rank-recursive-identity-bridge-goal/roles/r3-star/results.json
```

The direct endpoint walk, formula (4), and orbit DP agree for every endpoint
for `1<=N<=5` and `0<=k<=6`:

```text
1071 exact endpoint count equalities
918 exact last-factor recurrence equalities
153 exact labeled orbit-transition-multiplicity equalities
```

In particular, the required every-endpoint check through `N=5,k=6` passed.
The direct table also sums to `(N-1)^k` at every tested rank and length.
Fixed-seed samples in four nontrivial fibers always evaluated to the requested
endpoint.  Their empirical frequencies are reported only as smoke tests; the
uniformity conclusion is the induction after (9), not a statistical claim.

The state-growth calculation independently records `S_10=97`,
`S_20=2087`, `S_50=1091745`, and `S_100=1452423276`, consistent with the
proved partition-scale bound.

## 9. Dependencies, limitation, and handoff

Directly proved here: feasibility (1), (5); support decomposition (4), (8);
last-factor sampler and exact uniformity (9); pointed orbit descriptor,
transitions, state count, and superpolynomial bound (12)--(17); arithmetic and
random-bit complexity.

Audited primary input: Féray Theorem 1.2 for the arbitrary-length transitive
count, with Proposition 1.1 and Lemma 3.1 for its precise scope.  Independent
minimal-case corroboration: Irving--Rattan Theorem 1.1 and Corollary 1.2.

The first remaining issue is no longer inside R3.  The branch sampler R2 must
combine these computable values `A_N(k,h^{-1}g)` with lower-rank bridge counts
and sample the actual labeled `h` without enumerating `S_(N-1)`.  This report
does not claim that the full rank recursion is polynomial.

role: r3-star
claim: Every feasible prescribed-endpoint length-k star bridge in S_N can be counted and sampled exactly in expected time polynomial in N and k by positive exact-support decomposition, Féray's transitive coefficient formula, and labeled last-factor recursion.
status: proved
assumptions: Exact fair random bits for weighted draws; audited use of Féray Theorem 1.2 under the identical map-composition convention.
evidence: report.md equations (1)-(17); star_bridge.py; exhaustive results.json checks for every endpoint through N=5,k=6.
independent_checks: Direct labeled endpoint DP and the independently derived pointed-orbit DP both match the coefficient formula in 1071 cases; a fresh cross-role/coordinator audit has been requested and remains outside this lane.
complexity: Conservative O(N^3 k^3) exact-rational operations on O(N k log(N+k))-bit integers, O(k^2 log N) expected random bits, polynomial space under recomputation, and zero total-variation error.
first_unproved_step: Outside R3: sample the weighted labeled branch h in the rank disintegration using lower-rank bridge counts and these star counts without enumerating S_(N-1).
verdict: promote
