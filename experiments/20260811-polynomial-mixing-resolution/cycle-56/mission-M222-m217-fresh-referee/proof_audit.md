# M222 clean-room proof audit of immutable M217

Date: 2026-08-13 UTC.

Verdict: **ACCEPT** M217's strict exact signed-DE reduction. The reduction,
normalizer estimate, macroscopic-tail lemma, and implication from WBE are
correct. WBE and signed averaged DE remain unresolved. This audit makes no
claim about DV, J2, PCR, any downstream gap statement, or either Terminal.

## 1. Immutable gates

All eight files named by frozen M217 passed `sha256sum -c SHA256SUMS` before
their contents were used. The checksum-file digest is exactly

    7772f6ec3fbdeaf82353f46a660f0bb641ef475696ac64dcca456643a5bf5557.

For source comparison, all checksum entries in M192/M195, M199/M207, and
M211/M215 also passed. Their checksum-file digests agree with the six values
recorded by M217. No predecessor was edited.

## 2. Independent split-weight derivation

Put

    tau(r)=r^(r-1)/r!,       b_r=e^(-r)tau(r).

The tree-function convolution gives

    sum_(s=1)^(k-1) b_s b_(k-s)=2(k-1)b_k/k.

Because `k` is odd, pairing `s` with `k-s` shows

    sum_(1<=s<k/2) b_s b_(k-s)=(k-1)b_k/k.

Thus

    q_s=[k/(k-1)] b_s b_(k-s)/b_k

is a probability law on the smaller first split. Conditional on this split,
the probability that the ordered second edge is disjoint from the first is

    a_F(s)=1-gamma_F(s).

Therefore their joint mass is the subprobability weight

    qhat_s=q_s a_F(s).

There is no division by `sum_s q_s a_F(s)`: such a division would change the
original disjoint submeasure and is absent from M217.

Let the unnormalised literal B/A profile numerators be

    B_s^Z=a_L(s) Phi_s^D(Z),
    A_s^Z=a_F(s) Psi_s^D(Z).

Then direct substitution, before any estimate, gives

    qhat_s[Phi_s^D(Z)-Psi_s^D(Z)]
      =q_s{[a_F(s)/a_L(s)]B_s^Z-A_s^Z}.              (2.1)

Thus the factor `a_F` cancels the A conditional normalizer exactly. It does
not cancel the B normalizer and it is not a renormalized split law.

## 3. Exact blocks, signs, and literal completeness

For `Y_l`, independent regrouping of the accepted literal formulas gives

    B_surv=h(s)F_l(D-s)+h(D-s)F_l(s),
    B_frag=W_s(F_l)+W_(D-s)(F_l),

    A_surv=h(s)J_l(k-s)+h(k-s)J_l(s)
           +u[J_l(s)+J_l(k-s)],
    A_frag=W_s(J_l)+W_(k-s)(J_l)+C_l.                (3.1)

For `X_l`, take the exact surviving one-run contributions inside M199's
literal `(B-X)` and `(A-full)` sums and define each fragmentation block as
the full literal numerator minus that surviving sub-sum. This is an exact
partition, not an approximation.

For either `Z=X_l,Y_l`, write these partitions as

    B_s^Z=B_surv,s^Z+B_frag,s^Z,
    A_s^Z=A_surv,s^Z+A_frag,s^Z

and define

    S_Z=sum_s q_s(B_surv,s^Z-A_surv,s^Z),
    K_Z=sum_s q_s(B_frag,s^Z-A_frag,s^Z),
    N_Z=sum_s q_s[a_F(s)/a_L(s)-1]B_s^Z.             (3.2)

Expanding (2.1) proves, with the displayed B-minus-A signs,

    DE_Z=S_Z+K_Z+N_Z.                                (3.3)

The literal supports confirm completeness. The B sum ranges over every
`(i,r,d,a)` with `r` in `{s,D-s}` and imposes no same/cross-kind deletion;
the A-full sum ranges over every disjoint ordered pair. The three-term
incidence law `F_l` retains both seam crossings. The `X_l` complement retains
the two-run face. Indicators are added with multiplicity, so equal-size and
equal-kind collisions are not deduplicated. Consequently (3.2) retains both
observables, every kind, both seams, and every collision stratum.

## 4. Exact normalizer ratio and uniform remainder

With `D=2k-1` and `R=2k-3`, direct subtraction gives

    a_F-a_L=gamma_L-gamma_F
      =2/R [1/(k-s)-1/(D-s)]
      =2(k-1)/[R(k-s)(D-s)].                         (4.1)

Therefore

    a_F/a_L-1=2(k-1)/[R(k-s)(D-s)a_L].              (4.2)

For odd `k=2j+1` and `s<k/2`, one has `s<=j` and `D-s>=3j+1`.
The function

    h(r)=(r-1)(r-2)/(rR)=(r-3+2/r)/R

is increasing for integer `r>=2`. At `r=3j+1`, the inequality
`h(r)>=1/2` is equivalent to

    (6j-1)(j-1)>=0.

Hence `a_L>=h(D-s)>=1/2`, with equality at `(k,s)=(3,1)`. Also
`R>=k`, `k-s>=(k+1)/2`, and `D-s>=(3k-1)/2`. Substitution in
(4.2), followed by
`3k(k-1)<=(k+1)(3k-1)`, gives the explicit uniform bound
`a_F/a_L-1<=16/(3k^2)`.

Both prefix observables lie in `[0,3]`. Since `a_L` is a probability and

    B_s^Z=a_L Phi_s^D(Z),

one has `0<=B_s^Z<=3`. Using `sum_s q_s=1` in (3.2) yields

    |N_Z|<=16/k^2,       Z=X_l,Y_l,                  (4.3)

after adjusting the universal constant at the finite endpoint. This is
uniform in the full stated `l` range.

## 5. Independent Stirling and tail proof

The elementary uniform Stirling inequalities

    sqrt(2 pi) r^(r+1/2)e^(-r) <= r!
      <= e r^(r+1/2)e^(-r),       r>=1,

imply absolute constants `c,C>0` with

    c r^(-3/2)<=b_r<=C r^(-3/2).                    (5.1)

For `s<k/2`, (5.1) gives

    b_(k-s)/b_k<=C[k/(k-s)]^(3/2)<=C.

Moreover `k/(k-1)<=3/2` and `0<=a_F<=1`. Hence

    qhat_s
      =[k/(k-1)]b_s[b_(k-s)/b_k]a_F(s)
      <=C b_s<=C s^(-3/2).                          (5.2)

The integral test now proves, uniformly for integer `1<=m<k/2`,

    sum_(m<=s<k/2) qhat_s
      <=C sum_(s>=m)s^(-3/2)
      <=C/sqrt(m).                                  (5.3)

Taking `m=ceil(epsilon k)` for fixed `0<epsilon<1/2` gives
`O_epsilon(k^-1/2)`; for `epsilon>=1/2` the range is empty.

## 6. Why the tail closes only the macroscopic-l scale

Since both normalized profiles are in `[0,3]`, the absolute contribution
from all `s>=epsilon k` is at most a constant times (5.3), namely
`O(k^-1/2)`. If `l` is comparable to `k`, then

    sqrt(l)/k=Theta(k^-1/2),

so this tail is target-sized. If `l` is fixed, the requested scale is
`Theta(k^-1)`, while (5.3) supplies only `O(k^-1/2)`. The tail estimate is
then too weak by a factor of order `sqrt(k)`. This is an insufficiency, not
a counterexample: signed cancellation across `s` may still improve it.

## 7. Exact WBE implication

Assume only the unresolved signed estimate

    |S_Z+K_Z|<=C sqrt(l)/k.                          (WBE)

Equations (3.3) and (4.3) give

    |DE_Z|<=C sqrt(l)/k+C'/k^2.

Because `k>=3` and `l>=2`, the second term is absorbed into the first. Thus
WBE implies DE exactly as claimed. It does not prove WBE. M192's nonzero
Abel endpoint lies outside DE and is neither dropped nor altered here.

## 8. Independent finite falsification

`checker.py` contains no imports and loads no M217 code or data. Its local
rational arithmetic verifies at `k=3,5`:

- `sum_s q_s=1` and the exact subprobability totals;
- both denominator identities and (4.2) at every admissible `s`;
- the A-normalizer cancellation term by term;
- the exact Y surviving/kernel/normalizer decomposition for every admissible
  `l`.

All checks pass. In particular it independently obtains `sum qhat=2/3` and
`DE_(Y_2)=-8/45` at `k=3`, and `sum qhat=26/35` and
`DE_(Y_4)=-1471428533/11063808000` at `k=5`, matching the frozen calibration.
These two ranks are exact falsification only and prove no universal estimate.

## 9. Numbered objections

1. **Material objections:** none.
2. **Nonmaterial M217 qualifications:** none.
3. **Repository source-lock note:** `AGENTS.md` names
   `references/experiments.md`, which is absent. The corresponding existing
   skill-owned file
   `.codex/skills/reversible-circuit-sampler/references/experiments.md` was
   read. This path discrepancy does not affect M217's mathematics.
