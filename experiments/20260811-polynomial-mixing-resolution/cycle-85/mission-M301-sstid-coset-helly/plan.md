# M301 plan: SSTID finite-action coset-Helly frontier

Date: 2026-08-14 UTC.

## Scope and immutable gates

This mission works only in the minimal connected sector

```text
Z_d={w in Transpositions(S_d)^(2d-2): product(w)=id,
                                      support(w) connected}.
```

Permutations compose as `(pq)(x)=p(q(x))`; signed right-Hurwitz words act
chronologically, `w^(x;y)=(w^x)^y`.  The ambient project target remains the
uniform global fixed-length bridge and the exact lazy `{3,4,5}` heat-bath
kernel of `GOAL_SPEC.md`, but this mission proves no Markov-chain estimate.

Before fixing the candidate below, the frozen predecessor gates reproduced:

```text
M296 SHA256SUMS  9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f
M299 SHA256SUMS  1654bcd6319b3020fe49a34e54a9961b2687ba5daab107baca11873749065b8d
```

Every payload row in both manifests passes `sha256sum -c`.  M299 independently
accepts M296's exact residualization and explicitly leaves SSTID open.

## Accepted interface

For one actual M135 perfect-matching color, fix a reference selected
`H=Stab_(S_d)(d)`-orbit edge `Q_0`.  With `S=BStab_d` and M291's source and
target frames, M296/M299 prove

```text
C_Q=Trans_S(x_Q,y_Q),
intersection_Q F_Q
 =alpha_0;(intersection_Q C_Q);delta_0^(-1).
```

Projection to the finite Hurwitz action image preserves common nonemptiness
exactly, but does not control shortest literal braid length.  Pairwise
double-coset compatibility is distinct from a higher-arity intersection.

## Analytic candidate fixed before computation

The first natural finite-action shortcut is the following precise assertion.

> **Matching-transporter 2-Helly (MT2H).**  Let `M` be any perfect matching
> in the actual M135 orbit-incidence multigraph `B_(d,i)`.  For its actual
> selected `H`-orbit edges, if every pair of finite action fibers intersects,
> ```text
> K_P intersect K_Q != empty       for all P,Q in M,
> ```
> then the whole matching has a common finite action,
> ```text
> intersection_(Q in M) K_Q != empty.
> ```

If MT2H were true, coloring only M296's exact pairwise incompatibility graph
would discharge the nonemptiness half of SSTID.  It would still say nothing
about polynomial literal representative length.

This mission will first analyze MT2H as a coset statement: fibers are cosets
of varying point/two-point stabilizers, for which no general 2-Helly theorem
exists.  It will then run **one compact exact diagnostic only**, at `d=3`,
enumerating the finite signed-Hurwitz image, the actual `H`-orbit incidence
edges, all perfect matchings, and all fiber intersections.  The diagnostic is
used only to seek a strict actual-edge counterexample to MT2H (or to delimit
the first surviving lemma); it is not asymptotic evidence.

## Decision rule

- If an actual matching has pairwise-intersecting fibers but empty total
  intersection, freeze MT2H as **REFUTED (exact finite)** and state the next
  standalone requirement: a genuinely higher-arity refinement invariant.
- If no such matching exists at the fixed guard, do not infer MT2H.  Freeze
  the exact finite result and the first unresolved all-rank lemma, preserving
  the separate literal-length obligation.

No every-color route, rank lift, voltage, congestion, gap, mixing, or Terminal
claim is in scope.
