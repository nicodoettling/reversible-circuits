# M269 plan: directional path-row transducer

## Objective

Resolve the first open routing obligation left by M262/M265: replace the
refuted bare two-state `O -> C` cyclic path-row transition by an actual-token,
direction-sensitive frontier description.  At minimum distinguish `O^-`
(`a<v`) from `O^+` (`a>v`), and refine the literal state further if the word
forces it.

## Locked inputs

- M250/M254 metric pruning and accepted literal-distance conventions.
- M257/M260 raw cyclic contexts CP-1--CP-6 only; CPR and RST remain separate.
- M262/M265 arbitrary-rank counterfamily refuting the first-above-`v` bare
  `O -> C` transition.

Exact source paths and hashes will be recorded in `checkpoint.md` after the
source-lock audit.

## Work plan

1. Reconstruct the actual cyclic word and all six accepted local contexts.
2. Parameterize each path-row by the relative order of `a`, `v`, its path
   neighbors, and the exposed successor/predecessor tokens.
3. Derive a deterministic literal frontier transition table, or isolate a
   smallest all-rank family showing that any proposed finite state is
   insufficient.
4. State the strongest proved internal path-row theorem ending strictly before
   the rank-dependent `a=1` row.  Keep RST separate.
5. Use at most a tiny, predeclared finite guard after the analytic derivation.
6. Freeze a theorem or obstruction, the exact first open lemma, manifest, and
   SHA-256 inventory; request a fresh audit.

## Claim discipline

This mission will not infer IDL, all-rank routing, a routing-length bound, a
spectral gap, polynomial mixing, or a terminal conclusion.  It will not claim
that `O^-`/`O^+` is sufficient without a complete literal proof.

## Expected failure modes

- Direction alone may not encode whether the exposed token is `B_a^v`,
  `W_a^v`, `B_v^a`, `W_v^a`, `S`, `S_A`, or `S_C`.
- The cyclic seam may preserve a second open frontier not seen in the edited
  five-token neighborhood.
- The transition may depend on the predecessor/successor of `a` in canonical
  child order, forcing an unbounded label parameter but possibly only a finite
  order type.
- A local row theorem may hold while the separate root-seam transition fails.

