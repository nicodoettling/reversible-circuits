# Fresh nonauthor audit of the R3 exact star-bridge algorithm

Date: 2026-09-01
Auditor: `r2-branch` worker, after completion of its own R2 report
Artifact under audit: `roles/r3-star/report.md`
Target: count and sample uniformly the length-`k` words in
`{(i N):1<=i<N}` having prescribed product `q in S_N`

## Audit outcome

**Accept.**  The R3 count formula, exact-used-support decomposition,
feasibility criterion, last-factor orientation, exact-uniform backward
sampler, and polynomial Turing-time claim are correct.  The primary theorem
has the claimed exponent and normalization.  An implementation written from
scratch, without importing the R3 implementation, agrees with a separate
labeled endpoint-and-support dynamic program in every tested case.

This accepts an exact polynomial-time solution of R3.  It does not imply that
the joint rank branch `(k,h)` in R2, or arbitrary-endpoint recursive closure
in R4, is exact polynomial time.

## 1. Convention and primary-source audit

Permutations here are maps and

```text
(p q)(x) = p(q(x)).
```

A displayed word `t_1 ... t_k` therefore acts right-to-left as a map.  If a
factor is appended on the right, the running product changes from `p` to
`p t`.

I inspected Valentin Féray,
[*Partial Jucys--Murphy elements and star
factorizations*](https://arxiv.org/html/0904.4854v2), arXiv:0904.4854v2,
directly rather than relying on the R3 report's transcription.

- Section 1.1.1 defines a transitive factorization
  `sigma=g_1...g_r` by requiring the factors to generate the full symmetric
  group.  Section 1.1.2 observes that for the stars `(i n)` this is equivalent
  to using every star generator at least once.
- Definition 2.1 defines partial-permutation multiplication as
  `tilde(sigma) o tilde(sigma')`.  Thus its displayed products use the same
  map convention above; no inversion or word reversal is required.
- Proposition 1.1 states that the transitive length-`r` star count depends
  only on the ordinary conjugacy class, despite the distinguished pivot.
- Theorem 1.2 states, for a partition `lambda` of the active size `n`,

  ```text
  r!/n! * product_i lambda_i
    * [t^g] F(t)^(n-2) product_i F(lambda_i t),

  g = r-(|lambda|+length(lambda)-2),
  F(t) = 2 sinh(t/2)/t.
  ```

  In particular the exponent is `n-2`, not `length(lambda)-2`, and the
  normalization is `r!/n!`, not `r!/z_lambda` or `r!/(n-1)!`.
- Lemma 3.1 identifies the transitive part with full partial-permutation
  support.  Equation (12), after the paper's coefficient derivation, repeats
  the normalization as `r!/|lambda|!`; since `lambda` partitions `n`, this is
  exactly the `r!/n!` in Theorem 1.2.

The paper covers arbitrary factor count, not only minimal factorizations.
The R3 use of this theorem is exact and within its stated transitive scope.

## 2. Independently reconstructed count

Write

```text
A_N(k,q) = [q] J_N^k,
J_N       = sum_(i<N) (i N).
```

Let the cycle of `q` containing `N` have length `a`.  Let
`b_1,...,b_r` be the lengths of all nontrivial cycles not containing `N`,
and let `f` be the number of fixed lower labels.  Define

```text
mu       = (a,b_1,...,b_r),
n_0      = |mu|,
c_0      = length(mu),
ell_*(q) = n_0+c_0-2.
```

The part `a=1` is retained when the pivot is fixed; fixed lower labels are
not put in `mu`.  For `s=0,...,f`, set

```text
lambda_s = mu union 1^s,
n_s      = n_0+s,
g_s      = k-(n_s+length(lambda_s)-2)
         = k-ell_*(q)-2s.
```

For `n_s>=2`, Féray's theorem gives the transitive count

```text
T_k(lambda_s)
 = k!/n_s! * product_(u in lambda_s) u
   * [t^g_s] F(t)^(n_s-2) product_(u in lambda_s) F(u t).   (1)
```

For the singleton active set, the necessary separate convention is
`T_0((1))=1` and `T_k((1))=0` for `k>0`.  The audited arbitrary-support
formula is

```text
A_N(k,q) = sum_(s=0)^f binom(f,s) T_k(lambda_s).             (2)
```

### Proof of the exact-used-support decomposition

For a star word `w`, put

```text
U(w) = {i<N : (i N) occurs in w}.
```

Every moved lower label of `q` lies in `U(w)`, since factors outside a label
fix that label.  Any other member of `U(w)` is therefore one of the `f`
fixed lower labels of `q`.  Consequently every word belongs to a unique cell

```text
U(w) = {moved lower labels of q} union S,
S subseteq {fixed lower labels of q}.
```

Fix one such `S`, of size `s`, and restrict to the active set
`{N} union U(w)`.  By exactness of the support, every active star generator
occurs.  Its star graph is connected, so the generated group is the full
symmetric group on that active set.  Thus the restricted factorization is
transitive.  Conversely, a transitive star factorization on that active set
uses every one of its star generators and hence has exactly that support.
The restricted endpoint has cycle type `lambda_s`.

Relabel the active set so that `N` becomes its last label.  Proposition 1.1
makes the count depend only on `lambda_s`, so every one of the `binom(f,s)`
choices of `S` contributes exactly (1).  The cells are disjoint, proving
(2).  This also explains why retaining only the `s=f` term would count only
ambient-transitive words and would be wrong for the arbitrary star fiber.

All coefficients of

```text
F(u t) = sum_(d>=0 even) u^d t^d/(2^d(d+1)!)
```

are nonnegative.  Formula (2) is therefore a positive sum over genuine
disjoint support cells; it is not a signed character expansion.

## 3. Feasibility, minimality, and padding

The claimed minimum

```text
ell_*(q) = (a-1) + sum_j (b_j+1)                            (3)
```

is correct.

For the lower bound, work on the exact active set of a transposition word.
After `j` factors, let `d_j` be the number of components of its factor graph
and `c_j` the number of cycles of its prefix product, both on the fixed
active vertex set of size `v`.  Then

```text
Phi_j = j-v-c_j+2d_j
```

starts at zero.  An edge joining graph components decreases both `d_j` and
`c_j` by one, leaving `Phi` unchanged.  An edge within one graph component
either splits a permutation cycle, again leaving `Phi` unchanged, or joins
two permutation cycles, increasing `Phi` by two.  Hence `Phi_j>=0`.
At a connected endpoint this gives

```text
k >= v+c-2.                                                 (4)
```

With no optional fixed label, `(v,c)=(n_0,c_0)` and (4) gives (3).  Exact
support containing `s` optional fixed labels raises both `v` and `c` by `s`,
so that cell has minimum `ell_*(q)+2s`.  This agrees exactly with `g_s` in
(1).

The bound is attained under the declared convention.  If the pivot cycle is
`(N x_2 ... x_a)`, then

```text
(N x_2 ... x_a) = (N x_a)(N x_(a-1))...(N x_2).
```

For a nonpivot cycle `(y_1 ... y_b)`,

```text
(y_1 ... y_b)
 = (N y_1)(N y_b)(N y_(b-1))...(N y_2)(N y_1).
```

Each second block fixes `N` and has the displayed nonpivot cycle as product.
Concatenating the blocks therefore realizes the disjoint cycles of `q` in
length (3).  Sign forces `k` and `ell_*(q)` to have the same parity.  For
`N>=2`, appending `(1 N)(1 N)` supplies arbitrary padding by two.  Thus

```text
A_N(k,q)>0  iff  k>=ell_*(q) and k=ell_*(q) mod 2,           (5)
```

for `N>=2`.

Boundary cases are consequently complete:

- `N=1`: the generator alphabet is empty; only `(k,q)=(0,e)` is feasible.
- `N=2`: there is one generator.  The identity has one word at each even
  length and none at odd length; `(1 2)` has one word at each odd length and
  none at even length.
- `k=0`: only `q=e` has the empty word.
- Odd `k`: feasible precisely for an odd endpoint satisfying (5).
- Minimal length is (3); every larger feasible length follows by pair
  padding.  Pair padding proves existence, not uniformity, and the sampler
  below counts all histories rather than only padded ones.

## 4. Last-factor orientation and exact sampling

Suppose a length-`r` word has prefix product `p` and last factor
`tau_i=(i N)`.  Under the convention above,

```text
q = p tau_i,
p = q tau_i,
```

because `tau_i` is an involution.  Hence the correct last-factor recurrence
is

```text
A_N(r,q) = sum_(i<N) A_N(r-1,q(i N)).                       (6)
```

The right multiplication is material.  The independent check found the
small witness `N=3`, `r=2`, `q=(1 2 3)`: the prefix weights for last factors
`(1 3),(2 3)` are `(1,0)`, whereas the left products
`(1 3)q,(2 3)q` give `(0,1)`.  Left multiplication can describe a
first-factor recurrence if the selected factor is prepended; it cannot be
substituted into the proposed append-last sampler.

The exact sampler computes the `N-1` nonnegative integers in (6), chooses
`I` with probability

```text
A_N(r-1,q(I N))/A_N(r,q),
```

recursively samples the actual labeled prefix endpoint `q(I N)`, and appends
`(I N)`.  No permutation fiber is enumerated.  Inductively, a word in branch
`I` has probability

```text
A_N(r-1,q(I N))/A_N(r,q)
  * 1/A_N(r-1,q(I N))
= 1/A_N(r,q).
```

Thus every output word is exactly uniform and has the prescribed labeled
endpoint.  A fair-bit rejection draw from the cumulative integer weights is
Las Vegas exact.  Zero-weight children are skipped; an infeasible root is
reported rather than sampled.

## 5. Polynomial Turing bit complexity

The rational-operation count in R3 does lift to polynomial bit complexity.
For all degrees `d<=k`, the denominator of a coefficient of `F(u t)`,
`u<=N`, divides

```text
D = 2^k (k+1)!.
```

A coefficient extraction in (1) multiplies

```text
M = (n_s-2)+length(lambda_s) <= 2N-2
```

truncated series.  A common denominator `D^M` therefore suffices.  Its bit
length is `O(N k log(k+2))`.  Bounding coefficient numerators by the factors
`u^d`, and the number of convolution choices by `(k+1)^M`, gives the
uniform bound

```text
B = O(N(k+1) log(N+k+2))                                   (7)
```

bits for reduced intermediates (and only a constant multiple of this before
gcd reduction).  The factorial prefactor contributes
`O(k log(k+2)+N log(N+1))` bits, already polynomial and covered by the same
coarse bound after treating `k=0` separately.

Schoolbook truncated convolution takes `O(N k^2)` rational operations per
support-size term.  There are at most `N` values of `s`, so one endpoint
count takes `O(N^2 k^2)` rational operations.  At each of `k` backward
levels the sampler computes at most `N-1` child counts.  Recomputing rather
than relying on memoization therefore gives the conservative bound

```text
O(N^3 k^3) rational operations on O(B)-bit integers,
```

or, with ordinary schoolbook integer arithmetic and Euclidean gcd, a coarse
`O(N^3 k^3 B^2)` polynomial bit-operation bound.  Polynomial working space
suffices: a count uses polynomially many truncated coefficients, and the
sampler stack has depth `k`.

Finally `A_N(r,q)<=(N-1)^r`, so a weighted choice needs
`O(r log N)` expected fair bits.  Summing over levels gives
`O(k^2 log N)` expected random bits.  The algorithm is polynomial in the
numeric parameters `N,k` and outputs `k` factors; it is exact, so it has no
`epsilon` or TV-error dependence.

## 6. Independent exhaustive checks

The script `audit_r3_independent.py` contains no import from
`roles/r3-star`.  It independently implements (1)-(2), and separately builds
a direct dynamic program indexed by the actual labeled endpoint and the
exact lower-label support mask.  It then symbolically expands the backward
kernel and checks the exact rational probability of every word in every
tested nonempty fiber.

Reproduction, with CPython 3.12.3 and no nonstandard dependencies:

```bash
python3 experiments/20260901-rank-recursive-identity-bridge-goal/roles/r2-branch/audit_r3_independent.py \
  --output experiments/20260901-rank-recursive-identity-bridge-goal/roles/r2-branch/audit_r3_results.json
```

Repository commit recorded by the artifact:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

Exact results:

```text
351  formula = brute endpoint equalities
3467 formula = brute exact-support-cell equalities
318  last-factor recurrence equalities
351  feasibility equivalences
29   total mass identities sum_q A_N(k,q)=(N-1)^k
152  endpoint minimality and +2 padding checks
145  nonempty fibers with symbolically exact uniform sampler laws
5324 individual words assigned and checked at probability 1/A_N(k,q)
```

The endpoint, support, feasibility, and sampler checks cover every endpoint
for `N=1,2,3,4` and every `k=0,...,6`, plus every endpoint in the complete
`N=5,k=6` slice.  Thus the `N=5` check is not a selected endpoint smoke test.
All support masks, including zero-count cells, were checked.  Selected totals
include

```text
A_3(4,e)=6,
A_4(6,e)=93,
A_5(6,e)=244.
```

Finite checks are used here to falsify translation, support, recurrence, and
implementation errors.  The general theorem follows from the support
bijection, Féray's theorem, and the induction above, not from enumeration.

## 7. Secondary pointed-state check

The natural `S_(N-1)`-conjugacy state is a pivot-cycle length `a` together
with a partition of the remaining `N-a` labels.  Hence its exact state count
is

```text
S_N = sum_(u=0)^(N-1) p(u).
```

The independent partition recurrence reproduces
`S_10=97`, `S_20=2087`, `S_50=1091745`, and
`S_100=1452423276`.  Since `S_N>=p(N-1)=2^Omega(sqrt(N))` by the elementary
distinct-parts subset construction, a full pointed-orbit table is
superpolynomial.  This is only an obstruction to that table implementation;
formula (2) and the last-factor sampler avoid it.

## 8. Dependencies and exact remaining concern

Accepted external input: Féray, Proposition 1.1 and Theorem 1.2, with Lemma
3.1 and Equation (12) used to audit scope, convention, and normalization.
Everything turning that transitive enumeration into an arbitrary-support
count and an exact sampler was independently proved above.

The exact remaining concern is outside R3: repeated polynomial calls to the
star counter solve the conditional star word once `(k,h)` is known, but do
not themselves sample the joint rank branch weighted by the lower-rank bridge
count.  This audit also does not reprove Féray's published coefficient
theorem from first principles; it verifies its exact primary-source statement
and that every use made here satisfies its hypotheses.

audit_verdict: accept
accepted_claim: Every feasible prescribed-endpoint star bridge can be counted and sampled exactly in expected Turing time polynomial in N and k, with zero total-variation error.
remaining_concern: No unresolved step remains inside the R3 reduction beyond the cited Féray theorem; the first external open step is joint rank-branch sampling/recursive closure, not star-bridge sampling.
