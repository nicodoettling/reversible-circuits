# Mission M276 checkpoint

Status: **initialized before M272 inspection**.

The owned audit directory, plan, and checkpoint were created before opening
the frozen M272 payload.  The project skill has been read completely.  Next:
read the required repository source-of-truth files, verify the advertised M272
inventory digest, and only then inspect the immutable bundle and dependencies.

## Immutable gate

The advertised M272 checksum-file digest matches exactly:

```text
af54db1f8bf948ee15439aeee5330d5b18ea7101e2dba062c47c8f949262eed3
```

Every M272 payload passes its inventory.  The five declared dependency
inventories also pass, with checksum-file digests

```text
M91   0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703
M94   47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562
M261  b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b
M264  b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f
M267  001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6
```

The transitive M270 audit inventory also passes; its digest is
`6c0c6e13c62885a0c56e8c232c0f2ddc48922be56b3edce97a4f9c9b9ca5491e`
and its frozen verdict accepts M267 only at the stated endpoint-profile
scope.

## Predeclared independent checker

Before opening either M272 script or JSON artifact, implement one
self-contained standard-library checker, with no imports from or reads of
M272 code/data.  At exactly `k=3,5`, rebuild minimal-factorization counts
from cycle decompositions and check:

1. raw `H_(j,A/B)`, `p,q,Phi,Psi` normalizations and the measure Abel law;
2. the quantile `q`-to-`p` coupling, support `S<=T`, and crossing mass
   `Pr(S<=u<T)=-D_u`;
3. null-owner `E_ell`, the outside phase factor `1/n`, the literal good/bad
   first-edge partition, and a nonzero good vector at `k=3`;
4. the channel-one face/cross-convolution collision identity;
5. channel-two shared-endpoint probabilities and total masses, the nonzero
   disjoint endpoint, and the vector Abel identity.

Finite checks can refute exact identities only.  They cannot prove any BV
estimate or downstream conclusion.

## Final checkpoint

The checker passed every predeclared assertion at `k=3,5`.  Its phase
good/bad and channel-two signed-vector values make ten exact matches to the
frozen M272 results.  Both original M272 checkers were then rerun to `/tmp`
at `k=3,5,7`; each complete result array matches its frozen JSON exactly.

The raw laws, channel normalizations, quantile crossing identity, full path
telescoping, phase `1/n`, phase partition/refutation, channel-one collision
identity, and channel-two triangle/vector Abel reduction pass.

One material frozen-proof objection remains.  M272's channel-one BV proof
asserts every term is `O(k^-3/2)` on `k/2<a<=k`, but

```text
rho_A(k-1)=nu_k(1)=(k-1)^(k-3)/k^(k-2)=Theta(1/k).
```

Its subsequent displayed tail estimate is stated only for `a>k`, where
`rho_A=0`, so the short-cycle `A` tail is not proved in M272.  Under the
strict immutable-package rule the verdict is **REJECT M272 AS FROZEN**.

`proof_audit.md` supplies an append-only repair:
`rho_A(k-c)=c nu_k(c)` has adjacent variation
`O(1/(k c^(3/2))+1/(k^2 sqrt(c)))`, summing to `O(1/k)`.  With the corrected
range partition this proves the channel-one collision derivative `O(1/k)`
in M276, pending fresh audit.

Final open hierarchy:

```text
CSBV + CEBV => CIBV,
CIBV + DOR  => PBV <=> SET.
```

`CSBV`, `CEBV`, `CIBV`, `DOR`, `SET`, `PBV`, `FD`, `FCL1`, every gap,
mixing statement, and Terminal remain unresolved.
