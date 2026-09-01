# M240 checkpoint

Status: source-lock reconstruction in progress.

The controlling ledger entries have been located.  Accepted inputs presently
used are exactly:

- M214/M218: a complete rank-five-to-six finite contour schedule;
- M220/M223: literal carrier/boundary identities plus a counterexample to the
  compact late-ancestor/direct-run key;
- M225/M228: a complete but nearly full-contour rank-six-to-seven table;
- M231/M234: the finite route-normal `Z_2` quotient and its literal-word-kernel
  theorem;
- M236/M237: an unchanged complete next-rank replay.

No all-rank inference has been made.

## Exact symbolic source/target relation (fixed before checks)

Let `d>=5`; let `T` be a tree on `[d]`, rooted at the leaf `d`, with
`{1,d}` its root edge; set `T^+=T union {{1,d+1}}`.  Write

```text
pi_d=(2d-3,2d-2,1,2,...,2d-4),
i=2v-3,                 2<=v<=d-1,
N=F_d(T,s_i pi_d) (0,d)(0,d),
A=F_(d+1)(T^+,s_i pi_(d+1)).                       (C.1)
```

Here `F_r` is the literal plus-mirror DPS closure: for boundary label `j`,
its factor is the transposition between the first black endpoint of `j` and
the black endpoint created by the distance-three closure of `j` (or the root
white vertex when no such black endpoint is created), with the repository's
zero-based physical labels.  Thus (C.1), not merely product equality, is the
source/target word relation to be proved.

Routes act chronologically from left to right by

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).          (C.2)
```

Let `P(v)=(v,p(v),...,1)`, let `lambda` say that an internal path vertex is
larger than `v`, let `alpha` say that two consecutive internal path entries
ascend, and for `0<=t<L=d-v-1` put

```text
c_t=1[p(v+t+1)=v],
epsilon_0=-1 if c_0=1 else +1,
epsilon_t=-1 if c_t=1 else -epsilon_(t-1),
Q=prod_(t=0)^(L-1)
      R_(2(v+t)-2)^epsilon_t R_(2(v+t)-1)^epsilon_t,
B_d=R_(2d-4)^-1 R_(2d-3) R_(2d-2)^-1
    R_(2d-3)^-1 R_(2d-4)^-1.                       (C.3)
```

The all-rank target is exactly

```text
lambda OR alpha  => N=A,
NOT(lambda OR alpha)
  => act(N,Q B_d Q^-1)=A.                           (C.4)
```

Because action is chronological, the open implication is equivalently the
following factor-level carrier relation:

```text
act(N,Q) and act(A,Q) agree outside positions
p,...,p+3, p=2d-4, and on those positions are

act(N,Q)[p:p+4]=((xy),(zx),(zy),(z n)),
act(A,Q)[p:p+4]=((x n),(zy),(zy),(zx))               (C.5)
```

for four distinct physical symbols `x,y,z,n=d`.  Formula (C.5), including
the claim that no outside position changes, is the exact symbolic DPS
contour lemma still to be derived.  It is stronger and more local than merely
checking (C.4) at a rank.

## First nontrivial identity (proved algebraically before checks)

For arbitrary distinct `x,y,z,n`, five literal applications of (C.2) give

```text
(xy,zx,zy,zn)
 ->(zy,xy,zy,zn)          by R_p^-1
 ->(zy,zy,zx,zn)          by R_(p+1)
 ->(zy,zy,xn,zx)          by R_(p+2)^-1
 ->(zy,xn,zy,zx)          by R_(p+1)^-1
 ->(xn,zy,zy,zx)          by R_p^-1.                 (C.6)
```

Hence `B_d` proves (C.5) once the all-rank contour statement supplies its
four-factor hypotheses.  This calculation is unconditional.  No endpoint or
finite-rank check has been run in M240.

Next is an algebraic derivation of (C.5), or its first symbolic failure,
directly from boundary trace/closure.
