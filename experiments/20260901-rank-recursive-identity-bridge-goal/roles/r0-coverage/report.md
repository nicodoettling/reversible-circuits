# R0 final report: complete coverage under the dense identity bridge

## Outcome

**Proved.**  The identity-bridge conditioning does not spoil exponential
complete-transposition coverage at the scheduled length.  In fact, for every
`N>=2`, with `L_N=2N^3` and `U_N` uniform on `Omega(N,L_N;e)`,

```text
Pr_{w~U_N}[not Full_N(w)] <= exp(-2N).              (R0)
```

Here `Full_N` means that all `binom(N,2)` transpositions occur, so the
unweighted support graph is the complete graph `K_N` (not
`K_(binom(N,2))`).  The proof works with exact bridge return counts.  It is
not an unconditioned coupon-collector calculation.

## 1. Target, convention, and feasibility

Permutations are maps and

```text
(sigma tau)(x) = sigma(tau(x)).
```

Thus the displayed word `t_1...t_L` acts on points right-to-left.  A random
walk implemented by successive right multiplication has states

```text
e, t_1, t_1t_2, ..., t_1...t_L,
```

so its return count uses exactly the displayed word convention.

The target in this report is the global fixed-length uniform bridge law on

```text
Omega(N,L;e) = {(t_1,...,t_L) in T_N^L: t_1...t_L=e}.
```

For completeness, let `c(g)` count all cycles of `g`, including fixed points,
and put `ell_T(g)=N-c(g)`.  For `N>=2`,

```text
Omega(N,L;g) is nonempty
iff L>=ell_T(g) and sign(g)=(-1)^L.                 (1.1)
```

Necessity follows because a transposition changes the cycle count by one and
has sign `-1`.  For sufficiency, under the convention above,

```text
(a_1 ... a_r)=(a_1 a_r)(a_1 a_(r-1))...(a_1 a_2).
```

Doing this for every nontrivial cycle gives `ell_T(g)` factors.  Append any
number of adjacent pairs `tt` to add an arbitrary even amount of length.

Consequences for the required boundary cases are:

- `L` odd and `g=e`: the fiber is empty, so there is no uniform identity
  target to which a probability statement could apply.
- `L=0`: the identity fiber is the singleton empty word.  It is not full for
  `N>=2`.
- `L=2`: every identity word is `tt`; it is full only when `N=2`.
- `N=2`: there is one transposition.  Endpoint parity determines the unique
  word at every feasible length.  Every positive-length word is full.
- At minimal endpoint length, (1.1) gives feasibility but generally not full
  support.  The coverage theorem below is a dense-length statement.

## 2. Quantified return-count theorem

### Theorem 2.1 (proved)

Let `N>=3`, `M=binom(N,2)`, and let `L>=0` be even.  If `U_(N,L)` is uniform
on `Omega(N,L;e)`, then

```text
Pr_{U_(N,L)}[not Full_N]
 <= M(1-1/M)^L + (M N!/2)(1-2/N)^L.               (2.1)
```

In particular, at `L=2N^3`, the right side is at most `exp(-2N)`.

### Proof

Fix one transposition `a`.  On `ell^2(S_N,unif)`, define right-convolution
operators

```text
P   = (1/M) sum_(t in T_N) R_t,
Q_a = (1/(M-1)) sum_(t in T_N, t!=a) R_t,
(R_t f)(x)=f(xt).
```

Both are real self-adjoint Markov operators.  If `p_L=P^L(e,e)` and
`q_L=Q_a^L(e,e)`, direct word counting gives

```text
|Omega(N,L;e)|                 = M^L p_L,
#{w in Omega(N,L;e): a absent} = (M-1)^L q_L.
```

Therefore the exact bridge-conditioned probability is

```text
Pr[a absent]
 = ((M-1)/M)^L q_L/p_L.                            (2.2)
```

This identity is the point at which the conditioning is retained exactly.

We next control `q_L`.  Regard the allowed transpositions `T_N minus {a}` as
the edges of the graph `G_a=K_N minus {a}` with unit rates.  Its interchange
generator, after identifying configurations with permutations, is

```text
calL_IP = sum_(t!=a)(R_t-I) = (M-1)(Q_a-I).         (2.3)
```

The graph `G_a` is connected for `N>=3`, and the transpositions on the edges
of any connected graph generate `S_N`.  Thus this Cayley walk is irreducible:
its `+1` eigenspace consists only of constants.  Sign twisting below then also
shows that its `-1` eigenspace consists only of `sgn`.

If the endpoints of the deleted edge are `u,v` and
`b=mathbf_e_u-mathbf_e_v`, the one-particle graph Laplacian is

```text
Delta_a = N I - J - b b^T.
```

On the orthocomplement of constants this is `N I-bb^T`.  Since
`||b||^2=2`, its eigenvalues there are `N-2` along `b` and `N` on the
remaining `N-2` dimensions.  Thus the one-particle spectral gap is exactly
`N-2`.

Caputo--Liggett--Richthammer, Theorem 1.1, says that on every weighted graph
the interchange-process spectral gap equals this one-particle gap.  Applying
it to (2.3), the largest eigenvalue of `Q_a` below `1` is

```text
rho = 1-(N-2)/(M-1).                               (2.4)
```

The source uses a continuous-time generator on particle configurations.  The
normalization in (2.3) translates it to this report's discrete-time operator.
Swapping positions versus right-multiplying labels changes the realization by
inversion/unitary conjugacy and does not change the spectrum.

There is one remaining parity point.  Constants and `sgn` are eigenvectors of
`Q_a` with eigenvalues `1` and `-1`.  If `S` denotes multiplication of a
function by `sgn`, then every allowed generator is odd, so

```text
Q_a S = -S Q_a.
```

Hence the spectrum is symmetric under `lambda -> -lambda`.  On
`W={1,sgn}^perp`, every positive eigenvalue is at most (2.4), and sign
twisting gives the same bound for the absolute value of every negative
eigenvalue.  Thus

```text
||Q_a|_W|| = rho.                                  (2.5)
```

For any right-Cayley operator all diagonal return probabilities are equal, so
the identity return probability is its trace divided by `N!`.  Since `L` is
even, every eigenvalue contributes a nonnegative `L`th power.  Separating the
`1` and `sgn` eigenvectors gives

```text
q_L <= 2/N! + rho^L.                               (2.6)
```

The same trace argument for `P`, using only its two eigenvectors `1` and
`sgn`, gives

```text
p_L >= 2/N!.                                       (2.7)
```

Combining (2.2), (2.6), and (2.7),

```text
Pr[a absent]
 <= ((M-1)/M)^L (1+(N!/2)rho^L).                  (2.8)
```

Union bound (2.8) over all `M` choices of `a`.  Finally,

```text
((M-1)/M)rho
 = (M-N+1)/M
 = (N-2)/N
 = 1-2/N.
```

This yields (2.1).  QED.

### Dense simplification

Let `L=2N^3`.  For `N>=3`, `2 log N<=N`, so `log M<=N`.  Also

```text
L/M = 4N^2/(N-1) >= 4N.
```

Using `1-x<=exp(-x)`, the first term of (2.1) is at most

```text
exp(log M-L/M) <= exp(-3N).                         (2.9)
```

The second is at most

```text
exp(log(M/2)+log(N!)-2L/N)
 <= exp(N+N^2-4N^2)
 <= exp(-3N).                                      (2.10)
```

Here `log(N!)<=N log N<=N^2`.  Since
`2 exp(-3N)<=exp(-2N)`, (R0) follows for `N>=3`.  For `N=2`, `L_2=16` and
the unique identity word uses the only transposition, so the failure
probability is zero.  Thus (R0) holds for every `N>=2`, stronger than the
requested sufficiently-large-`N` statement.

## 3. Primary-source dependency audit

The only non-elementary proof input is:

- P. Caputo, T. M. Liggett, and T. Richthammer, *Proof of Aldous' spectral
  gap conjecture*, Journal of the American Mathematical Society **23**(3)
  (2010), 831--851, **Theorem 1.1**, DOI
  [10.1090/S0894-0347-10-00659-4](https://doi.org/10.1090/S0894-0347-10-00659-4).
  It states equality of the interchange and one-particle random-walk spectral
  gaps for every weighted graph, exactly the input used on `G_a`.

This source was inspected at the theorem statement and at its definitions of
the random-walk and interchange generators.  No hypothesis of transitivity,
regularity, laziness, or completeness is added; `G_a` is a connected
unweighted graph for `N>=3`.

An optional independent full-walk cross-check uses P. Diaconis and M.
Shahshahani, *Generating a random permutation with random transpositions*,
Z. Wahrscheinlichkeitstheorie verw. Gebiete **57** (1981), 159--179,
DOI [10.1007/BF00535487](https://doi.org/10.1007/BF00535487): Lemma 7 gives
the transposition character-ratio formula, Lemma 10 its dominance
monotonicity, and Theorem 3/Corollary 3 give the convolution spectrum.  This
is used only by the symbolic diagnostic, not as a logical dependency of
Theorem 2.1.

## 4. Independent derivation and falsification checks

There is a second, looser operator route.  For the full walk, the same
spectral-gap theorem on `K_N`, plus sign twisting, gives

```text
||P|_W|| = 1-N/M.
```

The exact identity

```text
P=(1/M)R_a+((M-1)/M)Q_a
```

implies `||Q_a-P||<=2/M` and hence

```text
||Q_a|_W|| <= 1-(N-2)/M.
```

This independently recovers the checkpoint's slightly weaker version of the
same exponential R0 bound.  It checks the direct deleted-graph normalization.

The deterministic standard-library script
[exact_coverage_check.py](./exact_coverage_check.py) was run as

```text
python3 experiments/20260901-rank-recursive-identity-bridge-goal/roles/r0-coverage/exact_coverage_check.py
```

under Python 3.12.3 at repository commit
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.  It uses exact integer and
rational arithmetic.  No seed is applicable.  Machine-readable selected
output is in [exact_check_results.json](./exact_check_results.json).

The checks passed:

- every deleted edge gave the same return count for every tested even length
  through `N=5,L=6`;
- (2.2), (2.6), (2.7), and (2.8) held exactly for `N=3,4,5` at
  `L=0,2,4,6` and at the dense lengths `54,128,250`;
- exact coverage enumeration recovered `27` identity words in `S_3,L=4`, of
  which `12` are full, and `3936` in `S_4,L=6`, of which `96` are full;
- the coverage union inequality held in every enumerated case;
- the full-walk nontrivial absolute character ratio was exactly `1-N/M` for
  all partitions through `N=12`;
- the deleted-graph constants and
  `((M-1)/M)rho=(N-2)/N` held symbolically through `N=12`.

These finite checks could have falsified a normalization, return-count, or
inequality claim in the displayed cases.  They do not prove the quantified
theorem; the proof above supplies that step.

## 5. Consequence for the dense-support approximation

If `A=Full_N`, then for any probability law `mu`,

```text
d_TV(mu,mu(.|A))=mu(A^c).
```

Therefore replacing `U_N` by its complete-support conditional law costs at
most `exp(-2N)` in total variation.  R0 supplies no reason to put an edge-mask
in the rank-recursive state.

## 6. Dependency and claim ledger for this role

| Claim | Status | Dependency | Evidence |
|---|---|---|---|
| Endpoint feasibility (1.1) | proved | none | cycle-count argument and explicit factorization |
| Exact missing-edge bridge ratio (2.2) | proved | none | direct normalized word counts; exact DP |
| Deleted-walk absolute radius (2.5) | proved | CLR Theorem 1.1 | explicit `K_N-a` Laplacian and sign twist |
| General coverage bound (2.1) | proved | preceding rows | trace bounds and union bound |
| Dense R0 with `c=2` | proved | (2.1) | explicit inequalities (2.9)--(2.10) |
| Finite exact cases | empirical only as evidence for universal theorem; exact as finite facts | script correctness | deterministic exact arithmetic output |

There is no unproved mathematical step remaining in R0.  A fresh-worker audit
is still required by the run protocol before the coordinator accepts the
`promote` verdict.

role: r0-coverage
claim: For every N>=2, the uniform identity bridge at L_N=2N^3 misses some transposition with probability at most exp(-2N); for N>=3 the stronger all-even-L bound (2.1) holds.
status: proved
assumptions: The established Caputo--Liggett--Richthammer Theorem 1.1 on equality of interchange and one-particle spectral gaps; no conjectural project assumption.
evidence: Theorem 2.1 and its convention-complete proof above; exact_coverage_check.py; exact_check_results.json.
independent_checks: A separate P-versus-Q operator perturbation derivation, exact return/coverage DP through N=5, symbolic spectral constants through N=12; fresh-worker audit pending coordinator assignment.
complexity: The theorem is analytic and introduces no sampler state or coverage mask. For one alphabet the checker uses O(L N! binom(N,2)) time and O(N!) memory; checking every deleted edge adds another binom(N,2) time factor, and the support-mask DP is used only in tiny cases. It is validation, not the proposed sampler.
first_unproved_step: None for R0; only the run-mandated independent human/worker audit remains before coordinator acceptance.
verdict: promote
