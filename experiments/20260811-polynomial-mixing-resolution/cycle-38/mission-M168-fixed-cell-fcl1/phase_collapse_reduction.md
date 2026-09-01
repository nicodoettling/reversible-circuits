# M168 exact phase-collapse reduction for the first fixed cell

Date: 2026-08-13.

Status: Propositions 1--3 are **proved**. The two uniform scalar estimates
`(PCS-bound)` and `(FD-bound)` are **unresolved**. Consequently `(FCL1)` is
unresolved. This note concerns only M161/M166's accepted balanced fixed cell
for M73's nonlazy cyclic rank-two quotient kernel.

## 1. Scope, convention, and accepted score

Permutations compose as `(pq)(x)=p(q(x))`; factors multiply left-to-right.
Let `n=3k`, with odd `k>=3`, and

```text
h=(0 1 ... n-1),
A_k=(0,k,2k),                 B_k=(0,1)(k,2k),
E_r=(r,r+1)                   (indices modulo n),
t_y=E_0 E_(y+1),              1<=y<=n-3.
```

Write `O_y` for the cyclic target orbit and

```text
z_k(y)=[bar K^2(O_B,O_y)-bar K^2(O_A,O_y)]/pi_y,
Z_k(y)=k z_k(y).
```

M161/M166 proved that `pi_y=bar pi(O_y)` is independent of `y`, that
`O_y=O_(n-2-y)`, and that every `z_k(y)` is the full signed convolution of
both source channels and all triangle/double intermediate and `IS/IN/X`
target topologies before absolute value. The target is

```text
(FCL1)  sup_(odd k>=3) sum_(y=1)^(n-3)|Z_k(y)|<infinity.
```

For a permutation `g`, put

```text
A_g=F_(n-3)(g^-1h),
C_g(s)=F_(n-5)((gs)^-1h),
F_T=F_(n-3)(t_1^-1h).
```

Let `X_n` be M73's raw supported rank-two products and let `a(s)` be their
ordered transposition-pair lift multiplicity (`3` for a triangle and `2`
for a double).

## 2. Complete all-lag phase collapse

Fix `s in X_n` and put `q=s^-1h`. Its three residual cycles are denoted
`C_i`, with sizes `d_i`. Call the polygon boundary edge `E_r` **generic for
`s`** when its head `r+1` is fixed by `s`. Equivalently,

```text
q(r)=s^-1(r+1)=r+1,
```

so a generic `E_r` is literally a directed adjacent edge of one cycle of
`q`.

The supported rank-two products are the cyclically oriented triangles and
the two noncrossing double colors. Directly writing their residual cycles in
positive cyclic-gap coordinates gives the following elementary fact: if
`r+1` belongs to the support of `s`, then `E_r` joins two different residual
cycles of `q`; if `r+1` is fixed, `E_r` is the adjacent cycle edge just
displayed. Thus a boundary edge can decrease the transposition rank of `q`
only in the generic case. This is also the literal face-boundary description
behind M73's triangle and two double schemas.

Let

```text
g_i=#{generic E_r lying in C_i},
a_i=#{r: E_r and E_(r+1) are both generic edges of C_i}.
```

Here `a_i` counts each ambient adjacent unordered edge-pair once. The lags
`l=y+1`, `1<=y<=n-3`, are exactly `2,...,n-2`. Hence `(r,l)` enumerates every
ordered pair of disjoint polygon boundary edges exactly once. There are

```text
g_i(g_i-1)-2a_i
```

ordered disjoint pairs in one component `C_i`, and `2g_i g_j` ordered pairs
between `C_i,C_j` when `i<j`.

Left multiplication by a generic edge isolates its tail as a singleton.
Two disjoint generic edges in one cycle therefore change its size `d_i`
into `(1,1,d_i-2)`; one generic edge in each of two cycles changes
`(d_i,d_j)` into `(1,d_i-1,1,d_j-1)`. Invalid sizes contribute zero.

### Proposition 1 (proved: complete phase moment)

Define

```text
S(s)=sum_i [g_i(g_i-1)-2a_i]
          F_(n-5)(sort(d_1,...,1,1,d_i-2,...,d_3))
    +sum_(i<j)2g_i g_j
          F_(n-5)(sort(d_(other),1,d_i-1,1,d_j-1)).   (PC)
```

Then

```text
S(s)=sum_(y=1)^(n-3) sum_(r mod n)
        F_(n-5)(E_r E_(r+y+1) s^-1h).                (2.1)
```

In M161's language, `(PC)` sums `IS` and `IN` into the one-component second
moment and `X` into the cross-component product moment. No absolute value is
taken, and all triangle/double intermediates remain to be summed afterward.

#### Proof

The lag enumeration gives all ordered disjoint boundary-edge pairs. A
non-generic edge joins distinct residual cycles and cannot lower rank; a
generic edge is an actual cycle edge and isolates one singleton. The two
counting formulas and the displayed completion sizes now partition every
nonzero summand in `(2.1)`. QED.

### Proposition 2 (proved: exact signed cell-sum formula)

One has

```text
sum_(y=1)^(n-3) z_k(y)
 =n^(n-2)/(n F_T)
  sum_(s in X_n) a(s) S(s)/A_s
       [C_(B_k)(s)/A_(B_k)-C_(A_k)(s)/A_(A_k)].       (PCS)
```

#### Proof

Expand the accepted M94/M161 raw intermediate convolution. For a fixed
intermediate `s`, summing the literal target orbit over phase and then over
`y` gives `(2.1)`. The target lift factor `2` cancels the same factor in
`pi_y=2nF_T/n^(n-2)`; the intermediate lift remains `a(s)`. This gives
`(PCS)`. All signed source terms, intermediate kinds, and target topologies
are still combined before any absolute value. QED.

No quotient matrix, shell decomposition, or continuum replacement occurs
in `(PC)--(PCS)`.

## 3. Physical cell event and deterministic L1 closure

Let `mathcal C_k` be the set of distinct physical target orbits represented
by the colored list `O_y`, `1<=y<=n-3`. Since `n` is odd, reflection has no
fixed point on this list, and every physical orbit occurs exactly twice.

### Proposition 3 (proved: event identity and scalar sufficient condition)

The complete two-step event contrast is

```text
Delta_k(mathcal C_k)
 :=bar K^2(O_B,mathcal C_k)-bar K^2(O_A,mathcal C_k)
  =(pi_y/2) sum_y z_k(y).                             (CE)
```

For an arbitrary real sequence `x_1,...,x_N`, let

```text
V(x)=sum_(i=1)^(N-1)|x_(i+1)-x_i|.
```

Then

```text
sum_i|x_i|<=|sum_i x_i|+N V(x).                      (TV-close)
```

Consequently `(FCL1)` follows from the pair of uniform estimates

```text
(PCS-bound)  k |sum_(y=1)^(n-3) z_k(y)|=O(1),

(FD-bound)   k^2 sum_(y=1)^(n-4)|z_k(y+1)-z_k(y)|=O(1).  (SC)
```

#### Proof

The constant target mass and the exact two-to-one colored list give `(CE)`.
For `(TV-close)`, the arithmetic mean lies between the minimum and maximum
of the sequence, and the range is at most `V(x)`. Thus
`|x_i-mean(x)|<=V(x)` for every `i`; sum
`|x_i|<=|mean(x)|+|x_i-mean(x)|` over `i`.

Apply this inequality to `x_y=Z_k(y)=kz_k(y)` with `N=n-3=3k-3`:

```text
sum_y|Z_k(y)|
 <= k|sum_y z_k(y)|+(3k-3)k V(z_k).
```

The two bounds in `(SC)` make the right side uniformly bounded. QED.

There is also an exact sign alternative. Writing
`P_k=sum_y(z_k(y))_+` and `N_k=sum_y(-z_k(y))_+`,

```text
sum_y|Z_k(y)|
 =k|sum_y z_k(y)|+2k min(P_k,N_k).                   (NEG-id)
```

Thus `(PCS-bound)` plus `k min(P_k,N_k)=O(1)` would prove `(FCL1)`; universal
one-sign is a still stronger sufficient statement. Neither a sign theorem
nor the negative-mass bound is proved here.

## 4. Exact checks and limitations

`signed_cell_sum_probe.py` implements `(PC)--(PCS)` without a quotient
matrix. Over exact `Fraction` it reproduces the sum of every frozen M161
score at `k=3,5,7`. Targeted floating evaluation was stopped at
`k=9,11,13,15`. The values of `k sum_y z_k(y)` are approximately

```text
3.12033, 2.43231, 2.17959, 2.05295, 1.97715, 1.92673, 1.89079.
```

The corresponding `n^2 Delta_k(mathcal C_k)` values are approximately

```text
2.66440, 1.51186, 1.19283, 1.04895, .96771, .91568, .87955.
```

These finite values are calibration only. A separate targeted exact M161
evaluation at `k=9` found all 24 scores positive and
`A_k(1,1)=0.7698574787`; positivity through `k=9` is not promoted.

The first unresolved statements are exactly `(PCS-bound)` and `(FD-bound)`.
The component moments `g_i,a_i` are not determined solely by the unordered
residual cycle sizes, so `(PC)` does not immediately collapse to a
one-dimensional Borel-size average. An asymptotic bound must still preserve
the signed source contrast across both channels. Finite positivity supplies
no universal sign theorem.

This fixed-cell reduction gives no direct-L1 or all-edge estimate and no H0,
spectral-gap, bridge, identity-chain, mixing, or Terminal inference.

