# M211 Checkpoint

## Start checkpoint

- The owned directory and plan were initialized before substantive work.
- Target: only the standalone two-clause IKBE estimate for the normalized
  literal disjoint-double profiles.
- M192/M195 and M199/M207 are immutable; their complete checksum gates are
  next.
- IKBE-a, IKBE-b, DV, DE, conditional J=2, and every downstream claim are
  open at start.
- Diagnostics are capped at odd k<=11 and will follow, not precede, an
  analytic formula.

## Immutable gate

- Every SHA256SUMS entry in M192, M195, M199, and M207 passed.
- Their checksum-file digests are, respectively:
  4c6cd295cd2a8259d396f8f9218e7f98746e7d005a255cfb4f14dc2d96336c60,
  1f0c398bd92edf37e16880c239e0bf65d63622e1de9c2c9904a26fd560d93f0a,
  1de555bba9affef15b7f2b9585de7955f9d9bd23fc838c76508186d7438c25ed,
  and 817988cd61ed290b6ce86e90510ee6e1a3358339bff5c8ca757c26acd2e1979d.
- All four predecessor missions remain unedited.

## Halfway substantive checkpoint: IKBE-b obstruction

- Write D=2k-1, R=D-2,
  h(r)=(r-1)(r-2)/(rR), u=(k-1)/R, and
  W_r(f)=sum_(d<r)(r-d-1)K_R(r,d)f(d).
  M199 gives

      Phi_s^D(Y_l) =
        [h(s)F_l(D-s)+h(D-s)F_l(s)
         +W_s(F_l)+W_(D-s)(F_l)]
        /[h(s)+h(D-s)],

      Psi_s^D(Y_l) =
        [h(s)J_l(k-s)+h(k-s)J_l(s)
         +W_s(J_l)+W_(k-s)(J_l)
         +u(J_l(s)+J_l(k-s))+C_l]
        /[h(s)+h(k-s)+u].

- For the exact sequence k=12q-1, s=3q, l=4q, the cutoff lies strictly
  between s and k-s. Hence F_l(D-s)=J_l(k-s)=0,
  F_l(s)=1-s/D, and J_l(s)=1-s/k.
- Uniform Borel tails imply that if r/k tends to rho>0 and the cutoff tends
  linearly to infinity, then

      W_r(F_l), W_r(J_l) -> (rho/2) beta,
      C_l -> beta/2,       beta=sum_(d>=2)b_d=1-e^-1.

  The proof splits d<=r/2, where
  b_(r-d)/b_r<=C and the tail is O(M^-1/2), from d>r/2, where c=r-d gives
  total O(r^-1/2). For fixed d both F_l(d),J_l(d) tend to 1{d>=2}.
- Therefore the total kernel terms converge to beta on both B and A, both
  normalizers converge to one, but the surviving-face terms differ by

      (1-1/8)^2 - (1-1/8)(1-1/4) = 7/64.

  Thus

      Phi_(3q)^D(Y_(4q)) - Psi_(3q)^D(Y_(4q)) -> 7/64,

  whereas sqrt(4q)/(12q-1) tends to zero.
- Conclusion: IKBE-b, hence the two-clause IKBE lemma as stated, is
  refuted. This is an analytic asymptotic obstruction, not finite-sign
  inference. IKBE-a remains open; no conditional J=2 or downstream claim
  follows.

## Final checkpoint

- The critical-Borel tail bound is formalized with uniform
  O(M^-1/2)+O(k^-1/2) control, and the exact 7/64 limit is proved.
- A formula-only exact checker, capped at k=3,5,7,9,11, reproduces the
  audited closed formulas and normalization identities. The q=1 witness
  (k,s,l)=(11,3,4) has positive defect approximately 0.0922412.
- Final verdict: pointwise IKBE-b and the two-clause IKBE conjunction are
  refuted. IKBE-a/DV and signed averaged DE remain open.
- The corrected route is precisely the original signed q_hat-averaged DE,
  not a pointwise estimate or a proposed counterterm.
- All immutable inputs remain unedited; no conditional J=2 or downstream
  claim is made.
