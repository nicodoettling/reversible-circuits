# Universal irreducibility of the aligned length-four bridge chain

Use `(pq)(x)=p(q(x))`.  For `m=2n>=4`, let

```text
B=(1/(n-1)) sum_{q=1}^{n-1} H_{2q-1,4}.
```

## Proposition

For every `N>=3` and even `m>=4`, `B` is irreducible on `Omega(N,m)`.

## Proof

Every adjacent pair of positions is contained in an aligned window.  If the
pair begins at an even position `j`, use the window beginning at `j-1`.  If it
begins at an odd position other than `m-1`, use the window beginning at `j`;
for the last pair use the final window beginning at `m-3`.

Inside that window, hold the other two factors fixed.  Replacing the selected
pair by either its right Hurwitz image or its inverse preserves the pair's
ordered product and hence the four-letter product.  It is therefore a
positive-probability outcome of the aligned heat bath.  By the audited
Ben-Itzhak--Teicher classification, these moves connect every word to a
representative made entirely of adjacent square pairs with the same labeled
component sets and weights.

The same containing-window argument realizes every square refresh
`(t,t)->(s,s)`, again holding the other two factors fixed.  Successively
refreshing the paired representative to one fixed transposition connects it
to a universal word.  Heat-bath transitions are symmetric, so reversing these
paths connects every pair of states.

A specified four-letter outcome has probability at least

```text
1/[(n-1)F_4(h)] >= 1/[(n-1)M^3]
```

under nonlazy `B`; this proves positivity only.  At `m=4`, the sole aligned
window is the whole word and the argument reduces to a one-step global heat
bath.  No path-length or congestion bound is claimed.

This closes the qualitative clause in the Parity-block bridge Poincare
proposition.  Its universal inverse-polynomial gap remains open.
