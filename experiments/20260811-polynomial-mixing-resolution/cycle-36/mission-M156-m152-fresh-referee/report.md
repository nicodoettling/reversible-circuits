# M156 fresh-referee report on frozen M152

Date: 2026-08-13 UTC. Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

## Field 1 — verdict and objections

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
```

M152 proves the exact killed-atom beta-posterior identity and a global
canonical-basin beta-Jensen majorant.  Its exact right-heavy witness refutes
the associated pointwise supersolution family as a uniform all-suffix
contraction certificate.

## Field 2 — immutable provenance

All requested frozen hashes match:

```text
f1dafebd7f6722a16abedbf5382ad433e729f5294295f06b23fb6d82eb97bd70  report.md
dfebb6c250f6c4fcf0eaf44da961d0887613ad28012689b52b6a40c441023b6d  beta_jensen_obstruction.md
5c9cd1a4693859147d0f356f30e997e2d3e8c1c04f6ead4c8d4ff4740edf4388  beta_potential.py
b4880001fb4b8b706c40ee58ca14dd90649efc204dbdf2a31c551c0c597eb6fa  beta_potential.json
0c444c254bd49c008cd4836f14d16ecc43aa8aace628e5177278e2457304db51  freeze_manifest.md
141a6d131e4d1c36e6d5d2716d249ee157544084269e28ac78c279ba02fc94c6  SHA256SUMS
```

The frozen checker reran byte-identically.  The actual manifest filename is
`freeze_manifest.md`.

## Field 3 — killed atom and context audit

With `X=d-j`, beta-binomial posterior conjugacy gives the retained identity

```text
sum_(x=0)^(d-1) P(X=x)V_psi(kappa+d,D+x)
 =E[(1-Theta^d)psi(Theta)].
```

The missing `X=d`, equivalently `j=0`, contribution is exactly
`E[Theta^d psi(Theta)]`; it is not conditioned away.  All three contextual
point functions have the claimed beta expectations.  The clean-room checker
passed 21 full/retained/killed monomial checks and 280 literal-source context
checks.

## Field 4 — Jensen and Bellman audit

For endpoint current `theta_E=E[J_E(Theta)]`, the exact normalization is

```text
A_0/q=sum_E theta_E^2/(q c_E).
```

Jensen therefore yields the stated reward
`r=sum_E J_E^2/(q c_E)` with no extra factor of `q`.  Induction over suffix
excess, together with the exact retained identity, proves

```text
H/q <= E[phi_(B,L)(Theta)].
```

The equality Bellman recursion is pointwise minimal among supersolutions
using this same reward because every child multiplier is nonnegative on
`[0,1]`.  This minimality does not extend beyond that named architecture.

## Field 5 — exact obstruction and independent check

At `(s,kappa,D,B)=(9,2,1,3)`, `L=6`,

```text
q=3176523/25000000,

V-(1-q)
 =5714491495302498676679596453643417785239504603683
  /223395363274892426079078092636160000000000000000000
 >0.
```

The independent checker enumerates literal compositions rather than grouped
root masses.  Its degree-12 polynomial integral equals a separately evaluated
discrete-posterior recursion and matches every frozen fraction exactly.

## Field 6 — true excursion and scope

The independently rebuilt exact recurrence gives

```text
H/q approximately 0.5663747547,
1-q approximately 0.8729390800,
(1-q)-H/q approximately 0.3065643253 >0.
```

Thus the witness is a rigorous obstruction to this Jensen proof family, not
to the contraction inequality.  The accepted M145/M149 right-heavy `L=6`
theorem remains intact.  M152 proves no all-suffix contraction, auxiliary
gap, `ROOT-MEAN LIFT`, original heat-bath gap, polynomial mixing theorem, or
project terminal.

## Field 7 — reproducibility and hygiene

Run from the repository root:

```text
python3 -B experiments/20260811-polynomial-mixing-resolution/cycle-36/mission-M156-m152-fresh-referee/fresh_referee.py \
  --output experiments/20260811-polynomial-mixing-resolution/cycle-36/mission-M156-m152-fresh-referee/fresh_referee.json
```

Python 3.12.3, standard library only, exact `Fraction` arithmetic,
deterministic `seed=null`, no predecessor imports, and no broad scan.  A
second run to `/tmp` reproduced the result digest byte-for-byte.  Only the
owned M156 directory was edited; no predecessor, coordinator, manuscript,
skill, package, configuration, commit, or remote state was changed.

