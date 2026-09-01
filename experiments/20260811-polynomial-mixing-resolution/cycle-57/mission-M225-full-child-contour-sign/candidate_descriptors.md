# M225 predeclared child-contour candidates

Date: 2026-08-13 UTC. **SOURCE-ORDER ASSERTION:** this file is frozen before
any M225 `d=6 -> 7` endpoint replay.  Exactly two nested candidates are
defined; no third refinement is permitted.

## 1. Common setup

Let `T` be a tree on `[d]`, rooted at leaf `d` adjacent to attachment vertex
1. For an ordinary odd edit `i=2v-3`, `2<=v<=d-1`, let

```text
P(v)=(v,p(v),p^2(v),...,1)
```

be the stopped parent path. Put `L=d-v-1` and define the ordered full
larger-child bit vector

```text
c_t=1 iff p(v+t+1)=v,       0<=t<L.                   (1.1)
```

Thus unlike M220's initial-run statistic, `(c_0,...,c_(L-1))` retains every
larger old nonroot label attached directly below `v`, including a child after
an earlier gap.

Define signs by the deterministic automaton

```text
epsilon_0 = -1 if c_0=1, else +1;

epsilon_t = -1              if c_t=1,
epsilon_t = -epsilon_(t-1)  if c_t=0,       t>=1.     (1.2)
```

When the child vector is an initial run of `r` ones followed only by zeros,
(1.2) gives M220's exact signs: inverse on the first `r` generator pairs,
then alternating signs beginning positive. In the M220 witness, the vector
changes from `(0,0,0)` to `(0,0,1)`, so (1.2) changes only the final sign.

Put

```text
Q_A(d,v,c)= product t=0,...,L-1 of
             R_(2(v+t)-2)^epsilon_t R_(2(v+t)-1)^epsilon_t,

B_d=R_(2d-4)^- R_(2d-3) R_(2d-2)^-
    R_(2d-3)^- R_(2d-4)^-,                           (1.3)

C_A=Q_A B_d Q_A^-1.
```

All products are chronological.

## 2. Symbolic carrier transport

For distinct symbols `x,y,z,n`, direct signed-Hurwitz action gives

```text
B_p[(xy),(zx),(zy),(zn)]=[(xn),(zy),(zy),(zx)].       (2.1)
```

Conjugating (2.1) by any chronological word `Q` proves

```text
(Q B_p Q^-1)[Q X]=Q Y                                (2.2)
```

whenever `B_p X=Y`. Therefore each generator pair in (1.3) is a transport
stage that moves the four-factor carrier window across one doubled DPS slot;
the sign records on which side the off-contour child incidence is met.

The boundary identities remain

```text
(R_p^-)^2[a,b,a]=[b,aba,a],
R_p^-[a,b]=[aba,a].                                  (2.3)
```

They define the two final-edit words below independently of A/B.

## 3. Candidate A — full larger-child vector

The Candidate-A descriptor for an ordinary odd edit is

```text
D_A(T,v)=(v, late(v), c(T,v), forward_exception(v)), (3.1)

late(v)=1 iff an internal vertex of P(v) is greater than v,

forward_exception(v)=1 iff v>=4 and
P(v)=(v,2,3,...,v-1,1).
```

Its assigned word is

```text
late(v)=1 or forward_exception(v)=1 -> identity;
otherwise                            -> C_A(d,v,c).    (3.2)
```

Candidate A differs from M220 only by retaining all bits in (1.1) and using
the sign automaton (1.2). It deliberately leaves M220's single forward-path
exception rule unchanged, making it separately falsifiable.

## 4. Candidate B — full stopped-contour incidence word

Candidate B strictly refines A. Write

```text
P(v)=(u_0=v,u_1,...,u_s=1).
```

For each path vertex `u_j`, record the increasing list

```text
O_j=sorted{w in [d-1] : p(w)=u_j and w not in P(v)}. (4.1)
```

The full descriptor is

```text
D_B(T,v)=(D_A(T,v), P(v), O_0,O_1,...,O_s).          (4.2)
```

This includes every direct larger child from A, the whole attachment path,
and every off-path child incidence along that contour. In particular it
distinguishes the M220 star from the `{2,5}` witness.

Let the internal contour word be

```text
I(v)=(u_1,...,u_(s-1)).
```

Predeclare the ascent flag

```text
ascent(v)=1 iff some consecutive entries of I(v) satisfy u_j<u_(j+1).
                                                               (4.3)
```

Candidate B assigns

```text
late(v)=1 or ascent(v)=1 -> identity;
otherwise                 -> C_A(d,v,c).              (4.4)
```

At `d=5`, (4.3) specializes exactly to M214's exceptional path
`(4,2,3,1)`: its internal word `(2,3)` has an ascent. At `d=6,v=5`, (4.3)
predeclares a uniform extension to every stopped path whose internal contour
is not decreasing at every adjacent step. This replaces, rather than tunes,
the one forward-chain exception.

Formula (4.4) is still a single conjugate-of-carrier word. The nested contour
data certify which local closure regime is asserted; the ordered full child
vector drives every sign in its transport conjugator.

## 5. Common non-odd edits

Both candidates assign

```text
internal even i<=2d-6  -> identity;
i=2d-4                 -> (R_(2d-5)^-)^2;
i=2d-3                 -> R_(2d-2)^-.                 (5.1)
```

## 6. Decision rules and strict boundary

Test Candidate A first over all 1,125 rows. If any row fails, retain its full
failure table and then test the already frozen Candidate B. Candidate B is
accepted as an exact finite theorem only if all 1,125 literal replays pass.

Failure of either displayed word does not imply that no alternative braid
exists. Success proves only the complete finite `d=6 -> 7` table and the
recorded finite maximum correction length. Neither outcome proves all-rank
induction, every-color routing, voltage-corrected total length, spectral gap,
mixing, or Terminal.

