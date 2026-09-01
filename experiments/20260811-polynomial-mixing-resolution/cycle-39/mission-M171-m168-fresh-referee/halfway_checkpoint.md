# M171 halfway checkpoint

Date: 2026-08-13.

The supplied four M168 SHA-256 digests match, and `sha256sum -c` passes for
all eight entries in M168's frozen payload inventory.

The clean-room audit imports no M168 implementation.  It rebuilt every
rank-two state and its lift multiplicity from literal ordered pairs of
distinct transpositions, then ran exactly `k=3,5` and stopped.  It verified:

- the fixed-head, directed-residual-edge, same-component, and rank-drop
  characterizations of a generic boundary edge;
- all `18,144` and `573,300` ordered disjoint boundary-edge pairs;
- the component counts `g_i(g_i-1)-2a_i` and `2g_i g_j`;
- all `5,670` and `308,880` nonzero inserted completion-size formulas;
- nonzero retention of `IS`, `IN`, and `X`;
- direct all-lag sums equal `(PC)` for every `336` and `3,185` supported
  intermediate state;
- direct raw convolution equals `(PCS)` with its stated normalization; and
- three/six physical cell orbits each have exactly two colored appearances,
  with `(CE)`'s factor `1/2` holding exactly.

The independently reconstructed signed sums are

```text
k=3: 7345139916497931/7061881225000000
k=5: 73077925347453973355779108467047756359425607682995598110051
     /150223593265440401176815963858761531101584168449901928120320
```

Both match frozen M168 exactly.  The deterministic `(TV-close)`, `(NEG-id)`,
and `(SC)` implications also pass algebraic audit.  Neither scalar uniform
bound in `(SC)` is proved.  The prospective verdict is `ACCEPT`, subject to
the final hash/hygiene gate and explicit nonmaterial objections in the final
report.

