# M248 report: exact WBE and signed averaged DE assembly

Date: 2026-08-14 UTC.

## Verdict

**PROMOTE WBE AND SIGNED AVERAGED DE AS PROVED, SUBJECT TO A FRESH
IMMUTABLE AUDIT OF THIS ASSEMBLY.**

For every odd `k>=3` and integer
`2<=ell<=(3k-1)/2`, the exact literal prefix observables obey

```text
|S_(Y_ell)+K_(Y_ell)|<=7000sqrt(ell)/k,
|S_(X_ell)+K_(X_ell)|<=7160sqrt(ell)/k.
```

Thus WBE is closed for both observables. The accepted exact normalizer
identity further gives

```text
|N_Z|<=16/k^2,
|DE_(Y_ell)|<=7004sqrt(ell)/k,
|DE_(X_ell)|<=7164sqrt(ell)/k.
```

The common explicit DE constant is `7164`.

## Exact assembly

M226/M229 proves, before any absolute value is taken,

```text
S_Y+K_Y=sum_(y=2)^ell c^Y_(k,y),
(S_X+K_X)-(S_Y+K_Y)=sum_(y=2)^ell c^T_(k,y).
```

M239/M246 proves the first prefix is at most `7000sqrt(ell)/k`.
M235/M238 proves the second is at most `160sqrt(ell)/k`. One triangle
inequality gives the X constant `7160`; Y keeps `7000`.

The raw identities retain every same/cross kind, both seams, the X
complementary two-run face, and every equal-size collision with multiplicity.
No conditional profile normalizer or pointwise absolute difference is
introduced.

## Explicit normalizer bound

M217/M222 proves

```text
DE_Z=S_Z+K_Z+N_Z,
a_F/a_L-1=2(k-1)/[R(k-s)(D-s)a_L].
```

Using `R>=k`, `k-s>=(k+1)/2`, `D-s>=(3k-1)/2`, and
`a_L>=1/2` gives

```text
a_F/a_L-1<=16/(3k^2).
```

Because `B_s^Z<=3` and `sum_s q_s=1`, this yields `|N_Z|<=16/k^2`.
Finally `k^2 ell>=18>16` on the complete domain, so
`16/k^2<=4sqrt(ell)/k`, producing the displayed DE constants.

## Immutable dependency gate

Every file in the frozen M217/M222, M226/M229, M235/M238, and M239/M246
inventories passed before use. Exact checksum-file digests are recorded in
`checkpoint.md` and `manifest.md`. No predecessor was edited. M229's
nonmaterial correction restricting `G_k` to `1<=x<=(3k-3)/2` is already
enforced by M239/M246 and creates no domain mismatch here.

## Compact check

The command

```text
python3 experiments/20260811-polynomial-mixing-resolution/cycle-66/mission-M248-wbe-de-assembly/algebra_domain_check.py
```

uses no imports, randomness, predecessor code, or predecessor data. It checks
the constant additions and exact cross-multiplied domain inequalities at all
odd `3<=k<=1001`, all admissible splits, and all admissible cutoffs. All
checks pass; the smallest absorption margin is the boundary value
`3^2*2-16=2`. These finite rows are falsification evidence only.

## Dependency labels and exclusions

- Frozen proved/accepted inputs: exact `DE=S+K+N`; exact coefficient
  identities; TCM constant `160`; YCM constant `7000`.
- New proved conclusion: WBE constants `7000,7160`, normalizer bound
  `16/k^2`, and signed averaged DE constants `7004,7164`.
- Unproved assumptions: none.
- Still open: DV.
- Not inferred: conditional J2, PCR/WPCR/SCBR, any comparison theorem,
  spectral gap, polynomial mixing, or either Terminal.

## Action

Freeze this mission and request a fresh referee to verify the immutable
dependency gates, both coefficient identities, the single WBE triangle
inequality, the explicit normalizer arithmetic, and the scope exclusions.

