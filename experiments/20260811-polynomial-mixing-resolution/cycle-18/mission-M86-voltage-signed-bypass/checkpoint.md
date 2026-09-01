# M86 halfway checkpoint

Date: 2026-08-12. Commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Status at halfway

The accepted M84 zero row does **not** extend from the canonical positive
elimination law to all polynomial-length state-independent signed Hurwitz
laws, even on its own voltage family. A constructive bypass is now isolated
for `W_L`, all global label conjugates, all cyclic factor phases, and all
interleavings with the disjoint ambient doubled edge. The full arbitrary
two-component macro remains uncovered.

Let

```text
d=8L^2,  k=16L^2=2d,
C_d=(01)^2(12)^2...((d-2)(d-1))^2(01)^2.
```

Deleting the final `(01)^2` leaves the connected identity doubled path, so
`C_d` is marked. The accepted constructive Classification-H audit gives a
deterministic signed Hurwitz word `beta_L` carrying `W_L` to `C_d` with
length at most `50 d k^3`: run its explicit Lemmas 3.7--3.10 procedure with
lexicographic shortest paths and earliest-occurrence tie breaking from each
of the two fixed public templates `W_L,C_d` to the same componentwise
canonical word, then reverse the `C_d` path. All branching occurs while
precomputing this one index/sign sequence. Applying the stored word later is
not state adaptive.

Hurwitz action commutes generator-by-generator with global relabeling, hence

```text
beta_L(sigma W_L)=sigma C_d.
```

Let `rho_k=R_0 R_1 ... R_(k-2)`. On an identity word it is literal cyclic
left shift. For each pair-slot set `I subset {0,...,k+1}`, `|I|=2`, let
`S_I` stably move those two slots to the final positions. For the natural
source class

```text
x_(sigma,q,I)=Interleave_I(sigma rho_k^q(W_L), sigma(e),sigma(e)),
e=(d,d+1),  0<=q<k,
```

the fixed indexed word

```text
gamma_(I,q)=S_I rho_k^(-q) beta_L
```

sends `x_(sigma,q,I)` to `sigma C_d, sigma(e),sigma(e)`, which has the
specified marked genus-one square. Uniform choice from the indexed family has

```text
P=k binom(k+2,2),             eta>=1/P,
E length <=50 d k^3 +(k-1)^2/2+k.
```

Parallel braid representations are allowed: the law is on indexed words, and
the correct index retains mass `1/P`. Every prefix is a bijection, so word
index, prefix time, and the actual directed edge recover at most one source,
exactly as in M75's accepted coarea theorem.

## New obstruction retained with the bypass

A separate topological estimate appears to be universal for this source:
if a signed braid of `q` adjacent generators sends `W_L` to a safe adjacent
square, pull its pair annulus back to the original voltage torus. Its
nonseparating homology projects to a nonzero vector of `L Z^2`. The skeleton
starts with the two collision bands, and each inverse local edge slide adds
at most two original-band traversals, including when one tracked collision
strand participates. Since each original band has each voltage coordinate in
`{-1,0,1}`,

```text
L <= max(|V_x|,|V_y|) <=2q+2,
q >=(L-2)/2.
```

This is only an `Omega(L)=Omega(sqrt(N))` distance lower bound and is fully
compatible with polynomial routing. It rigorously refutes uniformly bounded
signed templates, not the new constructive bypass or the heat-bath chain.
The local signed-slide case split and ambient extension remain to be written
carefully before freezing.

## Exact finite probes

A fresh standard-library implementation verifies signed generator inverses,
identity preservation, literal safe deletion, and endpoint replay. Fixed
seeds found exact certificate paths of length `68` for `W_1` and `23789` for
`W_2`. It found no hit for `W_3` in `200000` random signed steps. The first
two paths are exact finite certificates; the third statement is empirical
only. None is needed for the asymptotic construction, which uses the accepted
constructive classification algorithm.

## Remaining work before freeze

1. Formalize the signed-slide voltage increment lemma, including pair-strand
   participation.
2. Add an exact family audit for stable sorting, phase inversion, relabel
   equivariance, canonical target safety, and indexed-family counts.
3. State the inherited `H3` capacity and terminal-refresh constants when the
   law is inserted into M75's theorem.
4. Freeze a nine-field report and hashes; then request a fresh referee.

No Terminal-A, Terminal-B, full-macro, or full-`K` conclusion is claimed.
