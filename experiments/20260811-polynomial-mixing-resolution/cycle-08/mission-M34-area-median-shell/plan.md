# M34 plan: area-median shell and action

## Exact target

Permutations are composed as maps with `(pq)(x)=p(q(x))`.  For `N>=6`, put
`m=2N-2` and let `F_N` be the connected full-support part of
`Omega(N,m)`.  For

```text
h_j=N-cycles(t_1...t_j),   Area=sum_(j=1)^m h_j,
```

choose an integer threshold `q_N` with conditional mass
`1/4<=Pr_F(Area<=q_N)<=1/2`.  The mission is to prove a universal
inverse-polynomial lower bound for the original lazy `{3,4,5}` heat-bath
conductance of this cut, or to prove a superpolynomial obstruction with exact
global mass and all block-length flows.

## Proof lanes

1. **Weighted shell enumeration.**  Derive or locate an exact recursion for
   minimal transitive identity factorizations with prescribed prefix-height
   area.  Audit whether the Cayley-tree/permutation Hurwitz-tree sampler makes
   the height path a tractable random object; do not assume a Catalan or tree
   lumping.
2. **One-step action.**  Classify length-two valleys in the transposition
   Cayley graph and prove, or finitely falsify, a same-product local lift to a
   peak.  Translate any lift into an actual `H_4` outcome with every kernel
   normalization.  Quantify exceptional maximum-height valleys and the number
   of actionable valleys.
3. **Isoperimetric injection.**  If local lifts exist, seek an injective or
   bounded-multiplicity map from the lower area tail to its width-12 shell.
   A polynomial diameter or an iterated polynomial adjacent-layer ratio is
   insufficient.
4. **Terminal-B audit.**  If exact/sampled layers suggest a phase separation,
   define the threshold explicitly and prove both stationary orientation and
   complete `Q_3+Q_4+Q_5` boundary flow before making any asymptotic claim.

## Computation standard

Exact enumeration or bounded orbit closure is used only to falsify a named
universal local-action or layer-shape lemma.  Every script records the commit,
Python version, deterministic seed metadata, parameters, exact counts, and
the claim tested.  Finite spectra or apparent scaling will not be interpreted
as a universal theorem.

## Expected failure modes

- Area layers are already nonunimodal at `N=5`; no unimodality shortcut.
- A word at `N=6` has zero one-step exit from `F_N`; no pointwise macro escape.
- A valley need not admit an upper diamond, or upper diamonds may have
  exponential preimage accumulation.
- The Duchi--Poulalhon--Schaeffer bijection preserves counting but has no
  cited local-move or prefix-height intertwining.
- Conditional mass at a discrete quantile may jump across `1/2`; existence
  and orientation of the requested threshold must be proved, not assumed.

The halfway checkpoint will freeze the strongest exact action/shell fact and
the first remaining standalone implication.  The final report will follow the
required nine-field schema.
