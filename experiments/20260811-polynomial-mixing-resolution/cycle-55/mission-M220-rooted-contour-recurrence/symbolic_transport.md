# M220 symbolic one-leaf transport identities

Date: 2026-08-13 UTC.  This note was written before the `d=6 -> 7` finite
check.  Proved formal identities and the conjectural recurrence are separated.

## 1. Setup

Let the old identity word have length `2d-2`; after adjoining root leaf
`d+1` at attachment vertex 1, the word has length `2d`.  Factors and Hurwitz
generators are indexed from 1.  All actions below are chronological and all
letters are transpositions, hence involutions:

```text
R_j(a,b)    = (b,bab),
R_j^-1(a,b) = (aba,a).
```

The canonical rooted orders and endpoints are

```text
pi_d       =(2d-3,2d-2 | 1,2 | ... | 2d-5,2d-4),
pi_(d+1)   =(2d-1,2d   | 1,2 | ... | 2d-3,2d-2),

N_(T,i)=F_d(T,s_i pi_d)(0,d)(0,d),
A_(T,i)=F_(d+1)(T+{1,d+1},s_i pi_(d+1)).
```

Direct boundary closure, before any edit, gives the exact extension identity

```text
F_(d+1)(T+{1,d+1},pi_(d+1))=F_d(T,pi_d)(0,d)^2.       (1.1)
```

The issue is that swapping boundary values before closure can change the
distance-three pairings and hence need not commute with (1.1).

## 2. Proved formal four-factor carrier

Put

```text
B_p=R_p^- R_(p+1) R_(p+2)^- R_(p+1)^- R_p^-.
```

For four distinct symbols `x,y,z,n`, literal signed-Hurwitz calculation gives

```text
B_p [(xy),(zx),(zy),(zn)]
    =[(xn),(zy),(zy),(zx)].                            (2.1)
```

Indeed, the five intermediate four-tuples are

```text
(xy,zx,zy,zn)
(zy,xy,zy,zn)
(zy,zy,zx,zn)
(zy,zy,xn,zx)
(zy,xn,zy,zx)
(xn,zy,zy,zx).
```

For one-leaf extension, the carrier sits at

```text
p=2d-4,
B_d=R_(2d-4)^- R_(2d-3) R_(2d-2)^-
    R_(2d-3)^- R_(2d-4)^-.                            (2.2)
```

M214's standard edit-5 word is exactly `B_5`.

## 3. Proved formal boundary-edit identities

For distinct `x,y,z`, put `a=(xy)`, `b=(zx)`, and `c=aba=(zy)`.
Two inverse moves at one position give

```text
(R_p^-)^2 [a,b,a]=[b,c,a].                            (3.1)
```

For any adjacent transpositions `a,b`, one inverse move gives

```text
R_p^- [a,b]=[aba,a].                                  (3.2)
```

These are exactly the formal shapes behind M214's last two corrections.
They motivate the all-rank boundary schedules

```text
i=2d-4: (R_(2d-5)^-)^2,
i=2d-3: R_(2d-2)^-.                                  (3.3)
```

Equations (2.1), (3.1), and (3.2) are unconditional word identities.  Their
application to every DPS endpoint still requires the claimed local factor
shapes, which the recurrence below proposes and the finite check will test.

## 4. Rank-five conjugator pattern

Every nontrivial odd-edit correction in M214 has the form

```text
C_(5,v,r)=Q_(5,v,r) B_5 Q_(5,v,r)^-1.                (4.1)
```

For `v=2,3,4`, let `L=5-v-1`.  M214's five nontrivial conjugators are exactly

```text
Q_(5,v,r)=product over t=0,...,L-1 of
           R_(2(v+t)-2)^eps_t R_(2(v+t)-1)^eps_t,

eps_t = -1 if t<r;
eps_t = (-1)^(t-r) if t>=r.                           (4.2)
```

Thus the first `r` generator pairs are inverse; after the direct-child run,
the signs alternate beginning with positive.  Formula (4.2) is an exact
re-expression of the accepted rank-five table, not yet an all-rank theorem.

## 5. Candidate rooted-contour recurrence (**CONJECTURED BEFORE CHECK**)

For an ordinary odd edit `i=2v-3`, `2<=v<=d-1`, root `T` at leaf `d` and
stop the parent path at attachment vertex 1.  Define

```text
P_T(v)=(v,p(v),...,1),
late_T(v)=1 iff an internal path vertex is greater than v,
run_T(v)=max{r: p(v+k)=v for every 1<=k<=r, v+k<=d-1}.
```

To extend M214's one exceptional class, define the forward-chain flag

```text
exception_T(v)=1 iff v>=4 and
P_T(v)=(v,2,3,...,v-1,1).                             (5.1)
```

This is the literal rank-stable extension of M214's path `(4,2,3,1)`; no
claim of uniqueness is built into the definition.

The proposed correction table is

```text
ordinary odd i=2v-3:
  late_T(v)=1 or exception_T(v)=1 -> identity;
  otherwise                         -> Q_(d,v,run) B_d Q_(d,v,run)^-1,

where Q_(d,v,r) is (4.2) with L=d-v-1;

internal even i<=2d-6               -> identity;
cross-boundary i=2d-4               -> (R_(2d-5)^-)^2;
old-high-pair i=2d-3                -> R_(2d-2)^-.     (5.2)
```

At `d=5`, (5.2) reproduces every accepted M214 word and class exactly.
At larger rank it is **conjectured**.  Its value is that it is explicit and
falsifiable without route search: all tree dependence is the declared
`(v,late,run,exception)` key, and every correction word is a closed formula.

## 6. Planned falsification boundary

The next computation will generate exactly the 125 trees on `[6]` whose root
6 is a leaf adjacent to 1, and replay (5.2) for edits 1 through 9 after
extension to `[7]`.  It will neither enumerate a Hurwitz quotient nor search
for alternative routes.

One failed replay refutes (5.2).  To show that the proposed finite key itself
does not even determine this schedule behavior, the checker will additionally
seek the first same-key pair in which one row satisfies the declared common
word and another does not.  Such a pair rejects only (5.1)--(5.2); it does not
prove that no richer tree descriptor or different common braid exists.

