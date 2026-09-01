# M203 plan: structural all-d matching-route extension

## Objective

Determine whether M200's exact `d=5` every-color quotient-route theorem extends
structurally to M181's explicit width

```text
1 <= s <= 1+floor((d-1)/3),  d>=5,
```

without enumerating `Q_d` for `d>=6`.

## Immutable gate and proposed route

1. Verify full frozen manifests of M181/M183, M196/M198, and M200/M202.
   Never edit them.
2. Formalize M181's anchored block/filler word, the rooted DPS inverse, an
   arbitrary `H`-orbit representative, and one adjacent-value edit.
3. Test the indispensable locality premise: does the matched DPS target of an
   embedded word decompose into an edited active block plus unchanged,
   synchronized other blocks/fillers after arbitrary allowed relabeling?
4. If locality holds, prove a conditional block-product quotient-route lemma
   with exact hypotheses. If it fails, archive the first exact symbolic
   obstruction/counterexample and state the narrowest surviving condition.

## Computation cap and falsification

No `Q_d` enumeration is allowed for `d>=6`. A compact `d=6` rooted-DPS spot
check may test locality across the one-block-plus-two-fillers boundary. Stop
once a decisive exact counterexample or theorem hypothesis is identified.

## Scope boundary

Maintain the distinction between an ordinary quotient-route certificate and
the later stabilizer-voltage correction supplied qualitatively by M175 when
full rank applies. No polynomial quotient length, correction length, total
length, spectral gap, mixing, or Terminal claim is permitted without proof.

## Deliverables

Write this plan/checkpoint first, then immutable-gate and halfway checkpoints,
compact symbolic audit/results, proof or obstruction note, nine-field report,
freeze manifest/hashes, and fresh-referee request.
