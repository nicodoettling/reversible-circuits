# M73 plan: cyclic-orbit incidence gap

Date: 2026-08-12.

## Objective and scoped target

For odd `n=2l+1>=7`, `m=n-1`, and endpoint
`h=(0 1 ... n-1)`, study the uniform law on reduced transposition
factorizations `t_1...t_m=h`.  Permutations compose as
`(pq)(x)=p(q(x))`, and factor tuples multiply left-to-right.

The target claim is M70's exact remaining proposition: an
inverse-polynomial Poincare gap for the `H_0` sector, equivalently the
uniform stationary-flow quotient by simultaneous conjugation

```text
U(t_1,...,t_m)=(h^-1 t_1 h,...,h^-1 t_m h),
```

of the complete-pair chain `C_l` or aligned pair chain `B_l`.  This is a
fixed nonidentity-endpoint auxiliary theorem, not Terminal A or B.

## Candidate route

1. Reconstruct Stanley's factorization-to-labelled-Cayley-tree bijection and
   determine the exact induced action of `U` on trees and Pruefer codes.
2. Test whether quotienting this action makes one-coordinate Pruefer refresh
   or one-edge UST basis exchange polynomially simulable by the adjacent
   raw-pair chain `L_n`, hence by `B_l` through M70's full-state H4 padding.
3. If direct locality fails, seek a randomized recoverable path comparison
   at uniform microstate stationary flow, explicitly retaining cyclic phase
   and exchanged labels as metadata.
4. If that comparison fails, isolate the smallest exact obstruction and
   verify it exhaustively at `n=5,7`; distinguish path length, density, and
   genuine capacity/congestion obstructions.

## Named claims to falsify

- `U` becomes diagonal cyclic relabeling of Stanley trees or Pruefer codes.
- Every quotient UST basis exchange has a bounded- or polynomial-length
  adjacent-Hurwitz representative with polynomially recoverable load.
- The orbit-incidence statistic is determined by an unrooted degree profile.

The third claim is already refuted by M70 at `n=7` and is retained only as a
calibration.

## Exact computation

A deterministic Python harness will enumerate all reduced long-cycle
factorizations for `n=5` and `n=7`, verify endpoint products and the free
cyclic action, reconstruct Stanley trees/Pruefer codes, compute the induced
`U` action, and measure quotient locality for relevant source moves.  Raw
machine-readable output will record Python version, repository commit,
commands, parameters, and `seed=null`.

## Expected failure modes

- Stanley's bijection is uniform but cyclic conjugation is a nonlocal tree
  automorphism rather than label shift.
- A single source-chain move changes linearly many tree/Pruefer coordinates;
  linear distance alone is not a congestion obstruction.
- A canonical quotient representative has exponentially unbalanced basins.
- Exact finite ranks or spectral gaps do not prove asymptotic mixing.

## Deliverables and verdicts

Write `checkpoint.md` by halfway, then a nine-field `report.md` giving one of:

- `PROVED`: explicit polynomial comparison/gap in `H_0`;
- `REFUTED`: an asymptotic superpolynomial cut/eigenmode in `H_0`;
- `OPEN AT A NAMED STEP`: a strictly smaller rigorous obstruction with exact
  finite falsifiers.

