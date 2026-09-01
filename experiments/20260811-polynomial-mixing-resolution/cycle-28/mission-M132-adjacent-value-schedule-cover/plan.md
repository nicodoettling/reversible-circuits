# M132 plan: adjacent-value polynomial schedule cover

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and exact target

Work in the uniform minimal connected identity sector

```text
Z_d={(t_1,...,t_(2d-2)): t_1...t_(2d-2)=id,
                              support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`; displayed tuple factors multiply
left-to-right. The physical moves are signed adjacent right-Hurwitz actions

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

For the accepted rooted DPS coordinates `(T,pi)`, let `tau_i` be the physical
involution induced by swapping adjacent values `i,i+1` of `pi`. Test the
standalone claim:

> For every `d>=2` and `1<=i<2d-2`, `Z_d` is covered by `d^O(1)` agreement
> sets of fixed signed braid words of length `d^O(1)` implementing `tau_i`.

This target is only the adjacent-permutation coordinate of the ideal rooted
product chain. It is not the global fixed-length bridge target, a route for
UST exchanges, an all-edge comparison, or a gap theorem.

## Method

1. Reconstruct the root-independent endpoint map and exact signed-Hurwitz
   action on complete `d=3,4` DPS states without importing predecessor code.
2. Extract natural contour metadata for the two swapped labels: endpoint
   vertices, cyclic incidences, local closure status, and affected output
   interval(s). Group sources by increasingly coarse metadata.
3. Search for one fixed schedule per metadata class, first by exact action-
   image closure at `d=3`, then by bounded bidirectional schedule synthesis at
   `d=4`. Verify every proposed class against every source in that class.
4. If the metadata yields a stable symbolic family, prove the class-count,
   route-length, scheduled/compressed recovery, and exact factor-`d` root
   quotient. If it fails, freeze the smallest explicit metadata collision or
   invariant obstruction and state the surviving narrower lemma.

## Named failure modes

- assuming one fixed braid, already refuted by M127/M130;
- reporting a finite `d=3,4` cover as asymptotic evidence;
- allowing a source identifier as “metadata,” which makes class count
  exponential;
- bounding conditional source recovery while omitting total descriptor count;
- omitting scheduled holds or compressed-time multiplicity;
- omitting the exact `d` white-root quotient;
- inferring UST routing, all-edge congestion, `Gamma_0`, a physical gap, or a
  Terminal claim.

## Reproduction standard

Deterministic Python 3 standard-library scripts; seed recorded as `null`.
Machine-readable exact output will be JSON. The halfway checkpoint will name
the strongest proved/refuted statement before final synthesis.
