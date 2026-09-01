# Mission M266 Plan: Full DV-to-PCS Assembly

## Objective

Assemble, without redoing the accepted component calculations, the fixed-cell
response theorem obtained from the independently audited M251/M255 Y-response
bound and M258/M263 exact two-run comparison.  Then trace its constants and
domains through the accepted difference estimate (DE), M252/M253 WPCR, and
M256/M259 response chain through the proved PCS bound.

## Declared target and scope

The ambient sampler target remains the uniform law on the fixed-length bridge
space

```text
Omega(N,m) = { (t_1,...,t_m) in T_N^m : t_1 ... t_m = id }.
```

This mission concerns only the fixed-cell analytic response chain used in the
current comparison proof.  It does not prove FCL1, a bridge-chain spectral
gap, polynomial mixing of the local `{3,4,5}` heat-bath chain, or a terminal
resolution.

## Required source artifacts

Verify the immutable manifests and inspect the theorem passages for:

- M192/M195 (DE),
- M217/M222 (SCBR/BR/BIR and PCS route inputs),
- M248/M249 (preceding exact fixed-cell reduction),
- M251/M255 (Y-DV, constant `18400`),
- M252/M253 (full DV + DE implies WPCR),
- M256/M259 (WPCR-to-PCS response chain), and
- M258/M263 (exact `X-Y=Theta`, TAV constant `500`).

Record M256's nonmaterial correction to the cited M166 manifest hash.

## Deliverables

- `assembly_proof.md`: compact theorem, exact domains, constants, and
  dependency chain.
- `verify_assembly.py` and `results.json`: deterministic checks of the
  arithmetic substitutions, channel normalizations, and exceptional-case
  domain table.
- `checkpoint.md`: substantive checkpoint.
- `report.md`: verdict and exact remaining stop.
- `freeze_manifest.sha256`: immutable file digests.

## Acceptance discipline

The intended conclusion is a proved fixed-cell response/PCS bound conditional
only on the already accepted named dependencies.  The final report must retain
singletons, endpoints, `k=3`, and odd-`n` handling; must not claim PCR; and must
state FD/minority-sign as the exact remaining stop before FCL1.
