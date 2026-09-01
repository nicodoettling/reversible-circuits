# M09 report: linear defect buffers do not remove the base-flow problem

## 1. Exact claims, quantifiers, and convention

Use `(pq)(x)=p(q(x))` and read tuple products from left to right.  Put

```text
T=T_N,  M=binom(N,2),  E=T^2,  q=|E|=M^2,
p(a,b)=ab,  G=A_N,
F_r(g)={B in E^r:p(B_1)...p(B_r)=g}.
```

Let `Q(g)=|F_1(g)|/q=P_T^2(g)`.  For `L>=1` and feasible `h in G`, let
`Omega_L(h)=F_L(h)` have its uniform law `pi_h`.  The adjacent chain `B_L`
chooses one of the `L-1` adjacent coordinate pairs uniformly and replaces it
uniformly at fixed ordered product.  The reference chain is the whole-fiber
heat bath on `Omega_L(h)`.

Three scoped theorems are proved.

### Theorem 1: codebook-cylinder congestion obstruction

Fix a width `r<=L`.  For each `d in G`, let
`C_r(d) subset F_r(d)`, put `C=union_d C_r(d)`, and write `S=|C|`.  Let
`W_1,...,W_J` be `J` specified length-`r` coordinate windows.  Suppose a
possibly randomized comparison route is supplied for every distinct ordered
pair in every feasible `Omega_L(h)^2`, and every such route hits

```text
A={z: z[W_j] in C for at least one j}
```

with probability one.  Then:

1. For at least one feasible endpoint `h`,

   ```text
   pi_h(A)<=J S/q^r.                                    (1.1)
   ```

2. For that endpoint, whenever the right side of (1.1) is at most `1/2`,
   every such routed comparison has directed congestion at least

   ```text
   rho >= q^r/(4 J S).                                  (1.2)
   ```

3. More strongly, suppose `Q^(L-r)` is pointwise `epsilon`-close to uniform:

   ```text
   (1-epsilon)/|G| <= Q^(L-r)(g) <=(1+epsilon)/|G|
   for every g in G.                                    (1.3)
   ```

   Then for every feasible prescribed endpoint, including `h=e`,

   ```text
   pi_h(A)<=kappa J S/q^r,
   rho>=q^r/(4 kappa J S),  kappa=(1+epsilon)/(1-epsilon), (1.4)
   ```

   once the displayed mass upper bound is at most `1/2`.

Any buffer code which represents every defect in `A_N` has

```text
r>=r_N=floor((N-1)/2).                                  (1.5)
```

If there are at most `P(N,L)` codewords per defect, where `P` is any fixed
polynomial, and `J<=L<=C_0N log(N+1)`, then (1.2), and also the prescribed-
endpoint version (1.4), are superpolynomial in `NL`.  Explicitly,

```text
q^r/|A_N| >= 2 N^(N-4)/4^(N-2),                         (1.6)
rho >= N^(N-4)/[2 kappa 4^(N-2) J P(N,L)]               (1.7)
```

in the pointwise-mixed case, up to the harmless subtraction by one before
the mass is below `1/2`.  Thus a canonical buffer, or polynomially many
canonical buffers per defect, cannot give a polynomial-congestion proof.

### Theorem 2: linear-width complementary-recovery obstruction

Fix any constant `C>1/2`.  For every sufficiently large odd `N`, every

```text
r_N=(N-1)/2 <= r <= C N,
```

and every fixed `N`-cycle `c`, define

```text
a_C=exp(-16C)/(2C).
```

Then

```text
|F_r(e)|/|F_r(c)| >= (2/N) exp(a_C N-3C).               (1.8)
```

Consequently consider fixed length-`r` outside words with products

```text
p(A)=p(D)=e,  p(A')=c^(-1),  p(D')=c.
```

For arbitrary overwritten blocks `U,V in F_r(e)`, both

```text
x=A U D,            y=A' V D'
```

belong to the identity fiber `Omega_(3r)(e)`.  At the synchronized zipper
cut, a current cross state and the usual complementary cross state have the
forms

```text
z=A' B D,           z_comp=A B_comp D'.                (1.9)
```

Their identity constraints force

```text
B in F_r(c),        B_comp in F_r(c^(-1)).              (1.10)
```

Any lossless recovery rule which reconstructs every ordered `(U,V)` from
`(B,B_comp)` and one of `R` metadata labels must therefore satisfy

```text
R >= (|F_r(e)|/|F_r(c)|)^2
  >= (4/N^2) exp(2a_C N-6C).                            (1.11)
```

This remains exponential when the two output buffers range over their
*entire* fixed-product fibers.  It rigorously refutes the proposed uniform
injective complementary-bridge accounting with polynomial metadata for every
linear buffer width.  It does not refute a fractional flow which never asks
for such lossless per-context recovery.

### Theorem 3: a fully balanced random shift is the open base comparison

Fix `r` and `s in G`.  Every state of `Omega_(r+1)(s)` has a unique notation
`(B,X)` with `B in E^r,X in E`, and also a unique notation `(Y,B')` with
`Y in E,B' in E^r`.  Therefore ordered legal shifts

```text
(B,X) -> (Y,B'),      p(B)p(X)=p(Y)p(B')=s              (1.12)
```

are exactly all ordered pairs in `Omega_(r+1)(s)^2`.

Suppose a “balanced randomized shift” assigns a probability distribution on
adjacent-chain paths to every pair in (1.12), with demand
`|Omega_(r+1)(s)|^-2`, and has comparison load

```text
max_e [ sum_(u,v) |Omega|^-2
              sum_(gamma contains e) Pr(gamma)|gamma| ] / Q_B(e) <=P. (1.13)
```

Then it is, literally, a multicommodity comparison of the whole-fiber heat
bath to `B_(r+1)`, and

```text
gap(B_(r+1);s)>=1/P.                                   (1.14)
```

Conversely every all-pairs path-flow comparison on that fiber is a balanced
shift family after applying the two notations above.  Thus replacing the
small codebook by a fully randomized all-pairs buffer does not by itself
reduce the problem: at `L=r+1` it is exactly the missing base-scale flow.

These theorems refute two proposed buffer architectures, not the existence of
some polynomial comparison and not Terminal A or Terminal B.

## 2. Full argument

### 2.1 Minimum universal buffer width

A word in `E^r` is a word of `2r` transpositions after exposing its ordered
microfactors.  The transposition length of `g in S_N` is

```text
ell_T(g)=N-number_of_cycles(g),
```

with fixed points counted as cycles.  Among even permutations its maximum is
`N-1` for odd `N`, attained by an `N`-cycle, and `N-2` for even `N`, attained
by an `(N-1)`-cycle with one fixed point.  Hence a buffer that can represent
every `d in A_N` must have

```text
2r>=N-1  (N odd),       2r>=N-2  (N even),
```

which is exactly (1.5).  Conversely those worst endpoints have even minimal
length and can be padded by adjacent transposition squares, so this is the
correct feasibility threshold rather than only a lower bound artifact.

### 2.2 Cylinder mass: endpoint-free argument

First sample `Z=(Z_1,...,Z_L)` uniformly from the unconstrained product
space `E^L`, and let `H=p(Z_1)...p(Z_L)`.  Every fixed length-`r` window is
uniform on `E^r`.  The union bound gives

```text
Pr(Z in A)<=J S/q^r.                                   (2.1)
```

Conditioning on `H` decomposes this probability exactly as

```text
Pr(Z in A)=sum_(h:Omega_L(h) nonempty) Pr(H=h) pi_h(A). (2.2)
```

At least one feasible `h` therefore satisfies (1.1).  This argument needs no
mixing estimate and allows overlapping candidate windows.

### 2.3 Cylinder mass at a prescribed endpoint

Consider a window with `a` coordinates before it and `b` after it, where
`a+b=L-r`.  Fix a buffer word `B` of product `d`.  The number of outside
completions to endpoint `h` is

```text
q^(a+b) sum_u Q^a(u) Q^b(d^(-1)u^(-1)h)
 =q^(L-r) Q^(L-r)(h d^(-1)).                            (2.3)
```

The equality uses that `Q`, and hence every convolution power of `Q`, is a
class function: `d^(-1)u^(-1)h` and `u^(-1)h d^(-1)` are conjugate.  The
total fiber size is

```text
|Omega_L(h)|=q^L Q^L(h).                               (2.4)
```

If (1.3) holds, convolution by the probability `Q^r` shows that the same
pointwise bounds hold for `Q^L`.  Dividing (2.3) by (2.4) yields

```text
pi_h(Z[W]=B)<=kappa q^(-r).                             (2.5)
```

Sum over `C` and the `J` windows to obtain (1.4)'s mass bound.  The accepted
pointwise smoothing theorem supplies `epsilon=1/16`, hence `kappa=17/15`,
after `L-r=s_*(N)=O(N log(N+1))`.  Taking `L=r+s_*(N)` therefore places the
identity-endpoint obstruction inside the current `O(N log N)` base window.

### 2.4 A forced small cylinder gives large comparison congestion

Let `A` have stationary mass `alpha`, and write
`V=|Omega_L(h)|>=2`.  The whole-fiber heat bath sends total nontrivial demand

```text
(1-alpha)(1-1/V)
```

from sources outside `A` to distinct targets.  Every routed realization of
that demand must make a first entrance into `A`.  Therefore the total raw
routed flow through directed edges from `A^c` to `A` is at least this amount.

The total adjacent-chain capacity of those edges is

```text
Q_B(A^c,A)<=sum_(z in A)pi_h(z)=alpha.                  (2.6)
```

Thus some directed edge has raw load/capacity at least
`(1-alpha)(1-1/V)/alpha`.  Standard comparison load has the additional nonnegative
path-length factor, so the same lower bound applies to comparison congestion.
If `alpha<=1/2`, this is at least `1/(4alpha)`.  Substitution of (1.1) or
(1.4) proves (1.2) and (1.4).  The proof applies unchanged to randomized
paths.  More generally, if routes hit `A` only with aggregate probability
`eta` over the nontrivial reference demand, the same first-entrance argument
applies to the portion originating outside `A`; no stronger formula is used
here.

### 2.5 Exact superpolynomial specialization

For `N>=3`,

```text
M=N(N-1)/2>=N^2/4,       q=M^2>=N^4/16,
|A_N|=N!/2<=N^N/2.                                      (2.7)
```

Together with `r>=r_N>=(N-2)/2`, this gives

```text
q^r/|A_N|
 >=2 (N^4/16)^((N-2)/2)/N^N
 =2 N^(N-4)/4^(N-2),                                  (2.8)
```

which is (1.6).  If `S<=|A_N|P(N,L)`, substitute (2.8) in
`q^r/(4kappa J S)` to get (1.7).  For every fixed `D`,

```text
[N^(N-4)/(4^(N-2)J P(N,L))]/(NL)^D -> infinity         (2.9)
```

whenever `J<=L<=C_0N log(N+1)` and `P` is a fixed polynomial: the logarithm
of the numerator is `N log N-O(N)`, whereas all displayed denominator factors
outside `4^N` have logarithm `O(log N)`.  This is the requested literal
superpolynomial quantification for the route congestion.  It is a route
obstruction, not a spectral-gap upper bound.

### 2.6 Exponential fixed-product fiber imbalance at every linear width

Now take odd `N`, `r_N<=r<=CN`, and set `k=2r`.  Since one increment exposes
two independent uniform transpositions,

```text
|F_r(g)|=M^k P_T^k(e,g).                               (2.10)
```

At the identity, Fourier inversion for the uniform-transposition walk gives

```text
P_T^k(e,e)=1/N! sum_(lambda partition N)
                 d_lambda^2 theta_lambda^k.            (2.11)
```

Every `theta_lambda` is real and `k` is even.  All summands are therefore
nonnegative, and the trivial and sign representations contribute one each:

```text
P_T^k(e,e)>=2/N!.                                      (2.12)
```

For a fixed `N`-cycle `c`, every vertex must occur in at least one of the `k`
transpositions: an untouched vertex would be fixed by their product.  Randomly
orient each transposition.  The resulting `2k` endpoint symbols are uniform
subject only to the two symbols in each pair being distinct.  If `Cover`
denotes the event that all labels occur, comparison with `2k` fully
independent uniform symbols gives

```text
Pr_distinct(Cover)
 <=(N/(N-1))^k Pr_iid(Cover)
 <=exp(3C) Pr_iid(Cover).                              (2.13)
```

For the iid experiment let `Z` be the number of unobserved labels.  Since
`2k<=4CN`,

```text
E Z=N(1-1/N)^(2k)>=N exp(-8C).                         (2.14)
```

Changing one sample changes `Z` by at most one.  McDiarmid's bounded-
difference inequality therefore gives

```text
Pr_iid(Z=0)
 <=exp[-2(E Z)^2/(2k)]
 <=exp[-N exp(-16C)/(2C)]
 =exp(-a_C N).                                         (2.15)
```

The transposition law is conjugation invariant, and there are `(N-1)!`
`N`-cycles.  Equations (2.13)--(2.15) imply

```text
P_T^k(e,c)<=exp(3C-a_C N)/(N-1)!.                      (2.16)
```

Divide (2.12) by (2.16); the common factor `M^k` in (2.10) cancels.  This
proves (1.8).  Both fibers are nonempty: `k>=N-1` has the parity of the
minimal `N`-cycle factorization length and any surplus is padded by squares.

### 2.7 Why the natural complementary record needs exponential metadata

Choose once and for all feasible outside words `A,A',D,D'` with the products
in Theorem 2.  The products in (1.9) are

```text
p(A' B D)=c^(-1)p(B),
p(A B_comp D')=p(B_comp)c.                             (2.17)
```

Thus (1.10) is forced; it is not a choice of canonical representatives.
There are `|F_r(e)|^2` possible ordered overwritten pairs `(U,V)` but only
`|F_r(c)| |F_r(c^(-1))|=|F_r(c)|^2` possible buffer records.  If a decoder
also receives one of `R` labels, injectivity gives the first inequality in
(1.11), and (1.8) gives the second.

Stage indices, a constant number of exposed payload letters, and any fixed
polynomial number of local choices can be absorbed into `R` and do not change
the exponential conclusion.  The total identity word length here is `3r`,
which is `O(N)` and hence lies below `C_0N log(N+1)` for all sufficiently
large `N` for any fixed positive `C_0`.

The counting theorem deliberately does not say that a fractional comparison
must possess an injective decoder.  A weighted many-to-many flow may give
rare outside contexts proportionally small demand and obtain cancellation
which a uniform recovery map cannot see.  Such a construction would be a
genuinely different argument.

### 2.8 Exact all-pairs-shift equivalence

Let `V=|Omega_(r+1)(s)|`.  The reference whole heat bath has stationary
directed demand `V^-2` on every ordered state pair and Dirichlet form exactly
`Var_pi`.  Equation (1.12) neither omits nor duplicates any pair: splitting
before the last coordinate gives `(B,X)`, while splitting after the first
gives `(Y,B')`.

For any path-flow family, Cauchy--Schwarz along paths gives

```text
Var_pi(f)=E_whole(f,f)
 <=rho E_B(f,f),                                       (2.18)
```

where `rho` is exactly (1.13).  This proves (1.14).  Conversely, an all-pairs
comparison flow is relabeled by the two unique splittings to produce precisely
the proposed balanced shifts.  This proves the claimed equivalence of flow
objects and makes the circularity exact rather than heuristic.

## 3. Probability, runtime, path length, and congestion accounting

- The cylinder obstruction uses exact unit whole-heat-bath demand and total
  incoming stationary capacity at most `pi_h(A)`.  It loses no scan factor;
  the lower bound applies a fortiori when the path-length multiplier used by
  comparison is included.
- With accepted `epsilon=1/16`, the only endpoint-conditioning factor is
  `kappa=17/15`.
- For codebooks of at most `P(N,L)` words per defect, the route congestion is
  at least (1.7), superpolynomial by (2.9).
- For every fixed linear-width constant `C`, the lossless cross-complement
  metadata is at least `(4/N^2)exp(2a_CN-6C)` with
  `a_C=exp(-16C)/(2C)`.
- No polynomial local path for a fully randomized buffer was constructed.
  The exact load it would have to control is (1.13); claiming that load bound
  would prove the missing length-`r+1` bridge gap by (1.14).
- `bridge_count_ratio.py` is deterministic, uses arbitrary-precision integer
  class recurrences, and took about 7 seconds through `N=24` under Python
  `3.12.3`.  There is no random seed.  Its complexity is polynomial in the
  partition count `p(N)` and `N` for each tested `N`; it is a finite
  falsification tool, not a scalable sampler or a proof of asymptotics.

## 4. Dependencies

- **Proved here:** minimum universal buffer width; endpoint-free and
  pointwise-mixed cylinder mass bounds; forced-cylinder congestion; explicit
  superpolynomial specialization; coupon-collector endpoint imbalance;
  complementary-record counting; exact all-pairs-shift flow equivalence.
- **Proved project input:** parity-aware pointwise smoothing for
  `Q=P_T^2` after `s_*(N)=O(N log(N+1))`, including the value
  `epsilon=1/16`; exact heat-bath reversibility and directed capacities.
- **Cited/standard and displayed:** Fourier inversion for the central random
  transposition walk; only positivity at even time and the trivial/sign terms
  are used.  This is the same convention-audited Fourier formula used in the
  accepted M10 recursion.
- **Cited/standard and applied with constants:** McDiarmid's bounded-
  difference inequality.  Equations (2.14)--(2.15) show every parameter used.
- **Empirical finite check:** exact class recurrence through `N=24`.  It is
  not used in either asymptotic proof.
- **Not used:** irreducibility, Douvropoulos--Lewis, Hurwitz diameter, a
  canonical normal form, or any unproved bridge-count asymptotic.

## 5. First unproved standalone proposition

**Balanced all-pairs shift flow (BASF).**  There exist universal constants
`c>0`, `C_0,C_1<infinity` such that for every `N>=3`, every

```text
r_N<=r<=C_0N,
```

and every feasible `s in A_N`, the exact demands `|Omega_(r+1)(s)|^-2` for
all shifts (1.12) admit fractional flows through adjacent two-increment
heat-bath edges satisfying

```text
rho<=c^(-1)(Nr)^C_1.                                   (5.1)
```

The flow must be analyzed directly; it may not use a polynomial-size defect
code cylinder or a uniform lossless cross-complement decoder.  By Theorem 3,
BASF is exactly the missing whole-heat-bath comparison at these base lengths,
not a consequence of defect representability.  A larger sliding zipper would
also need aggregate, rather than worst-context, concatenation of these flows.

## 6. Strongest self-attack

The two obstructions are architecture-specific.

1. A payload-dependent randomized buffer whose union covers a macroscopic
   fraction of `E^r` does not enter the small codebook cylinder in Theorem 1.
2. A fractional flow need not decode `(U,V)` from `(B,B_comp)` for every fixed
   outside context.  The exponentially imbalanced contexts in Theorem 2 may
   have correspondingly small stationary demand, and an aggregate weighted
   calculation could cancel the imbalance.
3. Theorem 3 says that a completely balanced replacement is the base problem;
   it does not say that BASF is false.
4. No conductance upper bound, slow eigenfunction, or gap upper bound for the
   actual aligned chain or `K` is obtained.  In particular (1.8) is an
   endpoint heat-kernel ratio, not a bottleneck.

Accordingly none of these results supports Terminal B.  The strongest escape
route is a many-to-many weighted flow with no synchronized low-entropy record,
possibly exploiting exact random-transposition character structure.

## 7. Calibration suite

- **Odd original `m`:** the transposition identity fiber is empty.  This
  report works with paired even lengths only.
- **`m=0`, `N=2`:** singleton cases are untouched and trivially mixed.
- **Original `m=2`:** pair length one has no adjacent update and is excluded
  from the target theorem.  A universal buffer cannot fit there.
- **Original `m=4`:** pair length two is the whole-word aligned update.  The
  obstruction is not applied; its exact gap is already closed.
- **`N=3,4`:** `p:E->A_N` is surjective with width one.  Exact fiber counts
  are `3,3` at `N=3` and `6,3,2` by product type at `N=4`; the ratio
  `q/|A_N|=3` is not asymptotically small.  This agrees with the independently
  accepted one-letter zipper.
- **27/120/3936 cases:** they lie in the preceding whole-word/surjective
  calibrations; no contradiction is predicted.
- **Minimum/full-cycle endpoint:** for odd `N`, the `N`-cycle is precisely the
  endpoint forcing `r_N=(N-1)/2` and used in Theorem 2.
- **Sparse lengths and `L=2` failure:** widths below `r_N` cannot represent all
  defects.  The report does not infer local simulation at length two.
- **Ordered microfactors:** the entropy is `q^r=M^(2r)`, not merely the number
  of product values.  Collapsing ordered transposition-pair labels would erase
  the obstruction incorrectly.
- **Ordered interleavings/noncommutativity:** (2.3), (2.17), and all buffer
  product equations retain their exact order; no commuting of disjoint macro
  components is assumed.
- **Fixed hub:** Theorem 1 quantitatively recovers the known tiny-mass hub
  problem and extends it to polynomial-size code families.

## 8. Artifacts and reproduction

Owned artifacts:

```text
experiments/20260811-polynomial-mixing-resolution/cycle-05/
  mission-M09-buffer-zipper/
    plan.md
    checkpoint.md
    bridge_count_ratio.py
    bridge_count_ratios_N3_N20.json
    bridge_count_ratios_N3_N24.json
    report.md
```

Starting repository commit:

```text
502a6f031c6d5a4bc0064ee5b370a4fa3914f993
```

Reproduction command:

```text
cd experiments/20260811-polynomial-mixing-resolution/cycle-05/mission-M09-buffer-zipper
python3 bridge_count_ratio.py --n-min 3 --n-max 24 \
  --output bridge_count_ratios_N3_N24.json
```

The exact run found no finite counterexample to a polynomial *neighboring*
fiber-count ratio: its largest effective exponent through `N=24` was about
`2.99`.  It did expose the growing arbitrary-endpoint imbalance predicted by
Theorem 2: the effective `N`-exponent of the global max/min ratio reached
about `7.91` at `N=24`.  These are exact finite counts but only calibration;
the asymptotic result is the independent proof in Section 2.6.

## 9. Verdict

**OPEN AT A NAMED STEP: BALANCED ALL-PAIRS SHIFT FLOW (BASF).**
