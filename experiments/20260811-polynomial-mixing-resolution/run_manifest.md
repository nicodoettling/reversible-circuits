# Persistent Polynomial-Mixing Resolution Run

- Start date (UTC): 2026-08-11
- Repository commit: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`
- Target: uniform law on `Omega(N,m)` for `N>=3`, even `m>=4`
- Terminal outcomes: exactly TERMINAL A or TERMINAL B in the goal prompt
- Available concurrency: coordinator plus three workers
- Mission schedule: M01--M15 in sequential waves; no mission is dropped
- Bulk-output policy: keep bulk output outside Git and record any path used
- Dependency policy: no package installation or machine-configuration changes

## Composition convention

Permutations are maps on `[N]`. Multiplication `pq` means composition `p`
after `q`, so `(pq)(x)=p(q(x))`. Words evaluate to `t_1...t_m` in this
notation. The project right Hurwitz move is

    (a,b) -> (b,b^{-1}ab).

The Ben-Itzhak--Teicher generator is its inverse and induces the same orbit
relation.

## Exact kernel

For `R_m={r in {3,4,5}:r<=m}`,

    K_{N,m} = (1/2) I
      + (1/(2|R_m|)) sum_{r in R_m}
          (1/(m-r+1)) sum_{i=1}^{m-r+1} H_{i,r},

where `H_{i,r}` replaces the selected block by an exactly uniform length-`r`
transposition word with the same ordered product.

## Cycle 01

- Coordinator: M01 independent classification/irreducibility closure
- Worker lane 1: M12 sparse and near-minimal red team
- Worker lane 2: M13 full-support and entropic red team
- Worker lane 3: M15 resource and paradigm audit

Every worker owns only its named mission directory and must produce
`plan.md`, `checkpoint.md`, and `report.md`. Computations, if any, also require
machine-readable raw output and exact reproduction commands.
