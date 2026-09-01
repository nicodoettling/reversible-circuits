# M157 final report: exact two-beta signed-current representation

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: PROMOTE FOR FRESH REFEREE AUDIT.
PROVED: exact shared-X two-posterior transfer and finite signed/PSD kernel
        equality for H/q.
REFUTED: pointwise positivity of the exact equality kernel and the natural
         actual-kernel diagonal-trace repair as a uniform right-heavy
         certificate.
UNRESOLVED: a specialized off-diagonal cancellation inequality.
```

This narrows the post-M152 positive route but does not prove or refute the
true all-suffix contraction.

## Field 2 — scope, target, and convention

The project target remains uniform fixed-length identity transposition words.
Permutations compose as `(pq)(x)=p(q(x))`, factors left-to-right.  This
mission concerns only the normalized full unweighted reset excursion in the
auxiliary nonlazy minimal-long-cycle parking projection.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| shared-X two-beta signed-current kernel | auxiliary right-heavy all-suffix excursion budget | N/A: no sampler | N/A: auxiliary recurrence | exact transfer/reset/recursion and rational obstructions | equality kept; naive positive repairs refuted |

No auxiliary gap, `ROOT-MEAN LIFT`, original lazy `{3,4,5}` heat-bath gap,
polynomial mixing result, Terminal A, or Terminal B follows.

## Field 3 — exact shared-X transfer

For `mu=Beta(D,kappa-D)`, put

```text
L_x(u)=binom(d,x)u^x(1-u)^(d-x),
p_x=integral L_x dmu,
mu_x=Beta(D+x,kappa-D+d-x).
```

Bayes' rule gives the exact two-copy identity

```text
p_x mu_x(du)mu_x(dv)
 =[L_x(u)L_x(v)/p_x]mu(du)mu(dv).
```

Thus the retained transfer is the sum over `x=0,...,d-1`; the killed
`x=d` term is exactly `L_d(u)L_d(v)/p_d`.  Their respective double-beta
masses are `1-p_d` and `p_d`.  The kernel is necessarily state-dependent:
already for `d=1`, its retained coefficient is `2` at `(2,1)` and `3/2` at
`(3,1)`.

## Field 4 — exact reset and finite recursion

For the actual basin currents,

```text
R(u,v)=sum_E J_E(u)J_E(v)/(q c_E),
A_0/q=integral integral R dmu dmu.
```

Recursively multiplying each child kernel by its shared-X RN factor gives a
finite bivariate kernel `K_x`, because suffix excess strictly decreases.
Induction proves exactly

```text
H(x)/q_x=integral integral K_x(u,v)mu_x(du)mu_x(dv).
```

Every kernel is PSD as a sum of rank-one history-current features, but may
be negative pointwise.  At the M152 witness `(9,2,1,3)`, the kernel has 49
monomials, bidegree `(6,6)`, coefficient digest
`771567a049b76b2a546874b32de3170b8d1be32b3c7293c1a36cd9d84dec28f4`,
and its beta-square integral equals the independently evaluated exact
`H/q`.

## Field 5 — first pointwise sign obstruction

At `(s,kappa,D,B)=(3,2,1,1)` the exact reset kernel satisfies

```text
R(0,1)=-165/512.
```

Every shared-X likelihood product vanishes at `(u,v)=(0,1)`, so all
descendant terms vanish there and the full exact kernel has the same value.
Hence the exact two-copy equality cannot be turned into a pointwise
nonnegative supersolution without a new inequality.

## Field 6 — named positive repairs and exact failures

Local polarization of each reset feature before child-posterior propagation
reproduces M152's Jensen Bellman majorant exactly, including its positive
budget violation at `(9,2,1,3)`.

A distinct valid repair assembles the full exact history kernel first, then
uses PSD to bound its product-beta integral by its diagonal trace.  It first
fails in the capped fresh grid at

```text
(s,kappa,D,B)=(8,2,1,2), L=6,
trace approximately .8136933467,
budget approximately .8032201338,
positive margin approximately .0104732130.
```

The margin is the exact positive fraction

```text
132628808872888410508233058471582685297059
/12663621893778357952841743000389707366400000.
```

The true `H/q` is approximately `.4386703515`, so this is only a proof-device
obstruction.  No positive-part or absolute-value theorem is asserted.

## Field 7 — dependencies and frame scope

Accepted inputs are M147/M151's exact all-suffix recurrence and attachment
coordinates, and M152/M156's latent-beta context functions.  M123/M128 is
negative provenance only: it refutes a generic ambient canonical-basin frame.
The new exact recursion never assumes that frame.  Its diagonal-trace
inequality uses the actual constructed history features and fails by its own
exact witness.

The resulting equality is otherwise a repackaging of the nilpotent
recurrence.  State-dependent denominators and signed off-diagonal products
are precisely the information which a future nontrivial inequality must use.

## Field 8 — reproducibility and exact checks

Run from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-36/mission-M157-two-beta-signed-majorant/two_beta_exact.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-36/mission-M157-two-beta-signed-majorant/two_beta_exact.json \
  --max-B 3 --max-excess 6 --max-kappa 16
```

Python 3.12.3, standard library only, exact `Fraction` arithmetic,
deterministic `seed=null`.  The run reports zero failures across 51,840
shared-X monomial identities, 720 transfer-mass rows, 2,520 reset equalities,
and seven exact full-kernel equalities.  It also records all 21 capped fresh
right-heavy values.  These finite passes do not prove any new uniform target
range.

## Field 9 — next lemma and hygiene

The first remaining positive lemma is an off-diagonal cancellation bound for
the actual recursively generated kernels which keeps the state-dependent
shared-X transfer and exact killed atom, while avoiding polarization,
diagonal trace, positive part, absolute value, and the rejected generic basin
frame.

Owned artifacts are `plan.md`, `checkpoint.md`, `two_beta_theorem.md`,
`two_beta_exact.py`, `two_beta_exact.json`, this report,
`freeze_manifest.md`, and `SHA256SUMS`.  No predecessor, coordinator,
manuscript, project-skill, package, configuration, commit, or remote state was
changed.
