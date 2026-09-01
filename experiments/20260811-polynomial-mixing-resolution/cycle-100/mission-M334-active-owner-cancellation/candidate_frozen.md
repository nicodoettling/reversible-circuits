# M334 frozen analytic candidate — AOEC and ownerwise coboundary

Date: 2026-08-14 UTC

Status: frozen before any computation

## 1. Exact signed active-owner incidences

Fix odd `k>=3`, `n=3k`, `1<=u<k/2`, admissible `2<=ell<=n-2`, and one maximal QBD block endpoint `T=T_q`. Use M325's exact positive and absolute-negative truncated exterior measures `p_T,n_T`, which each have mass `T`. For one exterior atom `e`, every middle phase `a in Z/kZ`, and every target phase `x in Z/nZ`, put

```text
s=e f_(a,u),
omega_T(e)=p_T(e) on the positive exterior support,
omega_T(e)=-n_T(e) on the negative exterior support.        (1.1)
```

The state keeps its literal source topology `K(s) in {T,S,N}`. In the designated exterior/middle channel the supports are disjoint, so the `T` contribution is exactly zero, but it is retained rather than silently reclassified. For generic target phases let `o_s(x)` be the owner and `d_s(x)` its residual size. The completion topology is retained as same-owner interlaced/nested (`IS/IN`) or cross-owner (`X`) until the final active-type sum.

Define the active type only after those labels are recorded:

```text
A(s,x)=S_d
  if o_s(x)=o_s(x+ell) is nonnull and has size d,

A(s,x)=X_(d,e), d<=e,
  if the two nonnull owners are distinct and have sizes d,e. (1.2)
```

Invalid/support-head terms are zero. For every active type `A`, define the fully combined signed mass

```text
Delta_T(A)
 =sum_e omega_T(e) sum_(a in Z/kZ) sum_(x in Z/nZ)
      1[A(e f_(a,u),x)=A].                            (1.3)
```

Equation (1.3) sums the cross, internal, and seam exterior atoms; all middle phases; all target phases; both `S/N` source topologies (and the identically zero `T` row); and every `IS/IN/X` completion label before comparing signs. No absolute value is taken inside any of those sums. In M325 notation,

```text
Delta_T(S_d)=Delta_T^S(d),
Delta_T(X_(d,e))=Delta_T^X(d,e).                     (1.4)
```

## 2. Frozen target AOEC_1

> **ACTIVE-OWNER ENDPOINT CANCELLATION (`AOEC_1`).** For every allowed `(k,u,ell)`, every maximal QBD endpoint `T_q`, and every active type,
> ```text
> Delta_(T_q)(S_d)>=0                 for d>=3,
> Delta_(T_q)(X_(d,e))>=0             for 2<=d<=e.   (AOEC_1)
> ```

This is strictly weaker than TOEC: all inactive-owner data have been quotiented out, and no atom-to-atom or same-full-signature transport is required. The accepted `k=5` signature obstruction remains a firewall against reintroducing TOEC, but it does not decide `(AOEC_1)`.

## 3. Exact coefficient identity

Put

```text
a_d=tau(d-1)/tau(d),       b_d=tau(d-2)/tau(d),
kappa_(S_d)=b_d,           kappa_(X_(d,e))=a_d a_e.  (3.1)
```

For each state and target phase, the literal completion ratio depends only on the active type: it is `b_d` for a same-owner pair and `a_d a_e` for two owners. Inactive owners contribute one. Therefore the exact active-owner identity is

```text
Psi(T)=sum_A kappa_A Delta_T(A),                     (3.2)
```

where every `kappa_A>0`. Thus `(AOEC_1)` implies `Psi(T_q)>=0` at every maximal block endpoint, exactly `GQAC_1`.

## 4. Ownerwise block coboundary

Let `T_(-1)=0`, `Delta_(-1)(A)=0`, and

```text
delta_(q,A)=Delta_(T_q)(A)-Delta_(T_(q-1))(A).       (4.1)
```

Then the exact scalar block increment is

```text
C_q=Psi(T_q)-Psi(T_(q-1))
   =sum_A kappa_A delta_(q,A).                       (4.2)
```

For a fixed active type, prefix nonnegativity `Delta_(T_q)(A)>=0` is equivalent to the existence of nonnegative causal flows `pi^A_(p,q)` (`p<q`) and leftovers `L^A_p>=0` satisfying

```text
sum_(p<q) pi^A_(p,q)=max(-delta_(q,A),0),
sum_(q>p) pi^A_(p,q)+L^A_p=max(delta_(p,A),0).       (4.3)
```

Consequently

```text
delta_(q,A)
 =L^A_q+sum_(r>q)pi^A_(q,r)-sum_(p<q)pi^A_(p,q),    (4.4)

C_q
 =sum_A kappa_A L^A_q
  +sum_(r>q)sum_A kappa_A pi^A_(q,r)
  -sum_(p<q)sum_A kappa_A pi^A_(p,q).                (4.5)
```

At the terminal endpoint all internal flows cancel:

```text
P_(k,ell)(u)=sum_A kappa_A sum_q L^A_q>=0.           (4.6)
```

Equations (4.2)--(4.6) are the required coefficient-resolved coboundary. They are identities/conditional equivalences, not a proof that the ownerwise flows exist.

## 5. Analytic target and sole authorized guard

For owner intervals `U_i(s)`, let

```text
C^s_(i,j)(ell)=|U_i(s) intersect (U_j(s)-ell)|.      (5.1)
```

Then `Delta_T(S_d)` is the signed complete aggregate of `C_(i,i)` over owners of size `d`, while `Delta_T(X_(d,e))` is the corresponding ordered cross-owner aggregate, folded to `d<=e`. This interval-incidence representation is exact and is the all-rank analytic route.

If the interval geometry does not yield a proof, the sole authorized guard is predeclared now as:

```text
k=7; every u in {1,2,3}; every admissible ell;
every maximal QBD endpoint; exact rational AOEC tables.       (5.2)
```

It may refute a universal active type but cannot prove `(AOEC_1)` or an all-rank trend. No other rank, transport, grouping, or replacement search is permitted.

## 6. Scope firewall

TOEC remains refuted at `k=5`. AOEC, GQAC, and MCLP are unresolved at this freeze point. No GOCI/OCI/CP/MS/FCL1, spectral-gap, mixing, or Terminal inference is made.
