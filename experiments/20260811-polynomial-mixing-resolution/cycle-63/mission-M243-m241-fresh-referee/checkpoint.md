# Mission M243 checkpoint

Status: substantive audit complete; preparing frozen verdict.

The project skill has been read.  The audit scope and nonclaims were frozen in
`plan.md` before inspecting M241's proof.  Next steps are to read the complete
source lock, verify M241's immutable hash inventory, and independently
reconstruct `R1`--`R3` and only their `SG=128`, `GG2=70` implications.

## Immutable-input verification

- M241's `SHA256SUMS` digest is exactly
  `07918bbf968c93f34cbd252f938b1e6e21566ba2907836872592bb744ef53936`.
- Every file in that inventory passed `sha256sum -c SHA256SUMS` before the
  proof was opened.
- The accepted M226 and M229 inventories also pass.  Their checksum-file
  digests are respectively
  `a40efdff6338c6342d12c92522c940d03d4b4e31efa18bbd492a2a2e2fe0a78a`
  and
  `6b3f53cdefce9ee8f991b5245d658574cc3b488087f9913067d8d3b94a4eb688`.
- Source commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Substantive status

Independent derivations reproduce all three estimates and both advertised
local implications.  The clean-room checker passes every tested odd
`3<=k<=35`, including the empty `k=3` SG domain, empty `x=1` strips,
the telescoping boundary `r=2x`, and all GG2 endpoints.  This is finite
falsification only.  No `YCM` or downstream statement has been audited or
claimed.
