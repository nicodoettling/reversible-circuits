# M282 plan: channel-two signed scalar-Abel vector bound

## Scope and target

This mission addresses one proof obligation only: the channel-two signed
scalar-Abel vector bound (CSBV) isolated by M272.  The ambient sampler target
is the uniform law on

```text
Omega(N,m) = {(t_1,...,t_m) in T_N^m : t_1 ... t_m = id},
```

for the lazy exact same-product `{3,4,5}` block heat-bath kernel specified in
`GOAL_SPEC.md`.  The present work neither proves a sampler theorem nor changes
that kernel.

For odd `k >= 3`, retain every literal lag/phase/kind/collision coordinate of
M272's channel-two profiles and prove or refute

```text
|| E_{k-1} Phi^D_{k-1}
   + sum_{u=1}^{k-2} E_u (Phi^D_u-Phi^D_{u+1}) ||_1 = O(1/k),
```

with

```text
E_{k-1} = -6(k-1) / [k(2k-1)(2k-3)].
```

Any proof must expose signed cancellation at coefficient level before taking
norms.  The adjacent-profile triangle/CDV route refuted by M272 is excluded.

## Inputs to verify

- immutable M272, M276, and M279 artifacts;
- relevant M192/M195 channel-two prefix-response artifacts;
- relevant M217/M222 signed averaged-DE artifacts;
- relevant M248/M249 WBE/DE assembly artifacts.

Hashes and claimed statuses will be checked before reuse.  Disagreements are
reported rather than resolved silently.

## Proof workflow

1. Reconstruct the literal definitions of `E_u` and `Phi^D_u` and the exact
   coordinate index set from frozen sources.
2. Expand the Abel expression coefficient-by-coefficient, preserving phase,
   lag, kind, and collision labels.
3. Search analytically for cancellation within each literal coordinate or a
   coarser partition licensed by an exact identity.
4. If formulas are fixed and a boundary ambiguity remains, run at most one
   compact, predeclared exact finite falsifier after reading the experiment
   reference.  Finite scaling will be labeled empirical/exact-finite, never a
   proof.
5. Freeze either (a) a theorem proving CSBV, or (b) the narrowest exact
   reduction and its first standalone missing estimate/counterexample.

## Boundary and falsification checks

- odd `k=3` (empty interior sum except the endpoint contribution);
- smallest nontrivial interior case `k=5`;
- endpoint `u=k-1` and all collision cases;
- literal zero-mass and coincident-coordinate cases;
- sign conventions and both Abel representations.

## Exclusions

No work on CEBV, DOR, SET, FCL1, fixed edits, spectral gaps, mixing times, or
Terminal A/B.  No shared durable file will be edited.

