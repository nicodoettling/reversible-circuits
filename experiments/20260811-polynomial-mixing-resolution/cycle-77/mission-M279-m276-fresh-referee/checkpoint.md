# M279 checkpoint

Date: 2026-08-14 UTC.

Status: complete and frozen.  Source gate, independent analytic repair,
finite clean-room guard, fresh audit, and final disposition all pass.

The project source of truth, goal specification, reversible-circuit-sampler
skill, and sampling-problem reference were read first.

## Immutable source lock

Every payload in each cited inventory verifies.  The independently computed
inventory-file digests are

```text
M276  882de0a7f8365d3eea17db14adb193860250e1df0772f5257e3fbaa9c2d666db
M272  af54db1f8bf948ee15439aeee5330d5b18ea7101e2dba062c47c8f949262eed3
M91   0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703
M94   47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562
M261  b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b
M264  b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f
M267  001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6
M270  6c0c6e13c62885a0c56e8c232c0f2ddc48922be56b3edce97a4f9c9b9ca5491e
```

## Substantive analytic checkpoint

M272's frozen proof is materially invalid at its claimed near-end bulk step.
For `a=k-1`, the short-cycle term is

```text
rho_A(k-1)=nu_k(1)=(k-1)^(k-3)/k^(k-2)=Theta(1/k),
```

whereas M272 asserts `O(k^-3/2)` for every summand on that range.  Its next
tail formula starts only at `a>k`, where `rho_A=0`, so it does not repair this
omission.

Independently put `c=k-a`, `h_c=c b_c`, and
`R_k(c)=b_(k-c)/b_k`.  For `1<=c<k/2`, exact Borel algebra gives

```text
g_k(c)=rho_A(k-c)=h_c R_k(c)/(k-1).
```

The ratio identity

```text
r_j=b_(j-1)/b_j=e(1-1/j)^(j-2)
```

implies `R_k(c)=product_(i=0)^(c-1)r_(k-i)=O(1)` and
`|R_k(c+1)-R_k(c)|=O(1/k)`.  Stirling plus the exact adjacent ratio gives

```text
h_c=O(c^-1/2),
|h_(c+1)-h_c|=O(c^-3/2).
```

Therefore

```text
g_k(c)=O(1/[k sqrt(c)]),
|g_k(c+1)-g_k(c)|
 =O(1/[k c^(3/2)]+1/[k^2 sqrt(c)]).
```

Adding the boundary `g_k(0)=0` yields total variation `O(1/k)`.  The same
argument handles the long-cycle small-complement tail.  Its central `B`
range has per-chord size `O(k^-5/2)`, adjacent difference `O(k^-7/2)`, and
piecewise-linear counts `O(k)`, hence variation `O(k^-3/2)`.  The two
junctions have the neighboring bounds (the `a=k`/`a=k+1` long-cycle values
even agree exactly).  Combined with M272's unaffected low-range cancellation,
this proves `TV(rho_B-rho_A)=O(1/k)`.

The exact collision identity then gives the corrected channel-one/J1 bound:
the face terms cost `O(1/k)`, while each convolution term is at most
`||a_B-a_A||_1 ||Delta m||_1=(2/k)(4/k)=8/k^2`.

The raw-law normalizations, stochastic `q`-to-`p` coupling and `-D_u`
crossing mass, telescoping sign, outside phase `1/n`, literal phase
partition, channel-two shared masses, nonzero disjoint endpoint, and vector
Abel boundary term have also survived formula-level reconstruction.  Their
finite clean-room guard passes at the predeclared ranks.  Its normalized
result digest is

```text
39f879bc696d59f5d850ad7d39c9352eb7626353d0d4d18480feaefd8f649cf9.
```

M276's own no-read checker was replayed to `/tmp`; its output is byte-equal
to the frozen result and has SHA-256
`99611a4d3fa23cb6d092f89da9fbeff0ff5ef2d828d3fd2b1440d1bc09b16f09`.

## Final disposition

```text
ACCEPT M276'S APPEND-ONLY SALVAGE.
MATERIAL OBJECTIONS TO M276: NONE.
NONMATERIAL OBJECTIONS TO M276: NONE.
M272 AS FROZEN REMAINS REJECTED.
```

The exact surviving hierarchy is `CSBV+CEBV => CIBV` and
`CIBV+DOR => PBV <=> SET`.  Every antecedent and downstream conclusion,
including `FD`, `FCL1`, gaps, mixing, and both Terminals, remains unresolved.
