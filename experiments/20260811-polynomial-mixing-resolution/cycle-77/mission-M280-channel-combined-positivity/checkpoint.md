# M280 checkpoint

Status: source lock complete; exact formula reconstruction in progress.

The required project skill, core source-of-truth documents, and experiment
standard have been read. The mission directory and plan were created before
substantive formula work.

All ten required inventories pass `sha256sum -c SHA256SUMS`. Their observed
checksum-file digests are:

```text
M161 17bd62a9b121a10058f87c576275411186e1c3c5039fa07a9cf29c9bea7358d8
M166 344b6c76e538ecc82ac64ace908a21aabfb805330bad8a72c6ba042831e869c3
M168 3f86fc364d1809752d06085eddad8b2e75132ea03c1d27d5a87e9ec3b1cb84bd
M171 c47a095db5925fe69fe1756080943523376b4194b5a4cb3f6d112d8c7306fe2d
M174 fea1f624d6b65fb8404eee0324832aa601e1bf4f202598b60a6608b1a23a51ba
M178 6ca82e9fe821c5a56b4d590dab28b29bf5e4cbc3c0af0a91c0538a53abd51fba
M266 6203ef0dca1e2c46696cec5bc1446da9656ace2b8a3a4ce9b2131267b200c052
M268 62976d7adca32d4ea7819ad36c7623430e26f75eced98a7b88bec58a4d0de2ef
M274 c3bdadca0f95679fed1fbcf461e60cf01bc4d669cc087e90792c29ec4d4a6e4e
M277 c419b7c95e7c6fe4086d1098d6f0578445a1c3af700cabe4e90cf90d7c39d890
```

Accepted scope retained: PCS is proved only for the first auxiliary fixed
cell; CP, OS+, MS, and FCL1 are open. M277's nonmaterial corrections are
also retained: M274's checker has a transitive NumPy dependency, the `k=9`
minimum is tied at `y=7,18`, and the all-rank atom obstruction concerns the
displayed literal ordered-atom decomposition only.

Next: derive the fully recombined channel coefficients from M91's normalized
conditional laws, preserving the direct `T/D`, `IS/IN/X`, cyclic-phase, and
endpoint/reflection terms.

## Final checkpoint

The exact reconstruction is complete in `channel_positivity_reduction.md`.
CP is equivalent to the two owner-correlation inequalities `(OCI_1)` and
`(OCI_2)`, with complete raw and Abel formulas displayed.  The exact
monotone split transport supplies only an endpoint expectation identity and
does not furnish a pathwise sign; the known MON/FOSD/raw-atom firewalls
remain decisive.

The sole predeclared new falsifier ran at `k=11`, every one of the 30 target
lags, and both channels.  All 60 exact channel values are positive; minima
occur at reflected lags `y=9,22`.  Multiple retained kind/topology pieces
are negative, so this is recombined finite positivity only.  CP, OS+, MS,
and FCL1 remain unresolved.  The report and fresh-audit request are ready;
mission-local syntax, JSON, whitespace, and cache checks pass.
