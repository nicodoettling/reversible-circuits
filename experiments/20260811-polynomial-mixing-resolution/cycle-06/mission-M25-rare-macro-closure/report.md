# M25 final report: the maximal disconnected macro closure leaks polynomially

## 1. Exact claim, quantifiers, convention, and kernel

Use `(pq)(x)=p(q(x))`; words evaluate as `t_1...t_m`.  Let
`M=binom(N,2)`.  For every `N>=5`, set

```text
L=N^3,                 m=4(L+1)=4N^3+4.                (1.1)
```

The original chain is

```text
K=(1/2)I
 +(1/6) sum_{r=3}^5 [1/(m-r+1)] sum_i H_{i,r}.         (1.2)
```

Let `c(w)` be the number of components of the transposition support graph,
including isolated labels, and define

```text
U_N={w in Omega(N,m):c(w)>=2}.                          (1.3)
```

Let `A_N` denote the entire M22 rare macro: one connected size-three
weight-four component and one connected complementary component of weight
`m-4`, with all label choices, internal words, and color interleavings.

**Theorem (proved).**  The macro `A_N` is nonempty and is contained in `U_N`.
The latter is the maximal union of all disconnected macro-fibers and obeys

```text
pi_{N,m}(U_N)<=1/4,                                    (1.4)

Phi_pm^K(U_N)
 :=Q_K(U_N,U_N^c)/min(pi(U_N),pi(U_N^c))
 >=(N-1)/(128M^2)
 =1/[32N^2(N-1)]
 >=1/(32N^3).                                          (1.5)
```

Thus the entire rare macro plus the strongest possible halo made only of
disconnected macros is not a superpolynomial bottleneck for this explicit
infinite sequence.  This is a scoped anti-bottleneck theorem, not Terminal A
or a refutation of Terminal B by other cuts.

## 2. Full proof and construction

### 2.1 Why this is the strongest macro closure

The rare size-three component supports a connected identity word of length
four, and the complementary `N-3` labels support one of even length `4N^3`,
since

```text
4N^3>=2((N-3)-1).
```

Their disjoint interleavings prove `A_N` is nonempty.  Both components
together use all labels, so this is **not** a missing-label event.

Every word-level move which changes only color order remains in `A_N`.  Every
split, isolate creation, weight transfer, repartition, or partial merge whose
output remains disconnected lies in `U_N`, regardless of how far its macro
is from `A_N`.  Therefore `U_N` absorbs every such move, not only a chosen
one-step list.  Conversely, the only macro datum not in `U_N` is

```text
{([N],m)},                                               (2.1)
```

the connected full-support macro.  Thus `U_N` is the maximal proper union of
complete disconnected macros.  It is stronger than the requested minimal
halo: any further macro-saturated enlargement is all of `Omega(N,m)`.

### 2.2 Dense exact-partition input and mass orientation

The frozen Cycle-02 M12 theorem applies because, for `N>=5`,
`log(2N)<=N` and

```text
4M log(2N)
 <=2N^2(N-1)
 <=2N^3
 <m-2=4N^3+2.                                          (2.2)
```

For completeness, here is the exact part of that theorem used below.  For a
labeled set partition `P`, let `E_P(k)` be the number of ordered length-`k`
identity words with exact support partition `P`.  If `e(P)` is the number of
transpositions internal to its blocks and `h(P)` is the product of their
factorial sizes, the parity-aware central-walk trace plus a union bound over
block refinements gives, at `k=m,m-2`,

```text
e(P)^k/h(P) <=E_P(k)<=4e(P)^k/h(P).                    (2.3)
```

This estimate includes isolated blocks, all direct-product parity modes, and
every ordered component-color interleaving.

Define the exact component-layer counts

```text
W_c(k)=sum_{P:|P|=c}E_P(k),
Z_N(m)=sum_{c=1}^{N-1}W_c(m)=|Omega(N,m)|.              (2.4)
```

In particular, the global stationary mass is exactly

```text
pi(U_N)=[sum_{c=2}^{N-1}W_c(m)]/Z_N(m).                 (2.5)
```

To compare adjacent layers, merge the first two blocks of a partition,
ordered by least label.  If their sizes are `a,b`, (2.3) bounds the source to
target weight ratio by

```text
4 binom(a+b,a) exp[-4log(2N)ab].                        (2.6)
```

For each target, summing (2.6) over every possible split of its block
containing label one is at most `4/N^4`.  All inverse multiplicities are in
this preimage sum.  Therefore

```text
W_{c+1}(m)<=q_N W_c(m),          q_N=4/N^4<=1/4.        (2.7)
```

It follows that

```text
sum_{c>=2}W_c(m)
 <=W_2(m)/(1-q_N)
 <=W_1(m)/3.                                            (2.8)
```

Equations (2.5)--(2.8) prove both

```text
pi(U_N)<=1/4                                            (2.9)
```

and the exact boundary-layer comparison

```text
W_2(m)/sum_{c>=2}W_c(m)>=1-q_N>=3/4.                   (2.10)
```

This is a global orientation under `pi_{N,m}`, not a conditional macro mass.

### 2.3 Actual padded-H3 escape from the two-component layer

Fix an exact two-block partition `P`.  Put

```text
e=e(P),                    x=M-e.
```

Thus `e` is the number of internal edges and `x` is the number crossing the
two components.  At a designated adjacent slot, inserting `(t,t)` into an
exact-support core counted by `E_P(m-2)`, with `t` one of the `e` internal
edges, is injective.  Deletion recovers the core and `t`.  Equation (2.3)
therefore gives the exact averaged safe-square bound

```text
e E_P(m-2)/E_P(m)>=1/(4e).                              (2.11)
```

For every such marked square and every crossing transposition `s`, use the
actual update

```text
(t,t,a)->(s,s,a),
```

padding on the left instead at the final adjacent slot.  Both ordered block
products equal the padding transposition `a`.  Deleting `(t,t)` retained
exact partition `P`, while inserting the crossing square `(s,s)` joins its
last two components.  Hence the target has `c=1` and exits `U_N`.

The exact length-three transposition-product fiber size is

```text
D_N=F_3(a)=(3N^2+N-12)/2<=4M.                           (2.12)
```

One specified target therefore has full-`K` probability

```text
1/[6(m-2)D_N],                                          (2.13)
```

including the factor `1/2` from laziness, the probability `1/3` of selecting
`r=3`, the scan over `m-2` windows, and uniform conditional resampling.

Targets charged to different marked adjacent positions have different
discrepancy positions; summation is collision-free.  Summing over all `m-1`
positions and all `x` crossing edges gives the exact-partition averaged exit
bound

```text
(m-1)[1/(4e)]x/[6(m-2)D_N]
 >=x/(24eD_N)
 >=(N-1)/(96M^2)=:alpha_N.                             (2.14)
```

The last inequality uses `e<=M`, `D_N<=4M`, and
`x=a(N-a)>=N-1` for every two-block partition, including one isolated label.

### 2.4 Complete boundary-flow normalization

For `r=3,4,5`, define the exact stationary contribution

```text
Q_r(U_N,U_N^c)
 =pi(U_N)/[6(m-r+1)]
   E_{w|U_N}[sum_i H_{i,r}(w,U_N^c)].                   (2.15)
```

The lazy identity contributes no boundary flow, and the original chain has
the exact equality

```text
Q_K(U_N,U_N^c)=Q_3+Q_4+Q_5.                            (2.16)
```

Equation (2.14) retains a certified subset of `Q_3` from `c=2`.  Every other
`H_3` exit and all `Q_4,Q_5` exits remain present and nonnegative.  Combining
(2.10), (2.14), and the orientation (2.9) yields

```text
Phi_pm^K(U_N)
 >=(3/4)alpha_N
 =(N-1)/(128M^2),                                      (2.17)
```

which is (1.5).  No projection, rejected-exit restriction, or graph-only
transition probability has replaced `K`.

## 3. Worst probability, runtime, path, and congestion accounting

- Exact smaller-side mass: equation (2.5), with the rigorous orientation
  `pi(U_N)<=1/4`.
- Exact relative mass of the charged `c=2` layer: at least `3/4`.
- Safe-square incidence at one marked slot: at least `1/(4e)` averaged in
  every exact two-component partition.
- Specified full-chain heat-bath target: `1/[6(m-2)D_N]`.
- Summed two-component exit: at least `(N-1)/(96M^2)`.
- Conductance: at least `(N-1)/(128M^2)>=1/(32N^3)`.
- Every witness is one actual `K` transition; path length is one and there is
  no comparison congestion or canonical hub.
- Locating a safe adjacent square costs `O(m)`; listing all crossing targets
  costs `O(N^2)`.  The exact `r<=5` block sampler has inherited polynomial
  per-step cost.

## 4. Dependencies and statuses

1. **Proved here:** the exact closure interpretation, rare-macro inclusion,
   dense-hypothesis check, and specialization through (2.17).
2. **Proved and independently frozen in Cycle-02 M12:** the central trace
   estimate (2.3), layer ratio (2.7), safe-square incidence, collision audit,
   and full-`K` dense-threshold theorem.  Exact source:
   `cycle-02/mission-M12-high-surplus/proof_final.md`, Theorem 1 and Lemmas
   2.1, 2.2, 3.1.
3. **Inherited proved:** connected identity-factorization feasibility iff the
   even length is at least `2(v-1)`; component interleaving; exact heat-bath
   reversibility and stationarity.
4. **Not used:** M23's missing-label theorem, any connected-Hurwitz gap,
   length-two simulation, finite spectrum, fresh-square folklore, canonical
   routing, or graph-only dynamics.
5. **Empirical dependencies:** none.

## 5. First unproved standalone proposition

> **FULL-SUPPORT ONE-STEP SHELL.**  For the sequence (1.1), let
>
> ```text
> F_N={y:c(y)=1 and K(x,y)>0 for some x in U_N},
> V_N=U_N union F_N.
> ```
>
> Determine whether `V_N` is a proper subset, compute its exact global
> stationary orientation, and account for all `Q_3+Q_4+Q_5` flow from `V_N`.
> If it is proper, prove inverse-polynomial conductance or prove a
> superpolynomial upper bound.

Because (2.1) is the unique connected macro, this proposition necessarily
uses internal full-support structure rather than only component data or color
interleavings.

## 6. Strongest self-attack

This proof controls the maximal disconnected **macro-saturated** closure.  It
does not imply a conductance lower bound for every smaller hand-picked subset:
conductance is not monotone under set inclusion.  Nor does it control a cut
which includes a carefully selected part of the connected full-support fiber.

The proof also uses the deliberately dense sequence `m=4N^3+4`.  A rare-macro
construction at near-minimal or intermediate length can fall outside the
trace hypothesis and remains logically separate.  Finally, a polynomial
lower bound for this cut is not a global Poincare inequality and supplies no
evidence against unrelated Terminal-B mechanisms.

## 7. Calibration

- Odd `m`: the bridge is empty; no cut is asserted.
- `m=0` and `N=2` with even `m`: singleton regimes; outside the theorem.
- `m=2,N>=3`: excluded disconnected chain; outside the theorem.
- `S_3,m=4`: `W_1=24,W_2=3`, total 27, with four pure-Hurwitz macros.  The
  whole-word `H_4` has coefficient `1/4`; the dense theorem is not asserted.
- `S_4,m=4`: `W_2=114,W_3=6`, total 120, with 13 macros.  Full support is
  infeasible, showing why dense orientation must not be extrapolated here;
  `H_4` is retained.
- `S_4,m=6`: `W_1=2880,W_2=1050,W_3=6`, total 3936, with 17 macros.
- The rare component is exactly near-minimal, of length `2(3-1)=4`; the
  complementary component satisfies the exact feasibility criterion.
- Exact-partition weights include every ordered color interleaving of
  disjoint components.
- No edge-multiplicity or vertex-degree parity shortcut is used.
- Every boundary witness is an actual padded `H_3`, not the false `L=2`
  simulation.
- The mass is globally oriented before conductance is divided, and the full
  `Q_3+Q_4+Q_5` decomposition is explicit.

## 8. Artifacts and reproduction

Owned artifacts:

- `plan.md`
- `checkpoint.md`
- `report.md`

No computation was needed.  Reproduce the proof by checking equations
(2.2)--(2.17) against the frozen exact-partition result at

```text
experiments/20260811-polynomial-mixing-resolution/
  cycle-02/mission-M12-high-surplus/proof_final.md
```

Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 9. Verdict

PROVED

The verdict concerns the inverse-polynomial conductance of the maximal
disconnected rare-macro closure, not either global terminal outcome.
