# M227 final report: bandwidth-growth envelope

Date: 2026-08-13 UTC.

## Verdict

```text
KEEP (EXACT ONE-ATOM OBSTRUCTION/TRADEOFF):
WIDTH-1 AND WIDTH-2 PSD COMPRESSION BOTH STRICTLY INCREASE THE EXPLICIT
DEGREE-1-TO-6 ATOM'S FIRST-JACOBI CHARGE, AND WIDTH 2 IS STRICTLY CHEAPER.

UNRESOLVED:
THE EXACT OPTIMA, A DEGREE-UNIFORM COMPRESSION FACTOR, AGGREGATION OVER
RETAINED ATOMS, AND ANY RECURSIVE CONTRACTION.
```

## Immutable source gate

Every payload in frozen M210/M213, M216/M219, and M221/M224 passed before
use. Their checksum-ledger digests are respectively

```text
fe96d736dd4b0bd330d98975a47ad8e4e42a949d34ec27f5087daadd48120c7b
1ac5c73bf04d6ebff0c063c0fec5dc2fd4b33320e811261eb24644ff442a2af3
2c25bb31839bf8ff64181b9e4437fe70f5530bf5e7d0aa4eca8de4c21388d414
8a25c9a3edca393ff82137f65427188879da232597324c67d90062aa7d98c7ed
ff5315e5930f3d8dc3c959acbb4413e32df4cf1f9870338e94ec892c18ec1983
e147831cc9349f796770c5e1c5cc8e849ec83f6464767aa3ac72c0f15eb8f0a7
```

All predecessor directories remained immutable.

## Exact result

For the elevated atom

```text
e=(1,5/6,2/3,1/2,1/3,1/6,0),  M=ee^T,
```

let `p_w` be the least fresh first-Jacobi charge of a degree-six
bandwidth-`w` coefficient matrix PSD-dominating `M`. Exact rational primal
and dual certificates give

```text
60650731/180180000 <= p_1 <= 1136822741/3363360000,
167478197/630630000 <= p_2 <= 894863807/3363360000.
```

Since the raw atom has charge `1/4`, exact subtraction proves

```text
p_1>p_2>1/4.
```

The checker freezes every rational certificate entry and every positive
`LDL^T` pivot. The bracket widths are about `0.00139021` and `0.000489616`;
these decimals are interpretations only, not proof inputs.

## Meaning

Bandwidth relaxation from one to two has a rigorously quantified strict
benefit for this atom. Neither target band is cost-free: even width two must
increase the atom charge by at least

```text
9820697/630630000.
```

This refutes a factor-one compression inequality for either band at this
degree-`1` to degree-`6` lift. It does not refute all degree-uniform factors
greater than one. The exact optimal factors for this atom are not claimed.

## Generic retained statement

Degree elevation is the exact binomial matrix `E_(n,L)`, so a rank-one atom
`zz^T` becomes `(E_(n,L)z)(E_(n,L)z)^T`. Its optimal band compression is the
explicit conic primal/dual pair in `bracket_theorem.md`. This formulation is
degree-general, but no degree-uniform cost estimate is proved.

Multiplying a surviving atom by its exact `eta/pi_a` scales its raw charge,
majorant, and certified cost by that same positive scalar. Killed `a=d`
branches stay deleted. There is no proved aggregation bound across branches.

## Boundary and disposition

This mission used exactly the requested M221 degree-one-to-six atom and no
adjacent row. It proves no recursive cone closure, contraction, total AMV,
all-state theorem, spectral gap, mixing bound, or Terminal result. Verdict is
`KEEP`, not promotion to a recursion lemma. A fresh immutable audit should
reconstruct `G,e`, verify the four matrices and all exact pivots, and check
the three strict separations.

Reproduce with

```text
python3 -B bandwidth_growth_exact.py --output results.json
```

Python 3.12.3, standard library only, exact `Fraction`, `seed=null`.

