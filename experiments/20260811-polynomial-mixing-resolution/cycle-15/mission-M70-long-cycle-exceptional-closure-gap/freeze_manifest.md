# M70 frozen referee bundle

Frozen: 2026-08-12. Repository commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

The following files are immutable for the first fresh referee pass:

```text
202500636dd2a1ef730359b19a7fd72621e00b6c19c4cdb25979708e01b1e29d  plan.md
71bcbecab47566114be4dfb1ef19c0cae9e8be56c288aa2d9dbd2fe7c607d63b  checkpoint.md
1a0d4f5de74feb7597a0333046875168c5b5040a83db27cd6dd4c87f430fbdf6  theorem.md
9ff75c1a9ddb9ecc366609e4dc76f37d511c5f6befa05cb8c4ad5bf19d10eeda  report.md
72efac625867105b914e6f19a38927a3cec374711db83f43be7e8003d674086b  n7_exceptional_krylov.py
4d9151b0decefb47ad89c4a61d4c3a01218e0e787864cc4de824e0a93a270803  n7_exceptional_krylov.json
d7c5b0de6333224cb3cc7cd10fff604b1d4982c92f844cd3f3d9e1a7fd2bce32  h0_parking_projection.py
a9ed1ef7fb2ff4eba9051536e34f46952f22978475f002e13426c213f0e517d4  h0_parking_projection_n7.json
```

## Fresh-referee request

Return `ACCEPT` or `REJECT` with numbered objections. Check independently:

1. the exact additive variance and conditional-projection Rayleigh bounds,
   including all `C_l`, `B_l`, and half-lazy `{3,4,5}` scan coefficients;
2. the project Hurwitz convention, `delta^m=mathcal U`, telescoping occurrence
   count, and the factor four in the heat-bath comparison;
3. the full-state, macro-changing edgewise padding proof
   `E_B>=M^-4 E_L`, rather than importing M27's fixed-multiset theorem;
4. the sine-frequency constants, odd-`n` character indexing, and the direct
   `C_l`/`K^h` comparison constants;
5. the claim that the whole Krylov closure lies in `H_1` and therefore has an
   inverse-polynomial lower gap;
6. freeness of cyclic conjugation, orbit count, stationary-flow quotient, and
   the exact interpretation/rank certificate for `nu_O`;
7. every scope exclusion: no bound on `H_0`, no lift to identity-conditioned
   original `K`, and no Terminal A/B inference.
