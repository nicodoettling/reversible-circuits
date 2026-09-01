# M339 independent proof audit

Date: 2026-08-14 UTC

## Pair identities

At an actual compatible node, `V=G_I(supp(lambda))` consists of positive
weight vertices with nonempty signatures. Thus each `P` lies in its own
compatibility child `C(P)`, and

```text
n(P):=W-c(P)=sum_({Q:{P,Q} in E})lambda_Q.
```

Multiplying by `lambda_P` and summing counts each unordered incompatibility
edge once from each endpoint:

```text
sum_P lambda_P(W-c(P))=2Phi=rho W^2.
```

Subtracting from `sum_P lambda_P W=W^2` gives exactly

```text
sum_P lambda_P c(P)=W^2(1-rho).
```

These hold for arbitrary nonnegative input weights after restriction to their
positive support.

## Heavy active pivot

Assume `rho>0`, let `A` be the active vertices and
`L=lambda(A)>0`. Inactive vertices have no incompatibility edge, so every
active pivot is compatible with all inactive weight.

If `L<=sqrt(rho)W`, any active `P` has
`c(P)>=W-L>=(1-sqrt(rho))W`. If
`L>sqrt(rho)W`, the first identity restricted to `A` gives an active
`P` with

```text
n(P)<=rho W^2/L<sqrt(rho)W,
```

and again `c(P)=W-n(P)>=(1-sqrt(rho))W`. No support-size or unweighted
premise is used.

## Whole-shadow identities

Expanding `Xi_A=sum_(P in A)lambda_P T(P)` and interchanging finite sums
over pivots and unordered pairs gives exactly

```text
Xi_A=sum_({Q,R} subset V)lambda_Q lambda_R lambda(Sh(Q,R)).
```

The shadow condition retains both parent edges and genuinely regenerated
triple-empty pairs; replacing the child by an induced graph would invalidate
this identity. Since `rho'_P=2T(P)/c(P)^2`,

```text
sum_(P in A)lambda_P c(P)^2 rho'_P=2Xi_A.
```

For `rho>0`, `A` is nonempty and
`Z_A=sum_A lambda_Pc(P)^2>0`; division gives the claimed weighted
min/average/max inequality.

At `rho=0`, `A` is empty and both summed identities remain valid as
`0=0`, but `2Xi_A/Z_A` is `0/0` and the min/max sets are empty.
M337's displayed normalized average (3.3) therefore needs the explicit
domain `rho>0`. This is nonmaterial because the candidate separately
declares `rho=0` terminal and never chooses a pivot there.

## Conditional stopping and weight

Assume the universal anchor/start clause and W-RATSD+HLDT clauses with their
intended positive polynomial exponents and nonnegative loss constants. Write
`delta=d^(-B_rel)`. The weighted simple incompatibility graph gives
`0<=rho<=1`. Every high-density nonterminal step has
`rho_(t+1)<=(1-delta)rho_t`.

After
`N=ceil(B_low d^B_rel log d)` such steps,

```text
rho_N <=(1-delta)^N rho_0
       <exp(-delta N)<=d^(-B_low).
```

Hence a terminal alternative has occurred earlier or the strict low-density
clause supplies the final pivot. Equality at the threshold causes no gap
because the strict exponential inequality yields strict entry below it.

On nonterminal steps,

```text
sum_t log(W_t/W_(t+1))
 <=C_log log(d) sum_t(rho_t-rho_(t+1))
 <=C_log log d.
```

The initial anchor costs at most `C_init log d`. Every terminal pivot,
whether reached from the high- or low-density alternative, separately costs
at most `C_fin log d`. If the current node already has `rho=0`, it is
terminal and no final pivot loss is charged. Therefore

```text
W_final>=||lambda||_1/d^(C_init+C_log+C_fin).
```

All child vertices retain positive weights, so `T(P)=0` means the final
whole-child incompatibility graph is genuinely edgeless. Tuple length is at
most `d^B_init+N+1`, hence polynomial after enlarging one universal
exponent.

This is only a conditional stopping/weight theorem. The universal anchor is
an explicit unproved start hypothesis. AHTSS and AHLDT are exactly the two
unresolved actual higher-orbital selection inputs. No HPRN, WRAD, or
downstream conclusion is promoted.
