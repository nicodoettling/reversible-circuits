# M299 final report: fresh immutable referee of M296

Date: 2026-08-14 UTC.

## Verdict

```text
FINAL VERDICT: ACCEPT M296 AT ITS STATED NONTERMINAL SCOPE.
MATERIAL OBJECTIONS: NONE.
NONMATERIAL QUALIFICATIONS: TWO READING GUARDS.
```

M296's frozen top digest is exactly
`9ab0978c92fee4f92d000604eac4610dbbe6c7aeeaebe3fe86968514990d1f7f`.
Its exact seven-payload inventory has no extra files and every row passes.
All 60 frozen predecessor rows from M112/M119, M135/M137, M284/M288, and
M291/M294 pass at the cited top digests; both cited M13 hashes reproduce.

## Accepted theorem package

With chronological right action, `S=BStab_d`, and one reference edge
`Q_0`, every candidate common braid has the unique form

```text
beta=alpha_0;s;delta_0^(-1),   s in S.
```

For

```text
L_Q=alpha_Q^(-1);alpha_0,
R_Q=delta_0^(-1);delta_Q,
C_Q={s in S:L_Q;s;R_Q in S},
```

the exact identities are

```text
C_Q=Trans_S(c^L_Q,c^(R_Q^(-1))),

intersection_Q(alpha_Q;S;delta_Q^(-1))
 =alpha_0;(intersection_Q C_Q);delta_0^(-1).
```

The pairwise condition and the requested right-coset orientation independently
rederive as

```text
C_Q != empty
 iff S;L_Q;S=S;R_Q^(-1);S,

C_Q=s_Q;[S intersect R_Q;S;R_Q^(-1)]
     =[S intersect L_Q^(-1);S;L_Q];s_Q.
```

The arbitrary-pair formula has exactly M296's orientation. Pairwise
compatibility is not sufficient for a higher-arity intersection.

Frame changes give the common translate
`C_Q'=u_0^(-1);C_Q;v_0`. Projection to the finite action preserves common
nonemptiness because `S` is the full preimage of the finite point
stabilizer, but it does not preserve shortest literal length. The two length
inequalities

```text
|beta|<=2L_d+|s|,   |s|<=2L_d+|beta|
```

are correct.

## Stabilizer and Schreier audit

Direct right-Hurwitz evaluation confirms

```text
R_(2r-1) in S,   R_(2r)^3 in S,
```

and the four-letter `q_r` swaps adjacent doubled-star square blocks, so
`q_r^2 in S` with displayed length eight while `q_r notin S`.

The literal Schreier rows

```text
t_x;R_j^(+/-1);t_(x^R_j^(+/-1))^(-1)
```

telescope exactly and generate all of `S`. Each has representative length
at most `100d(2d-2)^3+1`, but there are as many as

```text
2(2d-3)d^(d-3)(2d-2)!.
```

This is polynomial word length with exponential/factorial indexing, not a
polynomial transporter-diameter theorem.

## Qualifications and stopping line

1. `A_d` in the finite-action proposition is locally defined as an action
   image, not the alternating group.
2. “Two-point stabilizer” and “complete short inventory” must retain M296's
   explicit no-diameter/no-compression qualifications.

SSTID remains the first unresolved lemma: polynomially cover every actual
matching color by subfamilies whose higher-arity `C_Q` intersections contain
polynomial-length literal stabilizer elements.

No common-prefix strategy is revived. No every-color schedule, voltage,
congestion, spectral gap, mixing theorem, Terminal A, or Terminal B follows.
