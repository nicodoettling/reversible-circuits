# M312: weighted framed transporter-signature hierarchy

Date: 2026-08-14 UTC.

Status: **exact recursive and weighted-normalization laws proved; the
predeclared forced-signature route is obstructed as a formal consequence of
the accepted geometry; actual `d>=6` WRAD remains unresolved.**

## 1. Scope, conventions, and finite/literal boundary

Fix `d>=6`, `m=2d-2`, one adjacent edit index, and one actual perfect
matching `M` of M135's orbit-incidence multigraph.  Let `Gamma=B_m` act on
the right on `Z_d`, with chronological multiplication

```text
w^(g;h)=(w^g)^h.
```

Fix the doubled-star chart `c` and write

```text
S={s in Gamma:c^s=c}.
```

For every matching-selected edge `Q`, M291/M294 supplies short frames

```text
w_Q^alpha_Q=c,       tau_i(w_Q)^delta_Q=c.
```

M296/M299 proves that the literal endpoint fiber is

```text
F_Q=alpha_Q;S;delta_Q^(-1).                          (1.1)
```

Let `p:Gamma->A_d` be the finite action image and
`Sbar=Stab_(A_d)(c)`.  Then `S=p^(-1)(Sbar)`.  All membership and
nonemptiness statements below descend exactly to `A_d`; a finite element
or a lift of it need not have polynomial shortest literal braid length.

No pair-overlap moment is used anywhere in this note.

## 2. Exact anchored weighted normalization

For nonnegative weights put

```text
W_lambda(a)=sum_(Q in M)lambda_Q 1[a in K_Q],
W*(lambda)=max_(a in A_d)W_lambda(a).
```

Fix an anchor `Q_0`, abbreviate its frames by `alpha_0,delta_0`, and define

```text
L_Q=alpha_Q^(-1);alpha_0,
R_Q=delta_0^(-1);delta_Q,
C_Q={s in S:L_Q;s;R_Q in S}.                         (2.1)
```

Here `L_0=R_0=1` and `C_0=S`.

### Proposition 2.1 (anchored WRAD identity; **PROVED**)

For a fixed anchor,

```text
max_(a in K_(Q_0)) W_lambda(a)
 =max_(s in S) sum_(Q in M)lambda_Q
                    1[L_Q;s;R_Q in S].              (2.2)
```

For every nonzero weight vector,

```text
W*(lambda)
 =max_(Q_0 in supp(lambda)) max_(s in S)
    sum_(Q in M)lambda_Q 1[L_Q;s;R_Q in S],          (2.3)
```

where the frames and `L_Q,R_Q` in the inner maximum are normalized at that
`Q_0`.

#### Proof

Every literal braid satisfying the anchor has the unique form

```text
beta=alpha_0;s;delta_0^(-1),       s in S.
```

Using (1.1),

```text
beta in F_Q
iff alpha_Q^(-1);beta;delta_Q in S
iff L_Q;s;R_Q in S.                                  (2.4)
```

Projection is the full preimage of the finite stabilizer, so maximizing
over literal `s` gives exactly the finite conditional maximum, proving
(2.2).  For (2.3), choose a global maximizer `a*`.  Individual fibers are
nonempty, so `W*(lambda)>0`; hence `a*` agrees with some positive-weight
edge `Q_0`.  It appears in that anchor's conditional maximum.  Every
conditional maximum is bounded by the global one, giving equality.  QED.

Thus a single arbitrarily preselected anchor gives only a conditional
maximum.  The outer positive-weight anchor in (2.3) is material.

## 3. Exact hierarchical transporter signatures

M296's point coordinates are

```text
x_Q=c^L_Q,       y_Q=c^(R_Q^(-1)),
C_Q={s in S:x_Q^s=y_Q}.                              (3.1)
```

For a finite ordered tuple `I` of distinct matching edges, define

```text
T_I=intersection_(P in I) C_P.
```

Suppose `T_I` is nonempty and choose `s_I in T_I`.  Put

```text
H_I={h in S:x_P^h=x_P for every P in I},
z_Q^I=y_Q^(s_I^(-1)),
D_I(Q)={h in H_I:x_Q^h=z_Q^I}.                       (3.2)
```

The exact subset `D_I(Q)` is the residual transporter signature of `Q` at
the node `I`.

### Theorem 3.1 (recursive action and higher-arity law; **PROVED**)

For every compatible `I`,

```text
T_I=H_I;s_I.                                         (3.3)
```

For every further tuple `J`,

```text
T_(I union J)
 ={h;s_I:h in intersection_(Q in J)D_I(Q)}.          (3.4)
```

In particular, `I union J` is compatible exactly when the residual
signatures in (3.4) have a common point.

#### Proof

If `h in H_I`, then the source tuple first remains fixed under `h` and is
then sent to the target tuple by `s_I`, so `h;s_I in T_I`.  Conversely, if
`s in T_I`, then

```text
x_P^(s;s_I^(-1))=y_P^(s_I^(-1))=x_P
```

for all `P in I`; hence `s;s_I^(-1) in H_I` and (3.3) follows.  For
`s=h;s_I`, the additional equation for `Q` is

```text
x_Q^(h;s_I)=y_Q
iff x_Q^h=y_Q^(s_I^(-1))=z_Q^I
iff h in D_I(Q).
```

Impose this simultaneously for every `Q in J` to obtain (3.4).  QED.

### Proposition 3.2 (witness and frame covariance; **PROVED**)

Every other node witness is `s'_I=g;s_I` for some `g in H_I`, and

```text
z_Q'= (z_Q^I)^(g^(-1)),
D'_I(Q)=D_I(Q);g^(-1).                               (3.5)
```

Thus nonemptiness, equality to all of `H_I`, and common intersection of the
residual signatures are independent of the chosen witness.

Under the accepted frame changes

```text
alpha_Q'=alpha_Q;u_Q,     delta_Q'=delta_Q;v_Q,
u_Q,v_Q in S,
```

the normalized data transform by

```text
x_Q'=x_Q^u_0,      y_Q'=y_Q^v_0,
s_I'=u_0^(-1);s_I;v_0,
H_I'=u_0^(-1);H_I;u_0,
D_I'(Q)=u_0^(-1);D_I(Q);u_0.                         (3.6)
```

Consequently every hierarchical predicate used below is intrinsic.

#### Proof

Equation (3.5) follows by substituting `s'_I=g;s_I` in (3.2).  For (3.6),
M296's frame covariance gives

```text
L_Q'=u_Q^(-1);L_Q;u_0,
R_Q'=v_0^(-1);R_Q;v_Q.
```

Since the nonreference factors fix `c`, the stated point transforms follow.
Direct conjugation then gives the stabilizer and transporter transforms.
QED.


### Corollary 3.3 (one-pivot signature action; **PROVED**)

If `P` is extendable from `I`, choose `h_P in D_I(P)` and set

```text
I'=I union {P},
s_(I')=h_P;s_I,
H_(I')=H_I intersect Stab_S(x_P),
z_Q^(I')=(z_Q^I)^(h_P^(-1)),
D_(I')(Q)={k in H_(I'):x_Q^k=(z_Q^I)^(h_P^(-1))}.   (3.7)
```

Then `s_(I')` is a witness for the child node, and (3.7) is the exact
signature update for every remaining constraint.  Iterating (3.7) gives the
higher-arity law (3.4), with no averaging.

#### Proof

Equation (3.4) with `J={P}` puts `h_P;s_I` in `T_(I')`.  The new
source stabilizer is the old tuple stabilizer intersected with the stabilizer
of `x_P`.  Finally invert `h_P;s_I` in the definition of `z_Q` and
substitute into (3.2).  QED.

## 4. The predeclared HSCA candidate

Define the forced-true signature cell

```text
F(I)={Q in M:D_I(Q)=H_I}.                            (4.1)
```

This is witness-independent by (3.5).  More explicitly,

```text
Q in F(I)
iff x_Q is fixed by every h in H_I
    and x_Q^s_I=y_Q.                                 (4.2)
```

Indeed the identity element of `H_I` first forces `z_Q^I=x_Q`, after which
`D_I(Q)=H_I` says exactly that `H_I` fixes `x_Q`.

The plan predeclared HSCA: for every actual matching and every nonzero
weight vector, find a compatible tuple `I` containing a positive-weight
anchor, with `|I|=O(log d)`, such that

```text
lambda(F(I))>=||lambda||_1/d^C.                      (4.3)
```

### Proposition 4.1 (HSCA implies WRAD; **PROVED**)

Every element of `T_I=H_I;s_I` satisfies every edge in `F(I)`.  Hence
(4.3), followed by the anchored identity (2.3), gives WRAD with the same
polynomial exponent.  This uses pointwise forced completion, not an average
or a pair moment.  QED.

## 5. First exact obstruction: forced signatures are too rigid formally

The accepted abstract `Sym/Alt` identity matching gives a decisive test of
the proof mechanism, now without using its RCOM calculation.

Let `X` have `N=N_d` points, where

```text
N_d=d^(d-3)(2d-2)!/d!,
```

and let `A=Sym(X)` or `Alt(X)` in its natural action.  Put
`K_x={a:a(x)=x}` and use unit weight on every constraint.  The identity
action agrees with all constraints, so WRAD holds with density one.

Choose an anchor and any compatible pivot tuple `I` of size `t`.  In the
anchored hierarchy `H_I` is the pointwise stabilizer of the `t` pivot
points.  If `N-t>=2` for `Sym(X)`, or `N-t>=3` for `Alt(X)`, its fixed-point
set is exactly the pivot set.  By (4.2), therefore,

```text
F(I)=I,       lambda(F(I))/||lambda||_1=t/N.          (5.1)
```

Since `N_d>=d^(d-3)`, for every fixed polynomial pivot bound `t<=d^B` and
every fixed `C`,

```text
t/N_d < d^(-C)
```

for all sufficiently large `d`.  Thus even allowing polynomial rather than
logarithmic pivot depth does not make the forced-cell mechanism follow from
general transitivity, uniform point fibers, and transporter-coset geometry.

This is a **proved obstruction to deriving HSCA from the accepted formal
geometry alone**, not a realization inside the actual M135 matching.  It
does not refute actual HSCA.  It shows exactly what a proof would still need:
an actual-specific theorem that small tuple stabilizers acquire enormous
fixed closures.  No accepted matching, frame, subgroup, or routing input
supplies such a fixed-closure theorem.

## 6. Strict surviving reduction: conditional-compatibility collapse

The recursive law exposes a weaker signature that is not defeated by the
forced-cell obstruction.  For the positive-weight support
`U=supp(lambda)`, define the individually extendable cell

```text
G_I(U)={Q in U:D_I(Q) is nonempty}
      ={Q in U:T_I intersect C_Q is nonempty}.        (6.1)
```

It is intrinsic by (3.5).  Call `I` **collapsing** when

```text
intersection_(Q in G_I(U)) D_I(Q) is nonempty.       (6.2)
```

By (3.4), (6.2) is exactly the higher-arity statement that one completion
of the node satisfies every constraint that is individually extendable from
the node.

> **POLYNOMIAL HIERARCHICAL TRANSPORTER COLLAPSE (PHTC).**  There are
> universal constants `B,C` such that for every actual `d>=6` matching and
> every nonzero `lambda>=0`, some positive-weight anchor admits a compatible
> pivot tuple `I` of size at most `d^B` for which
> ```text
> lambda(G_I(U))>=||lambda||_1/d^C
> ```
> and (6.2) holds.

### Proposition 6.1 (PHTC implies WRAD; **PROVED**)

Choose `h` in (6.2).  Equation (3.4) says that `h;s_I` lies in every
`C_Q`, `Q in G_I(U)`.  Its weighted agreement is therefore at least the PHTC
lower bound.  Apply (2.3).  QED.

PHTC survives both exact obstructions currently on record:

- In the `Sym/Alt` identity matching, take only the anchor.  Every
  positive-weight constraint is individually extendable and the identity
  lies in their total intersection, so `G_I(U)=U` and the node collapses.
- In M301/M304's actual `d=3` triple, any two fibers meet in a singleton and
  the triple intersection is empty.  Choose the pair of greatest total
  weight.  Its transporter is a singleton, its extendable cell is exactly
  that pair, and it captures at least two thirds of the total weight.

These checks do not prove PHTC at actual `d>=6`; they only show that it is a
strictly surviving higher-arity reduction rather than a rephrased pairwise
Helly rule.  PHTC asks for a polynomial-size compatibility certificate and
one exact common residual point.  It does not average intersections.

## 7. Exact stopping line

```text
anchored WRAD normalization with outer anchor        proved
recursive signature and higher-arity law             proved
witness/frame covariance                              proved
HSCA => WRAD                                          proved
HSCA from generic framed transporter geometry         obstructed
actual d>=6 HSCA                                      unresolved
PHTC => WRAD                                          proved
actual d>=6 PHTC/WRAD                                 unresolved
polynomial literal representative length              unresolved separately
```

The first new actual-specific obligation is PHTC.  No `d=6` computation was
run: after the exact analytic obstruction, a selected-matching guard would
not prove the missing all-rank fixed-closure or collapse theorem, and the
mission rules forbid a broad universe/stabilizer census.

No MRAD, SSTID, routing, voltage correction, congestion, spectral gap,
mixing, or Terminal conclusion is inferred.
