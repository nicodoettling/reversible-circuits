# Fresh immutable audit request for M296

Please audit frozen M296 independently and do not edit it.

## Required gates

1. Verify every M296 checksum and all predecessor inventories/top digests in
   `dependency_audit.md`.
2. Fix the chronological right-action convention and independently check the
   local doubled-star stabilizer formulas:

   ```text
   R_(2r-1) in S,       R_(2r)^3 in S,
   q_r=R_(2r);R_(2r-1);R_(2r+1);R_(2r),
   q_r(a,a,b,b)=(b,b,a,a),       q_r^2 in S.
   ```

   Confirm that `q_r` itself maps the chart to a global relabeling and is not
   silently treated as a literal chart stabilizer.
3. Reprove the Reidemeister--Schreier inventory without quotienting braid
   elements to actions. Check the telescope

   ```text
   s=product_i(t_(x_(i-1));g_i;t_(x_i)^(-1))
   ```

   and the per-row bound `100d(2d-2)^3+1`. Confirm that an exponentially
   indexed short-generator inventory gives no polynomial transporter
   diameter.
4. Audit the reference-edge orientation. Starting from
   `F_Q=alpha_Q;S;delta_Q^(-1)`, verify exactly

   ```text
   L_Q=alpha_Q^(-1);alpha_0,
   R_Q=delta_0^(-1);delta_Q,
   C_Q={s in S:L_Q;s;R_Q in S}
      =Trans_S(c^(L_Q),c^(R_Q^(-1))),

   intersection_Q F_Q
      =alpha_0;(intersection_Q C_Q);delta_0^(-1).
   ```
5. Independently derive the pairwise double-coset criterion

   ```text
   C_Q != empty iff S;L_Q;S=S;R_Q^(-1);S
   ```

   and its arbitrary-pair form. Check that this is an equality of literal
   braid double cosets, equivalently an orbit test for the literal point
   stabilizer.
6. Given `s_Q in C_Q`, rederive both transporter-coset orientations and the
   two-point stabilizers:

   ```text
   C_Q=Stab_S(x_Q);s_Q=s_Q;Stab_S(y_Q),
   Stab_S(y_Q)=S intersect R_Q;S;R_Q^(-1).
   ```
7. Verify frame covariance. If all frames are postcomposed by stabilizer
   elements, the residual sets must change by the same reference-dependent
   two-sided translate `C_Q'=u_0^(-1);C_Q;v_0`, independent of the
   nonreference changes.
8. Check that projection to the finite action preserves the complete common
   nonemptiness predicate because `S` is the full preimage of the finite
   point stabilizer. Enforce that it does not preserve shortest braid length.
9. Recheck both inequalities

   ```text
   |beta|<=2L_d+|s|,       |s|<=2L_d+|beta|,
   L_d=50d(2d-2)^3,
   ```

   so the polynomial representative condition is equivalent after
   residualization.
10. Enforce the nonimplications. Pairwise double-coset compatibility is only
    a necessary diagnostic for a whole class; no Helly theorem is claimed.
    The exact first open lemma is SSTID: a polynomial cover whose
    higher-arity transporter-coset intersections contain polynomial-length
    stabilizer representatives. No common-prefix cover, every-color route,
    rank lift, voltage, congestion, gap, mixing, or Terminal conclusion is
    accepted.

No finite enumeration is needed. A clean-room symbolic group-action audit is
preferred.
