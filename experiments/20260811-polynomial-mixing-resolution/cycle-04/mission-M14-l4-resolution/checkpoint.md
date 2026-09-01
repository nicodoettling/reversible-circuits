# Halfway checkpoint: qualitative l=4 connectivity closes

## Exact setting

Use `(pq)(x)=p(q(x))`.  Fix `N>=3`, a feasible endpoint `h in A_N`, and a
length-eight transposition word with product `h`.  The nonlazy aligned chain
is

```text
B_4=(1/3)(H_{1,4}+H_{3,4}+H_{5,4}).
```

The target law is uniform on the fixed-product microfactor word fiber.

## Checked classification input

Douvropoulos--Lewis published Theorem 18 (Theorem 4.2 in the section-numbered
preprint), after the checked type-A specialization,
says two same-length transposition factorizations of arbitrary fixed `h` are
Hurwitz-equivalent exactly when their factorization graphs have the same
labeled connected components and the same factor count on every component.
Their left Hurwitz convention is inverse to the other common project
convention, so the orbit relation is unchanged.

Every adjacent position pair among `1,...,8` lies in at least one of the
three aligned windows.  Replacing `(a,b)` by `(b,bab)` and retaining the
other two window factors preserves its four-factor ordered product.  Thus
every elementary Hurwitz move has positive `B_4` probability, including the
boundary pairs `(1,2)` and `(7,8)`.  Each fixed component/weight macro-fiber
is consequently connected.

## Macro connection by actual square outcomes

If a connected component `C` is a union of `q_C` cycles of `h`, with
`v_C` vertices and `k_C` factors, Douvropoulos--Lewis published Proposition
8(4) (Proposition 2.7(4) in the section-numbered preprint) specializes to

```text
k_C=v_C+q_C-2+2g_C,       g_C>=0.
```

Within its Hurwitz orbit it can be put in a form consisting of connected
factorizations on two unions of endpoint cycles followed by an adjacent
bridge square `(f,f)`.  Replacing that square by `(e,e)` inside a chosen
anchor component splits the old component and transfers the factor pair to
the anchor.  Similarly, each positive `g_C` exposes a surplus square that
can be transferred.

Every adjacent square position is contained in an aligned window.  Retaining
the other two factors and replacing `(f,f)` by `(e,e)` leaves the window
product unchanged, so this is an actual heat-bath outcome, not an auxiliary
move.

For `h!=id`, choose one nontrivial endpoint cycle as anchor, split every
component into individual endpoint cycles, and transfer all surplus pairs to
the anchor.  This yields a common macro.  For `h=id`, reduce to a single
active edge and then use

```text
s^8 -> r^4 s^4 -> r^8
```

to reach a designated edge.  At minimum endpoint length no square is needed:
the macro of separate endpoint cycles is already unique.  Therefore the
microfactorized aligned chain is connected for every feasible endpoint.

## Exact product-path translation

Grouping positions as four ordered transposition pairs gives increments
`q_1,...,q_4 in supp(Q_N)`.  An aligned update is exactly an adjacent
two-increment same-product replacement.  Every product replacement lifts to
microfactors, and microfactor labels above a fixed product path can be
refreshed while retaining both increment products.  Components therefore
agree exactly.  Universal l=4 product-path connectivity follows.

## Remaining halfway work

The classification supplies no quantitative Hurwitz diameter, but fixed
length makes this unnecessary.  The endpoint fiber has at most `M^8` states
and every positive transition is at least `1/(3M^4)`.  The remaining task is
to freeze a spanning-tree Poincare comparison with path length, load,
stationary mass, and the Hamiltonian/random-scan normalization explicit.

The prior exact all-endpoint survival through `N=7` is a calibration check,
not an input to this proof.
