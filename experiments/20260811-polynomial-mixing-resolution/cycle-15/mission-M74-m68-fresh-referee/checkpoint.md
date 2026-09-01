# M74 checkpoint: M68 audit

## Frozen integrity

The frozen M68 report has the requested SHA-256
`96c52fdc8f6a07d51869b5bf83415b001a9c7e825e22f041c69836ae3435241d`.
All sixteen supporting hashes displayed in its field 8 also match.

## Proof checks completed

- The marked insertion/deletion identity and the normalized DYZ inequality
  give
  `E Z_int >= 6(d-1)/(d^2 k)` with no missing factorial.  The inherited
  recurrence is uniform for every `d>=2,g>=1`; at `d=2`, `C_g(2)=1` and the
  first exact normalized ratio is `1/12`.
- A fixed consecutive pair among `k` uniformly interleaved component
  occurrences is globally consecutive with probability
  `binom(m-1,k-1)/binom(m,k)=k/m`.  Consequently the report's
  `3/[Nm(m-1)]` marked-state probability is correct.
- The transposition-product three-factor fiber count is
  `D_N=M+6(N-2)+(N-2)(N-3)=(3N^2+N-12)/2`.  Combining the mark probability
  with one specified padded `H3` outcome gives exactly
  `theta_N=1/[2Nm(m-1)(m-2)D_N]`.
- In the two-component case the frozen phrase “support tree” must be read as
  “prefix join tree.”  The actual argument is valid: after deletion, the two
  minimal component join trees are joined by the first copy of the inserted
  cross edge, while the second copy is a cut.  A fixed tree has at most one
  edge across the component bipartition, leaving at least `N-2` safe cross
  edges into `F_N minus A`.
- The fixed-word translate-cover implication has the right orientation and
  constant.  Each prefix is bijective; `(j,t)` plus a charged directed edge
  recovers at most one source; there are at most `LD` such pairs.  A padded
  Hurwitz step has probability at least `1/[6(m-2)M^2]`, and a final safe
  square refresh has no larger load.
- The dense/partial dichotomy is correctly scoped.  Removing uniform macro
  mass `u` loses at most `u` from the whole-macro mean.  Sparse portions gain
  volume only over an `H_N`-radius window; the report does not infer a
  one-radius boundary from that fact.

## Independent reruns

Six deterministic reruns were written in this M74 directory.  After deleting
only `argv` and `elapsed_seconds`, every field matches its frozen counterpart:

```text
colored handle       path length 2, unequal adjacent marked edges
macro saturation     2 full / 47 partial / 41 missed macros
pointwise exit       90 c=3 and all 10 c=4 states have zero direct exit
square domination    762940 / 762940 dominated at N=5
two deletion         240 failures, all at component count 2
four null            37200 / 657610 distinct component words fail
```

The independent exact recurrence-normalization rerun through `d<=12` and
`k<=80` has zero failures.  These finite checks validate normalization and
the named counterexamples only; they do not establish asymptotic expansion.

## Provisional verdict

`ACCEPT`, subject to the final scope and artifact-hash pass.  The join-tree
terminology correction above is nonmaterial.  No M68 claim implies Terminal
A or Terminal B.
