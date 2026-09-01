# Mission M262 plan: cyclic path rows

## Objective

Starting only from the freshly accepted M257 raw contexts CP-1--CP-6 and
their locked predecessors, prove or sharply reduce the first open cyclic
path-row lemma (CPR).  The target is the literal metric simplification of the
actual token word through the reversed base and every strict internal
ancestor: `O -> O` on strict descents and `O -> C` at the first ascent, with
the claimed side counts and rank-stable black endpoints.  The rank-dependent
`a=1` root row is excluded and remains RST.

## Scope and immutable inputs

- **Combinatorial target:** deterministic DPS LIFO closure of the ordinary
  odd edit; no probability law or Markov kernel is used here.
- **Allowed inputs:** M240/M242, M244/M247 in the accepted Theorem 3.1 scope,
  M250/M254, M257/M260, and the locked DPS source.
- **Required distinction:** an `O` or `C` input is the full side-token
  word/state, not a one-bit summary; canonical off-path subtrees are nonroot.
- **Required proof form:** arbitrary-rank token induction before any finite
  check, including cyclic-wrap children and exhausted label sets.
- **Stopping line:** before the rank-dependent `a=1` row and final root
  completion reserved for RST.

## Method

1. Verify all predecessor manifests and the locked DPS digest.
2. Reconstruct the exact token semantics and M250 equations (4.1)--(4.5),
   retaining side identities, stack order, and named black endpoints.
3. Expand CP-5 analytically to identify the exact base token word and its
   exposed set `E_v`.
4. Derive a literal arbitrary-rank transducer for CP-2--CP-4 with one retained
   path-child hole.  Prove the `O -> O` descent and `O -> C` first-ascent
   rows, or stop at the first exact obstruction.
5. Audit inherited low labels outside `E_v` and the cyclic post-wrap sector.
6. Only after the proof recurrence is fixed, use a minimal finite check if it
   can falsify a universal row identity; finite interpolation is forbidden.
7. Freeze the strongest proved theorem or standalone residual lemma, with the
   exact remaining RST tables and no downstream inference.

## Expected failure modes

- The state tag may omit stack-order data needed to determine a row.
- A post-wrap off-path block may alter the number of side tokens between the
  retained hole and its closer.
- The first ascent may have more than one possible named black endpoint,
  depending on the literal input word.
- Base simplification may fail to initialize exactly `O(E_v)` for a boundary
  child configuration.

## Verdict vocabulary

`proved`, `refuted`, or `unresolved reduction`.  CPR does not imply RST,
RSPT, IDL, routing, a gap, mixing, or either Terminal.
