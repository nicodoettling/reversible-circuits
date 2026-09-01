# M134 plan: fresh referee of frozen M132

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Objective and immutable input

Independently audit the frozen M132 adjacent-value schedule-cover submission.
M132 is immutable. This mission writes only in its own directory and imports no
predecessor experiment code or result file.

The auxiliary target is uniform on

```text
Z_d={(t_1,...,t_(2d-2)): t_1...t_(2d-2)=id,
                              support connected on [d]}.
```

Permutations compose as `(pq)(x)=p(q(x))`, displayed factors multiply
left-to-right, and the signed right-Hurwitz moves are

```text
R_j(a,b)=(b,bab),       R_j^(-1)(a,b)=(aba,a).
```

## Audit obligations

1. Verify all assigned M132 hashes before inspecting the claims.
2. Reimplement the accepted `+` DPS closure, brute `Z_3,Z_4`, canonical rooted
   representatives, descended adjacent-value maps, and signed Hurwitz action.
3. Reproduce the displayed `d=4,i=1` source/target words and equality of every
   field in the defined polynomial contour descriptor.
4. Independently enumerate the paired subgroups and compare them with the hand
   descriptions of orders `96` and `288`.
5. Audit the descriptor range bound, including the unique distance-three event
   per label needed for the `(S+1)^10` factor.
6. Recompute the complete `d=3` conflict graphs, clique/chromatic numbers,
   signed action image, agreement masks, and exact minimum schedule cover.
7. Check the conditional prefix-recovery, compressed-time, index, and exact
   factor-`d` root-quotient scope; distinguish finite or capped searches from
   asymptotic statements.
8. Issue `ACCEPT` or `REJECT` with numbered material objections, then freeze an
   independent checker, raw JSON, report, manifest, and checksums.

## Failure conditions

- Any mismatch in the displayed DPS certificate or full descriptor.
- A source/target subgroup equality, wrong hand description, or wrong order.
- A hidden superpolynomial descriptor field invalidating the `O(d^40)` claim.
- Failure of the necessary-coloring implication or any `d=3` exact figure.
- Promotion of a capped non-finding, finite cover, or conditional recovery to
  an asymptotic schedule-cover, congestion, or gap theorem.

The audit proves no UST basis-exchange routing, physical gap, `Gamma_0` bound,
original heat-bath gap, Terminal A, or Terminal B result.
