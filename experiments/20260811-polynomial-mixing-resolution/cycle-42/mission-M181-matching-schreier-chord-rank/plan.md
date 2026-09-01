# M181 plan: accepted-matching Schreier chord rank

## Objective

Resolve exactly the first open structural step after L-0259 for every accepted
nonempty ordered `d>=5` DPS matching subfamily: determine the realizable
relative-orientation chord-gain column space in its actual synchronized
signed-Hurwitz Schreier component, and decide whether each required fixed-
physical-endpoint tree offset belongs to that space.

## Target and conventions

The auxiliary target is the qualitative diagonal signed-Hurwitz orbit-lifting
problem on connected product-one length-`2d-2` transposition words modulo
simultaneous relabeling. The voltage group is
`W_s=F_2^s/<(1,...,1)>`. Permutations use the project convention
`(pq)(x)=p(q(x))`; chronological signed Hurwitz moves are
`R_j(a,b)=(b,b^{-1}ab)` and `R_j^{-1}(a,b)=(aba^{-1},a)`.

No global probability distribution, Markov kernel, mixing, or spectral-gap
claim is made in this structural mission.

## Mandatory reconciliation

Before proof work, hash-gate and read the frozen accepted artifacts for
M135/M137, M141/M143, M146/M148, M154/M158, M163/M164, M169/M172, and
M175/M176. Reconcile their exact hypotheses, physical representatives,
matching definition, quotient action, section/coboundary convention, and
word-order convention. Report any disagreement rather than choosing one.

## Proof strategy

1. Extract the exact accepted DPS matching tuple and the actual synchronized
   quotient component—not a Cartesian or generator-forgetting relaxation.
2. Seek explicit local closed signed-braid cycles whose canonicalization-sign
   gains generate `W_s`, with literal realizability in the M175 sense.
3. Separately express every required fixed-endpoint offset and prove it lies
   in the generated span.
4. If full rank fails, prove an exact invariant or counterfamily.
5. If neither closes, isolate a strictly narrower standalone realization
   lemma with a proved nontrivial step and a precise falsifier.

## Computation cap and falsifiers

- Minimal symbolic audits only; no broad `d=5` quotient enumeration or group
  closure.
- Finite checks may falsify formulas but cannot prove the all-`d` theorem.
- Do not infer qualitative connectivity from finite closure.
- Do not address polynomial word length before zero-membership is proved.
- No original heat-bath gap, mixing, or Terminal claim.

## Deliverables

`checkpoint.md`, `halfway_checkpoint.md`, proof or obstruction notes, only
compact reproducible artifacts if needed, a nine-field `report.md`,
`freeze_manifest.md`, and `SHA256SUMS`, followed by a request for fresh audit.
