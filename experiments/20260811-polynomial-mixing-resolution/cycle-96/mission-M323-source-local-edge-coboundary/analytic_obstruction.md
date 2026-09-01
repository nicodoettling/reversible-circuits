# M323 exact obstruction to product-fixed source surgery

Date: 2026-08-14 UTC.

Status: **`SLPF` refuted at its literal-support condition; repaired reduction
only.**

## 1. Analytic source-support obstruction

Source A has exterior residual components

```text
C_-=(0,...,k-1),       C_+=(2k,...,3k-1),
```

whereas source B joins their nonzero arcs into

```text
L=(1,...,k-1,2k,...,3k-1).
```

A transposition joining a vertex of `C_-` to a vertex of `C_+` is internal
to `L` and can therefore be a rank-decreasing first factor for source B.
The same transposition joins two distinct residual cycles for source A, so it
increases rank by one.  It cannot begin a minimal source-A completion.

This obstruction is not detected by `Exc_pf`: the transposition may cross a
changed source seam while the marked owner and every support head avoid all
five seam vertices.  Consequently the product-fixed switch can be undefined
off its frozen exceptional set.  This failure precedes split-cell support,
weight equality, and any edge norm.

## 2. Exact actual-token witness

The sole predeclared exact guard finds the first lexicographic witness at

```text
k=7, n=21, row H_2, quantile cell (s,t)=(1,1),
source-B channel 2, split 1,
e=(6,14),              f=(3,5).
```

Here `e=(k-1,2k)` is internal to B's long cycle `L` but joins A's distinct
cycles `C_-` and `C_+`.  The marked slot and head geometry is

```text
marked owner size       2
marked generic support  {3}
support heads            {2,4,5,13}
Sigma                     {0,1,6,14,20}.
```

Thus both intersections in `Exc_pf` are empty.  Under source A the ranks are

```text
rank(Q_A), rank(e Q_A), rank(f e Q_A) = (18,19,18),
```

instead of the required `(18,17,16)`.  Therefore
`sigma(eta_B)` does not exist.

This raw atom is not removed by residual-profile subtraction.  Its exact
profile masses in cell `(1,1)` are

```text
g_A(P)=0,
f_B(P)=21484375/54238159872,
[f_B(P)-g_A(P)]_+=21484375/54238159872.
```

The cell has

```text
pi_(1,1)=61917364224/137858491849,
rho_(1,1)=49168032837363259/1633552709319917568,
```

and the positive total residual-token mass carried by this weighted raw atom
is exactly

```text
22000000000/91400180095887 > 0.
```

Hence an actual nonexceptional token has no product-fixed reverse raw atom.
The unordered-edge/reversed-orientation condition cannot even be stated for
its image.  `SLPF` is refuted independently of the proposed weight
coboundary.

## 3. Strongest strictly narrower repaired reduction

For a source-R raw prefix `(e,f)`, define the opposite-source seam predicate

```text
BadPref_R(e,f)
 := rank(e Q_barR) != rank(Q_barR)-1
    or rank(f e Q_barR) != rank(Q_barR)-2.           (3.1)
```

Equivalently, one of the observed prefix edges joins rather than cuts the
opposite source's residual components across a changed exterior seam.  This
uses only the literal prefix and fixed source seam/component geometry; it
does not consult a profile-edge sign or aggregate surplus.

Enlarge the exception to

```text
Exc_pf^* = Exc_pf
           union BadPref_A(xi_A)
           union BadPref_B(eta_B).                  (3.2)
```

On `(Exc_pf^*)^c`, the two retained prefixes have positive opposite-source
minimal-completion counts, so the first support obstruction is removed
exactly.  The token edge table decomposes before norms into the restrictions

```text
J=J_compatible+J_exceptional.                       (3.3)
```

The strictly narrower repaired lemma `SLPF*` is:

1. on the compatible part, prove that `(2.3)` of `token_and_candidate.md`
   lands in a supported reverse residual token and satisfies an exact local
   weight coboundary;
2. prove the single combined exceptional-mass estimates
   ```text
   mass(Exc_pf^{*,H_d}) <= C d b_d/k,
   mass(Exc_pf^{*,A_d}) <= C d b_d/k,
   mass(Exc_pf^{*,C_de})<= C max(d,e)b_d b_e/k.
   ```

If item 1 cancels `J_compatible`, `(3.3)` bounds the remaining edge flux by
the one combined exceptional measure.  No channel, type, cell, or orientation
is bounded separately.

`SLPF*` is source-local and strictly narrower than the refuted assertion, but
both its weight coboundary and its Borel exceptional-mass scale are
**unresolved**.  The `k=7` witness proves no asymptotic lower bound for the
enlarged exception.

No MPCF or downstream conclusion follows.
