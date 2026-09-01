# M36 report: an exact Lorentzian ideal chain for parking multisets

Date: 2026-08-11.  Repository base commit:
`502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.

This is a nonterminal scoped theorem.  It supplies the comparison source for
GENERAL PARKING-MULTISET FLOW; it does not compare that source to the actual
heat-bath projection and does not prove Terminal A or Terminal B.

## 1. Exact claim

Fix `r>=1` and put `n=r+1`.  A sorted parking-label multiset is represented
by its multiplicity vector

```text
m=(m_0,...,m_(r-1)) in N^r.
```

Its feasible set is

```text
J_r={m: sum_i m_i=r and sum_(i=0)^k m_i>=k+1
         for every 0<=k<=r-1}.                         (1.1)
```

The exact stationary mass induced by a uniform minimal transposition
factorization of the long cycle is

```text
pi_r(m)= [r!/n^(n-2)] product_i 1/m_i!.                (1.2)
```

There is a reversible Markov chain `D_r` on `J_r` with the following exact
description.  From `m`, choose a source type `i` with probability `m_i/r`,
put `eta=m-e_i`, let

```text
A(eta)={j:eta+e_j in J_r},
```

and choose `j` uniformly from `A(eta)`.  Set
`m'=eta+e_j`.  Then

```text
gap(D_r)>=1/r,                                         (1.3)
D_r(m,m')>=1/r^2 whenever m'!=m and D_r(m,m')>0.       (1.4)
```

Membership and one step can be implemented in time polynomial in `r`
(`O(r^2)` by direct prefix tests, or `O(r)` with maintained prefix slack).

## 2. The prefix-feasible set is M-convex

For `x,y in J_r`, write

```text
X_k=sum_(t=0)^k x_t,  Y_k=sum_(t=0)^k y_t,
X_(-1)=Y_(-1)=0.
```

Fix `i` with `x_i>y_i`, and put `delta=x-y`.  Let

```text
a=max({k<i:Y_k=k+1} union {-1}),
b=min{k>=i:X_k=k+1}.
```

The index `b` exists because `X_(r-1)=r`.  At `a`, either `a=-1` or
`y` is tight, so `X_a-Y_a>=0`.  At `b`, `x` is tight, so
`X_b-Y_b<=0`.  Therefore

```text
sum_(t=a+1)^b delta_t=(X_b-Y_b)-(X_a-Y_a)<=0.          (2.1)
```

Since `delta_i>0`, (2.1) gives an index `j!=i` with
`a<j<=b` and `delta_j<0`.

If `j<i`, every `y` prefix from `j` through `i-1` has at least one unit
of slack, by the definition of `a`.  Thus moving one unit of `y` from
`j` to `i` preserves (1.1), while moving one unit of `x` from `i` to the
earlier index `j` can only increase the affected prefixes.  Hence

```text
x-e_i+e_j in J_r,   y+e_i-e_j in J_r.
```

If `j>i`, every `x` prefix from `i` through `j-1` has at least one unit
of slack, by the definition of `b`.  Moving one unit of `x` right from
`i` to `j` is therefore feasible, and the reverse move in `y` only
increases the affected prefixes.  The same displayed symmetric exchange
again holds.  This proves the symmetric exchange axiom, so `J_r` is
M-convex.

## 3. Lorentzian polynomial and polarization

Define the normalized support polynomial

```text
f_r(z)=sum_(m in J_r) z^m/m!,  m!=product_i m_i!.     (3.1)
```

Branden--Huh, *Lorentzian polynomials*, Annals of Mathematics 192
(2020), Theorem 3.10, says exactly that the normalized generating
polynomial of an M-convex set is Lorentzian.  Thus (3.1) is Lorentzian and,
equivalently here, completely/strongly log-concave.

Polarize each of the `r` variables into `r` clones.  If `Pi f_r` denotes
this multiaffine degree-`r` polarization, Branden--Huh Proposition 3.1
preserves the Lorentzian property.  A clone subset `S` with occupancy
vector `m` has coefficient

```text
w(S)=product_i [(r-m_i)!/r!].                          (3.2)
```

Indeed, polarization replaces `z_i^(m_i)` by
`binom(r,m_i)^(-1)e_(m_i)` and

```text
(1/m_i!)/binom(r,m_i)=(r-m_i)!/r!.
```

There are `product_i binom(r,m_i)` clone subsets above `m`.  Summing (3.2)
over that fiber gives `1/m!`, so the occupancy projection of the polarized
law is exactly (1.2), not merely a comparable measure.

## 4. Down-up gap and exact projected kernel

Run the standard degree-`r` down-up walk on clone subsets: delete one of
the `r` selected clones uniformly, then add an available clone with
probability proportional to the resulting coefficient (3.2).
Anari--Liu--Oveis Gharan--Vinzant, *Log-Concave Polynomials II*,
Theorem 1.1 (arXiv:1811.01816; Annals of Mathematics 199 (2024)), gives

```text
gap(P_clone)>=1/r                                     (4.1)
```

for this multiaffine strongly log-concave law.

The stationary-flow projection by clone occupancy has gap no smaller than
(4.1): for every macro function, its lift has exactly the same variance and
Dirichlet form.  It remains to identify that projection.

Suppose the deleted clone has type `i`, and let `eta=m-e_i`.  For a
feasible destination type `j`, there are `r-eta_j` available clones.  The
total coefficient of all resulting subsets of type `j` is

```text
(r-eta_j) [(r-eta_j-1)!/r!]
  product_(k!=j)[(r-eta_k)!/r!]
=product_k[(r-eta_k)!/r!],                            (4.2)
```

which is independent of `j`.  Thus the destination type is exactly uniform
on `A(eta)`, proving the description of `D_r`.  The source type has
probability `m_i/r`; since `m_i>=1` when selected and
`1<=|A(eta)|<=r`, every positive off-diagonal transition is at least
`1/r^2`.  Equations (1.3)--(1.4) follow.

## 5. Probability, runtime, path, and congestion accounting

- Stationary normalization is exact: a macro has `r!/m!` ordered parking
  words and there are `n^(n-2)` minimal long-cycle factorizations.
- The ideal step retains its deletion probability `m_i/r` and uniform
  feasible-destination probability `1/|A(eta)|`; no hidden clone factor
  remains after (4.2).
- The ideal chain has path length one per unit exchange and minimum positive
  probability `r^-2`.
- Direct implementation scans at most `r` destinations and checks at most
  `r` prefix inequalities per destination, hence costs `O(r^2)` without
  preprocessing.
- No congestion comparison to the actual projected rank-two heat bath is
  claimed.  That missing flow is precisely M35.

## 6. Dependencies

1. **Proved here:** the symmetric-exchange proof for `J_r`, the exact
   polarized fiber weights, the projected transition formula, the runtime,
   and the `r^-2` positive-rate floor.
2. **Cited with checked hypotheses:** Branden--Huh Theorem 3.10 and
   Proposition 3.1.  The polynomial is homogeneous, nonnegative, and its
   support is the proved M-convex set.
3. **Cited with checked hypotheses:** Anari--Liu--Oveis Gharan--Vinzant
   Theorem 1.1.  The polarized polynomial is multiaffine, homogeneous of
   degree `r`, and strongly log-concave, so its down-up gap is at least
   `1/r`.
4. **Inherited proved:** Stanley's bijection identifies uniform minimal
   long-cycle factorizations with uniform parking functions and gives the
   orbit mass (1.2).
5. **Open:** comparison of `D_r` to the actual stationary-flow parking
   projection.

Primary-source identifiers:

- Petter Branden and June Huh, DOI `10.4007/annals.2020.192.3.4`.
- Nima Anari, Kuikui Liu, Shayan Oveis Gharan, and Cynthia Vinzant,
  DOI `10.4007/annals.2024.199.1.4`, arXiv `1811.01816`.

## 7. First unproved standalone proposition

> **LORENTZIAN-TO-HEAT-BATH PARKING FLOW.**  Every transition of `D_r`
> can be fractionally routed through the stationary-flow projection of the
> actual adjacent rank-two heat bath on minimal long-cycle factorizations,
> with path length and edge congestion bounded by `r^C` for a universal
> constant `C`.

Together with the fixed-multiset restriction theorem in M27 and JSTV, this
would prove an inverse-polynomial gap for the complete minimal long-cycle
sector.  It would still leave other endpoints/surpluses in the base bridge
theorem.

## 8. Strongest self-attack and calibration

The actual projected heat bath can give a feasible unit exchange
exponentially small direct probability: M27/M32 prove the balanced binary
rate `2/[3(r-1)binom(r,a)]`.  Therefore (1.4) cannot be transferred by
edgewise domination.  M27's two-hop bypass proves only one structured
family and gives no global congestion bound.  This is a genuine remaining
obligation, not a normalization issue.

At `r=1`, `J_r={(1)}` and all chains are singletons.  At `r=2`, the two
macros `(2,0),(1,1)` have unnormalized weights `1/2,1`, hence masses
`1/3,2/3`, agreeing with the three minimal factorizations of a 3-cycle.
Both are included by the proof.  The identity-chain cases `m=0,2,4`, odd
raw length, `N=2`, and the 27/120/3936 calibrations are not instances of
this minimal nonidentity sector and are not used to infer a global theorem.
The paired-bridge application keeps the required even raw factor length.

No computation was used.

## 9. Verdict

PROVED

This verdict is scoped to the ideal parking-macro chain (1.1)--(1.4).
The global goal remains OPEN AT LORENTZIAN-TO-HEAT-BATH PARKING FLOW and,
beyond the minimal long-cycle stratum, PRODUCT-INCREMENT BASE CORRELATION.

