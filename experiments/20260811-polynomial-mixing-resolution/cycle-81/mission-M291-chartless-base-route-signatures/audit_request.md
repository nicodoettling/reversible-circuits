# Fresh immutable audit request for M291

Please audit frozen M291 independently and do not edit it.

## Required gates

1. Verify every M291 checksum, then independently verify all frozen
   dependency inventories and top digests in `dependency_audit.md`, including
   M284 top digest
   `3176a4b175fd58f65ed2b71d81c5d2f1fc794cb9e7c7e2370ebcecaff19a62f3`.
2. Check M13 Claim D's applicability exactly: every `w_Q`,
   `tau_i(w_Q)`, and `c_d` has one connected labeled weighted support
   component `[d]` of weight `2d-2`.  Confirm that its displayed
   `50Nm^3` bound gives each frame length at most
   `50d(2d-2)^3`; do not infer any flow or congestion statement.
3. Verify that
   `c_d=(1,2)^2(1,3)^2...(1,d)^2` is the locked M278 canonical-slot word
   for the star rooted at leaf `d` with root edge `{1,d}`, hence a valid
   doubled-tree extension source chart.
4. Recheck chronological orientation in the exact literal braid identity

   ```text
   Ktilde_Q=alpha_Q;BStab_d;delta_Q^(-1).
   ```

   In particular, `alpha_Q^(-1);beta;delta_Q` must fix `c_d`, and changing
   either normalization frame must leave the displayed set invariant.
5. Check the actual arbitrary-color edge quantifier: `tau_i` is
   `H`-equivariant and braid actions commute with relabeling, so the
   individual word `alpha_Q;delta_Q^(-1)` realizes the entire selected
   `H`-orbit edge, not merely one preferred representative.
6. Audit the word/action firewall.  At this fixed rank, prove both

   ```text
   p_d(Ktilde_Q)=K_Q,
   p_d(intersection_Q Ktilde_Q)=intersection_Q K_Q,
   ```

   by lifting one common global action.  Also verify that this equality
   supplies neither shortest braid length nor an action-image embedding
   across ranks and does not alter M284's literal `j_d` theorem.
7. Recompute the two cardinalities without importing M291 arithmetic:

   ```text
   |P_d|=d^(d-2)(d-1)!,
   |C|=(|Z_d|/d!)(d-1)!=d^(d-4)(2d-2)!.
   ```

   The second count must use exactly one physical `H`-orbit over each left
   global orbit in the chosen perfect-matching color.
8. Check the injective-action union bound and every quantifier in the named
   common-prefix cover: overlapping arbitrary subsets are allowed, prefix
   length is unlimited, and different members of one class may land in
   different paired trees.  Verify

   ```text
   q>=|C|/|P_d|=(2d-2)!/[d^2(d-1)!]>=d^(d-3).
   ```
9. Enforce the decisive nonimplication.  The bound in Gate 8 is only for a
   common source prefix landing in the broad paired-tree set (or the inverse
   target-suffix version).  It is **not** a lower bound on genuine common
   schedule classes because the source and target frames can cancel through
   different elements of `BStab_d`.
10. Confirm that the exact remaining obligation is the framed-stabilizer
    common-intersection with polynomial literal representatives.  No
    every-color common-schedule theorem, local rank lift, voltage,
    congestion, gap, mixing, or Terminal claim is present.

The most important possible objections are misuse of M13's component
hypothesis, an incorrect `|C|/|P_d|` factor, a false same-rank
action-image intersection qualification, or leakage from the prefix-cover
lower bound to the true M135 schedule cover.  No broad enumeration is
needed: a clean-room symbolic and cardinality audit is preferred.
