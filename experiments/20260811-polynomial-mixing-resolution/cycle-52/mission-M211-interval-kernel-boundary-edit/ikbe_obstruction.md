# M211: rigorous obstruction to pointwise IKBE-b

Date: 2026-08-13 UTC.

Status: the pointwise clause IKBE-b, and therefore the conjunction called
IKBE in M199, is **refuted**. IKBE-a/DV and the signed averaged DE lemma
remain **unresolved**. No conditional J=2 or downstream conclusion is made.

## 1. Statement

Use M199/M207's audited notation, with

    D=2k-1, R=2k-3,
    b_d=e^(-d)d^(d-1)/d!,
    K_R(r,d)=b_d b_(r-d)/(R b_r),
    h(r)=(r-1)(r-2)/(rR),
    u=(k-1)/R.

Let Phi_s^D and Psi_s^D be the normalized B/A literal disjoint-double laws
and let Y_l count one-run faces of sizes 2 through l.

### Theorem (proved: bulk pointwise obstruction)

For every positive integer q put

    k_q=12q-1,  s_q=3q,  l_q=4q.

These parameters are admissible, and

    lim_(q to infinity)
      [Phi_(s_q)^D(Y_(l_q))-Psi_(s_q)^D(Y_(l_q))]
      = 7/64.                                           (1.1)

Consequently there is no universal C for which

    |Phi_s^D(Y_l)-Psi_s^D(Y_l)| <= C sqrt(l)/k

throughout the range asserted in IKBE-b. Thus the two-clause IKBE lemma is
false as stated.

## 2. Exact closed formulas

For a function f on child sizes define

    W_r(f)=sum_(d=1)^(r-1)(r-d-1)K_R(r,d)f(d).          (2.1)

Let F_l(x) be M199's two-seam incidence average and

    J_l(x)=(k-x)/k 1{2<=x<=l}.

Regrouping the exact M199 formulas, without approximation, gives

    Phi_s^D(Y_l)
      =[h(s)F_l(D-s)+h(D-s)F_l(s)
        +W_s(F_l)+W_(D-s)(F_l)]
        /[h(s)+h(D-s)],                                (2.2)

and

    Psi_s^D(Y_l)
      =[h(s)J_l(k-s)+h(k-s)J_l(s)
        +W_s(J_l)+W_(k-s)(J_l)
        +u(J_l(s)+J_l(k-s))+C_l]
        /[h(s)+h(k-s)+u],                              (2.3)

where

    C_l=sum_(d=1)^(k-1)(k-d)K_R(k,d)1{2<=d<=l}.        (2.4)

The denominator identities follow from the exact shared-endpoint deletion:

    h(s)+h(D-s)=1-gamma_L(s),
    h(s)+h(k-s)+u=1-gamma_F(s).                        (2.5)

## 3. Critical-Borel tail lemma

Put

    beta=sum_(d=2)^infinity b_d=1-e^(-1).              (3.1)

The equality uses the critical Borel normalization sum_d b_d=1 and
b_1=e^(-1).

### Lemma (proved)

Let k tend to infinity, R=2k-3, and let r=r_k satisfy
r/k -> rho in (0,2]. Suppose 0<=f_k(d)<=1 and, for every fixed d,

    f_k(d) -> 1{d>=2}.

Then

    W_r(f_k) -> (rho/2) beta.                           (3.2)

Moreover, if l=l_k tends to infinity with l<=k/2, then

    sum_(d=1)^(k-1)(k-d)K_R(k,d)1{2<=d<=l}
      -> beta/2.                                       (3.3)

### Proof

Stirling's formula supplies absolute constants c,C such that

    c m^(-3/2) <= b_m <= C m^(-3/2)                   (3.4)

for every m>=1. It also gives b_(r-d)/b_r ->1 for fixed d.

Fix M. For M<d<=r/2, (3.4) gives

    b_(r-d)/b_r <= C[r/(r-d)]^(3/2) <= C,

so the contribution to (2.1) is at most

    C sum_(d>M)b_d <= C M^(-1/2).                     (3.5)

For d>r/2 put c=r-d. Again (3.4) gives
b_(r-c)/b_r<=C, and that tail is at most

    C/R sum_(c<r/2)c b_c
      <= C sqrt(r)/R
      =O(k^(-1/2)).                                   (3.6)

For each fixed d, its summand in (2.1) converges to

    (rho/2)b_d 1{d>=2}.

First let k tend to infinity at fixed M, then use (3.5)--(3.6) and let
M tend to infinity. This proves (3.2).

For (3.3), fixed d has limiting coefficient b_d/2. Because l<=k/2,
only the analogue of (3.5) is needed for the tail; l tending to infinity
eventually includes every fixed d>=2. This proves (3.3). QED.

## 4. Evaluation of the witness

For k=12q-1,

    D=24q-3, R=24q-5, n=36q-3,
    s=3q, l=4q.

The parameters obey 1<=s<k/2 and
2<=l<=(3k-1)/2. Since s<k, M199's first seam law says that the gaps for an
s-step source arc are s, s+1, and s+k with multiplicities D-2s,s,s.
The cutoff includes the first two gaps and excludes the third. Hence

    F_l(s)=1-s/D.                                     (4.1)

For x=D-s the complementary length is s. M199's second seam law gives gaps
n-s,n-s-1,n-s-k, all exceeding l. Therefore

    F_l(D-s)=0.                                       (4.2)

The contiguous A law gives exactly

    J_l(s)=1-s/k,   J_l(k-s)=0.                       (4.3)

For every fixed d, both F_l(d) and J_l(d) tend to 1{d>=2}. Applying the
lemma at the four macroscopic parent sizes gives

    W_s(F_l)             -> beta/8,
    W_(D-s)(F_l)         -> 7beta/8,
    W_s(J_l)             -> beta/8,
    W_(k-s)(J_l)         -> 3beta/8,
    C_l                  -> beta/2.                   (4.4)

Thus the complete kernel contribution tends to beta on both sides. Also,

    h(s)       ->1/8,  h(D-s)->7/8,
    h(k-s)     ->3/8,  u->1/2,                        (4.5)

so both denominators in (2.2)--(2.3) tend to one. The remaining first-face
terms have limits

    h(D-s)F_l(s) -> (7/8)(7/8)=49/64,

    [h(k-s)+u]J_l(s)
      ->(3/8+1/2)(3/4)=42/64.                         (4.6)

Subtracting (4.4)--(4.6) proves (1.1).

Finally,

    sqrt(l_q)/k_q = 2sqrt(q)/(12q-1) ->0.

The positive limit 7/64 contradicts IKBE-b for every proposed universal
constant C. QED.

## 5. What is and is not refuted

- Refuted: pointwise IKBE-b for Y_l.
- Refuted: the conjunction named IKBE in M199, because one clause is false.
- Open: IKBE-a, equivalently DV.
- Open: the original signed averaged DE statement

      |sum_(s<k/2) q_hat_s
          [Phi_s^D(Z)-Psi_s^D(Z)]|
        <= C sqrt(l)/k.

The witness lies at a macroscopic split. It does not rule out the small
q_hat mass of that region, cancellation across s, or cancellation between
the combined literal profiles. Therefore DE itself is not refuted.

The corrected route is to prove the signed q_hat-averaged DE directly,
without the false pointwise strengthening. No counterterm or downstream
claim is proposed here.

## 6. Falsification and dependencies

The formula-only exact checker evaluates (2.2)--(2.4) at odd k<=11 and
checks both normalization identities. At q=1 (k,s,l)=(11,3,4), the defect
is the positive exact rational recorded in ikbe_formula_results.json,
approximately 0.0922412, already near 7/64. These finite values merely
calibrate the proved asymptotic calculation.

Proved inputs: M199's literal formulas, accepted by M207; elementary uniform
Stirling bounds; critical Borel normalization. No finite sign, topology
reconstruction, or unproved asymptotic inference is used.
