# M92 plan: arbitrary-macro signed cover or direct coarea

Date: 2026-08-12 UTC. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and exact scope

Work only on the accepted two-component minimal-exterior frontier after
M75/M77, M84/M85, and M86/M89.  The global background target is uniform on

```text
Omega(N,m)={w in Trans(S_N)^m:eval(w)=id}
```

for the literal lazy exact same-product `{3,4,5}` heat-bath kernel.  At
minimal ambient length `m=2N-2`, a two-component exterior macro has one
connected genus-one component and one connected genus-zero component.
M75's marked set consists of states with a globally adjacent square in the
genus-one component whose deletion leaves that component connected.

The convention is `(pq)(x)=p(q(x))`, tuple factors are evaluated
left-to-right, and signed Hurwitz generators are

```text
R_i(a,b)=(b,bab),        R_i^(-1)(a,b)=(aba,a).
```

Target one of the following, without claiming more:

1. a polynomial-time state-independent law on bijective signed-Hurwitz
   transport words, polynomial expected length, and inverse-polynomial
   worst-source hit of the literal M75 marked set for every two-component
   minimal exterior macro;
2. a direct arbitrary-partial-macro first-boundary/coarea inequality with
   polynomial actual-edge occupation; or
3. a rigorous refutation of a natural universal oblivious law.

Signed-Hurwitz paths will remain distinct from unrestricted `H4/H5` moves.
No full-`K`, spectral-gap, mixing, Terminal-A, or Terminal-B claim will be
made without its actual proof.

## Accepted inputs

- M75/M77 randomized bijective first-crossing theorem and exact heat-bath
  normalization `p_H=1/[6(m-2)binom(N,2)^2]`.
- M84/M85 exact zero row for the canonical positive-elimination law on the
  voltage family.
- M86/M89 fixed signed normalizer on the relabel/phase/interleaving symmetry
  class, with polynomial indexed metadata and inverse-prefix recovery.
- Conditional Classification H/transitivity input: if its source and
  conventions are verified, a state-adaptive signed-Hurwitz route of
  polynomial length exists.  It does not itself give a source-independent
  law or polynomial congestion, and the final positive reductions will not
  rely on it.

## Attack plan

1. **Torus certificate.**  Model every connected genus-one component as its
   chronological cellular torus.  Build a deterministic tree-cotree
   decomposition from visible factor/face data and isolate the two leftover
   edges/fundamental cycles.  Determine whether a connected-deletable pair
   can be exposed by a braid depending only on polynomial metadata such as a
   constant number of factor positions, endpoints, and orientations.
2. **Surgery audit.**  Write the literal signed-Hurwitz braid required by
   any proposed certificate.  Reject it if its positional word still depends
   on the full source tree/cotree, rotation data, or an exponential branch
   transcript.  Count expected length, indexed mass, and actual-edge recovery.
3. **Oblivious-law red team.**  Analyze natural random spanning-tree or
   random-arborescence normalizers.  In particular, test whether choosing a
   root/edge order independently of the source produces a fixed positional
   word, or merely hides a source-adaptive branching algorithm behind random
   tie-breaking.  Prove a limitation when possible.
4. **Exact falsification only.**  Use small connected genus-one identity
   words to test proposed local certificate/surgery statements.  Computation
   will not be used to prove an all-size claim.
5. **Report and freeze.**  Produce a halfway checkpoint, a nine-field report,
   machine-readable exact output for any finite audit, hashes, and clean
   bytecode-cache status.  Do not edit predecessors or shared durable files.

## Named failure modes

- a canonical tree/cotree requires `Theta(N)` source-dependent choices whose
  branch words have exponential support with no row-mass or overlap bound;
- a topological witness identifies a nonseparating curve but not a literal
  equal-factor collision or connected deletion;
- polynomial word-family cardinality is substituted for weighted expected
  occupation or inverse-prefix actual-edge recovery;
- a braid is recomputed adaptively from the unknown source after sampling;
- a signed-Hurwitz claim is silently promoted to an `H4/H5` or full-kernel
  statement;
- finite positive checks are promoted to a universal theorem.

## Environment and reproducibility

Python: `3.12.3`.  Prefer deterministic standard-library scripts, run with
`PYTHONDONTWRITEBYTECODE=1`; fixed seeds will be recorded if randomness is
used.  Exact commands, parameters, elapsed time, and scope warnings will be
stored in outputs and the final report.
