# M03 checkpoint

Date: 2026-08-11  
Commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`

Convention: `(pq)(x)=p(q(x))`; words are `t_1...t_m`.  All gaps are
Poincare constants for the displayed normalization.

## Status

**M02 audit: ACCEPTED.**  The macro mass

```text
W_m(alpha)=m! product_B C(|B|,k_B)/k_B!
```

includes color interleavings exactly.  The full `r=3,4,5` stationary-flow
projection formula, the common-core square formula, the class count

```text
D_N=(3N^2+N-12)/2<=4M,
```

and

```text
E_barK >= c_sq E_S,
c_sq=M/[2|R_m|(m-2)D_N]>=1/[24(m-2)]
```

all survive exact checks in `S_3,m=4`, `S_4,m=4`, and `S_4,m=6`.
`S` and aligned `B` are connected in all three cases, and the frozen
qualitative proofs handle `m=4` as a whole-word aligned window.

## New dense projection theorem

Let `Pi` be the stationary-flow projection of `S` onto the exact labeled
support partition, with stationary mass `nu(P)=E_P(m)/|Omega(N,m)|`.  Put
`M=binom(N,2)`.  Using the frozen M12 target-wise child-mass estimate and
fixed-slot square injection, I proved:

> If `N>=3`, `m` is even, and `m-2>=4M log(2N)`, then every cut of the
> partition state space has conductance at least `3/(16M^2)`, and
> `gap(Pi)>=9/(512M^4)`.

The proof roots all labeled partitions at the full-support partition using
the M12 parent map.  Each child subtree has mass at most `4/3` times its top
mass, the root has mass at least `3/4`, and every child-to-parent `S` edge has
probability at least `1/(4M^2)`.  Decomposing an arbitrary set into induced
tree components accounts for its full stationary mass and boundary flow.
There is no path routing or repeated-edge hub.

This is stronger than the M12 component-threshold theorem.  Bounds for the
`N-2` nested sets `{c<=c_0}` do not control conductance over arbitrary sets:
an arbitrary set can split one layer or form a nonmonotone union, and no
rearrangement theorem is available.

## Exact fixed-partition restriction

For a fixed partition with nontrivial block sizes `v_i`, let
`E_i=binom(v_i,2)`, and write its total surplus as an allocation
`g_1+...+g_q=G`.  With

```text
a_v(g)=C(v,2(v-1)+2g)/[2(v-1)+2g]!,
rho_v(g)=a_v(g-1)/a_v(g),
```

the conditional law and every off-diagonal restricted transition are

```text
nu_P(g) proportional to product_i a_{v_i}(g_i),
S_P(g,g-e_i_unit+e_j_unit)
 =E_i E_j rho_{v_i}(g_i)/[M m(m-1)].
```

Thus the restriction is an exact zero-range allocation chain.  Comparing
directly to the uniform-destination complete-graph zero-range generator

```text
L_Z=(1/q)sum_{i,j}rho_{v_i}(g_i)[f(g-e_i+e_j)-f(g)]
```

with the same stationary law gives

```text
gap(S_P)>=q gap(Z_P)/[M m(m-1)].
```

Boudou--Caputo--Dai Pra--Posta Theorem 4.2, generator (4.2), condition
(4.11), then gives `gap(Z_P)>=delta_P` if

```text
delta_P=min_i inf_g [rho_{v_i}(g+1)-rho_{v_i}(g)]>0.
```

M12's audited deduction from Dubrovin--Yang--Zagier Proposition 1 proves the
useful unconditional action-rate bound `rho_v(g)>=12/v^3`.  It controls the
first increment and every nonzero rate, but not later rate differences.

The exact finite audit has `rho_v(g+1)>rho_v(g)` through `v<=5,g<=5`.
This is empirical only.  Gaudilliere--Reygner's ultra-log-concavity shortcut
is already refuted: at `v=4,g=1`,

```text
rho_4(1)=16/13, rho_4(2)=195/82,
rho_4(2)-2rho_4(1)=-89/1066<0.
```

## Current exact frontier

**HURWITZ-RATE-CURVATURE.**  Prove universal `c_0>0,A<infinity` such that,
with `rho_v(0)=0`,

```text
rho_v(g+1)-rho_v(g)>=c_0(v+g+1)^(-A)
```

for every `v>=2,g>=0`; or replace it by a comparably quantitative direct
Poincare theorem for the exact allocation chain.  This would close the
fixed-partition restrictions and hence the dense `S` gap by JSTV, but not the
sparse regime or the full word-fiber gap.

Full argument, literature hypotheses, calibration, and reproduction commands
are in `proof.md` and `report.md`.

