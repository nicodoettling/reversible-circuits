# M229 plan: fresh immutable referee of M226

## Objective

Independently audit frozen M226's strict scalar coefficient reduction of WBE, without attempting either remaining moment lemma.

## Immutable and source lock

- Read the project source lock and only relevant frozen proof context.
- Verify every file in M226's `SHA256SUMS` and its claimed checksum-file digest `a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a` before using it.
- Treat M226 as immutable; M229 owns only this directory.

## Audit obligations

1. Independently derive `G_k(x)` from the surviving and two fragmentation sources.
2. Derive all `B^Y_{k,y}` seam cases from the two-seam incidence atoms.
3. Derive the closed A coefficient from all four sources and the Borel convolution.
4. Verify `S_Y+K_Y` is exactly the coefficient prefix.
5. Verify X minus Y is exactly the signed two-run coefficient prefix retaining kinds, seams, and collisions.
6. Prove only conditionally that YCM+TCM imply WBE and, via audited M217/M222, DE.
7. Reproduce the `k=5` count-five-versus-four shortcut refutation and compact `k=3,5` coefficient checks with clean-room code that imports no M226 code or data.

## Exclusions

Do not attempt YCM or TCM. Do not claim WBE, DE, J2, PCR, a spectral gap, mixing, or either Terminal.

## Deliverables

`checkpoint.md`, `proof_audit.md`, a clean-room checker and results, `report.md`, `freeze_manifest.md`, and `SHA256SUMS`, with explicit ACCEPT/REJECT and numbered objections.

