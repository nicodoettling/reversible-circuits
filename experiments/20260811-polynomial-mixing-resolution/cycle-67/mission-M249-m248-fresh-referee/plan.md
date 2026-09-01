# Mission M249 Plan: Fresh Immutable Referee of M248

## Objective

Audit the frozen M248 WBE/DE assembly at
`cycle-66/mission-M248-wbe-de-assembly` without modifying it.  Return an
independent `ACCEPT` or `REJECT` verdict supported by exact provenance checks,
line-by-line algebra/domain checks, and one compact no-import checker.

## Scope

- Verify M248's complete frozen SHA-256 inventory, including the supplied
  top digest
  `c3726d05943b696c11f8e984fae9aa0ee342d00c0744bd7bf0a0f665acbe8bd8`.
- Verify every cited frozen inventory for M217/M222, M226/M229, M235/M238,
  and M239/M246.
- Independently audit these exact statements and their domains:
  1. `S_Y+K_Y = YCM`;
  2. `X-Y = TCM`, including all kinds, seams, and collision cases;
  3. WBE constants `7000` and `7160`;
  4. the exact normalizer formula and `|N_Z| <= 16/k^2`;
  5. absorption of the normalizer by `4 sqrt(ell)/k`;
  6. DE constants `7004` and `7164`.
- Write a compact no-import algebra/domain checker only.
- Do not inspect or prove DV and do not infer J2, PCR, SCBR, gap, mixing, or
  either Terminal conclusion.

## Method and acceptance gates

1. Read project source-of-truth and skill guidance before audit work.
2. Initialize this plan and checkpoint before opening M248 or dependencies.
3. Record exact frozen file inventories and recompute all file and aggregate
   hashes without modifying source missions.
4. Trace every invoked lemma from M248 to its cited accepted referee report and
   underlying proof artifact; reject on any provenance mismatch or unproved
   strengthening.
5. Re-derive the identities, domains, triangle inequalities, and constants
   independently, checking odd `k >= 3` and `2 <= ell <= (3k-1)/2` plus any
   narrower source domains.
6. Run one deterministic no-import checker for boundary-domain and constant
   arithmetic only.  Its output is an exact implementation check, not a proof.
7. Freeze this mission with report, checker output, manifest, and aggregate
   SHA-256 inventory.  `ACCEPT` requires every gate above to pass; otherwise
   report `REJECT` with numbered objections.

## Status labels

- Source theorems are accepted only to the extent proved and independently
  refereed in their frozen artifacts.
- This mission's algebraic conclusions are labeled `proved` only after both
  provenance and independent derivation pass.
- Checker output is labeled `exact finite arithmetic validation`, never an
  asymptotic proof.

