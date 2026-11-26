# Identity-Bridge Sampler Paper

This folder contains a LaTeX research note consolidating completed findings on
fixed-length identity-bridge sampling in symmetric groups.  Its main result is
a polynomial-time, fixed-negligible-error rank-recursive sampler at length
`2N^3`; it also records the transposition heat-bath model, its remaining
conductance obstruction to universal polynomial local mixing, the remaining
long-length mixing questions, and expander-generator benchmark directions.

Main file:

```text
main.tex
```

The historical filename `identity_transposition_samplers.tex` is retained as a
compatibility wrapper that inputs `main.tex`.  The paper body is split into one
file per section under `sections/`.

Scope:

- exact small-case enumeration,
- the exact old/star stable-sort disintegration,
- exact polynomial-time prescribed-endpoint star sampling,
- a polynomial-time rank-recursive sampler at length `2N^3` with total
  variation at most `3N exp(-N/12288)`,
- exponentially likely complete transposition support in the dense bridge,
- pure Hurwitz orbit obstruction,
- graph-theoretic closed-walk, token-swapping, and rewrite-graph interpretation,
- exact block heat-bath stationarity,
- finite small-case spectral evidence,
- prefix-rejection bottlenecks for conditional block sampling,
- direct exact r=4/r=5 block samplers and integrated {3,4,5} heat-bath,
- a balanced bottleneck for every bounded-slot uniform-stationary walk,
- superpolynomial slowdown for growing budgets `b=o(m/(log m)^3)`,
- rapid mixing of a specified ideal `O(N log N)` overlapping block bath,
- an all-endpoint base-length reduction for longer pair-chain mixing,
- long-length support-profile conductance and all-endpoint pair connectivity,
- sharp spaced-prefix cut bounds and a relabeling reduction at quadratic length,
- an `Omega(N^4)` quadratic mixing lower bound, including the relabeling quotient,
- current regime-specific polynomial-mixing proof obligations,
- conditional projection/decomposition and large-block comparison routes,
- negative congestion lesson for deterministic canonical-square routing,
- alternative expander-generator benchmark models, including
  Kassabov-style generators.

The note includes the September 2026 rank-recursive result and the November
24, 2026 conductance-draft audit. The latter's proofs and exact checks are in
`../../experiments/20261124-conductance-audit/`; the manuscript section
`sections/conductance_obstruction.tex` gives the expanded proofs.
The November 26 follow-up is in `../../experiments/20261126-window-reductions/`
and the sections `growing_windows.tex` and `quadratic_diagnostics.tex`.
Its relabeling comparison uses a proved conservative `N^-11` term; stronger
exponents in the supplied sketch remain unverified. Ideal large-block mixing
does not include a polynomial exact-conditional implementation guarantee.
Internal audits do not replace independent human referee review.

Build, if a LaTeX distribution is installed:

```bash
latexmk -pdf main.tex
```
