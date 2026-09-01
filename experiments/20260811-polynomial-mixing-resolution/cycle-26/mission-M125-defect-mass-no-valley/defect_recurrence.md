# M125 exact defect-mass coefficient reduction

Date: 2026-08-13 UTC.

## 1. Target, convention, and scope

For `d>=2`, this note concerns the auxiliary stationary law

```text
rho(kappa)=|C_kappa|/Z_inc
```

of M113/M118's connected-unicycle incidence chain `A_d`.  A realizable key is
`kappa=(j,p,Q_L,Q_R)`, and its cycle defect is

```text
R(kappa)=d-c(p) in {0,...,d-2}.
```

Define the unnormalized defect masses

```text
M[d,r]=sum_{R(kappa)=r}|C_kappa|.
```

Permutations compose as `(pq)(x)=p(q(x))`, and tuple factors multiply
left-to-right.  The target here is `rho`, not the original uniform identity-
word law and not M113's lifted law `bar_pi`.  The only imported enumerative
input is the M113 cell formula, accepted independently by M118:

```text
|C_kappa|=j!(2d-j)!
  product_{B in Q_L union Q_R}|B|^(c_B-3)
  product_{a cycle of p}[a^a/(a-1)!]^2.               (1.1)
```

Everything below is an exact reduction of `M[d,r]`.  It proves neither a
universal no-valley statement nor a spectral gap.

## 2. Indexed cycle atoms and one-colour partitions

Fix a permutation cycle type `lambda=(a_1,...,a_c)` of `d`, and temporarily
index the actual cycles, even when some lengths agree.  For nonempty
`S subseteq [c]`, write

```text
A(S)=sum_{i in S}a_i,
w(S)=A(S)^(|S|-3).                                    (2.1)
```

A coarsening `Q` of the cycle partition is exactly a set partition `pi` of
the indexed atoms.  Its block factor in (1.1) is

```text
product_{B in pi}w(B).
```

Let

```text
P_S(y)=sum_{pi partition of S} y^|pi| product_{B in pi}w(B),
P_empty(y)=1.                                         (2.2)
```

**PROVED, rooted block recurrence.**  If `o` is any fixed atom of nonempty
`S`, then

```text
P_S(y)=y sum_{B subseteq S, o in B} w(B)P_{S-B}(y).   (2.3)
```

Indeed, the block containing `o` is unique; removing it leaves an arbitrary
partition of `S-B`.  This is a disjoint and weight-preserving decomposition.

## 3. Connected pairs and the unicycle diagonal

Put

```text
A_S(y,z)=P_S(y)P_S(z).                                (3.1)
```

Thus `A_S` enumerates ordered pairs `(pi_L,pi_R)` of coloured partitions.
Let `C_S(y,z)` enumerate only pairs whose join `pi_L join pi_R` is the
indiscrete partition of `S`, with the same product weight.  Every arbitrary
pair decomposes uniquely over the connected components of its join.  Choosing
the component containing a fixed root `o` gives

```text
A_S(y,z)=sum_{U subseteq S, o in U} C_U(y,z)A_{S-U}(y,z),
C_S=A_S-sum_{proper U subset S, o in U}C_U A_{S-U}.    (3.2)
```

**PROVED, incidence interpretation.**  A pair with `L=|pi_L|` and
`R=|pi_R|` gives a bipartite multigraph with `L+R` partition-block vertices
and one labelled edge for each of the `c` cycle atoms.  Its underlying graph
is connected exactly when the join is indiscrete.  Conditional on
connectedness, it is unicyclic exactly when

```text
L+R=c.                                                (3.3)
```

There are no isolated block vertices because every block contains an atom.
Consequently `[y^L z^(c-L)]C_[c]` is exactly the incidence-weight sum required
by (1.1), with no hidden key or word multiplicity.

## 4. Exact cycle-type coefficient theorem

For `a>=1`, abbreviate

```text
h(a)=a^a/(a-1)!.
```

If the integer partition `lambda` has `m_s` parts equal to `s`, then the
number of permutations of this type is

```text
n(lambda)=d!/product_s(s^m_s m_s!).                   (4.1)
```

**PROVED, exact type contribution.**  For every `d>=2`, `2<=c<=d`, and
`r=d-c`, the contribution of `lambda` to `M[d,r]` is

```text
n(lambda) product_i h(a_i)^2
  * sum_{L=1}^{c-1}
      (d+c-2L)!(d-c+2L)!
      [y^L z^(c-L)]C_[c](y,z).                        (4.2)
```

Proof.  Equations (2.1)--(3.3) enumerate exactly the two coarsenings and their
block factors.  For a term with `L+R=c`, M113 realizability gives

```text
j=d+R-L=d+c-2L,
2d-j=d-c+2L.                                          (4.3)
```

These are the two factorials in (1.1).  The atom factor in (1.1) is
`product_i h(a_i)^2`, independent of the coarsenings, and (4.1) restores the
choice of the permutation.  Summing (4.2) over all integer partitions of `d`
with `c=d-r` proves the formula.

All displayed quantities can be rational before summation because negative
exponents occur in (2.1).  Their final sum is an integer because (4.2) is a
partition of the actual integer cell count (1.1); the executable also checks
integrality exactly.

## 5. Exact multiset aggregation

The subset recurrence is already finite, but equal cycle lengths cause many
identical subset states.  Let the distinct atom sizes be `s_1,...,s_k`, let
`nu=(nu_1,...,nu_k)` be their multiplicities, and distinguish one root atom
of a type `q` with `nu_q>0`.  For a submultiset `b<=nu` containing that root,
the number of indexed subsets of type `b` is

```text
N_nu(b)=binom(nu_q-1,b_q-1)
        product_{i != q}binom(nu_i,b_i).               (5.1)
```

Grouping (2.3) and (3.2) by `b` gives, exactly,

```text
P_nu(y)=y sum_{b contains root}N_nu(b)w(b)P_{nu-b}(y),
A_nu=sum_{b contains root}N_nu(b)C_b A_{nu-b}.         (5.2)
```

The full-set term in the second identity is `C_nu`; moving the proper terms
to the other side gives the connected recurrence.  This proves the multiset
engine used by `defect_species.py`; it is not a heuristic symmetry quotient.
It reduces the state table for a type from all indexed subsets to the
submultisets `product_i(nu_i+1)`.  The separate audit compares this engine
both with the original subset recurrence and with direct pairs of set
partitions.

Colour exchange gives the exact symmetry

```text
[y^L z^R]C_[c]=[y^R z^L]C_[c],                        (5.3)
```

and the two cut factorials in (4.2) exchange as well.

## 6. Boundary cases and the repaired bug

- `c=1` contributes nothing: a key has at least one left and one right block,
  while (3.3) would require `L+R=1`.  The preserved core mistakenly sent this
  impossible type to defect slot `d-1`; the wrapper hid the resulting boundary
  error.  The core now excludes `c<2` directly.
- At `d=2`, only `lambda=(1,1)` occurs.  It has `L=R=1` and gives the one-state
  row `M[2,*]=[1]`.
- For `d>=3`, the defect range is exactly `0<=r<=d-2`, as in M120/M124.
- Both side lengths in (4.3) are positive for `1<=L<=c-1`.

## 7. Exact ULC obstruction

The primitive `d=4` row is

```text
(M[4,0],M[4,1],M[4,2]) proportional to (627,1520,1113).
```

For a three-term sequence, ultra-log-concavity after division by the binomial
row `(1,2,1)` requires

```text
1520^2 >= 4*627*1113.
```

This is **REFUTED** exactly:

```text
1520^2-4*627*1113 = -481004 < 0.                     (7.1)
```

Ordinary log-concavity survives this case, with exact primitive margin

```text
1520^2-627*1113 = 1612549 > 0.                        (7.2)
```

For the quadratic defect polynomial, (7.1) is also its negative
discriminant, so real-rootedness is already impossible at `d=4`.  Thus
real-rooted/ULC machinery cannot prove the desired ordinary statement for
these exact masses.

## 8. First unresolved coefficient inequality

Let `H[d,c]` denote the sum of (4.2) over all integer partitions of `d` with
exactly `c` parts.  Then

```text
M[d,r]=H[d,d-r].                                      (8.1)
```

The first standalone stronger target is the completely explicit coefficient
inequality

```text
H[d,c]^2 >= H[d,c-1]H[d,c+1]
for d>=4 and 3<=c<=d-1.                              (8.2)
```

**UNRESOLVED.**  Equations (2.3), (3.2), and (4.2) reduce (8.2) to integer
partitions and rooted submultisets, with no permutations, keys, or words left
to classify.  But (3.2) is subtractive, and no positivity-preserving theorem
for (8.2) is known here.  Exact finite verification cannot replace such a
theorem.

Inequality (8.2) would imply ordinary log-concavity of every defect row and
hence M120's DEFECT NO-VALLEY lemma.  Conversely, no-valley is weaker than
(8.2), so failure of (8.2) would not by itself refute no-valley.  Even a proof
of no-valley would yield only M120's conditional defect-projection gap; the
fixed-defect two-step gap, `gap(A_d)`, the M113 handle projection, and the
original lazy `{3,4,5}` heat-bath gap would all remain open.
