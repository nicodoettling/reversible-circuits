# M94 plan: balanced Abel asymptotic attack

Date: 2026-08-12. Scope: frozen M91/M93 balanced `H0` family only.

## Objective and exact target

Permutations compose as `(pq)(x)=p(q(x))`, with tuple factors multiplied
left-to-right.  For `n=3k`, odd `k>=3`, the target law is uniform on minimal
length-`n-1` transposition factorizations of `h=(0 1 ... n-1)`, and `bar K`
is M73's nonlazy rank-two pair-product kernel modulo conjugation by `h`.
For

```text
A_k=(0,k,2k),        B_k=(0,1)(k,2k),
eta_k=bar K(B_k,.)-bar K(A_k,.),
```

decide M91's balanced Abel collision inequality

```text
||bar K(eta_k/bar pi)||_(2,bar pi)^2 = O(k^-4)          (BA2)
```

if possible.  If `(BA2)` fails because of rare target orbits, prove or refute
the weaker direct signed bound `||eta_k bar K||_1=O(k^-2)`.

## Method

1. Re-express the localized four-step contrast through residual component
   sizes and exact Cayley completion counts, retaining the `J=1,2` channels,
   cyclic phases, orbit stabilizers, and all signs.
2. Derive a target-residual/Borel-convolution representation that exposes
   boundary and rare-orbit contributions.  Test specifically for a logarithmic
   divergence of the stationary `L2` contrast which may coexist with bounded
   signed `L1`.
3. Use deterministic exact or high-precision finite calculations only to
   falsify identities or guide the analytic decomposition; label all finite
   scaling as empirical.
4. Prove the strongest uniform inequality available without triangle-splitting
   the two channels.  If the last step remains open, isolate it as one sharper
   standalone summation or integral inequality.

## Falsifiable outcomes

- prove `(BA2)` with an explicit constant;
- prove a lower bound incompatible with `(BA2)` and determine whether direct
  signed `L1=O(k^-2)` survives;
- or produce a strictly sharper exact convolution reduction plus a rigorous
  partial bound/counterterm analysis.

## Failure modes and scope discipline

- No absolute values or separate estimates before combining both channels and
  the complete second row.
- No use of finite `k` values as asymptotic evidence.
- No generic-orbit replacement for the size-`k` orbit of `A_k`.
- No H0 gap, fixed-endpoint bridge gap, identity heat-bath gap, or Terminal
  conclusion without a separate proof.

Required deliverables are `checkpoint.md`, analytic notes, reproducible
scripts and machine-readable output if computation is used, a nine-field
`report.md`, and a final `SHA256SUMS` after cache cleanup.
