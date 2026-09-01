# M59 plan: fixed join-tree internal/rejected-exit red team

## Exact target

Use `(pq)(x)=p(q(x))`, `N>=4`, `m=2N-2`, and the literal lazy exact
same-product `{3,4,5}` chain.  For a labeled tree `T` on `[N]`, define

```text
F_N(T)={w in F_N:T_J(w)=T}.
```

Study the rejected-exit restriction of `K` to `F_N(T)` and the corresponding
mean-lift/internal-flow problem.  Either prove a universal inverse-polynomial
restriction or mean-lift bound, or construct an explicit infinite internal
cut with full conditional and global mass plus all `H3,H4,H5` exit flow.  A
slow auxiliary restriction alone is not Terminal B for global `K`.

## Structural route

1. Use the exact fixed-tree automaton from M47: a prefix state is
   `(permutation p, accepted tree-edge set S)`.  A factor internal to a
   component of `(V,S)` leaves `S` fixed; the unique unused `T` edge joining
   two components enlarges `S`.  Length `2N-2`, identity endpoint, and full
   `S=E(T)` characterize the fiber.
2. Refine the M49 strand coordinate: for a tree leaf `v`, fixed deleted base
   word and two null positions support at most `(N-1)^2` lifts.  Determine
   whether local `H3/H4/H5` moves mix these insertion-coordinate histories
   and null positions with a polynomial rate rather than only counting them.
3. Seek a decomposition over deleted-leaf base words, null positions, and
   insertion histories.  Avoid routing all states through an adjacent-square
   hub unless its congestion is explicitly polynomial.

## Independent Terminal-B lane

Test cuts based on the order/chronology of joins and cuts, especially:

- the rank of a distinguished tree edge among the `N-1` join events;
- the first-return/null-position separation of a leaf strand;
- linear-extension or prefix-subtree balance of the accepted-edge process;
- doubled-tree/aligned chronology only as a calibration, not a hub.

For any asymptotic proposal, calculate the actual fixed-tree word weights,
global mass orientation after embedding into `Omega`, and every `H3,H4,H5`
boundary contribution.

## Exact bounded falsification

Enumerate the smallest decisive fixed fibers: every labeled star/path shape
at `N=4` (sizes 186 and 178) and representative `N=5` shapes if feasible.
Build the exact rejected-exit support graph, including all same-product
outcomes for `r=3,4,5`, and test:

```text
UNIVERSAL RESTRICTION IRREDUCIBILITY:
for every N>=4 and every labeled T, K restricted to F_N(T) is connected.
```

A finite disconnect refutes that named lemma; finite connectivity does not
prove it.  Record exact commands, commit, Python, no random seed, component
sizes, and the statistic shells crossed by each block length.

## Expected failure modes

- Rejected-exit restrictions may be disconnected even though full `K` and
  the tree-saturated projection have polynomial escape.
- Null positions may move only after changing the join tree, making a fixed-
  tree restriction the wrong object for mean lift.
- A chronology trace can be slow in the restriction but leak rapidly through
  tree-changing `H4/H5` moves in global `K`.
- A deterministic adjacent-square normalization can have exponentially small
  stationary mass and exponential congestion.
