# M28 plan: full-support one-step shell

## Objective

For `N>=5`, `m=4N^3+4`, and

```text
U={w:c(w)>=2},
F={connected full-support y:K(x,y)>0 for some x in U},
V=U union F,
```

determine `F` exactly, prove whether `V` is proper, orient its global
stationary mass, and bound the boundary flow of the original lazy exact
`r=3,4,5` chain.  Multiplication is `(pq)(x)=p(q(x))`.

## Exact characterization to prove

Let a crossing occurrence for a vertex bipartition be a factor whose two
endpoints lie on opposite sides.  Prove

```text
V={w: for some nontrivial vertex cut, all crossing occurrences
      lie in one interval of at most five positions}.
```

The forward direction uses the update window from a disconnected predecessor.
For the converse, the outside product lies in the cut subgroup; parity and
transposition length give an internal length-five replacement with the same
product.

## Counting and boundary strategy

1. Upper-bound `|V|` using length-six covers of the witness intervals.  The
   even outside length permits the audited central-trace bound for every cut.
   Sum all cut sizes with factorial weights, retaining the dominant isolate
   cut rather than paying a raw `2^N` loss.
2. Construct many boundary sources using one isolated label `z`, the prefix
   `(s,q,q,q,s)` with `s=(z,1)` and `q=(2,3)`, and a dense `q`-endpoint tail
   on the other `N-1` labels which remains connected after deletion of any
   five consecutive factors.
3. Prove such robust tails comprise a constant fraction using an explicit
   parity-aware character-ratio lower bound and a cut/window union bound.
4. In the `H_5` window beginning at the second `s`, push that transposition
   through the first four tail factors by four right Hurwitz swaps.  Its new
   occurrence is at position nine, while the first remains at position one.
   The target is deletion-robust and lies outside `V`.
5. Include the exact `1/[6(m-4)F_5]` transition probability,
   `F_5<=M^4`, and retain all other `Q_3,Q_4,Q_5` flow as nonnegative.

## Expected failure modes

- Macro reachability alone does not characterize `F`; the unchanged outside
  support is essential.
- Removing five factors changes parity of the outside endpoint; use a
  length-six cover for the shell upper bound and an odd-endpoint Fourier bound
  for tails.
- A raw union over all cuts loses `2^N`; retain subgroup factorials and the
  exponential penalty by cut size.
- Repairing one witness cut need not make a word robust.  Demand a tail which
  stays connected after every five-position deletion and retain two separated
  edges incident to `z`.
- Finite examples cannot establish properness or conductance.

## Computation

No computation is planned.  All estimates are exact or elementary
asymptotic inequalities valid for every `N>=5`.
