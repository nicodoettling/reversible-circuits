# M129 checkpoint: recurrence audit passes, final freeze pending

Date: 2026-08-13 UTC.

## Status

The frozen M125 checksum set passes.  The supplied immutable hashes resolve to
the actual filenames `freeze_manifest.md`, `audit_recurrence.py`, and
`defect_recurrence.md`; no frozen file has been modified.

The algebraic audit currently finds no objection:

- selecting the unique one-colour block containing a root proves the stated
  `P_S` recurrence;
- the components of `pi_L join pi_R` give a unique rooted connected-component
  decomposition, proving the subtractive `C_S` recurrence;
- the bipartite incidence multigraph has `c` atom-edges and `L+R` block
  vertices, so connectedness plus `L+R=c` is exactly cyclomatic number one;
- substituting `R=c-L` into `j=d+R-L` gives the two factorials
  `(d+c-2L)!` and `(d-c+2L)!`;
- the cycle-type multiplicity and squared atom factors reproduce the accepted
  M113/M118 cell formula with no extra cycle-indexing factor;
- a key has `L,R>=1`, so the diagonal excludes `c=1` and gives defect range
  `0<=r<=d-2`.

## Fresh exact check

`independent_referee.py` imports no M125 module.  It independently implements:

1. literal ordered pairs of set partitions;
2. an indexed-subset root recurrence rooted at the greatest indexed atom;
3. an equal-size multiset recurrence rooted at the largest present cycle
   size, opposite M125's smallest-present root convention.

The first full run reported zero failures:

- 23 cycle types and 47,728 literal partition pairs through `d=6`;
- indexed and multiset recurrences for 58 cycle types through `d=8`;
- exact rows through `d=22`, all matching frozen M125;
- all 21 rows unimodal and ordinarily log-concave;
- every row `d=4,...,22` fails ULC;
- primitive `d=4` row `(627,1520,1113)`, ordinary margin `1612549`, and
  ULC margin `-481004`;
- weakest tested ordinary ratio at `(d,r)=(22,7)`, exactly matching the
  frozen numerator and denominator and approximately `1.0118053687`.

The checker is being extended only to record a direct comparison with M124's
independently frozen exact-key rows for `d=2,...,5`; M124's complete checksum
set also passes.  A final full run and report/freeze artifacts remain.

## Scope guard

The finite checks do not prove universal ordinary log-concavity or DEFECT
NO-VALLEY.  No projection gap, fixed-defect gap, `gap(A_d)`, handle-projection
gap, original `{3,4,5}`-chain gap, or terminal result is claimed.
