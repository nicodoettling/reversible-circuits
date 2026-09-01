# M64 plan: multistep minimal/exterior closure red team

## Objective and exact target

Use the convention `(pq)(x)=p(q(x))`, `m=2N-2`, and the literal lazy
`r in {3,4,5}` exact same-product heat-bath kernel.  Let `F_N` be the
minimal connected full-support macro.  Fix the balanced path-core union
`A_N subset F_N` from M63 and define the exterior support-graph closure by

```text
E_0={y in F_N^c:K(x,y)>0 for some x in A_N},
E_(k+1)=E_k union {y in F_N^c:K(x,y)>0 for some x in E_k},
C_k=A_N union E_k.
```

The main target is either:

1. an explicit growing `k(N)` for which `C_k` has superpolynomially small
   two-sided conductance, with exact global mass and complete H3/H4/H5
   boundary flow; or
2. a uniform inverse-polynomial conductance theorem, or the strongest
   rigorously delimited anti-bottleneck subrange, based on an exterior-depth
   boundary identity/canonical escape statistic.

The independent fallback candidate is a positive-surplus insertion-history
phase: a proper mixed cut built from a fixed deleted-label bridge base and a
halo of square insertions/refinements.  It will be tested against explicit
square-refresh and support-merge outcomes rather than inferred from an
auxiliary insertion chain.

## Work program

1. Prove the exact breadth-first layer and stationary-flow identities for
   `E_k`, including orientation and every block size.
2. Derive exact degree and minimum-positive-transition bounds and determine
   what they do and do not imply for growing depth.
3. Seek a canonical exterior-depth escape certificate.  Audit whether
   disconnected minimal-length words admit a pointwise local merge; if not,
   isolate the exact obstruction.
4. Enumerate the complete `N=5,m=8` exterior closure from the accepted M63
   balanced core cut.  Record layer sizes, exact rational boundary flow by
   `r=3,4,5`, mass orientation, and the universal assertion this can
   falsify.  This calculation is diagnostic only unless paired with a finite
   basis argument.
5. Analyze the positive-surplus insertion-history candidate independently.
6. Freeze a halfway checkpoint after the exact identities and first
   decisive obstruction/result, then write the required nine-field report.

## Expected failure modes

- A polynomial support degree only yields `N^{O(k)}` mass control and is not
  uniform when `k` grows.
- A large halo is not a bottleneck without an upper bound on its full shell
  flow and the correct smaller-side mass.
- Conductance is not monotone under adding exterior layers.
- Pointwise adjacent-square or merge certificates may fail even when their
  stationary average is polynomial.
- Dense-shell trace estimates at `m=4N^3+4` cannot be imported at
  `m=2N-2` because their even-outside smoothing hypothesis is absent.
- A slow insertion-history restriction is nonresponsive if any literal H4
  or H5 outcome bypasses it.

## Computation metadata contract

Any exact script will use deterministic enumeration (`seed=null`), Python
3.12.3, no nonstandard package, `PYTHONDONTWRITEBYTECODE=1`, machine-readable
JSON, repository commit `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`, and an
explicit statement of the universal claim it could falsify.
