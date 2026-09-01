# M162 plan: vector beta cancellation

Date: 2026-08-13 UTC.

## Objective and scope

Work only on the normalized full unweighted reset excursion `F=H/q` in the
auxiliary nonlazy minimal-long-cycle parking projection.  The project target
remains uniform fixed-length identity transposition words; permutations
compose as `(pq)(x)=p(q(x))`, with factors displayed left-to-right.  This
mission claims nothing about an auxiliary gap, ROOT-MEAN LIFT, the original
lazy `{3,4,5}` heat-bath chain, polynomial mixing, or a project terminal.

Starting from frozen M157/M160, construct the actual finite history feature
map `Phi_x` such that

```text
K_x(u,v)=<Phi_x(u),Phi_x(v)>,
F(x)=|| E_(Beta(D,kappa-D)) Phi_x ||^2.
```

Use the shared-observation beta-binomial transfer, including the killed
`x=d` branch, to derive a vector-valued posterior/Doob identity and the
Jacobi decomposition of `Phi_x`.  Test a precise centered-energy correction
to diagonal trace, beginning with subtraction of the degree-one Jacobi
energy.  This is distinct from pointwise polarization, positive part,
absolute value, and the generic basin frame.

## Falsifiable claim and caps

For a beta law `mu`, let `P_1(u)=u-E_mu u` and

```text
T_1(x)=E_mu ||Phi_x||^2
       - ||E_mu[P_1 Phi_x]||^2/E_mu[P_1^2].
```

The first tested sufficient inequality is `F(x)<=T_1(x)`, universally by
orthogonal projection, together with the nontrivial boundary claim
`T_1(B,L,2,1)<=1-q_(B,L)` on fresh right-heavy states.  If the boundary
claim fails, record the first exact counterexample and test the least higher
Jacobi truncation that survives the prescribed finite grid.  Finite survival
will be labeled exact finite, not a theorem.

Exact tests are capped at `B<=3`, `L<=6`, `kappa<=8`; there is no `L=7`
enumeration.  All theorem-critical arithmetic uses `Fraction`, Python's
standard library, and deterministic `seed=null`.

## Deliverables

- `checkpoint.md` at halfway;
- a standalone exact checker and machine-readable JSON;
- a theorem note distinguishing exact equality, universal inequality,
  finite diagnostics, and unresolved steps;
- a nine-field frozen `report.md`, `freeze_manifest.md`, and `SHA256SUMS`.

