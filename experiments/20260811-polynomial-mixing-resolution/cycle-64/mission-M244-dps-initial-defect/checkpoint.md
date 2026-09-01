# Mission M244 Checkpoint

Status: final theorem written; freeze preparation in progress.

## Source lock

The immutable M240 and M242 inventories verify, including their requested top
digests. The primary source is Enrica Duchi, Dominique Poulalhon, and Gilles
Schaeffer, *Uniform random sampling of simple branched coverings of the sphere
by itself*, SODA 2014, pp. 294--304, DOI
`10.1137/1.9781611973402.21`. The author-hosted PDF used here has SHA-256

```text
98a38c327c96e37d7dfd04ae93f0012a0742f6398958ddcbe2dd3501ddb52ea2.
```

The paper has been read in full. Proposition 3 inserts black `x_a` in the
first parent edge of white `y_a`; Lemma 2 supplies the distance-one/
distance-three local closure; Theorem 5 proves the LIFO closure is inverse to
the quadrangulation-to-tree map. It writes `tau_m ... tau_1=id`; reversing the
displayed source word gives the project's left-to-right factor convention.
The accepted plus-mirror implementation instead reverses the source's cyclic
white/black convention and directly produces the project display. Neither
choice changes the intrinsic matching or physical transpositions.

## Exact recurrence fixed before checking

For a rooted labeled Hurwitz tree `H`, trace its unique outer contour. At a
white (respectively black) vertex, rotate labels increasingly (respectively
decreasingly). Emit a tree-side token `S` when the next label is incident and
otherwise emit a half-edge `W_a^ell` (respectively `B_a^ell`). The source
LIFO closure is the cyclic rewrite

```text
W_a^ell S^q B_b^ell  ->  S_ell,       q in {1,3},
```

whenever the displayed half-edges are consecutive among remaining
half-edges. For `q=3`, record `x_b` as the second black endpoint of face
`ell`; if no such closure occurs, the second endpoint is the final root black
vertex. This recurrence is definitionally equivalent to DPS RandomQuad and
is independent of any finite rank.

For the canonical order with the pair at `x_v` reversed, prune contour
intervals that do not meet the stopped parent path `P(v)`. The remaining
rewrite has two states, `C` (sealed) and `O` (one exposed defect). The local
transition table to prove is fixed as follows:

```text
path step v>a>b                    O -> O
path contains a>v                  O -> C
internal path step a<b             O -> C
off-path child r>v with p(r)=v      O -> O, expose both x_r faces
all other off-path sectors          state unchanged
root boundary                       C -> literal extension;
                                    O -> cursor/child/root split
```

Thus the defect reaches the root exactly when `P(v)` is strictly decreasing.
In state `O`, its recorded second endpoint is the current final root black;
the exposed direct-child faces have that same endpoint. At the final root
sector the two old high labels have partners `x_v,x_root`; after extension,
the old-root slot closes twice to `x_1` and the new high labels have partners
`x_v,x_newroot`. This table is the analytic boundary-stack recurrence to be
derived, not an inference from finite data.

The generic off-path row is now proved in the exact scope needed. A canonical
unedited excursion, characterized by `R_a=L_a+1`, is a contiguous contour
interval whose complete internal rewrite nodes leave exactly the single white
interface token `W^R_a`. The reversed edited slot `x_v` is excluded. The
tempting zero-balance claim was corrected: the excursion has excess one, and
becomes balanced only after adjoining a virtual `B^R_a`.

What remains unresolved is solely the metric interface: after the complete
rewrite nodes are deleted at ranks `d` and `d+1`, prove that every retained
old-label pair sees the same one-versus-three side count and black endpoint,
with the declared larger-direct-child and stopped-path/root exceptions. This
is frozen as RSMI in `stack_pruning_reduction.md`. RSMI implies M240 IDL, but
RSMI itself is not claimed.
