# M231 symbolic quotient invariance

## Exact factorization of the declared word map

Let `D_B` denote the full frozen contour descriptor and extract

```text
q(D_B)=(v,lambda,alpha,epsilon).
```

The displayed Candidate-B word contains the descriptor only in two places:

1. `lambda OR alpha` selects identity versus carrier;
2. `(v,epsilon)` determines every generator index and sign in `Q`, hence in
   `Q B_d Q^-1`.

Therefore there is an explicit map `f_1` such that

```text
W_B = f_1 o q,
```

which proves word homogeneity of `Z_1` without finite enumeration.

Now define

```text
r(v,lambda,alpha,epsilon)=
  ("closed",)        if lambda OR alpha,
  ("open",v,epsilon) otherwise.
```

There is likewise an explicit map `f_2` with

```text
W_B = f_2 o r o q.
```

This proves word homogeneity of the route-normal quotient `Z_2`. No path or
off-path statistic can change the literal assigned word while `Z_2` is fixed.

## Why this is not yet an all-rank closure lemma

The factorization is a theorem about the *declared formula*. It does not prove
that two arbitrary trees with equal `Z_2` require the same correction at
higher rank. That needs a separate DPS statement establishing

```text
kappa=1  => N=A,
kappa=0  => Q(v,epsilon) B_d Q(v,epsilon)^-1 N=A
```

uniformly in `d`. M231 tests exactly these implications on the complete
finite rank-six template and nothing larger.

## Word-count reconciliation

At `d=6`, the four odd edits can contribute identity plus literal carrier
words indexed by the occurring open pairs `(v,epsilon)`. Internal even edits
reuse identity, while edits 8 and 9 contribute two fixed boundary words. The
finite checker will count the occurring image; no word is searched for or
learned from an endpoint.
