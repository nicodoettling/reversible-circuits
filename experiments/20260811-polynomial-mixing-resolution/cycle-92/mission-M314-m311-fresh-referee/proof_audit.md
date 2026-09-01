# M314 independent QBD/QBP proof audit

Date: 2026-08-14 UTC

## Exact scope

Condition on accepted M307/M308 QTI_1: for odd `k>=3`, `m=k-1`,
`1<=u<k/2`, and `2<=ell<=3k-2`, positive masses `x_c,y_d` have the same
total and

```text
P_(k,ell)(u)=sum_(c,d) pi_cd (Xbar_c-Ybar_d).
```

Every response mean retains all `k` middle phases.  This is only the
auxiliary channel-one all-middle coefficient, not the global identity bridge
or local heat-bath chain.

## Staircase and support bound

Let `I_c=(A_(c-1),A_c]`, `J_d=(B_(d-1),B_d]`, and let the distinct sorted
union of their endpoints be `0=t_0<...<t_s=mu`.  Each interval
`(t_(r-1),t_r]` lies in one unique pair `(I_c,J_d)` and has mass `pi_cd`.
Conversely, an intersection of two such half-open consecutive intervals has
no cumulative endpoint in its interior, so each positive transport cell is
exactly one of these segments.  Passing a breakpoint increments `c`, `d`, or
both, hence the support is a coordinatewise monotone staircase.

There are at most `2(m-1)+2=2m` distinct endpoints, hence at most
`2m-1=2(k-1)-1` supported cells.  Coincident endpoints merely make a diagonal
step and do not create, duplicate, or omit a cell.

## Rung orientation

For rung `h=min(c,d)`, if `c>d` then positive overlap gives

```text
A_d <= A_(c-1) < B_d,
```

so `R_h=A_h-B_h<0`.  If `c<d`, the symmetric inequalities give
`B_c<=B_(d-1)<A_c`, so `R_h>0`.  Therefore the sign fixes every existing
off-diagonal rung direction, while `R_h=0` forbids an off-diagonal rung-h
cell.  No false converse is needed.

## Sign-block identity

With `M_h=max(A_h,B_h)`, the half-open conventions give exactly

```text
min(c(t),d(t))>=a  iff  t>M_(a-1),
min(c(t),d(t))<=b  iff  t<=M_b.
```

Thus cells with `a<=min(c,d)<=b` occupy `(M_(a-1),M_b]`.  Each `M_h` is an
actual cumulative endpoint, so the interval never slices a cell.  The unique
maximal constant-sign runs of `R_h`, including every zero run and terminal
`R_m=0`, consequently form a disjoint, exhaustive partition.  Grouping QTI_1
over it proves exactly

```text
P_(k,ell)(u)=sum_q C_q(k,u,ell).                 (QBD_1)
```

This is an all-rank rearrangement identity, not a positivity theorem.

## QBP sufficiency

The predeclared QBP_1 is `C_q>=0` for every maximal sign block.  QBD_1 makes
`QBP_1 => P_(k,ell)(u)>=0` immediate.  No converse, cellwise sign, alternate
grouping, or downstream result follows.  The derivation is valid at the
minimal allowed odd rank and at coincident/zero cumulative differences; the
main-chain exceptional cases are not implicated by this auxiliary model.

Verdict on the analytic claims: **proved exactly at their stated scope**.
