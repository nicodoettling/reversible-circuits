# M222 report: fresh immutable referee of M217

Date: 2026-08-13 UTC.

## 1. Verdict

**ACCEPT.** M217 proves the strict exact signed-DE three-block reduction,
the uniform `O(k^-2)` normalizer remainder, and the macroscopic
`qhat`-mass tail. Its claim that WBE would imply DE is exact. WBE and DE
remain unresolved.

## 2. Immutable gate

Every file in M217's frozen inventory passed. The exact digest of its
`SHA256SUMS` file is

    7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557.

The six cited predecessor inventories also passed and were not edited.

## 3. Target and convention

Target: the original unnormalised disjoint ordered-double B/A response under
uniform minimal transposition factorizations in the fixed-cell calculation,
`n=3k`, odd `k>=3`, for `Z=X_l,Y_l`. Composition is
`(pq)(x)=p(q(x))`, with displayed factors left-to-right. This is not the
global bridge heat-bath kernel.

## 4. Exact weight and cancellation

The exact joint first-split/disjoint mass is

    qhat_s=q_s a_F(s),

with no renormalization. Multiplication by `qhat_s` cancels the A conditional
normalizer in `Psi=A/a_F` and leaves the B factor `a_F/a_L`.

## 5. Exact decomposition and retained terms

Independent expansion verifies

    DE_Z=S_Z+K_Z+N_Z,
    N_Z=sum_s q_s[a_F(s)/a_L(s)-1]B_s^Z.

Every sign is B minus A. The exact numerator partitions retain `X_l` and
`Y_l`, all same/cross kinds, both seam incidences, the X complementary
two-run face, and all collision multiplicities.

## 6. Exact bounds

Direct subtraction gives

    a_F/a_L-1=2(k-1)/[R(k-s)(D-s)a_L].

The bound `a_L>=1/2` yields `N_Z=O(k^-2)` uniformly. Independent uniform
Stirling inequalities give

    qhat_s<=C s^-3/2,
    sum_(s>=m) qhat_s<=C/sqrt(m).

The macroscopic tail is target-sized when `l` is comparable to `k`. It is
only `O(k^-1/2)` against an `O(k^-1)` target when `l` is fixed, so it does
not by itself close DE in the full range.

## 7. Remaining lemma and implication

The first open statement remains

    |S_Z+K_Z|<=C sqrt(l)/k.                          (WBE)

Together with `N_Z=O(k^-2)` and `l>=2`, WBE implies DE. This audit neither
proves nor tests WBE.

## 8. Exact finite check

`checker.py` is deterministic, contains no imports, loads no M217 artifact,
and uses local exact rational arithmetic. At `k=3,5`, every denominator,
ratio, cancellation, and Y three-block identity passes for all admissible
`l`. The selected exact values match M217. This is finite falsification only.

## 9. Numbered objections and action

1. Material objections: none.
2. Nonmaterial M217 qualifications: none.
3. Repository note: `AGENTS.md` points to the absent path
   `references/experiments.md`; the existing skill-owned experiment reference
   was used instead. This does not affect the verdict.

Action: freeze M222 as an accepting audit. Keep WBE, DE, DV, J2, PCR, all
downstream gap claims, and both Terminals open. Do not infer anything from the
two finite ranks.

