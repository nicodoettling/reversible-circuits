# M146 checkpoint

Date: 2026-08-13 UTC.

## Reconciliation complete

- Read the project skill and required core sources.
- M135/M137 is accepted only for the polynomial orbit-incidence conflict
  coloring (`chi<=d` for `d=3` and `d>=5`, uniformly `chi<=d^6`); it does not
  provide simultaneous realization.
- M141/M143 is accepted only for the `d>=5` theorem that every nonempty
  subfamily of a matching has source and target aligned generated subgroup
  `P_(d,s)`; this rules out generated-subgroup invariants but not tuple
  conjugacy classes or action-coset obstructions.
- The inherited sandbox intermittently fails filesystem commands with
  `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`; read-only
  reconciliation used the approved escalated path.  No predecessor file was
  modified.

## Exact claim now under attack

For an M135 matching subfamily `I`, define at position `j`

```text
x_j=(u_j^q)_(q in I),   y_j=(tau_i(u^q)_j)_(q in I).
```

Every `x_j,y_j` is all-odd and lies in `P_(d,|I|)`.  Test whether the source
and target multisets of `P_(d,|I|)`-conjugacy classes are equal.  The first
proof obligation is the exact criterion for two all-odd transposition tuples
to be conjugate inside `P_(d,s)`, rather than merely in `S_d^s`.

## Status labels

- Preservation under a common signed braid: **proved necessary** (Hurwitz
  moves permute factors and conjugate one factor tuple by another).
- Exact `P_(d,s)` conjugacy classification: **proved**. An ambient product
  class splits into `2^max(r-1,0)` classes, where `r` is the number of
  coordinates with distinct-odd cycle type.
- Preservation by every M135 matching for `d>=5`: **proved**, using the
  accepted M141/M143 equality of both aligned generated groups with
  `P_(d,s)`. All aligned factor tuples are all-odd transposition tuples and
  hence occupy one class.
- Polynomial refinement by this descriptor: **vacuous**; the descriptor is
  constant and no refinement is required.
- Simultaneous braid realization: **still unresolved**. Passing this
  necessary invariant is not sufficient.

## Exact bounded checks completed

- One representative of every cycle type in `S_d`, `2<=d<=7`, confirms the
  centralizer-parity criterion.
- Full `P_(d,s)` conjugacy-orbit enumeration for `2<=d<=4`, `1<=s<=3`, has
  zero splitting-formula failures and exactly one all-transposition class.
- Explicit even transporters were checked for every ordered pair of
  transpositions through `d=7`, with zero failures.
- All nine deterministic `d=3` M137 matchings and all nonempty subfamilies
  were checked. Among the 93 subfamilies whose literal source and target
  groups agree, all 93 class multisets agree; the other 42 already change the
  literal generated subgroup.
