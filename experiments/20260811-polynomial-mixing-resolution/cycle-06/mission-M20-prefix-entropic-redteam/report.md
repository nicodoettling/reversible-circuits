# M20 final report: full-support midpoint-prefix renewal red team

Date: 2026-08-11  
Owned directory: `experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M20-prefix-entropic-redteam/`

## 1. Exact claim, quantifiers, and convention

Permutations satisfy `(pq)(x)=p(q(x))`; a displayed word evaluates as
`t_1...t_m`.  Let `M=binom(N,2)`, let `pi_(N,m)` be uniform on

```text
Omega(N,m)={w in T_N^m:t_1...t_m=id},
```

and use the original lazy chain

```text
K=(1/2)I
 +(1/(2|R_m|)) sum_(r in R_m)
      (1/(m-r+1)) sum_i H_(i,r),
R_m={3,4,5} intersect [m].                            (1.1)
```

For each `N>=3`, set

```text
k_N=2N^3,  m_N=2k_N=4N^3.                             (1.2)
```

Define the relaxed midpoint-renewal event and its connected-full-support
restriction by

```text
A_N^0={w in Omega(N,m_N):t_1...t_(k_N)=id},
A_N={w in A_N^0:the factorization graph is connected on all [N]}.  (1.3)
```

The candidate Terminal-B claim was that the factorial mass, prefix locality,
and full-support internal geometry in (1.3) create superpolynomially small
conductance for the original chain.  It is **refuted**.  The exact stationary
mass is oriented, but every state has a one-step length-three exit of
probability at least

```text
q_N=1/[6(m_N-2)M^2].                                  (1.4)
```

Consequently

```text
Phi_pm^K(A_N)>=q_N,                                   (1.5)
```

which is inverse polynomial in `N m_N`.  This is a scoped candidate-cut
rejection, not Terminal B and not a global gap theorem.

## 2. Full argument and construction

### 2.1 Exact return and stationary-mass formulas

Let

```text
C_d(r)=#{(t_1,...,t_r) in T_d^r:t_1...t_r=id},        (2.1)
```

with `C_1(0)=1` and `C_1(r)=0` for `r>0`.  Since a word in `A_N^0` is exactly
an ordered pair of independent length-`k_N` identity words,

```text
|A_N^0|=C_N(k_N)^2,
pi(A_N^0)=C_N(k_N)^2/C_N(2k_N).                       (2.2)
```

There is also an exact connected count.  For a set partition `P` of `[N]`,
let `R_P(k)` count length-`k` return words whose every edge is internal to a
block of `P`.  If the block sizes are `d_1,...,d_s`, then

```text
R_P(k)=sum_(r_1+...+r_s=k)
         [k!/(r_1!...r_s!)] prod_j C_(d_j)(r_j).       (2.3)
```

Indeed the restricted factors on disjoint blocks commute; their positions
are an arbitrary color interleaving, and each block product must be identity.

For an ordered pair of half-words, its union support graph has a unique
component partition `sigma`.  Both half-words use only edges within `P`
exactly when `sigma` refines `P`.  Möbius inversion on the partition lattice,
where

```text
mu(P,top)=(-1)^(|P|-1)(|P|-1)!,                       (2.4)
```

therefore gives

```text
J_N(k):=|A_N|
 =sum_(P partition [N])
    (-1)^(|P|-1)(|P|-1)! R_P(k)^2,                    (2.5)

pi(A_N)=J_N(k_N)/C_N(2k_N).                           (2.6)
```

Equations (2.2)--(2.6) count the ordered interleavings and the connected
full-support restriction exactly; no macro-conditional mass is substituted
for the global stationary law.

### 2.2 Quantitative orientation on the explicit dense sequence

Let `P_N` be the nonlazy uniform-transposition walk and
`p_N(r)=P_N^r(id,id)`.  Then `C_N(r)=M^r p_N(r)`.  For even `r`, Fourier
inversion for the transposition class gives

```text
p_N(r)=(2/N!)(1+epsilon_N(r)),                         (2.7)
0<=epsilon_N(r)
 <=(N!/2)(1-2/(N-1))^r
 <=(N!/2) exp[-2r/(N-1)].                             (2.8)
```

The two leading terms are the trivial and sign representations.  The exact
proper character-ratio bound in (2.8) follows because the largest absolute
proper transposition ratio is that of `(N-1,1)` and its conjugate,
`(N-3)/(N-1)=1-2/(N-1)`.  For `N=3` the sole remaining ratio is zero.

At `r=k_N=2N^3`, use `N!<=N^N`, `log N<=N`, and
`4N^3/(N-1)>=4N^2` to get

```text
epsilon_N(k_N)<=exp(-3N^2)/2<1/16.                    (2.9)
```

Combining (2.2), (2.7), and the lower bound
`p_N(2k_N)>=2/N!` gives

```text
pi(A_N^0)
 <=(2/N!)(17/16)^2
 <=289/768<1/2.                                       (2.10)
```

Thus `A_N^0`, and hence `A_N`, is correctly oriented as the smaller side.

It remains to verify that the literal connected restriction is not empty or
an anomalously tiny subevent inside the renewal event.  Conditional on
`A_N^0`, the two half-words are independent uniform return bridges.  If their
union graph is disconnected, some nontrivial vertex cut has no crossing
factor in either half.  A cut with sides of sizes `s,N-s` leaves

```text
L=binom(s,2)+binom(N-s,2)<=M-(N-1)=M(N-2)/N           (2.11)
```

allowed transpositions.  Dropping the return constraint gives at most `L^k`
half-words, whereas the trivial and sign terms give
`C_N(k_N)>=2M^(k_N)/N!`.  There are fewer than `2^(N-1)` unoriented cuts, so

```text
Pr(A_N^0 minus A_N | A_N^0)
 <=delta_N
 :=2^(N-3)(N!)^2((N-2)/N)^(2k_N)
 <=2^(N-3)(N!)^2 exp(-8N^2).                          (2.12)
```

Since `2^(N-3)(N!)^2<=exp(3N^2)` for `N>=3`, `delta_N<=exp(-5N^2)<1/2`.
Thus `J_N(k_N)>0`; moreover

```text
(1-delta_N)pi(A_N^0)<=pi(A_N)<=pi(A_N^0),             (2.13)
pi(A_N)=(2/N!)(1+O(exp(-3N^2))).                      (2.14)
```

This explicitly handles both stationary mass and its orientation.  The
factorial smallness in (2.14) is not treated as low conductance.

### 2.3 Every cut state has an exact original-K exit

Fix `w in A_N`.  Write

```text
a=t_(k_N), b=t_(k_N+1), c=t_(k_N+2),
P=t_1...t_(k_N-1).
```

The midpoint renewal says `Pa=id`.  Since `a` is an involution,

```text
P=a.                                                   (2.15)
```

Use the legal length-three window starting at original position `k_N`.
There are two exhaustive cases.

1. If `a!=b`, use the right Hurwitz outcome

   ```text
   (a,b,c) -> (b,bab,c).                               (2.16)
   ```

   Its product is `b(bab)c=abc`.  The new midpoint prefix is
   `Pb=ab!=id`.

2. If `a=b`, choose any transposition `d!=a`, possible because `N>=3`, and
   use the square refresh

   ```text
   (a,a,c) -> (d,d,c).                                 (2.17)
   ```

   Both products equal `c`; the new midpoint prefix is `Pd=ad!=id`.

Thus (2.16) or (2.17) is in the exact same-product conditional fiber and
lands outside even the relaxed event `A_N^0`.  It is therefore outside
`A_N`, regardless of whether its support remains connected.

A length-three transposition fiber has at most `M^2` words: choosing its
first two factors determines the third permutation uniquely.  For (1.2),
`R_m={3,4,5}`.  The exact probability of selecting the nontrivial half of
`K`, block size three, the chosen window, and the displayed conditional
outcome is at least

```text
(1/2)(1/3)(1/(m_N-2))(1/M^2)
 =1/[6(m_N-2)M^2]=q_N.                                (2.18)
```

Consequently

```text
Q_K(A_N,A_N^c)
 =sum_(w in A_N)pi(w)K(w,A_N^c)
 >=pi(A_N)q_N.                                         (2.19)
```

By (2.10), the denominator in two-sided conductance is `pi(A_N)`, proving
(1.5).  Since `M<=N^2/2` and `m_N-2<=m_N`,

```text
q_N>=2/(3m_N N^4),                                    (2.20)
```

so this cannot be superpolynomially small in `N m_N`.

### 2.4 Every midpoint-crossing scan normalization

For the relaxed prefix event `A_N^0`, a same-product block lying wholly in
the first half preserves its total prefix product, and a block wholly in the
second half leaves it unchanged.  A length-`r` window can change the prefix
exactly only if it straddles the cut after site `k_N`.  The valid starts are

```text
k_N-r+2,...,k_N,
```

exactly `r-1` windows.  Hence the exact counts are

| block size | crossing windows | all windows |
|---:|---:|---:|
| 3 | 2 | `m_N-2` |
| 4 | 3 | `m_N-3` |
| 5 | 4 | `m_N-4` |

Including laziness and the uniform block-size scan,

```text
K(w,(A_N^0)^c)
 <=beta_m
 :=(1/6)[2/(m_N-2)+3/(m_N-3)+4/(m_N-4)]
 =Theta(1/m_N).                                        (2.21)
```

Together with (2.18), this brackets the relaxed candidate between inverse
polynomials.  For the connected restriction `A_N`, a noncrossing window can
also exit by destroying connected support.  Such windows are all among the
`m-r+1` scans and contribute additional nonnegative boundary flow.  They are
not omitted from an upper bound: no analogue of (2.21) is claimed for
`A_N`.  Their possible contribution only strengthens the rejection (2.19).

## 3. Probability, runtime, path, and congestion accounting

- The chosen exit probability is exactly lower-bounded by (2.18), including
  the outer laziness, `1/3` block-size choice, `1/(m-2)` window scan, and
  `M^-2` fiber outcome.
- The exit is one Markov transition; its comparison path length is one and
  there is no multicommodity congestion claim.
- Enumerating a length-three fiber requires at most `M^2=O(N^4)` candidate
  pairs, so the exact local update has polynomial cost.
- The prefix-only cut has exactly nine potentially active windows across all
  three block sizes, with full coefficients in (2.21).  The connected cut can
  have additional support-loss exits; all have nonnegative flow.
- Formula (2.5) is an exact enumerative identity with Bell-number many
  partition terms.  It is used to state stationary mass exactly, not as a
  polynomial-time sampler.
- The finite harness is deterministic.  Its largest enumeration is
  `6^6=46,656` raw words for `S_4,m=6`; no random seed is applicable.

## 4. Dependencies, labeled by status

1. **PROVED HERE:** exact masses (2.2)--(2.6), dense orientation
   (2.7)--(2.14), the two exhaustive exits (2.16)--(2.17), full original-`K`
   normalization (2.18), flow bound (2.19), and all crossing-window counts.
2. **PROVED/AUDITED PROJECT INPUT:** the transposition-class Fourier formula
   and proper character-ratio maximum `(N-3)/(N-1)`; uniform stationarity and
   reversibility of `K`; exact same-product heat baths.
3. **EXACT FINITE:** `results.json` reproduces the 27/120/3936 calibration
   counts, Möbius counts, exit certificates, and small-case full-K flows.
4. **EMPIRICAL:** none in the theorem.  Recorded runtimes are descriptive.
5. **CONDITIONAL/OPEN:** uniform isoperimetry for arbitrary dense prefix
   subsets, high-representation matrix-coefficient cuts, and every other
   internal full-support cut.

## 5. First unproved standalone proposition

> **DENSE MIDPOINT-PREFIX ISOPERIMETRY.**  There exist universal
> `c>0,C<infinity` such that for every `N>=3`, every even
> `k>=2N^3`, every midpoint-prefix subset `S subset Alt_N` under the
> identity bridge of length `m=2k`, and
> `B_S={w:t_1...t_k in S}` with
> `0<pi(B_S)<=1/2`, the original kernel satisfies
>
> ```text
> Q_K(B_S,B_S^c)/pi(B_S) >= c(Nm)^(-C).                (5.1)
> ```

Here `Alt_N` denotes the alternating group.  Even prefix length forces the
midpoint product to lie there.
Proving (5.1) would rule out every dense prefix cycle/character threshold,
not merely the renewal singleton.  Refuting it with an explicit sequence and
superpolynomial boundary would be a genuine Terminal-B candidate.  Prefix
locality alone supplies only the polynomial `O(1/m)` upper action rate and
does not decide (5.1).

## 6. Strongest self-attack

1. The candidate is a single prefix-product level.  A high-dimensional
   matrix-coefficient or fractal prefix subset might have a much thinner
   boundary under the induced crossing-window kernel; (1.5) says nothing
   about it.
2. Connected full support is overwhelmingly likely **conditional on this
   dense renewal event**, but the event itself has mass about `2/N!`.  The
   proof correctly divides boundary flow by the same factorial mass.
3. Restricting to connected support can only add exits from noncrossing
   windows.  Therefore the prefix-only upper action rate (2.21) must not be
   quoted as an upper bound for the connected cut.
4. The choice `m=4N^3` deliberately enters a pointwise-smoothed dense regime.
   It does not analyze a new sparse near-minimal tree-shape phase.  Previously
   rejected minimal/full-support cuts remain separate inherited results.
5. An inverse-polynomial conductance lower bound for this one set neither
   proves a global spectral gap nor refutes any other Terminal-B family.

## 7. Calibration suite

- Odd `m`: `Omega(N,m)` is empty.  `m=0` and `N=2` even are singleton cases.
  `m=2` is excluded.  The theorem uses even `m>=108`.
- `S_3,m=4`: exactly 27 identity words; `A^0` has nine states and mass `1/3`,
  while the connected cut has six states and mass `2/9`.  The exact original-
  `K` conductances are `1/3` and `7/18`, respectively.  All nine displayed
  length-three certificates pass, including three equal-boundary cases.
- `S_4,m=4`: exactly 120 identity words; `A^0` has 36 states and conductance
  `7/20`.  The connected restriction is empty because two square edges
  cannot form a connected graph on four vertices.  The whole-word `H_4`
  contribution is included in that exact conductance.
- `S_4,m=6`: exactly 3,936 identity words.  The midpoint has odd length three,
  so both renewal cuts are empty; no false mass is assigned.
- The exact Möbius formula agrees with enumeration at `N=3,4,k=2` and gives
  positive connected counts `15,252,840` at `(N,k)=(4,6)` and
  `3,036,897,974,880` at `(5,8)`.
- Near-minimal doubled trees, ordered color interleavings, and the inadequacy
  of degree/multiplicity parity are respected.  The proof uses neither a
  canonical hub nor a graph-only dynamics.
- Pure Hurwitz invariants are not used as global invariants: a Hurwitz outcome
  is used only as one positive-probability result inside an actual `H_3`
  heat bath, and the equal-edge case uses a non-Hurwitz square refresh.

## 8. Artifacts and reproduction

Artifacts in the owned directory:

- `plan.md`
- `checkpoint.md`
- `prefix_renewal_check.py`
- `results.json`
- `report.md`

Reproduce from the repository root:

```bash
python3 -m compileall \
  experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M20-prefix-entropic-redteam/prefix_renewal_check.py

python3 \
  experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M20-prefix-entropic-redteam/prefix_renewal_check.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-06/mission-M20-prefix-entropic-redteam/results.json
```

Environment: Python 3.12.3 with the standard library only.  The computation
is deterministic and uses no seed.  It states the universal count and exit
claims that the finite cases could falsify; the universal proof is Sections
2.1--2.4, not extrapolation from these cases.

## 9. Verdict

**REFUTED.**  The proposed connected-full-support midpoint-prefix renewal
family does not have superpolynomially small conductance for the original
lazy `r={3,4,5}` chain.  Its conductance is at least (1.4), despite factorial
stationary mass and an `O(1/m)` prefix action rate.  This refutes only the
named candidate; Terminal A/B remains unresolved at (5.1) and other internal
full-support statistics.
