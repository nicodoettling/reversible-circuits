# M326 exact append-only salvage obligation

Date: 2026-08-14 UTC

Frozen M323 must remain unchanged.  Its claimed off-`Exc_pf` witness can be
salvaged only by a new append-only certificate for the missing A endpoint.

Keep the frozen `k=7,H_2`, cell `(s,t)=(1,1)`, and bad B atom `eta_*` with
`e=(6,14)`, `f=(3,5)`.  Define the non-Touch A residual mass

```text
N_A=sum_P a_(1,1)(P)
    sum_(xi_A over the raw fiber (s=1,P))
       Pr[xi_A|s=1,P] 1[not Touch_Sigma(xi_A)].      (1)
```

The exact missing assertion is

```text
N_A>0.                                               (2)
```

Equivalently, exhibit one concrete A raw marked atom with positive
`a_(1,1)(P)`, positive conditional fiber weight, and both its marked-owner
and support-head sets disjoint from `Sigma`.

If `(2)` is proved, the nonexceptional token mass paired with `eta_*` is

```text
c_H pi_(1,1) b_(1,1)(Q)/rho_(1,1)
 *Pr[eta_*|t=1,Q] * N_A >0.                          (3)
```

The already-proved absence of `sigma(eta_*)_A` would then refute `S_pf` on
an actual token outside `Exc_pf`.  Without `(2)`, only the positive mass
obtained by replacing `N_A` with the full A residual mass `rho` is known.

This is the first exact salvage obligation.  M326 performs no computation or
search for such an A atom and proposes no alternative surgery.
