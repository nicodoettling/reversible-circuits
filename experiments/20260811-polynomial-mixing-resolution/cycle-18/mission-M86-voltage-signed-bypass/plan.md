# M86 plan: signed-braid bypass of the voltage zero row

Date: 2026-08-12. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and exact scope

The ambient project target is uniform on

```text
Omega(N,m)={w in T_N^m: eval(w)=id}
```

for the literal lazy exact same-product `{3,4,5}` block heat-bath kernel.
This mission studies only the two-component minimal-exterior comparison
subproblem after M84/M85 refuted M75's canonical positive-elimination row
bound. It does not modify the kernel or target and cannot by itself prove
Terminal A or Terminal B.

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors are evaluated
left-to-right. The right signed Hurwitz generators are

```text
R(a,b)=(b,bab),       R^(-1)(a,b)=(aba,a).
```

The concrete source is the accepted voltage word `W_L`, with
`d=8L^2`, `k=16L^2`, optionally interleaved with the disjoint doubled edge
that places it in M75's two-component minimal macro.

## Named claim under test

> **Voltage signed-bypass question.** Is there a polynomial-size or
> polynomial-time samplable, source-independent probability law on literal
> bijective signed Hurwitz words, of polynomial expected length, that sends
> every natural phase of `W_L` to M75's connected-deletable-square marked set
> with inverse-polynomial probability, with recoverable first crossings?

The first goal is a deterministic construction or impossibility statement on
`W_L`, not a universal macro theorem. Any transformation must be specified as
an index word in `R_i^{+/-1}` independent of the factor values. A family must
include its support size/sampling rule, length, collision metadata, and the
actual-edge inverse-prefix recovery needed by M75's coarea theorem.

## Work plan

1. Reconstruct `W_L`, signed Hurwitz actions, the marked set, and the
   torus-voltage homology test in a fresh auditable script.
2. Prove the topological length constraint: every safe final square has a
   pulled-back embedded curve of nonzero homology in `L Z^2`; quantify how
   much a bounded-crossing signed template can change its voltage.
3. Search exact small moduli and natural phases for literal braid words that
   realize `L` windings of the primitive base cycles
   `0-7-2-6-0` or `0-7-1-6-0`, then algebraically lift any found pattern.
4. Audit state independence, bijectivity, expected/max length, family size,
   first-hit probability, and actual directed-edge recovery. Reject any
   state-dependent certificate search disguised as a fixed law.
5. If no bypass is proved, freeze the strongest rigorous obstruction or
   exact counterexample and state the narrower general partial-macrofiber
   lemma that remains. Finite search will be labeled empirical/exact-finite,
   never asymptotic proof.

## Falsification and boundary cases

- Check `L=1,2,3` and natural cyclic translations/chronological block phases.
- Verify word evaluation, factor multiset invariance, support connectedness,
  exact adjacent-square deletion safety, and inverse action for every used
  generator.
- Distinguish an existing pair-annulus transported by a homeomorphism from a
  new collision created when two distinct factors become equal.
- Check odd `m`, `m=0`, `m=2`, and `N=2` only as scope exclusions; they do not
  instantiate this voltage family.

## Expected failure modes

- A homeomorphism cannot turn a separating marked annulus into a
  nonseparating one, but signed braid motion may create a different collision;
  conflating these is invalid.
- A braid selected after inspecting the source is not a state-independent
  cover law unless a fixed metadata family and probability law are supplied.
- An `Omega(L)` winding lower bound is compatible with polynomial length
  because `N,m=Theta(L^2)`; it refutes only bounded-crossing templates.
- Polynomial family cardinality alone does not control coarea congestion;
  inverse-prefix recovery must be literal.

## Reproducibility standard

Scripts will use Python 3.12.3 and the standard library only, with fixed or
null seeds recorded in machine-readable output. Commands, elapsed times,
parameters, exact/empirical status, and repository commit will be recorded in
the final report. A halfway `checkpoint.md`, nine-field `report.md`, and
`SHA256SUMS` will be produced in this directory only.
