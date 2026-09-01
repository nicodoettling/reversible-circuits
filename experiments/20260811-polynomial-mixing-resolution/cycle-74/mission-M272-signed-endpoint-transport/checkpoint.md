# M272 checkpoint

Status: first exact coupling checkpoint; `SET/PBV` unresolved.

The required project skill and source-of-truth documents have been read.  All
files named by the frozen M91/M94/M261/M264/M267 checksum ledgers pass
`sha256sum -c SHA256SUMS`.  Their checksum-ledger digests are

```text
M91   0274b7993e908095f7620d3c14a2909b51f404181f4824d605fa92e3ac7bf703
M94   47476a726ffd78a3a53b0547494c7e6b67755fa8dd2ff9d1225515032b5e8562
M261  b3d04b071d417c0d8364f4cc254937c963a84d52f743f804557836455f74007b
M264  b0059b10a09a5bb5859d813007b6f21b4d72d3fc96db0b8938df6210741c057f
M267  001f9aca8d2b75117cc85349355f0f787d433cb14399c64599752f6d09135aa6
```

`adjacent_transport.md` now constructs exact literal couplings of
`Phi_(j,u)` and `Phi_(j,u+1)` for both M91 channels.  Channel one shares the
middle factor; channel two uses an explicit maximal coupling of the exact
completion-count conditional second-factor laws.  It proves

```text
sum_K <w, sum_j alpha_j sum_u D_u A_(j,u,K,ell)>
 =1/n sum_j alpha_j sum_u D_u
    E_C[j,u][E_ell(s)-E_ell(t)].
```

The formula retains `T/D` outcomes, literal phase, owner-pair `kappa`, both
channels, signed `D_u`, and the phase-average factor `1/n`; no absolute value
or statewise envelope has been applied.  This identity was rederived from
the M91 marginal laws and the owner selection in M261, rather than assumed
from M267.

Current labels:

- Adjacent-split coupling identity: `proved exact`.
- Full monotone split/embedding path identity: `proved exact`.  The quantile
  split coupling has crossing mass `-D_u`, so path telescoping combines the
  complete `D_u` and `q_u` flows into one coupling of
  `sum q_u Psi_(j,u)` and `sum p_u Phi_(j,u)` before any cost.  Its endpoint
  formula is `(5.8)` in `adjacent_transport.md`.
- SET/PBV/FD: `unresolved`; the remaining required factor `1/n` must come
  from literal phase/two-cycle geometry or the combined-channel endpoint
  response, since the statewise envelope after telescoping supplies only a
  constant endpoint cost.
- M267 owner-charge normalization used here: `independently rederived`.
- Exact bad-phase indicator and combined-channel partition: `proved` in
  `phase_incidence_lemma.md`.  The seam-only shortcut is `refuted` at
  `k=3`: the same-block/nonzero part is nonzero and remains at the target
  finite scale through `k=7`.
- Conditional channel-one collision derivative:
  `sum_ell|eta_1(Delta I_ell)|=O(1/k)` is `proved` analytically from the
  literal ambient-face law and a critical-Borel bounded-variation estimate.
- Channel two: shared-endpoint collision contribution `O(1/k)` and the
  vector-valued disjoint Abel identity are `proved`; the signed disjoint
  bounds `(CSBV)/(CEBV)` remain `unresolved`.
- Full channel-combined collision `(CIBV)` and decorated owner-ratio
  transport `(DOR)`: `unresolved`.
- No claim about FCL1, the sampler gap, mixing, or a terminal outcome.
