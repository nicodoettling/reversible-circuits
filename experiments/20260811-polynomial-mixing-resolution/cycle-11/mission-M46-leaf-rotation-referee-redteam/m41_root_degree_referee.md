# Fresh referee note: M41 root-degree projection gap

Frozen checkpoint SHA-256:
`9c0fc7da93f9ad18d817af431e45feb8ed871b36e2a1781bcee0d24824c449b3`.

## Verdict

**ACCEPT.**

Numbered objections: **none**.

1. The fixed-root Prüfer code has length `r-1`, so
   `d_0-1~Bin(r-1,1/(r+1))` exactly.
2. In the reversible Dirichlet form, using only the lowering orientation
   counts each undirected edge once.  The aggregate coefficient at root
   degree `k` is exactly `2k(k-1)/[3r(r-1)]`; there is no omitted factor two.
3. For `b=k-1`, the Bernoulli random-scan heat bath has downward rate
   `b(1-p)/(r-1)` and gap `1/(r-1)`.  The exact coefficient ratio is
   `2(b+1)(r+1)/(3r^2)>=4(r+1)/(3r^2)`.
4. Hence the stationary-flow root-degree projection has gap at least
   `4(r+1)/[3r^2(r-1)]`.
5. At `r=2`, its down/up rates are `2/3,1/3`, and the formula gives the
   exact gap one.

The conclusion is only a Poincare bound for functions of root degree; it is
not a gap theorem for the full parking projection or the original chain.
