# M156 proof audit of frozen M152

Date: 2026-08-13 UTC.

## 1. Immutable gate and scope

All six coordinator-supplied SHA-256 digests match the frozen M152 bytes.
The supplied manifest digest belongs to `freeze_manifest.md`; there is no
`frozen_manifest.json`.  A rerun of the frozen checker to `/tmp` reproduced
the frozen JSON digest
`b4880001fb4b8b706c40ee58ca14dd90649efc204dbdf2a31c551c0c597eb6fa`.

The audited object is the normalized full unweighted reset excursion in the
auxiliary nonlazy minimal-long-cycle parking projection.  It is not a sampler
claim, an auxiliary gap, `ROOT-MEAN LIFT`, an original-chain gap, or a project
terminal.

## 2. Exact retained-subkernel identity

Put `X=d-j`.  Under the accepted attachment law,

```text
Theta ~ Beta(D,kappa-D),
X | Theta ~ Binomial(d,Theta),
(kappa,D) -> (kappa+d,D+X).
```

For nonnegative measurable `psi`, posterior conjugacy gives

```text
Theta | X=x ~ Beta(D+x,kappa-D+d-x).
```

Thus the full posterior average of `V_psi` is `E psi(Theta)`.  More
importantly, the omitted branch is exactly `X=d`, so its joint contribution
is `E[Theta^d psi(Theta)]`.  Subtraction gives

```text
sum_(x=0)^(d-1) P(X=x)V_psi(kappa+d,D+x)
 = E[(1-Theta^d)psi(Theta)].
```

This is an unconditioned killed-subkernel identity: no survival probability
is divided out.  The M152 proof therefore accounts for the killed `j=0` atom
with the correct sign and normalization.  The clean-room checker verified 21
independent monomial instances, checking the full, retained, and killed terms
separately.

## 3. Context lift and Jensen normalization

For a source `C` of degree `d` and last part `t`, the three point functions
have the exact accepted contextual expectations:

```text
t<B: E[0]=0,
t=B: E[d Theta^(d-1)]
     =d(D)rise_(d-1)/(kappa)rise_(d-1),
t>B: E[q_child(1-Theta^d)]
     =q_child[1-(D)rise_d/(kappa)rise_d].
```

The clean-room checker verified this for all 280 literal sources in three
audit contexts, including every one of the 256 compositions at the witness.

For an active canonical endpoint `E`, let

```text
J_E(u)=sum_(C in B_E) rho(C)(g_C(u)-q),
c_E=degree(E)rho(E).
```

Then the exact endpoint current is `theta_E=E[J_E(Theta)]`, and the accepted
reset normalization is

```text
A_0/q = sum_E theta_E^2/(q c_E).
```

Endpointwise Jensen therefore gives exactly

```text
A_0/q <= E[sum_E J_E(Theta)^2/(q c_E)].
```

There is neither an extra nor a missing factor of `q`.  This directly bounds
the exact reset and is logically separate from M140's one-power envelope.

## 4. Bellman recursion and global majorant

Write the point reward as

```text
r_(B,L)(u)=sum_E J_E(u)^2/(q_(B,L)c_E).
```

The accepted normalized excursion recurrence has descendant coefficient
`mbar_(L,B)(h,d) q_(B,h-1)`.  Applying the induction hypothesis to each
retained child and then the retained-subkernel identity from Section 2 turns
the whole degree-`d` child sum into

```text
E[(1-Theta^d) phi_(B,h-1)(Theta)].
```

Consequently the displayed M152 recursion

```text
phi_(B,L)=r_(B,L)
 +sum_(h,d) mbar q_child (1-u^d)phi_(B,h-1)
```

is exactly the induction produced by the accepted recurrence.  Every child
has suffix excess `h-1<L`; hence the induction is finite.  All exterior
coefficients are nonnegative, `r>=0`, and `1-u^d>=0` on `[0,1]`, so `phi` is
nonnegative there.  The reset Jensen inequality supplies the only inequality.
This proves, for every valid attachment state,

```text
H/q <= E[phi_(B,L)(Theta)].
```

The clean-room checker rebuilt this polynomial by enumerating literal root
compositions and their `rho` masses, not by importing or reproducing M152's
grouped Cayley-coefficient routine.

## 5. Minimality in the named family

Suppose nonnegative point functions `psi_(B,L)` satisfy the M152 pointwise
supersolution inequality with the same canonical-basin Jensen reward.  At
suffix excess zero the inequality gives `psi>=r=phi`.  If the claim holds at
all smaller excesses, replacing every child `psi` by the pointwise smaller
child `phi` can only decrease the right side because all multipliers are
nonnegative on `[0,1]`.  The equality recursion then gives `psi>=phi`.

This induction proves pointwise minimality exactly within the named family.
It does not compare against signed cross-beta potentials, sharper
current-square inequalities, nonpointwise amortizations, or other state
spaces.  M152 states this limitation correctly.

## 6. Exact right-heavy witness

At

```text
(s,kappa,D,B)=(9,2,1,3), L=6,
q=3176523/25000000,
```

the beta law is uniform.  The independently rebuilt Bellman polynomial has
degree 12 and exact integral

```text
200725034388752880197118033887607702918039504603683
/223395363274892426079078092636160000000000000000000.
```

A second evaluation through the discrete retained posterior recursion gives
the same fraction.  Subtracting `1-q=21823477/25000000` gives

```text
5714491495302498676679596453643417785239504603683
/223395363274892426079078092636160000000000000000000
>0.
```

Since every pointwise supersolution dominates this polynomial, this one
right-heavy state refutes a uniform boundary certificate for the entire
named family.

## 7. Independent true excursion and L=6 compatibility

Literal-root enumeration of the exact reset and nilpotent descendant
recurrence gives

```text
exact reset/q
 =58622378202530621387204787973
  /152536634460000000000000000000,

exact descendants/q
 =9319613794564632698601357521105736737
  /51190344502039685438875740835676160000,

exact H/q
 =884793664847325174104678035065147237189087444781
  /1562205337586660322231315333120000000000000000000.
```

Therefore

```text
(1-q)-H/q
 =478916425316663507856429919018519092410912555219
  /1562205337586660322231315333120000000000000000000
 >0,
```

approximately `0.3065643253`.  The Jensen reset is approximately `0.656632`
while the exact reset is approximately `0.384317`, confirming that the
witness exposes proof-device looseness.  It is not a counterexample to true
right-heavy contraction and leaves the accepted M145/M149 `L=6` theorem
intact.

## 8. Referee disposition

```text
FINAL VERDICT: ACCEPT.
MATERIAL NUMBERED OBJECTIONS: NONE.
NONMATERIAL CORRECTIONS: NONE.
```

The exact obstruction should be promoted only with its qualifier: it refutes
the pointwise latent-beta canonical-basin Jensen supersolution architecture,
not every deficit-aware potential and not the true contraction inequality.

