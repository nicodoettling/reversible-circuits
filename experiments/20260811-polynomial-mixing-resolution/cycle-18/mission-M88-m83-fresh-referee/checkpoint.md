# M88 checkpoint: provisional acceptance

Date: 2026-08-12.

## Frozen provenance

The assigned M83 hashes match exactly:

```text
report.md
6e7a42b0166dab0c1c7a46cb65844258ff8c5887de4d2e488d9cdd8749d06eee

freeze_manifest.sha256
87866cd283f860bb87bb0eeed7973daa5d78646ded5bb410114e6520b8a2d941
```

Running the manifest check from the repository root passed all 24 entries.
The initial check from the mission directory failed only because the manifest
contains repository-relative paths; rerunning under its intended path
convention resolved every entry.

## Provisional verdict

**ACCEPT, with zero material objections found so far.**

Fresh exact enumeration at `k=3,5` reconstructed all admissible rank-two
targets and both source rows without importing M83/M73 code.  It found:

```text
k  support  K_A(F)  K_B(F)                  selected B mass
3      336       0  1732/5625               832/5625
5     3185       0  119367232/730731375     1333643264/19729747125
```

Both rows normalize to one.  The selected masses equal the closed `p_k`
formula exactly.  The direct enumeration also checks strict adjacency,
cyclic invariance of `F_k`, every selected target's membership in `F_k`, two
ordered micro-lifts per selected double, no duplicate raw targets, and the
long-chord split multiplicities

```text
#{e: smaller split=s}=s          for 1<=s<=k-2,
#{e: smaller split=k-1}=2(k-1).
```

The Borel identity and all three explicit lower-bound factors have also been
derived independently.  The final audit will spell out the dominated
Riemann-sum argument and the full A-side zero-event proof.

## Scope guard

The theorem refutes only a universal `O(1/n)` bound on **one-step** local
influence along strict endpoint-sharing edges.  It neither proves nor refutes
the open `O(n^-2)` two-step inequality, and it has no direct H0-gap,
fixed-endpoint-gap, identity-heat-bath-gap, or Terminal A/B conclusion.
