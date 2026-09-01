# Full-parking leaf-count threshold anti-bottleneck

Frozen: 2026-08-11.  The convention is `(pq)(x)=p(q(x))`, and factor
tuples multiply left-to-right.  This note concerns only the nonlazy full
adjacent-rank-two stationary-flow projection `bar P_r` of M35.  It is not a
statement about the auxiliary leaf-only chain, and it is not a gap theorem
for `bar P_r` or for the original identity-word chain `K`.

## Theorem

Let `r>=2`, let

```text
J_r={d in N^r: sum_i d_i=r and sum_(i=0)^k d_i>=k+1
                     for 0<=k<r},
pi_r(d)=r!/[(r+1)^(r-1) product_(i=0)^(r-1) d_i!].
```

Append `d_r=0`, interpret `(d_0,...,d_r)` as the preorder outdegree
sequence of its plane tree, and put

```text
L(d)=#{0<=i<=r:d_i=0},
A_(r,ell)={d:L(d)<=ell}.
```

For every integer `ell` for which

```text
pi_r(A_(r,ell))>=1/4  and  pi_r(A_(r,ell)^c)>=1/4,
```

the exact stationary boundary flow satisfies

```text
Q_barP(A_(r,ell),A_(r,ell)^c)
   >=1/[60(r+1)(r-1)].                                (1)
```

Thus no balanced threshold in the literal number of plane-tree leaves is a
superpolynomial bottleneck for the full parking projection.

## Proof

### 1. Deterministic supply of leaf-increasing actual moves

For a rooted tree on `r+1` vertices let `n_k` be the number of vertices of
outdegree `k`.  Since `sum n_k=r+1` and `sum k n_k=r`,

```text
n_0=1+sum_(k>=2)(k-1)n_k.
```

Writing `L=n_0` and `U=n_1`, the number of vertices of outdegree at least
two is at most `L-1`, whence

```text
U>=r+2-2L.
```

After possibly excluding the root, the number `U_*` of nonroot unary
vertices therefore obeys

```text
U_*>=r+1-2L.                                         (2)
```

Every nonroot unary vertex `j`, with parent `i`, is the target of the M35
leaf rotation which turns `j` back into a leaf and restores its child as
the next sibling.  In degree coordinates this reverse transition is

```text
d -> d+e_i-e_j.
```

It increases `L` by one.  M35's accepted exact count gives its reverse rate

```text
c_r=2/[3r(r-1)].                                     (3)
```

Different unary vertices give different destination vectors (a coincidence
would force a two-cycle in the parent relation).  Hence every state with
`L=ell` has aggregate actual rate at least

```text
c_r(r+1-2ell)                                        (4)
```

from level `ell` to level `ell+1`, whenever the right side is positive.
All other `bar P_r` transitions are retained as nonnegative flow.

### 2. Exact stationary leaf law and unimodality

The cycle lemma identifies `pi_r` with the unique Lukasiewicz rotation of
the occupancy vector of `r` independent balls in `r+1` boxes.  `L` is
rotation invariant, so it has exactly the empty-box law.  With `n=r+1`
and `k=n-ell` occupied boxes,

```text
Pr(L=ell)=(n)_k S(r,k)/n^r,                           (5)
```

where `S(r,k)` is a Stirling number of the second kind.

For completeness, the Stirling polynomial
`P_r(x)=sum_k S(r,k)x^k` has only real nonpositive zeros.  This follows
inductively from `P_(r+1)=x(P_r+P'_r)`: the logarithmic derivative
interlaces the zeros of `P_r`, including multiplicities.  Newton's
inequalities make every fixed row `S(r,k)` log-concave.  This is the
classical real-rootedness argument of L. H. Harper, *Stirling Behavior is
Asymptotically Normal*, Ann. Math. Statist. 38 (1967), 410--414,
doi:10.1214/aoms/1177698956.  The falling factorial `(n)_k` is log-concave
because its successive ratios `n-k+1` decrease.  Their pointwise product,
and then reversal from `k` to `ell`, is log-concave.  Thus the law in (5)
is unimodal.

For any unimodal law on at most `r+1` values, if both sides of the threshold
at `ell` have mass at least `1/4`, then

```text
Pr(L=ell)>=1/[4(r+1)].                               (6)
```

Indeed, if a mode is at or to the left of `ell`, every atom strictly to the
right is at most the level-`ell` atom, and the right tail proves (6).  If a
mode is to the right, every atom at or to the left is at most the
level-`ell` atom, and the left cumulative mass proves (6).

### 3. The analytic range `r>=128`

The empty-box mean is

```text
E L=(r+1)(r/(r+1))^r<=3r/8.                          (7)
```

For `r>=128`, (7) follows from
`E L/r <=(1+1/r)exp(-r/(r+1))`; the latter expression decreases in `r`,
and at `r=128` it is below `3/8`.  An entirely rational verification of
the last inequality uses

```text
exp(128/129)>
  1+128/129+(128/129)^2/2+(128/129)^3/6+(128/129)^4/24.
```

Changing one ball changes `L` by at most one.  McDiarmid's inequality and
(7) therefore give

```text
Pr(L>9r/20)<=exp(-9r/800)<1/4                       (8)
```

for `r>=128`; the last strict inequality follows already at `128` from the
fourth-order lower Taylor bound for `exp(36/25)>4`.

A threshold with right side at least `1/4` must consequently satisfy
`ell<9r/20`.  Equations (2), (3), and (6) now yield

```text
Q_barP(A,A^c)
 >=Pr(L=ell) c_r(r+1-2ell)
 >=[1/(4(r+1))] [2/(3r(r-1))] [r/10]
 =1/[60(r+1)(r-1)].
```

### 4. Exact finite range `2<=r<=127`

Formula (5), the recurrence

```text
S(a,k)=S(a-1,k-1)+kS(a-1,k),
```

and the integer comparisons `4 Pr(L<=ell)>=1` and
`4 Pr(L>ell)>=1` give a complete exact calculation over this finite range.
For every balanced threshold it verifies `r+1-2ell>0` and verifies the same
lower bound (1) using (4), without floating point.  The minimum of

```text
(r+1)(r-1) Pr(L=ell) c_r(r+1-2ell)
```

over the audited thresholds is `9261/15625` at `(r,ell)=(9,4)`, much
larger than `1/60`.  The deterministic reproducer and full integer output
are `leaf_count_small_r_audit.py` and `leaf_count_small_r127.json`.

This finite calculation closes only the explicitly bounded range; the
analytic argument above proves every `r>=128`.

## Dependencies and scope

- **Proved here:** (2), the occupancy formula, unimodality reduction,
  analytic constants, and finite-range closure.
- **Accepted exact dependency:** M35's leaf-rotation rate (3), including the
  three-outcome heat-bath and `r-1` scan normalization.
- **Cited and re-derived:** Harper's real-rooted Stirling-polynomial
  argument; no asymptotic normality is used.
- **Not claimed:** a conductance lower bound for arbitrary cuts, a spectral
  gap for `bar P_r`, a transfer to the minimal identity-word sector, or any
  result for the global half-lazy `{3,4,5}` chain `K`.

## Reproduction

From this directory:

```text
python3 leaf_count_small_r_audit.py --r-min 2 --r-max 127 \
  --output leaf_count_small_r127.json
```

The calculation is deterministic and uses only Python exact integers and
`fractions.Fraction`; no seed or nonstandard package is used.
