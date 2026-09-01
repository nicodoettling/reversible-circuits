# M259 Plan — Fresh Referee of M256

## Objective

Independently referee the immutable M256 synthesis. Verify hashes and cited
predecessor inventories, then audit only the stated conditional implication
chain from full DV plus accepted DE through WPCR, SCBR, BR/BIR, and the
affine-kind transfer to the physical prefix-cycle-sum conclusion.

## Scope and prohibitions

- Treat every M256 and predecessor artifact as immutable.
- Check all parameter translations, especially `n=3k` versus `K/n` notation,
  and every equivalence direction used in the synthesis.
- Confirm that PCS does not imply FCL1/A_k, and that FD-bound / the M168
  minority-sign issue remains separate.
- Do not attempt DV, FD, a spectral gap, polynomial mixing, or a Terminal.
- Use only a compact exact-algebra checker if a mechanical check is needed.

## Method

1. Read the mandated source-of-truth documents and relevant proof artifacts.
2. Recompute the full SHA-256 inventory and top digest for M256, expected
   `f55b7092a1cc079a8c2d46e978f42772b7c3b5d1747cede45c34d38547524261`.
3. Verify every cited predecessor inventory/digest before relying on it.
4. Re-derive each implication and record any missing hypothesis, wrong
   normalization, unjustified equivalence, or overclaim.
5. Issue a binary ACCEPT/REJECT verdict with a complete objection list and
   frozen artifact hashes.

## Expected failure modes

- An unstated use of PCR or the unresolved J1-PCR term.
- Loss of a singleton/first-difference boundary term in the WPCR-to-SCBR step.
- A one-way estimate presented as an equivalence.
- A factor of three or symbol collision in the `n=3k` translation.
- Incorrect promotion from PCS to FCL1/A_k or absorption of FD-bound.

