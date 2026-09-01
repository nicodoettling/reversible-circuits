# M147 checkpoint

Date: 2026-08-13 UTC.

## Initialization and reconciliation

The required project skill, `HANDOFF.md`, `GOAL_SPEC.md`, the sampling and
experiment references, and the accepted M109/M114, M115/M116, M117/M121,
M140/M144 artifacts have been read.  The repository-level instruction names
`references/experiments.md`, while the actual required file is located at
`.codex/skills/reversible-circuit-sampler/references/experiments.md`; that
path discrepancy is recorded rather than silently ignored.

The default filesystem sandbox intermittently fails during `bwrap` loopback
setup with `RTM_NEWADDR: Operation not permitted`.  Scoped approved reads are
being used; no package or machine configuration is changed.

## Exact starting point

For a reachable context `x=(s,K,R,B)`, suffix excess `L=s-B`, attachment
offset `a`, deficit `D=K-R`, and `z=1/(K+1)`, the accepted transformed
recurrence retains every `j=1,...,k`:

```text
H(x)=A_0(x)+sum_(k,t>B) rho_s(k,t)
                  sum_(j=1)^k nu_(K,R,k)(j) H(y_j),
y_j=(t-1,K+k,R+j,B).
```

Both suffix excess and the accepted phase strictly decrease.  A deep child
has suffix excess `t-B-1`, deficit `D+k-j`, and attachment offset increased
by `k`.  Thus a universal envelope must be defined on arbitrary-deficit
children, not only on right-heavy seeds.

The corrected reset decomposition is

```text
A_0/q <= q[C_s-sum_E a_E lambda_E]
          +sum_E theta_E^2/(q c_E),
c_E=degree(E)rho(E), b_E=c_E lambda_E, 0<=a_E<=b_E.
```

M140/M144 prove `C_s<3/4` for `s>=100`; the rejected M131
`a_E lambda_E^2` display is excluded.

## Decisive result

The second route is complete.  Writing `kappa=K+1` and `D=K-R`, the exact
attachment law is

```text
nu_(kappa,D,d)(j)
 =binom(d,j)(D)^(rise)_(d-j)(kappa-D)^(rise)_j
   /(kappa)^(rise)_d,
```

and a child updates `(kappa,D)` to `(kappa+d,D+d-j)`.  This gives a closed
all-suffix functional recurrence `F_(B,L)(kappa,D)` with corrected one-power
reset subtraction.  It does not collapse to a right-heavy scalar recurrence.

At the exact `L=1` boundary `(s,B)=(3,2)`,

```text
H(3,K,K-D,2)/q
 =1/16+[2D/(K+1)-3/8]^2/4,  q=3/8.
```

For fixed `K=32`, the right-heavy state `D=1` has

```text
H=24313/743424<15/64,
```

while the same scalar data with `R=1,D=31` has

```text
H=175033/743424>15/64,
margin=793/743424.
```

More generally, the `R=1` family equals the local budget at `K=31` and
strictly exceeds it for every `K>=32`.  Both states have identical `L,B,s,q`,
`C_3=9/32`, all Cayley ratios, `K`, and `z`; only `D` differs.  The bad state
is a positive-probability `j=1` child of the fresh right-heavy seed
`(K+2,1,0,2)`, through degree `K-1`, last part four.  Hence the family is in
the actual accepted reachable closure.

The first necessary extra statistic is `D`, equivalently
`p=D/(K+1)`.  The pair `(kappa,D)` closes the exact attachment recursion.
A fixed truncation to `r` deficit moments is not exact at unbounded suffix:
two explicit binomial-parity measures agree on every degree-`<=r` polynomial
but differ on the rising factorial of degree `r+1` queried by attachment.

The obstruction is deliberately scoped.  It refutes an exact or pointwise
budget-preserving deficit-blind Bellman closure; it does not refute a future
nonlocal amortization that lets selected children exceed their local budget.

## Exact audit

`all_suffix_exact.py` is standalone and uses exact `Fraction` arithmetic.  A
capped deterministic run verifies 270 attachment normalizations, eight
suffix-recursion identities (including three minimal `B=1`, or `L+1=s`,
boundaries), eleven boundary rows through `K=4096`, the exact `C_3`, three
reachability witnesses, and nine moment-pair identities.  It reports zero
failures.  The first run exposed only an implementation issue from evaluating
the algebraic Cayley formula with exponent `-1`; rewriting the identical
quantity as `p n^(n-p)/[n(n-p)!]` restored exact rational construction before
any result was retained.

No explicit `L=6` support or basin enumeration was performed; that remains
M145's assignment.
