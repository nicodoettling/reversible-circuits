# M194 plan: efficient exact Q5 stabilizer orbit

## Objective

Decide synchronized quotient-component membership for all 54 named `d=5`,
width-two targets using M191's immutable exact 8,400-point action. Replace the
stalled generic Magma stabilizer with a direct Schreier-transversal algorithm.

## Target and conventions

The exact finite target is the diagonal signed-Hurwitz orbit of source IDs
`(16,0)` in `Q_5^2`. The fourteen frozen action permutations are ordered by
symbols

```text
1,2,...,7,-1,-2,...,-7.
```

They act on the right and braid words are chronological. For a BFS tree word
`t_x` taking source first ID `16` to `x`, each generator `g` gives the
Schreier loop

```text
t_x g t_(xg)^(-1).
```

It fixes first ID 16. Apply these loops directly to the second-coordinate
action and BFS only the orbit of second source ID 0.

There is no probability distribution or Markov kernel in this structural
finite mission.

## Immutable gate and method

1. Verify the complete M191 manifest and action digest before use.
2. Recheck all action rows are bijective and positive/negative pairs inverse.
3. Build a BFS transversal on all 8,400 first-coordinate states.
4. Stream all `8400*14` Schreier loops as induced transformations of second
   coordinates; retain only those that enlarge its orbit, then close exactly.
5. For each target, reduce by the inverse tree word and decide exact membership.
6. Archive chronological route words for positives. For negatives archive the
   adjusted ID, complete orbit bitmap/digest, and closure under every Schreier
   loop.
7. Directly replay every positive route in the frozen action.

## Cap and exclusions

Cap wall time at five minutes and memory at a modest level. If exact closure
does not finish, terminate and freeze INCONCLUSIVE. Do not enumerate `Q_5^2`,
rerun generic Magma stabilizers, or infer anything all-`d`, every-color,
asymptotic in route length, spectral, mixing, or Terminal.

## Deliverables

Write a halfway checkpoint, proof note, efficient checker and exact JSON,
nine-field report, freeze manifest, and hashes. Final verdict is ACCEPT,
REJECT, or INCONCLUSIVE for this exact finite classification.
