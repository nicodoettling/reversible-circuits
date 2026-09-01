# M269 checkpoint

Status: analytic theorem and four-row guard complete; ready to freeze.

## Immutable source lock

The six frozen inventory files used by this mission have SHA-256 digests

```text
M250  243b86178d3badea9d7ec88ee03feb36be4d51d841c997e98982ad21d2ede3b7
M254  77f099e14959a0d0e3730ab26fca7ddf230f97f1cfbda86f6d7d93b4e8e8ca04
M257  9250c4692a4bf56df675e389fd605ee492b33840010720e7c0e83420dd64e6b1
M260  eec582cb89b5c472658fb05e992e3b549e9e796b774ab5042e3ee712b1a82144
M262  eafeb1d890030f0e30baf424193adf53c1658fc8b9f4568e0bd9de1b524def0a
M265  ced42bf8a6ccd7ca9ffffdca94919c366273b712875cfe08eeead393b88193f8
```

M265's inventory was also checked entry by entry. M265 independently checks
the M262/M257/M260 and M250/M254 gates in its proof audit, so the accepted
dependency boundary is unchanged.

## Halfway result

Reindex the cyclic labels by declaring `R_v` to have position zero. If the
current strict internal path vertex is `a`, put

```text
r_v(a) = (R_a-R_v) mod M,       1 <= r_v(a) <= M-1.
```

Direct CP-5 insertion into a bare CP-2 parent row produces the literal lens

```text
F_v(r) = S S B_v^(r-1) ... B_v^1 S^(R_v)
             W_v^1 ... W_v^r S S.
```

The analytic token calculation now being formalized gives the corrected
bare-row transition

```text
F_v(r) -> F_v(s),  if s<r,
F_v(r) -> C_b,     if s>r,
```

where `s=r_v(b)` for the next strict internal parent and `C_b` is the
canonical one-open residual at `b`. Thus `O^-`/`O^+` alone is not sufficient:
the cyclic width (equivalently the endpoint order type) is forced. The proof
will list every distance-three row and will not cross the rank-dependent
`a=1` seam.

No CPR, RST, IDL, routing, gap, mixing, or Terminal claim is promoted here.

## Final checkpoint

The bare lens required one exact extension after the full CP-2 child audit:
rooted children of `v` whose cyclic slot lies below the current width remain
as literal ports. Canonical siblings at every later path parent, including
post-wrap siblings, reduce by an exact two-row distance-three macro. With
that decoration, initialization, contraction, expansion, and sealed
propagation are proved for all strict internal rows. The four declared
symbolic guards pass; their machine-readable output has SHA-256
`20b23422f39b0cf5c9af91b30a289d6ce64da2f900ea2543eb1d599653c02fe2`.

The first unresolved step is DL-RST at `a=1`, including the new child `d`
and final root completion.
