# A superpolynomial separator for the weighted leaf-rotation chain

Date: 2026-08-11.  This note concerns rooted plane trees, not the full
identity-word chain.  A tree has `r` edges, and

```text
omega(t)=product_v 1/d_v(t)!,
Z_r=(r+1)^(r-1)/r!,
pi_r(t)=omega(t)/Z_r.
```

For `r>=2`, the exact M35 leaf rotation replaces a leaf child followed by
one sibling subtree by a unary child containing that subtree.  In Dyck
notation it is `UD P <-> U P D`, where `P` is one primitive excursion.  Let
`L_r` be the reversible chain retaining these edges with the exact rates

```text
c_r d_i in the forward direction,  c_r in reverse,
c_r=2/[3r(r-1)],
```

and putting unused probability on the diagonal.

## Theorem

Put, for `r>=3`,

```text
n=r-1,
D_r=2+ceil(log_2 n),
b_r=(r+1)(e/D_r)^D_r.
```

There is a set `A_r` of plane trees such that every `L_r` edge from `A_r`
to its complement has its other endpoint in

```text
B_r={t:max_v d_v(t)>=D_r},
```

and

```text
pi_r(B_r) <= b_r,
pi_r(A_r) >= e^(-1)-b_r,
pi_r(A_r^c) >= 3/(8e^2)-b_r.                       (1)
```

Consequently, once the two denominators in (1) are positive,

```text
gap(L_r)
 <= b_r/[(e^(-1)-b_r)(3/(8e^2)-b_r)].              (2)
```

In particular, for every fixed `C>0`,

```text
r^C gap(L_r) -> 0.                                  (3)
```

Thus every polynomial-congestion comparison from the M41 weighted
leaf-replanting chain `Y_r` to `L_r` is false.  This does not imply a slow
gap for the full parking projection: its non-leaf rank-two moves are not
edges of `L_r` and may cross this cut.

## 1. Root compositions and reversible pebbles

Let the root children of a plane tree `t`, from left to right, have branch
sizes

```text
a(t)=(a_1,...,a_k),
```

where a branch size includes its edge from the root.  Thus every `a_i` is
positive, their sum is `r`, and `k=d_root(t)`.  Define the set of proper
prefix sums

```text
S(t)={a_1,a_1+a_2,...,a_1+...+a_(k-1)} subset {1,...,r-1}.   (4)
```

A leaf rotation below the root does not change any root branch size, so it
fixes `S(t)`.  A leaf rotation at the root replaces two consecutive branch
sizes

```text
(1,q) <-> (q+1).
```

If `s` is the sum of the preceding branch sizes, this toggles `s+1` in
`S(t)`, and the predecessor `s` is either zero or is already in `S(t)`.
Therefore (4) maps every leaf-rotation edge into the reversible-pebble
graph on the directed path with vertices `1,...,n=r-1`:

```text
toggle pebble i only if i=1 or pebble i-1 is present.        (5)
```

In the induced rotation graph on `B_r^c`, the root has at most `D_r-1`
children.  Hence every projected configuration has at most

```text
p=D_r-2=ceil(log_2 n)                              (6)
```

pebbles.

The empty configuration and the singleton `{n}` are in different
components of the graph (5) restricted to at most `p` pebbles.  Indeed, a
path between them would be a persistent reversible pebbling of the
directed `n`-vertex path using `p` pebbles.  Komarath--Sarma--Sawlani,
arXiv:1604.05510, Theorem 12, identifies the persistent reversible pebbling
number of a directed tree with one plus the edge-ranking number of its
underlying tree.  The edge-ranking number of the `n`-vertex path is
`ceil(log_2 n)`: if `M(k)` is the maximum number of edges in a path ranked
with `k` colors, the highest color occurs at most once and splits the path
into two paths ranked with `k-1` colors, so

```text
M(k)<=1+2M(k-1)=2^k-1.
```

The matching upper bound follows by ranking a median edge highest and
recursing.  Thus persistent pebbling requires
`ceil(log_2 n)+1`, one more than (6).

Let `C_0` be the component of the empty configuration in the pebble graph
with cap `p`, and define

```text
A_r={t notin B_r:S(t) in C_0}.                       (7)
```

If an `L_r` edge starting in `A_r` also ends outside `B_r`, its projected
move is an edge of the capped pebble graph or is stationary, so its endpoint
is still in `A_r`.  Hence every edge leaving (7) enters `B_r`.

## 2. The two sides have constant mass

Every root-degree-one tree has `S(t)` empty.  Removing its root and root
edge leaves an arbitrary tree with `r-1` edges, so its exact mass is

```text
pi_r(d_root=1)=Z_(r-1)/Z_r
                  =(r/(r+1))^(r-1) >= e^(-1).       (8)
```

The last inequality follows from
`log(1-x)>=-x/(1-x)` with `x=1/(r+1)`.  Removing the exceptional set `B_r`
from (8) proves the first nontrivial lower bound in (1).

For the other side, take trees whose ordered root branch-size composition
is exactly

```text
(r-1,1)=(n,1).                                      (9)
```

Their prefix set is `{n}`, which is not in `C_0`.  The first child subtree
in (9) has `r-2` internal edges, the second child is a leaf, and the root
weight is `1/2!`.  Thus (9) has exact mass

```text
(1/2) Z_(r-2)/Z_r
 = r(r-1)^(r-2)/[2(r+1)^(r-1)]
 = [r/(2(r+1))] [(r-1)/(r+1)]^(r-2)
 >= 3/(8e^2).                                       (10)
```

For `r>=3`, the first factor is at least `3/8`.  For the second, use
`log(1-x)>=-x/(1-x)` with `x=2/(r+1)` to get an exponent greater than
`-2`.  Removing `B_r` from (10) gives the second lower bound in (1).

## 3. Separator mass and the gap

The M41 cycle-lemma/Vervaat argument identifies the maximum outdegree under
`pi_r` with the maximum occupancy when `r` independent balls are put
uniformly into `r+1` boxes.  A union bound and the binomial tail inequality
give, for every integer `D>=1`,

```text
pi_r(max_v d_v>=D)<=(r+1)(e/D)^D.                   (11)
```

Taking `D=D_r` proves the first line of (1).  Moreover,

```text
log b_r = log(r+1)+D_r(1-log D_r)
         =-Omega(log r log log r),                  (12)
```

so `b_r=o(r^-C)` for every fixed `C`.

By reversibility and the support property following (7),

```text
Q_L(A_r,A_r^c)=Q_L(A_r,B_r)=Q_L(B_r,A_r)<=pi_r(B_r).
```

Testing the Poincare quotient with the indicator of `A_r` gives (2), and
(1), (2), and (12) prove (3).

Finally, a polynomial flow comparison would give
`E_Y<=r^C E_L` for some fixed `C`.  Since M41 proves
`gap(Y_r)>=1/[16(r+1)^8]`, this would imply
`gap(L_r)>=1/[16r^C(r+1)^8]`, contradicting (3).  This rules out arbitrary
fractional polynomial-congestion flow, not only deterministic paths.

## 4. Calibration and scope

- `r=1` is the singleton convention and is outside the separator.
- At `r=2`, the two nominal root branches are indistinguishable leaves;
  the asymptotic separator begins at `r=3`.
- The two stationary-mass witnesses for the separator are the one-root-branch
  event, whose prefix configuration is empty, and the ordered root
  composition `(r-1,1)`, whose prefix configuration is `{r-1}`.  The latter
  is a branch of size `r-1` followed by a root leaf.
- Exact enumeration through `r=10` gives the minimum possible maximum
  degree on any rotation path between these endpoints as
  `2+ceil(log_2(r-1))`, matching the proof.  The computation is a bounded
  falsifier only.
- Stars have denominator `r!`, paths denominator `1`, and no comparison of
  these point masses is used in the stationary cut.
- The conclusion is for `L_r`.  The exact parking projection contains
  additional rank-two edges, and the original `{3,4,5}` identity chain has
  still more moves.  No Terminal-A or Terminal-B conclusion follows.
