# M41 plan: adjacent-value parking-flow congestion

## Objective

Resolve the exact minimal-long-cycle implication left by M35:

> Route the adjacent-value Lorentzian parking chain `A_r` through the
> stationary-flow projection `bar P_r` of the actual adjacent rank-two
> heat bath with path length and total congestion polynomial in `r`.

M35 proves `gap(A_r)>=r^-7`. A polynomial comparison would therefore prove
an inverse-polynomial gap for the parking-multiset projection. This remains
only one stratum of the base-scale fixed-endpoint theorem and is nonterminal.

## Convention and laws

Composition is `(pq)(x)=p(q(x))`, with tuple products read left to right.
States are parking count vectors

    J_r={m: sum_i m_i=r and sum_{i=0}^k m_i>=k+1 for every k<r},

with stationary law

    pi_r(m)=r!/(r+1)^(r-1) prod_i 1/m_i!.

`A_r` retains from the M36 delete/reinsert chain only positive moves
`m->m-e_i+e_j` with `|i-j|=1`, rejecting all other moves. `bar P_r`
is the exact stationary-flow projection of the uniform adjacent rank-two
heat bath on minimal factorizations of a fixed `(r+1)`-cycle.

## Work program

1. Independently audit the M35 reduction `gap(A_r)>=r^-7`.
2. Derive exact actual-flow formulas for the warning family
   `0^a 1 2^b -> 0^a 2^(b+1)` and its proposed longer buffer detours.
3. Extend the M39 exact harness to aggregate *simultaneous* comparison load
   for named deterministic or fractional routing rules. Individual widest
   capacity is not enough.
4. Seek an injective metadata/recovery theorem or a stationary randomized
   flow whose path length, mass ratios, and edge multiplicity are all
   polynomial in `r`.
5. If a routing rule fails, freeze the smallest exact counterexample or an
   asymptotic exponential-load family. Such a failure refutes only the rule,
   not Terminal A or Terminal B.

## Calibration and failure modes

- M32's balanced binary exchange has a genuine polynomial two-hop bypass.
- M35's `0^a 1 2^b` family is adjacent-value but every nontrivial two-hop
  stationary bottleneck is exponentially weak when `a,b` are balanced.
- M39 proves unrestricted ideal edges first require distance three at
  `r=5` and distance four at `r=7`; adjacent-value reachability happened
  to remain within two steps through that finite range.
- The parking stationary weights are factorially nonuniform. Transition
  probability without stationary mass is not capacity.
- A canonical buffer macro of exponentially small mass or a one-commodity
  widest path cannot establish polynomial total congestion.

## Required deliverable

Return the nine-field proof schema. The exact verdict must be `PROVED`,
`REFUTED`, or `OPEN AT A NAMED STEP` for ADJACENT-VALUE PARKING FLOW.
No finite positive result is a universal proof.
