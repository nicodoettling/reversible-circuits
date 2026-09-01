# M322 Independent Proof Audit of M318

Date: 2026-08-14 UTC.

Verdict: **ACCEPT at the frozen identity-and-obstruction scope.**

## 1. Staircase endpoints and truncated marginals

The half-open quantile intervals `I_c=(A_(c-1),A_c]` and
`J_d=(B_(d-1),B_d]` both partition `(0,mu_k]`. Their distinct cumulative
endpoints give

```text
0=t_0<t_1<...<t_s=mu_k.
```

Each `(t_(r-1),t_r]` lies in one unique supported cell `(c_r,d_r)` and
has mass `omega_r=t_r-t_(r-1)`. Therefore, at `T=t_j`,

```text
sum_c |I_c intersect (0,T]|=T
 =sum_d |J_d intersect (0,T]|,
Psi(T)=sum_(r<=j) omega_r(Xbar_(c_r)-Ybar_(d_r))
      =sum_c lambda_c(T)Xbar_c-sum_d rho_d(T)Ybar_d.
```

All `Xbar,Ybar` already contain every middle phase.

For the maximal sign block `H_q=[a_q,b_q]`, M311's exact interval
characterization puts its cells on
`(M_(a_q-1),M_(b_q)]`. Hence at
`T_q=M_(b_q)`,

```text
Psi(T_q)=Phi_(b_q)=sum_(p<=q) C_p.
```

The last block has `b_Q=m=k-1` and `M_m=mu_k`, so the terminal prefix is
the complete aggregate `P_(k,ell)(u)).

## 2. Discrete Abel coboundary

For every endpoint `t_j`, summation by parts gives

```text
Psi(t_j)=t_j Z_j-sum_(r<j)t_r(Z_(r+1)-Z_r).
```

Expansion assigns coefficients `t_1`, `t_r-t_(r-1)`, and
`t_j-t_(j-1)` to the first, interior, and final `Z` values, respectively,
so the signs and endpoint are exact.

At a breakpoint the next cell increments `c`, `d`, or both. Thus

```text
Z_(r+1)-Z_r
 =(Xbar_(c_(r+1))-Xbar_(c_r))
  -(Ybar_(d_(r+1))-Ybar_(d_r))
```

covers horizontal, vertical, and coincident-endpoint steps without assigning
a sign to any exchange.

## 3. Causal compensation equivalence

Write `C_q=C_q^+-C_q^-`. If nonnegative flows from earlier positive blocks
meet every later negative demand and leave `L_p>=0`, then any prefix equals
unused supply inside the prefix plus supply reserved for later demands, so it
is nonnegative.

Conversely, process blocks left to right. At a negative block,
`Psi_q>=0` says accumulated earlier supply covers its entire demand.
Greedily assigning that supply constructs the causal flow. Unused terminal
supply gives `L_p`. The exact inventory identity is

```text
C_q=L_q+sum_(r>q)pi_(q,r)-sum_(p<q)pi_(p,q).
```

All internal flows cancel on summation, yielding exactly

```text
P_(k,ell)(u)=Psi_Q=sum_q L_q>=0.
```

This flow is an equivalent scalar inventory reformulation of canonical prefix
nonnegativity, not an independent proof that GQAC holds.

## 4. Formal obstruction and actual stopping line

Frozen coefficient geometry fixes masses, staircase cells, rungs, and blocks
but does not sign the owner-response values. The supported-cell bipartite
graph is a forest: each horizontal or vertical staircase step adds one new
coordinate vertex, while a coincident step starts a new component. Thus
arbitrary supported cell values, including M318's first-block-negative
assignment, can be represented as `D_cd=Xbar_c-Ybar_d`; a common shift on
each component makes both potential families nonnegative. A still simpler
formal witness is `Xbar_c=0,Ybar_d=1` everywhere.

Accordingly the coefficient identities alone allow a negative first prefix.
For the literal owner law, each truncated prefix divided by `T` is a
difference of two normalized positive owner-response means, but statewise
nonnegativity does not order those means. GQAC is therefore the first
actual-owner-specific inequality and remains unresolved. The formal model is
not an actual-owner counterexample.

No cellwise sign, maximal-block sign, fixed-middle sign, MON/FOSD, PSD, or
one-direction Abel monotonicity is used or revived.

## 5. Sole frozen k=13 guard

No code was executed in this audit. Formula and metadata inspection verifies:

- the wrapper SHA-gates M311's source at
  `703f4d8db29c60ee3f1d3f1cd7418aa11782f9a309a310c2a259d8d30d09eb94`;
- its only source substitutions are `K=11 -> 13` and
  `30 -> 36` admissible lags;
- the frozen result has six middle-cut classes, thirteen retained phases,
  36 lags, and 216 rows;
- three canonical blocks give 648 prefixes, with zero negative prefixes and
  zero rows containing one;
- all 216 complete aggregates are positive, with zero zero or negative;
- QTI, QBD, and reflection fields are exactly true;
- the exact minimum prefix is terminal at `(u,ell,block)=(2,12,2)`, and the
  same minimum aggregate occurs at `(2,12)` and reflected `(2,27)`.

These are finite facts at one rank and imply no trend or all-rank theorem.

## 6. Numbered objections and scope

Material objections: **none**.

Nonmaterial objection 1: the reproduction commands in M318's
`guard_report.md` and `run_manifest.md` name the nonexistent relative
source
`../../cycle-90/mission-M311-hahn-quantile-block-divergence/qbp_k11.py`.
The frozen JSON records the actual authenticated source as
`cycle-91/mission-M311-multicell-hahn-quantile/qbp_k11.py`; from M318's
directory the correct relative path is
`../../cycle-91/mission-M311-multicell-hahn-quantile/qbp_k11.py`.
The source digest matches, so this is a reproducibility-documentation error
only and does not affect the frozen exact result.

GQAC and MCLP remain unresolved. No GOCI, OCI, CP, MS, FCL1, gap, mixing, or
Terminal conclusion follows.
