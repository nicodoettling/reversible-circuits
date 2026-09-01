# M298 report: fresh audit of frozen M295

Date: 2026-08-14 UTC.

Verdict: **ACCEPT** with zero material objections and one nonmaterial
notation qualification.

## Strongest independently verified result

The channel-one fixed-middle candidate

```text
FMCP_1:  sum_e gamma(e)F_ell(ef) >= 0
```

is exactly false at `k=5`.  The exact minimum is attained at
`f=(6,9)` and the reflected lags `ell=6,9`:

```text
-779985545058827083283361063988362608513
/11367752922135489592720891699200000000000.
```

Exactly 16 of 120 fixed-middle cells are negative.  Nevertheless, every
fully `nu_M`-weighted channel-one lag remains strictly positive.  Hence this
is a counterexample to `FMCP_1`, not to `GOCI_1` or `OCI_1`.

## Audit evidence

- M295 top inventory digest is exactly
  `42fa1c38b08359ae949fa0076557c2d42fdda232d1e7b318432e6787795ca3e5`;
  every listed file passes and the inventory is exact.
- All eight cited predecessor inventories pass and match ledger entries
  L-0302, L-0306, L-0309, and L-0311.
- `independent_fmcp_audit.py` reads no M295 artifact and reconstructs chord
  laws, residual cycles, repaired owner autocorrelations, positive cyclic
  compositions, and source normalization with exact `Fraction` arithmetic.
- Direct, repaired, and positive-composition `eta_1` values agree for every
  admissible lag.  A later post-hoc comparator matches all 120 M295 cells and
  all twelve scaled and unscaled full lag values.
- Exact multiplicities are three for triangles and four for `S/N` doubles;
  the anchor is already a support vertex, so there is no extra `n`.
- Both channel-two source laws have mass one; the split source has first-
  component masses `1/2,1/2`, so no extra channel-two `1/2` is permitted.
- Replaying M295 reproduces its frozen raw-output hash byte-for-byte.

## Numbered objections

### Material

1. None.

### Nonmaterial

1. Retain “designated exterior/middle channel-one decomposition” whenever
   writing the scalar shorthand `beta_1(ef)=gamma(e)nu_M(f)`.  The shorthand
   is exact in scope; unrestricted rank-two ordered products have multiple
   lifts.  The atom-summed fixed-middle identity is unambiguous and exact.

## Claim ledger

| claim | status | evidence | action |
|---|---|---|---|
| M295 frozen inventory | verified | top and per-file SHA-256 | accept immutable package |
| designated `beta_1=gamma nu_M` and fixed-middle disintegration | proved | Section 2 of `proof_audit.md`; injectivity plus atom sum | retain with qualifier |
| direct = repaired = positive composition | proved at exact `k=5` audit scope | `independent_results.json` | retain as finite checker validation |
| triangle/double factors `1/3,1/4`; no `n`; no channel-two extra `1/2` | proved normalization identities | exact multiplicity and completion enumeration | retain |
| universal `FMCP_1` | refuted | exact negative witness, 16/120 count | do not reuse |
| all full `eta_1` lags at `k=5` | exact finite positive fact | twelve exact fractions and post-hoc equality | do not extrapolate |
| `GOCI_1`, `GOCI_2`, `OCI`, CP/OS+/MS/FCL1 | unresolved | no all-rank proof or counterexample | remain open |
| gap, mixing, Terminal | unresolved | out of scope | no inference |

## Scope firewall

The audit refutes `FMCP_1` only.  It does not establish or refute
`GOCI_1`, `GOCI_2`, `OCI`, `CP`, `OS+`, `MS`, `FCL1`, a spectral gap,
polynomial mixing, or either Terminal.  The exceptional main-chain cases
`m` odd, `m=0`, `m=2`, and `N=2` are not implicated because this is an
already-reduced auxiliary fixed-cell calculation.
