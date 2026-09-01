# M328 fixed charge and first obstruction

Date: 2026-08-14 UTC

Status: **the predeclared source-local charge is obstructed formally; actual `d>=6` AATSD remains unresolved.** No computation was run.

## 1. Exact node algebra retained

At an authenticated compatible node `I`, retain M324/M327's literal residual signatures and write

```text
V=G_I(U),                         W=lambda(V),
C(P)={Q in V:D_I(P) intersect D_I(Q) nonempty},
c(P)=lambda(C(P)),
E={ {Q,R} subset V:D_I(Q) intersect D_I(R)=empty },
Phi=sum_({Q,R} in E) lambda_Q lambda_R,
rho=2Phi/W^2.
```

For an active pivot `P`, the whole child is exactly `C(P)`, not a chosen subcell, and

```text
D_child(Q)=(D_I(P) intersect D_I(Q));h_P^(-1),
E_child={ {Q,R} subset C(P):
          D_I(P) intersect D_I(Q) intersect D_I(R)=empty },
T(P)=sum_({Q,R} in E_child) lambda_Q lambda_R,
W'=c(P),       Phi'=T(P),       rho'=2T(P)/c(P)^2.   (1.1)
```

Each actual matching edge `Q` carries its literal M135 incidence flag

```text
iota(Q)=(source global S_d-orbit, source H-orbit,
         target global S_d-orbit, target H-orbit),
```

and the selected set is a perfect matching in the `d`-regular bipartite orbit-incidence multigraph `B_(d,i)`.

## 2. Predeclared candidate: MIDEC

This candidate was fixed after the source lock and before any computation.

For a pivot `P`, give each child edge `f={Q,R}` normalized demand

```text
nu_f=2 lambda_Q lambda_R/c(P)^2,
```

and each parent edge `e={A,B}` normalized capacity

```text
mu_e=2 lambda_A lambda_B/W^2.
```

Call `e` literally incidence-admissible for `f` at `P` when either `e=f` is already a parent edge, or the matching edges indexed by `P,Q,R,A,B` occur on one common simple `M`-alternating cycle of the literal multigraph `B_(d,i)`. This relation uses the actual source/target orbit incidences; it does not inspect final edge signs or create an arbitrary post hoc mass matching.

> **MATCHING-INCIDENCE DELETED-EDGE CHARGE (MIDEC).** There are universal constants `B,C,K` such that at every nonterminal actual `d>=6` node some active `P` admits nonnegative coefficients `theta_(f,e)`, supported only on the preceding literal incidence-admissibility relation, with
> ```text
> sum_e theta_(f,e)=nu_f                         for every child edge f,
> sum_f theta_(f,e)<=mu_e                        for every parent edge e,
> sum_e mu_e-sum_f nu_f
>   >= log(W/c(P))/(C log d),                    (2.1)
> ```
> and, unless the child is edgeless,
> ```text
> sum_e mu_e-sum_f nu_f >= d^(-B).              (2.2)
> ```
> Moreover each literal incidence flag participates in at most `d^K` admissible charge paths.

MIDEC is deliberately a before-norms weighted charge: `sum_e mu_e=rho` and `sum_f nu_f=rho'`. Hence (2.1)--(2.2) imply AATSD (6.1)--(6.2) exactly, without an induced-child substitution or a support-size bound.

## 3. First exact obstruction: unweighted incidence has no arbitrary-weight capacity

MIDEC's source-local mechanism cannot be obtained from M135 incidence/orbit data with arbitrary nonnegative weights.

Consider any active pivot `P` and a genuinely regenerated child edge `f={Q,R}`:

```text
D_I(Q) intersect D_I(R) nonempty,
D_I(P) intersect D_I(Q) nonempty,
D_I(P) intersect D_I(R) nonempty,
D_I(P) intersect D_I(Q) intersect D_I(R)=empty.      (3.1)
```

Every parent edge deleted by pivoting at `P` has at least one endpoint in `V\C(P)`. Keep `lambda_Q,lambda_R` fixed and positive, and multiply every weight in `V\C(P)` by `epsilon>0`. Then the regenerated demand `nu_f` stays bounded away from zero as `epsilon -> 0`, whereas the capacity of every deleted parent edge tends to zero. A literal alternating cycle changes no weight: its off-matching rungs have no `lambda` coordinate at all. Bounded path multiplicity therefore cannot repair the capacity deficit.

Equivalently, a weight-independent source-local map from regenerated triples to deleted parent incidences can never prove a universal inequality of the form

```text
sum_(regenerated f) lambda(f)
 <= d^K sum_(deleted e) lambda(e)                    (3.2)
```

for arbitrary `lambda`: the two sides use independently scalable coordinates. This remains true even if all incidence-admissibility restrictions are dropped. Thus the obstruction is to the weighted charging mechanism itself, not to the chosen alternating-cycle radius.

M135 supplies an unweighted regular multigraph and perfect matching. It supplies neither weights on off-matching rungs nor any comparison between arbitrary weights on different selected edges. Its conflict independence is also only a paired-generated-subgroup invariant and does not detect (3.1). Consequently the stipulated literal incidence/orbit data cannot pay regenerated triple-shadow mass with inverse-polynomial loss after all weights are retained.

The authenticated `d=3` star/triple from M301/M304/M324 is an exact boundary realization of precisely this scaling failure: heavy pairwise-compatible leaves regenerate a positive child edge while all deleted-edge capacity can be made arbitrarily small. It is used only to validate the formal obstruction, not as a `d>=6` counterexample.

This does **not** refute actual `d>=6` AATSD. A weight-dependent active-pivot theorem could avoid every regenerative pivot exposed by (3.1), but proving that requires new actual triple-orbit information absent from M135 incidence.

## 4. Strictly weaker surviving lemma

The strongest clean repair that survives the scaling obstruction is:

> **RELATIVE ACTIVE TRIPLE-SHADOW DESCENT (RATSD).** There are universal `B,C` such that along some anchored actual path, whenever the child is nonterminal, an active pivot satisfies
> ```text
> log(W/W') <= C log(d) (rho-rho'),
> rho-rho' >= d^(-B) rho.                            (4.1)
> ```

RATSD is strictly weaker than AATSD because its decrease vanishes with the current weighted conflict density. It is compatible with independent rescaling of low-mass conflict coordinates. It is **unresolved** and, by itself, does not give a polynomial pivot bound for arbitrary real weights: one still needs an actual low-density terminality statement

```text
rho<d^(-B_1)  =>  some active pivot has edgeless child. (4.2)
```

or another weight-independent stopping certificate. Equations (4.1)--(4.2), if proved with compatible quantifiers, would recover the missing absolute step. Neither follows from conflict independence, pair moments, transitivity, polynomial support, or induced-graph reasoning.

## 5. Stopping line

```text
exact child W/Phi/rho formulas                         proved (locked input)
MIDEC => AATSD                                        proved by normalization
source-local incidence charge for arbitrary weights   formally obstructed
actual d>=6 AATSD                                     unresolved
actual d>=6 RATSD / low-density terminality            unresolved
```

No HPRN, APOH, WRAD, literal representative-length, routing, congestion, spectral-gap, mixing, or Terminal inference is made.
