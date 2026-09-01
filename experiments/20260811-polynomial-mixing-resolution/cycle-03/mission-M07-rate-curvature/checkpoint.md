# Halfway checkpoint

## Stable result

`dense_curvature.md` proves an exact adjacent-rate curvature bound.  If
`v>=3`, `M=binom(v,2)`, `k=2(v-1)+2g`, and

```text
k-2 >= 4 M log(2v),
```

then

```text
rho_v(g+1)-rho_v(g) >= (2k-2/k)/M^2 >= k/M^2.
```

The proof uses the regular-character expansion for all identity returns and
an explicit cut union bound for disconnected support.  It bounds the three
adjacent relative errors separately; this is essential because two unrelated
constant-factor asymptotics cannot preserve curvature.

## Exact falsification scan

`curvature_scan.py` implements Dubrovin--Yang--Zagier Theorem 1 and equations
(14)--(15) in exact integer arithmetic.  It found no nonpositive increment
for

```text
2<=v<=60, 0<=g<=300.
```

The smallest increment for large `v` occurs near `g=v/3`; the observed
quantity `(v+g+1)^3 [rho_v(g+1)-rho_v(g)]` decreases slowly toward roughly
`90`.  This finite computation can refute positivity but cannot prove it.

The normalization calibrations are exact:

```text
C_0(2)=1, C_0(3)=24, C_0(4)=2880,
rho_4(1)=16/13, rho_4(2)=195/82.
```

For `v=2`, the special first increment is
`rho_2(1)-rho_2(0)=12`; the formula `4k+2` applies only to increments with
`g>=1`.  The zero-range rate-increment hypothesis is indexed by every
occupancy `g>=0`, including this first increment.

## Failed shortcut

The DYZ polynomial `gamma_v(s)` has positive coefficients, but positivity
alone does not make the factorial-normalized coefficient sequence
log-concave: arbitrary positive mixtures of powers of
`s=4sinh^2(x/2)` can acquire a new high-degree contribution and violate
log-concavity.  Moreover, after removing the forced factor `s^(v-1)`, the
DYZ polynomials already have nonreal roots at `v=4`.  Thus a plain
real-rooted/PF-sequence argument is unavailable.

## Exact frontier

The first unproved proposition is **LOW-AND-INTERMEDIATE-GENUS CURVATURE**:
prove a universal inverse-polynomial lower bound on the increment for

```text
v>=3, 0<=g, 2(v-1)+2g-2 < 4 binom(v,2) log(2v).
```

This is still an infinite `g=O(v^2 log v)` region.  DYZ Proposition 1 proves
only `rho_v(g)>=12/v^3`; its convolution-ratio argument does not control the
difference of consecutive ratios.  The next attack is to seek a synchronized
strong-log-concavity statement for the ordered-split summands in that positive
recurrence, and to falsify it before using convolution closure.
