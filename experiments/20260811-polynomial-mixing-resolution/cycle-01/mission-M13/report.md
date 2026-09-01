# M13 Final Report: Full-Support and Entropic Red Team

## 1. Exact claim and outcome

Fix maps on `[N]` with multiplication `pq=p after q`, so
`(pq)(x)=p(q(x))`, and evaluate a word as `t_1...t_m`.  The target is
uniform on

```text
Omega(N,m) = {w in T_N^m : eval(w)=id},
```

and the reviewed kernel is

```text
K = (1/2) I
  + (1/(2 |R_m|)) sum_{r in R_m}
      (1/(m-r+1)) sum_i H_{i,r},
R_m = {3,4,5} intersect [m].
```

Here `H_{i,r}` is uniform on the exact length-`r` same-product fiber.

The assigned terminal claim under attack was:

> There is an allowed `(N,m)` for which `K` is reducible, or there is an
> explicit infinite sequence along which its gap is superpolynomially small
> in `Nm`, caused by a statistic invisible to labeled weighted support
> components.

No such construction survived. Two natural infinite-family cuts in the
minimal all-label connected fiber are rigorously rejected below, including
their exact stationary masses and normalized transition probabilities. A
naive constant-one mean-lift inequality is rigorously refuted, but the
required polynomial-factor mean-lift statement is not.

## 2. Full argument and constructions

### 2.1 Standard restriction and exact Hurwitz domination

Let `F` be a feasible labeled weighted support-component fiber, and let
`pi_F` be uniform on `F`. The standard restriction of `K` to `F` is

```text
K^F(x,y) = K(x,y)                                      if x != y are in F,
K^F(x,x) = K(x,x) + K(x,Omega(N,m) minus F).
```

Thus every exit is held. Its Dirichlet form is

```text
E_{K^F}(f,f)
 = (1/(2|F|)) sum_{x,y in F} K(x,y) (f(x)-f(y))^2.
```

Define the lazy symmetric random-scan Hurwitz walk `P_H` on `F` by

```text
P_H = (1/2) I
    + (1/(4(m-1))) sum_{j=1}^{m-1} (U_{j,+}+U_{j,-}),
```

where, for transpositions,

```text
U_{j,+}: (a,b) -> (b,bab),
U_{j,-}: (a,b) -> (aba,a).
```

The two deterministic maps are inverse permutations of `F`, so `P_H` is
reversible for `pi_F`. Ben-Itzhak--Teicher Theorem 3.4, with the already
audited inverse-generator convention translation, makes `P_H` irreducible
on `F`.

Put `M=binom(N,2)` and `B=|R_m|`. For every `N>=3` and even `m>=4`,

```text
E_{K^F}(f,f)
 >= [(m-1)/(2 B (m-2) M^2)] E_{P_H}(f,f).                 (2.1)
```

Proof with all normalizations:

1. For `j<=m-2`, assign both oriented Hurwitz moves at pair `j,j+1` to
   the length-three window starting at `j`. Assign the two moves at the
   last pair `m-1,m` to the window starting at `m-2`.
2. Each assigned output is in the same length-three same-product fiber and,
   because a Hurwitz move preserves labeled weighted support components, is
   in `F`.
3. If `F_3(h)` is the size of a length-three conditional fiber, then
   `F_3(h)<=M^2`: the first two transpositions determine the third
   permutation uniquely. Hence each specified output has conditional
   probability at least `M^{-2}`.
4. A length-three window receives at most four assigned oriented generator
   instances: the last window can receive two signs for each of its two
   adjacent pairs. Even if outputs coincide, its heat-bath squared-difference
   sum is therefore at least `1/(4M^2)` times the assigned Hurwitz sum.
5. The `r=3` contribution to `E_{K^F}` has coefficient
   `1/[4B(m-2)]`: one factor `1/2` is from the Dirichlet-form definition,
   one is the outer laziness in `K`, then come `1/B` and `1/(m-2)`.
   Consequently
   `E_{K^F} >= [1/(16B(m-2)M^2)] sum_{j,sign} E[(Delta f)^2]`.
6. The same generator sum in `E_{P_H}` has coefficient
   `1/[8(m-1)]`. Dividing the coefficients gives (2.1).

Therefore

```text
gap(K^F)
 >= [(m-1)/(2 B (m-2) M^2)] gap(P_H).                    (2.2)
```

For `m=4`, `B=2` and the coefficient is `3/(8M^2)`; the whole-word
`r=4` heat bath is present in `K` but is not needed for this lower
comparison. For even `m>=6`, `B=3`.

This closes the literal hidden-invariant avenue inside a macro-fiber:
Classification H plus (2.1) gives connectivity with explicitly polynomial
one-edge weights. It does not close the expansion avenue, because a connected
Hurwitz Schreier graph can still have an exponentially thin collective cut.

### 2.2 Exact prefix locality and an unavoidable polynomial speed limit

For `X_k=t_1...t_k`, a same-product window changes `X_k` only if it
straddles the cut `k|k+1`. The number of eligible length-`r` windows is

```text
c(m,k,r)
 = max(0, min(k,m-r+1) - max(1,k-r+2) + 1),
```

so the exact probability of selecting an eligible window is

```text
a(m,k)
 = (1/(2B)) sum_{r in R_m} c(m,k,r)/(m-r+1).             (2.3)
```

This is `O(1/m)` at an interior cut.

There is also a rigorous gap upper bound on every nonempty all-label
connected-support fiber. Global conjugation acts transitively on
transpositions and preserves that fiber, so `pi_F(t_1=s)=1/M` for every
`s in T_N`. Only the unique window starting at position one can alter
`t_1`. The indicator Rayleigh quotient therefore gives

```text
gap(K^F)
 <= [1/(1-1/M)] [1/(2B)] sum_{r in R_m} 1/(m-r+1).       (2.4)
```

Thus a uniform constant gap is false. Equation (2.4) is only polynomial
slowness and cannot refute TERMINAL A.

### 2.3 Rejection of the adjacent-doubled-tree cut

Now take the minimal full-support regime `m=2(N-1)` and write
`F_N` for its all-label connected fiber. Goulden--Jackson Theorem 1.1
specialized to cycle type `1^N` gives

```text
|F_N| = (2N-2)! N^(N-3).                                 (2.5)
```

Let `D_N` consist of words

```text
(e_1,e_1,e_2,e_2,...,e_{N-1},e_{N-1})
```

whose distinct edges form a labeled tree. Cayley's and Dénes' enumeration
gives

```text
|D_N| = N^(N-2) (N-1)!,
pi_F(D_N) = N!/(2N-2)!.                                  (2.6)
```

This is superexponentially small, so its small mass cannot simply be ignored.

Nevertheless it is not a trap. In every state of `D_N`, apply the right
Hurwitz move to the first two factors of the length-three block
`(e_1,e_2,e_2)` starting at position two. Since `e_1!=e_2`, the result is
not in `D_N`; it remains in `F_N`. The exact kernel assigns this specified
output probability at least

```text
q_N = 1/[2 B (m-2) M^2].                                 (2.7)
```

Accordingly its stationary boundary flow satisfies the fully normalized bound

```text
Q_F(D_N,D_N^c)
 = pi_F(D_N) E[K^F(x,D_N^c) | x in D_N]
 >= pi_F(D_N) q_N,
```

and its outward conductance is at least `q_N`, an inverse polynomial.
The canonical doubled-tree family is therefore neither a useful comparison
hub nor a superpolynomial bottleneck cut.

### 2.4 Rejection of the midpoint-N-cycle (“mountain”) cut

Let

```text
A_N = {w in F_N : X_{N-1} is an N-cycle}.
```

Dénes' theorem gives exactly `N^(N-2)` minimal transposition
factorizations of each fixed `N`-cycle. There are `(N-1)!` such cycles,
and conditional on the midpoint the two halves are independent
factorizations of `x` and `x^{-1}`. Hence

```text
|A_N| = (N-1)! N^(2N-4),
pi_F(A_N) = (N-1)! N^(N-1)/(2N-2)!.                      (2.8)
```

By Stirling's formula this mass is exponential on the scale
`(e/4)^N`. It is below `1/2` from `N=5` onward and then decreases, so
this is a legitimate rare-mass asymptotic cut to audit.

Fix its midpoint cycle `x`. Let `a` be the last transposition in the first
half. If `a` cuts the cycle into lengths `s,N-s`, the number of possible
minimal prefixes is

```text
binom(N-2,s-1) s^(s-2) (N-s)^(N-s-2).
```

This follows because a minimal factorization of the two-cycle permutation
`xa` splits into independently interleaved minimal factorizations of its two
cycles. In particular, for each of the `N` cyclically adjacent
transpositions,

```text
Pr(a=e | x) = p_N = (N-1)^(N-3)/N^(N-2).
```

The first transposition `b` of the second half has the same marginal,
independently conditional on `x`. Therefore the exact probability that
`a,b` are distinct cyclically adjacent edges is

```text
rho_N = N(N-1)p_N^2
      = ((N-1)/N)(1-1/N)^(2N-6)
      >= 1/24.                                           (2.9)
```

For two distinct noninterlacing chords of a cycle, at least one of `xab`
and `xba` has three cycles: right multiplication by the first chord cuts
the cycle, and the second chord either cuts one resulting cycle or joins the
two; if one order joins, the reverse order cuts. Distinct cyclically adjacent
edges are noninterlacing. In the project convention, the right and inverse
Hurwitz moves across the midpoint change the midpoint from `x` to
`xab` and `xba`, respectively. Thus, on the event in (2.9), at least one
specified output leaves `A_N` while staying in `F_N`.

Using the length-three window beginning at the midpoint and the same exact
normalization as (2.7),

```text
Q_F(A_N,A_N^c)
 >= pi_F(A_N) rho_N/[2 B (m-2) M^2],
Phi_F(A_N)
 >= 1/[48 B (m-2) M^2].                                 (2.10)
```

Thus the exponentially rare mountain family has inverse-polynomial outward
conductance. Prefix height alone does not yield TERMINAL B in the most
extreme minimal-factorization phase.

### 2.5 Explicit mean-lift counterexample to constant one

Let the macro partition be labeled weighted support-component data and let
`F` be one macro-fiber. Define its exit propensity

```text
b(x)=K(x,F^c),  b_bar=E[b | F],
h(x)=(b_bar-b(x)) 1[x in F].
```

Then `h` has conditional mean zero in every macro-fiber. For
`f_theta=1_F+theta h`, the fiber means are exactly `1` on `F` and
`0` elsewhere, so their projected Dirichlet energy is
`Q(F,F^c)=pi(F)b_bar`. On the full chain,

```text
E(1_F,h)
 = sum_{x in F} pi(x)b(x)h(x)
 = -pi(F) Var_F(b).
```

Consequently, whenever `b` is nonconstant, choosing

```text
theta = pi(F) Var_F(b) / E(h,h)
```

strictly lowers `E(f_theta,f_theta)` below the projected energy. The
unqualified inequality with `q_lift=1` is therefore false.

The exact `S_4,m=6` calculation found 25 exit-propensity values on the
2880-state full-support fiber,

```text
pi(F)=30/41,
b_bar=99483/852800,
Var_F(b)=2718739/3285360000,
theta=146577006950400/60313936202861,
E_projected/E_full=18000633945807662589/
                   17690307456970582525
                  = 1.0175421761...
```

for this explicit function. This refutes only constant one. It neither
produces a growing lower bound on `q_lift(N,m)` nor refutes a polynomial
mean-lift comparison.

## 3. Probability, runtime, path length, and congestion accounting

- A specified padded Hurwitz output receives probability at least
  `1/[2B(m-2)M^2]` from `K`.
- The Dirichlet comparison loss in (2.1) is at most
  `2B(m-2)M^2/(m-1)`; this is a direct edge allocation, not routing through
  a canonical state. The allocation multiplicity is at most four.
- The doubled-tree outward probability is at least (2.7) for every state.
- The mountain outward probability averaged under its exact stationary
  conditional law is at least (2.10).
- No comparison paths, diameter theorem, or multicommodity flow are claimed;
  hence there is no hidden path-length or hub-congestion assertion.
- The deterministic exact script enumerates `M^m` words in each smoke case
  and then all conditional block outcomes for the named cuts. It checked
  4,923,552 block outcomes in `S_4,m=6` and completed in about 17 seconds
  in the recorded environment. This is a finite falsifier, not a scalable
  sampler.

## 4. Dependencies

- **Proved project inputs:** exact heat-bath reversibility/stationarity;
  feasible connected-component lengths; macro-fiber factorization; exact
  kernel definition and normalization.
- **Cited and convention-audited:** Ben-Itzhak--Teicher, Theorem 3.4, for
  identity-factorization Hurwitz classes. Its generator is inverse to the
  project's named right move and gives the same equivalence relation.
- **Cited:** I. P. Goulden and D. M. Jackson, “Transitive Factorisations into
  Transpositions and Holomorphic Mappings on the Sphere,” *Proc. AMS* 125
  (1997), Theorem 1.1, for (2.5) and the genus-zero specialization.
- **Cited:** J. Dénes, “The Representation of a Permutation as the Product of
  a Minimal Number of Transpositions, and its Connection with the Theory of
  Graphs,” 1959, for the `N^(N-2)` long-cycle count.
- **Proved here:** restriction normalization, comparison (2.1), prefix
  locality and (2.4), the two cut-flow lower bounds, and the general
  exit-propensity mean-lift construction.
- **Exact finite computation:** all numbers attributed to
  `exact_cut_audit.py`. They are not asymptotic evidence.
- **Resource audit result:** a targeted primary-source search found
  transitivity and enumeration papers but no quantitative spectral-gap or
  mixing theorem for this exact identity-factorization Hurwitz walk. This is
  a limited negative search result, not proof that no such theorem exists.

## 5. First unproved standalone proposition

**Uniform connected Hurwitz-orbit gap.** There exist universal constants
`c>0` and `C<infinity` such that, for every `N>=3` and every even
`m>=2(N-1)`, the lazy symmetric random-scan right/inverse Hurwitz walk
`P_H` on the set of length-`m`, all-label connected-support
transposition factorizations of the identity satisfies

```text
gap(P_H) >= c (Nm)^(-C).
```

Together with (2.2), this would give the required polynomial restricted gap
on the full-support fiber. It does not by itself prove the projection or
mean-lift bounds.

## 6. Strongest self-attack

The comparison is deliberately one-way. Polynomial move probabilities,
transitivity, and rejection of two geometrically natural cuts do not preclude
a barbell hidden in the braid-group action. The Hurwitz Schreier graph may
have a collective bottleneck involving many tree/map shapes even though no
individual statistic is invariant and every canonical/mountain state has a
polynomial-probability exit. Conversely, a slow `P_H` would not
automatically make `K^F` slow because the larger heat baths can bypass it.

The mean-lift witness shows precisely why a Jensen argument with constant one
fails, but its ratio is only `1.0175` in one finite case. Exit propensity or
the capacity of gateway states could still deteriorate superpolynomially;
nothing here bounds it asymptotically. The exact finite conductances reject
only the named small cuts.

## 7. Calibration results

- Odd `m`: `Omega(N,m)` is empty; no chain claim.
- `m=0`: singleton.
- `N=2`, even `m`: singleton.
- `m=2,N>=3`: disconnected and excluded.
- `S_3,m=4`: 27 identity words, 24 all-label full-support words; the script
  includes the whole-word `r=4` heat bath.
- `S_4,m=4`: 120 identity words, while the all-four-label connected fiber is
  empty because `4<2(4-1)`.
- `S_4,m=6`: 3936 identity words, 2880 all-label full-support words.
- Zero prefix-locality violations occurred in 4,923,552 exact `S_4,m=6`
  block outcomes.
- Exact smaller-side conductance in `S_4,m=6`: midpoint/mountain
  `2017283/12894336 ~= 0.156447`; aligned doubled tree
  `1324/4797 ~= 0.276006`; every distinct-edge threshold was at least
  `0.247185`.
- Explicit one-step full-support witnesses change distinct-edge count,
  edge-multiplicity parity, vertex-degree parity, midpoint distance, and
  aligned doubled-tree status.
- Disjoint-component color interleaving is not silently removed: (2.1) was
  stated for a general fixed macro-fiber, while the asymptotic cuts were
  explicitly all-label connected.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
| --- | --- | --- | --- | --- | --- |
| Exact `K`, with standard restriction `K^F` for fiber cuts | global uniform bridge; conditional uniform on `F` after restriction | yes, all enumerated outputs | unrestricted options cross macro/Hurwitz classes; `F` itself is one Hurwitz class | exact counts, prefix locality, named cut flow, exit propensity | reject the named finite and asymptotic cuts only |

- No use was made of the false length-two simulation claim, the fixed-hub
  routing strategy, or finite convergence extrapolation.

## 8. Artifacts and reproduction

Files:

- `plan.md`
- `checkpoint.md`
- `exact_cut_audit.py`
- `results.json`
- this `report.md`

Commands, from the repository root:

```text
python3 -m compileall experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M13/exact_cut_audit.py
python3 experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M13/exact_cut_audit.py --output experiments/20260811-polynomial-mixing-resolution/cycle-01/mission-M13/results.json --seed 130013 --commit 502a6f031c6d5a4bc0064ee5b370a4fa3914f993
```

Environment: Python 3.12.3, Linux 6.8.0-136-generic x86_64, no nonstandard
dependencies. The recorded seed is `130013`; the calculation is
deterministic.

## 9. Verdict

OPEN AT A NAMED STEP: Uniform connected Hurwitz-orbit gap.

