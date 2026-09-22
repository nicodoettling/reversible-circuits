# Blind Brief: Fixed-Length Identity-Word Sampling

You are the nonauthor referee in a one-hour research run. Initially read only
this brief, the coordinator's operational deadlines, repository safety rules
and primary mathematical sources needed by your own argument. Do not inspect
other role directories or old proof/verdict reports until your blind report
is frozen. Record unavoidable inherited context; blindness is not independence
of the shared model or repository framing.

Use gpt-6-astra / ultra, no delegation, no competing goal. Own only
experiments/20260922-sparse-boundary/roles/r5-referee/. Checkpoint within
20 minutes from SERVICE activation, freeze blind_report.md by 30 minutes,
then receive and review exact candidate versions. The coordinator sends the
absolute cap deadlines. Do not launch processes outside the capped run.
No installs, escalation, machine changes, old-file edits, commits or pushes.

## Definitions and Questions

For N>=2 let T_N be all transpositions of S_N, with distinguished labels
and ordered positions. Products satisfy (ab)(x)=a(b(x)). Let

```text
Omega(N,m) = {w in T_N^m : product(w)=id},
U_(N,m) = Unif(Omega(N,m)).
K = max{1<=v<=N : v^(2v)<=(N+m+2)^4}, fixed at the top-level input.
```

A nontrivial support component on v vertices containing ell factors has
ell=2v-2+2g, integer g>=0. Isolates are (v,ell)=(1,0).

Define A as words for which every nontrivial component satisfies
g<=1 OR v<=K, and B as words for which every such component has v<=K.
Small components may have arbitrarily large g. In particular B subset A.
The mathematical distributions under review are Q_A=Unif(A), Q_B=Unif(B).
Their TV errors from U are exactly 1-|A|/|Omega| and 1-|B|/|Omega|.

For every even m with m^4<=N^3, do either of these laws have error bounded
uniformly by one explicit eta(N) negligible in N? Here negligible means
eventually <=N^(-a) for EVERY fixed a>0. The two questions are distinct.
The sequence m_*(N)=max{even m>=0 : m^4<=N^3} is a concrete diagnostic.

Try to prove, refute, or isolate a precise missing lemma. If another
polynomial-time sampler solves this range, state its literal sampling
choices, dependencies, expected BIT complexity and statistical error.
Failure of A or B is not computational hardness of uniform sampling.
Do not mistake a vacuous upper bound for a lower bound on actual error.
Finite numerical results cannot prove or refute eventual negligibility.

Treat m=0,m=2,N=2 and odd m explicitly; N=1 has only the empty word.
Version changes to the range or allowed sets and keep the original questions.
No unconditioned independent-edge graph model is assumed.

## Permitted Sources

You may check exact counting statements in primary sources, with all label,
position and normalization factors verified:

- Dubrovin-Yang-Zagier, Classical Hurwitz numbers and related combinatorics:
  https://people.mpim-bonn.mpg.de/zagier/files/tex/ClassicalHurwitz/HurwitzRevised.pdf
- Vakil, Genus 0 and 1 Hurwitz numbers:
  https://math.stanford.edu/~vakil/files/g01hurwitz.pdf
- Chapuy-Louf-Walsh, Random partitions under the Plancherel-Hurwitz measure:
  https://arxiv.org/pdf/2206.11315

Literature claims with different length regimes or only o(1) error require
an explicit transfer argument. Scalar word counts alone are not a decoder.

Save the complete initial brief, your frozen report/hash, all finite tests
and source checks. After freezing, record the exact later review inputs and
audit the strongest resulting claim, checking quantifiers, conditioning,
resource accounting and all repairs. If no theorem survives, say so plainly.
