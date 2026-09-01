# M84 halfway checkpoint

Date: 2026-08-12. Commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Current verdict

The frontier has narrowed from arbitrary order histories to a static random
subset chain, and there is now a candidate exact infinite zero-row theorem
for the accepted voltage family. The theorem is not yet frozen at this
checkpoint because its ribbon-surface collision lemma is undergoing a full
local proof audit.

## Proved algebraic reduction

Let `S` be the set of original labels already selected. Extracting the labels
of `S` in increasing chronological order emits exactly the original factors
in `S`. Its residual is

```text
r_j(S)=H_j(S)^(-1) t_j H_j(S),
H_j(S)=product of t_l over l in S, l>j, in chronological order.
```

Any other selection order of the same set differs only by Hurwitz moves
inside the emitted prefix. Therefore:

- the residual tuple is a function of `S` alone;
- the emitted prefix has the labeled support-component partition of the
  original selected-edge graph `G[S]`;
- duplicate availability and deletion connectivity are functions of `S` and
  the proposed pair, not the order reaching `S`.

For unselected `i<j`, with

```text
B = product of selected t_l with i<l<j,
```

the current residual factors agree exactly when

```text
t_i = B t_j B^(-1).
```

Thus canonical elimination is a uniformly ordered chain through subsets, not
an exponentially branching history-dependent state process.

## Collision contour and candidate theorem

The conjugacy relation tracks the two endpoints of `t_j` through the selected
intermediate transpositions. The two token paths, closed using `t_i,t_j`,
form the pullback of the dual two-edge curve created by the adjacent equal
endpoint factors. The standard cellular-dual criterion gives:

```text
deletion is connected  <=>  collision contour is nonseparating.
```

On the genus-one chronological surface this is equivalent to nonzero integral
homology. The pending audit is to spell out the elementary Hurwitz edge-slide
identification and show that selections outside `(i,j)` are isotopies of this
curve and cannot change its separation type.

For `W_L`, every one of the 16 base factor blocks is a perfect matching. Each
of the two token paths crosses at most one edge per block. Only four blocks
carry nonzero `x` voltage and four carry nonzero `y` voltage. Including the
two closing pair edges gives

```text
|V_x|<=10, |V_y|<=10.
```

A closed contour in the `Z_L^2` lift has `V in L Z^2`. Hence for `L>=11`,
`V=0`, so the contour is separating and every collision is unsafe. If the
collision-contour lemma survives audit, this proves the exact zero row

```text
eta_L=0 for every L>=11,
```

refuting the simple-positive-braid row lower bound on an explicit infinite
sequence. It would not be Terminal B for the heat-bath chain.

## Exact computational checks so far

- Full tail-subset enumeration found no safe pair for `W_2` with unselected
  complement size `2`, `3`, or `4` (`2016`, `41664`, and `635376` subsets).
- The base `W_1` first has 19 safe pairs across 19 of the 1820 four-label
  complements, exact one-level mass `19/10920`.
- Exact contour calculations for M81's two replayable unsafe `W_2`
  collisions give homology `(0,0)`; an exact base safe pair gives `(0,1)`.
- In fixed-seed exact-per-state probes, `safe iff contour homology !=0` had
  zero mismatches across 508 base collisions, 97 `W_2` collisions, and 27
  `W_3` collisions. Every `W_2,W_3` contour had zero homology. This is
  empirical support only, not the proof.

## Remaining work

1. Write the factorization-map/dart proof of the collision-contour lemma,
   including the local right-Hurwitz edge slide.
2. Verify the voltage cocycle is an integral homology basis on the base torus
   (zero face sums plus the accepted basis cycles suffice).
3. Add exact static-order consistency and bounded-voltage audits, label all
   computation correctly, then write the nine-field report.
4. Freeze hashes, remove caches, and hand off the theorem for a fresh referee.

No terminal heat-bath claim is made.
