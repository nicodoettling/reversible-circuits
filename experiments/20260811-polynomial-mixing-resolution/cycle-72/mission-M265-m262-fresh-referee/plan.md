# M265 Fresh Referee Plan for M262

Date: 2026-08-14

## Objective

Freshly audit M262's claimed arbitrary-rank counterfamily to the cyclic
path-row metric lemma (CPR), using the raw cyclic contexts frozen by M257 and
accepted by M260.  The audit will determine whether the family genuinely
refutes the stated `O -> C` CPR bound, whether it instead exposes an
under-specification in the old `O/C` root-seam-table (RST) notation, and which
claims remain open.

## Scope and claim discipline

- Ambient sampler target: the global fixed-length uniform law on
  `Omega(N,m)` for the lazy exact same-product `{3,4,5}` heat-bath kernel of
  `GOAL_SPEC.md`.  This audit concerns only a deterministic comparison-word
  lemma and makes no routing, spectral-gap, mixing-time, or Terminal claim.
- Multiplication/convention dependency: use M257's frozen raw cyclic CP
  contexts exactly as written; do not silently change cyclic order,
  substitution, deletion, or row orientation.
- Required family: every integer rank `rho >= 8`, with root/path/tree data,
  `E_4={6}`, nonroot edited node `a=6`, CP-5 old word, CP-2 substitution,
  complete-node deletion order, and the exposed row
  `W_6^6 S B_6^6 -> S`.
- Boundary guard only: independently instantiate `rho=8,9` to catch indexing
  or admissibility errors.  These finite cases do not prove the arbitrary-rank
  statement; the symbolic construction must do that.
- Preserve the possibility of a differently stated raw-context/IDL lemma if
  the old CPR fails.

## Audit sequence

1. Freeze-check M262's top digest and every payload hash before reading the
   mathematical contents.
2. Identify and hash the exact M257/M260 dependencies named by M262.
3. Reconstruct the family symbolically for arbitrary `rho >= 8`, checking the
   root, path, parent map, child order, path/nonpath status, and all referenced
   labels and ranks.
4. Expand CP-5 at `a=6`; apply the CP-2 nonroot substitution; then perform
   complete-node deletion in the stipulated order and verify the surviving
   row and its distance.
5. Run a tiny independent `rho=8,9` guard from a separately written checker
   or hand-audited table, recording machine-readable output if code is used.
6. Compare the counterfamily against the exact quantified statement of CPR,
   and separately audit what the old `O/C` RST notation did and did not
   specify.
7. Freeze an `ACCEPT` or `REJECT` report with numbered objections, dependency
   hashes, payload hashes, and the residual frontier.

## Expected failure modes

- `a=6` accidentally lies at the root or outside the path for a boundary rank.
- `E_4={6}` is incompatible with the claimed parent/child or complete-node
  order.
- CP-5 or CP-2 is paraphrased rather than used literally.
- The displayed row is present but not exposed after all required deletions.
- A distance-one row is mistaken for a refutation of a differently quantified
  or differently oriented CPR claim.
- Old `O/C` notation encodes more path/rank information than the audit notices.

