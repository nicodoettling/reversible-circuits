# Identity-Bridge Sampler Paper

This folder contains a LaTeX research note consolidating completed findings on
fixed-length identity-bridge sampling in symmetric groups, including the
transposition heat-bath model, current polynomial-mixing proof obligations, and
expander-generator benchmark directions.

Main file:

```text
main.tex
```

The historical filename `identity_transposition_samplers.tex` is retained as a
compatibility wrapper that inputs `main.tex`.  The paper body is split into one
file per section under `sections/`.

Scope:

- exact small-case enumeration,
- pure Hurwitz orbit obstruction,
- graph-theoretic closed-walk, token-swapping, and rewrite-graph interpretation,
- exact block heat-bath stationarity,
- finite small-case spectral evidence,
- prefix-rejection bottlenecks for conditional block sampling,
- direct exact r=4/r=5 block samplers and integrated {3,4,5} heat-bath,
- current irreducibility and polynomial-mixing proof obligations,
- conditional projection/decomposition and large-block comparison routes,
- negative congestion lesson for deterministic canonical-square routing,
- alternative expander-generator benchmark models, including
  Kassabov-style generators.

The note includes completed findings through the polynomial upper-bound and
later polynomial-mixing swarm attempts.

Build, if a LaTeX distribution is installed:

```bash
latexmk -pdf main.tex
```

