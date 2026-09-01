# M54 final report: root quotient accepted; spine-bias mean lift isolated

Date: 2026-08-11. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Exact quantified claim and conventions

Permutations compose as `(pq)(x)=p(q(x))`; factor tuples multiply
left-to-right. This report concerns the full **nonlazy** uniform scan of
the `r-1` adjacent rank-two same-product heat baths on minimal
transposition factorizations of `(0 1 ... r)`, and its stationary-flow
parking-degree projection `Pbar_r`. It is not a theorem for the original
identity bridge chain `K`.

For every `r>=2`, write

```text
J_r={d in N^r: sum_i d_i=r and sum_(i=0)^q d_i>=q+1},
pi_r(d)=r!/[(r+1)^(r-1) product_i d_i!],
alpha_r=2/[3r(r-1)].
```

The following scoped claims survive this referee audit.

1. **ACCEPT, no numbered objections:** M50's root-composition stationary
   law and exact rates, M41 Section 11's sharpened root-quotient gap, and
   M50's exact fixed-composition product restriction. In particular,

   ```text
   gap(Rroot_r)>=alpha_r/(3e)=2/[9e r(r-1)].
   ```

2. **PROVED:** a root split into ordered sizes `(A,B)` is supported exactly
   when `B` is a proper suffix subtree along the merged branch's rightmost
   spine. The cut and degree-macro target are unique.

3. **PROVED:** if `b=(c_1,...,c_k)` is a coarse root composition,
   `p_b(d)` is the aggregate rate from `d` to all one-root-split
   refinements, and `q_b=E_[pi(.|b)]p_b`, then

   ```text
   q_b=2 alpha_r sum_i (c_i-1)/c_i,
   p_b(d)<=alpha_r(r-k),
   p_b(d)/q_b<=(r-k+1)/2<=r/2.
   ```

4. **REFUTED:** an individual right-spine split rate is determined by
   `(A,B)` and the cut parent's local degree/child count. It already fails
   at `r=4`. The stronger unary branch-additive formula for aggregate
   split propensity also fails at `r=4`.

5. **CONDITIONAL:** the accepted root quotient and product restriction
   imply an inverse-polynomial gap for `Pbar_r` once the standalone
   SPINE-BIAS H-minus-one BOUND in Field 5 is proved. No such bound is
   proved here.

Thus this mission proves useful scoped statements but neither Terminal A
nor Terminal B for `K`.

## 2. Full argument and constructions

### 2.1 Stationary root law and exact transition rates

For a root composition `a=(a_1,...,a_k)`, put

```text
Z_s=(s+1)^(s-1)/s!,  w_a=Z_(a-1)=a^(a-1)/a!.
```

Deleting the root edges leaves independent weighted branches, while the
root contributes `1/k!`; hence

```text
rho_r(a)=Z_r^(-1)(k!)^(-1) product_i w_(a_i).
```

At a fixed boundary between two children of a vertex of degree `d_h`, the
two corresponding lower-`h` factors are adjacent in a uniformly random
parking-multiset word with probability

```text
binom(r-1,d_h-1)/binom(r,d_h)=d_h/r.
```

The scan contributes `1/(r-1)` and the three-element pair fibre has two
upward outcomes. The exact boundary rate is therefore

```text
(d_h/r)(1/(r-1))(2/3)=alpha_r d_h.
```

At the root, merging a fixed adjacent pair has rate `alpha_r k`.
Detailed balance and

```text
rho(a)/rho(a^merge)=w_Aw_B/[k w_(A+B)]
```

give reverse split rate
`alpha_r w_Aw_B/w_(A+B)`. These are stationary-flow rates; reverse
splits are not strongly lumpable inside a coarse fibre.

### 2.2 Root-quotient Poincare bound

The accepted canonical path repeatedly merges the first two parts to the
one-part composition. Its length is at most `2(r-1)`, but the proof uses
stationary path length rather than this worst case. Lagrange inversion for
`T(z)=z exp(T(z))` gives

```text
[z^A]T(z)^p=p A^(A-p-1)/(A-p)!.
```

For a merge edge whose refined state begins `(A,c_2,...,c_k)`, the source
basin mass is at most `e rho(s)`, and its height first moment is at most
`e k rho(s)`. Root degree minus one is exactly
`Bin(r-1,1/(r+1))`, so its mean is below one. Counting both path halves,
including the case in which both traverse the same edge, gives load at
most `3e k rho(s)`. The exact capacity is
`rho(s)alpha_r k`, hence congestion at most `3e/alpha_r` and

```text
gap(Rroot_r)>=alpha_r/(3e).
```

The undirected-capacity convention makes this estimate conservative by a
factor two rather than missing a factor. At `r=2` the two quotient rates
are `2/3` and `1/3`, and the exact gap is one.

### 2.3 Exact product restriction

Conditioned on root branch sizes, the stationary law is the product of
the smaller branch laws. For a branch with `s` internal edges, a specified
local gap is empty in the global interleaving with probability `s/r`; the
resulting global site is selected with probability `1/(r-1)`. Summing the
`s-1` local gaps gives exact action fraction

```text
s(s-1)/[r(r-1)].
```

Therefore the rejected-exit restricted Dirichlet form is exactly the sum
of the smaller `Pbar_s` forms with those coefficients. With a
ROOT-MEAN-LIFT cost `A r^C`, M50's balanced induction closes with exponent
`D=max{4,C+3}`; the sharpened quotient gap saves one power of `r` from the
older calculation.

### 2.4 Universal right-spine support and numerical-rate obstruction

Reverse a proposed split. In the refined tree its parts `A,B` are
adjacent root children. The accepted child-boundary lemma says that every
supported merge attaches `B` at a vertex on the rightmost spine of `A`,
as its last child, and that every such attachment is supported. In the
merged branch, the rightmost spine therefore enters `B`, so `B` is a
suffix subtree. Conversely, detaching any proper suffix subtree on that
spine reverses such a merge. Subtree sizes strictly decrease down a path,
so a prescribed `B` selects a unique edge. If its parent is `j`, the
unique target is `d+e_0-e_j`.

Rates require more than these local data. With `alpha_4=1/18`, exact
enumeration gives

```text
(0,0,1,1)->(0,0,0,1)  at (2/3)alpha_4,
(0,0,2,2)->(0,0,0,2)  at (4/3)alpha_4.
```

Both have branch size `3`, split `(2,1)`, cut-parent degree `2`, and two
children. This rigorously refutes the local numerical formula.

The exact bounded audit also finds, for all `2<=r<=7`, the pattern

```text
d=(0^z,z,z+1,...,r-1),
Pbar_r(d,d+e_0-e_(r-1))=alpha_r/binom(r-1,z).
```

Central individual rates are exponentially small. This pattern remains
finite evidence because a universal marked-word bijection has not been
proved; it is not used as an asymptotic obstruction.

### 2.5 Aggregate reverse-split density

For `b=(c_1,...,c_k)`, Lagrange inversion gives

```text
sum_(A=1)^(c-1) w_Aw_(c-A)/w_c=2(c-1)/c,
```

which proves the exact mean `q_b` in Field 1. A split neighbour has
`d'=d+e_0-e_j`. Its reverse merge uses one fixed boundary and has rate at
most `alpha_r(k+1)`, while

```text
pi(d')/pi(d)=d_j/(k+1).
```

Detailed balance bounds that split contribution by `alpha_r d_j`.
There is at most one target macro for each `j`; summing gives
`p_b(d)<=alpha_r sum_(j>=1)d_j=alpha_r(r-k)`.
Writing `x_i=c_i-1`, concentration of the fixed surplus minimizes
`sum_i x_i/(x_i+1)`, so

```text
sum_i(c_i-1)/c_i >=(r-k)/(r-k+1).
```

The displayed linear density bound follows.

This does not itself give additive induction. The separate three-state
construction in `three_state_mean_lift_obstruction.md` has constant target
density and one-sided exact lumping, yet quotient/full energy ratio
`q/(4 epsilon)`. Thus internal geometry is essential.

### 2.6 Exact H-minus-one reduction

Fix a coarse composition `b` and a one-split refinement `a`. Let

```text
p_(b,a)(d)=Pbar_r(d,F_a),
q_(b,a)=E_[pi(.|b)] p_(b,a)=Rroot_r(b,a),
ell_(b,a)(g)=E_[pi(.|b)][(p_(b,a)-q_(b,a))g].
```

Let `E_b` be the exact rejected-exit internal Dirichlet form in fibre
`F_b`, and let `||ell||_(-1,b)^2` be the dual quadratic norm against
`E_b`. For a crossing edge, the refined source marginal is exactly
`pi(.|a)` and the coarse target marginal has density `p_(b,a)/q_(b,a)`.
Writing the fibre-mean difference as crossing increment plus target bias,
then applying Jensen and dual Cauchy, gives

```text
E_Rroot(E[f|root])
 <=2 E_cross(f)
   +2 sum_b rho(b) E_b(f)
      sum_(a refining b) ||ell_(b,a)||_(-1,b)^2/q_(b,a).
```

Consequently the proposition in Field 5 implies ROOT-MEAN LIFT with
constant `2 max(1,A r^C)`. Each `ell_(b,a)` is supported on the proved
right-spine suffix-cut event. This is the smallest exact open implication.

The tempting branch formula
`p_b/alpha_r=sum_i phi_(c_i)(branch_i)` is false already at `r=4`:
macro `(0,0,1,1)`, composition `(3,1)`, has observed `2/3` versus unary
prediction `1`. Even the literal unary harmonic bound fails at `r=7`:
macro `(0,1,1,3,4,5,6)` has `p/alpha_r=157/60=H_7+1/42`.
Thus a proof must retain contextual interleaving weights or use a robust
Hardy/coboundary argument.

## 3. Worst-case probability, runtime, path, and congestion accounting

- Exact per-boundary action rate: `alpha_r d_h=2d_h/[3r(r-1)]`.
- Exact root quotient merge/split rates are in Field 2.1.
- Quotient canonical-path length: at most `2(r-1)`; stationary-flow
  congestion: at most `3e/alpha_r=9e r(r-1)/2`.
- Quotient gap: at least `2/[9e r(r-1)]`.
- Branch restriction coefficient: exactly `s(s-1)/[r(r-1)]`.
- Aggregate reverse-split density: at most `r/2`; this is an upper bound,
  not a lower bound on individual transitions.
- The path-family diagnostic exhibits finite central rates as small as
  `alpha_r/binom(r-1,floor((r-1)/2))`; it is not promoted universally.
- Exact enumerations use all parking macros, all minimal factorizations,
  and all rank-two fibres. Their time and memory are exponential in `r`
  and are falsification tools only. Quotient-only enumeration has
  `2^(r-1)` states. No polynomial sampler runtime or global comparison
  congestion is claimed by this mission.

## 4. Dependencies

- **Proved/accepted:** M50 child-boundary theorem, root stationary law and
  quotient rates; M41 Section 11 stationary-length congestion; exact M50
  product restriction and balanced conditional induction.
- **Cited, convention checked in the frozen inputs:** Stanley--Biane
  parking-multiset enumeration and Goulden--Yong noncrossing factor-tree
  order. This report does not reopen their already audited translation.
- **Proved here:** aggregate split mean/density bound; universal
  right-spine support/uniqueness; the `r=4` local-rate counterexample; the
  H-minus-one reduction; the abstract three-state obstruction.
- **Empirical exact finite:** spectra, sharp mean-lift constants, contextual
  branch locality through `r=7`, the binomial path-family rates, and the
  numerical H-minus-one coefficients.
- **Conditional:** polynomial full-`Pbar_r` gap from SPINE-BIAS
  H-minus-one BOUND and balanced induction.
- **Resource mismatch:** Caraceni--Stauffer treats uniform coloured plane
  trees; Fleurat gives a size-growth coupling for conditioned Poisson
  trees; Evans--Winter is continuum CRT prune-regraft; Abraham--Delmas--He
  is size-changing Galton--Watson pruning. None supplies the required
  fixed-size conditioned-Poisson right-spine Poincare inequality.

## 5. First unproved standalone step

> **SPINE-BIAS H-minus-one BOUND.** There are universal constants
> `A,C<infinity` such that, for every `r>=2` and every root composition
> `b` of `r`,
> ```text
> sum_(a: one-split refinement of b)
>   ||ell_(b,a)||_(-1,b)^2/q_(b,a) <= A r^C.
> ```
> Here `ell_(b,a)(g)=E_[pi(.|b)][(p_(b,a)-q_(b,a))g]`, and the dual norm
> is taken against the exact rejected-exit product restriction `E_b`.

The support of every summand is an explicitly characterized right-spine
suffix-cut event. A proof by local coboundaries/effective resistance, or a
counterexample family with superpolynomial dual norm, would decide this
named step.

## 6. Strongest self-attack

The universal support proof inherits M50's accepted child-boundary theorem
and therefore its Stanley--Biane/Goulden--Yong convention translation.
The proof controls support but not individual marked-word multiplicity;
the latter demonstrably depends on global interleaving. The striking
binomial-small family has not been proved for unbounded `r` and must not
be used as an asymptotic theorem.

All H-minus-one values are floating generalized-eigenvalue diagnostics on
`r<=7`; they could begin growing rapidly later. The maximum summed
coefficient rises from `0` at `r=2` to about `1.221424` at `r=7`, so the
data do not justify a constant bound. Contextual branch locality also has
only bounded verification. Finally, even a proof for this minimal
long-cycle parking projection would still need a separately checked lift
to all relevant sectors of the original identity chain `K`; none is
claimed here.

## 7. Calibration

- `r=1`: singleton minimal-factorization sector; quotient and internal
  variance are zero by convention.
- `r=2`: exact quotient rates `2/3,1/3`, gap one; all formulas retain the
  three-state fibre and one scan site.
- Star/path stationary weight ratio is `r!`, so no uniform-plane-tree
  theorem is substituted. Repeated zeros and rare nonzero labels are
  retained in the exact orbit weight `r!/product d_i!`.
- Root-unary, many-singleton, balanced, and highly unbalanced compositions
  are all included through `r=7`; the quotient spectrum includes every
  composition through `r=14`.
- The exact constructor was previously audited through `n=r+1<=8` and
  reconstructs every parking word, factorization, pair fibre, and projected
  capacity. These passes can falsify but not prove universal claims.
- Odd `m`, `m=0`, `N=2`, `m=2`, and the identity-word calibrations
  `S_3,m=4`, `S_4,m=4`, `S_4,m=6` are outside this minimal long-cycle
  auxiliary sector. No statement about those cases or about `K` is inferred.

## 8. Artifacts and reproduction commands

All artifacts are in this mission directory. Python was `3.12.3`; no
random seed is applicable because every calculation is exhaustive.

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M54-root-mean-lift-referee/root_quotient_spectrum.py --r-max 14 --exact-r-max 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M54-root-mean-lift-referee/root_quotient_spectrum_results.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M54-root-mean-lift-referee/root_mean_lift_exact.py --r-max 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M54-root-mean-lift-referee/root_mean_lift_results.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M54-root-mean-lift-referee/branch_split_additivity.py --r-max 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M54-root-mean-lift-referee/branch_split_additivity_results.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M54-root-mean-lift-referee/spine_split_audit.py --r-max 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M54-root-mean-lift-referee/spine_split_audit_results.json

python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M54-root-mean-lift-referee/spine_bias_hminus.py --r-max 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-12/mission-M54-root-mean-lift-referee/spine_bias_hminus_results.json
```

The exact sharp ROOT-MEAN-LIFT constants for `r=2,...,7` are
`1,1.075269,1.116345,1.156997,1.198451,1.240218`. The maximum individual
H-minus-one coefficients are
`0,.111111,.150958,.223398,.282762,.328047`, and the maximum sums are
`0,.138889,.339680,.576228,.857589,1.221424`. These are diagnostics only.

## 9. Verdict

OPEN AT A NAMED STEP: SPINE-BIAS H-minus-one BOUND.
