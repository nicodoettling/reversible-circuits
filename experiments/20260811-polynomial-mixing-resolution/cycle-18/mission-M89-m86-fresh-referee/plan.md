# M89 plan: fresh referee of frozen M86

Date: 2026-08-12.

## Objective

Independently audit the frozen M86 signed marked-cover theorem and issue one
binary `ACCEPT` or `REJECT` decision with numbered material objections.  The
frozen M86 files must not be modified.

## Frozen inputs

The three user-specified SHA-256 values will be checked before proof review:

```text
5c09b466fc404ee7145f87125456f23e539fffb1e8c0aeff0264ded32a78a6ff  report.md
c147163c711ba06b82b8248d0d86fe4ef6ecd7d8b8ae9c2014944e1bc7e25682  signed_cover_theorem.md
34e1d07d5cda1188dc757d3eb9b6bd32ff5c6daddef5471bdb9f2a124e7d5cbd  SHA256SUMS
```

## Audit obligations

1. Check the accepted M13 Classification-H hypotheses and whether the stored
   `50 d k^3` signed braid is genuinely state-independent and polynomial.
2. Check generatorwise relabel equivariance.
3. Check the `rho_k` convention, stable pair sort, endpoint order, family
   cardinality, and mean/maximum lengths.
4. Check the marked target against M75, including `p_H`, terminal refresh,
   restricted source-class scope, and wrong-index first exits.
5. Check indexed-law success probability and literal inverse-prefix
   actual-edge recovery.
6. Redraw/audit Lemma 7.1 for positive and inverse generators, including one
   or both marked collision occurrences, and separate the local algebra from
   the global pullback induction and cover-homology consequence.
7. Check all boundary and terminal-scope statements.

## Independent computation

Run the smallest deterministic family/algebra checks into this owned
directory.  Add a focused verifier if needed for any disputed universal local
identity.  Computation is falsification support only; it cannot replace the
global topological proof.

## Deliverables

Write a halfway `checkpoint.md`; a nine-field `report.md` containing exact
decision, audit argument, accounting, dependencies, first unresolved step,
strongest self-attack/numbered objections, calibrations, reproduction, and
final classification; machine-readable rerun output where used; and a frozen
manifest plus SHA-256 list.  Remove bytecode/cache files and report all owned
artifacts.
