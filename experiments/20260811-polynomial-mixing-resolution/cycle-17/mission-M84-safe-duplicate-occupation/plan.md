# M84 plan: safe-duplicate reachability and occupation

Date: 2026-08-12. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## 1. Objective and exact target

Continue the accepted M78/M81 frontier for the canonical uniform positive-
elimination process on a connected genus-one transposition identity word.
The ambient project target remains the uniform law on `Omega(N,m)` for the
lazy exact same-product `{3,4,5}` heat-bath chain, but this mission studies
only one proposed comparison row law and makes no direct spectral claim.

For an elimination state `(O,R)` with `s=|R|`, call an unordered pair of
positions `{i,j}` safe when `R_i=R_j=p` and deleting the two next equal
outputs leaves

```text
O + R[:i] + (p R[i+1] p,...,p R[j-1] p) + R[j+1:]
```

connected. If there are `a` such pairs, the exact next-two hazard is
`2a/[s(s-1)]`.

## 2. Convention

Permutations compose as `(pq)(x)=p(q(x))`; tuple factors are evaluated
left-to-right; the right Hurwitz generator is `R(a,b)=(b,bab)`; canonical
elimination picks a uniformly random remaining original label at every step,
outputs its current transposition, deletes it, and conjugates all residual
factors to its left by it.

## 3. Named alternatives

Seek one of the following rigorous outcomes.

1. Prove a universal inverse-polynomial lower bound on the total probability
   of hitting a safe duplicate for every connected exterior two-component
   word in the M75 minimal-macro scope.
2. Prove such a bound first for the explicit voltage family `W_L`, with all
   dependence on `L`, `d=8L^2`, and `k=16L^2` explicit.
3. Produce an explicit infinite family for which this hit probability is
   zero or superpolynomially small.
4. If neither terminal alternative closes, give a strictly narrower exact
   reduction with at least one nontrivial proved step and explicit remaining
   lemma.

## 4. Proof program

- Derive exact graph/topological invariants of elimination states, including
  whether canonical elimination is representable as deletion/contraction or
  partial duality of the chronological ribbon graph.
- Characterize duplicates and safe duplicates without enumerating full
  label orders.
- Analyze `W_L` through its `Z_L^2` cover and base `K_(4,4)` quotient.
- Test candidate monotonicity, covering, matroid, and hazard inequalities on
  exact small states before asserting them.
- Separate exact symbolic or exhaustive facts from fixed-seed Monte Carlo.

## 5. Computation and parameters

Use standard-library Python only. Exact tests will prioritize the base word
`L=1`, quotient-aware or bounded-prefix checks for `L=2`, small generic
connected genus-one words, and exhaustive microexamples where completeness is
literal. Monte Carlo, if used, will include fixed seeds and multiple `L`
values and will be labeled empirical.

## 6. Expected failure modes

- A long first-hit depth need not make total hit probability small.
- A selected noncontractible cycle need not be safe (already refuted by M81).
- Zero Monte Carlo hits do not prove zero reachability or an asymptotic bound.
- A state quotient is invalid unless it preserves chronology, conjugation,
  output support, duplicate multiplicity, connectivity, and transition mass.
- A bound for the canonical row law alone is neither a heat-bath bottleneck
  nor a spectral-gap theorem.

## 7. Required artifacts

Write `checkpoint.md` by halfway, auditable scripts plus machine-readable raw
output for nontrivial computations, a nine-field `report.md`, and
`SHA256SUMS`. Remove caches and freeze the owned directory before handoff.

## 8. Reproduction metadata

Record exact commands, parameters, random seeds, Python version, dependency
versions, elapsed time, and the repository commit in every machine-readable
artifact. No external literature dependency is planned.
