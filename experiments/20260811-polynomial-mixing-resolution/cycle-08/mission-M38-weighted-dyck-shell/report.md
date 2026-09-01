# M38 final report: exact weighted-Dyck recurrence, quartile shell still open

This mission proves an exact universal coefficient recurrence and a universal
adjacent-layer no-cliff inequality.  It does **not** prove either alternative
requested in M38: the recurrence has not yielded a uniform quartile-shell
lower bound, while the finite coefficients give no superpolynomial thin-shell
family.  Consequently there is no Terminal-B candidate here.

## 1. Exact claim, quantifiers, and convention

Permutations are maps on `[N]`; `pq` means `p` after `q`, so
`(pq)(x)=p(q(x))`.  Put `n=N-1`, `m=2n`, and let

```text
F_N={w=(t_1,...,t_m):t_1...t_m=id and the factor-support graph is connected}.
```

For `x_j=t_1...t_j`, put

```text
h_j=N-cycles(x_j),              Area(w)=sum_(j=1)^m h_j,
H_N(a)=#{w in F_N:Area(w)=a}.
```

The sign path of `w` records `U` when `h_j-h_(j-1)=1` and `D` when it is
`-1`; it is a Dyck path of semilength `n`.  For a fixed Dyck path `P`, write
`W_N(P)` for its exact `F_N`-fiber size.

### Theorem 1 (literal support-Mobius/cut-join coefficient formula)

For every `N>=3`, every Dyck path `P` of length `2N-2`, and every integer
`a`, the following finite recurrence gives `W_N(P)` and `H_N(a)` exactly.

Let `lambda=(lambda_1,...,lambda_k)` run over integer partitions of `N`, and
put

```text
b_N(lambda)=N!/[prod_i lambda_i! prod_d m_d(lambda)!],
mu(lambda)=(-1)^(k-1)(k-1)!.
```

Here `b_N(lambda)` is the number of labeled set partitions with block-size
profile `lambda`.  For a cycle type `alpha |- d`, let `m_j(alpha)` be the
multiplicity of part `j`, and define

```text
c_d(alpha,beta)=#{t in T_d : type(s_alpha t)=beta},                 (1.1)
```

where `s_alpha` is any fixed permutation of type `alpha`.  This number is
independent of the representative.  Its only nonzero values are the following
literal cut/join coefficients:

- joining unequal `i<j` cycles into `i+j`:
  `m_i(alpha)m_j(alpha)ij`;
- joining two `i`-cycles:
  `binom(m_i(alpha),2)i^2`;
- cutting a `k`-cycle into unequal `i<k-i`:
  `m_k(alpha)k`;
- cutting an even `k`-cycle into two `k/2` cycles:
  `m_k(alpha)k/2`.

For a tuple `bold alpha=(alpha_1,...,alpha_k)` with
`alpha_i |- lambda_i`, define

```text
r(bold alpha)=sum_i(lambda_i-ell(alpha_i)).
```

Coordinates refer to the fixed labeled blocks, even when block sizes repeat.
Let `C_lambda(bold alpha,bold beta)` be `c_(lambda_i)(alpha_i,beta_i)` if the
two tuples differ only in coordinate `i`, summed over such coordinates, and
zero otherwise.  Start the exact area transfer at

```text
D_0^lambda(1_lambda,0)=1,
1_lambda=((1^lambda_1),...,(1^lambda_k)),
```

and use

```text
D_(j+1)^lambda(bold beta,a+r(bold beta))
 +=D_j^lambda(bold alpha,a) C_lambda(bold alpha,bold beta).         (1.2)
```

Then, with `A_lambda(a)=D_m^lambda(1_lambda,a)`,

```text
H_N(a)=sum_(lambda |- N) b_N(lambda)mu(lambda)A_lambda(a).          (1.3)
```

For a fixed path `P`, filter each transition in (1.2) to
`r(bold beta)-r(bold alpha)=+1` at a `U` and `-1` at a `D`, omit the area
index, and call the final identity mass `A_lambda(P)`.  Then

```text
W_N(P)=sum_(lambda |- N) b_N(lambda)mu(lambda)A_lambda(P).          (1.4)
```

Equations (1.1)--(1.4) are a proved universal formula, not an inference from
the bounded computation.

### Theorem 2 (universal adjacent-area no-cliff inequality)

For every `N>=3` and every feasible `a<n^2`,

```text
H_N(a+2) >= H_N(a)/n.                                               (1.5)
```

In particular every parity-compatible area from the minimum `n` to the
maximum `n^2` is feasible.  The factor `n` in (1.5) is the exact worst-case
bound supplied by this argument; it cannot simply be iterated over the
`Theta(n^2)` layers without a superpolynomial loss.

### Exact finite result (diagnostic only)

The recurrence was evaluated with exact integers through `N=13`, and all
fixed paths were evaluated through `N=8`.  It reproduces all inherited
`N=3,4,5` tables, Hurwitz's total `(2N-2)!N^(N-3)`, and the exact mountain
coefficient.  For the first area whose conditional CDF is at least `1/4`, the
results are

```text
N   q    CDF          H_N(q)/sum_(a<=q)H_N(a)
3    2   0.250000     1.000000
4    7   0.466667     0.535714
5   12   0.424048     0.485682
6   17   0.259597     0.468939
7   26   0.301992     0.331111
8   35   0.262017     0.278382
9   46   0.254324     0.243256
10  59   0.259755     0.206486
11  74   0.274404     0.177200
12  89   0.250343     0.162941
13 108   0.278470     0.139193
```

Thus the desired threshold exists in these exact cases and its shell ratio is
larger than `1/N`.  This is finite falsification evidence only.

## 2. Full argument

### 2.1 Support-partition Mobius inversion

For a labeled set partition `rho` of `[N]`, let `A_rho(P)` count identity
words of path `P` all of whose transpositions have both endpoints in a block
of `rho`.  Let `E_sigma(P)` count words whose exact support-component
partition, including isolated labels, is `sigma`.  Then

```text
A_rho(P)=sum_(sigma<=rho) E_sigma(P).
```

The connected words are exactly `E_top(P)`.  The partition-lattice Mobius
function to the one-block top is
`mu(rho,top)=(-1)^(|rho|-1)(|rho|-1)!`, hence

```text
E_top(P)=sum_rho (-1)^(|rho|-1)(|rho|-1)! A_rho(P).                 (2.1)
```

The value of `A_rho(P)` depends only on the block-size profile.  Grouping
(2.1) by profiles and using the exact labeled multiplicity `b_N(lambda)`
proves (1.4).  The identical argument coefficientwise in an area marker proves
(1.3).

### 2.2 Exact Young-subgroup transfer

If all factors remain within `rho`, the prefix permutation lies in the Young
subgroup `prod_(B in rho) S_B`.  Conjugacy inside this subgroup reduces a
prefix to the tuple of cycle types in the blocks.  Right multiplication by a
transposition changes the number of cycles by exactly one.  If its endpoints
are in distinct cycles of lengths `i,j`, there are `ij` choices for that pair
of cycles; if the endpoints are in one `k`-cycle, cyclic separation gives
`k` transpositions for unequal resulting sizes and `k/2` for equal halves.
Multiplying by the numbers of available cycles gives exactly the four cases
in (1.1).  Their sum over all targets is `binom(d,2)`.

The rank of a Young-subgroup element is the sum of the coordinate ranks.
After a transition to `bold beta`, the new prefix contributes
`r(bold beta)` to area.  This proves (1.2), and returning to the all-identity
tuple imposes the exact bridge endpoint.  Filtering the rank increment gives
the fixed Dyck-path version.  No ordering information is discarded: the
transfer is applied once for every ordered factor position.

### 2.3 Proof of the no-cliff inequality

Fix `a<n^2`.  Every word in the layer `L_a` has a nonmountain Dyck path and
therefore at least one adjacent `DU` valley.  By the M34 upper-diamond lemma,
at every specified valley the right Hurwitz replacement

```text
(u,v) -> (v,vuv)
```

defines a labeled directed incidence `(w,i)` from `L_a` to `L_(a+2)`, remains
in `F_N`, and raises area by exactly two.  Hence the number of directed valley
incidences is at least `H_N(a)`; no claim that different positions have
different unlabeled targets is needed.

For a target word and a specified position, the inverse is unique:
`(v,z)` can only have come from `(v z v,v)`.  Moreover that position must be
an adjacent `UD` peak of the target path.  A Dyck path of semilength `n` has
at most `n` peaks.  Thus every target has at most `n` incoming directed
valley edges, so

```text
H_N(a) <= #(directed valley incidences) <= n H_N(a+2),
```

which is (1.5).  The bottom coefficient is positive by the direct formula

```text
H_N(n)=(N-1)!N^(N-2):                                               (2.2)
```

an area-minimum word is an ordered list of `n` adjacent doubled edges, and
connectedness says those distinct edges form a labeled spanning tree.  Hence
(1.5) also proves contiguous feasibility.

### 2.4 Why the three analytic upgrades tried here do not close the shell

**Canonical injection.**  Applying a deterministic valley raise until a
chosen shell is reached has at most `n` inverse choices at every step.  The
area range contains

```text
1+(n^2-n)/2
```

layers, so the resulting preimage bound is `n^Theta(n^2)`, not polynomial.
The complete `N=4` auxiliary calculation also refutes the stronger shortcut
“every nonminimum word has an adjacent left or right Hurwitz move lowering
area”: it finds 192 area-5 states with no such descent, including the explicit
witness stored in `reverse-hurwitz-N4.json`.  This refutes that proposed
reverse action, not the full local heat bath.

**Variance/anti-concentration.**  The exact distributions through `N=13`
have a broad, apparently smooth central region and shell ratio of order
`1/N`, but a variance bound alone gives no lower bound on a particular lattice
atom.  The deterministic support bound only gives `Var(Area)<=O(n^4)`, which
is compatible with a missing quartile level or a very thin crossing shell.
No log-concavity shortcut is available: the exact `N=5` coefficients

```text
3000,23400,60600,132840,207600,205560,375000
```

are already nonunimodal and non-log-concave.

**Perron--Frobenius transfer.**  For each fixed profile `lambda`, (1.2) is a
nonnegative finite transfer matrix (and is symmetrizable using conjugacy-class
sizes).  Connectedness, however, is extracted by the alternating Mobius sum
(1.3).  The cancellation is not polynomially stable.  At the bottom path the
unrestricted identity count is `M^n`, whereas (2.2) gives exact connected
fraction

```text
H_N(n)/M^n = 2^n n!/[N n^n]
             =Theta(sqrt(n)/N (2/e)^n).                             (2.3)
```

Thus a pointwise polynomial Radon comparison with the unrestricted positive
transfer is false.  One can instead augment the positive transfer by the
generated support partition, but no uniform spectral or log-Sobolev estimate
for that growing state space was obtained.  The Duchi--Poulalhon--Schaeffer
Hurwitz-tree sampler explains the exact total count, but its stated bijection
does not identify this prefix-rank area statistic or provide its local limit.

These failures leave the quartile coefficient statement below as the precise
frontier rather than silently importing ordinary Dyck-path unimodality.

## 3. Probability, runtime, path length, and congestion accounting

For the original chain

```text
K=(1/2)I+(1/(2|R_m|)) sum_(r in R_m) 1/(m-r+1) sum_i H_(i,r),
R_m={r in {3,4,5}:r<=m},
```

M34 proves for `N>=6`, every lower area threshold
`A_q={w in F_N:Area(w)<=q}` with conditional mass at most `1/2`,

```text
Phi_pm^K(A_q)
 >= [H_N(q)/sum_(a<=q)H_N(a)]/[6(m-2)M^3].                         (3.1)
```

The specified crossing is one padded `H_3` move, with exact probability
`1/[6(m-2)F_3(g)]` and `F_3(g)<=M^3`.  This includes laziness, the `1/3`
block-size choice, the specified one of `m-2` windows, and the exact
conditional-fiber outcome.  All `H_4,H_5` flow remains in `K` and is discarded
only as a nonnegative term in the lower bound.  If the named open proposition
holds with exponent `C`, (3.1) is `Omega(N^(-C-7))` because `m=2N-2` and
`M=binom(N,2)`.

For the exact area recurrence, let

```text
s_lambda=prod_i p(lambda_i),
d_lambda=max_(bold alpha) #{bold beta:C_lambda(bold alpha,bold beta)>0}.
```

There are at most `n^2+1` area indices and `d_lambda<=sum_i
binom(lambda_i,2)<=M`.  The area dynamic program therefore uses, in unit-cost
integer arithmetic,

```text
O(m(n^2+1) sum_(lambda|-N) s_lambda d_lambda) operations,
O((n^2+1) max_(lambda|-N) s_lambda) working memory.                 (3.2)
```

The actual integer bit lengths are polynomial (`O(N log N)` for the relevant
counts up to profile/Mobius factors), so bit complexity adds a polynomial
factor.  Precomputing all cut/join rows by the validator's literal
transposition enumeration costs at most
`O(sum_(d<=N) p(d)d^3)` elementary operations; using the displayed formulas
is faster.  Fixed-path enumeration additionally multiplies by the Catalan
number and is diagnostic only.  The complete `N<=13` area run took 32.57
seconds on the recorded Python 3.12.3 environment; the complete `N<=8`
fixed-path run took 1.21 seconds.

No comparison path or canonical hub is used in Theorems 1--2.  The recurrence
is an exact enumerator, not a polynomial-time sampler in variable `N`.

## 4. Dependencies, each labeled

1. **PROVED HERE:** the support-partition Mobius formula, literal cut/join
   transfer, exact area and fixed-path recurrences, adjacent-layer no-cliff
   inequality, contiguous area support, and the exponentially small bottom
   connected/unrestricted ratio (2.3).
2. **INHERITED PROVED:** M34's join-tree lemma, upper-diamond valley action,
   exact padded-`H_3` probability, full-`K` threshold-flow lower bound, and
   fixed-path cover monotonicity; exact heat-bath reversibility/stationarity.
3. **CITED:** Cayley's labeled-tree count, Hurwitz's identity-factorization
   total `(2N-2)!N^(N-3)`, and the mountain count via minimal cycle
   factorizations.  They are independently checked by every exact run.
4. **CITED RESOURCE, NOT USED AS AN AREA THEOREM:** Duchi, Poulalhon and
   Schaeffer, [*Uniform random sampling of simple branched coverings of the
   sphere by itself*](https://www.irif.fr/~duchi/SODA-2014.pdf), SODA 2014,
   Theorem 3.3, Proposition 4.1, and Corollary 6.1, for the Hurwitz-tree
   bijection, `N`-to-one Cayley-tree/permutation encoding, total count, and
   linear perfect sampler.  The paper supplies no prefix-area
   anti-concentration theorem.
5. **CITED RESOURCE, NOT USED AS A THEOREM:** Ferrari,
   [*Unimodality and Dyck paths*](https://arxiv.org/abs/1207.7295), for the
   fact that ordinary Dyck-rank unimodality is not an available black box.
6. **EXACT FINITE:** all area coefficients through `N=13`, all fixed-path
   coefficients through `N=8`, and complete `F_4` adjacent-Hurwitz descent
   falsification.  These test named claims only and make no finite-to-universal
   inference.

## 5. First unproved standalone proposition

> **WEIGHTED DYCK QUARTILE-SHELL COEFFICIENT BOUND.**  There are universal
> constants `c>0` and `C<infinity` such that for every `N>=6` there is a
> feasible area `q_N` satisfying
>
> ```text
> 1/4 <= sum_(a<=q_N)H_N(a)/[(2N-2)!N^(N-3)] <= 1/2
> ```
>
> and
>
> ```text
> H_N(q_N) >= c N^(-C) sum_(a<=q_N)H_N(a).                          (5.1)
> ```

The natural candidate is the first conditional quartile.  The exact
recurrence defines every coefficient in (5.1), but neither its alternating
transfer form nor (1.5) currently proves (5.1).  By (3.1), this proposition
would rigorously reject the proposed area-median cut by inverse-polynomial
full-`K` conductance.

## 6. Strongest self-attack / failure mode

The principal result is an exact exponential-size recurrence, not an
asymptotic estimate.  Alternating support-Mobius cancellation is severe enough
that Perron--Frobenius smoothing for each unrestricted Young-subgroup bridge
does not survive automatically.  The no-cliff inequality has the wrong loss
for iteration over `Theta(N^2)` layers, and the complete reverse-Hurwitz
falsifier removes the simplest way to reverse it.

Even a future proof that the shell ratio in (5.1) is superpolynomially small
would **not** by itself establish Terminal B.  A conductance upper bound must
also count every crossing from the full width-12 area shell under `H_3,H_4,H_5`
and every exit from `F_N`, then orient by the exact global mass.  This mission
has only the M34 lower bound on one `H_3` flow, not those required upper
bounds.  Conversely, proving (5.1) rejects only this named area-threshold cut;
it is not an arbitrary-cut or full-chain gap theorem.

## 7. Calibration suite

- **Odd `m`:** `Omega(N,m)` is empty by sign; this mission uses even
  `m=2N-2`.
- **`m=0`, `N=2`:** singleton cases, treated separately.  For `N=2`, the
  minimal connected word is itself a singleton and Theorem 2 has no
  nonmaximum layer.
- **`m=2,N>=3`:** excluded disconnected local-chain regime; not used.
- **`S_3,m=4`:** global size 27 and four pure-Hurwitz components.  The minimal
  connected macro has 24 words and exact area table `{2:6,4:18}`.  Here
  `R_m={3,4}`, so `H_4` is a whole-word heat bath and the `1/3` block-size
  normalization in (3.1) is not asserted.
- **`S_4,m=4`:** global size 120 and 13 pure-Hurwitz components; this is below
  the minimal connected full-support length and is not conflated with `F_4`.
- **`S_4,m=6`:** global size 3936 and 17 pure-Hurwitz components.  The minimal
  connected macro has 2880 words and exact area table
  `{3:96,5:528,7:720,9:1536}`.
- **`N=5,m=8`:** exact connected table is
  `{4:3000,6:23400,8:60600,10:132840,12:207600,14:205560,16:375000}`;
  its dip at 14 explicitly calibrates against assumed unimodality.
- **Doubled-tree minimum:** equation (2.2) treats every ordering of a labeled
  spanning tree, not one exponentially rare canonical hub.
- **Ordering/interleavings:** recurrence (1.2) processes ordered factor
  positions and does not replace the word by its support graph.
- **Parity:** only sign forces even length; edge- or degree-parity is never
  used as an identity criterion.
- **`L=2` failure:** the upper-diamond pair is padded in an actual `H_3`
  window; no general length-two simulation is assumed.

## 8. Artifact paths and exact reproduction commands

Owned artifacts:

- `plan.md`
- `checkpoint.md`
- `weighted_dyck_recurrence.py`
- `results-N13.json` (main exact area run)
- `results-paths-N8.json` (complete fixed-path run through `N=8`)
- `results.json` and `results-paths-N6.json` (earlier exact checkpoints)
- `reverse_hurwitz_action_falsifier.py`
- `reverse-hurwitz-N4.json`
- this `report.md`

From the repository root:

```bash
python3 experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M38-weighted-dyck-shell/weighted_dyck_recurrence.py \
  --max-n 13 --path-validation-max-n 5 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M38-weighted-dyck-shell/results-N13.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M38-weighted-dyck-shell/weighted_dyck_recurrence.py \
  --max-n 8 --path-validation-max-n 8 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M38-weighted-dyck-shell/results-paths-N8.json

python3 experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M38-weighted-dyck-shell/reverse_hurwitz_action_falsifier.py \
  --N 4 \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-08/mission-M38-weighted-dyck-shell/reverse-hurwitz-N4.json
```

All runs are deterministic, dependency-free Python 3.12.3 computations at
repository commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.  The main
script records fixed seed `380811` although it uses no stochastic inference.

## 9. Verdict

**OPEN AT A NAMED STEP: WEIGHTED DYCK QUARTILE-SHELL COEFFICIENT BOUND.**
