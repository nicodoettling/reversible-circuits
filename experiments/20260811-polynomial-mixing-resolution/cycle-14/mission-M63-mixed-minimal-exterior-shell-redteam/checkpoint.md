# M63 halfway checkpoint: mixed halos leak polynomially

## Setup

Fix a labeled path tree `T_N`, its original leaf `v` with neighbor `u`, and
the other original leaf `w`.  Let `Core=Del_{v,w}`, choose any nonempty proper
core set `B`, and put

```text
A={x in F_N(T_N):Core(x) in B},
Z=Del_v(A).
```

Core membership is constant on every `v`-deletion cell.  Hence every
`z in Z` has the canonical hub `z(v,u)^2 in A`, and the M49 fiber bound gives

```text
|A|<=Lambda_N |Z|,
Lambda_N=binom(2N-2,2)(N-1)^2.                      (C.1)
```

For each `a!=u`, the same final H3 fiber contains

```text
z(v,a)^2.
```

This word is in `F_N`, but its join tree is `T_N-v` with leaf `v` attached
at `a`, so it is outside the original path-sector `A`.  There are exactly
`N-2` such outcomes, each with probability

```text
1/[6(m-2)D_N],  D_N=(3N^2+N-12)/2.                 (C.2)
```

## Candidate 1: the smallest specified-target halo

Fix one transposition `s` avoiding `v` and define

```text
E^(1)={z s^2:z in Z},  C^(1)=A union E^(1).
```

The map `z -> z s^2` is injective, every target omits `v`, and

```text
|E^(1)|=|Z|,
pi(C^(1))=(|A|+|Z|)/|Omega|.                        (C.3)
```

This is the smallest halo absorbing the one specified M60 target from each
hub.  Equations (C.1)--(C.3) give

```text
Q(C^(1),(C^(1))^c)/pi(C^(1))
 >=(N-2)/[6(m-2)D_N(Lambda_N+1)]
 >=1/(144N^6)                                       (C.4)
```

for `N>=5`.  Thus this literal mixed cut is not Terminal B.

The exact N=5 balanced-core audit has

```text
|A|=3904, |Z|=|E^(1)|=87, |C^(1)|=3991,
pi(C^(1))=3991/1770940,
```

and complete exact escape

```text
17932842729275693759/44514228823515360000
=0.4028564169981168...,
```

split as `0.102784...` from H3, `0.141089...` from H4, and `0.158984...`
from H5.  The universal lower bound there is `1/183192`.

## Candidate 2: every one-step exterior neighbor

Let

```text
E^(all)={y in F_N^c:K(x,y)>0 for some x in A}.
```

This absorbs every exterior H3/H4/H5 target from all of `A`.  Its exact mass
is `( |A|+|E^(all)| )/|Omega|`, while literal outdegree gives

```text
|E^(all)|
 <=|A| D_out,
D_out=sum_(r=3)^5 (m-r+1)M^r<=3mM^5.               (C.5)
```

The alternate full-support targets (C.2) are not exterior and remain outside
the cut.  Therefore

```text
Q/pi(C^(all))
 >=(N-2)/[6(m-2)D_N Lambda_N(1+D_out)]
 >=1/(672N^17).                                     (C.6)
```

The same bound holds for every intermediate halo
`E^(1) subseteq E subseteq E^(all)`.

## Candidate 3: the nonlocal fixed-missing-label halo

Let

```text
A_v={identity words having no factor incident to v},
C^(v)=A union A_v.
```

This exterior set is not a one-step shell.  Its stationary mass is exactly

```text
pi(C^(v))=[|A|+|Omega(N-1,m)|]/|Omega(N,m)|.         (C.7)
```

The inherited marked-square incidence gives an `A_v`-conditional square
certificate with probability at least `1/binom(N-1,2)`.  Refreshing it to a
square `(v,a)^2` has `N-1` choices.  At most `a=u` can enter the fixed path
sector `A`; every one of the other `N-2` outcomes leaves both `A_v` and `A`.
Thus

```text
Q(C^(v),(C^(v))^c)/pi(C^(v))
 >=min{
   (N-2)/[6(m-2)D_N Lambda_N],
   1/[3(m-2)(N-1)D_N]
 }
 >=1/(96N^6).                                       (C.8)
```

At N=5, `|Omega(4,8)|=140160`, so this mixed cut has exact size
`3904+140160=144064` out of `1770940`.

## Current gap

The three halos span one specified target per cell, every one-step exterior
neighbor, and the full fixed-missing-label phase.  The next possible cut must
use a recursively closed or multi-label exterior set whose mass grows faster
than one-step polynomial outdegree while its own boundary is correlated with
the internal core cut.  No such family is presently proved to have small
flow.

