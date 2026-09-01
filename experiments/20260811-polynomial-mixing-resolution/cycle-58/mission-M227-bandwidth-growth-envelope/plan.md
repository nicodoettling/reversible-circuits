# M227 plan: cost-controlled Bernstein bandwidth-growth envelope

Date: 2026-08-13 UTC.

## Objective

Quantify the exact first-Jacobi cost of compressing the explicit M221
unsaturated degree-one-to-six rank-one lift back into coefficient bandwidth
one and bandwidth two. Then prove or refute one generic degree-elevation
compression formula. This is an envelope subproblem, not a recursive
contraction theorem.

## Target and conventions

The project target remains uniform fixed-length identity transposition words,
with `(pq)(x)=p(q(x))` and displayed factors read left-to-right. Every retained
history branch continues to carry the exact factor `eta/pi_a`; killed `a=d`
branches remain absent. M227 analyzes the coefficient envelope applied after
that exact branch lift and does not modify these probabilistic weights.

## Immutable source lock

The project skill, `HANDOFF.md`, `GOAL_SPEC.md`, sampling/experiment
references, and relevant manuscript status were refreshed. M210/M213,
M216/M219, and M221/M224 are immutable. Every payload passes and their
checksum-ledger digests are:

```text
M210 fe96d736dd4b0bd330d98975a47ad8e4e42a949d34ec27f5087daadd48120c7b
M213 1ac5c73bf04d6ebff0c063c0fec5dc2fd4b33320e811261eb24644ff442a2af3
M216 2c25bb31839bf8ff64181b9e4437fe70f5530bf5e7d0aa4eca8de4c21388d414
M219 8a25c9a3edca393ff82137f65427188879da232597324c67d90062aa7d98c7ed
M221 ff5315e5930f3d8dc3c959acbb4413e32df4cf1f9870338e94ec892c18ec1983
M224 e147831cc9349f796770c5e1c5cc8e849ec83f6464767aa3ac72c0f15eb8f0a7
```

## Explicit atom and conic programs fixed before diagnostics

At cap `L=6`, let

```text
e=(1,5/6,2/3,1/2,1/3,1/6,0)^T,
M=e e^T.
```

This is the exact retained `d=1,a=0` lift of the degree-one rank-one feature
vector `(1,1)`, after multiplication to degree two and elevation to degree
six. Let `G` be the exact uniform first-Jacobi cost matrix in the degree-six
Bernstein basis. For target bandwidth `w in {1,2}`, define

```text
c_w=min <G,C>
    subject to C-M>=_PSD0,
               C_ij=0 for |i-j|>w.                    (P_w)
```

The explicit `C>=0` condition is redundant. With `P=C-M`, the exact dual is

```text
c_w=max <M,X>=e^T X e
    subject to X>=_PSD0,
               X_ij=G_ij for |i-j|<=w.               (D_w)
```

Large rational diagonal `C` gives strict primal feasibility. Numerical SDP
may guide candidate discovery, but only exact rational primal/dual PSD
certificates or a separate analytic completeness argument will be promoted.

## Analytic route

1. Reconstruct `G`, `e`, and the lifted atom with exact standard-library
   arithmetic and no predecessor import/data.
2. Solve `(P_1)/(D_1)` and `(P_2)/(D_2)` exactly, or freeze certified rational
   brackets if exact optima are provably nonrational and a completeness
   argument identifies them.
3. Compare optimal compression cost to the raw atom cost `<G,M>` and to the
   coarse diagonal envelopes.
4. Derive one generic rank-one degree-elevation theorem. Candidate form:
   characterize the optimal bandwidth-`w` domination of `e e^T` using the
   interval/chordal structure, with a quantified cost for a declared PSD
   functional `G`; otherwise provide an exact counterexample to a proposed
   degree-uniform factor.
5. State linearity: multiplying a branch by `eta/pi_a` scales both raw and
   envelope charges by the same positive scalar. No aggregation over branches
   is inferred without a proved summation bound.

## Boundaries and exclusions

- Only the explicit degree-one-to-six atom and one generic rank-one elevation
  theorem/counterexample.
- No second fresh row, parameter scan, or arbitrary-kernel cone search.
- No recursive contraction unless full aggregation and closure are actually
  proved; no all-state, total-AMV, gap, mixing, or Terminal A/B claim.

