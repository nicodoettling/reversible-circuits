# Exact adjacent-split endpoint transport

Date: 2026-08-14 UTC.

Status: Proposition 1 is a **proved exact coupling identity**.  It is not an
estimate.  `SET`, `PBV`, and `FD-bound` remain **unresolved**.

## 1. Setting and literal conditional laws

Use `(pq)(x)=p(q(x))`, displayed factors left-to-right, `n=3k`, and odd
`k>=3`.  Let

```text
L=(1,...,k-1,2k,...,3k-1),       d=|L|=2k-1,
M=(k,...,2k-1).
```

Write `L_r` for the vertex in phase `r in Z/dZ` of this displayed directed
cycle and

```text
e_(u,r)={L_r,L_(r+u)},            1<=u<=k-1.         (1.1)
```

Because `d` is odd, `r -> e_(u,r)` enumerates the `d` chords with smaller
source split `u` exactly once.  All these chords have the same M91 first-edge
probability `nu_L(e_(u,r))=p_u/d`; consequently the conditional phase `r` is
uniform.

For channel one, after choosing `e_(u,r)`, independently choose
`f~nu_M`.  This gives the literal conditional product law
`Phi_(1,u)=Law(e_(u,r)f)`.

For channel two put

```text
c_(u,r)(f)=N_L(e_(u,r),f)/nu_L(e_(u,r)),             (1.2)
```

on the admissible second factors `f in T(e_(u,r)L)`, extended by zero to all
transpositions.  M91's completion-count normalization gives
`sum_f c_(u,r)(f)=1`; hence
`Phi_(2,u)=Law(e_(u,r)f)` for uniform `r` and
`f~c_(u,r)`.

## 2. A literal adjacent coupling

For channel one define `C_(1,u)` by choosing `r` uniformly, choosing one
`f~nu_M`, and setting

```text
s=e_(u,r)f,                    t=e_(u+1,r)f.         (2.1)
```

For channel two, at fixed `(u,r)`, abbreviate
`c_0=c_(u,r)` and `c_1=c_(u+1,r)`.  Define their explicit maximal coupling

```text
m(f)=min(c_0(f),c_1(f)),       gamma=sum_f m(f),

C_(u,r)(f,g)
 =1[f=g]m(f)
  +(c_0(f)-m(f))(c_1(g)-m(g))/(1-gamma),             (2.2)
```

where the second term is omitted when `gamma=1`.  Choose `r` uniformly,
choose `(f,g)` by `(2.2)`, and set

```text
s=e_(u,r)f,                    t=e_(u+1,r)g.         (2.3)
```

Call the resulting coupling `C_(2,u)`.  Formula `(2.2)` is nonnegative and
has marginals `c_0,c_1`, so `C_(j,u)` has exact marginals
`Phi_(j,u),Phi_(j,u+1)` for `j=1,2`.  No quotient representative, product
kind, collision, cyclic phase, or second-factor completion weight has been
dropped.

## 3. Endpoint-profile identity with every normalization visible

Independently of M267, for a supported product `a` define its null-extended
generic-edge owner `o_a`, the exact rooted-tree owner coefficient `kappa_a`,
and

```text
E_ell(a)=sum_(x mod n) [
 kappa_a(o_a(x-ell),o_a(x+1))
-kappa_a(o_a(x-ell),o_a(x))].                       (3.1)
```

At phase `x`, let `sigma_a(ell,x)` retain the intermediate kind, all three
residual sizes, the three literal owners at `x-ell,x,x+1`, their equality
pattern, and `ell`.  Let `w(sigma)` be the bracketed charge in `(3.1)`, and
define the kind-separated empirical signature measure

```text
P_(K,ell)(a)=1[K(a)=K] (1/n)sum_(x mod n)
                         delta_(sigma_a(ell,x)).     (3.2)
```

Then, directly from the definitions,

```text
sum_K <w,P_(K,ell)(a)>=E_ell(a)/n.                  (3.3)
```

### Proposition 1 (proved: adjacent `D_u` transport identity)

For each channel, split, kind, and lag,

```text
A_(j,u,K,ell)
 =E_((s,t)~C_(j,u))[P_(K,ell)(s)-P_(K,ell)(t)].     (3.4)
```

Consequently the complete adjacent-split part of M267's tensor satisfies

```text
G_ell^adj
 :=sum_K <w, sum_(j=1)^2 alpha_j
                  sum_(u=1)^(k-2)D_u A_(j,u,K,ell)>

 =1/n sum_(j=1)^2 alpha_j sum_(u=1)^(k-2)D_u
       E_((s,t)~C_(j,u))[E_ell(s)-E_ell(t)].         (3.5)
```

#### Proof

The two marginals just verified imply `(3.4)` by linearity of the empirical
profile map `(3.2)`.  Pairing with `w`, summing `K` before doing anything
else, and applying `(3.3)` gives `(3.5)`.  QED.

Equation `(3.5)` is deliberately still signed: both `j=1,2` channels and
all `T/D` outcomes remain inside the scalar sum, every `D_u<0` retains its
sign, and the exterior factor `1/n` from phase averaging is explicit.  No
absolute value or statewise endpoint-variation envelope has yet been used.
Taking absolute values separately in `j`, `u`, or product kind would not be
the target argument.

## 4. What remains

The analogous literal coupling for `Phi_(j,u)` versus `Psi_(j,u)` must be
constructed on the actual two-cycle embedding.  More importantly, its
`q_u` flow has to be superposed with `(3.5)` and algebraically cancelled
before any coupling cost or statewise lag-`l1` envelope is applied.  That
signed cancellation, not the existence of the marginal couplings above, is
the first unresolved step toward `SET`.

## 5. Full monotone split transport: `D/q` cancels before cost

Put `h=(k-1)/2`.  Let `S` have the short-cycle split law `q` on
`{1,...,h}` and let `T` have the long-cycle split law `p` on
`{1,...,k-1}`.  M91's proved inequality `D_u<0` is exactly

```text
Pr(T<=u)=sum_(v<=u)p_v <=sum_(v<=u)q_v=Pr(S<=u).     (5.1)
```

Hence the common-uniform quantile coupling `pi(s,t)` has `S<=T` almost
surely.  It also has the exact edge-crossing law

```text
sum_(s<=u<t)pi(s,t)=Pr(S<=u<T)=-D_u.                (5.2)
```

Here is a fully literal way to attach factor configurations to this split
coupling.  For channel one, couple the uniform chord phase in the two-cycle
embedding underlying `Psi_(1,s)` to the uniform chord phase in `L`
underlying `Phi_(1,s)` by maximal coupling on the actual ambient
transposition; on the unmatched mass use the product of the two residual
phase laws.  In both cases use one common independent `f~nu_M`.  This is a
coupling `B_(1,s)` of the raw ordered-factor laws whose product pushforwards
are `Psi_(1,s),Phi_(1,s)`.

For channel two define the normalized raw ordered-pair atoms

```text
b_s(e,f)=1[e in E_L(s)] N_L(e,f)/p_s,
a_s(e,f)=1[e in E_(C_- union C_+)(s)]
          N_(C_-C_+)(e,f)/q_s.                      (5.3)
```

The fair exterior-component choice is already in the second completion
law.  Couple `a_s,b_s` by the explicit maximal-coupling formula `(2.2)` on
the common raw atom space of ambient ordered transposition pairs.  This is
`B_(2,s)`.  It retains shared-endpoint triangles, both double colors, every
ordered lift, and every source-completion weight.

Disintegrate `B_(j,s)` as a kernel from its `Psi` raw configuration to its
`Phi` raw configuration.  Likewise disintegrate the adjacent coupling
`C_(j,u)` from Section 2 as a kernel from the raw `Phi_(j,u)` configuration
to the raw `Phi_(j,u+1)` configuration.  Conditional on `(S,T)=(s,t)`, first
sample

```text
(Y_s,X_s)~B_(j,s),
```

then apply the adjacent kernels successively to obtain

```text
X_s,X_(s+1),...,X_t.                                 (5.4)
```

Every `X_u` on a path that reaches level `u` has marginal `Phi_(j,u)`;
`Y_s` has marginal `Psi_(j,s)`.  Therefore the endpoints of the mixed path
law have marginals

```text
Y_S ~ sum_s q_s Psi_(j,s)=H_(j,A),
X_T ~ sum_t p_t Phi_(j,t)=H_(j,B).                  (5.5)
```

### Proposition 2 (proved: full `D/q` path identity)

For every test function `g` on supported product states,

```text
E[g(X_T)-g(Y_S)]
 =sum_s q_s[Phi_(j,s)-Psi_(j,s)](g)
  +sum_u D_u[Phi_(j,u)-Phi_(j,u+1)](g).             (5.6)
```

Consequently, after mixing the two path laws with the unchanged channel
masses `alpha_1,alpha_2`,

```text
eta(g)=sum_(j=1)^2 alpha_j E_j[g(X_T)-g(Y_S)].       (5.7)
```

In particular, with `g=E_ell`,

```text
sum_K <w,T_(K,ell)>
 =1/n sum_(j=1)^2 alpha_j
       E_j[E_ell(X_T)-E_ell(Y_S)].                  (5.8)
```

#### Proof

Telescope `g(X_T)-g(Y_S)` along `(5.4)`.  The initial edge contributes the
first sum of `(5.6)`.  A path crosses the adjacent edge `u -> u+1` exactly
on `{S<=u<T}`; by `(5.2)` its mass is `-D_u`, and its conditional raw
marginals are `Phi_(j,u),Phi_(j,u+1)`.  Its contribution is therefore

```text
(-D_u)[Phi_(j,u+1)-Phi_(j,u)](g)
 =D_u[Phi_(j,u)-Phi_(j,u+1)](g).
```

Summing proves `(5.6)`.  M91's exact channel decomposition proves `(5.7)`.
The independently rederived phase normalization `(3.3)` proves `(5.8)`.
QED.

This is the required algebraic cancellation point.  The `Theta(sqrt(k))`
sum of individual `|D_u|` no longer appears: all internal split levels have
cancelled, and only the two endpoints of one full merged-versus-separate
transport remain.  Nevertheless `(5.8)` is not yet an `O(n^-2)` estimate.
Applying the statewise endpoint-`l1` envelope now gives only `O(1/n)` for the
left side after its displayed `1/n`, whereas `SET` needs `O(1/n^2)`.  The
remaining gain must therefore come from the literal chord-phase/two-cycle
embedding and/or cancellation between the two channel endpoint responses,
not from another triangle bound on path edges.
