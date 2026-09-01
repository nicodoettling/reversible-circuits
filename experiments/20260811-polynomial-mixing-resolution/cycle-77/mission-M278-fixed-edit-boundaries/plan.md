# M278 plan: arbitrary-rank fixed-edit DPS boundaries

## Objective

Prove, refute, or strictly reduce the literal arbitrary-rank DPS
boundary-factor shapes for the fixed edit families omitted from the accepted
ordinary odd-edit route.

## Exact target

For every `d>=5` and every tree on `[d]` rooted at leaf `d` with `{1,d}`:

```text
internal even i<=2d-6   : identity,
i=2d-4                  : (R_(2d-5)^(-1))^2,
i=2d-3                  : R_(2d-2)^(-1).
```

Derive the exact old-padded/new DPS source and target factors which make the
unconditional tuple identities apply.  Include chronological composition,
signs, root/new-child slots, post-wrap cases, and the minimal boundary
`d=5`.

## Immutable gate

Use only frozen M225/M228, M231/M234, M236/M237, M240/M242, M269/M271,
M273/M275, and the locked DPS source.  Verify every inventory before use.
Do not edit any predecessor.

## Method and stopping line

1. Reconstruct each fixed edit directly from the DPS incidence map and
   cyclic LIFO closure.
2. State and prove an analytic all-rank boundary-shape theorem, or identify
   the first false row and give an arbitrary-rank obstruction/minimal repaired
   state.
3. Only after freezing the formulas, run a tiny predeclared `d=5,6` guard.
4. State the formal composition with accepted ordinary routes, but do not
   infer every-color synchronization, voltage, congestion, a gap, mixing, or
   Terminal before a fresh audit and separate assembly.

## Deliverables

- `checkpoint.md`
- `fixed_edit_boundary_theorem.md` or a strict obstruction note
- optional `guard.py` and `guard_results.json`
- `report.md`, `freeze_manifest.md`, and `SHA256SUMS`

## Status

Initialized; substantive dependency inspection has not begun.
