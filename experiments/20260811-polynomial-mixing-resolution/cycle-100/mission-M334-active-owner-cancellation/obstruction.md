# M334 exact AOEC obstruction

Date: 2026-08-14 UTC

Status: **proved exact finite refutation of `AOEC_1` at `k=7`; no all-rank or downstream inference**

## 1. Frozen identity retained

For every canonical maximal endpoint `T` and active type `A`, M334's signed incidence is

```text
Delta_T(A)
 = sum_e omega_T(e) sum_(a in Z/kZ) sum_(x in Z/3kZ)
     1[A(e f_(a,u),x)=A].
```

The state data are classified by source topology and completion topology before this sum. The exact completion coefficients are

```text
kappa_(S_d)=b_d,
kappa_(X_(d,e))=a_d a_e,
```

and therefore

```text
Psi(T)=sum_A kappa_A Delta_T(A).                       (AOTI)
```

Writing `delta_(q,A)=Delta_(T_q)(A)-Delta_(T_(q-1))(A)` also gives the exact coefficient-resolved block coboundary

```text
Psi(T_q)-Psi(T_(q-1))=sum_A kappa_A delta_(q,A).
```

These are unconditional algebraic identities. The causal-flow representation in `candidate_frozen.md` is equivalent to ownerwise prefix nonnegativity; it does not assert that such flows exist.

## 2. Sole guard and exact counterexample

Only the predeclared guard was evaluated: `k=7`, every `u in {1,2,3}`, every admissible lag, and every canonical maximal QBD endpoint. The harness SHA-gates accepted M311's no-import exact QBD implementation, mechanically specializes `K=11` to `K=7`, and adds active-owner incidence bookkeeping. It uses exact `Fraction` arithmetic.

The first lexicographic failure is

```text
u=1, ell=2, block_index=0, endpoint_b=3,
T=5665610708886866/30120839742579859,
A=S_14.
```

At this endpoint the fully accumulated positive cross/`N` mass of `S_14` is zero, while

```text
negative internal mass = 11343430713381552/30120839742579859,
negative seam mass     = 5184/16807.
```

Thus, after the exact common-denominator combination,

```text
Delta_T(S_14)
 = 0
   - 11343430713381552/30120839742579859
   - 5184/16807
 = -20633990196069360/30120839742579859 < 0.
```

This single exact value contradicts the universal condition `Delta_T(S_d)>=0`. Hence `AOEC_1` is refuted.

The most negative recorded prefix is for `S_19`, `u=1`, `ell=10`, block zero:

```text
-207274081831549056/30120839742579859.
```

Across the frozen guard there are 2,920 negative active-prefix instances and 7,364 nonzero active-prefix instances. These counts are descriptive finite facts, not trends.

## 3. Exact checks and scope

The harness checks statewise AOTI, prefix AOTI, every retained middle and target phase, separate internal and seam negative contributions, equal exterior normalization, and lag reflection. All checks pass exactly.

The obstruction is strictly to AOEC. Because AOTI is a positive-coefficient sum across *different* active types, negative `Delta_T(A)` can in principle be offset by other active types. Accordingly this mission neither refutes nor proves GQAC. The first unresolved scalar statement is exactly the weighted aggregate already displayed by AOTI; no replacement cancellation target is introduced here.

TOEC remains independently refuted at `k=5`. No other rank, reformulation, transport, grouping, cellwise bound, fixed-middle sign, MON/FOSD, PSD, Abel monotonicity, GQAC, MCLP, GOCI, OCI, CP, MS, FCL1, gap, mixing, or Terminal inference is part of this freeze.
