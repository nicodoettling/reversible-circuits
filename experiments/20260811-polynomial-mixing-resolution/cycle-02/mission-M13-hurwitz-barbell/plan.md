# Plan: Hurwitz-barbell red team

## Exact target and scope

Attack the proposed uniform inverse-polynomial gap for the lazy symmetric
Hurwitz walk on every connected identity-transposition orbit, concentrating on
the minimal full-support orbit with `N>=3` and `m=2(N-1)`. A literal negative
result for this subchain is only a failure of a sufficient comparison route;
it is not TERMINAL B for the larger `{3,4,5}` heat-bath chain unless the same
cut has its complete `K` boundary bounded.

Permutations are maps on `[N]`; `pq` means `p` after `q`, and a word is
`t_1...t_m`. On a fixed Hurwitz orbit `F`, use

    P_H = (1/2) I
          + [1/(4(m-1))] sum_{i=1}^{m-1} (R_i + R_i^{-1}),

where `R_i(a,b)=(b,bab)` and `R_i^{-1}(a,b)=(aba,a)` for transpositions.
The target law is uniform on `F`.

## Named claims under attack

1. **Braid-abelian quotient obstruction.** Determine whether a cyclic
   coordinate that advances by one under every `R_i` can have
   superpolynomial size or an exponentially thin interval boundary. Account
   for the full-twist stabilizer, exact quotient kernel, stationary masses,
   and both directed boundary flows.
2. **Minimal join-tree / Dyck cuts.** For `m=2(N-1)`, define the prefix
   join/cut word, its height/area statistics, and the tree of join edges.
   Search for a barbell based on tree shape, Pruefer data, or excursion shape.
   Exact enumeration is used only to falsify named structural lemmas and
   proposed finite formulas.
3. **Residual pure-braid modes.** Separate ordinary braid-abelian characters
   from nonabelian Schreier geometry and pure-braid stabilizer quotients. If
   no terminal cut survives, state the smallest remaining proposition.

## Proof and computation protocol

- Prove all infinite statements algebraically, including the exponent and
  action of the full twist.
- For any cut `A`, report `pi_F(A)` and
  `Q(A,A^c)=|F|^{-1} sum_{x in A}P_H(x,A^c)` with every laziness, scan, and
  orientation coefficient.
- If exact enumeration is useful, test only `S_3,m=4` and `S_4,m=6` on the
  minimal full-support orbit. Record a fixed seed, Python version, exact
  command, machine-readable output, and the universal claim each field could
  falsify. No finite gap is promoted to an asymptotic conclusion.
- Produce a genuine halfway `checkpoint.md`, then a final nine-field
  `report.md` with dependencies, self-attack, calibration, and exact verdict.

## Expected failure modes

- The full twist may bound only ordinary abelian characters and leave
  nonnormal stabilizer or pure-braid Schreier bottlenecks untouched.
- A join-tree statistic may fail to be Markov, uniformly distributed, or
  locally controlled by one Hurwitz generator.
- An exponentially rare tree-shape set is not a bottleneck unless its
  outward flow is exponentially smaller still.
- Slow `P_H` does not imply slow `K`; every such conclusion will be labeled
  as a route obstruction unless a complete `K` calculation is supplied.
