# M335 exact obstruction to the enlarged-exception source switch

Date: 2026-08-14 UTC

Status: **the frozen `S_pf^*` compatible-part coboundary is refuted at
reverse-residual landing; the exact flux split and exceptional scalar
reduction survive.**

## 1. General same-cell obstruction

Fix a supported cell `(s,t)`. By definition,

```text
a_st(P)=[g_s(P)-f_t(P)]_+,
b_st(P)=[f_t(P)-g_s(P)]_+.
```

Therefore the supports of `a_st` and `b_st` are disjoint. In particular,

```text
a_st(P)>0 and b_st(Q)>0
  imply b_st(P)=0 and a_st(Q)=0.                    (1.1)
```

Every residual token in this cell is directed `P->Q`. If a literal endpoint
swap preserves the same cell, its proposed reverse token would require
`a_st(Q)>0` and `b_st(P)>0`, contradicting `(1.1)`. Hence:

> **Same-cell landing lemma.** A positive residual token cannot be sent to a
> reverse residual token in the same cell merely by swapping its endpoint
> profiles.

This is an exact identity of the canonical residual-product coupling. It does
not use an estimate or final edge surplus.

## 2. Exact off-exception realization

The sole predeclared guard uses only `k=9,n=27,H_2`. It finds the first
lexicographic compatible token in cell `(1,1)`.

Its A endpoint is

```text
xi_A: channel 2, split 1,
      e=(3,4), f=(4,5), slot 1, owner size 1,
      profile P=0,
      marked-owner support empty,
      support heads {2,3,4}.
```

Its B endpoint is

```text
eta_B: channel 2, split 1,
       e=(3,4), f=(4,6), slot 2, owner size 2,
       profile Q=(-1,0,...,0,1),
       marked-owner support {4},
       support heads {2,3,5}.
```

Here `Sigma={0,1,8,18,26}`. Both displayed endpoint owner/head sets are
disjoint from `Sigma`. Their opposite-source raw atoms exist with positive
minimal-completion masses:

```text
sigma(eta_B)_A raw unconditional mass =224/1358127,
sigma(xi_A)_B  raw unconditional mass
 =19461950683593750/65835730184725763239.
```

The switched marked owner/head sets are unchanged, so they also avoid
`Sigma`. Thus all four `Touch` predicates are false and both `BadPref`
predicates are false: the original token lies outside `Exc_pf^*` and so does
the raw switched pair.

## 3. Exact positive token and failed landing

The original cell data are

```text
pi_11=72057594037927936/168377826559400929,
rho_11=2354028198661286694240715
       /102166958637249138505285632,
a_11(P)=583013693948397585119897
        /34055652879083046168428544,
b_11(Q)=3296284725931531/9493588014497005568.
```

The complete conditional raw-fiber probabilities are

```text
u_A(xi_A|1,P)=20841167403/73338099464768,
u_B(eta_B|1,Q)=198428693313536/6311626321257167.
```

With the corrected `c_H=62/23`, the original token weight is exactly

```text
425758390993809446972368496973627659814865534216945520778179328
/160127614349801894448349798657905382956928144305646616084388152620616845
>0.                                                     (3.1)
```

Both source-switched endpoints still have split 1, so the derived reverse
cell is `(1,1)`, which is supported with the same `pi_11` and `rho_11`.
But `(1.1)` gives, and the exact guard reproduces,

```text
a_11(Q)=0,             b_11(P)=0.                  (3.2)
```

Consequently the proposed reverse residual token has zero mass and is not in
the token universe. The first nontrivial clause `(4.1)` of
`candidate_formula.md` fails; the exact weight ratio `(4.2)` is never
defined. Raw-label involutivity cannot cancel `J_compatible` because it is
not an involution of the residual token measure.

## 4. Strongest surviving identities

The enlarged predicate remains literal and source-local, and tokenwise
restriction still gives

```text
J=J_compatible+J_exceptional.                       (4.1)
```

On raw labels outside `Exc_pf^*`, the product-fixed source switch remains an
involution, preserves the unordered response-profile pair, reverses its
formal order, and preserves the exception predicate. What fails is landing
in the canonically oriented residual-product token law.

For the exceptional part, exact marginalization and `a<=g`, `b<=f` retain
the scalar bound

```text
mass_X(Exc_pf^*)
 <=c_X [ k/(k-1) sum_(s<=h)b_s R_k(s)E_A^X(s)
        +(2k-1)/(2k-2) sum_(t<=k-1)b_t R_(2k-1)(t)E_B^X(t)].  (4.2)
```

The desired H/A/C bounds on `(4.2)` remain an explicit unproved scalar lemma.
Even if proved, they would control only `J_exceptional`; this mission's
source switch does not cancel `J_compatible`.

Any future source-local coboundary must, at minimum, move a same-cell token to
a different supported cell where the residual signs actually reverse, or
provide an exact signed-measure cancellation that is not a tokenwise endpoint
swap. This is a necessary condition, not a proposed replacement surgery.

No MPCF or downstream conclusion follows.

