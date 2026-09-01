# M305 report: combined Borel profile route to SOCL

Date: 2026-08-14 UTC.

## Verdict

**Inconclusive; keep CBPV as the first unresolved marked-profile lemma.**

The deterministic implication `CBPV => SOCL` is proved exactly, and the
underlying complete scalar conditioned-Borel split coefficient has
`O(1/k)` discrete variation at every odd rank.  This does not prove CBPV:
the scalar coefficient has `Theta(k^(-1/2))` absolute mass, and the actual
owner-response profile changes with the split.  The first missing step is
the fully combined marked-profile Abel estimate `(CMPAD)` in
`analytic_reduction.md`.

SOCL, SOCT, BODT, DOR, PBV/FD/FCL1, gap, mixing, and every Terminal
statement remain unresolved.

## Scope

The target is the accepted M297/M302 complete centered first-pair law in
the auxiliary uniform minimal-factorization model, with odd `k>=3`,
`n=3k`, and `(pq)(x)=p(q(x))`.  It is not the global fixed-length bridge
law and not the `{3,4,5}` heat-bath chain.

Every imported inventory is source-locked in `source_lock.md`.  No
predecessor, coordinator file, manuscript, or project skill was edited.

## Proved exact advances

1. Literal owner response profiles obey

   ```text
   ||P^H||_1<=32,
   ||P^A||_1<=4d,
   ||P^C||_1<=4min(d,e).
   ```

   Grouping only after the complete `Omega_T/Omega_S/Omega_N` coefficient
   is formed proves `CBPV => SOCL` with the exact three requested row
   scales.

2. For `b_j=e^(-j)j^(j-1)/j!` and `R_m(q)=b_(m-q)/b_m`, the half-range
   complementary ratios satisfy uniform value, adjacent-gap, and
   adjacent-rank estimates.  Applied to M91's complete split laws
   `p_s,q_s`, this proves

   ```text
   sum_s |Delta(p_s-q_s)|=O(1/k).
   ```

3. The general shortcut from scalar coefficient variation to a marked
   response bound is strictly false: bounded profile kernels can align
   with the sign of `p_s-q_s`, producing `Theta(k^(-1/2))` rather than
   `O(1/k)`.  This refutes only the shortcut, not CBPV.

## Small sizes

- Formal `u_1=0`; every size-one response row is zero.  A literal
  coefficient measure may retain an atom at the zero profile, which is
  harmless and omitted from the reduced response measure.
- `Delta A_2=Delta A_3=0` on the target lag range.
- `H_2,H_3` and off-diagonal rows involving sizes two or three do not
  vanish and remain inside `(CMPAD)`.
- At `k=3`, the threshold is one, so SOCL is exactly trivial.

## Sole finite diagnostic

The predeclared deterministic guard used only `k=11`, `n=33`, exact
rational arithmetic, and no nonstandard dependency.  It SHA-gated the
frozen M297 probe, reconstructed both complete source laws, and grouped
the physical signed coefficient by literal response profile only after all
sources, live channels, `T/S/N` kinds, phases, seams, and incidences were
combined.

```text
states                                      27,060
positive-composition representations       91,110
raw ordered A/B pairs                      23,595 / 52,845
max k||mu^H_d||/(d b_d), d>=2              2.3542421865
max k||mu^A_d||/(d b_d), d>=4              0.8658065231
max k||mu^C_de||/(max(d,e)b_db_e), d,e>=2  4.9293426565
```

CBPV survives this rank.  These values are finite-only and establish no
uniform constant.

## First unresolved lemma

`CMPAD` is the single norm bound on the exact measure

```text
sum_u D_u(F_u-F_(u+1)) + sum_s q_s(F_s-G_s),
```

where `F,G` are the two-channel-combined pushforwards through the actual
`H/A/C` owner-incidence mark.  All source/type/topology/phase/seam terms
are inside this expression before the norm.  Proving its three Borel-scaled
bounds is exactly the missing CBPV step; no separate Abel-term or channel
estimate is claimed.

## Artifact map

- `plan.md`: pre-computation candidate and decision rule.
- `source_lock.md`: immutable dependency gates.
- `profile_implication.md`: exact conditional implication.
- `analytic_reduction.md`: Borel lemma, shortcut obstruction, and CMPAD.
- `cbpv_k11_guard.py`, `cbpv_k11_results.json`: sole finite guard.
- `run_manifest.md`: reproducibility metadata.
- `audit_request.md`: fresh-audit checklist.
