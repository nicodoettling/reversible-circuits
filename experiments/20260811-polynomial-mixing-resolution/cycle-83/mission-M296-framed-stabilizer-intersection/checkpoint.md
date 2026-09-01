# M296 Halfway Checkpoint

Status: halfway dependency and algebra audit complete.

- Mission scope and the literal/action/orbit/length type firewall are fixed
  in `plan.md`.
- The M291/M294 framed-fiber statement has been located; its accepted open
  interface is the exact common intersection of
  `alpha_Q;BStab_d;delta_Q^(-1)` over families of actual M135-selected
  `H`-orbit edges.
- All 60 frozen payload rows in M112/M119, M135/M137, M284/M288, and
  M291/M294 pass. M13's two observed proof hashes also reproduce. Exact
  provenance is in `dependency_audit.md`.
- With `Gamma=B_(2d-2)`, `S=BStab_d`, and a fixed reference edge `Q_0`,
  every candidate common schedule has the unique form

  ```text
  beta=alpha_0;s;delta_0^(-1),  s in S.
  ```

  For another edge `Q`, put
  `L_Q=alpha_Q^(-1);alpha_0` and
  `R_Q=delta_0^(-1);delta_Q`. Its exact residual constraint is the
  `S`-transporter

  ```text
  C_Q={s in S:L_Q;s;R_Q in S}
     =Trans_S(c_d^(L_Q),c_d^(R_Q^(-1))).
  ```

  Thus the full framed problem is an intersection of transporter cosets
  inside the chart stabilizer, not a common-prefix problem.
- Pairwise compatibility with the reference edge is equivalent to the exact
  double-coset equality

  ```text
  S L_Q S = S R_Q^(-1) S.
  ```

  If `s_Q in C_Q`, then
  `C_Q=s_Q [S intersect R_Q S R_Q^(-1)]`; the subgroup is the stabilizer in
  `S` of the relative target point. Higher-arity intersection, not this
  pairwise test, is the first remaining issue.
- The doubled-star chart has explicit short stabilizer loops:
  `R_(2r-1)` fixes each equal pair and `R_(2r)^3` fixes each adjacent pair
  of incident star edges. A complete Reidemeister--Schreier inventory can
  be chosen with every generator of length at most
  `100d(2d-2)^3+1`, but it has exponentially many rows. This supplies no
  polynomial transporter diameter or cover.
- No compact finite guard is needed: the reductions are exact group-action
  identities.
- No predecessor or coordinator file has been edited.
