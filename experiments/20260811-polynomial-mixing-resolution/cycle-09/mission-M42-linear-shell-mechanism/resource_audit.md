# M42 resource audit: subset occupation and changing expander walks

## Local search

The three PDFs in the repository's `Literature/` directory do not contain a
concentration theorem for Bernoulli--Laplace occupation under deterministic
permutation kicks or a first-return shell-layer theorem.  The M42 proof does
not use an unverified local citation.

## Primary sources checked

### Diaconis--Shahshahani

Persi Diaconis and Mehrdad Shahshahani, *Time to Reach Stationarity in the
Bernoulli--Laplace Diffusion Model*, SIAM Journal on Mathematical Analysis 18
(1987), 208--218, DOI 10.1137/0518016:

<https://epubs.siam.org/doi/10.1137/0518016>

The paper diagonalizes the Bernoulli--Laplace/Johnson walk by the Gelfand-pair
method and analyzes its mixing scale.  M42 uses the same subset action but a
different normalization: one chooses uniformly from all `E=binom(d,2)`
transpositions, including those that fix the subset.  The required spectrum
is therefore derived directly from the Johnson adjacency eigenvalues:

```text
P_s=(e_s/E)I+(1/E)A_J,
lambda_j=1-j(d-j+1)/E.
```

This normalization gives mean-zero norm `1-2/(d-1)`.  No mixing-time
conclusion is imported without this translation.

### Gillman

David Gillman, *A Chernoff Bound for Random Walks on Expander Graphs*, SIAM
Journal on Computing 27 (1998), 1203--1220, DOI
10.1137/S0097539794268765:

<https://epubs.siam.org/doi/10.1137/S0097539794268765>

Gillman's theorem gives exponentially small occupation deviations for one
homogeneous weighted-graph walk in terms of its expansion/spectral data.  It
does **not** literally cover the M42 core after fixed primitive-block products:
those products insert deterministic permutation kicks and make the checkpoint
transitions time-dependent.

M42 therefore does not cite Gillman's conclusion as a dependency.  It proves
the needed changing-walk estimate directly: centrality makes every `r`-step
kicked transition `P_s^r U`, with mean-zero norm at most `1/(16d^2)`, and the
one-state projection identity

```text
||D(P_s^r U)D||<=1/binom(d,s)+1/(16d^2)<=2/d
```

controls any prescribed collection of visits.  This is sufficient for the
extreme confinement event used here and avoids an unjustified homogeneous-
chain transfer.

## First-return/hard-rod search

The targeted primary search did not locate a theorem that simultaneously
handles:

1. canonical first returns of the prefix action to `Stab(z)`;
2. the exact segmentation cost by connected length-five window hulls;
3. hard-rod placement under a fixed full permutation endpoint; and
4. a boundary-layer-to-cumulative-volume ratio polynomial in `N,m`.

Abstract polymer/clique-dynamics theorems require multiplicative polymer
weights and insert/delete transitions, already audited as mismatched in M40.
The next entropy-matched segmentation statement remains an internal named
proposition rather than a cited result.

## Applicability verdict

- Bernoulli--Laplace spectral input: **applicable after the explicit lazy
  normalization translation; also rederived algebraically.**
- Homogeneous expander Chernoff theorem: **not literally applicable with
  kicks; replaced by a proved projection-product bound.**
- Polymer/animal boundary injection: **no applicable primary theorem found.**
