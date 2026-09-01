# M337 exact pivot averaging and higher-orbital stop

Date: 2026-08-14 UTC

Status: **exact identities and a heavy-active-pivot lemma proved; actual
high-density RATSD selection and low-density whole-child terminality remain
unresolved.** No computation was run.

## 1. Exact pairwise weight averages

At the authenticated node of `candidate.md`, set

```text
n(P)=W-c(P)=lambda({Q:{P,Q} in E}).
```

Every unordered incompatibility edge contributes its weight product once to
`n(P)` at each endpoint. Therefore

```text
sum_(P in V)lambda_P n(P)=2Phi=rho W^2,             (1.1)
sum_(P in V)lambda_P c(P)=W^2-2Phi=W^2(1-rho).     (1.2)
```

Inactive vertices have `n(P)=0` and are compatible with every vertex. Thus
the left side of `(1.1)` is already an active-pivot sum. These are exact
arbitrary-weight identities; they use the residual incompatibility graph,
not M135 conflict edges.

## 2. Weight-dependent heavy active pivot

> **Lemma 2.1 (proved).** If `rho>0`, some active pivot satisfies
> ```text
> c(P)>=(1-sqrt(rho))W.                              (2.1)
> ```

### Proof

Let `L=lambda(A)` be the total active weight. If `L<=sqrt(rho)W`, every
active pivot is compatible with all inactive vertices, so

```text
c(P)>=W-L>=(1-sqrt(rho))W.
```

If `L>sqrt(rho)W`, divide `(1.1)` by `L`. Some active `P` has

```text
n(P)<=rho W^2/L<sqrt(rho)W,
```

and hence `(2.1)`. QED.

This lemma retains arbitrary real weights and requires no support-cardinality
bound. At low density it controls the weight loss of at least one active
pivot. It says nothing about that pivot's whole child triple shadow `T(P)`.

## 3. Exact whole-triple-shadow Fubini identity

For an unordered pair `{Q,R}` define its active pivot shadow

```text
Sh(Q,R)={P in A:
          Q,R in C(P),
          D_I(P) intersection D_I(Q) intersection D_I(R)=empty}.
```

Interchanging the finite sums in the definition of `T(P)` gives

```text
Xi_A:=sum_(P in A)lambda_P T(P)
 =sum_({Q,R} subset V)lambda_Q lambda_R lambda(Sh(Q,R)).  (3.1)
```

If `{Q,R}` is a parent incompatibility edge, its pair intersection is already
empty and

```text
Sh(Q,R)=A intersection C(Q) intersection C(R).
```

If it is parent-compatible, membership in `Sh(Q,R)` is exactly a genuinely
regenerated empty triple intersection. Thus `(3.1)` contains both retained
parent edges and the full regenerated triple shadow; neither may be deleted
or replaced by an induced graph.

Since `rho'_P=2T(P)/c(P)^2`, `(3.1)` is equivalently

```text
sum_(P in A)lambda_P c(P)^2 rho'_P=2Xi_A.           (3.2)
```

Writing `Z_A=sum_(P in A)lambda_P c(P)^2`, one obtains the exact active-pivot
average

```text
min_(P in A)rho'_P <= 2Xi_A/Z_A
                   <= max_(P in A)rho'_P.           (3.3)
```

Equations `(3.1)--(3.3)` are the strongest averaging identity supplied by the
accepted one-/two-/three-signature algebra. An actual relative-descent theorem
must control the higher-orbital numerator `Xi_A`; pairwise density `rho` alone
does not do so.

## 4. Exact conditional W-RATSD+HLDT implication

The proof in Section 3 of `candidate.md` is complete. Under its universally
quantified but unproved anchor, high-density selection, and low-density
terminality clauses:

1. at most `ceil(B_low d^B_rel log d)` nonterminal steps occur;
2. nonterminal logarithmic losses telescope to at most `C_log log d`;
3. the terminal step loses at most `C_fin log d` by a separate explicit
   clause;
4. the final whole child is edgeless and retains weight at least
   `||lambda||_1/d^(C_init+C_log+C_fin)`.

This proves only the conditional quantitative implication. It does not prove
the candidate hypotheses or promote HPRN.

## 5. First actual higher-orbital lemmas

The exact averages isolate two standalone actual-family obligations.

> **ACTUAL HIGH-DENSITY WEIGHTED TRIPLE-SHADOW SELECTION (AHTSS).** Above
> `rho=d^(-B_low)`, an active pivot satisfies the whole-child relative drop
> and logarithmic payment in `(2.3)` of `candidate.md`, unless it has an
> edgeless child with the final-step weight bound `(2.2)`.

> **ACTUAL HEAVY LOW-DENSITY TERMINALITY (AHLDT).** Below that threshold,
> some active pivot in the heavy set guaranteed by Lemma 2.1 has
> ```text
> T(P)=0.                                            (5.1)
> ```

For `B_low>=1` and `d>=6`, Lemma 2.1 would then give a stronger final mass
than `W/d`: `c(P)>W/2`. Thus AHLDT includes the required final-step loss
without a support-size assumption.

Both AHTSS and AHLDT are **unresolved for the actual `d>=6` family**. They
are statements about actual triple orbitals, not graph theory.

## 6. Why pair averaging cannot prove the missing lemma

A tempting generic inequality would bound the triple-shadow numerator by

```text
2Xi_A <= rho Z_A.                                   (6.1)
```

The accepted `d=3` star/triple boundary data formally refutes `(6.1)` as a
set-algebra or graph consequence. Give each of the three leaves weight one
and the center weight `epsilon`. Each leaf is a heavy active pivot with
`c(P)=3`, `T(P)=1`, while the center has `T(P)=0`. Hence

```text
2Xi_A=6,
Z_A=27+epsilon^3,
rho=6epsilon/(3+epsilon)^2,
```

so the right side of `(6.1)` tends to zero. Equivalently, every heavy leaf
regenerates the child edge even as the parent conflict density vanishes; only
the vanishing-weight center is terminal.

This is used solely to refute a generic pair-averaging proof and to validate
the final-step quantifier. It is not promoted to an actual `d>=6`
counterexample. AHTSS/AHLDT could still follow from new actual higher-orbital
structure, but no authenticated predecessor supplies it.

## 7. Stop

No `d=6` guard is warranted: a finite census cannot prove the universal
actual higher-orbital clauses, and no single local formula beyond
`(3.1)--(3.3)` is left ambiguous. No induced-child, unweighted MIDEC,
polynomial-support, transitivity, pair-moment, or conflict-independence
shortcut is used.

HPRN, WRAD, routing, gap, mixing, Terminal, and every downstream statement
remain unresolved.

