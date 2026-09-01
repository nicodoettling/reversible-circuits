# M43 resource audit: renewal and polymer hypotheses

## Local-first search

The local `Literature/` directory contains only:

- `0110110v1.pdf` (Hurwitz equivalence for identity transposition
  factorizations),
- `2406.07478v3.pdf` (unconditioned reversible-circuit moment gaps and
  expander generators), and
- `2603.19110v1.pdf` (post-quantum cryptography from stabilizer decoding).

None states a first-return segmentation, hard-rod boundary-layer, or polymer
shell theorem applicable to the literal `V^(a)` sets.  Searches of the local
experiment index and internal-source section for `renewal`, `polymer`,
`hard rod`, `first return`, and `cluster decomposition` found no additional
source.

## Primary sources audited

### Hong--Zhou finite-state passage-time transform

Wenming Hong and Ke Zhou, *A note on the passage time of finite state Markov
chains*, arXiv:1302.5987 (2013), Theorem 2.1:

<https://arxiv.org/abs/1302.5987>

For a finite discrete-time chain with absorbing state `d`, their Theorem 2.1
expresses the generating function `E_i[s^tau]` of the absorption time as a
ratio of minors of `I-sP`.  This literally applies to the two-orbit point
process obtained by tracking whether the inverse prefix fixes `z`, and it can
recover the primitive-return generating function.

It does **not** supply the M43 theorem: the shell cost is the minimum over
groupings of multiple excursions with window-hull cost
`ceil((L-1)/4)`, the total word has a fixed group endpoint, and the needed
statement is a finite coefficient comparison uniform in growing `N,m,a`.
No hypothesis or conclusion of Theorem 2.1 controls those hard-rod layouts or
the boundary-source/cumulative-volume ratio.  M43 instead derives the exact
coefficient identity (C.9)--(C.10) directly.

### Goulden--Jackson cluster inversion

I. P. Goulden and D. M. Jackson, *An Inversion Theorem for Cluster
Decompositions of Sequences with Distinguished Subsequences*, Journal of the
London Mathematical Society (2) 20 (1979), 567--576, DOI
10.1112/jlms/s2-20.3.567:

<https://doi.org/10.1112/jlms/s2-20.3.567>

The paper gives a generating-function inversion for sequences with marked
distinguished subsequences, using connected overlap clusters.  Its framework
is conceptually close to marking short inter-excursion gaps.

It is not quoted as a theorem dependency.  Here an excursion is defined by a
group-valued prefix state; the cost is an optimization over local-window
hulls; internal gaps share one fixed-endpoint coefficient; and the exact
finite-volume hard-rod layout matters.  The abstract inversion theorem does
not, without a new encoding, imply the quantitative factor
`(1-3yD_A)^(-p)` or the original-`K` boundary flow.  The two binomial
identities needed by M43 are proved directly.

### Friedrich--Göbel--Krejca--Pappik polymer clique dynamics

Tobias Friedrich, Andreas Göbel, Martin S. Krejca, and Marcus Pappik,
*Polymer Dynamics via Cliques: New Conditions for Approximations*,
arXiv:2007.08293, Theorems 1.1 and 3.4:

<https://arxiv.org/abs/2007.08293>

Their state space is an abstract polymer model with multiplicative positive
activities and pairwise incompatibility; their chain samples an empty or
single-polymer choice from a selected incompatibility clique.  Theorem 3.4
assumes the paper's clique-dynamics condition and bounds that chain's mixing.

The literal bridge shell does not have multiplicative polymer weights after
conditioning the total permutation product, an update history is not a
unique compatible polymer family, and `K` is a same-product interval heat
bath rather than clique insert/delete dynamics.  Consequently neither
Theorem 1.1 nor 3.4 applies.  In particular, invoking polymer rapid mixing
would not account for `H_3,H_4,H_5` boundary flow.

### Spitzer's Markov renewal theorem

Frank Spitzer, *Renewal theorems for Markov chains*, Proceedings of the Fifth
Berkeley Symposium on Mathematical Statistics and Probability, Vol. II,
Part 2 (1967), 311--320:

<https://projecteuclid.org/ebooks/berkeley-symposium-on-mathematical-statistics-and-probability/Proceedings-of-the-Fifth-Berkeley-Symposium-on-Mathematical-Statistics-and/chapter/Renewal-theorems-for-Markov-chains/bsmsp/1200513474>

Spitzer studies asymptotic Green functions and renewal limits for Markov
chains under recurrence/drift hypotheses.  Those results concern long-time
renewal asymptotics, not a finite exact coefficient with a growing state
space, fixed group endpoint, bounded local-window segmentation cost, and an
inverse-polynomial boundary-layer comparison.  No result there is literally
applicable to M43.

## Conclusion

No audited primary theorem transfers directly.  The remaining segmentation
loss is not real in the range `a=o(N^3)`: the project-specific canonical
decomposition produces the exact negative-binomial resummation

```text
sum_h (3yD_A)^h (p)^(over h)/h!=(1-3yD_A)^(-p),
```

and its logarithm is `O(a/N^3)`.  This conclusion depends on the proved
path-cost inequality and exact hard-rod counts, not on an asymptotic renewal
or polymer theorem.
