# Final synthesis consistency audit

Auditor: `r3-intermediate-hybrid`, reused after its role freeze. Task started
2026-09-05 15:49 UTC, bounded to ten minutes. This is a consistency audit of
the coordinator synthesis against the frozen role theorems, not new
research or a replacement audit of their complete proofs.

Status: **final; ACCEPT**, 2026-09-05 15:56 UTC. All numbered observations
were resolved in the coordinator's final rewrite. No unresolved material
mathematical or synthesis objection remains.

## Sources inspected

- Coordinator `phase_diagram.md` and `claim_ledger.md` at 15:49 UTC.
- Frozen R1, R2, R3 `report.md`.
- R1 `fresh_dense_audit.md`, final accept at 15:46 UTC.
- R2 `fresh_short_audit.md`, final accept.
- The first coordinator report read was explicitly work in progress. Its
  replacement, marked `Status: final synthesis`, was then read in full;
  the final changes were rechecked at 15:55–15:56 UTC.

## Numbered observations sent promptly to the coordinator

**O1 — precision wording.** The phase diagram's phrase “the dense theorem's
error floor” risks sounding like a lower bound on the actual sampler error.
The proof supplies an upper-bound guarantee. Replace it with “the stated
dense error guarantee does not improve merely by increasing computation at
fixed `N,m`.” No corresponding computational or statistical lower bound
has been proved. This is a wording correction, not an objection to R2's
theorem.

**O2 — final-status reconciliation.** The phase diagram still said the
fresh audits were pending and the hybrid certificate was being finalized.
Those audits and the hybrid proof are complete. Final coordinator files
must record the completed state and exactly one classification.

**O3 — integer hybrid eligibility (implementation clarification).** A
manifestly polynomial-time sufficient dense component predicate is

```
b=ceil(log2(1/epsilon)),
q_v=floor(ell/[2v(v-1)]),
q_v >= max(4ceil(log2 v), 144[b+ceil(log2(24Nv^2))]),
2C(v,ell)>=Z(v,ell),
```

with `v>=5` and feasibility. It implies the requested unconditional error
`epsilon/(8N)`: since `exp(-x)<=2^(-x)` for `x>=0`, the R2 bound
`3v^2 exp(-q_v/144)` is at most `epsilon/(8N)`. Thus an exact certificate
implementation can use only integer comparisons and dyadic bit lengths;
it need not resolve an exact transcendental logarithm ceiling. The
existing mathematical eligibility statement is sufficient for the theorem;
this explicit conservative predicate improves implementation clarity.

Suggested additional clarity: display the support-marked DP state cap
`v^(2v)<=(Nm+2)^c` with fixed `c` directly among connected primitives. An
unrestricted R1 bridge sampler is not by itself a connected sampler;
rejection requires the certified acceptance probability. R3 and the claim
ledger already preserve this distinction correctly.

## Consistency findings

- The exact `exp(O(sqrt(min(m,N)))) poly(N,m)` bound matches R1, including
  expected exact time, arbitrary endpoints, and its separate bounded-time
  valid-endpoint variant. Fixed regime constants must stay fixed as `N`
  grows. Precision-aware use of a large `b` is identified separately.
- The dense parameter is consistently `floor(m/[2N(N-1)])`, not the
  initially proposed density without its factor two. The exponent `1/144`,
  `3N^2` prefactor, low-rank fallback, and
  `2N(N-1)ceil(144 ln(3N^2/epsilon))` sufficient length match R2.
- Arithmetic-operation bounds are not presented as unit-cost bit bounds:
  the phase diagram explicitly retains polynomial-bit operands and
  expected random-bit runtime.
- The sparse global sampler is exactly uniform on a declared subset and
  approximate globally; its TV error is exactly `1-Z0/Z`, with the audited
  sufficient bound `m^4/[48(N-m+1)^2]` for even `m<=N`.
- All connected scalar counts being polynomial-time computable is kept
  distinct from positive-surplus connected word generation. DYZ scalar
  recurrence terms are not asserted to decode to actual uniform words.
- The hybrid retains the exact labeled component/interleaving weights and
  charges both omitted macro mass and internal component errors. Its
  rejection branch is used only with a connected-mass certificate.
- The uncovered set excludes all stated sufficient regimes and certified
  instances; the displayed square-root-to-quadratic band is explicitly
  conservative. It is not called an impossibility or hardness band.
- The first concrete open connected family `g=1,ell=2v` is correctly
  distinguished from the fixed-genus long-cycle endpoint result.
- Both negative results are scoped to named methods: explicit type-table
  enumeration grows too large, and minimal-only approximation fails above
  the proved power threshold. Neither establishes computational hardness.
- `quantified-phase-diagram` is the supported classification: at least the
  exact short regime and dense approximate regime are proved, with the
  extra sparse theorem and an explicit uncovered set. The supplied results
  do not justify `all-length-polytime`.

## Final disposition and reviewed snapshot

**O1 resolved.** The standalone phase diagram now says that more
computation is not proved to improve the stated dense error guarantee and
explicitly disclaims a matching lower bound on actual TV error. The
coordinator report uses the same upper-bound interpretation.

**O2 resolved.** The phase diagram and coordinator report now say final
synthesis, reflect both accepted reciprocal audits, and use exactly the
classification `quantified-phase-diagram`. The ledger consistently marks
the hybrid as a proved certificate/reduction and all-length sampling as
unresolved. Its `audit/synthesis` header does not assert a pending theorem.

**O3 resolved.** Both the phase diagram and coordinator report include
the conservative integer dense-component predicate and the exact
`2C>=Z` acceptance test. The phase diagram additionally displays the
support-marked DP cap explicitly, while the report explains the cap and
the rejection requirement. There is no unrestricted-to-connected target
substitution.

The final coordinator report contains the strongest audited theorem,
complete diagram, uncovered-band definition, first standalone connected
sampling lemma, precise external dependency/convention translations,
negative findings, and a single next human-review target. Exact endpoints
and expected polynomial bit time remain explicit. The classification is
supported by the accepted short/sparse/dense results; it is not inferred
from an absence of counterexamples.

Reviewed coordinator snapshot SHA-256 values at 15:56 UTC:

| artifact | SHA-256 |
|---|---|
| phase_diagram.md | `90f391c265d1c8114ece5cdeffcc7a62d47114791314b09d65f9fee4415a6ebf` |
| claim_ledger.md | `d64d75b7b3ef5f33c073392620dc20f0be46251c0b462c5bcd0d3cc86982e7cb` |
| coordinator_report.md | `65b14ff96d38bda2b8fc0d5e7d3ac96ea8dd5e49f6b07592868c7e38f685c7c8` |

These identify the reviewed content, not an assertion that the coordinator
cannot append final provenance afterward. Only this `synthesis_audit.md`
was added or edited during the reused audit task; the frozen R3 report,
code, results, hashes, and other workers' files were left unchanged.

Final verdict: **ACCEPT THE SYNTHESIS. ZERO UNRESOLVED MATERIAL OBJECTIONS.**
