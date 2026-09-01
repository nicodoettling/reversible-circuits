# M251 checkpoint

Status: exact paired-domain identity proved; analytic estimates active.

- Mission directory initialized before inspecting prior mission details.
- Exact target is the **unweighted** adjacent-split DV sum from the mission
  assignment; no `q` or `qhat` weight will be introduced.
- Immutable M192/M195 and M199/M207 were audited.  Their exact conventions,
  normalization, triangular tuple domains, one-/two-run atoms, and collision
  multiplicities agree.
- `paired_difference_identity.md` proves the exact common-domain `s -> s+1`
  identity.  It pairs the expanding short and shrinking long pieces before
  absolute values and isolates survivor/cutoff, common kernel, common seam,
  boundary strip, and normalization blocks.
- The leading `1/R` derivatives in the normalization cancel exactly.  The
  paired strip identity also cancels its common `b_d/R` kernel before leaving
  likelihood-ratio, seam/cutoff, and unmatched-tail terms.
- The seam-free Borel cumulative increment was subsequently proved by an
  exact convolution bound and a far-parent likelihood-ratio expansion.  A
  discarded monotonicity shortcut was false and is not used.
- Constant annihilation plus finite Abel expansion proves the complete
  `Y`-profile DV estimate with explicit constant `18400`.
- The sole remaining `X` obligation is the literal complementary two-run
  adjacent variation `(TAV)` in Section 5 of `y_dv_theorem.md`.
- Final verdict: proved paired identity and `Y-DV`; unresolved `TAV/X-DV`;
  no downstream inference.  Freeze and fresh-audit preparation is active.
- Current verdict: `unresolved`.
