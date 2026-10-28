# Resource conditioning clarification, 2026-10-28

Coordinator review of draftv1 requested splitting macro-generation cost from decoder cost, or proving rejection-attempt independence after conditioning on a completed macro. The stronger conditional bound in draftv1 was an explicit pending interface, not a proved assertion; it is unnecessary.

Adopted resolution in draftv2: T=T_pre+T_dec, prove E T_pre<=A P^d without conditioning on the final macro, and prove E[T_dec|M]<=A P^d W9(M) for every positive-probability completed macro. Sum with the law of total expectation. Exact fair-bit calls in the macro phase have uniform conditional expected cost on each actual past history and there are polynomially many calls. All decoder randomness uses the untouched fair-bit tail after that stage.

This avoids inferring costs under posterior restriction from marginal bounds. The original stronger RC formulation remains on disk as a deliberately preserved draft; no theorem scope or expectation estimate changes. A separate implementation clarification excludes inherited exact_index exhaustive-test hooks from the production getrandbits interface and its bit-cost claim.
