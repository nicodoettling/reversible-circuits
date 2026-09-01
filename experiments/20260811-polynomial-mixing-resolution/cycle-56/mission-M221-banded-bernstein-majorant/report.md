# M221 final report: minimal banded Bernstein majorant

Date: 2026-08-13 UTC.

## Field 1 — verdict

```text
PROVED FOR THE EXACT B=1,L=6,kappa=2,D=1 ROW:
THE LEAST FEASIBLE DEGREE-SIX BERNSTEIN COEFFICIENT BANDWIDTH IS ONE.

REFUTED AS A RAW RECURSIVE FAMILY:
FIXED WIDTH ONE IS NOT CLOSED UNDER UNSATURATED RETAINED LIFTS.

UNRESOLVED:
A COST-CONTROLLED WIDTH-ONE ENVELOPE AND FRESH CONTRACTION.
```

## Field 2 — target and strict scope

The project target remains uniform fixed-length identity transposition words,
with `(pq)(x)=p(q(x))` and displayed factors read left-to-right. M221 concerns
only one auxiliary fresh first-Jacobi row. It establishes no all-state
majorant, contraction, total AMV, gap, mixing, or Terminal result.

## Field 3 — immutable source gate

Every payload in frozen M210/M213 and M216/M219 passed before use. Their
checksum-ledger digests are respectively

```text
fe96d736dd4b0bd330d98975a47ad8e4e42a949d34ec27f5087daadd48120c7b
1ac5c73bf04d6ebff0c063c0fec5dc2fd4b33320e811261eb24644ff442a2af3
2c25bb31839bf8ff64181b9e4437fe70f5530bf5e7d0aa4eca8de4c21388d414
8a25c9a3edca393ff82137f65427188879da232597324c67d90062aa7d98c7ed
```

All predecessors remained immutable.

## Field 4 — exact conic pair

For degree-six Bernstein vector `b`, bandwidth `w` means
`C_ij=0` for `|i-j|>w`. If `K=b^T A b` is the actual kernel and `G` is the
first-Jacobi charge matrix, the primal/dual pair is

```text
p_w=min <G,C>                  d_w=max <A,X>
    s.t. C-A>=0,                   s.t. X>=0,
         C_ij=0 off band;               X_ij=G_ij on band.
```

The primal has the strict point `C=tI` for large rational `t`; strong duality
holds. The promoted decision uses only exact primal/dual weak certificates.

## Field 5 — width-zero obstruction

The rational M216/M219 dual `X_0=vv^T+diag(G_jj-r_j^2)` is feasible for
width zero and has exact positive excess

```text
<A,X_0>-(1-q)
=1000948704365931347999936328408157889213
 /48209994003606915089647408250880000000000 > 0.
```

Thus width zero cannot fit the budget.

## Field 6 — exact width-one primal

The exact symmetric tridiagonal matrix `C_1` has

```text
diag(C_1)=(101/50,111/100,43/100,19/25,39/25,99/50,21/5),
offdiag(C_1)=(1/3,2/15,1/12,1/5,3/5,11/8).
```

Its strict signed-diagonal-dominance margins are

```text
(253/150,193/300,16/75,143/300,19/25,1/200,113/40),
```

so `C_1>0`. Exact subtraction shows `C_1-A` is also symmetric strictly
diagonally dominant with positive diagonal; its smallest row margin is

```text
22066085580152050340437577895121
/9632366434287095922007474176000000 > 0.
```

Hence `C_1-A>0`. Its charge is

```text
<G,C_1>=4937603/9172800,
(1-q)-<G,C_1>=485323987/37571788800 > 0.
```

Together with the width-zero obstruction, this proves least feasible
bandwidth `w=1` for this exact row only.

## Field 7 — independent exact reconstruction

The standalone checker uses grouped Cayley roots, exact `Fraction` arithmetic,
the retained factor `eta/pi_a`, and exact omission of killed `a=d`. It imports
and reads no predecessor code or data. It reproduces

```text
kernel d2ee4261fd89e712d0649d9cea3c30952256bff82c99134a59fce7b151505152
A      d1dd37fe74b894523b4b049099d194ed34fb64fb36d144b48ff3746a34e1ccae
```

and independently constructs the charge matrix, both certificates, all PSD
margins, and exact charges.

## Field 8 — lift closure and exact failure

A saturated likelihood lift shifts both Bernstein indices by the same amount
and preserves bandwidth. If the multiplied degree is `n<L`, degree elevation
spreads each index across an interval of length `L-n`, so raw bandwidth can
grow from `w` to at most

```text
min(L,w+(L-n)).
```

The bound is attained enough to refute closure: a degree-one width-one
rank-one atom with vector `(1,1)`, after retained `d=1,a=0` multiplication
and elevation from degree two to six, has vector

```text
(1,5/6,2/3,1/2,1/3,1/6,0)
```

and outer-product bandwidth five. Thus raw width one is not recursively
closed. Although `Tr(M)I>=M` is a positive-linear diagonal envelope for every
PSD `M`, no charge control is proved for it.

## Field 9 — disposition and reproducibility

Verdict: `KEEP` as exact one-row structural progress, not `PROMOTE` to a
recursive contraction lemma. The next standalone obligation is a
cost-controlled reset/lift envelope preserving the width-one budget advantage,
or a broader structured cone with analytic closure.

Run:

```text
python3 -B banded_bernstein_exact.py --output results.json
```

Python 3.12.3, standard library only, exact `Fraction`, `seed=null`. No
numerical SDP output is frozen or used in any promoted conclusion.

