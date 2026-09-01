# M250 plan: exact RSMI+ metric interface

## Objective

Starting only from the locked Duchi--Poulalhon--Schaeffer source, accepted
M244 pruning theorem, immutable M240/M242 and M247 gates, prove every exact
RSMI+ clause stated in M247 Section 5, or freeze the first exact counterexample
or strict remaining lemma.

## Scope and labels

- Target: a deterministic combinatorial metric-interface theorem for the
  rooted-tree encoding; no Markov-chain target is asserted here.
- Status at initialization: **unresolved**.
- Allowed input: M244 Theorem 3.1 pruning; locked source definitions and the
  exact immutable gates named above.
- Forbidden inference: rejected RSMI, fixed edits, every-color/voltage claims,
  circuit length, spectral gap, mixing, or Terminal A/B.

## Method

1. Lock and hash the allowed artifacts; extract M247 Section 5 clauses and
   source conventions literally.
2. Derive a local side-token/interface recurrence, including cyclic root and
   sealed/open boundary behavior.
3. Check, clause by clause: open-only larger child; edited IDL-a endpoint;
   common nonchild `h_r^2`/disjoint endpoint; sealed closed transition/root
   equality; open-root four-block and unnamed-coordinate equality.
4. If all clauses hold, prove coordinate exhaustion and hence RSMI+ => IDL.
   Otherwise isolate the first false clause or strict missing lemma.
5. Only after the recurrence is fixed, optionally predeclare one tiny targeted
   falsifier; no broad rank census.
6. Freeze theorem/obstruction, report, manifest, and SHA-256 inventory, then
   request an independent referee.

## Expected failure modes

- cyclic root indexing differs from the linear interval recurrence;
- an off-path subtree contributes a boundary token not covered by pruning;
- sealing identifies a coordinate only after an unstated rotation;
- the four open-root blocks omit a named or unnamed coordinate;
- coordinate exhaustion silently assumes the rejected older RSMI.

## Computation policy

No finite scan is authorized at initialization. A tiny falsifier may be added
only after the exact recurrence and its tested clause/domain are written down.

