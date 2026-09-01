# M296 Freeze Manifest

Date: 2026-08-14 UTC.

## Frozen verdict

```text
PROMOTE: exact residual chart-stabilizer tuple-transporter identity,
         pairwise double-coset criterion, transporter-coset form,
         frame/action/length firewalls, and explicit stabilizer structure.
OPEN:    SSTID higher-arity intersection plus polynomial representative
         diameter, hence the true polynomial matching-coset refinement.
```

## Frozen exact statements

Fixing one edge `Q_0` and writing `S=BStab_d`, every common schedule is
parameterized by one `s in S`. For

```text
L_Q=alpha_Q^(-1);alpha_0,
R_Q=delta_0^(-1);delta_Q,
C_Q={s in S:L_Q;s;R_Q in S},
```

the exact family identity is

```text
intersection_Q(alpha_Q;S;delta_Q^(-1))
 =alpha_0;(intersection_Q C_Q);delta_0^(-1).
```

Each `C_Q` is the `S`-transporter from `c^(L_Q)` to `c^(R_Q^(-1))`.
It is nonempty exactly when

```text
S;L_Q;S=S;R_Q^(-1);S,
```

and, after choosing one transporter, is a coset of the corresponding
two-point stabilizer. Short common braids and short residual stabilizer
elements are polynomially equivalent up to the two accepted `O(d^4)`
frames.

The literal doubled-star stabilizer contains the displayed local loops
`R_(2r-1)`, `R_(2r)^3`, and `q_r^2`. A complete indexed Schreier inventory
has per-row length at most `100d(2d-2)^3+1`; its exponential indexing gives
no polynomial transporter diameter or cover.

## Frozen dependency gate

- All 60 payload rows in M112/M119, M135/M137, M284/M288, and M291/M294
  pass.
- M13's two observed proof hashes reproduce.
- No predecessor, coordinator, manuscript, project-skill, handoff, goal,
  agent-guide, or other worker file was edited.

## Frozen qualifications

1. The short local loops are not claimed to generate the full stabilizer.
2. The complete Schreier inventory is not a polynomial-size or
   polynomial-diameter theorem.
3. The pairwise double-coset test does not imply a higher-arity common
   transporter.
4. Finite action preserves nonemptiness but not literal representative
   length.
5. SSTID, every-color synchronization, voltage, congestion, every gap,
   mixing, and Terminal remain open.

## Frozen payload

- `plan.md`
- `checkpoint.md`
- `dependency_audit.md`
- `framed_stabilizer_transporter.md`
- `report.md`
- `audit_request.md`
- this `freeze_manifest.md`

`SHA256SUMS` is generated after this manifest, inventories every payload
above, and excludes itself.
