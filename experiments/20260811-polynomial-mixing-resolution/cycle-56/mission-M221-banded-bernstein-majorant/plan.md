# M221 plan: minimal off-diagonal Bernstein PSD-envelope bandwidth

Date: 2026-08-13 UTC.

## Objective

At the single fresh state `(B,L,kappa,D)=(1,6,2,1)`, determine exactly the
least coefficient bandwidth that permits a degree-six Bernstein PSD kernel to
dominate the exact actual kernel while meeting the first-Jacobi budget. Then
audit only the algebraic stability of that finite cone under exact retained
likelihood lifts and degree elevation.

## Target and conventions

The project target remains the uniform law on fixed-length identity
transposition words. Permutations compose as `(pq)(x)=p(q(x))`, with displayed
factors read left-to-right. M221 concerns only an auxiliary fresh first-Jacobi
kernel certificate; it is not an original-chain contraction or mixing claim.

## Immutable source lock

- Read the project skill, `HANDOFF.md`, `GOAL_SPEC.md`, the sampling and exact
  experiment references, and the relevant manuscript status sections.
- Treat M210/M213 and M216/M219 as immutable.
- Verify every frozen payload before using the accepted full-Gram recursion,
  actual coefficient matrix `A`, or diagonal-cone obstruction.

Expected ledger digests:

```text
M210 fe96d736dd4b0bd330d98975a47ad8e4e42a949d34ec27f5087daadd48120c7b
M213 1ac5c73bf04d6ebff0c063c0fec5dc2fd4b33320e811261eb24644ff442a2af3
M216 2c25bb31839bf8ff64181b9e4437fe70f5530bf5e7d0aa4eca8de4c21388d414
M219 8a25c9a3edca393ff82137f65427188879da232597324c67d90062aa7d98c7ed
```

## Named cone and conic programs fixed before diagnostics

Let `b(u)=(b_(6,0)(u),...,b_(6,6)(u))^T`. For bandwidth
`w in {0,...,6}`, define

```text
C_w={J_C(u,v)=b(u)^T C b(v):
     C=C^T>=_PSD0 and C_ij=0 whenever |i-j|>w}.
```

Write the exact actual kernel as `K=b^T A b`, let `G` be the exact charge
matrix satisfying `Q[b^T C b]=<G,C>`, and put `beta=1-q`. The primal is

```text
p_w=min <G,C>
    subject to C-A>=_PSD0,
               C_ij=0 for |i-j|>w.                    (P_w)
```

Since `A>=0`, the domination constraint already implies `C>=0`. Equivalently,
with `P=C-A`, minimize `<G,A>+<G,P>` over `P>=0` and
`P_ij=-A_ij` off the band. Its dual is

```text
d_w=max <A,X>
    subject to X>=_PSD0,
               X_ij=G_ij for |i-j|<=w.                (D_w)
```

Strict primal feasibility follows from `C=tI` for sufficiently large rational
`t`, so strong duality holds. A rational primal `C` with exact PSD certificates
and `<G,C><=beta` proves feasibility. A rational dual `X` with the displayed
band equalities and `<A,X>>beta` proves budget infeasibility.

## Method

1. Independently reconstruct `A`, `G`, `q`, and the actual slack using exact
   `Fraction` arithmetic and no predecessor import/data.
2. Numerical SDP may locate certificates for successive `w`, but it will not
   be promoted.
3. Rationalize candidate primal/dual matrices and certify PSD exactly, using
   rational `LDL^T`, principal minors, or explicit Gram/rank-one factors.
4. Establish the least feasible `w` by exact obstruction certificates for all
   smaller widths and one exact feasible certificate at that width.
5. Check how likelihood multiplication and degree elevation act on bandwidth.
   State precisely whether the named fixed-width cone is closed, requires a
   wider envelope, or is refuted as a recursive family.
6. Freeze theorem/obstruction, exact checker/results, report, audit request,
   manifest, and checksums.

## Boundaries and exclusions

- Primary computation: only `(B,L,kappa,D)=(1,6,2,1)` and its forced recursive
  reconstruction.
- At most one adjacent boundary row, only if needed to falsify a closure claim.
- No parameter scan beyond `w=0,...,6` for this one matrix.
- No all-state recursive contraction, total AMV, spectral-gap, mixing, or
  Terminal A/B inference.

