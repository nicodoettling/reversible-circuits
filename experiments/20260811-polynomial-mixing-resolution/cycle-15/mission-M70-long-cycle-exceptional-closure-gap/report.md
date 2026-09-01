# M70 final report: polynomial exceptional closure, residual cyclic incidence

Date: 2026-08-12. Owned directory:
`experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M70-long-cycle-exceptional-closure-gap/`.

## 1. Exact quantified claim and conventions

Permutations compose as `(pq)(x)=p(q(x))`; tuple products are left-to-right.
Let `l>=3`, `n=2l+1`, `m=2l=n-1`, `M=binom(n,2)`, and
`h=(0 1 ... n-1)`.  The state law is uniform on the `n^(n-2)` minimal
transposition factorizations `t_1...t_m=h`.  Pair coordinates are
`X_j=(t_(2j-1),t_(2j))`.

On this same fixed-endpoint space define

```text
C_l=binom(l,2)^(-1)sum_(i<j)P_(i,j),
B_l=(l-1)^(-1)sum_(j=1)^(l-1)P_(j,j+1),
K^h=(1/2)I+(1/6)sum_(r=3)^5
       (m-r+1)^(-1)sum_(i=1)^(m-r+1)H_(i,r).
```

Here `P_(i,j)` is exact heat bath of the two selected pair coordinates and
`H_(i,r)` is exact raw length-`r` same-product heat bath.  `K^h` is not the
identity chain in the global goal.

**Proved scoped theorem.**  Let `F` be the accepted M67 frequency-two additive
witness and let `H_k` be the character space for simultaneous conjugation by
`h`.  For all sufficiently large `l`,

```text
R_C(F), R_B(F), R_(K^h)(F) = O(l^(-3/2)).            (1.1)
```

For every nonzero `k` and every `Phi in H_k`,

```text
R_B(Phi)>=4/(M^4 n^6),
R_C(Phi)>=8/(l M^4 n^6),
R_(K^h)(Phi)>=1/(3M^4 n^6).                          (1.2)
```

On `H_1`, containing `F`, the right sides improve by a factor four.  Hence
the exact Krylov closure `span{F,PF,P^2F,...}` for each chain `P` is
polynomially sandwiched: the witness is a genuine polynomial slow direction,
but its entire invariant closure cannot contain a superpolynomial mode.

This proves the assigned exceptional-closure bypass.  It proves neither the
gap on the invariant sector `H_0`, the full fixed-endpoint bridge gap, nor any
bound on original identity-conditioned `K`.

## 2. Full argument / construction

The full proof, including all constants, is in `theorem.md`.  Its three parts
are as follows.

First, if

```text
V=E|f(G_1)|^2,
C=Re E[conj(f(G_1))f(G_2)],
kappa=C/V,
```

then central two-position symmetry and M67 give

```text
||F||^2=lV[1+(l-1)kappa],
kappa>=(24/d_0)n^(-1/2)+o(n^-1/2),
C>0 eventually.
```

A two-pair heat bath dissipates at most `2(V+C)`.  A raw window of length at
most five touches at most three pair coordinates and dissipates at most
`3V+6C`.  Exact scan averaging gives

```text
R_C(F),R_B(F)
 <=2(1+kappa)/[l(1+(l-1)kappa)],
R_(K^h)(F)
 <=(3+6kappa)/[2l(1+(l-1)kappa)],
```

which are (1.1), since `0<kappa<=1`.

Second, let `mathcal U` conjugate all raw factors by `h`.  Every exact heat
bath commutes with its Koopman operator `U`, and `F in H_1`, where
`H_k={Phi:U Phi=omega^(2k)Phi}`.  The project Hurwitz generators satisfy

```text
delta=sigma_1...sigma_(m-1):
(t_1,...,t_m)->(t_2,...,t_m,h^-1 t_1 h),
delta^m=mathcal U.
```

The word has length `m(m-1)` and uses every generator `m` times.  Telescoping
it and comparing each Hurwitz permutation to its adjacent raw-pair heat bath
gives

```text
R_(L_n)(Phi)>=sin^2(2pi k/n)/[m^2(m-1)^2].           (2.1)
```

For clarity, M27's stated spectral theorem was only for fixed parking
multisets.  M70 independently proves the full-state edgewise padding lemma:
for every off-diagonal adjacent-raw edge `x->y`, choose an aligned H4 window
containing its unique changed pair and keep the two padding factors fixed.
Then

```text
B_l(x,y)>=1/[(l-1)M^4],
L_n(x,y)<=1/[2(m-1)],
```

so pointwise `B_l(x,y)>=M^-4L_n(x,y)`, even when the parking macro changes.
Together with `sin(pi/n)>=2/n`, this proves the `B_l` bound.  The literal
coefficient comparisons

```text
E_C >=(2/l)E_B,
E_(K^h)>=[(l-1)/(6(2l-3))]E_B >=(1/12)E_B
```

give the other two bounds in (1.2).

Third, conjugation acts freely: no nontrivial power of an odd long cycle fixes
a two-element transposition support.  Thus `H_0` is the exact uniform
stationary-flow quotient on `n^(n-3)` cyclic orbits, with

```text
bar P(O,O')=(1/n)sum_(x in O)P(x,O').                (2.2)
```

For a parking multiplicity vector `d(w)`, its cyclic projection is exactly
described by the orbit incidence law

```text
nu_O(d)=(1/n)#{q:d(mathcal U^q w)=d},
A_0f(O)=sum_d nu_O(d)f(d).                            (2.3)
```

Exact enumeration through `n=7` refutes the tempting simplification that
`A_0f` is constant for every centered parking-macro function: the rational
image ranks for `n=3,4,5,6,7` are `1,4,10,36,116`.  At `n=7`, this incidence
law is not even determined by the unlabeled support-tree degree multiset.
This is a finite structural refutation, not an asymptotic gap statement.

## 3. Worst-case probability, runtime, path, and congestion accounting

- Full twist path length: exactly `m(m-1)<n^2`; each adjacent Hurwitz index
  appears exactly `m` times.
- Hurwitz-to-raw-heat-bath loss: at most `4` in squared norm.
- Full-space raw-to-aligned padding: one selected aligned scan has probability
  `1/(l-1)`, and the H4 fiber has at most `M^4`; the retained transition is
  the literal target, with no hub and no path congestion.
- Complete-to-aligned coefficient: exactly `2/l` on retained adjacent pair
  projections.
- `K^h`-to-aligned coefficient: exactly `(l-1)/[6(2l-3)]>=1/12`, including
  laziness, the factor-of-three block choice, and the H4 scan denominator.
- A direct fixed-`r<=5` conditional sampler can enumerate at most `M^r`
  candidate raw blocks, polynomial in `n`; inherited direct samplers are also
  available.  M70 introduces no superpolynomial per-step operation.
- Exact `n=7` enumeration has `16807` states.  The exact combinatorial checks
  take seconds on Python 3.12.3; ARPACK eigenvalues are diagnostic only.

## 4. Dependencies, labeled by status

- **Proved and accepted:** M67 v4's moment/correlation theorem, definitive
  manifest SHA-256
  `629439ef523c86537e9d5170312dd95235d575d0a34d62b76517a91ff95735c0`;
  fresh referee ACCEPT report SHA-256
  `b3ad5bfc5fa249f32363afa115d858271e35ad09cffc18b5e31936838619aa35`.
- **Proved here:** conditional-variance upper bounds; full-twist convention;
  character-sector Poincare inequality; full-space edgewise H4 padding;
  `C_l` and `K^h` coefficient comparisons; free cyclic action and quotient.
- **Cited standard:** Dénes' count `n^(n-2)` for minimal long-cycle
  transposition factorizations.  Only the orbit count uses it; the sector gap
  does not.
- **Empirical/exact finite falsifiers:** all state/fiber construction and rank
  arithmetic are exact; Krylov eigenvalues use floating ARPACK.  Neither is
  used to prove (1.1)--(1.2).
- **Conditional/open:** no input about the `H_0` quotient gap is assumed.

## 5. First unproved standalone step

> **CYCLIC-ORBIT INCIDENCE GAP.**  For every `l>=3`, the exact
> stationary-flow quotient (2.2) of `C_l` or `B_l`, including the nonconstant
> orbit-incidence statistics `nu_O` in (2.3), has inverse-polynomial Poincare
> gap in `n=2l+1`.

This would close the fixed minimal-long-cycle bridge only.  It would not prove
the arbitrary-endpoint or identity-conditioned theorem.

## 6. Strongest self-attack

The full-twist proof deliberately extracts only cyclic frequency.  It gives
zero information on `H_0`, which has `n^(n-3)` states and, by the exact rank
test, retains a substantial parking-derived quotient.  Treating cyclic
rerooting as zero cost does not make the rooted parking macro lumpable; a
comparison to unrooted leaf replanting must be built at microstate
stationary-flow level.  The `n^-14`/`n^-15` lower bounds are very crude but
polynomial; improving them does not address this qualitative zero-frequency
gap.

Conversely, the `O(l^-3/2)` Rayleigh upper bound is only polynomial and is at
a nonidentity endpoint.  A long-cycle prefix fiber inside an identity bridge
is not closed under crossing `H3,H4,H5` windows.  No stationary-mass or
boundary-flow argument here lifts the witness to original `K`.

## 7. Calibration

- Odd identity length is empty; M70 instead uses the even minimal length
  `m=n-1=2l` of an odd long cycle.
- `m=0` and `N=2` are singleton calibrations outside this theorem.
- `m=2` (`l=1`) has no pair-pair scan and is excluded.  `l=2,m=4` needs a
  separate `{3,4}` definition because H5 is absent; M70 starts at `l=3`.
- `S_3,m=4`, `S_4,m=4`, and `S_4,m=6` are identity-bridge calibrations and
  are untouched.  In particular M70 never drops the whole-word H4 update at
  `m=4`; it makes no claim there.
- Every M70 state is near-minimal in the strongest sense: its support graph is
  a labeled tree with distinct edges.  This is why adjacent raw-pair fibers
  have size two or three.
- At `n=7,l=3`, exact enumeration checks the full twist on all `16807` states
  and all `120050` directed raw-pair edges for full-space H4 padding.  The
  minimum exact ratio `B_l(x,y)/(M^-4L_n(x,y))` is `194481/25>1`.
- The finite Krylov gaps are `0.25303` (`C`), `0.17535` (`B`), `0.01549`
  (`L`), and `0.10230` (`K^h`); these are falsifiers only.

## 8. Artifacts and reproduction commands

- `plan.md`
- `checkpoint.md`
- `theorem.md`
- `n7_exceptional_krylov.py`, `n7_exceptional_krylov.json`
- `h0_parking_projection.py`, `h0_parking_projection_n7.json`

Commands from repository root:

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M70-long-cycle-exceptional-closure-gap/n7_exceptional_krylov.py --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M70-long-cycle-exceptional-closure-gap/n7_exceptional_krylov.json
python3 experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M70-long-cycle-exceptional-closure-gap/h0_parking_projection.py --n-max 7 --output experiments/20260811-polynomial-mixing-resolution/cycle-15/mission-M70-long-cycle-exceptional-closure-gap/h0_parking_projection_n7.json
```

Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
Seed: none; both computations are deterministic.

## 9. Verdict

**PROVED**

The assigned exceptional-closure claim is proved: the M67 witness is a
polynomial slow direction, while its entire nonzero-frequency invariant
closure has an explicit inverse-polynomial gap.  This is a nonterminal scoped
theorem.  The global goal remains open at CYCLIC-ORBIT INCIDENCE GAP and, far
beyond it, at the arbitrary-endpoint/identity mean-lift.
