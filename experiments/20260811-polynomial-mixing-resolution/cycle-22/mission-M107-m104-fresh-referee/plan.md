# M107 plan: fresh referee of M104

Date: 2026-08-12 UTC  
Repository commit at start: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`  
Owner: M107 only  
Verdict vocabulary: `ACCEPT`, `ACCEPT WITH CORRECTIONS`, or `REJECT`

## Objective and declared target

Independently referee the frozen M104 fixed-cut partial-fiber decomposition for the exact M97 lift. The declared target law is the M97 lifted stationary law on marked admissible cuts,

```text
tilde_pi(w,j)=pi_d(w)/ell(w),
```

with permutation convention `(pq)(x)=p(q(x))`, tuple factors evaluated left-to-right, and M97's half-lazy signed Hurwitz kernel and exact lift normalization retained literally.

This mission will not edit M104, infer a polynomial gap from finite enumeration, assume quantitative Classification H, route through a canonical word, or claim M92/full-kernel/Terminal completion.

## Claims under test

1. Every supplied M104 payload hash and every entry in its checksum manifest is exact.
2. At fixed realizable `kappa=(j,p,Q_L,Q_R)`, the raw word fiber is an exact product with the stated component factor counts and unicyclic incidence identity.
3. The handle variables have the correct side dependence:
   `r_L(u)=j-b(uv)+1`, `r_R(v)=h(uv)-j`, and
   `ell=r_L+r_R-1`, yielding the exact integral product mixture for `1/ell`.
4. Literal internal signed Hurwitz moves preserve the fixed key and admissibility, while every nontrivial seam proposal changes the key or leaves the admissible lift.
5. The raw/lifted edge-flow and variance comparisons imply the stated `D^3` restricted-gap loss.
6. The two-side M05 shuttle comparison has valid source recovery, two retained color slots, scan normalization, path lengths, metadata bounds, congestion, and final constants `420D^10` and `420D^13`.
7. The generic projection decomposition proves `gap(L)>=alpha beta/7`, hence only the conditional bound `gamma_1>=Gamma_0 beta/(2940D^13)`.
8. The explicit `kappa_e` cell has the claimed kernel identity, including the `d=2` convention, and creates exact same-size circularity rather than an induction.

## Method and parameters

- Read the required skill, `HANDOFF.md`, `GOAL_SPEC.md`, sampling and experiment references, and only the frozen M05/referee, M92/M95, M97/M101, and M104 artifacts needed for this audit.
- Verify frozen files byte-for-byte before drawing conclusions.
- Re-derive each probability and constant from the definitions, recording numbered objections or corrections even if the final verdict is acceptance.
- Build a no-import independent exact checker in this directory and exhaustively rerun the smallest decisive cases `d=2,3,4`. Finite results are falsification evidence only.
- Write a halfway checkpoint, machine-readable results, a nine-field final report, a freeze manifest, and checksums. Run cache, whitespace, and shared-worktree audits.

## Expected failure modes

- A frozen hash mismatch or silent post-freeze edit.
- Prefix/suffix dependence reversed in the handle-width identity.
- Conditioning that fixes less than the claimed independent side data.
- A seam proposal that stays nontrivially inside a fixed cell.
- A missing stationary-flow, laziness, scan, or identity-slot factor.
- Non-injective source recovery in the generalized shuttle map.
- An unjustified PSD/compression or between-cell mean estimate in the `1/7` decomposition.
- The `kappa_e` cell failing for `d=2` or failing to be exactly same-size.
- Treating unresolved `Gamma_0(d)` or `beta(d)` as quantitatively controlled.

## Checkpoints

- [in progress] Required-source and frozen-hash audit.
- [pending] Independent algebra/constant audit and halfway checkpoint.
- [pending] No-import exact `d<=4` falsification audit.
- [pending] Nine-field report, freeze manifest, checksums, and final verdict.
