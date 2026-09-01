# M280 halfway checkpoint

Date: 2026-08-14 UTC.

## Exact reconstruction reached

For odd `k>=3`, `n=3k`, target lag `ell=y+1`, and normalized channel
difference

```text
eta_j=H_(j,B)-H_(j,A),                    j=1,2,
```

the literal M161/M261 response gives

```text
CP_j(k,y)=Lambda_n/R_n * eta_j(F_ell),
Lambda_n=(n-2)(1-2/n)^(-(n-3)),
R_n=(n-3)(n-4),

F_ell(s)=sum_(a,b) kappa_ab(s) C_ab^s(ell),
C_ab^s(ell)=sum_(r mod n) chi_a^s(r)chi_b^s(r+ell).
```

The outer `eta_j` retains the normalized M91 source laws and their literal
`T/D` outcomes.  Terms `a=b` retain the `IS/IN` phase classification; terms
`a!=b` are exactly `X`.  Invalid phases are zero.  The equivalent direct raw
form is M274/M277's `(H_(j,B)-H_(j,A))(2W/(A_s pi_y))`, and the equivalent
Abel form retains both gradient and embedding sums before the channel sign.

The scalar prefactor is positive.  Therefore CP is exactly the pair of
standalone inequalities

```text
(OCI_j)   eta_j(F_ell)>=0
          for j=1,2, odd k>=3, 2<=ell<=n-2.
```

Statewise reflection `F_ell=F_(n-ell)` covers both endpoints and gives the
same reflection for every channel separately.

## Implication chain and proved input

With positive source-independent `alpha_1,alpha_2`,

```text
CP_1,CP_2>=0
 => z_k(y)=alpha_1 CP_1+alpha_2 CP_2>=0             (OS+)
 => N_k=0 and k min(P_k,N_k)=0                      (MS)
 => FCL1,
```

where only the last implication uses accepted M266/M268 PCS through

```text
sum_y|kz_k(y)|
 =k|sum_y z_k(y)|+2k min(P_k,N_k).
```

No later-cell, direct-L1, gap, mixing, or Terminal conclusion is licensed.

## Analytic obstruction

M272/M276's exact monotone `q`-to-`p` transport may be applied with
`g=F_ell`; it telescopes every gradient and embedding term to

```text
eta_j(F_ell)=E_j[F_ell(X_T)-F_ell(Y_S)].
```

This is an equality of expectations only.  The response is not ordered
along the path: frozen M274/M277 refutes the adjacent/embedding MON order,
response FOSD, and literal raw-atom positivity.  Hence this coupling does
not prove `(OCI_j)`.  The positive channel-two kind transfer also remains
separate from its signed collision/decorated coefficient, while channel one
has zero kind transfer.  No valid analytic sign proof has emerged.

## One predeclared exact falsifier

Use the sole allowed new finite test at exactly `k=11` (`n=33`), every
`ell=2,...,31`, and both channels.  Enumerate only the literal first two
ordered source factors, evaluate `F_ell` by exact owner correlations, and
record the full `T/D` by `IS/IN/X` decomposition.  Required guards:

- each source law and each conditional channel normalizes exactly;
- direct response equals the sum of all six kind/topology pieces;
- channelwise reflection and both lag endpoints agree;
- `alpha_1 CP_1+alpha_2 CP_2` has the accepted normalization;
- all arithmetic is `Fraction`, deterministic, `seed=null`.

A negative entry refutes CP and will be frozen as the first exact
counterexample.  All-positive `k=11` data remain finite-only and leave
`(OCI_j)` open.
