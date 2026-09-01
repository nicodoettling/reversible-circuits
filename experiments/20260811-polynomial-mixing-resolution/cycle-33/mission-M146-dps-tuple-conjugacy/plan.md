# M146 plan: DPS tuple-conjugacy invariant

Date: 2026-08-13 UTC.

## Objective

Continue the accepted M135/M137 conflict-coloring reduction and the
M141/M143 multisource common-parity negative sharpening.  For a subfamily of
sources, package factor position `j` as an aligned tuple

```text
x_j=(u_j^1,...,u_j^s) in P_(d,s) <= S_d^s.
```

A common signed Hurwitz braid acts by Nielsen transformations on the ordered
factor tuple, so it preserves the multiset of conjugacy classes of the
individual `x_j` inside the generated group `P_(d,s)`.  Determine whether
every M135 matching preserves this source-versus-target multiset, or whether
the matchings admit a polynomial refinement by a complete polynomial-size
descriptor for this necessary invariant.

## Target, convention, and scope

For `d>=2`, `m=2d-2`, the auxiliary target is uniform on

```text
Z_d={(t_1,...,t_m):t_1...t_m=id,
                         support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed factors multiply
left-to-right.  Signed right-Hurwitz moves are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

This mission studies only a necessary invariant for simultaneous DPS braid
realization.  It proves no common braid, polynomial braid length, gap, or
Terminal conclusion.

## Work program

1. Reconcile and cite only the frozen accepted scopes of M135/M137 and
   M141/M143.
2. Prove the exact conjugacy classification in
   `P_(d,s)={(g_1,...,g_s):sgn(g_1)=...=sgn(g_s)}` for the relevant all-odd
   tuples of transpositions, including the exceptional centralizer/parity
   cases.
3. Translate that classification to a finite descriptor for the multiset of
   aligned factor-tuple conjugacy classes.
4. Test a named, bounded exact question: the deterministic M135 matching at
   `d=3` as calibration and, only if feasible without broad enumeration, the
   smallest `d=5` matching/color counterexample search.  Cap all searches and
   record exact bounds.
5. Freeze either a universal preservation/refinement theorem or the smallest
   exact falsifier, with the first remaining unproved step stated precisely.

## Expected failure modes

- Conjugacy in `P_(d,s)` may split an ambient `S_d^s` class according to the
  parity image of the common centralizer.
- A matching can pass all generated-subgroup tests while changing this finer
  multiset.
- Exact `d=5` construction may be too large; in that event only a named,
  capped local/orbit computation will be attempted and the universal status
  will remain proof-driven.
- Preservation of the multiset is necessary but not sufficient for a common
  signed braid.

## Reproducibility and ownership

All scripts are deterministic (`seed=null`), use Python 3 from the repository
environment, and record exact caps and dependencies.  Owned files are only
under this mission directory.  Final artifacts will include a theorem/proof
or exact falsifier, machine-readable output where computation is used, a
nine-field report, freeze manifest, and SHA-256 inventory.
