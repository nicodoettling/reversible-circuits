# M337 frozen weighted actual-family RATSD/terminality candidate

Date: 2026-08-14 UTC

Status: frozen after the immutable source lock and before any computation.

## 1. Exact actual node

Fix `d>=6`, one actual M135 perfect matching, arbitrary nonzero weights
`lambda>=0`, and the universally quantified positive outer anchor. At a
compatible node `I`, retain the accepted actual signatures

```text
D_I(Q) subset H_I,
V=G_I(supp(lambda)),
W=lambda(V),
E={{Q,R} subset V:D_I(Q) intersection D_I(R)=empty},
Phi=sum_({Q,R} in E)lambda_Q lambda_R,
rho=2Phi/W^2.
```

The active set is

```text
A={P in V:deg_E(P)>0}.
```

For an active pivot `P`, use the whole actual child, never an induced graph:

```text
C(P)={Q in V:D_I(P) intersection D_I(Q) nonempty},
c(P)=lambda(C(P)),
T(P)=sum_({Q,R} subset C(P))lambda_Q lambda_R
     1[D_I(P) intersection D_I(Q) intersection D_I(R)=empty],
W'=c(P),
Phi'=T(P),
rho'=2T(P)/c(P)^2.                                 (1.1)
```

All weights are arbitrary nonnegative reals. The positive anchor, constants,
and exponents below are universal over every such actual weighted instance.

## 2. Frozen candidate: W-RATSD+HLDT

> **WEIGHT-DEPENDENT RELATIVE ACTIVE TRIPLE-SHADOW DESCENT WITH HEAVY
> LOW-DENSITY TERMINALITY (W-RATSD+HLDT).** There are universal constants
> `B_init,C_init,B_rel,B_low,C_log,C_fin` such that every nonzero weighted
> actual `d>=6` matching admits a positive anchor and a compatible initial
> tuple `I_0` satisfying
> ```text
> |I_0|<=d^B_init,
> W_0>=||lambda||_1/d^C_init.                       (2.1)
> ```
> At every selected nonterminal node:
>
> **High-density alternative.** If `rho>=d^(-B_low)`, an active pivot `P`
> exists whose whole child in `(1.1)` either
> ```text
> T(P)=0 and c(P)>=W/d^C_fin,                        (2.2)
> ```
> or is nonterminal and obeys
> ```text
> rho' <=(1-d^(-B_rel))rho,
> log(W/c(P))<=C_log log(d)(rho-rho').              (2.3)
> ```
>
> **Low-density terminality.** If
> `0<rho<d^(-B_low)`, an active pivot exists with
> ```text
> T(P)=0 and c(P)>=W/d^C_fin.                        (2.4)
> ```
>
> If `rho=0`, the current node is already terminal and no final pivot or
> weight loss is charged.

Clauses `(2.2)` and `(2.4)` explicitly control the final step. The
logarithmic loss clause is never silently omitted merely because the chosen
child is terminal.

## 3. Exact conditional stopping implication

Assume `(2.1)--(2.4)`. Every nonterminal descent step multiplies `rho` by at
most `1-d^(-B_rel)`. Since `rho<=1`, after at most

```text
N=ceil(B_low d^B_rel log d)                         (3.1)
```

such steps, either a terminal alternative has already occurred or the path
enters the low-density regime and `(2.4)` supplies the terminal pivot.

On the nonterminal descent steps, summing `(2.3)` telescopes:

```text
sum_t log(W_t/W_(t+1))
 <=C_log log(d) sum_t(rho_t-rho_(t+1))
 <=C_log log d.                                     (3.2)
```

The final terminal step loses at most `C_fin log d`, while `(2.1)` loses at
most `C_init log d` relative to the total weight. Hence

```text
W_final>=||lambda||_1/d^(C_init+C_log+C_fin).       (3.3)
```

The final whole child has `T(P)=0`, so its actual residual incompatibility
graph is edgeless. The total tuple length is at most
`d^B_init+N+1`, which is bounded by `d^B` for a universal `B` after enlarging
the exponent. Thus W-RATSD+HLDT would meet the quantitative whole-node
conclusion required by HPRN.

This is a **proved conditional implication only**. None of `(2.1)--(2.4)` is
asserted for the actual family, so HPRN and every consequence remain
unresolved pending proof and fresh audit.

## 4. Decision rule

Derive all exact pivot averages available from `(1.1)`. If they prove
`(2.2)--(2.4)` together with `(2.3)`, freeze a conditional proof route. If
they do not, isolate the first genuinely actual higher-orbital lemma, retaining
the whole `T(P)` and final-step weight bound. No graph replacement,
unweighted charge, polynomial-support premise, or rank-3 promotion is allowed.

No finite guard is presently authorized. It may be added only by an
append-only predeclared plan naming one formula after the analytic stop.

