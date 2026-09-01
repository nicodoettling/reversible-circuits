# R2 final report: positive branch sampling

Date: 2026-09-01 UTC

## Resolution

**Proved:** there is a positive polynomial-state sampler for a labeled
`(k,h)` whose law is uniformly negligible-error close to the exact branch law
throughout an explicit dense regime.  For the scheduled length `L=2N^3`, its
branch error is at most

```text
2 exp(-N^2/2)       for every N>=4 and every feasible g in S_N.       (1)
```

The construction never enumerates `S_(N-1)` or partitions.  It samples a
labeled `h`, not merely its cycle type, and all its weights are nonnegative
integers.

This is a material solution of the dense R2 primitive, but it is not by itself
a full recursive sampler theorem.  The guarantee applies to a call `(N,L,g)`
when its explicit pointwise bound is small.  R4/R5 must still prove that
arbitrary internal lengths remain in such a regime, provide a fallback when
they do not, and telescope the errors.  At fixed `N,L`, this method also does
not support a requested `epsilon` below its displayed error floor.

For exact sampling at arbitrary feasible short lengths, the final result is a
strict positive reduction to a labeled stabilizer-connection primitive.  The
natural type-cell table for that primitive is proved superpolynomial in its
declared state inventory; this is only a scoped implementation obstruction,
not a hardness theorem.

## 1. Convention and exact target

Permutations are maps and

```text
(alpha beta)(x)=alpha(beta(x));
```

the rightmost displayed factor acts first.  Let

```text
H = S_(N-1) <= S_N,
d = |T_(N-1)| = binom(N-1,2),
b = N-1,
A_s(h) = [h] C_(N-1)^s,
B_k(q) = [q] J_N^k.
```

For a feasible external endpoint `g`, R1 proves that the exact unnormalized
branch weight is

```text
w(k,h)=binom(L,k) A_(L-k)(h) B_k(h^(-1)g).                    (2)
```

Its normalizer is `[g]C_N^L`.  The target in this report is the normalized
law `P` from (2).  Put `s=L-k` and

```text
a=g^(-1)(N).                                                  (3)
```

## 2. A two-state positive star-coset sampler

As `h` ranges over `H`, `q=h^{-1}g` ranges over the left coset `Hg`.  This
coset has the elementary description

```text
q in Hg  iff  q(a)=N.                                        (4)
```

Indeed, `q=h^{-1}g` sends `a=g^{-1}(N)` to `N`.  Conversely, if `q(a)=N`,
then `h=gq^{-1}` fixes `N`.

Let `S_k(a)` be the number of displayed star words of length `k` whose product
`q` satisfies (4).  Read such a word in reverse displayed order, which is the
order in which its factors act on the token initially at `a`.  By symmetry,
only two token states matter.  If `u_j` counts `j`-step star sequences taking
the pivot token to the pivot and `v_j` does the same from any fixed lower
token, then

```text
u_0=1, v_0=0,
u_(j+1)=(N-1)v_j,
v_(j+1)=u_j+(N-2)v_j,                                        (5)
S_k(a)=u_k if a=N, and v_k otherwise.
```

These counts also give an exact labeled backward sampler.  At a token state
`x` with `j` steps left, choose the next lower label `i` with weight equal to
the `(j-1)`-step completion count from `(i N)(x)`.  Reverse the sampled
applied-order factors to obtain the displayed word `v`.  Every admissible
word is chosen with probability `1/S_k(a)`.  Its endpoint `q` is therefore
chosen with probability `B_k(q)/S_k(a)`, and

```text
h=gq^(-1)                                                     (6)
```

is an actual labeled member of `H`.  Equations (3)--(6) independently confirm
the `h^{-1}g` orientation from R1.

## 3. The positive two-sided sampler

The sampler uses the fact that one of `s` and `k` is at least `L/2`.

### 3.1 Old-long region: `s>=k`

Replace the old endpoint count by its parity-uniform value

```text
Abar_s(h)=d^s * 2/(N-1)!     when sign(h)=(-1)^s.             (7)
```

Keep `B_k(h^{-1}g)` exact.  The total approximate mass at `k` is

```text
binom(L,k) d^s * 2/(N-1)! * S_k(a).                          (8)
```

Conditionally on `k`, use the token sampler in Section 2 and return (6).  This
samples the exact `B`-weighted labeled coset without evaluating `B` at each
endpoint and without listing `H`.

### 3.2 Star-long region: `k>s`

Keep `A_s(h)` exact and replace the star endpoint count by

```text
Bbar_k(q)=b^k * 2/N!         when sign(q)=(-1)^k.             (9)
```

Since `sum_h A_s(h)=d^s`, the approximate mass at `k` is

```text
binom(L,k) d^s b^k * 2/N!.                                  (10)
```

Conditionally on `k`, draw `s` independent uniform old transpositions and
return their displayed product `h`.  This directly samples the labeled law
`A_s(h)/d^s`; no endpoint count is evaluated.

### 3.3 One exact integer draw for `k`

Multiplying (8) and (10) by the common constant `N!/2` gives the integer
weights

```text
W_k = N binom(L,k)d^s S_k(a),    s>=k,
W_k =   binom(L,k)d^s b^k,       k>s.                        (11)
```

Draw `k` proportionally to (11), then use the appropriate labeled procedure
above.  This defines `Q` entirely through positive counts.

In the old-long region the procedure already produces the star word.  In the
star-long region, the proved R3 algorithm can subsequently sample a uniform
star word with endpoint `h^{-1}g`.  Whenever the pointwise error below is
less than one, approximate and exact supports coincide, so that fiber is
nonempty.  Applying the same exact conditional R3 kernel to `P` and `Q`
preserves their TV distance.  R3 uses conservative polynomial Turing
complexity `O(N^3k^3)` exact-rational operations on polynomial-bit integers.

## 4. Pointwise periodic mixing bounds

The conditioning on `g` requires pointwise relative bounds, not merely total
variation mixing of an unconditioned endpoint.

### 4.1 General Fourier lemma

Let a symmetric walk on a finite group `G` have all generators odd.  Remove
the trivial and sign representations, and suppose every remaining Fourier
block has operator norm at most `rho`.  Fourier inversion, the trace bound
`|Tr(UM)|<=dim(U)||M||`, and `sum dim(lambda)^2=|G|` imply that, on the parity
class reachable at time `t`,

```text
| P^t(e,x)/(2/|G|) - 1 | <= (|G|-2)/2 * rho^t.              (12)
```

The trivial and sign blocks give exactly the `2/|G|` term.  This derivation is
also why the prefactor is `(|G|-2)/2`, rather than an unconditioned mixing
constant.

### 4.2 Old all-transposition endpoint

For the nonlazy all-transposition walk on `S_r`, the normalized class sum is
scalar in irreducible shape `lambda`, with eigenvalue equal to the
transposition character ratio, equivalently the sum of Young-diagram
contents divided by `binom(r,2)`.  Apart from `(r)` and `(1^r)`, the largest
absolute value is attained at `(r-1,1)` and its transpose:

```text
rho_old(r)=(r-3)/(r-1).                                     (13)
```

One elementary proof moves boxes upward to maximize the content sum; among
non-row diagrams the maximizer is `(r-1,1)`, whose content sum is
`binom(r-1,2)-1`.  Transposition gives the negative extremum.

Thus, for `r>=4`,

```text
delta_old(r,t)=(r!-2)/2 * ((r-3)/(r-1))^t.                 (14)
```

For `r=2` the parity classes are singletons.  For `r=3`, the walk is exactly
parity-uniform after every positive time.  These are handled directly.

The representation formulas used in (12)--(14) are also visible in
Diaconis--Shahshahani, *Generating a Random Permutation with Random
Transpositions* (1981), inversion formula (2.2), class transform (2.6), and
transposition ratio (2.8):
<https://doi.org/10.1007/BF00535487>.  Their displayed walk includes holding;
here the holding eigenvalue is removed and the pure transposition ratio is
used.  Symmetry of transpositions makes left/right convolution conventions
equivalent for this bound.

### 4.3 Star endpoint

The nonlazy star transition operator is `J_N/(N-1)`.  In a
Young/Gelfand--Tsetlin basis, `J_N` has eigenvalue equal to the content of the
box containing `N`.  Only the trivial and sign tableaux have contents
`N-1` and `-(N-1)`; every other content has absolute value at most `N-2`.
Consequently

```text
rho_star(N)=(N-2)/(N-1),
delta_star(N,t)=(N!-2)/2 * ((N-2)/(N-1))^t.                (15)
```

The primary spectral input is Novak--Schvartzman, *Cutoff for the Star
Transposition Random Walk*, equations (2.1) and (3.3):
<https://jinovak.com/wp-content/uploads/2021/05/starcutoff.pdf>.  They use the
lazy operator `(I+J_N)/N`; removing `I` and normalizing by `N-1` gives (15).

## 5. Uniform branch error

Define, with the low-rank conventions above,

```text
Delta(N,L) = max{
  delta_old(N-1,ceil(L/2)),
  delta_star(N,floor(L/2)+1)
}.                                                           (16)
```

In the old-long region, the ratio between exact and approximate
unnormalized weights is `A_s(h)/Abar_s(h)`.  In the star-long region it is
`B_k(q)/Bbar_k(q)`.  Equations (14)--(16) put every such ratio in
`[1-Delta,1+Delta]`.

If `Delta<1`, the supports coincide.  If `Z/Zbar` is the ratio of
normalizers, it too lies in this interval.  Therefore

```text
d_TV(P,Q)
 <= (1/(2(1-Delta))) E_Q |w/wbar - Z/Zbar|
 <= Delta/(1-Delta).                                        (17)
```

This is uniform over the feasible external endpoint `g`; no bridge return
probability appears in the denominator.

For a requested `0<epsilon<=1`, (17) gives error at most `epsilon` whenever

```text
Delta(N,L) <= epsilon/(1+epsilon).                           (18)
```

A simple sufficient dense-length condition follows from
`1-x<=exp(-x)` and `m!<=m^m`.  Put
`delta_0=epsilon/(1+epsilon)`.  For `N>=5`, it suffices that

```text
L >= max{
 (N-2)((N-1)log(N-1)+log(1/delta_0)),
 2(N-1)(N log N+log(1/delta_0))
}.                                                           (19)
```

The runtime is polynomial in `N,L,log(1/epsilon)` on inputs satisfying (18)
or (19).  At a fixed length, however, decreasing `epsilon` cannot force
`Delta` lower; (19) is a regime condition, not an arbitrary-precision
mechanism.

### Scheduled specialization

Take `L=2N^3`.  Every region uses a mixed segment of length at least `N^3`.
For `N>=5`,

```text
delta_old <= (N-1)!/2 * exp(-2N^3/(N-2)) <= exp(-N^2).
```

For `N>=4`,

```text
delta_star <= N!/2 * exp(-N^3/(N-1)) <= exp(-N^2/2).
```

The `N=4` old walk has rank three and is already exactly parity-uniform.
Thus `Delta<=exp(-N^2/2)<1/2`, and (17) proves (1).

## 6. State count and Turing complexity

The positive dense sampler stores the two arrays `(u_j,v_j)`, powers and
`L+1` branch weights: `O(L)` integer states.  Counts are bounded by
`(N-1)^L`; after the binomial and old-factor terms are included, every weight
has `O(L log N)` bits.  The arrays, binomial coefficients, and powers require
`O(L)` polynomial-bit integer operations.

Sampling `k` uses one exact range draw and a cumulative scan.  The token
bridge and old-word generation take at most `L` factor steps and return an
actual labeled `h`; displayed products can be updated by swapping two images.
A conservative implementation uses `O(L^2 log N)` expected fair random bits
because the sequential token completion totals have decreasing
`O(L log N)` bit lengths.  All arithmetic and storage are polynomial in the
numerical parameters.  No factorial-size object is generated.

If the star word is also required in the star-long case, compose this with
R3's polynomial exact conditional sampler.  Its exactness adds no branch
error.

## 7. What the exact type compression does and does not solve

Let `lambda(h)` be the ordinary cycle type of `h in H`, and let `mu(q)` be
the pointed cycle type recording the length of the cycle containing `N` and
the partition of all other cycle lengths.  Both endpoint counts are constant
on these types.  Define the nonnegative connection multiplicity

```text
M_g(lambda,mu)
 = #{h in H : lambda(h)=lambda,
              mu(h^(-1)g)=mu}.                              (20)
```

Then the exact law has the positive cell expansion

```text
binom(L,k) A_s(lambda) B_k(mu) M_g(lambda,mu).               (21)
```

R3 makes every fixed `B_k(mu)` polynomially countable and its labeled star
fiber polynomially sampleable.  That fact does not sample (21): one must
still draw a joint cell with its connection multiplicity and an actual
labeled `h` uniformly from the chosen cell.

There are exactly

```text
p(N-1) ordinary lower-rank cycle types,
P_N=sum_(u=0)^(N-1)p(u) pointed types,
p(N-1) P_N rectangular type cells per k.                    (22)
```

Even for `g=e`, precisely `p(N-1)` set-theoretically nonempty cells occur,
because `mu(h^{-1})=(1,lambda(h))`.  If `n=N-1` and `m` is maximal with
`2+...+(m+1)<=n`, every subset of `{2,...,m+1}`, padded by parts `1`, gives a
distinct partition of `n`.  Hence

```text
p(n)>=2^m=2^Omega(sqrt(n)),                                  (23)
```

so an implementation that explicitly materializes even the nonempty
identity-endpoint type cells is superpolynomial.  The full rectangular table
is larger.  The exact computed inventories include

| `N` | `p(N-1)` | `P_N` | product |
|---:|---:|---:|---:|
| 10 | 30 | 97 | 2,910 |
| 20 | 490 | 2,087 | 1,022,630 |
| 50 | 173,525 | 1,091,745 | 189,445,051,125 |
| 100 | 169,229,875 | 1,452,423,276 | 245,793,409,444,570,500 |

Each numeric cell weight itself has only polynomial bit length:
`A_s<=d^s`, `B_k<=b^k`, `M_g<=(N-1)!`, and `binom(L,k)<=2^L`, giving
`O(L log N+N log N)` bits.  It is the number and labeled construction of
cells, not the size of one integer, that fails.

Storing every member of every cell reverts to `(N-1)!` endpoints.  A positive
alternative is to sample uniformly from the conjugacy class `lambda` and
reject until `mu(h^{-1}g)=mu`, but its expected trials are
`|class(lambda)|/M_g(lambda,mu)`, for which there is no polynomial uniform
bound.  Signed character/connection-coefficient formulas do not supply a
probabilistic sampler.

Thus (22)--(23) refute only the explicit type-table implementation.  They do
not rule out a generating-function or direct labeled connection sampler.

## 8. Boundaries and arbitrary internal states

- **`N=2`.** `H=S_1`, so `s=0`, `k=L`, and `h=e` are forced.  The sole star
  word has the parity-prescribed endpoint.  R2 is exact.
- **`N=3`.** Parity classes of `H=S_2` are singletons, so (7) is exact for
  every `s`; using the old-long/token construction for every `k` gives an
  exact branch sampler.
- **`N=4`.** The all-transposition walk on `H=S_3` is parity-uniform for every
  `s>=1`.  Those branches use the exact token construction.  The sole `s=0`
  branch has `h=e` and mass `B_L(g)`, computable by R3.  Hence R2 is also exact
  at this rank.
- **`L=0`.** Feasibility forces `g=e`; the only branch is `(k,h)=(0,e)`.
- **Odd `L`.** Identity is infeasible.  For an arbitrary odd `g` satisfying
  the usual transposition-length bound, all branch signs in (2) and (11)
  agree automatically.
- **Minimal endpoint length.** The exact branch law is well-defined, but for
  `N>=5` a short call generally has `Delta>=1`; no approximation claim is
  made.  This is part of the surviving exact connection primitive.
- **Pair padding.** Appending equal transposition pairs proves feasibility at
  all same-parity larger lengths, but does not itself imply (18).  The explicit
  length bound must still be checked.
- **Internal recursion.** The theorem accepts every feasible endpoint, but
  not every feasible length.  It is therefore insufficient to claim recursive
  closure without the R4/R5 length and telescope analysis.

## 9. Exact validation and independent audit

The standard-library script `branch_audit.py` ran at repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993` under Python 3.12.3, with seed
`20260901` only for output smoke tests and no nonstandard dependency.

Exact command:

```text
/usr/bin/time -v python3 experiments/20260901-rank-recursive-identity-bridge-goal/roles/r2-branch/branch_audit.py --max-small-n 5 --max-small-length 8 --dense-n 4 5 --output experiments/20260901-rank-recursive-identity-bridge-goal/roles/r2-branch/results.json > experiments/20260901-rank-recursive-identity-bridge-goal/roles/r2-branch/run.log 2>&1
```

It performed:

- 1,368 exact branch-normalizer and feasibility checks for all endpoints;
- 532 exact small-fiber TV calculations;
- 126 direct star-coset versus token-recurrence equalities;
- 125 special exact low-rank positive marginal checks;
- 1,911 labeled sampler smoke checks;
- an exact calculation for every feasible endpoint at `N=4,L=128` and
  `N=5,L=250`.

The maximum exact dense TV values were

| `N,L` | endpoints | maximum exact TV | bound (17) |
|---|---:|---:|---:|
| `4,128` | 12 | `6.86151696931699e-13` | `3.939679082071359e-11` |
| `5,250` | 60 | `1.0035021268542645e-19` | `1.067999867952456e-14` |

These finite values are exact rational calculations stored in `results.json`;
their decimal renderings are only for readability.  They corroborate but do
not prove the general spectral theorem.

The fresh R6 worker independently reimplemented the branch laws rather than
importing this script.  Its `checkpoint.md`, `exact_redteam.py`, and
`results.json` reproduce the coset orientation, common scale, token
recurrence, exact rational dense maxima, maximizing endpoints, and bound for
every feasible dense endpoint.  It also records the adversarial short identity
cases

```text
N=3,L=4: 56/783,
N=4,L=4: 9/136,
N=4,L=6: 29/287,
```

for the deliberately two-sided approximate rule.  These nonzero short errors
are retained and illustrate why dense hypotheses cannot be dropped.  The
special low-rank exact sampler in Section 8 uses the old-flat rule beyond the
two-sided split and is a separate claim.

SHA-256:

```text
2e749744f26b017dbdb494c0d541f7544429fc09e6907142b499e0e5dccc134f  branch_audit.py
c8525ef3218fdcf477d51202d4beea36b9c3196b32a823d0c4eae2ac0d87bb92  results.json
4e83f7ac62af38453f5818624b4d3544b45fed406fdf7e4752841777720c1b17  run.log
```

## 10. Exact remaining primitive

The first unresolved exact R2 statement is now:

```text
Positive stabilizer-connection sampler.
Given N,s,k,g and the nonnegative class weights A_s(lambda) and the
polynomially evaluable R3 weights B_k(mu), sample a cell (lambda,mu) with
weight A_s(lambda)B_k(mu)M_g(lambda,mu) and then a uniform labeled
h in that cell, in time polynomial in N,s,k, without enumerating partitions
or S_(N-1).
```

Solving this would cover the short/unmixed calls not certified by (18).
Alternatively, R4/R5 may prove those calls have negligible total mass and
use the dense sampler with an explicit telescope.  The present report proves
neither alternative.

role: r2-branch
claim: The positive two-sided labeled branch sampler (11) has d_TV at most Delta/(1-Delta) uniformly over feasible g whenever Delta<1, and at L=2N^3 this is at most 2 exp(-N^2/2); exact arbitrary-short R2 reduces to the stated positive stabilizer-connection sampler.
status: proved
assumptions: Exact fair random bits; the standard transposition character-ratio spectrum and Jucys--Murphy content spectrum audited above; the finalized R3 theorem when a conditional star word is requested in the star-long branch.
evidence: Sections 2--8 give the positive algorithm, pointwise proof, state and bit complexity, dense specialization, boundaries, and scoped type-table obstruction; branch_audit.py and results.json give all-endpoint exact checks.
independent_checks: The fresh R6 implementation independently reproduced the formulas and all exact dense maxima/bounds for every feasible endpoint at N=4,L=128 and N=5,L=250; its checkpoint.md and results.json report no mismatch.
complexity: O(L) polynomial-bit states and polynomial Turing time for the branch draw, with O(L^2 log N) conservative expected random bits; composing the star-long branch with R3 costs its conservative O(N^3 L^3) exact-rational operations and preserves TV.
first_unproved_step: Prove the positive stabilizer-connection sampler above, or prove an R4/R5 internal-length invariant and summable telescope that never requires it outside negligible mass.
verdict: promote
