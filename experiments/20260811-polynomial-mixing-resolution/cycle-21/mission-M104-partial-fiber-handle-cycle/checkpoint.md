# M104 checkpoint: fixed-cell theorem and same-size obstruction

Date: 2026-08-12. Status: final proof package complete; awaiting fresh audit.

The required project skill, `HANDOFF.md`, `GOAL_SPEC.md`, sampling and
experiment references, and frozen M92/M95/M97/M101 artifacts have been read.
Their accepted boundary is retained: M97 supplies an everywhere-defined
tree--unicycle--tree cut and spectrum-preserving lift, but no partial-fiber
gap, seam conductance, `gamma_1(d)` bound, full heat-bath result, or Terminal
claim.

The first exact question is now locked at fixed
`(j,p,Q_L,Q_R)`. I am separating the raw uniform word-fiber product law from
the lifted factor `1/ell(w)`, then checking which literal signed moves remain
inside that conditioning. The leading self-attack is the admissible
`p=id` cut with a full-label connected genus-zero identity factorization of
length `2d-2` on one side and a square on the other: it offers no label-size
decrease and may simply reintroduce the minimal genus-zero Hurwitz gap.

The raw conditional fiber at fixed `kappa=(j,p,Q_L,Q_R)` is now proved to be
a literal product of the two componentwise genus-zero side laws.  For
`D=2d-1`, the lifted conditional has density within `[D^-1,D]` of that raw
product, and

```text
ell(u,v)=r_L(u)+r_R(v)-1,
1/ell(u,v)=integral_0^1 z^(r_L(u)-1)z^(r_R(v)-1) dz.
```

Wholly internal signed moves preserve the fixed key.  A seam move stays in
the key only when the two boundary transpositions agree, in which case it is
a self-loop.  Comparing the exact restricted lift to the raw product loses
at most `D^3` in gap.  Extending M05's shuttle comparison with all scan and
mixture factors displayed gives

```text
gap(L_kappa)>=Gamma_0(d)/(420D^13).
```

If `beta(d)` is the exact seam-cell projection gap, a generic decomposition
gives the conditional implication

```text
gamma_1(d)>=Gamma_0(d) beta(d)/(2940D^13).
```

Both `Gamma_0(d)` and `beta(d)` remain unresolved.  More decisively, the
cell with `j=2d-2,p=id`, a full left support block, and one right square is
exactly the full-label minimal genus-zero identity-factorization space
`Z_d` on its nontrivial coordinate.  Its raw restriction is

```text
P_kappa=[(D-2)/D]P_0,d+[2/D]I.
```

Thus the fixed-cell route reintroduces the same-`d` minimal genus-zero gap and
does not create an induction.  This is a sharp obstruction to that proof
route, not a slow-mixing result.

The deterministic audit exhausted `d=2,3,4`, finding zero failures in raw
product counts, side handle-distance dependence, internal key preservation,
incidence, or component lengths.  Every nontrivial seam proposal changed the
key or lost cut admissibility.  These finite facts calibrate the universal
algebra and are not asymptotic gap evidence.
