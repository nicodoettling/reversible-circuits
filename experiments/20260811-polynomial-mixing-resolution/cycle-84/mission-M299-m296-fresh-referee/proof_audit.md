# M299 clean-room proof audit of frozen M296

Date: 2026-08-14 UTC.

## 1. Verdict and scope

```text
FINAL VERDICT: ACCEPT M296 AT ITS STATED NONTERMINAL SCOPE.
MATERIAL OBJECTIONS: NONE.
```

The accepted content is an exact reparameterization of simultaneous endpoint
fibers by transporter-coset intersections inside the literal doubled-star
point stabilizer, its pairwise double-coset diagnostic, the explicit short
local stabilizer elements, and a complete but exponentially indexed
Reidemeister--Schreier inventory. SSTID remains unresolved.

The ambient project target is uniform on the global fixed-length identity
bridge, with the lazy exact same-product `{3,4,5}` heat-bath kernel fixed in
`GOAL_SPEC.md`. M296 proves only deterministic statements in the minimal
connected sector `Z_d`, `m=2d-2`, for `d>=6`. Nothing audited below is a
conductance, spectral-gap, or mixing theorem.

## 2. Immutable package and exact inventory

The SHA-256 of M296's `SHA256SUMS` is exactly

```text
9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f.
```

The directory contains exactly seven payloads plus `SHA256SUMS`. The seven
manifest rows are exactly:

| payload | SHA-256 |
|---|---|
| `plan.md` | `2bcd43b5405673d194af941ec8d2898fa4091543766d2540089360af55f5c6ec` |
| `checkpoint.md` | `221574b9886b2dbc1948ace4fbf3f73a0e22570344c25cebfc3f05a9b5f6cd9f` |
| `dependency_audit.md` | `546795f8f8ec82f9866196c902439f8ef53670774a708094d9d09ac694a7d5d6` |
| `framed_stabilizer_transporter.md` | `82dfe01919e4726f7b5d4e1b7c2f44d85ea91534b3de8a48970f1a6c0f70c2d7` |
| `report.md` | `4006dd7bfa22b41a958eadffd134fc368d69b94f3ca22de7c6dc76c932c49fd0` |
| `audit_request.md` | `152230121baba2466efd06dae98b970f62320ebdd6db080a0c13c19f1c0e8e0c` |
| `freeze_manifest.md` | `f49364c40b45ed24d190310335884a4dd0e1097b9a576a7c35096b94d5c355c9` |

Every row passes `sha256sum -c`; no unlisted payload is present.

## 3. Cited-input audit

The eight predecessor top digests and all 60 payload rows independently pass:

| mission | rows | reproduced top digest | imported content checked |
|---|---:|---|---|
| M112 | 13 | `43b5255f014d8d7e480aa6d17130bb982e30b12a763c20a94e8c453de38f9cb3` | rooted DPS product |
| M119 | 8 | `1fa3bddcbc228cdf61e9be9fb316f9da88b38f44fb8d1c8fb8dd4638bac966a8` | fresh acceptance of root quotient |
| M135 | 7 | `8d7ca3afbab24be7b1552b433e9f0f0260efbbb658af4bd66cccd676452a5358` | free actions, incidence matchings, action fibers |
| M137 | 6 | `47dfb3f81d5e16e88b676f57f0c6fc0237b7993fff5c5c4a071046c597c51af5` | fresh audit of M135 |
| M284 | 6 | `3176a4b175fd58f65ed2b71d81c5d2f1fc794cb9e7c7e2370ebcecaff19a62f3` | word-level rank lift and chart obstruction |
| M288 | 8 | `fd4120e216b9140c4a8938724c3415393d6f5495a105f817cf681871545942ca` | fresh audit of M284 |
| M291 | 7 | `cc60538b886df2a332dd06e6b3fc8ee1fb9cb2d032ef77b39c269c1fdafbc4b0` | individual frames and intrinsic fibers |
| M294 | 5 | `64f2e3305855de7d9eaa57e4b315e7d379442acc6a1588389106f222feb9333a` | fresh audit of M291 |

M13 predates the freeze format. Its two cited artifacts reproduce as

```text
diameter_audit.md  536fd8acf9b263984736b0f7bc2f986e8aa27bde14bf4392b4c60efc60febb67
report.md          4cf19e45d9b0306b8e8744ae1cfc0935bba5ca7bbb64f62599f0e85dc7064324
```

The semantic imports are also exact:

1. M13 supplies an individual signed-Hurwitz route of length at most
   `50Nm^3` between words with the same labeled weighted support-component
   data. With `N=d`, `m=2d-2`, this is
   `L_d=50d(2d-2)^3`. It supplies no common route or congestion.
2. The rooted DPS law has cardinality
   `d^(d-2)(2d-2)!` before forgetting the root and is exactly `d`-to-one.
   Hence `|Z_d|=d^(d-3)(2d-2)!`.
3. M135/M137 proves the free `G=S_d` and `H=Stab_G(d)` actions and that
   every perfect-matching color selects one actual `H`-orbit edge over
   every left global orbit. Conflict independence is not simultaneous
   realization.
4. M284/M288 begins rank lifting only after a genuine common literal base
   schedule and valid chart are available; chart/local-type-only coverage is
   false.
5. M291/M294 supplies separate short source and target frames through the
   fixed doubled-star chart and the intrinsic fibers
   `alpha_Q;S;delta_Q^(-1)`. Its exponential obstruction is only to
   one-sided common chart prefixes or inverse suffixes.

No cited input supplies SSTID or any downstream mixing claim.

## 4. Chronological residualization

Use the right action convention

```text
w^(x;y)=(w^x)^y
```

and write

```text
F_Q=alpha_Q;S;delta_Q^(-1),
S={s:c^s=c}.
```

Fix a reference `Q_0`. Every `beta in F_0` has the unique form

```text
beta=alpha_0;s;delta_0^(-1),   s in S,
```

because `s=alpha_0^(-1);beta;delta_0`. For another `Q`,

```text
beta in F_Q
iff alpha_Q^(-1);beta;delta_Q in S
iff L_Q;s;R_Q in S,
```

where the only orientation consistent with chronological composition is

```text
L_Q=alpha_Q^(-1);alpha_0,
R_Q=delta_0^(-1);delta_Q.
```

Thus

```text
C_Q={s in S:L_Q;s;R_Q in S}.
```

Acting on `c`, the residual condition is

```text
c^(L_Q;s;R_Q)=c
iff (c^L_Q)^s=c^(R_Q^(-1)).
```

Consequently, with
`x_Q=c^L_Q` and `y_Q=c^(R_Q^(-1))`,

```text
C_Q=Trans_S(x_Q,y_Q)
```

and cancellation in the unique reference parameterization gives exactly

```text
intersection_Q F_Q
 =alpha_0;(intersection_Q C_Q);delta_0^(-1).
```

This is a two-sided residualization. It does not select a common source
prefix.

## 5. Pairwise double cosets and coset orientations

If `s in C_Q`, put `t=L_Q;s;R_Q in S`. Then

```text
L_Q=t;R_Q^(-1);s^(-1) in S;R_Q^(-1);S.
```

Conversely, if `L_Q=a;R_Q^(-1);b` with `a,b in S`, then choosing
`s=b^(-1)` gives `L_Q;s;R_Q=a in S`. Therefore

```text
C_Q != empty
iff S;L_Q;S=S;R_Q^(-1);S.
```

Taking an arbitrary edge `P` as reference gives, with no reversal,

```text
F_P intersect F_Q != empty
iff
S;alpha_Q^(-1);alpha_P;S
 =S;delta_Q^(-1);delta_P;S.
```

This is equality of literal braid double cosets. Equivalently, left
multiplication by `S` does not move `c`, and right multiplication moves
`c^g` around its `S`-orbit, so `S g S` classifies that orbit.

Now choose `s_Q in C_Q`. For a right action, direct multiplication gives

```text
C_Q=Stab_S(x_Q);s_Q=s_Q;Stab_S(y_Q).
```

Since `Stab_Gamma(c^g)=g^(-1);S;g`,

```text
Stab_S(x_Q)=S intersect L_Q^(-1);S;L_Q,
Stab_S(y_Q)=S intersect R_Q;S;R_Q^(-1).
```

Hence the exact orientation requested in the audit is

```text
C_Q=s_Q;[S intersect R_Q;S;R_Q^(-1)].
```

The bracketed subgroup fixes both `c` and `y_Q`; “two-point stabilizer”
has precisely that relative meaning. Pairwise nonemptiness does not imply a
common point in several such varying cosets.

## 6. Frame covariance, finite action, and length

For alternate frames

```text
alpha_Q'=alpha_Q;u_Q,   delta_Q'=delta_Q;v_Q,
u_Q,v_Q in S,
```

one obtains

```text
L_Q'=u_Q^(-1);L_Q;u_0,
R_Q'=v_0^(-1);R_Q;v_Q.
```

Removing the outer nonreference stabilizer factors from the membership test
shows

```text
C_Q'=u_0^(-1);C_Q;v_0.
```

Thus all constraints receive the same reference-dependent two-sided
translate, while nonreference frame choices cancel.

Let `p:Gamma->A` be the finite action image and
`Sbar=Stab_A(c)`. By definition,

```text
S=p^(-1)(Sbar),   p(S)=Sbar.
```

Every residual transporter is therefore the full preimage of its finite
transporter. A single common finite action has any one braid lift lying in
all literal transporters. Common nonemptiness is preserved exactly, while
shortest literal braid length is not.

Finally,

```text
beta=alpha_0;s;delta_0^(-1),
s=alpha_0^(-1);beta;delta_0
```

and the two reference frames have length at most `L_d`. The triangle
inequality gives both

```text
|beta|<=2L_d+|s|,   |s|<=2L_d+|beta|.
```

Polynomial representative length is therefore equivalent across the exact
residualization, not automatic from finite-action nonemptiness.

## 7. Local doubled-star stabilizer checks

Write

```text
c=e_1,e_1,e_2,e_2,...,e_(d-1),e_(d-1),
e_r=(1,r+1).
```

For every involution `a`,

```text
R(a,a)=(a,a),
```

so `R_(2r-1) in S`. For adjacent star edges `a,b`, put `z=bab`.
The three incident transpositions form the usual triangle, and direct
right-Hurwitz evaluation gives

```text
(a,b) -> (b,z) -> (z,a) -> (a,b).
```

Hence `R_(2r)^3 in S`.

For

```text
q_r=R_(2r);R_(2r-1);R_(2r+1);R_(2r),
```

direct evaluation for involutions `a,b` is

```text
(a,a,b,b)
 -> (a,b,bab,b)
 -> (b,bab,bab,b)
 -> (b,bab,b,a)
 -> (b,b,a,a).
```

Thus `q_r` swaps adjacent square blocks and `q_r^2 in S` with displayed
length eight. On the doubled-star chart, `q_r` is global conjugation by
the transposition of the two relevant leaves, but it changes the literal
factor tuple. It is not itself in `S`.

## 8. Reidemeister--Schreier inventory

Choose `t_x` with
`c^t_x=x`, `|t_x|<=L_d`, and `t_c=1`. For every signed generator
`g=R_j^(+/-1)` and `y=x^g`, set

```text
h_(x,g)=t_x;g;t_y^(-1).
```

The state path is `c -> x -> y -> c`, so every row lies in `S`. If
`s=g_1;...;g_k in S` and
`x_i=c^(g_1;...;g_i)`, then `x_0=x_k=c` and the literal group product
telescope is

```text
s=product_i [t_(x_(i-1));g_i;t_(x_i)^(-1)].
```

No action quotient is used in this cancellation. The rows generate the full
literal subgroup `S`.

Each row has a displayed representative of length at most

```text
2L_d+1=100d(2d-2)^3+1.
```

There are at most

```text
2(2d-3)|Z_d|
 =2(2d-3)d^(d-3)(2d-2)!
```

indexed rows. Duplicates and identities are allowed, so this is an upper
bound. The factorially large index set is the decisive firewall: short
individual generators do not give a polynomial-size presentation, short
transporter, polynomial orbit diameter, or SSTID.

## 9. Exact stopping line

For a subfamily `I`, the family has a common braid of polynomial length if
and only if its higher-arity residual intersection

```text
intersection_(Q in I) C_Q
```

contains a polynomial-length element of `S`. Therefore M296's SSTID is
necessary and sufficient for the framed-stabilizer polynomial cover at this
interface. The pairwise double-coset graph is only a necessary diagnostic.

```text
ACCEPT:
  chronological residualization and tuple-transporter identity;
  literal pairwise double-coset equivalence;
  both transporter-coset orientations and conjugate stabilizers;
  frame covariance and exact finite-action nonemptiness;
  polynomial length equivalence;
  local doubled-star stabilizer elements;
  complete short but exponentially indexed Schreier inventory.

UNRESOLVED:
  SSTID higher-arity intersections and short representatives;
  true polynomial matching-coset refinement.

NO INFERENCE:
  common-prefix revival; every-color route; rank lift; voltage;
  congestion; spectral gap; mixing; Terminal A or Terminal B.
```

## 10. Objections and qualifications

### Material objections

None. Zero numbered material objections.

### Nonmaterial qualifications

1. `A_d` in M296 Proposition 6.2 denotes the finite braid-action image,
   not the alternating group; M296 defines the notation locally, so this is
   only a reading guard.
2. “Two-point stabilizer” and “complete short Schreier inventory” are exact
   algebraic descriptions, not polynomial structural theorems. M296 already
   states both limitations explicitly.
