# M230 fresh immutable referee report

Date: 2026-08-13 UTC.

## Verdict

```text
REJECT M227 AS A SELF-CONTAINED FROZEN PROOF.

CORRECTED THEOREM INDEPENDENTLY SALVAGED IN M230:
THE FULL SEVEN-DIMENSIONAL CERTIFICATES PROVE p_1>p_2>1/4 FOR THE ONE ATOM.
```

## Frozen-source verification

M227's `SHA256SUMS` digest is exactly

```text
7b679294f7c6a4aa956a3577ae3350880698eb92d7b5776157f5f0e444e09105.
```

All eight listed payloads pass, and its complete top-level inventory is the
eight payloads plus `SHA256SUMS`. M227 remained immutable.

## Numbered objections

1. **M-1 (material): invalid zero-coordinate proof.** Restricting a full
   primal matrix to coordinates `0,...,5` does not generally preserve
   `<G,C>` because permitted last-coordinate band entries contribute to the
   objective. Consequently the frozen six-dimensional duals are not, by
   themselves, feasible certificates for the declared seven-dimensional
   dual. M227's section 2 therefore does not prove its stated reduction.

No further objection was found within scope.

## Independent salvage

The clean-room checker independently reconstructs `e`, `M`, and `G`, obtains
raw charge `1/4`, and verifies all four rational active matrices and all exact
active `LDL^T` pivots. It then constructs explicit full dual completions:

```text
w=1: y=(869/1494)Xbar[:,5],       final pivot 25/747;
w=2: y=(-43/54)Xbar[:,4]
         +(419/324)Xbar[:,5],     final pivot 97/3564.
```

The complete full matrices are frozen in `results.json`. They are positive
definite, match `G` on every required band entry, and preserve the objective
because `e_6=0`. The primal matrices extend by a zero final row/column. The
full-dimensional brackets are therefore

```text
60650731/180180000 <= p_1 <= 1136822741/3363360000,
167478197/630630000 <= p_2 <= 894863807/3363360000,
```

and exact arithmetic verifies all three claimed positive separations. Hence
M230 salvages the theorem `p_1>p_2>1/4`, but not M227's frozen proof.

## Generic statement and boundaries

The generic binomial rank-one elevation formula is correct. Positive scaling
by each surviving exact `eta/pi_a` scales the atom, certificate, and charge;
the envelope creates no killed `a=d` branch. These facts do not aggregate the
atoms or provide recursion.

The exact optima, a degree-uniform compression factor, aggregation, recursive
closure/contraction, all-state control, gap, mixing, and Terminal A/B remain
unresolved and are not claimed.

## Reproduction

```text
python3 -B fresh_referee_exact.py --output results.json
```

Python 3.12.3; standard-library exact `Fraction`; `seed=null`.

