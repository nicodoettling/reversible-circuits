# M216 plan: full nonconstant PSD majorant

Date: 2026-08-13 UTC.

## Objective

Target the unresolved fresh-parent first-Jacobi full-child-Gram majorant
lemma left by accepted M210/M213. Seek either:

1. an explicit parameterized, nonconstant PSD kernel supersolution
   `J_(B,L)(u,v)` whose exact reset plus retained likelihood lifts fit the
   fresh budget; or
2. an exact obstruction to one named finite-dimensional kernel ansatz.

## Target and conventions

The project target remains the uniform law on fixed-length identity words in
transpositions. Permutations compose as `(pq)(x)=p(q(x))`, with displayed
factors read left-to-right. This mission concerns only the normalized fresh
first-Jacobi auxiliary recursion, not an original-chain mixing theorem.

## Immutable inputs and ownership

- Own only `cycle-54/mission-M216-full-kernel-psd-majorant/`.
- Treat M210/M213 and the prior accepted AMV chain as immutable.
- Verify frozen inventories before importing formulas or conclusions.

## Analytic route

1. Reconstruct the exact reset kernel and child-lift recursion, including the
   single `1/pi_a`, exterior `eta`, and omission of killed `a=d`.
2. Inspect only minimal exact low-`L` kernels to identify a named closed
   nonconstant family, initially weighted Jacobi/Christoffel or Green-kernel
   candidates.
3. State the PSD order and antitone residual certificate symbolically before
   diagnostics.
4. Test the chosen ansatz only for compact `L<=6` rows. A universal theorem
   requires an analytic closure certificate; otherwise freeze the first exact
   counterexample/obstruction to that ansatz.

## Expected failure modes

- likelihood multiplication raises polynomial degree outside a fixed-rank
  Jacobi family;
- PSD coefficient order may fail despite the scalar first-Jacobi budget;
- constant-kernel or finite-summary collapse (already refuted) may reappear;
- exact reset coordinates may not lie in the proposed cone;
- a finite diagnostic pass may be mistaken for a universal result.

## Deliverables

Durable halfway checkpoint, exact derivation or named-ansatz obstruction,
compact reproducible checker/results, nine-field report, audit request,
manifest, and SHA256 freeze. No broad enumeration, total-AMV, gap, mixing, or
Terminal claim.
