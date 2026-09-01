# Halfway checkpoint: M10 two-block recursion referee

## Provisional verdict

`ACCEPT`, subject to final source/dependency wording.  No mathematical
counterexample has been found.

## Independent derivations completed

- Diaconis--Shahshahani Lemma 14 uses the with-replacement lazy eigenvalue
  `z=1/N+(N-1)r/N` at exponent `2s`.  Pairing conjugate partitions in the
  even nonlazy return gives exactly the M10 majorant, and the primary
  Section 3 estimates make it arbitrarily small at
  `s=(N/2)log N+cN`.
- The endpoint-tilt density is
  `(1+delta)(1+d)/[(1+d_x)(1+e_y)]`.  Its sharp pointwise deviation is
  `64/225` at `epsilon=1/16`; the used `22/75` is conservative.
- The tails and boundary variables have equal maximal correlation even with
  microfactor labels: the boundaries are functions of the tails and the
  full bridge factorization gives the reverse data-processing inequality.
- Two conditional-expectation projections have average gap `(1-rho)/2` on
  each principal-angle plane; `rho<=22/75` gives more than `1/3`.
- Each local Hamiltonian site occurs once or twice in the two length-`L`
  intervals, so the `1/2` domination and one factor-`3` loss are exact.
- The overlap parity choice, affine halving, base stopping range, and
  `3^{-ceil(log_2 x)}>=(1/3)x^{-log_2 3}` are correct.
- `gap(B)=Lambda/(n-1)` is an identity.  Direct coefficient comparison with
  the lazy full chain gives `(m-2)/[12(m-3)]>=1/12` for `m>=6`; `m=4` is the
  separate whole-word case.

## Falsification harness

With seed `20260811`, `counterexample_audit.py` tested 20,000 sparse/dense
tilted joint laws and 399,920 affine-recursion instances.  It found no
violation.  The largest density deviation was `0.27304<22/75`, the largest
maximal correlation was `0.06247`, and the two-projection formula error was
below `7.3e-16`.  This finite survival is not proof; the analytic derivations
above carry the theorem.

## Remaining work

- Freeze the full nine-field report with the base quantitative gap clearly
  labeled open.
- Search primary literature for a theorem directly covering the remaining
  fixed-endpoint adjacent bridge actions, or state the exact mismatch.
