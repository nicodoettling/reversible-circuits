# M201 substantive checkpoint

Date: 2026-08-13 UTC.
Status: exact compatible-slack formula derived; independent lower-sector
reservation route exactly obstructed at the first `h>=4` case.

## Immutable gate and scope

- Complete frozen ledgers for M173/M177, M179/M184, and M193/M197 pass. No
  predecessor was edited.
- Scope is only the fresh-parent reset plus `h>=4` remainder. No total AMV,
  all-state/all-`L`, gap, mixing, or terminal is claimed.

## Exact compatible lower-sector reservations

For a fixed fresh parent `xi=(B+L,2,1,B)`, the accepted coefficients must be
evaluated at the same `L`:

```text
h1 <=(1-q0) A1(L-1),
A1(n)=sum_r eta1(n,r)R_(r+1),

h2 <= 1/4                              if L=2,
      (2/3) M2(L-2)                    if L>=3,
M2(n)=(n+1)^n(n+2)/(n+3)^(n+1),

h3 < 3/8                               if L=3,
     (3/4) M3(L-3)                     if L>=4,
M3(n)=(3/2)(n+1)^n(n+2)(n+3)/(n+4)^(n+2).
```

Here `q0=w_B/w_(B+1)` and `q=q_(B,L)`. Thus the exact residual after those
accepted *upper bounds* is

```text
Delta_(B,L)=1-q-(1-q0)A1(L-1)-H2(L)-H3(L).         (B)
```

This keeps the `q0` dependence and the mutually compatible exterior
boundaries; it does not add the three global worst constants.

## Exact route obstruction at `(B,L)=(2,4)`

This is the first state with an `h=4` descendant. Exact same-`L` values are

```text
q=26250/117649,          q0=2/3,
A1(3)=3299/18750,        h1<=3299/56250,
H2(4)=24/125,            H3(4)=27/125,

Delta_(2,4)=293289307/945393750 ~=0.310229793.
```

Direct evaluation of the accepted full vector/history kernel gives

```text
T1_reset=6628367198857337/21450464220937500 ~=0.309008100,
T1_(h=4)=1735419680239/29524500000000       ~=0.058778969.
```

Therefore

```text
T1_reset+T1_(h=4)-Delta_(2,4)
=480024264873449410111/8339940489100500000000
~=0.057557277>0.                                      (O)
```

Equation (O) exactly refutes the proof route that reserves the accepted
`h1,h2,h3` upper bounds independently and asks reset plus `h>=4` to fit in
the nominal leftover (B). It is not an unrestricted polynomial witness: it
uses the actual finite history feature, every Jacobi cross term through exact
`T1`, and killed observations before the direct sum.

## Logical reach and next lemma

The witness does **not** refute the true parent inequality. At `(2,4)`, the
exact complete value is about `0.405167471`, well below
`1-q~=0.776878682`. The accepted lower-sector estimates are loose and their
unused slack pays for reset/tail in the exact history.

Hence the first remaining lemma must jointly amortize the actual `h<=3`
sector slack with reset and `h>=4`, or provide a vector/history inequality
that couples them. A standalone positive tail bound against `Delta_(B,L)` is
false already at the minimal tail case.

Next: package the exact clean-room diagnostic and freeze this strict route
obstruction/reduction with a fresh-audit request.
