# M51 plan: original-`K` leaf-count and degree-profile cuts

## Exact target

Use `(pq)(x)=p(q(x))` and the exact lazy `r={3,4,5}` same-product heat bath.
At `N>=4,m=2N-2`, let `F_N` be the minimal connected full-support identity
macro and `T_J(w)` the prefix join tree.  The primary distinct cut is

```text
L_(N,q)={w in F_N: number_of_leaves(T_J(w))>=q},
2<=q<=N-1.
```

Either prove a uniform inverse-polynomial two-sided conductance lower bound
for every nontrivial threshold under the original global chain, or construct
a literal Terminal-B sequence with exact stationary mass and complete
`H3+H4+H5` boundary flow.  Do not identify the actual join-tree law with an
auxiliary uniform plane-tree or parking law.

## Main proof attempt

1. Use the M49 strand-deletion map, but reprove every consequence needed here:
   deleting a join-tree leaf gives a word in `F_(N-1)`, exact tree `T-v`, and
   deletion-fiber multiplicity at most
   `binom(2N-2,2)(N-1)^2` per deleted label.
2. A tree-leaf deletion changes leaf count by `0` or `-1`.  Therefore every
   state above threshold `q` maps to the `(N-1)`-label tail at `q-1`, giving
   an exact weighted threshold-count inequality.
3. Reverse this with overlap-free adjacent-square insertions.  A leaf
   attachment never decreases the leaf count; if the base has exactly `q-1`
   leaves, attaching to any nonleaf raises it to `q`.  Audit the extreme
   `q=N-1` star case, where there is exactly one allowed attachment.
4. Refresh the inserted square through one exact padded `H3` outcome.  Track
   laziness, block-size choice, window choice, and the exact
   `D_N=(3N^2+N-12)/2` fiber.  Decompose the full boundary as
   `Q3+Q4+Q5`, retaining the latter two as nonnegative flow.
5. Use `min(pi(A),pi(A^c))<=pi(A)` with exact global masses, never a
   conditional smaller-side assumption.

## Falsification and calibrations

Cross-check the count inequalities against the existing exact `F_4,F_5`
join-tree layer data and, if useful, create a focused deterministic artifact
whose finite scope is explicitly stated.  Check the star and path endpoints,
`m=4` whole-word `H4`, `S3,m4`, `S4,m4`, `S4,m6`, doubled-tree examples,
ordered word behavior, parity limitations, and the failure of `L=2`
simulation.  A finite pass is never an asymptotic proof.

## Deliverables

Write a genuine `checkpoint.md` and a nine-field `report.md` with exact
theorem, proof, rate/runtime accounting, labeled dependencies, first next
gap, self-attack, calibrations, artifacts/commands, and verdict exactly
`PROVED`, `REFUTED`, or `OPEN AT A NAMED STEP`.
