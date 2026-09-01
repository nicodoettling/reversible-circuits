# Fresh referee report on M48

Date: 2026-08-11.  Referee lane: M46.  This is an independent audit of the
frozen M48 auxiliary theorem, not a terminal review of the global goal.

Frozen inputs:

```text
M48 report.md
  a609ecb60f6806d34894b7927d9bb27fdbe3949e59f9e30039e1bf974ce8d40e
M48 separator_theorem.md
  032e154ca4de74980b793d74f9970640707e9955a24a78d4b03c12e5147c89d0
```

## Verdict

**ACCEPT.**

Numbered objections: **none**.

The accepted statement is scoped exactly as follows.  For the weighted
leaf-rotation subchain `L_r`, `r>=3`, put

```text
n=r-1,
D_r=2+ceil(log_2 n),
b_r=(r+1)(e/D_r)^D_r.
```

Then, whenever the denominator factors are positive,

```text
gap(L_r)
 <=b_r/[(e^(-1)-b_r)(3/(8e^2)-b_r)],
```

so `r^C gap(L_r)->0` for every fixed `C>0`.  Consequently no universal
polynomial-congestion comparison from the M41 chain `Y_r` to `L_r` exists.
This is auxiliary and is not Terminal B for the original chain `K`.

## Referee checks

1. **Root-prefix projection.**  If the root branch sizes are
   `(a_1,...,a_k)`, their proper prefix set has `k-1` elements.  Internal
   M35 rotations preserve it.  A root rotation `(1,q)<->(q+1)` toggles
   `s+1` with predecessor `s=0` or `s` already present.  Thus every `L_r`
   edge maps *into* the reversible-pebble graph.  M48 correctly avoids the
   false surjectivity claim: an inverse tree split additionally needs a
   unary branch root.

2. **Pebbling off-by-one.**  Below degree `D_r`, the root degree is at most
   `D_r-1`, hence there are at most `p=D_r-2=ceil(log_2 n)` pebbles.  A path
   from `empty` to `{n}` would be a persistent reversible pebbling of the
   directed path on exactly `n` vertices.  Komarath--Sarma--Sawlani's
   theorem gives one plus the edge-ranking number; a `k`-color ranking has
   at most `2^k-1` edges, and median recursion is sharp.  The required space
   is `ceil(log_2 n)+1`, so the two configurations are disconnected at cap
   `p`.

3. **Boundary containment.**  For
   `A_r={Delta<D_r:S in C_0}`, a low-degree `L_r` neighbor remains in the
   same capped-pebble component.  Therefore every edge leaving `A_r` has
   its other endpoint in `B_r={Delta>=D_r}`.  This uses only the graph
   homomorphism in check 1, not surjectivity.

4. **Stationary reservoirs.**  Root-degree-one trees have exact mass
   `Z_(r-1)/Z_r=(r/(r+1))^(r-1)>=e^-1`.  Ordered root composition
   `(r-1,1)` has exact mass
   `(1/2)Z_(r-2)/Z_r=r(r-1)^(r-2)/[2(r+1)^(r-1)]>=3/(8e^2)` and prefix
   `{n}`.  Removing `B_r` gives the claimed lower bounds on both sides.

5. **Separator mass.**  The cycle lemma maps `pi_r` to the unique
   Lukasiewicz rotation of `r` uniform balls in `r+1` boxes; maximum
   occupancy is rotation-invariant.  The union/binomial bound therefore
   gives `pi(B_r)<=b_r`.  Since `D_r=Theta(log r)`,
   `log b_r=-Omega(log r log log r)`.

6. **Flow and gap normalization.**  Reversibility gives
   `Q_L(A,A^c)=Q_L(A,B)=Q_L(B,A)<=pi(B)`.  The indicator Dirichlet form is
   exactly this flow and its variance is `pi(A)pi(A^c)`, producing the
   displayed gap bound without a missing factor two, scan factor, or
   laziness factor.  Combining it with
   `gap(Y_r)>=1/[16(r+1)^8]` correctly contradicts every polynomial
   Dirichlet-form comparison.

## Numbered nonlift theorem

**N1 (proved; full projected chain bypass).**  Let `E_r^-` be the trees of
ordered root composition `(r-1,1)` and maximum degree at most `D_r-2`.
Every such source is in `A_r^c`, has `d_0=2`, and M35's aggregate identity
gives

```text
sum_(j>0) Pbar_r(d,d-e_0+e_j)=4/[3r(r-1)].
```

Every positive target has root degree one, empty prefix set, and maximum
degree at most `D_r-1`, hence lies in `A_r`.  With

```text
beta_r=r(r-1)^(r-2)/[2(r+1)^(r-1)],
bprime_r=(r+1)(e/(D_r-1))^(D_r-1),
```

the reservoir has mass at least `beta_r-bprime_r`, so orientation and
reversibility give

```text
Q_Pbar(A_r,A_r^c)
 =Q_Pbar(A_r^c,A_r)
 >=4(beta_r-bprime_r)/[3r(r-1)].
```

Thus the M48 separator is rigorously crossed at inverse-polynomial flow by
non-leaf moves of the full projection.  At `r=3`, the exact low-degree edge
`(2,1,0)->(1,2,0)` has rate `1/9`.  The theorem explicitly excludes any
claim about other full-`Pbar_r` cuts or the full identity-word chain `K`.

## Scope conclusion

- **ACCEPTED:** the auxiliary superpolynomial `L_r` gap upper bound.
- **REFUTED:** every polynomial `Y_r`-to-`L_r` comparison.
- **PROVED:** this cut does not lift to the full `Pbar_r` chain.
- **OPEN:** FULL ACTUAL PARKING FLOW or a genuinely different full-`Pbar_r`
  cut; all original-`K` terminal implications.
