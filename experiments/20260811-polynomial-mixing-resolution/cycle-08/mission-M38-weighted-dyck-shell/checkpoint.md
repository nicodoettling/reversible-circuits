# M38 halfway checkpoint — exact recurrence obtained, shell inequality open

## Stable result: support Möbius inversion plus cut/join transfer

Fix `N>=3`, `m=2N-2`, and a Dyck sign path `P` of length `m`.  Let
`W_N(P)` be the number of connected full-support identity transposition words
with prefix-rank path `P`.  The following is now proved directly.

For a set partition `rho` of `[N]`, let `A_rho(P)` count the identity words
with sign path `P` all of whose factors have both endpoints in one block of
`rho`.  If `E_sigma(P)` counts words whose exact support-component partition
(including isolated labels) is `sigma`, then

```text
A_rho(P)=sum_(sigma<=rho) E_sigma(P).
```

Partition-lattice Möbius inversion at the one-block top partition gives

```text
W_N(P)=sum_(rho partition [N])
       (-1)^(|rho|-1)(|rho|-1)! A_rho(P).             (C.1)
```

Group `rho` by its integer block-size partition
`lambda=(lambda_1,...,lambda_k) |- N`.  The exact labeled multiplicity is

```text
b(lambda)=N!/[prod_i lambda_i! prod_d m_d(lambda)!].  (C.2)
```

For one fixed `rho`, `A_rho(P)` has a finite transfer recurrence on tuples of
cycle types of the Young subgroup `S_(lambda_1) x ... x S_(lambda_k)`.  For a
partition `alpha |- d` and a fixed permutation `s_alpha` of that type, put

```text
c_d(alpha,beta)=#{t in T_d:type(s_alpha t)=beta}.
```

This is well-defined by conjugacy.  It has the usual exact cut/join values:

- joining unequal cycle lengths `i,j`: `m_i m_j i j`;
- joining equal lengths `i`: `binom(m_i,2)i^2`;
- cutting a `k`-cycle into unequal lengths `i,k-i`: `m_k k`;
- cutting into equal halves: `m_k k/2`.

For a tuple of types `bold alpha`, set
`r(bold alpha)=sum_i(lambda_i-ell(alpha_i))`.  Starting with unit mass at the
all-identity tuple, the recurrence replaces one coordinate according to `c`,
retaining only rank increment `+1` or `-1` prescribed by the next symbol of
`P`.  The mass at the all-identity tuple after `m` steps is `A_lambda(P)`.
Combining with (C.1)--(C.2) is an exact formula for every `W_N(P)`.

The same recurrence tracks area: after transition to `bold beta`, increase
the area index by `r(bold beta)`, and sum over both cut/join signs.  Thus, with
`D_j^lambda(bold alpha,a)` denoting the exact count after `j` factors,

```text
D_(j+1)^lambda(bold beta,a+r(bold beta))
 +=D_j^lambda(bold alpha,a) C_lambda(bold alpha,bold beta),
```

and the connected area coefficient is the signed sum (C.1) at the identity
endpoint.  This recurrence is universal; the bounded implementation is only
a validator and diagnostic.

## Exact validation and named falsification

The deterministic implementation
`weighted_dyck_recurrence.py` uses exact integers.  It reproduces:

- `N=3`: path weights `6,18` and area weights `{2:6,4:18}`;
- every one of the five inherited `N=4` path weights and area weights
  `{3:96,5:528,7:720,9:1536}`;
- every one of the fourteen inherited `N=5` path weights and the nonunimodal
  area table
  `{4:3000,6:23400,8:60600,10:132840,12:207600,14:205560,16:375000}`.

For every `3<=N<=13`, the sum of coefficients is exactly
`(2N-2)! N^(N-3)`, and the top coefficient is exactly
`(N-1)! N^(2N-4)`.  The bottom coefficient also has the direct formula

```text
W_N((UD)^(N-1))=(N-1)! N^(N-2)=N!N^(N-3):           (C.3)
```

at every return to identity the two factors must be the same transposition,
and connectedness says that the `N-1` distinct paired edges are an ordered
labeled spanning tree.

The finite computation can falsify the universal *existence* of a threshold
whose conditional CDF is in `[1/4,1/2]`: a single `N` with no such layer would
do so.  No failure occurs through `N=13`.  Taking the first admissible layer,
the exact diagnostics are:

```text
N   q    CDF          layer/CDF
3    2   0.250000     1.000000
4    7   0.466667     0.535714
5   12   0.424048     0.485682
6   17   0.259597     0.468939
7   26   0.301992     0.331111
8   35   0.262017     0.278382
9   46   0.254324     0.243256
10  59   0.259755     0.206486
11  74   0.274404     0.177200
12  89   0.250343     0.162941
13 108   0.278470     0.139193
```

These values are consistent with a ratio of order `1/N`, but this is exact
finite evidence, not an asymptotic theorem.  Complete fixed-path enumeration
through `N=8` also confirms the inherited cover monotonicity.  The smallest
cover ratio is the near-mountain-to-mountain ratio and decreases from `3` at
`N=3` to about `1.485` at `N=8`, so a proof cannot assume a cover expansion
factor bounded substantially above one.

## Current analytic frontier

M34 gives an injection for each specified Dyck cover, hence fixed-path weight
monotonicity.  It does not give a global injection between adjacent area
layers because images from different valley positions overlap.  Indeed, even
at the path level both `UDUUDD` and `UUDDUD` raise at their leftmost valley to
`UUDUDD`.  Invoking unweighted rank-unimodality would be invalid: that is a
known open Dyck-lattice problem, and weighted monotonicity alone does not
control the number of paths in an area layer.

The exact first unproved implication is now:

> **LOWER-HALF COEFFICIENT BOUND.**  If `H_N(a)` is the connected coefficient
> furnished by (C.1) and the cut/join recurrence, prove that there is a
> feasible `q_N` with `1/4<=sum_(a<=q_N)H_N(a)/|F_N|<=1/2` and
> `H_N(q_N)>=N^(-C)sum_(a<=q_N)H_N(a)` for a universal `C`.

I will next attack this directly from the transfer recurrence and from
weighted valley-edge double counting.  If it remains open, the final report
will freeze the recurrence as a reusable theorem and isolate exactly why it
does not yet give the required asymptotic shell mass.
