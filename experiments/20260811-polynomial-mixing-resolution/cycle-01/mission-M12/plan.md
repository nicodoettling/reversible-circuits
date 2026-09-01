# M12 Plan: Sparse and Near-Minimal Red Team

## Objective and target

Seek a rigorous TERMINAL B refutation for the uniform fixed-length bridge law

\[
\pi_{N,m}=\operatorname{Unif}\Omega(N,m),\qquad
\Omega(N,m)=\{(t_1,\ldots,t_m)\in T_N^m:t_1\cdots t_m=\mathrm{id}\},
\]

in the regime \(N\ge 3\), even \(m\ge4\).  Permutations are maps on
\([N]\), \(pq=p\circ q\), and a word evaluates as \(t_1\cdots t_m\).
The reviewed kernel is exactly

\[
K_{N,m}=\tfrac12 I+\frac1{2|R_m|}\sum_{r\in R_m}
 \frac1{m-r+1}\sum_{i=1}^{m-r+1}H_{i,r},
\quad R_m=\{r\in\{3,4,5\}:r\le m\},
\]

where \(H_{i,r}\) is uniform on the length-\(r\) same-product fiber.

The terminal target is either a genuine reducibility example in the stated
regime or an explicit infinite sequence with superpolynomially small gap.
Anything weaker will be reported as nonterminal.

## Proof program

1. Derive exact global enumeration formulas for \(|\Omega(N,m)|\), support
   restrictions, and the near-minimal full-support layer using character or
   transitive-factorization counts.  Use them to prevent a rare-set cut from
   being mistaken for a bottleneck.
2. Test four named cut families analytically:
   - full support versus one or more isolated labels;
   - minimal connected words \(m=2(N-1)\) versus words with local square
     certificates;
   - thin weighted-component merge/split interfaces;
   - low surplus/low repeated-edge or low adjacent-square layers.
3. For every candidate, calculate the exact one-step boundary probability,
   including laziness, uniform block-size choice, window normalization, and
   conditional-fiber probability.  Establish stationary mass on both sides or
   reject the cut.
4. Search first for simple universal escape moves from sparse states.  A
   polynomial lower bound on escape from every state of a proposed cut
   decisively rules out that cut as a superpolynomial bottleneck even though it
   does not prove global rapid mixing.
5. If useful, perform only exact finite calculations tied to a named universal
   lemma; record fixed seeds (if stochastic), environment, commands, and raw
   machine-readable output.  Finite values are falsification evidence only.

## Calibration and failure modes

Every claimed statement will separately address odd \(m\), \(m=0\), \(m=2\),
\(N=2\), the three exact smoke cases, the whole-word \(r=4\) update at
\(m=4\), doubled-tree near-minimal words, color interleavings of disjoint
components, and the known failures of parity-only characterizations,
length-two simulation, and canonical-hub routing.

Expected failure modes are: exponentially small candidate mass; local escape
probability that is only polynomially small; an invalid graph-only argument
that forgets word order; or a necessary counting ratio for which no uniform
asymptotic estimate is available.  The final report will name the first such
standalone proposition if TERMINAL B is not obtained.

## Deliverables

- `checkpoint.md`: genuine halfway results and discarded cuts.
- Optional proof notes or exact scripts/raw data, confined to this directory.
- `report.md`: the required nine-part return schema and exact verdict.
