# M220 plan: rooted-contour correction recurrence or first obstruction

## Objective

Determine whether M214's finite rooted-contour correction key extends from
the `d=5 -> 6` one-leaf template to the next rank, including the edits that
were new at `d=6`.  The primary target is an analytic local identity for the
DPS boundary closure and its chronological signed-Hurwitz correction.  If the
finite key fails, freeze the first exact same-key incompatibility and reject
only that proposed descriptor.

## Audited object and convention

There is no probability distribution or Markov kernel in this mission.  For a
tree `T` on `[d]` rooted at leaf `d` adjacent to attachment vertex 1, define

```text
pi_d=(2d-3,2d-2 | 1,2 | 3,4 | ... | 2d-5,2d-4),
E(T)=T union {{1,d+1}},
pi_(d+1)=(2d-1,2d | 1,2 | ... | 2d-3,2d-2).
```

For every old edit `1<=i<=2d-3`, compare

```text
N_(T,i)=F_d(T,s_i pi_d)(0,d)(0,d),
A_(T,i)=F_(d+1)(E(T),s_i pi_(d+1)).
```

Signed right-Hurwitz generators act chronologically by

```text
R_j(a,b)=(b,bab),       R_j^-1(a,b)=(aba,a).
```

## Source lock

Before substantive dependence, verify every entry and top inventory digest in
frozen M203/M205, M208/M212, and M214/M218.  Never edit predecessors.

## Analytic-first program

1. Express the rooted plus-mirror DPS closure under the one-leaf extension in
   terms of its boundary half-edge pairings and identify exactly which factor
   labels can change after an adjacent-value edit.
2. Derive symbolic Hurwitz transport identities for a corrected endpoint,
   including the final old-label edits `i=2d-4,2d-3` that were not in M214's
   inherited `d=5` table.
3. State a candidate all-rank descriptor extending late ancestor, initial
   direct-child run, and the edit-5 exceptional path.  Do not call it complete
   before an induction or a complete counterexample test.
4. Only after the symbolic derivation, perform a compact exact `d=6 -> 7`
   check.  Generate rooted trees directly; do not enumerate `Q_6`, `Q_7`, or
   search for correction routes.
5. If the descriptor fails, archive the lexicographically first pair of
   trees/edits with the same declared key but incompatible required behavior.
   A no-go applies only to that key/schedule claim.  If it survives, prove the
   strongest bounded finite schedule family justified by the identities and
   check, without extrapolating beyond a valid induction.

## Exact obstruction criterion

For a proposed descriptor class and its claimed common chronological word,
one failed literal endpoint replay refutes that word.  A stronger same-key
obstruction requires two rows sharing the key for which no single candidate
behavior allowed by the analytic statement can serve both; bounded route
search misses are not negative evidence.  Prefer an explicit symbolic factor
mismatch or complete finite action invariant.

## Scope exclusions

No quotient-state enumeration or route search; no every-color or arbitrary
Hurwitz-representative theorem; no voltage-corrected or total route-length
bound; no spectral-gap, polynomial-mixing, or Terminal claim.

## Deliverables

Immutable/source checkpoint, halfway checkpoint, symbolic transport notes,
deterministic checker and machine-readable results, exact theorem or first
obstruction, nine-field report, freeze manifest, `SHA256SUMS`, and a request
for fresh immutable audit.

