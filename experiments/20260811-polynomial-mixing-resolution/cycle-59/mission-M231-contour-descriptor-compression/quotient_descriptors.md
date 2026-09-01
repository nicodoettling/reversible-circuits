# M231 predeclared quotient descriptors

Date: 2026-08-13 UTC. **SOURCE-ORDER ASSERTION:** this file is fixed before
any M231 endpoint is constructed or inspected. Exactly two nested quotients
are permitted; no third quotient or post-failure refinement is allowed.

## Common symbolic data

For an ordinary odd edit `i=2v-3` at old rank `d`, write the stopped path

```text
P(v)=(v,p(v),...,1).
```

Let

```text
lambda = 1 iff an internal vertex of P(v) is greater than v,
alpha  = 1 iff two consecutive internal entries of P(v) ascend,
kappa  = lambda OR alpha.
```

For `L=d-v-1`, let `c_t=1` iff `v+t+1` is a direct child of `v`, and define
the sign vector `epsilon=A(c)` by

```text
epsilon_0 = -1 if c_0=1, else +1,
epsilon_t = -1 if c_t=1, else -epsilon_(t-1).
```

The frozen Candidate-B formula is

```text
W_B(T,v) = identity                            if kappa=1,
             Q(v,epsilon) B_d Q(v,epsilon)^-1  if kappa=0,

Q(v,epsilon)=product_(t=0)^(L-1)
  R_(2(v+t)-2)^epsilon_t R_(2(v+t)-1)^epsilon_t.
```

The forward-exception flag, the full path beyond `lambda/alpha`, and the
off-path child lists do not occur in this literal word expression.

## Quotient 1: readable symbolic quotient

Define

```text
Z_1(T,v)=(v,lambda,alpha,epsilon).              (Q1)
```

This retains the two logically distinct closure reasons but discards the
forward flag, full path, and all off-path lists. Its assigned word is the
displayed `W_B` with `kappa=lambda OR alpha`.

Before seeing the table, the number of possible `Z_1` values at fixed `v` is
at most `4*2^L`: respectively 32, 16, 8, and 4 for `v=2,3,4,5`, all
substantially below 101.

## Quotient 2: route-normal quotient

Coarsen `Z_1` once more:

```text
Z_2(T,v) = ("closed",)             if kappa=1,
           ("open",v,epsilon)      if kappa=0.        (Q2)
```

The assigned word is identity in the closed class and the displayed
`Q B_d Q^-1` in an open class. At fixed `v`, there are at most `1+2^L`
classes: 9, 5, 3, and 2. Globally across the four odd edits there are at most
16 classes before checking which sign vectors occur.

This quotient is “route normal” only in the literal-formula sense: it is
derived without inspecting endpoints or discovered routes. Different open
keys must be retained because `v` fixes generator locations and `epsilon`
fixes generator signs.

## Decision rule

For each quotient, first verify algebraic word homogeneity classwise, then
literal endpoint correctness on all 500 odd rows. If either property fails,
archive the first lexicographic same-quotient different-word or pass/failure
pair. Otherwise promote the strongest exact finite compression.

For reconciliation only, the five non-odd edit families use identity plus two
fixed nonidentity boundary words. Thus the previously reported 14 full-table
words may consist of the odd-word image together with those two boundary
words; the exact count is deferred to computation.

Success proves only the complete finite `d=6 -> 7` table. It proves no
all-rank sufficiency of `kappa` or `epsilon`, no every-color routing, no
voltage-corrected/total length statement, no gap/mixing result, and no
Terminal claim.
