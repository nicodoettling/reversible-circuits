# local-endpoint-blindness

- Created UTC: 2026-10-19T14:01:50.457099+00:00
- Objective: Determine what endpoint-blind short-window initialization implies for fixed-endpoint local circuit mixing
- Target distribution: Uniform fixed-length transposition words with prescribed product g in S_N
- Parameters: arbitrary N,m,g in proofs; deterministic exact checks on S3 and S4,
  including identity lengths 4 and 6, odd endpoints, and dense count recurrences.
- Composition: (pq)(x)=p(q(x)); all linear windows, no wraparound.
- Kernels: K_A=I/2+H/4+R/4 (uniform adjacent signed Hurwitz and square
  refresh); Q_r=I/2 plus half a uniform exact length-r heat bath;
  Q_345 chooses equally among available lengths 3,4,5. Results for finite
  propagation cover any fixed mixture of these kernels.
- Tested claims: endpoint-blind short marginals; pinned-prefix starts with
  identical short marginals; persistence and coupon bounds for local moves;
  exact hidden eigenmode for S3 heat baths; a conditional comparison theorem
  locating the extra premise needed for global mixing.
- Commands: `python3 -B experiments/20261019-140150-local-endpoint-blindness/check.py`.
- Raw data: results.jsonl; exact integer/Fraction calculations, no PRNG and
  therefore no random seed. No nonstandard dependencies or installations.
- Expected failure modes: marginal independence confused with conditional
  independence; parity ignored; a slow polynomial mode misreported as
  superpolynomial mixing; a macro heat bath substituted for the user's local
  kernel; long-overlap results incorrectly presented as new despite HB-BASE.
- Interpretation: author proofs plus finite falsification checks, not an
  independent review or an asymptotic conclusion from finite spectra.
- Next changes: write proof, claim ledger and report; add a provisional map
  record without changing prior evidence or promoting the unresolved gap.
