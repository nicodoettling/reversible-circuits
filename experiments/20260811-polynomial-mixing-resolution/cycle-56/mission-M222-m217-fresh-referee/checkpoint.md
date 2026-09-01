# M222 checkpoint

## Start

- M222 initialized `plan.md` and this checkpoint before substantive work.
- M217 is immutable; M222 owns only this directory.
- Scope is the exact signed averaged DE reduction and its asymptotic
  bookkeeping, not WBE itself.

## Immutable gate

- Every M217 `SHA256SUMS` entry passed.
- The checksum-file digest is exactly
  `7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557`.
- All cited M192/M195, M199/M207, and M211/M215 inventories also passed and
  agree with the digests recorded by M217.

## Halfway result

- Independently derived `qhat_s=q_s a_F(s)` as the unnormalised joint
  split/disjoint mass.
- Verified that this factor cancels the A conditional normalizer and leaves
  the B ratio `a_F/a_L`.
- Verified the exact B-minus-A definitions and signs in
  `DE_Z=S_Z+K_Z+N_Z` for both literal observables. The complementary X face,
  all kinds, both seams, and collisions remain in the partition.
- Derived
  `a_F/a_L-1=2(k-1)/[R(k-s)(D-s)a_L]` and an explicit uniform
  `N_Z=O(k^-2)` estimate.

## Final result

- Independent uniform Stirling bounds prove
  `qhat_s<=C s^-3/2` and the tail `C/sqrt(m)`.
- The tail is target-sized for `l` comparable to `k`, but not for fixed
  `l`; no cancellation is inferred.
- WBE plus the normalizer estimate implies DE by the triangle inequality.
- The clean-room no-import exact checker passes at `k=3,5` and reproduces
  the frozen selected rational values.
- Final verdict: **ACCEPT**, no material or nonmaterial M217 objections.
  WBE and DE remain open; no excluded downstream claim was considered.
