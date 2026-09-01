# M210 plan: cumulative slack ladder through height three

Date: 2026-08-13 UTC.

## Objective

Test the universal fresh-parent cumulative-slack statement left by M206/M209:

```text
S_1(B,L)+S_2(B,L)+S_3(B,L) >= X_3(B,L).
```

Here `S_h=U_h-T_h` uses the accepted compatible same-parent sector bound and
the exact actual sector charge, while `X_3` is reset plus `h>=4` charge above
the nominal residual. Seek an analytic recursive/monotone certificate first.
If the statement is false, freeze its first exact bounded counterexample and
identify the first deeper rung or state variable required.

## Target and conventions

- Project target: uniform fixed-length identity transposition words.
- Auxiliary object: normalized full unweighted reset excursion `F=H/q` at a
  fresh right-heavy parent `(B+L,2,1,B)`.
- Composition: `(pq)(x)=p(q(x))`, displayed factors left-to-right.
- Preserve the orthogonal actual-history decomposition, every
  likelihood-weighted Hilbert/Jacobi cross term, parent covariance
  subtraction, and exact deletion of killed `a=d`.

## Immutable dependencies

Treat M206/M209 and M173/M177, M179/M184, M193/M197, M201/M204 as immutable.
Verify all ledgers before substantive use and write only in M210.

## Method

1. Derive the exact `C_3-X_3` recursion before computation, exposing whether
   it is merely the full fresh `T_1` deficit or admits a stronger monotone
   decomposition.
2. Identify a precise candidate state variable/residual certificate. Do not
   add independent worst-case bounds.
3. Only then run compact exact diagnostics, capped at `B<=4,L<=10`, stopping
   at the first counterexample or decisive obstruction.
4. A universal theorem requires an analytic certificate; finite passes are
   evidence only.

## Guardrails

No broad scan, scalar/Jensen/diagonal shortcut, survival conditioning,
unproved all-`L` inference, total AMV, gap, mixing, or Terminal claim.

## Deliverables

Durable halfway checkpoint, theorem/reduction or exact counterexample,
compact reproducible exact artifact, nine-field report with numbered
self-objections, manifest/SHA freeze, and fresh immutable audit request.
