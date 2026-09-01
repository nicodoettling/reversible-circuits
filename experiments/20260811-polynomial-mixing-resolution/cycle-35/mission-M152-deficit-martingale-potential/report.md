# M152 final report: beta-mixture potential obstruction

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict

```text
FINAL VERDICT: PROMOTE FOR FRESH REFEREE AUDIT.
PROVED: exact killed-atom Doob identity and global beta-Jensen majorant.
REFUTED: the full pointwise latent-beta Jensen supersolution family as a
         right-heavy all-suffix contraction certificate.
UNRESOLVED: a sharper deficit-aware amortized potential.
```

This is a proof-route obstruction, not an auxiliary-chain bottleneck and not
a counterexample to right-heavy contraction.

## Field 2 — scope, target, and convention

The project target remains uniform on fixed-length identity transposition
words.  Permutations compose as `(pq)(x)=p(q(x))`, factors left-to-right.
This mission concerns only the normalized full unweighted reset excursion in
the auxiliary nonlazy minimal-long-cycle parking projection.

| candidate | claimed target | identity ok | crosses Hurwitz components | exact diagnostics | verdict |
|---|---|---|---|---|---|
| latent-beta Jensen Bellman potential | right-heavy auxiliary all-suffix excursion budget | N/A: no sampler | N/A: auxiliary recurrence | exact Doob/Jensen identities and rational `L=6` witness | global majorant proved; contraction certificate refuted |

No auxiliary gap, `ROOT-MEAN LIFT`, original lazy `{3,4,5}` heat-bath gap,
polynomial mixing result, Terminal A, or Terminal B follows.

## Field 3 — exact killed attachment identity

For `X=d-j`, the attachment is beta-binomial and the child is
`(kappa+d,D+X)`.  If `Theta~Beta(D,kappa-D)` and
`V_psi(kappa,D)=E[psi(Theta)]`, posterior conjugacy gives

```text
sum_(X=0)^(d-1)Pr[X]V_psi(kappa+d,D+X)
 =E[(1-Theta^d)psi(Theta)].
```

The removed `j=0` term is exactly `E[Theta^d psi(Theta)]`.  It is neither
dropped nor hidden by conditioning.

## Field 4 — proved global majorant

Each accepted contextual mean is the beta expectation of the point function

```text
g_C(u)=0                  if last(C)<B,
       d u^(d-1)          if last(C)=B,
       q_child(1-u^d)     if last(C)>B.
```

For basin point currents `J_E`, Jensen gives the exact-reset upper bound

```text
A_0/q <= E[sum_E J_E(Theta)^2/(q c_E)].
```

Using this point reward and the exact factor `(1-u^d)` recursively defines a
finite nonnegative polynomial `phi_(B,L)`.  Induction on suffix excess proves

```text
H/q <= V_(B,L)(kappa,D):=E[phi_(B,L)(Theta)]
```

for every valid attachment state.  This is an exact all-suffix majorant at
arbitrary deficit, but not a contraction.

## Field 5 — exact obstruction

The equality recursion gives the pointwise-minimal integrand among every
nonnegative supersolution using this canonical-basin Jensen reward.  At the
fresh right-heavy state

```text
(s,kappa,D,B)=(9,2,1,3), L=6,
q=3176523/25000000,
```

its exact degree-twelve beta integral exceeds `1-q` by

```text
5714491495302498676679596453643417785239504603683
/223395363274892426079078092636160000000000000000000
 approximately 0.02558017056.
```

Every pointwise supersolution in the named family is at least this minimal
one, so the whole family is refuted as a uniform right-heavy certificate.

## Field 6 — accepted L=6 theorem remains intact

An independent exact resolvent at the same state gives

```text
H/q approximately 0.5663747547,
1-q approximately 0.8729390800,
true budget slack approximately 0.3065643253.
```

All three quantities are stored as exact rationals.  Hence the target
inequality passes strongly at the obstruction state.  The accepted M145/M149
right-heavy `L=6` theorem is untouched; only this looser proof device fails.

## Field 7 — dependencies and relation to prior obstructions

Accepted positive inputs are M147/M151's exact all-suffix recurrence and
attachment coordinates.  M140/M144 supplies the corrected one-power reset
context, but the new majorant instead bounds the exact reset directly by
Jensen and does not modify that theorem.  M145/M149 is used only to state the
already accepted `L=6` status.  M123/M128's canonical-basin frame obstruction
explains why a universal Bessel repair is unavailable; it is not needed to
prove the exact witness.

The result does not refute potentials that retain signed cross-beta
information, use a sharper current-square inequality, or leave the
pointwise-latent supersolution architecture.

## Field 8 — reproducibility

Run:

```text
python3 -B beta_potential.py \
  --output beta_potential.json --max-excess 6 --max-kappa 128
```

Environment: Python 3.12.3, standard library only, exact `Fraction`
arithmetic, deterministic `seed=null`.  The result reports zero failures over
2,142 killed-atom/Doob monomial checks, five Jensen audits, an independent
discrete-posterior evaluation of the witness, and a separate exact
reset/resolvent evaluation.

The capped passed boundary rows are empirical/exact finite diagnostics only
and prove no universal passed range.  The failed row is a theorem-level
refutation because one exact state suffices to disprove the universal
supersolution claim.

## Field 9 — next lemma and hygiene

The first remaining positive lemma is to find a deficit-aware potential that
preserves enough signed cross-beta current information to avoid the Jensen
loss while charging the exact killed atom.  It must not rely on the refuted
canonical-basin Bessel frame.

Only this owned M152 directory was edited.  No package, configuration,
predecessor, coordinator, manuscript, or project-skill file was changed.

