# M152 beta-mixture potential and exact Jensen obstruction

Date: 2026-08-13 UTC.

## 1. Scope and result

This note concerns only the full unweighted reset excursion of the auxiliary
nonlazy stationary-flow parking-degree projection in the minimal-long-cycle
sector.  The project target remains uniform on fixed-length identity
transposition words.  Permutations compose as `(pq)(x)=p(q(x))`, with
displayed factors left-to-right.

The results are:

1. a proved killed-atom Doob identity for arbitrary nonnegative latent-beta
   potentials;
2. a proved global nonnegative beta-mixture/Jensen majorant for the exact
   all-suffix excursion;
3. an exact right-heavy witness refuting the entire associated pointwise
   Jensen-supersolution family as a contraction proof; and
4. an independent exact check that the true excursion at that witness has
   large positive budget slack.

No all-suffix contraction, auxiliary gap, `ROOT-MEAN LIFT`, original-chain
gap, polynomial mixing result, Terminal A, or Terminal B is claimed.

## 2. Coordinates and latent-beta representation

Use the accepted M147/M151 coordinates

```text
s=B+L,  kappa=K+1,  D=K-R,  1<=D<kappa,
q_(B,L)=w_(L+1)w_B/w_(B+L+1).
```

For an attachment group of degree `d`, put `X=d-j`.  The full law is

```text
X~BetaBinomial(d,D,kappa-D),
(kappa,D)->(kappa+d,D+X).                            (2.1)
```

Equivalently, sample

```text
Theta~Beta(D,kappa-D),  X|Theta~Binomial(d,Theta).   (2.2)
```

The excursion retains `j=1,...,d`, equivalently `X=0,...,d-1`, and kills
exactly `j=0`, equivalently `X=d`.  No conditioning on survival is used.

Let `C` be a source composition, with degree `d` and last part `t`.  Define
the point contextual function

```text
g_(B,C)(u)=0,                                      t<B,
            d u^(d-1),                            t=B,
            q_(B,t-B-1)(1-u^d),                  t>B.          (2.3)
```

The accepted contextual mean is exactly

```text
f_(kappa,D;B)(C)=E[g_(B,C)(Theta)].                (2.4)
```

For `t=B`, (2.4) uses
`E[Theta^(d-1)]=(D)^(rise)_(d-1)/(kappa)^(rise)_(d-1)`.
For `t>B`, `E[Theta^d]` is the killed `j=0` mass.

## 3. Exact killed-atom Doob identity

Let `psi:[0,1]->[0,infinity]` be measurable.  Define its beta-mixture value

```text
V_psi(kappa,D)=E_(Theta~Beta(D,kappa-D))[psi(Theta)].          (3.1)
```

Beta-binomial conjugacy says that conditional on `X=x`, the same latent
variable has posterior law

```text
Theta|X=x ~ Beta(D+x,kappa-D+d-x).                            (3.2)
```

Therefore Tonelli's theorem gives

```text
sum_(x=0)^d Pr[X=x]V_psi(kappa+d,D+x)=E[psi(Theta)],

sum_(x=0)^(d-1) Pr[X=x]V_psi(kappa+d,D+x)
 =E[(1-Theta^d)psi(Theta)].                                  (3.3)
```

The second line is the exact retained-subkernel identity.  The removed term
is

```text
Pr[X=d]V_psi(kappa+d,D+d)=E[Theta^d psi(Theta)].               (3.4)
```

In particular `D/kappa` is a martingale under the full law, but (3.3), not
the un-killed martingale statement alone, is the identity relevant to the
excursion.

## 4. Pointwise Jensen reset reward

For every active canonical endpoint `E`, let `B_E` be its source basin and
`c_E=degree(E)rho(E)` its accepted capacity.  Define the point current

```text
J_E(u)=sum_(C in B_E)rho(C)[g_(B,C)(u)-q_(B,L)]                (4.1)
```

and the nonnegative point reset reward

```text
r_(B,L)(u)=sum_E J_E(u)^2/[q_(B,L)c_E].                       (4.2)
```

Writing `A_(B,L)(kappa,D)=A_0/q` for the exact normalized reset energy,
(2.4) and Jensen's inequality yield

```text
A_(B,L)(kappa,D)
 =sum_E E[J_E(Theta)]^2/[q c_E]
 <=E[r_(B,L)(Theta)].                                        (4.3)
```

This uses the exact reset, so it neither invokes nor alters M140's corrected
one-power envelope.  It is a different rigorous upper bound.  The price is
that Jensen discards cancellation across values of the latent variable
separately in every overlapping basin.

## 5. Minimal beta-Jensen Bellman integrand

Let the normalized root-group mass be

```text
mbar_(L,B)(h,d)
 =c(L-h,d-1)/[d! w_(L+1)(w_B/w_(B+h))].                       (5.1)
```

Define recursively, in increasing suffix excess,

```text
phi_(B,L)(u)=r_(B,L)(u)
 +sum_(h=1)^L 1[B+h-1>=2] sum_d
    mbar_(L,B)(h,d)q_(B,h-1)(1-u^d)
      phi_(B,h-1)(u).                                         (5.2)
```

Every coefficient outside the polynomials themselves is nonnegative, and
suffix excess decreases from `L` to `h-1`.  Thus (5.2) defines a finite
nonnegative polynomial, of degree at most `2L`, for every `B,L`.

Set

```text
V_(B,L)(kappa,D)
 =E_(Theta~Beta(D,kappa-D))[phi_(B,L)(Theta)].                 (5.3)
```

> **Theorem 5.1 (proved global majorant).**  For every valid state,
> ```text
> F_(B,L)(kappa,D):=H(B+L,kappa-1,kappa-1-D,B)/q_(B,L)
> <=V_(B,L)(kappa,D).                                         (5.4)
> ```

**Proof.**  Induct on `L`.  Bound the exact reset by (4.3).  For a child of
degree `d`, apply the induction hypothesis at each retained `X=0,...,d-1`.
Equation (3.3) turns the resulting beta-binomial sum exactly into
`E[(1-Theta^d)phi_child(Theta)]`.  Multiplying by the normalized root mass
and child split and summing gives the expectation of the second line of
(5.2).  Adding (4.3) proves (5.4).  The induction is finite because every
child has smaller suffix excess.  QED.

This theorem explicitly accounts for killed mass and holds at arbitrary
deficit.  It is not a contraction theorem because `V` need not respect the
right-heavy boundary budget.

## 6. Exact obstruction to every pointwise Jensen supersolution

Consider any nonnegative functions `psi_(B,L)` that obey the pointwise
supersolution inequality obtained from (5.2):

```text
psi_(B,L)(u)>=r_(B,L)(u)
 +sum_(h,d) mbar q_child(1-u^d)psi_(B,h-1)(u)       for all u. (6.1)
```

Induction on `L` shows `psi_(B,L)(u)>=phi_(B,L)(u)` pointwise.  Hence (5.2)
is the minimal member of the whole family (6.1).

At the fresh right-heavy state

```text
(s,kappa,D,B)=(9,2,1,3),  L=6,
q=q_(3,6)=3176523/25000000,                         (6.2)
```

the beta law is uniform on `[0,1]`.  Exact integration of the degree-twelve
polynomial in (5.2) gives

```text
V_(3,6)(2,1)
 =200725034388752880197118033887607702918039504603683
  /223395363274892426079078092636160000000000000000000.
```

Subtracting `1-q=21823477/25000000` gives

```text
V_(3,6)(2,1)-(1-q)
 =5714491495302498676679596453643417785239504603683
  /223395363274892426079078092636160000000000000000000
 >0.                                                            (6.3)
```

> **Theorem 6.1 (proved route obstruction).**  No beta-mixture potential
> whose latent integrands satisfy the pointwise canonical-basin Jensen
> supersolution (6.1) can both dominate the excursion by this route and obey
> `V_(B,L)(kappa,1)<=1-q_(B,L)` at every right-heavy seed.

This is stronger than failure of one chosen polynomial: every pointwise
supersolution of the named reward dominates the minimal polynomial and hence
fails at (6.2).  It does not refute potentials that retain signed cross-beta
terms, replace the basinwise Jensen step, or amortize on a different state
space.

## 7. The true excursion remains well below budget

The standalone checker separately evaluates the exact basin currents and
the full nilpotent descendant recurrence, without using `phi`.  At (6.2),

```text
exact A_0/q
 =58622378202530621387204787973
  /152536634460000000000000000000
 approximately 0.3843167145,

exact descendant contribution/q
 =9319613794564632698601357521105736737
  /51190344502039685438875740835676160000
 approximately 0.1820580401,

exact H/q
 =884793664847325174104678035065147237189087444781
  /1562205337586660322231315333120000000000000000000
 approximately 0.5663747547.                                      (7.1)
```

Consequently the true budget slack is the positive rational

```text
(1-q)-H/q
 =478916425316663507856429919018519092410912555219
  /1562205337586660322231315333120000000000000000000
 approximately 0.3065643253.                                      (7.2)
```

The obstruction is therefore looseness of the proof device, not failure of
the target inequality.  In particular it is consistent with, and leaves
untouched, the accepted M145/M149 theorem proving right-heavy contraction for
all suffix-excess-six states.

At this witness, the pointwise reset lift is about `0.656632` versus the
exact reset `0.384317`; the lifted descendant charge is about `0.241888`
versus the exact `0.182058`.  The principal loss is already the separate
basinwise Jensen step.

## 8. Exact checks and limitations

Run from this mission directory:

```text
python3 -B beta_potential.py \
  --output beta_potential.json --max-excess 6 --max-kappa 128
```

The script is standalone, standard-library-only, deterministic
(`seed=null`), and uses `fractions.Fraction` for every theorem-critical
calculation.  It checks:

- 2,142 monomial instances of both the full posterior identity and exact
  killed-atom subtraction;
- exact point-context identities and positive Jensen slack at five audit
  states;
- equality of the witness value computed by polynomial integration and by a
  separate discrete beta-binomial child recursion;
- the exact rational witness (6.2)--(6.3); and
- a separate exact reset/resolvent evaluation proving (7.1)--(7.2).

The 21 boundary rows with `B<=3`, `L<=6`, and `kappa<=128` are capped
diagnostics only.  Their passed entries do not prove the boundary for those
suffixes uniformly in `B` or `kappa`; the single exact failed row is promoted
only because its displayed rational evaluation is a complete counterexample
to the universal supersolution claim.

The natural next positive route must preserve some signed dependence across
latent-beta values or use a sharper current-square lift.  A universal
canonical-basin Bessel shortcut is unavailable because the accepted M123/M128
rank-five frame obstruction already refutes that operator inequality.

