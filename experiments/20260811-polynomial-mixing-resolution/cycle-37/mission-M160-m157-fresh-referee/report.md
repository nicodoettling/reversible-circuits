# M160 final report: fresh referee audit of frozen M157

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and objections

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
```

M157 proves the exact shared-observation two-posterior transfer and a finite
signed but positive-semidefinite history-kernel equality for `H/q`.  It also
correctly refutes pointwise positivity and the actual-kernel diagonal-trace
repair as uniform right-heavy certificates.  No contraction or gap follows.

## Field 2 — immutable provenance

All supplied frozen hashes match exactly:

```text
c9f3317574fafa9daf1d1c08be625132a879716cb876914065d783b28cfe22c2  report.md
e3dcd4d5c3c01d4c146fab67def1c025342f89185a3ba5dc957bbfd10df1eae3  two_beta_theorem.md
a86672353beefa2b048dc45f57fd70cd3756dacaae0fd1b7b587f0d07a507741  two_beta_exact.py
ad7714307a2c66afe6a3f8a375001a794fd8b1d935a4b0ee81cb612eea1d1832  two_beta_exact.json
03b50a837d6d8b30de4312aec2bf2f356e32a8ccffed3617d37079df1f0b84cd  freeze_manifest.md
2b26b2041ce84d4ccc737316873c3022c2e7a5e852cbff0bb71bb2eeafb580a3  plan.md
f10489f356cf5b5ce1d3d793d44bc11913f315f478dba20a0db80edac219c694  checkpoint.md
```

M157's complete `SHA256SUMS` also verifies.

## Field 3 — posterior transfer and equality

For one shared observation `X=x`, Bayes gives

```text
p_x mu_x tensor mu_x
 =(L_x tensor L_x)/p_x times mu tensor mu.
```

Its retained and killed masses are exactly `1-p_d` and `p_d`.  The RN kernel
is state-dependent through `p_x`; its degree-one retained coefficient is `2`
at `(kappa,D)=(2,1)` and `3/2` at `(3,1)`.

Direct expansion of the reset currents, followed by induction over the
strictly descending suffix DAG, proves

```text
H(x)/q_x=integral integral K_x dmu_x dmu_x.
```

The clean-room exact rebuild matches the reset and full values at three
selected states and reproduces the 49-term M152-witness kernel digest.

## Field 4 — PSD and exact sign obstruction

The reset is a positive sum of current outer products.  Every descendant RN
multiplier sends a feature `f` to `L_x f` with positive weight, so the finite
kernel is PSD as an actual history-feature kernel.  PSD does not imply
pointwise nonnegativity.

Ranks below three have zero active reset kernel.  At
`(s,kappa,D,B)=(3,2,1,1)`, exact expansion gives

```text
K(0,1)=R(0,1)=-165/512.
```

Every retained likelihood product vanishes at `(0,1)`, so descendants cannot
alter this value.  M157's pointwise-sign obstruction is exact and minimal in
rank.

## Field 5 — positive repairs

The diagonal-trace inequality is valid for the actual generated features,
but its first failure in the declared 21-row fresh grid is
`(8,2,1,2)`.  The exact positive budget margin is

```text
132628808872888410508233058471582685297059
/12663621893778357952841743000389707366400000.
```

The true `H/q` is approximately `0.4386703515`, so this is only a proof-device
failure.  Local feature polarization independently reproduces M152's exact
Jensen value and positive margin at `(9,2,1,3)`.  M123/M128's generic ambient
frame obstruction is not used: M157's trace concerns its actual recursively
constructed history features.

## Field 6 — exact checks and scope

Run from the M160 directory:

```text
python3 -B independent_referee.py --output independent_results.json
```

Python 3.12.3, standard library only, exact `Fraction` arithmetic,
deterministic `seed=null`, no predecessor imports, and no broad scan.  The
checker reports zero failures over 504 posterior-monomial identities, 16
retained/killed mass rows, three full-kernel equalities, the exact smallest
sign witness, all 21 capped trace rows, and the M152 polarization witness.

Accepted scope is only the auxiliary normalized full unweighted reset
excursion.  The equality is a repackaging of the nilpotent recurrence, not a
new inequality.  The off-diagonal cancellation lemma, all-suffix
contraction, auxiliary gap, `ROOT-MEAN LIFT`, original-chain gap, polynomial
mixing, Terminal A, and Terminal B remain unresolved.

## Field 7 — hygiene

Only the owned M160 directory was edited.  No predecessor, coordinator,
manuscript, project skill, package, configuration, commit, or remote state
was changed.
