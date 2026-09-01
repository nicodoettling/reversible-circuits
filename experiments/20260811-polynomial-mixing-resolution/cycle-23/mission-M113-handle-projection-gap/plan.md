# M113 plan: exact handle-cell projection gap

Date: 2026-08-12 UTC.

## Objective

Analyze M104's unresolved `HANDLE-CELL PROJECTION GAP` for the exact
spectrum-preserving M97 lift.  The auxiliary target is the uniform law on
connected-support identity transposition words of length `2d`, and the exact
half-lazy signed adjacent-Hurwitz kernel and multiplication convention are
those in M104.  The projected cells are

```text
kappa=(j,p,Q_L,Q_R),
p=eval(t_1...t_j),
Q_L=support partition of the prefix,
Q_R=support partition of the suffix.
```

The target deliverable is either an explicit `beta(d)>=d^{-O(1)}` bound for
the stationary-flow projection `bar L`, or a rigorous obstruction to a named
comparison that leaves a strictly narrower standalone lemma.

## Method

1. Derive the exact projected stationary mass and edge flow directly from
   `tilde_pi(w,j)=pi_d(w)/ell(w)` and
   `L((w,j),(w',j'))=P_d(w,w')/ell(w')`.
2. Separate word-preserving cut-refresh flow from nontrivial signed physical
   proposals, and state exactly which same-cut proposals are internal, seam,
   or make the old cut inadmissible.
3. Encode realizable keys by the connected-unicyclic incidence graph of
   `Q_L,Q_R` and the cycles of `p`; use the exact genus-zero side counts where
   they are genuinely sufficient.
4. Test only named universal comparison lemmas on exact `d<=4` data.  In
   particular audit zero-flow endpoints, reducibility, and `d=2` separately.
5. Avoid canonical-word hubs and do not infer asymptotic expansion from the
   finite audit.

## Candidate proof routes and failure modes

- Compare `bar L` to a cut-shift/seam-surgery chain on realizable incidence
  keys.  Failure mode: the proposed local surgery may have zero conditional
  mass or require hidden side-factorization information.
- Use the holding part of `P_d` to extract a word-preserving cut-refresh
  subchain.  Failure mode: this subchain decomposes by the underlying word
  and cannot by itself mix keys globally.
- Use the exact genus-zero Hurwitz enumeration formula to cancel cell-size
  ratios in stationary flows.  Failure mode: the `1/ell` tilt depends on
  handle distances not determined by the key.

## Claim discipline

Every material conclusion will be labeled `proved`, `conditional`, `exact
finite`, `refuted`, or `unresolved`.  Classification H remains conditional
under the current repository guide and will not be silently imported.  This
mission makes no claim about `Gamma_0(d)`, `gamma_1(d)`, the full heat-bath
chain, or either terminal outcome unless independently proved.

## Reproduction metadata

Repository commit at start: `502a6f031c6d5a4bc0064ee5b370a4fa3914f993`.
Any exact script will use Python's standard library, deterministic
enumeration (`seed=null`), and machine-readable JSON output.
